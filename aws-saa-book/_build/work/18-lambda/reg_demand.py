"""register-18: merge the miners' demand statuses into brief.v0.json (found / partial / not-found)."""
import json
B = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/"
W = B + "_build/work/18-lambda/"
brief = json.load(open(W + "brief.v0.json"))
facts = {}
for line in open(B + "data/facts/lambda.jsonl"):
    if line.strip():
        f = json.loads(line)
        facts[f["id"]] = f
other = {}
for line in open(B + "data/facts/rds-proxy.jsonl"):
    if line.strip():
        f = json.loads(line)
        other[f["id"]] = f


def live(i):
    """Follow supersede links; drop rejected facts."""
    seen = 0
    while seen < 5:
        f = facts.get(i) or other.get(i)
        if f is None:
            return None
        if f["status"] == "superseded":
            i = f["superseded_by"]
            seen += 1
            continue
        if f["status"] == "rejected":
            return None
        return i
    return None


got = {}


def put(did, status, ids, note=None):
    g = got.setdefault(did, {"status": None, "facts": [], "notes": []})
    order = {"found": 0, "partial": 1, "not-found": 2}
    if g["status"] is None or order[status] < order[g["status"]]:
        g["status"] = status
    for i in ids:
        if i not in g["facts"]:
            g["facts"].append(i)
    if note:
        g["notes"].append(note)


def norm(s):
    s = s.lower()
    if s == "filled":
        return "found"
    if s.startswith("contradicted"):
        return "partial"
    return s


beh = json.load(open(W + "mine-behavior.json"))
for x in beh["demand"]:
    put(x["id"], norm(x["status"]), x.get("facts", []), x.get("note"))
num = json.load(open(W + "mine-numbers.json"))
for did, x in num["demand"].items():
    n = " ".join(filter(None, [x.get("note"), x.get("not_found"), x.get("contradiction")])) or None
    put(did, norm(x["status"]), x.get("facts", []), n)
faq = json.load(open(W + "mine-faq.json"))
for did, x in faq["demand"].items():
    put(did, norm(x["status"]), x.get("facts", []), x.get("note"))
dc = json.load(open(W + "mine-decisions+changes.json"))
for x in dc["demand"]:
    n = " ".join(filter(None, [x.get("note"), x.get("not_found")])) or None
    put(x["id"], norm(x["status"]), x.get("facts", []), n)

# registrar updates (register-18)
R = {
 "d117": ("found", ["lambda-sqs-execution-role-read-permissions"], "register-18: fetched docs/lambda/latest/dg/testing-guide; the guide names sqs:ReceiveMessage, sqs:DeleteMessage and sqs:GetQueueAttributes as the execution-role actions for reading the queue."),
 "d125": ("found", ["lambda-change-streaming-200-mb-2025", "lambda-payload-streamed-response"], "register-18: found the What's New post of 2025-07-31 (20 MB to 200 MB) through the What's New feed; fetched and adopted as lambda-change-streaming-200-mb-2025."),
 "d050": ("found", ["lambda-async-default-two-retries", "lambda-async-retry-attempts-0-to-2"], "register-18: the FAQ fact 'retried at least 3 times' was rejected (contradicts the guide's two retries, configurable 0 to 2)."),
 "d051": ("found", ["lambda-async-throttle-retry-6-hours"], "register-18: the FAQ fact on 15-30 minutes of burst absorption was rejected (older wording; the guide retries throttled events for up to 6 hours)."),
 "d103": ("found", ["lambda-async-throttle-retry-6-hours"], "register-18: lambda-faq-throttle-async-burst-15-30-min rejected; the guide value is lambda-async-throttle-retry-6-hours."),
 "d084": ("partial", ["lambda-faq-advanced-logging-no-charge"], "register-18: the FAQ says CloudWatch Logs ingestion and storage are still paid (lambda-faq-advanced-logging-no-charge). A NAT gateway charge for VPC functions is not stated on a saved Lambda page; pointer to the VPC chapter."),
 "d087": ("not-found", [], "register-18 search: 'better price performance', '34%' and 'Graviton' over all saved pages; the 34% figure appears only in What's New feed items (not evidence for a capability fact). Keep the claim qualitative."),
 "d115": ("partial", [], "register-18 search: 'GPU' in the full Lambda developer guide gives no statement; do not write 'no GPU' as a fact."),
 "d133": ("found", ["lambda-sqs-provisioned-mode-3x-80x", "lambda-sqs-esm-1250-default-100000-provisioned", "lambda-sqs-provisioned-mode-pollers-range"], "register-18: the 16x and 2-2000 wordings were rejected as older; teach 80x / 100,000 from the current guide."),
 "d044": ("found", [], "register-18: the demand hypothesis (1,000) is contradicted; the guide says 1,250 per event source mapping (100,000 in provisioned mode).")
}
for did, (st, ids, note) in R.items():
    g = got.setdefault(did, {"status": None, "facts": [], "notes": []})
    g["status"] = st
    for i in ids:
        if i not in g["facts"]:
            g["facts"].append(i)
    g["notes"].append(note)

missing = []
for d in brief["demand"]:
    g = got.get(d["id"])
    if g is None:
        missing.append(d["id"])
        continue
    ids = []
    for i in g["facts"]:
        j = live(i)
        if j and j not in ids:
            ids.append(j)
    d["status"] = g["status"] if ids or g["status"] == "not-found" else "not-found"
    d["facts"] = ids
    if g["notes"]:
        d["note"] = " | ".join(g["notes"])
    d["registered_by"] = "register-18"
json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
import collections
print(collections.Counter(d["status"] for d in brief["demand"]))
print("missing", missing)
print([(d["id"], d["status"]) for d in brief["demand"] if d["status"] != "found"])
