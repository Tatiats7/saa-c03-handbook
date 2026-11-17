"""Compact view of brief.v0.json: top keys, then each demand item on a few lines."""
import json, sys

d = json.load(open(sys.argv[1]))
for k, v in d.items():
    if k == "demand":
        continue
    s = json.dumps(v)
    print(f"== {k}: {s[:1200]}")
print("== demand:", len(d.get("demand", [])))
for it in d.get("demand", []):
    extra = {k: v for k, v in it.items() if k not in ("id", "bullet", "question", "status", "facts")}
    print(f"- {it.get('id')} [{it.get('bullet')}] {it.get('status')}: {it.get('question')}")
    print(f"    facts: {', '.join(it.get('facts') or [])}")
    if extra:
        print(f"    extra: {json.dumps(extra)[:400]}")
