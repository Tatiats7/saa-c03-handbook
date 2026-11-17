"""adjudicate-34 helper: builds one amend patch per fact from adj-spec.json.

Spec entry keys (all optional except id): claim, values, qualifiers (merged into the
current ones), note, keep (list of current evidence indexes to keep, default all),
replace ({index: new quote}), add (list of {src, quote, table_header?, heading?, url?}).
Writes adj/<id>.json. Read-only on the fact store.
"""
import json, os, sys

ROOT = sys.argv[1]
spec = json.load(open(os.path.join(ROOT, "_build/work/34-streaming/adj-spec.json")))
outdir = os.path.join(ROOT, "_build/work/34-streaming/adj")
os.makedirs(outdir, exist_ok=True)

facts, urls = {}, {}
fdir = os.path.join(ROOT, "data/facts")
for fn in os.listdir(fdir):
    if not fn.endswith(".jsonl"):
        continue
    for line in open(os.path.join(fdir, fn)):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        for e in f.get("evidence", []):
            urls.setdefault(e["source_id"], e["url"])
        if fn[:-6] in ("data-firehose", "kinesis-data-streams", "msk"):
            facts[f["id"]] = f

def item(e):
    d = {"source_id": e["source_id"], "url": e["url"], "quote": e["quote"], "table_header": e.get("table_header")}
    if e.get("heading"):
        d["heading"] = e["heading"]
    return d

n = 0
for s in spec:
    f = facts[s["id"]]
    patch = {}
    if "claim" in s:
        patch["claim"] = s["claim"]
    if "values" in s:
        patch["values"] = s["values"]
    if "qualifiers" in s:
        q = dict(f["qualifiers"])
        q.update(s["qualifiers"])
        patch["qualifiers"] = q
    if "note" in s:
        patch["note"] = s["note"]
    if "note_append" in s:
        patch["note"] = ((f.get("note") or "") + " | " + s["note_append"]).strip(" |")
    ev = [item(e) for e in f["evidence"]]
    for k, v in s.get("replace", {}).items():
        ev[int(k)]["quote"] = v
    if "keep" in s:
        ev = [ev[i] for i in s["keep"]]
    for a in s.get("add", []):
        sid = a["src"]
        d = {"source_id": sid, "url": a.get("url") or urls[sid], "quote": a["quote"], "table_header": a.get("table_header")}
        if a.get("heading"):
            d["heading"] = a["heading"]
        if a.get("first"):
            ev.insert(0, d)
        else:
            ev.append(d)
    if "keep" in s or "replace" in s or "add" in s:
        patch["evidence"] = ev
    json.dump(patch, open(os.path.join(outdir, s["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
    n += 1
print(n)
