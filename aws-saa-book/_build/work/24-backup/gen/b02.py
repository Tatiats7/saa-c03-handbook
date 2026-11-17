import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/24-backup")
from fx import *
D = "docs/aws-backup/latest/devguide/"
WS, FA, V, AP = D + "working-with-supported-services", D + "backup-feature-availability", D + "create-a-vault", D + "create-a-vault-access-policy"
f = []
f.append(F("backup-native-service-backups-not-centrally-governed", "restriction",
 "Some AWS services offer their own stand-alone backup features that work without AWS Backup, but the backups those services create themselves are not available for central governance through AWS Backup.",
 "Does AWS Backup centrally govern the backups that a service creates with its own backup feature?",
 ["offer their own, stand-alone backup features", "not available for central governance through AWS Backup"],
 [E(WS, "Some AWS Backup-supported AWS services offer their own, stand-alone backup features. Those features are available to you independent of whether you use AWS Backup. However, the backups other AWS services create are not available for central governance through AWS Backup.")],
 scope="backups created by the services themselves", tier0=True, bullets=["4.1.K5"]))
f.append(F("backup-native-relationship-varies-by-service", "behavior",
 "How AWS Backup relates to a service's native backups varies by service: for some, such as RDS continuous backups, it uses the same underlying backup infrastructure; for others, such as DynamoDB, it works as a separate backup layer.",
 "Does AWS Backup use the same infrastructure as a service's native backups, or a separate layer?",
 ["varies by service", "separate backup layer", "same underlying backup infrastructure"],
 [E(W := D + "whatisbackup", "The relationship between AWS Backup and native service backup mechanisms varies by service. In some cases, AWS Backup uses the same underlying backup infrastructure as the native service (for example, Amazon RDS continuous backups). In other cases, AWS Backup operates as a separate backup layer (for example, DynamoDB).")],
 scope="AWS Backup and native service backups", bullets=["4.1.K5"]))
f.append(F("backup-central-management-needs-opt-in-plan-and-vault", "behavior",
 "To centrally manage data protection for your supported services, you opt in to managing that service with AWS Backup, create an on-demand backup or schedule backups with a backup plan, and store the backups in backup vaults.",
 "What must you do for AWS Backup to centrally manage the protection of a supported service?",
 ["opt in to managing that service with AWS Backup", "store your backups in backup vaults"],
 [E(WS, "To configure AWS Backup to centrally manage data protection for all your supported services, you must opt in to managing that service with AWS Backup, create an on-demand backup or schedule backups using a backup plan, and store your backups in backup vaults.")],
 scope="AWS Backup central management", bullets=["4.1.K5"]))
f.append(F("backup-ddb-advanced-features-since-2021-11", "capability",
 "Since November 2021 AWS Backup has advanced features for DynamoDB backups: copying backups across Regions and accounts, tiering backups to cold storage, and using tags for permissions and cost management.",
 "What do the advanced DynamoDB backup features in AWS Backup add?",
 ["copying your backups across AWS Regions and accounts", "tiering backups to cold storage", "November 2021"],
 [E(WS, "Starting November 2021, AWS Backup also introduced advanced features for DynamoDB backups. Those advanced features include copying your backups across AWS Regions and accounts, tiering backups to cold storage, and using tags for permissions and cost management.")],
 scope="DynamoDB backups in AWS Backup", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-ddb-advanced-default-for-new-customers", "default",
 "New AWS Backup customers onboarding after November 2021 have the advanced DynamoDB backup features enabled by default.",
 "Are the advanced DynamoDB backup features on by default?",
 ["enabled by default", "onboarding after November 2021"],
 [E(WS, "New AWS Backup customers onboarding after November 2021 will have advanced DynamoDB backup features enabled by default.")],
 scope="AWS Backup customers onboarding after November 2021", dm="default", cond="existing customers are recommended to enable them", bullets=["4.1.S6"]))
f.append(F("backup-ddb-advanced-same-warm-price-tier-and-tag-savings", "behavior",
 "Enabling the advanced DynamoDB features does not change warm backup storage pricing, and you can save money by tiering backups to cold storage and by using cost allocation tags.",
 "Does enabling the advanced DynamoDB backup features change the warm storage price?",
 ["no difference in warm backup storage pricing", "tiering backups to cold storage"],
 [E(WS, "We recommend all existing AWS Backup customers enable advanced features for DynamoDB. There is no difference in warm backup storage pricing after you enable advanced features, and you can save money by tiering backups to cold storage and optimize your costs by using cost allocation tags.")],
 scope="DynamoDB backups in AWS Backup", bullets=["4.1.S6", "4.3.S1"]))
