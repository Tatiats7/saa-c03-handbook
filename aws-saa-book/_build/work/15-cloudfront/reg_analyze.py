"""register-15: read-only analysis of chapter 15 facts. Writes reg-analysis.txt and reg-table.txt."""
import json, re, sys, collections, itertools, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "aws-saa-book" / "tools"))
from saalib import common, lint  # noqa

W = ROOT / "aws-saa-book/_build/work/15-cloudfront"
rows = [json.loads(l) for f in ["cloudfront", "global-accelerator"] for l in open(ROOT / f"aws-saa-book/data/facts/{f}.jsonl")]
live = [r for r in rows if r["status"] not in ("rejected", "superseded")]
out = []
def p(*a): out.append(" ".join(str(x) for x in a))

# a) displays
p("== displays")
for r in live:
    qs = [common.normalize_text(e["quote"]) for e in r["evidence"]]
    for v in r["values"]:
        d = v["display"]
        if not re.search(r"\d", d):
            nw = len(d.split())
            inq = any(lint.holds_display(q, common.normalize_text(d)) for q in qs)
            if nw > 8 or not inq:
                p("DISP", r["id"], f"words={nw}", f"inquote={inq}", repr(d))
    if not r["values"]:
        p("NOVAL", r["id"])

# d) qualifiers
p("== qualifiers")
for r in live:
    q = r.get("qualifiers") or {}
    if not (q.get("scope") or "").strip():
        p("NOSCOPE", r["id"], r["kind"])

# e) namespace
p("== namespace (evidence page families)")
for r in live:
    srcs = [e["source_id"] for e in r["evidence"]]
    fam = "cloudfront" if r["service"] == "cloudfront" else "global-accelerator"
    keys = {"cloudfront": ["cloudfront", "CloudFront"], "global-accelerator": ["global-accelerator", "globalaccelerator"]}[fam]
    if not any(any(k in s for k in keys) for s in srcs):
        p("NS", r["id"], srcs)

# b) duplicates by overlapping quote
p("== same-span duplicates")
spans = collections.defaultdict(list)
for r in live:
    for e in r["evidence"]:
        spans[e["source_id"]].append((e.get("match") or [0, 0], r["id"], common.normalize_text(e["quote"])))
pairs = set()
for sid, lst in spans.items():
    for (m1, a, q1), (m2, b, q2) in itertools.combinations(lst, 2):
        if a == b:
            continue
        if (m1[0] < m2[1] and m2[0] < m1[1]) or q1 == q2:
            pairs.add(tuple(sorted((a, b))))
for a, b in sorted(pairs):
    p("DUP", a, b)

# c) similar claims (same numbers)
p("== similar claims")
def toks(c):
    return {t for t in re.findall(r"[a-z]+", re.sub(r"\S*\d\S*", " ", (c or "").lower())) if len(t) > 2}
bys = collections.defaultdict(list)
for r in live:
    bys[r["service"]].append(r)
for s, lst in bys.items():
    for a, b in itertools.combinations(lst, 2):
        ta, tb = toks(a["claim"]), toks(b["claim"])
        if ta and tb and len(ta & tb) / len(ta | tb) >= 0.5 and tuple(sorted((a["id"], b["id"]))) not in pairs:
            p("SIM", a["id"], b["id"], round(len(ta & tb) / len(ta | tb), 2))

(W / "reg-analysis.txt").write_text("\n".join(out) + "\n")

# table for reading
t = []
for r in sorted(live, key=lambda r: r["id"]):
    q = r.get("qualifiers") or {}
    t.append(f"### {r['id']} | {r['kind']} hard={r['hard']} rel={r['exam_relevance']} vol={r['volatility']} tier={r['source_tier']} rev={r['rev']}")
    t.append(f"  C: {r['claim']}")
    t.append(f"  D: {[v['display'] for v in r['values']]}  S: {q.get('scope')}|{q.get('default_or_max')}|{q.get('adjustable')}|{q.get('condition')}")
    for e in r["evidence"]:
        t.append(f"  Q[{e['source_id'].split('/')[-1]}]: {e['quote'][:260]}")
(W / "reg-table.txt").write_text("\n".join(t) + "\n")
print(len(out), "analysis lines;", len(live), "facts in table")
