"""register-32: apply reg-decisions.json through the saa.py CLI, one command at a time.
Every change goes through `saa.py facts amend`; this script only sequences the calls and logs
each result to reg-apply.log.jsonl. Arguments: ids to skip."""
import json, subprocess, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/32-step-functions/"
SAA = [sys.executable, B + "/tools/saa.py"]
D = json.load(open(W + "reg-decisions.json"))
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


for i in D["patch_ids"]:
    if i in skip:
        continue
    run(["facts", "amend", i, "--file", "aws-saa-book/_build/work/32-step-functions/reg-patches/%s.json" % i,
         "--reason", "register-32: displays shortened to verbatim quote phrases of at most 8 words, claim, evidence or scope made consistent (reg_gen.py)",
         "--by", "register-32", "--json"], "amend " + i)
for o, n, why in D["supersede"]:
    if o in skip:
        continue
    run(["facts", "amend", o, "--supersede", n, "--reason", "register-32: " + why, "--by", "register-32", "--json"], "supersede %s -> %s" % (o, n))
print("FAILS", len(fails))
for f in fails:
    print(json.dumps(f)[:1500])
