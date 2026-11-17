"""register-17: run the planned saa.py commands one after another (each one a separate, plain CLI call).

Reads reg-plan.json (written by reg_build.py --write). Logs every command and its output to reg-run.log.
Usage: python3 reg_run.py amend|retire|resolve
"""
import json, subprocess, sys
REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
W = "aws-saa-book/_build/work/17-auto-scaling/"
SAA = "aws-saa-book/tools/saa.py"
plan = json.load(open(REPO + "/" + W + "reg-plan.json"))
phase = sys.argv[1]
cmds = []
if phase == "amend":
    for i in plan["amend"]:
        cmds.append(["facts", "amend", i, "--file", W + "reg-patches/" + i + ".json", "--by", "register-17",
                     "--reason", "register-17: registrar merge (short verbatim displays, scope, merged duplicates, claims cut to their quotes)"])
elif phase == "retire":
    for old, new, why in plan["supersede"]:
        cmds.append(["facts", "amend", old, "--supersede", new, "--by", "register-17", "--reason", "register-17 duplicate: " + why])
    for i, why in plan["reject"]:
        cmds.append(["facts", "amend", i, "--reject", "--by", "register-17", "--reason", "register-17: " + why])
elif phase == "resolve":
    dec = json.load(open(REPO + "/" + W + "reg-decisions.json"))
    for cf, keep, both, other, why in dec["resolve"]:
        if both:
            cmds.append(["facts", "conflicts", "--resolve", cf, "--both", "--reason", "register-17: " + why])
        else:
            cmds.append(["facts", "conflicts", "--resolve", cf, "--keep", keep, "--reason", "register-17: " + why])
    for cf in dec["resolve_both_per_call_quotas"]:
        cmds.append(["facts", "conflicts", "--resolve", cf, "--both", "--reason",
                     "register-17: different scope: per-API-call array limits of different operations (rows of the quotas table)"])
fails = 0
with open(REPO + "/" + W + "reg-run-%s.log" % phase, "w") as log:
    for c in cmds:
        r = subprocess.run([sys.executable, SAA] + c, cwd=REPO, capture_output=True, text=True)
        log.write("$ saa.py %s\nexit=%d\n%s%s\n" % (" ".join(c[:3]), r.returncode, r.stdout, r.stderr))
        if r.returncode != 0:
            fails += 1
            print("FAIL", " ".join(c[:3]), r.returncode, (r.stdout + r.stderr).strip()[:600])
print(phase, "commands:", len(cmds), "failed:", fails)
