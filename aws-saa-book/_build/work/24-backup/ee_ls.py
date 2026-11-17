"""List exam-English word ids: python3 ee_ls.py OUT"""
import json, sys
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "data"
ee = json.loads((root / "exam-english.json").read_text())
lines = []
for g in ee["groups"]:
    lines.append(f"## {g['id']}")
    for it in g["items"]:
        keys = list(it.keys())
        lines.append(f"{it.get('id')} | {it.get('word') or it.get('phrase')} | {str(it.get('meaning', ''))[:70]}")
lines.insert(0, f"item keys: {keys}")
Path(sys.argv[1]).write_text("\n".join(lines))
print("written", len(lines))
