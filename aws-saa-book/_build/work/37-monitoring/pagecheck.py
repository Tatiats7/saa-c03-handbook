"""Check that every fetched page is assigned to a mining lens and fill lens page lists.

Usage: python3 -I aws-saa-book/_build/work/37-monitoring/pagecheck.py
Reads brief.v0.json, the fetch-*.txt results and mine-plan.json; writes mine-plan.json with
each lens's `pages` (union of its demand sources plus its `extra_pages`) and `demand`, and
prints the fetched pages no lens reads.
"""
import json
import re
from pathlib import Path

WORK = Path("aws-saa-book/_build/work/37-monitoring")
brief = json.loads((WORK / "brief.v0.json").read_text())
plan = json.loads((WORK / "mine-plan.json").read_text())

fetched = []
for f in sorted(WORK.glob("fetch-*.txt")):
    for line in f.read_text().splitlines():
        m = re.match(r"^(fetched|cached|unchanged|not-modified) (\S+) status=200", line)
        if m:
            fetched.append(m.group(2))
bad = {"www/solutions/case-studies/zs-associates-security-case-study"}
fetched = [s for s in dict.fromkeys(fetched) if s not in bad]

assigned = set()
for name, lens in plan["lenses"].items():
    pages, demand = [], []
    for d in brief["demand"]:
        if d["lens"] == name:
            demand.append(d["id"])
            pages += d.get("sources", [])
    pages += lens.get("extra_pages", [])
    lens["pages"] = list(dict.fromkeys(pages))
    lens["demand"] = demand
    assigned.update(lens["pages"])

missing_snap = [p for p in assigned if not (Path("aws-saa-book/_build/corpus/snap") / f"{p}.txt").exists()]
unassigned = [p for p in fetched if p not in assigned]
plan["all_pages_count"] = len(assigned)
plan["not_in_corpus"] = sorted(missing_snap)
(WORK / "mine-plan.json").write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n")
print(f"fetched usable: {len(fetched)}; assigned: {len(assigned)}; not in corpus: {missing_snap}")
print("unassigned fetched pages:")
for p in unassigned:
    print("  ", p)
