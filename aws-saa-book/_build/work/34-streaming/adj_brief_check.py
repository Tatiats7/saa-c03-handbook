"""adjudicate-34: parse brief.v0.json and report demand items whose facts are rejected/superseded (read-only)."""
import json, os, sys
ROOT = sys.argv[1]
b = json.load(open(os.path.join(ROOT, "_build/work/34-streaming/brief.v0.json")))
status = {}
for fn in os.listdir(os.path.join(ROOT, "data/facts")):
    if fn.endswith(".jsonl"):
        for line in open(os.path.join(ROOT, "data/facts", fn)):
            if line.strip():
                f = json.loads(line)
                status[f["id"]] = f["status"]
from collections import Counter
c = Counter()
for d in b["demand"]:
    c[d["status"]] += 1
    for i in d.get("facts", []):
        s = status.get(i, "missing")
        if s in ("rejected", "superseded", "missing"):
            print(d["id"], i, s)
print("ok", len(b["demand"]), dict(c))
