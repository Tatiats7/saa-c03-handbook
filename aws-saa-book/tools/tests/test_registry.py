"""Tests for saalib/registry.py: `registry build|set|check|show|wave-args` and `coverage` (TOOLS.md section 4).

Run:  python3 aws-saa-book/tools/tests/run.py registry

Every test works on a sandbox copy of the fixture book. No test makes a network request
(`registry build` always runs with --offline).
"""
import json
import unittest

import sandbox
from saalib import common, registry, schemas

FIX = common.FIXTURES / "book"
GUIDE = "_build/registry/exam-guide.json"
SERVICES = "_build/registry/services.json"
SNAP = "_build/corpus/snap/docs/fixture/exam-guide"

# Small excerpts in the markup of the real exam guide pages (invented service names).
DOMAIN_EXCERPT = """

# Content Domain 2: Design Resilient Widget Stores
<a name="x-domain2"></a>

**Topics**
+ [Task 2.1: Design scalable storage](#x-task1)
+ [Task 2.2: Design storage for two Regions](#x-task2)

## Task 2.1: Design scalable storage
<a name="x-task1"></a>

Knowledge of:
+ Shelf capacity (for example, widgets per shelf)
+ Storage types

Skills in:
+ Selecting a shelf

This paragraph is not a bullet.
+ This list has no label and is skipped

## Task 2.2: Design storage for two Regions
<a name="x-task2"></a>

Skills in:
- Copying a shelf
* Moving a crate
"""

SERVICES_EXCERPT = """

# In-Scope AWS Services
<a name="x"></a>

**Topics**
+ [Security](#x-security)

## Security, Identity, and Compliance
<a name="x-security"></a>
+ AWS Sample Access Manager (SAM9)
+ Amazon Widget Store

## Storage
+ Amazon Widget Store
"""


def page(text, sid="docs/x/page"):
    return {"source_id": sid, "url": "https://docs.aws.amazon.com/x/latest/guide/page.html", "sha256": "0" * 64, "text": text}


def codes(findings):
    return [f["code"] for f in findings]


def strip_time(doc):
    doc = dict(doc)
    doc.pop("built_at", None)
    return doc


class Base(unittest.TestCase):
    def setUp(self):
        self.book = sandbox.make("registry-" + self.id().split(".")[-1])

    def tearDown(self):
        sandbox.remove(self.book)

    def load(self, relative):
        return common.read_json(self.book / relative)

    def patch_file(self, obj):
        path = self.book / "_build" / "patch.json"
        common.write_json(path, obj)
        return str(path)


