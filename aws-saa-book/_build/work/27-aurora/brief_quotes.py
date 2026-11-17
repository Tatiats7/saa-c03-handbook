"""Print the evidence quotes of the given fact ids (helper of brief-27; read-only). Usage: brief_quotes.py ID ..."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
want = set(sys.argv[1:])
for p in sorted((ROOT / "data" / "facts").glob("*.jsonl")):
    for line in p.read_text().splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        if f["id"] in want:
            print(f"== {f['id']} [{f.get('status')}] displays={[v['display'] for v in f.get('values') or []]}")
            for e in f["evidence"]:
                print(f"   {e['url']}")
                print(f"   Q: {e['quote']}")
