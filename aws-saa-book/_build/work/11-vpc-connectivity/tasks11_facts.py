"""tasks-11 helper: print facts by id or by a word search (read-only).

Usage:
  python3 aws-saa-book/_build/work/11-vpc-connectivity/tasks11_facts.py id ID [ID ...]
  python3 aws-saa-book/_build/work/11-vpc-connectivity/tasks11_facts.py grep SERVICE WORD [WORD ...]
"""
import json
import sys
from pathlib import Path

FACTS = Path(__file__).resolve().parents[3] / "data" / "facts"


def load_all():
    out = {}
    for p in sorted(FACTS.glob("*.jsonl")):
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                f = json.loads(line)
            except Exception:
                continue
            out[f.get("id")] = f
    return out


def show(f):
    print("=" * 80)
    print(f.get("id"), "|", f.get("status"), "|", f.get("kind"), "| hard:", f.get("hard"), "| vol:", f.get("volatility"))
    print("CLAIM:", f.get("claim"))
    print("DISPLAYS:", [v.get("display") for v in (f.get("values") or [])])
    for ev in f.get("evidence", []):
        print("  URL:", ev.get("url"))
        if ev.get("heading"):
            print("  HEADING:", ev.get("heading"))
        if ev.get("table_header"):
            print("  HEADER:", ev.get("table_header"))
        print("  QUOTE:", ev.get("quote"))


def main():
    mode = sys.argv[1]
    facts = load_all()
    if mode == "id":
        for fid in sys.argv[2:]:
            f = facts.get(fid)
            if f is None:
                print("=" * 80)
                print(fid, "NOT FOUND")
            else:
                show(f)
    elif mode == "grep":
        svc = sys.argv[2]
        words = [w.lower() for w in sys.argv[3:]]
        for fid, f in facts.items():
            if svc != "*" and f.get("service") != svc:
                continue
            if f.get("status") in ("rejected", "superseded"):
                continue
            text = json.dumps(f).lower()
            if all(w in text for w in words):
                show(f)


if __name__ == "__main__":
    main()
