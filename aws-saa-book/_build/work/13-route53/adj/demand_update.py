"""adjudicate-13: set brief demand statuses from fact statuses.
found + all facts verified -> filled; partial stays partial; no facts -> not-found;
an item with a fact that waits for a revote keeps its status and lists the ids in pending_revote."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
st = {}
for svc in os.listdir(os.path.join(B, "data/facts")):
    if svc.endswith(".jsonl"):
        for line in open(os.path.join(B, "data/facts", svc)):
            f = json.loads(line)
            st[f["id"]] = f.get("status")
path = os.path.join(HERE, "..", "brief.v0.json")
brief = json.load(open(path))
count = {}
for d in brief["demand"]:
    fs = d.get("facts") or []
    pend = [x for x in fs if st.get(x) != "verified"]
    if not fs:
        d["status"] = "not-found"
    elif pend:
        d["pending_revote"] = pend
    else:
        d.pop("pending_revote", None)
        if d["status"] == "found":
            d["status"] = "filled"
    count[d["status"]] = count.get(d["status"], 0) + 1
brief["demand_status_by"] = "adjudicate-13 (2026-10-13): filled = every fact verified; pending_revote = repaired facts waiting for fresh votes"
json.dump(brief, open(path, "w"), ensure_ascii=False, indent=1)
print(count, sum(1 for d in brief["demand"] if d.get("pending_revote")))
