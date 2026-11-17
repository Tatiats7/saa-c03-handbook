"""Tests of saalib/lint.py (chapter lint, shared functions, sync). Every test works on a sandbox copy of the fixture.

A must-fail test changes one thing in the sandbox and asserts the exit code and the finding code.
"""
import re
import unittest

import sandbox
from saalib import common, lint, schemas

ANCHOR = "This default protects the widgets of a new project from a mistake."
NEW_H3 = """### {heading} (3 min)

{body}

**Stop and answer.** Ben picks Frankfurt for a new shelf. Where does the shelf store its widgets?

<details>
<summary>Answer</summary>

In Frankfurt.

</details>

## Numbers that decide answers (1 min)"""


class Base(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("lint-" + self.id().split(".")[-1][:60])
        self.fast = self.book / "99-sample" / "1-fast.md"
        self.deep = self.book / "99-sample" / "2-deep.md"

    def tearDown(self):
        sandbox.remove(self.book)

    def lint(self, *extra, draft=True):
        args = ["lint", "99"] + (["--draft"] if draft else []) + list(extra)
        code, result, err = sandbox.run_json(self.book, *args)
        self.assertIsNotNone(result, err)
        return code, result

    def add_sentence(self, sentence):
        sandbox.replace_text(self.deep, ANCHOR, ANCHOR + " " + sentence)

    def fails_with(self, rule, draft=True, contains=None):
        code, result = self.lint(draft=draft)
        hits = [f for f in result["errors"] if f["code"] == rule]
        self.assertEqual(code, 1, result["errors"])
        self.assertTrue(hits, f"{rule} not in {[f['code'] for f in result['errors']]}")
        if contains:
            self.assertTrue(any(contains in f["msg"] for f in hits), hits)
        return result

    def sync(self, *extra):
        return sandbox.run_json(self.book, "sync", "99", *extra)


class FixturePasses(Base):
    def test_fixture_has_no_blocking_finding_in_draft_mode(self):
        code, result = self.lint()
        self.assertEqual(result["errors"], [])
        self.assertEqual(code, 2)
        self.assertIn("W307", [f["code"] for f in result["warnings"]])
        self.assertEqual(result["counts"]["minutes"], {"fast": 16, "pass": 38, "full": 52})
        self.assertGreater(result["counts"]["fact_links"], 20)
        report = common.read_json(self.book / "_build" / "reports" / "lint" / "99.json")
        self.assertEqual(report["chapter"], "99")

    def test_fixture_passes_without_draft_after_sync(self):
        self.assertEqual(self.sync()[0], 0)
        code, result = self.lint(draft=False)
        self.assertEqual(result["errors"], [])
        self.assertEqual(code, 2)

    def test_read_only_is_not_an_absolute_word(self):
        self.add_sentence("The shelf is read-only for other teams.")
        code, result = self.lint()
        self.assertEqual(result["errors"], [])

    def test_no_fact_requirement_marker_is_a_warning(self):
        self.add_sentence("Use a shelf when the widgets must stay in Germany. <!-- no-fact: requirement -->")
        code, result = self.lint()
        self.assertEqual(result["errors"], [])
        self.assertIn("W308", [f["code"] for f in result["warnings"]])

    def test_study_time_in_heuristic_text_needs_no_link(self):
        with sandbox.paths(self.book):
            self.assertEqual(lint.check_text("The team studies 20 minutes a day.", "x", "heuristic"), [])
            self.assertEqual(lint.check_text("You must always read the last sentence first.", "x", "heuristic"), [])
            codes = [f["code"] for f in lint.check_text("The exam takes 130 minutes.", "x", "heuristic")]
            self.assertEqual(codes, ["L305"])

    def test_missing_svg_is_a_warning_in_draft_mode(self):
        (self.book / "diagrams" / "svg" / "sample-hero.svg").unlink()
        code, result = self.lint()
        self.assertEqual(result["errors"], [])
        self.assertIn("L701", [f["code"] for f in result["warnings"]])

    def test_file_option_filters_the_findings(self):
        self.add_sentence("Teams leverage shelves.")
        code, result = self.lint("--file", "1-fast.md")
        self.assertEqual(result["errors"], [])
        code, result = self.lint("--file", "2-deep.md")
        self.assertEqual(code, 1)


class MustFailStructure(Base):
    def test_must_fail_missing_required_section(self):
        sandbox.replace_text(self.fast, "## Check (1 min)\n<!-- section: role=check; route=fast; minutes=1 -->\n", "")
        self.fails_with("L104", contains="missing required section")

    def test_must_fail_sections_out_of_order(self):
        text = self.fast.read_text(encoding="utf-8")
        a = "## Check (1 min)\n<!-- section: role=check; route=fast; minutes=1 -->"
        b = "## Recap from memory (1 min)\n<!-- section: role=recap; route=fast; minutes=1 -->"
        self.assertIn(a, text)
        self.assertIn(b, text)
        self.fast.write_text(text.replace(a, "@@").replace(b, a).replace("@@", b), encoding="utf-8")
        self.fails_with("L104", contains="out of order")

    def test_must_fail_file_over_word_limit(self):
        with open(self.fast, "a", encoding="utf-8") as f:
            f.write("\n" + "\n\n".join("The team counts the widgets on the shelf again." for _ in range(60)) + "\n")
        self.fails_with("L201")

    def test_must_fail_missing_hand_file(self):
        self.deep.unlink()
        self.fails_with("L101")

    def test_must_fail_front_matter_differs_from_registry(self):
        sandbox.replace_text(self.fast, "slug: sample", "slug: simple")
        self.fails_with("L102")

    def test_must_fail_h1_differs_from_title(self):
        sandbox.replace_text(self.deep, "# Amazon Widget Store in depth", "# Widget Store in depth")
        self.fails_with("L103")

    def test_must_fail_flag_minutes_differ_from_heading(self):
        sandbox.replace_text(self.fast, "<!-- section: role=check; route=fast; minutes=1 -->", "<!-- section: role=check; route=fast; minutes=2 -->")
        self.fails_with("L105")

    def test_must_fail_wrong_prompt_count(self):
        sandbox.replace_text(self.fast, "**Predict 2.** A team has 600 widgets. Do the widgets fit on one shelf?\n\n", "")
        self.fails_with("L106")

    def test_must_fail_predict_prompt_without_question_mark(self):
        sandbox.replace_text(self.fast, "A team has 600 widgets. Do the widgets fit on one shelf?", "A team has 600 widgets. The widgets fit on one shelf.")
        self.fails_with("L107")

    def test_must_fail_changed_recently_line_without_br(self):
        old = "> **Old:** [200 widgets](../facts/widget.md#widget-shelf-max-widgets).<br>"
        sandbox.replace_text(self.fast, old, old[:-4])
        self.fails_with("L107")

    def test_must_fail_duplicate_section_id(self):
        block = NEW_H3.format(heading="A new shelf is private until the owner changes it", body="A team picks the Region at the start.")
        sandbox.replace_text(self.deep, "## Numbers that decide answers (1 min)", block)
        self.fails_with("L108")

    def test_must_fail_heading_with_absolute_word_and_no_fact_link(self):
        block = NEW_H3.format(heading="A shelf always stays in one Region", body="A team picks the Region at the start.")
        sandbox.replace_text(self.deep, "## Numbers that decide answers (1 min)", block)
        self.fails_with("L308")

    def test_must_fail_five_column_table_in_fast_file(self):
        text = self.fast.read_text(encoding="utf-8")
        start = text.index("<!-- table: compare -->")
        end = text.index("\n\n", start)
        rows = text[start:end].split("\n")
        rows = [rows[0]] + [r + (" --- | --- |" if set(r) <= set("|-: ") else " more | more |") for r in rows[1:]]
        self.fast.write_text(text[:start] + "\n".join(rows) + text[end:], encoding="utf-8")
        self.fails_with("L502")

    def test_must_fail_table_without_kind_comment(self):
        sandbox.replace_text(self.fast, "<!-- table: words -->\n", "")
        self.fails_with("L501")

    def test_must_fail_signals_cell_without_quotes(self):
        sandbox.replace_text(self.fast, '| "send widgets to another Region" |', "| send widgets to another Region |")
        self.fails_with("L503")

    def test_must_fail_code_block_without_language(self):
        sandbox.replace_text(self.deep, "```json", "```")
        self.fails_with("L804")


class MustFailFacts(Base):
    def test_must_fail_fact_link_to_unknown_fact(self):
        sandbox.replace_text(self.fast, "#widget-crate-capacity)", "#widget-crate-nothing)")
        self.fails_with("L301")

    def test_must_fail_link_text_without_canonical_value(self):
        sandbox.replace_text(self.fast, "[500 widgets](../facts/widget.md#widget-shelf-max-widgets) | [50", "[many widgets](../facts/widget.md#widget-shelf-max-widgets) | [50")
        self.fails_with("L303")

    def test_must_fail_link_text_with_wrong_number_that_ends_like_the_value(self):
        # W0 integration: `150 widgets` holds the display `50 widgets` as a plain substring.
        sandbox.replace_text(self.fast, "| [50 widgets](../facts/widget.md#widget-crate-capacity) |",
                             "| [150 widgets](../facts/widget.md#widget-crate-capacity) |")
        self.fails_with("L303")

    def test_holds_display_number_boundaries(self):
        self.assertTrue(lint.holds_display("up to 500 widgets.", "500 widgets"))
        self.assertTrue(lint.holds_display("5 gbps", "5 gbps"))
        self.assertFalse(lint.holds_display("up to 45 gbps", "5 gbps"))
        self.assertFalse(lint.holds_display("1,500 widgets", "500 widgets"))
        self.assertFalse(lint.holds_display("0.5 gbps", "5 gbps"))
        self.assertFalse(lint.holds_display("port 4430", "port 443"))
        self.assertFalse(lint.holds_display("port 443.5", "port 443"))
        self.assertTrue(lint.holds_display("port 443, then", "port 443"))
        self.assertTrue(lint.holds_display("security groups", "security group"))
        self.assertFalse(lint.holds_display("anything", ""))

    def test_must_fail_link_to_unverified_fact(self):
        def change(rows):
            next(r for r in rows if r["id"] == "widget-crate-capacity")["status"] = "disputed"
        sandbox.edit_jsonl(self.book / "data" / "facts" / "widget.jsonl", change)
        self.fails_with("L302")

    def test_must_fail_bare_number_with_unit_in_explanatory_section(self):
        self.add_sentence("A shelf answers in 5 ms.")
        self.fails_with("L304", contains="5 ms")

    def test_must_fail_absolute_word_without_fact_link(self):
        self.add_sentence("A shelf never leaves its Region.")
        self.fails_with("L304", contains="never")

    def test_must_fail_always_keeps_3_copies(self):
        self.add_sentence("Each shelf always keeps 3 copies.")
        self.fails_with("L304", contains="3 copies")

    def test_must_fail_must_after_exam_signal_phrase(self):
        sandbox.replace_text(self.deep, "points to a shelf, not to a crate.", "must point to a shelf, not to a crate.")
        self.fails_with("L304", contains="must")

    def test_must_fail_unknown_no_fact_reason(self):
        self.add_sentence("A shelf never leaves its Region. <!-- no-fact: because -->")
        self.fails_with("L304")

    def test_must_fail_number_with_unit_in_exam_heuristic(self):
        sandbox.replace_text(self.deep, "prefers the option that keeps the secure default.",
                             "prefers the option that keeps the secure default. The exam takes 130 minutes.")
        self.fails_with("L305")

    def test_must_fail_aws_quote_changed_by_one_word(self):
        sandbox.replace_text(self.deep, '> "You cannot move a shelf to another Region."', '> "You cannot ship a shelf to another Region."')
        self.fails_with("L306")

    def test_must_fail_needs_fact_marker_in_ready_file(self):
        code, result = self.lint("--strict")
        self.assertEqual(code, 1)
        self.assertIn("L307", [f["code"] for f in result["errors"]])


class MustFailStyle(Base):
    def test_must_fail_unknown_callout_label(self):
        sandbox.replace_text(self.deep, "> **Key fact:**", "> **Remember:**")
        self.fails_with("L401")

    def test_must_fail_banned_word(self):
        self.add_sentence("Teams leverage shelves.")
        self.fails_with("L801", contains="leverage")

    def test_must_fail_former_name(self):
        self.add_sentence("Teams chart their widgets in QuickSight.")
        self.fails_with("L802")

    def test_must_fail_contraction(self):
        self.add_sentence("The shelf doesn't move.")
        self.fails_with("L803")

    def test_must_fail_sentence_over_the_maximum(self):
        self.add_sentence("The owner of the shelf " + "and the owner of the next shelf " * 6 + "count the widgets together.")
        self.fails_with("L202", contains="sentence")

    def test_must_fail_banned_term_variant_in_alt_text(self):
        sandbox.replace_text(self.fast, "A Region frame that contains one shelf, and a team outside the frame",
                             "A Region box that contains one shelf, and a team outside the box")
        self.fails_with("L901")

    def test_must_fail_broken_cross_reference(self):
        sandbox.replace_text(self.deep, "1-fast.md#signals-and-traps-2-min", "1-fast.md#signals-and-traps-9-min")
        self.fails_with("L601")

    def test_must_fail_bare_url(self):
        self.add_sentence("Read https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html for more.")
        self.fails_with("L602")

    def test_must_fail_external_link_in_prose(self):
        self.add_sentence("Read the [limits page](https://example.com/limits) for more.")
        self.fails_with("L602")

    def test_must_fail_trap_id_defined_twice(self):
        sandbox.replace_text(self.fast, "<!-- trap: sample-trap-shelf-unlimited -->", "<!-- trap: sample-trap-shelf-move -->")
        self.fails_with("L604")

    def test_must_fail_missing_diagram_file(self):
        self.assertEqual(self.sync()[0], 0)
        (self.book / "diagrams" / "svg" / "sample-hero.svg").unlink()
        self.fails_with("L701", draft=False)

    def test_must_fail_caption_missing(self):
        sandbox.replace_text(self.fast, "**Figure.** A shelf sits inside one Region, and the team reaches the shelf from outside.\n\n", "")
        self.fails_with("L702")

    def test_must_fail_brief_trap_missing_from_hand_files(self):
        self.assertEqual(self.sync()[0], 0)
        common.write_json(self.book / "_build" / "work" / "99-sample" / "brief.json",
                          {"chapter": "99", "sections": [], "traps": [{"id": "sample-trap-not-written", "belief": "x", "truth": "y", "facts": []}]})
        self.fails_with("L905", draft=False)


class SharedFunctions(Base):
    def test_template_and_helpers(self):
        with sandbox.paths(self.book):
            tpl = lint.template("99")
            self.assertEqual(tpl["key"], "deep")
            self.assertEqual([f["name"] for f in tpl["files"]][:2], ["1-fast.md", "2-deep.md"])
            self.assertEqual(lint.anchor("Check (2 min)"), "check-2-min")
            self.assertEqual(lint.section_id("Signals and traps (4 min)"), "signals-and-traps")
            self.assertEqual(lint.word_count("One [two three](../facts/a.md#a-b) <!-- no --> | four |\n\n```bash\nfive\n```\n"), 4)

    def test_sections_traps_and_a_list(self):
        with sandbox.paths(self.book):
            secs = lint.sections("99")
            row = secs["2-deep.md"]["a-shelf-belongs-to-one-region-for-its-whole-life"]
            self.assertEqual((row["level"], row["parent"], row["route"], row["role"], row["minutes"], row["planned"]),
                             (3, "how-it-works", "pass", "how", 3, False))
            self.assertEqual(row["anchor"], "a-shelf-belongs-to-one-region-for-its-whole-life-3-min")
            self.assertEqual(secs["1-fast.md"]["look-first"]["role"], "task")
            self.assertEqual(lint.traps(), {"sample-trap-shelf-global": "99", "sample-trap-shelf-move": "99", "sample-trap-shelf-unlimited": "99"})
            self.assertEqual(lint.a_list_facts("99"), ["widget-shelf-max-widgets"])

    def test_brief_adds_planned_sections_and_traps(self):
        common.write_json(self.book / "_build" / "work" / "99-sample" / "brief.json",
                          {"chapter": "99", "sections": [{"file": "2-deep.md", "section": "a-planned-subsection", "heading": "A planned subsection"}],
                           "traps": [{"id": "sample-trap-planned", "belief": "x", "truth": "y", "facts": []}]})
        with sandbox.paths(self.book):
            self.assertTrue(lint.sections("99")["2-deep.md"]["a-planned-subsection"]["planned"])
            self.assertEqual(lint.traps()["sample-trap-planned"], "99")

    def test_must_fail_strict_text_plain_value(self):
        with sandbox.paths(self.book):
            found = lint.check_strict_text("A shelf holds up to 500 widgets.", "sample-q001")
            self.assertEqual([f["code"] for f in found], ["L304"])
            self.assertEqual(found[0]["item"], "sample-q001")
            ok = "A shelf holds [up to 500 widgets](../facts/widget.md#widget-shelf-max-widgets)."
            self.assertEqual(lint.check_strict_text(ok, "sample-q001"), [])

    def test_must_fail_strict_text_links_and_words(self):
        with sandbox.paths(self.book):
            codes = lambda text, stem=None: [f["code"] for f in lint.check_strict_text(text, "q", stem)]
            self.assertEqual(codes("A crate holds [50 widgets](../facts/widget.md#widget-crate-none)."), ["L301"])
            self.assertEqual(codes("A crate holds [some widgets](../facts/widget.md#widget-crate-capacity)."), ["L303"])
            self.assertEqual(codes("Teams leverage a crate."), ["L801"])
            self.assertEqual(codes("The 40 widgets fit in one crate."), ["L304"])
            self.assertEqual(codes("The 40 widgets fit in one crate.", stem="A partner needs 40 of the widgets."), [])
            self.assertEqual(codes('If the stem said "add 50 more widgets" instead: keep the shelf.'), [])
            self.assertEqual(codes("Does a shelf always stay?"), [])

    def test_gate_lint_is_a_valid_gate_record(self):
        with sandbox.paths(self.book):
            gate = lint.gate_lint("99", draft=True)
            self.assertEqual(schemas.validate(gate, "gate"), [])
            self.assertTrue(gate["ok"])
            self.assertEqual(gate["exit"], 2)
            self.assertIn("99-sample/1-fast.md", [i["path"] for i in gate["inputs"]])

    def test_must_fail_gate_lint_without_draft_on_fresh_fixture(self):
        with sandbox.paths(self.book):
            gate = lint.gate_lint("99")
            self.assertFalse(gate["ok"])
            self.assertEqual(gate["exit"], 1)
            self.assertEqual({f["code"] for f in gate["errors"]}, {"L101", "L601"})     # L601: the fact sheet is not built yet


class OtherTemplates(Base):
    """Smoke test: the real SPEC.json with a skeleton chapter of every other template. No rule may crash."""

    CARD = ("**Formerly.** Amazon Old Name.\n\n**What it is.** A managed service for tests.\n\n**Stem signals.**\n\n"
            "- \"first stem phrase\"\n- \"second stem phrase\"\n\n**Do not confuse with.** Other Service: it differs.\n\n"
            "> **Say it:** A short sentence to say.\n\n**Source.** [Page](https://docs.aws.amazon.com/example/latest/ug/what-is.html)\n")
    PATTERN = ("### Warm standby (2 min)\n\n**Problem.** A company needs an RPO of 15 minutes.\n\n**Services.** Two Regions.\n\n"
               "**Cost and effort.** Medium.\n\n**Choose when.** The budget allows it.\n\n**Not when.** Cost decides.\n\n"
               "**Common wrong alternative.** Backup and restore.\n\n**Stop and answer.** Which pattern fits?\n\n"
               "<details>\n<summary>Answer</summary>\n\nWarm standby.\n\n</details>\n")

    def test_skeleton_chapters_of_every_template_lint_and_sync(self):
        real_spec = common.REAL_BOOK / "_build" / "style" / "SPEC.json"
        seed = common.read_json(common.REAL_BOOK / "_build" / "registry" / "book.seed.json")
        if not real_spec.exists() or not seed:
            self.skipTest("no real SPEC.json or seed")
        (self.book / "_build" / "style" / "SPEC.json").write_bytes(real_spec.read_bytes())
        ids = ("00", "01", "20", "40", "44", "45", "46", "49", "50")
        entries = [dict(c, tasks=[], bullets=[]) for c in seed["chapters"] if c["id"] in ids]
        self.assertEqual(len(entries), len(ids))
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"].extend(entries))
        with sandbox.paths(self.book):
            for e in entries:
                tpl = lint.template(e)
                folder = self.book / f"{e['id']}-{e['slug']}"
                folder.mkdir()
                for fs in tpl["files"]:
                    if fs.get("source") != "hand" or (fs.get("present_when") and not e.get("cards")):
                        continue
                    first = fs["name"] == "1-fast.md"
                    head = (f"id: \"{e['id']}\"\nslug: {e['slug']}\ntitle: \"{e['title']}\"\nfile: fast\ntier: {e['tier']}\n"
                            "domains: [1]\ntasks: []\nservices: []\nminutes: {fast: 1, pass: 1, full: 1}\n" if first
                            else f"chapter: \"{e['id']}\"\nfile: deep\ntitle: \"{e['title']}\"\n")
                    out = [f"---\n{head}status: draft\nupdated: 2026-10-04\n---\n\n# {e['title']}\n"]
                    for s in fs.get("sections", []):
                        card = s.get("role") == "card"
                        title = "Example Service" if "<" in s["heading"] else s["heading"]
                        flag = f"<!-- section: role={s['role']}; route={s['route']}; minutes=2" + ("; service=batch" if card else "") + " -->"
                        body = self.CARD if card else (self.PATTERN if s.get("subsection_fields") else "The team studies 20 minutes a day.\n")
                        if s.get("counts", {}).get("plan_regions"):
                            body += f"\n<!-- plan:start id={s.get('plan', 'a')} -->\n<!-- plan:end -->\n"
                        out.append(f"## {title} (2 min)\n{flag}\n\n{body}")
                    (folder / fs["name"]).write_text("\n".join(out), encoding="utf-8")
        for e in entries:
            code, result, err = sandbox.run_json(self.book, "lint", e["id"], "--draft")
            self.assertIsNotNone(result, f"{e['id']}: {err}")
            self.assertIn(code, (1, 2), err)
            self.assertNotIn("Traceback", err)
            code, result, err = sandbox.run_json(self.book, "sync", e["id"])
            self.assertEqual(code, 0, f"{e['id']}: {err}")
            self.assertTrue(any(p.endswith("sources.md") for p in result["written"]), result)
        code, result, err = sandbox.run_json(self.book, "lint", "--all", "--draft")
        self.assertIsNotNone(result, err)
        self.assertEqual(len(result["chapters"]), len(ids) + 1)
        code, result, err = sandbox.run_json(self.book, "sync", "--all", "--check")
        self.assertIsNotNone(result, err)
        self.assertNotIn("Traceback", err)


class Sync(Base):
    def test_must_fail_fresh_sandbox_reports_missing_files(self):
        code, result, err = self.sync("--check")
        self.assertEqual(code, 1, err)
        self.assertEqual(result["missing"], ["99-sample/3-do.md", "99-sample/4-say.md", "99-sample/5-quiz.md", "99-sample/sources.md",
                                             "facts/widget.md"])
        self.assertEqual(result["stale"], ["99-sample/1-fast.md"])
        with sandbox.paths(self.book):
            gate = lint.gate_sync("99")
            self.assertFalse(gate["ok"])
            self.assertEqual({f["code"] for f in gate["errors"]}, {"S01"})
            self.assertEqual(schemas.validate(gate, "gate"), [])

    def test_sync_twice_gives_identical_bytes(self):
        code, first, err = self.sync()
        self.assertEqual(code, 0, err)
        self.assertEqual(len(first["written"]), 6)                      # five chapter files and facts/widget.md
        self.assertIn("facts/widget.md", first["written"])
        names = ["1-fast.md", "3-do.md", "4-say.md", "5-quiz.md", "sources.md"]
        before = {n: (self.book / "99-sample" / n).read_bytes() for n in names}
        self.assertTrue(before["5-quiz.md"].startswith(b"<!-- generated by saa.py; do not edit -->\n"))
        code, second, err = self.sync()
        self.assertEqual((code, second["written"], second["unchanged"]), (0, [], 6))
        self.assertEqual(before, {n: (self.book / "99-sample" / n).read_bytes() for n in names})
        self.assertEqual(self.sync("--check")[0], 0)
        with sandbox.paths(self.book):
            self.assertTrue(lint.gate_sync("99")["ok"])

    def test_must_fail_stale_after_takeaway_change(self):
        self.assertEqual(self.sync()[0], 0)

        def change(doc):
            doc["items"][0]["takeaway"] = "When one shelf is full, add a second shelf in the same Region."
        sandbox.edit_json(self.book / "data" / "99-sample" / "questions.json", change)
        before = (self.book / "99-sample" / "5-quiz.md").read_bytes()
        code, result, err = self.sync("--check")
        self.assertEqual(code, 1)
        self.assertEqual(result["stale"], ["99-sample/5-quiz.md"])
        self.assertEqual(before, (self.book / "99-sample" / "5-quiz.md").read_bytes(), "--check writes nothing")

    def test_must_fail_hand_edit_inside_task_region_is_stale(self):
        self.assertEqual(self.sync()[0], 0)
        sandbox.replace_text(self.fast, "Read the Region column of one shelf.", "Read the Region column of two shelves.")
        code, result, err = self.sync("--check")
        self.assertEqual(code, 1)
        self.assertEqual(result["stale"], ["99-sample/1-fast.md"])

    def test_hand_text_outside_regions_is_never_changed(self):
        original = self.fast.read_text(encoding="utf-8")
        self.assertEqual(self.sync()[0], 0)
        filled = self.fast.read_text(encoding="utf-8")
        self.assertIn("It kills the belief.", filled)
        emptied = re.sub(r"(<!-- task:start id=sample-t01 -->\n).*?(<!-- task:end -->)", r"\1\2", filled, flags=re.S)
        self.assertEqual(emptied, original)

    def test_candidate_question_is_not_printed(self):
        def change(doc):
            doc["items"][3]["status"] = "candidate"
        sandbox.edit_json(self.book / "data" / "99-sample" / "questions.json", change)
        self.assertEqual(self.sync()[0], 0)
        quiz = (self.book / "99-sample" / "5-quiz.md").read_text(encoding="utf-8")
        self.assertIn("quiz:start id=sample-q003", quiz)
        self.assertNotIn("sample-q004", quiz)
        self.assertEqual(quiz.count("### Question "), 3)

    def test_only_writes_the_named_kind(self):
        code, result, err = self.sync("--only", "quiz")
        self.assertEqual((code, result["written"]), (0, ["99-sample/5-quiz.md"]))

    def test_must_fail_invalid_data_file_exits_3(self):
        def change(doc):
            doc["items"][0]["difficulty"] = "hard"
        sandbox.edit_json(self.book / "data" / "99-sample" / "questions.json", change)
        code, result, err = self.sync()
        self.assertEqual(code, 3)
        self.assertEqual(result["errors"][0]["code"], "X01")
        self.assertFalse((self.book / "99-sample" / "5-quiz.md").exists())

    def test_glossary_is_generated_with_only(self):
        code, result, err = self.sync("--only", "glossary")
        self.assertEqual(code, 0, err)
        text = (self.book / "glossary.md").read_text(encoding="utf-8")
        self.assertIn("### crate\n\n**Say it.** KRAYT", text)
        self.assertLess(text.index("### crate"), text.index("### shelf"))


if __name__ == "__main__":
    unittest.main()
