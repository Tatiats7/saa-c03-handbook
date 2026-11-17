import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
MC, PI, PC, CB, RC, DB = D + "manage-cross-account", D + "point-in-time-recovery", D + "point-in-time-recovery-copying", D + "creating-a-backup", D + "recov-point-create-a-copy", D + "deleting-backups"
OD = D + "recov-point-create-on-demand-backup"
f = []
f.append(F("backup-org-policy-merge-only-same-plan-name", "behavior",
 "Backup policies are merged only when they share the same backup plan name; otherwise policies can coexist in an account without merging.",
 "When are Organizations backup policies merged into one effective plan?",
 ["only for backup policies that share the same backup plan name", "coexist in that account without any merging"],
 [E(MC, "Merging is done only for backup policies that share the same backup plan name. You can also have policy A and policy B coexist in that account without any merging.")],
 scope="Organizations backup policy inheritance", bullets=["1.3.S1", "4.3.S1"]))
f.append(F("backup-pitr-continuous-works-by-full-backup-and-transaction-logs", "behavior",
 "Continuous backup first creates a full backup of the resource and then constantly backs up its transaction logs; point-in-time recovery replays the transaction log on the full backup to the time you choose.",
 "How do continuous backups and point-in-time recovery work in AWS Backup?",
 ["constantly backing up your resource's transaction logs", "replaying the transaction log to the time"],
 [E(PI, "Continuous backup works by first creating a full backup of your resource, and then constantly backing up your resource’s transaction logs. PITR works by accessing your full backup and replaying the transaction log to the time that you tell AWS Backup to recover.")],
 scope="continuous backups", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-pitr-restore-rewinds-to-chosen-time", "capability",
 "With continuous backups you can restore a supported resource by rewinding it to a specific time you choose, to within 1 second of precision, going back a maximum of 35 days.",
 "How precise is a point-in-time restore from continuous backups and how far back can it go?",
 ["within 1 second of precision", "a maximum of 35 days"],
 [E(PI, "With continuous backups, you can restore your AWS Backup-supported resource by rewinding it back to a specific time that you choose, within 1 second of precision (going back a maximum of 35 days).")],
 scope="continuous backups, supported resources", dm="max", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-pitr-recommend-continuous-and-snapshot-rules-together", "behavior",
 "Because continuous and snapshot backups offer different advantages, AWS recommends protecting resources with both continuous and snapshot backup rules.",
 "Should a resource have a continuous backup rule, a snapshot rule, or both?",
 ["both continuous and snapshot backup rules", "different advantages"],
 [E(PI, "Because continuous and snapshot backups offer different advantages, we recommend that you protect your resources with both continuous and snapshot backup rules.")],
 scope="resources that support continuous backups", tier0=True, bullets=["1.3.S5", "4.3.S1"]))
f.append(F("backup-on-demand-backup-starts-immediately", "behavior",
 "An on-demand backup begins to back up your resource immediately, and you can use it to create a backup at a time other than the schedule of a backup plan.",
 "When does an on-demand backup start and what is it for?",
 ["begins to back up your resource immediately", "other than the scheduled time defined in a backup plan"],
 [E(PI, "An on-demand backup begins to back up your resource immediately. You can choose an on-demand backup if you wish to create a backup at a time other than the scheduled time defined in a backup plan. An on-demand backup can be used, for example, to test backup and functionality at any time.")],
 scope="on-demand backups", bullets=["4.1.S6"]))
f.append(F("backup-on-demand-not-usable-with-pitr", "restriction",
 "You cannot use on-demand backups with point-in-time recovery, because an on-demand backup preserves the resource's state at one moment while PITR uses continuous backups that record changes over a period of time.",
 "Can an on-demand backup be a continuous (PITR) backup?",
 ["can't use on-demand backups with PITR", "record changes over a period of time"],
 [E(PI, "You can't use on-demand backups with PITR, because an on-demand backup preserves resources in the state they are in when the backup is taken, while PITR uses continuous backups, which record changes over a period of time.")],
 scope="on-demand backups and PITR", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-continuous-plan-one-recovery-point-updated", "behavior",
 "A continuous backup plan creates one continuous recovery point and updates that recovery point whenever the job runs.",
 "How many recovery points does a continuous backup plan create?",
 ["creates one continuous recovery point", "updates that recovery point whenever the job runs"],
 [E(PI, "You can opt in to continuous backups for supported resources when you create a backup plan in AWS Backup using the AWS Backup console or the API. The continuous backup plan creates one continuous recovery point and updates that recovery point whenever the job runs.")],
 scope="continuous backup plans", bullets=["1.3.S5"]))
