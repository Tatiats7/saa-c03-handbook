"""register-15: build amend patches from reg-spec.json into reg-patches/<id>.json.

Spec per fact id: {"display": {key: new display or null to drop}, "claim": str, "add_evidence": [{"source_id", "url", "quote"}],
"drop_evidence": [index], "source_tier": n, "exam_relevance": str, "note": str}
Checks: a display without a digit has at most 8 words and is held by a normalised quote of the fact;
a display with a digit is held by the claim or a quote (M7)."""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "aws-saa-book" / "tools"))
from saalib import common, lint  # noqa

W = ROOT / "aws-saa-book/_build/work/15-cloudfront"
spec = json.loads((W / "reg-spec.json").read_text())
rows = {}
for f in ["cloudfront", "global-accelerator"]:
    for l in open(ROOT / f"aws-saa-book/data/facts/{f}.jsonl"):
        r = json.loads(l); rows[r["id"]] = r
out = W / "reg-patches"
out.mkdir(exist_ok=True)
problems = []
for fid, s in spec.items():
    if fid.startswith("_"):
        continue
    r = rows[fid]
    patch = {}
    ev = [dict((k, e.get(k)) for k in ("source_id", "url", "quote", "table_header", "heading") if k in e) for e in r["evidence"]]
    if "drop_evidence" in s or "add_evidence" in s:
        ev = [e for i, e in enumerate(ev) if i not in set(s.get("drop_evidence", []))] + s.get("add_evidence", [])
        patch["evidence"] = ev
    claim = s.get("claim", r["claim"])
    if "claim" in s:
        patch["claim"] = claim
    if "display" in s:
        vals = []
        for v in r["values"]:
            if v["key"] in s["display"]:
                nd = s["display"][v["key"]]
                if nd is None:
                    continue
                v = dict(v, display=nd)
            vals.append(v)
        for k, nd in s["display"].items():
            if nd is not None and k not in [v["key"] for v in r["values"]]:
                vals.append({"key": k, "display": nd})
        patch["values"] = vals
    vals = patch.get("values", r["values"])
    qs = [common.normalize_text(e["quote"]) for e in ev]
    nc = common.normalize_text(claim)
    for v in vals:
        d = common.normalize_text(v["display"])
        if re.search(r"\d", d):
            if not (lint.holds_display(nc, d) or any(lint.holds_display(q, d) for q in qs)):
                problems.append(f"{fid}: digit display not held: {v['display']!r}")
        else:
            if len(v["display"].split()) > 8:
                problems.append(f"{fid}: display over 8 words: {v['display']!r}")
            if not any(lint.holds_display(q, d) for q in qs):
                problems.append(f"{fid}: display not in a quote: {v['display']!r}")
    for k in ("source_tier", "exam_relevance", "note", "volatility"):
        if k in s:
            patch[k] = s[k]
    (out / f"{fid}.json").write_text(json.dumps(patch, indent=1, ensure_ascii=False) + "\n")
print(f"{len([k for k in spec if not k.startswith('_')])} patches")
for p in problems:
    print("PROBLEM", p)
