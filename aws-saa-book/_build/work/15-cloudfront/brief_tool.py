"""brief-15 helper: list volatile facts, and check every fact id named in brief.json.

Usage (from the repo root):
  python3 aws-saa-book/_build/work/15-cloudfront/brief_tool.py volatile
  python3 aws-saa-book/_build/work/15-cloudfront/brief_tool.py check
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FACTS = ROOT / "data" / "facts"
WORK = Path(__file__).resolve().parent
SNAP_CUT = "2024-10-04"  # snapshot 2026-10-04 minus 24 months


def load():
    rows = {}
    for path in FACTS.glob("*.jsonl"):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            rows[row["id"]] = row
    return rows


def volatile(f):
    if f.get("volatility") == "frequently-changing" or f.get("kind") == "price":
        return True
    ch = f.get("changed") or {}
    d = ch.get("date")
    if not d:
        return False
    return d >= (SNAP_CUT if len(d) > 7 else SNAP_CUT[:7])


def main():
    rows = load()
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    if mode == "volatile":
        out = []
        for fid, f in sorted(rows.items()):
            if f.get("home_chapter") != "15" or f.get("status") != "verified":
                continue
            if volatile(f):
                why = "price" if f.get("kind") == "price" else (f.get("volatility") if f.get("volatility") != "stable" else "changed " + str((f.get("changed") or {}).get("date")))
                out.append(f"{fid} | {f.get('kind')} | {why}")
        (WORK / "volatile-15.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"{len(out)} volatile verified facts of chapter 15 -> volatile-15.txt")
        return
    brief = json.loads((WORK / "brief.json").read_text(encoding="utf-8"))
    text = json.dumps(brief)
    ids = set(re.findall(r"\b((?:cloudfront|global-accelerator|acm|elb|s3|route53|waf|shield|global-infrastructure|lambda|vpc|ec2)-[a-z0-9]+(?:-[a-z0-9]+)+)\b", text))
    trap_ids = {t["id"] for t in brief.get("traps", [])}
    bad, vol = [], []
    for fid in sorted(ids):
        if "-trap-" in fid or fid.startswith("cloudfront-q") or re.match(r"^cloudfront-(c|t|s|q)\d", fid):
            continue
        if fid in ("cloudfront-hero", "cloudfront-before", "cloudfront-after"):
            continue
        f = rows.get(fid)
        if f is None:
            bad.append(f"MISSING {fid}")
        elif f.get("status") != "verified":
            bad.append(f"NOT VERIFIED ({f.get('status')}) {fid}")
        elif volatile(f):
            vol.append(fid)
    print("not ok:" if bad else "all named fact ids verified")
    for b in bad:
        print("  " + b)
    print(f"volatile named ({len(vol)}): " + ", ".join(vol))
    # slot checks
    slots = brief.get("question_slots", [])
    print(f"slots {len(slots)}; traps {len(trap_ids)}; sections {len(brief.get('sections', []))}")
    from collections import Counter
    print("difficulty", Counter(s["difficulty"] for s in slots))
    print("layer", Counter(s["layer"] for s in slots))
    print("type", Counter(s["type"] for s in slots))
    print("on a trap", sum(1 for s in slots if s.get("trap")))
    print("bullets", Counter(s["bullet"] for s in slots))
    conc = Counter(s["concept"] for s in slots)
    print("concepts >2", [c for c, n in conc.items() if n > 2])
    secs = {s["file"] + "#" + s["section"] for s in brief.get("sections", [])}
    for s in slots:
        if s.get("section") not in secs:
            print("slot section not in sections:", s.get("id"), s.get("section"))
    for key in ("tasks", "speak", "cards", "diagrams"):
        for it in brief.get(key, []):
            sec = it.get("section")
            if sec and sec not in secs:
                print(f"{key} section not in sections:", it.get("id"), sec)
    used = set()
    for s in slots:
        if s.get("trap"):
            used.add(s["trap"])
        for t in s.get("distractor_traps", []):
            used.add(t)
    print("brief traps cited by no slot:", sorted(trap_ids - used))
    words = 0
    for s in brief.get("sections", []):
        if s.get("words_all_in"):
            words += s["words_all_in"]
    print("how-it-works words_all_in sum", words)


if __name__ == "__main__":
    main()
