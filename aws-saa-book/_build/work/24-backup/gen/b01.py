import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
W, A, P, H = D + "whatisbackup", D + "about-backup-plans", D + "plan-options-and-configuration", D + "how-it-works"
S = D + "assigning-resources"
f = []
f.append(F("backup-what-is-fully-managed-centralize", "behavior",
 "AWS Backup is a fully managed service that centralizes and automates data protection across AWS services, in the cloud and on premises.",
 "What is AWS Backup and what does it cover?",
 ["fully-managed service", "centralize and automate data protection", "in the cloud, and on premises"],
 [E(W, "AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud, and on premises.")],
 scope="AWS Backup", hard=False, tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-does-not-govern-backups-outside-aws-backup", "restriction",
 "AWS Backup does not govern backups that you take in your AWS environment outside of AWS Backup.",
 "Does AWS Backup manage or govern backups that were made outside AWS Backup, for example by a service's own backup feature?",
 ["does not govern backups", "outside of AWS Backup"],
 [E(W, "AWS Backup does not govern backups you take in your AWS environment outside of AWS Backup.")],
 scope="backups made outside AWS Backup", tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-plan-is-policy-expression", "behavior",
 "A backup plan is a policy expression that defines when and how you back up your AWS resources, such as DynamoDB tables or EFS file systems.",
 "What is a backup plan in AWS Backup?",
 ["a policy expression", "when and how you want to back up"],
 [E(A, "In AWS Backup, a backup plan is a policy expression that defines when and how you want to back up your AWS resources, such as Amazon DynamoDB tables or Amazon Elastic File System (Amazon EFS) file systems.")],
 scope="backup plan", hard=False, tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-plan-multiple-plans-per-requirement", "capability",
 "You can create multiple backup plans when workloads have different backup requirements.",
 "Can you have more than one backup plan for workloads with different backup requirements?",
 ["create multiple backup plans", "different backup requirements"],
 [E(A, "You can create multiple backup plans if you have workloads with different backup requirements.")],
 scope="AWS Backup backup plans", bullets=["4.3.S1"]))
f.append(F("backup-plan-applied-by-tagging-resources", "capability",
 "AWS Backup lets you apply a backup plan to your AWS resources by tagging them; it then backs up the resources automatically according to the plan.",
 "How do you apply a backup plan to resources in AWS Backup?",
 ["apply backup plans to your AWS resources", "by simply tagging them"],
 [E(H, "AWS Backup lets you apply backup plans to your AWS resources by simply tagging them. AWS Backup then automatically backs up your AWS resources according to the backup plan that you defined.")],
 scope="AWS Backup backup plans", tier0=True, bullets=["4.3.S1"]))
f.append(F("backup-tag-integration-group-resources", "capability",
 "Integration with AWS tags lets you quickly apply a backup plan to a group of resources so that they are backed up consistently and in a compliant manner.",
 "What does tag integration give you in AWS Backup?",
 ["quickly apply a backup plan to a group", "consistent and compliant manner"],
 [E(W, "Integration with AWS tags enables you to quickly apply a backup plan to a group of AWS resources, so that they are backed up in a consistent and compliant manner.")],
 scope="AWS Backup tag-based assignment", hard=False, bullets=["4.3.S1"]))
f.append(F("backup-service-opt-in-before-plan-assignment", "behavior",
 "Before you include a service in a backup plan, you opt in to using AWS Backup for that service, in the console or with the AWS CLI.",
 "What must you do for a service before you can include its resources in a backup plan?",
 ["opt in to using AWS Backup", "console or AWS CLI"],
 [E(S, "Before you decide which services to include in backup plan, use the AWS Backup console or AWS CLI to opt in to using AWS Backup to work with those services.")],
 scope="service opt-in, AWS Backup", cond="applies before assigning resources of that service", bullets=["4.3.S1"]))
f.append(F("backup-service-opt-in-checked-per-region", "behavior",
 "The describe-region-settings command shows which services you have opted into in a specific Region, so the service opt-in is a Region setting.",
 "Is the AWS Backup service opt-in a per-Region setting?",
 ["opted into in a specific Region", "describe-region-settings"],
 [E(S, "Use the aws backup describe-region-settings command to determine which services you have opted into in a specific Region.")],
 scope="per Region", bullets=["4.3.S1"]))
f.append(F("backup-opt-in-still-applies-with-tag-assignment", "behavior",
 "If you assign resources only by tags, the service opt-in settings still apply.",
 "If a backup plan assigns resources only by tags, does the service opt-in still matter?",
 ["only use tags for resource assignment", "service opt-in settings will still apply"],
 [E(S, "If you only use tags for resource assignment, then the service opt-in settings will still apply.")],
 scope="resource assignment by tags", bullets=["4.3.S1"]))
