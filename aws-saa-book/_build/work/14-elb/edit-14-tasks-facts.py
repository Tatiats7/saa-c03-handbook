"""edit-14: add the facts filled by fr-0054 and fr-0056 to the task items that use them.

Reads data/14-elb/tasks.json and writes _build/work/14-elb/edit-14-tasks-replace.json
for `saa.py tasks add --chapter 14 --file ... --replace`.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
src = ROOT / "data" / "14-elb" / "tasks.json"
out = ROOT / "_build" / "work" / "14-elb" / "edit-14-tasks-replace.json"

data = json.loads(src.read_text())
items = data["items"] if isinstance(data, dict) else data
add = {
    "elb-t01": ["elb-alb-tls-policy-protocols-pq-and-2016-08"],
    "elb-t02": ["elb-tagging-api-getresources-elb-resources"],
    "elb-t03": ["elb-tagging-api-getresources-elb-resources"],
}
keep_out = {"label", "checked", "status", "rev", "chapter"}
result = []
for item in items:
    if item["id"] not in add:
        continue
    new = {k: v for k, v in item.items() if k not in keep_out}
    facts = list(new.get("facts") or [])
    for f in add[item["id"]]:
        if f not in facts:
            facts.append(f)
    new["facts"] = facts
    result.append(new)
out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")
print(out, len(result))
