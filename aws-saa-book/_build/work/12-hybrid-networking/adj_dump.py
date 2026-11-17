"""adjudicate-12: read-only dump of disputed chapter 12 facts with their current-rev votes.

Writes adj-dump.txt.
"""
import json
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/12-hybrid-networking/"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if line:
            f = json.loads(line)
            facts[f["id"]] = f
votes = {}
for s in SVCS:
    for line in open(ROOT + "/_build/facts/votes/%s.jsonl" % s):
        line = line.strip()
        if line:
            v = json.loads(line)
            votes.setdefault(v["fact"], []).append(v)
out = open(W + "adj-dump.txt", "w")
n = 0
for i in sorted(facts):
    f = facts[i]
    if f.get("home_chapter") != "12" or f["status"] != "disputed":
        continue
    n += 1
    q = f.get("qualifiers") or {}
    out.write("== %s | %s | hard=%s | vol=%s | rev=%s | repairs=%s | amended_by=%s\n" % (
        i, f["kind"], f["hard"], f.get("volatility"), f["rev"], f.get("repairs", 0), f.get("amended_by")))
    out.write("  C: %s\n" % f["claim"])
    for v in f.get("values") or []:
        out.write("  D[%s]: %s\n" % (v.get("key"), v.get("display")))
    out.write("  S: %s | dom=%s | adj=%s | cond=%s\n" % (q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition")))
    if f.get("changed"):
        out.write("  CH: %s\n" % json.dumps(f["changed"]))
    if f.get("derivation"):
        out.write("  DER: %s\n" % json.dumps(f["derivation"]))
    for k, e in enumerate(f.get("evidence") or []):
        out.write("  E%d: %s :: %s%s\n" % (k, e["source_id"], e["quote"], " [H:%s]" % e.get("heading") if e.get("heading") else ""))
        if e.get("table_header"):
            out.write("     TH: %s\n" % e["table_header"])
    for v in votes.get(i, []):
        if v["rev"] != f["rev"]:
            continue
        out.write("  V %s %s (%s): %s\n" % (v["lens"], v["verdict"], v["voter"], v.get("reason")))
    out.write("  deps-note: %s\n\n" % (f.get("note") or ""))
out.close()
print("disputed", n)
