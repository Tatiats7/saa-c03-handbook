"""register-26: merge the miners' demand mappings into brief.v0.json (statuses found / partial / not-found)."""
import json, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/26-rds/"
WRITE = len(sys.argv) > 1 and sys.argv[1] == "--write"

facts = {}
for p in ["rds", "rds-proxy"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

ALIAS = {  # rejected outdated FAQ facts -> the guide fact that states the current truth
    "rds-faq-read-replica-count-15-or-5": "rds-quota-read-replicas-per-primary",
    "rds-faq-cross-region-replicas-not-sql-server": "rds-cross-region-replica-all-engines",
    "rds-faq-read-replica-cross-region": "rds-cross-region-replica-all-engines",
    "rds-faq-delete-instance-automated-backups-deleted": "rds-delete-instance-automated-backups-deleted",
    "rds-faq-blue-green-unsupported-topologies": "rds-blue-green-supports-proxy",
}


def live(i, seen=None):
    seen = seen or set()
    i = ALIAS.get(i, i)
    f = facts.get(i)
    if f is None or i in seen:
        return None
    seen.add(i)
    if f["status"] == "superseded":
        return live(f.get("superseded_by"), seen)
    if f["status"] == "rejected":
        return None
    return i


NORM = {"answered": "found", "found": "found", "filled": "found", "answered-by-other-lens": "found",
        "partial": "partial", "partly found": "partial", "not found": "not-found", "not-found": "not-found"}
m = {}


def add(did, ids, lens, status, note=None):
    e = m.setdefault(did, {"facts": [], "flags": []})
    for i in ids or []:
        j = live(i)
        if j and j not in e["facts"]:
            e["facts"].append(j)
    e["flags"].append((lens, NORM.get(status, status), note))


for lens, name in [("behavior", "mine-behavior.json"), ("faq", "mine-faq.json"), ("decisions+changes", "mine-decisions+changes.json")]:
    d = json.load(open(W + name))["demand"]
    for did, v in d.items():
        add(did, (v.get("facts") or []) + (v.get("current_truth") or []) + (v.get("also_existing") or []), lens, v.get("status"),
            v.get("note") or v.get("not_found"))
for v in json.load(open(W + "mine-numbers.json"))["demand"]:
    add(v["id"], v.get("facts"), "numbers", v.get("status"), v.get("note") or v.get("not_found"))

override = {
    "d26-009": ("partial", ["rds-external-source-binlog-replication"],
                "register-26: replication from an external MySQL or MariaDB source added (MySQL.Procedural.Importing.External.Repl); native dump and load pages still not mined"),
    "d26-006": ("partial", ["rds-blue-green-engines-only"],
                "IAM database authentication per engine not mined; Blue/Green engines from rds-blue-green-engines-only"),
    "d26-056": ("found", ["rds-external-source-binlog-replication"],
                "register-26: fetched MySQL.Procedural.Importing.External.Repl; binary log file replication with a MySQL or MariaDB instance outside RDS"),
}

b = json.load(open(W + "brief.v0.json"))
counts, report = {}, []
for d in b["demand"]:
    e = m.get(d["id"], {"facts": [], "flags": []})
    if d["id"] in override:
        st, extra, note = override[d["id"]]
        for x in extra:
            if x not in e["facts"]:
                e["facts"].append(x)
    else:
        sts = [f[1] for f in e["flags"]]
        notes = [f"{f[0]}: {f[2]}" for f in e["flags"] if f[2] and f[1] != "found"]
        if not sts:
            st, note = ("found", None) if e["facts"] else ("not-found", "no miner mapped a fact")
        elif all(s == "found" for s in sts):
            st, note = "found", None
        elif "partial" in sts or ("found" in sts and "not-found" in sts):
            st, note = "partial", "; ".join(notes) or None
        else:
            st, note = sts[0], "; ".join(notes) or None
        if st == "found" and not e["facts"]:
            st, note = "not-found", "status found but no live fact"
    d["status"] = st
    d["facts"] = e["facts"]
    if note:
        d["note"] = note
    d["registered_by"] = "register-26"
    counts[st] = counts.get(st, 0) + 1
    if st != "found":
        report.append((d["id"], st, len(e["facts"]), (note or "")[:140]))
print(counts)
for x in report:
    print(x)
if WRITE:
    b.setdefault("notes", []).append("2026-10-12 register-26: demand statuses set from the four miner notes after the merge (superseded ids followed to the kept fact; rejected outdated FAQ facts mapped to the guide fact)")
    json.dump(b, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("written")
