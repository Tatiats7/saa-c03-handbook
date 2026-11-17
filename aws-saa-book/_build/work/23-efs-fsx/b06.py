import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

WI = "win/what-is"; HA = "win/high-availability-multiAZ"; CL = "win/supported-fsx-clients"; AD = "win/aws-ad-integration-fsxW"
BK = "win/using-backups"; SC = "win/managing-storage-configuration"; DFS = "win/using-dfs-namespaces"; SQ = "win/sql-server"
F = []
F.append(f("fsx-windows-fully-managed-native-windows-file-servers-smb", "behavior",
  "Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers backed by a fully native Windows file system, and it supports the SMB protocol to access file storage over a network.",
  "What is Amazon FSx for Windows File Server, and which protocol does it use?",
  [(WI, "Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system."),
   (WI, "Amazon FSx has native support for Windows file system features and for the industry-standard Server Message Block (SMB) protocol to access file storage over a network.")],
  ["fully managed Microsoft Windows file servers", "Server Message Block (SMB) protocol"], "Amazon FSx for Windows File Server", "4.1.K4", tier0=True))
F.append(f("fsx-windows-smb-versions-2-0-to-3-1-1", "capability",
  "FSx for Windows File Server is compatible with the SMB protocol versions 2.0 through 3.1.1.",
  "Which SMB versions does FSx for Windows File Server support?",
  [(CL, "FSx for Windows File Server is compatible with the Server Message Block (SMB) protocol versions 2.0 through 3.1.1, giving you the flexibility to connect to your file systems using a wide variety of compute instances and operating systems.")],
  ["SMB) protocol versions 2.0 through 3.1.1", "2.0 through 3.1.1"], "Amazon FSx for Windows File Server", "4.1.K4"))
F.append(f("fsx-windows-clients-windows-and-linux-instances-workspaces-appstream-vmware", "capability",
  "You can access FSx for Windows File Server shares from all Windows versions starting from Windows Server 2008 and Windows 7 and from current versions of Linux, and you can map them on EC2 instances, WorkSpaces instances, AppStream 2.0 instances and VMware Cloud on AWS VMs.",
  "Which clients can access FSx for Windows File Server?",
  [(WI, "You can access your shares from all Windows versions starting from Windows Server 2008 and Windows 7, and also from current versions of Linux. You can map your Amazon FSx file shares on Amazon Elastic Compute Cloud (Amazon EC2) instances, and on WorkSpaces instances, Amazon AppStream 2.0 instances, and VMware Cloud on AWS VMs.")],
  ["current versions of Linux", "VMware Cloud on AWS VMs", "starting from Windows Server 2008"], "Amazon FSx for Windows File Server clients", "4.1.K4", tier0=True))
F.append(f("fsx-windows-supported-compute-ec2-ecs-workspaces", "capability",
  "FSx for Windows File Server is supported for Amazon EC2 instances (Windows, Mac and Amazon Linux 2023), Amazon ECS containers, WorkSpaces instances and Amazon WorkSpaces Applications.",
  "Which AWS compute services are supported with FSx for Windows File Server?",
  [(CL, "Amazon Elastic Compute Cloud (Amazon EC2) instances, including Microsoft Windows, Mac, and Amazon Linux 2023 instances."),
   (CL, "Amazon Elastic Container Service (Amazon ECS) containers.")],
  ["Microsoft Windows, Mac, and Amazon Linux 2023 instances", "Amazon Elastic Container Service (Amazon ECS) containers"], "Amazon FSx for Windows File Server clients", "4.1.K4", rel="extended"))
F.append(f("fsx-windows-other-smb-clients-not-supported-by-aws", "restriction",
  "Other SMB-compatible clients may function with FSx for Windows File Server, but they are not supported by AWS.",
  "Are SMB clients other than the listed operating systems supported?",
  [(CL, "Other SMB-compatible clients may function but are not supported by AWS.")],
  ["may function but are not supported by AWS", "Other SMB-compatible clients"], "Amazon FSx for Windows File Server clients", "4.1.K4", rel="reference"))
F.append(f("fsx-windows-on-premises-direct-connect-or-vpn", "capability",
  "You can access FSx for Windows File Server file shares from on-premises compute instances by using AWS Direct Connect or Site-to-Site VPN.",
  "How do on-premises servers reach an FSx for Windows File Server file system?",
  [(WI, "You can access your file shares from on-premises compute instances using AWS Direct Connect or Site-to-Site VPN.")],
  ["AWS Direct Connect or Site-to-Site VPN", "from on-premises compute instances"], "Amazon FSx for Windows File Server clients", "4.1.K4", tier0=True))
