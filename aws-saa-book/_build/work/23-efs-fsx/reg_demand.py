"""register-23: merge the miners' demand statuses into brief.v0.json (found / partial / not-found).

Miner notes: mine-behavior.json and mine-decisions+changes.json list facts per demand item; mine-faq.json lists
answered and not-found items; mine-numbers.json lists only the not-found items. Items without a fact list get
their facts by matching: facts of the same service whose evidence comes from the item's sources or its lens
pages, ranked by shared question words (at least 3). Registrar overrides are in reg-demand-overrides.json.
Pass --write to update brief.v0.json; otherwise only reg-demand-result.txt is written.
"""
import json, re, glob, sys, collections
B = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/"
W = B + "_build/work/23-efs-fsx/"
brief = json.load(open(W + "brief.v0.json"))
plan = json.load(open(W + "mine-plan.json"))
facts = {}
for svc in ("efs", "fsx"):
    for line in open(B + "data/facts/%s.jsonl" % svc):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def live(i):
    for _ in range(6):
        f = facts.get(i)
        if f is None:
            return None
        if f["status"] == "superseded":
            i = f["superseded_by"]
            continue
        if f["status"] == "rejected":
            return None
        return i
    return None


got = {}


def put(did, status, ids, note=None):
    g = got.setdefault(did, {"status": None, "facts": [], "notes": []})
    order = {"found": 0, "partial": 1, "not-found": 2}
    s = {"filled": "found", "answered": "found"}.get(status, status)
    if g["status"] is None or order[s] < order[g["status"]]:
        g["status"] = s
    for i in ids:
        if i not in g["facts"]:
            g["facts"].append(i)
    if note:
        g["notes"].append(note)


beh = json.load(open(W + "mine-behavior.json"))
for did, x in beh["demand"].items():
    put(did, x["status"], x.get("facts", []), x.get("not_found") or x.get("note"))
dc = json.load(open(W + "mine-decisions+changes.json"))
dem = dc["demand"]
for did, x in (dem.items() if isinstance(dem, dict) else [(y["id"], y) for y in dem]):
    put(did, x["status"], x.get("facts", []), x.get("note") or x.get("not_found"))
faq = json.load(open(W + "mine-faq.json"))
for did in faq.get("answered", []):
    put(did, "found", [])
partial_faq = {x["demand"]: x["note"] for x in faq.get("not_found", [])}
num = json.load(open(W + "mine-numbers.json"))
nf_num = {x["id"]: x["note"] for x in num.get("demand_not_found", [])}

STOP = set("the a an and or of to in for on with is are be by that this it its your you can as from at not which what "
           "how does do when per vs versus there their than many much any each one and/or".split())


def toks(s):
    return {t for t in re.findall(r"[a-z][a-z0-9-]+", s.lower()) if t not in STOP and len(t) > 2}


lens_pages = {k: set(v.get("pages", [])) for k, v in plan["lenses"].items()}
ch_live = [f for f in facts.values() if f.get("home_chapter") == "23" and f["status"] not in ("rejected", "superseded")]


def match(dm):
    q = toks(dm["question"])
    srcs = set(dm.get("sources") or []) | lens_pages.get(dm.get("lens"), set())
    ql = dm["question"].lower()
    subs = [s for s, w in (("windows", "windows"), ("lustre", "lustre"), ("ontap", "ontap"), ("openzfs", "openzfs")) if w in ql]
    scored = []
    for f in ch_live:
        if f["service"] != dm["service"]:
            continue
        if subs and not any(s in f["id"] for s in subs) and not re.search(r"compare|when-to-choose|decision", f["id"]):
            continue
        if not any(e["source_id"] in srcs for e in f["evidence"]):
            continue
        s = len(q & (toks(f["claim"]) | toks(f["id"].replace("-", " "))))
        if s >= 3:
            scored.append((s, f["id"]))
    scored.sort(reverse=True)
    return [i for _, i in scored[:6]]


over = json.load(open(W + "reg-demand-overrides.json"))
out = []
for dm in brief["demand"]:
    did = dm["id"]
    g = got.get(did, {"status": None, "facts": [], "notes": []})
    ids = [j for j in (live(i) for i in g["facts"]) if j]
    ids = list(dict.fromkeys(ids))
    status = g["status"]
    notes = list(g["notes"])
    if not ids:
        ids = match(dm)
        if ids:
            notes.append("register-23: facts matched by source and question words")
    if did in nf_num:
        notes.append("mine-numbers: " + nf_num[did])
        status = "partial" if ids else "not-found"
    if did in partial_faq:
        notes.append("mine-faq: " + partial_faq[did])
        status = "partial" if ids else "not-found"
    if status is None:
        status = "found" if ids else "not-found"
    if status == "found" and not ids:
        status = "not-found"
    if did in over:
        o = over[did]
        status = o["status"]
        for i in o.get("facts", []):
            j = live(i)
            if j and j not in ids:
                ids.insert(0, j)
            elif not j:
                print("override fact not live:", did, i)
        notes.append(o["note"])
    dm["status"] = status
    dm["facts"] = ids
    if notes:
        dm["note"] = " | ".join(n for n in notes if n)
    dm["registered_by"] = "register-23"
    out.append("%s %s [%s] %s\n   %s\n" % (did, status, dm["service"], dm["question"][:110], ", ".join(ids)))
open(W + "reg-demand-result.txt", "w").write("".join(out))
print(collections.Counter(d["status"] for d in brief["demand"]))
if "--write" in sys.argv:
    json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("wrote brief.v0.json")
