"""Resolve selection.txt to URLs, flag cached ones, write batch files of at most 40 uncached URLs.
Usage: python3 resolve.py   (paths are fixed relative to this file)"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
BOOK = HERE.parents[2]
sys.path.insert(0, str(BOOK / "tools"))
from saalib import corpus  # noqa: E402

CORPUS = BOOK / "_build" / "corpus"
by_sid = {}
for idx_path in (CORPUS / "index").glob("*.json"):
    try:
        idx = json.loads(idx_path.read_text())
    except Exception:
        continue
    for p in idx.get("pages", []):
        by_sid.setdefault(p["source_id"], p["url"])

rows, missing = [], []
for line in (HERE / "selection.txt").read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    if line.startswith("https://"):
        url = line
        sid = corpus.source_id_for(url)
    else:
        sid = line
        url = by_sid.get(sid)
        if not url:
            missing.append(sid)
            continue
    cached = (CORPUS / "snap" / f"{sid}.txt").exists()
    rows.append((sid, url, cached))

seen, uniq = set(), []
for r in rows:
    if r[0] in seen:
        continue
    seen.add(r[0])
    uniq.append(r)

todo = [u for (_, u, c) in uniq if not c]
letters = "abcdefghij"
for i in range(0, len(todo), 40):
    (HERE / f"urls-{letters[i // 40]}.txt").write_text("\n".join(todo[i:i + 40]) + "\n")
(HERE / "selection-resolved.txt").write_text(
    "\n".join(f"{'*' if c else ' '} {s} | {u}" for (s, u, c) in uniq) + "\n")
print(f"selected={len(uniq)} cached={sum(1 for r in uniq if r[2])} to_fetch={len(todo)} "
      f"batches={(len(todo) + 39) // 40} missing_from_index={missing}")
