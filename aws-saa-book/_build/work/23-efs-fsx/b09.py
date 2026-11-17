import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

WI = "zfs/what-is-fsx"; AD = "zfs/availability-durability"; SN = "zfs/snapshots-openzfs"; PF = "zfs/performance"; OD = "zfs/on-demand-replication"
IT = "zfs/performance-intelligent-tiering"; BK = "zfs/using-backups"
F = []
F.append(f("fsx-openzfs-fully-managed-move-from-onprem-zfs-linux-file-servers", "behavior",
  "Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data to AWS from on-premises ZFS or other Linux-based file servers.",
  "What is Amazon FSx for OpenZFS built for?",
  [(WI, "Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data to AWS from on-premises ZFS or other Linux-based file servers.")],
  ["fully managed file storage service", "on-premises ZFS or other Linux-based file servers"], "Amazon FSx for OpenZFS", "2.2.S8", tier0=True))
F.append(f("fsx-openzfs-nfs-v3-v4-clients-linux-windows-macos", "capability",
  "Amazon FSx for OpenZFS file systems are accessible from Linux, Windows and macOS compute instances and containers using the NFS protocol (v3, v4.0, v4.1, v4.2).",
  "Which protocol and clients does FSx for OpenZFS support?",
  [(WI, "Amazon FSx for OpenZFS file systems are broadly accessible from Linux, Windows, and macOS compute instances and containers using the industry-standard NFS protocol (v3, v4.0, v4.1, v4.2).")],
  ["NFS protocol (v3, v4.0, v4.1, v4.2)", "Linux, Windows, and macOS compute instances"], "Amazon FSx for OpenZFS", "2.2.S8", tier0=True))
F.append(f("fsx-openzfs-signature-features-compression-snapshots-clones", "behavior",
  "FSx for OpenZFS provides OpenZFS data management capabilities including data compression, near instant point-in-time snapshots and data cloning, designed for use with the Amazon FSx API.",
  "What are the signature data management features of FSx for OpenZFS?",
  [(WI, "Powerful OpenZFS data management capabilities including data compression, near instant point-in-time snapshots, and data cloning, designed for use with the Amazon FSx API.")],
  ["data compression, near instant point-in-time snapshots", "data cloning"], "Amazon FSx for OpenZFS", "2.2.S8", tier0=True))
F.append(f("fsx-openzfs-volumes-thin-provisioning-user-group-quotas", "capability",
  "FSx for OpenZFS supports multiple volumes per file system, thin provisioning, and user and group quotas for cost-efficient shared file systems across multiple users and applications.",
  "Does FSx for OpenZFS support quotas and multiple volumes?",
  [(WI, "Support for multiple volumes per file system, thin provisioning, and user and group quotas for cost-efficient shared file systems across multiple users and applications.")],
  ["multiple volumes per file system", "user and group quotas"], "Amazon FSx for OpenZFS", "2.2.K11", rel="extended"))
