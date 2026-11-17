import sys
sys.path.insert(0, 'aws-saa-book/_build/work/23-efs-fsx')
from gen_lib import *

DG = 'docs/decision-guides/latest/decision-guides/choosing-aws-storage-service'
BP = 'docs/fsx/latest/WindowsGuide/windows-best-practices'
facts = []

def add(*a, **k):
    facts.append(F(*a, **k))

# ---------- storage type definitions (d052)
add('efs-decision-guide-definition-block-storage', 'efs', 'behavior',
    'The AWS storage decision guide defines block storage as technology that controls data storage and storage devices.',
    'How does the AWS storage decision guide define block storage?',
    ['Block storage is technology that controls data storage and storage devices'],
    [ev('sent', DG, 'Block storage is technology that controls data storage')],
    scope='storage type definitions', bul=['3.1.K3', '4.1.K11', '2.1.K13'], rel='extended')
add('efs-decision-guide-definition-file-storage', 'efs', 'behavior',
    'The AWS storage decision guide defines file systems as storing data in a hierarchical structure of files and folders; in network environments, file-based storage often uses network-attached storage (NAS) technology.',
    'How does the AWS storage decision guide define file storage?',
    ['hierarchical structure of files and folders'],
    [ev('sent', DG, 'File systems store data in a hierarchical structure of files and folders.'),
     ev('sent', DG, 'In network environments, file-based storage often uses network-attached storage (NAS) technology.')],
    scope='storage type definitions', bul=['3.1.K3', '4.1.K11', '2.1.K13'], rel='extended')
add('efs-decision-guide-definition-object-storage', 'efs', 'behavior',
    'The AWS storage decision guide defines object storage as technology that stores and manages data in an unstructured format called objects, where each object is tagged with a unique identifier and holds metadata that describes the content.',
    'How does the AWS storage decision guide define object storage?',
    ['unstructured format called objects'],
    [ev('sent', DG, 'Object storage is a technology that stores and manages data in an unstructured format called objects.'),
     ev('sent', DG, 'Each object is tagged with a unique identifier and contains metadata')],
    scope='storage type definitions', bul=['3.1.K3', '4.1.K11', '2.1.K13'], rel='extended')
add('fsx-decision-guide-online-migration-options', 'fsx', 'behavior',
    'In the AWS storage decision guide, the online migration options include AWS DataSync, AWS Transfer Family, Amazon FSx for NetApp ONTAP SnapMirror and AWS Storage Gateway, and online migration is optimized for frequent updates to data and for time-critical or ongoing workloads.',
    'Which services does the storage decision guide list for online data migration, and when is online migration the right choice?',
    ['Online is optimized for frequent updates to data'],
    [ev('row', DG, '| Online | Online is optimized for frequent updates to data.')],
    scope='migration options table of the decision guide', bul=['4.1.K4', '2.2.S7'], rel='extended')

# ---------- FSx for Windows best practices: security
add('fsx-windows-bp-dont-modify-delete-eni', 'fsx', 'restriction',
    'AWS says not to modify or delete the elastic network interface (ENI) that is associated with an FSx for Windows File Server file system, because doing so can cause a permanent loss of connection between your VPC and the file system.',
    'What can happen if you modify or delete the network interface of an FSx for Windows File Server file system?',
    ['permanent loss of connection between your VPC and your file system'],
    [ev('sent', BP, 'Modifying or deleting the network interface can cause a permanent loss of connection')],
    scope='FSx for Windows File Server network security', bul=['4.1.K4'], rel='extended')
add('fsx-windows-bp-security-groups-and-network-acls-limit-access', 'fsx', 'capability',
    'You can use security groups and network access control lists (ACLs) to limit access to FSx for Windows File Server file systems, and the security group and network ACLs for the subnets must allow traffic on the required ports.',
    'How do you limit network access to an FSx for Windows File Server file system?',
    ['security groups and network access control lists (ACLs)'],
    [ev('sent', BP, 'You can use security groups and network access control lists (ACLs) to limit access to your file systems.'),
     ev('sent', BP, 'Make sure that the security group and the network ACLs for the subnets')],
    scope='FSx for Windows File Server network security', bul=['4.1.K4'], rel='extended')
