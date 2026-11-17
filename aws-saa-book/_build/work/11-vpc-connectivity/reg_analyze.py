"""register-11: read-only consistency checks over the live chapter 11 facts; writes reg-analysis.txt."""
import json, re, collections
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/11-vpc-connectivity/"
SVCS = ["vpc-peering", "transit-gateway", "vpc-endpoints", "privatelink"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if line:
            f = json.loads(line)
            if f["status"] not in ("rejected", "superseded"):
                facts[f["id"]] = f


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("`", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip().lower()

out = open(W + "reg-analysis.txt", "w")
sec = collections.defaultdict(list)
for i in sorted(facts):
    f = facts[i]
    c = f["claim"]
    quotes = [norm(e["quote"]) for e in f.get("evidence") or []]
    for v in f.get("values") or []:
        d = v.get("display", "")
        nd = norm(d)
        if not re.search(r"\d", d):
            if len(d.split()) > 8:
                sec["long-display"].append("%s [%s] %s" % (i, v.get("key"), d))
            if not any(nd in q for q in quotes):
                sec["display-not-in-quote"].append("%s [%s] %s" % (i, v.get("key"), d))
    neg = re.search(r"\b(not|no|n't|cannot|only|never|always|must|without|free)\b|n't", c, re.I)
    if not f["hard"]:
        if f["kind"] in ("pricing-dimension",):
            sec["soft-pricing"].append("%s :: %s" % (i, c[:160]))
        elif neg:
            sec["soft-with-absolute-like-word"].append("%s [%s] :: %s" % (i, f["kind"], c[:200]))
        elif re.search(r"\d", c):
            sec["soft-with-digit"].append("%s [%s] :: %s" % (i, f["kind"], c[:200]))
    q = f.get("qualifiers") or {}
    if f["hard"] and not (q.get("scope") or "").strip() and f["kind"] != "change":
        sec["hard-no-scope"].append("%s [%s] :: %s" % (i, f["kind"], c[:140]))
    if not f.get("question"):
        sec["no-question"].append(i)
    if not f.get("bullets"):
        sec["no-bullets"].append(i)
    sec["rel-%s" % f.get("exam_relevance")].append(i)
    sec["kind-%s" % f["kind"]].append(i)
    if f["hard"]:
        sec["hard"].append(i)
    # namespace check: claim about another service
    for e in f.get("evidence") or []:
        sid = e["source_id"]
        if i.startswith("vpc-peering") and ("tgw" in sid or "privatelink" in sid) and "peering" not in sid:
            sec["ns-check"].append("%s <- %s" % (i, sid))
        if i.startswith("transit-gateway") and ("peering/" in sid or "/privatelink/" in sid):
            sec["ns-check"].append("%s <- %s" % (i, sid))
        if i.startswith("vpc-endpoints") and ("/tgw/" in sid or "peering/" in sid):
            sec["ns-check"].append("%s <- %s" % (i, sid))
        if i.startswith("privatelink") and ("/tgw/" in sid or "peering/" in sid):
            sec["ns-check"].append("%s <- %s" % (i, sid))
for k in sorted(sec):
    if k.startswith("rel-") or k.startswith("kind-") or k == "hard":
        out.write("## %s: %d\n" % (k, len(sec[k])))
        continue
    out.write("## %s: %d\n" % (k, len(sec[k])))
    for x in sec[k]:
        out.write("  %s\n" % x)
out.close()
print({k: len(v) for k, v in sec.items()})
