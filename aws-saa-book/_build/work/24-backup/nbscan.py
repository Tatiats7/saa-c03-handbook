"""Scan verified facts of given services for keywords.
python3 nbscan.py OUT svc1,svc2 kw1|kw2|kw3
Writes id | kind | hard | claim | displays for every verified fact whose id or claim matches a keyword."""
import json, re, sys
from pathlib import Path

out, svcs, kws = sys.argv[1], sys.argv[2].split(","), sys.argv[3]
rx = re.compile(kws, re.I)
root = Path(__file__).resolve().parents[3] / "data" / "facts"
lines = []
for svc in svcs:
    p = root / f"{svc}.jsonl"
    if not p.is_file():
        lines.append(f"## {svc}: no file")
        continue
    n = 0
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        if f.get("status") != "verified":
            continue
        text = f["id"] + " " + f.get("claim", "")
        if not rx.search(text):
            continue
        n += 1
        disp = " || ".join(v.get("display", "") for v in f.get("values") or [])
        lines.append(f"{f['id']} [{f.get('kind')}{' hard' if f.get('hard') else ''}] ch{f.get('home_chapter')}\n   {f.get('claim')}\n   displays: {disp}")
    lines.insert(len(lines) - n, f"## {svc}: {n} matches")
Path(out).write_text("\n".join(lines), encoding="utf-8")
print("written", out, len(lines))
