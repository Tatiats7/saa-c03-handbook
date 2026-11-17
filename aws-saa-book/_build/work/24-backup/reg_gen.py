"""Registrar patch generator for chapter 24. Usage: python3 -I reg_gen.py
Writes one patch per fact to _build/work/24-backup/reg-patches/<id>.json and a list reg-patches/_list.txt.
Read-only on the fact store."""
import json, os, re, unicodedata

ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
OUT = ROOT + "/_build/work/24-backup/reg-patches"
os.makedirs(OUT, exist_ok=True)


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("**", "").replace("`", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip().lower()


facts = {}
for line in open(ROOT + "/data/facts/backup.jsonl"):
    if line.strip():
        f = json.loads(line)
        facts[f["id"]] = f

# number-free displays cut to verbatim phrases of at most 8 words (RULINGS 2026-10-11); None removes the value
D = {
 "backup-audit-manager-audits-policies-against-controls": {"v1": "audit the compliance of your AWS Backup policies"},
 "backup-audit-manager-control-in-backup-plan": {"v1": "included in at least one backup plan", "v2": "Evaluates if resources are included"},
 "backup-audit-manager-control-in-lag-vault": {"v2": "copied to a logically air-gapped vault"},
 "backup-audit-manager-control-vault-lock": {"v1": "backup plan with an AWS Backup Vault Lock"},
 "backup-audit-manager-findings-into-aws-audit-manager": {"v1": "findings into AWS Audit Manager"},
 "backup-audit-manager-frameworks-and-daily-reports": {"v1": "one or more governance control templates"},
 "backup-audit-manager-needs-resource-tracking-aws-config": {"v2": "AWS Config to track your AWS Backup resources"},
 "backup-audit-manager-pricing-per-control-evaluation-and-config": {"v1": "based on the number of control evaluations"},
 "backup-audit-manager-reports-two-types-job-and-compliance": {"v2": "monitor resource levels or the different controls"},
 "backup-aurora-vault-snapshots-no-charge-condition": {"v1": "does not charge for Aurora snapshots"},
 "backup-automatic-backups-use-plan-lifecycle-vault-and-tags": {"v1": "configured with the lifecycle settings", "v2": "organized in the backup vault"},
 "backup-billing-not-fully-managed-billed-by-service-lag-vault-under-backup": {"v2": "charges occur under AWS Backup"},
 "backup-central-management-needs-opt-in-plan-and-vault": {"v1": "opt in to managing that service"},
 "backup-change-org-policy-redshift-serverless-dsql-2026-04": {"was": "tag-based selections or backing up all resources"},
 "backup-change-vault-lock-governance-mode-2022-10": {"modes": "governance mode for additional IAM protections"},
 "backup-cold-storage-transition-setting-cannot-change": {"rule": "setting cannot be changed after a backup"},
 "backup-cold-storage-update-min-age-plus-one-day": {"rule": "a minimum of the backup’s age"},
 "backup-continuous-cannot-be-scheduled": {"v1": "cannot be scheduled"},
 "backup-continuous-copy-becomes-snapshot-no-pitr": {"v2": "is not available for these copies"},
 "backup-continuous-copy-rule-takes-snapshot-then-copies": {"v1": "takes a snapshot of the resource"},
 "backup-continuous-multiple-rules-multiple-vaults-extra-become-snapshots": {"v1": "according to the first rule processed"},
 "backup-continuous-rds-backup-window-managed-while-aws-backup-manages": {"v2": "near the Amazon RDS maintenance window"},
 "backup-continuous-rds-settings-managed-only-in-aws-backup": {"v1": "can't create or modify continuous backup settings", "v2": "AWS Backup console or the AWS Backup CLI"},
 "backup-continuous-rds-supported-not-multi-az-clusters": {"v1": "does not support continuous backups or point-in-time recovery"},
 "backup-copy-cold-storage-backups-cannot-be-copied": {"v1": "archive tiers cannot be copied"},
 "backup-copy-footnote-rds-multi-az-clusters-no-copy": {"v1": "do not currently support any copy operations"},
 "backup-copy-one-job-at-a-time-per-resource": {"v1": "Only one backup or copy job can run"},
 "backup-cross-account-copy-purpose-recover-deleted-original": {"v1": "from its destination account to its source account"},
 "backup-cross-account-destination-vault-key-policy-and-shared-cmk": {"v2": "share this customer managed key"},
 "backup-cross-account-destination-vault-must-allow-copy-into": {"v2": "will deny attempts to copy"},
 "backup-cross-account-enable-only-with-management-credentials": {"v1": "can only be enabled or disabled"},
 "backup-cross-account-management-components": {"v1": "cross-account monitoring, cross-account backups, backup policies", "v2": "Not all of these elements are available"},
 "backup-cross-account-monitor-all-accounts-in-one-place": {"v1": "all of your accounts in one place"},
 "backup-cross-account-no-cold-tier-copies": {"v1": "does not support cross-account copies"},
 "backup-cross-region-copy-on-demand-or-scheduled": {"v1": "on demand or automatically"},
 "backup-cross-region-first-copy-full-then-incremental": {"v2": "in the same AWS Region will be incremental"},
 "backup-cross-region-no-cold-tier-copies": {"v1": "does not support cross-Region copies"},
 "backup-dashboard-audits-backup-and-restore-activity": {"v1": "audit backup and restore activity"},
 "backup-ddb-advanced-does-not-replace-native-pitr": {"v1": "do not replace or duplicate native DynamoDB point-in-time"},
 "backup-delegated-admin-performs-most-admin-tasks-from-member-account": {"v1": "delegate administration of AWS Backup"},
 "backup-delegated-admin-reduces-management-account-access": {"v1": "minimizes the number of users with access"},
 "backup-ebs-role-that-created-snapshot-must-delete-or-archive": {"v2": "must be used to delete recovery points"},
 "backup-ec2-marketplace-product-code-ami-no-cross-account-copy": {"v1": "can't copy an AMI with a product code"},
 "backup-edit-lifecycle-and-tags-after-creation": {"v1": "change the lifecycle or tags of the backup"},
 "backup-encryption-aurora-row": {"v1": "encrypt the source Amazon Aurora cluster"},
 "backup-encryption-copies-of-unencrypted-aurora-docdb-neptune-unencrypted": {"v2": "Amazon DocumentDB, and Amazon Neptune clusters"},
 "backup-encryption-copy-not-fully-managed-cmk-or-service-key": {"v2": "the managed key of the service"},
 "backup-encryption-copy-uses-destination-vault-key": {"v1": "the KMS key of the target vault"},
 "backup-encryption-cross-account-aws-managed-key-unsupported-not-fully-managed": {"v1": "isn't supported for resources that aren't fully managed", "v2": "an AWS managed key is immutable"},
 "backup-encryption-ddb-without-advanced-row": {"v1": "encrypt the source DynamoDB table"},
 "backup-encryption-ebs-row": {"v1": "used to encrypt the source volume"},
 "backup-encryption-independent-for-fully-managed-types": {"v2": "encryption method other than one determined"},
 "backup-encryption-rds-row": {"v1": "encrypt the source Amazon RDS database"},
 "backup-expired-recovery-points-still-stored-and-billed": {"v1": "continue to store expired recovery points"},
 "backup-faq-audit-manager-purpose": {"v1": "the compliance of your data protection policies"},
 "backup-faq-backup-rule-four-parts": {"v1": "comprised of one or more backup rules"},
 "backup-faq-cloudwatch-dashboards-fallback": {"v1": "Amazon CloudWatch dashboards are included"},
 "backup-faq-delegated-admin-centralize": {"v2": "removing the need for member accounts"},
 "backup-faq-hipaa-eligible-baa": {"v2": "a HIPAA BAA in place with AWS"},
 "backup-faq-key-features-advanced": {"v2": "immutable backup copies with AWS Backup"},
 "backup-faq-lag-vault-definition": {"v1": "vault that store an immutable backup", "v2": "both primary backups and copies of backups"},
 "backup-faq-mpa-access-when-account-inaccessible": {"v1": "even when the account becomes inaccessible"},
 "backup-faq-restore-testing-plan": {"v1": "frequency of restore tests, target start time"},
 "backup-faq-s3-what-is-backed-up": {"v1": "object data, object tags, access control lists (ACLs)"},
 "backup-faq-sns-alerting": {"v2": "a backup succeeds or a restore is initiated"},
 "backup-faq-vault-encrypted-per-region": {"v2": "each AWS Region where AWS Backup is available"},
 "backup-faq-vault-lock-grace-time": {"v1": "the grace time has not expired"},
 "backup-faq-vault-lock-new-recovery-points-and-failed-jobs": {"v2": "fail all backup jobs"},
 "backup-faq-vault-lock-three-properties": {"v2": "minimum acceptable retention days, maximum acceptable retention days"},
 "backup-faq-vault-lock-vs-glacier-vault-lock": {"v1": "data residing in your AWS Backup backup vault"},
 "backup-faq-vmware-cold-storage-90-days": {"v2": "pro-rated charge equal to the storage charge"},
 "backup-faq-vmware-copy-to-other-region": {"v1": "a different AWS Region from your production backups"},
 "backup-faq-what-is-backup": {"v1": "centralizes and automates data protection"},
 "backup-feature-row-dynamodb-advanced": {"cells": None},
 "backup-feature-row-ebs": {"cells": None},
 "backup-feature-row-efs": {"cells": None},
 "backup-feature-row-fsx-ontap": {"cells": None},
 "backup-feature-support-not-assumed-unless-stated": {"v1": "should not be assumed"},
 "backup-fsx-backups-kept-after-source-deleted": {"v1": "even after the source file system is deleted"},
 "backup-full-management-central-billing-and-cost-allocation-tags": {"v2": "appear under \"Backup\""},
 "backup-iam-default-service-role-console-auto-cli-manual": {"v1": "created when you use the AWS Management Console"},
 "backup-iam-narrow-roles-and-who-can-pass-them": {"v2": "who can pass that role to AWS Backup"},
 "backup-iam-service-role-must-trust-aws-backup": {"v1": "AWS Backup listed as a trusted entity", "v2": "Different permissions are required"},
 "backup-incremental-requires-earlier-backup-in-vault-or-region": {"v1": "only be incremental if the vault"},
 "backup-incremental-restore-full-even-after-first-backup-expired": {"v1": "reference data to allow a full restore", "v2": "reached the end of its lifecycle"},
 "backup-lag-primary-backup-fully-managed-direct-no-vault-copy": {"v1": "can back up directly"},
 "backup-lag-vault-key-chosen-at-creation-only": {"v1": "an AWS KMS encryption key during vault creation"},
 "backup-lag-vault-lag-to-lag-copy-on-demand-only": {"v1": "cannot be scheduled in a backup plan"},
 "backup-lag-vault-restore-access-vault-view-delete": {"v1": "a view of an underlying logically air-gapped vault", "v2": "does not block this deletion"},
 "backup-lag-vault-secondary-vault-use-case-features": {"v1": "part of a data protection strategy", "v2": "a vault lock in compliance mode"},
 "backup-lag-vault-share-with-account-ids-only": {"v1": "only individual account IDs are supported"},
 "backup-lag-vault-shared-account-view-restore-not-copy": {"v1": "but not to create a copy"},
 "backup-lag-vault-source-key-fully-managed-cmk-or-aws-managed": {"v1": "by an AWS managed key"},
 "backup-lag-vault-source-key-not-fully-managed-needs-cmk": {"v1": "must be encrypted with a customer managed key", "v2": "not fully managed resources are not supported"},
 "backup-lag-vault-standard-vault-is-primary-type": {"v2": "stored within a standard backup vault"},
 "backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported": {"v1": "Unencrypted Amazon Aurora"},
 "backup-lag-vs-standard-restore-row": {"v1": "the same account to which the vault belongs"},
 "backup-lag-vs-standard-security-row": {"v1": "always locked with a vault lock", "v2": "in compliance or governance mode"},
 "backup-legal-hold-multiple-holds-backup-kept-until-all-removed": {"v1": "cannot be deleted as long as it has", "v2": "all legal holds on a backup are removed"},
 "backup-legal-hold-no-expiry-released-by-user-complements-vault-lock": {"v1": "does not expire"},
 "backup-legal-hold-only-original-backup-not-copies": {"v1": "apply only to the original backup", "v2": "does not retain or carry its legal hold"},
 "backup-malware-billed-by-guardduty-not-backup": {"v2": "will not see any AWS Backup charges"},
 "backup-malware-incremental-vs-full-scans": {"v1": "only the data that changed", "v2": "examine the entire recovery point"},
 "backup-malware-on-demand-scan-find-last-clean-backup": {"v1": "identify your last clean backup", "v2": "use a full scan"},
 "backup-malware-scan-resource-types-selected-per-plan": {"v2": "applies only to your selected resource types"},
 "backup-malware-scanning-by-guardduty-automate-or-on-demand": {"v1": "provided by Amazon GuardDuty Malware Protection"},
 "backup-metering-copy-charged-once-recovery-point-created": {"rule": "charged once a recovery point has been created"},
 "backup-metering-copy-data-transfer-account-by-management": {"managed": "source account will see the data transfer charges", "other": "destination account will see the data transfer charges"},
 "backup-monitoring-cloudwatch-eventbridge-cloudtrail-sns": {"v1": "track metrics and create alarms"},
 "backup-on-demand-backup-starts-immediately": {"v2": "other than the scheduled time"},
 "backup-org-member-accounts-need-vault-and-iam-role": {"v2": "the IAM role that will be used"},
 "backup-org-policy-merge-only-same-plan-name": {"v1": "share the same backup plan name"},
 "backup-plan-update-does-not-change-existing-recovery-points": {"v2": "does not affect the recovery point"},
 "backup-pricing-cold-early-deletion-prorated-90-days": {"charge": "pro-rated charge equal to the storage charge"},
 "backup-pricing-cost-allocation-tags-cost-explorer": {"v1": "track and optimize AWS Backup costs"},
 "backup-pricing-cross-region-transfer-out-only": {"rule": "when transferring data out of an AWS Region", "same": "no charges for transfers"},
 "backup-pricing-eks-per-namespace-creation-fee": {"fee": "one time backup creation fee"},
 "backup-pricing-gb-day-resource-types": {"unit": "billed on a GB-day basis"},
 "backup-pricing-overview-dimensions": {"dims": "backup storage you use", "fee": "no minimum fee"},
 "backup-pricing-restore-billed-gb-restored": {"basis": "sum of the data across all the restores"},
 "backup-pricing-restore-testing-evaluation-per-recovery-point": {"rule": "orchestrate for restore through a restore testing plan"},
 "backup-rds-custom-oracle-outposts-local-zones-unsupported": {"v1": "RDS Custom for Oracle is not currently supported"},
 "backup-rds-only-first-snapshot-full-later-incremental": {"v1": "Only the first snapshot ever taken"},
 "backup-rds-snapshots-share-free-backup-storage-allocation": {"v1": "free backup storage allocation"},
 "backup-restore-aurora-cluster-only-no-instance": {"v1": "does not create or attach"},
 "backup-restore-ddb-cross-account-same-key-must-be-shared": {"v1": "you must share the key"},
 "backup-restore-efs-single-weekly-backup-only-that-state": {"v1": "only restore to the state"},
 "backup-restore-no-sla-for-restore-time": {"v1": "does not provide any service-level agreements (SLAs)"},
 "backup-restore-testing-best-practice-designated-account": {"v1": "designate an account to be used"},
 "backup-restore-testing-resources-deleted-after-validation": {"v1": "deletes the resources involved with the restore test"},
 "backup-restore-testing-same-restore-jobs-as-on-demand": {"v1": "in the same way as on-demand restores"},
 "backup-restore-testing-tag-removed-needs-manual-delete": {"v2": "AWS Backup cannot delete the resource"},
 "backup-restore-testing-vs-restore-audit-manager-row": {"v1": "a restore test meets specified restore objectives"},
 "backup-restore-testing-vs-restore-resources-row": {"v1": "you can assign to your testing plan"},
 "backup-s3-backup-types-object-data-tags-acls-metadata": {"v1": "object data, tags, Access Control Lists (ACLs)"},
 "backup-s3-copies-available-copies-of-continuous-no-pitr": {"v1": "do not have point-in-time restore capabilities"},
 "backup-s3-eventbridge-disabled-failure-is-silent": {"v2": "no notification, alert, or backup job failure"},
 "backup-s3-no-sse-c-no-bucket-config-no-outposts": {"v1": "not offer support for backups of SSE-C-encrypted objects"},
 "backup-s3-restore-to-standard-all-or-specific-objects-existing-or-new-bucket": {"v1": "all the objects in a bucket"},
 "backup-s3-single-backup-policy-central-encrypted-vault": {"v1": "a single backup policy in AWS Backup"},
 "backup-sap-hana-on-ec2-via-backint": {"v1": "AWS Backint to support SAP HANA database"},
 "backup-search-charges-index-search-storage-restore": {"v1": "each search job incurs a charge"},
 "backup-search-find-files-or-objects-without-full-restore": {"v1": "search the metadata of your backups", "v2": "just the specific file or object"},
 "backup-search-index-created-by-plan-opt-in": {"v1": "created with each periodic backup"},
 "backup-search-needs-index-standard-vault-only": {"v1": "must first have a corresponding index"},
 "backup-tiering-applies-to-existing-and-new-backups": {"v1": "both existing backup data in vaults"},
 "backup-user-notifications-view-job-progress-and-changes": {"v1": "your backup, copy, and restore jobs"},
 "backup-vault-container-and-key-for-some-backups": {"v2": "managed by their source AWS services"},
 "backup-vault-key-applies-only-to-independent-encryption-types": {"v2": "used to encrypt the source resource"},
 "backup-vault-lock-account-closure-deletes-vault-after-90-days": {"v2": "AWS Backup Vault Lock was in place"},
 "backup-vault-lock-compliance-config-fixed-while-recovery-points": {"v1": "cannot be altered or deleted by a customer"},
 "backup-vault-lock-compliance-grace-time-remove-or-change": {"v1": "you can still remove the vault lock"},
 "backup-vault-lock-compliance-immutable-by-anyone": {"v1": "cannot be altered or deleted by any user"},
 "backup-vault-lock-enforced-even-during-grace-time": {"v2": "still in the cooling-off grace time period"},
 "backup-vault-lock-governance-lock-removable-with-iam": {"v2": "who have the appropriate IAM permissions"},
 "backup-vault-lock-min-max-retention-fail-nonconforming-jobs": {"v2": "recovery points that are already in the vault"},
 "backup-vault-lock-not-glacier-vault-lock": {"v1": "not the same feature as Amazon Glacier"},
 "backup-vault-required-before-plan-or-job": {"v2": "before creating a backup plan"},
 "backup-vmware-vms-on-premises-and-vmc": {"v2": "to either on premises or VMC"},
}

# light changes: exam relevance and tier0 of the facts kept from duplicate pairs
LIGHT = {
 "backup-tiering-s3-lower-cost-tier-up-to-30-percent": {"exam_relevance": "core", "tier0": True},
 "backup-cold-storage-transition-setting-cannot-change": {"exam_relevance": "core"},
 "backup-cold-storage-incremental-warm-full-8-days": {"exam_relevance": "core"},
 "backup-restore-destructive-exceptions-listed": {"tier0": True},
 "backup-legal-hold-max-50-active-per-account": {"exam_relevance": "extended"},
 "backup-copy-one-job-at-a-time-per-resource": {"exam_relevance": "core"},
}

# hard true on capability facts (consistent with the guide-lens capability facts)
HARD = ["backup-dashboard-audits-backup-and-restore-activity", "backup-faq-audit-manager-config-integration",
        "backup-faq-audit-manager-report-types", "backup-faq-cloudtrail-activity-logs", "backup-faq-dashboards-job-tracking",
        "backup-faq-key-features-advanced", "backup-faq-key-features-centralized", "backup-faq-restore-testing-plan",
        "backup-faq-s3-existing-plan-tags-or-arns", "backup-faq-s3-what-is-backed-up", "backup-faq-sns-alerting",
        "backup-faq-vault-resource-based-policy", "backup-organizations-cross-account-monitoring-management",
        "backup-tag-integration-group-resources"]

problems = []
written = []
ids = sorted(set(D) | set(LIGHT) | set(HARD))
for fid in ids:
    f = facts.get(fid)
    if f is None or f["status"] in ("rejected", "superseded"):
        problems.append("missing or retired: " + fid)
        continue
    patch = {}
    if fid in D:
        vals = []
        for v in f["values"]:
            k = v["key"]
            if k in D[fid]:
                nd = D[fid][k]
                if nd is None:
                    continue
                vals.append({**v, "display": nd})
            else:
                vals.append(dict(v))
        for k in D[fid]:
            if k not in {v["key"] for v in f["values"]}:
                problems.append("%s: unknown key %s" % (fid, k))
        quotes = [norm(e["quote"]) for e in f["evidence"]]
        for v in vals:
            d = v["display"]
            if not re.search(r"\d", d) and len(d.split()) > 8:
                problems.append("%s: still long: %s" % (fid, d))
            if not any(norm(d) in q for q in quotes):
                problems.append("%s: not in a quote: %s" % (fid, d))
        disp = [v["display"] for v in vals]
        if len(set(disp)) != len(disp):
            problems.append("%s: duplicate displays" % fid)
        if not vals:
            problems.append("%s: no values left" % fid)
        patch["values"] = vals
    if fid in LIGHT:
        patch.update(LIGHT[fid])
    if fid in HARD:
        if f.get("hard"):
            problems.append("%s: already hard" % fid)
        if not f.get("question"):
            problems.append("%s: no question" % fid)
        patch["hard"] = True
    json.dump(patch, open(OUT + "/" + fid + ".json", "w"), indent=1, ensure_ascii=False)
    written.append(fid)

open(OUT + "/_list.txt", "w").write("\n".join(written) + "\n")
print("patches", len(written))
for p in problems:
    print("PROBLEM", p)
