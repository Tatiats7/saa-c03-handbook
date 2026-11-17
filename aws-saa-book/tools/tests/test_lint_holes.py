"""Regression tests for the holes of _build/reports/gate-break-grounding.md that live in saalib/lint.py and
saalib/_sync.py (H3 for L306, H10 to H14). The attempt id of the gate breaker is in each test name.
"""
import unittest

import sandbox
from test_lint import Base

MAXLINK = "(../facts/widget.md#widget-shelf-max-widgets)"


class HardClaimsWithoutLink(Base):
    """H10, H11, H12: L304 sees the number or the absolute word."""

    def flagged(self, sentence, code="L304", contains=None):
        self.add_sentence(sentence)
        return self.fails_with(code, contains=contains)

    def test_must_fail_l02_non_breaking_space(self):
        self.flagged("A crate holds 9000 widgets.")

    def test_must_fail_l03_number_in_words(self):
        self.flagged("A crate holds nine thousand widgets.")

    def test_must_fail_l04_adjective_between_number_and_noun(self):
        self.flagged("A crate holds 9000 small widgets.")

    def test_must_fail_l06_entity_for_the_space(self):
        self.flagged("A crate holds 9000&nbsp;widgets.")

    def test_must_fail_l12_plus_sign(self):
        self.flagged("A crate holds 9000+ widgets.")

    def test_must_fail_l31_full_width_digits(self):
        self.flagged("A crate holds ９０００ widgets.")

    def test_must_fail_l07_entity_inside_an_absolute_word(self):
        self.flagged("A shelf is alw&#97;ys open.", contains="always")

    def test_must_fail_l08_zero_width_space_inside_an_absolute_word(self):
        self.flagged("A crate is on​ly for shipping.", contains="only")

    def test_must_fail_l09_other_absolute_words(self):
        self.flagged("A crate is invariably public.", contains="invariably")

    def test_must_fail_l09_no_one(self):
        self.flagged("No one except the owner is able to delete it.", contains="No one")

    def test_must_fail_l10_can_not_in_two_words(self):
        self.flagged("You can not copy a crate.", contains="can not")

    def test_must_fail_l13_claim_in_inline_code(self):
        self.flagged("A crate holds `up to 9000 widgets`.")

    def test_must_fail_l14_claim_as_a_question(self):
        self.flagged("Did you know that a crate holds 9000 widgets?")

    def test_must_fail_l22_second_number_next_to_a_fact_link(self):
        self.flagged(f"A crate holds 9000 widgets, more than the [500 widgets]{MAXLINK} of a shelf.", contains="9000 widgets")

    def test_must_fail_l29_claim_in_a_summary_line(self):
        sandbox.replace_text(self.deep, "<summary>Go deeper: the shelf quota</summary>",
                             "<summary>Go deeper: a crate always holds 9000 widgets</summary>")
        self.fails_with("L304")

    def test_must_fail_l32_file_outside_the_template(self):
        (self.book / "99-sample" / "6-extra.md").write_text("# Extra\n\nA crate always holds 9000 widgets.\n", encoding="utf-8")
        self.fails_with("L101", draft=False, contains="6-extra.md")

    def test_a_command_in_inline_code_is_still_ignored(self):
        self.add_sentence("Run `aws widget list-shelves --max-items 5` to see the shelves.")
        code, result = self.lint()
        self.assertEqual(result["errors"], [])


class FactLinkText(Base):
    """H13: the link text holds the display and nothing that changes it."""

    def test_must_fail_l19_display_inside_a_number_written_with_a_space(self):
        self.add_sentence(f"A shelf holds [up to 2 500 widgets]{MAXLINK}.")
        self.fails_with("L303")

    def test_must_fail_l20_link_text_with_a_second_number(self):
        self.add_sentence(f"A shelf holds [not 500 widgets but 9000 widgets]{MAXLINK}.")
        self.fails_with("L303")

    def test_must_fail_l21_negated_display(self):
        self.add_sentence("A new shelf is [not private](../facts/widget.md#widget-shelf-default-private) for the team.")
        self.fails_with("L303", contains="not")

    def test_link_text_with_two_displays_of_one_fact_passes(self):
        self.add_sentence(f"The maximum grew from [200 widgets to 500 widgets]{MAXLINK}.")
        code, result = self.lint()
        self.assertEqual(result["errors"], [])


class QuoteBlocks(Base):
    """H3 for L306: a quote block is whole sentences of the evidence quote."""

    def test_must_fail_l30_quote_block_without_its_first_words(self):
        sandbox.replace_text(self.deep, '> "You cannot move a shelf to another Region."', '> "move a shelf to another Region."')
        self.fails_with("L306", contains="whole sentences")


class SyncFactSheets(Base):
    """H14: the chapter form of sync (the sync gate) reads the fact sheets; lint sees a missing sheet."""

    def test_must_fail_s02_hand_edited_fact_sheet(self):
        self.assertEqual(sandbox.run(self.book, "sync", "--all")[0], 0)
        sheet = self.book / "facts" / "widget.md"
        sandbox.replace_text(sheet, "500 widgets", "900 widgets")
        code, result, _err = self.sync("--check")
        self.assertEqual(code, 1)
        self.assertEqual(result["stale"], ["facts/widget.md"])
        code, result, _err = sandbox.run_json(self.book, "gate", "99", "--gate", "sync")
        self.assertEqual(code, 1)

    def test_must_fail_s03_deleted_fact_sheet(self):
        self.assertEqual(sandbox.run(self.book, "sync", "--all")[0], 0)
        (self.book / "facts" / "widget.md").unlink()
        code, result, _err = self.sync("--check")
        self.assertEqual(code, 1)
        self.assertEqual(result["missing"], ["facts/widget.md"])
        self.fails_with("L601", draft=False, contains="facts/widget.md")

    def test_must_fail_s04_orphan_fact_sheet(self):
        self.assertEqual(sandbox.run(self.book, "sync", "--all")[0], 0)
        (self.book / "facts" / "ghost.md").write_text(
            "<!-- generated by saa.py; do not edit -->\n# Ghost: facts\n\n### ghost-limit\n\n**Claim.** A ghost holds 9 widgets.\n",
            encoding="utf-8")
        code, result, _err = sandbox.run_json(self.book, "sync", "--all", "--check")
        self.assertEqual(code, 1)
        self.assertIn("facts/ghost.md", result["stale"])


if __name__ == "__main__":
    unittest.main()
