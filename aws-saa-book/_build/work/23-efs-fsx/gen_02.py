import sys
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from gen_lib import *

W = 'www/fsx/when-to-choose-fsx'
T = 'AWS "Choosing an Amazon FSx File System" page'
facts = []

def add(*a, **k):
    facts.append(F(*a, **k))

# --- familiar file system table
add('fsx-when-to-choose-lustre-from-parallel-fs', 'fsx', 'behavior',
    'The AWS page on choosing an FSx file system recommends FSx for Lustre when your current storage technology is Lustre or another parallel file system.',
    'Which FSx file system matches an existing Lustre or other parallel file system?',
    ['FSx for Lustre'], [ev('row', W, '| Lustre or other parallel file systems |')],
    scope='FSx file system choice by current storage technology', bul=['4.1.K4', '2.2.S8'], t0=True)
add('fsx-when-to-choose-ontap-from-nas', 'fsx', 'behavior',
    'The AWS page on choosing an FSx file system recommends FSx for NetApp ONTAP when your current storage technology is NetApp ONTAP or another NAS appliance.',
    'Which FSx file system matches an existing NetApp ONTAP system or another NAS appliance?',
    ['FSx for NetApp ONTAP'], [ev('row', W, '| NetApp ONTAP or other NAS appliances |')],
    scope='FSx file system choice by current storage technology', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)
add('fsx-when-to-choose-openzfs-from-zfs', 'fsx', 'behavior',
    'The AWS page on choosing an FSx file system recommends FSx for OpenZFS when your current storage technology is ZFS or another Linux-based file server.',
    'Which FSx file system matches an existing ZFS or other Linux-based file server?',
    ['FSx for OpenZFS'], [ev('row', W, '| ZFS or other Linux-based file servers |')],
    scope='FSx file system choice by current storage technology', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)
add('fsx-when-to-choose-windows-from-windows-server', 'fsx', 'behavior',
    'The AWS page on choosing an FSx file system recommends FSx for Windows File Server when your current storage technology is Microsoft Windows Server.',
    'Which FSx file system matches an existing Microsoft Windows Server file server?',
    ['FSx for Windows File Server'], [ev('row', W, '| Microsoft Windows Server |')],
    scope='FSx file system choice by current storage technology', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)

# --- performance and scale
add('fsx-compare-latency-by-type', 'fsx', 'behavior',
    'AWS lists latency of less than 1 ms for FSx for NetApp ONTAP, FSx for Windows File Server and FSx for Lustre, and less than 0.5 ms for FSx for OpenZFS.',
    'What latency does AWS list for each FSx file system type?',
    [('ontap', '<1 ms'), ('openzfs', '<0.5 ms')], [ev('row', W, '| Latency |')],
    scope='per FSx file system type', bul=['4.1.K4', '3.1.S1'])
add('fsx-compare-max-throughput-per-file-system', 'fsx', 'limit',
    'AWS lists maximum throughput per file system of 72-80 GB/s for FSx for NetApp ONTAP, 10-21 GB/s for OpenZFS, 12-20 GB/s for Windows File Server and 1000 GB/s for Lustre. The lower number of a range is baseline throughput, and the upper number is a higher level enabled by caching, bursting and compression.',
    'What maximum throughput per file system does AWS list for each FSx file system type, and what do the two numbers of a range mean?',
    [('ontap', '72-80 GB/s'), ('openzfs', '10-21 GB/s'), ('windows', '12-20 GB/s'), ('lustre', '1000 GB/s')],
    [ev('row', W, '| Max. throughput per file system |'),
     ev('sent', W, 'The lower number in the range refers to baseline throughput.'),
     ev('sent', W, 'The upper number in the range refers to higher levels of throughput')],
    scope='per file system, per FSx file system type', dm='max', cond='a range gives baseline (lower) to enhanced (upper) throughput', bul=['4.1.K4', '3.1.S1'], t0=True)
