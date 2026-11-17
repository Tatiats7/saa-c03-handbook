"""register-17: merge the miners' demand statuses into brief.v0.json, mapping retired fact ids to the kept ones."""
import json
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/17-auto-scaling/"
facts = {}
for s in ["ec2-auto-scaling", "aws-auto-scaling", "ec2"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


def resolve(i):
    seen = set()
    while i in facts and facts[i]["status"] == "superseded" and i not in seen:
        seen.add(i)
        i = facts[i].get("superseded_by") or i
    if i not in facts or facts[i]["status"] == "rejected":
        return None
    return i


miner = {}
for n in ["mine-numbers.json", "mine-behavior.json", "mine-faq.json", "mine-decisions+changes.json"]:
    d = json.load(open(W + n))
    dem = d["demand"]
    items = dem.items() if isinstance(dem, dict) else [(x["id"], x) for x in dem]
    for k, v in items:
        miner[k] = dict(v, lens_file=n)

extra = {
    "d82": {"status": "filled", "add": ["ec2-auto-scaling-imds-target-lifecycle-state"],
            "note": "register-17: fetched retrieving-target-lifecycle-state-through-imds and added ec2-auto-scaling-imds-target-lifecycle-state. SIGTERM is not mentioned on the AWS pages searched (gracefully-handle-instance-termination, lifecycle hook pages); do not teach it as an AWS statement."},
    "d28": {"status": "filled", "add": ["ec2-auto-scaling-target-tracking-creates-two-alarms"],
            "note": "register-17: the alarm count is on scale-sqs-queue-cli (fetched): a target tracking policy creates two alarms, one for scaling out and one for scaling in."},
    "d78": {"status": "partial",
            "note": "register-17: TechnologyOne and BurdaForward case pages redirect to the generic Customer Success Stories index (miner, 2026-10-12); a corpus search on 2026-10-12 found only the case-study listing API rows, no case text. NASA JPL and Canva used instead."},
}
brief = json.load(open(W + "brief.v0.json"))
counts = {}
for item in brief["demand"]:
    m = miner.get(item["id"])
    if not m:
        item["status"] = "not-found"
        item["note"] = "register-17: no miner record"
    else:
        st = m.get("status")
        st = {"partly-filled": "partial"}.get(st, st)
        ids = []
        for i in m.get("facts", []):
            r = resolve(i)
            if r and r not in ids:
                ids.append(r)
        e = extra.get(item["id"], {})
        for i in e.get("add", []):
            if i not in ids:
                ids.append(i)
        item["facts"] = ids
        item["status"] = e.get("status", st)
        notes = [x for x in [m.get("note"), e.get("note")] if x]
        if m.get("not_found"):
            notes.append("not found: " + json.dumps(m["not_found"]))
        if notes:
            item["note"] = " | ".join(notes)
        if not ids and item["status"] == "filled":
            item["status"] = "not-found"
    item["registered_by"] = "register-17"
    counts[item["status"]] = counts.get(item["status"], 0) + 1
brief["note"] = (brief.get("note") or "") + " | register-17 (2026-10-12): demand statuses merged from the four mine-*.json files; superseded fact ids mapped to the kept facts."
json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
print(counts)
