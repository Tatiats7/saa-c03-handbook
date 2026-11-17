import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

W = "efs/whatisefs"; P = "efs/performance"; MT = "efs/managing-throughput"; FAQ = "www/efs/faq"; AB = "efs/automatic-backups"
BK = "efs/awsbackup"; R = "efs/efs-replication"; CR = "efs/create-replication"; FO = "efs/replication-fail-over"
F = []
F.append(f("efs-general-purpose-always-recommended-max-io-higher-latency", "behavior",
  "Max I/O performance mode has higher per-operation latencies than General Purpose mode, so AWS recommends always using General Purpose performance mode.",
  "Which EFS performance mode does AWS recommend, and why?",
  [(P, "For faster performance, we recommend always using General Purpose performance mode."),
   (P, "Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.")],
  ["always using General Purpose performance mode", "higher per-operation latencies with Max I/O"], "EFS performance modes", "3.1.S1", tier0=True))
F.append(f("efs-one-zone-always-general-purpose", "restriction",
  "One Zone file systems always use the General Purpose performance mode.",
  "Which performance mode do One Zone EFS file systems use?",
  [(P, "One Zone file systems always use the General Purpose performance mode.")],
  ["always use the General Purpose performance mode", "One Zone file systems"], "One Zone file system", "3.1.S1", tier0=True))
F.append(f("efs-max-io-not-supported-one-zone-or-elastic", "restriction",
  "Max I/O performance mode is a previous generation mode and is not supported for One Zone file systems or for file systems that use Elastic throughput.",
  "Which EFS file systems cannot use the Max I/O performance mode?",
  [(P, "Max I/O mode is not supported for One Zone file systems or file systems that use Elastic throughput.")],
  ["not supported for One Zone file systems", "file systems that use Elastic throughput"], "EFS performance modes", "3.1.S1", tier0=True))
F.append(f("efs-default-modes-general-purpose-and-elastic", "default",
  "For most workloads AWS recommends the default modes, which are the General Purpose performance mode and the Elastic throughput mode.",
  "Which performance and throughput modes are the EFS defaults?",
  [(W, "For most workloads, we recommend using the default modes, which are the General Purpose performance mode and the Elastic throughput modes.")],
  ["we recommend using the default modes", "General Purpose performance mode"],
  "EFS file system", "3.1.S1", dm="default", adj=True, tier0=True))
F.append(f("efs-performance-mode-cannot-change-after-available", "restriction",
  "You cannot change the performance mode after the file system becomes available.",
  "Can you change the performance mode of an existing EFS file system?",
  [("efs/creating-using-create-fs", "You cannot change the performance mode after the file system becomes available.")],
  ["cannot change the performance mode", "after the file system becomes available"], "EFS performance mode", "3.1.S1"))
F.append(f("efs-three-throughput-modes", "behavior",
  "Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting.",
  "What are the three EFS throughput modes?",
  [(P, "Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting.")],
  ["three throughput modes", "Elastic, Provisioned, and Bursting"], "EFS throughput modes", "3.1.S1", tier0=True))
F.append(f("efs-elastic-throughput-default-recommended", "default",
  "Elastic throughput is the default throughput mode in the Amazon EFS console and is recommended for most use cases.",
  "Which EFS throughput mode is the default and recommended?",
  [(MT, "*Elastic throughput* is the default throughput mode in the Amazon EFS console and is recommended for most use cases.")],
  ["default throughput mode in the Amazon EFS console", "recommended for most use cases"], "EFS throughput modes", "3.1.S1", dm="default", adj=True, tier0=True))
F.append(f("efs-elastic-scales-automatically-no-provisioning-pay-per-use", "behavior",
  "With Elastic throughput, EFS scales throughput up or down automatically, so you do not specify or provision throughput; you pay only for the metadata and data read or written, and you do not accrue or consume burst credits.",
  "How does Elastic throughput scale and how is it billed?",
  [(P, "Because throughput performance for file systems with Elastic throughput scales automatically, you don't need to specify or provision the throughput capacity to meet your application needs. You pay only for the amount of metadata and data read or written, and you don't accrue or consume burst credits while using Elastic throughput.")],
  ["scales automatically", "pay only for the amount of metadata", "don't accrue or consume burst credits"],
  "EFS Elastic throughput", "3.1.S1", tier0=True))
