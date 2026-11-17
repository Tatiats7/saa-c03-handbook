import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
V, VL, PB, M = D + "create-a-vault", D + "vault-lock", D + "lag-vault-primary-backup", D + "multipartyapproval"
f = []
f.append(F("backup-plan-pointing-at-deleted-vault-fails", "behavior",
 "A backup plan that points to a deleted backup vault makes backup creation fail, so you update plans to point to new vaults when you delete a vault.",
 "What happens to a backup plan whose target vault is deleted?",
 ["points to a deleted backup vault", "cause the backup creation to fail"],
 [E(V, "When you delete a backup vault, update your backup plans to point to new backup vaults. A backup plan that points to a deleted backup vault will cause the backup creation to fail.")],
 scope="backup plans and vaults", rel="extended", bullets=["2.2.S5"]))
# Vault lock remaining
f.append(F("backup-vault-lock-mode-set-by-changeable-for-days", "behavior",
 "In the API, a vault lock is created in governance mode when you leave out ChangeableForDays; if you include that parameter, the lock is created in compliance mode.",
 "How does the Vault Lock API choose between governance mode and compliance mode?",
 ["do not include ChangeableForDays", "created in compliance mode"],
 [E(VL, "If you wish to create a vault lock in governance mode, do not include `ChangeableForDays`. If this parameter is included, the vault lock will be created in compliance mode.")],
 scope="PutBackupVaultLockConfiguration", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-min-max-retention-fail-nonconforming-jobs", "behavior",
 "With a vault lock minimum and maximum retention, new backup and copy jobs that do not conform fail, while recovery points already in the vault keep their previous lifecycle settings.",
 "What happens to jobs and existing recovery points when Vault Lock sets minimum and maximum retention?",
 ["will fail if they do not conform", "not apply to recovery points that are already in the vault"],
 [E(VL, "New backup and copy jobs created in the vault will fail if they do not conform to the retention periods you set; these periods will not apply to recovery points that are already in the vault. Recovery points that were present in the vault prior to the vault lock being enabled will follow their previous lifecycle settings.")],
 scope="Vault Lock min and max retention", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-retention-periods-optional-no-enforcement-if-unset", "default",
 "If you do not set a maximum (or minimum) retention period, Vault Lock does not enforce one.",
 "Does Vault Lock enforce a retention range if you do not set one?",
 ["will not enforce a maximum retention period", "will not enforce a minimum retention period"],
 [E(VL, "If not specified, AWS Backup Vault Lock will not enforce a maximum retention period. If specified, backup and copy jobs to this vault with lifecycle retention periods longer than the maximum retention period will fail."),
  E(VL, "If not specified, AWS Backup Vault Lock will not enforce a minimum retention period. If specified, backup and copy jobs to this vault with lifecycle retention periods shorter than the minimum retention period will fail.")],
 scope="Vault Lock min and max retention", dm="default", bullets=["1.3.S1"], rel="extended"))
f.append(F("backup-vault-lock-worm-and-extra-defense-benefits", "behavior",
 "Vault Lock gives a write-once, read-many (WORM) configuration for all backups in a vault and an additional layer of defense against inadvertent or malicious deletion.",
 "What does AWS Backup Vault Lock give you?",
 ["WORM (write-once, read-many) configuration", "inadvertent or malicious deletions"],
 [E(VL, "WORM (write-once, read-many) configuration for all the backups you store and create in a backup vault."),
  E(VL, "An additional layer of defense that protects backups (recovery points) in your backup vaults from inadvertent or malicious deletions.")],
 scope="AWS Backup Vault Lock", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-lock-enforces-retention-against-privileged-users", "behavior",
 "Vault Lock enforces backup lifecycle retention periods, which prevents early deletions by privileged users, including the AWS account root user.",
 "Does Vault Lock stop privileged users, including root, from deleting backups early?",
 ["prevent early deletions by privileged users", "AWS account root user"],
 [E(VL, "Enforcement of backup lifecycle retention periods, which prevent early deletions by privileged users (including the AWS account root user), and help meet your organization’s data protection policies and procedures.")],
 scope="AWS Backup Vault Lock", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-cohasset-assessment-sec-cftc-finra", "behavior",
 "AWS Backup Vault Lock has been assessed by Cohasset Associates for use in environments subject to SEC 17a-4, CFTC and FINRA regulations.",
 "Has Vault Lock been assessed for regulated financial environments such as SEC 17a-4?",
 ["assessed by Cohasset Associates", "SEC 17a-4, CFTC, and FINRA regulations"],
 [E(VL, "AWS Backup Vault Lock has been assessed by Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and FINRA regulations.")],
 scope="AWS Backup Vault Lock", bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-no-extra-charge-storage-charges-apply", "pricing-dimension",
 "AWS Backup Vault Lock is available at no additional charge, and standard AWS Backup storage charges apply to backups stored in a locked vault.",
 "Does Vault Lock cost extra, and what do you still pay for in a locked vault?",
 ["available at no additional charge", "Standard AWS Backup storage charges apply"],
 [E(VL, "AWS Backup Vault Lock is available at no additional charge. Standard AWS Backup storage charges apply to backups stored in a locked vault.")],
 scope="AWS Backup Vault Lock", tier0=True, bullets=["1.3.S1", "4.3.S1"]))
