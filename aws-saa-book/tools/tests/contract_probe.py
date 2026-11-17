#!/usr/bin/env python3
"""Read-only probe used by the contract critique (implementer lens).

    python3 aws-saa-book/tools/tests/contract_probe.py

Parses every JSON and JSONL contract file, validates the fixture and the seeds against the
schemas, and tries a few TOOLS.md rules on the unchanged fixture. It writes nothing.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from saalib import common, schemas  # noqa: E402

REAL = common.REAL_BOOK
FIX = common.FIXTURES / "book"
out = []


def say(*parts):
    out.append(" ".join(str(p) for p in parts))


def words(text):
    return len([t for t in text.split() if re.search(r"[A-Za-z0-9]", t)])


# ---------------------------------------------------------------- 1. every JSON file parses
roots = [REAL / "_build" / "schemas", REAL / "_build" / "style", REAL / "_build" / "registry", REAL / "data",
         REAL / "diagrams" / "src", common.FIXTURES]
bad = 0
count = 0
for root in roots:
    for path in sorted(root.rglob("*")):
        if path.suffix == ".json":
            count += 1
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001
                bad += 1
                say("PARSE FAIL", common.rel(path), exc)
        elif path.suffix == ".jsonl":
            count += 1
            for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if line.strip():
                    try:
                        json.loads(line)
                    except Exception as exc:  # noqa: BLE001
                        bad += 1
                        say("PARSE FAIL", common.rel(path), n, exc)
say(f"1. parsed {count} JSON/JSONL files, {bad} failures")

# ---------------------------------------------------------------- 2. schema validation
def v(label, obj, name, definition=None):
    try:
        errors = schemas.validate(obj, name, definition)
    except Exception as exc:  # noqa: BLE001
        errors = [f"validator raised {exc!r}"]
    say(f"2. {label} vs {name}: {'ok' if not errors else errors[:6]}")


v("seed book", common.read_json(REAL / "_build" / "registry" / "book.seed.json"), "book")
v("fixture book.json", common.read_json(FIX / "data" / "book.json"), "book")
v("fixture questions", common.read_json(FIX / "data" / "99-sample" / "questions.json"), "question")
v("fixture cards", common.read_json(FIX / "data" / "99-sample" / "cards.json"), "card")
v("fixture speak", common.read_json(FIX / "data" / "99-sample" / "speak.json"), "speak")
v("fixture tasks", common.read_json(FIX / "data" / "99-sample" / "tasks.json"), "task")
v("fixture terms", common.read_json(FIX / "data" / "terms.json"), "terms")
v("real terms", common.read_json(REAL / "data" / "terms.json"), "terms")
v("real exam-english", common.read_json(REAL / "data" / "exam-english.json"), "exam-english")
for i, fact in enumerate(common.read_jsonl(FIX / "data" / "facts" / "widget.jsonl")):
    errors = schemas.validate(fact, "fact")
    if errors:
        say("2. fixture fact", fact.get("id"), errors[:4])
say("2. fixture facts checked")
for row in common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl"):
    errors = schemas.validate(row, "vote")
    if errors:
        say("2. fixture vote", row.get("fact"), errors[:4])
say("2. fixture votes checked")
for row in common.read_jsonl(FIX / "_build" / "facts" / "requests.jsonl"):
    errors = schemas.validate(row, "fact-request")
    if errors:
        say("2. fixture request", row.get("id"), errors[:4])
say("2. fixture requests checked")
v("fixture ledger", common.read_json(FIX / "_build" / "ledger" / "chapters" / "99.json"), "ledger-chapter")
v("fixture gate", common.read_json(FIX / "_build" / "ledger" / "gates" / "99.facts-final.json"), "gate")
v("fixture exam-guide", common.read_json(FIX / "_build" / "registry" / "exam-guide.json"), "exam-guide")
v("fixture services", common.read_json(FIX / "_build" / "registry" / "services.json"), "services")
feeds = common.FIXTURES / "feeds"
for name, schema in (("whatsnew.json", "change-item"), ("cases.json", "case-item")):
    data = common.read_json(feeds / name)
    say(f"2. feeds/{name}: top-level {type(data).__name__}; keys {list(data)[:6] if isinstance(data, dict) else len(data)}")

# schema keyword subset, all schemas
allowed = set(common.read_json(REAL / "_build" / "style" / "SPEC.json")["data_files"]["schema_keywords_used"])


def keywords(node, found, inside_props=False):
    if isinstance(node, dict):
        for key, sub in node.items():
            if inside_props:
                keywords(sub, found)
                continue
            found.add(key)
            if key in ("properties", "$defs"):
                keywords(sub, found, True)
            elif key == "items":
                keywords(sub, found)
    return found


for path in sorted((REAL / "_build" / "schemas").glob("*.schema.json")):
    used = keywords(common.read_json(path), set())
    extra = sorted(used - allowed)
    if extra:
        say("2. schema uses undeclared keywords:", path.name, extra)
say("2. schema keyword subset checked")

# nullable + pattern: does the validator accept null where a pattern is set?
say("2. null with pattern accepted:", schemas.check(None, {"type": ["string", "null"], "pattern": "^a$"}, {}) == [])

# ---------------------------------------------------------------- 3. terms: glossary anchor equals id
def anchor(text):
    return re.sub(r"[^a-z0-9 -]", "", text.lower()).replace(" ", "-")


terms = common.read_json(REAL / "data" / "terms.json")["terms"]
mismatch = [(t["id"], t["term"], anchor(t["term"])) for t in terms if anchor(t["term"]) != t["id"]]
say(f"3. real terms: {len(terms)}; '### <term>' anchor differs from id for {len(mismatch)}:", mismatch[:12])
dups = {}
for t in terms:
    dups.setdefault(anchor(t["term"]), []).append(t["id"])
say("3. duplicate term anchors:", {k: v2 for k, v2 in dups.items() if len(v2) > 1})
heading_re = re.compile(common.read_json(REAL / "_build" / "style" / "SPEC.json")["headings"]["h2_h3_regex"])
say("3. terms whose text is not a legal H3:", [t["term"] for t in terms if not heading_re.match(t["term"])][:15])

# ---------------------------------------------------------------- 4. banned words and term variants in the fixture
real_spec = common.read_json(REAL / "_build" / "style" / "SPEC.json")
fix_spec = common.read_json(FIX / "_build" / "style" / "SPEC.json")
say("4. fixture SPEC banned_words equal real:", fix_spec["lint"]["banned_words"] == real_spec["lint"]["banned_words"],
    "| absolute:", fix_spec["lint"]["absolute_words"] == real_spec["lint"]["absolute_words"])
say("4. fixture count_nouns:", fix_spec["lint"]["number_with_unit"]["count_nouns"])
say("4. fixture units equal real:", fix_spec["lint"]["number_with_unit"]["units"] == real_spec["lint"]["number_with_unit"]["units"])
texts = {name: (FIX / "99-sample" / name).read_text(encoding="utf-8") for name in ("1-fast.md", "2-deep.md")}
for name in ("questions.json", "cards.json", "speak.json", "tasks.json"):
    texts[name] = (FIX / "data" / "99-sample" / name).read_text(encoding="utf-8")
for name, text in texts.items():
    for lineno, line in enumerate(text.splitlines(), 1):
        for word in list(fix_spec["lint"]["banned_words"]) + list(fix_spec["lint"]["warn_words"]):
            if re.search(r"(?<![A-Za-z0-9-])" + re.escape(word) + r"(?![A-Za-z0-9-])", line, re.I):
                kind = "banned" if word in fix_spec["lint"]["banned_words"] else "warn"
                say(f"4. {kind} word {word!r} in {name}:{lineno}: {line.strip()[:90]}")
fix_terms = common.read_json(FIX / "data" / "terms.json")["terms"]
for name, text in texts.items():
    for lineno, line in enumerate(text.splitlines(), 1):
        for t in fix_terms:
            for variant in t["banned"]:
                if re.search(r"\b" + re.escape(variant) + r"\b", line, re.I):
                    say(f"4. banned variant {variant!r} (term {t['id']}) in {name}:{lineno}: {line.strip()[:90]}")

# ---------------------------------------------------------------- 5. item word ranges against the fixture SPEC
q = fix_spec["questions"]
say("5. fixture SPEC stem/option/explanation/total:", q["stem_words"], q["option_words"], q["option_words_difficulty_1"],
    q["explanation_words"], q["why_words"], q["twin_words"], q["takeaway_words"], q["explanation_total_words"], q["worked_words"])
for item in common.read_json(FIX / "data" / "99-sample" / "questions.json")["items"]:
    lens = [words(o["text"]) for o in item["options"]]
    mean = sum(lens) / len(lens)
    spread = max(abs(n - mean) / mean for n in lens)
    total = words(item["explanation"]) + sum(words(o["why"]) for o in item["options"]) + words(item["twin"])
    total_wrong_only = words(item["explanation"]) + sum(words(o["why"]) for o in item["options"] if not o["correct"]) + words(item["twin"])
    worked = sum(words(s) for s in item["worked"]["steps"]) if item.get("worked") else None
    say(f"5. {item['id']}: stem {words(item['stem'])}, options {lens} mean {mean:.1f} spread {spread:.2f}, explanation {words(item['explanation'])},"
        f" whys {[words(o['why']) for o in item['options']]}, twin {words(item['twin'])}, takeaway {words(item['takeaway'])},"
        f" total {total} (wrong whys only {total_wrong_only}), worked {worked}")
s = fix_spec["speak"]
sp = common.read_json(FIX / "data" / "99-sample" / "speak.json")["items"][0]
say("5. speak: SPEC words", s["sixty_second_words"], "lines", s["sixty_second_lines"], "| item words",
    words(" ".join(sp["sixty_second"])), "lines", len(sp["sixty_second"]), "ten", words(sp["ten_second"]))
say("5. speak digits-in-names regex on 'Route 53', 'S3', 'gp3', 'IPv4', 'EC2':",
    [bool(re.fullmatch(s["digits_allowed_inside_names_regex"], w)) for w in ("Route 53", "S3", "gp3", "IPv4", "EC2")])
say("5. fixture counts:", json.dumps(fix_spec["templates"]["deep"]["counts"]))
say("5. fixture tasks SPEC:", json.dumps(fix_spec["tasks"]["types"]), json.dumps(fix_spec["tasks"]["steps"]))
say("5. fixture cards SPEC back/front:", fix_spec["cards"]["back_words_max"], fix_spec["cards"]["front_words_max"])

# ---------------------------------------------------------------- 6. facts: M4, M5, M7, M12 and vote quotes on the fixture
facts = common.read_jsonl(FIX / "data" / "facts" / "widget.jsonl")
snap = FIX / "_build" / "corpus" / "snap"
for fact in facts:
    for ev in fact["evidence"]:
        n = words(ev["quote"])
        if not ev["quote"].startswith("|") and not 8 <= n <= 80:
            say(f"6. M4 {fact['id']}: quote has {n} words")
    quotes = " ".join((ev["quote"] + " " + (ev["table_header"] or "")) for ev in fact["evidence"])
    for number in re.findall(r"\d[\d,]*(?:\.\d+)?", fact["claim"]):
        if number.replace(",", "") not in quotes.replace(",", ""):
            say(f"6. M5 {fact['id']}: claim number {number} is in no quote")
    for value in fact["values"]:
        d = common.normalize_text(value["display"])
        if d not in common.normalize_text(fact["claim"]) and not any(d in common.normalize_text(ev["quote"]) for ev in fact["evidence"]):
            say(f"6. M7 {fact['id']}: display {value['display']!r} is in neither claim nor quote")
    say(f"6. {fact['id']}: question={fact.get('question')!r} author={fact.get('author')!r} hard={fact['hard']} kind={fact['kind']}")


def tokens(claim):
    return {t for t in re.findall(r"[a-z]+", re.sub(r"\S*\d\S*", " ", claim.lower()))}


for i, a in enumerate(facts):
    for b in facts[i + 1:]:
        ta, tb = tokens(a["claim"]), tokens(b["claim"])
        j = len(ta & tb) / len(ta | tb)
        if j >= 0.4:
            say(f"6. M12 jaccard {j:.2f}: {a['id']} / {b['id']}")
for row in common.read_jsonl(FIX / "_build" / "facts" / "votes" / "widget.jsonl"):
    if row.get("quote"):
        page = (snap / (row["source_id"] + ".txt")).read_text(encoding="utf-8")
        say("6. vote quote found in snapshot:", row["fact"], common.find_quote(row["quote"], page) is not None)
case = [f for f in facts if f["kind"] == "case-study"][0]["evidence"][0]["quote"]
say("6. L306 case quote with outer quotes kept:", common.find_quote('"We moved our widget inventory to Amazon Widget Store and stopped running our own storage servers"', case) is not None,
    "| stripped:", common.find_quote("We moved our widget inventory to Amazon Widget Store and stopped running our own storage servers", case) is not None,
    "| CONVENTIONS D13 form with a period:", common.find_quote("We moved our widget inventory to Amazon Widget Store and stopped running our own storage servers.", case) is not None)

# ---------------------------------------------------------------- 7. tasks: create regex against real-looking commands
create = re.compile(real_spec["tasks"]["create_command_regex"])
samples = [
    "aws ec2 run-instances --launch-template LaunchTemplateName=saa-x --tag-specifications 'ResourceType=instance,Tags=[{Key=book,Value=saa},{Key=task,Value=ec2-t01}]'",
    "aws iam create-role --role-name saa-x --assume-role-policy-document file://trust.json --tags Key=book,Value=saa Key=task,Value=iam-t01",
    "aws ec2 create-tags --resources i-0abc --tags Key=book,Value=saa",
    "aws s3api put-object --bucket saa-x --key a.txt --copy-source b",
    "aws ec2 describe-instances --filters Name=tag:book,Values=saa",
    "aws resourcegroupstaggingapi get-resources --tag-filters Key=book,Values=saa",
]
for cmd in samples:
    say(f"7. creates={len(create.findall(cmd))} book=saa literal={'book=saa' in cmd} :: {cmd[:70]}")
for pat in real_spec["tasks"]["banned_command_patterns"]:
    for cmd in ("aws ec2 authorize-security-group-ingress --group-id sg-0a22b --protocol tcp --port 443 --cidr 10.0.0.0/16",
                "aws ec2 create-route --route-table-id rtb-1 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-1"):
        if re.search(pat, cmd):
            say(f"7. banned pattern {pat!r} matches harmless: {cmd[:80]}")

# ---------------------------------------------------------------- 8. SPEC internal checks
for key, tpl in real_spec["templates"].items():
    for f in tpl["files"]:
        if f["source"] == "hand" and f.get("sections"):
            total = sum(sec["words"]["max"] for sec in f["sections"] if "max" in sec["words"])
            fmax = f["words"].get("max") or max(v2["max"] for v2 in f["words"].get("by_tier", {}).values())
            req_min = sum(sec["words"].get("min", 0) for sec in f["sections"] if sec["required"])
            say(f"8. {key}/{f['name']}: file max {fmax}, file min {f['words'].get('min')}, sum of section max {total}, sum of required section min {req_min}")
ids_in_spec = {}
for key, tpl in list(real_spec["templates"].items()) + list(real_spec["chapter_overrides"].items()):
    for f in tpl.get("files", []):
        for sec in f.get("sections", []):
            if not sec["heading"].startswith("<") and anchor(sec["heading"]) != sec["key"]:
                ids_in_spec.setdefault(key, []).append(f"{sec['key']} != {anchor(sec['heading'])}")
say("8. SPEC section keys (template-internal since contract fix 1) that differ from the heading anchor (count per template):", {k: len(v2) for k, v2 in ids_in_spec.items()})
say("8. example:", ids_in_spec.get("deep", [])[:4])
ov = real_spec["chapter_overrides"]
say("8. override keys:", {k: sorted(v2) for k, v2 in ov.items()})
real_wrapper_roles = set(real_spec["roles"])
labels = [c["label"] for c in real_spec["callouts"]["labels"]]
say("8. callout labels:", labels)
say("8. regions kinds:", real_spec["generated_regions"]["kinds"])
h = re.compile(real_spec["headings"]["h2_h3_regex"])
for name in ("Amazon DocumentDB (with MongoDB compatibility)", "Amazon Keyspaces (for Apache Cassandra)", "AWS Identity and Access Management (IAM)",
             "Amazon Managed Crate Service (Amazon MCS)", "S3 Standard-IA costs less, but has a retrieval fee", "A NAT gateway's bandwidth"):
    say(f"8. heading regex accepts {name!r}: {bool(h.match(name))}")
ev = common.read_json(FIX / "_build" / "ledger" / "events.jsonl") if False else common.read_jsonl(FIX / "_build" / "ledger" / "events.jsonl")
say("8. events keys:", sorted({k for e in ev for k in e}))
print("\n".join(out))
