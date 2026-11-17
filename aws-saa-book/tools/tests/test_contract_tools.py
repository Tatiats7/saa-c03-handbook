"""Tests for the tool contract: the schemas named in TOOLS.md, the shared validator, the sandbox helper
and the fixture build state (facts, votes, requests, registry, exam guide, ledger).

Run:  python3 aws-saa-book/tools/tests/run.py contract      (runs test_contract.py too)

These tests read files and one sandbox copy. They prove that the fixture obeys the data rules that
TOOLS.md states (so module authors can trust it), not that any module is implemented.
"""
import copy
import json
import re
import unittest

import sandbox
from saalib import common, schemas

REAL = common.REAL_BOOK
FIX = common.FIXTURES / "book"
SCHEMA_NAMES = ["fact", "vote", "fact-request", "book", "exam-guide", "services", "ledger-chapter", "gate",
                "change-item", "case-item", "mock"]
STAGES = ["plan", "mine", "register", "verify-facts", "brief", "prose", "questions", "tasks", "cards", "speak",
          "diagrams", "edit", "review", "fix", "verify-questions", "finalize"]
POSITIVE = {"entail": "support", "derive": "support", "currency": "current", "rederive": "match"}
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def keywords(node, found):
    """Collect schema keywords, walking only into sub-schemas (not into property names)."""
    if isinstance(node, dict):
        for key, sub in node.items():
            found.add(key)
            if key in ("properties", "$defs"):
                for child in sub.values():
                    keywords(child, found)
            elif key == "items":
                keywords(sub, found)
    return found


def numbers(text):
    return {n.replace(",", "").rstrip(".") for n in NUMBER.findall(text)}


def words(text):
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def facts():
    return common.read_jsonl(FIX / "data" / "facts" / "widget.jsonl")


class SchemaFiles(unittest.TestCase):
    def test_schemas_use_only_the_declared_keywords(self):
        allowed = set(load(REAL / "_build" / "style" / "SPEC.json")["data_files"]["schema_keywords_used"])
        for name in SCHEMA_NAMES:
            schema = load(REAL / "_build" / "schemas" / f"{name}.schema.json")
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema", name)
            self.assertEqual(schema["$id"], f"{name}.schema.json")
            used = keywords(schema, set())
            self.assertTrue(used <= allowed, f"{name}: {sorted(used - allowed)}")

    def test_ledger_schema_names_every_stage_of_tools_md(self):
        schema = schemas.load("ledger-chapter")
        self.assertEqual(list(schema["properties"]["stages"]["properties"]), STAGES)
        text = (REAL / "_build" / "style" / "TOOLS.md").read_text(encoding="utf-8")
        for stage in STAGES:
            self.assertIn(f"| `{stage}` |", text)

    def test_gate_schema_names_every_gate_of_tools_md(self):
        text = (REAL / "_build" / "style" / "TOOLS.md").read_text(encoding="utf-8")
        for gate in schemas.load("gate")["properties"]["gate"]["enum"]:
            self.assertIn(f"`{gate}`", text, gate)

    def test_validator_matches_the_data_schemas_of_the_content_contract(self):
        for name, file in (("question", "questions.json"), ("card", "cards.json"), ("speak", "speak.json"), ("task", "tasks.json")):
            self.assertEqual(schemas.validate(load(FIX / "data" / "99-sample" / file), name), [], name)
        item = load(FIX / "data" / "99-sample" / "questions.json")["items"][0]
        self.assertEqual(schemas.validate(item, "question", "question"), [])


