## How it works (51 min)
<!-- section: role=how; route=full; minutes=51 -->

### An EBS volume lives in one Availability Zone and can outlive its instance (3 min)

An Amazon EBS **volume** (VOL-yoom) is storage that keeps its data after a stop.

1. **Attach in one zone.** The volume and the instance [must be in the same Availability Zone](../facts/ebs.md#ebs-volume-same-az-as-instance).
2. **Copy inside the zone.** EBS keeps the volume [automatically replicated within its Availability Zone](../facts/ebs.md#ebs-volume-replicated-within-az).
3. **Outlive a stop.** The volume is [off-instance storage](../facts/ebs.md#ebs-volume-persists-independently-of-instance) that [remains attached throughout the stop-start cycle](../facts/ebs.md#ebs-volume-stays-attached-through-stop-start).
4. **Decide at termination.** A flag on each attached volume decides whether it is deleted with its instance.

Why off the instance? The instance can be replaced, but the data has to stay.

> **Exam signal:** "the data must stay after the instance is terminated" points to the [Delete on termination flag](../facts/ebs.md#ebs-faq-root-delete-on-termination-no) of the root volume.

> **Exam trap:** Many think that a volume can move to another zone. It [must be in the same Availability Zone](../facts/ebs.md#ebs-volume-same-az-as-instance) as its instance: restore a **snapshot** there. <!-- trap: ebs-trap-volume-attaches-across-azs -->

> **Say it:** The short answer is: a volume is block storage in one zone. The thing to watch is the delete flag of the root volume.

**Stop and answer.** An instance with default root and data volumes is terminated. Which volume survives?

<details>
<summary>Answer</summary>

The data volume. By default, the root volume is [deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-root-default-true). Other volumes created at launch [are not deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-additional-default-false).

</details>

### Instance store data lives on the host and ends with the instance (3 min)

A cache or scratch files must be fast, and they can disappear.

1. **Use storage on the host.** An **instance store** gives [temporary block-level storage](../facts/instance-store.md#instance-store-physically-attached-host-disks) on disks [physically attached to the host computer](../facts/instance-store.md#instance-store-physically-attached-host-disks).
2. **Get it with the type, at launch.** [Not every instance type provides instance store volumes](../facts/instance-store.md#instance-store-size-varies-by-type), and [there is no additional charge](../facts/instance-store.md#instance-store-no-additional-charge). You attach them [only when you launch it](../facts/instance-store.md#instance-store-attach-only-at-launch).
3. **Get the speed.** SSD instance store volumes give [high random I/O performance with very low latency](../facts/instance-store.md#instance-store-ssd-high-random-io).
4. **Lose it after a stop.** Data [persists even if the instance is rebooted](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop), but a stop ends it.

Why does a stop erase it? At a stop, hibernation or termination, every block is [cryptographically erased](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop). So the data is **ephemeral** (ih-FEM-er-ul).

> **Exam signal:** "temporary data", "cache" or "scratch data" points to instance store, which fits [buffers, caches, scratch data](../facts/instance-store.md#instance-store-ideal-for-temporary-data).

> **Say it:** The short answer is: instance store is fast scratch space on the host. The thing to watch is a stop.

**Stop and answer.** A team caches thumbnails on instance store. The instance is rebooted on Monday and stopped on Friday. Is the cache there on Tuesday, and after the weekend?

<details>
<summary>Answer</summary>

Tuesday: yes, the data [persists even if the instance is rebooted](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop). After the weekend: no, the [data on any instance store volumes is erased](../facts/instance-store.md#instance-store-data-erased-on-stop).

</details>

### SSD volumes serve small random IO and HDD volumes serve large sequential reads (4 min)
<!-- section: route=pass -->

A database makes small random reads and needs **IOPS** (EYE-ops), operations each second. A log job reads large files in order and needs **throughput** (THROO-put), data each second.

1. **Pick the family.** Solid state drive (SSD) volumes are [SSD-backed storage for transactional workloads](../facts/ebs.md#ebs-ssd-transactional-hdd-throughput-categories). Hard disk drive (HDD) volumes are [HDD-backed storage for throughput intensive workloads](../facts/ebs.md#ebs-ssd-transactional-hdd-throughput-categories).
2. **Match the input and output (I/O).** st1 and sc1 suit [large, sequential I/O](../facts/ebs.md#ebs-hdd-large-sequential-not-small-random). sc1 serves [colder data requiring fewer scans per day](../facts/ebs.md#ebs-sc1-use-cases).

![A decision ladder with three questions. Large sequential data that is scanned rarely leads to sc1; large sequential data that is scanned often leads to st1; a need beyond gp3 leads to io2 Block Express; everything else leads to gp3.](../diagrams/svg/ebs-volume-ladder.svg)

**Figure.** Large sequential data fits an HDD type, and other workloads start on gp3 unless they need io2 Block Express.

Why do small random reads perform badly on HDD? There, an I/O of [1 MiB or less counts as a 1 MiB I/O credit](../facts/ebs.md#ebs-hdd-io-counted-as-1-mib). A small random read costs as much as a large one, and sequential reads are merged.

> **Exam signal:** "big data" or "log processing" points to st1, and "cold data" at the lowest cost to sc1.

> **Say it:** The short answer is: SSD for small random reads, HDD for long scans. The thing to watch is the boot volume.

**Stop and answer.** A weekly job scans 10 TB of logs, with no deadline. Which HDD type fits, and what would change your answer?

<details>
<summary>Answer</summary>

sc1: [the lowest cost per GB](../facts/ebs.md#ebs-sc1-lowest-cost-per-gb), and a rare scan can live with its [maximum of 250 MiB/s](../facts/ebs.md#ebs-sc1-max-throughput). A fast or frequent scan needs st1, with a [maximum of 500 MiB/s](../facts/ebs.md#ebs-st1-max-throughput).

</details>

### gp3 lets you buy IOPS and throughput without buying more storage (4 min)
<!-- section: route=pass -->

A small database needs many IOPS but little space. gp3 gives a baseline at any size, and you add IOPS as you need them.

1. **Start at the baseline.** Every gp3 volume gets [3,000 IOPS](../facts/ebs.md#ebs-gp3-baseline-iops) and [125 MiB/s](../facts/ebs.md#ebs-gp3-baseline-throughput) at any size.
2. **Add performance on its own.** You raise IOPS and throughput [independently of volume size](../facts/ebs.md#ebs-gp3-performance-independent-of-size), up to [500 IOPS per GiB](../facts/ebs.md#ebs-gp3-max-iops-80000). The maximum of [80,000](../facts/ebs.md#ebs-gp3-max-iops-80000) IOPS needs [160 GiB or larger](../facts/ebs.md#ebs-gp3-max-iops-80000).
3. **Compare gp2.** gp2 gives [3 IOPS per GiB](../facts/ebs.md#ebs-gp2-iops-per-gib), so its [performance scales with volume size](../facts/ebs.md#ebs-gp2-performance-scales-with-size).

<!-- table: plain -->
| Question | gp3 | gp2 |
|---|---|---|
| Burst | None: [3,000 IOPS](../facts/ebs.md#ebs-faq-gp3-no-burst) of consistent performance | [burst to 3,000 IOPS](../facts/ebs.md#ebs-gp2-burst-3000-iops) when [smaller than 1 TiB](../facts/ebs.md#ebs-gp2-burst-3000-iops) |
| Price per GiB | [20 percent lower price per GiB](../facts/ebs.md#ebs-gp3-20-percent-lower-price) | Higher |

Why split size and IOPS? They are two needs, and [you pay only for what you provision](../facts/ebs.md#ebs-billed-provisioned-gb-month).

> **Exam signal:** "cost-effective" with "boot volumes" or "medium-sized databases" points to gp3, for a [balance between cost and performance](../facts/ebs.md#ebs-faq-gp3-suited-workloads).

> **Exam trap:** Many think that a slow gp2 database needs a bigger volume. gp3 adds IOPS [independently of volume size](../facts/ebs.md#ebs-gp3-performance-independent-of-size). <!-- trap: ebs-trap-grow-gp-volume-for-iops -->

> **Say it:** The short answer is: gp3 sells space and IOPS separately. The thing to watch is gp2, where more IOPS means more space.

**Stop and answer.** A 200 GiB gp2 volume gives a database too few IOPS. No more space is needed. What is the cheapest fix?

<details>
<summary>Answer</summary>

Change it to gp3 and provision IOPS, at a [20 percent lower price per GiB](../facts/ebs.md#ebs-gp3-20-percent-lower-price).

</details>

### io2 Block Express buys more IOPS lower latency and higher durability (4 min)

io2 Block Express costs more than gp3, so choose it when a requirement asks for it.

1. **Know where gp3 ends.** AWS points to io2 Block Express for [higher durability, better latency consistency](../facts/ebs.md#ebs-faq-gp3-to-io2-when), or more IOPS.
2. **Provision the IOPS.** One volume takes [up to 256,000](../facts/ebs.md#ebs-io2-max-iops-ratio) IOPS on a Nitro instance, at [1,000:1](../facts/ebs.md#ebs-io2-max-iops-ratio) IOPS per GiB. Nitro is [a collection of hardware and software components](../facts/ec2.md#ec2-nitro-system-definition) built by AWS.
3. **Get lower latency.** **Latency** (LAY-ten-see) is the time a request takes. io2 Block Express is [sub-millisecond](../facts/ebs.md#ebs-faq-average-latency), and gp3 has [single-digit millisecond latency](../facts/ebs.md#ebs-gp3-latency).
4. **Get higher durability.** **Durability** (dyoor-uh-BIL-ih-tee) is how unlikely data loss is. io2 Block Express has [99.999 percent volume durability](../facts/ebs.md#ebs-io2-durability-afr), and gp3 has [99.8 percent to 99.9 percent](../facts/ebs.md#ebs-gp3-durability-afr).

- **Wrong belief:** io2 durability makes snapshots unnecessary. **Truth:** Durability and snapshots [protect against different types of failures](../facts/ebs.md#ebs-faq-io2-still-snapshot-and-replicate). <!-- trap: ebs-trap-io2-durability-replaces-backup -->

Why pay more? Block Express talks to Nitro instances over [Scalable Reliable Datagrams (SRD)](../facts/ebs.md#ebs-faq-block-express-definition), a faster network protocol.

> **Exam signal:** "sub-millisecond latency" points to io2 Block Express, for [consistent sub-millisecond latency](../facts/ebs.md#ebs-io2-use-cases).

> **Exam trap:** Many think that every production database needs io2. gp3 is [the lowest cost SSD volume](../facts/ebs.md#ebs-gp3-lowest-cost-ssd) and fits [medium sized single instance databases](../facts/ebs.md#ebs-gp3-use-cases). <!-- trap: ebs-trap-io2-for-every-database -->

> **Say it:** The short answer is: io2 Block Express is for the database that outgrows gp3. The thing to watch is the price.

**Stop and answer.** An io2 Block Express volume has 60,000 provisioned IOPS and is attached to an instance type not built on Nitro. What does the database get?

<details>
<summary>Answer</summary>

About half. Such types attach volumes provisioned with [up to 64,000 IOPS](../facts/ebs.md#ebs-io2-nitro-iops-limit), but they reach [up to 32,000 IOPS](../facts/ebs.md#ebs-io2-nitro-iops-limit).

</details>

### The instance and its EBS bandwidth can cap a fast volume (4 min)

A team provisions a fast volume, and the database is still slow.

1. **The smaller limit wins.** EBS performance is [bounded by the instance type's performance limits](../facts/ebs.md#ebs-instance-performance-bounded-by-smaller) or the volumes, [whichever is smaller](../facts/ebs.md#ebs-instance-performance-bounded-by-smaller).
2. **Use EBS-optimized bandwidth.** EBS-optimized instances give [dedicated bandwidth for Amazon EBS I/O](../facts/ebs.md#ebs-optimized-dedicated-bandwidth). On current generation types, EBS optimization is [enabled by default at no additional cost](../facts/ec2.md#ec2-ebs-optimized-default-current-generation).
3. **Stripe for more.** [Creating a RAID 0 array](../facts/ebs.md#ebs-raid0-more-than-one-volume) (a redundant array of independent disks) adds performance, but one lost volume means [complete data loss for the array](../facts/ebs.md#ebs-raid0-one-volume-loss-loses-array).

- **Wrong belief:** More volume IOPS speed up any instance. **Truth:** An instance at its own EBS limit gets nothing more. <!-- trap: ebs-trap-more-volume-iops-raises-instance-io -->

Why does the instance matter? Every I/O travels over the instance's own link to EBS, and that link is the instance's [dedicated bandwidth for Amazon EBS I/O](../facts/ebs.md#ebs-optimized-dedicated-bandwidth).

> **Exam signal:** "the volume never reaches its provisioned IOPS" points to the EBS limit of the instance type.

> **Say it:** The short answer is: the instance has its own EBS limit. The thing to watch is RAID 0: one lost volume loses the array.

**Stop and answer.** Two volumes of 40,000 IOPS each serve one instance whose EBS limit is lower than their sum. What limits the database?

<details>
<summary>Answer</summary>

The instance type, because EBS performance follows [whichever is smaller](../facts/ebs.md#ebs-instance-performance-bounded-by-smaller).

</details>

### Elastic Volumes grows or retunes a volume in place but cannot shrink it (3 min)

A volume fills up, and the team wants no stop and no copy.

1. **Modify in place.** Elastic Volumes can [increase the volume size, change the volume type](../facts/ebs.md#ebs-elastic-volumes-modify-without-detach) or adjust performance. On an instance that supports it, this works [without detaching the volume or restarting the instance](../facts/ebs.md#ebs-elastic-volumes-modify-without-detach).
2. **Grow the file system.** After a size increase, [you must also extend the volume's partition](../facts/ebs.md#ebs-extend-partition-after-size-increase) and the **file system**.

- **Wrong belief:** More space needs a new, larger volume. **Truth:** Elastic Volumes grows the same volume in place. <!-- trap: ebs-trap-grow-needs-new-volume -->

> **Exam signal:** "increase storage or IOPS with no downtime" points to Elastic Volumes.

> **Exam trap:** Many think that a team can shrink a volume after a cleanup. For a smaller size, you [create a smaller volume](../facts/ebs.md#ebs-volume-size-cannot-decrease) and copy the data. <!-- trap: ebs-trap-shrink-volume -->

> **Try it:** Try to shrink a gp3 volume, then grow and retune it. See [3-do.md](3-do.md). <!-- task: ebs-t02 -->

> **Say it:** The short answer is: grow or retune a volume as it runs. The thing to watch is that it does not shrink.

**Stop and answer.** A team grew a volume from 100 GiB to 300 GiB. The operating system still shows 100 GiB. What is missing?

<details>
<summary>Answer</summary>

The partition and the file system: [you must also extend the volume's partition](../facts/ebs.md#ebs-extend-partition-after-size-increase).

</details>

### Multi-Attach shares one io2 volume and the application must coordinate writes (4 min)

A clustered database wants two instances to see one volume, so that a **standby** can take over immediately.

1. **Attach to several instances.** Multi-Attach lets you [attach a single Provisioned IOPS SSD](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az) volume to instances [in the same Availability Zone](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az).
2. **Coordinate the writes.** XFS and EXT4 are [not designed to be accessed simultaneously](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system), so you [use a clustered file system](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system).

- **Wrong belief:** A gp3 volume can use Multi-Attach. **Truth:** Multi-Attach is [supported exclusively on](../facts/ebs.md#ebs-multi-attach-provisioned-iops-only) io1 and io2. <!-- trap: ebs-trap-multi-attach-any-volume-type -->

> **Exam signal:** "shared block storage" for a cluster in one zone points to io2 with Multi-Attach.

> **Exam trap:** Many think that a web fleet in three zones can share uploads on one Multi-Attach volume. Multi-Attach works [in the same Availability Zone](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az), so Amazon EFS fits the fleet. <!-- trap: ebs-trap-multi-attach-as-shared-file-system -->

> **Say it:** The short answer is: a cluster in one zone can share one io2 volume. The thing to watch is write safety.

**Stop and answer.** Two nodes share an io2 volume with 64,000 provisioned IOPS, and both are busy. Can each node get 64,000 IOPS?

<details>
<summary>Answer</summary>

No. The [aggregate performance of all of the attached instances](../facts/ebs.md#ebs-multi-attach-shares-provisioned-performance) stays within the provisioned IOPS.

</details>

### Each snapshot stores changed blocks but can restore the whole volume (4 min)
<!-- section: route=pass -->

Replication does not bring back a deleted table. A backup does.

1. **Copy changes.** Snapshots are [incremental backups](../facts/ebs.md#ebs-snapshot-incremental-changed-blocks): after the first, EBS saves the [blocks on the volume that have changed](../facts/ebs.md#ebs-snapshot-incremental-changed-blocks).
2. **Store outside the zone.** The data is [stored redundantly in multiple Availability Zones](../facts/ebs.md#ebs-snapshot-stored-in-s3-multiple-azs) in Amazon S3.
3. **Mind the cache.** A snapshot [does not include data that has been cached](../facts/ebs.md#ebs-snapshot-excludes-cached-data) by the application or the operating system. For a complete snapshot, [pause writes to the volume](../facts/ebs.md#ebs-snapshot-consistency-pause-writes-or-unmount) first.

- **Wrong belief:** Snapshots sit in your own S3 **bucket**. **Truth:** You manage them with the Amazon EC2 API, not with the [Amazon S3 console or the Amazon S3 API](../facts/ebs.md#ebs-snapshot-s3-buckets-not-accessible). <!-- trap: ebs-trap-snapshots-in-my-s3-bucket -->

![Two panels. Before: snapshot 1 holds blocks A, B and C, snapshot 2 holds a new block B and points to A and C in snapshot 1, snapshot 3 holds a new block C. After snapshot 1 is deleted: block A stays with snapshot 2, and snapshot 3 still restores the whole volume.](../diagrams/svg/ebs-snapshot-chain.svg)

**Figure.** Deleting an older snapshot keeps the blocks that newer snapshots still use, so the newest one still restores the whole volume.

> **Exam signal:** "point-in-time backup of an EBS volume" points to a snapshot.

> **Exam trap:** Many think that deleting old snapshots breaks the newest restore. Deletion removes [only the data that is referenced exclusively](../facts/ebs.md#ebs-snapshot-delete-removes-only-exclusive-data) by that snapshot. <!-- trap: ebs-trap-delete-old-snapshot-breaks-restore -->

> **Say it:** The short answer is: a snapshot copies changed blocks to Amazon S3. The thing to watch is cached data.

**Stop and answer.** A volume has five daily snapshots. Before the second one, the application rewrote every block. The team deletes the first snapshot. Does the bill drop?

<details>
<summary>Answer</summary>

Yes. Deletion removes [only the data that is referenced exclusively](../facts/ebs.md#ebs-snapshot-delete-removes-only-exclusive-data) by that snapshot, and no newer snapshot uses its blocks.

</details>

### A restored volume can start in any zone but reads slowly at first (4 min)

A restored database volume is ready to attach, but the first queries are slow.

1. **Pick any zone.** You can [restore volumes in any Availability Zones](../facts/ebs.md#ebs-snapshot-restore-in-any-az-of-region) of the Region.
2. **Wait for the blocks.** The blocks are [downloaded from Amazon S3 to the new volume](../facts/ebs.md#ebs-volume-initialization-from-snapshot). Until then, the volume can show [increased I/O latency and decreased performance](../facts/ebs.md#ebs-volume-initialization-from-snapshot).
3. **Or skip the wait.** With fast snapshot restore, a volume is [fully initialized at creation](../facts/ebs.md#ebs-fsr-volume-fully-initialized-at-creation). An initialization rate makes it [fully performant in a predictable amount of time](../facts/ebs.md#ebs-volume-initialization-rate-range).
4. **Or read every block yourself.** On Linux, you [read all of the blocks on the device](../facts/ebs.md#ebs-manual-initialization-read-all-blocks) with dd or fio.

> **Exam signal:** "restore volumes at full performance immediately" points to fast snapshot restore, to [avoid the initial performance hit during initialization](../facts/ebs.md#ebs-faq-fsr-when-to-use).

> **Exam trap:** Many think that a restored volume is fast at once. Until initialization ends, it can show [increased I/O latency and decreased performance](../facts/ebs.md#ebs-volume-initialization-from-snapshot). <!-- trap: ebs-trap-restored-volume-full-speed -->

> **Try it:** Snapshot a volume and restore it in another zone. See [3-do.md](3-do.md). <!-- task: ebs-t03 -->

> **Say it:** The short answer is: restore the snapshot into any zone you need. The thing to watch is the slow start.

**Stop and answer.** Ten test volumes come from one 20 GiB snapshot every morning, and the first test run is slow. Name a managed fix and a low-cost fix.

<details>
<summary>Answer</summary>

Managed: fast snapshot restore on that snapshot in that zone, where a full bucket covers [up to 10 initialized volumes](../facts/ebs.md#ebs-faq-fsr-up-to-10-volumes) for a snapshot this small. Low-cost: [read all of the blocks on the device](../facts/ebs.md#ebs-manual-initialization-read-all-blocks) with dd or fio.

</details>

### Copying or sharing a snapshot puts the backup in another Region or account (3 min)

A snapshot survives the loss of a zone. Against the loss of a Region, or [your account being compromised](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account), you copy it out.

1. **Copy across Regions.** [Snapshots are constrained to the Region](../facts/ebs.md#ebs-snapshot-regional-copy-before-sharing), but you can [copy snapshots from one Region to another](../facts/ebs.md#ebs-snapshot-copy-cross-region-and-encrypt).
2. **Share with accounts.** You share a snapshot [privately with individual AWS accounts](../facts/ebs.md#ebs-snapshot-share-public-or-specific-accounts) or publicly.
3. **Share the key too.** For an encrypted snapshot, [you must also share the customer managed key](../facts/ebs.md#ebs-snapshot-share-encrypted-share-cmk-too).
4. **Block public sharing.** Block public access for snapshots [is a Regional setting](../facts/ebs.md#ebs-snapshot-bpa-regional-account-setting) that blocks [any attempt to publicly share snapshots](../facts/ebs.md#ebs-snapshot-bpa-blocks-public-sharing-in-region).

- **Wrong belief:** A zone failure needs a snapshot copy in another Region. **Truth:** You can [restore volumes in any Availability Zones](../facts/ebs.md#ebs-snapshot-restore-in-any-az-of-region) of the same Region. <!-- trap: ebs-trap-zone-loss-needs-second-region -->

<!-- table: plain -->
| Snapshot | Share with an account | Share publicly |
|---|---|---|
| Unencrypted | Yes | Yes, unless block public access has it [automatically blocked](../facts/ebs.md#ebs-snapshot-bpa-blocks-public-sharing-in-region) |
| Encrypted, customer managed key | Yes, and [you must also share the customer managed key](../facts/ebs.md#ebs-snapshot-share-encrypted-share-cmk-too) | No: [Public snapshots of encrypted volumes are not supported](../facts/ebs.md#ebs-snapshot-only-unencrypted-public) |
| Encrypted, **AWS managed key** | No: only [encrypted with a customer managed key](../facts/ebs.md#ebs-snapshot-aws-managed-key-not-shareable) | No |

Why the key rule? The other account has to decrypt the data.

> **Exam signal:** "disaster recovery in another Region" points to a cross-Region snapshot copy.

> **Exam trap:** Many think that any encrypted snapshot can go to a partner account. Of the encrypted snapshots, only those [encrypted with a customer managed key](../facts/ebs.md#ebs-snapshot-aws-managed-key-not-shareable) can be shared. <!-- trap: ebs-trap-share-snapshot-with-aws-managed-key -->

> **Say it:** The short answer is: copy the snapshot out of the Region and the account. The thing to watch is the key.

**Stop and answer.** A team copies a snapshot to US West (Oregon) every night. Why is the first transfer much larger?

<details>
<summary>Answer</summary>

For the first copy to a new Region, [a full (non-incremental) copy is created](../facts/ebs.md#ebs-snapshot-copy-new-region-full-copy).

</details>

### EBS encryption covers the volume its snapshots and the path to the instance (4 min)
<!-- section: route=pass -->

A customer asks whether all their volumes and backups are encrypted.

1. **Choose the key.** EBS uses an AWS Key Management Service (AWS KMS) key: by default [aws/ebs](../facts/ebs.md#ebs-encryption-aws-managed-key-alias-per-region), or [a symmetric customer managed encryption key](../facts/ebs.md#ebs-encryption-aws-managed-key-alias-per-region).
2. **Encrypt on the host.** Host encryption protects [data-at-rest and data-in-transit](../facts/ebs.md#ebs-encryption-on-host-covers-in-transit) between instance and volume.
3. **Let it flow to copies.** [Snapshots of encrypted EBS volumes are automatically encrypted](../facts/ebs.md#ebs-encryption-propagates-to-snapshots-and-volumes).

- **Wrong belief:** Encryption by default is one setting for the whole account. **Truth:** It is [a Region-specific setting](../facts/ebs.md#ebs-encryption-by-default-region-setting): turn it on in each Region that you use. <!-- trap: ebs-trap-encryption-by-default-account-wide -->

<!-- table: plain -->
| You want | Path |
|---|---|
| Encrypt an existing volume | Snapshot, [create an encrypted copy of that snapshot](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot), new volume |
| Remove encryption | Not possible: [you cannot remove encryption](../facts/ebs.md#ebs-encryption-cannot-be-removed) |

Why on the host? The data is encrypted before it travels to the volume, with [the same IOPS performance on encrypted volumes](../facts/ebs.md#ebs-encryption-same-iops-minimal-latency).

> **Exam signal:** "ensure that all new EBS volumes are encrypted" points to the Region setting, which [has no effect on existing EBS volumes](../facts/ebs.md#ebs-encryption-by-default-new-resources-only).

> **Say it:** The short answer is: encrypt with a KMS key, and snapshots inherit it. The thing to watch is old volumes.

**Stop and answer.** Encryption by default is on. A developer restores a volume from an old unencrypted snapshot. Is the new volume encrypted?

<details>
<summary>Answer</summary>

Yes: [encryption is mandatory for volumes restored](../facts/ebs.md#ebs-encrypted-snapshot-restore-default-key) from unencrypted snapshots.

</details>

### Data Lifecycle Manager and AWS Backup take snapshots on a schedule (4 min)

People forget backups that they take by hand.

1. **Write a policy.** Amazon Data Lifecycle Manager automates the [creation, retention, and deletion of EBS snapshots](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis), [at no additional cost](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis).
2. **Copy away.** A schedule can copy snapshots to [up to three additional Regions or Outposts](../facts/ebs.md#ebs-dlm-cross-region-copy-three-regions).
3. **Archive what you keep long.** The snapshot archive tier gives [up to 75 percent lower snapshot storage costs](../facts/ebs.md#ebs-archive-75-percent-lower-cost). A restore from it can take [up to 72 hours](../facts/ebs.md#ebs-archive-restore-up-to-72-hours).

<!-- table: plain -->
| Question | Data Lifecycle Manager | AWS Backup |
|---|---|---|
| Protects | EBS snapshots and EBS-backed AMIs | [supports many AWS services](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts) |
| Policy scope | Your account; it can copy to [specific Regions in an isolated account](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account) | [apply it across accounts and Regions](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts) |
| Immutable backups | Snapshot lock, next subsection | [Vault Lock enforces immutability](../facts/ebs.md#ebs-aws-backup-air-gapped-vault-lock) |

**Deciding question:** Only EBS snapshots and AMIs, or one policy for many services and accounts?

> **Exam signal:** "automate the creation, retention and deletion of EBS snapshots" points to Data Lifecycle Manager.

> **Exam trap:** Many think that the archive tier lowers the cost of every snapshot. AWS recommends it for [monthly, quarterly, or yearly snapshots](../facts/ebs.md#ebs-archive-recommended-monthly-not-daily). An archived snapshot is [converted to a full snapshot](../facts/ebs.md#ebs-archive-full-snapshot), so archiving daily snapshots [can lead to higher costs](../facts/ebs.md#ebs-archive-recommended-monthly-not-daily). <!-- trap: ebs-trap-archive-daily-snapshots -->

> **Say it:** The short answer is: a policy takes and deletes snapshots for you. The thing to watch is scope across accounts.

**Stop and answer.** A company keeps daily snapshots for 30 days and monthly snapshots for seven years. Which ones should go to the archive tier?

<details>
<summary>Answer</summary>

The monthly ones. Archiving the daily ones [can lead to higher costs](../facts/ebs.md#ebs-archive-recommended-monthly-not-daily) than keeping them in the standard tier.

</details>

### Recycle Bin and snapshot lock stop snapshots from being deleted too early (3 min)

An engineer deletes the wrong snapshot, or an attacker deletes all of them.

1. **Catch deletions.** Recycle Bin restores deleted [EBS volumes, EBS snapshots, and EBS-backed AMIs](../facts/ebs.md#ebs-recycle-bin-recovers-volumes-snapshots-amis).
2. **Write a rule in each Region.** [You must create retention rules](../facts/ebs.md#ebs-recycle-bin-needs-regional-retention-rules) in each Region that needs protection.
3. **Lock the important ones.** No user can delete a locked snapshot, [regardless of their IAM permissions](../facts/ebs.md#ebs-snapshot-lock-no-user-can-delete).
4. **Use compliance mode against everyone.** An optional **cooling-off period** of [from 1 to 72 hours](../facts/ebs.md#ebs-snapshot-lock-cooling-off-range) can come first; without one, compliance mode starts at once. After it, [you must wait for the lock to expire](../facts/ebs.md#ebs-snapshot-lock-compliance-mode).

- **Wrong belief:** A lock in governance mode stops every user. **Truth:** In governance mode, [users with appropriate IAM permissions can unlock](../facts/ebs.md#ebs-snapshot-lock-governance-mode) the snapshot. <!-- trap: ebs-trap-governance-lock-stops-admins -->
- **Wrong belief:** A Recycle Bin rule stops a delete. **Truth:** The delete happens, and the snapshot is [retained in the Recycle Bin](../facts/ebs.md#ebs-snapshot-delete-retained-by-recycle-bin-rule) for recovery. <!-- trap: ebs-trap-recycle-bin-prevents-deletion -->

<!-- table: plain -->
| Question | Recycle Bin | Snapshot lock |
|---|---|---|
| When it acts | After a delete | Before a delete |
| Cost | [billed at the same rate as regular snapshots](../facts/ebs.md#ebs-recycle-bin-billed-same-rate) | Lock [at no additional cost](../facts/ebs.md#ebs-snapshot-lock-no-additional-cost) |

> **Exam signal:** "recover accidentally deleted EBS snapshots" points to Recycle Bin. "no user, administrators included, can delete the backups" points to snapshot lock in compliance mode.

> **Say it:** The short answer is: Recycle Bin undoes a deletion, and a lock prevents it. The thing to watch is the rule in each Region.

**Stop and answer.** A snapshot in US West (Oregon) has a governance-mode lock. The only Recycle Bin rule is in US East (N. Virginia). An administrator unlocks and deletes the snapshot. Can the team get it back?

<details>
<summary>Answer</summary>

No. In governance mode, [users with appropriate IAM permissions can unlock](../facts/ebs.md#ebs-snapshot-lock-governance-mode) it, and [you must create retention rules](../facts/ebs.md#ebs-recycle-bin-needs-regional-retention-rules) in each Region.

</details>

