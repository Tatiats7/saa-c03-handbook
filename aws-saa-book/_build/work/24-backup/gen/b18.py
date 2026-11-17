import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
MP, BS, BT, BN, IR, DR, W, CP = D + "malware-protection", D + "backup-search", D + "backup-tiering", D + "backup-notifications", D + "iam-service-roles", D + "disaster-recovery-resiliency", D + "whatisbackup", D + "creating-a-backup-plan"
f = []
FC = dict(vol="frequently-changing")
f.append(F("backup-malware-scanning-by-guardduty-automate-or-on-demand", "capability",
 "Malware scanning of your backups is provided by Amazon GuardDuty Malware Protection, which lets you automate scanning of recovery points through existing backup workflows or start on-demand scans of previously created backups.",
 "Which service scans AWS Backup recovery points for malware and how can scans be started?",
 ["Malware scanning of your backups is provided by Amazon GuardDuty Malware Protection", "initiate on-demand scans of previously created backups"],
 [E(MP, "Malware scanning of your backups is provided by Amazon GuardDuty Malware Protection. Using Amazon GuardDuty Malware Protection for AWS Backup allows you to automate scanning of recovery points through existing backup workflows, or initiate on-demand scans of previously created backups.")],
 scope="AWS Backup malware protection", tier0=True, bullets=["2.2.S5"], **FC))
f.append(F("backup-malware-scan-resource-types-selected-per-plan", "behavior",
 "When you configure malware protection in a backup plan you specify which resource types to scan (EC2, EBS, S3 or all supported resources) and the scan type (full or incremental); malware scanning applies only to the selected resource types.",
 "Which resources does malware scanning cover in a backup plan?",
 ["specify which resource types to scan", "Malware scanning applies only to your selected resource types"],
 [E(CP, "When configuring malware protection, specify which resource types to scan (Amazon EC2, Amazon EBS, Amazon S3, or all supported resources) and the scanning types (full or incremental). Malware scanning applies only to your selected resource types.")],
 scope="AWS Backup malware protection in backup plans", bullets=["2.2.S5"], **FC))
f.append(F("backup-malware-on-demand-scan-find-last-clean-backup", "behavior",
 "AWS Backup recommends on-demand scans to identify your last clean backup, and a full scan before a restore so the entire backup is examined with the latest threat detection model.",
 "How do you find the last clean recovery point before a restore?",
 ["using on-demand scans to identify your last clean backup", "use a full scan to examine the entire backup"],
 [E(MP, "AWS Backup recommends using on-demand scans to identify your last clean backup. When scanning before a restore operation, use a full scan to examine the entire backup with the latest threat detection model.")],
 scope="AWS Backup malware protection", tier0=True, bullets=["2.2.S5"], **FC))
f.append(F("backup-malware-two-iam-roles-required", "restriction",
 "AWS Backup malware scanning requires two IAM roles: the backup role with a managed policy that lets AWS Backup start scans, and a new scanner role with the AWSBackupGuardDutyRolePolicyForScans policy that trusts malware-protection.guardduty.amazonaws.com.",
 "How many IAM roles does AWS Backup malware scanning need?",
 ["requires two IAM roles", "trusts malware-protection.guardduty.amazonaws.com"],
 [E(MP, "AWS Backup malware scanning requires two IAM roles to scan your recovery points for potential malware:"),
  E(MP, "Second, a new scanner role is required with AWSBackupGuardDutyRolePolicyForScans managed policy that trusts malware-protection.guardduty.amazonaws.com.")],
 scope="AWS Backup malware protection", rel="extended", bullets=["2.2.S5", "1.3.S1"], **FC))
f.append(F("backup-malware-incremental-vs-full-scans", "behavior",
 "Incremental scans analyze only the data that changed between the target and base recovery point and are faster and cheaper, while full scans examine the entire recovery point, take longer and cost more.",
 "How do incremental and full malware scans differ?",
 ["analyze only the data that changed between the target and base recovery point", "examine the entire recovery point regardless of previous scans"],
 [E(MP, "Incremental scans analyze only the data that changed between the target and base recovery point. These scans are faster and more cost-effective for regular scanning, making them ideal for frequent periodic backups where you want to scan newly backed up data."),
  E(MP, "Full scans examine the entire recovery point regardless of previous scans. While these scans provide comprehensive coverage, they take longer to complete and incur higher costs.")],
 scope="AWS Backup malware scans", rel="extended", bullets=["2.2.S5", "4.3.S1"], **FC))
