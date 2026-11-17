"""Tests of tools/helpers/registry_preflight.py (the check of `registry set` patch files). Offline, in a sandbox."""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

import sandbox

from saalib import common

HELPER = Path(__file__).resolve().parent.parent / "helpers" / "registry_preflight.py"
LIMITS = "https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html"
CASE = "https://aws.amazon.com/solutions/case-studies/tallis-freight/"
NOTE = "Frequency note (third-party research; planning input only, never evidence). Widgets are rank 1."


def _load():
    spec = importlib.util.spec_from_file_location("registry_preflight", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PreflightTest(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("preflight-" + self.id().split(".")[-1])
        self.folder = self.book / "_build" / "tmp" / "patches"
        self.folder.mkdir(parents=True)
        self.preflight = _load()

    def tearDown(self):
        sandbox.remove(self.book)

    def patch(self, **changes) -> dict:
        obj = {"sources": {"pages": [LIMITS]}, "bullets": ["1.1.K1"], "notes": NOTE}
        obj.update(changes)
        (self.folder / "patch-99.json").write_text(json.dumps(obj), encoding="utf-8")
        return obj

    def check(self) -> dict:
        with sandbox.paths(self.book):
            return self.preflight.check(self.folder)

    def codes(self, result) -> list:
        return [finding["code"] for finding in result["errors"]]

    def test_good_patch_passes(self):
        self.patch()
        result = self.check()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["patches"], 1)
        self.assertEqual(result["chapters"][0]["bullets"], 1)
        self.assertEqual([w["code"] for w in result["warnings"]], ["W13"])      # services but no guide

    def test_must_fail_url_not_in_corpus(self):
        self.patch(sources={"pages": [LIMITS, "https://docs.aws.amazon.com/widget-store/latest/userguide/missing.html"]})
        result = self.check()
        self.assertFalse(result["ok"])
        self.assertEqual(self.codes(result), ["P03"])

    def test_must_fail_redirected_url(self):
        self.patch()
        meta = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store" / "limits.meta.json"
        sandbox.edit_json(meta, lambda m: m.update(final_url="https://docs.aws.amazon.com/widget-store/latest/userguide/index.html"))
        result = self.check()
        self.assertEqual(self.codes(result), ["P04"])

    def test_same_page_with_md_extension_is_not_a_redirect(self):
        self.patch()
        meta = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store" / "limits.meta.json"
        sandbox.edit_json(meta, lambda m: m.update(final_url=LIMITS[:-5] + ".md"))
        self.assertTrue(self.check()["ok"])

    def test_must_fail_snapshot_without_text(self):
        self.patch()
        text = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store" / "limits.txt"
        text.write_text("too short\n", encoding="utf-8")
        self.assertEqual(self.codes(self.check()), ["P05"])

    def test_must_fail_host_outside_allow_list(self):
        self.patch(sources={"pages": ["https://example.com/"]})
        self.assertEqual(self.codes(self.check()), ["P02"])

    def test_must_fail_guide_root_without_index(self):
        self.patch(sources={"pages": [LIMITS], "guides": ["https://docs.aws.amazon.com/widget-store/latest/userguide/"]})
        result = self.check()
        self.assertEqual(self.codes(result), ["P06"])
        self.assertEqual(result["warnings"], [])

    def test_must_fail_unknown_bullet_and_task(self):
        self.patch(bullets=["1.1.K1", "1.1.K99"], tasks=["9.9"])
        self.assertEqual(self.codes(self.check()), ["P08", "P08"])

    def test_must_fail_cards_key_and_mapped_key(self):
        self.patch(cards=["gadget"], service_map={"Amazon Gadget Store": ["gadget"]})
        self.assertEqual(self.codes(self.check()), ["P09", "P09"])

    def test_must_fail_note_without_mark_or_too_long(self):
        self.patch(notes="Widgets are asked often.")
        self.assertEqual(self.codes(self.check()), ["P10"])
        self.patch(notes=NOTE + " x" * 1000)
        self.assertEqual(self.codes(self.check()), ["P10"])

    def test_must_fail_unknown_tags_and_faq_without_questions(self):
        self.patch(sources={"pages": [LIMITS], "faq": [CASE], "whatsnew_tags": ["amazon-widget"], "case_tags": ["widget"]})
        self.assertEqual(sorted(self.codes(self.check())), ["P07", "P11", "P11"])

    def test_must_fail_unknown_patch_key(self):
        self.patch(title="A seed-owned key")
        self.assertEqual(self.codes(self.check()), ["P01"])

    def test_warns_when_more_bullets_than_written_questions(self):
        with sandbox.paths(self.book):
            guide = common.read_json(common.REGISTRY / "exam-guide.json")
            spec = common.read_json(common.STYLE_DIR / "SPEC.json")
        write = spec["templates"]["deep"]["counts"]["questions"]["write"]
        bullets = [b["id"] for b in guide["bullets"]]
        self.patch(bullets=bullets)
        result = self.check()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual("W12" in [w["code"] for w in result["warnings"]], len(bullets) > write)

    def test_write_batch_lists_each_url_once(self):
        self.patch(sources={"pages": [LIMITS, CASE], "quotas": [LIMITS], "guides": ["https://docs.aws.amazon.com/x/"]})
        patches = self.preflight.load_patches(self.folder)
        self.assertEqual(self.preflight.urls_of(patches), [LIMITS, CASE])

    def test_cli_needs_a_folder_inside_the_book(self):
        self.assertEqual(self.preflight.main(["/tmp", "--check"]), common.EXIT_POLICY)
        empty = self.book / "_build" / "tmp" / "empty"
        empty.mkdir()
        self.assertEqual(self.preflight.main([str(empty), "--check"]), common.EXIT_PRECONDITION)


if __name__ == "__main__":
    unittest.main()
