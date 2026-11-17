"""Expand a compact FAQ fact spec (JSON list) into the facts-add input shape.

Usage: python3 expand.py SPEC.json OUT.json
Spec item keys: id, kind, claim, q, d (displays), ev (list of [src, quote] or [src, quote, heading]),
optional: scope, dom, adj, cond, hard, rel, b (bullets), vol, note, tier0.
src: f = www/rds/faqs, p = www/rds/proxy.
"""
import json
import re
import sys

SRC = {
    "f": ("www/rds/faqs", "https://aws.amazon.com/rds/faqs/"),
    "p": ("www/rds/proxy", "https://aws.amazon.com/rds/proxy/"),
}


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60].strip("-") or "value"


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = []
    for it in spec:
        fid = it["id"]
        service = "rds-proxy" if fid.startswith("rds-proxy-") else "rds"
        values = []
        seen = set()
        for d in it["d"]:
            k = slug(d)
            while k in seen:
                k += "-x"
            seen.add(k)
            values.append({"key": k, "display": d})
        ev = []
        for e in it["ev"]:
            sid, url = SRC[e[0]]
            item = {"source_id": sid, "url": url, "quote": e[1], "table_header": None}
            if len(e) > 2:
                item["heading"] = e[2]
            ev.append(item)
        out.append({
            "id": fid,
            "service": service,
            "home_chapter": "26",
            "kind": it["kind"],
            "claim": it["claim"],
            "question": it["q"],
            "values": values,
            "qualifiers": {
                "scope": it.get("scope", ""),
                "default_or_max": it.get("dom", ""),
                "adjustable": it.get("adj", False),
                "condition": it.get("cond", ""),
            },
            "evidence": ev,
            "source_tier": 2,
            "hard": it.get("hard", True),
            "tier0": it.get("tier0", False),
            "volatility": it.get("vol", "stable"),
            "changed": None,
            "exam_relevance": it.get("rel", "core"),
            "bullets": it.get("b", []),
            "note": it.get("note"),
        })
    json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(len(out), "facts written to", sys.argv[2])


main()