f.append(F("backup-malware-billed-by-guardduty-not-backup", "pricing-dimension",
 "Malware protection for AWS Backup is provided and billed by Amazon GuardDuty; you do not see AWS Backup charges for it and all usage appears under Amazon GuardDuty billing.",
 "Who bills for malware scanning of backups?",
 ["provided and billed by Amazon GuardDuty", "will not see any AWS Backup charges related to using this feature"],
 [E(MP, "Malware protection is provided and billed by Amazon GuardDuty. You will not see any AWS Backup charges related to using this feature. All usage can be viewed under Amazon GuardDuty's billing.")],
 scope="AWS Backup malware protection", tier0=True, bullets=["2.2.S5", "4.3.S1"], **FC))
f.append(F("backup-malware-scan-results-threats-found-or-not", "behavior",
 "A malware scan result of NO_THREATS_FOUND means no potential malware was detected, while THREATS_FOUND means potential malware was discovered.",
 "What do the malware scan results of AWS Backup mean?",
 ["NO_THREATS_FOUND", "THREATS_FOUND"],
 [E(MP, "A `NO_THREATS_FOUND` status means no potential malware was detected, while `THREATS_FOUND` indicates potential malware was discovered.")],
 scope="AWS Backup malware scan results", rel="extended", bullets=["2.2.S5"], **FC))
# Search
f.append(F("backup-search-find-files-or-objects-without-full-restore", "capability",
 "AWS Backup search lets you search the metadata of backups of supported resource types for files or objects that match properties such as size, creation date and resource type, so you can find and restore just the specific file or object instead of restoring a full backup.",
 "Can you find and restore a single file or object from a backup without restoring everything?",
 ["search the metadata of your backups of supported resource types", "find and restore just the specific file or object you require"],
 [E(BS, "AWS Backup offers the ability for you to search the metadata of your backups of supported resource types at a granular level for files or objects that match the properties you define in your search, such as size, creation date, and resource type."),
  E(BS, "Restoring a full backup just to find the specific item that might be in it can take hours or days. Instead, with a backup search, you can find and restore just the specific file or object you require.")],
 scope="AWS Backup search", tier0=True, bullets=["1.3.K2"], **FC))
f.append(F("backup-search-needs-index-standard-vault-only", "restriction",
 "A recovery point must have a backup index to be searchable, and only recovery points in a standard backup vault can have one; recovery points in a logically air-gapped vault do not currently support backup indexes.",
 "What must a backup have before it can be searched?",
 ["a backup (recovery point) must first have a corresponding index", "do not currently support backup indexes"],
 [E(BS, "To be searchable, a backup (recovery point) must first have a corresponding index."),
  E(BS, "Recovery points of supported resource types can have a backup index if they are stored in a standard backup vault (recovery points in a logical air-gapped vault do not currently support backup indexes).")],
 scope="AWS Backup search", tier0=True, bullets=["1.3.K2", "2.2.S5"], **FC))
f.append(F("backup-search-results-kept-7-days-export-to-s3", "limit",
 "AWS Backup retains search results for 7 days from completion, and a best practice is to export the results to an S3 bucket to keep them longer.",
 "How long does AWS Backup keep search results?",
 ["retains search results for 7 days", "export your search results to an S3 bucket"],
 [E(BS, "AWS Backup retains search results for 7 days, starting with the completion time and date."),
  E(BS, "A best practice is to export your search results to an S3 bucket to retain results beyond the 7 day retention.")],
 scope="AWS Backup search results", dm="max", tier0=True, bullets=["1.3.K2"], **FC))
f.append(F("backup-search-charges-index-search-storage-restore", "pricing-dimension",
 "Each backup index creation and each search job incurs a charge, each backup index has a storage charge, and each restore from search results is charged like other restore jobs.",
 "What do you pay for with AWS Backup search?",
 ["Each backup index creation and each search job incurs a charge", "Each backup index has a storage charge"],
 [E(BS, "Each backup index creation and each search job incurs a charge. Each backup index has a storage charge. Each restore from search results (as with all other all restore jobs) is charged.")],
 scope="AWS Backup search", bullets=["4.3.S1"], **FC))
