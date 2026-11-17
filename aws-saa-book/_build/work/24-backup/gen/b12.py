import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
PI, RB, EFS, DDB, AUR, RT, RV = D + "point-in-time-recovery", D + "restoring-a-backup", D + "restoring-efs", D + "restoring-dynamodb", D + "restoring-aur", D + "restore-testing", D + "restore-testing-validation"
AM, CC, AR, LH, W = D + "aws-backup-audit-manager", D + "choosing-controls", D + "working-with-audit-reports", D + "legalhold", D + "whatisbackup"
f = []
f.append(F("backup-continuous-rds-copy-uses-snapshot-instead-of-logs", "behavior",
 "For RDS continuous backups, AWS Backup creates a snapshot and copies it with the frequency specified in the backup plan, instead of copying transaction logs.",
 "How does AWS Backup copy an RDS continuous backup to another Region?",
 ["creates a snapshot and copies it", "frequency specified in the backup plan"],
 [E(PI, "Instead, AWS Backup creates a snapshot and copies it with the frequency specified in the backup plan.")],
 scope="RDS continuous backups", bullets=["1.3.S5"]))
f.append(F("backup-restore-creates-new-resource-protects-existing", "behavior",
 "When you use AWS Backup to restore a backup, it creates a new resource from the backup, to protect your existing resources from being destroyed by the restore.",
 "Does an AWS Backup restore overwrite the existing resource?",
 ["it creates a new resource", "protect your existing resources from being destroyed"],
 [E(RB, "When you use AWS Backup to restore a backup, it creates a new resource with the backup that you are restoring. This is to protect your existing resources from being destroyed by your restore activity.")],
 scope="AWS Backup restores", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-destructive-exceptions-listed", "restriction",
 "A small set of resource types perform destructive restores that overwrite existing data; for all other resource types AWS Backup creates a new resource during restore.",
 "Which AWS Backup restores can overwrite existing data?",
 ["perform destructive restores that overwrite existing data", "creates a new resource during restore"],
 [E(RB, "The following resource types perform destructive restores that overwrite existing data:"),
  E(RB, "For all other resource types, AWS Backup creates a new resource during restore.")],
 scope="AWS Backup restores", cond="the exceptions are the resource types the page lists as destructive", bullets=["1.3.K2"]))
f.append(F("backup-restore-no-sla-for-restore-time", "restriction",
 "AWS Backup does not provide any service-level agreements (SLAs) for restore time; restore times vary with system load and capacity.",
 "Does AWS Backup guarantee a restore time?",
 ["does not provide any service-level agreements (SLAs) for a restore time", "system load and capacity"],
 [E(RB, "AWS Backup does not provide any service-level agreements (SLAs) for a restore time. Restore times can vary based upon system load and capacity, even for restores containing the same resources.")],
 scope="AWS Backup restores", tier0=True, bullets=["1.3.K2", "2.2.K4"]))
f.append(F("backup-restore-from-cold-storage-takes-longer", "behavior",
 "Restoring from cold storage typically takes 4 hours more than restoring from warm storage.",
 "How much longer does a restore from cold storage take than from warm storage?",
 ["typically takes 4 hours more", "than restoring from warm storage"],
 [E(RB, "Restoring from cold storage typically takes 4 hours more than restoring from warm storage.")],
 scope="restore from cold storage", cond="typical value", tier0=True, bullets=["1.3.K2", "4.1.S6"]))
f.append(F("backup-restore-tags-copied-by-default-in-console-not-in-api", "default",
 "When you restore in the console, source tags are copied by default; in the StartRestoreJob API, CopySourceTagsToRestoredResource is false by default, which excludes the original source tags.",
 "Are tags copied to a restored resource by default?",
 ["your source tags will be copied by default", "set to false by default"],
 [E(RB, "When you restore a backup in the console flow, your source tags will be copied by default. In the console, uncheck the box if you wish to opt out of copying tags to a restored resource"),
  E(RB, "In the API operation StartRestoreJob, the parameter CopySourceTagsToRestoredResource is set to false by default, which will exclude the original source tags from the resource you are restoring.")],
 scope="restore jobs, console versus API", dm="default", adj=True, rel="extended", bullets=["1.3.K2"]))
