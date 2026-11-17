"""close-facts-13: recompute demand statuses of brief.v0.json from fact statuses.
Usage: python3 close_demand.py REPO_ROOT [--write]
"""
import glob, json, os, sys, collections

root = sys.argv[1]
write = "--write" in sys.argv
facts = {}
for f in glob.glob(os.path.join(root, "aws-saa-book/data/facts/*.jsonl")):
    for line in open(f):
        line = line.strip()
        if line:
            d = json.loads(line)
            facts[d["id"]] = d

def resolve(fid, seen=None):
    seen = seen or set()
    f = facts.get(fid)
    if f is None or fid in seen:
        return [(fid, "missing")]
    seen.add(fid)
    if f.get("status") == "superseded" and f.get("superseded_by"):
        sb = f["superseded_by"]
        sb = sb if isinstance(sb, list) else [sb]
        out = []
        for s in sb:
            out += resolve(s, seen)
        return out
    return [(fid, f.get("status"))]

path = os.path.join(root, "aws-saa-book/_build/work/13-route53/brief.v0.json")
b = json.load(open(path))
before = collections.Counter(x["status"] for x in b["demand"])
changes = []
for d in b["demand"]:
    res = []
    for fid in d.get("facts", []):
        for r in resolve(fid):
            if r not in res:
                res.append(r)
    ver = [i for i, s in res if s == "verified"]
    bad = [i for i, s in res if s != "verified"]
    old = d["status"]
    if not ver:
        new = "not-found"
    elif old == "partial" or bad:
        new = "partial"
    else:
        new = "filled"
    if new != old or bad or ver != d.get("facts", []):
        changes.append((d["id"], old, new, d.get("facts"), ver, bad))
    d["status"] = new
    d["facts"] = ver
    if bad:
        d["dropped_facts"] = bad
b["demand_status_by"] = ("close-facts-13 (2026-10-13, after facts finalize and stage end verify-facts): "
    "filled = every fact verified and the question answered; partial = verified facts answer only part of the question "
    "(kept from the miners' and adjudicator's judgement, or a fact was rejected); not-found = no verified fact. "
    "Superseded facts are replaced by their successor; rejected facts are listed in dropped_facts.")
after = collections.Counter(x["status"] for x in b["demand"])
for c in changes:
    print(c)
print("before", dict(before), "after", dict(after))
if write:
    with open(path, "w") as fh:
        json.dump(b, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("written")
