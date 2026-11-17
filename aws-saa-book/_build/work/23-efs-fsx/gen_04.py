import sys
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from gen_lib import *

WHA = 'docs/fsx/latest/WindowsGuide/high-availability-multiAZ'
OHA = 'docs/fsx/latest/ONTAPGuide/high-availability-AZ'
ZHA = 'docs/fsx/latest/OpenZFSGuide/availability-durability'
LWI = 'docs/fsx/latest/LustreGuide/what-is'
SQL = 'docs/fsx/latest/WindowsGuide/sql-server'
facts = []

def add(*a, **k):
    facts.append(F(*a, **k))

# ---------- durability and replication across the family
add('fsx-windows-multi-az-two-azs-sync-replication', 'fsx', 'behavior',
    'FSx for Windows File Server Multi-AZ file systems run a high-availability cluster of Windows file servers across two Availability Zones, a preferred AZ and a standby AZ, and replicate data synchronously within each AZ and between the two AZs.',
    'How does an FSx for Windows File Server Multi-AZ file system protect data across Availability Zones?',
    ['spread across two AZs (a preferred AZ and a standby AZ)', 'replicated synchronously within each individual AZ and between the two AZs'],
    [ev('sent', WHA, 'Multi-AZ file systems are composed of a high-availability cluster of Windows file servers'),
     ev('sent', WHA, 'Data is replicated synchronously within each individual AZ and between the two AZs.')],
    scope='FSx for Windows File Server Multi-AZ deployment', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-windows-recommend-multi-az-for-production', 'fsx', 'behavior',
    'AWS recommends Multi-AZ file systems for most FSx for Windows File Server production workloads, and describes Single-AZ as a cost-efficient choice for test and development workloads, for workloads with replication built into the application layer, and for workloads with relaxed availability and RPO needs.',
    'Which FSx for Windows File Server deployment type does AWS recommend for production, and when is Single-AZ enough?',
    ['We recommend using Multi-AZ file systems for most production workloads'],
    [ev('sent', WHA, 'We recommend using Multi-AZ file systems for most production workloads'),
     ev('sent', WHA, 'Single-AZ deployment is designed as a cost-efficient solution for test and development workloads')],
    scope='FSx for Windows File Server deployment types', bul=['2.2.K11', '4.1.S10'], t0=True)
add('fsx-windows-single-az-about-30-minutes-downtime', 'fsx', 'behavior',
    'FSx for Windows File Server Single-AZ file systems usually experience about 30 minutes of downtime during failure recovery events and during the planned maintenance window that you configure for the file system.',
    'How much downtime can an FSx for Windows File Server Single-AZ file system have during failure recovery?',
    ['about 30 minutes of downtime'],
    [ev('sent', WHA, 'Single-AZ file systems usually experience about 30 minutes of downtime')],
    scope='FSx for Windows File Server Single-AZ deployment', bul=['2.2.K11'])
add('fsx-windows-multi-az-failover-under-30-seconds', 'fsx', 'behavior',
    'A failover of an FSx for Windows File Server Multi-AZ file system typically completes in less than 30 seconds, from detection of the failure on the active file server to promotion of the standby file server to active status.',
    'How long does an FSx for Windows File Server Multi-AZ failover typically take?',
    ['less than 30 seconds'],
    [ev('sent', WHA, 'A failover typically completes in less than 30 seconds from the detection of the failure')],
    scope='FSx for Windows File Server Multi-AZ deployment', bul=['2.2.K11'])
add('fsx-ontap-single-az-1-to-12-ha-pairs', 'fsx', 'behavior',
    'FSx for NetApp ONTAP Single-AZ 1 is a first-generation file system with one high-availability pair, and Single-AZ 2 is a second-generation file system with 1 to 12 high-availability pairs.',
    'How many HA pairs can an FSx for NetApp ONTAP Single-AZ file system have?',
    ['1–12 HA pairs'],
    [ev('sent', OHA, 'Single-AZ 1 is a first-generation file system with one high-availability (HA) pair')],
    scope='FSx for NetApp ONTAP Single-AZ deployment types', dm='', bul=['2.2.K11', '4.1.K4'])