f.append(F("backup-restore-efs-full-or-item-level", "capability",
 "For an Amazon EFS restore you can perform a full restore, which restores the entire file system, or an item-level restore of a specific file or directory.",
 "Which kinds of restore does AWS Backup offer for EFS?",
 ["full restore or an item-level restore", "restores a specific file or directory"],
 [E(EFS, "If you are restoring an Amazon Elastic File System (Amazon EFS) instance, you can perform a full restore or an item-level restore."),
  E(EFS, "When you perform an item-level restore, AWS Backup restores a specific file or directory.")],
 scope="Amazon EFS restores", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-efs-no-destructive-restore-recovery-directory", "restriction",
 "AWS Backup does not support destructive restores with Amazon EFS: it restores the file system to a recovery directory off the root directory instead of overwriting the source or an existing file system.",
 "Does an EFS restore overwrite the existing file system?",
 ["does not support destructive restores with Amazon EFS", "recovery directory off of the root directory"],
 [E(EFS, "AWS Backup does not support destructive restores with Amazon EFS. A destructive restore is when a restored file system deletes or overwrites the source or existing file system. Instead, AWS Backup restores your file system to a recovery directory off of the root directory.")],
 scope="Amazon EFS restores", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-efs-files-not-in-original-locations", "behavior",
 "After an EFS full restore, the restored files are in a recovery subdirectory under the root of the file system, not in their original locations, and you must manually move or copy them to where they belong.",
 "Where do restored EFS files end up and what must you do?",
 ["located in a recovery subdirectory under the root", "Files are not restored to their original locations"],
 [E(EFS, "After a full restore completes, all restored files are located in a recovery subdirectory under the root of the file system."),
  E(EFS, "Files are not restored to their original locations. You must manually move or copy the restored files from this recovery directory to their intended locations. The same behavior applies to item-level restores.")],
 scope="Amazon EFS restores", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-efs-item-level-to-new-or-existing-file-system", "capability",
 "You can restore EFS items to either a new or an existing file system, and each restore attempt creates a new recovery directory off the root directory to hold the restored files.",
 "Can an EFS item-level restore go to an existing file system?",
 ["either a new or existing file system", "creates a new recovery directory"],
 [E(EFS, "You can restore those items to either a new or existing file system."),
  E(EFS, "Regardless of whether you perform an Amazon EFS item-level restore to an existing file system or to a new file system, each restore attempt creates a new recovery directory off of the root directory to contain the restored files.")],
 scope="Amazon EFS item-level restores", bullets=["1.3.K2"]))
f.append(F("backup-restore-efs-single-weekly-backup-only-that-state", "behavior",
 "If you keep only one weekly backup of an EFS file system, you can restore only to the state of the file system when that backup was taken, not to earlier incremental backups.",
 "What can you restore if only one weekly EFS backup is kept?",
 ["can only restore to the state of the file system at the time you took that backup", "can't restore to prior incremental backups"],
 [E(EFS, "If you only keep one weekly backup, you can only restore to the state of the file system at the time you took that backup. You can't restore to prior incremental backups.")],
 scope="Amazon EFS restores", rel="extended", bullets=["1.3.K2"]))
f.append(F("backup-restore-ddb-to-new-table", "behavior",
 "A DynamoDB restore in AWS Backup creates a new table: you enter a new table name when you restore.",
 "Does an AWS Backup restore of a DynamoDB table overwrite the existing table?",
 ["enter a new table name", "New table name"],
 [E(DDB, "For Settings, New table name text field, enter a new table name.")],
 scope="DynamoDB restores", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-ddb-cross-region-same-key-needs-multi-region-key", "restriction",
 "To encrypt a table restored from a cross-Region backup with the same key as the original table, the key must be a multi-Region key; AWS-owned and AWS-managed keys are not multi-Region keys.",
 "Can a table restored from a cross-Region backup use an AWS-managed key identical to the source?",
 ["your key must be a multi-Region key", "AWS-owned and AWS-managed keys are not multi-Region keys"],
 [E(DDB, "When restoring a cross-Region backup, to encrypt your restored table using the same key you used to encrypt your original table, your key must be a multi-Region key. AWS-owned and AWS-managed keys are not multi-Region keys.")],
 scope="DynamoDB restores of cross-Region copies", bullets=["1.3.K2", "1.3.S5"]))
