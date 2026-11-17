facts card: 14 facts
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
fsx-faq-windows-datasync-replicate-same-and-cross-region
  claim: You can use AWS DataSync to schedule periodic replication of an FSx for Windows file system to a second file system, in the same Region or across Regions.
  scope: FSx for Windows File Server replication.
  link: [AWS DataSync](../facts/fsx.md#fsx-faq-windows-datasync-replicate-same-and-cross-region)
fsx-faq-ontap-nfs-smb-multiprotocol
  claim: FSx for NetApp ONTAP provides access over all versions of NFS and SMB, and also supports multi-protocol access, which is concurrent NFS and SMB access to the same data.
  scope: FSx for NetApp ONTAP.
  link: [all versions of the Network File System (NFS)](../facts/fsx.md#fsx-faq-ontap-nfs-smb-multiprotocol)
  link: [multi-protocol access](../facts/fsx.md#fsx-faq-ontap-nfs-smb-multiprotocol)
fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp
  claim: AWS recommends using NetApp SnapMirror to migrate on-premises NetApp ONTAP file systems to FSx for ONTAP.
  scope: Amazon FSx for NetApp ONTAP migration.
  link: [recommend using SnapMirror to migrate](../facts/fsx.md#fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp)
  link: [migrate your NetApp ONTAP file systems](../facts/fsx.md#fsx-ontap-snapmirror-recommended-for-migrating-onprem-netapp)
fsx-when-to-choose-ontap-from-nas
  claim: The AWS page on choosing an FSx file system recommends FSx for NetApp ONTAP when your current storage technology is NetApp ONTAP or another NAS appliance.
  scope: FSx file system choice by current storage technology.
  link: [FSx for NetApp ONTAP](../facts/fsx.md#fsx-when-to-choose-ontap-from-nas)
fsx-compare-protocol-support
  claim: AWS lists protocol support as SMB, NFS and iSCSI for FSx for NetApp ONTAP, NFS for OpenZFS, SMB for Windows File Server, and a custom POSIX-compliant protocol optimized for performance for Lustre.
  scope: per FSx file system type.
  link: [SMB 2.0, 2.1, 3.0, 3.1.1 NFS 3, 4.0, 4.1, 4.2 iSCSI (shared block storage)](../facts/fsx.md#fsx-compare-protocol-support)
  link: [NFS 3, 4.0, 4.1, 4.2](../facts/fsx.md#fsx-compare-protocol-support)
fsx-when-to-choose-openzfs-from-zfs
  claim: The AWS page on choosing an FSx file system recommends FSx for OpenZFS when your current storage technology is ZFS or another Linux-based file server.
  scope: FSx file system choice by current storage technology.
  link: [FSx for OpenZFS](../facts/fsx.md#fsx-when-to-choose-openzfs-from-zfs)
fsx-faq-openzfs-snapshots-clones-replication
  claim: FSx for OpenZFS offers ZFS-powered capabilities including point-in-time snapshots, in-place data cloning, and on-demand data replication across file systems.
  scope: FSx for OpenZFS.
  link: [point-in-time snapshots, in-place data cloning](../facts/fsx.md#fsx-faq-openzfs-snapshots-clones-replication)
  link: [on-demand data replication across file systems](../facts/fsx.md#fsx-faq-openzfs-snapshots-clones-replication)
fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot
  claim: A clone volume is a writable copy initialized with the same data as the snapshot, created almost instantly and initially consuming no additional storage; it keeps a dependency on its source snapshot, so you cannot delete the snapshot while the clone is in use.
  scope: FSx for OpenZFS clones.
  link: [writable copy](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
  link: [created almost instantly](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
  link: [cannot delete this source snapshot](../facts/fsx.md#fsx-openzfs-clone-volume-writable-instant-depends-on-snapshot)
fsx-overview-openzfs-migrate-without-changing-apps
  claim: The AWS overview whitepaper says FSx for OpenZFS makes it easy to migrate on-premises file servers without changing your applications or how you manage data.
  scope: Amazon FSx for OpenZFS.
  link: [without changing your applications](../facts/fsx.md#fsx-overview-openzfs-migrate-without-changing-apps)
fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib
  claim: With Microsoft DFS Namespaces you can group file shares on multiple FSx for Windows File Server file systems into one namespace and scale file storage beyond the 64 TiB maximum of a single file system, up to hundreds of petabytes.
  scope: FSx for Windows File Server DFS Namespaces.
  link: [maximum storage capacity of single file system (64 TiB)](../facts/fsx.md#fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib)
  link: [one common folder structure, or namespace](../facts/fsx.md#fsx-windows-dfs-namespaces-group-file-systems-scale-beyond-64-tib)
fsx-windows-limit-max-storage-capacity
  claim: The maximum storage capacity of an FSx for Windows SSD or HDD file system is 64 TiB.
  scope: per file system, SSD and HDD; maximum; not adjustable.
  link: [64 TiB](../facts/fsx.md#fsx-windows-limit-max-storage-capacity)
fsx-compare-client-compatibility
  claim: AWS lists client compatibility as Windows, Linux and macOS for FSx for NetApp ONTAP, OpenZFS and Windows File Server, and Linux for FSx for Lustre.
  scope: per FSx file system type.
  link: [Linux](../facts/fsx.md#fsx-compare-client-compatibility)