class Parser(unittest.TestCase):
    def test_domain_page_tasks_and_bullets(self):
        parsed = registry.parse_pages([page(DOMAIN_EXCERPT)])
        self.assertEqual(parsed["pages"][0]["role"], "domain")
        self.assertEqual([(t["id"], t["title"], t["line"]) for t in parsed["tasks"]],
                         [("2.1", "Design scalable storage", 10), ("2.2", "Design storage for two Regions", 23)])
        self.assertEqual([b["id"] for b in parsed["bullets"]], ["2.1.K1", "2.1.K2", "2.1.S1", "2.2.S1", "2.2.S2"])
        self.assertEqual(parsed["bullets"][0]["text"], "Shelf capacity (for example, widgets per shelf)")
        self.assertEqual(parsed["bullets"][0]["line"], 14)
        self.assertEqual((parsed["bullets"][3]["kind"], parsed["bullets"][3]["n"], parsed["bullets"][3]["domain"]), ("skill", 1, 2))
        lines = DOMAIN_EXCERPT.splitlines()
        for bullet in parsed["bullets"]:
            self.assertEqual(lines[bullet["line"] - 1][2:], bullet["text"])

    def test_services_page_short_names_and_merge(self):
        parsed = registry.parse_pages([page(SERVICES_EXCERPT)])
        self.assertEqual(parsed["pages"][0]["role"], "in-scope")
        self.assertEqual(len(parsed["in_scope_raw"]), 3)
        book = {"chapters": [{"id": "03", "slug": "sam", "tier": "medium", "services": ["sam9"]},
                             {"id": "21", "slug": "w", "tier": "deep", "services": ["widget-store"]}], "service_map": {}}
        entries = registry._entries(parsed["in_scope_raw"], book, True)
        self.assertEqual(len(entries), 2)
        self.assertEqual((entries[0]["short_name"], entries[0]["keys"], entries[0]["home_chapter"], entries[0]["level"]),
                         ("SAM9", ["sam9"], "03", "medium"))
        self.assertEqual(entries[1]["categories"], ["Security, Identity, and Compliance", "Storage"])
        self.assertEqual((entries[1]["keys"], entries[1]["line"]), (["widget-store"], 12))

    def test_automatic_match_and_service_map(self):
        self.assertEqual(registry.auto_slugs("Amazon Managed Crate Service (Amazon MCS)", "Amazon MCS"),
                         ["managed-crate-service", "mcs"])
        book = {"chapters": [{"id": "10", "slug": "c", "tier": "deep", "services": ["mcs", "crates"]}],
                "service_map": {"Amazon Widget Store": ["crates", "mcs"]}}
        self.assertEqual(registry.keys_for("Amazon Managed Crate Service (Amazon MCS)", "Amazon MCS", book), ["mcs"])
        self.assertEqual(registry.keys_for("Amazon Widget Store", None, book), ["crates", "mcs"])
        self.assertEqual(registry.keys_for("Amazon Gadget Service", None, book), [])

    def test_weights_and_roles(self):
        overview = "# Guide\n\n+ [Content Domain 1: A b c (60% of scored content)](#a)\n+ Content Domain 2: D e f (40% of scored content)\n"
        parsed = registry.parse_pages([page(overview, "docs/x/o"), page("# Something else\n\n+ a list\n", "docs/x/p")])
        self.assertEqual([p["role"] for p in parsed["pages"]], ["overview", "other"])
        self.assertEqual([(d["id"], d["title"], d["weight"]) for d in parsed["domains"]], [(1, "A b c", 60), (2, "D e f", 40)])
        self.assertTrue(any("4 domains" in p for p in parsed["problems"]))

    def test_must_fail_weights_that_add_up_to_99(self):
        lines = "".join(f"+ Content Domain {n}: Title {n} ({w}% of scored content)\n" for n, w in ((1, 29), (2, 26), (3, 24), (4, 20)))
        parsed = registry.parse_pages([page("# Guide\n\n" + lines)])
        self.assertEqual(len(parsed["domains"]), 4)
        self.assertTrue(any("99" in p for p in parsed["problems"]))


