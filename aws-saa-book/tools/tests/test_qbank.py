"""Tests of saalib/qbank.py: q, cards, speak, mocks, drills (TOOLS-items.md section 7).

Every test works on a sandbox copy of the fixture book. A must-fail test changes one thing and
asserts the exit code and the finding code.
"""
import copy
import os
import unittest

import sandbox
from saalib import common, qbank, schemas

SEED = 20261004
QFILE = ("data", "99-sample", "questions.json")
CFILE = ("data", "99-sample", "cards.json")
SFILE = ("data", "99-sample", "speak.json")
SOURCE = "docs/fixture/widget-store/limits"


def codes(findings):
    return [f["code"] for f in findings]


def unique_words(n, count=18):
    """Letter-only words that no other question uses, so that stems are not near-duplicates."""
    letters = "bcdfghjklm"
    return " ".join("zq" + "".join(letters[int(d)] for d in f"{n * 100 + i:05d}") for i in range(count))


def make_distinct(q, n):
    """Turn a copy of a fixture question into another question for the duplicate test (Q302, K04): one more first
    sentence in the stem and three more words in every option."""
    words = unique_words(n, 40).split()
    q["stem"] = f"A company runs the {' '.join(words[:18])} program. " + q["stem"]
    for k, option in enumerate(q["options"]):
        option["text"] = option["text"].rstrip(".") + " for " + " ".join(words[18 + 3 * k:21 + 3 * k]) + "."
    return q