add('fsx-compare-max-throughput-single-client', 'fsx', 'limit',
    'AWS lists maximum throughput available to a single client accessing a file system as 18 GB/s for FSx for NetApp ONTAP, 10 GB/s for OpenZFS, 20 GB/s for Windows File Server and 150 GB/s for Lustre.',
    'What is the maximum throughput one client can get from each FSx file system type?',
    [('ontap', '18 GB/s'), ('openzfs', '10 GB/s'), ('windows', '20 GB/s'), ('lustre', '150 GB/s')],
    [ev('row', W, '| Max. throughput available to a single client')],
    scope='per client, per FSx file system type', dm='max', bul=['4.1.K4', '3.1.S1'])
add('fsx-compare-max-iops-per-file-system', 'fsx', 'limit',
    'AWS lists maximum IOPS per file system as millions for FSx for NetApp ONTAP, 1-2 million for OpenZFS, hundreds of thousands for Windows File Server and millions for Lustre.',
    'What maximum IOPS per file system does AWS list for each FSx file system type?',
    [('openzfs', '1-2 million'), ('windows', 'Hundreds of thousands')], [ev('row', W, '| Max. IOPS per file system |')],
    scope='per file system, per FSx file system type', dm='max', bul=['4.1.K4', '3.1.S1'])
add('fsx-compare-max-file-system-size', 'fsx', 'limit',
    'AWS lists maximum file system size as virtually unlimited (tens of PBs) for FSx for NetApp ONTAP, 512 TiB for OpenZFS, 64 TiB for Windows File Server and multiple PBs for Lustre.',
    'What maximum file system size does AWS list for each FSx file system type?',
    [('openzfs', '512 TiB'), ('windows', '64 TiB'), ('ontap', 'Virtually unlimited (10s of PBs)'), ('lustre', 'Multiple PBs')],
    [ev('row', W, '| Maximum file system size |')],
    scope='per file system, per FSx file system type', dm='max', bul=['4.1.K4', '3.1.S2'], t0=True)

# --- accessibility
add('fsx-compare-client-compatibility', 'fsx', 'behavior',
    'AWS lists client compatibility as Windows, Linux and macOS for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and Linux for FSx for Lustre.',
    'Which client operating systems does each FSx file system type support?',
    [('lustre', 'Linux')], [ev('row', W, '| Client compatibility |')],
    scope='per FSx file system type', bul=['4.1.K4', '2.2.S8'])
add('fsx-compare-protocol-support', 'fsx', 'behavior',
    'AWS lists protocol support as SMB, NFS and iSCSI for FSx for NetApp ONTAP, NFS for OpenZFS, SMB for Windows File Server, and a custom POSIX-compliant protocol optimized for performance for Lustre.',
    'Which protocols does each FSx file system type support?',
    [('ontap', 'SMB 2.0, 2.1, 3.0, 3.1.1 NFS 3, 4.0, 4.1, 4.2 iSCSI (shared block storage)'), ('openzfs', 'NFS 3, 4.0, 4.1, 4.2')],
    [ev('row', W, '| Protocol support |')],
    scope='per FSx file system type', bul=['4.1.K4', '2.2.S8'], t0=True)
add('fsx-compare-lustre-only-s3-import-export', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, only FSx for Lustre is marked as supporting automatic import and export of S3 data sets.',
    'Which FSx file system type automatically imports and exports S3 data sets?',
    ['Automatic import/export of S3 data sets'], [ev('row', W, '| Automatic import/export of S3 data sets |')],
    scope='FSx file system comparison page', bul=['4.1.K4', '2.2.S8'], t0=True)

# --- hybrid
add('fsx-compare-ontap-only-hybrid-caching', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for on-premises caching of FSx data, with NetApp Global File Cache and NetApp FlexCache.',
    'Which FSx file system supports caching FSx data on premises?',
    ['NetApp Global File Cache, NetApp FlexCache'], [ev('row', W, '| On-premises caching of FSx data |')],
    scope='hybrid usage, FSx file system comparison page', bul=['4.1.K4', '2.2.S8'])
