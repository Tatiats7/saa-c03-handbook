import sys
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from gen_lib import *

OD = 'docs/fsx/latest/ONTAPGuide/document-history'
WNB = 'www/about-aws/whats-new/'
facts = []

def add(*a, **k):
    facts.append(F(*a, **k))

SL = WNB + '2025/03/amazon-fsx-netapp-ontap-no-charges-snaplock-licensing'
add('fsx-change-ontap-snaplock-licensing-fee-removed-2025-03', 'fsx', 'change',
    'On 2025-03-05 Amazon FSx for NetApp ONTAP eliminated SnapLock licensing fees for data stored in SnapLock volumes. The removal applies automatically to new and existing SnapLock volumes on all FSx for ONTAP file systems in all AWS Regions where they are available.',
    'Does FSx for NetApp ONTAP still charge a SnapLock licensing fee, and since when?',
    [('date', '2025-03-05'), ('old', 'SnapLock licensing fees')],
    [ev('sent', SL, 'Starting March 5, 2025, Amazon FSx for NetApp ONTAP eliminates SnapLock licensing fees'),
     ev('sent', SL, 'This license removal requires no changes to customer applications'),
     ev('sent', SL, 'The removal of SnapLock licensing fees applies to all FSx for ONTAP file systems')],
    vol='changed-since-2022', changed=CH('2025-03-05', 'SnapLock licensing fees', 0), ci=[wn('fsx', 'amazon-fsx-netapp-ontap-no-charges-snaplock-licensing')],
    note='Cost change: older notes list a SnapLock license charge for FSx for ONTAP. SnapLock gives write once, read many (WORM) protection for specified retention periods.',
    bul=['4.1.S10', '4.1.K4'], rel='extended', scope='FSx for NetApp ONTAP SnapLock volumes')

AG = WNB + '2025/03/aws-backup-logically-air-gapped-vault-amazon-fsx'
add('fsx-change-backup-air-gapped-vault-lustre-windows-openzfs-2025-03', 'fsx', 'change',
    'On 2025-03-13 AWS Backup added logically air-gapped vault support for Amazon FSx for Lustre, Amazon FSx for Windows File Server and Amazon FSx for OpenZFS. A logically air-gapped vault stores immutable backup copies that are locked by default.',
    'Which FSx file systems could use AWS Backup logically air-gapped vaults from March 2025?',
    [('date', '2025-03-13'), ('what', 'logically air-gapped vault')],
    [ev('sent', AG, 'Today, we are announcing the availability of AWS Backup logically air-gapped vault support'),
     ev('sent', AG, 'A logically air-gapped vault stores immutable backup copies that are locked by default'),
     head(AG, 'logically air-gapped vault support for Amazon FSx')],
    vol='frequently-changing', ci=[wn('fsx', 'aws-backup-logically-air-gapped-vault-amazon-fsx')],
    note='ONTAP was added on 2026-09-28 (see fsx-change-ontap-air-gapped-vault-2026-09). Pointer to the AWS Backup chapter.',
    bul=['2.2.K11', '4.1.K4'], rel='reference', scope='AWS Backup with Amazon FSx')

add('fsx-change-ontap-autonomous-ransomware-protection-2025-04', 'fsx', 'change',
    'On 2025-04-07 FSx for NetApp ONTAP began to support Autonomous Ransomware Protection (ARP), a NetApp AI-driven feature that monitors and protects against ransomware and malware attacks.',
    'When did FSx for NetApp ONTAP add Autonomous Ransomware Protection, and what does it do?',
    [('date', '2025-04-07'), ('what', 'Autonomous Ransomware Protection (ARP)')],
    [ev('row', OD, 'Autonomous Ransomware Protection (ARP) is now supported')],
    vol='frequently-changing', ci=[hist(OD, 'Autonomous Ransomware Protection (ARP) is now supported'), wn('fsx', 'amazon-fsx-netapp-ontap-autonomous-ransomware-protection')],
    bul=['4.1.K4'], rel='reference', scope='FSx for NetApp ONTAP security')

WI = 'docs/fsx/latest/WindowsGuide/what-is'
OW = 'docs/fsx/latest/ONTAPGuide/what-is-fsx-ontap'
ZW = 'docs/fsx/latest/OpenZFSGuide/what-is-fsx'

add('fsx-ontap-what-is-migrate-backup-burst-from-on-premises-ontap', 'fsx', 'behavior',
    'AWS says that for customers who use NetApp ONTAP on premises, FSx for ONTAP is an ideal solution to migrate, back up or burst file-based applications to AWS without changing the application code or how they manage their data.',
    'Why is FSx for NetApp ONTAP the fit for an on-premises NetApp ONTAP user?',
    ['migrate, back up, or burst your file-based applications'],
    [ev('sent', OW, 'For customers who use NetApp ONTAP on-premises')],
    scope='FSx for NetApp ONTAP', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)
add('fsx-ontap-what-is-ssd-performance-pay-small-fraction', 'fsx', 'behavior',
    'AWS says that with FSx for ONTAP you can get SSD levels of performance for your workload while paying for SSD storage for only a small fraction of your data, because it automatically tiers data to lower-cost, elastic storage.',
    'How does FSx for NetApp ONTAP cut storage cost while keeping SSD performance?',
    ['paying for SSD storage for only a small fraction of your data'],
    [ev('sent', OW, 'With FSx for ONTAP, you can achieve SSD levels of performance'),
     ev('sent', OW, 'FSx for ONTAP automatically tiers your data to lower-cost, elastic storage')],
    scope='FSx for NetApp ONTAP', bul=['4.1.S10', '4.1.K7'])
