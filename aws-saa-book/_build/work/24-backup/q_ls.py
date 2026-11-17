"""Print status, displays, quotes and changed of facts: python3 q_ls.py OUT id1 id2 ..."""
import json, sys
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "data" / "facts"
want = sys.argv[2:]
found = {}
for p in root.glob("*.jsonl"):
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        if f["id"] in want:
            found[f["id"]] = f
lines = []
for i in want:
    f = found.get(i)
    if not f:
        lines.append(f"{i}: NOT FOUND")
        continue
    lines.append(f"{i} [{f.get('status')}] kind={f.get('kind')} hard={f.get('hard')} changed={json.dumps(f.get('changed'))}")
    lines.append("  displays: " + " || ".join(v.get("display", "") for v in f.get("values") or []))
    for e in f.get("evidence") or []:
        lines.append(f"  quote: {e.get('quote')}")
        lines.append(f"  url: {e.get('url')} | title: {e.get('title')}")
Path(sys.argv[1]).write_text("\n".join(lines), encoding="utf-8")
print("written", len(lines))
