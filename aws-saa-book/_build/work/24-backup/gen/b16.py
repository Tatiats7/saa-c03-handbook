import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
S3, RDS, DDB, MV, WIN = D + "s3-backups", D + "rds-backup", D + "advanced-ddb-backup", D + "multi-volume-crash-consistent", D + "windows-backups"
f = []
f.append(F("backup-s3-no-cold-storage-transition", "restriction",
 "Cold storage transition of S3 backups is not supported.",
 "Can AWS Backup move S3 backups to cold storage?",
 ["Cold storage transition of S3 backups is not supported", "S3 backups"],
 [E(S3, "Cold storage transition of S3 backups is not supported.")],
 scope="S3 backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-rds-periodic-snapshots-are-manual-backups-in-rds", "behavior",
 "Periodic snapshots created by AWS Backup are considered manual backups in Amazon RDS, while continuous backups created by AWS Backup are considered automated backups in Amazon RDS.",
 "How does RDS classify backups created by AWS Backup?",
 ["considered manual backups in Amazon RDS", "considered automated backups in Amazon RDS"],
 [E(RDS, "Periodic snapshots created by AWS Backup are considered manual backups in Amazon RDS. These are snapshot-based backups taken according to your backup plan schedule."),
  E(RDS, "Continuous backups created by AWS Backup are considered automated backups in Amazon RDS. These enable point-in-time restore (PITR) by maintaining transaction logs alongside automated snapshots.")],
 scope="RDS backups created by AWS Backup", tier0=True, bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-rds-aws-backup-creates-manual-db-snapshot-same-chain", "behavior",
 "When AWS Backup backs up an RDS instance it creates a manual DB snapshot with the create-db-snapshot operation, and all snapshots of the instance, whether automated, manual or from AWS Backup, belong to the same incremental snapshot chain.",
 "What does AWS Backup create when it backs up an RDS instance?",
 ["creates a manual DB snapshot of that instance", "same incremental snapshot chain"],
 [E(RDS, "When you use AWS Backup to create a backup (recovery point) of an Amazon RDS instance, AWS Backup creates a manual DB snapshot of that instance by using the `create-db-snapshot` operation in Amazon RDS. All snapshots of a DB instance, whether they come from Amazon RDS automated backups, manual snapshots, or AWS Backup, belong to the same incremental snapshot chain for that instance.")],
 scope="RDS instances backed up by AWS Backup", tier0=True, bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-rds-only-first-snapshot-full-later-incremental", "behavior",
 "Only the first snapshot ever taken of an RDS DB instance stores the full contents of the database; every later snapshot is incremental, so the first recovery point AWS Backup creates can also be incremental if earlier snapshots exist.",
 "Is the first AWS Backup snapshot of an RDS instance always a full snapshot?",
 ["Only the first snapshot ever taken of a DB instance stores the full contents", "is incremental, not a new full snapshot"],
 [E(RDS, "Only the first snapshot ever taken of a DB instance stores the full contents of the database. Every later snapshot of the same instance is incremental, which means it stores only the data that changed since the most recent snapshot. As a result, if the instance already has automated backups or earlier snapshots, the first recovery point that AWS Backup creates is also incremental, not a new full snapshot.")],
 scope="RDS DB instance snapshots", bullets=["4.1.K5"]))
f.append(F("backup-rds-snapshots-share-free-backup-storage-allocation", "pricing-dimension",
 "AWS Backup periodic snapshots count as manual backups toward your total RDS backup storage, alongside automated backups; RDS gives free backup storage equal to your provisioned DB instance storage for both combined, and storage beyond that is billed.",
 "Do AWS Backup snapshots of RDS use the free RDS backup storage allocation?",
 ["free backup storage allocation equal to your provisioned DB instance storage", "Storage beyond that allocation is billed"],
 [E(RDS, "AWS Backup periodic snapshots are classified as manual backups in Amazon RDS. While they share the same incremental snapshot chain as automated backups, they count toward your total backup storage alongside automated backups. Amazon RDS provides a free backup storage allocation equal to your provisioned DB instance storage — this covers both automated backups and manual snapshots combined. Storage beyond that allocation is billed.")],
 scope="RDS backup storage", tier0=True, bullets=["4.3.S1", "4.1.K5"]))
