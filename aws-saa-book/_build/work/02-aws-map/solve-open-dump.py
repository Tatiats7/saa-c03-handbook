import json, sys
root = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/data/facts/"
out = open(sys.argv[1], "w")
for svc in sys.argv[2:]:
    for line in open(root + svc + ".jsonl"):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        if f.get("status") != "verified":
            continue
        out.write("## " + f["id"] + "\n")
        out.write("CLAIM: " + f.get("claim", "") + "\n")
        for e in f.get("evidence", []):
            out.write("Q[" + e.get("source_id", "") + "]: " + e.get("quote", "") + "\n")
        out.write("\n")
