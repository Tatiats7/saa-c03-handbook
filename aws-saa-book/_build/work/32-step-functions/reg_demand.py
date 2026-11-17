"""register-32 (read-only): demand items with status, plus miners' not_found/partial notes."""
import json
W = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/32-step-functions"
b = json.load(open(W + "/brief.v0.json"))
out = []
from collections import Counter
out.append("statuses: " + str(Counter(d.get("status") for d in b["demand"])))
out.append("keys of a demand item: " + str(list(b["demand"][0].keys())))
for d in b["demand"]:
    if d.get("status") not in ("found",):
        out.append(f"{d['id']} [{d.get('status')}] {d.get('bullet')} :: {d.get('question')} :: facts={d.get('facts')} note={d.get('note')}")
for lens in ("faq", "numbers+changes", "behavior+decisions"):
    m = json.load(open(f"{W}/mine-{lens}.json"))
    out.append(f"=== mine-{lens}: keys {list(m.keys())}")
    for k in ("not_found", "partial"):
        v = m.get(k)
        if v:
            out.append(f"-- {k}: " + json.dumps(v, ensure_ascii=False, indent=0))
open(W + "/reg-out-demand.txt", "w").write("\n".join(out) + "\n")
print(len(out))
