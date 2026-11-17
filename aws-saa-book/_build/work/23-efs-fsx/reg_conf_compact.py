"""register-23: one line per open conflict of chapter 23 (read-only)."""
import json, glob
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/23-efs-fsx/"
facts = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
conf = [json.loads(l) for l in open(ROOT + "/_build/facts/conflicts.jsonl") if l.strip()]
with open(W + "reg-conf-compact.txt", "w") as o:
    for c in conf:
        if c["status"] != "open":
            continue
        a, b = c["facts"]
        fa, fb = facts[a], facts[b]
        same_src = fa["evidence"][0]["source_id"] == fb["evidence"][0]["source_id"]
        o.write("%s %s %s{%s} | %s{%s} | %s\n" % (
            c["id"], "S" if same_src else "D", a, ";".join(v["display"] for v in fa["values"]),
            b, ";".join(v["display"] for v in fb["values"]),
            "" if same_src else fa["evidence"][0]["source_id"] + " vs " + fb["evidence"][0]["source_id"]))
