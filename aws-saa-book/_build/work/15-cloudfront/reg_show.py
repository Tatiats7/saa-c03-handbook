"""register-15: print full fact blocks for the ids given on the command line (prefix 'cf:' = cloudfront-, 'ga:' = global-accelerator-)."""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
rows = {}
for f in ["cloudfront", "global-accelerator"]:
    for l in open(ROOT / f"aws-saa-book/data/facts/{f}.jsonl"):
        r = json.loads(l); rows[r["id"]] = r
for a in sys.argv[1:]:
    i = a.replace("cf:", "cloudfront-").replace("ga:", "global-accelerator-")
    r = rows.get(i)
    if r is None:
        print("MISSING", i); continue
    q = r.get("qualifiers") or {}
    print(f"[{i}] {r['kind']} hard={r['hard']} rel={r['exam_relevance']} tier={r['source_tier']} vol={r['volatility']} st={r['status']} rev={r['rev']}")
    print(f"   C: {r['claim']}")
    print(f"   D: {[v for v in r['values']]}")
    print(f"   S: {q}  changed={r.get('changed')}  items={r.get('change_items')}")
    for e in r["evidence"]:
        print(f"   Q[{e['source_id']} th={e.get('table_header')!r} h={e.get('heading')!r}]: {e['quote']}")
