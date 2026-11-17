"""Read-only: do facts that cite SOURCE_ID still match its current snapshot? Usage: python3 -I quotecheck.py SOURCE_ID"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from saalib import common, corpus  # noqa: E402
sid = sys.argv[1]
text = corpus.load_text(sid)
bad = ok = 0
for f in sorted((ROOT / "data" / "facts").glob("*.jsonl")):
    for line in f.read_text().splitlines():
        if not line.strip():
            continue
        fact = json.loads(line)
        evs = fact.get("evidence") or []
        if isinstance(evs, dict):
            evs = [evs]
        for ev in evs:
            if ev.get("source_id") != sid:
                continue
            q = ev.get("quote", "")
            hit = common.find_quote(q, text) is not None
            ok += hit
            bad += not hit
            if not hit:
                print("NO MATCH", fact.get("id"), fact.get("status"), "|", q[:160])
print("ok", ok, "no-match", bad)