F.append(f("fsx-openzfs-three-deployment-types-multi-az-single-az-ha-non-ha", "behavior",
  "FSx for OpenZFS supports three file system deployment types, Multi-AZ (HA), Single-AZ (HA) and Single-AZ (non-HA), each with a different level of availability and durability.",
  "Which deployment types does FSx for OpenZFS offer?",
  [(WI, "FSx for OpenZFS supports three file system deployment types—Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA)—with each one offering a different level of availability and durability:")],
  ["Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA)", "three file system deployment types"], "Amazon FSx for OpenZFS", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-multi-az-ha-copy-in-each-az-failover-60-seconds", "behavior",
  "Multi-AZ (HA) file systems replicate data and support failover across multiple Availability Zones in the same Region, with a separate copy of the data in each Availability Zone, and failover typically completes within 60 seconds.",
  "How does Multi-AZ (HA) FSx for OpenZFS protect data and how long is failover?",
  [(WI, "Multi-AZ (HA) file systems offer high availability and high durability by replicating your data and supporting failover across multiple Availability Zones in the same AWS Region, with a separate copy of your data in each Availability Zone. Failover typically completes within 60 seconds.")],
  ["separate copy of your data", "Failover typically completes within 60 seconds"], "FSx for OpenZFS Multi-AZ (HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-single-az-ha-primary-standby-same-az-60-seconds", "behavior",
  "Single-AZ (HA) file systems deploy a primary and a standby file system within the same Availability Zone to give continuous availability during failover and failback, and failover typically completes within 60 seconds.",
  "How does Single-AZ (HA) FSx for OpenZFS provide availability?",
  [(WI, "Single-AZ (HA) file systems offer high availability by deploying a primary and standby file system within the same Availability Zone to deliver continuous availability in the event of failover and failback. Failover typically completes within 60 seconds.")],
  ["primary and standby file system within", "Failover typically completes within 60 seconds"], "FSx for OpenZFS Single-AZ (HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-single-az-non-ha-self-healing-30-minutes", "behavior",
  "Single-AZ (non-HA) file systems recover by themselves within a single Availability Zone by detecting and addressing component failures automatically, and recovery typically completes within 30 minutes.",
  "How does Single-AZ (non-HA) FSx for OpenZFS recover from a failure?",
  [(WI, "Single-AZ (non-HA) file systems ensure self-healing recovery within a single Availability Zone by automatically detecting and addressing component failures. Recovery typically completes within 30 minutes.")],
  ["self-healing recovery within a single Availability Zone", "Recovery typically completes within 30 minutes"], "FSx for OpenZFS Single-AZ (non-HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-multi-az-sync-replication-within-and-between-azs", "behavior",
  "Relative to Single-AZ file systems, Multi-AZ (HA) file systems give enhanced durability by replicating data synchronously both within each Availability Zone and between the two Availability Zones.",
  "How does Multi-AZ (HA) FSx for OpenZFS replicate data?",
  [(AD, "Relative to Single-AZ (non-HA and HA) file systems, Multi-AZ (HA) file systems provide enhanced durability by replicating data synchronously both within each individual Availability Zone and between the two Availability Zones.")],
  ["replicating data synchronously", "within each individual Availability Zone and between"], "FSx for OpenZFS Multi-AZ (HA)", "2.2.K11"))
F.append(f("fsx-openzfs-multi-az-recommended-business-critical-database", "behavior",
  "Multi-AZ (HA) file systems are recommended for business-critical production workloads and database workloads that need storage that is highly available and durable across Availability Zones in the same Region.",
  "When should you choose Multi-AZ (HA) for FSx for OpenZFS?",
  [(AD, "Multi-AZ (HA) file systems are recommended for business critical production workloads and database workloads that require storage that is highly available and durable across Availability Zones in the same AWS Region.")],
  ["business critical production workloads", "database workloads"], "FSx for OpenZFS Multi-AZ (HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-single-az-ha-recommended-analytics-eda", "behavior",
  "Single-AZ (HA) file systems are recommended as a cost-effective solution for workloads that need high availability but not storage redundancy across Availability Zones, including analytics and EDA workloads.",
  "When should you choose Single-AZ (HA) for FSx for OpenZFS?",
  [(AD, "Single-AZ (HA) file systems are recommended as a cost-effective solution for workloads that need high availability, but don't need storage redundancy across Availability Zones, including analytics, and EDA workloads.")],
  ["cost-effective solution for workloads that need high availability", "analytics, and EDA workloads"], "FSx for OpenZFS Single-AZ (HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-single-az-non-ha-cost-efficient-tolerates-downtime", "behavior",
  "Single-AZ (non-HA) file systems usually experience about 30 minutes of downtime during failure recovery and the planned maintenance window, and suit workloads that can tolerate temporary loss of availability and, in rare cases, the loss of data updates since the most recent backup.",
  "When should you choose Single-AZ (non-HA) for FSx for OpenZFS?",
  [(AD, "Single-AZ (non-HA) file systems usually experience about 30 minutes of downtime during failure recovery events, and during the planned maintenance window that you configure for your file system. Single-AZ (non-HA) file systems are designed as a cost-efficient solution for workloads that can tolerate temporary loss of availability in the event of planned file system maintenance, unplanned service disruption or, in rare cases, the loss of data updates since the most recent backup.")],
  ["about 30 minutes of downtime", "cost-efficient solution for workloads that can tolerate"], "FSx for OpenZFS Single-AZ (non-HA)", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-single-az-failure-may-be-unrecoverable-restore-backup", "restriction",
  "For all Single-AZ file systems, file system failure may be unrecoverable in rare cases, such as storage component failures, and then you recover the file system from the most recent backup.",
  "What can you do if a Single-AZ FSx for OpenZFS file system cannot be recovered?",
  [(AD, "For all Single-AZ file systems, file system failure may be unrecoverable in rare cases, such as storage component failures. In these cases, you can recover your file system from the most recent backup.")],
  ["may be unrecoverable in rare cases", "from the most recent backup"], "FSx for OpenZFS Single-AZ", "2.2.K11", rel="extended"))
