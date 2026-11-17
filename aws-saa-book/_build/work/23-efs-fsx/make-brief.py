"""Builds brief.v0.json and mine-plan.json for chapter 23 (EFS and FSx).

Run from the repo root after the page batch has finished:
    python3 aws-saa-book/_build/work/23-efs-fsx/make-brief.py
It reads the corpus to count which sources are saved and lists the rest as
fetch_failures. No network access.
"""
import json, sys
from pathlib import Path

ROOT = Path("aws-saa-book")
sys.path.insert(0, str(ROOT / "tools"))
from saalib import corpus  # noqa: E402

WORK = ROOT / "_build/work/23-efs-fsx"
EFS = "https://docs.aws.amazon.com/efs/latest/ug/"
WIN = "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/"
LUS = "https://docs.aws.amazon.com/fsx/latest/LustreGuide/"
ONT = "https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/"
OZF = "https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/"

registry = json.load(open(ROOT / "data/book.json"))
entry = next(c for c in registry["chapters"] if c["id"] == "23") if "chapters" in registry else None
if entry is None:
    entry = registry["23"] if "23" in registry else None
if entry is None:
    for c in registry.get("chapters", registry.get("items", [])):
        if c.get("id") == "23":
            entry = c
src = entry["sources"]

batch_urls = [u.strip() for u in open(ROOT / "_build/tmp/urls-23.txt") if u.strip()]
case_urls = [
    "https://aws.amazon.com/solutions/case-studies/deepbrain-case-study/",
    "https://aws.amazon.com/solutions/case-studies/ancestry-case-study/",
    "https://aws.amazon.com/solutions/case-studies/adobe-case-study/",
    "https://aws.amazon.com/solutions/case-studies/phillips66-migration-case-study/",
]
universe = []
for key in ("pages", "faq", "history", "quotas", "pricing"):
    universe += src[key]
universe += batch_urls + case_urls
seen, ordered = set(), []
for u in universe:
    if u not in seen:
        seen.add(u)
        ordered.append(u)

fetched, failures = [], []
for u in ordered:
    sid = corpus.source_id_for(u)
    if corpus.load_text(sid) is not None:
        fetched.append(sid)
    else:
        failures.append({"url": u, "source_id": sid, "reason": "plan batch cut short by the harness; fetch at mine start with: saa.py fetch --batch aws-saa-book/_build/work/23-efs-fsx/urls-batch.txt"})

B = {  # bullet short names, for readability of the demand list
    "k2": "3.1.K2", "k3": "3.1.K3", "s1": "3.1.S1", "s2": "3.1.S2",
    "k4": "4.1.K4", "k7": "4.1.K7", "k11": "4.1.K11", "s4": "4.1.S4", "s10": "4.1.S10",
    "k13": "2.1.K13", "r11": "2.2.K11", "r7": "2.2.S7", "r8": "2.2.S8",
}

