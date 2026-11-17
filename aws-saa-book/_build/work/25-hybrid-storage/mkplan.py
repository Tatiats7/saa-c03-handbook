"""Write brief.v0.json and mine-plan.json for chapter 25 (plan-25). Usage: python3 -I mkplan.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
TODAY = "2026-10-14"

FG = "docs/filegateway/latest/files3/"
VG = "docs/storagegateway/latest/vgw/"
TG = "docs/storagegateway/latest/tgw/"
FX = "docs/filegateway/latest/filefsxw/"
DS = "docs/datasync/latest/userguide/"
SB = "docs/snowball/latest/developer-guide/"
TF = "docs/transfer/latest/userguide/"
DG = "docs/decision-guides/latest/decision-guides/"
WN = "www/about-aws/whats-new/"
SGF, DSF, SBF, TFF = "www/storagegateway/faqs", "www/datasync/faqs", "www/snowball/faqs", "www/aws-transfer-family/faqs"
DTT = "docs/datatransferterminal/latest/userguide/"


def P(prefix, *names):
    return [prefix + n for n in names]


D = []


def d(n, bullet, kind, lens, service, question, look, tags=None):
    item = {"id": "d25-%03d" % n, "bullet": bullet, "kind": kind, "lens": lens, "service": service,
            "status": "open", "facts": [], "question": question, "look_in": look}
    if tags:
        item["tags"] = tags
    D.append(item)


# ---------------- Storage Gateway: behavior ----------------
d(1, "3.1.K1", "definition", "behavior", "storage-gateway",
  "What is AWS Storage Gateway in one sentence (hybrid cloud storage that gives on-premises applications access to cloud storage)? Which gateway types exist today (Amazon S3 File Gateway, Amazon FSx File Gateway, Tape Gateway, Volume Gateway), and what does each one present to the on-premises application? Quote each guide's own definition.",
  P(FG, "what-is-file-s3") + P(VG, "WhatIsStorageGateway") + P(TG, "WhatIsStorageGateway") + [SGF, "docs/whitepapers/latest/aws-overview/storage-services", "www/storagegateway/features"])
d(2, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Where can a gateway run: which hypervisors (VMware ESXi, Microsoft Hyper-V, Linux KVM, Nutanix AHV), an Amazon EC2 instance, or the Storage Gateway Hardware Appliance? Which gateway types can run on Amazon EC2 and why would you run one there?",
  P(FG, "Requirements", "resource-vm-setup", "hardware-appliance") + P(VG, "Requirements", "hardware-appliance") + [SGF, WN + "2025/12/aws-storage-gateway-nutanix-avh-hypervisor"])
d(3, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "Amazon S3 File Gateway: which file protocols does it present (NFS, SMB)? How is a file share mapped to an S3 bucket (and prefix), and is each file stored as one S3 object in its native format, so that other applications can read the objects directly with the S3 API?",
  P(FG, "what-is-file-s3", "file-gateway-concepts", "GettingStartedCreateFileShare", "create-nfs-file-share", "create-smb-file-share") + [SGF, "www/storagegateway/file/s3"])
d(4, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "S3 File Gateway local cache: what is kept in the cache (recently used data, data waiting to upload), how are writes uploaded to S3 (asynchronously), what is the benefit (low-latency access), and when is cached data evicted?",
  P(FG, "file-gateway-concepts", "decide-local-disks-and-sizes", "Performance") + [SGF])
d(5, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Which S3 storage classes can an S3 File Gateway file share write to directly (S3 Standard, S3 Standard-IA, S3 One Zone-IA, S3 Intelligent-Tiering)? How do objects reach S3 Glacier classes (S3 Lifecycle)? What do the guides warn about minimum storage duration charges when a file share writes to an IA class?",
  P(FG, "storage-classes", "edit-storage-class", "avoid-unanticipated-costs", "CreatingAnNFSFileShare") + [SGF])
d(6, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "What happens when objects are added to the bucket by something other than this gateway (another gateway, an application using the S3 API)? Does the gateway see them automatically, or do you need RefreshCache (manual or automated cache refresh)? Does Storage Gateway coordinate writes from several gateways to the same objects (no object locking across gateways)?",
  P(FG, "FileSharePrexistingObjects", "refresh-cache") + [SGF])
d(7, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Which Amazon S3 features keep working with objects written by an S3 File Gateway (S3 Lifecycle, cross-Region replication, S3 event notifications, S3 Object Lock, versioning)? How does the application learn that a file was uploaded (file upload notification through Amazon EventBridge or CloudWatch Events)?",
  P(FG, "s3-object-lock", "monitoring-file-gateway") + [SGF])
d(8, "3.1.K1", "capability", "behavior", "storage-gateway",
  "How are users authenticated and limited on file shares: SMB with Microsoft Active Directory or guest access, SMB access control lists, NFS client allow lists, and the gateway's SMB security level?",
  P(FG, "enable-ad-settings", "CreatingAnSMBFileShare", "CreatingAnNFSFileShare") + [SGF])
d(9, "3.1.K1", "default", "behavior", "storage-gateway",
  "How does Storage Gateway encrypt data in transit (TLS between gateway and AWS) and at rest (SSE-S3 by default; SSE-KMS; DSSE-KMS for S3 File Gateway; KMS for volumes, snapshots and tapes)? State the default exactly as the guides do.",
  P(FG, "encryption", "encrypt-objects-stored-by-file-gateway-in-amazon-s3") + P(VG, "encryption") + P(TG, "encryption") + [SGF])
d(10, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "Volume Gateway: cached volumes vs stored volumes. Where does the primary copy of the data live in each mode (S3 with a local cache of frequently accessed data, or on premises with asynchronous backup to AWS as point-in-time snapshots)? Which protocol do clients use (iSCSI block)?",
  P(VG, "WhatIsStorageGateway", "StorageGatewayConcepts", "resource-volume-gateway") + [SGF, "www/storagegateway/volume"])
d(11, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "How are Volume Gateway volumes backed up and restored: point-in-time snapshots stored as Amazon EBS snapshots, snapshot schedules, restore to an EBS volume (attach to EC2) or to a new gateway volume, cloning, and AWS Backup integration? Can you see volume data as objects in S3 (no)?",
  P(VG, "backing-up-volumes", "snapshot", "SchedulingSnapshot", "clone-volume", "migrate-data-volume-cached", "migrate-data-volume-stored") + [SGF])
d(12, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Volume Gateway and Tape Gateway security on the iSCSI side: CHAP authentication between initiators and targets. Volume and Tape Gateways also keep an upload buffer and a cache on local disks; what is each disk for?",
  P(VG, "GettingStartedConfigureChap", "decide-local-disks-and-sizes", "PerfUploadBuffer-common", "PerfCache-common") + P(TG, "decide-local-disks-and-sizes"))
d(13, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "Tape Gateway: what does it present (a virtual tape library over iSCSI: tape drives and a media changer), which existing backup applications work with it, where are virtual tapes stored (S3), and what happens when backup software ejects a tape (archive to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive)? How is an archived tape retrieved, and how long can retrieval take?",
  P(TG, "WhatIsStorageGateway", "StorageGatewayConcepts", "archiving-tapes-vtl", "retrieving-archived-tapes-vtl", "moving-tapes-vtl", "resource_vtl-devices", "backup-Veeam") + [SGF, "www/storagegateway/vtl"])
d(14, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Tape Gateway retention controls: custom tape pools with tape retention lock (governance or compliance mode) and write-once-read-many (WORM) virtual tapes. What do they protect against?",
  P(TG, "CreatingCustomTapePool", "managing-virtual-tapes-vtl", "understand-tapes-status") + [SGF])
d(15, "3.1.K1", "restriction", "behavior", "storage-gateway",
  "Amazon FSx File Gateway: what did it do (low-latency on-premises SMB access to Amazon FSx for Windows File Server shares with a local cache), and what is its status now (not available to new customers since October 28, 2024; existing customers continue)? What does AWS suggest instead (access FSx for Windows File Server directly)?",
  P(FX, "what-is-file-fsxw", "DocumentHistory", "attach-fsxw-filesystem") + ["docs/general/latest/gr/maintenance_services", SGF],
  ["reuse fsx-change-fsx-file-gateway-maintenance-2024-10 and fsx-faq-windows-file-gateway-onprem if they fit"])
d(16, "3.1.K1", "behavior", "behavior", "storage-gateway",
  "Availability of a gateway: what does Storage Gateway high availability on VMware (vSphere HA) protect against, and what does the Resilience page say about the gateway as a single on-premises appliance?",
  P(FG, "vmware-ha", "troubleshooting-ha-issues", "disaster-recovery-resiliency") + P(VG, "vmware-ha", "disaster-recovery-resiliency") + [SGF])
d(17, "3.5.S3", "capability", "behavior", "storage-gateway",
  "Networking of a gateway: can it use AWS Direct Connect? Can it be activated and send data through an interface VPC endpoint (AWS PrivateLink) instead of public endpoints? Can it use a proxy? Which gateway types support bandwidth rate limits (throttling) and schedules?",
  P(FG, "using-dx", "gateway-private-link", "create-vpc-endpoint", "MaintenanceUpdateBandwidth-common") + P(VG, "using-dx", "gateway-private-link", "MaintenanceUpdateBandwidth-common") + P(TG, "MaintenanceUpdateBandwidth-common") + [SGF])
d(18, "3.1.K1", "capability", "behavior", "storage-gateway",
  "Which Storage Gateway resources can AWS Backup protect (Volume Gateway volumes), and what does AWS Backup add (central policies, retention)? Reuse the chapter 24 canon where it fits.",
  [SGF, "docs/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data"],
  ["reuse backup-storage-gateway-volume-gateway-supported"])
d(19, "3.5.K6", "behavior", "behavior", "storage-gateway",
  "Performance guidance: what limits S3 File Gateway throughput (cache disks, number of file shares, network), and what do the Performance pages recommend for Volume and Tape Gateways? Quote the guidance; do not invent throughput figures.",
  P(FG, "Performance", "Performance-Throughput", "best-practices") + P(VG, "Performance", "best-practices") + P(TG, "Performance", "best-practices"))

# ---------------- Storage Gateway: numbers ----------------
d(30, "3.5.K6", "number", "numbers", "storage-gateway",
  "S3 File Gateway quotas (table 'Quotas for file shares' of fgw-quotas): maximum file shares per gateway (one bucket per file share; several shares may use one bucket with non-overlapping prefixes), maximum size of an individual file, maximum path length, maximum file name length, and the metadata cache sizes Small/Medium/Large. One fact per row.",
  P(FG, "fgw-quotas"))
d(31, "3.5.K6", "number", "numbers", "storage-gateway",
  "Recommended local disk sizes: S3 File Gateway cache minimum and maximum; Volume and Tape Gateway cache and upload buffer minimum and maximum. Quote the rows with their headers.",
  P(FG, "fgw-quotas") + P(VG, "resource-gateway-limits") + P(TG, "resource-gateway-limits"))
d(32, "3.5.K6", "number", "numbers", "storage-gateway",
  "Volume quotas: maximum size of a cached volume and of a stored volume, maximum number of volumes per gateway, total size of all volumes per gateway (cached and stored), and the rule that a snapshot of a cached volume larger than 16 TiB cannot be restored to an EBS volume.",
  P(VG, "resource-gateway-limits"))
d(33, "3.5.K6", "number", "numbers", "storage-gateway",
  "Tape quotas: minimum and maximum virtual tape size, maximum number of tapes per gateway, total size of tapes per gateway, and the archive limits (no limit).",
  P(TG, "resource-gateway-limits") + [SGF])
d(34, "3.5.K6", "number", "numbers", "storage-gateway",
  "Account-level Storage Gateway quotas in the General Reference (table 'Service quotas' of gr/sg): pick the rows a question could use (for example file shares or tapes per gateway, gateways per account) and quote each with its header.",
  ["docs/general/latest/gr/sg"])
d(35, "3.5.K6", "number", "numbers", "storage-gateway",
  "FAQ numbers: maximum supported local cache per gateway, maximum size of an individual file on S3 File Gateway, how much data a virtual tape holds, how much volume data per gateway. Check each against the quota pages and record any difference.",
  [SGF] + P(FG, "fgw-quotas") + P(VG, "resource-gateway-limits") + P(TG, "resource-gateway-limits"))

# ---------------- Storage Gateway: changes ----------------
d(40, "3.5.K6", "change", "changes", "storage-gateway",
  "Change: maximum virtual tape size went from 5 TiB to 15 TiB (Tape Gateway document history, October 2022). Old value, new value, date, pointer to the current quota fact.",
  P(TG, "DocumentHistory", "resource-gateway-limits"))
d(41, "3.5.K6", "change", "changes", "storage-gateway",
  "Change: S3 File Gateway file shares per gateway went from 10 to 50 (S3 File Gateway document history, January 2023).",
  P(FG, "DocumentHistory", "fgw-quotas"))
d(42, "3.1.K1", "change", "changes", "storage-gateway",
  "Change: Amazon FSx File Gateway closed to new customers on October 28, 2024 (announced September 26, 2024); it is on the Services in Maintenance list. Reuse fsx-change-fsx-file-gateway-maintenance-2024-10 if it fits; otherwise add a storage-gateway change fact.",
  P(FX, "DocumentHistory") + P(VG, "DocumentHistory") + ["docs/general/latest/gr/maintenance_services"])
d(43, "3.1.K1", "change", "changes", "storage-gateway",
  "Change: Tape Gateway can no longer be hosted on Snowball Edge devices (March 2024).",
  P(TG, "DocumentHistory") + P(SB, "doc-history"))
d(44, "3.1.K1", "change", "changes", "storage-gateway",
  "Changes 2024-2025 that touch exam answers: DSSE-KMS for S3 File Gateway (September 2024), SMB security level that enforces 256-bit AES (May 2024), IPv6 (September 2025), VPC endpoint policies (September 2025), Nutanix AHV hypervisor (December 2025). One change fact each, with date.",
  P(FG, "DocumentHistory") + [WN + "2025/09/aws-storage-gateway-ipv6", WN + "2025/09/aws-storage-gateway-vpc-endpoint-policies", WN + "2025/12/aws-storage-gateway-nutanix-avh-hypervisor"])
d(45, "3.1.K1", "change", "changes", "storage-gateway",
  "Recent changes: console copy of file shares across gateways (2026-07-14, examinable but very recent); FIPS endpoints over AWS PrivateLink for Tape and Volume Gateway (2026-08-19) and for S3 File Gateway (2026-09-10): both after 2026-07-15, so 'not examinable yet'.",
  [WN + "2026/07/aws-storage-gateway-console-copy-file-shares", WN + "2026/08/storage-gateway-fips-privatelink", WN + "2026/09/storage-gateway-fips-privatelink-s3"])

# ---------------- DataSync: behavior ----------------
d(50, "3.5.K3", "definition", "behavior", "datasync",
  "What is AWS DataSync in one sentence (an online data movement service)? Which locations can it move data between (NFS, SMB, HDFS, self-managed object storage, other clouds, Amazon S3, Amazon EFS, every Amazon FSx type)? Which use cases does the guide name (migration, archiving cold data, replication for business continuity, recurring transfers for ongoing workflows)?",
  P(DS, "what-is-datasync", "working-with-locations", "transferring-on-premises-storage", "transferring-aws-storage") + [DSF, "www/datasync/features", "docs/whitepapers/latest/aws-overview/migration-services"])
d(51, "3.5.K3", "behavior", "behavior", "datasync",
  "How DataSync works: agent, location, task, task execution. What happens in a task execution (prepare/scan, transfer, verify), and does a later run copy only data that changed (incremental)?",
  P(DS, "how-datasync-transfer-works", "create-task-how-to", "run-task", "task-options") + [DSF])
d(52, "3.5.S3", "capability", "behavior", "datasync",
  "When is a DataSync agent needed and when not (on-premises and other-cloud storage vs transfers between AWS storage services, including cross-Region)? Where can an agent run (VMware ESXi, KVM, Hyper-V, Amazon EC2)? What agent resources does the guide require, including the RAM rule for tasks with more than 20 million files?",
  P(DS, "do-i-need-datasync-agent", "agent-requirements", "deploy-agents") + [DSF])
d(53, "3.5.S3", "capability", "behavior", "datasync",
  "Network paths for DataSync: public service endpoints, VPC service endpoints (AWS PrivateLink), FIPS endpoints; using AWS Direct Connect (public or private virtual interface); required ports. Does DataSync require a VPN (FAQ)?",
  P(DS, "choose-service-endpoint", "networking-datasync", "datasync-network", "direct-connect-architecture", "required-network-interfaces") + [DSF])
d(54, "3.5.K3", "behavior", "behavior", "datasync",
  "Task modes: Basic mode vs Enhanced mode. What does each support (locations, file counts, metrics, parallelism) and which locations does Enhanced mode support today? Mark any location added after 2026-07-15 as not examinable yet.",
  P(DS, "choosing-task-mode") + [DSF])
d(55, "3.5.S3", "capability", "behavior", "datasync",
  "Task options that decide exam answers: transfer only data that changed vs all data, keep or delete files at the destination, overwrite, filters (include/exclude), manifests, schedules (and the shortest schedule interval), and bandwidth limits (can you cap DataSync bandwidth and change it while a task runs?).",
  P(DS, "task-options", "filtering", "transferring-with-manifest", "task-scheduling", "configure-bandwidth") + [DSF])
d(56, "3.5.S3", "behavior", "behavior", "datasync",
  "Data integrity: which verification options exist (verify only transferred data, verify all, none), what DataSync checks during transfer, and what the FAQ says about how DataSync makes sure data is copied correctly.",
  P(DS, "configure-data-verification-options") + [DSF])
d(57, "3.5.K3", "behavior", "behavior", "datasync",
  "Metadata: which file metadata does DataSync preserve (POSIX permissions, timestamps, Windows ACLs/NTFS metadata) and how are files and folders converted to and from S3 objects (metadata stored as object user metadata)?",
  P(DS, "metadata-copied", "configure-metadata", "special-files-copied") + [DSF])
d(58, "3.5.S3", "default", "behavior", "datasync",
  "Encryption: in transit (TLS, version), at rest (the destination's encryption, for example SSE-S3 or SSE-KMS on the bucket), and internetwork traffic privacy.",
  P(DS, "encryption-in-transit", "encrypting-data", "internetwork-traffic-privacy") + [DSF])
d(59, "4.1.S3", "behavior", "behavior", "datasync",
  "DataSync with S3 storage classes: can it write directly to S3 Glacier Instant Retrieval, Flexible Retrieval and Deep Archive? Which S3 request and storage charges does DataSync cause (requests per object, minimum storage duration, incomplete multipart uploads)?",
  P(DS, "create-s3-location", "multipart-upload-policy") + [DSF])
d(60, "3.5.S3", "capability", "behavior", "datasync",
  "Monitoring and audit: CloudWatch metrics and logs, task reports (what they list, why they help an audit), EventBridge events, task execution history.",
  P(DS, "monitoring-overview", "task-reports", "configure-logging", "transfer-performance-counters") + [DSF])
d(61, "3.5.S3", "behavior", "decisions", "datasync",
  "Planning a large migration: how does the guide estimate a migration timeline (data size, network bandwidth, proof of concept), and how do you scale (several tasks, several agents, partitioning by folder)?",
  P(DS, "datasync-large-migration", "gathering-migration-requirements", "datasync-large-migration-timelines", "datasync-large-migration-data-partitioning") + [DSF])
d(62, "3.5.K3", "capability", "behavior", "datasync",
  "Other clouds and other accounts: transfers from Google Cloud Storage, Azure Blob Storage, Azure Files and other object storage (with or without an agent); S3-to-S3 transfers across accounts.",
  P(DS, "transferring-other-cloud-storage", "third-party-cloud-transfer-considerations", "s3-cross-account-transfer") + [DSF, WN + "2025/05/aws-datasync-accelerates-cross-cloud-data-transfers"])
d(63, "3.5.S3", "behavior", "behavior", "datasync",
  "What happens if a task execution is interrupted (network loss, agent restart), and what happens on the next run? Does DataSync affect the performance of the source file system, and can the bandwidth limit protect production traffic?",
  [DSF] + P(DS, "configure-bandwidth", "run-task"))

# ---------------- DataSync: numbers ----------------
d(70, "3.5.K6", "number", "numbers", "datasync",
  "DataSync quotas (table 'DataSync quotas' of datasync-limits): tasks per account and Region; Basic mode files, objects and directories per task execution (on-premises/other cloud to AWS vs between AWS services); Enhanced mode (virtually unlimited); maximum throughput per task with an agent and without one; queued executions per task; concurrent Enhanced mode executions; days of task history; manifest size. One fact per row, quoted with the header.",
  P(DS, "datasync-limits"))
d(71, "3.5.K6", "number", "numbers", "datasync",
  "Storage system limits (table 'Storage system, file, and object limits'): maximum total file path length, file name length, S3 object name length.",
  P(DS, "datasync-limits"))
d(72, "3.5.K6", "number", "numbers", "datasync",
  "Agent resource requirements: vCPU and RAM for the agent VM or EC2 instance, the higher RAM for large file counts, and the minimum EC2 instance size if the page gives one.",
  P(DS, "agent-requirements"))
d(73, "3.5.K6", "number", "numbers", "datasync",
  "Speed claims AWS states: a single DataSync task can fully use a 10 Gbps link (Snowball Edge availability change page); 'up to 10 times faster' than open-source tools (FAQ/features; reuse efs-datasync-up-to-10-times-faster-than-linux-copy if same claim). Record the exact scope of each claim.",
  [SB + "snowball-edge-availability-change", DSF, "www/datasync/features"])

# ---------------- DataSync: changes ----------------
d(80, "3.5.K3", "change", "changes", "datasync",
  "Change: Enhanced mode introduced 2024-10-30 (S3 to S3), extended to other clouds without an agent (2025-05-29) and to on-premises file servers to S3 (2025-12-12); EFS, FSx for Lustre, HDFS, Azure Blob and object storage on 2026-07-28 (not examinable yet; efs-change-datasync-enhanced-mode-efs-lustre-2026-07 exists).",
  P(DS, "doc-history", "choosing-task-mode") + [WN + "2025/05/aws-datasync-accelerates-cross-cloud-data-transfers", WN + "2025/12/aws-datasync-scalability-performance-on-premises-file-transfers", WN + "2026/07/aws-datasync-hdfs-azure-blob-hyper-v", WN + "2026/07/aws-datasync-amazon-efs-fsx-lustre"])
d(81, "4.1.S7", "change", "changes", "datasync",
  "Change: DataSync no longer supports AWS Snowball Edge as a location (November 12, 2024).",
  P(DS, "doc-history", "working-with-locations"))
d(82, "4.1.S7", "change", "changes", "datasync",
  "Change: DataSync Discovery is no longer available (May 20, 2025). Older material may name it as the tool to assess on-premises storage.",
  P(DS, "doc-history", "understanding-your-storage"))
d(83, "3.5.S3", "change", "changes", "datasync",
  "Other changes with dates: manifests (2024-02-07), task reports (2023-08-30), Azure Blob GA (2023-07-25), agentless cross-Region transfers including opt-in Regions (2024-07-24), Kerberos for SMB (2025-01-28), IPv6 (2025-07-16), VPC endpoint policies and FIPS VPC endpoints (2025-09-30), Secrets Manager for all location types (2026-03-20), shared VPCs (2026-09-15/29, not examinable yet), TLS 1.3 (2023-06-28).",
  P(DS, "doc-history") + [WN + "2025/01/aws-datasync-kerberos-authentication", WN + "2025/10/aws-datasync-vpc-endpoint-policies", WN + "2026/03/aws-datasync-secrets-manager", WN + "2026/09/aws-datasync-shared-vpcs"])

# ---------------- Snow Family ----------------
d(90, "3.5.K3", "definition", "behavior", "snow-family",
  "What is AWS Snowball Edge (a physical device AWS ships to you; you copy data onto it and ship it back, and AWS imports the data into S3)? Which job types exist (import into S3, export from S3, local compute and storage)? Quote the guide's 'how it works' steps.",
  P(SB, "whatisedge", "how-it-works", "jobs", "importtype", "exporttype", "computetype") + [SBF, "www/snowball"])
d(91, "4.1.S7", "restriction", "behavior", "snow-family",
  "Current status of Snow Family: Snowball Edge is no longer available to new customers (since November 7, 2025; on the maintenance list from October 7, 2025); AWS no longer offers any Snow Family device to new customers; the product page announces end of support on December 31, 2026 in commercial Regions. Which alternatives does AWS name (DataSync for online transfers, optionally with a Direct Connect hosted connection; AWS Data Transfer Terminal; AWS Partner solutions; AWS Outposts for edge compute)?",
  P(SB, "snowball-edge-availability-change", "doc-history") + ["docs/general/latest/gr/maintenance_services", "www/snowball", SBF, DG + "choosing-aws-storage-service"])
d(92, "3.5.K6", "number", "numbers", "snow-family",
  "Device options and capacity: Snowball Edge Storage Optimized 210 TB and Snowball Edge Compute Optimized. Usable storage, vCPUs, memory and network interfaces from the device tables (one fact per value the exam could use). What does the FAQ say about how much data one job can transfer?",
  P(SB, "device-differences") + [SBF])
d(93, "3.5.S3", "behavior", "behavior", "snow-family",
  "Security of Snowball Edge: encryption with 256-bit keys managed in AWS KMS, keys not stored on the device, tamper-evident enclosure and TPM, data erased from the device after import. Data validation during copy and after import.",
  P(SB, "data-protection", "validation") + [SBF])
d(94, "3.5.S3", "capability", "behavior", "snow-family",
  "How data is copied onto a device: the Amazon S3 interface (S3 adapter, S3 compatible storage), the NFS interface, AWS OpsHub, batching many small files; the file interface is deprecated (March 2024). Best practices for transfer speed.",
  P(SB, "using-adapter", "shared-using-nfs", "batching-small-files", "aws-opshub", "BestPractices", "s3compatible-on-snow", "using-client-commands") + [SBF])
d(95, "3.5.K6", "number", "numbers", "snow-family",
  "Time and logistics: how long a job takes end to end (FAQ), how long you can keep a device, shipping considerations, how AWS suggests calibrating a large transfer and planning a multi-device migration (Large Data Migration Manager).",
  P(SB, "LargeDataMigration", "calibrating-large-transfer", "create-data-migration-plan", "shipping", "return-device", "monitor-status") + [SBF])
d(96, "3.5.K3", "capability", "behavior", "snow-family",
  "Edge computing on Snowball Edge: EC2-compatible instances, clusters, Amazon EKS Anywhere; AWS names AWS Outposts as the alternative for edge compute.",
  P(SB, "using-ec2", "manage-clusters", "ClusterOverview", "ec2-edge-limits", "snowball-edge-availability-change"))
d(97, "4.1.S7", "restriction", "changes", "snow-family",
  "Hypothesis (FRESHNESS): AWS Snowmobile was fully shut down (2024-03-14) and AWS Snowcone and older Snowball Edge models were retired (ordering stopped 2024-11-12, support ended 2025-11-12). Search the saved Snow pages, the FAQ and the document history; if no saved AWS page states it, report not-found (the writer then says only what the canon supports).",
  P(SB, "doc-history", "snowball-edge-availability-change") + [SBF, "www/snowball", "docs/general/latest/gr/maintenance_services"])
d(98, "4.1.S3", "pricing", "numbers", "snow-family",
  "Snowball Edge pricing dimensions (no dollar amounts): service fee per job (includes some days on site), extra daily fee, shipping, data transfer into S3, S3 storage after import; long-term pricing.",
  ["www/snowball/pricing"] + P(SB, "pricing") + [SBF])
d(99, "3.5.K6", "number", "numbers", "snow-family",
  "Snowball Edge quotas page: object size range when importing into S3 (the page still says 5 TB; the S3 chapter owns s3-change-max-object-size-50-tb-2025-12, so record the Snow page's value only with its scope and flag the difference), Region availability rows.",
  P(SB, "limits"))
d(100, "3.5.S3", "definition", "behavior", "snow-family",
  "AWS Data Transfer Terminal (the offline alternative AWS names): what it is (a physical location where you bring your own storage devices and upload to AWS), network connection speed at the site, encryption responsibilities, and how you reserve a slot. File the facts under snow-family with the id prefix snow-family-dtt-* (no separate service key exists).",
  [DTT + "what-is-dtt", DTT + "tech-requirements", DTT + "data-protection", "www/data-transfer-terminal", DG + "choosing-networking-and-content-delivery-service", DG + "choosing-aws-storage-service"])
d(101, "3.5.K6", "change", "changes", "snow-family",
  "Snow changes with dates: Storage Optimized 210 TB device (2023-05-31; was 80 TB), file interface deprecated (2024-03-01), Tape Gateway on Snowball Edge deprecated (2024-03-14), closure to new customers announced 2025-10-07 effective 2025-11-07, end of support 2026-12-31 (product page). Older exam questions assume Snowball, Snowcone and Snowmobile can be ordered.",
  P(SB, "doc-history", "snowball-edge-availability-change") + ["www/snowball", "docs/general/latest/gr/maintenance_services"])

# ---------------- Transfer Family ----------------
d(110, "2.1.K2", "definition", "behavior", "transfer-family",
  "What is AWS Transfer Family in one sentence (fully managed file transfers over SFTP, FTPS, FTP and AS2 into and out of Amazon S3 or Amazon EFS)? Can existing users keep their file transfer clients and scripts unchanged?",
  P(TF, "what-is-aws-transfer-family", "sftp-for-transfer-family") + [TFF, "www/aws-transfer-family/features", "docs/whitepapers/latest/aws-overview/migration-services"])
d(111, "2.1.K2", "restriction", "behavior", "transfer-family",
  "Protocol rules: which protocols an endpoint can enable; FTP only in a VPC and never internet-facing; FTPS needs a server certificate (AWS Certificate Manager); SFTP runs over SSH. SFTP vs FTPS: which to use when (FAQ).",
  P(TF, "sftp-for-transfer-family", "create-server-sftp", "create-server-ftps", "create-server-ftp") + [TFF])
d(112, "2.1.K2", "capability", "behavior", "transfer-family",
  "Endpoint types: public vs VPC (internal, or internet-facing with Elastic IP addresses). How do partners get fixed IP addresses to allow-list, and how do you restrict access by source IP (security groups on a VPC endpoint)? Custom hostname with Amazon Route 53. Network Load Balancer in front of a server.",
  P(TF, "tf-server-endpoint", "create-server-in-vpc", "requirements-dns", "working-with-nlb") + [TFF])
d(113, "2.1.K2", "capability", "behavior", "transfer-family",
  "Identity providers: service managed users (SSH public keys), AWS Directory Service for Microsoft Active Directory, Microsoft Entra ID, custom identity provider through AWS Lambda or Amazon API Gateway. Which protocols support which provider (for example password authentication)?",
  P(TF, "create-user", "service-managed-users", "custom-idp-intro", "custom-lambda-idp", "directory-services-users") + [TFF])
d(114, "2.1.K2", "behavior", "behavior", "transfer-family",
  "How users reach S3: the IAM role the service assumes per user, session policies to share one role among many users, home directories, logical directories that restrict users to their folder (chroot).",
  P(TF, "requirements-roles", "users-policies", "users-policies-session", "logical-dir-mappings", "configure-storage") + [TFF])
d(115, "2.1.K2", "capability", "behavior", "transfer-family",
  "Storage back ends: Amazon S3 and Amazon EFS; Amazon FSx for NetApp ONTAP through S3 access points (2026-01-26). Which operations are supported on S3 (no append, rename limits)?",
  P(TF, "configure-storage", "fsx-s3-access-points") + [TFF, WN + "2026/01/aws-transfer-family-amazon-fsx-netapp-ontap"],
  ["reuse efs-transfer-family-sftp-ftps-ftp-same-region and efs-faq-transfer-family-protocols"])
d(116, "2.1.K2", "capability", "behavior", "transfer-family",
  "Processing after upload: managed workflows (predefined steps copy, tag, delete, decrypt PGP; custom step with Lambda) and Amazon EventBridge events. When to use which (FAQ).",
  P(TF, "transfer-workflows", "nominal-steps-workflow", "eventbridge") + [TFF])
d(117, "2.1.K2", "capability", "behavior", "transfer-family",
  "Outbound and B2B: SFTP connectors (send files to or fetch files from a partner's remote SFTP server, static IPs) and AS2 (business-to-business messages with message disposition notifications).",
  P(TF, "creating-connectors", "reference-architectures", "as2-for-transfer-family") + [TFF])
d(118, "2.1.K2", "capability", "behavior", "transfer-family",
  "Transfer Family web apps: browser-based access to S3 for users who do not use a file transfer client; identity through IAM Identity Center; permissions through S3 Access Grants; web apps in a VPC.",
  P(TF, "web-app", "create-webapp-in-vpc") + [TFF])
d(119, "2.1.K2", "behavior", "behavior", "transfer-family",
  "Security and resilience: security policies (allowed cryptographic algorithms), encryption at rest (S3 server-side encryption, KMS), PGP decryption, AWS WAF through API Gateway for a custom identity provider, Multi-AZ resilience of a server.",
  P(TF, "security-policies", "encryption-at-rest", "key-management", "web-application-firewall", "disaster-recovery-resiliency", "infrastructure-security") + [TFF])
d(120, "2.1.K2", "capability", "behavior", "transfer-family",
  "Monitoring: structured JSON logs in CloudWatch Logs, CloudWatch metrics, CloudTrail.",
  P(TF, "structured-logging", "metrics") + [TFF])
d(121, "3.5.K6", "number", "numbers", "transfer-family",
  "Transfer Family quotas (General Reference table 'Service quotas'): servers per account, VPC_ENDPOINT servers per account, concurrent sessions per server, service managed users per server, SSH keys per user, maximum file size (the row still says 5 Terabytes as 'the maximum size of an individual object in Amazon S3'; record it with its scope and flag that S3 itself changed, see s3-change-max-object-size-50-tb-2025-12), idle connection timeout, SFTP connectors per account. One fact per row with the header.",
  ["docs/general/latest/gr/transfer-service"])
d(122, "3.5.K6", "number", "numbers", "transfer-family",
  "SFTP connector scaling and quotas (scale-and-limits-sftp-connector): concurrent connections, file size, transfer rate; and the 2026-09-30 automatic approval of quota increases up to 1,000 (not examinable yet).",
  P(TF, "scale-and-limits-sftp-connector") + [WN + "2026/09/aws-transfer-family-sftp-connector-quota-1000"])
d(123, "2.1.K2", "change", "changes", "transfer-family",
  "Transfer Family changes with dates: AS2 (2022-07), SFTP connectors (2023-07-25), static IPs for connectors (2024-01-16), EventBridge events (2024-02-08), web apps (2024-12-01), IPv6 endpoints (2025-06-30), SFTP connectors with VPC egress (2025-10-14), web apps in a VPC (2025-11-19), FSx for ONTAP (2026-01-26); not examinable yet: source IP preservation behind an NLB (2026-09-15/17), connector quota auto-approval (2026-09-30), custom log groups for workflows (2026-10-01).",
  P(TF, "doc-history") + [WN + "2025/06/aws-transfer-family-ipv6-endpoints", WN + "2025/10/aws-transfer-family-sftp-connectors-vpc-based-connectivity", WN + "2025/11/transfer-family-web-apps-vpc-endpoints", WN + "2026/01/aws-transfer-family-amazon-fsx-netapp-ontap", WN + "2026/09/transfer-family-sftp-source-ip-nlb", WN + "2026/09/aws-transfer-family-sftp-connector-quota-1000", WN + "2026/10/transfer-family-custom-cloudwatch-log-groups"])

# ---------------- Pricing ----------------
d(130, "4.1.S3", "pricing", "numbers", "storage-gateway",
  "Storage Gateway pricing dimensions (no dollar amounts): storage in S3 or for volumes and tapes, requests, data written to AWS, data transfer out, snapshot storage, retrieval and early deletion of archived tapes. What does the FAQ say about charges for data transferred into AWS?",
  ["www/storagegateway/pricing", SGF] + P(FG, "avoid-unanticipated-costs"))
d(131, "4.1.S3", "pricing", "numbers", "datasync",
  "DataSync pricing dimensions: a charge per gigabyte copied (Basic vs Enhanced mode), any per-task-execution charge, plus the charges of the AWS services involved (S3 requests and storage, data transfer, VPC endpoints). No dollar amounts.",
  ["www/datasync/pricing", DSF] + P(DS, "multipart-upload-policy"))
d(132, "4.1.S3", "pricing", "numbers", "transfer-family",
  "Transfer Family pricing dimensions: per hour for each enabled protocol on an endpoint (also while the server is stopped, per FAQ), per gigabyte uploaded and downloaded, connectors, workflows, web app units. No dollar amounts.",
  ["www/aws-transfer-family/pricing", TFF])

# ---------------- Decisions and comparisons ----------------
d(140, "3.5.K3", "decision", "decisions", "datasync",
  "DataSync vs Storage Gateway: when does AWS say to use each (move or replicate data vs ongoing low-latency on-premises access to cloud data; can they be combined: DataSync for the bulk migration, then File Gateway for ongoing access)? Quote the FAQ answer and the decision guides.",
  [DSF, SGF, DG + "migration-on-aws-how-to-choose", DG + "choosing-aws-storage-service"])
d(141, "3.5.K3", "decision", "decisions", "datasync",
  "DataSync vs Amazon S3 Transfer Acceleration, and DataSync vs AWS Transfer Family: quote the two FAQ answers. Reuse s3-transfer-acceleration-when-to-use where it fits.",
  [DSF])
d(142, "4.1.S7", "decision", "decisions", "datasync",
  "DataSync vs rsync or the S3 command line, and DataSync vs S3 Replication vs S3 Batch Operations for copying between buckets: quote the FAQ answers.",
  [DSF])
d(143, "4.1.S7", "decision", "decisions", "datasync",
  "Online vs offline transfer: what decides it per AWS (migration goals, network bandwidth throughput and reliability, size of data; scheduling transfers in off hours; physical moves when bandwidth is minimal)? Quote the Snowball Edge availability change page, the storage decision guide migration rows and the migration decision guide 'Large data transfer challenges'.",
  [SB + "snowball-edge-availability-change", DG + "choosing-aws-storage-service", DG + "migration-on-aws-how-to-choose"])
d(144, "3.5.S3", "decision", "decisions", "datasync",
  "DataSync with an AWS Direct Connect hosted connection to overcome bandwidth limits for the duration of a migration (Snowball Edge availability change page), and the DataSync guide's Direct Connect architecture examples. Reuse the chapter 12 hosted-connection facts (direct-connect-hosted-connection-provisioned-by-partner, direct-connect-limit-hosted-port-speeds).",
  [SB + "snowball-edge-availability-change"] + P(DS, "direct-connect-architecture", "networking-datasync"))
d(145, "3.1.K1", "decision", "decisions", "storage-gateway",
  "Choosing the gateway type from the stem: file access (NFS/SMB) to objects in S3 -> S3 File Gateway; block storage over iSCSI with data in AWS -> Volume Gateway cached; low-latency access to the whole dataset on premises with backups in AWS -> Volume Gateway stored; existing backup software that writes to tapes -> Tape Gateway. Quote the sentences that support each signal (guides, FAQ, storage decision guide row for Storage Gateway).",
  P(FG, "what-is-file-s3") + P(VG, "WhatIsStorageGateway") + P(TG, "WhatIsStorageGateway") + [SGF, DG + "choosing-aws-storage-service", "www/storagegateway/features"])
d(146, "3.1.K1", "decision", "decisions", "storage-gateway",
  "Why Storage Gateway for applications that cannot change: 'Why should I use AWS Storage Gateway?' and the use cases in the FAQ (move backups to the cloud, replace on-premises file shares with cloud-backed shares, low-latency access to data in AWS). Also the hybrid cloud whitepaper and the migration decision guide's hybrid storage sentence.",
  [SGF, "docs/whitepapers/latest/hybrid-cloud-with-aws/aws-hybrid-cloud-solutions", DG + "migration-on-aws-how-to-choose"])
d(147, "2.1.K2", "decision", "decisions", "transfer-family",
  "Transfer Family vs running your own SFTP server on Amazon EC2: what the service manages for you (no servers to run, scaling, high availability) and why existing partners need no change. Migration decision guide 'File transfer workloads'.",
  [TFF, DG + "migration-on-aws-how-to-choose"] + P(TF, "what-is-aws-transfer-family", "disaster-recovery-resiliency"))
d(148, "4.1.K8", "decision", "decisions", "storage-gateway",
  "One-sentence definitions for the comparison table, from the AWS overview whitepaper (storage services and migration services pages): Storage Gateway, DataSync, Snow Family, Transfer Family. Use them as the 'In one breath' sources.",
  ["docs/whitepapers/latest/aws-overview/storage-services", "docs/whitepapers/latest/aws-overview/migration-services"])
d(149, "4.1.K8", "decision", "decisions", "datasync",
  "Well-Architected: REL09-BP01 (on-premises data backed up with Storage Gateway or DataSync), COST08-BP03 (services that reduce data transfer cost; its Snow Family sentence is old and must not be used as a current recommendation), PERF04-BP05 (Transfer Family to improve throughput). Quote what each says and its scope.",
  ["docs/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data", "docs/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_implement_services", "docs/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_network_protocols_improve_performance"])
d(150, "4.1.S3", "decision", "decisions", "datasync",
  "Lowest-cost transfer: what the guides and FAQ say about cost of DataSync vs building your own scripted transfers (lower TCO, availability change page), about S3 request costs of many small files, and about avoiding unexpected S3 costs with File Gateway (avoid-unanticipated-costs).",
  [SB + "snowball-edge-availability-change", DSF] + P(DS, "multipart-upload-policy") + P(FG, "avoid-unanticipated-costs"))

# ---------------- Callvale ----------------
d(160, "3.5.S3", "decision", "decisions", "datasync",
  "Callvale (month 21): the bank's 80 TB archive is 6.7 million files that must reach S3 in 30 days. Is 6.7 million files within one Basic mode task execution (on-premises to AWS limit), and what does the agent need for more than 20 million files? Which facts let the writer say that one DataSync task can do the job?",
  P(DS, "datasync-limits", "agent-requirements", "choosing-task-mode"), ["callvale"])
d(161, "3.5.S3", "capability", "decisions", "datasync",
  "Callvale: can DataSync run over the bank's Direct Connect connection (private virtual interface with a VPC service endpoint, or public virtual interface)? Quote the DataSync Direct Connect architecture page and the FAQ.",
  P(DS, "direct-connect-architecture", "choose-service-endpoint") + [DSF], ["callvale"])
d(162, "3.5.S3", "capability", "decisions", "datasync",
  "Callvale: the bank allows 500 Mbps. Can a DataSync task be limited to a set bandwidth, and can the limit be changed while the task runs? Is the transfer incremental if the task is run again, and does it verify the data?",
  P(DS, "configure-bandwidth", "task-options", "configure-data-verification-options") + [DSF], ["callvale"])
d(163, "3.5.S3", "behavior", "decisions", "datasync",
  "Callvale: the bank's auditors want proof of what was copied. Do DataSync task reports list every transferred and verified file (chain of custody)?",
  P(DS, "task-reports") + [DSF], ["callvale"])
d(164, "3.1.K1", "decision", "decisions", "storage-gateway",
  "Callvale: the bank's recorder can only write to a file share; an S3 File Gateway runs in the bank's data center and writes into the audio bucket under the prefix ostell/archive/ in S3 Standard-IA. Facts needed: a file share writes files as objects under a prefix, the storage class can be set per file share, the gateway can run on the bank's hypervisor and use Direct Connect, encryption in transit.",
  P(FG, "what-is-file-s3", "GettingStartedCreateFileShare", "storage-classes", "edit-storage-class", "using-dx", "encryption") + [SGF], ["callvale"])
d(165, "2.1.K2", "decision", "decisions", "transfer-family",
  "Callvale: Dorrin Health sends 6,000 recordings (about 70 GB) each night at 01:00 by SFTP to sftp.callvale.example. Facts needed: Transfer Family SFTP endpoint writing to S3, custom hostname with Route 53, service managed users with SSH keys, logical directories per customer, start processing on upload (managed workflow or EventBridge), the cost line (per protocol hour, per GB).",
  P(TF, "requirements-dns", "service-managed-users", "logical-dir-mappings", "transfer-workflows", "eventbridge") + [TFF, "www/aws-transfer-family/pricing"], ["callvale"])
d(166, "4.1.S7", "decision", "decisions", "snow-family",
  "Callvale: Ana asks 'network or ship devices?'. The story weighed an AWS Snow Family device. Which canon facts give the current reason it is not the answer (closed to new customers, end of support date) and what AWS names instead? The data/startup.json note asks the writer to check the device status in the canon before stating why Snow was not chosen.",
  P(SB, "snowball-edge-availability-change") + ["www/snowball", DG + "choosing-aws-storage-service"], ["callvale"])
d(167, "3.5.K6", "behavior", "decisions", "datasync",
  "Callvale: does AWS give a method to estimate transfer time from data size and bandwidth (DataSync large-migration timelines)? The 74-day and 15-day figures are story arithmetic and need no fact; the method sentence lets the writer show the calculation.",
  P(DS, "datasync-large-migration-timelines", "gathering-migration-requirements"), ["callvale"])

# ---------------- Real world ----------------
d(170, "3.5.K3", "case", "decisions", "transfer-family",
  "Case studies: one verbatim sentence each from Myriota (AWS Transfer for SFTP), 3M (AWS DataSync used with Application Migration Service) and Oxford University GLAM (collections stored in S3 through AWS Storage Gateway, cost reduction). Keep only what the page states.",
  ["www/solutions/case-studies/myriota-case-study", "www/solutions/case-studies/3m-accelerating-migration-case-study", "www/solutions/case-studies/glam"])

# ---------------- FAQ quick-fire ----------------
FAQS = [
    (180, "3.1.K1", "storage-gateway", SGF, "Storage Gateway FAQ 'Why should I use AWS Storage Gateway?' and 'What use cases does AWS Storage Gateway support?'"),
    (181, "3.1.K1", "storage-gateway", SGF, "Storage Gateway FAQ 'Can I directly access objects stored in S3 by using Amazon S3 File Gateway?' and 'What if my bucket already contains objects?'"),
    (182, "3.1.K1", "storage-gateway", SGF, "Storage Gateway FAQ 'When I look in Amazon S3 why can't I see my volume data?'"),
    (183, "3.1.K1", "storage-gateway", SGF, "Storage Gateway FAQ 'How do I use Tape Gateway with S3 Glacier Deep Archive storage class?' and 'Does Tape Gateway support Write Once Read Many (WORM) capability?'"),
    (184, "3.5.S3", "storage-gateway", SGF, "Storage Gateway FAQ 'Can I use AWS Storage Gateway with AWS Direct Connect?' and 'Can I deploy a Storage Gateway on my private non-routable network? Does Storage Gateway support AWS PrivateLink?'"),
    (185, "4.1.S3", "storage-gateway", SGF, "Storage Gateway FAQ 'When using File Gateway, will I incur S3 request charges?' and 'How will I be charged for network data transfer to and from AWS when using AWS Storage Gateway?'"),
    (186, "3.5.K3", "datasync", DSF, "DataSync FAQ 'When do I use AWS DataSync and when do I use AWS Storage Gateway?'"),
    (187, "3.5.K3", "datasync", DSF, "DataSync FAQ 'When do I use AWS DataSync, and when do I use Amazon S3 Transfer Acceleration?' and 'When do I use AWS DataSync and when do I use AWS Transfer Family?'"),
    (188, "3.5.S3", "datasync", DSF, "DataSync FAQ 'What happens if an AWS DataSync task is interrupted?' and 'Can I control the amount of network bandwidth that an AWS DataSync task uses?'"),
    (189, "3.5.S3", "datasync", DSF, "DataSync FAQ 'Does AWS DataSync require setting up a VPN to connect to my destination storage?' and 'Can I use AWS DataSync with AWS Direct Connect?'"),
    (190, "4.1.S7", "datasync", DSF, "DataSync FAQ 'How is AWS DataSync different from using command line tools such as rsync or the Amazon S3 command line interface?'"),
    (191, "2.1.K2", "transfer-family", TFF, "Transfer Family FAQ 'Can my users continue to use their existing file transfer clients and applications?' and 'Can I use my corporate domain name (sftp.mycompanyname.com) to access my endpoint?'"),
    (192, "2.1.K2", "transfer-family", TFF, "Transfer Family FAQ 'Can I use FTP with an internet facing endpoint?' and 'Can my end users use fixed IP addresses to allowlist access to my server's endpoint in their firewalls?'"),
    (193, "4.1.S3", "transfer-family", TFF, "Transfer Family FAQ 'I have stopped my server. Will I be billed while it is stopped?' and 'How am I billed for use of the service?'"),
    (194, "2.1.K2", "transfer-family", TFF, "Transfer Family FAQ 'What identity provider options are supported by the service?' and 'Are anonymous users supported?'"),
    (195, "4.1.S7", "snow-family", SBF, "Snowball FAQ 'Notice' item (availability) and 'How long does it take to transfer my data?'"),
]
for n, b, svc, src, q in FAQS:
    d(n, b, "faq", "faq", svc, "Verbatim FAQ answer for the quick-fire section: " + q + ". Record the question text exactly as the FAQ prints it.", [src])

ITEMS = {x["id"]: x for x in D}
assert len(ITEMS) == len(D)

# ---------------- brief.v0.json ----------------
sources = json.loads((HERE / "sources.json").read_text())
UNUSABLE = {
    "docs/wellarchitected/latest/performance-efficiency-pillar/perf_data_access_patterns_select_storage": "fetched with status 200 but the snapshot text is empty (an HTML stub; the page has no .md twin). Not a registry source; replaced by perf_networking_choose_network_protocols_improve_performance (PERF04-BP05).",
    "docs/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized": "fetched with status 200 but the snapshot text is empty (HTML stub). Not a registry source; replaced by cost_data_transfer_implement_services (COST08-BP03).",
    "www/solutions/case-studies/goldman-sachs-transfer-family-case-study": "fetched with status 200 but the page redirects to the generic case-study directory (title 'Customer Success Stories'); not usable as evidence. Use myriota-case-study for Transfer Family.",
    "www/solutions/case-studies/emirates-case-study": "redirects to the generic case-study directory; not usable.",
    "www/solutions/case-studies/ryanair-video-case-study": "redirects to the generic case-study directory; not usable. Use glam for Storage Gateway.",
    "www/solutions/case-studies/paige-case-study": "redirects to the generic case-study directory; not usable.",
    "www/solutions/case-studies/jps-case-study": "redirects to the generic case-study directory; not usable.",
}
URLS = {
    "docs/wellarchitected/latest/performance-efficiency-pillar/perf_data_access_patterns_select_storage": "https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_access_patterns_select_storage.html",
    "docs/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized": "https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized.html",
    "www/solutions/case-studies/goldman-sachs-transfer-family-case-study": "https://aws.amazon.com/solutions/case-studies/goldman-sachs-transfer-family-case-study/",
    "www/solutions/case-studies/emirates-case-study": "https://aws.amazon.com/solutions/case-studies/emirates-case-study/",
    "www/solutions/case-studies/ryanair-video-case-study": "https://aws.amazon.com/solutions/case-studies/ryanair-video-case-study/",
    "www/solutions/case-studies/paige-case-study": "https://aws.amazon.com/solutions/case-studies/paige-case-study/",
    "www/solutions/case-studies/jps-case-study": "https://aws.amazon.com/solutions/case-studies/jps-case-study/",
}
fetch_failures = [{"url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/welcome.html",
                   "reason": "final answer was not 200 (exit 1); nothing stored. Not a registry source. Large-migration planning comes from the DataSync guide pages datasync-large-migration*, gathering-migration-requirements and datasync-large-migration-timelines."}]
for sid, why in UNUSABLE.items():
    fetch_failures.append({"url": URLS[sid], "reason": why})
usable = [s for s in sources if s["source_id"] not in UNUSABLE]

notes = [
    "Research input only: FREQUENCY.md (rank 13 of 42, 'strong', 3 first-hand reports; pairs DataSync vs Storage Gateway, S3 File vs Volume (cached/stored) vs Tape Gateway, DataSync vs Snowball vs Transfer Family; stem signals 'minimal code changes', 'existing backup software and tapes', 'SFTP', 'limited bandwidth', 'LEAST cost to transfer') and FRESHNESS.md section 'Backup, Storage Gateway, DataSync, Snow, Transfer Family' plus its section 3 lifecycle rows are hypotheses. Every value must come from a saved AWS page.",
    "Snow Family trap for the writer: the exam guide still lists AWS Snow Family in scope, but the saved pages say Snowball Edge is no longer available to new customers (availability change page; maintenance list date October 7, 2025; document history: effective November 7, 2025) and the product page www/snowball announces end of support on December 31, 2026 in commercial Regions. Teach Snowball Edge as an answer older questions expect, with a 'Changed recently' note, and teach DataSync (optionally over a Direct Connect hosted connection) and AWS Data Transfer Terminal as what AWS names today. The Well-Architected COST08-BP03 sentence still recommends Snow Family devices including Snowmobile; never use it as current advice.",
    "Storage decision guide: docs/decision-guides/latest/decision-guides/choosing-aws-storage-service was revalidated by plan-25 on 2026-10-14 because the decision-guides document history (2026-10-05) says the guide now names AWS Data Transfer Terminal instead of Snow Family. Six verified facts of chapters 22 and 23 no longer match the new text (list in revalidation-impact.json in this folder); the orchestrator decides how to handle them. Miners quote the current snapshot.",
    "Quota trap for the writer: the Transfer Family quota row 'File size' (5 Terabytes, 'the maximum size of an individual object in Amazon S3') and the Snowball quotas note (objects up to 5 TB) predate the S3 change to 50 TB (s3-change-max-object-size-50-tb-2025-12, chapter 21). Record those rows only with their own scope; do not state 5 TB as the S3 maximum. S3 File Gateway's own maximum file size (fgw-quotas) is a separate value.",
    "Ownership: chapter 12 owns Direct Connect and Site-to-Site VPN (reuse direct-connect-hosted-* facts, for example direct-connect-hosted-connection-provisioned-by-partner and direct-connect-limit-hosted-port-speeds); chapter 21 owns S3 storage classes, Lifecycle, Object Lock and S3 Transfer Acceleration (reuse s3-transfer-acceleration-* facts); chapter 23 owns EFS and FSx (reuse efs-datasync-*, efs-transfer-family-*, efs-faq-transfer-family-protocols, fsx-change-fsx-file-gateway-maintenance-2024-10, fsx-faq-windows-file-gateway-onprem, fsx-windows-migrate-with-datasync-or-robocopy); chapter 24 owns AWS Backup (reuse backup-storage-gateway-volume-gateway-supported); AWS Outposts belongs to its own chapter (here only the sentence that names it as the Snowball Edge compute alternative).",
    "Fact namespaces: storage-gateway-* (all four gateway types; prefix the type, for example storage-gateway-s3-file-*, storage-gateway-volume-*, storage-gateway-tape-*, storage-gateway-fsx-file-*), datasync-*, snow-family-* (Snowball Edge and AWS Data Transfer Terminal as snow-family-dtt-*), transfer-family-*. Change facts: <service>-change-*. FAQ facts: <service>-faq-*. Comparison facts sit with the service they decide for (datasync-vs-storage-gateway-* under datasync). Before adding, run 'python3 aws-saa-book/tools/saa.py facts list --service <key>' for s3, efs, fsx, backup, direct-connect, well-architected and reuse an existing id.",
    "Not examinable yet (GA after 2026-07-15): Storage Gateway FIPS endpoints over PrivateLink for Tape and Volume Gateway (2026-08-19) and for S3 File Gateway (2026-09-10); DataSync Enhanced mode for EFS, FSx for Lustre, HDFS, Azure Blob and object storage, and Hyper-V agents (2026-07-28); DataSync shared VPCs (2026-09-15 history, 2026-09-29 What's New); Transfer Family source IP preservation behind an NLB (2026-09-15/17), SFTP connector quota auto-approval up to 1,000 (2026-09-30), custom CloudWatch log groups for managed workflows (2026-10-01). Examinable but recent ('Changed recently'): Storage Gateway console copy of file shares (2026-07-14), DataSync Secrets Manager for all locations (2026-03-20), Transfer Family FSx for ONTAP (2026-01-26), DataSync Enhanced mode on-premises to S3 (2025-12-12), Snowball Edge closed to new customers (2025-11-07).",
    "Change inputs: changes-storage-gateway.txt (51 items since 2022-07-01), changes-datasync.txt (83), changes-snow-family.txt (24), changes-transfer-family.txt (about 90; skip Region launches and Terraform modules) in this folder; 'python3 aws-saa-book/tools/saa.py changes for <service> --find TEXT --verbose'. What's New posts of 2025-2026 named in the demand items are saved (urls-j-whatsnew.txt). The Snowmobile and Snowcone retirements are not in the feeds (d25-097 is a hypothesis).",
    "FAQ indexes parsed 2026-10-14: corpus/faq/storagegateway.jsonl (200 rows; row 200 '[] NA' is page noise), datasync.jsonl (83; row 83 noise), snowball.jsonl (60; row 1 'Notice', row 60 noise), aws-transfer-family.jsonl (200; row 200 noise). Question lists: faq-storagegateway.txt, faq-datasync.txt, faq-snowball.txt, faq-transfer-family.txt in this folder. Storage Gateway and Transfer Family both parsed exactly 200 rows; if a FAQ question you need is missing, search the snapshot text with 'saa.py show <faq source> --around TEXT'.",
    "Case studies in the corpus: www/solutions/case-studies/myriota-case-study (AWS Transfer for SFTP), 3m-accelerating-migration-case-study (DataSync with Application Migration Service), glam (Oxford GLAM, Storage Gateway, 50-60 percent lower storage cost). Five other candidates redirect to the directory page (fetch_failures).",
    "Callvale (STARTUP.md chapter 25, stage 3, month 21): the bank's 80 TB archive, 6.7 million recordings, must be in S3 within 30 days; a VPN test reached 100 Mbps (74 days); the bank allows 500 Mbps on Direct Connect (15 days). Options: custom copy programs through the VPN / an AWS Snow Family device / AWS DataSync through Direct Connect (chosen; qualifier 'least operational overhead'; accepts using the bank's allowance for about 15 days). Also: the bank's recorder can only write to a file share, so an S3 File Gateway runs in the bank's data center (prefix ostell/archive/, S3 Standard-IA); Dorrin Health sends 6,000 recordings (about 70 GB) at 01:00 by SFTP to sftp.callvale.example. Ana asks: '80 terabytes: do we send it through the network or do we ship storage devices?' data/startup.json: 'Snow Family: check the current device status in the canon before you state why it was not chosen.' Demand items tagged 'callvale' hold the facts behind these reasons; if the canon has no sentence for a stated reason, the miner reports not-found and the writer changes the reason. Question stems never name Callvale.",
    "Lens names in the demand items: numbers, changes (lens numbers+changes); behavior, decisions (lens behavior+decisions); faq (lens faq). See mine-plan.json.",
]

bullets = ["3.1.K1", "3.5.K3", "3.5.K6", "3.5.S3", "4.1.K8", "4.1.S3", "4.1.S7", "2.1.K2"]
covered = {x["bullet"] for x in D}
missing = [b for b in bullets if b not in covered]
assert not missing, missing

brief = {
    "chapter": "25", "slug": "hybrid-storage",
    "title": "Storage Gateway, DataSync, Snow Family and Transfer Family",
    "template": "medium", "written_by": "plan-25", "written_at": TODAY,
    "sources_fetched": len(usable), "fetch_failures": fetch_failures, "notes": notes, "demand": D,
}
(HERE / "brief.v0.json").write_text(json.dumps(brief, indent=1, ensure_ascii=False) + "\n")

# ---------------- mine-plan.json ----------------
LENS_OF = {"numbers": "numbers+changes", "changes": "numbers+changes", "behavior": "behavior+decisions",
           "decisions": "behavior+decisions", "faq": "faq"}
lenses = {"numbers+changes": [], "behavior+decisions": [], "faq": []}
pages = {k: [] for k in lenses}
for x in D:
    L = LENS_OF[x["lens"]]
    lenses[L].append(x["id"])
    for p in x["look_in"]:
        if p not in pages[L]:
            pages[L].append(p)

usable_ids = {s["source_id"] for s in usable} | {"docs/decision-guides/latest/decision-guides/choosing-networking-and-content-delivery-service"}
unknown = sorted({p for L in pages for p in pages[L] if p not in usable_ids})

# every usable guide page goes to the behavior lens as extra reading, quotas/history/pricing to numbers
for s in usable:
    sid = s["source_id"]
    if any(sid in pages[L] for L in pages):
        continue
    if sid.startswith("www/about-aws/whats-new/") or sid.endswith(("DocumentHistory", "doc-history")) or "limits" in sid or "quotas" in sid or "pricing" in sid:
        pages["numbers+changes"].append(sid)
    else:
        pages["behavior+decisions"].append(sid)

beh = lenses["behavior+decisions"]
def ids(lo, hi):
    return [i for i in beh if lo <= int(i[4:]) <= hi]

plan = {
    "chapter": "25", "written_by": "plan-25", "written_at": TODAY,
    "rules": [
        "Read brief.v0.json in this folder first: its notes say what is not examinable yet, who owns what, the Snow Family and quota traps, and the Callvale facts. Each demand item has a question and look_in (source_ids of saved snapshots). Answer the question only from those pages, or from another saved AWS page you name.",
        "Facts go into files of 10 to 25 facts each under aws-saa-book/_build/work/25-hybrid-storage/ named facts-<lens>-NN.json (lens names: numbers, changes, behavior, decisions, faq). Each fact names its demand item id.",
        "Every quote is copied verbatim from the saved snapshot (use 'python3 aws-saa-book/tools/saa.py show <source_id> --around TEXT' and 'search'; use 'tables <source_id> --index N' for quota rows and quote the row with its header, for example the 'Quotas for file shares' table of docs/filegateway/latest/files3/fgw-quotas or the 'DataSync quotas' table of docs/datasync/latest/userguide/datasync-limits). Never paraphrase inside a quote. The quote must carry every clause, scope, condition and exception of the claim on its own: when the condition stands in the next sentence, include that sentence in the quote; otherwise narrow the claim. A display of a fact without numbers is a verbatim phrase of at most 8 words from the quote.",
        "Fact namespaces by service: storage-gateway-*, datasync-*, snow-family-* (AWS Data Transfer Terminal as snow-family-dtt-*), transfer-family-*. Change facts: <service>-change-*. FAQ facts: <service>-faq-*. Comparison facts sit with the service they decide for (datasync-vs-storage-gateway-* under datasync). Before adding, run 'python3 aws-saa-book/tools/saa.py facts list --service <key>' for s3, efs, fsx, backup, direct-connect and well-architected and reuse an existing id instead of duplicating (brief.v0.json notes list the likely ones).",
        "A demand item that the pages cannot answer is reported as not-found in the miner note with what was searched; never answer from memory. A demand item that starts with 'Hypothesis' is a research claim to test, not a fact to confirm.",
        "All pages below are in the corpus (fetched or cached by plan-25 on 2026-10-14). A page outside this list is fetched with 'python3 aws-saa-book/tools/saa.py fetch <url>' before it is quoted. Pages in brief.v0.json fetch_failures are blocked or unusable; use the replacement named in each reason.",
        "Snow Family: every Snowball Edge fact keeps its status scope. A claim such as 'use Snowball Edge to move petabytes offline' must not be stated as current advice without the availability change; the Well-Architected COST08-BP03 Snow sentence is old and must not be mined as a recommendation.",
        "Not examinable yet: anything GA after 2026-07-15 (list in brief.v0.json notes). Record such a change as a change fact with its date so the writer can label it; never let it replace the examinable value in a numbers fact.",
        "Pricing: dimensions only, never a dollar amount.",
    ],
    "lenses": {
        "numbers+changes": {"demand": lenses["numbers+changes"], "demand_count": len(lenses["numbers+changes"]),
                             "change_inputs": ["aws-saa-book/_build/work/25-hybrid-storage/changes-storage-gateway.txt",
                                               "aws-saa-book/_build/work/25-hybrid-storage/changes-datasync.txt",
                                               "aws-saa-book/_build/work/25-hybrid-storage/changes-snow-family.txt",
                                               "aws-saa-book/_build/work/25-hybrid-storage/changes-transfer-family.txt",
                                               "python3 aws-saa-book/tools/saa.py changes for <service> --find TEXT --verbose"],
                             "pages": pages["numbers+changes"], "page_count": len(pages["numbers+changes"])},
        "behavior+decisions": {"demand": beh, "demand_count": len(beh),
                                "batches": {
                                    "behavior-a (Storage Gateway)": ids(1, 19),
                                    "behavior-b (DataSync)": ids(50, 69),
                                    "behavior-c (Snow Family and Data Transfer Terminal; Transfer Family)": ids(90, 129),
                                    "decisions (comparisons, decision guides, whitepapers, Well-Architected, Callvale, case studies)": ids(140, 179),
                                },
                                "pages": pages["behavior+decisions"], "page_count": len(pages["behavior+decisions"])},
        "faq": {"demand": lenses["faq"], "demand_count": len(lenses["faq"]),
                "faq_index": "aws-saa-book/_build/corpus/faq/storagegateway.jsonl, datasync.jsonl, snowball.jsonl, aws-transfer-family.jsonl; question lists in aws-saa-book/_build/work/25-hybrid-storage/faq-*.txt; use 'python3 aws-saa-book/tools/saa.py faq <url> --find TEXT'",
                "pages": pages["faq"], "page_count": len(pages["faq"])},
    },
    "lens_instructions": {
        "numbers+changes": "Limits, defaults, sizes, times and pricing dimensions, then change items. Use 'tables' on docs/filegateway/latest/files3/fgw-quotas, docs/storagegateway/latest/vgw/resource-gateway-limits (cached and stored volume columns: one fact per column value), docs/storagegateway/latest/tgw/resource-gateway-limits, docs/datasync/latest/userguide/datasync-limits, docs/general/latest/gr/sg and docs/general/latest/gr/transfer-service (table 'Service quotas'), docs/snowball/latest/developer-guide/device-differences, and adopt rows with their header. Each value is its own fact. Change items: date, old value where a page states it, new value, pointer to the current-truth fact; mark items GA after 2026-07-15 as not examinable yet. Two files minimum: facts-numbers-NN.json and facts-changes-NN.json.",
        "behavior+decisions": "Can, cannot, only, by default, what happens when. One quoted sentence per claim; where a page gives a list (gateway types, DataSync locations, task options, Transfer Family endpoint types and identity providers, Snowball job types), make one fact per item. Work in the four batches given; write behavior-a first. Decisions: quote the FAQ comparison answers, the two decision guides, the AWS overview whitepaper definitions and the Well-Architected pages for every comparison (DataSync vs Storage Gateway; DataSync vs Transfer Acceleration; DataSync vs Transfer Family; DataSync vs rsync and S3 Replication; online vs offline; gateway type by signal; Transfer Family vs self-managed SFTP), the Callvale items (tagged callvale; if the canon has no sentence for a stated reason, report not-found so the writer changes the reason), and one quote each from the three case studies.",
        "faq": "Verbatim FAQ answers for the FAQ quick-fire section (medium template: 5 items shown; mine 14 to 18 for choice) from the four FAQ pages. Prefer short answers that settle a question in one or two sentences; record the question text exactly as the FAQ prints it. Skip the '[] NA' rows (page noise). The Snowball FAQ 'Notice' row is the availability notice; quote it as snow-family-faq-notice-*.",
    },
}
(HERE / "mine-plan.json").write_text(json.dumps(plan, indent=1, ensure_ascii=False) + "\n")
print("demand", len(D), "by lens", {k: len(v) for k, v in lenses.items()}, "pages", {k: len(v) for k, v in pages.items()}, "sources", len(usable))
print("look_in not in usable corpus list:", unknown)
