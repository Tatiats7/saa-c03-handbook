"""register-19: print the demand items of brief.v0.json in one line each (read-only)."""
import json, collections
W = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/19-containers/"
b = json.load(open(W + "brief.v0.json"))
print({k: (v if not isinstance(v, list) else len(v)) for k, v in b.items()})
print(collections.Counter(d.get("status") for d in b["demand"]))
for d in b["demand"]:
    extra = {k: v for k, v in d.items() if k not in ("id", "bullet", "question", "status", "facts")}
    print("%s | %s | %s | %d | %s | %s" % (d["id"], d.get("bullet"), d.get("status"), len(d.get("facts") or []), d["question"][:150], json.dumps(extra)[:200]))