add('fsx-ontap-multi-az-sync-replication-across-azs', 'fsx', 'behavior',
    'FSx for NetApp ONTAP Multi-AZ file systems have a single HA pair whose standby file server is in a different Availability Zone from the active one, and any changes written to the file system are synchronously replicated across Availability Zones to the standby.',
    'How does an FSx for NetApp ONTAP Multi-AZ file system keep a copy in a second Availability Zone?',
    ['synchronously replicated across Availability Zones to the standby'],
    [ev('sent', OHA, 'Multi-AZ deployments have a single HA pair of file servers'),
     ev('sent', OHA, 'Any changes written to your file system are synchronously replicated')],
    scope='FSx for NetApp ONTAP Multi-AZ deployment types', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-ontap-single-az-cost-optimized-dev-test', 'fsx', 'behavior',
    'AWS says FSx for NetApp ONTAP Single-AZ file systems are designed for use cases that do not need the data resiliency model of a Multi-AZ file system, and are a cost-optimized choice for development and test environments or secondary copies of data stored elsewhere.',
    'When does AWS say an FSx for NetApp ONTAP Single-AZ file system is the right choice?',
    ['cost-optimized solution'],
    [ev('sent', OHA, 'Single-AZ file systems are designed for use cases that do not require the data resiliency model'),
     ev('sent', OHA, 'They provide a cost-optimized solution for use cases')],
    scope='FSx for NetApp ONTAP Single-AZ deployment types', bul=['2.2.K11', '4.1.S10'])
add('fsx-openzfs-three-deployment-types', 'fsx', 'behavior',
    'FSx for OpenZFS supports three file system deployment types: Multi-AZ (HA), Single-AZ (HA) and Single-AZ (non-HA).',
    'Which deployment types does FSx for OpenZFS offer?',
    ['Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA)'],
    [ev('sent', ZHA, 'FSx for OpenZFS supports three file system deployment types')],
    scope='FSx for OpenZFS', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-openzfs-multi-az-sync-two-azs-failover-60-seconds', 'fsx', 'behavior',
    'FSx for OpenZFS Multi-AZ (HA) file systems replicate data synchronously within each Availability Zone and between the two Availability Zones, and fail over to the standby Availability Zone automatically, typically within 60 seconds.',
    'How does an FSx for OpenZFS Multi-AZ (HA) file system protect data, and how fast does it fail over?',
    ['typically within 60 seconds'],
    [ev('sent', ZHA, 'Multi-AZ (HA) file systems are composed of a high-availability pair of file servers'),
     ev('sent', ZHA, 'Relative to Single-AZ (non-HA and HA) file systems, Multi-AZ (HA) file systems provide enhanced durability'),
     ev('sent', ZHA, 'also offer enhanced availability by automatically failing over')],
    scope='FSx for OpenZFS Multi-AZ (HA) deployment', bul=['2.2.K11', '4.1.K4'])
add('fsx-openzfs-single-az-non-ha-about-30-minutes', 'fsx', 'behavior',
    'FSx for OpenZFS Single-AZ (non-HA) file systems usually experience about 30 minutes of downtime during failure recovery events and during the planned maintenance window.',
    'How much downtime can an FSx for OpenZFS Single-AZ (non-HA) file system have during failure recovery?',
    ['about 30 minutes of downtime'],
    [ev('sent', ZHA, 'usually experience about 30 minutes of downtime')],
    scope='FSx for OpenZFS Single-AZ (non-HA) deployment', bul=['2.2.K11'])
add('fsx-openzfs-single-az-ha-cost-effective-no-cross-az', 'fsx', 'behavior',
    'AWS recommends FSx for OpenZFS Single-AZ (HA) file systems as a cost-effective choice for workloads that need high availability but not storage redundancy across Availability Zones, including analytics and EDA workloads.',
    'When does AWS recommend an FSx for OpenZFS Single-AZ (HA) file system?',
    ['cost-effective solution for workloads that need high availability'],
    [ev('sent', ZHA, 'Single-AZ (HA) file systems are recommended as a cost-effective solution')],
    scope='FSx for OpenZFS Single-AZ (HA) deployment', bul=['2.2.K11', '4.1.S10'])
