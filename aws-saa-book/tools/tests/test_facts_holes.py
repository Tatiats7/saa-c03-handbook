"""Regression tests for the holes of _build/reports/gate-break-grounding.md that live in saalib/facts.py.

Each test repeats one attempt of the gate breaker (its id is in the test name) and asserts that the gate
now rejects the bad input. See _build/reports/gate-break-fixes.md.
"""
import unittest

import sandbox
from saalib import common
from test_facts import BASE, MAX, SID, URL, Case, fact

SOFT = {"kind": "behavior", "hard": False, "question": None}


class NonHardFacts(Case):
    """H1 and H9: no fact is verified without an entail vote, and an amend cannot remove that need."""

    def test_must_fail_f11_non_hard_fact_is_not_verified_without_a_vote(self):
        code, result, err = self.add(fact(
            id="widget-x-false", **SOFT,
            claim="A shelf copies its widgets to every other Region automatically, and every user of the account reads it.",
            values=[{"key": "v", "display": "copies its widgets to every other Region"}],
            evidence=[{"source_id": SID, "url": URL, "quote": "A crate is a container for widgets that you ship between Regions."}]))
        self.assertEqual(code, 0, err or result)
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", "widget-x-false")
        self.assertEqual(code, 2)
        self.assertEqual(result["verified"], [])
        self.assertEqual(result["pending"], [{"id": "widget-x-false", "missing": ["entail"]}])
        self.assertEqual(self.stored()["widget-x-false"]["status"], "mech-pass")

    def test_must_fail_a01_amend_to_hard_false_still_needs_a_vote(self):
        patch = self.put("patch.json", {"claim": "A shelf is a Regional resource that copies its widgets to each other AWS Region.",
                                        "hard": False})
        code, result, err = sandbox.run_json(self.book, "facts", "amend", "widget-shelf-scope", "--file", patch,
                                             "--reason", "wording", "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", "widget-shelf-scope")
        self.assertEqual(code, 2)
        self.assertEqual(result["verified"], [])
        self.assertEqual(self.stored()["widget-shelf-scope"]["status"], "mech-pass")

    def test_must_fail_amend_without_a_label(self):
        before = self.facts_file.read_bytes()
        patch = self.put("patch.json", {"claim": "A shelf is a Regional resource: it stores its widgets in one AWS Region."})
        code, _out, _err = sandbox.run(self.book, "facts", "amend", "widget-shelf-scope", "--file", patch, "--reason", "wording")
        self.assertEqual(code, 3)
        self.assertEqual(self.facts_file.read_bytes(), before)

    def test_must_fail_the_agent_that_amended_votes_on_the_new_rev(self):
        patch = self.put("patch.json", {"claim": "A shelf is a Regional resource: it stores its widgets in one AWS Region."})
        code, _result, err = sandbox.run_json(self.book, "facts", "amend", "widget-shelf-scope", "--file", patch,
                                              "--reason", "wording", "--by", "editor-z")
        self.assertEqual(code, 0, err)
        vote = {"fact": "widget-shelf-scope", "rev": 2, "lens": "entail", "verdict": "support", "reason": "The quote states it."}
        self.assertEqual(self.vote("Editor-Z", vote)[0], 1)
        self.assertEqual(self.vote("verifier-x", vote)[0], 0)