f.append(F("backup-rds-consolidated-snapshot-charged-once", "pricing-dimension",
 "When RDS consolidates an automated and a manual snapshot entry, both entries reference the same underlying snapshot data, you are charged only once for it, and retention and point-in-time restore are unaffected.",
 "Are you charged twice when RDS consolidates an AWS Backup snapshot with an automated backup?",
 ["charged only once for that single underlying snapshot", "reference the same underlying snapshot data"],
 [E(RDS, "When a backup is consolidated, both the manual and automated snapshot entries reference the same underlying snapshot data. You are charged only once for that single underlying snapshot and your data remains fully protected. Also, backup retention and point-in-time restore functionality are unaffected regardless of whether entries are consolidated.")],
 scope="RDS consolidated backups", rel="extended", bullets=["4.3.S1"]))
f.append(F("backup-rds-toggling-continuous-backups-takes-instance-offline", "restriction",
 "Enabling continuous backups for RDS through AWS Backup when they were disabled, or disabling them when they were enabled, takes the RDS instance offline to make the change; if automated backups were enabled from RDS and simply moved to AWS Backup, no downtime is required.",
 "Does turning continuous backups on or off through AWS Backup cause downtime for an RDS instance?",
 ["takes the Amazon RDS instance offline", "then no downtime is required"],
 [E(RDS, "Enabling continuous backups for Amazon RDS using AWS Backup when they were previously disabled (or disabling continuous backups when they were previously enabled) takes the Amazon RDS instance offline to make the changes. Plan this change during a maintenance window to minimize impact. If automated backups were enabled from Amazon RDS and that backup was simply moved to AWS Backup, then no downtime is required.")],
 scope="RDS instances", bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-rds-custom-oracle-outposts-local-zones-unsupported", "restriction",
 "AWS Backup does not support RDS Custom for Oracle, and does not support backup and restore of RDS on Outposts or in Local Zones.",
 "Which RDS deployments can AWS Backup not back up?",
 ["RDS Custom for Oracle is not currently supported by AWS Backup", "RDS on Outposts or in Local Zones"],
 [E(RDS, "RDS Custom for Oracle is not currently supported by AWS Backup."),
  E(RDS, "AWS Backup does not support backup and restore of RDS on Outposts or in Local Zones, including Dedicated Local Zones.")],
 scope="Amazon RDS deployments", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-rds-multi-az-mysql-postgres-one-primary-two-standbys", "capability",
 "AWS Backup backs up and supports Amazon RDS for MySQL and for PostgreSQL Multi-AZ deployment options with one primary and two readable standby database instances.",
 "Which RDS Multi-AZ deployment does AWS Backup support?",
 ["MySQL and for PostgreSQL Multi-AZ", "one primary and two readable standby database instances"],
 [E(RDS, "AWS Backup backs up and supports Amazon RDS for MySQL and for PostgreSQL Multi-AZ (Availability Zone) deployment options with one primary and two readable standby database instances.")],
 scope="RDS Multi-AZ DB clusters", rel="extended", bullets=["4.1.S6"]))
# DDB advanced
f.append(F("backup-ddb-advanced-default-for-customers-without-vault-before-2021-11-21", "default",
 "Advanced DynamoDB backup features are enabled by default for customers who started using AWS Backup after November 2021, specifically those who had not created a backup vault before November 21, 2021.",
 "Which customers have the advanced DynamoDB backup features on by default?",
 ["not created a backup vault prior to November 21, 2021", "after November 2021"],
 [E(DDB, "Customers who started using AWS Backup after November 2021 have advanced DynamoDB backup features enabled by default. Specifically, advanced DynamoDB backup features are enabled by default to customers who have not created a backup vault prior to November 21, 2021.")],
 scope="AWS Backup customers", dm="default", adj=True, tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-ddb-advanced-benefits-cold-copy-tags", "capability",
 "With the advanced features enabled, new DynamoDB backups can use cold storage tiering, cost allocation tags, cross-Region and cross-account copy, and inherit tags from their source tables for permissions and service control policies.",
 "What do the advanced DynamoDB backup features unlock?",
 ["Backups inherit tags from their source DynamoDB tables", "service control policies (SCPs)"],
 [E(DDB, "After you enable AWS Backup's advanced features in your AWS Region, you unlock the following features for all new for DynamoDB table backups you create:"),
  E(DDB, "Backups inherit tags from their source DynamoDB tables, allowing you to use those tags to set permissions and service control policies (SCPs).")],
 scope="DynamoDB backups, per Region", cond="advanced features enabled in the Region; applies to new backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-ddb-advanced-opt-in-by-plan-or-on-demand-automatic-policy-manual", "behavior",
 "Backups created by a backup plan or on demand automatically opt your account in to advanced DynamoDB backups, but if the backup job is created by a backup policy you must opt in manually, in the console or the CLI.",
 "How does an account opt in to advanced DynamoDB backups?",
 ["automatically opt-in your account", "manually opt-in to Advanced DynamoDB backups"],
 [E(DDB, "Backups created by a plan or on-demand will automatically opt-in your account to allow backups of Advanced DDB resources."),
  E(DDB, "If your backup job is created by a backup policy, you need to manually opt-in to Advanced DynamoDB backups, either through the Backup console or through CLI.")],
 scope="DynamoDB advanced backup opt-in", rel="extended", bullets=["4.1.S6", "1.3.S1"]))