class Build(Base):
    def test_build_offline_gives_exactly_the_fixture_files(self):
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 0, err)
        self.assertEqual(result, {"chapters": 1, "domains": 4, "tasks": 5, "bullets": 13, "in_scope": 3,
                                  "in_scope_unique": 2, "out_of_scope": 1, "unmapped": [], "changed_bullets": []})
        for name in (GUIDE, SERVICES):
            self.assertEqual(strip_time(self.load(name)), strip_time(common.read_json(FIX / name)), name)
        book, fixture = self.load("data/book.json"), common.read_json(FIX / "data" / "book.json")
        book["book"].pop("built_at")
        fixture["book"].pop("built_at")
        self.assertEqual(book, fixture)
        for name, schema in ((GUIDE, "exam-guide"), (SERVICES, "services"), ("data/book.json", "book")):
            self.assertEqual(schemas.validate(self.load(name), schema), [], name)

    def test_build_from_nothing_but_the_pages(self):
        (self.book / GUIDE).unlink()
        (self.book / SERVICES).unlink()
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 0, err)
        self.assertEqual(strip_time(self.load(GUIDE)), strip_time(common.read_json(FIX / GUIDE)))
        self.assertEqual(strip_time(self.load(SERVICES)), strip_time(common.read_json(FIX / SERVICES)))

    def test_seed_owns_its_keys_and_tool_keys_are_kept(self):
        seed = common.read_json(FIX / "data" / "book.json")
        seed["book"] = {k: seed["book"][k] for k in ("title", "exam", "snapshot_date", "change_window_start",
                                                     "exam_eligibility_cutoff", "mock_seed", "domain_split")}
        seed.pop("service_map")
        seed["chapters"] = [{"id": "99", "slug": "sample", "title": "Widget Store, renamed", "part": "storage", "tier": "deep",
                             "wave": "W1", "services": ["widget"]},
                            {"id": "98", "slug": "new", "title": "New chapter", "part": "storage", "tier": "deep",
                             "wave": "W1", "services": ["gizmo"]}]
        common.write_json(self.book / "_build" / "registry" / "book.seed.json", seed)
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 0, err)
        book = self.load("data/book.json")
        first, second = book["chapters"]
        self.assertEqual((first["title"], first["wave"]), ("Widget Store, renamed", "W1"))
        self.assertEqual(len(first["bullets"]), 13)
        self.assertEqual(len(first["sources"]["pages"]), 2)
        self.assertEqual((second["tasks"], second["bullets"]), ([], []))
        self.assertEqual(sorted(second["sources"]), sorted(registry.SOURCE_LISTS))
        self.assertEqual(book["book"]["exam_guide"]["guide_id"], "fixture-exam-guide")
        self.assertEqual(book["service_map"]["Amazon Widget Store"], ["widget"])
        self.assertEqual(schemas.validate(book, "book"), [])

    def test_first_build_from_the_seed_adds_the_defaults(self):
        with sandbox.paths(self.book):
            seed = {"book": {"title": "T"}, "parts": [], "chapters": [{"id": "01", "slug": "a", "services": []}]}
            book = registry._merge_book(seed, None, {"version": "0.9"})
        self.assertEqual(book["book"]["fact_namespaces"], {"exam": "01"})
        self.assertEqual(book["book"]["style_version"], "0.9")
        self.assertEqual(book["book"]["exam_guide"]["guide_id"], "aws-certification-solutions-architect-associate-03")
        self.assertEqual(book["service_map"], {})
        self.assertEqual(book["chapters"][0]["sources"]["whatsnew_tags"], [])

    def test_unmapped_entry_gives_exit_2(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["service_map"].__delitem__("Amazon Widget Store"))
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 2, err)
        self.assertEqual(result["unmapped"], ["Amazon Widget Store"])
        entry = self.load(SERVICES)["in_scope"][0]
        self.assertEqual((entry["keys"], entry["home_chapter"], entry["level"]), ([], None, None))
        self.assertEqual(self.load(SERVICES)["counts"]["unmapped"], 1)

    def test_must_fail_changed_bullet_text(self):
        sandbox.replace_text(self.book / SNAP / "domain1.txt", "The shared responsibility model for widgets",
                             "The shared responsibility model for crates")
        before = (self.book / GUIDE).read_text(encoding="utf-8")
        book_before = (self.book / "data" / "book.json").read_text(encoding="utf-8")
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 1)
        self.assertEqual(result["changed_bullets"], ["1.1.K2"])
        self.assertEqual((self.book / GUIDE).read_text(encoding="utf-8"), before)
        self.assertEqual((self.book / "data" / "book.json").read_text(encoding="utf-8"), book_before)
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline", "--accept-changes")
        self.assertEqual(code, 0, err)
        self.assertEqual(result["changed_bullets"], ["1.1.K2"])
        texts = {b["id"]: b["text"] for b in self.load(GUIDE)["bullets"]}
        self.assertEqual(texts["1.1.K2"], "The shared responsibility model for crates")

    def test_must_fail_removed_bullet_id(self):
        sandbox.replace_text(self.book / SNAP / "domain1.txt", "+ Designing an access model for shelves that several teams use\n", "")
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 1)
        self.assertEqual(result["changed_bullets"], ["1.1.S1"])

    def test_must_fail_overview_weights_add_up_to_99(self):
        sandbox.replace_text(self.book / SNAP / "overview.txt", "(30% of scored content)", "(29% of scored content)")
        before = (self.book / GUIDE).read_text(encoding="utf-8")
        code, result, err = sandbox.run_json(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 1)
        self.assertIn("99", result["error"])
        self.assertEqual((self.book / GUIDE).read_text(encoding="utf-8"), before)

    def test_must_fail_missing_index_or_snapshot_is_a_precondition(self):
        (self.book / SNAP / "domain3.txt").unlink()
        code, out, err = sandbox.run(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 3)
        (self.book / "_build" / "corpus" / "index" / "fixture-exam-guide.json").unlink()
        code, out, err = sandbox.run(self.book, "registry", "build", "--offline")
        self.assertEqual(code, 3)

    def test_python_api(self):
        with sandbox.paths(self.book):
            self.assertEqual(registry.exam_guide()["counts"]["bullets"], 13)
            self.assertEqual(len(registry.services()["in_scope"]), 2)
            self.assertEqual(registry.service_keys_in_scope(), {"widget"})
            (self.book / SERVICES).unlink()
            self.assertIsNone(registry.services())
            self.assertEqual(registry.service_keys_in_scope(), set())