class NumbersAndUnits(Case):
    """H2: M5 sees a unit after an adjective or two spaces, a magnitude word or suffix, and a number in words."""

    def reject_m5(self, claim, display, quote):
        code, result, err = self.add(fact(id="widget-x-num", claim=claim, values=[{"key": "v", "display": display}],
                                          evidence=[{"source_id": SID, "url": URL, "quote": quote}], **SOFT))
        self.assertEqual(code, 1, err or result)
        self.assertIn("M5", self.codes(result))
        self.assertNotIn("widget-x-num", self.stored())

    def test_must_fail_f06_unit_after_an_adjective(self):
        self.reject_m5("Widget Store deletes an empty crate after 7 full hours.", "7 full hours",
                       "Widget Store deletes an empty crate after 7 days.")

    def test_must_fail_f07_unit_after_two_spaces(self):
        self.reject_m5("Widget Store deletes an empty crate after 7  hours.", "7  hours",
                       "Widget Store deletes an empty crate after 7 days.")

    def test_must_fail_f08_magnitude_word(self):
        self.reject_m5("A crate holds 50 thousand widgets.", "50 thousand widgets", "A crate can hold up to 50 widgets.")

    def test_must_fail_f09_magnitude_suffix(self):
        self.reject_m5("A crate holds 50K widgets.", "50K widgets", "A crate can hold up to 50 widgets.")

    def test_must_fail_f10_number_in_words(self):
        self.reject_m5("A shelf holds nine hundred widgets.", "nine hundred widgets", "Each shelf can hold up to 500 widgets.")

    def test_number_phrases_in_process(self):
        with sandbox.paths(self.book):
            from saalib import facts
            ctx = facts._Ctx()

            def nums(text, quote_side=False):
                return [(n["num"], n["unit"], n.get("mag")) for n in facts._numbers_of(text, ctx, quote_side)[0]]
            self.assertEqual(nums("nine hundred widgets"), [("900", None, None)])
            self.assertEqual(nums("twenty-five days"), [("25", "days", None)])
            self.assertEqual(nums("two thousand five hundred", quote_side=True), [("2500", None, None)])
            self.assertEqual(nums("50 thousand widgets"), [("50", None, "thousand")])
            self.assertEqual(nums("50K widgets"), [("50", None, "thousand")])
            self.assertEqual(nums("5 MB"), [("5", "MB", None)])
            self.assertEqual(nums("after 7 full hours"), [("7", "hours", None)])
            self.assertEqual(nums("one of the shelves"), [])


class QuoteShape(Case):
    """H3, H4 and H6: a quote is whole sentences of the page, with no hidden text, and no flattened table."""

    def reject(self, code, quote, claim="You can move a shelf to another Region.", display="move a shelf to another Region"):
        exit_code, result, err = self.add(fact(id="widget-x-quote", claim=claim, values=[{"key": "v", "display": display}],
                                               evidence=[{"source_id": SID, "url": URL, "quote": quote}], **SOFT))
        self.assertEqual(exit_code, 1, err or result)
        self.assertIn(code, self.codes(result))
        self.assertNotIn("widget-x-quote", self.stored())

    def test_must_fail_f03_quote_that_starts_in_the_middle_of_a_sentence(self):
        self.reject("M4", "move a shelf to another Region. To use another Region, copy the shelf.")

    def test_must_fail_quote_that_ends_in_the_middle_of_a_sentence(self):
        self.reject("M4", "A shelf is a Regional resource. A shelf stores widgets in one",
                    claim="A shelf is a Regional resource.", display="Regional resource")

    def test_must_fail_f17_quote_across_a_heading(self):
        self.reject("M8", "To use another Region, copy the shelf. Crates A crate is a container for widgets that you ship between Regions.",
                    claim="You copy the shelf to a crate.", display="copy the shelf")

    def test_must_fail_f18_words_hidden_in_angle_brackets(self):
        self.reject("M3", "You <can now move a shelf, where before you> cannot move a shelf to another Region. "
                          "To use another Region, copy the shelf.", display="can now move a shelf")

    def test_must_fail_number_hidden_in_a_list_prefix(self):
        self.reject("M3", "A crate can hold up to\n999) 50 widgets.", claim="A crate holds many widgets.", display="50 widgets")

    def test_must_fail_f16_flattened_table_text(self):
        self.reject("M4", "Resource Default Adjustable Shelves per Region 20 Yes Widgets per shelf 500 No",
                    claim="An account starts with many shelves in each Region.", display="Shelves per Region")

    def test_must_fail_f20_navigation_text(self):
        sentence = "AWS Documentation Amazon Widget Store User Guide Feedback Preferences Contact Us English Create an AWS Account"
        sid, url = self.page("nav2", "# Widget page\n\n" + sentence + "\n")
        code, result, err = self.add(fact(id="widget-x-nav", claim="The user guide has a feedback link.", **SOFT,
                                          values=[{"key": "v", "display": "User Guide"}],
                                          evidence=[{"source_id": sid, "url": url, "quote": sentence}]))
        self.assertEqual(code, 1, err or result)
        self.assertIn("M8", self.codes(result))

    def test_whole_sentences_over_two_lines_are_accepted(self):
        code, result, err = self.add(fact(
            id="widget-x-two", claim="A shelf stores widgets in one AWS Region and holds up to 500 widgets.",
            kind="limit", question="How many widgets does a shelf hold?", values=[{"key": "v", "display": "500 widgets"}],
            qualifiers={"scope": "per shelf", "default_or_max": "max", "adjustable": False, "condition": ""},
            evidence=[{"source_id": SID, "url": URL,
                       "quote": "A shelf stores widgets in one AWS Region. Each shelf can hold up to 500 widgets."}]))
        self.assertEqual(code, 0, err or result)


