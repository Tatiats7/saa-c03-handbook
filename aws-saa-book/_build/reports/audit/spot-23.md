# spot-23: Opus spot check of chapter 23 (EFS and FSx) entail votes

Date: 2026-10-13. Checker: spot-23 (Opus). Stage context: verify-facts running, after the first entail round, before adjudication.

## Sample

Pool: 877 facts with home_chapter 23 and status mech-pass in `data/facts/efs.jsonl` and `data/facts/fsx.jsonl`. Ids sorted, `random.Random(20261013 + 23).sample(pool, 30)`. Ids in `spot-23.sample.json`.

Each fact was judged with `facts show` and, where the context mattered, `show <source> --around`, under the strict rule of TOOLS.md 5.4 and RULINGS 2026-10-13 safeguard 1.

## Result

- Checked: 30. Positive (support): 24. Not positive (partial): 6.
- The first-round voters had already marked 2 of the 6 partial (`efs-faq-free-tier-5-gb-standard`, `efs-onezone-other-az-instance-pays-data-access-charges`).
- Voter misses (voter support, spot-23 partial): 4 of 30 (13%). This is three or more misses: **flag logged for chapter 23** under RULINGS 2026-10-13 safeguard 2. Two of the four (cross-account replication, default backup plan) are mild: one dropped condition plus an unstated "because", and one unsupported qualifier.

## Non-positive verdicts

| Fact | First-round vote | spot-23 | Reason |
|---|---|---|---|
| efs-faq-free-tier-5-gb-standard | partial | partial | The next sentence excludes EFS One Zone and the next paragraph says new AWS customers get Free Tier credits from July 15, 2025; the claim stated the 5 GB offer without either. |
| fsx-faq-ontap-single-az-cost-optimized | support | partial | "these use cases" (dev/test, secondary copies, no cross-AZ resiliency) resolves only in the preceding sentence. |
| efs-onezone-other-az-instance-pays-data-access-charges | partial | partial | The quote is a worked example (us-west-2c), not the general rule the claim states. |
| fsx-windows-automatic-storage-increase-solution-cloudformation | support | partial | The claim reads as a built-in setting; the mechanism (an AWS-developed custom CloudFormation template) stands only in the next sentence. |
| efs-cross-account-replication-destination-must-exist-first | support | partial | Claim dropped the quote's ordering condition ("before you can create the IAM role for the source account") and added a causal "because" that the quote does not state. |
| efs-default-backup-plan-daily-35-day-retention | support | partial | Qualifier `adjustable: true` is not carried by the quote (editability is stated on another page). |

## Amended (each once, `--by spot-23`, all now rev 2, mech-pass; no dependents)

Patch files: `_build/work/23-efs-fsx/spot-23/<id>.json`.

1. **efs-faq-free-tier-5-gb-standard**: claim now carries the One Zone exclusion and the July 15, 2025 credits sentence; two verbatim FAQ quotes added (same page); displays added. Note for the adjudicator: the fact now mentions a change, but `volatility` is still `stable`, so no currency vote is required. Consider setting it.
2. **fsx-faq-ontap-single-az-cost-optimized**: added the preceding FAQ sentence (same page); the claim names the use cases.
3. **efs-onezone-other-az-instance-pays-data-access-charges**: added the general sentence from `docs/efs/latest/ug/mounting-one-zone` ("You can avoid data transfer charges between Availability Zones ..."); the claim scopes the us-west-2c case as the AWS example.
4. **fsx-windows-automatic-storage-increase-solution-cloudformation**: added the next sentence (same page, verbatim with its U+2010 hyphen in "AWS‐developed"); the claim names the CloudFormation template.
5. **efs-cross-account-replication-destination-must-exist-first**: claim only; it now follows the quote (the IAM-role ordering is kept, "because" removed).
6. **efs-default-backup-plan-daily-35-day-retention**: added the verbatim sentence from `docs/efs/latest/ug/automatic-backups` ("You can edit the default backup plan settings using the AWS Backup console."); claim extended.

No batch was cut and nothing was finalized. The adjudicator sends these six to a fresh independent vote. No fact judged positive was touched.

## Positive (24)

efs-limit-hard-links-per-file, fsx-faq-ontap-s3-access-points-attach, fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days, efs-backup-plan-and-vault-cannot-be-deleted, efs-faq-control-instances-with-security-groups-and-iam, fsx-faq-lustre-backups-not-on-s3-linked, efs-mount-targets-only-one-vpc-at-a-time, fsx-ontap-limit-user-backup-retention, fsx-lustre-limit-backup-copies-in-progress, fsx-faq-openzfs-intelligent-tiering-moves-back-no-extra-fees, efs-change-access-points-10000-per-file-system-2025-02, efs-lifecycle-automatic-transition-between-classes, efs-faq-elastic-throughput-when, fsx-windows-ad-options-aws-managed-or-self-managed, fsx-windows-multi-az-enhanced-durability-availability-auto-failover, fsx-faq-ontap-scale-tens-gbps-millions-iops, fsx-faq-windows-always-encrypts-at-rest-kms, fsx-change-lustre-efa-gpudirect-2024-11, fsx-ontap-snaplock-compliance-no-delete-by-any-user, fsx-ontap-snaplock-worm-compliance-and-enterprise-modes, fsx-faq-windows-failover-triggers, fsx-faq-openzfs-backups-pit-consistent-incremental-rto, efs-faq-access-from-ecs-task-definition, efs-overview-thousands-of-instances-and-on-premises.

Minor observations (not verdict-changing): `fsx-lustre-limit-backup-copies-in-progress` sits under a table header "Limit per file system" while its row says "per account"; the claim follows the row. `fsx-faq-openzfs-intelligent-tiering-moves-back-no-extra-fees` has an id that says "no extra fees", but its claim does not.
