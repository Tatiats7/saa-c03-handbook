"""Tests of saalib/ledger.py: stage, gate, status, report, selftest (TOOLS.md section 3).

Every test works in its own sandbox copy of the fixture book and runs in-process, so that the
gates of other modules can be replaced by fakes (ledger._module is patched).
"""
import argparse
import contextlib
import io
import json
import types
import unittest
from unittest import mock

import sandbox
from saalib import common, ledger, schemas

FINALIZE = ["facts-final", "lint", "sync", "questions-verified", "cards", "speak", "tasks", "diagrams",
            "findings-closed", "counts"]
BULLETS = ["1.1.K1", "1.1.K2", "1.1.S1", "2.1.K1", "2.1.K2", "2.1.S1", "2.1.S2", "2.2.K1", "2.2.S1", "3.1.K1",
           "3.1.S1", "4.1.K1", "4.1.S1"]


def fake_gate(gate, errors=(), warnings=(), inputs=()):
    def fn(ch_id, quick=False, **options):
        files = [{"path": p, "sha256": common.sha256_file(common.BOOK / p)} for p in inputs]
        return {"gate": gate, "chapter": ch_id, "ok": not errors, "exit": 1 if errors else (2 if warnings else 0),
                "errors": list(errors), "warnings": list(warnings), "counts": {}, "inputs": files}
    return fn


def fake_modules(**overrides):
    """Passing fakes of every gate of facts, lint, qbank and lab; `overrides` maps a gate name to a function."""
    hand = ["99-sample/1-fast.md", "99-sample/2-deep.md"]
    table = {}
    for gate, (mod, fn) in ledger.EXTERNAL_GATES.items():
        files = hand if mod == "lint" else ["data/facts/widget.jsonl"] if mod == "facts" else []
        table.setdefault(mod, {})[fn] = overrides.get(gate) or fake_gate(gate, inputs=files)
    modules = {name: types.SimpleNamespace(**fns) for name, fns in table.items()}
    real = ledger._module
    return lambda name: modules[name] if name in modules else real(name)


def brief(**changes):
    doc = {"chapter": "99",
           "sections": [{"file": "2-deep.md", "section": "how-it-works", "heading": "How it works", "bullets": list(BULLETS),
                         "facts": ["widget-shelf-max-widgets"]}],
           "traps": [{"id": "sample-trap-shelf-move", "belief": "A shelf can move.", "truth": "It cannot.",
                      "facts": ["widget-shelf-move"]}],
           "question_slots": [{"bullet": b, "concept": "shelf", "difficulty": "core", "type": "single", "layer": "core",
                               "exam_english": []} for b in BULLETS],
           "terms": ["shelf"], "tasks": [], "diagrams": []}
    doc.update(changes)
    return doc