class SnapshotProvenance(Case):
    """H5: a snapshot that the fetch tool did not write, or that was edited afterwards, is no evidence."""

    def test_must_fail_f19_hand_written_snapshot(self):
        sentence = "Widget Store bills each shelf for the widgets that it holds every month."
        base = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store"
        (base / "pricing.txt").write_text("# Pricing\n\n" + sentence + "\n", encoding="utf-8")
        url = "https://docs.aws.amazon.com/widget-store/latest/userguide/pricing.html"
        common.write_json(base / "pricing.meta.json", {"source_id": "docs/fixture/widget-store/pricing", "url": url,
                                                       "title": "Amazon Widget Store pricing"})
        code, result, err = self.add(fact(id="widget-x-fake", claim="Widget Store bills each shelf for its widgets.", **SOFT,
                                          values=[{"key": "v", "display": "bills each shelf"}],
                                          evidence=[{"source_id": "docs/fixture/widget-store/pricing", "url": url, "quote": sentence}]))
        self.assertEqual(code, 1, err or result)
        self.assertEqual(self.codes(result), {"M2"})

    def test_must_fail_f22_new_fact_on_an_edited_snapshot(self):
        sentence = "A shelf can also hold up to 9000 widgets when you ask for it."
        path = self.book / "_build" / "corpus" / "snap" / (SID + ".txt")
        path.write_text(path.read_text(encoding="utf-8") + "\n" + sentence + "\n", encoding="utf-8")
        code, result, err = self.add(fact(id="widget-x-tamper", claim="A shelf holds up to 9000 widgets on request.", kind="limit",
                                          values=[{"key": "v", "display": "9000 widgets"}],
                                          qualifiers={"scope": "per shelf", "default_or_max": "max", "adjustable": True, "condition": ""},
                                          evidence=[{"source_id": SID, "url": URL, "quote": sentence}]))
        self.assertEqual(code, 1, err or result)
        self.assertEqual(self.codes(result), {"M2"})

    def test_must_fail_fixture_snapshot_in_the_real_book(self):
        with sandbox.paths(self.book):
            from saalib import facts
            snap = facts._Ctx().snap(SID)
            self.assertIsNone(facts._provenance(SID, snap))
            real = common.REAL_BOOK
            try:
                common.REAL_BOOK = self.book          # pretend that the sandbox is the real book
                self.assertIn("fixture", facts._provenance(SID, snap))
            finally:
                common.REAL_BOOK = real


class Voters(Case):
    """H7 and H8: labels are compared without case, a voter votes once per rev and lens, votes are bound to content."""

    def entail(self, verdict="support", rev=1, fid=None):
        return {"fact": fid or BASE["id"], "rev": rev, "lens": "entail", "verdict": verdict,
                "reason": "The quote states the claim word for word."}

    def test_must_fail_f14_author_votes_under_another_case(self):
        self.add(fact())
        before = self.votes_file.read_bytes()
        for label in ("Miner-A", "MINER_A", "miner a"):
            code, result, err = self.vote(label, self.entail())
            self.assertEqual(code, 1, err)
        self.assertEqual(self.votes_file.read_bytes(), before)

    def test_must_fail_f15_second_vote_under_the_label_of_a_disputing_voter(self):
        self.add(fact())
        self.assertEqual(self.vote("verifier-b", self.entail(verdict="not-supported"))[0], 0)
        self.assertEqual(sandbox.run_json(self.book, "facts", "finalize", BASE["id"])[0], 1)
        self.assertEqual(self.vote("verifier-b", self.entail())[0], 1)
        self.assertEqual(self.vote("Verifier-B", self.entail())[0], 1)
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        self.assertEqual((code, result["disputed"]), (1, [BASE["id"]]))

    def test_must_fail_later_positive_line_in_the_log_does_not_cancel_a_negative_vote(self):
        self.add(fact())
        self.vote("verifier-b", self.entail(verdict="not-supported"))
        rows = common.read_jsonl(self.votes_file)
        common.write_jsonl(self.votes_file, rows + [dict(rows[-1], verdict="support")])
        code, result, _err = sandbox.run_json(self.book, "facts", "finalize", BASE["id"])
        self.assertEqual((code, result["disputed"]), (1, [BASE["id"]]))

    def test_must_fail_f25_hand_edited_claim_loses_its_votes(self):
        self.edit_fact("widget-shelf-move", lambda row: row.update(
            claim="You can move a shelf to another Region. To use another Region, copy the shelf."))
        code, result, _err = sandbox.run_json(self.book, "facts", "verify", "widget-shelf-move")
        self.assertEqual(code, 1)
        self.assertIn("F04", {f["code"] for f in result["failed"][0]["errors"]})
        self.assertEqual(self.stored()["widget-shelf-move"]["status"], "candidate")

    def test_must_fail_vote_line_without_a_content_hash_does_not_count(self):
        self.add(fact())
        self.edit_fact(BASE["id"], lambda row: row.update(status="verified"))
        common.append_jsonl(self.votes_file, dict(self.entail(), voter="verifier-x", ts="2026-10-04T00:00:00Z", batch=None,
                                                  source_id=None, quote=None, answer=None))
        with sandbox.paths(self.book):
            from saalib import facts
            gate = facts.gate_final("99")
            self.assertIn("F04", [f["code"] for f in gate["errors"] if f["item"] == BASE["id"]])

    def test_vote_stores_the_content_hash(self):
        self.add(fact())
        self.vote("verifier-x", self.entail())
        with sandbox.paths(self.book):
            from saalib import facts
            self.assertEqual(common.read_jsonl(self.votes_file)[-1]["content"], facts.content_hash(self.stored()[BASE["id"]]))


