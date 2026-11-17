"""List terms of data/terms.json (id | term | short | chapter) and exam-English word ids.
python3 terms_ls.py OUT"""
import json, sys
from pathlib import Path

root = Path(__file__).resolve().parents[3] / "data"
t = json.loads((root / "terms.json").read_text())
lines = [f"terms: {len(t.get('terms', []))}; keys of one: {list(t['terms'][0].keys())}"]
for x in t.get("terms", []):
    lines.append(f"{x.get('id')} | {x.get('term')} | {x.get('short') or ''} | ch {x.get('chapter') or x.get('chapters') or ''} | {', '.join((x.get('collocations') or [])[:2])}")
ee = json.loads((root / "exam-english.json").read_text())
if isinstance(ee, dict):
    lines.append(f"exam-english keys: {list(ee.keys())}")
    words = next((v for v in ee.values() if isinstance(v, list)), [])
else:
    words = ee
lines.append(f"== exam-english: {len(words)}; keys: {list(words[0].keys())}")
for w in words:
    lines.append(f"{w.get('id')} | {w.get('word')} | {w.get('meaning', '')[:60]}")
Path(sys.argv[1]).write_text("\n".join(lines))
print("written", sys.argv[1], len(lines))