class Base(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("qbank-" + self.id().split(".")[-1])

    def tearDown(self):
        sandbox.remove(self.book)

    def path(self, *parts):
        return self.book.joinpath(*parts)

    def edit_q(self, qid, change):
        def apply(doc):
            change(next(q for q in doc["items"] if q["id"] == qid))
        sandbox.edit_json(self.path(*QFILE), apply)

    def edit_item(self, parts, iid, change):
        def apply(doc):
            change(next(i for i in doc["items"] if i["id"] == iid))
        sandbox.edit_json(self.path(*parts), apply)

    def question(self, qid):
        return next(q for q in common.read_json(self.path(*QFILE))["items"] if q["id"] == qid)

    def lint(self, kind, *extra):
        return sandbox.run_json(self.book, kind, "lint", "99", *extra)

    def assert_lint_fails(self, kind, code, *extra):
        rc, result, err = self.lint(kind, *extra)
        self.assertEqual(rc, 1, err or result)
        self.assertIn(code, codes(result["errors"]))
        self.assertFalse(result["ok"])

    def write(self, name, obj):
        path = self.path(name)
        common.write_json(path, obj)
        return str(path)

    def new_question(self, change=None):
        q = copy.deepcopy(next(q for q in common.read_json(self.path(*QFILE))["items"] if q["id"] == "sample-q004"))
        del q["id"]
        make_distinct(q, 900)       # `q add` refuses a copy of a stored question (Q302)
        if change:
            change(q)
        return q

    def add_q(self, change=None, *extra):
        return sandbox.run_json(self.book, "q", "add", "--chapter", "99", "--file", self.write("in.json", self.new_question(change)), *extra)

    def assert_add_rejects(self, code, change):
        rc, result, err = self.add_q(change)
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(result["added"], [])
        self.assertIn(code, codes(result["rejected"][0]["errors"]))
        self.assertEqual(len(common.read_json(self.path(*QFILE))["items"]), 4)


# ---------------------------------------------------------------- q lint

class QuestionLint(Base):
    def test_fixture_passes(self):
        rc, result, err = self.lint("q")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result["counts"], {"total": 4, "candidate": 0, "verified": 0, "ready": 4, "rejected": 0, "multi": 1, "twin_pairs": 1})
        rc, result, err = self.lint("q", "--ship")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = sandbox.run_json(self.book, "q", "lint", "--all")
        self.assertEqual(rc, 0, err or result)

    def test_text_output_is_short(self):
        rc, out, err = sandbox.run(self.book, "q", "lint", "99")
        self.assertEqual(rc, 0, err)
        self.assertTrue(out.startswith("q lint 99: ok"))
        self.assertLessEqual(len(out.splitlines()), 41)

    def test_must_fail_wrong_option_count(self):
        fifth = {"id": "e", "text": "A second crate that stays in us-east-1.", "correct": False, "why": "A crate that stays in us-east-1 sends nothing to the partner in the other Region.",
                 "concept": "crate", "trap": None, "misconception": "keeps the crate at home", "distractor_type": "different-problem"}
        self.edit_q("sample-q004", lambda q: q["options"].append(fifth))
        self.assert_lint_fails("q", "Q102")

    def test_must_fail_three_options(self):
        self.edit_q("sample-q004", lambda q: q["options"].pop())
        self.assert_lint_fails("q", "Q101")

    def test_must_fail_multi_keys_do_not_match_select(self):
        self.edit_q("sample-q003", lambda q: q["options"][1].update(correct=False, misconception="reads the Region as a setting", distractor_type="wrong-configuration"))
        self.assert_lint_fails("q", "Q102")

    def test_must_fail_multi_select_text(self):
        self.edit_q("sample-q003", lambda q: q.update(stem=q["stem"].replace("(Select TWO.)", "(Select THREE.)")))
        self.assert_lint_fails("q", "Q102")

    def test_must_fail_single_with_select_instruction(self):
        self.edit_q("sample-q004", lambda q: q.update(stem=q["stem"] + " (Select TWO.)"))
        self.assert_lint_fails("q", "Q102")

    def test_must_fail_key_much_longer_than_other_options(self):
        long_key = ("Create a second shelf in us-east-1 with the same owner and the same settings as the first shelf, "
                    "then put all of the new widgets on the second shelf next month.")
        self.edit_q("sample-q001", lambda q: q["options"][0].update(text=long_key))
        self.assert_lint_fails("q", "Q104")

    def test_must_fail_explanation_names_an_option_letter(self):
        self.edit_q("sample-q001", lambda q: q.update(explanation=q["explanation"] + " Option B is wrong."))
        self.assert_lint_fails("q", "Q105")

    def test_must_fail_fact_id_does_not_resolve(self):
        self.edit_q("sample-q004", lambda q: q["facts"].append("widget-no-such-fact"))
        self.assert_lint_fails("q", "Q110")

    def test_must_fail_unverified_fact(self):
        def change(rows):
            next(r for r in rows if r["id"] == "widget-crate-capacity")["status"] = "disputed"
        sandbox.edit_jsonl(self.path("data", "facts", "widget.jsonl"), change)
        self.assert_lint_fails("q", "Q110")

    def test_must_fail_link_text_without_the_value(self):
        self.edit_q("sample-q004", lambda q: q.update(explanation=q["explanation"].replace("[50 widgets]", "[60 widgets]")))
        self.assert_lint_fails("q", "Q110")

    def test_must_fail_unknown_trap(self):
        self.edit_q("sample-q004", lambda q: q["options"][1].update(trap="sample-trap-no-such-trap"))
        self.assert_lint_fails("q", "Q109")

    def test_must_fail_section_does_not_resolve(self):
        self.edit_q("sample-q004", lambda q: q.update(section="1-fast.md#no-such-section"))
        self.assert_lint_fails("q", "Q111")

    def test_must_fail_bullet_of_another_task(self):
        self.edit_q("sample-q004", lambda q: q.update(bullets=["2.2.K1"]))
        self.assert_lint_fails("q", "Q111")

    def test_must_fail_volatile_fact_decides_the_key(self):
        def change(spec):
            spec["questions"]["volatile_window_months"] = 24
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), change)
        rc, result, err = self.lint("q")
        self.assertEqual(rc, 1, err)
        flagged = {f["item"] for f in result["errors"] if f["code"] == "Q112"}
        self.assertEqual(flagged, {"sample-q001", "sample-q002"})

    def test_must_fail_twin_with_the_same_key(self):
        def change(q):
            q["options"][0].update(correct=True, misconception=None, distractor_type=None)
            q["options"][1].update(correct=False, misconception="keeps one shelf", distractor_type="violates-qualifier")
        self.edit_q("sample-q002", change)
        self.assert_lint_fails("q", "Q114")

    def test_must_fail_wrong_path_marker_missing(self):
        self.edit_q("sample-q001", lambda q: q["worked"].update(wrong_path=False))
        self.assert_lint_fails("q", "Q114")

    def test_must_fail_banned_word_in_explanation(self):
        self.edit_q("sample-q004", lambda q: q.update(takeaway="Widgets that travel simply go in a crate; widgets that stay go on a shelf."))
        self.assert_lint_fails("q", "Q115")

    def test_must_fail_duplicate_signature(self):
        def change(q):
            q["concept"] = "shelf-defaults"
            q["options"][2].update(trap="sample-trap-shelf-global", misconception=None)
        self.edit_q("sample-q004", change)
        rc, result, err = self.lint("q")
        self.assertEqual(rc, 2, err or result)
        self.assertIn("Q203", codes(result["warnings"]))
        self.assert_lint_fails("q", "Q203", "--ship")

    def test_must_fail_ship_counts(self):
        self.edit_q("sample-q004", lambda q: q.update(status="verified"))
        self.assert_lint_fails("q", "Q201", "--ship")

    def test_must_fail_too_many_without_qualifier(self):
        def change(spec):
            spec["questions"]["no_qualifier_share_max"] = 0.25
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), change)
        self.assert_lint_fails("q", "Q204")

    def test_must_fail_near_duplicate_stem(self):
        copied = self.question("sample-q004")["stem"]
        self.edit_q("sample-q003", lambda q: q.update(stem=copied + " (Select TWO.)"))
        rc, result, err = sandbox.run_json(self.book, "q", "dedupe")
        self.assertEqual(rc, 1, err or result)
        pair = result["pairs"][0]
        self.assertEqual((pair["a"], pair["b"], pair["kind"]), ("sample-q003", "sample-q004", "duplicate"))
        rc, result, err = sandbox.run_json(self.book, "q", "lint", "--all")
        self.assertEqual(rc, 1)
        self.assertIn("Q302", codes(result["errors"]))

    def test_dedupe_exempts_twins(self):
        rc, result, err = sandbox.run_json(self.book, "q", "dedupe")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result["pairs"], [])

    def test_must_fail_duplicate_id(self):
        def change(doc):
            doc["items"].append(copy.deepcopy(doc["items"][3]))
        sandbox.edit_json(self.path(*QFILE), change)
        self.assert_lint_fails("q", "Q301")

    def test_list(self):
        rc, result, err = sandbox.run_json(self.book, "q", "list", "--chapter", "99", "--status", "ready")
        self.assertEqual(rc, 0, err)
        self.assertEqual(len(result["questions"]), 4)
        self.assertEqual(result["questions"][0]["concept"], "shelf-capacity")


# ---------------------------------------------------------------- q add, set-status, gates