class DisplayBoundaries(Case):
    """W0 follow-up 3: a display that sits inside a longer number is not present (lint.holds_display rule) in M7
    and in the re-derivation match of the audit."""

    def test_must_fail_m7_display_inside_a_longer_number_in_process(self):
        with sandbox.paths(self.book):
            from saalib import facts
            ctx = facts._Ctx()
            for display, text in (("5 Gbps", "The link gives 45 Gbps."), ("500 widgets", "A shelf holds 2 500 widgets."),
                                  ("1,000", "The default is 11,000.")):
                row = fact(claim=text, values=[{"key": "v", "display": display}],
                           evidence=[{"source_id": SID, "url": URL, "quote": text}])
                codes = {code for code, _msg in facts._check_rest(row, ctx)}
                self.assertIn("M7", codes, f"{display!r} must not count as present in {text!r}")
            row = fact(claim="The link gives 5 Gbps.", values=[{"key": "v", "display": "5 Gbps"}],
                       evidence=[{"source_id": SID, "url": URL, "quote": "The link gives 5 Gbps."}])
            self.assertNotIn("M7", {code for code, _msg in facts._check_rest(row, ctx)})

    def test_must_fail_m7_display_inside_a_thousands_group_through_facts_add(self):
        sid, url = self.page("big-shelves", "Each big shelf can hold up to 2 500 widgets.\n")
        self.must_reject("M7", claim="Each big shelf can hold up to 2 500 widgets.",
                         question="How many widgets does a big shelf hold?",
                         values=[{"key": "max", "display": "500 widgets"}],
                         evidence=[{"source_id": sid, "url": url, "quote": "Each big shelf can hold up to 2 500 widgets."}])

    def test_must_fail_rederive_answer_holds_the_display_inside_a_longer_token(self):
        sid, _url = self.page("volumes", "Volumes of type gp30 hold the widgets of a shelf.\n"
                                          "Volumes of type gp3 hold the widgets of a crate.\n")
        row = fact(id="widget-volume-type", claim="A shelf uses gp3 volumes.", question="Which volume type does a shelf use?",
                   values=[{"key": "type", "display": "gp3"}], hard=False, kind="behavior")
        base = {"lens": "rederive", "rev": 1, "source_id": sid, "reason": "Found on the volumes page."}
        with sandbox.paths(self.book):
            from saalib import facts
            ctx = facts._Ctx()
            wrong = dict(base, answer="gp30", quote="Volumes of type gp30 hold the widgets of a shelf.")
            self.assertEqual(facts._rederive_verdict(row, wrong, ctx), "mismatch")
            right = dict(base, answer="gp3", quote="Volumes of type gp3 hold the widgets of a crate.")
            self.assertEqual(facts._rederive_verdict(row, right, ctx), "match")


