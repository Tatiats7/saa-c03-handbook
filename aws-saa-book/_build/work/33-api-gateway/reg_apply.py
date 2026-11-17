"""register-33: apply reg-decisions.json through the saa.py CLI, one command at a time.

Every change goes through `saa.py facts amend`; this script only sequences the calls and
logs each result to reg-apply.log.jsonl.
Run: python3 -I aws-saa-book/_build/work/33-api-gateway/reg_apply.py <repo root>
"""
import json, subprocess, sys

ROOT = sys.argv[1]
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/33-api-gateway/"
SAA = [sys.executable, B + "/tools/saa.py"]
D = json.load(open(W + "reg-decisions.json"))
log = open(W + "reg-apply.log.jsonl", "a")
fails = 0


def run(args, what):
    global fails
    r = subprocess.run(SAA + args, cwd=ROOT, capture_output=True, text=True)
    rec = {"what": what, "code": r.returncode, "out": r.stdout[-1500:], "err": r.stderr[-800:]}
    log.write(json.dumps(rec) + "\n")
    log.flush()
    if r.returncode not in (0, 2):
        fails += 1
        print("FAIL", r.returncode, what, (r.stdout + r.stderr)[-600:])
    return r.returncode


for i in D["patch_ids"]:
    run(["facts", "amend", i, "--file", "aws-saa-book/_build/work/33-api-gateway/reg-patches/%s.json" % i,
         "--reason", "register-33: displays shortened to verbatim phrases, scope or duplicates made consistent (reg-decisions.json)",
         "--by", "register-33", "--json"], "amend " + i)
for o, n, why in D["supersede"]:
    run(["facts", "amend", o, "--supersede", n, "--reason", "register-33: duplicate; " + why, "--by", "register-33", "--json"],
        "supersede %s -> %s" % (o, n))
print("done; failures:", fails)
