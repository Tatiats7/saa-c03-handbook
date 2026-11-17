import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
EBSL = "docs/ebs/latest/userguide/snapshot-lifecycle"
DDB = "docs/amazondynamodb/latest/developerguide/Backup-and-Restore"
ST = "docs/whitepapers/latest/aws-overview/storage-services"
CV = "www/solutions/case-studies/calverthealth-case-study"
MB, OD, CB, EB, W = D + "metering-and-billing", D + "recov-point-create-on-demand-backup", D + "creating-a-backup", D + "editing-a-backup", D + "whatisbackup"
f = []
f.append(F("ebs-dlm-no-additional-cost-complete-backup-for-ec2-and-ebs", "pricing-dimension",
 "Combined with EventBridge and CloudTrail monitoring, Amazon Data Lifecycle Manager provides a complete backup solution for EC2 instances and EBS volumes at no additional cost.",
 "Does Amazon Data Lifecycle Manager cost extra for EBS snapshot and AMI automation?",
 ["at no additional cost", "complete backup solution for Amazon EC2 instances and EBS volumes"],
 [E(EBSL, "Combined with Amazon EventBridge and AWS CloudTrail monitoring, Amazon Data Lifecycle Manager provides a complete backup solution for Amazon EC2 instances and EBS volumes at no additional cost.")],
 scope="Amazon Data Lifecycle Manager", service="ebs", tier0=True, bullets=["4.1.K5", "4.3.S1"]))
f.append(F("dynamodb-backup-on-demand-two-options-dynamodb-or-aws-backup", "behavior",
 "There are two options for creating and managing DynamoDB on-demand backups: DynamoDB itself and AWS Backup.",
 "Who can create and manage DynamoDB on-demand backups?",
 ["two options for creating and managing DynamoDB on-demand backups", "AWS Backup"],
 [E(DDB, "There are two options for creating and managing DynamoDB on-demand backups:")],
 scope="DynamoDB on-demand backups", service="dynamodb", tier0=True, bullets=["4.1.K5", "1.3.S5"]))
f.append(F("dynamodb-backup-native-no-abac-tagging-use-aws-backup", "restriction",
 "Tagging and attribute-based access control (ABAC) are not supported for native DynamoDB backups, so to use ABAC with backups you should use AWS Backup.",
 "Can you use tag-based access control on native DynamoDB backups?",
 ["aren't supported for DynamoDB backups", "we recommend that you use AWS Backup"],
 [E(DDB, "Tagging and attribute-based access control (ABAC) aren't supported for DynamoDB backups. To use ABAC with backups, we recommend that you use AWS Backup.")],
 scope="native DynamoDB backups", service="dynamodb", tier0=True, bullets=["4.1.K5", "1.3.S1"]))
f.append(F("backup-overview-whitepaper-centralize-automate-policy-based", "behavior",
 "The AWS overview whitepaper describes AWS Backup as a cost-effective, fully managed, policy-based service that enables you to centralize and automate data protection across AWS services.",
 "How does the AWS overview of storage services describe AWS Backup?",
 ["centralize and automate data protection across AWS services", "cost-effective, fully managed, policy-based service"],
 [E(ST, "AWS Backup enables you to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale.")],
 scope="AWS Backup", hard=False, bullets=["4.1.S6", "4.1.K5"]))
f.append(F("backup-billing-not-fully-managed-billed-by-service-lag-vault-under-backup", "pricing-dimension",
 "For resource types without full AWS Backup management, some AWS Backup activity such as storage costs is billed under the respective AWS service, but with a logically air-gapped vault all storage and data transfer charges appear under AWS Backup.",
 "Where do backup storage charges appear for resource types that are not fully managed?",
 ["billing reflected by the respective AWS service", "all storage or data transfer charges occur under AWS Backup"],
 [E(MB, "When a resource type does not support full AWS Backup management, some of your AWS Backup activity such as storage costs for your backups, have billing reflected by the respective AWS service. However, if you are using a Logically air-gapped vault, all storage or data transfer charges occur under AWS Backup.")],
 scope="AWS Backup billing", tier0=True, bullets=["4.3.S1"]))
f.append(F("backup-audit-manager-pricing-per-control-evaluation-and-config", "pricing-dimension",
 "AWS Backup Audit Manager is charged by the number of control evaluations, where one evaluation is one resource against one control, and AWS Config recording, which it requires, is charged separately on the AWS Config bill.",
 "What do you pay for with AWS Backup Audit Manager?",
 ["charges for usage based on the number of control evaluations", "AWS Config charges for each configuration item recorded"],
 [E(MB, "AWS Backup Audit Manager charges for usage based on the number of control evaluations. A control evaluation is the evaluation of one resource against one control. Control evaluation charges appear on your AWS Backup bill."),
  E(MB, "To use AWS Backup Audit Manager controls, you must enable AWS Config recording to track your backup activity. AWS Config charges for each configuration item recorded, and these charges appear on your AWS Config bill.")],
 scope="AWS Backup Audit Manager", tier0=True, bullets=["4.3.S1", "1.3.S1"]))
