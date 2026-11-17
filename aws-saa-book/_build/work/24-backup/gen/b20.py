import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
FA = D + "backup-feature-availability"
f = []
rows = [
 ("ec2", 0, "In the feature availability by resource table, the Amazon EC2 row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, restore testing, logically air-gapped vault and malware protection, and no check mark for continuous backup, full management, lifecycle to cold storage, item-level restore, backup search or backup tiering.",
  "Which AWS Backup features does Amazon EC2 support?", ["Amazon EC2", "Lifecycle to cold storage"], True),
 ("s3", 1, "In the feature availability by resource table, the Amazon S3 row has check marks for every feature column except lifecycle to cold storage, including continuous backup and point-in-time restore, full management, backup search and backup tiering.",
  "Which AWS Backup features does Amazon S3 support?", ["Amazon S3", "Lifecycle to cold storage"], True),
 ("ebs", 2, "In the feature availability by resource table, the Amazon EBS row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, lifecycle to cold storage, item-level restore, restore testing, logically air-gapped vault, backup search and malware protection, and no check mark for continuous backup, full management or backup tiering.",
  "Which AWS Backup features does Amazon EBS support?", ["Amazon EBS", "Lifecycle to cold storage"], True),
 ("rds-instance", 3, "In the feature availability by resource table, the Amazon RDS DB instance row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, and restore testing, and no check mark for full management, lifecycle to cold storage or logically air-gapped vault.",
  "Which AWS Backup features does an Amazon RDS DB instance support?", ["Amazon RDS DB instance", "Continuous backup and point-in-time restore"], True),
 ("aurora", 5, "In the feature availability by resource table, the Amazon Aurora row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, restore testing and logically air-gapped vault, and no check mark for full management, lifecycle to cold storage, item-level restore or backup search.",
  "Which AWS Backup features does Amazon Aurora support, and can Aurora backups move to cold storage?", ["Amazon Aurora", "Lifecycle to cold storage"], True),
 ("efs", 7, "In the feature availability by resource table, the Amazon EFS row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, full management, lifecycle to cold storage, item-level restore, restore testing and logically air-gapped vault, and no check mark for continuous backup.",
  "Which AWS Backup features does Amazon EFS support?", ["Amazon EFS", "Lifecycle to cold storage"], True),
 ("dynamodb", 20, "In the feature availability by resource table, the Amazon DynamoDB row (without advanced features) has check marks only for AWS Backup Audit Manager and restore testing, and no check mark for cross-Region backup, cross-account backup, full management or lifecycle to cold storage.",
  "Which AWS Backup features does DynamoDB support without the advanced features?", ["Amazon DynamoDB", "Lifecycle to cold storage"], True),
 ("dynamodb-advanced", 21, "In the feature availability by resource table, the DynamoDB with advanced features row has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, full management, lifecycle to cold storage, restore testing and logically air-gapped vault, and no check mark for incremental backup or continuous backup.",
  "Which AWS Backup features does DynamoDB support once advanced features are enabled?", ["DynamoDB with", "Lifecycle to cold storage"], True),
]
for fid, r, claim, q, d, t0 in rows:
    f.append(F("backup-feature-row-" + fid, "capability", claim, q, d, [ROW(FA, 0, r)],
     scope="feature availability by resource", tier0=t0, bullets=["4.1.S6", "4.3.S1"], vol="frequently-changing"))
f.append(F("backup-copy-footnote-rds-aurora-docdb-neptune-single-action-copy", "capability",
 "Amazon RDS, Aurora, DocumentDB and Neptune support cross-Region and cross-account snapshot copying in a single action.",
 "Can RDS and Aurora snapshots be copied across Region and account in one action?",
 ["cross-Region and cross-account snapshot copying in a single action", "Amazon RDS, Aurora, DocumentDB, and Neptune"],
 [E(FA, "Amazon RDS, Aurora, DocumentDB, and Neptune now support cross-Region and cross-account snapshot copying in a single action.")],
 scope="RDS, Aurora, DocumentDB, Neptune snapshots", bullets=["1.3.S5"], vol="frequently-changing"))
f.append(F("backup-copy-footnote-rds-multi-az-clusters-no-copy", "restriction",
 "RDS Multi-AZ database instances can be copied, but Multi-AZ clusters do not currently support any copy operations.",
 "Can an RDS Multi-AZ cluster backup be copied to another Region or account?",
 ["Multi-AZ clusters do not currently support any copy operations", "Multi-AZ"],
 [E(FA, "RDS multi availability zone (Multi-AZ) database instances can be copied, but Multi-AZ clusters do not currently support any copy operations.")],
 scope="RDS Multi-AZ", tier0=True, bullets=["1.3.S5"], vol="frequently-changing"))
f.append(F("backup-copy-from-incremental-rds-s3-from-full-aurora-sap", "behavior",
 "Amazon RDS and Amazon S3 support cross-account and cross-Region copy from incremental backups, while Amazon Aurora and SAP HANA on EC2 support cross-account and cross-Region copy from full backups.",
 "Are cross-Region copies of RDS and Aurora backups incremental or full?",
 ["support cross-account and cross-Region copy from incremental backups", "support cross-account and cross-Region copy from full backups"],
 [E(FA, "Amazon RDS and Amazon S3 support cross-account and cross-Region copy from incremental backups. Amazon RDS also supports simultaneous cross-Region and cross-account snapshot copying in a single action."),
  E(FA, "Amazon Aurora and SAP HANA on Amazon EC2 instances support cross-account and cross-Region copy from full backups. Amazon Aurora also supports simultaneous cross-Region and cross-account snapshot copying in a single action.")],
 scope="copy of RDS, S3, Aurora and SAP HANA backups", rel="extended", bullets=["1.3.S5"], vol="frequently-changing"))
f.append(F("backup-feature-support-not-assumed-unless-stated", "behavior",
 "AWS Backup offers a set of features for all supported resources, and support for any other feature or service should not be assumed unless explicitly mentioned.",
 "Can you assume a backup feature works for every resource type?",
 ["Support for a feature or service should not be assumed", "unless explicitly mentioned"],
 [E(FA, "AWS Backup offers the following features for its supported AWS services, as well as for supported third-party applications. Support for a feature or service should not be assumed unless explicitly mentioned.")],
 scope="AWS Backup features", hard=True, bullets=["4.1.S6"]))
dump("facts-behavior-20.json", f)
