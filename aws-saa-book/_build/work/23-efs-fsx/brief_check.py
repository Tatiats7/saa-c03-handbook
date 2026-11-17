"""Helper of brief-23: show facts, list volatile facts, check brief.json against the canon.

Usage (from the repo root):
  python3 aws-saa-book/_build/work/23-efs-fsx/brief_check.py show ID [ID ...]
  python3 aws-saa-book/_build/work/23-efs-fsx/brief_check.py volatile
  python3 aws-saa-book/_build/work/23-efs-fsx/brief_check.py check
Read-only except for the report file written by `check` (brief-check.txt next to this script).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOK = HERE.parents[2]
FACTS = BOOK / "data" / "facts"
sys.path.insert(0, str(BOOK / "tools"))


def load_facts():
    out = {}
    for path in sorted(FACTS.glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            out[row["id"]] = row
    return out


def is_volatile(fact):
    try:
        from saalib import facts as F  # noqa
        return F.is_volatile(fact)
    except Exception:  # fallback: 24 months before 2026-10-14
        if fact.get("volatility") == "frequently-changing" or fact.get("kind") == "price":
            return True
        ch = fact.get("changed") or {}
        return bool(ch.get("date")) and ch["date"] >= "2024-10-14"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def show(ids):
    canon = load_facts()
    for fid in ids:
        f = canon.get(fid)
        if not f:
            print(f"== {fid}: NOT IN CANON")
            continue
        print(f"== {fid} [{f.get('status')}] kind={f.get('kind')} hard={f.get('hard')} volatile={is_volatile(f)}")
        print("   displays:", " | ".join(v.get("display", "") for v in f.get("values", [])))
        if f.get("changed"):
            print("   changed:", f["changed"])
        for ev in f.get("evidence", []):
            print("   url:", ev.get("url"))
            print("   quote:", ev.get("quote"))
            if ev.get("table_header"):
                print("   header:", ev.get("table_header"))


def volatile():
    canon = load_facts()
    for fid, f in sorted(canon.items()):
        if f.get("home_chapter") == "23" and f.get("status") == "verified" and is_volatile(f):
            print(fid)


PAIR = re.compile(r"\[([^\[\]]+)\]\s*\(([a-z0-9][a-z0-9-]+)\)")


def walk(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def check():
    canon = load_facts()
    brief = json.loads((HERE / "brief.json").read_text(encoding="utf-8"))
    errors, notes = [], []
    # every fact id that appears anywhere as a fact-id-shaped token in a 'facts' list or in a (fact-id) pair
    ids = set()
    for path, text in walk(brief):
        if re.search(r"\.(facts|facts_for_steps|facts_for_caption|key_facts|cost_facts)\[\d+\]$", path) or path.endswith(".fact"):
            ids.add(text)
        for disp, fid in PAIR.findall(text):
            if fid not in canon:
                if "-" in fid and not fid.startswith(("efs-fsx-", "ee-", "fr-", "q")):
                    errors.append(f"{path}: pair id {fid} not in canon")
                continue
            ids.add(fid)
            displays = [norm(v.get("display", "")) for v in canon[fid].get("values", [])]
            if norm(disp) not in displays:
                errors.append(f"{path}: [{disp}] is not a display of {fid}; displays: {displays}")
    # every bracketed text must be a display of some fact id named in the same string
    id_rx = re.compile(r"\b([a-z0-9]+(?:-[a-z0-9]+){2,})\b")
    loose = []
    for path, text in walk(brief):
        named = [t for t in id_rx.findall(text) if t in canon]
        for disp in re.findall(r"\[([^\[\]]+)\]", text):
            if not named:
                loose.append(f"{path}: [{disp}] (no fact id in string)")
                continue
            ok = any(norm(disp) == norm(v.get("display", "")) for fid in named for v in canon[fid].get("values", []))
            if not ok:
                loose.append(f"{path}: [{disp}] not a display of {named}")
    for fid in sorted(ids):
        f = canon.get(fid)
        if not f:
            errors.append(f"fact {fid} not in canon")
        elif f.get("status") != "verified":
            errors.append(f"fact {fid} status {f.get('status')}")
    # traps
    trap_ids = [t["id"] for t in brief.get("traps", [])]
    if len(trap_ids) > 13:
        errors.append(f"{len(trap_ids)} traps > 13")
    for t in trap_ids:
        if not t.startswith("efs-fsx-trap-"):
            errors.append(f"trap id {t} lacks the slug prefix")
    # slots
    ee_ids = set(re.findall(r'"id":\s*"(ee-[^"]+)"', (BOOK / "data" / "exam-english.json").read_text(encoding="utf-8")))
    sections = {f"{s['file']}#{s['section']}" for s in brief["sections"]}
    known_traps = set(trap_ids) | set(brief.get("traps_from_other_chapters", {}).get("ids", []))
    for i, s in enumerate(brief["question_slots"]):
        for w in s.get("exam_english", []):
            if w not in ee_ids:
                errors.append(f"slot {i}: unknown exam-English id {w}")
        if s.get("section") and s["section"] not in sections:
            errors.append(f"slot {i}: section {s['section']} not in brief sections")
        if s.get("trap") and s["trap"] not in known_traps:
            errors.append(f"slot {i}: trap {s['trap']} unknown")
        for fid in s.get("key_facts", []):
            f = canon.get(fid)
            if f and is_volatile(f):
                errors.append(f"slot {i}: key fact {fid} is volatile")
    for t in brief.get("tasks", []):
        if t.get("section") and t["section"] not in sections:
            errors.append(f"task {t.get('id')}: section {t['section']} not in brief sections")
    for t in brief.get("speak", []):
        if t.get("section") and t["section"] not in sections:
            errors.append(f"speak {t.get('id')}: section {t['section']} not in brief sections")
    for c in brief.get("cards", []):
        if c.get("section") and c["section"] not in sections:
            errors.append(f"card {c.get('id')}: section {c['section']} not in brief sections")
        if c.get("trap") and c["trap"] not in known_traps:
            errors.append(f"card {c.get('id')}: trap {c['trap']} unknown")
    # terms
    terms = json.loads((BOOK / "data" / "terms.json").read_text(encoding="utf-8"))
    bank = set()
    for t in terms.get("terms", []):
        bank.add(t.get("id"))
        bank.add(t.get("term"))
    for t in brief.get("terms", []):
        if t not in bank:
            errors.append(f"term {t} not in the bank")
    # bullets
    book = json.loads((BOOK / "data" / "book.json").read_text(encoding="utf-8"))
    entry = next(c for c in book["chapters"] if c["id"] == "23")
    in_sec = {b for s in brief["sections"] for b in s.get("bullets", [])}
    in_slot = {s["bullet"] for s in brief["question_slots"]}
    for b in entry.get("bullets", []):
        if b not in in_sec:
            errors.append(f"bullet {b} in no section")
        if b not in in_slot:
            errors.append(f"bullet {b} in no slot")
    notes.append(f"facts named: {len(ids)}; traps {len(trap_ids)}; slots {len(brief['question_slots'])}; sections {len(brief['sections'])}")
    vol = sorted(fid for fid in ids if canon.get(fid) and is_volatile(canon[fid]))
    notes.append("volatile facts named: " + ", ".join(vol))
    report = "\n".join(notes + ["ERRORS:"] + errors + ["LOOSE BRACKETS:"] + loose + ["END"])
    (HERE / "brief-check.txt").write_text(report + "\n", encoding="utf-8")
    print(report)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "show":
        show(sys.argv[2:])
    elif cmd == "volatile":
        volatile()
    else:
        check()
