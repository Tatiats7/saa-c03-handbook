"""Build _build/work/27-aurora/brief.json (brief-27) and check it against the fact canon.

Run: python3 aws-saa-book/_build/work/27-aurora/build_brief.py
Checks: every fact id named is verified; every "[display] (fact-id)" pair uses a display of that fact;
section ids are the lint anchors of the headings and are unique; every bullet has a section and a slot.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import facts as F  # noqa: E402

FACTS = {}
for p in (ROOT / "data" / "facts").glob("*.jsonl"):
    for line in p.read_text().splitlines():
        if line.strip():
            f = json.loads(line)
            FACTS[f["id"]] = f
TERMS = {t["id"] for t in json.loads((ROOT / "data" / "terms.json").read_text())["terms"]}
BULLETS = ["3.3.K1", "3.3.K7", "3.3.K8", "3.3.S1", "3.3.S2", "3.3.S4", "4.3.K7", "4.3.K8", "4.3.K9",
           "4.3.S3", "2.1.K15", "2.2.K6", "2.2.S2"]


def anchor(h):
    return "".join(c for c in h.strip().lower() if c.isalnum() or c in " -").replace(" ", "-")


exec((HERE / "brief_data.py").read_text())  # defines BRIEF

# ---------------------------------------------------------------- checks
errors, warnings = [], []
# 1. section ids and uniqueness
seen = {}
for s in BRIEF["sections"]:
    sid = anchor(s["heading"])
    if s["section"] != sid:
        errors.append(f"section id {s['section']!r} != anchor {sid!r}")
    if sid in seen:
        errors.append(f"duplicate section id {sid}")
    seen[sid] = s["file"]
    for fid in s["facts"]:
        if fid not in FACTS or FACTS[fid].get("status") != "verified":
            errors.append(f"section {sid}: fact {fid} not verified")
    if s.get("plan") and isinstance(s["plan"], dict) and s["file"] == "2-deep.md":
        hw = len(s["heading"].split())
        if not 5 <= hw <= 14:
            errors.append(f"heading {s['heading']!r} has {hw} words")
# 2. traps
for t in BRIEF["traps"]:
    for fid in t["facts"]:
        if FACTS.get(fid, {}).get("status") != "verified":
            errors.append(f"trap {t['id']}: fact {fid} not verified")
if len(BRIEF["traps"]) > 13:
    errors.append("more than 13 traps")
# 3. bullets
sec_b = {b for s in BRIEF["sections"] for b in s["bullets"]}
slot_b = {q["bullet"] for q in BRIEF["question_slots"]}
for b in BULLETS:
    if b not in sec_b:
        errors.append(f"bullet {b} has no section")
    if b not in slot_b:
        errors.append(f"bullet {b} has no question slot")
# 4. terms
for t in BRIEF["terms"]:
    if t not in TERMS:
        errors.append(f"term {t} not in data/terms.json")
# 5. every [display] (fact-id) pair, everywhere
blob = json.dumps(BRIEF, ensure_ascii=False)


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


pair_re = re.compile(r"\[([^\[\]]+)\] \(([a-z0-9-]+)\)")
pairs = 0
found_pairs = [p for s in strings(BRIEF) for p in pair_re.findall(s)]
for disp, fid in found_pairs:
    pairs += 1
    f = FACTS.get(fid)
    if not f:
        errors.append(f"unknown fact {fid} (display {disp!r})")
        continue
    if f.get("status") != "verified":
        errors.append(f"fact {fid} is {f.get('status')}")
    displays = [v["display"] for v in f.get("values") or []]
    if disp not in displays:
        errors.append(f"display {disp!r} is not a display of {fid}: {displays}")
# 6. every fact-like token anywhere is a verified fact (ids of traps, items, diagrams excluded)
skip = re.compile(r"^(aurora-(trap|t0|c0|q0|s0|hero|before|after|replica-compare)|rds-trap|how-the-exam|aws-map-trap|kms-trap|lambda-trap|dynamodb-trap|ebs-trap)")
named = set()


def collect(x, key=None):
    if isinstance(x, dict):
        for k, v in x.items():
            collect(v, k)
    elif isinstance(x, list):
        for v in x:
            collect(v, key)
    elif isinstance(x, str):
        if key in ("facts", "key_facts", "facts_for_steps", "facts_for_caption", "fact", "faq_alternates"):
            named.add(x)
        for m in re.findall(r"\(((?:aurora|rds|dynamodb|lambda)[a-z0-9-]*-[a-z0-9-]+)[;),]", x):
            named.add(m)


collect(BRIEF)
for tok in named:
    if skip.match(tok):
        continue
    f = FACTS.get(tok)
    if not f:
        errors.append(f"unknown id {tok}")
    elif f.get("status") != "verified":
        errors.append(f"fact {tok} is {f.get('status')}")
# 7. volatile facts used as question keys
vol = sorted(i for i, f in FACTS.items() if f.get("home_chapter") == "27" and f.get("status") == "verified" and F.is_volatile(f))
BRIEF["question_plan"]["volatile_facts_never_in_explanation_or_correct_why"] = (
    "These verified chapter-27 facts are volatile (facts.is_volatile) and must never be linked in an explanation or in the why of "
    "a correct option (Q112); prose and cards can link them where a plan names them: " + ", ".join(vol) + ".")
for q in BRIEF["question_slots"]:
    for fid in q.get("key_facts", []):
        if fid in vol:
            errors.append(f"slot {q['id']}: key fact {fid} is volatile")
        if FACTS.get(fid, {}).get("status") != "verified":
            errors.append(f"slot {q['id']}: key fact {fid} not verified")
# 8. counts
n = BRIEF["question_plan"]
qs = BRIEF["question_slots"]
trap_slots = sum(1 for q in qs if q.get("trap"))
if trap_slots * 2 < len(qs):
    errors.append(f"only {trap_slots} of {len(qs)} slots on a trap")
cited = {q.get("trap") for q in qs} | {t for q in qs for t in q.get("distractor_traps", [])}
for t in BRIEF["traps"]:
    if t["id"] not in cited:
        warnings.append(f"trap {t['id']} is cited by no slot")
placed = {t.get("placed_in", "") for t in BRIEF["traps"]}

print(json.dumps({"errors": errors, "warnings": warnings, "pairs_checked": pairs, "sections": len(BRIEF["sections"]),
                  "traps": len(BRIEF["traps"]), "slots": len(qs), "trap_slots": trap_slots,
                  "volatile_ch27": len(vol)}, indent=1))
if not errors:
    out = HERE / "brief.json"
    out.write_text(json.dumps(BRIEF, indent=2, ensure_ascii=False) + "\n")
    print("wrote", out.relative_to(ROOT.parent))