f.append(F("backup-vault-lock-locked-backups-persist-until-lifecycle-ends", "restriction",
 "Backups within a locked vault cannot be deleted until their lifecycle completes, which gives persistent costs if retention is set too long; a recovery point with retention set to Always is kept forever once the grace time expires.",
 "Can you delete a backup in a locked vault before its lifecycle ends, and what is the cost risk?",
 ["cannot be deleted until their lifecycle completes", "retained forever"],
 [E(VL, "Backups within a locked vault cannot be deleted until their lifecycle completes, resulting in persistent costs if you are not careful. For example, ensure there are no recovery points with a retention period set to \"Always\"—once the grace time expires, these recovery points will be retained forever and cannot be altered or deleted.")],
 scope="locked vault", cond="the grace time has expired for the Always example", tier0=True, bullets=["1.3.S1", "4.3.S1"]))
f.append(F("backup-vault-lock-account-closure-deletes-vault-after-90-days", "restriction",
 "If you close an AWS account that contains a backup vault, AWS suspends the account for 90 days with backups intact, and if you do not reopen it in that time AWS deletes the vault contents even when Vault Lock was in place.",
 "Does Vault Lock protect backups if the AWS account is closed?",
 ["suspend your account for 90 days", "even if AWS Backup Vault Lock was in place"],
 [E(VL, "When you close an AWS account that contains a backup vault, AWS and AWS Backup suspend your account for 90 days with your backups intact. If you do not reopen your account during those 90 days, AWS deletes the contents of your backup vault, even if AWS Backup Vault Lock was in place.")],
 scope="closing an AWS account with a locked vault", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-not-glacier-vault-lock", "restriction",
 "AWS Backup Vault Lock is not the same feature as Amazon Glacier Vault Lock, which is compatible only with Amazon Glacier.",
 "Is AWS Backup Vault Lock the same as S3 Glacier Vault Lock?",
 ["not the same feature as Amazon Glacier Vault Lock", "compatible only with Amazon Glacier"],
 [E(VL, "AWS Backup Vault Lock is not the same feature as Amazon Glacier Vault Lock, which is compatible only with Amazon Glacier.")],
 scope="Vault Lock features compared", tier0=True, bullets=["1.3.S1"]))
