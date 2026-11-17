import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

WI = "ont/what-is-fsx-ontap"; HW = "ont/how-it-works-fsx-ontap"; HA = "ont/high-availability-AZ"; VC = "ont/volume-storage-capacity"
SN = "ont/snapshots-ontap"; SL = "ont/snaplock"; HS = "ont/how-snaplock-works"; BK = "ont/using-backups"; CL = "ont/supported-fsx-clients"
F = []
F.append(f("fsx-ontap-fully-managed-built-on-netapp-ontap", "behavior",
  "Amazon FSx for NetApp ONTAP is a fully managed service that provides reliable, scalable, high-performing and feature-rich file storage built on NetApp's ONTAP file system.",
  "What is Amazon FSx for NetApp ONTAP?",
  [(WI, "Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp's popular ONTAP file system.")],
  ["fully managed service", "built on NetApp's popular ONTAP file system"], "Amazon FSx for NetApp ONTAP", "2.2.S8", tier0=True))
F.append(f("fsx-ontap-multiprotocol-nfs-smb-iscsi-nvme-multiple-os", "capability",
  "You can access FSx for ONTAP data from Linux, Windows and macOS clients at the same time over NFS (v3, v4, v4.1, v4.2) and SMB, and you can also use the NVMe and iSCSI block protocols.",
  "Which protocols does FSx for NetApp ONTAP serve?",
  [(HW, "You can access your data on FSx for ONTAP volumes from multiple Linux, Windows, or macOS clients simultaneously over the NFS (v3, v4, v4.1, v4.2) and SMB protocols. You can also access data using the Non-Volatile Memory Express (NVMe) and Internet Small Computer Systems Interface (iSCSI) block protocol.")],
  ["Linux, Windows, or macOS clients simultaneously", "Non-Volatile Memory Express (NVMe)"], "Amazon FSx for NetApp ONTAP", "2.2.S8", tier0=True))
F.append(f("fsx-ontap-supported-clients-nfs-smb-iscsi-versions", "capability",
  "FSx for ONTAP supports access over NFS (v3, v4.0, v4.1 and v4.2), all versions of SMB (including 2.0, 3.0 and 3.1.1) and the iSCSI protocol.",
  "Which NFS and SMB versions does FSx for ONTAP support?",
  [(CL, "FSx for ONTAP file systems support accessing data from a wide variety of compute instances and operating systems. It does this by supporting access using the Network File System (NFS) protocol (v3, v4.0, v4.1 and v4.2), all versions of the Server Message Block (SMB) protocol (including 2.0, 3.0, and 3.1.1), and the Internet Small Computer Systems Interface (iSCSI) protocol.")],
  ["v3, v4.0, v4.1 and v4.2", "including 2.0, 3.0, and 3.1.1"], "Amazon FSx for NetApp ONTAP clients", "4.1.K4"))
F.append(f("fsx-ontap-no-public-internet-access", "restriction",
  "Amazon FSx doesn't support accessing FSx for ONTAP file systems from the public internet.",
  "Can an FSx for ONTAP file system be reached from the public internet?",
  [(CL, "Amazon FSx doesn't support accessing file systems from the public internet.")],
  ["doesn't support accessing file systems", "from the public internet"], "Amazon FSx for NetApp ONTAP clients", "4.1.K4", rel="extended"))
F.append(f("fsx-ontap-four-deployment-types", "behavior",
  "FSx for ONTAP uses Single-AZ and Multi-AZ deployment types, with four options: Single-AZ 1, Single-AZ 2, Multi-AZ 1 and Multi-AZ 2.",
  "Which deployment types does FSx for NetApp ONTAP offer?",
  [(HA, "Amazon FSx for NetApp ONTAP uses Single-AZ and Multi-AZ deployment types. You can choose from four options: Single-AZ 1, Single-AZ 2, Multi-AZ 1, and Multi-AZ 2.")],
  ["Single-AZ 1, Single-AZ 2, Multi-AZ 1, and Multi-AZ 2", "Single-AZ and Multi-AZ deployment types"], "Amazon FSx for NetApp ONTAP", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-single-az-1-one-ha-pair-single-az-2-up-to-12", "behavior",
  "Single-AZ 1 is a first-generation file system with one high-availability pair, whereas Single-AZ 2 is a second-generation file system with 1 to 12 HA pairs.",
  "How many HA pairs can an FSx for ONTAP Single-AZ file system have?",
  [(HA, "Single-AZ 1 is a first-generation file system with one high-availability (HA) pair, whereas Single-AZ 2 is a second-generation file system with 1–12 HA pairs.")],
  ["with 1–12 HA pairs", "first-generation file system with one high-availability"], "Amazon FSx for NetApp ONTAP Single-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-single-az-active-standby-pairs-separate-fault-domains", "behavior",
  "A Single-AZ FSx for ONTAP file system provisions one to twelve pairs of active-standby file servers, with the active and standby server of each pair in separate fault domains within one Availability Zone.",
  "How are the file servers of a Single-AZ FSx for ONTAP file system arranged?",
  [(HA, "When you create a Single-AZ file system, Amazon FSx automatically provisions one to twelve pairs of file servers in an active-standby configuration, with the active and standby file servers in each pair located in separate fault domains within a single Availability Zone in the AWS Region.")],
  ["active-standby configuration", "separate fault domains within a single Availability Zone"], "Amazon FSx for NetApp ONTAP Single-AZ", "2.2.K11"))
