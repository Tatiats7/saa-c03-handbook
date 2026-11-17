---
chapter: "24"
file: deep
title: AWS Backup in depth
status: draft
updated: 2026-10-22
---

# AWS Backup in depth

## How it works (28 min)
<!-- section: role=how; route=full; minutes=28 -->

### A backup plan turns the RPO and the retention into scheduled rules (4 min)
<!-- section: route=pass -->

A company wants daily backups and monthly backups that stay for years, in several accounts.

1. **Set the objective.** The **recovery point objective** ([RPO](../facts/well-architected.md#well-architected-rpo-definition)) is the data loss, in time, that you accept. The **recovery time objective** ([RTO](../facts/well-architected.md#well-architected-rto-definition)) is how long the service can stay down.
2. **Write the rules.** A **backup plan** is [comprised of one or more backup rules](../facts/backup.md#backup-faq-backup-rule-four-parts). Each **backup rule** sets a schedule, a **backup window**, a lifecycle and a backup vault.
3. **Select resources.** In a **resource assignment**, you [apply backup plans to your AWS resources](../facts/backup.md#backup-plan-applied-by-tagging-resources) by their tags.
4. **Pass a role.** For each resource assignment, [you must pass a service role](../facts/backup.md#backup-iam-role-passed-for-plans-on-demand-copy-restore).

Why rules, not scripts? A rule states what you want, and AWS Backup [automates the creation of backups](../facts/backup.md#backup-faq-assigned-resources-encrypted-vault).

> **Exam signal:** "one backup policy for all accounts in the organization" points to a **backup policy** in AWS Organizations. Backup policies [centrally manage and apply backup plans](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable).

<details>
<summary>Go deeper: running backup for an organization</summary>

A **delegated administrator** manages AWS Backup from [outside the management account](../facts/backup.md#backup-delegated-admin-performs-most-admin-tasks-from-member-account).

</details>

> **Say it:** The short answer is: one backup plan turns the RPO into rules. The thing to watch is the role.

**Stop and answer.** A team adds the tag of its DynamoDB tables to a correct backup plan. No DynamoDB backups appear. What is missing?

<details>
<summary>Answer</summary>

The **service opt-in** for DynamoDB. With tags, the [service opt-in settings will still apply](../facts/backup.md#backup-opt-in-still-applies-with-tag-assignment).

</details>

### Each backup becomes a recovery point in an encrypted backup vault (4 min)

Where does a finished backup live, and which key protects it?

1. **Store.** A **recovery point** [represents the content of a resource](../facts/backup.md#backup-recovery-point-is-backup-at-specified-time) at one moment. AWS Backup [saves recovery points in backup vaults](../facts/backup.md#backup-recovery-points-saved-in-vaults): a **backup vault** is an [encrypted storage location in your AWS account](../facts/backup.md#backup-faq-vault-encrypted-per-region).
2. **Store less.** The first backup is full. Each later **incremental backup** stores [only the changes to your AWS resources](../facts/backup.md#backup-incremental-first-full-then-changes).
3. **Encrypt.** The AWS Key Management Service (AWS KMS) key of a backup vault [applies to the backups of certain resource types](../facts/backup.md#backup-vault-key-applies-only-to-independent-encryption-types). These types have **independent encryption**.

<!-- table: plain -->
| Resource | Backup encrypted with |
|---|---|
| Amazon S3 | The vault key, [even if the source Amazon S3 buckets are not encrypted](../facts/backup.md#backup-encryption-s3-row) |
| Amazon EBS | The key [used to encrypt the source volume](../facts/backup.md#backup-encryption-ebs-row), or none |
| Amazon RDS | The key used to [encrypt the source Amazon RDS database](../facts/backup.md#backup-encryption-rds-row), or none |

Why two kinds? Types with **full AWS Backup management** get their own Amazon Resource Names (ARNs): [Backup ARNs begin with](../facts/backup.md#backup-full-management-backup-arns-for-backup-specific-policies) arn:aws:backup.

> **Exam signal:** "back up all EBS volumes of an instance at the same moment" points to AWS Backup, which takes [crash-consistent, multi-volume snapshots](../facts/ebs.md#ebs-aws-backup-multi-volume-crash-consistent).

> **Say it:** The short answer is: each backup is a recovery point in a backup vault. The thing to watch is the key.

**Stop and answer.** The role of AWS Backup has no access to the KMS key of an S3 bucket. The job reports success. Is the data backed up?

<details>
<summary>Answer</summary>

No. The [objects are not backed up or restored](../facts/backup.md#backup-encryption-role-needs-kms-access-else-silent-skip).

</details>

### Continuous backups allow point-in-time restore but keep at most 35 days (4 min)
<!-- section: route=pass -->

A bad deployment corrupts a database at 10:20, after the midnight backup.

1. **Turn it on.** A rule can make a **continuous backup** instead of a **snapshot backup**, also called periodic. [Continuous backups allow you to perform point-in-time restore](../facts/backup.md#backup-continuous-rule-allows-pitr-unlike-snapshot).
2. **Record.** AWS Backup takes a full backup, then keeps [constantly backing up your resource's transaction logs](../facts/backup.md#backup-pitr-continuous-works-by-full-backup-and-transaction-logs).
3. **Rewind.** A **point-in-time restore** goes [within 1 second of precision](../facts/backup.md#backup-pitr-restore-rewinds-to-chosen-time) to your chosen time, back [a maximum of 35 days](../facts/backup.md#backup-pitr-restore-rewinds-to-chosen-time).

<!-- table: plain -->
| Question | Snapshot backup | Continuous backup |
|---|---|---|
| How often | [As frequently as every hour](../facts/backup.md#backup-snapshot-hourly-and-100-years) | Every change |
| How long kept | Up to [100 years](../facts/backup.md#backup-retention-snapshot-range) | [1 day to 35 days](../facts/backup.md#backup-retention-continuous-range) |

Why does AWS recommend [both continuous and snapshot backup rules](../facts/backup.md#backup-pitr-recommend-continuous-and-snapshot-rules-together)? One rule gives the second of a recent mistake; the other keeps years.

> **Exam signal:** "undo accidental deletions in an S3 bucket" points to continuous backups, which help with [undoing accidental deletions](../facts/backup.md#backup-faq-s3-continuous-vs-periodic-use).

> **Exam trap:** A copy of a continuous backup in another Region loses point-in-time restore. The copy [becomes a snapshot (periodic) backup](../facts/backup.md#backup-continuous-copy-becomes-snapshot-no-pitr). <!-- trap: backup-trap-copy-keeps-pitr -->

<details>
<summary>Go deeper: one continuous backup per resource</summary>

A resource [can only have one continuous backup](../facts/backup.md#backup-continuous-one-per-resource-redundant-extra), and continuous backups [cannot be scheduled](../facts/backup.md#backup-continuous-cannot-be-scheduled) with a cron expression.

</details>

> **Say it:** The short answer is: continuous backups rewind to a second, and snapshots keep years. The thing to watch is copies.

**Stop and answer.** A team wants a DynamoDB table back at the second before a bad write. Does AWS Backup do it?

<details>
<summary>Answer</summary>

No. Its DynamoDB backups are periodic and [do not replace or duplicate native DynamoDB point-in-time](../facts/backup.md#backup-ddb-advanced-does-not-replace-native-pitr) recovery. Turn on DynamoDB point-in-time recovery.

</details>

### The lifecycle moves some backups to cold storage and later deletes them (4 min)

Monthly backups stay for years and are rarely restored.

1. **Start warm.** **Warm storage** comes first: every backup is [stored in warm storage](../facts/backup.md#backup-every-backup-starts-in-warm-storage). The **backup lifecycle** can later move it to **cold storage**.
2. **Check the type.** For types without cold storage, the setting is [ignored for other resources](../facts/backup.md#backup-cold-storage-ignored-for-unsupported-resources).
3. **Stay long enough.** A backup stays in cold storage for a [minimum of 90 days](../facts/backup.md#backup-cold-storage-min-90-days-retention-rule).
4. **Expire.** AWS Backup deletes an expired backup [over the following 8 hours](../facts/backup.md#backup-plan-expired-backups-deleted-within-8-hours).

<!-- table: plain -->
| Resource | Cold storage |
|---|---|
| Amazon EBS | Yes, when backups run [monthly or less often](../facts/backup.md#backup-cold-ebs-is-snapshot-archive-monthly-or-less) |
| Amazon DynamoDB | Only [DynamoDB with advanced features](../facts/backup.md#backup-cold-storage-resource-types) |
| Amazon S3 | No: [cold storage transition of S3 backups is not supported](../facts/backup.md#backup-s3-no-cold-storage-transition) |

Why monthly for EBS? An archived EBS snapshot is [converted to a full snapshot](../facts/ebs.md#ebs-archive-full-snapshot).

> **Exam signal:** "keep backups for years at the lowest cost" points to a lifecycle rule to a [lower-cost tier called cold storage](../facts/backup.md#backup-every-backup-starts-in-warm-storage).

> **Exam trap:** Continuous backups never move to cold storage: they keep a [maximum retention period of 35 days](../facts/backup.md#backup-pitr-no-cold-storage-because-35-vs-90). <!-- trap: backup-trap-every-backup-goes-cold -->

> **Say it:** The short answer is: move old backups to cold storage where allowed. The thing to watch is the minimum stay.

**Stop and answer.** A rule keeps monthly EBS backups for 30 days and moves them to cold storage after 7 days. Will AWS Backup accept the rule?

<details>
<summary>Answer</summary>

No. Cold storage needs a total retention period of [90 days or greater](../facts/backup.md#backup-cold-storage-plan-total-retention-90-days).

</details>

### A copy in another Region or account survives the loss of the source (4 min)
<!-- section: route=pass -->

Backups in one account and one Region can all be lost together.

1. **Add a copy action.** A **copy action** copies each backup [in the same or another AWS Region](../facts/backup.md#backup-copy-action-same-or-other-region-and-account), [in the same account or another account](../facts/backup.md#backup-copy-action-same-or-other-region-and-account).
2. **Copy to a Region.** A **cross-Region copy** uses [the KMS key of the target vault](../facts/backup.md#backup-encryption-copy-uses-destination-vault-key).
3. **Copy to an account.** For a **cross-account copy**, the accounts [must belong to the same organization](../facts/backup.md#backup-cross-account-requires-same-organization). The destination backup vault allows [the access policy backup:CopyIntoBackupVault](../facts/backup.md#backup-cross-account-destination-vault-must-allow-copy-into).
4. **Recover.** You copy a deleted backup back [from its destination account to its source account](../facts/backup.md#backup-cross-account-copy-purpose-recover-deleted-original), then restore it.

<!-- table: plain -->
| Copy | Protects against |
|---|---|
| Another Region | The loss of a Region |
| Another account | Deletes with stolen production credentials |

Why a second account? Production credentials can only copy into it: cross-account requests [other than backup:CopyIntoBackupVault will be rejected](../facts/backup.md#backup-vault-policy-cross-account-only-copy-into-vault).

> **Exam signal:** "ransomware" points to a **logically air-gapped vault**, part of a [ransomware resilience strategy](../facts/backup.md#backup-faq-lag-vault-ransomware-strategy).

> **Exam trap:** A copy action does not reach every AWS account. For another company, share a logically air-gapped vault [with accounts in different Organizations](../facts/backup.md#backup-faq-lag-vault-share-ram). <!-- trap: backup-trap-cross-account-any-account -->

> **Say it:** The short answer is: copy backups to a second account and Region. The thing to watch is the vault policy.

**Stop and answer.** Last year's monthly backups are in cold storage. Can a new rule copy them to another Region?

<details>
<summary>Answer</summary>

No. Backups in cold storage or [archive tiers cannot be copied](../facts/backup.md#backup-copy-cold-storage-backups-cannot-be-copied).

</details>

### Vault Lock in compliance mode stops even the root user from deleting backups (4 min)
<!-- section: route=pass -->

An attacker with administrator credentials holds every IAM permission.

1. **Choose a mode.** AWS Backup **Vault Lock** has **governance mode** and **compliance mode**.
2. **Set retention limits.** New jobs [will fail if they do not conform](../facts/backup.md#backup-vault-lock-min-max-retention-fail-nonconforming-jobs) to the lock's minimum and maximum retention.
3. **Wait before it locks.** A compliance lock has a **grace time** of [at least 3 days (72 hours)](../facts/backup.md#backup-vault-lock-grace-time-minimum-3-days).
4. **Deny deletes.** Any user, [including the root user](../facts/backup.md#backup-vault-lock-denies-delete-and-lifecycle-change-even-root), fails to delete a locked backup.

<!-- table: plain -->
| Question | Governance mode | Compliance mode |
|---|---|---|
| Who can remove the lock | It can have its [lock removed by users with sufficient IAM permissions](../facts/backup.md#backup-vault-lock-governance-lock-removable-with-iam) | It [cannot be altered or deleted by any user](../facts/backup.md#backup-vault-lock-compliance-immutable-by-anyone) |

Why a grace time? During it, [you can still remove the vault lock](../facts/backup.md#backup-vault-lock-compliance-grace-time-remove-or-change) and fix a mistake.

> **Exam signal:** "keep one backup past its retention" points to a **legal hold**, which [does not expire](../facts/backup.md#backup-legal-hold-no-expiry-released-by-user-complements-vault-lock).

**Spot the bug.** A vault access policy denies backup:DeleteRecoveryPoint to all but the security role. An engineer still deletes an RDS snapshot in it. What is wrong?

<details>
<summary>Answer</summary>

Vault access policies [only control user access to AWS Backup APIs](../facts/backup.md#backup-vault-access-policy-controls-only-backup-apis). The engineer used the Amazon RDS API.

</details>

> **Try it:** Lock a backup vault in governance mode, then unlock it. See [3-do.md](3-do.md). <!-- task: backup-t02 -->

> **Say it:** The short answer is: lock the vault in compliance mode. The thing to watch is the grace time.

**Stop and answer.** A company locks a vault in compliance mode, then closes its account. Are the backups kept?

<details>
<summary>Answer</summary>

No. AWS and AWS Backup [suspend your account for 90 days](../facts/backup.md#backup-vault-lock-account-closure-deletes-vault-after-90-days), then AWS deletes the vault contents.

</details>

### Most restores create a new resource and restore testing proves they work (4 min)

An auditor asks for proof that backups restore, and how long a restore takes.

1. **Restore.** For most resource types, AWS Backup [creates a new resource during restore](../facts/backup.md#backup-restore-destructive-exceptions-listed).
2. **Test on a schedule.** **Restore testing** gives [automated and periodic evaluation of restore viability](../facts/backup.md#backup-restore-testing-automated-periodic-evaluation), then [deletes the resources involved with the restore test](../facts/backup.md#backup-restore-testing-resources-deleted-after-validation).
3. **Prove it.** **AWS Backup Audit Manager** audits [the compliance of your data protection policies](../facts/backup.md#backup-faq-audit-manager-purpose). A **framework** holds controls, such as [Restore time for resources meet target](../facts/backup.md#backup-audit-manager-control-restore-time).

Why test? AWS Backup [does not provide any service-level agreements (SLAs)](../facts/backup.md#backup-restore-no-sla-for-restore-time) for restore time.

> **Exam signal:** "prove to auditors that backups follow the policy" points to AWS Backup Audit Manager. "Check every month that backups restore" points to restore testing.

> **Exam trap:** A restore rarely overwrites data: only [Amazon Redshift Serverless](../facts/backup.md#backup-restore-destructive-exceptions-listed) and [SAP HANA on Amazon EC2](../facts/backup.md#backup-restore-destructive-exceptions-listed) restores overwrite. <!-- trap: backup-trap-restore-overwrites -->

> **Say it:** The short answer is: restores create new resources, and tests prove them. The thing to watch is restore time.

**Stop and answer.** A team restores an Amazon EFS backup into the existing file system. Users still see the broken files. Did the restore fail?

<details>
<summary>Answer</summary>

No. The files are [located in a recovery subdirectory under the root](../facts/backup.md#backup-restore-efs-files-not-in-original-locations).

</details>

## Numbers that decide answers (2 min)
<!-- section: role=numbers; route=full; minutes=2 -->

### A-list

<!-- table: numbers -->
| Number | What it is | Why it decides an answer |
|---|---|---|
| [as frequently as every hour](../facts/backup.md#backup-snapshot-hourly-and-100-years) | Most frequent snapshot backup | A shorter RPO needs a continuous backup |
| [1 day to 35 days](../facts/backup.md#backup-retention-continuous-range) | Retention of a continuous backup | Older points need snapshot backups |
| [most recent 5 minutes of activity](../facts/backup.md#backup-pitr-latest-restorable-time-by-service) | Latest RDS point-in-time restore | For S3: [most recent 15 minutes of activity](../facts/backup.md#backup-pitr-latest-restorable-time-by-service) |
| [minimum of 90 days](../facts/backup.md#backup-cold-storage-min-90-days-retention-rule) | Time a backup stays in cold storage | A short retention stays warm |
| [at least 3 days (72 hours)](../facts/backup.md#backup-vault-lock-grace-time-minimum-3-days) | Shortest grace time of a compliance lock | After it ends, the lock is fixed |

### B-list

<!-- table: numbers -->
| Number | What it is |
|---|---|
| [typically takes 4 hours more](../facts/backup.md#backup-restore-from-cold-storage-takes-longer) | Extra time of a restore from cold storage |
| [99.999999999% (11 nines)](../facts/backup.md#backup-resilience-stored-across-azs-eleven-nines) | Designed durability of stored backups |

## Decision record (2 min)
<!-- section: role=example; route=full; minutes=2 -->

**Context.** The bank asks for every backup policy and a restore test. Callvale's data sits in four services across several accounts.

![Before: in several accounts, an Aurora cluster, a DynamoDB table, an EFS file system and an EBS volume each have their own backup setting. No report covers all four.](../diagrams/svg/backup-before.svg)

**Figure.** Each data store keeps its own backup setting, so there is no common policy, lock or report.

**Requirement.** Keep daily backups for 30 days and monthly backups for 7 years, and no administrator can delete a backup. Which solution has the LEAST operational overhead?

**Options.**

- Each service's own backup settings.
- Custom snapshot programs.
- **AWS Backup plans for the whole organization.**

**Decision.** One backup policy, a tag-based plan in each account, a vault in compliance mode, and a copy to a backup account.

![After: an organization backup policy puts one backup plan in each account. The plan selects the four data stores by tag, writes to a locked backup vault and copies to a vault in a backup account.](../diagrams/svg/backup-after.svg)

**Figure.** One backup plan selects resources by tag in every account, writes to a locked vault and copies to a backup account.

**Trade-off.** A second policy layer, and locked seven-year copies that [cannot be deleted until their lifecycle completes](../facts/backup.md#backup-vault-lock-locked-backups-persist-until-lifecycle-ends).

## FAQ quick-fire (3 min)
<!-- section: role=faq; route=full; minutes=3 -->

**FAQ 1.** Do highly durable services still need backups?

<details>
<summary>Answer</summary>

Yes. [Even durable resources are susceptible to threats](../facts/backup.md#backup-faq-why-durable-still-needs-backup).

> "Even durable resources are susceptible to threats such as bugs in your application that can cause accidental deletions or corruption."
> — [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)

</details>

**FAQ 2.** Do Data Lifecycle Manager policies control AWS Backup plans?

<details>
<summary>Answer</summary>

No. They [work independently from each other](../facts/backup.md#backup-faq-dlm-and-backup-independent).

> "Amazon Data Lifecycle Manager policies and backup plans created in AWS Backup work independently from each other and provide two ways to manage EBS snapshots."
> — [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)

</details>

**FAQ 3.** Can S3 backups move to cold storage?

<details>
<summary>Answer</summary>

No. [Cold storage transition of S3 backups is not supported](../facts/backup.md#backup-s3-no-cold-storage-transition).

> "AWS Backup for S3 supports backup access policies and encryption of backups with a different key, but does not support cold storage tier."
> — [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)

</details>

**FAQ 4.** Can a backup be kept after its retention period ends?

<details>
<summary>Answer</summary>

Yes. A legal hold keeps it [even if their retention period is over](../facts/backup.md#backup-faq-legal-hold-definition).

> "These holds prevent backups from being deleted, even if their retention period is over, and remain in place until explicitly released."
> — [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)

</details>

**FAQ 5.** Can AWS Backup back up an S3 bucket without versioning?

<details>
<summary>Answer</summary>

No. [S3 Versioning is a prerequisite to creating backups](../facts/backup.md#backup-faq-s3-versioning-prerequisite).

> "Yes, turning on S3 Versioning is a prerequisite to creating backups of S3 buckets and objects."
> — [AWS Backup FAQs](https://aws.amazon.com/backup/faqs/)

</details>

## In the real world (1 min)
<!-- section: role=realworld; route=full; minutes=1 -->

**Games24x7, 2024.** In testing, the gaming company Games24x7 reached an RPO of [1 hour](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto) and an RTO of [30 minutes](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto) for a large database.

> "Games24x7 set up automated backups for this stored data using AWS Backup."
> — [Achieving 1-Hour RPO and 30-Minute RTO Using AWS Backup with Games24x7](https://aws.amazon.com/solutions/case-studies/games24x7-backup-case-study/)

**It shows:** a tested restore turns RPO and RTO targets into proof.

> **Say it:** Games24x7 automated its backups with AWS Backup. A restore test proved its recovery targets.
