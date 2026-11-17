"""Dump all keys of a JSON file except the given ones: python3 insp2.py FILE OUT skip1,skip2"""
import json, sys

d = json.load(open(sys.argv[1]))
skip = set(sys.argv[3].split(",")) if len(sys.argv) > 3 else set()
out = {k: v for k, v in d.items() if k not in skip}
with open(sys.argv[2], "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("written", sys.argv[2])