F.append(f("fsx-ontap-single-az-failover-within-seconds", "behavior",
  "During planned maintenance or an unplanned disruption of an active file server, Amazon FSx automatically and independently fails over that HA pair to the standby file server, typically within a few seconds, with no manual intervention.",
  "How does a Single-AZ FSx for ONTAP file system handle a file server failure?",
  [(HA, "During planned file system maintenance or an unplanned service disruption of any active file server, Amazon FSx automatically and independently fails over that high-availability (HA) pair to the standby file server, typically within a few seconds. During a failover, you continue to have access to your data without manual intervention.")],
  ["typically within a few seconds", "automatically and independently fails over"], "Amazon FSx for NetApp ONTAP Single-AZ", "2.2.K11"))
F.append(f("fsx-ontap-single-az-for-dev-test-secondary-copies", "behavior",
  "Single-AZ FSx for ONTAP file systems suit use cases that do not require the data resiliency of Multi-AZ, such as development and test environments or secondary copies of data already stored on premises or in other Regions, because they replicate data only within a single Availability Zone.",
  "When is a Single-AZ FSx for ONTAP file system the right choice?",
  [(HA, "Single-AZ file systems are designed for use cases that do not require the data resiliency model of a Multi-AZ file system. They provide a cost-optimized solution for use cases such as development and test environments, or storing secondary copies of data that is already stored on premises or in other AWS Regions, by only replicating data within a single Availability Zone.")],
  ["development and test environments", "only replicating data within a single Availability Zone"], "Amazon FSx for NetApp ONTAP Single-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-multi-az-standby-other-az-sync-replication", "behavior",
  "A Multi-AZ FSx for ONTAP file system has a single HA pair whose standby file server is in a different Availability Zone from the active one, and every change is synchronously replicated across Availability Zones to the standby.",
  "How does Multi-AZ FSx for ONTAP replicate data?",
  [(HA, "Multi-AZ deployments have a single HA pair of file servers, the standby file server is deployed in a different Availability Zone from the active file server in the same AWS Region. Any changes written to your file system are synchronously replicated across Availability Zones to the standby.")],
  ["deployed in a different Availability Zone", "synchronously replicated across Availability Zones"], "Amazon FSx for NetApp ONTAP Multi-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-multi-az-continuous-availability-business-critical", "behavior",
  "Multi-AZ FSx for ONTAP file systems are designed to provide continuous availability to data even when an Availability Zone is unavailable, and suit business-critical production workloads that need built-in replication across Availability Zones.",
  "When is Multi-AZ FSx for ONTAP the right choice?",
  [(HA, "Multi-AZ file systems support all the availability and durability features of Single-AZ file systems. In addition, they are designed to provide continuous availability to data even when an Availability Zone is unavailable."),
   (HA, "Multi-AZ file systems are designed for use cases such as business-critical production workloads that require high availability to shared ONTAP file data and need storage with built-in replication across Availability Zones.")],
  ["continuous availability to data", "business-critical production workloads"], "Amazon FSx for NetApp ONTAP Multi-AZ", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-deployment-type-cannot-change-after-creation", "restriction",
  "You can't change an FSx for ONTAP file system's deployment type after creation; to change it you back up your data and restore it on a new file system, or migrate the data with SnapMirror, DataSync or another copy tool.",
  "Can you change an FSx for ONTAP file system from Single-AZ to Multi-AZ later?",
  [(HA, "You can't change your file system's deployment type after creation. If you want to change the deployment type (for example, to move from Single-AZ 1 to Single-AZ 2), you can back up your data and restore it on a new file system. You can also migrate your data with NetApp SnapMirror, with AWS DataSync, or with a third-party data copying tool.")],
  ["can't change your file system's deployment type", "restore it on a new file system"],
  "Amazon FSx for NetApp ONTAP", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-failover-conditions", "behavior",
  "FSx for ONTAP file systems automatically fail over an HA pair to the standby file server if the preferred or active server becomes unavailable or undergoes planned maintenance, or if an Availability Zone outage occurs (Multi-AZ only).",
  "What triggers failover of an FSx for ONTAP HA pair?",
  [(HA, "Single-AZ and Multi-AZ file systems automatically fail over a given HA pair from the preferred or active file server to the standby file server if any of the following conditions occur:"),
   (HA, "The preferred or active file server becomes unavailable"), (HA, "The preferred or active file server undergoes planned maintenance"),
   (HA, "An Availability Zone outage occurs (Multi-AZ file systems only)")],
  ["becomes unavailable", "undergoes planned maintenance", "Multi-AZ file systems only"], "Amazon FSx for NetApp ONTAP failover", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-failover-failback-under-60-seconds", "sla",
  "An FSx for ONTAP failover typically completes in less than 60 seconds from detection of the failure to promotion of the standby, and for Multi-AZ file systems failback to the recovered preferred file server is automatic and usually takes less than 60 seconds.",
  "How long does an FSx for ONTAP failover take?",
  [(HA, "For Multi-AZ file systems, when the preferred file server is fully recovered and becomes available, Amazon FSx automatically fails back to it, with failback usually completing in less than 60 seconds. For Single-AZ and Multi-AZ file systems, a failover typically completes in less than 60 seconds from the detection of the failure on the active file server to the promotion of the standby file server to active status.")],
  ["less than 60 seconds", "automatically fails back to it"], "Amazon FSx for NetApp ONTAP failover", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-failover-transparent-nfs-smb-iscsi-needs-multipathing", "behavior",
  "For NFS and SMB clients, failovers are transparent because the endpoint IP address stays the same; for iSCSI and NVMe/TCP, transparency depends on client-side multipathing that you must configure on the client.",
  "Are FSx for ONTAP failovers transparent to clients?",
  [(HA, "For NFS and SMB clients, failovers are transparent because the endpoint IP address that clients use to access your data remains the same, so Linux, Windows, and macOS applications resume file system operations without manual intervention. For the iSCSI and NVMe/TCP block storage protocols, failover transparency instead depends on client-side multipathing, which you must configure on the client so that it automatically fails over between your file servers.")],
  ["failovers are transparent", "client-side multipathing"], "Amazon FSx for NetApp ONTAP failover", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-each-ha-pair-fails-over-independently", "behavior",
  "For second-generation FSx for ONTAP file systems with multiple HA pairs, each HA pair's failover behavior is independent.",
  "Does a failure of one HA pair fail over the whole multi-pair FSx for ONTAP file system?",
  [(HA, "For second-generation file systems with multiple HA pairs, each HA pair's failover behavior is independent.")],
  ["failover behavior is independent", "each HA pair's failover"], "Amazon FSx for NetApp ONTAP failover", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-test-failover-by-changing-throughput-capacity", "capability",
  "You can test failover on an FSx for ONTAP file system by modifying its throughput capacity.",
  "How do you test failover on FSx for ONTAP?",
  [(HA, "You can test failover on your file system by modifying its throughput capacity.")],
  ["test failover on your file system", "modifying its throughput capacity"], "Amazon FSx for NetApp ONTAP failover", "2.2.K11", rel="reference"))
