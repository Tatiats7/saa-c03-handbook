"""register-15: print fact blocks for pairs of a kind (DUP or SIM) from reg-analysis.txt into reg-pairs-<kind>.txt."""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
W = ROOT / "aws-saa-book/_build/work/15-cloudfront"
kind = sys.argv[1]
rows = {json.loads(l)["id"]: json.loads(l) for f in ["cloudfront", "global-accelerator"] for l in open(ROOT / f"aws-saa-book/data/facts/{f}.jsonl")}
def block(i):
    r = rows[i]
    q = r.get("qualifiers") or {}
    s = [f"  [{i}] {r['kind']} hard={r['hard']} rel={r['exam_relevance']} tier={r['source_tier']} st={r['status']}",
         f"     C: {r['claim']}", f"     D: {[v['display'] for v in r['values']]} S: {q.get('scope')}"]
    for e in r["evidence"]:
        s.append(f"     Q[{e['source_id'].split('/')[-1]} @{(e.get('match') or [0])[0]}]: {e['quote'][:400]}")
    return "\n".join(s)
out = []
for line in open(W / "reg-analysis.txt"):
    p = line.split()
    if p and p[0] == kind:
        out.append(f"== {p[1]} / {p[2]} {' '.join(p[3:])}")
        out.append(block(p[1])); out.append(block(p[2]))
(W / f"reg-pairs-{kind}.txt").write_text("\n".join(out) + "\n")
print(len(out))
