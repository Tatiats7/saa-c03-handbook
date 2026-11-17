"""Read-only: dump disputed/pending facts of chapter 31 with their counting votes."""
import json, sys, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
ROOT = os.path.abspath(ROOT)
svcs = ["sqs", "sns", "eventbridge"]
facts = {}
for s in svcs:
    with open(os.path.join(ROOT, "data", "facts", s + ".jsonl")) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            facts[d["id"]] = d
votes = {}
for s in svcs:
    with open(os.path.join(ROOT, "_build", "facts", "votes", s + ".jsonl")) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            v = json.loads(line)
            votes.setdefault(v["fact"], []).append(v)
conf = []
with open(os.path.join(ROOT, "_build", "facts", "conflicts.jsonl")) as f:
    for line in f:
        line = line.strip()
        if line:
            c = json.loads(line)
            if c.get("status") == "open":
                conf.append(c)
want = sys.argv[1] if len(sys.argv) > 1 else "disputed"
out = []
for fid, d in sorted(facts.items()):
    if d.get("home_chapter") != "31" or d.get("status") != want:
        continue
    out.append("=" * 70)
    out.append(f"{fid}  rev={d['rev']} kind={d['kind']} hard={d['hard']} repairs={d.get('repairs',0)} vol={d.get('volatility')} changed={bool(d.get('changed'))} ci={d.get('change_items')} author={d.get('author')} amended_by={d.get('amended_by')}")
    out.append("CLAIM: " + d["claim"])
    out.append("VALUES: " + json.dumps(d.get("values")))
    out.append("QUAL: " + json.dumps(d.get("qualifiers")))
    if d.get("changed"):
        out.append("CHANGED: " + json.dumps(d.get("changed")))
    for e in d.get("evidence", []):
        out.append(f"  SRC {e['source_id']} hdr={e.get('table_header')} heading={e.get('heading')}")
        out.append("  QUOTE: " + e["quote"])
    for v in votes.get(fid, []):
        if v["rev"] != d["rev"]:
            continue
        out.append(f"  VOTE {v['lens']} {v['verdict']} by {v['voter']}: {v.get('reason')}")
    for c in conf:
        if fid in c["facts"]:
            out.append(f"  CONFLICT {c['id']}: {c['facts']}")
print("\n".join(out))