F.append(f("fsx-openzfs-failover-triggers", "behavior",
  "Multi-AZ (HA) and Single-AZ (HA) file systems automatically fail over to the standby file server when the preferred file server becomes unavailable, when the throughput capacity is changed, or when it undergoes planned maintenance, and Multi-AZ (HA) file systems also fail over if an Availability Zone disruption occurs.",
  "What triggers failover of an FSx for OpenZFS file system?",
  [(AD, "Multi-AZ (HA) and Single-AZ (HA) file systems automatically fail over from the preferred file server to the standby file server under the following conditions:"),
   (AD, "The preferred file server becomes unavailable."), (AD, "The file system's throughput capacity is changed."), (AD, "The preferred file server undergoes planned maintenance."),
   (AD, "Multi-AZ (HA) file systems will also fail over if an Availability Zone disruption occurs.")],
  ["becomes unavailable", "throughput capacity is changed", "Availability Zone disruption occurs"], "FSx for OpenZFS failover", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-failover-failback-under-60-seconds-io-pause", "sla",
  "An FSx for OpenZFS failover typically takes less than 60 seconds from failure detection to promotion of the standby, the file system automatically fails back to the recovered preferred file server usually in less than 60 seconds, and I/O might be briefly paused during failover and failback.",
  "How long does an FSx for OpenZFS failover take?",
  [(AD, "A failover typically takes less than 60 seconds from the detection of the failure on the active file server to the promotion of the standby file server to active status."),
   (AD, "When the preferred file server is fully recovered and becomes available, Amazon FSx automatically fails back to it, usually in less than 60 seconds."),
   (AD, "During failover and failback, I/O might be briefly paused and Amazon CloudWatch metrics might be temporarily unavailable.")],
  ["less than 60 seconds", "I/O might be briefly paused"], "FSx for OpenZFS failover", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-migrate-between-deployment-types-backup-rsync-replication", "capability",
  "You can migrate between FSx for OpenZFS deployment types by restoring from a backup, by using rsync, or by using on-demand replication.",
  "How do you move an FSx for OpenZFS file system to a different deployment type?",
  [(AD, "You can also migrate between deployment types by restoring from a backup, using **rsync**, or using on-demand replication.")],
  ["restoring from a backup", "using on-demand replication"], "FSx for OpenZFS deployment types", "2.2.K11", rel="extended"))
F.append(f("fsx-openzfs-clients-same-az-as-preferred-file-server", "behavior",
  "For in-AWS applications, AWS recommends launching clients in the same Availability Zone as the preferred file server to minimize latency.",
  "Where should clients run to minimize latency to an FSx for OpenZFS file system?",
  [(AD, "For in-AWS applications, we recommend that you launch your clients in the same Availability Zone as your preferred file server to minimize latency.")],
  ["same Availability Zone as your preferred file server", "to minimize latency"], "FSx for OpenZFS", "2.2.K11", rel="reference"))
