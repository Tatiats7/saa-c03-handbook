import json, os, re, sys

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
SNAP = ROOT + "/_build/corpus/snap/"
HOME = {"backup": "24", "organizations": "04", "ebs": "22", "s3": "21", "s3-glacier": "21", "rds": "26",
        "aurora": "27", "dynamodb": "28", "efs": "23", "fsx": "23", "control-tower": "04", "guardduty": "09",
        "well-architected": "02"}


sys.path.insert(0, ROOT + "/tools")
from saalib.common import normalize_text as norm

def url_of(sid):
    m = json.load(open(SNAP + sid + ".meta.json"))
    return m["url"], m.get("title")


def E(sid, quote, header=None):
    txt = open(SNAP + sid + ".txt").read()
    if norm(quote) not in norm(txt):
        print("QUOTE NOT FOUND", sid, quote[:80], file=sys.stderr)
    url, _ = url_of(sid)
    if len(quote.split()) > 80:
        print("QUOTE TOO LONG", len(quote.split()), quote[:60], file=sys.stderr)
    return {"source_id": sid, "url": url, "quote": quote, "table_header": header}


def F(id, kind, claim, question, displays, ev, scope="", cond="", dm="", adj=False, hard=None, tier0=False,
      rel="core", service="backup", vol="stable", bullets=None, tier=1, note=None):
    if hard is None:
        hard = True
    f = {
        "id": id, "service": service, "home_chapter": HOME[service], "kind": kind, "claim": claim,
        "question": question,
        "values": [{"key": "v%d" % (i + 1), "display": d} for i, d in enumerate(displays)],
        "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
        "evidence": ev, "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol, "changed": None,
        "exam_relevance": rel,
    }
    if bullets:
        f["bullets"] = bullets
    if note:
        f["note"] = note
    return f


def dump(name, facts):
    p = ROOT + "/_build/work/24-backup/" + name
    json.dump(facts, open(p, "w"), indent=1, ensure_ascii=False)
    print("wrote", p, len(facts))


def ROW(sid, table, row):
    from saalib import corpus
    txt = open(SNAP + sid + ".txt").read()
    t = corpus.parse_tables(txt)[table]
    r = t["rows"][row]
    url, _ = url_of(sid)
    return {"source_id": sid, "url": url, "quote": r["text"], "table_header": t["header_text"]}
