"""register-12: apply reg-decisions.json through the saa.py CLI, one command at a time (adapted from register-19).

Every change goes through `saa.py facts amend` or `saa.py facts conflicts`; this script only sequences the calls
and logs each result to reg-apply.log.jsonl. Arguments: ids to skip. Steps: amends, supersedes, rejects, conflicts.
"""
import json, subprocess, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/12-hybrid-networking/"
SAA = [sys.executable, B + "/tools/saa.py"]
D = json.load(open(W + "reg-decisions.json"))
ids = json.load(open(W + "reg-patch-ids.json"))
skip = set(sys.argv[1:])
log = open(W + "reg-apply.log.jsonl", "a")
fails = []


def run(args, what):
    r = subprocess.run(SAA + args, cwd=ROOT, capture_output=True, text=True)
    rec = {"what": what, "code": r.returncode, "out": r.stdout[-1500:], "err": r.stderr[-800:]}
    log.write(json.dumps(rec) + "\n")
    log.flush()
    if r.returncode not in (0, 2):
        fails.append(rec)
    print(r.returncode, what)
    return r.returncode


for i in ids:
    if i in skip:
        continue
    run(["facts", "amend", i, "--file", "aws-saa-book/_build/work/12-hybrid-networking/reg-patches/%s.json" % i,
         "--reason", "register-12: displays, claim, scope, evidence or relevance made consistent (reg-decisions.json)",
         "--by", "register-12", "--json"], "amend " + i)
for o, n, why in D["supersede"]:
    if o in skip:
        continue
    run(["facts", "amend", o, "--supersede", n, "--reason", "register-12: " + why, "--by", "register-12", "--json"], "supersede %s -> %s" % (o, n))
for i, why in D["reject"]:
    if i in skip:
        continue
    run(["facts", "amend", i, "--reject", "--reason", "register-12: " + why, "--by", "register-12", "--json"], "reject " + i)
print("FAILS", len(fails))
for f in fails:
    print(json.dumps(f)[:1200])
