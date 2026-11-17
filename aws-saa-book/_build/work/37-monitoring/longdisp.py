import json, re, sys, glob
for path in sys.argv[1:]:
    for line in open(path):
        f = json.loads(line)
        if f.get("author") != "mine-37-behavior+decisions" and not path.endswith(".json"):
            continue
        for v in f["values"]:
            d = v["display"]
            if not re.search(r"\d", d) and len(d.split()) > 8:
                print(f["id"], "|", v["key"], "|", len(d.split()), "|", d)