F.append(f("fsx-windows-other-vpc-account-region-via-peering-or-transit-gateway", "capability",
  "You can access an FSx for Windows File Server file system from clients in a different VPC, AWS account or AWS Region by using VPC peering or transit gateways.",
  "How do you reach FSx for Windows File Server from another VPC, account or Region?",
  [(CL, "You can access your FSx for Windows File Server file system from support clients that are located in a different VPC, AWS account, or AWS Region than what is associated with your file system using VPC peering or transit gateways.")],
  ["a different VPC, AWS account, or AWS Region", "VPC peering or transit gateways"], "Amazon FSx for Windows File Server clients", ["4.1.K4"], tier0=True))
F.append(f("fsx-windows-filegateway-closed-to-new-customers", "restriction",
  "Amazon FSx File Gateway is no longer available to new customers, and existing customers can continue to use it normally.",
  "Can new customers use Amazon FSx File Gateway for on-premises access to FSx for Windows File Server?",
  [(CL, "Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally.")],
  ["no longer available to new customers", "continue to use the service normally"], "Amazon FSx File Gateway", "4.1.K4", rel="extended", vol="frequently-changing"))
F.append(f("fsx-windows-dns-name-per-file-system-microsoft-dns", "behavior",
  "FSx for Windows File Server provides a DNS name for every file system, and it registers DNS records only if you use Microsoft DNS as the default DNS; with a third-party DNS you must set up DNS entries manually.",
  "Does FSx for Windows File Server register DNS records for third-party DNS?",
  [(CL, "Amazon FSx only registers DNS records for a file system if you are using Microsoft DNS as the default DNS. If you are using a third-party DNS, you must manually set up DNS entries for your Amazon FSx file systems.")],
  ["only registers DNS records for a file system", "manually set up DNS entries"], "Amazon FSx for Windows File Server", "4.1.K4", rel="reference"))
F.append(f("fsx-windows-dns-aliases-keep-existing-names", "capability",
  "Using DNS aliases, you can move Windows file share data to FSx for Windows File Server and continue to use the existing DNS names to access the data.",
  "How do you keep existing file share names after migrating to FSx for Windows File Server?",
  [("win/dns-aliases", "Using DNS aliases, you can move your Windows file share data to FSx for Windows File Server and continue using the existing DNS names to access data on Amazon FSx.")],
  ["continue using the existing DNS names", "Using DNS aliases"], "Amazon FSx for Windows File Server DNS aliases", "2.2.S7", tier0=True))
F.append(f("fsx-windows-joins-active-directory-for-authentication-and-acls", "behavior",
  "When you create an FSx for Windows File Server file system you join it to your Active Directory domain, which provides user authentication and file- and folder-level access control.",
  "Does FSx for Windows File Server need Active Directory?",
  [(AD, "When you create an FSx for Windows File Server file system, you join it to your Active Directory domain to provide user authentication and file- and folder-level access control.")],
  ["join it to your Active Directory domain", "user authentication and file- and folder-level access control"], "Amazon FSx for Windows File Server", "2.2.S7", tier0=True))
F.append(f("fsx-windows-ad-options-aws-managed-or-self-managed", "capability",
  "You can join an FSx for Windows File Server file system to AWS Managed Microsoft AD or to your existing self-managed Active Directory domain, on-premises or in the cloud.",
  "Which Active Directory options work with FSx for Windows File Server?",
  [("win/fsx-aws-managed-ad", "If your organization is using AWS Managed Microsoft AD to manage identities and devices, we recommend that you integrate your Amazon FSx file system with AWS Managed Microsoft AD."),
   ("win/fsx-aws-managed-ad", "Your organization might manage identities and devices on a self-managed Active Directory domain (on-premises or in the cloud). If so, you can join your Amazon FSx file system directly to your existing, self-managed Active Directory domain.")],
  ["integrate your Amazon FSx file system", "existing, self-managed Active Directory domain"],
  "Amazon FSx for Windows File Server", "2.2.S7", tier0=True))
F.append(f("fsx-windows-ad-connector-simple-ad-not-supported", "restriction",
  "Amazon FSx does not support Active Directory Connector and Simple Active Directory.",
  "Can an FSx for Windows File Server file system join Simple AD or AD Connector?",
  [(AD, "Amazon FSx does not support [Active Directory Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) and [Simple Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html).")],
  ["does not support", "Amazon FSx does not support"], "Amazon FSx for Windows File Server", "2.2.S7"))
