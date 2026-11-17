"""register-11: read-only dump of chapter 11 facts and conflicts for the registrar.

Writes reg-dump.txt (one block per fact), reg-conf.txt (open conflicts that touch chapter 11)
and reg-dups.txt (pairs of live facts with similar claims or identical quotes).
"""
import json, re
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/11-vpc-connectivity/"
SVCS = ["vpc-peering", "transit-gateway", "vpc-endpoints", "privatelink"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if not line:
            continue
        f = json.loads(line)
        facts[f["id"]] = f
live = {i: f for i, f in facts.items() if f["status"] not in ("rejected", "superseded")}
out = open(W + "reg-dump.txt", "w")
stats = {}
for i in sorted(live):
    f = live[i]
    stats[f["status"]] = stats.get(f["status"], 0) + 1
    q = f.get("qualifiers") or {}
    out.write("== %s | %s | hard=%s | rel=%s | vol=%s | ch=%s | b=%s | note=%s | st=%s rev=%s | by=%s\n" % (
        i, f["kind"], f["hard"], f.get("exam_relevance"), f.get("volatility"),
        json.dumps(f.get("changed")) if f.get("changed") else "-", ",".join(f.get("bullets") or []),
        (f.get("note") or "")[:120], f["status"], f["rev"], f.get("author")))
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

def toks(s):
    return set(w for w in re.findall(r"[a-z]+", s.lower()) if len(w) > 2)

dup = open(W + "reg-dups.txt", "w")
ids = sorted(live)
quote_of = {}
for i in ids:
    for e in live[i].get("evidence") or []:
        quote_of.setdefault(e["quote"].strip(), []).append(i)
nd = 0
for qtext, who in sorted(quote_of.items()):
    if len(who) > 1:
        nd += 1
        dup.write("SAMEQUOTE %s :: %s\n" % (" / ".join(who), qtext[:160]))
for a in range(len(ids)):
    ta = toks(live[ids[a]]["claim"])
    for b in range(a + 1, len(ids)):
        tb = toks(live[ids[b]]["claim"])
        if not ta or not tb:
            continue
        j = len(ta & tb) / float(len(ta | tb))
        if j >= 0.5:
            nd += 1
            dup.write("SIM %.2f %s / %s\n   A: %s\n   B: %s\n" % (j, ids[a], ids[b], live[ids[a]]["claim"][:220], live[ids[b]]["claim"][:220]))
dup.close()

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
        conf.write("   %s [%s]: %s\n" % (x, f["status"] if f else "-", (f["claim"] if f else "(other chapter)")[:260]))
conf.close()
print("facts", len(live), "stats", stats, "open conflicts", k, "dup lines", nd)
