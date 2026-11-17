"""adjudicate-17: record fact verification state on the brief's demand items (status stays filled / partial / contradicted)."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
BRIEF = pathlib.Path(__file__).resolve().parent / "brief.v0.json"
status = {}
for p in (ROOT / "data/facts").glob("*.jsonl"):
    for l in p.read_text().splitlines():
        if l.strip():
            f = json.loads(l)
            status[f["id"]] = f["status"]
b = json.loads(BRIEF.read_text())
changed = 0
for d in b["demand"]:
    ids = d.get("facts", [])
    if not ids:
        d["status"] = "not found" if d["status"] == "filled" else d["status"]
        continue
    states = {i: status.get(i, "missing") for i in ids}
    pending = [i for i, s in states.items() if s == "mech-pass"]
    bad = [i for i, s in states.items() if s in ("rejected", "superseded", "missing", "disputed")]
    d["facts_verified"] = sum(1 for s in states.values() if s == "verified")
    if pending:
        d["facts_pending_revote"] = pending
        tag = "adjudicate-17 (2026-10-13): repaired once, awaiting revote in 17-entail-015"
        if tag not in d.get("note", ""):
            d["note"] = (d.get("note", "") + " | " + tag).strip(" |")
        changed += 1
    else:
        d.pop("facts_pending_revote", None)
    if bad:
        d["facts_not_live"] = bad
        if len(bad) == len(ids) and d["status"] == "filled":
            d["status"] = "not found"
BRIEF.write_text(json.dumps(b, indent=1, ensure_ascii=False) + "\n")
print(f"demand items with pending revote: {changed}")