class SheetLinks(Case):
    """W0 follow-up 4: the fact sheet is a reader file; a quote with a Markdown link or image prints the link text
    only. The stored quote does not change."""

    def test_sheet_prints_the_link_text_of_a_quote_only(self):
        console = "https://console.aws.amazon.com/servicequotas/home"
        quotes = {"widget-shelves-per-region": f"| Shelves per Region | 20 | [Yes]({console}) |",
                  "widget-crate-capacity": "A crate can hold up to [50 widgets](https://docs.aws.amazon.com/widget-store/latest/userguide/crates.html).",
                  "widget-shelf-move": "You cannot move a shelf ![arrow](https://d1.awsstatic.com/arrow.png) to another Region. To use another Region, copy the shelf."}
        for fid, quote in quotes.items():
            self.edit_fact(fid, lambda row, q=quote: row["evidence"][0].update(quote=q))
        code, _result, err = sandbox.run_json(self.book, "facts", "render", "--service", "widget")
        self.assertEqual(code, 0, err)
        text = (self.book / "facts" / "widget.md").read_text(encoding="utf-8")
        self.assertNotIn("console.aws.amazon.com", text)
        self.assertNotIn("d1.awsstatic.com", text)
        self.assertNotIn("crates.html", text)
        for part in ('> "Shelves per Region | 20 | Yes" (columns: Resource | Default | Adjustable)',
                     '> "A crate can hold up to 50 widgets."',
                     '> "You cannot move a shelf arrow to another Region. To use another Region, copy the shelf."'):
            self.assertIn(part, text)
        for line in text.split("\n"):
            if line.startswith('> "'):
                self.assertNotIn("](", line)
        rows = self.stored()
        for fid, quote in quotes.items():
            self.assertEqual(rows[fid]["evidence"][0]["quote"], quote)


CERT_SID = "aws/fixture/certification/certified-widget-specialist"
CERT_URL = "https://aws.amazon.com/certification/certified-widget-specialist/"


def cert_fact(quote="130 minutes", heading="Exam duration", **over):
    """A fact on the invented certification page: by default the value line `130 minutes` under `### Exam duration`."""
    ev = {"source_id": CERT_SID, "url": CERT_URL, "quote": quote}
    if heading is not None:
        ev["heading"] = heading
    body = dict(id="exam-duration-minutes", service="exam", kind="exam-policy",
                claim="The AWS Certified Widget Specialist exam lasts 130 minutes.",
                question="How long is the AWS Certified Widget Specialist exam?",
                values=[{"key": "duration", "display": "130 minutes", "spoken": "one hundred thirty minutes"}],
                qualifiers={"scope": "per exam", "default_or_max": "fixed", "adjustable": False, "condition": ""},
                evidence=[ev])
    body.update(over)
    return fact(**body)


def language_fact(quote):
    return cert_fact(quote=quote, heading="Languages offered", id="exam-language-offered", kind="behavior", hard=False,
                     question=None, claim=f"The AWS Certified Widget Specialist exam is offered in {quote}.",
                     values=[{"key": "language", "display": quote}], qualifiers={"scope": "", "default_or_max": "",
                                                                                 "adjustable": False, "condition": ""})