add('fsx-lustre-scratch-not-replicated-persistent-replicated', 'fsx', 'behavior',
    'FSx for Lustre scratch file systems suit temporary storage and shorter-term processing, and their data is not replicated and does not persist if a file server fails. In persistent file systems, data is replicated and file servers are replaced if they fail.',
    'How do FSx for Lustre scratch and persistent file systems differ in durability?',
    ['Data is not replicated and does not persist if a file server fails', 'In persistent file systems, data is replicated'],
    [ev('sent', LWI, 'Scratch file systems are ideal for temporary storage'),
     ev('sent', LWI, 'Data is not replicated and does not persist if a file server fails.'),
     ev('sent', LWI, 'In persistent file systems, data is replicated')],
    scope='FSx for Lustre deployment types', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-lustre-persistent-for-longer-term-throughput', 'fsx', 'behavior',
    'AWS says FSx for Lustre persistent file systems are ideal for longer-term storage and throughput-focused workloads.',
    'Which FSx for Lustre deployment type suits longer-term storage?',
    ['longer-term storage and throughput-focused workloads'],
    [ev('sent', LWI, 'Persistent file systems are ideal for longer-term storage')],
    scope='FSx for Lustre deployment types', bul=['2.2.K11', '4.1.K4'], rel='extended')

# ---------- legacy and purpose-built picks
add('fsx-windows-ca-shares-required-multi-az-for-sql-server', 'fsx', 'restriction',
    'For Microsoft SQL Server, FSx for Windows File Server supports continuously available (CA) file shares. You can create CA shares on Single-AZ 2 file systems, but it is required that you use CA shares on Multi-AZ file systems for all SQL Server deployments, whether HA or not.',
    'Which FSx for Windows File Server deployment type must hold SQL Server data files on CA shares?',
    ['continuously available (CA) file shares', 'required that you use CA shares on Multi-AZ file systems'],
    [ev('sent', SQL, 'Amazon FSx is optimized to provide shared storage for SQL Server databases'),
     ev('sent', SQL, 'While you can create CA shares on Single-AZ 2 file systems')],
    scope='FSx for Windows File Server with Microsoft SQL Server', bul=['2.2.S8', '2.2.S7'], t0=True)
add('fsx-windows-sql-server-two-uses-data-files-and-witness', 'fsx', 'capability',
    'You can use FSx for Windows File Server as shared storage for high availability Microsoft SQL Server in two ways: as storage for active data files and as an SMB file share witness.',
    'In which two ways can FSx for Windows File Server serve a SQL Server high availability deployment?',
    ['storage for active data files and as an SMB file share witness'],
    [ev('sent', SQL, 'You can use FSx for Windows File Server as shared storage for High Availability (HA) Microsoft SQL Server deployments in two ways')],
    scope='FSx for Windows File Server with Microsoft SQL Server', bul=['2.2.S8'])
add('fsx-windows-sql-server-ssd-recommended', 'fsx', 'behavior',
    'AWS recommends SSD storage for SQL Server on FSx for Windows File Server, because SSD storage is designed for the highest-performance and most latency-sensitive workloads, including databases.',
    'Which FSx for Windows File Server storage type does AWS recommend for SQL Server?',
    ['SSD storage is recommended for SQL Server'],
    [ev('sent', SQL, 'SSD storage is recommended for SQL Server.'),
     ev('sent', SQL, 'SSD storage is designed for the highest-performance and most latency-sensitive workloads')],
    scope='FSx for Windows File Server with Microsoft SQL Server', bul=['2.2.S8', '3.1.S1'])
add('fsx-windows-faq-workloads-crm-erp-dotnet-home-dirs', 'fsx', 'behavior',
    'The FSx for Windows File Server FAQ says the service was designed for use cases that need Windows shared file storage, such as CRM, ERP, custom or .NET applications, home directories, web serving and content management, and Microsoft SQL Server.',
    'Which workloads is FSx for Windows File Server designed for?',
    ['Windows shared file storage'],
    [ev('sent', 'www/fsx/windows/faqs', 'Amazon FSx was designed for a broad set of use cases that require Windows shared file storage')],
    scope='FSx for Windows File Server', bul=['2.2.S7', '2.2.S8'], t0=True)