f.append(F("backup-restore-ddb-cross-account-same-key-must-be-shared", "restriction",
 "To encrypt a table restored from a cross-account backup with the same key as the original table, you must share the key in the source account with the destination account; AWS-owned and AWS-managed keys cannot be shared between accounts.",
 "What is needed to restore a cross-account DynamoDB backup with the original key?",
 ["you must share the key in your source account with your destination account", "cannot be shared between accounts"],
 [E(DDB, "When restoring a cross-account backup, to encrypt your restored table using the same key you used to encrypt your original table, you must share the key in your source account with your destination account. AWS-owned and AWS-managed keys cannot be shared between accounts.")],
 scope="DynamoDB restores of cross-account copies", bullets=["1.3.K2", "1.3.S5"]))
f.append(F("backup-restore-aurora-cluster-only-no-instance", "behavior",
 "AWS Backup restores an Aurora cluster; it does not create or attach an RDS instance to the cluster, so you add an instance to the restored cluster yourself.",
 "Does an Aurora restore through AWS Backup include a DB instance?",
 ["does not create or attach an Amazon RDS instance to your cluster", "AWS Backup restores your Aurora cluster"],
 [E(AUR, "AWS Backup restores your Aurora cluster; it does not create or attach an Amazon RDS instance to your cluster.")],
 scope="Aurora restores", tier0=True, bullets=["1.3.K2"]))
# Restore testing
f.append(F("backup-restore-testing-automated-periodic-evaluation", "behavior",
 "Restore testing is an AWS Backup feature that automatically and periodically evaluates whether restores will work, and monitors restore job duration.",
 "What is restore testing in AWS Backup?",
 ["automated and periodic evaluation of restore viability", "monitor restore job duration times"],
 [E(RT, "Restore testing, a feature offered by AWS Backup, provides automated and periodic evaluation of restore viability, as well as the ability to monitor restore job duration times.")],
 scope="AWS Backup restore testing", tier0=True, bullets=["1.3.K2", "2.2.S5"]))
f.append(F("backup-restore-testing-plan-steps", "behavior",
 "You create a restore testing plan with a name, the test frequency and the target start time, assign the resources to include, and choose specific or random recovery points; AWS Backup infers the metadata needed for the restore.",
 "How do you set up restore testing?",
 ["the frequency for your restore tests", "specific or random recovery points"],
 [E(RT, "First, you create a restore testing plan where you provide a name for your plan, the frequency for your restore tests, and the target start time. Then, you assign the resources you want to include in your plan. You then choose to include specific or random recovery points in your test. AWS Backup backup intelligently infers the metadata that will be needed for your restore job to be successful.")],
 scope="AWS Backup restore testing", bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-results-show-compliance-and-duration", "behavior",
 "When the scheduled time arrives AWS Backup starts restore jobs from the plan and monitors the time taken; afterwards you can use the results to show compliance, such as successful restore test scenarios or the restore job completion time.",
 "What can you use restore test results for?",
 ["monitors the time taken to complete the restore", "restore job completion time"],
 [E(RT, "When the scheduled time in your plan arrives, AWS Backup starts restore jobs based on your plan and monitors the time taken to complete the restore."),
  E(RT, "After the restore test plan completes its run, you can use the results to show compliance for organizational or governance requirements such as the successful completion of restore test scenarios or the restore job completion time.")],
 scope="AWS Backup restore testing", bullets=["1.3.K2", "2.2.K4"]))
