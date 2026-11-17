"""Build _build/work/31-messaging/brief.json (brief-31) and check it against the fact canon.

Run: python3 aws-saa-book/_build/work/31-messaging/build_brief.py [--probe]
Checks: every fact id named is verified; every "[display] (fact-id)" pair uses a display of that fact; section ids are the
lint section ids of the headings and are unique; every bullet has a section and a slot; FAQ quotes come from the evidence;
trap ids of other chapters exist; key facts of slots are not volatile; terms are bank terms.
With --probe it only prints the evidence of the FAQ and case facts and the volatile facts of the chapter.
"""
import json
import re
import sys
from collections import Counter
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
BULLETS = ["2.1.K2", "2.1.K5", "2.1.K11", "2.1.S1", "2.1.S3", "3.2.K3", "3.2.S1", "3.2.S2", "1.1.S5"]
CH = "31"


def anchor(h):
    return LINT.section_id(h)


def verified(fid):
    return FACTS.get(fid, {}).get("status") == "verified"


VOL = sorted(i for i, f in FACTS.items() if f.get("home_chapter") == CH and f.get("status") == "verified" and F.is_volatile(f))

if "--probe" in sys.argv:
    ids = sys.argv[sys.argv.index("--probe") + 1:]
    for fid in ids:
        f = FACTS.get(fid)
        if not f:
            print("MISSING", fid)
            continue
        print(fid, f.get("status"), "volatile" if F.is_volatile(f) else "")
        for e in f.get("evidence", []):
            print("   url:", e.get("url"))
            print("   quote:", e.get("quote"))
        print("   displays:", [v.get("display") for v in f.get("values") or []])
    if not ids:
        print("volatile chapter-31 facts:", len(VOL))
        print("\n".join(VOL))
    sys.exit(0)

BRIEF = {}
for part in ("a", "b", "c", "d", "e", "f"):
    exec((HERE / f"brief_part_{part}.py").read_text())

errors, warnings = [], []
pair_re = re.compile(r"\[([^\[\]]+)\] \(([a-z0-9-]+)\)")
id_re = re.compile(r"\(((?:sqs|sns|eventbridge|lambda|ec2-auto-scaling|ecs|s3)-[a-z0-9-]+)[;),]")
skip = re.compile(r"^(messaging-|lambda-trap|s3-trap|how-the-exam|auto-scaling-trap|kms-trap|iam-trap)")


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


# 0. complete the facts list of every section from its plan
for s in BRIEF["sections"]:
    named = list(s["facts"]) + [i for i in ids_in(s.get("plan", "")) if not skip.match(i)]
    seen_f, out = set(), []
    for fid in named:
        if fid not in seen_f:
            seen_f.add(fid)
            out.append(fid)
    s["facts"] = out

# 1. section ids and uniqueness
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
            errors.append(f"section {sid}: fact {fid} not verified ({FACTS.get(fid, {}).get('status')})")
    if isinstance(s.get("plan"), dict):
        hw = len(s["heading"].split())
        if not 5 <= hw <= 14:
            errors.append(f"heading {s['heading']!r} has {hw} words")
        if not re.fullmatch(r"[A-Za-z0-9 -]+", s["heading"]):
            errors.append(f"heading {s['heading']!r} has a character a heading cannot hold")
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
    if not t["id"].startswith("messaging-trap-"):
        errors.append(f"trap {t['id']} does not start with messaging-trap-")
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
        errors.append(f"bullet {b} is the primary bullet of no slot")
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
    if t["id"] != LINT.anchor(t["term"]) and not t.get("id_note"):
        warnings.append(f"term request id {t['id']} is not the anchor of {t['term']!r} ({LINT.anchor(t['term'])})")
    for fid in t["facts"]:
        if not verified(fid):
            errors.append(f"term request {t['id']}: fact {fid} not verified")
for a in BRIEF["term_amendments"]:
    if a["id"] not in TERMS:
        errors.append(f"term amendment {a['id']} not in the bank")
    for fid in a.get("add_facts", []):
        if not verified(fid):
            errors.append(f"term amendment {a['id']}: fact {fid} not verified")

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

# 7. FAQ quotes come from the evidence of their fact (filled here when absent)
for item in BRIEF["faq"]:
    f = FACTS.get(item["fact"], {})
    ev = f.get("evidence", [])
    if not ev:
        errors.append(f"FAQ {item['n']}: no evidence for {item['fact']}")
        continue
    if not item.get("quote"):
        item["quote"] = ev[0]["quote"]
    if not item.get("url"):
        item["url"] = ev[0]["url"]
    if not any(item["quote"] in e["quote"] for e in ev):
        errors.append(f"FAQ {item['n']}: quote not in the evidence of {item['fact']}")
    if not any(e["url"] == item["url"] for e in ev):
        errors.append(f"FAQ {item['n']}: url differs from the evidence of {item['fact']}")
    if "faqs" not in item["url"]:
        warnings.append(f"FAQ {item['n']}: url {item['url']} is not a FAQ page")
    if F.is_volatile(f):
        warnings.append(f"FAQ {item['n']}: fact {item['fact']} is volatile")
    item["quote_words"] = len(item["quote"].split())

