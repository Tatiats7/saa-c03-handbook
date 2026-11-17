"""register-35: close the open conflicts that touch chapter 35 facts with --both (every pair was checked: different
quotas, rows, editions, deployment options or versions, a dated change next to its current-truth fact, or a pair whose
other fact was already superseded at registration). Logs to reg-conflicts-log.jsonl."""
import json, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange"]
facts = {}
for s in SERVICES:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f
ch35 = {i for i, f in facts.items() if str(f.get("home_chapter")) == "35"}


def reason(a, b):
    fa, fb = facts[a], facts[b]
    if "superseded" in (fa["status"], fb["status"]):
        return "one fact of the pair was superseded at registration as a duplicate"
    if fa["kind"] == "change" or fb["kind"] == "change":
        return "different dated changes, or a dated change next to its current-truth fact"
    if "-quota-" in a or "-quota-" in b:
        return "different quotas (different rows of the quota table)"
    if "-worker-" in a:
        return "different worker types (different rows)"
    if "-sla-" in a:
        return "different deployment options with their own SLA commitments"
    if "-price-" in a or "-price-" in b:
        return "different billed resources (crawler, development endpoint, ETL job) with their own minimums"
    return "different scope: different editions, sizes, releases or resources"


for line in open(ROOT + "/_build/facts/conflicts.jsonl"):
    if not line.strip():
        continue
    c = json.loads(line)
    if c.get("status") != "open" or not any(x in ch35 for x in c["facts"]):
        continue
    a, b = c["facts"]
    why = reason(a, b)
    p = subprocess.run([sys.executable, ROOT + "/tools/saa.py", "facts", "conflicts", "--resolve", c["id"], "--both",
                        "--reason", "register-35: " + why], cwd=REPO, capture_output=True, text=True)
    with open(W + "reg-conflicts-log.jsonl", "a") as fh:
        fh.write(json.dumps({"id": c["id"], "facts": c["facts"], "reason": why, "rc": p.returncode, "out": p.stdout[-300:], "err": p.stderr[-300:]}) + "\n")
    print(c["id"], p.returncode, why, flush=True)