f.append(F("backup-restore-testing-resources-deleted-after-validation", "behavior",
 "Once the optional validation completes or the validation window closes, AWS Backup deletes the resources involved in the restore test, in accordance with service SLAs.",
 "What happens to the restored resource after a restore test?",
 ["AWS Backup deletes the resources involved with the restore test", "validation window closes"],
 [E(RT, "Once the optional validation completes or the validation window closes, AWS Backup deletes the resources involved with the restore test, and the resources will be deleted in accordance with service SLAs.")],
 scope="AWS Backup restore testing", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-same-restore-jobs-as-on-demand", "behavior",
 "Restore testing runs restore jobs in the same way as on-demand restores and uses the same recovery points as an on-demand restore.",
 "How does a restore test differ from an on-demand restore in how it restores?",
 ["runs restore jobs in the same way as on-demand restores", "same recovery points"],
 [E(RT, "Restore testing runs restore jobs in the same way as on-demand restores and uses the same recovery points (backups) as an on-demand restore.")],
 scope="AWS Backup restore testing", rel="extended", bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-vs-restore-resources-row", "capability",
 "The resource types you can assign to a restore testing plan are Aurora, DocumentDB, DynamoDB, EBS, EC2, EFS, FSx (Lustre, ONTAP, OpenZFS, Windows), Neptune, RDS and S3, while any resource can be restored on demand.",
 "Which resource types can a restore testing plan include?",
 ["The resource types you can assign to your testing plan include", "All resources can be restored"],
 [ROW(RT, 0, 3)], scope="AWS Backup restore testing", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-vs-restore-results-row", "behavior",
 "After a restore testing job completes, the restored resource is deleted when the validation window finishes, whereas after an on-demand restore job the restored resource remains.",
 "Is the resource from a restore test kept?",
 ["the restored resource is deleted after the", "the restored version of the resource remains"],
 [ROW(RT, 0, 4)], scope="restore testing versus restore", tier0=True, bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-vs-restore-audit-manager-row", "capability",
 "AWS Backup Audit Manager can turn on a control to confirm whether a restore test meets specified restore objectives.",
 "Can Audit Manager check whether restore tests meet your restore objectives?",
 ["Can turn on a control to confirm if a restore test meets specified restore objectives", "AWS Backup Audit Manager"],
 [ROW(RT, 0, 1)], scope="restore testing", bullets=["1.3.K2", "1.3.S1"]))
f.append(F("backup-restore-testing-best-practice-designated-account", "behavior",
 "The recommended best practice for restore testing is to designate an account to be used for restore tests.",
 "Which account does AWS recommend for running restore tests?",
 ["designate an account to be used for restore tests", "Recommended best practice"],
 [ROW(RT, 0, 0)], scope="restore testing", rel="extended", bullets=["1.3.K2", "2.2.S5"]))
f.append(F("backup-restore-testing-tag-removed-needs-manual-delete", "restriction",
 "Resources restored by a restore testing plan that support tag-on-restore carry the awsbackup-restore-test tag; if a user removes the tag, AWS Backup cannot delete the resource at the end of the test and the user must delete it manually.",
 "What happens if the restore-test tag is removed from a restored resource?",
 ["awsbackup-restore-test", "AWS Backup cannot delete the resource at the end of the testing period"],
 [E(RT, "Resources that are restored by a restore testing plan and support tag-on-restore have a tag of `awsbackup-restore-test`. If a user removes this tag, AWS Backup cannot delete the resource at the end of the testing period and the user will have to delete it manually instead.")],
 scope="restore testing cleanup", rel="extended", bullets=["1.3.K2"]))
f.append(F("backup-restore-testing-validation-event-driven-eventbridge", "capability",
 "Restore testing validation is an optional event-driven check: you build a validation workflow with any EventBridge target such as Lambda and an EventBridge rule that listens for the restore job reaching COMPLETED.",
 "How do you validate a restore test result automatically?",
 ["event-driven validation", "any target supported by Amazon EventBridge"],
 [E(RV, "You have the option of creating an event-driven validation that runs when a restore testing job completes."),
  E(RV, "First, create a validation workflow with any target supported by Amazon EventBridge, such as AWS Lambda.")],
 scope="restore testing validation", rel="extended", bullets=["1.3.K2"]))
