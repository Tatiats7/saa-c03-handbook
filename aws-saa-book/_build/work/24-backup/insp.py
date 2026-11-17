"""Inspect JSON structure of a brief: python3 insp.py FILE [key] [maxlen]"""
import json, sys

path = sys.argv[1]
d = json.load(open(path))
key = sys.argv[2] if len(sys.argv) > 2 else None
maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 400


def short(v, n=maxlen):
    s = json.dumps(v, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + "..."


if key is None:
    for k, v in d.items():
        if isinstance(v, list):
            print(f"{k}: list[{len(v)}]")
            if v:
                print("   first:", short(v[0]))
        elif isinstance(v, dict):
            print(f"{k}: dict keys={list(v.keys())[:30]}")
        else:
            print(f"{k}: {short(v)}")
else:
    v = d
    for part in key.split("."):
        if isinstance(v, list):
            v = v[int(part)]
        else:
            v = v[part]
    if isinstance(v, list):
        for i, x in enumerate(v):
            print(i, short(x))
    else:
        print(json.dumps(v, ensure_ascii=False, indent=1)[: maxlen * 20])
