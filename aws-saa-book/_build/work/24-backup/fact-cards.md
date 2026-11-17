facts card: 532 facts
backup-audit-manager-audits-policies-against-controls
  claim: AWS Backup Audit Manager audits the compliance of your backup policies against controls that you define; a control is a procedure that audits a backup requirement such as backup frequency or retention period.
  scope: AWS Backup Audit Manager.
  link: [audit the compliance of your AWS Backup policies](../facts/backup.md#backup-audit-manager-audits-policies-against-controls)
  link: [backup frequency or the backup retention period](../facts/backup.md#backup-audit-manager-audits-policies-against-controls)
backup-audit-manager-control-cross-account-copy
  claim: The control Cross-account backup copy is scheduled evaluates whether a resource has a cross-account backup copy configured.
  scope: AWS Backup Audit Manager controls.
  link: [Cross-account backup copy is scheduled](../facts/backup.md#backup-audit-manager-control-cross-account-copy)
  link: [cross-account backup copy configured](../facts/backup.md#backup-audit-manager-control-cross-account-copy)
backup-audit-manager-control-cross-region-copy
  claim: The control Cross-Region backup copy is scheduled evaluates whether a resource is configured to create copies of its backups to another AWS Region.
  scope: AWS Backup Audit Manager controls.
  link: [Cross-Region backup copy is scheduled](../facts/backup.md#backup-audit-manager-control-cross-region-copy)
  link: [copies of its backups to another AWS Region](../facts/backup.md#backup-audit-manager-control-cross-region-copy)
backup-audit-manager-control-encrypted
  claim: The control Recovery points are encrypted evaluates whether the recovery points are encrypted and has no customizable parameters.
  scope: AWS Backup Audit Manager controls.
  link: [Recovery points are encrypted](../facts/backup.md#backup-audit-manager-control-encrypted)
  link: [Evaluates if the recovery points are encrypted](../facts/backup.md#backup-audit-manager-control-encrypted)
backup-audit-manager-control-in-backup-plan
  claim: The control Backup resources are included in at least one backup plan evaluates whether resources are included in at least one backup plan and has no customizable parameters.
  scope: AWS Backup Audit Manager controls.
  link: [included in at least one backup plan](../facts/backup.md#backup-audit-manager-control-in-backup-plan)
  link: [Evaluates if resources are included](../facts/backup.md#backup-audit-manager-control-in-backup-plan)
backup-audit-manager-control-in-lag-vault
  claim: The control Resources are inside a logically air-gapped vault evaluates whether resources have at least one recovery point copied to a logically air-gapped vault within the specified value and timeframe.
  scope: AWS Backup Audit Manager controls.
  link: [Resources are inside a logically air-gapped vault](../facts/backup.md#backup-audit-manager-control-in-lag-vault)
  link: [copied to a logically air-gapped vault](../facts/backup.md#backup-audit-manager-control-in-lag-vault)
backup-audit-manager-control-min-frequency-retention
  claim: The control Backup plan has minimum frequency and minimum retention evaluates whether backup frequency and retention period meet the minimums you set, with the backup frequency and retention period as customizable parameters.
  scope: AWS Backup Audit Manager controls.
  link: [Backup plan has minimum frequency and minimum retention](../facts/backup.md#backup-audit-manager-control-min-frequency-retention)
  link: [Backup frequency; retention period](../facts/backup.md#backup-audit-manager-control-min-frequency-retention)
backup-audit-manager-control-restore-time
  claim: The control Restore time for resources meet target evaluates whether a restore testing job completed within the target restore time.
  scope: AWS Backup Audit Manager controls.
  link: [Restore time for resources meet target](../facts/backup.md#backup-audit-manager-control-restore-time)
  link: [restore testing job completed within target restore time](../facts/backup.md#backup-audit-manager-control-restore-time)
backup-audit-manager-control-vault-lock
  claim: The control Resources are in a backup plan with an AWS Backup Vault Lock evaluates whether a resource has a backup plan configured to store backups in a locked backup vault.
  scope: AWS Backup Audit Manager controls.
  link: [backup plan with an AWS Backup Vault Lock](../facts/backup.md#backup-audit-manager-control-vault-lock)
  link: [store backups in a locked backup vault](../facts/backup.md#backup-audit-manager-control-vault-lock)
backup-audit-manager-control-vault-prevent-deletion
  claim: The control Vaults prevent manual deletion of recovery points evaluates whether backup vaults deny manual deletion of recovery points except by certain IAM roles, with no IAM role exceptions by default.
  scope: AWS Backup Audit Manager controls.
  link: [Vaults prevent manual deletion of recovery points](../facts/backup.md#backup-audit-manager-control-vault-prevent-deletion)
  link: [By default, there are no IAM role exceptions](../facts/backup.md#backup-audit-manager-control-vault-prevent-deletion)
backup-audit-manager-cross-account-reports-management-and-delegated-only
  claim: In AWS Backup Audit Manager, all account holders can create cross-Region reports; management and delegated administrator account holders can also create cross-account reports.
  scope: AWS Backup Audit Manager reports.
  link: [All account holders can create cross-Region reports](../facts/backup.md#backup-audit-manager-cross-account-reports-management-and-delegated-only)
  link: [also create cross-account reports](../facts/backup.md#backup-audit-manager-cross-account-reports-management-and-delegated-only)
backup-audit-manager-findings-into-aws-audit-manager
  claim: You can automatically import AWS Backup Audit Manager findings into AWS Audit Manager to include backup compliance in your overall compliance posture, and the daily reports can show evidence of compliance over time.
  scope: AWS Backup Audit Manager.
  link: [findings into AWS Audit Manager](../facts/backup.md#backup-audit-manager-findings-into-aws-audit-manager)
  link: [evidence of compliance with your controls over time](../facts/backup.md#backup-audit-manager-findings-into-aws-audit-manager)
backup-audit-manager-frameworks-and-daily-reports
  claim: In AWS Backup Audit Manager you create frameworks that contain one or more governance control templates; Audit Manager automatically generates a new report for you every 24 hours and publishes it to Amazon S3, and you can also generate on-demand reports.
  scope: AWS Backup Audit Manager.
  link: [one or more governance control templates](../facts/backup.md#backup-audit-manager-frameworks-and-daily-reports)
  link: [automatically generates a new report for you every 24 hours](../facts/backup.md#backup-audit-manager-frameworks-and-daily-reports)
backup-audit-manager-needs-resource-tracking-aws-config
  claim: Before you create your first compliance-related framework in AWS Backup Audit Manager you must turn on resource tracking, which lets AWS Config track your AWS Backup resources, and charges apply for it.
  scope: AWS Backup Audit Manager frameworks.
  link: [you must turn on resource tracking](../facts/backup.md#backup-audit-manager-needs-resource-tracking-aws-config)
  link: [AWS Config to track your AWS Backup resources](../facts/backup.md#backup-audit-manager-needs-resource-tracking-aws-config)
backup-audit-manager-only-active-resources-evaluated
  claim: Only active resources are included when AWS Backup Audit Manager controls evaluate compliance: a running EC2 instance is evaluated, a stopped one is not.
  scope: AWS Backup Audit Manager controls.
  link: [only active resources will be included](../facts/backup.md#backup-audit-manager-only-active-resources-evaluated)
  link: [An EC2 instance in a stopped state will not be included](../facts/backup.md#backup-audit-manager-only-active-resources-evaluated)
backup-audit-manager-pricing-per-control-evaluation-and-config
  claim: AWS Backup Audit Manager is charged by the number of control evaluations, where one evaluation is one resource against one control, and AWS Config recording, which it requires, is charged separately on the AWS Config bill.
  scope: AWS Backup Audit Manager.
  link: [based on the number of control evaluations](../facts/backup.md#backup-audit-manager-pricing-per-control-evaluation-and-config)
  link: [AWS Config charges for each configuration item recorded](../facts/backup.md#backup-audit-manager-pricing-per-control-evaluation-and-config)
backup-audit-manager-reports-delivered-only-to-same-account-bucket
  claim: AWS Backup Audit Manager delivers reports only to Amazon S3 buckets that belong to the account in which the report plan or on-demand report is created; cross-account bucket delivery is not supported.
  scope: AWS Backup Audit Manager reports.
  link: [only to Amazon S3 buckets that belong to the account](../facts/backup.md#backup-audit-manager-reports-delivered-only-to-same-account-bucket)
  link: [Cross-account Amazon S3 bucket delivery is not supported](../facts/backup.md#backup-audit-manager-reports-delivered-only-to-same-account-bucket)
backup-audit-manager-reports-two-types-job-and-compliance
  claim: AWS Backup Audit Manager has two types of reports, and you choose the type when you create a report: a jobs report, and a compliance report, which can monitor resource levels or the different controls that are in effect.
  scope: AWS Backup Audit Manager reports.
  link: [compliance report](../facts/backup.md#backup-audit-manager-reports-two-types-job-and-compliance)
  link: [monitor resource levels or the different controls](../facts/backup.md#backup-audit-manager-reports-two-types-job-and-compliance)
backup-aurora-vault-snapshots-no-charge-condition
  claim: AWS does not charge for Aurora snapshots in a backup vault as long as Aurora automated backups are enabled and their retention period is longer than the retention period of the Aurora snapshots; snapshots whose database was deleted are charged.
  scope: Aurora snapshots in an AWS Backup vault; Aurora automated backups enabled and automated-backup retention longer than snapshot retention.
  link: [does not charge for Aurora snapshots](../facts/backup.md#backup-aurora-vault-snapshots-no-charge-condition)
  link: [charged if the snapshots' database is deleted](../facts/backup.md#backup-aurora-vault-snapshots-no-charge-condition)
backup-automatic-backups-use-plan-lifecycle-vault-and-tags
  claim: Backups created automatically by backup plans are configured with the lifecycle settings of the plan, organized in the backup vault the plan specifies, and assigned the tags listed in the plan.
  scope: backup plans.
  link: [configured with the lifecycle settings](../facts/backup.md#backup-automatic-backups-use-plan-lifecycle-vault-and-tags)
  link: [organized in the backup vault](../facts/backup.md#backup-automatic-backups-use-plan-lifecycle-vault-and-tags)
backup-billing-not-fully-managed-billed-by-service-lag-vault-under-backup
  claim: For resource types without full AWS Backup management, some AWS Backup activity such as storage costs is billed under the respective AWS service, but with a logically air-gapped vault all storage and data transfer charges appear under AWS Backup.
  scope: AWS Backup billing.
  link: [billing reflected by the respective AWS service](../facts/backup.md#backup-billing-not-fully-managed-billed-by-service-lag-vault-under-backup)
  link: [charges occur under AWS Backup](../facts/backup.md#backup-billing-not-fully-managed-billed-by-service-lag-vault-under-backup)
backup-case-calverthealth-edr-and-aws-backup-rto-72-hours-to-under-2
  claim: CalvertHealth deployed AWS Elastic Disaster Recovery and AWS Backup on almost 140 servers for its electronic health records system, and the changes cut its recovery time objective from 72 hours to under 2 hours, a 97 percent improvement.
  scope: CalvertHealth electronic health records system.
  link: [72 hours to under 2 hours](../facts/backup.md#backup-case-calverthealth-edr-and-aws-backup-rto-72-hours-to-under-2)
  link: [97 percent improvement](../facts/backup.md#backup-case-calverthealth-edr-and-aws-backup-rto-72-hours-to-under-2)
backup-central-management-needs-opt-in-plan-and-vault
  claim: To centrally manage data protection for your supported services, you opt in to managing that service with AWS Backup, create an on-demand backup or schedule backups with a backup plan, and store the backups in backup vaults.
  scope: AWS Backup central management.
  link: [opt in to managing that service](../facts/backup.md#backup-central-management-needs-opt-in-plan-and-vault)
  link: [store your backups in backup vaults](../facts/backup.md#backup-central-management-needs-opt-in-plan-and-vault)
backup-change-aurora-continuous-pitr-2023-09
  claim: The AWS Backup document history lists "Support for Amazon Aurora continuous backups and Point-in-time restore" on September 7, 2023: AWS Backup now supports continuous backups and point-in-time restore (PITR) for Aurora resources.
  scope: Aurora continuous backups in AWS Backup.
  link: [September 7, 2023](../facts/backup.md#backup-change-aurora-continuous-pitr-2023-09)
backup-change-aurora-dsql-2025-05
  claim: The AWS Backup document history lists "AWS Backup support for Amazon Aurora DSQL clusters" on May 27, 2025: AWS Backup now offers integration with Aurora DSQL in several AWS Regions, and customers can create backups and restore recovery points for Aurora DSQL single-Region and multi-Region clusters.
  scope: AWS Backup Amazon Aurora DSQL support.
  link: [May 27, 2025](../facts/backup.md#backup-change-aurora-dsql-2025-05)
backup-change-backup-search-2024-12
  claim: The AWS Backup document history lists "Search feature added" on December 17, 2024: the option to search your backup metadata for item level properties to help you find recovery points and other files or objects you want to restore.
  scope: AWS Backup search.
  link: [December 17, 2024](../facts/backup.md#backup-change-backup-search-2024-12)
backup-change-cloudformation-stacks-2022-11
  claim: The AWS Backup document history lists "AWS Backup offers support to backup AWS CloudFormation application stacks" on November 27, 2022: AWS Backup can back up CloudFormation and restore applications containing multiple resources by backing up a stack and restoring the resources within it.
  scope: AWS Backup CloudFormation application stack backups.
  link: [November 27, 2022](../facts/backup.md#backup-change-cloudformation-stacks-2022-11)
backup-change-delegated-admin-2022-11
  claim: The AWS Backup document history lists "AWS Backup offers delegated administrator accounts and backup policy delegation" on November 27,2022: accounts enrolled in AWS Organizations can designate member accounts as delegated administrator accounts.
  scope: AWS Backup with AWS Organizations.
  link: [November 27,2022](../facts/backup.md#backup-change-delegated-admin-2022-11)
backup-change-ebs-cold-storage-2023-11
  claim: The AWS Backup document history lists "Support for Amazon EBS cold storage" on November 27, 2023: AWS Backup now supports transitioning EBS backups from warm to cold storage.
  scope: AWS Backup cold storage for Amazon EBS.
  link: [November 27, 2023](../facts/backup.md#backup-change-ebs-cold-storage-2023-11)
backup-change-eks-support-2025-11
  claim: The AWS Backup document history lists "AWS Backup support for Amazon Elastic Kubernetes Service clusters" on November 10, 2025: customers can create backups and restore recovery points for Amazon EKS clusters and their associated resources.
  scope: AWS Backup Amazon EKS support.
  link: [November 10, 2025](../facts/backup.md#backup-change-eks-support-2025-11)
backup-change-fsx-ontap-cross-copy-2026-08
  claim: The AWS Backup document history lists "AWS Backup adds cross-Region and cross-account copy support for FSx for ONTAP" on August 27, 2026: AWS Backup now supports cross-account and cross-Region copy of FSx for ONTAP backups in most AWS Regions where FSx for ONTAP is supported.
  scope: FSx for ONTAP backup copies; generally available after 2026-07-15.
  link: [August 27, 2026](../facts/backup.md#backup-change-fsx-ontap-cross-copy-2026-08)
backup-change-guardduty-malware-protection-2025-11
  claim: The AWS Backup document history lists "Amazon GuardDuty Malware Protection for AWS Backup" on November 19, 2025: Amazon GuardDuty Malware Protection now supports AWS Backup, extending malware detection capabilities to EC2, EBS, and S3 backups.
  scope: Amazon GuardDuty Malware Protection for AWS Backup.
  link: [November 19, 2025](../facts/backup.md#backup-change-guardduty-malware-protection-2025-11)
  link: [EC2, EBS, and S3 backups](../facts/backup.md#backup-change-guardduty-malware-protection-2025-11)
backup-change-lag-cmk-2025-11
  claim: The AWS Backup document history lists "Logically air-gapped vault support for AWS KMS customer-managed keys" on November 6, 2025: logically air-gapped vaults now support encryption with AWS KMS customer-managed keys.
  scope: logically air-gapped vault encryption.
  link: [November 6, 2025](../facts/backup.md#backup-change-lag-cmk-2025-11)
backup-change-lag-eks-2026-03
  claim: The AWS Backup document history lists "Amazon EKS support for logically air-gapped vaults" on March 12, 2026: AWS Backup now supports backup, copy, and restore functionality for Amazon EKS clusters to logically air-gapped vaults.
  scope: logically air-gapped vault, Amazon EKS.
  link: [March 12, 2026](../facts/backup.md#backup-change-lag-eks-2026-03)
backup-change-lag-fsx-ontap-2026-09
  claim: The AWS Backup document history lists "Logically air-gapped vault support for FSx for ONTAP" on September 28, 2026: recovery points of FSx for ONTAP resources can now be copied to logically air-gapped vaults.
  scope: logically air-gapped vault, FSx for ONTAP; generally available after 2026-07-15.
  link: [September 28, 2026](../facts/backup.md#backup-change-lag-fsx-ontap-2026-09)
backup-change-lag-fsx-resource-expansion-2025-03
  claim: The AWS Backup document history lists "Logically air-gapped vault resource expansion" on March 12, 2025: recovery points of FSx for Lustre, FSx for Windows File Server, and FSx for OpenZFS resources can now be copied into a logically air-gapped vault.
  scope: logically air-gapped vault, FSx resource types.
  link: [March 12, 2025](../facts/backup.md#backup-change-lag-fsx-resource-expansion-2025-03)
backup-change-lag-primary-backups-2025-11
  claim: The AWS Backup document history lists "Primary backups to logically air-gapped vaults" on November 17, 2025: logically air-gapped vaults are now supported as a primary backup target, so a single backup copy can be kept. Previously, logically air-gapped vaults could only store copies of existing backups.
  scope: logically air-gapped vault as backup target.
  link: [November 17, 2025](../facts/backup.md#backup-change-lag-primary-backups-2025-11)
  link: [could only store copies of existing backups](../facts/backup.md#backup-change-lag-primary-backups-2025-11)
  changed: 2025-11-17: was Previously, logically air-gapped vaults could only store copies of existing backups.
backup-change-lag-vault-ga-2024-08
  claim: The AWS Backup document history dates the logically air-gapped vault to August 7, 2024, after a preview that ended June 27, 2024: it was introduced as a secondary type of vault for storing copies of backups, with enhanced security features and vault access sharing through AWS RAM. A later entry of November 17, 2025 adds primary backups: logically air-gapped vaults are now supported as a primary backup target, and previously they could only store copies of existing backups.
  scope: logically air-gapped vault.
  link: [August 7, 2024](../facts/backup.md#backup-change-lag-vault-ga-2024-08)
backup-change-legal-hold-2022-11
  claim: The AWS Backup document history lists "AWS Backup offers Legal Hold" on November 27, 2022: a new tool to help protect recovery points through a legal hold.
  scope: AWS Backup legal holds.
  link: [November 27, 2022](../facts/backup.md#backup-change-legal-hold-2022-11)
backup-change-multi-party-approval-2025-06
  claim: The AWS Backup document history lists "AWS Backup support for Multi-party approval" on June 17, 2025: optional integration for logically air-gapped vaults to use Multi-party approval, stated then as currently available for accounts in US East (N. Virginia).
  scope: multi-party approval for logically air-gapped vaults; the Region availability is the wording of that row, not a current statement.
  link: [June 17, 2025](../facts/backup.md#backup-change-multi-party-approval-2025-06)
backup-change-org-policy-redshift-serverless-dsql-2026-04
  claim: On Apr 21, 2026 AWS Backup announced Amazon Redshift Serverless namespaces and Amazon Aurora DSQL clusters as resource types in AWS Organizations backup policies. Previously, backing up them through organization backup policies required using tag-based selections or backing up all resources in a member account.
  scope: AWS Organizations backup policies.
  link: [Apr 21, 2026](../facts/backup.md#backup-change-org-policy-redshift-serverless-dsql-2026-04)
  link: [tag-based selections or backing up all resources](../facts/backup.md#backup-change-org-policy-redshift-serverless-dsql-2026-04)
  changed: 2026-04-21: was Previously, backing up Redshift Serverless namespaces and Aurora DSQL clusters through organization backup policies required using tag-based selections or backing up all resources in a member account.
backup-change-org-policy-selections-schema-2024-11
  claim: The AWS Organizations document history lists "Updated Backup policies" on November 14, 2024: AWS Backup policies updated the selections policy key to include a conditions policy key and added a new resources policy key to the schema, giving more flexibility in resource selection for backup policies.
  scope: AWS Organizations backup policies.
  link: [November 14, 2024](../facts/backup.md#backup-change-org-policy-selections-schema-2024-11)
backup-change-redshift-2022-11
  claim: The AWS Backup document history lists "AWS Backup supports Amazon Redshift" on November 27, 2022: AWS Backup can back up Amazon Redshift clusters and restore Redshift clusters and tables.
  scope: AWS Backup Amazon Redshift backups.
  link: [November 27, 2022](../facts/backup.md#backup-change-redshift-2022-11)
backup-change-redshift-serverless-2025-03
  claim: The AWS Backup document history lists "AWS Backup support for Amazon Redshift Serverless namespaces" on March 31, 2025: customers can use AWS Backup to create Redshift Serverless manual snapshot backups and to restore to Redshift Serverless namespaces.
  scope: AWS Backup Amazon Redshift Serverless support.
  link: [March 31, 2025](../facts/backup.md#backup-change-redshift-serverless-2025-03)
backup-change-restore-testing-2023-11
  claim: The AWS Backup document history lists "Introducing restore testing" on November 27, 2023: restore testing brings automated and periodic evaluation of restore viability and the ability to monitor restore job duration times.
  scope: AWS Backup restore testing.
  link: [November 27, 2023](../facts/backup.md#backup-change-restore-testing-2023-11)
backup-change-s3-access-points-2026-08
  claim: The AWS Backup document history lists "Access points for S3 backups" on August 6, 2026: AWS Backup now lets you create read-only access points for Amazon S3 recovery points, so you can access backup data using S3 APIs without initiating a restore.
  scope: access points for S3 backups; generally available after 2026-07-15.
  link: [August 6, 2026](../facts/backup.md#backup-change-s3-access-points-2026-08)
backup-change-s3-more-than-1000-buckets-2026-09
  claim: The AWS Backup document history lists "Expanded Amazon S3 bucket support" on September 1, 2026: AWS Backup now supports protecting more than 1,000 Amazon S3 buckets per account by integrating with Amazon S3 Event Notifications with system-generated tags.
  scope: S3 buckets protected per account; generally available after 2026-07-15.
  link: [September 1, 2026](../facts/backup.md#backup-change-s3-more-than-1000-buckets-2026-09)
  link: [more than 1,000 Amazon S3 buckets per account](../facts/backup.md#backup-change-s3-more-than-1000-buckets-2026-09)
backup-change-s3-tiering-2025-11
  claim: The AWS Backup document history lists "Backup tiering" on November 18, 2025: AWS Backup introduces a low-cost warm storage tier for Amazon S3 backup data.
  scope: S3 backup tiering.
  link: [November 18, 2025](../facts/backup.md#backup-change-s3-tiering-2025-11)
backup-change-schedule-preview-2025-10
  claim: On Oct 15, 2025 AWS Backup announced schedule preview for backup plans, helping you validate when your backups are scheduled to run; it shows the next ten scheduled backup runs, including when continuous backup, indexing, or copy settings take effect.
  scope: backup plan schedule preview.
  link: [Oct 15, 2025](../facts/backup.md#backup-change-schedule-preview-2025-10)
  link: [next ten scheduled backup runs](../facts/backup.md#backup-change-schedule-preview-2025-10)
backup-change-single-action-snapshot-copy-2025-10
  claim: On Oct 30, 2025 AWS Backup announced copying database snapshots across AWS Regions and accounts using a single copy action, for Amazon RDS, Amazon Aurora, Amazon Neptune, and Amazon DocumentDB. Previously this was a two-step process: first copying to a different Region, and then to a different account, or vice versa. The AWS Backup document history lists the same capability on October 23, 2025.
  scope: database snapshot copies (RDS, Aurora, Neptune, DocumentDB); the What's New post and the document history row give different dates.
  link: [Oct 30, 2025](../facts/backup.md#backup-change-single-action-snapshot-copy-2025-10)
  link: [two-step process](../facts/backup.md#backup-change-single-action-snapshot-copy-2025-10)
  link: [October 23, 2025](../facts/backup.md#backup-change-single-action-snapshot-copy-2025-10)
  changed: 2025-10-30: was Previously, you needed to perform this as a two-step process—first copying to a different Region, and then to a different account (or vice versa).
backup-change-vault-lock-governance-mode-2022-10
  claim: The AWS Backup document history lists "Expanded AWS Backup Vault Lock functionality" on October 4, 2022: Vault Lock can now be created in governance mode for additional IAM protections or in compliance mode to ensure immutability.
  scope: AWS Backup Vault Lock.
  link: [October 4, 2022](../facts/backup.md#backup-change-vault-lock-governance-mode-2022-10)
  link: [governance mode for additional IAM protections](../facts/backup.md#backup-change-vault-lock-governance-mode-2022-10)
backup-cold-ebs-is-snapshot-archive-monthly-or-less
  claim: Cold storage for Amazon EBS is Amazon EBS Snapshots Archive; if cold storage is enabled and your backup frequency is monthly or less often, you can have your backup plan transition EBS snapshots.
  scope: EBS snapshots in AWS Backup; cold storage enabled and backup frequency monthly or less often.
  link: [Amazon EBS Snapshots Archive](../facts/backup.md#backup-cold-ebs-is-snapshot-archive-monthly-or-less)
  link: [monthly or less often](../facts/backup.md#backup-cold-ebs-is-snapshot-archive-monthly-or-less)
backup-cold-incremental-billing-by-reference
  claim: For incremental resource types, data moves from warm to cold storage when no warm backup still references it, and data referenced only by cold backups is billed at cold storage tier prices; other backups stay at warm storage prices.
  scope: resource types that support incremental backups.
  link: [no longer referenced by warm backups](../facts/backup.md#backup-cold-incremental-billing-by-reference)
  link: [billed at cold storage tier prices](../facts/backup.md#backup-cold-incremental-billing-by-reference)
backup-cold-storage-ignored-for-unsupported-resources
  claim: The list of resources that can transition to cold storage is the Lifecycle to cold storage section of the Feature availability by resource table; the cold storage expression is ignored for other resources.
  scope: backup lifecycle settings.
  link: [ignored for other resources](../facts/backup.md#backup-cold-storage-ignored-for-unsupported-resources)
  link: [“Lifecycle to cold storage” section](../facts/backup.md#backup-cold-storage-ignored-for-unsupported-resources)
backup-cold-storage-incremental-warm-full-8-days
  claim: For incremental backups you must have at least one warm full backup. AWS Backup recommends not moving a backup to cold storage until after at least 8 days; if the full backup moves too soon, such as after 1 day, AWS Backup creates another warm full backup.
  scope: resource types that support incremental backups and cold storage; minimum; a recommendation, not a hard limit.
  link: [at least 8 days](../facts/backup.md#backup-cold-storage-incremental-warm-full-8-days)
  link: [transition to cold storage after 1 day](../facts/backup.md#backup-cold-storage-incremental-warm-full-8-days)
  say: at least eight days
backup-cold-storage-min-90-days-retention-rule
  claim: Backups that are transitioned to cold storage must be stored in cold storage for a minimum of 90 days, so the retention setting must be 90 days greater than the transition to cold after days setting.
  scope: backups that transition to cold storage; minimum.
  link: [minimum of 90 days](../facts/backup.md#backup-cold-storage-min-90-days-retention-rule)
  link: [90 days greater than the “transition to cold after days” setting](../facts/backup.md#backup-cold-storage-min-90-days-retention-rule)
  say: at least ninety days
backup-cold-storage-plan-total-retention-90-days
  claim: To use cold storage in a backup plan, you must have a total retention period of 90 days or greater.
  scope: backup plan lifecycle with cold storage; minimum.
  link: [90 days or greater](../facts/backup.md#backup-cold-storage-plan-total-retention-90-days)
  say: ninety days or more
backup-cold-storage-resource-types
  claim: The backup plan options page says cold storage is currently available for AWS CloudFormation, DynamoDB with advanced features, Amazon EBS (using EBS Snapshot Archive), Amazon EFS, SAP HANA databases on Amazon EC2 instances, Amazon Timestream and VMware virtual machines; the feature availability by resource table also marks lifecycle to cold storage for Amazon Aurora DSQL.
  scope: AWS Backup lifecycle to cold storage; DynamoDB only with advanced features.
  link: [Amazon EBS (using EBS Snapshot Archive)](../facts/backup.md#backup-cold-storage-resource-types)
  link: [Amazon EFS](../facts/backup.md#backup-cold-storage-resource-types)
  link: [DynamoDB with advanced features](../facts/backup.md#backup-cold-storage-resource-types)
  link: [Amazon Aurora DSQL](../facts/backup.md#backup-cold-storage-resource-types)
backup-cold-storage-transition-setting-cannot-change
  claim: The transition to cold after days setting of a backup cannot be changed after the backup has been transitioned to cold.
  scope: a backup already transitioned to cold storage.
  link: [setting cannot be changed after a backup](../facts/backup.md#backup-cold-storage-transition-setting-cannot-change)
  link: [“transition to cold after days” setting](../facts/backup.md#backup-cold-storage-transition-setting-cannot-change)
backup-cold-storage-update-min-age-plus-one-day
  claim: When you update the transition to cold after days setting of an existing backup, the value must be a minimum of the backup's age plus one day.
  scope: updating the lifecycle of an existing backup; minimum.
  link: [backup’s age plus one day](../facts/backup.md#backup-cold-storage-update-min-age-plus-one-day)
  link: [a minimum of the backup’s age](../facts/backup.md#backup-cold-storage-update-min-age-plus-one-day)
backup-continuous-aurora-not-in-lag-vault-but-vault-lock-ok
  claim: Aurora continuous backups are supported in vaults protected by Vault Lock, with the vault's retention settings enforced, but they do not support the logically air-gapped vault feature; to use a logically air-gapped vault with Aurora, use periodic snapshot backups.
  scope: Aurora continuous backups.
  link: [do not support the logically air-gapped vault feature](../facts/backup.md#backup-continuous-aurora-not-in-lag-vault-but-vault-lock-ok)
  link: [use periodic snapshot backups instead](../facts/backup.md#backup-continuous-aurora-not-in-lag-vault-but-vault-lock-ok)
backup-continuous-aurora-rpo-under-five-minutes
  claim: The recovery point objective (RPO) for Aurora continuous backups is typically less than 5 minutes, because Aurora copies data to Amazon S3 continuously in the background.
  scope: Aurora continuous backups; typical value.
  link: [typically less than 5 minutes](../facts/backup.md#backup-continuous-aurora-rpo-under-five-minutes)
  link: [copies data to Amazon S3 continuously](../facts/backup.md#backup-continuous-aurora-rpo-under-five-minutes)
backup-continuous-cannot-be-scheduled
  claim: Continuous backups and point-in-time restore cannot be scheduled with a time or cron expression, because they record changes over a period of time.
  scope: continuous backups.
  link: [cannot be scheduled](../facts/backup.md#backup-continuous-cannot-be-scheduled)
  link: [changes recorded over a period of time](../facts/backup.md#backup-continuous-cannot-be-scheduled)
backup-continuous-copy-becomes-snapshot-no-pitr
  claim: When a cross-Region or cross-account copy of a continuous backup is made, the copy becomes a snapshot (periodic) backup, and point-in-time restore is not available for the copy.
  scope: copies of continuous backups.
  link: [becomes a snapshot (periodic) backup](../facts/backup.md#backup-continuous-copy-becomes-snapshot-no-pitr)
  link: [is not available for these copies](../facts/backup.md#backup-continuous-copy-becomes-snapshot-no-pitr)
backup-continuous-copy-rule-takes-snapshot-then-copies
  claim: If a continuous backup rule also specifies a cross-account or cross-Region copy and AWS Backup supports the operation for the resource type, AWS Backup takes a snapshot of the resource and copies the snapshot to the destination vault; AWS Backup does not support on-demand copies of continuous backups.
  scope: continuous backup copies; AWS Backup supports the copy operation for the resource type.
  link: [takes a snapshot of the resource](../facts/backup.md#backup-continuous-copy-rule-takes-snapshot-then-copies)
  link: [does not support on-demand copies of continuous backups](../facts/backup.md#backup-continuous-copy-rule-takes-snapshot-then-copies)
backup-continuous-multiple-rules-multiple-vaults-extra-become-snapshots
  claim: If rules specify continuous backups of one resource in more than one vault, AWS Backup creates one continuous backup under the first rule processed, and each later continuous rule for that resource results in a snapshot (periodic) backup instead.
  scope: continuous backup rules, multiple vaults.
  link: [according to the first rule processed](../facts/backup.md#backup-continuous-multiple-rules-multiple-vaults-extra-become-snapshots)
  link: [will result in a snapshot (periodic) backup instead](../facts/backup.md#backup-continuous-multiple-rules-multiple-vaults-extra-become-snapshots)
backup-continuous-multiple-rules-single-vault-longest-retention
  claim: If several rules specify more than one continuous backup in a single vault, AWS Backup follows the rule with the longest retention period and ignores the additional rules.
  scope: continuous backup rules, single vault.
  link: [follows the rule with the longest retention period](../facts/backup.md#backup-continuous-multiple-rules-single-vault-longest-retention)
  link: [ignores additional rules](../facts/backup.md#backup-continuous-multiple-rules-single-vault-longest-retention)
backup-continuous-one-per-resource-redundant-extra
  claim: Each resource can have only one continuous backup (recovery point); additional continuous backups are redundant.
  scope: per resource; maximum.
  link: [can only have one continuous backup](../facts/backup.md#backup-continuous-one-per-resource-redundant-extra)
  link: [additional continuous backups are redundant](../facts/backup.md#backup-continuous-one-per-resource-redundant-extra)
backup-continuous-plan-one-recovery-point-updated
  claim: A continuous backup plan creates one continuous recovery point and updates that recovery point whenever the job runs.
  scope: continuous backup plans.
  link: [creates one continuous recovery point](../facts/backup.md#backup-continuous-plan-one-recovery-point-updated)
  link: [updates that recovery point whenever the job runs](../facts/backup.md#backup-continuous-plan-one-recovery-point-updated)
backup-continuous-rds-backup-window-managed-while-aws-backup-manages
  claim: While AWS Backup manages continuous backups for an RDS instance you cannot configure the automated backup window directly; AWS Backup places it near the RDS maintenance window, and you can influence the placement by adjusting the RDS maintenance window.
  scope: RDS instances with AWS Backup continuous backups.
  link: [cannot directly configure the automated backup window](../facts/backup.md#backup-continuous-rds-backup-window-managed-while-aws-backup-manages)
  link: [near the Amazon RDS maintenance window](../facts/backup.md#backup-continuous-rds-backup-window-managed-while-aws-backup-manages)
backup-continuous-rds-copy-uses-snapshot-instead-of-logs
  claim: You can't create copies of Amazon RDS continuous backups because AWS Backup for Amazon RDS does not allow copying transaction logs; instead, AWS Backup creates a snapshot and copies it with the frequency specified in the backup plan.
  scope: RDS continuous backups.
  link: [creates a snapshot and copies it](../facts/backup.md#backup-continuous-rds-copy-uses-snapshot-instead-of-logs)
  link: [frequency specified in the backup plan](../facts/backup.md#backup-continuous-rds-copy-uses-snapshot-instead-of-logs)
backup-continuous-rds-pitr-via-aws-backup-or-rds
  claim: You can perform a point-in-time restore of an RDS instance using either AWS Backup or Amazon RDS.
  scope: RDS point-in-time restore.
  link: [using either AWS Backup or Amazon RDS](../facts/backup.md#backup-continuous-rds-pitr-via-aws-backup-or-rds)
  link: [point-in-time restore](../facts/backup.md#backup-continuous-rds-pitr-via-aws-backup-or-rds)
backup-continuous-rds-settings-managed-only-in-aws-backup
  claim: After you apply an AWS Backup continuous backup rule to an RDS instance, you cannot create or modify continuous backup settings in Amazon RDS; you make changes through the AWS Backup console or CLI.
  scope: RDS instances with AWS Backup continuous backups.
  link: [can't create or modify continuous backup settings](../facts/backup.md#backup-continuous-rds-settings-managed-only-in-aws-backup)
  link: [AWS Backup console or the AWS Backup CLI](../facts/backup.md#backup-continuous-rds-settings-managed-only-in-aws-backup)
backup-continuous-rds-supported-not-multi-az-clusters
  claim: AWS Backup supports continuous backups and point-in-time recovery for all RDS instances and Aurora that the native RDS service supports, but not for Amazon RDS Multi-AZ clusters.
  scope: RDS and Aurora continuous backups.
  link: [does not support continuous backups or point-in-time recovery](../facts/backup.md#backup-continuous-rds-supported-not-multi-az-clusters)
  link: [all Amazon RDS instances and Aurora](../facts/backup.md#backup-continuous-rds-supported-not-multi-az-clusters)
backup-continuous-rule-allows-pitr-unlike-snapshot
  claim: A continuous backup rule is created with the enable continuous backups checkbox, and unlike snapshot backups it allows point-in-time restore.
  scope: continuous backup rules, supported resources.
  link: [continuous backups allow you to perform point-in-time restore](../facts/backup.md#backup-continuous-rule-allows-pitr-unlike-snapshot)
  link: [Unlike snapshot backups](../facts/backup.md#backup-continuous-rule-allows-pitr-unlike-snapshot)
backup-continuous-s3-depends-on-eventbridge-events
  claim: AWS Backup for S3 relies on S3 events delivered through Amazon EventBridge; if that setting is disabled in the S3 bucket notification settings, continuous backups stop for those buckets.
  scope: S3 continuous backups.
  link: [relies on receiving S3 events through Amazon EventBridge](../facts/backup.md#backup-continuous-s3-depends-on-eventbridge-events)
  link: [continuous backups will stop](../facts/backup.md#backup-continuous-s3-depends-on-eventbridge-events)
backup-copies-keep-source-creation-date-and-retention
  claim: Copies keep their source configuration, including the creation date (the time the source was created, not the copy) and the retention period, though you can override the retention period.
  scope: backup copies.
  link: [Copies retain their source configuration](../facts/backup.md#backup-copies-keep-source-creation-date-and-retention)
  link: [You can override the retention period](../facts/backup.md#backup-copies-keep-source-creation-date-and-retention)
backup-copy-action-same-or-other-region-and-account
  claim: A backup plan can optionally create a backup copy in the same or another AWS Region, and the copy can go to the same account or another account.
  scope: copy action in a backup plan.
  link: [in the same or another AWS Region](../facts/backup.md#backup-copy-action-same-or-other-region-and-account)
  link: [in the same account or another account](../facts/backup.md#backup-copy-action-same-or-other-region-and-account)
backup-copy-cold-storage-backups-cannot-be-copied
  claim: Backups in cold storage or archive tiers cannot be copied across accounts or Regions.
  scope: cross-account and cross-Region copies.
  link: [archive tiers cannot be copied](../facts/backup.md#backup-copy-cold-storage-backups-cannot-be-copied)
  link: [most resource types](../facts/backup.md#backup-copy-cold-storage-backups-cannot-be-copied)
backup-copy-expire-90-days-beyond-cold-transition
  claim: For a backup copy, the Expire value, which is the number of days after creation that the copy is deleted, must be greater than 90 days beyond the Transition to cold storage value.
  scope: copy lifecycle of a backup copy that transitions to cold storage; minimum.
  link: [greater than 90 days beyond the Transition to cold storage value](../facts/backup.md#backup-copy-expire-90-days-beyond-cold-transition)
  link: [90 days](../facts/backup.md#backup-copy-expire-90-days-beyond-cold-transition)
  say: ninety days
backup-copy-footnote-rds-multi-az-clusters-no-copy
  claim: A footnote of the AWS Backup feature availability table says RDS Multi-AZ database instances can be copied, but Multi-AZ clusters do not currently support any copy operations; the AWS Backup RDS page also says copying a Multi-AZ DB cluster snapshot is not supported.
  scope: RDS Multi-AZ.
  link: [do not currently support any copy operations](../facts/backup.md#backup-copy-footnote-rds-multi-az-clusters-no-copy)
  link: [Multi-AZ](../facts/backup.md#backup-copy-footnote-rds-multi-az-clusters-no-copy)
backup-copy-from-incremental-rds-s3-from-full-aurora-sap
  claim: Amazon RDS and Amazon S3 support cross-account and cross-Region copy from incremental backups, while Amazon Aurora and SAP HANA on EC2 support cross-account and cross-Region copy from full backups.
  scope: copy of RDS, S3, Aurora and SAP HANA backups.
  link: [support cross-account and cross-Region copy from incremental backups](../facts/backup.md#backup-copy-from-incremental-rds-s3-from-full-aurora-sap)
  link: [support cross-account and cross-Region copy from full backups](../facts/backup.md#backup-copy-from-incremental-rds-s3-from-full-aurora-sap)
backup-copy-iam-role-trusted-entity-default-created
  claim: The IAM role that creates a backup copy must list AWS Backup as a trusted entity; if you choose Default and the default role does not exist, AWS Backup creates one with the correct permissions.
  scope: backup copy IAM role.
  link: [AWS Backup listed as a trusted entity](../facts/backup.md#backup-copy-iam-role-trusted-entity-default-created)
  link: [a role is created for you](../facts/backup.md#backup-copy-iam-role-trusted-entity-default-created)
backup-copy-job-retry-phase-2-hours
  claim: If AWS Backup encounters a system error, a copy job enters a retry phase that lasts for 2 hours.
  scope: copy jobs; fixed; after system errors.
  link: [2 hours](../facts/backup.md#backup-copy-job-retry-phase-2-hours)
  say: two hours
backup-copy-lifecycle-follows-source-when-unset
  claim: If no expiry (DeleteAfterDays) is set in the copy settings, the copy follows the lifecycle settings of the backup it was copied from.
  scope: backup copy lifecycle; default; not adjustable.
  link: [follow the lifecycle settings of the backup](../facts/backup.md#backup-copy-lifecycle-follows-source-when-unset)
  link: [is not specified in the copy settings](../facts/backup.md#backup-copy-lifecycle-follows-source-when-unset)
backup-copy-never-expire-after-100-years
  claim: If you want backup copies to never expire, either set your source backups to never expire or specify that the copy expires 100 years after its creation.
  scope: backup copies.
  link: [100 years after its creation](../facts/backup.md#backup-copy-never-expire-after-100-years)
  link: [never expire](../facts/backup.md#backup-copy-never-expire-after-100-years)
  say: one hundred years after creation
backup-copy-no-sla-on-completion-time
  claim: AWS Backup does not provide any service-level agreements (SLAs) for copy job completion times; copy times vary with system load, capacity and resource size.
  scope: copy jobs.
  link: [does not provide any service-level agreements (SLAs)](../facts/backup.md#backup-copy-no-sla-on-completion-time)
  link: [copy job completion times](../facts/backup.md#backup-copy-no-sla-on-completion-time)
backup-copy-one-job-at-a-time-per-resource
  claim: Only one backup or copy job can run at a time for a given resource; additional copy jobs for that resource stay in CREATED status until the running job completes.
  scope: per resource; maximum.
  link: [Only one backup or copy job can run](../facts/backup.md#backup-copy-one-job-at-a-time-per-resource)
  link: [remain in CREATED status](../facts/backup.md#backup-copy-one-job-at-a-time-per-resource)
backup-copy-unsupported-without-checkmark
  claim: If a resource type has no check mark in the cross-Region backup or cross-account backup columns of the feature availability table, copy operations for that resource type are not supported in any scenario, including same-Region, same-account copies to a different vault.
  scope: resource types without a cross-Region or cross-account check mark.
  link: [not supported in any scenario](../facts/backup.md#backup-copy-unsupported-without-checkmark)
  link: [same-Region and same-account copies to a different vault](../facts/backup.md#backup-copy-unsupported-without-checkmark)
backup-copy-warm-retention-3-days-avoid-full-copy
  claim: For resources that support incremental cross-Region copy and cold storage, a copy configuration with only 1-day warm retention can fall back to a full copy, so AWS Backup recommends a warm retention period of at least 3 days or more for the copy action.
  scope: copy actions for resources that support incremental cross-Region copy and cold storage; minimum; a recommendation, not a hard limit.
  link: [at least 3 days or more](../facts/backup.md#backup-copy-warm-retention-3-days-avoid-full-copy)
  link: [only 1-day warm retention](../facts/backup.md#backup-copy-warm-retention-3-days-avoid-full-copy)
  say: at least three days
backup-cross-account-copy-purpose-recover-deleted-original
  claim: A cross-account backup securely copies backups to accounts in your organization, and if the original backup is inadvertently deleted you can copy it from the destination account back to the source account and start the restore.
  scope: cross-account copy.
  link: [from its destination account to its source account](../facts/backup.md#backup-cross-account-copy-purpose-recover-deleted-original)
  link: [inadvertently deleted](../facts/backup.md#backup-cross-account-copy-purpose-recover-deleted-original)
backup-cross-account-destination-key-fully-managed-vs-others
  claim: For a cross-account copy of resources fully managed by AWS Backup the destination vault can use a customer managed key or the AWS Backup managed key; for all other resource types a customer managed key is required, because AWS managed key policies are immutable and cannot be shared cross-account.
  scope: cross-account copy destination vault key.
  link: [a customer managed key is required](../facts/backup.md#backup-cross-account-destination-key-fully-managed-vs-others)
  link: [AWS managed key policies are immutable](../facts/backup.md#backup-cross-account-destination-key-fully-managed-vs-others)
backup-cross-account-destination-vault-key-policy-and-shared-cmk
  claim: For a cross-account copy you create a backup vault in the destination account with an encryption key and a resource-based access policy that lets AWS Backup access the resources, and in the source account you share a customer managed key with the destination account if the resources use one.
  scope: cross-account copy.
  link: [you must create a backup vault](../facts/backup.md#backup-cross-account-destination-vault-key-policy-and-shared-cmk)
  link: [share this customer managed key](../facts/backup.md#backup-cross-account-destination-vault-key-policy-and-shared-cmk)
backup-cross-account-destination-vault-must-allow-copy-into
  claim: You must allow backup:CopyIntoBackupVault in the access policy of the destination backup vault; without that policy attempts to copy into the destination account are denied.
  scope: destination backup vault of a cross-account copy.
  link: [the access policy backup:CopyIntoBackupVault](../facts/backup.md#backup-cross-account-destination-vault-must-allow-copy-into)
  link: [will deny attempts to copy](../facts/backup.md#backup-cross-account-destination-vault-must-allow-copy-into)
backup-cross-account-enable-only-with-management-credentials
  claim: Cross-account backup can be enabled or disabled only with the credentials of the AWS Organizations management account.
  scope: cross-account backup setting.
  link: [can only be enabled or disabled](../facts/backup.md#backup-cross-account-enable-only-with-management-credentials)
  link: [management account credentials](../facts/backup.md#backup-cross-account-enable-only-with-management-credentials)
backup-cross-account-management-account-enables-feature
  claim: The AWS Organizations management account opts in to cross-account backup, and before cross-account backups can start you must enable cross-account backup in the AWS Backup console or through the UpdateGlobalSettings API.
  scope: cross-account backup.
  link: [management account](../facts/backup.md#backup-cross-account-management-account-enables-feature)
  link: [UpdateGlobalSettings](../facts/backup.md#backup-cross-account-management-account-enables-feature)
backup-cross-account-management-components
  claim: Cross-account management in AWS Backup consists of cross-account monitoring, cross-account backups, backup policies and delegated administrator accounts, and not all of these elements are available in all Regions.
  scope: AWS Backup cross-account management.
  link: [cross-account monitoring, cross-account backups, backup policies](../facts/backup.md#backup-cross-account-management-components)
  link: [Not all of these elements are available](../facts/backup.md#backup-cross-account-management-components)
backup-cross-account-management-must-be-enabled-by-management-account
  claim: Before cross-account management can be used in AWS Backup, the management account must enable (opt in to) the feature; after that, backup policies can manage resources in multiple accounts.
  scope: AWS Backup cross-account management.
  link: [the management account must enable the feature](../facts/backup.md#backup-cross-account-management-must-be-enabled-by-management-account)
  link: [opt in](../facts/backup.md#backup-cross-account-management-must-be-enabled-by-management-account)
backup-cross-account-monitor-all-accounts-in-one-place
  claim: With AWS Organizations set up, AWS Backup can monitor activities in all your accounts in one place, and you can create a backup policy for selected accounts and view aggregate backup job activity in the AWS Backup console.
  scope: AWS Backup cross-account monitoring.
  link: [all of your accounts in one place](../facts/backup.md#backup-cross-account-monitor-all-accounts-in-one-place)
  link: [aggregate backup job activities](../facts/backup.md#backup-cross-account-monitor-all-accounts-in-one-place)
backup-cross-account-no-cold-tier-copies
  claim: AWS Backup does not support cross-account copies for storage in cold tiers.
  scope: cross-account copies.
  link: [does not support cross-account copies](../facts/backup.md#backup-cross-account-no-cold-tier-copies)
  link: [cold tiers](../facts/backup.md#backup-cross-account-no-cold-tier-copies)
backup-cross-account-requires-same-organization
  claim: To manage resources across accounts in AWS Backup, the accounts must belong to the same organization in AWS Organizations.
  scope: cross-account copy.
  link: [must belong to the same organization](../facts/backup.md#backup-cross-account-requires-same-organization)
  link: [AWS Organizations](../facts/backup.md#backup-cross-account-requires-same-organization)
backup-cross-region-copy-minimum-distance-requirement
  claim: AWS Backup describes cross-Region copy as particularly valuable when business continuity or compliance requirements call for storing backups a minimum distance away from production data.
  scope: cross-Region copy.
  link: [business continuity or compliance requirements](../facts/backup.md#backup-cross-region-copy-minimum-distance-requirement)
  link: [a minimum distance away from your production data](../facts/backup.md#backup-cross-region-copy-minimum-distance-requirement)
backup-cross-region-copy-on-demand-or-scheduled
  claim: AWS Backup can copy backups to multiple AWS Regions on demand or automatically as part of a scheduled backup plan.
  scope: cross-Region copy.
  link: [on demand or automatically](../facts/backup.md#backup-cross-region-copy-on-demand-or-scheduled)
  link: [copy backups to multiple AWS Regions](../facts/backup.md#backup-cross-region-copy-on-demand-or-scheduled)
backup-cross-region-ebs-different-key-full-copy
  claim: For EBS, copying a snapshot to a vault that uses a different KMS key gives a full (not incremental) copy; if you always copy to the same vault with the same key, later copies stay incremental.
  scope: EBS snapshot copies.
  link: [results in a full (not incremental) copy](../facts/backup.md#backup-cross-region-ebs-different-key-full-copy)
  link: [subsequent copies remain incremental](../facts/backup.md#backup-cross-region-ebs-different-key-full-copy)
backup-cross-region-first-copy-full-then-incremental
  claim: The first copy of a backup to a new Region is a full copy; for services that support incremental backups, later copies in that Region are in general incremental, and AWS Backup re-encrypts the copy with the destination vault's customer managed key.
  scope: cross-Region copy.
  link: [copies the backup in full](../facts/backup.md#backup-cross-region-first-copy-full-then-incremental)
  link: [in the same AWS Region will be incremental](../facts/backup.md#backup-cross-region-first-copy-full-then-incremental)
backup-cross-region-no-cold-tier-copies
  claim: AWS Backup does not support cross-Region copies for storage in cold tiers.
  scope: cross-Region copies.
  link: [does not support cross-Region copies](../facts/backup.md#backup-cross-region-no-cold-tier-copies)
  link: [cold tiers](../facts/backup.md#backup-cross-region-no-cold-tier-copies)
backup-cross-region-rds-copies-default-option-group
  claim: AWS Backup does not pass the option group in a cross-Region RDS copy; it copies the default option group even if you configured a custom option group.
  scope: Amazon RDS cross-Region copies.
  link: [does not pass the option group](../facts/backup.md#backup-cross-region-rds-copies-default-option-group)
  link: [copies the default option group](../facts/backup.md#backup-cross-region-rds-copies-default-option-group)
backup-dashboard-audits-backup-and-restore-activity
  claim: AWS Backup provides a dashboard that makes it simple to audit backup and restore activity across AWS services.
  scope: AWS Backup console.
  link: [audit backup and restore activity](../facts/backup.md#backup-dashboard-audits-backup-and-restore-activity)
  link: [across AWS services](../facts/backup.md#backup-dashboard-audits-backup-and-restore-activity)
backup-ddb-advanced-benefits-cold-copy-tags
  claim: After you enable AWS Backup's advanced DynamoDB features in a Region, DynamoDB backups inherit the tags of their source tables, so you can use those tags to set permissions and service control policies.
  scope: DynamoDB backups, per Region; advanced features enabled in the Region; applies to new backups.
  link: [Backups inherit tags from their source DynamoDB tables](../facts/backup.md#backup-ddb-advanced-benefits-cold-copy-tags)
  link: [service control policies (SCPs)](../facts/backup.md#backup-ddb-advanced-benefits-cold-copy-tags)
backup-ddb-advanced-default-for-customers-without-vault-before-2021-11-21
  claim: Advanced DynamoDB backup features are enabled by default for customers who started using AWS Backup after November 2021, specifically those who had not created a backup vault before November 21, 2021.
  scope: AWS Backup customers; default; adjustable.
  link: [not created a backup vault prior to November 21, 2021](../facts/backup.md#backup-ddb-advanced-default-for-customers-without-vault-before-2021-11-21)
  link: [after November 2021](../facts/backup.md#backup-ddb-advanced-default-for-customers-without-vault-before-2021-11-21)
backup-ddb-advanced-default-for-new-customers
  claim: New AWS Backup customers onboarding after November 2021 have the advanced DynamoDB backup features enabled by default, and AWS recommends that all existing AWS Backup customers enable advanced features for DynamoDB.
  scope: AWS Backup customers onboarding after November 2021; default; not adjustable; existing customers are recommended to enable them.
  link: [enabled by default](../facts/backup.md#backup-ddb-advanced-default-for-new-customers)
  link: [onboarding after November 2021](../facts/backup.md#backup-ddb-advanced-default-for-new-customers)
backup-ddb-advanced-does-not-replace-native-pitr
  claim: AWS Backup advanced DynamoDB features give periodic snapshot-based backups and do not replace or duplicate native DynamoDB point-in-time recovery (PITR), which gives continuous backup; if your recovery strategy needs both, you may enable both AWS Backup advanced features and native DynamoDB PITR, and in that case you will incur charges for both.
  scope: DynamoDB backups.
  link: [do not replace or duplicate native DynamoDB point-in-time](../facts/backup.md#backup-ddb-advanced-does-not-replace-native-pitr)
  link: [you will incur charges for both](../facts/backup.md#backup-ddb-advanced-does-not-replace-native-pitr)
backup-ddb-advanced-features-since-2021-11
  claim: Since November 2021 AWS Backup has advanced features for DynamoDB backups: copying backups across Regions and accounts, tiering backups to cold storage, and using tags for permissions and cost management.
  scope: DynamoDB backups in AWS Backup.
  link: [copying your backups across AWS Regions and accounts](../facts/backup.md#backup-ddb-advanced-features-since-2021-11)
  link: [tiering backups to cold storage](../facts/backup.md#backup-ddb-advanced-features-since-2021-11)
  link: [November 2021](../facts/backup.md#backup-ddb-advanced-features-since-2021-11)
backup-ddb-advanced-opt-in-by-plan-or-on-demand-automatic-policy-manual
  claim: Backups created by a backup plan or on demand automatically opt your account in to advanced DynamoDB backups, but if the backup job is created by a backup policy you must opt in manually, in the console or the CLI.
  scope: DynamoDB advanced backup opt-in.
  link: [automatically opt-in your account](../facts/backup.md#backup-ddb-advanced-opt-in-by-plan-or-on-demand-automatic-policy-manual)
  link: [manually opt-in to Advanced DynamoDB backups](../facts/backup.md#backup-ddb-advanced-opt-in-by-plan-or-on-demand-automatic-policy-manual)
backup-ddb-advanced-same-warm-price-tier-and-tag-savings
  claim: Enabling the advanced DynamoDB features does not change warm backup storage pricing, and you can save money by tiering backups to cold storage and by using cost allocation tags.
  scope: DynamoDB backups in AWS Backup.
  link: [no difference in warm backup storage pricing](../facts/backup.md#backup-ddb-advanced-same-warm-price-tier-and-tag-savings)
  link: [tiering backups to cold storage](../facts/backup.md#backup-ddb-advanced-same-warm-price-tier-and-tag-savings)
backup-default-vault-created-by-console
  claim: The first time you use the Backup vaults page of the AWS Backup console in a Region, the console automatically creates a default vault for that Region.
  scope: per Region, AWS Backup console.
  link: [automatically creates a default vault for the Region](../facts/backup.md#backup-default-vault-created-by-console)
  link: [first use the Backup Vaults page](../facts/backup.md#backup-default-vault-created-by-console)
backup-default-vault-not-created-by-cli-sdk-cloudformation
  claim: If you use AWS Backup through the AWS CLI, AWS SDK or CloudFormation, a default vault is not created and you must create your own vault.
  scope: AWS CLI, AWS SDK and CloudFormation.
  link: [a default vault is not created](../facts/backup.md#backup-default-vault-not-created-by-cli-sdk-cloudformation)
  link: [You must create your own vault](../facts/backup.md#backup-default-vault-not-created-by-cli-sdk-cloudformation)
backup-delegated-admin-manage-policies-member-accounts
  claim: A management account by default is the account used to edit and manage policies; with the delegated administrator feature you can delegate these management functions to member accounts you designate, and those accounts can manage policies in addition to the management account.
  scope: AWS Backup policies in AWS Organizations.
  link: [account used to edit and manage policies](../facts/backup.md#backup-delegated-admin-manage-policies-member-accounts)
  link: [delegate these management functions to member accounts](../facts/backup.md#backup-delegated-admin-manage-policies-member-accounts)
backup-delegated-admin-performs-most-admin-tasks-from-member-account
  claim: You can delegate AWS Backup administration to a member account in AWS Organizations, so assigned users there can do most AWS Backup administrative tasks from outside the management account and across the organization.
  scope: AWS Backup delegated administrator.
  link: [delegate administration of AWS Backup](../facts/backup.md#backup-delegated-admin-performs-most-admin-tasks-from-member-account)
  link: [outside the management account](../facts/backup.md#backup-delegated-admin-performs-most-admin-tasks-from-member-account)
backup-delegated-admin-privileges-enable-cross-account-row
  claim: Only the management account can enable cross-account management; delegated administrator and member accounts cannot.
  scope: AWS Backup delegated administration.
  link: [Enable cross-account management](../facts/backup.md#backup-delegated-admin-privileges-enable-cross-account-row)
  link: [Yes | No | No](../facts/backup.md#backup-delegated-admin-privileges-enable-cross-account-row)
backup-delegated-admin-privileges-manage-policies-row
  claim: The management account and a delegated administrator can manage backup policies across accounts in AWS Organizations; member accounts cannot.
  scope: AWS Backup delegated administration.
  link: [Manage backup policies across accounts in AWS Organizations](../facts/backup.md#backup-delegated-admin-privileges-manage-policies-row)
  link: [Yes | Yes | No](../facts/backup.md#backup-delegated-admin-privileges-manage-policies-row)
backup-delegated-admin-privileges-monitor-jobs-row
  claim: The management account and a delegated administrator can monitor cross-account jobs; member accounts cannot.
  scope: AWS Backup delegated administration.
  link: [Monitor cross-account jobs](../facts/backup.md#backup-delegated-admin-privileges-monitor-jobs-row)
  link: [Yes | Yes | No](../facts/backup.md#backup-delegated-admin-privileges-monitor-jobs-row)
backup-delegated-admin-privileges-register-deregister-row
  claim: Only the management account can register or deregister delegated administrator accounts; delegated administrator and member accounts cannot.
  scope: AWS Backup delegated administration.
  link: [Register/deregister delegated administrator accounts](../facts/backup.md#backup-delegated-admin-privileges-register-deregister-row)
  link: [Yes | No | No](../facts/backup.md#backup-delegated-admin-privileges-register-deregister-row)
backup-delegated-admin-reduces-management-account-access
  claim: Delegated administrator accounts allow managing backup policies, minimize the number of users with access to the management account, and permit cross-account monitoring of jobs; accounts, not users, are designated as delegated administrators.
  scope: AWS Backup delegated administrator.
  link: [minimizes the number of users with access](../facts/backup.md#backup-delegated-admin-reduces-management-account-access)
  link: [accounts, not users, are designated as delegated administrators](../facts/backup.md#backup-delegated-admin-reduces-management-account-access)
backup-delegated-admin-registration-alone-does-not-enable-policy-management
  claim: Registering an account as a delegated administrator alone does not enable backup policy management; you must also complete further steps for the account to view and edit backup policies.
  scope: AWS Backup delegated administrator.
  link: [alone does not enable backup policy management](../facts/backup.md#backup-delegated-admin-registration-alone-does-not-enable-policy-management)
  link: [view and edit backup policies](../facts/backup.md#backup-delegated-admin-registration-alone-does-not-enable-policy-management)
backup-does-not-govern-backups-outside-aws-backup
  claim: AWS Backup does not govern backups that you take in your AWS environment outside of AWS Backup.
  scope: backups made outside AWS Backup.
  link: [does not govern backups](../facts/backup.md#backup-does-not-govern-backups-outside-aws-backup)
  link: [outside of AWS Backup](../facts/backup.md#backup-does-not-govern-backups-outside-aws-backup)
backup-ebs-role-that-created-snapshot-must-delete-or-archive
  claim: The IAM role used to create an EBS snapshot recovery point is associated with that snapshot, and the same role must be used to delete those recovery points or transition them to an archive tier.
  scope: EBS snapshot recovery points.
  link: [associated with that snapshot](../facts/backup.md#backup-ebs-role-that-created-snapshot-must-delete-or-archive)
  link: [must be used to delete recovery points](../facts/backup.md#backup-ebs-role-that-created-snapshot-must-delete-or-archive)
backup-ebs-supports-cold-storage-archive-tier
  claim: Amazon EBS is one of the resources that supports a transition of backups to cold storage.
  scope: EBS backups.
  link: [supports a transition of backups to cold storage](../facts/backup.md#backup-ebs-supports-cold-storage-archive-tier)
  link: [EBS is one of the resource](../facts/backup.md#backup-ebs-supports-cold-storage-archive-tier)
backup-ec2-backup-is-ebs-backed-ami-with-snapshots
  claim: An EC2 backup in AWS Backup takes snapshots of the root volume, launch configuration and all associated EBS volumes, stores certain instance configuration parameters, and stores the backup data as an EBS volume-backed AMI.
  scope: EC2 instances in AWS Backup.
  link: [Amazon EBS volume-backed Amazon Machine Image (AMI)](../facts/backup.md#backup-ec2-backup-is-ebs-backed-ami-with-snapshots)
  link: [snapshot of the root Amazon EBS storage volume](../facts/backup.md#backup-ec2-backup-is-ebs-backed-ami-with-snapshots)
backup-ec2-marketplace-product-code-ami-no-cross-account-copy
  claim: An AMI created from an instance launched from an AWS Marketplace AMI has a product code, and with Amazon EC2 you cannot copy an AMI with a product code to another account, so AWS Backup has the same restriction.
  scope: EC2 instances launched from AWS Marketplace AMIs.
  link: [can't copy an AMI with a product code](../facts/backup.md#backup-ec2-marketplace-product-code-ami-no-cross-account-copy)
  link: [AWS Backup also has this restriction](../facts/backup.md#backup-ec2-marketplace-product-code-ami-no-cross-account-copy)
backup-ec2-never-reboots-instances
  claim: AWS Backup does not reboot your EC2 instances at any time.
  scope: EC2 instances in AWS Backup.
  link: [does not reboot your EC2 instances](../facts/backup.md#backup-ec2-never-reboots-instances)
  link: [at any time](../facts/backup.md#backup-ec2-never-reboots-instances)
backup-ec2-whole-instance-single-recovery-point
  claim: AWS Backup can back up an entire EC2 instance including its EBS volumes, and you can restore the whole instance from a single recovery point, including root volume, data volumes and some configuration such as instance type and key pair.
  scope: EC2 instances in AWS Backup.
  link: [restore an entire Amazon EC2 instance from a single recovery point](../facts/backup.md#backup-ec2-whole-instance-single-recovery-point)
  link: [instance type and key pair](../facts/backup.md#backup-ec2-whole-instance-single-recovery-point)
backup-edit-lifecycle-and-tags-after-creation
  claim: After you create a backup, you can change its lifecycle or tags; the lifecycle defines when the backup is transitioned to cold storage and when it expires, and AWS Backup transitions and expires backups automatically according to it. The cold storage expression is ignored for resources that are not in the Lifecycle to cold storage list, and editing backup tags in the AWS Backup console is only supported for backups of Amazon EFS file systems and advanced DynamoDB.
  scope: AWS Backup recovery points; cold storage only for supported resource types; console tag edits only for EFS and advanced DynamoDB backups.
  link: [change the lifecycle or tags of the backup](../facts/backup.md#backup-edit-lifecycle-and-tags-after-creation)
  link: [AWS Backup transitions and expires backups automatically](../facts/backup.md#backup-edit-lifecycle-and-tags-after-creation)
backup-efs-automatic-backup-vault-reserved
  claim: The EFS automatic backup vault aws/efs/automatic-backup-vault is reserved for automatic EFS backups only; using it as a destination for other backup plans gives an insufficient privileges error.
  scope: Amazon EFS automatic backup vault.
  link: [reserved for those automatic backups only](../facts/backup.md#backup-efs-automatic-backup-vault-reserved)
  link: [insufficient privileges](../facts/backup.md#backup-efs-automatic-backup-vault-reserved)
backup-eks-cluster-state-and-persistent-storage
  claim: AWS Backup backs up Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached by a persistent volume claim (EBS volumes, EFS file systems and S3 buckets), as a composite recovery point with a child recovery point for each resource.
  scope: Amazon EKS clusters.
  link: [Kubernetes cluster state and persistent storage](../facts/backup.md#backup-eks-cluster-state-and-persistent-storage)
  link: [composite recovery point](../facts/backup.md#backup-eks-cluster-state-and-persistent-storage)
backup-encryption-audit-manager-detects-unencrypted
  claim: AWS Backup Audit Manager helps you automatically detect unencrypted backups.
  scope: AWS Backup Audit Manager.
  link: [automatically detect unencrypted backups](../facts/backup.md#backup-encryption-audit-manager-detects-unencrypted)
  link: [AWS Backup Audit Manager helps you](../facts/backup.md#backup-encryption-audit-manager-detects-unencrypted)
backup-encryption-aurora-row
  claim: Aurora cluster snapshots are encrypted with the key of the source cluster (snapshots of unencrypted clusters stay unencrypted), and independent AWS Backup encryption is not supported.
  scope: Amazon Aurora backups.
  link: [encrypt the source Amazon Aurora cluster](../facts/backup.md#backup-encryption-aurora-row)
  link: [Not supported](../facts/backup.md#backup-encryption-aurora-row)
backup-encryption-copies-of-unencrypted-aurora-docdb-neptune-unencrypted
  claim: Copies of unencrypted Aurora, DocumentDB and Neptune clusters are also unencrypted.
  scope: copies of Aurora, DocumentDB and Neptune backups.
  link: [are also unencrypted](../facts/backup.md#backup-encryption-copies-of-unencrypted-aurora-docdb-neptune-unencrypted)
  link: [Amazon DocumentDB, and Amazon Neptune clusters](../facts/backup.md#backup-encryption-copies-of-unencrypted-aurora-docdb-neptune-unencrypted)
backup-encryption-copy-fully-managed-cmk-or-backup-managed-key
  claim: For a copy of a resource fully managed by AWS Backup, you can encrypt it with a customer managed key or the AWS Backup managed key (aws/backup).
  scope: copies of fully managed resource types.
  link: [customer managed key (CMK)](../facts/backup.md#backup-encryption-copy-fully-managed-cmk-or-backup-managed-key)
  link: [AWS Backup managed key](../facts/backup.md#backup-encryption-copy-fully-managed-cmk-or-backup-managed-key)
backup-encryption-copy-not-fully-managed-cmk-or-service-key
  claim: For a copy of a resource that is not fully managed by AWS Backup, the destination vault key must be a customer managed key or the managed key of the service that owns the resource; for an EC2 instance a Backup managed key cannot be used, and a CMK or aws/ebs must be used to avoid copy job failure.
  scope: copies of resource types not fully managed by AWS Backup.
  link: [a Backup managed key cannot be used](../facts/backup.md#backup-encryption-copy-not-fully-managed-cmk-or-service-key)
  link: [the managed key of the service](../facts/backup.md#backup-encryption-copy-not-fully-managed-cmk-or-service-key)
backup-encryption-copy-uses-destination-vault-key
  claim: When you copy backups across accounts or Regions, AWS Backup automatically encrypts the copies for most resource types, even if the original backup is unencrypted, using the KMS key of the target vault.
  scope: cross-account and cross-Region copies; most resource types.
  link: [the KMS key of the target vault](../facts/backup.md#backup-encryption-copy-uses-destination-vault-key)
  link: [even if the original backup is unencrypted](../facts/backup.md#backup-encryption-copy-uses-destination-vault-key)
backup-encryption-cross-account-aws-managed-key-unsupported-not-fully-managed
  claim: Cross-account copy with AWS managed keys is not supported for resources that are not fully managed by AWS Backup, because the key policy of an AWS managed key is immutable and prevents copying the key across accounts.
  scope: cross-account copies of resource types not fully managed by AWS Backup.
  link: [isn't supported for resources that aren't fully managed](../facts/backup.md#backup-encryption-cross-account-aws-managed-key-unsupported-not-fully-managed)
  link: [an AWS managed key is immutable](../facts/backup.md#backup-encryption-cross-account-aws-managed-key-unsupported-not-fully-managed)
backup-encryption-ddb-advanced-row
  claim: After you enable advanced DynamoDB backup features, DynamoDB backups are always encrypted with the KMS key configured in the AWS Backup vault, and independent AWS Backup encryption is supported.
  scope: DynamoDB with advanced backup features.
  link: [DynamoDB backups are always encrypted](../facts/backup.md#backup-encryption-ddb-advanced-row)
  link: [Supported](../facts/backup.md#backup-encryption-ddb-advanced-row)
backup-encryption-ddb-without-advanced-row
  claim: Without advanced DynamoDB backup features, DynamoDB backups are encrypted with the key of the source table (snapshots of unencrypted tables stay unencrypted) and independent AWS Backup encryption is not supported.
  scope: DynamoDB without advanced backup features.
  link: [encrypt the source DynamoDB table](../facts/backup.md#backup-encryption-ddb-without-advanced-row)
  link: [Not supported](../facts/backup.md#backup-encryption-ddb-without-advanced-row)
backup-encryption-ebs-row
  claim: By default EBS backups are encrypted with the key of the source volume or are unencrypted, you can override this during restore by specifying a KMS key, and independent AWS Backup encryption is not supported.
  scope: Amazon EBS backups.
  link: [used to encrypt the source volume](../facts/backup.md#backup-encryption-ebs-row)
  link: [Not supported](../facts/backup.md#backup-encryption-ebs-row)
backup-encryption-efs-row
  claim: EFS backups are always encrypted with the KMS key configured in the AWS Backup vault, and independent AWS Backup encryption is supported.
  scope: Amazon EFS backups.
  link: [Amazon EFS backups are always encrypted](../facts/backup.md#backup-encryption-efs-row)
  link: [Supported](../facts/backup.md#backup-encryption-efs-row)
backup-encryption-failed-jobs-from-deny-or-revoked-grant
  claim: Failed backup jobs can come from one or more Deny statements on the KMS key or from a grant revoked for the key.
  scope: AWS Backup and KMS keys.
  link: [Deny statements applied to the KMS key](../facts/backup.md#backup-encryption-failed-jobs-from-deny-or-revoked-grant)
  link: [a grant revoked for the key](../facts/backup.md#backup-encryption-failed-jobs-from-deny-or-revoked-grant)
backup-encryption-independent-for-fully-managed-types
  claim: For resource types that support full AWS Backup management, backups can use an encryption method other than the source resource's, controlled by the KMS key of the backup vault where the backup is stored.
  scope: resource types with full AWS Backup management.
  link: [independent encryption](../facts/backup.md#backup-encryption-independent-for-fully-managed-types)
  link: [encryption method other than one determined](../facts/backup.md#backup-encryption-independent-for-fully-managed-types)
backup-encryption-independent-uses-aes-256
  claim: When AWS Backup independently encrypts a backup, it uses the AES-256 encryption algorithm.
  scope: independent encryption.
  link: [industry-standard AES-256 encryption algorithm](../facts/backup.md#backup-encryption-independent-uses-aes-256)
  link: [independently encrypts a backup](../facts/backup.md#backup-encryption-independent-uses-aes-256)
backup-encryption-not-fully-managed-inherit-source
  claim: Backups of resource types that are not fully managed by AWS Backup typically inherit the encryption settings of their source resource.
  scope: resource types not fully managed by AWS Backup.
  link: [not fully managed by AWS Backup](../facts/backup.md#backup-encryption-not-fully-managed-inherit-source)
  link: [inherit the encryption settings from their source resource](../facts/backup.md#backup-encryption-not-fully-managed-inherit-source)
backup-encryption-rds-row
  claim: RDS snapshots are encrypted with the key of the source database (snapshots of unencrypted databases stay unencrypted), and independent AWS Backup encryption is not supported.
  scope: Amazon RDS backups.
  link: [encrypt the source Amazon RDS database](../facts/backup.md#backup-encryption-rds-row)
  link: [Not supported](../facts/backup.md#backup-encryption-rds-row)
backup-encryption-role-needs-kms-access-else-silent-skip
  claim: The IAM role used for a backup or restore must have access to the KMS key; otherwise the job succeeds but the objects are not backed up or restored.
  scope: backup and restore jobs, KMS key.
  link: [Otherwise the job is successful](../facts/backup.md#backup-encryption-role-needs-kms-access-else-silent-skip)
  link: [objects are not backed up or restored](../facts/backup.md#backup-encryption-role-needs-kms-access-else-silent-skip)
backup-encryption-s3-row
  claim: S3 backups are encrypted with a KMS key associated with the backup vault (customer managed, or the AWS managed key of AWS Backup), AWS Backup encrypts all S3 backups even if the source bucket is unencrypted, and independent AWS Backup encryption is supported.
  scope: Amazon S3 backups.
  link: [Supported](../facts/backup.md#backup-encryption-s3-row)
  link: [even if the source Amazon S3 buckets are not encrypted](../facts/backup.md#backup-encryption-s3-row)
backup-every-backup-starts-in-warm-storage
  claim: Every backup is created and stored in warm storage; depending on how long you store it, you may transition it to a lower-cost tier called cold storage, an optional feature whose supported resources are shown in the Feature availability by resource table.
  scope: AWS Backup storage tiers.
  link: [stored in warm storage](../facts/backup.md#backup-every-backup-starts-in-warm-storage)
  link: [lower-cost tier called cold storage](../facts/backup.md#backup-every-backup-starts-in-warm-storage)
backup-existing-backups-retained-regardless-of-source-health
  claim: AWS Backup retains previously created backups consistent with your lifecycle policy, regardless of the health of the source resource.
  scope: AWS Backup recovery points.
  link: [regardless of the health of your source resource](../facts/backup.md#backup-existing-backups-retained-regardless-of-source-health)
  link: [consistent with your lifecycle policy](../facts/backup.md#backup-existing-backups-retained-regardless-of-source-health)
backup-faq-access-backups-both-ways
  claim: Backups created by services with their own backup capabilities, such as EBS snapshots, can be accessed using AWS Backup, and backups created by AWS Backup can be accessed using the source service.
  scope: backups of services with existing backup capabilities.
  link: [can be accessed using AWS Backup](../facts/backup.md#backup-faq-access-backups-both-ways)
  link: [can be accessed using the source service](../facts/backup.md#backup-faq-access-backups-both-ways)
backup-faq-advanced-features-automatic
  claim: EFS, S3, Timestream, SAP HANA on EC2, Aurora DSQL and VMware virtual machines automatically support AWS Backup advanced features.
  scope: EFS, S3, Timestream, SAP HANA on EC2, Aurora DSQL, VMware.
  link: [automatically support AWS Backup advanced features](../facts/backup.md#backup-faq-advanced-features-automatic)
backup-faq-advanced-features-service-list
  claim: The FAQ says S3, EFS, Timestream, SAP HANA on EC2, Aurora DSQL and DynamoDB currently support AWS Backup advanced features through backup functionality integrated with AWS Backup.
  scope: advanced features (FAQ service list).
  link: [support AWS Backup advanced features](../facts/backup.md#backup-faq-advanced-features-service-list)
backup-faq-assigned-resources-encrypted-vault
  claim: After you define a backup plan and assign AWS resources to it, AWS Backup automates the creation of backups and stores them in an encrypted backup vault that you designate.
  scope: resources assigned to a backup plan.
  link: [automates the creation of backups](../facts/backup.md#backup-faq-assigned-resources-encrypted-vault)
  link: [encrypted backup vault that you designate](../facts/backup.md#backup-faq-assigned-resources-encrypted-vault)
backup-faq-audit-manager-compliance-status
  claim: A control is COMPLIANT when all the resources it evaluates are compliant, and a framework is COMPLIANT when all of its controls are compliant.
  scope: Audit Manager controls and frameworks.
  link: [compliance status of the control is COMPLIANT](../facts/backup.md#backup-faq-audit-manager-compliance-status)
  link: [compliance status of the framework is COMPLIANT](../facts/backup.md#backup-faq-audit-manager-compliance-status)
backup-faq-audit-manager-config-integration
  claim: AWS Backup Audit Manager integrates with AWS Config to track backup activity and to turn your data protection policies into backup controls.
  scope: AWS Backup Audit Manager.
  link: [integrates with AWS Config](../facts/backup.md#backup-faq-audit-manager-config-integration)
  link: [transcribe your data protection policies into backup controls](../facts/backup.md#backup-faq-audit-manager-config-integration)
backup-faq-audit-manager-control-framework
  claim: An Audit Manager control is a procedure that audits the compliance of one backup requirement, such as backup frequency or retention period; a framework is a collection of controls deployed and managed as a single entity.
  scope: AWS Backup Audit Manager.
  link: [a collection of controls](../facts/backup.md#backup-faq-audit-manager-control-framework)
  link: [deployed and managed as a single entity](../facts/backup.md#backup-faq-audit-manager-control-framework)
backup-faq-audit-manager-multi-account-reports
  claim: With Audit Manager you can create multi-Region and multi-account reports from your AWS Organization's management account.
  scope: AWS Backup Audit Manager reports.
  link: [multi-Region and multi-account reports](../facts/backup.md#backup-faq-audit-manager-multi-account-reports)
  link: [AWS Organization's management account](../facts/backup.md#backup-faq-audit-manager-multi-account-reports)
backup-faq-audit-manager-purpose
  claim: AWS Backup Audit Manager audits and reports on the compliance of your data protection policies, and helps you maintain and demonstrate compliance with them.
  scope: AWS Backup Audit Manager.
  link: [the compliance of your data protection policies](../facts/backup.md#backup-faq-audit-manager-purpose)
backup-faq-audit-manager-report-types
  claim: Audit Manager reports cover backup activity (backup, copy and restore jobs), scanning activity (malware scanning jobs) and compliance posture (compliance frameworks).
  scope: AWS Backup Audit Manager reports.
  link: [AWS Backup activity reports](../facts/backup.md#backup-faq-audit-manager-report-types)
  link: [AWS Backup compliance reports](../facts/backup.md#backup-faq-audit-manager-report-types)
backup-faq-backup-plan-central-policy
  claim: A backup plan is the central data protection policy of AWS Backup, and it works across AWS services for compute, storage and databases. It defines parameters such as backup frequency and backup retention period.
  scope: backup plan.
  link: [central data protection policy called a backup plan](../facts/backup.md#backup-faq-backup-plan-central-policy)
  link: [backup frequency and backup retention period](../facts/backup.md#backup-faq-backup-plan-central-policy)
backup-faq-backup-rule-four-parts
  claim: A backup plan has one or more backup rules, and each rule has a schedule (frequency and window), a lifecycle rule, a target backup vault, and tags to add to backups.
  scope: backup plan, backup rule.
  link: [comprised of one or more backup rules](../facts/backup.md#backup-faq-backup-rule-four-parts)
backup-faq-can-back-up-on-premises
  claim: AWS Backup can back up on-premises Storage Gateway volumes and VMware virtual machines, which gives one common way to manage backups on premises and on AWS.
  scope: on-premises data (FAQ).
  link: [on-premises Storage Gateway volumes and VMware virtual machines](../facts/backup.md#backup-faq-can-back-up-on-premises)
  link: [both on premises and on AWS](../facts/backup.md#backup-faq-can-back-up-on-premises)
backup-faq-cloudtrail-activity-logs
  claim: AWS Backup integrates with AWS CloudTrail to give a consolidated view of backup activity logs and to simplify the audit process for protected resources.
  scope: AWS Backup activity logging.
  link: [integrates with AWS CloudTrail](../facts/backup.md#backup-faq-cloudtrail-activity-logs)
  link: [consolidated view of backup activity logs](../facts/backup.md#backup-faq-cloudtrail-activity-logs)
backup-faq-cloudwatch-dashboards-fallback
  claim: In Regions where the native AWS Backup dashboard is not supported, Amazon CloudWatch dashboards are included in the AWS Backup console to show metrics on completed or failed backup, copy and restore jobs.
  scope: Regions without the native dashboard.
  link: [Amazon CloudWatch dashboards are included](../facts/backup.md#backup-faq-cloudwatch-dashboards-fallback)
backup-faq-dashboards-job-tracking
  claim: AWS Backup includes dashboards to track backup activities such as backup, copy and restore jobs.
  scope: AWS Backup console.
  link: [dashboards to track backup activities](../facts/backup.md#backup-faq-dashboards-job-tracking)
backup-faq-delegated-admin-actions
  claim: Delegated backup administrators can create and manage backup policies and monitor backup activity across accounts.
  scope: delegated backup administrator.
  link: [create and manage backup policies](../facts/backup.md#backup-faq-delegated-admin-actions)
  link: [monitor backup activity across accounts](../facts/backup.md#backup-faq-delegated-admin-actions)
backup-faq-delegated-admin-centralize
  claim: A delegated administrator lets you delegate backup policy management in AWS Organizations and cross-account monitoring in AWS Backup to dedicated backup administration accounts, so member accounts do not need to access the management account for backup administration.
  scope: AWS Organizations backup administration.
  link: [dedicated backup administration accounts](../facts/backup.md#backup-faq-delegated-admin-centralize)
  link: [removing the need for member accounts](../facts/backup.md#backup-faq-delegated-admin-centralize)
backup-faq-dlm-and-backup-independent
  claim: Amazon Data Lifecycle Manager policies and AWS Backup plans work independently from each other and give two ways to manage EBS snapshots.
  scope: EBS snapshots.
  link: [work independently from each other](../facts/backup.md#backup-faq-dlm-and-backup-independent)
  link: [two ways to manage EBS snapshots](../facts/backup.md#backup-faq-dlm-and-backup-independent)
backup-faq-dlm-vs-backup-when-to-use
  claim: Use Amazon Data Lifecycle Manager to automate creation, retention and deletion of EBS snapshots. Use AWS Backup to manage and monitor backups across the AWS services you use, including EBS volumes, from a single place.
  scope: EBS snapshots versus multi-service backups.
  link: [creation, retention, and deletion of EBS snapshots](../facts/backup.md#backup-faq-dlm-vs-backup-when-to-use)
  link: [from a single place](../facts/backup.md#backup-faq-dlm-vs-backup-when-to-use)
backup-faq-dynamodb-advanced-opt-in
  claim: To activate AWS Backup advanced features for DynamoDB, you must opt in through settings.
  scope: DynamoDB advanced features.
  link: [you must opt in through settings](../facts/backup.md#backup-faq-dynamodb-advanced-opt-in)
backup-faq-encryption-independent-vault-level
  claim: Backups for EFS, DynamoDB, S3, Timestream and VMware virtual machines are encrypted in transit and at rest independently from the source services, and the encryption is configured at the backup vault level.
  scope: EFS, DynamoDB, S3, Timestream and VMware backups.
  link: [independently from source services](../facts/backup.md#backup-faq-encryption-independent-vault-level)
  link: [Encryption is configured at the backup vault level](../facts/backup.md#backup-faq-encryption-independent-vault-level)
backup-faq-encryption-source-service-method
  claim: Backups from EC2, EBS, FSx, RDS, Aurora, DocumentDB, Neptune and Storage Gateway are encrypted with the source service's backup encryption method; for example EBS snapshots use the key of the volume they were made from.
  scope: EC2, EBS, FSx, RDS, Aurora, DocumentDB, Neptune, Storage Gateway backups.
  link: [the encryption key of the volume](../facts/backup.md#backup-faq-encryption-source-service-method)
  link: [source service’s backup encryption methodology](../facts/backup.md#backup-faq-encryption-source-service-method)
backup-faq-guardduty-malware-how
  claim: AWS Backup starts malware scans from backup plan settings or on-demand requests, GuardDuty then reads, decrypts and scans the backup content, and all scans run asynchronously so backup workflows and performance are not impacted.
  scope: GuardDuty Malware Protection for AWS Backup.
  link: [reads, decrypts, and scans the backup content](../facts/backup.md#backup-faq-guardduty-malware-how)
  link: [All scans run asynchronously](../facts/backup.md#backup-faq-guardduty-malware-how)
backup-faq-guardduty-malware-what
  claim: Amazon GuardDuty Malware Protection for AWS Backup detects malicious code in S3, EC2 and EBS backups; you can enable automatic scanning in backup plans or run on-demand scans to find clean recovery points.
  scope: GuardDuty Malware Protection for AWS Backup (FAQ).
  link: [Amazon S3, Amazon EC2, and Amazon EBS backups](../facts/backup.md#backup-faq-guardduty-malware-what)
  link: [run on-demand scans to identify clean recovery points](../facts/backup.md#backup-faq-guardduty-malware-what)
backup-faq-hipaa-eligible-baa
  claim: AWS Backup is HIPAA eligible, which means that if you have a HIPAA BAA in place with AWS, you can use AWS Backup to transfer protected health information (PHI).
  scope: AWS Backup compliance (FAQ); a HIPAA BAA must be in place with AWS.
  link: [AWS Backup is HIPAA eligible](../facts/backup.md#backup-faq-hipaa-eligible-baa)
  link: [a HIPAA BAA in place with AWS](../facts/backup.md#backup-faq-hipaa-eligible-baa)
backup-faq-key-features-advanced
  claim: The FAQ lists these advanced features: lifecycle policies to a low-cost storage tier, backup storage and encryption independent from the source data, indexing and search, malware scanning, Audit Manager reporting, delete protection with Vault Lock, and immutable copies with a logically air-gapped vault.
  scope: AWS Backup advanced features (FAQ).
  link: [delete protection with AWS Backup Vault Lock](../facts/backup.md#backup-faq-key-features-advanced)
  link: [immutable backup copies with AWS Backup](../facts/backup.md#backup-faq-key-features-advanced)
backup-faq-key-features-centralized
  claim: AWS Backup provides a centralized console, automated backup scheduling, backup retention management, and backup monitoring and alerting.
  scope: AWS Backup core features.
  link: [centralized console, automated backup scheduling](../facts/backup.md#backup-faq-key-features-centralized)
  link: [backup monitoring and alerting](../facts/backup.md#backup-faq-key-features-centralized)
backup-faq-lag-vault-definition
  claim: A logically air-gapped vault is a type of AWS Backup vault that stores an immutable backup, encrypted with AWS owned keys or customer managed KMS keys, and works for both primary backups and copies of backups.
  scope: logically air-gapped vault.
  link: [vault that store an immutable backup](../facts/backup.md#backup-faq-lag-vault-definition)
  link: [both primary backups and copies of backups](../facts/backup.md#backup-faq-lag-vault-definition)
backup-faq-lag-vault-locked-by-default
  claim: In a logically air-gapped vault, immutable backups are locked by default and protected by encryption with AWS-owned keys (preferred) or customer managed keys.
  scope: logically air-gapped vault; default; not adjustable; encryption uses AWS-owned keys (preferred) or customer managed keys.
  link: [immutable backups are locked by default](../facts/backup.md#backup-faq-lag-vault-locked-by-default)
  link: [AWS-owned keys (preferred)](../facts/backup.md#backup-faq-lag-vault-locked-by-default)
backup-faq-lag-vault-ransomware-strategy
  claim: A logically air-gapped vault is part of a data protection or ransomware resilience strategy, and its backups can be shared with and restored from a different account than the one that created the backup.
  scope: logically air-gapped vault.
  link: [ransomware resilience strategy](../facts/backup.md#backup-faq-lag-vault-ransomware-strategy)
  link: [restored from a different account](../facts/backup.md#backup-faq-lag-vault-ransomware-strategy)
backup-faq-lag-vault-share-ram
  claim: Logically air-gapped vaults are shared across accounts through AWS RAM, within your AWS Organizations and with accounts in different Organizations, and backups can be restored in the destination account without extra copies.
  scope: logically air-gapped vault sharing.
  link: [through AWS Resource Access Manager (AWS RAM)](../facts/backup.md#backup-faq-lag-vault-share-ram)
  link: [with accounts in different Organizations](../facts/backup.md#backup-faq-lag-vault-share-ram)
backup-faq-legal-hold-definition
  claim: Legal holds, also known as litigation holds, prevent backups from being deleted even if their retention period is over, and they stay in place until they are explicitly released.
  scope: legal hold.
  link: [even if their retention period is over](../facts/backup.md#backup-faq-legal-hold-definition)
  link: [remain in place until explicitly released](../facts/backup.md#backup-faq-legal-hold-definition)
backup-faq-lifecycle-warm-to-cold
  claim: The AWS Backup lifecycle feature can automatically transition recovery points from a warm storage tier to a lower-cost cold storage tier.
  scope: AWS Backup lifecycle (FAQ).
  link: [a lower-cost cold storage tier](../facts/backup.md#backup-faq-lifecycle-warm-to-cold)
backup-faq-mpa-access-when-account-inaccessible
  claim: Multi-party approval for a logically air-gapped vault lets customers authorize access to backups even when the account becomes inaccessible, including because of malware.
  scope: multi-party approval with logically air-gapped vaults.
  link: [even when the account becomes inaccessible](../facts/backup.md#backup-faq-mpa-access-when-account-inaccessible)
backup-faq-mpa-approvers-vote
  claim: Approvers review and vote on the access request through the Approval portal, which allows the requester to restore or copy backups for recovery.
  scope: multi-party approval.
  link: [vote for the request through the Approval portal](../facts/backup.md#backup-faq-mpa-approvers-vote)
backup-faq-native-dashboard-cross-account-region
  claim: The native AWS Backup dashboard monitors backup health across multiple environments through cross-account and cross-Region support.
  scope: AWS Backup native dashboard.
  link: [cross account and cross region support](../facts/backup.md#backup-faq-native-dashboard-cross-account-region)
  link: [monitor backup health across multiple environments](../facts/backup.md#backup-faq-native-dashboard-cross-account-region)
backup-faq-pci-dss-compliant
  claim: AWS Backup is PCI-DSS compliant, which the FAQ says means you can use it to transfer payment information.
  scope: AWS Backup compliance (FAQ).
  link: [AWS Backup is PCI-DSS compliant](../facts/backup.md#backup-faq-pci-dss-compliant)
  link: [transfer payment information](../facts/backup.md#backup-faq-pci-dss-compliant)
backup-faq-per-service-capabilities-unchanged
  claim: Per-service backup features (S3 Replication, EBS snapshots, RDS snapshots, FSx backups, DynamoDB backups, Storage Gateway snapshots) remain unchanged when AWS Backup is used.
  scope: per-service backup capabilities (FAQ).
  link: [existing per-service backup capabilities remain unchanged](../facts/backup.md#backup-faq-per-service-capabilities-unchanged)
backup-faq-recovery-point-definition
  claim: A recovery point represents the content of a resource at a specified time and also holds metadata such as information about the resource, restore parameters and tags.
  scope: recovery point.
  link: [content of a resource at a specified time](../facts/backup.md#backup-faq-recovery-point-definition)
  link: [restore parameters, and tags](../facts/backup.md#backup-faq-recovery-point-definition)
backup-faq-restore-testing-compliance-evidence
  claim: After a restore testing plan runs, you can use the results to meet compliance and governance requirements by showing that restore tests completed and how long the restore jobs took.
  scope: restore testing results.
  link: [successful completion of restore test scenarios](../facts/backup.md#backup-faq-restore-testing-compliance-evidence)
  link: [completion times for the restore job](../facts/backup.md#backup-faq-restore-testing-compliance-evidence)
backup-faq-restore-testing-plan
  claim: You can automate restore testing with a restore testing plan that defines the frequency of restore tests, the target start time and the criteria for recovery point selection.
  scope: restore testing plan.
  link: [frequency of restore tests, target start time](../facts/backup.md#backup-faq-restore-testing-plan)
backup-faq-s3-continuous-35-days
  claim: Continuous backups of S3 resources in AWS Backup can restore to any point in time within the last 35 days.
  scope: continuous backups of S3 (FAQ); maximum; not adjustable.
  link: [within the last 35 days](../facts/backup.md#backup-faq-s3-continuous-35-days)
  say: within the last thirty-five days
backup-faq-s3-continuous-vs-periodic-use
  claim: Continuous S3 backups are useful for undoing accidental deletions, while periodic S3 snapshots help meet long-term data retention needs.
  scope: AWS Backup for S3.
  link: [undoing accidental deletions](../facts/backup.md#backup-faq-s3-continuous-vs-periodic-use)
  link: [long-term data retention needs](../facts/backup.md#backup-faq-s3-continuous-vs-periodic-use)
backup-faq-s3-existing-plan-tags-or-arns
  claim: To back up S3 with an existing backup plan, add your S3 resources to that plan using tags or S3 bucket ARNs.
  scope: AWS Backup for S3.
  link: [using tags or S3 bucket ARNs](../facts/backup.md#backup-faq-s3-existing-plan-tags-or-arns)
backup-faq-s3-first-full-then-incremental
  claim: For S3 backups, the first backup is a full snapshot and subsequent backups are incremental.
  scope: AWS Backup for S3.
  link: [The first backup is a full snapshot](../facts/backup.md#backup-faq-s3-first-full-then-incremental)
  link: [subsequent backups are incremental](../facts/backup.md#backup-faq-s3-first-full-then-incremental)
backup-faq-s3-native-vs-backup-roles
  claim: Backup administrators use AWS Backup to manage backups, restores and compliance across several AWS services; Amazon S3 Versioning, Object Lock and Replication help storage administrators preserve S3 data, and both sets of capabilities can be used together.
  scope: AWS Backup versus S3 native features.
  link: [Versioning , Object Lock , and Replication](../facts/backup.md#backup-faq-s3-native-vs-backup-roles)
  link: [use both sets of capabilities together](../facts/backup.md#backup-faq-s3-native-vs-backup-roles)
backup-faq-s3-no-cold-storage
  claim: AWS Backup for S3 supports backup access policies and encryption of backups with a different key, but does not support the cold storage tier.
  scope: AWS Backup for S3.
  link: [does not support cold storage tier](../facts/backup.md#backup-faq-s3-no-cold-storage)
  link: [encryption of backups with a different key](../facts/backup.md#backup-faq-s3-no-cold-storage)
backup-faq-s3-versioning-prerequisite
  claim: Turning on S3 Versioning is a prerequisite to creating backups of S3 buckets and objects; set a lifecycle expiration period for versions because AWS Backup stores all unexpired versions and S3 costs might otherwise increase.
  scope: AWS Backup for S3.
  link: [S3 Versioning is a prerequisite to creating backups](../facts/backup.md#backup-faq-s3-versioning-prerequisite)
backup-faq-s3-warm-tier-60-days-30-percent
  claim: The low-cost warm storage tier can reduce storage costs for eligible S3 backup data by up to 30%, and you can enable tiering for S3 backup data that has been in a backup vault for 60 days or longer, with a nominal one-time transition fee.
  scope: S3 backup data in AWS Backup (FAQ); minimum; not adjustable.
  link: [by up to 30%](../facts/backup.md#backup-faq-s3-warm-tier-60-days-30-percent)
  link: [in a backup vault for 60 days or longer](../facts/backup.md#backup-faq-s3-warm-tier-60-days-30-percent)
  say: by up to thirty percent | in a backup vault for sixty days or longer
backup-faq-s3-warm-tier-same-performance
  claim: The low-cost warm tier maintains the same performance and features as the standard tier, including ransomware protection, backup recovery and auditing capabilities.
  scope: low-cost warm storage tier for S3 backups.
  link: [same performance and features as the standard tier](../facts/backup.md#backup-faq-s3-warm-tier-same-performance)
backup-faq-s3-what-is-backed-up
  claim: AWS Backup can create continuous point-in-time backups or periodic backups of S3 buckets, including object data, object tags, access control lists (ACLs) and user-defined metadata.
  scope: AWS Backup for S3.
  link: [object data, object tags, access control lists (ACLs)](../facts/backup.md#backup-faq-s3-what-is-backed-up)
backup-faq-sns-alerting
  claim: AWS Backup integrates with Amazon SNS to automate alerting for backup activities, such as when a backup succeeds or a restore is initiated.
  scope: AWS Backup notifications.
  link: [integrates with Amazon Simple Notification Service](../facts/backup.md#backup-faq-sns-alerting)
  link: [a backup succeeds or a restore is initiated](../facts/backup.md#backup-faq-sns-alerting)
backup-faq-vault-encrypted-per-region
  claim: A backup vault is an encrypted storage location in your AWS account that stores and organizes recovery points, and you can create new backup vaults in each AWS Region where AWS Backup is available.
  scope: backup vault, per AWS Region.
  link: [encrypted storage location in your AWS account](../facts/backup.md#backup-faq-vault-encrypted-per-region)
  link: [each AWS Region where AWS Backup is available](../facts/backup.md#backup-faq-vault-encrypted-per-region)
backup-faq-vault-lock-centrally-protects-across-services
  claim: AWS Backup Vault Lock prevents manual deletion of backups and changes to backup lifecycle settings to help you centrally protect backups across AWS services.
  scope: AWS Backup Vault Lock.
  link: [prevents manual deletion of backups](../facts/backup.md#backup-faq-vault-lock-centrally-protects-across-services)
  link: [centrally protect backups across AWS services](../facts/backup.md#backup-faq-vault-lock-centrally-protects-across-services)
backup-faq-vault-lock-denies-in-locked-vault
  claim: In a locked vault, AWS Backup denies any attempt to delete a backup or update its lifecycle properties, even from the root account user.
  scope: vault with an active Vault Lock configuration; the vault is locked.
  link: [including the root account user](../facts/backup.md#backup-faq-vault-lock-denies-in-locked-vault)
  link: [AWS Backup denies the operation](../facts/backup.md#backup-faq-vault-lock-denies-in-locked-vault)
backup-faq-vault-lock-grace-time
  claim: Until the grace time expires you can update and remove the Vault Lock configuration, and once it expires AWS Backup will not allow any change to the configuration.
  scope: AWS Backup Vault Lock grace time; grace time is a number of days that you define.
  link: [the grace time has not expired](../facts/backup.md#backup-faq-vault-lock-grace-time)
  link: [will not allow any change to the configuration](../facts/backup.md#backup-faq-vault-lock-grace-time)
backup-faq-vault-lock-new-recovery-points-and-failed-jobs
  claim: Once Vault Lock is activated, AWS Backup protects all newly created recovery points in the vault against deletion and lifecycle changes, and fails every backup job whose retention period does not meet the acceptable retention periods.
  scope: vault with Vault Lock activated.
  link: [protect all newly created recovery points](../facts/backup.md#backup-faq-vault-lock-new-recovery-points-and-failed-jobs)
  link: [fail all backup jobs](../facts/backup.md#backup-faq-vault-lock-new-recovery-points-and-failed-jobs)
backup-faq-vault-lock-prevents-reencrypt
  claim: You can enable delete protection on backup vaults with AWS Backup Vault Lock to prevent malicious actors from re-encrypting your data.
  scope: backup vaults with Vault Lock.
  link: [Enable delete-protection on backup vaults](../facts/backup.md#backup-faq-vault-lock-prevents-reencrypt)
  link: [prevent malicious actors from re-encrypting your data](../facts/backup.md#backup-faq-vault-lock-prevents-reencrypt)
backup-faq-vault-lock-purpose-worm
  claim: AWS Backup Vault Lock helps you prevent changes to backup lifecycle and prevent manual deletion of backups, and it implements safeguards that check you store backups with a Write-Once-Read-Many (WORM) model.
  scope: AWS Backup Vault Lock.
  link: [prevent manual deletion of backups](../facts/backup.md#backup-faq-vault-lock-purpose-worm)
  link: [Write-Once-Read-Many (WORM) model](../facts/backup.md#backup-faq-vault-lock-purpose-worm)
backup-faq-vault-lock-three-properties
  claim: Vault Lock is an optional configuration at the backup vault level with three properties: minimum acceptable retention days, maximum acceptable retention days and grace time.
  scope: AWS Backup Vault Lock configuration.
  link: [three properties](../facts/backup.md#backup-faq-vault-lock-three-properties)
  link: [minimum acceptable retention days, maximum acceptable retention days](../facts/backup.md#backup-faq-vault-lock-three-properties)
backup-faq-vault-lock-vs-glacier-vault-lock
  claim: AWS Backup Vault Lock applies to data in an AWS Backup backup vault, while S3 Glacier Vault Lock applies to an individual S3 Glacier vault.
  scope: Vault Lock comparison (FAQ).
  link: [data residing in your AWS Backup backup vault](../facts/backup.md#backup-faq-vault-lock-vs-glacier-vault-lock)
  link: [applies to an individual S3 Glacier Vault](../facts/backup.md#backup-faq-vault-lock-vs-glacier-vault-lock)
backup-faq-vault-resource-based-policy
  claim: AWS Backup can set resource-based policies on backup vaults to control access to the vault and the backups in it.
  scope: backup vault access policy.
  link: [resource-based policies on backup vaults](../facts/backup.md#backup-faq-vault-resource-based-policy)
  link: [control access to the backup vault](../facts/backup.md#backup-faq-vault-resource-based-policy)
backup-faq-vmware-cold-storage-90-days
  claim: VMware backups can be moved to cold storage with lifecycle policies; backups in cold storage have a minimum of 90 days of storage, and backups deleted before 90 days incur a pro-rated charge for the remaining days.
  scope: VMware backups transitioned to cold storage; minimum; not adjustable.
  link: [minimum 90 days of storage](../facts/backup.md#backup-faq-vmware-cold-storage-90-days)
  link: [pro-rated charge equal to the storage charge](../facts/backup.md#backup-faq-vmware-cold-storage-90-days)
  say: minimum ninety days of storage
backup-faq-vmware-copy-to-other-account
  claim: You can copy VMware backups to another AWS account, and this is enabled by the integration of AWS Backup with AWS Organizations.
  scope: VMware backups.
  link: [copy VMware backups to another AWS account](../facts/backup.md#backup-faq-vmware-copy-to-other-account)
  link: [integration with AWS Organizations](../facts/backup.md#backup-faq-vmware-copy-to-other-account)
backup-faq-vmware-copy-to-other-region
  claim: The FAQ says you can store a copy of VMware backups in a different AWS Region from your production backups to meet business continuity, disaster recovery and compliance requirements.
  scope: VMware backups.
  link: [a different AWS Region from your production backups](../facts/backup.md#backup-faq-vmware-copy-to-other-region)
backup-faq-vmware-first-full-then-incremental-forever
  claim: AWS Backup supports first full, then incremental-forever backups of VMware VMs, created on demand or on the schedule of a backup plan.
  scope: VMware VMs.
  link: [first full, then incremental-forever backups](../facts/backup.md#backup-faq-vmware-first-full-then-incremental-forever)
backup-faq-what-is-backup
  claim: The FAQ describes AWS Backup as a fully managed service that centralizes and automates data protection across AWS services (for example S3, FSx, EC2 and RDS) and across hybrid VMware workloads.
  scope: AWS Backup service definition (FAQ).
  link: [centralizes and automates data protection](../facts/backup.md#backup-faq-what-is-backup)
backup-faq-why-durable-still-needs-backup
  claim: The FAQ says that even durable resources are susceptible to threats such as application bugs that cause accidental deletions or corruption.
  scope: data protection rationale (FAQ).
  link: [Even durable resources are susceptible to threats](../facts/backup.md#backup-faq-why-durable-still-needs-backup)
backup-feature-row-aurora
  claim: In the feature availability by resource table, Amazon Aurora has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, restore testing and logically air-gapped vault, and no check mark for full management, lifecycle to cold storage, item-level restore, backup search, backup tiering, malware protection or access points. The incremental backup check carries footnote 6: snapshots are full and incremental backup is offered through PITR. The cross-Region and cross-account checks carry footnote 3: Amazon RDS, Aurora, DocumentDB, and Neptune support cross-Region and cross-account snapshot copying in a single action.
  scope: Amazon Aurora row of the AWS Backup feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon Aurora](../facts/backup.md#backup-feature-row-aurora)
  link: [Amazon Aurora | ✓ 3 | ✓ 3 | ✓ | ✓ 6 | ✓](../facts/backup.md#backup-feature-row-aurora)
backup-feature-row-aurora-dsql
  claim: In the feature availability by resource table, Amazon Aurora DSQL has check marks for cross-Region backup, cross-account backup, full management, lifecycle to cold storage and logically air-gapped vault, and no check mark for AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, item-level restore or restore testing.
  scope: Amazon Aurora DSQL in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon Aurora DSQL](../facts/backup.md#backup-feature-row-aurora-dsql)
  link: [Amazon Aurora DSQL | ✓ | ✓](../facts/backup.md#backup-feature-row-aurora-dsql)
backup-feature-row-dynamodb
  claim: In the feature availability by resource table, the Amazon DynamoDB row (without advanced features) has check marks only for AWS Backup Audit Manager and restore testing, and no check mark for cross-Region backup, cross-account backup, full management or lifecycle to cold storage.
  scope: feature availability by resource.
  link: [Amazon DynamoDB](../facts/backup.md#backup-feature-row-dynamodb)
  link: [Lifecycle to cold storage](../facts/backup.md#backup-feature-row-dynamodb)
backup-feature-row-dynamodb-advanced
  claim: In the feature availability by resource table, DynamoDB with AWS Backup advanced features has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, full management, lifecycle to cold storage, restore testing and logically air-gapped vault, and no check mark for incremental backup, continuous backup and point-in-time restore or item-level restore.
  scope: DynamoDB with advanced features in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [DynamoDB with AWS Backup advanced features](../facts/backup.md#backup-feature-row-dynamodb-advanced)
backup-feature-row-ebs
  claim: In the feature availability by resource table, Amazon EBS has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, lifecycle to cold storage, item-level restore, restore testing, logically air-gapped vault, backup search and malware protection, and no check mark for continuous backup and point-in-time restore, full management, backup tiering or access points.
  scope: Amazon EBS in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon EBS](../facts/backup.md#backup-feature-row-ebs)
backup-feature-row-ec2
  claim: In the feature availability by resource table, Amazon EC2 has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, restore testing, logically air-gapped vault and malware protection, and no check mark for continuous backup and point-in-time restore, full management, lifecycle to cold storage, item-level restore, backup search, backup tiering or access points.
  scope: Amazon EC2 in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon EC2](../facts/backup.md#backup-feature-row-ec2)
  link: [Amazon EC2 | ✓ | ✓ | ✓ | ✓](../facts/backup.md#backup-feature-row-ec2)
backup-feature-row-efs
  claim: In the feature availability by resource table, Amazon EFS has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, full management, lifecycle to cold storage, item-level restore, restore testing and logically air-gapped vault, and no check mark for continuous backup and point-in-time restore, backup search, backup tiering, malware protection or access points.
  scope: Amazon EFS in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon EFS](../facts/backup.md#backup-feature-row-efs)
backup-feature-row-eks
  claim: In the feature availability by resource table, Amazon EKS has check marks for cross-Region backup, cross-account backup, full management, item-level restore and logically air-gapped vault, and no check mark for AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, lifecycle to cold storage, restore testing, backup search, backup tiering, malware protection or access points. The row label carries footnote 10: features for persistent storage backups (such as Amazon EBS) taken as part of Amazon EKS backups reflect the feature support of those resource types. The logically air-gapped vault check carries footnote 11: not currently available in Middle East (Bahrain) and Middle East (UAE).
  scope: Amazon EKS in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon EKS10](../facts/backup.md#backup-feature-row-eks)
  link: [Amazon EKS10 | ✓ | ✓](../facts/backup.md#backup-feature-row-eks)
backup-feature-row-fsx-ontap
  claim: In the feature availability by resource table, FSx for ONTAP has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, restore testing and logically air-gapped vault, and no check mark for continuous backup and point-in-time restore, full management, lifecycle to cold storage or item-level restore.
  scope: FSx for ONTAP in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [FSx for ONTAP](../facts/backup.md#backup-feature-row-fsx-ontap)
backup-feature-row-rds-instance
  claim: In the feature availability by resource table, Amazon RDS DB instance (single-AZ and Multi-AZ) has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, and restore testing, and no check mark for full management, lifecycle to cold storage, item-level restore or logically air-gapped vault. The cross-Region and cross-account checks carry footnote 3: Amazon RDS, Aurora, DocumentDB, and Neptune support cross-Region and cross-account snapshot copying in a single action, and RDS Multi-AZ database instances can be copied, but Multi-AZ clusters do not currently support any copy operations. The Audit Manager check carries footnote 4, which points to the RDS Multi-AZ backups page for the Regions where Backup Audit Manager support is available.
  scope: Amazon RDS DB instance in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon RDS DB instance](../facts/backup.md#backup-feature-row-rds-instance)
  link: [Amazon RDS DB instance (single-AZ and Multi-AZ)](../facts/backup.md#backup-feature-row-rds-instance)
backup-feature-row-redshift-serverless
  claim: In the feature availability by resource table, Amazon Redshift Serverless has a check mark only in the item-level restore column, and no check mark for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, full management, lifecycle to cold storage, restore testing or logically air-gapped vault.
  scope: Amazon Redshift Serverless in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon Redshift Serverless](../facts/backup.md#backup-feature-row-redshift-serverless)
  link: [✓](../facts/backup.md#backup-feature-row-redshift-serverless)
backup-feature-row-s3
  claim: In the feature availability by resource table, Amazon S3 has check marks for cross-Region backup, cross-account backup, AWS Backup Audit Manager, incremental backup, continuous backup and point-in-time restore, full management, item-level restore, restore testing, logically air-gapped vault, backup search, backup tiering, malware protection and access points, and no check mark for lifecycle to cold storage.
  scope: Amazon S3 in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [Amazon S3](../facts/backup.md#backup-feature-row-s3)
  link: [Amazon S3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓](../facts/backup.md#backup-feature-row-s3)
backup-feature-row-sap-hana
  claim: In the feature availability by resource table, SAP HANA databases on Amazon EC2 instances have check marks for cross-Region backup, cross-account backup, incremental backup, continuous backup and point-in-time restore, full management and lifecycle to cold storage, and no check mark for AWS Backup Audit Manager, item-level restore, restore testing or logically air-gapped vault. The incremental backup check carries footnote 6: snapshots are full and incremental backup is offered through PITR.
  scope: SAP HANA databases on Amazon EC2 instances in the feature availability by resource table; a blank cell means no check mark in the table.
  link: [SAP HANA databases on Amazon EC2 instances](../facts/backup.md#backup-feature-row-sap-hana)
  link: [SAP HANA databases on Amazon EC2 instances | ✓ | ✓](../facts/backup.md#backup-feature-row-sap-hana)
backup-feature-snapshot-copy-single-action-databases
  claim: Amazon RDS, Aurora, DocumentDB, and Neptune support cross-Region and cross-account snapshot copying in a single action; RDS Multi-AZ database instances can be copied, but Multi-AZ clusters do not currently support any copy operations.
  scope: snapshot copies of RDS, Aurora, DocumentDB and Neptune; not RDS Multi-AZ clusters, which support no copy operations.
  link: [Amazon RDS, Aurora, DocumentDB, and Neptune](../facts/backup.md#backup-feature-snapshot-copy-single-action-databases)
  link: [in a single action](../facts/backup.md#backup-feature-snapshot-copy-single-action-databases)
backup-feature-support-not-assumed-unless-stated
  claim: AWS Backup offers a set of features for all supported resources, and support for any other feature or service should not be assumed unless explicitly mentioned.
  scope: AWS Backup features.
  link: [should not be assumed](../facts/backup.md#backup-feature-support-not-assumed-unless-stated)
  link: [unless explicitly mentioned](../facts/backup.md#backup-feature-support-not-assumed-unless-stated)
backup-fsx-backups-kept-after-source-deleted
  claim: When AWS Backup manages FSx backups, it keeps them even after the source file system is deleted, which protects against accidental or malicious deletion.
  scope: FSx backups managed by AWS Backup.
  link: [even after the source file system is deleted](../facts/backup.md#backup-fsx-backups-kept-after-source-deleted)
  link: [accidental or malicious deletion](../facts/backup.md#backup-fsx-backups-kept-after-source-deleted)
backup-fsx-uses-native-fsx-backup-same-consistency
  claim: AWS Backup uses the built-in backup functionality of Amazon FSx, so backups taken from the AWS Backup console have the same file system consistency, performance and restore options as backups taken in the FSx console.
  scope: FSx file systems.
  link: [built-in backup functionality of Amazon FSx](../facts/backup.md#backup-fsx-uses-native-fsx-backup-same-consistency)
  link: [same restore options](../facts/backup.md#backup-fsx-uses-native-fsx-backup-same-consistency)
backup-full-management-backup-arns-for-backup-specific-policies
  claim: For resource types with full AWS Backup management, backup ARNs begin with arn:aws:backup instead of the source resource's ARN, so you can create access policies that apply to backups and not to the source resources.
  scope: resource types with full AWS Backup management.
  link: [Backup ARNs begin with](../facts/backup.md#backup-full-management-backup-arns-for-backup-specific-policies)
  link: [not the source resources](../facts/backup.md#backup-full-management-backup-arns-for-backup-specific-policies)
backup-full-management-central-billing-and-cost-allocation-tags
  claim: For resource types with full AWS Backup management, charges for AWS Backup, including storage, data transfers, restores and early deletion, appear under Backup on your bill instead of under each supported resource, and you can use Cost Explorer cost allocation tags.
  scope: resource types with full AWS Backup management.
  link: [Centralized backup billing](../facts/backup.md#backup-full-management-central-billing-and-cost-allocation-tags)
  link: [appear under "Backup"](../facts/backup.md#backup-full-management-central-billing-and-cost-allocation-tags)
backup-full-management-independent-encryption-vault-key
  claim: For resource types with full AWS Backup management, AWS Backup automatically encrypts backups with the KMS key of the backup vault instead of the source resource's key, which adds a layer of defense.
  scope: resource types with full AWS Backup management.
  link: [Independent encryption](../facts/backup.md#backup-full-management-independent-encryption-vault-key)
  link: [KMS key of your AWS Backup vault](../facts/backup.md#backup-full-management-independent-encryption-vault-key)
backup-gateway-connects-vmware-to-backup
  claim: Backup gateway is downloadable AWS Backup software that you deploy to your VMware infrastructure to connect your VMware VMs to AWS Backup.
  scope: VMware virtual machines.
  link: [Backup gateway](../facts/backup.md#backup-gateway-connects-vmware-to-backup)
  link: [downloadable AWS Backup software](../facts/backup.md#backup-gateway-connects-vmware-to-backup)
backup-guardduty-malware-scanning-of-recovery-points
  claim: AWS Backup integrates with Amazon GuardDuty to scan recovery points automatically for malware, which helps detect potential malware in EC2, EBS and S3 backups.
  scope: AWS Backup malware scanning.
  link: [automated malware scanning of your recovery points](../facts/backup.md#backup-guardduty-malware-scanning-of-recovery-points)
  link: [EC2, EBS, and S3 backups](../facts/backup.md#backup-guardduty-malware-scanning-of-recovery-points)
backup-iam-default-service-role-console-auto-cli-manual
  claim: The default service role, named AWSBackupDefaultServiceRole, is created automatically when you use the AWS Management Console but must be created manually when you use the AWS CLI, and it contains the managed policies AWSBackupServiceRolePolicyForBackup and AWSBackupServiceRolePolicyForRestores.
  scope: AWS Backup default service role; default; not adjustable.
  link: [created when you use the AWS Management Console](../facts/backup.md#backup-iam-default-service-role-console-auto-cli-manual)
  link: [AWSBackupDefaultServiceRole](../facts/backup.md#backup-iam-default-service-role-console-auto-cli-manual)
backup-iam-narrow-roles-and-who-can-pass-them
  claim: You can control access to backups with narrowly scoped roles and by specifying who can pass the role to AWS Backup, for example a role that only backs up RDS databases that only RDS database owners can pass.
  scope: AWS Backup service roles.
  link: [defining narrowly scoped roles](../facts/backup.md#backup-iam-narrow-roles-and-who-can-pass-them)
  link: [who can pass that role to AWS Backup](../facts/backup.md#backup-iam-narrow-roles-and-who-can-pass-them)
backup-iam-role-passed-for-plans-on-demand-copy-restore
  claim: You must pass a service role when you assign resources to a backup plan or run an on-demand backup, copy or restore, and AWS Backup uses that role to create, tag and delete resources in your account.
  scope: AWS Backup service role.
  link: [you must pass a service role](../facts/backup.md#backup-iam-role-passed-for-plans-on-demand-copy-restore)
  link: [create, tag, and delete resources in your account](../facts/backup.md#backup-iam-role-passed-for-plans-on-demand-copy-restore)
backup-iam-service-role-must-trust-aws-backup
  claim: The role you pass to AWS Backup must have an IAM policy with the permissions for backup operations such as creating, restoring or expiring backups, with different permissions for each supported service, and AWS Backup must be a trusted entity so it can assume the role.
  scope: AWS Backup service role.
  link: [AWS Backup listed as a trusted entity](../facts/backup.md#backup-iam-service-role-must-trust-aws-backup)
  link: [Different permissions are required](../facts/backup.md#backup-iam-service-role-must-trust-aws-backup)
backup-incremental-aurora-only-through-continuous-backups
  claim: Some resources, such as Aurora, offer incremental backup only through continuous backups and point-in-time restore, not through snapshot-based backups.
  scope: Aurora backups.
  link: [only through continuous backups and point-in-time restore (PITR)](../facts/backup.md#backup-incremental-aurora-only-through-continuous-backups)
  link: [not through snapshot-based backups](../facts/backup.md#backup-incremental-aurora-only-through-continuous-backups)
backup-incremental-first-full-then-changes
  claim: For supported resource types, AWS Backup stores periodic backups incrementally: the first backup is a full copy and each later backup stores only the changes.
  scope: resource types that support incremental backups; supported resource types only.
  link: [backs up a full copy of your data](../facts/backup.md#backup-incremental-first-full-then-changes)
  link: [only the changes to your AWS resources](../facts/backup.md#backup-incremental-first-full-then-changes)
backup-incremental-not-all-types-full-copy
  claim: Not all resource types support incremental backups; for those that do not, each backup is a full copy, which can cost more in storage.
  scope: resource types without incremental backup support.
  link: [each backup is a full copy](../facts/backup.md#backup-incremental-not-all-types-full-copy)
  link: [higher storage costs](../facts/backup.md#backup-incremental-not-all-types-full-copy)
backup-incremental-requires-earlier-backup-in-vault-or-region
  claim: A backup of a fully managed resource can be incremental only if its vault also contains an earlier backup; other resource types can have incremental backups as long as there is a previous backup of the resource in the same Region.
  scope: incremental backups, vaults and Regions.
  link: [only be incremental if the vault](../facts/backup.md#backup-incremental-requires-earlier-backup-in-vault-or-region)
  link: [within the same Region](../facts/backup.md#backup-incremental-requires-earlier-backup-in-vault-or-region)
backup-incremental-restore-full-even-after-first-backup-expired
  claim: Every backup after the first full one is incremental, but all AWS Backup backups keep the reference data needed for a full restore, even after the original full backup has reached the end of its lifecycle and been deleted.
  scope: incremental backups.
  link: [reference data to allow a full restore](../facts/backup.md#backup-incremental-restore-full-even-after-first-backup-expired)
  link: [reached the end of its lifecycle](../facts/backup.md#backup-incremental-restore-full-even-after-first-backup-expired)
backup-job-start-retry-every-10-minutes
  claim: During the start window, if AWS Backup receives an error that allows a backup job to be retried, it retries beginning the job at least every 10 minutes until the job begins or its status changes to EXPIRED when the start window is over.
  scope: backup jobs during the start window; only for errors that allow the job to be retried.
  link: [at least every 10 minutes](../facts/backup.md#backup-job-start-retry-every-10-minutes)
  say: at least every ten minutes
backup-lag-concurrent-copies-aurora-20
  claim: For logically air-gapped vaults, the maximum is 20 concurrent copies for Aurora.
  scope: concurrent copies to logically air-gapped vaults, resource type Aurora; maximum; not adjustable.
  link: [20 concurrent copies](../facts/backup.md#backup-lag-concurrent-copies-aurora-20)
  say: twenty concurrent copies
backup-lag-concurrent-copies-ebs-20
  claim: For logically air-gapped vaults, the maximum is 20 concurrent copies for Amazon EBS. For EC2, the EBS concurrent copy limit applies to any snapshots copied as part of an AMI copy.
  scope: concurrent copies to logically air-gapped vaults, resource type EBS; maximum; not adjustable; the EBS limit also applies to snapshots copied as part of an EC2 AMI copy.
  link: [20 concurrent copies](../facts/backup.md#backup-lag-concurrent-copies-ebs-20)
  say: twenty concurrent copies
backup-lag-concurrent-copies-fsx-5
  claim: For logically air-gapped vaults, the maximum is 5 concurrent copies for FSx.
  scope: concurrent copies to logically air-gapped vaults, resource type FSx; maximum; not adjustable.
  link: [5 concurrent copies](../facts/backup.md#backup-lag-concurrent-copies-fsx-5)
  say: five concurrent copies
backup-lag-concurrent-copies-storage-gateway-5
  claim: For logically air-gapped vaults, the maximum is 5 concurrent copies for Storage Gateway.
  scope: concurrent copies to logically air-gapped vaults, resource type Storage Gateway; maximum; not adjustable.
  link: [5 concurrent copies](../facts/backup.md#backup-lag-concurrent-copies-storage-gateway-5)
  say: five concurrent copies
backup-lag-min-retention-7-days
  claim: When you create a logically air-gapped vault, the minimum retention period is the shortest time a backup can be retained in the vault, backups with shorter retention cannot be copied into it, and the minimum value allowed is 7 days.
  scope: minimum retention period set when creating a logically air-gapped vault; minimum; not adjustable; values for months and years meet this minimum.
  link: [7 days](../facts/backup.md#backup-lag-min-retention-7-days)
  say: seven days
backup-lag-primary-backup-direct-single-copy
  claim: A logically air-gapped vault can be the primary backup destination in the same account for scheduled and on-demand jobs, which removes the need to keep separate copies in a standard vault and a logically air-gapped vault.
  scope: logically air-gapped vault primary backup.
  link: [primary backup destination within the same account](../facts/backup.md#backup-lag-primary-backup-direct-single-copy)
  link: [separate copies in both a standard backup vault](../facts/backup.md#backup-lag-primary-backup-direct-single-copy)
backup-lag-primary-backup-ebs-ec2-aurora-fsx-temp-recovery-point
  claim: Resources such as EBS, EC2, Aurora and FSx cannot back up directly to a logically air-gapped vault: AWS Backup creates a temporary recovery point in the backup vault and then automatically copies it to the logically air-gapped vault.
  scope: resource types not supporting full AWS Backup management.
  link: [cannot back up directly to logically air-gapped vaults](../facts/backup.md#backup-lag-primary-backup-ebs-ec2-aurora-fsx-temp-recovery-point)
  link: [temporary recovery point in your backup vault](../facts/backup.md#backup-lag-primary-backup-ebs-ec2-aurora-fsx-temp-recovery-point)
backup-lag-primary-backup-fully-managed-direct-no-vault-copy
  claim: Resource types with full AWS Backup management, such as EFS, S3 and DynamoDB with advanced features, can back up directly to a logically air-gapped vault: no recovery point is created in the backup vault and no copy operation is required.
  scope: resource types supporting full AWS Backup management.
  link: [can back up directly](../facts/backup.md#backup-lag-primary-backup-fully-managed-direct-no-vault-copy)
  link: [no copy operation is required](../facts/backup.md#backup-lag-primary-backup-fully-managed-direct-no-vault-copy)
backup-lag-primary-backup-no-direct-cross-account-or-region
  claim: You cannot create backups directly into a logically air-gapped vault cross-account or cross-Region; AWS Backup recommends a logically air-gapped vault in the same Region for faster recovery without a copy.
  scope: logically air-gapped vault primary backup.
  link: [cannot create backups directly cross-account or cross-Region](../facts/backup.md#backup-lag-primary-backup-no-direct-cross-account-or-region)
  link: [in the same Region](../facts/backup.md#backup-lag-primary-backup-no-direct-cross-account-or-region)
backup-lag-primary-backup-no-new-charge
  claim: The logically air-gapped vault primary backup feature has no new pricing: you pay only for backups stored in logically air-gapped vaults and, for applicable resources, temporary snapshots at prevailing rates.
  scope: logically air-gapped vault primary backup.
  link: [no new pricing for this feature](../facts/backup.md#backup-lag-primary-backup-no-new-charge)
  link: [temporary snapshots](../facts/backup.md#backup-lag-primary-backup-no-new-charge)
backup-lag-service-owned-key-rotation-90-days
  claim: The default rotation policy for the service-owned encryption keys of logically air-gapped vaults is 90 days, and you can request rotation once every 6 months through a support ticket.
  scope: service-owned encryption keys of logically air-gapped vaults; default; adjustable; rotation on request through a support ticket.
  link: [90 days](../facts/backup.md#backup-lag-service-owned-key-rotation-90-days)
  link: [once every 6 months](../facts/backup.md#backup-lag-service-owned-key-rotation-90-days)
  say: ninety days | once every six months
backup-lag-vault-aws-owned-key-recommended
  claim: AWS Backup recommends using AWS owned keys with logically air-gapped vaults.
  scope: logically air-gapped vault encryption.
  link: [recommends using AWS owned keys](../facts/backup.md#backup-lag-vault-aws-owned-key-recommended)
  link: [logically air-gapped vaults](../facts/backup.md#backup-lag-vault-aws-owned-key-recommended)
backup-lag-vault-definition-secondary-vault-rto
  claim: A logically air-gapped vault is a secondary type of vault with additional security beyond a standard backup vault and the ability to share vault access with other accounts, so recovery time can be faster and more flexible after an incident.
  scope: logically air-gapped vault.
  link: [secondary type of vault](../facts/backup.md#backup-lag-vault-definition-secondary-vault-rto)
  link: [increased security beyond a standard backup vault](../facts/backup.md#backup-lag-vault-definition-secondary-vault-rto)
backup-lag-vault-delete-only-when-empty-key-deleted-after-seven-days
  claim: A logically air-gapped vault cannot be deleted while it still contains backups, and deleting the vault also deletes its key seven days later.
  scope: logically air-gapped vault deletion.
  link: [cannot be deleted if they still contain backups](../facts/backup.md#backup-lag-vault-delete-only-when-empty-key-deleted-after-seven-days)
  link: [seven days after the vault is deleted](../facts/backup.md#backup-lag-vault-delete-only-when-empty-key-deleted-after-seven-days)
backup-lag-vault-encryption-key-and-compliance-lock
  claim: Each logically air-gapped vault is encrypted with an AWS owned key (the default) or optionally a customer managed KMS key, and each vault is equipped with Vault Lock compliance mode.
  scope: logically air-gapped vault; default; compliance mode is always on.
  link: [AWS owned key (default)](../facts/backup.md#backup-lag-vault-encryption-key-and-compliance-lock)
  link: [Vault Lock's compliance mode](../facts/backup.md#backup-lag-vault-encryption-key-and-compliance-lock)
backup-lag-vault-jobs-fail-outside-min-max-retention
  claim: The retention period specified in your backup plan must be compatible with the minimum and maximum retention periods configured for your logically air-gapped vault; the AWS troubleshooting guidance names an incompatible retention period as the possible cause when backup jobs or copy jobs fail.
  scope: logically air-gapped vault; retention period of the job outside the vault's minimum or maximum retention.
  link: [Backup jobs or copy jobs fail](../facts/backup.md#backup-lag-vault-jobs-fail-outside-min-max-retention)
  link: [minimum or maximum retention settings](../facts/backup.md#backup-lag-vault-jobs-fail-outside-min-max-retention)
backup-lag-vault-key-chosen-at-creation-only
  claim: You can select the KMS key of a logically air-gapped vault only during vault creation; all backups in the vault are encrypted with that key and you cannot change or migrate the vault to a different key.
  scope: logically air-gapped vault encryption key.
  link: [an AWS KMS encryption key during vault creation](../facts/backup.md#backup-lag-vault-key-chosen-at-creation-only)
  link: [cannot change or migrate your vaults](../facts/backup.md#backup-lag-vault-key-chosen-at-creation-only)
backup-lag-vault-lag-to-lag-copy-on-demand-only
  claim: You can copy a backup from one logically air-gapped vault to another only on demand, not on a schedule in a backup plan, and you can copy from a logically air-gapped vault to a standard vault only if the copy is encrypted with a customer managed key.
  scope: copies out of a logically air-gapped vault.
  link: [cannot be scheduled in a backup plan](../facts/backup.md#backup-lag-vault-lag-to-lag-copy-on-demand-only)
  link: [encrypted with a customer managed key](../facts/backup.md#backup-lag-vault-lag-to-lag-copy-on-demand-only)
backup-lag-vault-mpa-recovery-when-owner-inaccessible
  claim: You can integrate logically air-gapped vaults with multi-party approval (MPA) to recover the backups in the vault even if the vault-owning account is inaccessible.
  scope: logically air-gapped vault with multi-party approval.
  link: [even if the vault-owning account is inaccessible](../facts/backup.md#backup-lag-vault-mpa-recovery-when-owner-inaccessible)
  link: [Multi-party approval](../facts/backup.md#backup-lag-vault-mpa-recovery-when-owner-inaccessible)
backup-lag-vault-owner-account-closed-access-via-mpa
  claim: If the account that owns a logically air-gapped vault is closed, you can still restore or copy its backups through multi-party approval until the post-closure period ends; after that the backups are no longer accessible.
  scope: logically air-gapped vault with multi-party approval.
  link: [until the post-closure period ends](../facts/backup.md#backup-lag-vault-owner-account-closed-access-via-mpa)
  link: [no longer accessible](../facts/backup.md#backup-lag-vault-owner-account-closed-access-via-mpa)
backup-lag-vault-ram-share-restore-in-other-account
  claim: You can use AWS RAM to share a logically air-gapped vault with other AWS accounts, including accounts in other organizations, so the backups can be restored from an account the vault is shared with.
  scope: logically air-gapped vault with AWS RAM.
  link: [AWS Resource Access Manager (RAM)](../facts/backup.md#backup-lag-vault-ram-share-restore-in-other-account)
  link: [accounts in other organizations](../facts/backup.md#backup-lag-vault-ram-share-restore-in-other-account)
backup-lag-vault-recommend-cross-region-copies
  claim: For greater resiliency, AWS recommends creating cross-Region copies in logically air-gapped vaults, in the same or separate accounts.
  scope: logically air-gapped vault.
  link: [creating cross-Region copies in logically air-gapped vaults](../facts/backup.md#backup-lag-vault-recommend-cross-region-copies)
  link: [same or separate accounts](../facts/backup.md#backup-lag-vault-recommend-cross-region-copies)
backup-lag-vault-restore-access-vault-view-delete
  claim: Deleting a restore access backup vault, which is a view of an underlying logically air-gapped vault with no recovery points of its own, is allowed from the recovery account even in FAILED state, and Vault Lock compliance mode does not block it.
  scope: restore access backup vault.
  link: [a view of an underlying logically air-gapped vault](../facts/backup.md#backup-lag-vault-restore-access-vault-view-delete)
  link: [does not block this deletion](../facts/backup.md#backup-lag-vault-restore-access-vault-view-delete)
backup-lag-vault-restore-from-owner-or-shared-account
  claim: You can restore a backup in a logically air-gapped vault from the account that owns the vault or from any account the vault is shared with.
  scope: logically air-gapped vault.
  link: [from either the account that owns the vault](../facts/backup.md#backup-lag-vault-restore-from-owner-or-shared-account)
  link: [any account with which the vault is shared](../facts/backup.md#backup-lag-vault-restore-from-owner-or-shared-account)
backup-lag-vault-share-with-account-ids-only
  claim: A logically air-gapped vault can be shared only with individual AWS account IDs, in your organization or in another organization; it cannot be shared with an entire organization or with organizational units.
  scope: sharing a logically air-gapped vault through AWS RAM.
  link: [only individual account IDs are supported](../facts/backup.md#backup-lag-vault-share-with-account-ids-only)
  link: [cannot be shared with an entire organization](../facts/backup.md#backup-lag-vault-share-with-account-ids-only)
backup-lag-vault-shared-account-view-restore-not-copy
  claim: A copy of a backup in a logically air-gapped vault can be created from the account to which the vault belongs; accounts with which the vault has been shared can view or restore a backup, but not create a copy.
  scope: accounts a logically air-gapped vault is shared with.
  link: [but not to create a copy](../facts/backup.md#backup-lag-vault-shared-account-view-restore-not-copy)
  link: [from the account to which the vault belongs](../facts/backup.md#backup-lag-vault-shared-account-view-restore-not-copy)
backup-lag-vault-source-key-fully-managed-cmk-or-aws-managed
  claim: When you create or copy a backup of a fully managed resource type into a logically air-gapped vault, the source resource can be encrypted by a customer managed key or an AWS managed key.
  scope: fully managed resource types, logically air-gapped vault.
  link: [by an AWS managed key](../facts/backup.md#backup-lag-vault-source-key-fully-managed-cmk-or-aws-managed)
  link: [fully managed resource type](../facts/backup.md#backup-lag-vault-source-key-fully-managed-cmk-or-aws-managed)
backup-lag-vault-source-key-not-fully-managed-needs-cmk
  claim: When you create or copy a backup of a resource type that is not fully managed into a logically air-gapped vault, the source must be encrypted with a customer managed key; AWS managed keys are not supported for those resources.
  scope: resource types not fully managed by AWS Backup, logically air-gapped vault.
  link: [must be encrypted with a customer managed key](../facts/backup.md#backup-lag-vault-source-key-not-fully-managed-needs-cmk)
  link: [not fully managed resources are not supported](../facts/backup.md#backup-lag-vault-source-key-not-fully-managed-needs-cmk)
backup-lag-vault-standard-vault-is-primary-type
  claim: A standard backup vault is the primary type of vault in AWS Backup and each backup is stored in a backup vault when the backup is created; a logically air-gapped vault stores primary backups or copies of backups first created in a standard backup vault.
  scope: standard backup vault, logically air-gapped vault.
  link: [primary and standard type of vault](../facts/backup.md#backup-lag-vault-standard-vault-is-primary-type)
  link: [stored within a standard backup vault](../facts/backup.md#backup-lag-vault-standard-vault-is-primary-type)
backup-lag-vault-stored-in-backup-service-owned-account
  claim: A logically air-gapped vault stores its backups in an AWS Backup service owned account, which is why the backups appear as shared outside your organization in CloudTrail modify attribute items.
  scope: logically air-gapped vault.
  link: [AWS Backup service owned account](../facts/backup.md#backup-lag-vault-stored-in-backup-service-owned-account)
  link: [shared outside your organization](../facts/backup.md#backup-lag-vault-stored-in-backup-service-owned-account)
backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported
  claim: Unencrypted Aurora, DocumentDB and Neptune clusters are not supported for a logically air-gapped vault, because they do not support encryption of unencrypted DB cluster snapshots.
  scope: logically air-gapped vault, Aurora, DocumentDB, Neptune.
  link: [Unencrypted Amazon Aurora](../facts/backup.md#backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported)
  link: [are not supported for logically air-gapped vault](../facts/backup.md#backup-lag-vault-unencrypted-aurora-docdb-neptune-unsupported)
backup-lag-vs-standard-billing-row
  claim: All storage and data transfer charges of a logically air-gapped vault occur under AWS Backup, while for a standard vault the charges of resource types fully managed by AWS Backup occur under AWS Backup and other resource types are billed under their own services.
  scope: standard backup vault versus logically air-gapped vault.
  link: [All billing charges from these vaults](../facts/backup.md#backup-lag-vs-standard-billing-row)
  link: [occur under "AWS Backup"](../facts/backup.md#backup-lag-vs-standard-billing-row)
backup-lag-vs-standard-restore-row
  claim: In the comparison table, backups in a standard backup vault can be restored by the same account to which the vault belongs, while backups in a logically air-gapped vault can be restored by a different account than the one to which the vault belongs if the vault is shared with that account.
  scope: standard backup vault versus logically air-gapped vault.
  link: [the same account to which the vault belongs](../facts/backup.md#backup-lag-vs-standard-restore-row)
  link: [restored by a different account](../facts/backup.md#backup-lag-vs-standard-restore-row)
backup-lag-vs-standard-security-row
  claim: A logically air-gapped vault is always locked with a vault lock in compliance mode and encrypts with an AWS owned key or a customer managed key, while a standard vault can optionally use a vault lock in compliance or governance mode.
  scope: standard backup vault versus logically air-gapped vault.
  link: [always locked with a vault lock](../facts/backup.md#backup-lag-vs-standard-security-row)
  link: [in compliance or governance mode](../facts/backup.md#backup-lag-vs-standard-security-row)
backup-lag-vs-standard-sharing-row
  claim: A standard backup vault is not compatible with AWS RAM and its access is managed through policies and AWS Organizations, while a logically air-gapped vault can optionally be shared across accounts using AWS RAM.
  scope: standard backup vault versus logically air-gapped vault.
  link: [Not compatible with AWS RAM](../facts/backup.md#backup-lag-vs-standard-sharing-row)
  link: [optionally be shared across accounts using AWS RAM](../facts/backup.md#backup-lag-vs-standard-sharing-row)
backup-legal-hold-expired-backups-deleted-24-hours
  claim: Removing a legal hold eliminates it from all backups to which it was attached, and any backups that expired during the legal hold are deleted within 24 hours after the legal hold is removed.
  scope: backups that expired while under a legal hold; maximum.
  link: [within 24 hours](../facts/backup.md#backup-legal-hold-expired-backups-deleted-24-hours)
  say: within twenty-four hours
backup-legal-hold-max-50-active-per-account
  claim: Each account can have a maximum of 50 legal holds active at one time.
  scope: per account, active at one time; maximum; not adjustable.
  link: [maximum of 50 legal holds](../facts/backup.md#backup-legal-hold-max-50-active-per-account)
  say: fifty legal holds
backup-legal-hold-multiple-holds-backup-kept-until-all-removed
  claim: A backup cannot be deleted as long as it has at least one legal hold; after all legal holds on it are removed, it is subject to its retention lifecycle again.
  scope: AWS Backup legal holds.
  link: [cannot be deleted as long as it has](../facts/backup.md#backup-legal-hold-multiple-holds-backup-kept-until-all-removed)
  link: [all legal holds on a backup are removed](../facts/backup.md#backup-legal-hold-multiple-holds-backup-kept-until-all-removed)
backup-legal-hold-no-expiry-released-by-user-complements-vault-lock
  claim: A legal hold gives additional protection against deletion of individual recovery points, does not expire, and stays active until a user with sufficient permissions releases it, whereas Vault Lock protects the vault.
  scope: AWS Backup legal holds and Vault Lock.
  link: [does not expire](../facts/backup.md#backup-legal-hold-no-expiry-released-by-user-complements-vault-lock)
  link: [released by a user with sufficient permissions](../facts/backup.md#backup-legal-hold-no-expiry-released-by-user-complements-vault-lock)
backup-legal-hold-not-for-continuous-backups
  claim: Legal holds can be applied to backups created by AWS Backup if their lifecycles allow it, but legal holds do not apply to continuous backups.
  scope: AWS Backup legal holds.
  link: [Legal holds do not apply to continuous backups](../facts/backup.md#backup-legal-hold-not-for-continuous-backups)
  link: [one or more backups](../facts/backup.md#backup-legal-hold-not-for-continuous-backups)
backup-legal-hold-only-original-backup-not-copies
  claim: Legal holds apply only to the original backup; a backup copied across Regions or accounts does not carry its legal hold, and only recovery points created by AWS Backup can be part of a legal hold.
  scope: AWS Backup legal holds.
  link: [apply only to the original backup](../facts/backup.md#backup-legal-hold-only-original-backup-not-copies)
  link: [does not retain or carry its legal hold](../facts/backup.md#backup-legal-hold-only-original-backup-not-copies)
backup-legal-hold-prevents-deletion-delays-lifecycle
  claim: A legal hold is an administrative tool that prevents backups from being deleted while under the hold, and lifecycle policies that would alter the backup status are delayed until the hold is removed.
  scope: AWS Backup legal holds.
  link: [backups under a hold cannot be deleted](../facts/backup.md#backup-legal-hold-prevents-deletion-delays-lifecycle)
  link: [delayed until the legal hold is removed](../facts/backup.md#backup-legal-hold-prevents-deletion-delays-lifecycle)
backup-lifecycle-restore-until-end
  claim: The backup lifecycle is the number of days a backup is stored, and a backup can be restored until the end of its lifecycle.
  scope: AWS Backup lifecycle.
  link: [until the end of their lifecycle](../facts/backup.md#backup-lifecycle-restore-until-end)
  link: [number of days you specify](../facts/backup.md#backup-lifecycle-restore-until-end)
backup-malware-billed-by-guardduty-not-backup
  claim: Malware protection for AWS Backup is provided and billed by Amazon GuardDuty; you do not see AWS Backup charges for it and all usage appears under Amazon GuardDuty billing.
  scope: AWS Backup malware protection.
  link: [provided and billed by Amazon GuardDuty](../facts/backup.md#backup-malware-billed-by-guardduty-not-backup)
  link: [will not see any AWS Backup charges](../facts/backup.md#backup-malware-billed-by-guardduty-not-backup)
backup-malware-incremental-baseline-365-days
  claim: Even when incremental malware scanning is selected, AWS Backup performs a full scan if the baseline recovery point was scanned more than 365 days ago, because Amazon GuardDuty retains finding information for only 365 days.
  scope: incremental malware scans in AWS Backup; maximum.
  link: [more than 365 days ago](../facts/backup.md#backup-malware-incremental-baseline-365-days)
  say: more than three hundred sixty-five days ago
backup-malware-incremental-vs-full-scans
  claim: Incremental scans analyze only the data that changed between the target and base recovery point and are faster and cheaper, while full scans examine the entire recovery point, take longer and cost more.
  scope: AWS Backup malware scans.
  link: [only the data that changed](../facts/backup.md#backup-malware-incremental-vs-full-scans)
  link: [examine the entire recovery point](../facts/backup.md#backup-malware-incremental-vs-full-scans)
backup-malware-on-demand-scan-find-last-clean-backup
  claim: AWS Backup recommends on-demand scans to identify your last clean backup, and a full scan before a restore so the entire backup is examined with the latest threat detection model.
  scope: AWS Backup malware protection.
  link: [identify your last clean backup](../facts/backup.md#backup-malware-on-demand-scan-find-last-clean-backup)
  link: [use a full scan](../facts/backup.md#backup-malware-on-demand-scan-find-last-clean-backup)
backup-malware-scan-resource-types-selected-per-plan
  claim: When you configure malware protection in a backup plan you specify which resource types to scan (EC2, EBS, S3 or all supported resources) and the scan type (full or incremental); malware scanning applies only to the selected resource types.
  scope: AWS Backup malware protection in backup plans.
  link: [specify which resource types to scan](../facts/backup.md#backup-malware-scan-resource-types-selected-per-plan)
  link: [applies only to your selected resource types](../facts/backup.md#backup-malware-scan-resource-types-selected-per-plan)
backup-malware-scan-results-threats-found-or-not
  claim: A malware scan result of NO_THREATS_FOUND means no potential malware was detected, while THREATS_FOUND means potential malware was discovered.
  scope: AWS Backup malware scan results.
  link: [NO_THREATS_FOUND](../facts/backup.md#backup-malware-scan-results-threats-found-or-not)
  link: [THREATS_FOUND](../facts/backup.md#backup-malware-scan-results-threats-found-or-not)
backup-malware-scanning-by-guardduty-automate-or-on-demand
  claim: Malware scanning of your backups is provided by Amazon GuardDuty Malware Protection, which lets you automate scanning of recovery points through existing backup workflows or start on-demand scans of previously created backups.
  scope: AWS Backup malware protection.
  link: [provided by Amazon GuardDuty Malware Protection](../facts/backup.md#backup-malware-scanning-by-guardduty-automate-or-on-demand)
  link: [initiate on-demand scans of previously created backups](../facts/backup.md#backup-malware-scanning-by-guardduty-automate-or-on-demand)
backup-malware-two-iam-roles-required
  claim: AWS Backup malware scanning requires two IAM roles; the second is a new scanner role with the AWSBackupGuardDutyRolePolicyForScans managed policy that trusts malware-protection.guardduty.amazonaws.com.
  scope: AWS Backup malware protection.
  link: [requires two IAM roles](../facts/backup.md#backup-malware-two-iam-roles-required)
  link: [trusts malware-protection.guardduty.amazonaws.com](../facts/backup.md#backup-malware-two-iam-roles-required)
backup-metering-aurora-continuous-snapshots-no-storage-charge
  claim: During the configured retention period for Aurora continuous backups, up to 35 days, snapshots do not incur a storage charge, and snapshots retained past this window are charged as full backups.
  scope: snapshots of Aurora with continuous backups in AWS Backup; maximum.
  link: [up to 35 days](../facts/backup.md#backup-metering-aurora-continuous-snapshots-no-storage-charge)
  link: [charged as full backups](../facts/backup.md#backup-metering-aurora-continuous-snapshots-no-storage-charge)
backup-metering-copy-charged-once-recovery-point-created
  claim: You are charged for a copy job only once a recovery point has been created in the destination vault, and there is no charge when a copy job fails and no recovery point is created.
  scope: AWS Backup copy jobs.
  link: [charged once a recovery point has been created](../facts/backup.md#backup-metering-copy-charged-once-recovery-point-created)
  link: [no charge when a copy job fails](../facts/backup.md#backup-metering-copy-charged-once-recovery-point-created)
backup-metering-copy-data-transfer-account-by-management
  claim: For cross-account and cross-Region copies, the source account sees the data transfer charges for resources fully managed by AWS Backup, and the destination account sees them for resources that are not fully managed.
  scope: cross-account and cross-Region copies, by whether the resource type is fully managed by AWS Backup; depends on whether the resource type supports full AWS Backup management.
  link: [source account will see the data transfer charges](../facts/backup.md#backup-metering-copy-data-transfer-account-by-management)
  link: [destination account will see the data transfer charges](../facts/backup.md#backup-metering-copy-data-transfer-account-by-management)
backup-metering-warm-retention-one-week-avoid-full-backups
  claim: To avoid additional charges, configure your retention policy with a warm storage duration of at least one week.
  scope: retention policy of backups for resource types with incremental backups; minimum; a recommendation; example uses daily backups retained for one day.
  link: [at least one week](../facts/backup.md#backup-metering-warm-retention-one-week-avoid-full-backups)
  say: at least one week
backup-monitoring-cloudwatch-eventbridge-cloudtrail-sns
  claim: AWS Backup integrates with CloudWatch for metrics and alarms, EventBridge for backup events, CloudTrail for a consolidated view of backup activity logs, and SNS for backup activity notifications such as a succeeded backup.
  scope: AWS Backup monitoring.
  link: [track metrics and create alarms](../facts/backup.md#backup-monitoring-cloudwatch-eventbridge-cloudtrail-sns)
  link: [consolidated view of backup activity logs](../facts/backup.md#backup-monitoring-cloudwatch-eventbridge-cloudtrail-sns)
backup-mpa-capability-from-organizations-for-lag-vaults
  claim: Multi-party approval is a capability from AWS Organizations that you can add to logically air-gapped vaults, to protect critical operations through a distributed approval process.
  scope: multi-party approval.
  link: [a capability from AWS Organizations](../facts/backup.md#backup-mpa-capability-from-organizations-for-lag-vaults)
  link: [distributed approval process](../facts/backup.md#backup-mpa-capability-from-organizations-for-lag-vaults)
backup-mpa-no-extra-cost-storage-charges-apply
  claim: There is no additional cost for multi-party approval teams with logically air-gapped vaults, but storage and cross-Region transfer charges apply.
  scope: multi-party approval.
  link: [no additional cost](../facts/backup.md#backup-mpa-no-extra-cost-storage-charges-apply)
  link: [storage and cross-region transfers charges apply](../facts/backup.md#backup-mpa-no-extra-cost-storage-charges-apply)
backup-mpa-recommends-separate-recovery-organization
  claim: A best practice for multi-party approval is two or more AWS organizations: a primary organization that holds the logically air-gapped vaults and a secondary recovery organization where the approval team is managed.
  scope: multi-party approval best practices.
  link: [Two (or more) AWS organizations](../facts/backup.md#backup-mpa-recommends-separate-recovery-organization)
  link: [recovery organization](../facts/backup.md#backup-mpa-recommends-separate-recovery-organization)
backup-mpa-restore-compromised-vault-contents
  claim: Multi-party approval helps protect critical resources and shorten the time to return to full operation after a disruption by malicious actors or malware, and helps you restore the contents of a logically air-gapped vault that may have been compromised.
  scope: multi-party approval.
  link: [minimize the time to return to full operation](../facts/backup.md#backup-mpa-restore-compromised-vault-contents)
  link: [may have been compromised](../facts/backup.md#backup-mpa-restore-compromised-vault-contents)
backup-mpa-team-resources-only-in-us-east-1
  claim: Multi-party approval team resources can be created and stored only in the US East (N. Virginia) Region.
  scope: multi-party approval teams.
  link: [can only be created and stored](../facts/backup.md#backup-mpa-team-resources-only-in-us-east-1)
  link: [US East (N. Virginia)](../facts/backup.md#backup-mpa-team-resources-only-in-us-east-1)
backup-mpa-trusted-group-approves-recovery-account-access
  claim: With multi-party approval, a group of trusted individuals can collaboratively approve access to a logically air-gapped vault from a separately created recovery account when malicious activity may compromise the primary account.
  scope: multi-party approval.
  link: [group of trusted individuals](../facts/backup.md#backup-mpa-trusted-group-approves-recovery-account-access)
  link: [separately-created recovery account](../facts/backup.md#backup-mpa-trusted-group-approves-recovery-account-access)
backup-native-relationship-varies-by-service
  claim: How AWS Backup relates to a service's native backups varies by service: for some, such as RDS continuous backups, it uses the same underlying backup infrastructure; for others, such as DynamoDB, it works as a separate backup layer.
  scope: AWS Backup and native service backups.
  link: [varies by service](../facts/backup.md#backup-native-relationship-varies-by-service)
  link: [separate backup layer](../facts/backup.md#backup-native-relationship-varies-by-service)
  link: [same underlying backup infrastructure](../facts/backup.md#backup-native-relationship-varies-by-service)
backup-native-service-backups-not-centrally-governed
  claim: Some AWS services offer their own stand-alone backup features that work without AWS Backup, but the backups those services create themselves are not available for central governance through AWS Backup.
  scope: backups created by the services themselves.
  link: [offer their own, stand-alone backup features](../facts/backup.md#backup-native-service-backups-not-centrally-governed)
  link: [not available for central governance through AWS Backup](../facts/backup.md#backup-native-service-backups-not-centrally-governed)
backup-on-demand-backup-starts-immediately
  claim: An on-demand backup begins to back up your resource immediately, and you can use it to create a backup at a time other than the schedule of a backup plan.
  scope: on-demand backups.
  link: [begins to back up your resource immediately](../facts/backup.md#backup-on-demand-backup-starts-immediately)
  link: [other than the scheduled time](../facts/backup.md#backup-on-demand-backup-starts-immediately)
backup-on-demand-ec2-no-reboot-default
  claim: AWS Backup takes EC2 backups with no reboot as the default behavior.
  scope: EC2 backups; default; not adjustable.
  link: [EC2 backups with "no reboot" as the default behavior](../facts/backup.md#backup-on-demand-ec2-no-reboot-default)
  link: [AWS Backup takes EC2 backups](../facts/backup.md#backup-on-demand-ec2-no-reboot-default)
backup-on-demand-not-usable-with-pitr
  claim: You cannot use on-demand backups with point-in-time recovery, because an on-demand backup preserves the resource's state at one moment while PITR uses continuous backups that record changes over a period of time.
  scope: on-demand backups and PITR.
  link: [can't use on-demand backups with PITR](../facts/backup.md#backup-on-demand-not-usable-with-pitr)
  link: [record changes over a period of time](../facts/backup.md#backup-on-demand-not-usable-with-pitr)
backup-on-demand-retention-split-between-warm-and-cold
  claim: For an on-demand backup you set the total retention period in days, and if you specify time in cold storage the retention period is divided between warm and cold storage.
  scope: on-demand backups.
  link: [total retention period](../facts/backup.md#backup-on-demand-retention-split-between-warm-and-cold)
  link: [divided between warm and cold storage](../facts/backup.md#backup-on-demand-retention-split-between-warm-and-cold)
backup-opt-in-still-applies-with-tag-assignment
  claim: If you assign resources only by tags, the service opt-in settings still apply.
  scope: resource assignment by tags.
  link: [only use tags for resource assignment](../facts/backup.md#backup-opt-in-still-applies-with-tag-assignment)
  link: [service opt-in settings will still apply](../facts/backup.md#backup-opt-in-still-applies-with-tag-assignment)
backup-org-management-account-opt-in-overrides-member-accounts
  claim: For backup plans managed by Organizations, the resource opt-in settings of the management account override those of a member account, even if delegated administrator accounts are configured, because delegated administrators cannot override settings the way a management account can.
  scope: Organizations-managed backup plans.
  link: [resource opt-in settings in the management account override](../facts/backup.md#backup-org-management-account-opt-in-overrides-member-accounts)
  link: [cannot override settings like a management account can](../facts/backup.md#backup-org-management-account-opt-in-overrides-member-accounts)
backup-org-member-accounts-need-vault-and-iam-role
  claim: As you add member accounts to your organization, ensure that each account has at least one backup and/or logically air-gapped vault; the backup policies you create identify the AWS Regions, the vaults used in the backup plan, the resources to back up and the IAM role that will be used to create the backup, and backup policies that reference accounts that lack the required information will not work as expected.
  scope: member accounts of an organization.
  link: [will not work as expected](../facts/backup.md#backup-org-member-accounts-need-vault-and-iam-role)
  link: [the IAM role that will be used](../facts/backup.md#backup-org-member-accounts-need-vault-and-iam-role)
backup-org-policy-creates-visible-plan-in-each-account
  claim: When you apply a backup policy to the whole organization, each account gets that backup policy, which creates a corresponding backup plan that is visible in that account.
  scope: Organizations backup policies.
  link: [creates a corresponding backup plan](../facts/backup.md#backup-org-policy-creates-visible-plan-in-each-account)
  link: [visible in that account](../facts/backup.md#backup-org-policy-creates-visible-plan-in-each-account)
backup-org-policy-merge-only-same-plan-name
  claim: Backup policies are merged only when they share the same backup plan name; otherwise policies can coexist in an account without merging.
  scope: Organizations backup policy inheritance.
  link: [share the same backup plan name](../facts/backup.md#backup-org-policy-merge-only-same-plan-name)
  link: [coexist in that account without any merging](../facts/backup.md#backup-org-policy-merge-only-same-plan-name)
backup-org-policy-resources-by-type-or-tag-not-arns
  claim: Backup policies select resources by resource type or by tags, but not by individual resource ARNs; to back up individual resources by ARN, use a local backup plan resource assignment.
  scope: Organizations backup policies.
  link: [by resource types](../facts/backup.md#backup-org-policy-resources-by-type-or-tag-not-arns)
  link: [not by individual resource ARNs](../facts/backup.md#backup-org-policy-resources-by-type-or-tag-not-arns)
backup-org-policy-selections-resource-types-and-exclusions
  claim: In an Organizations backup policy, the resource_types element lists the resource types to include in a backup plan, and the not_resource_types element lists the resource types to exclude.
  scope: selections of an AWS Organizations backup policy.
  link: [Resource types to include in a backup plan.](../facts/backup.md#backup-org-policy-selections-resource-types-and-exclusions)
  link: [Resource types to exclude from a backup plan.](../facts/backup.md#backup-org-policy-selections-resource-types-and-exclusions)
backup-organizations-cross-account-monitoring-management
  claim: AWS Backup works with AWS Organizations to simplify cross-account monitoring and management.
  scope: AWS Backup and AWS Organizations.
  link: [simplify cross-account monitoring and management](../facts/backup.md#backup-organizations-cross-account-monitoring-management)
  link: [AWS Backup works with AWS Organizations](../facts/backup.md#backup-organizations-cross-account-monitoring-management)
backup-overlapping-rules-longer-retention-wins
  claim: When the start windows of different rules in a backup plan overlap, AWS Backup retains the backup under the rule with the longer retention period.
  scope: rules of one backup plan.
  link: [rule with the longer retention period](../facts/backup.md#backup-overlapping-rules-longer-retention-wins)
  link: [start windows of different rules overlap](../facts/backup.md#backup-overlapping-rules-longer-retention-wins)
backup-overview-whitepaper-centralize-automate-policy-based
  claim: The AWS overview whitepaper describes AWS Backup as a cost-effective, fully managed, policy-based service that enables you to centralize and automate data protection across AWS services.
  scope: AWS Backup.
  link: [centralize and automate data protection across AWS services](../facts/backup.md#backup-overview-whitepaper-centralize-automate-policy-based)
  link: [cost-effective, fully managed, policy-based service](../facts/backup.md#backup-overview-whitepaper-centralize-automate-policy-based)
backup-pitr-continuous-works-by-full-backup-and-transaction-logs
  claim: Continuous backup first creates a full backup of the resource and then constantly backs up its transaction logs; point-in-time recovery replays the transaction log on the full backup to the time you choose.
  scope: continuous backups.
  link: [constantly backing up your resource's transaction logs](../facts/backup.md#backup-pitr-continuous-works-by-full-backup-and-transaction-logs)
  link: [replaying the transaction log to the time](../facts/backup.md#backup-pitr-continuous-works-by-full-backup-and-transaction-logs)
backup-pitr-latest-restorable-time-by-service
  claim: For point-in-time restore through AWS Backup, Amazon RDS allows restores up to the most recent 5 minutes of activity, Aurora up to the most recent activity shown by LatestRestorableTime (typically less than 5 minutes), and Amazon S3 up to the most recent 15 minutes of activity.
  scope: point-in-time restore of Amazon RDS, Aurora and Amazon S3; maximum; not adjustable; Aurora: typically less than 5 minutes.
  link: [most recent 5 minutes of activity](../facts/backup.md#backup-pitr-latest-restorable-time-by-service)
  link: [most recent 15 minutes of activity](../facts/backup.md#backup-pitr-latest-restorable-time-by-service)
  say: the last five minutes | the last fifteen minutes
backup-pitr-no-cold-storage-because-35-vs-90
  claim: Continuous backups do not support transition to cold storage, because transition to cold requires a minimum transition period of 90 days while continuous backups have a maximum retention period of 35 days.
  scope: continuous backups.
  link: [minimum transition period of 90 days](../facts/backup.md#backup-pitr-no-cold-storage-because-35-vs-90)
  link: [maximum retention period of 35 days](../facts/backup.md#backup-pitr-no-cold-storage-because-35-vs-90)
backup-pitr-recommend-continuous-and-snapshot-rules-together
  claim: Because continuous and snapshot backups offer different advantages, AWS recommends protecting resources with both continuous and snapshot backup rules.
  scope: resources that support continuous backups.
  link: [both continuous and snapshot backup rules](../facts/backup.md#backup-pitr-recommend-continuous-and-snapshot-rules-together)
  link: [different advantages](../facts/backup.md#backup-pitr-recommend-continuous-and-snapshot-rules-together)
backup-pitr-restore-rewinds-to-chosen-time
  claim: With continuous backups you can restore a supported resource by rewinding it to a specific time you choose, to within 1 second of precision, going back a maximum of 35 days.
  scope: continuous backups, supported resources; maximum.
  link: [within 1 second of precision](../facts/backup.md#backup-pitr-restore-rewinds-to-chosen-time)
  link: [a maximum of 35 days](../facts/backup.md#backup-pitr-restore-rewinds-to-chosen-time)
backup-pitr-retention-change-1-to-35-days-via-plan
  claim: You must use your backup plan to change the retention period of an existing continuous backup rule, the minimum retention period is 1 day, the maximum retention period is 35 days, and the change takes effect when the next backup is completed after the change.
  scope: continuous backup rules; maximum; not adjustable; change takes effect when the next backup completes.
  link: [minimum retention period is 1 day](../facts/backup.md#backup-pitr-retention-change-1-to-35-days-via-plan)
  link: [maximum retention period is 35 days](../facts/backup.md#backup-pitr-retention-change-1-to-35-days-via-plan)
backup-plan-applied-by-tagging-resources
  claim: AWS Backup lets you apply a backup plan to your AWS resources by tagging them; it then backs up the resources automatically according to the plan.
  scope: AWS Backup backup plans.
  link: [apply backup plans to your AWS resources](../facts/backup.md#backup-plan-applied-by-tagging-resources)
  link: [by simply tagging them](../facts/backup.md#backup-plan-applied-by-tagging-resources)
backup-plan-composed-of-one-or-more-backup-rules
  claim: A backup plan is composed of one or more backup rules.
  scope: backup plans.
  link: [composed of one or more backup rules](../facts/backup.md#backup-plan-composed-of-one-or-more-backup-rules)
  link: [Backup plans](../facts/backup.md#backup-plan-composed-of-one-or-more-backup-rules)
backup-plan-expired-backups-deleted-within-8-hours
  claim: When backups expire and are marked for deletion by a lifecycle policy, AWS Backup deletes them at a randomly chosen point over the following 8 hours, which helps ensure consistent performance.
  scope: backups that expire under a lifecycle policy.
  link: [over the following 8 hours](../facts/backup.md#backup-plan-expired-backups-deleted-within-8-hours)
  link: [randomly chosen point](../facts/backup.md#backup-plan-expired-backups-deleted-within-8-hours)
  say: within eight hours after expiry
backup-plan-is-policy-expression
  claim: A backup plan is a policy expression that defines when and how you back up your AWS resources, such as DynamoDB tables or EFS file systems.
  scope: backup plan.
  link: [a policy expression](../facts/backup.md#backup-plan-is-policy-expression)
  link: [when and how you want to back up](../facts/backup.md#backup-plan-is-policy-expression)
backup-plan-maintenance-window-conflicts
  claim: In general, AWS database services cannot start backups 1 hour before or during their maintenance window, and Amazon FSx cannot start backups 3 hours before or during its maintenance window or automatic backup window; Amazon Aurora is exempt. The exception is when you opt in to AWS Backup for both snapshot and continuous backups for a supported service.
  scope: AWS database services (Amazon Aurora exempt) and Amazon FSx; in general; not when you opt in to AWS Backup for both snapshot and continuous backups for a supported service.
  link: [1 hour before or during their maintenance window](../facts/backup.md#backup-plan-maintenance-window-conflicts)
  link: [3 hours before or during their maintenance window](../facts/backup.md#backup-plan-maintenance-window-conflicts)
  say: one hour before or during their maintenance window | three hours before or during their maintenance window
backup-plan-multiple-plans-per-requirement
  claim: You can create multiple backup plans when workloads have different backup requirements.
  scope: AWS Backup backup plans.
  link: [create multiple backup plans](../facts/backup.md#backup-plan-multiple-plans-per-requirement)
  link: [different backup requirements](../facts/backup.md#backup-plan-multiple-plans-per-requirement)
backup-plan-pointing-at-deleted-vault-fails
  claim: A backup plan that points to a deleted backup vault makes backup creation fail, so you update plans to point to new vaults when you delete a vault.
  scope: backup plans and vaults.
  link: [points to a deleted backup vault](../facts/backup.md#backup-plan-pointing-at-deleted-vault-fails)
  link: [cause the backup creation to fail](../facts/backup.md#backup-plan-pointing-at-deleted-vault-fails)
backup-plan-snapshot-frequency-options
  claim: In the AWS Backup console, a backup rule can create snapshot backups every hour, every 12 hours, daily, weekly, or monthly. A cron expression, or the AWS Backup CLI, can schedule snapshot backups as frequently as hourly.
  scope: snapshot backups in a backup rule (not continuous backups).
  link: [every hour, 12 hours, daily, weekly, or monthly](../facts/backup.md#backup-plan-snapshot-frequency-options)
  link: [as frequently as hourly](../facts/backup.md#backup-plan-snapshot-frequency-options)
  say: as often as every hour
backup-plan-update-does-not-change-existing-recovery-points
  claim: Updating a backup plan affects the recovery points it creates in the future, but not the recovery points it has already created.
  scope: backup plan updates.
  link: [affects the future recovery points it will create](../facts/backup.md#backup-plan-update-does-not-change-existing-recovery-points)
  link: [does not affect the recovery point](../facts/backup.md#backup-plan-update-does-not-change-existing-recovery-points)
backup-plan-window-complete-within-default-7-days
  claim: In the backup plan console, the Complete within setting of the backup window defaults to 7 days, and you should leave enough time for the backup to complete even if the job starts at the end of the start window.
  scope: backup window of a backup rule, console default; default; adjustable.
  link: [7 days](../facts/backup.md#backup-plan-window-complete-within-default-7-days)
  say: seven days
backup-plan-window-optimized-by-default
  claim: By default AWS Backup optimizes the backup windows of a plan; you can customize the window in the console or programmatically.
  scope: backup plan windows; default; adjustable.
  link: [backup windows are optimized by AWS Backup](../facts/backup.md#backup-plan-window-optimized-by-default)
  link: [customize the backup window](../facts/backup.md#backup-plan-window-optimized-by-default)
backup-plan-window-start-time-default-0030
  claim: In the backup plan console, the backup window start time defaults to 12:30 AM (00:30 in 24hr time) in your system's local timezone.
  scope: backup window of a backup rule, console default; default; not adjustable; in your system's local timezone.
  link: [12:30 AM](../facts/backup.md#backup-plan-window-start-time-default-0030)
  say: twelve thirty in the morning
backup-plan-window-start-within-default-8-hours
  claim: In the backup plan console, the Start within setting of the backup window defaults to 8 hours, and you can change it to specify a window of time for the backup to start.
  scope: backup window of a backup rule, console default; default; adjustable.
  link: [8 hours](../facts/backup.md#backup-plan-window-start-within-default-8-hours)
  say: eight hours
backup-pricing-audit-manager-evaluation-rate
  claim: AWS Backup Audit Manager backup evaluation charges are prorated per evaluation at $0.00125 per backup evaluation.
  scope: AWS Backup Audit Manager backup evaluations, as listed on the AWS Backup pricing page; fixed.
  link: [$0.00125 per backup evaluation](../facts/backup.md#backup-pricing-audit-manager-evaluation-rate)
backup-pricing-cold-early-deletion-prorated-90-days
  claim: Backups transitioned to cold storage must be retained for a minimum of 90 days, and backups deleted before 90 days incur a pro-rated charge equal to the storage charge for the remaining days.
  scope: backups transitioned to cold storage; minimum; backups deleted before 90 days in cold storage.
  link: [minimum of 90 days](../facts/backup.md#backup-pricing-cold-early-deletion-prorated-90-days)
  link: [pro-rated charge equal to the storage charge](../facts/backup.md#backup-pricing-cold-early-deletion-prorated-90-days)
  say: at least ninety days
backup-pricing-cost-allocation-tags-cost-explorer
  claim: You can use cost allocation tags to track and optimize AWS Backup costs on a detailed level, and view and filter those tags in AWS Cost Explorer.
  scope: AWS Backup cost allocation tags.
  link: [track and optimize AWS Backup costs](../facts/backup.md#backup-pricing-cost-allocation-tags-cost-explorer)
  link: [AWS Cost Explorer](../facts/backup.md#backup-pricing-cost-allocation-tags-cost-explorer)
backup-pricing-cross-region-transfer-out-only
  claim: You only incur data transfer charges when transferring data out of an AWS Region, and there are no charges for transfers within the same AWS Region.
  scope: AWS Backup cross-Region data transfer pricing.
  link: [when transferring data out of an AWS Region](../facts/backup.md#backup-pricing-cross-region-transfer-out-only)
  link: [no charges for transfers](../facts/backup.md#backup-pricing-cross-region-transfer-out-only)
backup-pricing-eks-per-namespace-creation-fee
  claim: Backups of an EKS cluster incur a one time backup creation fee charged per namespace backed up.
  scope: Amazon EKS cluster backups.
  link: [one time backup creation fee](../facts/backup.md#backup-pricing-eks-per-namespace-creation-fee)
  link: [per namespace backed up](../facts/backup.md#backup-pricing-eks-per-namespace-creation-fee)
backup-pricing-gb-day-resource-types
  claim: Backups of EFS, S3, VMware, SAP HANA on EC2 and Amazon Timestream are billed on a GB-day basis instead of a GB-hour basis, so their backup storage is billed for the whole day.
  scope: backup storage of EFS, S3, VMware, SAP HANA on EC2 and Amazon Timestream.
  link: [billed on a GB-day basis](../facts/backup.md#backup-pricing-gb-day-resource-types)
  link: [EFS, S3, VMware, SAP HANA on EC2 and Amazon Timestream](../facts/backup.md#backup-pricing-gb-day-resource-types)
backup-pricing-overview-dimensions
  claim: With AWS Backup you pay for the backup storage you use, backup data transferred between AWS Regions, backup data you restore, and backup evaluations, with no minimum fee and no setup charges.
  scope: AWS Backup pricing.
  link: [backup storage you use](../facts/backup.md#backup-pricing-overview-dimensions)
  link: [no minimum fee](../facts/backup.md#backup-pricing-overview-dimensions)
backup-pricing-restore-billed-gb-restored
  claim: The restore amount billed in a month is based on the amount of data restored in the month, measured in GB, as the sum of the data across all restores performed in the month.
  scope: AWS Backup restore pricing.
  link: [measured in GB](../facts/backup.md#backup-pricing-restore-billed-gb-restored)
  link: [sum of the data across all the restores](../facts/backup.md#backup-pricing-restore-billed-gb-restored)
backup-pricing-restore-testing-evaluation-per-recovery-point
  claim: Restore testing evaluation charges are incurred for each backup or recovery point that you successfully orchestrate for restore through a restore testing plan.
  scope: AWS Backup restore testing pricing.
  link: [each backup or recovery point](../facts/backup.md#backup-pricing-restore-testing-evaluation-per-recovery-point)
  link: [orchestrate for restore through a restore testing plan](../facts/backup.md#backup-pricing-restore-testing-evaluation-per-recovery-point)
backup-pricing-s3-extra-charges-versioning-requests-eventbridge
  claim: In the AWS Backup pricing example for Amazon S3 backups, AWS notes additional charges for S3 Versioning, and incremental backups incur additional charges for storage as well as for S3 GET/LIST requests and EventBridge.
  scope: AWS Backup for Amazon S3 (pricing page example).
  link: [additional charges for S3 Versioning](../facts/backup.md#backup-pricing-s3-extra-charges-versioning-requests-eventbridge)
  link: [S3 GET/LIST requests and Eventbridge](../facts/backup.md#backup-pricing-s3-extra-charges-versioning-requests-eventbridge)
backup-pricing-s3-min-128-kb-object
  claim: For S3 objects smaller than 128 KB, the backups are priced as a 128-KB backup.
  scope: S3 object backups; minimum; per S3 object smaller than 128 KB.
  link: [priced as a 128-KB backup](../facts/backup.md#backup-pricing-s3-min-128-kb-object)
  link: [smaller than 128 KB](../facts/backup.md#backup-pricing-s3-min-128-kb-object)
backup-pricing-storage-billed-gb-month-average
  claim: AWS Backup storage pricing is based on the amount of storage your backup data consumes, and the amount billed in a month is based on the average storage space used throughout the month, billed as GB-Month.
  scope: AWS Backup storage pricing.
  link: [billed as GB-Month](../facts/backup.md#backup-pricing-storage-billed-gb-month-average)
  link: [average storage space used throughout the month](../facts/backup.md#backup-pricing-storage-billed-gb-month-average)
backup-pricing-tiering-60-days-warm-before-low-cost
  claim: Backup data can be moved to the low-cost warm storage tier based on a tiering configuration, and objects need to be retained in the warm storage tier for a minimum of 60 days before transitioning to the low-cost tier.
  scope: backup tiering to the low-cost warm storage tier, as footnoted on the AWS Backup pricing page; minimum.
  link: [minimum of 60 days](../facts/backup.md#backup-pricing-tiering-60-days-warm-before-low-cost)
  say: at least sixty days
backup-quota-additional-copy-jobs-per-vault-after-limit
  claim: Once the limit of 100 concurrent copy jobs from one Region to another Region per account per Region is reached, new copy jobs can still begin while a specific vault in the destination Region has fewer than 5 concurrent copy jobs, up to a maximum of 5 concurrently. The quota is not adjustable, and the table footnote says the limit only applies to resource types fully managed by AWS Backup.
  scope: per vault in the destination Region, after the 100-job per-account limit is reached; maximum; not adjustable; applies once the limit of 100 concurrent copy jobs per account per Region is reached; only resource types fully managed by AWS Backup.
  link: [5 concurrent copy jobs](../facts/backup.md#backup-quota-additional-copy-jobs-per-vault-after-limit)
  say: five concurrent copy jobs
backup-quota-audit-manager-controls-per-region
  claim: The default quota is 50 controls per account per Region in AWS Backup Audit Manager, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [50 controls](../facts/backup.md#backup-quota-audit-manager-controls-per-region)
  say: fifty controls
backup-quota-audit-manager-frameworks-per-region
  claim: The default quota is 15 frameworks per account per Region in AWS Backup Audit Manager, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [15 frameworks](../facts/backup.md#backup-quota-audit-manager-frameworks-per-region)
  say: fifteen frameworks
backup-quota-audit-manager-report-plans-per-account
  claim: The default quota is 20 report plans per account in AWS Backup Audit Manager, and the quota is adjustable.
  scope: per account; default; adjustable.
  link: [20 report plans](../facts/backup.md#backup-quota-audit-manager-report-plans-per-account)
  say: twenty report plans
backup-quota-backup-plans-per-region-per-account
  claim: The default quota is 300 backup plans per Region per account, and the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [300 backup plans](../facts/backup.md#backup-quota-backup-plans-per-region-per-account)
  say: three hundred backup plans
backup-quota-concurrent-copy-jobs-destination-region
  claim: A limit of 100 concurrent copy jobs from one Region to another applies per account per Region, and it applies only to resource types fully managed by AWS Backup. The quota is not adjustable.
  scope: per account, per destination Region; resource types fully managed by AWS Backup only; maximum; not adjustable; resource types fully managed by AWS Backup.
  link: [100 concurrent copy jobs](../facts/backup.md#backup-quota-concurrent-copy-jobs-destination-region)
  say: one hundred concurrent copy jobs
backup-quota-concurrent-cross-account-copies-same-resource
  claim: The quota is 30 concurrent cross-account copies that can be made of the same resource to the same destination Region, and the quota is not adjustable.
  scope: per resource, per destination Region; default; not adjustable.
  link: [30 concurrent cross-account copies](../facts/backup.md#backup-quota-concurrent-cross-account-copies-same-resource)
  say: thirty concurrent cross-account copies
backup-quota-concurrent-jobs-per-resource
  claim: The quota is 1 concurrent backup and copy job per resource, and the quota is not adjustable.
  scope: per resource; default; not adjustable.
  link: [1 concurrent backup and copy job](../facts/backup.md#backup-quota-concurrent-jobs-per-resource)
  say: one concurrent backup and copy job
backup-quota-conditions-per-resource-assignment
  claim: The policy quota is 30 conditions in a resource assignment in a backup plan, and the quota is not adjustable.
  scope: per resource assignment in a backup plan; default; not adjustable.
  link: [30 conditions](../facts/backup.md#backup-quota-conditions-per-resource-assignment)
  say: thirty conditions
backup-quota-copy-actions-per-backup-rule
  claim: The policy quota is 5 copy actions per backup rule, and the quota is not adjustable.
  scope: per backup rule; default; not adjustable.
  link: [5 copy actions](../facts/backup.md#backup-quota-copy-actions-per-backup-rule)
  say: five copy actions
backup-quota-eks-namespaces-per-cluster-backup
  claim: The default quota is 10,000 namespaces per EKS cluster backup, and the quota is adjustable.
  scope: per EKS cluster backup; default; adjustable.
  link: [10,000 namespaces](../facts/backup.md#backup-quota-eks-namespaces-per-cluster-backup)
  say: ten thousand namespaces
backup-quota-eks-restore-jobs-per-target-cluster
  claim: The quota is 1 restore job per target EKS cluster, and the quota is not adjustable.
  scope: per target EKS cluster; default; not adjustable.
  link: [1 restore job per target EKS cluster](../facts/backup.md#backup-quota-eks-restore-jobs-per-target-cluster)
  say: one restore job per target EKS cluster
backup-quota-malware-running-scan-jobs-per-account
  claim: The default quota is 150 running scan jobs per account for AWS Backup malware scanning with Amazon GuardDuty, and the quota is adjustable.
  scope: per account, AWS Backup malware scanning with Amazon GuardDuty; default; adjustable.
  link: [150 running scan jobs](../facts/backup.md#backup-quota-malware-running-scan-jobs-per-account)
  say: one hundred fifty running scan jobs
backup-quota-recovery-points-per-vault
  claim: The default quota is 1,000,000 recovery points per backup vault, and the quota is adjustable.
  scope: per backup vault; default; adjustable.
  link: [1,000,000 recovery points](../facts/backup.md#backup-quota-recovery-points-per-vault)
  say: one million recovery points
backup-quota-resource-assignments-per-backup-plan
  claim: The quota is 100 resource assignments per backup plan, and the quota is not adjustable.
  scope: per backup plan; default; not adjustable.
  link: [100 resource assignments](../facts/backup.md#backup-quota-resource-assignments-per-backup-plan)
  say: one hundred resource assignments
backup-quota-restore-testing-plans
  claim: The quota is 100 restore testing plans, and the quota is not adjustable.
  scope: restore testing plans; default; not adjustable.
  link: [100 restore testing plans](../facts/backup.md#backup-quota-restore-testing-plans)
  say: one hundred restore testing plans
backup-quota-restore-testing-selection-window-max-days
  claim: The maximum value of the restore testing selection window is 365 days, and the quota is not adjustable.
  scope: selection window of a restore testing plan; maximum; not adjustable.
  link: [365 days](../facts/backup.md#backup-quota-restore-testing-selection-window-max-days)
  say: three hundred sixty-five days
backup-quota-restore-testing-start-window-hours
  claim: The boundaries of the restore testing start window are a minimum of 1 hour and a maximum of 168 hours, and the quota is not adjustable.
  scope: start window of a restore testing plan; maximum; not adjustable; minimum 1 hour, maximum 168 hours.
  link: [1 hour](../facts/backup.md#backup-quota-restore-testing-start-window-hours)
  link: [168 hours](../facts/backup.md#backup-quota-restore-testing-start-window-hours)
  say: one hour | one hundred sixty-eight hours
backup-quota-rules-per-backup-plan
  claim: The policy quota is 10 backup plan rules in a plan, and the quota is not adjustable.
  scope: per backup plan; default; not adjustable.
  link: [10 backup plan rules](../facts/backup.md#backup-quota-rules-per-backup-plan)
  say: ten backup plan rules
backup-quota-search-concurrent-indexing-jobs
  claim: The default quota is 40 concurrent indexing jobs in an account in most AWS Regions, and the quota is adjustable; in the Asia Pacific (Malaysia), Canada (Central), Asia Pacific (Thailand), and Mexico (Central) Regions the default is 10, also adjustable.
  scope: per account, most AWS Regions; default; adjustable; a lower default applies in a few Regions.
  link: [40 concurrent indexing jobs](../facts/backup.md#backup-quota-search-concurrent-indexing-jobs)
  say: forty concurrent indexing jobs
backup-quota-tag-resource-selections-per-plan
  claim: The policy quota is 10 resource selections that use tags in a plan, and the quota is not adjustable.
  scope: per backup plan; default; not adjustable.
  link: [10 resource selections that use tags](../facts/backup.md#backup-quota-tag-resource-selections-per-plan)
  say: ten resource selections that use tags
backup-quota-tags-added-to-recovery-point
  claim: The policy quota is 10 tags added to a recovery point, and the quota is not adjustable.
  scope: per recovery point; default; not adjustable.
  link: [10 tags added to a recovery point](../facts/backup.md#backup-quota-tags-added-to-recovery-point)
  say: ten tags added to a recovery point
backup-quota-tags-in-resource-selection
  claim: The policy quota is 30 tags in a resource selection, and the quota is not adjustable.
  scope: per resource selection; default; not adjustable.
  link: [30 tags in a resource selection](../facts/backup.md#backup-quota-tags-in-resource-selection)
  say: thirty tags in a resource selection
backup-quota-tags-per-cross-account-policy-selection
  claim: The quota is 30 tags per resource selection in a cross account backup policy. It is not adjustable, and additional tags go into multiple resource assignments or backup plans.
  scope: per resource selection in a cross account backup policy; default; not adjustable.
  link: [30 tags](../facts/backup.md#backup-quota-tags-per-cross-account-policy-selection)
  say: thirty tags
backup-quota-vaults-per-region-per-account
  claim: The default quota is 300 vaults (backup vaults and logically air-gapped vaults together) per Region per account, and you can request an increase.
  scope: per Region, per account; backup vaults and logically air-gapped vaults counted together; default; adjustable.
  link: [300](../facts/backup.md#backup-quota-vaults-per-region-per-account)
  say: three hundred
backup-quota-versions-per-backup-plan
  claim: The default quota is 2,000 versions per backup plan, and the quota is adjustable.
  scope: per backup plan; default; adjustable.
  link: [2,000 versions](../facts/backup.md#backup-quota-versions-per-backup-plan)
  say: two thousand versions
backup-rds-aws-backup-creates-manual-db-snapshot-same-chain
  claim: When AWS Backup backs up an RDS instance it creates a manual DB snapshot with the create-db-snapshot operation, and all snapshots of the instance, whether automated, manual or from AWS Backup, belong to the same incremental snapshot chain.
  scope: RDS instances backed up by AWS Backup.
  link: [creates a manual DB snapshot of that instance](../facts/backup.md#backup-rds-aws-backup-creates-manual-db-snapshot-same-chain)
  link: [same incremental snapshot chain](../facts/backup.md#backup-rds-aws-backup-creates-manual-db-snapshot-same-chain)
backup-rds-consolidated-snapshot-charged-once
  claim: When RDS consolidates an automated and a manual snapshot entry, both entries reference the same underlying snapshot data, you are charged only once for it, and retention and point-in-time restore are unaffected.
  scope: RDS consolidated backups.
  link: [charged only once for that single underlying snapshot](../facts/backup.md#backup-rds-consolidated-snapshot-charged-once)
  link: [reference the same underlying snapshot data](../facts/backup.md#backup-rds-consolidated-snapshot-charged-once)
backup-rds-custom-oracle-outposts-local-zones-unsupported
  claim: AWS Backup does not support RDS Custom for Oracle, and does not support backup and restore of RDS on Outposts or in Local Zones.
  scope: Amazon RDS deployments.
  link: [RDS Custom for Oracle is not currently supported](../facts/backup.md#backup-rds-custom-oracle-outposts-local-zones-unsupported)
  link: [RDS on Outposts or in Local Zones](../facts/backup.md#backup-rds-custom-oracle-outposts-local-zones-unsupported)
backup-rds-multi-az-mysql-postgres-one-primary-two-standbys
  claim: AWS Backup backs up and supports Amazon RDS for MySQL and for PostgreSQL Multi-AZ deployment options with one primary and two readable standby database instances.
  scope: RDS Multi-AZ DB clusters.
  link: [MySQL and for PostgreSQL Multi-AZ](../facts/backup.md#backup-rds-multi-az-mysql-postgres-one-primary-two-standbys)
  link: [one primary and two readable standby database instances](../facts/backup.md#backup-rds-multi-az-mysql-postgres-one-primary-two-standbys)
backup-rds-only-first-snapshot-full-later-incremental
  claim: Only the first snapshot ever taken of an RDS DB instance stores the full contents of the database; every later snapshot is incremental, so the first recovery point AWS Backup creates can also be incremental if earlier snapshots exist.
  scope: RDS DB instance snapshots.
  link: [Only the first snapshot ever taken](../facts/backup.md#backup-rds-only-first-snapshot-full-later-incremental)
  link: [also incremental, not a new full snapshot](../facts/backup.md#backup-rds-only-first-snapshot-full-later-incremental)
backup-rds-periodic-snapshots-are-manual-backups-in-rds
  claim: Periodic snapshots created by AWS Backup are considered manual backups in Amazon RDS, while continuous backups created by AWS Backup are considered automated backups in Amazon RDS.
  scope: RDS backups created by AWS Backup.
  link: [considered manual backups in Amazon RDS](../facts/backup.md#backup-rds-periodic-snapshots-are-manual-backups-in-rds)
  link: [considered automated backups in Amazon RDS](../facts/backup.md#backup-rds-periodic-snapshots-are-manual-backups-in-rds)
backup-rds-snapshots-share-free-backup-storage-allocation
  claim: AWS Backup periodic snapshots count as manual backups toward your total RDS backup storage, alongside automated backups; RDS gives free backup storage equal to your provisioned DB instance storage for both combined, and storage beyond that is billed.
  scope: RDS backup storage.
  link: [free backup storage allocation](../facts/backup.md#backup-rds-snapshots-share-free-backup-storage-allocation)
  link: [Storage beyond that allocation is billed](../facts/backup.md#backup-rds-snapshots-share-free-backup-storage-allocation)
backup-rds-toggling-continuous-backups-takes-instance-offline
  claim: Enabling continuous backups for RDS through AWS Backup when they were disabled, or disabling them when they were enabled, takes the RDS instance offline to make the change; if automated backups were enabled from RDS and simply moved to AWS Backup, no downtime is required.
  scope: RDS instances.
  link: [takes the Amazon RDS instance offline](../facts/backup.md#backup-rds-toggling-continuous-backups-takes-instance-offline)
  link: [then no downtime is required](../facts/backup.md#backup-rds-toggling-continuous-backups-takes-instance-offline)
backup-recovery-point-is-backup-at-specified-time
  claim: A backup, or recovery point, represents the content of a resource such as an EBS volume or DynamoDB table at a specified time; the terms recovery point and backup are used interchangeably.
  scope: AWS Backup recovery points.
  link: [represents the content of a resource](../facts/backup.md#backup-recovery-point-is-backup-at-specified-time)
  link: [used interchangeably](../facts/backup.md#backup-recovery-point-is-backup-at-specified-time)
backup-recovery-points-saved-in-vaults
  claim: AWS Backup saves recovery points in backup vaults, which you can organize according to your business needs.
  scope: AWS Backup vaults.
  link: [saves recovery points in backup vaults](../facts/backup.md#backup-recovery-points-saved-in-vaults)
  link: [organize according to your business needs](../facts/backup.md#backup-recovery-points-saved-in-vaults)
backup-redshift-clusters-and-serverless-namespaces
  claim: AWS Backup supports Amazon Redshift provisioned clusters and Redshift Serverless namespaces.
  scope: Amazon Redshift.
  link: [Amazon Redshift provisioned clusters](../facts/backup.md#backup-redshift-clusters-and-serverless-namespaces)
  link: [Redshift Serverless namespaces](../facts/backup.md#backup-redshift-clusters-and-serverless-namespaces)
backup-resilience-at-least-as-durable-as-source-service
  claim: AWS Backup stores your backups with at least as much resilience and durability as the resource's original AWS service would give you if you backed it up there.
  scope: AWS Backup recovery points.
  link: [at least as much resilience and durability](../facts/backup.md#backup-resilience-at-least-as-durable-as-source-service)
  link: [original AWS service would give you](../facts/backup.md#backup-resilience-at-least-as-durable-as-source-service)
backup-resilience-copy-across-regions-greater-resilience
  claim: AWS Backup lets you copy your backups across Regions for even greater resilience.
  scope: AWS Backup cross-Region copy.
  link: [copy your backups across Regions](../facts/backup.md#backup-resilience-copy-across-regions-greater-resilience)
  link: [even greater resilience](../facts/backup.md#backup-resilience-copy-across-regions-greater-resilience)
backup-resilience-stored-across-azs-eleven-nines
  claim: AWS Backup is designed to store your backups redundantly across multiple Availability Zones for durability of 99.999999999% (11 nines) in any given year, provided that you adhere to the current AWS Backup documentation.
  scope: AWS Backup recovery points; provided that you adhere to the current AWS Backup documentation.
  link: [99.999999999% (11 nines)](../facts/backup.md#backup-resilience-stored-across-azs-eleven-nines)
  link: [across multiple Availability Zones](../facts/backup.md#backup-resilience-stored-across-azs-eleven-nines)
backup-restore-aurora-cluster-only-no-instance
  claim: AWS Backup restores an Aurora cluster; it does not create or attach an Amazon RDS instance to the cluster, and the guide's steps then create and attach an Amazon RDS instance to the restored Aurora cluster using the CLI.
  scope: Aurora restores.
  link: [does not create or attach](../facts/backup.md#backup-restore-aurora-cluster-only-no-instance)
  link: [AWS Backup restores your Aurora cluster](../facts/backup.md#backup-restore-aurora-cluster-only-no-instance)
backup-restore-ddb-cross-account-same-key-must-be-shared
  claim: To encrypt a table restored from a cross-account backup with the same key as the original table, you must share the key in the source account with the destination account; AWS-owned and AWS-managed keys cannot be shared between accounts.
  scope: DynamoDB restores of cross-account copies.
  link: [you must share the key](../facts/backup.md#backup-restore-ddb-cross-account-same-key-must-be-shared)
  link: [cannot be shared between accounts](../facts/backup.md#backup-restore-ddb-cross-account-same-key-must-be-shared)
backup-restore-ddb-cross-region-same-key-needs-multi-region-key
  claim: To encrypt a table restored from a cross-Region backup with the same key as the original table, the key must be a multi-Region key; AWS-owned and AWS-managed keys are not multi-Region keys.
  scope: DynamoDB restores of cross-Region copies.
  link: [your key must be a multi-Region key](../facts/backup.md#backup-restore-ddb-cross-region-same-key-needs-multi-region-key)
  link: [AWS-owned and AWS-managed keys are not multi-Region keys](../facts/backup.md#backup-restore-ddb-cross-region-same-key-needs-multi-region-key)
backup-restore-ddb-to-new-table
  claim: When you restore a DynamoDB recovery point in the AWS Backup console, the Settings step has a New table name text field in which you enter a new table name.
  scope: DynamoDB restores.
  link: [enter a new table name](../facts/backup.md#backup-restore-ddb-to-new-table)
  link: [New table name](../facts/backup.md#backup-restore-ddb-to-new-table)
backup-restore-destructive-exceptions-listed
  claim: When AWS Backup restores a backup, it creates a new resource with the backup, to protect existing resources from being destroyed by the restore. The exceptions are Amazon Redshift Serverless, whose namespace restores overwrite all existing data in the target namespace, and SAP HANA on Amazon EC2, whose restores overwrite the database at the target restore location; for all other resource types AWS Backup creates a new resource during restore.
  scope: AWS Backup restores, by resource type; Amazon Redshift Serverless namespace restores and SAP HANA on Amazon EC2 restores are destructive.
  link: [perform destructive restores that overwrite existing data](../facts/backup.md#backup-restore-destructive-exceptions-listed)
  link: [creates a new resource during restore](../facts/backup.md#backup-restore-destructive-exceptions-listed)
  link: [Amazon Redshift Serverless](../facts/backup.md#backup-restore-destructive-exceptions-listed)
  link: [SAP HANA on Amazon EC2](../facts/backup.md#backup-restore-destructive-exceptions-listed)
  link: [protect your existing resources from being destroyed](../facts/backup.md#backup-restore-destructive-exceptions-listed)
backup-restore-efs-files-not-in-original-locations
  claim: After an EFS full restore, the restored files are in a recovery subdirectory under the root of the file system, not in their original locations, and you must manually move or copy them to where they belong.
  scope: Amazon EFS restores.
  link: [located in a recovery subdirectory under the root](../facts/backup.md#backup-restore-efs-files-not-in-original-locations)
  link: [Files are not restored to their original locations](../facts/backup.md#backup-restore-efs-files-not-in-original-locations)
backup-restore-efs-full-or-item-level
  claim: For an Amazon EFS restore you can perform a full restore, which restores the entire file system, or an item-level restore of a specific file or directory.
  scope: Amazon EFS restores.
  link: [full restore or an item-level restore](../facts/backup.md#backup-restore-efs-full-or-item-level)
  link: [restores a specific file or directory](../facts/backup.md#backup-restore-efs-full-or-item-level)
backup-restore-efs-item-level-to-new-or-existing-file-system
  claim: You can restore EFS items to either a new or an existing file system, and each restore attempt creates a new recovery directory off the root directory to hold the restored files.
  scope: Amazon EFS item-level restores.
  link: [either a new or existing file system](../facts/backup.md#backup-restore-efs-item-level-to-new-or-existing-file-system)
  link: [creates a new recovery directory](../facts/backup.md#backup-restore-efs-item-level-to-new-or-existing-file-system)
backup-restore-efs-no-destructive-restore-recovery-directory
  claim: AWS Backup does not support destructive restores with Amazon EFS: it restores the file system to a recovery directory off the root directory instead of overwriting the source or an existing file system.
  scope: Amazon EFS restores.
  link: [does not support destructive restores with Amazon EFS](../facts/backup.md#backup-restore-efs-no-destructive-restore-recovery-directory)
  link: [recovery directory off of the root directory](../facts/backup.md#backup-restore-efs-no-destructive-restore-recovery-directory)
backup-restore-efs-single-weekly-backup-only-that-state
  claim: If you keep only one weekly backup of an EFS file system, you can restore only to the state of the file system when that backup was taken, not to earlier incremental backups.
  scope: Amazon EFS restores.
  link: [only restore to the state](../facts/backup.md#backup-restore-efs-single-weekly-backup-only-that-state)
  link: [can't restore to prior incremental backups](../facts/backup.md#backup-restore-efs-single-weekly-backup-only-that-state)
backup-restore-from-cold-storage-takes-longer
  claim: Restoring from cold storage typically takes 4 hours more than restoring from warm storage.
  scope: restore from cold storage; typical value.
  link: [typically takes 4 hours more](../facts/backup.md#backup-restore-from-cold-storage-takes-longer)
  link: [than restoring from warm storage](../facts/backup.md#backup-restore-from-cold-storage-takes-longer)
backup-restore-no-sla-for-restore-time
  claim: AWS Backup does not provide any service-level agreements (SLAs) for restore time; restore times vary with system load and capacity.
  scope: AWS Backup restores.
  link: [does not provide any service-level agreements (SLAs)](../facts/backup.md#backup-restore-no-sla-for-restore-time)
  link: [system load and capacity](../facts/backup.md#backup-restore-no-sla-for-restore-time)
backup-restore-testing-automated-periodic-evaluation
  claim: Restore testing is an AWS Backup feature that automatically and periodically evaluates whether restores will work, and monitors restore job duration.
  scope: AWS Backup restore testing.
  link: [automated and periodic evaluation of restore viability](../facts/backup.md#backup-restore-testing-automated-periodic-evaluation)
  link: [monitor restore job duration times](../facts/backup.md#backup-restore-testing-automated-periodic-evaluation)
backup-restore-testing-best-practice-designated-account
  claim: The recommended best practice for restore testing is to designate an account to be used for restore tests.
  scope: restore testing.
  link: [designate an account to be used](../facts/backup.md#backup-restore-testing-best-practice-designated-account)
  link: [Recommended best practice](../facts/backup.md#backup-restore-testing-best-practice-designated-account)
backup-restore-testing-eligible-recovery-point-range
  claim: In a restore testing plan you specify the time frame from which recovery points are selected, and you can select 1 to 365 days, 1 to 52 weeks, 1 to 12 months, or 1 year.
  scope: eligible recovery points of a restore testing plan; maximum; not adjustable; console selection options.
  link: [1 to 365 days](../facts/backup.md#backup-restore-testing-eligible-recovery-point-range)
  link: [1 to 52 weeks](../facts/backup.md#backup-restore-testing-eligible-recovery-point-range)
  link: [1 to 12 months](../facts/backup.md#backup-restore-testing-eligible-recovery-point-range)
backup-restore-testing-plan-steps
  claim: You create a restore testing plan with a name, the test frequency and the target start time, assign the resources to include, and choose specific or random recovery points; AWS Backup infers the metadata needed for the restore.
  scope: AWS Backup restore testing.
  link: [the frequency for your restore tests](../facts/backup.md#backup-restore-testing-plan-steps)
  link: [specific or random recovery points](../facts/backup.md#backup-restore-testing-plan-steps)
backup-restore-testing-resources-deleted-after-validation
  claim: Once the optional validation completes or the validation window closes, AWS Backup deletes the resources involved in the restore test, in accordance with service SLAs.
  scope: AWS Backup restore testing.
  link: [deletes the resources involved with the restore test](../facts/backup.md#backup-restore-testing-resources-deleted-after-validation)
  link: [validation window closes](../facts/backup.md#backup-restore-testing-resources-deleted-after-validation)
backup-restore-testing-results-show-compliance-and-duration
  claim: When the scheduled time arrives AWS Backup starts restore jobs from the plan and monitors the time taken; afterwards you can use the results to show compliance, such as successful restore test scenarios or the restore job completion time.
  scope: AWS Backup restore testing.
  link: [monitors the time taken to complete the restore](../facts/backup.md#backup-restore-testing-results-show-compliance-and-duration)
  link: [restore job completion time](../facts/backup.md#backup-restore-testing-results-show-compliance-and-duration)
backup-restore-testing-same-restore-jobs-as-on-demand
  claim: Restore testing runs restore jobs in the same way as on-demand restores and uses the same recovery points as an on-demand restore.
  scope: AWS Backup restore testing.
  link: [in the same way as on-demand restores](../facts/backup.md#backup-restore-testing-same-restore-jobs-as-on-demand)
  link: [same recovery points](../facts/backup.md#backup-restore-testing-same-restore-jobs-as-on-demand)
backup-restore-testing-tag-removed-needs-manual-delete
  claim: Resources restored by a restore testing plan that support tag-on-restore carry the awsbackup-restore-test tag; if a user removes the tag, AWS Backup cannot delete the resource at the end of the test and the user must delete it manually.
  scope: restore testing cleanup.
  link: [awsbackup-restore-test](../facts/backup.md#backup-restore-testing-tag-removed-needs-manual-delete)
  link: [AWS Backup cannot delete the resource](../facts/backup.md#backup-restore-testing-tag-removed-needs-manual-delete)
backup-restore-testing-validation-event-driven-eventbridge
  claim: Restore testing validation is an option: you can create an event-driven validation that runs when a restore testing job completes, by creating a validation workflow with any target supported by Amazon EventBridge, such as AWS Lambda, and adding an EventBridge rule that listens for the restore job reaching the status COMPLETED.
  scope: restore testing validation.
  link: [event-driven validation](../facts/backup.md#backup-restore-testing-validation-event-driven-eventbridge)
  link: [any target supported by Amazon EventBridge](../facts/backup.md#backup-restore-testing-validation-event-driven-eventbridge)
backup-restore-testing-validation-retain-1-to-168-hours
  claim: If you plan to run validation on a restore test, you select retain for a specific number of hours and input a value from 1 to 168 hours, inclusive; validation can be run programmatically but not from the AWS Backup console.
  scope: retention period before cleanup of a restore test, when validation is planned; maximum; not adjustable; validation can be run programmatically but not from the console.
  link: [from 1 to 168 hours, inclusive](../facts/backup.md#backup-restore-testing-validation-retain-1-to-168-hours)
  link: [168 hours](../facts/backup.md#backup-restore-testing-validation-retain-1-to-168-hours)
  say: one hundred sixty-eight hours
backup-restore-testing-vs-restore-audit-manager-row
  claim: AWS Backup Audit Manager can turn on a control to confirm whether a restore test meets specified restore objectives.
  scope: restore testing.
  link: [a restore test meets specified restore objectives](../facts/backup.md#backup-restore-testing-vs-restore-audit-manager-row)
  link: [AWS Backup Audit Manager](../facts/backup.md#backup-restore-testing-vs-restore-audit-manager-row)
backup-restore-testing-vs-restore-resources-row
  claim: The resource types you can assign to a restore testing plan are Aurora, DocumentDB, DynamoDB, EBS, EC2, EFS, FSx (Lustre, ONTAP, OpenZFS, Windows), Neptune, RDS and S3, while any resource can be restored on demand.
  scope: AWS Backup restore testing.
  link: [you can assign to your testing plan](../facts/backup.md#backup-restore-testing-vs-restore-resources-row)
  link: [All resources can be restored](../facts/backup.md#backup-restore-testing-vs-restore-resources-row)
backup-restore-testing-vs-restore-results-row
  claim: After a restore testing job completes, the restored resource is deleted when the validation window finishes, whereas after an on-demand restore job the restored resource remains.
  scope: restore testing versus restore.
  link: [the restored resource is deleted after the](../facts/backup.md#backup-restore-testing-vs-restore-results-row)
  link: [the restored version of the resource remains](../facts/backup.md#backup-restore-testing-vs-restore-results-row)
backup-retention-continuous-range
  claim: The retention period for continuous backups can range from 1 day to 35 days.
  scope: retention period of continuous backups; maximum; not adjustable.
  link: [1 day to 35 days](../facts/backup.md#backup-retention-continuous-range)
  link: [35 days](../facts/backup.md#backup-retention-continuous-range)
  say: thirty-five days
backup-retention-s3-continuous-max-35-days
  claim: The retention period of each continuous backup of an Amazon S3 bucket has a maximum of 35 days.
  scope: continuous backups of Amazon S3 buckets; maximum; not adjustable.
  link: [maximum of 35 days](../facts/backup.md#backup-retention-s3-continuous-max-35-days)
  say: thirty-five days
backup-retention-s3-periodic-up-to-99-years
  claim: The snapshot made by a periodic Amazon S3 backup can have a retention period of up to 99 years.
  scope: periodic (snapshot) backups of Amazon S3 buckets; maximum; not adjustable.
  link: [up to 99 years](../facts/backup.md#backup-retention-s3-periodic-up-to-99-years)
  say: up to ninety-nine years
backup-retention-snapshot-range
  claim: The retention period for snapshot backups can range between 1 day and 100 years, or indefinitely if you do not enter one.
  scope: retention period of snapshot backups; maximum; not adjustable; or indefinitely if you do not enter a retention period.
  link: [1 day](../facts/backup.md#backup-retention-snapshot-range)
  link: [100 years](../facts/backup.md#backup-retention-snapshot-range)
  link: [between 1 day and 100 years](../facts/backup.md#backup-retention-snapshot-range)
  say: one day | one hundred years
backup-s3-access-points-direct-access-without-restore
  claim: AWS Backup lets you access S3 backup data directly through S3 access points, without initiating a restore.
  scope: S3 backups.
  link: [access S3 backup data directly through S3 access points](../facts/backup.md#backup-s3-access-points-direct-access-without-restore)
  link: [without initiating a restore](../facts/backup.md#backup-s3-access-points-direct-access-without-restore)
backup-s3-backup-any-object-size
  claim: AWS Backup supports backup and restore operations for S3 objects of any size, up to the maximum object size supported by Amazon S3.
  scope: AWS Backup for Amazon S3; maximum.
  link: [objects of any size](../facts/backup.md#backup-s3-backup-any-object-size)
  link: [maximum object size supported by Amazon S3](../facts/backup.md#backup-s3-backup-any-object-size)
backup-s3-backup-types-object-data-tags-acls-metadata
  claim: With AWS Backup you can create two types of backups of S3 buckets, including object data, tags, access control lists (ACLs) and user-defined metadata: continuous backups, which allow restore to any point in time within the last 35 days, and periodic backups, which use snapshots to retain data for your specified duration up to 99 years.
  scope: S3 backups.
  link: [object data, tags, Access Control Lists (ACLs)](../facts/backup.md#backup-s3-backup-types-object-data-tags-acls-metadata)
  link: [Continuous backups](../facts/backup.md#backup-s3-backup-types-object-data-tags-acls-metadata)
backup-s3-continuous-and-periodic-same-vault
  claim: Continuous and periodic backups of S3 buckets must both reside in the same backup vault.
  scope: S3 backups.
  link: [must both reside in the same backup vault](../facts/backup.md#backup-s3-continuous-and-periodic-same-vault)
  link: [Continuous and periodic backups of S3 buckets](../facts/backup.md#backup-s3-continuous-and-periodic-same-vault)
backup-s3-continuous-pitr-last-35-days-one-plan
  claim: S3 continuous backups let you restore to any point in time within the last 35 days, and continuous backups for an S3 bucket should be configured in only one backup plan.
  scope: S3 continuous backups; maximum.
  link: [restore to any point in time within the last 35 days](../facts/backup.md#backup-s3-continuous-pitr-last-35-days-one-plan)
  link: [only be configured in one backup plan](../facts/backup.md#backup-s3-continuous-pitr-last-35-days-one-plan)
backup-s3-copies-available-copies-of-continuous-no-pitr
  claim: Cross-account and cross-Region copies are available for S3 backups, but copies of continuous backups do not have point-in-time restore capabilities.
  scope: S3 backup copies.
  link: [do not have point-in-time restore capabilities](../facts/backup.md#backup-s3-copies-available-copies-of-continuous-no-pitr)
  link: [Cross-account and cross-Region copies are available](../facts/backup.md#backup-s3-copies-available-copies-of-continuous-no-pitr)
backup-s3-eventbridge-disabled-failure-is-silent
  claim: If the bucket-level Amazon EventBridge notification setting is disabled, S3 stops publishing object-level events and the AWS Backup managed rule receives none; the failure is silent, with no notification, alert or backup job failure from AWS Backup.
  scope: S3 continuous backups.
  link: [This failure is silent](../facts/backup.md#backup-s3-eventbridge-disabled-failure-is-silent)
  link: [no notification, alert, or backup job failure](../facts/backup.md#backup-s3-eventbridge-disabled-failure-is-silent)
backup-s3-first-full-then-object-level-incremental
  claim: For both S3 backup types, the first backup is a full backup and subsequent backups are incremental at object level.
  scope: S3 backups.
  link: [the first backup is a full backup](../facts/backup.md#backup-s3-first-full-then-object-level-incremental)
  link: [incremental at object-level](../facts/backup.md#backup-s3-first-full-then-object-level-incremental)
backup-s3-general-purpose-buckets-only-no-directory-buckets
  claim: AWS Backup supports backup and restore of general purpose S3 buckets; directory buckets are not supported.
  scope: S3 bucket types.
  link: [general purpose S3 buckets](../facts/backup.md#backup-s3-general-purpose-buckets-only-no-directory-buckets)
  link: [Directory buckets are not supported](../facts/backup.md#backup-s3-general-purpose-buckets-only-no-directory-buckets)
backup-s3-glacier-archive-classes-not-supported
  claim: The archived storage classes S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are not supported for AWS Backup S3 backups.
  scope: S3 storage classes.
  link: [S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive are not supported](../facts/backup.md#backup-s3-glacier-archive-classes-not-supported)
  link: [archived storage classes](../facts/backup.md#backup-s3-glacier-archive-classes-not-supported)
backup-s3-kms-decrypt-then-reencrypt-with-vault-key
  claim: When backing up S3 objects encrypted with AWS KMS keys (SSE-KMS), AWS Backup calls kms:Decrypt against the source KMS key because it uses an independent encryption model for S3 backups: it first decrypts the data using the source KMS key, then re-encrypts it using the backup vault's KMS key.
  scope: S3 backups of SSE-KMS objects.
  link: [decrypt the data using the source KMS key](../facts/backup.md#backup-s3-kms-decrypt-then-reencrypt-with-vault-key)
  link: [re-encrypt it using the backup vault's KMS key](../facts/backup.md#backup-s3-kms-decrypt-then-reencrypt-with-vault-key)
backup-s3-no-cold-storage-transition
  claim: Cold storage transition of S3 backups is not supported.
  scope: S3 backups.
  link: [Cold storage transition of S3 backups is not supported](../facts/backup.md#backup-s3-no-cold-storage-transition)
  link: [S3 backups](../facts/backup.md#backup-s3-no-cold-storage-transition)
backup-s3-no-sse-c-no-bucket-config-no-outposts
  claim: AWS Backup does not support backups of SSE-C-encrypted S3 objects, of bucket configurations such as bucket policies, settings, names or access points, or of S3 on AWS Outposts.
  scope: S3 backups.
  link: [not offer support for backups of SSE-C-encrypted objects](../facts/backup.md#backup-s3-no-sse-c-no-bucket-config-no-outposts)
  link: [backups of bucket configurations](../facts/backup.md#backup-s3-no-sse-c-no-bucket-config-no-outposts)
backup-s3-only-resource-with-backup-tiering
  claim: Amazon S3 is the only resource that supports backup tiering to a lower cost warm storage tier.
  scope: backup tiering.
  link: [the only resource that supports backup tiering](../facts/backup.md#backup-s3-only-resource-with-backup-tiering)
  link: [lower cost warm storage tier](../facts/backup.md#backup-s3-only-resource-with-backup-tiering)
backup-s3-periodic-frequency-options
  claim: You can schedule periodic backups of S3 buckets in frequencies such as 1 hour, 12 hours, 1 day, 1 week, or 1 month.
  scope: periodic (snapshot) backups of Amazon S3 buckets; frequencies such as the ones listed.
  link: [1 hour, 12 hours, 1 day, 1 week, or 1 month](../facts/backup.md#backup-s3-periodic-frequency-options)
  link: [frequencies such as 1 hour](../facts/backup.md#backup-s3-periodic-frequency-options)
backup-s3-recommend-lifecycle-expiration-for-versions
  claim: For S3 backups, AWS recommends that you set a lifecycle expiration period for your S3 versions. All objects, including all versions, in the bucket when the backup begins are stored in the recovery point, and the storage cost is calculated for all objects in the backup, including objects scheduled for deletion.
  scope: S3 backups.
  link: [set a lifecycle expiration period for your S3 versions](../facts/backup.md#backup-s3-recommend-lifecycle-expiration-for-versions)
  link: [including objects scheduled for deletion](../facts/backup.md#backup-s3-recommend-lifecycle-expiration-for-versions)
backup-s3-requires-versioning-enabled
  claim: You must enable S3 Versioning on an S3 bucket to use AWS Backup for Amazon S3.
  scope: S3 buckets backed up by AWS Backup.
  link: [must enable S3 Versioning on your S3 bucket](../facts/backup.md#backup-s3-requires-versioning-enabled)
  link: [to use AWS Backup for Amazon S3](../facts/backup.md#backup-s3-requires-versioning-enabled)
backup-s3-restore-cross-region-copy-restores-in-copy-region
  claim: While S3 backups can be copied cross-Region, restore jobs occur only in the same Region in which the original backup or copy is located.
  scope: S3 restores.
  link: [restore jobs only occur in the same Region](../facts/backup.md#backup-s3-restore-cross-region-copy-restores-in-copy-region)
  link: [original backup or copy is located](../facts/backup.md#backup-s3-restore-cross-region-copy-restores-in-copy-region)
backup-s3-restore-latest-version-only-by-default
  claim: By default AWS Backup restores only the latest version of your S3 objects; you can choose to restore additional or all versions.
  scope: S3 restores; default; adjustable.
  link: [restores only the latest version of your objects](../facts/backup.md#backup-s3-restore-latest-version-only-by-default)
  link: [restore additional or all versions](../facts/backup.md#backup-s3-restore-latest-version-only-by-default)
backup-s3-restore-not-destructive-existing-objects-skipped
  claim: Restores of S3 objects are skipped if the destination bucket has an object with the same name or version ID. When you restore to the original S3 bucket, AWS Backup does not perform a destructive restore: it will not put an object into the bucket in place of an object that already exists, regardless of version; but a delete marker in the current version is treated as the object being nonexistent, so a restore can occur.
  scope: S3 restores; a current-version delete marker counts as no object, so that object can be restored.
  link: [does not perform a destructive restore](../facts/backup.md#backup-s3-restore-not-destructive-existing-objects-skipped)
  link: [same name or version ID](../facts/backup.md#backup-s3-restore-not-destructive-existing-objects-skipped)
backup-s3-restore-to-standard-all-or-specific-objects-existing-or-new-bucket
  claim: You can restore S3 data backed up with AWS Backup to the S3 Standard storage class, restoring all objects in a bucket or specific objects, into an existing or a new bucket.
  scope: S3 restores.
  link: [all the objects in a bucket](../facts/backup.md#backup-s3-restore-to-standard-all-or-specific-objects-existing-or-new-bucket)
  link: [an existing or new bucket](../facts/backup.md#backup-s3-restore-to-standard-all-or-specific-objects-existing-or-new-bucket)
backup-s3-single-backup-policy-central-encrypted-vault
  claim: You can use a single backup policy in AWS Backup to centrally automate backups of your application data, and AWS Backup organizes backups across AWS services and third-party applications in one centralized, encrypted backup vault.
  scope: AWS Backup central backup policies.
  link: [a single backup policy in AWS Backup](../facts/backup.md#backup-s3-single-backup-policy-central-encrypted-vault)
  link: [one centralized, encrypted location](../facts/backup.md#backup-s3-single-backup-policy-central-encrypted-vault)
backup-s3-system-tag-events-all-buckets-arn-events-1000
  claim: For S3 continuous backups, system tag-based event configuration supports all general purpose buckets in your account, matching your Amazon S3 bucket quota, while bucket-ARN-based event configuration supports up to 1,000 buckets per account.
  scope: per account, S3 buckets protected with the bucket-ARN method; maximum; not adjustable; bucket-ARN method is used when the backup role lacks s3:ListTagsForResource.
  link: [up to 1,000 buckets per account](../facts/backup.md#backup-s3-system-tag-events-all-buckets-arn-events-1000)
  link: [all general purpose buckets in your account](../facts/backup.md#backup-s3-system-tag-events-all-buckets-arn-events-1000)
  say: up to one thousand buckets per account
backup-sap-hana-on-ec2-via-backint
  claim: AWS Backup works with AWS Backint to support SAP HANA database backup and restore on Amazon EC2 instances.
  scope: SAP HANA on EC2.
  link: [AWS Backint to support SAP HANA database](../facts/backup.md#backup-sap-hana-on-ec2-via-backint)
  link: [on Amazon EC2 instances](../facts/backup.md#backup-sap-hana-on-ec2-via-backint)
backup-search-charges-index-search-storage-restore
  claim: Each backup index creation and each search job incurs a charge, each backup index has a storage charge, and each restore from search results is charged like other restore jobs.
  scope: AWS Backup search.
  link: [each search job incurs a charge](../facts/backup.md#backup-search-charges-index-search-storage-restore)
  link: [Each backup index has a storage charge](../facts/backup.md#backup-search-charges-index-search-storage-restore)
backup-search-find-files-or-objects-without-full-restore
  claim: AWS Backup search lets you search the metadata of backups of supported resource types for files or objects that match properties such as size, creation date and resource type, so you can find and restore just the specific file or object instead of restoring a full backup.
  scope: AWS Backup search.
  link: [search the metadata of your backups](../facts/backup.md#backup-search-find-files-or-objects-without-full-restore)
  link: [just the specific file or object](../facts/backup.md#backup-search-find-files-or-objects-without-full-restore)
backup-search-index-created-by-plan-opt-in
  claim: You can opt in to have a backup index created with each periodic backup of a supported resource type (continuous backups get daily indexes), and only recovery points that have an index can be included in a backup search.
  scope: AWS Backup backup plans.
  link: [created with each periodic backup](../facts/backup.md#backup-search-index-created-by-plan-opt-in)
  link: [continuous backups will have daily indexes created](../facts/backup.md#backup-search-index-created-by-plan-opt-in)
backup-search-needs-index-standard-vault-only
  claim: To be searchable, a recovery point must first have a corresponding index; recovery points of supported resource types can have a backup index if they are stored in a standard backup vault, and recovery points in a logically air-gapped vault do not currently support backup indexes.
  scope: AWS Backup search.
  link: [must first have a corresponding index](../facts/backup.md#backup-search-needs-index-standard-vault-only)
  link: [do not currently support backup indexes](../facts/backup.md#backup-search-needs-index-standard-vault-only)
backup-search-results-kept-7-days-export-to-s3
  claim: AWS Backup retains search results for 7 days from completion, and a best practice is to export the results to an S3 bucket to keep them longer.
  scope: AWS Backup search results; maximum; not adjustable.
  link: [retains search results for 7 days](../facts/backup.md#backup-search-results-kept-7-days-export-to-s3)
  link: [export your search results to an S3 bucket](../facts/backup.md#backup-search-results-kept-7-days-export-to-s3)
backup-service-must-exist-in-region
  claim: To use AWS Backup with a supported AWS service in a particular Region, that service must be available in the Region.
  scope: per Region.
  link: [the service must be available in the Region](../facts/backup.md#backup-service-must-exist-in-region)
  link: [in a particular Region](../facts/backup.md#backup-service-must-exist-in-region)
backup-service-opt-in-before-plan-assignment
  claim: Before you include a service in a backup plan, you opt in to using AWS Backup for that service, in the console or with the AWS CLI.
  scope: service opt-in, AWS Backup; applies before assigning resources of that service.
  link: [opt in to using AWS Backup](../facts/backup.md#backup-service-opt-in-before-plan-assignment)
  link: [console or AWS CLI](../facts/backup.md#backup-service-opt-in-before-plan-assignment)
backup-service-opt-in-checked-per-region
  claim: The describe-region-settings command shows which services you have opted into in a specific Region, so the service opt-in is a Region setting.
  scope: per Region.
  link: [opted into in a specific Region](../facts/backup.md#backup-service-opt-in-checked-per-region)
  link: [describe-region-settings](../facts/backup.md#backup-service-opt-in-checked-per-region)
backup-snapshot-hourly-and-100-years
  claim: Snapshot backups can be taken as frequently as every hour, and they can be stored for up to a maximum of 100 years.
  scope: snapshot backups (not continuous backups); maximum; not adjustable.
  link: [as frequently as every hour](../facts/backup.md#backup-snapshot-hourly-and-100-years)
  link: [a maximum of 100 years](../facts/backup.md#backup-snapshot-hourly-and-100-years)
  say: as often as every hour | up to one hundred years
backup-sns-cross-account-and-fifo-topics-unsupported
  claim: Although Amazon SNS allows cross-account notifications, AWS Backup does not currently support this, and AWS Backup does not currently support SNS FIFO topics, only Standard topics.
  scope: AWS Backup SNS notifications.
  link: [AWS Backup does not currently support this feature](../facts/backup.md#backup-sns-cross-account-and-fifo-topics-unsupported)
  link: [does not currently support SNS FIFO topics](../facts/backup.md#backup-sns-cross-account-and-fifo-topics-unsupported)
backup-source-ec2-must-be-running-or-stopped
  claim: To back up an EC2 instance, the instance can be running or stopped but not terminated, because only a running or stopped instance can communicate with AWS Backup.
  scope: EC2 instances.
  link: [can be in the running or stopped state](../facts/backup.md#backup-source-ec2-must-be-running-or-stopped)
  link: [but not the terminated state](../facts/backup.md#backup-source-ec2-must-be-running-or-stopped)
backup-storage-gateway-volume-gateway-supported
  claim: AWS Backup supports Storage Gateway Volume Gateway, and you can restore EBS snapshots as Storage Gateway volumes.
  scope: AWS Storage Gateway.
  link: [AWS Backup supports Storage Gateway Volume Gateway](../facts/backup.md#backup-storage-gateway-volume-gateway-supported)
  link: [restore Amazon EBS snapshots as Storage Gateway volumes](../facts/backup.md#backup-storage-gateway-volume-gateway-supported)
backup-supported-resource-aurora
  claim: AWS Backup supports Amazon Aurora clusters.
  scope: supported resource types.
  link: [Aurora clusters](../facts/backup.md#backup-supported-resource-aurora)
  link: [Amazon Aurora](../facts/backup.md#backup-supported-resource-aurora)
backup-supported-resource-dynamodb
  claim: AWS Backup supports Amazon DynamoDB tables.
  scope: supported resource types.
  link: [Amazon DynamoDB tables](../facts/backup.md#backup-supported-resource-dynamodb)
  link: [Amazon DynamoDB](../facts/backup.md#backup-supported-resource-dynamodb)
backup-supported-resource-ebs
  claim: AWS Backup supports Amazon EBS volumes.
  scope: supported resource types.
  link: [Amazon EBS volumes](../facts/backup.md#backup-supported-resource-ebs)
  link: [Amazon Elastic Block Store (Amazon EBS)](../facts/backup.md#backup-supported-resource-ebs)
backup-supported-resource-ec2
  claim: AWS Backup supports Amazon EC2 instances that are backed by Amazon EBS volumes.
  scope: supported resource types.
  link: [Amazon EC2 instances backed by Amazon EBS volumes](../facts/backup.md#backup-supported-resource-ec2)
  link: [Amazon Elastic Compute Cloud (Amazon EC2)](../facts/backup.md#backup-supported-resource-ec2)
backup-supported-resource-efs
  claim: AWS Backup supports Amazon EFS file systems.
  scope: supported resource types.
  link: [Amazon EFS file systems](../facts/backup.md#backup-supported-resource-efs)
  link: [Amazon Elastic File System (Amazon EFS)](../facts/backup.md#backup-supported-resource-efs)
backup-supported-resource-rds
  claim: AWS Backup supports Amazon RDS database instances of all database engines and Multi-Availability Zone clusters.
  scope: supported resource types.
  link: [including all database engines](../facts/backup.md#backup-supported-resource-rds)
  link: [Multi-Availability Zone clusters](../facts/backup.md#backup-supported-resource-rds)
backup-supported-resource-s3
  claim: AWS Backup supports Amazon S3 data.
  scope: supported resource types.
  link: [Amazon S3 data](../facts/backup.md#backup-supported-resource-s3)
  link: [Amazon Simple Storage Service (Amazon S3)](../facts/backup.md#backup-supported-resource-s3)
backup-tag-integration-group-resources
  claim: Integration with AWS tags lets you quickly apply a backup plan to a group of resources so that they are backed up consistently and in a compliant manner.
  scope: AWS Backup tag-based assignment.
  link: [quickly apply a backup plan to a group](../facts/backup.md#backup-tag-integration-group-resources)
  link: [consistent and compliant manner](../facts/backup.md#backup-tag-integration-group-resources)
backup-tiering-applies-to-existing-and-new-backups
  claim: Tiering configurations apply to both existing backup data in vaults and new backups created after the configuration is established.
  scope: S3 backup tiering.
  link: [both existing backup data in vaults](../facts/backup.md#backup-tiering-applies-to-existing-and-new-backups)
  link: [created after the configuration is established](../facts/backup.md#backup-tiering-applies-to-existing-and-new-backups)
backup-tiering-delete-config-keeps-existing-data
  claim: Deleting a tiering configuration keeps existing data in the lower-cost tier but prevents new data from tiering down.
  scope: S3 backup tiering configurations.
  link: [keeps existing data in the lower-cost tier](../facts/backup.md#backup-tiering-delete-config-keeps-existing-data)
  link: [prevents new data from tiering down](../facts/backup.md#backup-tiering-delete-config-keeps-existing-data)
backup-tiering-irreversible
  claim: S3 backup tiering is irreversible: once objects move to the lower-cost tier, they remain there until the backup is deleted according to the retention policies.
  scope: S3 backup tiering.
  link: [irreversible](../facts/backup.md#backup-tiering-irreversible)
  link: [remain there until the backup is deleted](../facts/backup.md#backup-tiering-irreversible)
backup-tiering-max-100-resources
  claim: Up to 100 specific resources across all resource groups can be selected per S3 backup tiering configuration.
  scope: per S3 backup tiering configuration, across all resource groups; maximum; not adjustable.
  link: [Up to 100 specific resources](../facts/backup.md#backup-tiering-max-100-resources)
  say: up to one hundred specific resources
backup-tiering-max-5-resource-selections
  claim: A vault-specific S3 backup tiering configuration supports up to 5 different resource groups with their tiering settings.
  scope: per vault-specific S3 backup tiering configuration; maximum; not adjustable.
  link: [up to 5 different resource group](../facts/backup.md#backup-tiering-max-5-resource-selections)
  say: up to five resource groups
backup-tiering-min-60-days-daily-check
  claim: AWS Backup checks object age daily and moves eligible objects to the lower-cost tier; objects become eligible when they reach the specified age threshold, which has a minimum of 60 days.
  scope: S3 backup tiering configurations; minimum; not adjustable.
  link: [minimum 60 days](../facts/backup.md#backup-tiering-min-60-days-daily-check)
  link: [on a daily basis](../facts/backup.md#backup-tiering-min-60-days-daily-check)
  say: at least sixty days
backup-tiering-one-config-per-vault
  claim: Each vault can only have one S3 tiering configuration apart from the default configuration, and if both an all-vaults and a specific vault configuration exist, the specific vault configuration takes priority.
  scope: per vault, S3 backup tiering; maximum; apart from the default configuration.
  link: [only have one tiering configuration](../facts/backup.md#backup-tiering-one-config-per-vault)
  link: [specific vault configuration takes priority](../facts/backup.md#backup-tiering-one-config-per-vault)
backup-tiering-s3-lower-cost-tier-up-to-30-percent
  claim: AWS Backup offers a lower-cost warm storage tier for Amazon S3 backups that reduces long-term storage costs by up to 30% while keeping the same performance and features as the warm storage tier.
  scope: Amazon S3 backups in AWS Backup; maximum.
  link: [up to 30%](../facts/backup.md#backup-tiering-s3-lower-cost-tier-up-to-30-percent)
  link: [lower-cost warm storage tier for Amazon S3 backups](../facts/backup.md#backup-tiering-s3-lower-cost-tier-up-to-30-percent)
  say: up to thirty percent
backup-tiering-scope-all-vaults-or-targeted
  claim: You can configure S3 backup tiering for all S3 backups for all vaults in an account, or create targeted configurations for specific vaults and protected resources.
  scope: S3 backup tiering configurations.
  link: [all S3 backups for all vaults in an account](../facts/backup.md#backup-tiering-scope-all-vaults-or-targeted)
  link: [targeted configurations for specific vaults and protected resources](../facts/backup.md#backup-tiering-scope-all-vaults-or-targeted)
backup-tiering-three-cost-components-one-time-transition-fee
  claim: Backup tiering has three cost components (warm storage tier, low-cost warm storage tier and transition costs), and moving data to the lower-cost tier incurs a one-time per-object transition fee based on the number of objects eligible for tiering.
  scope: S3 backup tiering.
  link: [three cost components](../facts/backup.md#backup-tiering-three-cost-components-one-time-transition-fee)
  link: [one-time per-object transition fee](../facts/backup.md#backup-tiering-three-cost-components-one-time-transition-fee)
backup-user-notifications-view-job-progress-and-changes
  claim: With AWS User Notifications you can view the progress of backup, copy and restore jobs and changes to your backup policies, vaults, recovery points and settings from the Notification Center.
  scope: AWS Backup notifications.
  link: [your backup, copy, and restore jobs](../facts/backup.md#backup-user-notifications-view-job-progress-and-changes)
  link: [Notification Center](../facts/backup.md#backup-user-notifications-view-job-progress-and-changes)
backup-vault-access-policy-allow-create-limit-delete
  claim: You can assign policies to backup vaults and the resources in them, for example to let users create backup plans and on-demand backups but limit their ability to delete recovery points.
  scope: backup vault access policies.
  link: [limit their ability to delete recovery points](../facts/backup.md#backup-vault-access-policy-allow-create-limit-delete)
  link: [assign policies to backup vaults](../facts/backup.md#backup-vault-access-policy-allow-create-limit-delete)
backup-vault-access-policy-controls-only-backup-apis
  claim: Vault access policies control only user access to AWS Backup APIs; backups such as EBS and RDS snapshots can also be reached through those services' own APIs, so you need separate IAM policies for them to control access fully.
  scope: AWS Backup vault access policies.
  link: [only control user access to AWS Backup APIs](../facts/backup.md#backup-vault-access-policy-controls-only-backup-apis)
  link: [separate access policies in IAM](../facts/backup.md#backup-vault-access-policy-controls-only-backup-apis)
backup-vault-access-policy-no-wildcard-action
  claim: Unlike other IAM-based policies, AWS Backup vault access policies do not support a wildcard in the Action key.
  scope: AWS Backup vault access policies.
  link: [don't support a wildcard](../facts/backup.md#backup-vault-access-policy-no-wildcard-action)
  link: [in the Action key](../facts/backup.md#backup-vault-access-policy-no-wildcard-action)
backup-vault-backups-immutable-content-and-survive-source-deletion
  claim: The content of each AWS Backup backup is immutable, and backup vaults keep backups separate from their source instances, so a vault keeps EC2 and EBS backups per the lifecycle policy even if you delete the source instance and volumes.
  scope: AWS Backup recovery points and vaults.
  link: [no one can alter that content](../facts/backup.md#backup-vault-backups-immutable-content-and-survive-source-deletion)
  link: [even if you delete the source Amazon EC2 instance and Amazon EBS volumes](../facts/backup.md#backup-vault-backups-immutable-content-and-survive-source-deletion)
backup-vault-container-and-key-for-some-backups
  claim: A backup vault is a container that stores and organizes your backups, and when you create it you must specify the KMS key that encrypts some of the backups in it, while the encryption of other backups is managed by their source services.
  scope: AWS Backup vaults.
  link: [a container that stores and organizes your backups](../facts/backup.md#backup-vault-container-and-key-for-some-backups)
  link: [managed by their source AWS services](../facts/backup.md#backup-vault-container-and-key-for-some-backups)
backup-vault-default-key-aws-backup-alias
  claim: By default AWS Backup creates a KMS key with the alias aws/backup for the vault; you can choose that key or any other key in your account.
  scope: backup vault KMS key; default; adjustable.
  link: [KMS key with the alias aws/backup](../facts/backup.md#backup-vault-default-key-aws-backup-alias)
  link: [any other key in your account](../facts/backup.md#backup-vault-default-key-aws-backup-alias)
backup-vault-delete-only-when-empty
  claim: You can delete a backup vault only after you delete (or your backup plan lifecycles expire) all the recovery points in it, to guard against accidental or malicious mass deletion.
  scope: backup vault deletion.
  link: [only after you delete](../facts/backup.md#backup-vault-delete-only-when-empty)
  link: [accidental or malicious mass deletion](../facts/backup.md#backup-vault-delete-only-when-empty)
backup-vault-key-applies-only-to-independent-encryption-types
  claim: The encryption key specified in an AWS Backup vault applies to the backups of certain resource types, and backups of all other resource types are backed up using the key that is used to encrypt the source resource. AWS Backup offers independent encryption, controlled through the AWS KMS key configuration in the backup vault, for resource types that support full AWS Backup management.
  scope: backup vault KMS key; resource types with full AWS Backup management use the vault key; other types keep the source key.
  link: [applies to the backups of certain resource types](../facts/backup.md#backup-vault-key-applies-only-to-independent-encryption-types)
  link: [used to encrypt the source resource](../facts/backup.md#backup-vault-key-applies-only-to-independent-encryption-types)
backup-vault-kms-key-fixed-after-creation
  claim: After you create a backup vault and set its KMS encryption key, you cannot edit the key for that vault.
  scope: backup vault encryption key.
  link: [can no longer edit the key](../facts/backup.md#backup-vault-kms-key-fixed-after-creation)
  link: [After you create a backup vault](../facts/backup.md#backup-vault-kms-key-fixed-after-creation)
backup-vault-lock-account-closure-deletes-vault-after-90-days
  claim: If you close an AWS account that contains a backup vault, AWS suspends the account for 90 days with backups intact, and if you do not reopen it in that time AWS deletes the vault contents even when Vault Lock was in place.
  scope: closing an AWS account with a locked vault.
  link: [suspend your account for 90 days](../facts/backup.md#backup-vault-lock-account-closure-deletes-vault-after-90-days)
  link: [AWS Backup Vault Lock was in place](../facts/backup.md#backup-vault-lock-account-closure-deletes-vault-after-90-days)
backup-vault-lock-cohasset-assessment-sec-cftc-finra
  claim: AWS Backup Vault Lock has been assessed by Cohasset Associates for use in environments subject to SEC 17a-4, CFTC and FINRA regulations.
  scope: AWS Backup Vault Lock.
  link: [assessed by Cohasset Associates](../facts/backup.md#backup-vault-lock-cohasset-assessment-sec-cftc-finra)
  link: [SEC 17a-4, CFTC, and FINRA regulations](../facts/backup.md#backup-vault-lock-cohasset-assessment-sec-cftc-finra)
backup-vault-lock-compliance-config-fixed-while-recovery-points
  claim: When a lock is active in compliance mode and the grace time is over, the vault configuration cannot be altered or deleted by a customer, an account or data owner, or AWS as long as the vault contains recovery points.
  scope: Vault Lock, compliance mode, after the grace time; the vault holds recovery points.
  link: [cannot be altered or deleted by a customer](../facts/backup.md#backup-vault-lock-compliance-config-fixed-while-recovery-points)
  link: [as long as it contains recovery points](../facts/backup.md#backup-vault-lock-compliance-config-fixed-while-recovery-points)
backup-vault-lock-compliance-grace-time-remove-or-change
  claim: In compliance mode, a locked vault cannot be deleted after the grace time ends if any recovery points are in it, but during the grace time you can still remove the vault lock and change its configuration.
  scope: Vault Lock, compliance mode; grace time not yet expired.
  link: [you can still remove the vault lock](../facts/backup.md#backup-vault-lock-compliance-grace-time-remove-or-change)
  link: [cooling-off period](../facts/backup.md#backup-vault-lock-compliance-grace-time-remove-or-change)
backup-vault-lock-compliance-immutable-by-anyone
  claim: A vault lock in compliance mode cannot be altered or deleted by any user or by AWS; it has a grace time period you set, after which the contents and the vault lock become immutable.
  scope: Vault Lock, compliance mode; immutable after the grace time ends.
  link: [cannot be altered or deleted by any user](../facts/backup.md#backup-vault-lock-compliance-immutable-by-anyone)
  link: [grace time period you set](../facts/backup.md#backup-vault-lock-compliance-immutable-by-anyone)
backup-vault-lock-compliance-intent-lock-cannot-be-removed
  claim: Compliance mode is meant for vaults whose contents should never be deleted or altered until the retention period ends; once locked, the lock cannot be removed, though the vault itself can be deleted if it is empty.
  scope: Vault Lock, compliance mode; vault empty to be deletable.
  link: [the lock cannot be removed](../facts/backup.md#backup-vault-lock-compliance-intent-lock-cannot-be-removed)
  link: [expected to never be deleted or altered](../facts/backup.md#backup-vault-lock-compliance-intent-lock-cannot-be-removed)
backup-vault-lock-denies-delete-and-lifecycle-change-even-root
  claim: If any user, including the root user, tries to delete a backup or change its lifecycle properties in a locked vault, AWS Backup denies the operation.
  scope: locked backup vault.
  link: [including the root user](../facts/backup.md#backup-vault-lock-denies-delete-and-lifecycle-change-even-root)
  link: [AWS Backup will deny the operation](../facts/backup.md#backup-vault-lock-denies-delete-and-lifecycle-change-even-root)
backup-vault-lock-enforced-even-during-grace-time
  claim: While a vault is locked, delete or update operations on the recovery points in it fail, even while you are still within the grace time.
  scope: locked vault (Locked true).
  link: [delete or update operations to the recovery points](../facts/backup.md#backup-vault-lock-enforced-even-during-grace-time)
  link: [still in the cooling-off grace time period](../facts/backup.md#backup-vault-lock-enforced-even-during-grace-time)
backup-vault-lock-enforces-retention-against-privileged-users
  claim: Vault Lock enforces backup lifecycle retention periods, which prevents early deletions by privileged users, including the AWS account root user.
  scope: AWS Backup Vault Lock.
  link: [prevent early deletions by privileged users](../facts/backup.md#backup-vault-lock-enforces-retention-against-privileged-users)
  link: [AWS account root user](../facts/backup.md#backup-vault-lock-enforces-retention-against-privileged-users)
backup-vault-lock-governance-intent-designated-personnel
  claim: Governance mode lets only users with sufficient IAM privileges manage the vault, which helps an organization ensure only designated personnel can change a backup vault.
  scope: Vault Lock, governance mode.
  link: [only designated personnel can make changes](../facts/backup.md#backup-vault-lock-governance-intent-designated-personnel)
  link: [sufficient IAM privileges](../facts/backup.md#backup-vault-lock-governance-intent-designated-personnel)
backup-vault-lock-governance-lock-removable-with-iam
  claim: A vault locked in governance mode can have its lock removed, and the vault managed or deleted, by users with sufficient IAM permissions.
  scope: Vault Lock, governance mode.
  link: [lock removed by users with sufficient IAM permissions](../facts/backup.md#backup-vault-lock-governance-lock-removable-with-iam)
  link: [who have the appropriate IAM permissions](../facts/backup.md#backup-vault-lock-governance-lock-removable-with-iam)
backup-vault-lock-grace-time-minimum-3-days
  claim: In compliance mode, a vault lock has a cooling-off period from the creation of the vault lock until the vault and its lock become immutable; you choose the duration of this period, called grace time, and it must be at least 3 days (72 hours).
  scope: compliance-mode Vault Lock (ChangeableForDays); minimum; not adjustable; compliance mode only.
  link: [at least 3 days (72 hours)](../facts/backup.md#backup-vault-lock-grace-time-minimum-3-days)
  say: at least three days
backup-vault-lock-locked-backups-persist-until-lifecycle-ends
  claim: Backups within a locked vault cannot be deleted until their lifecycle completes, which gives persistent costs if retention is set too long; a recovery point with retention set to Always is kept forever once the grace time expires.
  scope: locked vault; the grace time has expired for the Always example.
  link: [cannot be deleted until their lifecycle completes](../facts/backup.md#backup-vault-lock-locked-backups-persist-until-lifecycle-ends)
  link: [retained forever](../facts/backup.md#backup-vault-lock-locked-backups-persist-until-lifecycle-ends)
backup-vault-lock-max-retention-36500-days
  claim: The longest maximum retention period you can set in a Vault Lock configuration is 36500 days, approximately 100 years.
  scope: MaxRetentionDays of an AWS Backup Vault Lock; maximum; not adjustable.
  link: [36500 days](../facts/backup.md#backup-vault-lock-max-retention-36500-days)
  link: [approximately 100 years](../facts/backup.md#backup-vault-lock-max-retention-36500-days)
  say: thirty-six thousand five hundred days
backup-vault-lock-min-max-retention-fail-nonconforming-jobs
  claim: With a vault lock minimum and maximum retention, new backup and copy jobs that do not conform fail, while recovery points already in the vault keep their previous lifecycle settings.
  scope: Vault Lock min and max retention.
  link: [will fail if they do not conform](../facts/backup.md#backup-vault-lock-min-max-retention-fail-nonconforming-jobs)
  link: [recovery points that are already in the vault](../facts/backup.md#backup-vault-lock-min-max-retention-fail-nonconforming-jobs)
backup-vault-lock-min-retention-1-day
  claim: The shortest minimum retention period you can set in a Vault Lock configuration is 1 day.
  scope: MinRetentionDays of an AWS Backup Vault Lock; minimum; not adjustable.
  link: [1 day](../facts/backup.md#backup-vault-lock-min-retention-1-day)
  say: one day
backup-vault-lock-mode-set-by-changeable-for-days
  claim: In the API, a vault lock is created in governance mode when you leave out ChangeableForDays; if you include that parameter, the lock is created in compliance mode.
  scope: PutBackupVaultLockConfiguration.
  link: [do not include ChangeableForDays](../facts/backup.md#backup-vault-lock-mode-set-by-changeable-for-days)
  link: [created in compliance mode](../facts/backup.md#backup-vault-lock-mode-set-by-changeable-for-days)
backup-vault-lock-no-extra-charge-storage-charges-apply
  claim: AWS Backup Vault Lock is available at no additional charge, and standard AWS Backup storage charges apply to backups stored in a locked vault.
  scope: AWS Backup Vault Lock.
  link: [available at no additional charge](../facts/backup.md#backup-vault-lock-no-extra-charge-storage-charges-apply)
  link: [Standard AWS Backup storage charges apply](../facts/backup.md#backup-vault-lock-no-extra-charge-storage-charges-apply)
backup-vault-lock-not-glacier-vault-lock
  claim: AWS Backup Vault Lock is not the same feature as Amazon Glacier Vault Lock, which is compatible only with Amazon Glacier.
  scope: Vault Lock features compared.
  link: [not the same feature as Amazon Glacier](../facts/backup.md#backup-vault-lock-not-glacier-vault-lock)
  link: [compatible only with Amazon Glacier](../facts/backup.md#backup-vault-lock-not-glacier-vault-lock)
backup-vault-lock-one-lock-per-vault
  claim: Each vault can have one vault lock in place.
  scope: per backup vault; maximum; not adjustable.
  link: [one vault lock](../facts/backup.md#backup-vault-lock-one-lock-per-vault)
  link: [Each vault](../facts/backup.md#backup-vault-lock-one-lock-per-vault)
backup-vault-lock-prevents-anyone-including-you-deleting
  claim: You can use AWS Backup Vault Lock to prevent anyone (including you) from deleting backups or altering their retention period, which helps enforce a write-once-read-many (WORM) model; vaults locked in governance mode, however, can have the lock removed by users with sufficient IAM permissions.
  scope: AWS Backup Vault Lock; a governance-mode lock can be removed by users with sufficient IAM permissions.
  link: [prevent anyone (including you) from deleting backups](../facts/backup.md#backup-vault-lock-prevents-anyone-including-you-deleting)
  link: [write-once-read-many](../facts/backup.md#backup-vault-lock-prevents-anyone-including-you-deleting)
backup-vault-lock-retention-periods-optional-no-enforcement-if-unset
  claim: If you do not set a maximum (or minimum) retention period, Vault Lock does not enforce one.
  scope: Vault Lock min and max retention; default; not adjustable.
  link: [will not enforce a maximum retention period](../facts/backup.md#backup-vault-lock-retention-periods-optional-no-enforcement-if-unset)
  link: [will not enforce a minimum retention period](../facts/backup.md#backup-vault-lock-retention-periods-optional-no-enforcement-if-unset)
backup-vault-lock-two-modes-governance-compliance
  claim: When you create a Vault Lock you choose between two modes: governance mode or compliance mode.
  scope: AWS Backup Vault Lock.
  link: [Governance mode](../facts/backup.md#backup-vault-lock-two-modes-governance-compliance)
  link: [Compliance mode](../facts/backup.md#backup-vault-lock-two-modes-governance-compliance)
backup-vault-lock-worm-and-extra-defense-benefits
  claim: Vault Lock gives a write-once, read-many (WORM) configuration for all backups in a vault and an additional layer of defense against inadvertent or malicious deletion.
  scope: AWS Backup Vault Lock.
  link: [WORM (write-once, read-many) configuration](../facts/backup.md#backup-vault-lock-worm-and-extra-defense-benefits)
  link: [inadvertent or malicious deletions](../facts/backup.md#backup-vault-lock-worm-and-extra-defense-benefits)
backup-vault-policy-cross-account-only-copy-into-vault
  claim: Regardless of a vault access policy, AWS Backup rejects cross-account access for any action other than backup:CopyIntoBackupVault; this restriction applies to vault access policies on both standard and logically air-gapped vaults. Logically air-gapped vaults additionally support cross-account sharing through AWS RAM, which enables operations such as restore through a separate mechanism outside of vault access policies.
  scope: vault access policies, standard and logically air-gapped vaults; AWS RAM sharing of logically air-gapped vaults is a separate mechanism.
  link: [other than backup:CopyIntoBackupVault will be rejected](../facts/backup.md#backup-vault-policy-cross-account-only-copy-into-vault)
  link: [both standard and logically air-gapped backup vaults](../facts/backup.md#backup-vault-policy-cross-account-only-copy-into-vault)
backup-vault-policy-deny-delete-recovery-point-except-principal
  claim: A resource-based access policy on a backup vault can prevent anyone except named principals from deleting a recovery point in that vault.
  scope: backup vault access policy.
  link: [resource-based access policy on a backup vault](../facts/backup.md#backup-vault-policy-deny-delete-recovery-point-except-principal)
  link: [from deleting a recovery point](../facts/backup.md#backup-vault-policy-deny-delete-recovery-point-except-principal)
backup-vault-required-before-plan-or-job
  claim: You must create at least one backup vault before you create a backup plan or start a backup job.
  scope: AWS Backup vaults.
  link: [at least one vault](../facts/backup.md#backup-vault-required-before-plan-or-job)
  link: [before creating a backup plan](../facts/backup.md#backup-vault-required-before-plan-or-job)
backup-vault-sets-kms-key-and-access
  claim: You can use backup vaults to set the AWS KMS encryption key that is used to encrypt backups in the vault and to control access to the backups in the vault; the vault key applies to the backups of certain resource types, and backups of all other resource types use the key that encrypts the source resource.
  scope: backup vault.
  link: [encryption key that is used to encrypt backups](../facts/backup.md#backup-vault-sets-kms-key-and-access)
  link: [control access to the backups](../facts/backup.md#backup-vault-sets-kms-key-and-access)
backup-vmware-vms-on-premises-and-vmc
  claim: AWS Backup protects on-premises VMware virtual machines and VMs in VMware Cloud on AWS: you can back them up to AWS Backup and restore them to either on premises or VMware Cloud.
  scope: VMware virtual machines.
  link: [on-premises VMware virtual machines](../facts/backup.md#backup-vmware-vms-on-premises-and-vmc)
  link: [to either on premises or VMC](../facts/backup.md#backup-vmware-vms-on-premises-and-vmc)
backup-what-is-fully-managed-centralize
  claim: AWS Backup is a fully managed service that centralizes and automates data protection across AWS services, in the cloud and on premises.
  scope: AWS Backup.
  link: [fully-managed service](../facts/backup.md#backup-what-is-fully-managed-centralize)
  link: [centralize and automate data protection](../facts/backup.md#backup-what-is-fully-managed-centralize)
  link: [in the cloud, and on premises](../facts/backup.md#backup-what-is-fully-managed-centralize)
backup-window-jobs-start-within-window
  claim: A backup window consists of the time the window begins and its duration in hours, and backup jobs are started within this window.
  scope: backup rules.
  link: [Backup jobs are started within this window](../facts/backup.md#backup-window-jobs-start-within-window)
  link: [duration of the window in hours](../facts/backup.md#backup-window-jobs-start-within-window)
backup-windows-vss-application-consistent-ec2-only
  claim: With AWS Backup you can back up and restore VSS-enabled Windows applications running on Amazon EC2 instances; if the application has a VSS writer registered with Windows VSS, AWS Backup creates a snapshot that is consistent for that application. AWS Backup only supports application-consistent backups of resources running on Amazon EC2, and not all instance types or applications are supported for Windows VSS backups.
  scope: Windows VSS backups on EC2.
  link: [VSS writer registered with Windows VSS](../facts/backup.md#backup-windows-vss-application-consistent-ec2-only)
  link: [only supports application-consistent backups of resources running on Amazon EC2](../facts/backup.md#backup-windows-vss-application-consistent-ec2-only)
backup-windows-vss-ssm-agent-required
  claim: For Windows VSS backups, you must download, install and configure the SSM agent in AWS Systems Manager; this step is required.
  scope: Windows VSS backups on EC2.
  link: [This step is required](../facts/backup.md#backup-windows-vss-ssm-agent-required)
  link: [SSM agent in AWS Systems Manager](../facts/backup.md#backup-windows-vss-ssm-agent-required)
