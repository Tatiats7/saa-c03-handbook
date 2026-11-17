"""Read-only helper for adjudicate-34: dumps disputed facts with votes and packet context."""
import json, sys, os

ROOT = sys.argv[1]
OUT = sys.argv[2]
fin = json.load(open(os.path.join(ROOT, "_build/work/34-streaming/finalize-1.json")))
ids = set(fin["disputed"])
facts = {}
for svc in ("data-firehose", "kinesis-data-streams", "msk"):
    for line in open(os.path.join(ROOT, "data/facts", svc + ".jsonl")):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        if f["id"] in ids:
            facts[f["id"]] = f
votes = {}
for svc in ("data-firehose", "kinesis-data-streams", "msk"):
    p = os.path.join(ROOT, "_build/facts/votes", svc + ".jsonl")
    for line in open(p):
        line = line.strip()
        if not line:
            continue
        v = json.loads(line)
        if v["fact"] in ids:
            votes.setdefault(v["fact"], []).append(v)
ctx = {}
pdir = os.path.join(ROOT, "_build/facts/packets")
for fn in sorted(os.listdir(pdir)):
    if fn.startswith("34-"):
        pk = json.load(open(os.path.join(pdir, fn)))
        for pf in pk["facts"]:
            if pf["id"] in ids:
                ctx.setdefault(pf["id"], [e.get("context") for e in pf.get("evidence", [])])
out = []
for i in fin["disputed"]:
    f = facts.get(i)
    if not f:
        out.append("## " + i + "\n(not found)\n")
        continue
    s = ["## " + i + "  rev=%s repairs=%s kind=%s hard=%s vol=%s changed=%s" % (f.get("rev"), f.get("repairs"), f.get("kind"), f.get("hard"), f.get("volatility"), json.dumps(f.get("changed")))]
    s.append("CLAIM: " + f["claim"])
    s.append("VALUES: " + json.dumps(f.get("values")))
    s.append("QUAL: " + json.dumps(f.get("qualifiers")))
    s.append("CHANGE_ITEMS: " + json.dumps(f.get("change_items")))
    for e in f["evidence"]:
        s.append("SRC: " + e["source_id"] + (" HDR: " + str(e.get("table_header")) if e.get("table_header") else "") + (" HEADING: " + str(e.get("heading")) if e.get("heading") else ""))
        s.append("QUOTE: " + e["quote"])
    for v in votes.get(i, []):
        if v["rev"] == f["rev"]:
            s.append("VOTE %s %s by %s: %s" % (v["lens"], v["verdict"], v["voter"], v.get("reason")))
    for c in ctx.get(i, []):
        if c:
            s.append("CONTEXT: " + c.replace("\n", " / "))
    out.append("\n".join(s) + "\n")
open(OUT, "w").write("\n".join(out))
print(len(out))
