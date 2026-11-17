import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
RP, VA, P, WS, CP = D + "recovery-points", D + "vaults", D + "plan-options-and-configuration", D + "working-with-supported-services", D + "creating-a-backup-plan"
f = []
f.append(F("backup-recovery-point-is-backup-at-specified-time", "behavior",
 "A backup, or recovery point, represents the content of a resource such as an EBS volume or DynamoDB table at a specified time; the terms recovery point and backup are used interchangeably.",
 "What is a recovery point in AWS Backup?",
 ["represents the content of a resource", "used interchangeably"],
 [E(RP, "A backup, or recovery point, represents the content of a resource, such as an Amazon Elastic Block Store (Amazon EBS) volume or Amazon DynamoDB table, at a specified time. Recovery point is a term that refers generally to the different backups in AWS services, such as Amazon EBS snapshots and DynamoDB backups. The terms recovery point and backup are used interchangeably.")],
 scope="AWS Backup recovery points", hard=False, tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-recovery-points-saved-in-vaults", "behavior",
 "AWS Backup saves recovery points in backup vaults, which you can organize according to your business needs.",
 "Where does AWS Backup save recovery points?",
 ["saves recovery points in backup vaults", "organize according to your business needs"],
 [E(RP, "AWS Backup saves recovery points in backup vaults, which you can organize according to your business needs.")],
 scope="AWS Backup vaults", hard=False, bullets=["4.1.K5", "2.2.S5"]))
f.append(F("backup-vault-container-and-key-for-some-backups", "behavior",
 "A backup vault is a container that stores and organizes your backups, and when you create it you must specify the KMS key that encrypts some of the backups in it, while the encryption of other backups is managed by their source services.",
 "What is a backup vault and does its KMS key encrypt every backup?",
 ["a container that stores and organizes your backups", "Encryption for other backups is managed by their source AWS services"],
 [E(VA, "In AWS Backup, a backup vault is a container that stores and organizes your backups."),
  E(VA, "When creating a backup vault, you must specify the AWS Key Management Service (AWS KMS) encryption key that encrypts some of the backups placed in this vault. Encryption for other backups is managed by their source AWS services.")],
 scope="AWS Backup vaults", tier0=True, bullets=["4.1.K5", "2.2.S5"]))
f.append(F("backup-plan-composed-of-one-or-more-backup-rules", "behavior",
 "A backup plan is composed of one or more backup rules.",
 "What is a backup plan made of?",
 ["composed of one or more backup rules", "Backup plans"],
 [E(P, "Backup plans are composed of one or more backup rules.")],
 scope="backup plans", hard=False, bullets=["4.1.K5"]))
f.append(F("backup-window-jobs-start-within-window", "behavior",
 "A backup window consists of the time the window begins and its duration in hours, and backup jobs are started within this window.",
 "What does the backup window control?",
 ["Backup jobs are started within this window", "duration of the window in hours"],
 [E(P, "Backup windows consist of the time that the backup window begins and the duration of the window in hours. Backup jobs are started within this window.")],
 scope="backup rules", bullets=["4.1.S6"]))
f.append(F("backup-sap-hana-on-ec2-via-backint", "capability",
 "AWS Backup works with AWS Backint to support SAP HANA database backup and restore on Amazon EC2 instances.",
 "How does AWS Backup protect SAP HANA on EC2?",
 ["AWS Backint to support SAP HANA database backup and restore", "on Amazon EC2 instances"],
 [E(WS, "AWS Backup works with AWS Backint to support SAP HANA database backup and restore on Amazon EC2 instances.")],
 scope="SAP HANA on EC2", rel="extended", bullets=["4.1.S6"]))
dump("facts-behavior-27.json", f)
