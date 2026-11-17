"""Regression tests for the diagram holes of _build/reports/gate-break-practice.md (attempts 58 to 61)."""
import unittest

import sandbox
from saalib import common, ledger
from saalib.diagram import pipeline, shapes
from test_diagram_kinds import COMMON, RAW_OK, RawCase, check, codes, raw_spec, sequence_spec

RAW_PLAIN = RAW_OK.replace('  <use href="#ic-user" x="120" y="26" width="48" height="48"/>\n', "")


class RawGeometry(RawCase):
    def test_must_fail_58_two_labels_in_one_place(self):
        twice = RAW_OK.replace("</svg>", '  <text class="dg-nl" x="50" y="55">Other text</text>\n'
                                         '  <text class="dg-nl" x="52" y="56">Third</text>\n</svg>')
        self.assertIn("label-overlap", codes(self.raw(twice)))
        self.assertNotIn("label-overlap", codes(self.raw(RAW_OK)))

    def test_must_fail_58_text_wider_than_the_drawing(self):
        wide = RAW_OK.replace("</svg>", '  <text class="dg-el" x="150" y="20">A very long edge label</text>\n</svg>')
        self.assertIn("text-overflow", codes(self.raw(wide)))

    def test_must_fail_59_number_in_a_raw_text(self):
        number = RAW_OK.replace("Left part", "Max 999 TB")
        self.assertIn("label-number", codes(self.raw(number)))


class Labels(unittest.TestCase):
    def test_must_fail_59_node_label_with_a_number_that_the_claim_does_not_hold(self):
        spec = sequence_spec()
        spec["actors"][1]["label"] = "Max 999 TB"
        self.assertIn("label-number", codes(check(spec)))
        spec["claim"] = "The app server stores up to 999 TB for the user."
        self.assertNotIn("label-number", codes(check(spec)))
        self.assertNotIn("label-number", codes(check(sequence_spec())))

    def test_must_fail_60_second_sentence_that_starts_with_a_small_letter(self):
        self.assertFalse(shapes.one_sentence("A request passes through three tiers. it always uses 9 hops and never fails."))
        self.assertTrue(shapes.one_sentence("A request passes through three tiers."))
        spec = dict(sequence_spec(), claim="The user asks for a file. it never fails.")
        self.assertIn("claim", codes(check(spec)))


class DiagramsGate(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("diagram-holes-" + self.id().split(".")[-1])

    def tearDown(self):
        sandbox.remove(self.book)

    def test_must_fail_61_svg_that_is_not_the_output_of_its_spec(self):
        with sandbox.paths(self.book):
            common.write_json(common.DIAGRAM_SRC / "sample-hero.json", dict(COMMON, id="sample-hero", kind="raw", size="s"))
            (common.DIAGRAM_SRC / "sample-hero.svg").write_text(RAW_PLAIN, encoding="utf-8")
            gate = ledger.gate_diagrams("99")           # the fixture SVG was made from no spec
            self.assertEqual([e["code"] for e in gate["errors"]], ["D04"], gate["errors"])
            built = pipeline.build_one("sample-hero")
            self.assertEqual([i for i in built["issues"] if i["level"] == "error"], [])
            self.assertEqual(ledger.gate_diagrams("99")["errors"], [])
            svg = common.DIAGRAM_SVG / "sample-hero.svg"
            svg.write_text(svg.read_text(encoding="utf-8").replace("Left part", "Hand edit"), encoding="utf-8")
            self.assertEqual([e["code"] for e in ledger.gate_diagrams("99")["errors"]], ["D04"])


if __name__ == "__main__":
    unittest.main()
