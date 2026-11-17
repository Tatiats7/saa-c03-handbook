import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
FA, L, W, PB, V = D + "backup-feature-availability", D + "logicallyairgappedvault", D + "whatisbackup", D + "lag-vault-primary-backup", D + "create-a-vault"
f = []
f.append(F("backup-lag-primary-backup-no-direct-cross-account-or-region", "restriction",
 "You cannot create backups directly into a logically air-gapped vault cross-account or cross-Region; AWS Backup recommends a logically air-gapped vault in the same Region for faster recovery without a copy.",
 "Can a primary backup be created directly in a logically air-gapped vault in another account or Region?",
 ["cannot create backups directly cross-account or cross-Region", "in the same Region"],
 [E(PB, "You cannot create backups directly cross-account or cross-Region. We recommend backing up to a logically air-gapped vault in the same Region to enable faster recovery without requiring a copy."),
  E(PB, "The logically air-gapped vault must be in the same account and Region as your backup vault.")],
 scope="logically air-gapped vault primary backup", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
# LAG compare table rows
f.append(F("backup-lag-vs-standard-restore-row", "behavior",
 "A standard backup vault's backups can be restored only by the account that owns the vault, while backups in a logically air-gapped vault can be restored by a different account if the vault is shared with it.",
 "Which accounts can restore from a standard vault and from a logically air-gapped vault?",
 ["restored by the same account to which the vault belongs", "restored by a different account"],
 [ROW(L, 0, 4)], scope="standard backup vault versus logically air-gapped vault", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vs-standard-security-row", "behavior",
 "A logically air-gapped vault is always locked with a vault lock in compliance mode and encrypts with an AWS owned key or a customer managed key, while a standard vault can optionally use a vault lock in compliance or governance mode.",
 "How do the security features of a standard vault and a logically air-gapped vault differ?",
 ["Is always locked with a vault lock in compliance mode", "optionally use a vault lock in compliance or governance mode"],
 [ROW(L, 0, 5)], scope="standard backup vault versus logically air-gapped vault", tier0=True, bullets=["2.2.S5", "1.3.S1"], vol="frequently-changing"))
f.append(F("backup-lag-vs-standard-sharing-row", "behavior",
 "A standard backup vault is not compatible with AWS RAM and its access is managed through policies and AWS Organizations, while a logically air-gapped vault can optionally be shared across accounts using AWS RAM.",
 "Which vault type can be shared with AWS RAM?",
 ["Not compatible with AWS RAM", "optionally be shared across accounts using AWS RAM"],
 [ROW(L, 0, 6)], scope="standard backup vault versus logically air-gapped vault", tier0=True, bullets=["2.2.S5"], vol="frequently-changing"))
f.append(F("backup-lag-vs-standard-billing-row", "pricing-dimension",
 "All storage and data transfer charges of a logically air-gapped vault occur under AWS Backup, while for a standard vault the charges of resource types fully managed by AWS Backup occur under AWS Backup and other resource types are billed under their own services.",
 "Under which service do logically air-gapped vault charges appear on the bill?",
 ["All billing charges from these vaults", "occur under \"AWS Backup\""],
 [ROW(L, 0, 1)], scope="standard backup vault versus logically air-gapped vault", bullets=["4.3.S1"], vol="frequently-changing"))
# whatisbackup resource rows
for fid, row, claim, q, d in [
 ("ec2", 0, "AWS Backup supports Amazon EC2 instances that are backed by Amazon EBS volumes.", "Which EC2 instances can AWS Backup back up?", ["Amazon EC2 instances backed by Amazon EBS volumes", "Amazon Elastic Compute Cloud (Amazon EC2)"]),
 ("s3", 1, "AWS Backup supports Amazon S3 data.", "Does AWS Backup support Amazon S3?", ["Amazon S3 data", "Amazon Simple Storage Service (Amazon S3)"]),
 ("ebs", 2, "AWS Backup supports Amazon EBS volumes.", "Does AWS Backup support Amazon EBS volumes?", ["Amazon EBS volumes", "Amazon Elastic Block Store (Amazon EBS)"]),
 ("dynamodb", 3, "AWS Backup supports Amazon DynamoDB tables.", "Does AWS Backup support DynamoDB tables?", ["Amazon DynamoDB tables", "Amazon DynamoDB"]),
 ("rds", 4, "AWS Backup supports Amazon RDS database instances of all database engines and Multi-Availability Zone clusters.", "Which RDS resources does AWS Backup support?", ["including all database engines", "Multi-Availability Zone clusters"]),
 ("aurora", 6, "AWS Backup supports Amazon Aurora clusters.", "Does AWS Backup support Aurora?", ["Aurora clusters", "Amazon Aurora"]),
 ("efs", 7, "AWS Backup supports Amazon EFS file systems.", "Does AWS Backup support Amazon EFS?", ["Amazon EFS file systems", "Amazon Elastic File System (Amazon EFS)"]),
]:
    f.append(F("backup-supported-resource-" + fid, "capability", claim, q, d, [ROW(W, 0, row)],
     scope="supported resource types", tier0=(fid in ("ec2", "aurora", "dynamodb", "efs", "ebs")), bullets=["4.1.S6"]))
dump("facts-behavior-06.json", f)
