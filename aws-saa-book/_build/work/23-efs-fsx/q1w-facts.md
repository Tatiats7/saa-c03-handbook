facts card: 39 facts
efs-general-purpose-always-recommended-max-io-higher-latency
  claim: Max I/O performance mode has higher per-operation latencies than General Purpose mode, so AWS recommends always using General Purpose performance mode.
  scope: EFS performance modes.
  link: [always using General Purpose performance mode](../facts/efs.md#efs-general-purpose-always-recommended-max-io-higher-latency)
  link: [higher per-operation latencies with Max I/O](../facts/efs.md#efs-general-purpose-always-recommended-max-io-higher-latency)
efs-max-io-not-supported-one-zone-or-elastic
  claim: Max I/O performance mode is a previous generation mode and is not supported for One Zone file systems or for file systems that use Elastic throughput.
  scope: EFS performance modes.
  link: [not supported for One Zone file systems](../facts/efs.md#efs-max-io-not-supported-one-zone-or-elastic)
  link: [file systems that use Elastic throughput](../facts/efs.md#efs-max-io-not-supported-one-zone-or-elastic)
efs-provisioned-use-when-known-needs-5-percent-or-more
  claim: Use Provisioned throughput if you know your workload's performance requirements, or if your application drives throughput at 5% or more of the average-to-peak ratio.
  scope: EFS Provisioned throughput.
  link: [know your workload's performance requirements](../facts/efs.md#efs-provisioned-use-when-known-needs-5-percent-or-more)
  link: [5% or more of the average-to-peak ratio](../facts/efs.md#efs-provisioned-use-when-known-needs-5-percent-or-more)
efs-pricing-provisioned-throughput-predictable-sustained
  claim: AWS says to use EFS Provisioned Throughput if you have predictable and high levels of sustained throughput requirements, and that the amount billed in a month is based on the average throughput provisioned in excess of the baseline throughput included with your EFS Standard storage usage.
  scope: EFS Provisioned Throughput.
  link: [predictable and high levels of sustained throughput requirements](../facts/efs.md#efs-pricing-provisioned-throughput-predictable-sustained)
efs-provisioned-throughput-independent-of-size
  claim: With Provisioned throughput you specify a level of throughput that the file system can drive, independent of the file system's size or burst credit balance.
  scope: EFS Provisioned throughput.
  link: [you specify a level of throughput](../facts/efs.md#efs-provisioned-throughput-independent-of-size)
  link: [independent of the file system's size](../facts/efs.md#efs-provisioned-throughput-independent-of-size)
efs-faq-one-zone-use-cases
  claim: EFS One Zone storage classes are ideal for workloads such as development, build, and staging environments.
  scope: EFS One Zone storage classes.
  link: [development, build, and staging environments](../facts/efs.md#efs-faq-one-zone-use-cases)
efs-pricing-one-zone-for-no-multi-az-need
  claim: AWS says EFS One Zone file systems are ideal for applications that do not require the Multi-AZ availability and durability of EFS Regional file systems.
  scope: EFS One Zone.
  link: [do not require the Multi-AZ availability and durability](../facts/efs.md#efs-pricing-one-zone-for-no-multi-az-need)
efs-regional-multi-az-continuous-availability
  claim: A Regional EFS file system stores data redundantly across multiple Availability Zones in one AWS Region, which keeps the data continuously available even when one or more Availability Zones are unavailable.
  scope: Regional file system.
  link: [continuous availability to the data](../facts/efs.md#efs-regional-multi-az-continuous-availability)
  link: [even when one or more Availability Zones](../facts/efs.md#efs-regional-multi-az-continuous-availability)
efs-onezone-not-resilient-to-az-outage
  claim: EFS One Zone file systems are not resilient to a complete Availability Zone outage; during an outage you lose availability because the data is not replicated to a different Availability Zone.
  scope: One Zone file system.
  link: [not resilient to a complete AZ outage](../facts/efs.md#efs-onezone-not-resilient-to-az-outage)
  link: [loss of availability](../facts/efs.md#efs-onezone-not-resilient-to-az-outage)
efs-faq-one-zone-single-az
  claim: EFS One Zone file systems store data redundantly in a single AZ, so the data will be unavailable and might be lost during a disaster or other fault within that AZ.
  scope: EFS One Zone file systems.
  link: [store data redundantly within a single AZ](../facts/efs.md#efs-faq-one-zone-single-az)
efs-regional-designed-to-sustain-az-loss
  claim: EFS Regional file systems are designed to sustain data if an Availability Zone is lost, and they support concurrent access from mount targets in all Availability Zones of the Region.
  scope: Regional file system.
  link: [sustain data if an AZ is lost](../facts/efs.md#efs-regional-designed-to-sustain-az-loss)
  link: [concurrent access from EFS mount targets](../facts/efs.md#efs-regional-designed-to-sustain-az-loss)
efs-faq-access-from-lambda-function-settings
  claim: You can access EFS from AWS Lambda functions by referencing an EFS file system in the function settings.
  scope: EFS with AWS Lambda.
  link: [an EFS file system in your function settings](../facts/efs.md#efs-faq-access-from-lambda-function-settings)
efs-faq-use-case-file-vs-block-vs-object
  claim: EFS is a file storage service, Amazon EBS is a block-level storage service for use with EC2, and Amazon S3 is an object storage service.
  scope: EFS vs EBS vs S3.
  link: [file storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [block-level storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [object storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
efs-serverless-elastic-no-provisioning
  claim: Amazon EFS is serverless and fully elastic: you do not provision or manage storage capacity, and a file system grows and shrinks automatically as you add and remove files.
  scope: Amazon EFS file system.
  link: [serverless, fully elastic file storage](../facts/efs.md#efs-serverless-elastic-no-provisioning)
  link: [growing and shrinking automatically](../facts/efs.md#efs-serverless-elastic-no-provisioning)
  link: [without provisioning or managing storage capacity](../facts/efs.md#efs-serverless-elastic-no-provisioning)
efs-faq-elastic-grow-shrink
  claim: EFS file systems are elastic: they grow and shrink automatically as files are added and removed.
  scope: EFS file system.
  link: [elastic, automatically growing and shrinking](../facts/efs.md#efs-faq-elastic-grow-shrink)
fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd
  claim: FSx for OpenZFS has two storage classes: Intelligent-Tiering, where you are billed for the data you store and do not specify a file system size, and SSD, where you specify a file system size and pay for the storage you provision.
  scope: FSx for OpenZFS storage classes.
  link: [fully elastic, cost-effective storage](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
  link: [do not need to specify](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
  link: [pay for the amount of storage](../facts/fsx.md#fsx-openzfs-two-storage-classes-intelligent-tiering-and-ssd)
fsx-lustre-use-scratch-for-short-term-persistent-for-long-term
  claim: Use scratch FSx for Lustre file systems when you need cost-optimized storage for short-term, processing-heavy workloads, and persistent file systems for longer-term storage and for throughput-focused workloads that run for extended periods or indefinitely and that might be sensitive to disruptions in availability.
  scope: FSx for Lustre deployment types.
  link: [cost-optimized storage for short-term, processing-heavy workloads](../facts/fsx.md#fsx-lustre-use-scratch-for-short-term-persistent-for-long-term)
  link: [sensitive to disruptions in availability](../facts/fsx.md#fsx-lustre-use-scratch-for-short-term-persistent-for-long-term)
fsx-lustre-scratch-temporary-not-replicated
  claim: Scratch FSx for Lustre file systems are for temporary storage and shorter-term processing; data is not replicated and does not persist if a file server fails.
  scope: FSx for Lustre scratch file systems.
  link: [Data is not replicated](../facts/fsx.md#fsx-lustre-scratch-temporary-not-replicated)
  link: [does not persist if a file server fails](../facts/fsx.md#fsx-lustre-scratch-temporary-not-replicated)
fsx-lustre-persistent-replicated-servers-replaced
  claim: Persistent FSx for Lustre file systems are for longer-term storage and throughput-focused workloads; data is replicated and file servers are replaced if they fail.
  scope: FSx for Lustre persistent file systems.
  link: [data is replicated](../facts/fsx.md#fsx-lustre-persistent-replicated-servers-replaced)
  link: [file servers are replaced if they fail](../facts/fsx.md#fsx-lustre-persistent-replicated-servers-replaced)
fsx-faq-lustre-backups-not-on-scratch
  claim: Backups are not supported on FSx for Lustre scratch file systems because they are designed for temporary storage and shorter-term processing of data.
  scope: FSx for Lustre scratch file systems.
  link: [Backups aren’t supported on scratch file systems](../facts/fsx.md#fsx-faq-lustre-backups-not-on-scratch)
fsx-decision-guide-lustre-speed-workloads
  claim: The AWS storage decision guide says FSx for Lustre is optimized for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing and financial modeling.
  scope: Amazon FSx for Lustre.
  link: [machine learning, high performance computing (HPC)](../facts/fsx.md#fsx-decision-guide-lustre-speed-workloads)
  link: [video processing, and financial modeling](../facts/fsx.md#fsx-decision-guide-lustre-speed-workloads)
fsx-windows-ca-shares-required-multi-az-for-sql-server
  claim: For Microsoft SQL Server, FSx for Windows File Server supports continuously available (CA) file shares. You can create CA shares on Single-AZ 2 file systems, but it is required that you use CA shares on Multi-AZ file systems for all SQL Server deployments, whether HA or not.
  scope: FSx for Windows File Server with Microsoft SQL Server.
  link: [continuously available (CA) file shares](../facts/fsx.md#fsx-windows-ca-shares-required-multi-az-for-sql-server)
  link: [use CA shares on Multi-AZ file systems](../facts/fsx.md#fsx-windows-ca-shares-required-multi-az-for-sql-server)
fsx-windows-sql-server-ssd-recommended
  claim: AWS recommends SSD storage for SQL Server on FSx for Windows File Server, because SSD storage is designed for the highest-performance and most latency-sensitive workloads, including databases.
  scope: FSx for Windows File Server with Microsoft SQL Server.
  link: [SSD storage is recommended for SQL Server](../facts/fsx.md#fsx-windows-sql-server-ssd-recommended)
fsx-windows-sql-server-active-data-files-or-share-witness-ssd
  claim: You can use FSx for Windows File Server as shared storage for high availability SQL Server in two ways, as storage for active data files and as an SMB file share witness, and SSD storage is recommended for SQL Server.
  scope: FSx for Windows File Server with SQL Server.
  link: [storage for active data files](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
  link: [SMB file share witness](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
  link: [SSD storage is recommended](../facts/fsx.md#fsx-windows-sql-server-active-data-files-or-share-witness-ssd)
fsx-ontap-tiering-policy-auto-31-days-default-console
  claim: The Auto tiering policy moves all cold user data and snapshots to the capacity pool tier; the cooling period is 31 days by default and configurable from 2 to 183 days, and Auto is the default policy when creating a volume in the console.
  scope: FSx for ONTAP volume tiering policy Auto; default; adjustable.
  link: [by default is 31 days](../facts/fsx.md#fsx-ontap-tiering-policy-auto-31-days-default-console)
  link: [between 2–183 days](../facts/fsx.md#fsx-ontap-tiering-policy-auto-31-days-default-console)
fsx-ontap-tiering-policy-all-marks-everything-cold
  claim: The All tiering policy marks all user data and snapshot data as cold and stores it in the capacity pool tier, where data blocks stay cold when read; file metadata always remains on the SSD tier.
  scope: FSx for ONTAP volume tiering policy All.
  link: [marks all user data and snapshot data](../facts/fsx.md#fsx-ontap-tiering-policy-all-marks-everything-cold)
  link: [file metadata always remains on the SSD tier](../facts/fsx.md#fsx-ontap-tiering-policy-all-marks-everything-cold)
fsx-ontap-tiering-policy-none-keeps-all-on-ssd
  claim: The None tiering policy keeps all of a volume's data on the primary storage tier and prevents it from being moved to capacity pool storage.
  scope: FSx for ONTAP volume tiering policy None.
  link: [keeps all of your volume’s data](../facts/fsx.md#fsx-ontap-tiering-policy-none-keeps-all-on-ssd)
  link: [prevents it from being moved](../facts/fsx.md#fsx-ontap-tiering-policy-none-keeps-all-on-ssd)
fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli
  claim: The Snapshot Only tiering policy moves only snapshot data to the capacity pool tier, with a cooling period that is 2 days by default and configurable from 2 to 183 days; it is the default policy when creating a volume with the AWS CLI, API or ONTAP CLI.
  scope: FSx for ONTAP volume tiering policy Snapshot Only; default; adjustable.
  link: [moves only snapshot data](../facts/fsx.md#fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli)
  link: [by default is set to 2 days](../facts/fsx.md#fsx-ontap-tiering-policy-snapshot-only-2-days-default-cli)
efs-replication-rpo-rto-minutes
  claim: EFS replication is continual and designed to provide a recovery point objective (RPO) and a recovery time objective (RTO) of minutes.
  scope: EFS replication.
  link: [objective (RTO) of minutes](../facts/efs.md#efs-replication-rpo-rto-minutes)
  link: [Replication is continual](../facts/efs.md#efs-replication-rpo-rto-minutes)
efs-replication-failover-delete-configuration-replica-writeable
  claim: To fail over to the replica file system you delete its replication configuration; after the configuration is deleted the replica becomes writeable and you can use it in your application workflow.
  scope: EFS replication failover.
  link: [by deleting its replication configuration](../facts/efs.md#efs-replication-failover-delete-configuration-replica-writeable)
  link: [the replica becomes writeable](../facts/efs.md#efs-replication-failover-delete-configuration-replica-writeable)
efs-replication-destination-faq-region-or-az-of-choice
  claim: You can use EFS Replication to replicate your file system to a Region or Availability Zone of your choice, without managing additional infrastructure or custom processes.
  scope: EFS replication.
  link: [Region or Availability Zone (AZ) of your choice](../facts/efs.md#efs-replication-destination-faq-region-or-az-of-choice)
  link: [without having to manage additional infrastructure](../facts/efs.md#efs-replication-destination-faq-region-or-az-of-choice)
efs-replication-destination-read-only-while-replicating
  claim: The destination file system of EFS replication is read-only while replication is enabled, and applications can use it in read-only mode for low-latency cross-Region access.
  scope: EFS replication.
  link: [new read-only destination file system](../facts/efs.md#efs-replication-destination-read-only-while-replicating)
  link: [use the replica file system in read-only mode](../facts/efs.md#efs-replication-destination-read-only-while-replicating)
fsx-windows-multi-az-standby-two-azs-sync-replication
  claim: A Multi-AZ FSx for Windows file system is a high-availability cluster of Windows file servers across two Availability Zones (a preferred and a standby AZ) using Windows Server Failover Clustering, and data is replicated synchronously within each AZ and between the two AZs.
  scope: FSx for Windows File Server Multi-AZ.
  link: [a preferred AZ and a standby AZ](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
  link: [replicated synchronously within each individual AZ](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
  link: [Windows Server Failover Clustering](../facts/fsx.md#fsx-windows-multi-az-standby-two-azs-sync-replication)
fsx-windows-multi-az-enhanced-durability-availability-auto-failover
  claim: Compared with Single-AZ, Multi-AZ deployments give enhanced durability by replicating data across AZs, and enhanced availability by failing over automatically to the standby AZ during planned maintenance and unplanned disruption.
  scope: FSx for Windows File Server Multi-AZ.
  link: [enhanced durability by further replicating data across AZs](../facts/fsx.md#fsx-windows-multi-az-enhanced-durability-availability-auto-failover)
  link: [failing over automatically to the standby AZ](../facts/fsx.md#fsx-windows-multi-az-enhanced-durability-availability-auto-failover)
fsx-windows-single-az-one-server-one-az-30-minutes-downtime
  claim: A Single-AZ FSx for Windows file system has one Windows file server and its storage volumes in a single Availability Zone, replicates data automatically against the failure of a single component in most cases, and usually has about 30 minutes of downtime during failure recovery and planned maintenance.
  scope: FSx for Windows File Server Single-AZ.
  link: [about 30 minutes of downtime](../facts/fsx.md#fsx-windows-single-az-one-server-one-az-30-minutes-downtime)
  link: [single Windows file server instance](../facts/fsx.md#fsx-windows-single-az-one-server-one-az-30-minutes-downtime)
fsx-lustre-s3-presents-objects-as-files-and-writes-back
  claim: When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files, imports listings of existing files at file system creation, and can write file system data back to S3.
  scope: FSx for Lustre S3 data repository.
  link: [transparently presents S3 objects as files](../facts/fsx.md#fsx-lustre-s3-presents-objects-as-files-and-writes-back)
  link: [write file system data back to S3](../facts/fsx.md#fsx-lustre-s3-presents-objects-as-files-and-writes-back)
fsx-faq-lustre-s3-object-imported-on-first-access
  claim: The content of an S3 object is imported automatically only when you first access the associated file on the file system, so an object's data does not consume file system space unless accessed at least once.
  scope: FSx for Lustre linked to Amazon S3.
  link: [imported automatically from S3 only when you access](../facts/fsx.md#fsx-faq-lustre-s3-object-imported-on-first-access)
efs-decision-guide-block-row-single-instance
  claim: In the AWS storage decision guide table, block storage (Amazon EBS and the EC2 instance store) is for low-latency, high-performance durable storage attached to single Amazon EC2 instances or containers, such as databases.
  scope: storage type table of the decision guide.
  link: [attached to single Amazon EC2 instances or containers](../facts/efs.md#efs-decision-guide-block-row-single-instance)
efs-decision-guide-file-system-row-shared-access
  claim: In the AWS storage decision guide table, file system storage is the type for applications that need shared read and write access across multiple EC2 instances or containers, or from multiple on-premises servers; the services listed for it include Amazon EFS and the Amazon FSx file systems.
  scope: storage type table of the decision guide.
  link: [shared read and write access](../facts/efs.md#efs-decision-guide-file-system-row-shared-access)