add('fsx-ontap-what-is-multiprotocol-nfs-smb-iscsi-nvme', 'fsx', 'capability',
    'FSx for ONTAP offers multi-protocol access to data using the NFS, SMB, iSCSI and NVMe protocols, and its file storage is broadly accessible from Linux, Windows and macOS compute instances running in AWS or on premises.',
    'Which protocols and clients does FSx for NetApp ONTAP serve?',
    ['Network File System (NFS), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and Non-Volatile Memory Express (NVMe) protocols'],
    [ev('full', OW, 'Multi-protocol [access to data]'),
     ev('sent', OW, 'FSx for ONTAP provides feature-rich, fast, and flexible shared file storage')],
    scope='FSx for NetApp ONTAP', bul=['4.1.K4', '2.2.S8'])
add('fsx-openzfs-what-is-move-from-on-premises-zfs-linux-servers', 'fsx', 'behavior',
    'AWS says Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data to AWS from on-premises ZFS or other Linux-based file servers, without changing your application code or how you manage data.',
    'What is FSx for OpenZFS for, according to the FSx for OpenZFS user guide?',
    ['on-premises ZFS or other Linux-based file servers'],
    [ev('sent', ZW, 'Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data'),
     ev('sent', ZW, 'You can do this without changing your application code or how you manage data.')],
    scope='FSx for OpenZFS', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)
add('fsx-openzfs-what-is-nfs-clients-snapshots-clones', 'fsx', 'capability',
    'FSx for OpenZFS file systems are accessible from Linux, Windows and macOS compute instances and containers through the industry-standard NFS protocol, and support OpenZFS features such as instant point-in-time snapshots and data cloning.',
    'Which protocol and which data management features does FSx for OpenZFS provide?',
    ['industry-standard NFS protocol', 'instant point-in-time snapshots and data cloning'],
    [ev('sent', ZW, 'Amazon FSx for OpenZFS file systems are broadly accessible from Linux, Windows, and macOS'),
     ev('sent', ZW, 'With complete support for OpenZFS features like instant point-in-time snapshots and data cloning')],
    scope='FSx for OpenZFS', bul=['4.1.K4', '2.2.S8'])
add('fsx-openzfs-what-is-two-storage-classes-billing', 'fsx', 'pricing-dimension',
    'FSx for OpenZFS has two storage classes. With Intelligent-Tiering you are billed for the data you store and do not need to specify a file system size; with SSD storage you specify a file system size and pay for the amount of storage you provision.',
    'How do the two FSx for OpenZFS storage classes differ in billing and sizing?',
    ['pay for the amount of storage that you provision', 'do not need to specify a file system size'],
    [ev('sent', ZW, 'With Intelligent-Tiering, you are billed for the data you store'),
     ev('sent', ZW, 'With SSD storage, you specify a file system size')],
    scope='FSx for OpenZFS storage classes', bul=['4.1.S10', '4.1.S4'], vol='frequently-changing')
add('fsx-windows-what-is-unchanged-windows-apps-workloads', 'fsx', 'behavior',
    'AWS says that with file storage on Amazon FSx the code, applications and tools that Windows developers and administrators use today can continue to work unchanged. Ideal workloads include business applications, home directories, web serving, content management, data analytics, software build setups and media processing.',
    'Which existing Windows applications and workloads fit FSx for Windows File Server without changes?',
    ['can continue to work unchanged'],
    [ev('sent', WI, 'With file storage on Amazon FSx, the code, applications, and tools'),
     ev('sent', WI, 'Windows applications and workloads ideal for Amazon FSx include')],
    scope='FSx for Windows File Server', bul=['4.1.K4', '2.2.S7', '2.2.S8'], t0=True)
add('fsx-windows-what-is-smb-versions-and-clients', 'fsx', 'capability',
    'FSx for Windows File Server is accessible with the SMB protocol, supporting versions 2.0 to 3.1.1, from all Windows versions starting from Windows Server 2008 and Windows 7, and also from current versions of Linux.',
    'Which SMB versions and client operating systems does FSx for Windows File Server support?',
    ['supporting versions 2.0 to 3.1.1'],
    [ev('sent', WI, 'Amazon FSx is accessible from compute instances with the SMB protocol'),
     ev('sent', WI, 'You can access your shares from all Windows versions starting from Windows Server 2008')],
    scope='FSx for Windows File Server', bul=['4.1.K4', '2.2.S7'])
add('fsx-windows-what-is-access-other-vpc-account-region-on-premises', 'fsx', 'capability',
    'You can access FSx for Windows File Server file shares from on-premises compute instances using AWS Direct Connect or Site-to-Site VPN, and from a different VPC, account or AWS Region using VPC peering or transit gateways.',
    'Can clients in another VPC, account, Region or on premises reach an FSx for Windows File Server file system?',
    ['AWS Direct Connect or Site-to-Site VPN', 'VPC peering or transit gateways'],
    [ev('sent', WI, 'You can access your file shares from on-premises compute instances using AWS Direct Connect or Site-to-Site VPN.'),
     ev('sent', WI, 'You do so using VPC peering or transit gateways.')],
    scope='FSx for Windows File Server network access', bul=['4.1.K4', '2.2.S7'])

write('aws-saa-book/_build/work/23-efs-fsx/facts-changes-07.json', facts)