class Check(Base):
    def check(self, *extra):
        return sandbox.run_json(self.book, "registry", "check", *extra)

    def test_fixture_passes(self):
        code, result, err = self.check()
        self.assertEqual((code, result["errors"], result["warnings"]), (0, [], []), err)
        self.assertEqual(result["counts"], {"chapters": 1, "bullets_unassigned": 0, "services_unmapped": 0})
        self.assertTrue(result["ok"])
        code, result, err = self.check("--urls")
        self.assertEqual((code, result["errors"]), (0, []), err)

    def test_text_output_is_short(self):
        code, out, err = sandbox.run(self.book, "registry", "check")
        self.assertEqual(code, 0, err)
        self.assertTrue(out.startswith("registry check: ok"))
        self.assertLessEqual(len(out.splitlines()), 41)

    def test_must_fail_bullet_in_no_chapter(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0]["bullets"].remove("4.1.S1"))
        code, result, err = self.check()
        self.assertEqual(code, 1)
        self.assertEqual(codes(result["errors"]), ["R03"])
        self.assertEqual(result["errors"][0]["item"], "4.1.S1")
        self.assertEqual(result["counts"]["bullets_unassigned"], 1)
        # W0 integration: the text form must name the bullet (it printed only `data/book.json: R03 ...`).
        code, out, err = sandbox.run(self.book, "registry", "check")
        self.assertEqual(code, 1)
        self.assertIn("R03 bullet is in the bullets of no chapter [4.1.S1]", out)

    def test_must_fail_task_in_no_chapter(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0]["tasks"].remove("3.1"))
        code, result, err = self.check()
        self.assertEqual((code, codes(result["errors"])), (1, ["R03"]))

    def test_must_fail_removed_service_map_entry(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["service_map"].__delitem__("Amazon Widget Store"))
        code, result, err = self.check()
        self.assertEqual(code, 1)
        self.assertEqual(codes(result["errors"]), ["R04"])
        self.assertEqual(result["counts"]["services_unmapped"], 1)

    def test_must_fail_schema_error(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0].update(wave="W16"))
        code, result, err = self.check()
        self.assertEqual(code, 1)
        self.assertIn("R01", codes(result["errors"]))

    def test_must_fail_missing_exam_guide(self):
        (self.book / GUIDE).unlink()
        code, result, err = self.check()
        self.assertEqual(code, 1)
        self.assertEqual(codes(result["errors"]), ["R01"])

    def test_must_fail_duplicate_key_unknown_part_unknown_template(self):
        def change(book):
            other = json.loads(json.dumps(book["chapters"][0]))
            other.update(id="98", slug="other", part="nowhere", tier="medium", bullets=[], tasks=[])
            book["chapters"].append(other)
        sandbox.edit_json(self.book / "data" / "book.json", change)
        code, result, err = self.check()
        self.assertEqual(code, 1)
        messages = [f["msg"] for f in result["errors"] if f["code"] == "R02"]
        self.assertEqual(len(messages), 3, messages)
        self.assertTrue(any("service key `widget` is used twice" in m for m in messages))
        self.assertTrue(any("part `nowhere`" in m for m in messages))
        self.assertTrue(any("template `medium`" in m for m in messages))

    def test_must_fail_front_chapter_without_override_and_bad_cards_key(self):
        def change(book):
            book["chapters"][0]["tier"] = "front"
            book["chapters"][0]["cards"] = ["gizmo"]
        sandbox.edit_json(self.book / "data" / "book.json", change)
        code, result, err = self.check()
        self.assertEqual(code, 1)
        messages = [f["msg"] for f in result["errors"] if f["code"] == "R02"]
        self.assertTrue(any("chapter_overrides" in m for m in messages), messages)
        self.assertTrue(any("cards key `gizmo`" in m for m in messages), messages)

    def test_must_fail_service_key_of_an_out_of_scope_entry(self):
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0]["services"].append("gadget-service"))
        code, result, err = self.check()
        self.assertEqual(code, 1)
        self.assertEqual(codes(result["errors"]), ["R05"])
        self.assertEqual(codes(result["warnings"]), ["R11"])

    def test_must_fail_source_on_a_foreign_host(self):
        sandbox.edit_json(self.book / "data" / "book.json",
                          lambda b: b["chapters"][0]["sources"]["faq"].append("https://example.com/faq/"))
        code, result, err = self.check()
        self.assertEqual((code, codes(result["errors"])), (1, ["R06"]))

    def test_must_fail_url_that_is_not_in_the_corpus(self):
        sandbox.edit_json(self.book / "data" / "book.json",
                          lambda b: b["chapters"][0]["sources"]["faq"].append("https://aws.amazon.com/widget-store/faqs/"))
        code, result, err = self.check()
        self.assertEqual(code, 0, result)
        code, result, err = self.check("--urls")
        self.assertEqual((code, codes(result["errors"])), (1, ["R06"]))

    def test_must_fail_guide_root_without_an_index(self):
        # A guide root (sources.guides) is not a page and has no snapshot. With --urls it is in the
        # corpus only when `saa.py guide ROOT` has written its index under corpus/index/.
        root = "https://docs.aws.amazon.com/widget-store/latest/userguide/"
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0]["sources"]["guides"].append(root))
        code, result, err = self.check()
        self.assertEqual(code, 0, result)
        code, result, err = self.check("--urls")
        self.assertEqual((code, codes(result["errors"])), (1, ["R06"]))
        self.assertIn("has no guide index", result["errors"][0]["msg"])
        index_dir = self.book / "_build" / "corpus" / "index"
        common.write_json(index_dir / "other-guide.json",       # an index of another guide does not count
                          {"guide_id": "other-guide", "root": "https://docs.aws.amazon.com/other/latest/userguide/", "pages": []})
        code, result, err = self.check("--urls")
        self.assertEqual((code, codes(result["errors"])), (1, ["R06"]))
        common.write_json(index_dir / "widget-store-userguide.json",
                          {"guide_id": "widget-store-userguide", "root": root, "pages": []})
        code, result, err = self.check("--urls")
        self.assertEqual((code, result["errors"]), (0, []), err)

    def test_guide_index_with_its_own_id_is_found_by_its_root(self):
        root = "https://docs.aws.amazon.com/widget-store/latest/userguide/"
        sandbox.edit_json(self.book / "data" / "book.json", lambda b: b["chapters"][0]["sources"]["guides"].append(root))
        common.write_json(self.book / "_build" / "corpus" / "index" / "widgets.json",      # made with `guide --id widgets`
                          {"guide_id": "widgets", "root": root, "pages": []})
        code, result, err = self.check("--urls")
        self.assertEqual((code, result["errors"]), (0, []), err)

    def test_must_fail_fact_namespace(self):
        sandbox.edit_json(self.book / "data" / "book.json",
                          lambda b: b["book"].update(fact_namespaces={"exam": "01", "widget": "99"}))
        code, result, err = self.check()
        self.assertEqual((code, codes(result["errors"])), (1, ["R07", "R07"]))

    def test_warnings_r11_r12_r16(self):
        def change(book):
            book["chapters"][0]["services"].append("gizmo")
            book["chapters"][0]["sources"]["pages"] = []
        sandbox.edit_json(self.book / "data" / "book.json", change)
        code, result, err = self.check()
        self.assertEqual((code, result["errors"]), (2, []))
        self.assertEqual(sorted(codes(result["warnings"])), ["R11", "R12"])

    def test_warning_r16_redirected_snapshot(self):
        meta = self.book / "_build" / "corpus" / "snap" / "docs" / "fixture" / "widget-store" / "limits.meta.json"
        sandbox.edit_json(meta, lambda m: m.update(final_url="https://docs.aws.amazon.com/widget-store/latest/userguide/quotas.html"))
        code, result, err = self.check("--urls")
        self.assertEqual((code, codes(result["warnings"])), (2, ["R16"]), result)


