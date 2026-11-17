"""adjudicate-13: list brief demand items with the current status of their facts."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
st = {}
for line in open(os.path.join(B, "data/facts/route53.jsonl")):
    f = json.loads(line)
    st[f["id"]] = f.get("status")
for svc in os.listdir(os.path.join(B, "data/facts")):
    if svc.endswith(".jsonl") and svc != "route53.jsonl":
        for line in open(os.path.join(B, "data/facts", svc)):
            f = json.loads(line)
            st.setdefault(f["id"], f.get("status"))
brief = json.load(open(os.path.join(HERE, "..", "brief.v0.json")))
out = []
for d in brief["demand"]:
    fs = d.get("facts") or []
    stats = [f"{x}={st.get(x, 'MISSING')}" for x in fs]
    flag = "" if d["status"] == "filled" and all(st.get(x) == "verified" for x in fs) else "  <--"
    extra = {k: v for k, v in d.items() if k not in ("id", "bullet", "kind", "lens", "service", "question", "look_in", "status", "facts")}
    out.append(f"{d['id']} [{d['status']}] {' '.join(stats)}{flag} {json.dumps(extra, ensure_ascii=False) if extra else ''}")
    if flag:
        out.append("    Q: " + d["question"])
open(os.path.join(HERE, "demand-check.txt"), "w").write("\n".join(out))
print(len(brief["demand"]), sum(1 for l in out if l.endswith("<--") or "<--" in l))
