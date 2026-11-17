"""Print the shape of a brief.json: top keys, counts, and one sample of each list."""
import json, sys

p = sys.argv[1]
d = json.load(open(p))
for k, v in d.items():
    if isinstance(v, list):
        print(f"== {k}: list[{len(v)}]")
        if v:
            print(json.dumps(v[0], indent=1)[:1500])
            if len(v) > 1 and isinstance(v[0], dict):
                keys = set()
                for x in v:
                    if isinstance(x, dict):
                        keys |= set(x.keys())
                print("  all keys:", sorted(keys))
    elif isinstance(v, dict):
        print(f"== {k}: dict keys={list(v.keys())}")
        print(json.dumps(v, indent=1)[:2500])
    else:
        print(f"== {k}: {str(v)[:300]}")
