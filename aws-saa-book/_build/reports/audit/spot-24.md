# spot-24: Opus spot check of chapter 24 (AWS Backup) entail votes

Date: 2026-10-14. Checker: spot-24 (Opus). Stage context: verify-facts running (attempt 1), after the first entail round, before adjudication.

## Sample

Pool: 536 facts with home_chapter 24 and status mech-pass in `data/facts/backup.jsonl`. Ids sorted, `random.Random(20261013 + 24).sample(pool, 30)`. Ids in `spot-24.sample.json`.

Each fact was judged from its claim, values, qualifiers, quotes, packet context and headings (`facts show`, the `24-entail-*` packets) and, where the context mattered, `show <source>`, under the strict rule of TOOLS.md 5.4, the entail packet instruction ("with the same scope and qualifiers") and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 26. Not positive (partial): 4.
- The first-round voters had already marked 3 of the 4 partial.
- Voter misses (voter support, spot-24 partial): 1 of 30 (`backup-ddb-advanced-default-for-new-customers`). Under three: **no flag** for chapter 24.
- One sampled fact had no first-round entail vote: `backup-quota-audit-manager-report-plans-per-account` (rev 1, votes empty). spot-24 judged it support; the adjudicator should make sure it gets its entail vote.

## Non-positive verdicts

| Fact | First-round vote | spot-24 | Reason |
|---|---|---|---|
| backup-ddb-advanced-default-for-new-customers | support | partial | The qualifier condition "existing customers are recommended to enable them" stands only in the next paragraph, not in the quote. |
| backup-feature-row-aurora | partial | partial | The incremental-backup check carries footnote 6 ("Snapshots are full and incremental backup is offered through PITR") and the copy checks carry footnote 3; both stood only outside the quote. |
| backup-pitr-retention-change-1-to-35-days-via-plan | partial | partial | The qualifier condition (change takes effect when the next backup completes) stands only in the sentence after the quote. |
| backup-s3-recommend-lifecycle-expiration-for-versions | partial | partial | The claim's causal "because" link between the recommendation and the stored versions and cost is not stated in any quote; the claim also dropped "when the backup begins". |

## Amended (each once, `--by spot-24`, all mech-pass after; no dependents)

Patch files: `_build/work/24-backup/spot-24/<id>.json`. Every quote is verbatim from a saved AWS page (same pages as before).

1. **backup-ddb-advanced-default-for-new-customers** (now rev 2): added the verbatim "We recommend all existing AWS Backup customers enable advanced features for DynamoDB." from `working-with-supported-services` as a second evidence item; claim now also says AWS recommends that existing customers enable the advanced features.
2. **backup-feature-row-aurora** (now rev 3): added footnote lines "6 Snapshots are full and incremental backup is offered through PITR." and "3 Amazon RDS, Aurora, DocumentDB, and Neptune now support cross-Region and cross-account snapshot copying in a single action." from `backup-feature-availability` as evidence; the claim names both footnotes.
3. **backup-pitr-retention-change-1-to-35-days-via-plan** (now rev 2): quote extended by the next sentence ("The change in retention period will take effect when the next backup is completed following this change."); claim now states it.
4. **backup-s3-recommend-lifecycle-expiration-for-versions** (now rev 2): claim narrowed to the three stated sentences without the causal link, with the scope "in the bucket when the backup begins"; evidence unchanged.

No batch was cut and nothing was finalized. The adjudicator sends these four to a fresh independent vote. No fact judged positive was touched.

## Positive (26)

backup-vault-lock-compliance-grace-time-remove-or-change, backup-cross-account-monitor-all-accounts-in-one-place, backup-quota-eks-namespaces-per-cluster-backup, backup-cold-storage-ignored-for-unsupported-resources, backup-s3-single-backup-policy-central-encrypted-vault, backup-encryption-failed-jobs-from-deny-or-revoked-grant, backup-quota-eks-restore-jobs-per-target-cluster, backup-fsx-backups-kept-after-source-deleted, backup-continuous-rds-pitr-via-aws-backup-or-rds, backup-vault-access-policy-allow-create-limit-delete, backup-change-legal-hold-2022-11, backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported, backup-lag-primary-backup-ebs-ec2-aurora-fsx-temp-recovery-point, backup-quota-tags-in-resource-selection, backup-copy-iam-role-trusted-entity-default-created, backup-faq-audit-manager-control-framework, backup-continuous-cannot-be-scheduled, backup-overview-whitepaper-centralize-automate-policy-based, backup-delegated-admin-privileges-register-deregister-row, backup-quota-audit-manager-report-plans-per-account (no first-round vote), backup-central-management-needs-opt-in-plan-and-vault, backup-tiering-three-cost-components-one-time-transition-fee, backup-encryption-ebs-row, backup-vault-lock-min-max-retention-fail-nonconforming-jobs, backup-plan-composed-of-one-or-more-backup-rules, backup-faq-vault-encrypted-per-region.

## Observations for the adjudicator (not entail verdicts)

- `backup-tiering-three-cost-components-one-time-transition-fee`: support. Its scope "S3 backup tiering" is a narrowing of the quote's subject; the page overview confirms tiering is for S3 backups.
- `backup-continuous-cannot-be-scheduled`: support. The next paragraph on that page has the maintenance-window rule for snapshot backups (with Aurora exempt); that belongs in a separate fact.
- Pattern in this chapter: qualifier `condition` fields filled from the next sentence or paragraph. The voters caught one (PITR retention) and missed one (DynamoDB advanced features). Other facts with a non-empty `condition` are worth a second look.