F.append(f("efs-elastic-best-for-spiky-low-average-to-peak", "behavior",
  "Elastic throughput is the best throughput mode for spiky or unpredictable workloads that are hard to forecast, or for applications that drive 5% or less of peak throughput on average.",
  "When is EFS Elastic throughput the best choice?",
  [(P, "Elastic throughput is the best throughput mode for spiky or unpredictable workloads with performance requirements that are difficult to forecast, or for applications that drive throughput at 5% or less of the peak throughput on average (the average-to-peak ratio).")],
  ["spiky or unpredictable workloads", "5% or less of the peak throughput"], "EFS Elastic throughput", "3.1.S1", tier0=True))
F.append(f("efs-provisioned-throughput-independent-of-size", "behavior",
  "With Provisioned throughput you specify a level of throughput that the file system can drive, independent of the file system's size or burst credit balance.",
  "What does EFS Provisioned throughput let you set?",
  [(P, "With Provisioned throughput, you specify a level of throughput that the file system can drive independent of the file system's size or burst credit balance.")],
  ["you specify a level of throughput", "independent of the file system's size"], "EFS Provisioned throughput", "3.1.S1", tier0=True))
F.append(f("efs-provisioned-use-when-known-needs-5-percent-or-more", "behavior",
  "Use Provisioned throughput if you know your workload's performance requirements, or if your application drives throughput at 5% or more of the average-to-peak ratio.",
  "When should you use EFS Provisioned throughput?",
  [(P, "Use Provisioned throughput if you know your workload's performance requirements, or if your application drives throughput at 5% or more of the average-to-peak ratio.")],
  ["know your workload's performance requirements", "5% or more of the average-to-peak ratio"], "EFS Provisioned throughput", "3.1.S1"))
F.append(f("efs-provisioned-billed-for-throughput-enabled", "pricing-dimension",
  "For file systems using Provisioned throughput, you are charged for the amount of throughput enabled for the file system.",
  "What are you charged for with EFS Provisioned throughput?",
  [(P, "For file systems using Provisioned throughput, you are charged for the amount of throughput enabled for the file system.")],
  ["charged for the amount of throughput enabled", "Provisioned throughput"], "EFS Provisioned throughput", "3.1.S1", rel="extended"))
F.append(f("efs-bursting-scales-with-storage-size-recommended-for", "behavior",
  "Bursting throughput is recommended for workloads that need throughput that scales with the amount of storage in the file system.",
  "When is EFS Bursting throughput recommended?",
  [(P, "Bursting throughput is recommended for workloads that require throughput that scales with the amount of storage in your file system.")],
  ["throughput that scales with the amount of storage", "Bursting throughput is recommended"], "EFS Bursting throughput", "3.1.S1"))
F.append(f("efs-bursting-credits-accrue-below-base-and-deducted-above", "behavior",
  "With Bursting throughput, burst credits accrue when the file system consumes below its base throughput rate and are deducted when throughput exceeds the base rate.",
  "How do burst credits work in EFS Bursting throughput?",
  [(P, "Burst credits accrue when the file system consumes below its base throughput rate, and are deducted when throughput exceeds the base rate.")],
  ["Burst credits accrue", "deducted when throughput exceeds the base rate"], "EFS Bursting throughput", "3.1.S1", rel="extended"))
F.append(f("efs-bursting-credits-allow-up-to-12-hours-continuous-burst", "behavior",
  "File systems can accumulate enough burst credits to burst for up to 12 hours continuously.",
  "How long can an EFS file system burst on accumulated credits?",
  [(P, "This behavior means that file systems can accumulate enough credits to burst for up to 12 hours continuously.")],
  ["burst for up to 12 hours continuously", "accumulate enough credits"], "EFS Bursting throughput", "3.1.S1", dm="max", rel="extended"))
