import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
S3, S3R, RDS, DDB, MV, WIN = D + "s3-backups", D + "restoring-s3", D + "rds-backup", D + "advanced-ddb-backup", D + "multi-volume-crash-consistent", D + "windows-backups"
f = []
# S3
f.append(F("backup-s3-single-backup-policy-central-encrypted-vault", "capability",
 "You can use a single backup policy in AWS Backup to centrally automate backups of your application data, and AWS Backup organizes backups across AWS services and third-party applications in one centralized, encrypted backup vault.",
 "Can one backup policy cover several services and keep their backups in one place?",
 ["use a single backup policy in AWS Backup to centrally automate", "one centralized, encrypted location"],
 [E(S3, "You can use a single backup policy in AWS Backup to centrally automate the creation of backups of your application data. AWS Backup automatically organizes backups across different AWS services and third-party applications in one centralized, encrypted location (known as a backup vault) so that you can manage backups of your entire application through a centralized experience.")],
 scope="AWS Backup central backup policies", tier0=True, bullets=["4.3.S1", "1.3.S1"]))
f.append(F("backup-s3-requires-versioning-enabled", "restriction",
 "You must enable S3 Versioning on an S3 bucket to use AWS Backup for Amazon S3.",
 "What must be enabled on an S3 bucket before AWS Backup can back it up?",
 ["must enable S3 Versioning on your S3 bucket", "to use AWS Backup for Amazon S3"],
 [E(S3, "You must enable S3 Versioning on your S3 bucket to use AWS Backup for Amazon S3.")],
 scope="S3 buckets backed up by AWS Backup", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-s3-recommend-lifecycle-expiration-for-versions", "behavior",
 "AWS recommends setting a lifecycle expiration period for your S3 versions, because the recovery point stores all objects and versions in the bucket and storage cost is calculated for all objects in the backup, including objects scheduled for deletion.",
 "Why set an S3 lifecycle expiration for object versions when using AWS Backup?",
 ["set a lifecycle expiration period for your S3 versions", "including objects scheduled for deletion"],
 [E(S3, "We recommend that you set a lifecycle expiration period for your S3 versions."),
  E(S3, "All objects (including all versions) in the bucket when the backup begins will be stored in the recovery point (completed backup). These can include the current version of each object, older versions, delete markers, and objects pending lifecycle actions."),
  E(S3, "The storage cost will be calculated for all objects in the backup, including objects scheduled for deletion (objects that will expire).")],
 scope="S3 backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-s3-backup-types-object-data-tags-acls-metadata", "behavior",
 "AWS Backup backs up S3 buckets including object data, tags, access control lists (ACLs) and user-defined metadata, as continuous backups or periodic backups.",
 "What does an AWS Backup S3 backup include and which backup types exist?",
 ["object data, tags, Access Control Lists (ACLs), and user-defined metadata", "Continuous backups"],
 [E(S3, "With AWS Backup, you can create the following types of backups of your S3 buckets, including object data, tags, Access Control Lists (ACLs), and user-defined metadata:")],
 scope="S3 backups", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-s3-continuous-pitr-last-35-days-one-plan", "behavior",
 "S3 continuous backups let you restore to any point in time within the last 35 days, and continuous backups for an S3 bucket should be configured in only one backup plan.",
 "How far back can an S3 continuous backup restore, and in how many plans should it be configured?",
 ["restore to any point in time within the last 35 days", "only be configured in one backup plan"],
 [E(S3, "Continuous backups allow you to restore to any point in time within the last 35 days. Continuous backups for an S3 bucket should only be configured in one backup plan.")],
 scope="S3 continuous backups", dm="max", tier0=True, bullets=["4.1.S6", "1.3.S5"]))
f.append(F("backup-s3-continuous-and-periodic-same-vault", "restriction",
 "Continuous and periodic backups of S3 buckets must both reside in the same backup vault.",
 "Can the continuous and periodic backups of one S3 bucket be in different vaults?",
 ["must both reside in the same backup vault", "Continuous and periodic backups of S3 buckets"],
 [E(S3, "Continuous and periodic backups of S3 buckets must both reside in the same backup vault.")],
 scope="S3 backups", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-s3-first-full-then-object-level-incremental", "behavior",
 "For both S3 backup types, the first backup is a full backup and subsequent backups are incremental at object level.",
 "Are S3 backups full or incremental?",
 ["the first backup is a full backup", "incremental at object-level"],
 [E(S3, "For both backup types, the first backup is a full backup, while subsequent backups are incremental at object-level.")],
 scope="S3 backups", bullets=["4.1.S6", "4.1.K5"]))
