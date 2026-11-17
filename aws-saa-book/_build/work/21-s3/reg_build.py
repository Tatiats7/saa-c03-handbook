"""register-21: build amend patch files from reg-decisions.json (writes only under _build/work/21-s3/reg-patches)."""
import json, re, sys, copy, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text  # noqa: E402

W = ROOT + "/_build/work/21-s3/"
OUTDIR = W + "reg-patches/"
os.makedirs(OUTDIR, exist_ok=True)

facts = {}
for p in [ROOT + "/data/facts/s3.jsonl", ROOT + "/data/facts/s3-glacier.jsonl"]:
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f

D = json.load(open(W + "reg-decisions.json"))
problems = []
superseded = {o: n for o, n, _ in D["supersede"]}
rejected = {r[0] for r in D["reject"]}
for cf, keep, both, _ in D["resolve"]:
    pass

# targets of edits
patch = {}  # id -> dict of fields


def P(i):
    if i not in facts:
        problems.append("unknown fact " + i)
        return None
    if i in superseded or i in rejected:
        problems.append("edit on a fact that is superseded/rejected: " + i)
    if i not in patch:
        patch[i] = {}
    return patch[i]


def cur(i, field):
    p = patch.get(i, {})
    return copy.deepcopy(p[field]) if field in p else copy.deepcopy(facts[i][field])


# displays
for i, m in D["display"].items():
    p = P(i)
    if p is None:
        continue
    vals = cur(i, "values")
    keys = [v["key"] for v in vals]
    for k, d in m.items():
        if k not in keys:
            problems.append("%s: no value key %s" % (i, k))
            continue
        if d is None:
            vals = [v for v in vals if v["key"] != k]
        else:
            for v in vals:
                if v["key"] == k:
                    v["display"] = d
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
    if "claim" in m:
        p["claim"] = m["claim"]
    if "scope" in m or "condition" in m:
        q = cur(i, "qualifiers")
        if "scope" in m:
            q["scope"] = m["scope"]
        if "condition" in m:
            q["condition"] = m["condition"]
        p["qualifiers"] = q
    if "add_values" in m:
        vals = cur(i, "values")
        for k, d in m["add_values"]:
            vals.append({"key": k, "display": d})
        p["values"] = vals
    if "drop_values" in m:
        p["values"] = [v for v in cur(i, "values") if v["key"] not in m["drop_values"]]
    if "drop_evidence" in m or "add_evidence_from" in m:
        ev = cur(i, "evidence")
        if "drop_evidence" in m:
            ev = [e for n, e in enumerate(ev) if n not in m["drop_evidence"]]
        for src, n in m.get("add_evidence_from", []):
            ev.append(copy.deepcopy(facts[src]["evidence"][n]))
        p["evidence"] = ev
    if "change_items_from" in m:
        ci = list(facts[i].get("change_items") or [])
        for c in facts[m["change_items_from"]].get("change_items") or []:
            if c not in ci:
                ci.append(c)
        p["change_items"] = ci
    if "volatility" in m:
        p["volatility"] = m["volatility"]

# bullets merge from superseded / conflict-rejected facts
merge_into = {}
for o, n, _ in D["supersede"]:
    merge_into.setdefault(n, []).append(o)
conf = {}
for line in open(ROOT + "/_build/facts/conflicts.jsonl"):
    if line.strip():
        c = json.loads(line)
        conf[c["id"]] = c
for cf, keep, both, _ in D["resolve"]:
    if keep:
        other = [x for x in conf[cf]["facts"] if x != keep][0]
        merge_into.setdefault(keep, []).append(other)
for n, olds in merge_into.items():
    if n in superseded:
        problems.append("supersede target is itself superseded: " + n)
    b = cur(n, "bullets")
    nb = list(b)
    for o in olds:
        for x in facts[o].get("bullets") or []:
            if x not in nb:
                nb.append(x)
    if nb != b:
        P(n)["bullets"] = nb

# validation of displays (every live fact that stays)
conf_rejected = set()
for cf, keep, both, _ in D["resolve"]:
    if keep:
        conf_rejected.update(x for x in conf[cf]["facts"] if x != keep)
for i in sorted(facts):
    f = facts[i]
    if f["status"] in ("rejected", "superseded") or i in superseded or i in rejected or i in conf_rejected:
        continue
    p = patch.get(i, {})
    vals = p.get("values", f["values"])
    claim = p.get("claim", f["claim"])
    ev = p.get("evidence", f["evidence"])
    quotes = [normalize_text(e.get("quote") or "") for e in ev] + [normalize_text(e.get("table_header") or "") for e in ev]
    nc = normalize_text(claim)
    seen = set()
    for v in vals:
        d = v["display"]
        nd = normalize_text(d)
        if nd in seen:
            problems.append("%s: duplicate display %s" % (i, d))
        seen.add(nd)
        inq = any(nd in q for q in quotes)
        if not inq and nd not in nc:
            problems.append("%s: display not held: %s" % (i, d))
        if not re.search(r"\d", re.sub(r"\b(S3|EC2|Route 53|IPv4|IPv6|AES-256)\b", "", d)):
            if len(d.split()) > 8:
                problems.append("%s: number-free display over 8 words: %s" % (i, d))
            if not inq:
                problems.append("%s: number-free display not verbatim in a quote: %s" % (i, d))
    if not vals:
        problems.append("%s: no values left" % i)

for i, p in patch.items():
    json.dump(p, open(OUTDIR + i + ".json", "w"), indent=1, ensure_ascii=False)

print("patches", len(patch))
print("problems", len(problems))
for x in problems:
    print(" -", x)
json.dump(sorted(patch), open(W + "reg-patch-ids.json", "w"), indent=0)
