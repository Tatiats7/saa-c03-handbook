import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

WI = "lus/what-is"; UF = "lus/using-fsx-lustre"; DRA = "lus/create-dra-linked-data-repo"; OV = "lus/overview-dra-data-repo"
BK = "lus/using-backups-fsx"; IT = "lus/intelligent-tiering-file-systems"; FAQ = "www/fsx/lustre/faqs"
F = []
F.append(f("fsx-lustre-workloads-ml-hpc-video-financial", "behavior",
  "FSx for Lustre runs the high-performance Lustre file system for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing and financial modeling.",
  "What is Amazon FSx for Lustre built for?",
  [(WI, "You use Lustre for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing, and financial modeling.")],
  ["machine learning, high performance computing (HPC)", "video processing, and financial modeling"], "Amazon FSx for Lustre", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-posix-compliant-read-after-write-locking", "behavior",
  "FSx for Lustre is POSIX-compliant, so current Linux-based applications work without changes, and it provides read-after-write consistency and supports file locking.",
  "Does FSx for Lustre need application changes, and what consistency does it give?",
  [(WI, "FSx for Lustre is POSIX-compliant, so you can use your current Linux-based applications without having to make any changes."),
   (WI, "It also provides read-after-write consistency and supports file locking.")],
  ["FSx for Lustre is POSIX-compliant", "read-after-write consistency", "supports file locking"], "Amazon FSx for Lustre", "2.2.S8", rel="extended"))
F.append(f("fsx-lustre-clients-ec2-ecs-eks-linux-amis-lustre-client", "capability",
  "FSx for Lustre file systems are accessible from Amazon EC2 instances, Amazon ECS Docker containers and containers on Amazon EKS, and FSx for Lustre is compatible with popular Linux-based AMIs.",
  "Which compute services and operating systems can mount an FSx for Lustre file system?",
  [(WI, "Amazon FSx for Lustre file systems are accessible from compute workloads running on Amazon Elastic Compute Cloud (Amazon EC2) instances, on Amazon Elastic Container Service (Amazon ECS) Docker containers, and containers running on Amazon Elastic Kubernetes Service (Amazon EKS)."),
   (WI, "Amazon FSx for Lustre is compatible with the most popular Linux-based AMIs, including Amazon Linux 2023 and Amazon Linux 2, Red Hat Enterprise Linux (RHEL), CentOS, Ubuntu, and SUSE Linux.")],
  ["Amazon EC2", "Linux-based AMIs", "Amazon Elastic Kubernetes Service (Amazon EKS)"], "Amazon FSx for Lustre clients", "4.1.K4", tier0=True))
F.append(f("fsx-lustre-ec2-client-open-source-lustre-client-other-azs", "capability",
  "You access an FSx for Lustre file system from EC2 instances using the open-source Lustre client, and instances in other Availability Zones of the same VPC can access it if the networking allows access across subnets.",
  "How does an EC2 instance mount FSx for Lustre, and can it be in another Availability Zone?",
  [(WI, "**Amazon EC2** – You access your file system from your Amazon EC2 compute instances using the open-source Lustre client. Amazon EC2 instances can access your file system from other Availability Zones within the same Amazon Virtual Private Cloud (Amazon VPC), provided your networking configuration provides for access across subnets within the VPC.")],
  ["open-source Lustre client", "from other Availability Zones within the same"], "Amazon FSx for Lustre clients", "4.1.K4", rel="extended"))
F.append(f("fsx-lustre-on-premises-and-peered-vpc-access", "capability",
  "You can access an FSx for Lustre file system from EC2 instances in a peered VPC, or from on-premises clients connected to the file system's VPC with Direct Connect or VPN.",
  "How do on-premises clients or another VPC reach FSx for Lustre?",
  [("lus/mounting-on-premises", "You can access your Amazon FSx file system in two ways. One is from Amazon EC2 instances located in an Amazon VPC that's peered to the file system's VPC. The other is from on-premises clients that are connected to your file system's VPC using Direct Connect or VPN.")],
  ["peered to the file system's VPC", "using Direct Connect or VPN"], "Amazon FSx for Lustre clients", "4.1.K4", tier0=True))