f.append(F("backup-s3-eventbridge-disabled-failure-is-silent", "restriction",
 "If the bucket-level Amazon EventBridge notification setting is disabled, S3 stops publishing object-level events and the AWS Backup managed rule receives none; the failure is silent, with no notification, alert or backup job failure from AWS Backup.",
 "What happens, and is anything reported, if EventBridge notifications are disabled on a bucket under continuous backup?",
 ["This failure is silent", "no notification, alert, or backup job failure is generated by AWS Backup"],
 [E(S3, "If the bucket-level Amazon EventBridge notification setting is disabled, S3 stops publishing object-level events. The AWS Backup-managed Amazon EventBridge rule remains enabled but receives no events for that bucket. This failure is silent – no notification, alert, or backup job failure is generated by AWS Backup.")],
 scope="S3 continuous backups", tier0=True, bullets=["4.1.S6", "1.3.S5"]))
f.append(F("backup-s3-no-cold-storage-transition", "restriction",
 "Cold storage transition of S3 backups is not supported; you use the AWS Backup lifecycle policy to define when the backup expires.",
 "Can AWS Backup move S3 backups to cold storage?",
 ["Cold storage transition of S3 backups is not supported", "Use AWS Backup lifecycle management policy"],
 [E(S3, "Use AWS Backup lifecycle management policy to define the timeline for backup expiration. Cold storage transition of S3 backups is not supported.")],
 scope="S3 backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-s3-only-resource-with-backup-tiering", "capability",
 "Amazon S3 is the only resource that supports backup tiering to a lower cost warm storage tier.",
 "Which resource supports backup tiering to a lower-cost warm storage tier?",
 ["the only resource that supports backup tiering", "lower cost warm storage tier"],
 [E(S3, "Amazon S3 is the only resource that supports backup tiering to a lower cost warm storage tier.")],
 scope="backup tiering", tier0=True, bullets=["4.1.S6", "4.3.S1"], vol="frequently-changing"))
f.append(F("backup-s3-no-sse-c-no-bucket-config-no-outposts", "restriction",
 "AWS Backup does not support backups of SSE-C-encrypted S3 objects, of bucket configurations such as bucket policies, settings, names or access points, or of S3 on AWS Outposts.",
 "Which S3 content can AWS Backup not back up?",
 ["does not offer support for backups of SSE-C-encrypted objects", "backups of bucket configurations"],
 [E(S3, "AWS Backup does not offer support for backups of SSE-C-encrypted objects. AWS Backup also does not support backups of bucket configurations, including bucket policies, settings, names, or access points."),
  E(S3, "AWS Backup does not support backups of S3 on AWS Outposts.")],
 scope="S3 backups", bullets=["4.1.S6"]))
f.append(F("backup-s3-general-purpose-buckets-only-no-directory-buckets", "restriction",
 "AWS Backup supports backup and restore of general purpose S3 buckets; directory buckets are not supported.",
 "Does AWS Backup back up S3 directory buckets?",
 ["general purpose S3 buckets", "Directory buckets are not supported"],
 [E(S3, "AWS Backup supports backup and restore of general purpose S3 buckets. Directory buckets are not supported at this time.")],
 scope="S3 bucket types", bullets=["4.1.S6"]))
f.append(F("backup-s3-glacier-archive-classes-not-supported", "restriction",
 "The archived storage classes S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are not supported for AWS Backup S3 backups.",
 "Can AWS Backup back up S3 objects in Glacier Deep Archive?",
 ["S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are not supported", "archived storage classes"],
 [E(S3, "The archived storage classes S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are not supported.")],
 scope="S3 storage classes", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-s3-kms-decrypt-then-reencrypt-with-vault-key", "behavior",
 "To back up SSE-KMS encrypted S3 objects, AWS Backup first decrypts the data using the source KMS key and then re-encrypts it using the backup vault's KMS key.",
 "How does AWS Backup handle S3 objects encrypted with a KMS key?",
 ["decrypt the data using the source KMS key", "re-encrypt it using the backup vault's KMS key"],
 [E(S3, "To achieve this, AWS Backup must first decrypt the data using the source KMS key, then re-encrypt it using the backup vault's KMS key.")],
 scope="S3 backups of SSE-KMS objects", rel="extended", bullets=["1.3.S1", "4.1.S6"]))
