"""fix-18: write status and resolution into the chapter 18 findings files from fix-18-resolutions.json."""
import json
import pathlib
import sys

work = pathlib.Path(sys.argv[1])
res = json.loads((work / "fix-18-resolutions.json").read_text())
seen = set()
for name in ("claims.json", "reader.json", "exam.json"):
    path = work / "findings" / name
    data = json.loads(path.read_text())
    for f in data["findings"]:
        if f["id"] in res:
            f["status"], f["resolution"] = res[f["id"]]
            seen.add(f["id"])
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
missing = sorted(set(res) - seen)
print("updated", len(seen), "missing", missing)
