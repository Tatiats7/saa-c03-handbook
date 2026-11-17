"""register-27: compact dump of the chapter's live facts (reads data/facts; writes one text file)."""
import json, sys

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
OUT = sys.argv[1]
rows = []
for s in ("aurora", "aurora-serverless"):
    for line in open(f"{ROOT}/data/facts/{s}.jsonl"):
        if line.strip():
            rows.append(json.loads(line))
rows.sort(key=lambda f: f["id"])
out = []
for f in rows:
    if f["status"] in ("rejected", "superseded"):
        continue
    q = f.get("qualifiers") or {}
    out.append("%s |%s|%s|%s|%s|%s| %s" % (
        f["id"], f["kind"], "H" if f.get("hard") else "-", f.get("exam_relevance"),
        f.get("volatility", "")[:3], q.get("scope", ""), f["claim"]))
    out.append("   D: " + " || ".join(v["display"] for v in f.get("values", [])) +
               ("   CH:%s" % f["changed"].get("date") if f.get("changed") else "") +
               "   SRC:" + ",".join(e["source_id"].split("/")[-1][:40] for e in f["evidence"]))
open(OUT, "w").write("\n".join(out) + "\n")
print("wrote", OUT, len(out))
