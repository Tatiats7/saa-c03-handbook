"""register-35: set demand statuses in brief.v0.json (found / partial / not-found) from the miners' notes and the
demand ids that the facts carry in their note field. Superseded ids are followed to the kept fact. Dry run unless --write."""
import json, re, sys

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
WRITE = len(sys.argv) > 1 and sys.argv[1] == "--write"
SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange", "redshift", "data-firehose",
            "rds", "aurora", "s3", "dynamodb"]
facts = {}
for s in SERVICES:
    try:
        fh = open(ROOT + "/data/facts/%s.jsonl" % s)
    except OSError:
        continue
    for line in fh:
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def live(i, seen=None):
    seen = seen or set()
    f = facts.get(i)
    if f is None or i in seen:
        return None
    seen.add(i)
    if f["status"] == "superseded":
        return live(f.get("superseded_by"), seen)
    if f["status"] == "rejected":
        return None
    return i


m = {}


def add(did, ids, status=None, note=None):
    e = m.setdefault(did, {"facts": [], "flags": []})
    for i in ids or []:
        j = live(i)
        if j and j not in e["facts"]:
            e["facts"].append(j)
    if status:
        e["flags"].append((status, note))


# facts that carry a demand id in their note (chapter 35 facts)
for i, f in facts.items():
    if str(f.get("home_chapter")) == "35" and f["status"] not in ("rejected", "superseded"):
        for did in re.findall(r"\bd0\d\d\b", f.get("note") or ""):
            add(did, [i])

faq = json.load(open(W + "mine-faq.json"))["demand_map"]
for did, v in faq.items():
    st = "found" if v.get("status") == "filled" else v.get("status")
    nf = v.get("not_found")
    add(did, v.get("facts"), "partial" if nf else st, "; ".join(nf) if nf else None)

beh = json.load(open(W + "mine-behavior+decisions.json"))["demand"]
for did, v in beh.items():
    if did == "d024-d044":
        continue
    ids = list(v.get("facts") or [])
    for lst in (v.get("reasons") or {}).values():
        ids += lst
    add(did, ids, "found" if str(v.get("status", "")).startswith("filled") else v.get("status"), v.get("contradiction"))

num = json.load(open(W + "mine-numbers+changes.json"))["demand_status"]
for did, text in num.items():
    if text.startswith("partly not found"):
        add(did, [], "partial", "numbers+changes: " + text)
    elif "not found" in text:
        add(did, [], "partial", "numbers+changes: " + text)
    else:
        add(did, [], "found", None)

try:
    override = json.load(open(W + "reg-demand-override.json"))
except OSError:
    override = {}

b = json.load(open(W + "brief.v0.json"))
counts, report = {}, []
for d in b["demand"]:
    e = m.get(d["id"], {"facts": [], "flags": []})
    ov = override.get(d["id"])
    if ov:
        for x in ov.get("facts", []):
            j = live(x)
            if j and j not in e["facts"]:
                e["facts"].append(j)
        st, note = ov["status"], ov.get("note")
    else:
        sts = [f[0] for f in e["flags"]]
        notes = [f[1] for f in e["flags"] if f[1]]
        if "partial" in sts:
            st = "partial"
        elif e["facts"]:
            st = "found"
        else:
            st = "not-found"
        note = "; ".join(notes) or None
    if st in ("found", "partial") and not e["facts"]:
        st, note = "not-found", (note or "") + " (no live fact mapped)"
    d["status"] = st
    d["facts"] = e["facts"]
    if note:
        d["note"] = note
    d["registered_by"] = "register-35"
    counts[st] = counts.get(st, 0) + 1
    report.append((d["id"], st, len(e["facts"]), (note or "")[:160]))
print(counts)
for x in report:
    if x[1] != "found" or x[2] < 2:
        print(x)
if WRITE:
    b.setdefault("notes", []).append("2026-10-22 register-35: demand statuses set from the miner notes and the demand ids in the fact notes, after the merge (superseded ids followed to the kept fact)")
    json.dump(b, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("written")