f.append(F("backup-search-index-created-by-plan-opt-in", "capability",
 "You can opt in to have a backup index created with each periodic backup of a supported resource type (continuous backups get daily indexes), and only recovery points that have an index can be included in a backup search.",
 "How do you make future backups searchable?",
 ["created with each periodic backup of a supported resource type", "continuous backups will have daily indexes created"],
 [E(CP, "(Optional) You can opt in to have a backup index created with each periodic backup of a supported resource type (continuous backups will have daily indexes created). Only recovery points (backups) that have an associated index can be included in a backup search.")],
 scope="AWS Backup backup plans", bullets=["1.3.K2"], **FC))
# Tiering
f.append(F("backup-tiering-s3-lower-cost-warm-tier-same-performance", "capability",
 "AWS Backup offers a lower-cost warm storage tier for S3 backups that reduces long-term storage costs by up to 30% and provides the same performance and features as the warm storage tier.",
 "What does AWS Backup tiering offer for S3 backups?",
 ["lower-cost warm storage tier for Amazon S3 backups", "same performance and features as the warm storage tier"],
 [E(BT, "AWS Backup offers a lower-cost warm storage tier for Amazon S3 backups that reduces long-term storage costs by up to 30% while maintaining enterprise-grade protection and recovery capabilities. The low-cost tier provides the same performance and features as the warm storage tier.")],
 scope="S3 backup tiering", cond="savings are an upper bound", tier0=True, bullets=["4.1.S6", "4.3.S1"], **FC))
f.append(F("backup-tiering-three-cost-components-one-time-transition-fee", "pricing-dimension",
 "Backup tiering has three cost components (warm storage tier, low-cost warm storage tier and transition costs), and moving data to the lower-cost tier incurs a one-time per-object transition fee based on the number of objects eligible for tiering.",
 "What do you pay for with S3 backup tiering?",
 ["three cost components", "one-time per-object transition fee"],
 [E(BT, "Backup tiering has three cost components: warm storage tier, low-cost warm storage tier, and transition costs. When backup data transitions to the lower-cost tier, you'll incur a one-time per-object transition fee based on the number of objects eligible for tiering.")],
 scope="S3 backup tiering", bullets=["4.3.S1"], **FC))
f.append(F("backup-tiering-applies-to-existing-and-new-backups", "behavior",
 "Tiering configurations apply to both existing backup data in vaults and new backups created after the configuration is established.",
 "Does an S3 tiering configuration apply to backups that already exist?",
 ["both existing backup data in vaults and new backups", "created after the configuration is established"],
 [E(BT, "Tiering configurations apply to both existing backup data in vaults and new backups created after the configuration is established.")],
 scope="S3 backup tiering", rel="extended", bullets=["4.3.S1"], **FC))
# Notifications, IAM, resilience, monitoring
f.append(F("backup-sns-cross-account-and-fifo-topics-unsupported", "restriction",
 "Although Amazon SNS allows cross-account notifications, AWS Backup does not currently support this, and AWS Backup does not currently support SNS FIFO topics, only Standard topics.",
 "Can AWS Backup send events to an SNS topic in another account or to a FIFO topic?",
 ["AWS Backup does not currently support this feature", "does not currently support SNS FIFO topics"],
 [E(BN, "While the Amazon SNS service allows cross-account notifications, AWS Backup does not currently support this feature. You must specify your own AWS account ID and the resource ARN of your topic."),
  E(BN, "AWS Backup supports Standard topics for SNS best-effort deduplication, but AWS Backup does not currently support SNS FIFO topics for Strict deduplication.")],
 scope="AWS Backup SNS notifications", bullets=["1.3.S1"]))
f.append(F("backup-user-notifications-view-job-progress-and-changes", "capability",
 "With AWS User Notifications you can view the progress of backup, copy and restore jobs and changes to your backup policies, vaults, recovery points and settings from the Notification Center.",
 "How can you follow AWS Backup job progress and changes in notifications?",
 ["view the progress of your backup, copy, and restore jobs", "Notification Center"],
 [E(BN, "With User Notifications, you can view the progress of your backup, copy, and restore jobs and changes to your backup policies, vaults, recovery points, and settings from the User Notifications Notification Center.")],
 scope="AWS Backup notifications", rel="extended", bullets=["1.3.S1"]))
