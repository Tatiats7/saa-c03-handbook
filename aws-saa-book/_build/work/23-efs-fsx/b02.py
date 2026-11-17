import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

W = "efs/whatisefs"; H = "efs/how-it-works"; FE = "efs/features"; MF = "efs/mounting-fs"; LC = "efs/lifecycle-management-efs"
P = "efs/performance"; MT = "efs/managing-throughput"; FAQ = "www/efs/faq"; DS = "efs/trnsfr-data-using-datasync"
F = []
F.append(f("efs-mount-helper-recommended-nfs-alternative", "behavior",
  "AWS recommends the EFS mount helper for mounting EFS file systems on EC2 Linux and Mac instances; as an alternative you can mount manually with the standard Linux NFS client.",
  "How do you mount an EFS file system, and what does AWS recommend?",
  [(MF, "To mount EFS file systems, we recommend that you use the EFS mount helper."),
   (MF, "Alternatively, you can manually mount EFS file systems using the standard Linux NFS client.")],
  ["use the EFS mount helper", "standard Linux NFS client"], "Amazon EFS clients", "3.1.K2", tier0=True))
F.append(f("efs-automount-at-instance-start", "capability",
  "You can use the EFS mount helper or NFS to configure an EC2 instance to mount an EFS file system automatically when the instance starts.",
  "Can an EC2 instance mount EFS automatically at start?",
  [(MF, "Additionally, you can use the EFS mount helper or NFS to configure an EC2 instance to automatically mount an EFS file system when the instance starts.")],
  ["automatically mount an EFS file system", "when the instance starts"], "Amazon EFS clients", "3.1.K2", rel="extended"))
F.append(f("efs-mount-helper-tls-option-encrypts-nfs-traffic", "behavior",
  "When encryption of data in transit is declared as a mount option, Amazon EFS establishes a secure TLS connection when the file system is mounted, and all NFS traffic is routed through it.",
  "How does the mount helper's TLS option protect data in transit?",
  [("efs/encryption-in-transit", "When encryption of data in transit is declared as a mount option for your EFS file system, Amazon EFS establishes a secure TLS connection with your EFS file system upon mounting your file system. All NFS traffic is routed through this encrypted connection.")],
  ["establishes a secure TLS connection", "All NFS traffic is routed", "declared as a mount option"], "Amazon EFS encryption in transit", ["3.1.K2", "3.1.K3"], tier0=True))
F.append(f("efs-encryption-in-transit-tls", "capability",
  "Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS).",
  "Which protocol encrypts EFS data in transit?",
  [("efs/encryption-in-transit", "Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS).")],
  ["encryption of data in transit", "Transport Layer Security (TLS)"], "Amazon EFS encryption in transit", "3.1.K2"))
F.append(f("efs-two-forms-encryption-when-enabled", "behavior",
  "Amazon EFS supports encryption in transit and encryption at rest; you enable encryption at rest when you create the file system, which encrypts all data and metadata, and you enable encryption in transit when you mount it.",
  "When do you enable each form of EFS encryption?",
  [(W, "Amazon EFS supports two forms of encryption for file systems: encryption in transit and encryption at rest. You can enable encryption at rest when creating an EFS file system. If you do, all of your data and metadata is encrypted. You can enable encryption in transit when you mount the file system.")],
  ["enable encryption at rest when creating", "enable encryption in transit when you mount", "all of your data and metadata is encrypted"],
  "Amazon EFS encryption", "3.1.K2", tier0=True))
F.append(f("efs-region-property-for-cross-region-mount", "restriction",
  "To mount an EFS file system from an EC2 instance in a different AWS Region than the file system, you must edit the region property in the efs-utils.conf file.",
  "What must you change to mount an EFS file system from another Region?",
  [("efs/mount-different-region", "To mount your EFS file system from an EC2 instance that is in a different AWS Region than the file system, you must edit the `region` property value in the `efs-utils.conf` file.")],
  ["different AWS Region than the file system", "efs-utils.conf"], "Amazon EFS, cross-Region mount", "3.1.K2"))
F.append(f("efs-other-account-or-vpc-resolve-mount-target-manually", "restriction",
  "By default the EFS mount helper uses DNS to resolve the mount target IP address, so when you mount from a different account or VPC you need to resolve the mount target manually.",
  "What is needed to mount an EFS file system from another VPC or account?",
  [("efs/manage-fs-access-vpc-peering", "By default, the EFS mount helper uses domain name service (DNS) to resolve the IP address of your EFS mount target. If you are mounting the file system from a different account or virtual private cloud (VPC), you need to resolve the EFS mount target manually.")],
  ["a different account or virtual private cloud", "resolve the EFS mount target manually"], "Amazon EFS, cross-account or cross-VPC mount", "3.1.K2"))
