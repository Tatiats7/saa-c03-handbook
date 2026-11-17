"""Compact page list of one guide: '<mark><basename> | <title>'.

Usage: python3 -I aws-saa-book/_build/work/37-monitoring/compact.py GUIDE_ID OUTFILE [SKIP_PREFIX ...]
"""
import json
import sys
from pathlib import Path

ROOT = Path("aws-saa-book/_build/corpus")
gid, out = sys.argv[1], sys.argv[2]
skip = tuple(sys.argv[3:])
idx = json.loads((ROOT / "index" / f"{gid}.json").read_text())
rows = []
for p in idx["pages"]:
    sid = p["source_id"]
    base = sid.rsplit("/", 1)[-1]
    if skip and base.startswith(skip):
        continue
    mark = "*" if (ROOT / "snap" / f"{sid}.txt").exists() else " "
    rows.append(f"{mark}{base} | {p['title']}")
Path(out).write_text("\n".join(rows) + "\n")
print(f"wrote {out}: {len(rows)} rows")