F.append(f("fsx-windows-single-az-one-server-one-az-30-minutes-downtime", "behavior",
  "A Single-AZ FSx for Windows file system has one Windows file server and its storage volumes in a single Availability Zone, replicates data automatically against the failure of a single component in most cases, and usually has about 30 minutes of downtime during failure recovery and planned maintenance.",
  "What does a Single-AZ FSx for Windows File Server file system protect against, and how long is the downtime?",
  [(HA, "Single-AZ file systems are composed of a single Windows file server instance and a set of storage volumes within a single Availability Zone (AZ). With Single-AZ file systems, data is automatically replicated to protect it from the failure of a single component in most cases."),
   (HA, "Single-AZ file systems usually experience about 30 minutes of downtime during failure recovery events, and during the planned maintenance window that you configure for your file system.")],
  ["about 30 minutes of downtime", "single Windows file server instance"], "FSx for Windows File Server Single-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-windows-single-az-unrecoverable-restore-from-backup", "restriction",
  "With a Single-AZ FSx for Windows file system, failure may be unrecoverable in rare cases, such as multiple component failures or a non-graceful failure of the single file server, in which case you recover from the most recent backup.",
  "What can you do if a Single-AZ FSx for Windows file system is unrecoverable?",
  [(HA, "With Single-AZ file systems, file system failure may be unrecoverable in rare cases, such as due to multiple component failures or due to a non-graceful failure of the single file server that leaves the file system in an inconsistent state, in which case you can recover your file system from the most recent backup.")],
  ["may be unrecoverable in rare cases", "from the most recent backup"], "FSx for Windows File Server Single-AZ", "2.2.K11", rel="extended"))
F.append(f("fsx-windows-multi-az-standby-two-azs-sync-replication", "behavior",
  "A Multi-AZ FSx for Windows file system is a high-availability cluster of Windows file servers across two Availability Zones (a preferred and a standby AZ) using Windows Server Failover Clustering, and data is replicated synchronously within each AZ and between the two AZs.",
  "How does a Multi-AZ FSx for Windows file system replicate data?",
  [(HA, "Multi-AZ file systems are composed of a high-availability cluster of Windows file servers spread across two AZs (a preferred AZ and a standby AZ), leveraging Windows Server Failover Clustering (WSFC) technology and a set of storage volumes on each of the two AZs. Data is replicated synchronously within each individual AZ and between the two AZs.")],
  ["a preferred AZ and a standby AZ", "replicated synchronously within each individual AZ", "Windows Server Failover Clustering"], "FSx for Windows File Server Multi-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-windows-multi-az-enhanced-durability-availability-auto-failover", "behavior",
  "Compared with Single-AZ, Multi-AZ deployments give enhanced durability by replicating data across AZs, and enhanced availability by failing over automatically to the standby AZ during planned maintenance and unplanned disruption.",
  "What does Multi-AZ add over Single-AZ for FSx for Windows File Server?",
  [(HA, "Relative to Single-AZ deployment, Multi-AZ deployments provide enhanced durability by further replicating data across AZs, and enhanced availability during planned system maintenance and unplanned service disruption by failing over automatically to the standby AZ.")],
  ["enhanced durability by further replicating data across AZs", "failing over automatically to the standby AZ"], "FSx for Windows File Server Multi-AZ", "2.2.K11"))
F.append(f("fsx-windows-multi-az-recommended-production-single-az-dev-test", "behavior",
  "AWS recommends Multi-AZ file systems for most production workloads, and describes Single-AZ as a cost-efficient solution for test and development workloads and for production workloads with replication in the application layer or relaxed availability and RPO needs.",
  "When should you choose Single-AZ or Multi-AZ for FSx for Windows File Server?",
  [(HA, "We recommend using Multi-AZ file systems for most production workloads given the high availability and durability model it provides."),
   (HA, "Single-AZ deployment is designed as a cost-efficient solution for test and development workloads, certain production workloads that have replication built into the application layer and do not require additional storage-level redundancy, and production workloads that have relaxed availability and Recovery Point Objective (RPO) needs.")],
  ["Multi-AZ file systems for most production workloads", "cost-efficient solution for test and development workloads"],
  "FSx for Windows File Server deployment types", "2.2.K11", tier0=True))