f.append(F("backup-continuous-one-per-resource-redundant-extra", "restriction",
 "Each resource can have only one continuous backup (recovery point); additional continuous backups are redundant.",
 "How many continuous backups can one resource have?",
 ["can only have one continuous backup", "additional continuous backups are redundant"],
 [E(PI, "Each resource (such as an Amazon S3 bucket or an Amazon RDS database) can only have one continuous backup (recovery point); additional continuous backups are redundant.")],
 scope="per resource", dm="max", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-continuous-multiple-rules-single-vault-longest-retention", "behavior",
 "If several rules specify more than one continuous backup in a single vault, AWS Backup follows the rule with the longest retention period and ignores the additional rules.",
 "Which rule wins when several rules ask for a continuous backup of one resource in one vault?",
 ["follows the rule with the longest retention period", "ignores additional rules"],
 [E(PI, "If multiple rules specify that more than one continuous backup should be in a single vault, AWS Backup follows the rule with the longest retention period (lifecycle) and ignores additional rules.")],
 scope="continuous backup rules, single vault", rel="extended", bullets=["1.3.S5", "4.3.S1"]))
f.append(F("backup-continuous-multiple-rules-multiple-vaults-extra-become-snapshots", "behavior",
 "If rules specify continuous backups of one resource in more than one vault, AWS Backup creates one continuous backup under the first rule processed, and each later continuous rule for that resource results in a snapshot (periodic) backup instead.",
 "What happens when continuous backup rules for one resource point at different vaults?",
 ["creates one continuous backup according to the first rule processed", "will result in a snapshot (periodic) backup instead"],
 [E(PI, "If multiple rules specify that more than one continuous backup should be in more than one vault, AWS Backup creates one continuous backup according to the first rule processed. Each subsequent rule specifying a continuous backup for a resource that already has a continuous backup will result in a snapshot (periodic) backup instead.")],
 scope="continuous backup rules, multiple vaults", rel="extended", bullets=["1.3.S5"]))
f.append(F("backup-continuous-s3-depends-on-eventbridge-events", "restriction",
 "AWS Backup for S3 relies on S3 events delivered through Amazon EventBridge; if that setting is disabled in the S3 bucket notification settings, continuous backups stop for those buckets.",
 "What stops S3 continuous backups if it is turned off?",
 ["relies on receiving S3 events through Amazon EventBridge", "continuous backups will stop"],
 [E(PI, "AWS Backup for S3 relies on receiving S3 events through Amazon EventBridge. If this setting is disabled in S3 bucket notification settings, continuous backups will stop for those buckets with the setting turned off.")],
 scope="S3 continuous backups", tier0=True, bullets=["1.3.S5", "4.1.S6"]))
f.append(F("backup-continuous-rds-supported-not-multi-az-clusters", "restriction",
 "AWS Backup supports continuous backups and point-in-time recovery for all RDS instances and Aurora that the native RDS service supports, but not for Amazon RDS Multi-AZ clusters.",
 "Does AWS Backup support continuous backups for RDS Multi-AZ clusters?",
 ["does not support continuous backups or point-in-time recovery for Amazon RDS Multi-AZ clusters", "all Amazon RDS instances and Aurora"],
 [E(PI, "AWS Backup supports continuous backups and point-in-time recovery for all Amazon RDS instances and Aurora that are supported by the native Amazon RDS service. AWS Backup does not support continuous backups or point-in-time recovery for Amazon RDS Multi-AZ clusters.")],
 scope="RDS and Aurora continuous backups", tier0=True, bullets=["1.3.S5", "4.1.S6"]))