class QuestionAdd(Base):
    def test_add_sets_the_tool_fields(self):
        rc, result, err = self.add_q(lambda q: q.update(status="ready", rev=7, volatile=True))
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result, {"added": ["sample-q005"], "replaced": [], "rejected": []})
        q = self.question("sample-q005")
        self.assertEqual((q["status"], q["rev"], q["keyRev"], q["volatile"], q["pool"]), ("candidate", 1, 1, False, "chapter"))
        self.assertEqual(q["verification"], {"status": "candidate", "round": 0, "solvers": []})

    def test_replace_a_verified_question_resets_it(self):
        def change(q):
            q.clear()
            q.update(copy.deepcopy(self.question("sample-q004")))       # the stored text: the key does not change
            q["options"][0], q["options"][1] = q["options"][1], q["options"][0]
        rc, result, err = self.add_q(change, "--replace")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result["replaced"], ["sample-q004"])
        q = self.question("sample-q004")
        self.assertEqual((q["status"], q["rev"], q["keyRev"], q["verification"]["status"]), ("candidate", 2, 1, "candidate"))

    def test_must_fail_add_an_existing_id_without_replace(self):
        self.assert_add_rejects("Q301", lambda q: q.update(id="sample-q004"))

    def test_must_fail_file_outside_the_book(self):
        rc, out, err = sandbox.run(self.book, "q", "add", "--chapter", "99", "--file", "/etc/hosts")
        self.assertEqual(rc, 4)

    def test_must_fail_two_correct_options_on_a_single(self):
        self.assert_add_rejects("Q102", lambda q: q["options"][2].update(correct=True, misconception=None, distractor_type=None))

    def test_must_fail_always_in_an_option(self):
        self.assert_add_rejects("Q105", lambda q: q["options"][3].update(text="A higher quota that always applies in us-east-1."))

    def test_must_fail_option_letter_in_explanation(self):
        self.assert_add_rejects("Q105", lambda q: q.update(explanation=q["explanation"] + " Option B is wrong."))

    def test_must_fail_keyword_not_in_stem(self):
        self.assert_add_rejects("Q107", lambda q: q.update(keywords=["needs 60 of the widgets"]))

    def test_must_fail_wrong_option_without_trap_and_misconception(self):
        self.assert_add_rejects("Q108", lambda q: q["options"][2].update(misconception=None))

    def test_must_fail_plain_number_in_explanation(self):
        text = ("The widgets travel to another Region, and a crate is the container that you ship between Regions. "
                "A shelf holds up to 500 widgets, so the shelf stays in place.")
        self.assert_add_rejects("Q110", lambda q: q.update(explanation=text))

    def test_must_fail_unverified_fact(self):
        def change(rows):
            next(r for r in rows if r["id"] == "widget-shelf-move")["status"] = "mech-pass"
        sandbox.edit_jsonl(self.path("data", "facts", "widget.jsonl"), change)
        self.assert_add_rejects("Q110", None)

    def test_must_fail_stem_repeats_the_key(self):
        def spec(s):
            s["questions"]["stem_key_overlap_margin_max"] = 0.25
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), spec)
        key = ("A crate for the partner in the ap-south-1 Region that needs 40 of the widgets next week, "
               "while the other widgets stay in us-east-1 on the shelf.")
        self.assert_add_rejects("Q113", lambda q: q["options"][0].update(text=key))

    def test_must_fail_difficulty_2_without_qualifier(self):
        self.assert_add_rejects("Q106", lambda q: q.update(difficulty=2))

    def test_must_fail_question_without_a_bullet(self):
        self.assert_add_rejects("Q116", lambda q: q.update(bullets=[]))

    def test_must_fail_set_status_ready_without_verification(self):
        self.edit_q("sample-q004", lambda q: q.update(status="candidate", verification={"status": "candidate", "round": 0, "solvers": []}))
        rc, result, err = sandbox.run_json(self.book, "q", "set-status", "--chapter", "99", "--status", "ready", "sample-q004")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(result["set"], [])
        self.assertIn("Q206", codes(result["refused"][0]["errors"]))
        self.assertEqual(self.question("sample-q004")["status"], "candidate")

    def test_set_status_retired_needs_a_reason(self):
        rc, out, err = sandbox.run(self.book, "q", "set-status", "--chapter", "99", "--status", "retired", "sample-q004")
        self.assertEqual(rc, 1)
        rc, result, err = sandbox.run_json(self.book, "q", "set-status", "--chapter", "99", "--status", "retired", "sample-q004", "--reason", "replaced")
        self.assertEqual(rc, 0, err)
        self.assertEqual(self.question("sample-q004")["status"], "retired")


class Standalone(Base):
    """The module also works when lint, facts, registry, corpus and ledger are missing (local fallbacks)."""

    def setUp(self):
        super().setUp()
        os.environ["SAA_QBANK_STANDALONE"] = "1"

    def tearDown(self):
        os.environ.pop("SAA_QBANK_STANDALONE", None)
        super().tearDown()

    def test_fixture_passes(self):
        for kind in ("q", "cards", "speak"):
            rc, result, err = self.lint(kind, "--ship")
            self.assertEqual(rc, 0, err or result)

    def test_must_fail_plain_number_in_explanation(self):
        self.edit_q("sample-q004", lambda q: q.update(explanation=q["explanation"] + " A shelf holds up to 500 widgets."))
        self.assert_lint_fails("q", "Q110")

    def test_must_fail_unknown_trap_section_and_fact(self):
        def change(q):
            q["options"][1]["trap"] = "sample-trap-no-such-trap"
            q["section"] = "2-deep.md#no-such-section"
            q["facts"].append("widget-no-such-fact")
        self.edit_q("sample-q004", change)
        rc, result, err = self.lint("q")
        self.assertEqual(rc, 1, err or result)
        self.assertLessEqual({"Q109", "Q110", "Q111"}, set(codes(result["errors"])))

    def test_must_fail_volatile_and_number_card(self):
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), lambda s: s["questions"].update(volatile_window_months=24))
        self.assert_lint_fails("q", "Q112")
        self.edit_item(CFILE, "sample-c001", lambda c: c.update(front="In Amazon Widget Store, one crate holds up to {{c1::50 widgets}}.", facts=["widget-crate-capacity"]))
        self.assert_lint_fails("cards", "C104")