F.append(f("fsx-ontap-ha-pairs-by-generation", "behavior",
  "First-generation FSx for ONTAP file systems and second-generation Multi-AZ file systems support one HA pair, while second-generation Single-AZ file systems support up to 12 HA pairs.",
  "How many HA pairs do FSx for ONTAP file systems support?",
  [(HW, "First-generation FSx for ONTAP file systems and second-generation Multi-AZ file systems support one HA pair. Second-generation Single-AZ file systems support up to 12 HA pairs.")],
  ["support one HA pair", "support up to 12 HA pairs"], "Amazon FSx for NetApp ONTAP", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-svm-isolated-file-server-joins-active-directory", "behavior",
  "A storage virtual machine (SVM) is an isolated file server with its own administrative and data access endpoints, and you can join SVMs to a Microsoft Active Directory for file access authentication and authorization.",
  "What is a storage virtual machine in FSx for ONTAP and how does it use Active Directory?",
  [(HW, "A storage virtual machine (SVM) is an isolated file server with its own administrative and data access endpoints for administering and accessing data."),
   (HW, "You can join SVMs to a Microsoft Active Directory for file access authentication and authorization.")],
  ["isolated file server", "join SVMs to a Microsoft Active Directory"], "Amazon FSx for NetApp ONTAP SVM", "2.2.S7", tier0=True))
F.append(f("fsx-ontap-volumes-logical-containers-on-svms-thin-provisioned", "behavior",
  "FSx for ONTAP volumes are logical containers hosted on SVMs, and they are thin provisioned, so they only consume storage capacity for the data stored in them.",
  "What is a volume in FSx for ONTAP and how is its capacity used?",
  [(HW, "Volumes are logical containers that are hosted on SVMs, and data stored in them consumes physical storage capacity on your file system."),
   (HW, "FSx for ONTAP volumes are thin provisioned, meaning that they only consume storage capacity for the data stored in them.")],
  ["logical containers that are hosted on SVMs", "thin provisioned"], "Amazon FSx for NetApp ONTAP volumes", "2.2.S7", tier0=True))