f.append(F("backup-fsx-uses-native-fsx-backup-same-consistency", "behavior",
 "AWS Backup uses the built-in backup functionality of Amazon FSx, so backups taken from the AWS Backup console have the same file system consistency, performance and restore options as backups taken in the FSx console.",
 "Does an FSx backup taken through AWS Backup differ in consistency from one taken in the FSx console?",
 ["built-in backup functionality of Amazon FSx", "same restore options"],
 [E(WS, "AWS Backup uses the built-in backup functionality of Amazon FSx. So backups taken from the AWS Backup console have the same level of file system consistency and performance, and the same restore options as backups that are taken through the Amazon FSx console.")],
 scope="FSx file systems", bullets=["4.1.S6"]))
f.append(F("backup-fsx-backups-kept-after-source-deleted", "behavior",
 "When AWS Backup manages FSx backups, it keeps them even after the source file system is deleted, which protects against accidental or malicious deletion.",
 "Are FSx backups managed by AWS Backup kept after the file system is deleted?",
 ["retains your backups even after the source file system is deleted", "accidental or malicious deletion"],
 [E(WS, "If you use AWS Backup to manage these backups, you gain additional functionality, such as unlimited retention options, and the ability to create scheduled backups as frequently as every hour. In addition, AWS Backup retains your backups even after the source file system is deleted. This protects against accidental or malicious deletion.")],
 scope="FSx backups managed by AWS Backup", tier0=True, bullets=["4.1.S6", "2.2.S5"]))
f.append(F("backup-ec2-whole-instance-single-recovery-point", "capability",
 "AWS Backup can back up an entire EC2 instance including its EBS volumes, and you can restore the whole instance from a single recovery point, including root volume, data volumes and some configuration such as instance type and key pair.",
 "Can you restore an entire EC2 instance from one AWS Backup recovery point?",
 ["restore an entire Amazon EC2 instance from a single recovery point", "instance type and key pair"],
 [E(WS, "You can schedule or perform on-demand backup jobs that include entire EC2 instances, including its Amazon EBS volumes. Therefore, you can restore an entire Amazon EC2 instance from a single recovery point, including the root volume, data volumes, and some instance configuration settings, such as the instance type and key pair.")],
 scope="EC2 instances in AWS Backup", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-ec2-backup-is-ebs-backed-ami-with-snapshots", "behavior",
 "An EC2 backup in AWS Backup takes snapshots of the root volume, launch configuration and all associated EBS volumes, stores certain instance configuration parameters, and stores the backup data as an EBS volume-backed AMI.",
 "What does AWS Backup create when it backs up an EC2 instance?",
 ["Amazon EBS volume-backed Amazon Machine Image (AMI)", "snapshot of the root Amazon EBS storage volume"],
 [E(WS, "When backing up an Amazon EC2 instance, AWS Backup takes a snapshot of the root Amazon EBS storage volume, the launch configurations, and all associated EBS volumes. AWS Backup stores certain configuration parameters of the EC2 instance, including instance type, security groups, Amazon VPC, monitoring configuration, and tags. The backup data is stored as an Amazon EBS volume-backed Amazon Machine Image (AMI).")],
 scope="EC2 instances in AWS Backup", tier0=True, bullets=["4.1.S6"]))
f.append(F("backup-ec2-never-reboots-instances", "behavior",
 "AWS Backup does not reboot your EC2 instances at any time.",
 "Does AWS Backup reboot an EC2 instance to back it up?",
 ["does not reboot your EC2 instances", "at any time"],
 [E(WS, "AWS Backup does not reboot your EC2 instances at any time.")],
 scope="EC2 instances in AWS Backup", bullets=["4.1.S6"]))
f.append(F("backup-ec2-marketplace-product-code-ami-no-cross-account-copy", "restriction",
 "An AMI created from an instance launched from an AWS Marketplace AMI has a product code, and with Amazon EC2 you cannot copy an AMI with a product code to another account, so AWS Backup has the same restriction.",
 "Can AWS Backup copy a backup of an EC2 instance that was launched from an AWS Marketplace AMI to another account?",
 ["can't copy an AMI with a product code to another account", "AWS Backup also has this restriction"],
 [E(WS, "If the instance was launched from an AMI from AWS Marketplace, the instance has a product code. An AMI created from the instance also has a product code. With Amazon EC2, you can't copy an AMI with a product code to another account. Therefore, AWS Backup also has this restriction.")],
 scope="EC2 instances launched from AWS Marketplace AMIs", rel="extended", bullets=["1.3.S5"]))
