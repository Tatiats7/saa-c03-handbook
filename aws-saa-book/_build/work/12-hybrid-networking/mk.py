"""Helper that builds fact dicts for facts add (work file of the miner, not part of the book)."""
import json
import re

SNAP = "aws-saa-book/_build/corpus/snap/"


def _meta(sid):
    return json.load(open(SNAP + sid + ".meta.json"))


def ev(sid, quote, header=None):
    m = _meta(sid)
    txt = open(SNAP + sid + ".txt").read()
    flat = re.sub(r"\s+", " ", txt)
    if re.sub(r"\s+", " ", quote) not in flat:
        print("WARN quote not literally in", sid, ":", quote[:70])
    return {"source_id": sid, "url": m["url"], "quote": quote, "table_header": header}


def fact(id, service, kind, claim, question, values, scope, dm, adj, evidence, cond="", tier=1,
         vol="stable", changed=None, change_items=None, exam="extended", bullets=None, note="", tier0=False,
         derivation=None):
    """values: list of (key, display, spoken)."""
    f = {
        "id": id, "service": service, "home_chapter": "12", "kind": kind, "claim": claim, "question": question,
        "values": [{"key": k, "display": d, "spoken": s} for k, d, s in values],
        "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
        "evidence": evidence, "source_tier": tier, "hard": True, "tier0": tier0, "volatility": vol,
        "changed": changed, "exam_relevance": exam, "bullets": bullets or [], "note": note,
    }
    if change_items:
        f["change_items"] = change_items
    if derivation:
        f["derivation"] = derivation
    return f


def dump(facts, name):
    for f in facts:
        for v in f["values"]:
            if not v.get("spoken"):
                v.pop("spoken", None)
    path = "aws-saa-book/_build/work/12-hybrid-networking/" + name
    json.dump(facts, open(path, "w"), indent=1, ensure_ascii=False)
    print(len(facts), "facts ->", path)


def cid(svc, text, src=None):
    """change item key for the row whose title contains text (svc: dx, cvpn, s2s)."""
    rows = json.load(open("aws-saa-book/_build/work/12-hybrid-networking/changes-%s.json" % svc))["rows"]
    hits = [r for r in rows if text.lower() in r["title"].lower() and (src is None or r["source"] == src)]
    if len(hits) != 1:
        raise SystemExit("cid %s %r: %d hits" % (svc, text, len(hits)))
    r = hits[0]
    return r["id"] if r["source"] == "whatsnew" else "%s#%s" % (r["history_source_id"], r["line"])


def row(sid, prefix):
    """the stripped snapshot line that starts with prefix (a table row)."""
    hits = [l.strip() for l in open(SNAP + sid + ".txt").read().split("\n") if l.strip().startswith(prefix)]
    if len(hits) != 1:
        raise SystemExit("row %s %r: %d hits" % (sid, prefix, len(hits)))
    return hits[0]