# (bullet, lens, service, question, source hints)
D = [
    # ---- EFS: what it is, protocol, clients, scale
    ("k2", "behavior", "efs", "What is Amazon EFS, and which protocol and version do clients use to mount it (NFS v4.x)?", ["docs/efs/latest/ug/whatisefs", "docs/efs/latest/ug/how-it-works"]),
    ("k3", "behavior", "efs", "Which operating systems can mount an EFS file system natively, and is Windows supported?", ["docs/efs/latest/ug/whatisefs", "www/efs/faq"]),
    ("k4", "behavior", "efs", "How many compute instances or containers can read and write one EFS file system at the same time?", ["docs/efs/latest/ug/whatisefs", "www/efs/faq"]),
    ("s2", "behavior", "efs", "Does an EFS file system grow and shrink automatically, with no capacity to provision?", ["docs/efs/latest/ug/whatisefs", "docs/efs/latest/ug/features"]),
    ("s2", "numbers", "efs", "What is the maximum size of a single file in EFS, and the maximum file system size?", ["docs/efs/latest/ug/limits", "www/efs/faq"]),
    ("k2", "behavior", "efs", "What is a mount target, how many mount targets can a file system have in one Availability Zone, and why does a Regional file system need one per AZ?", ["docs/efs/latest/ug/how-it-works", "docs/efs/latest/ug/limits"]),
    ("k2", "behavior", "efs", "Which AWS compute services can use EFS without code change (EC2, ECS, Fargate, EKS, Lambda, SageMaker)?", ["www/efs/faq", "docs/efs/latest/ug/features"]),
    ("k2", "behavior", "efs", "Can on-premises servers mount EFS, and over which connections (Direct Connect, Site-to-Site VPN)?", ["www/efs/faq", "docs/efs/latest/ug/manage-fs-access-vpc-peering"]),
    ("k2", "behavior", "efs", "Can a file system be mounted from another VPC, another account, or another Region, and what is needed (peering, transit gateway, inter-Region)?", ["docs/efs/latest/ug/manage-fs-access-vpc-peering", "docs/efs/latest/ug/mount-different-region", "www/efs/faq"]),
    ("k2", "behavior", "efs", "How do you move existing data into EFS (AWS DataSync, AWS Transfer Family), and which is recommended for on-premises file data?", ["docs/efs/latest/ug/trnsfr-data-using-datasync", "www/efs/faq"]),
    ("k2", "behavior", "efs", "Which file locking does EFS support (NFSv4 locks), and are file system names global like bucket names?", ["www/efs/faq"]),
    ("k2", "behavior", "efs", "How does the EFS mount helper mount a file system (DNS name, TLS option, fstab automount)?", ["docs/efs/latest/ug/mounting-fs", "docs/efs/latest/ug/encryption-in-transit"]),
    # ---- EFS: file system types, durability, availability
    ("r11", "behavior", "efs", "What are the two EFS file system types (Regional, One Zone), and how is data stored in each (across multiple AZs vs within one AZ)?", ["docs/efs/latest/ug/whatisefs", "docs/efs/latest/ug/features", "www/efs/faq"]),
    ("r11", "numbers", "efs", "What durability is EFS designed for (how many nines), and what availability does Regional vs One Zone target?", ["www/efs/faq", "docs/efs/latest/ug/disaster-recovery-resiliency"]),
    ("r11", "behavior", "efs", "What extra failure modes does a One Zone file system add, and what does AWS recommend to protect against them (automatic backups on by default)?", ["www/efs/faq", "docs/efs/latest/ug/mounting-one-zone"]),
    ("s10", "numbers", "efs", "How much cheaper is One Zone storage than Regional storage (percentage on the pricing page)?", ["www/efs/pricing", "www/efs/faq"]),
    ("r11", "behavior", "efs", "When you mount a One Zone file system from an instance in another AZ, what happens to availability and data transfer charges?", ["docs/efs/latest/ug/mounting-one-zone", "www/efs/pricing"]),
    # ---- EFS: storage classes and lifecycle (data lifecycles bullet)
    ("k7", "behavior", "efs", "Which EFS storage classes exist (Standard, Infrequent Access, Archive), and which file system types and throughput modes support each?", ["docs/efs/latest/ug/lifecycle-management-efs", "www/efs/faq"]),
    ("k7", "behavior", "efs", "How does an EFS lifecycle policy work: transition to IA, transition to Archive, and transition back to Standard on first access?", ["docs/efs/latest/ug/lifecycle-management-efs"]),
    ("k7", "numbers", "efs", "Which 'days since last access' values can a lifecycle policy use (1, 7, 14, 30, 60, 90, 180, 270, 365 days), and what are the defaults for a new file system?", ["docs/efs/latest/ug/lifecycle-management-efs", "docs/efs/latest/ug/creating-using-create-fs"]),
    ("s10", "numbers", "efs", "Is there a minimum billing duration (90 days) and a minimum billable file size (128 KiB) for IA and Archive?", ["www/efs/faq", "www/efs/pricing"]),
    ("s10", "numbers", "efs", "What does reading or writing IA and Archive data cost (per-GB access charge), and what latency do these classes have?", ["www/efs/pricing", "www/efs/faq", "docs/efs/latest/ug/performance"]),
    ("k7", "numbers", "efs", "How is metered size computed per storage class, and how is file system metering reported in CloudWatch (StorageBytes dimensions)?", ["docs/efs/latest/ug/metered-sizes"]),
    # ---- EFS: performance
    ("s1", "behavior", "efs", "What are the EFS performance modes (General Purpose, Max I/O), which is default, which is recommended, and which file systems cannot use Max I/O (One Zone, Elastic)?", ["docs/efs/latest/ug/performance", "docs/efs/latest/ug/creating-using-create-fs"]),
    ("s1", "behavior", "efs", "What are the EFS throughput modes (Elastic, Provisioned, Bursting), which is default and recommended, and how often can you switch?", ["docs/efs/latest/ug/managing-throughput", "docs/efs/latest/ug/performance"]),
    ("s1", "numbers", "efs", "What read and write throughput can an Elastic file system reach per Region (GiBps), and what are the limits in the other Regions?", ["docs/efs/latest/ug/performance", "docs/efs/latest/ug/limits"]),
    ("s1", "numbers", "efs", "How does Bursting throughput scale with stored data (baseline MiBps per TiB and burst MiBps per TiB), and how do burst credits work?", ["docs/efs/latest/ug/performance"]),
    ("s1", "numbers", "efs", "What is the Provisioned throughput maximum, and when is Provisioned the right choice over Elastic or Bursting?", ["docs/efs/latest/ug/performance", "docs/efs/latest/ug/managing-throughput", "docs/efs/latest/ug/limits"]),
    ("s1", "numbers", "efs", "What is the per-client throughput maximum (MiBps), and how many file operations per second does General Purpose mode support (and up to what by request)?", ["docs/efs/latest/ug/performance", "docs/efs/latest/ug/limits"]),
    ("s1", "numbers", "efs", "What first-byte read and write latency does EFS state for Standard data (about 1 ms read, about 2.7 ms write) versus IA and Archive (tens of ms), and does One Zone differ?", ["docs/efs/latest/ug/performance", "www/efs/faq"]),
    ("s1", "numbers", "efs", "Per-file-system maximum IOPS by throughput mode (Elastic read 900,000 to 2,500,000, write 500,000; Provisioned 55,000 and 25,000; Bursting 35,000 and 7,000) and the default Elastic IOPS before a quota increase.", ["docs/efs/latest/ug/performance", "docs/efs/latest/ug/limits"]),
    ("s4", "behavior", "efs", "Does EFS need storage auto scaling or capacity planning (no: elastic), and what does the exam call 'auto scaling' for file storage compared with EBS and FSx?", ["docs/efs/latest/ug/whatisefs", "www/efs/faq"]),
    # ---- EFS: backup, replication, DR
    ("r11", "behavior", "efs", "What does EFS automatic backup use (AWS Backup), is it on by default for console-created file systems, and what is the default retention?", ["docs/efs/latest/ug/automatic-backups", "www/efs/faq"]),
    ("r11", "behavior", "efs", "What is EFS replication: destination Region or same Region, replica read-only, recovery point objective target (minutes)?", ["docs/efs/latest/ug/efs-replication", "www/efs/faq"]),
    ("r11", "behavior", "efs", "Can EFS replicate to a file system in another AWS account (cross-account replication), and since when?", ["docs/efs/latest/ug/cross-account-replication", "docs/efs/latest/ug/document-history"]),
    ("r11", "behavior", "efs", "How do you fail over to the replica and fail back (delete the replication configuration; replicate to an existing file system)?", ["docs/efs/latest/ug/replication-fail-over", "docs/efs/latest/ug/efs-replication"]),
    ("r11", "behavior", "efs", "Is a replica point-in-time consistent, and can the replica be a One Zone file system?", ["www/efs/faq", "docs/efs/latest/ug/efs-replication"]),
    # ---- EFS: security
    ("k2", "behavior", "efs", "How is EFS encrypted at rest (KMS; chosen at creation, cannot be changed later) and in transit (TLS through the mount helper)?", ["docs/efs/latest/ug/encryption-at-rest", "docs/efs/latest/ug/encryption-in-transit", "www/efs/faq"]),
    ("k2", "behavior", "efs", "What is an EFS access point, what does it enforce (POSIX user and group, root directory), and how many per file system (10,000)?", ["docs/efs/latest/ug/efs-access-points", "docs/efs/latest/ug/limits", "www/efs/faq"]),
    ("k2", "behavior", "efs", "How do you control which clients can mount a file system (security groups on mount targets, NFS port 2049, file system policy with IAM)?", ["docs/efs/latest/ug/iam-access-control-nfs-efs", "docs/efs/latest/ug/mounting-IAM-option", "www/efs/faq"]),
    ("k2", "behavior", "efs", "What does 'block public access' mean for an EFS file system policy?", ["docs/efs/latest/ug/access-control-block-public-access"]),
    ("k2", "numbers", "efs", "Resource quotas: mount targets per VPC, VPCs per file system, security groups per mount target, connections per file system.", ["docs/efs/latest/ug/limits"]),
    # ---- EFS: pricing
    ("s10", "numbers", "efs", "What are the EFS pricing dimensions (storage GB-month per class, Elastic throughput per GB transferred, Provisioned throughput MiBps-month, IA and Archive access per GB, replication transfer)?", ["www/efs/pricing", "www/efs/faq"]),
    ("s10", "numbers", "efs", "Is there a charge for Bursting throughput or for metadata operations, and how is Elastic throughput billed?", ["www/efs/faq", "www/efs/pricing"]),
    # ---- EFS: changes (FRESHNESS hypotheses)
    ("s1", "decisions+changes", "efs", "Changed recently (hypothesis): Elastic replaced Bursting as the default throughput mode on 2023-04-13; older questions may assume Bursting.", ["docs/efs/latest/ug/document-history", "docs/efs/latest/ug/managing-throughput"]),
    ("k7", "decisions+changes", "efs", "Changed recently (hypothesis): on 2023-11-26 'Standard-IA / One Zone-IA' wording became Regional and One Zone file systems with Standard, IA and Archive classes.", ["docs/efs/latest/ug/document-history", "docs/efs/latest/ug/lifecycle-management-efs"]),
    ("s2", "decisions+changes", "efs", "Changed recently (hypothesis): mount targets per VPC rose from 400 to 1,400 (2024-05-15) and access points per file system from 1,000 to 10,000 (2025-02-10).", ["docs/efs/latest/ug/document-history", "docs/efs/latest/ug/limits"]),
    ("s1", "decisions+changes", "efs", "Changed recently (hypothesis): Elastic throughput limits were raised in steps from 2024-03 to 2025-05 (10 to 60 GiBps read); which value is current per Region?", ["docs/efs/latest/ug/document-history", "docs/efs/latest/ug/limits"]),
    ("r11", "decisions+changes", "efs", "Changed recently (hypothesis): cross-account replication added 2024-11-19; replication to an existing file system (failback) added 2023-11-27.", ["docs/efs/latest/ug/document-history"]),
    ("k2", "decisions+changes", "efs", "Changed recently (low): IPv6 support for EFS (2025-06-09); DataSync Enhanced mode for EFS and Lustre (2026-07-28, after the examinability cutoff).", ["docs/efs/latest/ug/document-history"]),
    # ---- Comparisons: S3 vs EBS vs EFS vs instance store; object/file/block
    ("k3", "decisions+changes", "efs", "When should you use EFS versus EBS versus S3 (the FAQ answer and the decision guide wording)?", ["www/efs/faq", "docs/decision-guides/latest/decision-guides/choosing-aws-storage-service"]),
    ("k11", "decisions+changes", "efs", "Object, file and block storage: how does AWS define each, and which service is which (S3, EFS and FSx, EBS and instance store)?", ["docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "docs/whitepapers/latest/aws-overview/storage-services"]),
    ("k13", "decisions+changes", "efs", "Which storage types can many instances share at once: EBS (one instance, Multi-Attach only for io1/io2 in one AZ) versus EFS and FSx (many clients across AZs)?", ["docs/decision-guides/latest/decision-guides/choosing-aws-storage-service", "docs/efs/latest/ug/whatisefs"]),
    ("r7", "decisions+changes", "efs", "A Linux application that reads and writes a local directory, cannot change, and must run on many instances: why EFS and not S3 (S3 needs API calls), and what does S3 Files change (GA 2026-04-07: examinable?)?", ["docs/AmazonS3/latest/userguide/s3-files", "www/efs/faq"]),
    ("s10", "numbers", "efs", "Cost order per GB-month: EFS Standard versus S3 Standard versus EBS gp3 (the trade-off Callvale accepts: a higher price per gigabyte than S3).", ["www/efs/pricing"]),
    ("k4", "decisions+changes", "fsx", "Which FSx file system type fits which protocol and workload (the 'when to choose FSx' page and the storage decision guide)?", ["www/fsx/when-to-choose-fsx", "docs/decision-guides/latest/decision-guides/choosing-aws-storage-service"]),
    ("r8", "decisions+changes", "fsx", "One-line discriminators: EFS (Linux NFS, elastic) versus FSx for Windows (SMB, AD) versus Lustre (HPC, S3 link) versus ONTAP (multi-protocol NetApp) versus OpenZFS (NFS, snapshots and clones).", ["www/fsx/when-to-choose-fsx", "www/fsx/windows/faqs", "www/fsx/netapp-ontap/faqs", "www/fsx/openzfs/faqs"]),
    ("k4", "decisions+changes", "fsx", "One-sentence definitions of EFS and each FSx type from the AWS overview whitepaper (for 'In one breath').", ["docs/whitepapers/latest/aws-overview/storage-services"]),
    ("r11", "numbers", "fsx", "Availability SLA per FSx type and deployment (the 'when to choose' table: Multi-AZ 99.99%; Single-AZ 99.9% for ONTAP, 99.5% for OpenZFS, Windows and Lustre) and the EFS SLA for Regional versus One Zone.", ["www/fsx/when-to-choose-fsx", "www/efs/faq"]),
    ("k4", "numbers", "fsx", "The 'when to choose' comparison table: latency, maximum throughput per file system, maximum file system size, client compatibility and protocol support for the four FSx types.", ["www/fsx/when-to-choose-fsx"]),
    # ---- FSx for Windows File Server
    ("k4", "behavior", "fsx", "What is FSx for Windows File Server: SMB protocol, Windows Server, NTFS, Windows ACLs, DFS, shadow copies?", ["docs/fsx/latest/WindowsGuide/what-is", "www/fsx/windows/faqs"]),
    ("r7", "behavior", "fsx", "Does FSx for Windows require Active Directory, and which directories work (AWS Managed Microsoft AD, self-managed AD, AD in another VPC or account)?", ["docs/fsx/latest/WindowsGuide/aws-ad-integration-fsxW", "docs/fsx/latest/WindowsGuide/self-managed-AD"]),
    ("r11", "behavior", "fsx", "Single-AZ versus Multi-AZ FSx for Windows: standby file server in another AZ, synchronous replication, automatic failover; what triggers failover and how long it takes?", ["docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "www/fsx/windows/faqs"]),
    ("k4", "behavior", "fsx", "Which clients can access FSx for Windows (Windows, Linux, macOS; EC2, ECS, WorkSpaces, AppStream, VMware Cloud on AWS, on-premises over DX or VPN)?", ["docs/fsx/latest/WindowsGuide/supported-fsx-clients", "www/fsx/windows/faqs"]),
    ("s1", "numbers", "fsx", "FSx for Windows storage types SSD and HDD: minimum capacity (32 GiB SSD, 2,000 GiB HDD), maximum per file system (64 TiB), and latency of each.", ["docs/fsx/latest/WindowsGuide/limits", "docs/fsx/latest/WindowsGuide/performance", "www/fsx/windows/faqs"]),
    ("s1", "numbers", "fsx", "FSx for Windows throughput capacity range (8 MBps to 12,288 MBps) and SSD IOPS (baseline 3 per GiB, maximum 400,000); can each be changed after creation?", ["docs/fsx/latest/WindowsGuide/limits", "docs/fsx/latest/WindowsGuide/performance"]),
    ("s4", "behavior", "fsx", "Can FSx for Windows storage capacity be increased (yes, by at least 10%) or decreased (no), and how do you automate increases from a CloudWatch alarm?", ["docs/fsx/latest/WindowsGuide/managing-storage-configuration", "www/fsx/windows/faqs"]),
    ("s10", "behavior", "fsx", "Can you change the storage type (HDD to SSD only?) and what does data deduplication save on general file shares (typical percentage)?", ["docs/fsx/latest/WindowsGuide/managing-data-dedup", "www/fsx/windows/faqs", "docs/fsx/latest/WindowsGuide/managing-storage-configuration"]),
    ("s2", "behavior", "fsx", "How do DFS Namespaces group many file systems under one namespace and scale out performance (shard data across file systems)?", ["docs/fsx/latest/WindowsGuide/using-dfs-namespaces", "docs/fsx/latest/WindowsGuide/scaleout-performance"]),
    ("r11", "behavior", "fsx", "FSx for Windows backups: daily automatic backups (retention 0 to 90 days, default), user-initiated backups, stored on S3, copy across Regions and accounts; are backups file-system-consistent?", ["docs/fsx/latest/WindowsGuide/using-backups", "www/fsx/windows/faqs", "docs/fsx/latest/WindowsGuide/limits"]),
    ("r11", "behavior", "fsx", "What are shadow copies (Windows VSS), and how do end users restore previous versions of files?", ["docs/fsx/latest/WindowsGuide/shadow-copies-fsxW", "www/fsx/windows/faqs"]),
    ("k4", "behavior", "fsx", "FSx for Windows encryption at rest (KMS, always on) and in transit (SMB Kerberos session keys, SMB 3 encryption) and which clients support it.", ["docs/fsx/latest/WindowsGuide/encryption-at-rest", "www/fsx/windows/faqs"]),
    ("r11", "behavior", "fsx", "Can DFS Replication be used on Multi-AZ or Single-AZ 2 file systems, and how do you replicate an FSx for Windows file system to another (AWS DataSync, AWS Backup copy)?", ["docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "www/fsx/windows/faqs"]),
    ("r7", "behavior", "fsx", "How do you migrate on-premises Windows file shares to FSx (AWS DataSync, Robocopy) and keep permissions and DNS names (DNS aliases, cutover)?", ["docs/fsx/latest/WindowsGuide/migrate-files-fsx", "www/fsx/windows/faqs"]),
    ("r8", "behavior", "fsx", "How does FSx for Windows serve Microsoft SQL Server (continuously available SMB shares for failover cluster instances; Multi-AZ)?", ["docs/fsx/latest/WindowsGuide/sql-server", "www/fsx/windows/faqs"]),
    ("s10", "numbers", "fsx", "FSx for Windows pricing dimensions: storage GB-month (SSD, HDD), throughput capacity MBps-month, provisioned SSD IOPS, backups GB-month; Multi-AZ priced higher than Single-AZ.", ["www/fsx/windows/pricing", "www/fsx/windows/faqs"]),
    ("s2", "numbers", "fsx", "FSx for Windows quotas: file systems per account (100), file shares per file system (100,000), maximum automated backup retention (90 days).", ["docs/fsx/latest/WindowsGuide/limits"]),
    ("r11", "behavior", "fsx", "What is 'Single-AZ 2' versus 'Single-AZ 1' for FSx for Windows (HDD support, feature table by deployment type)?", ["docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "docs/fsx/latest/WindowsGuide/what-is"]),
    ("k4", "behavior", "fsx", "Can FSx for Windows be accessed from multiple VPCs, accounts and Regions, and from a shared VPC?", ["www/fsx/windows/faqs"]),
    ("k4", "decisions+changes", "fsx", "Changed recently (hypotheses): SSD IOPS scaled separately from storage and storage type update (2023-08-09); maximum throughput 12 GB/s (2023-08-09); maximum IOPS 400,000 (2024-01-18); FSRM support (2025-11-19).", ["docs/fsx/latest/WindowsGuide/doc-history"]),
    ("k4", "decisions+changes", "fsx", "Changed recently (hypothesis, pointer to chapter 25): Amazon FSx File Gateway closed to new customers 2024-10-28; the answer is direct access to FSx for Windows.", ["docs/fsx/latest/WindowsGuide/doc-history", "www/fsx/windows/faqs"]),
    # ---- FSx for Lustre
    ("r8", "behavior", "fsx", "What is FSx for Lustre, which workloads is it built for (HPC, machine learning, media processing, financial modeling), and which clients can mount it (Linux only)?", ["docs/fsx/latest/LustreGuide/what-is", "www/fsx/lustre/faqs"]),
    ("r11", "behavior", "fsx", "Scratch versus persistent deployment types: which replicates data within the AZ, which does not persist data if a server fails, and what is each for?", ["docs/fsx/latest/LustreGuide/using-fsx-lustre", "www/fsx/lustre/faqs"]),
    ("s1", "numbers", "fsx", "Lustre storage classes SSD, HDD and Intelligent-Tiering: minimum capacity (1,200 GiB SSD, 6,000 GiB HDD), capacity increments, and latency of each.", ["docs/fsx/latest/LustreGuide/using-fsx-lustre", "docs/fsx/latest/LustreGuide/ssd-storage", "docs/fsx/latest/LustreGuide/limits"]),
    ("s1", "numbers", "fsx", "Lustre throughput per unit of storage (MBps per TiB) for scratch, persistent SSD tiers and HDD, and the aggregate limits (hundreds of GBps, millions of IOPS).", ["docs/fsx/latest/LustreGuide/performance", "docs/fsx/latest/LustreGuide/limits", "www/fsx/lustre/faqs"]),
    ("r8", "behavior", "fsx", "How does the S3 link work: a data repository association, lazy loading of file contents on first access, automatic import of bucket changes, automatic export of file system changes?", ["docs/fsx/latest/LustreGuide/overview-dra-data-repo", "docs/fsx/latest/LustreGuide/autoimport-data-repo-dra", "docs/fsx/latest/LustreGuide/autoexport-data-repo-dra"]),
    ("k7", "behavior", "fsx", "What are data repository tasks (import, export, release), and what does 'release' do to free space while the S3 copy stays?", ["docs/fsx/latest/LustreGuide/data-repository-tasks", "www/fsx/lustre/faqs"]),
    ("k7", "behavior", "fsx", "Can one Lustre file system link to several S3 buckets or prefixes, and can one bucket be linked to several file systems?", ["www/fsx/lustre/faqs", "docs/fsx/latest/LustreGuide/overview-dra-data-repo"]),
    ("r11", "behavior", "fsx", "Which Lustre file systems support backups (persistent only; not scratch), with what retention, and is the backup stored on S3?", ["docs/fsx/latest/LustreGuide/using-backups-fsx", "www/fsx/lustre/faqs", "docs/fsx/latest/LustreGuide/limits"]),
    ("r11", "behavior", "fsx", "Is FSx for Lustre a single-AZ service, and what availability and durability does AWS state for it?", ["www/fsx/lustre/faqs", "docs/fsx/latest/LustreGuide/using-fsx-lustre"]),
    ("k4", "behavior", "fsx", "How do you mount Lustre from EC2, ECS, EKS, on-premises or another VPC, and how do Spot Instances fit (interruption and data)?", ["docs/fsx/latest/LustreGuide/mounting-ec2-instance", "docs/fsx/latest/LustreGuide/mounting-on-premises", "docs/fsx/latest/LustreGuide/working-with-ec2-spot-instances"]),
    ("s10", "behavior", "fsx", "What is the Lustre Intelligent-Tiering storage class (elastic, pay for use, SSD read cache), and when is it cheaper than SSD or HDD?", ["docs/fsx/latest/LustreGuide/intelligent-tiering-file-systems", "www/fsx/lustre/faqs"]),
    ("s10", "numbers", "fsx", "Lustre pricing dimensions: provisioned storage GB-month by class and throughput tier, Intelligent-Tiering by usage, backups, data repository requests.", ["www/fsx/lustre/pricing", "www/fsx/lustre/faqs"]),
    ("s2", "numbers", "fsx", "Lustre quotas: file systems per account (100), maximum storage per Persistent 2 file system (1,200,000 GiB), HDD read cache size.", ["docs/fsx/latest/LustreGuide/limits"]),
    ("k4", "behavior", "fsx", "Lustre encryption at rest (default KMS) and in transit (supported instance types only).", ["docs/fsx/latest/LustreGuide/what-is", "www/fsx/lustre/faqs"]),
    ("r8", "decisions+changes", "fsx", "Changed recently (hypotheses): release data repository tasks (2023-08-09); throughput tier adjustable (2023-11-16); metadata IOPS up 15x (2024-06-07); EFA and GPUDirect (2024-11-27); Lustre version upgrades (2025-02-12); Intelligent-Tiering (2025-05-29).", ["docs/fsx/latest/LustreGuide/doc-history"]),
    ("r8", "behavior", "fsx", "How does SageMaker or AWS Batch use FSx for Lustre to speed up training and HPC jobs (the FAQ answers)?", ["www/fsx/lustre/faqs"]),
    # ---- FSx for NetApp ONTAP
    ("r8", "behavior", "fsx", "What is FSx for NetApp ONTAP, which protocols does it serve at once (NFS, SMB, iSCSI, NVMe/TCP), and which clients (Linux, Windows, macOS)?", ["docs/fsx/latest/ONTAPGuide/what-is-fsx-ontap", "docs/fsx/latest/ONTAPGuide/supported-fsx-clients", "www/fsx/netapp-ontap/faqs"]),
    ("r11", "behavior", "fsx", "ONTAP Single-AZ versus Multi-AZ: HA pair, standby, failover trigger and time; second-generation scale-out with up to 12 HA pairs.", ["docs/fsx/latest/ONTAPGuide/high-availability-AZ", "www/fsx/netapp-ontap/faqs"]),
    ("k7", "behavior", "fsx", "ONTAP storage tiers: primary SSD and capacity pool; tiering policies (Snapshot-only, Auto, All, None), cooling days, and what moves to capacity pool.", ["docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap", "docs/fsx/latest/ONTAPGuide/modify-volume-tiering-policy", "www/fsx/netapp-ontap/faqs"]),
    ("s10", "numbers", "fsx", "ONTAP storage efficiency (deduplication, compression, compaction): typical savings percentage for general file shares, and what capacity pool costs relative to SSD.", ["docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap", "www/fsx/netapp-ontap/faqs", "www/fsx/netapp-ontap/pricing"]),
    ("r11", "behavior", "fsx", "SnapMirror for cross-Region replication and DR, FlexCache for low-latency caching, and snapshots for user self-service restores.", ["docs/fsx/latest/ONTAPGuide/scheduled-replication", "docs/fsx/latest/ONTAPGuide/using-flexcache", "docs/fsx/latest/ONTAPGuide/snapshots-ontap"]),
    ("r11", "behavior", "fsx", "SnapLock WORM: Compliance versus Enterprise mode, who can delete, retention; licensing charge removed 2025-03-05.", ["docs/fsx/latest/ONTAPGuide/snaplock", "docs/fsx/latest/ONTAPGuide/how-snaplock-works", "www/fsx/netapp-ontap/faqs"]),
    ("r7", "behavior", "fsx", "Storage virtual machines and volumes: what each is, and how an SVM joins Active Directory for SMB access.", ["docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap", "www/fsx/netapp-ontap/faqs"]),
    ("s1", "numbers", "fsx", "ONTAP limits: maximum SSD capacity (first generation 192 TiB; second generation 512 TiB per HA pair up to 1 PiB), throughput capacity range, SSD IOPS, capacity pool size.", ["docs/fsx/latest/ONTAPGuide/limits", "docs/fsx/latest/ONTAPGuide/performance", "www/fsx/netapp-ontap/faqs"]),
    ("r11", "behavior", "fsx", "ONTAP backups: volume-level daily backups, retention up to 90 days, AWS Backup support, cross-Region copy (2026-08-27: after the examinability cutoff).", ["www/fsx/netapp-ontap/faqs", "docs/fsx/latest/ONTAPGuide/limits", "docs/fsx/latest/ONTAPGuide/document-history"]),
    ("k7", "behavior", "fsx", "S3 access points attached to ONTAP (2025-12-02) and OpenZFS (2025-06-25) volumes: S3 API access to file data without copying; examinable or not?", ["docs/fsx/latest/ONTAPGuide/accessing-data-via-s3-access-points", "docs/fsx/latest/OpenZFSGuide/s3accesspoints-for-FSx", "docs/fsx/latest/ONTAPGuide/document-history"]),
    ("r7", "behavior", "fsx", "Migrating an on-premises NetApp system to FSx for ONTAP (SnapMirror, DataSync) and using ONTAP as a VMware Cloud on AWS datastore.", ["www/fsx/netapp-ontap/faqs", "docs/fsx/latest/ONTAPGuide/what-is-fsx-ontap"]),
    ("s10", "numbers", "fsx", "ONTAP pricing dimensions: SSD storage, capacity pool storage and requests, throughput capacity, provisioned SSD IOPS above the included 3 per GiB, backups; Multi-AZ pricing.", ["www/fsx/netapp-ontap/pricing", "www/fsx/netapp-ontap/faqs"]),
    ("k4", "behavior", "fsx", "ONTAP encryption at rest (KMS) and in transit (SMB encryption, Nitro-based encryption, IPsec, Kerberos for NFS).", ["www/fsx/netapp-ontap/faqs", "docs/fsx/latest/ONTAPGuide/what-is-fsx-ontap"]),
    ("r8", "behavior", "fsx", "Shared block storage on ONTAP: iSCSI LUNs and NVMe/TCP for Windows and Linux hosts (for SQL Server and VMware).", ["docs/fsx/latest/ONTAPGuide/supported-fsx-clients", "www/fsx/netapp-ontap/faqs"]),
    ("k4", "behavior", "fsx", "How is a Multi-AZ ONTAP file system reached from on-premises or a peered VPC (floating IP, routing through transit gateway)?", ["docs/fsx/latest/ONTAPGuide/high-availability-AZ", "www/fsx/netapp-ontap/faqs"]),
    ("r11", "behavior", "fsx", "Autonomous Ransomware Protection on ONTAP (2025-04-07): what it detects and what it does.", ["www/fsx/netapp-ontap/faqs", "docs/fsx/latest/ONTAPGuide/document-history"]),
    ("r8", "decisions+changes", "fsx", "Changed recently (hypotheses): 12 HA pairs and 72 GBps (2024-03-04); second-generation file systems and NVMe/TCP (2024-07-09); decreasing SSD capacity (2025-08-14); S3 access (2025-12-02).", ["docs/fsx/latest/ONTAPGuide/document-history"]),
    ("r8", "faq", "fsx", "When should you use FSx for ONTAP versus the other FSx types (the FAQ answer)?", ["www/fsx/netapp-ontap/faqs"]),
    # ---- FSx for OpenZFS
    ("r8", "behavior", "fsx", "What is FSx for OpenZFS, which NFS versions does it serve, which clients, and what are its signature features (snapshots, clones, compression)?", ["docs/fsx/latest/OpenZFSGuide/what-is-fsx", "www/fsx/openzfs/faqs"]),
    ("r11", "behavior", "fsx", "OpenZFS deployment types: Single-AZ (non-HA), Single-AZ (HA) and Multi-AZ; when to choose each; failover behaviour.", ["docs/fsx/latest/OpenZFSGuide/availability-durability", "www/fsx/openzfs/faqs"]),
    ("s1", "numbers", "fsx", "OpenZFS performance and limits: throughput capacity range (64 to 10,240 MBps), IOPS (up to 400,000 or more), latency, storage 64 GiB to 512 TiB.", ["docs/fsx/latest/OpenZFSGuide/performance", "docs/fsx/latest/OpenZFSGuide/limits", "www/fsx/openzfs/faqs"]),
    ("r11", "behavior", "fsx", "OpenZFS snapshots and clones: point-in-time, near-instant, writable clones; user and group quotas; which compression algorithms.", ["docs/fsx/latest/OpenZFSGuide/snapshots-openzfs", "www/fsx/openzfs/faqs"]),
    ("r11", "behavior", "fsx", "OpenZFS replication: on-demand data replication across file systems and Regions, periodic replication, backups.", ["docs/fsx/latest/OpenZFSGuide/on-demand-replication", "www/fsx/openzfs/faqs"]),
    ("s10", "behavior", "fsx", "OpenZFS Intelligent-Tiering storage class (2024-12-01): elastic capacity, SSD read cache, cost versus SSD.", ["docs/fsx/latest/OpenZFSGuide/performance-intelligent-tiering", "www/fsx/openzfs/faqs"]),
    ("s10", "numbers", "fsx", "OpenZFS pricing dimensions: SSD storage, throughput capacity, provisioned IOPS above the included, backups, Intelligent-Tiering by usage.", ["www/fsx/openzfs/pricing", "www/fsx/openzfs/faqs"]),
    ("r8", "faq", "fsx", "When should you use FSx for OpenZFS versus the other FSx types and versus EFS (the FAQ answer)?", ["www/fsx/openzfs/faqs", "www/fsx/when-to-choose-fsx"]),
    ("s2", "numbers", "fsx", "OpenZFS quotas: volumes per file system (100), snapshots (700), client connections per file server.", ["docs/fsx/latest/OpenZFSGuide/limits"]),
    ("r8", "decisions+changes", "fsx", "Changed recently (hypotheses): Multi-AZ (2023-08-09); on-demand replication (2023-11-26); Single-AZ (HA) (2024-07-09); Intelligent-Tiering (2024-12-01); S3 access (2025-06-25); Multi-AZ in shared VPCs (2026-05-13).", ["docs/fsx/latest/OpenZFSGuide/document-history"]),
    # ---- Cross-cutting (family), Callvale, real world
    ("k7", "decisions+changes", "fsx", "Data lifecycle across the family: EFS lifecycle policies, Lustre release and export to S3, ONTAP capacity pool tiering, FSx Intelligent-Tiering: which is automatic and which needs a task?", ["docs/efs/latest/ug/lifecycle-management-efs", "docs/fsx/latest/LustreGuide/data-repository-tasks", "docs/fsx/latest/ONTAPGuide/how-it-works-fsx-ontap"]),
    ("r11", "decisions+changes", "fsx", "Durability and replication across the family: which file systems are multi-AZ by design, which offer a Multi-AZ option, which are single-AZ only, and which replicate across Regions natively.", ["docs/efs/latest/ug/whatisefs", "docs/fsx/latest/WindowsGuide/high-availability-multiAZ", "docs/fsx/latest/ONTAPGuide/high-availability-AZ", "docs/fsx/latest/OpenZFSGuide/availability-durability", "www/fsx/lustre/faqs"]),
    ("s4", "decisions+changes", "fsx", "Which file systems need capacity planning and when 'storage auto scaling' is required: EFS (none), FSx (provisioned capacity, increase only, alarm-driven automation), Intelligent-Tiering (elastic).", ["docs/fsx/latest/WindowsGuide/managing-storage-configuration", "docs/efs/latest/ug/whatisefs", "docs/fsx/latest/OpenZFSGuide/performance-intelligent-tiering"]),
    ("r7", "decisions+changes", "fsx", "Legacy application patterns with no code change: Windows app with SMB and AD permissions (FSx for Windows), Linux app with a shared directory (EFS), on-premises NetApp (ONTAP), ZFS or NFS appliance (OpenZFS).", ["www/fsx/when-to-choose-fsx", "www/efs/faq", "www/fsx/windows/faqs"]),
    ("r8", "decisions+changes", "fsx", "Purpose-built picks: HPC or ML training on an S3 dataset that needs hundreds of GBps (Lustre); SQL Server shared storage (FSx for Windows CA shares or ONTAP iSCSI); shared container storage (EFS).", ["www/fsx/lustre/faqs", "docs/fsx/latest/WindowsGuide/sql-server", "www/efs/faq"]),
    ("r11", "behavior", "fsx", "AWS Backup coverage of EFS and every FSx type, and the logically air-gapped vault support for FSx (2025-03-13) and for ONTAP (2026-09-28: after the cutoff).", ["docs/efs/latest/ug/automatic-backups", "www/fsx/windows/faqs", "docs/fsx/latest/ONTAPGuide/document-history"]),
    ("k2", "behavior", "efs", "Callvale decision facts: EFS mounts from many instances in three AZs through one mount target per AZ, ECS on Fargate and Linux workers can mount it, no code change for a POSIX directory, and the per-GB price is above S3 Standard.", ["docs/efs/latest/ug/how-it-works", "www/efs/faq", "www/efs/pricing"]),
    ("r7", "behavior", "fsx", "Callvale stage 4 facts: Peldon's 12 TB of Windows file shares move to FSx for Windows (SMB, Directory Service, DataSync or Robocopy migration, Multi-AZ, 64 TiB maximum).", ["docs/fsx/latest/WindowsGuide/migrate-files-fsx", "docs/fsx/latest/WindowsGuide/aws-ad-integration-fsxW", "docs/fsx/latest/WindowsGuide/limits"]),
    ("k4", "decisions+changes", "efs", "Real-world example (EFS): one sentence from an AWS case study (DeepBrain AI, startup, EFS with EKS; or Ancestry, genomics on EFS).", ["www/solutions/case-studies/deepbrain-case-study", "www/solutions/case-studies/ancestry-case-study"]),
    ("k4", "decisions+changes", "fsx", "Real-world example (FSx): one sentence from an AWS case study (Adobe, Firefly training on FSx for Lustre; or Phillips 66, NetApp migration to FSx for ONTAP).", ["www/solutions/case-studies/adobe-case-study", "www/solutions/case-studies/phillips66-migration-case-study"]),
    # ---- FAQ quick-fire candidates (one per service family beyond those above)
    ("k2", "faq", "efs", "FAQ quick-fire: 'How many file systems, mount targets, or access points can I create?' and 'How much data can I store?'", ["www/efs/faq"]),
    ("s1", "faq", "efs", "FAQ quick-fire: 'What latency, throughput, and IOPS performance can I expect?' and 'What throughput modes are available?'", ["www/efs/faq"]),
    ("r11", "faq", "efs", "FAQ quick-fire: 'How durable is Amazon EFS?' and 'Is my replica file system point-in-time consistent?'", ["www/efs/faq"]),
    ("r11", "faq", "fsx", "FAQ quick-fire (Windows): 'What is the difference between Single-AZ and Multi-AZ file systems?' and 'What happens during a failover and how long does it take?'", ["www/fsx/windows/faqs"]),
    ("s10", "faq", "fsx", "FAQ quick-fire (Windows): 'What storage options does Amazon FSx support? How should I choose?' and 'How much storage savings can I expect with Data Deduplication?'", ["www/fsx/windows/faqs"]),
    ("r8", "faq", "fsx", "FAQ quick-fire (Lustre): 'What deployment options are available?' and 'How does Amazon FSx for Lustre stay synchronized with my S3 buckets?'", ["www/fsx/lustre/faqs"]),
    ("r11", "faq", "fsx", "FAQ quick-fire (Lustre): 'Can I take a backup of any FSx for Lustre file system?' and 'What are the availability and durability characteristics?'", ["www/fsx/lustre/faqs"]),
    ("k7", "faq", "fsx", "FAQ quick-fire (ONTAP): 'How does capacity pool tiering reduce my storage costs?' and 'What percentage of my data can I have tiered to capacity pool storage?'", ["www/fsx/netapp-ontap/faqs"]),
    ("r11", "faq", "fsx", "FAQ quick-fire (ONTAP): 'When should I use a Multi-AZ file system vs. a Single-AZ file system?' and 'Does FSx for ONTAP offer write-once-read-many protection?'", ["www/fsx/netapp-ontap/faqs"]),
    ("r11", "faq", "fsx", "FAQ quick-fire (OpenZFS): 'When should I use a Single-AZ (non-HA) file system?' and 'What capabilities does FSx for OpenZFS provide for disaster recovery?'", ["www/fsx/openzfs/faqs"]),
    ("s10", "faq", "fsx", "FAQ quick-fire (OpenZFS): 'How does Intelligent-Tiering reduce my costs?' and 'How is the SSD read cache sized by default?'", ["www/fsx/openzfs/faqs"]),
]

demand = []
for n, (b, lens, service, q, hints) in enumerate(D, start=1):
    demand.append({
        "id": f"d{n:03d}",
        "bullet": B[b],
        "question": q,
        "status": "open",
        "facts": [],
        "lens": lens,
        "service": service,
        "sources": hints,
    })

covered = {d["bullet"] for d in demand}
missing = [b for b in entry["bullets"] if b not in covered]
if missing:
    print("BULLETS WITHOUT A DEMAND ITEM:", missing)
    sys.exit(1)

brief = {
    "chapter": "23",
    "slug": "efs-fsx",
    "title": "EFS and FSx",
    "template": "deep",
    "services": ["efs", "fsx"],
    "sources_fetched": len(fetched),
    "fetch_failures": failures,
    "sources": fetched,
    "demand": demand,
    "notes": [
        "Plan stage, run plan-23. Every demand item is a question; no answer is recorded here.",
        "FREQUENCY.md and FRESHNESS.md items appear only as hypotheses to check against the saved pages.",
        "GA dates after 2026-07-15 (ONTAP cross-Region backup copy 2026-08-27, ONTAP air-gapped vault 2026-09-28, DataSync Enhanced mode 2026-07-28, MGN to ONTAP 2026-08-30, OpenZFS Multi-AZ shared VPC 2026-05-13 is before) must be labelled per RULINGS rule 7 once dated from the saved history page.",
        "Neighbour facts that live elsewhere: EBS Multi-Attach (chapter 22), S3 classes (chapter 21), AWS Backup vault lock (chapter 24), Storage Gateway and FSx File Gateway closure (chapter 25), DataSync (chapter 25 or 26).",
    ],
}
json.dump(brief, open(WORK / "brief.v0.json", "w"), indent=1)

# ---- mine plan: pages and demand items per lens
pages_by_lens = {"numbers": [], "behavior": [], "decisions+changes": [], "faq": []}
for sid in fetched:
    if "/limits" in sid or "/pricing" in sid or "/performance" in sid or "metered-sizes" in sid or "managing-throughput" in sid \
       or "ssd-storage" in sid or "intelligent-tiering" in sid or "volume-storage-capacity" in sid or "managing-storage-configuration" in sid \
       or "high-availability" in sid or "availability-durability" in sid or "managing-data-dedup" in sid:
        pages_by_lens["numbers"].append(sid)
    if "/faq" in sid:
        pages_by_lens["faq"].append(sid)
    elif "document-history" in sid or "doc-history" in sid or "decision-guides" in sid or "when-to-choose-fsx" in sid \
         or "whitepapers" in sid or "s3-files" in sid or "case-studies" in sid:
        pages_by_lens["decisions+changes"].append(sid)
    elif "/limits" in sid or "/pricing" in sid:
        pass
    else:
        pages_by_lens["behavior"].append(sid)

plan = {
    "chapter": "23",
    "lenses": {
        lens: {
            "what": what,
            "pages": pages_by_lens[lens],
            "demand": [d["id"] for d in demand if d["lens"] == lens],
            "extra_indexes": extra,
        }
        for lens, what, extra in [
            ("numbers", "Every limit, default, size, throughput, IOPS, latency, retention, percentage and price dimension; quote table rows with the header; one fact per value.",
             ["_build/corpus/faq/efs.jsonl (pricing section)"]),
            ("behavior", "Can / cannot / only / always claims: protocols, clients, mount model, deployment types, failover, replication, backups, encryption, access control, S3 link, tiering.", []),
            ("decisions+changes", "Choice rules between EFS, the FSx types, S3, EBS; every FRESHNESS hypothesis checked against the saved history page with the date; case-study sentences; examinability label for GA after 2026-07-15.",
             ["_build/corpus/changes/efs.jsonl", "_build/corpus/changes/fsx.jsonl", "_build/corpus/cases/index.jsonl"]),
            ("faq", "Verbatim FAQ sentences for the 10 quick-fire items and the comparison answers; quote from the FAQ snapshot, matched with find_quote.",
             ["_build/corpus/faq/efs.jsonl", "_build/corpus/faq/fsx-windows.jsonl", "_build/corpus/faq/fsx-lustre.jsonl", "_build/corpus/faq/fsx-netapp-ontap.jsonl", "_build/corpus/faq/fsx-openzfs.jsonl"]),
        ]
    },
    "work_files": sorted(p.name for p in WORK.glob("*.txt")),
    "rules": [
        "Quote only from snap/<source_id>.txt; full:<guide> hits are pointers.",
        "A FAQ or What's New row is an index, never the evidence; the fact's quote comes from the page snapshot.",
        "Current AWS names only; 'Standard-IA' and 'One Zone-IA' may appear once as former names.",
    ],
}
json.dump(plan, open(WORK / "mine-plan.json", "w"), indent=1)
print(f"sources_fetched={len(fetched)} failures={len(failures)} demand={len(demand)}")
for f in failures:
    print("  missing:", f["url"])
for lens, v in plan["lenses"].items():
    print(f"  {lens}: pages={len(v['pages'])} demand={len(v['demand'])}")