add('fsx-windows-bp-join-active-directory-two-options', 'fsx', 'capability',
    'You can join an FSx for Windows File Server file system to your Microsoft Active Directory domain to provide user authentication and share-, file- and folder-level access control. FSx provides two Active Directory options: AWS managed Microsoft Active Directory or self-managed Microsoft Active Directory.',
    'What Active Directory options does FSx for Windows File Server offer, and what do they provide?',
    ['AWS managed Microsoft Active Directory', 'self-managed Microsoft Active Directory'],
    [ev('sent', BP, 'When you create an Amazon FSx file system, you can join it to your'),
     ev('sent', BP, 'Amazon FSx provides you with two options for Active Directory')],
    scope='FSx for Windows File Server Active Directory', bul=['4.1.K4', '2.2.S7'], t0=True)
add('fsx-windows-bp-windows-acls-enforced-existing-acls-migrate', 'fsx', 'capability',
    'FSx for Windows File Server uses standard Windows access control lists (ACLs) for fine-grained share-, file- and folder-level access control, and automatically verifies the credentials of users who access file system data to enforce them. You can migrate an existing security ACL configuration without modifications.',
    'How does FSx for Windows File Server enforce file permissions, and can existing ACLs move over?',
    ['standard Windows access control lists (ACLs)'],
    [ev('sent', BP, 'With Amazon FSx, you use standard Windows access control lists (ACLs)'),
     ev('sent', BP, 'Amazon FSx file systems automatically verify the credentials of users'),
     ev('sent', BP, 'In addition, you can migrate the existing security ACL configuration to Amazon FSx without any modifications.')],
    scope='FSx for Windows File Server access control', bul=['4.1.K4', '2.2.S7'], t0=True)
add('fsx-windows-bp-self-managed-ad-least-privilege-service-account', 'fsx', 'behavior',
    'For FSx for Windows File Server with a self-managed Active Directory, AWS recommends a separate Organizational Unit for the file systems and a service account configured with the minimum privileges required.',
    'What does AWS recommend for the service account and OU when FSx for Windows File Server joins a self-managed Active Directory?',
    ['minimum privileges required'],
    [ev('sent', BP, 'Use an OU for your Amazon FSx file systems that’s separate'),
     ev('sent', BP, 'Configure or delegate the service account that you provide to Amazon FSx with the minimum privileges required.')],
    scope='FSx for Windows File Server self-managed Active Directory', bul=['4.1.K4'], rel='extended')
add('fsx-windows-bp-secrets-manager-for-ad-credentials', 'fsx', 'capability',
    'You can use AWS Secrets Manager to store and manage the Microsoft Active Directory domain join service account credentials for FSx for Windows File Server, which removes the need to store sensitive credentials in plaintext in application code or configuration files.',
    'How can you avoid storing the Active Directory join credentials for FSx for Windows File Server in plaintext?',
    ['AWS Secrets Manager'],
    [ev('sent', BP, 'You can use AWS Secrets Manager to securely store and manage your Microsoft Active Directory domain join service account credentials.'),
     ev('sent', BP, 'This approach eliminates the need to store sensitive credentials in plaintext')],
    scope='FSx for Windows File Server self-managed Active Directory', bul=['4.1.K4'], vol='frequently-changing', rel='extended',
    note='The Secrets Manager integration was added on 2025-11-05 (Windows document history).')
add('fsx-windows-bp-ad-misconfigured-status-risk', 'fsx', 'behavior',
    'For FSx for Windows File Server with a self-managed Active Directory, FSx rejoins the file server to Active Directory during failure recovery, routine maintenance and throughput capacity updates. If the Active Directory configuration is not valid during such an event, the file system changes to the Misconfigured status and is at risk of becoming unavailable.',
    'What happens to an FSx for Windows File Server file system if its Active Directory configuration is invalid during maintenance?',
    ['at risk of becoming unavailable'],
    [ev('sent', BP, 'During failure recovery events, routine maintenance events, and throughput capacity update actions'),
     ev('sent', BP, 'If the Active Directory configuration is not valid during an event')],
    scope='FSx for Windows File Server self-managed Active Directory', bul=['4.1.K4', '2.2.K11'], rel='extended')
