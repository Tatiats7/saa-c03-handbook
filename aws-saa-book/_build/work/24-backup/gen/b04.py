import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
L, PB = D + "logicallyairgappedvault", D + "lag-vault-primary-backup"
f = []
f.append(F("backup-lag-vault-definition-secondary-vault-rto", "behavior",
 "A logically air-gapped vault is a secondary type of vault with additional security beyond a standard backup vault and the ability to share vault access with other accounts, so recovery time can be faster and more flexible after an incident.",
 "What is a logically air-gapped vault in AWS Backup?",
 ["secondary type of vault", "increased security beyond a standard backup vault"],
 [E(L, "AWS Backup offers a secondary type of vault which can store backups in a container with additional security features. A logically air-gapped vault is a specialized vault which provides increased security beyond a standard backup vault, as well as the ability to share vault access to other accounts so that recovery time objectives (RTOs) can be faster and more flexible in case of an incident that requires rapid restoration of resources.")],
 scope="logically air-gapped vault", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-encryption-key-and-compliance-lock", "behavior",
 "Each logically air-gapped vault is encrypted with an AWS owned key (the default) or optionally a customer managed KMS key, and each vault is equipped with Vault Lock compliance mode.",
 "How is a logically air-gapped vault encrypted and locked?",
 ["AWS owned key (default)", "Vault Lock's compliance mode"],
 [E(L, "Logically air-gapped vaults come equipped with additional protection features; each vault is encrypted with either an AWS owned key (default) or optionally with a customer-managed KMS key, and each vault is equipped with AWS Backup Vault Lock's compliance mode.")],
 scope="logically air-gapped vault", cond="compliance mode is always on", dm="default", tier0=True, bullets=["2.2.S5", "1.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-vault-mpa-recovery-when-owner-inaccessible", "capability",
 "You can integrate logically air-gapped vaults with multi-party approval (MPA) to recover the backups in the vault even if the vault-owning account is inaccessible.",
 "How can you recover backups in a logically air-gapped vault when the owning account is inaccessible?",
 ["even if the vault-owning account is inaccessible", "Multi-party approval"],
 [E(L, "You can integrate your logically air-gapped vaults with Multi-party approval (MPA) to enable recovery of backups in the vaults even if the vault-owning account is inaccessible, which helps to maintain business continuity.")],
 scope="logically air-gapped vault with multi-party approval", tier0=True, bullets=["2.2.S5", "1.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-vault-ram-share-restore-in-other-account", "capability",
 "You can use AWS RAM to share a logically air-gapped vault with other AWS accounts, including accounts in other organizations, so the backups can be restored from an account the vault is shared with.",
 "How do you let a different account restore backups from a logically air-gapped vault?",
 ["AWS Resource Access Manager (RAM)", "accounts in other organizations"],
 [E(L, "Further more, you can choose to integrate with AWS Resource Access Manager (RAM) to share a logically air-gapped vault with other AWS accounts (including accounts in other organizations) so that the backups stored within the vault can be restored from an account with which the vault is shared, if needed for data loss recovery or restore testing.")],
 scope="logically air-gapped vault with AWS RAM", tier0=True, bullets=["2.2.S5", "1.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-vault-stored-in-backup-service-owned-account", "behavior",
 "A logically air-gapped vault stores its backups in an AWS Backup service owned account, which is why the backups appear as shared outside your organization in CloudTrail modify attribute items.",
 "Where does a logically air-gapped vault store its backups?",
 ["AWS Backup service owned account", "shared outside your organization"],
 [E(L, "As part of this added security, a logically air-gapped vault stores its backups in an AWS Backup service owned account (which results in backups shown as shared outside your organization in modify attribute items in AWS CloudTrail logs).")],
 scope="logically air-gapped vault", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-owner-account-closed-access-via-mpa", "behavior",
 "If the account that owns a logically air-gapped vault is closed, you can still restore or copy its backups through multi-party approval until the post-closure period ends; after that the backups are no longer accessible.",
 "Can you still reach backups in a logically air-gapped vault after its owning account is closed?",
 ["until the post-closure period ends", "no longer accessible"],
 [E(L, "In the scenario where your logically air-gapped vault owning account is closed (maliciously or otherwise), you can still access backups in the vault (restore or copy them) via MPA until the post-closure period ends. After the post-closure period expires, the backups are no longer accessible.")],
 scope="logically air-gapped vault with multi-party approval", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-recommend-cross-region-copies", "behavior",
 "For greater resiliency, AWS recommends creating cross-Region copies in logically air-gapped vaults, in the same or separate accounts.",
 "What does AWS recommend for greater resiliency with logically air-gapped vaults?",
 ["creating cross-Region copies in logically air-gapped vaults", "same or separate accounts"],
 [E(L, "For greater resiliency, we recommend creating cross-Region copies in logically air-gapped vaults in same or separate accounts.")],
 scope="logically air-gapped vault", hard=False, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-secondary-vault-use-case-features", "behavior",
 "A logically air-gapped vault is a secondary vault for a data protection strategy that is automatically set with a compliance-mode vault lock, encrypts by default with an AWS owned key, and holds backups that can be shared with and restored from a different account.",
 "What does a logically air-gapped vault give you compared with keeping backups only in a standard vault?",
 ["secondary vault that serves as part of a data protection strategy", "Is automatically set with a vault lock in compliance mode"],
 [E(L, "A logically air-gapped vault is a secondary vault that serves as part of a data protection strategy."),
  E(L, "Is automatically set with a vault lock in compliance mode"),
  E(L, "Contains backups which, through AWS RAM or MPA, can be shared with and restored from a different account than the one that created the backup")],
 scope="logically air-gapped vault", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported", "restriction",
 "Unencrypted Aurora, DocumentDB and Neptune clusters are not supported for a logically air-gapped vault, because they do not support encryption of unencrypted DB cluster snapshots.",
 "Can an unencrypted Aurora cluster be backed up into a logically air-gapped vault?",
 ["Unencrypted Amazon Aurora, Amazon DocumentDB, and Amazon Neptune clusters", "are not supported for logically air-gapped vault"],
 [E(L, "Unencrypted Amazon Aurora, Amazon DocumentDB, and Amazon Neptune clusters are not supported for logically air-gapped vault, as they do not support encryption of unencrypted DB cluster snapshots.")],
 scope="logically air-gapped vault, Aurora, DocumentDB, Neptune", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-standard-vault-is-primary-type", "behavior",
 "A standard backup vault is the primary type of vault in AWS Backup and each backup is stored in a backup vault when the backup is created; a logically air-gapped vault stores primary backups or copies of backups first created in a standard backup vault.",
 "What is the difference in role between a standard backup vault and a logically air-gapped vault?",
 ["primary and standard type of vault", "initially created and stored within a standard backup vault"],
 [E(L, "A backup vault is the primary and standard type of vault used in AWS Backup. Each backup is stored in a backup vault when the backup is created."),
  E(L, "A logically air-gapped vault is a specialized vault with additional security and flexible sharing for faster recovery time (RTO). This vault stores primary backups or copies of backups that were initially created and stored within a standard backup vault.")],
 scope="standard backup vault, logically air-gapped vault", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-source-key-fully-managed-cmk-or-aws-managed", "behavior",
 "When you create or copy a backup of a fully managed resource type into a logically air-gapped vault, the source resource can be encrypted by a customer managed key or an AWS managed key.",
 "Which source encryption keys work for copying a fully managed resource type into a logically air-gapped vault?",
 ["customer managed key or by an AWS managed key", "fully managed resource type"],
 [E(L, "When you create or copy a backup of a fully managed resource type, the source resource can be encrypted by a customer managed key or by an AWS managed key.")],
 scope="fully managed resource types, logically air-gapped vault", tier0=True, bullets=["2.2.S5", "1.3.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-source-key-not-fully-managed-needs-cmk", "restriction",
 "When you create or copy a backup of a resource type that is not fully managed into a logically air-gapped vault, the source must be encrypted with a customer managed key; AWS managed keys are not supported for those resources.",
 "Can an EBS volume encrypted with an AWS managed key be copied to a logically air-gapped vault?",
 ["the source must be encrypted with a customer managed key", "AWS managed keys for not fully managed resources are not supported"],
 [E(L, "When you create or copy a backup of other resource types (ones not fully managed), the source must be encrypted with a customer managed key. AWS managed keys for not fully managed resources are not supported.")],
 scope="resource types not fully managed by AWS Backup, logically air-gapped vault", tier0=True, bullets=["2.2.S5", "1.3.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-lag-to-lag-copy-on-demand-only", "restriction",
 "You can copy a backup from one logically air-gapped vault to another only on demand, not on a schedule in a backup plan, and you can copy from a logically air-gapped vault to a standard vault only if the copy is encrypted with a customer managed key.",
 "Can a backup plan schedule copies from one logically air-gapped vault to another?",
 ["this type of backup cannot be scheduled in a backup plan", "encrypted with a customer managed key"],
 [E(L, "You can copy a backup from one logically air-gapped vault to another logically air-gapped vault on-demand (this type of backup cannot be scheduled in a backup plan). You can copy a backup from a logically air-gapped vault to a standard backup vault as long as the copy is encrypted with a customer managed key.")],
 scope="copies out of a logically air-gapped vault", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-shared-account-view-restore-not-copy", "restriction",
 "A copy of a backup can be created only from the account that owns the logically air-gapped vault; accounts the vault is shared with can view or restore a backup but cannot create a copy.",
 "Can an account that a logically air-gapped vault is shared with copy its backups?",
 ["view or a restore a backup, but not to create a copy", "from the account to which the vault belongs"],
 [E(L, "A copy of a backup can be created from the account to which the vault belongs. Accounts with which the vault has been shared have the ability to view or a restore a backup, but not to create a copy.")],
 scope="accounts a logically air-gapped vault is shared with", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-share-with-account-ids-only", "restriction",
 "A logically air-gapped vault can be shared only with individual AWS account IDs, in your organization or in another organization; it cannot be shared with an entire organization or with organizational units.",
 "Can a logically air-gapped vault be shared with a whole organization or an OU?",
 ["only individual account IDs are supported as share principals", "cannot be shared with an entire organization"],
 [E(L, "A vault can be shared with individual AWS account IDs only. You can share with an account in your organization or with an account in another organization. The vault cannot be shared with an entire organization or with organizational units (OUs) — only individual account IDs are supported as share principals.")],
 scope="sharing a logically air-gapped vault through AWS RAM", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-restore-from-owner-or-shared-account", "capability",
 "You can restore a backup in a logically air-gapped vault from the account that owns the vault or from any account the vault is shared with.",
 "Which accounts can restore a backup stored in a logically air-gapped vault?",
 ["from either the account that owns the vault", "any account with which the vault is shared"],
 [E(L, "You can restore a backup stored in a logically air-gapped vault from either the account that owns the vault or from any account with which the vault is shared.")],
 scope="logically air-gapped vault", tier0=True, bullets=["2.2.S5", "1.3.K2"], vol="frequently-changing"))
f.append(F("backup-lag-vault-delete-only-when-empty-key-deleted-after-seven-days", "restriction",
 "A logically air-gapped vault cannot be deleted while it still contains backups, and deleting the vault also deletes its key seven days later.",
 "Can you delete a logically air-gapped vault that still holds recovery points?",
 ["cannot be deleted if they still contain backups", "seven days after the vault is deleted"],
 [E(L, "Vaults cannot be deleted if they still contain backups (recovery points). Ensure the vault is empty of backups before you initiate a delete operation."),
  E(L, "Deletion of a vault also deletes the key associated with the vault seven days after the vault is deleted in accordance with key deletion policy.")],
 scope="logically air-gapped vault deletion", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-key-chosen-at-creation-only", "restriction",
 "You can select the KMS key of a logically air-gapped vault only during vault creation; all backups in the vault are encrypted with that key and you cannot change or migrate the vault to a different key.",
 "Can you change the encryption key of a logically air-gapped vault after creating it?",
 ["only select an AWS KMS encryption key during vault creation", "cannot change or migrate your vaults"],
 [E(L, "You can only select an AWS KMS encryption key during vault creation. Once created, all backups contained in the vault will be encrypted with that key. You cannot change or migrate your vaults to use a different encryption key.")],
 scope="logically air-gapped vault encryption key", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-aws-owned-key-recommended", "behavior",
 "AWS Backup recommends using AWS owned keys with logically air-gapped vaults.",
 "Which key type does AWS Backup recommend for a logically air-gapped vault?",
 ["recommends using AWS owned keys", "logically air-gapped vaults"],
 [E(L, "AWS Backup recommends using AWS owned keys with logically air-gapped vaults.")],
 scope="logically air-gapped vault encryption", hard=False, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vault-restore-access-vault-view-delete", "behavior",
 "Deleting a restore access backup vault, which is a view of an underlying logically air-gapped vault with no recovery points of its own, is allowed from the recovery account even in FAILED state, and Vault Lock compliance mode does not block it.",
 "Does Vault Lock compliance mode stop you deleting a restore access vault?",
 ["is a view of an underlying logically air-gapped vault", "Vault Lock (compliance mode) does not block this deletion"],
 [E(L, "A restore access backup vault is a view of an underlying logically air-gapped vault and contains no recovery points of its own. You can delete it with DeleteBackupVault from the recovery account even when it is in FAILED state. Vault Lock (compliance mode) does not block this deletion.")],
 scope="restore access backup vault", rel="extended", bullets=["2.2.S5"], vol="frequently-changing"))
dump("facts-behavior-04.json", f)
