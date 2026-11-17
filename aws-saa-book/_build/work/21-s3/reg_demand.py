"""register-21: merge the miners' demand mappings into brief.v0.json (statuses found / partial / not-found)."""
import json, sys
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/21-s3/"
WRITE = len(sys.argv) > 1 and sys.argv[1] == "--write"

facts = {}
for p in ["s3", "s3-glacier"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % p):
        if line.strip():
            f = json.loads(line)
            facts[f["id"]] = f


ALIAS = {  # facts rejected in favour of a kept duplicate (conflict --keep, or reject)
    "s3-faq-replication-delete-markers": "s3-replication-delete-markers-optional",
    "s3-transfer-acceleration-use-cases": "s3-transfer-acceleration-when-to-use",
    "s3-lifecycle-no-charge-after-expiration": "s3-lifecycle-expired-object-not-charged",
    "s3-faq-mrap-17-regions": "s3-mrap-regions-max",
}


def live(i, seen=None):
    """Follow superseded_by; drop rejected and unknown ids."""
    seen = seen or set()
    if i in ALIAS:
        i = ALIAS[i]
    f = facts.get(i)
    if f is None or i in seen:
        return None
    seen.add(i)
    if f["status"] == "superseded":
        return live(f.get("superseded_by"), seen)
    if f["status"] == "rejected":
        return None
    return i


m = {}       # demand id -> {"facts": set, "flags": [(lens, status, note)]}


def add(did, ids, lens, status=None, note=None):
    e = m.setdefault(did, {"facts": [], "flags": []})
    for i in ids or []:
        j = live(i)
        if j and j not in e["facts"]:
            e["facts"].append(j)
    if status:
        e["flags"].append((lens, status, note))


faq = json.load(open(W + "mine-faq.json"))
for did, ids in faq["demand"].items():
    add(did, ids, "faq")
add("d076", ["s3-event-notifications-at-least-once-seconds", "s3-event-notifications-no-order-duplicates"], "register")
for did, v in faq.get("not_found", {}).items():
    add(did, [], "faq", "not-found", v.get("where") if isinstance(v, dict) else v)
for did, note in faq.get("partial", {}).items():
    add(did, [], "faq", "partial", note)
for lens in ["numbers", "behavior"]:
    d = json.load(open(W + "mine-%s.json" % lens))["demand"]
    for did, v in d.items():
        add(did, v.get("facts"), lens, None if v.get("status") in ("answered", "found") else v.get("status"), v.get("note") or v.get("not_found"))
for lens in ["decisions", "changes"]:
    d = json.load(open(W + "mine-%s.json" % lens))["demand"]
    for v in d:
        st = v.get("status")
        add(v["id"], (v.get("facts") or []) + (v.get("replaced_by") or []), lens,
            None if st in ("answered", "found") else st, v.get("note") or v.get("not_found"))

# registrar judgements on flags (see register-21.json for the reasons)
override = {
    "d076": ("found", "FAQ lens found nothing; the behavior lens covers delivery (at least once, seconds, no ordering) from the user guide"),
    "d065": ("found", "FAQ is partial; the pricing page facts state data in from the internet is free and same-Region transfer is free"),
    "d091": ("found", "Macie from the FAQ; GuardDuty S3 protection from the security best practices page (s3-guardduty-s3-protection-cloudtrail-events)"),
    "d144": ("found", "algorithms from the FAQ; the December 2024 default from s3-change-crc64nvme-default-checksum-2024-12"),
    "d146": ("partial", "no AWS page found that states the accelerated path is encrypted; facts say same security as regular transfers and no data kept at edge locations"),
    "d009": ("partial", "no AWS page says which bucket type the exam means; facts give the four types and that general purpose buckets are the original type recommended for most use cases"),
    "d070": ("partial", "no AWS page compares batch with individual uploads; request charges, multipart upload and parallel connections are grounded"),
    "d088": ("partial", "the guide gives no explicit rule for bucket policy vs user policy; grounded: either works in one account, bucket policies for cross-account grants, 20 KB size limit, access points for policy space"),
    "d161": ("partial", "closing date 2025-12-15 not found in a saved AWS page; the guide notice and the maintenance list date 2025-10-07 are grounded"),
    "d156": ("not-found", "the Pomelo case study page now redirects to the generic listing; replaced by the Bynder S3 Intelligent-Tiering case study"),
    "d157": ("not-found", "the Dropsuite case study page now redirects to the generic listing; replaced by the Snap S3 Glacier Instant Retrieval case study"),
}

b = json.load(open(W + "brief.v0.json"))
out = []
counts = {}
for d in b["demand"]:
    e = m.get(d["id"], {"facts": [], "flags": []})
    st, note = None, None
    if d["id"] in override:
        st, note = override[d["id"]]
    elif e["flags"]:
        st = e["flags"][0][1]
        note = e["flags"][0][2]
        if st in ("answered",):
            st = "found"
    elif e["facts"]:
        st = "found"
    else:
        st = "not-found"
        note = "no miner mapped a fact"
    d["status"] = st
    d["facts"] = e["facts"]
    if note:
        d["note"] = note
    d["registered_by"] = "register-21"
    counts[st] = counts.get(st, 0) + 1
    if st != "found" or not e["facts"]:
        out.append((d["id"], st, len(e["facts"]), note))
print(counts)
for x in out:
    print(x)
if WRITE:
    b.setdefault("notes", [])
    if isinstance(b["notes"], list):
        b["notes"].append("2026-10-12 register-21: demand statuses set from the five miner notes after the merge (superseded ids followed to the kept fact)")
    json.dump(b, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
    print("written")