f.append(F("backup-overlapping-rules-longer-retention-wins", "behavior",
 "When the start windows of different rules in a backup plan overlap, AWS Backup retains the backup under the rule with the longer retention period.",
 "If two rules in one backup plan overlap, which rule's backup does AWS Backup keep?",
 ["rule with the longer retention period", "start windows of different rules overlap"],
 [E(P, "When the start windows of different rules overlap, AWS Backup retains the backup under the rule with the longer retention period."),
  E(P, "If you have a backup plan with multiple rules and the time frames of the two rules overlap, AWS Backup optimizes the backup and takes a backup for the rule with the longer retention time.")],
 scope="rules of one backup plan", tier0=True, bullets=["4.3.S1"]))
f.append(F("backup-incremental-first-full-then-changes", "behavior",
 "For supported resource types, AWS Backup stores periodic backups incrementally: the first backup is a full copy and each later backup stores only the changes.",
 "How does AWS Backup store periodic backups for resource types that support incremental backups?",
 ["backs up a full copy of your data", "only the changes to your AWS resources"],
 [E(A, "AWS Backup efficiently stores your periodic backups incrementally for supported resource types. The first backup of an AWS resource backs up a full copy of your data. For each successive incremental backup, only the changes to your AWS resources are backed up.")],
 scope="resource types that support incremental backups", cond="supported resource types only", tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-incremental-not-all-types-full-copy", "restriction",
 "Not all resource types support incremental backups; for those that do not, each backup is a full copy, which can cost more in storage.",
 "What happens for resource types that do not support incremental backups?",
 ["each backup is a full copy", "higher storage costs"],
 [E(A, "Not all resource types support incremental backups. For resources that do not support incremental backups, each backup is a full copy, which can result in higher storage costs.")],
 scope="resource types without incremental backup support", bullets=["4.1.K5"]))
f.append(F("backup-lifecycle-restore-until-end", "behavior",
 "The backup lifecycle is the number of days a backup is stored, and a backup can be restored until the end of its lifecycle.",
 "Until when can an AWS Backup backup be restored?",
 ["until the end of their lifecycle", "number of days you specify"],
 [E(P, "Backups are stored for the number of days you specify, known as the backup lifecycle. Backups can be restored until the end of their lifecycle.")],
 scope="AWS Backup lifecycle", bullets=["4.1.S6"]))
f.append(F("backup-every-backup-starts-in-warm-storage", "behavior",
 "Every backup is created and stored in warm storage first; you can transition it to the lower-cost cold storage tier.",
 "Which storage tier does a new backup start in, and what is the cheaper tier?",
 ["stored in warm storage", "lower-cost tier called cold storage"],
 [E(P, "Every backup is created and is stored in warm storage. Depending on how long you choose to store your backup, you may wish to transition your backup to a lower-cost tier called cold storage.")],
 scope="AWS Backup storage tiers", bullets=["4.1.S6"]))
f.append(F("backup-cold-ebs-is-snapshot-archive-monthly-or-less", "behavior",
 "Cold storage for EBS backups is EBS Snapshots Archive, and with cold storage enabled a backup plan can transition EBS snapshots only when the backup frequency is monthly or less often.",
 "How does AWS Backup cold storage work for EBS, and for which backup frequency can EBS snapshots transition?",
 ["Amazon EBS Snapshots Archive", "monthly or less often"],
 [E(D + "creating-a-backup-plan", "Cold storage for Amazon EBS is Amazon EBS Snapshots Archive. Snapshots transitioned to archive storage tier will display in the console as cold tier. If cold storage is enabled, and if your backup frequency is monthly or less often, you can have your backup plan transition EBS snapshots.")],
 scope="EBS snapshots in AWS Backup", cond="cold storage enabled and backup frequency monthly or less often", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-cold-transition-setting-locked-after-transition", "restriction",
 "You cannot change the transition-to-cold-after-days setting after a backup has been transitioned to cold storage.",
 "Can you change the transition-to-cold setting after a backup has moved to cold storage?",
 ["can't change the", "after a backup has been transitioned to cold"],
 [E(P, "You can't change the “transition to cold after days” setting after a backup has been transitioned to cold.")],
 scope="a backup already in cold storage", bullets=["4.1.S6"]))
f.append(F("backup-cold-incremental-needs-warm-full-backup", "behavior",
 "For resource types that support incremental backups, you must have at least one warm full backup; if the full backup moves to cold storage too soon, AWS Backup creates another warm full backup.",
 "What happens if the full backup of an incremental resource type moves to cold storage too soon?",
 ["at least one warm full backup", "another warm full backup"],
 [E(P, "Some services support incremental backups. For incremental backups, you must have at least one warm full backup. AWS Backup recommends that you set your lifecycle settings to not move your backup to cold storage until after at least 8 days. If the full backup is transitioned to cold storage too soon (for example, a transition to cold storage after 1 day), AWS Backup will create another warm full backup.")],
 scope="resource types that support incremental backups", bullets=["4.1.S6"]))