class HeadingScopedQuotes(Case):
    """W0c: a short value line under a heading ("### Exam duration", then "130 minutes") is evidence only when the
    evidence item names that heading, the quote is the whole line, the heading is the nearest heading above it and
    the line is among the 5 non-empty lines under it (TOOLS.md 5.2)."""

    def exam_rows(self):
        return {row["id"]: row for row in common.read_jsonl(self.book / "data" / "facts" / "exam.jsonl")}

    def reject_m4(self, row):
        code, result, err = self.add(row)
        self.assertEqual(code, 1, err or result)
        self.assertEqual(self.codes(result), {"M4"})
        self.assertNotIn(row["id"], self.exam_rows())
        return result["rejected"][0]["errors"][0]["msg"]

    def test_value_line_under_its_heading_passes_and_reaches_packet_and_sheet(self):
        code, result, err = self.add(cert_fact())
        self.assertEqual(code, 0, err or result)
        row = self.exam_rows()["exam-duration-minutes"]
        self.assertEqual(row["status"], "mech-pass")
        self.assertEqual((row["evidence"][0]["quote"], row["evidence"][0]["heading"]), ("130 minutes", "Exam duration"))
        code, result, err = sandbox.run_json(self.book, "facts", "batch", "--chapter", "99", "--lens", "entail")
        self.assertEqual((code, result["batches"]), (0, ["99-entail-001"]), err)
        out = self.book / "_in" / "packet.json"
        code, _out, err = sandbox.run(self.book, "facts", "packet", "99-entail-001", "--out", str(out))
        self.assertEqual(code, 0, err)
        ev = common.read_json(out)["facts"][0]["evidence"][0]
        self.assertEqual((ev["heading"], ev["quote"]), ("Exam duration", "130 minutes"))
        self.assertIn("### Exam duration", ev["context"])
        vote = {"fact": "exam-duration-minutes", "rev": 1, "lens": "entail", "verdict": "support",
                "reason": "The value line under the heading Exam duration states 130 minutes."}
        self.assertEqual(self.vote("verifier-x", vote)[0], 0)
        code, result, err = sandbox.run_json(self.book, "facts", "finalize", "exam-duration-minutes")
        self.assertEqual((code, result["verified"]), (0, ["exam-duration-minutes"]), err or result)
        code, _result, err = sandbox.run_json(self.book, "facts", "render", "--service", "exam")
        self.assertEqual(code, 0, err)
        sheet = (self.book / "facts" / "exam.md").read_text(encoding="utf-8")
        self.assertIn('> Exam duration: "130 minutes"', sheet)
        code, result, err = sandbox.run_json(self.book, "facts", "card", "exam-duration-minutes")
        self.assertEqual(code, 0, err)
        self.assertEqual(set(result["cards"][0]), {"id", "status", "claim", "scope", "links", "spoken", "changed"})

    def test_heading_is_part_of_the_content_hash(self):
        with sandbox.paths(self.book):
            from saalib import facts
            row = cert_fact()
            other = cert_fact(heading="Category")
            self.assertNotEqual(facts.content_hash(row), facts.content_hash(other))
            plain = fact()
            self.assertEqual(facts.content_hash(plain), facts.content_hash(dict(plain, evidence=[
                dict(plain["evidence"][0], heading=None)])))

    def test_must_fail_short_quote_without_heading(self):
        self.reject_m4(cert_fact(heading=None))

    def test_must_fail_heading_that_is_not_the_nearest_heading_above_the_line(self):
        self.assertIn("nearest heading", self.reject_m4(cert_fact(heading="Category")))

    def test_must_fail_quote_that_is_not_a_whole_line(self):
        msg = self.reject_m4(cert_fact(quote="65 questions", heading="Exam format", id="exam-question-count",
                                       claim="The AWS Certified Widget Specialist exam has 65 questions.",
                                       question="How many questions does the exam have?",
                                       values=[{"key": "count", "display": "65 questions"}]))
        self.assertIn("whole line", msg)

    def test_must_fail_heading_that_is_not_in_the_snapshot(self):
        self.assertIn("not a heading", self.reject_m4(cert_fact(heading="Exam length")))

    def test_must_fail_value_line_more_than_five_lines_below_the_heading(self):
        self.assertIn("5", self.reject_m4(language_fact("Simplified Chinese")))
        code, result, err = self.add(language_fact("Portuguese (Brazil)"))          # the fifth line still counts
        self.assertEqual(code, 0, err or result)

    def test_must_fail_heading_together_with_a_table_header(self):
        row = cert_fact()
        row["evidence"][0]["table_header"] = "| Resource | Default | Adjustable |"
        self.reject_m4(row)

    def test_adopt_heading_builds_the_evidence(self):
        body = cert_fact()
        del body["evidence"]
        code, result, err = sandbox.run_json(self.book, "facts", "adopt", "--source", CERT_SID, "--heading", "Exam duration",
                                             "--file", self.put("one.json", body), "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        ev = self.exam_rows()["exam-duration-minutes"]["evidence"][0]
        self.assertEqual((ev["quote"], ev["heading"], ev["url"], ev["table_header"]),
                         ("130 minutes", "Exam duration", CERT_URL, None))
        body = language_fact("Portuguese (Brazil)")
        del body["evidence"]
        code, result, err = sandbox.run_json(self.book, "facts", "adopt", "--source", CERT_SID, "--heading",
                                             "Languages offered", "--line", "5", "--file", self.put("two.json", body),
                                             "--by", "miner-a")
        self.assertEqual(code, 0, err or result)
        self.assertEqual(self.exam_rows()["exam-language-offered"]["evidence"][0]["quote"], "Portuguese (Brazil)")

    def test_must_fail_adopt_heading_that_is_not_in_the_snapshot(self):
        body = cert_fact()
        del body["evidence"]
        code, _out, err = sandbox.run(self.book, "facts", "adopt", "--source", CERT_SID, "--heading", "Exam length",
                                      "--file", self.put("one.json", body), "--by", "miner-a")
        self.assertEqual(code, 1, err)
        self.assertEqual(self.exam_rows(), {})


if __name__ == "__main__":
    unittest.main()