dump("facts-behavior-12.json", f[:15])
dump("facts-behavior-13.json", f[15:])

g = []
g.append(F("backup-audit-manager-audits-policies-against-controls", "behavior",
 "AWS Backup Audit Manager audits the compliance of your backup policies against controls that you define; a control is a procedure that audits a backup requirement such as backup frequency or retention period.",
 "What does AWS Backup Audit Manager do and what is a control?",
 ["audit the compliance of your AWS Backup policies against controls", "backup frequency or the backup retention period"],
 [E(AM, "You can use AWS Backup Audit Manager to audit the compliance of your AWS Backup policies against controls that you define. A control is a procedure designed to audit the compliance of a backup requirement, such as the backup frequency or the backup retention period.")],
 scope="AWS Backup Audit Manager", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-only-active-resources-evaluated", "restriction",
 "Only active resources are included when AWS Backup Audit Manager controls evaluate compliance: a running EC2 instance is evaluated, a stopped one is not.",
 "Are stopped EC2 instances evaluated by Audit Manager controls?",
 ["only active resources will be included", "An EC2 instance in a stopped state will not be included"],
 [E(AM, "Note that only active resources will be included when controls evaluate resources for compliance. For example, an Amazon EC2 instance in a running state will be evaluated. An EC2 instance in a stopped state will not be included in the compliance evaluation.")],
 scope="AWS Backup Audit Manager controls", bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-frameworks-and-daily-reports", "behavior",
 "In AWS Backup Audit Manager you create frameworks of governance control templates, view how many resources are compliant, and create reports; it automatically generates a new report every 24 hours, published to Amazon S3, and you can also generate on-demand reports.",
 "How does AWS Backup Audit Manager produce evidence of compliance?",
 ["Create frameworks that contain one or more governance control templates", "automatically generates a new report for you every 24 hours"],
 [E(AM, "Create frameworks that contain one or more governance control templates."),
  E(AM, "AWS Backup Audit Manager automatically generates a new report for you every 24 hours and publishes it to Amazon S3. You can also generate on-demand reports.")],
 scope="AWS Backup Audit Manager", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-needs-resource-tracking-aws-config", "restriction",
 "Before you create your first compliance-related framework in AWS Backup Audit Manager you must turn on resource tracking, which lets AWS Config track your AWS Backup resources, and charges apply for it.",
 "What must you turn on before creating an Audit Manager framework?",
 ["you must turn on resource tracking", "allows AWS Config to track your AWS Backup resources"],
 [E(AM, "Before you create your first compliance-related framework, you must turn on resource tracking. Doing so allows AWS Config to track your AWS Backup resources."),
  E(AM, "Charges apply when you turn on resource tracking.")],
 scope="AWS Backup Audit Manager frameworks", tier0=True, bullets=["1.3.S1", "4.3.S1"]))
g.append(F("backup-audit-manager-reports-two-types-job-and-compliance", "behavior",
 "AWS Backup Audit Manager has a second report type, the compliance report, which can monitor resource levels or the different controls in effect; the other type is the jobs report.",
 "Which report types does AWS Backup Audit Manager offer?",
 ["compliance report", "monitor resource levels or the different controls that are in effect"],
 [E(AR, "There are two types of reports. When you create a report, you choose which type is created."),
  E(AR, "The second type of report is a compliance report. Compliance reports can monitor resource levels or the different controls that are in effect.")],
 scope="AWS Backup Audit Manager reports", bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-reports-delivered-only-to-same-account-bucket", "restriction",
 "AWS Backup Audit Manager delivers reports only to Amazon S3 buckets that belong to the account in which the report plan or on-demand report is created; cross-account bucket delivery is not supported.",
 "Can an Audit Manager report be delivered to an S3 bucket in another account?",
 ["only to Amazon S3 buckets that belong to the account", "Cross-account Amazon S3 bucket delivery is not supported"],
 [E(AR, "AWS Backup Audit Manager delivers reports only to Amazon S3 buckets that belong to the account in which the report plan or on-demand report is created. Cross-account Amazon S3 bucket delivery is not supported.")],
 scope="AWS Backup Audit Manager reports", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-cross-account-reports-management-and-delegated-only", "restriction",
 "All account holders can create cross-Region reports, but only management and delegated administrator account holders can also create cross-account reports.",
 "Who can create organization-wide (cross-account) Audit Manager reports?",
 ["All account holders can create cross-Region reports", "also create cross-account reports"],
 [E(AR, "All account holders can create cross-Region reports; management and delegated administrator account holders can also create cross-account reports.")],
 scope="AWS Backup Audit Manager reports", bullets=["1.3.S1"]))
