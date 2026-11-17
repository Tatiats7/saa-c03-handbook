import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
EN, CR, CA = D + "encryption", D + "cross-region-backup", D + "create-cross-account-backup"
f = []
f.append(F("backup-encryption-independent-for-fully-managed-types", "behavior",
 "For resource types that support full AWS Backup management, backups can use an encryption method other than the source resource's, controlled by the KMS key of the backup vault where the backup is stored.",
 "What is independent encryption in AWS Backup and which resource types get it?",
 ["independent encryption", "encryption method other than one determined by the source resource's encryption"],
 [E(EN, "AWS Backup offers independent encryption for resource types that support full AWS Backup management. Independent encryption means that recovery points (backups) you create through AWS Backup can have an encryption method other than one determined by the source resource's encryption."),
  E(EN, "This encryption is controlled through the AWS KMS key configuration in the backup vault where your backup in stored.")],
 scope="resource types with full AWS Backup management", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-encryption-not-fully-managed-inherit-source", "behavior",
 "Backups of resource types that are not fully managed by AWS Backup typically inherit the encryption settings of their source resource.",
 "Which encryption settings do backups of resource types that are not fully managed by AWS Backup use?",
 ["not fully managed by AWS Backup", "inherit the encryption settings from their source resource"],
 [E(EN, "Backups of resource types that are not fully managed by AWS Backup typically inherit the encryption settings from their source resource.")],
 scope="resource types not fully managed by AWS Backup", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-encryption-role-needs-kms-access-else-silent-skip", "restriction",
 "The IAM role used for a backup or restore must have access to the KMS key; otherwise the job succeeds but the objects are not backed up or restored.",
 "What happens if the IAM role of a backup job cannot use the KMS key?",
 ["Otherwise the job is successful", "objects are not backed up or restored"],
 [E(EN, "Your IAM role must have access to the KMS key being used to back up and restore the object. Otherwise the job is successful but the objects are not backed up or restored.")],
 scope="backup and restore jobs, KMS key", bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-encryption-independent-uses-aes-256", "behavior",
 "When AWS Backup independently encrypts a backup, it uses the AES-256 encryption algorithm.",
 "Which algorithm does AWS Backup use for independent encryption?",
 ["industry-standard AES-256 encryption algorithm", "independently encrypts a backup"],
 [E(EN, "When AWS Backup independently encrypts a backup, it uses the industry-standard AES-256 encryption algorithm.")],
 scope="independent encryption", bullets=["1.3.S1"]))
f.append(F("backup-encryption-audit-manager-detects-unencrypted", "capability",
 "AWS Backup Audit Manager helps you automatically detect unencrypted backups.",
 "How can you detect unencrypted backups in AWS Backup?",
 ["automatically detect unencrypted backups", "AWS Backup Audit Manager helps you"],
 [E(EN, "AWS Backup Audit Manager helps you automatically detect unencrypted backups.")],
 scope="AWS Backup Audit Manager", bullets=["1.3.S1"]))
f.append(F("backup-encryption-copy-uses-destination-vault-key", "behavior",
 "When you copy backups across accounts or Regions, AWS Backup automatically encrypts the copies for most resource types, even if the original backup is unencrypted, using the KMS key of the target vault.",
 "Which key encrypts a cross-Region or cross-account copy?",
 ["encrypts the copy using the KMS key of the target vault", "even if the original backup is unencrypted"],
 [E(EN, "When you copy your backups across accounts or Regions, AWS Backup automatically encrypts those copies for most resource types, even if the original backup is unencrypted. AWS Backup encrypts the copy using the KMS key of the target vault.")],
 scope="cross-account and cross-Region copies", cond="most resource types", tier0=True, bullets=["1.3.S1", "1.3.S5"]))