f.append(F("backup-ddb-advanced-does-not-replace-native-pitr", "behavior",
 "AWS Backup advanced DynamoDB features give periodic snapshot-based backups and do not replace or duplicate native DynamoDB point-in-time recovery, which gives continuous backup; if you enable both you are charged for both.",
 "Does enabling advanced DynamoDB backup replace native DynamoDB PITR, and what does running both cost?",
 ["do not replace or duplicate native DynamoDB point-in-time recovery", "you will incur charges for both"],
 [E(DDB, "AWS Backup advanced DynamoDB features provide periodic snapshot-based backups with additional capabilities. These do not replace or duplicate native DynamoDB point-in-time recovery (PITR), which provides continuous backup with second-level granularity. If your recovery strategy requires both periodic snapshots (for long-term retention, cross-Region DR, or compliance) and continuous recovery (for operational recovery within a short window), you may choose to enable both AWS Backup advanced features and native DynamoDB PITR. In this case, you will incur charges for both — this is intentional complementary protection, not unintended duplication.")],
 scope="DynamoDB backups", tier0=True, bullets=["4.1.K5", "4.3.S1", "1.3.S5"]))
# EBS / EC2
f.append(F("backup-ebs-role-that-created-snapshot-must-delete-or-archive", "restriction",
 "The IAM role used to create an EBS snapshot recovery point is associated with that snapshot, and the same role must be used to delete those recovery points or transition them to an archive tier.",
 "Which role is needed to delete or archive an EBS recovery point created by AWS Backup?",
 ["associated with that snapshot", "must be used to delete recovery points created by it"],
 [E(MV, "The role used to create an EBS snapshot recovery point is associated with that snapshot. This same role must be used to delete recovery points created by it or to transition recovery points of it to an archive tier.")],
 scope="EBS snapshot recovery points", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-ebs-supports-cold-storage-archive-tier", "capability",
 "Amazon EBS is one of the resources that supports a transition of backups to cold storage, through the EBS Snapshots Archive tier.",
 "Can AWS Backup move EBS backups to cold storage?",
 ["supports a transition of backups to cold storage", "Amazon EBS Archive Tier"],
 [E(MV, "EBS is one of the resource that supports a transition of backups to cold storage.")],
 scope="EBS backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-windows-vss-application-consistent-ec2-only", "capability",
 "AWS Backup can back up and restore VSS-enabled Windows applications on EC2 instances, creating a snapshot that is consistent for the application if it has a VSS writer registered with Windows VSS; application-consistent backups are supported only for resources running on EC2.",
 "Can AWS Backup take application-consistent backups of Windows applications?",
 ["VSS writer registered with Windows VSS", "only supports application-consistent backups of resources running on Amazon EC2"],
 [E(WIN, "If the application has VSS writer registered with Windows VSS, then AWS Backup creates a snapshot that will be consistent for that application."),
  E(WIN, "AWS Backup only supports application-consistent backups of resources running on Amazon EC2, specifically backup scenarios where application data can be restored by replacing an existing instance with a new instance created from the backup. Not all instance types or applications are supported for Windows VSS backups.")],
 scope="Windows VSS backups on EC2", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-windows-vss-ssm-agent-required", "restriction",
 "For Windows VSS backups, you must download, install and configure the SSM agent in AWS Systems Manager; this step is required.",
 "What must be installed to take Windows VSS backups with AWS Backup?",
 ["This step is required", "SSM agent in AWS Systems Manager"],
 [E(WIN, "Download, install, and configure the SSM agent in AWS Systems Manager. This step is required.")],
 scope="Windows VSS backups on EC2", rel="extended", bullets=["4.1.S6"]))
dump("facts-behavior-16.json", f)