F.append(f("efs-datasync-copies-between-storage-types-incl-efs", "capability",
  "AWS DataSync can copy data between NFS and SMB file servers, self-managed object storage, AWS Snowball Edge, Amazon S3 buckets, EFS file systems, and FSx for Windows File Server file systems.",
  "Which AWS service moves existing data into EFS from other storage?",
  [(DS, "DataSync can copy data between Network File System (NFS), Server Message Block (SMB) file servers, self-managed object storage, AWS Snowball Edge, Amazon S3 buckets, EFS file systems, and FSx for Windows File Server file systems.")],
  ["Amazon S3 buckets, EFS file systems", "FSx for Windows File Server file systems"], "AWS DataSync with EFS", "3.1.K2", tier0=True))
F.append(f("efs-datasync-between-efs-regions-and-accounts", "capability",
  "You can use DataSync to transfer files between two EFS file systems, including file systems in different AWS Regions and file systems owned by different AWS accounts.",
  "Can data be copied between EFS file systems in different Regions or accounts?",
  [(DS, "You can also use DataSync to transfer files between two EFS file systems, including file systems in different AWS Regions and file systems owned by different AWS accounts.")],
  ["between two EFS file systems", "different AWS Regions", "owned by different AWS accounts"], "AWS DataSync with EFS", "3.1.K2"))
F.append(f("efs-datasync-recommended-for-onpremises-file-data", "capability",
  "AWS DataSync is the fast and simple way to sync existing on-premises file systems into EFS, and it works over any network, including AWS Direct Connect.",
  "Which service copies existing on-premises file data to Amazon EFS?",
  [(FAQ, "AWS DataSync provides a fast and simple way to securely sync existing file systems into EFS and works over any network, including AWS Direct Connect.")],
  ["fast and simple way to securely sync", "including AWS Direct Connect"], "AWS DataSync with EFS", "3.1.K2", tier0=True))
F.append(f("efs-datasync-up-to-10-times-faster-than-linux-copy", "capability",
  "Over Direct Connect, DataSync can copy data into EFS up to 10 times faster than standard Linux copy tools.",
  "How much faster than standard Linux copy tools can DataSync copy data into EFS?",
  [(FAQ, "Once mounted, you can use DataSync to copy data into EFS up to 10 times faster than standard Linux copy tools.")],
  ["up to 10 times faster", "standard Linux copy tools"], "AWS DataSync with EFS", "3.1.K2", dm="max", rel="extended"))
F.append(f("efs-transfer-family-sftp-ftps-ftp-same-region", "capability",
  "AWS Transfer Family is a fully managed file transfer service for SFTP, FTPS and FTP, and the data that end users upload and download over those protocols is stored in the EFS file system; Transfer Family endpoints must be in the same Region as the file system.",
  "Which service gives SFTP or FTP access to an EFS file system, and where must its endpoint be?",
  [(FAQ, "AWS Transfer Family is a fully managed file transfer service that provides support for Secure File Transfer Protocol (SFTP), File Transfer Protocol over SSL (FTPS), and File Transfer Protocol (FTP)."),
   (FAQ, "AWS Transfer Family endpoints must be in the same Region as your Amazon EFS file system.")],
  ["fully managed file transfer service", "must be in the same Region", "SFTP, FTPS"], "AWS Transfer Family with EFS", "3.1.K2", rel="extended"))
F.append(f("efs-file-locking-nfsv4-byte-range", "capability",
  "NFS client applications can use NFS version 4 file locking, including byte-range locking, for read and write operations on EFS files.",
  "Which file locking does Amazon EFS support?",
  [(FE, "NFS client applications can use NFS version 4 file locking (including byte-range locking) for read and write operations on Amazon EFS files.")],
  ["NFS version 4 file locking", "including byte-range locking"], "Amazon EFS file locking", "3.1.K2", tier0=True))
F.append(f("efs-advisory-locking-only", "restriction",
  "Amazon EFS supports only advisory locking, and read and write operations do not check for conflicting locks before they run.",
  "Does EFS enforce file locks on reads and writes?",
  [(FE, "Amazon EFS only supports advisory locking and read/write operations don’t check for conflicting locks before executing.")],
  ["only supports advisory locking", "don’t check for conflicting locks"], "Amazon EFS file locking", "3.1.K2"))
F.append(f("efs-close-to-open-consistency", "behavior",
  "Amazon EFS provides the close-to-open consistency semantics that applications expect from NFS.",
  "Which consistency semantics does EFS provide?",
  [(FE, "Amazon EFS provides the close-to-open consistency semantics that applications expect from NFS.")],
  ["close-to-open consistency semantics", "applications expect from NFS"], "Amazon EFS", "3.1.K2", rel="extended"))