add('efs-faq-use-cases-and-one-zone-fit', 'efs', 'behavior',
    'The EFS FAQ says EFS supports big data and analytics, media processing, content management, web serving and home directories; Standard storage classes suit workloads needing the highest durability and availability, and One Zone storage classes suit development, build and staging environments.',
    'Which workloads does the EFS FAQ list for EFS, and where does it place One Zone?',
    ['highest levels of durability and availability'],
    [ev('sent', 'www/efs/faq', 'Amazon EFS provides performance for a broad spectrum of workloads and applications'),
     ev('sent', 'www/efs/faq', 'Amazon EFS Standard storage classes are ideal for workloads'),
     ev('sent', 'www/efs/faq', 'EFS One Zone storage classes are ideal for workloads such as development')],
    scope='Amazon EFS', bul=['2.2.S7', '2.2.S8', '4.1.S10'])
add('efs-whitepaper-container-storage-lift-and-shift-use-cases', 'efs', 'behavior',
    'The AWS overview whitepaper names these EFS use cases: lift-and-shift enterprise applications, big data analytics, web serving and content management, application development and testing, media and entertainment workflows, database backups and container storage.',
    'Which use cases does the AWS overview whitepaper give for Amazon EFS?',
    ['lift-and-shift enterprise applications', 'container storage'],
    [ev('sent', 'docs/whitepapers/latest/aws-overview/storage-services', 'Use cases such as lift-and-shift enterprise applications')],
    scope='Amazon EFS', bul=['2.2.S7', '2.2.S8'])

# ---------- FSx cost dimensions
add('fsx-windows-pricing-five-categories', 'fsx', 'pricing-dimension',
    'AWS says the cost of FSx for Windows File Server has five categories: storage capacity, SSD IOPS, throughput capacity, backups and data transfer.',
    'What do you pay for with FSx for Windows File Server?',
    ['storage capacity, SSD IOPS, throughput capacity, backups, and data transfer'],
    [ev('sent', 'www/fsx/windows/pricing', 'There are five categories to consider when storing and managing your data')],
    scope='FSx for Windows File Server billing', bul=['4.1.S10'], t0=True)
add('fsx-windows-pricing-multi-az-replication-in-throughput-price', 'fsx', 'pricing-dimension',
    'For FSx for Windows File Server Multi-AZ file systems, the cost of transferring data between Availability Zones for replication is included in the throughput capacity price.',
    'Do you pay separately for cross-AZ replication traffic on an FSx for Windows File Server Multi-AZ file system?',
    ['included in the throughput capacity price'],
    [ev('sent', 'www/fsx/windows/pricing', 'For multi-AZ file systems, the cost to transfer data between AZs for replication of data is included')],
    scope='FSx for Windows File Server Multi-AZ billing', bul=['4.1.S10'])
add('fsx-windows-pricing-ssd-iops-3-per-gb-included', 'fsx', 'default',
    'FSx for Windows File Server includes 3 IOPS for every GB of SSD storage by default; you can optionally provision more and pay for the average IOPS provisioned above the included rate.',
    'How many SSD IOPS per GB are included by default with FSx for Windows File Server, and how are extra IOPS billed?',
    ['3 IOPS are included for every GB of SSD storage'],
    [ev('sent', 'www/fsx/windows/pricing', 'By default, 3 IOPS are included for every GB of SSD storage.'),
     ev('sent', 'www/fsx/windows/pricing', 'You can optionally provision a higher level of IOPS')],
    scope='per GB of SSD storage', dm='default', adj=True, cond='you can provision a higher level of IOPS', bul=['4.1.S10', '3.1.S1'])
add('fsx-ontap-pricing-five-components', 'fsx', 'pricing-dimension',
    'AWS says the cost of FSx for NetApp ONTAP has five components: SSD storage, SSD IOPS, capacity pool usage, throughput capacity and backups. S3 requests are charged when you access data through S3 Access Points.',
    'What do you pay for with FSx for NetApp ONTAP?',
    ['SSD storage, SSD IOPS, capacity pool usage, throughput capacity, and backups'],
    [ev('sent', 'www/fsx/netapp-ontap/pricing', 'There are five Amazon FSx for NetApp ONTAP components to consider'),
     ev('sent', 'www/fsx/netapp-ontap/pricing', 'S3 requests: You pay for S3 requests when accessing data stored on your FSx for ONTAP file systems using S3 Access Points.')],
    scope='FSx for NetApp ONTAP billing', bul=['4.1.S10'], t0=True)