class Gates(Base):
    def test_gates_pass_on_the_fixture(self):
        with sandbox.paths(self.book):
            for fn, name in ((qbank.gate_questions, "questions"), (qbank.gate_questions_verified, "questions-verified"),
                             (qbank.gate_cards, "cards"), (qbank.gate_speak, "speak")):
                gate = fn("99")
                self.assertEqual((gate["gate"], gate["chapter"], gate["ok"], gate["exit"]), (name, "99", True, 0), gate["errors"])
                self.assertEqual(schemas.validate(gate, "gate"), [])
                self.assertIn(f"data/99-sample/{'questions' if 'questions' in name else name}.json", [i["path"] for i in gate["inputs"]])
            self.assertEqual(len(qbank.items("99", "questions")), 4)
            self.assertEqual(len(qbank.items("sample", "cards")), 3)

    def test_must_fail_ready_question_without_passed_verification(self):
        self.edit_q("sample-q004", lambda q: q["verification"].update(status="candidate"))
        with sandbox.paths(self.book):
            self.assertTrue(qbank.gate_questions("99")["ok"])
            gate = qbank.gate_questions_verified("99")
        self.assertFalse(gate["ok"])
        self.assertEqual(gate["exit"], 1)
        self.assertIn("Q206", codes(gate["errors"]))

    def test_must_fail_gate_cards_and_speak(self):
        self.edit_item(CFILE, "sample-c002", lambda c: c.update(back="No; copy it; then delete it"))
        self.edit_item(SFILE, "sample-s01", lambda s: s.update(skeleton=s["skeleton"][:3] + ["this cue is far longer than six words allow"]))
        with sandbox.paths(self.book):
            cards, speak = qbank.gate_cards("99"), qbank.gate_speak("99")
        self.assertIn("C105", codes(cards["errors"]))
        self.assertIn("P104", codes(speak["errors"]))
        self.assertEqual((cards["exit"], speak["exit"]), (1, 1))


# ---------------------------------------------------------------- blind packs and adjudication