F.append(f("fsx-ontap-two-storage-tiers-primary-ssd-and-capacity-pool", "behavior",
  "An FSx for ONTAP file system has two storage tiers: primary storage, which is provisioned high-performance SSD storage for the active portion of your data, and capacity pool storage, which is fully elastic, scales to petabytes and is cost optimized for infrequently accessed data.",
  "What are the two storage tiers of FSx for ONTAP?",
  [(HW, "An FSx for ONTAP file system has two *storage tiers*: primary storage and capacity pool storage. Primary storage is provisioned, scalable, high-performance SSD storage that’s purpose-built for the active portion of your data set. Capacity pool storage is a fully elastic storage tier that can scale to petabytes in size and is cost optimized for infrequently accessed data.")],
  ["primary storage and capacity pool storage", "fully elastic storage tier"], "Amazon FSx for NetApp ONTAP storage tiers", "4.1.K7", tier0=True))
F.append(f("fsx-ontap-tiering-policy-per-volume-cooling-period", "behavior",
  "Data tiering automatically moves data between the SSD and capacity pool tiers; each volume has a tiering policy that controls whether cold data moves to the capacity tier, and the cooling period determines when data becomes cold.",
  "What controls when FSx for ONTAP moves data to the capacity pool?",
  [(HW, "Each volume has a tiering policy that controls whether data is moved to the capacity tier when it becomes inactive (cold). A volume's Tiering policy cooling period determines when data becomes inactive (cold).")],
  ["tiering policy that controls whether data is moved", "cooling period determines when data becomes inactive"], "Amazon FSx for NetApp ONTAP storage tiers", "4.1.K7", tier0=True))
F.append(f("fsx-ontap-tiering-policy-auto-31-days-default-console", "default",
  "The Auto tiering policy moves all cold user data and snapshots to the capacity pool tier; the cooling period is 31 days by default and configurable from 2 to 183 days, and Auto is the default policy when creating a volume in the console.",
  "What does the Auto tiering policy do and what is its default cooling period?",
  [(VC, "**Auto** – This policy moves all cold data—user data and snapshots—to the capacity pool tier. The cooling rate of data is determined by the policy's cooling period, which by default is 31 days, and is configurable to values between 2–183 days."),
   (VC, "This is the default policy when creating a volume using the Amazon FSx console.")],
  ["by default is 31 days", "between 2–183 days"], "FSx for ONTAP volume tiering policy Auto", "4.1.K7", dm="default", adj=True, tier0=True))
F.append(f("fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli", "default",
  "The Snapshot Only tiering policy moves only snapshot data to the capacity pool tier, with a cooling period that is 2 days by default and configurable from 2 to 183 days; it is the default policy when creating a volume with the AWS CLI, API or ONTAP CLI.",
  "What does the Snapshot Only tiering policy do?",
  [(VC, "**Snapshot Only** – This policy moves only snapshot data to the capacity pool storage tier. The rate at which snapshots are tiered to the capacity pool is determined by the policy's cooling period, which by default is set to 2 days, and is configurable to values between 2–183 days."),
   (VC, "This is the default policy when creating a volume using the AWS CLI, Amazon FSx API, or the NetApp ONTAP CLI.")],
  ["moves only snapshot data", "by default is set to 2 days"], "FSx for ONTAP volume tiering policy Snapshot Only", "4.1.K7", dm="default", adj=True, tier0=True))
F.append(f("fsx-ontap-tiering-policy-all-marks-everything-cold", "behavior",
  "The All tiering policy marks all user data and snapshot data as cold and stores it in the capacity pool tier, where data blocks stay cold when read; file metadata always remains on the SSD tier.",
  "What does the All tiering policy do in FSx for ONTAP?",
  [(VC, "**All** – This policy marks all user data and snapshot data as cold, and stores it in the capacity pool tier. When data blocks are read, they remain cold and are not written to the primary storage tier."),
   (VC, "Note that file metadata always remains on the SSD tier.")],
  ["marks all user data and snapshot data", "file metadata always remains on the SSD tier"], "FSx for ONTAP volume tiering policy All", "4.1.K7", tier0=True))
F.append(f("fsx-ontap-tiering-policy-none-keeps-all-on-ssd", "behavior",
  "The None tiering policy keeps all of a volume's data on the primary storage tier and prevents it from being moved to capacity pool storage.",
  "Which FSx for ONTAP tiering policy keeps data only on SSD?",
  [(VC, "**None** – This policy keeps all of your volume’s data on the primary storage tier, and prevents it from being moved to capacity pool storage.")],
  ["keeps all of your volume’s data", "prevents it from being moved"], "FSx for ONTAP volume tiering policy None", "4.1.K7", tier0=True))
F.append(f("fsx-ontap-tiering-happens-24-48-hours-after-cooling-period", "behavior",
  "Data is tiered 24 to 48 hours after its cooling period expires, and tiering is a background process with a lower priority than client-facing requests.",
  "When is data tiered after the cooling period of an FSx for ONTAP volume expires?",
  [(VC, "Data is tiered 24–48 hours after its cooling period expires. Tiering is a background process that consumes network resources, and has a lower priority than client-facing requests.")],
  ["24–48 hours after its cooling period expires", "lower priority than client-facing requests"], "FSx for ONTAP volume tiering", "4.1.K7", rel="extended"))
