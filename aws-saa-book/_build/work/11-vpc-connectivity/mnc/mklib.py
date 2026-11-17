import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))  # aws-saa-book
SNAP = os.path.join(ROOT, "_build", "corpus", "snap")
TGWQ = "docs/vpc/latest/tgw/transit-gateway-quotas"
EPQ = "docs/vpc/latest/privatelink/vpc-limits-endpoints"
TGWP = "www/transit-gateway/pricing"
PLP = "www/privatelink/pricing"
PLF = "www/privatelink/faqs"
errors = []


def _text(src):
    with open(os.path.join(SNAP, src + ".txt"), encoding="utf-8") as f:
        return f.read()


def _meta(src):
    with open(os.path.join(SNAP, src + ".meta.json"), encoding="utf-8") as f:
        return json.load(f)


def ev(src, quote, header=None):
    t = _text(src)
    if quote not in t:
        errors.append((src, quote[:90]))
    d = {"source_id": src, "url": _meta(src)["url"], "quote": quote, "table_header": header}
    return d


def F(i, service, kind, claim, question, values, evidence, scope="", dom="", adj=False, cond="", rel="extended",
      bullets=("4.4.K6",), hard=True, tier0=False, vol="stable", changed=None, items=None, note=None, tier=1):
    d = {
        "id": i, "service": service, "home_chapter": "11", "kind": kind, "claim": claim, "question": question,
        "values": [{"key": k, "display": dd, **({"spoken": s} if s else {})} for k, dd, s in values],
        "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
        "evidence": evidence, "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol,
        "changed": changed, "exam_relevance": rel, "bullets": list(bullets), "note": note,
    }
    if items:
        d["change_items"] = items
    return d


def write(name, facts):
    path = os.path.join(HERE, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(facts, f, indent=1, ensure_ascii=False)
    print(name, len(facts), "facts")
    if errors:
        print("QUOTES NOT FOUND:")
        for e in errors:
            print("  ", e)
        errors.clear()