F.append(f("efs-file-system-id-globally-unique-names-not", "behavior",
  "Every EFS file system has an automatically generated ID that is globally unique; file system names are tags and do not need to be unique, so they are not global like S3 bucket names.",
  "Are EFS file system names global like S3 bucket names?",
  [(FAQ, "Every file system has an automatically generated ID number that is globally unique. You can tag your file system with a name, and these names don’t need to be unique.")],
  ["automatically generated ID number", "names don’t need to be unique", "globally unique"], "Amazon EFS file system", "3.1.K2", rel="extended"))
F.append(f("efs-standard-class-ssd-lowest-latency-new-data-first", "behavior",
  "The EFS Standard storage class uses SSD storage for the lowest latency for frequently accessed files, and new file system data is written to Standard first before lifecycle management can tier it to IA or Archive.",
  "Where is new data written in EFS, and which class is for frequently accessed files?",
  [(FE, "New file system data is first written to the EFS Standard storage class and then can be tiered to the EFS Infrequent Access and EFS Archive storage classes by using lifecycle management.")],
  ["first written to the EFS Standard storage class", "tiered to the EFS Infrequent Access"], "EFS storage classes", "4.1.K7", tier0=True))
F.append(f("efs-archive-needs-elastic-throughput-no-bursting-provisioned", "restriction",
  "The EFS Archive storage class is supported on file systems with Elastic throughput, and if a lifecycle policy transitions data to Archive you cannot change the throughput mode to Bursting or Provisioned.",
  "Which throughput modes work with the EFS Archive storage class?",
  [(FE, "The EFS Archive storage class is supported on EFS file systems with Elastic throughput. If your file system has a lifecycle policy that transitions data to Archive, you cannot change the throughput mode to Bursting or Provisioned.")],
  ["supported on EFS file systems with Elastic throughput", "cannot change the throughput mode"], "EFS Archive storage class", ["4.1.K7", "3.1.S1"], tier0=True))
F.append(f("efs-ia-archive-billed-per-class-plus-access-charges", "pricing-dimension",
  "You are billed for the amount of data in each EFS storage class, and you are also billed data access charges when files in IA or Archive are read or when data transitions between classes through lifecycle management.",
  "What are you billed for when you use EFS IA and Archive storage?",
  [(FE, "You are billed for the amount of data in each storage class. You are also billed data access charges when files in IA or Archive storage are read, or for data that transitions between storage classes using lifecycle management.")],
  ["data in each storage class", "billed data access charges"],
  "EFS storage classes", "4.1.K7", tier0=True))
F.append(f("efs-no-data-access-charges-with-aws-backup", "pricing-dimension",
  "You do not incur data access charges when you use AWS Backup to back up lifecycle-management-enabled EFS file systems.",
  "Does AWS Backup of a lifecycle-managed EFS file system incur data access charges?",
  [(FE, "You don't incur data access charges when using AWS Backup to back up lifecycle management-enabled EFS file systems.")],
  ["don't incur data access charges", "AWS Backup to back up"], "EFS storage classes and AWS Backup", "4.1.K7", rel="extended"))
F.append(f("efs-ia-no-minimum-storage-duration-archive-90-days", "pricing-dimension",
  "EFS IA has no minimum storage duration, but data tiered to EFS Archive has a minimum storage duration of 90 days.",
  "Is there a minimum storage duration for EFS IA and EFS Archive?",
  [(FAQ, "EFS IA has no minimum storage duration. Data that is tiered to EFS Archive has a minimum storage duration of 90 days.")],
  ["EFS IA has no minimum storage duration", "minimum storage duration of 90 days"], "EFS IA and EFS Archive", "4.1.K7", rel="extended"))
F.append(f("efs-lifecycle-policy-applies-to-entire-file-system", "behavior",
  "EFS lifecycle policies apply to the entire file system.",
  "Do EFS lifecycle policies apply to single files or to the whole file system?",
  [(LC, "Lifecycle policies apply to the entire EFS file system.")],
  ["apply to the entire EFS file system", "Lifecycle policies apply"], "EFS lifecycle management", "4.1.K7", rel="extended"))
F.append(f("efs-lifecycle-transition-based-on-last-access-timer-reset", "behavior",
  "EFS lifecycle transition time is based on when a file was last accessed in the Standard storage class, and the lifecycle timer is reset whenever a file in Standard is accessed.",
  "What does an EFS lifecycle policy measure to decide when to move a file?",
  [(LC, "Transition time is based on when the files were last accessed in the Standard storage class."),
   (LC, "Whenever a file in Standard is accessed, the lifecycle management timer is reset.")],
  ["last accessed in the Standard storage class", "lifecycle management timer is reset"], "EFS lifecycle management", "4.1.K7", tier0=True))