f.append(F("backup-pricing-cost-allocation-tags-cost-explorer", "capability",
 "You can use cost allocation tags to track and optimize AWS Backup costs on a detailed level, and view and filter those tags in AWS Cost Explorer.",
 "How can you track AWS Backup costs per tag?",
 ["cost allocation tags to track and optimize AWS Backup costs", "AWS Cost Explorer"],
 [E(MB, "You can use cost allocation tags to track and optimize AWS Backup costs on a detailed level, and view and filter those tags using AWS Cost Explorer.")],
 scope="AWS Backup cost allocation tags", bullets=["4.3.S1"]))
f.append(F("backup-automatic-backups-use-plan-lifecycle-vault-and-tags", "behavior",
 "Backups created automatically by backup plans are configured with the lifecycle settings of the plan, organized in the backup vault the plan specifies, and assigned the tags listed in the plan.",
 "What settings does an automatic backup get from its backup plan?",
 ["configured with the lifecycle settings that are defined in the backup plan", "organized in the backup vault that is specified in the backup plan"],
 [E(CB, "When backups are created automatically by backup plans, they are configured with the lifecycle settings that are defined in the backup plan. They are organized in the backup vault that is specified in the backup plan. They are also assigned the tags that are listed in the backup plan.")],
 scope="backup plans", bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-edit-lifecycle-and-tags-after-creation", "capability",
 "After you create a backup, you can change its lifecycle or tags; the lifecycle defines when the backup moves to cold storage and when it expires, and AWS Backup transitions and expires backups automatically according to it.",
 "Can you change the lifecycle of a backup after it is created?",
 ["you can change the lifecycle or tags of the backup", "AWS Backup transitions and expires backups automatically"],
 [E(EB, "After you create a backup using AWS Backup, you can change the lifecycle or tags of the backup. The lifecycle defines when a backup is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.")],
 scope="AWS Backup recovery points", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-on-demand-ec2-no-reboot-default", "default",
 "AWS Backup takes EC2 backups with no reboot as the default behavior.",
 "Does an AWS Backup EC2 backup reboot the instance by default?",
 ["EC2 backups with \"no reboot\" as the default behavior", "AWS Backup takes EC2 backups"],
 [E(OD, "AWS Backup takes EC2 backups with \"no reboot\" as the default behavior.")] if False else [E(OD, "AWS Backup takes EC2 backups with \"no reboot\" as the default behavior. AWS Backup currently supports resources running on Amazon EC2, and certain instance types are not supported.")],
 scope="EC2 backups", dm="default", bullets=["4.1.S6"]))
f.append(F("backup-on-demand-retention-split-between-warm-and-cold", "behavior",
 "For an on-demand backup you set the total retention period in days, and if you specify time in cold storage the retention period is divided between warm and cold storage.",
 "How is the retention of an on-demand backup divided between warm and cold storage?",
 ["total retention period", "divided between warm and cold storage"],
 [E(OD, "For Total retention period, specify the number of days. If you specified time in cold storage, the retention period is divided between warm and cold storage.")],
 scope="on-demand backups", bullets=["4.1.S6"]))
f.append(F("backup-case-calverthealth-edr-and-aws-backup-rto-72-hours-to-under-2", "case-study",
 "CalvertHealth deployed AWS Elastic Disaster Recovery and AWS Backup on almost 140 servers for its electronic health records system, and the changes cut its recovery time objective from 72 hours to under 2 hours, a 97 percent improvement.",
 "What RTO improvement did CalvertHealth get with AWS Elastic Disaster Recovery and AWS Backup?",
 ["72 hours to under 2 hours", "97 percent improvement"],
 [E(CV, "A CalvertHealth network engineer worked alongside HealthCare Triangle and the AWS team to deploy AWS Elastic Disaster Recovery and AWS Backup on almost 140 servers."),
  E(CV, "The changes reduced CalvertHealth’s RTO from 72 hours to under 2 hours—a 97 percent improvement."),
  E(CV, "The RTO for CalvertHealth’s EHR system was 48 to 72 hours—an unacceptable amount of time.")],
 scope="CalvertHealth electronic health records system", tier=4, tier0=False, rel="extended", bullets=["2.2.K4"]))
dump("facts-behavior-25.json", f)