F.append(f("fsx-openzfs-snapshot-read-only-image-restore-files", "behavior",
  "A snapshot is a read-only image of an FSx for OpenZFS volume at a point in time, and with snapshots users can view and restore individual folders and files from an earlier snapshot.",
  "What is an FSx for OpenZFS snapshot and what can users do with it?",
  [(SN, "A *snapshot* is a read-only image of an FSx for OpenZFS volume at a point in time."),
   (SN, "With snapshots, your users can easily view and restore individual folders and files from an earlier snapshot.")],
  ["read-only image of an FSx for OpenZFS volume", "restore individual folders and files"], "FSx for OpenZFS snapshots", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot", "behavior",
  "A clone volume is a writable copy initialized with the same data as the snapshot, created almost instantly and initially consuming no additional storage; it keeps a dependency on its source snapshot, so you cannot delete the snapshot while the clone is in use.",
  "What is an FSx for OpenZFS clone volume?",
  [(SN, "A clone volume is a writable copy that is initialized with the same data as the snapshot from which it was created."),
   (SN, "Clone volumes are created almost instantly and initially consume no additional storage capacity."),
   (SN, "However, each clone volume maintains a dependency on its source snapshot, so you cannot delete this source snapshot while the clone volume is in use.")],
  ["writable copy", "created almost instantly", "cannot delete this source snapshot"], "FSx for OpenZFS clones", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-full-copy-volume-independent-slower", "behavior",
  "A full-copy volume is a fully independent writable copy of a snapshot, but because all of the data must be transferred it can take significantly longer to create than a clone volume.",
  "How does a full-copy volume differ from a clone volume in FSx for OpenZFS?",
  [(SN, "A full-copy volume is also initialized with the same data as its source snapshot, but is a fully independent writable copy. However, because a full-copy volume requires transferring all of the data from the source snapshot, it can take a significantly longer time to create than a clone volume.")],
  ["fully independent writable copy", "significantly longer time to create"], "FSx for OpenZFS clones", "2.2.K11", rel="extended"))
F.append(f("fsx-openzfs-compression-zstandard-vs-lz4", "behavior",
  "FSx for OpenZFS volumes support Zstandard compression, which gives very high on-disk compression with higher read throughput and reduced write throughput than LZ4, and LZ4 compression, which gives higher write throughput but lower compression than Zstandard.",
  "Which compression algorithms does FSx for OpenZFS support?",
  [(PF, "*Zstandard compression* delivers very high levels of on-disk data compression, with higher read throughput and reduced write throughput performance than LZ4 compression."),
   (PF, "*LZ4 compression* delivers higher write throughput performance, but achieves lower levels of data compression than Zstandard compression.")],
  ["very high levels of on-disk data compression", "higher write throughput performance"], "FSx for OpenZFS data compression", "4.1.S10", tier0=True))
F.append(f("fsx-openzfs-on-demand-replication-snapshots-across-regions-accounts", "capability",
  "FSx for OpenZFS supports on-demand data replication, which transfers snapshots of data between file systems within and across AWS Regions and accounts, and it is available for all deployment types in Regions where FSx for OpenZFS is available.",
  "How do you replicate FSx for OpenZFS data across Regions or accounts?",
  [(OD, "Amazon FSx for OpenZFS supports on-demand data replication, enabling you to transfer snapshots of data between file systems within and across AWS Regions and accounts."),
   (OD, "On-demand data replication is available for all deployment types in AWS Regions where Amazon FSx for OpenZFS is available.")],
  ["transfer snapshots of data between file systems", "within and across AWS Regions and accounts"], "FSx for OpenZFS replication", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-replication-use-cases-read-replicas-passive-standby-dr", "behavior",
  "On-demand data replication can synchronize data to development or test environments, maintain read replicas for scale-out read performance, and maintain a passive standby file system for disaster recovery.",
  "What are the use cases of FSx for OpenZFS on-demand replication?",
  [(OD, "Establishing and maintaining read replicas to provide scale-out read performance."),
   (OD, "Maintaining a passive standby file system for use in disaster recovery cases.")],
  ["maintaining read replicas", "passive standby file system"], "FSx for OpenZFS replication", "2.2.K11", rel="extended"))
