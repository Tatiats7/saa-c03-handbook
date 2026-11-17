import sys
sys.path.insert(0, "aws-saa-book/_build/work/23-efs-fsx")
from mk import f, emit

FAQ = "www/efs/faq"
F = []
F.append(f("efs-faq-three-storage-classes-standard-ia-archive", "behavior",
  "Amazon EFS offers three storage classes: EFS Standard, EFS Infrequent Access and EFS Archive, and EFS Archive is optimized for and supported on Regional file systems that use the default Elastic throughput mode.",
  "Which EFS storage classes exist and which file systems support Archive?",
  [(FAQ, "Amazon EFS offers three storage classes: EFS Standard, EFS Infrequent Access, and EFS Archive."),
   (FAQ, "EFS Archive is optimized for and supported on EFS Regional file systems using EFS’s default Elastic Throughput mode.")],
  ["three storage classes", "EFS Standard, EFS Infrequent Access, and EFS Archive", "EFS Regional file systems using EFS’s default"],
  "EFS storage classes", "4.1.K7", tier0=True))
F.append(f("efs-faq-ia-quarter-archive-year-designed-for", "behavior",
  "EFS Infrequent Access is designed for data accessed only a few times a quarter and EFS Archive for data accessed a few times a year or less, and both are cost-optimized classes with low double-digit millisecond latencies.",
  "Which EFS storage class is for data accessed a few times a quarter and which for a few times a year?",
  [(FAQ, "For data that’s infrequently accessed, you can use EFS’s two cost-optimized storage classes that provide low double-digit millisecond latencies: EFS Infrequent Access (IA), designed for data accessed only a few times a quarter, and EFS Archive, designed for data accessed a few times a year or less.")],
  ["a few times a quarter", "a few times a year or less", "low double-digit millisecond latencies"], "EFS storage classes", "4.1.K7", tier0=True))
F.append(f("efs-replication-new-destination-regional-or-one-zone-choice", "capability",
  "When you replicate to a new file system you choose the file system type of the destination, Regional or One Zone, and the KMS key used for encryption.",
  "Can an EFS replica be a One Zone file system?",
  [("efs/create-replication", "When you replicate to a new file system, you choose the file system type and the AWS Key Management Service (AWS KMS) key to use for encryption."),
   ("efs/create-replication", "Choose **One Zone** to create a file system that stores data and metadata redundantly within a single Availability Zone.")],
  ["you choose the file system type", "redundantly within a single Availability Zone"], "EFS replication", "2.2.K11"))
F.append(f("efs-replication-destination-has-no-mount-targets", "behavior",
  "Amazon EFS does not create any mount targets when it creates the replication destination file system.",
  "Does EFS create mount targets on a replication destination file system?",
  [("efs/create-replication", "Additionally, Amazon EFS does not create any mount targets when it creates the destination file system.")],
  ["does not create any mount targets", "destination file system"], "EFS replication", "2.2.K11", rel="extended"))
F.append(f("efs-faq-encryption-minimal-effect-on-io", "behavior",
  "Encrypting data has a minimal effect on EFS I/O latency and throughput.",
  "Does encryption slow down Amazon EFS?",
  [(FAQ, "Encrypting your data has a minimal effect on I/O latency and throughput.")],
  ["minimal effect on I/O latency and throughput", "Encrypting your data"], "Amazon EFS encryption", "3.1.K2", rel="extended"))
F.append(f("efs-posix-permissions-and-no-code-change-for-nfs-apps", "behavior",
  "Amazon EFS supports controlling access to file systems through Portable Operating System Interface (POSIX) permissions.",
  "Can an application that uses a POSIX directory use EFS without code changes?",
  [("efs/whatisefs", "Amazon EFS also supports controlling access to your file systems through Portable Operating System Interface (POSIX) permissions.")],
  ["controlling access to your file systems", "Portable Operating System Interface (POSIX) permissions"], "Amazon EFS", "3.1.K2", rel="extended"))
F.append(f("fsx-windows-vpc-sharing-supported", "capability",
  "FSx for Windows File Server supports VPC sharing, which enables you to view, create, modify and delete resources in a shared subnet in a VPC owned by another AWS account.",
  "Can FSx for Windows File Server be created in a shared VPC?",
  [("win/limit-access-security-groups", "FSx for Windows File Server supports VPC sharing, which enables you to view, create, modify, and delete resources in a shared subnet in a VPC owned by another AWS account.")],
  ["supports VPC sharing", "a VPC owned by another AWS account"], "Amazon FSx for Windows File Server", "4.1.K4", rel="extended"))
