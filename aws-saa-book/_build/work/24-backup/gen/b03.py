import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
V, AP, VL = D + "create-a-vault", D + "create-a-vault-access-policy", D + "vault-lock"
f = []
f.append(F("backup-vault-required-before-plan-or-job", "restriction",
 "You must create at least one backup vault before you create a backup plan or start a backup job.",
 "Do you need a backup vault before creating a backup plan or a backup job?",
 ["at least one vault", "before creating a backup plan or starting a backup job"],
 [E(V, "You must create at least one vault before creating a backup plan or starting a backup job.")],
 scope="AWS Backup vaults", bullets=["2.2.S5"]))
f.append(F("backup-default-vault-created-by-console", "behavior",
 "The first time you use the Backup vaults page of the AWS Backup console in a Region, the console automatically creates a default vault for that Region.",
 "When does AWS Backup create a default vault?",
 ["automatically creates a default vault for the Region", "first use the Backup Vaults page"],
 [E(V, "When you first use the Backup Vaults page of the AWS Backup console in an AWS Region, the console automatically creates a default vault for the Region.")],
 scope="per Region, AWS Backup console", bullets=["2.2.S5"]))
f.append(F("backup-default-vault-not-created-by-cli-sdk-cloudformation", "restriction",
 "If you use AWS Backup through the AWS CLI, AWS SDK or CloudFormation, a default vault is not created and you must create your own vault.",
 "Is a default vault created when you use AWS Backup through the CLI, SDK or CloudFormation?",
 ["a default vault is not created", "You must create your own vault"],
 [E(V, "However, if you use AWS Backup through the AWS CLI, AWS SDK, or CloudFormation, a default vault is not created. You must create your own vault.")],
 scope="AWS CLI, AWS SDK and CloudFormation", bullets=["2.2.S5"]))
f.append(F("backup-vault-kms-key-fixed-after-creation", "restriction",
 "After you create a backup vault and set its KMS encryption key, you cannot edit the key for that vault.",
 "Can you change the KMS key of a backup vault after it is created?",
 ["can no longer edit the key", "After you create a backup vault"],
 [E(V, "After you create a backup vault and set the AWS KMS encryption key, you can no longer edit the key for that backup vault.")],
 scope="backup vault encryption key", tier0=True, bullets=["2.2.S5"]))
f.append(F("backup-vault-default-key-aws-backup-alias", "default",
 "By default AWS Backup creates a KMS key with the alias aws/backup for the vault; you can choose that key or any other key in your account.",
 "Which KMS key does a backup vault use by default?",
 ["KMS key with the alias aws/backup", "any other key in your account"],
 [E(V, "By default, AWS Backup creates a KMS key with the alias `aws/backup` for you. You can choose that key or choose any other key in your account (cross-account KMS keys can be used via CLI).")],
 scope="backup vault KMS key", dm="default", adj=True, bullets=["2.2.S5"]))
f.append(F("backup-vault-key-applies-only-to-independent-encryption-types", "behavior",
 "The KMS key set on a backup vault applies only to backups of resource types that support AWS Backup independent encryption (the Full management column); backups of all other resource types use the key that encrypts the source resource.",
 "Does the vault's KMS key encrypt every backup in the vault?",
 ["applies to the backups of certain resource types", "key that is used to encrypt the source resource"],
 [E(V, "The encryption key that is specified in an AWS Backup vault applies to the backups of certain resource types. For more information about backup encryption, see Encryption for backups in AWS Backup in the Security section. Backups of all other resource types are backed up using the key that is used to encrypt the source resource.")],
 scope="backup vault KMS key", cond="Full management resource types use the vault key; other types keep the source key", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-delete-only-when-empty", "restriction",
 "You can delete a backup vault only after you delete (or your backup plan lifecycles expire) all the recovery points in it, to guard against accidental or malicious mass deletion.",
 "When can a backup vault be deleted?",
 ["only after you delete", "accidental or malicious mass deletion"],
 [E(V, "To guard against accidental or malicious mass deletion, you can delete a backup vault in AWS Backup only after you delete (or your backup plan lifecycles) all the recovery points in your backup vault.")],
 scope="backup vault deletion", tier0=True, bullets=["2.2.S5"]))
f.append(F("backup-plan-pointing-at-deleted-vault-fails", "behavior",
 "A backup plan that points to a deleted backup vault makes backup creation fail, so you update plans to point to new vaults when you delete a vault.",
 "What happens to a backup plan whose target vault is deleted?",
 ["point to a deleted backup vault", "cause the backup creation to fail"],
 [E(V, "When you delete a backup vault, update your backup plans to point to new backup vaults. A backup plan that points to a deleted backup vault will cause the backup creation to fail.")],
 scope="backup plans and vaults", rel="extended", bullets=["2.2.S5"]))