F.append(f("efs-lifecycle-default-ia-after-30-days", "default",
  "By default, files not accessed in the Standard storage class for 30 days are transitioned into IA.",
  "After how many days without access does the default EFS lifecycle policy move files to IA?",
  [(LC, "By default, files that are not accessed in Standard storage fclass or 30 days are transitioned into IA.")],
  ["30 days", "transitioned into IA"], "EFS lifecycle policy, Transition into IA", "4.1.K7", dm="default", adj=True, tier0=True))
F.append(f("efs-lifecycle-default-archive-after-90-days", "default",
  "By default, files not accessed in the Standard storage class for 90 days are transitioned into the Archive storage class.",
  "After how many days without access does the default EFS lifecycle policy move files to Archive?",
  [(LC, "By default, files that are not accessed in the Standard storage class for 90 days are transitioned in to the Archive storage class.")],
  ["90 days", "transitioned in to the Archive storage class"], "EFS lifecycle policy, Transition into Archive", "4.1.K7", dm="default", adj=True, tier0=True))
F.append(f("efs-lifecycle-default-no-move-back-to-standard", "default",
  "By default, files are not moved back to the Standard storage class when they are accessed in IA or Archive; they stay in the IA or Archive storage class.",
  "Are files moved back to EFS Standard when they are read from IA or Archive?",
  [(LC, "By default, files are not moved back to the Standard storage class, and they remain in the IA or Archive storage class when they are accessed.")],
  ["not moved back to the Standard storage class", "remain in the IA or Archive storage class"], "EFS lifecycle policy, Transition into Standard", "4.1.K7", dm="default", adj=True, tier0=True))
F.append(f("efs-lifecycle-transition-to-standard-on-first-access", "capability",
  "For performance-sensitive use cases that need the fastest latency, such as applications with many small files, you can set the lifecycle policy to transition files back into Standard storage on first access.",
  "How do you move a file back to EFS Standard when it is read?",
  [(LC, "For performance-sensitive use cases that demand the fastest latency performance (such as applications that work with a large volume of small files), choose to transition files into Standard storage **On first access**.")],
  ["fastest latency performance", "transition files into Standard storage"], "EFS lifecycle policy, Transition into Standard", "4.1.K7", rel="extended"))
F.append(f("efs-lifecycle-faq-intelligent-tiering-promotes-on-access", "capability",
  "You can enable EFS Intelligent-Tiering to promote files from EFS IA and EFS Archive back to EFS Standard when they are accessed.",
  "How can accessed files return from IA or Archive to EFS Standard?",
  [(FAQ, "You can also enable EFS Intelligent-Tiering to promote files from EFS IA and EFS Archive back to EFS Standard when they are accessed, which provides subsequent reads of those files with the faster, sub-millisecond latencies of EFS Standard.")],
  ["enable EFS Intelligent-Tiering", "back to EFS Standard when they are accessed"], "EFS lifecycle management", "4.1.K7", rel="extended"))
F.append(f("efs-metadata-always-stored-in-standard", "behavior",
  "File metadata, including file names, ownership information and the directory structure, is always stored in the Standard storage class.",
  "Which storage class holds EFS file metadata?",
  [(LC, "File metadata, including file names, ownership information, and file system directory structure, is always stored in Standard to help ensure consistent metadata performance.")],
  ["always stored in Standard", "file names, ownership information"], "EFS lifecycle management", "4.1.K7", rel="extended"))
F.append(f("efs-metadata-operations-do-not-count-as-access", "behavior",
  "Metadata operations on files in IA or Archive storage, such as listing the contents of a directory, do not count as file access.",
  "Does listing a directory reset the lifecycle timer of files in IA or Archive?",
  [(LC, "Metadata operations for file systems in IA or Archive storage, such as listing the contents of a directory, don't count as file access.")],
  ["listing the contents of a directory", "don't count as file access"], "EFS lifecycle management", "4.1.K7", rel="extended"))
F.append(f("efs-writes-to-ia-archive-go-to-standard-first", "behavior",
  "All write operations to files in IA or Archive are first written to Standard storage, and the data becomes eligible to transition again after 24 hours.",
  "What happens to a write to a file that is stored in EFS IA or Archive?",
  [(LC, "All write operations to files in the file system's IA or Archive storage classes are first written to Standard storage classes, and are then eligible to be transitioned to the applicable storage class after 24 hours.")],
  ["first written to Standard storage classes", "after 24 hours"], "EFS lifecycle management", "4.1.K7", rel="extended"))
F.append(f("efs-lifecycle-operations-lower-priority-than-workload", "behavior",
  "File system operations for lifecycle management have a lower priority than operations for the EFS file system workload.",
  "Do lifecycle transitions compete with application I/O on EFS?",
  [(LC, "File system operations for lifecycle management have a lower priority than operations for EFS file system workloads.")],
  ["have a lower priority", "lifecycle management"], "EFS lifecycle management", "4.1.K7", rel="reference"))
emit("facts-behavior-02.json", F)
