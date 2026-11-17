"""adjudicate-31: drop rejected or superseded facts from brief demand items; an item with no fact left becomes not-found."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
status = {}
for name in os.listdir(os.path.join(ROOT, "data", "facts")):
    if name.endswith(".jsonl"):
        for line in open(os.path.join(ROOT, "data", "facts", name)):
            if line.strip():
                d = json.loads(line)
                status[d["id"]] = d.get("status")
path = os.path.join(HERE, "brief.v0.json")
b = json.load(open(path))
changed = []
for d in b["demand"]:
    facts = d.get("facts") or []
    gone = [f for f in facts if status.get(f) in ("rejected", "superseded") or f not in status]
    if not gone:
        continue
    d["facts"] = [f for f in facts if f not in gone]
    note = "adjudicate-31: removed " + ", ".join(gone) + " (rejected or superseded at verify-facts)"
    d["note"] = (d.get("note") + " | " + note) if d.get("note") else note
    if not d["facts"]:
        d["status"] = "not-found"
    changed.append((d["id"], gone, d["status"]))
json.dump(b, open(path, "w"), indent=1, ensure_ascii=False)
for c in changed:
    print(c)
from collections import Counter
print(Counter(x["status"] for x in b["demand"]))