g.append(F("backup-audit-manager-findings-into-aws-audit-manager", "capability",
 "You can automatically import AWS Backup Audit Manager findings into AWS Audit Manager to include backup compliance in your overall compliance posture, and the daily reports can show evidence of compliance over time.",
 "Can backup compliance findings be included in AWS Audit Manager?",
 ["automatically import AWS Backup Audit Manager findings into AWS Audit Manager", "evidence of compliance with your controls over time"],
 [E(W, "It also generates daily reports that you can use to demonstrate evidence of compliance with your controls over time. To include your backup compliance alongside your overall compliance posture, you can automatically import AWS Backup Audit Manager findings into AWS Audit Manager.")],
 scope="AWS Backup Audit Manager", rel="extended", bullets=["1.3.S1"]))
for fid, row, claim, q, d in [
 ("in-backup-plan", 0, "The control Backup resources are included in at least one backup plan evaluates whether resources are included in at least one backup plan and has no customizable parameters.", "Which Audit Manager control checks that resources are in a backup plan?", ["Backup resources are included in at least one backup plan", "Evaluates if resources are included in at least one backup plan"]),
 ("min-frequency-retention", 1, "The control Backup plan has minimum frequency and minimum retention evaluates whether backup frequency and retention period meet the minimums you set, with the backup frequency and retention period as customizable parameters.", "Which Audit Manager control checks backup frequency and retention?", ["Backup plan has minimum frequency and minimum retention", "Backup frequency; retention period"]),
 ("vault-prevent-deletion", 2, "The control Vaults prevent manual deletion of recovery points evaluates whether backup vaults deny manual deletion of recovery points except by certain IAM roles, with no IAM role exceptions by default.", "Which Audit Manager control checks that vaults prevent manual deletion of recovery points?", ["Vaults prevent manual deletion of recovery points", "By default, there are no IAM role exceptions"]),
 ("encrypted", 3, "The control Recovery points are encrypted evaluates whether the recovery points are encrypted and has no customizable parameters.", "Which Audit Manager control checks that backups are encrypted?", ["Recovery points are encrypted", "Evaluates if the recovery points are encrypted"]),
 ("cross-region-copy", 5, "The control Cross-Region backup copy is scheduled evaluates whether a resource is configured to create copies of its backups to another AWS Region.", "Which Audit Manager control checks cross-Region copy?", ["Cross-Region backup copy is scheduled", "copies of its backups to another AWS Region"]),
 ("cross-account-copy", 6, "The control Cross-account backup copy is scheduled evaluates whether a resource has a cross-account backup copy configured.", "Which Audit Manager control checks cross-account copy?", ["Cross-account backup copy is scheduled", "cross-account backup copy configured"]),
 ("vault-lock", 7, "The control Resources are in a backup plan with an AWS Backup Vault Lock evaluates whether a resource has a backup plan configured to store backups in a locked backup vault.", "Which Audit Manager control checks that backups go to a locked vault?", ["Resources are in a backup plan with an AWS Backup Vault Lock", "store backups in a locked backup vault"]),
 ("restore-time", 9, "The control Restore time for resources meet target evaluates whether a restore testing job completed within the target restore time.", "Which Audit Manager control compares restore test time with a target?", ["Restore time for resources meet target", "restore testing job completed within target restore time"]),
 ("in-lag-vault", 10, "The control Resources are inside a logically air-gapped vault evaluates whether resources have at least one recovery point copied to a logically air-gapped vault within the specified value and timeframe.", "Which Audit Manager control checks logically air-gapped vault copies?", ["Resources are inside a logically air-gapped vault", "at least one recovery point copied to a logically air-gapped vault"]),
]:
    g.append(F("backup-audit-manager-control-" + fid, "capability", claim, q, d, [ROW(CC, 0, row)],
     scope="AWS Backup Audit Manager controls", bullets=["1.3.S1"], rel=("core" if fid in ("vault-prevent-deletion", "cross-region-copy", "vault-lock", "restore-time") else "extended")))