F.append(f("fsx-openzfs-periodic-replication-schedule-incremental", "capability",
  "With ongoing periodic data replication you can schedule an automatic snapshot of a source volume and an incremental replication of that snapshot to a destination volume at a certain interval, for example every 15 minutes.",
  "How do you set up continuing scheduled replication for FSx for OpenZFS?",
  [("zfs/ongoing-periodic-data-replication", "With ongoing periodic data replication, you can set up a schedule that automatically takes a snapshot of a source volume and performs an incremental replication of that snapshot on a destination volume at a certain interval, for example every 15 minutes.")],
  ["automatically takes a snapshot of a source volume", "incremental replication of that snapshot"], "FSx for OpenZFS replication", "2.2.K11", tier0=True))
F.append(f("fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd", "behavior",
  "FSx for OpenZFS has two storage classes: Intelligent-Tiering, where you are billed for the data you store and do not specify a file system size, and SSD, where you specify a file system size and pay for the storage you provision.",
  "Which storage classes does FSx for OpenZFS offer and how is each billed?",
  [(WI, "Two storage classes: Intelligent-Tiering and SSD storage. The Intelligent-Tiering storage class offers fully elastic, cost-effective storage that is suitable for most workloads, as well as an optional SSD read cache that you can provision. With Intelligent-Tiering, you are billed for the data you store, depending on the size of your dataset, and do not need to specify a file system size."),
   (WI, "With SSD storage, you specify a file system size and pay for the amount of storage that you provision.")],
  ["fully elastic, cost-effective storage", "do not need to specify", "pay for the amount of storage"],
  "FSx for OpenZFS storage classes", "4.1.S10", tier0=True))
F.append(f("fsx-openzfs-intelligent-tiering-no-iops-provisioning-pay-per-request", "pricing-dimension",
  "With the Intelligent-Tiering storage class you do not need to provision IOPS; you pay for data access based on usage, in the form of read and write requests.",
  "Do you provision IOPS for the FSx for OpenZFS Intelligent-Tiering storage class?",
  [(IT, "With the Intelligent-Tiering storage class, you do not need to provision IOPS. Instead, you pay for data access based on usage, in the form of read and write requests.")],
  ["do not need to provision IOPS", "pay for data access based on usage"], "FSx for OpenZFS Intelligent-Tiering storage class", "4.1.S10", tier0=True))
F.append(f("fsx-openzfs-intelligent-tiering-latency-tens-of-ms-vs-ssd-cache", "behavior",
  "Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds and per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.",
  "What latency does FSx for OpenZFS Intelligent-Tiering storage have compared with its SSD read cache?",
  [(IT, "Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds as well as per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.")],
  ["roughly tens of milliseconds", "sub-millisecond latency and no per-request costs"], "FSx for OpenZFS Intelligent-Tiering storage class", "4.1.S10", rel="extended"))
F.append(f("fsx-openzfs-intelligent-tiering-read-cache-sizing-modes", "capability",
  "You can configure the SSD read cache of an Intelligent-Tiering file system with one of three sizing modes, Automatic, Custom or None.",
  "How can you size the SSD read cache of an FSx for OpenZFS Intelligent-Tiering file system?",
  [(IT, "You can configure your SSD read cache with one of three sizing mode options: Automatic, Custom, or None.")],
  ["three sizing mode options", "Automatic, Custom, or None"], "FSx for OpenZFS Intelligent-Tiering storage class", "4.1.S10", rel="extended"))
