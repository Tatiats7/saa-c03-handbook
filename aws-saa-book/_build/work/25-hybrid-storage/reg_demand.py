"""register-25: set demand statuses and facts in brief.v0.json (found / partial / not-found).

Inputs: fact notes that name demand ids (behavior+decisions and numbers+changes miners), mine-faq.json demand map,
the miners' not-found lists, and registrar overrides in reg-demand-overrides.json. Items without any fact get
candidates by matching: live facts of the item's service whose evidence comes from the item's look_in pages,
ranked by shared question words (at least 3). Pass --write to update brief.v0.json; otherwise only
reg-demand-result.txt is written.
"""
import json, os, re, sys, collections
W = os.path.dirname(os.path.abspath(__file__)) + "/"
B = os.path.abspath(W + "../../..") + "/"
brief = json.load(open(W + "brief.v0.json"))
facts = {}
for svc in ("storage-gateway", "datasync", "snow-family", "transfer-family"):
    for line in open(B + "data/facts/%s.jsonl" % svc):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
# facts of other services named by overrides
for svc in ("s3", "efs", "fsx", "direct-connect", "backup"):
    p = B + "data/facts/%s.jsonl" % svc
    if os.path.exists(p):
        for line in open(p):
            if line.strip():
                f = json.loads(line)
                facts.setdefault(f["id"], f)


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


got = collections.defaultdict(list)
notes = collections.defaultdict(list)
for f in facts.values():
    if f.get("home_chapter") != "25":
        continue
    for tok in re.findall(r"d25-\d{3}", f.get("note") or ""):
        got[tok].append(f["id"])
faq = json.load(open(W + "mine-faq.json"))
for did, ids in faq["demand"].items():
    got[did].extend(ids)
nf = {}
bd = json.load(open(W + "mine-behavior+decisions.json"))
for x in bd.get("demand_not_found", []):
    nf[x["id"]] = "mine-behavior+decisions: %s not found; looked in %s" % (x["part"], x["where_looked"])
nc = json.load(open(W + "mine-numbers+changes.json"))
for x in nc.get("not_found", []):
    did = x["demand"].split()[0]
    nf[did] = "mine-numbers+changes: not found: %s (%s)" % (x["claim"], x["result"])
for x in nc.get("partly_found", []):
    nf[x["demand"]] = "mine-numbers+changes: partly found: " + x["result"]

STOP = set("the a an and or of to in for on with is are be by that this it its your you can as from at not which what "
           "how does do when per vs versus there their than many much any each one and/or quote page say says".split())


def toks(s):
    return {t for t in re.findall(r"[a-z][a-z0-9-]+", s.lower()) if t not in STOP and len(t) > 2}


ch_live = [f for f in facts.values() if f.get("home_chapter") == "25" and f["status"] not in ("rejected", "superseded")]


def match(dm):
    q = toks(dm["question"])
    srcs = set(dm.get("look_in") or [])
    scored = []
    for f in ch_live:
        if dm.get("service") and f["service"] != dm["service"]:
            continue
        if srcs and not any(e["source_id"] in srcs for e in f["evidence"]):
            continue
        s = len(q & (toks(f["claim"]) | toks(f["id"].replace("-", " "))))
        if s >= 3:
            scored.append((s, f["id"]))
    scored.sort(reverse=True)
    return [i for _, i in scored[:6]]


over = json.load(open(W + "reg-demand-overrides.json")) if os.path.exists(W + "reg-demand-overrides.json") else {}
assign = over.pop("assign", {})
for fid, did in assign.items():
    j = live(fid)
    if not j:
        print("assign fact not live:", fid)
        continue
    if did in over and over[did].get("replace"):
        over[did]["facts"].append(j)
    else:
        got[did].append(j)
out = []
for dm in brief["demand"]:
    did = dm["id"]
    ids = list(dict.fromkeys(j for j in (live(i) for i in got.get(did, [])) if j))
    nts = []
    status = "found" if ids else None
    if not ids:
        ids = match(dm)
        if ids:
            status = "found"
            nts.append("register-25: facts matched by source page and question words")
    if did in nf:
        nts.append(nf[did])
        status = "partial" if ids else "not-found"
    if did in over:
        o = over[did]
        if o.get("replace"):
            ids = []
        for i in o.get("facts", []):
            j = live(i)
            if j and j not in ids:
                ids.append(j)
            elif not j:
                print("override fact not live:", did, i)
        status = o["status"]
        nts.append(o["note"])
    if status is None:
        status = "not-found"
    dm["status"] = status
    dm["facts"] = ids
    if nts:
        dm["note"] = " | ".join(n for n in nts if n)
    dm["registered_by"] = "register-25"
    out.append("%s %s [%s] %s\n   %s\n" % (did, status, dm.get("service"), dm["question"][:120], ", ".join(ids)))
# orphans: live chapter facts named by no demand item get the best-matching item of their service
named = {i for dm in brief["demand"] for i in dm["facts"]}
SKIP = {"d25-180", "d25-181", "d25-182", "d25-183", "d25-184", "d25-185", "d25-186", "d25-187", "d25-188",
        "d25-189", "d25-190", "d25-191", "d25-192", "d25-193", "d25-194", "d25-195", "d25-097"}
orph = []
for f in sorted(ch_live, key=lambda x: x["id"]):
    if f["id"] in named:
        continue
    best = None
    ft = toks(f["claim"]) | toks(f["id"].replace("-", " "))
    for dm in brief["demand"]:
        if dm["id"] in SKIP or dm.get("service") != f["service"]:
            continue
        is_change = "change" in dm["question"].lower()[:30]
        if (f["kind"] == "change") != is_change:
            continue
        s = len(toks(dm["question"]) & ft)
        if best is None or s > best[0]:
            best = (s, dm["id"])
    if best and best[0] >= 2:
        for dm in brief["demand"]:
            if dm["id"] == best[1]:
                dm["facts"].append(f["id"])
                if dm["status"] == "not-found":
                    dm["status"] = "partial"
        orph.append("%s -> %s (%d)" % (f["id"], best[1], best[0]))
    else:
        orph.append("%s -> NONE" % f["id"])
out.append("\nORPHANS (assigned by best question-word overlap)\n" + "\n".join(orph) + "\n")
open(W + "reg-demand-result.txt", "w").write("".join(out))
print(collections.Counter(d["status"] for d in brief["demand"]))
if "--write" in sys.argv:
    json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("wrote brief.v0.json")