F.append(f("fsx-windows-managed-ad-other-vpc-or-account-needs-connectivity", "restriction",
  "If you connect an FSx for Windows File Server file system to an AWS Managed Microsoft AD in a different VPC or account, you must ensure connectivity between that VPC and the VPC where you create the file system.",
  "What is needed to use an AWS Managed Microsoft AD from another VPC or account with FSx for Windows File Server?",
  [("win/fsx-aws-managed-ad", "If you are connecting your Amazon FSx file system to an AWS Managed Microsoft Active Directory in a different VPC or account, then ensure connectivity between that VPC and the Amazon VPC where you want to create the file system.")],
  ["in a different VPC or account", "ensure connectivity between that VPC"], "Amazon FSx for Windows File Server", "2.2.S7", rel="extended"))
F.append(f("fsx-windows-resource-forest-one-way-trust", "capability",
  "To isolate FSx file systems in a separate Active Directory forest from your users, you join the file system to an AWS Managed Microsoft AD and establish a one-way forest trust with your existing self-managed Active Directory domain.",
  "How do you isolate FSx for Windows File Server resources in a separate Active Directory forest?",
  [("win/fsx-aws-managed-ad", "You then establish a one-way forest trust relationship between an AWS Managed Microsoft AD domain that you create and your existing self-managed Active Directory domain.")],
  ["one-way forest trust relationship", "self-managed Active Directory domain"], "Amazon FSx for Windows File Server", "2.2.S7", rel="extended"))
F.append(f("fsx-windows-aws-backup-centralized-backup-option", "capability",
  "For FSx for Windows File Server you can use AWS Backup as part of a centralized backup solution for your AWS resources.",
  "Can AWS Backup protect FSx for Windows File Server file systems?",
  [("win/using-backups", "You can also use AWS Backup as part of a centralized backup solution for your AWS resources.")],
  ["use AWS Backup as part of", "centralized backup solution"], "FSx for Windows File Server backups", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-aws-backup-uses-builtin-fsx-backup-functionality", "behavior",
  "AWS Backup uses the built-in backup functionality of Amazon FSx.",
  "Does AWS Backup work with FSx for ONTAP volume backups?",
  [("ont/using-backups", "AWS Backup uses the built-in backup functionality of Amazon FSx.")],
  ["built-in backup functionality of Amazon FSx", "AWS Backup uses"], "FSx for ONTAP backups", "2.2.K11", rel="extended"))
F.append(f("fsx-ontap-backup-logically-air-gapped-vault-aws-backup", "capability",
  "You can store FSx for ONTAP volume backups created by AWS Backup in a logically air-gapped vault, a specialized AWS Backup vault that is encrypted and protected by AWS Backup Vault Lock in compliance mode.",
  "How can FSx for ONTAP backups be protected from deletion in an isolated vault?",
  [("ont/using-backups", "You can store FSx for ONTAP volume backups created by AWS Backup in a logically air-gapped vault. A logically air-gapped vault is a specialized AWS Backup vault that provides increased security beyond a standard backup vault. Each vault is encrypted and is protected by AWS Backup Vault Lock in compliance mode, which prevents backups from being deleted or altered before the end of their retention period.")],
  ["logically air-gapped vault", "AWS Backup Vault Lock in compliance mode"], "FSx for ONTAP backups", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-backup-copy-cross-region-manual-and-aws-backup", "capability",
  "Amazon FSx lets you manually copy FSx for ONTAP volume backups to another AWS Region or within the same Region, within the same AWS account, and you can use AWS Backup to copy backups across Regions and across accounts.",
  "How can FSx for ONTAP backups be copied to another Region or account?",
  [("ont/copy-backups", "With Amazon FSx, you can manually copy volume backups to another AWS Region (cross-Region copies) or within the same AWS Region (in-Region copies). Both copy types operate within the same AWS account."),
   ("ont/copy-backups", "You can also use AWS Backup to copy backups across AWS Regions and across AWS accounts.")],
  ["another AWS Region (cross-Region copies)", "across AWS Regions and across AWS accounts"], "FSx for ONTAP backups", "2.2.K11", tier0=True))
F.append(f("fsx-ontap-block-storage-iscsi-luns-nvme-namespaces-san", "capability",
  "Amazon FSx for NetApp ONTAP supports the iSCSI and NVMe over TCP (NVMe/TCP) block storage protocols; you configure storage by creating LUNs for iSCSI and namespaces for NVMe, and hosts access them using iSCSI or TCP protocols.",
  "Which block storage protocols does FSx for ONTAP support and what do you create for each?",
  [
   ("ont/supported-fsx-clients", "Amazon FSx for NetApp ONTAP supports the Internet Small Computer Systems Interface (iSCSI) and Non-Volatile Memory Express (NVMe) over TCP (NVMe/TCP) block storage protocols."),
   ("ont/supported-fsx-clients", "You configure storage by creating LUNs for iSCSI and by creating namespaces for NVMe. LUNs and namespaces are then accessed by hosts using iSCSI or TCP protocols.")],
  ["iSCSI) and Non-Volatile Memory Express (NVMe)", "creating LUNs for iSCSI", "creating namespaces for NVMe"], "Amazon FSx for NetApp ONTAP block storage", "2.2.S8", tier0=True))
emit("facts-behavior-10.json", F)
