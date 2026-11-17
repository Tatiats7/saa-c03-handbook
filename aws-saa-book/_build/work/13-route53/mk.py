#!/usr/bin/env python3
"""Expands compact fact sources (src-behavior-NN.py defining F) into facts-behavior-NN.json for 'facts add'."""
import json, re, sys, importlib.util
from pathlib import Path

HERE = Path(__file__).parent
BASE = "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/"
ABS = re.compile(r"\b(only|always|never|cannot|must|by default|up to|at most|not supported)\b", re.I)
HARDKINDS = {"limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy"}


def url_for(p):
    if p.startswith("http"):
        return p
    return BASE + p + ".html"


def build(n):
    spec = importlib.util.spec_from_file_location("src", HERE / f"src-behavior-{n}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    out = []
    only = set(sys.argv[2:])
    for f in m.F:
        if only and f['id'] not in only:
            continue
        ev = []
        for e in f["e"]:
            if isinstance(e, str):
                e = (f["p"], e)
            item = {"url": url_for(e[0]), "quote": e[1]}
            if len(e) > 2 and e[2]:
                item["table_header"] = e[2]
            ev.append(item)
        kind = f.get("k", "behavior")
        hard = f.get("h")
        if hard is None:
            hard = kind in HARDKINDS or bool(ABS.search(f["c"]))
        if kind in HARDKINDS or ABS.search(f["c"]):
            hard = True
        vals = []
        for v in f["v"]:
            d = {"key": v[0], "display": v[1]}
            if len(v) > 2:
                d["spoken"] = v[2]
            vals.append(d)
        fact = {
            "id": f["id"], "service": "route53", "home_chapter": "13", "kind": kind,
            "claim": f["c"], "question": f["q"], "values": vals,
            "qualifiers": {"scope": f.get("s", ""), "default_or_max": f.get("d", ""),
                           "adjustable": f.get("a", False), "condition": f.get("n", "")},
            "evidence": ev, "source_tier": 1, "hard": hard, "tier0": f.get("t0", False),
            "volatility": f.get("vol", "stable"), "changed": f.get("ch"),
            "exam_relevance": f.get("rel", "core"), "bullets": f.get("b", []),
        }
        if f.get("ci"):
            fact["change_items"] = f["ci"]
        if f.get("note"):
            fact["note"] = f["note"]
        out.append(fact)
    path = HERE / (f"facts-behavior-{n}.json" if not only else f"facts-behavior-{n}-retry.json")
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(path, len(out))


if __name__ == "__main__":
    build(sys.argv[1])