class Verification(Base):
    def setUp(self):
        super().setUp()

        def reset(doc):
            for q in doc["items"]:
                q["status"] = "candidate"
                q["verification"] = {"status": "candidate", "round": 0, "solvers": []}
        sandbox.edit_json(self.path(*QFILE), reset)

    def pack(self, lens, rnd=0, name=None):
        out = self.path("_build", "packs", name or f"{lens}-r{rnd}.json")
        rc, text, err = sandbox.run(self.book, "q", "pack", "--chapter", "99", "--lens", lens, "--round", str(rnd), "--out", str(out))
        self.assertEqual(rc, 0, err)
        return out

    def answers(self, lens, rnd=0, wrong=None, flag=None, bad_quote=None, only=None, solver=None, repack=True):
        if repack:      # `q adjudicate` takes answers only for the text of the newest pack of the lens and round
            self.pack(lens, rnd)
        rows = []
        for q in common.read_json(self.path(*QFILE))["items"]:
            if only and q["id"] not in only:
                continue
            order = qbank.permutation(SEED, q["id"], lens, rnd, [o["id"] for o in q["options"]])
            labels = {oid: qbank.LABELS[n] for n, oid in enumerate(order)}
            key = sorted(labels[o["id"]] for o in q["options"] if o["correct"])
            if q["id"] == wrong:
                key = sorted(labels[o["id"]] for o in q["options"] if not o["correct"])[:len(key)]
            flag_q, _, flag_text = (flag or ":").partition(":")
            row = {"id": q["id"], "answer": key, "flag": flag_text if q["id"] == flag_q else None, "stem_only": None, "citations": None, "case": None}
            if lens == "closed":
                row["stem_only"] = "my solution before the options"
            if lens == "ambiguity":
                row["case"] = {"label": "A", "text": "the strongest case for a wrong option"}
            if lens == "open":
                quote = "A crate can hold up to 50 widgets."
                if q["id"] == bad_quote:
                    quote = "A crate can hold up to 75 widgets."
                row["citations"] = {label: ["widget-shelf-scope"] for label in labels.values()}
                row["citations"]["A"] = [{"source_id": SOURCE, "quote": quote}]
            rows.append(row)
        return self.write(f"answers-{lens}-r{rnd}.json", {"pack": f"sample-r{rnd}-{lens}", "lens": lens,
                                                          "solver": solver or f"solver-{lens}", "answers": rows})

    def adjudicate(self, rnd=0, **kw):
        per_lens = {lens: {} for lens in qbank.LENSES}
        for key, (lens, value) in kw.items():
            per_lens[lens][key] = value
        only = kw.get("only_ids")
        files = [self.answers(lens, rnd, only=only[1] if only else None, **{k: v for k, v in per_lens[lens].items() if k != "only_ids"}) for lens in qbank.LENSES]
        return sandbox.run_json(self.book, "q", "adjudicate", "--chapter", "99", "--answers", *files)

    def test_pack_is_blind(self):
        out = self.pack("closed")
        pack = common.read_json(out)
        self.assertEqual((pack["pack"], pack["chapter"], pack["lens"], pack["round"]), ("sample-r0-closed", "99", "closed", 0))
        self.assertEqual(len(pack["items"]), 4)
        for item in pack["items"]:
            self.assertEqual(set(item), {"id", "type", "select", "stem", "options"})
            for n, option in enumerate(item["options"]):
                self.assertEqual(set(option), {"label", "text"})
                self.assertEqual(option["label"], "ABCDEF"[n])
        text = out.read_text(encoding="utf-8")
        for word in ('"correct"', '"why"', '"explanation"', '"trap"', '"facts"', "A crate is the container"):
            self.assertNotIn(word, text)
        self.assertEqual(qbank.pack_findings(pack), [])

    def test_must_fail_pack_that_still_holds_the_key(self):
        pack = common.read_json(self.pack("closed"))
        pack["items"][0]["options"][0]["correct"] = True
        self.assertEqual(codes(qbank.pack_findings(pack)), ["Q401"])
        pack = common.read_json(self.pack("open"))
        pack["items"][1]["explanation"] = "the key is the first option"
        self.assertEqual(codes(qbank.pack_findings(pack)), ["Q401"])

    def test_pack_order_differs_per_lens_and_repeats_per_lens(self):
        orders = {}
        for lens in qbank.LENSES:
            pack = common.read_json(self.pack(lens))
            orders[lens] = [[o["text"] for o in item["options"]] for item in pack["items"]]
        self.assertTrue(orders["closed"] != orders["open"] or orders["open"] != orders["ambiguity"])
        again = common.read_json(self.pack("closed", name="closed-again.json"))
        self.assertEqual([[o["text"] for o in item["options"]] for item in again["items"]], orders["closed"])

    def test_must_fail_pack_without_candidates(self):
        rc, out, err = sandbox.run(self.book, "q", "pack", "--chapter", "99", "--lens", "closed", "--round", "1", "--out", str(self.path("p.json")))
        self.assertEqual(rc, 3)

    def test_all_agree_passes_then_select(self):
        rc, result, err = self.adjudicate()
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result, {"pass": ["sample-q001", "sample-q002", "sample-q003", "sample-q004"], "needs_edit": [], "rejected": [], "below_min": False})
        q = self.question("sample-q003")
        self.assertEqual((q["status"], q["verification"]["status"]), ("verified", "pass"))
        solvers = {s["lens"]: s for s in q["verification"]["solvers"]}
        self.assertEqual(solvers["open"]["answer"], ["a", "b"])
        self.assertTrue(solvers["open"]["citations_ok"])
        self.assertIn("widget-shelf-scope", solvers["open"]["citations"])
        self.assertEqual(schemas.validate(q, "question", "question"), [])
        rc, result, err = sandbox.run_json(self.book, "q", "adjudicate", "--chapter", "99", "--select")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(len(result["ready"]), 4)
        rc, result, err = self.lint("q", "--ship")
        self.assertEqual(rc, 0, err or result)

    def test_must_fail_one_dissenting_solver(self):
        rc, result, err = self.adjudicate(wrong=("closed", "sample-q004"))
        self.assertEqual(rc, 0, err or result)
        self.assertNotIn("sample-q004", result["pass"])
        self.assertEqual(result["needs_edit"], [{"id": "sample-q004", "reasons": ["closed disagrees"]}])
        q = self.question("sample-q004")
        self.assertEqual((q["status"], q["verification"]["status"], q["verification"]["round"]), ("candidate", "candidate", 1))
        self.assertFalse(next(s for s in q["verification"]["solvers"] if s["lens"] == "closed")["agree"])

    def test_must_fail_ambiguity_flag(self):
        rc, result, err = self.adjudicate(flag=("ambiguity", "sample-q002:the stem misses a constraint"))
        self.assertEqual(result["needs_edit"], [{"id": "sample-q002", "reasons": ["ambiguity flag"]}])
        self.assertNotIn("sample-q002", result["pass"])

    def test_must_fail_citation_quote_not_in_snapshot(self):
        rc, result, err = self.adjudicate(bad_quote=("open", "sample-q001"))
        self.assertEqual(result["needs_edit"], [{"id": "sample-q001", "reasons": ["open citations"]}])

    def test_must_fail_second_failure_rejects(self):
        rc, result, err = self.adjudicate(wrong=("open", "sample-q004"))
        self.assertEqual([e["id"] for e in result["needs_edit"]], ["sample-q004"])
        self.pack("closed", rnd=1)
        rc, result, err = self.adjudicate(rnd=1, wrong=("ambiguity", "sample-q004"), only_ids=("closed", {"sample-q004"}))
        self.assertEqual(rc, 1, err or result)
        self.assertEqual((result["rejected"], result["below_min"]), (["sample-q004"], True))
        q = self.question("sample-q004")
        self.assertEqual((q["status"], q["verification"]["status"]), ("rejected", "rejected"))
        rows = common.read_jsonl(self.path("_build", "qbank", "rejected.jsonl"))
        self.assertEqual([r["id"] for r in rows], ["sample-q004"])
        rc, result, err = sandbox.run_json(self.book, "q", "adjudicate", "--chapter", "99", "--select")
        self.assertEqual(rc, 1)
        self.assertFalse(result["ok"])
        self.assertEqual(self.question("sample-q001")["status"], "verified")

    def test_must_fail_two_files_of_one_lens(self):
        a = self.answers("closed")
        rc, out, err = sandbox.run(self.book, "q", "adjudicate", "--chapter", "99", "--answers", a, a, self.answers("open"))
        self.assertEqual(rc, 3)

    def test_edit_after_a_failed_round(self):
        self.adjudicate(wrong=("closed", "sample-q004"))
        rc, result, err = self.add_q(lambda q: q.update(id="sample-q004"), "--replace")
        self.assertEqual(rc, 0, err or result)
        q = self.question("sample-q004")
        self.assertEqual((q["rev"], q["verification"]["round"], q["verification"]["solvers"]), (2, 1, []))
        rc, result, err = self.adjudicate(rnd=1, only_ids=("closed", {"sample-q004"}))
        self.assertEqual(result["pass"], ["sample-q004"])
        self.assertEqual(self.question("sample-q004")["verification"]["status"], "edited-pass")


# ---------------------------------------------------------------- cards