# 8. volatile facts and slots
BRIEF["question_plan"]["volatile_facts_never_in_explanation_or_correct_why"] = (
    "These verified chapter-31 facts are volatile (facts.is_volatile: a price, frequently-changing, or changed within the "
    "volatile window) and must never decide a key or be linked in an explanation or in the why of a correct option (Q112); "
    "prose, cards and Changed recently can link them where a plan names them: " + ", ".join(VOL) + ".")
qs = BRIEF["question_slots"]
ids_seen = set()
for q in qs:
    if q["id"] in ids_seen:
        errors.append(f"duplicate slot id {q['id']}")
    ids_seen.add(q["id"])
    for fid in q.get("key_facts", []):
        if fid in VOL or F.is_volatile(FACTS.get(fid, {})):
            errors.append(f"slot {q['id']}: key fact {fid} is volatile")
        if not verified(fid):
            errors.append(f"slot {q['id']}: key fact {fid} not verified")
    for e in q["exam_english"]:
        if e not in EE:
            errors.append(f"slot {q['id']}: unknown exam-English id {e}")
    for t in ([q.get("trap")] if q.get("trap") else []) + q.get("distractor_traps", []):
        if t not in own and t not in known_traps:
            errors.append(f"slot {q['id']}: trap {t} unknown")
    if q["section"].split("#")[1] not in seen:
        errors.append(f"slot {q['id']}: section {q['section']} not in the brief")
    if q["layer"] == "core" and q["difficulty"] == 3:
        errors.append(f"slot {q['id']}: a core slot has difficulty 3")
trap_slots = sum(1 for q in qs if q.get("trap"))
if trap_slots * 2 < len(qs):
    errors.append(f"only {trap_slots} of {len(qs)} slots on a trap")
cited = {q.get("trap") for q in qs} | {t for q in qs for t in q.get("distractor_traps", [])}
for t in BRIEF["traps"]:
    if t["id"] not in cited:
        errors.append(f"trap {t['id']} is cited by no slot")
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
    if len(c["facts"]) != 1:
        warnings.append(f"card {c['id']}: {len(c['facts'])} facts")
    if len(c["back"].split()) > 12:
        warnings.append(f"card {c['id']}: back has {len(c['back'].split())} words")
    if c.get("trap") and c["trap"] not in own and c["trap"] not in known_traps:
        errors.append(f"card {c['id']}: trap {c['trap']} unknown")
    if c["section"].split("#")[1] not in seen:
        errors.append(f"card {c['id']}: section {c['section']} not in the brief")
deck = Counter(c["deck"] for c in BRIEF["cards"])
a_cards = {r["card"] for r in BRIEF["numbers"]["a_list"]}
for cid in a_cards:
    if not any(c["id"] == cid and c["type"] == "number" for c in BRIEF["cards"]):
        errors.append(f"A-list card {cid} is not a number card")
if sum(1 for c in BRIEF["cards"] if c["type"] == "number") != len(BRIEF["numbers"]["a_list"]):
    warnings.append("number cards differ from A-list rows")

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
    if not d["id"].startswith("messaging-"):
        errors.append(f"diagram {d['id']} does not start with the slug")
    if len(d["claim"].split()) > 24:
        errors.append(f"diagram {d['id']}: claim has {len(d['claim'].split())} words")

# 11. budget
words = sum(s.get("words_all_in", 0) for s in BRIEF["sections"])
subs = [s for s in BRIEF["sections"] if isinstance(s.get("plan"), dict)]

print(json.dumps({"errors": errors, "warnings": warnings, "pairs_checked": pairs, "sections": len(BRIEF["sections"]),
                  "subsections": len(subs), "words_all_in_sum": words, "traps": len(BRIEF["traps"]), "slots": len(qs),
                  "trap_slots": trap_slots, "difficulty": diff, "layer": layer, "multi": multi, "cards": deck,
                  "volatile_ch31": len(VOL), "term_requests": len(BRIEF["term_requests"]),
                  "faq_quote_words": [i.get("quote_words") for i in BRIEF["faq"]]}, indent=1))
if not errors:
    out = HERE / "brief.json"
    out.write_text(json.dumps(BRIEF, indent=2, ensure_ascii=False) + "\n")
    print("wrote", out.relative_to(ROOT.parent))
