facts card: 869 facts
efs-access-point-enforces-posix-user-and-root-directory
  claim: An EFS access point can enforce a user identity, including POSIX groups, for all requests made through it, and can enforce a different root directory so clients can access only that directory and its subdirectories.
  scope: EFS access point.
  link: [enforce a user identity](../facts/efs.md#efs-access-point-enforces-posix-user-and-root-directory)
  link: [enforce a different root directory](../facts/efs.md#efs-access-point-enforces-posix-user-and-root-directory)
  link: [specified directory or its subdirectories](../facts/efs.md#efs-access-point-enforces-posix-user-and-root-directory)
efs-access-point-faq-configure-os-user-group-root-directory
  claim: When you create an EFS access point you can configure an operating system user and group, and a root directory, for all connections that use it.
  scope: EFS access point.
  link: [operating system user and group](../facts/efs.md#efs-access-point-faq-configure-os-user-group-root-directory)
  link: [a root directory for all connections](../facts/efs.md#efs-access-point-faq-configure-os-user-group-root-directory)
efs-access-point-faq-root-directory-auto-created-first-connect
  claim: If you specify the root directory's owner, EFS creates the access point root directory with the permissions you provide the first time a client connects.
  scope: EFS access point.
  link: [automatically create it](../facts/efs.md#efs-access-point-faq-root-directory-auto-created-first-connect)
  link: [the first time a client connects](../facts/efs.md#efs-access-point-faq-root-directory-auto-created-first-connect)
efs-access-point-iam-policy-enforces-specific-access-point
  claim: You can use IAM policies to enforce that specific applications use a specific access point.
  scope: EFS access point.
  link: [specific applications use a specific access point](../facts/efs.md#efs-access-point-iam-policy-enforces-specific-access-point)
  link: [IAM) policies](../facts/efs.md#efs-access-point-iam-policy-enforces-specific-access-point)
efs-access-point-mount-with-mount-helper-tls
  claim: You use the EFS mount helper when mounting a file system through an access point, and the mount command includes the file system ID, the access point ID and the tls mount option.
  scope: EFS access point.
  link: [use the EFS mount helper](../facts/efs.md#efs-access-point-mount-with-mount-helper-tls)
  link: [the access point ID](../facts/efs.md#efs-access-point-mount-with-mount-helper-tls)
efs-access-point-needs-mount-target-first
  claim: You must create at least one mount target in your VPC before using access points, because mount targets provide network connectivity while access points provide access control.
  scope: EFS access point.
  link: [create at least one mount target](../facts/efs.md#efs-access-point-needs-mount-target-first)
  link: [provide the network connectivity](../facts/efs.md#efs-access-point-needs-mount-target-first)
  link: [provide the access control](../facts/efs.md#efs-access-point-needs-mount-target-first)
efs-advisory-locking-only
  claim: Amazon EFS supports only advisory locking, and read and write operations do not check for conflicting locks before they run.
  scope: Amazon EFS file locking.
  link: [only supports advisory locking](../facts/efs.md#efs-advisory-locking-only)
  link: [don’t check for conflicting locks](../facts/efs.md#efs-advisory-locking-only)
efs-allows-connections-from-any-source-port
  claim: To support a broad set of NFS clients, Amazon EFS allows connections from any source port.
  scope: EFS mount target network access.
  link: [allows connections from any source port](../facts/efs.md#efs-allows-connections-from-any-source-port)
  link: [broad set of NFS clients](../facts/efs.md#efs-allows-connections-from-any-source-port)
efs-archive-needs-elastic-throughput-no-bursting-provisioned
  claim: The EFS Archive storage class is supported on file systems with Elastic throughput, and if a lifecycle policy transitions data to Archive you cannot change the throughput mode to Bursting or Provisioned.
  scope: EFS Archive storage class.
  link: [supported on EFS file systems with Elastic throughput](../facts/efs.md#efs-archive-needs-elastic-throughput-no-bursting-provisioned)
  link: [cannot change the throughput mode](../facts/efs.md#efs-archive-needs-elastic-throughput-no-bursting-provisioned)
efs-automount-at-instance-start
  claim: You can use the EFS mount helper or NFS to configure an EC2 instance to mount an EFS file system automatically when the instance starts.
  scope: Amazon EFS clients.
  link: [automatically mount an EFS file system](../facts/efs.md#efs-automount-at-instance-start)
  link: [when the instance starts](../facts/efs.md#efs-automount-at-instance-start)
efs-backup-cli-api-default-only-one-zone
  claim: When you create a file system with the CLI or API, automatic backups are enabled by default only for One Zone file systems.
  scope: EFS automatic backups; default; adjustable.
  link: [enabled by default only for One Zone](../facts/efs.md#efs-backup-cli-api-default-only-one-zone)
  link: [automatically backed up by AWS Backup by default](../facts/efs.md#efs-backup-cli-api-default-only-one-zone)
efs-backup-incremental-and-restore-to-standard
  claim: AWS Backup backs up all data in an EFS file system whatever storage class the data is in, performs incremental backups of EFS file systems, and restores all files to the Standard storage class when you restore a recovery point.
  scope: EFS backups with AWS Backup.
  link: [whatever storage class the data is in](../facts/efs.md#efs-backup-incremental-and-restore-to-standard)
  link: [restored to the Standard storage class](../facts/efs.md#efs-backup-incremental-and-restore-to-standard)
  link: [incremental backups of EFS file systems](../facts/efs.md#efs-backup-incremental-and-restore-to-standard)
efs-backup-modifications-during-backup-may-be-inconsistent
  claim: You can modify an EFS file system while a backup runs, but inconsistencies such as duplicated, skewed, or excluded data can occur if you make modifications during the backup.
  scope: EFS backups with AWS Backup.
  link: [duplicated, skewed, or excluded data](../facts/efs.md#efs-backup-modifications-during-backup-may-be-inconsistent)
  link: [modify your EFS file systems while](../facts/efs.md#efs-backup-modifications-during-backup-may-be-inconsistent)
efs-backup-on-by-default-in-console
  claim: When you create an EFS file system in the console, automatic backups are turned on by default.
  scope: EFS automatic backups; default; adjustable.
  link: [automatic backups are turned on by default](../facts/efs.md#efs-backup-on-by-default-in-console)
  link: [using the Amazon EFS console](../facts/efs.md#efs-backup-on-by-default-in-console)
efs-backup-onezone-enabled-by-default-faq
  claim: EFS Backups are enabled by default for all EFS One Zone file systems.
  scope: One Zone file system; default; adjustable.
  link: [enabled by default for all EFS One Zone](../facts/efs.md#efs-backup-onezone-enabled-by-default-faq)
  link: [EFS Backups](../facts/efs.md#efs-backup-onezone-enabled-by-default-faq)
efs-backup-plan-and-vault-cannot-be-deleted
  claim: The default EFS backup plan and the default EFS backup vault cannot be deleted.
  scope: EFS default backup plan.
  link: [backup plan and backup vault cannot be deleted](../facts/efs.md#efs-backup-plan-and-vault-cannot-be-deleted)
  link: [cannot be deleted](../facts/efs.md#efs-backup-plan-and-vault-cannot-be-deleted)
efs-backup-restore-new-or-existing-full-or-item-level
  claim: You can restore EFS backup data to either a new or an existing file system, and you can choose a full restore or an item-level restore.
  scope: EFS backups with AWS Backup.
  link: [either a new or existing file system](../facts/efs.md#efs-backup-restore-new-or-existing-full-or-item-level)
  link: [full restore or an item-level restore](../facts/efs.md#efs-backup-restore-new-or-existing-full-or-item-level)
efs-block-public-access-default-no-public-access
  claim: By default, new EFS file systems do not allow public access, but you can modify file system policies to allow public access.
  scope: EFS block public access; default; adjustable.
  link: [new EFS file systems don't allow public access](../facts/efs.md#efs-block-public-access-default-no-public-access)
  link: [modify file system policies to allow public access](../facts/efs.md#efs-block-public-access-default-no-public-access)
efs-block-public-access-prevents-public-resource-policies
  claim: Enabling Block Public Access protects EFS resources by preventing public access from being granted through the resource policies that are directly attached to the file system.
  scope: EFS block public access.
  link: [preventing public access from being granted](../facts/efs.md#efs-block-public-access-prevents-public-resource-policies)
  link: [resource policies that are directly attached](../facts/efs.md#efs-block-public-access-prevents-public-resource-policies)
efs-burst-example-100gib
  claim: A file system with 100 GiB of metered data in Standard storage can burst to 300 MiBps read-only or 100 MiBps write-only for up to 72 minutes per day, and drive up to 15 MiBps read-only or 5 MiBps write-only continuously.
  scope: file system with 100 GiB of metered data in Standard storage, Bursting throughput; maximum; not adjustable.
  link: [72 minutes per day](../facts/efs.md#efs-burst-example-100gib)
  link: [15 MiBps](../facts/efs.md#efs-burst-example-100gib)
efs-burst-example-10tib
  claim: A file system with 10 TiB of metered data in Standard storage can burst to 3 GiBps read-only or 1 GiBps write-only for 12 hours per day, and drive 1.5 GiBps read-only or 500 MiBps write-only continuously.
  scope: file system with 10 TiB of metered data in Standard storage, Bursting throughput; maximum; not adjustable.
  link: [3 GiBps](../facts/efs.md#efs-burst-example-10tib)
  link: [1.5 GiBps](../facts/efs.md#efs-burst-example-10tib)
efs-burst-example-1tib
  claim: A file system with 1 TiB of metered data in Standard storage can burst to 300 MiBps read-only or 100 MiBps write-only for 12 hours per day, and drive 150 MiBps read-only or 50 MiBps write-only continuously.
  scope: file system with 1 TiB of metered data in Standard storage, Bursting throughput; maximum; not adjustable.
  link: [12 hours per day](../facts/efs.md#efs-burst-example-1tib)
  link: [150 MiBps](../facts/efs.md#efs-burst-example-1tib)
efs-bursting-base-rate-per-gib
  claim: With Bursting throughput, the base throughput is proportionate to the file system's size in the Standard storage class, at a rate of 50 KiBps per each GiB of storage.
  scope: per GiB of Standard storage; fixed; not adjustable.
  link: [50 KiBps per each GiB](../facts/efs.md#efs-bursting-base-rate-per-gib)
efs-bursting-burst-rate-with-credits
  claim: When burst credits are available, a file system can drive throughput up to 100 MiBps per TiB in Standard storage (100 KiBps per GiB), up to the AWS Region limit, with a minimum of 100 MiBps.
  scope: per TiB of Standard storage; maximum; not adjustable; burst credits available; up to the AWS Region limit.
  link: [100 MiBps per TiB](../facts/efs.md#efs-bursting-burst-rate-with-credits)
efs-bursting-credits-accrue-below-base-and-deducted-above
  claim: With Bursting throughput, burst credits accrue when the file system consumes below its base throughput rate and are deducted when throughput exceeds the base rate.
  scope: EFS Bursting throughput.
  link: [Burst credits accrue](../facts/efs.md#efs-bursting-credits-accrue-below-base-and-deducted-above)
  link: [deducted when throughput exceeds the base rate](../facts/efs.md#efs-bursting-credits-accrue-below-base-and-deducted-above)
efs-bursting-credits-allow-up-to-12-hours-continuous-burst
  claim: File systems can accumulate enough burst credits to burst for up to 12 hours continuously.
  scope: EFS Bursting throughput; maximum.
  link: [burst for up to 12 hours continuously](../facts/efs.md#efs-bursting-credits-allow-up-to-12-hours-continuous-burst)
  link: [accumulate enough credits](../facts/efs.md#efs-bursting-credits-allow-up-to-12-hours-continuous-burst)
efs-bursting-large-file-systems-burst-half-time
  claim: File systems larger than 1 TiB can always burst for up to 50 percent of the time if they are inactive for the remaining 50 percent of the time.
  scope: Bursting throughput, file systems larger than 1 TiB; maximum; inactive for the remaining 50 percent of the time.
  link: [50 percent of the time](../facts/efs.md#efs-bursting-large-file-systems-burst-half-time)
efs-bursting-max-throughput-major-regions
  claim: Total Bursting throughput for a Regional or One Zone file system in US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Sydney) and Europe (Ireland) is a maximum read of 5 GiBps and a maximum write of 3 GiBps.
  scope: per Regional or One Zone file system, for all connected clients, in the listed Regions; maximum; not adjustable.
  link: [5 GiBps](../facts/efs.md#efs-bursting-max-throughput-major-regions)
  link: [3 GiBps](../facts/efs.md#efs-bursting-max-throughput-major-regions)
efs-bursting-rate-without-credits
  claim: If no burst credits are available, a file system can drive up to 50 MiBps per TiB of storage, with a minimum of 1 MiBps.
  scope: per TiB of storage; maximum; not adjustable; no burst credits available.
  link: [50 MiBps per TiB](../facts/efs.md#efs-bursting-rate-without-credits)
efs-bursting-read-metering-one-third
  claim: Amazon EFS meters read operations up to one-third the rate of write operations, permitting a baseline rate of up to 150 KiBps per GiB of read throughput, or 50 KiBps per GiB of write throughput.
  scope: per GiB of Standard storage; maximum; not adjustable; Bursting throughput baseline.
  link: [150 KiBps per GiB](../facts/efs.md#efs-bursting-read-metering-one-third)
efs-bursting-scales-with-storage-size-recommended-for
  claim: Bursting throughput is recommended for workloads that need throughput that scales with the amount of storage in the file system.
  scope: EFS Bursting throughput.
  link: [throughput that scales with the amount of storage](../facts/efs.md#efs-bursting-scales-with-storage-size-recommended-for)
  link: [Bursting throughput is recommended](../facts/efs.md#efs-bursting-scales-with-storage-size-recommended-for)
efs-case-ginkgo-migrating-active-projects-to-efs
  claim: The AWS case study says Ginkgo Bioworks is migrating to Amazon EFS, a serverless, fully elastic file system, to get more insight into its file usage and optimize further.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [greater level of insight into its file usage](../facts/efs.md#efs-case-ginkgo-migrating-active-projects-to-efs)
efs-case-mazzuma-model-data-efs-sagemaker
  claim: The AWS case study says Mazzuma used Amazon EFS, a serverless, fully elastic file storage service, to store and transfer model data into Amazon SageMaker at speeds of 1.5 Gbps.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [serverless, fully elastic file storage service](../facts/efs.md#efs-case-mazzuma-model-data-efs-sagemaker)
efs-case-world-kinect-efs-oracle-application-files
  claim: The AWS case study says World Kinect, after migrating its Oracle E-Business Suite to AWS, used Amazon EFS to automatically provision and manage application files.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [automatically provision and manage application files](../facts/efs.md#efs-case-world-kinect-efs-oracle-application-files)
efs-change-access-points-10000-per-file-system-2025-02
  claim: On 2025-02-10 Amazon EFS raised the maximum number of access points a single file system can have from 1,000 to 10,000, and you can also request an increase for this limit.
  scope: access points per file system.
  link: [2025-02-10](../facts/efs.md#efs-change-access-points-10000-per-file-system-2025-02)
  link: [10,000](../facts/efs.md#efs-change-access-points-10000-per-file-system-2025-02)
  link: [1,000](../facts/efs.md#efs-change-access-points-10000-per-file-system-2025-02)
  changed: 2025-02-10: was 1,000
efs-change-archive-storage-class-and-file-system-types-2023-11
  claim: On 2023-11-26 Amazon EFS added the EFS Archive storage class, file system types, and the Transition into Archive lifecycle policy. EFS now offers three storage classes: EFS Standard, EFS Infrequent Access (EFS IA) and EFS Archive.
  scope: EFS storage classes.
  link: [2023-11-26](../facts/efs.md#efs-change-archive-storage-class-and-file-system-types-2023-11)
  link: [three storage classes](../facts/efs.md#efs-change-archive-storage-class-and-file-system-types-2023-11)
efs-change-cross-account-replication-2024-11
  claim: On 2024-11-19 Amazon EFS added support for cross-account replication.
  scope: EFS Replication.
  link: [2024-11-19](../facts/efs.md#efs-change-cross-account-replication-2024-11)
  link: [cross-account replication](../facts/efs.md#efs-change-cross-account-replication-2024-11)
efs-change-datasync-enhanced-mode-efs-lustre-2026-07
  claim: On 2026-07-28 AWS DataSync Enhanced mode began to support Amazon EFS and Amazon FSx for Lustre as source or destination locations. Before this, customers who wanted to move data to or from EFS or FSx for Lustre were limited to Basic mode.
  scope: AWS DataSync Enhanced mode locations.
  link: [2026-07-28](../facts/efs.md#efs-change-datasync-enhanced-mode-efs-lustre-2026-07)
  link: [Basic mode](../facts/efs.md#efs-change-datasync-enhanced-mode-efs-lustre-2026-07)
  changed: 2026-07-28: was Basic mode
efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04
  claim: On 2025-04-10 Amazon EFS raised the Elastic throughput read limit in all other Regions from 10 to 20 GiBps, while the specific Regions stay at 60 GiBps.
  scope: Elastic throughput read limit per file system, all other Regions.
  link: [2025-04-10](../facts/efs.md#efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04)
  link: [20 GiBps](../facts/efs.md#efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04)
  link: [10](../facts/efs.md#efs-change-elastic-read-throughput-20-gibps-other-regions-2025-04)
  changed: 2025-04-10: was 10
efs-change-elastic-read-throughput-60-gibps-four-regions-2025-05
  claim: On 2025-05-02 Amazon EFS raised the maximum read throughput for Elastic throughput file systems from 20 GiBps to 60 GiBps in Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Sydney) and Europe (London).
  scope: Elastic throughput read limit per file system, four Regions.
  link: [2025-05-02](../facts/efs.md#efs-change-elastic-read-throughput-60-gibps-four-regions-2025-05)
  link: [60 GiBps](../facts/efs.md#efs-change-elastic-read-throughput-60-gibps-four-regions-2025-05)
  link: [20 GiBps](../facts/efs.md#efs-change-elastic-read-throughput-60-gibps-four-regions-2025-05)
  changed: 2025-05-02: was 20 GiBps
efs-change-elastic-replaces-bursting-default-2023-04
  claim: On 2023-04-13 Amazon EFS made Elastic the default and recommended throughput mode for file systems, instead of Bursting.
  scope: EFS default throughput mode.
  link: [2023-04-13](../facts/efs.md#efs-change-elastic-replaces-bursting-default-2023-04)
  link: [Elastic](../facts/efs.md#efs-change-elastic-replaces-bursting-default-2023-04)
  link: [Bursting](../facts/efs.md#efs-change-elastic-replaces-bursting-default-2023-04)
  changed: 2023-04-13: was Bursting
efs-change-ipv6-support-2025-06
  claim: On 2025-06-09 Amazon EFS added support for Internet Protocol Version 6 (IPv6) on the EFS service APIs and on mount targets.
  scope: EFS APIs and mount targets.
  link: [2025-06-09](../facts/efs.md#efs-change-ipv6-support-2025-06)
  link: [IPv6](../facts/efs.md#efs-change-ipv6-support-2025-06)
efs-change-mount-targets-per-vpc-1400-2024-05
  claim: On 2024-05-15 Amazon EFS raised the maximum number of mount targets for each virtual private cloud (VPC) from 400 to 1,400.
  scope: mount targets per VPC.
  link: [2024-05-15](../facts/efs.md#efs-change-mount-targets-per-vpc-1400-2024-05)
  link: [1,400](../facts/efs.md#efs-change-mount-targets-per-vpc-1400-2024-05)
  link: [400](../facts/efs.md#efs-change-mount-targets-per-vpc-1400-2024-05)
  changed: 2024-05-15: was 400
efs-change-per-client-throughput-1500-mibps-2024-04
  claim: On 2024-04-30 Amazon EFS set the maximum combined read and write throughput to 1,500 MiBps for file systems that use Elastic throughput and are mounted with version 2.0 or later of the EFS client (amazon-efs-utils) or the EFS CSI Driver (aws-efs-csi-driver).
  scope: per client, Elastic throughput.
  link: [2024-04-30](../facts/efs.md#efs-change-per-client-throughput-1500-mibps-2024-04)
  link: [1,500 MiBps](../facts/efs.md#efs-change-per-client-throughput-1500-mibps-2024-04)
efs-change-replicate-to-existing-file-system-failback-2023-11
  claim: On 2023-11-27 Amazon EFS made it possible to replicate file systems to existing file systems, which makes it easier to synchronize changes between file systems for failback purposes.
  scope: EFS Replication destination.
  link: [2023-11-27](../facts/efs.md#efs-change-replicate-to-existing-file-system-failback-2023-11)
  link: [replicated to existing file systems](../facts/efs.md#efs-change-replicate-to-existing-file-system-failback-2023-11)
efs-clients-current-linux-nfsv41-and-mount-helper
  claim: AWS recommends a current generation Linux NFSv4.1 client, such as those in the latest Amazon Linux, Amazon Linux 2, Red Hat, Ubuntu, and macOS Big Sur AMIs, together with the EFS mount helper.
  scope: Amazon EFS clients.
  link: [current generation Linux NFSv4.1 client](../facts/efs.md#efs-clients-current-linux-nfsv41-and-mount-helper)
  link: [macOS Big Sur AMIs](../facts/efs.md#efs-clients-current-linux-nfsv41-and-mount-helper)
  link: [in conjunction with the EFS mount helper](../facts/efs.md#efs-clients-current-linux-nfsv41-and-mount-helper)
efs-close-to-open-consistency
  claim: Amazon EFS provides the close-to-open consistency semantics that applications expect from NFS.
  scope: Amazon EFS.
  link: [close-to-open consistency semantics](../facts/efs.md#efs-close-to-open-consistency)
  link: [applications expect from NFS](../facts/efs.md#efs-close-to-open-consistency)
efs-compute-services-ec2-ecs-eks-lambda-fargate
  claim: Amazon EFS is accessible from most types of AWS compute instances, including Amazon EC2, Amazon ECS, Amazon EKS, AWS Lambda, and AWS Fargate.
  scope: Amazon EFS clients.
  link: [Amazon EC2, Amazon ECS, Amazon EKS](../facts/efs.md#efs-compute-services-ec2-ecs-eks-lambda-fargate)
  link: [most types of Amazon Web Services compute instances](../facts/efs.md#efs-compute-services-ec2-ecs-eks-lambda-fargate)
  link: [AWS Lambda, and AWS Fargate](../facts/efs.md#efs-compute-services-ec2-ecs-eks-lambda-fargate)
efs-concurrent-access-multiple-clients-multiple-azs
  claim: You can access an EFS file system concurrently from multiple NFS clients, and EC2 and other compute instances in multiple Availability Zones of the same Region can share it; EFS supports one to thousands of EC2 instances connecting at once.
  scope: EFS file system.
  link: [concurrently from multiple NFS clients](../facts/efs.md#efs-concurrent-access-multiple-clients-multiple-azs)
  link: [one to thousands of Amazon Elastic Compute Cloud (EC2) instances](../facts/efs.md#efs-concurrent-access-multiple-clients-multiple-azs)
efs-cross-account-replication-destination-must-exist-first
  claim: For cross-account replication you must create both the source file system and the destination file system before you can create the IAM role for the source account; Amazon EFS cannot create the destination file system for you during replication.
  scope: EFS cross-account replication.
  link: [create both the source file system](../facts/efs.md#efs-cross-account-replication-destination-must-exist-first)
  link: [cannot create the destination file system for you](../facts/efs.md#efs-cross-account-replication-destination-must-exist-first)
efs-cross-account-replication-needs-file-system-policies
  claim: Cross-account replication needs an IAM role that gives Amazon EFS permission to replicate in the destination account, plus policies on the file systems that you share across accounts.
  scope: EFS cross-account replication.
  link: [create an IAM role that gives Amazon](../facts/efs.md#efs-cross-account-replication-needs-file-system-policies)
  link: [create policies on the file systems](../facts/efs.md#efs-cross-account-replication-needs-file-system-policies)
efs-cross-account-replication-requires-iam-role-not-service-linked
  claim: For cross-account replication you must provide an IAM role when you create the replication configuration; using the service-linked role is not permitted.
  scope: EFS cross-account replication.
  link: [must provide an IAM role](../facts/efs.md#efs-cross-account-replication-requires-iam-role-not-service-linked)
  link: [service-linked role is not permitted](../facts/efs.md#efs-cross-account-replication-requires-iam-role-not-service-linked)
efs-cross-account-replication-supported
  claim: You can replicate EFS file systems across AWS accounts.
  scope: EFS replication.
  link: [replicate EFS file systems across AWS accounts](../facts/efs.md#efs-cross-account-replication-supported)
  link: [across AWS accounts](../facts/efs.md#efs-cross-account-replication-supported)
efs-datasync-between-efs-regions-and-accounts
  claim: You can use DataSync to transfer files between two EFS file systems, including file systems in different AWS Regions and file systems owned by different AWS accounts.
  scope: AWS DataSync with EFS.
  link: [between two EFS file systems](../facts/efs.md#efs-datasync-between-efs-regions-and-accounts)
  link: [different AWS Regions](../facts/efs.md#efs-datasync-between-efs-regions-and-accounts)
  link: [owned by different AWS accounts](../facts/efs.md#efs-datasync-between-efs-regions-and-accounts)
efs-datasync-copies-between-storage-types-incl-efs
  claim: AWS DataSync can copy data between NFS and SMB file servers, self-managed object storage, AWS Snowball Edge, Amazon S3 buckets, EFS file systems, and FSx for Windows File Server file systems.
  scope: AWS DataSync with EFS.
  link: [Amazon S3 buckets, EFS file systems](../facts/efs.md#efs-datasync-copies-between-storage-types-incl-efs)
  link: [FSx for Windows File Server file systems](../facts/efs.md#efs-datasync-copies-between-storage-types-incl-efs)
efs-datasync-recommended-for-onpremises-file-data
  claim: AWS DataSync provides a fast and simple way to securely sync existing file systems into EFS, and it works over any network, including AWS Direct Connect.
  scope: AWS DataSync with EFS.
  link: [fast and simple way to securely sync](../facts/efs.md#efs-datasync-recommended-for-onpremises-file-data)
  link: [including AWS Direct Connect](../facts/efs.md#efs-datasync-recommended-for-onpremises-file-data)
efs-datasync-up-to-10-times-faster-than-linux-copy
  claim: AWS Direct Connect provides a dedicated network connection over which you can mount EFS file systems; once mounted, you can use DataSync to copy data into EFS up to 10 times faster than standard Linux copy tools.
  scope: AWS DataSync with EFS; maximum.
  link: [up to 10 times faster](../facts/efs.md#efs-datasync-up-to-10-times-faster-than-linux-copy)
  link: [standard Linux copy tools](../facts/efs.md#efs-datasync-up-to-10-times-faster-than-linux-copy)
efs-decision-guide-block-file-object-protocols
  claim: The AWS storage decision guide says file-based storage is mountable from virtually any operating system with the industry-standard protocols NFS and SMB, and that it suits workloads that need shared data across multiple compute instances.
  scope: file-based storage on AWS (EFS and FSx).
  link: [NFS and SMB](../facts/efs.md#efs-decision-guide-block-file-object-protocols)
  link: [shared data across multiple compute instances](../facts/efs.md#efs-decision-guide-block-file-object-protocols)
  say: N F S and S M B
efs-decision-guide-block-row-single-instance
  claim: In the AWS storage decision guide table, block storage (Amazon EBS and the EC2 instance store) is for low-latency, high-performance durable storage attached to single Amazon EC2 instances or containers, such as databases.
  scope: storage type table of the decision guide.
  link: [attached to single Amazon EC2 instances or containers](../facts/efs.md#efs-decision-guide-block-row-single-instance)
efs-decision-guide-block-storage-direct-attached
  claim: The AWS storage decision guide describes block storage as direct-attached to a compute instance with low-latency access, suitable for applications that need fast and consistent I/O.
  scope: block storage on AWS (EBS and instance store).
  link: [direct-attached to a compute instance](../facts/efs.md#efs-decision-guide-block-storage-direct-attached)
  link: [low-latency access](../facts/efs.md#efs-decision-guide-block-storage-direct-attached)
efs-decision-guide-definition-block-storage
  claim: The AWS storage decision guide defines block storage as technology that controls data storage and storage devices.
  scope: storage type definitions.
  link: [controls data storage and storage devices](../facts/efs.md#efs-decision-guide-definition-block-storage)
efs-decision-guide-definition-file-storage
  claim: The AWS storage decision guide defines file systems as storing data in a hierarchical structure of files and folders; in network environments, file-based storage often uses network-attached storage (NAS) technology.
  scope: storage type definitions.
  link: [hierarchical structure of files and folders](../facts/efs.md#efs-decision-guide-definition-file-storage)
efs-decision-guide-definition-object-storage
  claim: The AWS storage decision guide defines object storage as technology that stores and manages data in an unstructured format called objects, where each object is tagged with a unique identifier and holds metadata that describes the content.
  scope: storage type definitions.
  link: [unstructured format called objects](../facts/efs.md#efs-decision-guide-definition-object-storage)
efs-decision-guide-dr-multi-az-replication
  claim: The AWS storage decision guide says that choosing a storage service with disaster recovery features, such as replication across multiple Availability Zones, can help minimize the impact of a disaster, and that you should weigh your recovery time objective (RTO) and recovery point objective (RPO).
  scope: disaster recovery criterion in the storage decision guide.
  link: [replication across multiple Availability Zones](../facts/efs.md#efs-decision-guide-dr-multi-az-replication)
efs-decision-guide-file-system-row-shared-access
  claim: In the AWS storage decision guide table, file system storage is the type for applications that need shared read and write access across multiple EC2 instances or containers, or from multiple on-premises servers; the services listed for it include Amazon EFS and the Amazon FSx file systems.
  scope: storage type table of the decision guide.
  link: [shared read and write access](../facts/efs.md#efs-decision-guide-file-system-row-shared-access)
efs-decision-guide-object-storage-api-read-heavy
  claim: The AWS storage decision guide says object storage gives access to data through an application programming interface (API) over the internet and is well suited to read-heavy workloads such as streaming applications and services.
  scope: object storage on AWS (Amazon S3).
  link: [application programming interface (API) over the internet](../facts/efs.md#efs-decision-guide-object-storage-api-read-heavy)
  link: [read-heavy workloads](../facts/efs.md#efs-decision-guide-object-storage-api-read-heavy)
efs-decision-guide-use-appropriate-service-cost
  claim: The AWS storage decision guide lists things that can help you reduce cost when using an AWS storage service, among them: use the appropriate storage service for your workload type, and understand your data and how it is being used.
  scope: cost criterion in the storage decision guide.
  link: [appropriate storage service for your workload type](../facts/efs.md#efs-decision-guide-use-appropriate-service-cost)
  link: [Understand your data](../facts/efs.md#efs-decision-guide-use-appropriate-service-cost)
efs-default-backup-plan-daily-35-day-retention
  claim: The default EFS backup plan uses the AWS Backup recommended settings for automatic backups, which are daily backups with a 35-day retention period; you can edit the default backup plan settings using the AWS Backup console.
  scope: EFS default backup plan; default; adjustable.
  link: [daily backups with a 35-day retention period](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
  link: [AWS Backup recommended settings](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
  link: [edit the default backup plan settings](../facts/efs.md#efs-default-backup-plan-daily-35-day-retention)
efs-default-elastic-iops
  claim: By default, file systems that use Elastic throughput drive a maximum of 90,000 read IOPS for infrequently accessed data, 250,000 read IOPS for frequently accessed data, and 50,000 write IOPS.
  scope: per file system, Elastic throughput; default; adjustable; you can request an increase of up to 10 times these numbers.
  link: [90,000 read IOPS](../facts/efs.md#efs-default-elastic-iops)
  link: [250,000 read IOPS](../facts/efs.md#efs-default-elastic-iops)
  link: [50,000 write IOPS](../facts/efs.md#efs-default-elastic-iops)
efs-default-file-system-policy-full-access-anonymous
  claim: The default EFS file system policy does not use IAM to authenticate and grants full access to any anonymous client that can connect to the file system through a mount target.
  scope: EFS file system policy; default; adjustable.
  link: [does not use IAM to authenticate](../facts/efs.md#efs-default-file-system-policy-full-access-anonymous)
  link: [grants full access to any anonymous client](../facts/efs.md#efs-default-file-system-policy-full-access-anonymous)
efs-default-modes-general-purpose-and-elastic
  claim: For most workloads AWS recommends the default modes, which are the General Purpose performance mode and the Elastic throughput mode.
  scope: EFS file system; default; adjustable.
  link: [we recommend using the default modes](../facts/efs.md#efs-default-modes-general-purpose-and-elastic)
  link: [General Purpose performance mode](../facts/efs.md#efs-default-modes-general-purpose-and-elastic)
efs-dns-name-resolves-to-same-az-mount-target
  claim: You mount an EFS file system by its DNS name, which resolves to the IP address of the mount target in the same Availability Zone as your EC2 instance.
  scope: EFS mount target.
  link: [resolves to the IP address of the EFS](../facts/efs.md#efs-dns-name-resolves-to-same-az-mount-target)
  link: [Domain Name Service (DNS) name](../facts/efs.md#efs-dns-name-resolves-to-same-az-mount-target)
efs-elastic-best-for-spiky-low-average-to-peak
  claim: Elastic throughput is the best throughput mode for spiky or unpredictable workloads that are hard to forecast, or for applications that drive 5% or less of peak throughput on average.
  scope: EFS Elastic throughput.
  link: [spiky or unpredictable workloads](../facts/efs.md#efs-elastic-best-for-spiky-low-average-to-peak)
  link: [5% or less of the peak throughput](../facts/efs.md#efs-elastic-best-for-spiky-low-average-to-peak)
efs-elastic-regional-max-throughput-major-regions
  claim: Total default Elastic throughput for a Regional file system in US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney, Tokyo) and Europe (Frankfurt, Ireland, London) is a maximum read of 60 gibibytes per second (GiBps) and a maximum write (metered) throughput of 5 GiBps.
  scope: per Regional file system, for all connected clients, in the listed Regions; maximum; adjustable; increase through AWS Support.
  link: [60 gibibytes per second](../facts/efs.md#efs-elastic-regional-max-throughput-major-regions)
  link: [5 GiBps](../facts/efs.md#efs-elastic-regional-max-throughput-major-regions)
efs-elastic-regional-max-throughput-other-regions
  claim: Total default Elastic throughput for a Regional file system in all other AWS Regions is a maximum read of 20 GiBps and a maximum write (metered) throughput of 1 GiBps.
  scope: per Regional file system, for all connected clients, in all other Regions; maximum; adjustable; increase through AWS Support.
  link: [20 GiBps](../facts/efs.md#efs-elastic-regional-max-throughput-other-regions)
  link: [1 GiBps](../facts/efs.md#efs-elastic-regional-max-throughput-other-regions)
efs-elastic-scales-automatically-no-provisioning-pay-per-use
  claim: With Elastic throughput, EFS scales throughput up or down automatically, so you do not specify or provision throughput; you pay only for the metadata and data read or written, and you do not accrue or consume burst credits.
  scope: EFS Elastic throughput.
  link: [scales automatically](../facts/efs.md#efs-elastic-scales-automatically-no-provisioning-pay-per-use)
  link: [pay only for the amount of metadata](../facts/efs.md#efs-elastic-scales-automatically-no-provisioning-pay-per-use)
  link: [don't accrue or consume burst credits](../facts/efs.md#efs-elastic-scales-automatically-no-provisioning-pay-per-use)
efs-elastic-throughput-default-recommended
  claim: Elastic throughput is the default throughput mode in the Amazon EFS console and is recommended for most use cases.
  scope: EFS throughput modes; default; adjustable.
  link: [default throughput mode in the Amazon EFS console](../facts/efs.md#efs-elastic-throughput-default-recommended)
  link: [recommended for most use cases](../facts/efs.md#efs-elastic-throughput-default-recommended)
efs-encryption-at-rest-aes-256-data-and-metadata
  claim: Amazon EFS uses the industry-standard AES-256 encryption algorithm to encrypt data and metadata at rest.
  scope: EFS encryption at rest.
  link: [industry-standard AES-256 encryption algorithm](../facts/efs.md#efs-encryption-at-rest-aes-256-data-and-metadata)
  link: [data and metadata at rest](../facts/efs.md#efs-encryption-at-rest-aes-256-data-and-metadata)
efs-encryption-at-rest-console-default-cli-explicit
  claim: Encryption at rest is enabled by default when you create a file system in the EFS console, but when you use the AWS CLI, API or SDKs you must enable encryption explicitly.
  scope: EFS encryption at rest; default; adjustable.
  link: [encryption at rest is enabled by default](../facts/efs.md#efs-encryption-at-rest-console-default-cli-explicit)
  link: [you must explicity enable encryption](../facts/efs.md#efs-encryption-at-rest-console-default-cli-explicit)
efs-encryption-in-transit-tls
  claim: Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS).
  scope: Amazon EFS encryption in transit.
  link: [encryption of data in transit](../facts/efs.md#efs-encryption-in-transit-tls)
  link: [Transport Layer Security (TLS)](../facts/efs.md#efs-encryption-in-transit-tls)
efs-encryption-scp-condition-key-enforcement
  claim: You can define service control policies in AWS Organizations to enforce Amazon EFS encryption for all accounts in your organization.
  scope: EFS encryption at rest.
  link: [service control policies (SCPs) inside AWS Organizations](../facts/efs.md#efs-encryption-scp-condition-key-enforcement)
  link: [enforce Amazon EFS encryption](../facts/efs.md#efs-encryption-scp-condition-key-enforcement)
efs-encryption-setting-cannot-change-after-creation
  claim: After you create an EFS file system you cannot change its encryption setting, so you cannot make an unencrypted file system encrypted.
  scope: EFS encryption at rest.
  link: [cannot change its encryption setting](../facts/efs.md#efs-encryption-setting-cannot-change-after-creation)
  link: [cannot modify an unencrypted file system](../facts/efs.md#efs-encryption-setting-cannot-change-after-creation)
efs-encryption-transparent-no-application-change
  claim: In an encrypted EFS file system, data and metadata are encrypted before being written to storage and automatically decrypted when read, transparently to your applications.
  scope: EFS encryption at rest.
  link: [automatically decrypted when read](../facts/efs.md#efs-encryption-transparent-no-application-change)
  link: [don't need to modify your applications](../facts/efs.md#efs-encryption-transparent-no-application-change)
efs-faq-access-from-ecs-task-definition
  claim: You can access EFS from containers launched by Amazon ECS, with both EC2 and Fargate launch types, by referencing an EFS file system in the task definition.
  scope: EFS with Amazon ECS.
  link: [both EC2 and Fargate launch types](../facts/efs.md#efs-faq-access-from-ecs-task-definition)
efs-faq-access-from-eks-csi-driver
  claim: You can access EFS from containers launched by Amazon EKS, with either EC2 or Fargate launch types, using the EFS CSI driver.
  scope: EFS with Amazon EKS.
  link: [the EFS CSI driver](../facts/efs.md#efs-faq-access-from-eks-csi-driver)
efs-faq-access-from-lambda-function-settings
  claim: You can access EFS from AWS Lambda functions by referencing an EFS file system in the function settings.
  scope: EFS with AWS Lambda.
  link: [an EFS file system in your function settings](../facts/efs.md#efs-faq-access-from-lambda-function-settings)
efs-faq-access-point-definition
  claim: An EFS Access Point is a network endpoint that applications use to access an EFS file system and enforce file- and folder-level POSIX permissions, based on fine-grained access control and policy-based permissions defined in IAM.
  scope: EFS Access Points.
  link: [a network endpoint](../facts/efs.md#efs-faq-access-point-definition)
efs-faq-archive-cost-50-percent
  claim: EFS Archive offers up to 50% lower cost than EFS Infrequent Access, with a higher request charge when the data is accessed.
  scope: EFS Archive compared with EFS IA; maximum.
  link: [up to 50% lower cost](../facts/efs.md#efs-faq-archive-cost-50-percent)
efs-faq-archive-minimum-duration-90-days
  claim: EFS IA has no minimum storage duration; data tiered to EFS Archive has a minimum storage duration of 90 days.
  scope: per file, EFS IA and EFS Archive; minimum; not adjustable.
  link: [minimum storage duration of 90 days](../facts/efs.md#efs-faq-archive-minimum-duration-90-days)
  link: [no minimum storage duration](../facts/efs.md#efs-faq-archive-minimum-duration-90-days)
efs-faq-archive-regional-elastic-only
  claim: EFS Archive is optimized for and supported on EFS Regional file systems that use the default Elastic Throughput mode.
  scope: EFS Archive.
  link: [EFS Regional file systems](../facts/efs.md#efs-faq-archive-regional-elastic-only)
  link: [default Elastic Throughput mode](../facts/efs.md#efs-faq-archive-regional-elastic-only)
efs-faq-backup-aws-backup-incremental
  claim: Amazon EFS Backup is powered by AWS Backup, which centrally manages and automates backups of EFS file systems.
  scope: EFS Backup.
  link: [powered by AWS Backup](../facts/efs.md#efs-faq-backup-aws-backup-incremental)
efs-faq-backup-incremental-after-first
  claim: During the initial backup of an EFS file system, a copy of the entire file system is made in the backup vault.
  scope: EFS Backup, AWS Backup vault.
  link: [a copy of the entire file system](../facts/efs.md#efs-faq-backup-incremental-after-first)
efs-faq-concurrent-onprem-and-ec2
  claim: You can access an EFS file system at the same time from on-premises servers and from EC2 instances in your VPC.
  scope: on-premises access to EFS.
  link: [on-premises datacenter as well as EC2 instances](../facts/efs.md#efs-faq-concurrent-onprem-and-ec2)
efs-faq-control-instances-with-security-groups-and-iam
  claim: You control which EC2 instances can access an EFS file system with VPC security group rules and IAM policies; security groups control network traffic and an IAM policy on the file system controls which clients can mount it and with what permissions.
  scope: Amazon EFS access control.
  link: [VPC security group rules and IAM policies](../facts/efs.md#efs-faq-control-instances-with-security-groups-and-iam)
  link: [Attach an IAM policy to your file system](../facts/efs.md#efs-faq-control-instances-with-security-groups-and-iam)
efs-faq-datasync-agent-required
  claim: For DataSync into or out of EFS you must first deploy a software agent, except when copying files between two Amazon EFS file systems.
  scope: DataSync with EFS.
  link: [deploy a software agent](../facts/efs.md#efs-faq-datasync-agent-required)
efs-faq-datasync-between-regions-transfer-family-same-region
  claim: DataSync can transfer files between two EFS file systems, including ones in different AWS Regions. AWS Transfer Family endpoints must be in the same Region as the EFS file system.
  scope: DataSync and Transfer Family with EFS.
  link: [including ones in different AWS Regions](../facts/efs.md#efs-faq-datasync-between-regions-transfer-family-same-region)
  link: [must be in the same Region](../facts/efs.md#efs-faq-datasync-between-regions-transfer-family-same-region)
efs-faq-durability-11-nines
  claim: Amazon EFS is designed to provide 99.999999999% (11 nines) of durability over a given year.
  scope: per year; fixed.
  link: [99.999999999%](../facts/efs.md#efs-faq-durability-11-nines)
  link: [11 nines](../facts/efs.md#efs-faq-durability-11-nines)
efs-faq-efs-semantics-strong-consistency-locking
  claim: EFS provides a file system interface and file system access semantics such as strong consistency and file locking, with concurrently accessible storage for up to thousands of EC2 instances.
  scope: EFS.
  link: [strong consistency and file locking](../facts/efs.md#efs-faq-efs-semantics-strong-consistency-locking)
efs-faq-efs-vs-ebs-vs-s3
  claim: The EFS FAQ says EFS is file storage for compute and on-premises servers, with strong consistency, file locking and concurrent access for up to thousands of EC2 instances; EBS is block storage for the lowest-latency access from a single EC2 instance; S3 is object storage reached through an internet API.
  scope: EFS, EBS and S3 compared.
  link: [concurrently accessible storage](../facts/efs.md#efs-faq-efs-vs-ebs-vs-s3)
  link: [lowest-latency access to data](../facts/efs.md#efs-faq-efs-vs-ebs-vs-s3)
  link: [an internet API that can be accessed anywhere](../facts/efs.md#efs-faq-efs-vs-ebs-vs-s3)
  link: [strong consistency and file locking](../facts/efs.md#efs-faq-efs-vs-ebs-vs-s3)
efs-faq-elastic-grow-shrink
  claim: EFS file systems are elastic: they grow and shrink automatically as files are added and removed.
  scope: EFS file system.
  link: [elastic, automatically growing and shrinking](../facts/efs.md#efs-faq-elastic-grow-shrink)
efs-faq-elastic-throughput-billed-gb-transferred
  claim: The Elastic Throughput amount billed in a month is based on the read and write data transferred within the month, measured in GB transferred.
  scope: per month, EFS Elastic Throughput.
  link: [“GB transferred.”](../facts/efs.md#efs-faq-elastic-throughput-billed-gb-transferred)
efs-faq-elastic-throughput-billing
  claim: With Elastic Throughput, performance scales automatically with workload activity, and you pay only for the throughput you use, measured as data transferred per month.
  scope: EFS Elastic Throughput.
  link: [performance automatically scales](../facts/efs.md#efs-faq-elastic-throughput-billing)
  link: [only pay for the throughput you use](../facts/efs.md#efs-faq-elastic-throughput-billing)
efs-faq-elastic-throughput-default
  claim: Elastic Throughput is the default throughput mode of EFS and is suitable for most file workloads.
  scope: EFS throughput mode; default; not adjustable.
  link: [Elastic Throughput](../facts/efs.md#efs-faq-elastic-throughput-default)
  link: [default throughput mode](../facts/efs.md#efs-faq-elastic-throughput-default)
efs-faq-elastic-throughput-when
  claim: Elastic Throughput is ideal when peak throughput is unknown or the workload is very spiky with low baseline activity, meaning it uses less than 5% of capacity on average when you provision for peak needs.
  scope: EFS throughput mode choice.
  link: [less than 5% of capacity on average](../facts/efs.md#efs-faq-elastic-throughput-when)
  link: [unsure of your application’s peak throughput needs](../facts/efs.md#efs-faq-elastic-throughput-when)
efs-faq-encrypt-rest-and-transit
  claim: Amazon EFS can encrypt data at rest and in transit; the two can be configured together or separately.
  scope: EFS encryption.
  link: [at rest and in transit](../facts/efs.md#efs-faq-encrypt-rest-and-transit)
  link: [together or separately](../facts/efs.md#efs-faq-encrypt-rest-and-transit)
efs-faq-encryption-at-rest-kms
  claim: Data encrypted at rest in EFS is transparently encrypted when written and decrypted when read, with encryption keys managed by AWS KMS.
  scope: EFS encryption at rest.
  link: [Encryption keys are managed by the AWS KMS](../facts/efs.md#efs-faq-encryption-at-rest-kms)
efs-faq-encryption-in-transit-tls-1-2
  claim: EFS encryption in transit uses industry-standard Transport Layer Security (TLS) 1.2 between clients and file systems.
  scope: EFS encryption in transit.
  link: [Transport Layer Security (TLS) 1.2](../facts/efs.md#efs-faq-encryption-in-transit-tls-1-2)
efs-faq-encryption-minimal-effect-on-io
  claim: Encrypting data has a minimal effect on EFS I/O latency and throughput.
  scope: Amazon EFS encryption.
  link: [minimal effect on I/O latency and throughput](../facts/efs.md#efs-faq-encryption-minimal-effect-on-io)
  link: [Encrypting your data](../facts/efs.md#efs-faq-encryption-minimal-effect-on-io)
efs-faq-failback-incremental-changes
  claim: After a disaster is over, you can fail back by transferring only incremental changes from the EFS replica back to the original file system.
  scope: EFS Replication failback.
  link: [transferring only incremental changes](../facts/efs.md#efs-faq-failback-incremental-changes)
efs-faq-file-system-policy-mount-permissions
  claim: An IAM policy attached to an EFS file system controls which clients can mount it and with what permissions, and EFS Access Points manage application access.
  scope: EFS file system policy.
  link: [control which clients can mount your file system](../facts/efs.md#efs-faq-file-system-policy-mount-permissions)
efs-faq-file-system-types
  claim: EFS Regional file systems (recommended) offer the highest levels of durability and availability by storing data with and across multiple Availability Zones.
  scope: EFS file system types.
  link: [EFS Regional file systems (recommended)](../facts/efs.md#efs-faq-file-system-types)
efs-faq-free-tier-5-gb-standard
  claim: The EFS FAQ says that, upon sign up, new EFS customers receive 5 GB of Amazon EFS Standard each month for one year under the AWS Free Tier, which is not applicable to files stored in the EFS One Zone file system type; the same FAQ says that starting July 15, 2025, new AWS customers receive up to $200 in AWS Free Tier credits that can be applied towards eligible services, including Amazon EFS.
  scope: new EFS customers, AWS Free Tier; EFS Standard only (not One Zone); The 5 GB offer is the FAQ's Free Tier wording; new AWS customers from July 15, 2025 receive Free Tier credits.
  link: [5 GB of Amazon EFS Standard each month for one year](../facts/efs.md#efs-faq-free-tier-5-gb-standard)
  link: [not applicable to files stored in the EFS One Zone file system type](../facts/efs.md#efs-faq-free-tier-5-gb-standard)
  link: [up to $200 in AWS Free Tier credits](../facts/efs.md#efs-faq-free-tier-5-gb-standard)
efs-faq-ia-archive-128-kib-billing
  claim: There is no minimum file size for IA or Archive, but files smaller than 128 KiB in these classes incur storage charges as if they were 128 KiB.
  scope: per file, EFS IA and EFS Archive billing; minimum; not adjustable.
  link: [smaller than 128 KiB](../facts/efs.md#efs-faq-ia-archive-128-kib-billing)
efs-faq-ia-archive-same-throughput-higher-latency
  claim: Compared with EFS Standard, EFS IA and Archive offer the same throughput and IOPS scalability but with higher first-byte latencies.
  scope: EFS IA and EFS Archive compared with EFS Standard.
  link: [the same throughput and IOPS scalability](../facts/efs.md#efs-faq-ia-archive-same-throughput-higher-latency)
efs-faq-ia-cost-95-percent
  claim: EFS IA offers up to 95% lower cost than EFS Standard for infrequently accessed data.
  scope: EFS IA compared with EFS Standard; maximum.
  link: [up to 95% lower cost](../facts/efs.md#efs-faq-ia-cost-95-percent)
efs-faq-ia-quarter-archive-year-designed-for
  claim: EFS Infrequent Access is designed for data accessed only a few times a quarter and EFS Archive for data accessed a few times a year or less, and both are cost-optimized classes with low double-digit millisecond latencies.
  scope: EFS storage classes.
  link: [a few times a quarter](../facts/efs.md#efs-faq-ia-quarter-archive-year-designed-for)
  link: [a few times a year or less](../facts/efs.md#efs-faq-ia-quarter-archive-year-designed-for)
  link: [low double-digit millisecond latencies](../facts/efs.md#efs-faq-ia-quarter-archive-year-designed-for)
efs-faq-iam-policy-common-settings
  claim: In the EFS console you can apply common policies such as disabling root access, enforcing read-only access, or enforcing that all connections are encrypted.
  scope: EFS file system policy.
  link: [disabling root access, enforcing read-only access](../facts/efs.md#efs-faq-iam-policy-common-settings)
efs-faq-intelligent-tiering-promotes
  claim: EFS Intelligent-Tiering promotes files from IA and Archive back to Standard when they are accessed, so later reads have the sub-millisecond latencies of EFS Standard.
  scope: EFS Intelligent-Tiering.
  link: [back to EFS Standard when they are accessed](../facts/efs.md#efs-faq-intelligent-tiering-promotes)
efs-faq-lifecycle-default-30-90-days
  claim: The default, recommended EFS lifecycle policy tiers files from Standard to IA after 30 consecutive days without access and to Archive after 90 consecutive days without access.
  scope: EFS Lifecycle Management; default; not adjustable.
  link: [30 consecutive days without access](../facts/efs.md#efs-faq-lifecycle-default-30-90-days)
  link: [90 consecutive days without access](../facts/efs.md#efs-faq-lifecycle-default-30-90-days)
efs-faq-locking-nfs-v4-1-advisory
  claim: Locking in EFS follows the NFS v4.1 protocol for advisory locking and lets applications use both whole file and byte range locks.
  scope: EFS file locking.
  link: [advisory locking](../facts/efs.md#efs-faq-locking-nfs-v4-1-advisory)
  link: [both whole file and byte range locks](../facts/efs.md#efs-faq-locking-nfs-v4-1-advisory)
efs-faq-metadata-metered-4-kib
  claim: For Elastic Throughput, EFS meters metadata operations at a minimum of 4 KiB.
  scope: per metadata operation, Elastic Throughput; minimum.
  link: [a minimum of 4 KiB](../facts/efs.md#efs-faq-metadata-metered-4-kib)
efs-faq-metadata-operations-charged
  claim: EFS data transfer charges apply to metadata operations such as list (ls), remove (rm), and create directory (mkdir).
  scope: EFS Elastic Throughput billing.
  link: [EFS data transfer charges for metadata operations](../facts/efs.md#efs-faq-metadata-operations-charged)
efs-faq-mount-helper-encrypts-transit
  claim: Data can be encrypted in transit between an EFS file system and its clients by using the Amazon EFS mount helper.
  scope: EFS encryption in transit.
  link: [Amazon EFS mount helper](../facts/efs.md#efs-faq-mount-helper-encrypts-transit)
efs-faq-mount-linux-instance-dns-name
  claim: To access an EFS file system, you mount it on an EC2 Linux-based instance using the standard Linux mount command and the file system's DNS name.
  scope: EFS on EC2.
  link: [standard Linux mount command](../facts/efs.md#efs-faq-mount-linux-instance-dns-name)
efs-faq-nfs-v4-protocol
  claim: EFS uses the NFS v4 protocol.
  scope: EFS file access.
  link: [NFS v4](../facts/efs.md#efs-faq-nfs-v4-protocol)
efs-faq-one-zone-single-az
  claim: EFS One Zone file systems store data redundantly in a single AZ, so the data will be unavailable and might be lost during a disaster or other fault within that AZ.
  scope: EFS One Zone file systems.
  link: [store data redundantly within a single AZ](../facts/efs.md#efs-faq-one-zone-single-az)
efs-faq-one-zone-single-mount-target
  claim: EFS One Zone file systems support only one highly available mount target, in a single AZ.
  scope: EFS One Zone file systems; maximum.
  link: [only one highly available EFS mount target](../facts/efs.md#efs-faq-one-zone-single-mount-target)
efs-faq-one-zone-use-cases
  claim: EFS One Zone storage classes are ideal for workloads such as development, build, and staging environments.
  scope: EFS One Zone storage classes.
  link: [development, build, and staging environments](../facts/efs.md#efs-faq-one-zone-use-cases)
efs-faq-onprem-mount-nfs-v4-1
  claim: You mount an EFS file system on an on-premises Linux server with the standard Linux mount command, using the NFS v4.1 protocol.
  scope: on-premises access to EFS.
  link: [NFS v4.1](../facts/efs.md#efs-faq-onprem-mount-nfs-v4-1)
efs-faq-onprem-needs-direct-connect-or-vpn
  claim: To access EFS file systems from on premises you must have an AWS Direct Connect or AWS VPN connection between the on-premises datacenter and your VPC.
  scope: on-premises access to EFS.
  link: [a Direct Connect or AWS VPN connection](../facts/efs.md#efs-faq-onprem-needs-direct-connect-or-vpn)
efs-faq-replication-failover-minutes
  claim: In the event of a disaster, you can fail over to the EFS replica file system and resume operations for business-critical applications within minutes.
  scope: EFS Replication failover.
  link: [within minutes](../facts/efs.md#efs-faq-replication-failover-minutes)
efs-faq-replication-lost-and-found
  claim: If you interrupt EFS replication in a disaster recovery event, files that were transferred but not yet copied to their final locations are in a lost+found directory under the root directory of the replica.
  scope: EFS replica file system.
  link: [lost+found directory](../facts/efs.md#efs-faq-replication-lost-and-found)
efs-faq-replication-replica-lifecycle-savings-92
  claim: With EFS Replication you can configure the replica independently of the source to use cost-optimized storage classes and a shorter age-off lifecycle policy, to save up to 92% on costs.
  scope: EFS replica file system; maximum.
  link: [up to 92%](../facts/efs.md#efs-faq-replication-replica-lifecycle-savings-92)
efs-faq-replication-timesincelastsync-metric
  claim: EFS Replication publishes a timestamp metric on Amazon CloudWatch called TimeSinceLastSync.
  scope: EFS Replication.
  link: [TimeSinceLastSync](../facts/efs.md#efs-faq-replication-timesincelastsync-metric)
efs-faq-same-semantics-onprem-and-ec2
  claim: EFS provides the same file system access semantics, such as strong data consistency and file locking, across all EC2 instances and on-premises servers.
  scope: EFS.
  link: [the same file system access semantics](../facts/efs.md#efs-faq-same-semantics-onprem-and-ec2)
efs-faq-standard-sub-millisecond
  claim: EFS Standard is an SSD-powered class designed to deliver sub-millisecond latencies.
  scope: EFS Standard.
  link: [sub-millisecond latencies](../facts/efs.md#efs-faq-standard-sub-millisecond)
efs-faq-store-petabytes
  claim: You can store petabytes of data in Amazon EFS.
  scope: EFS file system.
  link: [petabytes](../facts/efs.md#efs-faq-store-petabytes)
efs-faq-three-storage-classes-standard-ia-archive
  claim: Amazon EFS offers three storage classes: EFS Standard, EFS Infrequent Access and EFS Archive, and EFS Archive is optimized for and supported on Regional file systems that use the default Elastic throughput mode.
  scope: EFS storage classes.
  link: [three storage classes](../facts/efs.md#efs-faq-three-storage-classes-standard-ia-archive)
  link: [EFS Standard, EFS Infrequent Access, and EFS Archive](../facts/efs.md#efs-faq-three-storage-classes-standard-ia-archive)
  link: [EFS Regional file systems using EFS’s default](../facts/efs.md#efs-faq-three-storage-classes-standard-ia-archive)
efs-faq-use-case-file-vs-block-vs-object
  claim: EFS is a file storage service, Amazon EBS is a block-level storage service for use with EC2, and Amazon S3 is an object storage service.
  scope: EFS vs EBS vs S3.
  link: [file storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [block-level storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [object storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
efs-faq-use-cases-and-one-zone-fit
  claim: The EFS FAQ says EFS supports big data and analytics, media processing, content management, web serving and home directories; Standard storage classes suit workloads needing the highest durability and availability, and One Zone storage classes suit development, build and staging environments.
  scope: Amazon EFS.
  link: [highest levels of durability and availability](../facts/efs.md#efs-faq-use-cases-and-one-zone-fit)
efs-file-locking-nfsv4-byte-range
  claim: NFS client applications can use NFS version 4 file locking, including byte-range locking, for read and write operations on EFS files.
  scope: Amazon EFS file locking.
  link: [NFS version 4 file locking](../facts/efs.md#efs-file-locking-nfsv4-byte-range)
  link: [including byte-range locking](../facts/efs.md#efs-file-locking-nfsv4-byte-range)
efs-file-system-id-globally-unique-names-not
  claim: Every EFS file system has an automatically generated ID that is globally unique; file system names are tags and do not need to be unique, so they are not global like S3 bucket names.
  scope: Amazon EFS file system.
  link: [automatically generated ID number](../facts/efs.md#efs-file-system-id-globally-unique-names-not)
  link: [names don’t need to be unique](../facts/efs.md#efs-file-system-id-globally-unique-names-not)
  link: [globally unique](../facts/efs.md#efs-file-system-id-globally-unique-names-not)
efs-free-tier-not-one-zone
  claim: The AWS Free Tier is not applicable to files stored in the One Zone storage file system type.
  scope: One Zone file systems.
  link: [is not applicable to files stored in the One Zone](../facts/efs.md#efs-free-tier-not-one-zone)
efs-general-purpose-always-recommended-max-io-higher-latency
  claim: Max I/O performance mode has higher per-operation latencies than General Purpose mode, so AWS recommends always using General Purpose performance mode.
  scope: EFS performance modes.
  link: [always using General Purpose performance mode](../facts/efs.md#efs-general-purpose-always-recommended-max-io-higher-latency)
  link: [higher per-operation latencies with Max I/O](../facts/efs.md#efs-general-purpose-always-recommended-max-io-higher-latency)
efs-ia-archive-billed-per-class-plus-access-charges
  claim: You are billed for the amount of data in each EFS storage class, and you are also billed data access charges when files in IA or Archive are read or when data transitions between classes through lifecycle management.
  scope: EFS storage classes.
  link: [data in each storage class](../facts/efs.md#efs-ia-archive-billed-per-class-plus-access-charges)
  link: [billed data access charges](../facts/efs.md#efs-ia-archive-billed-per-class-plus-access-charges)
efs-iam-authorization-logged-to-cloudtrail
  claim: When you use IAM authorization for NFS clients, client connections and IAM authorization decisions are logged to AWS CloudTrail.
  scope: EFS IAM authorization for NFS clients.
  link: [logged to AWS CloudTrail](../facts/efs.md#efs-iam-authorization-logged-to-cloudtrail)
  link: [IAM authorization decisions](../facts/efs.md#efs-iam-authorization-logged-to-cloudtrail)
efs-iam-identity-and-resource-policies-control-client-access
  claim: You can use both IAM identity policies and resource policies to control client access to EFS, including read-only, write and root access.
  scope: EFS IAM authorization for NFS clients.
  link: [IAM identity policies and resource policies](../facts/efs.md#efs-iam-identity-and-resource-policies-control-client-access)
  link: [read-only, write, and root access](../facts/efs.md#efs-iam-identity-and-resource-policies-control-client-access)
efs-iam-nfs-client-authorization-requires-mount-helper
  claim: You must use the EFS mount helper to mount an EFS file system in order to use IAM authorization to control client access.
  scope: EFS IAM authorization for NFS clients.
  link: [must use the EFS mount helper](../facts/efs.md#efs-iam-nfs-client-authorization-requires-mount-helper)
  link: [IAM authorization to control client access](../facts/efs.md#efs-iam-nfs-client-authorization-requires-mount-helper)
efs-iops-not-billed-separately
  claim: You are not billed separately for IOPS on EFS; IOPS are included in a file system's throughput accounting.
  scope: Amazon EFS.
  link: [not billed separately for IOPS](../facts/efs.md#efs-iops-not-billed-separately)
  link: [included in a file system's throughput accounting](../facts/efs.md#efs-iops-not-billed-separately)
efs-latency-ia-archive-first-byte
  claim: The EFS Infrequent Access (IA) and EFS Archive storage classes provide first-byte latencies of tens of milliseconds.
  scope: EFS IA and EFS Archive storage classes.
  link: [tens of milliseconds](../facts/efs.md#efs-latency-ia-archive-first-byte)
efs-latency-standard-first-byte
  claim: The EFS Standard storage class provides first-byte latencies as low as 1 millisecond for reads and 2.7 milliseconds for writes.
  scope: EFS Standard storage class; minimum; not adjustable; best case.
  link: [1 millisecond](../facts/efs.md#efs-latency-standard-first-byte)
  link: [2.7 milliseconds](../facts/efs.md#efs-latency-standard-first-byte)
efs-lifecycle-automatic-transition-between-classes
  claim: EFS lifecycle management automatically transitions data between storage classes according to the lifecycle configuration of the file system. The lifecycle policies apply to the entire EFS file system.
  scope: EFS lifecycle management.
  link: [automatically transition data between storage classes](../facts/efs.md#efs-lifecycle-automatic-transition-between-classes)
  link: [apply to the entire EFS file system](../facts/efs.md#efs-lifecycle-automatic-transition-between-classes)
efs-lifecycle-default-archive-after-90-days
  claim: By default, files not accessed in the Standard storage class for 90 days are transitioned into the Archive storage class.
  scope: EFS lifecycle policy, Transition into Archive; default; adjustable.
  link: [90 days](../facts/efs.md#efs-lifecycle-default-archive-after-90-days)
  link: [transitioned in to the Archive storage class](../facts/efs.md#efs-lifecycle-default-archive-after-90-days)
efs-lifecycle-default-ia-after-30-days
  claim: By default, files not accessed in the Standard storage class for 30 days are transitioned into IA.
  scope: EFS lifecycle policy, Transition into IA; default; adjustable.
  link: [30 days](../facts/efs.md#efs-lifecycle-default-ia-after-30-days)
  link: [transitioned into IA](../facts/efs.md#efs-lifecycle-default-ia-after-30-days)
efs-lifecycle-default-no-move-back-to-standard
  claim: By default, files are not moved back to the Standard storage class when they are accessed in IA or Archive; they stay in the IA or Archive storage class.
  scope: EFS lifecycle policy, Transition into Standard; default; adjustable.
  link: [not moved back to the Standard storage class](../facts/efs.md#efs-lifecycle-default-no-move-back-to-standard)
  link: [remain in the IA or Archive storage class](../facts/efs.md#efs-lifecycle-default-no-move-back-to-standard)
efs-lifecycle-operations-lower-priority-than-workload
  claim: File system operations for lifecycle management have a lower priority than operations for the EFS file system workload.
  scope: EFS lifecycle management.
  link: [have a lower priority](../facts/efs.md#efs-lifecycle-operations-lower-priority-than-workload)
  link: [lifecycle management](../facts/efs.md#efs-lifecycle-operations-lower-priority-than-workload)
efs-lifecycle-recommended-defaults-quick-create
  claim: In the Amazon EFS console, Quick create uses recommended settings that include lifecycle policies to transition the file system to EFS Infrequent Access (IA) storage after 30 days, to EFS Archive storage after 90 days, and not to transition to EFS Standard storage.
  scope: per new file system, recommended settings; default; adjustable; console quick create.
  link: [30 days](../facts/efs.md#efs-lifecycle-recommended-defaults-quick-create)
  link: [90 days](../facts/efs.md#efs-lifecycle-recommended-defaults-quick-create)
efs-lifecycle-transition-based-on-last-access-timer-reset
  claim: EFS lifecycle transition time is based on when a file was last accessed in the Standard storage class, and the lifecycle timer is reset whenever a file in Standard is accessed.
  scope: EFS lifecycle management.
  link: [last accessed in the Standard storage class](../facts/efs.md#efs-lifecycle-transition-based-on-last-access-timer-reset)
  link: [lifecycle management timer is reset](../facts/efs.md#efs-lifecycle-transition-based-on-last-access-timer-reset)
efs-lifecycle-transition-to-ia-valid-values
  claim: The lifecycle policy setting for the number of days after files were last accessed in the Standard storage class at which to move them to Infrequent Access (IA) storage (TransitionToIA) accepts AFTER_1_DAY, AFTER_7_DAYS, AFTER_14_DAYS, AFTER_30_DAYS, AFTER_60_DAYS, AFTER_90_DAYS, AFTER_180_DAYS, AFTER_270_DAYS and AFTER_365_DAYS.
  scope: per lifecycle policy; maximum; not adjustable; TransitionToIA.
  link: [AFTER_7_DAYS](../facts/efs.md#efs-lifecycle-transition-to-ia-valid-values)
efs-lifecycle-transition-to-standard-on-first-access
  claim: For performance-sensitive use cases that need the fastest latency, such as applications with many small files, you can set the lifecycle policy to transition files back into Standard storage on first access.
  scope: EFS lifecycle policy, Transition into Standard.
  link: [fastest latency performance](../facts/efs.md#efs-lifecycle-transition-to-standard-on-first-access)
  link: [transition files into Standard storage](../facts/efs.md#efs-lifecycle-transition-to-standard-on-first-access)
efs-limit-directory-depth
  claim: The number of levels for directory depth in an EFS file system is 1,000.
  scope: per file system; maximum; not adjustable.
  link: [1,000](../facts/efs.md#efs-limit-directory-depth)
efs-limit-file-name-length
  claim: File name length is limited to 255 bytes in an EFS file system.
  scope: per file name; maximum; not adjustable.
  link: [255 bytes](../facts/efs.md#efs-limit-file-name-length)
efs-limit-file-system-policy-characters
  claim: The character limit for each EFS file system policy is 20,000.
  scope: per file system policy; maximum; not adjustable.
  link: [20,000](../facts/efs.md#efs-limit-file-system-policy-characters)
efs-limit-general-purpose-file-operations
  claim: The number of file operations per second for General Purpose mode is 250,000.
  scope: per file system, per second, General Purpose mode; maximum; not adjustable.
  link: [250,000](../facts/efs.md#efs-limit-general-purpose-file-operations)
efs-limit-hard-links-per-file
  claim: The number of hard links to a file is 177 in an EFS file system.
  scope: per file; maximum; not adjustable.
  link: [177](../facts/efs.md#efs-limit-hard-links-per-file)
efs-limit-locks-per-file
  claim: The number of locks on a single file across all instances and users is 512 in an EFS file system.
  scope: per file; maximum; not adjustable.
  link: [512](../facts/efs.md#efs-limit-locks-per-file)
efs-limit-nfs-active-users-open-files
  claim: Up to 65,536 active users for each client can have files open at the same time.
  scope: per client; maximum; not adjustable.
  link: [65,536 active users](../facts/efs.md#efs-limit-nfs-active-users-open-files)
efs-limit-nfs-client-throughput-elastic
  claim: For file systems using Elastic throughput and mounted with amazon-efs-utils version 2.0 or later or the Amazon EFS CSI Driver, the maximum combined read and write throughput for a Linux NFSv4.1 client is 1,500 mebibytes per second (MiBps).
  scope: per NFS client (Linux NFSv4.1); maximum; not adjustable; Elastic throughput; mounted with amazon-efs-utils 2.0 or later or the EFS CSI Driver.
  link: [1,500 mebibytes per second](../facts/efs.md#efs-limit-nfs-client-throughput-elastic)
efs-limit-nfs-client-throughput-other
  claim: For a Linux NFSv4.1 client, the maximum throughput for all file systems other than those using Elastic throughput with the newer EFS client or CSI driver is 500 MiBps.
  scope: per NFS client (Linux NFSv4.1); maximum; not adjustable; all other file systems.
  link: [500 MiBps](../facts/efs.md#efs-limit-nfs-client-throughput-other)
efs-limit-nfs-group-ids-per-user
  claim: The NFS protocol supports a maximum of 16 group IDs (GIDs) per user and additional GIDs are truncated from NFS client requests.
  scope: per user; maximum; not adjustable.
  link: [16 group IDs](../facts/efs.md#efs-limit-nfs-group-ids-per-user)
efs-limit-nfs-latency-for-max-per-client-throughput
  claim: Network latency of 1 ms or less is required to achieve maximum per-client throughput to EFS.
  scope: per client connection; maximum; not adjustable.
  link: [1 ms or less](../facts/efs.md#efs-limit-nfs-latency-for-max-per-client-throughput)
efs-limit-nfs-locks-per-connection
  claim: Each unique mount on the client can acquire up to a total of 65,536 locks per connection.
  scope: per unique mount on the client, per connection; maximum; not adjustable.
  link: [65,536 locks](../facts/efs.md#efs-limit-nfs-locks-per-connection)
efs-limit-nfs-open-files-per-instance
  claim: Up to 65,536 files can be open at the same time on the instance; listing directory contents does not count as opening a file.
  scope: per instance; maximum; not adjustable.
  link: [65,536 files](../facts/efs.md#efs-limit-nfs-open-files-per-instance)
efs-limit-nfs-request-accounting-4kb
  claim: Every Network File System (NFS) request is accounted for as 4 kilobyte (KB) of throughput, or its actual request and response size, whichever is larger.
  scope: per NFS request; minimum; not adjustable.
  link: [4 kilobyte](../facts/efs.md#efs-limit-nfs-request-accounting-4kb)
efs-limit-single-file-size
  claim: The size of a single file in an EFS file system is limited to 52,673,613,135,872 bytes (47.9 TiB).
  scope: per file; maximum; not adjustable.
  link: [47.9 TiB](../facts/efs.md#efs-limit-single-file-size)
efs-limit-symlink-length
  claim: Symbolic link (symlink) length is limited to 4,080 bytes in an EFS file system.
  scope: per symbolic link; maximum; not adjustable.
  link: [4,080 bytes](../facts/efs.md#efs-limit-symlink-length)
efs-max-io-not-supported-one-zone-or-elastic
  claim: Max I/O performance mode is a previous generation mode and is not supported for One Zone file systems or for file systems that use Elastic throughput.
  scope: EFS performance modes.
  link: [not supported for One Zone file systems](../facts/efs.md#efs-max-io-not-supported-one-zone-or-elastic)
  link: [file systems that use Elastic throughput](../facts/efs.md#efs-max-io-not-supported-one-zone-or-elastic)
efs-metadata-always-stored-in-standard
  claim: File metadata, including file names, ownership information and the directory structure, is always stored in the Standard storage class.
  scope: EFS lifecycle management.
  link: [always stored in Standard](../facts/efs.md#efs-metadata-always-stored-in-standard)
  link: [file names, ownership information](../facts/efs.md#efs-metadata-always-stored-in-standard)
efs-metadata-operations-do-not-count-as-access
  claim: Metadata operations on files in IA or Archive storage, such as listing the contents of a directory, do not count as file access.
  scope: EFS lifecycle management.
  link: [listing the contents of a directory](../facts/efs.md#efs-metadata-operations-do-not-count-as-access)
  link: [don't count as file access](../facts/efs.md#efs-metadata-operations-do-not-count-as-access)
efs-metering-elastic-data-increments
  claim: With Elastic throughput, data operations are metered in 1 KiB increments after the first 32 KiB.
  scope: Elastic throughput, data operations; fixed.
  link: [1 KiB increments after the first 32 KiB](../facts/efs.md#efs-metering-elastic-data-increments)
efs-metering-elastic-metadata-increments
  claim: With Elastic throughput, metadata operations are metered in 1 KiB increments after the first 4 KiB.
  scope: Elastic throughput, metadata operations; fixed.
  link: [1 KiB increments after the first 4 KiB](../facts/efs.md#efs-metering-elastic-metadata-increments)
efs-metering-ia-archive-access-128kib
  claim: Data access for IA and Archive storage is metered in 128 KiB increments.
  scope: IA and Archive storage classes, data access; fixed.
  link: [128 KiB increments](../facts/efs.md#efs-metering-ia-archive-access-128kib)
efs-metering-ia-archive-metadata-in-standard
  claim: IA and Archive file metadata (2 KiB per file) is always stored and metered in the Standard storage class.
  scope: per file, IA and Archive; fixed.
  link: [2 KiB per file](../facts/efs.md#efs-metering-ia-archive-metadata-in-standard)
efs-metering-new-file-system-size
  claim: Upon creation, a file system has a single empty root directory and therefore has a metered size of 6 KiB.
  scope: per new file system; fixed; not adjustable.
  link: [6 KiB](../facts/efs.md#efs-metering-new-file-system-size)
efs-metering-object-metadata-and-data-increments
  claim: Each EFS file system object is metered for 2 kibibytes (KiB) of metadata (for its inode) and one or more increments of 4 KiB of data.
  scope: per object; fixed.
  link: [2 kibibytes](../facts/efs.md#efs-metering-object-metadata-and-data-increments)
  link: [4 KiB](../facts/efs.md#efs-metering-object-metadata-and-data-increments)
efs-metering-provisioned-hourly
  claim: Amazon EFS meters file systems with Provisioned throughput mode enabled once every hour.
  scope: Provisioned throughput; fixed.
  link: [once every hour](../facts/efs.md#efs-metering-provisioned-hourly)
efs-metering-provisioned-pay-for-time-enabled
  claim: For file systems that use Provisioned throughput mode, you pay only for the amount of time that throughput is enabled.
  scope: Provisioned throughput.
  link: [amount of time that throughput is enabled](../facts/efs.md#efs-metering-provisioned-pay-for-time-enabled)
efs-metering-read-requests-one-third
  claim: Amazon EFS meters the throughput for read requests at one-third the rate of the other file system I/O operations.
  scope: read requests; fixed.
  link: [one-third the rate](../facts/efs.md#efs-metering-read-requests-one-third)
efs-metric-storagebytes-emitted-every-15-minutes
  claim: The EFS StorageBytes metric, the size of the file system in bytes including the data stored in the EFS storage classes, is emitted to CloudWatch every 15 minutes.
  scope: StorageBytes metric, per file system; fixed.
  link: [every 15 minutes](../facts/efs.md#efs-metric-storagebytes-emitted-every-15-minutes)
efs-metric-storagebytes-total-rounds-small-files
  claim: In the Total dimension of the EFS storage metric, the metered size of data stored in the file system in all storage classes, files smaller than 128KiB in the EFS Infrequent Access (IA) and EFS Archive storage classes are rounded to 128KiB.
  scope: StorageBytes metric, Total dimension.
  link: [rounded to 128KiB](../facts/efs.md#efs-metric-storagebytes-total-rounds-small-files)
efs-min-billing-per-file-ia-archive
  claim: The EFS Infrequent Access (IA) and Archive storage classes have a minimum billing charge per file of 128 KiB.
  scope: per file, IA and Archive storage classes; minimum.
  link: [128 KiB](../facts/efs.md#efs-min-billing-per-file-ia-archive)
efs-mount-helper-recommended-nfs-alternative
  claim: AWS recommends the EFS mount helper for mounting EFS file systems on EC2 Linux and Mac instances; as an alternative you can mount manually with the standard Linux NFS client.
  scope: Amazon EFS clients.
  link: [use the EFS mount helper](../facts/efs.md#efs-mount-helper-recommended-nfs-alternative)
  link: [standard Linux NFS client](../facts/efs.md#efs-mount-helper-recommended-nfs-alternative)
efs-mount-helper-tls-option-encrypts-nfs-traffic
  claim: When encryption of data in transit is declared as a mount option, Amazon EFS establishes a secure TLS connection when the file system is mounted, and all NFS traffic is routed through it.
  scope: Amazon EFS encryption in transit.
  link: [establishes a secure TLS connection](../facts/efs.md#efs-mount-helper-tls-option-encrypts-nfs-traffic)
  link: [All NFS traffic is routed](../facts/efs.md#efs-mount-helper-tls-option-encrypts-nfs-traffic)
  link: [declared as a mount option](../facts/efs.md#efs-mount-helper-tls-option-encrypts-nfs-traffic)
efs-mount-target-created-at-or-after-file-system-creation
  claim: You can create a mount target when you create the file system or after, and later you can add mount targets, delete them, and change their security groups.
  scope: EFS mount target.
  link: [create additional mount targets](../facts/efs.md#efs-mount-target-created-at-or-after-file-system-creation)
  link: [modify the security groups for mount targets](../facts/efs.md#efs-mount-target-created-at-or-after-file-system-creation)
efs-mount-target-definition-ip-nfs-endpoint
  claim: A mount target provides an IP address for an NFSv4 endpoint at which you can mount an EFS file system; to access a file system in a VPC you create one or more mount targets in that VPC.
  scope: EFS mount target.
  link: [provides an IP address for an NFSv4 endpoint](../facts/efs.md#efs-mount-target-definition-ip-nfs-endpoint)
  link: [one or more mount targets in the VPC](../facts/efs.md#efs-mount-target-definition-ip-nfs-endpoint)
efs-mount-target-ip-address-cannot-change
  claim: You cannot change the IP address of an existing mount target; to change it you delete the mount target and create a new one with the new address.
  scope: EFS mount target.
  link: [can't change the IP address](../facts/efs.md#efs-mount-target-ip-address-cannot-change)
  link: [delete the mount target and create](../facts/efs.md#efs-mount-target-ip-address-cannot-change)
efs-mount-target-vpc-change-requires-deleting-targets
  claim: To modify the VPC for mount targets you must first delete the existing mount targets.
  scope: EFS mount target.
  link: [first delete the existing mount targets](../facts/efs.md#efs-mount-target-vpc-change-requires-deleting-targets)
  link: [modify the VPC for mount targets](../facts/efs.md#efs-mount-target-vpc-change-requires-deleting-targets)
efs-mount-targets-highly-available-static-ip-dns
  claim: EFS mount targets are designed to be highly available, and their IP addresses and DNS names in each Availability Zone are static even though they are redundant components backed by multiple resources.
  scope: EFS mount target.
  link: [designed to be highly available](../facts/efs.md#efs-mount-targets-highly-available-static-ip-dns)
  link: [IP addresses and DNS for your mount targets](../facts/efs.md#efs-mount-targets-highly-available-static-ip-dns)
  link: [are static](../facts/efs.md#efs-mount-targets-highly-available-static-ip-dns)
efs-mount-targets-only-one-vpc-at-a-time
  claim: An EFS file system can have mount targets in only one VPC at a time.
  scope: EFS file system.
  link: [only one VPC at a time](../facts/efs.md#efs-mount-targets-only-one-vpc-at-a-time)
  link: [can have mount targets](../facts/efs.md#efs-mount-targets-only-one-vpc-at-a-time)
efs-nfs-client-needs-network-connection-to-port-2049
  claim: An NFSv4.1 client can only mount an EFS file system if it can make a network connection to the NFS port (TCP port 2049) of one of the file system's mount targets.
  scope: EFS mount target network access.
  link: [NFS port (TCP port 2049)](../facts/efs.md#efs-nfs-client-needs-network-connection-to-port-2049)
  link: [can only mount a file system](../facts/efs.md#efs-nfs-client-needs-network-connection-to-port-2049)
efs-nfs-throughput-metering-read-one-third
  claim: NFS client throughput is calculated as the total number of bytes that are sent and received, with a minimum NFS request size of 4 KB (after applying a 1/3 metering rate for read requests).
  scope: per NFS client; minimum; not adjustable.
  link: [minimum NFS request size of 4 KB](../facts/efs.md#efs-nfs-throughput-metering-read-one-third)
efs-no-data-access-charges-with-aws-backup
  claim: You do not incur data access charges when you use AWS Backup to back up lifecycle-management-enabled EFS file systems.
  scope: EFS storage classes and AWS Backup.
  link: [don't incur data access charges](../facts/efs.md#efs-no-data-access-charges-with-aws-backup)
  link: [AWS Backup to back up](../facts/efs.md#efs-no-data-access-charges-with-aws-backup)
efs-one-mount-target-per-az-shared-by-instances
  claim: You can create one mount target in each Availability Zone in a Region; if the VPC has several subnets in that zone you create it in one of them, and all EC2 instances in that zone share it.
  scope: EFS mount target, per Availability Zone.
  link: [one mount target in each Availability Zone](../facts/efs.md#efs-one-mount-target-per-az-shared-by-instances)
  link: [mount target in one of the subnets](../facts/efs.md#efs-one-mount-target-per-az-shared-by-instances)
  link: [share that mount target](../facts/efs.md#efs-one-mount-target-per-az-shared-by-instances)
efs-one-zone-always-general-purpose
  claim: One Zone file systems always use the General Purpose performance mode.
  scope: One Zone file system.
  link: [always use the General Purpose performance mode](../facts/efs.md#efs-one-zone-always-general-purpose)
  link: [One Zone file systems](../facts/efs.md#efs-one-zone-always-general-purpose)
efs-one-zone-bursting-same-as-regional
  claim: One Zone file systems that use Bursting throughput can drive the same per-file-system read and write throughput amounts as Regional file systems using Bursting throughput (maximum read of 5 GiBps for read and 3 GiBps for write).
  scope: One Zone file systems with Bursting throughput; maximum.
  link: [5 GiBps](../facts/efs.md#efs-one-zone-bursting-same-as-regional)
efs-one-zone-max-throughput-elastic-provisioned
  claim: Total default Elastic and Provisioned throughput for a One Zone file system in all AWS Regions is a maximum read of 3 GiBps and a maximum write (metered) throughput of 1 GiBps.
  scope: per One Zone file system, for all connected clients, in all Regions; maximum; not adjustable.
  link: [3 GiBps](../facts/efs.md#efs-one-zone-max-throughput-elastic-provisioned)
  link: [1 GiBps](../facts/efs.md#efs-one-zone-max-throughput-elastic-provisioned)
efs-onezone-automatic-backup-aws-backup
  claim: Amazon EFS automatically backs up One Zone file systems with AWS Backup, and you can restore a backup to any operational Availability Zone in the Region or to a different Region.
  scope: One Zone file system.
  link: [backs up One Zone file systems](../facts/efs.md#efs-onezone-automatic-backup-aws-backup)
  link: [different AWS Region](../facts/efs.md#efs-onezone-automatic-backup-aws-backup)
efs-onezone-az-loss-data-may-be-lost
  claim: If all or part of the Availability Zone is lost or damaged, for example by fire or water damage, data in a One Zone file system may be lost.
  scope: One Zone file system.
  link: [One Zone storage class may be lost](../facts/efs.md#efs-onezone-az-loss-data-may-be-lost)
  link: [fire and water damage](../facts/efs.md#efs-onezone-az-loss-data-may-be-lost)
efs-onezone-ecs-eks-lambda-same-az-subnets
  claim: When you use a One Zone file system with Amazon ECS, Amazon EKS or AWS Lambda, you need to configure the service to use the same Availability Zone as the file system: with Amazon ECS you should choose only subnets in that Availability Zone when launching your task, and with Lambda you configure your function to only launch invocations into subnets in that Availability Zone.
  scope: One Zone file system with ECS and Lambda.
  link: [subnets that are in the same Availability Zone](../facts/efs.md#efs-onezone-ecs-eks-lambda-same-az-subnets)
  link: [only launch invocations into subnets](../facts/efs.md#efs-onezone-ecs-eks-lambda-same-az-subnets)
efs-onezone-not-resilient-to-az-outage
  claim: EFS One Zone file systems are not resilient to a complete Availability Zone outage; during an outage you lose availability because the data is not replicated to a different Availability Zone.
  scope: One Zone file system.
  link: [not resilient to a complete AZ outage](../facts/efs.md#efs-onezone-not-resilient-to-az-outage)
  link: [loss of availability](../facts/efs.md#efs-onezone-not-resilient-to-az-outage)
efs-onezone-only-certain-azs
  claim: One Zone file systems are available only in certain Availability Zones.
  scope: One Zone file system.
  link: [available to only certain Availability Zones](../facts/efs.md#efs-onezone-only-certain-azs)
  link: [One Zone file systems are available](../facts/efs.md#efs-onezone-only-certain-azs)
efs-onezone-other-az-mount-needs-az-name-or-mount-target-dns
  claim: To mount a One Zone file system on an EC2 instance in a different Availability Zone, you have to specify the file system's Availability Zone name or the DNS name of its mount target in the mount helper command.
  scope: One Zone file system.
  link: [specify the file system's Availability Zone name](../facts/efs.md#efs-onezone-other-az-mount-needs-az-name-or-mount-target-dns)
  link: [DNS name of the file system's mount target](../facts/efs.md#efs-onezone-other-az-mount-needs-az-name-or-mount-target-dns)
efs-onezone-same-az-avoids-transfer-charges-better-performance
  claim: Accessing a One Zone file system from an EC2 instance in the same Availability Zone as the file system's mount target avoids data transfer charges between Availability Zones and gives better performance.
  scope: One Zone file system.
  link: [avoid data transfer charges between Availability Zones](../facts/efs.md#efs-onezone-same-az-avoids-transfer-charges-better-performance)
  link: [achieve better performance](../facts/efs.md#efs-onezone-same-az-avoids-transfer-charges-better-performance)
  link: [located in the same Availability Zone](../facts/efs.md#efs-onezone-same-az-avoids-transfer-charges-better-performance)
efs-onezone-single-mount-target-same-az
  claim: A One Zone file system supports only a single mount target, located in the same Availability Zone as the file system; you cannot add additional mount targets.
  scope: One Zone file system.
  link: [support only a single mount target](../facts/efs.md#efs-onezone-single-mount-target-same-az)
  link: [You cannot add additional mount targets](../facts/efs.md#efs-onezone-single-mount-target-same-az)
efs-onpremises-mount-via-direct-connect-or-vpn
  claim: You can mount EFS file systems on on-premises data center servers when they are connected to your VPC with AWS Direct Connect or Site-to-Site VPN.
  scope: Amazon EFS, on-premises access.
  link: [AWS Direct Connect or Site-to-Site VPN](../facts/efs.md#efs-onpremises-mount-via-direct-connect-or-vpn)
  link: [on your on-premises data center servers](../facts/efs.md#efs-onpremises-mount-via-direct-connect-or-vpn)
efs-onpremises-no-extra-cost-pay-direct-connect
  claim: There is no additional cost for on-premises access to EFS file systems; you are charged for the Direct Connect connection to your VPC.
  scope: Amazon EFS, on-premises access.
  link: [no additional cost for on-premises access](../facts/efs.md#efs-onpremises-no-extra-cost-pay-direct-connect)
  link: [charged for the Direct Connect connection](../facts/efs.md#efs-onpremises-no-extra-cost-pay-direct-connect)
efs-onpremises-security-group-allow-nfs-port-2049
  claim: To reach EFS from an on-premises server you add a rule to the mount target security group that allows inbound traffic to the NFS port (2049) from that server.
  scope: EFS mount target security group.
  link: [NFS port (2049)](../facts/efs.md#efs-onpremises-security-group-allow-nfs-port-2049)
  link: [allow inbound traffic](../facts/efs.md#efs-onpremises-security-group-allow-nfs-port-2049)
  link: [mount target security group](../facts/efs.md#efs-onpremises-security-group-allow-nfs-port-2049)
efs-onpremises-server-must-be-linux
  claim: An on-premises server that mounts EFS must have a Linux-based operating system.
  scope: Amazon EFS, on-premises access.
  link: [must have a Linux-based operating system](../facts/efs.md#efs-onpremises-server-must-be-linux)
  link: [on-premises server](../facts/efs.md#efs-onpremises-server-must-be-linux)
efs-onpremises-use-mount-target-ip-instead-of-dns
  claim: AWS recommends mounting an EFS file system on an on-premises server by using a mount target IP address instead of a DNS name.
  scope: Amazon EFS, on-premises access.
  link: [mount target IP address instead of](../facts/efs.md#efs-onpremises-use-mount-target-ip-instead-of-dns)
  link: [using a mount target IP address](../facts/efs.md#efs-onpremises-use-mount-target-ip-instead-of-dns)
efs-other-account-or-vpc-resolve-mount-target-manually
  claim: By default the EFS mount helper uses DNS to resolve the mount target IP address, so when you mount from a different account or VPC you need to resolve the mount target manually.
  scope: Amazon EFS, cross-account or cross-VPC mount.
  link: [a different account or virtual private cloud](../facts/efs.md#efs-other-account-or-vpc-resolve-mount-target-manually)
  link: [resolve the EFS mount target manually](../facts/efs.md#efs-other-account-or-vpc-resolve-mount-target-manually)
efs-overview-regional-linux-shared-access
  claim: The AWS overview whitepaper describes Amazon EFS as a regional service that stores data within and across multiple Availability Zones for high availability and durability, and as fully managed with no changes needed to existing applications and tools.
  scope: Amazon EFS.
  link: [within and across multiple Availability Zones (AZs)](../facts/efs.md#efs-overview-regional-linux-shared-access)
  link: [requires no changes to your existing applications](../facts/efs.md#efs-overview-regional-linux-shared-access)
efs-overview-thousands-of-instances-and-on-premises
  claim: The AWS overview whitepaper says you can access EFS file systems across Availability Zones and AWS Regions and share files between thousands of Amazon EC2 instances and on-premises servers through Direct Connect or Site-to-Site VPN.
  scope: Amazon EFS.
  link: [thousands of Amazon EC2 instances and on-premises servers](../facts/efs.md#efs-overview-thousands-of-instances-and-on-premises)
efs-performance-mode-cannot-change-after-available
  claim: You cannot change the performance mode after the file system becomes available.
  scope: EFS performance mode.
  link: [cannot change the performance mode](../facts/efs.md#efs-performance-mode-cannot-change-after-available)
  link: [after the file system becomes available](../facts/efs.md#efs-performance-mode-cannot-change-after-available)
efs-posix-permissions-and-no-code-change-for-nfs-apps
  claim: Amazon EFS supports controlling access to file systems through Portable Operating System Interface (POSIX) permissions.
  scope: Amazon EFS.
  link: [controlling access to your file systems](../facts/efs.md#efs-posix-permissions-and-no-code-change-for-nfs-apps)
  link: [Portable Operating System Interface (POSIX) permissions](../facts/efs.md#efs-posix-permissions-and-no-code-change-for-nfs-apps)
efs-pricing-cross-az-transfer-rate
  claim: If you access your EFS mount target from another AZ, you are charged the EC2 cross-AZ data transfer rate ($0.01/GB) for data transfer in and out of the AZ.
  scope: per GB, cross-AZ access to an EFS mount target.
  link: [$0.01/GB](../facts/efs.md#efs-pricing-cross-az-transfer-rate)
efs-pricing-dimensions-storage-activity
  claim: AWS says you pay for EFS by the primary and backup storage you use and by your read, write and tiering activity. There is no minimum fee or setup charge.
  scope: Amazon EFS billing.
  link: [no minimum fee or setup charge](../facts/efs.md#efs-pricing-dimensions-storage-activity)
  link: [read, write, and tiering activity](../facts/efs.md#efs-pricing-dimensions-storage-activity)
efs-pricing-elastic-default-pay-for-throughput-used
  claim: AWS says Elastic Throughput is the default throughput mode for EFS and is recommended for most workloads. With Elastic Throughput, performance scales automatically with your workload activity and you pay only for the throughput you use.
  scope: new EFS file systems; default; adjustable; throughput mode can be changed.
  link: [Elastic Throughput is the default throughput mode](../facts/efs.md#efs-pricing-elastic-default-pay-for-throughput-used)
efs-pricing-no-charge-same-az-access
  claim: AWS says there are no data transfer charges when you access an EFS mount target from within the same Availability Zone, or when you replicate data across EFS file systems within the same Availability Zone.
  scope: EFS data transfer within one Region.
  link: [no data transfer charges](../facts/efs.md#efs-pricing-no-charge-same-az-access)
  link: [from within the same Availability Zone (AZ)](../facts/efs.md#efs-pricing-no-charge-same-az-access)
efs-pricing-one-zone-for-no-multi-az-need
  claim: AWS says EFS One Zone file systems are ideal for applications that do not require the Multi-AZ availability and durability of EFS Regional file systems.
  scope: EFS One Zone.
  link: [do not require the Multi-AZ availability and durability](../facts/efs.md#efs-pricing-one-zone-for-no-multi-az-need)
efs-pricing-provisioned-excess-over-baseline
  claim: The Provisioned throughput amount billed in a month is based on the throughput provisioned in excess of the file system’s included baseline throughput from Standard storage, up to the prevailing Bursting baseline throughput limits in the AWS Region.
  scope: Provisioned throughput, per month.
  link: [in excess of your file system’s included baseline](../facts/efs.md#efs-pricing-provisioned-excess-over-baseline)
efs-pricing-provisioned-throughput-predictable-sustained
  claim: AWS says to use EFS Provisioned Throughput if you have predictable and high levels of sustained throughput requirements, and that the amount billed in a month is based on the average throughput provisioned in excess of the baseline throughput included with your EFS Standard storage usage.
  scope: EFS Provisioned Throughput.
  link: [predictable and high levels of sustained throughput requirements](../facts/efs.md#efs-pricing-provisioned-throughput-predictable-sustained)
efs-pricing-replication-pays-both-file-systems
  claim: AWS says that with EFS Replication you pay the prevailing storage and read, write and tiering activity rates for both the source and the destination EFS file system, plus any applicable data transfer charges between them.
  scope: EFS Replication billing.
  link: [source and destination EFS file systems](../facts/efs.md#efs-pricing-replication-pays-both-file-systems)
efs-protocol-nfsv4-versions
  claim: Amazon EFS supports the Network File System version 4 protocol, in the versions NFSv4.1 and NFSv4.0.
  scope: Amazon EFS.
  link: [NFSv4.1 and NFSv4.0](../facts/efs.md#efs-protocol-nfsv4-versions)
  link: [Network File System version 4](../facts/efs.md#efs-protocol-nfsv4-versions)
efs-provisioned-24-hour-wait-before-switch-or-decrease
  claim: After you change a file system to Provisioned throughput or increase the provisioned amount, you must wait at least 24 hours before you can change the throughput mode again or decrease the provisioned amount.
  scope: EFS Provisioned throughput.
  link: [wait at least 24 hours](../facts/efs.md#efs-provisioned-24-hour-wait-before-switch-or-decrease)
  link: [change the throughput mode again](../facts/efs.md#efs-provisioned-24-hour-wait-before-switch-or-decrease)
efs-provisioned-billed-for-throughput-enabled
  claim: For file systems using Provisioned throughput, you are charged for the amount of throughput enabled for the file system.
  scope: EFS Provisioned throughput.
  link: [charged for the amount of throughput enabled](../facts/efs.md#efs-provisioned-billed-for-throughput-enabled)
  link: [Provisioned throughput](../facts/efs.md#efs-provisioned-billed-for-throughput-enabled)
efs-provisioned-regional-max-throughput-major-regions
  claim: Total default Provisioned throughput for a Regional file system in US East (Ohio), US East (N. Virginia), US West (Oregon) and Europe (Ireland) is a maximum read of 10 GiBps and a maximum write (metered) throughput of 3.33 GiBps.
  scope: per Regional file system, for all connected clients, in the listed Regions; maximum; adjustable; increase through AWS Support.
  link: [10 GiBps](../facts/efs.md#efs-provisioned-regional-max-throughput-major-regions)
  link: [3.33 GiBps](../facts/efs.md#efs-provisioned-regional-max-throughput-major-regions)
efs-provisioned-regional-max-throughput-other-regions
  claim: Total default Provisioned throughput for a Regional file system in all other AWS Regions is a maximum read of 3 GiBps and a maximum write (metered) throughput of 1 GiBps.
  scope: per Regional file system, for all connected clients, in all other Regions; maximum; adjustable; increase through AWS Support.
  link: [3 GiBps](../facts/efs.md#efs-provisioned-regional-max-throughput-other-regions)
  link: [1 GiBps](../facts/efs.md#efs-provisioned-regional-max-throughput-other-regions)
efs-provisioned-throughput-independent-of-size
  claim: With Provisioned throughput you specify a level of throughput that the file system can drive, independent of the file system's size or burst credit balance.
  scope: EFS Provisioned throughput.
  link: [you specify a level of throughput](../facts/efs.md#efs-provisioned-throughput-independent-of-size)
  link: [independent of the file system's size](../facts/efs.md#efs-provisioned-throughput-independent-of-size)
efs-provisioned-use-when-known-needs-5-percent-or-more
  claim: Use Provisioned throughput if you know your workload's performance requirements, or if your application drives throughput at 5% or more of the average-to-peak ratio.
  scope: EFS Provisioned throughput.
  link: [know your workload's performance requirements](../facts/efs.md#efs-provisioned-use-when-known-needs-5-percent-or-more)
  link: [5% or more of the average-to-peak ratio](../facts/efs.md#efs-provisioned-use-when-known-needs-5-percent-or-more)
efs-public-policy-evaluation-assumes-public-until-fixed-values
  claim: To decide whether a file system policy is public, Amazon EFS assumes the policy is public and then evaluates whether it qualifies as non-public.
  scope: EFS block public access.
  link: [assumes that the file system policy is public](../facts/efs.md#efs-public-policy-evaluation-assumes-public-until-fixed-values)
  link: [qualifies as non-public](../facts/efs.md#efs-public-policy-evaluation-assumes-public-until-fixed-values)
efs-quota-access-points-per-file-system
  claim: A file system can have a maximum of 10,000 access points unless you request an increase. Since February 10, 2025 the maximum is 10,000; it was 1,000 before.
  scope: per file system; maximum; adjustable; you can request an increase.
  link: [10,000](../facts/efs.md#efs-quota-access-points-per-file-system)
  changed: 2025-02-10: was 1,000
efs-quota-connections-per-file-system
  claim: The number of connections for each EFS file system is 25,000.
  scope: per file system; maximum; not adjustable.
  link: [25,000](../facts/efs.md#efs-quota-connections-per-file-system)
efs-quota-elastic-iops-increase-factor
  claim: By default, file systems that use Elastic throughput drive a maximum of 90,000 read IOPS for infrequently accessed data, 250,000 read IOPS for frequently accessed data and 50,000 write IOPS; if your workload requires more IOPS, you can request an increase of up to 10 times these numbers.
  scope: per file system, Elastic throughput; maximum; adjustable; request through quota increase.
  link: [10 times](../facts/efs.md#efs-quota-elastic-iops-increase-factor)
efs-quota-mount-targets-per-az
  claim: The quota for mount targets is 1 mount target for each file system in an Availability Zone.
  scope: per file system, per Availability Zone; maximum; not adjustable.
  link: [1 mount target](../facts/efs.md#efs-quota-mount-targets-per-az)
efs-quota-mount-targets-per-vpc
  claim: The quota is 1,400 mount targets for each virtual private cloud (VPC).
  scope: per VPC; maximum; not adjustable.
  link: [1,400 mount targets](../facts/efs.md#efs-quota-mount-targets-per-vpc)
efs-quota-security-groups-per-mount-target
  claim: The quota for security groups is 5 security groups for each mount target.
  scope: per mount target; maximum; not adjustable.
  link: [5 security groups](../facts/efs.md#efs-quota-security-groups-per-mount-target)
efs-quota-tags-per-file-system
  claim: The quota for tags is 50 tags for each file system.
  scope: per file system; maximum; not adjustable.
  link: [50 tags](../facts/efs.md#efs-quota-tags-per-file-system)
efs-quota-vpcs-per-file-system
  claim: The quota is 1 VPC for each file system.
  scope: per file system; maximum; not adjustable.
  link: [1 VPC](../facts/efs.md#efs-quota-vpcs-per-file-system)
efs-read-throughput-discounted
  claim: EFS discounts read throughput so that you can drive higher read throughput than write throughput.
  scope: EFS throughput modes.
  link: [Read throughput is discounted](../facts/efs.md#efs-read-throughput-discounted)
  link: [higher read throughput than write throughput](../facts/efs.md#efs-read-throughput-discounted)
efs-region-property-for-cross-region-mount
  claim: To mount an EFS file system from an EC2 instance in a different AWS Region than the file system, you must edit the region property in the efs-utils.conf file.
  scope: Amazon EFS, cross-Region mount.
  link: [different AWS Region than the file system](../facts/efs.md#efs-region-property-for-cross-region-mount)
  link: [efs-utils.conf](../facts/efs.md#efs-region-property-for-cross-region-mount)
efs-regional-designed-to-sustain-az-loss
  claim: EFS Regional file systems are designed to sustain data if an Availability Zone is lost, and they support concurrent access from mount targets in all Availability Zones of the Region.
  scope: Regional file system.
  link: [sustain data if an AZ is lost](../facts/efs.md#efs-regional-designed-to-sustain-az-loss)
  link: [concurrent access from EFS mount targets](../facts/efs.md#efs-regional-designed-to-sustain-az-loss)
efs-regional-mount-target-per-az-same-az-access
  claim: For a Regional file system a mount target is created in each Availability Zone, and AWS recommends that you access the file system through the mount target in the same Availability Zone for performance and cost reasons.
  scope: Regional file system; default; not adjustable.
  link: [a mount target was created in each](../facts/efs.md#efs-regional-mount-target-per-az-same-az-access)
  link: [within the same Availability Zone](../facts/efs.md#efs-regional-mount-target-per-az-same-az-access)
  link: [for performance and cost reasons](../facts/efs.md#efs-regional-mount-target-per-az-same-az-access)
efs-regional-multi-az-continuous-availability
  claim: A Regional EFS file system stores data redundantly across multiple Availability Zones in one AWS Region, which keeps the data continuously available even when one or more Availability Zones are unavailable.
  scope: Regional file system.
  link: [continuous availability to the data](../facts/efs.md#efs-regional-multi-az-continuous-availability)
  link: [even when one or more Availability Zones](../facts/efs.md#efs-regional-multi-az-continuous-availability)
efs-regional-recommended-type
  claim: Regional is the recommended EFS file system type; it stores data redundantly across multiple geographically separated Availability Zones within the same AWS Region.
  scope: Regional file system.
  link: [Regional file systems (recommended)](../facts/efs.md#efs-regional-recommended-type)
  link: [multiple geographically separated Availability Zones](../facts/efs.md#efs-regional-recommended-type)
efs-replication-automatic-transparent-data-and-metadata
  claim: When you enable replication, Amazon EFS automatically and transparently replicates the data and metadata of the source file system to a destination file system.
  scope: EFS replication.
  link: [automatically and transparently replicates](../facts/efs.md#efs-replication-automatic-transparent-data-and-metadata)
  link: [data and metadata on the source file system](../facts/efs.md#efs-replication-automatic-transparent-data-and-metadata)
efs-replication-available-all-efs-regions
  claim: Replication is available in all AWS Regions in which Amazon EFS is available.
  scope: EFS replication.
  link: [available in all AWS Regions](../facts/efs.md#efs-replication-available-all-efs-regions)
  link: [in which Amazon EFS is available](../facts/efs.md#efs-replication-available-all-efs-regions)
efs-replication-cannot-delete-file-system-in-configuration
  claim: You cannot delete a file system that is part of a replication configuration; you must delete the replication configuration first.
  scope: EFS replication.
  link: [cannot delete a file system that is part](../facts/efs.md#efs-replication-cannot-delete-file-system-in-configuration)
  link: [delete the replication configuration before deleting](../facts/efs.md#efs-replication-cannot-delete-file-system-in-configuration)
efs-replication-delete-config-takes-minutes-destination-writeable
  claim: Deleting a replication configuration and changing the destination file system to be writeable can take several minutes, and you can delete the configuration from either the source or the destination file system.
  scope: EFS replication.
  link: [can take several minutes to complete](../facts/efs.md#efs-replication-delete-config-takes-minutes-destination-writeable)
  link: [either the source or the destination](../facts/efs.md#efs-replication-delete-config-takes-minutes-destination-writeable)
efs-replication-destination-faq-region-or-az-of-choice
  claim: You can use EFS Replication to replicate your file system to a Region or Availability Zone of your choice, without managing additional infrastructure or custom processes.
  scope: EFS replication.
  link: [Region or Availability Zone (AZ) of your choice](../facts/efs.md#efs-replication-destination-faq-region-or-az-of-choice)
  link: [without having to manage additional infrastructure](../facts/efs.md#efs-replication-destination-faq-region-or-az-of-choice)
efs-replication-destination-has-no-mount-targets
  claim: Amazon EFS does not create any mount targets when it creates the replication destination file system.
  scope: EFS replication.
  link: [does not create any mount targets](../facts/efs.md#efs-replication-destination-has-no-mount-targets)
  link: [destination file system](../facts/efs.md#efs-replication-destination-has-no-mount-targets)
efs-replication-destination-metered-12-mib-hidden-data
  claim: To facilitate replication, EFS creates hidden directories and metadata on the destination file system, which equal approximately 12 mebibytes (MiB) of metered data that you are billed for.
  scope: EFS replication destination.
  link: [approximately 12 mebibytes (MiB) of metered data](../facts/efs.md#efs-replication-destination-metered-12-mib-hidden-data)
  link: [hidden directories and metadata](../facts/efs.md#efs-replication-destination-metered-12-mib-hidden-data)
efs-replication-destination-new-or-existing-region-of-choice
  claim: EFS Replication copies your file system data into a new or existing file system in the Region of your choice, transferring only incremental changes.
  scope: EFS replication.
  link: [new or existing file system](../facts/efs.md#efs-replication-destination-new-or-existing-region-of-choice)
  link: [only incremental changes](../facts/efs.md#efs-replication-destination-new-or-existing-region-of-choice)
efs-replication-destination-read-only-while-replicating
  claim: The destination file system of EFS replication is read-only while replication is enabled, and applications can use it in read-only mode for low-latency cross-Region access.
  scope: EFS replication.
  link: [new read-only destination file system](../facts/efs.md#efs-replication-destination-read-only-while-replicating)
  link: [use the replica file system in read-only mode](../facts/efs.md#efs-replication-destination-read-only-while-replicating)
efs-replication-failback-discard-or-preserve-changes
  claim: During failback you can choose to discard the changes made to the replica during failover, or preserve them by copying them back to the primary file system.
  scope: EFS replication failback.
  link: [discard the changes made to your replica](../facts/efs.md#efs-replication-failback-discard-or-preserve-changes)
  link: [preserve them by copying them back](../facts/efs.md#efs-replication-failback-discard-or-preserve-changes)
efs-replication-failover-delete-configuration-replica-writeable
  claim: To fail over to the replica file system you delete its replication configuration; after the configuration is deleted the replica becomes writeable and you can use it in your application workflow.
  scope: EFS replication failover.
  link: [by deleting its replication configuration](../facts/efs.md#efs-replication-failover-delete-configuration-replica-writeable)
  link: [the replica becomes writeable](../facts/efs.md#efs-replication-failover-delete-configuration-replica-writeable)
efs-replication-file-system-in-one-configuration-only
  claim: A file system can be part of only one replication configuration, and a destination file system cannot be the source of another replication configuration.
  scope: EFS replication.
  link: [part of only one replication configuration](../facts/efs.md#efs-replication-file-system-in-one-configuration-only)
  link: [cannot use a destination file system](../facts/efs.md#efs-replication-file-system-in-one-configuration-only)
efs-replication-initial-sync-before-replica-accessible
  claim: Replicated data is accessible in the destination file system only after the initial sync completes, and how long that takes depends on the size of the source and the number of files.
  scope: EFS replication.
  link: [only after the initial sync completes](../facts/efs.md#efs-replication-initial-sync-before-replica-accessible)
  link: [size of the source file system](../facts/efs.md#efs-replication-initial-sync-before-replica-accessible)
efs-replication-new-destination-regional-or-one-zone-choice
  claim: When you replicate to a new file system you choose the file system type of the destination, Regional or One Zone, and the KMS key used for encryption.
  scope: EFS replication.
  link: [you choose the file system type](../facts/efs.md#efs-replication-new-destination-regional-or-one-zone-choice)
  link: [redundantly within a single Availability Zone](../facts/efs.md#efs-replication-new-destination-regional-or-one-zone-choice)
efs-replication-no-abac-tags
  claim: EFS replication does not support using tags for attribute-based access control (ABAC).
  scope: EFS replication.
  link: [does not support using tags](../facts/efs.md#efs-replication-no-abac-tags)
  link: [attribute-based access control (ABAC)](../facts/efs.md#efs-replication-no-abac-tags)
efs-replication-not-point-in-time-consistent
  claim: EFS replication is not point-in-time consistent: changes are transferred based on the Last synced time for the replication, and changes made to the source file system after the recorded time might not have been replicated yet.
  scope: EFS replication.
  link: [point-in-time consistent manner](../facts/efs.md#efs-replication-not-point-in-time-consistent)
  link: [doesn't provide point-in-time consistent replication](../facts/efs.md#efs-replication-not-point-in-time-consistent)
efs-replication-rpo-15-minutes-most-file-systems
  claim: After the initial replication finishes, Amazon EFS maintains a recovery point objective (RPO) of 15 minutes for most file systems.
  scope: EFS replication, after initial sync.
  link: [RPO) of 15 minutes](../facts/efs.md#efs-replication-rpo-15-minutes-most-file-systems)
  link: [for most file systems](../facts/efs.md#efs-replication-rpo-15-minutes-most-file-systems)
efs-replication-rpo-longer-large-busy-sources
  claim: If the source file system has files that change very frequently and has either more than 100 million files or files larger than 100 GB, replication may take longer than 15 minutes.
  scope: EFS replication.
  link: [more than 100 million files](../facts/efs.md#efs-replication-rpo-longer-large-busy-sources)
  link: [larger than 100 GB](../facts/efs.md#efs-replication-rpo-longer-large-busy-sources)
  link: [longer than 15 minutes](../facts/efs.md#efs-replication-rpo-longer-large-busy-sources)
efs-replication-rpo-rto-minutes
  claim: EFS replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes.
  scope: EFS replication.
  link: [objective (RTO) of minutes](../facts/efs.md#efs-replication-rpo-rto-minutes)
  link: [Replication is continual](../facts/efs.md#efs-replication-rpo-rto-minutes)
efs-sagemaker-training-jobs-access
  claim: You can access training data in EFS from Amazon SageMaker training jobs by referencing an EFS file system in your CreateTrainingJob request.
  scope: Amazon EFS with SageMaker.
  link: [access training data in EFS](../facts/efs.md#efs-sagemaker-training-jobs-access)
  link: [Amazon SageMaker training jobs](../facts/efs.md#efs-sagemaker-training-jobs-access)
efs-security-access-iam-and-security-groups
  claim: NFS client access to Amazon EFS is controlled by both IAM policies and network security policies such as security groups. EFS also supports controlling access through POSIX permissions.
  scope: Amazon EFS.
  link: [controlled by both AWS Identity and Access Management](../facts/efs.md#efs-security-access-iam-and-security-groups)
  link: [network security policies, such as security groups](../facts/efs.md#efs-security-access-iam-and-security-groups)
efs-security-groups-on-mount-target-and-instance
  claim: When using EFS you specify VPC security groups for your EC2 instances and security groups for the EFS mount targets associated with the file system.
  scope: EFS mount target network access.
  link: [security groups for the EFS mount targets](../facts/efs.md#efs-security-groups-on-mount-target-and-instance)
  link: [VPC security groups for your EC2 instances](../facts/efs.md#efs-security-groups-on-mount-target-and-instance)
efs-serverless-elastic-no-provisioning
  claim: Amazon EFS is serverless and fully elastic: you do not provision or manage storage capacity, and a file system grows and shrinks automatically as you add and remove files.
  scope: Amazon EFS file system.
  link: [serverless, fully elastic file storage](../facts/efs.md#efs-serverless-elastic-no-provisioning)
  link: [growing and shrinking automatically](../facts/efs.md#efs-serverless-elastic-no-provisioning)
  link: [without provisioning or managing storage capacity](../facts/efs.md#efs-serverless-elastic-no-provisioning)
efs-sla-monthly-uptime-one-zone-99-9
  claim: Under the Amazon EFS SLA, for file systems using One Zone storage classes, a Monthly Uptime Percentage less than 99.9% but greater than or equal to 99.0% earns a 10% service credit.
  scope: per file system, One Zone storage classes, Monthly Uptime Percentage.
  link: [99.9%](../facts/efs.md#efs-sla-monthly-uptime-one-zone-99-9)
efs-sla-monthly-uptime-standard-99-99
  claim: Under the Amazon EFS SLA, for file systems using Standard storage classes, a Monthly Uptime Percentage less than 99.99% but greater than or equal to 99.0% earns a 10% service credit.
  scope: per file system, Standard storage classes, Monthly Uptime Percentage.
  link: [99.99%](../facts/efs.md#efs-sla-monthly-uptime-standard-99-99)
efs-sla-regional-file-system-availability
  claim: In the file system types table, the Regional file system type is listed with an availability of 99.99% across at least 3 Availability Zones.
  scope: Regional file systems; as listed in the file system types table.
  link: [99.99%](../facts/efs.md#efs-sla-regional-file-system-availability)
efs-standard-class-ssd-lowest-latency-new-data-first
  claim: The EFS Standard storage class uses SSD storage for the lowest latency for frequently accessed files, and new file system data is written to Standard first before lifecycle management can tier it to IA or Archive.
  scope: EFS storage classes.
  link: [first written to the EFS Standard storage class](../facts/efs.md#efs-standard-class-ssd-lowest-latency-new-data-first)
  link: [tiered to the EFS Infrequent Access](../facts/efs.md#efs-standard-class-ssd-lowest-latency-new-data-first)
efs-switch-throughput-mode-no-downtime
  claim: You can change the throughput mode and the provisioned throughput amount after the file system is available, and changing the throughput mode does not cause application downtime.
  scope: EFS throughput modes.
  link: [change the throughput mode](../facts/efs.md#efs-switch-throughput-mode-no-downtime)
  link: [does not cause application downtime](../facts/efs.md#efs-switch-throughput-mode-no-downtime)
efs-three-throughput-modes
  claim: Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting.
  scope: EFS throughput modes.
  link: [three throughput modes](../facts/efs.md#efs-three-throughput-modes)
  link: [Elastic, Provisioned, and Bursting](../facts/efs.md#efs-three-throughput-modes)
efs-throughput-above-region-max-needs-increase
  claim: Throughput in excess of an AWS Region's maximum throughput requires a throughput quota increase.
  scope: per AWS Region.
  link: [requires a throughput quota increase](../facts/efs.md#efs-throughput-above-region-max-needs-increase)
efs-throughput-bursting-constrained-move-to-elastic-or-provisioned
  claim: AWS says that if an EFS file system on Bursting throughput is throughput-constrained, for example it uses more than 80% of the permitted throughput or has used all of its burst credits, you should use Elastic or Provisioned throughput instead.
  scope: EFS throughput modes.
  link: [more than 80% of the permitted throughput](../facts/efs.md#efs-throughput-bursting-constrained-move-to-elastic-or-provisioned)
efs-throughput-bursting-scales-with-storage
  claim: AWS says to use Bursting throughput for EFS when you want throughput that scales with the amount of storage in your file system.
  scope: EFS throughput modes.
  link: [scales with the amount of storage](../facts/efs.md#efs-throughput-bursting-scales-with-storage)
efs-throughput-combined-read-write-100pct
  claim: A file system can achieve a combined 100% of its read and write throughput.
  scope: per file system.
  link: [combined 100%](../facts/efs.md#efs-throughput-combined-read-write-100pct)
efs-throughput-elastic-recommended-spiky
  claim: AWS recommends the default Elastic throughput mode for EFS when you have spiky or unpredictable workloads whose performance requirements are hard to forecast, or when your application drives throughput at an average-to-peak ratio of 5% or less.
  scope: EFS throughput modes.
  link: [average-to-peak ratio of 5% or less](../facts/efs.md#efs-throughput-elastic-recommended-spiky)
efs-transfer-family-sftp-ftps-ftp-same-region
  claim: AWS Transfer Family is a fully managed file transfer service for SFTP, FTPS and FTP; your end users can use their SFTP, FTP or FTPS clients to access data stored in your Amazon EFS file system, and Transfer Family endpoints must be in the same Region as the file system.
  scope: AWS Transfer Family with EFS.
  link: [fully managed file transfer service](../facts/efs.md#efs-transfer-family-sftp-ftps-ftp-same-region)
  link: [must be in the same Region](../facts/efs.md#efs-transfer-family-sftp-ftps-ftp-same-region)
  link: [Secure File Transfer Protocol (SFTP)](../facts/efs.md#efs-transfer-family-sftp-ftps-ftp-same-region)
efs-two-forms-encryption-when-enabled
  claim: Amazon EFS supports encryption in transit and encryption at rest; you enable encryption at rest when you create the file system, which encrypts all data and metadata, and you enable encryption in transit when you mount it.
  scope: Amazon EFS encryption.
  link: [enable encryption at rest when creating](../facts/efs.md#efs-two-forms-encryption-when-enabled)
  link: [enable encryption in transit when you mount](../facts/efs.md#efs-two-forms-encryption-when-enabled)
  link: [all of your data and metadata is encrypted](../facts/efs.md#efs-two-forms-encryption-when-enabled)
  link: [encryption in transit and encryption at rest](../facts/efs.md#efs-two-forms-encryption-when-enabled)
efs-whatisefs-one-zone-single-az-loss-risk
  claim: EFS One Zone file systems store data within a single Availability Zone. If all or part of that zone is lost or damaged, data stored in these file systems might be lost.
  scope: EFS One Zone file systems; loss or damage to all or part of the Availability Zone.
  link: [file systems might be lost](../facts/efs.md#efs-whatisefs-one-zone-single-az-loss-risk)
efs-whitepaper-container-storage-lift-and-shift-use-cases
  claim: The AWS overview whitepaper names these EFS use cases: lift-and-shift enterprise applications, big data analytics, web serving and content management, application development and testing, media and entertainment workflows, database backups and container storage.
  scope: Amazon EFS.
  link: [lift-and-shift enterprise applications](../facts/efs.md#efs-whitepaper-container-storage-lift-and-shift-use-cases)
  link: [container storage](../facts/efs.md#efs-whitepaper-container-storage-lift-and-shift-use-cases)
efs-windows-ec2-not-supported
  claim: Using Amazon EFS with Microsoft Windows-based Amazon EC2 instances is not supported.
  scope: Amazon EFS clients.
  link: [is not supported](../facts/efs.md#efs-windows-ec2-not-supported)
  link: [Microsoft Windows–based Amazon EC2 instances](../facts/efs.md#efs-windows-ec2-not-supported)
efs-writes-to-ia-archive-go-to-standard-first
  claim: All write operations to files in IA or Archive are first written to Standard storage, and the data becomes eligible to transition again after 24 hours.
  scope: EFS lifecycle management.
  link: [first written to Standard storage classes](../facts/efs.md#efs-writes-to-ia-archive-go-to-standard-first)
  link: [after 24 hours](../facts/efs.md#efs-writes-to-ia-archive-go-to-standard-first)
fsx-case-adobe-lustre-gpu-never-idle
  claim: The AWS case study says Adobe used Amazon FSx for Lustre high-performance file storage for fast access to data and to make sure GPU resources are never left idle.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [GPU resources are never left idle](../facts/fsx.md#fsx-case-adobe-lustre-gpu-never-idle)
fsx-case-avionte-windows-file-server-rdp-content
  claim: The AWS case study says Avionté uses Amazon FSx for Windows File Server, fully managed file storage built on Windows Server, to persist the application content of its remote desktop protocol based application.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [persist its remote desktop protocol application content](../facts/fsx.md#fsx-case-avionte-windows-file-server-rdp-content)
fsx-case-phillips66-ontap-capacity-pool-80-percent
  claim: The AWS case study says Phillips 66 cycled 90 percent of its data into the elastic capacity-pool tier of FSx for NetApp ONTAP, which reduced its storage costs by 80 percent.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [reduced its storage costs by 80 percent](../facts/fsx.md#fsx-case-phillips66-ontap-capacity-pool-80-percent)
fsx-case-phillips66-snapmirror-no-refactoring
  claim: The AWS case study says Phillips 66 migrated data center environments to Amazon EC2 and FSx for NetApp ONTAP, relied on NetApp SnapMirror for these migrations to preserve its existing data organization and security controls, and removed the need for code rewriting, rearchitecting or refactoring.
  scope: customer case study on the AWS site; a customer statement published by AWS, not a service guarantee.
  link: [the need for code rewriting, rearchitecting, or refactoring](../facts/fsx.md#fsx-case-phillips66-snapmirror-no-refactoring)
fsx-change-backup-air-gapped-vault-lustre-windows-openzfs-2025-03
  claim: On 2025-03-13 AWS Backup added logically air-gapped vault support for Amazon FSx for Lustre, Amazon FSx for Windows File Server and Amazon FSx for OpenZFS. A logically air-gapped vault stores immutable backup copies that are locked by default.
  scope: AWS Backup with Amazon FSx.
  link: [2025-03-13](../facts/fsx.md#fsx-change-backup-air-gapped-vault-lustre-windows-openzfs-2025-03)
  link: [logically air-gapped vault](../facts/fsx.md#fsx-change-backup-air-gapped-vault-lustre-windows-openzfs-2025-03)
fsx-change-fsx-file-gateway-maintenance-2024-10
  claim: Amazon FSx File Gateway is listed in maintenance with an announcement date of 2024-10-28: it is no longer available to new customers, and existing customers can continue to use the service normally.
  scope: Amazon FSx File Gateway availability.
  link: [2024-10-28](../facts/fsx.md#fsx-change-fsx-file-gateway-maintenance-2024-10)
  link: [no longer available to new customers](../facts/fsx.md#fsx-change-fsx-file-gateway-maintenance-2024-10)
fsx-change-lustre-efa-gpudirect-2024-11
  claim: On 2024-11-27 FSx for Lustre began to let you create a Persistent 2 file system with Elastic Fabric Adapter (EFA) support for increased network performance; enabling EFA also provides support for GPUDirect Storage (GDS) and ENA Express.
  scope: FSx for Lustre Persistent 2 file systems.
  link: [2024-11-27](../facts/fsx.md#fsx-change-lustre-efa-gpudirect-2024-11)
  link: [Elastic Fabric Adapter (EFA)](../facts/fsx.md#fsx-change-lustre-efa-gpudirect-2024-11)
fsx-change-lustre-intelligent-tiering-2025-05
  claim: On 2025-05-29 FSx for Lustre added the Intelligent-Tiering storage class, which provides fully elastic storage with an optional SSD cache for low-latency access to frequently accessed data.
  scope: FSx for Lustre storage classes.
  link: [2025-05-29](../facts/fsx.md#fsx-change-lustre-intelligent-tiering-2025-05)
  link: [fully elastic storage with an optional SSD cache](../facts/fsx.md#fsx-change-lustre-intelligent-tiering-2025-05)
fsx-change-lustre-metadata-performance-persistent-2-2024-06
  claim: On 2024-06-06 FSx for Lustre began to let you create a Persistent 2 file system with a metadata configuration that provides the ability to increase metadata performance.
  scope: FSx for Lustre Persistent 2 file systems.
  link: [2024-06-06](../facts/fsx.md#fsx-change-lustre-metadata-performance-persistent-2-2024-06)
  link: [increase metadata performance](../facts/fsx.md#fsx-change-lustre-metadata-performance-persistent-2-2024-06)
fsx-change-lustre-release-data-repository-tasks-2023-08
  claim: On 2023-08-09 FSx for Lustre added release data repository tasks, which release archived files from a file system linked to an S3 data repository: releasing a file keeps the file listing and metadata but removes the local copy of the file content.
  scope: FSx for Lustre linked to an S3 data repository.
  link: [2023-08-09](../facts/fsx.md#fsx-change-lustre-release-data-repository-tasks-2023-08)
  link: [release data repository tasks](../facts/fsx.md#fsx-change-lustre-release-data-repository-tasks-2023-08)
fsx-change-lustre-throughput-capacity-scaling-persistent-ssd-2023-11
  claim: On 2023-11-16 FSx for Lustre began to let you modify the throughput capacity of existing persistent SSD-based file systems as your throughput requirements evolve.
  scope: FSx for Lustre persistent SSD-based file systems.
  link: [2023-11-16](../facts/fsx.md#fsx-change-lustre-throughput-capacity-scaling-persistent-ssd-2023-11)
  link: [modify the throughput capacity](../facts/fsx.md#fsx-change-lustre-throughput-capacity-scaling-persistent-ssd-2023-11)
fsx-change-lustre-version-upgrade-2025-02
  claim: On 2025-02-12 FSx for Lustre began to let you upgrade the Lustre version of your file system to a newer version.
  scope: FSx for Lustre.
  link: [2025-02-12](../facts/fsx.md#fsx-change-lustre-version-upgrade-2025-02)
  link: [upgrade the Lustre version](../facts/fsx.md#fsx-change-lustre-version-upgrade-2025-02)
fsx-change-ontap-12-ha-pairs-72-gbps-2024-03
  claim: On 2024-03-04 FSx for NetApp ONTAP added support for 12 HA pairs in scale-out file systems; file systems with 12 HA pairs can deliver up to 72 GBps of throughput capacity and 2,400,000 SSD IOPS.
  scope: FSx for NetApp ONTAP scale-out file systems.
  link: [2024-03-04](../facts/fsx.md#fsx-change-ontap-12-ha-pairs-72-gbps-2024-03)
  link: [12 HA pairs](../facts/fsx.md#fsx-change-ontap-12-ha-pairs-72-gbps-2024-03)
  link: [72 GBps](../facts/fsx.md#fsx-change-ontap-12-ha-pairs-72-gbps-2024-03)
fsx-change-ontap-air-gapped-vault-2026-09
  claim: On 2026-09-28 AWS Backup logically air-gapped vaults began to support Amazon FSx for NetApp ONTAP. A logically air-gapped vault stores immutable backups that are locked by default and isolated with encryption using AWS owned keys or customer-managed keys.
  scope: AWS Backup logically air-gapped vault with FSx for NetApp ONTAP.
  link: [2026-09-28](../facts/fsx.md#fsx-change-ontap-air-gapped-vault-2026-09)
  link: [logically air-gapped vault](../facts/fsx.md#fsx-change-ontap-air-gapped-vault-2026-09)
fsx-change-ontap-autonomous-ransomware-protection-2025-04
  claim: On 2025-04-07 FSx for NetApp ONTAP began to support Autonomous Ransomware Protection (ARP), a NetApp AI-driven feature that monitors and protects against ransomware and malware attacks.
  scope: FSx for NetApp ONTAP security.
  link: [2025-04-07](../facts/fsx.md#fsx-change-ontap-autonomous-ransomware-protection-2025-04)
  link: [Autonomous Ransomware Protection (ARP)](../facts/fsx.md#fsx-change-ontap-autonomous-ransomware-protection-2025-04)
fsx-change-ontap-decrease-ssd-capacity-2025-08
  claim: On 2025-08-14 FSx for NetApp ONTAP began to let you decrease the SSD storage capacity of second-generation file systems, to optimize storage costs for workloads with varying high-performance storage needs.
  scope: FSx for NetApp ONTAP second-generation SSD storage.
  link: [2025-08-14](../facts/fsx.md#fsx-change-ontap-decrease-ssd-capacity-2025-08)
  link: [decrease SSD storage capacity](../facts/fsx.md#fsx-change-ontap-decrease-ssd-capacity-2025-08)
fsx-change-ontap-nvme-over-tcp-2024-07
  claim: On 2024-07-09 FSx for NetApp ONTAP added support for the Non-Volatile Memory Express over TCP (NVMe/TCP) protocol.
  scope: FSx for NetApp ONTAP block protocols.
  link: [2024-07-09](../facts/fsx.md#fsx-change-ontap-nvme-over-tcp-2024-07)
  link: [NVMe/TCP](../facts/fsx.md#fsx-change-ontap-nvme-over-tcp-2024-07)
fsx-change-ontap-s3-access-points-2025-12
  claim: On 2025-12-02 FSx for NetApp ONTAP added Amazon S3 access points, a way to access data stored in FSx for ONTAP file systems with the Amazon S3 API without changing the existing file system configuration.
  scope: FSx for NetApp ONTAP file systems.
  link: [2025-12-02](../facts/fsx.md#fsx-change-ontap-s3-access-points-2025-12)
  link: [Amazon S3 access points](../facts/fsx.md#fsx-change-ontap-s3-access-points-2025-12)
fsx-change-ontap-second-generation-file-systems-2024-07
  claim: On 2024-07-09 FSx for NetApp ONTAP added second-generation Single-AZ and Multi-AZ file systems; a single high-availability (HA) pair now delivers up to 6 GBps of throughput capacity and 200,000 SSD IOPS.
  scope: FSx for NetApp ONTAP second-generation file systems.
  link: [2024-07-09](../facts/fsx.md#fsx-change-ontap-second-generation-file-systems-2024-07)
  link: [6 GBps](../facts/fsx.md#fsx-change-ontap-second-generation-file-systems-2024-07)
fsx-change-ontap-snaplock-licensing-fee-removed-2025-03
  claim: On 2025-03-05 Amazon FSx for NetApp ONTAP eliminated SnapLock licensing fees for data stored in SnapLock volumes. The removal applies automatically to new and existing SnapLock volumes on all FSx for ONTAP file systems in all AWS Regions where they are available.
  scope: FSx for NetApp ONTAP SnapLock volumes.
  link: [2025-03-05](../facts/fsx.md#fsx-change-ontap-snaplock-licensing-fee-removed-2025-03)
  link: [SnapLock licensing fees](../facts/fsx.md#fsx-change-ontap-snaplock-licensing-fee-removed-2025-03)
  changed: 2025-03-05: was SnapLock licensing fees
fsx-change-openzfs-cross-region-account-replication-2023-12
  claim: On 2023-12-20 FSx for OpenZFS added cross-region and cross-account data replication.
  scope: FSx for OpenZFS replication.
  link: [2023-12-20](../facts/fsx.md#fsx-change-openzfs-cross-region-account-replication-2023-12)
  link: [cross-region and cross-account data replication](../facts/fsx.md#fsx-change-openzfs-cross-region-account-replication-2023-12)
fsx-change-openzfs-intelligent-tiering-2024-12
  claim: On 2024-12-01 FSx for OpenZFS added the Intelligent-Tiering storage class: fully elastic storage with an optional SSD cache, where you are billed for the data you store and do not need to specify a file system size at creation.
  scope: FSx for OpenZFS storage classes.
  link: [2024-12-01](../facts/fsx.md#fsx-change-openzfs-intelligent-tiering-2024-12)
  link: [fully elastic storage](../facts/fsx.md#fsx-change-openzfs-intelligent-tiering-2024-12)
fsx-change-openzfs-multi-az-deployment-2023-08
  claim: On 2023-08-09 FSx for OpenZFS added the Multi-AZ deployment type.
  scope: FSx for OpenZFS deployment types.
  link: [2023-08-09](../facts/fsx.md#fsx-change-openzfs-multi-az-deployment-2023-08)
  link: [Multi-AZ deployment type](../facts/fsx.md#fsx-change-openzfs-multi-az-deployment-2023-08)
fsx-change-openzfs-multi-az-shared-vpc-2026-05
  claim: On 2026-05-13 FSx for OpenZFS began to let participant accounts create Multi-AZ file systems in VPCs shared with them in the same AWS organization. Before this, participant accounts could create Multi-AZ file systems only in VPCs they owned.
  scope: FSx for OpenZFS Multi-AZ in shared VPCs.
  link: [2026-05-13](../facts/fsx.md#fsx-change-openzfs-multi-az-shared-vpc-2026-05)
  link: [Multi-AZ file systems in VPCs they owned](../facts/fsx.md#fsx-change-openzfs-multi-az-shared-vpc-2026-05)
  changed: 2026-05-13: was could only create Multi-AZ file systems in VPCs they owned
fsx-change-openzfs-on-demand-replication-2023-11
  claim: On 2023-11-26 FSx for OpenZFS added on-demand data replication.
  scope: FSx for OpenZFS replication.
  link: [2023-11-26](../facts/fsx.md#fsx-change-openzfs-on-demand-replication-2023-11)
  link: [on-demand data replication](../facts/fsx.md#fsx-change-openzfs-on-demand-replication-2023-11)
fsx-change-openzfs-s3-access-points-2025-06
  claim: On 2025-06-25 FSx for OpenZFS added Amazon S3 access points attached to FSx for OpenZFS volumes, so you can use the S3 object API to access file data.
  scope: FSx for OpenZFS volumes.
  link: [2025-06-25](../facts/fsx.md#fsx-change-openzfs-s3-access-points-2025-06)
  link: [Amazon S3 access points](../facts/fsx.md#fsx-change-openzfs-s3-access-points-2025-06)
fsx-change-openzfs-single-az-ha-deployment-2024-07
  claim: On 2024-07-09 FSx for OpenZFS added the Single-AZ (HA) deployment type.
  scope: FSx for OpenZFS deployment types.
  link: [2024-07-09](../facts/fsx.md#fsx-change-openzfs-single-az-ha-deployment-2024-07)
  link: [Single-AZ (HA) deployment type](../facts/fsx.md#fsx-change-openzfs-single-az-ha-deployment-2024-07)
fsx-change-windows-file-server-resource-manager-2025-11
  claim: On 2025-11-19 FSx for Windows File Server added support for File Server Resource Manager (FSRM). FSRM support is available at no additional cost for new file systems in all AWS Regions where FSx for Windows File Server is available, and existing file systems get it during an upcoming maintenance window.
  scope: FSx for Windows File Server FSRM.
  link: [2025-11-19](../facts/fsx.md#fsx-change-windows-file-server-resource-manager-2025-11)
  link: [no additional cost](../facts/fsx.md#fsx-change-windows-file-server-resource-manager-2025-11)
fsx-change-windows-max-iops-400k-2024-01
  claim: On 2024-01-17 FSx for Windows File Server raised maximum IOPS from 350K to 400K for file systems with 12 GBps of throughput capacity or higher, and raised the maximum at lower throughput capacities as well.
  scope: FSx for Windows File Server SSD IOPS, 12 GBps throughput capacity.
  link: [2024-01-17](../facts/fsx.md#fsx-change-windows-max-iops-400k-2024-01)
  link: [400K](../facts/fsx.md#fsx-change-windows-max-iops-400k-2024-01)
  link: [350K](../facts/fsx.md#fsx-change-windows-max-iops-400k-2024-01)
  changed: 2024-01-17: was 350K
fsx-change-windows-max-throughput-12-gbps-2023-08
  claim: On 2023-08-09 FSx for Windows File Server file systems began to support up to 12 GBps throughput capacity.
  scope: FSx for Windows File Server throughput capacity.
  link: [2023-08-09](../facts/fsx.md#fsx-change-windows-max-throughput-12-gbps-2023-08)
  link: [12 GBps](../facts/fsx.md#fsx-change-windows-max-throughput-12-gbps-2023-08)
fsx-change-windows-ssd-iops-provisioning-independent-2023-08
  claim: On 2023-08-09 FSx for Windows File Server file systems began to support SSD IOPS provisioning independently of storage capacity.
  scope: FSx for Windows File Server SSD IOPS.
  link: [2023-08-09](../facts/fsx.md#fsx-change-windows-ssd-iops-provisioning-independent-2023-08)
  link: [SSD IOPS provisioning independently of storage capacity](../facts/fsx.md#fsx-change-windows-ssd-iops-provisioning-independent-2023-08)
fsx-change-windows-storage-type-hdd-to-ssd-update-2023-08
  claim: On 2023-08-09 FSx for Windows File Server file systems began to support updating the storage type from HDD to SSD.
  scope: FSx for Windows File Server storage type.
  link: [2023-08-09](../facts/fsx.md#fsx-change-windows-storage-type-hdd-to-ssd-update-2023-08)
  link: [updating from HDD storage type to SSD](../facts/fsx.md#fsx-change-windows-storage-type-hdd-to-ssd-update-2023-08)
fsx-compare-acl-types
  claim: On the AWS page comparing FSx file systems, access control lists are marked for FSx for NetApp ONTAP (NFS 4.0, v4.1, NTFS) and FSx for Windows File Server (NTFS), and not for OpenZFS or Lustre.
  scope: security and compliance table.
  link: [NFS 4.0, v4.1, NTFS](../facts/fsx.md#fsx-compare-acl-types)
  link: [NTFS](../facts/fsx.md#fsx-compare-acl-types)
fsx-compare-active-directory-ontap-windows
  claim: On the AWS page comparing FSx file systems, Active Directory support for file system access authentication and access control is marked only for FSx for NetApp ONTAP and FSx for Windows File Server.
  scope: security and compliance table.
  link: [Active Directory support for file system access authentication](../facts/fsx.md#fsx-compare-active-directory-ontap-windows)
fsx-compare-antivirus-ontap-only
  claim: On the AWS page comparing FSx file systems, anti-virus integration is marked only for FSx for NetApp ONTAP.
  scope: security and compliance table.
  link: [Anti-virus integration](../facts/fsx.md#fsx-compare-antivirus-ontap-only)
fsx-compare-availability-sla
  claim: AWS lists the availability SLA as 99.99% for Multi-AZ and 99.9% for Single-AZ on FSx for NetApp ONTAP; 99.99% for Multi-AZ and 99.5% for Single-AZ on OpenZFS and Windows File Server; and 99.5% for Single-AZ on Lustre.
  scope: per FSx file system type and deployment type.
  link: [99.99%](../facts/fsx.md#fsx-compare-availability-sla)
  link: [99.9%](../facts/fsx.md#fsx-compare-availability-sla)
  link: [99.5%](../facts/fsx.md#fsx-compare-availability-sla)
fsx-compare-client-compatibility
  claim: AWS lists client compatibility as Windows, Linux and macOS for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and Linux for FSx for Lustre.
  scope: per FSx file system type.
  link: [Linux](../facts/fsx.md#fsx-compare-client-compatibility)
fsx-compare-cold-data-options
  claim: For cost-optimized storage of cold, infrequently accessed data, AWS lists a low-cost tier with cold data cycled to it automatically for FSx for NetApp ONTAP, an HDD storage option for FSx for Windows File Server and an HDD storage option for FSx for Lustre; FSx for OpenZFS is not marked.
  scope: price/performance table, FSx file system comparison page.
  link: [cold data automatically cycled to it](../facts/fsx.md#fsx-compare-cold-data-options)
  link: [HDD storage option](../facts/fsx.md#fsx-compare-cold-data-options)
fsx-compare-compliance-all-four-types
  claim: AWS lists the same compliance programs for all four FSx file system types, among them HIPAA BAA, PCI/DSS, ISO, SOC, IRAP, GDPR, ISMAP, FINMA, MTCS, C5, ENS High, OSPAR and HITRUST CSF.
  scope: security and compliance table.
  link: [HIPAA BAA, PCI/DSS, ISO, SOC](../facts/fsx.md#fsx-compare-compliance-all-four-types)
fsx-compare-cross-region-replication
  claim: On the AWS page comparing FSx file systems, cross-Region replication is marked for FSx for NetApp ONTAP (NetApp SnapMirror) and for FSx for Lustre (using S3 cross-region replication), and not for OpenZFS or Windows File Server.
  scope: availability and data protection table.
  link: [NetApp SnapMirror](../facts/fsx.md#fsx-compare-cross-region-replication)
  link: [Using S3 cross-region replication](../facts/fsx.md#fsx-compare-cross-region-replication)
fsx-compare-dedup-ontap-windows-only
  claim: On the AWS page comparing FSx file systems, data deduplication is marked only for FSx for NetApp ONTAP and FSx for Windows File Server, and it applies to both file system storage and backups.
  scope: price/performance table, FSx file system comparison page.
  link: [Data deduplication](../facts/fsx.md#fsx-compare-dedup-ontap-windows-only)
fsx-compare-deployment-options
  claim: AWS lists deployment options of Single-AZ and Multi-AZ for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and Single-AZ with Persistent or Scratch for FSx for Lustre.
  scope: per FSx file system type.
  link: [Single-AZ - Persistent or Scratch](../facts/fsx.md#fsx-compare-deployment-options)
  link: [Single-AZ and Multi-AZ](../facts/fsx.md#fsx-compare-deployment-options)
fsx-compare-file-access-auditing-ontap-windows
  claim: On the AWS page comparing FSx file systems, file access auditing is marked only for FSx for NetApp ONTAP and FSx for Windows File Server.
  scope: security and compliance table.
  link: [File access auditing](../facts/fsx.md#fsx-compare-file-access-auditing-ontap-windows)
fsx-compare-instant-cloning-ontap-openzfs
  claim: On the AWS page comparing FSx file systems, instant cloning is marked only for FSx for NetApp ONTAP and FSx for OpenZFS.
  scope: availability and data protection table.
  link: [Instant cloning](../facts/fsx.md#fsx-compare-instant-cloning-ontap-openzfs)
fsx-compare-latency-by-type
  claim: AWS lists latency of less than 1 ms for FSx for NetApp ONTAP, FSx for Windows File Server and FSx for Lustre, and less than 0.5 ms for FSx for OpenZFS.
  scope: per FSx file system type.
  link: [<1 ms](../facts/fsx.md#fsx-compare-latency-by-type)
  link: [<0.5 ms](../facts/fsx.md#fsx-compare-latency-by-type)
fsx-compare-lustre-only-s3-import-export
  claim: On the AWS page comparing FSx file systems, only FSx for Lustre is marked as supporting automatic import and export of S3 data sets.
  scope: FSx file system comparison page.
  link: [Automatic import/export of S3 data sets](../facts/fsx.md#fsx-compare-lustre-only-s3-import-export)
fsx-compare-max-file-system-size
  claim: AWS lists maximum file system size as virtually unlimited (tens of PBs) for FSx for NetApp ONTAP, 512 TiB for OpenZFS, 64 TiB for Windows File Server and multiple PBs for Lustre.
  scope: per file system, per FSx file system type; maximum; not adjustable.
  link: [512 TiB](../facts/fsx.md#fsx-compare-max-file-system-size)
  link: [64 TiB](../facts/fsx.md#fsx-compare-max-file-system-size)
  link: [Virtually unlimited (10s of PBs)](../facts/fsx.md#fsx-compare-max-file-system-size)
  link: [Multiple PBs](../facts/fsx.md#fsx-compare-max-file-system-size)
fsx-compare-max-iops-per-file-system
  claim: AWS lists maximum IOPS per file system as millions for FSx for NetApp ONTAP, 1-2 million for OpenZFS, hundreds of thousands for Windows File Server and millions for Lustre.
  scope: per file system, per FSx file system type; maximum; not adjustable.
  link: [1-2 million](../facts/fsx.md#fsx-compare-max-iops-per-file-system)
  link: [Hundreds of thousands](../facts/fsx.md#fsx-compare-max-iops-per-file-system)
fsx-compare-max-throughput-per-file-system
  claim: AWS lists maximum throughput per file system of 72-80 GB/s for FSx for NetApp ONTAP, 10-21 GB/s for OpenZFS, 12-20 GB/s for Windows File Server and 1000 GB/s for Lustre. The lower number of a range is baseline throughput, and the upper number is a higher level enabled by caching, bursting and compression.
  scope: per file system, per FSx file system type; maximum; not adjustable; a range gives baseline (lower) to enhanced (upper) throughput.
  link: [72-80 GB/s](../facts/fsx.md#fsx-compare-max-throughput-per-file-system)
  link: [10-21 GB/s](../facts/fsx.md#fsx-compare-max-throughput-per-file-system)
  link: [12-20 GB/s](../facts/fsx.md#fsx-compare-max-throughput-per-file-system)
  link: [1000 GB/s](../facts/fsx.md#fsx-compare-max-throughput-per-file-system)
fsx-compare-max-throughput-single-client
  claim: AWS lists maximum throughput available to a single client accessing a file system as 18 GB/s for FSx for NetApp ONTAP, 10 GB/s for OpenZFS, 20 GB/s for Windows File Server and 150 GB/s for Lustre.
  scope: per client, per FSx file system type; maximum; not adjustable.
  link: [18 GB/s](../facts/fsx.md#fsx-compare-max-throughput-single-client)
  link: [10 GB/s](../facts/fsx.md#fsx-compare-max-throughput-single-client)
  link: [20 GB/s](../facts/fsx.md#fsx-compare-max-throughput-single-client)
  link: [150 GB/s](../facts/fsx.md#fsx-compare-max-throughput-single-client)
fsx-compare-ontap-only-compute-burst-flexcache
  claim: On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for compute burst to the cloud, using FSx as an on-AWS cache of on-premises data with NetApp FlexCache.
  scope: hybrid usage, FSx file system comparison page.
  link: [NetApp FlexCache](../facts/fsx.md#fsx-compare-ontap-only-compute-burst-flexcache)
fsx-compare-ontap-only-hybrid-caching
  claim: On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for on-premises caching of FSx data, with NetApp Global File Cache and NetApp FlexCache.
  scope: hybrid usage, FSx file system comparison page.
  link: [NetApp Global File Cache, NetApp FlexCache](../facts/fsx.md#fsx-compare-ontap-only-hybrid-caching)
fsx-compare-ontap-only-snapmirror-dr-from-on-premises
  claim: On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for backup and disaster recovery from on premises to AWS, using NetApp SnapMirror.
  scope: hybrid usage, FSx file system comparison page.
  link: [NetApp SnapMirror](../facts/fsx.md#fsx-compare-ontap-only-snapmirror-dr-from-on-premises)
fsx-compare-protocol-support
  claim: AWS lists protocol support as SMB, NFS and iSCSI for FSx for NetApp ONTAP, NFS for OpenZFS, SMB for Windows File Server, and a custom POSIX-compliant protocol optimized for performance for Lustre.
  scope: per FSx file system type.
  link: [SMB 2.0, 2.1, 3.0, 3.1.1 NFS 3, 4.0, 4.1, 4.2 iSCSI (shared block storage)](../facts/fsx.md#fsx-compare-protocol-support)
  link: [NFS 3, 4.0, 4.1, 4.2](../facts/fsx.md#fsx-compare-protocol-support)
fsx-compare-snapshots-restore-not-lustre
  claim: On the AWS page comparing FSx file systems, inline instantaneous snapshots are marked for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and are not marked for FSx for Lustre.
  scope: availability and data protection table.
  link: [Inline instantaneous snapshots](../facts/fsx.md#fsx-compare-snapshots-restore-not-lustre)
fsx-decision-guide-cache-file-cache-row
  claim: In the AWS storage decision guide table, the cache storage type is served by Amazon File Cache, a fully managed, scalable, high-speed cache on AWS for processing file data stored in disparate locations, including on-premises NFS file systems, cloud file systems (FSx for OpenZFS, FSx for NetApp ONTAP) and Amazon S3.
  scope: storage type table of the decision guide.
  link: [Amazon File Cache](../facts/fsx.md#fsx-decision-guide-cache-file-cache-row)
fsx-decision-guide-four-file-systems-align-to-popular
  claim: The AWS storage decision guide says the Amazon FSx data storage family comes in four options that align to popular file systems: Windows File Server, Lustre, OpenZFS and NetApp ONTAP.
  scope: Amazon FSx family.
  link: [four options that align to popular file systems](../facts/fsx.md#fsx-decision-guide-four-file-systems-align-to-popular)
fsx-decision-guide-lustre-speed-workloads
  claim: The AWS storage decision guide says FSx for Lustre is optimized for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing and financial modeling.
  scope: Amazon FSx for Lustre.
  link: [machine learning, high performance computing (HPC)](../facts/fsx.md#fsx-decision-guide-lustre-speed-workloads)
  link: [video processing, and financial modeling](../facts/fsx.md#fsx-decision-guide-lustre-speed-workloads)
fsx-decision-guide-online-migration-options
  claim: In the AWS storage decision guide, the online migration options include AWS DataSync, AWS Transfer Family, Amazon FSx for NetApp ONTAP SnapMirror and AWS Storage Gateway, and online migration is optimized for frequent updates to data and for time-critical or ongoing workloads.
  scope: migration options table of the decision guide.
  link: [Online is optimized for frequent updates to data](../facts/fsx.md#fsx-decision-guide-online-migration-options)
fsx-decision-guide-ontap-compat-migration-path
  claim: The AWS storage decision guide says that if you already use NetApp ONTAP appliances on premises, Amazon FSx for NetApp ONTAP gives a seamless migration path.
  scope: migration compatibility criterion in the storage decision guide.
  link: [seamless migration path](../facts/fsx.md#fsx-decision-guide-ontap-compat-migration-path)
fsx-decision-guide-windows-smb-lustre-linux
  claim: The AWS storage decision guide says Windows-based clients can use Amazon FSx for Windows File Server, which gives highly available storage with full SMB support, and that FSx for Lustre is designed for Unix and Linux based file systems.
  scope: client type criterion in the storage decision guide.
  link: [full Server Message Block (SMB) support](../facts/fsx.md#fsx-decision-guide-windows-smb-lustre-linux)
  link: [Unix/Linux-based file systems](../facts/fsx.md#fsx-decision-guide-windows-smb-lustre-linux)
fsx-faq-lustre-always-encrypts-at-rest-kms
  claim: Amazon FSx for Lustre always encrypts your file system data and your backups at rest using keys you manage through AWS KMS.
  scope: FSx for Lustre encryption at rest.
  link: [always encrypts your file system data](../facts/fsx.md#fsx-faq-lustre-always-encrypts-at-rest-kms)
fsx-faq-lustre-backup-durability-11-nines-s3
  claim: Amazon FSx stores backups with 99.999999999% (11 9's) of durability on Amazon S3.
  scope: FSx for Lustre backups; fixed.
  link: [99.999999999%](../facts/fsx.md#fsx-faq-lustre-backup-durability-11-nines-s3)
fsx-faq-lustre-backups-daily-incremental
  claim: Amazon FSx takes daily automatic backups of FSx for Lustre file systems and allows additional backups at any point; backups are incremental.
  scope: FSx for Lustre backups.
  link: [Amazon FSx backups are incremental](../facts/fsx.md#fsx-faq-lustre-backups-daily-incremental)
fsx-faq-lustre-backups-not-on-s3-linked
  claim: Backups are not supported on FSx for Lustre file systems linked to an S3 bucket, because the S3 bucket serves as the primary storage location for the full dataset.
  scope: FSx for Lustre linked to Amazon S3.
  link: [Backups aren’t supported on file systems linked](../facts/fsx.md#fsx-faq-lustre-backups-not-on-s3-linked)
fsx-faq-lustre-backups-not-on-scratch
  claim: Backups are not supported on FSx for Lustre scratch file systems because they are designed for temporary storage and shorter-term processing of data.
  scope: FSx for Lustre scratch file systems.
  link: [Backups aren’t supported on scratch file systems](../facts/fsx.md#fsx-faq-lustre-backups-not-on-scratch)
fsx-faq-lustre-consistent-sub-ms-latency
  claim: FSx for Lustre provides consistent, sub-millisecond latencies for file operations.
  scope: FSx for Lustre file operations.
  link: [consistent, sub-millisecond latencies](../facts/fsx.md#fsx-faq-lustre-consistent-sub-ms-latency)
fsx-faq-lustre-data-repository-associations
  claim: You link a file system to S3 buckets by creating data repository associations using the Amazon FSx console, the AWS CLI, or the Amazon FSx API.
  scope: FSx for Lustre with Amazon S3.
  link: [data repository associations](../facts/fsx.md#fsx-faq-lustre-data-repository-associations)
fsx-faq-lustre-deployment-options-scratch-persistent
  claim: Amazon FSx for Lustre provides two deployment options: scratch and persistent.
  scope: FSx for Lustre deployment options.
  link: [scratch and persistent](../facts/fsx.md#fsx-faq-lustre-deployment-options-scratch-persistent)
fsx-faq-lustre-efa-7x-700-gbps-per-client
  claim: FSx for Lustre with EFA support enabled provides up to 7x, or up to 700 Gbps, higher per-client throughput compared with previous FSx for Lustre file systems.
  scope: per client, EFA-enabled FSx for Lustre; maximum.
  link: [up to 7x](../facts/fsx.md#fsx-faq-lustre-efa-7x-700-gbps-per-client)
  link: [up to 700 Gbps](../facts/fsx.md#fsx-faq-lustre-efa-7x-700-gbps-per-client)
fsx-faq-lustre-intelligent-tiering-34-percent-lower
  claim: Intelligent-Tiering provides up to 34% lower costs compared with traditional on-premises HDD deployments.
  scope: FSx for Lustre Intelligent-Tiering; maximum.
  link: [up to 34% lower costs](../facts/fsx.md#fsx-faq-lustre-intelligent-tiering-34-percent-lower)
fsx-faq-lustre-intelligent-tiering-elastic-ssd-cache
  claim: The Intelligent-Tiering storage class provides fully elastic, intelligently tiered storage with an optional SSD read cache to speed up access to frequently accessed data.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [fully elastic, intelligently tiered storage](../facts/fsx.md#fsx-faq-lustre-intelligent-tiering-elastic-ssd-cache)
fsx-faq-lustre-intelligent-tiering-read-cache-latency
  claim: With Intelligent-Tiering, data in the SSD read cache has sub-millisecond time-to-first-byte latencies, and all other data has time-to-first-byte latencies in the range of tens of milliseconds.
  scope: FSx for Lustre Intelligent-Tiering.
  link: [sub-millisecond time-to-first-byte latencies](../facts/fsx.md#fsx-faq-lustre-intelligent-tiering-read-cache-latency)
  link: [tens of milliseconds](../facts/fsx.md#fsx-faq-lustre-intelligent-tiering-read-cache-latency)
fsx-faq-lustre-intelligent-tiering-throughput-multiples-4000
  claim: Intelligent-Tiering file systems can be provisioned with multiples of 4,000 MB/s of throughput capacity, independent of storage capacity.
  scope: per file system, Intelligent-Tiering; fixed; not adjustable.
  link: [multiples of 4,000 MB/s](../facts/fsx.md#fsx-faq-lustre-intelligent-tiering-throughput-multiples-4000)
fsx-faq-lustre-lz4-compression-no-performance-impact
  claim: FSx for Lustre data compression uses the LZ4 algorithm, which is optimized for compression speed, so enabling compression will not adversely impact file system performance.
  scope: FSx for Lustre data compression.
  link: [LZ4 compression algorithm](../facts/fsx.md#fsx-faq-lustre-lz4-compression-no-performance-impact)
fsx-faq-lustre-metadata-server-per-12000-iops
  claim: When metadata IOPS are increased, FSx automatically adds a new metadata server for each 12,000 metadata IOPS provisioned.
  scope: FSx for Lustre metadata servers.
  link: [each 12,000 metadata IOPS provisioned](../facts/fsx.md#fsx-faq-lustre-metadata-server-per-12000-iops)
fsx-faq-lustre-multiple-file-systems-one-bucket
  claim: You can create multiple FSx for Lustre file systems linked to the same S3 bucket.
  scope: FSx for Lustre linked to Amazon S3.
  link: [linked to the same S3 bucket](../facts/fsx.md#fsx-faq-lustre-multiple-file-systems-one-bucket)
fsx-faq-lustre-no-auto-backups-when-linked-to-s3
  claim: FSx will not take automatic backups of an FSx for Lustre file system if it is linked to S3.
  scope: FSx for Lustre linked to Amazon S3.
  link: [will not take automatic backups](../facts/fsx.md#fsx-faq-lustre-no-auto-backups-when-linked-to-s3)
fsx-faq-lustre-persistent-server-replaced-within-minutes
  claim: On a persistent file system, if a file server becomes unavailable it is replaced automatically and within minutes.
  scope: FSx for Lustre persistent file systems.
  link: [replaced automatically and within minutes](../facts/fsx.md#fsx-faq-lustre-persistent-server-replaced-within-minutes)
fsx-faq-lustre-release-data-task
  claim: You can release inactive data from S3-linked FSx for Lustre file systems by using a data repository task.
  scope: FSx for Lustre linked to Amazon S3.
  link: [data repository task](../facts/fsx.md#fsx-faq-lustre-release-data-task)
fsx-faq-lustre-release-does-not-guarantee-never-full
  claim: Releasing file system data does not ensure that an FSx for Lustre file system will never become full.
  scope: FSx for Lustre linked to Amazon S3.
  link: [Releasing file system data will not ensure](../facts/fsx.md#fsx-faq-lustre-release-does-not-guarantee-never-full)
fsx-faq-lustre-s3-import-export-tasks-alternative
  claim: Instead of automatic import and export, you can import and export batches of new and changed data between the file system and S3 for fine-grained control over data synchronization.
  scope: FSx for Lustre linked to Amazon S3.
  link: [batches of new and changed data](../facts/fsx.md#fsx-faq-lustre-s3-import-export-tasks-alternative)
fsx-faq-lustre-s3-link-transparent
  claim: You can link an FSx for Lustre file system to S3 buckets, and FSx for Lustre makes the S3 data transparently accessible in the file system.
  scope: FSx for Lustre with Amazon S3.
  link: [link your Amazon FSx for Lustre file system](../facts/fsx.md#fsx-faq-lustre-s3-link-transparent)
fsx-faq-lustre-s3-object-imported-on-first-access
  claim: The content of an S3 object is imported automatically only when you first access the associated file on the file system, so an object's data does not consume file system space unless accessed at least once.
  scope: FSx for Lustre linked to Amazon S3.
  link: [imported automatically from S3 only when you access](../facts/fsx.md#fsx-faq-lustre-s3-object-imported-on-first-access)
fsx-faq-lustre-s3-sync-both-directions
  claim: FSx for Lustre can be configured to keep content synchronized in both directions between the file system and the linked S3 buckets.
  scope: FSx for Lustre linked to Amazon S3.
  link: [synchronized in both directions](../facts/fsx.md#fsx-faq-lustre-s3-sync-both-directions)
fsx-faq-lustre-ssd-class-provisioned
  claim: The SSD storage class is provisioned: you specify a file system size and pay storage costs for the amount of storage provisioned.
  scope: FSx for Lustre SSD storage class.
  link: [you specify a file system size](../facts/fsx.md#fsx-faq-lustre-ssd-class-provisioned)
fsx-faq-lustre-storage-classes-ssd-intelligent-tiering
  claim: Amazon FSx for Lustre offers SSD and Intelligent-Tiering storage classes.
  scope: FSx for Lustre storage classes.
  link: [SSD and Intelligent-Tiering storage classes](../facts/fsx.md#fsx-faq-lustre-storage-classes-ssd-intelligent-tiering)
fsx-faq-lustre-storage-increase-every-six-hours
  claim: You can increase an FSx for Lustre file system's storage capacity every six hours, in the same increments that you can provision new file systems.
  scope: per file system, storage capacity increase; fixed; not adjustable.
  link: [every six hours](../facts/fsx.md#fsx-faq-lustre-storage-increase-every-six-hours)
fsx-faq-lustre-tbps-millions-iops-sub-ms
  claim: FSx for Lustre file systems scale to TB/s of throughput and millions of IOPS.
  scope: FSx for Lustre.
  link: [TB/s of throughput and millions of IOPS](../facts/fsx.md#fsx-faq-lustre-tbps-millions-iops-sub-ms)
fsx-faq-lustre-throughput-per-tib-ssd-125-1000
  claim: SSD-based FSx for Lustre file systems can be provisioned with 125, 250, 500, or 1,000 MB/s of throughput per TiB of storage provisioned.
  scope: per TiB of storage provisioned, SSD-based file systems; fixed; not adjustable.
  link: [125, 250, 500, or 1,000 MB/s](../facts/fsx.md#fsx-faq-lustre-throughput-per-tib-ssd-125-1000)
fsx-faq-lustre-upgrade-requires-unmount
  claim: You are required to unmount all clients from an FSx for Lustre file system before initiating a Lustre version upgrade.
  scope: FSx for Lustre version upgrades.
  link: [unmount all clients from your file system](../facts/fsx.md#fsx-faq-lustre-upgrade-requires-unmount)
fsx-faq-ontap-3-iops-per-gb-ssd
  claim: Each gigabyte of FSx for NetApp ONTAP SSD storage includes 3 disk IOPS, and additional IOPS can be provisioned as needed.
  scope: per GB of SSD storage; default; adjustable.
  link: [3 disk IOPS](../facts/fsx.md#fsx-faq-ontap-3-iops-per-gb-ssd)
fsx-faq-ontap-active-directory-nfs-smb
  claim: You can optionally join an FSx for ONTAP file system to your organization's Active Directory so users can use their existing AD-based identities to authenticate and access it over NFS or SMB.
  scope: FSx for NetApp ONTAP authentication.
  link: [join your file system to your organization’s AD](../facts/fsx.md#fsx-faq-ontap-active-directory-nfs-smb)
fsx-faq-ontap-auto-tiering-less-accessed-to-capacity-pool
  claim: As you write data to FSx for ONTAP, less frequently accessed data is automatically transitioned to the capacity pool tier, which grows and shrinks with the amount of data tiered to it.
  scope: FSx for NetApp ONTAP capacity pool tiering.
  link: [automatically transitioned to the capacity pool tier](../facts/fsx.md#fsx-faq-ontap-auto-tiering-less-accessed-to-capacity-pool)
fsx-faq-ontap-backups-crash-consistent-offline
  claim: FSx for ONTAP backups are a crash-consistent and secondary, offline copy of a volume in your file system.
  scope: FSx for NetApp ONTAP backups.
  link: [crash-consistent and secondary, offline copy of a volume](../facts/fsx.md#fsx-faq-ontap-backups-crash-consistent-offline)
fsx-faq-ontap-backups-daily-by-default
  claim: By default, Amazon FSx takes an automatic backup of your FSx for ONTAP volumes each day during a backup window that you specify.
  scope: FSx for NetApp ONTAP volumes; default; adjustable.
  link: [automatic backup of your volumes each day](../facts/fsx.md#fsx-faq-ontap-backups-daily-by-default)
fsx-faq-ontap-backups-stored-across-azs
  claim: Backups for both Multi-AZ and Single-AZ FSx for ONTAP file systems are stored across multiple AZs to achieve high durability.
  scope: FSx for NetApp ONTAP backups.
  link: [stored across multiple AZs](../facts/fsx.md#fsx-faq-ontap-backups-stored-across-azs)
fsx-faq-ontap-capacity-pool-elastic-petabytes
  claim: Capacity pool storage is a fully elastic storage tier that can scale to petabytes in size and is cost-optimized for infrequently accessed data.
  scope: FSx for NetApp ONTAP capacity pool storage.
  link: [can scale to petabytes in size](../facts/fsx.md#fsx-faq-ontap-capacity-pool-elastic-petabytes)
fsx-faq-ontap-capacity-pool-no-provisioning
  claim: You do not need to provision storage for data in an FSx for ONTAP file system's capacity pool.
  scope: FSx for NetApp ONTAP capacity pool storage.
  link: [do not need to provision storage](../facts/fsx.md#fsx-faq-ontap-capacity-pool-no-provisioning)
fsx-faq-ontap-clients-linux-windows-macos
  claim: You can access FSx for NetApp ONTAP data from Linux, Windows, or macOS instances running on Amazon EC2, ECS, EKS, VMware Cloud on AWS, Red Hat OpenShift Service on AWS, Amazon WorkSpaces, and Amazon AppStream 2.0.
  scope: FSx for NetApp ONTAP clients.
  link: [Linux, Windows, or macOS instances](../facts/fsx.md#fsx-faq-ontap-clients-linux-windows-macos)
fsx-faq-ontap-compression-dedup-ssd-preserved-in-tier
  claim: You can enable compression and deduplication for data in SSD storage, and the savings are preserved when data is tiered to capacity pool storage. Storage efficiency is always enabled for backup data.
  scope: FSx for NetApp ONTAP storage efficiency.
  link: [preserved when data is tiered to capacity pool](../facts/fsx.md#fsx-faq-ontap-compression-dedup-ssd-preserved-in-tier)
fsx-faq-ontap-encryption-in-transit-options
  claim: FSx for ONTAP supports encrypting data in transit using AWS Nitro-based encryption in select Regions, the IPsec protocol, or Kerberos-based encryption in transit if the file system is joined to an AD.
  scope: FSx for NetApp ONTAP encryption in transit.
  link: [AWS Nitro-based encryption in select Regions](../facts/fsx.md#fsx-faq-ontap-encryption-in-transit-options)
  link: [the IP security (IPsec) protocol](../facts/fsx.md#fsx-faq-ontap-encryption-in-transit-options)
  link: [Kerberos-based encryption in transit](../facts/fsx.md#fsx-faq-ontap-encryption-in-transit-options)
fsx-faq-ontap-encrypts-at-rest-kms
  claim: Amazon FSx for NetApp ONTAP automatically encrypts all your file system's data and backups at rest using keys you manage through AWS KMS.
  scope: FSx for NetApp ONTAP encryption at rest.
  link: [automatically encrypts all your file system’s data](../facts/fsx.md#fsx-faq-ontap-encrypts-at-rest-kms)
fsx-faq-ontap-failover-within-60-seconds
  claim: FSx for ONTAP file systems automatically fail over and back as needed, typically within 60 seconds, and clients automatically fail over and back with the file system.
  scope: FSx for NetApp ONTAP failover; fixed.
  link: [typically within 60 seconds](../facts/fsx.md#fsx-faq-ontap-failover-within-60-seconds)
fsx-faq-ontap-flexcache-cache-for-onprem-data
  claim: You can configure FSx for NetApp ONTAP as a cache for on-premises data by using NetApp FlexCache, to access an on-premises NetApp file system from AWS with low latency.
  scope: FSx for NetApp ONTAP hybrid use.
  link: [NetApp FlexCache](../facts/fsx.md#fsx-faq-ontap-flexcache-cache-for-onprem-data)
fsx-faq-ontap-iscsi-nvme-tcp-block
  claim: FSx for NetApp ONTAP also provides shared block storage over the iSCSI and NVMe-over-TCP protocols.
  scope: FSx for NetApp ONTAP.
  link: [iSCSI and NVMe-over-TCP protocols](../facts/fsx.md#fsx-faq-ontap-iscsi-nvme-tcp-block)
fsx-faq-ontap-latency-ssd-vs-capacity-pool
  claim: FSx for NetApp ONTAP provides consistent sub-millisecond latencies for data on SSD storage and tens of milliseconds of latency for data on capacity pool storage.
  scope: FSx for NetApp ONTAP.
  link: [sub-millisecond latencies](../facts/fsx.md#fsx-faq-ontap-latency-ssd-vs-capacity-pool)
  link: [tens of milliseconds of latency](../facts/fsx.md#fsx-faq-ontap-latency-ssd-vs-capacity-pool)
fsx-faq-ontap-multi-az-two-file-servers-separate-azs
  claim: For Multi-AZ file systems, each FSx for ONTAP file system is powered by two file servers in separate AZs, each with its own storage.
  scope: FSx for NetApp ONTAP Multi-AZ.
  link: [two file servers in separate AZs](../facts/fsx.md#fsx-faq-ontap-multi-az-two-file-servers-separate-azs)
fsx-faq-ontap-multi-az-when
  claim: You should use a Multi-AZ FSx for ONTAP file system if your application needs storage that is highly available and durable across AZs in the same AWS Region.
  scope: FSx for NetApp ONTAP deployment types.
  link: [highly available and durable across AZs](../facts/fsx.md#fsx-faq-ontap-multi-az-when)
fsx-faq-ontap-nfs-smb-multiprotocol
  claim: FSx for NetApp ONTAP provides access over all versions of NFS and SMB, and also supports multi-protocol access, which is concurrent NFS and SMB access to the same data.
  scope: FSx for NetApp ONTAP.
  link: [all versions of the Network File System (NFS)](../facts/fsx.md#fsx-faq-ontap-nfs-smb-multiprotocol)
  link: [multi-protocol access](../facts/fsx.md#fsx-faq-ontap-nfs-smb-multiprotocol)
fsx-faq-ontap-onprem-access-vpn-dx-tgw
  claim: Multi-AZ FSx for ONTAP file systems can be accessed from on premises using AWS VPN or Direct Connect with AWS Transit Gateway.
  scope: FSx for NetApp ONTAP Multi-AZ network access.
  link: [Direct Connect with AWS Transit Gateway](../facts/fsx.md#fsx-faq-ontap-onprem-access-vpn-dx-tgw)
fsx-faq-ontap-primary-storage-provisioned-ssd
  claim: Primary storage is provisioned, high-performance SSD storage purpose-built for the active portion of your data set.
  scope: FSx for NetApp ONTAP primary storage.
  link: [provisioned, high-performance SSD storage](../facts/fsx.md#fsx-faq-ontap-primary-storage-provisioned-ssd)
fsx-faq-ontap-s3-access-points-attach
  claim: You can access FSx file data by attaching S3 Access Points directly to FSx for NetApp ONTAP file systems.
  scope: FSx for NetApp ONTAP with Amazon S3.
  link: [attaching S3 Access Points](../facts/fsx.md#fsx-faq-ontap-s3-access-points-attach)
fsx-faq-ontap-s3-access-points-data-stays-on-fsx
  claim: With S3 Access Points attached, FSx storage appears as an FSX_ONTAP storage class in the S3 API.
  scope: FSx for NetApp ONTAP with Amazon S3.
  link: [FSX_ONTAP storage class](../facts/fsx.md#fsx-faq-ontap-s3-access-points-data-stays-on-fsx)
fsx-faq-ontap-s3-access-points-hundreds
  claim: You can attach up to hundreds of S3 access points to an FSx for ONTAP file system, each configured with application-specific permissions.
  scope: per file system, S3 access points; maximum; not adjustable.
  link: [up to hundreds of access points](../facts/fsx.md#fsx-faq-ontap-s3-access-points-hundreds)
fsx-faq-ontap-scale-tens-gbps-millions-iops
  claim: An FSx for NetApp ONTAP file system can scale up to tens of GB/s and millions of IOPS.
  scope: per file system, FSx for NetApp ONTAP; maximum.
  link: [tens of GB/s and millions of IOPS](../facts/fsx.md#fsx-faq-ontap-scale-tens-gbps-millions-iops)
fsx-faq-ontap-single-az-cost-optimized
  claim: FSx for NetApp ONTAP Single-AZ file systems are built for use cases that need storage replicated within an AZ but do not require resiliency across AZs, such as development and test workloads or secondary copies of data already stored on-premises or in other AWS Regions, and they are cost-optimized for these use cases by only replicating data within an AZ.
  scope: FSx for NetApp ONTAP Single-AZ.
  link: [only replicating data within an AZ](../facts/fsx.md#fsx-faq-ontap-single-az-cost-optimized)
  link: [do not require resiliency across AZs](../facts/fsx.md#fsx-faq-ontap-single-az-cost-optimized)
fsx-faq-ontap-single-az-file-server-pairs
  claim: For Single-AZ file systems, each FSx for ONTAP file system is powered by one or more file server pairs in the same AZ.
  scope: FSx for NetApp ONTAP Single-AZ.
  link: [one or more file server pairs in the same AZ](../facts/fsx.md#fsx-faq-ontap-single-az-file-server-pairs)
fsx-faq-ontap-single-az-sap-hana-certified
  claim: FSx for NetApp ONTAP Single-AZ file systems are SAP-certified for scale-up SAP HANA workloads.
  scope: FSx for NetApp ONTAP Single-AZ file systems.
  link: [SAP-certified for scale-up SAP HANA workloads](../facts/fsx.md#fsx-faq-ontap-single-az-sap-hana-certified)
fsx-faq-ontap-single-az-when
  claim: Single-AZ file systems are built for use cases that need storage replicated within an AZ but do not require resiliency across AZs, such as development and test workloads or secondary copies of data stored on premises or in other Regions.
  scope: FSx for NetApp ONTAP deployment types.
  link: [development and test workloads](../facts/fsx.md#fsx-faq-ontap-single-az-when)
fsx-faq-ontap-snaplock-compliance-no-delete
  claim: In SnapLock Compliance mode, a file once transitioned to WORM cannot be modified or deleted by any user during its retention period.
  scope: FSx for NetApp ONTAP SnapLock Compliance mode.
  link: [cannot be modified or deleted by any user](../facts/fsx.md#fsx-faq-ontap-snaplock-compliance-no-delete)
fsx-faq-ontap-snaplock-compliance-use-case
  claim: You should use SnapLock Compliance to meet regulatory compliance requirements such as SEC Rule 17a-4(f), or to protect your WORM data from ransomware.
  scope: FSx for NetApp ONTAP SnapLock Compliance mode.
  link: [SEC Rule 17a-4(f)](../facts/fsx.md#fsx-faq-ontap-snaplock-compliance-use-case)
fsx-faq-ontap-snaplock-enterprise-flexible
  claim: In SnapLock Enterprise mode, authorized users can selectively delete WORM files or the SnapLock volume at any time.
  scope: FSx for NetApp ONTAP SnapLock Enterprise mode.
  link: [selectively delete WORM files or the SnapLock volume](../facts/fsx.md#fsx-faq-ontap-snaplock-enterprise-flexible)
fsx-faq-ontap-snaplock-two-modes
  claim: Amazon FSx supports two modes of retention with SnapLock: Compliance and Enterprise.
  scope: FSx for NetApp ONTAP SnapLock.
  link: [Compliance and Enterprise](../facts/fsx.md#fsx-faq-ontap-snaplock-two-modes)
fsx-faq-ontap-snapmirror-cross-region
  claim: FSx for ONTAP supports NetApp SnapMirror, which can replicate data automatically to another FSx for ONTAP file system, including one in another AWS Region.
  scope: FSx for NetApp ONTAP replication.
  link: [NetApp SnapMirror replication](../facts/fsx.md#fsx-faq-ontap-snapmirror-cross-region)
fsx-faq-ontap-snapmirror-rpo-5-minutes
  claim: With SnapMirror you can configure replication with a Recovery Point Objective of as low as five minutes and a Recovery Time Objective in single-digit minutes.
  scope: FSx for NetApp ONTAP SnapMirror replication; minimum.
  link: [as low as five minutes](../facts/fsx.md#fsx-faq-ontap-snapmirror-rpo-5-minutes)
  link: [single-digit minutes](../facts/fsx.md#fsx-faq-ontap-snapmirror-rpo-5-minutes)
fsx-faq-ontap-snapshots-previous-versions
  claim: Linux and macOS end users can view FSx for ONTAP snapshots in the .snapshot directory at the root of their file system.
  scope: FSx for NetApp ONTAP snapshots.
  link: [.snapshot](../facts/fsx.md#fsx-faq-ontap-snapshots-previous-versions)
fsx-faq-ontap-ssd-capacity-grow-or-shrink
  claim: You can grow or shrink the SSD tier capacity of an FSx for NetApp ONTAP file system at any time while continuing to use it.
  scope: FSx for NetApp ONTAP SSD tier.
  link: [grow or shrink the capacity](../facts/fsx.md#fsx-faq-ontap-ssd-capacity-grow-or-shrink)
fsx-faq-ontap-svm-isolated-file-server
  claim: A storage virtual machine (SVM) is an isolated file server with its own administrative credentials and endpoints for administering and accessing data.
  scope: FSx for NetApp ONTAP SVMs.
  link: [isolated file server](../facts/fsx.md#fsx-faq-ontap-svm-isolated-file-server)
fsx-faq-ontap-svms-share-storage-and-throughput
  claim: Each SVM is a virtual resource, so the SVMs in an FSx for ONTAP file system share the file system's storage and throughput capacity.
  scope: FSx for NetApp ONTAP SVMs.
  link: [share your file system’s storage and throughput capacity](../facts/fsx.md#fsx-faq-ontap-svms-share-storage-and-throughput)
fsx-faq-ontap-throughput-change-failover-transparent
  claim: Changing throughput capacity causes an automatic failover and failback that typically takes a few minutes and is transparent to NFS, SMB and iSCSI clients.
  scope: FSx for NetApp ONTAP throughput change.
  link: [typically takes a few minutes to complete](../facts/fsx.md#fsx-faq-ontap-throughput-change-failover-transparent)
fsx-faq-ontap-tiering-block-level-any-file-size
  claim: All files in FSx for ONTAP volumes can be transitioned to capacity pool storage, regardless of size.
  scope: FSx for NetApp ONTAP capacity pool tiering.
  link: [regardless of size](../facts/fsx.md#fsx-faq-ontap-tiering-block-level-any-file-size)
fsx-faq-ontap-tiering-cooling-period-2-to-183-days
  claim: For the Auto or Snapshot-only tiering policy you can optionally specify a minimum cooling period between 2 and 183 days before data becomes a candidate for the capacity pool.
  scope: per volume, Auto or Snapshot-only tiering policy; maximum; adjustable.
  link: [between 2 and 183 days](../facts/fsx.md#fsx-faq-ontap-tiering-cooling-period-2-to-183-days)
fsx-faq-ontap-tiering-no-percentage-limit
  claim: Amazon FSx does not limit the percentage of your data that you can tier to capacity pool storage.
  scope: FSx for NetApp ONTAP capacity pool tiering.
  link: [does not limit to the percentage](../facts/fsx.md#fsx-faq-ontap-tiering-no-percentage-limit)
fsx-faq-ontap-tiering-policy-auto-default
  claim: Each FSx for ONTAP volume has a tiering policy; you can choose from four policies, and volumes created with the AWS Console use the Auto policy by default.
  scope: per volume, volumes created with the AWS Console; default; adjustable.
  link: [“Auto” tiering policy](../facts/fsx.md#fsx-faq-ontap-tiering-policy-auto-default)
fsx-faq-ontap-two-storage-tiers
  claim: Each FSx for NetApp ONTAP file system has two storage tiers: primary storage and capacity pool storage.
  scope: FSx for NetApp ONTAP storage tiers.
  link: [primary storage and capacity pool storage](../facts/fsx.md#fsx-faq-ontap-two-storage-tiers)
fsx-faq-ontap-virtually-no-data-limit
  claim: There is virtually no limit to how much data you can store in a single FSx for NetApp ONTAP file system.
  scope: per file system, FSx for NetApp ONTAP; maximum; not adjustable.
  link: [virtually no limit](../facts/fsx.md#fsx-faq-ontap-virtually-no-data-limit)
fsx-faq-ontap-windows-previous-versions-tab
  claim: Windows end users can view FSx for ONTAP snapshots in the Previous Versions tab of Windows Explorer.
  scope: FSx for NetApp ONTAP snapshots.
  link: [Previous Versions](../facts/fsx.md#fsx-faq-ontap-windows-previous-versions-tab)
fsx-faq-ontap-worm-snaplock
  claim: FSx for NetApp ONTAP offers write-once-read-many (WORM) protection for data with SnapLock.
  scope: FSx for NetApp ONTAP SnapLock.
  link: [write-once-read-many (WORM) protection](../facts/fsx.md#fsx-faq-ontap-worm-snaplock)
fsx-faq-openzfs-3-iops-per-gb
  claim: Each gigabyte of FSx for OpenZFS storage includes three disk IOPS, and you can provision additional disk IOPS as needed.
  scope: per GB of storage; default; adjustable.
  link: [three disk IOPS](../facts/fsx.md#fsx-faq-openzfs-3-iops-per-gb)
fsx-faq-openzfs-512-tib-max-per-file-system
  claim: You can provision up to a maximum of 512 TiBs on a single FSx for OpenZFS file system.
  scope: per file system, FSx for OpenZFS; maximum; not adjustable.
  link: [512 TiBs](../facts/fsx.md#fsx-faq-openzfs-512-tib-max-per-file-system)
fsx-faq-openzfs-at-rest-always-kms
  claim: FSx for OpenZFS file system data and backups are always encrypted at rest using keys you manage through AWS KMS.
  scope: FSx for OpenZFS encryption at rest.
  link: [always encrypted at rest](../facts/fsx.md#fsx-faq-openzfs-at-rest-always-kms)
fsx-faq-openzfs-backups-pit-consistent-incremental-rto
  claim: FSx for OpenZFS backups are point-in-time consistent, incremental, easy to manage, and quick to create and restore, with an RTO of 5-10 minutes.
  scope: FSx for OpenZFS backups.
  link: [RTO of 5-10 minutes](../facts/fsx.md#fsx-faq-openzfs-backups-pit-consistent-incremental-rto)
  link: [point-in-time consistent](../facts/fsx.md#fsx-faq-openzfs-backups-pit-consistent-incremental-rto)
fsx-faq-openzfs-billing-dimensions
  claim: FSx for OpenZFS file systems are billed on provisioned storage capacity (per GB-month), provisioned throughput (per MBps-month) and optional additional SSD IOPS (per IOP-month).
  scope: FSx for OpenZFS pricing.
  link: [storage capacity provisioned (per GB-month)](../facts/fsx.md#fsx-faq-openzfs-billing-dimensions)
  link: [throughput provisioned (per MBps-month)](../facts/fsx.md#fsx-faq-openzfs-billing-dimensions)
fsx-faq-openzfs-cache-hit-ratio-80-percent
  claim: For most workloads, a cache hit ratio of 80% provides the right balance of performance and cost optimization.
  scope: FSx Intelligent-Tiering SSD read cache.
  link: [cache hit ratio of 80%](../facts/fsx.md#fsx-faq-openzfs-cache-hit-ratio-80-percent)
fsx-faq-openzfs-cached-vs-ssd-throughput
  claim: FSx for OpenZFS file systems can deliver over 1 million IOPS and 21 GB/s when accessing data cached on the file server, and hundreds of thousands of IOPS and 10 GB/s when accessing data in SSD storage.
  scope: per file system, FSx for OpenZFS; maximum; not adjustable.
  link: [21 GB/s](../facts/fsx.md#fsx-faq-openzfs-cached-vs-ssd-throughput)
  link: [10 GB/s](../facts/fsx.md#fsx-faq-openzfs-cached-vs-ssd-throughput)
fsx-faq-openzfs-clients-linux-windows-macos
  claim: You can access FSx for OpenZFS data from Linux, Windows, or macOS clients running on Amazon EC2, ECS, EKS, VMware Cloud on AWS, Amazon WorkSpaces, and Amazon AppStream 2.0.
  scope: FSx for OpenZFS clients.
  link: [Linux, Windows, or macOS clients](../facts/fsx.md#fsx-faq-openzfs-clients-linux-windows-macos)
fsx-faq-openzfs-compression-write-heavy-tradeoff
  claim: Enabling compression may reduce FSx for OpenZFS file system performance for write-heavy workloads, because data is compressed as it is written to disk.
  scope: FSx for OpenZFS compression.
  link: [may reduce file system performance for write-heavy workloads](../facts/fsx.md#fsx-faq-openzfs-compression-write-heavy-tradeoff)
fsx-faq-openzfs-copy-backups-to-other-regions
  claim: FSx for OpenZFS can copy file system backups to other AWS Regions to meet cross-Region disaster recovery or business continuity objectives.
  scope: FSx for OpenZFS disaster recovery.
  link: [copy file system backups to other AWS Regions](../facts/fsx.md#fsx-faq-openzfs-copy-backups-to-other-regions)
fsx-faq-openzfs-daily-backups-default-cross-region-copy
  claim: Daily automatic backups are enabled by default for FSx for OpenZFS, and you can update the retention policy at any time.
  scope: FSx for OpenZFS backups; default; adjustable.
  link: [Daily automatic backups are enabled by default](../facts/fsx.md#fsx-faq-openzfs-daily-backups-default-cross-region-copy)
fsx-faq-openzfs-encrypts-at-rest-and-in-transit
  claim: FSx for OpenZFS automatically encrypts data at rest and in transit.
  scope: FSx for OpenZFS encryption.
  link: [automatically encrypts data at rest and in transit](../facts/fsx.md#fsx-faq-openzfs-encrypts-at-rest-and-in-transit)
fsx-faq-openzfs-ha-pair-failover-60-seconds
  claim: With FSx for OpenZFS Multi-AZ (HA) and Single-AZ (HA) file systems, Amazon FSx deploys an HA pair of file servers with automatic failover and failback; file systems automatically fail over and back as needed, typically within 60 seconds, and clients automatically fail over and back with the file system.
  scope: FSx for OpenZFS HA file systems; fixed.
  link: [typically within 60 seconds](../facts/fsx.md#fsx-faq-openzfs-ha-pair-failover-60-seconds)
fsx-faq-openzfs-ha-pair-of-file-servers
  claim: With Multi-AZ (HA) and Single-AZ (HA) file systems, Amazon FSx deploys a high-availability pair of file servers with automatic failover and failback.
  scope: FSx for OpenZFS HA file systems.
  link: [high-availability (HA) pair of file servers](../facts/fsx.md#fsx-faq-openzfs-ha-pair-of-file-servers)
fsx-faq-openzfs-intelligent-tiering-20-gbps-400k-iops
  claim: The Intelligent-Tiering storage class delivers up to 20 Gigabytes per second of throughput and 400,000 IOPS on OpenZFS.
  scope: per file system, FSx for OpenZFS Intelligent-Tiering; maximum; not adjustable.
  link: [up to 20 Gigabytes per second](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-20-gbps-400k-iops)
  link: [400,000 IOPS](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-20-gbps-400k-iops)
fsx-faq-openzfs-intelligent-tiering-30-90-day-tiers
  claim: Intelligent-Tiering stores data accessed in the last 30 days in the Frequent Access tier, moves data not accessed in 30 days to Infrequent Access, and data not accessed in 90 days to Archive.
  scope: FSx Intelligent-Tiering storage class.
  link: [accessed in the last 30 days](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-30-90-day-tiers)
  link: [hasn’t been accessed in 90 days](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-30-90-day-tiers)
fsx-faq-openzfs-intelligent-tiering-85-percent-lower-than-ssd
  claim: Intelligent-Tiering provides up to 85% lower costs than the FSx SSD storage class and up to 20% lower costs compared to traditional on-premises HDD deployments.
  scope: FSx for OpenZFS Intelligent-Tiering; maximum.
  link: [up to 85% lower costs](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-85-percent-lower-than-ssd)
  link: [up to 20% lower costs](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-85-percent-lower-than-ssd)
fsx-faq-openzfs-intelligent-tiering-available-on-openzfs
  claim: The Amazon FSx Intelligent-Tiering storage class combines NAS familiarity with fully elastic storage that tiers data automatically, and is currently available on FSx for OpenZFS file systems.
  scope: FSx Intelligent-Tiering storage class.
  link: [optimizes costs by tiering data automatically](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-available-on-openzfs)
fsx-faq-openzfs-intelligent-tiering-billing
  claim: For FSx Intelligent-Tiering you pay per GB per month for the data you store, with the price dependent on the tier the data is stored in, and per GB per month for your provisioned SSD read cache.
  scope: FSx Intelligent-Tiering pricing.
  link: [price dependent on the tier](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-billing)
fsx-faq-openzfs-intelligent-tiering-moves-back-no-extra-fees
  claim: When you access data in the Infrequent Access or Archive tiers, the data automatically moves back to the Frequent Access tier.
  scope: FSx Intelligent-Tiering storage class.
  link: [automatically moves back to the Frequent Access tier](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-moves-back-no-extra-fees)
fsx-faq-openzfs-intelligent-tiering-multi-az-redundant
  claim: For file systems using the FSx Intelligent-Tiering storage class, Amazon FSx stores all of your data redundantly across multiple Availability Zones.
  scope: FSx Intelligent-Tiering storage class.
  link: [redundantly across multiple Availability Zones (AZs)](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-multi-az-redundant)
fsx-faq-openzfs-intelligent-tiering-no-retrieval-costs
  claim: With FSx Intelligent-Tiering there are no additional IOPS, retrieval, or transition costs beyond your normal read/write operation costs.
  scope: FSx Intelligent-Tiering storage class.
  link: [no additional IOPS, retrieval, or transition costs](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-no-retrieval-costs)
fsx-faq-openzfs-intelligent-tiering-sla-99-99
  claim: The Amazon FSx Intelligent-Tiering storage class provides an SLA of 99.99%.
  scope: FSx Intelligent-Tiering storage class; fixed.
  link: [99.99%](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-sla-99-99)
fsx-faq-openzfs-intelligent-tiering-vs-ssd-choice
  claim: Use the Intelligent-Tiering storage class for most NAS data sets, and the SSD storage class only for data sets that require the performance of all-flash storage across all data.
  scope: FSx for OpenZFS storage classes.
  link: [performance of all-flash storage across all data](../facts/fsx.md#fsx-faq-openzfs-intelligent-tiering-vs-ssd-choice)
fsx-faq-openzfs-multi-az-ha-recommended
  claim: AWS recommends Multi-AZ highly available (HA) file systems for most production workloads for the high availability and durability model they provide.
  scope: FSx for OpenZFS deployment types.
  link: [Multi-AZ highly available (HA) file systems](../facts/fsx.md#fsx-faq-openzfs-multi-az-ha-recommended)
fsx-faq-openzfs-nfs-versions-and-s3-api
  claim: FSx for OpenZFS provides access to shared file storage over NFS v3, v4, v4.1 and v4.2, and over the S3 API by attaching S3 Access Points to the file system.
  scope: FSx for OpenZFS.
  link: [NFS protocol (v3, v4, v4.1, v4.2)](../facts/fsx.md#fsx-faq-openzfs-nfs-versions-and-s3-api)
fsx-faq-openzfs-other-vpc-and-onprem-access
  claim: You can access FSx for OpenZFS file systems from another VPC, including a VPC in another Region, using AWS Transit Gateway or VPC Peering, and from on premises using AWS Direct Connect or VPN.
  scope: FSx for OpenZFS network access.
  link: [AWS Transit Gateway or VPC Peering](../facts/fsx.md#fsx-faq-openzfs-other-vpc-and-onprem-access)
fsx-faq-openzfs-over-1-million-iops-hundreds-of-microseconds
  claim: FSx for OpenZFS delivers over 1 million IOPS, with latencies as low as a few hundred microseconds for high-performance workloads.
  scope: FSx for OpenZFS.
  link: [over 1 million IOPs](../facts/fsx.md#fsx-faq-openzfs-over-1-million-iops-hundreds-of-microseconds)
  link: [a few hundred microseconds](../facts/fsx.md#fsx-faq-openzfs-over-1-million-iops-hundreds-of-microseconds)
fsx-faq-openzfs-posix-permissions
  claim: You control which users and groups have access to which files and directories on your FSx for OpenZFS volumes using POSIX permissions.
  scope: FSx for OpenZFS access control.
  link: [POSIX permissions](../facts/fsx.md#fsx-faq-openzfs-posix-permissions)
fsx-faq-openzfs-restore-access-within-minutes
  claim: The FSx for OpenZFS FAQ says that when you restore from a backup by creating a new file system with the restore from backup option, you can access all of your data within minutes while the restore completes in the background.
  scope: FSx for OpenZFS restore from backup.
  link: [within minutes](../facts/fsx.md#fsx-faq-openzfs-restore-access-within-minutes)
fsx-faq-openzfs-s3-access-points-attach
  claim: You can access FSx file data by attaching S3 Access Points directly to your FSx for OpenZFS file systems.
  scope: FSx for OpenZFS with Amazon S3.
  link: [attaching S3 Access Points](../facts/fsx.md#fsx-faq-openzfs-s3-access-points-attach)
fsx-faq-openzfs-s3-access-points-storage-class
  claim: With S3 Access Points attached, FSx storage appears as an FSX_OPENZFS storage class in the S3 API.
  scope: FSx for OpenZFS with Amazon S3.
  link: [FSX_OPENZFS storage class](../facts/fsx.md#fsx-faq-openzfs-s3-access-points-storage-class)
fsx-faq-openzfs-scale-throughput-any-time
  claim: You can scale throughput capacity of an FSx for OpenZFS file system up or down at any time using the console, AWS CLI or Amazon FSx API.
  scope: FSx for OpenZFS throughput capacity.
  link: [scale up or down throughput capacity](../facts/fsx.md#fsx-faq-openzfs-scale-throughput-any-time)
fsx-faq-openzfs-single-az-ha-when
  claim: Use Single-AZ (HA) for workloads that require consistent single-AZ latencies, such as certain EDA and HPC workloads, and as a cost-effective solution for workloads that do not require the durability of Multi-AZ (HA).
  scope: FSx for OpenZFS Single-AZ (HA).
  link: [consistent single-AZ latencies](../facts/fsx.md#fsx-faq-openzfs-single-az-ha-when)
fsx-faq-openzfs-single-az-non-ha-recovery-30-minutes
  claim: With Single-AZ (non-HA) file systems, Amazon FSx resumes availability after failure events by monitoring for hardware failures and replacing infrastructure components, typically within 30 minutes.
  scope: FSx for OpenZFS Single-AZ (non-HA); fixed.
  link: [typically within 30 minutes](../facts/fsx.md#fsx-faq-openzfs-single-az-non-ha-recovery-30-minutes)
fsx-faq-openzfs-single-az-non-ha-when
  claim: Use Single-AZ (non-HA) file systems for testing and development, meaning non-production workloads that do not require high availability or durability and can tolerate downtimes, typically up to 30 minutes, caused by recoverable hardware failures and planned maintenance.
  scope: FSx for OpenZFS Single-AZ (non-HA).
  link: [typically up to 30 minutes](../facts/fsx.md#fsx-faq-openzfs-single-az-non-ha-when)
fsx-faq-openzfs-snapshot-directory-zfs-snapshot
  claim: End users and application administrators can view FSx for OpenZFS snapshots in the .zfs/snapshot directory at the root of a volume, and can access individual files and folders in those snapshots.
  scope: FSx for OpenZFS snapshots.
  link: [.zfs/snapshot](../facts/fsx.md#fsx-faq-openzfs-snapshot-directory-zfs-snapshot)
fsx-faq-openzfs-snapshots-clones-replication
  claim: FSx for OpenZFS offers ZFS-powered capabilities including point-in-time snapshots, in-place data cloning, and on-demand data replication across file systems.
  scope: FSx for OpenZFS.
  link: [point-in-time snapshots, in-place data cloning](../facts/fsx.md#fsx-faq-openzfs-snapshots-clones-replication)
  link: [on-demand data replication across file systems](../facts/fsx.md#fsx-faq-openzfs-snapshots-clones-replication)
fsx-faq-openzfs-ssd-read-cache-default-sizing
  claim: By default, Amazon FSx automatically selects an SSD read cache size based on the throughput level you choose, or you can choose a smaller or larger cache and scale it up or down at any time.
  scope: FSx Intelligent-Tiering SSD read cache; default; adjustable.
  link: [automatically selects an SSD read cache size](../facts/fsx.md#fsx-faq-openzfs-ssd-read-cache-default-sizing)
fsx-faq-openzfs-volume-grow-quota-reservation
  claim: By default, FSx for OpenZFS volumes can grow up to the available capacity on the file system; you can set a quota to limit volume size and a reservation to set aside a minimum amount of capacity.
  scope: per volume, FSx for OpenZFS; default; adjustable.
  link: [grow up to the available capacity](../facts/fsx.md#fsx-faq-openzfs-volume-grow-quota-reservation)
fsx-faq-openzfs-volumes-thin-provisioned-without-reservation
  claim: Without a reservation, FSx for OpenZFS volumes are thin-provisioned and consume storage capacity only for the data stored in them.
  scope: FSx for OpenZFS volumes.
  link: [thin-provisioned](../facts/fsx.md#fsx-faq-openzfs-volumes-thin-provisioned-without-reservation)
fsx-faq-windows-3-iops-per-gb-ssd
  claim: Each gigabyte of SSD storage includes 3 disk IOPS, and additional IOPS can be provisioned as needed.
  scope: per GB of SSD storage; default; adjustable.
  link: [3 disk IOPS](../facts/fsx.md#fsx-faq-windows-3-iops-per-gb-ssd)
fsx-faq-windows-access-control-acls-sg-iam
  claim: FSx provides standard Windows permissions (full support for Windows ACLs) for files and folders.
  scope: FSx for Windows File Server access control.
  link: [standard Windows permissions](../facts/fsx.md#fsx-faq-windows-access-control-acls-sg-iam)
fsx-faq-windows-active-directory-join
  claim: When creating an FSx file system you join it to your Microsoft AD, either an AWS Managed Microsoft AD or your self-managed Microsoft AD.
  scope: FSx for Windows File Server authentication.
  link: [AWS Managed Microsoft AD](../facts/fsx.md#fsx-faq-windows-active-directory-join)
  link: [self-managed Microsoft AD](../facts/fsx.md#fsx-faq-windows-active-directory-join)
fsx-faq-windows-always-encrypts-at-rest-kms
  claim: FSx for Windows File Server always encrypts file system data and backups at rest using keys you manage through AWS KMS.
  scope: FSx for Windows File Server encryption at rest.
  link: [always encrypts your file system data](../facts/fsx.md#fsx-faq-windows-always-encrypts-at-rest-kms)
fsx-faq-windows-audit-default-on-console
  claim: When you create an FSx for Windows file system from the AWS Management Console, file access auditing is turned on by default.
  scope: FSx for Windows File Server created from the console; default; adjustable.
  link: [file access auditing is turned on by default](../facts/fsx.md#fsx-faq-windows-audit-default-on-console)
fsx-faq-windows-backup-window-30-minutes
  claim: The daily backup window is a 30-minute window that you specify when creating a file system.
  scope: per file system, daily automatic backup; fixed; not adjustable.
  link: [30-minute window](../facts/fsx.md#fsx-faq-windows-backup-window-30-minutes)
fsx-faq-windows-backups-stored-in-s3
  claim: To ensure high durability, Amazon FSx stores backups in Amazon S3.
  scope: FSx for Windows File Server backups.
  link: [stores backups in Amazon S3](../facts/fsx.md#fsx-faq-windows-backups-stored-in-s3)
fsx-faq-windows-billing-dimensions
  claim: FSx for Windows File Server is billed hourly based on deployment type, storage type, storage capacity, throughput capacity and SSD IOPS above the default 3 IOPS included for every GB of SSD storage.
  scope: FSx for Windows File Server pricing.
  link: [deployment type (Single-AZ or Multi-AZ)](../facts/fsx.md#fsx-faq-windows-billing-dimensions)
  link: [default 3 IOPS](../facts/fsx.md#fsx-faq-windows-billing-dimensions)
fsx-faq-windows-built-on-windows-server-ad
  claim: FSx for Windows File Server is built on Windows Server and offers administrative features such as user quotas, end-user file restore and Microsoft Active Directory integration.
  scope: FSx for Windows File Server.
  link: [built on Windows Server](../facts/fsx.md#fsx-faq-windows-built-on-windows-server-ad)
  link: [Microsoft Active Directory (AD) integration](../facts/fsx.md#fsx-faq-windows-built-on-windows-server-ad)
fsx-faq-windows-clients-and-concurrency
  claim: Amazon FSx is accessible from Windows, Linux and MacOS compute instances and devices, and thousands of them can access a file system concurrently.
  scope: FSx for Windows File Server clients.
  link: [Windows, Linux, and MacOS](../facts/fsx.md#fsx-faq-windows-clients-and-concurrency)
  link: [Thousands of compute instances and devices](../facts/fsx.md#fsx-faq-windows-clients-and-concurrency)
fsx-faq-windows-daily-backups-incremental
  claim: FSx takes daily automatic backups of file systems and allows additional backups at any point.
  scope: FSx for Windows File Server backups.
  link: [daily automatic backups](../facts/fsx.md#fsx-faq-windows-daily-backups-incremental)
fsx-faq-windows-datasync-replicate-same-and-cross-region
  claim: You can use AWS DataSync to schedule periodic replication of an FSx for Windows file system to a second file system, in the same Region or across Regions.
  scope: FSx for Windows File Server replication.
  link: [AWS DataSync](../facts/fsx.md#fsx-faq-windows-datasync-replicate-same-and-cross-region)
fsx-faq-windows-dedup-definition
  claim: Data Deduplication is a Windows Server feature that reduces costs from redundant and uncompressed data by storing duplicated portions of files only once and compressing the data after deduplication.
  scope: FSx for Windows File Server Data Deduplication.
  link: [storing duplicated portions of files only once](../facts/fsx.md#fsx-faq-windows-dedup-definition)
fsx-faq-windows-dedup-typical-savings
  claim: Typical Data Deduplication savings average 50-60% for general-purpose file shares, 30-50% for user documents and 70-80% for software development data sets.
  scope: FSx for Windows File Server Data Deduplication, typical savings.
  link: [50-60%](../facts/fsx.md#fsx-faq-windows-dedup-typical-savings)
  link: [30-50%](../facts/fsx.md#fsx-faq-windows-dedup-typical-savings)
  link: [70-80%](../facts/fsx.md#fsx-faq-windows-dedup-typical-savings)
fsx-faq-windows-delete-fs-deletes-automatic-backups
  claim: When you delete an FSx file system, all its automatic daily backups are deleted, and user-initiated backups remain.
  scope: FSx for Windows File Server backups.
  link: [automatic daily backups associated with the file system](../facts/fsx.md#fsx-faq-windows-delete-fs-deletes-automatic-backups)
fsx-faq-windows-dfs-hundreds-of-pb
  claim: Amazon FSx supports Microsoft Distributed File System (DFS) to organize shares from multiple file systems into a single folder structure up to hundreds of PB in size.
  scope: FSx for Windows File Server.
  link: [Distributed File System (DFS)](../facts/fsx.md#fsx-faq-windows-dfs-hundreds-of-pb)
  link: [hundreds of PB](../facts/fsx.md#fsx-faq-windows-dfs-hundreds-of-pb)
fsx-faq-windows-dfs-namespaces-scale-out
  claim: FSx supports Microsoft DFS Namespaces to scale out performance across multiple file systems in the same namespace, up to tens of GBps and millions of IOPs.
  scope: FSx for Windows File Server.
  link: [DFS) Namespaces](../facts/fsx.md#fsx-faq-windows-dfs-namespaces-scale-out)
  link: [tens of GBps and millions of IOPs](../facts/fsx.md#fsx-faq-windows-dfs-namespaces-scale-out)
fsx-faq-windows-failback-under-20-minutes
  claim: Failback occurs once the file server in the preferred subnet is fully recovered, typically under 20 minutes, and also completes within 30 seconds.
  scope: FSx for Windows File Server Multi-AZ failback.
  link: [typically under 20 minutes](../facts/fsx.md#fsx-faq-windows-failback-under-20-minutes)
  link: [completes within 30 seconds](../facts/fsx.md#fsx-faq-windows-failback-under-20-minutes)
fsx-faq-windows-failover-30-seconds
  claim: Failovers in a Multi-AZ FSx for Windows file system typically complete within 30 seconds, measured from detection of the failure to promotion of the other file server.
  scope: FSx for Windows File Server Multi-AZ failover; fixed.
  link: [typically complete within 30 seconds](../facts/fsx.md#fsx-faq-windows-failover-30-seconds)
fsx-faq-windows-failover-triggers
  claim: FSx automatically fails over on loss of availability of the active file server, caused by a failure in the active AZ or of the file server itself, and also temporarily fails over during planned maintenance or when throughput scaling is started.
  scope: FSx for Windows File Server Multi-AZ failover.
  link: [failure in the active Availability Zone](../facts/fsx.md#fsx-faq-windows-failover-triggers)
fsx-faq-windows-file-gateway-onprem
  claim: Amazon FSx File Gateway provides low-latency, on-premises access to fully managed file shares in the cloud.
  scope: FSx for Windows File Server.
  link: [Amazon FSx File Gateway](../facts/fsx.md#fsx-faq-windows-file-gateway-onprem)
fsx-faq-windows-hdd-workloads
  claim: HDD storage is designed for a broad spectrum of workloads, including home directories, user and departmental shares, and content management systems.
  scope: FSx for Windows File Server HDD storage.
  link: [home directories, user and departmental shares](../facts/fsx.md#fsx-faq-windows-hdd-workloads)
fsx-faq-windows-in-transit-smb-3-kerberos
  claim: FSx encrypts data in transit using SMB Kerberos session keys when you access the file system from clients that support SMB 3.0 and higher.
  scope: FSx for Windows File Server encryption in transit.
  link: [SMB 3.0 (and higher)](../facts/fsx.md#fsx-faq-windows-in-transit-smb-3-kerberos)
fsx-faq-windows-increase-storage-change-throughput
  claim: You can increase the storage capacity, and increase or decrease the throughput capacity, of an FSx for Windows file system while continuing to use it, at any time.
  scope: FSx for Windows File Server scaling.
  link: [increase or decrease the throughput capacity](../facts/fsx.md#fsx-faq-windows-increase-storage-change-throughput)
fsx-faq-windows-latency-ssd-hdd
  claim: FSx for Windows File Server provides consistent sub-millisecond latencies with SSD storage and single-digit millisecond latencies with HDD storage for file operations.
  scope: FSx for Windows File Server file operations.
  link: [sub-millisecond latencies with SSD storage](../facts/fsx.md#fsx-faq-windows-latency-ssd-hdd)
  link: [single-digit millisecond latencies with HDD storage](../facts/fsx.md#fsx-faq-windows-latency-ssd-hdd)
fsx-faq-windows-linux-clients-no-auto-failover
  claim: Linux clients do not automatically connect to the standby file server upon a failover, and automatically resume file system operations once failback to the preferred file server is complete.
  scope: FSx for Windows File Server Multi-AZ clients.
  link: [don’t automatically connect to the standby file server](../facts/fsx.md#fsx-faq-windows-linux-clients-no-auto-failover)
fsx-faq-windows-multi-vpc-peering-tgw
  claim: You can access FSx file systems from multiple VPCs, AWS accounts and AWS Regions using VPC Peering connections or AWS Transit Gateway.
  scope: FSx for Windows File Server network access.
  link: [VPC Peering connections or AWS Transit Gateway](../facts/fsx.md#fsx-faq-windows-multi-vpc-peering-tgw)
fsx-faq-windows-onprem-direct-connect-vpn
  claim: You can access FSx file systems from on premises using an AWS Direct Connect or AWS VPN connection between your on-premises datacenter and your Amazon VPC.
  scope: FSx for Windows File Server network access.
  link: [AWS Direct Connect or AWS VPN connection](../facts/fsx.md#fsx-faq-windows-onprem-direct-connect-vpn)
fsx-faq-windows-scaling-no-additional-cost
  claim: Scaling storage capacity and throughput capacity of an FSx for Windows file system is available at no additional cost.
  scope: FSx for Windows File Server scaling.
  link: [no additional cost](../facts/fsx.md#fsx-faq-windows-scaling-no-additional-cost)
fsx-faq-windows-shadow-copies-restore
  claim: FSx supports file- or folder-level restores to previous versions through Windows shadow copies, which are point-in-time snapshots of the file system.
  scope: FSx for Windows File Server end-user restore.
  link: [Windows shadow copies](../facts/fsx.md#fsx-faq-windows-shadow-copies-restore)
fsx-faq-windows-single-az-definition
  claim: Single-AZ file systems have a single Windows file server instance and a set of storage volumes within one Availability Zone.
  scope: FSx for Windows File Server Single-AZ.
  link: [a single Windows file server instance](../facts/fsx.md#fsx-faq-windows-single-az-definition)
fsx-faq-windows-smb-protocol
  claim: Amazon FSx for Windows File Server provides file storage that is accessible from compute instances over the SMB protocol.
  scope: FSx for Windows File Server.
  link: [the SMB protocol](../facts/fsx.md#fsx-faq-windows-smb-protocol)
fsx-faq-windows-ssd-workloads
  claim: SSD storage is designed for the highest-performance and most latency-sensitive workloads, including databases, media processing workloads, and data analytics applications.
  scope: FSx for Windows File Server SSD storage.
  link: [databases, media processing workloads, and data analytics applications](../facts/fsx.md#fsx-faq-windows-ssd-workloads)
fsx-faq-windows-storage-grow-no-downtime
  claim: FSx grows the storage capacity of an existing FSx for Windows file system without downtime impact, by adding larger disks, migrating data in the background, and removing the original disks.
  scope: FSx for Windows File Server storage scaling.
  link: [without any downtime impact](../facts/fsx.md#fsx-faq-windows-storage-grow-no-downtime)
fsx-faq-windows-storage-types-hdd-ssd
  claim: Amazon FSx for Windows File Server provides two types of storage, Hard Disk Drives (HDD) and Solid State Drives (SSD), to optimize cost and performance.
  scope: FSx for Windows File Server storage types.
  link: [Hard Disk Drives (HDD)](../facts/fsx.md#fsx-faq-windows-storage-types-hdd-ssd)
  link: [Solid State Drives (SSD)](../facts/fsx.md#fsx-faq-windows-storage-types-hdd-ssd)
fsx-faq-windows-supported-windows-versions
  claim: Amazon FSx supports all Windows versions starting from Windows Server 2008 and Windows 7, and current versions of Linux using the cifs-utils tool.
  scope: FSx for Windows File Server clients.
  link: [starting from Windows Server 2008 and Windows 7](../facts/fsx.md#fsx-faq-windows-supported-windows-versions)
  link: [cifs-utils](../facts/fsx.md#fsx-faq-windows-supported-windows-versions)
fsx-faq-windows-throughput-capacity-configurable
  claim: Every FSx for Windows file system has a throughput capacity that you configure when the file system is created and that you can change at any time.
  scope: FSx for Windows File Server.
  link: [throughput capacity that you conﬁgure](../facts/fsx.md#fsx-faq-windows-throughput-capacity-configurable)
fsx-faq-windows-throughput-update-failover
  claim: Updating the throughput capacity typically takes a few minutes; Multi-AZ file systems experience an automatic failover and failback, and single-AZ file systems are offline for a brief period.
  scope: FSx for Windows File Server throughput change.
  link: [typically takes a few minutes](../facts/fsx.md#fsx-faq-windows-throughput-update-failover)
  link: [offline for a brief period of time](../facts/fsx.md#fsx-faq-windows-throughput-update-failover)
fsx-lustre-auto-export-and-export-tasks-not-simultaneous
  claim: Automatic import and import data repository tasks can be used simultaneously on a file system, but automatic export and export data repository tasks can't be used simultaneously.
  scope: FSx for Lustre data repository.
  link: [can be used simultaneously](../facts/fsx.md#fsx-lustre-auto-export-and-export-tasks-not-simultaneous)
  link: [can't be used simultaneously](../facts/fsx.md#fsx-lustre-auto-export-and-export-tasks-not-simultaneous)
fsx-lustre-automatic-import-and-export-defaults-console-versus-cli
  claim: Automatic import and automatic export (new, changed, deleted) are turned on by default when you add a data repository from the console, but are disabled by default when you use the AWS CLI or the Amazon FSx API.
  scope: FSx for Lustre data repository association; default; adjustable.
  link: [turned on by default when you add](../facts/fsx.md#fsx-lustre-automatic-import-and-export-defaults-console-versus-cli)
  link: [disabled by default when using the AWS CLI](../facts/fsx.md#fsx-lustre-automatic-import-and-export-defaults-console-versus-cli)
fsx-lustre-automatic-import-export-behavior
  claim: With automatic import the file system imports file metadata as files are created, modified or deleted in the S3 data repository, and with automatic export it exports file data and metadata as files are created, modified or deleted on the file system.
  scope: FSx for Lustre data repository association.
  link: [automatically imports file metadata](../facts/fsx.md#fsx-lustre-automatic-import-export-behavior)
  link: [automatically exports file data and metadata](../facts/fsx.md#fsx-lustre-automatic-import-export-behavior)
fsx-lustre-aws-batch-and-parallelcluster-integration
  claim: FSx for Lustre integrates with AWS Batch using EC2 Launch Templates, and with AWS ParallelCluster, which can create FSx for Lustre file systems or use existing ones during cluster creation.
  scope: FSx for Lustre integrations.
  link: [integrates with AWS Batch](../facts/fsx.md#fsx-lustre-aws-batch-and-parallelcluster-integration)
  link: [AWS ParallelCluster](../facts/fsx.md#fsx-lustre-aws-batch-and-parallelcluster-integration)
fsx-lustre-backup-default-retention-zero
  claim: The default retention period for automatic daily backups of an FSx for Lustre file system is 0 days.
  scope: per FSx for Lustre file system; default; adjustable.
  link: [0 days](../facts/fsx.md#fsx-lustre-backup-default-retention-zero)
fsx-lustre-backup-retention-range
  claim: You can set the automatic daily backup retention period of an FSx for Lustre file system to be between 0–90 days.
  scope: per FSx for Lustre file system; maximum; adjustable.
  link: [0–90 days](../facts/fsx.md#fsx-lustre-backup-retention-range)
fsx-lustre-backups-incremental-stored-in-s3-11-nines
  claim: FSx for Lustre backups are file-system-consistent, highly durable and incremental, and Amazon FSx stores them in Amazon S3 with 99.999999999% (11 9's) durability.
  scope: FSx for Lustre backups.
  link: [file-system-consistent, highly durable, and incremental](../facts/fsx.md#fsx-lustre-backups-incremental-stored-in-s3-11-nines)
  link: [99.999999999% (11 9's) durability](../facts/fsx.md#fsx-lustre-backups-incremental-stored-in-s3-11-nines)
fsx-lustre-backups-persistent-only-not-s3-linked-not-scratch
  claim: Backups are supported only on FSx for Lustre persistent file systems that are not linked to an Amazon S3 data repository; scratch file systems and S3-linked file systems do not support backups.
  scope: FSx for Lustre backups.
  link: [supported only on FSx for Lustre persistent](../facts/fsx.md#fsx-lustre-backups-persistent-only-not-s3-linked-not-scratch)
  link: [not linked to an Amazon S3 data repository](../facts/fsx.md#fsx-lustre-backups-persistent-only-not-s3-linked-not-scratch)
fsx-lustre-client-throughput-efa
  claim: The maximum throughput per client for an EFA-enabled FSx for Lustre file system with an EFA client network interface is 700 Gbps.
  scope: per client, EFA-enabled file system, EFA interface; maximum; not adjustable.
  link: [700 Gbps](../facts/fsx.md#fsx-lustre-client-throughput-efa)
fsx-lustre-client-throughput-efa-gds
  claim: The maximum throughput per client for an EFA-enabled FSx for Lustre file system with the client network interface EFA with GDS is 1200 Gbps.
  scope: per client, EFA-enabled file system, EFA with GDS; maximum; not adjustable.
  link: [1200 Gbps](../facts/fsx.md#fsx-lustre-client-throughput-efa-gds)
fsx-lustre-client-throughput-non-efa
  claim: The maximum throughput per client for a non EFA-enabled FSx for Lustre file system, with any client network interface, is 100 Gbps; traffic between an individual client instance and an individual FSx for Lustre object storage server is limited to 5 Gbps.
  scope: per client, non EFA-enabled file system; maximum; not adjustable.
  link: [100 Gbps](../facts/fsx.md#fsx-lustre-client-throughput-non-efa)
fsx-lustre-clients-ec2-ecs-eks-linux-amis-lustre-client
  claim: FSx for Lustre file systems are accessible from Amazon EC2 instances, Amazon ECS Docker containers and containers on Amazon EKS, and FSx for Lustre is compatible with popular Linux-based AMIs.
  scope: Amazon FSx for Lustre clients.
  link: [Amazon EC2](../facts/fsx.md#fsx-lustre-clients-ec2-ecs-eks-linux-amis-lustre-client)
  link: [Linux-based AMIs](../facts/fsx.md#fsx-lustre-clients-ec2-ecs-eks-linux-amis-lustre-client)
  link: [Amazon Elastic Kubernetes Service (Amazon EKS)](../facts/fsx.md#fsx-lustre-clients-ec2-ecs-eks-linux-amis-lustre-client)
fsx-lustre-conflicting-writes-not-prevented
  claim: If you modify the same file in both the file system and the S3 bucket you should coordinate at the application level, because FSx for Lustre doesn't prevent conflicting writes in multiple locations.
  scope: FSx for Lustre data repository association.
  link: [application-level coordination](../facts/fsx.md#fsx-lustre-conflicting-writes-not-prevented)
  link: [doesn't prevent conflicting writes](../facts/fsx.md#fsx-lustre-conflicting-writes-not-prevented)
fsx-lustre-dra-links-directory-to-bucket-or-prefix
  claim: A link between a directory on the FSx for Lustre file system and an S3 bucket or prefix is called a data repository association (DRA), and you can create it when creating the file system or at any time afterwards.
  scope: FSx for Lustre S3 data repository.
  link: [data repository association (DRA)](../facts/fsx.md#fsx-lustre-dra-links-directory-to-bucket-or-prefix)
  link: [or at any time after](../facts/fsx.md#fsx-lustre-dra-links-directory-to-bucket-or-prefix)
fsx-lustre-dra-up-to-8-each-unique-directory-and-prefix
  claim: You can configure a maximum of 8 data repository associations on an FSx for Lustre file system, and each one must have a unique file system directory and a unique S3 bucket or prefix.
  scope: per FSx for Lustre file system; maximum; not adjustable.
  link: [maximum of 8 data repository associations](../facts/fsx.md#fsx-lustre-dra-up-to-8-each-unique-directory-and-prefix)
  link: [unique S3 bucket or prefix](../facts/fsx.md#fsx-lustre-dra-up-to-8-each-unique-directory-and-prefix)
fsx-lustre-ec2-client-open-source-lustre-client-other-azs
  claim: You access an FSx for Lustre file system from EC2 instances using the open-source Lustre client, and instances in other Availability Zones of the same VPC can access it if the networking allows access across subnets.
  scope: Amazon FSx for Lustre clients.
  link: [open-source Lustre client](../facts/fsx.md#fsx-lustre-ec2-client-open-source-lustre-client-other-azs)
  link: [from other Availability Zones within the same](../facts/fsx.md#fsx-lustre-ec2-client-open-source-lustre-client-other-azs)
fsx-lustre-efa-recommended-over-10-gbps
  claim: If you are creating an FSx for Lustre file system with over 10 GBps of throughput capacity, AWS recommends enabling Elastic Fabric Adapter (EFA) to optimize throughput per client instance.
  scope: per FSx for Lustre file system.
  link: [over 10 GBps](../facts/fsx.md#fsx-lustre-efa-recommended-over-10-gbps)
fsx-lustre-encryption-at-rest-automatic-kms-in-transit-supported-instances
  claim: Amazon FSx automatically encrypts FSx for Lustre file system data at rest using keys managed in AWS KMS, and data in transit is automatically encrypted in certain AWS Regions when accessed from supported EC2 instances.
  scope: FSx for Lustre encryption.
  link: [automatically encrypts file system data at rest](../facts/fsx.md#fsx-lustre-encryption-at-rest-automatic-kms-in-transit-supported-instances)
  link: [in certain AWS Regions when accessed from supported](../facts/fsx.md#fsx-lustre-encryption-at-rest-automatic-kms-in-transit-supported-instances)
fsx-lustre-hdd-single-digit-ms-latency
  claim: The FSx for Lustre HDD storage class can be used with workloads that need consistent single-digit ms latency across all data.
  scope: FSx for Lustre HDD storage class.
  link: [single-digit ms](../facts/fsx.md#fsx-lustre-hdd-single-digit-ms-latency)
fsx-lustre-hdd-ssd-read-cache-20-percent
  claim: You can provision an optional SSD read cache that is sized to 20% of your HDD storage capacity to provide low-latency access to frequently-accessed data.
  scope: FSx for Lustre HDD storage class; fixed.
  link: [20% of your HDD storage capacity](../facts/fsx.md#fsx-lustre-hdd-ssd-read-cache-20-percent)
fsx-lustre-import-same-region-export-standard-class
  claim: To automatically import updates, the FSx for Lustre file system and the linked S3 bucket must be in the same AWS Region, and S3 objects created by automatic export use the S3 Standard storage class.
  scope: FSx for Lustre data repository association.
  link: [must be located in the same AWS Region](../facts/fsx.md#fsx-lustre-import-same-region-export-standard-class)
  link: [written using the S3 Standard storage class](../facts/fsx.md#fsx-lustre-import-same-region-export-standard-class)
fsx-lustre-intelligent-tiering-elastic-pay-for-data-stored
  claim: The FSx for Lustre Intelligent-Tiering storage class provides fully elastic, intelligently tiered storage; you pay for the amount of data you store and do not have to specify a file system size.
  scope: FSx for Lustre storage classes.
  link: [fully elastic, intelligently tiered storage](../facts/fsx.md#fsx-lustre-intelligent-tiering-elastic-pay-for-data-stored)
  link: [do not have to specify](../facts/fsx.md#fsx-lustre-intelligent-tiering-elastic-pay-for-data-stored)
fsx-lustre-intelligent-tiering-latency-tens-of-ms-vs-cache-sub-ms
  claim: Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds and per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [roughly tens of milliseconds](../facts/fsx.md#fsx-lustre-intelligent-tiering-latency-tens-of-ms-vs-cache-sub-ms)
  link: [sub-millisecond latency and no per-request costs](../facts/fsx.md#fsx-lustre-intelligent-tiering-latency-tens-of-ms-vs-cache-sub-ms)
fsx-lustre-intelligent-tiering-no-extra-retrieval-or-transition-cost
  claim: In the Intelligent-Tiering storage class all access to non-cached data has the same performance regardless of tier, and there are no additional IOPS, retrieval or transition costs beyond normal read and write costs.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [no additional IOPS, retrieval, or transition costs](../facts/fsx.md#fsx-lustre-intelligent-tiering-no-extra-retrieval-or-transition-cost)
  link: [independent of the data's tier](../facts/fsx.md#fsx-lustre-intelligent-tiering-no-extra-retrieval-or-transition-cost)
fsx-lustre-intelligent-tiering-no-s3-data-repository-link
  claim: Intelligent-Tiering FSx for Lustre file systems don't support linking to Amazon S3 data repositories.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [don't support linking to Amazon S3 data repositories](../facts/fsx.md#fsx-lustre-intelligent-tiering-no-s3-data-repository-link)
  link: [Intelligent-Tiering file systems](../facts/fsx.md#fsx-lustre-intelligent-tiering-no-s3-data-repository-link)
fsx-lustre-intelligent-tiering-recommended-most-workloads-cache-friendly
  claim: The Intelligent-Tiering storage class is suitable and recommended for most FSx for Lustre workloads that do not need consistent low latency across the full dataset; the storage class provides the best balance of price and performance for most workloads.
  scope: FSx for Lustre storage classes.
  link: [suitable and recommended for most workloads](../facts/fsx.md#fsx-lustre-intelligent-tiering-recommended-most-workloads-cache-friendly)
  link: [best balance of price and performance](../facts/fsx.md#fsx-lustre-intelligent-tiering-recommended-most-workloads-cache-friendly)
fsx-lustre-intelligent-tiering-ssd-read-cache-savings-vs-ssd-hdd
  claim: With the optional SSD read cache, Intelligent-Tiering file systems can perform at levels comparable to SSD file systems for most workloads while delivering storage cost savings relative to the SSD and HDD storage classes.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [comparable to SSD file systems](../facts/fsx.md#fsx-lustre-intelligent-tiering-ssd-read-cache-savings-vs-ssd-hdd)
  link: [storage cost savings relative to](../facts/fsx.md#fsx-lustre-intelligent-tiering-ssd-read-cache-savings-vs-ssd-hdd)
fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days
  claim: The Intelligent-Tiering storage class moves data to the Infrequent Access tier after 30 consecutive days without access and to the Archive Instant Access tier after 90 consecutive days, and moves data back to the Frequent Access tier when it is accessed.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [30 consecutive days](../facts/fsx.md#fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days)
  link: [90 consecutive days](../facts/fsx.md#fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days)
  link: [automatically moves back to the Frequent Access tier](../facts/fsx.md#fsx-lustre-intelligent-tiering-three-tiers-30-and-90-days)
fsx-lustre-intelligent-tiering-throughput-increments
  claim: Intelligent-Tiering file systems support throughput capacities in increments of 4000 MBps.
  scope: per Intelligent-Tiering file system; fixed; not adjustable.
  link: [4000 MBps](../facts/fsx.md#fsx-lustre-intelligent-tiering-throughput-increments)
fsx-lustre-it-archive-instant-access-90-days
  claim: In the FSx for Lustre Intelligent-Tiering storage class, data that hasn’t been accessed in 90 consecutive days automatically moves to the Archive Instant Access tier, which costs less than the Infrequent Access tier.
  scope: FSx for Lustre Intelligent-Tiering storage class; fixed; not adjustable.
  link: [90 consecutive days](../facts/fsx.md#fsx-lustre-it-archive-instant-access-90-days)
fsx-lustre-it-frequent-access-30-days
  claim: In the FSx for Lustre Intelligent-Tiering storage class, data accessed in the last 30 days is stored in the Frequent Access tier.
  scope: FSx for Lustre Intelligent-Tiering storage class; fixed; not adjustable.
  link: [last 30 days](../facts/fsx.md#fsx-lustre-it-frequent-access-30-days)
fsx-lustre-it-infrequent-access-30-days
  claim: In the FSx for Lustre Intelligent-Tiering storage class, data that hasn’t been accessed in 30 consecutive days automatically moves to the Infrequent Access tier, which costs less than the Frequent Access tier.
  scope: FSx for Lustre Intelligent-Tiering storage class; fixed; not adjustable.
  link: [30 consecutive days](../facts/fsx.md#fsx-lustre-it-infrequent-access-30-days)
fsx-lustre-it-max-storage-per-oss
  claim: Amazon FSx for Lustre Intelligent-Tiering file systems support a maximum of 512 TiB of storage per OSS.
  scope: per object storage server (OSS), Intelligent-Tiering; maximum; not adjustable.
  link: [512 TiB](../facts/fsx.md#fsx-lustre-it-max-storage-per-oss)
fsx-lustre-lazy-loaded-from-s3-as-needed
  claim: When FSx for Lustre is an input data source for Amazon SageMaker, SageMaker jobs start as soon as the file system is linked with the S3 bucket, and data is lazy loaded as needed from Amazon S3 for processing jobs.
  scope: FSx for Lustre S3 data repository.
  link: [lazy loaded as needed from Amazon S3](../facts/fsx.md#fsx-lustre-lazy-loaded-from-s3-as-needed)
  link: [Data is lazy loaded](../facts/fsx.md#fsx-lustre-lazy-loaded-from-s3-as-needed)
fsx-lustre-limit-automated-backup-retention
  claim: The maximum retention period for automated backups of an FSx for Lustre file system is 90 days.
  scope: per file system; maximum; not adjustable.
  link: [90 days](../facts/fsx.md#fsx-lustre-limit-automated-backup-retention)
fsx-lustre-limit-backup-copies-in-progress
  claim: The maximum number of backup copy requests in progress to a single destination Region per account is 5.
  scope: per account, per destination Region; maximum; not adjustable.
  link: [5](../facts/fsx.md#fsx-lustre-limit-backup-copies-in-progress)
fsx-lustre-limit-max-capacity-persistent-1-hdd
  claim: The maximum storage capacity of an FSx for Lustre Persistent_1 HDD file system is 1,002,000 GiB.
  scope: per Persistent_1 HDD file system; maximum; not adjustable.
  link: [1,002,000 GiB](../facts/fsx.md#fsx-lustre-limit-max-capacity-persistent-1-hdd)
fsx-lustre-limit-max-capacity-persistent-1-ssd
  claim: The maximum storage capacity of an FSx for Lustre Persistent_1 SSD file system is 604,800 GiB.
  scope: per Persistent_1 SSD file system; maximum; not adjustable.
  link: [604,800 GiB](../facts/fsx.md#fsx-lustre-limit-max-capacity-persistent-1-ssd)
fsx-lustre-limit-max-capacity-persistent-2
  claim: The maximum storage capacity of an FSx for Lustre Persistent_2 file system is 1,200,000 GiB.
  scope: per Persistent_2 file system; maximum; not adjustable.
  link: [1,200,000 GiB](../facts/fsx.md#fsx-lustre-limit-max-capacity-persistent-2)
fsx-lustre-limit-max-throughput-per-unit-hdd
  claim: The maximum throughput per unit of storage for FSx for Lustre HDD is 40 MBps.
  scope: per unit of storage, HDD; maximum; not adjustable.
  link: [40 MBps](../facts/fsx.md#fsx-lustre-limit-max-throughput-per-unit-hdd)
fsx-lustre-limit-max-throughput-per-unit-ssd
  claim: The maximum throughput per unit of storage for FSx for Lustre SSD is 1000 MBps.
  scope: per unit of storage, SSD; maximum; not adjustable.
  link: [1000 MBps](../facts/fsx.md#fsx-lustre-limit-max-throughput-per-unit-ssd)
fsx-lustre-limit-min-hdd-capacity
  claim: The minimum storage capacity of an FSx for Lustre HDD file system is 6,000 GiB.
  scope: per HDD file system; minimum; not adjustable.
  link: [6,000 GiB](../facts/fsx.md#fsx-lustre-limit-min-hdd-capacity)
fsx-lustre-limit-min-ssd-capacity
  claim: The minimum storage capacity of an FSx for Lustre SSD file system is 1,200 GiB.
  scope: per SSD file system; minimum; not adjustable.
  link: [1,200 GiB](../facts/fsx.md#fsx-lustre-limit-min-ssd-capacity)
fsx-lustre-limit-min-throughput-per-unit-hdd
  claim: The minimum throughput per unit of storage for FSx for Lustre HDD is 12 MBps.
  scope: per unit of storage, HDD; minimum; not adjustable.
  link: [12 MBps](../facts/fsx.md#fsx-lustre-limit-min-throughput-per-unit-hdd)
fsx-lustre-limit-min-throughput-per-unit-ssd
  claim: The minimum throughput per unit of storage for FSx for Lustre SSD is 50 MBps.
  scope: per unit of storage, SSD; minimum; not adjustable.
  link: [50 MBps](../facts/fsx.md#fsx-lustre-limit-min-throughput-per-unit-ssd)
fsx-lustre-limit-s3-file-updates-per-month
  claim: The number of file updates from a linked S3 bucket per FSx for Lustre file system is 10 million per month.
  scope: per file system, per month; maximum; not adjustable.
  link: [10 million / month](../facts/fsx.md#fsx-lustre-limit-s3-file-updates-per-month)
fsx-lustre-limit-tags-per-file-system
  claim: The maximum number of tags per FSx for Lustre file system is 50.
  scope: per file system; maximum; not adjustable.
  link: [50](../facts/fsx.md#fsx-lustre-limit-tags-per-file-system)
fsx-lustre-on-premises-and-peered-vpc-access
  claim: You can access an FSx for Lustre file system from EC2 instances in a peered VPC, or from on-premises clients connected to the file system's VPC with Direct Connect or VPN.
  scope: Amazon FSx for Lustre clients.
  link: [peered to the file system's VPC](../facts/fsx.md#fsx-lustre-on-premises-and-peered-vpc-access)
  link: [using Direct Connect or VPN](../facts/fsx.md#fsx-lustre-on-premises-and-peered-vpc-access)
fsx-lustre-persistent-1-hdd-throughput-per-tib
  claim: For a Persistent 1 file system with HDD storage, the throughput per unit of storage is either 12 or 40 MBps per TiB.
  scope: per TiB of storage, Persistent 1 HDD; fixed; not adjustable.
  link: [12 or 40 MBps per TiB](../facts/fsx.md#fsx-lustre-persistent-1-hdd-throughput-per-tib)
fsx-lustre-persistent-1-ssd-throughput-per-tib
  claim: For a Persistent 1 file system with SSD storage, the throughput per unit of storage is either 50, 100, or 200 MBps per TiB.
  scope: per TiB of storage, Persistent 1 SSD; fixed; not adjustable.
  link: [50, 100, or 200 MBps per TiB](../facts/fsx.md#fsx-lustre-persistent-1-ssd-throughput-per-tib)
fsx-lustre-persistent-2-latest-generation-persistent-1-ssd-hdd
  claim: Persistent 2 is the latest generation of FSx for Lustre persistent deployment type and supports SSD and Intelligent-Tiering storage classes, while Persistent 1 supports SSD and HDD storage classes.
  scope: FSx for Lustre deployment types.
  link: [latest generation of Persistent deployment type](../facts/fsx.md#fsx-lustre-persistent-2-latest-generation-persistent-1-ssd-hdd)
  link: [support SSD and Intelligent-Tiering storage classes](../facts/fsx.md#fsx-lustre-persistent-2-latest-generation-persistent-1-ssd-hdd)
  link: [SSD (solid state drive) and HDD](../facts/fsx.md#fsx-lustre-persistent-2-latest-generation-persistent-1-ssd-hdd)
fsx-lustre-persistent-2-ssd-throughput-per-tib
  claim: Persistent 2 file systems with SSD storage support throughput per unit of storage of 250, 500, or 1000 MBps per TiB, higher than Persistent 1 file systems.
  scope: per TiB of storage, Persistent 2 SSD; fixed; not adjustable.
  link: [250, 500, or 1000 MBps per TiB](../facts/fsx.md#fsx-lustre-persistent-2-ssd-throughput-per-tib)
fsx-lustre-persistent-encrypts-in-transit-automatically
  claim: Persistent FSx for Lustre deployment types automatically encrypt data in transit when they are accessed from Amazon EC2 instances that support encryption in transit.
  scope: FSx for Lustre persistent file systems.
  link: [automatically encrypt data in transit](../facts/fsx.md#fsx-lustre-persistent-encrypts-in-transit-automatically)
  link: [instances that support encryption in transit](../facts/fsx.md#fsx-lustre-persistent-encrypts-in-transit-automatically)
fsx-lustre-persistent-failed-server-replaced-within-minutes-clients-retry
  claim: On a persistent FSx for Lustre file system, an unavailable file server is replaced automatically within minutes of failure, and client requests to that server transparently retry and eventually succeed.
  scope: FSx for Lustre persistent file systems.
  link: [replaced automatically within minutes of failure](../facts/fsx.md#fsx-lustre-persistent-failed-server-replaced-within-minutes-clients-retry)
  link: [transparently retry and eventually succeed](../facts/fsx.md#fsx-lustre-persistent-failed-server-replaced-within-minutes-clients-retry)
fsx-lustre-persistent-replicated-servers-replaced
  claim: Persistent FSx for Lustre file systems are for longer-term storage and throughput-focused workloads; data is replicated and file servers are replaced if they fail.
  scope: FSx for Lustre persistent file systems.
  link: [data is replicated](../facts/fsx.md#fsx-lustre-persistent-replicated-servers-replaced)
  link: [file servers are replaced if they fail](../facts/fsx.md#fsx-lustre-persistent-replicated-servers-replaced)
fsx-lustre-persistent-ssd-hdd-replicated-within-az-intelligent-tiering-multi-az
  claim: On persistent FSx for Lustre file systems, SSD and HDD data is replicated within the same Availability Zone, while Intelligent-Tiering data is replicated across multiple Availability Zones.
  scope: FSx for Lustre persistent file systems.
  link: [replicated within the same Availability Zone](../facts/fsx.md#fsx-lustre-persistent-ssd-hdd-replicated-within-az-intelligent-tiering-multi-az)
  link: [replicated across multiple Availability Zones](../facts/fsx.md#fsx-lustre-persistent-ssd-hdd-replicated-within-az-intelligent-tiering-multi-az)
fsx-lustre-posix-compliant-read-after-write-locking
  claim: FSx for Lustre is POSIX-compliant, so current Linux-based applications work without changes, and it provides read-after-write consistency and supports file locking.
  scope: Amazon FSx for Lustre.
  link: [FSx for Lustre is POSIX-compliant](../facts/fsx.md#fsx-lustre-posix-compliant-read-after-write-locking)
  link: [read-after-write consistency](../facts/fsx.md#fsx-lustre-posix-compliant-read-after-write-locking)
  link: [supports file locking](../facts/fsx.md#fsx-lustre-posix-compliant-read-after-write-locking)
fsx-lustre-pricing-cross-az-access-rate
  claim: For FSx for Lustre, accessing data from an AZ other than the file system's preferred AZ in the same Region is charged at $0.01/GB in each direction.
  scope: per GB in each direction, access from a non-preferred AZ in the same Region.
  link: [$0.01/GB](../facts/fsx.md#fsx-lustre-pricing-cross-az-access-rate)
fsx-lustre-pricing-intelligent-tiering-dimensions
  claim: For FSx for Lustre Intelligent-Tiering you pay for the average storage consumed in each access tier, an optional SSD read cache, data access (read and write requests) and provisioned throughput capacity, plus monitoring and automation.
  scope: FSx for Lustre Intelligent-Tiering storage class.
  link: [average amount of storage consumed per access tier](../facts/fsx.md#fsx-lustre-pricing-intelligent-tiering-dimensions)
fsx-lustre-pricing-metadata-iops-included-ssd-hdd
  claim: With the FSx for Lustre SSD or HDD storage class, a default number of metadata IOPS are included with each file system based on the storage capacity provisioned, and you pay for provisioned IOPS above that default level.
  scope: FSx for Lustre SSD or HDD storage class.
  link: [default number of metadata IOPS are included](../facts/fsx.md#fsx-lustre-pricing-metadata-iops-included-ssd-hdd)
fsx-lustre-pricing-prorated-by-second
  claim: For FSx for Lustre, pricing is quoted on a monthly basis, usage is prorated by the second, and you are billed for your average usage over a month.
  scope: FSx for Lustre.
  link: [prorated by the second](../facts/fsx.md#fsx-lustre-pricing-prorated-by-second)
fsx-lustre-quota-backups-per-account
  claim: The default for Lustre backups is 500, the maximum number of user-initiated backups that you can have for all Amazon FSx for Lustre file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [500](../facts/fsx.md#fsx-lustre-quota-backups-per-account)
fsx-lustre-quota-intelligent-tiering-ssd-read-cache-per-account
  claim: The default for Lustre Persistent Intelligent-Tiering SSD read cache storage capacity is 100800, the maximum amount of provisioned SSD read cache storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Intelligent-Tiering file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100800](../facts/fsx.md#fsx-lustre-quota-intelligent-tiering-ssd-read-cache-per-account)
fsx-lustre-quota-intelligent-tiering-throughput-per-account
  claim: The default for Lustre Persistent Intelligent-Tiering throughput capacity is 100000, the total amount of throughput capacity (in MBps) allowed for all Amazon FSx for Lustre Intelligent-Tiering file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100000](../facts/fsx.md#fsx-lustre-quota-intelligent-tiering-throughput-per-account)
fsx-lustre-quota-persistent-1-capacity-per-account
  claim: The default for Lustre Persistent 1 file storage capacity is 100800, the maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Persistent 1 file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100800](../facts/fsx.md#fsx-lustre-quota-persistent-1-capacity-per-account)
fsx-lustre-quota-persistent-1-file-systems
  claim: The default for Lustre Persistent 1 file systems is 100, the maximum number of Amazon FSx for Lustre Persistent 1 file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-lustre-quota-persistent-1-file-systems)
fsx-lustre-quota-persistent-2-capacity-per-account
  claim: The default for Lustre Persistent 2 file storage capacity is 100800, the maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Persistent 2 file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100800](../facts/fsx.md#fsx-lustre-quota-persistent-2-capacity-per-account)
fsx-lustre-quota-persistent-2-file-systems
  claim: The default for Lustre Persistent 2 file systems is 100, the maximum number of Amazon FSx for Lustre Persistent 2 file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-lustre-quota-persistent-2-file-systems)
fsx-lustre-quota-persistent-hdd-capacity-per-file-system
  claim: The default for Lustre Persistent HDD storage capacity (per file system) is 102000, the maximum amount of HDD storage capacity (in GiB) that you can configure for an Amazon FSx for Lustre persistent file system.
  scope: per file system, per AWS Region; default; adjustable.
  link: [102000](../facts/fsx.md#fsx-lustre-quota-persistent-hdd-capacity-per-file-system)
fsx-lustre-quota-scratch-capacity-per-account
  claim: The default for Lustre Scratch storage capacity is 100800, the maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre scratch file systems in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100800](../facts/fsx.md#fsx-lustre-quota-scratch-capacity-per-account)
fsx-lustre-quota-scratch-file-systems
  claim: The default for Lustre Scratch file systems is 100, the maximum number of Amazon FSx for Lustre scratch file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-lustre-quota-scratch-file-systems)
fsx-lustre-release-frees-space-keeps-metadata-reloads-from-s3
  claim: A release data repository task frees file system space by removing the local copy of a file's contents while keeping its listing and metadata, and the content is automatically and transparently loaded back from the linked S3 bucket when the file is accessed.
  scope: FSx for Lustre data repository tasks.
  link: [retains the file listing and metadata](../facts/fsx.md#fsx-lustre-release-frees-space-keeps-metadata-reloads-from-s3)
  link: [removes the local copy of that file's contents](../facts/fsx.md#fsx-lustre-release-frees-space-keeps-metadata-reloads-from-s3)
fsx-lustre-release-task-frees-space-needs-task
  claim: For FSx for Lustre, a release data repository task frees file system space by releasing files already exported to Amazon S3. The released file content is removed but its metadata stays, and reading the file again retrieves it from S3.
  scope: FSx for Lustre linked to an S3 data repository.
  link: [release data repository task](../facts/fsx.md#fsx-lustre-release-task-frees-space-needs-task)
  link: [transparently retrieves the file content from Amazon S3](../facts/fsx.md#fsx-lustre-release-task-frees-space-needs-task)
fsx-lustre-s3-presents-objects-as-files-and-writes-back
  claim: When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files, imports listings of existing files at file system creation, and can write file system data back to S3.
  scope: FSx for Lustre S3 data repository.
  link: [transparently presents S3 objects as files](../facts/fsx.md#fsx-lustre-s3-presents-objects-as-files-and-writes-back)
  link: [write file system data back to S3](../facts/fsx.md#fsx-lustre-s3-presents-objects-as-files-and-writes-back)
fsx-lustre-sagemaker-input-source-skips-s3-download
  claim: Amazon FSx for Lustre integrates with Amazon SageMaker AI as an input data source, which accelerates training jobs by eliminating the initial download step from Amazon S3.
  scope: FSx for Lustre integrations.
  link: [input data source](../facts/fsx.md#fsx-lustre-sagemaker-input-source-skips-s3-download)
  link: [eliminating the initial download step from Amazon S3](../facts/fsx.md#fsx-lustre-sagemaker-input-source-skips-s3-download)
fsx-lustre-scratch-burst-six-times-200
  claim: Scratch file systems provide high burst throughput of up to six times the baseline throughput of 200 MBps per TiB of storage capacity.
  scope: FSx for Lustre scratch file systems, per TiB of storage capacity; maximum.
  link: [six times](../facts/fsx.md#fsx-lustre-scratch-burst-six-times-200)
  link: [200 MBps per TiB](../facts/fsx.md#fsx-lustre-scratch-burst-six-times-200)
fsx-lustre-scratch-server-failure-io-error-no-replacement
  claim: On a scratch FSx for Lustre file system, file servers are not replaced if they fail and data is not replicated; files on other servers stay accessible, but clients that access data on the failed server or disk get an immediate I/O error.
  scope: FSx for Lustre scratch file systems.
  link: [file servers aren't replaced if they fail](../facts/fsx.md#fsx-lustre-scratch-server-failure-io-error-no-replacement)
  link: [immediate I/O error](../facts/fsx.md#fsx-lustre-scratch-server-failure-io-error-no-replacement)
fsx-lustre-scratch-ssd-throughput-per-tib
  claim: For a Scratch file system with SSD storage, the throughput per unit of storage is 200 MBps per TiB.
  scope: per TiB of storage, Scratch SSD; fixed; not adjustable.
  link: [200 MBps per TiB](../facts/fsx.md#fsx-lustre-scratch-ssd-throughput-per-tib)
fsx-lustre-scratch-temporary-not-replicated
  claim: Scratch FSx for Lustre file systems are for temporary storage and shorter-term processing; data is not replicated and does not persist if a file server fails.
  scope: FSx for Lustre scratch file systems.
  link: [Data is not replicated](../facts/fsx.md#fsx-lustre-scratch-temporary-not-replicated)
  link: [does not persist if a file server fails](../facts/fsx.md#fsx-lustre-scratch-temporary-not-replicated)
fsx-lustre-spot-instances-unmount-before-interruption
  claim: To keep FSx for Lustre file systems unaffected by EC2 Spot Instance interruptions, AWS recommends unmounting the file system before terminating or hibernating Spot Instances.
  scope: FSx for Lustre with Spot Instances.
  link: [can be used with EC2 Spot Instances](../facts/fsx.md#fsx-lustre-spot-instances-unmount-before-interruption)
  link: [unmounting Amazon FSx file systems](../facts/fsx.md#fsx-lustre-spot-instances-unmount-before-interruption)
fsx-lustre-ssd-class-sub-millisecond-full-dataset
  claim: The SSD storage class of FSx for Lustre provides low-latency (sub-millisecond) access to your full dataset, and you pay for the amount of storage you provision.
  scope: FSx for Lustre storage classes.
  link: [low-latency (sub-millisecond) access to your full dataset](../facts/fsx.md#fsx-lustre-ssd-class-sub-millisecond-full-dataset)
  link: [SSD storage class is provisioned](../facts/fsx.md#fsx-lustre-ssd-class-sub-millisecond-full-dataset)
fsx-lustre-storage-increase-only
  claim: You can only increase the amount of storage capacity for an FSx for Lustre file system; you cannot decrease storage capacity.
  scope: per FSx for Lustre file system.
  link: [cannot decrease storage capacity](../facts/fsx.md#fsx-lustre-storage-increase-only)
fsx-lustre-storage-increase-wait-6-hours
  claim: You can't make further storage capacity increases on an FSx for Lustre file system until 6 hours after the last increase was requested.
  scope: per FSx for Lustre file system; minimum.
  link: [6 hours](../facts/fsx.md#fsx-lustre-storage-increase-wait-6-hours)
fsx-lustre-three-data-repository-task-types
  claim: FSx for Lustre has three types of data repository tasks: export tasks copy from the file system to the linked S3 bucket, import tasks copy from the bucket to the file system, and release tasks release files that were exported to the bucket.
  scope: FSx for Lustre.
  link: [three types of data repository tasks](../facts/fsx.md#fsx-lustre-three-data-repository-task-types)
fsx-lustre-use-scratch-for-short-term-persistent-for-long-term
  claim: Use scratch FSx for Lustre file systems when you need cost-optimized storage for short-term, processing-heavy workloads, and persistent file systems for longer-term storage and for throughput-focused workloads that run for extended periods or indefinitely and that might be sensitive to disruptions in availability.
  scope: FSx for Lustre deployment types.
  link: [cost-optimized storage for short-term, processing-heavy workloads](../facts/fsx.md#fsx-lustre-use-scratch-for-short-term-persistent-for-long-term)
  link: [sensitive to disruptions in availability](../facts/fsx.md#fsx-lustre-use-scratch-for-short-term-persistent-for-long-term)
fsx-lustre-workloads-ml-hpc-video-financial
  claim: FSx for Lustre runs the high-performance Lustre file system for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing and financial modeling.
  scope: Amazon FSx for Lustre.
  link: [machine learning, high performance computing (HPC)](../facts/fsx.md#fsx-lustre-workloads-ml-hpc-video-financial)
  link: [video processing, and financial modeling](../facts/fsx.md#fsx-lustre-workloads-ml-hpc-video-financial)
fsx-ontap-arp-ai-driven-detects-ransomware-creates-snapshot
  claim: Autonomous Ransomware Protection (ARP) is an AI-driven NetApp ONTAP feature that monitors and protects data against ransomware and malware if your Windows or Linux clients become compromised, and when it detects abnormal activity it automatically creates an ONTAP snapshot.
  scope: FSx for ONTAP Autonomous Ransomware Protection.
  link: [monitors and protects your data against ransomware](../facts/fsx.md#fsx-ontap-arp-ai-driven-detects-ransomware-creates-snapshot)
  link: [an ONTAP snapshot is automatically created](../facts/fsx.md#fsx-ontap-arp-ai-driven-detects-ransomware-creates-snapshot)
fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost
  claim: ARP looks for changes in data entropy, changes in file extension types and surges in abnormal volume activity with encrypted data, and there is no additional cost for enabling ARP on an FSx for ONTAP file system.
  scope: FSx for ONTAP Autonomous Ransomware Protection.
  link: [Changes in entropy](../facts/fsx.md#fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost)
  link: [Changes in file IOPS](../facts/fsx.md#fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost)
  link: [no additional cost for enabling ARP](../facts/fsx.md#fsx-ontap-arp-detects-entropy-extension-iops-no-extra-cost)
fsx-ontap-arp-not-a-defense-against-rogue-administrators
  claim: ARP doesn't prevent rogue administrators with credentials from accessing an FSx for ONTAP file system, so AWS recommends a layered approach with AWS Backup, ONTAP snapshots and SnapLock.
  scope: FSx for ONTAP Autonomous Ransomware Protection.
  link: [doesn't prevent rogue administrators](../facts/fsx.md#fsx-ontap-arp-not-a-defense-against-rogue-administrators)
  link: [layered security approach](../facts/fsx.md#fsx-ontap-arp-not-a-defense-against-rogue-administrators)
fsx-ontap-automatic-backup-retention-console-30-days-default-1-to-90
  claim: In the console you can set the automatic daily backup retention period of an FSx for ONTAP file system from 1 to 90 days, and the default is 30 days.
  scope: FSx for ONTAP automatic daily backups; default; adjustable.
  link: [default automatic daily backup retention period is 30 days](../facts/fsx.md#fsx-ontap-automatic-backup-retention-console-30-days-default-1-to-90)
  link: [from 1 to 90 days](../facts/fsx.md#fsx-ontap-automatic-backup-retention-console-30-days-default-1-to-90)
fsx-ontap-aws-backup-uses-builtin-fsx-backup-functionality
  claim: AWS Backup uses the built-in backup functionality of Amazon FSx.
  scope: FSx for ONTAP backups.
  link: [built-in backup functionality of Amazon FSx](../facts/fsx.md#fsx-ontap-aws-backup-uses-builtin-fsx-backup-functionality)
  link: [AWS Backup uses](../facts/fsx.md#fsx-ontap-aws-backup-uses-builtin-fsx-backup-functionality)
fsx-ontap-backup-copy-cross-region-manual-and-aws-backup
  claim: Amazon FSx lets you manually copy FSx for ONTAP volume backups to another AWS Region or within the same Region, within the same AWS account, and you can use AWS Backup to copy backups across Regions and across accounts.
  scope: FSx for ONTAP backups.
  link: [another AWS Region (cross-Region copies)](../facts/fsx.md#fsx-ontap-backup-copy-cross-region-manual-and-aws-backup)
  link: [across AWS Regions and across AWS accounts](../facts/fsx.md#fsx-ontap-backup-copy-cross-region-manual-and-aws-backup)
fsx-ontap-backup-logically-air-gapped-vault-aws-backup
  claim: You can store FSx for ONTAP volume backups created by AWS Backup in a logically air-gapped vault, a specialized AWS Backup vault that is encrypted and protected by AWS Backup Vault Lock in compliance mode.
  scope: FSx for ONTAP backups.
  link: [logically air-gapped vault](../facts/fsx.md#fsx-ontap-backup-logically-air-gapped-vault-aws-backup)
  link: [AWS Backup Vault Lock in compliance mode](../facts/fsx.md#fsx-ontap-backup-logically-air-gapped-vault-aws-backup)
fsx-ontap-backups-automatic-daily-and-user-initiated-per-volume
  claim: FSx for ONTAP takes automatic daily backups, enabled by default for a file system's volumes, and user-initiated backups of volumes, and all backups are incremental.
  scope: FSx for ONTAP backups.
  link: [automatic daily backups and user-initiated backups](../facts/fsx.md#fsx-ontap-backups-automatic-daily-and-user-initiated-per-volume)
  link: [enabled by default for your file system's volumes](../facts/fsx.md#fsx-ontap-backups-automatic-daily-and-user-initiated-per-volume)
fsx-ontap-backups-not-for-dp-lsm-flexcache-snapmirror-destination-volumes
  claim: Amazon FSx doesn't support backing up data protection (DP) volumes, load sharing mirror (LSM) volumes, or destination volumes for FlexCache and SnapMirror.
  scope: FSx for ONTAP backups.
  link: [backing up data protection (DP) volumes](../facts/fsx.md#fsx-ontap-backups-not-for-dp-lsm-flexcache-snapmirror-destination-volumes)
  link: [destination volumes for FlexCache and SnapMirror](../facts/fsx.md#fsx-ontap-backups-not-for-dp-lsm-flexcache-snapmirror-destination-volumes)
fsx-ontap-block-storage-iscsi-luns-nvme-namespaces-san
  claim: Amazon FSx for NetApp ONTAP supports the iSCSI and NVMe over TCP (NVMe/TCP) block storage protocols; you configure storage by creating LUNs for iSCSI and namespaces for NVMe, and hosts access them using iSCSI or TCP protocols.
  scope: Amazon FSx for NetApp ONTAP block storage.
  link: [iSCSI) and Non-Volatile Memory Express (NVMe)](../facts/fsx.md#fsx-ontap-block-storage-iscsi-luns-nvme-namespaces-san)
  link: [creating LUNs for iSCSI](../facts/fsx.md#fsx-ontap-block-storage-iscsi-luns-nvme-namespaces-san)
  link: [creating namespaces for NVMe](../facts/fsx.md#fsx-ontap-block-storage-iscsi-luns-nvme-namespaces-san)
fsx-ontap-cooling-period-range
  claim: You can set the FSx for ONTAP tiering cooling period to a value in the range of 2–183 days.
  scope: per volume, Auto and Snapshot-only tiering policies; maximum; adjustable.
  link: [2–183 days](../facts/fsx.md#fsx-ontap-cooling-period-range)
fsx-ontap-default-mtu-9001
  claim: The default maximum transmission unit (MTU) setting for network interfaces on an FSx for ONTAP file system is 9,001 bytes.
  scope: per FSx for ONTAP file system network interface; default; not adjustable.
  link: [9,001 bytes](../facts/fsx.md#fsx-ontap-default-mtu-9001)
fsx-ontap-deployment-type-cannot-change-after-creation
  claim: You can't change an FSx for ONTAP file system's deployment type after creation; to change it you back up your data and restore it on a new file system, or migrate the data with SnapMirror, DataSync or another copy tool.
  scope: Amazon FSx for NetApp ONTAP.
  link: [can't change your file system's deployment type](../facts/fsx.md#fsx-ontap-deployment-type-cannot-change-after-creation)
  link: [restore it on a new file system](../facts/fsx.md#fsx-ontap-deployment-type-cannot-change-after-creation)
fsx-ontap-each-ha-pair-fails-over-independently
  claim: For second-generation FSx for ONTAP file systems with multiple HA pairs, each HA pair's failover behavior is independent.
  scope: Amazon FSx for NetApp ONTAP failover.
  link: [failover behavior is independent](../facts/fsx.md#fsx-ontap-each-ha-pair-fails-over-independently)
  link: [each HA pair's failover](../facts/fsx.md#fsx-ontap-each-ha-pair-fails-over-independently)
fsx-ontap-encrypted-at-rest-kms-file-systems-and-backups
  claim: All FSx for ONTAP file systems and backups are encrypted at rest with keys managed in AWS KMS, and data is encrypted and decrypted transparently.
  scope: Amazon FSx for NetApp ONTAP encryption.
  link: [encrypted at rest with keys managed](../facts/fsx.md#fsx-ontap-encrypted-at-rest-kms-file-systems-and-backups)
  link: [automatically decrypted as it is read](../facts/fsx.md#fsx-ontap-encrypted-at-rest-kms-file-systems-and-backups)
fsx-ontap-failover-conditions
  claim: FSx for ONTAP file systems automatically fail over an HA pair to the standby file server if the preferred or active server becomes unavailable or undergoes planned maintenance, or if an Availability Zone outage occurs (Multi-AZ only).
  scope: Amazon FSx for NetApp ONTAP failover.
  link: [becomes unavailable](../facts/fsx.md#fsx-ontap-failover-conditions)
  link: [undergoes planned maintenance](../facts/fsx.md#fsx-ontap-failover-conditions)
  link: [Multi-AZ file systems only](../facts/fsx.md#fsx-ontap-failover-conditions)
fsx-ontap-failover-failback-under-60-seconds
  claim: An FSx for ONTAP failover typically completes in less than 60 seconds from detection of the failure to promotion of the standby, and for Multi-AZ file systems failback to the recovered preferred file server is automatic and usually takes less than 60 seconds.
  scope: Amazon FSx for NetApp ONTAP failover.
  link: [less than 60 seconds](../facts/fsx.md#fsx-ontap-failover-failback-under-60-seconds)
  link: [automatically fails back to it](../facts/fsx.md#fsx-ontap-failover-failback-under-60-seconds)
fsx-ontap-failover-transparent-nfs-smb-iscsi-needs-multipathing
  claim: For NFS and SMB clients, failovers are transparent because the endpoint IP address stays the same; for iSCSI and NVMe/TCP, transparency depends on client-side multipathing that you must configure on the client.
  scope: Amazon FSx for NetApp ONTAP failover.
  link: [failovers are transparent](../facts/fsx.md#fsx-ontap-failover-transparent-nfs-smb-iscsi-needs-multipathing)
  link: [client-side multipathing](../facts/fsx.md#fsx-ontap-failover-transparent-nfs-smb-iscsi-needs-multipathing)
fsx-ontap-flexcache-remote-caching-sparsely-populated
  claim: FlexCache is NetApp ONTAP's remote caching capability that brings datasets closer to clients; a FlexCache volume is a sparsely populated cache of an origin volume, best suited for read-intensive workflows with infrequent data changes.
  scope: FSx for ONTAP FlexCache.
  link: [remote caching capability](../facts/fsx.md#fsx-ontap-flexcache-remote-caching-sparsely-populated)
  link: [sparsely-populated cache](../facts/fsx.md#fsx-ontap-flexcache-remote-caching-sparsely-populated)
  link: [read-intensive workflows with infrequent data changes](../facts/fsx.md#fsx-ontap-flexcache-remote-caching-sparsely-populated)
fsx-ontap-four-deployment-types
  claim: FSx for ONTAP uses Single-AZ and Multi-AZ deployment types, with four options: Single-AZ 1, Single-AZ 2, Multi-AZ 1 and Multi-AZ 2.
  scope: Amazon FSx for NetApp ONTAP.
  link: [Single-AZ 1, Single-AZ 2, Multi-AZ 1, and Multi-AZ 2](../facts/fsx.md#fsx-ontap-four-deployment-types)
  link: [Single-AZ and Multi-AZ deployment types](../facts/fsx.md#fsx-ontap-four-deployment-types)
fsx-ontap-fully-managed-built-on-netapp-ontap
  claim: Amazon FSx for NetApp ONTAP is a fully managed service that provides reliable, scalable, high-performing and feature-rich file storage built on NetApp's ONTAP file system.
  scope: Amazon FSx for NetApp ONTAP.
  link: [fully managed service](../facts/fsx.md#fsx-ontap-fully-managed-built-on-netapp-ontap)
  link: [built on NetApp's popular ONTAP file system](../facts/fsx.md#fsx-ontap-fully-managed-built-on-netapp-ontap)
fsx-ontap-ha-pairs-by-generation
  claim: First-generation FSx for ONTAP file systems and second-generation Multi-AZ file systems support one HA pair, while second-generation Single-AZ file systems support up to 12 HA pairs.
  scope: Amazon FSx for NetApp ONTAP.
  link: [support one HA pair](../facts/fsx.md#fsx-ontap-ha-pairs-by-generation)
  link: [support up to 12 HA pairs](../facts/fsx.md#fsx-ontap-ha-pairs-by-generation)
fsx-ontap-in-transit-kerberos-and-ipsec-options
  claim: FSx for ONTAP can encrypt data in transit with Kerberos-based encryption over NFS and SMB and with IPsec-based encryption over NFS, iSCSI and SMB.
  scope: Amazon FSx for NetApp ONTAP encryption.
  link: [Kerberos-based encryption over NFS and SMB](../facts/fsx.md#fsx-ontap-in-transit-kerberos-and-ipsec-options)
  link: [IPsec-based encryption over NFS, iSCSI, and SMB](../facts/fsx.md#fsx-ontap-in-transit-kerberos-and-ipsec-options)
fsx-ontap-limit-automated-backup-retention
  claim: The maximum retention period for automated backups of an FSx for ONTAP file system is 90 days.
  scope: per file system; maximum; not adjustable.
  link: [90 days](../facts/fsx.md#fsx-ontap-limit-automated-backup-retention)
fsx-ontap-limit-backups-per-volume
  claim: The maximum number of backups of an FSx for ONTAP volume is 4,091 per volume.
  scope: per volume; maximum; not adjustable.
  link: [4,091](../facts/fsx.md#fsx-ontap-limit-backups-per-volume)
fsx-ontap-limit-max-ssd-capacity
  claim: The maximum SSD storage capacity of an FSx for ONTAP file system is 512 TiB per HA pair, up to 1 PiB, for second-generation Single-AZ file systems; 512 TiB for second-generation Multi-AZ file systems; and 192 TiB for first-generation file systems.
  scope: per file system, by generation and deployment type; maximum; not adjustable.
  link: [512 TiB](../facts/fsx.md#fsx-ontap-limit-max-ssd-capacity)
  link: [1 PiB](../facts/fsx.md#fsx-ontap-limit-max-ssd-capacity)
  link: [192 TiB](../facts/fsx.md#fsx-ontap-limit-max-ssd-capacity)
fsx-ontap-limit-max-ssd-iops
  claim: The maximum SSD IOPS of an FSx for ONTAP file system is 200,000 per HA pair (up to 12 pairs) for second-generation Single-AZ, 200,000 total for second-generation Multi-AZ, and 160,000 or 80,000 for first-generation file systems depending on the Region.
  scope: per file system, by generation, deployment type and Region; maximum; not adjustable.
  link: [200,000](../facts/fsx.md#fsx-ontap-limit-max-ssd-iops)
  link: [160,000](../facts/fsx.md#fsx-ontap-limit-max-ssd-iops)
  link: [80,000](../facts/fsx.md#fsx-ontap-limit-max-ssd-iops)
fsx-ontap-limit-max-throughput-capacity
  claim: The maximum throughput capacity of an FSx for ONTAP file system is 73,728 MBps for second-generation Single-AZ, 6,144 MBps for second-generation Multi-AZ, and 4,096 MBps or 2,048 MBps for first-generation file systems depending on the Region.
  scope: per file system, by generation, deployment type and Region; maximum; not adjustable.
  link: [73,728 MBps](../facts/fsx.md#fsx-ontap-limit-max-throughput-capacity)
  link: [6,144 MBps](../facts/fsx.md#fsx-ontap-limit-max-throughput-capacity)
  link: [4,096 MBps](../facts/fsx.md#fsx-ontap-limit-max-throughput-capacity)
  link: [2,048 MBps](../facts/fsx.md#fsx-ontap-limit-max-throughput-capacity)
fsx-ontap-limit-min-ssd-capacity
  claim: The minimum SSD storage capacity of an FSx for ONTAP file system is 1,024 GiB per high-availability (HA) pair.
  scope: per high-availability (HA) pair; minimum; not adjustable.
  link: [1,024 GiB](../facts/fsx.md#fsx-ontap-limit-min-ssd-capacity)
fsx-ontap-limit-min-ssd-capacity-for-decrease
  claim: The minimum SSD storage capacity for initiating a decrease operation on an FSx for ONTAP file system is 1,126 GiB per HA pair.
  scope: per HA pair; minimum; not adjustable.
  link: [1,126 GiB](../facts/fsx.md#fsx-ontap-limit-min-ssd-capacity-for-decrease)
fsx-ontap-limit-min-ssd-decrease-percentage
  claim: The minimum SSD decrease percentage of an FSx for ONTAP file system is 9% smaller than current capacity.
  scope: per decrease operation; minimum; not adjustable.
  link: [9% smaller](../facts/fsx.md#fsx-ontap-limit-min-ssd-decrease-percentage)
fsx-ontap-limit-min-throughput-capacity
  claim: The minimum throughput capacity of an FSx for ONTAP file system is 384 MBps for second-generation file systems with 1 HA pair, 1,536 MBps per HA pair for second-generation file systems with 2 or more HA pairs, and 128 MBps for first-generation file systems.
  scope: per file system, by generation and number of HA pairs; minimum; not adjustable.
  link: [384 MBps](../facts/fsx.md#fsx-ontap-limit-min-throughput-capacity)
  link: [128 MBps](../facts/fsx.md#fsx-ontap-limit-min-throughput-capacity)
fsx-ontap-limit-recommended-max-ssd-utilization
  claim: The recommended maximum SSD utilization of an FSx for ONTAP file system is 80% for optimal performance and tiering functionality.
  scope: per file system; maximum; not adjustable.
  link: [80%](../facts/fsx.md#fsx-ontap-limit-recommended-max-ssd-utilization)
fsx-ontap-limit-snapshots-per-volume
  claim: The maximum number of snapshots on an FSx for ONTAP volume is 1,023 per volume.
  scope: per volume; maximum; not adjustable.
  link: [1,023](../facts/fsx.md#fsx-ontap-limit-snapshots-per-volume)
fsx-ontap-limit-tags-per-file-system
  claim: The maximum number of tags per FSx for ONTAP file system is 50.
  scope: per file system; maximum; not adjustable.
  link: [50](../facts/fsx.md#fsx-ontap-limit-tags-per-file-system)
fsx-ontap-limit-user-backup-retention
  claim: The maximum retention period for user-initiated backups of an FSx for ONTAP file system is no retention limit.
  scope: per file system; maximum; not adjustable.
  link: [No retention limit](../facts/fsx.md#fsx-ontap-limit-user-backup-retention)
fsx-ontap-multi-az-continuous-availability-business-critical
  claim: Multi-AZ FSx for ONTAP file systems are designed to provide continuous availability to data even when an Availability Zone is unavailable, and suit business-critical production workloads that need built-in replication across Availability Zones.
  scope: Amazon FSx for NetApp ONTAP Multi-AZ.
  link: [continuous availability to data](../facts/fsx.md#fsx-ontap-multi-az-continuous-availability-business-critical)
  link: [business-critical production workloads](../facts/fsx.md#fsx-ontap-multi-az-continuous-availability-business-critical)
fsx-ontap-multi-az-floating-ip-endpoints
  claim: The NFS, SMB and ONTAP management endpoints on Multi-AZ FSx for ONTAP file systems use floating IP addresses so that connected clients transition seamlessly between the preferred and standby file servers during a failover.
  scope: Amazon FSx for NetApp ONTAP Multi-AZ.
  link: [use floating internet protocol (IP) addresses](../facts/fsx.md#fsx-ontap-multi-az-floating-ip-endpoints)
  link: [seamlessly transition between the preferred and standby](../facts/fsx.md#fsx-ontap-multi-az-floating-ip-endpoints)
fsx-ontap-multi-az-outside-vpc-needs-transit-gateway
  claim: The NFS, SMB and ONTAP management endpoints of FSx for ONTAP Multi-AZ file systems use floating IP addresses; because VPC Peering, Direct Connect and Site-to-Site VPN don't support transitive peering, you are required to use Transit Gateway to access these interfaces from networks outside the file system's VPC.
  scope: Amazon FSx for NetApp ONTAP Multi-AZ.
  link: [don't support transitive peering](../facts/fsx.md#fsx-ontap-multi-az-outside-vpc-needs-transit-gateway)
  link: [required to use Transit Gateway](../facts/fsx.md#fsx-ontap-multi-az-outside-vpc-needs-transit-gateway)
fsx-ontap-multi-az-standby-other-az-sync-replication
  claim: A Multi-AZ FSx for ONTAP file system has a single HA pair whose standby file server is in a different Availability Zone from the active one, and every change is synchronously replicated across Availability Zones to the standby.
  scope: Amazon FSx for NetApp ONTAP Multi-AZ.
  link: [deployed in a different Availability Zone](../facts/fsx.md#fsx-ontap-multi-az-standby-other-az-sync-replication)
  link: [synchronously replicated across Availability Zones](../facts/fsx.md#fsx-ontap-multi-az-standby-other-az-sync-replication)
fsx-ontap-multiprotocol-nfs-smb-iscsi-nvme-multiple-os
  claim: You can access FSx for ONTAP data from Linux, Windows and macOS clients at the same time over NFS (v3, v4, v4.1, v4.2) and SMB, and you can also use the NVMe and iSCSI block protocols.
  scope: Amazon FSx for NetApp ONTAP.
  link: [Linux, Windows, or macOS clients simultaneously](../facts/fsx.md#fsx-ontap-multiprotocol-nfs-smb-iscsi-nvme-multiple-os)
  link: [Non-Volatile Memory Express (NVMe)](../facts/fsx.md#fsx-ontap-multiprotocol-nfs-smb-iscsi-nvme-multiple-os)
fsx-ontap-no-public-internet-access
  claim: Amazon FSx doesn't support accessing FSx for ONTAP file systems from the public internet.
  scope: Amazon FSx for NetApp ONTAP clients.
  link: [doesn't support accessing file systems](../facts/fsx.md#fsx-ontap-no-public-internet-access)
  link: [from the public internet](../facts/fsx.md#fsx-ontap-no-public-internet-access)
fsx-ontap-post-process-compression-14-days
  claim: ONTAP runs post-process compression for data that is retained on SSD storage for a minimum of 14 days.
  scope: FSx for ONTAP SSD storage; minimum; adjustable.
  link: [14 days](../facts/fsx.md#fsx-ontap-post-process-compression-14-days)
fsx-ontap-pricing-backups-incremental
  claim: FSx for ONTAP backups are incremental, which means that only the changes after your most recent backup are saved, so you save on storage costs by not duplicating data.
  scope: FSx for NetApp ONTAP backups.
  link: [incremental](../facts/fsx.md#fsx-ontap-pricing-backups-incremental)
fsx-ontap-pricing-capacity-pool-definition
  claim: FSx for ONTAP capacity pool storage is elastic storage that is cost-optimized for infrequently-accessed data.
  scope: FSx for NetApp ONTAP capacity pool storage.
  link: [elastic storage](../facts/fsx.md#fsx-ontap-pricing-capacity-pool-definition)
fsx-ontap-pricing-capacity-pool-pay-for-consumed-plus-requests
  claim: For FSx for NetApp ONTAP capacity pool storage you pay only for the storage space consumed, and you also pay request costs for each read and write operation whenever the data is accessed.
  scope: FSx for NetApp ONTAP capacity pool storage.
  link: [pay only for the storage space consumed](../facts/fsx.md#fsx-ontap-pricing-capacity-pool-pay-for-consumed-plus-requests)
  link: [requests costs (per read and write operation)](../facts/fsx.md#fsx-ontap-pricing-capacity-pool-pay-for-consumed-plus-requests)
fsx-ontap-pricing-five-components
  claim: AWS says the cost of FSx for NetApp ONTAP has five components: SSD storage, SSD IOPS, capacity pool usage, throughput capacity and backups. S3 requests are charged when you access data through S3 Access Points.
  scope: FSx for NetApp ONTAP billing.
  link: [five Amazon FSx for NetApp ONTAP components](../facts/fsx.md#fsx-ontap-pricing-five-components)
  link: [SSD storage, SSD IOPS, capacity pool usage](../facts/fsx.md#fsx-ontap-pricing-five-components)
fsx-ontap-pricing-prorated-by-hour
  claim: For FSx for NetApp ONTAP, pricing is quoted on a monthly basis, usage is prorated by the hour, and you are billed for your average usage over a month.
  scope: FSx for NetApp ONTAP.
  link: [prorated by the hour](../facts/fsx.md#fsx-ontap-pricing-prorated-by-hour)
fsx-ontap-pricing-ssd-iops-included
  claim: For FSx for NetApp ONTAP, 3 IOPS are included for every GB of SSD storage by default.
  scope: per GB of SSD storage; default.
  link: [3 IOPS](../facts/fsx.md#fsx-ontap-pricing-ssd-iops-included)
fsx-ontap-quota-backups-per-account
  claim: The default for ONTAP backups is 10,000, the maximum number of user-initiated volume backups for all Amazon FSx for NetApp ONTAP file systems that you can have in an AWS account.
  scope: per account, per AWS Region, all ONTAP file systems; default; adjustable.
  link: [10,000](../facts/fsx.md#fsx-ontap-quota-backups-per-account)
fsx-ontap-quota-file-systems-per-account
  claim: The default for ONTAP file systems is 100, the maximum number of Amazon FSx for NetApp ONTAP file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-ontap-quota-file-systems-per-account)
fsx-ontap-quota-ssd-capacity-per-account
  claim: The default for ONTAP SSD storage capacity is 524,288, the maximum amount of SSD storage capacity (in GiB) for all Amazon FSx for NetApp ONTAP file systems that you can have in this account.
  scope: per account, per AWS Region, all ONTAP file systems; default; adjustable.
  link: [524,288](../facts/fsx.md#fsx-ontap-quota-ssd-capacity-per-account)
fsx-ontap-quota-ssd-iops-per-account
  claim: The default for ONTAP SSD IOPS is 1,000,000, the maximum amount of SSD IOPS for all Amazon FSx for NetApp ONTAP file systems that you can have in this account.
  scope: per account, per AWS Region, all ONTAP file systems; default; adjustable.
  link: [1,000,000](../facts/fsx.md#fsx-ontap-quota-ssd-iops-per-account)
fsx-ontap-quota-throughput-capacity-per-account
  claim: The default for ONTAP throughput capacity is 10,240, the maximum amount of throughput capacity (in MBps) for all Amazon FSx for NetApp ONTAP file systems that you can have in this account.
  scope: per account, per AWS Region, all ONTAP file systems; default; adjustable.
  link: [10,240](../facts/fsx.md#fsx-ontap-quota-throughput-capacity-per-account)
fsx-ontap-restore-backup-same-region-copy-first-for-other-region
  claim: You can restore an FSx for ONTAP volume backup to any existing FSx for ONTAP file system you have access to that is in the same AWS Region where the backup is stored.
  scope: FSx for ONTAP backups.
  link: [any existing FSx for ONTAP file system](../facts/fsx.md#fsx-ontap-restore-backup-same-region-copy-first-for-other-region)
  link: [same AWS Region where the backup is stored](../facts/fsx.md#fsx-ontap-restore-backup-same-region-copy-first-for-other-region)
fsx-ontap-s3-access-points-block-public-access-always-on
  claim: Amazon S3 enforces Block public access by default for all access points attached to an FSx for ONTAP volume, and you cannot modify or disable this setting.
  scope: Amazon FSx for NetApp ONTAP S3 access points.
  link: [enforces Block public access by default](../facts/fsx.md#fsx-ontap-s3-access-points-block-public-access-always-on)
  link: [cannot modify or disable this setting](../facts/fsx.md#fsx-ontap-s3-access-points-block-public-access-always-on)
fsx-ontap-s3-access-points-s3-api-on-file-data-no-copy
  claim: An S3 access point attached to an FSx for ONTAP volume lets you access file data through the S3 API while the data stays on the file system and you keep using NFS and SMB alongside it.
  scope: Amazon FSx for NetApp ONTAP S3 access points.
  link: [access your file data using the S3 API](../facts/fsx.md#fsx-ontap-s3-access-points-s3-api-on-file-data-no-copy)
  link: [continue using the NFS and SMB protocols](../facts/fsx.md#fsx-ontap-s3-access-points-s3-api-on-file-data-no-copy)
fsx-ontap-single-az-1-one-ha-pair-single-az-2-up-to-12
  claim: Single-AZ 1 is a first-generation file system with one high-availability pair, whereas Single-AZ 2 is a second-generation file system with 1 to 12 HA pairs.
  scope: Amazon FSx for NetApp ONTAP Single-AZ.
  link: [with 1–12 HA pairs](../facts/fsx.md#fsx-ontap-single-az-1-one-ha-pair-single-az-2-up-to-12)
  link: [first-generation file system with one high-availability](../facts/fsx.md#fsx-ontap-single-az-1-one-ha-pair-single-az-2-up-to-12)
fsx-ontap-single-az-active-standby-pairs-separate-fault-domains
  claim: A Single-AZ FSx for ONTAP file system provisions one to twelve pairs of active-standby file servers, with the active and standby server of each pair in separate fault domains within one Availability Zone.
  scope: Amazon FSx for NetApp ONTAP Single-AZ.
  link: [active-standby configuration](../facts/fsx.md#fsx-ontap-single-az-active-standby-pairs-separate-fault-domains)
  link: [separate fault domains within a single Availability Zone](../facts/fsx.md#fsx-ontap-single-az-active-standby-pairs-separate-fault-domains)
fsx-ontap-single-az-failover-within-seconds
  claim: During planned maintenance or an unplanned disruption of an active file server, Amazon FSx automatically and independently fails over that HA pair to the standby file server, typically within a few seconds, with no manual intervention.
  scope: Amazon FSx for NetApp ONTAP Single-AZ.
  link: [typically within a few seconds](../facts/fsx.md#fsx-ontap-single-az-failover-within-seconds)
  link: [automatically and independently fails over](../facts/fsx.md#fsx-ontap-single-az-failover-within-seconds)
fsx-ontap-single-az-for-dev-test-secondary-copies
  claim: Single-AZ FSx for ONTAP file systems suit use cases that do not require the data resiliency of Multi-AZ, such as development and test environments or secondary copies of data already stored on premises or in other Regions, because they replicate data only within a single Availability Zone.
  scope: Amazon FSx for NetApp ONTAP Single-AZ.
  link: [development and test environments](../facts/fsx.md#fsx-ontap-single-az-for-dev-test-secondary-copies)
  link: [only replicating data within a single Availability Zone](../facts/fsx.md#fsx-ontap-single-az-for-dev-test-secondary-copies)
  link: [cost-optimized solution](../facts/fsx.md#fsx-ontap-single-az-for-dev-test-secondary-copies)
fsx-ontap-single-az-secondary-ips-no-transit-gateway-needed
  claim: On Single-AZ FSx for ONTAP file systems the NFS, SMB and management endpoints are secondary IP addresses within the VPC's CIDR range, so clients can use VPC Peering, Direct Connect or Site-to-Site VPN without AWS Transit Gateway.
  scope: Amazon FSx for NetApp ONTAP Single-AZ.
  link: [secondary IP addresses](../facts/fsx.md#fsx-ontap-single-az-secondary-ips-no-transit-gateway-needed)
  link: [without requiring AWS Transit Gateway](../facts/fsx.md#fsx-ontap-single-az-secondary-ips-no-transit-gateway-needed)
fsx-ontap-snaplock-compliance-no-delete-by-any-user
  claim: After a file is moved to the WORM state on a SnapLock Compliance volume, no user can delete it before its retention period expires.
  scope: FSx for ONTAP SnapLock Compliance.
  link: [can't be deleted before its retention period expires](../facts/fsx.md#fsx-ontap-snaplock-compliance-no-delete-by-any-user)
  link: [by any user](../facts/fsx.md#fsx-ontap-snaplock-compliance-no-delete-by-any-user)
fsx-ontap-snaplock-compliance-use-cases-sec-finra-cftc
  claim: You can use SnapLock Compliance to address government or industry-specific mandates such as SEC Rule 17a-4(f), FINRA Rule 4511 and CFTC Regulation 1.31.
  scope: FSx for ONTAP SnapLock Compliance.
  link: [SEC Rule 17a-4(f), FINRA Rule 4511](../facts/fsx.md#fsx-ontap-snaplock-compliance-use-cases-sec-finra-cftc)
  link: [CFTC Regulation 1.31](../facts/fsx.md#fsx-ontap-snaplock-compliance-use-cases-sec-finra-cftc)
fsx-ontap-snaplock-enterprise-specific-users-privileged-delete
  claim: SnapLock Enterprise lets you authorize only specific users to delete files, and you can use it to test retention settings before using SnapLock Compliance.
  scope: FSx for ONTAP SnapLock Enterprise.
  link: [authorize only specific users to delete files](../facts/fsx.md#fsx-ontap-snaplock-enterprise-specific-users-privileged-delete)
  link: [test retention settings](../facts/fsx.md#fsx-ontap-snaplock-enterprise-specific-users-privileged-delete)
fsx-ontap-snaplock-set-at-volume-creation-no-conversion
  claim: You must decide at volume creation whether a volume uses SnapLock, a non-SnapLock volume can't be converted to a SnapLock volume, and a SnapLock volume can't be converted between Enterprise and Compliance.
  scope: FSx for ONTAP SnapLock.
  link: [at the time of creation](../facts/fsx.md#fsx-ontap-snaplock-set-at-volume-creation-no-conversion)
  link: [can't be converted to a SnapLock volume](../facts/fsx.md#fsx-ontap-snaplock-set-at-volume-creation-no-conversion)
fsx-ontap-snaplock-worm-compliance-and-enterprise-modes
  claim: SnapLock moves files to a write once, read many (WORM) state that prevents modification or deletion for a specified retention period, and FSx for ONTAP supports the Compliance and Enterprise retention modes.
  scope: FSx for ONTAP SnapLock.
  link: [write once, read many (WORM) state](../facts/fsx.md#fsx-ontap-snaplock-worm-compliance-and-enterprise-modes)
  link: [Compliance and Enterprise modes of retention](../facts/fsx.md#fsx-ontap-snaplock-worm-compliance-and-enterprise-modes)
fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp
  claim: AWS recommends using NetApp SnapMirror to migrate on-premises NetApp ONTAP file systems to FSx for ONTAP.
  scope: Amazon FSx for NetApp ONTAP migration.
  link: [recommend using SnapMirror to migrate](../facts/fsx.md#fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp)
  link: [migrate your NetApp ONTAP file systems](../facts/fsx.md#fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp)
fsx-ontap-snapmirror-scheduled-replication-in-and-cross-region
  claim: You can use NetApp SnapMirror to schedule periodic replication of an FSx for ONTAP file system to or from a second file system, in-Region or cross-Region, as frequently as every 5 minutes.
  scope: FSx for ONTAP SnapMirror.
  link: [both in-Region and cross-Region deployments](../facts/fsx.md#fsx-ontap-snapmirror-scheduled-replication-in-and-cross-region)
  link: [as frequently as every 5 minutes](../facts/fsx.md#fsx-ontap-snapmirror-scheduled-replication-in-and-cross-region)
fsx-ontap-snapmirror-volume-level-only-no-synchronous
  claim: Only volume-level SnapMirror replication is supported by FSx for ONTAP, and synchronous SnapMirror, including StrictSync, is not supported.
  scope: FSx for ONTAP SnapMirror.
  link: [Only volume-level SnapMirror replication is supported](../facts/fsx.md#fsx-ontap-snapmirror-volume-level-only-no-synchronous)
  link: [Synchronous SnapMirror](../facts/fsx.md#fsx-ontap-snapmirror-volume-level-only-no-synchronous)
fsx-ontap-snapshots-1023-per-volume-limit
  claim: You can store a maximum of 1,023 snapshots per volume at any point in time.
  scope: per FSx for ONTAP volume; maximum; not adjustable.
  link: [maximum of 1,023 snapshots per volume](../facts/fsx.md#fsx-ontap-snapshots-1023-per-volume-limit)
  link: [at any point in time](../facts/fsx.md#fsx-ontap-snapshots-1023-per-volume-limit)
fsx-ontap-snapshots-restore-individual-files-self-service
  claim: With ONTAP snapshots, users can view and restore individual files or folders from an earlier snapshot to undo changes, recover deleted content and compare file versions.
  scope: Amazon FSx for NetApp ONTAP snapshots.
  link: [restore individual files or folders](../facts/fsx.md#fsx-ontap-snapshots-restore-individual-files-self-service)
  link: [from an earlier snapshot](../facts/fsx.md#fsx-ontap-snapshots-restore-individual-files-self-service)
fsx-ontap-ssd-increase-and-second-gen-decrease
  claim: You can increase the SSD storage capacity of an FSx for ONTAP file system as your storage needs grow, and on second-generation file systems you can also decrease SSD storage capacity.
  scope: FSx for NetApp ONTAP SSD storage.
  link: [increase the SSD storage capacity](../facts/fsx.md#fsx-ontap-ssd-increase-and-second-gen-decrease)
  link: [decrease SSD storage capacity](../facts/fsx.md#fsx-ontap-ssd-increase-and-second-gen-decrease)
fsx-ontap-storage-efficiency-65-percent-typical
  claim: The typical storage capacity savings for general purpose file sharing workloads is 65% from compression, deduplication and compaction on both the SSD and capacity pool tiers, without sacrificing performance.
  scope: Amazon FSx for NetApp ONTAP storage efficiency.
  link: [65% from compression, deduplication, and compaction](../facts/fsx.md#fsx-ontap-storage-efficiency-65-percent-typical)
  link: [general purpose file sharing workloads](../facts/fsx.md#fsx-ontap-storage-efficiency-65-percent-typical)
fsx-ontap-supported-clients-nfs-smb-iscsi-versions
  claim: FSx for ONTAP supports access over NFS (v3, v4.0, v4.1 and v4.2), all versions of SMB (including 2.0, 3.0 and 3.1.1) and the iSCSI protocol.
  scope: Amazon FSx for NetApp ONTAP clients.
  link: [v3, v4.0, v4.1 and v4.2](../facts/fsx.md#fsx-ontap-supported-clients-nfs-smb-iscsi-versions)
  link: [including 2.0, 3.0, and 3.1.1](../facts/fsx.md#fsx-ontap-supported-clients-nfs-smb-iscsi-versions)
fsx-ontap-svm-isolated-file-server-joins-active-directory
  claim: A storage virtual machine (SVM) is an isolated file server with its own administrative and data access endpoints, and you can join SVMs to a Microsoft Active Directory for file access authentication and authorization.
  scope: Amazon FSx for NetApp ONTAP SVM.
  link: [isolated file server](../facts/fsx.md#fsx-ontap-svm-isolated-file-server-joins-active-directory)
  link: [join SVMs to a Microsoft Active Directory](../facts/fsx.md#fsx-ontap-svm-isolated-file-server-joins-active-directory)
fsx-ontap-test-failover-by-changing-throughput-capacity
  claim: You can test failover on an FSx for ONTAP file system by modifying its throughput capacity.
  scope: Amazon FSx for NetApp ONTAP failover.
  link: [test failover on your file system](../facts/fsx.md#fsx-ontap-test-failover-by-changing-throughput-capacity)
  link: [modifying its throughput capacity](../facts/fsx.md#fsx-ontap-test-failover-by-changing-throughput-capacity)
fsx-ontap-tiering-happens-24-48-hours-after-cooling-period
  claim: Data is tiered 24 to 48 hours after its cooling period expires, and tiering is a background process with a lower priority than client-facing requests.
  scope: FSx for ONTAP volume tiering.
  link: [24–48 hours after its cooling period expires](../facts/fsx.md#fsx-ontap-tiering-happens-24-48-hours-after-cooling-period)
  link: [lower priority than client-facing requests](../facts/fsx.md#fsx-ontap-tiering-happens-24-48-hours-after-cooling-period)
fsx-ontap-tiering-policy-all-marks-everything-cold
  claim: The All tiering policy marks all user data and snapshot data as cold and stores it in the capacity pool tier, where data blocks stay cold when read; file metadata always remains on the SSD tier.
  scope: FSx for ONTAP volume tiering policy All.
  link: [marks all user data and snapshot data](../facts/fsx.md#fsx-ontap-tiering-policy-all-marks-everything-cold)
  link: [file metadata always remains on the SSD tier](../facts/fsx.md#fsx-ontap-tiering-policy-all-marks-everything-cold)
fsx-ontap-tiering-policy-auto-31-days-default-console
  claim: The Auto tiering policy moves all cold user data and snapshots to the capacity pool tier; the cooling period is 31 days by default and configurable from 2 to 183 days, and Auto is the default policy when creating a volume in the console.
  scope: FSx for ONTAP volume tiering policy Auto; default; adjustable.
  link: [by default is 31 days](../facts/fsx.md#fsx-ontap-tiering-policy-auto-31-days-default-console)
  link: [between 2–183 days](../facts/fsx.md#fsx-ontap-tiering-policy-auto-31-days-default-console)
fsx-ontap-tiering-policy-none-keeps-all-on-ssd
  claim: The None tiering policy keeps all of a volume's data on the primary storage tier and prevents it from being moved to capacity pool storage.
  scope: FSx for ONTAP volume tiering policy None.
  link: [keeps all of your volume’s data](../facts/fsx.md#fsx-ontap-tiering-policy-none-keeps-all-on-ssd)
  link: [prevents it from being moved](../facts/fsx.md#fsx-ontap-tiering-policy-none-keeps-all-on-ssd)
fsx-ontap-tiering-policy-per-volume-cooling-period
  claim: Data tiering automatically moves data between the SSD and capacity pool tiers; each volume has a tiering policy that controls whether cold data moves to the capacity tier, and the cooling period determines when data becomes cold.
  scope: Amazon FSx for NetApp ONTAP storage tiers.
  link: [tiering policy that controls whether data is moved](../facts/fsx.md#fsx-ontap-tiering-policy-per-volume-cooling-period)
  link: [cooling period determines when data becomes inactive](../facts/fsx.md#fsx-ontap-tiering-policy-per-volume-cooling-period)
fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli
  claim: The Snapshot Only tiering policy moves only snapshot data to the capacity pool tier, with a cooling period that is 2 days by default and configurable from 2 to 183 days; it is the default policy when creating a volume with the AWS CLI, API or ONTAP CLI.
  scope: FSx for ONTAP volume tiering policy Snapshot Only; default; adjustable.
  link: [moves only snapshot data](../facts/fsx.md#fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli)
  link: [by default is set to 2 days](../facts/fsx.md#fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli)
fsx-ontap-two-storage-tiers-primary-ssd-and-capacity-pool
  claim: An FSx for ONTAP file system has two storage tiers: primary storage, which is provisioned high-performance SSD storage for the active portion of your data, and capacity pool storage, which is fully elastic, scales to petabytes and is cost optimized for infrequently accessed data.
  scope: Amazon FSx for NetApp ONTAP storage tiers.
  link: [primary storage and capacity pool storage](../facts/fsx.md#fsx-ontap-two-storage-tiers-primary-ssd-and-capacity-pool)
  link: [fully elastic storage tier](../facts/fsx.md#fsx-ontap-two-storage-tiers-primary-ssd-and-capacity-pool)
fsx-ontap-user-initiated-backups-retained-forever
  claim: User-initiated FSx for ONTAP backups are retained forever unless you delete them, and they are retained even after you delete the volume or the file system.
  scope: FSx for ONTAP backups.
  link: [retained forever, unless you delete them](../facts/fsx.md#fsx-ontap-user-initiated-backups-retained-forever)
  link: [retained even after you delete the volume](../facts/fsx.md#fsx-ontap-user-initiated-backups-retained-forever)
fsx-ontap-vmware-cloud-external-datastore
  claim: You can use FSx for ONTAP as an external datastore for VMware Cloud on AWS Software-Defined Data Centers (SDDCs).
  scope: Amazon FSx for NetApp ONTAP.
  link: [external datastore for VMware Cloud on AWS](../facts/fsx.md#fsx-ontap-vmware-cloud-external-datastore)
  link: [Software-Defined Data Centers (SDDCs)](../facts/fsx.md#fsx-ontap-vmware-cloud-external-datastore)
fsx-ontap-volumes-logical-containers-on-svms-thin-provisioned
  claim: FSx for ONTAP volumes are logical containers hosted on SVMs, and they are thin provisioned, so they only consume storage capacity for the data stored in them.
  scope: Amazon FSx for NetApp ONTAP volumes.
  link: [logical containers that are hosted on SVMs](../facts/fsx.md#fsx-ontap-volumes-logical-containers-on-svms-thin-provisioned)
  link: [thin provisioned](../facts/fsx.md#fsx-ontap-volumes-logical-containers-on-svms-thin-provisioned)
fsx-ontap-what-is-migrate-backup-burst-from-on-premises-ontap
  claim: AWS says that for customers who use NetApp ONTAP on premises, FSx for ONTAP is an ideal solution to migrate, back up or burst file-based applications to AWS without changing the application code or how they manage their data.
  scope: FSx for NetApp ONTAP.
  link: [migrate, back up, or burst your file-based applications](../facts/fsx.md#fsx-ontap-what-is-migrate-backup-burst-from-on-premises-ontap)
fsx-ontap-what-is-multiprotocol-nfs-smb-iscsi-nvme
  claim: FSx for ONTAP offers multi-protocol access to data using the NFS, SMB, iSCSI and NVMe protocols, and its file storage is broadly accessible from Linux, Windows and macOS compute instances running in AWS or on premises.
  scope: FSx for NetApp ONTAP.
  link: [Internet Small Computer Systems Interface (iSCSI)](../facts/fsx.md#fsx-ontap-what-is-multiprotocol-nfs-smb-iscsi-nvme)
  link: [Network File System (NFS), Server Message Block (SMB)](../facts/fsx.md#fsx-ontap-what-is-multiprotocol-nfs-smb-iscsi-nvme)
  link: [Non-Volatile Memory Express (NVMe) protocols](../facts/fsx.md#fsx-ontap-what-is-multiprotocol-nfs-smb-iscsi-nvme)
fsx-ontap-what-is-ssd-performance-pay-small-fraction
  claim: AWS says that with FSx for ONTAP you can achieve SSD levels of performance for your workload while paying for SSD storage for only a small fraction of your data; in addition, FSx for ONTAP automatically tiers your data to lower-cost, elastic storage.
  scope: FSx for NetApp ONTAP.
  link: [SSD storage for only a small fraction](../facts/fsx.md#fsx-ontap-what-is-ssd-performance-pay-small-fraction)
fsx-openzfs-access-control-security-groups-iam-unix-permissions
  claim: Amazon FSx provides access control for OpenZFS at the file system level with VPC security groups, at the API level with IAM access policies, and at the file and folder level with Unix permissions.
  scope: Amazon FSx for OpenZFS.
  link: [Amazon Virtual Private Cloud (Amazon VPC) security groups](../facts/fsx.md#fsx-openzfs-access-control-security-groups-iam-unix-permissions)
  link: [supports Unix permissions](../facts/fsx.md#fsx-openzfs-access-control-security-groups-iam-unix-permissions)
fsx-openzfs-automatic-daily-backup-default-30-days-console-user-kept-forever
  claim: By default Amazon FSx takes an automatic daily backup of an FSx for OpenZFS file system; the console default retention is 30 days, the maximum retention for automatic backups is 90 days, and user-initiated backups are kept forever unless you delete them.
  scope: FSx for OpenZFS backups; default; adjustable.
  link: [default automatic daily backup retention period is 30 days](../facts/fsx.md#fsx-openzfs-automatic-daily-backup-default-30-days-console-user-kept-forever)
  link: [maximum retention period of 90 days](../facts/fsx.md#fsx-openzfs-automatic-daily-backup-default-30-days-console-user-kept-forever)
fsx-openzfs-backups-consistent-incremental-stored-in-s3
  claim: FSx for OpenZFS backups are file-system-consistent, highly durable and incremental, and Amazon FSx stores them in Amazon S3.
  scope: FSx for OpenZFS backups.
  link: [file-system-consistent, highly durable, and incremental](../facts/fsx.md#fsx-openzfs-backups-consistent-incremental-stored-in-s3)
  link: [stores backups in Amazon Simple Storage Service](../facts/fsx.md#fsx-openzfs-backups-consistent-incremental-stored-in-s3)
fsx-openzfs-clients-same-az-as-preferred-file-server
  claim: For in-AWS applications, AWS recommends launching clients in the same Availability Zone as the preferred file server to minimize latency.
  scope: FSx for OpenZFS.
  link: [same Availability Zone as your preferred file server](../facts/fsx.md#fsx-openzfs-clients-same-az-as-preferred-file-server)
  link: [to minimize latency](../facts/fsx.md#fsx-openzfs-clients-same-az-as-preferred-file-server)
fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot
  claim: A clone volume is a writable copy initialized with the same data as the snapshot, created almost instantly and initially consuming no additional storage; it keeps a dependency on its source snapshot, so you cannot delete the snapshot while the clone is in use.
  scope: FSx for OpenZFS clones.
  link: [writable copy](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
  link: [created almost instantly](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
  link: [cannot delete this source snapshot](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
fsx-openzfs-compression-zstandard-vs-lz4
  claim: FSx for OpenZFS volumes support Zstandard compression, which gives very high on-disk compression with higher read throughput and reduced write throughput than LZ4, and LZ4 compression, which gives higher write throughput but lower compression than Zstandard.
  scope: FSx for OpenZFS data compression.
  link: [very high levels of on-disk data compression](../facts/fsx.md#fsx-openzfs-compression-zstandard-vs-lz4)
  link: [higher write throughput performance](../facts/fsx.md#fsx-openzfs-compression-zstandard-vs-lz4)
fsx-openzfs-encryption-at-rest-kms-backups-in-transit-automatic
  claim: Amazon FSx automatically encrypts FSx for OpenZFS data at rest in file systems and backups using keys that you manage in AWS KMS.
  scope: Amazon FSx for OpenZFS encryption.
  link: [automatically encrypts data at rest](../facts/fsx.md#fsx-openzfs-encryption-at-rest-kms-backups-in-transit-automatic)
  link: [file systems and backups](../facts/fsx.md#fsx-openzfs-encryption-at-rest-kms-backups-in-transit-automatic)
fsx-openzfs-failover-failback-under-60-seconds-io-pause
  claim: An FSx for OpenZFS failover typically takes less than 60 seconds from failure detection to promotion of the standby, the file system automatically fails back to the recovered preferred file server usually in less than 60 seconds, and I/O might be briefly paused during failover and failback.
  scope: FSx for OpenZFS failover.
  link: [less than 60 seconds](../facts/fsx.md#fsx-openzfs-failover-failback-under-60-seconds-io-pause)
  link: [I/O might be briefly paused](../facts/fsx.md#fsx-openzfs-failover-failback-under-60-seconds-io-pause)
fsx-openzfs-failover-triggers
  claim: Multi-AZ (HA) and Single-AZ (HA) file systems automatically fail over to the standby file server when the preferred file server becomes unavailable, when the throughput capacity is changed, or when it undergoes planned maintenance, and Multi-AZ (HA) file systems also fail over if an Availability Zone disruption occurs.
  scope: FSx for OpenZFS failover.
  link: [becomes unavailable](../facts/fsx.md#fsx-openzfs-failover-triggers)
  link: [throughput capacity is changed](../facts/fsx.md#fsx-openzfs-failover-triggers)
  link: [Availability Zone disruption occurs](../facts/fsx.md#fsx-openzfs-failover-triggers)
fsx-openzfs-full-copy-volume-independent-slower
  claim: A full-copy volume is a fully independent writable copy of a snapshot, but because all of the data must be transferred it can take significantly longer to create than a clone volume.
  scope: FSx for OpenZFS clones.
  link: [fully independent writable copy](../facts/fsx.md#fsx-openzfs-full-copy-volume-independent-slower)
  link: [significantly longer time to create](../facts/fsx.md#fsx-openzfs-full-copy-volume-independent-slower)
fsx-openzfs-fully-managed-move-from-onprem-zfs-linux-file-servers
  claim: Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data to AWS from on-premises ZFS or other Linux-based file servers.
  scope: Amazon FSx for OpenZFS.
  link: [fully managed file storage service](../facts/fsx.md#fsx-openzfs-fully-managed-move-from-onprem-zfs-linux-file-servers)
  link: [on-premises ZFS or other Linux-based file servers](../facts/fsx.md#fsx-openzfs-fully-managed-move-from-onprem-zfs-linux-file-servers)
fsx-openzfs-intelligent-tiering-elastic-grows-shrinks
  claim: FSx for OpenZFS file systems that use the Intelligent-Tiering storage class use fully elastic, intelligently tiered, regional block storage that automatically grows and shrinks to fit the workload.
  scope: FSx for OpenZFS Intelligent-Tiering storage class.
  link: [automatically grows and shrinks](../facts/fsx.md#fsx-openzfs-intelligent-tiering-elastic-grows-shrinks)
fsx-openzfs-intelligent-tiering-latency-tens-of-ms-vs-ssd-cache
  claim: Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of milliseconds and per-request costs, while accesses from the SSD read cache return with sub-millisecond latency and no per-request costs.
  scope: FSx for OpenZFS Intelligent-Tiering storage class.
  link: [roughly tens of milliseconds](../facts/fsx.md#fsx-openzfs-intelligent-tiering-latency-tens-of-ms-vs-ssd-cache)
  link: [sub-millisecond latency and no per-request costs](../facts/fsx.md#fsx-openzfs-intelligent-tiering-latency-tens-of-ms-vs-ssd-cache)
fsx-openzfs-intelligent-tiering-no-iops-provisioning-pay-per-request
  claim: With the Intelligent-Tiering storage class you do not need to provision IOPS; you pay for data access based on usage, in the form of read and write requests.
  scope: FSx for OpenZFS Intelligent-Tiering storage class.
  link: [do not need to provision IOPS](../facts/fsx.md#fsx-openzfs-intelligent-tiering-no-iops-provisioning-pay-per-request)
  link: [pay for data access based on usage](../facts/fsx.md#fsx-openzfs-intelligent-tiering-no-iops-provisioning-pay-per-request)
fsx-openzfs-intelligent-tiering-read-cache-sizing-modes
  claim: You can configure the SSD read cache of an Intelligent-Tiering file system with one of three sizing modes, Automatic, Custom or None.
  scope: FSx for OpenZFS Intelligent-Tiering storage class.
  link: [three sizing mode options](../facts/fsx.md#fsx-openzfs-intelligent-tiering-read-cache-sizing-modes)
  link: [Automatic, Custom, or None](../facts/fsx.md#fsx-openzfs-intelligent-tiering-read-cache-sizing-modes)
fsx-openzfs-limit-automated-backup-retention
  claim: The maximum retention period for automated backups of an FSx for OpenZFS file system is 90 days.
  scope: per file system; maximum; not adjustable.
  link: [90 days](../facts/fsx.md#fsx-openzfs-limit-automated-backup-retention)
fsx-openzfs-limit-max-capacity-intelligent-tiering
  claim: The maximum storage capacity for FSx for OpenZFS file systems using the Intelligent-Tiering storage class is 512 TiB.
  scope: per file system, Intelligent-Tiering; maximum; not adjustable.
  link: [512 TiB](../facts/fsx.md#fsx-openzfs-limit-max-capacity-intelligent-tiering)
fsx-openzfs-limit-max-capacity-single-az-2
  claim: The maximum storage capacity for FSx for OpenZFS Single-AZ 2 (non-HA and HA) file systems is 512 TiB.
  scope: per Single-AZ 2 (non-HA and HA) file system; maximum; not adjustable.
  link: [512 TiB](../facts/fsx.md#fsx-openzfs-limit-max-capacity-single-az-2)
fsx-openzfs-limit-max-snapshots
  claim: The maximum number of snapshots per FSx for OpenZFS file system is 700.
  scope: per file system; maximum; not adjustable.
  link: [700](../facts/fsx.md#fsx-openzfs-limit-max-snapshots)
fsx-openzfs-limit-max-throughput-capacity
  claim: The maximum throughput capacity of an FSx for OpenZFS file system is 10,240 MBps.
  scope: per file system; maximum; not adjustable.
  link: [10,240 MBps](../facts/fsx.md#fsx-openzfs-limit-max-throughput-capacity)
fsx-openzfs-limit-max-volumes
  claim: The maximum number of volumes per FSx for OpenZFS file system is 100.
  scope: per file system; maximum; not adjustable.
  link: [100](../facts/fsx.md#fsx-openzfs-limit-max-volumes)
fsx-openzfs-limit-min-storage-capacity
  claim: The minimum storage capacity of an FSx for OpenZFS file system is 64 GiB.
  scope: per file system; minimum; not adjustable.
  link: [64 GiB](../facts/fsx.md#fsx-openzfs-limit-min-storage-capacity)
fsx-openzfs-limit-min-throughput-capacity
  claim: The minimum throughput capacity of an FSx for OpenZFS file system is 64 MBps.
  scope: per file system; minimum; not adjustable.
  link: [64 MBps](../facts/fsx.md#fsx-openzfs-limit-min-throughput-capacity)
fsx-openzfs-limit-tags-per-file-system
  claim: The maximum number of tags per FSx for OpenZFS file system is 50.
  scope: per file system; maximum; not adjustable.
  link: [50](../facts/fsx.md#fsx-openzfs-limit-tags-per-file-system)
fsx-openzfs-limit-user-backup-retention
  claim: The maximum retention period for user-initiated backups of an FSx for OpenZFS file system is no retention limit.
  scope: per file system; maximum; not adjustable.
  link: [no retention limit](../facts/fsx.md#fsx-openzfs-limit-user-backup-retention)
fsx-openzfs-limit-user-group-quotas-per-volume
  claim: The maximum number of user and group quotas per FSx for OpenZFS volume is 100.
  scope: per volume; maximum; not adjustable.
  link: [100](../facts/fsx.md#fsx-openzfs-limit-user-group-quotas-per-volume)
fsx-openzfs-migrate-between-deployment-types-backup-rsync-replication
  claim: You can migrate between FSx for OpenZFS deployment types by restoring from a backup, by using rsync, or by using on-demand replication.
  scope: FSx for OpenZFS deployment types.
  link: [restoring from a backup](../facts/fsx.md#fsx-openzfs-migrate-between-deployment-types-backup-rsync-replication)
  link: [using on-demand replication](../facts/fsx.md#fsx-openzfs-migrate-between-deployment-types-backup-rsync-replication)
fsx-openzfs-multi-az-ha-copy-in-each-az-failover-60-seconds
  claim: Multi-AZ (HA) file systems replicate data and support failover across multiple Availability Zones in the same Region, with a separate copy of the data in each Availability Zone, and failover typically completes within 60 seconds.
  scope: FSx for OpenZFS Multi-AZ (HA).
  link: [separate copy of your data](../facts/fsx.md#fsx-openzfs-multi-az-ha-copy-in-each-az-failover-60-seconds)
  link: [Failover typically completes within 60 seconds](../facts/fsx.md#fsx-openzfs-multi-az-ha-copy-in-each-az-failover-60-seconds)
fsx-openzfs-multi-az-recommended-business-critical-database
  claim: Multi-AZ (HA) file systems are recommended for business-critical production workloads and database workloads that need storage that is highly available and durable across Availability Zones in the same Region.
  scope: FSx for OpenZFS Multi-AZ (HA).
  link: [business critical production workloads](../facts/fsx.md#fsx-openzfs-multi-az-recommended-business-critical-database)
  link: [database workloads](../facts/fsx.md#fsx-openzfs-multi-az-recommended-business-critical-database)
fsx-openzfs-multi-az-sync-two-azs-failover-60-seconds
  claim: FSx for OpenZFS Multi-AZ (HA) file systems replicate data synchronously within each Availability Zone and between the two Availability Zones, and fail over to the standby Availability Zone automatically, typically within 60 seconds.
  scope: FSx for OpenZFS Multi-AZ (HA) deployment.
  link: [typically within 60 seconds](../facts/fsx.md#fsx-openzfs-multi-az-sync-two-azs-failover-60-seconds)
  link: [replicating data synchronously](../facts/fsx.md#fsx-openzfs-multi-az-sync-two-azs-failover-60-seconds)
fsx-openzfs-nfs-v3-v4-clients-linux-windows-macos
  claim: Amazon FSx for OpenZFS file systems are accessible from Linux, Windows and macOS compute instances and containers using the NFS protocol (v3, v4.0, v4.1, v4.2).
  scope: Amazon FSx for OpenZFS.
  link: [NFS protocol (v3, v4.0, v4.1, v4.2)](../facts/fsx.md#fsx-openzfs-nfs-v3-v4-clients-linux-windows-macos)
  link: [Linux, Windows, and macOS compute instances](../facts/fsx.md#fsx-openzfs-nfs-v3-v4-clients-linux-windows-macos)
fsx-openzfs-on-demand-replication-snapshots-across-regions-accounts
  claim: FSx for OpenZFS supports on-demand data replication, which transfers snapshots of data between file systems within and across AWS Regions and accounts, and it is available for all deployment types in Regions where FSx for OpenZFS is available.
  scope: FSx for OpenZFS replication.
  link: [transfer snapshots of data between file systems](../facts/fsx.md#fsx-openzfs-on-demand-replication-snapshots-across-regions-accounts)
  link: [within and across AWS Regions and accounts](../facts/fsx.md#fsx-openzfs-on-demand-replication-snapshots-across-regions-accounts)
fsx-openzfs-periodic-replication-schedule-incremental
  claim: With ongoing periodic data replication you can schedule an automatic snapshot of a source volume and an incremental replication of that snapshot to a destination volume at a certain interval, for example every 15 minutes.
  scope: FSx for OpenZFS replication.
  link: [automatically takes a snapshot of a source volume](../facts/fsx.md#fsx-openzfs-periodic-replication-schedule-incremental)
  link: [incremental replication of that snapshot](../facts/fsx.md#fsx-openzfs-periodic-replication-schedule-incremental)
fsx-openzfs-pricing-multi-az-no-transfer-fees
  claim: For FSx for OpenZFS Multi-AZ file systems there are no data transfer fees and cross-AZ data replication costs are included in the throughput capacity price. For Single-AZ file systems you pay for data transfer in both directions when you access the file system from a non-preferred Availability Zone in the same Region.
  scope: FSx for OpenZFS data transfer.
  link: [no data transfer fees](../facts/fsx.md#fsx-openzfs-pricing-multi-az-no-transfer-fees)
fsx-openzfs-pricing-prorated-by-second
  claim: For FSx for OpenZFS, pricing is quoted on a monthly basis, usage is prorated by the second, and you are billed for your average usage over a month.
  scope: FSx for OpenZFS.
  link: [prorated by the second](../facts/fsx.md#fsx-openzfs-pricing-prorated-by-second)
fsx-openzfs-pricing-ssd-iops-included
  claim: For FSx for OpenZFS, 3 IOPS are included for every GB of SSD storage by default.
  scope: per GB of SSD storage; default.
  link: [3 IOPS](../facts/fsx.md#fsx-openzfs-pricing-ssd-iops-included)
fsx-openzfs-quota-backups-per-account
  claim: The default for OpenZFS backups is 10,000, the maximum number of user-initiated backups for all Amazon FSx for OpenZFS file systems that you can have in this account.
  scope: per account, per AWS Region, all OpenZFS file systems; default; adjustable.
  link: [10,000](../facts/fsx.md#fsx-openzfs-quota-backups-per-account)
fsx-openzfs-quota-disk-iops-per-account
  claim: The default for OpenZFS disk IOPS is 400,000, the total amount of disk IOPS allowed for all Amazon FSx for OpenZFS file systems in this account.
  scope: per account, per AWS Region, all OpenZFS file systems; default; adjustable.
  link: [400,000](../facts/fsx.md#fsx-openzfs-quota-disk-iops-per-account)
fsx-openzfs-quota-file-systems-per-account
  claim: The default for OpenZFS file systems is 100, the maximum number of Amazon FSx for OpenZFS file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-openzfs-quota-file-systems-per-account)
fsx-openzfs-quota-ssd-capacity-per-account
  claim: The default for OpenZFS SSD storage capacity is 65,536 (262,144 in US East (N. Virginia), US East (Ohio), and US West (Oregon)), the maximum amount of SSD storage capacity (in GiB) that you can configure for all Amazon FSx for OpenZFS file systems in this account.
  scope: per account, per AWS Region, all OpenZFS file systems; default; adjustable.
  link: [65,536](../facts/fsx.md#fsx-openzfs-quota-ssd-capacity-per-account)
  link: [262,144](../facts/fsx.md#fsx-openzfs-quota-ssd-capacity-per-account)
fsx-openzfs-quota-throughput-capacity-per-account
  claim: The default for OpenZFS throughput capacity is 10,240, the total amount of throughput capacity (in MBps) allowed for all Amazon FSx for OpenZFS file systems in this account.
  scope: per account, per AWS Region, all OpenZFS file systems; default; adjustable.
  link: [10,240](../facts/fsx.md#fsx-openzfs-quota-throughput-capacity-per-account)
fsx-openzfs-record-size-default-intelligent-tiering
  claim: When you create a volume, the default ZFS record size for FSx for OpenZFS file systems using the Intelligent-Tiering storage class is 1024 KiB.
  scope: per volume, Intelligent-Tiering storage class; default; adjustable.
  link: [1024 KiB](../facts/fsx.md#fsx-openzfs-record-size-default-intelligent-tiering)
fsx-openzfs-record-size-default-other
  claim: When you create an FSx for OpenZFS volume, the default ZFS record size is 128 KiB for file systems that do not use the Intelligent-Tiering storage class (Intelligent-Tiering file systems default to 1024 KiB).
  scope: per volume, file systems that do not use Intelligent-Tiering; default; adjustable.
  link: [128 KiB](../facts/fsx.md#fsx-openzfs-record-size-default-other)
fsx-openzfs-replication-use-cases-read-replicas-passive-standby-dr
  claim: On-demand data replication can synchronize data to development or test environments, maintain read replicas for scale-out read performance, and maintain a passive standby file system for disaster recovery.
  scope: FSx for OpenZFS replication.
  link: [maintaining read replicas](../facts/fsx.md#fsx-openzfs-replication-use-cases-read-replicas-passive-standby-dr)
  link: [passive standby file system](../facts/fsx.md#fsx-openzfs-replication-use-cases-read-replicas-passive-standby-dr)
fsx-openzfs-s3-access-points-attach-to-openzfs-volumes
  claim: S3 access points are named network endpoints that attach to either S3 general purpose buckets or FSx for OpenZFS volumes, so applications that work with S3 can use file data on FSx for OpenZFS without changes or moving data out of file storage.
  scope: Amazon FSx for OpenZFS S3 access points.
  link: [access file data stored on Amazon FSx](../facts/fsx.md#fsx-openzfs-s3-access-points-attach-to-openzfs-volumes)
  link: [attach to either S3 general purpose buckets](../facts/fsx.md#fsx-openzfs-s3-access-points-attach-to-openzfs-volumes)
fsx-openzfs-s3-access-points-latency
  claim: Amazon S3 access points for FSx for OpenZFS file systems deliver latency in the tens of milliseconds range, consistent with S3 bucket access.
  scope: S3 access points for FSx for OpenZFS.
  link: [tens of milliseconds](../facts/fsx.md#fsx-openzfs-s3-access-points-latency)
fsx-openzfs-signature-features-compression-snapshots-clones
  claim: FSx for OpenZFS provides OpenZFS data management capabilities including data compression, near instant point-in-time snapshots and data cloning, designed for use with the Amazon FSx API.
  scope: Amazon FSx for OpenZFS.
  link: [data compression, near instant point-in-time snapshots](../facts/fsx.md#fsx-openzfs-signature-features-compression-snapshots-clones)
  link: [data cloning](../facts/fsx.md#fsx-openzfs-signature-features-compression-snapshots-clones)
fsx-openzfs-single-az-2-iops-throughput
  claim: Single-AZ 2 file systems offer double the performance scalability of Single-AZ 1, delivering up to 400,000 IOPS and 10 GBps throughput for both reads and writes to persistent SSD storage.
  scope: per FSx for OpenZFS Single-AZ 2 file system, persistent SSD storage; maximum; not adjustable.
  link: [400,000 IOPS](../facts/fsx.md#fsx-openzfs-single-az-2-iops-throughput)
  link: [10 GBps](../facts/fsx.md#fsx-openzfs-single-az-2-iops-throughput)
fsx-openzfs-single-az-2-nvme-cache
  claim: FSx for OpenZFS Single-AZ 2 file systems include an up to 2.5 TB high-speed NVMe read cache that caches your most recently-accessed data, making that data accessible at millions of IOPS and with latencies of a few hundred microseconds.
  scope: per FSx for OpenZFS Single-AZ 2 file system; maximum.
  link: [2.5 TB](../facts/fsx.md#fsx-openzfs-single-az-2-nvme-cache)
  link: [a few hundred microseconds](../facts/fsx.md#fsx-openzfs-single-az-2-nvme-cache)
fsx-openzfs-single-az-failure-may-be-unrecoverable-restore-backup
  claim: For all Single-AZ file systems, file system failure may be unrecoverable in rare cases, such as storage component failures, and then you recover the file system from the most recent backup.
  scope: FSx for OpenZFS Single-AZ.
  link: [may be unrecoverable in rare cases](../facts/fsx.md#fsx-openzfs-single-az-failure-may-be-unrecoverable-restore-backup)
  link: [from the most recent backup](../facts/fsx.md#fsx-openzfs-single-az-failure-may-be-unrecoverable-restore-backup)
fsx-openzfs-single-az-ha-failover-60-seconds
  claim: FSx for OpenZFS Single-AZ (HA) file systems fail over from the primary file server to the standby file server typically within 60 seconds during planned maintenance events or unplanned service disruptions.
  scope: FSx for OpenZFS Single-AZ (HA) file systems.
  link: [60 seconds](../facts/fsx.md#fsx-openzfs-single-az-ha-failover-60-seconds)
fsx-openzfs-single-az-ha-primary-standby-same-az-60-seconds
  claim: Single-AZ (HA) file systems deploy a primary and a standby file system within the same Availability Zone to give continuous availability during failover and failback, and failover typically completes within 60 seconds.
  scope: FSx for OpenZFS Single-AZ (HA).
  link: [primary and standby file system within](../facts/fsx.md#fsx-openzfs-single-az-ha-primary-standby-same-az-60-seconds)
  link: [Failover typically completes within 60 seconds](../facts/fsx.md#fsx-openzfs-single-az-ha-primary-standby-same-az-60-seconds)
fsx-openzfs-single-az-ha-recommended-analytics-eda
  claim: Single-AZ (HA) file systems are recommended as a cost-effective solution for workloads that need high availability but not storage redundancy across Availability Zones, including analytics and EDA workloads.
  scope: FSx for OpenZFS Single-AZ (HA).
  link: [cost-effective solution for workloads that need high availability](../facts/fsx.md#fsx-openzfs-single-az-ha-recommended-analytics-eda)
  link: [analytics, and EDA workloads](../facts/fsx.md#fsx-openzfs-single-az-ha-recommended-analytics-eda)
fsx-openzfs-single-az-non-ha-cost-efficient-tolerates-downtime
  claim: Single-AZ (non-HA) file systems usually experience about 30 minutes of downtime during failure recovery and the planned maintenance window, and suit workloads that can tolerate temporary loss of availability and, in rare cases, the loss of data updates since the most recent backup.
  scope: FSx for OpenZFS Single-AZ (non-HA).
  link: [about 30 minutes of downtime](../facts/fsx.md#fsx-openzfs-single-az-non-ha-cost-efficient-tolerates-downtime)
  link: [cost-efficient solution for workloads that can tolerate](../facts/fsx.md#fsx-openzfs-single-az-non-ha-cost-efficient-tolerates-downtime)
fsx-openzfs-single-az-non-ha-self-healing-30-minutes
  claim: Single-AZ (non-HA) file systems recover by themselves within a single Availability Zone by detecting and addressing component failures automatically, and recovery typically completes within 30 minutes.
  scope: FSx for OpenZFS Single-AZ (non-HA).
  link: [self-healing recovery within a single Availability Zone](../facts/fsx.md#fsx-openzfs-single-az-non-ha-self-healing-30-minutes)
  link: [Recovery typically completes within 30 minutes](../facts/fsx.md#fsx-openzfs-single-az-non-ha-self-healing-30-minutes)
fsx-openzfs-snapshot-read-only-image-restore-files
  claim: A snapshot is a read-only image of an FSx for OpenZFS volume at a point in time, and with snapshots users can view and restore individual folders and files from an earlier snapshot.
  scope: FSx for OpenZFS snapshots.
  link: [read-only image of an FSx for OpenZFS volume](../facts/fsx.md#fsx-openzfs-snapshot-read-only-image-restore-files)
  link: [restore individual folders and files](../facts/fsx.md#fsx-openzfs-snapshot-read-only-image-restore-files)
fsx-openzfs-ssd-utilization-below-80
  claim: The recommendation is to keep storage utilization of SSD (provisioned) FSx for OpenZFS file systems below 80% of the total capacity.
  scope: per SSD (provisioned) file system; maximum; not adjustable.
  link: [below 80%](../facts/fsx.md#fsx-openzfs-ssd-utilization-below-80)
fsx-openzfs-three-deployment-types-multi-az-single-az-ha-non-ha
  claim: FSx for OpenZFS supports three file system deployment types, Multi-AZ (HA), Single-AZ (HA) and Single-AZ (non-HA), each with a different level of availability and durability.
  scope: Amazon FSx for OpenZFS.
  link: [Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA)](../facts/fsx.md#fsx-openzfs-three-deployment-types-multi-az-single-az-ha-non-ha)
  link: [three file system deployment types](../facts/fsx.md#fsx-openzfs-three-deployment-types-multi-az-single-az-ha-non-ha)
fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd
  claim: FSx for OpenZFS has two storage classes: Intelligent-Tiering, where you are billed for the data you store and do not specify a file system size, and SSD, where you specify a file system size and pay for the storage you provision.
  scope: FSx for OpenZFS storage classes.
  link: [fully elastic, cost-effective storage](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
  link: [do not need to specify](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
  link: [pay for the amount of storage](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
fsx-openzfs-volumes-thin-provisioning-user-group-quotas
  claim: FSx for OpenZFS supports multiple volumes per file system, thin provisioning, and user and group quotas for cost-efficient shared file systems across multiple users and applications.
  scope: Amazon FSx for OpenZFS.
  link: [multiple volumes per file system](../facts/fsx.md#fsx-openzfs-volumes-thin-provisioning-user-group-quotas)
  link: [user and group quotas](../facts/fsx.md#fsx-openzfs-volumes-thin-provisioning-user-group-quotas)
fsx-openzfs-what-is-nfs-clients-snapshots-clones
  claim: FSx for OpenZFS file systems are accessible from Linux, Windows and macOS compute instances and containers through the industry-standard NFS protocol, and support OpenZFS features such as instant point-in-time snapshots and data cloning.
  scope: FSx for OpenZFS.
  link: [industry-standard NFS protocol](../facts/fsx.md#fsx-openzfs-what-is-nfs-clients-snapshots-clones)
  link: [instant point-in-time snapshots and data cloning](../facts/fsx.md#fsx-openzfs-what-is-nfs-clients-snapshots-clones)
fsx-overview-lustre-s3-integration-hpc
  claim: The AWS overview whitepaper says FSx for Lustre is seamlessly integrated with Amazon S3, so you can link long-term data sets with high-performance file systems for compute-intensive workloads.
  scope: Amazon FSx for Lustre.
  link: [seamlessly integrated with Amazon S3](../facts/fsx.md#fsx-overview-lustre-s3-integration-hpc)
fsx-overview-ontap-multiprotocol-nfs-smb-iscsi
  claim: The AWS overview whitepaper says FSx for NetApp ONTAP offers high-performance file storage accessible from Linux, Windows and macOS compute instances through the NFS, SMB and iSCSI protocols.
  scope: Amazon FSx for NetApp ONTAP.
  link: [Linux, Windows, and macOS](../facts/fsx.md#fsx-overview-ontap-multiprotocol-nfs-smb-iscsi)
  link: [NFS, SMB, and iSCSI](../facts/fsx.md#fsx-overview-ontap-multiprotocol-nfs-smb-iscsi)
fsx-overview-openzfs-migrate-without-changing-apps
  claim: The AWS overview whitepaper says FSx for OpenZFS makes it easy to migrate on-premises file servers without changing your applications or how you manage data.
  scope: Amazon FSx for OpenZFS.
  link: [without changing your applications](../facts/fsx.md#fsx-overview-openzfs-migrate-without-changing-apps)
fsx-overview-windows-smb-ntfs-ad-dfs
  claim: The AWS overview whitepaper says FSx for Windows File Server is built on Windows Server and supports the SMB protocol and Windows NTFS, Active Directory integration and Distributed File System (DFS).
  scope: Amazon FSx for Windows File Server.
  link: [the SMB protocol and Windows NTFS](../facts/fsx.md#fsx-overview-windows-smb-ntfs-ad-dfs)
  link: [Distributed File System (DFS)](../facts/fsx.md#fsx-overview-windows-smb-ntfs-ad-dfs)
fsx-when-to-choose-lustre-from-parallel-fs
  claim: The AWS page on choosing an FSx file system recommends FSx for Lustre when your current storage technology is Lustre or another parallel file system.
  scope: FSx file system choice by current storage technology.
  link: [FSx for Lustre](../facts/fsx.md#fsx-when-to-choose-lustre-from-parallel-fs)
fsx-when-to-choose-ontap-from-nas
  claim: The AWS page on choosing an FSx file system recommends FSx for NetApp ONTAP when your current storage technology is NetApp ONTAP or another NAS appliance.
  scope: FSx file system choice by current storage technology.
  link: [FSx for NetApp ONTAP](../facts/fsx.md#fsx-when-to-choose-ontap-from-nas)
fsx-when-to-choose-openzfs-from-zfs
  claim: The AWS page on choosing an FSx file system recommends FSx for OpenZFS when your current storage technology is ZFS or another Linux-based file server.
  scope: FSx file system choice by current storage technology.
  link: [FSx for OpenZFS](../facts/fsx.md#fsx-when-to-choose-openzfs-from-zfs)
fsx-when-to-choose-windows-from-windows-server
  claim: The AWS page on choosing an FSx file system recommends FSx for Windows File Server when your current storage technology is Microsoft Windows Server.
  scope: FSx file system choice by current storage technology.
  link: [FSx for Windows File Server](../facts/fsx.md#fsx-when-to-choose-windows-from-windows-server)
fsx-windows-access-control-acls-security-groups-iam-ad
  claim: FSx for Windows File Server gives file- and folder-level access control with Windows ACLs, file system-level access control with VPC security groups, and API-level access control with IAM policies, and users are authenticated with Microsoft Active Directory.
  scope: Amazon FSx for Windows File Server.
  link: [Windows access control lists (ACLs)](../facts/fsx.md#fsx-windows-access-control-acls-security-groups-iam-ad)
  link: [Amazon Virtual Private Cloud (Amazon VPC) security groups](../facts/fsx.md#fsx-windows-access-control-acls-security-groups-iam-ad)
fsx-windows-ad-connector-simple-ad-not-supported
  claim: Amazon FSx does not support Active Directory Connector and Simple Active Directory.
  scope: Amazon FSx for Windows File Server.
  link: [does not support](../facts/fsx.md#fsx-windows-ad-connector-simple-ad-not-supported)
  link: [Amazon FSx does not support](../facts/fsx.md#fsx-windows-ad-connector-simple-ad-not-supported)
fsx-windows-ad-options-aws-managed-or-self-managed
  claim: You can join an FSx for Windows File Server file system to AWS Managed Microsoft AD or to your existing self-managed Active Directory domain, on-premises or in the cloud.
  scope: Amazon FSx for Windows File Server.
  link: [integrate your Amazon FSx file system](../facts/fsx.md#fsx-windows-ad-options-aws-managed-or-self-managed)
  link: [existing, self-managed Active Directory domain](../facts/fsx.md#fsx-windows-ad-options-aws-managed-or-self-managed)
fsx-windows-automatic-backups-deleted-with-file-system
  claim: Automatic daily backups of an FSx for Windows File Server file system are deleted when the file system is deleted.
  scope: FSx for Windows File Server backups.
  link: [deleted when the file system is deleted](../facts/fsx.md#fsx-windows-automatic-backups-deleted-with-file-system)
  link: [Automatic daily backups](../facts/fsx.md#fsx-windows-automatic-backups-deleted-with-file-system)
fsx-windows-automatic-storage-increase-solution-cloudformation
  claim: You can automatically increase an FSx for Windows File Server file system's storage capacity when free storage capacity falls below a threshold that you specify, by deploying the AWS-developed custom CloudFormation template that implements the automated solution.
  scope: FSx for Windows File Server storage capacity.
  link: [automatically increase your file system's storage capacity](../facts/fsx.md#fsx-windows-automatic-storage-increase-solution-cloudformation)
  link: [falls below a defined threshold](../facts/fsx.md#fsx-windows-automatic-storage-increase-solution-cloudformation)
  link: [custom CloudFormation template](../facts/fsx.md#fsx-windows-automatic-storage-increase-solution-cloudformation)
fsx-windows-aws-backup-centralized-backup-option
  claim: For FSx for Windows File Server you can use AWS Backup as part of a centralized backup solution for your AWS resources.
  scope: FSx for Windows File Server backups.
  link: [use AWS Backup as part of](../facts/fsx.md#fsx-windows-aws-backup-centralized-backup-option)
  link: [centralized backup solution](../facts/fsx.md#fsx-windows-aws-backup-centralized-backup-option)
fsx-windows-backup-brief-io-pause-seconds
  claim: During an FSx for Windows File Server backup, storage I/O may be suspended briefly, typically for a few seconds; because the VSS service needs to flush any cached writes to disk before resuming I/O, the pause may be longer when the workload has many write operations per second.
  scope: FSx for Windows File Server backups.
  link: [storage I/O may be suspended briefly](../facts/fsx.md#fsx-windows-backup-brief-io-pause-seconds)
  link: [typically for a few seconds](../facts/fsx.md#fsx-windows-backup-brief-io-pause-seconds)
fsx-windows-backup-copy-cross-region-and-aws-backup-cross-account
  claim: You can use Amazon FSx to copy FSx for Windows File Server backups within the same account to another Region or within the same Region (cross-Region copies only within the same AWS partition), and you can use AWS Backup to copy backups across Regions and across accounts.
  scope: FSx for Windows File Server backups.
  link: [another AWS Region (cross-Region copies)](../facts/fsx.md#fsx-windows-backup-copy-cross-region-and-aws-backup-cross-account)
  link: [across AWS Regions and across AWS accounts](../facts/fsx.md#fsx-windows-backup-copy-cross-region-and-aws-backup-cross-account)
fsx-windows-backup-default-retention-console
  claim: When you create an FSx for Windows file system in the Amazon FSx console, the default automatic daily backup retention period is 30 days.
  scope: per file system, created in the Amazon FSx console; default; adjustable; the default differs in the Amazon FSx API and CLI.
  link: [30 days](../facts/fsx.md#fsx-windows-backup-default-retention-console)
fsx-windows-backup-retention-range
  claim: You can set the automatic daily backup retention period of an FSx for Windows file system to be between 0–90 days.
  scope: per file system; maximum; adjustable.
  link: [0–90 days](../facts/fsx.md#fsx-windows-backup-retention-range)
fsx-windows-backup-retention-zero-off
  claim: Setting the retention period to 0 (zero) days turns off automatic daily backups of an FSx for Windows file system.
  scope: per file system.
  link: [0 (zero) days](../facts/fsx.md#fsx-windows-backup-retention-zero-off)
fsx-windows-backups-file-system-consistent-incremental-stored-in-s3
  claim: FSx for Windows File Server backups are file-system-consistent (using VSS), highly durable and incremental, and Amazon FSx stores them in Amazon S3.
  scope: FSx for Windows File Server backups.
  link: [file-system-consistent, highly durable, and incremental](../facts/fsx.md#fsx-windows-backups-file-system-consistent-incremental-stored-in-s3)
  link: [stores backups in Amazon Simple Storage Service](../facts/fsx.md#fsx-windows-backups-file-system-consistent-incremental-stored-in-s3)
fsx-windows-bp-ad-misconfigured-status-risk
  claim: For FSx for Windows File Server with a self-managed Active Directory, FSx rejoins the file server to Active Directory during failure recovery, routine maintenance and throughput capacity updates. If the Active Directory configuration is not valid during such an event, the file system changes to the Misconfigured status and is at risk of becoming unavailable.
  scope: FSx for Windows File Server self-managed Active Directory.
  link: [at risk of becoming unavailable](../facts/fsx.md#fsx-windows-bp-ad-misconfigured-status-risk)
fsx-windows-bp-dont-change-system-user-ntfs-permissions
  claim: FSx for Windows File Server requires that the SYSTEM user have full control NTFS ACL permissions on all folders in the file system; changing them may make the file system inaccessible and future backups unusable.
  scope: FSx for Windows File Server NTFS ACLs.
  link: [full control NTFS ACL permissions on all folders](../facts/fsx.md#fsx-windows-bp-dont-change-system-user-ntfs-permissions)
fsx-windows-bp-dont-modify-delete-eni
  claim: AWS says not to modify or delete the elastic network interface (ENI) that is associated with an FSx for Windows File Server file system, because doing so can cause a permanent loss of connection between your VPC and the file system.
  scope: FSx for Windows File Server network security.
  link: [permanent loss of connection between your VPC](../facts/fsx.md#fsx-windows-bp-dont-modify-delete-eni)
fsx-windows-bp-join-active-directory-two-options
  claim: You can join an FSx for Windows File Server file system to your Microsoft Active Directory domain to provide user authentication and share-, file- and folder-level access control. FSx provides two Active Directory options: AWS managed Microsoft Active Directory or self-managed Microsoft Active Directory.
  scope: FSx for Windows File Server Active Directory.
  link: [AWS managed Microsoft Active Directory](../facts/fsx.md#fsx-windows-bp-join-active-directory-two-options)
  link: [self-managed Microsoft Active Directory](../facts/fsx.md#fsx-windows-bp-join-active-directory-two-options)
fsx-windows-bp-keep-20-percent-free-storage
  claim: AWS recommends keeping at least 20% of free storage capacity at all times on an FSx for Windows File Server file system, and increasing throughput capacity by at least 20% before increasing storage capacity to offset any performance impact during the storage increase.
  scope: FSx for Windows File Server capacity planning.
  link: [at least 20% of free storage capacity at all times](../facts/fsx.md#fsx-windows-bp-keep-20-percent-free-storage)
fsx-windows-bp-monitor-free-storage-capacity-metric
  claim: You can use the FreeStorageCapacity CloudWatch metric to monitor the amount of free storage available on an FSx for Windows File Server file system and see how it trends.
  scope: FSx for Windows File Server monitoring.
  link: [FreeStorageCapacity](../facts/fsx.md#fsx-windows-bp-monitor-free-storage-capacity-metric)
fsx-windows-bp-multi-az-for-most-production-workloads
  claim: AWS recommends Multi-AZ file systems for most FSx for Windows File Server production workloads that require high availability to shared Windows file data.
  scope: FSx for Windows File Server deployment types.
  link: [Multi-AZ file systems](../facts/fsx.md#fsx-windows-bp-multi-az-for-most-production-workloads)
fsx-windows-bp-secrets-manager-for-ad-credentials
  claim: You can use AWS Secrets Manager to store and manage the Microsoft Active Directory domain join service account credentials for FSx for Windows File Server, which removes the need to store sensitive credentials in plaintext in application code or configuration files.
  scope: FSx for Windows File Server self-managed Active Directory.
  link: [AWS Secrets Manager](../facts/fsx.md#fsx-windows-bp-secrets-manager-for-ad-credentials)
fsx-windows-bp-security-groups-and-network-acls-limit-access
  claim: You can use security groups and network access control lists (ACLs) to limit access to FSx for Windows File Server file systems, and the security group and network ACLs for the subnets must allow traffic on the required ports.
  scope: FSx for Windows File Server network security.
  link: [security groups and network access control lists (ACLs)](../facts/fsx.md#fsx-windows-bp-security-groups-and-network-acls-limit-access)
fsx-windows-bp-self-managed-ad-least-privilege-service-account
  claim: For FSx for Windows File Server with a self-managed Active Directory, AWS recommends a separate Organizational Unit for the file systems and a service account configured with the minimum privileges required.
  scope: FSx for Windows File Server self-managed Active Directory.
  link: [minimum privileges required](../facts/fsx.md#fsx-windows-bp-self-managed-ad-least-privilege-service-account)
fsx-windows-bp-shadow-copies-three-times-throughput
  claim: If you use shadow copies on FSx for Windows File Server, AWS recommends increasing throughput capacity to a value at least three times the value that your workload is expected to drive, to avoid Windows Server deleting your shadow copies.
  scope: FSx for Windows File Server shadow copies.
  link: [at least three times the value](../facts/fsx.md#fsx-windows-bp-shadow-copies-three-times-throughput)
fsx-windows-bp-throughput-update-interrupts-single-az-failover-multi-az
  claim: Updating throughput capacity of an FSx for Windows File Server file system interrupts availability for a few minutes on Single-AZ file systems and causes failover and failback on Multi-AZ file systems, so AWS recommends doing it during idle periods.
  scope: FSx for Windows File Server throughput capacity updates.
  link: [interrupts availability for a few minutes](../facts/fsx.md#fsx-windows-bp-throughput-update-interrupts-single-az-failover-multi-az)
fsx-windows-bp-windows-acls-enforced-existing-acls-migrate
  claim: FSx for Windows File Server uses standard Windows access control lists (ACLs) for fine-grained share-, file- and folder-level access control, and automatically verifies the credentials of users who access file system data to enforce them. You can migrate an existing security ACL configuration without modifications.
  scope: FSx for Windows File Server access control.
  link: [standard Windows access control lists (ACLs)](../facts/fsx.md#fsx-windows-bp-windows-acls-enforced-existing-acls-migrate)
fsx-windows-ca-shares-required-multi-az-for-sql-server
  claim: For Microsoft SQL Server, FSx for Windows File Server supports continuously available (CA) file shares. You can create CA shares on Single-AZ 2 file systems, but it is required that you use CA shares on Multi-AZ file systems for all SQL Server deployments, whether HA or not.
  scope: FSx for Windows File Server with Microsoft SQL Server.
  link: [continuously available (CA) file shares](../facts/fsx.md#fsx-windows-ca-shares-required-multi-az-for-sql-server)
  link: [use CA shares on Multi-AZ file systems](../facts/fsx.md#fsx-windows-ca-shares-required-multi-az-for-sql-server)
fsx-windows-clients-windows-and-linux-instances-workspaces-appstream-vmware
  claim: You can access FSx for Windows File Server shares from all Windows versions starting from Windows Server 2008 and Windows 7 and from current versions of Linux, and you can map them on EC2 instances, WorkSpaces instances, AppStream 2.0 instances and VMware Cloud on AWS VMs.
  scope: Amazon FSx for Windows File Server clients.
  link: [current versions of Linux](../facts/fsx.md#fsx-windows-clients-windows-and-linux-instances-workspaces-appstream-vmware)
  link: [VMware Cloud on AWS VMs](../facts/fsx.md#fsx-windows-clients-windows-and-linux-instances-workspaces-appstream-vmware)
  link: [starting from Windows Server 2008](../facts/fsx.md#fsx-windows-clients-windows-and-linux-instances-workspaces-appstream-vmware)
fsx-windows-dedup-background-transparent-compression-default
  claim: Data deduplication on FSx for Windows File Server runs as a background process that is transparent to users, and when you enable it data compression is enabled by default.
  scope: FSx for Windows File Server data deduplication.
  link: [Data compression is enabled by default](../facts/fsx.md#fsx-windows-dedup-background-transparent-compression-default)
  link: [runs as a background process](../facts/fsx.md#fsx-windows-dedup-background-transparent-compression-default)
fsx-windows-dedup-typical-savings-50-60-percent
  claim: Data deduplication on FSx for Windows File Server typically saves 50 to 60 percent for general-purpose file shares, with 30 to 50 percent for user documents and 70 to 80 percent for software development datasets.
  scope: FSx for Windows File Server data deduplication.
  link: [50–60 percent for general-purpose file shares](../facts/fsx.md#fsx-windows-dedup-typical-savings-50-60-percent)
  link: [30–50 percent for user documents](../facts/fsx.md#fsx-windows-dedup-typical-savings-50-60-percent)
fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib
  claim: With Microsoft DFS Namespaces you can group file shares on multiple FSx for Windows File Server file systems into one namespace and scale file storage beyond the 64 TiB maximum of a single file system, up to hundreds of petabytes.
  scope: FSx for Windows File Server DFS Namespaces.
  link: [maximum storage capacity of single file system (64 TiB)](../facts/fsx.md#fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib)
  link: [one common folder structure, or namespace](../facts/fsx.md#fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib)
fsx-windows-dfs-shards-scale-out-read-write-performance
  claim: By using DFS Namespaces you can scale out read and write performance for I/O-intensive workloads by spreading file data (shards) across multiple FSx file systems under one unified namespace.
  scope: FSx for Windows File Server DFS Namespaces.
  link: [scale out performance (both read and write)](../facts/fsx.md#fsx-windows-dfs-shards-scale-out-read-write-performance)
  link: [spreading your file data across multiple](../facts/fsx.md#fsx-windows-dfs-shards-scale-out-read-write-performance)
fsx-windows-dns-aliases-keep-existing-names
  claim: Using DNS aliases, you can move Windows file share data to FSx for Windows File Server and continue to use the existing DNS names to access the data.
  scope: Amazon FSx for Windows File Server DNS aliases.
  link: [continue using the existing DNS names](../facts/fsx.md#fsx-windows-dns-aliases-keep-existing-names)
  link: [Using DNS aliases](../facts/fsx.md#fsx-windows-dns-aliases-keep-existing-names)
fsx-windows-dns-name-per-file-system-microsoft-dns
  claim: Amazon FSx registers DNS records for an FSx for Windows File Server file system only if you are using Microsoft DNS as the default DNS; if you are using a third-party DNS, you must manually set up DNS entries for your file systems.
  scope: Amazon FSx for Windows File Server.
  link: [only registers DNS records for a file system](../facts/fsx.md#fsx-windows-dns-name-per-file-system-microsoft-dns)
  link: [manually set up DNS entries](../facts/fsx.md#fsx-windows-dns-name-per-file-system-microsoft-dns)
fsx-windows-encrypted-at-rest-always-kms-aes-256
  claim: All Amazon FSx file systems are encrypted at rest with keys managed in AWS KMS, using the AES-256 algorithm, and data is encrypted and decrypted transparently.
  scope: Amazon FSx for Windows File Server encryption.
  link: [encrypted at rest with keys managed](../facts/fsx.md#fsx-windows-encrypted-at-rest-always-kms-aes-256)
  link: [industry-standard AES-256 encryption algorithm](../facts/fsx.md#fsx-windows-encrypted-at-rest-always-kms-aes-256)
fsx-windows-encrypted-in-transit-smb-kerberos-session-keys
  claim: Data in transit to FSx for Windows File Server is automatically encrypted using SMB Kerberos session keys.
  scope: Amazon FSx for Windows File Server encryption.
  link: [automatically encrypted using SMB Kerberos session keys](../facts/fsx.md#fsx-windows-encrypted-in-transit-smb-kerberos-session-keys)
  link: [Data in transit](../facts/fsx.md#fsx-windows-encrypted-in-transit-smb-kerberos-session-keys)
fsx-windows-failover-io-paused-resync-hours-hdd
  claim: While a Multi-AZ file system fails over and back, I/O may be paused and CloudWatch metrics may be temporarily unavailable, and synchronizing activity during that time can take up to multiple hours for HDD storage and for write-heavy, IOPS-heavy workloads.
  scope: FSx for Windows File Server Multi-AZ.
  link: [I/O may be paused](../facts/fsx.md#fsx-windows-failover-io-paused-resync-hours-hdd)
  link: [multiple hours for file systems with HDD](../facts/fsx.md#fsx-windows-failover-io-paused-resync-hours-hdd)
fsx-windows-failover-transparent-same-dns-name
  claim: Because the file system's DNS name stays the same, failovers are transparent to Windows applications, which resume file system operations without manual intervention.
  scope: FSx for Windows File Server Multi-AZ.
  link: [DNS name remains the same](../facts/fsx.md#fsx-windows-failover-transparent-same-dns-name)
  link: [transparent to Windows applications](../facts/fsx.md#fsx-windows-failover-transparent-same-dns-name)
fsx-windows-failover-triggers-az-outage-unavailable-maintenance
  claim: A Multi-AZ FSx for Windows file system fails over automatically from the preferred to the standby file server when an Availability Zone outage occurs, when the preferred file server becomes unavailable, or when it undergoes planned maintenance.
  scope: FSx for Windows File Server Multi-AZ.
  link: [An Availability Zone outage occurs](../facts/fsx.md#fsx-windows-failover-triggers-az-outage-unavailable-maintenance)
  link: [The preferred file server becomes unavailable](../facts/fsx.md#fsx-windows-failover-triggers-az-outage-unavailable-maintenance)
  link: [undergoes planned maintenance](../facts/fsx.md#fsx-windows-failover-triggers-az-outage-unavailable-maintenance)
fsx-windows-failover-under-30-seconds-failback-automatic
  claim: A failover of a Multi-AZ FSx for Windows file system typically completes in less than 30 seconds, and failback to the preferred file server is automatic and also takes less than 30 seconds once the preferred file server has recovered.
  scope: FSx for Windows File Server Multi-AZ.
  link: [less than 30 seconds](../facts/fsx.md#fsx-windows-failover-under-30-seconds-failback-automatic)
  link: [promotion of the standby file server](../facts/fsx.md#fsx-windows-failover-under-30-seconds-failback-automatic)
fsx-windows-faq-workloads-crm-erp-dotnet-home-dirs
  claim: The FSx for Windows File Server FAQ says the service was designed for use cases that need Windows shared file storage, such as CRM, ERP, custom or .NET applications, home directories, web serving and content management, and Microsoft SQL Server.
  scope: FSx for Windows File Server.
  link: [Windows shared file storage](../facts/fsx.md#fsx-windows-faq-workloads-crm-erp-dotnet-home-dirs)
fsx-windows-filegateway-closed-to-new-customers
  claim: Amazon FSx File Gateway is no longer available to new customers, and existing customers can continue to use it normally.
  scope: Amazon FSx File Gateway.
  link: [no longer available to new customers](../facts/fsx.md#fsx-windows-filegateway-closed-to-new-customers)
  link: [continue to use the service normally](../facts/fsx.md#fsx-windows-filegateway-closed-to-new-customers)
fsx-windows-fully-managed-native-windows-file-servers-smb
  claim: Amazon FSx for Windows File Server provides fully managed Microsoft Windows file servers backed by a fully native Windows file system, and it supports the SMB protocol to access file storage over a network.
  scope: Amazon FSx for Windows File Server.
  link: [fully managed Microsoft Windows file servers](../facts/fsx.md#fsx-windows-fully-managed-native-windows-file-servers-smb)
  link: [Server Message Block (SMB) protocol](../facts/fsx.md#fsx-windows-fully-managed-native-windows-file-servers-smb)
fsx-windows-joins-active-directory-for-authentication-and-acls
  claim: When you create an FSx for Windows File Server file system you join it to your Active Directory domain, which provides user authentication and file- and folder-level access control.
  scope: Amazon FSx for Windows File Server.
  link: [join it to your Active Directory domain](../facts/fsx.md#fsx-windows-joins-active-directory-for-authentication-and-acls)
  link: [user authentication and file- and folder-level access control](../facts/fsx.md#fsx-windows-joins-active-directory-for-authentication-and-acls)
fsx-windows-keep-20-percent-free-storage
  claim: AWS recommends keeping at least 20% of free storage capacity on an FSx for Windows File Server file system at all times, because using all of it can hurt performance and might introduce data inconsistencies.
  scope: FSx for Windows File Server storage capacity.
  link: [at least 20% of free storage capacity](../facts/fsx.md#fsx-windows-keep-20-percent-free-storage)
  link: [introduce data inconsistencies](../facts/fsx.md#fsx-windows-keep-20-percent-free-storage)
fsx-windows-latency-cache-sub-millisecond
  claim: FSx for Windows File Server file servers use a fast in-memory cache to achieve consistent sub-millisecond latencies for actively accessed data.
  scope: FSx for Windows File Server, data in the in-memory cache.
  link: [consistent sub-millisecond latencies](../facts/fsx.md#fsx-windows-latency-cache-sub-millisecond)
fsx-windows-latency-ssd-vs-hdd
  claim: For data not in the in-memory cache, FSx for Windows File Server provides sub-millisecond file operation latencies with SSD storage and single-digit millisecond latencies with HDD storage.
  scope: FSx for Windows File Server, data not in the in-memory cache.
  link: [sub-millisecond](../facts/fsx.md#fsx-windows-latency-ssd-vs-hdd)
  link: [single-digit millisecond](../facts/fsx.md#fsx-windows-latency-ssd-vs-hdd)
fsx-windows-limit-automated-backup-retention
  claim: The maximum retention period for automated backups of an FSx for Windows File Server file system is 90 days.
  scope: per file system; maximum; not adjustable.
  link: [90 days](../facts/fsx.md#fsx-windows-limit-automated-backup-retention)
fsx-windows-limit-backup-copies-in-progress
  claim: The maximum number of backup copy requests in progress to a single destination Region per account is 5.
  scope: per account, per destination Region; maximum; not adjustable.
  link: [5](../facts/fsx.md#fsx-windows-limit-backup-copies-in-progress)
fsx-windows-limit-max-file-shares
  claim: The maximum number of file shares of an FSx for Windows File Server file system is 100,000.
  scope: per file system; maximum; not adjustable.
  link: [100,000](../facts/fsx.md#fsx-windows-limit-max-file-shares)
fsx-windows-limit-max-ssd-iops
  claim: The maximum SSD IOPS of an FSx for Windows File Server file system is 400,000; FSx file systems provide 400,000 IOPS in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo) and Asia Pacific (Singapore), and up to 80,000 IOPS in all AWS Regions where Amazon FSx is available.
  scope: per file system; maximum; not adjustable.
  link: [400,000](../facts/fsx.md#fsx-windows-limit-max-ssd-iops)
fsx-windows-limit-max-storage-capacity
  claim: The maximum storage capacity of an FSx for Windows SSD or HDD file system is 64 TiB.
  scope: per file system, SSD and HDD; maximum; not adjustable.
  link: [64 TiB](../facts/fsx.md#fsx-windows-limit-max-storage-capacity)
fsx-windows-limit-max-throughput-capacity
  claim: The maximum throughput capacity of an FSx for Windows File Server file system is 12,288 MBps; throughput capacity levels of 4,608 MBps and higher are supported only in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo) and Asia Pacific (Singapore).
  scope: per file system; maximum; not adjustable.
  link: [12,288 MBps](../facts/fsx.md#fsx-windows-limit-max-throughput-capacity)
fsx-windows-limit-min-hdd-capacity
  claim: The minimum storage capacity of an FSx for Windows HDD file system is 2,000 GiB.
  scope: per HDD file system; minimum; not adjustable.
  link: [2,000 GiB](../facts/fsx.md#fsx-windows-limit-min-hdd-capacity)
fsx-windows-limit-min-ssd-capacity
  claim: The minimum storage capacity of an FSx for Windows SSD file system is 32 GiB.
  scope: per SSD file system; minimum; not adjustable.
  link: [32 GiB](../facts/fsx.md#fsx-windows-limit-min-ssd-capacity)
fsx-windows-limit-min-ssd-iops
  claim: The minimum SSD IOPS of an FSx for Windows File Server file system is 96.
  scope: per file system; minimum; not adjustable.
  link: [96](../facts/fsx.md#fsx-windows-limit-min-ssd-iops)
fsx-windows-limit-min-throughput-capacity
  claim: The minimum throughput capacity of an FSx for Windows File Server file system is 8 MBps.
  scope: per file system; minimum; not adjustable.
  link: [8 MBps](../facts/fsx.md#fsx-windows-limit-min-throughput-capacity)
fsx-windows-limit-tags-per-file-system
  claim: The maximum number of tags per FSx for Windows File Server file system is 50.
  scope: per file system; maximum; not adjustable.
  link: [50](../facts/fsx.md#fsx-windows-limit-tags-per-file-system)
fsx-windows-linux-clients-no-automatic-dns-failover
  claim: Linux clients do not support automatic DNS-based failover, so they don't automatically connect to the standby file server during a failover; they automatically resume file system operations after the Multi-AZ file system has failed back to the file server in the preferred subnet.
  scope: FSx for Windows File Server Multi-AZ.
  link: [do not support automatic DNS-based failover](../facts/fsx.md#fsx-windows-linux-clients-no-automatic-dns-failover)
  link: [resume file system operations](../facts/fsx.md#fsx-windows-linux-clients-no-automatic-dns-failover)
fsx-windows-managed-ad-other-vpc-or-account-needs-connectivity
  claim: If you connect an FSx for Windows File Server file system to an AWS Managed Microsoft AD in a different VPC or account, you must ensure connectivity between that VPC and the VPC where you create the file system.
  scope: Amazon FSx for Windows File Server.
  link: [in a different VPC or account](../facts/fsx.md#fsx-windows-managed-ad-other-vpc-or-account-needs-connectivity)
  link: [ensure connectivity between that VPC](../facts/fsx.md#fsx-windows-managed-ad-other-vpc-or-account-needs-connectivity)
fsx-windows-migrate-use-ssd-then-hdd-via-backup
  claim: To migrate large amounts of data to FSx for Windows File Server as quickly as possible, use a file system configured with SSD storage, and afterwards you can move the data to HDD storage if that suits your application.
  scope: FSx for Windows File Server migration.
  link: [configured with solid state drive (SSD) storage](../facts/fsx.md#fsx-windows-migrate-use-ssd-then-hdd-via-backup)
  link: [as quickly as possible](../facts/fsx.md#fsx-windows-migrate-use-ssd-then-hdd-via-backup)
fsx-windows-migrate-with-datasync-or-robocopy
  claim: To migrate existing files to FSx for Windows File Server, AWS recommends AWS DataSync, and as an alternative you can use Robocopy.
  scope: FSx for Windows File Server migration.
  link: [we recommend using AWS DataSync](../facts/fsx.md#fsx-windows-migrate-with-datasync-or-robocopy)
  link: [you can use Robust File Copy, or Robocopy](../facts/fsx.md#fsx-windows-migrate-with-datasync-or-robocopy)
fsx-windows-multi-az-enhanced-durability-availability-auto-failover
  claim: Compared with Single-AZ, Multi-AZ deployments give enhanced durability by replicating data across AZs, and enhanced availability by failing over automatically to the standby AZ during planned maintenance and unplanned disruption.
  scope: FSx for Windows File Server Multi-AZ.
  link: [enhanced durability by further replicating data across AZs](../facts/fsx.md#fsx-windows-multi-az-enhanced-durability-availability-auto-failover)
  link: [failing over automatically to the standby AZ](../facts/fsx.md#fsx-windows-multi-az-enhanced-durability-availability-auto-failover)
fsx-windows-multi-az-feature-row-hdd-ca-shares
  claim: In the feature support table for FSx for Windows File Server, the Multi-AZ deployment type is marked for SSD storage, HDD storage, DFS namespaces, custom DNS names and CA shares, and has no mark for DFS replication; a note on the CA shares mark says you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.
  scope: FSx for Windows File Server deployment type.
  link: [Multi-AZ](../facts/fsx.md#fsx-windows-multi-az-feature-row-hdd-ca-shares)
fsx-windows-multi-az-recommended-production-single-az-dev-test
  claim: AWS recommends Multi-AZ file systems for most production workloads, and describes Single-AZ as a cost-efficient solution for test and development workloads and for production workloads with replication in the application layer or relaxed availability and RPO needs.
  scope: FSx for Windows File Server deployment types.
  link: [Multi-AZ file systems for most production workloads](../facts/fsx.md#fsx-windows-multi-az-recommended-production-single-az-dev-test)
  link: [cost-efficient solution for test and development workloads](../facts/fsx.md#fsx-windows-multi-az-recommended-production-single-az-dev-test)
fsx-windows-multi-az-standby-two-azs-sync-replication
  claim: A Multi-AZ FSx for Windows file system is a high-availability cluster of Windows file servers across two Availability Zones (a preferred and a standby AZ) using Windows Server Failover Clustering, and data is replicated synchronously within each AZ and between the two AZs.
  scope: FSx for Windows File Server Multi-AZ.
  link: [a preferred AZ and a standby AZ](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
  link: [replicated synchronously within each individual AZ](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
  link: [Windows Server Failover Clustering](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
fsx-windows-other-smb-clients-not-supported-by-aws
  claim: Other SMB-compatible clients may function with FSx for Windows File Server, but they are not supported by AWS.
  scope: Amazon FSx for Windows File Server clients.
  link: [may function but are not supported by AWS](../facts/fsx.md#fsx-windows-other-smb-clients-not-supported-by-aws)
  link: [Other SMB-compatible clients](../facts/fsx.md#fsx-windows-other-smb-clients-not-supported-by-aws)
fsx-windows-pricing-cross-az-access-rate
  claim: When you access an FSx for Windows File Server file system from the same Region but from an AZ other than its preferred AZ, Multi-AZ file systems created before February 23, 2022 and Single-AZ file systems are charged $0.01/GB in each direction.
  scope: per GB in each direction, access from a non-preferred AZ in the same Region; Multi-AZ file systems created before February 23, 2022, and Single-AZ file systems.
  link: [$0.01/GB](../facts/fsx.md#fsx-windows-pricing-cross-az-access-rate)
fsx-windows-pricing-five-categories
  claim: AWS says the cost of FSx for Windows File Server has five categories: storage capacity, SSD IOPS, throughput capacity, backups and data transfer.
  scope: FSx for Windows File Server billing.
  link: [five categories to consider](../facts/fsx.md#fsx-windows-pricing-five-categories)
  link: [storage capacity, SSD IOPS, throughput capacity](../facts/fsx.md#fsx-windows-pricing-five-categories)
fsx-windows-pricing-multi-az-no-cross-az-access-charge
  claim: When you access an FSx for Windows File Server file system from the same Region but from an AZ other than its preferred AZ, Multi-AZ file systems created on or after February 23, 2022 have no data transfer charges.
  scope: Multi-AZ file systems created on or after February 23, 2022.
  link: [no data transfer charges](../facts/fsx.md#fsx-windows-pricing-multi-az-no-cross-az-access-charge)
fsx-windows-pricing-multi-az-replication-in-throughput-price
  claim: For FSx for Windows File Server Multi-AZ file systems, the cost of transferring data between Availability Zones for replication is included in the throughput capacity price.
  scope: FSx for Windows File Server Multi-AZ billing.
  link: [included in the throughput capacity price](../facts/fsx.md#fsx-windows-pricing-multi-az-replication-in-throughput-price)
fsx-windows-pricing-prorated-by-hour
  claim: For FSx for Windows File Server, pricing is quoted on a monthly basis, usage is prorated by the hour, and you are billed for your average usage over a month.
  scope: FSx for Windows File Server.
  link: [prorated by the hour](../facts/fsx.md#fsx-windows-pricing-prorated-by-hour)
fsx-windows-pricing-ssd-iops-3-per-gb-included
  claim: FSx for Windows File Server includes 3 IOPS for every GB of SSD storage by default; you can optionally provision more and pay for the average IOPS provisioned above the included rate.
  scope: per GB of SSD storage; default; adjustable; you can provision a higher level of IOPS.
  link: [3 IOPS are included for every GB of SSD storage](../facts/fsx.md#fsx-windows-pricing-ssd-iops-3-per-gb-included)
fsx-windows-pricing-storage-depends-on-deployment-and-type
  claim: The FSx for Windows File Server price of storage capacity depends on the deployment type (single-AZ or multi-AZ) and the storage type (SSD or HDD) you choose.
  scope: FSx for Windows File Server storage capacity.
  link: [deployment type](../facts/fsx.md#fsx-windows-pricing-storage-depends-on-deployment-and-type)
fsx-windows-pricing-throughput-depends-on-deployment
  claim: The FSx for Windows File Server price of throughput capacity depends on the deployment type (single-AZ or multi-AZ) you choose for your file system.
  scope: FSx for Windows File Server throughput capacity.
  link: [deployment type](../facts/fsx.md#fsx-windows-pricing-throughput-depends-on-deployment)
fsx-windows-quota-backups-per-account
  claim: The default for Windows backups is 500, the maximum number of user-initiated backups for all FSx for Windows File Server file systems that you can have in this account.
  scope: per account, per AWS Region, all Windows file systems; default; adjustable.
  link: [500](../facts/fsx.md#fsx-windows-quota-backups-per-account)
fsx-windows-quota-file-systems-per-account
  claim: The default for Windows file systems is 100, the maximum number of Amazon FSx for Windows File Server file systems that you can create in this account.
  scope: per account, per AWS Region; default; adjustable.
  link: [100](../facts/fsx.md#fsx-windows-quota-file-systems-per-account)
fsx-windows-quota-hdd-capacity-per-account
  claim: The default for Windows HDD storage capacity is 524288, the maximum amount of HDD storage capacity (in GiB) allowed for all FSx for Windows File Server file systems in this account.
  scope: per account, per AWS Region, all Windows file systems; default; adjustable.
  link: [524288](../facts/fsx.md#fsx-windows-quota-hdd-capacity-per-account)
fsx-windows-quota-ssd-capacity-per-account
  claim: The default for Windows SSD storage capacity is 524288, the maximum amount of SSD storage capacity (in GiB) allowed for all FSx for Windows File Server file systems in this account.
  scope: per account, per AWS Region, all Windows file systems; default; adjustable.
  link: [524288](../facts/fsx.md#fsx-windows-quota-ssd-capacity-per-account)
fsx-windows-quota-throughput-capacity-per-account
  claim: The default for Windows throughput capacity is 10240, the total amount of throughput capacity (in MBps) allowed for all Amazon FSx for Windows file systems in this account.
  scope: per account, per AWS Region, all Windows file systems; default; adjustable.
  link: [10240](../facts/fsx.md#fsx-windows-quota-throughput-capacity-per-account)
fsx-windows-quota-total-ssd-iops-per-account
  claim: The default for Windows total SSD IOPS is 500,000, the total amount of SSD IOPS allowed for all FSx for Windows File Server file systems in this account.
  scope: per account, per AWS Region, all Windows file systems; default; adjustable.
  link: [500,000](../facts/fsx.md#fsx-windows-quota-total-ssd-iops-per-account)
fsx-windows-resource-forest-one-way-trust
  claim: In the resource forest isolation model, you join your FSx for Windows File Server file system to an AWS Managed Microsoft AD setup and then establish a one-way forest trust relationship between that AWS Managed Microsoft AD domain and your existing self-managed Active Directory domain.
  scope: Amazon FSx for Windows File Server.
  link: [one-way forest trust relationship](../facts/fsx.md#fsx-windows-resource-forest-one-way-trust)
  link: [self-managed Active Directory domain](../facts/fsx.md#fsx-windows-resource-forest-one-way-trust)
fsx-windows-shadow-copies-default-max-20
  claim: When you enable shadow copies on FSx for Windows, the default limit for the maximum number of shadow copies stored on the file system is 20.
  scope: per file system; default; adjustable; you can set it up to 500.
  link: [20](../facts/fsx.md#fsx-windows-shadow-copies-default-max-20)
fsx-windows-shadow-copies-max-500
  claim: You can store a maximum of 500 shadow copies per file system at any point in time on FSx for Windows; fewer than 64 are recommended.
  scope: per file system; maximum; not adjustable.
  link: [500 shadow copies](../facts/fsx.md#fsx-windows-shadow-copies-max-500)
fsx-windows-shadow-copies-not-enabled-by-default-not-backup-substitute
  claim: Shadow copies are not enabled on FSx for Windows File Server by default; to protect your data with shadow copies you must enable shadow copies and set up a shadow copy schedule, and shadow copies are not a substitute for backups.
  scope: FSx for Windows File Server shadow copies; default; adjustable.
  link: [enabled on FSx for Windows File Server](../facts/fsx.md#fsx-windows-shadow-copies-not-enabled-by-default-not-backup-substitute)
  link: [not a substitute for backups](../facts/fsx.md#fsx-windows-shadow-copies-not-enabled-by-default-not-backup-substitute)
fsx-windows-shadow-copy-definition-restore-previous-versions
  claim: A Microsoft Windows shadow copy is a snapshot of a Windows file system at a point in time, and with shadow copies enabled users can quickly recover deleted or changed files and compare file versions.
  scope: FSx for Windows File Server shadow copies.
  link: [snapshot of a Windows file system](../facts/fsx.md#fsx-windows-shadow-copy-definition-restore-previous-versions)
  link: [quickly recover deleted or changed files](../facts/fsx.md#fsx-windows-shadow-copy-definition-restore-previous-versions)
fsx-windows-shadow-copy-storage-default-10-percent
  claim: When you enable shadow copies on FSx for Windows, the default limit for the maximum shadow copy storage is 10 percent of your file system.
  scope: per file system; default; adjustable.
  link: [10 percent](../facts/fsx.md#fsx-windows-shadow-copy-storage-default-10-percent)
fsx-windows-single-az-1-feature-row-ssd-dfs-replication
  claim: In the feature support table for FSx for Windows File Server, the Single-AZ 1 deployment type is marked for SSD storage, DFS namespaces, DFS replication and custom DNS names, and has no mark for HDD storage or CA shares.
  scope: FSx for Windows File Server deployment type.
  link: [Single-AZ 1](../facts/fsx.md#fsx-windows-single-az-1-feature-row-ssd-dfs-replication)
fsx-windows-single-az-2-feature-row-hdd-ca-shares
  claim: In the feature support table for FSx for Windows File Server, the Single-AZ 2 deployment type is marked for SSD storage, HDD storage, DFS namespaces, custom DNS names and CA shares, and has no mark for DFS replication; a note on the CA shares mark says that while you can create CA shares on Single-AZ 2 file systems, you should use CA shares on Multi-AZ file systems for SQL Server HA deployments.
  scope: FSx for Windows File Server deployment type.
  link: [Single-AZ 2](../facts/fsx.md#fsx-windows-single-az-2-feature-row-hdd-ca-shares)
fsx-windows-single-az-one-server-one-az-30-minutes-downtime
  claim: A Single-AZ FSx for Windows file system has one Windows file server and its storage volumes in a single Availability Zone, replicates data automatically against the failure of a single component in most cases, and usually has about 30 minutes of downtime during failure recovery and planned maintenance.
  scope: FSx for Windows File Server Single-AZ.
  link: [about 30 minutes of downtime](../facts/fsx.md#fsx-windows-single-az-one-server-one-az-30-minutes-downtime)
  link: [single Windows file server instance](../facts/fsx.md#fsx-windows-single-az-one-server-one-az-30-minutes-downtime)
fsx-windows-single-az-unrecoverable-restore-from-backup
  claim: With a Single-AZ FSx for Windows file system, failure may be unrecoverable in rare cases, such as multiple component failures or a non-graceful failure of the single file server, in which case you recover from the most recent backup.
  scope: FSx for Windows File Server Single-AZ.
  link: [may be unrecoverable in rare cases](../facts/fsx.md#fsx-windows-single-az-unrecoverable-restore-from-backup)
  link: [from the most recent backup](../facts/fsx.md#fsx-windows-single-az-unrecoverable-restore-from-backup)
fsx-windows-smb-versions-2-0-to-3-1-1
  claim: FSx for Windows File Server is compatible with the SMB protocol versions 2.0 through 3.1.1.
  scope: Amazon FSx for Windows File Server.
  link: [SMB) protocol versions 2.0 through 3.1.1](../facts/fsx.md#fsx-windows-smb-versions-2-0-to-3-1-1)
  link: [2.0 through 3.1.1](../facts/fsx.md#fsx-windows-smb-versions-2-0-to-3-1-1)
fsx-windows-sql-server-active-data-files-or-share-witness-ssd
  claim: You can use FSx for Windows File Server as shared storage for high availability SQL Server in two ways, as storage for active data files and as an SMB file share witness, and SSD storage is recommended for SQL Server.
  scope: FSx for Windows File Server with SQL Server.
  link: [storage for active data files](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
  link: [SMB file share witness](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
  link: [SSD storage is recommended](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
fsx-windows-sql-server-ssd-recommended
  claim: AWS recommends SSD storage for SQL Server on FSx for Windows File Server, because SSD storage is designed for the highest-performance and most latency-sensitive workloads, including databases.
  scope: FSx for Windows File Server with Microsoft SQL Server.
  link: [SSD storage is recommended for SQL Server](../facts/fsx.md#fsx-windows-sql-server-ssd-recommended)
fsx-windows-ssd-iops-automatic-mode
  claim: In Automatic mode, Amazon FSx automatically scales the SSD IOPS of an FSx for Windows file system to maintain 3 SSD IOPS per GiB of storage capacity, up to 400,000 SSD IOPS per file system.
  scope: per FSx for Windows file system, Automatic IOPS mode; default; adjustable; up to 400,000 SSD IOPS per file system.
  link: [3 SSD IOPS per GiB](../facts/fsx.md#fsx-windows-ssd-iops-automatic-mode)
fsx-windows-ssd-iops-pay-above-3-per-gib
  claim: For higher levels of provisioned SSD IOPS on FSx for Windows, you pay for the average IOPS above 3 IOPS per GiB per file system.
  scope: per FSx for Windows file system.
  link: [above 3 IOPS per GiB](../facts/fsx.md#fsx-windows-ssd-iops-pay-above-3-per-gib)
fsx-windows-ssd-iops-user-provisioned-range
  claim: In User-provisioned mode you can specify the number of SSD IOPS of an FSx for Windows file system within the range of 96–400,000.
  scope: per FSx for Windows file system, User-provisioned IOPS mode; maximum; adjustable.
  link: [96–400,000](../facts/fsx.md#fsx-windows-ssd-iops-user-provisioned-range)
fsx-windows-storage-capacity-6-hours-between-increases
  claim: You cannot make further storage capacity increases on an FSx for Windows File Server file system until 6 hours after the last increase was requested or until storage optimization has completed, whichever is longer.
  scope: FSx for Windows File Server storage capacity.
  link: [6 hours after the last increase was requested](../facts/fsx.md#fsx-windows-storage-capacity-6-hours-between-increases)
  link: [whichever time is longer](../facts/fsx.md#fsx-windows-storage-capacity-6-hours-between-increases)
fsx-windows-storage-capacity-increase-minimum-10-percent
  claim: Each storage capacity increase of an FSx for Windows File Server file system must be a minimum of 10 percent of the current storage capacity, up to the maximum allowed value of 65,536 GiB.
  scope: per storage capacity increase, FSx for Windows File Server; minimum; not adjustable.
  link: [minimum of 10 percent](../facts/fsx.md#fsx-windows-storage-capacity-increase-minimum-10-percent)
  link: [65,536 GiB](../facts/fsx.md#fsx-windows-storage-capacity-increase-minimum-10-percent)
fsx-windows-storage-capacity-increase-only-never-decrease
  claim: You can only increase the storage capacity of an FSx for Windows File Server file system; you cannot decrease it.
  scope: FSx for Windows File Server storage capacity.
  link: [Increase only](../facts/fsx.md#fsx-windows-storage-capacity-increase-only-never-decrease)
  link: [can't decrease storage capacity](../facts/fsx.md#fsx-windows-storage-capacity-increase-only-never-decrease)
fsx-windows-storage-hdd-vs-ssd-use-cases
  claim: FSx for Windows File Server offers SSD and HDD storage; HDD is designed for home directories, user and departmental shares and content management systems, and SSD for the highest-performance, most latency-sensitive workloads such as databases, media processing and data analytics.
  scope: FSx for Windows File Server storage types.
  link: [home directories, user and departmental shares](../facts/fsx.md#fsx-windows-storage-hdd-vs-ssd-use-cases)
  link: [highest-performance and most latency-sensitive workloads](../facts/fsx.md#fsx-windows-storage-hdd-vs-ssd-use-cases)
fsx-windows-storage-increase-min-throughput-16
  claim: To increase storage capacity, an FSx for Windows file system must have a minimum throughput capacity of 16 MBps.
  scope: per FSx for Windows file system; minimum; to increase storage capacity.
  link: [16 MBps](../facts/fsx.md#fsx-windows-storage-increase-min-throughput-16)
fsx-windows-storage-type-hdd-to-ssd-only
  claim: You can change the storage type of an FSx for Windows File Server file system from HDD to SSD but not from SSD to HDD; to go from SSD to HDD you restore a backup to a new file system that uses HDD storage.
  scope: FSx for Windows File Server storage type.
  link: [from HDD to SSD](../facts/fsx.md#fsx-windows-storage-type-hdd-to-ssd-only)
  link: [from SSD to HDD](../facts/fsx.md#fsx-windows-storage-type-hdd-to-ssd-only)
fsx-windows-supported-compute-ec2-ecs-workspaces
  claim: FSx for Windows File Server is supported for Amazon EC2 instances, including Microsoft Windows, Mac, and Amazon Linux 2023 instances, and for Amazon ECS containers.
  scope: Amazon FSx for Windows File Server clients.
  link: [Microsoft Windows, Mac, and Amazon Linux 2023 instances](../facts/fsx.md#fsx-windows-supported-compute-ec2-ecs-workspaces)
  link: [Amazon Elastic Container Service (Amazon ECS) containers](../facts/fsx.md#fsx-windows-supported-compute-ec2-ecs-workspaces)
fsx-windows-test-failover-by-changing-throughput-capacity
  claim: You can test failover of a Multi-AZ FSx for Windows file system by modifying its throughput capacity.
  scope: FSx for Windows File Server Multi-AZ.
  link: [modifying its throughput capacity](../facts/fsx.md#fsx-windows-test-failover-by-changing-throughput-capacity)
  link: [test failover](../facts/fsx.md#fsx-windows-test-failover-by-changing-throughput-capacity)
fsx-windows-throughput-4608-regions
  claim: Throughput capacity levels of 4,608 MBps and higher are supported only in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore).
  scope: per FSx for Windows file system; minimum; supported only in six listed Regions.
  link: [4,608 MBps and higher](../facts/fsx.md#fsx-windows-throughput-4608-regions)
fsx-windows-throughput-below-32-test-dev
  claim: Throughput capacity levels below 32 megabytes per second (MBps) can be selected with the Amazon FSx API or CLI, but they are meant for test and development workloads, not for production workloads.
  scope: per FSx for Windows file system.
  link: [32 megabytes per second](../facts/fsx.md#fsx-windows-throughput-below-32-test-dev)
fsx-windows-throughput-iops-by-region
  claim: Amazon FSx file systems provide up to 2 GBps and 80,000 IOPS in all AWS Regions where Amazon FSx is available, and 12 GBps of throughput and 400,000 IOPS in US East (N. Virginia), US West (Oregon), US East (Ohio), Europe (Ireland), Asia Pacific (Tokyo), and Asia Pacific (Singapore).
  scope: per FSx for Windows file system, by AWS Region; maximum; not adjustable; the 12 GBps and 400,000 IOPS levels apply in six listed Regions.
  link: [2 GBps](../facts/fsx.md#fsx-windows-throughput-iops-by-region)
  link: [80,000 IOPS](../facts/fsx.md#fsx-windows-throughput-iops-by-region)
  link: [12 GBps](../facts/fsx.md#fsx-windows-throughput-iops-by-region)
  link: [400,000 IOPS](../facts/fsx.md#fsx-windows-throughput-iops-by-region)
fsx-windows-user-initiated-backups-never-expire
  claim: User-initiated FSx for Windows File Server backups never expire, are available for as long as you want to keep them, and are retained even after you delete the file system that was backed up.
  scope: FSx for Windows File Server backups.
  link: [backups of Amazon FSx file systems never expire](../facts/fsx.md#fsx-windows-user-initiated-backups-never-expire)
  link: [retained even after you delete the file system](../facts/fsx.md#fsx-windows-user-initiated-backups-never-expire)
fsx-windows-vpc-sharing-supported
  claim: FSx for Windows File Server supports VPC sharing, which enables you to view, create, modify and delete resources in a shared subnet in a VPC owned by another AWS account.
  scope: Amazon FSx for Windows File Server.
  link: [supports VPC sharing](../facts/fsx.md#fsx-windows-vpc-sharing-supported)
  link: [a VPC owned by another AWS account](../facts/fsx.md#fsx-windows-vpc-sharing-supported)
fsx-windows-what-is-access-other-vpc-account-region-on-premises
  claim: You can access FSx for Windows File Server file shares from on-premises compute instances using AWS Direct Connect or Site-to-Site VPN, and from a different VPC, account or AWS Region using VPC peering or transit gateways.
  scope: FSx for Windows File Server network access.
  link: [AWS Direct Connect or Site-to-Site VPN](../facts/fsx.md#fsx-windows-what-is-access-other-vpc-account-region-on-premises)
  link: [VPC peering or transit gateways](../facts/fsx.md#fsx-windows-what-is-access-other-vpc-account-region-on-premises)
fsx-windows-what-is-smb-versions-and-clients
  claim: FSx for Windows File Server is accessible with the SMB protocol, supporting versions 2.0 to 3.1.1, from all Windows versions starting from Windows Server 2008 and Windows 7, and also from current versions of Linux.
  scope: FSx for Windows File Server.
  link: [supporting versions 2.0 to 3.1.1](../facts/fsx.md#fsx-windows-what-is-smb-versions-and-clients)
fsx-windows-what-is-unchanged-windows-apps-workloads
  claim: AWS says that with file storage on Amazon FSx the code, applications and tools that Windows developers and administrators use today can continue to work unchanged. Ideal workloads include business applications, home directories, web serving, content management, data analytics, software build setups and media processing.
  scope: FSx for Windows File Server.
  link: [can continue to work unchanged](../facts/fsx.md#fsx-windows-what-is-unchanged-windows-apps-workloads)
