"""Tests of saalib/facts.py (TOOLS.md section 5). Every test works on a sandbox copy of the fixture book."""
import copy
import unittest

import sandbox
from saalib import common

URL = "https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html"
SID = "docs/fixture/widget-store/limits"
MAX = "widget-shelf-max-widgets"

BASE = {
    "id": "widget-crate-empty-delete", "service": "widget", "home_chapter": "99", "kind": "behavior",
    "claim": "Widget Store deletes an empty crate after 7 days.",
    "question": "After how many days does Widget Store delete an empty crate?",
    "values": [{"key": "after", "display": "7 days", "spoken": "seven days"}],
    "qualifiers": {"scope": "per crate", "default_or_max": "", "adjustable": False, "condition": ""},
    "evidence": [{"source_id": SID, "url": URL, "quote": "Widget Store deletes an empty crate after 7 days."}],
    "source_tier": 1, "hard": True, "tier0": False, "volatility": "stable", "changed": None, "exam_relevance": "extended",
}


def fact(**over):
    out = copy.deepcopy(BASE)
    out.update(copy.deepcopy(over))
    return out


def page_fact(fid, sid, url, sentence, claim, display, **over):
    return fact(id=fid, claim=claim, question="What does the page say about this?",
                values=[{"key": "v", "display": display}],
                evidence=[{"source_id": sid, "url": url, "quote": sentence}], **over)


