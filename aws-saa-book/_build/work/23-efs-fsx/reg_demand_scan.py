"""register-23: read the miners' notes and list the demand items that are not filled (read-only)."""
import json, glob, os
W = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/23-efs-fsx/"
brief = json.load(open(W + "brief.v0.json"))
got = {}
for p in sorted(glob.glob(W + "mine-*.json")):
    name = os.path.basename(p)
    if name == "mine-plan.json":
        continue
    d = json.load(open(p))
    dem = d.get("demand")
    items = dem.items() if isinstance(dem, dict) else [(x["id"], x) for x in (dem or [])]
    for did, x in items:
        got.setdefault(did, []).append((name, x))
with open(W + "reg-demand-scan.txt", "w") as o:
    for dm in brief["demand"]:
        lst = got.get(dm["id"], [])
        sts = sorted({str(x.get("status")) for _, x in lst})
        if not lst or any(s not in ("filled", "found") for s in sts):
            o.write("%s [%s] %s\n  Q: %s\n" % (dm["id"], dm["service"], ",".join(sts) or "NONE", dm["question"]))
            for n, x in lst:
                extra = {k: v for k, v in x.items() if k not in ("status",)}
                o.write("  %s: %s %s\n" % (n, x.get("status"), json.dumps(extra, ensure_ascii=False)[:600]))
print(len(brief["demand"]), "demand;", sum(1 for d in brief["demand"] if d["id"] in got), "with notes")
