---
id: "22"
slug: ebs
title: EBS and instance store
file: fast
tier: deep
domains: [1, 2, 3, 4]
tasks: ["3.1", "4.1", "2.2", "1.3"]
services: [ebs, instance-store]
minutes: {fast: 20, pass: 74, full: 168}
status: ready
updated: 2026-10-13
---

# EBS and instance store

## Predict (1 min)
<!-- section: role=predict; route=fast; minutes=1 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** AWS automatically replicates every EBS **volume** inside its **Availability Zone**. Does AWS also keep a backup that you can restore after a mistake? <!-- gist-trap -->

**Predict 2.** An **instance** with an **instance store** volume is stopped at night and started in the morning. Is the data on the instance store still there?

**Predict 3.** A volume is much larger than its data. Can you make the same volume smaller to save money?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

In AWS CloudShell, read three **Region** settings: encryption by default, its key, and **block public access** for snapshots. Then find which of two instance types has instance store, without creating anything.

<!-- task:start id=ebs-t01 -->

Look

**It kills the belief.** "Every new EBS volume is encrypted automatically."

> **Cost:** $0.

**Permissions.** `ec2:GetEbsEncryptionByDefault`, `ec2:GetEbsDefaultKmsKeyId`, `ec2:GetSnapshotBlockPublicAccessState`, `ec2:DescribeInstanceTypes`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read whether EBS encryption by default is turned on in this Region.

   ```bash
   aws ec2 get-ebs-encryption-by-default
   ```

   Expect: EbsEncryptionByDefault with true or false. The value is for this Region only. If it shows true, every new volume that you create in this Region is encrypted while the setting stays on. If it shows false, this Region does not enforce encryption, so check the Encrypted field of each new volume.

2. Read the KMS key that EBS encryption uses by default in this Region.

   ```bash
   aws ec2 get-ebs-default-kms-key-id
   ```

   Expect: KmsKeyId with alias/aws/ebs, the AWS managed key that EBS creates in each Region. If someone in your account chose a customer managed key, you see the ARN of that key instead.

3. Read the state of block public access for snapshots in this Region.

   ```bash
   aws ec2 get-snapshot-block-public-access-state
   ```

   Expect: State with block-all-sharing, block-new-sharing or unblocked. ManagedBy can also show: account, or declarative-policy when a policy of your organization sets the state. Like encryption by default, the setting is for this Region only.

