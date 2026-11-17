"""register-18: apply reg-decisions.json through the saa.py CLI, one command at a time.

Every change goes through `saa.py facts amend` or `saa.py facts conflicts`; this script
only sequences the calls and logs each result to reg-apply.log.jsonl.
"""
import json, subprocess, sys, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/18-lambda/"
SAA = [sys.executable, B + "/tools/saa.py"]
D = json.load(open(W + "reg-decisions.json"))
ids = json.load(open(W + "reg-patch-ids.json"))
skip = set(sys.argv[1:])
log = open(W + "reg-apply.log.jsonl", "a")
conf = {}
for line in open(B + "/_build/facts/conflicts.jsonl"):
    if line.strip():
        c = json.loads(line)
        conf[c["id"]] = c


def run(args, what):
    r = subprocess.run(SAA + args, cwd=ROOT, capture_output=True, text=True)
    rec = {"what": what, "code": r.returncode, "out": r.stdout[-1500:], "err": r.stderr[-800:]}
    log.write(json.dumps(rec) + "\n")
    log.flush()
    print(r.returncode, what)
    return r.returncode


for i in ids:
    if i in skip:
        continue
    run(["facts", "amend", i, "--file", "aws-saa-book/_build/work/18-lambda/reg-patches/%s.json" % i,
         "--reason", "register-18: displays, scope, claim or relevance made consistent (reg-decisions.json)",
         "--by", "register-18", "--json"], "amend " + i)
for o, n, why in D["supersede"]:
    run(["facts", "amend", o, "--supersede", n, "--reason", "register-18: " + why, "--by", "register-18", "--json"], "supersede %s -> %s" % (o, n))
for i, why in D["reject"]:
    run(["facts", "amend", i, "--reject", "--reason", "register-18: " + why, "--by", "register-18", "--json"], "reject " + i)
for cf, why in D["conflicts_both"]:
    keep = conf[cf]["facts"][0]
    run(["facts", "conflicts", "--resolve", cf, "--keep", keep, "--both", "--reason", "register-18: " + why], "conflict " + cf)