f.append(F("backup-efs-automatic-backup-vault-reserved", "restriction",
 "The EFS automatic backup vault aws/efs/automatic-backup-vault is reserved for automatic EFS backups only; using it as a destination for other backup plans gives an insufficient privileges error.",
 "Can you use the EFS automatic backup vault as the destination of your own backup plan or for cross-account copies?",
 ["reserved for those automatic backups only", "insufficient privileges"],
 [E(WS, "The Amazon EFS automatic backup vault aws/efs/automatic-backup-vault is reserved for those automatic backups only. This vault should not be used to create cross-account copies or as a destination for backups created by other non-automated backup plans. If you use it as a destination for other backup plans, you will receive an \"insufficient privileges\" error.")],
 scope="Amazon EFS automatic backup vault", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-aurora-vault-snapshots-no-charge-condition", "pricing-dimension",
 "AWS does not charge for Aurora snapshots in a backup vault as long as Aurora automated backups are enabled and their retention period is longer than the retention period of the Aurora snapshots; snapshots whose database was deleted are charged.",
 "When are Aurora snapshots stored in an AWS Backup vault not charged?",
 ["does not charge for Aurora snapshots stored inside a backup vault", "charged if the snapshots' database is deleted"],
 [E(WS, "AWS does not charge for Aurora snapshots stored inside a backup vault as long as Aurora has automated backups enabled and the retention period for Aurora automated backups is more than the retention period of Aurora snapshots. Any snapshots within the backup vault will be charged if the snapshots’ database is deleted (deletions may occur accidentally or during blue/green deployment).")],
 scope="Aurora snapshots in an AWS Backup vault", cond="Aurora automated backups enabled and automated-backup retention longer than snapshot retention", tier0=True, bullets=["4.3.S1"]))
f.append(F("backup-storage-gateway-volume-gateway-supported", "capability",
 "AWS Backup supports Storage Gateway Volume Gateway, and you can restore EBS snapshots as Storage Gateway volumes.",
 "Which Storage Gateway type does AWS Backup support?",
 ["AWS Backup supports Storage Gateway Volume Gateway", "restore Amazon EBS snapshots as Storage Gateway volumes"],
 [E(WS, "AWS Backup supports Storage Gateway Volume Gateway. You can also restore Amazon EBS snapshots as Storage Gateway volumes.")],
 scope="AWS Storage Gateway", bullets=["4.1.S6"]))
f.append(F("backup-vmware-vms-on-premises-and-vmc", "capability",
 "AWS Backup protects on-premises VMware virtual machines and VMs in VMware Cloud on AWS: you can back them up to AWS Backup and restore them to either on premises or VMware Cloud.",
 "Can AWS Backup back up on-premises VMware virtual machines?",
 ["on-premises VMware virtual machines", "restore from AWS Backup to either on premises or VMC"],
 [E(WS, "AWS Backup supports centralized and automated data protection for on-premises VMware virtual machines (VMs) along with VMs in the VMware Cloud™ (VMC) on AWS. You can back up from your on premises and VMC virtual machines to AWS Backup. Then, you can restore from AWS Backup to either on premises or VMC.")],
 scope="VMware virtual machines", bullets=["4.1.S6"]))
f.append(F("backup-gateway-connects-vmware-to-backup", "behavior",
 "Backup gateway is downloadable AWS Backup software that you deploy to your VMware infrastructure to connect your VMware VMs to AWS Backup.",
 "What connects VMware virtual machines to AWS Backup?",
 ["Backup gateway", "downloadable AWS Backup software"],
 [E(WS, "Backup gateway is downloadable AWS Backup software that you deploy to your VMware infrastructure to connect your VMware VMs to AWS Backup.")],
 scope="VMware virtual machines", hard=False, bullets=["4.1.S6"]))
