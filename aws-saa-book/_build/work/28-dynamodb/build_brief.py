"""Build _build/work/28-dynamodb/brief.json (brief-28) and check it against the fact canon.

Run: python3 aws-saa-book/_build/work/28-dynamodb/build_brief.py
Checks: every fact id named is verified; every "[display] (fact-id)" pair uses a display of that fact; section ids are the
lint section ids of the headings and are unique; every bullet has a section and a slot; FAQ quotes are in the evidence;
trap ids of other chapters exist; key facts of slots are not volatile; terms are bank terms.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import facts as F  # noqa: E402
from saalib import lint as LINT  # noqa: E402

FACTS = {}
for p in (ROOT / "data" / "facts").glob("*.jsonl"):
    for line in p.read_text().splitlines():
        if line.strip():
            f = json.loads(line)
            FACTS[f["id"]] = f
TERMS = {t["id"] for t in json.loads((ROOT / "data" / "terms.json").read_text())["terms"]}
EE = {x["id"] for g in json.loads((ROOT / "data" / "exam-english.json").read_text())["groups"] for x in g["items"]}
BULLETS = ["3.3.K1", "3.3.K2", "3.3.K3", "3.3.K4", "3.3.K8", "3.3.S2", "3.3.S4", "4.3.K4", "4.3.K5", "4.3.K9", "4.3.S3",
           "2.2.S2", "2.2.S5"]


def anchor(h):
    return LINT.section_id(h)


exec((HERE / "brief_data.py").read_text())  # defines BRIEF

errors, warnings = [], []
pair_re = re.compile(r"\[([^\[\]]+)\] \(([a-z0-9-]+)\)")
id_re = re.compile(r"\(((?:dynamodb|dax|lambda|vpc|vpc-endpoints|elasticache|rds|aurora|eventbridge|well-architected)-[a-z0-9-]+)[;),]")
skip = re.compile(r"^(dynamodb-(trap|t0|c0|q0|s0|hero|before|after|hot-partition|dax-read|transaction$|streams$|accelerator$)|"
                  r"aurora-trap|rds-trap|lambda-trap|vpc-trap|kms-trap|how-the-exam|lambda-function$|vpc-endpoints-$)")


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def ids_in(x):
    out = []
    for s in strings(x):
        for _d, fid in pair_re.findall(s):
            out.append(fid)
        for fid in id_re.findall(s):
            out.append(fid)
    return out


def verified(fid):
    return FACTS.get(fid, {}).get("status") == "verified"


# 0. complete the facts list of every section from its plan
for s in BRIEF["sections"]:
    named = list(s["facts"]) + [i for i in ids_in(s.get("plan", "")) if not skip.match(i)]
    seen_f, out = set(), []
    for fid in named:
        if fid not in seen_f:
            seen_f.add(fid)
            out.append(fid)
    s["facts"] = out

# 1. section ids and uniqueness (H2, H3 and the fixed H3 of the fast and numbers sections)
seen = {}
for s in BRIEF["sections"]:
    sid = anchor(s["heading"])
    if s["section"] != sid:
        errors.append(f"section id {s['section']!r} != lint section id {sid!r}")
    if sid in seen:
        errors.append(f"duplicate section id {sid}")
    seen[sid] = s["file"]
    for fid in s["facts"]:
        if not verified(fid):
            errors.append(f"section {sid}: fact {fid} not verified")
    if isinstance(s.get("plan"), dict):
        hw = len(s["heading"].split())
        if not 5 <= hw <= 14:
            errors.append(f"heading {s['heading']!r} has {hw} words")
for extra in [t["h3_section_id"] for t in BRIEF["compare_tables"]] + ["traps", "a-list", "b-list"]:
    if extra in seen:
        errors.append(f"H3 id {extra} collides with a section id")
    seen[extra] = "h3"
for t in BRIEF["compare_tables"]:
    if anchor(t["title"]) != t["h3_section_id"]:
        errors.append(f"compare table id {t['h3_section_id']} != {anchor(t['title'])}")

# 2. traps
for t in BRIEF["traps"]:
    for fid in t["facts"]:
        if not verified(fid):
            errors.append(f"trap {t['id']}: fact {fid} not verified")
if len(BRIEF["traps"]) > 13:
    errors.append("more than 13 traps")
known_traps = LINT.traps()
for tid in BRIEF["traps_from_other_chapters"]["ids"]:
    if tid not in known_traps:
        errors.append(f"other-chapter trap {tid} unknown to lint.traps()")
own = {t["id"] for t in BRIEF["traps"]}

# 3. bullets
sec_b = {b for s in BRIEF["sections"] for b in s["bullets"]}
slot_b = {q["bullet"] for q in BRIEF["question_slots"]}
for b in BULLETS:
    if b not in sec_b:
        errors.append(f"bullet {b} has no section")
    if b not in slot_b:
        warnings.append(f"bullet {b} is the primary bullet of no slot")
for b in sec_b | slot_b:
    if b not in BULLETS:
        errors.append(f"bullet {b} is not in the registry entry")

# 4. terms
for t in BRIEF["terms"]:
    if t not in TERMS:
        errors.append(f"term {t} not in data/terms.json")
for t in BRIEF["term_requests"]:
    if t["id"] in TERMS:
        warnings.append(f"term request {t['id']} already in the bank")
    for fid in t["facts"]:
        if not verified(fid):
            errors.append(f"term request {t['id']}: fact {fid} not verified")
for a in BRIEF["term_amendments"]:
    if a["id"] not in TERMS:
        errors.append(f"term amendment {a['id']} not in the bank")

# 5. every [display] (fact-id) pair, everywhere
pairs = 0
for s in strings(BRIEF):
    for disp, fid in pair_re.findall(s):
        if skip.match(fid):
            continue
        pairs += 1
        f = FACTS.get(fid)
        if not f:
            errors.append(f"unknown fact {fid} (display {disp!r})")
            continue
        if f.get("status") != "verified":
            errors.append(f"fact {fid} is {f.get('status')}")
        displays = [v["display"] for v in f.get("values") or []]
        if disp not in displays and disp.lower() not in [d.lower() for d in displays]:
            errors.append(f"display {disp!r} is not a display of {fid}: {displays}")

# 6. every fact-like token anywhere is a verified fact
named = set()


def collect(x, key=None):
    if isinstance(x, dict):
        for k, v in x.items():
            collect(v, k)
    elif isinstance(x, list):
        for v in x:
            collect(v, key)
    elif isinstance(x, str):
        if key in ("facts", "key_facts", "facts_for_steps", "facts_for_caption", "fact", "faq_alternates", "add_facts"):
            named.add(x)
        for m in id_re.findall(x):
            named.add(m)


collect(BRIEF)
for tok in sorted(named):
    if skip.match(tok):
        continue
    f = FACTS.get(tok)
    if not f:
        errors.append(f"unknown id {tok}")
    elif f.get("status") != "verified":
        errors.append(f"fact {tok} is {f.get('status')}")

# 7. FAQ quotes are in the evidence of their fact
for item in BRIEF["faq"]:
    f = FACTS.get(item["fact"], {})
    quotes = [e["quote"] for e in f.get("evidence", [])]
    if not any(item["quote"] in q for q in quotes):
        errors.append(f"FAQ {item['n']}: quote not found in the evidence of {item['fact']}: {quotes}")
    if not any(e["url"] == item["url"] for e in f.get("evidence", [])):
        errors.append(f"FAQ {item['n']}: url differs from the evidence of {item['fact']}")
    if F.is_volatile(f):
        warnings.append(f"FAQ {item['n']}: fact {item['fact']} is volatile")

# 8. volatile facts and slots
vol = sorted(i for i, f in FACTS.items() if f.get("home_chapter") == "28" and f.get("status") == "verified" and F.is_volatile(f))
BRIEF["question_plan"]["volatile_facts_never_in_explanation_or_correct_why"] = (
    "These verified chapter-28 facts are volatile (facts.is_volatile) and must never be linked in an explanation or in the why of "
    "a correct option (Q112); prose and cards can link them where a plan names them: " + ", ".join(vol) + ".")
qs = BRIEF["question_slots"]
for q in qs:
    for fid in q.get("key_facts", []):
        if fid in vol:
            errors.append(f"slot {q['id']}: key fact {fid} is volatile")
        if not verified(fid):
            errors.append(f"slot {q['id']}: key fact {fid} not verified")
    for e in q["exam_english"]:
        if e not in EE:
            errors.append(f"slot {q['id']}: unknown exam-English id {e}")
    for t in ([q.get("trap")] if q.get("trap") else []) + q.get("distractor_traps", []):
        if t not in own and t not in known_traps:
            errors.append(f"slot {q['id']}: trap {t} unknown")
    if not q["section"].split("#")[1] in seen:
        errors.append(f"slot {q['id']}: section {q['section']} not in the brief")
trap_slots = sum(1 for q in qs if q.get("trap"))
if trap_slots * 2 < len(qs):
    errors.append(f"only {trap_slots} of {len(qs)} slots on a trap")
cited = {q.get("trap") for q in qs} | {t for q in qs for t in q.get("distractor_traps", [])}
for t in BRIEF["traps"]:
    if t["id"] not in cited:
        warnings.append(f"trap {t['id']} is cited by no slot")
from collections import Counter  # noqa: E402
diff = Counter(q["difficulty"] for q in qs)
layer = Counter(q["layer"] for q in qs)
multi = sum(1 for q in qs if q["type"] == "multi")
concepts = Counter(q["concept"] for q in qs)
for c, n in concepts.items():
    if n > 2:
        errors.append(f"concept {c} used {n} times")

# 9. cards
for c in BRIEF["cards"]:
    for fid in c["facts"]:
        if not verified(fid):
            errors.append(f"card {c['id']}: fact {fid} not verified")
    if len(c["back"].split()) > 12:
        warnings.append(f"card {c['id']}: back has {len(c['back'].split())} words")
deck = Counter(c["deck"] for c in BRIEF["cards"])

# 10. tasks, speak, diagrams
for t in BRIEF["tasks"] + BRIEF["speak"]:
    if t["section"].split("#")[1] not in seen:
        errors.append(f"{t['id']}: section {t['section']} not in the brief")
    for fid in t.get("facts", []):
        if not verified(fid):
            errors.append(f"{t['id']}: fact {fid} not verified")
for d in BRIEF["diagrams"]:
    for fid in d.get("facts_for_steps", []) + d.get("facts_for_caption", []):
        if not verified(fid):
            errors.append(f"diagram {d['id']}: fact {fid} not verified")

# 11. budget
words = sum(s.get("words_all_in", 0) for s in BRIEF["sections"])
subs = [s for s in BRIEF["sections"] if isinstance(s.get("plan"), dict)]

print(json.dumps({"errors": errors, "warnings": warnings, "pairs_checked": pairs, "sections": len(BRIEF["sections"]),
                  "subsections": len(subs), "words_all_in_sum": words, "traps": len(BRIEF["traps"]), "slots": len(qs),
                  "trap_slots": trap_slots, "difficulty": diff, "layer": layer, "multi": multi, "cards": deck,
                  "volatile_ch28": len(vol), "term_requests": len(BRIEF["term_requests"])}, indent=1))
if not errors:
    out = HERE / "brief.json"
    out.write_text(json.dumps(BRIEF, indent=2, ensure_ascii=False) + "\n")
    print("wrote", out.relative_to(ROOT.parent))
