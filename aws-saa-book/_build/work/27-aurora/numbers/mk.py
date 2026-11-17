import json, os, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
OUT = ROOT + "/_build/work/27-aurora/numbers/"


def url_of(src):
    meta = json.load(open(f"{ROOT}/_build/corpus/snap/{src}.meta.json"))
    return meta["url"]


def F(id, kind, claim, question, values, scope, dm, adj, src, quote, cond="", exam="core", bullets=(),
      vol="stable", header=None, note="", svc="aurora", changed=None, change_items=(), hard=True, more=()):
    vals = []
    for i, v in enumerate(values):
        if isinstance(v, str):
            vals.append({"key": f"v{i+1}", "display": v})
        else:
            d = {"key": v[0], "display": v[1]}
            if len(v) > 2 and v[2]:
                d["spoken"] = v[2]
            vals.append(d)
    ev = [{"source_id": src, "url": url_of(src), "quote": quote, "table_header": header}]
    for m in more:
        ev.append({"source_id": m[0], "url": url_of(m[0]), "quote": m[1], "table_header": (m[2] if len(m) > 2 else None)})
    f = {"id": id, "service": svc, "home_chapter": "27", "kind": kind, "claim": claim, "question": question,
         "values": vals,
         "qualifiers": {"scope": scope, "default_or_max": dm, "adjustable": adj, "condition": cond},
         "evidence": ev, "source_tier": 1, "hard": hard, "tier0": False, "volatility": vol,
         "exam_relevance": exam, "bullets": list(bullets), "change_items": list(change_items), "note": note}
    if changed:
        f["changed"] = changed
    return f


def write(name, facts):
    json.dump(facts, open(OUT + name, "w"), indent=1)
    print(name, len(facts))