class Case(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("facts-" + self.id().split(".")[-1])
        self.facts_file = self.book / "data" / "facts" / "widget.jsonl"
        self.votes_file = self.book / "_build" / "facts" / "votes" / "widget.jsonl"

    def tearDown(self):
        sandbox.remove(self.book)

    # -- helpers
    def put(self, name, obj):
        path = self.book / "_in" / name
        common.write_json(path, obj)
        return str(path)

    def add(self, *facts, by="miner-a"):
        return sandbox.run_json(self.book, "facts", "add", "--file", self.put("facts.json", list(facts)), "--by", by)

    def codes(self, result, index=0):
        return {f["code"] for f in result["rejected"][index]["errors"]}

    def must_reject(self, code, **over):
        exit_code, result, err = self.add(fact(**over))
        self.assertEqual(exit_code, 1, err)
        self.assertEqual(result["added"], [])
        self.assertEqual(self.codes(result), {code})
        self.assertNotIn(BASE["id"], self.stored())
        rejected = common.read_jsonl(self.book / "_build" / "facts" / "rejected.jsonl")
        self.assertEqual(rejected[-1]["input"]["id"], BASE["id"])

    def stored(self):
        return {row["id"]: row for row in common.read_jsonl(self.facts_file)}

    def vote(self, by, *votes):
        return sandbox.run_json(self.book, "facts", "vote", "--file", self.put("votes.json", list(votes)), "--by", by)

    def page(self, name, text):
        """A new snapshot in the sandbox corpus. Returns (source_id, url)."""
        sid = f"docs/fixture/widget-store/{name}"
        url = f"https://docs.aws.amazon.com/widget-store/latest/userguide/{name}.html"
        base = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store"
        (base / f"{name}.txt").write_text(text, encoding="utf-8")
        common.write_json(base / f"{name}.meta.json", {
            "source_id": sid, "url": url, "title": f"Widget Store {name}", "fixture": True,
            "sha256": common.sha256_file(base / f"{name}.txt"), "sha256_of": f"{name}.txt"})
        return sid, url

    def edit_fact(self, fid, change):
        def apply(rows):
            for row in rows:
                if row["id"] == fid:
                    change(row)
        sandbox.edit_jsonl(self.facts_file, apply)


class MechanicalChecks(Case):
    def test_fixture_facts_pass_verify(self):
        before = self.facts_file.read_bytes()
        code, result, err = sandbox.run_json(self.book, "facts", "verify", "--service", "widget")
        self.assertEqual(code, 0, err)
        self.assertEqual((result["checked"], result["ok"], result["failed"]), (7, 7, []))
        self.assertEqual(self.facts_file.read_bytes(), before)
        self.assertFalse((self.book / "_build" / "facts" / "conflicts.jsonl").exists())

    def test_add_stores_a_good_fact_as_mech_pass(self):
        code, result, err = self.add(fact())
        self.assertEqual(code, 0, err)
        self.assertEqual(result, {"added": [BASE["id"]], "rejected": [], "conflicts": []})
        row = self.stored()[BASE["id"]]
        self.assertEqual((row["status"], row["rev"], row["author"], row["votes"]), ("mech-pass", 1, "miner-a", []))
        self.assertEqual(row["evidence"][0]["sha256"], common.sha256_file(
            self.book / "_build" / "corpus" / "snap" / (SID + ".txt")))
        self.assertEqual(len(row["evidence"][0]["match"]), 2)
        self.assertEqual(list(self.stored()), sorted(self.stored()))

    def test_add_needs_a_label(self):
        code, _out, _err = sandbox.run(self.book, "facts", "add", "--file", self.put("facts.json", [fact()]), "--by", "unknown")
        self.assertEqual(code, 3)

    def test_must_fail_paraphrased_quote(self):
        self.must_reject("M3", evidence=[{"source_id": SID, "url": URL,
                                          "quote": "Widget Store removes an empty crate after 7 days."}])

    def test_must_fail_wrong_number(self):
        self.must_reject("M5", claim="Widget Store deletes an empty crate after 70 days.",
                         values=[{"key": "after", "display": "70 days"}])

    def test_must_fail_wrong_number_in_a_stored_display(self):
        self.edit_fact(MAX, lambda row: row["values"][0].update(display="5,000 widgets"))
        code, result, _err = sandbox.run_json(self.book, "facts", "verify", "--service", "widget")
        self.assertEqual(code, 1)
        self.assertEqual([f["id"] for f in result["failed"]], [MAX])
        self.assertIn("M5", [f["code"] for f in result["failed"][0]["errors"]])
        self.assertEqual(self.stored()[MAX]["status"], "candidate")

    def test_must_fail_unit_mismatch_tb_is_not_tib(self):
        sid, url = self.page("sizes", "# Widget sizes\n\nEach widget can store up to 500 TB of data in one shelf.\n")
        sentence = "Each widget can store up to 500 TB of data in one shelf."
        bad = page_fact("widget-size-max", sid, url, sentence, "A widget stores up to 500 TiB of data.", "500 TiB")
        code, result, err = self.add(bad)
        self.assertEqual(code, 1, err)
        self.assertEqual(self.codes(result), {"M5"})
        self.assertIn("unit mismatch", result["rejected"][0]["errors"][0]["msg"])
        good = page_fact("widget-size-max", sid, url, sentence, "A widget stores up to 500 TB of data.", "500 TB")
        code, result, err = self.add(good)
        self.assertEqual(code, 0, err)

    def test_number_word_in_the_quote_counts_as_its_digit(self):
        sentence = "A crate label can have up to twelve characters in any Region."
        sid, url = self.page("labels", "# Labels\n\n" + sentence + "\n")
        code, result, err = self.add(page_fact("widget-label-length", sid, url, sentence,
                                               "A crate label has up to 12 characters.", "12 characters"))
        self.assertEqual(code, 0, err or result)

    def test_must_fail_quote_from_navigation_text(self):
        sentence = "Did this page help you? Tell us how we can make the documentation better."
        sid, url = self.page("nav", "# Widget page\n\n" + sentence + "\n")
        code, result, err = self.add(page_fact("widget-page-help", sid, url, sentence,
                                               "The page asks whether it helped the reader.", "helped the reader", hard=False))
        self.assertEqual(code, 1, err)
        self.assertEqual(self.codes(result), {"M8"})

    def test_must_fail_host_outside_the_allow_list(self):
        code, result, err = self.add(fact(evidence=[{"source_id": SID, "url": "https://example.com/widget/limits.html",
                                                     "quote": BASE["evidence"][0]["quote"]}]))
        self.assertEqual(code, 1, err)
        self.assertIn("M2", self.codes(result))
        self.assertNotIn(BASE["id"], self.stored())

    def test_must_fail_missing_qualifier_on_a_limit(self):
        self.must_reject("M6", kind="limit",
                         qualifiers={"scope": "", "default_or_max": "max", "adjustable": False, "condition": ""})

    def test_must_fail_display_in_neither_claim_nor_quote(self):
        self.must_reject("M7", values=[{"key": "after", "display": "empty box"}])

    def test_must_fail_short_quote_that_is_not_a_complete_sentence(self):
        self.must_reject("M4", evidence=[{"source_id": SID, "url": URL, "quote": "empty crate after 7 days."}])

    def test_short_complete_sentence_is_accepted(self):
        code, result, err = self.add(fact(
            id="widget-shelf-regional", claim="A shelf is a Regional resource.", hard=False,
            question=None, values=[{"key": "word", "display": "Regional resource"}],
            evidence=[{"source_id": SID, "url": URL, "quote": "A shelf is a Regional resource."}]))
        self.assertEqual(code, 0, err or result)

    def test_must_fail_hard_fact_without_question(self):
        self.must_reject("M13", question="")

    def test_must_fail_hard_false_on_a_limit(self):
        self.must_reject("M11", kind="limit", hard=False,
                         qualifiers={"scope": "per crate", "default_or_max": "fixed", "adjustable": False, "condition": ""})

    def test_must_fail_hard_false_with_a_number_and_unit(self):
        self.must_reject("M11", hard=False)

    def quota(self, header):
        return fact(id="widget-crates-per-account", kind="quota", claim="The default quota is 5 crates per account.",
                    question="What is the default quota of crates per account?",
                    values=[{"key": "default", "display": "5 crates"}],
                    qualifiers={"scope": "per account", "default_or_max": "default", "adjustable": True, "condition": ""},
                    evidence=[{"source_id": SID, "url": URL, "quote": "| Crates per account | 5 | Yes |", "table_header": header}])

    def test_must_fail_table_row_without_table_header(self):
        code, result, err = self.add(self.quota(None))
        self.assertEqual(code, 1, err)
        self.assertEqual(self.codes(result), {"M4"})

    def test_must_fail_table_row_with_the_header_of_another_table(self):
        code, result, err = self.add(self.quota("| Change | Description | Date |"))
        self.assertEqual(code, 1, err)
        self.assertEqual(self.codes(result), {"M4"})
        code, result, err = self.add(self.quota("| Resource | Default | Adjustable |"))
        self.assertEqual(code, 0, err or result)

    def test_adopt_attaches_the_header_row_by_script(self):
        body = self.quota(None)
        del body["evidence"]
        code, result, err = sandbox.run_json(self.book, "facts", "adopt", "--source", SID, "--table", "0", "--row", "2",
                                             "--file", self.put("one.json", body), "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        ev = self.stored()["widget-crates-per-account"]["evidence"][0]
        self.assertEqual(ev["quote"], "| Crates per account | 5 | Yes |")
        self.assertEqual(ev["table_header"], "| Resource | Default | Adjustable |")
        self.assertEqual(ev["url"], URL)

    def test_adopt_sentence_takes_the_whole_sentence(self):
        body = fact()
        del body["evidence"]
        code, result, err = sandbox.run_json(self.book, "facts", "adopt", "--source", SID, "--sentence", "an empty crate",
                                             "--file", self.put("one.json", body), "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        self.assertEqual(self.stored()[BASE["id"]]["evidence"][0]["quote"], BASE["evidence"][0]["quote"])

    def test_must_fail_adopt_sentence_found_twice(self):
        body = fact()
        del body["evidence"]
        code, _out, err = sandbox.run(self.book, "facts", "adopt", "--source", SID, "--sentence", "can hold up to",
                                      "--file", self.put("one.json", body), "--by", "miner-a")
        self.assertEqual(code, 1, err)
        self.assertNotIn(BASE["id"], self.stored())

    def test_must_fail_changed_snapshot_hash(self):
        path = self.book / "_build" / "corpus" / "snap" / (SID + ".txt")
        path.write_text(path.read_text(encoding="utf-8") + "\nOne more line.\n", encoding="utf-8")
        code, result, _err = sandbox.run_json(self.book, "facts", "verify", MAX)
        self.assertEqual(code, 1)
        self.assertEqual({f["code"] for f in result["failed"][0]["errors"]}, {"M2"})
        row = self.stored()[MAX]
        self.assertEqual((row["status"], row["stale"]), ("candidate", "snapshot-changed"))

    def test_must_fail_reused_id(self):
        code, result, _err = self.add(fact(id="widget-crate-capacity"))
        self.assertEqual(code, 1)
        self.assertIn("M1", self.codes(result))

    def test_must_fail_file_outside_the_book(self):
        code, _out, _err = sandbox.run(self.book, "facts", "add", "--file", "/etc/hosts", "--by", "miner-a")
        self.assertEqual(code, 4)

    def test_candidate_that_passes_becomes_mech_pass(self):
        self.edit_fact(MAX, lambda row: row.update(status="candidate", stale="mech-failed"))
        code, _result, err = sandbox.run_json(self.book, "facts", "verify", MAX)
        self.assertEqual(code, 0, err)
        self.assertEqual(self.stored()[MAX]["status"], "mech-pass")

    def test_number_rules_in_process(self):
        with sandbox.paths(self.book):
            from saalib import facts
            ctx = facts._Ctx()

            def nums(text, quote_side=False):
                return [(n["num"], n["unit"]) for n in facts._numbers_of(text, ctx, quote_side)[0]]
            self.assertEqual(nums("Amazon S3 and EC2 in us-east-1 on gp3 return 4xx"), [])
            self.assertEqual(nums("5GB or 10-second or 1,000 widgets"), [("5", "GB"), ("10", "second"), ("1000", None)])
            self.assertEqual(nums("from 1 to 5 GB", quote_side=True), [("1", "GB"), ("5", "GB")])
            self.assertEqual(nums("On November 19, 2025 it grew to 500."), [("500", None)])
            self.assertEqual(facts._numbers_of("On November 19, 2025 and in 2024-03.", ctx)[1], ["2024-03", "2025-11-19"])
            self.assertEqual(ctx.unit_key("seconds"), ctx.unit_key("second"))
            self.assertNotEqual(ctx.unit_key("TB"), ctx.unit_key("TiB"))


class Votes(Case):
    def entail(self, verdict="support", rev=1, fid=None):
        return {"fact": fid or BASE["id"], "rev": rev, "lens": "entail", "verdict": verdict,
                "reason": "The quote states the claim word for word."}

    def test_must_fail_author_cannot_vote(self):
        self.add(fact())
        before = self.votes_file.read_bytes()
        code, result, err = self.vote("miner-a", self.entail())
        self.assertEqual(code, 1, err)
        self.assertEqual(result["appended"], 0)
        self.assertEqual(self.votes_file.read_bytes(), before)

    def test_must_fail_vote_on_a_stale_rev(self):
        self.add(fact())
        before = self.votes_file.read_bytes()
        code, _result, _err = self.vote("verifier-x", self.entail(rev=2))
        self.assertEqual(code, 1)
        self.assertEqual(self.votes_file.read_bytes(), before)

    def test_must_fail_verdict_of_another_lens_and_quote_not_in_snapshot(self):
        self.add(fact())
        code, _result, _err = self.vote("verifier-x", self.entail(verdict="current"))
        self.assertEqual(code, 1)
        bad = dict(self.entail(), source_id=SID, quote="A crate can hold up to 51 widgets.")
        code, _result, _err = self.vote("verifier-x", bad)
        self.assertEqual(code, 1)

    def test_must_fail_finalize_without_the_required_votes(self):
        self.add(fact())
        code, result, err = sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        self.assertEqual(code, 2, err)
        self.assertEqual(result["verified"], [])
        self.assertEqual(result["pending"], [{"id": BASE["id"], "missing": ["entail"]}])
        self.assertEqual(self.stored()[BASE["id"]]["status"], "mech-pass")

    def test_must_fail_one_partial_vote_gives_disputed(self):
        self.add(fact())
        self.assertEqual(self.vote("verifier-x", self.entail())[0], 0)
        self.assertEqual(self.vote("verifier-y", self.entail(verdict="partial"))[0], 0)
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", "--chapter", "99")
        self.assertEqual(code, 1)
        self.assertEqual(result["disputed"], [BASE["id"]])
        self.assertEqual(self.stored()[BASE["id"]]["status"], "disputed")

    def test_must_fail_changed_fact_stays_pending_without_a_currency_vote(self):
        self.edit_fact(MAX, lambda row: row.update(status="mech-pass", votes=[]))
        sandbox.edit_jsonl(self.votes_file, lambda rows: [v for v in rows if v["lens"] != "currency"])
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", MAX)
        self.assertEqual(code, 2)
        self.assertEqual(result["pending"], [{"id": MAX, "missing": ["currency"]}])
        self.assertEqual(self.stored()[MAX]["status"], "mech-pass")

    def test_positive_votes_verify_and_the_summary_is_written(self):
        self.add(fact())
        self.vote("verifier-x", self.entail())
        code, result, err = sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        self.assertEqual(code, 0, err)
        self.assertEqual(result["verified"], [BASE["id"]])
        row = self.stored()[BASE["id"]]
        self.assertEqual(row["status"], "verified")
        self.assertEqual(row["votes"], [{"lens": "entail", "verdict": "support", "voter": "verifier-x", "rev": 1}])

    def test_finalize_on_the_fixture_changes_nothing(self):
        before = self.facts_file.read_bytes()
        code, result, err = sandbox.run_json(self.book, "facts", "finalize", "--service", "widget")
        self.assertEqual(code, 0, err)
        self.assertEqual(result, {"verified": [], "disputed": [], "rejected": [], "pending": []})
        self.assertEqual(self.facts_file.read_bytes(), before)

    def test_must_fail_hand_edited_status(self):
        self.add(fact())
        self.edit_fact(BASE["id"], lambda row: row.update(status="verified"))
        with sandbox.paths(self.book):
            from saalib import facts
            gate = facts.gate_final("99")
            self.assertFalse(gate["ok"])
            self.assertIn("F04", [f["code"] for f in gate["errors"] if f["item"] == BASE["id"]])
        code, result, _err = sandbox.run_json(self.book, "facts", "verify", BASE["id"])
        self.assertEqual(code, 1)
        self.assertEqual({f["code"] for f in result["failed"][0]["errors"]}, {"F04"})
        self.assertEqual(self.stored()[BASE["id"]]["status"], "candidate")

    def test_must_fail_second_bad_vote_after_a_repair_rejects(self):
        self.add(fact())
        self.vote("verifier-x", self.entail(verdict="not-supported"))
        sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        patch = self.put("patch.json", {"claim": "Widget Store deletes each empty crate after 7 days."})
        code, result, err = sandbox.run_json(self.book, "facts", "amend", BASE["id"], "--file", patch, "--reason", "repair",
                                             "--by", "miner-a")
        self.assertEqual(code, 0, err)
        row = self.stored()[BASE["id"]]
        self.assertEqual((row["rev"], row["repairs"], row["status"]), (2, 1, "mech-pass"))
        self.assertEqual(sandbox.run_json(self.book, "facts", "finalize", BASE["id"])[0], 2)     # old votes do not count
        self.vote("verifier-x", self.entail(verdict="unsure", rev=2))
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        self.assertEqual(code, 1)
        self.assertEqual(result["rejected"], [BASE["id"]])

    def test_packet_hides_author_status_and_votes(self):
        self.add(fact())
        code, result, err = sandbox.run_json(self.book, "facts", "batch", "--chapter", "99", "--lens", "entail")
        self.assertEqual(code, 0, err)
        self.assertEqual(result["batches"], ["99-entail-001"])
        out = self.book / "_in" / "packet.json"
        code, _out, err = sandbox.run(self.book, "facts", "packet", "99-entail-001", "--out", str(out))
        self.assertEqual(code, 0, err)
        packet = common.read_json(out)
        self.assertEqual([f["id"] for f in packet["facts"]], [BASE["id"]])
        item = packet["facts"][0]
        self.assertFalse({"author", "status", "votes", "exam_relevance", "note"} & set(item))
        self.assertIn("Widget Store deletes an empty crate after 7 days.", item["evidence"][0]["context"])
        self.assertEqual(item["evidence"][0]["headings"], ["Amazon Widget Store limits", "Crates"])
        self.vote("verifier-x", self.entail())
        code, result, _err = sandbox.run_json(self.book, "facts", "batch", "--chapter", "99", "--lens", "entail")
        self.assertEqual(result["batches"], [])


class AmendAndDependents(Case):
    def patch_display(self):
        return self.put("patch.json", {"values": [
            {"key": "max", "display": "up to 500 widgets", "spoken": "up to five hundred widgets"},
            {"key": "old", "display": "200 widgets", "spoken": "two hundred widgets"}]})

    def test_amend_of_a_display_resets_dependents_and_marks_the_chapter_stale(self):
        code, result, err = sandbox.run_json(self.book, "facts", "amend", MAX, "--file", self.patch_display(),
                                             "--reason", "the display now holds the absolute word", "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        self.assertEqual((result["rev"], result["status"], result["broken_links"]), (2, "mech-pass", []))
        self.assertGreater(result["replaced"], 0)
        self.assertEqual(result["dependents"]["questions"], ["sample-q001", "sample-q002"])
        self.assertIn("sample-c001", result["dependents"]["cards"])
        row = self.stored()[MAX]
        self.assertEqual((row["rev"], row["status"], row["votes"]), (2, "mech-pass", []))
        questions = {q["id"]: q for q in common.read_json(self.book / "data" / "99-sample" / "questions.json")["items"]}
        for qid in ("sample-q001", "sample-q002"):
            self.assertEqual(questions[qid]["status"], "candidate")
            self.assertEqual(questions[qid]["verification"], {"status": "candidate", "round": 0, "solvers": []})
        self.assertEqual(questions["sample-q003"]["status"], "ready")
        self.assertIn("[up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets)", questions["sample-q002"]["options"][1]["why"])
        fast = (self.book / "99-sample" / "1-fast.md").read_text(encoding="utf-8")
        self.assertNotIn("[500 widgets](../facts/widget.md#widget-shelf-max-widgets)", fast)
        self.assertNotIn("up to up to", fast)
        self.assertIn("[200 widgets](../facts/widget.md#widget-shelf-max-widgets)", fast)
        ledger = common.read_json(self.book / "_build" / "ledger" / "chapters" / "99.json")
        self.assertTrue(any(f"fact {MAX} amended" in str(entry) for entry in ledger["stale"]), ledger["stale"])
        log = common.read_jsonl(self.book / "_build" / "reports" / "changelog.jsonl")[-1]
        self.assertEqual((log["fact"], log["chapters"]), (MAX, ["99"]))
        self.assertIn("500 widgets", log["was"])

    def test_must_fail_amend_to_a_number_that_no_quote_holds(self):
        before = self.facts_file.read_bytes()
        patch = self.put("patch.json", {"claim": "A shelf holds up to 600 widgets. Before November 19, 2025 the maximum was 200 widgets.",
                                        "values": [{"key": "max", "display": "600 widgets"}, {"key": "old", "display": "200 widgets"}]})
        code, result, _err = sandbox.run_json(self.book, "facts", "amend", MAX, "--file", patch, "--reason", "test", "--by", "miner-a")
        self.assertEqual(code, 1)
        self.assertIn("M5", [f["code"] for f in result["errors"]])
        self.assertEqual(self.facts_file.read_bytes(), before)
        questions = common.read_json(self.book / "data" / "99-sample" / "questions.json")["items"]
        self.assertEqual(questions[0]["status"], "ready")

    def test_dry_run_writes_nothing(self):
        before = self.facts_file.read_bytes()
        fast = (self.book / "99-sample" / "1-fast.md").read_bytes()
        code, result, err = sandbox.run_json(self.book, "facts", "amend", MAX, "--file", self.patch_display(),
                                             "--reason", "look first", "--dry-run", "--by", "miner-a")
        self.assertEqual(code, 0, err)
        self.assertGreater(result["replaced"], 0)
        self.assertEqual(self.facts_file.read_bytes(), before)
        self.assertEqual((self.book / "99-sample" / "1-fast.md").read_bytes(), fast)

    def test_light_patch_keeps_rev_status_and_votes(self):
        patch = self.put("patch.json", {"note": "checked by the registrar", "tier0": False})
        code, result, err = sandbox.run_json(self.book, "facts", "amend", MAX, "--file", patch, "--reason", "note")
        self.assertEqual(code, 0, err)
        row = self.stored()[MAX]
        self.assertEqual((row["rev"], row["status"], len(row["votes"]), row["note"]), (1, "verified", 2, "checked by the registrar"))

    def test_must_fail_patch_of_a_tool_owned_key(self):
        patch = self.put("patch.json", {"status": "verified"})
        code, _out, _err = sandbox.run(self.book, "facts", "amend", MAX, "--file", patch, "--reason", "no")
        self.assertEqual(code, 1)

    def test_reject_resets_dependents(self):
        code, result, err = sandbox.run_json(self.book, "facts", "amend", "widget-crate-capacity", "--reject", "--reason", "test")
        self.assertEqual(code, 0, err)
        self.assertEqual(self.stored()["widget-crate-capacity"]["status"], "rejected")
        questions = {q["id"]: q for q in common.read_json(self.book / "data" / "99-sample" / "questions.json")["items"]}
        self.assertEqual(questions["sample-q004"]["status"], "candidate")
        with sandbox.paths(self.book):
            from saalib import facts
            gate = facts.gate_final("99")
            self.assertIn("F02", [f["code"] for f in gate["errors"] if f["item"] == "widget-crate-capacity"])

    def test_freshen_offline_passes_and_reports_a_missing_quote(self):
        code, result, err = sandbox.run_json(self.book, "freshen", "--offline")
        self.assertEqual(code, 0, err)
        self.assertEqual((result["facts_ok"], result["facts_broken"]), (7, []))
        sandbox.replace_text(self.book / "_build" / "corpus" / "snap" / (SID + ".txt"),
                             "A crate can hold up to 50 widgets.", "A crate can hold up to 60 widgets.")
        code, result, _err = sandbox.run_json(self.book, "freshen", "--offline")
        self.assertEqual(code, 1)
        self.assertEqual(result["facts_broken"], ["widget-crate-capacity"])
        row = self.stored()["widget-crate-capacity"]
        self.assertEqual((row["status"], row["stale"]), ("candidate", "quote-missing"))
        self.assertEqual(self.stored()[MAX]["status"], "verified")
        questions = {q["id"]: q for q in common.read_json(self.book / "data" / "99-sample" / "questions.json")["items"]}
        self.assertEqual(questions["sample-q004"]["status"], "candidate")


class GatesSheetsQueues(Case):
    def test_gates_pass_on_the_fixture(self):
        with sandbox.paths(self.book):
            from saalib import facts, schemas
            for gate in (facts.gate_mech("99"), facts.gate_final("99"), facts.gate_final("99", quick=True)):
                self.assertTrue(gate["ok"], gate["errors"])
                self.assertEqual(gate["exit"], 0)
                self.assertEqual(schemas.validate(gate, "gate"), [])
                self.assertIn("data/facts/widget.jsonl", [i["path"] for i in gate["inputs"]])
            self.assertEqual(facts.gate_final("99")["counts"], {"verified": 7, "rejected": 0, "superseded": 0, "candidate": 0,
                                                              "mech-pass": 0, "disputed": 0, "open_conflicts": 0})
            self.assertEqual(len(facts.load("widget")), 7)
            self.assertEqual(facts.displays(facts.load()[MAX]), ["500 widgets", "200 widgets"])

    def test_must_fail_gate_final_with_a_disputed_fact(self):
        self.edit_fact("widget-shelf-move", lambda row: row.update(status="disputed"))
        with sandbox.paths(self.book):
            from saalib import facts
            gate = facts.gate_final("99")
            self.assertEqual((gate["ok"], gate["exit"]), (False, 1))
            self.assertEqual([(f["code"], f["item"]) for f in gate["errors"]], [("F02", "widget-shelf-move")])

    def test_must_fail_gate_mech_with_a_wrong_number(self):
        self.edit_fact("widget-crate-capacity", lambda row: row.update(claim="A crate holds up to 55 widgets."))
        with sandbox.paths(self.book):
            from saalib import facts
            gate = facts.gate_mech("99")
            self.assertFalse(gate["ok"])
            self.assertEqual({(f["code"], f["item"]) for f in gate["errors"]}, {("M5", "widget-crate-capacity")})
            self.assertIn("M5", [f["code"] for f in facts.gate_final("99")["errors"]])

    def test_must_fail_gate_mech_without_facts(self):
        self.facts_file.write_text("", encoding="utf-8")
        with sandbox.paths(self.book):
            from saalib import facts
            self.assertEqual([f["code"] for f in facts.gate_mech("99")["errors"]], ["F01"])

    def test_is_volatile(self):
        with sandbox.paths(self.book):
            from saalib import facts
            rows = facts.load()
            self.assertFalse(facts.is_volatile(rows[MAX]))
            self.assertTrue(facts.is_volatile(dict(rows[MAX], kind="price")))
            sandbox.edit_json(self.book / "_build" / "style" / "SPEC.json",
                              lambda spec: spec["questions"].update(volatile_window_months=24))
            self.assertTrue(facts.is_volatile(rows[MAX]))
            self.assertFalse(facts.is_volatile(rows["widget-shelf-move"]))

    def test_render_writes_the_fact_sheet(self):
        code, result, err = sandbox.run_json(self.book, "facts", "render", "--service", "widget")
        self.assertEqual(code, 0, err)
        text = (self.book / "facts" / "widget.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("<!-- generated by saa.py; do not edit -->\n# Amazon Widget Store: facts\n\n7 facts, "))
        self.assertIn("Last checked 2026-10-04.", text)
        for part in ("### widget-shelf-max-widgets\n\n**Claim.** A shelf holds up to 500 widgets.",
                     "**Write it as.** `500 widgets` · `200 widgets`",
                     "**Scope.** per shelf; maximum; not adjustable.",
                     '> "Each shelf can hold up to 500 widgets."\n> — [Amazon Widget Store limits](' + URL + ")",
                     '> "Shelves per Region | 20 | Yes" (columns: Resource | Default | Adjustable)',
                     "**Changed.** 2025-11-19: was 200 widgets.",
                     "**Scope.** per Region, per account; default; adjustable."):
            self.assertIn(part, text)
        code, result, _err = sandbox.run_json(self.book, "facts", "render", "--all")
        self.assertEqual((result["written"], result["unchanged"]), ([], 1))

    def test_unverified_fact_is_not_rendered_and_not_carded(self):
        self.add(fact())
        sandbox.run(self.book, "facts", "render", "--all")
        self.assertNotIn(BASE["id"], (self.book / "facts" / "widget.md").read_text(encoding="utf-8"))
        code, result, _err = sandbox.run_json(self.book, "facts", "card", "--chapter", "99")
        self.assertEqual(len(result["cards"]), 7)
        self.assertIn("[500 widgets](../facts/widget.md#widget-shelf-max-widgets)", result["cards"][-1]["links"]
                      + [link for card in result["cards"] for link in card["links"]])
        code, result, _err = sandbox.run_json(self.book, "facts", "card", "--chapter", "99", "--all")
        self.assertEqual(len(result["cards"]), 8)

    def test_supersede_keeps_the_old_anchor(self):
        self.add(fact(id="widget-crate-capacity-v2", claim="One crate holds up to 50 widgets, and no more.",
                      question="How many widgets fit in a crate?", values=[{"key": "max", "display": "50 widgets"}],
                      evidence=[{"source_id": SID, "url": URL, "quote": "A crate can hold up to 50 widgets."}]))
        code, result, err = sandbox.run_json(self.book, "facts", "amend", "widget-crate-capacity", "--supersede",
                                             "widget-crate-capacity-v2", "--relink", "--reason", "better wording")
        self.assertEqual(code, 0, err)
        rows = self.stored()
        self.assertEqual((rows["widget-crate-capacity"]["status"], rows["widget-crate-capacity"]["superseded_by"]),
                         ("superseded", "widget-crate-capacity-v2"))
        fast = (self.book / "99-sample" / "1-fast.md").read_text(encoding="utf-8")
        self.assertIn("[50 widgets](../facts/widget.md#widget-crate-capacity-v2)", fast)
        self.assertNotIn("#widget-crate-capacity)", fast)
        sandbox.run(self.book, "facts", "render", "--all")
        sheet = (self.book / "facts" / "widget.md").read_text(encoding="utf-8")
        self.assertIn("### widget-crate-capacity\n\nReplaced by [widget-crate-capacity-v2](#widget-crate-capacity-v2).", sheet)

    def test_conflict_queue_blocks_verification(self):
        sentence = "A large crate can hold up to 80 widgets."
        sid, url = self.page("large", "# Large crates\n\n" + sentence + "\n")
        code, result, err = self.add(page_fact("widget-crate-large", sid, url, sentence, "A crate holds up to 80 widgets.",
                                               "80 widgets", kind="limit",
                                               qualifiers={"scope": "per crate", "default_or_max": "max", "adjustable": False, "condition": ""}))
        self.assertEqual(code, 0, err or result)
        self.assertEqual(result["conflicts"], ["cf-0001"])
        self.vote("verifier-x", {"fact": "widget-crate-large", "rev": 1, "lens": "entail", "verdict": "support",
                                 "reason": "The quote states the limit."})
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", "widget-crate-large")
        self.assertEqual((code, result["disputed"]), (1, ["widget-crate-large"]))
        with sandbox.paths(self.book):
            from saalib import facts
            self.assertIn(("F03", "widget-crate-capacity"), [(f["code"], f["item"]) for f in facts.gate_final("99")["errors"]])
        sandbox.run(self.book, "facts", "verify", "--all")                         # the pair is queued once
        self.assertEqual(len(common.read_jsonl(self.book / "_build" / "facts" / "conflicts.jsonl")), 1)
        code, result, err = sandbox.run_json(self.book, "facts", "conflicts", "--resolve", "cf-0001", "--both",
                                             "--reason", "different crate sizes")
        self.assertEqual(code, 0, err)
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", "widget-crate-large")
        self.assertEqual((code, result["verified"]), (0, ["widget-crate-large"]))

    def test_conflict_resolved_with_keep_rejects_the_other_fact(self):
        sentence = "A large crate can hold up to 80 widgets."
        sid, url = self.page("large", "# Large crates\n\n" + sentence + "\n")
        self.add(page_fact("widget-crate-large", sid, url, sentence, "A crate holds up to 80 widgets.", "80 widgets"))
        code, result, err = sandbox.run_json(self.book, "facts", "conflicts", "--resolve", "cf-0001", "--keep",
                                             "widget-crate-capacity", "--reason", "the page is about another product")
        self.assertEqual(code, 0, err)
        self.assertEqual(self.stored()["widget-crate-large"]["status"], "rejected")

    def test_request_queue(self):
        args = ["facts", "request", "--chapter", "99", "--service", "widget", "--where", "2-deep.md#numbers-that-decide-answers"]
        code, result, err = sandbox.run_json(self.book, *args, "--question", "How many crates does one account hold by default?")
        self.assertEqual(code, 0, err)
        self.assertEqual((result["id"], result["status"]), ("fr-0003", "open"))
        code, result, _err = sandbox.run_json(self.book, *args, "--question", "after how many days does Widget Store delete an empty crate?")
        self.assertEqual(result["duplicate_of"], "fr-0001")
        self.assertEqual(len(common.read_jsonl(self.book / "_build" / "facts" / "requests.jsonl")), 3)
        code, result, _err = sandbox.run_json(self.book, *args, "--fact", MAX, "--display", "500 widgets per shelf")
        self.assertEqual((result["fact"], result["display"], result["question"]), (MAX, "500 widgets per shelf", "display: 500 widgets per shelf"))
        code, result, _err = sandbox.run_json(self.book, "facts", "request", "--list", "--status", "open")
        self.assertEqual(result["count"], 3)
        code, result, _err = sandbox.run_json(self.book, "facts", "request", "--close", "fr-0001", "--fact", MAX)
        self.assertEqual((code, result["status"]), (0, "filled"))

    def test_must_fail_request_closed_with_an_unverified_fact(self):
        self.add(fact())
        code, _out, _err = sandbox.run(self.book, "facts", "request", "--close", "fr-0001", "--fact", BASE["id"])
        self.assertEqual(code, 1)
        code, _out, _err = sandbox.run(self.book, "facts", "request", "--close", "fr-0001", "--unfillable")
        self.assertEqual(code, 1)
        rows = common.read_jsonl(self.book / "_build" / "facts" / "requests.jsonl")
        self.assertEqual(rows[0]["status"], "open")

    def test_audit_sample_and_rederive_votes(self):
        code, first, err = sandbox.run_json(self.book, "audit", "sample", "--n", "3", "--seed", "7")
        self.assertEqual(code, 0, err)
        code, again, _err = sandbox.run_json(self.book, "audit", "sample", "--n", "3", "--seed", "7")
        self.assertEqual([f["id"] for f in first["facts"]], [f["id"] for f in again["facts"]])
        self.assertEqual(len(first["facts"]), 3)
        code, chapter, _err = sandbox.run_json(self.book, "audit", "sample", "--n", "6", "--seed", "1", "--chapter", "99")
        self.assertEqual(chapter["facts"][0]["id"], MAX)                           # tier0 first
        out = self.book / "_in" / "audit.json"
        sandbox.run(self.book, "audit", "packet", "s1-n6", "--out", str(out))
        packet = common.read_json(out)
        self.assertEqual(set(packet["facts"][0]), {"id", "rev", "service", "question"})
        base = {"rev": 1, "lens": "rederive", "reason": "Found on the limits page.", "source_id": SID}
        code, result, err = self.vote("auditor-a",
                                      dict(base, fact="widget-shelf-move", answer="No, you copy the shelf.",
                                           quote="You cannot move a shelf to another Region."),
                                      dict(base, fact="widget-crate-capacity", answer="5 widgets",
                                           quote="| Crates per account | 5 | Yes |"),
                                      dict(base, fact="widget-shelf-default-private", answer=None, quote=None, source_id=None))
        self.assertEqual(code, 0, err or result)
        self.assertEqual([v["verdict"] for v in result["verdicts"]], ["match", "mismatch", "not-found"])
        rows = self.stored()
        self.assertEqual(rows["widget-shelf-move"]["status"], "verified")
        self.assertEqual(rows["widget-crate-capacity"]["status"], "disputed")
        self.assertEqual(rows["widget-shelf-default-private"]["status"], "disputed")
        code, result, _err = sandbox.run_json(self.book, "audit", "result", "s1-n6")
        self.assertEqual(code, 1)
        self.assertEqual((result["sample"], result["match"], result["expand"]), (6, 1, ["99"]))
        self.assertEqual(sorted(result["failed"]), ["widget-crate-capacity", "widget-shelf-default-private"])


if __name__ == "__main__":
    unittest.main()
