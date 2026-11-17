import sys
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from gen_lib import *

WP = 'docs/whitepapers/latest/aws-overview/storage-services'
DG = 'docs/decision-guides/latest/decision-guides/choosing-aws-storage-service'
PERF = 'docs/efs/latest/ug/performance'
WHAT = 'docs/efs/latest/ug/whatisefs'
LIFE = 'docs/efs/latest/ug/lifecycle-management-efs'
facts = []

def add(*a, **k):
    facts.append(F(*a, **k))

# ---------- whitepaper one-liners (In one breath)
add('efs-overview-regional-linux-shared-access', 'efs', 'behavior',
    'The AWS overview whitepaper describes Amazon EFS as a regional service that stores data within and across multiple Availability Zones for high availability and durability, and as fully managed with no changes needed to existing applications and tools.',
    'How does the AWS overview whitepaper describe Amazon EFS in one breath?',
    ['a regional service storing data within and across multiple Availability Zones (AZs)', 'requires no changes to your existing applications and tools'],
    [ev('sent', WP, 'Amazon EFS is a regional service storing data within and across multiple Availability Zones'),
     ev('sent', WP, 'Amazon EFS is a fully managed service that requires no changes')],
    scope='Amazon EFS', bul=['4.1.K4', '2.2.S7'], t0=True)
add('efs-overview-thousands-of-instances-and-on-premises', 'efs', 'capability',
    'The AWS overview whitepaper says you can access EFS file systems across Availability Zones and AWS Regions and share files between thousands of Amazon EC2 instances and on-premises servers through Direct Connect or Site-to-Site VPN.',
    'How many clients can share an EFS file system, and can on-premises servers reach it?',
    ['thousands of Amazon EC2 instances and on-premises servers'],
    [ev('sent', WP, 'You can access your file systems across Availability Zones and AWS Regions')],
    scope='Amazon EFS', bul=['3.1.K2', '2.1.K13'])
add('fsx-overview-lustre-s3-integration-hpc', 'fsx', 'capability',
    'The AWS overview whitepaper says FSx for Lustre is seamlessly integrated with Amazon S3, so you can link long-term data sets with high-performance file systems for compute-intensive workloads.',
    'What integration makes FSx for Lustre fit HPC and machine learning on S3 data?',
    ['seamlessly integrated with Amazon S3'],
    [ev('sent', WP, 'Amazon FSx for Lustre is seamlessly integrated with Amazon S3')],
    scope='Amazon FSx for Lustre', bul=['4.1.K4', '2.2.S8'], t0=True)
add('fsx-overview-ontap-multiprotocol-nfs-smb-iscsi', 'fsx', 'capability',
    'The AWS overview whitepaper says FSx for NetApp ONTAP offers high-performance file storage accessible from Linux, Windows and macOS compute instances through the NFS, SMB and iSCSI protocols.',
    'Which protocols and client operating systems does FSx for NetApp ONTAP serve?',
    ['Linux, Windows, and macOS', 'NFS, SMB, and iSCSI'],
    [ev('sent', WP, 'Amazon FSx for NetApp ONTAP offers high-performance file storage that is broadly accessible')],
    scope='Amazon FSx for NetApp ONTAP', bul=['4.1.K4', '2.2.S8'], t0=True)
add('fsx-overview-openzfs-migrate-without-changing-apps', 'fsx', 'capability',
    'The AWS overview whitepaper says FSx for OpenZFS makes it easy to migrate on-premises file servers without changing your applications or how you manage data.',
    'Why does the AWS overview whitepaper present FSx for OpenZFS as a migration target for on-premises file servers?',
    ['without changing your applications or how you manage data'],
    [ev('sent', WP, 'Amazon FSx for OpenZFS makes it easy to migrate your on-premises file servers')],
    scope='Amazon FSx for OpenZFS', bul=['4.1.K4', '2.2.S7', '2.2.S8'])