add('fsx-windows-bp-dont-change-system-user-ntfs-permissions', 'fsx', 'restriction',
    'FSx for Windows File Server requires that the SYSTEM user have full control NTFS ACL permissions on all folders in the file system; changing them may make the file system inaccessible and future backups unusable.',
    'What NTFS permission must the SYSTEM user keep on an FSx for Windows File Server file system?',
    ['full control NTFS ACL permissions on all folders'],
    [ev('sent', BP, 'Amazon FSx requires that the SYSTEM user have full control NTFS ACL permissions on all folders within your file system.'),
     ev('sent', BP, 'Changing the NTFS ACL permissions for the SYSTEM user may result in your file system becoming inaccessible')],
    scope='FSx for Windows File Server NTFS ACLs', bul=['4.1.K4'], rel='extended')

# ---------- FSx for Windows best practices: capacity and cost
add('fsx-windows-bp-keep-20-percent-free-storage', 'fsx', 'behavior',
    'AWS recommends keeping at least 20% of free storage capacity at all times on an FSx for Windows File Server file system, and increasing throughput capacity by at least 20% before increasing storage capacity to offset any performance impact during the storage increase.',
    'How much free storage should you keep on an FSx for Windows File Server file system, and what should you do with throughput before a storage increase?',
    ['at least 20% of free storage capacity at all times'],
    [ev('sent', BP, 'We recommend maintaining at least 20% of free storage capacity at all times on your file system.'),
     ev('sent', BP, 'We also recommend increasing throughput capacity by at least 20% before increasing storage capacity')],
    scope='FSx for Windows File Server capacity planning', bul=['4.1.S4', '3.1.S2'], t0=True)
add('fsx-windows-bp-monitor-free-storage-capacity-metric', 'fsx', 'behavior',
    'You can use the FreeStorageCapacity CloudWatch metric to monitor the amount of free storage available on an FSx for Windows File Server file system and see how it trends.',
    'Which CloudWatch metric shows free storage on an FSx for Windows File Server file system?',
    ['FreeStorageCapacity'],
    [ev('sent', BP, 'You can use the *FreeStorageCapacity* CloudWatch metric')],
    scope='FSx for Windows File Server monitoring', bul=['4.1.S4'], rel='extended')
add('fsx-windows-bp-throughput-update-interrupts-single-az-failover-multi-az', 'fsx', 'behavior',
    'Updating throughput capacity of an FSx for Windows File Server file system interrupts availability for a few minutes on Single-AZ file systems and causes failover and failback on Multi-AZ file systems, so AWS recommends doing it during idle periods.',
    'What happens when you change the throughput capacity of an FSx for Windows File Server file system, and when should you do it?',
    ['interrupts availability for a few minutes for Single-AZ file systems'],
    [ev('sent', BP, 'Updating throughput capacity interrupts availability for a few minutes for Single-AZ file systems'),
     ev('sent', BP, 'we recommend scheduling maintenance windows and performing throughput capacity updates during idle periods')],
    scope='FSx for Windows File Server throughput capacity updates', bul=['4.1.S4', '2.2.K11'])
add('fsx-windows-bp-shadow-copies-three-times-throughput', 'fsx', 'behavior',
    'If you use shadow copies on FSx for Windows File Server, AWS recommends increasing throughput capacity to a value at least three times the value that your workload is expected to drive, to avoid Windows Server deleting your shadow copies.',
    'How much throughput capacity should an FSx for Windows File Server file system with shadow copies have compared with the workload?',
    ['at least three times the value'],
    [ev('sent', BP, 'If you’re using shadow copies, increase throughput capacity to a value')],
    scope='FSx for Windows File Server shadow copies', bul=['4.1.S4', '3.1.S1'], rel='extended')
add('fsx-windows-bp-multi-az-for-most-production-workloads', 'fsx', 'behavior',
    'AWS recommends Multi-AZ file systems for most FSx for Windows File Server production workloads that require high availability to shared Windows file data.',
    'Which FSx for Windows File Server deployment type does the best practices page recommend for production?',
    ['Multi-AZ file systems'],
    [ev('sent', BP, 'We recommend using **Multi-AZ file systems** for most production workloads')],
    scope='FSx for Windows File Server deployment types', bul=['2.2.K11', '4.1.K4'])

write('aws-saa-book/_build/work/23-efs-fsx/facts-decisions-06.json', facts)
