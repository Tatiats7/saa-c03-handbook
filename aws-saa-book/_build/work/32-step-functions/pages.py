"""List guide pages with an in-corpus flag. Usage: python3 -I pages.py GUIDE_ID [OUTFILE]"""
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "corpus")
g = sys.argv[1]
d = json.load(open(os.path.join(ROOT, "index", g + ".json")))
lines = []
for p in d["pages"]:
    sid = p["source_id"]
    have = os.path.exists(os.path.join(ROOT, "snap", sid + ".txt"))
    lines.append(("Y " if have else "- ") + sid.split("/")[-1] + " | " + p["title"] + " | " + p["url"])
out = "\n".join(lines)
if len(sys.argv) > 2:
    open(sys.argv[2], "w").write(out + "\n")
print(out)
