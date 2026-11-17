"""List the pages of the chapter's guide indexes with a 'saved' flag. Usage: python3 -I pages.py OUT"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
CORPUS = ROOT / "_build" / "corpus"
GUIDES = ["filegateway-files3", "storagegateway-vgw", "storagegateway-tgw", "filegateway-filefsxw",
          "datasync-userguide", "snowball-developer-guide", "transfer-userguide"]
out = []
for g in GUIDES:
    d = json.loads((CORPUS / "index" / f"{g}.json").read_text())
    out.append(f"## {g} '{d.get('title')}' pages={d.get('page_count')} history={d.get('history')} quotas={d.get('quotas')} built={d.get('built_at')}")
    for i, p in enumerate(d["pages"]):
        saved = (CORPUS / "snap" / (p["source_id"] + ".txt")).exists()
        out.append(f"{g}\t{i}\t{'S' if saved else '-'}\t{p['title']}\t{p['url']}")
pathlib.Path(sys.argv[1]).write_text("\n".join(out) + "\n")
print(len(out))