F.append(f("fsx-ontap-storage-efficiency-65-percent-typical", "behavior",
  "The typical storage capacity savings for general purpose file sharing workloads is 65% from compression, deduplication and compaction on both the SSD and capacity pool tiers, without sacrificing performance.",
  "How much storage does FSx for ONTAP storage efficiency typically save?",
  [(HW, "The typical storage capacity savings for general purpose file sharing workloads without sacrificing performance is 65% from compression, deduplication, and compaction, on both the SSD and capacity pool storage tiers.")],
  ["65% from compression, deduplication, and compaction", "general purpose file sharing workloads"], "Amazon FSx for NetApp ONTAP storage efficiency", "4.1.S10", tier0=True))
F.append(f("fsx-ontap-snapshots-restore-individual-files-self-service", "behavior",
  "With ONTAP snapshots, users can view and restore individual files or folders from an earlier snapshot to undo changes, recover deleted content and compare file versions.",
  "How do users restore files on FSx for ONTAP without an administrator?",
  [(SN, "With snapshots, your users can easily view and restore individual files or folders from an earlier snapshot to undo changes, recover deleted content, and compare file versions.")],
  ["restore individual files or folders", "from an earlier snapshot"], "Amazon FSx for NetApp ONTAP snapshots", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snapshots-1023-per-volume-limit", "limit",
  "You can store a maximum of 1,023 snapshots per volume at any point in time.",
  "How many snapshots can an FSx for ONTAP volume hold?",
  [(SN, "You can store a maximum of 1,023 snapshots per volume at any point in time.")],
  ["maximum of 1,023 snapshots per volume", "at any point in time"], "per FSx for ONTAP volume", "2.2.K11", dm="max", rel="extended"))
F.append(f("fsx-ontap-snapmirror-scheduled-replication-in-and-cross-region", "capability",
  "You can use NetApp SnapMirror to schedule periodic replication of an FSx for ONTAP file system to or from a second file system, in-Region or cross-Region, as frequently as every 5 minutes.",
  "Which ONTAP feature replicates FSx for ONTAP data across Regions?",
  [("ont/scheduled-replication", "You can use NetApp SnapMirror to schedule periodic replication of your FSx for ONTAP file system to or from a second file system. This capability is available for both in-Region and cross-Region deployments."),
   ("ont/scheduled-replication", "Replication can be scheduled as frequently as every 5 minutes, although intervals should be carefully chosen based on RPOs (Recovery Point Objectives), RTOs (Recovery Time Objectives), and performance considerations.")],
  ["both in-Region and cross-Region deployments", "as frequently as every 5 minutes"], "FSx for ONTAP SnapMirror", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snapmirror-volume-level-only-no-synchronous", "restriction",
  "Only volume-level SnapMirror replication is supported by FSx for ONTAP, and synchronous SnapMirror, including StrictSync, is not supported.",
  "Which SnapMirror modes does FSx for ONTAP support?",
  [("ont/scheduled-replication", "Only volume-level SnapMirror replication is supported by FSx for ONTAP. Synchronous SnapMirror, including StrictSync, is not supported.")],
  ["Only volume-level SnapMirror replication is supported", "Synchronous SnapMirror"], "FSx for ONTAP SnapMirror", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp", "behavior",
  "AWS recommends using NetApp SnapMirror to migrate on-premises NetApp ONTAP file systems to FSx for ONTAP.",
  "How do you migrate an on-premises NetApp system to FSx for ONTAP?",
  [("ont/migrating-fsx-ontap-snapmirror", "We recommend using SnapMirror to migrate on-premise NetApp ONTAP file systems to FSx for ONTAP."),
   ("ont/migrating-fsx-ontap-snapmirror", "You can migrate your NetApp ONTAP file systems to Amazon FSx for NetApp ONTAP using NetApp SnapMirror.")],
  ["recommend using SnapMirror to migrate", "migrate your NetApp ONTAP file systems"], "Amazon FSx for NetApp ONTAP migration", "2.2.S7", tier0=True))
