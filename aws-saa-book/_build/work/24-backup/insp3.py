"""Compact view of the brief.v0 demand list: python3 insp3.py V0 OUT"""
import json, sys

d = json.load(open(sys.argv[1]))
lines = []
for x in d["demand"]:
    lines.append(f"{x['id']} [{x['bullet']}] {x['status']} :: {x['question']}")
    if x.get("note"):
        lines.append(f"   note: {x['note']}")
    vf = x.get("verified_facts") or x.get("facts") or []
    lines.append(f"   facts: {', '.join(vf)}")
for k in ("research_input", "register", "fetch_failures"):
    lines.append(f"== {k}")
    lines.append(json.dumps(d.get(k), ensure_ascii=False, indent=1))
open(sys.argv[2], "w").write("\n".join(lines))
print("written", sys.argv[2], len(lines))