F.append(f("fsx-lustre-scratch-temporary-not-replicated", "behavior",
  "Scratch FSx for Lustre file systems are for temporary storage and shorter-term processing; data is not replicated and does not persist if a file server fails.",
  "Which FSx for Lustre deployment type does not replicate data?",
  [(WI, "Scratch file systems are ideal for temporary storage and shorter-term processing of data. Data is not replicated and does not persist if a file server fails.")],
  ["Data is not replicated", "does not persist if a file server fails"], "FSx for Lustre scratch file systems", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-persistent-replicated-servers-replaced", "behavior",
  "Persistent FSx for Lustre file systems are for longer-term storage and throughput-focused workloads; data is replicated and file servers are replaced if they fail.",
  "How does a persistent FSx for Lustre file system handle a failed file server?",
  [(WI, "Persistent file systems are ideal for longer-term storage and throughput-focused workloads. In persistent file systems, data is replicated, and file servers are replaced if they fail.")],
  ["data is replicated", "file servers are replaced if they fail"], "FSx for Lustre persistent file systems", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-persistent-ssd-hdd-replicated-within-az-intelligent-tiering-multi-az", "behavior",
  "On persistent FSx for Lustre file systems, SSD and HDD data is replicated within the same Availability Zone, while Intelligent-Tiering data is replicated across multiple Availability Zones.",
  "Is an FSx for Lustre SSD file system replicated across Availability Zones?",
  [(UF, "For SSD and HDD-based file systems, data is automatically replicated within the same Availability Zone in which the file system is located. For Intelligent-Tiering file systems, data is replicated across multiple Availability Zones.")],
  ["replicated within the same Availability Zone", "replicated across multiple Availability Zones"], "FSx for Lustre persistent file systems", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-persistent-failed-server-replaced-within-minutes-clients-retry", "behavior",
  "On a persistent FSx for Lustre file system, an unavailable file server is replaced automatically within minutes of failure, and client requests to that server transparently retry and eventually succeed.",
  "What happens to client requests when a persistent Lustre file server fails?",
  [(UF, "On a persistent file system, if a file server becomes unavailable, it's replaced automatically within minutes of failure. During that time, client requests for data on that server transparently retry and eventually succeed after the file server is replaced.")],
  ["replaced automatically within minutes of failure", "transparently retry and eventually succeed"], "FSx for Lustre persistent file systems", "2.2.K11"))
F.append(f("fsx-lustre-scratch-server-failure-io-error-no-replacement", "behavior",
  "On a scratch FSx for Lustre file system, file servers are not replaced if they fail and data is not replicated; files on other servers stay accessible, but clients that access data on the failed server or disk get an immediate I/O error.",
  "What happens when a file server fails on a scratch FSx for Lustre file system?",
  [(UF, "On a scratch file system, file servers aren't replaced if they fail and data isn't replicated. If a file server or a storage disk becomes unavailable on a scratch file system, files stored on other servers are still accessible. If clients try to access data that is on the unavailable server or disk, clients experience an immediate I/O error.")],
  ["file servers aren't replaced if they fail", "immediate I/O error"], "FSx for Lustre scratch file systems", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-use-scratch-for-short-term-persistent-for-long-term", "behavior",
  "Use scratch FSx for Lustre file systems for cost-optimized, short-term, processing-heavy workloads, and persistent file systems for longer-term storage and throughput-focused workloads that run for extended periods and are sensitive to disruptions in availability.",
  "When do you choose scratch or persistent for FSx for Lustre?",
  [(UF, "Use scratch file systems when you need cost-optimized storage for short-term, processing-heavy workloads."),
   (UF, "Use persistent file systems for longer-term storage and for throughput-focused workloads that run for extended periods or indefinitely, and that might be sensitive to disruptions in availability.")],
  ["cost-optimized storage for short-term, processing-heavy workloads", "sensitive to disruptions in availability"],
  "FSx for Lustre deployment types", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-persistent-encrypts-in-transit-automatically", "behavior",
  "Persistent FSx for Lustre deployment types automatically encrypt data in transit when they are accessed from Amazon EC2 instances that support encryption in transit.",
  "Is data in transit encrypted on FSx for Lustre?",
  [(UF, "Persistent deployment types automatically encrypt data in transit when they are accessed from Amazon EC2 instances that support encryption in transit.")],
  ["automatically encrypt data in transit", "instances that support encryption in transit"], "FSx for Lustre persistent file systems", "4.1.K4", rel="extended"))