F.append(f("fsx-ontap-flexcache-remote-caching-sparsely-populated", "behavior",
  "FlexCache is NetApp ONTAP's remote caching capability that brings datasets closer to clients; a FlexCache volume is a sparsely populated cache of an origin volume, best suited for read-intensive workflows with infrequent data changes.",
  "What is FlexCache and when is it best used?",
  [("ont/using-flexcache", "FlexCache is NetApp ONTAP's remote caching capability that brings datasets closer to clients, improving access performance and reducing costs."),
   ("ont/using-flexcache", "A FlexCache volume is a sparsely-populated cache that provides access to data stored in an origin volume."),
   ("ont/using-flexcache", "FlexCache volumes are best suited for read-intensive workflows with infrequent data changes because any changes to the origin data require the cache to be refreshed.")],
  ["remote caching capability", "sparsely-populated cache", "read-intensive workflows with infrequent data changes"], "FSx for ONTAP FlexCache", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snaplock-worm-compliance-and-enterprise-modes", "capability",
  "SnapLock moves files to a write once, read many (WORM) state that prevents modification or deletion for a specified retention period, and FSx for ONTAP supports the Compliance and Enterprise retention modes.",
  "Which SnapLock retention modes does FSx for ONTAP support?",
  [(SL, "SnapLock is a feature that allows you to protect your files by transitioning them to a write once, read many (WORM) state, which prevents modification or deletion for a specified retention period."),
   (SL, "Amazon FSx for NetApp ONTAP supports the Compliance and Enterprise modes of retention with SnapLock.")],
  ["write once, read many (WORM) state", "Compliance and Enterprise modes of retention"], "FSx for ONTAP SnapLock", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snaplock-compliance-no-delete-by-any-user", "restriction",
  "After a file is moved to the WORM state on a SnapLock Compliance volume, no user can delete it before its retention period expires.",
  "Who can delete a WORM file on a SnapLock Compliance volume before retention ends?",
  [("ont/snaplock-compliance", "After a file is transitioned to the write once, read many (WORM) state on a SnapLock Compliance volume, it can't be deleted before its retention period expires by any user.")],
  ["can't be deleted before its retention period expires", "by any user"], "FSx for ONTAP SnapLock Compliance", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snaplock-enterprise-specific-users-privileged-delete", "behavior",
  "SnapLock Enterprise lets you authorize only specific users to delete files, and you can use it to test retention settings before using SnapLock Compliance.",
  "How does SnapLock Enterprise differ from Compliance for deleting files?",
  [("ont/snaplock-enterprise", "You can use SnapLock Enterprise to authorize only specific users to delete files."),
   ("ont/snaplock-enterprise", "You can use SnapLock Enterprise to test retention settings before using SnapLock Compliance.")],
  ["authorize only specific users to delete files", "test retention settings"], "FSx for ONTAP SnapLock Enterprise", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-snaplock-compliance-use-cases-sec-finra-cftc", "capability",
  "You can use SnapLock Compliance to address government or industry-specific mandates such as SEC Rule 17a-4(f), FINRA Rule 4511 and CFTC Regulation 1.31.",
  "Which SnapLock mode addresses SEC and FINRA retention mandates?",
  [("ont/snaplock-compliance", "You can use SnapLock Compliance to address government or industry-specific mandates such as SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC Regulation 1.31.")],
  ["SEC Rule 17a-4(f), FINRA Rule 4511", "CFTC Regulation 1.31"], "FSx for ONTAP SnapLock Compliance", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-snaplock-set-at-volume-creation-no-conversion", "restriction",
  "You must decide at volume creation whether a volume uses SnapLock, a non-SnapLock volume can't be converted to a SnapLock volume, and a SnapLock volume can't be converted between Enterprise and Compliance.",
  "Can you turn an existing FSx for ONTAP volume into a SnapLock volume?",
  [(HS, "You must specify whether a volume will use SnapLock settings at the time of creation. A non-SnapLock volume can't be converted to a SnapLock volume after creation."),
   ("ont/snaplock-enterprise", "A SnapLock volume can't be converted from Enterprise to Compliance, or from Compliance to Enterprise.")],
  ["at the time of creation", "can't be converted to a SnapLock volume"], "FSx for ONTAP SnapLock", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-backups-automatic-daily-and-user-initiated-per-volume", "behavior",
  "FSx for ONTAP takes automatic daily backups, enabled by default for a file system's volumes, and user-initiated backups of volumes, and all backups are incremental.",
  "How does FSx for ONTAP back up volumes?",
  [(BK, "With FSx for ONTAP, you can protect your data by taking automatic daily backups and user-initiated backups of the volumes on your file system."),
   (BK, "When you create a file system, automatic daily backups are enabled by default for your file system's volumes."),
   (BK, "All Amazon FSx backups (automatic daily backups and user-initiated backups) are incremental, which means that they only store changes in the data since the previous backup was completed.")],
  ["automatic daily backups and user-initiated backups", "enabled by default for your file system's volumes"], "FSx for ONTAP backups", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-automatic-backup-retention-console-30-days-default-1-to-90", "default",
  "In the console you can set the automatic daily backup retention period of an FSx for ONTAP file system from 1 to 90 days, and the default is 30 days.",
  "What is the default retention of FSx for ONTAP automatic daily backups?",
  [(BK, "Using the console, you can set the retention period for automatic daily backups to a value from 1 to 90 days when creating a file system or at any time. The default automatic daily backup retention period is 30 days.")],
  ["default automatic daily backup retention period is 30 days", "from 1 to 90 days"], "FSx for ONTAP automatic daily backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("fsx-ontap-user-initiated-backups-retained-forever", "behavior",
  "User-initiated FSx for ONTAP backups are retained forever unless you delete them, and they are retained even after you delete the volume or the file system.",
  "How long are user-initiated FSx for ONTAP backups kept?",
  [(BK, "Your user-initiated backups are incremental relative to other backups that may have been created for a volume and are retained forever, unless you delete them. User-initiated backups are retained even after you delete the volume or the file system the backups were created on.")],
  ["retained forever, unless you delete them", "retained even after you delete the volume"], "FSx for ONTAP backups", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-backups-not-for-dp-lsm-flexcache-snapmirror-destination-volumes", "restriction",
  "Amazon FSx doesn't support backing up data protection (DP) volumes, load sharing mirror (LSM) volumes, or destination volumes for FlexCache and SnapMirror.",
  "Which FSx for ONTAP volumes cannot be backed up?",
  [(BK, "Amazon FSx doesn't support backing up data protection (DP) volumes, load sharing mirror (LSM) volumes, or destination volumes for FlexCache and SnapMirror.")],
  ["backing up data protection (DP) volumes", "destination volumes for FlexCache and SnapMirror"], "FSx for ONTAP backups", "2.2.K11", rel="reference"))
