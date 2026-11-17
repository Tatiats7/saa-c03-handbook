"""register-27: apply reg-decisions.json and reg-patches/ through the saa.py CLI, one command at a time.
Log: _build/work/27-aurora/reg-apply-log.jsonl. Re-runnable: steps that already succeeded (rc 0 or 2) are skipped."""
import json, os, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/27-aurora/"
LOG = W + "reg-apply-log.jsonl"
BY = "register-27"
D = json.load(open(W + "reg-decisions.json"))
R = json.load(open(W + "reg-build-report.json"))

done = set()
if os.path.exists(LOG):
    for line in open(LOG):
        if line.strip():
            r = json.loads(line)
            if r.get("rc") in (0, 2):
                done.add(r["step"])
fails = 0


def run(step, argv):
    global fails
    if step in done:
        return
    p = subprocess.run([sys.executable, ROOT + "/tools/saa.py"] + argv, cwd=REPO, capture_output=True, text=True)
    rec = {"step": step, "rc": p.returncode, "out": (p.stdout or "")[-800:], "err": (p.stderr or "")[-800:]}
    with open(LOG, "a") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if p.returncode not in (0, 2):
        fails += 1
    print(step, p.returncode, (p.stdout or p.stderr or "").strip().splitlines()[:1], flush=True)


for cf, why in D["conflicts_both"].items():
    run("conflict:" + cf, ["facts", "conflicts", "--resolve", cf, "--both", "--reason", "register-27: " + why])
for old, new, why in D["supersede"]:
    run("supersede:" + old, ["facts", "amend", old, "--supersede", new, "--reason", "register-27 duplicate or namespace: " + why, "--by", BY])
for fid, why in D["reject"]:
    run("reject:" + fid, ["facts", "amend", fid, "--reject", "--reason", "register-27: " + why, "--by", BY])
for fid in R["patches"]:
    run("patch:" + fid, ["facts", "amend", fid, "--file", "aws-saa-book/_build/work/27-aurora/reg-patches/" + fid + ".json",
                         "--reason", "register-27: scope, displays (verbatim, at most 8 words), hard, bullets or relevance made consistent", "--by", BY])
print("finished, failures:", fails)