add('fsx-ontap-pricing-capacity-pool-pay-for-consumed-plus-requests', 'fsx', 'pricing-dimension',
    'For FSx for NetApp ONTAP capacity pool storage you pay only for the storage space consumed, and you also pay request costs for each read and write operation whenever the data is accessed.',
    'How is FSx for NetApp ONTAP capacity pool storage billed?',
    ['pay only for the storage space consumed', 'request costs'],
    [ev('sent', 'www/fsx/netapp-ontap/pricing', 'With capacity pool storage, you pay only for the storage space consumed.'),
     ev('sent', 'www/fsx/netapp-ontap/pricing', 'For data that is in capacity pool storage, you also pay requests costs')],
    scope='FSx for NetApp ONTAP capacity pool storage', bul=['4.1.S10', '4.1.K7'])
add('fsx-lustre-pricing-intelligent-tiering-dimensions', 'fsx', 'pricing-dimension',
    'For FSx for Lustre Intelligent-Tiering you pay for the average storage consumed in each access tier, an optional SSD read cache, data access (read and write requests) and provisioned throughput capacity, plus monitoring and automation.',
    'What do you pay for with the FSx for Lustre Intelligent-Tiering storage class?',
    ['Frequent Access tier, Infrequent Access tier, and Archive Instant Access tier'],
    [ev('sent', 'www/fsx/lustre/pricing', 'Intelligent-Tiering storage: You pay for the average amount of storage consumed per access tier'),
     ev('sent', 'www/fsx/lustre/pricing', 'Monitoring and automation: You pay for the average amount of all storage'),
     ev('sent', 'www/fsx/lustre/pricing', 'SSD read cache (optional): You pay for the average amount of cache provisioned'),
     ev('sent', 'www/fsx/lustre/pricing', 'Data access: You pay for the average number of read and write request operations'),
     ev('sent', 'www/fsx/lustre/pricing', 'Throughput capacity: You pay for the average throughput capacity')],
    scope='FSx for Lustre Intelligent-Tiering storage class', bul=['4.1.S10', '4.1.K7'], vol='frequently-changing')
add('fsx-openzfs-pricing-multi-az-no-transfer-fees', 'fsx', 'pricing-dimension',
    'For FSx for OpenZFS Multi-AZ file systems there are no data transfer fees and cross-AZ data replication costs are included in the throughput capacity price. For Single-AZ file systems you pay for data transfer in both directions when you access the file system from a non-preferred Availability Zone in the same Region.',
    'Do you pay for cross-AZ traffic on FSx for OpenZFS?',
    ['no data transfer fees'],
    [ev('sent', 'www/fsx/openzfs/pricing', 'You pay for data transfer in both directions when accessing your Single-AZ file system'),
     ev('sent', 'www/fsx/openzfs/pricing', 'For Multi-AZ file systems, we charge no data transfer fees')],
    scope='FSx for OpenZFS data transfer', bul=['4.1.S10', '2.2.K11'])

# ---------- case studies
CS = 'customer case study on the AWS site'
CC = 'a customer statement published by AWS, not a service guarantee'
add('fsx-case-adobe-lustre-gpu-never-idle', 'fsx', 'case-study',
    'The AWS case study says Adobe used Amazon FSx for Lustre high-performance file storage for fast access to data and to make sure GPU resources are never left idle.',
    'What does the Adobe case study say it used FSx for Lustre for?',
    ['GPU resources are never left idle'],
    [ev('sent', 'www/solutions/case-studies/adobe-case-study', 'Adobe used Amazon FSx for Lustre high-performance file storage')],
    scope=CS, cond=CC, bul=['4.1.K4', '2.2.S8'], rel='reference')