F.append(f("fsx-windows-failover-triggers-az-outage-unavailable-maintenance", "behavior",
  "A Multi-AZ FSx for Windows file system fails over automatically from the preferred to the standby file server when an Availability Zone outage occurs, when the preferred file server becomes unavailable, or when it undergoes planned maintenance.",
  "What triggers failover of a Multi-AZ FSx for Windows file system?",
  [(HA, "Multi-AZ file systems automatically fail over from the preferred file server to the standby file server if any of the following conditions occur:"),
   (HA, "An Availability Zone outage occurs."), (HA, "The preferred file server becomes unavailable."), (HA, "The preferred file server undergoes planned maintenance.")],
  ["An Availability Zone outage occurs", "The preferred file server becomes unavailable", "undergoes planned maintenance"],
  "FSx for Windows File Server Multi-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-windows-failover-under-30-seconds-failback-automatic", "sla",
  "A failover of a Multi-AZ FSx for Windows file system typically completes in less than 30 seconds, and failback to the preferred file server is automatic and also takes less than 30 seconds once the preferred file server has recovered.",
  "How long does an FSx for Windows File Server Multi-AZ failover take?",
  [(HA, "A failover typically completes in less than 30 seconds from the detection of the failure on the active file server to the promotion of the standby file server to active status. Failback to the original Multi-AZ configuration also completes in less than 30 seconds, and only occurs once the file server in the preferred subnet is fully recovered.")],
  ["less than 30 seconds", "promotion of the standby file server"], "FSx for Windows File Server Multi-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-windows-failover-transparent-same-dns-name", "behavior",
  "Because the file system's DNS name stays the same, failovers are transparent to Windows applications, which resume file system operations without manual intervention.",
  "Do Windows applications need changes after an FSx for Windows File Server failover?",
  [(HA, "Because the file system's DNS name remains the same, failovers are transparent to Windows applications, which resume file system operations without manual intervention.")],
  ["DNS name remains the same", "transparent to Windows applications"], "FSx for Windows File Server Multi-AZ", "2.2.K11"))
F.append(f("fsx-windows-linux-clients-no-automatic-dns-failover", "restriction",
  "Linux clients do not support automatic DNS-based failover, so they do not connect to the standby file server during a failover; they resume after the file system fails back to the preferred file server.",
  "How do Linux clients behave during a Multi-AZ FSx for Windows failover?",
  [(HA, "Linux clients do not support automatic DNS-based failover. Therefore, they don't automatically connect to the standby file server during a failover. They will automatically resume file system operations after the Multi-AZ file system has failed back to the file server in the preferred subnet.")],
  ["do not support automatic DNS-based failover", "resume file system operations"], "FSx for Windows File Server Multi-AZ", "2.2.K11", rel="extended"))
F.append(f("fsx-windows-failover-io-paused-resync-hours-hdd", "restriction",
  "While a Multi-AZ file system fails over and back, I/O may be paused and CloudWatch metrics may be temporarily unavailable, and synchronizing activity during that time can take up to multiple hours for HDD storage and for write-heavy, IOPS-heavy workloads.",
  "What happens to I/O during failover of an FSx for Windows File Server Multi-AZ file system?",
  [(HA, "During the brief period in which your file system is failing over and failing back, I/O may be paused and Amazon CloudWatch metrics may be temporarily unavailable."),
   (HA, "This process can take up to multiple hours for file systems with HDD storage, and for workloads that are write-heavy and IOPS-heavy.")],
  ["I/O may be paused", "multiple hours for file systems with HDD"], "FSx for Windows File Server Multi-AZ", "2.2.K11", rel="extended"))
F.append(f("fsx-windows-test-failover-by-changing-throughput-capacity", "capability",
  "You can test failover of a Multi-AZ FSx for Windows file system by modifying its throughput capacity.",
  "How do you test failover on an FSx for Windows File Server Multi-AZ file system?",
  [(HA, "You can test failover your Multi-AZ file system by modifying its throughput capacity.")],
  ["modifying its throughput capacity", "test failover"], "FSx for Windows File Server Multi-AZ", "2.2.K11", rel="extended"))
F.append(f("fsx-windows-backups-file-system-consistent-incremental-stored-in-s3", "behavior",
  "FSx for Windows File Server backups are file-system-consistent (using VSS), highly durable and incremental, and Amazon FSx stores them in Amazon S3.",
  "How are FSx for Windows File Server backups made consistent and stored?",
  [(BK, "With Amazon FSx, backups are file-system-consistent, highly durable, and incremental."),
   (BK, "To ensure file system consistency, Amazon FSx uses the Volume Shadow Copy Service (VSS) in Microsoft Windows. To ensure high durability, Amazon FSx stores backups in Amazon Simple Storage Service (Amazon S3).")],
  ["file-system-consistent, highly durable, and incremental", "stores backups in Amazon Simple Storage Service"],
  "FSx for Windows File Server backups", "2.2.K11", tier0=True))
