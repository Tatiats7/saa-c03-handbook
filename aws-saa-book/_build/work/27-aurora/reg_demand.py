"""register-27: set demand statuses and fact lists in brief.v0.json from the miners' notes, the fact notes
(d27-NNN) and the registrar's own map for the behavior lens (whose miner note gave no per-item map).
Superseded ids are followed to the kept fact; rejected ids are dropped. Usage: python3 -I reg_demand.py [--write]"""
import json, os, re, sys

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/27-aurora/"
WRITE = "--write" in sys.argv

allf = {}
for fn in os.listdir(ROOT + "/data/facts"):
    if fn.endswith(".jsonl"):
        for line in open(ROOT + "/data/facts/" + fn):
            if line.strip():
                f = json.loads(line)
                allf[f["id"]] = f
ch = {k: v for k, v in allf.items() if v["service"] in ("aurora", "aurora-serverless")}
D = json.load(open(W + "reg-decisions.json"))
SUP = {o: n for o, n, _ in D["supersede"]}
REJ = {r for r, _ in D["reject"]}
ALIAS = {"aurora-faq-cross-region-replicas-global-db-five-regions": "aurora-global-secondary-regions-max-10",
         "aurora-faq-delete-drops-automated-backups": "aurora-retain-automated-backups-after-delete"}


def live(i, depth=0):
    if depth > 5 or i is None:
        return None
    i = ALIAS.get(i, i)
    if i in SUP:
        return live(SUP[i], depth + 1)
    f = allf.get(i)
    if f is None:
        return None
    if f["status"] == "superseded":
        return live(f.get("superseded_by"), depth + 1)
    if f["status"] == "rejected" or i in REJ:
        return None
    return i


m = {}


def add(did, ids):
    e = m.setdefault(did, [])
    for i in ids:
        j = live(i)
        if j and j not in e:
            e.append(j)


# 1. fact notes
for k, f in ch.items():
    for d in re.findall(r"d27-\d{3}", f.get("note") or ""):
        add(d, [k])
# 2. miner notes with per-item maps
faq = json.load(open(W + "mine-faq.json"))["demand"]
for d, v in faq.items():
    add(d, v.get("facts") or [])
dec = json.load(open(W + "mine-decisions+changes.json"))["demand"]
for d, v in dec.items():
    add(d, [x.split(" ")[0] for x in v.get("facts") or []])
# 3. registrar map (regex over live chapter ids, or exact ids of other namespaces)
MAP = json.load(open(W + "reg-demand-map.json"))
live_ids = sorted(k for k in ch if live(k) == k)
for d, pats in MAP["map"].items():
    for p in pats:
        if p in allf and not p.startswith("^"):
            add(d, [p])
        else:
            add(d, [k for k in live_ids if re.search(p, k)])

STATUS = MAP["status"]  # d -> [status, note]
b = json.load(open(W + "brief.v0.json"))
counts, report = {}, []
for d in b["demand"]:
    facts = m.get(d["id"], [])
    st, note = STATUS.get(d["id"], (None, None))
    if st is None:
        st = "found" if facts else "not-found"
    if st == "found" and not facts:
        st, note = "not-found", "no live fact"
    d["status"] = st
    d["facts"] = facts
    if note:
        d["note"] = note
    d["registered_by"] = "register-27"
    counts[st] = counts.get(st, 0) + 1
    report.append((d["id"], st, len(facts)))
print(counts)
for x in report:
    if x[1] != "found" or x[2] < 1:
        print(x)
print("min facts per found item:", min(n for _, s, n in report if s == "found"))
if WRITE:
    b.setdefault("notes", [])
    if isinstance(b["notes"], list):
        b["notes"].append("2026-10-13 register-27: demand statuses set after the merge (fact notes, faq and decisions miner maps, registrar map for the behavior lens; superseded ids followed to the kept fact)")
    json.dump(b, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("written")