class LedgerCase(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("ledger-" + self.id().split(".")[-1])
        self.addCleanup(sandbox.remove, self.book)
        self.enterContext(sandbox.paths(self.book))

    def cli(self, *argv):
        parser = argparse.ArgumentParser()
        ledger.register(parser.add_subparsers(dest="cmd"))
        args = parser.parse_args([*argv, "--json"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            try:
                code = args.func(args)
            except SystemExit as exc:
                code = exc.code
        try:
            return code, json.loads(out.getvalue())
        except ValueError:
            return code, None

    def led(self):
        doc = common.read_json(self.book / "_build" / "ledger" / "chapters" / "99.json")
        self.assertEqual(schemas.validate(doc, "ledger-chapter"), [])
        return doc

    def fakes(self, **overrides):
        self.enterContext(mock.patch.object(ledger, "_module", fake_modules(**overrides)))

    def write_brief(self, **changes):
        common.write_json(self.book / "_build" / "work" / "99-sample" / "brief.json", brief(**changes))

    def write_findings(self, lens, findings):
        common.write_json(self.book / "_build" / "work" / "99-sample" / "findings" / f"{lens}.json",
                          {"lens": lens, "chapter": "99", "findings": findings})

    def set_stages(self, names, status="pass"):
        def change(doc):
            for name in names:
                doc["stages"][name] = {"status": status, "attempts": 0, "pass_seq": 1, "inputs_hash": None}
            doc["status"] = ledger._status_of(doc)
        sandbox.edit_json(self.book / "_build" / "ledger" / "chapters" / "99.json", change)

    def drafted(self):
        self.set_stages(["brief", "prose", "questions", "tasks", "cards", "speak", "diagrams", "edit"])
        self.assertEqual(self.led()["status"], "drafted")

    def pass_stage(self, stage):
        code, res = self.cli("stage", "begin", "99", stage)
        self.assertEqual(res["decision"], "GO", res)
        code, res = self.cli("stage", "end", "99", stage)
        self.assertEqual(res["result"], "PASS", res)
        return code, res


class StageBegin(LedgerCase):
    def test_fixture_passed_stage_answers_go_inputs_changed(self):
        code, res = self.cli("stage", "begin", "99", "plan")
        self.assertEqual((code, res), (0, {"decision": "GO", "chapter": "99", "stage": "plan", "attempt": 1,
                                           "reason": "inputs-changed"}))
        self.assertEqual(self.led()["stages"]["plan"]["status"], "running")

    def test_must_fail_begin_with_unmet_prerequisite_is_blocked(self):
        code, res = self.cli("stage", "begin", "sample", "prose")
        self.assertEqual(code, 3)
        self.assertEqual((res["decision"], res["reason"]), ("BLOCKED", "prereq:brief"))
        self.assertNotIn("prose", self.led()["stages"])          # no attempt is used

    def test_must_fail_unknown_stage_or_chapter_exits_3(self):
        self.assertEqual(self.cli("stage", "begin", "99", "render")[0], 3)
        self.assertEqual(self.cli("stage", "begin", "42", "plan")[0], 3)

    def test_skip_when_inputs_are_unchanged(self):
        code, res = self.pass_stage("plan")
        self.assertEqual(code, 0)
        self.assertEqual(self.led()["stages"]["plan"]["pass_seq"], 2)
        code, res = self.cli("stage", "begin", "99", "plan")
        self.assertEqual((code, res["decision"], res["reason"]), (0, "SKIP", "already-passed"))
        self.assertEqual(self.led()["stages"]["plan"]["status"], "pass")

    def test_must_fail_begin_after_prerequisite_passed_again_is_go_not_skip(self):
        self.fakes()
        self.pass_stage("plan")
        self.pass_stage("mine")
        self.assertEqual(self.cli("stage", "begin", "99", "mine")[1]["decision"], "SKIP")
        self.cli("stage", "reset", "99", "plan", "--reason", "new sources")
        self.pass_stage("plan")
        self.assertEqual(self.led()["stages"]["mine"]["status"], "stale")
        code, res = self.cli("stage", "begin", "99", "mine")
        self.assertEqual((res["decision"], res["reason"]), ("GO", "stale"))

    def test_not_applicable_stage_is_skipped(self):
        def change(spec):
            spec["templates"]["deep"]["counts"]["speak"]["count"] = 0
        sandbox.edit_json(self.book / "_build" / "style" / "SPEC.json", change)
        code, res = self.cli("stage", "begin", "99", "speak")
        self.assertEqual((code, res["decision"], res["reason"]), (0, "SKIP", "not-applicable"))
        self.assertEqual(self.led()["stages"]["speak"]["status"], "na")


class StageEnd(LedgerCase):
    def test_must_fail_end_when_the_gate_fails(self):
        self.cli("stage", "reset", "99", "brief", "--reason", "test")
        self.assertEqual(self.cli("stage", "begin", "99", "brief")[1]["decision"], "GO")
        code, res = self.cli("stage", "end", "99", "brief")              # the fixture has no brief.json
        self.assertEqual(code, 1)
        self.assertEqual(res["result"], "FAIL")
        self.assertEqual(res["errors"][0]["code"], "B01")
        stage = self.led()["stages"]["brief"]
        self.assertEqual((stage["status"], stage["attempts"]), ("fail", 1))
        self.assertTrue(stage["reason"].split(": ")[-1].startswith("B01"))
        record = common.read_json(self.book / "_build" / "ledger" / "gates" / "99.brief.json")
        self.assertEqual(schemas.validate(record, "gate"), [])
        self.assertFalse(record["ok"])

    def test_must_fail_fourth_attempt_is_blocked(self):
        self.cli("stage", "reset", "99", "brief", "--reason", "test")
        for attempt in (1, 2, 3):
            code, res = self.cli("stage", "begin", "99", "brief")
            self.assertEqual((res["decision"], res["attempt"]), ("GO", attempt))
            self.assertEqual(self.cli("stage", "end", "99", "brief")[0], 1)
        code, res = self.cli("stage", "begin", "99", "brief")
        self.assertEqual((code, res["decision"], res["reason"]), (3, "BLOCKED", "attempts"))
        doc = self.led()
        self.assertEqual(doc["status"], "blocked")
        self.assertEqual(doc["blocked"]["stage"], "brief")
        self.assertEqual(self.cli("stage", "reset", "99", "brief", "--reason", "brief repaired")[0], 0)
        self.assertEqual(self.led()["status"], "facts-verified")
        self.assertEqual(self.cli("stage", "begin", "99", "brief")[1]["decision"], "GO")

    def test_must_fail_end_on_a_stage_that_is_not_running_exits_3(self):
        code, res = self.cli("stage", "end", "99", "plan")
        self.assertEqual(code, 3)
        self.assertEqual(self.led()["stages"]["plan"]["status"], "pass")

    def test_fail_option_records_a_failure_without_gates(self):
        self.cli("stage", "begin", "99", "plan")
        code, res = self.cli("stage", "end", "99", "plan", "--fail", "fetch failed")
        self.assertEqual((code, res["result"], res["gates"]), (1, "FAIL", []))
        self.assertEqual(self.led()["stages"]["plan"]["reason"], "fetch failed")

    def test_pass_stores_counts_warnings_and_exits_2(self):
        warning = {"code": "W307", "file": "99-sample/2-deep.md", "line": 3, "item": None, "msg": "needs-fact marker"}
        self.fakes(**{"facts-mech": fake_gate("facts-mech", warnings=[warning])})
        self.pass_stage("plan")
        self.cli("stage", "begin", "99", "mine")
        code, res = self.cli("stage", "end", "99", "mine", "--counts", "facts_added=7", "--note", "ok")
        self.assertEqual((code, res["result"]), (2, "PASS"))
        self.assertEqual(res["gates"][0]["record"], "_build/ledger/gates/99.facts-mech.json")
        doc = self.led()
        self.assertEqual(doc["stages"]["mine"]["counts"], {"facts_added": 7})
        self.assertIn("facts-mech: W307 needs-fact marker", doc["warnings"])
        self.assertIn("open fact request fr-0001", doc["warnings"])

    def test_must_fail_missing_module_is_check_unavailable_exit_3(self):
        self.enterContext(mock.patch.object(ledger, "_module", lambda name: None))
        code, res = self.cli("gate", "99", "--gate", "lint")
        self.assertEqual((code, res["result"], res["errors"][0]["code"]), (3, "UNAVAILABLE", "X03"))
        self.assertFalse((self.book / "_build" / "ledger" / "gates" / "99.lint.json").exists())
        self.pass_stage("plan")
        self.cli("stage", "begin", "99", "mine")
        code, res = self.cli("stage", "end", "99", "mine")
        self.assertEqual((code, res["result"]), (3, "UNAVAILABLE"))
        stage = self.led()["stages"]["mine"]
        self.assertEqual((stage["status"], stage["attempts"]), ("running", 0))      # nothing passed, no attempt used

    def test_must_fail_gate_function_that_crashes_or_lies_fails(self):
        def crash(ch_id, **options):
            raise RuntimeError("boom")
        self.fakes(lint=crash, sync=lambda ch_id, **o: {"gate": "sync", "chapter": ch_id, "ok": False})
        code, res = self.cli("gate", "99", "--gate", "lint")
        self.assertEqual((code, res["errors"][0]["code"]), (1, "X02"))
        code, res = self.cli("gate", "99", "--gate", "sync")
        self.assertEqual((code, res["errors"][0]["code"]), (1, "X01"))

    def test_must_fail_verify_facts_fails_when_a_fact_is_disputed(self):
        try:
            from saalib import facts
        except ImportError:
            self.skipTest("saalib.facts is not written yet")
        if not hasattr(facts, "gate_final"):
            self.skipTest("facts.gate_final is not written yet")
        def change(rows):
            rows[0]["status"] = "disputed"
        sandbox.edit_jsonl(self.book / "data" / "facts" / "widget.jsonl", change)
        self.set_stages(["verify-facts"], status="running")
        code, res = self.cli("stage", "end", "99", "verify-facts")
        self.assertEqual((code, res["result"]), (1, "FAIL"))
        self.assertIn("F02", [e["code"] for e in res["errors"]])

    def test_must_fail_failed_finalize_puts_the_front_matter_status_back(self):
        # W0 result, ledger problem 1: a failed finalize must not leave `status: ready` in the hand files
        error = {"code": "L303", "file": "99-sample/2-deep.md", "line": 3, "item": None, "msg": "wrong number in a fact link"}
        self.fakes(lint=fake_gate("lint", errors=[error]))
        self.set_stages([s for s in ledger.STAGE_NAMES if s != "finalize"])
        self.set_stages(["finalize"], status="running")
        files = [self.book / "99-sample" / "1-fast.md", self.book / "99-sample" / "2-deep.md"]
        before = [p.read_text(encoding="utf-8") for p in files]
        self.assertTrue(all("\nstatus: draft\n" in text for text in before))
        code, res = self.cli("stage", "end", "99", "finalize")
        self.assertEqual((code, res["result"]), (1, "FAIL"), res)
        self.assertEqual(self.led()["stages"]["finalize"]["status"], "fail")
        self.assertEqual([p.read_text(encoding="utf-8") for p in files], before)

    def test_failed_fix_stage_keeps_the_previous_status_and_a_passed_one_writes_it(self):
        self.set_stages([s for s in ledger.STAGE_NAMES if s not in ("fix", "finalize")])
        for lens in ("claims", "exam", "reader"):
            self.write_findings(lens, [])
        fast = self.book / "99-sample" / "1-fast.md"
        sandbox.replace_text(fast, "status: draft\n", "status: drafted\n")
        self.fakes(sync=fake_gate("sync", errors=[{"code": "S01", "file": "99-sample/5-quiz.md", "line": 1, "item": None,
                                                   "msg": "generated file is stale"}]))
        self.set_stages(["fix"], status="running")
        code, res = self.cli("stage", "end", "99", "fix")
        self.assertEqual((code, res["result"]), (1, "FAIL"), res)
        self.assertIn("\nstatus: drafted\n", fast.read_text(encoding="utf-8"))
        self.fakes()
        self.set_stages(["fix"], status="running")
        code, res = self.cli("stage", "end", "99", "fix")
        self.assertEqual(res["result"], "PASS", res)
        self.assertIn("\nstatus: reviewed\n", fast.read_text(encoding="utf-8"))

    def test_front_matter_status_is_one_line_rewrite(self):
        ch = common.chapter("99")
        before = (self.book / "99-sample" / "1-fast.md").read_text(encoding="utf-8")
        self.assertEqual(sorted(ledger._write_front_status(ch, "reviewed")), ["99-sample/1-fast.md", "99-sample/2-deep.md"])
        after = (self.book / "99-sample" / "1-fast.md").read_text(encoding="utf-8")
        self.assertEqual(after, before.replace("status: draft", "status: reviewed", 1))
        self.assertEqual(ledger._write_front_status(ch, "reviewed"), [])


class OwnGates(LedgerCase):
    def codes(self, result):
        self.assertEqual(schemas.validate(dict(result, ts="t", run=None, tool_version="t"), "gate"), [])
        return [e["code"] for e in result["errors"]]

    def test_plan_passes_on_the_fixture(self):
        result = ledger.gate_plan("99")
        self.assertEqual(self.codes(result), [], result["errors"])
        self.assertIn("_build/work/99-sample/brief.v0.json", [i["path"] for i in result["inputs"]])

    def test_must_fail_plan_bullet_without_demand_item(self):
        sandbox.edit_json(self.book / "_build" / "work" / "99-sample" / "brief.v0.json", lambda d: d["demand"].pop() and None)
        self.assertEqual(self.codes(ledger.gate_plan("99")), ["B02"])

    def test_must_fail_plan_source_not_in_corpus(self):
        def change(doc):
            doc["chapters"][0]["sources"]["faq"] = ["https://aws.amazon.com/widget-store/faqs/"]
        sandbox.edit_json(self.book / "data" / "book.json", change)
        self.assertEqual(self.codes(ledger.gate_plan("99")), ["B03"])

    def test_brief_passes_when_complete(self):
        self.write_brief()
        result = ledger.gate_brief("99")
        self.assertEqual(self.codes(result), [], result["errors"])

    def test_must_fail_brief_missing_bullet_unverified_fact_unknown_term(self):
        self.assertEqual(self.codes(ledger.gate_brief("99")), ["B01"])
        self.write_brief(question_slots=brief()["question_slots"][1:])
        self.assertEqual(self.codes(ledger.gate_brief("99")), ["B02"])
        self.write_brief(terms=["shelf", "pallet"])
        self.assertEqual(self.codes(ledger.gate_brief("99")), ["B11"])
        self.write_brief()
        def change(rows):
            for row in rows:
                if row["id"] == "widget-shelf-move":
                    row["status"] = "disputed"
        sandbox.edit_jsonl(self.book / "data" / "facts" / "widget.jsonl", change)
        self.assertEqual(self.codes(ledger.gate_brief("99")), ["B04"])

    def test_must_fail_findings_and_findings_closed(self):
        self.assertEqual(self.codes(ledger.gate_findings("99")), ["B05", "B05", "B05"])
        self.assertEqual(self.codes(ledger.gate_findings_closed("99")), ["B05", "B05", "B05"])
        finding = {"id": "c1", "file": "2-deep.md", "section": "how-it-works", "quote": "x", "type": "unsupported",
                   "severity": "blocking", "evidence": "no fact link", "status": "open", "resolution": None}
        self.write_findings("claims", [finding, {"id": "c2", "severity": "note", "status": "fixed"}])
        self.write_findings("reader", [])
        self.write_findings("exam", [])
        self.assertEqual(self.codes(ledger.gate_findings("99")), ["B06"])
        self.assertEqual(self.codes(ledger.gate_findings_closed("99")), ["B07"])
        self.write_findings("claims", [dict(finding, status="fixed")])
        self.assertEqual(self.codes(ledger.gate_findings("99")), [])
        self.assertEqual(self.codes(ledger.gate_findings_closed("99")), [])

    def test_must_fail_diagrams_gate_fixture_has_no_spec(self):
        self.assertEqual(self.codes(ledger.gate_diagrams("99")), ["D01"])

    def test_must_fail_counts_gate_open_request_and_stale(self):
        self.fakes()
        self.assertEqual(self.codes(ledger.gate_counts("99")), ["B09"])
        sandbox.replace_text(self.book / "_build" / "facts" / "requests.jsonl", '"status": "open"', '"status": "filled"')
        self.assertEqual(self.codes(ledger.gate_counts("99")), [])
        sandbox.replace_text(self.book / "99-sample" / "2-deep.md", "status: draft\n", "")
        self.assertEqual(self.codes(ledger.gate_counts("99")), ["B08"])

    def test_must_fail_counts_gate_takes_ship_errors_of_other_modules(self):
        def tasks(ch_id, quick=False, ship=False, **options):
            error = {"code": "T113", "file": None, "line": None, "item": "sample-t02", "msg": "invented command"}
            return fake_gate("tasks", errors=[error] if ship else [])(ch_id)
        self.fakes(tasks=tasks)
        self.assertEqual(self.codes(ledger.gate_counts("99")), ["T113", "B09"])


class MarkStale(LedgerCase):
    def test_mark_stale_sets_passed_stages_and_keeps_the_reason(self):
        self.drafted()
        result = ledger.mark_stale("99", "fact widget-shelf-move amended", item_stages=["questions"])
        self.assertEqual(result["stale"], ["questions", "edit"])
        doc = self.led()
        self.assertEqual(doc["stale"], ["fact widget-shelf-move amended"])
        self.assertEqual(doc["stages"]["prose"]["status"], "pass")
        self.assertEqual(doc["status"], "facts-verified")
        self.fakes()
        self.assertIn("B10", [e["code"] for e in ledger.gate_counts("99")["errors"]])


class GateAll(LedgerCase):
    def ready_to_gate(self):
        self.drafted()
        self.fakes()
        passing = lambda name: (lambda ch_id, **o: fake_gate(name)(ch_id))
        for name, fn in (("diagrams", "gate_diagrams"), ("counts", "gate_counts"), ("findings-closed", "gate_findings_closed")):
            self.enterContext(mock.patch.object(ledger, fn, passing(name)))

    def test_must_fail_no_record(self):
        self.ready_to_gate()
        code, res = self.cli("gate", "--all", "--quick")
        self.assertEqual(code, 3)
        self.assertEqual(res["chapters"][0]["result"], "no-record")
        self.assertEqual(self.led()["status"], "drafted")

    def test_must_fail_stale_gate_after_one_byte_of_an_input_changes(self):
        self.ready_to_gate()
        code, res = self.cli("gate", "99")
        self.assertEqual((code, res["result"]), (0, "PASS"))
        self.assertEqual([g["gate"] for g in res["gates"]], FINALIZE)
        code, res = self.cli("gate", "--all", "--quick")
        self.assertEqual((code, res["chapters"][0]["result"]), (0, "ok"))
        with open(self.book / "99-sample" / "1-fast.md", "a", encoding="utf-8") as f:
            f.write("x")
        code, res = self.cli("gate", "--all", "--quick")
        self.assertEqual(code, 3)
        row = res["chapters"][0]
        self.assertEqual((row["id"], row["result"], row["stale_gates"], row["failed_gates"]), ("99", "stale", ["lint"], []))

    def test_must_fail_gate_all_reports_a_failed_gate(self):
        self.ready_to_gate()
        error = {"code": "S01", "file": "99-sample/5-quiz.md", "line": None, "item": None, "msg": "file is stale"}
        self.fakes(sync=fake_gate("sync", errors=[error]))
        code, res = self.cli("gate", "--all")
        self.assertEqual((code, res["chapters"][0]["result"], res["chapters"][0]["failed_gates"]), (1, "fail", ["sync"]))
        self.assertEqual(self.cli("gate", "--all", "--quick")[0], 1)

    def test_planned_chapters_are_not_gated(self):
        code, res = self.cli("gate", "--all", "--quick")
        self.assertEqual((code, res), (0, {"chapters": []}))


class StatusReportSelftest(LedgerCase):
    def test_status(self):
        code, res = self.cli("status")
        self.assertEqual(code, 0)
        self.assertEqual(res["totals"], {"facts-verified": 1})
        row = res["chapters"][0]
        self.assertEqual((row["id"], row["slug"], row["tier"], row["wave"], row["next_stage"]), ("99", "sample", "deep", "W0", "brief"))
        self.assertEqual(row["facts"], {"verified": 7, "total": 7})
        self.assertEqual(row["questions"]["target"], 4)
        self.assertEqual(ledger._status_line(row).split()[:6], ["99", "sample", "deep", "W0", "facts-verified", "next=brief"])
        self.assertEqual(self.cli("status", "--wave", "W7")[1], {"totals": {}, "chapters": []})

    def test_report_wave(self):
        code, res = self.cli("report", "wave", "0")
        self.assertEqual(code, 0)
        self.assertEqual(res["report"], "_build/reports/wave-W0.json")
        self.assertEqual(common.read_json(self.book / "_build" / "reports" / "wave-W0.json"), res)
        self.assertEqual((res["ready"], res["open_requests"], res["counts"]["facts"]), ([], 1, 7))
        self.assertEqual(res["in_progress"], [{"id": "99", "status": "facts-verified", "next_stage": "brief"}])

    def test_must_fail_report_unknown_wave_exits_3(self):
        self.assertEqual(self.cli("report", "wave", "W9")[0], 3)

    def test_must_fail_selftest_needs_a_must_fail_test_per_module(self):
        tests = self.book / "_build" / "selftests"
        tests.mkdir()
        body = ("import unittest\n\nclass T(unittest.TestCase):\n    def test_must_fail_bad_input(self):\n        pass\n"
                "    def test_other(self):\n        pass\n")
        (tests / "test_zzledgerdemo.py").write_text(body, encoding="utf-8")
        code, res = ledger.selftest(tests_dir=tests, required=["zzledgerdemo"])
        self.assertEqual((code, res["tests"], res["failures"], res["errors"]), (0, 2, 0, 0))
        self.assertEqual(res["must_fail"], {"zzledgerdemo": 1})
        code, res = ledger.selftest(tests_dir=tests, required=["zzledgerdemo", "facts"])
        self.assertEqual((code, res["missing_must_fail"]), (1, ["facts"]))
        (tests / "test_zzledgerbroken.py").write_text(body.replace("pass", "self.fail('x')", 1), encoding="utf-8")
        code, res = ledger.selftest(tests_dir=tests, required=[])
        self.assertEqual((code, res["failures"], res["modules"]["zzledgerbroken"]["failures"]), (1, 1, 1))


if __name__ == "__main__":
    unittest.main()
