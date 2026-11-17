facts card: 413 facts
ebs-ami-creation-snapshots-each-ebs-volume
  claim: Creating an EBS-backed AMI makes snapshots of the instance's root volume and its other attached EBS volumes, and you are charged for those snapshots until you deregister the AMI and delete the snapshots.
  scope: EBS-backed AMIs.
  link: [creates snapshots of your instance's root volume](../facts/ebs.md#ebs-ami-creation-snapshots-each-ebs-volume)
  link: [charged for the snapshots until you deregister](../facts/ebs.md#ebs-ami-creation-snapshots-each-ebs-volume)
ebs-ami-deregister-keeps-snapshots-by-default
  claim: By default, deregistering an AMI has no effect on the snapshots created with it, which keep incurring storage costs; you can optionally delete the associated snapshots during deregistration, except a snapshot that other AMIs also use.
  scope: AMI deregistration; default; adjustable; snapshot deletion can be requested at deregistration.
  link: [also has no effect on any snapshots](../facts/ebs.md#ebs-ami-deregister-keeps-snapshots-by-default)
  link: [optionally delete its associated snapshots](../facts/ebs.md#ebs-ami-deregister-keeps-snapshots-by-default)
  link: [it won't be deleted even if specified](../facts/ebs.md#ebs-ami-deregister-keeps-snapshots-by-default)
ebs-app-consistent-windows-vss-ssm
  claim: You can take application-consistent snapshots of all EBS volumes attached to a Windows instance by using AWS Systems Manager command documents (VSS).
  scope: EC2 Windows instances.
  link: [AWS Systems Manager command documents](../facts/ebs.md#ebs-app-consistent-windows-vss-ssm)
  link: [application-consistent snapshots](../facts/ebs.md#ebs-app-consistent-windows-vss-ssm)
ebs-archive-75-percent-lower-cost
  claim: EBS Snapshots Archive offers up to 75 percent lower snapshot storage costs for snapshots you plan to store for 90 days or longer and rarely need to access.
  scope: per archived snapshot, compared with the standard tier; maximum; snapshots kept 90 days or longer and rarely accessed.
  link: [up to 75 percent lower snapshot storage costs](../facts/ebs.md#ebs-archive-75-percent-lower-cost)
  link: [90 days or longer](../facts/ebs.md#ebs-archive-75-percent-lower-cost)
  say: up to seventy-five percent lower snapshot storage costs | ninety days or longer
ebs-archive-full-snapshot
  claim: When you archive a snapshot, the incremental snapshot is converted to a full snapshot and moved from the standard tier to the archive tier.
  scope: per archived snapshot.
  link: [converted to a full snapshot](../facts/ebs.md#ebs-archive-full-snapshot)
  say: converted to a full snapshot
ebs-archive-min-period-90-days
  claim: The minimum archive period is 90 days; if you delete or permanently restore an archived snapshot earlier, you are billed for the remaining days in the archive tier, rounded to the nearest hour.
  scope: per archived snapshot; minimum; not adjustable; applies when you delete or permanently restore the snapshot before 90 days.
  link: [minimum archive period is 90 days](../facts/ebs.md#ebs-archive-min-period-90-days)
  say: minimum archive period is ninety days
ebs-archive-recommended-monthly-not-daily
  claim: AWS recommends the snapshot archive tier for monthly, quarterly or yearly snapshots; archiving the daily incremental snapshots of one volume can cost more than keeping them in the standard tier.
  scope: EBS Snapshots Archive tier.
  link: [monthly, quarterly, or yearly snapshots](../facts/ebs.md#ebs-archive-recommended-monthly-not-daily)
  link: [can lead to higher costs](../facts/ebs.md#ebs-archive-recommended-monthly-not-daily)
ebs-archive-restore-price
  claim: Restoring a snapshot from the archive tier is billed at $0.03 per GB of data restored, as a one-time charge.
  scope: per GB restored; example rate in the EBS guide.
  link: [$0.03 per GB of data restored](../facts/ebs.md#ebs-archive-restore-price)
  say: three cents per GB of data restored
ebs-archive-restore-up-to-72-hours
  claim: Restoring an archived snapshot from the archive tier to the standard tier can take up to 72 hours, depending on the size of the snapshot.
  scope: per archived snapshot restore; maximum; not adjustable; depends on snapshot size.
  link: [up to 72 hours](../facts/ebs.md#ebs-archive-restore-up-to-72-hours)
  say: up to seventy-two hours
ebs-archive-storage-price
  claim: Archived snapshots are billed at $0.0125 per GB-month; for example, a 100 GiB archived snapshot costs $1.25 per month.
  scope: per GB-month of archived snapshot; example rate in the EBS guide; check the pricing page for the Region.
  link: [$0.0125 per GB-month](../facts/ebs.md#ebs-archive-storage-price)
  say: one and a quarter cents per GB-month
ebs-archive-temporary-restore-no-early-charge
  claim: Temporarily restoring an archived snapshot before the minimum archive period of 90 days does not incur the early deletion charge.
  scope: per archived snapshot; temporary restore only.
  link: [does not incur this charge](../facts/ebs.md#ebs-archive-temporary-restore-no-early-charge)
  say: does not incur this charge
ebs-aws-backup-air-gapped-vault-lock
  claim: AWS Backup adds security and compliance for snapshots: logically air-gapped vaults isolate recovery points from production, and Vault Lock enforces immutability.
  scope: AWS Backup recovery points for EBS snapshots.
  link: [Logically air-gapped vaults](../facts/ebs.md#ebs-aws-backup-air-gapped-vault-lock)
  link: [Vault Lock enforces immutability](../facts/ebs.md#ebs-aws-backup-air-gapped-vault-lock)
ebs-aws-backup-central-policy-across-accounts
  claim: AWS Backup centralizes data protection: you define one backup policy and apply it across accounts and Regions, and it covers many services, including EBS, EC2, S3, EFS, RDS and Aurora.
  scope: AWS Backup policies.
  link: [apply it across accounts and Regions](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts)
  link: [supports many AWS services](../facts/ebs.md#ebs-aws-backup-central-policy-across-accounts)
ebs-aws-backup-multi-volume-crash-consistent
  claim: For EBS, AWS Backup takes crash-consistent, multi-volume snapshots that coordinate point-in-time backups of all volumes attached to an EC2 instance.
  scope: per EC2 instance.
  link: [crash-consistent, multi-volume snapshots](../facts/ebs.md#ebs-aws-backup-multi-volume-crash-consistent)
ebs-benefits-not-provided-by-instance-store
  claim: EBS volumes provide benefits that instance store volumes do not provide.
  scope: EBS versus instance store.
  link: [EBS volumes provide benefits](../facts/ebs.md#ebs-benefits-not-provided-by-instance-store)
  link: [not provided by instance store volumes](../facts/ebs.md#ebs-benefits-not-provided-by-instance-store)
ebs-billed-provisioned-gb-month
  claim: With EBS you pay for what you provision: volume storage for every volume type is charged by the GB provisioned per month until you release the storage, and IOPS and throughput beyond the baseline cost more.
  scope: per EBS volume; until the storage is released.
  link: [you pay only for what you provision](../facts/ebs.md#ebs-billed-provisioned-gb-month)
  link: [charged by the amount of GB](../facts/ebs.md#ebs-billed-provisioned-gb-month)
  say: you pay only for what you provision | charged by the GB you provision per month
ebs-billing-per-second-60-second-minimum
  claim: Provisioned storage, IOPS and throughput for gp3 volumes are billed in per-second increments with a 60-second minimum.
  scope: per gp3 volume; minimum.
  link: [per-second increments, with a 60-second minimum](../facts/ebs.md#ebs-billing-per-second-60-second-minimum)
  say: per-second increments with a sixty-second minimum
ebs-case-games24x7-aws-backup-rpo-rto
  claim: Games24x7 set up automated backups of its S3 and EBS data with AWS Backup and, in testing, reached an RPO of 1 hour and an RTO of 30 minutes for a 5 TB database; it kept costs down with incremental EBS snapshots.
  scope: Games24x7, recovery testing.
  link: [1 hour](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  link: [30 minutes](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  link: [5 TB](../facts/ebs.md#ebs-case-games24x7-aws-backup-rpo-rto)
  say: one hour | thirty minutes | five terabytes
ebs-case-ginkgo-smaller-volumes
  claim: Ginkgo Bioworks saved up to 90 percent of its Amazon EBS costs by reducing the size of the volumes it uses.
  scope: Ginkgo Bioworks.
  link: [up to 90 percent](../facts/ebs.md#ebs-case-ginkgo-smaller-volumes)
  link: [by reducing the size of the volumes](../facts/ebs.md#ebs-case-ginkgo-smaller-volumes)
  say: up to ninety percent
ebs-case-marqeta-io2-block-express
  claim: Marqeta began to migrate its most critical MySQL databases to EBS io2 Block Express volumes, whose specifications of 256K IOPS and 64TB met Marqeta's performance and capacity requirements.
  scope: Marqeta, MySQL databases.
  link: [256K IOPS](../facts/ebs.md#ebs-case-marqeta-io2-block-express)
  link: [64TB](../facts/ebs.md#ebs-case-marqeta-io2-block-express)
  say: two hundred fifty-six thousand IOPS | sixty-four terabytes
ebs-case-teradata-multi-attach-recovery
  claim: Teradata uses NVMe reservations with Multi-Attach on io2 Block Express volumes to switch nodes when a problem occurs, cutting outage time from up to 20 minutes to 1 minute, an improvement of 95 percent.
  scope: Teradata VantageCloud.
  link: [up to 20 minutes](../facts/ebs.md#ebs-case-teradata-multi-attach-recovery)
  link: [1 minute](../facts/ebs.md#ebs-case-teradata-multi-attach-recovery)
  link: [95 percent](../facts/ebs.md#ebs-case-teradata-multi-attach-recovery)
  say: up to twenty minutes | one minute | ninety-five percent
ebs-change-dlm-default-policies-2023-11
  claim: On November 16, 2023 Amazon Data Lifecycle Manager added default policies for EBS snapshots and EBS-backed AMIs that back up all volumes and instances in a Region.
  link: [November 16, 2023](../facts/ebs.md#ebs-change-dlm-default-policies-2023-11)
  link: [backup all volumes and instances in a Region](../facts/ebs.md#ebs-change-dlm-default-policies-2023-11)
  say: November sixteenth, twenty twenty-three
ebs-change-dlm-pre-post-scripts-2023-11
  claim: On November 7, 2023 Amazon Data Lifecycle Manager snapshot policies gained pre and post scripts to automate application-consistent snapshots.
  link: [November 7, 2023](../facts/ebs.md#ebs-change-dlm-pre-post-scripts-2023-11)
  link: [pre and post scripts](../facts/ebs.md#ebs-change-dlm-pre-post-scripts-2023-11)
  say: November seventh, twenty twenty-three
ebs-change-elastic-volumes-four-per-24h-2026-01
  claim: On January 15, 2026 Elastic Volumes changed: you can start a new modification as soon as the previous one completes, up to four times within a 24-hour period.
  scope: per volume.
  link: [January 15, 2026](../facts/ebs.md#ebs-change-elastic-volumes-four-per-24h-2026-01)
  link: [up to four times within a 24-hour period](../facts/ebs.md#ebs-change-elastic-volumes-four-per-24h-2026-01)
  say: January fifteenth, twenty twenty-six
ebs-change-gp3-limits-2025-09
  claim: On September 26, 2025 AWS raised the gp3 maximums to 64 TiB, 80,000 IOPS and 2,000 MiB/s per volume. Before that, the limits were 16 TiB, 16,000 IOPS and 1,000 MiB/s.
  scope: per gp3 volume; maximum; outside AWS Outposts.
  link: [September 26, 2025](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [64 TiB](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [80,000 IOPS](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [2,000 MiB/s](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [16,000 IOPS](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [16 TiB](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  link: [1,000 MiB/s](../facts/ebs.md#ebs-change-gp3-limits-2025-09)
  say: September twenty-sixth, twenty twenty-five | sixty-four tebibytes | eighty thousand IOPS | two thousand mebibytes per second | sixteen thousand IOPS | sixteen tebibytes | one thousand mebibytes per second
  changed: 2025-09-26: was the previous 16,000 IOPS limit
ebs-change-io2-all-block-express-2025-04
  claim: As of April 30, 2025, every io2 volume, new or previously created, is an io2 Block Express volume.
  scope: all io2 volumes.
  link: [April 30, 2025](../facts/ebs.md#ebs-change-io2-all-block-express-2025-04)
  link: [io2 Block Express](../facts/ebs.md#ebs-change-io2-all-block-express-2025-04)
  say: April thirtieth, twenty twenty-five
ebs-change-io2-all-regions-2025-07
  claim: On July 22, 2025 io2 volumes became available in all commercial and AWS GovCloud (US) Regions.
  link: [July 22, 2025](../facts/ebs.md#ebs-change-io2-all-regions-2025-07)
  say: July twenty-second, twenty twenty-five
ebs-change-multi-attach-nvme-reservations-2023-09
  claim: On September 18, 2023 Multi-Attach enabled io2 volumes gained support for NVMe reservations, a set of industry-standard storage fencing protocols.
  link: [September 18, 2023](../facts/ebs.md#ebs-change-multi-attach-nvme-reservations-2023-09)
  link: [NVMe reservations](../facts/ebs.md#ebs-change-multi-attach-nvme-reservations-2023-09)
  say: September eighteenth, twenty twenty-three
ebs-change-provisioned-rate-init-2025-05
  claim: On May 6, 2025 EBS added Provisioned Rate for Volume Initialization: you set an initialization rate when you create a volume so that it is fully initialized in a predictable amount of time.
  link: [May 6, 2025](../facts/ebs.md#ebs-change-provisioned-rate-init-2025-05)
  link: [fully initialized in a predictable amount of time](../facts/ebs.md#ebs-change-provisioned-rate-init-2025-05)
  say: May sixth, twenty twenty-five
ebs-change-recycle-bin-volumes-2025-11
  claim: On November 20, 2025 Recycle Bin started to protect EBS volumes against accidental deletion; before, it covered snapshots and EBS-backed AMIs.
  link: [November 20, 2025](../facts/ebs.md#ebs-change-recycle-bin-volumes-2025-11)
  link: [snapshots and EBS-backed AMIs](../facts/ebs.md#ebs-change-recycle-bin-volumes-2025-11)
  say: November twentieth, twenty twenty-five
  changed: 2025-11-20: was snapshots and EBS-backed AMIs
ebs-change-snapshot-bpa-2023-11
  claim: On November 9, 2023 EBS added block public access for snapshots, which prevents the public sharing of your snapshots.
  link: [November 9, 2023](../facts/ebs.md#ebs-change-snapshot-bpa-2023-11)
  say: November ninth, twenty twenty-three
ebs-change-snapshot-bpa-declarative-2024-12
  claim: On December 1, 2024 declarative policies in AWS Organizations became able to apply the block public access setting for snapshots across many Regions and accounts at once.
  link: [December 1, 2024](../facts/ebs.md#ebs-change-snapshot-bpa-declarative-2024-12)
  link: [across multiple Regions and accounts simultaneously](../facts/ebs.md#ebs-change-snapshot-bpa-declarative-2024-12)
  say: December first, twenty twenty-four
ebs-change-snapshot-lock-2023-11
  claim: On November 15, 2023 EBS added snapshot lock, which protects snapshots against accidental or malicious deletion and can store them in WORM format for a specific duration.
  link: [November 15, 2023](../facts/ebs.md#ebs-change-snapshot-lock-2023-11)
  say: November fifteenth, twenty twenty-three
ebs-change-time-based-ami-copy-2025-02
  claim: The EBS User Guide document history dates to February 25, 2025 the change that you can request a completion duration for EBS-backed AMI copy operations, so that AMI copies are completed within a specific timeframe.
  link: [February 25, 2025](../facts/ebs.md#ebs-change-time-based-ami-copy-2025-02)
  say: February twenty-fifth, twenty twenty-five
ebs-change-time-based-snapshot-copy-2024-11
  claim: On November 26, 2024 EBS added time-based snapshot copies: you request a completion duration so that a snapshot copy finishes within a specific timeframe.
  link: [November 26, 2024](../facts/ebs.md#ebs-change-time-based-snapshot-copy-2024-11)
  link: [request a completion duration](../facts/ebs.md#ebs-change-time-based-snapshot-copy-2024-11)
  say: November twenty-sixth, twenty twenty-four
ebs-change-volume-copy-2025-10
  claim: On October 14, 2025 EBS added volume copy: an instant, point-in-time copy of a volume within the same Availability Zone.
  link: [October 14, 2025](../facts/ebs.md#ebs-change-volume-copy-2025-10)
  link: [instant, point-in-time copy](../facts/ebs.md#ebs-change-volume-copy-2025-10)
  say: October fourteenth, twenty twenty-five
ebs-change-volume-copy-cross-account-2026-09
  claim: Posted on Sep 9, 2026: EBS Volume Clones added copying volumes across AWS accounts, with re-encryption under an AWS KMS key of the target account.
  scope: GA after the 2026-07-15 cutoff: not examinable yet.
  link: [Sep 9, 2026](../facts/ebs.md#ebs-change-volume-copy-cross-account-2026-09)
  link: [copying EBS volumes across AWS accounts](../facts/ebs.md#ebs-change-volume-copy-cross-account-2026-09)
  say: September ninth, twenty twenty-six
ebs-cloudwatch-metrics-free-only-when-attached
  claim: All EBS volume types automatically send 1-minute metrics to CloudWatch at no charge, but only while the volume is attached to an instance.
  scope: EBS volume CloudWatch metrics; default; volume attached to an instance.
  link: [1-minute periods at no charge](../facts/ebs.md#ebs-cloudwatch-metrics-free-only-when-attached)
  link: [when the volume is attached to an instance](../facts/ebs.md#ebs-cloudwatch-metrics-free-only-when-attached)
ebs-decision-guide-block-storage-single-instance
  claim: The AWS storage decision guide maps block storage (Amazon EBS and EC2 instance store) to applications that need low-latency, high-performance durable storage attached to single EC2 instances or containers, such as databases.
  scope: AWS storage decision guide, block storage.
  link: [attached to single Amazon EC2 instances or containers](../facts/ebs.md#ebs-decision-guide-block-storage-single-instance)
  link: [low-latency, high-performance durable storage](../facts/ebs.md#ebs-decision-guide-block-storage-single-instance)
ebs-decision-guide-file-storage-shared-access
  claim: The AWS storage decision guide maps file system storage (such as Amazon EFS and Amazon FSx) to applications and workloads that need shared read and write access across multiple Amazon EC2 instances or containers, or from multiple on-premises servers.
  scope: AWS storage decision guide, file storage.
  link: [shared read and write access across multiple Amazon EC2 instances](../facts/ebs.md#ebs-decision-guide-file-storage-shared-access)
ebs-delete-on-termination-additional-default-false
  claim: By default, additional EBS volumes created and attached at launch are not deleted when the instance is terminated; setting DeleteOnTermination to true at launch deletes them on termination.
  scope: additional (non-root) EBS volumes created and attached at launch; default; adjustable; DeleteOnTermination left at its default.
  link: [are not deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-additional-default-false)
  link: [DeleteOnTermination to true](../facts/ebs.md#ebs-delete-on-termination-additional-default-false)
ebs-delete-on-termination-root-default-true
  claim: By default, the root EBS volume created at launch is deleted when the instance is terminated; setting DeleteOnTermination to false at launch keeps the volume so you can attach it to another instance.
  scope: root EBS volume created at launch; default; adjustable; DeleteOnTermination left at its default.
  link: [deleted when that instance is terminated](../facts/ebs.md#ebs-delete-on-termination-root-default-true)
  link: [DeleteOnTermination to false](../facts/ebs.md#ebs-delete-on-termination-root-default-true)
ebs-detach-root-volume-stop-instance
  claim: To detach a volume that is the root device of an instance, you must stop the instance first.
  scope: root EBS volume.
  link: [you must stop the instance](../facts/ebs.md#ebs-detach-root-volume-stop-instance)
  link: [the root device of an instance](../facts/ebs.md#ebs-detach-root-volume-stop-instance)
ebs-detach-running-instance-unmount-first
  claim: You can detach an EBS volume explicitly or by terminating the instance, but if the instance is running you must first unmount the volume; if writes to the volume were in progress when it was detached, the data on the volume might be out of sync.
  scope: detaching EBS volumes; the instance is running.
  link: [you must first unmount the volume](../facts/ebs.md#ebs-detach-running-instance-unmount-first)
  link: [might be out of sync](../facts/ebs.md#ebs-detach-running-instance-unmount-first)
ebs-direct-api-request-pricing
  claim: EBS direct APIs ListChangedBlocks and ListSnapshotBlocks are charged per request, and GetSnapshotBlock and PutSnapshotBlock per SnapshotAPIUnit, where one request uses a 512 KiB block.
  scope: per API request.
  link: [charged per request](../facts/ebs.md#ebs-direct-api-request-pricing)
  link: [block size of 512 KiB](../facts/ebs.md#ebs-direct-api-request-pricing)
  say: charged per request | block size of five hundred twelve KiB
ebs-dlm-app-consistent-pre-post-scripts
  claim: Data Lifecycle Manager automates application-consistent snapshots through pre and post scripts in snapshot policies that target instances: the pre script freezes and flushes I/O before the snapshot starts, and the post script thaws I/O.
  scope: Data Lifecycle Manager snapshot policies that target instances; uses Systems Manager command documents.
  link: [enabling pre and post scripts](../facts/ebs.md#ebs-dlm-app-consistent-pre-post-scripts)
  link: [freeze and flush I/O](../facts/ebs.md#ebs-dlm-app-consistent-pre-post-scripts)
ebs-dlm-archive-min-retention-90-days
  claim: In a Data Lifecycle Manager policy, the minimum retention period for archived snapshots is 90 days.
  scope: per policy schedule with archiving; minimum; not adjustable.
  link: [minimum retention period for archived snapshots is 90 days](../facts/ebs.md#ebs-dlm-archive-min-retention-90-days)
  say: ninety days
ebs-dlm-archive-requires-28-days
  claim: Data Lifecycle Manager can archive snapshots only if the creation frequency is monthly or yearly, or a cron expression with a creation frequency of at least 28 days.
  scope: per policy schedule; minimum; snapshot archiving enabled.
  link: [at least 28 days](../facts/ebs.md#ebs-dlm-archive-requires-28-days)
  say: at least twenty-eight days
ebs-dlm-automates-snapshots-and-amis
  claim: Amazon Data Lifecycle Manager automates the creation, retention and deletion of EBS snapshots and EBS-backed AMIs, at no additional cost.
  scope: Amazon Data Lifecycle Manager.
  link: [creation, retention, and deletion of EBS snapshots](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis)
  link: [at no additional cost](../facts/ebs.md#ebs-dlm-automates-snapshots-and-amis)
ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis
  claim: Amazon Data Lifecycle Manager cannot manage snapshots or AMIs created by other means, and cannot automate instance store-backed AMIs.
  scope: Amazon Data Lifecycle Manager.
  link: [created by any other means](../facts/ebs.md#ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis)
  link: [instance store-backed AMIs](../facts/ebs.md#ebs-dlm-cannot-manage-other-snapshots-or-instance-store-amis)
ebs-dlm-cross-account-copy-isolated-account
  claim: Data Lifecycle Manager can automate cross-account snapshot copies: the source account shares snapshots and the target account's cross-account copy event policy copies them to chosen Regions in an isolated account and encrypts them, protecting against a compromised account.
  scope: Amazon Data Lifecycle Manager cross-account copy; both policies are created in the same Region.
  link: [specific Regions in an isolated account](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account)
  link: [your account being compromised](../facts/ebs.md#ebs-dlm-cross-account-copy-isolated-account)
ebs-dlm-cross-region-copy-three-regions
  claim: A Data Lifecycle Manager snapshot policy schedule that creates snapshots in a Region can copy them to up to three additional Regions or Outposts in your account, with a separate cross-Region copy rule for each destination.
  scope: per Data Lifecycle Manager policy schedule; maximum; not adjustable; the schedule creates snapshots in a Region.
  link: [up to three additional Regions or Outposts](../facts/ebs.md#ebs-dlm-cross-region-copy-three-regions)
  link: [a separate cross-Region copy rule](../facts/ebs.md#ebs-dlm-cross-region-copy-three-regions)
  say: up to three other Regions
ebs-dlm-custom-policies-target-by-tags
  claim: Data Lifecycle Manager custom policies use resource tags to choose what to back up: every instance or volume of the targeted type that has at least one of the policy's target tags is included.
  scope: Amazon Data Lifecycle Manager custom policies.
  link: [use resource tags to identify the resources](../facts/ebs.md#ebs-dlm-custom-policies-target-by-tags)
  link: [specified target resource tags](../facts/ebs.md#ebs-dlm-custom-policies-target-by-tags)
ebs-dlm-custom-policy-types
  claim: Data Lifecycle Manager custom policies are the EBS snapshot policy (targets volumes or instances), the EBS-backed AMI policy (targets instances) and the cross-account copy event policy (copies snapshots shared with you across Regions).
  scope: Amazon Data Lifecycle Manager custom policies.
  link: [EBS snapshot policy](../facts/ebs.md#ebs-dlm-custom-policy-types)
  link: [EBS-backed AMI policy](../facts/ebs.md#ebs-dlm-custom-policy-types)
  link: [Cross-account copy event policy](../facts/ebs.md#ebs-dlm-custom-policy-types)
ebs-dlm-custom-up-to-4-schedules
  claim: A Data Lifecycle Manager custom policy can have up to 4 schedules; schedule 1 is mandatory and schedules 2, 3 and 4 are optional.
  scope: per custom policy; maximum; not adjustable.
  link: [up to 4 schedules](../facts/ebs.md#ebs-dlm-custom-up-to-4-schedules)
  say: up to four schedules
ebs-dlm-default-policies-unbacked-resources
  claim: Data Lifecycle Manager default policies back up all volumes and instances in a Region that do not have recent backups, and an account can have one default policy per resource type in each Region.
  scope: Amazon Data Lifecycle Manager default policies, per account and Region.
  link: [that do not have recent backups](../facts/ebs.md#ebs-dlm-default-policies-unbacked-resources)
  link: [only one default policy per resource type](../facts/ebs.md#ebs-dlm-default-policies-unbacked-resources)
ebs-dlm-default-policy-four-hour-window
  claim: When you create and enable a Data Lifecycle Manager default policy, it randomly assigns targeted resources to a four-hour time window in which they are backed up at the creation frequency.
  scope: per default policy; fixed.
  link: [four-hour time window](../facts/ebs.md#ebs-dlm-default-policy-four-hour-window)
  say: four-hour time window
ebs-dlm-default-policy-min-age-24-hours
  claim: Data Lifecycle Manager default policies only start targeting resources that are at least 24 hours old.
  scope: per default policy; minimum.
  link: [at least 24 hours old](../facts/ebs.md#ebs-dlm-default-policy-min-age-24-hours)
  say: at least twenty-four hours old
ebs-dlm-default-policy-no-cross-account
  claim: A Data Lifecycle Manager default policy cannot share snapshots across accounts or make application-consistent snapshots; a custom policy can, using pre and post scripts for consistency.
  scope: Data Lifecycle Manager default versus custom snapshot policies.
  link: [Support cross-account sharing](../facts/ebs.md#ebs-dlm-default-policy-no-cross-account)
  link: [Yes, using pre and post scripts](../facts/ebs.md#ebs-dlm-default-policy-no-cross-account)
ebs-dlm-default-policy-targets-all-volumes
  claim: A Data Lifecycle Manager default policy for EBS snapshots targets all volumes in the Region that do not have recent snapshots, with optional exclusions; a custom policy targets only volumes or instances that have specific tags.
  scope: per Data Lifecycle Manager snapshot policy; default policy skips volumes with recent snapshots.
  link: [Targets all volumes in the Region](../facts/ebs.md#ebs-dlm-default-policy-targets-all-volumes)
  link: [Targets only volumes or instances](../facts/ebs.md#ebs-dlm-default-policy-targets-all-volumes)
  say: targets all volumes in the Region | targets only tagged volumes or instances
ebs-dlm-first-run-within-hour
  claim: The first Data Lifecycle Manager snapshot creation starts within one hour after the specified start time, and later ones start within one hour of their scheduled time.
  scope: per policy schedule; maximum.
  link: [within one hour after the specified start time](../facts/ebs.md#ebs-dlm-first-run-within-hour)
  say: within one hour after the specified start time
ebs-dlm-frequency-default-vs-custom
  claim: A Data Lifecycle Manager default policy for EBS snapshots creates snapshots every 1 to 7 days; a custom policy can run daily, weekly, monthly, yearly or on a custom cron expression.
  scope: per Data Lifecycle Manager snapshot policy; maximum; not adjustable.
  link: [Every 1 to 7 days.](../facts/ebs.md#ebs-dlm-frequency-default-vs-custom)
  say: every one to seven days
ebs-dlm-retention-default-vs-custom
  claim: A Data Lifecycle Manager default policy for EBS snapshots keeps snapshots for 2 to 14 days; a custom policy keeps up to 1000 snapshots (count-based) or up to 100 years (age-based).
  scope: per Data Lifecycle Manager snapshot policy; maximum; not adjustable.
  link: [2 to 14 days.](../facts/ebs.md#ebs-dlm-retention-default-vs-custom)
  link: [Up to 1000 snapshots (count-based)](../facts/ebs.md#ebs-dlm-retention-default-vs-custom)
  link: [up to 100 years (age-based)](../facts/ebs.md#ebs-dlm-retention-default-vs-custom)
  say: two to fourteen days | up to one thousand snapshots | up to one hundred years
ebs-dlm-retention-types-default-vs-custom
  claim: A Data Lifecycle Manager default policy for EBS snapshots supports age-based retention only; a custom EBS snapshot policy supports age-based and count-based retention.
  scope: per Data Lifecycle Manager snapshot policy.
  link: [Age-based retention only](../facts/ebs.md#ebs-dlm-retention-types-default-vs-custom)
  link: [Age-based and count-based retention](../facts/ebs.md#ebs-dlm-retention-types-default-vs-custom)
  say: age-based retention only | age-based and count-based retention
ebs-dlm-schedule-frequency-and-retention-type
  claim: A Data Lifecycle Manager policy schedule runs daily, weekly, monthly or yearly (or on a custom cron expression), and retains snapshots by their total count or by their age.
  scope: Amazon Data Lifecycle Manager snapshot policy schedules.
  link: [daily, weekly, monthly, or yearly schedule](../facts/ebs.md#ebs-dlm-schedule-frequency-and-retention-type)
  link: [either their total count or their age](../facts/ebs.md#ebs-dlm-schedule-frequency-and-retention-type)
ebs-dlm-schedules-default-vs-custom
  claim: A Data Lifecycle Manager default policy for EBS snapshots does not support multiple schedules; a custom EBS snapshot policy supports up to 4 schedules per policy.
  scope: per Data Lifecycle Manager snapshot policy; maximum; not adjustable; default policy: one schedule only.
  link: [up to 4 schedules per policy](../facts/ebs.md#ebs-dlm-schedules-default-vs-custom)
  say: up to four schedules per policy
ebs-elastic-volumes-four-modifications-24h
  claim: You can modify one EBS volume up to four times within a rolling 24-hour period, provided the volume is in-use or available and every earlier modification of it is completed.
  scope: per volume, rolling 24-hour period; maximum; not adjustable; the previous modification must be completed first.
  link: [up to four times within a rolling 24-hour period](../facts/ebs.md#ebs-elastic-volumes-four-modifications-24h)
  say: up to four times in any twenty-four hours
ebs-elastic-volumes-modify-without-detach
  claim: With Elastic Volumes you can increase volume size, change volume type or adjust performance; on an instance that supports Elastic Volumes you do it without detaching the volume or restarting the instance.
  scope: EBS volume; the instance supports Elastic Volumes.
  link: [without detaching the volume or restarting the instance](../facts/ebs.md#ebs-elastic-volumes-modify-without-detach)
  link: [increase the volume size, change the volume type](../facts/ebs.md#ebs-elastic-volumes-modify-without-detach)
ebs-empty-volume-no-initialization
  claim: Empty volumes deliver their maximum performance immediately after creation and do not need initialization.
  scope: empty EBS volumes; not created from a snapshot or a volume copy.
  link: [do not require initialization](../facts/ebs.md#ebs-empty-volume-no-initialization)
  link: [maximum performance immediately after creation](../facts/ebs.md#ebs-empty-volume-no-initialization)
ebs-encrypt-existing-volume-via-snapshot
  claim: You cannot encrypt an existing unencrypted volume or snapshot directly: snapshot the volume and create a new encrypted volume from the snapshot, or create an encrypted copy of an unencrypted snapshot.
  scope: unencrypted EBS volumes and snapshots.
  link: [You can't directly encrypt existing unencrypted volumes](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot)
  link: [create a new encrypted volume](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot)
  link: [create an encrypted copy of that snapshot](../facts/ebs.md#ebs-encrypt-existing-volume-via-snapshot)
ebs-encrypted-snapshot-restore-default-key
  claim: Without encryption by default, a volume restored from an unencrypted snapshot is unencrypted unless you set the Encrypted parameter; with encryption by default enabled, encryption is mandatory for volumes restored from unencrypted snapshots.
  scope: volumes restored from unencrypted snapshots; default; adjustable; depends on encryption by default in the Region.
  link: [is unencrypted by default](../facts/ebs.md#ebs-encrypted-snapshot-restore-default-key)
  link: [encryption is mandatory for volumes restored](../facts/ebs.md#ebs-encrypted-snapshot-restore-default-key)
ebs-encryption-aes-256
  claim: Amazon EBS encryption uses 256-bit Advanced Encryption Standard algorithms (AES-256) and an Amazon-managed key infrastructure.
  scope: Amazon EBS encryption.
  link: [AES-256](../facts/ebs.md#ebs-encryption-aes-256)
  link: [256-bit Advanced Encryption Standard](../facts/ebs.md#ebs-encryption-aes-256)
ebs-encryption-all-instance-types
  claim: All EC2 instance types, current and previous generation, support Amazon EBS encryption, and encryption by default is supported on all of them.
  scope: EC2 instance types.
  link: [All Amazon EC2 instance types support Amazon EBS encryption](../facts/ebs.md#ebs-encryption-all-instance-types)
  link: [all current generation and previous generation](../facts/ebs.md#ebs-encryption-all-instance-types)
ebs-encryption-all-volume-types
  claim: Every EBS volume type supports encryption.
  scope: EBS volume types.
  link: [All EBS volume types support encryption](../facts/ebs.md#ebs-encryption-all-volume-types)
  link: [support encryption](../facts/ebs.md#ebs-encryption-all-volume-types)
ebs-encryption-aws-managed-key-alias-per-region
  claim: EBS automatically creates a unique AWS managed key, alias aws/ebs, in each Region where you create EBS resources, and uses it by default; you can use a symmetric customer managed key instead.
  scope: per Region; default; adjustable; no customer managed key chosen.
  link: [aws/ebs](../facts/ebs.md#ebs-encryption-aws-managed-key-alias-per-region)
  link: [a unique AWS managed key in each Region](../facts/ebs.md#ebs-encryption-aws-managed-key-alias-per-region)
  link: [a symmetric customer managed encryption key](../facts/ebs.md#ebs-encryption-aws-managed-key-alias-per-region)
ebs-encryption-aws-managed-key-unless-cmk
  claim: The first time you create an encrypted EBS volume in a Region, AWS creates a default AWS managed KMS key, and EBS encryption uses that key unless you create and use a customer managed key.
  scope: per Region; default; adjustable; no customer managed key chosen.
  link: [default AWS managed KMS key](../facts/ebs.md#ebs-encryption-aws-managed-key-unless-cmk)
  link: [create and use a customer managed key](../facts/ebs.md#ebs-encryption-aws-managed-key-unless-cmk)
ebs-encryption-by-default-new-resources-only
  claim: Encryption by default makes the account encrypt the new EBS volumes and snapshot copies you create; it has no effect on existing EBS volumes or snapshots.
  scope: EBS encryption by default.
  link: [enforce the encryption of the new EBS volumes](../facts/ebs.md#ebs-encryption-by-default-new-resources-only)
  link: [has no effect on existing EBS volumes](../facts/ebs.md#ebs-encryption-by-default-new-resources-only)
ebs-encryption-by-default-region-setting
  claim: Encryption by default is a Region-specific setting; once it is enabled for a Region, you cannot disable it for individual volumes or snapshots in that Region.
  scope: per Region; after encryption by default is enabled.
  link: [a Region-specific setting](../facts/ebs.md#ebs-encryption-by-default-region-setting)
  link: [cannot disable it for individual volumes](../facts/ebs.md#ebs-encryption-by-default-region-setting)
ebs-encryption-cannot-be-removed
  claim: Encryption cannot be removed from an encrypted volume or snapshot, so a volume restored from an encrypted snapshot, or a copy of an encrypted snapshot, is always encrypted.
  scope: encrypted EBS volumes and snapshots.
  link: [You cannot remove encryption](../facts/ebs.md#ebs-encryption-cannot-be-removed)
  link: [is always encrypted](../facts/ebs.md#ebs-encryption-cannot-be-removed)
ebs-encryption-key-fixed-change-on-copy
  claim: You cannot change the KMS key of an existing snapshot or volume, but you can choose a different KMS key during a snapshot copy so that the copy is encrypted with the new key.
  scope: encrypted EBS volumes and snapshots.
  link: [You cannot change the KMS key](../facts/ebs.md#ebs-encryption-key-fixed-change-on-copy)
  link: [during a snapshot copy operation](../facts/ebs.md#ebs-encryption-key-fixed-change-on-copy)
ebs-encryption-mixed-volumes-on-one-instance
  claim: You can attach encrypted and unencrypted volumes to the same instance at the same time, and move data freely between them.
  scope: EBS volumes on one instance.
  link: [both encrypted and unencrypted volumes](../facts/ebs.md#ebs-encryption-mixed-volumes-on-one-instance)
  link: [you can freely transfer data between them](../facts/ebs.md#ebs-encryption-mixed-volumes-on-one-instance)
ebs-encryption-on-host-covers-in-transit
  claim: EBS encryption operations run on the servers that host the EC2 instances, so both data at rest and data in transit between the instance and its attached volume (and later snapshots) are protected.
  scope: encrypted EBS volumes.
  link: [data-at-rest and data-in-transit](../facts/ebs.md#ebs-encryption-on-host-covers-in-transit)
  link: [on the servers that host Amazon EC2 instances](../facts/ebs.md#ebs-encryption-on-host-covers-in-transit)
ebs-encryption-propagates-to-snapshots-and-volumes
  claim: Snapshots of encrypted EBS volumes are automatically encrypted, and volumes created from encrypted snapshots are automatically encrypted.
  scope: encrypted EBS volumes and snapshots.
  link: [Snapshots of encrypted EBS volumes are automatically encrypted](../facts/ebs.md#ebs-encryption-propagates-to-snapshots-and-volumes)
  link: [created from encrypted snapshots are automatically encrypted](../facts/ebs.md#ebs-encryption-propagates-to-snapshots-and-volumes)
ebs-encryption-same-iops-minimal-latency
  claim: Encrypted volumes deliver the same IOPS performance as unencrypted volumes with a minimal effect on latency, and encryption and decryption are transparent to you and your applications.
  scope: encrypted EBS volumes.
  link: [the same IOPS performance on encrypted volumes](../facts/ebs.md#ebs-encryption-same-iops-minimal-latency)
  link: [a minimal effect on latency](../facts/ebs.md#ebs-encryption-same-iops-minimal-latency)
ebs-encryption-users-need-kms-permissions
  claim: To use EBS encryption, users must be granted permission to call a set of AWS KMS actions on the key (such as kms:CreateGrant, kms:Decrypt and kms:GenerateDataKeyWithoutPlaintext).
  scope: IAM users and roles using EBS encryption.
  link: [You must grant users permission to call](../facts/ebs.md#ebs-encryption-users-need-kms-permissions)
  link: [do not allow full access to kms:CreateGrant](../facts/ebs.md#ebs-encryption-users-need-kms-permissions)
ebs-extend-partition-after-size-increase
  claim: After you increase the size of a volume, you must also extend the volume's partition and file system to use the additional storage capacity.
  scope: EBS volume size increase.
  link: [you must also extend the volume's partition](../facts/ebs.md#ebs-extend-partition-after-size-increase)
  link: [to make use of the additional storage capacity](../facts/ebs.md#ebs-extend-partition-after-size-increase)
ebs-faq-average-latency
  claim: The average latency between EC2 instances and EBS is single-digit milliseconds; the average latency of io2 Block Express volumes is sub-millisecond.
  scope: average latency between EC2 instances and EBS volumes.
  link: [single-digit milliseconds](../facts/ebs.md#ebs-faq-average-latency)
  link: [sub-millisecond](../facts/ebs.md#ebs-faq-average-latency)
ebs-faq-block-express-definition
  claim: EBS Block Express is the next generation of EBS storage server architecture, built for the highest performance with sub-millisecond latency; it uses Scalable Reliable Datagrams (SRD) to talk to Nitro System-based EC2 instances.
  scope: EBS Block Express; Nitro System-based EC2 instances.
  link: [next generation of Amazon EBS storage server architecture](../facts/ebs.md#ebs-faq-block-express-definition)
  link: [Scalable Reliable Datagrams (SRD)](../facts/ebs.md#ebs-faq-block-express-definition)
ebs-faq-detached-snapshot-and-delete
  claim: For a detached volume, AWS recommends considering creating a snapshot and deleting the volume to reduce costs.
  scope: detached EBS volumes; volume is detached.
  link: [creating a snapshot and deleting the volume](../facts/ebs.md#ebs-faq-detached-snapshot-and-delete)
ebs-faq-direct-apis-block-size-512kib
  claim: The GetSnapshotBlock and PutSnapshotBlock APIs support a 512KiB block size.
  scope: per block, GetSnapshotBlock and PutSnapshotBlock; fixed; not adjustable.
  link: [512KiB](../facts/ebs.md#ebs-faq-direct-apis-block-size-512kib)
ebs-faq-direct-apis-capabilities
  claim: The EBS direct APIs can create EBS snapshots, write data directly to snapshots, read data on snapshots, and identify the differences between two snapshots.
  scope: EBS snapshots.
  link: [write data directly to your snapshots](../facts/ebs.md#ebs-faq-direct-apis-capabilities)
  link: [read data on your snapshots](../facts/ebs.md#ebs-faq-direct-apis-capabilities)
  link: [identify the differences or changes between two snapshots](../facts/ebs.md#ebs-faq-direct-apis-capabilities)
ebs-faq-direct-apis-on-premises-dr
  claim: With the EBS direct APIs you can create incremental snapshots directly from on-premises data, for quick disaster recovery.
  scope: EBS direct APIs.
  link: [incremental snapshots directly from data on-premises](../facts/ebs.md#ebs-faq-direct-apis-on-premises-dr)
ebs-faq-dlm-ssm-app-consistent
  claim: Amazon Data Lifecycle Manager and AWS Systems Manager can coordinate freeze, flush I/O and unfreeze of an application or database together with the start of EBS snapshots, to automate application-consistent snapshots.
  scope: EBS snapshots; you provide the application-specific commands.
  link: [Amazon Data Lifecycle Manager and AWS Systems Manager](../facts/ebs.md#ebs-faq-dlm-ssm-app-consistent)
  link: [freeze, flush I/O, and unfreeze](../facts/ebs.md#ebs-faq-dlm-ssm-app-consistent)
ebs-faq-durable-data-ebs-or-s3
  claim: For data that needs a higher level of durability, AWS recommends EBS volumes or backing up the data to Amazon S3.
  scope: data that needs a higher level of durability; data requiring a higher level of durability.
  link: [using Amazon EBS volumes](../facts/ebs.md#ebs-faq-durable-data-ebs-or-s3)
  link: [backing up the data to Amazon S3](../facts/ebs.md#ebs-faq-durable-data-ebs-or-s3)
ebs-faq-elastic-volumes
  claim: Elastic Volumes lets you increase capacity, tune performance or change the volume type of an existing EBS volume with a single CLI call, API call or a few console clicks.
  scope: existing EBS volumes.
  link: [Elastic Volumes](../facts/ebs.md#ebs-faq-elastic-volumes)
  link: [change your volume type](../facts/ebs.md#ebs-faq-elastic-volumes)
  link: [increase capacity](../facts/ebs.md#ebs-faq-elastic-volumes)
ebs-faq-encrypted-from-unencrypted-ami
  claim: You can launch an instance with encrypted EBS volumes from an unencrypted AMI: when the AMI is backed by unencrypted EBS snapshots, you can encrypt some or all of the volumes during launch.
  scope: instance launch from an AMI.
  link: [encrypt some or all of the volumes](../facts/ebs.md#ebs-faq-encrypted-from-unencrypted-ami)
  say: yes, you can encrypt the volumes at launch
ebs-faq-encrypted-volume-at-launch
  claim: You can create encrypted data volumes when you launch an instance, including volumes that are not part of the AMI, with AWS managed or customer managed KMS keys, through the BlockDeviceMapping of RunInstances or the console launch wizard.
  scope: data volumes created at instance launch.
  link: [either AWS-managed or customer-managed](../facts/ebs.md#ebs-faq-encrypted-volume-at-launch)
  link: [BlockDeviceMapping](../facts/ebs.md#ebs-faq-encrypted-volume-at-launch)
ebs-faq-encryption-by-default-per-region
  claim: You can enable EBS encryption by default with a single setting per Region, which ensures that all new volumes are always encrypted.
  scope: per Region; encryption by default is enabled.
  link: [single setting per region](../facts/ebs.md#ebs-faq-encryption-by-default-per-region)
  link: [all new volumes are always encrypted](../facts/ebs.md#ebs-faq-encryption-by-default-per-region)
ebs-faq-encryption-covers-volumes-snapshots
  claim: EBS encryption encrypts EBS data volumes, boot volumes and snapshots, without you building and maintaining your own key management infrastructure.
  scope: Amazon EBS.
  link: [data volumes, boot volumes and snapshots](../facts/ebs.md#ebs-faq-encryption-covers-volumes-snapshots)
ebs-faq-encryption-key-choices
  claim: EBS encryption protects data at rest with Amazon-managed keys or with keys you create and manage in AWS KMS.
  scope: EBS encryption.
  link: [Amazon-managed keys](../facts/ebs.md#ebs-faq-encryption-key-choices)
  link: [keys you create and manage](../facts/ebs.md#ebs-faq-encryption-key-choices)
ebs-faq-encryption-unique-aes-256-key
  claim: Each newly created encrypted volume gets a unique 256-bit AES key, and volumes created from encrypted snapshots share that key.
  scope: per encrypted EBS volume.
  link: [unique 256-bit AES key](../facts/ebs.md#ebs-faq-encryption-unique-aes-256-key)
  link: [share the key](../facts/ebs.md#ebs-faq-encryption-unique-aes-256-key)
ebs-faq-fsr-credit-formula
  claim: To estimate the FSR credit bucket size and fill rate, divide 1,024 by the snapshot size; a 100 GiB snapshot has a maximum balance of 10 credits and refills 10 credits every hour.
  scope: per FSR-enabled snapshot, per Availability Zone; maximum; not adjustable; estimate.
  link: [divide 1,024 by your snapshot size](../facts/ebs.md#ebs-faq-fsr-credit-formula)
  link: [10 credits every hour](../facts/ebs.md#ebs-faq-fsr-credit-formula)
ebs-faq-fsr-disabled-on-delete
  claim: When you delete a snapshot, its FSR is automatically disabled and FSR billing for it ends.
  scope: FSR-enabled snapshots; the snapshot is deleted.
  link: [automatically disabled](../facts/ebs.md#ebs-faq-fsr-disabled-on-delete)
ebs-faq-fsr-enabled-per-az
  claim: FSR is enabled on a snapshot in the Availability Zone where the initialized volumes will be restored, and each AZ where it is enabled gets its own credit bucket.
  scope: per snapshot, per Availability Zone.
  link: [enable-fast-snapshot-restores](../facts/ebs.md#ebs-faq-fsr-enabled-per-az)
  link: [its own credit bucket](../facts/ebs.md#ebs-faq-fsr-enabled-per-az)
ebs-faq-fsr-not-faster-creation
  claim: Enabling Fast Snapshot Restore does not speed up snapshot creation; it improves restoring data from the snapshot to volumes.
  scope: FSR-enabled snapshots.
  link: [do not speed up snapshot creation time](../facts/ebs.md#ebs-faq-fsr-not-faster-creation)
ebs-faq-fsr-restored-full-performance
  claim: EBS volumes restored from FSR-enabled snapshots instantly receive their full performance.
  scope: volumes restored from FSR-enabled snapshots; the snapshot has FSR enabled.
  link: [instantly receive their full performance](../facts/ebs.md#ebs-faq-fsr-restored-full-performance)
ebs-faq-fsr-shared-snapshots-allowed
  claim: You can enable fast snapshot restore (FSR) for public snapshots and for all private snapshots shared with your account, and only your account is billed for the FSR of a shared snapshot.
  scope: snapshots shared with your account.
  link: [all private snapshots shared with your account](../facts/ebs.md#ebs-faq-fsr-shared-snapshots-allowed)
  link: [only your account will be billed](../facts/ebs.md#ebs-faq-fsr-shared-snapshots-allowed)
ebs-faq-fsr-up-to-10-volumes
  claim: When the FSR credit bucket is full, up to 10 initialized volumes can be created from an FSR-enabled snapshot at once; volume creations beyond the limit proceed as if FSR were not enabled.
  scope: per FSR-enabled snapshot, per Availability Zone; maximum; not adjustable; credit bucket is full.
  link: [up to 10 initialized volumes](../facts/ebs.md#ebs-faq-fsr-up-to-10-volumes)
  link: [as if FSR is not enabled](../facts/ebs.md#ebs-faq-fsr-up-to-10-volumes)
ebs-faq-fsr-when-to-use
  claim: Enable Fast Snapshot Restore when you are concerned about data-access latency when restoring a snapshot to a volume and want to avoid the initial performance hit during initialization; use cases include VDI, backup and restore, test/dev volume copies and booting from custom AMIs.
  scope: EBS snapshots.
  link: [avoid the initial performance hit during initialization](../facts/ebs.md#ebs-faq-fsr-when-to-use)
  link: [booting from custom AMIs](../facts/ebs.md#ebs-faq-fsr-when-to-use)
ebs-faq-gp-consistency-99
  claim: Attached to EBS-optimized instances, gp3 and gp2 volumes are designed to deliver within 10% of the provisioned IOPS performance 99% of the time in a given year.
  scope: per gp3 or gp2 volume, per year; fixed; attached to EBS-optimized instances.
  link: [within 10% of the provisioned IOPS performance](../facts/ebs.md#ebs-faq-gp-consistency-99)
  link: [99% of the time](../facts/ebs.md#ebs-faq-gp-consistency-99)
ebs-faq-gp-single-digit-ms
  claim: Attached to EBS-optimized instances, gp3 and gp2 volumes can achieve single-digit millisecond latencies.
  scope: gp3 and gp2 volumes; attached to EBS-optimized instances.
  link: [single digit millisecond latencies](../facts/ebs.md#ebs-faq-gp-single-digit-ms)
ebs-faq-gp3-no-burst
  claim: gp3 volumes do not burst: every gp3 volume includes 3,000 IOPS and 125 MB/s of consistent performance at no additional cost and can sustain them indefinitely.
  scope: per gp3 volume; default; baseline included with every gp3 volume.
  link: [3,000 IOPS](../facts/ebs.md#ebs-faq-gp3-no-burst)
  link: [125 MB/s](../facts/ebs.md#ebs-faq-gp3-no-burst)
  link: [at no additional cost](../facts/ebs.md#ebs-faq-gp3-no-burst)
ebs-faq-gp3-price-performance-balance
  claim: gp3 is the latest generation of General Purpose SSD and gives the right balance of price and performance for most applications that do not need the highest performance consistency or 99.999% durability.
  scope: gp3 volumes; the application does not require the highest performance consistency or 99.999% durability.
  link: [right balance of price and performance](../facts/ebs.md#ebs-faq-gp3-price-performance-balance)
  link: [latest generation of General Purpose SSD volumes](../facts/ebs.md#ebs-faq-gp3-price-performance-balance)
ebs-faq-gp3-suited-workloads
  claim: gp3 volumes are ideal for applications that need a balance between cost and performance, including medium-sized single-instance databases, data analytics, development and test environments, virtual desktops, web servers and boot volumes.
  scope: gp3 volumes.
  link: [balance between cost and performance](../facts/ebs.md#ebs-faq-gp3-suited-workloads)
  link: [development and test environments](../facts/ebs.md#ebs-faq-gp3-suited-workloads)
  link: [boot volumes](../facts/ebs.md#ebs-faq-gp3-suited-workloads)
ebs-faq-gp3-to-io2-when
  claim: For applications that need higher durability, better latency consistency, or higher IOPS and throughput than gp3 can provide, AWS recommends io2 Block Express volumes.
  scope: choice between gp3 and io2 Block Express; needs exceed what gp3 can provide.
  link: [we recommend using io2 Block Express volumes](../facts/ebs.md#ebs-faq-gp3-to-io2-when)
  link: [higher durability, better latency consistency](../facts/ebs.md#ebs-faq-gp3-to-io2-when)
ebs-faq-hdd-consistency-99
  claim: Attached to EBS-optimized instances, st1 and sc1 volumes are designed to deliver within 10% of the expected throughput performance 99% of the time in a given year.
  scope: per st1 or sc1 volume, per year; fixed; attached to EBS-optimized instances.
  link: [within 10% of the expected throughput performance](../facts/ebs.md#ebs-faq-hdd-consistency-99)
  link: [99% of the time](../facts/ebs.md#ebs-faq-hdd-consistency-99)
ebs-faq-hdd-not-for-random-small-io
  claim: A transactional workload with small, random I/Os, such as a database, will not perform well on HDD-backed volumes; sequential I/Os and large I/O sizes achieve the advertised st1 and sc1 performance for a longer period of time.
  scope: st1 and sc1 volumes; small, random I/O workloads.
  link: [won't perform well on HDD-backed volumes](../facts/ebs.md#ebs-faq-hdd-not-for-random-small-io)
  link: [sequential I/Os and large I/O sizes](../facts/ebs.md#ebs-faq-hdd-not-for-random-small-io)
ebs-faq-hdd-snapshot-lowers-writes
  claim: On st1 and sc1 only, taking a snapshot lowers expected write performance to the baseline rate until the snapshot completes.
  scope: st1 and sc1 volumes; while a snapshot is in progress.
  link: [write performance down to the baseline rate](../facts/ebs.md#ebs-faq-hdd-snapshot-lowers-writes)
  link: [specific to st1 and sc1](../facts/ebs.md#ebs-faq-hdd-snapshot-lowers-writes)
ebs-faq-hdd-workloads
  claim: HDD-backed EBS volumes (st1 and sc1) are designed for throughput-intensive and big-data workloads, large I/O sizes and sequential I/O patterns.
  scope: HDD-backed EBS volumes (st1, sc1).
  link: [throughput-intensive and big-data workloads](../facts/ebs.md#ebs-faq-hdd-workloads)
  link: [sequential I/O patterns](../facts/ebs.md#ebs-faq-hdd-workloads)
ebs-faq-instance-store-vs-ebs-persistence
  claim: Data on a local instance store persists only as long as the instance is alive, while data on an EBS volume can persist independently of the life of the instance.
  scope: instance store volumes and EBS volumes.
  link: [only as long as that instance is alive](../facts/ebs.md#ebs-faq-instance-store-vs-ebs-persistence)
  link: [persist independently of the life of the instance](../facts/ebs.md#ebs-faq-instance-store-vs-ebs-persistence)
ebs-faq-io2-256kb-io-16000-iops
  claim: In the FAQ example, an io2 Block Express volume provisioned with 40,000 IOPS for an I/O size of 16KB achieves up to 40,000 IOPS at that size; if the I/O size is increased to 256 KB, it achieves up to 16,000 IOPS, because the maximum throughput of 4000 MiB/s is achieved at 16,000 IOPS.
  scope: per io2 Block Express volume, FAQ example; maximum; not adjustable; a volume provisioned with 40,000 IOPS (FAQ example); I/O size of 256 KB.
  link: [16,000 IOPS](../facts/ebs.md#ebs-faq-io2-256kb-io-16000-iops)
  link: [4000 MiB/s](../facts/ebs.md#ebs-faq-io2-256kb-io-16000-iops)
ebs-faq-io2-consistency-99-9
  claim: Attached to EBS-optimized instances, io2 Block Express volumes are designed to deliver within 10% of the provisioned IOPS performance 99.9% of the time in a given year.
  scope: per io2 Block Express volume, per year; fixed; attached to EBS-optimized instances.
  link: [within 10%](../facts/ebs.md#ebs-faq-io2-consistency-99-9)
  link: [99.9% of the time](../facts/ebs.md#ebs-faq-io2-consistency-99-9)
ebs-faq-io2-durability-99999
  claim: io2 Block Express is designed for business-critical applications and offers 99.999% durability, 100X greater durability than other EBS volumes.
  scope: per io2 Block Express volume; fixed; design target.
  link: [99.999%](../facts/ebs.md#ebs-faq-io2-durability-99999)
  link: [100X greater durability](../facts/ebs.md#ebs-faq-io2-durability-99999)
ebs-faq-io2-still-snapshot-and-replicate
  claim: High volume durability, snapshots and replicating volumes across Availability Zones protect against different types of failures; customers can use one, two or all three approaches based on their data durability requirements.
  scope: io2 Block Express volumes.
  link: [protect against different types of failures](../facts/ebs.md#ebs-faq-io2-still-snapshot-and-replicate)
  link: [one, two, or all of these approaches](../facts/ebs.md#ebs-faq-io2-still-snapshot-and-replicate)
ebs-faq-io2-suited-workloads
  claim: io2 Block Express suits performance- and capacity-intensive workloads that benefit from lower latency, better latency consistency, higher IOPS, higher throughput or larger capacity in a single volume, such as relational and NoSQL databases (SAP HANA, Oracle, MS SQL, PostgreSQL, MySQL, MongoDB, Cassandra).
  scope: io2 Block Express volumes.
  link: [performance and capacity intensive workloads](../facts/ebs.md#ebs-faq-io2-suited-workloads)
  link: [relational and NoSQL databases](../facts/ebs.md#ebs-faq-io2-suited-workloads)
ebs-faq-multi-attach-application-requirements
  claim: An application can use Multi-Attach if it is built on Windows Server Failover Cluster, coordinates safe access to shared storage with NVMe reservations, or coordinates safe access at the application level.
  scope: Multi-Attach enabled volumes.
  link: [Windows Server Failover Cluster](../facts/ebs.md#ebs-faq-multi-attach-application-requirements)
  link: [NVMe reservations](../facts/ebs.md#ebs-faq-multi-attach-application-requirements)
  link: [coordinates safe access at the application-level](../facts/ebs.md#ebs-faq-multi-attach-application-requirements)
ebs-faq-multi-attach-delete-on-termination-last
  claim: For a Multi-Attach volume, the deleteOnTermination behavior is set by the configuration of the last attached instance that is terminated; for predictable behavior, set the flag the same way on all attached instances.
  scope: Multi-Attach enabled volumes.
  link: [the last attached instance that is terminated](../facts/ebs.md#ebs-faq-multi-attach-delete-on-termination-last)
  link: [for all of the instances](../facts/ebs.md#ebs-faq-multi-attach-delete-on-termination-last)
ebs-faq-multi-tenant-rate-limiting
  claim: EBS is a multi-tenant block storage service that uses rate limiting to avoid resource contention.
  scope: Amazon EBS.
  link: [multi-tenant block storage service](../facts/ebs.md#ebs-faq-multi-tenant-rate-limiting)
  link: [rate limiting](../facts/ebs.md#ebs-faq-multi-tenant-rate-limiting)
ebs-faq-piops-all-instance-types
  claim: Provisioned IOPS SSD io2 Block Express and io1 volumes are available on all EC2 instance types.
  scope: io2 Block Express and io1 volumes.
  link: [available on all EC2 instance types](../facts/ebs.md#ebs-faq-piops-all-instance-types)
ebs-faq-piops-base-io-size-16kb
  claim: Provisioned IOPS volumes have a base I/O size of 16KB; when you provision IOPS for io2 Block Express volumes, the IOPS rate you get depends on the I/O size of your application reads and writes.
  scope: Provisioned IOPS volumes; fixed.
  link: [16KB](../facts/ebs.md#ebs-faq-piops-base-io-size-16kb)
ebs-faq-piops-billed-when-detached
  claim: You are billed for the IOPS provisioned on a Provisioned IOPS volume even when it is disconnected from an instance.
  scope: Provisioned IOPS volumes; volume disconnected from an instance.
  link: [billed for the IOPS provisioned](../facts/ebs.md#ebs-faq-piops-billed-when-detached)
ebs-faq-piops-queue-depth
  claim: For maximum consistency, a Provisioned IOPS volume must keep an average queue depth of one for every 1000 provisioned IOPS in a minute.
  scope: per Provisioned IOPS volume; minimum; for maximum consistency; average rounded to the nearest whole number, in a minute.
  link: [one for every 1000 provisioned IOPS](../facts/ebs.md#ebs-faq-piops-queue-depth)
ebs-faq-provisioned-rate-initialization
  claim: Provisioned Rate for Volume Initialization is for volumes that need to be fully performant within a predictable amount of time; you enter the desired initialization rate when you launch instances from EBS-backed AMIs or create volumes from snapshots.
  scope: volumes created from snapshots or EBS-backed AMIs.
  link: [fully performant within a predictable amount of time](../facts/ebs.md#ebs-faq-provisioned-rate-initialization)
  link: [enter a desired volume initialization rate](../facts/ebs.md#ebs-faq-provisioned-rate-initialization)
ebs-faq-replicated-within-az
  claim: EBS volume data is replicated across multiple servers in one Availability Zone, at no additional charge, to prevent data loss from the failure of any single component.
  scope: per EBS volume, within its Availability Zone.
  link: [replicated across multiple servers in an Availability Zone](../facts/ebs.md#ebs-faq-replicated-within-az)
  link: [no additional charge](../facts/ebs.md#ebs-faq-replicated-within-az)
ebs-faq-root-delete-on-termination-no
  claim: To keep an EBS root volume after the instance ends, set its Delete on termination flag to No.
  scope: EBS volume used as a root partition; the volume is the root partition.
  link: [Delete on termination flag](../facts/ebs.md#ebs-faq-root-delete-on-termination-no)
  link: [persist outside the life of the instance](../facts/ebs.md#ebs-faq-root-delete-on-termination-no)
ebs-faq-share-encrypted-customer-managed-key
  claim: You can share encrypted snapshots and AMIs with other AWS accounts when they are encrypted with a customer managed KMS key.
  scope: encrypted snapshots and AMIs; encrypted with a customer managed key.
  link: [customer-managed customer master key (CMK)](../facts/ebs.md#ebs-faq-share-encrypted-customer-managed-key)
ebs-faq-six-volume-types
  claim: The EBS FAQ lists six volume types: Provisioned IOPS SSD (io2 Block Express and io1), General Purpose SSD (gp3 and gp2), Throughput Optimized HDD (st1) and Cold HDD (sc1).
  scope: Amazon EBS.
  link: [six volume types](../facts/ebs.md#ebs-faq-six-volume-types)
  link: [Provisioned IOPS SSD (io2 Block Express and io1)](../facts/ebs.md#ebs-faq-six-volume-types)
  link: [General Purpose SSD (gp3 and gp2)](../facts/ebs.md#ebs-faq-six-volume-types)
  link: [Throughput Optimized HDD (st1) and Cold HDD (sc1)](../facts/ebs.md#ebs-faq-six-volume-types)
ebs-faq-snapshot-consistent-detach
  claim: For consistent snapshots of a volume attached to an instance, AWS recommends detaching the volume cleanly, taking the snapshot, and then reattaching the volume; for root volumes, it recommends shutting down the machine.
  scope: EBS volumes attached to an instance.
  link: [detaching the volume cleanly](../facts/ebs.md#ebs-faq-snapshot-consistent-detach)
  link: [shutting down the machine](../facts/ebs.md#ebs-faq-snapshot-consistent-detach)
ebs-faq-snapshot-time-16tb-vs-1tb
  claim: By design, a snapshot of an entire 16 TB volume should take no longer than a snapshot of an entire 1 TB volume; actual time depends on factors such as the amount of data changed since the last snapshot.
  scope: EBS snapshot creation time; by design; actual time varies.
  link: [no longer than the time](../facts/ebs.md#ebs-faq-snapshot-time-16tb-vs-1tb)
  link: [16 TB volume](../facts/ebs.md#ebs-faq-snapshot-time-16tb-vs-1tb)
  link: [the amount of data that has changed](../facts/ebs.md#ebs-faq-snapshot-time-16tb-vs-1tb)
ebs-faq-snapshot-unique-id-restore-any
  claim: Each snapshot is given a unique identifier, and you can create volumes from any of your existing snapshots.
  scope: EBS snapshots.
  link: [a unique identifier](../facts/ebs.md#ebs-faq-snapshot-unique-id-restore-any)
  link: [based on any of their existing snapshots](../facts/ebs.md#ebs-faq-snapshot-unique-id-restore-any)
ebs-faq-snapshot-vs-az-replication-protects
  claim: Snapshots protect against a volume failure; replicating volumes across Availability Zones protects against an AZ-level failure and also gives faster recovery.
  scope: EBS volumes.
  link: [the unlikely event of a volume failure](../facts/ebs.md#ebs-faq-snapshot-vs-az-replication-protects)
  link: [protects against an AZ level failure](../facts/ebs.md#ebs-faq-snapshot-vs-az-replication-protects)
  link: [faster recovery in case of failure](../facts/ebs.md#ebs-faq-snapshot-vs-az-replication-protects)
ebs-faq-snapshot-written-data-only
  claim: Snapshots only capture data that has been written to the EBS volume, which might exclude data cached locally by the application or OS.
  scope: EBS snapshots.
  link: [only capture data that has been written](../facts/ebs.md#ebs-faq-snapshot-written-data-only)
  link: [locally cached by your application or OS](../facts/ebs.md#ebs-faq-snapshot-written-data-only)
ebs-faq-snapshots-not-via-s3-api
  claim: EBS snapshots cannot be accessed with the regular Amazon S3 API; they are only available through the Amazon EC2 API.
  scope: EBS snapshots.
  link: [only available through the Amazon EC2 API](../facts/ebs.md#ebs-faq-snapshots-not-via-s3-api)
ebs-faq-ssd-workloads
  claim: SSD-backed EBS volumes are designed for transactional, IOPS-intensive database workloads, boot volumes, and workloads that need high IOPS.
  scope: SSD-backed EBS volumes (io2 Block Express, io1, gp3, gp2).
  link: [transactional, IOPS-intensive database workloads, boot volumes](../facts/ebs.md#ebs-faq-ssd-workloads)
  link: [workloads that require high IOPS](../facts/ebs.md#ebs-faq-ssd-workloads)
ebs-faq-st1-500-instance-limit
  claim: st1 can drive throughput up to 500 MB/s, but performance is limited by the separate instance-level limit for EBS traffic.
  scope: per st1 volume; maximum; not adjustable; also limited by the instance-level limit for EBS traffic.
  link: [up to 500 MB/s](../facts/ebs.md#ebs-faq-st1-500-instance-limit)
  link: [the separate instance-level limit for EBS traffic](../facts/ebs.md#ebs-faq-st1-500-instance-limit)
ebs-faq-st1-sc1-scale-with-size
  claim: Performance of st1 and sc1 scales linearly with volume size, so striping these volumes may give less benefit.
  scope: st1 and sc1 volumes.
  link: [scales linearly with volume size](../facts/ebs.md#ebs-faq-st1-sc1-scale-with-size)
ebs-faq-standard-renamed-magnetic
  claim: EBS Standard volumes have been renamed to EBS Magnetic volumes.
  scope: EBS Standard (magnetic) volume type.
  link: [renamed to EBS Magnetic volumes](../facts/ebs.md#ebs-faq-standard-renamed-magnetic)
ebs-faq-stripe-prefer-io2
  claim: For higher performance needs, AWS recommends io2 Block Express volumes instead of the operational work of striping multiple volumes.
  scope: high-performance block storage for one instance; higher performance requirements.
  link: [We recommend using io2 Block Express volumes](../facts/ebs.md#ebs-faq-stripe-prefer-io2)
ebs-faq-volume-clone-source-unaffected
  claim: Creating a copy of a volume does not affect the performance of the source volume, during or after the copy.
  scope: source volume of a Volume Clones copy.
  link: [performance of the source volume is unaffected](../facts/ebs.md#ebs-faq-volume-clone-source-unaffected)
ebs-faq-volume-clones-same-az
  claim: Amazon EBS Volume Clones instantly create a copy of a volume within the same Availability Zone, giving fast access to point-in-time data with single-digit millisecond latency.
  scope: per EBS volume.
  link: [Amazon EBS Volume Clones](../facts/ebs.md#ebs-faq-volume-clones-same-az)
  link: [within the same Availability Zone](../facts/ebs.md#ebs-faq-volume-clones-same-az)
ebs-fsr-5-snapshots-per-region
  claim: You can enable up to 5 snapshots for fast snapshot restore per Region; the quota covers snapshots you own and snapshots shared with you, and a shared snapshot counts against your quota, not the owner's.
  scope: per account, per Region; default; adjustable; includes snapshots shared with you.
  link: [up to 5 snapshots](../facts/ebs.md#ebs-fsr-5-snapshots-per-region)
  say: up to five snapshots
ebs-fsr-billing-per-minute
  claim: Fast snapshot restore is billed for each minute it is enabled for a snapshot in a particular Availability Zone, pro-rated with a minimum of one hour.
  scope: per snapshot, per Availability Zone; minimum.
  link: [minimum of one hour](../facts/ebs.md#ebs-fsr-billing-per-minute)
  say: minimum of one hour
ebs-fsr-credit-bucket-per-snapshot-az
  claim: There is one volume creation credit bucket per snapshot per Availability Zone, and each volume created from a fast snapshot restore enabled snapshot consumes one credit.
  scope: per snapshot, per Availability Zone; fixed; with less than one credit, the volume is created without the benefit.
  link: [one credit bucket per snapshot per Availability Zone](../facts/ebs.md#ebs-fsr-credit-bucket-per-snapshot-az)
  say: one credit bucket per snapshot per Availability Zone
ebs-fsr-credit-example-128-gib
  claim: For a 128 GiB snapshot, the fast snapshot restore credit bucket holds at most 8 credits, so when the bucket is full you can create 8 initialized volumes at the same time.
  scope: per snapshot, per Availability Zone; maximum; not adjustable; example: 128 GiB snapshot; bucket size is MAX (1, MIN (10, 1024 ÷ snapshot size in GiB)).
  link: [8 initialized volumes simultaneously](../facts/ebs.md#ebs-fsr-credit-example-128-gib)
  say: eight initialized volumes simultaneously
ebs-fsr-dsu-hour-price
  claim: Fast snapshot restore is charged in DSU-hours for each snapshot and each Availability Zone where it is enabled; in US East (N. Virginia) one DSU-hour costs $0.75, billed per minute with a one-hour minimum.
  scope: per snapshot, per Availability Zone; US East (N. Virginia) example.
  link: [$0.75](../facts/ebs.md#ebs-fsr-dsu-hour-price)
  link: [one-hour minimum](../facts/ebs.md#ebs-fsr-dsu-hour-price)
  say: seventy-five cents per DSU-hour | one-hour minimum
ebs-fsr-full-benefit-performance
  claim: Volumes provisioned with up to 64,000 IOPS and 1,000 MiB/s throughput receive the full performance benefit of fast snapshot restore; for higher performance, AWS recommends initializing the volume.
  scope: per volume restored with fast snapshot restore; maximum; not adjustable; above these values, initialize the volume.
  link: [up to 64,000 IOPS](../facts/ebs.md#ebs-fsr-full-benefit-performance)
  link: [1,000 MiB/s throughput](../facts/ebs.md#ebs-fsr-full-benefit-performance)
  say: up to sixty-four thousand IOPS | one thousand mebibytes per second throughput
ebs-fsr-max-snapshot-size
  claim: Fast snapshot restore can be enabled only on snapshots with a size of 16 TiB or less.
  scope: per snapshot; maximum; not adjustable.
  link: [16 TiB or less](../facts/ebs.md#ebs-fsr-max-snapshot-size)
  say: sixteen TiB or less
ebs-fsr-optimize-60-minutes-per-tib
  claim: When fast snapshot restore is enabled for a snapshot, it takes 60 minutes per TiB to optimize the snapshot.
  scope: per snapshot; fixed; not adjustable.
  link: [60 minutes per TiB](../facts/ebs.md#ebs-fsr-optimize-60-minutes-per-tib)
  say: sixty minutes per TiB
ebs-fsr-price-example
  claim: In the guide's example, fast snapshot restore for one snapshot in one Availability Zone for 30 days costs $540 (720 hours at $0.75 per hour).
  scope: per snapshot, per Availability Zone, us-east-1 example; example values from the guide; check the pricing page for the Region.
  link: [$540](../facts/ebs.md#ebs-fsr-price-example)
  link: [$0.75](../facts/ebs.md#ebs-fsr-price-example)
  say: five hundred forty dollars | seventy-five cents per hour
ebs-fsr-volume-fully-initialized-at-creation
  claim: A volume created from a snapshot that is enabled for fast snapshot restore is fully initialized at creation and immediately delivers its full performance.
  scope: volumes created from FSR-enabled snapshots.
  link: [fully initialized at creation](../facts/ebs.md#ebs-fsr-volume-fully-initialized-at-creation)
  link: [immediately delivers its full performance](../facts/ebs.md#ebs-fsr-volume-fully-initialized-at-creation)
ebs-gp2-burst-3000-iops
  claim: gp2 volumes smaller than 1 TiB that are provisioned with less than 3,000 IOPS can burst to 3,000 IOPS when needed, for an extended period of time.
  scope: per gp2 volume; maximum; not adjustable; volume smaller than 1 TiB with baseline below 3,000 IOPS; governed by I/O credits.
  link: [burst to 3,000 IOPS](../facts/ebs.md#ebs-gp2-burst-3000-iops)
  link: [smaller than 1 TiB](../facts/ebs.md#ebs-gp2-burst-3000-iops)
  say: burst to three thousand IOPS | smaller than one TiB
ebs-gp2-credit-accrual-limit
  claim: A gp2 volume can hold at most 5.4 million I/O credits, enough to sustain the maximum burst of 3,000 IOPS for at least 30 minutes.
  scope: per gp2 volume; maximum; not adjustable.
  link: [5.4 million I/O credits](../facts/ebs.md#ebs-gp2-credit-accrual-limit)
  link: [at least 30 minutes](../facts/ebs.md#ebs-gp2-credit-accrual-limit)
  say: five point four million I/O credits | at least thirty minutes
ebs-gp2-credit-earn-rate
  claim: When I/O demand is at or below baseline, a gp2 volume earns I/O credits at 3 I/O credits per GiB of volume size per second.
  scope: per gp2 volume; fixed; not adjustable; while I/O demand is at or below baseline.
  link: [3 I/O credits per GiB of volume size per second](../facts/ebs.md#ebs-gp2-credit-earn-rate)
  say: three I/O credits per GiB per second
ebs-gp2-durability-afr
  claim: gp2 volumes are designed for 99.8 percent to 99.9 percent volume durability, with an annual failure rate no higher than 0.2 percent, and provide single-digit millisecond latency.
  scope: per gp2 volume, per year.
  link: [99.8 percent to 99.9 percent](../facts/ebs.md#ebs-gp2-durability-afr)
  link: [no higher than 0.2 percent](../facts/ebs.md#ebs-gp2-durability-afr)
  say: ninety-nine point eight to ninety-nine point nine percent | no higher than zero point two percent
ebs-gp2-initial-credit-balance
  claim: Each gp2 volume receives an initial I/O credit balance of 5.4 million I/O credits, which gives boot volumes a fast initial boot cycle.
  scope: per gp2 volume; default; not adjustable; at volume creation.
  link: [initial I/O credit balance of 5.4 million I/O credits](../facts/ebs.md#ebs-gp2-initial-credit-balance)
  say: initial balance of five point four million I/O credits
ebs-gp2-iops-per-gib
  claim: gp2 baseline IOPS scales linearly at 3 IOPS per GiB of volume size, between a minimum of 100 and a maximum of 16,000.
  scope: per gp2 volume; maximum; not adjustable; baseline IOPS depends on volume size.
  link: [3 IOPS per GiB](../facts/ebs.md#ebs-gp2-iops-per-gib)
  link: [minimum of 100](../facts/ebs.md#ebs-gp2-iops-per-gib)
  link: [maximum of 16,000](../facts/ebs.md#ebs-gp2-iops-per-gib)
  say: three IOPS per GiB | minimum of one hundred | maximum of sixteen thousand
ebs-gp2-max-iops-size
  claim: gp2 volumes of 5,334 GiB and larger are provisioned with 16,000 IOPS, the gp2 maximum.
  scope: per gp2 volume; maximum; not adjustable.
  link: [5,334 GiB and larger](../facts/ebs.md#ebs-gp2-max-iops-size)
  say: five thousand three hundred thirty-four GiB and larger
ebs-gp2-min-iops-small-volumes
  claim: gp2 volumes of 33.33 GiB and smaller are provisioned with the minimum of 100 IOPS.
  scope: per gp2 volume; minimum; not adjustable; volume size 33.33 GiB or smaller.
  link: [minimum of 100 IOPS](../facts/ebs.md#ebs-gp2-min-iops-small-volumes)
  say: minimum of one hundred IOPS
ebs-gp2-performance-scales-with-size
  claim: With gp2, performance scales with volume size: baseline IOPS grow linearly at 3 IOPS per GiB, from a minimum of 100 to a maximum of 16,000.
  scope: per gp2 volume; small gp2 volumes can also burst.
  link: [performance scales with volume size](../facts/ebs.md#ebs-gp2-performance-scales-with-size)
  link: [3 IOPS per GiB](../facts/ebs.md#ebs-gp2-performance-scales-with-size)
  say: three IOPS per gibibyte
ebs-gp2-size-range
  claim: A gp2 volume can range in size from 1 GiB to 16 TiB, and its performance scales linearly with its size.
  scope: per gp2 volume; maximum; not adjustable.
  link: [1 GiB to 16 TiB](../facts/ebs.md#ebs-gp2-size-range)
  say: one GiB to sixteen TiB
ebs-gp2-storage-price-example
  claim: In the pricing page example Region, gp2 storage costs $0.10 per GB-month, and I/O is included in the price of gp2 volumes.
  scope: per GB-month of gp2 storage; example Region rate.
  link: [$0.10 per GB-month](../facts/ebs.md#ebs-gp2-storage-price-example)
  say: ten cents per GB-month
ebs-gp2-throughput-170-gib
  claim: gp2 volumes of 170 GiB and smaller deliver a maximum throughput of 128 MiB/s.
  scope: per gp2 volume; maximum; not adjustable; volume size 170 GiB or smaller.
  link: [maximum throughput of 128 MiB/s](../facts/ebs.md#ebs-gp2-throughput-170-gib)
  say: maximum throughput of one hundred twenty-eight mebibytes per second
ebs-gp2-throughput-334-gib
  claim: gp2 volumes of 334 GiB and larger deliver 250 MiB/s of throughput.
  scope: per gp2 volume; maximum; not adjustable; volume size 334 GiB or larger.
  link: [334 GiB and larger](../facts/ebs.md#ebs-gp2-throughput-334-gib)
  link: [250 MiB/s](../facts/ebs.md#ebs-gp2-throughput-334-gib)
  say: three hundred thirty-four GiB and larger | two hundred fifty mebibytes per second
ebs-gp2-throughput-range
  claim: gp2 volumes deliver throughput between 128 MiB/s and 250 MiB/s, depending on the volume size.
  scope: per gp2 volume; maximum; not adjustable; depends on volume size.
  link: [between 128 MiB/s and 250 MiB/s](../facts/ebs.md#ebs-gp2-throughput-range)
  say: between one hundred twenty-eight and two hundred fifty mebibytes per second
ebs-gp3-20-percent-lower-price
  claim: gp3 volumes have a 20 percent lower price per GiB than gp2 volumes.
  scope: price per GiB, gp3 compared with gp2.
  link: [20 percent lower price per GiB](../facts/ebs.md#ebs-gp3-20-percent-lower-price)
  say: twenty percent lower price per GiB
ebs-gp3-baseline-iops
  claim: Every gp3 volume gets a consistent baseline of 3,000 IOPS, and this baseline is included in the price of storage.
  scope: per gp3 volume; default; adjustable; more IOPS can be provisioned for an additional cost.
  link: [3,000 IOPS](../facts/ebs.md#ebs-gp3-baseline-iops)
  say: three thousand IOPS
ebs-gp3-baseline-throughput
  claim: Every gp3 volume gets a consistent baseline throughput of 125 MiB/s, included in the price of storage.
  scope: per gp3 volume; default; adjustable; more throughput can be provisioned for an additional cost.
  link: [125 MiB/s](../facts/ebs.md#ebs-gp3-baseline-throughput)
  say: one hundred twenty-five mebibytes per second
ebs-gp3-console-default-type
  claim: When you use the console to create a volume or to create an AMI from a snapshot, gp3 is the default volume type; in other cases gp2 is the default selection.
  scope: volume creation and AMI creation from a snapshot; default; adjustable; console: gp3; other cases: gp2.
  link: [the default selection for volume type](../facts/ebs.md#ebs-gp3-console-default-type)
  link: [gp2 is the default selection](../facts/ebs.md#ebs-gp3-console-default-type)
  say: the default selection for volume type | gp2 is the default selection
ebs-gp3-durability-afr
  claim: gp3 volumes are designed for 99.8 percent to 99.9 percent volume durability, with an annual failure rate no higher than 0.2 percent (at most two volume failures per 1,000 running volumes in a year).
  scope: per gp3 volume, per year.
  link: [99.8 percent to 99.9 percent](../facts/ebs.md#ebs-gp3-durability-afr)
  link: [no higher than 0.2 percent](../facts/ebs.md#ebs-gp3-durability-afr)
  say: ninety-nine point eight to ninety-nine point nine percent | no higher than zero point two percent
ebs-gp3-iops-price-example
  claim: In the pricing page example Region, gp3 IOPS above the free baseline cost $0.005 per provisioned IOPS-month.
  scope: per provisioned IOPS-month above 3,000; example Region rate.
  link: [$0.005 per provisioned IOPS-month](../facts/ebs.md#ebs-gp3-iops-price-example)
  say: half a cent per provisioned IOPS-month
ebs-gp3-latency
  claim: gp3 volumes provide single-digit millisecond latency.
  scope: per gp3 volume.
  link: [single-digit millisecond latency](../facts/ebs.md#ebs-gp3-latency)
  say: single-digit millisecond latency
ebs-gp3-lowest-cost-ssd
  claim: gp3 is the latest generation of General Purpose SSD and the lowest cost SSD volume type that EBS offers.
  scope: among EBS SSD volume types.
  link: [the lowest cost SSD volume](../facts/ebs.md#ebs-gp3-lowest-cost-ssd)
ebs-gp3-max-iops-80000
  claim: A gp3 volume can be provisioned with up to 80,000 IOPS, at a ratio of 500 IOPS per GiB, so the maximum needs a volume of 160 GiB or larger. Before September 26, 2025 the maximum was 16,000 IOPS.
  scope: per gp3 volume; maximum; not adjustable; additional IOPS above the 3,000 IOPS baseline cost extra; outside AWS Outposts.
  link: [80,000](../facts/ebs.md#ebs-gp3-max-iops-80000)
  link: [500 IOPS per GiB](../facts/ebs.md#ebs-gp3-max-iops-80000)
  link: [160 GiB or larger](../facts/ebs.md#ebs-gp3-max-iops-80000)
  link: [16,000 IOPS](../facts/ebs.md#ebs-gp3-max-iops-80000)
  say: eighty thousand | five hundred IOPS per gibibyte | one hundred sixty gibibytes or larger | sixteen thousand IOPS
  changed: 2025-09-26: was the previous 16,000 IOPS limit
ebs-gp3-max-iops-min-size
  claim: The maximum gp3 IOPS can be provisioned only for volumes of 160 GiB or larger (500 IOPS per GiB × 160 GiB = 80,000 IOPS).
  scope: per gp3 volume; minimum; not adjustable; to provision the maximum IOPS.
  link: [160 GiB or larger](../facts/ebs.md#ebs-gp3-max-iops-min-size)
  say: one hundred sixty GiB or larger
ebs-gp3-max-size-64-tib
  claim: A gp3 volume can range in size from 1 GiB to 64 TiB. Before September 26, 2025 the maximum size was 16 TiB.
  scope: per gp3 volume; maximum; not adjustable; outside AWS Outposts.
  link: [64 TiB](../facts/ebs.md#ebs-gp3-max-size-64-tib)
  link: [1 GiB](../facts/ebs.md#ebs-gp3-max-size-64-tib)
  link: [16 TiB](../facts/ebs.md#ebs-gp3-max-size-64-tib)
  say: sixty-four tebibytes | one gibibyte | sixteen tebibytes
  changed: 2025-09-26: was the previous 16 TiB limit
ebs-gp3-max-throughput-2000
  claim: A gp3 volume can be provisioned with up to 2,000 MiB/s of throughput, at a ratio of 0.25 MiB/s per provisioned IOPS. Before September 26, 2025 the maximum was 1,000 MiB/s.
  scope: per gp3 volume; maximum; not adjustable; throughput above the 125 MiB/s baseline costs extra; outside AWS Outposts.
  link: [2,000 MiB/s](../facts/ebs.md#ebs-gp3-max-throughput-2000)
  link: [0.25 MiB/s per provisioned IOPS](../facts/ebs.md#ebs-gp3-max-throughput-2000)
  link: [1,000 MiB/s](../facts/ebs.md#ebs-gp3-max-throughput-2000)
  say: two thousand mebibytes per second | a quarter mebibyte per second per provisioned IOPS | one thousand mebibytes per second
  changed: 2025-09-26: was the previous 1,000 MiB/s limit
ebs-gp3-max-throughput-requirements
  claim: The maximum gp3 throughput can be provisioned at 8,000 IOPS or higher and on volumes of 16 GiB or larger.
  scope: per gp3 volume; minimum; not adjustable; to provision the maximum throughput.
  link: [8,000 IOPS or higher](../facts/ebs.md#ebs-gp3-max-throughput-requirements)
  link: [16 GiB or larger](../facts/ebs.md#ebs-gp3-max-throughput-requirements)
  say: eight thousand IOPS or higher | sixteen GiB or larger
ebs-gp3-outposts-limits
  claim: On AWS Outposts, gp3 volumes support sizes up to 16 TiB, IOPS up to 16,000, and throughput up to 1,000 MiB/s.
  scope: per gp3 volume on Outposts; maximum; not adjustable; on Outposts only.
  link: [up to 16 TiB](../facts/ebs.md#ebs-gp3-outposts-limits)
  link: [IOPS up to 16,000](../facts/ebs.md#ebs-gp3-outposts-limits)
  link: [up to 1,000 MiB/s](../facts/ebs.md#ebs-gp3-outposts-limits)
  say: up to sixteen TiB | IOPS up to sixteen thousand | up to one thousand mebibytes per second
ebs-gp3-performance-99-percent
  claim: AWS designs gp3 volumes to deliver their provisioned performance 99 percent of the time.
  scope: per gp3 volume.
  link: [99 percent of the time](../facts/ebs.md#ebs-gp3-performance-99-percent)
  say: ninety-nine percent of the time
ebs-gp3-performance-independent-of-size
  claim: With gp3 you scale volume performance independently of volume size, so you can provision the performance you need without provisioning extra storage capacity.
  scope: per gp3 volume; within the gp3 IOPS-per-GiB ratio.
  link: [independently of volume size](../facts/ebs.md#ebs-gp3-performance-independent-of-size)
  link: [without needing to provision additional block storage capacity](../facts/ebs.md#ebs-gp3-performance-independent-of-size)
ebs-gp3-performance-price-volume-types-page
  claim: The volume types page lists gp3 performance pricing as 3,000 IOPS free and $0.005 per provisioned IOPS-month above 3,000 IOPS, and 125 MB/s free and $0.04 per provisioned MB/s-month above 125 MiBps.
  scope: per gp3 volume, above the free baseline; the pricing page example uses $0.06 for throughput.
  link: [$0.005/provisioned IOPS-month over 3,000 IOPS](../facts/ebs.md#ebs-gp3-performance-price-volume-types-page)
  link: [$0.04/provisioned MB/s-month over 125 MiBps](../facts/ebs.md#ebs-gp3-performance-price-volume-types-page)
  say: half a cent per provisioned IOPS-month over three thousand | four cents per provisioned MB per second per month over one hundred twenty-five
ebs-gp3-storage-price-example
  claim: In the pricing page example Region, gp3 storage costs $0.08 per GB-month.
  scope: per GB-month of gp3 storage; example Region rate; varies by Region.
  link: [$0.08 per GB-month](../facts/ebs.md#ebs-gp3-storage-price-example)
  say: eight cents per GB-month
ebs-gp3-throughput-price-pricing-page
  claim: The pricing page example charges $0.06 per provisioned MB/s-month for gp3 throughput above the free baseline.
  scope: per provisioned MB/s-month above 125; example Region rate; the volume types page lists $0.04.
  link: [$0.06 per provisioned MB/s-month](../facts/ebs.md#ebs-gp3-throughput-price-pricing-page)
  say: six cents per provisioned MB per second per month
ebs-gp3-use-cases
  claim: AWS lists virtual desktops, medium-sized single-instance databases, low-latency interactive apps, dev and test, and boot volumes as gp3 use cases.
  scope: gp3 volumes.
  link: [medium sized single instance databases](../facts/ebs.md#ebs-gp3-use-cases)
  link: [boot volumes](../facts/ebs.md#ebs-gp3-use-cases)
ebs-gpt-boot-volume-64-tib
  claim: With the GPT partitioning scheme, boot volumes can be up to 64 TiB in size when used with GRUB2 (Linux) or UEFI boot mode (Windows).
  scope: per boot volume; maximum; not adjustable; GPT partitioning with GRUB2 (Linux) or UEFI boot mode (Windows).
  link: [up to 64 TiB in size](../facts/ebs.md#ebs-gpt-boot-volume-64-tib)
  say: up to sixty-four TiB in size
ebs-hdd-io-counted-as-1-mib
  claim: On st1 and sc1 volumes, an I/O request of 1 MiB or less counts as a 1 MiB I/O credit, but sequential I/Os are merged into 1 MiB I/O blocks and count only as one 1 MiB I/O credit.
  scope: per st1 or sc1 volume; fixed; sequential I/Os are merged.
  link: [1 MiB or less counts as a 1 MiB I/O credit](../facts/ebs.md#ebs-hdd-io-counted-as-1-mib)
  say: one MiB or less counts as a one MiB I/O credit
ebs-hdd-large-sequential-not-small-random
  claim: st1 and sc1 volumes are optimized for large, sequential I/O; for small, random I/O AWS recommends General Purpose SSD or Provisioned IOPS SSD volumes instead.
  scope: st1 and sc1 volumes.
  link: [large, sequential I/O](../facts/ebs.md#ebs-hdd-large-sequential-not-small-random)
  link: [discouraging workloads with small, random I/O](../facts/ebs.md#ebs-hdd-large-sequential-not-small-random)
ebs-hdd-performance-in-throughput-not-iops
  claim: Throughput Optimized HDD (st1) and Cold HDD (sc1) volumes are low-cost magnetic storage that defines performance in terms of throughput rather than IOPS.
  scope: st1 and sc1 volumes.
  link: [in terms of throughput rather than IOPS](../facts/ebs.md#ebs-hdd-performance-in-throughput-not-iops)
  link: [low-cost magnetic storage](../facts/ebs.md#ebs-hdd-performance-in-throughput-not-iops)
ebs-hdd-throughput-consistency
  claim: Both st1 and sc1 are designed for performance consistency of 90 percent of burst throughput 99 percent of the time.
  scope: per st1 or sc1 volume.
  link: [90 percent of burst throughput 99 percent of the time](../facts/ebs.md#ebs-hdd-throughput-consistency)
  say: ninety percent of burst throughput ninety-nine percent of the time
ebs-hdd-volumes-not-bootable
  claim: Throughput Optimized HDD (st1) and Cold HDD (sc1) volumes cannot be boot volumes.
  scope: st1 and sc1 volumes.
  link: [Bootable st1 volumes are not supported](../facts/ebs.md#ebs-hdd-volumes-not-bootable)
  link: [Bootable sc1 volumes are not supported](../facts/ebs.md#ebs-hdd-volumes-not-bootable)
ebs-instance-performance-bounded-by-smaller
  claim: An instance's EBS performance is bounded by the instance type's performance limits or by the combined performance of its attached volumes, whichever is smaller.
  scope: per instance.
  link: [whichever is smaller](../facts/ebs.md#ebs-instance-performance-bounded-by-smaller)
  link: [bounded by the instance type's performance limits](../facts/ebs.md#ebs-instance-performance-bounded-by-smaller)
ebs-io-merge-and-split
  claim: When small I/O operations are physically sequential, EBS attempts to merge them into a single I/O operation up to the maximum I/O size; when I/O operations are larger than the maximum I/O size, EBS attempts to split them into smaller I/O operations.
  scope: per EBS volume; physically sequential small I/O.
  link: [merge them into a single I/O operation](../facts/ebs.md#ebs-io-merge-and-split)
  say: merge them into a single I/O operation
ebs-io-performance-status-check-io1-io2-gp3
  claim: The I/O performance status check compares actual volume performance to expected performance and is available only for io1, io2 and gp3 volumes attached to an instance.
  scope: EBS volume status checks; volume attached to an instance.
  link: [compares actual volume performance to the expected performance](../facts/ebs.md#ebs-io-performance-status-check-io1-io2-gp3)
  link: [Provisioned IOPS SSD (io1 and io2) and General Purpose SSD (gp3)](../facts/ebs.md#ebs-io-performance-status-check-io1-io2-gp3)
ebs-io-size-cap-ssd-hdd
  claim: For counting IOPS, the I/O size is capped at 256 KiB for SSD volumes and 1,024 KiB for HDD volumes.
  scope: per I/O operation, by volume family; maximum; not adjustable.
  link: [256 KiB for SSD volumes](../facts/ebs.md#ebs-io-size-cap-ssd-hdd)
  link: [1,024 KiB for HDD volumes](../facts/ebs.md#ebs-io-size-cap-ssd-hdd)
  say: two hundred fifty-six KiB for SSD volumes | one thousand twenty-four KiB for HDD volumes
ebs-io-storage-price-example
  claim: In the pricing page example for io2 volumes, the example Region charges $0.125 per GB-month for storage.
  scope: per GB-month of io2 storage; example Region rate on the pricing page.
  link: [$0.125 per GB-month](../facts/ebs.md#ebs-io-storage-price-example)
  say: twelve and a half cents per GB-month
ebs-io1-all-instance-types
  claim: io1 volumes are available for all Amazon EC2 instance types.
  scope: io1 volumes.
  link: [available for all Amazon EC2 instance types](../facts/ebs.md#ebs-io1-all-instance-types)
  link: [all Amazon EC2 instance types](../facts/ebs.md#ebs-io1-all-instance-types)
ebs-io1-durability-afr
  claim: io1 volumes are designed for 99.8 percent to 99.9 percent volume durability, with an annual failure rate no higher than 0.2 percent.
  scope: per io1 volume, per year.
  link: [99.8 percent to 99.9 percent](../facts/ebs.md#ebs-io1-durability-afr)
  link: [no higher than 0.2 percent](../facts/ebs.md#ebs-io1-durability-afr)
  say: ninety-nine point eight to ninety-nine point nine percent | no higher than zero point two percent
ebs-io1-iops-ratio
  claim: The maximum ratio of provisioned IOPS to volume size for io1 is 50:1; for example, a 100 GiB io1 volume can be provisioned with up to 5,000 IOPS.
  scope: per io1 volume; maximum; not adjustable.
  link: [50:1](../facts/ebs.md#ebs-io1-iops-ratio)
  say: fifty to one
ebs-io1-max-iops-min-size
  claim: The maximum io1 IOPS can be provisioned for volumes of 1,280 GiB or larger (50 × 1,280 GiB = 64,000 IOPS).
  scope: per io1 volume; minimum; not adjustable; to provision the maximum IOPS.
  link: [1,280 GiB or larger](../facts/ebs.md#ebs-io1-max-iops-min-size)
  say: one thousand two hundred eighty GiB or larger
ebs-io1-max-throughput
  claim: To achieve the io1 maximum throughput of 1,000 MiB/s, a volume must be provisioned with 64,000 IOPS (16 KiB per provisioned IOPS).
  scope: per io1 volume; maximum; not adjustable; provisioned with 64,000 IOPS; attached to a Nitro-based instance.
  link: [1,000 MiB/s](../facts/ebs.md#ebs-io1-max-throughput)
  say: one thousand mebibytes per second
ebs-io1-nitro-iops-limit
  claim: An io1 volume can achieve up to 64,000 IOPS only on Nitro-based instances; on other instances it can achieve up to 32,000 IOPS.
  scope: per io1 volume, by instance type; maximum; Nitro-based instance versus other instances.
  link: [up to 64,000 IOPS only on](../facts/ebs.md#ebs-io1-nitro-iops-limit)
  link: [up to 32,000 IOPS](../facts/ebs.md#ebs-io1-nitro-iops-limit)
  say: up to sixty-four thousand IOPS only on Nitro-based instances | up to thirty-two thousand IOPS
ebs-io1-size-and-iops-range
  claim: An io1 volume can range in size from 4 GiB to 16 TiB and can be provisioned with 100 IOPS up to 64,000 IOPS.
  scope: per io1 volume; maximum; not adjustable.
  link: [4 GiB to 16 TiB](../facts/ebs.md#ebs-io1-size-and-iops-range)
  link: [up to 64,000 IOPS per volume](../facts/ebs.md#ebs-io1-size-and-iops-range)
  say: four GiB to sixteen TiB | up to sixty-four thousand IOPS per volume
ebs-io1-throughput-up-to-32000-iops
  claim: io1 volumes provisioned with up to 32,000 IOPS support a maximum I/O size of 256 KiB and yield as much as 500 MiB/s of throughput.
  scope: per io1 volume; maximum; not adjustable; provisioned with up to 32,000 IOPS.
  link: [as much as 500 MiB/s](../facts/ebs.md#ebs-io1-throughput-up-to-32000-iops)
  link: [maximum I/O size of 256 KiB](../facts/ebs.md#ebs-io1-throughput-up-to-32000-iops)
  say: as much as five hundred mebibytes per second | maximum I/O size of two hundred fifty-six KiB
ebs-io2-durability-afr
  claim: io2 Block Express volumes are designed for 99.999 percent volume durability, with an annual failure rate no higher than 0.001 percent (a single volume failure per 100,000 running volumes in a year).
  scope: per io2 Block Express volume, per year.
  link: [99.999 percent volume durability](../facts/ebs.md#ebs-io2-durability-afr)
  link: [no higher than 0.001 percent](../facts/ebs.md#ebs-io2-durability-afr)
  say: ninety-nine point nine nine nine percent volume durability | no higher than zero point zero zero one percent
ebs-io2-iops-price-tiers
  claim: io2 provisioned IOPS are priced in tiers per volume: in the example Region, $0.065 per provisioned IOPS-month for the first 32,000 IOPS and $0.046 from 32,001 to 64,000 IOPS; in an account enabled for io2 Block Express, IOPS above 64,000 are charged at the rate of the third tier.
  scope: per io2 volume; tiering is applied per volume; example Region rates.
  link: [$0.065 per provisioned IOPS-month for the first 32,000 IOPS](../facts/ebs.md#ebs-io2-iops-price-tiers)
  link: [$0.046 per provisioned IOPS from 32,001 to 64,000 IOPS](../facts/ebs.md#ebs-io2-iops-price-tiers)
  say: six and a half cents per IOPS-month for the first thirty-two thousand | four point six cents from thirty-two thousand one to sixty-four thousand
ebs-io2-iops-tiering-per-volume
  claim: io2 IOPS price tiering is applied per volume, so ten io2 volumes of 1,000 IOPS each are all charged at the first-tier rate.
  scope: per io2 volume.
  link: [IOPS tiering is applied at a volume level](../facts/ebs.md#ebs-io2-iops-tiering-per-volume)
  say: IOPS tiering is applied at a volume level
ebs-io2-latency-under-500-microseconds
  claim: When attached to Nitro-based instances, io2 Block Express volumes are designed to deliver an average latency of under 500 microseconds for 16KiB I/O operations.
  scope: per io2 Block Express volume; attached to a Nitro-based instance; 16KiB I/O operations.
  link: [under 500 microseconds](../facts/ebs.md#ebs-io2-latency-under-500-microseconds)
  say: under five hundred microseconds
ebs-io2-max-iops-min-size
  claim: The maximum io2 Block Express IOPS can be provisioned on volumes of 256 GiB and larger (1,000 IOPS × 256 GiB = 256,000 IOPS).
  scope: per io2 Block Express volume; minimum; not adjustable; to provision the maximum IOPS.
  link: [256 GiB and larger](../facts/ebs.md#ebs-io2-max-iops-min-size)
  say: two hundred fifty-six GiB and larger
ebs-io2-max-iops-ratio
  claim: An io2 Block Express volume supports provisioned IOPS up to 256,000, with an IOPS:GiB ratio of 1,000:1.
  scope: per io2 Block Express volume; maximum; not adjustable; 256,000 IOPS is achievable only on Nitro-based instances.
  link: [up to 256,000](../facts/ebs.md#ebs-io2-max-iops-ratio)
  link: [1,000:1](../facts/ebs.md#ebs-io2-max-iops-ratio)
  say: up to two hundred fifty-six thousand | one thousand to one
ebs-io2-max-size
  claim: An io2 Block Express volume has a storage capacity of up to 64 TiB (65,536 GiB).
  scope: per io2 Block Express volume; maximum; not adjustable.
  link: [up to 64 TiB](../facts/ebs.md#ebs-io2-max-size)
  say: up to sixty-four TiB
ebs-io2-max-throughput
  claim: An io2 Block Express volume delivers up to 4,000 MiB/s of throughput; throughput scales at 0.256 MiB/s per provisioned IOPS and reaches the maximum at 16,000 IOPS or higher.
  scope: per io2 Block Express volume; maximum; not adjustable; maximum reached at 16,000 IOPS or higher.
  link: [up to 4,000 MiB/s](../facts/ebs.md#ebs-io2-max-throughput)
  link: [0.256 MiB/s per provisioned IOPS](../facts/ebs.md#ebs-io2-max-throughput)
  say: up to four thousand mebibytes per second | zero point two five six mebibytes per second per provisioned IOPS
ebs-io2-nitro-iops-limit
  claim: Nitro-based instances support io2 volumes provisioned with up to 256,000 IOPS; other instance types can attach volumes provisioned with up to 64,000 IOPS but can achieve up to 32,000 IOPS.
  scope: per io2 volume, by instance type; maximum; Nitro-based instance versus other instance types.
  link: [up to 256,000 IOPS](../facts/ebs.md#ebs-io2-nitro-iops-limit)
  link: [up to 64,000 IOPS](../facts/ebs.md#ebs-io2-nitro-iops-limit)
  link: [up to 32,000 IOPS](../facts/ebs.md#ebs-io2-nitro-iops-limit)
  say: up to two hundred fifty-six thousand IOPS | up to sixty-four thousand IOPS | up to thirty-two thousand IOPS
ebs-io2-outlier-latency
  claim: io2 Block Express volumes have better outlier latency than General Purpose volumes, reducing the frequency of I/Os that exceed 800 microseconds by over 10 times.
  scope: io2 Block Express compared with gp2 and gp3.
  link: [exceeding 800 microseconds by over 10 times](../facts/ebs.md#ebs-io2-outlier-latency)
  say: exceeding eight hundred microseconds by over ten times
ebs-io2-use-cases
  claim: io2 Block Express suits workloads that need one volume with consistent sub-millisecond latency and higher IOPS and throughput than gp3, such as I/O-intensive relational and NoSQL databases.
  scope: io2 Block Express volumes.
  link: [consistent sub-millisecond latency](../facts/ebs.md#ebs-io2-use-cases)
  link: [higher IOPS and throughput than gp3 volumes](../facts/ebs.md#ebs-io2-use-cases)
  link: [I/O-intensive NoSQL & relational databases](../facts/ebs.md#ebs-io2-use-cases)
ebs-magnetic-previous-generation
  claim: Magnetic (standard) volumes are a previous generation type that deliver approximately 100 IOPS on average, with bursts of up to hundreds of IOPS, and range in size from 1 GiB to 1 TiB.
  scope: per Magnetic (standard) volume; maximum; not adjustable; previous generation.
  link: [approximately 100 IOPS on average](../facts/ebs.md#ebs-magnetic-previous-generation)
  link: [1 GiB to 1 TiB](../facts/ebs.md#ebs-magnetic-previous-generation)
  say: approximately one hundred IOPS on average | one GiB to one TiB
ebs-magnetic-standard-is-previous-generation
  claim: Magnetic (standard) volumes are previous generation volumes backed by magnetic drives; AWS recommends a current generation type when you need higher or more consistent performance.
  scope: Magnetic (standard) volumes.
  link: [previous generation volumes](../facts/ebs.md#ebs-magnetic-standard-is-previous-generation)
  link: [backed by magnetic drives](../facts/ebs.md#ebs-magnetic-standard-is-previous-generation)
ebs-manual-initialization-read-all-blocks
  claim: To initialize a restored volume manually on Linux, you read all of its blocks with the dd or fio utilities.
  scope: volumes created from snapshots, Linux.
  link: [read all of the blocks on the device](../facts/ebs.md#ebs-manual-initialization-read-all-blocks)
  link: [Use the dd or fio utilities](../facts/ebs.md#ebs-manual-initialization-read-all-blocks)
ebs-max-volume-size-64-tib
  claim: EBS supports a maximum volume size of 64 TiB, but whether the operating system recognizes all of that capacity depends on its design and on how the volume is partitioned.
  scope: per EBS volume; maximum; not adjustable; usable size depends on the OS, file system and partitioning scheme.
  link: [maximum volume size of 64 TiB](../facts/ebs.md#ebs-max-volume-size-64-tib)
  say: maximum volume size of sixty-four TiB
ebs-mbr-boot-volume-2-tib
  claim: With the MBR partitioning scheme, boot volumes are limited to 2 TiB in size.
  scope: per boot volume; maximum; not adjustable; MBR partitioning.
  link: [limited to 2 TiB](../facts/ebs.md#ebs-mbr-boot-volume-2-tib)
  say: limited to two TiB
ebs-metric-volume-iops-exceeded-check
  claim: The CloudWatch metric VolumeIOPSExceededCheck reports whether an application consistently tried to drive more IOPS than the volume's provisioned IOPS within the last minute; it is supported for volumes (except magnetic) attached to Nitro instances and not for Multi-Attach enabled volumes.
  scope: EBS volumes attached to Nitro instances; not magnetic, not Multi-Attach enabled.
  link: [VolumeIOPSExceededCheck](../facts/ebs.md#ebs-metric-volume-iops-exceeded-check)
  link: [exceeds the volume's provisioned IOPS performance](../facts/ebs.md#ebs-metric-volume-iops-exceeded-check)
ebs-metric-volume-stalled-io-check
  claim: The CloudWatch metric VolumeStalledIOCheck, published for Nitro instances only, reports whether a volume passed or failed a stalled IO check in the last minute.
  scope: EBS volumes attached to Nitro instances; Nitro instances only.
  link: [VolumeStalledIOCheck](../facts/ebs.md#ebs-metric-volume-stalled-io-check)
  link: [passed or failed a stalled IO check](../facts/ebs.md#ebs-metric-volume-stalled-io-check)
ebs-modification-cannot-cancel
  claim: A volume modification request cannot be cancelled after it has been submitted.
  scope: EBS volume modification.
  link: [You can't cancel a volume modification request](../facts/ebs.md#ebs-modification-cannot-cancel)
  link: [after it has been submitted](../facts/ebs.md#ebs-modification-cannot-cancel)
ebs-modification-free-charged-new-config
  claim: Modifying a volume's configuration has no charge; you are charged for the new configuration from the moment the modification starts.
  scope: EBS volume modification.
  link: [There is no charge to modify the configuration](../facts/ebs.md#ebs-modification-free-charged-new-config)
  link: [after volume modification starts](../facts/ebs.md#ebs-modification-free-charged-new-config)
ebs-modification-size-effective-at-optimizing
  claim: A size increase takes effect once the volume modification reaches the optimizing state, which usually takes a few seconds.
  scope: EBS volume size increase.
  link: [reaches the optimizing state](../facts/ebs.md#ebs-modification-size-effective-at-optimizing)
  link: [which usually takes a few seconds](../facts/ebs.md#ebs-modification-size-effective-at-optimizing)
ebs-modify-duration-1-tib
  claim: Volume modifications run on a best-effort basis and take from a few minutes to a few hours; typically a 1-TiB volume can take up to six hours to be modified.
  scope: per volume modification; maximum; not adjustable; typical value for a 1-TiB volume; time does not scale linearly with size.
  link: [up to six hours](../facts/ebs.md#ebs-modify-duration-1-tib)
  say: up to six hours
ebs-modify-gp2-to-gp3-auto-performance
  claim: In the guide's example, a 500 GiB gp2 volume with 250 MiB/s and 1500 IOPS changed to gp3 without stated performance gets 3000 IOPS (the gp3 baseline) and 250 MiB/s (to match the source gp2 throughput).
  scope: per volume changed from gp2 to gp3; default; adjustable; IOPS and throughput not specified; EBS uses the higher of the source gp2 performance and the gp3 baseline.
  link: [3000 IOPS (baseline `gp3` IOPS)](../facts/ebs.md#ebs-modify-gp2-to-gp3-auto-performance)
  link: [250 MiB/s](../facts/ebs.md#ebs-modify-gp2-to-gp3-auto-performance)
  say: three thousand IOPS | two hundred fifty mebibytes per second
ebs-modify-wait-for-completed
  claim: After you start a volume modification, you must wait for it to reach the completed state before you can start another modification of the same volume.
  scope: per EBS volume.
  link: [reach the `completed` state](../facts/ebs.md#ebs-modify-wait-for-completed)
  say: reach the completed state
ebs-multi-attach-16-nitro-instances
  claim: A Multi-Attach enabled volume can be attached to up to 16 instances built on the Nitro System that are in the same Availability Zone.
  scope: per Multi-Attach enabled volume; maximum; not adjustable; Nitro-based instances in the same Availability Zone.
  link: [up to 16 instances](../facts/ebs.md#ebs-multi-attach-16-nitro-instances)
  say: up to sixteen instances
ebs-multi-attach-infrastructure-issue-all-instances
  claim: A Multi-Attach enabled volume with an issue at the EBS infrastructure layer is unavailable to all attached instances, while EC2 or network issues may affect only some of them.
  scope: Multi-Attach enabled volumes.
  link: [unavailable to all attached instances](../facts/ebs.md#ebs-multi-attach-infrastructure-issue-all-instances)
  link: [might impact only some attached instances](../facts/ebs.md#ebs-multi-attach-infrastructure-issue-all-instances)
ebs-multi-attach-io-fencing-write-ordering
  claim: Multi-Attach enabled io1 and io2 volumes support I/O fencing, but your applications must provide write ordering for the attached instances to keep the data consistent.
  scope: Multi-Attach enabled io1 and io2 volumes.
  link: [support I/O fencing](../facts/ebs.md#ebs-multi-attach-io-fencing-write-ordering)
  link: [Your applications must provide write ordering](../facts/ebs.md#ebs-multi-attach-io-fencing-write-ordering)
ebs-multi-attach-needs-clustered-file-system
  claim: Standard file systems such as XFS and EXT4 are not designed for simultaneous access by several instances; with Multi-Attach you should use a clustered file system.
  scope: Multi-Attach enabled volumes.
  link: [use a clustered file system](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system)
  link: [not designed to be accessed simultaneously](../facts/ebs.md#ebs-multi-attach-needs-clustered-file-system)
ebs-multi-attach-no-extra-charge
  claim: There is no additional charge for EBS Multi-Attach; you pay the standard charges of the io1 or io2 volume.
  scope: Multi-Attach enabled volumes.
  link: [There are no additional charges](../facts/ebs.md#ebs-multi-attach-no-extra-charge)
  link: [the standard charges that apply](../facts/ebs.md#ebs-multi-attach-no-extra-charge)
ebs-multi-attach-not-boot-volume
  claim: Multi-Attach enabled volumes cannot be created as boot volumes.
  scope: Multi-Attach enabled volumes.
  link: [can't be created as boot volumes](../facts/ebs.md#ebs-multi-attach-not-boot-volume)
  link: [Multi-Attach enabled volumes](../facts/ebs.md#ebs-multi-attach-not-boot-volume)
ebs-multi-attach-provisioned-iops-only
  claim: Multi-Attach is supported only on Provisioned IOPS SSD (io1 and io2) volumes.
  scope: per EBS volume type.
  link: [supported exclusively on](../facts/ebs.md#ebs-multi-attach-provisioned-iops-only)
  link: [Provisioned IOPS SSD (`io1` and `io2`) volumes](../facts/ebs.md#ebs-multi-attach-provisioned-iops-only)
  say: supported exclusively on io1 and io2 | Provisioned IOPS SSD io1 and io2 volumes
ebs-multi-attach-provisioned-iops-same-az
  claim: EBS Multi-Attach lets you attach a single Provisioned IOPS SSD (io1 or io2) volume to several instances in the same Availability Zone, and each attached instance has full read and write permission.
  scope: Multi-Attach enabled io1 and io2 volumes.
  link: [attach a single Provisioned IOPS SSD](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
  link: [in the same Availability Zone](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
  link: [full read and write permission](../facts/ebs.md#ebs-multi-attach-provisioned-iops-same-az)
ebs-multi-attach-shares-provisioned-performance
  claim: Each instance attached to a Multi-Attach volume can drive up to the volume's maximum provisioned performance, but the combined performance of all attached instances cannot exceed it.
  scope: Multi-Attach enabled volumes; maximum.
  link: [aggregate performance of all of the attached instances](../facts/ebs.md#ebs-multi-attach-shares-provisioned-performance)
  link: [can't exceed the volume's maximum provisioned performance](../facts/ebs.md#ebs-multi-attach-shares-provisioned-performance)
ebs-multi-attach-toggle-only-when-detached
  claim: You can't enable or disable Multi-Attach while the volume is attached to an instance, and Multi-Attach can't be enabled during instance launch using either the Amazon EC2 console or the RunInstances API.
  scope: Multi-Attach on io1 and io2 volumes; the volume must not be attached.
  link: [You can't enable or disable Multi-Attach](../facts/ebs.md#ebs-multi-attach-toggle-only-when-detached)
  link: [can't be enabled during instance launch](../facts/ebs.md#ebs-multi-attach-toggle-only-when-detached)
ebs-multi-attach-type-change-io1-io2-only
  claim: For a Multi-Attach enabled volume, the only supported type change is between io1 and io2, in either direction and even while attached.
  scope: Multi-Attach enabled volumes.
  link: [between io1 and io2 in either direction](../facts/ebs.md#ebs-multi-attach-type-change-io1-io2-only)
  link: [Other volume type changes are not supported](../facts/ebs.md#ebs-multi-attach-type-change-io1-io2-only)
ebs-multi-attach-windows-io2-only
  claim: Linux instances support Multi-Attach enabled io1 and io2 volumes; Windows instances support Multi-Attach enabled io2 volumes only.
  scope: Multi-Attach by operating system.
  link: [Windows instances support Multi-Attach enabled io2 volumes only](../facts/ebs.md#ebs-multi-attach-windows-io2-only)
  link: [Linux instances support Multi-Attach enabled io1 and io2 volumes](../facts/ebs.md#ebs-multi-attach-windows-io2-only)
ebs-multi-volume-snapshot-set-fails-together
  claim: If any one snapshot in a multi-volume snapshot set fails, all the other snapshots of the set enter the error state.
  scope: multi-volume EBS snapshot set.
  link: [the other snapshots enter the error state](../facts/ebs.md#ebs-multi-volume-snapshot-set-fails-together)
  link: [any one snapshot in the multi-volume snapshot set](../facts/ebs.md#ebs-multi-volume-snapshot-set-fails-together)
ebs-multi-volume-snapshots-crash-consistent
  claim: Multi-volume snapshots are point-in-time, data-coordinated and crash-consistent across the EBS volumes attached to an instance; by default they cover all attached volumes, and you can exclude the root volume or specific data volumes.
  scope: multi-volume EBS snapshots of one instance; default; all attached volumes unless you exclude some.
  link: [data coordinated, and crash-consistent snapshots](../facts/ebs.md#ebs-multi-volume-snapshots-crash-consistent)
  link: [exclude the root volume, or specific data volumes](../facts/ebs.md#ebs-multi-volume-snapshots-crash-consistent)
ebs-new-volume-needs-file-system
  claim: New volumes are raw block devices and need a file system before you can mount and use them; volumes created from snapshots likely already have one, and creating a new file system on top overwrites the data.
  scope: newly attached EBS volumes.
  link: [you must create a file system on them](../facts/ebs.md#ebs-new-volume-needs-file-system)
  link: [the operation overwrites your data](../facts/ebs.md#ebs-new-volume-needs-file-system)
ebs-no-automatic-backup-customer-creates-snapshots
  claim: AWS does not automatically back up EBS volume data; creating snapshots regularly, or automating them with Amazon Data Lifecycle Manager or AWS Backup, is the customer's responsibility.
  scope: EBS volumes.
  link: [does not automatically back up the data](../facts/ebs.md#ebs-no-automatic-backup-customer-creates-snapshots)
  link: [it is your responsibility to create EBS snapshots](../facts/ebs.md#ebs-no-automatic-backup-customer-creates-snapshots)
ebs-non-boot-2-tib-needs-gpt
  claim: Non-boot volumes of 2 TiB (2048 GiB) or larger must use a GPT partition table to access the entire volume.
  scope: per non-boot volume; fixed; to access the entire volume.
  link: [2 TiB (2048 GiB) or larger](../facts/ebs.md#ebs-non-boot-2-tib-needs-gpt)
  say: two TiB or larger
ebs-nvme-devices-on-nitro
  claim: On instances built on the Nitro System, EBS volumes are exposed as NVMe block devices; the device names the operating system uses can differ from, or come in a different order than, the names in the block device mapping.
  scope: EBS volumes on Nitro-based instances.
  link: [exposed as NVMe block devices](../facts/ebs.md#ebs-nvme-devices-on-nitro)
  link: [in a different order than you specified](../facts/ebs.md#ebs-nvme-devices-on-nitro)
  link: [can be different than the name](../facts/ebs.md#ebs-nvme-devices-on-nitro)
ebs-optimized-dedicated-bandwidth
  claim: EBS-optimized instances use an optimized configuration stack and provide additional, dedicated bandwidth for EBS I/O, which minimizes contention between EBS I/O and other traffic from the instance.
  scope: EBS-optimized instances.
  link: [dedicated bandwidth for Amazon EBS I/O](../facts/ebs.md#ebs-optimized-dedicated-bandwidth)
  link: [minimizing contention between Amazon EBS I/O](../facts/ebs.md#ebs-optimized-dedicated-bandwidth)
ebs-optimized-default-or-hourly-fee
  claim: Some instance types are EBS-optimized by default (nothing to enable, and disabling has no effect); other types optionally support EBS optimization, which you enable during or after launch for an additional hourly fee; some types do not support it.
  scope: per instance type; default; adjustable; depends on the instance type.
  link: [EBS-optimized by default](../facts/ebs.md#ebs-optimized-default-or-hourly-fee)
  link: [an additional hourly fee](../facts/ebs.md#ebs-optimized-default-or-hourly-fee)
ebs-piops-99-9-percent
  claim: Provisioned IOPS SSD volumes (io2 and io1) deliver their provisioned IOPS performance 99.9 percent of the time.
  scope: per Provisioned IOPS SSD volume.
  link: [99.9 percent of the time](../facts/ebs.md#ebs-piops-99-9-percent)
  say: ninety-nine point nine percent of the time
ebs-pricing-gp2-hdd-io-included
  claim: For gp2, st1 and sc1 volumes, I/O is included in the price, so you pay only for each GB of storage you provision.
  scope: gp2, st1 and sc1 volumes.
  link: [I/O is included in the price](../facts/ebs.md#ebs-pricing-gp2-hdd-io-included)
ebs-pricing-gp3-iops-throughput-billed-separately
  claim: gp3 includes 3,000 IOPS and 125 MB/s free; additional IOPS and throughput are provisioned independently and charged per IOPS-month and per MB/s-month.
  scope: per gp3 volume.
  link: [free baseline performance of 3,000 provisioned IOPS](../facts/ebs.md#ebs-pricing-gp3-iops-throughput-billed-separately)
  link: [IOPS per month and MB/s per month](../facts/ebs.md#ebs-pricing-gp3-iops-throughput-billed-separately)
  say: a free baseline of three thousand provisioned IOPS
ebs-pricing-io2-iops-tiered
  claim: The provisioned IOPS charges are tiered: as you provision higher IOPS on a single volume, the effective provisioned IOPS charges decrease, which makes it more economical to scale IOPS on a single volume; IOPS tiering is applied at the volume level.
  scope: per io2 volume; tiering applies at the volume level.
  link: [The provisioned IOPS charges are tiered](../facts/ebs.md#ebs-pricing-io2-iops-tiered)
  link: [more economical to scale IOPS](../facts/ebs.md#ebs-pricing-io2-iops-tiered)
ebs-pricing-snapshot-incremental-and-copy-transfer
  claim: For the first snapshot of a volume, EBS saves a full copy of the data to Amazon S3; for each incremental snapshot, only the changed part of the volume is saved. Copying EBS snapshots is charged for the data transferred across Regions.
  scope: per snapshot.
  link: [only the changed part](../facts/ebs.md#ebs-pricing-snapshot-incremental-and-copy-transfer)
  link: [charged for the data transferred across regions](../facts/ebs.md#ebs-pricing-snapshot-incremental-and-copy-transfer)
ebs-product-use-cases-databases-san
  claim: The EBS product page lists running relational or NoSQL databases (such as SAP HANA, Oracle, SQL Server, PostgreSQL, MySQL, Cassandra and MongoDB) and moving mid-range on-premises SAN workloads as main use cases.
  scope: Amazon EBS.
  link: [Deploy and scale your choice of databases](../facts/ebs.md#ebs-product-use-cases-databases-san)
  link: [storage area network (SAN) workloads](../facts/ebs.md#ebs-product-use-cases-databases-san)
ebs-provisioned-rate-charged-on-snapshot-data
  claim: With a volume initialization rate you pay a per-GiB rate for the selected initialization tier, based on the full snapshot data size, not the size of the volume.
  scope: per volume created with an initialization rate; the rate varies by Region.
  link: [based on the full snapshot data size](../facts/ebs.md#ebs-provisioned-rate-charged-on-snapshot-data)
ebs-provisioned-rate-overrides-fsr
  claim: If you specify a volume initialization rate and the snapshot is enabled for fast snapshot restore, EBS uses the specified rate instead of fast snapshot restore; to use fast snapshot restore, leave the rate out.
  scope: per volume created from a snapshot.
  link: [uses the specified rate instead](../facts/ebs.md#ebs-provisioned-rate-overrides-fsr)
ebs-quota-archived-snapshots-per-volume
  claim: By default, a volume can have 25 archived snapshots in each supported Region; the quota is adjustable.
  scope: per volume, per Region; default; adjustable.
  link: [Each supported Region: 25](../facts/ebs.md#ebs-quota-archived-snapshots-per-volume)
  say: twenty-five in each supported Region
ebs-quota-concurrent-copy-volume
  claim: By default, an account can run 5 concurrent copy volume operations in each Region; the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [Each supported Region: 5](../facts/ebs.md#ebs-quota-concurrent-copy-volume)
  say: five in each supported Region
ebs-quota-concurrent-snapshot-copies
  claim: At most 20 concurrent snapshot copies can run to a single destination Region; the quota is marked not adjustable.
  scope: per destination Region; default; not adjustable.
  link: [Each supported Region: 20](../facts/ebs.md#ebs-quota-concurrent-snapshot-copies)
  say: twenty in each supported Region
ebs-quota-concurrent-snapshots-gp3
  claim: A gp3 volume can have at most 5 concurrent snapshots; the quota is not adjustable.
  scope: per gp3 volume; maximum; not adjustable.
  link: [Each supported Region: 5](../facts/ebs.md#ebs-quota-concurrent-snapshots-gp3)
  say: five in each supported Region
ebs-quota-concurrent-snapshots-sc1
  claim: An sc1 volume can have at most 1 concurrent snapshot; the quota is not adjustable.
  scope: per sc1 volume; maximum; not adjustable.
  link: [Each supported Region: 1](../facts/ebs.md#ebs-quota-concurrent-snapshots-sc1)
  say: one in each supported Region
ebs-quota-concurrent-snapshots-st1
  claim: An st1 volume can have at most 1 concurrent snapshot; the quota is not adjustable.
  scope: per st1 volume; maximum; not adjustable.
  link: [Each supported Region: 1](../facts/ebs.md#ebs-quota-concurrent-snapshots-st1)
  say: one in each supported Region
ebs-quota-gp2-storage
  claim: By default, the total gp2 storage per Region is 50 TiB in each Region that the quota row lists by name (including us-east-1) and 300 TiB in each of the other supported Regions; the quota is adjustable.
  scope: per account, per Region, all gp2 volumes; default; adjustable.
  link: [us-east-1: 50](../facts/ebs.md#ebs-quota-gp2-storage)
  link: [Each of the other supported Regions: 300](../facts/ebs.md#ebs-quota-gp2-storage)
  say: fifty TiB in us-east-1 | three hundred TiB in the other Regions
ebs-quota-gp3-storage
  claim: By default, the total gp3 storage per Region is 300 TiB in each Region that the quota row lists by name and 50 TiB in each of the other supported Regions; the quota is adjustable.
  scope: per account, per Region, all gp3 volumes; default; adjustable; 300 TiB in the Regions listed in the row.
  link: [Each of the other supported Regions: 50](../facts/ebs.md#ebs-quota-gp3-storage)
  say: fifty TiB in each of the other supported Regions
ebs-quota-in-progress-archive-restores
  claim: By default, an account can have 5 in-progress snapshot restores from archive in each Region; the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [Each supported Region: 5](../facts/ebs.md#ebs-quota-in-progress-archive-restores)
  say: five in each supported Region
ebs-quota-in-progress-archives
  claim: By default, an account can have 25 in-progress snapshot archives in each Region; the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [Each supported Region: 25](../facts/ebs.md#ebs-quota-in-progress-archives)
  say: twenty-five in each supported Region
ebs-quota-io1-iops
  claim: By default, at most 300,000 IOPS can be provisioned in total across io1 volumes in a Region; the quota is adjustable.
  scope: per Region, per account, all io1 volumes; default; adjustable.
  link: [Each supported Region: 300,000](../facts/ebs.md#ebs-quota-io1-iops)
  say: three hundred thousand in each supported Region
ebs-quota-io2-iops
  claim: By default, at most 100,000 IOPS can be provisioned in total across io2 volumes in a Region; the quota is adjustable.
  scope: per Region, per account, all io2 volumes; default; adjustable.
  link: [Each supported Region: 100,000](../facts/ebs.md#ebs-quota-io2-iops)
  say: one hundred thousand in each supported Region
ebs-quota-io2-storage
  claim: By default, the total io2 storage is 20 TiB in each Region; the quota is adjustable.
  scope: per account, per Region, all io2 volumes; default; adjustable.
  link: [Each supported Region: 20](../facts/ebs.md#ebs-quota-io2-storage)
  say: twenty TiB in each supported Region
ebs-quota-snapshot-copies-via-support
  claim: The quota for concurrent snapshot copies per destination Region cannot be adjusted with Service Quotas, but you can request an increase by contacting AWS Support.
  scope: per account, per destination Region; default; adjustable; through AWS Support, not Service Quotas.
  link: [by contacting AWS Support](../facts/ebs.md#ebs-quota-snapshot-copies-via-support)
  say: by contacting AWS Support
ebs-quota-snapshots-per-region
  claim: By default, an account can have 100,000 snapshots in each Region; the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [Each supported Region: 100,000](../facts/ebs.md#ebs-quota-snapshots-per-region)
  say: one hundred thousand in each supported Region
ebs-quota-st1-storage
  claim: By default, the total st1 storage per Region is 50 TiB in each Region that the quota row lists by name (including us-east-1) and 300 TiB in each of the other supported Regions; the quota is adjustable.
  scope: per account, per Region, all st1 volumes; default; adjustable.
  link: [us-east-1: 50](../facts/ebs.md#ebs-quota-st1-storage)
  link: [Each of the other supported Regions: 300](../facts/ebs.md#ebs-quota-st1-storage)
  say: fifty TiB in us-east-1 | three hundred TiB in the other Regions
ebs-quota-startsnapshot-pending
  claim: An account can have at most 100 pending snapshots created with the StartSnapshot API in each Region; the quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [Each supported Region: 100](../facts/ebs.md#ebs-quota-startsnapshot-pending)
  say: one hundred in each supported Region
ebs-quota-time-based-copy-throughput
  claim: By default, time-based snapshot copy throughput is 2,000 MiB/sec per destination Region at account level; the quota is adjustable.
  scope: per account, per destination Region; default; adjustable.
  link: [Each supported Region: 2,000](../facts/ebs.md#ebs-quota-time-based-copy-throughput)
  say: two thousand MiB per second
ebs-quotas-auto-increase
  claim: EBS monitors your provisioned storage and IOPS usage in each Region and might automatically increase your quotas per Region based on usage; you can still request an increase ahead of planned usage.
  scope: per account, per Region.
  link: [might automatically increase your quotas](../facts/ebs.md#ebs-quotas-auto-increase)
  say: might automatically increase your quotas
ebs-raid-over-8-volumes-diminishing
  claim: For RAID configurations, arrays larger than 8 volumes might have diminished performance returns because of increased I/O overhead.
  scope: per RAID array of EBS volumes.
  link: [arrays larger than 8 volumes](../facts/ebs.md#ebs-raid-over-8-volumes-diminishing)
  say: arrays larger than eight volumes
ebs-raid0-more-than-one-volume
  claim: A RAID 0 array of EBS volumes gives a file system more performance than you can provision on a single EBS volume; adding a volume adds its throughput and IOPS.
  scope: RAID 0 across EBS volumes.
  link: [Creating a RAID 0 array](../facts/ebs.md#ebs-raid0-more-than-one-volume)
  link: [higher level of performance for a file system](../facts/ebs.md#ebs-raid0-more-than-one-volume)
ebs-raid0-one-volume-loss-loses-array
  claim: In a striped array, performance is limited to the worst-performing volume in the set, and the loss of a single volume in the set results in complete data loss for the array.
  scope: RAID 0 across EBS volumes.
  link: [complete data loss for the array](../facts/ebs.md#ebs-raid0-one-volume-loss-loses-array)
  link: [limited to the worst performing volume](../facts/ebs.md#ebs-raid0-one-volume-loss-loses-array)
ebs-raid1-not-recommended
  claim: RAID 1 is not recommended with EBS: it needs more EC2-to-EBS bandwidth because data is written to several volumes at once, and it gives no write performance improvement.
  scope: RAID on EBS volumes.
  link: [RAID 1 is also not recommended](../facts/ebs.md#ebs-raid1-not-recommended)
  link: [does not provide any write performance improvement](../facts/ebs.md#ebs-raid1-not-recommended)
ebs-raid5-raid6-not-recommended
  claim: RAID 5 and RAID 6 are not recommended for EBS because their parity write operations consume some of the IOPS available to the volumes.
  scope: RAID on EBS volumes.
  link: [RAID 5 and RAID 6 are not recommended](../facts/ebs.md#ebs-raid5-raid6-not-recommended)
  link: [parity write operations](../facts/ebs.md#ebs-raid5-raid6-not-recommended)
ebs-recommended-quick-access-long-term-persistence
  claim: The storage decision guide recommends Amazon EBS for data that must be quickly accessible and needs long-term persistence; block storage is direct-attached to a compute instance with low-latency access.
  scope: AWS storage decision guide, Amazon EBS.
  link: [quickly accessible and requires long-term persistence](../facts/ebs.md#ebs-recommended-quick-access-long-term-persistence)
  link: [direct-attached to a compute instance](../facts/ebs.md#ebs-recommended-quick-access-long-term-persistence)
ebs-recycle-bin-billed-same-rate
  claim: There are no additional charges for Recycle Bin and retention rules, but snapshots in the Recycle Bin are billed at the same rate as regular snapshots, and volumes at the same rate as regular volumes.
  scope: per resource in the Recycle Bin; EBS-backed AMIs in the Recycle Bin incur no additional charges.
  link: [billed at the same rate as regular snapshots](../facts/ebs.md#ebs-recycle-bin-billed-same-rate)
  say: billed at the same rate as regular snapshots
ebs-recycle-bin-expired-permanently-deleted
  claim: You can restore a resource from the Recycle Bin at any time before its retention period expires; after expiry, an unrestored resource is permanently deleted and can no longer be recovered.
  scope: Recycle Bin.
  link: [at any time before its retention period expires](../facts/ebs.md#ebs-recycle-bin-expired-permanently-deleted)
  link: [no longer available for recovery](../facts/ebs.md#ebs-recycle-bin-expired-permanently-deleted)
ebs-recycle-bin-needs-regional-retention-rules
  claim: Recycle Bin protects resources only after you create retention rules in each AWS Region where you want protection; a rule names the resource type, the rule type and the retention period.
  scope: Recycle Bin, per Region.
  link: [you must create retention rules](../facts/ebs.md#ebs-recycle-bin-needs-regional-retention-rules)
  link: [in the AWS Regions in which you want](../facts/ebs.md#ebs-recycle-bin-needs-regional-retention-rules)
ebs-recycle-bin-recovers-volumes-snapshots-amis
  claim: Recycle Bin lets you restore accidentally deleted EBS volumes, EBS snapshots and EBS-backed AMIs, which it keeps for a period you specify before deleting them permanently.
  scope: Recycle Bin; a matching retention rule exists.
  link: [EBS volumes, EBS snapshots, and EBS-backed AMIs](../facts/ebs.md#ebs-recycle-bin-recovers-volumes-snapshots-amis)
  link: [for a time period that you specify](../facts/ebs.md#ebs-recycle-bin-recovers-volumes-snapshots-amis)
ebs-recycle-bin-rule-lock
  claim: You can optionally lock Region-level retention rules, except Region-level rules that have exclusion tags; a locked rule can't be modified or deleted until you unlock it and wait for the unlock delay period to expire, and rules remain unlocked by default unless you explicitly lock them.
  scope: Recycle Bin Region-level retention rules; default; Region-level rules that have exclusion tags can't be locked.
  link: [A locked retention rule can't be modified](../facts/ebs.md#ebs-recycle-bin-rule-lock)
  link: [wait for the unlock delay period to expire](../facts/ebs.md#ebs-recycle-bin-rule-lock)
  link: [Retention rules remain unlocked by default](../facts/ebs.md#ebs-recycle-bin-rule-lock)
ebs-recycle-bin-snapshot-retention-range
  claim: A Recycle Bin retention rule can keep deleted EBS snapshots and EBS-backed AMIs for 1 to 365 days.
  scope: per Recycle Bin retention rule for snapshots or AMIs; maximum; not adjustable.
  link: [EBS snapshots and EBS-backed AMIs: 1 - 365 days](../facts/ebs.md#ebs-recycle-bin-snapshot-retention-range)
  say: one to three hundred sixty-five days
ebs-recycle-bin-tag-and-region-level-rules
  claim: Tag-level retention rules protect resources that carry at least one of the rule's tags; Region-level retention rules by default protect all resources of the type in the Region, even untagged ones, minus any exclusion tags.
  scope: Recycle Bin retention rules.
  link: [use resource tags to identify the resources](../facts/ebs.md#ebs-recycle-bin-tag-and-region-level-rules)
  link: [even if the resources are not tagged](../facts/ebs.md#ebs-recycle-bin-tag-and-region-level-rules)
ebs-recycle-bin-unlock-delay
  claim: When you lock a Region-level Recycle Bin retention rule on creation, you must specify an unlock delay period of 7 to 30 days; rules stay unlocked by default.
  scope: per locked Region-level retention rule; maximum; not adjustable; only when the rule is locked.
  link: [7 to 30 days](../facts/ebs.md#ebs-recycle-bin-unlock-delay)
  say: seven to thirty days
ebs-replace-root-encrypts-with-default-encryption
  claim: When root volume replacement uses an existing replacement volume and the original root volume is encrypted, the replacement must also be encrypted: you can move from an unencrypted volume to an encrypted one, but not from encrypted to unencrypted. When encryption by default is enabled in the Region, a replacement root volume that the task creates (from a snapshot or an AMI) is always encrypted, regardless of the encryption status of the snapshot or the AMI root volume.
  scope: root volume replacement; first part: an existing volume as the replacement; second part: a volume created by the task with encryption by default enabled in the current Region.
  link: [but not from encrypted to unencrypted](../facts/ebs.md#ebs-replace-root-encrypts-with-default-encryption)
  link: [is always encrypted, regardless of the encryption status](../facts/ebs.md#ebs-replace-root-encrypts-with-default-encryption)
ebs-replace-root-from-snapshot-keeps-attributes
  claim: When you replace a root volume from a snapshot, the replacement root volume gets the same type, size and delete on termination attributes as the original root volume.
  scope: root volume replacement from a snapshot or to the launch state.
  link: [same type, size, and delete on termination attributes](../facts/ebs.md#ebs-replace-root-from-snapshot-keeps-attributes)
  link: [as the original root volume](../facts/ebs.md#ebs-replace-root-from-snapshot-keeps-attributes)
ebs-replace-root-volume-running-instance
  claim: EC2 can replace the root EBS volume of a running instance while keeping instance store data, the non-root EBS volumes and the network configuration; the instance is rebooted automatically during the process and its RAM contents are erased.
  scope: root volume replacement.
  link: [replace the root Amazon EBS volume](../facts/ebs.md#ebs-replace-root-volume-running-instance)
  link: [Non-root Amazon EBS volumes remain attached](../facts/ebs.md#ebs-replace-root-volume-running-instance)
  link: [The instance is automatically rebooted](../facts/ebs.md#ebs-replace-root-volume-running-instance)
ebs-root-volume-cannot-change-to-hdd
  claim: A root volume of type io1, io2, gp2, gp3 or standard cannot be modified to an st1 or sc1 volume, even when it is detached.
  scope: root EBS volumes.
  link: [can't be modified to an st1 or sc1 volume](../facts/ebs.md#ebs-root-volume-cannot-change-to-hdd)
  link: [even if it is detached from the instance](../facts/ebs.md#ebs-root-volume-cannot-change-to-hdd)
ebs-sc1-1-tib-burst-and-baseline
  claim: For a 1-TiB sc1 volume, burst throughput is limited to 80 MiB/s and the credit bucket fills at 12 MiB/s.
  scope: per sc1 volume of 1 TiB; maximum; not adjustable; scales linearly with volume size.
  link: [80 MiB/s](../facts/ebs.md#ebs-sc1-1-tib-burst-and-baseline)
  link: [12 MiB/s](../facts/ebs.md#ebs-sc1-1-tib-burst-and-baseline)
  say: eighty mebibytes per second | twelve mebibytes per second
ebs-sc1-baseline-range
  claim: On sc1 volume sizes from 0.125 TiB to 16 TiB, baseline throughput varies from 1.5 MiB/s to a maximum of 192 MiB/s, reached at 16 TiB.
  scope: per sc1 volume; maximum; not adjustable; maximum reached at 16 TiB.
  link: [0.125 TiB to 16 TiB](../facts/ebs.md#ebs-sc1-baseline-range)
  link: [1.5 MiB/s to a maximum of 192 MiB/s](../facts/ebs.md#ebs-sc1-baseline-range)
  say: zero point one two five TiB to sixteen TiB | one point five to one hundred ninety-two mebibytes per second
ebs-sc1-burst-range
  claim: sc1 burst throughput varies from 10 MiB/s to a cap of 250 MiB/s, which is reached at 3.125 TiB.
  scope: per sc1 volume; maximum; not adjustable; cap reached at 3.125 TiB.
  link: [10 MiB/s to a cap of 250 MiB/s](../facts/ebs.md#ebs-sc1-burst-range)
  say: ten to two hundred fifty mebibytes per second
ebs-sc1-lowest-cost-per-gb
  claim: sc1 (Cold HDD) has the lowest cost per GB of all EBS volume types and suits less frequently accessed workloads with large, cold datasets.
  scope: among all EBS volume types.
  link: [the lowest cost per GB](../facts/ebs.md#ebs-sc1-lowest-cost-per-gb)
  link: [less frequently accessed workloads](../facts/ebs.md#ebs-sc1-lowest-cost-per-gb)
ebs-sc1-max-throughput
  claim: sc1 throughput is capped at a maximum of 250 MiB/s; after the burst bucket is depleted, throughput is limited to the baseline of 12 MiB/s per TiB.
  scope: per sc1 volume; maximum; not adjustable.
  link: [maximum of 250 MiB/s](../facts/ebs.md#ebs-sc1-max-throughput)
  link: [12 MiB/s per TiB](../facts/ebs.md#ebs-sc1-max-throughput)
  say: maximum of two hundred fifty mebibytes per second | twelve mebibytes per second per TiB
ebs-sc1-storage-price-example
  claim: In the pricing page example Region, sc1 storage costs $0.015 per GB-month.
  scope: per GB-month of sc1 storage; example Region rate.
  link: [$0.015 per GB-month](../facts/ebs.md#ebs-sc1-storage-price-example)
  say: one and a half cents per GB-month
ebs-sc1-use-cases
  claim: AWS lists colder data that needs fewer scans per day as the sc1 use case, a good fit for large, sequential cold-data workloads.
  scope: sc1 volumes.
  link: [Colder data requiring fewer scans per day](../facts/ebs.md#ebs-sc1-use-cases)
  link: [large, sequential cold-data workloads](../facts/ebs.md#ebs-sc1-use-cases)
ebs-shared-snapshot-recopy-with-own-key
  claim: For an encrypted snapshot shared with you, AWS recommends copying it with a KMS key that you own, so you keep access if the original key is compromised or the owner revokes your access.
  scope: encrypted snapshots shared with you; recommendation.
  link: [using a KMS key that you own](../facts/ebs.md#ebs-shared-snapshot-recopy-with-own-key)
  link: [if the owner revokes your access](../facts/ebs.md#ebs-shared-snapshot-recopy-with-own-key)
ebs-snapshot-and-volume-delete-independent
  claim: Deleting a snapshot has no effect on the volume, and deleting a volume has no effect on the snapshots made from it.
  scope: EBS volumes and snapshots.
  link: [Deleting a volume has no effect](../facts/ebs.md#ebs-snapshot-and-volume-delete-independent)
  link: [Deleting a snapshot has no effect](../facts/ebs.md#ebs-snapshot-and-volume-delete-independent)
ebs-snapshot-async-volume-usable-while-pending
  claim: Snapshot creation is asynchronous: the snapshot is created at once but stays pending until all data is transferred to Amazon S3, and you can keep using the volume during this time; the volume does not need to be unmounted.
  scope: EBS snapshot creation.
  link: [Snapshot creation is asynchronous](../facts/ebs.md#ebs-snapshot-async-volume-usable-while-pending)
  link: [continue to use the volume during this time](../facts/ebs.md#ebs-snapshot-async-volume-usable-while-pending)
  link: [while the volume is attached and in use](../facts/ebs.md#ebs-snapshot-async-volume-usable-while-pending)
ebs-snapshot-aws-managed-key-not-shareable
  claim: Snapshots encrypted with the default AWS managed key cannot be shared; only snapshots encrypted with a customer managed key can be shared.
  scope: encrypted EBS snapshots.
  link: [You can't share snapshots that are encrypted](../facts/ebs.md#ebs-snapshot-aws-managed-key-not-shareable)
  link: [encrypted with a customer managed key](../facts/ebs.md#ebs-snapshot-aws-managed-key-not-shareable)
ebs-snapshot-bpa-blocks-public-sharing-in-region
  claim: After you enable block public access for snapshots in a Region, any attempt to publicly share snapshots in that Region is automatically blocked.
  scope: per Region, per account.
  link: [automatically blocked](../facts/ebs.md#ebs-snapshot-bpa-blocks-public-sharing-in-region)
  link: [any attempt to publicly share snapshots](../facts/ebs.md#ebs-snapshot-bpa-blocks-public-sharing-in-region)
ebs-snapshot-bpa-declarative-policy
  claim: The block public access setting can be applied with a declarative policy across several Regions and accounts at once; while a declarative policy is in use, the setting cannot be changed directly in an account.
  scope: block public access for EBS snapshots.
  link: [by using a declarative policy](../facts/ebs.md#ebs-snapshot-bpa-declarative-policy)
  link: [you can't modify the setting directly](../facts/ebs.md#ebs-snapshot-bpa-declarative-policy)
ebs-snapshot-bpa-no-additional-cost
  claim: Block public access for snapshots can be enabled at no additional cost.
  scope: block public access for EBS snapshots.
  link: [at no additional cost](../facts/ebs.md#ebs-snapshot-bpa-no-additional-cost)
ebs-snapshot-bpa-not-private-or-ami-sharing
  claim: Block public access for snapshots does not prevent private snapshot sharing, and it does not prevent public sharing of EBS-backed AMIs (that needs block public access for AMIs).
  scope: block public access for EBS snapshots.
  link: [does not prevent private snapshot sharing](../facts/ebs.md#ebs-snapshot-bpa-not-private-or-ami-sharing)
  link: [public sharing of EBS-backed AMIs](../facts/ebs.md#ebs-snapshot-bpa-not-private-or-ami-sharing)
ebs-snapshot-bpa-regional-account-setting
  claim: Block public access for snapshots is a Regional, account-level setting: it applies to all snapshots in the Region where it is enabled and to all users of the account, so you enable it in each Region; it cannot be enabled at the organization level.
  scope: per Region, per account.
  link: [is a Regional setting](../facts/ebs.md#ebs-snapshot-bpa-regional-account-setting)
  link: [is an account-level setting](../facts/ebs.md#ebs-snapshot-bpa-regional-account-setting)
ebs-snapshot-bpa-two-modes
  claim: Block public access for snapshots has two modes: block all sharing (already public snapshots become private and are no longer publicly available) and block new sharing (only new public sharing is blocked; already public snapshots stay public).
  scope: block public access for EBS snapshots.
  link: [Blocks all public sharing of your snapshots](../facts/ebs.md#ebs-snapshot-bpa-two-modes)
  link: [Blocks only new public sharing](../facts/ebs.md#ebs-snapshot-bpa-two-modes)
ebs-snapshot-charged-by-data-not-volume-size
  claim: Snapshot charges are based on the size of the data being backed up, not the size of the source volume, and later snapshots of the same volume are charged only for changed and new data.
  scope: EBS snapshots.
  link: [the size of the data being backed up](../facts/ebs.md#ebs-snapshot-charged-by-data-not-volume-size)
  link: [not the size of the source volume](../facts/ebs.md#ebs-snapshot-charged-by-data-not-volume-size)
ebs-snapshot-consistency-pause-writes-or-unmount
  claim: For a consistent and complete snapshot, AWS recommends pausing writes to the volume first; if you cannot pause writes, unmount the volume inside the instance, and you can remount once the snapshot is pending.
  scope: EBS snapshot creation; recommendation, not a requirement.
  link: [pause writes to the volume](../facts/ebs.md#ebs-snapshot-consistency-pause-writes-or-unmount)
  link: [unmount the volume, from within the instance](../facts/ebs.md#ebs-snapshot-consistency-pause-writes-or-unmount)
ebs-snapshot-copy-cross-region-and-encrypt
  claim: You can copy snapshots from one Region to another, copy snapshots that are shared with you, and copy an unencrypted snapshot to an encrypted snapshot.
  scope: EBS snapshot copy; the source snapshot is in the completed state.
  link: [copy snapshots from one Region to another](../facts/ebs.md#ebs-snapshot-copy-cross-region-and-encrypt)
  link: [copy an unencrypted snapshot to an encrypted snapshot](../facts/ebs.md#ebs-snapshot-copy-cross-region-and-encrypt)
  link: [snapshots that are shared with you](../facts/ebs.md#ebs-snapshot-copy-cross-region-and-encrypt)
ebs-snapshot-copy-cross-region-charge
  claim: Copying EBS snapshots is charged for the data transferred across Regions, and standard snapshot storage charges then apply in the destination Region.
  scope: per cross-Region snapshot copy.
  link: [charged for the data transferred across regions](../facts/ebs.md#ebs-snapshot-copy-cross-region-charge)
  say: charged for the data transferred across Regions
ebs-snapshot-copy-encrypted-source-key-outcome
  claim: When encryption by default is disabled in the destination Region, a copy of an encrypted snapshot is automatically encrypted; you can specify the KMS key, and if you do not, the AWS managed key (aws/ebs) is used.
  scope: copy of an encrypted EBS snapshot; default; adjustable; encryption by default disabled for the destination Region; no KMS key specified.
  link: [Automatically encrypted](../facts/ebs.md#ebs-snapshot-copy-encrypted-source-key-outcome)
  link: [the AWS managed key (aws/ebs) is used](../facts/ebs.md#ebs-snapshot-copy-encrypted-source-key-outcome)
ebs-snapshot-copy-fsr-not-inherited
  claim: A copy of a snapshot that is enabled for fast snapshot restore is not automatically enabled for fast snapshot restore; you must enable it explicitly on the copy.
  scope: EBS snapshot copy.
  link: [not automatically enabled for fast snapshot restore](../facts/ebs.md#ebs-snapshot-copy-fsr-not-inherited)
  link: [You must explicitly enable fast snapshot restore](../facts/ebs.md#ebs-snapshot-copy-fsr-not-inherited)
ebs-snapshot-copy-new-kms-key-full-copy
  claim: Snapshot copies in the same account and Region with the same KMS key are always incremental, but encrypting a copy with a different KMS key creates a complete (non-incremental) copy.
  scope: EBS snapshot copy.
  link: [are always incremental copies](../facts/ebs.md#ebs-snapshot-copy-new-kms-key-full-copy)
  link: [a complete (non-incremental) copy is created](../facts/ebs.md#ebs-snapshot-copy-new-kms-key-full-copy)
ebs-snapshot-copy-new-region-full-copy
  claim: If you copy a snapshot to a new Region, a full (non-incremental) copy is created, which results in additional storage costs; a copy across Regions or accounts is an incremental copy if the conditions listed in the EBS User Guide are met.
  scope: EBS snapshot copy across Regions or accounts; incremental only when the listed conditions are met.
  link: [a full (non-incremental) copy is created](../facts/ebs.md#ebs-snapshot-copy-new-region-full-copy)
  link: [the copy is an incremental copy](../facts/ebs.md#ebs-snapshot-copy-new-region-full-copy)
ebs-snapshot-copy-tags-not-copied
  claim: User-defined tags are not copied from the source snapshot to the snapshot copy; you can add tags during or after the copy.
  scope: EBS snapshot copy.
  link: [User-defined tags are not copied](../facts/ebs.md#ebs-snapshot-copy-tags-not-copied)
  link: [add user-defined tags during or after](../facts/ebs.md#ebs-snapshot-copy-tags-not-copied)
ebs-snapshot-created-in-source-region
  claim: When the source volume or instance is in a Region, you must create its snapshots in that same Region (copying to another Region is a separate step).
  scope: EBS snapshot creation; source resource is in a Region (not a Local Zone or Outpost).
  link: [in the same Region as the source resource](../facts/ebs.md#ebs-snapshot-created-in-source-region)
  link: [you must create snapshots](../facts/ebs.md#ebs-snapshot-created-in-source-region)
ebs-snapshot-delete-might-not-reduce-cost
  claim: Deleting a snapshot might not reduce storage costs, because other snapshots might reference its data and referenced data is always preserved.
  scope: EBS snapshots.
  link: [might not reduce your organization's data storage costs](../facts/ebs.md#ebs-snapshot-delete-might-not-reduce-cost)
  link: [referenced data is always preserved](../facts/ebs.md#ebs-snapshot-delete-might-not-reduce-cost)
ebs-snapshot-delete-removes-only-exclusive-data
  claim: Deleting a snapshot removes only the data referenced exclusively by that snapshot; deleting earlier snapshots does not affect your ability to create volumes from later snapshots of the volume.
  scope: EBS snapshots of one volume.
  link: [only the data that is referenced exclusively](../facts/ebs.md#ebs-snapshot-delete-removes-only-exclusive-data)
  link: [does not affect your ability to create volumes](../facts/ebs.md#ebs-snapshot-delete-removes-only-exclusive-data)
ebs-snapshot-delete-retained-by-recycle-bin-rule
  claim: A deleted snapshot that matches a Recycle Bin retention rule is kept in the Recycle Bin instead of being deleted at once.
  scope: EBS snapshot deletion; the snapshot matches a Recycle Bin retention rule.
  link: [retained in the Recycle Bin](../facts/ebs.md#ebs-snapshot-delete-retained-by-recycle-bin-rule)
  link: [instead of being immediately deleted](../facts/ebs.md#ebs-snapshot-delete-retained-by-recycle-bin-rule)
ebs-snapshot-deletion-keep-only-latest
  claim: Even though snapshots are saved incrementally, the deletion process is designed so that you need to retain only the most recent snapshot to restore the volume.
  scope: EBS snapshots of one volume.
  link: [retain only the most recent snapshot](../facts/ebs.md#ebs-snapshot-deletion-keep-only-latest)
  link: [the snapshot deletion process is designed](../facts/ebs.md#ebs-snapshot-deletion-keep-only-latest)
ebs-snapshot-excludes-cached-data
  claim: A snapshot holds only the data written to the volume at the time the snapshot was requested; data cached by applications or the operating system is not included.
  scope: EBS snapshot.
  link: [does not include data that has been cached](../facts/ebs.md#ebs-snapshot-excludes-cached-data)
  link: [data that was written to the volume](../facts/ebs.md#ebs-snapshot-excludes-cached-data)
ebs-snapshot-incremental-changed-blocks
  claim: EBS snapshots are incremental backups: after the first snapshot, only the blocks on the volume that have changed since the most recent snapshot are saved.
  scope: EBS snapshots of one volume.
  link: [incremental backups](../facts/ebs.md#ebs-snapshot-incremental-changed-blocks)
  link: [blocks on the volume that have changed](../facts/ebs.md#ebs-snapshot-incremental-changed-blocks)
ebs-snapshot-lock-compliance-mode
  claim: In compliance mode, after the optional cooling-off period ends nobody can unlock the snapshot, change the lock mode or shorten the lock; you can only lengthen it, and to delete the snapshot you must wait for the lock to expire.
  scope: snapshot lock, compliance mode; after the cooling-off period has expired.
  link: [you can't unlock the snapshot](../facts/ebs.md#ebs-snapshot-lock-compliance-mode)
  link: [you can only increase the lock duration](../facts/ebs.md#ebs-snapshot-lock-compliance-mode)
  link: [you must wait for the lock to expire](../facts/ebs.md#ebs-snapshot-lock-compliance-mode)
ebs-snapshot-lock-cooling-off-range
  claim: The optional cooling-off period for a compliance-mode snapshot lock can range from 1 to 72 hours; omit it to lock in compliance mode immediately.
  scope: per snapshot locked in compliance mode; maximum; not adjustable; compliance mode only; governance mode has no cooling-off period.
  link: [from 1 to 72 hours](../facts/ebs.md#ebs-snapshot-lock-cooling-off-range)
  say: from one to seventy-two hours
ebs-snapshot-lock-duration-range
  claim: A snapshot lock duration given as a number of days can range from 1 day to 36500 days (100 years); after it passes, the snapshot is unlocked automatically.
  scope: per locked snapshot; maximum; not adjustable; or set a lock expiration date instead.
  link: [1 day to 36500 days (100 years)](../facts/ebs.md#ebs-snapshot-lock-duration-range)
  say: one day to one hundred years
ebs-snapshot-lock-governance-mode
  claim: In governance mode, users with the right IAM permissions can unlock the snapshot or change its lock mode and duration at any time; the lock applies immediately, with no cooling-off period.
  scope: snapshot lock, governance mode.
  link: [users with appropriate IAM permissions can unlock](../facts/ebs.md#ebs-snapshot-lock-governance-mode)
  link: [there is no cooling-off period](../facts/ebs.md#ebs-snapshot-lock-governance-mode)
ebs-snapshot-lock-modes
  claim: You lock a snapshot in compliance mode or governance mode, for a specific duration or until a specific date.
  scope: per snapshot.
  link: [compliance mode or governance mode](../facts/ebs.md#ebs-snapshot-lock-modes)
  link: [locked for a specific duration](../facts/ebs.md#ebs-snapshot-lock-modes)
ebs-snapshot-lock-no-additional-cost
  claim: You can lock and unlock snapshots at no additional cost; locked snapshots are billed at standard EBS snapshot storage cost.
  scope: per locked snapshot.
  link: [at no additional cost](../facts/ebs.md#ebs-snapshot-lock-no-additional-cost)
  say: at no additional cost
ebs-snapshot-lock-no-user-can-delete
  claim: While a snapshot is locked, no user can delete it, whatever their IAM permissions; you can still use the locked snapshot like any other snapshot.
  scope: per locked snapshot; while the lock is in effect.
  link: [regardless of their IAM permissions](../facts/ebs.md#ebs-snapshot-lock-no-user-can-delete)
  link: [it can't be deleted by any user](../facts/ebs.md#ebs-snapshot-lock-no-user-can-delete)
ebs-snapshot-only-unencrypted-public
  claim: Only unencrypted snapshots can be shared publicly; an encrypted snapshot can be shared only with specific accounts.
  scope: public EBS snapshots.
  link: [You can share only unencrypted snapshots publicly](../facts/ebs.md#ebs-snapshot-only-unencrypted-public)
  link: [Public snapshots of encrypted volumes are not supported](../facts/ebs.md#ebs-snapshot-only-unencrypted-public)
ebs-snapshot-regional-copy-before-sharing
  claim: Snapshots are constrained to the Region in which they were created; to share one in another Region, copy it to that Region and share the copy.
  scope: EBS snapshots.
  link: [Snapshots are constrained to the Region](../facts/ebs.md#ebs-snapshot-regional-copy-before-sharing)
  link: [copy the snapshot to that Region](../facts/ebs.md#ebs-snapshot-regional-copy-before-sharing)
ebs-snapshot-registered-ami-root-not-deletable
  claim: You cannot delete the root device snapshot of a registered AMI, even if the AMI is deprecated or disabled; you must deregister the AMI first.
  scope: root device snapshot of a registered AMI.
  link: [You must first deregister the AMI](../facts/ebs.md#ebs-snapshot-registered-ami-root-not-deletable)
  link: [registered AMI is deprecated or disabled](../facts/ebs.md#ebs-snapshot-registered-ami-root-not-deletable)
ebs-snapshot-restore-in-any-az-of-region
  claim: Snapshot data is automatically replicated across all Availability Zones in the Region, so you can restore volumes in any Availability Zone of that Region.
  scope: EBS snapshots, within the snapshot's Region.
  link: [restore volumes in any Availability Zones](../facts/ebs.md#ebs-snapshot-restore-in-any-az-of-region)
  link: [replicated across all Availability Zones in the Region](../facts/ebs.md#ebs-snapshot-restore-in-any-az-of-region)
ebs-snapshot-restore-volume-other-az
  claim: A volume created from a snapshot is an exact copy of the original volume at snapshot time, and by specifying a different Availability Zone you can create that duplicate volume in that zone.
  scope: volume created from an EBS snapshot.
  link: [create a duplicate volume in that zone](../facts/ebs.md#ebs-snapshot-restore-volume-other-az)
  link: [an exact copy of the original volume](../facts/ebs.md#ebs-snapshot-restore-volume-other-az)
ebs-snapshot-root-volume-stop-instance-first
  claim: For a snapshot of a volume that is the root device of an instance, AWS recommends stopping the instance before taking the snapshot.
  scope: snapshot of a root volume; recommendation.
  link: [stop the instance before taking the snapshot](../facts/ebs.md#ebs-snapshot-root-volume-stop-instance-first)
  link: [serves as the root device](../facts/ebs.md#ebs-snapshot-root-volume-stop-instance-first)
ebs-snapshot-s3-buckets-not-accessible
  claim: Snapshots are stored in Amazon S3 buckets that you cannot access directly; you manage them with the EC2 console or EC2 API, not with the S3 console or S3 API.
  scope: EBS snapshots.
  link: [S3 buckets that you can't access directly](../facts/ebs.md#ebs-snapshot-s3-buckets-not-accessible)
  link: [Amazon S3 console or the Amazon S3 API](../facts/ebs.md#ebs-snapshot-s3-buckets-not-accessible)
ebs-snapshot-same-encryption-and-key-as-volume
  claim: A snapshot gets the same encryption status as its source volume: snapshots of unencrypted volumes are not encrypted, and snapshots of encrypted volumes are encrypted with the same KMS key as the volume.
  scope: EBS snapshot creation.
  link: [same encryption status as the volume](../facts/ebs.md#ebs-snapshot-same-encryption-and-key-as-volume)
  link: [using the same KMS key as the volume](../facts/ebs.md#ebs-snapshot-same-encryption-and-key-as-volume)
ebs-snapshot-share-encrypted-share-cmk-too
  claim: When you share an encrypted snapshot, you must also share the customer managed key that encrypted it, by giving the other account permissions on the key.
  scope: sharing encrypted EBS snapshots.
  link: [you must also share the customer managed key](../facts/ebs.md#ebs-snapshot-share-encrypted-share-cmk-too)
  link: [apply cross-account permissions to a customer managed key](../facts/ebs.md#ebs-snapshot-share-encrypted-share-cmk-too)
ebs-snapshot-share-public-or-specific-accounts
  claim: By changing a snapshot's permissions you can share it publicly with all other AWS accounts or privately with individual accounts; they can create their own volumes from it while your snapshot stays unaffected.
  scope: EBS snapshot permissions.
  link: [share snapshots publicly with all other AWS accounts](../facts/ebs.md#ebs-snapshot-share-public-or-specific-accounts)
  link: [privately with individual AWS accounts](../facts/ebs.md#ebs-snapshot-share-public-or-specific-accounts)
ebs-snapshot-standard-price
  claim: A snapshot in the standard tier is billed at the standard snapshot rate of $0.05 per GB-month.
  scope: per GB-month of standard-tier snapshot; example rate in the EBS guide.
  link: [$0.05 per GB-month](../facts/ebs.md#ebs-snapshot-standard-price)
  say: five cents per GB-month
ebs-snapshot-stored-in-s3-multiple-azs
  claim: An EBS snapshot writes a copy of the volume's data to Amazon S3, where it is stored redundantly in multiple Availability Zones.
  scope: EBS snapshot.
  link: [write a copy of the data](../facts/ebs.md#ebs-snapshot-stored-in-s3-multiple-azs)
  link: [stored redundantly in multiple Availability Zones](../facts/ebs.md#ebs-snapshot-stored-in-s3-multiple-azs)
ebs-snapshot-volume-need-not-be-attached
  claim: A volume does not need to be attached to a running instance for you to take a snapshot of it.
  scope: EBS snapshot.
  link: [does not need to be attached](../facts/ebs.md#ebs-snapshot-volume-need-not-be-attached)
  link: [attached to a running instance](../facts/ebs.md#ebs-snapshot-volume-need-not-be-attached)
ebs-ssd-transactional-hdd-throughput-categories
  claim: EBS volume types fall into two major categories: SSD-backed storage for transactional workloads and HDD-backed storage for throughput-intensive workloads.
  scope: EBS volume types.
  link: [SSD-backed storage for transactional workloads](../facts/ebs.md#ebs-ssd-transactional-hdd-throughput-categories)
  link: [HDD-backed storage for throughput intensive workloads](../facts/ebs.md#ebs-ssd-transactional-hdd-throughput-categories)
ebs-st1-1-tib-burst-and-baseline
  claim: For a 1-TiB st1 volume, burst throughput is limited to 250 MiB/s and the credit bucket fills at 40 MiB/s.
  scope: per st1 volume of 1 TiB; maximum; not adjustable; scales linearly with volume size.
  link: [250 MiB/s](../facts/ebs.md#ebs-st1-1-tib-burst-and-baseline)
  link: [40 MiB/s](../facts/ebs.md#ebs-st1-1-tib-burst-and-baseline)
  say: two hundred fifty mebibytes per second | forty mebibytes per second
ebs-st1-baseline-range
  claim: On st1 volume sizes from 0.125 TiB to 16 TiB, baseline throughput varies from 5 MiB/s to a cap of 500 MiB/s, which is reached at 12.5 TiB.
  scope: per st1 volume; maximum; not adjustable; cap reached at 12.5 TiB.
  link: [0.125 TiB to 16 TiB](../facts/ebs.md#ebs-st1-baseline-range)
  link: [5 MiB/s to a cap of 500 MiB/s](../facts/ebs.md#ebs-st1-baseline-range)
  say: zero point one two five TiB to sixteen TiB | five to five hundred mebibytes per second
ebs-st1-burst-range
  claim: st1 burst throughput varies from 31 MiB/s to a cap of 500 MiB/s, which is reached at 2 TiB.
  scope: per st1 volume; maximum; not adjustable; cap reached at 2 TiB.
  link: [31 MiB/s to a cap of 500 MiB/s](../facts/ebs.md#ebs-st1-burst-range)
  say: thirty-one to five hundred mebibytes per second
ebs-st1-low-cost-frequent-throughput
  claim: st1 (Throughput Optimized HDD) is a low cost HDD volume designed for frequently accessed, throughput-intensive workloads; though similar to Cold HDD (sc1) volumes, st1 volumes are designed to support frequently accessed data.
  scope: st1 volumes.
  link: [Low cost HDD volume](../facts/ebs.md#ebs-st1-low-cost-frequent-throughput)
  link: [frequently accessed, throughput-intensive workloads](../facts/ebs.md#ebs-st1-low-cost-frequent-throughput)
ebs-st1-max-throughput
  claim: st1 throughput is capped at a maximum of 500 MiB/s; after the burst bucket is depleted, throughput is limited to the baseline of 40 MiB/s per TiB.
  scope: per st1 volume; maximum; not adjustable.
  link: [maximum of 500 MiB/s](../facts/ebs.md#ebs-st1-max-throughput)
  link: [40 MiB/s per TiB](../facts/ebs.md#ebs-st1-max-throughput)
  say: maximum of five hundred mebibytes per second | forty mebibytes per second per TiB
ebs-st1-storage-price-example
  claim: In the pricing page example Region, st1 storage costs $0.045 per GB-month.
  scope: per GB-month of st1 storage; example Region rate.
  link: [$0.045 per GB-month](../facts/ebs.md#ebs-st1-storage-price-example)
  say: four and a half cents per GB-month
ebs-st1-use-cases
  claim: AWS lists big data, data warehouses and log processing as st1 use cases; st1 fits large, sequential workloads such as Amazon EMR and ETL.
  scope: st1 volumes.
  link: [Big data, data warehouses, log processing](../facts/ebs.md#ebs-st1-use-cases)
  link: [large, sequential workloads](../facts/ebs.md#ebs-st1-use-cases)
ebs-st1-vs-sc1-scan-choice
  claim: Use st1 for a throughput-oriented workload that must complete scans quickly (up to 500 MiB/s) or needs several full volume scans a day; use sc1 when optimizing for cost, the data is relatively infrequently accessed and you need no more than 250 MiB/s of scanning performance.
  scope: choice between st1 and sc1.
  link: [up to 500 MiB/s](../facts/ebs.md#ebs-st1-vs-sc1-scan-choice)
  link: [more than 250 MiB/s of scanning performance](../facts/ebs.md#ebs-st1-vs-sc1-scan-choice)
  say: up to five hundred mebibytes per second | more than two hundred fifty mebibytes per second of scanning performance
ebs-status-check-disables-io-on-inconsistency
  claim: When EBS finds a volume's data potentially inconsistent, by default it disables I/O to the volume from attached instances to prevent corruption, and the volume status becomes impaired; the Auto-Enable IO attribute overrides this.
  scope: EBS volume status checks; default; adjustable; Auto-Enable IO attribute not set.
  link: [disables I/O to the volume](../facts/ebs.md#ebs-status-check-disables-io-on-inconsistency)
  link: [the volume status is impaired](../facts/ebs.md#ebs-status-check-disables-io-on-inconsistency)
  link: [configuring the volume to automatically enable I/O](../facts/ebs.md#ebs-status-check-disables-io-on-inconsistency)
ebs-time-based-copy-duration-range
  claim: For a time-based snapshot or EBS-backed AMI copy, you can request a completion duration from 15 minutes to 48 hours, in 15 minute increments.
  scope: per time-based copy operation; maximum; not adjustable.
  link: [between 15 minutes and 48 hours](../facts/ebs.md#ebs-time-based-copy-duration-range)
  link: [15 minute increments](../facts/ebs.md#ebs-time-based-copy-duration-range)
  say: between fifteen minutes and forty-eight hours | fifteen minute increments
ebs-time-based-copy-for-rpo-rto
  claim: Time-based copies make snapshot and AMI copies, within and across Regions, finish in a specified timeframe, which helps meet disaster recovery RPO and RTO requirements.
  scope: time-based snapshot and EBS-backed AMI copies.
  link: [meet stringent disaster recovery requirements](../facts/ebs.md#ebs-time-based-copy-for-rpo-rto)
  link: [within and across AWS Regions](../facts/ebs.md#ebs-time-based-copy-for-rpo-rto)
ebs-time-based-copy-missed-duration-billing
  claim: If a time-based copy misses its requested duration because you exceeded a quota, you are billed at the rate for the actual completion duration; if EBS cannot meet the duration or cancels for service-side issues, you are not billed the additional charges.
  scope: per time-based copy operation; depends on whether the cause is your quota or a service-side issue.
  link: [billed based on the actual completion duration](../facts/ebs.md#ebs-time-based-copy-missed-duration-billing)
  link: [you are not billed the additional charges](../facts/ebs.md#ebs-time-based-copy-missed-duration-billing)
  say: billed based on the actual completion duration | you are not billed the additional charges
ebs-time-based-copy-per-operation-throughput
  claim: A single time-based snapshot copy operation can reach at most 500 MiB/s of throughput; this quota is not adjustable.
  scope: per time-based snapshot copy operation; maximum; not adjustable; for AMI copies, applies to each snapshot of the AMI.
  link: [500 MiB/s](../facts/ebs.md#ebs-time-based-copy-per-operation-throughput)
  say: five hundred mebibytes per second
ebs-time-based-copy-price-example
  claim: Time-based copies are charged per GiB of snapshot data copied at a rate set by the requested duration; in the guide's example, 3,000 GiB with an 8-hour duration costs $30 at $0.010 per GiB.
  scope: per GiB copied; rate depends on the requested completion duration.
  link: [$30 ($0.010 x 3,000 GiB)](../facts/ebs.md#ebs-time-based-copy-price-example)
  say: thirty dollars
ebs-time-based-copy-pricing
  claim: Time-based copy operations have an additional charge per GiB of snapshot data copied, at a rate that depends on the requested completion duration.
  scope: per time-based copy operation.
  link: [per GiB of snapshot data copied](../facts/ebs.md#ebs-time-based-copy-pricing)
  link: [based on the requested completion duration](../facts/ebs.md#ebs-time-based-copy-pricing)
ebs-volume-block-storage-device-like-hard-drive
  claim: An EBS volume is a durable, block-level storage device that you attach to an instance and then use as you would use a physical hard drive.
  scope: EBS volume.
  link: [durable, block-level storage device](../facts/ebs.md#ebs-volume-block-storage-device-like-hard-drive)
  link: [as you would use a physical hard drive](../facts/ebs.md#ebs-volume-block-storage-device-like-hard-drive)
ebs-volume-charged-while-data-persists
  claim: You keep paying for an EBS volume for as long as its data persists, and the data persists until the volume is deleted explicitly.
  scope: EBS volume.
  link: [as long as the data persists](../facts/ebs.md#ebs-volume-charged-while-data-persists)
  link: [until the volume is deleted explicitly](../facts/ebs.md#ebs-volume-charged-while-data-persists)
ebs-volume-copy-instant-access
  claim: A volume copy is created immediately and can be accessed at once, without waiting for the data to be copied from the source volume; the copy operation does not affect the performance of the source volume.
  scope: per volume copy; during initialization the copy gets baseline performance.
  link: [Volume copies are created immediately](../facts/ebs.md#ebs-volume-copy-instant-access)
  link: [can be accessed instantly](../facts/ebs.md#ebs-volume-copy-instant-access)
ebs-volume-copy-pricing
  claim: Copying a volume has a copy-operation charge based on the size of the data blocks written to the source volume when the copy is created; the new volume is then charged like any other EBS volume.
  scope: per volume copy.
  link: [charged for the copy operation](../facts/ebs.md#ebs-volume-copy-pricing)
  link: [size of the data blocks written](../facts/ebs.md#ebs-volume-copy-pricing)
ebs-volume-copy-same-az
  claim: A volume copy is a crash-consistent, point-in-time copy of the source volume, and it must be created in the same Availability Zone as the source volume.
  scope: per volume copy.
  link: [same Availability Zone as the source volume](../facts/ebs.md#ebs-volume-copy-same-az)
  link: [crash-consistent, point-in-time copy](../facts/ebs.md#ebs-volume-copy-same-az)
ebs-volume-from-snapshot-exact-replica-same-az-attach
  claim: A volume created from a snapshot begins as an exact replica of the volume the snapshot was taken from, and a created volume can be attached to any instance in its Availability Zone.
  scope: volumes created from EBS snapshots.
  link: [begins as an exact replica of the volume](../facts/ebs.md#ebs-volume-from-snapshot-exact-replica-same-az-attach)
  link: [any EC2 instance in the same Availability Zone](../facts/ebs.md#ebs-volume-from-snapshot-exact-replica-same-az-attach)
ebs-volume-from-snapshot-size-at-least-source
  claim: A volume created from a snapshot gets the source snapshot's volume size unless you set a size, and a size you set must be equal to or larger than the source snapshot's volume size.
  scope: volumes created from EBS snapshots; a size is specified.
  link: [equal to or larger than](../facts/ebs.md#ebs-volume-from-snapshot-size-at-least-source)
  say: the same size or larger, never smaller
ebs-volume-initialization-from-snapshot
  claim: For a volume created from a snapshot, the data blocks must be downloaded from Amazon S3 to the new volume (volume initialization); during this time the volume can show increased I/O latency and decreased performance.
  scope: volumes created from snapshots; until every block has been downloaded.
  link: [downloaded from Amazon S3 to the new volume](../facts/ebs.md#ebs-volume-initialization-from-snapshot)
  link: [increased I/O latency and decreased performance](../facts/ebs.md#ebs-volume-initialization-from-snapshot)
ebs-volume-initialization-rate-range
  claim: When you create a volume from a snapshot you can optionally specify a Provisioned Rate for Volume Initialization from 100 to 300 MiB/s, so the volume becomes fully initialized in a predictable time.
  scope: per volume created from a snapshot; maximum; not adjustable; optional; specified when you create the volume from a snapshot.
  link: [100 to 300 MiB/s](../facts/ebs.md#ebs-volume-initialization-rate-range)
  link: [fully performant in a predictable amount of time](../facts/ebs.md#ebs-volume-initialization-rate-range)
  say: one hundred to three hundred mebibytes per second
ebs-volume-persists-independently-of-instance
  claim: An EBS volume is off-instance storage: it can persist independently from the life of the EC2 instance it is attached to.
  scope: EBS volume.
  link: [persist independently from the running life](../facts/ebs.md#ebs-volume-persists-independently-of-instance)
  link: [off-instance storage](../facts/ebs.md#ebs-volume-persists-independently-of-instance)
ebs-volume-raw-unformatted-block-device
  claim: EBS volumes are presented to you as raw, unformatted block devices, so you format a volume with a file system (for example Ext4 on Linux or NTFS on Windows) before you install applications on it.
  scope: EBS volume.
  link: [raw, unformatted block devices](../facts/ebs.md#ebs-volume-raw-unformatted-block-device)
  link: [format the EBS volume with a file system](../facts/ebs.md#ebs-volume-raw-unformatted-block-device)
ebs-volume-replicated-within-az
  claim: When you create an EBS volume, it is automatically replicated within its Availability Zone, which prevents data loss from the failure of any single hardware component.
  scope: EBS volume.
  link: [automatically replicated within its Availability Zone](../facts/ebs.md#ebs-volume-replicated-within-az)
  link: [failure of any single hardware component](../facts/ebs.md#ebs-volume-replicated-within-az)
ebs-volume-same-az-as-instance
  claim: You can attach several EBS volumes to one instance, but the volume and the instance must be in the same Availability Zone.
  scope: EBS volume attachment.
  link: [must be in the same Availability Zone](../facts/ebs.md#ebs-volume-same-az-as-instance)
  link: [attach multiple EBS volumes to a single instance](../facts/ebs.md#ebs-volume-same-az-as-instance)
ebs-volume-size-cannot-decrease
  claim: You cannot decrease the size of an EBS volume; to get a smaller one, you create a smaller volume and migrate the data with an application-level tool such as rsync or robocopy.
  scope: EBS volume modification.
  link: [You can't decrease the volume size](../facts/ebs.md#ebs-volume-size-cannot-decrease)
  link: [create a smaller volume](../facts/ebs.md#ebs-volume-size-cannot-decrease)
ebs-volume-stays-attached-through-stop-start
  claim: You can stop and restart an EBS-backed instance without affecting the data on its attached EBS volume; the volume remains attached throughout the stop-start cycle.
  scope: EBS-backed instance; stop and start, not terminate.
  link: [remains attached throughout the stop-start cycle](../facts/ebs.md#ebs-volume-stays-attached-through-stop-start)
  link: [without affecting the data stored](../facts/ebs.md#ebs-volume-stays-attached-through-stop-start)
ebs-volume-type-names
  claim: The EBS volume types are General Purpose SSD (gp2 and gp3), Provisioned IOPS SSD (io1 and io2), Throughput Optimized HDD (st1), Cold HDD (sc1) and Magnetic (standard).
  scope: EBS volume types.
  link: [General Purpose SSD (gp2 and gp3)](../facts/ebs.md#ebs-volume-type-names)
  link: [Provisioned IOPS SSD (io1 and io2)](../facts/ebs.md#ebs-volume-type-names)
  link: [Throughput Optimized HDD (st1), Cold HDD (sc1)](../facts/ebs.md#ebs-volume-type-names)
ebs-vs-efs-az-scope-and-sharing
  claim: Each EBS volume is replicated within its own Availability Zone, while Amazon EFS is a regional service that stores data within and across multiple Availability Zones and gives shared access to thousands of EC2 instances.
  scope: EBS volume versus Amazon EFS file system; EBS Multi-Attach aside.
  link: [automatically replicated within its Availability Zone](../facts/ebs.md#ebs-vs-efs-az-scope-and-sharing)
  link: [within and across multiple Availability Zones](../facts/ebs.md#ebs-vs-efs-az-scope-and-sharing)
ebs-vs-instance-store-persistence
  claim: On the EC2 storage options page, an EBS volume persists independently of its instance and can be backed up with snapshots stored in Amazon S3, while instance store data is lost when you stop, hibernate or terminate the instance.
  scope: EBS volumes versus instance store volumes.
  link: [persists independently from the life](../facts/ebs.md#ebs-vs-instance-store-persistence)
  link: [any data on instance store volumes is lost](../facts/ebs.md#ebs-vs-instance-store-persistence)
ebs-wa-rel09-backup-capabilities
  claim: Well-Architected REL09-BP01 says services such as Amazon EBS have built-in backup capabilities and AWS Backup centralizes and automates data protection across AWS services.
  scope: Well-Architected reliability pillar, REL09-BP01.
  link: [have built in capabilities to create backups](../facts/ebs.md#ebs-wa-rel09-backup-capabilities)
  link: [centralize and automate data protection across AWS services](../facts/ebs.md#ebs-wa-rel09-backup-capabilities)
ebs-wa-sec08-encrypt-at-rest
  claim: Well-Architected SEC08-BP02 says to encrypt private data at rest; for EC2 it points to default encryption on the account so that new EBS volumes are automatically encrypted.
  scope: Well-Architected security pillar, SEC08-BP02.
  link: [Encrypt private data at rest](../facts/ebs.md#ebs-wa-sec08-encrypt-at-rest)
  link: [new EBS volumes are automatically encrypted](../facts/ebs.md#ebs-wa-sec08-encrypt-at-rest)
ebs-xen-linux-40-volumes
  claim: Attaching more than 40 volumes to a Xen-based Linux instance can cause boot failures; the count includes the root volume, instance store volumes and EBS volumes.
  scope: per Xen-based Linux instance; maximum; not adjustable; above 40 is best effort only.
  link: [more than 40 volumes](../facts/ebs.md#ebs-xen-linux-40-volumes)
  say: more than forty volumes
instance-store-attach-only-at-launch
  claim: Instance store volumes can be attached to an instance only when you launch it, not after launch.
  scope: per instance.
  link: [only when you launch it](../facts/instance-store.md#instance-store-attach-only-at-launch)
  say: only at launch
instance-store-data-erased-on-stop
  claim: When you stop an instance, the data on any instance store volumes is erased, so data you need must first be copied to persistent storage such as Amazon EBS or Amazon S3.
  scope: per instance; the instance is stopped.
  link: [data on any instance store volumes is erased](../facts/instance-store.md#instance-store-data-erased-on-stop)
  say: instance store data is erased on stop
instance-store-data-lost-when-disk-fails
  claim: When the underlying disk fails, the data on the failed instance store disk does not persist.
  scope: instance store volumes.
  link: [The underlying disk fails](../facts/instance-store.md#instance-store-data-lost-when-disk-fails)
  link: [on the failed disk does not persist](../facts/instance-store.md#instance-store-data-lost-when-disk-fails)
instance-store-data-not-in-ebs-backed-ami
  claim: Instance store data is not included in an EBS-backed AMI created from the instance, nor on the instance store volumes of instances launched from that AMI.
  scope: instance store volumes, EBS-backed AMI creation.
  link: [not included in the EBS-backed AMI](../facts/instance-store.md#instance-store-data-not-in-ebs-backed-ami)
  link: [instances launched from that AMI](../facts/instance-store.md#instance-store-data-not-in-ebs-backed-ami)
instance-store-data-persists-reboot-not-stop
  claim: Data on an instance store volume persists when the instance is rebooted, but not when the instance is stopped, hibernated, or terminated; then every block of the volume is cryptographically erased.
  scope: instance store volumes.
  link: [persists even if the instance is rebooted](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop)
  link: [stopped, hibernated, or terminated](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop)
  link: [cryptographically erased](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop)
  say: a reboot keeps instance store data | stop, hibernate or terminate loses it | the blocks are erased
instance-store-faq-only-temporary-data
  claim: AWS recommends using the local instance store only for temporary data.
  scope: instance store volumes.
  link: [only for temporary data](../facts/instance-store.md#instance-store-faq-only-temporary-data)
  say: instance store only for temporary data
instance-store-first-write-slower-initialize
  claim: On some instance store volumes the first write to each location is slower than later writes, so AWS recommends initializing the drives for high disk performance; instance types with direct-attached SSD and TRIM support give maximum performance at launch without initialization.
  scope: some instance store volumes; not needed on SSD instance store with TRIM support.
  link: [performs more slowly than subsequent writes](../facts/instance-store.md#instance-store-first-write-slower-initialize)
  link: [maximum performance at launch time, without initialization](../facts/instance-store.md#instance-store-first-write-slower-initialize)
instance-store-hibernate-data-lost
  claim: When an instance hibernates, its instance store volumes stay attached but the data on them is lost.
  scope: instance store volumes on a hibernated instance.
  link: [remain attached to the instance](../facts/instance-store.md#instance-store-hibernate-data-lost)
  link: [data on the instance store volumes is lost](../facts/instance-store.md#instance-store-hibernate-data-lost)
instance-store-ideal-for-temporary-data
  claim: Instance store is ideal for temporary information that changes frequently, such as buffers, caches and scratch data, and for temporary data that you replicate across a fleet of instances.
  scope: instance store.
  link: [temporary storage of information that changes frequently](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  link: [buffers, caches, scratch data](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  link: [replicate across a fleet of instances](../facts/instance-store.md#instance-store-ideal-for-temporary-data)
  say: temporary data that changes often | buffers, caches and scratch data | or data copied across many instances
instance-store-no-additional-charge
  claim: There is no additional charge for the instance store volumes provided with an instance; they are included in the usage cost of the instance.
  scope: per instance; instance types that provide instance store volumes.
  link: [There is no additional charge](../facts/instance-store.md#instance-store-no-additional-charge)
  say: instance store is included in the instance price
instance-store-not-for-valuable-long-term-data
  claim: Do not rely on instance store volumes for valuable, long-term data; to keep the data beyond the instance's lifetime you must copy it manually to more persistent storage such as an EBS volume, an S3 bucket or an EFS file system.
  scope: instance store volumes.
  link: [do not rely on instance store volumes](../facts/instance-store.md#instance-store-not-for-valuable-long-term-data)
  link: [manually copy that data to more persistent storage](../facts/instance-store.md#instance-store-not-for-valuable-long-term-data)
instance-store-nvme-encryption-xts-aes-256
  claim: Data on NVMe instance storage is encrypted with an XTS-AES-256 block cipher in a hardware module on the instance; the keys are unique per device, destroyed when the instance stops or terminates, and you cannot disable this encryption or supply your own key.
  scope: per NVMe instance store volume; default; not adjustable; always on; cannot be disabled.
  link: [XTS-AES-256 block cipher](../facts/instance-store.md#instance-store-nvme-encryption-xts-aes-256)
  say: XTS AES two fifty-six block cipher
instance-store-physically-attached-host-disks
  claim: An instance store provides temporary block-level storage on disks that are physically attached to the host computer, exposed to the instance as one or more block devices.
  scope: instance store.
  link: [temporary block-level storage](../facts/instance-store.md#instance-store-physically-attached-host-disks)
  link: [physically attached to the host computer](../facts/instance-store.md#instance-store-physically-attached-host-disks)
instance-store-root-deleted-on-terminate-or-failure
  claim: On an instance with an instance store root volume, data persists while the instance runs but is deleted when the instance terminates or fails; such instances do not support Stop and cannot be restored after they fail or terminate.
  scope: instances with an instance store root volume.
  link: [deleted when the instance is terminated](../facts/instance-store.md#instance-store-root-deleted-on-terminate-or-failure)
  link: [do not support the Stop action](../facts/instance-store.md#instance-store-root-deleted-on-terminate-or-failure)
  link: [it can't be restored](../facts/instance-store.md#instance-store-root-deleted-on-terminate-or-failure)
instance-store-root-limited-types-no-windows
  claim: Only the following instance types support an instance store volume as the root volume: C1, C3, D2, I2, M1, M2, M3, R3 and X1; Windows instances do not support instance store root volumes.
  scope: instance store root volumes.
  link: [C1, C3, D2, I2, M1, M2, M3, R3, and X1](../facts/instance-store.md#instance-store-root-limited-types-no-windows)
  link: [do not support instance store root volumes](../facts/instance-store.md#instance-store-root-limited-types-no-windows)
instance-store-size-example-r8id
  claim: For the instance types that support instance store volumes, the number and size of the instance store volumes vary by instance size; for example, r8id.large supports 1 x 118 GB instance store volume and r8id.32xlarge supports 2 x 3800 GB instance store volumes.
  scope: per instance, by instance size; maximum; not adjustable.
  link: [1 x 118 GB](../facts/instance-store.md#instance-store-size-example-r8id)
  link: [2 x 3800 GB](../facts/instance-store.md#instance-store-size-example-r8id)
  say: one volume of one hundred eighteen GB | two volumes of three thousand eight hundred GB
instance-store-size-varies-by-type
  claim: Instance store is temporary block storage on disks physically attached to the host; its size and number of devices vary by instance type and size, and not every instance type provides instance store volumes.
  scope: per instance type and size.
  link: [varies by instance type and instance size](../facts/instance-store.md#instance-store-size-varies-by-type)
  link: [not every instance type provides instance store volumes](../facts/instance-store.md#instance-store-size-varies-by-type)
  say: it depends on the instance type and size | some types have no instance store
instance-store-ssd-high-random-io
  claim: SSD instance store volumes deliver high random I/O performance with very low latency, for workloads that do not need the data to persist when the instance terminates or that use fault-tolerant architectures.
  scope: per SSD instance store volume; data need not persist after termination.
  link: [high random I/O performance with very low latency](../facts/instance-store.md#instance-store-ssd-high-random-io)
  say: high random I/O performance with very low latency
instance-store-ssd-leave-10-percent-unpartitioned
  claim: SSD-based instance store volumes have no space reserved for over-provisioning; to reduce write amplification, AWS recommends leaving 10 percent of the volume unpartitioned.
  scope: per SSD instance store volume; recommendation.
  link: [leave 10 percent of the volume unpartitioned](../facts/instance-store.md#instance-store-ssd-leave-10-percent-unpartitioned)
  say: leave ten percent of the volume unpartitioned
instance-store-tied-to-instance-lifetime
  claim: An instance store volume exists only during the lifetime of its instance; you can't make it persist beyond that lifetime, and you can't detach it and attach it to a different instance.
  scope: instance store volumes.
  link: [only during the lifetime of the instance](../facts/instance-store.md#instance-store-tied-to-instance-lifetime)
  link: [You can’t detach an instance store volume](../facts/instance-store.md#instance-store-tied-to-instance-lifetime)
  say: it lives only as long as its instance | you cannot move it to another instance
instance-store-type-change-data-not-transferred
  claim: When you change the instance type, the instance gets the instance store volumes of the new type (if it supports instance store), but the data does not transfer to the new instance.
  scope: instance store volumes; instance type changed.
  link: [does not transfer to the new instance](../facts/instance-store.md#instance-store-type-change-data-not-transferred)
  link: [supported by the new instance type](../facts/instance-store.md#instance-store-type-change-data-not-transferred)
