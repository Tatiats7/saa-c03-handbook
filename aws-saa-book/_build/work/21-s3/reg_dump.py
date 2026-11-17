"""register-21: compact dump of chapter 21 facts, one block per fact (read-only)."""
import json, glob, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
facts = {}
for p in [ROOT + "/data/facts/s3.jsonl", ROOT + "/data/facts/s3-glacier.jsonl"]:
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
out = []
for i in sorted(facts):
    f = facts[i]
    if f["status"] in ("rejected", "superseded"):
        continue
    q = f.get("qualifiers") or {}
    out.append("=== %s | %s | hard=%s | %s | %s | by=%s | bul=%s" % (i, f["kind"], f.get("hard"), f.get("exam_relevance"), f.get("volatility"), f.get("author"), ",".join(f.get("bullets") or [])))
    out.append("C: " + f["claim"])
    out.append("Q: " + (f.get("question") or ""))
    out.append("V: " + " || ".join("%s=%s" % (v.get("key"), v.get("display")) for v in f.get("values", [])))
    out.append("S: scope=%r dom=%r adj=%r cond=%r" % (q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition")))
    for e in f["evidence"]:
        out.append("E: [%s] %s%s" % (e["source_id"], ("H{%s} " % e["table_header"]) if e.get("table_header") else (("HD{%s} " % e["heading"]) if e.get("heading") else ""), e["quote"]))
    if f.get("changed"):
        out.append("CH: %s" % json.dumps(f["changed"]))
    if f.get("change_items"):
        out.append("CI: %s" % json.dumps(f["change_items"]))
open(sys.argv[1], "w").write("\n".join(out) + "\n")
print(len(out))
