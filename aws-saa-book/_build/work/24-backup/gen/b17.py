import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
RDS, DDB, MV = D + "rds-backup", D + "advanced-ddb-backup", D + "multi-volume-crash-consistent"
f = []
f.append(F("backup-rds-only-first-snapshot-full-later-incremental", "behavior",
 "Only the first snapshot ever taken of an RDS DB instance stores the full contents of the database; every later snapshot is incremental, so the first recovery point AWS Backup creates can also be incremental if earlier snapshots exist.",
 "Is the first AWS Backup snapshot of an RDS instance always a full snapshot?",
 ["Only the first snapshot ever taken of a DB instance stores the full contents", "also incremental, not a new full snapshot"],
 [E(RDS, "Only the first snapshot ever taken of a DB instance stores the full contents of the database. Every later snapshot of the same instance is incremental, which means it stores only the data that changed since the most recent snapshot. As a result, if the instance already has automated backups or earlier snapshots, the first recovery point that AWS Backup creates is also incremental, not a new full snapshot.")],
 scope="RDS DB instance snapshots", bullets=["4.1.K5"]))
f.append(F("backup-ddb-advanced-does-not-replace-native-pitr", "behavior",
 "AWS Backup advanced DynamoDB features give periodic snapshot-based backups and do not replace or duplicate native DynamoDB point-in-time recovery, which gives continuous backup; if you enable both, you are charged for both.",
 "Does enabling advanced DynamoDB backup replace native DynamoDB PITR, and what does running both cost?",
 ["do not replace or duplicate native DynamoDB point-in-time recovery", "you will incur charges for both"],
 [E(DDB, "AWS Backup advanced DynamoDB features provide periodic snapshot-based backups with additional capabilities. These do not replace or duplicate native DynamoDB point-in-time recovery (PITR), which provides continuous backup with second-level granularity."),
  E(DDB, "In this case, you will incur charges for both — this is intentional complementary protection, not unintended duplication.")],
 scope="DynamoDB backups", tier0=True, bullets=["4.1.K5", "4.3.S1", "1.3.S5"]))
f.append(F("backup-ebs-supports-cold-storage-archive-tier", "capability",
 "Amazon EBS is one of the resources that supports a transition of backups to cold storage, through the EBS Snapshots Archive tier.",
 "Can AWS Backup move EBS backups to cold storage?",
 ["supports a transition of backups to cold storage", "EBS is one of the resource"],
 [E(MV, "EBS is one of the resource that supports a transition of backups to cold storage.")],
 scope="EBS backups", tier0=True, bullets=["4.1.S6", "4.3.S1"]))
dump("facts-behavior-17.json", f)
