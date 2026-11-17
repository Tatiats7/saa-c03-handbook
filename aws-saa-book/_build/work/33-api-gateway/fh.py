import json, sys, os
SNAP = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/corpus/snap/"
DG = "docs/apigateway/latest/developerguide/"
WP = "docs/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/"
_url = {}
def url(sid):
    if sid not in _url:
        _url[sid] = json.load(open(SNAP + sid + ".meta.json"))["url"]
    return _url[sid]
def ev(sid, quote, header=None):
    if not sid.startswith(("docs/", "www/")):
        sid = DG + sid
    return {"source_id": sid, "url": url(sid), "quote": quote, "table_header": header}
def F(id, kind, claim, q, displays, evid, scope="", dm="", hard=None, exam="core", bullets=(), tier0=False, cond="", adj=False, tier=1, vol="stable", spoken=None, note=None, svc=None, home="33"):
    hardkinds = ("limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy")
    import re as _re
    absw = ["only","always","never","cannot","must","by default","up to","at most","not supported"]
    if hard is None:
        hard = kind in hardkinds
    if any(_re.search(r"\b"+w+r"\b", claim.lower()) for w in absw) or _re.search(r"\d", claim):
        hard = True
    vals = []
    for i, d in enumerate(displays):
        v = {"key": "v%d" % (i + 1), "display": d}
        vals.append(v)
    pre = (svc or "api-gateway") + "-"
    d = {"id": id if id.startswith(pre) else pre + id, "service": svc or "api-gateway", "home_chapter": home, "kind": kind,
         "claim": claim, "question": q, "values": vals,
         "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
         "evidence": evid, "source_tier": 4 if kind == "case-study" else tier, "hard": hard, "tier0": tier0,
         "volatility": vol, "changed": None, "exam_relevance": exam, "bullets": list(bullets)}
    if note: d["note"] = note
    return d
def T(sid, row, header):
    return ev(sid, row, header)
def write(name, facts):
    p = os.path.join("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway", name)
    json.dump(facts, open(p, "w"), indent=1, ensure_ascii=False)
    print("wrote", p, len(facts))

def row(id, label, rest, http, header, q, bullets=("2.1.K1",), sid="http-api-vs-rest", extra=None, exam="core", tier0=False, rowlabel=None):
    rl = rowlabel or label
    rowtext = "| %s | %s | %s |" % (rl, rest, http)
    if rest == "Yes" and http == "No":
        claim = "%s is available for REST APIs, not HTTP APIs: the AWS comparison table lists Yes for REST APIs and No for HTTP APIs." % label
        disp = [label, "REST APIs, not HTTP APIs"]; kind = "restriction"
    elif rest == "No" and http == "Yes":
        claim = "%s is available for HTTP APIs, not REST APIs: the AWS comparison table lists No for REST APIs and Yes for HTTP APIs." % label
        disp = [label, "HTTP APIs, not REST APIs"]; kind = "capability"
    else:
        claim = "%s is available for both REST APIs and HTTP APIs: the AWS comparison table lists Yes for both." % label
        disp = [label, "REST APIs and HTTP APIs"]; kind = "capability"
    evid = [T(sid, rowtext, header)]
    if extra: evid.append(extra)
    return F(id, kind, claim, q, disp, evid, scope="REST APIs versus HTTP APIs", bullets=bullets, exam=exam, tier0=tier0, hard=True if kind=="restriction" else None)

def rowline(sid, prefix):
    if not sid.startswith(("docs/", "www/")):
        sid = DG + sid
    for l in open(SNAP + sid + ".txt", encoding="utf-8"):
        if l.startswith(prefix):
            return l.rstrip("\n")
    raise SystemExit("row not found: " + prefix)