add('fsx-compare-ontap-only-snapmirror-dr-from-on-premises', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for backup and disaster recovery from on premises to AWS, using NetApp SnapMirror.',
    'Which FSx file system supports backup and disaster recovery from on premises to AWS?',
    ['NetApp SnapMirror'], [ev('row', W, '| Backup and disaster recovery from on premises to AWS |')],
    scope='hybrid usage, FSx file system comparison page', bul=['4.1.K4', '2.2.S8'])
add('fsx-compare-ontap-only-compute-burst-flexcache', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, only FSx for NetApp ONTAP is marked for compute burst to the cloud, using FSx as an on-AWS cache of on-premises data with NetApp FlexCache.',
    'Which FSx file system lets you burst compute to the cloud with FSx as a cache of on-premises data?',
    ['NetApp FlexCache'], [ev('row', W, '| Support for compute burst to the cloud')],
    scope='hybrid usage, FSx file system comparison page', bul=['4.1.K4', '2.2.S8'])

# --- price and performance
add('fsx-compare-cold-data-options', 'fsx', 'behavior',
    'For cost-optimized storage of cold, infrequently accessed data, AWS lists a low-cost tier with cold data cycled to it automatically for FSx for NetApp ONTAP, an HDD storage option for FSx for Windows File Server and an HDD storage option for FSx for Lustre; FSx for OpenZFS is not marked.',
    'How does each FSx file system type offer cheaper storage for cold data?',
    [('ontap', 'Low-cost tier with cold data automatically cycled to it'), ('hdd', 'HDD storage option')],
    [ev('row', W, '| Cost-optimized storage for cold, infrequently-accessed data |')],
    scope='price/performance table, FSx file system comparison page', bul=['4.1.K4', '4.1.S10', '4.1.K7'], t0=True)
add('fsx-compare-dedup-ontap-windows-only', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, data deduplication is marked only for FSx for NetApp ONTAP and FSx for Windows File Server, and it applies to both file system storage and backups.',
    'Which FSx file system types support data deduplication?',
    ['Data deduplication'], [ev('row', W, '| Data deduplication ** |'), ev('sent', W, 'Applies to both file system storage and backups')],
    scope='price/performance table, FSx file system comparison page', bul=['4.1.K4', '4.1.S10'])

# --- availability
add('fsx-compare-deployment-options', 'fsx', 'behavior',
    'AWS lists deployment options of Single-AZ and Multi-AZ for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and Single-AZ with Persistent or Scratch for FSx for Lustre.',
    'Which deployment options does each FSx file system type offer?',
    [('lustre', 'Single-AZ - Persistent or Scratch'), ('others', 'Single-AZ and Multi-AZ')],
    [ev('row', W, '| Deployment options |')],
    scope='per FSx file system type', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-compare-availability-sla', 'fsx', 'sla',
    'AWS lists the availability SLA as 99.99% for Multi-AZ and 99.9% for Single-AZ on FSx for NetApp ONTAP; 99.99% for Multi-AZ and 99.5% for Single-AZ on OpenZFS and Windows File Server; and 99.5% for Single-AZ on Lustre.',
    'What availability SLA does AWS list for each FSx file system type and deployment option?',
    [('multi', '99.99%'), ('ontap-single', '99.9%'), ('single', '99.5%')],
    [ev('row', W, '| Availability SLA |')],
    scope='per FSx file system type and deployment type', bul=['2.2.K11', '4.1.K4'], t0=True)
add('fsx-compare-snapshots-restore-not-lustre', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, inline instantaneous snapshots are marked for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and are not marked for FSx for Lustre.',
    'Which FSx file system types offer inline instantaneous snapshots?',
    ['Inline instantaneous snapshots'], [ev('row', W, '| Inline instantaneous snapshots |')],
    scope='availability and data protection table', bul=['4.1.K4'])