class FixtureAgainstSchemas(unittest.TestCase):
    def test_facts(self):
        rows = facts()
        self.assertEqual(len(rows), 7)
        for fact in rows:
            self.assertEqual(schemas.validate(fact, "fact"), [], fact["id"])

    def test_votes_and_requests(self):
        for vote in common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl"):
            self.assertEqual(schemas.validate(vote, "vote"), [], vote["fact"])
        for request in common.read_jsonl(FIX / "_build" / "facts" / "requests.jsonl"):
            self.assertEqual(schemas.validate(request, "fact-request"), [], request["id"])

    def test_registry_files(self):
        self.assertEqual(schemas.validate(load(FIX / "data" / "book.json"), "book"), [])
        self.assertEqual(schemas.validate(load(REAL / "_build" / "registry" / "book.seed.json"), "book"), [])
        self.assertEqual(schemas.validate(load(FIX / "_build" / "registry" / "exam-guide.json"), "exam-guide"), [])
        self.assertEqual(schemas.validate(load(FIX / "_build" / "registry" / "services.json"), "services"), [])

    def test_ledger_and_gate(self):
        self.assertEqual(schemas.validate(load(FIX / "_build" / "ledger" / "chapters" / "99.json"), "ledger-chapter"), [])
        gate = load(FIX / "_build" / "ledger" / "gates" / "99.facts-final.json")
        self.assertEqual(schemas.validate(gate, "gate"), [])
        for item in gate["inputs"]:
            self.assertEqual(common.sha256_file(FIX / item["path"]), item["sha256"], item["path"])

    def test_mock_manifest_example(self):
        mock = {"v": 1, "mock": "mock-exam-1", "chapter": "50", "seed": 20261054, "assembled": "2026-10-20", "minutes": 130,
                "domain_split": [20, 17, 15, 13], "questions": [f"mock-exam-1-q{n:03d}" for n in range(1, 66)],
                "spares": ["mock-exam-1-q066"], "counts": {"domains": {"1": 20, "2": 17, "3": 15, "4": 13}, "tasks": {"1.1": 6},
                                                           "multi": 8, "difficulty": {"1": 13, "2": 36, "3": 16}, "services": {"vpc": 4}}}
        self.assertEqual(schemas.validate(mock, "mock"), [])
        mock["questions"].append("mock-exam-1-q001")
        self.assertTrue(schemas.validate(mock, "mock"))

    def test_feed_rows_as_documented_in_tools_feeds(self):
        whatsnew = {"date": "2025-11-19", "title": "Regional NAT gateways", "summary": "text", "url": "https://aws.amazon.com/about-aws/whats-new/2025/11/x/",
                    "source": "whatsnew", "service": "vpc", "id": "whats-new-v2#abc", "tag": "amazon-vpc", "product_tags": ["amazon-vpc"],
                    "text": "whole text", "api_source_id": "api/whats-new-v2-amazon-vpc-s1000-p0"}
        history = {"date": "2025-11-21", "title": "Change", "summary": "Description", "url": "https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.html",
                   "source": "history", "service": "vpc", "link": "", "date_text": "November 21, 2025", "date_precision": "day",
                   "history_source_id": "docs/vpc/latest/userguide/WhatsNew", "line": 12, "quote": "| Change | Description | November 21, 2025 |",
                   "table_header": "| Change | Description | Date |"}
        case = {"id": "customer-references#1", "title": "Freecharge", "customer": "Freecharge", "url": "https://aws.amazon.com/solutions/case-studies/freecharge-in/",
                "date": "2023-12-17", "tags": ["dynamodb"], "tag_names": ["Amazon DynamoDB"], "summary": "text", "segments": ["startup"],
                "industry": "Financial Services", "location": "India", "content_type": "case-study", "languages": ["English"], "english": True,
                "fetchable": True, "source": "customer-references", "api_source_id": "api/customer-references-dynamodb-s250-p0"}
        self.assertEqual(schemas.validate(whatsnew, "change-item"), [])
        self.assertEqual(schemas.validate(history, "change-item"), [])
        self.assertEqual(schemas.validate(case, "case-item"), [])

    def test_must_fail_bad_inputs(self):
        fact = facts()[0]
        bad = copy.deepcopy(fact)
        bad["status"] = "approved"
        self.assertTrue(any("not in enum" in e for e in schemas.validate(bad, "fact")))
        bad = copy.deepcopy(fact)
        bad["value"] = "500"
        self.assertTrue(any("unknown key value" in e for e in schemas.validate(bad, "fact")))
        bad = copy.deepcopy(fact)
        bad["evidence"][0]["url"] = "https://example.com/limits.html"
        self.assertTrue(schemas.validate(bad, "fact"))
        bad = copy.deepcopy(fact)
        bad["evidence"] = []
        self.assertTrue(schemas.validate(bad, "fact"))
        vote = common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl")[0]
        vote["verdict"] = "yes"
        self.assertTrue(schemas.validate(vote, "vote"))
        ledger = load(FIX / "_build" / "ledger" / "chapters" / "99.json")
        ledger["stages"]["render"] = ledger["stages"]["plan"]
        self.assertTrue(any("unknown key render" in e for e in schemas.validate(ledger, "ledger-chapter")))
        ledger = load(FIX / "_build" / "ledger" / "chapters" / "99.json")
        ledger["stages"]["plan"]["attempts"] = 4
        self.assertTrue(schemas.validate(ledger, "ledger-chapter"))
        book = load(FIX / "data" / "book.json")
        book["chapters"][0]["wave"] = "W16"
        self.assertTrue(schemas.validate(book, "book"))
        gate = load(FIX / "_build" / "ledger" / "gates" / "99.facts-final.json")
        gate["errors"] = [{"code": "m5", "msg": "wrong number"}]
        self.assertTrue(schemas.validate(gate, "gate"))
        request = common.read_jsonl(FIX / "_build" / "facts" / "requests.jsonl")[0]
        request["status"] = "done"
        self.assertTrue(schemas.validate(request, "fact-request"))


