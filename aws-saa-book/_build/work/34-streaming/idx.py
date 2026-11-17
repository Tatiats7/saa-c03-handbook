"""List the pages of guide indexes with a corpus flag. Usage: python3 idx.py OUT GUIDE_ID..."""
import json, sys, pathlib
BOOK = pathlib.Path(__file__).resolve().parents[3]
CORPUS = BOOK / "_build" / "corpus"
out = pathlib.Path(sys.argv[1])
lines = []
for gid in sys.argv[2:]:
    idx = json.loads((CORPUS / "index" / f"{gid}.json").read_text())
    lines.append(f"== {gid} {idx['page_count']} pages")
    for p in idx["pages"]:
        sid = p["source_id"]
        have = (CORPUS / "snap" / f"{sid}.txt").exists()
        lines.append(f"{'*' if have else ' '} {sid} | {p['title']}")
out.write_text("\n".join(lines) + "\n")
print(len(lines), "lines")
