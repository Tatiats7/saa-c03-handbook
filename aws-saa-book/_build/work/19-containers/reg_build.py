"""register-19: build amend patch files from reg-decisions.json.

Writes only under _build/work/19-containers/reg-patches/. Reads data/facts/<service>.jsonl.
Checks every display of every live fact after the patches: held by a normalised quote,
and at most 8 words when it has no digit (RULINGS 2026-10-11, SPEC number_free_display_rule).
"""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/19-containers/"
OUT = W + "reg-patches/"
os.makedirs(OUT, exist_ok=True)
SVCS = ["ecr", "ecs", "ecs-anywhere", "eks", "eks-anywhere", "eks-distro", "fargate"]

facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

D = json.load(open(W + "reg-decisions.json"))
problems = []
gone = {o for o, n, _ in D["supersede"]} | {r[0] for r in D["reject"]}
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
    changed = False
    for old, new in m.items():
        hit = [v for v in vals if v["display"] == old]
        if not hit:
            problems.append("%s: no display %r" % (i, old))
            continue
        if new is None:
            vals = [v for v in vals if v["display"] != old]
            changed = True
        elif new != old:
            for v in hit:
                v["display"] = new
                v.pop("spoken", None)
            changed = True
    if changed:
        p["values"] = vals
    if not vals:
        problems.append("%s: no display left" % i)

for i, lst in D.get("add_values", {}).items():
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
    for k in ("claim", "note", "exam_relevance", "volatility", "qualifiers", "hard", "kind"):
        if k in m:
            p[k] = m[k]
    if "evidence_keep" in m:
        ev = cur(i, "evidence")
        p["evidence"] = [{"source_id": ev[j]["source_id"], "url": ev[j]["url"], "quote": ev[j]["quote"],
                          "table_header": ev[j].get("table_header")} for j in m["evidence_keep"]]

# bullets of superseded facts merge into the kept fact
for o, n, _ in D["supersede"]:
    if n not in facts or o not in facts:
        problems.append("supersede pair unknown: %s -> %s" % (o, n))
        continue
    if n in gone:
        problems.append("supersede target leaves: %s" % n)
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in facts[o].get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb


def check(i, vals, ev, claim, tag):
    nq = [normalize_text(e["quote"]) for e in ev]
    seen = set()
    for v in vals:
        d = v["display"]
        dn = normalize_text(d)
        if dn in seen:
            problems.append("%s %s: duplicate display %r" % (tag, i, d))
        seen.add(dn)
        numeric = bool(re.search(r"\d", d))
        if not numeric:
            if not any(dn in q for q in nq):
                problems.append("%s %s: number-free display not in a quote %r" % (tag, i, d))
            if len(d.split()) > 8:
                problems.append("%s %s: display over 8 words %r" % (tag, i, d))
        else:
            if not any(dn in q for q in nq) and dn not in normalize_text(claim):
                problems.append("%s %s: display in neither quote nor claim %r" % (tag, i, d))


for i, f in sorted(facts.items()):
    if f["status"] in ("rejected", "superseded") or i in gone or f.get("home_chapter") != "19":
        continue
    p = patch.get(i, {})
    check(i, p.get("values", f["values"]), p.get("evidence", f["evidence"]), p.get("claim", f["claim"]),
          "PATCHED" if i in patch else "UNTOUCHED")

for name in os.listdir(OUT):
    os.remove(OUT + name)
for i, p in sorted(patch.items()):
    json.dump(p, open(OUT + i + ".json", "w"), indent=1, ensure_ascii=False)
json.dump(sorted(patch), open(W + "reg-patch-ids.json", "w"), indent=1)
print("patches", len(patch))
print("problems", len(problems))
for x in problems:
    print(" ", x)