f.append(F("backup-s3-copies-available-copies-of-continuous-no-pitr", "behavior",
 "Cross-account and cross-Region copies are available for S3 backups, but copies of continuous backups do not have point-in-time restore capabilities.",
 "Can you do a point-in-time restore from a copy of an S3 continuous backup?",
 ["copies of continuous backups do not have point-in-time restore capabilities", "Cross-account and cross-Region copies are available"],
 [E(S3, "Cross-account and cross-Region copies are available for S3 backups, but copies of continuous backups do not have point-in-time restore capabilities.")],
 scope="S3 backup copies", bullets=["1.3.S5", "4.1.S6"]))
f.append(F("backup-s3-access-points-direct-access-without-restore", "capability",
 "AWS Backup lets you access S3 backup data directly through S3 access points, without initiating a restore.",
 "Can you read S3 backup data without restoring it?",
 ["access S3 backup data directly through S3 access points", "without initiating a restore"],
 [E(S3, "AWS Backup lets you access S3 backup data directly through S3 access points, without initiating a restore.")],
 scope="S3 backups", rel="reference", bullets=["4.1.S6"], vol="frequently-changing",
 note="not examinable yet: access points for S3 backups were announced 2026-08-06, after the 2026-07-15 cut-off"))
f.append(F("backup-s3-restore-to-standard-all-or-specific-objects-existing-or-new-bucket", "capability",
 "You can restore S3 data backed up with AWS Backup to the S3 Standard storage class, restoring all objects in a bucket or specific objects, into an existing or a new bucket.",
 "What can you restore from an S3 backup, and where?",
 ["all the objects in a bucket or specific objects", "an existing or new bucket"],
 [E(S3R, "You can restore the S3 data that you backed up using AWS Backup to the S3 Standard storage class. You can restore all the objects in a bucket or specific objects. You can restore them to an existing or new bucket.")],
 scope="S3 restores", tier0=True, bullets=["4.1.S6", "1.3.K2"]))
f.append(F("backup-s3-restore-latest-version-only-by-default", "default",
 "By default AWS Backup restores only the latest version of your S3 objects; you can choose to restore additional or all versions.",
 "Which object versions does an S3 restore bring back by default?",
 ["restores only the latest version of your objects", "restore additional or all versions"],
 [E(S3R, "By default, AWS Backup restores only the latest version of your objects. You have the choice to restore additional or all versions of the objects.")],
 scope="S3 restores", dm="default", adj=True, bullets=["4.1.S6", "1.3.K2"]))
f.append(F("backup-s3-restore-not-destructive-existing-objects-skipped", "restriction",
 "When restoring to the original S3 bucket, AWS Backup does not perform a destructive restore: it will not replace an object that already exists, regardless of version, and restores are skipped if the destination has an object with the same name or version ID.",
 "Does an S3 restore overwrite existing objects in the bucket?",
 ["does not perform a destructive restore", "same name or version ID"],
 [E(S3R, "AWS Backup does not perform a destructive restore, which means AWS Backup will not put an object into a bucket in place of an object that already exists, regardless of version."),
  E(S3R, "Restores of objects are skipped if the destination bucket has an object with the same name or version ID.")],
 scope="S3 restores", tier0=True, bullets=["1.3.K2", "4.1.S6"]))
f.append(F("backup-s3-restore-cross-region-copy-restores-in-copy-region", "restriction",
 "While S3 backups can be copied cross-Region, restore jobs occur only in the same Region in which the original backup or copy is located.",
 "Can you restore an S3 backup copy into a different Region than the copy?",
 ["restore jobs only occur in the same Region", "original backup or copy is located"],
 [E(S3R, "While S3 backups can be copied cross-Region, restore jobs only occur in the same Region in which the original backup or copy is located.")],
 scope="S3 restores", rel="extended", bullets=["1.3.S5", "1.3.K2"]))
dump("facts-behavior-15.json", f)