add('fsx-overview-windows-smb-ntfs-ad-dfs', 'fsx', 'capability',
    'The AWS overview whitepaper says FSx for Windows File Server is built on Windows Server and supports the SMB protocol and Windows NTFS, Active Directory integration and Distributed File System (DFS).',
    'What Windows features does FSx for Windows File Server support, according to the AWS overview whitepaper?',
    ['full support for the SMB protocol and Windows NTFS, Active Directory (AD) integration, and Distributed File System (DFS)'],
    [ev('sent', WP, 'Built on Windows Server, Amazon FSx provides shared file storage')],
    scope='Amazon FSx for Windows File Server', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)

# ---------- decision guide: criteria
add('fsx-decision-guide-four-file-systems-align-to-popular', 'fsx', 'behavior',
    'The AWS storage decision guide says the Amazon FSx data storage family comes in four options that align to popular file systems: Windows File Server, Lustre, OpenZFS and NetApp ONTAP.',
    'How many FSx file system types are there, and which popular file systems do they match?',
    ['four options that align to popular file systems'],
    [ev('sent', DG, 'For example, services in the Amazon FSx data storage family come in four options')],
    scope='Amazon FSx family', bul=['4.1.K4', '2.2.S8'])
add('efs-decision-guide-use-appropriate-service-cost', 'efs', 'behavior',
    'The AWS storage decision guide lists three ways to reduce storage cost: use the appropriate storage service for your workload type, monitor with AWS Cost Explorer and billing tools, and understand your data and how it is being used.',
    'What cost-reduction advice does the AWS storage decision guide give for choosing a storage service?',
    ['Use the appropriate storage service for your workload type.', 'Understand your data and how it is being used.'],
    [ev('sent', DG, 'Use the appropriate storage service for your workload type.'),
     ev('sent', DG, 'Understand your data and how it is being used.')],
    scope='cost criterion in the storage decision guide', bul=['4.1.S10'], rel='extended')
add('efs-decision-guide-dr-multi-az-replication', 'efs', 'behavior',
    'The AWS storage decision guide says that choosing a storage service with disaster recovery features, such as replication across multiple Availability Zones, can help minimize the impact of a disaster, and that you should weigh your recovery time objective (RTO) and recovery point objective (RPO).',
    'Which disaster recovery features and objectives does the storage decision guide tell you to weigh?',
    ['replication across multiple Availability Zones'],
    [ev('sent', DG, 'Choosing a storage service that provides disaster recovery features'),
     ev('sent', DG, 'consider factors such as recovery time objectives')],
    scope='disaster recovery criterion in the storage decision guide', bul=['2.2.K11'], rel='extended')
add('fsx-decision-guide-cache-file-cache-row', 'fsx', 'behavior',
    'In the AWS storage decision guide table, the cache storage type is served by Amazon File Cache, a fully managed, scalable, high-speed cache for processing file data stored on premises, in cloud file systems or in Amazon S3.',
    'Which AWS service is the cache storage type in the storage decision guide, and what does it front?',
    ['Amazon File Cache'],
    [ev('row', DG, '|  Cache  |')],
    scope='storage type table of the decision guide', bul=['4.1.K4'], rel='extended')

# ---------- EFS throughput mode choice
add('efs-throughput-elastic-recommended-spiky', 'efs', 'behavior',
    'AWS recommends the default Elastic throughput mode for EFS when you have spiky or unpredictable workloads whose performance requirements are hard to forecast, or when your application drives throughput at an average-to-peak ratio of 5% or less.',
    'When should you choose Elastic throughput for an EFS file system?',
    ['average-to-peak ratio of 5% or less'],
    [ev('sent', PERF, 'Use the default Elastic throughput when you have spiky')],
    scope='EFS throughput modes', bul=['3.1.S1', '4.1.S4'], t0=True)
add('efs-throughput-provisioned-known-requirements', 'efs', 'behavior',
    'AWS says to use Provisioned throughput for EFS if you know your workload performance requirements, or when your application drives throughput at an average-to-peak ratio of 5% or more.',
    'When should you choose Provisioned throughput for an EFS file system?',
    ['average-to-peak ratio of 5% or more'],
    [ev('sent', PERF, 'Use Provisioned throughput if you know')],
    scope='EFS throughput modes', bul=['3.1.S1'], t0=True)
