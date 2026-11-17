"""register-24: apply reg-patches/*.json through the saa.py CLI, one command at a time (sequential).
Log: _build/work/24-backup/reg-apply-log.jsonl. Re-runnable: steps that already succeeded are skipped."""
import json, os, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/24-backup/"
LOG = W + "reg-apply-log.jsonl"
BY = "register-24"
SKIP = {"backup-restore-destructive-exceptions-listed"}  # applied by hand

done = set()
if os.path.exists(LOG):
    for line in open(LOG):
        if line.strip():
            r = json.loads(line)
            if r.get("rc") in (0, 2):
                done.add(r["step"])
fails = 0
for fid in [l.strip() for l in open(W + "reg-patches/_list.txt") if l.strip()]:
    if fid in SKIP or fid in done:
        continue
    argv = ["facts", "amend", fid, "--file", "aws-saa-book/_build/work/24-backup/reg-patches/%s.json" % fid,
            "--reason", "register-24: displays cut to verbatim phrases of at most 8 words; relevance, tier0 or hard made consistent",
            "--by", BY]
    p = subprocess.run([sys.executable, ROOT + "/tools/saa.py"] + argv, cwd=REPO, capture_output=True, text=True)
    rec = {"step": fid, "rc": p.returncode, "out": (p.stdout or "")[-1500:], "err": (p.stderr or "")[-800:]}
    with open(LOG, "a") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if p.returncode not in (0, 2):
        fails += 1
        print("FAIL", fid, (p.stdout or p.stderr or "").strip()[:600], flush=True)
print("fails", fails)
