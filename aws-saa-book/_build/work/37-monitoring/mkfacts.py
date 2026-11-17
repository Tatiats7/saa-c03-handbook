#!/usr/bin/env python3
"""Expand compact fact specs into full fact inputs for `saa.py facts add`. Usage: mkfacts.py SPEC.json OUT.json
Spec row: id, k (kind), claim, q, v [[key, display(, spoken)]], sc, dm, adj, cond, ev [[source_id, quote(, table_header)]],
rel, d (demand id), n (extra note), t0, vol, ch (changed obj), ci (change_items), hard.
Checks that every quote is a substring of the normalised snapshot (a quick pre-check; the tool does the real one)."""
import json, sys, re, os

ROOT = "aws-saa-book"
brief = json.load(open(f"{ROOT}/_build/work/37-monitoring/brief.v0.json"))
BUL = {d["id"]: d["bullet"] for d in brief["demand"]}

sys.path.insert(0, f"{ROOT}/tools")
from saalib import common
norm = common.normalize_text

def snap(sid):
    base = f"{ROOT}/_build/corpus/snap/{sid}"
    meta = json.load(open(base + ".meta.json"))
    text = open(base + ".txt").read()
    return meta, text

def main(src, out):
    specs = json.load(open(src))
    res, bad = [], 0
    for s in specs:
        evs = []
        for e in s["ev"]:
            sid, quote = e[0], e[1]
            th = e[2] if len(e) > 2 else None
            meta, text = snap(sid)
            if norm(quote) not in norm(text):
                print("QUOTE NOT FOUND", s["id"], sid, quote[:80])
                bad += 1
            evs.append({"source_id": sid, "url": meta["url"], "quote": quote, "table_header": th})
        kind = s["k"]
        tier = 4 if kind == "case-study" else (2 if evs[0]["source_id"].startswith("www/") and "pricing" not in evs[0]["source_id"] else 1)
        if "tier" in s:
            tier = s["tier"]
        vals = []
        for v in s["v"]:
            d = {"key": v[0], "display": v[1]}
            if len(v) > 2:
                d["spoken"] = v[2]
            vals.append(d)
        f = {
            "id": s["id"], "service": next((k for k in ("health-dashboard", "managed-grafana", "managed-prometheus", "x-ray", "cloudwatch", "cloudtrail") if s["id"].startswith(k + "-")), "UNKNOWN"), "home_chapter": "37",
            "kind": kind, "claim": s["claim"], "question": s["q"], "values": vals,
            "qualifiers": {"scope": s.get("sc", ""), "default_or_max": s.get("dm", ""), "adjustable": s.get("adj", False), "condition": s.get("cond", "")},
            "evidence": evs, "source_tier": tier, "hard": s.get("hard", True), "tier0": s.get("t0", False),
            "volatility": s.get("vol", "stable"), "changed": s.get("ch"), "exam_relevance": s.get("rel", "core"),
            "bullets": [BUL[s["d"]]] if s.get("d") in BUL else [],
            "note": (s.get("d", "") + (" " + s["n"] if s.get("n") else "")).strip(),
        }
        if s.get("ci"):
            f["change_items"] = s["ci"]
        res.append(f)
    json.dump(res, open(out, "w"), indent=1)
    print(f"{len(res)} facts, {bad} quote problems -> {out}")

main(sys.argv[1], sys.argv[2])