4. Compare two instance types whose names differ by one letter, m5.large and m5d.large. Read whether each type has instance store, and its total size in GB.

   ```bash
   aws ec2 describe-instance-types --instance-types m5.large m5d.large --query "InstanceTypes[].[InstanceType,InstanceStorageSupported,InstanceStorageInfo.TotalSizeInGB]" --output table
   ```

   Expect: Two rows, in any order. m5.large shows False and no size (the table can show None). m5d.large shows True and a size in GB: the letter d means instance store volumes. If AWS says that a type is not offered in this Region, use c5.large and c5d.large.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** An EBS volume is a [durable, block-level storage device](../facts/ebs.md#ebs-volume-block-storage-device-like-hard-drive) that can [persist independently from the running life](../facts/ebs.md#ebs-volume-persists-independently-of-instance) of instances. Instance store is [temporary block-level storage](../facts/instance-store.md#instance-store-physically-attached-host-disks).

**The problem it solves.** A database needs storage that outlives the instance, and it needs a backup. Scratch files need fast storage that can disappear with the instance.

**Predict the picture.** When an instance writes to an EBS volume, where does the data go, and where does its backup go?

<details>
<summary>Show the picture</summary>

![A sequence with three participants: an EC2 instance, an EBS volume and Amazon S3. The instance writes blocks to the volume in its zone, EBS copies the volume inside that zone, a snapshot sends the changed blocks to Amazon S3, and a new volume is restored from it in another zone.](../diagrams/svg/ebs-hero.svg)

**Figure.** A volume serves its own Availability Zone, and its snapshots in Amazon S3 can rebuild it anywhere in the Region.

1. The instance writes a block to its EBS volume, which is [off-instance storage](../facts/ebs.md#ebs-volume-persists-independently-of-instance).
2. The volume and the instance [must be in the same Availability Zone](../facts/ebs.md#ebs-volume-same-az-as-instance).
3. The volume is [automatically replicated within its Availability Zone](../facts/ebs.md#ebs-volume-replicated-within-az).
4. A snapshot copies the [blocks on the volume that have changed](../facts/ebs.md#ebs-snapshot-incremental-changed-blocks) to Amazon S3.
5. The snapshot is [stored redundantly in multiple Availability Zones](../facts/ebs.md#ebs-snapshot-stored-in-s3-multiple-azs).
6. From the snapshot, you can [restore volumes in any Availability Zones](../facts/ebs.md#ebs-snapshot-restore-in-any-az-of-region) of the Region.

</details>

> **Startup example:** One volume holds the operating system, the database and temporary audio files. The volume filled up and the database stopped for 3 hours. The newest backup was 9 days old. Callvale must lose at most 24 hours of data and must recover within 8 hours.

## Words that go together (1 min)
<!-- section: role=words; route=fast; minutes=1 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| volume (VOL-yoom) | **attach** a volume to an instance | Block storage that you attach to an instance | instance store |
| snapshot | **restore** from a snapshot | A point-in-time copy of a volume | **Amazon Machine Image** (AMI) |
| instance store | an instance store **volume** | Temporary block storage on the host computer | EBS volume |
| ephemeral (ih-FEM-er-ul) | ephemeral **storage** | Temporary: the data disappears when the instance stops or ends | persistent |
| IOPS (EYE-ops) | **provision** IOPS | Read and write operations each second | throughput |
| throughput (THROO-put) | **high** throughput | The amount of data that moves each second | IOPS |
| latency (LAY-ten-see) | **low** latency | The time between a request and its response | throughput |
| durability (dyoor-uh-BIL-ih-tee) | **designed** for durability | How unlikely it is that stored data is lost | availability |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### EBS volume or instance store

<!-- table: compare -->
| Question | EBS volume | Instance store |
|---|---|---|
| Where does it live? | [off-instance storage](../facts/ebs.md#ebs-volume-persists-independently-of-instance) in the zone of its instance | Disks [physically attached to the host computer](../facts/instance-store.md#instance-store-physically-attached-host-disks) |
| What happens after a stop? | Kept: it [remains attached throughout the stop-start cycle](../facts/ebs.md#ebs-volume-stays-attached-through-stop-start) | Erased: the [data on any instance store volumes is erased](../facts/instance-store.md#instance-store-data-erased-on-stop) |
| How fast is it? | Set by the volume type and the instance | SSD types give [high random I/O performance with very low latency](../facts/instance-store.md#instance-store-ssd-high-random-io) |
| How is it billed? | [charged by the amount of GB](../facts/ebs.md#ebs-billed-provisioned-gb-month) that you provision | [There is no additional charge](../facts/instance-store.md#instance-store-no-additional-charge) beyond the instance |
| What does it fit? | Databases, boot volumes and data that you keep | [buffers, caches, scratch data](../facts/instance-store.md#instance-store-ideal-for-temporary-data) |

**Deciding question:** Must the data survive a stop, a termination or a disk failure?

### gp3 or io2 Block Express or an HDD type

gp3 and io2 Block Express are solid state drive (SSD) types. st1 and sc1 are hard disk drive (HDD) types.

<!-- table: compare -->
| Question | gp3 | io2 Block Express | st1 and sc1 |
|---|---|---|---|
| Which input/output (I/O) pattern? | Small and random | Small and random, with [consistent sub-millisecond latency](../facts/ebs.md#ebs-io2-use-cases) | [large, sequential I/O](../facts/ebs.md#ebs-hdd-large-sequential-not-small-random) |
| How does performance grow? | IOPS and throughput set [independently of volume size](../facts/ebs.md#ebs-gp3-performance-independent-of-size), within [500 IOPS per GiB](../facts/ebs.md#ebs-gp3-max-iops-80000) | Provisioned IOPS [up to 256,000](../facts/ebs.md#ebs-io2-max-iops-ratio) on Nitro-based instances | Throughput [scales linearly with volume size](../facts/ebs.md#ebs-faq-st1-sc1-scale-with-size) |
| Volume durability? | [99.8 percent to 99.9 percent](../facts/ebs.md#ebs-gp3-durability-afr) | [99.999 percent volume durability](../facts/ebs.md#ebs-io2-durability-afr) | Not the deciding question for HDD |
| Boot volume? | Yes: AWS lists [boot volumes](../facts/ebs.md#ebs-gp3-use-cases) | Yes: SSD types serve [transactional, IOPS-intensive database workloads, boot volumes](../facts/ebs.md#ebs-faq-ssd-workloads) | No: [bootable st1 volumes are not supported](../facts/ebs.md#ebs-hdd-volumes-not-bootable), nor sc1 |
| What does it fit? | [medium sized single instance databases](../facts/ebs.md#ebs-gp3-use-cases) | [I/O-intensive NoSQL & relational databases](../facts/ebs.md#ebs-io2-use-cases) | st1: [big data, data warehouses, log processing](../facts/ebs.md#ebs-st1-use-cases); sc1: cold data |

**Deciding question:** Is the I/O small and random or large and sequential, and does gp3 already cover the IOPS, latency and durability?

### Amazon EBS or Amazon EFS or Amazon S3

<!-- table: compare -->
| Question | Amazon EBS | Amazon EFS | Amazon S3 |
|---|---|---|---|
| What storage type? | A [block-level storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object) | A [file storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object) | An [object storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object) |
| Who uses it? | Storage [attached to single Amazon EC2 instances or containers](../facts/ebs.md#ebs-decision-guide-block-storage-single-instance) | Many instances, [within and across multiple Availability Zones](../facts/ebs.md#ebs-vs-efs-az-scope-and-sharing) | Applications that store and read objects |
| What does it fit? | Databases and boot volumes | [shared read and write access across multiple Amazon EC2 instances](../facts/ebs.md#ebs-decision-guide-file-storage-shared-access) | Objects such as call recordings |

**Deciding question:** Does one instance need a volume, do many instances need shared files, or does an application store objects?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "temporary data, cache, scratch space, lowest latency" | instance store | [buffers, caches, scratch data](../facts/instance-store.md#instance-store-ideal-for-temporary-data), with [high random I/O performance with very low latency](../facts/instance-store.md#instance-store-ssd-high-random-io) | the data must survive a stop: an EBS volume |
| "boot volume, dev and test, cost-effective" | gp3 | a [balance between cost and performance](../facts/ebs.md#ebs-faq-gp3-suited-workloads) | "sub-millisecond latency", "higher durability" or more than [80,000](../facts/ebs.md#ebs-gp3-max-iops-80000) IOPS: io2 Block Express |
| "sub-millisecond latency, I/O-intensive database" | io2 Block Express | [consistent sub-millisecond latency](../facts/ebs.md#ebs-io2-use-cases) | no latency or durability need, and "cost-effective": gp3 |
| "big data, log processing, sequential" | st1 | [big data, data warehouses, log processing](../facts/ebs.md#ebs-st1-use-cases) | rare scans at the lowest cost: sc1 |
| "several instances write one block volume" | io2 with Multi-Attach and a clustered file system | you can [attach a single Provisioned IOPS SSD](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az) volume to many instances | "standard file operations" or several Availability Zones: Amazon EFS |
| "all new EBS volumes must be encrypted" | encryption by default | a [single setting per region](../facts/ebs.md#ebs-faq-encryption-by-default-per-region) | existing volumes: snapshot, encrypted copy, new volume |
| "automate snapshot creation and retention" | Amazon Data Lifecycle Manager | automates the [creation, retention, and deletion of EBS snapshots](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis) | one policy across services and accounts: AWS Backup |
| "full performance right after a restore" | fast snapshot restore | helps [avoid the initial performance hit during initialization](../facts/ebs.md#ebs-faq-fsr-when-to-use) | a low-cost warm-up is enough: read every block with dd or fio |

### Traps

- **Wrong belief:** EBS replicates every volume, so AWS already keeps a backup. **Truth:** Replication protects against the [failure of any single hardware component](../facts/ebs.md#ebs-volume-replicated-within-az). AWS [does not automatically back up the data](../facts/ebs.md#ebs-no-automatic-backup-customer-creates-snapshots). <!-- trap: ebs-trap-aws-backs-up-ebs -->
- **Wrong belief:** Instance store is fast and free, so it fits a database. **Truth:** Use it [only for temporary data](../facts/instance-store.md#instance-store-faq-only-temporary-data). Data is lost when the instance is [stopped, hibernated, or terminated](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop), or when [the underlying disk fails](../facts/instance-store.md#instance-store-data-lost-when-disk-fails). <!-- trap: ebs-trap-instance-store-for-durable-data -->
- **Wrong belief:** EBS volumes persist, so the root volume stays after termination. **Truth:** By default, the root volume is [deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-root-default-true). Other volumes created at launch [are not deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-additional-default-false). <!-- trap: ebs-trap-terminate-keeps-root-volume -->
- **Wrong belief:** st1 or sc1 is a cheaper choice for a database or a boot volume. **Truth:** HDD types favor [sequential I/Os and large I/O sizes](../facts/ebs.md#ebs-faq-hdd-not-for-random-small-io), not the small, random I/O of a database. [Bootable st1 volumes are not supported](../facts/ebs.md#ebs-hdd-volumes-not-bootable), and sc1 is the same. <!-- trap: ebs-trap-hdd-for-database-or-boot -->
- **Wrong belief:** You can turn on encryption for an existing volume. **Truth:** You cannot encrypt it in place: take a snapshot and [create a new encrypted volume](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot). Encryption by default [has no effect on existing EBS volumes](../facts/ebs.md#ebs-encryption-by-default-new-resources-only). <!-- trap: ebs-trap-encrypt-volume-in-place -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-09-26) Larger gp3 volumes with more IOPS and throughput.<br>
> **Old:** [16 TiB](../facts/ebs.md#ebs-change-gp3-limits-2025-09), [16,000 IOPS](../facts/ebs.md#ebs-change-gp3-limits-2025-09) and [1,000 MiB/s](../facts/ebs.md#ebs-change-gp3-limits-2025-09) per volume.<br>
> **Now:** [64 TiB](../facts/ebs.md#ebs-change-gp3-limits-2025-09), [80,000 IOPS](../facts/ebs.md#ebs-change-gp3-limits-2025-09) and [2,000 MiB/s](../facts/ebs.md#ebs-change-gp3-limits-2025-09) per volume.<br>
> **The exam probably expects:** older questions choose io2 above [16,000 IOPS](../facts/ebs.md#ebs-change-gp3-limits-2025-09). Prefer an option that is right under both values.<br>
> **Status:** examinable.

> **Changed recently:** (2025-11-20) Recycle Bin also protects EBS volumes.<br>
> **Old:** Recycle Bin covered [snapshots and EBS-backed AMIs](../facts/ebs.md#ebs-change-recycle-bin-volumes-2025-11).<br>
> **Now:** from [November 20, 2025](../facts/ebs.md#ebs-change-recycle-bin-volumes-2025-11), Recycle Bin can also [protect Amazon EBS volumes against accidental deletions](../facts/ebs.md#ebs-change-recycle-bin-volumes-2025-11).<br>
> **The exam probably expects:** older questions say Recycle Bin covers only snapshots and AMIs.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** An engineer drops a table by mistake. Can the replicated EBS volume give the table back without a snapshot?

<details>
<summary>Answer</summary>

No. Replication protects against the [failure of any single hardware component](../facts/ebs.md#ebs-volume-replicated-within-az), and AWS [does not automatically back up the data](../facts/ebs.md#ebs-no-automatic-backup-customer-creates-snapshots).

**Predict 1:** No: snapshots are your job.

</details>

**Check 2.** A worker keeps a cache on instance store. The instance is rebooted after a patch. Is the cache still there?

<details>
<summary>Answer</summary>

Yes. The data [persists even if the instance is rebooted](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop).

**Predict 2:** No. After a stop, the [data on any instance store volumes is erased](../facts/instance-store.md#instance-store-data-erased-on-stop).

</details>

**Check 3.** A team changes a gp2 volume to gp3 and adds IOPS during database traffic. Must it stop the instance?

<details>
<summary>Answer</summary>

No. On an instance that supports Elastic Volumes, the change works [without detaching the volume or restarting the instance](../facts/ebs.md#ebs-elastic-volumes-modify-without-detach).

**Predict 3:** No. You cannot shrink a volume: [create a smaller volume](../facts/ebs.md#ebs-volume-size-cannot-decrease) and copy the data.

</details>

## Recap from memory (2 min)
<!-- section: role=recap; route=fast; minutes=2 -->

**Recap 1.** What happens to an EBS volume and to instance store after a stop?

<details>
<summary>Answer</summary>

The EBS volume [remains attached throughout the stop-start cycle](../facts/ebs.md#ebs-volume-stays-attached-through-stop-start). The [data on any instance store volumes is erased](../facts/instance-store.md#instance-store-data-erased-on-stop).

</details>

**Recap 2.** Which volume type fits "big data, log processing"?

<details>
<summary>Answer</summary>

st1.

</details>

**Recap 3.** How do you encrypt an existing unencrypted volume?

<details>
<summary>Answer</summary>

Take a snapshot and [create a new encrypted volume](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot) from it.

</details>