F.append(f("fsx-ontap-restore-backup-same-region-copy-first-for-other-region", "behavior",
  "You can restore an FSx for ONTAP volume backup to any existing FSx for ONTAP file system you have access to that is in the same AWS Region where the backup is stored.",
  "Where can an FSx for ONTAP volume backup be restored?",
  [(BK, "You can restore volume backups to any existing FSx for ONTAP file system you have access to that is in the same AWS Region where the backup is stored.")],
  ["any existing FSx for ONTAP file system", "same AWS Region where the backup is stored"], "FSx for ONTAP backups", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-arp-ai-driven-detects-ransomware-creates-snapshot", "behavior",
  "Autonomous Ransomware Protection (ARP) is an AI-driven NetApp ONTAP feature that monitors and protects data against ransomware and malware if your Windows or Linux clients become compromised, and when it detects abnormal activity it automatically creates an ONTAP snapshot.",
  "What does Autonomous Ransomware Protection do on FSx for ONTAP?",
  [("ont/ARP", "Autonomous Ransomware Protection (ARP) is a NetApp ONTAP AI-driven feature that monitors and protects your data against ransomware and malware attacks if your Windows or Linux clients become compromised."),
   ("ont/ARP", "If ARP detects any abnormal activity, an ONTAP snapshot is automatically created to help you recover your data as close as possible to the time of the potential attack.")],
  ["monitors and protects your data against ransomware", "an ONTAP snapshot is automatically created"], "FSx for ONTAP Autonomous Ransomware Protection", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost", "behavior",
  "ARP looks for changes in data entropy, changes in file extension types and surges in abnormal volume activity with encrypted data, and there is no additional cost for enabling ARP on an FSx for ONTAP file system.",
  "What signs does ARP look for and does it cost extra?",
  [("ont/ARP", "Changes in entropy, which means differences in the randomness of data in a file."),
   ("ont/ARP", "Changes in file IOPS, which means a surge in abnormal volume activity with encrypted data."),
   ("ont/ARP", "There is no additional cost for enabling ARP on your FSx for ONTAP file system.")],
  ["Changes in entropy", "Changes in file IOPS", "no additional cost for enabling ARP"], "FSx for ONTAP Autonomous Ransomware Protection", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-arp-not-a-defense-against-rogue-administrators", "restriction",
  "ARP doesn't prevent rogue administrators with credentials from accessing an FSx for ONTAP file system, so AWS recommends a layered approach with AWS Backup, ONTAP snapshots and SnapLock.",
  "Does ARP stop an administrator with valid credentials from damaging data?",
  [("ont/ARP", "ARP doesn't prevent rogue administrators with credentials from accessing your FSx for ONTAP file system. AWS recommends a layered security approach including AWS Backup, ONTAP snapshots, and SnapLock.")],
  ["doesn't prevent rogue administrators", "layered security approach"], "FSx for ONTAP Autonomous Ransomware Protection", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-encrypted-at-rest-kms-file-systems-and-backups", "behavior",
  "All FSx for ONTAP file systems and backups are encrypted at rest with keys managed in AWS KMS, and data is encrypted and decrypted transparently.",
  "Is encryption at rest optional for FSx for ONTAP?",
  [("ont/encryption-at-rest", "All Amazon FSx for NetApp ONTAP file systems and backups are encrypted at rest with keys managed using AWS Key Management Service (AWS KMS). Data is automatically encrypted before being written to the file system, and automatically decrypted as it is read.")],
  ["encrypted at rest with keys managed", "automatically decrypted as it is read"], "Amazon FSx for NetApp ONTAP encryption", "4.1.K4", tier0=True))
F.append(f("fsx-ontap-in-transit-kerberos-and-ipsec-options", "capability",
  "FSx for ONTAP can encrypt data in transit with Kerberos-based encryption over NFS and SMB and with IPsec-based encryption over NFS, iSCSI and SMB.",
  "How can data in transit to FSx for ONTAP be encrypted?",
  [("ont/encryption-in-transit", "Kerberos-based encryption over NFS and SMB protocols."),
   ("ont/encryption-in-transit", "IPsec-based encryption over NFS, iSCSI, and SMB protocols")],
  ["Kerberos-based encryption over NFS and SMB", "IPsec-based encryption over NFS, iSCSI, and SMB"], "Amazon FSx for NetApp ONTAP encryption", "4.1.K4", rel="extended"))