f.append(F("backup-vault-access-policy-allow-create-limit-delete", "capability",
 "You can assign policies to backup vaults and the resources in them, for example to let users create backup plans and on-demand backups but limit their ability to delete recovery points.",
 "How can you let users create backups but stop them deleting recovery points in a vault?",
 ["limit their ability to delete recovery points", "assign policies to backup vaults"],
 [E(AP, "With AWS Backup, you can assign policies to backup vaults and the resources they contain. Assigning policies allows you to do things like grant access to users to create backup plans and on-demand backups, but limit their ability to delete recovery points after they're created.")],
 scope="backup vault access policies", tier0=True, bullets=["2.2.S5", "1.3.S1"]))
f.append(F("backup-vault-access-policy-no-wildcard-action", "restriction",
 "Unlike other IAM-based policies, AWS Backup vault access policies do not support a wildcard in the Action key.",
 "Can a backup vault access policy use a wildcard in the Action element?",
 ["don't support a wildcard", "in the Action key"],
 [E(AP, "Unlike other IAM-based policies, AWS Backup access policies don't support a wildcard in the `Action` key.")],
 scope="AWS Backup vault access policies", rel="extended", bullets=["2.2.S5"]))
f.append(F("backup-vault-access-policy-controls-only-backup-apis", "behavior",
 "Vault access policies control only user access to AWS Backup APIs; backups such as EBS and RDS snapshots can also be reached through those services' own APIs, so you need separate IAM policies for them to control access fully.",
 "Does a vault access policy also block deleting EBS or RDS snapshot backups through the EBS or RDS APIs?",
 ["only control user access to AWS Backup APIs", "separate access policies in IAM"],
 [E(AP, "Vault access policies only control user access to AWS Backup APIs. Some backup types, such as Amazon Elastic Block Store (Amazon EBS) and Amazon Relational Database Service (Amazon RDS) snapshots, can also be accessed using the APIs of those services. You can create separate access policies in IAM that control access to those APIs to fully control the access to those backup types.")],
 scope="AWS Backup vault access policies", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-policy-cross-account-only-copy-into-vault", "restriction",
 "Whatever a vault access policy says, AWS Backup rejects cross-account access for any action other than backup:CopyIntoBackupVault; this applies to both standard and logically air-gapped vaults.",
 "Can another account call backup actions on a vault other than copying into it?",
 ["other than backup:CopyIntoBackupVault will be rejected", "both standard and logically air-gapped backup vaults"],
 [E(AP, "Regardless of the AWS Backup vault's access policy, cross-account access for any action other than `backup:CopyIntoBackupVault` will be rejected; that is, AWS Backup will reject any other request from an account that is different from the account of the resource that is being referenced. This restriction applies to vault access policies on both standard and logically air-gapped backup vaults.")],
 scope="vault access policies, standard and logically air-gapped vaults", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-policy-deny-delete-recovery-point-except-principal", "capability",
 "A resource-based access policy on a backup vault can prevent anyone except named principals from deleting a recovery point in that vault.",
 "How can you stop everyone except named principals from deleting recovery points in a vault?",
 ["resource-based access policy on a backup vault", "from deleting a recovery point"],
 [E(AP, "Follow these steps to create a resource-based access policy on a backup vault that prevents the deletion of any backups in the backup vault."),
  E(AP, "This policy prevents anyone who is not the principal from deleting a recovery point in the target backup vault.")],
 scope="backup vault access policy", tier0=True, bullets=["2.2.S5", "1.3.S1"]))