F.append(f("fsx-lustre-persistent-2-latest-generation-persistent-1-ssd-hdd", "behavior",
  "Persistent 2 is the latest generation of FSx for Lustre persistent deployment type and supports SSD and Intelligent-Tiering storage classes, while Persistent 1 supports SSD and HDD storage classes.",
  "Which storage classes do the Persistent 1 and Persistent 2 FSx for Lustre deployment types support?",
  [(UF, "Persistent 2 is the latest generation of Persistent deployment type, and is best-suited for use cases that require longer-term storage, and that require the highest levels of IOPS and throughput. Persistent 2 file systems support SSD and Intelligent-Tiering storage classes."),
   (UF, "Persistent 1 deployment types support SSD (solid state drive) and HDD (hard disk drive) storage classes.")],
  ["latest generation of Persistent deployment type", "support SSD and Intelligent-Tiering storage classes", "SSD (solid state drive) and HDD"],
  "FSx for Lustre deployment types", "2.2.K11", rel="extended"))
F.append(f("fsx-lustre-ssd-class-sub-millisecond-full-dataset", "behavior",
  "The SSD storage class of FSx for Lustre provides low-latency (sub-millisecond) access to your full dataset, and you pay for the amount of storage you provision.",
  "What does the FSx for Lustre SSD storage class provide?",
  [(UF, "The SSD storage class provides low-latency (sub-millisecond) access to your full dataset. The SSD storage class is provisioned, which means that you specify a file system size and pay storage costs for the amount of storage provisioned.")],
  ["low-latency (sub-millisecond) access to your full dataset", "SSD storage class is provisioned"], "FSx for Lustre storage classes", "4.1.S10", tier0=True))
F.append(f("fsx-lustre-hdd-class-single-digit-ms-optional-ssd-cache", "behavior",
  "The HDD storage class of FSx for Lustre suits workloads that need consistent single-digit millisecond latency across all data, and you can provision an optional SSD read cache sized to 20% of the HDD storage capacity.",
  "What are the latency and cache options of the FSx for Lustre HDD storage class?",
  [(UF, "The HDD storage class can be used with workloads that need consistent single-digit ms latency across all data. You can provision an optional SSD read cache that is sized to 20% of your HDD storage capacity to provide low-latency access to frequently-accessed data.")],
  ["consistent single-digit ms latency", "sized to 20% of your HDD storage capacity"], "FSx for Lustre storage classes", "4.1.S10", rel="extended"))
F.append(f("fsx-lustre-intelligent-tiering-elastic-pay-for-data-stored", "behavior",
  "The FSx for Lustre Intelligent-Tiering storage class provides fully elastic, intelligently tiered storage; you pay for the amount of data you store and do not have to specify a file system size.",
  "How is the FSx for Lustre Intelligent-Tiering storage class sized and billed?",
  [(UF, "The Intelligent-Tiering storage class provides fully elastic, intelligently tiered storage. Elasticity means that you pay for the amount of data you store and do not have to specify a file system size.")],
  ["fully elastic, intelligently tiered storage", "do not have to specify"], "FSx for Lustre storage classes", "4.1.S10", tier0=True))
F.append(f("fsx-lustre-intelligent-tiering-recommended-most-workloads-cache-friendly", "behavior",
  "The Intelligent-Tiering storage class is suitable and recommended for most FSx for Lustre workloads that do not need consistent low latency across the full dataset; the storage class provides the best balance of price and performance for most workloads.",
  "Which FSx for Lustre storage class is recommended for most workloads?",
  [(WI, "The Intelligent-Tiering storage class is suitable and recommended for most workloads that do not need consistent low-latency across your full dataset."),
   (UF, "The Intelligent-Tiering storage class provides the best balance of price and performance for most workloads.")],
  ["suitable and recommended for most workloads", "best balance of price and performance"], "FSx for Lustre storage classes", "4.1.S10", tier0=True))