add('efs-throughput-bursting-scales-with-storage', 'efs', 'behavior',
    'AWS says to use Bursting throughput for EFS when you want throughput that scales with the amount of storage in your file system.',
    'When should you choose Bursting throughput for an EFS file system?',
    ['throughput that scales with the amount of storage in your file system'],
    [ev('sent', PERF, 'Use Bursting throughput when you want throughput that scales')],
    scope='EFS throughput modes', bul=['3.1.S1'])
add('efs-throughput-bursting-constrained-move-to-elastic-or-provisioned', 'efs', 'behavior',
    'AWS says that if an EFS file system on Bursting throughput is throughput-constrained, for example it uses more than 80% of the permitted throughput or has used all of its burst credits, you should use Elastic or Provisioned throughput instead.',
    'What should you do when a Bursting throughput EFS file system runs short of throughput?',
    ['more than 80% of the permitted throughput'],
    [ev('sent', PERF, 'If, after using Bursting throughput, you find that your application is throughput-constrained')],
    scope='EFS throughput modes', bul=['3.1.S1'], rel='extended')
add('efs-pricing-elastic-default-pay-for-throughput-used', 'efs', 'default',
    'AWS says Elastic Throughput is the default throughput mode for EFS and is recommended for most workloads. With Elastic Throughput, performance scales automatically with your workload activity and you pay only for the throughput you use.',
    'What is the default EFS throughput mode and how is it billed?',
    ['Elastic Throughput is the default throughput mode'],
    [ev('sent', 'www/efs/pricing', 'Elastic Throughput is the default throughput mode'),
     ev('sent', 'www/efs/pricing', 'With Elastic Throughput, performance automatically scales')],
    scope='new EFS file systems', dm='default', adj=True, cond='throughput mode can be changed', bul=['3.1.S1', '4.1.S10'], t0=True)
add('efs-pricing-provisioned-throughput-predictable-sustained', 'efs', 'pricing-dimension',
    'AWS says to use EFS Provisioned Throughput if you have predictable and high levels of sustained throughput requirements, and that the amount billed in a month is based on the average throughput provisioned in excess of the baseline throughput included with your EFS Standard storage usage.',
    'When is EFS Provisioned Throughput the right choice, and what is billed for it?',
    ['predictable and high levels of sustained throughput requirements'],
    [ev('sent', 'www/efs/pricing', 'You should use Provisioned Throughput if you have predictable'),
     ev('sent', 'www/efs/pricing', 'Your Provisioned Throughput amount billed in a month')],
    scope='EFS Provisioned Throughput', bul=['3.1.S1', '4.1.S10'])

# ---------- EFS cost dimensions
add('efs-pricing-dimensions-storage-activity', 'efs', 'pricing-dimension',
    'AWS says you pay for EFS by the primary and backup storage you use and by your read, write and tiering activity. There is no minimum fee or setup charge.',
    'What do you pay for with Amazon EFS?',
    ['no minimum fee or setup charge', 'read, write, and tiering activity'],
    [ev('sent', 'www/efs/pricing', 'You pay only for the primary and backup storage you use'),
     ev('sent', 'www/efs/pricing', 'There is no minimum fee or setup charge.')],
    scope='Amazon EFS billing', bul=['4.1.S10'], t0=True)
add('efs-pricing-no-charge-same-az-access', 'efs', 'pricing-dimension',
    'AWS says there are no data transfer charges when you access an EFS mount target from within the same Availability Zone, or when you replicate data across EFS file systems within the same Availability Zone.',
    'Is there a data transfer charge for accessing EFS from the same Availability Zone?',
    ['no data transfer charges when accessing an EFS mount target from within the same Availability Zone'],
    [ev('sent', 'www/efs/pricing', 'There are no data transfer charges when accessing an EFS mount target')],
    scope='EFS data transfer within one Region', bul=['4.1.S10'])
