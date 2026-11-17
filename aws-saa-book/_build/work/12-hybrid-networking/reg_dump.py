"""register-12: read-only dump of chapter 12 facts and conflicts for the registrar.

Writes reg-dump.txt (one block per fact) and reg-conf.txt (open conflicts that touch chapter 12).
"""
import json, re, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/12-hybrid-networking/"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        facts[f["id"]] = f
out = open(W + "reg-dump.txt", "w")
n = 0
for i in sorted(facts):
    f = facts[i]
    if f["status"] in ("rejected", "superseded"):
        continue
    n += 1
    q = f.get("qualifiers") or {}
    out.write("== %s | %s | hard=%s | rel=%s | vol=%s | ch=%s | b=%s | note=%s | st=%s rev=%s\n" % (
        i, f["kind"], f["hard"], f.get("exam_relevance"), f.get("volatility"),
        json.dumps(f.get("changed")) if f.get("changed") else "-", ",".join(f.get("bullets") or []),
        (f.get("note") or "")[:120], f["status"], f["rev"]))
    out.write("  C: %s\n" % f["claim"])
    out.write("  Q: %s\n" % (f.get("question") or ""))
    for v in f.get("values") or []:
        d = v.get("display", "")
        wc = len(d.split())
        flag = " !LONG" if (wc > 8 and not re.search(r"\d", d)) else ""
        out.write("  D[%s] (%d)%s: %s\n" % (v.get("key"), wc, flag, d))
    out.write("  S: %s | dom=%s | adj=%s | cond=%s\n" % (q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition")))
    for e in f.get("evidence") or []:
        out.write("  E: %s :: %s%s\n" % (e["source_id"], e["quote"][:400], " [H:%s]" % e.get("heading") if e.get("heading") else ""))
        if e.get("table_header"):
            out.write("     TH: %s\n" % e["table_header"][:200])
    if f.get("change_items"):
        out.write("  CI: %s\n" % json.dumps(f["change_items"])[:200])
out.close()
conf = open(W + "reg-conf.txt", "w")
k = 0
for line in open(ROOT + "/_build/facts/conflicts.jsonl"):
    line = line.strip()
    if not line:
        continue
    c = json.loads(line)
    if c.get("status") != "open":
        continue
    if not any(x in facts for x in c["facts"]):
        continue
    k += 1
    conf.write("%s %s\n" % (c["id"], " / ".join(c["facts"])))
    for x in c["facts"]:
        f = facts.get(x)
        conf.write("   %s: %s\n" % (x, (f["claim"] if f else "(other chapter)")[:260]))
conf.close()
print("facts", n, "open conflicts", k)