class Set(Base):
    def set(self, *args):
        return sandbox.run_json(self.book, "registry", "set", *args)

    def test_merge_lists_and_tasks_of_bullets(self):
        def change(book):
            book["chapters"][0]["bullets"] = ["1.1.K1"]
            book["chapters"][0]["tasks"] = ["1.1"]
        sandbox.edit_json(self.book / "data" / "book.json", change)
        patch = self.patch_file({"sources": {"faq": ["https://aws.amazon.com/widget-store/faqs/"],
                                             "pages": ["https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html",
                                                       "https://docs.aws.amazon.com/widget-store/latest/userguide/crates.html"],
                                             "whatsnew_tags": ["amazon-widget-store"]},
                                 "bullets": ["2.2.K1", "1.1.K1"]})
        code, result, err = self.set("99", "--file", patch, "--bullets", "2.1.S1,2.2.S1", "--by", "tester")
        self.assertEqual(code, 0, err)
        self.assertEqual(result, {"chapter": "99", "added": {"sources.pages": 1, "sources.faq": 1, "sources.whatsnew_tags": 1,
                                                             "bullets": 3, "tasks": 2}, "tasks": ["1.1", "2.2", "2.1"]})
        ch = self.load("data/book.json")["chapters"][0]
        self.assertEqual(ch["bullets"], ["1.1.K1", "2.2.K1", "2.1.S1", "2.2.S1"])
        self.assertEqual(len(ch["sources"]["pages"]), 3)
        self.assertEqual(ch["sources"]["pages"][0], "https://docs.aws.amazon.com/widget-store/latest/userguide/limits.html")
        code, result, err = self.set("sample", "--bullets", "2.2.K1")
        self.assertEqual((code, result["added"]), (0, {}), err)

    def test_replace(self):
        patch = self.patch_file({"sources": {"pages": ["https://docs.aws.amazon.com/widget-store/latest/userguide/crates.html"]},
                                 "bullets": ["3.1.K1"]})
        code, result, err = self.set("99-sample", "--file", patch, "--replace", "sources.pages", "bullets", "--replace", "tasks")
        self.assertEqual(code, 0, err)
        ch = self.load("data/book.json")["chapters"][0]
        self.assertEqual(ch["sources"]["pages"], ["https://docs.aws.amazon.com/widget-store/latest/userguide/crates.html"])
        self.assertEqual((ch["bullets"], ch["tasks"], result["tasks"]), (["3.1.K1"], ["3.1"], ["3.1"]))

    def test_map_recomputes_the_keys_of_services_json(self):
        code, result, err = self.set("99", "--map", "Amazon Widget Store=")
        self.assertEqual(code, 0, err)
        doc = self.load(SERVICES)
        self.assertEqual((doc["in_scope"][0]["keys"], doc["in_scope"][0]["home_chapter"], doc["counts"]["unmapped"]), ([], None, 1))
        self.assertNotIn("Amazon Widget Store", self.load("data/book.json")["service_map"])
        code, result, err = self.set("99", "--map", "Amazon Widget Store=widget")
        self.assertEqual((code, result["added"]), (0, {"service_map": 1}), err)
        self.assertEqual(strip_time(self.load(SERVICES)), strip_time(common.read_json(FIX / SERVICES)))

    def test_cards(self):
        code, result, err = self.set("99", "--cards", "widget")
        self.assertEqual(code, 0, err)
        self.assertEqual(self.load("data/book.json")["chapters"][0]["cards"], ["widget"])
        code, result, err = self.set("99", "--cards", "gizmo")
        self.assertEqual(code, 1)

    def test_notes(self):
        note = "frequency (third-party research, not evidence): reported often;\n  sub-topics: shelves, crates"
        code, result, err = self.set("99", "--file", self.patch_file({"notes": note}))
        self.assertEqual((code, result["added"]), (0, {"notes": 1}), err)
        want = "frequency (third-party research, not evidence): reported often; sub-topics: shelves, crates"
        self.assertEqual(self.load("data/book.json")["chapters"][0]["notes"], want)
        code, out, err = sandbox.run(self.book, "registry", "show", "99")
        self.assertIn("notes: frequency (third-party research, not evidence)", out)
        code, result, err = self.set("99", "--file", self.patch_file({"notes": want}))      # the same note: nothing new
        self.assertEqual((code, result["added"]), (0, {}), err)
        code, result, err = self.set("99", "--bullets", "2.2.K1")                            # another patch keeps the note
        self.assertEqual(self.load("data/book.json")["chapters"][0]["notes"], want)
        code, result, err = self.set("99", "--file", self.patch_file({"notes": ""}))        # an empty note removes it
        self.assertEqual((code, result["added"]), (0, {"notes": 1}), err)
        self.assertNotIn("notes", self.load("data/book.json")["chapters"][0])
        self.assertEqual(schemas.validate(self.load("data/book.json"), "book"), [])

    def test_must_fail_notes_that_is_not_one_short_string(self):
        for bad in (["frequency: high"], {"frequency": "high"}, 7, "x" * (registry.NOTES_MAX_CHARS + 1)):
            code, result, err = self.set("99", "--file", self.patch_file({"notes": bad}))
            self.assertEqual(code, 1, bad)
            self.assertIn("notes", result["error"])
        self.assertTrue(self.unchanged())

    def unchanged(self):
        return self.load("data/book.json") == common.read_json(FIX / "data" / "book.json")

    def test_must_fail_seed_owned_key(self):
        code, result, err = self.set("99", "--file", self.patch_file({"title": "Another title"}))
        self.assertEqual(code, 1)
        self.assertIn("seed", result["error"])
        self.assertTrue(self.unchanged())

    def test_must_fail_foreign_host(self):
        code, result, err = self.set("99", "--file", self.patch_file({"sources": {"faq": ["https://example.com/"]}}))
        self.assertEqual(code, 4)
        self.assertTrue(self.unchanged())

    def test_must_fail_unknown_bullet(self):
        code, result, err = self.set("99", "--bullets", "4.4.K9")
        self.assertEqual(code, 1)
        self.assertTrue(self.unchanged())

    def test_must_fail_mapped_key_that_no_chapter_has(self):
        code, result, err = self.set("99", "--map", "Amazon Widget Store=gizmo")
        self.assertEqual(code, 1)
        code, result, err = self.set("99", "--file", self.patch_file({"service_map": {"Amazon Widget Store": ["widget", "gizmo"]}}))
        self.assertEqual(code, 1)
        self.assertTrue(self.unchanged())

    def test_must_fail_file_outside_the_book(self):
        code, out, err = sandbox.run(self.book, "registry", "set", "99", "--file", str(common.REPO / "README.md"))
        self.assertEqual(code, 4)

    def test_must_fail_unknown_chapter(self):
        code, out, err = sandbox.run(self.book, "registry", "set", "42", "--bullets", "1.1.K1")
        self.assertEqual(code, 3)