F.append(f("fsx-ontap-multi-az-floating-ip-endpoints", "behavior",
  "The NFS, SMB and ONTAP management endpoints on Multi-AZ FSx for ONTAP file systems use floating IP addresses so that connected clients transition seamlessly between the preferred and standby file servers during a failover.",
  "How do clients keep the same address during a Multi-AZ FSx for ONTAP failover?",
  [(CL, "The NFS, SMB, and ONTAP management endpoints on Amazon FSx for NetApp ONTAP Multi-AZ file systems use floating internet protocol (IP) addresses so that connected clients seamlessly transition between the preferred and standby file servers during a failover event.")],
  ["use floating internet protocol (IP) addresses", "seamlessly transition between the preferred and standby"], "Amazon FSx for NetApp ONTAP Multi-AZ", "4.1.K4", tier0=True))
F.append(f("fsx-ontap-multi-az-outside-vpc-needs-transit-gateway", "restriction",
  "VPC Peering, Direct Connect and Site-to-Site VPN don't support transitive peering, so you are required to use Transit Gateway to reach the floating-IP interfaces of a Multi-AZ file system from networks outside the file system's VPC.",
  "What is needed to reach a Multi-AZ FSx for ONTAP file system from on premises or another VPC?",
  [(CL, "VPC Peering, Direct Connect, and Site-to-Site VPN don't support transitive peering. Therefore, you are required to use Transit Gateway in order to access these interfaces from networks that are outside of your file system's VPC.")],
  ["don't support transitive peering", "required to use Transit Gateway"], "Amazon FSx for NetApp ONTAP Multi-AZ", "4.1.K4", tier0=True))
F.append(f("fsx-ontap-single-az-secondary-ips-no-transit-gateway-needed", "behavior",
  "On Single-AZ FSx for ONTAP file systems the NFS, SMB and management endpoints are secondary IP addresses within the VPC's CIDR range, so clients can use VPC Peering, Direct Connect or Site-to-Site VPN without AWS Transit Gateway.",
  "Does a Single-AZ FSx for ONTAP file system need Transit Gateway for outside access?",
  [(CL, "The endpoints used to access FSx for ONTAP Single-AZ file systems over NFS or SMB, and for administering file systems using the ONTAP CLI or REST API, are secondary IP addresses on the ENI of the active file server. The secondary IP addresses are within the VPC’s CIDR range, so clients can access data and management ports using VPC Peering, AWS Direct Connect, or Site-to-Site VPN without requiring AWS Transit Gateway.")],
  ["secondary IP addresses", "without requiring AWS Transit Gateway"], "Amazon FSx for NetApp ONTAP Single-AZ", "4.1.K4", rel="extended"))
F.append(f("fsx-ontap-s3-access-points-s3-api-on-file-data-no-copy", "capability",
  "An S3 access point attached to an FSx for ONTAP volume lets you access file data through the S3 API while the data stays on the file system and you keep using NFS and SMB alongside it.",
  "How can S3-based applications use data on FSx for ONTAP without copying it?",
  [("ont/accessing-data-via-s3-access-points", "The access point allows you to access your file data using the S3 API, though your data continues to reside on your FSx for ONTAP file system and you can continue using the NFS and SMB protocols to access your data alongside the S3 API.")],
  ["access your file data using the S3 API", "continue using the NFS and SMB protocols"], "Amazon FSx for NetApp ONTAP S3 access points", "4.1.K7", tier0=True))
F.append(f("fsx-ontap-s3-access-points-block-public-access-always-on", "restriction",
  "Amazon S3 enforces Block public access by default for all access points attached to an FSx for ONTAP volume, and you cannot modify or disable this setting.",
  "Can you allow public access on an S3 access point attached to FSx for ONTAP?",
  [("ont/accessing-data-via-s3-access-points", "Amazon S3 enforces Block public access by default for all access points attached to an FSx for ONTAP volume, and you cannot modify or disable this setting.")],
  ["enforces Block public access by default", "cannot modify or disable this setting"], "Amazon FSx for NetApp ONTAP S3 access points", "4.1.K7", rel="extended"))
F.append(f("fsx-ontap-vmware-cloud-external-datastore", "capability",
  "You can use FSx for ONTAP as an external datastore for VMware Cloud on AWS Software-Defined Data Centers (SDDCs).",
  "Can FSx for ONTAP be a datastore for VMware Cloud on AWS?",
  [("ont/vmware-cloud-ontap", "You can use FSx for ONTAP as an external datastore for VMware Cloud on AWS Software-Defined Data Centers (SDDCs).")],
  ["external datastore for VMware Cloud on AWS", "Software-Defined Data Centers (SDDCs)"], "Amazon FSx for NetApp ONTAP", "2.2.S7", tier0=True))
emit("facts-behavior-08.json", F)
