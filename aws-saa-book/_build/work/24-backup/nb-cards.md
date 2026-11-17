facts card: 19 facts
ebs-aws-backup-multi-volume-crash-consistent
  claim: For EBS, AWS Backup takes crash-consistent, multi-volume snapshots that coordinate point-in-time backups of all volumes attached to an EC2 instance.
  scope: per EC2 instance.
  link: [crash-consistent, multi-volume snapshots](../facts/ebs.md#ebs-aws-backup-multi-volume-crash-consistent)
rds-backup-aws-backup-not-in-snapshot-quota
  claim: Backups managed by AWS Backup are considered manual DB snapshots but don't count toward the manual snapshot quota.
  scope: per account, per Region; default; not adjustable.
  link: [don't count toward the manual snapshot quota](../facts/rds.md#rds-backup-aws-backup-not-in-snapshot-quota)
  say: they don't count toward the manual snapshot quota
rds-aws-backup-manual-snapshots-no-quota
  claim: You can manage RDS backups in AWS Backup; backups managed by AWS Backup count as manual DB snapshots but do not count toward the RDS DB snapshot quota.
  scope: RDS automated backups and snapshots.
  link: [considered manual DB snapshots](../facts/rds.md#rds-aws-backup-manual-snapshots-no-quota)
  link: [don't count toward the DB snapshot quota](../facts/rds.md#rds-aws-backup-manual-snapshots-no-quota)
organizations-backup-policy-effective-plan-immutable
  claim: Backup policies centrally apply AWS Backup plans to resources across the organization's accounts; the effective backup plan appears in each account as an immutable plan that can be viewed but not changed.
  scope: backup policies.
  link: [centrally manage and apply backup plans](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
  link: [as an immutable plan for that account](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
  link: [You can view it, but not change it](../facts/organizations.md#organizations-backup-policy-effective-plan-immutable)
control-tower-change-backup-integration-2024-11
  claim: On 2024-11-25 AWS Control Tower integrated with AWS Backup, so you can set up plans to back up your AWS Control Tower resources.
  scope: per landing zone.
  link: [2024-11-25](../facts/control-tower.md#control-tower-change-backup-integration-2024-11)
  link: [integrates with AWS Backup](../facts/control-tower.md#control-tower-change-backup-integration-2024-11)
  say: November twenty-fifth, twenty twenty-four | integrates with AWS Backup
well-architected-rpo-definition
  claim: RPO (Recovery Point Objective) is the maximum acceptable amount of time since the last data recovery point; the organization defines it, and it sets the acceptable data loss between the last recovery point and the interruption.
  scope: disaster recovery objectives.
  link: [maximum acceptable amount of time since the last data recovery point](../facts/well-architected.md#well-architected-rpo-definition)
  link: [RPO](../facts/well-architected.md#well-architected-rpo-definition)
well-architected-rto-definition
  claim: RTO (Recovery Time Objective) is the maximum acceptable delay between the interruption of service and the restoration of service; the organization defines it, and it sets the acceptable window of unavailability.
  scope: disaster recovery objectives.
  link: [maximum acceptable delay between the interruption of service and restoration of service](../facts/well-architected.md#well-architected-rto-definition)
  link: [RTO](../facts/well-architected.md#well-architected-rto-definition)
ebs-dlm-automates-snapshots-and-amis
  claim: Amazon Data Lifecycle Manager automates the creation, retention and deletion of EBS snapshots and EBS-backed AMIs, at no additional cost.
  scope: Amazon Data Lifecycle Manager.
  link: [creation, retention, and deletion of EBS snapshots](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis)
  link: [at no additional cost](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis)
ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis
  claim: Amazon Data Lifecycle Manager cannot manage snapshots or AMIs created by other means, and cannot automate instance store-backed AMIs.
  scope: Amazon Data Lifecycle Manager.
  link: [created by any other means](../facts/ebs.md#ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis)
  link: [instance store-backed AMIs](../facts/ebs.md#ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis)
ebs-dlm-cross-account-copy-isolated-account
  claim: Data Lifecycle Manager can automate cross-account snapshot copies: the source account shares snapshots and the target account's cross-account copy event policy copies them to chosen Regions in an isolated account and encrypts them, protecting against a compromised account.
  scope: Amazon Data Lifecycle Manager cross-account copy; both policies are created in the same Region.
  link: [specific Regions in an isolated account](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account)
  link: [your account being compromised](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account)
ebs-aws-backup-central-policy-across-accounts
  claim: AWS Backup centralizes data protection: you define one backup policy and apply it across accounts and Regions, and it covers many services, including EBS, EC2, S3, EFS, RDS and Aurora.
  scope: AWS Backup policies.
  link: [apply it across accounts and Regions](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts)
  link: [supports many AWS services](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts)
rds-backup-retention-range
  claim: The backup retention period of a DB instance can be set between 0 and 35 days, and setting it to 0 disables automated backups.
  scope: per DB instance; maximum; not adjustable; Multi-AZ DB clusters allow 1 to 35 days.
  link: [between 0 and 35 days](../facts/rds.md#rds-backup-retention-range)
  link: [Setting the backup retention period to 0 disables automated backups](../facts/rds.md#rds-backup-retention-range)
  say: zero to thirty-five days | zero turns automated backups off
dynamodb-pitr-35-days-default-1-to-35-configurable
  claim: Point-in-time recovery gives up to 35 days of recovery points at per-second granularity. The recovery period is 35 days by default and can be set to any value between 1 and 35 days per table.
  scope: per table with PITR enabled; default; adjustable; set with RecoveryPeriodinDays.
  link: [By default, your `RecoveryPeriodinDays` is 35](../facts/dynamodb.md#dynamodb-pitr-35-days-default-1-to-35-configurable)
  link: [any value between 1 and 35](../facts/dynamodb.md#dynamodb-pitr-35-days-default-1-to-35-configurable)
  link: [per second granularity](../facts/dynamodb.md#dynamodb-pitr-35-days-default-1-to-35-configurable)
  say: 35 days by default | anywhere from one to thirty-five days | per second
efs-default-backup-plan-daily-35-day-retention
  claim: The default EFS backup plan uses the AWS Backup recommended settings for automatic backups, which are daily backups with a 35-day retention period; you can edit the default backup plan settings using the AWS Backup console.
  scope: EFS default backup plan; default; adjustable.
  link: [daily backups with a 35-day retention period](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
  link: [AWS Backup recommended settings](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
  link: [edit the default backup plan settings](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
s3-object-lock-compliance-mode
  claim: In compliance mode, a protected object version cannot be overwritten or deleted by any user, including the root user; its retention mode cannot be changed and its retention period cannot be shortened. The only way to delete such an object before its retention date is to delete the AWS account.
  scope: per object version in compliance mode.
  link: [can't be overwritten or deleted by any user](../facts/s3.md#s3-object-lock-compliance-mode)
  link: [its retention period can't be shortened](../facts/s3.md#s3-object-lock-compliance-mode)
  link: [delete the associated AWS account](../facts/s3.md#s3-object-lock-compliance-mode)
s3-object-lock-governance-mode
  claim: In governance mode, users cannot overwrite or delete a locked object version or change its lock settings unless they have special permission. To override governance retention a user needs s3:BypassGovernanceRetention and must send the x-amz-bypass-governance-retention:true header.
  scope: per object version in governance mode; the user holds s3:BypassGovernanceRetention.
  link: [unless they have special permissions](../facts/s3.md#s3-object-lock-governance-mode)
  link: [s3:BypassGovernanceRetention](../facts/s3.md#s3-object-lock-governance-mode)
  link: [x-amz-bypass-governance-retention:true](../facts/s3.md#s3-object-lock-governance-mode)
s3-glacier-vault-lock-policy-immutable
  claim: Glacier Vault Lock enforces compliance controls such as write once read many (WORM) on an Amazon Glacier vault with a Vault Lock policy; once the policy is locked it can no longer be changed or deleted.
  scope: per Amazon Glacier vault.
  link: [lock the policy from future edits](../facts/s3-glacier.md#s3-glacier-vault-lock-policy-immutable)
  link: [can no longer be changed or deleted](../facts/s3-glacier.md#s3-glacier-vault-lock-policy-immutable)
ebs-case-games24x7-aws-backup-rpo-rto
  claim: Games24x7 set up automated backups of its S3 and EBS data with AWS Backup and, in testing, reached an RPO of 1 hour and an RTO of 30 minutes for a 5 TB database; it kept costs down with incremental EBS snapshots.
  scope: Games24x7, recovery testing.
  link: [1 hour](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  link: [30 minutes](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  link: [5 TB](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  say: one hour | thirty minutes | five terabytes
s3-glacier-change-vault-service-closed-2025-10
  claim: Amazon Glacier, the original standalone vault-based service, is no longer accepting new customers; the AWS list of services in maintenance shows Amazon S3 Glacier Direct with an announcement date of 2025-10-07. Existing data stays secure and accessible indefinitely, and for archival storage AWS recommends the S3 Glacier storage classes.
  scope: Amazon Glacier vaults and the 2012 REST API; existing customers continue.
  link: [2025-10-07](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  link: [is no longer accepting new customers](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  link: [Amazon Glacier storage classes in Amazon S3](../facts/s3-glacier.md#s3-glacier-change-vault-service-closed-2025-10)
  say: October seventh, twenty twenty-five | closed to new customers | the S3 Glacier storage classes