f.append(F("backup-monitoring-cloudwatch-eventbridge-cloudtrail-sns", "capability",
 "AWS Backup integrates with CloudWatch for metrics and alarms, EventBridge for backup events, CloudTrail for a consolidated view of backup activity logs, and SNS for backup activity notifications such as a succeeded backup.",
 "Which services does AWS Backup integrate with for monitoring and auditing?",
 ["CloudWatch allows you to track metrics and create alarms", "consolidated view of backup activity logs"],
 [E(W, "AWS Backup integrates with Amazon CloudWatch and Amazon EventBridge. CloudWatch allows you to track metrics and create alarms. EventBridge allows you to view and monitor AWS Backup events."),
  E(W, "AWS Backup integrates with AWS CloudTrail. CloudTrail gives you a consolidated view of backup activity logs that make it quick and easy to audit how your resources are backed up. AWS Backup also integrates with Amazon Simple Notification Service (Amazon SNS), providing you with backup activity notifications, such as when a backup succeeds or a restore has been initiated.")],
 scope="AWS Backup monitoring", tier0=True, bullets=["1.3.S1"]))
f.append(F("backup-dashboard-audits-backup-and-restore-activity", "capability",
 "AWS Backup provides a dashboard that makes it simple to audit backup and restore activity across AWS services.",
 "Is there a single view of backup and restore activity?",
 ["dashboard that makes it simple to audit backup and restore activity", "across AWS services"],
 [E(W, "AWS Backup provides a dashboard that makes it simple to audit backup and restore activity across AWS services.")],
 scope="AWS Backup console", hard=False, bullets=["1.3.S1"]))
f.append(F("backup-iam-service-role-must-trust-aws-backup", "behavior",
 "The role you pass to AWS Backup must have an IAM policy with the permissions for backup operations such as creating, restoring or expiring backups, with different permissions for each supported service, and AWS Backup must be a trusted entity so it can assume the role.",
 "What must the IAM role you pass to AWS Backup allow and trust?",
 ["must also have AWS Backup listed as a trusted entity", "Different permissions are required for each of the AWS services"],
 [E(IR, "The role that you pass to AWS Backup must have an IAM policy with the permissions that enable AWS Backup to perform actions associated with backup operations, such as creating, restoring, or expiring backups. Different permissions are required for each of the AWS services that AWS Backup supports. The role must also have AWS Backup listed as a trusted entity, which enables AWS Backup to assume the role.")],
 scope="AWS Backup service role", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-iam-role-passed-for-plans-on-demand-copy-restore", "behavior",
 "You must pass a service role when you assign resources to a backup plan or run an on-demand backup, copy or restore, and AWS Backup uses that role to create, tag and delete resources in your account.",
 "When must you pass a service role to AWS Backup?",
 ["you must pass a service role", "create, tag, and delete resources in your account"],
 [E(IR, "When you assign resources to a backup plan, or if you perform an on-demand backup, copy, or restore, you must pass a service role that has access to perform the underlying operations on the specified resources. AWS Backup uses this role to create, tag, and delete resources in your account.")],
 scope="AWS Backup service role", bullets=["1.3.S1"]))
f.append(F("backup-iam-default-service-role-console-auto-cli-manual", "default",
 "The default service role, named AWSBackupDefaultServiceRole, is created automatically when you use the AWS Management Console but must be created manually when you use the AWS CLI, and it contains the managed policies AWSBackupServiceRolePolicyForBackup and AWSBackupServiceRolePolicyForRestores.",
 "How does the default AWS Backup service role get created?",
 ["automatically created when you use the AWS Management Console", "AWSBackupDefaultServiceRole"],
 [E(IR, "The default role is automatically created when you use the AWS Management Console. You can create the default role using the AWS Command Line Interface (AWS CLI), but it must be done manually."),
  E(IR, "The default service role is named `AWSBackupDefaultServiceRole`. This service role contains two managed policies, AWSBackupServiceRolePolicyForBackup and AWSBackupServiceRolePolicyForRestores.")],
 scope="AWS Backup default service role", dm="default", rel="extended", bullets=["1.3.S1"]))