class Cards(Base):
    def test_fixture_passes(self):
        rc, result, err = self.lint("cards", "--ship")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = sandbox.run_json(self.book, "cards", "lint", "--all")
        self.assertEqual(rc, 0, err or result)

    def test_must_fail_back_over_the_word_limit(self):
        back = "No. You copy the shelf to the other Region and keep the first shelf."
        self.edit_item(CFILE, "sample-c002", lambda c: c.update(back=back))
        self.assert_lint_fails("cards", "C102")

    def test_must_fail_list_answer(self):
        self.edit_item(CFILE, "sample-c002", lambda c: c.update(back="No, copy it, keep both"))
        self.assert_lint_fails("cards", "C105")

    def test_must_fail_number_card_outside_the_a_list(self):
        def change(c):
            c.update(front="In Amazon Widget Store, one crate holds up to {{c1::50 widgets}}.", facts=["widget-crate-capacity"], trap=None)
        self.edit_item(CFILE, "sample-c001", change)
        self.assert_lint_fails("cards", "C104")

    def test_must_fail_number_not_in_a_display(self):
        self.edit_item(CFILE, "sample-c003", lambda c: c.update(back="A crate. It holds 60 widgets."))
        self.assert_lint_fails("cards", "C109")

    def test_must_fail_missing_number_card_with_ship(self):
        self.edit_item(CFILE, "sample-c001", lambda c: c.update(status="retired"))
        rc, result, err = self.lint("cards")
        self.assertEqual(rc, 2, err or result)
        self.assert_lint_fails("cards", "C204", "--ship")

    def test_must_fail_add_refuses_a_generated_type(self):
        card = {"type": "partner", "deck": "core", "front": "___ a shelf in a Region", "back": "create", "extra": None, "facts": [], "term": "shelf",
                "word": None, "speak": None, "trap": None, "section": None, "pair": None, "tags": []}
        rc, result, err = sandbox.run_json(self.book, "cards", "add", "--chapter", "99", "--file", self.write("card.json", card))
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["rejected"][0]["errors"]), ["C110"])

    def test_add_and_replace(self):
        card = copy.deepcopy(common.read_json(self.path(*CFILE))["items"][2])
        del card["id"]
        card.update(front="In Amazon Widget Store, how many widgets fit in the resource that ships between Regions?", back="50 widgets in one crate.")
        rc, result, err = sandbox.run_json(self.book, "cards", "add", "--chapter", "99", "--file", self.write("card.json", card))
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(result["added"], ["sample-c004"])
        stored = common.read_json(self.path(*CFILE))["items"][3]
        self.assertEqual((stored["status"], stored["rev"]), ("candidate", 1))
        rc, result, err = sandbox.run_json(self.book, "cards", "set-status", "--chapter", "99", "--status", "ready", "sample-c004")
        self.assertEqual(rc, 0, err or result)
        card["id"] = "sample-c004"
        rc, result, err = sandbox.run_json(self.book, "cards", "add", "--chapter", "99", "--replace", "--file", self.write("card.json", card))
        self.assertEqual(result["replaced"], ["sample-c004"])
        stored = common.read_json(self.path(*CFILE))["items"][3]
        self.assertEqual((stored["status"], stored["rev"]), ("candidate", 2))

    def test_build_generated_cards(self):
        rc, result, err = sandbox.run_json(self.book, "cards", "build")
        self.assertEqual(rc, 0, err or result)
        doc = common.read_json(self.path("data", "cards-terms.json"))
        self.assertEqual(schemas.validate(doc, "card"), [])
        self.assertEqual(doc["chapter"], "glossary")
        types = [c["type"] for c in doc["items"]]
        self.assertEqual((types.count("term"), types.count("meaning")), (5, 5))
        self.assertTrue(all(c["generated"] and c["status"] == "ready" and c["section"] is None for c in doc["items"]))
        partner = next(c for c in doc["items"] if c["type"] == "partner" and c["term"] == "idempotent")
        self.assertEqual((partner["front"], partner["back"]), ("an idempotent ___", "request"))
        first = self.path("data", "cards-terms.json").read_bytes()
        rc, result, err = sandbox.run_json(self.book, "cards", "build", "--check")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = sandbox.run_json(self.book, "cards", "build")
        self.assertEqual(result["written"], [])
        self.assertEqual(self.path("data", "cards-terms.json").read_bytes(), first)
        rc, result, err = sandbox.run_json(self.book, "cards", "lint", "--all")
        self.assertEqual(rc, 0, err or result)

    def test_must_fail_build_check_when_terms_change(self):
        sandbox.run(self.book, "cards", "build")
        sandbox.edit_json(self.path("data", "terms.json"), lambda d: d["terms"][0].update(meaning="The place that stores widgets in one Region."))
        rc, result, err = sandbox.run_json(self.book, "cards", "build", "--check")
        self.assertEqual(rc, 1)
        self.assertEqual(len(result["stale"]), 1)


# ---------------------------------------------------------------- speak