add('efs-pricing-replication-pays-both-file-systems', 'efs', 'pricing-dimension',
    'AWS says that with EFS Replication you pay the prevailing storage and read, write and tiering activity rates for both the source and the destination EFS file system, plus any applicable data transfer charges between them.',
    'What do you pay for when you use EFS Replication?',
    ['source and destination EFS file systems'],
    [ev('sent', 'www/efs/pricing', 'With EFS Replication, you pay the prevailing storage')],
    scope='EFS Replication billing', bul=['2.2.K11', '4.1.S10'])
add('efs-pricing-one-zone-for-no-multi-az-need', 'efs', 'behavior',
    'AWS says EFS One Zone file systems are ideal for applications that do not require the Multi-AZ availability and durability of EFS Regional file systems.',
    'When does AWS say an EFS One Zone file system is the right choice?',
    ['do not require the Multi-AZ availability and durability'],
    [ev('sent', 'www/efs/pricing', 'One Zone file systems redundantly store data within a single Availability Zone')],
    scope='EFS One Zone', bul=['4.1.S10', '2.2.K11'])

# ---------- EFS security
add('efs-security-two-encryption-forms', 'efs', 'capability',
    'Amazon EFS supports two forms of encryption for file systems: encryption in transit and encryption at rest.',
    'Which forms of encryption does Amazon EFS support?',
    ['encryption in transit and encryption at rest'],
    [ev('sent', WHAT, 'Amazon EFS supports two forms of encryption for file systems')],
    scope='Amazon EFS', bul=['3.1.K2'], t0=True)
add('efs-security-encryption-at-rest-chosen-at-creation', 'efs', 'behavior',
    'You can enable encryption at rest when you create an EFS file system. If you do, all of your data and metadata is encrypted. You can enable encryption in transit when you mount the file system.',
    'When do you turn on encryption at rest and encryption in transit for EFS?',
    ['when creating an EFS file system', 'when you mount the file system'],
    [ev('sent', WHAT, 'You can enable encryption at rest when creating an EFS file system.'),
     ev('sent', WHAT, 'If you do, all of your data and metadata is encrypted.'),
     ev('sent', WHAT, 'You can enable encryption in transit when you mount the file system.')],
    scope='Amazon EFS', bul=['3.1.K2'])
add('efs-security-access-iam-and-security-groups', 'efs', 'behavior',
    'NFS client access to Amazon EFS is controlled by both IAM policies and network security policies such as security groups. EFS also supports controlling access through POSIX permissions.',
    'What controls NFS client access to an EFS file system?',
    ['both AWS Identity and Access Management (IAM) policies and network security policies'],
    [ev('sent', WHAT, 'NFS client access to Amazon EFS is controlled by both'),
     ev('sent', WHAT, 'Amazon EFS also supports controlling access to your file systems through Portable Operating System Interface (POSIX) permissions.')],
    scope='Amazon EFS', bul=['3.1.K2'])

# ---------- lifecycle and capacity
add('efs-lifecycle-automatic-transition-between-classes', 'efs', 'capability',
    'EFS lifecycle management automatically transitions data between storage classes according to the lifecycle configuration of the file system. The lifecycle policies apply to the entire EFS file system.',
    'Is EFS data tiering automatic, and what does it apply to?',
    ['automatically transition data between storage classes', 'apply to the entire EFS file system'],
    [ev('sent', LIFE, 'Use lifecycle management to automatically transition data between storage classes'),
     ev('sent', LIFE, 'Lifecycle policies apply to the entire EFS file system.')],
    scope='EFS lifecycle management', bul=['4.1.K7', '4.1.S10'], t0=True)
add('efs-lifecycle-metadata-always-in-standard', 'efs', 'behavior',
    'EFS always stores file metadata, including file names, ownership information and directory structure, in the Standard storage class to help ensure consistent metadata performance.',
    'In which EFS storage class is file metadata stored when file contents move to IA or Archive?',
    ['always stored in Standard'],
    [ev('sent', LIFE, 'File metadata, including file names, ownership information')],
    scope='EFS lifecycle management', bul=['4.1.K7'], rel='extended')
