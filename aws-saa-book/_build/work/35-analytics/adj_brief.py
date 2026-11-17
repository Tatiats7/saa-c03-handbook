"""adjudicate-35: update the demand items of brief.v0.json after adjudication.
Removes rejected fact ids from each demand item, lists the ids that wait for a revote, and sets status not-found
when no fact is left."""
import json

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange"]

status = {}
for s in SERVICES:
    for line in open(ROOT + "/data/facts/" + s + ".jsonl"):
        if line.strip():
            f = json.loads(line)
            status[f["id"]] = f.get("status")

revote = set()
for b in ["35-entail-015", "35-entail-016", "35-entail-017", "35-currency-003"]:
    revote |= set(json.load(open(ROOT + "/_build/facts/batches/" + b + ".json"))["facts"])

path = W + "brief.v0.json"
brief = json.load(open(path))
changed = []
for d in brief["demand"]:
    facts = d.get("facts", [])
    dropped = [f for f in facts if status.get(f) in ("rejected", "superseded")]
    keep = [f for f in facts if f not in dropped]
    waiting = sorted(f for f in keep if f in revote)
    if dropped:
        d["facts"] = keep
        d["adjudicate_rejected"] = dropped
    if waiting:
        d["pending_revote"] = waiting
    elif "pending_revote" in d:
        del d["pending_revote"]
    if not keep and d.get("status") != "not-found":
        d["status"] = "not-found"
    if dropped or waiting:
        d["adjudicated_by"] = "adjudicate-35"
        changed.append((d["id"], d["status"], len(keep), len(dropped), len(waiting)))
json.dump(brief, open(path, "w"), ensure_ascii=False, indent=1)
for row in changed:
    print(*row)
