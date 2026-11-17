"""Expand compact fact specs into full fact JSON for `saa.py facts add`. Usage: python3 mk-behavior.py SPEC.json OUT.json"""
import json, re, sys

HARD_KINDS = {"limit", "quota", "default", "restriction", "price", "sla", "change", "exam-policy"}
ABS = re.compile(r"\b(only|always|never|cannot|must|by default|up to|at most|not supported|can't|no more than)\b|\d", re.I)
SVC = {"site-to-site-vpn": "12", "direct-connect": "12", "client-vpn": "12"}


def url_for(sid):
    p = sid.split("/", 1)[1]
    if sid.startswith("docs/"):
        return "https://docs.aws.amazon.com/" + p + ".html"
    if sid.startswith("www/"):
        return "https://aws.amazon.com/" + p + "/"
    raise SystemExit("unknown source id " + sid)


def main(spec_path, out_path):
    specs = json.load(open(spec_path, encoding="utf-8"))
    out = []
    for s in specs:
        fid = s["id"]
        svc = next(k for k in SVC if fid.startswith(k + "-"))
        kind = s["kind"]
        claim = s["claim"]
        hard = s.get("hard")
        if hard is None:
            hard = kind in HARD_KINDS or bool(ABS.search(claim))
        vals = []
        for v in s["v"]:
            d = {"key": v[0], "display": v[1]}
            if len(v) > 2 and v[2]:
                d["spoken"] = v[2]
            vals.append(d)
        ev = []
        for e in s["ev"]:
            item = {"source_id": e[0], "url": url_for(e[0]), "quote": e[1], "table_header": e[2] if len(e) > 2 else None}
            ev.append(item)
        www = all(e[0].startswith("www/") or "whitepapers" in e[0] or "wellarchitected" in e[0] or "decision-guides" in e[0] for e in s["ev"])
        tier = s.get("tier", 4 if kind == "case-study" else (2 if www else 1))
        f = {
            "id": fid, "service": svc, "home_chapter": "12", "kind": kind, "claim": claim,
            "question": s["q"], "values": vals,
            "qualifiers": {"scope": s.get("scope", ""), "default_or_max": s.get("dm", ""), "adjustable": s.get("adj", False), "condition": s.get("cond", "")},
            "evidence": ev, "source_tier": tier, "hard": hard, "tier0": s.get("t0", False),
            "volatility": s.get("vol", "stable"), "changed": None,
            "exam_relevance": s.get("rel", "core"), "bullets": s.get("b", []), "note": s.get("d", ""),
        }
        out.append(f)
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out_path, len(out))


main(sys.argv[1], sys.argv[2])