F.append(f("fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days", "behavior",
  "The Intelligent-Tiering storage class moves data to the Infrequent Access tier after 30 consecutive days without access and to the Archive Instant Access tier after 90 consecutive days, and moves data back to the Frequent Access tier when it is accessed.",
  "How does FSx for Lustre Intelligent-Tiering move data between its access tiers?",
  [(UF, "The Amazon FSx Intelligent-Tiering storage class automatically stores data in three access tiers."),
   (UF, "Data that hasn’t been accessed in 30 consecutive days automatically moves to the Infrequent Access tier, and costs less than data in the Frequent Access tier."),
   (UF, "Data that hasn’t been accessed in 90 consecutive days automatically moves to the Archive Instant Access tier, and costs less than data in the Infrequent Access tier."),
   (UF, "When you access data in the Infrequent Access or Archive Instant Access tiers, the data automatically moves back to the Frequent Access tier.")],
  ["30 consecutive days", "90 consecutive days", "automatically moves back to the Frequent Access tier"],
  "FSx for Lustre Intelligent-Tiering storage class", "4.1.S10", tier0=True))
F.append(f("fsx-lustre-intelligent-tiering-no-extra-retrieval-or-transition-cost", "pricing-dimension",
  "In the Intelligent-Tiering storage class all access to non-cached data has the same performance regardless of tier, and there are no additional IOPS, retrieval or transition costs beyond normal read and write costs.",
  "Are there retrieval or transition charges in FSx for Lustre Intelligent-Tiering?",
  [(UF, "All access to non-cached data has the same performance characteristics, independent of the data's tier, and there are no additional IOPS, retrieval, or transition costs beyond your normal read/write operation costs.")],
  ["no additional IOPS, retrieval, or transition costs", "independent of the data's tier"], "FSx for Lustre Intelligent-Tiering storage class", "4.1.S10", rel="extended"))
F.append(f("fsx-lustre-intelligent-tiering-ssd-read-cache-savings-vs-ssd-hdd", "behavior",
  "With the optional SSD read cache, Intelligent-Tiering file systems can perform at levels comparable to SSD file systems for most workloads while delivering storage cost savings relative to the SSD and HDD storage classes.",
  "When is FSx for Lustre Intelligent-Tiering cheaper than SSD or HDD?",
  [(IT, "As most workloads tend to be read-heavy and actively work with only a small subset of the overall dataset at any given time, the hybrid model of Intelligent-Tiering storage and the SSD read caches allows file systems using the Intelligent-Tiering storage class to provide storage that performs at levels comparable to SSD file systems for most workloads, while delivering storage cost savings relative to the SSD and HDD storage classes.")],
  ["comparable to SSD file systems", "storage cost savings relative to"], "FSx for Lustre Intelligent-Tiering storage class", "4.1.S10", tier0=True))
F.append(f("fsx-lustre-intelligent-tiering-latency-tens-of-ms-vs-cache-sub-ms", "behavior",
  "Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds and per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.",
  "What latency does FSx for Lustre Intelligent-Tiering storage have compared with its SSD read cache?",
  [(IT, "Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds as well as per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.")],
  ["roughly tens of milliseconds", "sub-millisecond latency and no per-request costs"], "FSx for Lustre Intelligent-Tiering storage class", "4.1.S10", rel="extended"))
