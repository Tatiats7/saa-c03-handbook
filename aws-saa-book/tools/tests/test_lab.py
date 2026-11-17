"""Tests of saalib/lab.py (`saa.py tasks ...`). Offline: the uv helpers are patched, except one test
that runs the real CLI model helper with `uv run --offline` (skipped when the cache has no awscli)."""
import argparse
import os
import shutil
import unittest
from unittest import mock

import sandbox
from saalib import common, lab, schemas

T2 = 1  # index of sample-t02 (the Try) in the fixture tasks.json


class LabCase(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("lab-" + self.id().split(".")[-1])
        self.tasks = self.book / "data" / "99-sample" / "tasks.json"

    def tearDown(self):
        sandbox.remove(self.book)

    def change(self, fn):
        def apply(doc):
            fn(doc["items"])        # the return value of fn is ignored: fn changes the items in place
        sandbox.edit_json(self.tasks, apply)

    def lint(self, ship=False):
        with sandbox.paths(self.book):
            return lab.lint_chapter(common.chapter("99"), ship=ship)

    def codes(self, ship=False):
        return [f["code"] for f in self.lint(ship)["errors"]]

    def assert_fails(self, code, fn):
        self.change(fn)
        code_cli, result, err = sandbox.run_json(self.book, "tasks", "lint", "99")
        self.assertEqual(code_cli, 1, err)
        self.assertIn(code, [f["code"] for f in result["errors"]])
        return result

    def ctx(self):
        return lab._Ctx(common.chapter("99"))


class LintFixture(LabCase):
    def test_fixture_passes_without_ship(self):
        code, result, err = sandbox.run_json(self.book, "tasks", "lint", "99")
        self.assertIn(code, (0, 2), err)
        self.assertEqual(result["errors"], [])
        self.assertTrue(result["ok"])
        self.assertEqual(result["counts"]["total"], 2)
        self.assertEqual([f["code"] for f in result["warnings"]], ["T113"])

    def test_text_output_is_short(self):
        code, out, err = sandbox.run(self.book, "tasks", "lint", "99")
        self.assertEqual(code, 2, err)
        self.assertTrue(out.startswith("WARN tasks lint"))
        self.assertLessEqual(len(out.splitlines()), 41)

    def test_gate_matches_schema(self):
        with sandbox.paths(self.book):
            gate = lab.gate_tasks("99")
            self.assertEqual(schemas.validate(gate, "gate"), [])
        self.assertTrue(gate["ok"])
        self.assertEqual(gate["exit"], 2)
        self.assertIn("data/99-sample/tasks.json", [i["path"] for i in gate["inputs"]])

    def test_must_fail_ship_without_cli_report(self):
        code, result, err = sandbox.run_json(self.book, "tasks", "lint", "99", "--ship")
        self.assertEqual(code, 1, err)
        self.assertEqual([f["code"] for f in result["errors"]], ["T113"])

    def test_lint_all(self):
        code, result, err = sandbox.run_json(self.book, "tasks", "lint", "--all")
        self.assertEqual(code, 2, err)
        self.assertEqual(result["counts"]["chapters"], 1)

    def test_must_fail_book_cost_over_the_maximum(self):
        sandbox.edit_json(self.book / "_build" / "style" / "SPEC.json", lambda s: s["tasks"].update({"book_cost_usd_max": -1}))
        code, result, err = sandbox.run_json(self.book, "tasks", "lint", "--all")
        self.assertEqual(code, 1, err)       # the fixture costs $0, which is over a maximum of -1
        self.assertEqual([f["code"] for f in result["errors"]], ["T119"])


class MustFail(LabCase):
    def test_must_fail_try_without_cleanup(self):
        self.assert_fails("T103", lambda items: items[T2].update({"cleanup": []}))

    def test_must_fail_missing_cost_line(self):
        self.assert_fails("T103", lambda items: items[T2].pop("cost"))

    def test_must_fail_missing_cost_if_forgotten(self):
        self.assert_fails("T103", lambda items: items[T2].update({"cost_if_forgotten": "nothing"}))

    def test_must_fail_missing_verify_step(self):
        self.assert_fails("T103", lambda items: items[T2].update({"verify": None}))

    def test_must_fail_look_that_creates(self):
        def fn(items):
            items[0]["steps"][1]["command"] = "aws widget create-shelf --name saa-x --tags book=saa,task=sample-t01"
        self.assert_fails("T103", fn)

    def test_must_fail_create_without_matching_delete(self):
        result = self.assert_fails("T107", lambda items: items[T2]["cleanup"].pop())
        self.assertNotIn("T103", [f["code"] for f in result["errors"]])

    def test_must_fail_cleanup_in_creation_order(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = "aws widget create-rack --name saa-sample-rack --tags book=saa,task=sample-t02"
            items[T2]["cleanup"][0]["command"] = "aws widget delete-shelf --name saa-sample-shelf"
            items[T2]["cleanup"][1]["command"] = "aws widget delete-rack --name saa-sample-rack"
        result = self.assert_fails("T107", fn)
        self.assertIn("reverse order", " ".join(f["msg"] for f in result["errors"]))

    def test_cleanup_in_reverse_order_passes(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = "aws widget create-rack --name saa-sample-rack --tags book=saa,task=sample-t02"
            items[T2]["cleanup"][0]["command"] = "aws widget delete-racks --name saa-sample-rack"
            items[T2]["cleanup"][1]["command"] = "aws widget delete-shelf --name saa-sample-shelf"
        self.change(fn)
        self.assertEqual(self.codes(), [])

    def test_launch_template_option_is_not_a_second_create(self):
        task = {"steps": [{"text": "x", "command": "aws ec2 run-instances --launch-template LaunchTemplateName=saa-lt --count 1"}],
                "cleanup": [{"text": "x", "command": "aws ec2 terminate-instances --instance-ids $ID"}]}
        with sandbox.paths(self.book):
            self.assertEqual(lab._pairing(self.ctx(), task), [])
            task["cleanup"] = []
            self.assertEqual(len(lab._pairing(self.ctx(), task)), 1)

    def test_must_fail_missing_tag(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = "aws widget create-shelf --name saa-sample-shelf"
        self.assert_fails("T106", fn)

    def test_must_fail_tag_of_another_task(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = "aws widget create-shelf --name saa-sample-shelf --tags book=saa,task=sample-t09"
        self.assert_fails("T106", fn)

    def test_key_value_tag_syntax_passes(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = ("aws widget create-shelf --name saa-sample-shelf "
                                                "--tags Key=book,Value=saa Key=task,Value=sample-t02")
        self.change(fn)
        self.assertEqual(self.codes(), [])

    def test_must_fail_security_group_port_22(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = ("aws ec2 authorize-security-group-ingress --group-id sg-1 "
                                                "--protocol tcp --port 22 --cidr 10.0.0.0/8")
        self.assert_fails("T105", fn)

    def test_must_fail_admin_ports_open_to_the_world(self):
        bad = [
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --protocol tcp --port 22 --cidr 0.0.0.0/0",
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --protocol tcp --port 3389 --cidr 0.0.0.0/0",
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --ip-permissions "
            "'IpProtocol=tcp,FromPort=3389,ToPort=3389,Ipv6Ranges=[{CidrIpv6=::/0}]'",
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --ip-permissions "
            "'IpProtocol=tcp,FromPort=22,ToPort=22,Ipv6Ranges=[{CidrIpv6=::/0}]'",
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --ip-permissions "
            "'IpProtocol=tcp,FromPort=0,ToPort=65535,IpRanges=[{CidrIp=0.0.0.0/0}]'",
            "aws ec2 authorize-security-group-ingress --group-id sg-1 --ip-permissions "
            "'IpProtocol=-1,IpRanges=[{CidrIp=0.0.0.0/0}]'",
        ]
        with sandbox.paths(self.book):
            ctx = self.ctx()
            for command in bad:
                self.assertTrue(lab._banned(ctx, command), command)
            ok = "aws ec2 authorize-security-group-ingress --group-id sg-1 --protocol tcp --port 443 --source-group sg-2"
            self.assertEqual(lab._banned(ctx, ok), [])

    def test_must_fail_public_bucket_acl(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = "aws s3api put-bucket-acl --bucket saa-sample --acl public-read"
        self.assert_fails("T105", fn)

    def test_must_fail_public_access_block_off(self):
        bad = [
            "aws s3api put-public-access-block --bucket saa-x --public-access-block-configuration "
            "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=true",
            "aws s3api put-public-access-block --bucket saa-x --public-access-block-configuration BlockPublicAcls=false",
            "aws s3api delete-public-access-block --bucket saa-x",
            "aws s3api put-object-acl --bucket saa-x --key a --acl public-read-write",
            "aws s3api put-bucket-acl --bucket saa-x --grant-read uri=http://acs.amazonaws.com/groups/global/AllUsers",
        ]
        with sandbox.paths(self.book):
            ctx = self.ctx()
            for command in bad:
                self.assertTrue(lab._banned(ctx, command), command)
            ok = ("aws s3api put-public-access-block --bucket saa-x --public-access-block-configuration "
                  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true")
            self.assertEqual(lab._banned(ctx, ok), [])

    def test_must_fail_access_key_creation(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = "aws iam create-access-key --user-name saa-user"
        self.assert_fails("T105", fn)

    def test_must_fail_aws_configure(self):
        def fn(items):
            items[T2]["steps"][2]["command"] = "aws configure"
        self.assert_fails("T105", fn)

    def test_must_fail_variable_without_capture(self):
        def fn(items):
            items[T2]["cleanup"][1]["command"] = "aws widget delete-shelf --name saa-sample-shelf --vpc $VPC_ID"
        self.assert_fails("T115", fn)

    def test_captured_variable_passes(self):
        def fn(items):
            items[T2]["steps"][0]["capture"] = {"name": "SHELF_ID", "query": "Shelf.Id"}
            items[T2]["cleanup"][1]["command"] = "aws widget delete-shelf --name saa-sample-shelf --shelf-id $SHELF_ID"
        self.change(fn)
        self.assertEqual(self.codes(), [])

    def test_must_fail_break_it_without_explain(self):
        self.assert_fails("T110", lambda items: items[T2]["steps"][1].pop("explain"))

    def test_must_fail_break_it_explain_links_a_fact_outside_facts(self):
        self.assert_fails("T110", lambda items: items[T2].update({"facts": []}))

    def test_must_fail_cost_without_fact(self):
        self.assert_fails("T109", lambda items: items[T2].update({"cost": "$0.05"}))

    def test_must_fail_pipe(self):
        def fn(items):
            items[T2]["verify"]["command"] = "aws widget list-shelves --tag book=saa | wc -l"
        self.assert_fails("T104", fn)

    def test_pipe_inside_a_quoted_query_passes(self):
        def fn(items):
            items[T2]["verify"]["command"] = "aws widget list-shelves --tag book=saa --query 'Shelves[] | length(@)'"
        self.change(fn)
        self.assertEqual(self.codes(), [])

    def test_must_fail_command_form(self):
        bad = ["aws s3 ls && aws s3 ls", "aws s3 ls; aws s3 ls", "aws s3 ls --profile dev", "sudo aws s3 ls", "ls -la",
               "aws ec2 describe-instances --instance-ids $(cat ids)", "aws ec2 describe-instances --query \"a[?b==`c`]\"",
               "curl -X POST https://example.com", "curl http://example.com", "aws s3api get-object --bucket <BUCKET> --key a out"]
        with sandbox.paths(self.book):
            ctx = self.ctx()
            for command in bad:
                self.assertTrue(lab._form_errors(ctx, command, ""), command)
            self.assertEqual(lab._form_errors(ctx, "aws s3api head-bucket --bucket <BUCKET>", "Use your bucket name for <BUCKET>."), [])
            self.assertEqual(lab._form_errors(ctx, "curl -sI https://example.com", ""), [])

    def test_must_fail_wrong_label(self):
        self.assert_fails("T101", lambda items: items[T2].update({"label": "run in a real account"}))

    def test_must_fail_unknown_trap(self):
        self.assert_fails("T111", lambda items: items[T2].update({"trap": "sample-trap-not-there"}))

    def test_must_fail_section_that_does_not_resolve(self):
        self.assert_fails("T111", lambda items: items[T2].update({"section": "2-deep.md#no-such-section"}))

    def test_must_fail_verify_without_tag_filter(self):
        def fn(items):
            items[T2]["verify"]["command"] = "aws widget list-shelves --all-regions"
        self.assert_fails("T108", fn)

    def test_must_fail_banned_word(self):
        def fn(items):
            items[T2]["steps"][0]["text"] = "Simply create a shelf with the name saa-sample-shelf."
        self.assert_fails("T112", fn)

    def test_must_fail_template_on_a_try(self):
        self.assert_fails("T120", lambda items: items[T2].update({"template": "data/99-sample/templates/sample-t02.yaml"}))

    def test_must_fail_look_on_the_pass_route(self):
        self.assert_fails("T201", lambda items: items[0].update({"pass_route": True}))

    def test_must_fail_ship_counts(self):
        self.change(lambda items: items[0].update({"status": "candidate"}))
        self.assertIn("T201", self.codes(ship=True))
        self.assertNotIn("T201", self.codes(ship=False))

    def test_warnings_name_and_click_path(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = "aws widget create-shelf --name my-shelf --tags book=saa,task=sample-t02"
            items[T2]["steps"][0]["text"] = "Click Shelves > Create and make a shelf."
            items[T2]["cleanup"][1]["command"] = "aws widget delete-shelf --name my-shelf"     # T107: the same resource
        self.change(fn)
        result = self.lint()
        self.assertEqual(result["errors"], [])
        self.assertLessEqual({"T116", "T117"}, {f["code"] for f in result["warnings"]})


class CheckCli(LabCase):
    @staticmethod
    def fake(ok=True, error="unknown service widget", tags=("--tags",)):
        def run(commands):
            return [{"command": c, "service": "widget", "operation": c.split()[2], "ok": ok,
                     "errors": [] if ok else [error], "tag_options": list(tags)} for c in commands]
        return run

    def test_must_fail_unknown_service(self):
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_helper", self.fake(ok=False)):
            code, report = lab.check_cli("99")
            self.assertEqual(code, 1)
            self.assertFalse(report["ok"])
            stored = common.read_json(common.REPORTS / "cli" / "99.json")
            self.assertEqual(stored["commands_sha256"], lab.commands_sha256(common.read_json(self.tasks)))
            self.assertEqual(stored["awscli"], lab.pinned_version("cli_model.py", "awscli"))
            self.assertIn("T113", [f["code"] for f in lab.lint_chapter(common.chapter("99"), ship=True)["errors"]])

    def test_must_fail_unknown_option(self):
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_helper", self.fake(ok=False, error="unknown option --tag")):
            args = argparse.Namespace(chapter="99", all=False, reference=False, json=True, out=None, max_lines=0)
            with mock.patch.object(common, "emit"):
                self.assertEqual(lab.cmd_check_cli(args), 1)

    def test_ok_report_clears_t113_until_a_command_changes(self):
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_helper", self.fake()):
            code, report = lab.check_cli("99")
            self.assertEqual(code, 0)
            self.assertEqual(len(report["commands"]), len(set(lab.chapter_commands(common.read_json(self.tasks)))))
            self.assertEqual(lab.lint_chapter(common.chapter("99"), ship=True)["errors"], [])
            self.change(lambda items: items[T2]["verify"].update({"command": "aws widget list-shelves --tag book=saa"}))
            self.assertEqual([f["code"] for f in lab.lint_chapter(common.chapter("99"), ship=True)["errors"]], ["T113"])

    def test_tag_model_warning(self):
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_helper", self.fake(tags=())):
            code, report = lab.check_cli("99")
            self.assertEqual(code, 0)
            self.assertIn("T118", [f["code"] for f in report["warnings"]])

    def test_must_fail_helper_cannot_run(self):
        def broken(commands):
            raise lab.HelperError("uv is not there")
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_helper", broken):
            code, report = lab.check_cli("99")
            self.assertEqual(code, 5)
            self.assertFalse((common.REPORTS / "cli" / "99.json").exists())

    def test_must_fail_real_model_unknown_option(self):
        """The real helper, from the uv cache only (no network request)."""
        if not shutil.which("uv"):
            self.skipTest("uv is not installed")
        commands = ["aws ec2 run-instances --image-id ami-1 --launch-template LaunchTemplateName=saa-lt",
                    "aws ec2 run-instances --image-idd ami-1",
                    "aws widget list-shelves",
                    "aws ec2 make-coffee",
                    "aws s3api put-bucket-tagging --bucket saa-x"]
        with mock.patch.dict(os.environ, {"SAA_UV_OFFLINE": "1"}):
            try:
                rows = lab._run_helper(commands)
            except lab.HelperError as exc:
                self.skipTest(f"awscli is not in the uv cache: {exc}")
        self.assertEqual([r["ok"] for r in rows], [True, False, False, False, False])
        self.assertIn("unknown option --image-idd", rows[1]["errors"][0])
        self.assertIn("unknown service widget", rows[2]["errors"][0])
        self.assertIn("unknown operation make-coffee", rows[3]["errors"][0])
        self.assertIn("missing required option --tagging", rows[4]["errors"][0])


class AddAndStatus(LabCase):
    def new_task(self, **changes):
        task = dict(common.read_json(self.tasks)["items"][T2])
        for key in ("id", "status", "rev", "label", "checked", "chapter"):
            task.pop(key)
        task["pass_route"] = False
        task["title"] = "Copy a shelf to a second Region"
        text = __import__("json").dumps(task).replace("sample-t02", "sample-t03")
        task = __import__("json").loads(text)
        task.update(changes)
        path = self.book / "_build" / "work" / "new-task.json"
        common.write_json(path, task)
        return path

    def test_add_sets_the_tool_fields(self):
        path = self.new_task(id="sample-t03")
        code, result, err = sandbox.run_json(self.book, "tasks", "add", "--chapter", "99", "--file", str(path))
        self.assertEqual(code, 0, err)
        self.assertEqual(result["added"], ["sample-t03"])
        stored = common.read_json(self.tasks)["items"][-1]
        self.assertEqual((stored["status"], stored["rev"], stored["chapter"]), ("candidate", 1, "sample"))
        self.assertEqual(stored["label"], "checked against docs, not run in a real account")
        self.assertEqual(stored["checked"], common.today())

    def test_must_fail_add_untagged_create(self):
        path = self.new_task(id="sample-t03")
        sandbox.replace_text(path, "--tags book=saa,task=sample-t03", "")
        code, result, err = sandbox.run_json(self.book, "tasks", "add", "--chapter", "99", "--file", str(path))
        self.assertEqual(code, 1, err)
        self.assertIn("T106", [f["code"] for f in result["rejected"][0]["errors"]])
        self.assertEqual(len(common.read_json(self.tasks)["items"]), 2)

    def test_must_fail_add_existing_id_without_replace(self):
        path = self.new_task(id="sample-t02")
        code, result, err = sandbox.run_json(self.book, "tasks", "add", "--chapter", "99", "--file", str(path))
        self.assertEqual(code, 1, err)
        self.assertEqual(result["rejected"][0]["errors"][0]["code"], "T101")

    def test_replace_a_ready_task(self):
        task = dict(common.read_json(self.tasks)["items"][T2])
        task["minutes"] = 12
        path = self.book / "_build" / "work" / "replace.json"
        common.write_json(path, task)
        code, result, err = sandbox.run_json(self.book, "tasks", "add", "--chapter", "99", "--file", str(path), "--replace")
        self.assertEqual(code, 0, err)
        self.assertEqual(result["replaced"], ["sample-t02"])
        stored = common.read_json(self.tasks)["items"][T2]
        self.assertEqual((stored["status"], stored["rev"], stored["minutes"]), ("candidate", 2, 12))

    def test_must_fail_file_outside_the_book(self):
        code, out, err = sandbox.run(self.book, "tasks", "add", "--chapter", "99", "--file", "/tmp/task.json")
        self.assertEqual(code, 4)

    def test_must_fail_set_ready_on_a_broken_task(self):
        self.change(lambda items: items[T2].update({"status": "candidate", "verify": None}))
        code, result, err = sandbox.run_json(self.book, "tasks", "set-status", "--chapter", "99", "--status", "ready", "sample-t02")
        self.assertEqual(code, 1, err)
        self.assertIn("T103", [f["code"] for f in result["refused"][0]["errors"]])
        self.assertEqual(common.read_json(self.tasks)["items"][T2]["status"], "candidate")

    def test_set_status(self):
        self.change(lambda items: items[T2].update({"status": "candidate"}))
        code, result, err = sandbox.run_json(self.book, "tasks", "set-status", "--chapter", "99", "--status", "ready", "sample-t02")
        self.assertEqual(code, 0, err)
        self.assertEqual(result["set"], ["sample-t02"])
        code, result, err = sandbox.run_json(self.book, "tasks", "set-status", "--chapter", "99", "--status", "retired", "sample-t02")
        self.assertEqual(code, 1, err)       # no --reason


class Emulate(LabCase):
    def test_placeholder_is_not_supported(self):
        def fn(items):
            items[T2]["steps"][0]["command"] += " --owner <ACCOUNT_ID>"
            items[T2]["steps"][0]["text"] += " Use your account id for <ACCOUNT_ID>."
        self.change(fn)
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_emulator", side_effect=AssertionError("must not run")):
            report = lab.emulate_task(common.read_json(self.tasks)["items"][T2])
        self.assertEqual(report["result"], "not-supported")

    def test_must_fail_emulation_report_with_fail(self):
        def fake(payload):
            self.assertEqual(len(payload["steps"]), 3)
            self.assertTrue(payload["steps"][1]["break_it"])
            return {"task": payload["task"], "result": "fail", "steps": [{"command": "x", "rc": 255, "ok": False}], "note": "step failed"}
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_emulator", fake), mock.patch.object(common, "emit"):
            args = argparse.Namespace(chapter="99", task="sample-t02", json=True, out=None, max_lines=0)
            self.assertEqual(lab.cmd_emulate(args), 1)
            self.assertIn("T114", [f["code"] for f in lab.lint_chapter(common.chapter("99"))["errors"]])

    def test_must_fail_emulator_cannot_start(self):
        def broken(payload):
            raise lab.HelperError("no uv")
        with sandbox.paths(self.book), mock.patch.object(lab, "_run_emulator", broken):
            args = argparse.Namespace(chapter="99", task="sample-t02", json=True, out=None, max_lines=0)
            self.assertEqual(lab.cmd_emulate(args), 5)


if __name__ == "__main__":
    unittest.main()