class ShowWaveCoverage(Base):
    def test_show(self):
        code, result, err = sandbox.run_json(self.book, "registry", "show", "sample")
        self.assertEqual(code, 0, err)
        self.assertEqual(result["chapter"]["id"], "99")
        self.assertEqual(result["bullets"][0], {"id": "1.1.K1", "text": "Shelf access controls (for example, private shelves)"})
        self.assertEqual([s["official_name"] for s in result["services"]],
                         ["Amazon Widget Store", "Amazon Managed Crate Service (Amazon MCS)"])
        code, out, err = sandbox.run(self.book, "registry", "show", "99")
        self.assertIn("bullet 4.1.S1: Designing the lowest-cost storage", out)

    def test_wave_args(self):
        code, out, err = sandbox.run(self.book, "registry", "wave-args", "W0")
        self.assertEqual(code, 0, err)
        self.assertEqual(len(out.strip().splitlines()), 1)
        result = json.loads(out)
        self.assertEqual((result["wave"], result["skipped"]), ("W0", []))
        ch = result["chapters"][0]
        self.assertEqual({k: ch[k] for k in ("id", "slug", "dir", "tier", "template", "xl", "services", "bullets", "mine_lenses",
                                             "status", "next_stage")},
                         {"id": "99", "slug": "sample", "dir": "99-sample", "tier": "deep", "template": "deep", "xl": False,
                          "services": ["widget"], "bullets": 13, "mine_lenses": 5, "status": "facts-verified",
                          "next_stage": "brief"})
        self.assertEqual(ch["counts"], {"questions_write": 4, "questions_ship": 4, "speak": 1, "cards": 3, "tasks_max": 2})
        self.assertEqual(ch["tasks"], ["1.1", "2.1", "2.2", "3.1", "4.1"])

    def test_wave_args_skips_a_ready_chapter(self):
        sandbox.edit_json(self.book / "_build" / "ledger" / "chapters" / "99.json", lambda d: d.update(status="ready"))
        code, out, err = sandbox.run(self.book, "registry", "wave-args", "0")
        self.assertEqual(code, 0, err)
        self.assertEqual(json.loads(out), {"wave": "W0", "chapters": [], "skipped": [{"id": "99", "reason": "ready"}]})

    def test_must_fail_unknown_wave(self):
        code, out, err = sandbox.run(self.book, "registry", "wave-args", "W9")
        self.assertEqual(code, 3)

    def test_coverage_report(self):
        code, result, err = sandbox.run_json(self.book, "coverage")
        self.assertEqual(code, 2, err)
        self.assertEqual(result["errors"], [])
        doc = self.load("_build/reports/coverage.json")
        self.assertEqual(sorted(doc), ["bullets", "errors", "services", "tasks", "warnings"])
        self.assertEqual((len(doc["bullets"]), len(doc["services"]), len(doc["tasks"])), (13, 2, 5))
        self.assertEqual(sorted(doc["bullets"][0]), ["chapters", "id", "mock_questions", "questions", "ready_chapters"])
        self.assertEqual((doc["bullets"][0]["chapters"], doc["bullets"][0]["ready_chapters"]), (["99"], 0))
        service = doc["services"][0]
        self.assertEqual((service["id"], service["keys"], service["home_chapter"], service["level"]),
                         ("amazon-widget-store", ["widget"], "99", "deep"))
        questions = [q for q in self.load("data/99-sample/questions.json")["items"]
                     if q["status"] == "ready" and q["pool"] in ("chapter", "drill")]
        self.assertEqual(service["questions"], len([q for q in questions if "widget" in q["services"]]))
        self.assertEqual(service["facts"], 7)
        self.assertEqual(service["cards"], len([c for c in self.load("data/99-sample/cards.json")["items"] if c["status"] == "ready"]))
        self.assertEqual(sum(t["questions"] for t in doc["tasks"]), len(questions))
        self.assertEqual(sum(b["questions"] for b in doc["bullets"]), sum(len(q["bullets"]) for q in questions))
        self.assertIn("V01", codes(doc["warnings"]))
        self.assertTrue((self.book / "_build" / "reports" / "coverage.md").read_text(encoding="utf-8").startswith("# Coverage"))

    def test_must_fail_release_with_a_chapter_that_is_not_ready(self):
        code, result, err = sandbox.run_json(self.book, "coverage", "--release")
        self.assertEqual(code, 1)
        self.assertIn("V01", codes(result["errors"]))
        self.assertFalse(result["ok"])

    def test_must_fail_release_service_without_home_chapter(self):
        def change(doc):
            doc["in_scope"][1].update(keys=[], home_chapter=None, level=None)
        sandbox.edit_json(self.book / SERVICES, change)
        code, result, err = sandbox.run_json(self.book, "coverage", "--release")
        self.assertEqual(code, 1)
        doc = self.load("_build/reports/coverage.json")
        self.assertIn("V02", codes(doc["errors"]))

    def test_must_fail_release_task_absent_from_a_mock(self):
        def change(book):
            book["chapters"].append({"id": "50", "slug": "mock-exam-1", "title": "Mock exam 1", "part": "storage", "tier": "mock",
                                     "wave": "W13", "services": []})
        sandbox.edit_json(self.book / "data" / "book.json", change)
        code, result, err = sandbox.run_json(self.book, "coverage", "--release")
        self.assertEqual(code, 1)
        doc = self.load("_build/reports/coverage.json")
        self.assertEqual(len([f for f in doc["errors"] if f["code"] == "V04"]), 5)
        self.assertEqual(doc["tasks"][0]["mock"], {"50": 0})

    def test_must_fail_coverage_without_registry_files(self):
        (self.book / GUIDE).unlink()
        code, out, err = sandbox.run(self.book, "coverage")
        self.assertEqual(code, 3)


if __name__ == "__main__":
    unittest.main()