f.append(F("backup-eks-cluster-state-and-persistent-storage", "capability",
 "AWS Backup backs up Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached by a persistent volume claim (EBS volumes, EFS file systems and S3 buckets), as a composite recovery point with a child recovery point for each resource.",
 "What does AWS Backup back up for an Amazon EKS cluster?",
 ["Kubernetes cluster state and persistent storage", "composite recovery point"],
 [E(WS, "AWS Backup supports backups of Amazon EKS clusters, including Kubernetes cluster state and persistent storage attached to the EKS cluster via a persistent volume claim (EBS volumes, EFS file systems, and S3 buckets)."),
  E(WS, "An Amazon EKS backup will create a composite recovery point, where a child recovery point will be for each resource backed up.")],
 scope="Amazon EKS clusters", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-redshift-clusters-and-serverless-namespaces", "capability",
 "AWS Backup supports Amazon Redshift provisioned clusters and Redshift Serverless namespaces.",
 "Which Amazon Redshift deployments does AWS Backup support?",
 ["Amazon Redshift provisioned clusters", "Redshift Serverless namespaces"],
 [E(WS, "AWS Backup supports Amazon Redshift provisioned clusters and Redshift Serverless namespaces.")],
 scope="Amazon Redshift", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-organizations-cross-account-monitoring-management", "capability",
 "AWS Backup works with AWS Organizations to simplify cross-account monitoring and management.",
 "What does AWS Backup do with AWS Organizations?",
 ["simplify cross-account monitoring and management", "AWS Backup works with AWS Organizations"],
 [E(WS, "AWS Backup works with AWS Organizations to simplify cross-account monitoring and management")],
 scope="AWS Backup and AWS Organizations", hard=False, bullets=["1.3.S1"]))
f.append(F("backup-guardduty-malware-scanning-of-recovery-points", "capability",
 "AWS Backup integrates with Amazon GuardDuty to scan recovery points automatically for malware, which helps detect potential malware in EC2, EBS and S3 backups.",
 "Which AWS service scans AWS Backup recovery points for malware, and for which backups?",
 ["automated malware scanning of your recovery points", "EC2, EBS, and S3 backups"],
 [E(WS, "AWS Backup integrates with Amazon GuardDuty to provide automated malware scanning of your recovery points. This integration helps you detect potential malware in your EC2, EBS, and S3 backups.")],
 scope="AWS Backup malware scanning", tier0=True, bullets=["2.2.S5"]))
f.append(F("backup-service-must-exist-in-region", "restriction",
 "To use AWS Backup with a supported AWS service in a particular Region, that service must be available in the Region.",
 "Can you use AWS Backup for a service in a Region where the service itself is not available?",
 ["the service must be available in the Region", "in a particular Region"],
 [E(FA, "To use AWS Backup with a supported AWS service in a particular Region, the service must be available in the Region.")],
 scope="per Region", rel="extended", bullets=["4.1.S6"]))
f.append(F("backup-copy-unsupported-without-checkmark", "restriction",
 "If a resource type has no check mark in the cross-Region backup or cross-account backup columns of the feature availability table, copy operations for that resource type are not supported in any scenario, including same-Region, same-account copies to a different vault.",
 "Can a resource type without a cross-Region or cross-account check mark be copied to a different vault in the same Region and account?",
 ["not supported in any scenario", "same-Region and same-account copies to a different vault"],
 [E(FA, "If a resource type does not have a checkmark in the Cross-Region backup or Cross-account backup columns, then copy operations for that resource type are not supported in any scenario, including same-Region and same-account copies to a different vault.")],
 scope="resource types without a cross-Region or cross-account check mark", tier0=True, bullets=["1.3.S5"]))
f.append(F("backup-continuous-copy-becomes-snapshot-no-pitr", "restriction",
 "When a cross-Region or cross-account copy of a continuous backup is made, the copy becomes a snapshot (periodic) backup, and point-in-time restore is not available for the copy.",
 "Can you do a point-in-time restore from a cross-Region or cross-account copy of a continuous backup?",
 ["becomes a snapshot (periodic) backup", "PITR (Point-in-Time Restore) is not available for these copies"],
 [E(FA, "Some resource types have both continuous backup capability and cross-Region and cross-account copy available. When a cross-Region or cross-account copy of a continuous backup is made, the copied recovery point (backup) becomes a snapshot (periodic) backup. PITR (Point-in-Time Restore) is not available for these copies.")],
 scope="copies of continuous backups", tier0=True, bullets=["1.3.S5"]))
dump("facts-behavior-02.json", f)