class Speak(Base):
    def edit_line(self, old, new):
        def change(s):
            s["sixty_second"] = [line.replace(old, new) for line in s["sixty_second"]]
            assert any(new in line for line in s["sixty_second"])
        self.edit_item(SFILE, "sample-s01", change)

    def test_fixture_passes(self):
        rc, result, err = self.lint("speak", "--ship")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = sandbox.run_json(self.book, "speak", "lint", "--all")
        self.assertEqual(rc, 0, err or result)

    def test_must_fail_digit_in_script(self):
        self.edit_line("five hundred widgets", "500 widgets")
        self.assert_lint_fails("speak", "P106")

    def test_must_fail_missing_starter(self):
        self.edit_line("The thing to watch is this:", "Remember this:")
        self.assert_lint_fails("speak", "P103")

    def test_must_fail_spoken_number_without_a_fact(self):
        self.edit_line("five hundred widgets", "six hundred widgets")
        self.assert_lint_fails("speak", "P109")

    def test_must_fail_sixty_second_far_over_the_word_limit(self):
        extra = ["A shelf is the place where your team keeps its widgets. Your team reaches the shelf from any office.",
                 "A crate is the container that carries widgets between Regions. Your team packs a crate and ships it.",
                 "The owner of a shelf decides who reads the shelf. Other people in the account wait for that decision.",
                 "A copy of a shelf gives a second Region the same widgets. The first shelf stays where it is."]

        def change(s):
            s["sixty_second"] = s["sixty_second"][:-1] + extra + s["sixty_second"][-1:]
        self.edit_item(SFILE, "sample-s01", change)
        rc, result, err = self.lint("speak")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["errors"]), ["P102"])
        self.assertIn("sixty_second has", result["errors"][0]["msg"])

    def test_must_fail_must_point_without_fact(self):
        self.edit_item(SFILE, "sample-s01", lambda s: s["key_points"][0].update(facts=[]))
        self.assert_lint_fails("speak", "P105")

    def test_must_fail_avoid_word_in_script(self):
        self.edit_line("you copy the shelf", "you migrate the shelf")
        self.assert_lint_fails("speak", "P107")

    def test_must_fail_ship_count(self):
        self.edit_item(SFILE, "sample-s01", lambda s: s.update(status="candidate"))
        self.assert_lint_fails("speak", "P201", "--ship")

    def test_must_fail_pack_total(self):
        rc, result, err = sandbox.run_json(self.book, "speak", "set-pack", "--chapter", "99", "sample-s01")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = sandbox.run_json(self.book, "speak", "lint", "--all")
        self.assertEqual(rc, 1)
        self.assertIn("P202", codes(result["errors"]))
        sandbox.run(self.book, "speak", "set-pack", "--chapter", "99", "sample-s01", "--off")
        rc, result, err = sandbox.run_json(self.book, "speak", "lint", "--all")
        self.assertEqual(rc, 0, err or result)


# ---------------------------------------------------------------- mocks and drills (synthetic pool)

SPLIT = [1, 3, 1, 1]
POOL = [("1.1", 1, "single"), ("1.1", 1, "single"), ("2.1", 2, "single"), ("2.1", 2, "multi"), ("2.2", 2, "single"),
        ("2.2", 2, "multi"), ("3.1", 3, "single"), ("3.1", 3, "single"), ("4.1", 4, "single"), ("4.1", 4, "single")]