add('fsx-case-phillips66-ontap-capacity-pool-80-percent', 'fsx', 'case-study',
    'The AWS case study says Phillips 66 cycled 90 percent of its data into the elastic capacity-pool tier of FSx for NetApp ONTAP, which reduced its storage costs by 80 percent.',
    'What storage cost result does the Phillips 66 case study report for FSx for NetApp ONTAP capacity-pool tiering?',
    ['reduced its storage costs by 80 percent'],
    [ev('sent', 'www/solutions/case-studies/phillips66-migration-case-study', 'Phillips 66 has cycled 90 percent of its data')],
    scope=CS, cond=CC, bul=['4.1.K4', '4.1.S10'], rel='reference')
add('fsx-case-phillips66-snapmirror-no-refactoring', 'fsx', 'case-study',
    'The AWS case study says Phillips 66 used NetApp SnapMirror to migrate to FSx for NetApp ONTAP while preserving its existing data organization and security controls, and without rewriting, rearchitecting or refactoring code.',
    'How did Phillips 66 migrate its on-premises NetApp ONTAP data to FSx for NetApp ONTAP?',
    ['the need for code rewriting, rearchitecting, or refactoring'],
    [ev('sent', 'www/solutions/case-studies/phillips66-migration-case-study', 'Phillips 66 relied on NetApp SnapMirror'),
     ev('sent', 'www/solutions/case-studies/phillips66-migration-case-study', 'By removing the need for code rewriting, rearchitecting, or refactoring')],
    scope=CS, cond=CC, bul=['4.1.K4', '2.2.S7'], rel='reference')
add('fsx-case-avionte-windows-file-server-rdp-content', 'fsx', 'case-study',
    'The AWS case study says Avionté uses Amazon FSx for Windows File Server, fully managed file storage built on Windows Server, to persist the application content of its remote desktop protocol based application.',
    'What does the Avionté case study use FSx for Windows File Server for?',
    ['persist its remote desktop protocol application content'],
    [ev('sent', 'www/solutions/case-studies/avionte-case-study', 'To persist its remote desktop protocol application content')],
    scope=CS, cond=CC, bul=['4.1.K4', '2.2.S7'], rel='reference')
add('efs-case-mazzuma-model-data-efs-sagemaker', 'efs', 'case-study',
    'The AWS case study says Mazzuma used Amazon EFS, a serverless, fully elastic file storage service, to store and transfer model data into Amazon SageMaker at speeds of 1.5 Gbps.',
    'What does the Mazzuma case study use Amazon EFS for?',
    ['serverless, fully elastic file storage service'],
    [ev('sent', 'www/solutions/case-studies/mazzuma', 'To store and transfer model data into Amazon SageMaker')],
    scope=CS, cond=CC, bul=['4.1.K4', '3.1.K2'], rel='reference')
add('efs-case-world-kinect-efs-oracle-application-files', 'efs', 'case-study',
    'The AWS case study says World Kinect, after migrating its Oracle E-Business Suite to AWS, used Amazon EFS to automatically provision and manage application files.',
    'What does the World Kinect case study use Amazon EFS for?',
    ['automatically provision and manage application files'],
    [ev('sent', 'www/solutions/case-studies/world-kinect-services-case-study', 'AWS helped World Kinect migrate its Oracle E-Business Suite to AWS'),
     ev('sent', 'www/solutions/case-studies/world-kinect-services-case-study', 'As a result, World Kinect experienced increased resilience')],
    scope=CS, cond=CC, bul=['4.1.K4', '2.2.S7'], rel='reference')
add('efs-case-ginkgo-migrating-active-projects-to-efs', 'efs', 'case-study',
    'The AWS case study says Ginkgo Bioworks is migrating to Amazon EFS, a serverless, fully elastic file system, to get more insight into its file usage and optimize further.',
    'Why is Ginkgo Bioworks migrating to Amazon EFS, according to its AWS case study?',
    ['greater level of insight into its file usage'],
    [ev('sent', 'www/solutions/case-studies/ginkgo-bioworks-case-study', 'To achieve a greater level of insight into its file usage')],
    scope=CS, cond=CC, bul=['4.1.K4', '4.1.S10'], rel='reference')

write('aws-saa-book/_build/work/23-efs-fsx/facts-decisions-04.json', facts)
