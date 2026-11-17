# adjudicate-23: repairs of disputed facts (one repair each), built from the current fact rows.
# add = extra evidence quotes (source_id, quote[, heading]); repl = {index: new quote}; claim/values replace.
EDITS = {
 "efs-backup-incremental-and-restore-to-standard": dict(
  claim="AWS Backup backs up all data in an EFS file system whatever storage class the data is in, performs incremental backups of EFS file systems, and restores all files to the Standard storage class when you restore a recovery point."),
 "efs-bursting-max-throughput-major-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional and One Zone file systems – Total Bursting throughput per file system for all connected clients in each AWS Region")]),
 "efs-bursting-max-throughput-other-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional and One Zone file systems – Total Bursting throughput per file system for all connected clients in each AWS Region")]),
 "efs-datasync-recommended-for-onpremises-file-data": dict(
  claim="AWS DataSync provides a fast and simple way to securely sync existing file systems into EFS, and it works over any network, including AWS Direct Connect."),
 "efs-datasync-up-to-10-times-faster-than-linux-copy": dict(
  claim="AWS Direct Connect provides a dedicated network connection over which you can mount EFS file systems; once mounted, you can use DataSync to copy data into EFS up to 10 times faster than standard Linux copy tools.",
  add=[("www/efs/faq", "AWS Direct Connect provides a high-bandwidth and lower-latency dedicated network connection over which you can mount your EFS file systems.")]),
 "efs-decision-guide-use-appropriate-service-cost": dict(
  claim="The AWS storage decision guide lists things that can help you reduce cost when using an AWS storage service, among them: use the appropriate storage service for your workload type, and understand your data and how it is being used.",
  add=[("docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "The following can help you reduce cost when using an AWS storage service:")]),
 "efs-elastic-regional-max-throughput-major-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional file systems – Total default Elastic throughput per file system for all connected clients in each AWS Region")]),
 "efs-elastic-regional-max-throughput-other-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional file systems – Total default Elastic throughput per file system for all connected clients in each AWS Region")]),
 "efs-lifecycle-recommended-defaults-quick-create": dict(
  claim="In the Amazon EFS console, Quick create uses recommended settings that include lifecycle policies to transition the file system to EFS Infrequent Access (IA) storage after 30 days, to EFS Archive storage after 90 days, and not to transition to EFS Standard storage.",
  add=[("docs/efs/latest/ug/creating-using-create-fs", "You can use Quick create to quickly create a file system with the following recommended settings.")]),
 "efs-lifecycle-transition-to-ia-valid-values": dict(
  claim="The lifecycle policy setting for the number of days after files were last accessed in the Standard storage class at which to move them to Infrequent Access (IA) storage (TransitionToIA) accepts AFTER_1_DAY, AFTER_7_DAYS, AFTER_14_DAYS, AFTER_30_DAYS, AFTER_60_DAYS, AFTER_90_DAYS, AFTER_180_DAYS, AFTER_270_DAYS and AFTER_365_DAYS.",
  add=[("docs/efs/latest/APIReference/API_LifecyclePolicy", "The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage.")]),
 "efs-limit-nfs-client-throughput-elastic": dict(
  add=[("docs/efs/latest/ug/limits", "The following quotas for NFS clients apply, assuming a Linux NFSv4.1 client:")]),
 "efs-limit-nfs-client-throughput-other": dict(
  add=[("docs/efs/latest/ug/limits", "The following quotas for NFS clients apply, assuming a Linux NFSv4.1 client:"),
       ("docs/efs/latest/ug/limits", "Maximum combined read and write throughput is 1,500 mebibytes per second (MiBps) for file systems using Elastic throughput and mounted using version 2.0 or later of the Amazon EFS client (amazon-efs-utils version) or the Amazon EFS CSI Driver (aws-efs-csi-driver).")]),
 "efs-limit-nfs-open-files-per-instance": dict(
  add=[("docs/efs/latest/ug/limits", "Listing directory contents doesn't count as opening a file.")]),
 "efs-max-io-not-supported-one-zone-or-elastic": dict(
  add=[("docs/efs/latest/ug/performance", "Max I/O mode is a previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies than the General Purpose mode.")]),
 "efs-metric-storagebytes-emitted-every-15-minutes": dict(
  claim="The EFS StorageBytes metric, the size of the file system in bytes including the data stored in the EFS storage classes, is emitted to CloudWatch every 15 minutes.",
  repl={0: "StorageBytes The size of the file system in bytes, including the amount of data stored in the EFS storage classes. This metric is emitted to CloudWatch every 15 minutes."}),
 "efs-metric-storagebytes-total-rounds-small-files": dict(
  claim="In the Total dimension of the EFS storage metric, the metered size of data stored in the file system in all storage classes, files smaller than 128KiB in the EFS Infrequent Access (IA) and EFS Archive storage classes are rounded to 128KiB.",
  repl={0: "Total is the metered size (in bytes) of data stored in the file system, in all storage classes. For EFS Infrequent Access (IA) and EFS Archive storage classes, files smaller than 128KiB are rounded to 128KiB."}),
 "efs-mount-helper-recommended-nfs-alternative": dict(
  add=[("docs/efs/latest/ug/mounting-fs", "The EFS mount helper helps you mount your EFS file systems on EC2 Linux and Mac instances running the supported distributions.")]),
 "efs-one-zone-max-throughput-elastic-provisioned": dict(
  add=[("docs/efs/latest/ug/limits", "One Zone file systems – Total default Elastic and Provisioned throughput per file system for all connected clients in each AWS Region")]),
 "efs-onezone-ecs-eks-lambda-same-az-subnets": dict(
  claim="When you use a One Zone file system with Amazon ECS, Amazon EKS or AWS Lambda, you need to configure the service to use the same Availability Zone as the file system: with Amazon ECS you should choose only subnets in that Availability Zone when launching your task, and with Lambda you configure your function to only launch invocations into subnets in that Availability Zone.",
  add=[("docs/efs/latest/ug/mounting-one-zone", "When you use a One Zone file system with Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, or AWS Lambda, you need to configure the service to use the same Availability Zone that the EFS file system is located in, illustrated as follows, and described in the following sections.")]),
 "efs-provisioned-regional-max-throughput-major-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional file systems – Total default Provisioned throughput per file system for all connected clients in each AWS Region")]),
 "efs-provisioned-regional-max-throughput-other-regions": dict(
  add=[("docs/efs/latest/ug/limits", "Regional file systems – Total default Provisioned throughput per file system for all connected clients in each AWS Region")]),
 "efs-quota-elastic-iops-increase-factor": dict(
  claim="By default, file systems that use Elastic throughput drive a maximum of 90,000 read IOPS for infrequently accessed data, 250,000 read IOPS for frequently accessed data and 50,000 write IOPS; if your workload requires more IOPS, you can request an increase of up to 10 times these numbers.",
  add=[("docs/efs/latest/ug/performance", "By default, file systems that use Elastic throughput drive a maximum of 90,000 read IOPS for infrequently accessed data, 250,000 read IOPS for frequently accessed data, and 50,000 write IOPS.")]),
 "efs-regional-multi-az-continuous-availability": dict(
  add=[("docs/efs/latest/ug/features", "Regional – Regional file systems (recommended) store data redundantly across multiple geographically separated Availability Zones within the same AWS Region.")]),
 "efs-replication-new-destination-regional-or-one-zone-choice": dict(
  add=[("docs/efs/latest/ug/create-replication", "Choose Regional to create a file system that stores data and metadata redundantly across all Availability Zones within the AWS Region.")]),
 "efs-replication-not-point-in-time-consistent": dict(
  claim="EFS replication is not point-in-time consistent: changes are transferred based on the Last synced time for the replication, and changes made to the source file system after the recorded time might not have been replicated yet.",
  add=[("docs/efs/latest/ug/efs-replication", "Instead they're transferred based on the Last synced time for the replication."),
       ("www/efs/faq", "Changes to your source file system after the recorded time might not have be replicated over.")]),
 "efs-sla-monthly-uptime-one-zone-99-9": dict(
  claim="Under the Amazon EFS SLA, for file systems using One Zone storage classes, a Monthly Uptime Percentage less than 99.9% but greater than or equal to 99.0% earns a 10% service credit."),
 "efs-sla-monthly-uptime-standard-99-99": dict(
  claim="Under the Amazon EFS SLA, for file systems using Standard storage classes, a Monthly Uptime Percentage less than 99.99% but greater than or equal to 99.0% earns a 10% service credit."),
 "efs-standard-class-ssd-lowest-latency-new-data-first": dict(
  add=[("docs/efs/latest/ug/features", "EFS Standard – The EFS Standard storage class uses solid state drive (SSD) storage to deliver the lowest levels of latency for frequently accessed files.")]),
 "efs-transfer-family-sftp-ftps-ftp-same-region": dict(
  claim="AWS Transfer Family is a fully managed file transfer service for SFTP, FTPS and FTP; your end users can use their SFTP, FTP or FTPS clients to access data stored in your Amazon EFS file system, and Transfer Family endpoints must be in the same Region as the file system.",
  add=[("www/efs/faq", "Once complete, your end users can use their SFTP, FTP, or FTPS clients to access data stored in your Amazon EFS file system.")]),
 "efs-whatisefs-one-zone-single-az-loss-risk": dict(
  add=[("docs/efs/latest/ug/whatisefs", "One Zone – One Zone file systems store data within a single Availability Zone.")]),
 "fsx-case-phillips66-ontap-capacity-pool-80-percent": dict(
  add=[("www/solutions/case-studies/phillips66-migration-case-study", "This feature of Amazon FSx for NetApp ONTAP offers a more cost-optimized way to store infrequently accessed data.")]),
 "fsx-case-phillips66-snapmirror-no-refactoring": dict(
  claim="The AWS case study says Phillips 66 migrated data center environments to Amazon EC2 and FSx for NetApp ONTAP, relied on NetApp SnapMirror for these migrations to preserve its existing data organization and security controls, and removed the need for code rewriting, rearchitecting or refactoring.",
  add=[("www/solutions/case-studies/phillips66-migration-case-study", "Then, it began to migrate complete data center environments, including back-office applications and production workloads, to Amazon Elastic Compute Cloud (Amazon EC2)—which offers secure and resizable compute capacity for virtually any workload—and Amazon FSx for NetApp ONTAP.")]),
 "fsx-change-fsx-file-gateway-maintenance-2024-10": dict(
  claim="Amazon FSx File Gateway is listed in maintenance with an announcement date of 2024-10-28: it is no longer available to new customers, and existing customers can continue to use the service normally."),
 "fsx-change-ontap-cross-region-backup-copy-2026-08": dict(
  claim="On 2026-08-27 FSx for NetApp ONTAP began to support copying backups within and across AWS Regions and across trusted accounts in your AWS organization. Previously, you could create and restore backups in the same Region and account as your file system."),
 "fsx-change-openzfs-multi-az-shared-vpc-2026-05": dict(
  add=[("www/about-aws/whats-new/2026/05/amazon-fsx-openzfs-multi-az-vpcs", "Posted on: May 13, 2026", "Amazon FSx for OpenZFS now supports creating Multi-AZ file systems in shared VPCs")]),
 "fsx-change-windows-file-server-resource-manager-2025-11": dict(
  add=[("www/about-aws/whats-new/2025/11/amazon-fsx-windows-file-server-resource-manager", "Existing file systems will receive FSRM support during an upcoming maintenance window.")]),
 "fsx-change-windows-ssd-iops-provisioning-independent-2023-08": dict(
  claim="On 2023-08-09 FSx for Windows File Server file systems began to support SSD IOPS provisioning independently of storage capacity."),
 "fsx-compare-cross-region-account-backups": dict(
  claim="On the AWS page comparing FSx file systems, cross-Region and cross-account backups are marked for FSx for Windows File Server and FSx for Lustre, and cross-Region backups are marked for FSx for OpenZFS."),
 "fsx-decision-guide-cache-file-cache-row": dict(
  claim="In the AWS storage decision guide table, the cache storage type is served by Amazon File Cache, a fully managed, scalable, high-speed cache on AWS for processing file data stored in disparate locations, including on-premises NFS file systems, cloud file systems (FSx for OpenZFS, FSx for NetApp ONTAP) and Amazon S3."),
 "fsx-decision-guide-four-file-systems-align-to-popular": dict(
  add=[("docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system."),
       ("docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "Amazon FSx for Lustre allows you to launch and run the high-performance Lustre file system."),
       ("docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "Amazon FSx for OpenZFS a fully managed file storage service that enables you to move data to AWS from on-premises ZFS or other Linux-based file servers."),
       ("docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "Amazon FSx for NetApp ONTAP a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp's popular ONTAP file system.")]),
 "fsx-faq-ontap-tiering-policy-auto-default": dict(
  add=[("www/fsx/netapp-ontap/faqs", "Each volume in your Amazon FSx for NetApp ONTAP file system has a tiering policy associated with it, which determines how the data within that volume is transitioned to and from capacity pool storage.")]),
 "fsx-faq-openzfs-ha-pair-failover-60-seconds": dict(
  claim="With FSx for OpenZFS Multi-AZ (HA) and Single-AZ (HA) file systems, Amazon FSx deploys an HA pair of file servers with automatic failover and failback; file systems automatically fail over and back as needed, typically within 60 seconds, and clients automatically fail over and back with the file system.",
  add=[("www/fsx/openzfs/faqs", "With Multi-AZ (HA) and Single-AZ (HA) file systems, Amazon FSx deploys a high-availability (HA) pair of file servers with automatic failover and failback to ensure high availability.")]),
 "fsx-faq-openzfs-restore-access-within-minutes": dict(
  claim="The FSx for OpenZFS FAQ says that when you restore from a backup by creating a new file system with the restore from backup option, you can access all of your data within minutes while the restore completes in the background.",
  add=[("www/fsx/openzfs/faqs", "You can restore from a backup by creating a new file system with the “restore from backup” option.")]),
 "fsx-faq-windows-smb-protocol": dict(
  claim="Amazon FSx for Windows File Server provides file storage that is accessible from compute instances over the SMB protocol.",
  values=[{"key": "smb", "display": "the SMB protocol"}],
  add=[("docs/fsx/latest/WindowsGuide/what-is", "Amazon FSx is accessible from compute instances with the SMB protocol (supporting versions 2.0 to 3.1.1).")]),
 "fsx-lustre-aws-batch-and-parallelcluster-integration": dict(
  add=[("docs/fsx/latest/LustreGuide/what-is", "It can automatically create FSx for Lustre file systems or use existing file systems during the cluster creation process.")]),
 "fsx-lustre-client-throughput-non-efa": dict(
  claim="The maximum throughput per client for a non EFA-enabled FSx for Lustre file system, with any client network interface, is 100 Gbps; traffic between an individual client instance and an individual FSx for Lustre object storage server is limited to 5 Gbps.",
  add=[("docs/fsx/latest/LustreGuide/performance", "The traffic between an individual client instance and an individual FSx for Lustre object storage server is limited to 5 Gbps.")]),
 "fsx-lustre-lazy-loaded-from-s3-as-needed": dict(
  claim="When FSx for Lustre is an input data source for Amazon SageMaker, SageMaker jobs start as soon as the file system is linked with the S3 bucket, and data is lazy loaded as needed from Amazon S3 for processing jobs.",
  add=[("www/fsx/lustre/faqs", "SageMaker jobs are started as soon as the FSx for Lustre file system is linked with the S3 bucket without needing to download the full machine learning training dataset from S3.")]),
 "fsx-lustre-pricing-metadata-iops-included-ssd-hdd": dict(
  add=[("www/fsx/lustre/pricing", "You can optionally provision a higher level of metadata IOPS, and you pay for the average IOPS provisioned above the default level included with storage capacity, measured in IOPS-months.")]),
 "fsx-lustre-use-scratch-for-short-term-persistent-for-long-term": dict(
  claim="Use scratch FSx for Lustre file systems when you need cost-optimized storage for short-term, processing-heavy workloads, and persistent file systems for longer-term storage and for throughput-focused workloads that run for extended periods or indefinitely and that might be sensitive to disruptions in availability."),
 "fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost": dict(
  add=[("docs/fsx/latest/ONTAPGuide/ARP", "Changes in file extension types, which means that the new extension isn't consistent with the normally used extension type.")]),
 "fsx-ontap-multi-az-outside-vpc-needs-transit-gateway": dict(
  claim="The NFS, SMB and ONTAP management endpoints of FSx for ONTAP Multi-AZ file systems use floating IP addresses; because VPC Peering, Direct Connect and Site-to-Site VPN don't support transitive peering, you are required to use Transit Gateway to access these interfaces from networks outside the file system's VPC.",
  add=[("docs/fsx/latest/ONTAPGuide/supported-fsx-clients", "The NFS, SMB, and ONTAP management endpoints on Amazon FSx for NetApp ONTAP Multi-AZ file systems use floating internet protocol (IP) addresses so that connected clients seamlessly transition between the preferred and standby file servers during a failover event.")]),
 "fsx-ontap-tiering-policy-per-volume-cooling-period": dict(
  add=[("docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap", "Data tiering is the process by which Amazon FSx for NetApp ONTAP automatically moves data between the SSD and the capacity pool storage tiers.")]),
 "fsx-ontap-what-is-ssd-performance-pay-small-fraction": dict(
  claim="AWS says that with FSx for ONTAP you can achieve SSD levels of performance for your workload while paying for SSD storage for only a small fraction of your data; in addition, FSx for ONTAP automatically tiers your data to lower-cost, elastic storage."),
 "fsx-openzfs-record-size-default-other": dict(
  claim="When you create an FSx for OpenZFS volume, the default ZFS record size is 128 KiB for file systems that do not use the Intelligent-Tiering storage class (Intelligent-Tiering file systems default to 1024 KiB).",
  add=[("docs/fsx/latest/OpenZFSGuide/performance", "When you create a volume, the default record size for file systems using the Intelligent-Tiering storage class is 1024 KiB.")]),
 "fsx-openzfs-replication-use-cases-read-replicas-passive-standby-dr": dict(
  add=[("docs/fsx/latest/OpenZFSGuide/on-demand-replication", "Synchronizing or distributing data to your development or test environments.")]),
 "fsx-windows-backup-brief-io-pause-seconds": dict(
  claim="During an FSx for Windows File Server backup, storage I/O may be suspended briefly, typically for a few seconds; because the VSS service needs to flush any cached writes to disk before resuming I/O, the pause may be longer when the workload has many write operations per second.",
  add=[("docs/fsx/latest/WindowsGuide/using-backups", "Because the VSS service needs to flush any cached writes to disk before resuming I/O, the duration of the pause may be longer if your workload has a large amount of write operations per second (`DataWriteOperations`).")]),
 "fsx-windows-backup-copy-cross-region-and-aws-backup-cross-account": dict(
  claim="You can use Amazon FSx to copy FSx for Windows File Server backups within the same account to another Region or within the same Region (cross-Region copies only within the same AWS partition), and you can use AWS Backup to copy backups across Regions and across accounts.",
  extra={"hard": True, "question": "How can you copy FSx for Windows File Server backups across Regions and across accounts, and within what boundary are cross-Region copies allowed?"},
  add=[("docs/fsx/latest/WindowsGuide/using-backups", "You can make cross-Region copies only within the same AWS partition.")]),
 "fsx-windows-dns-name-per-file-system-microsoft-dns": dict(
  claim="Amazon FSx registers DNS records for an FSx for Windows File Server file system only if you are using Microsoft DNS as the default DNS; if you are using a third-party DNS, you must manually set up DNS entries for your file systems."),
 "fsx-windows-failover-io-paused-resync-hours-hdd": dict(
  add=[("docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "For Multi-AZ file systems, any file read and write activity that occurs during failover and failback will need to be synchronized between the primary and secondary file servers.")]),
 "fsx-windows-failover-under-30-seconds-failback-automatic": dict(
  add=[("docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "When the resources in the preferred subnet are available, Amazon FSx automatically fails back to the preferred file server in the preferred subnet.")]),
 "fsx-windows-limit-max-ssd-iops": dict(
  claim="The maximum SSD IOPS of an FSx for Windows File Server file system is 400,000; FSx file systems provide 400,000 IOPS in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo) and Asia Pacific (Singapore), and up to 80,000 IOPS in all AWS Regions where Amazon FSx is available.",
  add=[("docs/fsx/latest/WindowsGuide/performance", "Amazon FSx file systems provide up to 2 GBps and 80,000 IOPS in all AWS Regions where Amazon FSx is available, and 12 GBps of throughput and 400,000 IOPS in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore).")]),
 "fsx-windows-limit-max-throughput-capacity": dict(
  claim="The maximum throughput capacity of an FSx for Windows File Server file system is 12,288 MBps; throughput capacity levels of 4,608 MBps and higher are supported only in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo) and Asia Pacific (Singapore).",
  add=[("docs/fsx/latest/WindowsGuide/performance", "Note that throughput capacity levels of 4,608 MBps and higher are supported only in the following regions: US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore).")]),
 "fsx-windows-linux-clients-no-automatic-dns-failover": dict(
  claim="Linux clients do not support automatic DNS-based failover, so they don't automatically connect to the standby file server during a failover; they automatically resume file system operations after the Multi-AZ file system has failed back to the file server in the preferred subnet."),
 "fsx-windows-multi-az-feature-row-hdd-ca-shares": dict(
  claim="In the feature support table for FSx for Windows File Server, the Multi-AZ deployment type is marked for SSD storage, HDD storage, DFS namespaces, custom DNS names and CA shares, and has no mark for DFS replication; a note on the CA shares mark says you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.",
  add=[("docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "While you can create continously available (CA) shares on Single-AZ 2 file systems, you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.")]),
 "fsx-windows-single-az-2-feature-row-hdd-ca-shares": dict(
  claim="In the feature support table for FSx for Windows File Server, the Single-AZ 2 deployment type is marked for SSD storage, HDD storage, DFS namespaces, custom DNS names and CA shares, and has no mark for DFS replication; a note on the CA shares mark says that while you can create CA shares on Single-AZ 2 file systems, you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.",
  add=[("docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "While you can create continously available (CA) shares on Single-AZ 2 file systems, you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.")]),
 "fsx-windows-pricing-cross-az-access-rate": dict(
  claim="When you access an FSx for Windows File Server file system from the same Region but from an AZ other than its preferred AZ, Multi-AZ file systems created before February 23, 2022 and Single-AZ file systems are charged $0.01/GB in each direction.",
  add=[("www/fsx/windows/pricing", "If you access your data from the same Region, but from an AZ other than your file system’s preferred AZ:")]),
 "fsx-windows-pricing-multi-az-no-cross-az-access-charge": dict(
  claim="When you access an FSx for Windows File Server file system from the same Region but from an AZ other than its preferred AZ, Multi-AZ file systems created on or after February 23, 2022 have no data transfer charges.",
  add=[("www/fsx/windows/pricing", "If you access your data from the same Region, but from an AZ other than your file system’s preferred AZ:")]),
 "fsx-windows-resource-forest-one-way-trust": dict(
  claim="In the resource forest isolation model, you join your FSx for Windows File Server file system to an AWS Managed Microsoft AD setup and then establish a one-way forest trust relationship between that AWS Managed Microsoft AD domain and your existing self-managed Active Directory domain.",
  add=[("docs/fsx/latest/WindowsGuide/fsx-aws-managed-ad", "You join your file system to an AWS Managed Microsoft AD setup.")]),
 "fsx-windows-shadow-copies-not-enabled-by-default-not-backup-substitute": dict(
  claim="Shadow copies are not enabled on FSx for Windows File Server by default; to protect your data with shadow copies you must enable shadow copies and set up a shadow copy schedule, and shadow copies are not a substitute for backups.",
  add=[("docs/fsx/latest/WindowsGuide/shadow-copies-fsxW", "To protect the data on your file system using shadow copies, you must enable shadow copies and set up a shadow copy schedule on your file system.")]),
 "fsx-windows-throughput-4608-regions": dict(
  repl={0: "Note that throughput capacity levels of 4,608 MBps and higher are supported only in the following regions: US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore)."}),
 "fsx-windows-throughput-iops-by-region": dict(
  repl={0: "Amazon FSx file systems provide up to 2 GBps and 80,000 IOPS in all AWS Regions where Amazon FSx is available, and 12 GBps of throughput and 400,000 IOPS in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore)."}),
 "fsx-windows-user-initiated-backups-never-expire": dict(
  claim="User-initiated FSx for Windows File Server backups never expire, are available for as long as you want to keep them, and are retained even after you delete the file system that was backed up."),
 "fsx-windows-what-is-access-other-vpc-account-region-on-premises": dict(
  repl={1: "In addition to accessing file shares that are in the same VPC, AWS account, and AWS Region as the file system, you can also access your shares from compute instances that are in a different Amazon VPC, account, or AWS Region. You do so using VPC peering or transit gateways."}),
 "fsx-ontap-quota-backups-per-account": "ONTAPQ",
 "fsx-ontap-quota-file-systems-per-account": "ONTAPQ",
 "fsx-ontap-quota-ssd-capacity-per-account": "ONTAPQ",
 "fsx-ontap-quota-ssd-iops-per-account": "ONTAPQ",
 "fsx-ontap-quota-throughput-capacity-per-account": "ONTAPQ",
 "fsx-windows-quota-backups-per-account": "WINQ",
 "fsx-windows-quota-file-systems-per-account": "WINQ",
 "fsx-windows-quota-hdd-capacity-per-account": "WINQ",
 "fsx-windows-quota-ssd-capacity-per-account": "WINQ",
 "fsx-windows-quota-throughput-capacity-per-account": "WINQ",
 "fsx-windows-quota-total-ssd-iops-per-account": "WINQ",
}
SHARED = {
 "ONTAPQ": dict(add=[("docs/fsx/latest/ONTAPGuide/limits", "Following are the quotas for Amazon FSx for NetApp ONTAP for each AWS account, per AWS Region, that you can increase.")]),
 "WINQ": dict(add=[("docs/fsx/latest/WindowsGuide/limits", "Following are the quotas for Amazon FSx for Windows File Server for each AWS account, per AWS Region, that you can increase.")]),
}
RETIRE = {
 "efs-change-access-points-1000-per-file-system-2023-01": ("supersede", "efs-change-access-points-10000-per-file-system-2025-02",
   "currency outdated: the 1,000 maximum was raised to 10,000 on 2025-02-10 (document history); the newer change fact carries the current state"),
 "efs-change-elastic-read-throughput-60-gibps-2024-10": ("supersede", "efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04",
   "currency outdated: the 10 GiBps limit for other Regions was raised to 20 GiBps on 2025-04-10 (document history)"),
 "efs-change-elastic-read-iops-90000-infrequent-2024-01": ("reject", None,
   "currency outdated: since 2024-11-26 the 90,000 figure is a default quota that can be raised on request, not the maximum; current state is in efs-quota-elastic-iops-increase-factor"),
 "efs-free-tier-5gb-12-months": ("reject", None,
   "currency outdated: the same pricing page says new AWS customers from 2025-07-15 receive Free Tier credits instead; efs-faq-free-tier-5-gb-standard carries both statements"),
}
