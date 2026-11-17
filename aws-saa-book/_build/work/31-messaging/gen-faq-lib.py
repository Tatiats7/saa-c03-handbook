"""Helper for the mine-31-faq lens: builds fact JSON files from compact specs.
Quotes are re-cut from the page snapshot so that curly quotes and dashes stay verbatim."""
import json, re, sys
ROOT = "aws-saa-book/_build/corpus/snap/"
SRC = {
    "sqs": ("www/sqs/faqs", "https://aws.amazon.com/sqs/faqs/"),
    "sns": ("www/sns/faqs", "https://aws.amazon.com/sns/faqs/"),
    "eb": ("www/eventbridge/faqs", "https://aws.amazon.com/eventbridge/faqs/"),
}
MAP = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})
_text = {}
def text(src):
    if src not in _text:
        _text[src] = open(ROOT + SRC[src][0] + ".txt", encoding="utf-8").read()
    return _text[src]
def recut(src, q):
    t = text(src)
    if q in t:
        return q
    nt = t.translate(MAP)
    nq = q.translate(MAP)
    i = nt.find(nq)
    if i < 0:
        return None
    return t[i:i + len(nq)]

ABS = re.compile(r"\b(only|always|never|cannot|must|by default|up to|at most|not supported)\b", re.I)
HARDK = {"limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy"}
errors = []
def F(service, fid, kind, claim, q, disp, quotes, scope, bullets, rel="core", dm="", adj=False, cond="",
      src="sqs", hard=None, vol="stable", note=None, tier0=False, qsrc=None):
    ev = []
    qs = quotes if isinstance(quotes, list) else [quotes]
    for i, qt in enumerate(qs):
        s = src if not qsrc else qsrc[i]
        r = recut(s, qt)
        if r is None:
            errors.append("QUOTE NOT FOUND %s: %s" % (fid, qt[:70]))
            r = qt
        ev.append({"source_id": SRC[s][0], "url": SRC[s][1], "quote": r, "table_header": None})
    if hard is None:
        hard = kind in HARDK or bool(ABS.search(claim)) or bool(re.search(r"\d", claim))
    vals = []
    for k, d in enumerate(disp):
        joined = " ".join(e["quote"] for e in ev)
        if d.translate(MAP) not in (joined + " " + claim).translate(MAP):
            errors.append("DISPLAY NOT HELD %s: %s" % (fid, d))
        vals.append({"key": "v%d" % (k + 1), "display": d})
    if len(disp) < 2:
        errors.append("FEWER THAN 2 DISPLAYS %s" % fid)
    f = {"id": service + "-" + fid, "service": service, "home_chapter": "31", "kind": kind, "claim": claim,
         "question": q, "values": vals,
         "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
         "evidence": ev, "source_tier": 2, "hard": hard, "tier0": tier0, "volatility": vol, "changed": None,
         "exam_relevance": rel, "bullets": bullets}
    if note:
        f["note"] = note
    return f

def emit(name, facts):
    ids = [f["id"] for f in facts]
    assert len(ids) == len(set(ids)), "duplicate ids in " + name
    path = "aws-saa-book/_build/work/31-messaging/" + name
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("[\n" + ",\n".join(json.dumps(f, ensure_ascii=False) for f in facts) + "\n]\n")
    print("wrote", path, len(facts))
    for e in errors:
        print(e)
    errors.clear()
