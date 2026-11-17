"""Adjudicate-13 helper: dump disputed facts with packet context and vote reasons."""
import json, glob, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", ".."))
B = os.path.join(ROOT, "aws-saa-book")
fin = json.load(open(os.path.join(B, "_build/work/13-route53/finalize.json")))
disp = set(fin["disputed"])

reasons = {}
for line in open(os.path.join(B, "_build/facts/votes/route53.jsonl")):
    v = json.loads(line)
    if v["fact"] in disp and v["verdict"] not in ("support", "current", "match"):
        reasons.setdefault(v["fact"], []).append(f'{v["lens"]}/{v["verdict"]} r{v["rev"]}: {v["reason"]}')

facts = {}
for line in open(os.path.join(B, "data/facts/route53.jsonl")):
    f = json.loads(line)
    if f["id"] in disp:
        facts[f["id"]] = f

ctx = {}
for p in sorted(glob.glob(os.path.join(B, "_build/facts/packets/13-*.json"))):
    d = json.load(open(p))
    for f in d.get("facts", []):
        if f["id"] in disp:
            ctx.setdefault(f["id"], f)

out = []
for i in sorted(disp):
    f = facts[i]
    out.append("=" * 100)
    out.append(f"ID {i}  rev={f['rev']} repairs={f.get('repairs',0)} kind={f['kind']} hard={f['hard']} vol={f.get('volatility')}")
    out.append("CLAIM: " + f["claim"])
    out.append("VALUES: " + json.dumps(f["values"], ensure_ascii=False))
    out.append("QUAL: " + json.dumps(f["qualifiers"], ensure_ascii=False))
    if f.get("changed"):
        out.append("CHANGED: " + json.dumps(f["changed"], ensure_ascii=False))
    for r in reasons.get(i, []):
        out.append("VOTE " + r)
    pk = ctx.get(i)
    for n, e in enumerate(f["evidence"]):
        out.append(f"EV{n} src={e['source_id']} heading={e.get('heading')} th={e.get('table_header')}")
        out.append("  Q: " + e["quote"])
        if pk and n < len(pk.get("evidence", [])):
            out.append("  CTX: " + pk["evidence"][n].get("context", "").replace("\n", " / "))
open(os.path.join(B, "_build/work/13-route53/adj/disputed-dump.txt"), "w").write("\n".join(out))
print(len(disp), len(facts), len(ctx))
