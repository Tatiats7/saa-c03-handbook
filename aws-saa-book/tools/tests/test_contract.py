"""Tests for the content contract: SPEC.json, the JSON Schemas, the vocabulary seeds and the fixture book.

Run:  python3 aws-saa-book/tools/tests/run.py contract

These tests read files only. They do not replace the lint (another module owns it); they prove that
the contract files are consistent with each other and that the fixture chapter follows the contract.
The small validator below supports exactly the schema keywords listed in SPEC.json under
data_files.schema_keywords_used, so the same subset can be reused by the real validator.
"""
import json
import re
import unittest
from pathlib import Path

from saalib import common

REAL = common.REAL_BOOK
FIX = common.FIXTURES / "book"
SCHEMAS = REAL / "_build" / "schemas"


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- minimal JSON Schema subset

_TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def _type_ok(value, name):
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, _TYPES[name])


def validate(value, schema, root, path="$"):
    """Return a list of error strings (empty when valid)."""
    errors = []
    if "$ref" in schema:
        target = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            target = target[part]
        return validate(value, target, root, path)
    if "type" in schema:
        names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_ok(value, n) for n in names):
            return [f"{path}: expected {names}, got {type(value).__name__}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in enum")
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than {schema['maxLength']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: above maximum {schema['maximum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: more than {schema['maxItems']} items")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(f"{path}: items are not unique")
        if "items" in schema:
            for i, item in enumerate(value):
                errors += validate(item, schema["items"], root, f"{path}[{i}]")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing {key}")
        props = schema.get("properties", {})
        for key, sub in value.items():
            if key in props:
                errors += validate(sub, props[key], root, f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unknown key {key}")
    return errors


def check(data, schema_name):
    schema = load(SCHEMAS / schema_name)
    return validate(data, schema, schema)


def schema_keywords(node, found):
    if isinstance(node, dict):
        for key, sub in node.items():
            found.add(key)
            if key in ("properties", "$defs"):
                for child in sub.values():
                    schema_keywords(child, found)
            elif key == "items":
                schema_keywords(sub, found)
    return found


# ---------------------------------------------------------------- Markdown helpers for the fixture

FACT_LINK = re.compile(r"\[([^\]]+)\]\(\.\./facts/([a-z0-9-]+)\.md#([a-z0-9-]+)\)")


def strip_front_matter(text):
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        return text[end + 5:]
    return text


def count_words(text):
    text = strip_front_matter(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    return sum(1 for tok in text.split() if re.search(r"[A-Za-z0-9]", tok))


def h2_sections(text):
    """[(heading without time box, minutes in heading, flag line)]"""
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            m = re.match(r"^## (.*?)(?: \((\d+) min\))?$", line)
            out.append((m.group(1), m.group(2), lines[i + 1] if i + 1 < len(lines) else ""))
    return out


def fixture_facts():
    return {f["id"]: f for f in common.read_jsonl(FIX / "data" / "facts" / "widget.jsonl")}


class SpecFiles(unittest.TestCase):
    def setUp(self):
        self.real = load(REAL / "_build" / "style" / "SPEC.json")
        self.fix = load(FIX / "_build" / "style" / "SPEC.json")

    def test_version(self):
        self.assertEqual(self.real["version"], "1.0")
        self.assertEqual(self.fix["version"], "1.0")

    def test_every_template_exists(self):
        self.assertEqual(set(self.real["templates"]), {"deep", "medium", "light", "front", "pattern", "synthesis", "mock"})

    def test_every_seed_chapter_resolves_to_a_template(self):
        seed = load(REAL / "_build" / "registry" / "book.seed.json")
        for ch in seed["chapters"]:
            key = ch.get("kind") or ch["tier"]
            self.assertIn(key, self.real["templates"], ch["id"])
            if key in ("front", "synthesis"):
                self.assertIn(ch["id"], self.real["chapter_overrides"], f"chapter {ch['id']} needs an override")

    def test_sections_are_complete(self):
        need = {"key", "heading", "role", "required", "route", "words"}
        specs = [t for t in self.real["templates"].values()] + [o for o in self.real["chapter_overrides"].values()]
        for spec in specs:
            for f in spec.get("files", []):
                self.assertIn(f["source"], ("hand", "generated"))
                for s in f.get("sections", []):
                    self.assertTrue(need <= set(s), f"{f['name']} section {s.get('key')}")
                    self.assertNotIn("id", s, "a template section has a `key`; the section id is the heading anchor")
                    self.assertIn(s["role"], self.real["roles"])
                    self.assertIn(s["route"], self.real["routes"])

    def test_budgets_follow_rulings(self):
        deep = {f["name"]: f for f in self.real["templates"]["deep"]["files"]}
        medium = {f["name"]: f for f in self.real["templates"]["medium"]["files"]}
        self.assertEqual(deep["1-fast.md"]["words"]["max"], 1800)
        self.assertEqual(deep["2-deep.md"]["words"], {"min": 3500, "max": 4500, "xl_max": 5500})
        self.assertEqual(medium["1-fast.md"]["words"]["max"], 1000)
        self.assertEqual(medium["2-deep.md"]["words"], {"min": 1800, "max": 2400})
        self.assertEqual(self.real["light_card"]["words"], {"min": 150, "max": 220})
        counts = self.real["templates"]
        self.assertEqual([counts[t]["counts"]["questions"]["shipped"] for t in ("deep", "medium", "light", "mock")], [18, 10, 6, 65])
        self.assertEqual([counts[t]["counts"]["speak"]["count"] for t in ("deep", "medium", "light")], [4, 2, 1])
        self.assertEqual(self.real["lint"]["absolute_words"], ["only", "always", "never", "cannot", "must", "by default", "up to", "at most", "not supported"])

    def test_fixture_spec_has_the_same_structure(self):
        def keys(node):
            return {k: keys(v) for k, v in node.items()} if isinstance(node, dict) else None

        def strip_lists(node):
            return {k: strip_lists(v) for k, v in node.items()} if isinstance(node, dict) else None

        self.assertEqual(set(self.real), set(self.fix))
        for top in self.real:
            if top in ("templates", "chapter_overrides", "about"):
                continue
            self.assertEqual(keys(self.real[top]), keys(self.fix[top]), f"structure differs under {top}")
        real_deep, fix_deep = self.real["templates"]["deep"], self.fix["templates"]["deep"]
        self.assertEqual(strip_lists(real_deep), strip_lists(fix_deep))
        for rf, ff in zip(real_deep["files"], fix_deep["files"]):
            self.assertEqual(rf["name"], ff["name"])
            self.assertEqual([s["key"] for s in rf.get("sections", [])], [s["key"] for s in ff.get("sections", [])])

    def test_table_row_limits_hold_the_required_tables(self):
        """Contract fix 1, writer finding 1: a required row count must fit the row limit of its table kind."""
        tables = self.real["tables"]
        need = {"plan_rows": "plan", "matrix_rows": "matrix", "a_list_rows": "numbers", "b_list_rows": "numbers",
                "signal_rows": "signals", "pairs_rows": "pairs", "glance_rows": "glance", "services_rows": "services"}
        specs = list(self.real["templates"].values()) + list(self.real["chapter_overrides"].values())
        seen = 0
        for spec in specs:
            for f in spec.get("files", []):
                for s in f.get("sections", []):
                    for name, count in s.get("counts", {}).items():
                        if name in need:
                            kind = tables["kinds"][need[name]]
                            limit = kind.get("rows_max", tables["rows_max"])
                            top = count["max"] if isinstance(count, dict) else count
                            self.assertLessEqual(top, limit, f"{f['name']} {s['key']} {name}")
                            seen += 1
        self.assertGreater(seen, 10)

    def test_must_fail_a_row_count_above_the_default_limit(self):
        self.assertGreater(24, self.real["tables"]["rows_max"], "24 matrix rows only fit because matrix has its own rows_max")
        self.assertEqual(self.real["tables"]["kinds"]["matrix"]["rows_max"], 24)

    def test_section_roles_and_table_kinds_of_the_fields_exist(self):
        kinds = set(self.real["tables"]["kinds"])
        for override in self.real["chapter_overrides"].values():
            for f in override.get("files", []):
                for s in f.get("sections", []):
                    for field in s.get("fields", []):
                        if field["label"].startswith("table:"):
                            self.assertIn(field["label"].split(":", 1)[1], kinds)
        self.assertEqual(self.real["startup"]["name"], self.fix["startup"]["name"])
        self.assertTrue((REAL / self.real["startup"]["fact_sheet"]).exists())

    def test_regexes_compile(self):
        for name, pattern in self.real["ids"].items():
            re.compile(pattern)
        for pattern in (self.real["section_flag"]["regex"], self.real["headings"]["h2_h3_regex"], self.real["fact_links"]["href_regex"],
                        self.real["diagram_embed"]["image_regex"], self.real["questions"]["letter_reference_regex"]):
            re.compile(pattern)
        for pattern in self.real["tasks"]["banned_command_patterns"] + self.real["code"]["banned_patterns"]:
            re.compile(pattern)


class Schemas(unittest.TestCase):
    NAMES = ["question", "card", "speak", "task", "terms", "exam-english"]

    def test_schemas_use_only_the_declared_keywords(self):
        allowed = set(load(REAL / "_build" / "style" / "SPEC.json")["data_files"]["schema_keywords_used"])
        for name in self.NAMES:
            schema = load(SCHEMAS / f"{name}.schema.json")
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            used = schema_keywords(schema, set())
            self.assertTrue(used <= allowed, f"{name}: {sorted(used - allowed)}")

    def test_fixture_data_is_valid(self):
        for name in ("question", "card", "speak", "task"):
            data = load(FIX / "data" / "99-sample" / f"{name}s.json") if name != "speak" else load(FIX / "data" / "99-sample" / "speak.json")
            self.assertEqual(check(data, f"{name}.schema.json"), [], name)
        self.assertEqual(check(load(FIX / "data" / "terms.json"), "terms.schema.json"), [])

    def test_real_seeds_are_valid(self):
        self.assertEqual(check(load(REAL / "data" / "terms.json"), "terms.schema.json"), [])
        self.assertEqual(check(load(REAL / "data" / "exam-english.json"), "exam-english.schema.json"), [])

    def test_must_fail_question_without_why(self):
        data = load(FIX / "data" / "99-sample" / "questions.json")
        del data["items"][0]["options"][1]["why"]
        self.assertTrue(any("missing why" in e for e in check(data, "question.schema.json")))

    def test_must_fail_question_with_bad_id_and_unknown_key(self):
        data = load(FIX / "data" / "99-sample" / "questions.json")
        data["items"][0]["id"] = "q-99-001"
        data["items"][0]["answer"] = "A"
        errors = check(data, "question.schema.json")
        self.assertTrue(any("does not match" in e for e in errors))
        self.assertTrue(any("unknown key answer" in e for e in errors))

    def test_must_fail_task_with_other_label(self):
        data = load(FIX / "data" / "99-sample" / "tasks.json")
        data["items"][1]["label"] = "tested in a real account"
        self.assertTrue(check(data, "task.schema.json"))

    def test_must_fail_speak_with_three_cues(self):
        data = load(FIX / "data" / "99-sample" / "speak.json")
        data["items"][0]["skeleton"].pop()
        self.assertTrue(check(data, "speak.schema.json"))

    def test_must_fail_exam_english_group_of_nine(self):
        data = load(REAL / "data" / "exam-english.json")
        data["groups"][0]["items"].pop()
        self.assertTrue(check(data, "exam-english.schema.json"))


class Seeds(unittest.TestCase):
    def test_terms(self):
        terms = load(REAL / "data" / "terms.json")["terms"]
        self.assertGreaterEqual(len(terms), 60)
        ids = [t["id"] for t in terms]
        self.assertEqual(len(ids), len(set(ids)))
        for t in terms:
            meaning = t["meaning"].replace("Route 53", "")
            self.assertFalse(re.search(r"(?<![A-Za-z])\d", meaning), f"{t['id']}: a meaning holds no numbers")
            self.assertTrue(t["collocations"], t["id"])
            anchor = re.sub(r"[^a-z0-9 -]", "", t["term"].lower()).replace(" ", "-")
            self.assertEqual(t["id"], anchor, "a term id is the GitHub anchor of its term (glossary links)")
            for variant in t["banned"] + t.get("banned_case", []):
                self.assertNotIn("(", variant, f"{t['id']}: a banned variant is literal; a condition goes to `avoid`")

    def test_must_fail_a_term_id_that_is_not_its_anchor(self):
        self.assertNotEqual("scp", re.sub(r"[^a-z0-9 -]", "", "service control policy").replace(" ", "-"))

    def test_exam_english_is_nine_groups_of_ten(self):
        groups = load(REAL / "data" / "exam-english.json")["groups"]
        self.assertEqual([len(g["items"]) for g in groups], [10] * 9)
        ids = [w["id"] for g in groups for w in g["items"]]
        self.assertEqual(len(set(ids)), 90)


class FixtureFacts(unittest.TestCase):
    def snapshot(self, source_id):
        return FIX / "_build" / "corpus" / "snap" / (source_id + ".txt")

    def test_six_facts_quote_the_limits_page_verbatim(self):
        facts = fixture_facts()
        on_limits = [f for f in facts.values() if f["evidence"][0]["source_id"] == "docs/fixture/widget-store/limits"]
        self.assertEqual(len(on_limits), 6)
        for fact in facts.values():
            self.assertRegex(fact["id"], r"^widget-[a-z0-9-]+$")
            for ev in fact["evidence"]:
                page = self.snapshot(ev["source_id"])
                self.assertEqual(common.sha256_file(page), ev["sha256"], fact["id"])
                self.assertIsNotNone(common.find_quote(ev["quote"], page.read_text(encoding="utf-8")), fact["id"])
                meta = load(page.with_suffix(".meta.json"))
                self.assertEqual(meta["url"], ev["url"])
                self.assertEqual(meta["sha256"], ev["sha256"])

    def test_must_fail_a_paraphrase_and_a_wrong_number(self):
        page = self.snapshot("docs/fixture/widget-store/limits").read_text(encoding="utf-8")
        self.assertIsNone(common.find_quote("Each shelf can hold up to 5,000 widgets.", page))
        self.assertIsNone(common.find_quote("A shelf has room for at most 500 widgets.", page))

    def test_numbers_in_display_values_appear_in_a_quote(self):
        for fact in fixture_facts().values():
            quotes = " ".join(ev["quote"] for ev in fact["evidence"])
            for value in fact["values"]:
                for number in re.findall(r"\d[\d,]*", value["display"]):
                    self.assertIn(number, quotes, f"{fact['id']}: {value['display']}")


class FixtureChapter(unittest.TestCase):
    def setUp(self):
        self.spec = load(FIX / "_build" / "style" / "SPEC.json")
        self.files = {f["name"]: f for f in self.spec["templates"]["deep"]["files"]}
        self.text = {name: (FIX / "99-sample" / name).read_text(encoding="utf-8") for name in ("1-fast.md", "2-deep.md")}
        self.facts = fixture_facts()

    def test_sections_in_order_with_flags(self):
        flag = re.compile(self.spec["section_flag"]["regex"])
        heading = re.compile(self.spec["headings"]["h2_h3_regex"])
        for name, text in self.text.items():
            want = [(s["heading"], s["role"], s["route"]) for s in self.files[name]["sections"]]
            got = []
            for title, minutes, flag_line in h2_sections(text):
                m = flag.match(flag_line)
                self.assertIsNotNone(m, f"{name}: bad flag after {title!r}: {flag_line!r}")
                self.assertEqual(m.group(3), minutes, f"{name}: minutes differ for {title!r}")
                got.append((title, m.group(1), m.group(2)))
            self.assertEqual(got, want, name)
            for line in text.splitlines():
                if line.startswith("## ") or line.startswith("### "):
                    self.assertRegex(line.split(" ", 1)[1], heading)

    def test_word_limits(self):
        for name, text in self.text.items():
            words = count_words(text)
            limits = self.files[name]["words"]
            self.assertGreaterEqual(words, limits["min"], name)
            self.assertLessEqual(words, limits["max"], name)

    def test_fast_minutes_equal_the_sum_of_time_boxes(self):
        text = self.text["1-fast.md"]
        total = sum(int(m) for _, m, _ in h2_sections(text))
        declared = int(re.search(r"minutes: \{fast: (\d+)", text).group(1))
        self.assertEqual(total, declared)

    def check_links(self, text, where):
        for label, service, fact_id in FACT_LINK.findall(text):
            self.assertIn(fact_id, self.facts, f"{where}: unknown fact {fact_id}")
            fact = self.facts[fact_id]
            self.assertEqual(fact["service"], service)
            self.assertEqual(fact["status"], "verified")
            shown = common.normalize_text(label)
            self.assertTrue(any(common.normalize_text(v["display"]) in shown for v in fact["values"]),
                            f"{where}: link text {label!r} holds no display value of {fact_id}")

    def test_fact_links_resolve_and_show_the_canonical_value(self):
        for name, text in self.text.items():
            self.assertGreater(len(FACT_LINK.findall(text)), 5)
            self.check_links(text, name)
        for name in ("questions.json", "cards.json"):
            self.check_links((FIX / "data" / "99-sample" / name).read_text(encoding="utf-8"), name)

    def test_must_fail_link_text_without_the_value(self):
        bad = "A shelf holds [many widgets](../facts/widget.md#widget-shelf-max-widgets)."
        with self.assertRaises(AssertionError):
            self.check_links(bad, "bad")

    def test_absolute_words_have_a_fact_link_in_strict_text(self):
        """A light version of the lint rule, enough to keep the fixture honest."""
        absolute = self.spec["lint"]["absolute_words"]
        exempt_roles = {r for r, v in self.spec["roles"].items() if v["grounding"] != "strict"}
        for name, text in self.text.items():
            role = None
            for block in strip_front_matter(text).split("\n\n"):
                first = block.strip().splitlines()[0] if block.strip() else ""
                if first.startswith("## "):
                    m = re.search(r"role=([a-z]+)", block)
                    role = m.group(1) if m else role
                    continue
                if role in exempt_roles or not block.strip() or block.lstrip().startswith(("```", "<!--", "<details", "<summary", "</details")):
                    continue
                for line in block.splitlines():
                    line = re.sub(r"<!--.*?-->", "", line)
                    if re.match(r"^\*\*(Predict|Check|Recap|FAQ) \d+\.\*\*|^\*\*(Stop and answer|Spot the bug|Predict the picture)\.\*\*", line):
                        continue
                    if re.match(r"^> \*\*(Startup example|Try it|Exam signal|Exam heuristic|The exam probably expects):\*\*", line):
                        continue
                    if line.startswith("> \"") or line.startswith("> — ["):
                        continue
                    line = re.sub(r"\*\*Wrong belief:\*\*.*?\*\*Truth:\*\*", "", line)
                    cells = line.split("|")[2:] if line.startswith("| \"") else [line]
                    for cell in cells:
                        for sentence in re.split(r"(?<=[.?!])\s+", cell):
                            if sentence.rstrip().endswith("?"):
                                continue
                            plain = FACT_LINK.sub(lambda m: m.group(1), sentence).lower()
                            if any(re.search(rf"\b{re.escape(w)}\b", plain) for w in absolute):
                                self.assertTrue(FACT_LINK.search(sentence), f"{name}: no fact link in: {sentence.strip()!r}")

    def test_aws_quote_blocks_match_evidence(self):
        quote = re.compile(r'^> "(.+?)"\n> — \[[^\]]+\]\((https://[^)]+)\)', re.M)
        found = quote.findall(self.text["2-deep.md"])
        self.assertEqual(len(found), 3)
        for text, url in found:
            ok = any(ev["url"] == url and common.find_quote(text, ev["quote"]) for f in self.facts.values() for ev in f["evidence"])
            self.assertTrue(ok, text)

    def test_traps_cited_by_questions_exist(self):
        traps = set(re.findall(r"<!-- trap: ([a-z0-9-]+) -->", self.text["1-fast.md"]))
        self.assertEqual(len(traps), 3)
        trap_re = re.compile(self.spec["ids"]["trap"])
        for t in traps:
            self.assertRegex(t, trap_re)
        questions = load(FIX / "data" / "99-sample" / "questions.json")["items"]
        for q in questions:
            correct = [o for o in q["options"] if o["correct"]]
            self.assertEqual(len(correct), q["select"], q["id"])
            self.assertEqual(len(q["options"]), 4 if q["type"] == "single" else 5)
            for kw in q["keywords"]:
                self.assertIn(kw, q["stem"], q["id"])
            for o in q["options"]:
                if o["correct"]:
                    continue
                self.assertTrue(o["trap"] or o["misconception"], f"{q['id']} option {o['id']}")
                if o["trap"]:
                    self.assertIn(o["trap"], traps)
        twins = [q for q in questions if q["twin_of"]]
        self.assertEqual(len(twins), 1)
        first = next(q for q in questions if q["id"] == twins[0]["twin_of"])
        self.assertNotEqual([o["id"] for o in first["options"] if o["correct"]], [o["id"] for o in twins[0]["options"] if o["correct"]])
        self.assertEqual(sum(1 for q in questions if q["type"] == "multi"), 1)

    def test_item_sections_exist(self):
        anchors = {}
        for name, text in self.text.items():
            for line in text.splitlines():
                if line.startswith("## ") or line.startswith("### "):
                    title = re.sub(r" \(\d+ min\)$", "", line.split(" ", 1)[1])
                    anchors.setdefault(name, set()).add(re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-"))
        for name in ("questions.json", "cards.json", "speak.json", "tasks.json"):
            for item in load(FIX / "data" / "99-sample" / name)["items"]:
                file, anchor = item["section"].split("#")
                self.assertIn(anchor, anchors[file], f"{item['id']}: {item['section']}")

    def test_speak_script_follows_the_four_moves(self):
        rules = self.spec["speak"]
        item = load(FIX / "data" / "99-sample" / "speak.json")["items"][0]
        script = " ".join(item["sixty_second"])
        position = -1
        for starter in rules["starters_in_order"]:
            found = script.find(starter)
            self.assertGreater(found, position, starter)
            position = found
        self.assertTrue(item["sixty_second"][-1].endswith("?"))
        self.assertLessEqual(len(item["ten_second"].split()), rules["ten_second_words_max"])
        words = len(script.split())
        self.assertTrue(rules["sixty_second_words"]["min"] <= words <= rules["sixty_second_words"]["max"], words)
        for sentence in re.split(r"(?<=[.?!])\s+", script):
            self.assertLessEqual(len(sentence.split()), rules["sentence_words_max"], sentence)
        self.assertFalse(re.search(r"\d", script))

    def test_try_task_has_cost_cleanup_verify_and_tags(self):
        tasks = {t["type"]: t for t in load(FIX / "data" / "99-sample" / "tasks.json")["items"]}
        rules = self.spec["tasks"]
        self.assertEqual(set(tasks), {"look", "try"})
        t = tasks["try"]
        self.assertTrue(t["cleanup"] and t["verify"] and t["cost"] and t["cost_if_forgotten"])
        self.assertTrue(any(s.get("break_it") for s in t["steps"]))
        create = re.compile(rules["create_command_regex"])
        created = 0
        for step in t["steps"]:
            command = step.get("command")
            if command and create.search(command.split()[2]):
                created += 1
                self.assertTrue(any(re.search(p, command) for p in rules["tag_patterns"]), command)
                self.assertTrue(any(re.search(p.replace("<task id>", t["id"]), command) for p in rules["tag_task_patterns"]), command)
            for banned in rules["banned_command_patterns"]:
                self.assertFalse(command and re.search(banned, command))
            if step.get("break_it"):
                for key in rules["break_it_step_needs"]:
                    self.assertTrue(step.get(key), key)
        self.assertEqual(created, 2)
        self.assertTrue(any(re.search(p, t["verify"]["command"]) for p in rules["verify_tag_patterns"]))
        self.assertTrue(t["pass_route"])

    def test_must_fail_real_cli_tag_syntax_against_the_literal_tag(self):
        """Contract fix 1, blocker: the literal `book=saa` is not in real AWS CLI tag syntax; the patterns must accept it."""
        rules = self.spec["tasks"]
        command = "aws iam create-role --role-name saa-demo --tags Key=book,Value=saa Key=task,Value=iam-t02"
        self.assertNotIn(rules["tag"], command)
        self.assertTrue(any(re.search(p, command) for p in rules["tag_patterns"]))
        untagged = "aws iam create-role --role-name saa-demo"
        self.assertFalse(any(re.search(p, untagged) for p in rules["tag_patterns"]))
        option = "aws ec2 run-instances --launch-template LaunchTemplateName=saa-web"
        self.assertEqual(sum(1 for word in option.split() if re.search(rules["create_command_regex"], word)), 1)


class DocumentSizes(unittest.TestCase):
    def test_contract_documents_are_within_their_budgets(self):
        style = REAL / "_build" / "style"
        self.assertLessEqual(count_words((style / "CONVENTIONS.md").read_text(encoding="utf-8")), 4900)
        self.assertLessEqual(count_words((style / "STYLE.md").read_text(encoding="utf-8")), 3000)


if __name__ == "__main__":
    unittest.main()
