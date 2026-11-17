"""Apply fix-12 resolutions to the chapter 12 findings files (status and resolution only)."""
import json
import sys
from pathlib import Path

work = Path(sys.argv[1])
res = json.loads((work / "fix-resolutions.json").read_text())
for lens, table in res.items():
    path = work / "findings" / f"{lens}.json"
    data = json.loads(path.read_text())
    seen = set()
    for f in data["findings"]:
        if f["id"] in table:
            f["status"], f["resolution"] = table[f["id"]]
            seen.add(f["id"])
    missing = set(table) - seen
    left = [f["id"] for f in data["findings"] if f["status"] == "open"]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    print(lens, "set", len(seen), "missing", sorted(missing), "open", left)