F.append(f("efs-switch-throughput-mode-no-downtime", "capability",
  "You can change the throughput mode and the provisioned throughput amount after the file system is available, and changing the throughput mode does not cause application downtime.",
  "Can you change the throughput mode of an EFS file system without downtime?",
  [(MT, "You can change the throughput mode and the provisioned throughput amount after the file system is available. Changing throughput mode does not cause application downtime.")],
  ["change the throughput mode", "does not cause application downtime"], "EFS throughput modes", "3.1.S1", tier0=True))
F.append(f("efs-provisioned-24-hour-wait-before-switch-or-decrease", "restriction",
  "After you change a file system to Provisioned throughput or increase the provisioned amount, you must wait at least 24 hours before you can change the throughput mode again or decrease the provisioned amount.",
  "How often can you change the EFS throughput mode or decrease the provisioned amount?",
  [(MT, "However, any time that you change the file system to Provisioned throughput or increase the provisioned throughput amount, you must wait at least 24 hours before you can change the throughput mode again or decrease the provisioned amount.")],
  ["wait at least 24 hours", "change the throughput mode again"], "EFS Provisioned throughput", "3.1.S1", tier0=True))
F.append(f("efs-iops-not-billed-separately", "pricing-dimension",
  "You are not billed separately for IOPS on EFS; IOPS are included in a file system's throughput accounting.",
  "Are IOPS billed separately on Amazon EFS?",
  [(P, "You are not billed separately for IOPS; they are included in a file system's throughput accounting.")],
  ["not billed separately for IOPS", "included in a file system's throughput accounting"], "Amazon EFS", "3.1.S1", rel="extended"))
F.append(f("efs-read-throughput-discounted", "behavior",
  "EFS discounts read throughput so that you can drive higher read throughput than write throughput.",
  "Is read throughput metered the same as write throughput in EFS?",
  [(P, "Read throughput is discounted to allow you to drive higher read throughput than write throughput.")],
  ["Read throughput is discounted", "higher read throughput than write throughput"], "EFS throughput modes", "3.1.S1", rel="extended"))