class Mocks(Base):
    def setUp(self):
        super().setUp()
        base = {q["id"]: q for q in common.read_json(self.path(*QFILE))["items"]}

        def spec(s):
            s["templates"]["mock"] = {"files": [], "counts": {"questions": {"shipped": 6, "core": 6, "extended": 0, "write": 10, "twin_pairs_min": 0,
                                                                              "multi": {"min": 1, "max": 2}, "worked": 0, "worked_wrong_path": 0}},
                                      "mock": {"domain_split": SPLIT, "minutes": 12, "max_questions_per_service": 10}}
            s["questions"]["no_qualifier_share_max"] = 1.0      # the synthetic pool has no qualifiers
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), spec)

        def book(b):
            for cid, slug in (("50", "mock-exam-1"), ("51", "mock-exam-2")):
                b["chapters"].append({"id": cid, "slug": slug, "title": slug, "part": "storage", "tier": "mock", "wave": "W0", "services": [], "tasks": [], "bullets": [],
                                      "sources": {"guides": [], "pages": [], "faq": [], "history": [], "quotas": [], "pricing": [], "whatsnew_tags": [], "case_tags": []}})
        sandbox.edit_json(self.path("data", "book.json"), book)
        for m, (cid, slug) in enumerate((("50", "mock-exam-1"), ("51", "mock-exam-2"))):
            items = []
            for n, (task, domain, typ) in enumerate(POOL, 1):
                q = copy.deepcopy(base["sample-q003" if typ == "multi" else "sample-q004"])
                q.update(id=f"{slug}-q{n:03d}", chapter=slug, pool="mock", layer="core", task=task, domain=domain, bullets=[],
                         section="99-sample/1-fast.md#choose-it-or-not", status="verified", twin_of=None, concept=f"concept-{m}-{n}")
                items.append(make_distinct(q, m * 50 + n))
            common.write_json(self.path("data", f"{cid}-{slug}", "questions.json"), {"v": 1, "chapter": slug, "items": items})

    def qfile(self, cid="50"):
        return self.path("data", f"{cid}-mock-exam-{int(cid) - 49}", "questions.json")

    def mfile(self, cid="50"):
        return self.path("data", f"{cid}-mock-exam-{int(cid) - 49}", "mock.json")

    def assemble(self, *extra):
        return sandbox.run_json(self.book, "mocks", "assemble", *extra)

    def check(self, *extra):
        return sandbox.run_json(self.book, "mocks", "check", *extra)

    def assert_check_fails(self, code, mock="50"):
        rc, result, err = self.check("--mock", mock)
        self.assertEqual(rc, 1, err or result)
        self.assertIn(code, codes(result["mocks"][0]["errors"]))

    def test_synthetic_pool_passes_the_item_rules(self):
        rc, result, err = sandbox.run_json(self.book, "q", "lint", "50")
        self.assertEqual(codes(result["errors"]), [], result["errors"])

    def test_assemble_and_check(self):
        rc, result, err = self.assemble("--mock", "50")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual((result["mock"], result["ok"], result["seed"], result["spares"]), ("50", True, SEED + 50, 4))
        manifest = common.read_json(self.mfile())
        self.assertEqual(schemas.validate(manifest, "mock"), [])
        self.assertEqual(len(manifest["questions"]), 6)
        self.assertEqual(manifest["counts"]["domains"], {"1": 1, "2": 3, "3": 1, "4": 1})
        self.assertEqual(sorted(manifest["counts"]["tasks"]), ["1.1", "2.1", "2.2", "3.1", "4.1"])
        self.assertTrue(1 <= manifest["counts"]["multi"] <= 2)
        status = {q["id"]: q["status"] for q in common.read_json(self.qfile())["items"]}
        self.assertEqual({i for i, s in status.items() if s == "ready"}, set(manifest["questions"]))
        rc, result, err = self.assemble("--mock", "51")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = self.check()
        self.assertEqual(rc, 0, err or result)
        self.assertEqual([m["ok"] for m in result["mocks"]], [True, True])
        rc, result, err = sandbox.run_json(self.book, "q", "lint", "50", "--ship")
        self.assertEqual(codes(result["errors"]), [], result["errors"])

    def test_same_seed_gives_the_same_manifest(self):
        self.assemble("--mock", "50", "--seed", "7")
        first = common.read_json(self.mfile())
        self.assemble("--mock", "50", "--seed", "7")
        self.assertEqual(common.read_json(self.mfile()), first)
        self.assemble("--mock", "50", "--seed", "8")
        self.assertEqual(common.read_json(self.mfile())["seed"], 8)

    def test_must_fail_assemble_with_a_task_statement_missing(self):
        def change(doc):
            doc["items"] = [q for q in doc["items"] if q["task"] != "3.1"]
        sandbox.edit_json(self.qfile(), change)
        rc, result, err = self.assemble("--mock", "50")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual((result["ok"], result["missing_tasks"]), (False, ["3.1"]))
        self.assertEqual(result["short"], [{"domain": 3, "need": 1, "have": 0}])
        self.assertFalse(self.mfile().exists())

    def test_must_fail_assemble_skips_unverified_candidates(self):
        def change(doc):
            for q in doc["items"]:
                if q["domain"] == 2 and q["type"] == "single":
                    q["verification"]["status"] = "candidate"
        sandbox.edit_json(self.qfile(), change)
        rc, result, err = self.assemble("--mock", "50")
        self.assertEqual(rc, 1, err or result)
        self.assertFalse(self.mfile().exists())

    def test_must_fail_wrong_domain_split(self):
        self.assemble("--mock", "50")

        def change(m):
            by_id = {q["id"]: q for q in common.read_json(self.qfile())["items"]}
            out = next(i for i in m["questions"] if by_id[i]["domain"] == 2)
            spare = next(i for i in m["spares"] if by_id[i]["domain"] == 1)
            m["questions"][m["questions"].index(out)] = spare
        sandbox.edit_json(self.mfile(), change)
        self.assert_check_fails("K02")

    def test_must_fail_reused_chapter_question(self):
        self.assemble("--mock", "50")
        sandbox.edit_json(self.mfile(), lambda m: m["questions"].__setitem__(0, "sample-q001"))
        self.assert_check_fails("K04")

    def test_must_fail_question_in_both_mocks(self):
        self.assemble()
        first = common.read_json(self.mfile("50"))["questions"][0]
        sandbox.edit_json(self.mfile("51"), lambda m: m["questions"].__setitem__(0, first))
        self.assert_check_fails("K04", "51")

    def test_must_fail_mock_stem_copied_from_a_chapter(self):
        self.assemble("--mock", "50")
        chosen = common.read_json(self.mfile())["questions"][0]
        stem = self.question("sample-q004")["stem"]

        def change(doc):
            q = next(q for q in doc["items"] if q["id"] == chosen)
            q["stem"] = stem + (" (Select TWO.)" if q["type"] == "multi" else "")
        sandbox.edit_json(self.qfile(), change)
        self.assert_check_fails("K04")

    def test_must_fail_volatile_question(self):
        self.assemble("--mock", "50")
        chosen = common.read_json(self.mfile())["questions"][0]

        def change(doc):
            next(q for q in doc["items"] if q["id"] == chosen)["volatile"] = True
        sandbox.edit_json(self.qfile(), change)
        self.assert_check_fails("K05")

    def test_must_fail_missing_manifest(self):
        self.assert_check_fails("K01")

    def test_must_fail_service_limit(self):
        self.assemble("--mock", "50")
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), lambda s: s["templates"]["mock"]["mock"].update(max_questions_per_service=4))
        self.assert_check_fails("K06")


class Drills(Base):
    def test_build_and_check(self):
        rc, result, err = sandbox.run_json(self.book, "drills", "build", "--size", "2")
        self.assertEqual(rc, 2, err or result)                      # domains 1, 3 and 4 have no question
        doc = common.read_json(self.path("data", "drills.json"))
        self.assertEqual(schemas.validate(doc, "drills"), [])
        self.assertEqual(doc["seed"], SEED)
        self.assertEqual(sorted(doc["drills"][1]["questions"]), ["sample-q003", "sample-q004"])
        again = sandbox.run_json(self.book, "drills", "build", "--size", "2")
        self.assertEqual(common.read_json(self.path("data", "drills.json")), doc)
        rc, result, err = sandbox.run_json(self.book, "drills", "check")
        self.assertEqual(rc, 0, err or result)

    def test_must_fail_drill_question_not_ready(self):
        sandbox.run(self.book, "drills", "build", "--size", "2")
        self.edit_q("sample-q003", lambda q: q.update(status="verified"))
        rc, result, err = sandbox.run_json(self.book, "drills", "check")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["errors"]), ["K22"])

    def test_must_fail_drill_of_the_wrong_domain(self):
        sandbox.run(self.book, "drills", "build", "--size", "2")

        def change(doc):
            doc["drills"][0]["questions"], doc["drills"][1]["questions"] = doc["drills"][1]["questions"], []
        sandbox.edit_json(self.path("data", "drills.json"), change)
        rc, result, err = sandbox.run_json(self.book, "drills", "check")
        self.assertEqual(rc, 1, err or result)
        self.assertIn("K22", codes(result["errors"]))


if __name__ == "__main__":
    unittest.main()
