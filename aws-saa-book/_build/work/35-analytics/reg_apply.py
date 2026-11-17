"""register-35: apply reg-build-report.json through the saa.py CLI, one command at a time.
Writes a log to _build/work/35-analytics/reg-apply-log.jsonl; a rerun skips the steps that already succeeded."""
import json, os, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
LOG = W + "reg-apply-log.jsonl"
BY = "register-35"
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
    print(step, p.returncode, (p.stdout or "").strip().splitlines()[:1], flush=True)


for old, new, why in R["supersede"]:
    run("supersede:" + old, ["facts", "amend", old, "--supersede", new, "--reason", "register-35 duplicate: " + why, "--by", BY])
for fid in R["patches"]:
    run("patch:" + fid, ["facts", "amend", fid, "--file", "aws-saa-book/_build/work/35-analytics/reg-patches/" + fid + ".json",
                         "--reason", "register-35: displays shortened to verbatim quote phrases, scope filled, duplicates merged", "--by", BY])
for cf, why in R["conflicts_both"].items():
    run("conflict:" + cf, ["facts", "conflicts", "--resolve", cf, "--both", "--reason", "register-35: " + why])
print("finished", flush=True)
