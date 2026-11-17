"""List term ids and terms of data/terms.json, one per line."""
import json, sys

d = json.load(open(sys.argv[1]))
items = d if isinstance(d, list) else d.get("terms", d)
if isinstance(items, dict):
    items = list(items.values())
for t in items:
    if isinstance(t, dict):
        print(t.get("id"), "|", t.get("term"), "|", t.get("short", ""), "|", t.get("kind", ""))