add('efs-elastic-storage-grows-and-shrinks-automatically', 'efs', 'capability',
    'Amazon EFS is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, so you do not provision or manage storage capacity.',
    'Do you have to plan or provision EFS storage capacity?',
    ['growing and shrinking automatically'],
    [ev('sent', WHAT, 'Amazon EFS is built to scale on demand to petabytes'),
     ev('sent', WHAT, 'provides serverless, fully elastic file storage')],
    scope='Amazon EFS', bul=['3.1.S2', '4.1.S4'], t0=True)
add('fsx-windows-storage-capacity-increase-only', 'fsx', 'restriction',
    'For FSx for Windows File Server you can only increase a file system storage capacity; you cannot decrease storage capacity.',
    'Can you reduce the storage capacity of an FSx for Windows File Server file system?',
    ['cannot decrease storage capacity'],
    [ev('sent', 'docs/fsx/latest/WindowsGuide/managing-storage-configuration', 'You can only increase a file system')],
    scope='per FSx for Windows File Server file system', bul=['4.1.S4', '3.1.S2'], t0=True)
add('fsx-windows-hdd-to-ssd-only', 'fsx', 'restriction',
    'On an existing FSx for Windows File Server file system you can change the storage type from HDD to SSD but not from SSD to HDD; to move to a different storage type you can restore a backup to a new file system.',
    'Can you change the storage type of an existing FSx for Windows File Server file system?',
    ['from HDD to SSD', 'cannot change the storage type from SSD to HDD'],
    [ev('sent', 'www/fsx/windows/faqs', 'You can change your file system storage type from HDD to SSD'),
     ev('sent', 'www/fsx/windows/faqs', 'Although you cannot change the storage type from SSD to HDD')],
    scope='existing FSx for Windows File Server file systems', bul=['4.1.S4', '4.1.S10'])
add('fsx-ontap-ssd-increase-and-second-gen-decrease', 'fsx', 'behavior',
    'You can increase the SSD storage capacity of an FSx for ONTAP file system as your storage needs grow, and on second-generation file systems you can also decrease SSD storage capacity.',
    'Can you grow or shrink the SSD storage of an FSx for NetApp ONTAP file system?',
    ['increase the SSD storage capacity', 'decrease SSD storage capacity'],
    [ev('sent', 'docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap', 'You can increase the SSD storage capacity of your file system'),
     ev('sent', 'docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap', 'On second-generation file systems, you can also decrease SSD storage capacity')],
    scope='FSx for NetApp ONTAP SSD storage', bul=['4.1.S4'], vol='frequently-changing')
add('fsx-ontap-thin-provisioned-volumes', 'fsx', 'behavior',
    'FSx for ONTAP volumes are thin provisioned, so they consume storage capacity only for the data stored in them and capacity is not reserved in advance.',
    'Do FSx for ONTAP volumes reserve their full size in advance?',
    ['thin provisioned'],
    [ev('sent', 'docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap', 'FSx for ONTAP volumes are thin provisioned')],
    scope='FSx for NetApp ONTAP volumes', bul=['4.1.S4', '4.1.S10'], rel='extended')
add('fsx-ontap-data-tiering-automatic-by-policy', 'fsx', 'capability',
    'FSx for NetApp ONTAP automatically moves data between the SSD tier and the capacity pool tier. Each volume has a tiering policy that controls whether data moves to the capacity tier when it becomes inactive.',
    'Does FSx for ONTAP tier cold data automatically, and what controls it?',
    ['automatically moves data', 'tiering policy'],
    [ev('sent', 'docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap', 'Data tiering is the process by which Amazon FSx for NetApp ONTAP automatically moves data'),
     ev('sent', 'docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap', 'Each volume has a tiering policy that controls whether data is moved')],
    scope='FSx for NetApp ONTAP volumes', bul=['4.1.K7', '4.1.S10'], t0=True)
