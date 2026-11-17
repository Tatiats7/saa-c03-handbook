"""say-17: print facts (status, claim, displays, spoken, quotes) for ids given on argv, or for every id in brief cards+speak."""
import json, sys, glob, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
facts = {}
for p in glob.glob(os.path.join(ROOT, "data", "facts", "*.jsonl")):
    for line in open(p):
        line = line.strip()
        if line:
            f = json.loads(line)
            facts[f["id"]] = f

ids = sys.argv[1:]
if not ids:
    b = json.load(open(os.path.join(os.path.dirname(__file__), "brief.json")))
    seen = []
    for c in b["cards"]:
        seen += c["facts"]
    for s in b["speak"]:
        seen += [x.lstrip("=") for x in s["facts"]]
    ids = list(dict.fromkeys(seen))
for i in ids:
    f = facts.get(i)
    if not f:
        print("MISSING", i)
        continue
    print("==", i, f.get("status"), "hard" if f.get("hard") else "")
    print("  claim:", f.get("claim"))
    for v in f.get("values") or []:
        print("  value:", v.get("display"), "|", v.get("spoken"))
    if "-q" not in sys.argv:
        for e in f.get("evidence", []):
            print("  quote:", e.get("quote"))