class FixtureFactsObeyTheMechanicalRules(unittest.TestCase):
    """A light version of M2 to M12 of TOOLS.md section 5.2, enough to keep the fixture honest."""

    def setUp(self):
        self.facts = facts()
        self.spec = load(FIX / "_build" / "style" / "SPEC.json")
        self.book = load(FIX / "data" / "book.json")

    def text(self, source_id):
        return (FIX / "_build" / "corpus" / "snap" / (source_id + ".txt")).read_text(encoding="utf-8")

    def test_m1_namespace_and_home(self):
        keys = {s: ch["id"] for ch in self.book["chapters"] for s in ch["services"]}
        for fact in self.facts:
            self.assertTrue(fact["id"].startswith(fact["service"] + "-"))
            self.assertEqual(keys[fact["service"]], fact["home_chapter"])

    def test_m2_m3_m4_evidence(self):
        for fact in self.facts:
            for ev in fact["evidence"]:
                page = FIX / "_build" / "corpus" / "snap" / (ev["source_id"] + ".txt")
                self.assertEqual(common.sha256_file(page), ev["sha256"])
                self.assertEqual(load(page.with_name(page.stem + ".meta.json"))["url"], ev["url"])
                text = page.read_text(encoding="utf-8")
                self.assertIsNotNone(common.find_quote(ev["quote"], text), fact["id"])
                if ev["quote"].lstrip().startswith("|"):
                    self.assertIsNotNone(ev["table_header"], fact["id"])
                    self.assertIsNotNone(common.find_quote(ev["table_header"], text))
                    self.assertEqual(ev["quote"].count("|"), ev["table_header"].count("|"))
                else:
                    self.assertTrue(8 <= len(words(ev["quote"])) <= 80, f"{fact['id']}: {len(words(ev['quote']))} words")

    def test_m5_numbers_are_literal_in_a_quote(self):
        for fact in self.facts:
            quoted = numbers(" ".join(ev["quote"] + " " + (ev["table_header"] or "") for ev in fact["evidence"]))
            claimed = numbers(fact["claim"]) | numbers(" ".join(v["display"] for v in fact["values"]))
            if fact["changed"]:
                claimed |= numbers(fact["changed"]["was"])
            self.assertTrue(claimed <= quoted, f"{fact['id']}: {sorted(claimed - quoted)} not in a quote")

    def test_must_fail_m5_a_claim_number_that_no_quote_holds(self):
        fact = copy.deepcopy(self.facts[0])
        fact["claim"] = fact["claim"].replace("500", "5,000")
        quoted = numbers(" ".join(ev["quote"] for ev in fact["evidence"]))
        self.assertFalse(numbers(fact["claim"]) <= quoted)

    def test_m6_m7_m9_m10_m11(self):
        absolute = self.spec["lint"]["absolute_words"]
        hard_kinds = {"limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy"}
        for fact in self.facts:
            if fact["kind"] in ("limit", "quota", "default"):
                self.assertTrue(fact["qualifiers"]["scope"] and fact["qualifiers"]["default_or_max"], fact["id"])
            haystack = [common.normalize_text(fact["claim"])] + [common.normalize_text(ev["quote"]) for ev in fact["evidence"]]
            shown = [common.normalize_text(v["display"]) for v in fact["values"]]
            self.assertEqual(len(shown), len(set(shown)))
            for display in shown:
                self.assertTrue(any(display in h for h in haystack), f"{fact['id']}: {display!r}")
            if fact["changed"]:
                self.assertLess(fact["changed"]["was_evidence"], len(fact["evidence"]))
                self.assertNotEqual(fact["volatility"], "stable")
            else:
                self.assertNotEqual(fact["volatility"], "changed-since-2022")
            self.assertEqual(fact["source_tier"] == 4, fact["kind"] == "case-study")
            claim = fact["claim"].lower()
            must_be_hard = fact["kind"] in hard_kinds or any(re.search(rf"\b{re.escape(w)}\b", claim) for w in absolute)
            if must_be_hard:
                self.assertTrue(fact["hard"], fact["id"])

    def test_m12_no_conflict_between_fixture_facts(self):
        def tokens(claim):
            return set(re.findall(r"[a-z]+", NUMBER.sub(" ", claim.lower())))
        for i, a in enumerate(self.facts):
            for b in self.facts[i + 1:]:
                ta, tb = tokens(a["claim"]), tokens(b["claim"])
                similar = len(ta & tb) / len(ta | tb) >= 0.6
                self.assertFalse(similar and numbers(a["claim"]) != numbers(b["claim"]), f"{a['id']} / {b['id']}")

    def test_votes_make_every_fact_verified_by_the_finalize_rules(self):
        votes = common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl")
        for fact in self.facts:
            required = set()
            if fact["hard"]:
                required.add("entail")
            if fact["changed"] or fact.get("change_items") or fact["volatility"] != "stable":
                required.add("currency")
            if fact.get("derivation"):
                required.add("derive")
            mine = [v for v in votes if v["fact"] == fact["id"] and v["rev"] == fact["rev"]]
            self.assertTrue(all(v["verdict"] == POSITIVE[v["lens"]] for v in mine), fact["id"])
            self.assertTrue(required <= {v["lens"] for v in mine}, f"{fact['id']}: missing {required - {v['lens'] for v in mine}}")
            self.assertEqual(fact["status"], "verified")
            self.assertEqual({(v["lens"], v["verdict"]) for v in fact["votes"]}, {(v["lens"], v["verdict"]) for v in mine})
            for vote in mine:
                if vote["quote"]:
                    self.assertIsNotNone(common.find_quote(vote["quote"], self.text(vote["source_id"])))

    def test_must_fail_a_changed_fact_without_a_currency_vote_is_not_verified(self):
        votes = [v for v in common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl") if v["lens"] != "currency"]
        fact = self.facts[0]
        self.assertIsNotNone(fact["changed"])
        self.assertNotIn("currency", {v["lens"] for v in votes if v["fact"] == fact["id"]})


class FixtureExamGuide(unittest.TestCase):
    """The expected output of `registry build --offline` must follow the parse rules of TOOLS.md 4.1."""

    def setUp(self):
        self.guide = load(FIX / "_build" / "registry" / "exam-guide.json")
        self.services = load(FIX / "_build" / "registry" / "services.json")
        self.index = load(FIX / "_build" / "corpus" / "index" / "fixture-exam-guide.json")

    def lines(self, source_id):
        return (FIX / "_build" / "corpus" / "snap" / (source_id + ".txt")).read_text(encoding="utf-8").splitlines()

    def test_pages_are_the_index_pages_with_their_hashes(self):
        self.assertEqual([p["source_id"] for p in self.guide["pages"]], [p["source_id"] for p in self.index["pages"]])
        self.assertEqual(load(FIX / "data" / "book.json")["book"]["exam_guide"]["guide_id"], self.index["guide_id"])
        for page in self.guide["pages"]:
            path = FIX / "_build" / "corpus" / "snap" / (page["source_id"] + ".txt")
            self.assertEqual(common.sha256_file(path), page["sha256"])
            meta = load(path.with_name(path.stem + ".meta.json"))
            self.assertEqual((meta["url"], meta["sha256"]), (page["url"], page["sha256"]))

    def test_tasks_and_bullets_are_verbatim_at_their_lines(self):
        for task in self.guide["tasks"]:
            self.assertEqual(self.lines(task["source_id"])[task["line"] - 1], f"## Task {task['id']}: {task['title']}")
        seen = {}
        for bullet in self.guide["bullets"]:
            self.assertEqual(self.lines(bullet["source_id"])[bullet["line"] - 1], "+ " + bullet["text"])
            letter = "K" if bullet["kind"] == "knowledge" else "S"
            seen[(bullet["task"], letter)] = seen.get((bullet["task"], letter), 0) + 1
            self.assertEqual(bullet["id"], f"{bullet['task']}.{letter}{seen[(bullet['task'], letter)]}")
            self.assertEqual(bullet["n"], seen[(bullet["task"], letter)])
            self.assertEqual(str(bullet["domain"]), bullet["task"][0])
        counted = sum(1 for p in self.guide["pages"] if p["role"] == "domain" for line in self.lines(p["source_id"])
                      if line.startswith("+ ") and not line.startswith("+ ["))
        self.assertEqual(counted, len(self.guide["bullets"]))
        self.assertEqual(self.guide["counts"], {"domains": 4, "tasks": len(self.guide["tasks"]), "bullets": len(self.guide["bullets"])})

    def test_domain_weights_come_from_the_overview_page(self):
        overview = "\n".join(self.lines("docs/fixture/exam-guide/overview"))
        found = {int(n): (title, int(w)) for n, title, w in re.findall(r"Content Domain (\d): (.+?) \((\d+)% of scored content\)", overview)}
        self.assertEqual(found, {d["id"]: (d["title"], d["weight"]) for d in self.guide["domains"]})
        self.assertEqual(sum(d["weight"] for d in self.guide["domains"]), 100)

    def test_services(self):
        book = load(FIX / "data" / "book.json")
        for entry in self.services["in_scope"] + self.services["out_of_scope"]:
            self.assertEqual(self.lines(entry["source_id"])[entry["line"] - 1], "+ " + entry["official_name"])
            self.assertEqual(entry["id"], common.slugify(entry["official_name"]))
        for entry in self.services["in_scope"]:
            self.assertEqual(entry["keys"], book["service_map"][entry["official_name"]])
            self.assertEqual(entry["home_chapter"], "99")
        self.assertEqual(self.services["counts"], {"in_scope": 3, "in_scope_unique": 2, "out_of_scope": 1, "unmapped": 0})

    def test_fixture_chapter_holds_every_bullet(self):
        chapter = load(FIX / "data" / "book.json")["chapters"][0]
        self.assertEqual(chapter["bullets"], [b["id"] for b in self.guide["bullets"]])
        self.assertEqual(chapter["tasks"], [t["id"] for t in self.guide["tasks"]])
        demand = load(FIX / "_build" / "work" / "99-sample" / "brief.v0.json")["demand"]
        self.assertEqual({d["bullet"] for d in demand}, set(chapter["bullets"]))
        questions = load(FIX / "data" / "99-sample" / "questions.json")["items"]
        for q in questions:
            self.assertIn(q["task"], chapter["tasks"], q["id"])

    def test_must_fail_weights_that_do_not_add_up(self):
        weights = [d["weight"] for d in self.guide["domains"]]
        weights[0] -= 1
        self.assertNotEqual(sum(weights), 100)


class SandboxHelper(unittest.TestCase):
    def test_make_run_and_paths(self):
        book = sandbox.make("contract-tools-sandbox")
        try:
            self.assertTrue((book / "data" / "book.json").exists())
            code, out, err = sandbox.run(book, "ping")
            self.assertEqual(code, 0, err)
            self.assertIn(str(book), out)
            real = common.DATA
            with sandbox.paths(book):
                self.assertEqual(common.DATA, book.resolve() / "data")
                self.assertEqual(common.load_book()["book"]["fixture"], True)
                self.assertEqual(schemas.validate(common.read_jsonl(common.FACTS_DIR / "widget.jsonl")[0], "fact"), [])
            self.assertEqual(common.DATA, real)
        finally:
            sandbox.remove(book)
        self.assertFalse(book.exists())

    def test_must_fail_book_dir_outside_the_book(self):
        code, out, err = sandbox.run(common.REPO, "ping")
        self.assertEqual(code, 4)


class DocumentSize(unittest.TestCase):
    def count(self, name):
        text = (REAL / "_build" / "style" / name).read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        text = re.sub(r"\]\([^)]*\)", "]", text)
        return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))

    def test_tools_documents_are_within_their_budgets(self):
        """Tokens that hold a letter or digit, code blocks removed (inline JSON counts, so this runs above a word count)."""
        self.assertLessEqual(self.count("TOOLS.md"), 7400, self.count("TOOLS.md"))
        self.assertLessEqual(self.count("TOOLS-items.md"), 4800, self.count("TOOLS-items.md"))

    def test_part_two_holds_the_sections_that_tools_md_points_to(self):
        hub = (REAL / "_build" / "style" / "TOOLS.md").read_text(encoding="utf-8")
        part = (REAL / "_build" / "style" / "TOOLS-items.md").read_text(encoding="utf-8")
        self.assertIn("TOOLS-items.md", hub)
        for heading in ("## 6.2 `sync", "## 7. Question bank", "## 8. Tasks"):
            self.assertIn(heading, part)
        for name in ("q", "cards", "speak", "mocks", "drills", "tasks", "sync", "lint", "facts", "audit", "freshen",
                     "registry", "coverage", "stage", "gate", "status", "report", "selftest"):
            self.assertIn(f"`{name}`", hub, name)


if __name__ == "__main__":
    unittest.main()
