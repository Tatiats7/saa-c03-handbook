"""Checks that every page named in mine-plan.json is a saved snapshot. Run: python3 -I check_plan.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "..", "..", "corpus", "snap")
plan = json.load(open(os.path.join(HERE, "mine-plan.json")))
missing = set()
for lens, e in plan["lenses"].items():
    for sid in e["pages"]:
        if not os.path.exists(os.path.join(SNAP, sid + ".txt")):
            missing.add(sid)
print("missing:", sorted(missing))
print("declared not_in_corpus:", plan["not_in_corpus"])