add('fsx-lustre-release-task-frees-space-needs-task', 'fsx', 'behavior',
    'For FSx for Lustre, a release data repository task frees file system space by releasing files already exported to Amazon S3. The released file content is removed but its metadata stays, and reading the file again retrieves it from S3.',
    'How do you free space on an FSx for Lustre file system linked to S3, and can the data still be read?',
    ['release data repository task', 'transparently retrieves the file content from Amazon S3'],
    [ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'You can use a release data repository task'),
     ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'The released file'),
     ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'transparently retrieves the file content')],
    scope='FSx for Lustre linked to an S3 data repository', bul=['4.1.K7'], t0=True)
add('fsx-lustre-three-data-repository-task-types', 'fsx', 'behavior',
    'FSx for Lustre has three types of data repository tasks: export tasks copy from the file system to the linked S3 bucket, import tasks copy from the bucket to the file system, and release tasks release files that were exported to the bucket.',
    'Which data repository task types does FSx for Lustre have?',
    ['three types of data repository tasks'],
    [ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'There are three types of data repository tasks'),
     ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'tasks export from your Lustre file system'),
     ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'tasks import from a linked S3 bucket'),
     ev('sent', 'docs/fsx/latest/LustreGuide/data-repository-tasks', 'tasks release files exported to a linked S3 bucket')],
    scope='FSx for Lustre', bul=['4.1.K7'])
add('fsx-lustre-intelligent-tiering-recommended-most', 'fsx', 'behavior',
    'AWS says the FSx for Lustre Intelligent-Tiering storage class is suitable and recommended for most workloads that do not need consistent low latency across the full dataset, and that it is fully elastic.',
    'For which workloads does AWS recommend the FSx for Lustre Intelligent-Tiering storage class?',
    ['suitable and recommended for most workloads'],
    [ev('sent', 'docs/fsx/latest/LustreGuide/what-is', 'The Intelligent-Tiering storage class is suitable and recommended'),
     ev('sent', 'docs/fsx/latest/LustreGuide/what-is', 'It provides fully-elastic and cost-effective storage')],
    scope='FSx for Lustre storage classes', bul=['4.1.K7', '4.1.S10'], vol='frequently-changing', t0=True)
add('fsx-openzfs-intelligent-tiering-elastic-grows-shrinks', 'fsx', 'capability',
    'FSx for OpenZFS file systems that use the Intelligent-Tiering storage class use fully elastic, intelligently tiered, regional block storage that automatically grows and shrinks to fit the workload.',
    'Does an FSx for OpenZFS Intelligent-Tiering file system need storage capacity planning?',
    ['automatically grows and shrinks'],
    [ev('sent', 'docs/fsx/latest/OpenZFSGuide/performance-intelligent-tiering', 'Instead of a set of volumes attached to each file server')],
    scope='FSx for OpenZFS Intelligent-Tiering storage class', bul=['4.1.S4', '4.1.K7'], vol='frequently-changing')
add('fsx-openzfs-intelligent-tiering-no-provisioned-iops', 'fsx', 'behavior',
    'With the FSx for OpenZFS Intelligent-Tiering storage class you do not need to provision IOPS; you pay for data access based on usage, in the form of read and write requests.',
    'Do you provision IOPS for FSx for OpenZFS Intelligent-Tiering?',
    ['do not need to provision IOPS'],
    [ev('sent', 'docs/fsx/latest/OpenZFSGuide/performance-intelligent-tiering', 'With the Intelligent-Tiering storage class, you do not need to provision IOPS.'),
     ev('sent', 'docs/fsx/latest/OpenZFSGuide/performance-intelligent-tiering', 'Instead, you pay for data access based on usage')],
    scope='FSx for OpenZFS Intelligent-Tiering storage class', bul=['4.1.S4', '4.1.S10'], vol='frequently-changing')

write('aws-saa-book/_build/work/23-efs-fsx/facts-decisions-03.json', facts)