f.append(F("backup-iam-narrow-roles-and-who-can-pass-them", "capability",
 "You can control access to backups with narrowly scoped roles and by specifying who can pass the role to AWS Backup, for example a role that only backs up RDS databases that only RDS database owners can pass.",
 "How can roles limit who can back up which resource types?",
 ["defining narrowly scoped roles", "specifying who can pass that role to AWS Backup"],
 [E(IR, "You can use roles to control access to your backups by defining narrowly scoped roles and by specifying who can pass that role to AWS Backup. For example, you could create a role that only grants permissions to back up Amazon Relational Database Service (Amazon RDS) databases and only grant Amazon RDS database owners permission to pass that role to AWS Backup.")],
 scope="AWS Backup service roles", bullets=["1.3.S1", "2.2.S5"]))
f.append(F("backup-resilience-stored-across-azs-eleven-nines", "behavior",
 "AWS Backup is designed to store your backups redundantly across multiple Availability Zones for durability of 99.999999999% (11 nines) in any given year, provided that you adhere to the current AWS Backup documentation.",
 "What durability and AZ spread does AWS Backup design for?",
 ["99.999999999% (11 nines)", "across multiple Availability Zones"],
 [E(DR, "AWS Backup is designed to use the AWS global infrastructure to resiliently and redundantly store your backups across multiple Availability Zones for durability of 99.999999999% (11 nines) in any given year, provided that you adhere to the current AWS Backup documentation.")],
 scope="AWS Backup recovery points", cond="provided that you adhere to the current AWS Backup documentation", dm="", tier0=True, bullets=["2.2.S5", "2.2.K4"]))
f.append(F("backup-resilience-at-least-as-durable-as-source-service", "behavior",
 "AWS Backup stores your backups with at least as much resilience and durability as the resource's original AWS service would give you if you backed it up there.",
 "How durable are backups in AWS Backup compared with the source service's own backups?",
 ["at least as much resilience and durability", "original AWS service would give you"],
 [E(DR, "AWS Backup stores your backups with at least as much resilience and durability as your resource’s original AWS service would give you, if you backed it up there.")],
 scope="AWS Backup recovery points", bullets=["2.2.S5", "2.2.K4"]))
f.append(F("backup-resilience-copy-across-regions-greater-resilience", "capability",
 "AWS Backup lets you copy your backups across Regions for even greater resilience.",
 "How do you get Region-level resilience for backups in AWS Backup?",
 ["copy your backups across Regions", "even greater resilience"],
 [E(DR, "Furthermore, AWS Backup empowers you to copy your backups across Regions for even greater resilience.")],
 scope="AWS Backup cross-Region copy", bullets=["2.2.S5", "2.2.K4"]))
f.append(F("backup-vault-backups-immutable-content-and-survive-source-deletion", "behavior",
 "The content of each AWS Backup backup is immutable, and backup vaults keep backups separate from their source instances, so a vault keeps EC2 and EBS backups per the lifecycle policy even if you delete the source instance and volumes.",
 "Do backups survive deletion of the source EC2 instance or EBS volume?",
 ["no one can alter that content", "even if you delete the source Amazon EC2 instance and Amazon EBS volumes"],
 [E(W, "The content of each AWS Backup backup is immutable, meaning that no one can alter that content. AWS Backup further secures your backups in backup vaults, which separates them safely from their source instances. For example, your vault will retain your Amazon EC2 and Amazon EBS backups according to the lifecycle policy you choose, even if you delete the source Amazon EC2 instance and Amazon EBS volumes.")],
 scope="AWS Backup recovery points and vaults", tier0=True, bullets=["2.2.S5", "1.3.S1"]))
f.append(F("backup-vault-lock-prevents-anyone-including-you-deleting", "behavior",
 "You can use AWS Backup Vault Lock to prevent anyone, including you, from deleting backups or altering their retention period, enforcing a write-once-read-many (WORM) model.",
 "How do you stop even yourself from deleting backups or shortening retention?",
 ["prevent anyone (including you) from deleting backups", "write-once-read-many"],
 [E(W, "You can use AWS Backup Vault Lock to prevent anyone (including you) from deleting backups or altering their retention period. AWS Backup Vault Lock helps you enforce a write-once-read-many (WORM) model and add another layer of defense to your defense in depth.")],
 scope="AWS Backup Vault Lock", tier0=True, bullets=["1.3.S1", "2.2.S5"]))
dump("facts-behavior-18.json", f[:20])
dump("facts-behavior-19.json", f[20:])