F.append(f("efs-backup-on-by-default-in-console", "default",
  "When you create an EFS file system in the console, automatic backups are turned on by default.",
  "Are automatic backups on by default when you create an EFS file system in the console?",
  [(AB, "When you create a file system using the Amazon EFS console, automatic backups are turned on by default.")],
  ["automatic backups are turned on by default", "using the Amazon EFS console"], "EFS automatic backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("efs-backup-cli-api-default-only-one-zone", "default",
  "When you create a file system with the CLI or API, automatic backups are enabled by default only for One Zone file systems.",
  "Are automatic backups on by default for a file system created with the CLI or API?",
  [(BK, "File systems that you create using the Amazon EFS console are automatically backed up by AWS Backup by default. When you use the CLI or API to create a file system, automatic backups are enabled by default only for One Zone file systems.")],
  ["enabled by default only for One Zone", "automatically backed up by AWS Backup by default"], "EFS automatic backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("efs-default-backup-plan-daily-35-day-retention", "default",
  "The default EFS backup plan uses the AWS Backup recommended settings, which are daily backups with a 35-day retention period.",
  "What are the schedule and retention of the default EFS backup plan?",
  [(BK, "The default EFS backup plan uses the AWS Backup recommended settings for automatic backups—daily backups with a 35-day retention period.")],
  ["daily backups with a 35-day retention period", "AWS Backup recommended settings"], "EFS default backup plan", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("efs-backup-plan-and-vault-cannot-be-deleted", "restriction",
  "The default EFS backup plan and the default EFS backup vault cannot be deleted.",
  "Can you delete the default EFS backup plan or vault?",
  [(BK, "The default backup plan and backup vault cannot be deleted.")],
  ["backup plan and backup vault cannot be deleted", "cannot be deleted"], "EFS default backup plan", "2.2.K11", rel="extended"))
F.append(f("efs-backup-incremental-and-restore-to-standard", "behavior",
  "AWS Backup backs up all EFS data whatever storage class it is in, makes incremental backups after the first full copy, and restores all files to the Standard storage class.",
  "How does AWS Backup treat storage classes and increments for EFS?",
  [(BK, "All data in an EFS file system is backed up, whatever storage class the data is in."),
   (BK, "When you restore a recovery point, all files are restored to the Standard storage class."),
   (BK, "AWS Backup performs incremental backups of EFS file systems.")],
  ["whatever storage class the data is in", "restored to the Standard storage class", "incremental backups of EFS file systems"],
  "EFS backups with AWS Backup", "2.2.K11"))
F.append(f("efs-backup-restore-new-or-existing-full-or-item-level", "capability",
  "You can restore EFS backup data to either a new or an existing file system, and you can choose a full restore or an item-level restore.",
  "Where can an EFS backup be restored?",
  [(BK, "You can restore file system data to either a new or existing file system. You also can choose whether to perform a full restore or an item-level restore.")],
  ["either a new or existing file system", "full restore or an item-level restore"], "EFS backups with AWS Backup", "2.2.K11", rel="extended"))
F.append(f("efs-backup-modifications-during-backup-may-be-inconsistent", "behavior",
  "You can modify an EFS file system while a backup runs, but inconsistencies such as duplicated, skewed, or excluded data can occur if you make modifications during the backup.",
  "Are EFS backups consistent if the file system changes during the backup?",
  [(BK, "You can access and modify your EFS file systems while your backup is occurring in AWS Backup. However, inconsistencies, such as duplicated, skewed, or excluded data, can occur if you make modifications to your file system while the backup is occurring.")],
  ["duplicated, skewed, or excluded data", "modify your EFS file systems while"],
  "EFS backups with AWS Backup", "2.2.K11", rel="extended"))
F.append(f("efs-backup-onezone-enabled-by-default-faq", "default",
  "EFS Backups are enabled by default for all EFS One Zone file systems.",
  "Are backups enabled by default for One Zone EFS file systems?",
  [(FAQ, "EFS Backups are enabled by default for all EFS One Zone file systems.")],
  ["enabled by default for all EFS One Zone", "EFS Backups"], "One Zone file system", "2.2.K11", dm="default", adj=True))
F.append(f("efs-onezone-not-resilient-to-az-outage", "restriction",
  "EFS One Zone file systems are not resilient to a complete Availability Zone outage; during an outage you lose availability because the data is not replicated to a different Availability Zone.",
  "What happens to a One Zone EFS file system during an Availability Zone outage?",
  [(FAQ, "EFS One Zone file systems are not resilient to a complete AZ outage. During an AZ outage, you will experience a loss of availability, because your file system data is not replicated to a different AZ.")],
  ["not resilient to a complete AZ outage", "loss of availability"], "One Zone file system", "2.2.K11", tier0=True))
F.append(f("efs-regional-designed-to-sustain-az-loss", "behavior",
  "EFS Regional file systems are designed to sustain data if an Availability Zone is lost, and they support concurrent access from mount targets in all Availability Zones of the Region.",
  "Does a Regional EFS file system survive the loss of an Availability Zone?",
  [(FAQ, "EFS Regional file systems are designed to sustain data if an AZ is lost."),
   (FAQ, "EFS Regional file systems support concurrent access from EFS mount targets in all AZs in the Region where they are located.")],
  ["sustain data if an AZ is lost", "concurrent access from EFS mount targets"], "Regional file system", "2.2.K11", tier0=True))
F.append(f("efs-mount-targets-highly-available-static-ip-dns", "behavior",
  "EFS mount targets are designed to be highly available, and their IP addresses and DNS names in each Availability Zone are static even though they are redundant components backed by multiple resources.",
  "Are EFS mount targets highly available, and do their addresses change?",
  [("efs/how-it-works", "Mount targets themselves are designed to be highly available."),
   ("efs/how-it-works", "As you design for high availability and failover to other Availability Zones, keep in mind that while the IP addresses and DNS for your mount targets in each Availability Zone are static, they are redundant components backed by multiple resources.")],
  ["designed to be highly available", "IP addresses and DNS for your mount targets", "are static"], "EFS mount target", "2.2.K11", rel="extended"))
emit("facts-behavior-03.json", F)
