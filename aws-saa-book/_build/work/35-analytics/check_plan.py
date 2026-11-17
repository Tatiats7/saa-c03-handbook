"""Check brief.v0.json and mine-plan.json: JSON valid, every source/page exists in the corpus, every demand item has a lens.
Usage: python3 check_plan.py"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
BOOK = HERE.parents[2]
SNAP = BOOK / "_build" / "corpus" / "snap"
brief = json.loads((HERE / "brief.v0.json").read_text())
ids = [d["id"] for d in brief["demand"]]
assert len(ids) == len(set(ids)), "duplicate demand ids"
missing = set()
for d in brief["demand"]:
    for s in d.get("sources", []):
        if s.startswith("_build/"):
            if not (BOOK / s).exists():
                missing.add(s)
        elif not (SNAP / f"{s}.txt").exists():
            missing.add(s)
bullets = sorted({d["bullet"] for d in brief["demand"]})
print(f"brief: {len(ids)} demand items; bullets {bullets}; missing sources {sorted(missing)}")
plan_path = HERE / "mine-plan.json"
if plan_path.exists():
    plan = json.loads(plan_path.read_text())
    assigned, pages, miss = [], set(), set()
    for name, lens in plan["lenses"].items():
        assigned += lens["demand"]
        for p in lens["pages"]:
            pages.add(p)
            if not (SNAP / f"{p}.txt").exists():
                miss.add(p)
    unassigned = sorted(set(ids) - set(assigned))
    double = sorted({i for i in assigned if assigned.count(i) > 1})
    unknown = sorted(set(assigned) - set(ids))
    print(f"mine-plan: {len(pages)} distinct pages; missing pages {sorted(miss)}; "
          f"unassigned demand {unassigned}; assigned twice {double}; unknown {unknown}")
