"""Regression tests for the holes of _build/reports/gate-break-practice.md that live in saalib/qbank.py
(questions, adjudication, mocks, cards, spoken items). The attempt number of the gate breaker is in each test name.
"""
import copy
import unittest

import sandbox
import test_qbank as tq
from saalib import common, qbank

codes = tq.codes


def drop_inherited_tests(cls, parent):
    """Keep the helpers of a test class of test_qbank without running its tests a second time."""
    for name in dir(parent):
        if name.startswith("test_") and name not in cls.__dict__:
            setattr(cls, name, None)


class QuestionShape(tq.Base):
    def test_must_fail_03_two_options_with_the_same_text(self):
        self.assert_add_rejects("Q102", lambda q: q["options"][2].update(text=q["options"][0]["text"]))

    def test_must_fail_04_long_key_between_short_options(self):
        def change(q):
            for option, text in zip(q["options"], ("A crate that the company packs today and then ships by air to the partner in ap-south-1.",
                                                   "The existing shelf, moved.", "A second shelf.", "A higher shelf quota.")):
                option["text"] = text
        self.assert_add_rejects("Q104", change)

    def test_must_fail_05_key_is_longer_than_every_wrong_option(self):
        def change(q):
            for option, text in zip(q["options"], ("A crate that the company packs today and ships to the partner in ap-south-1 soon.",
                                                   "The existing shelf, moved from us-east-1 to ap-south-1 by the company.",
                                                   "A second shelf that the company creates in us-east-1 next week.",
                                                   "A higher quota for the shelves of the company in us-east-1.")):
                option["text"] = text
        self.assert_add_rejects("Q104", change)

    def test_must_fail_06_key_made_of_stem_words_under_a_long_stem(self):
        sandbox.edit_json(self.path("_build", "style", "SPEC.json"), lambda s: s["questions"].update(stem_key_overlap_margin_max=0.25))

        def change(q):
            for option, text in zip(q["options"], ("A crate to send the partner the widgets next week from the shelf.",
                                                   "Request extra help through an enterprise support plan today, then wait.",
                                                   "Buy larger hardware and install it inside a private data center.",
                                                   "Open a ticket and let another team decide what happens later.")):
                option["text"] = text
        self.assert_add_rejects("Q113", change)

    def test_must_fail_07_option_named_by_position_or_bare_letter(self):
        self.assert_add_rejects("Q105", lambda q: q.update(explanation=q["explanation"] + " The second option is wrong."))
        self.assert_add_rejects("Q105", lambda q: q.update(explanation=q["explanation"] + " Also (C) is wrong."))
        self.assert_add_rejects("Q105", lambda q: q.update(explanation=q["explanation"] + " B is the usual trap."))

    def test_must_fail_10_negative_stem_in_lowercase(self):
        self.assert_add_rejects("Q105", lambda q: q.update(stem=q["stem"].replace(
            "Which Amazon Widget Store resource should the company use to send the 40 widgets?",
            "Which Amazon Widget Store resource is not a way to send the 40 widgets?")))

    def test_must_fail_11_none_of_these_options(self):
        self.assert_add_rejects("Q105", lambda q: q["options"][3].update(text="None of these options."))


