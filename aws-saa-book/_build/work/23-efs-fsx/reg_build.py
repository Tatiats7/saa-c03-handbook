"""register-23: build amend patch files from reg-decisions.json (adapted from register-18).

Writes only under _build/work/23-efs-fsx/reg-patches/. Reads data/facts/efs.jsonl and fsx.jsonl.
Checks every display of every patched fact: held by a normalised quote, and at most 8 words when it
has no number (RULINGS 2026-10-11). Also gives bullets to live facts that have none.
"""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/23-efs-fsx/"
OUT = W + "reg-patches/"
os.makedirs(OUT, exist_ok=True)
for name in os.listdir(OUT):
    os.remove(OUT + name)

facts = {}
for svc in ("efs", "fsx"):
    for line in open(ROOT + "/data/facts/%s.jsonl" % svc):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

D = json.load(open(W + "reg-decisions.json"))
problems = []
gone = {o for o, n, _ in D["supersede"]} | {r[0] for r in D["reject"]}
for o, n, _ in D["supersede"]:
    if n in gone:
        problems.append("supersede target leaves too: %s -> %s" % (o, n))
    if o not in facts or n not in facts:
        problems.append("unknown in supersede: %s -> %s" % (o, n))
patch = {}


def P(i):
    if i not in facts:
        problems.append("unknown fact " + i)
        return None
    if i in gone:
        problems.append("edit on a fact that leaves: " + i)
    return patch.setdefault(i, {})


def cur(i, field):
    p = patch.get(i, {})
    return copy.deepcopy(p[field]) if field in p else copy.deepcopy(facts[i].get(field))


for i, m in D["display"].items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    for old, new in m.items():
        hit = [v for v in vals if v["display"] == old]
        if not hit:
            problems.append("%s: no display %r" % (i, old))
            continue
        if new is None:
            vals = [v for v in vals if v["display"] != old]
        else:
            for v in hit:
                v["display"] = new
                v.pop("spoken", None)
    p["values"] = vals

for i, lst in D["add_values"].items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    for k, d in lst:
        if any(v["key"] == k for v in vals):
            problems.append("%s: key exists %s" % (i, k))
        vals.append({"key": k, "display": d})
    p["values"] = vals

for i, m in D["patch"].items():
    p = P(i)
    if p is None:
        continue
    for k in ("claim", "note", "exam_relevance", "volatility"):
        if k in m:
            p[k] = m[k]

# bullets of superseded facts merge into the kept fact
for o, n, _ in D["supersede"]:
    if n not in facts or o not in facts:
        continue
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in facts[o].get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb

# live facts of chapter 23 without bullets: assign by topic
RULES = [
    (r"backup|replicat|failover|durab|multi-az|single-az|snapshot", "2.2.K11"),
    (r"datasync|transfer-family|onprem|on-premises|vpn|direct-connect|tgw|peering|migrat", "2.2.S7"),
    (r"price|pricing|billing|cost|charge", "4.1.S10"),
    (r"limit|quota|throughput|iops|latency|performance", "3.1.S1"),
]
for i, f in facts.items():
    if f.get("home_chapter") != "23" or f["status"] in ("rejected", "superseded") or i in gone:
        continue
    if cur(i, "bullets"):
        continue
    bul = "3.1.K2"
    for rx, b in RULES:
        if re.search(rx, i):
            bul = b
            break
    P(i)["bullets"] = [bul]

# display checks on every patched fact
for i, p in patch.items():
    vals = p.get("values", facts[i]["values"])
    ev = facts[i]["evidence"]
    claim = p.get("claim", facts[i]["claim"])
    nq = [normalize_text(e["quote"]) for e in ev]
    seen = set()
    for v in vals:
        d = v["display"]
        dn = normalize_text(d)
        if dn in seen:
            problems.append("%s: duplicate display %r" % (i, d))
        seen.add(dn)
        stripped = re.sub(r"\b[A-Za-z]+[0-9][A-Za-z0-9.]*\b", "", d)
        numeric = bool(re.search(r"\d", stripped)) or bool(re.search(
            r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half|percent)\b", stripped, re.I))
        if not any(dn in q for q in nq):
            if numeric and dn in normalize_text(claim):
                continue
            problems.append("%s: display not in a quote %r" % (i, d))
        if not numeric and len(d.split()) > 8:
            problems.append("%s: display over 8 words %r" % (i, d))

for i, p in sorted(patch.items()):
    json.dump(p, open(OUT + i + ".json", "w"), indent=1, ensure_ascii=False)
json.dump(sorted(patch), open(W + "reg-patch-ids.json", "w"), indent=1)
print("patches", len(patch))
print("problems", len(problems))
for x in problems:
    print(" ", x)
