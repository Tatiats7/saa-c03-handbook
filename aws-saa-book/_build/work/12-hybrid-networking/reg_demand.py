"""register-12: write demand statuses into brief.v0.json (found / partial / not-found).

Sources: the d12-NNN ids in the notes of the live facts, the demand map of mine-faq.json, the not_found notes of the
other miners (as notes), and the registrar's own map and statuses in reg-demand-extra.json. Superseded ids are followed
to the kept fact; rejected ids are dropped. With --write the brief is updated, else it only prints.
"""
import json, re, sys
B = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/"
W = B + "_build/work/12-hybrid-networking/"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
brief = json.load(open(W + "brief.v0.json"))
facts = {}
for s in SVCS:
    for line in open(B + "data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def live(i):
    for _ in range(6):
        f = facts.get(i)
        if f is None:
            return None
        if f["status"] == "superseded":
            i = f.get("superseded_by")
            continue
        if f["status"] == "rejected":
            return None
        return i
    return None


got = {}


def put(did, ids, note=None):
    g = got.setdefault(did, {"facts": [], "notes": []})
    for i in ids:
        j = live(i)
        if j and j not in g["facts"]:
            g["facts"].append(j)
    if note and note not in g["notes"]:
        g["notes"].append(note)


for i, f in facts.items():
    if f["status"] in ("rejected", "superseded") or f.get("home_chapter") != "12":
        continue
    for did in set(re.findall(r"d12-\d{3}", f.get("note") or "")):
        put(did, [i])
faq = json.load(open(W + "mine-faq.json"))
for did, x in faq["demand"].items():
    put(did, x.get("facts", []), x.get("note"))
extra = json.load(open(W + "reg-demand-extra.json")) if len(sys.argv) > 1 or True else {}
for did, x in extra.get("map", {}).items():
    put(did, x.get("facts", []), x.get("note"))

out = []
for d in brief["demand"]:
    g = got.get(d["id"], {"facts": [], "notes": []})
    st = extra.get("status", {}).get(d["id"])
    if st is None:
        st = "found" if g["facts"] else "not-found"
    d["status"] = st
    d["facts"] = g["facts"]
    notes = list(g["notes"])
    if d["id"] in extra.get("notes", {}):
        notes.append(extra["notes"][d["id"]])
    if notes:
        d["note"] = " ".join(notes)
    out.append((d["id"], st, len(g["facts"])))
for x in out:
    if x[1] != "found" or x[2] == 0:
        print(x)
import collections
print(collections.Counter(x[1] for x in out))
if "--write" in sys.argv:
    brief["registered_by"] = "register-12"
    brief["registered_at"] = "2026-10-14"
    json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("written")