f.append(F("backup-continuous-rds-backup-window-managed-while-aws-backup-manages", "behavior",
 "While AWS Backup manages continuous backups for an RDS instance you cannot configure the automated backup window directly; AWS Backup places it near the RDS maintenance window, and you can influence the placement by adjusting the RDS maintenance window.",
 "Can you set the RDS automated backup window while AWS Backup manages continuous backups?",
 ["cannot directly configure the automated backup window", "positions this automated backup window near the Amazon RDS maintenance window"],
 [E(PI, "AWS Backup positions this automated backup window near the Amazon RDS maintenance window to prevent conflicts. You cannot directly configure the automated backup window while AWS Backup manages continuous backups, but you can influence its placement by adjusting your Amazon RDS maintenance window.")],
 scope="RDS instances with AWS Backup continuous backups", bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-continuous-rds-settings-managed-only-in-aws-backup", "restriction",
 "After you apply an AWS Backup continuous backup rule to an RDS instance, you cannot create or modify continuous backup settings in Amazon RDS; you make changes through the AWS Backup console or CLI.",
 "Where can you change continuous backup settings of an RDS instance covered by an AWS Backup continuous rule?",
 ["can't create or modify continuous backup settings in Amazon RDS", "through the AWS Backup console or the AWS Backup CLI"],
 [E(PI, "After you apply an AWS Backup continuous backup rule to an Amazon RDS instance, you can't create or modify continuous backup settings in Amazon RDS. You must make modifications through the AWS Backup console or the AWS Backup CLI.")],
 scope="RDS instances with AWS Backup continuous backups", bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-continuous-rds-cannot-copy-continuous-backups", "restriction",
 "You cannot create copies of RDS continuous backups because AWS Backup for RDS does not allow copying transaction logs; instead AWS Backup creates a snapshot and copies it with the frequency set in the backup plan.",
 "Can an RDS continuous backup be copied to another Region?",
 ["can't create copies of Amazon RDS continuous backups", "does not allow copying transaction logs"],
 [E(PI, "You can't create copies of Amazon RDS continuous backups because AWS Backup for Amazon RDS does not allow copying transaction logs. Instead, AWS Backup creates a snapshot and copies it with the frequency specified in the backup plan.")],
 scope="RDS continuous backups", bullets=["1.3.S5"]))
f.append(F("backup-continuous-rds-pitr-via-aws-backup-or-rds", "capability",
 "You can perform a point-in-time restore of an RDS instance using either AWS Backup or Amazon RDS.",
 "Can you do the point-in-time restore of an RDS instance in the RDS service when AWS Backup manages the continuous backup?",
 ["using either AWS Backup or Amazon RDS", "point-in-time restore"],
 [E(PI, "You can perform a point-in-time restore using either AWS Backup or Amazon RDS.")],
 scope="RDS point-in-time restore", bullets=["1.3.S5", "4.1.K5"]))
f.append(F("backup-continuous-aurora-not-in-lag-vault-but-vault-lock-ok", "restriction",
 "Aurora continuous backups are supported in vaults protected by Vault Lock, with the vault's retention settings enforced, but they do not support the logically air-gapped vault feature; to use a logically air-gapped vault with Aurora, use periodic snapshot backups.",
 "Can an Aurora continuous backup be stored in a logically air-gapped vault?",
 ["do not support the logically air-gapped vault feature", "use periodic snapshot backups instead"],
 [E(PI, "Aurora continuous backups are supported in vaults protected by AWS Backup Vault Lock, and the vault's minimum and maximum retention settings are enforced on the recovery point. However, Aurora continuous backups do not support the logically air-gapped vault feature. To use a logically air-gapped vault with Aurora, use periodic snapshot backups instead.")],
 scope="Aurora continuous backups", tier0=True, bullets=["1.3.S5", "2.2.S5"]))