F.append(f("fsx-openzfs-backups-consistent-incremental-stored-in-s3", "behavior",
  "FSx for OpenZFS backups are file-system-consistent, highly durable and incremental, and Amazon FSx stores them in Amazon S3.",
  "How are FSx for OpenZFS backups stored?",
  [(BK, "With FSx for OpenZFS, backups are file-system-consistent, highly durable, and incremental. To ensure high durability, Amazon FSx stores backups in Amazon Simple Storage Service (Amazon S3).")],
  ["file-system-consistent, highly durable, and incremental", "stores backups in Amazon Simple Storage Service"], "FSx for OpenZFS backups", "2.2.K11"))
F.append(f("fsx-openzfs-automatic-daily-backup-default-30-days-console-user-kept-forever", "default",
  "By default Amazon FSx takes an automatic daily backup of an FSx for OpenZFS file system; the console default retention is 30 days, the maximum retention for automatic backups is 90 days, and user-initiated backups are kept forever unless you delete them.",
  "What is the default retention of FSx for OpenZFS automatic daily backups?",
  [(BK, "By default, Amazon FSx takes an automatic daily backup of your file system."),
   (BK, "When you create a file system in the Amazon FSx console, the default automatic daily backup retention period is 30 days."),
   (BK, "While automatic daily backups have a maximum retention period of 90 days, user-initiated backups are kept forever, unless you delete them.")],
  ["default automatic daily backup retention period is 30 days", "maximum retention period of 90 days"], "FSx for OpenZFS backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("fsx-openzfs-encryption-at-rest-kms-backups-in-transit-automatic", "behavior",
  "Amazon FSx automatically encrypts FSx for OpenZFS data at rest in file systems and backups using keys that you manage in AWS KMS.",
  "Is data at rest encrypted in FSx for OpenZFS?",
  [(WI, "It automatically encrypts data at rest in file systems and backups using keys that you manage in AWS Key Management Service (AWS KMS).")],
  ["automatically encrypts data at rest", "file systems and backups"], "Amazon FSx for OpenZFS encryption", "4.1.K4", rel="extended"))
F.append(f("fsx-openzfs-access-control-security-groups-iam-unix-permissions", "behavior",
  "Amazon FSx provides access control for OpenZFS at the file system level with VPC security groups, at the API level with IAM access policies, and at the file and folder level with Unix permissions.",
  "How is access to FSx for OpenZFS controlled?",
  [(WI, "Amazon FSx provides access control at the file system level using Amazon Virtual Private Cloud (Amazon VPC) security groups, and at the API level using AWS Identity and Access Management (IAM) access policies. To provide access control at the file and folder level, Amazon FSx supports Unix permissions.")],
  ["Amazon Virtual Private Cloud (Amazon VPC) security groups", "supports Unix permissions"], "Amazon FSx for OpenZFS", "4.1.K4", tier0=True))
F.append(f("fsx-openzfs-s3-access-points-attach-to-openzfs-volumes", "capability",
  "S3 access points are named network endpoints that attach to either S3 general purpose buckets or FSx for OpenZFS volumes, so applications that work with S3 can use file data on FSx for OpenZFS without changes or moving data out of file storage.",
  "How can S3-based applications use data on FSx for OpenZFS without copying it?",
  [("zfs/s3accesspoints-for-FSx", "You can also use S3 access points to access file data stored on Amazon FSx file systems as if it were in S3, allowing you to use it with applications and services that work with S3 without application changes or moving data out of file storage. These access points are named network endpoints that attach to either S3 general purpose buckets or FSx for OpenZFS volumes.")],
  ["access file data stored on Amazon FSx", "attach to either S3 general purpose buckets"], "Amazon FSx for OpenZFS S3 access points", "4.1.K7", tier0=True))
emit("facts-behavior-09.json", F)
