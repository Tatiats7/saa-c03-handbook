"""adjudicate-13 spot check (RULINGS safeguard 2): dump 30 random verified chapter-13 facts with packet context."""
import json, glob, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
facts = [json.loads(l) for l in open(os.path.join(B, "data/facts/route53.jsonl"))]
ver = sorted(f["id"] for f in facts if f.get("status") == "verified" and f.get("home_chapter") == "13")
pick = sorted(random.Random(20261013).sample(ver, 30))
byid = {f["id"]: f for f in facts}
ctx = {}
for p in sorted(glob.glob(os.path.join(B, "_build/facts/packets/13-entail-*.json"))):
    for f in json.load(open(p)).get("facts", []):
        if f["id"] in pick:
            ctx[f["id"]] = f
out = [f"verified in chapter 13: {len(ver)}; sample seed 20261013"]
for i in pick:
    f = byid[i]
    out.append("=" * 80)
    out.append(f"ID {i} rev={f['rev']} kind={f['kind']}")
    out.append("CLAIM: " + f["claim"])
    out.append("VALUES: " + json.dumps(f["values"], ensure_ascii=False))
    out.append("QUAL: " + json.dumps(f["qualifiers"], ensure_ascii=False))
    pk = ctx.get(i, {})
    for n, e in enumerate(f["evidence"]):
        out.append(f"EV{n} {e['source_id']} heading={e.get('heading')} th={e.get('table_header')}")
        out.append("  Q: " + e["quote"])
        pe = (pk.get("evidence") or [])
        if n < len(pe):
            out.append("  CTX: " + pe[n].get("context", "").replace("\n", " / ")[:900])
open(os.path.join(HERE, "spot-dump.txt"), "w").write("\n".join(out))
print(len(ver), len(pick), len(ctx))
