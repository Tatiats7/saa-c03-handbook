"""Registrar helper for chapter 32 (read-only): dumps facts and open conflicts compactly."""
import json, sys, os

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/32-step-functions"
lst = json.load(open(W + "/reg-list.json"))
ids = {f["id"] for f in lst["facts"]}
facts = {}
for svc in ("step-functions", "mq", "appflow"):
    for line in open(f"{ROOT}/data/facts/{svc}.jsonl"):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        facts[f["id"]] = f
other = sorted(ids - set(facts))
mode = sys.argv[1] if len(sys.argv) > 1 else "facts"
out = []
if mode == "facts":
    svc = sys.argv[2]
    for fid in sorted(ids):
        f = facts.get(fid)
        if not f or f["service"] != svc:
            continue
        if f.get("status") in ("rejected", "superseded"):
            continue
        q = f.get("qualifiers") or {}
        ev = f.get("evidence") or []
        out.append(f"## {fid} [{f['kind']}] hard={f.get('hard')} rel={f.get('exam_relevance')} st={f.get('status')} by={f.get('author')}")
        out.append(f"C: {f['claim']}")
        out.append("V: " + " | ".join(v.get("display", "") for v in (f.get("values") or [])))
        out.append("Q: " + json.dumps({k: v for k, v in q.items() if v not in (None, '', [])}))
        if f.get("changed"):
            out.append("CH: " + json.dumps(f["changed"]))
        for e in ev:
            hdr = (" H=" + e["table_header"]) if e.get("table_header") else ""
            out.append(f"E: [{e.get('source_id')}] {e.get('quote')}{hdr}")
        out.append(f"QN: {f.get('question')}")
elif mode == "conflicts":
    c = json.load(open(W + "/reg-conflicts.json"))
    for cf in c["conflicts"]:
        if cf["status"] != "open":
            continue
        if not any(x in ids for x in cf["facts"]):
            continue
        out.append(f"### {cf['id']} {cf['facts']}")
        for x in cf["facts"]:
            f = facts.get(x)
            if f:
                out.append(f"  {x} [{f['status']}]: {f['claim']}")
                out.append("    V: " + " | ".join(v.get("display", "") for v in (f.get("values") or [])))
elif mode == "summary":
    from collections import Counter
    st = Counter(); hard = 0; svcs = Counter(); kinds = Counter()
    for fid in ids:
        f = facts.get(fid)
        if not f:
            continue
        st[f["status"]] += 1; svcs[f["service"]] += 1; kinds[f["kind"]] += 1
        if f.get("hard") and f["status"] not in ("rejected", "superseded"):
            hard += 1
    out.append(f"status {dict(st)} hard {hard} services {dict(svcs)} kinds {dict(kinds)} other {other}")
    rel = Counter((facts[i].get('exam_relevance'), facts[i]['service']) for i in ids if i in facts)
    out.append(str(dict(rel)))
    long_disp = []
    for fid in ids:
        f = facts.get(fid)
        if not f:
            continue
        for v in f.get("values") or []:
            d = v.get("display", "")
            if not any(ch.isdigit() for ch in d) and len(d.split()) > 8:
                long_disp.append((fid, d))
    out.append(f"long number-free displays: {len(long_disp)}")
    for x in long_disp:
        out.append(f"  {x[0]}: {x[1]}")
open(W + f"/reg-out-{mode}{('-' + sys.argv[2]) if len(sys.argv) > 2 else ''}.txt", "w").write("\n".join(out) + "\n")
print(len(out), "lines")
