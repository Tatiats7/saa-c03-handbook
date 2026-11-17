"""List every page of the chapter-37 guides with a corpus mark.

Usage: python3 -I aws-saa-book/_build/work/37-monitoring/idx.py OUTFILE [GUIDE_ID ...]
A line is: '* ' when the page snapshot exists, '  ' otherwise; then guide id, source_id, title.
"""
import json
import sys
from pathlib import Path

ROOT = Path("aws-saa-book/_build/corpus")
GUIDES = [
    "amazoncloudwatch-monitoring",
    "amazoncloudwatch-logs",
    "awscloudtrail-userguide",
    "xray-devguide",
    "health-ug",
    "grafana-userguide",
    "prometheus-userguide",
]

out = sys.argv[1]
guides = sys.argv[2:] or GUIDES
lines = []
for gid in guides:
    idx = json.loads((ROOT / "index" / f"{gid}.json").read_text())
    pages = idx["pages"]
    have = 0
    rows = []
    for p in pages:
        sid = p["source_id"]
        ok = (ROOT / "snap" / f"{sid}.txt").exists()
        have += ok
        rows.append(f"{'*' if ok else ' '} {gid} {sid} | {p['title']}")
    hist = (idx.get("history") or {}).get("source_id")
    quo = (idx.get("quotas") or {}).get("source_id")
    lines.append(f"## {gid}: {len(pages)} pages, {have} in corpus; history={hist}; quotas={quo}")
    lines.extend(rows)
Path(out).write_text("\n".join(lines) + "\n")
print(f"wrote {out}: {len(lines)} lines")