f.append(F("backup-continuous-aurora-rpo-under-five-minutes", "behavior",
 "The recovery point objective (RPO) for Aurora continuous backups is typically less than 5 minutes, because Aurora copies data to Amazon S3 continuously in the background.",
 "What RPO do Aurora continuous backups give?",
 ["typically less than 5 minutes", "copies data to Amazon S3 continuously"],
 [E(PI, "The recovery point objective (RPO) for Aurora continuous backups is typically less than 5 minutes, as Aurora copies data to Amazon S3 continuously in the background.")],
 scope="Aurora continuous backups", cond="typical value", tier0=True, bullets=["1.3.S5", "2.2.K4"]))
f.append(F("backup-continuous-copy-rule-takes-snapshot-then-copies", "behavior",
 "If a continuous backup rule also specifies a cross-account or cross-Region copy, AWS Backup takes a snapshot of the resource and copies the snapshot to the destination vault, and AWS Backup does not support on-demand copies of continuous backups.",
 "How is a continuous backup copied to another Region or account?",
 ["takes a snapshot of the resource and copies the snapshot", "does not support on-demand copies of continuous backups"],
 [E(D + "point-in-time-recovery-copying", "If a continuous backup rule also specifies a cross-account or cross-Region copy and AWS Backup supports the operation for the resource type, AWS Backup takes a snapshot of the resource and copies the snapshot to the destination vault."),
  E(D + "point-in-time-recovery-copying", "AWS Backup does not support on-demand copies of continuous backups.")],
 scope="continuous backup copies", bullets=["1.3.S5"]))
f.append(F("backup-incremental-restore-full-even-after-first-backup-expired", "behavior",
 "Every backup after the first full one is incremental, but all AWS Backup backups keep the reference data needed for a full restore, even after the original full backup has reached the end of its lifecycle and been deleted.",
 "Can you still do a full restore from an incremental backup after the first full backup was deleted?",
 ["retain the necessary reference data to allow a full restore", "even if the original (full) backup has reached the end of its lifecycle"],
 [E(CB, "Although each backup after the first (full) one is incremental (meaning it only captures changes from the previous backup), all backups made with AWS Backup retain the necessary reference data to allow a full restore. This is true even if the original (full) backup has reached the end of its lifecycle and been deleted.")],
 scope="incremental backups", tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-incremental-requires-earlier-backup-in-vault-or-region", "restriction",
 "A backup of a fully managed resource can be incremental only if its vault also contains an earlier backup; other resource types can have incremental backups as long as there is a previous backup of the resource in the same Region.",
 "When can a backup of a fully managed resource be incremental?",
 ["only be incremental if the vault in which the backup is created also contains an earlier backup", "within the same Region"],
 [E(CB, "Backups of resources which are fully managed by AWS Backup can only be incremental if the vault in which the backup is created also contains an earlier backup (incremental or full); other resource types (not fully managed by AWS Backup) can have incremental backups as long as there is a previous backup of the resource within the same Region.")],
 scope="incremental backups, vaults and Regions", rel="extended", bullets=["4.1.K5"]))
f.append(F("backup-incremental-aurora-only-through-continuous-backups", "restriction",
 "Some resources, such as Aurora, offer incremental backup only through continuous backups and point-in-time restore, not through snapshot-based backups.",
 "Does Aurora get incremental backups from AWS Backup snapshot rules?",
 ["only through continuous backups and point-in-time restore (PITR)", "not through snapshot-based backups"],
 [E(CB, "Some resources, such as Amazon Aurora, offer incremental backup only through continuous backups and point-in-time restore (PITR), not through snapshot-based backups.")],
 scope="Aurora backups", bullets=["4.1.K5", "1.3.S5"]))
f.append(F("backup-source-ec2-must-be-running-or-stopped", "restriction",
 "To back up an EC2 instance, the instance can be running or stopped but not terminated, because only a running or stopped instance can communicate with AWS Backup.",
 "Can AWS Backup back up a stopped EC2 instance?",
 ["can be in the running or stopped state", "but not the terminated state"],
 [E(CB, "To back up an Amazon EC2 instance, the instance can be in the `running` or `stopped` state, but not the `terminated` state. This is because a `running` or `stopped` instance can communicate with AWS Backup, but a `terminated` instance cannot.")],
 scope="EC2 instances", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-existing-backups-retained-regardless-of-source-health", "behavior",
 "AWS Backup retains previously created backups consistent with your lifecycle policy, regardless of the health of the source resource.",
 "Are backups kept if the source resource becomes unhealthy or is deleted?",
 ["regardless of the health of your source resource", "consistent with your lifecycle policy"],
 [E(CB, "AWS Backup retains previously-created backups consistent with your lifecycle policy, regardless of the health of your source resource.")],
 scope="AWS Backup recovery points", tier0=True, bullets=["2.2.S5", "4.1.S6"]))