f.append(F("backup-vault-lock-compliance-immutable-by-anyone", "restriction",
 "A vault lock in compliance mode cannot be altered or deleted by any user or by AWS; it has a grace time period you set, after which the contents and the vault lock become immutable.",
 "Can anyone, including AWS, change or delete a compliance-mode vault lock?",
 ["cannot be altered or deleted by any user or by AWS", "grace time period you set"],
 [E(VL, "A vault lock in Compliance mode cannot be altered or deleted by any user or by AWS. A vault lock in compliance mode has a grace time period you set before it locks and the contents and vault lock become immutable.")],
 scope="Vault Lock, compliance mode", cond="immutable after the grace time ends", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-lock-compliance-config-fixed-while-recovery-points", "restriction",
 "When a lock is active in compliance mode and the grace time is over, the vault configuration cannot be altered or deleted by a customer, an account or data owner, or AWS as long as the vault contains recovery points.",
 "Can anyone delete or change a compliance-mode locked vault after the grace time while it holds recovery points?",
 ["cannot be altered or deleted by a customer, account/data owner, or AWS", "as long as it contains recovery points"],
 [E(VL, "When a lock is active in Compliance mode and the grace time is over, the vault configuration cannot be altered or deleted by a customer, account/data owner, or AWS as long as it contains recovery points.")],
 scope="Vault Lock, compliance mode, after the grace time", cond="the vault holds recovery points", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-lock-one-lock-per-vault", "limit",
 "Each vault can have one vault lock in place.",
 "How many vault locks can one backup vault have?",
 ["one vault lock", "Each vault"],
 [E(VL, "Each vault can have one vault lock in place.")],
 scope="per backup vault", dm="max", bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-governance-lock-removable-with-iam", "behavior",
 "A vault locked in governance mode can have its lock removed, and the vault managed or deleted, by users with sufficient IAM permissions.",
 "Who can remove a governance-mode vault lock?",
 ["lock removed by users with sufficient IAM permissions", "managed or deleted by users who have the appropriate IAM permissions"],
 [E(VL, "Vaults locked in governance mode can have the lock removed by users with sufficient IAM permissions."),
  E(VL, "A vault locked in Governance mode can be managed or deleted by users who have the appropriate IAM permissions.")],
 scope="Vault Lock, governance mode", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-compliance-grace-time-remove-or-change", "behavior",
 "In compliance mode, a locked vault cannot be deleted after the grace time ends if any recovery points are in it, but during the grace time you can still remove the vault lock and change its configuration.",
 "Can you remove a compliance-mode vault lock during the grace time?",
 ["During grace time, you can still remove the vault lock", "cooling-off period"],
 [E(VL, "Vaults locked in compliance mode cannot be deleted once the cooling-off period (\"grace time\") expires if any recovery points are in the vault. During grace time, you can still remove the vault lock and change the lock configuration.")],
 scope="Vault Lock, compliance mode", cond="grace time not yet expired", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-compliance-intent-lock-cannot-be-removed", "behavior",
 "Compliance mode is meant for vaults whose contents should never be deleted or altered until the retention period ends; once locked, the lock cannot be removed, though the vault itself can be deleted if it is empty.",
 "What is compliance mode of Vault Lock meant for, and can the lock be removed once it is locked?",
 ["the lock cannot be removed", "expected to never be deleted or altered"],
 [E(VL, "Compliance mode is intended for backup vaults in which the vault (and by extension, its contents) is expected to never be deleted or altered until the data retention period is complete. Once a vault in compliance mode is locked, it is immutable, meaning the lock cannot be removed (the vault itself can be deleted if it is empty and does not contain any recovery points).")],
 scope="Vault Lock, compliance mode", cond="vault empty to be deletable", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-governance-intent-designated-personnel", "behavior",
 "Governance mode lets only users with sufficient IAM privileges manage the vault, which helps an organization ensure only designated personnel can change a backup vault.",
 "What is governance mode of Vault Lock meant for?",
 ["only designated personnel can make changes", "sufficient IAM privileges"],
 [E(VL, "Governance mode is intended to allow a vault to be managed only by users with sufficient IAM privileges. Governance mode helps an organization meet governance requirements, ensuring only designated personnel can make changes to a backup vault.")],
 scope="Vault Lock, governance mode", bullets=["1.3.S1"]))
f.append(F("backup-vault-lock-denies-delete-and-lifecycle-change-even-root", "behavior",
 "If any user, including the root user, tries to delete a backup or change its lifecycle properties in a locked vault, AWS Backup denies the operation.",
 "Can the root user delete a backup or shorten its lifecycle in a locked vault?",
 ["including the root user", "AWS Backup will deny the operation"],
 [E(VL, "If any user (including the root user) attempts to delete a backup or change the lifecycle properties in a locked vault, AWS Backup will deny the operation.")],
 scope="locked backup vault", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-vault-lock-enforced-even-during-grace-time", "behavior",
 "While a vault is locked, delete or update operations on the recovery points in it fail, even while you are still within the grace time.",
 "Does Vault Lock block deletes during the grace time too?",
 ["delete or update operations to the recovery points", "regardless of whether you are still in the cooling-off grace time period"],
 [E(VL, "True means that AWS Backup Vault Lock causes delete or update operations to the recovery points stored in the vault to fail (regardless of whether you are still in the cooling-off grace time period).")],
 scope="locked vault (Locked true)", bullets=["1.3.S1"]))
dump("facts-behavior-03.json", f)
