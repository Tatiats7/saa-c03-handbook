"""register-12: close the open conflicts of chapter 12 through `saa.py facts conflicts --resolve`, one call each.

Explicit decisions come from reg-decisions.json "conflicts" ([cf, keep id or BOTH-OR-CLOSE, reason]); every other
open conflict of the chapter is closed with --both and "conflicts_both_reason" (different scope). Log: reg-apply.log.jsonl.
"""
import json, subprocess, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/12-hybrid-networking/"
SAA = [sys.executable, B + "/tools/saa.py"]
D = json.load(open(W + "reg-decisions.json"))
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
mine = set()
for s in SVCS:
    for line in open(B + "/data/facts/%s.jsonl" % s):
        if line.strip():
            mine.add(json.loads(line)["id"])
explicit = {c: (k, r) for c, k, r in D["conflicts"]}
log = open(W + "reg-apply.log.jsonl", "a")
fails = []
for line in open(B + "/_build/facts/conflicts.jsonl"):
    if not line.strip():
        continue
    c = json.loads(line)
    if c.get("status") != "open" or not any(x in mine for x in c["facts"]):
        continue
    if c["id"] in explicit:
        keep, reason = explicit[c["id"]]
        args = ["--both"] if keep == "BOTH-OR-CLOSE" else ["--keep", keep]
    else:
        reason = D["conflicts_both_reason"]
        args = ["--both"]
    cmd = ["facts", "conflicts", "--resolve", c["id"]] + args + ["--reason", "register-12: " + reason, "--json"]
    r = subprocess.run(SAA + cmd, cwd=ROOT, capture_output=True, text=True)
    rec = {"what": "conflict %s %s" % (c["id"], " ".join(args)), "code": r.returncode, "out": r.stdout[-600:], "err": r.stderr[-400:]}
    log.write(json.dumps(rec) + "\n")
    print(r.returncode, rec["what"])
    if r.returncode != 0:
        fails.append(rec)
print("FAILS", len(fails))
for f in fails:
    print(json.dumps(f)[:800])