f.append(F("backup-copies-keep-source-creation-date-and-retention", "behavior",
 "Copies keep their source configuration, including the creation date (the time the source was created, not the copy) and the retention period, though you can override the retention period.",
 "Which creation date and retention does a backup copy keep?",
 ["Copies retain their source configuration", "You can override the retention period"],
 [E(RC, "Copies retain their source configuration, including creation dates and retention period. The creation date refers to when the source was created, not when the copy was created. You can override the retention period.")],
 scope="backup copies", bullets=["1.3.S5", "4.1.S6"]))
f.append(F("backup-copy-cold-storage-backups-cannot-be-copied", "restriction",
 "Backups in cold storage or archive tiers cannot be copied across accounts or Regions.",
 "Can a backup that is in cold storage be copied to another Region or account?",
 ["backups in cold storage or archive tiers cannot be copied", "most resource types"],
 [E(RC, "You can copy backups to multiple AWS accounts or AWS Regions on demand or automatically as part of a scheduled backup plan for most resource types, though backups in cold storage or archive tiers cannot be copied.")],
 scope="cross-account and cross-Region copies", tier0=True, bullets=["1.3.S5", "4.1.S6"]))
f.append(F("backup-copy-no-sla-on-completion-time", "restriction",
 "AWS Backup does not provide any service-level agreements (SLAs) for copy job completion times; copy times vary with system load, capacity and resource size.",
 "Does AWS Backup guarantee a completion time for copy jobs?",
 ["does not provide any service-level agreements (SLAs)", "copy job completion times"],
 [E(RC, "AWS Backup does not provide any service-level agreements (SLAs) for copy job completion times. Copy times can vary based upon system load, capacity, and the size of the resources being copied, even for copy jobs containing the same resources.")],
 scope="copy jobs", rel="extended", bullets=["1.3.S5", "2.2.K4"]))
f.append(F("backup-copy-one-job-at-a-time-per-resource", "restriction",
 "Only one backup or copy job can run at a time for a given resource; additional copy jobs for that resource stay in CREATED status until the running job completes.",
 "How many backup or copy jobs can run at once for one resource?",
 ["Only one backup or copy job can run at a time", "remain in CREATED status"],
 [E(RC, "Only one backup or copy job can run at a time for a given resource. Additional copy jobs for the same resource remain in `CREATED` status until the running job completes.")],
 scope="per resource", dm="max", rel="extended", bullets=["1.3.S5"]))
f.append(F("backup-expired-recovery-points-still-stored-and-billed", "behavior",
 "Recovery points that AWS Backup could not delete (status EXPIRED) stay in your account and might increase your storage costs until you delete them manually.",
 "What happens to recovery points that AWS Backup could not delete?",
 ["continue to store expired recovery points in your account", "increase your storage costs"],
 [E(DB, "You will continue to store expired recovery points in your account. This might increase your storage costs.")],
 scope="EXPIRED recovery points", rel="extended", bullets=["4.3.S1"]))
f.append(F("backup-plan-update-does-not-change-existing-recovery-points", "behavior",
 "Updating a backup plan affects the recovery points it creates in the future, but not the recovery points it has already created.",
 "Does editing a backup plan change the retention of existing recovery points?",
 ["affects the future recovery points it will create", "does not affect the recovery point it already created"],
 [E(DB, "Updating the backup plan affects the future recovery points it will create, but does not affect the recovery point it already created.")],
 scope="backup plan updates", tier0=True, bullets=["4.1.S6"]))
dump("facts-behavior-10.json", f[:13])
dump("facts-behavior-11.json", f[13:])