F.append(f("fsx-lustre-intelligent-tiering-no-s3-data-repository-link", "restriction",
  "Intelligent-Tiering FSx for Lustre file systems don't support linking to Amazon S3 data repositories.",
  "Can an Intelligent-Tiering FSx for Lustre file system be linked to an S3 bucket?",
  [("lus/fsx-data-repositories", "Intelligent-Tiering file systems don't support linking to Amazon S3 data repositories.")],
  ["don't support linking to Amazon S3 data repositories", "Intelligent-Tiering file systems"], "FSx for Lustre Intelligent-Tiering storage class", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-s3-presents-objects-as-files-and-writes-back", "behavior",
  "When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files, imports listings of existing files at file system creation, and can write file system data back to S3.",
  "How does FSx for Lustre integrate with S3?",
  [(WI, "When linked to an Amazon S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files. Amazon FSx imports listings of all existing files in your S3 bucket at file system creation."),
   (WI, "The file system also makes it possible for you to write file system data back to S3.")],
  ["transparently presents S3 objects as files", "write file system data back to S3"], "FSx for Lustre S3 data repository", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-lazy-loaded-from-s3-as-needed", "behavior",
  "With FSx for Lustre linked to an S3 bucket, data is lazy loaded as needed from Amazon S3 for processing jobs.",
  "How does FSx for Lustre load file contents from a linked S3 bucket?",
  [(FAQ, "Data is lazy loaded as needed from Amazon S3 for processing jobs.")],
  ["lazy loaded as needed from Amazon S3", "Data is lazy loaded"], "FSx for Lustre S3 data repository", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-dra-links-directory-to-bucket-or-prefix", "behavior",
  "A link between a directory on the FSx for Lustre file system and an S3 bucket or prefix is called a data repository association (DRA), and you can create it when creating the file system or at any time afterwards.",
  "What is a data repository association in FSx for Lustre?",
  [(DRA, "A link between a directory on the file system and an S3 bucket or prefix is called a *data repository association (DRA)*."),
   (DRA, "You can create the link when creating the file system or at any time after the file system has been created.")],
  ["data repository association (DRA)", "or at any time after"], "FSx for Lustre S3 data repository", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-dra-up-to-8-each-unique-directory-and-prefix", "limit",
  "You can configure a maximum of 8 data repository associations on an FSx for Lustre file system, and each one must have a unique file system directory and a unique S3 bucket or prefix.",
  "Can one FSx for Lustre file system link to several S3 buckets or prefixes?",
  [(DRA, "You can configure a maximum of 8 data repository associations on an FSx for Lustre file system."),
   (DRA, "Each DRA must have a unique FSx for Lustre file system directory and a unique S3 bucket or prefix associated with it.")],
  ["maximum of 8 data repository associations", "unique S3 bucket or prefix"], "per FSx for Lustre file system", "2.2.S8", dm="max", tier0=True))
F.append(f("fsx-lustre-automatic-import-and-export-defaults-console-versus-cli", "default",
  "Automatic import and automatic export (new, changed, deleted) are turned on by default when you add a data repository from the console, but are disabled by default when you use the AWS CLI or the Amazon FSx API.",
  "Are automatic import and export on by default when you link an S3 bucket to FSx for Lustre?",
  [(DRA, "Automatic import (new, changed, deleted) is turned on by default when you add a data repository from the console, but is disabled by default when using the AWS CLI or Amazon FSx API."),
   (DRA, "Automatic export (new, changed, deleted) is turned on by default when you add a data repository from the console, but is disabled by default when using the AWS CLI or Amazon FSx API.")],
  ["turned on by default when you add", "disabled by default when using the AWS CLI"],
  "FSx for Lustre data repository association", "2.2.S8", dm="default", adj=True, tier0=True))
F.append(f("fsx-lustre-automatic-import-export-behavior", "behavior",
  "With automatic import the file system imports file metadata as files are created, modified or deleted in the S3 data repository, and with automatic export it exports file data and metadata as files are created, modified or deleted on the file system.",
  "What do automatic import and automatic export do in FSx for Lustre?",
  [(OV, "When you turn on automatic import for a data repository association, your file system automatically imports file metadata as files are created, modified, and/or deleted in the S3 data repository."),
   (OV, "When you turn on automatic export on a data repository association, your file system automatically exports file data and metadata as files are created, modified, or deleted.")],
  ["automatically imports file metadata", "automatically exports file data and metadata"], "FSx for Lustre data repository association", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-import-same-region-export-standard-class", "restriction",
  "To automatically import updates, the FSx for Lustre file system and the linked S3 bucket must be in the same AWS Region, and S3 objects created by automatic export use the S3 Standard storage class.",
  "What must be true about the Region and what storage class does automatic export use?",
  [("lus/autoimport-data-repo-dra", "The FSx for Lustre file system and the linked S3 bucket must be located in the same AWS Region to automatically import updates."),
   ("lus/autoexport-data-repo-dra", "All S3 objects created by automatic export are written using the S3 Standard storage class.")],
  ["must be located in the same AWS Region", "written using the S3 Standard storage class"], "FSx for Lustre data repository association", "2.2.S8", rel="extended"))
