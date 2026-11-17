"""register-18: build amend patch files from reg-decisions.json.

Writes only under _build/work/18-lambda/reg-patches/. Reads data/facts/lambda.jsonl.
Checks every display of every patched fact: held by a normalised quote, and at most
8 words when it has no number (RULINGS 2026-10-11).
"""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/18-lambda/"
OUT = W + "reg-patches/"
os.makedirs(OUT, exist_ok=True)

facts = {}
for line in open(ROOT + "/data/facts/lambda.jsonl"):
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
                v.pop("spoken", None) if False else None
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

for i, s in D["scope"].items():
    p = P(i)
    if p is None:
        continue
    q = cur(i, "qualifiers")
    if q.get("scope"):
        problems.append("%s: scope not empty (%s)" % (i, q["scope"]))
    q["scope"] = s
    p["qualifiers"] = q

for i, m in D["patch"].items():
    p = P(i)
    if p is None:
        continue
    for k in ("claim", "note", "exam_relevance", "volatility"):
        if k in m:
            p[k] = m[k]
    if "evidence_quote" in m:
        ev = cur(i, "evidence")
        e = ev[0]
        p["evidence"] = [{"source_id": e["source_id"], "url": e["url"], "quote": m["evidence_quote"], "table_header": e.get("table_header")}]
    if "change_items_from" in m:
        ci = list(facts[i].get("change_items") or [])
        for c in facts[m["change_items_from"]].get("change_items") or []:
            if c not in ci:
                ci.append(c)
        p["change_items"] = ci

# bullets of superseded facts merge into the kept fact (same namespace only)
for o, n, _ in D["supersede"]:
    if n not in facts:
        continue
    b = cur(n, "bullets") or []
    nb = list(b)
    for x in facts[o].get("bullets") or []:
        if x not in nb:
            nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb

# display checks on every patched fact
NAME = re.compile(r"\b(S3|EC2|x86_64|arm64|Graviton2|IPv4|IPv6)\b")
NUMW = re.compile(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b", re.I)
for i, p in patch.items():
    vals = p.get("values", facts[i]["values"])
    ev = p.get("evidence", facts[i]["evidence"])
    claim = p.get("claim", facts[i]["claim"])
    nq = [normalize_text(e["quote"]) for e in ev]
    seen = set()
    for v in vals:
        d = v["display"]
        dn = normalize_text(d)
        if dn in seen:
            problems.append("%s: duplicate display %r" % (i, d))
        seen.add(dn)
        stripped = NAME.sub("", d)
        numeric = bool(re.search(r"\d", stripped)) or bool(NUMW.search(stripped))
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