F.append(f("fsx-windows-automatic-daily-backups-default-30-day-console-0-to-90", "default",
  "Amazon FSx takes an automatic daily backup by default; the default retention period is 30 days in the console and differs in the API and CLI, you can set it between 0 and 90 days, and 0 days turns automatic backups off.",
  "What is the default retention of FSx for Windows File Server automatic daily backups?",
  [(BK, "By default, Amazon FSx takes an automatic daily backup of your file system."),
   (BK, "When you create a file system in the Amazon FSx console, the default automatic daily backup retention period is 30 days. The default retention period is different in the Amazon FSx API and CLI. You can set the retention period to be between 0–90 days. Setting the retention period to 0 (zero) days turns off automatic daily backups.")],
  ["automatic daily backup retention period is 30 days", "between 0–90 days"], "FSx for Windows File Server backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("fsx-windows-user-initiated-backups-never-expire", "behavior",
  "User-initiated FSx for Windows File Server backups never expire, are kept even after the file system is deleted, and are deleted only by you.",
  "How long are user-initiated FSx for Windows File Server backups kept?",
  [(BK, "Your user-initiated backups of Amazon FSx file systems never expire, and they are available for as long as you want to keep them. User-initiated backups are retained even after you delete the file system that was backed up.")],
  ["backups of Amazon FSx file systems never expire", "retained even after you delete the file system"], "FSx for Windows File Server backups", "2.2.K11", tier0=True))
F.append(f("fsx-windows-automatic-backups-deleted-with-file-system", "behavior",
  "Automatic daily backups of an FSx for Windows File Server file system are deleted when the file system is deleted.",
  "What happens to automatic daily backups when you delete an FSx for Windows File Server file system?",
  [(BK, "Automatic daily backups are deleted when the file system is deleted.")],
  ["deleted when the file system is deleted", "Automatic daily backups"], "FSx for Windows File Server backups", "2.2.K11", rel="extended"))
F.append(f("fsx-windows-backup-copy-cross-region-and-aws-backup-cross-account", "capability",
  "You can copy FSx for Windows File Server backups within the same account to another Region or within the same Region, and you can use AWS Backup to copy backups across Regions and across accounts.",
  "How can FSx for Windows File Server backups be copied to another Region or account?",
  [(BK, "You can use Amazon FSx to manually copy backups within the same AWS account to another AWS Region (cross-Region copies) or within the same AWS Region (in-Region copies)."),
   (BK, "You can also use AWS Backup to copy backups across AWS Regions and across AWS accounts.")],
  ["another AWS Region (cross-Region copies)", "across AWS Regions and across AWS accounts"], "FSx for Windows File Server backups", "2.2.K11", tier0=True))
F.append(f("fsx-windows-backup-brief-io-pause-seconds", "behavior",
  "During a backup, storage I/O may be suspended briefly, typically for a few seconds, because the VSS service has to flush cached writes to disk.",
  "Does an FSx for Windows File Server backup pause I/O?",
  [(BK, "At some point during the backup process, storage I/O may be suspended briefly, typically for a few seconds.")],
  ["storage I/O may be suspended briefly", "typically for a few seconds"], "FSx for Windows File Server backups", "2.2.K11", rel="reference"))
