"""say-17: print the ready-made link lines of fact-cards*.md for the fact ids in brief cards+speak (or argv)."""
import json, sys, os, glob

here = os.path.dirname(__file__)
blocks = {}
for p in glob.glob(os.path.join(here, "fact-cards*.md")):
    cur = None
    for line in open(p):
        if line and not line.startswith(" "):
            cur = line.strip()
            blocks.setdefault(cur, [])
        elif cur and line.strip().startswith("link:"):
            blocks[cur].append(line.strip()[6:])
ids = sys.argv[1:]
if not ids:
    b = json.load(open(os.path.join(here, "brief.json")))
    seen = []
    for c in b["cards"]:
        seen += c["facts"]
    for s in b["speak"]:
        seen += [x.lstrip("=") for x in s["facts"]]
    ids = list(dict.fromkeys(seen))
for i in ids:
    print(i)
    for l in blocks.get(i, ["NO CARD"]):
        print("   ", l)
