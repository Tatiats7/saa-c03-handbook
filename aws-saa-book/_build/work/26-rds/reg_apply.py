"""register-26: apply reg-decisions.json and reg-patches/ through the saa.py CLI, one command at a time.
Writes a log to _build/work/26-rds/reg-apply-log.jsonl. Run once; it skips facts already retired or already patched (by log)."""
import json, os, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/26-rds/"
LOG = W + "reg-apply-log.jsonl"
BY = "register-26"
D = json.load(open(W + "reg-decisions.json"))
R = json.load(open(W + "reg-build-report.json"))

done = set()
if os.path.exists(LOG):
    for line in open(LOG):
        if line.strip():
            r = json.loads(line)
            if r.get("rc") in (0, 2):
                done.add(r["step"])


def run(step, argv):
    if step in done:
        return
    p = subprocess.run([sys.executable, ROOT + "/tools/saa.py"] + argv, cwd=REPO, capture_output=True, text=True)
    rec = {"step": step, "rc": p.returncode, "out": (p.stdout or "")[-600:], "err": (p.stderr or "")[-600:]}
    with open(LOG, "a") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(step, p.returncode, (p.stdout or "").strip().splitlines()[:1])


for old, new, why in D["supersede"]:
    run("supersede:" + old, ["facts", "amend", old, "--supersede", new, "--reason", "register-26 duplicate: " + why, "--by", BY])
for fid, why in D["reject"]:
    run("reject:" + fid, ["facts", "amend", fid, "--reject", "--reason", "register-26: " + why, "--by", BY])
for fid in R["patches"]:
    run("patch:" + fid, ["facts", "amend", fid, "--file", "aws-saa-book/_build/work/26-rds/reg-patches/" + fid + ".json",
                         "--reason", "register-26: scope, displays, hard, bullets or relevance made consistent", "--by", BY])
for cf, why in D["conflicts_both"].items():
    run("conflict:" + cf, ["facts", "conflicts", "--resolve", cf, "--both", "--reason", "register-26: " + why])
print("finished")
