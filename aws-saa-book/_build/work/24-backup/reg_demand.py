"""register-24: write demand statuses into brief.v0.json from the miners' mine-*.json notes and the registrar merges.
Usage: python3 -I reg_demand.py"""
import json, re, glob

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/24-backup/"

SUPERSEDED = {
 "backup-restore-creates-new-resource-protects-existing": "backup-restore-destructive-exceptions-listed",
 "backup-copy-one-job-per-resource-created-status": "backup-copy-one-job-at-a-time-per-resource",
 "backup-restore-testing-automated-periodic-viability": "backup-restore-testing-automated-periodic-evaluation",
 "backup-search-results-retained-7-days": "backup-search-results-kept-7-days-export-to-s3",
 "backup-search-metadata-granular-files-objects": "backup-search-find-files-or-objects-without-full-restore",
 "backup-restore-cold-takes-4-hours-more": "backup-restore-from-cold-storage-takes-longer",
 "backup-tiering-only-s3-supports": "backup-s3-only-resource-with-backup-tiering",
 "backup-tiering-s3-lower-cost-warm-tier-same-performance": "backup-tiering-s3-lower-cost-tier-up-to-30-percent",
 "backup-quota-legal-holds-per-account": "backup-legal-hold-max-50-active-per-account",
 "backup-legal-hold-definition-prevents-deletion": "backup-legal-hold-prevents-deletion-delays-lifecycle",
 "backup-malware-scanning-provided-by-guardduty": "backup-malware-scanning-by-guardduty-automate-or-on-demand",
 "backup-pitr-rds-multi-az-clusters-not-supported": "backup-continuous-rds-supported-not-multi-az-clusters",
 "backup-pitr-one-continuous-backup-per-resource": "backup-continuous-one-per-resource-redundant-extra",
 "backup-cold-transition-setting-locked-after-transition": "backup-cold-storage-transition-setting-cannot-change",
 "backup-lag-vault-key-aws-owned-default-or-customer-managed": "backup-lag-vault-encryption-key-and-compliance-lock",
 "backup-pitr-continuous-35-days-1-second-precision": "backup-pitr-restore-rewinds-to-chosen-time",
 "backup-audit-manager-report-every-24-hours": "backup-audit-manager-frameworks-and-daily-reports",
 "backup-cold-incremental-needs-warm-full-backup": "backup-cold-storage-incremental-warm-full-8-days",
}
ADDED = {
 "d014": ["backup-lag-vault-jobs-fail-outside-min-max-retention"],
 "d011": ["backup-pricing-s3-extra-charges-versioning-requests-eventbridge"],
 "d012": ["backup-pricing-s3-extra-charges-versioning-requests-eventbridge"],
}
REG_NOTES = {
 "d010": "Registrar search (2026-10-14): no saved page states object size rules for S3 backup tiering beyond the 128 KB billing minimum; stays partial.",
 "d011": "Registrar search: per-GB rates stay unquoted (script-rendered on the pricing page). Added the pricing-page note on extra S3 charges (Versioning, GET/LIST requests, EventBridge).",
 "d012": "Registrar search: neither the pricing page nor metering-and-billing says that only changed data is billed after the first full backup; the incremental and warm-retention facts cover the behavior. Added the S3 extra-charges fact.",
 "d014": "Registrar search: no maximum value for the maximum retention of a logically air-gapped vault is stated; added the fact that jobs outside the vault's minimum or maximum retention fail (lag-vault-primary-backup troubleshooting).",
 "d021": "The preview start (2023-08-09) is only in a What's New post that robots.txt blocks; not stored.",
}

# facts of every namespace
live = {}
for p in glob.glob(ROOT + "/data/facts/*.jsonl"):
    for line in open(p):
        if line.strip():
            f = json.loads(line)
            live[f["id"]] = f["status"]

notes = {}
for name in ("mine-numbers+changes.json", "mine-behavior+decisions.json", "mine-faq.json"):
    d = json.load(open(W + name))
    for did, item in d["demand"].items():
        notes[did] = (name, item)

brief = json.load(open(W + "brief.v0.json"))
problems = []
counts = {}
for dm in brief["demand"]:
    did = dm["id"]
    if did not in notes:
        problems.append(did + ": no miner note")
        continue
    src, item = notes[did]
    ids = []
    for raw in item.get("facts", []):
        for tok in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", raw):
            if tok in live or tok in SUPERSEDED:
                tok = SUPERSEDED.get(tok, tok)
                if tok not in ids:
                    ids.append(tok)
    for extra in ADDED.get(did, []):
        if extra not in ids:
            ids.append(extra)
    for i in ids:
        st = live.get(i)
        if st is None:
            problems.append("%s: unknown fact %s" % (did, i))
        elif st in ("rejected", "superseded"):
            problems.append("%s: retired fact %s" % (did, i))
    status = item.get("status", "filled")
    text = []
    for k in ("note", "not_found", "contradicted"):
        if item.get(k):
            text.append(("%s: %s" % (k, item[k])) if k != "note" else item[k])
    if did in REG_NOTES:
        text.append(REG_NOTES[did])
    dm["status"] = status
    dm["facts"] = ids
    dm["note"] = " ".join(text) if text else None
    dm["registered_by"] = "register-24"
    dm["mined_by"] = src.replace("mine-", "").replace(".json", "")
    counts[status] = counts.get(status, 0) + 1

brief["register"] = {"by": "register-24", "date": "2026-10-14", "demand_counts": counts}
json.dump(brief, open(W + "brief.v0.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps(counts))
for p in problems:
    print("PROBLEM", p)
