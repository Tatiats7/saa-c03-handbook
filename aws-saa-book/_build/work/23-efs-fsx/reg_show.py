"""register-23: print claim, displays and quotes of the facts named in reg-show-ids.txt (read-only)."""
import json, glob
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/23-efs-fsx/"
facts = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
ids = [l.strip() for l in open(W + "reg-show-ids.txt") if l.strip()]
with open(W + "reg-show.txt", "w") as o:
    for i in ids:
        f = facts.get(i)
        if not f:
            o.write("? %s\n" % i)
            continue
        o.write("%s [%s %s h=%s]\n  C: %s\n  D: %s\n" % (i, f["status"], f["kind"], f.get("hard"), f["claim"],
                                                       " ;; ".join("%s=%s" % (v["key"], v["display"]) for v in f["values"])))
        for e in f["evidence"]:
            o.write("  Q: %s\n" % e["quote"])
