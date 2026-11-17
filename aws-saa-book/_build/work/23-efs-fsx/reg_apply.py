"""register-23: apply reg-decisions.json through the saa.py CLI, one command at a time (adapted from register-18).

Every change goes through `saa.py facts amend` or `saa.py facts conflicts`; this script only sequences the
calls and logs each result to reg-apply.log.jsonl. Phase argument: `facts` (amend, supersede, reject) or
`conflicts` (close every open conflict that touches a chapter 23 fact).
"""
import json, subprocess, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
B = ROOT + "/aws-saa-book"
W = B + "/_build/work/23-efs-fsx/"
SAA = [sys.executable, B + "/tools/saa.py"]
LABEL = "register-23"
phase = sys.argv[1]
log = open(W + "reg-apply.log.jsonl", "a")
fails = []


def run(args, what):
    r = subprocess.run(SAA + args, cwd=ROOT, capture_output=True, text=True)
    rec = {"what": what, "code": r.returncode, "out": r.stdout[-1500:], "err": r.stderr[-800:]}
    log.write(json.dumps(rec) + "\n")
    log.flush()
    if r.returncode not in (0, 2):
        fails.append(rec)
    return r.returncode


def load_facts():
    facts = {}
    for svc in ("efs", "fsx"):
        for line in open(B + "/data/facts/%s.jsonl" % svc):
            if line.strip():
                f = json.loads(line)
                facts[f["id"]] = f
    return facts


if phase == "facts":
    D = json.load(open(W + "reg-decisions.json"))
    for i in json.load(open(W + "reg-patch-ids.json")):
        run(["facts", "amend", i, "--file", "aws-saa-book/_build/work/23-efs-fsx/reg-patches/%s.json" % i,
             "--reason", LABEL + ": displays (verbatim, at most 8 words), bullets, relevance or notes made consistent (reg-decisions.json)",
             "--by", LABEL, "--json"], "amend " + i)
    for o, n, why in D["supersede"]:
        run(["facts", "amend", o, "--supersede", n, "--reason", LABEL + ": " + why, "--by", LABEL, "--json"],
            "supersede %s -> %s" % (o, n))
    for i, why in D["reject"]:
        run(["facts", "amend", i, "--reject", "--reason", LABEL + ": " + why, "--by", LABEL, "--json"], "reject " + i)

elif phase == "conflicts":
    facts = load_facts()
    special = json.load(open(W + "reg-conflict-reasons.json"))
    conf = [json.loads(l) for l in open(B + "/_build/facts/conflicts.jsonl") if l.strip()]
    for c in conf:
        if c["status"] != "open" or not any(facts.get(x, {}).get("home_chapter") == "23" for x in c["facts"]):
            continue
        a, b = c["facts"]
        fa, fb = facts.get(a), facts.get(b)
        live = [x for x in (a, b) if facts.get(x) and facts[x]["status"] not in ("rejected", "superseded")]
        if len(live) == 1:
            other = b if live[0] == a else a
            st = facts[other]["status"] if other in facts else "missing"
            run(["facts", "conflicts", "--resolve", c["id"], "--keep", live[0], "--reason",
                 "%s: %s is %s (duplicate merged or wrong value rejected)" % (LABEL, other, st)], "conflict keep " + c["id"])
            continue
        if not live:
            run(["facts", "conflicts", "--resolve", c["id"], "--keep", a, "--both", "--reason",
                 LABEL + ": both facts already retired"], "conflict both-retired " + c["id"])
            continue
        why = special.get(c["id"])
        if why is None:
            sa = (fa.get("qualifiers") or {}).get("scope") or fa["kind"]
            sb = (fb.get("qualifiers") or {}).get("scope") or fb["kind"]
            why = "different scope: separate quota, limit or table rows (%s: %s; %s: %s)" % (a, sa, b, sb)
        run(["facts", "conflicts", "--resolve", c["id"], "--keep", a, "--both", "--reason", LABEL + ": " + why],
            "conflict both " + c["id"])

print("fails", len(fails))
for f in fails:
    print(json.dumps(f)[:600])