# Legal hold
g.append(F("backup-legal-hold-prevents-deletion-delays-lifecycle", "behavior",
 "A legal hold is an administrative tool that prevents backups from being deleted while under the hold, and lifecycle policies that would alter the backup status are delayed until the hold is removed.",
 "What does a legal hold do to a backup and its lifecycle?",
 ["backups under a hold cannot be deleted", "delayed until the legal hold is removed"],
 [E(LH, "A legal hold is an administrative tool that helps prevent backups from being deleted while under a hold. While the hold is in place, backups under a hold cannot be deleted and lifecycle policies that would alter the backup status (such as transition to a `Deleted` state) are delayed until the legal hold is removed.")],
 scope="AWS Backup legal holds", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-legal-hold-not-for-continuous-backups", "restriction",
 "Legal holds can be applied to backups created by AWS Backup if their lifecycles allow it, but legal holds do not apply to continuous backups.",
 "Can a legal hold protect a continuous backup?",
 ["Legal holds do not apply to continuous backups", "one or more backups"],
 [E(LH, "Legal holds can be applied to one or more backups (also known as recovery points) created by AWS Backup if their lifecycles allow it. Legal holds do not apply to continuous backups.")],
 scope="AWS Backup legal holds", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-legal-hold-only-original-backup-not-copies", "restriction",
 "Legal holds apply only to the original backup; a backup copied across Regions or accounts does not carry its legal hold, and only recovery points created by AWS Backup can be part of a legal hold.",
 "Does a legal hold follow a backup that is copied to another Region or account?",
 ["apply only to the original backup on which they are placed", "does not retain or carry its legal hold with it"],
 [E(LH, "Legal holds apply only to the original backup on which they are placed. When a backup is copied across Regions or accounts (if the resource supports it), it does not retain or carry its legal hold with it. A legal hold, like other resources, has a unique ARN (Amazon Resource Name) associated with it. Only recovery points created by AWS Backup can be part of a legal hold.")],
 scope="AWS Backup legal holds", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-legal-hold-no-expiry-released-by-user-complements-vault-lock", "behavior",
 "A legal hold gives additional protection against deletion of individual recovery points, does not expire, and stays active until a user with sufficient permissions releases it, whereas Vault Lock protects the vault.",
 "How does a legal hold differ from Vault Lock and when does it end?",
 ["does not expire and retains the data within the backup indefinitely", "released by a user with sufficient permissions"],
 [E(LH, "Note that while AWS Backup Vault Lock provides additional protections and immutability to a vault, a legal hold provides additional protection against deletion of individual backups (recovery points). The legal hold does not expire and retains the data within the backup indefinitely. The hold remains active until it is released by a user with sufficient permissions.")],
 scope="AWS Backup legal holds and Vault Lock", tier0=True, bullets=["1.3.S1"]))
g.append(F("backup-legal-hold-multiple-holds-backup-kept-until-all-removed", "behavior",
 "A backup cannot be deleted as long as it has at least one legal hold; after all legal holds on it are removed, it is subject to its retention lifecycle again.",
 "When does a backup under legal hold become subject to its lifecycle again?",
 ["cannot be deleted as long as it has at least one legal hold", "After all legal holds on a backup are removed"],
 [E(LH, "A backup cannot be deleted as long as it has at least one legal hold. After all legal holds on a backup are removed, it is subject to its retention lifecycle properties.")],
 scope="AWS Backup legal holds", bullets=["1.3.S1"]))
dump("facts-behavior-14.json", g)
