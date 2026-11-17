"""register-12: print compact blocks for the given fact ids (read-only).

Usage: python3 reg_view.py ID [ID ...]   or   python3 reg_view.py --pairs  (all shared-quote pairs of reg-analysis.txt)
"""
import json, re, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/12-hybrid-networking/"
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def block(i):
    f = facts.get(i)
    if not f:
        return "?? %s\n" % i
    q = f.get("qualifiers") or {}
    s = "== %s [%s %s hard=%s rel=%s vol=%s b=%s]\n" % (i, f["status"], f["kind"], f["hard"], f.get("exam_relevance"), f.get("volatility"), ",".join(f.get("bullets") or []))
    s += "  C: %s\n" % f["claim"]
    s += "  D: %s\n" % " | ".join(v["display"] for v in f.get("values") or [])
    s += "  S: %s / %s / adj=%s / cond=%s\n" % (q.get("scope"), q.get("default_or_max"), q.get("adjustable"), q.get("condition"))
    if f.get("changed"):
        s += "  CH: %s\n" % json.dumps(f["changed"])
    if f.get("note"):
        s += "  N: %s\n" % f["note"][:300]
    for e in f["evidence"]:
        s += "  E[%s]: %s\n" % (e["source_id"], e["quote"])
    return s


args = sys.argv[1:]
if args == ["--pairs"]:
    txt = open(W + "reg-analysis.txt").read()
    sec = txt.split("SHARED QUOTE SENTENCES:")[1].split("SIMILAR CLAIMS")[0]
    for line in sec.strip().splitlines():
        m = re.match(r"\s*(\S+) <> (\S+)", line)
        if m:
            print("#### PAIR")
            print(block(m.group(1)) + block(m.group(2)))
else:
    for i in args:
        print(block(i))