add('fsx-compare-instant-cloning-ontap-openzfs', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, instant cloning is marked only for FSx for NetApp ONTAP and FSx for OpenZFS.',
    'Which FSx file system types offer instant cloning?',
    ['Instant cloning'], [ev('row', W, '| Instant cloning |')],
    scope='availability and data protection table', bul=['4.1.K4', '2.2.S8'])
add('fsx-compare-cross-region-replication', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, cross-Region replication is marked for FSx for NetApp ONTAP (NetApp SnapMirror) and for FSx for Lustre (using S3 cross-region replication), and not for OpenZFS or Windows File Server.',
    'Which FSx file system types support cross-Region replication, and how?',
    [('ontap', 'NetApp SnapMirror'), ('lustre', 'Using S3 cross-region replication')],
    [ev('row', W, '| Cross-region replication |')],
    scope='availability and data protection table', bul=['2.2.K11', '4.1.K4'])
add('fsx-compare-cross-region-account-backups', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, cross-Region and cross-account backups are marked for FSx for OpenZFS (cross-Region), Windows File Server and Lustre, and not marked for FSx for NetApp ONTAP.',
    'Which FSx file system types support cross-Region or cross-account backups according to the comparison page?',
    ['Cross-region/cross-account backups'], [ev('row', W, '| Cross-region/cross-account backups |')],
    scope='availability and data protection table', vol='frequently-changing', bul=['2.2.K11', '4.1.K4'],
    note='ONTAP cross-Region backup copy was added 2026-08-27 (see the change fact); this page predates it.')

# --- security and compliance
add('fsx-compare-active-directory-ontap-windows', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, Active Directory support for file system access authentication and access control is marked only for FSx for NetApp ONTAP and FSx for Windows File Server.',
    'Which FSx file system types support Active Directory authentication and access control?',
    ['Active Directory support for file system access authentication and access control'],
    [ev('row', W, '| Active Directory support for file system access')],
    scope='security and compliance table', bul=['4.1.K4', '2.2.S7'], t0=True)
add('fsx-compare-file-access-auditing-ontap-windows', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, file access auditing is marked only for FSx for NetApp ONTAP and FSx for Windows File Server.',
    'Which FSx file system types support file access auditing?',
    ['File access auditing'], [ev('row', W, '| File access auditing |')],
    scope='security and compliance table', bul=['4.1.K4'])
add('fsx-compare-acl-types', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, access control lists are marked for FSx for NetApp ONTAP (NFS 4.0, v4.1, NTFS) and FSx for Windows File Server (NTFS), and not for OpenZFS or Lustre.',
    'Which FSx file system types support access control lists, and of which kind?',
    ['NFS 4.0, v4.1, NTFS', 'NTFS'], [ev('row', W, '| Access Control Lists (ACLs) |')],
    scope='security and compliance table', bul=['4.1.K4'])
add('fsx-compare-antivirus-ontap-only', 'fsx', 'behavior',
    'On the AWS page comparing FSx file systems, anti-virus integration is marked only for FSx for NetApp ONTAP.',
    'Which FSx file system type supports anti-virus integration?',
    ['Anti-virus integration'], [ev('row', W, '| Anti-virus integration |')],
    scope='security and compliance table', bul=['4.1.K4'])
add('fsx-compare-compliance-all-four-types', 'fsx', 'behavior',
    'AWS lists the same compliance programs for all four FSx file system types, among them HIPAA BAA, PCI/DSS, ISO, SOC, IRAP, GDPR, ISMAP, FINMA, MTCS, C5, ENS High, OSPAR and HITRUST CSF.',
    'Do the FSx file system types differ in compliance programs on the AWS comparison page?',
    ['HIPAA BAA, PCI/DSS, ISO, SOC, IRAP, GDPR, ISMAP, FINMA, MTCS, C5, ENS High, OSPAR, HITRUST CSF'],
    [ev('row', W, '| Compliance and certification |')],
    scope='security and compliance table', bul=['4.1.K4'], rel='reference')

write('aws-saa-book/_build/work/23-efs-fsx/facts-decisions-02.json', facts)