class Duplicates(tq.Base):
    def copy_of(self, qid, **over):
        q = copy.deepcopy(self.question(qid))
        del q["id"]
        q.update(over)
        return q

    def add(self, q):
        return sandbox.run_json(self.book, "q", "add", "--chapter", "99", "--file", self.write("in.json", q))

    def test_must_fail_08_exact_copy_under_a_new_id(self):
        rc, result, err = self.add(self.copy_of("sample-q004", concept="crate-again"))
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["rejected"][0]["errors"]), ["Q302"])
        self.assertEqual(len(common.read_json(self.path(*tq.QFILE))["items"]), 4)

    def test_must_fail_08_copy_in_the_file_fails_the_chapter_lint_and_the_gate(self):
        def change(doc):
            doc["items"].append(dict(copy.deepcopy(doc["items"][3]), id="sample-q005", concept="crate-again"))
        sandbox.edit_json(self.path(*tq.QFILE), change)
        self.assert_lint_fails("q", "Q302")
        rc, result, err = sandbox.run_json(self.book, "gate", "99", "--gate", "questions")
        self.assertEqual(rc, 1, err or result)

    def test_must_fail_09_reordered_clauses_are_a_duplicate(self):
        first = self.question("sample-q001")
        second = dict(copy.deepcopy(first), stem=(
            "On one shelf in the us-east-1 Region of Amazon Widget Store, a company keeps 400 widgets. Next month the company "
            "expects to add 300 more widgets. All widgets must stay in us-east-1, a compliance rule states. With the LEAST "
            "operational overhead, which solution will meet these requirements?"))
        value, duplicate = qbank.similarity(qbank._print(first), qbank._print(second))
        self.assertTrue(duplicate, value)
        other = self.question("sample-q004")
        self.assertFalse(qbank.similarity(qbank._print(first), qbank._print(other))[1])

    def test_must_fail_27_copy_with_one_more_sentence_is_a_duplicate(self):
        first = self.question("sample-q004")
        second = dict(copy.deepcopy(first), stem="A company runs the " + tq.unique_words(7, 12) + " program. " + first["stem"])
        self.assertTrue(qbank.similarity(qbank._print(first), qbank._print(second))[1])

    def test_must_fail_24_rejected_question_under_a_new_id(self):
        self.edit_q("sample-q004", lambda q: (q.update(status="rejected"), q["verification"].update(status="rejected")))
        rc, result, err = self.add(self.copy_of("sample-q004", status="candidate"))
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["rejected"][0]["errors"]), ["Q302"])
        self.assertIn("rejected question sample-q004", result["rejected"][0]["errors"][0]["msg"])

    def test_must_fail_25_set_status_verified_without_a_verification(self):
        self.edit_q("sample-q004", lambda q: q.update(status="candidate", verification={"status": "candidate", "round": 0, "solvers": []}))
        rc, result, err = sandbox.run_json(self.book, "q", "set-status", "--chapter", "99", "--status", "verified", "sample-q004")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(self.question("sample-q004")["status"], "candidate")


class Adjudication(tq.Verification):
    def refused(self, files):
        before = self.path(*tq.QFILE).read_bytes()
        rc, out, err = sandbox.run(self.book, "q", "adjudicate", "--chapter", "99", "--answers", *files)
        self.assertEqual(rc, 3, out + err)
        self.assertEqual(self.path(*tq.QFILE).read_bytes(), before)
        return err

    def files(self, **per_lens):
        return [self.answers(lens, **per_lens.get(lens, {})) for lens in qbank.LENSES]

    def edit_answers(self, path, change):
        sandbox.edit_json(path, change)
        return path

    def test_must_fail_17_answer_file_without_a_solver(self):
        files = self.files()
        self.edit_answers(files[1], lambda doc: doc.update(solver=None))
        self.assertIn("names no solver", self.refused(files))

    def test_must_fail_18_one_solver_signs_all_three_lenses(self):
        files = self.files(closed={"solver": "breaker"}, open={"solver": "Breaker"}, ambiguity={"solver": "breaker"})
        self.assertIn("three different solvers", self.refused(files))

    def test_must_fail_18_the_author_is_a_solver(self):
        rc, result, err = self.add_q(None, "--by", "writer-a")
        self.assertEqual(rc, 0, err or result)
        self.assertEqual(self.question("sample-q005")["authors"], ["writer-a"])
        files = self.files(open={"solver": "Writer-A"})
        self.assertIn("is an author of sample-q005", self.refused(files))

    def test_must_fail_19_closed_lens_without_stem_only_and_ambiguity_lens_without_a_case(self):
        files = self.files()

        def blank(key):
            def change(doc):
                for row in doc["answers"]:
                    row[key] = None
            return change
        self.edit_answers(files[0], blank("stem_only"))
        self.assertIn("no stem_only", self.refused(files))
        files = self.files()
        self.edit_answers(files[2], blank("case"))
        self.assertIn("has no case", self.refused(files))

    def test_must_fail_20_one_citation_for_every_label_or_a_one_word_quote(self):
        files = self.files()

        def same(doc):
            for row in doc["answers"]:
                row["citations"] = {label: ["widget-shelf-max-widgets"] for label in row["citations"]}
        self.edit_answers(files[1], same)
        rc, result, err = sandbox.run_json(self.book, "q", "adjudicate", "--chapter", "99", "--answers", *files)
        self.assertEqual(result["pass"], [], err)
        self.assertEqual({e["reasons"][0] for e in result["needs_edit"]}, {"open citations"})

    def test_must_fail_20_one_word_quote(self):
        files = self.files()

        def short(doc):
            for row in doc["answers"]:
                row["citations"]["A"] = [{"source_id": tq.SOURCE, "quote": "the"}]
        self.edit_answers(files[1], short)
        rc, result, err = sandbox.run_json(self.book, "q", "adjudicate", "--chapter", "99", "--answers", *files)
        self.assertEqual(result["pass"], [], err)

    def test_must_fail_21_two_rows_for_one_question(self):
        files = self.files()
        self.edit_answers(files[2], lambda doc: doc["answers"].append(dict(doc["answers"][-1], flag="a second answer is defensible")))
        self.assertIn("two rows for sample-q004", self.refused(files))

    def test_must_fail_22_old_answers_for_a_replaced_question(self):
        files = self.files()

        def change(q):
            q.clear()
            q.update(copy.deepcopy(self.question("sample-q004")))
            q["options"][2]["text"] = "A second shelf that the company creates in us-west-2."
        rc, result, err = self.add_q(change, "--replace")
        self.assertEqual(rc, 0, err or result)
        self.assertIn("sample-q004 changed after the pack went out", self.refused(files))

    def test_must_fail_22_answers_without_a_pack(self):
        files = [self.answers(lens, repack=False) for lens in qbank.LENSES]
        self.assertIn("was in no pack", self.refused(files))

    def test_must_fail_23_second_edit_after_a_failed_round(self):
        self.adjudicate(wrong=("closed", "sample-q004"))

        def edit(takeaway):
            def change(q):
                q.clear()
                q.update(copy.deepcopy(self.question("sample-q004")))
                q["takeaway"] = takeaway
            return self.add_q(change, "--replace")
        rc, result, err = edit("A crate is the resource that travels between two Regions.")
        self.assertEqual(rc, 0, err or result)
        rc, result, err = edit("Only a crate travels from one Region to another Region.")
        self.assertEqual(rc, 1, err or result)
        self.assertEqual(codes(result["rejected"][0]["errors"]), ["Q207"])
        self.assertEqual(self.question("sample-q004")["rev"], 2)