F.append(f("fsx-lustre-conflicting-writes-not-prevented", "restriction",
  "If you modify the same file in both the file system and the S3 bucket you should coordinate at the application level, because FSx for Lustre doesn't prevent conflicting writes in multiple locations.",
  "Does FSx for Lustre resolve conflicting edits made in the file system and in S3?",
  [(DRA, "If you modify the same file in both the file system and the S3 bucket, you should ensure application-level coordination to prevent conflicts. FSx for Lustre doesn't prevent conflicting writes in multiple locations.")],
  ["application-level coordination", "doesn't prevent conflicting writes"], "FSx for Lustre data repository association", "2.2.S8", rel="extended"))
F.append(f("fsx-lustre-auto-export-and-export-tasks-not-simultaneous", "restriction",
  "Automatic import and import data repository tasks can be used simultaneously on a file system, but automatic export and export data repository tasks can't be used simultaneously.",
  "Can automatic export and export tasks run together on an FSx for Lustre file system?",
  [(OV, "Automatic import and import data repository tasks can be used simultaneously on a file system."),
   (OV, "Automatic export and export data repository tasks can't be used simultaneously on a file system.")],
  ["can be used simultaneously", "can't be used simultaneously"], "FSx for Lustre data repository", "4.1.K7", rel="reference"))
F.append(f("fsx-lustre-three-data-repository-task-types-import-export-release", "behavior",
  "There are three types of FSx for Lustre data repository tasks: export tasks copy from the file system to a linked S3 bucket, import tasks copy from the linked bucket to the file system, and release tasks release files that were exported to the bucket.",
  "What are the FSx for Lustre data repository task types?",
  [("lus/data-repository-tasks", "**Export** data repository tasks export from your Lustre file system to a linked S3 bucket."),
   ("lus/data-repository-tasks", "**Import** data repository tasks import from a linked S3 bucket to your Lustre file system."),
   ("lus/data-repository-tasks", "**Release** data repository tasks release files exported to a linked S3 bucket from your Lustre file system.")],
  ["Export** data repository tasks", "release files exported to a linked S3 bucket"], "FSx for Lustre data repository tasks", "4.1.K7", tier0=True))
F.append(f("fsx-lustre-release-frees-space-keeps-metadata-reloads-from-s3", "behavior",
  "A release data repository task frees file system space by removing the local copy of a file's contents while keeping its listing and metadata, and the content is automatically and transparently loaded back from the linked S3 bucket when the file is accessed.",
  "What does releasing a file do in FSx for Lustre?",
  [("lus/file-release", "Releasing a file retains the file listing and metadata, but removes the local copy of that file's contents. If a user or application accesses a released file, the data is automatically and transparently loaded back onto your file system from your linked Amazon S3 bucket.")],
  ["retains the file listing and metadata", "removes the local copy of that file's contents"], "FSx for Lustre data repository tasks", "4.1.K7", tier0=True))
F.append(f("fsx-lustre-backups-persistent-only-not-s3-linked-not-scratch", "restriction",
  "Backups are supported only on FSx for Lustre persistent file systems that are not linked to an Amazon S3 data repository; scratch file systems and S3-linked file systems do not support backups.",
  "Which FSx for Lustre file systems support backups?",
  [(BK, "Backups are supported only on FSx for Lustre persistent file systems that are not linked to an Amazon S3 data repository."),
   (BK, "Backups are not supported on scratch file systems because these file systems are designed for temporary storage and shorter-term processing of data.")],
  ["supported only on FSx for Lustre persistent", "not linked to an Amazon S3 data repository"], "FSx for Lustre backups", "2.2.K11", tier0=True))
F.append(f("fsx-lustre-backups-incremental-stored-in-s3-11-nines", "behavior",
  "FSx for Lustre backups are file-system-consistent, highly durable and incremental, and Amazon FSx stores them in Amazon S3 with 99.999999999% (11 9's) durability.",
  "Where are FSx for Lustre backups stored and how durable are they?",
  [(BK, "Amazon FSx backups are file-system-consistent, highly durable, and incremental. To ensure high durability, Amazon FSx for Lustre stores backups in Amazon Simple Storage Service (Amazon S3) with 99.999999999% (11 9's) durability.")],
  ["file-system-consistent, highly durable, and incremental", "99.999999999% (11 9's) durability"], "FSx for Lustre backups", "2.2.K11", rel="extended"))