f.append(F("backup-encryption-copy-fully-managed-cmk-or-backup-managed-key", "capability",
 "For a copy of a resource fully managed by AWS Backup, you can encrypt it with a customer managed key or the AWS Backup managed key (aws/backup).",
 "Which keys can encrypt a copy of a fully managed resource type?",
 ["customer managed key (CMK)", "AWS Backup managed key"],
 [E(EN, "For a copy of a recovery point (backup) of a resource that is fully managed by AWS Backup, you can choose to encrypt it with a customer managed key (CMK) or an AWS Backup managed key (aws/backup).")],
 scope="copies of fully managed resource types", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
f.append(F("backup-encryption-copy-not-fully-managed-cmk-or-service-key", "restriction",
 "For a copy of a resource that is not fully managed by AWS Backup, the destination vault key must be a customer managed key or the managed key of the service that owns the resource; for an EC2 instance a Backup managed key cannot be used, and a CMK or aws/ebs must be used to avoid copy job failure.",
 "Can the AWS Backup managed key be the destination vault key when copying an EC2 instance?",
 ["a Backup managed key cannot be used", "must be a CMK or the managed key of the service"],
 [E(EN, "For a copy of a recovery point of a resource that is not fully managed by AWS Backup, the key associated to the destination vault must be a CMK or the managed key of the service that owns the underlying resource. For example, if you are copying an EC2 instance, a Backup managed key cannot be used. Instead, a CMK or Amazon EBS KMS key (aws/ebs) must be used to avoid copy job failure.")],
 scope="copies of resource types not fully managed by AWS Backup", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
f.append(F("backup-encryption-cross-account-aws-managed-key-unsupported-not-fully-managed", "restriction",
 "Cross-account copy with AWS managed keys is not supported for resources that are not fully managed by AWS Backup, because the key policy of an AWS managed key is immutable and prevents copying the key across accounts.",
 "Can a not fully managed resource encrypted with an AWS managed key be copied to another account?",
 ["isn't supported for resources that aren't fully managed by AWS Backup", "key policy of an AWS managed key is immutable"],
 [E(EN, "Cross-account copy with AWS managed keys isn't supported for resources that aren't fully managed by AWS Backup. The key policy of an AWS managed key is immutable, which prevents copying the key across accounts.")],
 scope="cross-account copies of resource types not fully managed by AWS Backup", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
f.append(F("backup-encryption-copies-of-unencrypted-aurora-docdb-neptune-unencrypted", "behavior",
 "Copies of unencrypted Aurora, DocumentDB and Neptune clusters are also unencrypted.",
 "Is a copy of an unencrypted Aurora cluster backup encrypted?",
 ["are also unencrypted", "unencrypted Amazon Aurora, Amazon DocumentDB, and Amazon Neptune clusters"],
 [E(EN, "Copies of unencrypted Amazon Aurora, Amazon DocumentDB, and Amazon Neptune clusters are also unencrypted.")],
 scope="copies of Aurora, DocumentDB and Neptune backups", rel="extended", bullets=["1.3.S1"]))
f.append(F("backup-encryption-failed-jobs-from-deny-or-revoked-grant", "behavior",
 "Failed backup jobs can come from one or more Deny statements on the KMS key or from a grant revoked for the key.",
 "What KMS problems make AWS Backup jobs fail?",
 ["Deny statements applied to the KMS key", "a grant revoked for the key"],
 [E(EN, "Failed jobs can occur due to either one or more Deny statements applied to the KMS key or due to a grant revoked for the key.")],
 scope="AWS Backup and KMS keys", rel="extended", bullets=["1.3.S1", "2.2.S5"]))
# Encryption table rows
f.append(F("backup-encryption-s3-row", "behavior",
 "S3 backups are encrypted with a KMS key associated with the backup vault (customer managed, or the AWS managed key of AWS Backup), AWS Backup encrypts all S3 backups even if the source bucket is unencrypted, and independent AWS Backup encryption is supported.",
 "How are S3 backups in AWS Backup encrypted?",
 ["Supported", "even if the source Amazon S3 buckets are not encrypted"],
 [ROW(EN, 0, 0)], scope="Amazon S3 backups", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-encryption-ddb-advanced-row", "behavior",
 "After you enable advanced DynamoDB backup features, DynamoDB backups are always encrypted with the KMS key configured in the AWS Backup vault, and independent AWS Backup encryption is supported.",
 "How are DynamoDB backups encrypted once advanced features are enabled?",
 ["DynamoDB backups are always encrypted", "Supported"],
 [ROW(EN, 0, 2)], scope="DynamoDB with advanced backup features", tier0=True, bullets=["1.3.S1", "4.1.S6"]))
f.append(F("backup-encryption-ddb-without-advanced-row", "behavior",
 "Without advanced DynamoDB backup features, DynamoDB backups are encrypted with the key of the source table (snapshots of unencrypted tables stay unencrypted) and independent AWS Backup encryption is not supported.",
 "How are DynamoDB backups encrypted without the advanced features?",
 ["same encryption key that was used to encrypt the source DynamoDB table", "Not supported"],
 [ROW(EN, 0, 3)], scope="DynamoDB without advanced backup features", tier0=True, bullets=["1.3.S1", "4.1.S6"]))
f.append(F("backup-encryption-efs-row", "behavior",
 "EFS backups are always encrypted with the KMS key configured in the AWS Backup vault, and independent AWS Backup encryption is supported.",
 "How are EFS backups encrypted in AWS Backup?",
 ["Amazon EFS backups are always encrypted", "Supported"],
 [ROW(EN, 0, 4)], scope="Amazon EFS backups", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-encryption-ebs-row", "behavior",
 "By default EBS backups are encrypted with the key of the source volume or are unencrypted, you can override this during restore by specifying a KMS key, and independent AWS Backup encryption is not supported.",
 "How are EBS backups encrypted in AWS Backup?",
 ["encrypted using the key that was used to encrypt the source volume", "Not supported"],
 [ROW(EN, 0, 5)], scope="Amazon EBS backups", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-encryption-rds-row", "behavior",
 "RDS snapshots are encrypted with the key of the source database (snapshots of unencrypted databases stay unencrypted), and independent AWS Backup encryption is not supported.",
 "How are RDS backups encrypted in AWS Backup?",
 ["same encryption key that was used to encrypt the source Amazon RDS database", "Not supported"],
 [ROW(EN, 0, 7)], scope="Amazon RDS backups", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-encryption-aurora-row", "behavior",
 "Aurora cluster snapshots are encrypted with the key of the source cluster (snapshots of unencrypted clusters stay unencrypted), and independent AWS Backup encryption is not supported.",
 "How are Aurora backups encrypted in AWS Backup?",
 ["same encryption key that was used to encrypt the source Amazon Aurora cluster", "Not supported"],
 [ROW(EN, 0, 8)], scope="Amazon Aurora backups", tier0=True, bullets=["1.3.S1"]))
dump("facts-behavior-07.json", f)

g = []
g.append(F("backup-cross-region-copy-on-demand-or-scheduled", "capability",
 "AWS Backup can copy backups to multiple AWS Regions on demand or automatically as part of a scheduled backup plan.",
 "How can you copy backups to another Region with AWS Backup?",
 ["on demand or automatically as part of a scheduled backup plan", "copy backups to multiple AWS Regions"],
 [E(CR, "Using AWS Backup, you can copy backups to multiple AWS Regions on demand or automatically as part of a scheduled backup plan.")],
 scope="cross-Region copy", tier0=True, bullets=["1.3.S5"]))
g.append(F("backup-cross-region-copy-minimum-distance-requirement", "behavior",
 "AWS Backup describes cross-Region copy as particularly valuable when business continuity or compliance requirements call for storing backups a minimum distance away from production data.",
 "Why would you copy backups to another Region?",
 ["business continuity or compliance requirements", "a minimum distance away from your production data"],
 [E(CR, "Cross-Region replication is particularly valuable if you have business continuity or compliance requirements to store backups a minimum distance away from your production data.")],
 scope="cross-Region copy", bullets=["1.3.S5", "2.2.K4"]))
g.append(F("backup-cross-region-first-copy-full-then-incremental", "behavior",
 "The first copy of a backup to a new Region is a full copy; for services that support incremental backups, later copies in that Region are in general incremental, and AWS Backup re-encrypts the copy with the destination vault's customer managed key.",
 "Is a cross-Region copy full or incremental?",
 ["copies the backup in full", "subsequent copies of that backup in the same AWS Region will be incremental"],
 [E(CR, "When you copy a backup to a new AWS Region for the first time, AWS Backup copies the backup in full. In general, if a service supports incremental backups, subsequent copies of that backup in the same AWS Region will be incremental. AWS Backup will re-encrypt your copy using the customer managed key of your destination vault.")],
 scope="cross-Region copy", tier0=True, bullets=["1.3.S5"]))
g.append(F("backup-cross-region-ebs-different-key-full-copy", "behavior",
 "For EBS, copying a snapshot to a vault that uses a different KMS key gives a full (not incremental) copy; if you always copy to the same vault with the same key, later copies stay incremental.",
 "When is a cross-Region copy of an EBS snapshot full instead of incremental?",
 ["results in a full (not incremental) copy", "subsequent copies remain incremental"],
 [E(CR, "An exception is Amazon EBS, where copying a snapshot to a vault that uses a different AWS KMS encryption key results in a full (not incremental) copy. If you consistently copy to the same vault with the same encryption key, subsequent copies remain incremental.")],
 scope="EBS snapshot copies", rel="extended", bullets=["1.3.S5"]))
g.append(F("backup-cross-region-no-cold-tier-copies", "restriction",
 "AWS Backup does not support cross-Region copies for storage in cold tiers.",
 "Can a cross-Region copy be stored in a cold tier?",
 ["does not support cross-Region copies for storage in cold tiers", "cold tiers"],
 [E(CR, "AWS Backup does not support cross-Region copies for storage in cold tiers.")],
 scope="cross-Region copies", tier0=True, bullets=["1.3.S5", "4.1.S6"]))
g.append(F("backup-cross-account-no-cold-tier-copies", "restriction",
 "AWS Backup does not support cross-account copies for storage in cold tiers.",
 "Can a cross-account copy be stored in a cold tier?",
 ["does not support cross-account copies for storage in cold tiers", "cold tiers"],
 [E(CA, "AWS Backup does not support cross-account copies for storage in cold tiers.")],
 scope="cross-account copies", tier0=True, bullets=["1.3.S5", "4.1.S6"]))
g.append(F("backup-cross-region-rds-copies-default-option-group", "behavior",
 "AWS Backup does not pass the option group in a cross-Region RDS copy; it copies the default option group even if you configured a custom option group.",
 "Which RDS option group does a cross-Region copy by AWS Backup use?",
 ["does not pass the option group", "copies the default option group"],
 [E(CR, "AWS Backup does not pass the option group when performing a cross-Region copy. Instead, AWS Backup copies the default option group, even if you have configured a custom option group.")],
 scope="Amazon RDS cross-Region copies", rel="extended", bullets=["1.3.S5"]))
g.append(F("backup-cross-account-requires-same-organization", "restriction",
 "To manage resources across accounts in AWS Backup, the accounts must belong to the same organization in AWS Organizations.",
 "Can you copy backups to an account in a different AWS Organizations organization?",
 ["must belong to the same organization", "AWS Organizations"],
 [E(CA, "Before you manage resources across multiple AWS accounts in AWS Backup, your accounts must belong to the same organization in the AWS Organizations service."),
  E(CA, "You can choose more than one destination account. The destination account must be in the same organization as the source account in AWS Organizations.")],
 scope="cross-account copy", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
g.append(F("backup-cross-account-copy-purpose-recover-deleted-original", "behavior",
 "A cross-account backup securely copies backups to accounts in your organization, and if the original backup is inadvertently deleted you can copy it from the destination account back to the source account and start the restore.",
 "How does a cross-account copy help if the original backup is deleted?",
 ["copy the backup from its destination account to its source account", "inadvertently deleted"],
 [E(CA, "Use a cross-account backup if you want to securely copy your backups to one or more AWS accounts in your organization for operational or security reasons. If your original backup is inadvertently deleted, you can copy the backup from its destination account to its source account, and then start the restore.")],
 scope="cross-account copy", tier0=True, bullets=["1.3.S5", "1.3.S1", "2.2.S5"]))
g.append(F("backup-cross-account-destination-vault-key-policy-and-shared-cmk", "behavior",
 "For a cross-account copy you create a backup vault in the destination account with an encryption key and a resource-based access policy that lets AWS Backup access the resources, and in the source account you share a customer managed key with the destination account if the resources use one.",
 "What must be set up in the destination and source accounts for a cross-account copy?",
 ["you must create a backup vault", "share this customer managed key with the destination account"],
 [E(CA, "In your destination account, you must create a backup vault. Then, you assign an encryption key to encrypt backups in the destination account, and a resource-based access policy to allow AWS Backup to access the resources you would like to copy. In the source account, if your resources are encrypted with a customer managed key, you must share this customer managed key with the destination account.")],
 scope="cross-account copy", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
g.append(F("backup-cross-account-destination-key-fully-managed-vs-others", "restriction",
 "For a cross-account copy of resources fully managed by AWS Backup the destination vault can use a customer managed key or the AWS Backup managed key; for all other resource types a customer managed key is required, because AWS managed key policies are immutable and cannot be shared cross-account.",
 "Which destination vault key does a cross-account copy need?",
 ["a customer managed key is required", "AWS managed key policies are immutable"],
 [E(CA, "For resources fully managed by AWS Backup, you can use either a customer managed key or the AWS Backup managed key (aws/backup) for the destination vault. For all other resource types, a customer managed key is required because AWS managed key policies are immutable and cannot be shared cross-account.")],
 scope="cross-account copy destination vault key", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
g.append(F("backup-cross-account-management-account-enables-feature", "behavior",
 "The AWS Organizations management account opts in to cross-account backup, and before cross-account backups can start you must enable cross-account backup in the AWS Backup console or through the UpdateGlobalSettings API.",
 "Which account enables cross-account backup for an organization?",
 ["management account", "UpdateGlobalSettings"],
 [E(CA, "The management account is the primary account in your organization, as defined by AWS Organizations, that you use to opt-in to cross-account backup across your AWS accounts. Before your organization can start with cross-account backups, you must enable cross-account backup in the AWS Backup console or through the UpdateGlobalSettings API.")],
 scope="cross-account backup", tier0=True, bullets=["1.3.S5", "1.3.S1"]))
g.append(F("backup-cross-account-enable-only-with-management-credentials", "restriction",
 "Cross-account backup can be enabled or disabled only with the credentials of the AWS Organizations management account.",
 "Who can enable or disable cross-account backup?",
 ["can only be enabled or disabled using these credentials", "management account credentials"],
 [E(CA, "Log in using your AWS Organizations management account credentials. Cross-account backup can only be enabled or disabled using these credentials.")],
 scope="cross-account backup setting", bullets=["1.3.S5", "1.3.S1"]))
g.append(F("backup-cross-account-destination-vault-must-allow-copy-into", "restriction",
 "You must allow backup:CopyIntoBackupVault in the access policy of the destination backup vault; without that policy attempts to copy into the destination account are denied.",
 "What must the destination vault's access policy allow for cross-account copy?",
 ["the access policy backup:CopyIntoBackupVault", "will deny attempts to copy into the destination account"],
 [E(CA, "You must “Allow” the access policy `backup:CopyIntoBackupVault` for your destination backup vault. The absence of this policy will deny attempts to copy into the destination account.")],
 scope="destination backup vault of a cross-account copy", tier0=True, bullets=["1.3.S5", "2.2.S5"]))
dump("facts-behavior-08.json", g)