drop_inherited_tests(Adjudication, tq.Verification)


class MockHoles(tq.Mocks):
    def chosen(self, typ="single"):
        by_id = {q["id"]: q for q in common.read_json(self.qfile())["items"]}
        return [i for i in common.read_json(self.mfile())["questions"] if by_id[i]["type"] == typ]

    def edit_mock_q(self, qid, change):
        def apply(doc):
            change(next(q for q in doc["items"] if q["id"] == qid))
        sandbox.edit_json(self.qfile(), apply)

    def test_must_fail_27_chapter_question_with_a_padding_sentence(self):
        self.assemble("--mock", "50")
        source = self.question("sample-q004")

        def change(q):
            q["stem"] = "A company runs the " + tq.unique_words(77, 12) + " program. " + source["stem"]
            for mine, theirs in zip(q["options"], source["options"]):
                mine["text"] = theirs["text"]
        self.edit_mock_q(self.chosen()[0], change)
        self.assert_check_fails("K04")

    def test_must_fail_28_two_questions_of_one_mock_with_the_same_stem(self):
        self.assemble("--mock", "50")
        first, second = self.chosen()[:2]
        stem = next(q for q in common.read_json(self.qfile())["items"] if q["id"] == first)["stem"]
        self.edit_mock_q(second, lambda q: q.update(stem=stem))
        self.assert_check_fails("K04")

    def test_must_fail_29_copy_of_a_drill_question(self):
        self.assemble("--mock", "50")
        self.edit_q("sample-q004", lambda q: q.update(pool="drill"))
        stem = self.question("sample-q004")["stem"]
        self.edit_mock_q(self.chosen()[0], lambda q: q.update(stem=stem))
        self.assert_check_fails("K04")

    def test_must_fail_30_manifest_minutes_and_counts_edited_by_hand(self):
        self.assemble("--mock", "50")
        sandbox.edit_json(self.mfile(), lambda m: m.update(minutes=9999))
        self.assert_check_fails("K01")
        self.assemble("--mock", "50")
        sandbox.edit_json(self.mfile(), lambda m: m["counts"].update(multi=0))
        self.assert_check_fails("K01")


