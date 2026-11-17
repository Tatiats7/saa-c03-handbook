"""List chapter 27 facts by group (helper of brief-27; read-only). Usage: brief_facts_list.py vol|faq|changed|case|kinds|ids PREFIX"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from saalib import facts as F  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
mode = sys.argv[1] if len(sys.argv) > 1 else "vol"
arg = sys.argv[2] if len(sys.argv) > 2 else ""
files = ("aurora", "aurora-serverless")
if mode == "other":
    files = tuple(arg.split(","))
rows = []
for svc in files:
    for line in (ROOT / "data" / "facts" / f"{svc}.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        if f.get("status") != "verified":
            continue
        rows.append(f)
for f in rows:
    ev = f["evidence"][0]["url"]
    vol = F.is_volatile(f)
    ch = f.get("changed") or {}
    if mode == "vol" and vol:
        print(f"{f['id']} ({f.get('volatility')}{', changed ' + ch.get('date', '') if ch else ''})")
    elif mode == "faq" and ("faq" in ev):
        print(f"{f['id']} | {f['kind']} | {ev.split('/')[-1]}{' | VOL' if vol else ''} | {[v['display'] for v in f.get('values') or []]}")
    elif mode == "changed" and ch:
        print(f"{f['id']} | changed {ch.get('date')} was {ch.get('was')!r} | {'VOL' if vol else ''} | {[v['display'] for v in f.get('values') or []]}")
    elif mode == "case" and f["kind"] == "case-study":
        print(f"{f['id']} | {ev} | {f['evidence'][0]['quote']}")
    elif mode == "kinds":
        pass
    elif mode == "other":
        print(f"{f['id']}{' VOL' if vol else ''} | {f['claim'][:160]} | {[v['display'] for v in f.get('values') or []]}")
    elif mode == "quote" and f["id"] == arg:
        print(json.dumps({"id": f["id"], "kind": f["kind"], "hard": f.get("hard"), "values": f.get("values"), "changed": ch, "evidence": [{"url": e["url"], "quote": e["quote"]} for e in f["evidence"]]}, indent=1))
if mode == "kinds":
    from collections import Counter
    print(Counter(f["kind"] for f in rows), len(rows), sum(1 for f in rows if F.is_volatile(f)))