F.append(f("fsx-lustre-automatic-daily-backup-default-retention-0-days", "default",
  "For FSx for Lustre you can set the automatic daily backup retention period between 0 and 90 days, and the default retention period is 0 days, which means no automatic daily backups.",
  "What is the default automatic daily backup retention for FSx for Lustre?",
  [(BK, "You can set the retention period to be between 0–90 days. Setting the retention period to 0 (zero) days turns off automatic daily backups. The default retention period for automatic daily backups is 0 days.")],
  ["default retention period for automatic daily backups is 0 days", "between 0–90 days"], "FSx for Lustre automatic daily backups", "2.2.K11", dm="default", adj=True, tier0=True))
F.append(f("fsx-lustre-spot-instances-unmount-before-interruption", "behavior",
  "To keep FSx for Lustre file systems unaffected by EC2 Spot Instance interruptions, AWS recommends unmounting the file system before terminating or hibernating Spot Instances.",
  "How should you handle Spot Instance interruptions when using FSx for Lustre?",
  [("lus/working-with-ec2-spot-instances", "FSx for Lustre can be used with EC2 Spot Instances to significantly lower your Amazon EC2 costs."),
   ("lus/working-with-ec2-spot-instances", "To ensure that Amazon FSx file systems are unaffected by EC2 Spot Instances Interruptions, we recommend unmounting Amazon FSx file systems prior to terminating or hibernating EC2 Spot Instances.")],
  ["can be used with EC2 Spot Instances", "unmounting Amazon FSx file systems"], "FSx for Lustre with Spot Instances", "4.1.K4", rel="extended"))
F.append(f("fsx-lustre-sagemaker-input-source-skips-s3-download", "capability",
  "Amazon FSx for Lustre integrates with Amazon SageMaker AI as an input data source, which accelerates training jobs by eliminating the initial download step from Amazon S3.",
  "How does FSx for Lustre speed up SageMaker AI training jobs?",
  [(WI, "Amazon FSx for Lustre integrates with Amazon SageMaker AI as an input data source. When using SageMaker AI with FSx for Lustre, your machine learning training jobs are accelerated by eliminating the initial download step from Amazon S3.")],
  ["input data source", "eliminating the initial download step from Amazon S3"], "FSx for Lustre integrations", "2.2.S8", tier0=True))
F.append(f("fsx-lustre-aws-batch-and-parallelcluster-integration", "capability",
  "FSx for Lustre integrates with AWS Batch using EC2 Launch Templates, and with AWS ParallelCluster, which can create FSx for Lustre file systems or use existing ones during cluster creation.",
  "Which HPC and batch services integrate with FSx for Lustre?",
  [(WI, "FSx for Lustre integrates with AWS Batch using EC2 Launch Templates."),
   (WI, "FSx for Lustre integrates with AWS ParallelCluster.")],
  ["integrates with AWS Batch", "AWS ParallelCluster"], "FSx for Lustre integrations", "2.2.S8", rel="extended"))
F.append(f("fsx-lustre-encryption-at-rest-automatic-kms-in-transit-supported-instances", "behavior",
  "Amazon FSx automatically encrypts FSx for Lustre file system data at rest using keys managed in AWS KMS, and data in transit is automatically encrypted in certain AWS Regions when accessed from supported EC2 instances.",
  "How are FSx for Lustre data at rest and in transit encrypted?",
  [(WI, "Amazon FSx automatically encrypts file system data at rest using keys managed in AWS Key Management Service (AWS KMS). Data in transit is also automatically encrypted on file systems in certain AWS Regions when accessed from supported Amazon EC2 instances.")],
  ["automatically encrypts file system data at rest", "in certain AWS Regions when accessed from supported"], "FSx for Lustre encryption", "4.1.K4", tier0=True))
emit("facts-behavior-07.json", F)