F.append(f("fsx-windows-shadow-copies-not-enabled-by-default-not-backup-substitute", "default",
  "Shadow copies are not enabled on FSx for Windows File Server by default, you must enable them and set a schedule, and they are not a substitute for backups.",
  "Are shadow copies on by default in FSx for Windows File Server, and do they replace backups?",
  [(SC.replace("managing-storage-configuration", "../x") if False else "win/shadow-copies-fsxW", "Shadow copies are *not* enabled on FSx for Windows File Server by default."),
   ("win/shadow-copies-fsxW", "Shadow copies are not a substitute for backups.")],
  ["enabled on FSx for Windows File Server", "not a substitute for backups"], "FSx for Windows File Server shadow copies", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("fsx-windows-shadow-copy-definition-restore-previous-versions", "behavior",
  "A Microsoft Windows shadow copy is a snapshot of a Windows file system at a point in time, and with shadow copies enabled users can quickly recover deleted or changed files and compare file versions.",
  "What are shadow copies and what can end users do with them?",
  [("win/shadow-copies-fsxW", "A Microsoft Windows *shadow copy* is a snapshot of a Windows file system at a point in time. With shadow copies enabled, users can quickly recover deleted or changed files that are stored on the network, and compare file versions.")],
  ["snapshot of a Windows file system", "quickly recover deleted or changed files"], "FSx for Windows File Server shadow copies", "2.2.K11", tier0=True))
F.append(f("fsx-windows-storage-capacity-increase-only-never-decrease", "restriction",
  "You can only increase the storage capacity of an FSx for Windows File Server file system; you cannot decrease it.",
  "Can you decrease the storage capacity of an FSx for Windows File Server file system?",
  [(SC, "**Increase only** – You can only *increase* the amount of storage capacity for a file system; you can't decrease storage capacity.")],
  ["Increase only", "can't decrease storage capacity"], "FSx for Windows File Server storage capacity", "4.1.S4", tier0=True))
F.append(f("fsx-windows-storage-capacity-increase-minimum-10-percent", "limit",
  "Each storage capacity increase of an FSx for Windows File Server file system must be a minimum of 10 percent of the current storage capacity, up to the maximum allowed value of 65,536 GiB.",
  "By how much must you increase the storage capacity of an FSx for Windows File Server file system?",
  [(SC, "**Minimum increase** – Each storage capacity increase must be a minimum of 10 percent of the file system's current storage capacity, up to the maximum allowed value of 65,536 GiB.")],
  ["minimum of 10 percent", "65,536 GiB"], "per storage capacity increase, FSx for Windows File Server", "4.1.S4", dm="min", tier0=True))
F.append(f("fsx-windows-storage-capacity-6-hours-between-increases", "restriction",
  "You cannot make further storage capacity increases on an FSx for Windows File Server file system until 6 hours after the last increase was requested or until storage optimization has completed, whichever is longer.",
  "How soon can you increase the storage capacity of an FSx for Windows File Server file system again?",
  [(SC, "**Time between increases** – You can't make further storage capacity increases on a file system until 6 hours after the last increase was requested, or until the storage optimization process has completed, whichever time is longer.")],
  ["6 hours after the last increase was requested", "whichever time is longer"], "FSx for Windows File Server storage capacity", "4.1.S4", rel="extended"))
F.append(f("fsx-windows-automatic-storage-increase-solution-cloudformation", "capability",
  "You can automatically increase an FSx for Windows File Server file system's storage capacity when free storage capacity falls below a threshold that you define.",
  "How can storage capacity increases be automated for FSx for Windows File Server?",
  [(SC, "You can automatically increase your file system's storage capacity when the amount of free storage capacity falls below a defined threshold that you specify.")],
  ["automatically increase your file system's storage capacity", "falls below a defined threshold"], "FSx for Windows File Server storage capacity", "4.1.S4", tier0=True))
F.append(f("fsx-windows-keep-20-percent-free-storage", "behavior",
  "AWS recommends keeping at least 20% of free storage capacity on an FSx for Windows File Server file system at all times, because using all of it can hurt performance and might introduce data inconsistencies.",
  "How much free storage capacity should you keep on an FSx for Windows File Server file system?",
  [(SC, "We recommend maintaining at least 20% of free storage capacity at all times on your file system. Using all of your storage capacity can negatively impact your performance and might introduce data inconsistencies.")],
  ["at least 20% of free storage capacity", "introduce data inconsistencies"], "FSx for Windows File Server storage capacity", "4.1.S4", rel="extended"))
F.append(f("fsx-windows-storage-type-hdd-to-ssd-only", "restriction",
  "You can change the storage type of an FSx for Windows File Server file system from HDD to SSD but not from SSD to HDD; to go from SSD to HDD you restore a backup to a new file system that uses HDD storage.",
  "Can you change an FSx for Windows File Server file system from SSD to HDD storage?",
  [(SC, "You can change your file system storage type from HDD to SSD using the AWS Management Console and AWS CLI."),
   (SC, "You can't change your file system storage type from SSD to HDD. If you want to change a file system's storage type from SSD to HDD, you will need to restore a backup of the file system to a new file system that you configure to use HDD storage.")],
  ["from HDD to SSD", "from SSD to HDD"], "FSx for Windows File Server storage type", "4.1.S10", tier0=True))
F.append(f("fsx-windows-storage-hdd-vs-ssd-use-cases", "behavior",
  "FSx for Windows File Server offers SSD and HDD storage; HDD is designed for home directories, user and departmental shares and content management systems, and SSD for the highest-performance, most latency-sensitive workloads such as databases, media processing and data analytics.",
  "Which FSx for Windows File Server storage type suits databases and which suits home directories?",
  [(WI, "HDD storage is designed for a broad spectrum of workloads, including home directories, user and departmental shares, and content management systems. SSD storage is designed for the highest-performance and most latency-sensitive workloads, including databases, media processing workloads, and data analytics applications.")],
  ["home directories, user and departmental shares", "highest-performance and most latency-sensitive workloads"], "FSx for Windows File Server storage types", "4.1.S10", tier0=True))
F.append(f("fsx-windows-dedup-typical-savings-50-60-percent", "behavior",
  "Data deduplication on FSx for Windows File Server typically saves 50 to 60 percent for general-purpose file shares, with 30 to 50 percent for user documents and 70 to 80 percent for software development datasets.",
  "How much storage does data deduplication typically save on general-purpose file shares?",
  [(SC, "Typical savings average 50–60 percent for general-purpose file shares. Within shares, savings range from 30–50 percent for user documents to 70–80 percent for software development datasets.")],
  ["50–60 percent for general-purpose file shares", "30–50 percent for user documents"], "FSx for Windows File Server data deduplication", "4.1.S10", tier0=True))
F.append(f("fsx-windows-dedup-background-transparent-compression-default", "behavior",
  "Data deduplication on FSx for Windows File Server runs as a background process that is transparent to users, and when you enable it data compression is enabled by default.",
  "How does data deduplication run on FSx for Windows File Server?",
  [(SC, "When you enable Data Deduplication, Data compression is enabled by default, compressing the data after deduplication for additional savings."),
   (SC, "Data deduplication runs as a background process that continually and automatically scans and optimizes your file system, and it is transparent to your users and connected clients.")],
  ["Data compression is enabled by default", "runs as a background process"], "FSx for Windows File Server data deduplication", "4.1.S10", rel="extended"))
F.append(f("fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib", "capability",
  "With Microsoft DFS Namespaces you can group file shares on multiple FSx for Windows File Server file systems into one namespace and scale file storage beyond the 64 TiB maximum of a single file system, up to hundreds of petabytes.",
  "How can you scale FSx for Windows File Server storage beyond a single file system?",
  [(DFS, "You can use Microsoft's Distributed File System (DFS) Namespaces to group file shares on multiple FSx for Windows File Server file systems into one common folder structure, or namespace. Using DFS Namespaces, you can scale file storage beyond the maximum storage capacity of single file system (64 TiB) for large file datasets—up to hundreds of petabytes.")],
  ["maximum storage capacity of single file system (64 TiB)", "one common folder structure, or namespace"], "FSx for Windows File Server DFS Namespaces", ["3.1.S2", "4.1.K4"], tier0=True))
F.append(f("fsx-windows-dfs-shards-scale-out-read-write-performance", "capability",
  "By using DFS Namespaces you can scale out read and write performance for I/O-intensive workloads by spreading file data (shards) across multiple FSx file systems under one unified namespace.",
  "How do you scale out FSx for Windows File Server performance beyond one file system?",
  [(DFS, "By using DFS Namespaces, you can scale out performance (both read and write) to serve I/O-intensive workloads by spreading your file data across multiple Amazon FSx file systems.")],
  ["scale out performance (both read and write)", "spreading your file data across multiple"],
  "FSx for Windows File Server DFS Namespaces", "3.1.S2", tier0=True))
F.append(f("fsx-windows-encrypted-at-rest-always-kms-aes-256", "behavior",
  "All Amazon FSx file systems are encrypted at rest with keys managed in AWS KMS, using the AES-256 algorithm, and data is encrypted and decrypted transparently.",
  "Is encryption at rest optional for Amazon FSx file systems?",
  [("win/encryption-at-rest", "All Amazon FSx file systems are encrypted at rest with keys managed using AWS Key Management Service (AWS KMS). Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read."),
   ("win/encryption-at-rest", "Amazon FSx uses an industry-standard AES-256 encryption algorithm to encrypt Amazon FSx data and metadata at rest.")],
  ["encrypted at rest with keys managed", "industry-standard AES-256 encryption algorithm"],
  "Amazon FSx for Windows File Server encryption", "4.1.K4", tier0=True))
F.append(f("fsx-windows-encrypted-in-transit-smb-kerberos-session-keys", "behavior",
  "Data in transit to FSx for Windows File Server is automatically encrypted using SMB Kerberos session keys.",
  "How is data in transit encrypted for FSx for Windows File Server?",
  [(WI, "Data in transit is also automatically encrypted using SMB Kerberos session keys.")],
  ["automatically encrypted using SMB Kerberos session keys", "Data in transit"], "Amazon FSx for Windows File Server encryption", "4.1.K4", tier0=True))
F.append(f("fsx-windows-access-control-acls-security-groups-iam-ad", "behavior",
  "FSx for Windows File Server gives file- and folder-level access control with Windows ACLs, file system-level access control with VPC security groups, and API-level access control with IAM policies, and users are authenticated with Microsoft Active Directory.",
  "How is access to FSx for Windows File Server controlled?",
  [(WI, "Amazon FSx provides access control at the file and folder level with Windows access control lists (ACLs). It provides access control at the file system level using Amazon Virtual Private Cloud (Amazon VPC) security groups. In addition, it provides access control at the API level using AWS Identity and Access Management (IAM) access policies. Users accessing file systems are authenticated with Microsoft Active Directory.")],
  ["Windows access control lists (ACLs)", "Amazon Virtual Private Cloud (Amazon VPC) security groups"],
  "Amazon FSx for Windows File Server", "4.1.K4", tier0=True))
F.append(f("fsx-windows-sql-server-ca-shares-required-on-multi-az", "restriction",
  "You can create continuously available (CA) shares on Single-AZ 2 file systems, but you are required to use CA shares on Multi-AZ file systems for all SQL Server deployments, whether highly available or not.",
  "Which FSx for Windows File Server deployment type should SQL Server use with continuously available shares?",
  [(SQ, "Amazon FSx is optimized to provide shared storage for SQL Server databases by supporting continuously available (CA) file shares."),
   (SQ, "While you can create CA shares on Single-AZ 2 file systems, it is required that you use CA shares on Multi-AZ file systems for all SQL Server deployments, whether HA or not.")],
  ["continuously available (CA) file shares", "use CA shares on Multi-AZ file systems"],
  "FSx for Windows File Server with SQL Server", "2.2.S8", tier0=True))
F.append(f("fsx-windows-sql-server-active-data-files-or-share-witness-ssd", "capability",
  "You can use FSx for Windows File Server as shared storage for high availability SQL Server in two ways, as storage for active data files and as an SMB file share witness, and SSD storage is recommended for SQL Server.",
  "How can FSx for Windows File Server be used in a highly available SQL Server deployment?",
  [(SQ, "You can use FSx for Windows File Server as shared storage for High Availability (HA) Microsoft SQL Server deployments in two ways: as storage for active data files and as an SMB file share witness."),
   (SQ, "SSD storage is recommended for SQL Server.")],
  ["storage for active data files", "SMB file share witness", "SSD storage is recommended"], "FSx for Windows File Server with SQL Server", "2.2.S8", rel="extended"))
F.append(f("fsx-windows-migrate-with-datasync-or-robocopy", "capability",
  "To migrate existing files to FSx for Windows File Server, AWS recommends AWS DataSync, and as an alternative you can use Robocopy.",
  "How do you migrate on-premises Windows file shares to FSx for Windows File Server?",
  [("win/migrate-files-fsx", "To migrate your existing files to FSx for Windows File Server file systems, we recommend using AWS DataSync, an online data transfer service designed to simplify, automate, and accelerate copying large amounts of data to and from AWS storage services."),
   ("win/migrate-files-fsx", "As an alternative solution, you can use Robust File Copy, or Robocopy, which is a command line directory and file replication command set for Microsoft Windows.")],
  ["we recommend using AWS DataSync", "you can use Robust File Copy, or Robocopy"], "FSx for Windows File Server migration", "2.2.S7", tier0=True))
F.append(f("fsx-windows-migrate-use-ssd-then-hdd-via-backup", "behavior",
  "To migrate large amounts of data to FSx for Windows File Server as quickly as possible, use a file system configured with SSD storage, and afterwards you can move the data to HDD storage if that suits your application.",
  "Which storage type speeds up a migration into FSx for Windows File Server?",
  [("win/migrate-files-fsx", "To migrate large amounts of data to FSx for Windows File Server as quickly as possible, use Amazon FSx file systems configured with solid state drive (SSD) storage. After the migration is complete, you can move the data to Amazon FSx file systems using hard disk drive (HDD) storage if that is the best solution for your application.")],
  ["configured with solid state drive (SSD) storage", "as quickly as possible"], "FSx for Windows File Server migration", "2.2.S7", rel="extended"))
emit("facts-behavior-06.json", F)