drop_inherited_tests(MockHoles, tq.Mocks)


class CardHoles(tq.Base):
    def back(self, text, code, card="sample-c003"):
        self.edit_item(tq.CFILE, card, lambda c: c.update(back=text))
        self.assert_lint_fails("cards", code)

    def test_must_fail_32_list_answer_with_one_comma_and_and(self):
        self.back("A shelf, a crate and a quota.", "C105")

    def test_must_fail_32_list_answer_with_slashes(self):
        self.back("shelf / crate / quota / Region", "C105")

    def test_must_fail_34_back_over_the_limit_joined_with_hyphens(self):
        self.back("No. Copy-the-shelf-to-the-other-Region-then-check-the-copy-then-delete-the-first-shelf-and-tell-the-team.",
                  "C102", card="sample-c002")

    def test_must_fail_35_wrong_number_written_as_a_word(self):
        self.back("A crate. It holds ninety widgets.", "C109")

    def test_must_fail_number_that_sits_inside_the_display_number(self):
        # W0 follow-up 3: `0 widgets` is a substring of the display `50 widgets` but not the same number
        self.back("A crate. It holds 0 widgets.", "C109")

    def test_must_fail_number_in_the_front_that_sits_inside_the_display_number(self):
        self.edit_item(tq.CFILE, "sample-c003", lambda c: c.update(
            front="In Amazon Widget Store, 0 widgets travel to another Region. Which resource carries them?"))
        self.assert_lint_fails("cards", "C109")

    def test_must_fail_37_near_duplicate_front_with_filler_words(self):
        card = copy.deepcopy(common.read_json(self.path(*tq.CFILE))["items"][1])
        del card["id"]
        card["front"] += " Think first, please."
        rc, result, err = sandbox.run_json(self.book, "cards", "add", "--chapter", "99", "--file", self.write("card.json", card))
        self.assertEqual(rc, 1, err or result)
        self.assertIn("C106", codes(result["rejected"][0]["errors"]))


class SpeakHoles(tq.Speak):
    def test_must_fail_39_long_answer_joined_with_hyphens(self):
        joined = "-".join(["the", "team", "keeps", "widgets", "on", "the", "shelf"] * 4)

        def change(s):
            s["sixty_second"] = [line + " " + joined.capitalize() + "." for line in s["sixty_second"][:-1]] + s["sixty_second"][-1:]
        self.edit_item(tq.SFILE, "sample-s01", change)
        self.assert_lint_fails("speak", "P102")

    def test_must_fail_40_long_follow_up_answer_and_key_point(self):
        long = " ".join(["Your team keeps the widgets on the shelf."] * 40)
        self.edit_item(tq.SFILE, "sample-s01", lambda s: s["follow_ups"][0].update(answer=long))
        self.assert_lint_fails("speak", "P102")
        self.edit_item(tq.SFILE, "sample-s01", lambda s: s["key_points"][0].update(point=long))
        self.assert_lint_fails("speak", "P102")

    def test_must_fail_42_number_word_before_two_other_words(self):
        self.edit_line("five hundred widgets", "nine hundred of your widgets")
        self.assert_lint_fails("speak", "P109")

    def test_must_fail_42_nineteen(self):
        self.edit_line("five hundred widgets", "nineteen widgets")
        self.assert_lint_fails("speak", "P109")

    def test_must_fail_key_point_number_that_sits_inside_the_display_number(self):
        # W0 follow-up 3: `0 widgets` is a substring of the display `500 widgets` but not the same number
        def change(s):
            for point in s["key_points"]:
                point["point"] = point["point"].replace("up to 500 widgets", "up to 0 widgets")
            assert any("0 widgets" in k["point"] for k in s["key_points"])
        self.edit_item(tq.SFILE, "sample-s01", change)
        self.assert_lint_fails("speak", "P109")

    def test_must_fail_follow_up_number_that_sits_inside_the_display_number(self):
        def change(s):
            s["follow_ups"][0]["answer"] = "No. You copy the shelf, and the copy holds 00 widgets too."
            s["follow_ups"][0]["facts"] = ["widget-shelf-move", "widget-shelf-max-widgets"]
        self.edit_item(tq.SFILE, "sample-s01", change)
        self.assert_lint_fails("speak", "P109")


drop_inherited_tests(SpeakHoles, tq.Speak)


if __name__ == "__main__":
    unittest.main()