f.append(F("backup-cold-incremental-billing-by-reference", "behavior",
 "For incremental resource types, data moves from warm to cold storage when no warm backup still references it, and data referenced only by cold backups is billed at cold storage tier prices; other backups stay at warm storage prices.",
 "How is incremental backup data billed when part of it is in cold storage?",
 ["no longer referenced by warm backups", "billed at cold storage tier prices"],
 [E(P, "For resource types that support incremental backups, AWS Backup transitions data from warm to cold storage if the transitioned data is no longer referenced by warm backups. Data in backups retained in cold storage that is only referenced by other cold backups is billed at cold storage tier prices. Other backups continue at warm storage tier pricing.")],
 scope="resource types that support incremental backups", bullets=["4.1.S6"]))
f.append(F("backup-copy-lifecycle-follows-source-when-unset", "default",
 "If no expiry (DeleteAfterDays) is set in the copy settings, the copy follows the lifecycle settings of the backup it was copied from.",
 "What lifecycle does a backup copy get when the copy settings do not set an expiry?",
 ["follow the lifecycle settings of the backup", "is not specified in the copy settings"],
 [E(P, "If the value for Lifecycle:DeleteAfterDays (shown as Expire in the console) is not specified in the copy settings, the copy will follow the lifecycle settings of the backup from which it is copied.")],
 scope="backup copy lifecycle", dm="default", bullets=["4.1.S6"]))
f.append(F("backup-copy-action-same-or-other-region-and-account", "capability",
 "A backup plan can optionally create a backup copy in the same or another AWS Region, and the copy can go to the same account or another account.",
 "Where can a backup plan copy action place a backup copy?",
 ["in the same or another AWS Region", "in the same account or another account"],
 [E(P, "As part of your backup plan, you can optionally create a backup copy in the same or another AWS Region. These copies can be made either in the same account or another account.")],
 scope="copy action in a backup plan", bullets=["1.3.S5"]))
f.append(F("backup-copy-iam-role-trusted-entity-default-created", "behavior",
 "The IAM role that creates a backup copy must list AWS Backup as a trusted entity; if you choose Default and the default role does not exist, AWS Backup creates one with the correct permissions.",
 "What must the IAM role used for a backup copy trust, and what happens if the default role is missing?",
 ["AWS Backup listed as a trusted entity", "a role is created for you"],
 [E(P, "The IAM role that AWS Backup uses when creating the copy. The role must also have AWS Backup listed as a trusted entity, which enables AWS Backup to assume the role. If you choose Default and the AWS Backup default role is not present in your account, a role is created for you with the correct permissions.")],
 scope="backup copy IAM role", bullets=["1.3.S1"]))
f.append(F("backup-continuous-cannot-be-scheduled", "restriction",
 "Continuous backups and point-in-time restore cannot be scheduled with a time or cron expression, because they record changes over a period of time.",
 "Can a continuous (PITR) backup rule be scheduled with a cron expression?",
 ["cannot be scheduled with a time or cron expression", "changes recorded over a period of time"],
 [E(P, "Continuous backups and point-in-time restore (PITR) reference the changes recorded over a period of time; therefore, they cannot be scheduled with a time or cron expression.")],
 scope="continuous backups", bullets=["1.3.S5"]))
f.append(F("backup-continuous-rule-allows-pitr-unlike-snapshot", "capability",
 "A continuous backup rule is created with the enable continuous backups checkbox, and unlike snapshot backups it allows point-in-time restore.",
 "What do continuous backups allow that snapshot backups do not?",
 ["continuous backups allow you to perform point-in-time restore", "Unlike snapshot backups"],
 [E(P, "You can also check the Enable continuous backups for supported resources checkbox to create a point-in-time restore (PITR)-enabled continuous backup rule. Unlike snapshot backups, continuous backups allow you to perform point-in-time restore.")],
 scope="continuous backup rules, supported resources", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-vault-sets-kms-key-and-access", "capability",
 "You use a backup vault to set the KMS key that encrypts the backups in it and to control access to those backups.",
 "What can you set on a backup vault?",
 ["encryption key that is used to encrypt backups", "control access to the backups"],
 [E(P, "You can use backup vaults to set the AWS Key Management Service (AWS KMS) encryption key that is used to encrypt backups in the backup vault and to control access to the backups in the backup vault.")],
 scope="backup vault", bullets=["2.2.S5"]))
f.append(F("backup-plan-window-optimized-by-default", "default",
 "By default AWS Backup optimizes the backup windows of a plan; you can customize the window in the console or programmatically.",
 "Who sets the backup window by default in an AWS Backup plan?",
 ["backup windows are optimized by AWS Backup", "customize the backup window"],
 [E(A, "By default, backup windows are optimized by AWS Backup. You can customize the backup window in the console or programmatically.")],
 scope="backup plan windows", dm="default", adj=True, bullets=["4.1.S6"]))
dump("facts-behavior-01.json", f)