# Primary backups to LAG
f.append(F("backup-lag-primary-backup-direct-single-copy", "capability",
 "A logically air-gapped vault can be the primary backup destination in the same account for scheduled and on-demand jobs, which removes the need to keep separate copies in a standard vault and a logically air-gapped vault.",
 "Can backups go straight into a logically air-gapped vault instead of being copied from a standard vault?",
 ["primary backup destination within the same account", "separate copies in both a standard backup vault"],
 [E(PB, "The logically air-gapped vault primary backup feature offers you the option to specify a logically air-gapped vault as a primary backup destination within the same account, for both scheduled and on-demand backup jobs. This eliminates the need to maintain separate copies in both a standard backup vault and a logically air-gapped vault, reducing costs and simplifying workflows while preserving the security benefits of logical air-gapping.")],
 scope="logically air-gapped vault primary backup", tier0=True, bullets=["2.2.S5", "4.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-primary-backup-same-account-and-region-only", "restriction",
 "To back up directly into a logically air-gapped vault, the vault must be in the same account and Region as your resources; you cannot create such backups directly cross-account or cross-Region.",
 "Can a primary backup go directly to a logically air-gapped vault in another Region or account?",
 ["same AWS account and Region as your resources", "cannot create backups directly cross-account or cross-Region"],
 [E(PB, "Your logically air-gapped vault must be in the same AWS account and Region as your resources to use this feature. You cannot create backups directly cross-account or cross-Region.")],
 scope="logically air-gapped vault primary backup", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-primary-backup-fully-managed-direct-no-vault-copy", "behavior",
 "Resource types with full AWS Backup management, such as EFS, S3 and DynamoDB with advanced features, can back up directly to a logically air-gapped vault: no recovery point is created in the backup vault and no copy operation is required.",
 "Which resource types back up directly to a logically air-gapped vault with no copy?",
 ["can back up directly to your logically air-gapped vault", "no copy operation is required"],
 [E(PB, "Some resource types, such as Amazon EFS, Amazon S3, Amazon DynamoDB with AWS Backup advanced features etc., that support full AWS Backup management, can back up directly to your logically air-gapped vault. No recovery point is created in your backup vault, and no copy operation is required.")],
 scope="resource types supporting full AWS Backup management", tier0=True, bullets=["2.2.S5", "4.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-primary-backup-ebs-ec2-aurora-fsx-temp-recovery-point", "behavior",
 "Resources such as EBS, EC2, Aurora and FSx cannot back up directly to a logically air-gapped vault: AWS Backup creates a temporary recovery point in the backup vault and then automatically copies it to the logically air-gapped vault.",
 "How do EBS, EC2, Aurora and FSx get backed up to a logically air-gapped vault as the primary target?",
 ["cannot back up directly to logically air-gapped vaults", "temporary recovery point in your backup vault"],
 [E(PB, "Resources such as Amazon EBS/EC2, Amazon Aurora, and Amazon FSx cannot back up directly to logically air-gapped vaults. For these resource types, AWS Backup creates a temporary recovery point in your backup vault and then automatically copies it to your logically air-gapped vault.")],
 scope="resource types not supporting full AWS Backup management", tier0=True, bullets=["2.2.S5", "4.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-primary-backup-no-new-charge", "pricing-dimension",
 "The logically air-gapped vault primary backup feature has no new pricing: you pay only for backups stored in logically air-gapped vaults and, for applicable resources, temporary snapshots at prevailing rates.",
 "Does primary backup to a logically air-gapped vault add a charge?",
 ["no new pricing for this feature", "temporary snapshots"],
 [E(PB, "There is no new pricing for this feature. You are only charged for backups stored in logically air-gapped vaults and for temporary snapshots (during their retention period in the system) for applicable resources at prevailing rates.")],
 scope="logically air-gapped vault primary backup", bullets=["4.3.S1"], vol="frequently-changing"))
# Multi-party approval
f.append(F("backup-mpa-capability-from-organizations-for-lag-vaults", "behavior",
 "Multi-party approval is a capability from AWS Organizations that you can add to logically air-gapped vaults, to protect critical operations through a distributed approval process.",
 "What is multi-party approval for logically air-gapped vaults?",
 ["a capability from AWS Organizations", "distributed approval process"],
 [E(M, "AWS Backup offers you the option to add Multi-party approval, a capability from AWS Organizations, to your logically air-gapped vaults. Multi-party approval provides an additional option to help to protect critical operations through a distributed approval process.")],
 scope="multi-party approval", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-mpa-restore-compromised-vault-contents", "behavior",
 "Multi-party approval helps protect critical resources and shorten the time to return to full operation after a disruption by malicious actors or malware, and helps you restore the contents of a logically air-gapped vault that may have been compromised.",
 "What is multi-party approval used for in AWS Backup?",
 ["minimize the time to return to full operation", "may have been compromised"],
 [E(M, "Multi-party approval is designed to help protect critical resources and to minimize the time to return to full operation, such as a disruption caused by malicious actors or malware events. This setup can help you restore the contents of a logically air-gapped vault that may have been compromised.")],
 scope="multi-party approval", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-mpa-trusted-group-approves-recovery-account-access", "behavior",
 "With multi-party approval, a group of trusted individuals can collaboratively approve access to a logically air-gapped vault from a separately created recovery account when malicious activity may compromise the primary account.",
 "Who approves access to a logically air-gapped vault from a recovery account?",
 ["group of trusted individuals", "separately-created recovery account"],
 [E(M, "As an AWS Backup customer, you can use Multi-party approval to grant approval capabilities of some operations to a group of trusted individuals who can collaboratively approve access to a logically air-gapped vault from a separately-created recovery account in the case of suspected malicious activity that may compromise use of the primary account.")],
 scope="multi-party approval", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-mpa-no-extra-cost-storage-charges-apply", "pricing-dimension",
 "There is no additional cost for multi-party approval teams with logically air-gapped vaults, but storage and cross-Region transfer charges apply.",
 "Does multi-party approval cost extra?",
 ["no additional cost", "storage and cross-region transfers charges apply"],
 [E(M, "There is no additional cost for integrating and using Multi-party approval teams with AWS Backup logically air-gapped vaults (storage and cross-region transfers charges apply, as shown on the pricing page).")],
 scope="multi-party approval", bullets=["4.3.S1"], vol="frequently-changing"))
f.append(F("backup-mpa-team-resources-only-in-us-east-1", "restriction",
 "Multi-party approval team resources can be created and stored only in the US East (N. Virginia) Region.",
 "In which Region are multi-party approval teams created?",
 ["can only be created and stored", "US East (N. Virginia)"],
 [E(M, "Multi-party approval Team resources can only be created and stored in AWS Region US East (N. Virginia).")],
 scope="multi-party approval teams", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-mpa-recommends-separate-recovery-organization", "behavior",
 "A best practice for multi-party approval is two or more AWS organizations: a primary organization that holds the logically air-gapped vaults and a secondary recovery organization where the approval team is managed.",
 "Where should the multi-party approval team be managed?",
 ["Two (or more) AWS organizations", "recovery organization"],
 [E(M, "Two (or more) AWS organizations through Organizations. One should be your primary organization where you have one or more accounts that have at least one logically air-gapped vault. The secondary organization should be your recovery organization. It is in this org where your multi-party approval team will be managed.")],
 scope="multi-party approval best practices", bullets=["2.2.S5"], vol="frequently-changing"))
dump("facts-behavior-05.json", f)
