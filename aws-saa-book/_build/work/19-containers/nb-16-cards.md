facts card: 492 facts
ec2-alarm-reboot-instance-check-recover-system-check
  claim: The CloudWatch reboot alarm action is recommended for instance status check failures, and the recover alarm action is suited for system status check failures.
  scope: CloudWatch alarm actions on an EC2 instance.
  link: [recommended for Instance Health Check failures](../facts/ec2.md#ec2-alarm-reboot-instance-check-recover-system-check)
  link: [suited for System Health Check failures](../facts/ec2.md#ec2-alarm-reboot-instance-check-recover-system-check)
  say: reboot for an instance check failure | recover for a system check failure
ec2-all-upfront-highest-discount
  claim: All Upfront payment gives the highest discount, because you prepay for the compute; it fits a company with available capital that wants maximum efficiency.
  scope: commitment payment options; when All Upfront is available.
  link: [prepaying for compute at the highest discount](../facts/ec2.md#ec2-all-upfront-highest-discount)
  say: All Upfront gives the highest discount
ec2-allowed-amis-per-region-declarative-policy
  claim: Allowed AMIs settings are set at the account level, directly or through a declarative policy, and must be configured in each Region; a declarative policy can apply them across many Regions and accounts at once, and while one is in use the setting can't be changed directly in the account.
  scope: per account, per Region.
  link: [configured in each AWS Region](../facts/ec2.md#ec2-allowed-amis-per-region-declarative-policy)
  link: [by using a declarative policy](../facts/ec2.md#ec2-allowed-amis-per-region-declarative-policy)
  say: it is set per Region | a declarative policy applies it across accounts and Regions
ec2-allowed-amis-public-and-shared-only
  claim: Allowed AMIs controls only the discovery and use of public AMIs and AMIs shared with your account; AMIs that your own account created are always discoverable and usable.
  scope: per account, per Region; Allowed AMIs criteria enabled.
  link: [AMIs created by your account are always discoverable](../facts/ec2.md#ec2-allowed-amis-public-and-shared-only)
  link: [public AMIs or AMIs shared with your account](../facts/ec2.md#ec2-allowed-amis-public-and-shared-only)
  say: it does not restrict your own AMIs | it controls public and shared AMIs
ec2-ami-block-public-access-defaults
  claim: Block public access for AMIs is enabled by default for new accounts and for existing accounts with no public AMIs, but it is disabled by default for an account that had one or more public AMIs on or after July 15, 2023, even if all its AMIs are now private, and for existing accounts with one or more public AMIs; when it is enabled, any attempt to make an AMI public is blocked, but AMIs that are already public stay public.
  scope: per account, per Region; default; adjustable; disabled by default if the account had a public AMI on or after July 15, 2023.
  link: [make an AMI public is automatically blocked](../facts/ec2.md#ec2-ami-block-public-access-defaults)
  link: [they remain publicly available](../facts/ec2.md#ec2-ami-block-public-access-defaults)
  say: with it on, nobody can make an AMI public | AMIs that are already public stay public
ec2-ami-copy-encryption-default-and-override
  claim: By default a CopyImage keeps the encryption state of the AMI's source snapshots; you can also encrypt an unencrypted AMI, or re-encrypt it with a different KMS key, by supplying encryption parameters during the copy.
  scope: EBS-backed AMI copy; default; adjustable; encryption by default off; with encryption by default on, new snapshots are encrypted.
  link: [maintains the existing encryption state](../facts/ec2.md#ec2-ami-copy-encryption-default-and-override)
  link: [simultaneously apply a new encryption state](../facts/ec2.md#ec2-ami-copy-encryption-default-and-override)
  link: [encrypted by the AWS account's default KMS key](../facts/ec2.md#ec2-ami-copy-encryption-default-and-override)
  say: you can encrypt during the copy
ec2-ami-copy-no-launch-permissions
  claim: Copying an AMI does not copy its launch permissions or S3 bucket permissions to the new AMI; you apply them to the new AMI after the copy completes.
  scope: AMI copy.
  link: [AWS does not copy launch permissions or Amazon S3 bucket permissions from the source AMI to the new AMI](../facts/ec2.md#ec2-ami-copy-no-launch-permissions)
  link: [you can apply launch permissions and Amazon S3 bucket permissions to the new AMI](../facts/ec2.md#ec2-ami-copy-no-launch-permissions)
  say: launch permissions are not copied with the AMI
ec2-ami-definition-and-contents
  claim: An AMI is an image that provides the software needed to set up and boot an EC2 instance and contains a block device mapping of the volumes to attach; you must specify an AMI at launch and it must be compatible with the instance type.
  scope: Amazon Machine Images.
  link: [an image that provides the software](../facts/ec2.md#ec2-ami-definition-and-contents)
  link: [a block device mapping](../facts/ec2.md#ec2-ami-definition-and-contents)
  link: [You must specify an AMI](../facts/ec2.md#ec2-ami-definition-and-contents)
  say: an AMI is the image that sets up and boots an instance
ec2-ami-encrypted-cannot-be-public
  claim: An AMI that includes encrypted volumes or snapshots of encrypted volumes can't be made public, but you can share it with specific AWS accounts.
  scope: AMIs with encrypted volumes or snapshots.
  link: [Some AMIs can't be made public](../facts/ec2.md#ec2-ami-encrypted-cannot-be-public)
  link: [share the AMI with specific AWS accounts](../facts/ec2.md#ec2-ami-encrypted-cannot-be-public)
  say: encrypted AMIs cannot be public | share them with chosen accounts instead
ec2-ami-encrypted-snapshots-shareable
  claim: AMIs with encrypted snapshots can be shared across AWS accounts, and you can encrypt some or all volumes at launch when the AMI's snapshots are unencrypted.
  scope: EBS-backed AMIs.
  link: [can be shared across AWS accounts](../facts/ec2.md#ec2-ami-encrypted-snapshots-shareable)
  link: [encrypt some or all of the volumes](../facts/ec2.md#ec2-ami-encrypted-snapshots-shareable)
  say: an encrypted AMI can be shared with other accounts
ec2-ami-launch-permissions-categories
  claim: Launch permissions decide who can launch instances from an AMI: public grants all AWS accounts, explicit grants specific accounts, organizations or OUs, and only the AMI owner can set them.
  scope: per AMI.
  link: [determine who can use an AMI](../facts/ec2.md#ec2-ami-launch-permissions-categories)
  link: [Only the owner of an AMI](../facts/ec2.md#ec2-ami-launch-permissions-categories)
  link: [specific AWS accounts, organizations, or organizational units](../facts/ec2.md#ec2-ami-launch-permissions-categories)
  say: only the owner can share an AMI
ec2-ami-quota-50000-per-region
  claim: An account can have at most 50,000 public and private AMIs per Region by default, including available, pending and disabled AMIs and AMIs in the Recycle Bin.
  scope: per account, per Region; default; adjustable; public and private AMIs, including disabled ones and those in the Recycle Bin.
  link: [50,000](../facts/ec2.md#ec2-ami-quota-50000-per-region)
  say: fifty thousand AMIs per Region
ec2-ami-region-specific-copy
  claim: An AMI is a Region-specific resource: to launch an instance in a Region the AMI must be in that Region, so to use one AMI in several Regions you copy it from the source Region to each target Region.
  scope: per Region.
  link: [AMIs are Region-specific resources](../facts/ec2.md#ec2-ami-region-specific-copy)
  link: [copy it from the source Region](../facts/ec2.md#ec2-ami-region-specific-copy)
  say: an AMI lives in one Region | copy the AMI to the other Region first
ec2-ami-root-volume-types
  claim: Every AMI is either EBS-backed (root volume is an EBS volume created from a snapshot; Linux and Windows) or S3-backed (root volume is an instance store volume created from a template in S3; Linux only).
  scope: AMI root volume type.
  link: [created from an Amazon EBS snapshot](../facts/ec2.md#ec2-ami-root-volume-types)
  link: [a template stored in Amazon S3](../facts/ec2.md#ec2-ami-root-volume-types)
  link: [Windows AMIs do not support instance store](../facts/ec2.md#ec2-ami-root-volume-types)
  say: Windows cannot use an instance store root volume
ec2-ami-shared-encrypted-launch-uses-your-default-key
  claim: When you launch from a shared AMI with an encrypted snapshot and supply no encryption parameters, the volume is encrypted with your own account's default KMS key; a snapshot you own stays encrypted with its original key.
  scope: instance launch from an EBS-backed AMI; default; no encryption parameters supplied.
  link: [your AWS account's default KMS key](../facts/ec2.md#ec2-ami-shared-encrypted-launch-uses-your-default-key)
  link: [encrypted to the same KMS key](../facts/ec2.md#ec2-ami-shared-encrypted-launch-uses-your-default-key)
  say: a shared encrypted AMI launches with your default KMS key
ec2-ami-sharing-quota-1000-entities
  claim: An AMI can be shared with at most 1,000 entities (organizations, organizational units and accounts) per Region by default; sharing with an organization or OU counts as one entity, not as its member accounts.
  scope: per AMI, per Region; default; adjustable; entities are organizations, OUs and accounts.
  link: [1,000](../facts/ec2.md#ec2-ami-sharing-quota-1000-entities)
  say: one thousand entities per AMI
ec2-ami-specific-to-region-os-arch
  claim: You can create an AMI from your own instance and launch instances with the same configuration from it, copy it to another Region, and share it with other accounts; one AMI can launch many instances with the same configuration.
  scope: Amazon Machine Images.
  link: [copy an AMI to another AWS Region](../facts/ec2.md#ec2-ami-specific-to-region-os-arch)
  link: [share an AMI that you created](../facts/ec2.md#ec2-ami-specific-to-region-os-arch)
  link: [launch multiple instances from a single AMI](../facts/ec2.md#ec2-ami-specific-to-region-os-arch)
  say: one AMI can launch many identical instances
ec2-ami-type-boot-time
  claim: An instance from an EBS-backed AMI usually boots in less than 1 minute; one from an S3-backed AMI usually boots in less than 5 minutes.
  scope: boot time by AMI root volume type.
  link: [Usually less than 1 minute](../facts/ec2.md#ec2-ami-type-boot-time)
  link: [Usually less than 5 minutes](../facts/ec2.md#ec2-ami-type-boot-time)
  say: usually under one minute for EBS backed | usually under five minutes for instance store backed
ec2-ami-type-modifications
  claim: For an EBS-backed AMI the instance type, kernel, RAM disk and user data can be changed while the instance is stopped; for an S3-backed AMI the instance attributes are fixed for the life of the instance.
  scope: AMI root volume type.
  link: [can be changed while the instance is stopped](../facts/ec2.md#ec2-ami-type-modifications)
  link: [fixed for the life of an instance](../facts/ec2.md#ec2-ami-type-modifications)
  say: an instance store backed instance keeps its attributes for life
ec2-ami-type-stopped-state
  claim: An instance from an EBS-backed AMI can be in a stopped state, with its root volume kept in EBS while it is not running; an instance from an S3-backed (instance store) AMI cannot be stopped and is either running or terminated.
  scope: AMI root volume type.
  link: [Can be in a stopped state](../facts/ec2.md#ec2-ami-type-stopped-state)
  link: [Cannot be in a stopped state](../facts/ec2.md#ec2-ami-type-stopped-state)
  say: an instance store backed instance is either running or terminated
ec2-api-private-via-privatelink
  claim: To call the Amazon EC2 API from your VPC using private IP addresses, you use AWS PrivateLink.
  scope: Amazon EC2 API access from a VPC.
  link: [use AWS PrivateLink](../facts/ec2.md#ec2-api-private-via-privatelink)
  say: an interface endpoint with PrivateLink
ec2-api-tls-1-2-required
  claim: Clients that call the Amazon EC2 API must support TLS; AWS requires TLS 1.2 and recommends TLS 1.3.
  scope: clients of the Amazon EC2 API; minimum.
  link: [TLS 1.2](../facts/ec2.md#ec2-api-tls-1-2-required)
  link: [TLS 1.3](../facts/ec2.md#ec2-api-tls-1-2-required)
  say: TLS one point two | TLS one point three recommended
ec2-batch-delayable-workloads-spot
  claim: For background or batch workloads that can be delayed or rescheduled without significant impact, Spot Instances give significant cost savings because an occasional interruption is a small business risk.
  scope: background or batch processing workloads; the work can be delayed or rescheduled.
  link: [Spot Instances offer significant cost savings](../facts/ec2.md#ec2-batch-delayable-workloads-spot)
  say: Spot, because a delay costs little
ec2-bp-basic-failover-eni-or-eip
  claim: For a basic failover solution, you can manually attach a network interface or Elastic IP address to a replacement instance; for an automated solution you can use Amazon EC2 Auto Scaling.
  scope: EC2 backup and recovery best practices.
  link: [attach a network interface or Elastic IP address](../facts/ec2.md#ec2-bp-basic-failover-eni-or-eip)
  say: move the network interface or Elastic IP to a new instance
ec2-bp-iam-roles-and-federation
  claim: The EC2 best practices say to manage access to AWS resources and APIs with identity federation through an identity provider and IAM roles whenever possible.
  scope: EC2 security best practices.
  link: [identity federation with an identity provider](../facts/ec2.md#ec2-bp-iam-roles-and-federation)
  say: use federation and IAM roles
ec2-bp-inspector-scan-vulnerabilities
  claim: Amazon Inspector automatically discovers and scans EC2 instances for software vulnerabilities and unintended network exposure.
  scope: EC2 security best practices.
  link: [software vulnerabilities and unintended network exposure](../facts/ec2.md#ec2-bp-inspector-scan-vulnerabilities)
  say: Amazon Inspector scans for vulnerabilities
ec2-bp-least-permissive-security-group
  claim: The EC2 best practices say to implement the least permissive rules for your security group.
  scope: EC2 security best practices.
  link: [the least permissive rules for your security group](../facts/ec2.md#ec2-bp-least-permissive-security-group)
  say: least permissive security group rules
ec2-bp-multi-az-critical-components
  claim: The EC2 best practices say to deploy critical components of your application across multiple Availability Zones and replicate your data appropriately.
  scope: EC2 backup and recovery best practices.
  link: [across multiple Availability Zones](../facts/ec2.md#ec2-bp-multi-az-critical-components)
  say: spread critical parts across Availability Zones
ec2-bp-request-limit-increases-in-advance
  claim: The EC2 best practices say to plan to request any limit increases in advance of the time you will need them.
  scope: EC2 resource management best practices.
  link: [request any limit increases in advance](../facts/ec2.md#ec2-bp-request-limit-increases-in-advance)
  say: ask for quota increases before you need them
ec2-bp-separate-ebs-for-os-and-data
  claim: The EC2 best practices say to use separate EBS volumes for the operating system and for your data, and to make sure the data volume persists after instance termination.
  scope: EC2 storage best practices.
  link: [separate Amazon EBS volumes for the operating system](../facts/ec2.md#ec2-bp-separate-ebs-for-os-and-data)
  say: one volume for the OS, another for data
ec2-burstable-baseline-burst-any-time
  claim: The T instance family provides a baseline CPU performance with the ability to burst above the baseline at any time for as long as required.
  scope: T instance family; bursting uses CPU credits; in unlimited mode surplus credits are charged.
  link: [burst above the baseline at any time](../facts/ec2.md#ec2-burstable-baseline-burst-any-time)
  say: it bursts above its baseline
ec2-burstable-cpu-credit-one-core-one-minute
  claim: A CPU credit provides the performance of a full CPU core for 1 minute.
  scope: per CPU credit; fixed; burstable performance instances.
  link: [a full CPU core for one minute](../facts/ec2.md#ec2-burstable-cpu-credit-one-core-one-minute)
  say: one full core for one minute
ec2-burstable-credit-accrual-limit-24-hours
  claim: The CPU credit accrual limit depends on the instance size and is in general equal to the maximum credits earned in 24 hours.
  scope: per burstable instance; maximum; not adjustable; depends on the instance size.
  link: [maximum credits earned in 24 hours](../facts/ec2.md#ec2-burstable-credit-accrual-limit-24-hours)
  say: about one day of earned credits
ec2-burstable-credits-after-stop-t2-lost-t3-7-days
  claim: CPU credits on a running instance do not expire; a T2 instance loses all accrued credits when it stops, while T8i, T4g, T3a and T3 keep the credit balance for 7 days after a stop.
  scope: per burstable instance; fixed; T2 versus T8i, T4g, T3a and T3.
  link: [credits on a running instance do not expire](../facts/ec2.md#ec2-burstable-credits-after-stop-t2-lost-t3-7-days)
  link: [the instance loses all its accrued credits](../facts/ec2.md#ec2-burstable-credits-after-stop-t2-lost-t3-7-days)
  link: [persists for seven days after an instance stops](../facts/ec2.md#ec2-burstable-credits-after-stop-t2-lost-t3-7-days)
  say: credits do not expire while running | T2 loses its credits on stop | T3 and newer keep credits for seven days
ec2-burstable-low-utilization-waste-use-t
  claim: Low-to-moderate CPU utilization workloads waste CPU cycles, so you pay for more than you use; low-cost burstable T instances address this.
  scope: workloads with low-to-moderate CPU utilization.
  link: [the low-cost burstable general purpose instances](../facts/ec2.md#ec2-burstable-low-utilization-waste-use-t)
  say: a burstable T instance
ec2-burstable-spot-standard-mode-recommended
  claim: Spot Instances launched as unlimited and used immediately for a short time with no idle time to earn credits incur surplus credit charges, so AWS recommends launching T4g and T3 Spot Instances in standard mode.
  scope: per burstable Spot Instance.
  link: [launch your T4g or T3 Spot Instances in standard mode to avoid paying higher costs](../facts/ec2.md#ec2-burstable-spot-standard-mode-recommended)
  say: standard mode for Spot T instances
ec2-burstable-standard-earn-spend-credits
  claim: A burstable performance instance continuously earns CPU credits when it stays below its CPU baseline and spends credits when it bursts above the baseline.
  scope: burstable performance instances.
  link: [stays below the CPU baseline](../facts/ec2.md#ec2-burstable-standard-earn-spend-credits)
  link: [spends credits when it bursts above the baseline](../facts/ec2.md#ec2-burstable-standard-earn-spend-credits)
  say: it earns credits below the baseline | it spends credits above the baseline
ec2-burstable-standard-no-credits-down-to-baseline
  claim: In Standard mode, a burstable performance instance uses its accrued credits to burst above baseline CPU utilization; if there are no accrued credits remaining, the instance gradually comes down to baseline CPU utilization and cannot burst above baseline until it accrues more credits.
  scope: burstable performance instances in Standard mode; no accrued credits remaining.
  link: [gradually comes down to baseline CPU utilization](../facts/ec2.md#ec2-burstable-standard-no-credits-down-to-baseline)
  link: [cannot burst above baseline](../facts/ec2.md#ec2-burstable-standard-no-credits-down-to-baseline)
  say: it slowly falls to the baseline | no bursting until it earns credits again
ec2-burstable-t-vs-m-savings-and-smallest-size
  claim: T instances can save up to 15% compared with M instances and come in sizes as small as 2 vCPUs and 0.5 GiB of memory; the burstable family is T8i, T4g, T3a and T3, plus the previous generation T2.
  scope: T instance family.
  link: [up to 15%](../facts/ec2.md#ec2-burstable-t-vs-m-savings-and-smallest-size)
  link: [as low as 2 vCPUs and 0.5 GiB of memory](../facts/ec2.md#ec2-burstable-t-vs-m-savings-and-smallest-size)
  link: [T8i, T4g, T3a, and T3 instance types, and the previous generation T2 instance types](../facts/ec2.md#ec2-burstable-t-vs-m-savings-and-smallest-size)
  say: up to fifteen percent less than M | two vCPUs and half a gibibyte
ec2-burstable-t2-launch-credits-standard-mode
  claim: Only T2 instances in Standard mode get launch credits; T8i, T4g, T3a and T3 instances earn no launch credits.
  scope: per burstable instance.
  link: [Only applicable for T2 instances configured for Standard mode.](../facts/ec2.md#ec2-burstable-t2-launch-credits-standard-mode)
  link: [T8i, T4g, T3a, and T3 instances do not earn launch credits.](../facts/ec2.md#ec2-burstable-t2-launch-credits-standard-mode)
  say: only T2 in Standard mode | T3 and newer get no launch credits
ec2-burstable-unlimited-24-hour-baseline-rule
  claim: In unlimited mode the hourly price covers all CPU spikes as long as average CPU utilization stays at or below the baseline over a rolling 24-hour period (or the instance lifetime, if shorter); sustained use above baseline is charged at a flat additional rate per vCPU-hour.
  scope: per burstable instance in unlimited mode.
  link: [rolling 24-hour period](../facts/ec2.md#ec2-burstable-unlimited-24-hour-baseline-rule)
  link: [flat additional rate per vCPU-hour](../facts/ec2.md#ec2-burstable-unlimited-24-hour-baseline-rule)
  say: a rolling twenty-four-hour window | a flat rate per vCPU-hour
ec2-burstable-unlimited-credit-price-per-vcpu-hour
  claim: In unlimited mode surplus CPU credits cost $0.05 per vCPU-hour for T2 and T3 on Linux, $0.04 for T4g and $0.06 for T8i; the credit price is the same for all sizes, for On-Demand, Spot and Reserved Instances, and in every Region.
  scope: per vCPU-hour of surplus credits; fixed; Linux, RHEL and SLES; Windows rates are higher.
  link: [$0.05 per vCPU-Hour](../facts/ec2.md#ec2-burstable-unlimited-credit-price-per-vcpu-hour)
  link: [$0.04 per vCPU-Hour](../facts/ec2.md#ec2-burstable-unlimited-credit-price-per-vcpu-hour)
  link: [$0.06 per vCPU-Hour](../facts/ec2.md#ec2-burstable-unlimited-credit-price-per-vcpu-hour)
  link: [the same for all instance sizes](../facts/ec2.md#ec2-burstable-unlimited-credit-price-per-vcpu-hour)
  say: five cents per vCPU-hour for T2 and T3 | four cents for T4g | six cents for T8i
ec2-burstable-unlimited-default-t3-and-newer
  claim: T8i, T4g, T3a and T3 instances launch in unlimited mode by default and earn no launch credits, so they can burst immediately; T3 instances on a Dedicated Host launch as standard, and unlimited mode is not supported there.
  scope: per burstable instance; default; adjustable; the account default credit specification can be changed.
  link: [These instances launch as unlimited by default](../facts/ec2.md#ec2-burstable-unlimited-default-t3-and-newer)
  link: [T3 instances launched on a Dedicated Host launch as standard by default](../facts/ec2.md#ec2-burstable-unlimited-default-t3-and-newer)
  say: T3 and newer launch as unlimited by default | T3 on a Dedicated Host launches as standard
ec2-capacity-blocks-duration-1-to-182-days
  claim: Capacity Blocks can be reserved for durations from 1 to 182 days, and can start within minutes of purchase or at a scheduled future date.
  scope: per Capacity Block; maximum; not adjustable.
  link: [from 1 to 182 days](../facts/ec2.md#ec2-capacity-blocks-duration-1-to-182-days)
  say: from one day to one hundred eighty-two days
ec2-capacity-blocks-instance-limits-64-and-256
  claim: Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.
  scope: per Capacity Block; across Capacity Blocks; maximum; not adjustable.
  link: [up to 64 instances](../facts/ec2.md#ec2-capacity-blocks-instance-limits-64-and-256)
  link: [up to 256 instances across Capacity Blocks](../facts/ec2.md#ec2-capacity-blocks-instance-limits-64-and-256)
  say: up to sixty-four instances per block | up to two hundred fifty-six across blocks
ec2-capacity-blocks-no-sp-or-ri-discount
  claim: Unlike On-Demand Capacity Reservations, Capacity Blocks for ML pricing cannot be combined with Savings Plans or Reserved Instance discounts.
  scope: Capacity Blocks for ML.
  link: [cannot be combined with Savings Plans](../facts/ec2.md#ec2-capacity-blocks-no-sp-or-ri-discount)
  say: no, Capacity Blocks get no Savings Plans or Reserved Instance discount
ec2-capacity-blocks-paid-upfront
  claim: The price of a Capacity Block depends on supply and demand at the time of purchase and is charged up front when the reservation is made; after you reserve it, the price doesn't change.
  scope: per Capacity Block.
  link: [charged up front](../facts/ec2.md#ec2-capacity-blocks-paid-upfront)
  link: [the price doesn't change](../facts/ec2.md#ec2-capacity-blocks-paid-upfront)
  say: you pay up front when you reserve | after you reserve, the price stays fixed
ec2-capacity-reservation-auto-match-attributes
  claim: By default, Capacity Reservations automatically match new and running instances with matching attributes (instance type, platform, Availability Zone and tenancy); you can instead target a reservation so only chosen instances run in it.
  scope: Capacity Reservation instance matching; default; adjustable; open Capacity Reservations.
  link: [automatically match new instances and running instances](../facts/ec2.md#ec2-capacity-reservation-auto-match-attributes)
  link: [instance type, platform, Availability Zone, and tenancy](../facts/ec2.md#ec2-capacity-reservation-auto-match-attributes)
  link: [you can also target a Capacity Reservation](../facts/ec2.md#ec2-capacity-reservation-auto-match-attributes)
  say: by default matching instances use the reservation automatically | type, platform, Availability Zone and tenancy must match
ec2-capacity-reservation-billed-per-second-60s-minimum
  claim: Capacity Reservations are billed at per-second granularity with a minimum of 60 seconds, starting when the reservation is provisioned in the account.
  scope: per Capacity Reservation; future-dated reservations start billing at the requested date.
  link: [per-second granularity, with a minimum of 60 seconds](../facts/ec2.md#ec2-capacity-reservation-billed-per-second-60s-minimum)
  link: [as soon as the Capacity Reservation is provisioned](../facts/ec2.md#ec2-capacity-reservation-billed-per-second-60s-minimum)
  say: per second, with a one-minute minimum | billing starts when it is provisioned
ec2-capacity-reservation-cancellation-rates
  claim: Cancelling a future-dated Capacity Reservation 8 or more weeks before the original start date has no charge; 2 to 8 weeks before costs at least 25% of the total commitment; within 2 weeks of the start date costs at least 50% of the total commitment; after delivery, during the commitment, at least 50% of the remaining commitment.
  scope: future-dated Capacity Reservation cancellation; minimum; minimum cancellation rate; the cancellation quote sets the exact charge.
  link: [8 or more weeks before the original start date](../facts/ec2.md#ec2-capacity-reservation-cancellation-rates)
  link: [25% of total commitment](../facts/ec2.md#ec2-capacity-reservation-cancellation-rates)
  link: [50% of total commitment](../facts/ec2.md#ec2-capacity-reservation-cancellation-rates)
  say: eight weeks or more before the start: no charge | two to eight weeks before: a quarter of the commitment | within two weeks: half of the commitment
ec2-capacity-reservation-charged-used-or-not
  claim: Capacity Reservations are charged at the equivalent On-Demand rate whether or not you run instances in the reserved capacity; when a matching instance runs, you pay for the instance and nothing for the reservation, with no upfront or additional charges.
  scope: Capacity Reservation pricing.
  link: [charged at the equivalent On-Demand rate](../facts/ec2.md#ec2-capacity-reservation-charged-used-or-not)
  link: [nothing for the reservation](../facts/ec2.md#ec2-capacity-reservation-charged-used-or-not)
  link: [no upfront or additional charges](../facts/ec2.md#ec2-capacity-reservation-charged-used-or-not)
  say: you pay the On-Demand rate whether you use it or not | a matching running instance covers the reservation
ec2-capacity-reservation-discount-from-sp-or-regional-ri
  claim: Billing discounts of Savings Plans and Regional Reserved Instances apply to Capacity Reservations with matching attributes; billing discounts of zonal Reserved Instances do not apply to Capacity Reservations.
  scope: Capacity Reservation billing discounts; the Capacity Reservation has matching attributes.
  link: [Savings Plans and Regional Reserved Instances apply](../facts/ec2.md#ec2-capacity-reservation-discount-from-sp-or-regional-ri)
  link: [zonal Reserved Instances do not apply](../facts/ec2.md#ec2-capacity-reservation-discount-from-sp-or-regional-ri)
  say: Savings Plans and regional Reserved Instances discount a Capacity Reservation | zonal Reserved Instance discounts do not apply
ec2-capacity-reservation-future-dated-commitment-rules
  claim: For a future-dated Capacity Reservation you choose the start date and a commitment duration; billing starts at that date, and during the commitment you can't lower the instance count or the commitment duration below the initial commitment. After the commitment elapses you can modify it in any way or cancel it without charge.
  scope: future-dated Capacity Reservation; during the commitment duration.
  link: [you can't decrease the instance count](../facts/ec2.md#ec2-capacity-reservation-future-dated-commitment-rules)
  link: [cancel it without charge](../facts/ec2.md#ec2-capacity-reservation-future-dated-commitment-rules)
  say: during the commitment you can't lower the count or the duration | after the commitment you can change or cancel it for free
ec2-capacity-reservation-future-dated-lead-time-5-to-120-days
  claim: You can create a Capacity Reservation for immediate use, or request one to be delivered between 5 and 120 days in the future.
  scope: per Capacity Reservation request; maximum; not adjustable; future-dated request.
  link: [between 5 and 120 days in the future](../facts/ec2.md#ec2-capacity-reservation-future-dated-lead-time-5-to-120-days)
  say: between five and one hundred twenty days ahead
ec2-capacity-reservation-future-dated-min-32-vcpus
  claim: A future-dated Capacity Reservation must be for an instance count with at least 32 vCPUs, for example at least 8 m5.xlarge instances.
  scope: per future-dated Capacity Reservation; minimum; not adjustable; families C, G, I, M, R, T, U and X.
  link: [a minimum of 32 vCPUs](../facts/ec2.md#ec2-capacity-reservation-future-dated-min-32-vcpus)
  say: at least thirty-two vCPUs
ec2-capacity-reservation-immediate-cancel-free
  claim: Cancelling a Capacity Reservation that is active with no commitment duration, or whose commitment duration has elapsed, is free; instances that were running in it keep running at On-Demand rates or at a matching Savings Plans or Regional Reserved Instance rate.
  scope: Capacity Reservation cancellation; active with no commitment duration or an elapsed commitment duration.
  link: [cancellation is free](../facts/ec2.md#ec2-capacity-reservation-immediate-cancel-free)
  link: [the instances continue to run normally](../facts/ec2.md#ec2-capacity-reservation-immediate-cancel-free)
  say: cancelling a reservation without a commitment is free | running instances keep running
ec2-capacity-reservation-immediate-no-term
  claim: Capacity Reservations reserve capacity in a specific Availability Zone for any duration; one for immediate use has no term commitment and can be modified or cancelled at any time.
  scope: per Capacity Reservation; immediate-use reservations; future-dated reservations have a commitment duration and a possible cancellation charge.
  link: [in a specific Availability Zone for any duration](../facts/ec2.md#ec2-capacity-reservation-immediate-no-term)
  link: [there is no term commitment](../facts/ec2.md#ec2-capacity-reservation-immediate-no-term)
  say: one Availability Zone, any duration | no term commitment
ec2-capacity-reservation-no-hibernate-resume-guarantee
  claim: Capacity Reservations do not ensure that a hibernated instance can resume after you try to start it.
  scope: Capacity Reservations and hibernation.
  link: [not ensure that a hibernated instance can resume](../facts/ec2.md#ec2-capacity-reservation-no-hibernate-resume-guarantee)
  link: [after you try to start it](../facts/ec2.md#ec2-capacity-reservation-no-hibernate-resume-guarantee)
  say: a Capacity Reservation does not guarantee a hibernated instance resumes
ec2-capacity-reservation-not-dedicated-hosts
  claim: Capacity Reservations cannot be used with Dedicated Hosts, but they can be used with Dedicated Instances.
  scope: Capacity Reservations.
  link: [Capacity Reservations can't be used with Dedicated Hosts](../facts/ec2.md#ec2-capacity-reservation-not-dedicated-hosts)
  link: [Capacity Reservations can be used with Dedicated Instances](../facts/ec2.md#ec2-capacity-reservation-not-dedicated-hosts)
  say: not with Dedicated Hosts | yes with Dedicated Instances
ec2-capacity-reservation-not-transferable-shareable
  claim: Capacity Reservations are not transferable from one AWS account to another, but they can be shared with other AWS accounts.
  scope: Capacity Reservations.
  link: [not transferable from one AWS account to another](../facts/ec2.md#ec2-capacity-reservation-not-transferable-shareable)
  link: [you can share Capacity Reservations](../facts/ec2.md#ec2-capacity-reservation-not-transferable-shareable)
  say: you cannot transfer a Capacity Reservation | but you can share it with other accounts
ec2-capacity-reservation-placement-group-cluster-only
  claim: Capacity Reservations can be created in cluster placement groups; spread and partition placement groups are not supported.
  scope: Capacity Reservations.
  link: [can be created in cluster placement groups](../facts/ec2.md#ec2-capacity-reservation-placement-group-cluster-only)
  link: [Spread and partition placement groups are not supported](../facts/ec2.md#ec2-capacity-reservation-placement-group-cluster-only)
  say: only cluster placement groups support Capacity Reservations | spread and partition groups do not
ec2-capacity-reservations-count-toward-on-demand-quota
  claim: Capacity Reservations count toward the On-Demand Instance quotas even when they are unused.
  scope: per account, per Region.
  link: [count toward your On-Demand Instance quotas](../facts/ec2.md#ec2-capacity-reservations-count-toward-on-demand-quota)
  link: [even if they are unused](../facts/ec2.md#ec2-capacity-reservations-count-toward-on-demand-quota)
  say: count toward the On-Demand quota even if unused | even when unused
ec2-case-logzio-graviton-30-percent
  claim: Migrating to AWS Graviton-based instances improved Logz.io's performance and let the company reduce its infrastructure costs by up to 30 percent, double what it had expected.
  scope: Logz.io OpenSearch and ingestion workloads (AWS case study); maximum.
  link: [up to 30 percent](../facts/ec2.md#ec2-case-logzio-graviton-30-percent)
  say: up to thirty percent lower infrastructure cost
ec2-case-nasa-jpl-critical-on-demand-and-odcr
  claim: The NASA JPL case study says that, for critical processing, JPL will also use EC2 On-Demand pricing with no long-term commitments and On-Demand Capacity Reservations to create and manage reserved capacity.
  scope: NASA JPL satellite data processing (AWS case study).
  link: [For critical processing](../facts/ec2.md#ec2-case-nasa-jpl-critical-on-demand-and-odcr)
  link: [On-Demand Capacity Reservations](../facts/ec2.md#ec2-case-nasa-jpl-critical-on-demand-and-odcr)
  say: On-Demand plus Capacity Reservations for the critical part | On-Demand Capacity Reservations
ec2-case-nasa-jpl-spot-fault-tolerant
  claim: The NASA JPL case study says that, since most of the satellite data processing system is fault tolerant, JPL will take advantage of Spot Instances for scaling.
  scope: NASA JPL satellite data processing (AWS case study).
  link: [most of the processing system is fault tolerant](../facts/ec2.md#ec2-case-nasa-jpl-spot-fault-tolerant)
  say: the processing is fault tolerant, so JPL scales on Spot
ec2-case-smartnews-graviton-ml-15-percent
  claim: SmartNews lowered the compute costs of its ML workloads by 15 percent by using AWS Graviton.
  scope: SmartNews ML workloads (AWS case study).
  link: [by 15 percent](../facts/ec2.md#ec2-case-smartnews-graviton-ml-15-percent)
  say: fifteen percent lower compute cost
ec2-case-smartnews-price-capacity-optimized
  claim: SmartNews scales its capacity up and down on AWS and uses an internal monitoring system with best practices such as a price-capacity optimized allocation strategy.
  scope: SmartNews Spot usage (AWS case study).
  link: [a price-capacity optimized allocation strategy](../facts/ec2.md#ec2-case-smartnews-price-capacity-optimized)
  say: price-capacity optimized allocation
ec2-case-smartnews-spot-50-percent
  claim: By using Spot Instances, SmartNews cut costs for its main compute workload by up to 50 percent.
  scope: SmartNews main compute workload (AWS case study); maximum.
  link: [up to 50 percent](../facts/ec2.md#ec2-case-smartnews-spot-50-percent)
  say: up to fifty percent
ec2-change-allowed-amis-2024-12
  claim: On 2024-12-01 Amazon EC2 added Allowed AMIs, which let you control the discovery and use of AMIs by specifying criteria that AMIs must meet.
  scope: per account.
  link: [2024-12-01](../facts/ec2.md#ec2-change-allowed-amis-2024-12)
  link: [control the discovery and use of AMIs](../facts/ec2.md#ec2-change-allowed-amis-2024-12)
  say: December first, twenty twenty-four
ec2-change-amazon-linux-2-end-of-support-2026-06
  claim: Amazon Linux 2 reached its end of support on 2026-06-30 and no longer receives standard security updates; AWS tells customers to migrate to Amazon Linux 2023 (AL2023), which is supported until June 2029.
  scope: Amazon Linux AMIs.
  link: [2026-06-30](../facts/ec2.md#ec2-change-amazon-linux-2-end-of-support-2026-06)
  link: [Customers should migrate to Amazon Linux 2023 (AL2023)](../facts/ec2.md#ec2-change-amazon-linux-2-end-of-support-2026-06)
  link: [supported until June 2029](../facts/ec2.md#ec2-change-amazon-linux-2-end-of-support-2026-06)
  say: June thirtieth, twenty twenty-six | move to Amazon Linux twenty twenty-three | AL2023 is supported until June twenty twenty-nine
ec2-change-ami-block-public-access-default-2023-10
  claim: On 2023-10-20 block public access for AMIs became enabled by default for all new accounts and for existing accounts with no public AMIs.
  scope: per account; default; new accounts and existing accounts with no public AMIs.
  link: [2023-10-20](../facts/ec2.md#ec2-change-ami-block-public-access-default-2023-10)
  link: [now enabled by default for all new accounts](../facts/ec2.md#ec2-change-ami-block-public-access-default-2023-10)
  say: October twentieth, twenty twenty-three
ec2-change-ami-compatible-instance-types-2026-09
  claim: On 2026-09-04 AWS announced that AMI owners can specify supported or unsupported instance types for their AMIs, and a launch on a non-permitted type is blocked; by default an AMI can still be launched on any instance type.
  scope: per AMI; default; set by the AMI owner.
  link: [2026-09-04](../facts/ec2.md#ec2-change-ami-compatible-instance-types-2026-09)
  link: [non-permitted instance type is automatically blocked](../facts/ec2.md#ec2-change-ami-compatible-instance-types-2026-09)
  link: [launched on any instance type](../facts/ec2.md#ec2-change-ami-compatible-instance-types-2026-09)
  say: September fourth, twenty twenty-six
ec2-change-capacity-blocks-6-months-2024-11
  claim: On 2024-11-21 Amazon EC2 made it possible to reserve Capacity Blocks for ML for up to 6 months (182 days).
  scope: per Capacity Block; maximum.
  link: [2024-11-21](../facts/ec2.md#ec2-change-capacity-blocks-6-months-2024-11)
  link: [up to 6 months (182 days)](../facts/ec2.md#ec2-change-capacity-blocks-6-months-2024-11)
  say: November twenty-first, twenty twenty-four | up to six months
ec2-change-capacity-blocks-instant-start-2024-11
  claim: On 2024-11-21 Amazon EC2 added Capacity Blocks for ML that can start as soon as 30 minutes after purchase, and the option to extend an existing Capacity Block.
  scope: Capacity Blocks for ML.
  link: [2024-11-21](../facts/ec2.md#ec2-change-capacity-blocks-instant-start-2024-11)
  link: [can start as soon as 30 minutes](../facts/ec2.md#ec2-change-capacity-blocks-instant-start-2024-11)
  link: [extend the duration of existing Capacity Blocks](../facts/ec2.md#ec2-change-capacity-blocks-instant-start-2024-11)
  say: November twenty-first, twenty twenty-four | can start in as little as thirty minutes
ec2-change-capacity-blocks-sharing-local-zones-2026-02
  claim: In February 2026 Capacity Blocks for ML gained two options: on February 2, 2026 you can share them with other accounts in your AWS organization, and on February 25, 2026 they became available in Local Zones.
  scope: Capacity Blocks for ML; UltraServer Capacity Blocks can't be shared.
  link: [share EC2 Capacity Blocks with other AWS accounts](../facts/ec2.md#ec2-change-capacity-blocks-sharing-local-zones-2026-02)
  link: [now available in Local Zones](../facts/ec2.md#ec2-change-capacity-blocks-sharing-local-zones-2026-02)
  say: you can share Capacity Blocks inside your organization
ec2-change-capacity-reservations-only-2024-11
  claim: On 2024-11-20 Amazon EC2 made it possible to specify that instances run only in a Capacity Reservation or a Capacity Reservation resource group.
  scope: instance launches.
  link: [2024-11-20](../facts/ec2.md#ec2-change-capacity-reservations-only-2024-11)
  link: [only run in a Capacity Reservation](../facts/ec2.md#ec2-change-capacity-reservations-only-2024-11)
  say: November twentieth, twenty twenty-four
ec2-change-eip-transfer-between-accounts-2022-10
  claim: On 2022-10-31 Amazon EC2 made it possible to transfer Elastic IP addresses from one AWS account to another.
  scope: Elastic IP addresses.
  link: [2022-10-31](../facts/ec2.md#ec2-change-eip-transfer-between-accounts-2022-10)
  link: [transfer Elastic IP addresses](../facts/ec2.md#ec2-change-eip-transfer-between-accounts-2022-10)
  say: October thirty-first, twenty twenty-two
ec2-change-future-dated-cr-2024-11
  claim: On 2024-11-21 Amazon EC2 added future-dated Capacity Reservations: you can request a Capacity Reservation for a future date instead of only for immediate use.
  scope: On-Demand Capacity Reservations.
  link: [2024-11-21](../facts/ec2.md#ec2-change-future-dated-cr-2024-11)
  link: [request Capacity Reservations for a future date](../facts/ec2.md#ec2-change-future-dated-cr-2024-11)
  say: November twenty-first, twenty twenty-four
ec2-change-future-dated-cr-cancel-2026-06
  claim: The Amazon EC2 User Guide document history entry dated 2026-06-02 says you can cancel a future-dated Capacity Reservation, and that depending on when you cancel, a charge may apply; a What's New post announced the same change in June 2026.
  scope: future-dated Capacity Reservation; a charge may apply.
  link: [2026-06-02](../facts/ec2.md#ec2-change-future-dated-cr-cancel-2026-06)
  link: [You can cancel a future-dated Capacity Reservation.](../facts/ec2.md#ec2-change-future-dated-cr-cancel-2026-06)
  say: June second, twenty twenty-six, in the document history
ec2-change-future-dated-cr-postpone-2026-09
  claim: On 2026-09-28 AWS announced that you can postpone the start date of a future-dated Capacity Reservation before delivery; the commitment duration can increase, depending on when you postpone.
  scope: future-dated Capacity Reservation; before delivery.
  link: [2026-09-28](../facts/ec2.md#ec2-change-future-dated-cr-postpone-2026-09)
  link: [you can now postpone your start date](../facts/ec2.md#ec2-change-future-dated-cr-postpone-2026-09)
  say: September twenty-eighth, twenty twenty-six
ec2-change-global-view-renamed-2026-06
  claim: On 2026-06-30 EC2 Global View was renamed AWS Global View; it shows EC2 resources and other supported AWS resources across all Regions in a single view.
  scope: console feature.
  link: [2026-06-30](../facts/ec2.md#ec2-change-global-view-renamed-2026-06)
  link: [now renamed AWS Global View](../facts/ec2.md#ec2-change-global-view-renamed-2026-06)
  say: June thirtieth, twenty twenty-six
ec2-change-graviton4-m8g-c8g-r8g-2024
  claim: AWS Graviton4 instance families arrived as follows: memory optimized R8g on July 9, 2024, and general purpose M8g and compute optimized C8g on September 25, 2024.
  scope: instance families.
  link: [July 9, 2024](../facts/ec2.md#ec2-change-graviton4-m8g-c8g-r8g-2024)
  link: [September 25, 2024](../facts/ec2.md#ec2-change-graviton4-m8g-c8g-r8g-2024)
  say: R8g in July twenty twenty-four | M8g and C8g in September twenty twenty-four
ec2-change-graviton5-m9g-r9g-2026
  claim: The EC2 Instance Types Guide document history lists general purpose M9g and M9gd instances powered by AWS Graviton5 on June 9, 2026, new compute optimized C9g and C9gd instances on June 30, 2026, and memory optimized R9g and R9gd instances powered by AWS Graviton5 on August 31, 2026.
  scope: instance families listed in the Instance Types Guide document history.
  link: [June 9, 2026](../facts/ec2.md#ec2-change-graviton5-m9g-r9g-2026)
  link: [June 30, 2026](../facts/ec2.md#ec2-change-graviton5-m9g-r9g-2026)
  link: [August 31, 2026](../facts/ec2.md#ec2-change-graviton5-m9g-r9g-2026)
  say: M9g in June twenty twenty-six | C9g at the end of June twenty twenty-six | R9g in August twenty twenty-six
ec2-change-hibernation-graviton-2024-07
  claim: On 2024-07-30 hibernation became available for newly launched instances on the Graviton types C6g, C6gn, C6gd, C7g, C7gd, M6g, M6gd, M7g, M7gd, R6g and R6gd, launched from an Amazon Linux or Ubuntu AMI that supports Graviton instance types.
  scope: newly launched instances; supported Graviton instance types and AMIs.
  link: [2024-07-30](../facts/ec2.md#ec2-change-hibernation-graviton-2024-07)
  link: [an Amazon Linux or Ubuntu AMI](../facts/ec2.md#ec2-change-hibernation-graviton-2024-07)
  say: July thirtieth, twenty twenty-four
ec2-change-imdsv2-account-default-2024-03
  claim: On 2024-03-25 Amazon EC2 made it possible to set IMDSv2 as the account default, so that all new instance launches in the account use IMDSv2 by default.
  scope: per account.
  link: [2024-03-25](../facts/ec2.md#ec2-change-imdsv2-account-default-2024-03)
  link: [set all new EC2 instance launches](../facts/ec2.md#ec2-change-imdsv2-account-default-2024-03)
  say: March twenty-fifth, twenty twenty-four
ec2-change-imdsv2-enforcement-2026-02
  claim: On 2026-02-24 Amazon EC2 added account-level IMDSv2 enforcement for each Region: when enforced, instances can only launch if they are configured to require IMDSv2.
  scope: per account, per Region.
  link: [2026-02-24](../facts/ec2.md#ec2-change-imdsv2-enforcement-2026-02)
  link: [enforce the use of IMDSv2](../facts/ec2.md#ec2-change-imdsv2-enforcement-2026-02)
  say: February twenty-fourth, twenty twenty-six
ec2-change-instance-connect-endpoint-2023-06
  claim: On 2023-06-13 Amazon EC2 added EC2 Instance Connect Endpoint, which lets you connect to an instance through SSH or RDP without the instance having a public IPv4 address.
  scope: instances in a VPC.
  link: [2023-06-13](../facts/ec2.md#ec2-change-instance-connect-endpoint-2023-06)
  link: [through SSH or RDP](../facts/ec2.md#ec2-change-instance-connect-endpoint-2023-06)
  say: June thirteenth, twenty twenty-three
ec2-change-interruptible-cr-2025-11
  claim: On 2025-11-21 Amazon EC2 added interruptible Capacity Reservations, which make unused reserved capacity temporarily available for other workloads within your account.
  scope: On-Demand Capacity Reservations.
  link: [2025-11-21](../facts/ec2.md#ec2-change-interruptible-cr-2025-11)
  link: [make unused capacity temporarily available](../facts/ec2.md#ec2-change-interruptible-cr-2025-11)
  say: November twenty-first, twenty twenty-five
ec2-change-managed-instances-console-2024-12
  claim: On 2024-12-01 Amazon EC2 managed instances became visible in the EC2 console.
  scope: EC2 console.
  link: [2024-12-01](../facts/ec2.md#ec2-change-managed-instances-console-2024-12)
  link: [view Amazon EC2 managed instances](../facts/ec2.md#ec2-change-managed-instances-console-2024-12)
  say: December first, twenty twenty-four
ec2-change-nested-virtualization-2026-02
  claim: On 2026-02-16 Amazon EC2 added nested virtualization: you can run hypervisors such as Hyper-V and KVM inside virtualized (non-bare metal) EC2 instances; previously, customers could only create and manage virtual machines inside bare metal EC2 instances.
  scope: supported virtual instance types.
  link: [2026-02-16](../facts/ec2.md#ec2-change-nested-virtualization-2026-02)
  link: [inside virtualized Amazon EC2 instances](../facts/ec2.md#ec2-change-nested-virtualization-2026-02)
  say: February sixteenth, twenty twenty-six
  changed: 2026-02-16: was could only create and manage virtual machines inside bare metal EC2 instances
ec2-change-precision-time-placement-group-2026-06
  claim: On 2026-06-29 Amazon EC2 added the precision-time placement group, which places instances on hardware with direct access to high-precision time sources.
  scope: placement groups.
  link: [2026-06-29](../facts/ec2.md#ec2-change-precision-time-placement-group-2026-06)
  link: [use a precision-time placement group](../facts/ec2.md#ec2-change-precision-time-placement-group-2026-06)
  say: June twenty-ninth, twenty twenty-six
ec2-change-public-ipv4-charge-2024-02
  claim: AWS charges for all public IPv4 addresses, including the public IPv4 addresses of running instances and Elastic IP addresses. Before February 1, 2024, an in-use public IPv4 address (Amazon-provided or Elastic IP) assigned to resources in your VPC had no charge, while an additional (secondary) Elastic IP address on a running EC2 instance and an idle Elastic IP address were already charged.
  scope: per public IPv4 address; the pre-2024 no-charge row covered in-use addresses assigned to resources in your VPC, not a secondary or idle Elastic IP.
  link: [AWS charges for all public IPv4 addresses](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02)
  link: [No charge](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02)
  say: every public IPv4 address is charged | an in-use public IPv4 address used to be free
  changed: 2024-02-01: was No charge
ec2-change-spot-hibernation-2023-10
  claim: On 2023-10-24 Amazon EC2 made it possible to hibernate Spot Instances with the same hibernation experience and instance families that are available for On-Demand Instances.
  scope: Spot Instances.
  link: [2023-10-24](../facts/ec2.md#ec2-change-spot-hibernation-2023-10)
  link: [hibernate your Spot Instances](../facts/ec2.md#ec2-change-spot-hibernation-2023-10)
  say: October twenty-fourth, twenty twenty-three
ec2-change-t8i-2026-09
  claim: On 2026-09-15 the burstable general purpose T8i instances were added; AWS says they give up to 30% better price performance than T3, come in four sizes (nano, micro, small, medium) and use the same CPU credit system as T3 with Standard and Unlimited modes.
  scope: T8i instance family; maximum; compared to T3.
  link: [2026-09-15](../facts/ec2.md#ec2-change-t8i-2026-09)
  link: [up to 30% better price performance](../facts/ec2.md#ec2-change-t8i-2026-09)
  link: [the same CPU credit system as T3](../facts/ec2.md#ec2-change-t8i-2026-09)
  say: September fifteenth, twenty twenty-six | up to thirty percent better price performance than T3
ec2-commitment-discount-application-order
  claim: When several commitment types are active, AWS applies them in a fixed order: Reserved Instances first, then EC2 Instance Savings Plans, then Compute Savings Plans.
  scope: EC2 billing with several commitments.
  link: [Reserved Instances first, then Amazon EC2 Instance Savings Plans, then Compute Savings Plans](../facts/ec2.md#ec2-commitment-discount-application-order)
  say: Reserved Instances first, then EC2 Instance Savings Plans, then Compute Savings Plans
ec2-compute-guide-beanstalk-web-apps
  claim: Elastic Beanstalk is specifically designed for running web applications: it provides the runtime on EC2 instances, so you need to deploy just your application code.
  scope: AWS Elastic Beanstalk.
  link: [specifically designed for running web applications](../facts/ec2.md#ec2-compute-guide-beanstalk-web-apps)
  say: Beanstalk is for web apps; you bring only code
ec2-compute-guide-ec2-overhead-justified-for-control
  claim: Managing EC2 instances means responsibility for setup, scaling, patching and securing servers, which can need a dedicated operations team; the overhead is often justified where granular control over the compute environment is necessary.
  scope: choosing an AWS compute service.
  link: [granular control over the compute environment](../facts/ec2.md#ec2-compute-guide-ec2-overhead-justified-for-control)
  say: when you need granular control
ec2-compute-guide-fargate-no-servers-for-containers
  claim: AWS Fargate is a technology you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.
  scope: AWS Fargate.
  link: [run containers without having to manage servers](../facts/ec2.md#ec2-compute-guide-fargate-no-servers-for-containers)
  say: Fargate runs containers with no servers to manage
ec2-compute-guide-horizontal-for-fluctuating
  claim: The compute decision guide says horizontal scalability is essential for dynamic workloads with fluctuating demands.
  scope: choosing an AWS compute service.
  link: [Horizontal scalability is essential](../facts/ec2.md#ec2-compute-guide-horizontal-for-fluctuating)
  say: scale out for changing demand
ec2-compute-guide-lambda-no-servers
  claim: Serverless computing options like AWS Lambda run code in response to events without the need to manage servers, reducing the operational burden.
  scope: AWS Lambda compared with EC2.
  link: [without the need to manage servers](../facts/ec2.md#ec2-compute-guide-lambda-no-servers)
  say: Lambda runs code on events, with no servers to manage
ec2-compute-guide-vertical-vs-horizontal-definition
  claim: Vertical scaling (scale up) adds more power to existing infrastructure, such as more CPU or memory for an instance; horizontal scaling (scale out) adds more instances to handle the load.
  scope: choosing an AWS compute service.
  link: [increasing the CPU or memory of an instance](../facts/ec2.md#ec2-compute-guide-vertical-vs-horizontal-definition)
  link: [adding more instances to handle the load](../facts/ec2.md#ec2-compute-guide-vertical-vs-horizontal-definition)
  say: vertical means a bigger instance | horizontal means more instances
ec2-compute-optimizer-improve-performance-save-money
  claim: AWS Compute Optimizer gives EC2 recommendations to improve performance, save money, or both, by analyzing existing instance specifications and utilization metrics.
  scope: Compute Optimizer recommendations for EC2; you have opted in.
  link: [improve performance, save money, or both](../facts/ec2.md#ec2-compute-optimizer-improve-performance-save-money)
  link: [existing instance specifications and utilization metrics](../facts/ec2.md#ec2-compute-optimizer-improve-performance-save-money)
  say: better performance, lower cost, or both | it looks at the instance specs and usage metrics
ec2-compute-optimizer-no-findings-12-30-hours
  claim: Compute Optimizer might give no recommendation for an instance if you opted in less than 12 hours ago, if the instance has run for less than 30 hours, or if its instance type is not supported.
  scope: Compute Optimizer findings for EC2 instances; minimum; not adjustable; finding classification None.
  link: [less than 12 hours](../facts/ec2.md#ec2-compute-optimizer-no-findings-12-30-hours)
  link: [less than 30 hours](../facts/ec2.md#ec2-compute-optimizer-no-findings-12-30-hours)
  say: opted in less than twelve hours ago | running less than thirty hours
ec2-compute-optimizer-opt-in-required
  claim: To get recommendations from Compute Optimizer, you must first opt in to Compute Optimizer.
  scope: Compute Optimizer.
  link: [you must first opt in to Compute Optimizer](../facts/ec2.md#ec2-compute-optimizer-opt-in-required)
  say: opt in first
ec2-compute-optimizer-over-provisioned-definition
  claim: Compute Optimizer finds an EC2 instance over-provisioned when at least one specification, such as CPU, memory or network, can be sized down while still meeting the workload's performance requirements, and no specification is under-provisioned.
  scope: Compute Optimizer findings for EC2 instances.
  link: [sized down while still meeting the performance requirements](../facts/ec2.md#ec2-compute-optimizer-over-provisioned-definition)
  link: [might lead to unnecessary infrastructure cost](../facts/ec2.md#ec2-compute-optimizer-over-provisioned-definition)
  say: it can be smaller and still meet the need | it wastes money
ec2-compute-optimizer-under-provisioned-definition
  claim: Compute Optimizer finds an EC2 instance under-provisioned when at least one specification, such as CPU, memory or network, does not meet the workload's performance requirements; this might lead to poor application performance.
  scope: Compute Optimizer findings for EC2 instances.
  link: [does not meet the performance requirements](../facts/ec2.md#ec2-compute-optimizer-under-provisioned-definition)
  say: one resource is too small
ec2-compute-sp-discount-follows-regions
  claim: Compute Savings Plans apply across all Regions, so the discount follows the workload when it moves between Regions or fails over; EC2 Instance Savings Plans are scoped to one Region.
  scope: Savings Plans scope.
  link: [Compute Savings Plans apply across all Regions](../facts/ec2.md#ec2-compute-sp-discount-follows-regions)
  link: [scoped to a specific Region](../facts/ec2.md#ec2-compute-sp-discount-follows-regions)
  say: Compute Savings Plans work in every Region
ec2-concepts-elastic-scale-up-down
  claim: Amazon EC2 provides on-demand, scalable computing capacity: you launch as many or as few virtual servers as you need, add capacity for compute-heavy tasks or traffic spikes, and reduce capacity again when usage decreases.
  scope: Amazon EC2.
  link: [on-demand, scalable computing capacity](../facts/ec2.md#ec2-concepts-elastic-scale-up-down)
  link: [as many or as few virtual servers](../facts/ec2.md#ec2-concepts-elastic-scale-up-down)
  link: [you can reduce capacity (scale down) again](../facts/ec2.md#ec2-concepts-elastic-scale-up-down)
  say: computing capacity on demand | as many servers as you need | and scale down when usage drops
ec2-create-ami-no-reboot-integrity-risk
  claim: If you clear the Reboot instance option when you create an AMI, EC2 does not shut down and reboot the instance, and AWS can't guarantee the file system integrity of the created image.
  scope: creating an AMI from an EBS-backed instance; the Reboot instance option is cleared.
  link: [can't guarantee the file system integrity](../facts/ec2.md#ec2-create-ami-no-reboot-integrity-risk)
  link: [it does not shut down and reboot](../facts/ec2.md#ec2-create-ami-no-reboot-integrity-risk)
  say: the image may not be consistent | the instance keeps running
ec2-create-ami-powers-down-by-default
  claim: When you create an AMI from an instance, EC2 powers down the instance first so that everything is in a consistent state; you can tell EC2 not to power down and reboot if you are confident the instance is consistent.
  scope: EBS-backed AMI creation from an instance; default; adjustable.
  link: [Amazon EC2 powers down the instance before creating the AMI](../facts/ec2.md#ec2-create-ami-powers-down-by-default)
  link: [you can tell Amazon EC2 not to power down and reboot the instance](../facts/ec2.md#ec2-create-ami-powers-down-by-default)
  say: by default EC2 powers the instance down before taking the image
ec2-create-ami-snapshots-all-ebs-volumes
  claim: Creating an EBS-backed AMI snapshots the root volume and every other attached EBS volume, and you are charged for those snapshots until you deregister the AMI and delete them; instance store data is not kept in the AMI.
  scope: EBS-backed AMI creation.
  link: [creates snapshots of your instance's root volume](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
  link: [You're charged for the snapshots](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
  link: [don't contain any data from the instance store](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
ec2-cyclical-layered-approach
  claim: Workloads with predictable but variable patterns benefit from a layered approach: Savings Plans for the baseline and On-Demand Capacity Reservations or Capacity Blocks for the predictable peaks.
  scope: cyclical EC2 workloads.
  link: [Savings Plans for the baseline](../facts/ec2.md#ec2-cyclical-layered-approach)
  say: Savings Plans for the baseline, reservations for the peaks
ec2-data-transfer-cross-region-charged
  claim: Accessing services in a different Region is charged for data transfer across Regions, and the charge depends on the source and destination Region.
  scope: per source and destination Region pair.
  link: [a charge for data transfer across Regions](../facts/ec2.md#ec2-data-transfer-cross-region-charged)
  say: cross-Region traffic is charged
ec2-data-transfer-inbound-free
  claim: There is no charge for inbound data transfer across all services in all Regions; data transfer from AWS to the internet is charged per service at rates of the originating Region.
  scope: per Region, per service.
  link: [no charge for inbound data transfer](../facts/ec2.md#ec2-data-transfer-inbound-free)
  link: [charged per service](../facts/ec2.md#ec2-data-transfer-inbound-free)
  say: data in is free | data out to the internet is charged
ec2-data-transfer-same-az-free-cross-az-charged
  claim: Data transfer within the same Availability Zone is free, while cross-Availability Zone communication between EC2 instances incurs data transfer charges.
  scope: between EC2 instances in one Region; workload components in the same Region.
  link: [within the same Availability Zone is free](../facts/ec2.md#ec2-data-transfer-same-az-free-cross-az-charged)
  link: [charges apply for cross-Availability Zone communication](../facts/ec2.md#ec2-data-transfer-same-az-free-cross-az-charged)
  say: same Availability Zone is free | cross-Availability Zone traffic is charged
ec2-dedicated-host-affinity-same-host-restart
  claim: Host affinity is set at the instance level; with affinity set to Host, an instance launched onto a specific host always restarts on the same host if stopped, and with Default it can restart on any available host while trying the last host on a best-effort basis.
  scope: Dedicated Host affinity.
  link: [always restarts on the same host if stopped](../facts/ec2.md#ec2-dedicated-host-affinity-same-host-restart)
  link: [it can be restarted on any available host](../facts/ec2.md#ec2-dedicated-host-affinity-same-host-restart)
  say: with Host affinity the instance comes back to the same host | with Default affinity it can move
ec2-dedicated-host-auto-placement-default-off
  claim: Auto-placement is set at the host level; when it is disabled (the default for new Dedicated Hosts) the host accepts only host-tenancy launches that name its host ID, and when it is enabled the host accepts any untargeted host-tenancy launch that matches its instance type configuration.
  scope: Dedicated Host auto-placement; default; adjustable.
  link: [the default setting for new Dedicated Hosts](../facts/ec2.md#ec2-dedicated-host-auto-placement-default-off)
  link: [that specify its unique host ID](../facts/ec2.md#ec2-dedicated-host-auto-placement-default-off)
  link: [accepts any untargeted, host tenancy instance launches](../facts/ec2.md#ec2-dedicated-host-auto-placement-default-off)
  say: auto-placement is off by default | when off, only launches that name the host ID land there
ec2-dedicated-host-billed-per-host-per-second
  claim: An On-Demand Dedicated Host is billed per second with a 60-second minimum for the whole host, regardless of how many instances or which sizes run on it; the price varies by instance family and Region.
  scope: per Dedicated Host; minimum; On-Demand Dedicated Hosts.
  link: [per second (with a minimum of 60 seconds) for active Dedicated Host](../facts/ec2.md#ec2-dedicated-host-billed-per-host-per-second)
  link: [regardless of the quantity or the size](../facts/ec2.md#ec2-dedicated-host-billed-per-host-per-second)
  say: per second per host, sixty-second minimum | no matter how many instances run on it
ec2-dedicated-host-byol-no-software-charge
  claim: You can bring existing Windows Server and SQL Server licenses to Dedicated Hosts, subject to Microsoft licensing terms, with no additional charge for software usage.
  scope: per Dedicated Host; subject to Microsoft licensing terms.
  link: [no additional charge for software usage](../facts/ec2.md#ec2-dedicated-host-byol-no-software-charge)
  say: no software charge with your own licenses
ec2-dedicated-host-byol-per-socket-core
  claim: Dedicated Hosts give comprehensive BYOL support: you can use existing per-socket, per-core or per-VM software licenses, such as Windows Server, SQL Server, SUSE Linux Enterprise Server and Red Hat Enterprise Linux, subject to your license terms.
  scope: Dedicated Hosts; subject to your license terms.
  link: [comprehensive Bring Your Own License (BYOL) support](../facts/ec2.md#ec2-dedicated-host-byol-per-socket-core)
  link: [per-socket, per-core, or per-VM software licenses](../facts/ec2.md#ec2-dedicated-host-byol-per-socket-core)
  say: Dedicated Hosts give full bring-your-own-license support | for per-socket and per-core licenses
ec2-dedicated-host-discount-options
  claim: Dedicated Hosts can be paid On-Demand, with Dedicated Host Reservations (No Upfront, Partial Upfront or All Upfront, each available in one-year and three-year terms, though only some instance families support the three-year term for No Upfront; All Upfront gives the lowest effective price), or covered by Savings Plans, which are not supported with the u-6tb1.metal to u-24tb1.metal Dedicated Hosts.
  scope: per Dedicated Host; only some instance families support the three-year No Upfront term; Savings Plans are not supported for the u-6tb1.metal to u-24tb1.metal hosts.
  link: [Dedicated Host Reservations provide a billing discount](../facts/ec2.md#ec2-dedicated-host-discount-options)
  link: [Provides the lowest effective price](../facts/ec2.md#ec2-dedicated-host-discount-options)
  link: [offers significant savings over On-Demand Instances](../facts/ec2.md#ec2-dedicated-host-discount-options)
  say: Dedicated Host Reservations or Savings Plans | All Upfront is the lowest price
ec2-dedicated-host-physical-server
  claim: An Amazon EC2 Dedicated Host is a physical server fully dedicated for your use; it gives visibility and control over instance placement and supports host affinity, and you can optionally share its instance capacity with other AWS accounts.
  scope: Dedicated Hosts.
  link: [a physical server that is fully dedicated](../facts/ec2.md#ec2-dedicated-host-physical-server)
  link: [visibility and control over instance placement](../facts/ec2.md#ec2-dedicated-host-physical-server)
  link: [optionally choose to share the instance capacity](../facts/ec2.md#ec2-dedicated-host-physical-server)
  say: a Dedicated Host is a whole physical server for you | you control where instances are placed
ec2-dedicated-host-priced-per-host-utilization
  claim: Dedicated Hosts are priced per physical host, not per instance, so their cost efficiency depends on how fully you use the instance capacity of each host.
  scope: Dedicated Hosts.
  link: [priced per physical host rather than per instance](../facts/ec2.md#ec2-dedicated-host-priced-per-host-utilization)
  say: you pay per physical host, not per instance
ec2-dedicated-host-reservation-family-and-az
  claim: A Dedicated Host Reservation applies to the instance family on the host, not the instance size, and covers one or more hosts of that family in a single Availability Zone; a host with a reservation cannot be released until the term ends.
  scope: per Dedicated Host Reservation.
  link: [applied to the instance family on the host](../facts/ec2.md#ec2-dedicated-host-reservation-family-and-az)
  link: [can't be released until the reservation's term](../facts/ec2.md#ec2-dedicated-host-reservation-family-and-az)
  say: the family, not the size
ec2-dedicated-host-socket-core-visibility
  claim: Dedicated Hosts provide visibility of the number of sockets and physical cores, while Dedicated Instances provide no such visibility.
  scope: per Dedicated Host or per Dedicated Instance.
  link: [the number of sockets and physical cores](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility)
  link: [No visibility](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility)
  say: Dedicated Hosts show sockets and cores | Dedicated Instances show no sockets or cores
ec2-dedicated-host-vs-instance-billing
  claim: Dedicated Hosts use per-host billing, while Dedicated Instances use per-instance billing.
  scope: per Dedicated Host or per Dedicated Instance.
  link: [Per-host billing](../facts/ec2.md#ec2-dedicated-host-vs-instance-billing)
  link: [Per-instance billing](../facts/ec2.md#ec2-dedicated-host-vs-instance-billing)
  say: Dedicated Hosts are billed per host | Dedicated Instances are billed per instance
ec2-dedicated-host-vs-instance-same-performance
  claim: Dedicated Instances and Dedicated Hosts both launch instances onto dedicated physical servers, and there are no performance, security or physical differences between Dedicated Instances and instances on Dedicated Hosts.
  scope: Dedicated Instances and Dedicated Hosts.
  link: [no performance, security, or physical differences](../facts/ec2.md#ec2-dedicated-host-vs-instance-same-performance)
  link: [onto dedicated physical servers](../facts/ec2.md#ec2-dedicated-host-vs-instance-same-performance)
  say: there is no performance or security difference | both put instances on dedicated servers
ec2-dedicated-instance-ebs-not-single-tenant
  claim: When you launch a Dedicated Instance backed by Amazon EBS, the EBS volume does not run on single-tenant hardware.
  scope: per Dedicated Instance.
  link: [the EBS volume doesn't run on single-tenant hardware](../facts/ec2.md#ec2-dedicated-instance-ebs-not-single-tenant)
  say: the EBS volume is not single-tenant
ec2-dedicated-instance-isolated-from-other-accounts
  claim: Dedicated Instances run on hardware dedicated to a single AWS account and are physically isolated at the host hardware level from instances of other AWS accounts, even accounts linked to one payer account; they might share hardware with non-dedicated instances from the same account.
  scope: Dedicated Instances.
  link: [hardware that's dedicated to a single AWS account](../facts/ec2.md#ec2-dedicated-instance-isolated-from-other-accounts)
  link: [might share hardware with other instances](../facts/ec2.md#ec2-dedicated-instance-isolated-from-other-accounts)
  link: [linked to a single payer account](../facts/ec2.md#ec2-dedicated-instance-isolated-from-other-accounts)
  say: Dedicated Instances run on hardware for one account | they can share hardware with your own other instances
ec2-dedicated-instance-no-placement-control
  claim: Dedicated Instances give no visibility or control over instance placement and do not support host affinity; after a stop and start a Dedicated Instance might not run on the same host, and they have limited BYOL support.
  scope: Dedicated Instances.
  link: [provide no visibility or control over instance placement](../facts/ec2.md#ec2-dedicated-instance-no-placement-control)
  link: [they do not support host affinity](../facts/ec2.md#ec2-dedicated-instance-no-placement-control)
  link: [limited support for Bring Your Own License](../facts/ec2.md#ec2-dedicated-instance-no-placement-control)
  say: no control over placement | and no host affinity
ec2-dedicated-ri-tenancy-must-match
  claim: A Reserved Instance with default tenancy applies only to running instances with default tenancy, not to instances with dedicated tenancy, and the tenancy of a Reserved Instance cannot be changed through modification.
  scope: per Reserved Instance; a Convertible Reserved Instance can be exchanged for one with a different tenancy.
  link: [only to a running instance with default tenancy](../facts/ec2.md#ec2-dedicated-ri-tenancy-must-match)
  link: [can't use the modification process](../facts/ec2.md#ec2-dedicated-ri-tenancy-must-match)
  say: default-tenancy Reserved Instances do not cover dedicated instances | you cannot modify the tenancy of a Reserved Instance
ec2-dedicated-spot-not-t-largest-size
  claim: All instance families support Dedicated Spot Instances except T instances, and for each supported family only the largest instance size or metal size supports them.
  scope: Dedicated Spot Instances.
  link: [except T instances](../facts/ec2.md#ec2-dedicated-spot-not-t-largest-size)
  link: [only the largest instance size or metal size](../facts/ec2.md#ec2-dedicated-spot-not-t-largest-size)
  say: every family except T can run Dedicated Spot Instances | and only the largest or metal size
ec2-default-tenancy-shared-hardware
  claim: By default, EC2 instances run on shared tenancy hardware, which means multiple AWS accounts might share the same physical hardware.
  scope: EC2 instance tenancy; default; adjustable.
  link: [run on shared tenancy hardware](../facts/ec2.md#ec2-default-tenancy-shared-hardware)
  link: [accounts might share the same physical hardware](../facts/ec2.md#ec2-default-tenancy-shared-hardware)
  say: by default instances run on shared hardware
ec2-delete-on-termination-defaults
  claim: Each EBS volume has a DeleteOnTermination attribute; by default the root volume is deleted when the instance terminates and any other EBS volume is preserved.
  scope: per EBS volume attached to an instance; default; adjustable.
  link: [The default is to delete the root volume](../facts/ec2.md#ec2-delete-on-termination-defaults)
  link: [DeleteOnTermination](../facts/ec2.md#ec2-delete-on-termination-defaults)
  link: [preserve any other EBS volumes](../facts/ec2.md#ec2-delete-on-termination-defaults)
  say: by default the root volume is deleted and other EBS volumes are kept | other EBS volumes are kept
ec2-ebs-backed-ami-recommended
  claim: AWS recommends AMIs backed by EBS because those instances launch faster and use persistent storage; the AMI you launch from determines the type of root volume.
  scope: root volume type.
  link: [these instances launch faster and use persistent storage](../facts/ec2.md#ec2-ebs-backed-ami-recommended)
  link: [determines the type of root volume](../facts/ec2.md#ec2-ebs-backed-ami-recommended)
  say: EBS backed instances launch faster and keep their storage
ec2-ebs-optimized-default-current-generation
  claim: For current generation instance types, EBS optimization is enabled by default at no additional cost.
  scope: per instance; default; not adjustable; current generation instance types; previous generation types have their own prices.
  link: [enabled by default at no additional cost](../facts/ec2.md#ec2-ebs-optimized-default-current-generation)
  say: on by default, no extra cost
ec2-ebs-root-can-stop-and-restart
  claim: An instance with an EBS root volume can be stopped and later restarted without affecting the data in its attached volumes; while stopped you can change its size or attach its root volume to another running instance for debugging.
  scope: instances with an EBS root volume.
  link: [can be stopped and later restarted](../facts/ec2.md#ec2-ebs-root-can-stop-and-restart)
  link: [to a different running instance for debugging](../facts/ec2.md#ec2-ebs-root-can-stop-and-restart)
  say: an EBS backed instance can be stopped and restarted without losing its volume data
ec2-efa-accelerates-ai-ml-hpc
  claim: An Elastic Fabric Adapter (EFA) is a network device that you attach to an EC2 instance to accelerate AI, ML and HPC applications.
  scope: Elastic Fabric Adapter.
  link: [a network device that you can attach](../facts/ec2.md#ec2-efa-accelerates-ai-ml-hpc)
  say: a network device for AI, ML and HPC
ec2-efa-lower-latency-than-tcp
  claim: EFA provides lower and more consistent latency and higher throughput than the TCP transport traditionally used in cloud-based HPC systems.
  scope: Elastic Fabric Adapter.
  link: [lower and more consistent latency and higher throughput](../facts/ec2.md#ec2-efa-lower-latency-than-tcp)
  say: lower, steadier latency and more throughput than TCP
ec2-efa-no-additional-cost
  claim: EFA is an optional EC2 networking feature that you can enable on any supported instance at no additional cost.
  scope: Elastic Fabric Adapter on supported instance types; supported instance types.
  link: [at no additional cost](../facts/ec2.md#ec2-efa-no-additional-cost)
  say: no extra cost
ec2-efa-os-bypass
  claim: With EFA, the Libfabric API bypasses the operating system kernel and communicates directly with the EFA device to put packets on the network, which reduces overhead.
  scope: Elastic Fabric Adapter; applications that use Libfabric, for example through MPI or NCCL.
  link: [bypasses the operating system kernel](../facts/ec2.md#ec2-efa-os-bypass)
  say: it skips the operating system kernel
ec2-efa-traffic-not-routable-across-az
  claim: EFA traffic cannot cross Availability Zones or VPCs; this does not apply to normal IP traffic from the ENA device of an EFA interface.
  scope: traffic through the EFA device; not normal IP traffic from the ENA device.
  link: [can't cross Availability Zones or VPCs](../facts/ec2.md#ec2-efa-traffic-not-routable-across-az)
  say: no, EFA traffic stays in one Availability Zone and VPC
ec2-efa-vs-ena-ip-networking
  claim: The EFA device provides OS-bypass and congestion control through the Scalable Reliable Datagram (SRD) protocol, while the ENA device offers traditional IP networking.
  scope: EFA and ENA network interfaces.
  link: [built-in OS-bypass and congestion control](../facts/ec2.md#ec2-efa-vs-ena-ip-networking)
  link: [the ENA device offers traditional IP networking](../facts/ec2.md#ec2-efa-vs-ena-ip-networking)
  say: EFA adds OS-bypass | ENA is normal IP networking
ec2-eice-no-additional-cost-cross-az-transfer
  claim: There is no additional cost for using EC2 Instance Connect Endpoints.
  scope: EC2 Instance Connect Endpoint.
  link: [There is no additional cost](../facts/ec2.md#ec2-eice-no-additional-cost-cross-az-transfer)
  link: [for using EC2 Instance Connect Endpoints](../facts/ec2.md#ec2-eice-no-additional-cost-cross-az-transfer)
  say: the endpoint itself is free | for Instance Connect Endpoints
ec2-eice-no-public-ip-no-igw-no-bastion
  claim: EC2 Instance Connect Endpoint lets you connect securely to an instance from the internet without a bastion host, without a public IPv4 or IPv6 address on the instance, and without direct internet connectivity (an internet gateway) for the VPC.
  scope: EC2 Instance Connect Endpoint.
  link: [without using a bastion host](../facts/ec2.md#ec2-eice-no-public-ip-no-igw-no-bastion)
  link: [to have a public IPv4 or IPv6 address](../facts/ec2.md#ec2-eice-no-public-ip-no-igw-no-bastion)
  link: [has direct internet connectivity](../facts/ec2.md#ec2-eice-no-public-ip-no-igw-no-bastion)
  say: no bastion host | no public IP on the instance | no internet gateway needed
ec2-eice-quota-1-per-vpc
  claim: A VPC can have at most 1 EC2 Instance Connect Endpoint, and this quota is not adjustable.
  scope: per VPC; maximum; not adjustable.
  link: [1 EC2 Instance Connect Endpoint](../facts/ec2.md#ec2-eice-quota-1-per-vpc)
  say: one endpoint per VPC
ec2-eice-quota-20-concurrent-connections
  claim: An EC2 Instance Connect Endpoint supports at most 20 concurrent connections, and this quota is not adjustable.
  scope: per EC2 Instance Connect Endpoint; maximum; not adjustable.
  link: [20 concurrent connections](../facts/ec2.md#ec2-eice-quota-20-concurrent-connections)
  say: twenty concurrent connections per endpoint
ec2-eice-quota-5-per-account-region
  claim: An AWS account can have at most 5 EC2 Instance Connect Endpoints per Region by default, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [5 EC2 Instance Connect Endpoints per Region](../facts/ec2.md#ec2-eice-quota-5-per-account-region)
  say: five endpoints per account per Region
ec2-eip-charged-in-use-and-idle
  claim: All Elastic IP addresses are charged, whether in use or idle, and AWS charges for all public IPv4 addresses, including those on running instances.
  scope: per Elastic IP address.
  link: [a charge for all Elastic IP addresses](../facts/ec2.md#ec2-eip-charged-in-use-and-idle)
  link: [AWS charges for all public IPv4 addresses](../facts/ec2.md#ec2-eip-charged-in-use-and-idle)
  say: every Elastic IP is charged, used or idle
ec2-eip-disassociated-stays-allocated
  claim: You can disassociate an Elastic IP address from a resource and associate it with a different resource; a disassociated Elastic IP address stays allocated to your account until you explicitly release it.
  scope: Elastic IP addresses.
  link: [associate it with a different resource](../facts/ec2.md#ec2-eip-disassociated-stays-allocated)
  link: [remains allocated to your account](../facts/ec2.md#ec2-eip-disassociated-stays-allocated)
  link: [until you explicitly release it](../facts/ec2.md#ec2-eip-disassociated-stays-allocated)
  say: you can move it to another resource | it stays in your account | until you release it
ec2-eip-mask-instance-failure-remap
  claim: An Elastic IP address is a static IPv4 address; by rapidly remapping it to another instance in your account, you can mask the failure of an instance or software.
  scope: Elastic IP addresses; the replacement instance is in the same account and Region.
  link: [a static IPv4 address](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  link: [rapidly remapping the address to another instance](../facts/ec2.md#ec2-eip-mask-instance-failure-remap)
  say: a static public IPv4 address | move the address to a healthy instance
ec2-eip-quota-5-per-region
  claim: The default quota is 5 Elastic IP addresses per Region, and the quota is adjustable.
  scope: per account, per Region; default; adjustable.
  link: [5 Elastic IP addresses per Region](../facts/ec2.md#ec2-eip-quota-5-per-region)
  say: five Elastic IP addresses per Region
ec2-eip-region-bound-ipv4-only
  claim: An Elastic IP address is static, is for use in one Region only and cannot be moved to another Region, and Elastic IP addresses are not supported for IPv6.
  scope: per Elastic IP address.
  link: [cannot be moved to a different Region](../facts/ec2.md#ec2-eip-region-bound-ipv4-only)
  link: [We do not support Elastic IP addresses for IPv6](../facts/ec2.md#ec2-eip-region-bound-ipv4-only)
  say: cannot move between Regions | no Elastic IPs for IPv6
ec2-enhanced-networking-benefits-no-charge
  claim: Enhanced networking gives higher bandwidth, higher packet per second (PPS) performance and consistently lower latency between instances, at no additional charge.
  scope: enhanced networking on supported instance types; supported instance types.
  link: [higher bandwidth, higher packet per second (PPS) performance](../facts/ec2.md#ec2-enhanced-networking-benefits-no-charge)
  link: [consistently lower latency between instances](../facts/ec2.md#ec2-enhanced-networking-benefits-no-charge)
  link: [no additional charge for using enhanced networking](../facts/ec2.md#ec2-enhanced-networking-benefits-no-charge)
  say: more bandwidth and more packets per second | and lower latency | it costs nothing extra
ec2-eni-attributes-follow-same-az
  claim: You attach a network interface to instances in the same Availability Zone; its attributes follow it when you detach it and reattach it to another instance, and network traffic is redirected to the new instance.
  scope: elastic network interfaces.
  link: [in the same Availability Zone](../facts/ec2.md#ec2-eni-attributes-follow-same-az)
  link: [The attributes of a network interface follow it](../facts/ec2.md#ec2-eni-attributes-follow-same-az)
  link: [network traffic is redirected](../facts/ec2.md#ec2-eni-attributes-follow-same-az)
  say: only within the same zone | its settings move with it | traffic goes to the new instance
ec2-eni-cross-vpc-same-az-same-account
  claim: An instance in one VPC can have a secondary network interface from a different VPC if the interface is in the same Availability Zone as the instance; multi-homed instances across VPCs in different AWS accounts are not possible.
  scope: secondary network interfaces; VPCs in the same account.
  link: [in the same Availability Zone as the instance](../facts/ec2.md#ec2-eni-cross-vpc-same-az-same-account)
  link: [across VPCs in different AWS accounts](../facts/ec2.md#ec2-eni-cross-vpc-same-az-same-account)
  say: yes, if the interface is in the same zone | but not across accounts
ec2-eni-hot-standby-failover
  claim: For a low-budget high-availability design, you attach the network interface of a failed instance to a hot standby instance; because the interface keeps its private IP addresses, Elastic IP addresses and MAC address, traffic flows to the standby as soon as it is attached, with no route table or DNS changes.
  scope: secondary or primary network interfaces moved between instances; the standby is in the same Availability Zone.
  link: [maintains its private IP addresses, Elastic IP addresses](../facts/ec2.md#ec2-eni-hot-standby-failover)
  link: [hot standby instance](../facts/ec2.md#ec2-eni-hot-standby-failover)
  link: [no changes to the route table](../facts/ec2.md#ec2-eni-hot-standby-failover)
  say: the interface keeps its IPs and MAC address | move it to a hot standby | no route or DNS changes needed
ec2-eni-primary-cannot-detach
  claim: Each instance has a default network interface, the primary network interface, which you can't detach from the instance.
  scope: the primary network interface of an instance.
  link: [You can't detach a primary network interface](../facts/ec2.md#ec2-eni-primary-cannot-detach)
  link: [Each instance has a default network interface](../facts/ec2.md#ec2-eni-primary-cannot-detach)
  say: the primary interface cannot be detached | every instance has one by default
ec2-family-accelerated-computing
  claim: Accelerated computing instances use hardware accelerators, or co-processors, to perform functions such as floating point calculations, graphics processing or data pattern matching more efficiently than software running on CPUs.
  scope: accelerated computing instance family.
  link: [hardware accelerators, or co-processors](../facts/ec2.md#ec2-family-accelerated-computing)
  link: [floating point number calculations, graphics processing](../facts/ec2.md#ec2-family-accelerated-computing)
  say: hardware accelerators like GPUs | for math and graphics work
ec2-family-compute-optimized
  claim: Compute optimized instances are designed for compute intensive applications that benefit from high performance processors, such as batch processing, media transcoding, high performance web servers, HPC, scientific modeling, dedicated gaming servers, ad server engines and machine learning inference.
  scope: compute optimized instance family.
  link: [compute intensive applications](../facts/ec2.md#ec2-family-compute-optimized)
  link: [benefit from high performance processors](../facts/ec2.md#ec2-family-compute-optimized)
  link: [batch processing workloads, media transcoding](../facts/ec2.md#ec2-family-compute-optimized)
  say: CPU-heavy applications | that need fast processors | for example batch jobs and media transcoding
ec2-family-general-purpose
  claim: General purpose instances provide a balance of compute, memory and networking resources and are ideal for applications that use these resources in equal proportions, such as web servers and code repositories.
  scope: general purpose instance family.
  link: [a balance of compute, memory, and networking resources](../facts/ec2.md#ec2-family-general-purpose)
  link: [such as web servers and code repositories](../facts/ec2.md#ec2-family-general-purpose)
  say: a balance of CPU, memory and network | for example web servers
ec2-family-memory-optimized
  claim: Memory optimized instances are designed to deliver fast performance for workloads that process large data sets in memory.
  scope: memory optimized instance family.
  link: [deliver fast performance](../facts/ec2.md#ec2-family-memory-optimized)
  link: [process large data sets in memory](../facts/ec2.md#ec2-family-memory-optimized)
  say: fast performance | for large data sets held in memory
ec2-family-storage-optimized
  claim: Storage optimized instances are designed for workloads that need high, sequential read and write access to very large data sets on local storage, and they deliver tens of thousands of low-latency random I/O operations per second (IOPS).
  scope: storage optimized instance family.
  link: [high, sequential read and write access](../facts/ec2.md#ec2-family-storage-optimized)
  link: [very large data sets on local storage](../facts/ec2.md#ec2-family-storage-optimized)
  link: [low-latency, random I/O operations per second (IOPS)](../facts/ec2.md#ec2-family-storage-optimized)
  say: heavy sequential reads and writes | on large local storage | many fast random I O operations
ec2-faq-az-isolation
  claim: Each Availability Zone runs on its own physically distinct, independent infrastructure; common failure points such as generators and cooling are not shared, and rare disasters such as fires or floods would affect only a single zone.
  scope: Availability Zones in a Region.
  link: [physically distinct, independent infrastructure](../facts/ec2.md#ec2-faq-az-isolation)
  link: [not shared across Availability Zones](../facts/ec2.md#ec2-faq-az-isolation)
  link: [would only affect a single Availability Zone](../facts/ec2.md#ec2-faq-az-isolation)
  say: separate physical infrastructure | no shared generators or cooling | a disaster hits one zone
ec2-faq-bare-metal-for-hardware-virtualization
  claim: AWS recommends evaluating bare metal instances for workloads that require access to hardware virtualization extensions and are performance sensitive or have strict latency requirements.
  scope: bare metal instance choice.
  link: [require access to hardware virtualization extensions](../facts/ec2.md#ec2-faq-bare-metal-for-hardware-virtualization)
  link: [evaluate Bare Metal instances](../facts/ec2.md#ec2-faq-bare-metal-for-hardware-virtualization)
  say: need hardware virtualization extensions | consider bare metal
ec2-faq-bill-shows-decimal-hours
  claim: EC2 charges are calculated per second, but the monthly bill shows cumulative usage per instance in decimal hours; 1 hour 10 minutes 4 seconds shows as 1.1677.
  scope: the monthly EC2 bill.
  link: [in decimal hours](../facts/ec2.md#ec2-faq-bill-shows-decimal-hours)
  link: [1.1677](../facts/ec2.md#ec2-faq-bill-shows-decimal-hours)
  say: the bill shows decimal hours | one point one six seven seven hours
ec2-faq-billing-running-state
  claim: Instance usage is billed for any time the instance is in the running state; to stop instance usage charges, stop or terminate the instance.
  scope: per instance.
  link: [in a "running" state](../facts/ec2.md#ec2-faq-billing-running-state)
  link: [Billing starts when an instance transitions into](../facts/ec2.md#ec2-faq-billing-running-state)
  say: billed while running | billing starts on the move to running
ec2-faq-burstable-sustained-high-cpu-use-m-or-c
  claim: If a workload consistently needs CPU usage much higher than the baseline, AWS suggests dedicated CPU instances such as M or C instead of burstable instances.
  scope: burstable performance instances versus fixed-performance instances.
  link: [consistently require CPU usage much higher](../facts/ec2.md#ec2-faq-burstable-sustained-high-cpu-use-m-or-c)
  link: [consider dedicated CPU instances](../facts/ec2.md#ec2-faq-burstable-sustained-high-cpu-use-m-or-c)
  say: steady high CPU | choose M or C
ec2-faq-buy-regional-ri-for-flexibility
  claim: If no capacity reservation is needed, buy a regional RI, which gives AZ and instance size flexibility.
  scope: Reserved Instance scope choice.
  link: [you should buy a regional RI](../facts/ec2.md#ec2-faq-buy-regional-ri-for-flexibility)
  link: [AZ and instance size flexibility](../facts/ec2.md#ec2-faq-buy-regional-ri-for-flexibility)
  say: no capacity needed: regional | AZ and size flexibility
ec2-faq-buy-zonal-ri-for-capacity
  claim: To use the capacity reservation of a Reserved Instance, buy the RI in a specific Availability Zone.
  scope: Reserved Instance scope choice.
  link: [buy an RI in a specific AZ](../facts/ec2.md#ec2-faq-buy-zonal-ri-for-capacity)
  say: need capacity: zonal
ec2-faq-capacity-blocks-eight-weeks-ahead
  claim: A Capacity Block can be purchased as far out as eight weeks into the future, or for now when capacity is available.
  scope: EC2 Capacity Blocks for ML, purchase lead time; maximum; not adjustable.
  link: [eight weeks into the future](../facts/ec2.md#ec2-faq-capacity-blocks-eight-weeks-ahead)
  say: up to eight weeks ahead
ec2-faq-capacity-blocks-in-ultraclusters
  claim: EC2 Capacity Blocks give access to high-performing GPU instances for ML and are delivered in EC2 UltraClusters for low network latency and high throughput.
  scope: EC2 Capacity Blocks for ML.
  link: [ensure capacity availability for GPU instances](../facts/ec2.md#ec2-faq-capacity-blocks-in-ultraclusters)
  link: [delivered in EC2 UltraClusters](../facts/ec2.md#ec2-faq-capacity-blocks-in-ultraclusters)
  say: assured GPU capacity | delivered in UltraClusters
ec2-faq-capacity-blocks-no-modify-or-cancel
  claim: A Capacity Block cannot be modified or canceled once it is reserved.
  scope: EC2 Capacity Blocks for ML.
  link: [cannot be modified or canceled](../facts/ec2.md#ec2-faq-capacity-blocks-no-modify-or-cancel)
  say: no changes and no cancel after you reserve it
ec2-faq-capacity-blocks-terminate-30-minutes-before-end
  claim: Around 30 minutes before a Capacity Block expires, AWS begins terminating any running instances in it.
  scope: instances running in an EC2 Capacity Block.
  link: [Around 30 minutes before](../facts/ec2.md#ec2-faq-capacity-blocks-terminate-30-minutes-before-end)
  say: about thirty minutes before the end
ec2-faq-capacity-blocks-vs-capacity-reservations
  claim: Capacity Blocks give scheduled, future-dated GPU capacity for ML workloads, while On-Demand Capacity Reservations give immediate, flexible capacity assurance for any workload with no advance scheduling or fixed end date.
  scope: Capacity Blocks for ML and On-Demand Capacity Reservations.
  link: [scheduled, future-dated GPU capacity specifically for ML workloads](../facts/ec2.md#ec2-faq-capacity-blocks-vs-capacity-reservations)
  link: [flexible, immediate capacity assurance for any workload](../facts/ec2.md#ec2-faq-capacity-blocks-vs-capacity-reservations)
  say: Capacity Blocks: GPU capacity for ML on future dates | Capacity Reservations: capacity now, any workload
ec2-faq-capacity-reservation-count-from-on-demand-limit
  claim: The number of instances that can be reserved with Capacity Reservations is based on the account's On-Demand instance limit, minus the instances already running.
  scope: Capacity Reservations per account per Region; maximum; adjustable.
  link: [based on your account's On-Demand instance limit](../facts/ec2.md#ec2-faq-capacity-reservation-count-from-on-demand-limit)
  link: [minus the number of instances](../facts/ec2.md#ec2-faq-capacity-reservation-count-from-on-demand-limit)
  say: set by the On-Demand limit | minus what already runs
ec2-faq-capacity-reservation-end-running-unaffected
  claim: An active Capacity Reservation can be ended (after any commitment period of a future-dated one) by canceling it or setting an end time; running instances are unaffected by changes, deletion or expiry of the reservation.
  scope: an active On-Demand Capacity Reservation.
  link: [Running instances are unaffected](../facts/ec2.md#ec2-faq-capacity-reservation-end-running-unaffected)
  say: running instances keep running
ec2-faq-capacity-reservation-modify-after-start
  claim: After a Capacity Reservation starts, its number of instances, match criteria and end date can be modified.
  scope: an active On-Demand Capacity Reservation.
  link: [modify the number of instances](../facts/ec2.md#ec2-faq-capacity-reservation-modify-after-start)
  link: [the match criteria, and the end date](../facts/ec2.md#ec2-faq-capacity-reservation-modify-after-start)
  say: count, match criteria and end date | match criteria and end date
ec2-faq-capacity-reservation-share-via-ram
  claim: Active Capacity Reservations can be shared with other AWS accounts or within an AWS Organization through AWS Resource Access Manager (AWS RAM).
  scope: active On-Demand Capacity Reservations.
  link: [through AWS Resource Access Manager (AWS RAM)](../facts/ec2.md#ec2-faq-capacity-reservation-share-via-ram)
  say: share with AWS RAM
ec2-faq-capacity-reservation-strict-requirements
  claim: Capacity Reservations are meant for strict capacity requirements of current or future business-critical workloads that need long or short-term capacity assurance.
  scope: On-Demand Capacity Reservations.
  link: [strict capacity requirements](../facts/ec2.md#ec2-faq-capacity-reservation-strict-requirements)
  link: [business-critical workloads](../facts/ec2.md#ec2-faq-capacity-reservation-strict-requirements)
  say: strict capacity needs | business-critical workloads
ec2-faq-capacity-reservation-tied-to-az-type-os-tenancy
  claim: A Capacity Reservation is tied to a specific Availability Zone, instance type, platform (OS) and tenancy; with Open match criteria it automatically covers matching running or newly launched instances while it has excess capacity.
  scope: per On-Demand Capacity Reservation.
  link: [tied to a specific AZ, instance type](../facts/ec2.md#ec2-faq-capacity-reservation-tied-to-az-type-os-tenancy)
  link: [‘Open’ match criteria](../facts/ec2.md#ec2-faq-capacity-reservation-tied-to-az-type-os-tenancy)
  link: [platform (OS) and tenancy](../facts/ec2.md#ec2-faq-capacity-reservation-tied-to-az-type-os-tenancy)
  say: AZ, type, OS and tenancy | Open: matching instances use it automatically | platform and tenancy
ec2-faq-cloudtrail-ec2-api-history
  claim: To get a history of all EC2 API calls on an account, including VPC and EBS calls, turn on AWS CloudTrail.
  scope: EC2 API call history per account.
  link: [you simply turn on CloudTrail](../facts/ec2.md#ec2-faq-cloudtrail-ec2-api-history)
  say: turn on CloudTrail
ec2-faq-cluster-pg-stop-start-stays
  claim: A stopped instance is started again in the cluster placement group it was in; if capacity is not available in that group, the start fails.
  scope: a stopped instance in a cluster placement group.
  link: [started as part of the cluster placement group](../facts/ec2.md#ec2-faq-cluster-pg-stop-start-stays)
  link: [the start will fail](../facts/ec2.md#ec2-faq-cluster-pg-stop-start-stays)
  say: it returns to the same group | no capacity: the start fails
ec2-faq-convertible-ri-change-type
  claim: Convertible RIs allow changing the instance type, operating system, tenancy or payment option during the term.
  scope: Convertible Reserved Instances during the term.
  link: [change the instance type, operating system, tenancy](../facts/ec2.md#ec2-faq-convertible-ri-change-type)
  say: Convertible: change type, OS, tenancy
ec2-faq-convertible-ri-no-exchange-limit
  claim: There are no exchange limits for Convertible RIs.
  scope: Convertible Reserved Instance exchanges; maximum; not adjustable.
  link: [no exchange limits for Convertible RIs](../facts/ec2.md#ec2-faq-convertible-ri-no-exchange-limit)
  say: no limit on exchanges
ec2-faq-convertible-ri-no-fee-true-up
  claim: Exchanging Convertible RIs has no fee, but a one-time true-up charge may apply for the price difference.
  scope: Convertible Reserved Instance exchanges.
  link: [you do not pay a fee](../facts/ec2.md#ec2-faq-convertible-ri-no-fee-true-up)
  link: [a one-time true-up charge](../facts/ec2.md#ec2-faq-convertible-ri-no-fee-true-up)
  say: no exchange fee | maybe a true-up charge
ec2-faq-convertible-ri-when
  claim: A Convertible RI suits customers who can commit for a three-year term for a significant discount but are uncertain about future instance needs or want to benefit from price changes.
  scope: choosing a Convertible Reserved Instance.
  link: [uncertain about their instance needs in the future](../facts/ec2.md#ec2-faq-convertible-ri-when)
  say: unsure about future needs
ec2-faq-cross-az-transfer-charged-both-sides
  claim: When data moves between instances in different Availability Zones, each instance is charged for its data in and data out at the corresponding data transfer rates.
  scope: instances in different Availability Zones.
  link: [charged for its data in and data out](../facts/ec2.md#ec2-faq-cross-az-transfer-charged-both-sides)
  say: each instance pays for its data in and out
ec2-faq-cross-region-transfer-out-and-in
  claim: Data between two instances in different Regions is charged at Inter-Region Data Transfer Out for the sending instance and Inter-Region Data Transfer In for the receiving instance.
  scope: two instances in different Regions.
  link: [at Inter-Region Data Transfer rates](../facts/ec2.md#ec2-faq-cross-region-transfer-out-and-in)
  say: Inter-Region Data Transfer rates apply
ec2-faq-discounted-ri-not-resellable
  claim: RIs bought with an AWS discount (for example an RI volume discount) are not eligible for sale on the EC2 RI Marketplace.
  scope: Reserved Instances bought with an AWS discount.
  link: [not eligible for sale on the EC2 RI Marketplace](../facts/ec2.md#ec2-faq-discounted-ri-not-resellable)
  say: discounted RIs cannot be resold
ec2-faq-eip-not-needed-per-instance
  claim: An Elastic IP address is not needed for every instance.
  scope: Elastic IP addresses.
  link: [You do not need an Elastic IP address](../facts/ec2.md#ec2-faq-eip-not-needed-per-instance)
  say: not every instance needs one
ec2-faq-fleet-no-additional-charge
  claim: EC2 Fleet has no additional charge; you pay only for the resources it launches.
  scope: EC2 Fleet.
  link: [EC2 Fleet comes at no additional charge](../facts/ec2.md#ec2-faq-fleet-no-additional-charge)
  say: no extra charge for EC2 Fleet
ec2-faq-fleet-no-on-demand-failover
  claim: EC2 Fleet does not fail over to On-Demand when Spot capacity is not fully available; it keeps trying to meet the requested Spot capacity.
  scope: EC2 Fleet Spot capacity.
  link: [attempt to meet your desired Spot capacity](../facts/ec2.md#ec2-faq-fleet-no-on-demand-failover)
  say: no, it keeps trying to get Spot
ec2-faq-fleet-on-demand-gets-ri-discount
  claim: An On-Demand Instance launched by EC2 Fleet that matches an existing Reserved Instance receives the Reserved Instance discount.
  scope: On-Demand Instances launched by EC2 Fleet; the instance matches an existing Reserved Instance.
  link: [that instance will receive the RI discount](../facts/ec2.md#ec2-faq-fleet-on-demand-gets-ri-discount)
  say: yes, a matching Fleet instance gets the RI discount
ec2-faq-fleet-single-region
  claim: An EC2 Fleet request cannot span multiple Regions; multi-Region EC2 Fleet requests are not supported.
  scope: EC2 Fleet requests.
  link: [do not support multi-region EC2 Fleet requests](../facts/ec2.md#ec2-faq-fleet-single-region)
  say: an EC2 Fleet is one Region only
ec2-faq-flex-baseline-40-burst-100
  claim: Flex instances provide a baseline CPU performance of 40% and can scale up to 100% CPU for 95% of the time over a 24-hour window.
  scope: Flex instances (for example M7i-flex, C7i-flex); fixed.
  link: [40%](../facts/ec2.md#ec2-faq-flex-baseline-40-burst-100)
  link: [100% CPU for 95% of the time](../facts/ec2.md#ec2-faq-flex-baseline-40-burst-100)
  link: [24-hour window](../facts/ec2.md#ec2-faq-flex-baseline-40-burst-100)
  say: forty percent baseline | full CPU for ninety-five percent of the time | over twenty-four hours
ec2-faq-g-series-vs-p-series
  claim: G-series GPU instances suit graphics, gaming, spatial computing, AI/ML inference and single-node training; P-series instances are optimized for AI inference and training of large foundation models.
  scope: GPU instance families.
  link: [graphics, gaming and spatial computing](../facts/ec2.md#ec2-faq-g-series-vs-p-series)
  link: [training of large foundation models](../facts/ec2.md#ec2-faq-g-series-vs-p-series)
  say: G for graphics and inference | P for large-model training
ec2-faq-hibernate-keeps-private-and-elastic-ip
  claim: When an instance is stopped or hibernated, its private IP address stays the same, as does its Elastic IP address if it has one.
  scope: a stopped or hibernated instance.
  link: [Your private IP address remains the same](../facts/ec2.md#ec2-faq-hibernate-keeps-private-and-elastic-ip)
  link: [as does your elastic IP address](../facts/ec2.md#ec2-faq-hibernate-keeps-private-and-elastic-ip)
  say: private IP stays the same | Elastic IP stays too
ec2-faq-hibernate-ram-always-encrypted
  claim: RAM data is always encrypted when it is moved to the EBS root volume; root volume encryption is enforced at instance launch.
  scope: hibernated instances.
  link: [RAM data is always encrypted](../facts/ec2.md#ec2-faq-hibernate-ram-always-encrypted)
  link: [enforced at instance launch time](../facts/ec2.md#ec2-faq-hibernate-ram-always-encrypted)
  say: RAM data is always encrypted | root encryption is enforced at launch
ec2-faq-hibernate-root-too-small-shuts-down
  claim: If the EBS root volume does not have enough space for the memory contents, hibernation fails and the instance is shut down instead.
  scope: hibernation of an instance.
  link: [hibernation will fail](../facts/ec2.md#ec2-faq-hibernate-root-too-small-shuts-down)
  link: [the instance will get shut down instead](../facts/ec2.md#ec2-faq-hibernate-root-too-small-shuts-down)
  say: hibernation fails | the instance shuts down instead
ec2-faq-hibernate-state-reason
  claim: A hibernated instance shows the state reason Client.UserInitiatedHibernate.
  scope: a hibernated instance.
  link: [‘Client.UserInitiatedHibernate’](../facts/ec2.md#ec2-faq-hibernate-state-reason)
  say: state reason Client dot User Initiated Hibernate
ec2-faq-hibernate-stop-ebs-backed-only
  claim: Stop and hibernate are available only for Amazon EBS-backed instances, and local instance storage is not persisted.
  scope: stop and hibernate actions.
  link: [available for Amazon EBS backed instances only](../facts/ec2.md#ec2-faq-hibernate-stop-ebs-backed-only)
  link: [Local instance storage is not persisted](../facts/ec2.md#ec2-faq-hibernate-stop-ebs-backed-only)
  say: only EBS-backed instances | instance store data is lost
ec2-faq-hibernate-trigger-stopinstances
  claim: Hibernation must be enabled at launch; it is then triggered with the StopInstances API and its Hibernate parameter.
  scope: hibernation of an instance.
  link: [StopInstances API with an additional ‘Hibernate’ parameter](../facts/ec2.md#ec2-faq-hibernate-trigger-stopinstances)
  say: StopInstances with Hibernate
ec2-faq-hibernate-use-case-prewarm
  claim: Hibernation suits applications that take a long time to bootstrap: pre-warmed instances can be resumed to reduce the time to return to service, because hibernation retains memory state across stop and start.
  scope: hibernation use cases.
  link: [take a long time to bootstrap](../facts/ec2.md#ec2-faq-hibernate-use-case-prewarm)
  link: [Hibernation retains memory state across Stop/Start cycles](../facts/ec2.md#ec2-faq-hibernate-use-case-prewarm)
  say: for slow-to-start applications | memory survives stop and start
ec2-faq-hibernate-vs-stop-ram
  claim: Hibernate persists the RAM data; stop shuts the instance down and clears RAM. In both cases data on the EBS root volume and attached EBS data volumes persists.
  scope: hibernate compared with stop.
  link: [the RAM data persisted](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  link: [RAM is cleared](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  say: hibernate keeps RAM | stop clears RAM
ec2-faq-hibernated-state-is-stopped
  claim: A hibernated instance is in the Stopped state.
  scope: a hibernated instance.
  link: [Hibernated instances are in ‘Stopped’ state](../facts/ec2.md#ec2-faq-hibernated-state-is-stopped)
  say: hibernated instances show Stopped
ec2-faq-high-memory-metal-cases
  claim: For High Memory instances, virtualized instances are generally recommended; metal instances are needed for unsupported OS versions, non-virtualized licensing or support needs, access to hardware features such as Intel VT-x, or a custom hypervisor such as ESXi.
  scope: High Memory instances.
  link: [run in non-virtualized mode to meet licensing](../facts/ec2.md#ec2-faq-high-memory-metal-cases)
  link: [when using custom hypervisor (e.g, ESXi)](../facts/ec2.md#ec2-faq-high-memory-metal-cases)
  say: licensing that needs non-virtualized mode | a custom hypervisor such as ESXi
ec2-faq-instance-store-for-temporary-data
  claim: AWS recommends the local instance store for temporary data, and EBS volumes or backups to Amazon S3 for data that needs higher durability.
  scope: instance store and EBS data placement.
  link: [use the local instance store for temporary data](../facts/ec2.md#ec2-faq-instance-store-for-temporary-data)
  link: [using Amazon EBS volumes or backing up](../facts/ec2.md#ec2-faq-instance-store-for-temporary-data)
  say: instance store is for temporary data | durable data: EBS or a backup to S3
ec2-faq-instance-type-regional-availability
  claim: The EC2 FAQ points to the Amazon EC2 Pricing page for the list of all instances and their regional availability.
  scope: instance type availability by Region.
  link: [visit Amazon EC2 Pricing](../facts/ec2.md#ec2-faq-instance-type-regional-availability)
  say: see the EC2 Pricing page
ec2-faq-inter-instance-flow-bandwidth
  claim: Inter-instance traffic within the same Region can use 5 Gbps for single-flow and up to 25 Gbps for multiflow traffic; in a placement group, select instances can use up to 10 Gbps for single-flow traffic.
  scope: inter-instance traffic within one Region; maximum; not adjustable; actual bandwidth depends on the instance type and its networking performance specification.
  link: [5 Gbps for single-flow](../facts/ec2.md#ec2-faq-inter-instance-flow-bandwidth)
  link: [up to 25 Gbps for multiflow traffic](../facts/ec2.md#ec2-faq-inter-instance-flow-bandwidth)
  link: [up to 10 Gbps for single-flow traffic](../facts/ec2.md#ec2-faq-inter-instance-flow-bandwidth)
  say: five gigabits per second per flow | up to twenty-five gigabits multiflow | up to ten gigabits per flow in a placement group
ec2-faq-launch-under-10-minutes
  claim: It typically takes less than 10 minutes from the RunInstances call until all requested instances begin their boot sequences; AMI size, instance count and recent use of the AMI affect the time.
  scope: from RunInstances to the start of the boot sequence; maximum; typical, not guaranteed.
  link: [less than 10 minutes](../facts/ec2.md#ec2-faq-launch-under-10-minutes)
  say: under ten minutes
ec2-faq-limit-increase-per-region
  claim: An EC2 limit increase applies only to the Region it was requested for.
  scope: EC2 instance limit increases.
  link: [tied to the region they were requested](../facts/ec2.md#ec2-faq-limit-increase-per-region)
  say: an increase applies only to its own Region
ec2-faq-maintenance-live-migration-no-stop
  claim: Non-intrusive maintenance technologies such as live update and live migration do not require instances to be stopped or rebooted, and customers need to take no action.
  scope: AWS maintenance by live update and live migration.
  link: [do not require instances to be stopped](../facts/ec2.md#ec2-faq-maintenance-live-migration-no-stop)
  say: no stop or reboot needed
ec2-faq-nitro-27-pci-devices
  claim: Instances on the Nitro Hypervisor support at most 27 additional PCI devices shared by EBS volumes and VPC network interfaces; for example, 3 additional network interfaces leave room for 24 EBS volumes.
  scope: instances on the Nitro Hypervisor, additional EBS volumes plus network interfaces; maximum; not adjustable; the user guide states a shared attachment limit for most Nitro types; see the volume limits facts.
  link: [27 additional PCI devices](../facts/ec2.md#ec2-faq-nitro-27-pci-devices)
  link: [up to 24 EBS volumes](../facts/ec2.md#ec2-faq-nitro-27-pci-devices)
  say: twenty-seven extra PCI devices | twenty-four EBS volumes with three extra interfaces
ec2-faq-nitro-hypervisor-cpu-memory-isolation
  claim: The Nitro Hypervisor mainly provides CPU and memory isolation, while VPC networking and EBS storage are implemented by dedicated Nitro Card hardware.
  scope: the Nitro Hypervisor.
  link: [CPU and memory isolation for EC2 instances](../facts/ec2.md#ec2-faq-nitro-hypervisor-cpu-memory-isolation)
  link: [implemented by dedicated hardware components, Nitro Cards](../facts/ec2.md#ec2-faq-nitro-hypervisor-cpu-memory-isolation)
  say: CPU and memory isolation | Nitro Cards handle VPC and EBS
ec2-faq-nvidia-gpu-for-cuda
  claim: For deep learning and AI models that need third-party proprietary libraries such as NVIDIA CUDA, cuDNN or TensorRT, AWS recommends NVIDIA GPU-based instances.
  scope: GPU instance choice for deep learning.
  link: [we recommend using the NVIDIA GPU-based instances](../facts/ec2.md#ec2-faq-nvidia-gpu-for-cuda)
  say: NVIDIA GPU instances
ec2-faq-on-demand-family-usage-counts-toward-limit
  claim: All usage of instances in a family, regardless of generation, size or configuration variant, counts toward that family's total vCPU limit.
  scope: per instance family vCPU limit.
  link: [accrue towards the family’s total vCPU limit](../facts/ec2.md#ec2-faq-on-demand-family-usage-counts-toward-limit)
  say: every size and generation counts toward one family limit
ec2-faq-public-ip-released-on-stop
  claim: By default an instance gets a private IP address and a public IP address; the private address stays with the network interface across stop and start, while the public address stays only until the instance is stopped, terminated or given an Elastic IP address.
  scope: an instance's private and auto-assigned public IP addresses.
  link: [remains associated with the network interface](../facts/ec2.md#ec2-faq-public-ip-released-on-stop)
  link: [until it is stopped, terminated or replaced](../facts/ec2.md#ec2-faq-public-ip-released-on-stop)
  say: private IP stays across stop and start | public IP lasts only until stop
ec2-faq-regional-transfer-charged-once
  claim: Regional Data Transfer rates apply when the other instance is in a different Availability Zone or public or Elastic IP addresses are used, but a given instance is charged only once even if both are true.
  scope: Regional Data Transfer between instances.
  link: [only charged once for a given instance](../facts/ec2.md#ec2-faq-regional-transfer-charged-once)
  say: charged once, not twice
ec2-faq-ri-modify-az-scope-size
  claim: During its term, an RI's Availability Zone can be modified, its scope changed between AZ and Region, and its instance size changed within the same family on Linux/Unix.
  scope: per Reserved Instance during its term.
  link: [modify the AZ of the RI](../facts/ec2.md#ec2-faq-ri-modify-az-scope-size)
  link: [scope of the RI from AZ to Region](../facts/ec2.md#ec2-faq-ri-modify-az-scope-size)
  link: [modify instance sizes within the same instance family](../facts/ec2.md#ec2-faq-ri-modify-az-scope-size)
  say: change the AZ | switch zonal and regional | change size within the family
ec2-faq-ri-not-for-spot-or-dedicated-hosts
  claim: Reserved Instance discounts do not apply to Spot Instances or to instances running on Dedicated Hosts; for Dedicated Hosts, AWS points to Dedicated Host Reservations.
  scope: Reserved Instance billing discount.
  link: [RIs do not apply to Spot instances](../facts/ec2.md#ec2-faq-ri-not-for-spot-or-dedicated-hosts)
  link: [purchase Dedicated Host Reservations](../facts/ec2.md#ec2-faq-ri-not-for-spot-or-dedicated-hosts)
  say: Reserved Instances do not cover Spot or Dedicated Hosts | for Dedicated Hosts, buy Dedicated Host Reservations
ec2-faq-ri-region-fixed
  claim: A Standard or Convertible RI cannot be transferred to another Region; its Region is fixed for the whole term.
  scope: per Reserved Instance.
  link: [fixed for the duration of the reservation's term](../facts/ec2.md#ec2-faq-ri-region-fixed)
  say: the Region is fixed for the term
ec2-faq-ri-still-purchasable-sp-encouraged
  claim: RIs can still be purchased and work alongside Savings Plans, but AWS encourages moving to Savings Plans as RIs expire because they offer the same savings with more flexibility.
  scope: Reserved Instances and Savings Plans.
  link: [You can continue purchasing RIs](../facts/ec2.md#ec2-faq-ri-still-purchasable-sp-encouraged)
  link: [encourage you to sign up for Savings Plans](../facts/ec2.md#ec2-faq-ri-still-purchasable-sp-encouraged)
  say: RIs can still be bought | AWS encourages Savings Plans
ec2-faq-ri-transfer-only-via-marketplace
  claim: EC2 Reserved Instances can be transferred only according to the RI Marketplace requirements and cannot otherwise be transferred.
  scope: per Reserved Instance.
  link: [cannot otherwise be transferred](../facts/ec2.md#ec2-faq-ri-transfer-only-via-marketplace)
  say: only through the RI Marketplace
ec2-faq-root-ebs-persists-beyond-instance
  claim: With an Amazon EBS root device, the root device data persists independently of the instance lifetime, so the instance can be stopped and restarted later.
  scope: root device stored on Amazon EBS.
  link: [persist independently from the lifetime of the instance](../facts/ec2.md#ec2-faq-root-ebs-persists-beyond-instance)
  say: EBS root: data outlives the instance
ec2-faq-root-instance-store-life-of-instance
  claim: With an instance store root device, root device data persists only during the life of the instance.
  scope: root device on the local instance store.
  link: [only persists during the life of the instance](../facts/ec2.md#ec2-faq-root-instance-store-life-of-instance)
  say: instance store root: data lasts only while the instance lives
ec2-faq-savings-plans-no-capacity-reservation
  claim: Savings Plans do not reserve capacity; capacity can be reserved with On-Demand Capacity Reservations, which Savings Plans can make cheaper.
  scope: Savings Plans for EC2.
  link: [Savings Plans do not provide a capacity reservation](../facts/ec2.md#ec2-faq-savings-plans-no-capacity-reservation)
  link: [pay lower prices on them with Savings Plans](../facts/ec2.md#ec2-faq-savings-plans-no-capacity-reservation)
  say: Savings Plans give a discount, not capacity
ec2-faq-spot-all-public-regions
  claim: Spot Instances are available in all public AWS Regions and for nearly all EC2 instance families and sizes.
  scope: Spot Instance availability.
  link: [available in all public AWS regions](../facts/ec2.md#ec2-faq-spot-all-public-regions)
  link: [nearly all EC2 instance families and sizes](../facts/ec2.md#ec2-faq-spot-all-public-regions)
  say: every public Region | nearly all families and sizes
ec2-faq-spot-charge-when-ec2-interrupts-first-hour
  claim: If Amazon EC2 terminates or stops a Spot Instance in its first instance hour, that usage is not charged; if the user stops or terminates it, usage is charged to the nearest second, except on SUSE Linux Enterprise Server (SLES), where a user stop or termination is charged for an entire hour.
  scope: Spot Instance billing on stop or interruption; the free first hour applies only when Amazon EC2 stops or terminates the instance; on SLES a user stop or termination is charged for an entire hour.
  link: [you will not be charged for that usage](../facts/ec2.md#ec2-faq-spot-charge-when-ec2-interrupts-first-hour)
  link: [charged to the nearest second](../facts/ec2.md#ec2-faq-spot-charge-when-ec2-interrupts-first-hour)
  say: interrupted by EC2 in the first hour: no charge | stopped by you: charged per second
ec2-faq-spot-fleet-no-auto-rebalance
  claim: Spot Fleet does not automatically terminate and relaunch running instances when cheaper pools appear; it replaces a terminated Spot Instance according to its allocation strategy.
  scope: Spot Fleet.
  link: [do not automatically terminate and relaunch instances](../facts/ec2.md#ec2-faq-spot-fleet-no-auto-rebalance)
  link: [Spot Fleet will replenish it](../facts/ec2.md#ec2-faq-spot-fleet-no-auto-rebalance)
  say: no automatic moves | it replaces terminated instances
ec2-faq-spot-fleet-not-guaranteed
  claim: Spot Fleet requests are not guaranteed to be fulfilled; they are subject to the same availability and prices as a single Spot Instance request.
  scope: Spot Fleet requests.
  link: [subject to the same availability and prices](../facts/ec2.md#ec2-faq-spot-fleet-not-guaranteed)
  say: no, Spot Fleet has the same availability as one Spot request
ec2-faq-spot-hibernate-benefit-ram-state
  claim: With hibernation, Spot Instances pause and resume around interruptions so workloads continue where they left off; it fits applications that depend on session or other data stored in RAM.
  scope: Spot Instances with hibernation.
  link: [pause and resume around any interruptions](../facts/ec2.md#ec2-faq-spot-hibernate-benefit-ram-state)
  link: [session data stored in RAM](../facts/ec2.md#ec2-faq-spot-hibernate-benefit-ram-state)
  say: pause and resume | for state held in RAM
ec2-faq-spot-hibernate-no-instance-fee
  claim: Hibernating a Spot Instance has no additional charge beyond EBS storage and other resources in use, and no instance usage fees are charged once it is hibernated.
  scope: a hibernated Spot Instance.
  link: [You are not charged instance usage fees](../facts/ec2.md#ec2-faq-spot-hibernate-no-instance-fee)
  link: [beyond the EBS storage costs](../facts/ec2.md#ec2-faq-spot-hibernate-no-instance-fee)
  say: no instance fees while hibernated | only EBS storage and other resources
ec2-faq-spot-hibernated-resumed-by-ec2
  claim: A user cannot directly resume a Spot Instance that Spot hibernated; Amazon EC2 controls the hibernate-resume cycle and resumes the instance when capacity becomes available.
  scope: Spot Instances hibernated by Spot.
  link: [Hibernate-resume cycle is controlled by Amazon EC2](../facts/ec2.md#ec2-faq-spot-hibernated-resumed-by-ec2)
  link: [when the capacity becomes available](../facts/ec2.md#ec2-faq-spot-hibernated-resumed-by-ec2)
  say: Amazon EC2, not you, resumes it
ec2-faq-spot-interruptions-mostly-by-customer
  claim: Over the last 3 months, 92% of Spot Instance interruptions were customers terminating the instance themselves because the application had completed its work.
  scope: Spot Instance interruptions over the last 3 months, as stated by the FAQ.
  link: [92%](../facts/ec2.md#ec2-faq-spot-interruptions-mostly-by-customer)
  say: ninety-two percent
ec2-faq-spot-limit-per-region
  claim: Spot Instances can be requested up to the account's Spot limit for each Region; new customers might start with a lower limit.
  scope: Spot Instance requests per account per Region; maximum; adjustable.
  link: [up to your Spot limit for each region](../facts/ec2.md#ec2-faq-spot-limit-per-region)
  say: up to the Spot limit per Region
ec2-faq-spot-no-windows-sql-server
  claim: Linux/UNIX, Windows Server and Red Hat Enterprise Linux are available as Spot Instances; Windows Server with SQL Server is not currently available.
  scope: Spot Instance operating systems.
  link: [Windows Server with SQL Server](../facts/ec2.md#ec2-faq-spot-no-windows-sql-server)
  say: Windows with SQL Server is not available on Spot
ec2-faq-spot-price-per-utc-hour
  claim: A Spot Instance pays the Spot price in effect at the beginning of each UTC hour, applied to the usage of the following hour.
  scope: running Spot Instances.
  link: [beginning of each UTC hour](../facts/ec2.md#ec2-faq-spot-price-per-utc-hour)
  say: the price at the start of each UTC hour
ec2-faq-spot-same-instances-as-on-demand
  claim: While running, Spot Instances are the same as On-Demand or Reserved Instances; Spot is best suited for fault-tolerant, flexible workloads.
  scope: Spot Instances.
  link: [exactly the same as On-Demand or Reserved instances](../facts/ec2.md#ec2-faq-spot-same-instances-as-on-demand)
  link: [best suited for fault-tolerant, flexible workloads](../facts/ec2.md#ec2-faq-spot-same-instances-as-on-demand)
  say: a running Spot Instance is the same instance | use Spot for fault-tolerant, flexible work
ec2-faq-spot-start-needs-capacity
  claim: A stopped Spot Instance starts only if Spot capacity is still available within the maximum price; capacity is checked at every start.
  scope: stopped Spot Instances; Spot capacity available within the maximum price.
  link: [start only if Spot capacity is still available](../facts/ec2.md#ec2-faq-spot-start-needs-capacity)
  say: it starts only if Spot capacity is still there
ec2-faq-spot-stop-persistent-requests-only
  claim: A user can stop a running Spot Instance and keep it for later use instead of terminating it or cancelling the Spot request; the EC2 FAQ says stop is available for persistent Spot requests.
  scope: Spot Instances; persistent Spot request.
  link: [Stop is available for persistent Spot requests](../facts/ec2.md#ec2-faq-spot-stop-persistent-requests-only)
  link: [keep these stopped instances for later use](../facts/ec2.md#ec2-faq-spot-stop-persistent-requests-only)
  say: you can stop a Spot Instance that comes from a persistent request
ec2-faq-spot-use-multiple-pools
  claim: AWS recommends using multiple Spot capacity pools to get the most Spot capacity, and EC2 Auto Scaling, EC2 Fleet and Spot Fleet can find cost-effective capacity across pools.
  scope: Spot Instances best practice.
  link: [using multiple Spot capacity pools](../facts/ec2.md#ec2-faq-spot-use-multiple-pools)
  say: spread Spot across many capacity pools
ec2-faq-stopped-instance-ebs-still-charged
  claim: For a stopped instance, AWS does not charge hourly usage or data transfer fees, but it does charge for the storage of any attached Amazon EBS volumes.
  scope: a stopped instance.
  link: [we do charge for the storage](../facts/ec2.md#ec2-faq-stopped-instance-ebs-still-charged)
  link: [don't charge hourly usage for a stopped instance](../facts/ec2.md#ec2-faq-stopped-instance-ebs-still-charged)
  say: EBS storage is still charged | no instance-hour charge while stopped
ec2-faq-t2-ri-or-spot
  claim: T2 instances can be bought as On-Demand Instances, Reserved Instances or Spot Instances.
  scope: T2 instances.
  link: [On-Demand Instances, Reserved Instances or Spot Instances](../facts/ec2.md#ec2-faq-t2-ri-or-spot)
  say: On-Demand, Reserved or Spot
ec2-faq-t2-zero-credits-baseline
  claim: When a T2 instance's CPU credit balance is zero, its performance stays at the baseline CPU performance.
  scope: T2 instances in standard mode.
  link: [performance will remain at baseline CPU performance](../facts/ec2.md#ec2-faq-t2-zero-credits-baseline)
  say: it drops to baseline
ec2-faq-trainium-inferentia-save-up-to-50
  claim: AWS Trainium and AWS Inferentia instances are purpose built for deep learning and generative AI, and AWS states they can save up to 50% on training and inference costs over comparable EC2 instances.
  scope: training and inference costs versus comparable EC2 instances; maximum.
  link: [up to 50%](../facts/ec2.md#ec2-faq-trainium-inferentia-save-up-to-50)
  link: [purpose built for deep learning and generative AI](../facts/ec2.md#ec2-faq-trainium-inferentia-save-up-to-50)
  say: up to fifty percent | built for deep learning
ec2-fleet-auto-scaling-recommended-method
  claim: As a general best practice, AWS recommends launching fleets of Spot and On-Demand Instances with Amazon EC2 Auto Scaling, because it adds features to manage the fleet.
  scope: fleets of Spot and On-Demand Instances.
  link: [with Amazon EC2 Auto Scaling](../facts/ec2.md#ec2-fleet-auto-scaling-recommended-method)
  say: use an Auto Scaling group
ec2-fleet-capacity-rebalancing-replaces-at-risk-spot
  claim: With Capacity Rebalancing enabled, a rebalance recommendation makes an EC2 Fleet or Spot Fleet launch a new Spot Instance before the at-risk instance is interrupted; it is available only for fleets of type maintain.
  scope: EC2 Fleet and Spot Fleet Capacity Rebalancing; Capacity Rebalancing enabled.
  link: [triggers the launch of a new Spot Instance](../facts/ec2.md#ec2-fleet-capacity-rebalancing-replaces-at-risk-spot)
  link: [before the at-risk instance is interrupted](../facts/ec2.md#ec2-fleet-capacity-rebalancing-replaces-at-risk-spot)
  link: [available only for fleets of type maintain](../facts/ec2.md#ec2-fleet-capacity-rebalancing-replaces-at-risk-spot)
  say: the rebalance signal launches a replacement Spot Instance | before the old one is interrupted
ec2-fleet-mixes-spot-and-on-demand
  claim: A fleet can launch multiple purchase options, Spot and On-Demand Instances, and Reserved Instance and Savings Plans discounts apply to the On-Demand Instances in the fleet.
  scope: EC2 Fleet and Spot Fleet.
  link: [multiple purchase options (Spot and On-Demand Instances)](../facts/ec2.md#ec2-fleet-mixes-spot-and-on-demand)
  say: a fleet can mix Spot and On-Demand
ec2-fleet-spot-price-capacity-optimized-recommended
  claim: For EC2 Fleet, AWS recommends the price capacity optimized Spot allocation strategy as the best choice for most Spot workloads and does not recommend the lowest price strategy, which has the highest interruption risk even though it is the default when you use the AWS CLI.
  scope: EC2 Fleet and Spot Fleet Spot allocation; default; the AWS CLI default is lowest price.
  link: [the best choice for most Spot workloads](../facts/ec2.md#ec2-fleet-spot-price-capacity-optimized-recommended)
  link: [highest risk of interruption](../facts/ec2.md#ec2-fleet-spot-price-capacity-optimized-recommended)
  link: [this is the default strategy](../facts/ec2.md#ec2-fleet-spot-price-capacity-optimized-recommended)
  say: price capacity optimized is the recommended strategy | lowest price has the highest interruption risk | lowest price is the CLI default
ec2-fleet-vs-spot-fleet-console-and-legacy
  claim: EC2 Fleet and Spot Fleet offer the same core functionality, but EC2 Fleet is available only from a command line, and Spot Fleet has console support but uses a legacy API with no planned investment.
  scope: EC2 Fleet and Spot Fleet.
  link: [only available using a command line](../facts/ec2.md#ec2-fleet-vs-spot-fleet-console-and-legacy)
  link: [a legacy API with no planned investment](../facts/ec2.md#ec2-fleet-vs-spot-fleet-console-and-legacy)
  say: EC2 Fleet is command line only | Spot Fleet is a legacy API
ec2-free-data-transfer-out-100-gb-per-month
  claim: AWS customers receive 100 GB of free data transfer out to the internet each month, aggregated across all AWS services and Regions (except China and GovCloud); rate tiers take into account aggregate Data Transfer Out to the internet across Amazon EC2, Amazon S3, Amazon RDS and other listed services.
  scope: AWS customers, per month, aggregated across all AWS services and Regions; maximum; except China and GovCloud.
  link: [100 GB of free data transfer out to the internet](../facts/ec2.md#ec2-free-data-transfer-out-100-gb-per-month)
  say: one hundred gigabytes free per month
ec2-free-tier-six-months-after-july-2025
  claim: Accounts created on or after July 15, 2025 can use t3.micro, t3.small, t4g.micro, t4g.small, t8i.micro and t8i.small for 6 months or until their credits are used up; accounts created before that date and less than 12 months old can use a t2.micro (or t3.micro where t2 is unavailable) for free within usage limits.
  scope: per account; maximum; account creation date relative to July 15, 2025.
  link: [for 6 months or until your credits are used up](../facts/ec2.md#ec2-free-tier-six-months-after-july-2025)
  link: [less than 12 months old, you can use a t2.micro instance for free](../facts/ec2.md#ec2-free-tier-six-months-after-july-2025)
  say: six months or until the credits run out
  changed: 2025-07-15: was you can use a `t2.micro` instance for free (or a `t3.micro` instance in Regions where `t2.micro` is unavailable) within certain usage limits
ec2-global-view-read-only
  claim: AWS Global View shows some of your resources in one Region or across many Regions in a single console, with a global search across Regions, but it does not let you modify resources.
  scope: AWS Global View console.
  link: [across multiple Regions in a single console](../facts/ec2.md#ec2-global-view-read-only)
  link: [does not let you modify resources](../facts/ec2.md#ec2-global-view-read-only)
  say: it shows resources across Regions | it cannot change resources
ec2-graviton-40-percent-better-price-performance
  claim: EC2 instances powered by AWS Graviton processors deliver up to 40% better price performance than comparable non-Graviton-based instances.
  scope: Graviton-based EC2 instances compared with comparable non-Graviton instances; maximum.
  link: [up to 40% better price performance](../facts/ec2.md#ec2-graviton-40-percent-better-price-performance)
  say: up to forty percent better price performance
ec2-graviton-compiled-apps-recompile
  claim: Applications in interpreted languages such as Java, Node and Python that are not reliant on native CPU instruction sets should run on Arm with minimal to no changes, while applications in compiled languages such as C, C++ and GoLang need to be re-compiled to generate Arm binaries.
  scope: moving applications to Graviton (Arm) instances.
  link: [need to be re-compiled to generate Arm binaries](../facts/ec2.md#ec2-graviton-compiled-apps-recompile)
  say: compiled code must be rebuilt for Arm
ec2-graviton-needs-arm64-ami
  claim: Graviton-based M6g and A1 instances need arm64 AMIs; x86 AMIs are not compatible with them.
  scope: Graviton-based M6g and A1 instances.
  link: [x86 AMIs are not compatible](../facts/ec2.md#ec2-graviton-needs-arm64-ami)
  say: no, you need an arm64 AMI
ec2-hibernate-cannot-modify-while-hibernated
  claim: A hibernated instance cannot be modified, unlike a plain stopped instance whose instance type or size can be changed.
  scope: per hibernated instance.
  link: [instance is hibernated, you can't modify it](../facts/ec2.md#ec2-hibernate-cannot-modify-while-hibernated)
  say: no changes while hibernated
ec2-hibernate-ebs-volume-types
  claim: Hibernation supports only General Purpose SSD (gp2 and gp3) and Provisioned IOPS SSD (io1 and io2) EBS volume types.
  scope: per instance.
  link: [gp2 and gp3](../facts/ec2.md#ec2-hibernate-ebs-volume-types)
  link: [io1 and io2](../facts/ec2.md#ec2-hibernate-ebs-volume-types)
  say: gp two and gp three | io one and io two
ec2-hibernate-enable-only-at-launch
  claim: Hibernation can be enabled only when an On-Demand or Spot Instance is launched; it cannot be enabled on an existing running or stopped instance.
  scope: per instance.
  link: [when you launch it](../facts/ec2.md#ec2-hibernate-enable-only-at-launch)
  link: [can't enable hibernation on an existing instance](../facts/ec2.md#ec2-hibernate-enable-only-at-launch)
  say: only at launch | not on an existing instance
ec2-hibernate-max-duration
  claim: An instance cannot stay hibernated for more than 60 days; to keep it longer you must start the hibernated instance, stop it and start it again.
  scope: per instance; maximum; not adjustable.
  link: [60 days](../facts/ec2.md#ec2-hibernate-max-duration)
  say: sixty days
ec2-hibernate-no-instance-fee-ebs-rates
  claim: A hibernated instance is charged at standard EBS storage rates and, like a stopped instance, incurs no instance usage fee; any Elastic IP addresses associated with it are still charged.
  scope: per hibernated instance.
  link: [charged at standard EBS rates for storage](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  link: [you do not incur instance usage fees](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  link: [charged for any Elastic IP addresses](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  say: only EBS storage | Elastic IPs are still charged
ec2-hibernate-not-in-auto-scaling-group
  claim: You cannot hibernate an instance that is in an Auto Scaling group or used by Amazon ECS; if you try, Amazon EC2 Auto Scaling marks the stopped instance as unhealthy and might terminate and replace it.
  scope: per instance.
  link: [You can't hibernate an instance](../facts/ec2.md#ec2-hibernate-not-in-auto-scaling-group)
  link: [Auto Scaling group or used by Amazon ECS](../facts/ec2.md#ec2-hibernate-not-in-auto-scaling-group)
  say: cannot hibernate an instance that is in an Auto Scaling group | in an Auto Scaling group or used by ECS
ec2-hibernate-ram-limits-linux-windows
  claim: A Linux instance cannot be hibernated if it has more than 150 GiB of RAM, and a Windows instance cannot be hibernated if it has more than 16 GiB of RAM.
  scope: per instance; maximum; not adjustable; Linux 150 GiB; Windows 16 GiB.
  link: [150 GiB](../facts/ec2.md#ec2-hibernate-ram-limits-linux-windows)
  link: [16 GiB](../facts/ec2.md#ec2-hibernate-ram-limits-linux-windows)
  say: one hundred fifty gibibytes for Linux | sixteen gibibytes for Windows
ec2-hibernate-root-volume-requirements
  claim: Hibernation requires the root volume to be an EBS volume, not an instance store volume, and that root volume must be encrypted.
  scope: per instance.
  link: [EBS volume](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  link: [must be encrypted](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  say: EBS volume | must be encrypted
ec2-hibernate-saves-ram-to-root-volume
  claim: Hibernation signals the operating system to suspend to disk, which saves the contents of RAM to the EBS root volume; when the instance starts again the root volume is restored, the RAM contents are reloaded and the instance keeps its instance ID.
  scope: hibernated EBS-backed instances.
  link: [saves the contents from the instance memory (RAM)](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the RAM contents are reloaded](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the instance retains its instance ID](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  say: hibernation saves the RAM to the EBS root volume
ec2-hibernate-spot-persistent-request
  claim: To hibernate a Spot Instance the Spot request must be persistent and must not specify a launch group; a Spot Instance that Amazon EC2 hibernated can be resumed only by Amazon EC2, when capacity returns at or below your maximum price.
  scope: per Spot Instance; interruption behavior hibernate.
  link: [The Spot Instance request type must be persistent](../facts/ec2.md#ec2-hibernate-spot-persistent-request)
  link: [only Amazon EC2 can resume your instance](../facts/ec2.md#ec2-hibernate-spot-persistent-request)
  say: a persistent Spot request | only EC2 resumes it
ec2-hibernate-supported-families-no-bare-metal
  claim: Hibernation needs an instance family that supports hibernation, and bare metal instances are not supported; the supported list covers general purpose families (including T2, T3, T3a, T4g and T8i), compute optimized, memory optimized and storage optimized families. Hibernation works with instances in all AWS Regions.
  scope: per instance.
  link: [bare metal instances are not supported](../facts/ec2.md#ec2-hibernate-supported-families-no-bare-metal)
  link: [all AWS Regions](../facts/ec2.md#ec2-hibernate-supported-families-no-bare-metal)
  say: no bare metal | every Region
ec2-host-isolation-between-instances
  claim: Different EC2 instances on the same physical host are isolated from each other as though they are on separate physical hosts; the hypervisor isolates CPU and memory.
  scope: EC2 instances on shared hosts.
  link: [as though they are on separate physical hosts](../facts/ec2.md#ec2-host-isolation-between-instances)
  say: isolated as if on separate hosts
ec2-hybrid-purchasing-common-pattern
  claim: A common pattern is Savings Plans for baseline capacity, On-Demand or Spot Instances for fluctuating load, and On-Demand Capacity Reservations for mission-critical applications that need capacity assurance.
  scope: EC2 purchasing strategy.
  link: [Savings Plans for baseline capacity](../facts/ec2.md#ec2-hybrid-purchasing-common-pattern)
  link: [On-Demand or Spot Instances for fluctuating workloads](../facts/ec2.md#ec2-hybrid-purchasing-common-pattern)
  say: Savings Plans for the baseline | On-Demand or Spot for the changing part
ec2-iam-role-no-credential-distribution
  claim: IAM roles let applications on EC2 instances make API requests securely without you creating, distributing or managing the security credentials the applications use.
  scope: IAM roles for EC2 instances.
  link: [without requiring you to manage the security credentials](../facts/ec2.md#ec2-iam-role-no-credential-distribution)
  link: [Instead of creating and distributing your AWS credentials](../facts/ec2.md#ec2-iam-role-no-credential-distribution)
  say: no credentials for you to manage | no keys to copy onto instances
ec2-iam-role-one-per-instance
  claim: You can attach only one IAM role to an instance, but you can attach the same role to many instances; an instance profile, the container EC2 uses for a role, can contain only one IAM role.
  scope: per EC2 instance; maximum.
  link: [only attach one IAM role to an instance](../facts/ec2.md#ec2-iam-role-one-per-instance)
  link: [attach the same role to many instances](../facts/ec2.md#ec2-iam-role-one-per-instance)
  link: [can contain only one IAM role](../facts/ec2.md#ec2-iam-role-one-per-instance)
  say: one role per instance | one role can serve many instances | an instance profile holds one role
ec2-iam-role-temporary-credentials-rotated
  claim: An application on the instance gets the role's security credentials from instance metadata; these credentials are temporary and AWS rotates them automatically, and the AWS SDKs and AWS CLI on the instance get them automatically.
  scope: IAM roles for EC2 instances.
  link: [These security credentials are temporary](../facts/ec2.md#ec2-iam-role-temporary-credentials-rotated)
  link: [we rotate them automatically](../facts/ec2.md#ec2-iam-role-temporary-credentials-rotated)
  link: [from the EC2 instance metadata service](../facts/ec2.md#ec2-iam-role-temporary-credentials-rotated)
  say: the credentials are temporary | AWS rotates them for you | the SDKs and CLI fetch them from instance metadata
ec2-imds-account-default-v2-new-instances
  claim: You can set the account default for the instance metadata version to IMDSv2 in each Region, so that new instances launch with IMDSv2 required (HttpTokens required) and a response hop limit of 2; the account default does not change existing instances.
  scope: per account, per Region; default; adjustable; account default set to IMDSv2; values can be overridden at launch.
  link: [launch with IMDSv2 required](../facts/ec2.md#ec2-imds-account-default-v2-new-instances)
  link: [`HttpPutResponseHopLimit` is set to `2`](../facts/ec2.md#ec2-imds-account-default-v2-new-instances)
  link: [do not affect existing instances](../facts/ec2.md#ec2-imds-account-default-v2-new-instances)
  say: new instances launch with IMDSv2 required | the hop limit becomes two | existing instances do not change
ec2-imds-account-enforcement-v2
  claim: You can enforce IMDSv2 at the account level for each Region; when it is enforced, an instance can launch only if it is configured to require IMDSv2, regardless of how the instance or AMI is configured, and a launch with IMDSv1 enabled fails.
  scope: per account, per Region; IMDSv2 enforcement enabled.
  link: [configured to require IMDSv2](../facts/ec2.md#ec2-imds-account-enforcement-v2)
  link: [the instance launch will fail](../facts/ec2.md#ec2-imds-account-enforcement-v2)
  say: only instances that require IMDSv2 can launch | a launch that allows IMDSv1 fails
ec2-imds-addresses-ipv4-ipv6
  claim: The Instance Metadata Service is reached at the IPv4 address 169.254.169.254; to retrieve instance metadata over IPv6 you enable and use the IMDS IPv6 address fd00:ec2::254, which needs a Nitro-based instance launched in a subnet that supports IPv6.
  scope: per instance; fixed; the IPv6 address must be enabled, and the instance must be Nitro-based in a subnet that supports IPv6.
  link: [169.254.169.254](../facts/ec2.md#ec2-imds-addresses-ipv4-ipv6)
  link: [fd00:ec2::254](../facts/ec2.md#ec2-imds-addresses-ipv4-ipv6)
  say: one six nine dot two five four dot one six nine dot two five four | f d zero zero, e c two, two five four
ec2-imds-ami-imds-support-v2
  claim: When you register or modify an AMI with the imds-support parameter set to v2.0, instances launched from that AMI get IMDSv2 as the metadata version and a hop limit of 2.
  scope: per AMI; default; adjustable; imds-support set to v2.0; launch and account settings take precedence.
  link: [automatically set to IMDSv2](../facts/ec2.md#ec2-imds-ami-imds-support-v2)
  link: [the hop limit is set to 2](../facts/ec2.md#ec2-imds-ami-imds-support-v2)
  say: an AMI with imds-support v2.0 launches instances that require IMDSv2 | and a hop limit of two
ec2-imds-default-v1-or-v2
  claim: By default, an instance accepts either IMDSv1 or IMDSv2 calls, or both; you can configure the Instance Metadata Service on each instance to accept only IMDSv2 calls, which makes IMDSv1 calls fail.
  scope: per instance; default; adjustable; when no launch, account or AMI setting requires IMDSv2.
  link: [either IMDSv1 or IMDSv2, or both](../facts/ec2.md#ec2-imds-default-v1-or-v2)
  link: [only accept IMDSv2 calls](../facts/ec2.md#ec2-imds-default-v1-or-v2)
  say: by default both IMDSv1 and IMDSv2 work | you can make an instance accept only IMDSv2
ec2-imds-options-precedence
  claim: Each instance metadata option is set at launch and evaluated separately, in this order of precedence: the instance configuration at launch (launch template or instance settings) first, then the account settings for the Region, then the AMI configuration, which applies only to HttpTokens and HttpPutResponseHopLimit.
  scope: per instance launch, per metadata option; the AMI level applies only to HttpTokens and HttpPutResponseHopLimit.
  link: [Precedence 1: Instance configuration at launch](../facts/ec2.md#ec2-imds-options-precedence)
  link: [Precedence 2: Account settings](../facts/ec2.md#ec2-imds-options-precedence)
  link: [Precedence 3: AMI configuration](../facts/ec2.md#ec2-imds-options-precedence)
  say: the launch settings win first | then the account settings | then the AMI
ec2-imds-put-hop-limit-default-1
  claim: By default, the response to IMDSv2 PUT requests has a hop limit of 1 at the IP protocol level; AWS suggests raising the hop limit to 2 in a container environment.
  scope: per instance metadata options; default; adjustable; can be changed with modify-instance-metadata-options.
  link: [hop limit of 1](../facts/ec2.md#ec2-imds-put-hop-limit-default-1)
  link: [increasing the hop limit to 2](../facts/ec2.md#ec2-imds-put-hop-limit-default-1)
  say: a hop limit of one by default | two for containers
ec2-imdsv2-token-ttl-1-second-to-6-hours
  claim: An IMDSv2 session token lasts for the duration set in the PUT request, from a minimum of 1 second to a maximum of 6 hours (21,600 seconds).
  scope: per IMDSv2 session token; maximum; not adjustable; the TTL is set in the token PUT request header.
  link: [maximum of six hours (21,600 seconds)](../facts/ec2.md#ec2-imdsv2-token-ttl-1-second-to-6-hours)
  link: [minimum of one second](../facts/ec2.md#ec2-imdsv2-token-ttl-1-second-to-6-hours)
  say: up to six hours | at least one second
ec2-instance-store-root-no-stop
  claim: Data on instance store volumes persists only while the instance runs; it is deleted when the instance is terminated or fails, and an instance with an instance store root volume does not support the Stop action.
  scope: instances with an instance store root volume.
  link: [do not support the Stop action](../facts/ec2.md#ec2-instance-store-root-no-stop)
  link: [persists as long as the instance is running](../facts/ec2.md#ec2-instance-store-root-no-stop)
  say: an instance store backed instance cannot be stopped, only terminated
ec2-instance-type-name-structure
  claim: An instance type name has an instance family and an instance size: the first position is the series, the second is the generation, the third is the options, and after the period comes the size, such as small, 4xlarge or metal for bare metal.
  scope: per instance type name.
  link: [instance family and instance size](../facts/ec2.md#ec2-instance-type-name-structure)
  link: [family indicates the series](../facts/ec2.md#ec2-instance-type-name-structure)
  link: [The second position indicates the generation](../facts/ec2.md#ec2-instance-type-name-structure)
  link: [The third position indicates the options](../facts/ec2.md#ec2-instance-type-name-structure)
  say: family first, then size | the first letter is the series | the number is the generation | the letters after the number are options
ec2-instance-type-option-letters
  claim: In an instance type name, option letters after the generation number show processor and capabilities: a is AMD processors, g is AWS Graviton processors, i is Intel processors, d is instance store volumes, n is network and EBS optimized, e is extra storage, memory or GPU memory, and flex is a Flex instance.
  scope: per instance type name; e means extra instance storage, extra memory or extra GPU memory, depending on the category.
  link: [AMD processors](../facts/ec2.md#ec2-instance-type-option-letters)
  link: [AWS Graviton processors](../facts/ec2.md#ec2-instance-type-option-letters)
  link: [Intel processors](../facts/ec2.md#ec2-instance-type-option-letters)
  link: [Instance store volumes](../facts/ec2.md#ec2-instance-type-option-letters)
  link: [Network and EBS optimized](../facts/ec2.md#ec2-instance-type-option-letters)
  link: [Flex instance](../facts/ec2.md#ec2-instance-type-option-letters)
  say: a means AMD | g means Graviton | i means Intel | d means local instance store | n means network and EBS optimized | flex means a Flex instance
ec2-instance-type-series-letters
  claim: In an instance type name, the series letter shows the broad purpose: for example C is compute optimized, M is general purpose, R is memory optimized, I is storage optimized, T is burstable performance, P is GPU accelerated and G is graphics intensive.
  scope: per instance type name.
  link: [Compute optimized](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [General purpose](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [Memory optimized](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [Storage optimized](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [Burstable performance](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [GPU accelerated](../facts/ec2.md#ec2-instance-type-series-letters)
  link: [Graphics intensive](../facts/ec2.md#ec2-instance-type-series-letters)
  say: C means compute optimized | M means general purpose | R means memory optimized | I means storage optimized | T means burstable performance | P means GPU accelerated | G means graphics intensive
ec2-instance-type-sizes-scale-resources
  claim: Instance types combine CPU, memory, storage and networking capacity in different ways, and each instance type includes one or more instance sizes, so you can scale resources to the requirements of the workload.
  scope: EC2 instance types.
  link: [one or more instance sizes](../facts/ec2.md#ec2-instance-type-sizes-scale-resources)
  link: [scale your resources to the requirements](../facts/ec2.md#ec2-instance-type-sizes-scale-resources)
  say: each type comes in several sizes | pick the size that fits the workload
ec2-instance-virtual-server-type-sets-hardware
  claim: An EC2 instance is a virtual server in the AWS Cloud; the instance type you specify at launch determines the hardware available to it, and each type offers a different balance of compute, memory, network and storage resources.
  scope: EC2 instances.
  link: [a virtual server in the AWS Cloud](../facts/ec2.md#ec2-instance-virtual-server-type-sets-hardware)
  link: [determines the hardware available to your instance](../facts/ec2.md#ec2-instance-virtual-server-type-sets-hardware)
  say: a virtual server | the instance type sets the hardware
ec2-interruptible-cr-billing-split
  claim: An interruptible Capacity Reservation is billed as an independent new reservation: the source reservation is billed for total capacity minus the allocated capacity, and the interruptible reservation for the allocated capacity.
  scope: interruptible Capacity Reservation.
  link: [billed for it as an independent new reservation](../facts/ec2.md#ec2-interruptible-cr-billing-split)
  say: billing is split between the source and the interruptible reservation
ec2-interruptible-cr-reclaim-terminates
  claim: With an interruptible Capacity Reservation the owner can reclaim the capacity at any time; when it is reclaimed, the consumer instances running in it are terminated, with no fallback to On-Demand or Spot, and the capacity returns to the source reservation.
  scope: interruptible Capacity Reservation; when the owner reclaims capacity.
  link: [any running consumer instances are terminated](../facts/ec2.md#ec2-interruptible-cr-reclaim-terminates)
  link: [there is no fallback to On-Demand or Spot](../facts/ec2.md#ec2-interruptible-cr-reclaim-terminates)
  say: the consumer instances are terminated | there is no fallback to On-Demand or Spot
ec2-interruptible-cr-targeted-share-ram
  claim: Interruptible Capacity Reservations are targeted by default, so an instance launch must target them; they can be shared with other accounts or an AWS organization through AWS RAM, and AWS recommends them only for applications that can be interrupted.
  scope: interruptible Capacity Reservation, capacity consumers; default.
  link: [by default targeted Capacity Reservations](../facts/ec2.md#ec2-interruptible-cr-targeted-share-ram)
  link: [applications that can be interrupted](../facts/ec2.md#ec2-interruptible-cr-targeted-share-ram)
  say: they are targeted, so the launch must target them | only for workloads that can be interrupted
ec2-key-pair-private-key-not-kept
  claim: Amazon EC2 stores the public key on your instance and you store the private key; because EC2 doesn't keep a copy of the private key, a lost private key can't be recovered.
  scope: EC2 key pairs.
  link: [stores the public key on your instance](../facts/ec2.md#ec2-key-pair-private-key-not-kept)
  link: [doesn't keep a copy of your private key](../facts/ec2.md#ec2-key-pair-private-key-not-kept)
  link: [no way to recover a private key](../facts/ec2.md#ec2-key-pair-private-key-not-kept)
  say: AWS keeps only the public key | AWS has no copy of the private key | a lost private key is gone
ec2-launch-template-stores-launch-parameters
  claim: A launch template stores instance launch parameters, such as the AMI ID, instance type and network settings, so you do not have to specify them every time you launch an instance.
  scope: EC2 launch templates.
  link: [the AMI ID, instance type, and network settings](../facts/ec2.md#ec2-launch-template-stores-launch-parameters)
  say: the AMI, instance type and network settings
ec2-launch-template-versions-default
  claim: A launch template stores launch parameters such as the AMI ID, instance type and network settings in numbered versions; when you launch without naming a version, the default version is used, and the default version is the first version unless you set another one.
  scope: per launch template; default; adjustable; no version specified at launch.
  link: [the default version is used](../facts/ec2.md#ec2-launch-template-versions-default)
  link: [it's the first version of the launch template](../facts/ec2.md#ec2-launch-template-versions-default)
  say: without a version, the default version is used | the default is the first version unless you change it
ec2-launch-template-versions-quota-10000
  claim: A launch template can have at most 10,000 versions per Region per account, and this quota is not adjustable.
  scope: per launch template, per Region, per account; maximum; not adjustable.
  link: [10,000 versions](../facts/ec2.md#ec2-launch-template-versions-quota-10000)
  say: ten thousand versions per launch template
ec2-launch-templates-quota-5000
  claim: An account can have at most 5,000 launch templates per Region, and this quota is not adjustable.
  scope: per account, per Region; maximum; not adjustable.
  link: [5,000 launch templates per Region](../facts/ec2.md#ec2-launch-templates-quota-5000)
  say: five thousand launch templates per Region
ec2-link-local-services-1024-pps-limit
  claim: There is a 1024 packet per second (PPS) limit to services that use link-local addresses.
  scope: services that use link-local addresses, in aggregate; maximum; not adjustable.
  link: [1024 packet per second (PPS) limit](../facts/ec2.md#ec2-link-local-services-1024-pps-limit)
  say: one thousand twenty-four packets per second
ec2-managed-instance-delegated-control
  claim: An Amazon EC2 managed instance is provisioned and managed by a designated service provider such as EKS Auto Mode or Amazon ECS managed instances; you can't modify its settings or terminate it directly, but you can tag it, and it has the same base charge as a normal instance plus a separate provider fee.
  scope: Amazon EC2 managed instances.
  link: [managed by a designated service provider](../facts/ec2.md#ec2-managed-instance-delegated-control)
  link: [You can’t directly modify the settings](../facts/ec2.md#ec2-managed-instance-delegated-control)
  link: [plus a separate fee for the service provider](../facts/ec2.md#ec2-managed-instance-delegated-control)
  say: a service provider runs the instance for you | you cannot change or terminate it yourself | normal instance price plus a provider fee
ec2-memory-scrubbed-on-stop-terminate
  claim: When you stop or terminate an instance, the hypervisor scrubs its memory (sets it to zero) before the memory is allocated to a new instance, and every block of storage is reset.
  scope: EC2 instance memory and storage; on stop or terminate.
  link: [scrubbed (set to zero) by the hypervisor](../facts/ec2.md#ec2-memory-scrubbed-on-stop-terminate)
  say: memory is wiped before reuse
ec2-metadata-user-data-not-protected
  claim: Instance metadata and user data can be accessed only from within the instance, but they are not protected by authentication or cryptographic methods, so you should not store sensitive data such as passwords or long-lived encryption keys as user data.
  scope: instance metadata and user data.
  link: [from within the instance itself](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  link: [not protected by authentication or cryptographic methods](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  link: [you should not store sensitive data](../facts/ec2.md#ec2-metadata-user-data-not-protected)
  say: only from inside the instance | but it is not protected | do not store secrets in user data
ec2-mission-critical-odcr-layer
  claim: For mission-critical systems, the decision guide adds On-Demand Capacity Reservations on top of the purchasing option for capacity assurance, combined with Savings Plans or Regional Reserved Instances to lower their cost.
  scope: mission-critical EC2 workloads.
  link: [provide assurance that the required resources are available](../facts/ec2.md#ec2-mission-critical-odcr-layer)
  say: Capacity Reservations make sure the capacity is there
ec2-multi-az-protects-from-location-failure
  claim: Launching EC2 instances in multiple Availability Zones protects your applications from the failure of a single location in the Region; if you distribute instances across Availability Zones and an instance fails, you can design your application so that an instance in another Availability Zone handles requests instead.
  scope: EC2 instances in a Region.
  link: [in multiple Availability Zones](../facts/ec2.md#ec2-multi-az-protects-from-location-failure)
  link: [the failure of a single location](../facts/ec2.md#ec2-multi-az-protects-from-location-failure)
  link: [an instance in another Availability Zone handles requests](../facts/ec2.md#ec2-multi-az-protects-from-location-failure)
  say: spread instances over several zones | to survive the loss of one location | another zone takes the requests
ec2-neighbour-batch-provisions-for-jobs
  claim: AWS Batch runs batch computing workloads of any scale as a fully managed service: it automatically provisions compute resources and optimizes the workload distribution, with no batch computing software to install or manage.
  scope: AWS Batch.
  link: [automatically provisions compute resources](../facts/ec2.md#ec2-neighbour-batch-provisions-for-jobs)
  say: Batch runs batch jobs and provisions the compute for you
ec2-neighbour-batch-runs-on-ec2-fargate
  claim: AWS Batch runs compute-intensive workloads on top of Amazon ECS and Amazon EKS, and can scale compute capacity on Amazon EC2 instances, Fargate resources and Amazon ECS Managed Instances.
  scope: AWS Batch.
  link: [Amazon EC2 instances, Fargate resources](../facts/ec2.md#ec2-neighbour-batch-runs-on-ec2-fargate)
  say: on EC2 instances or Fargate
ec2-neighbour-emr-analytics-frameworks
  claim: With Amazon EMR and its big data frameworks and related open-source projects, you can process data for analytics purposes and business intelligence workloads, and transform and move large amounts of data into and out of AWS data stores such as Amazon S3 and DynamoDB.
  scope: Amazon EMR.
  link: [analytics purposes and business intelligence workloads](../facts/ec2.md#ec2-neighbour-emr-analytics-frameworks)
  say: EMR runs big data frameworks for analytics
ec2-nested-virtualization-virtual-instances
  claim: Nested virtualization lets you run hypervisors such as Hyper-V and KVM inside virtual (non-bare metal) EC2 instances of supported types, at no additional cost; for performance-sensitive or latency-strict workloads that need hardware virtualization extensions, AWS recommends evaluating bare metal instances.
  scope: supported instance types; nested virtualization enabled on a supported type.
  link: [Virtual EC2 instances are non-bare metal instances.](../facts/ec2.md#ec2-nested-virtualization-virtual-instances)
  link: [no additional cost for using nested virtualization](../facts/ec2.md#ec2-nested-virtualization-virtual-instances)
  link: [to evaluate bare metal instances](../facts/ec2.md#ec2-nested-virtualization-virtual-instances)
  say: hypervisors can run inside normal virtual instances | there is no extra cost | for strict performance needs, consider bare metal
ec2-nitro-ena-and-nvme
  claim: Instances built on the AWS Nitro System use ENA for enhanced networking, and their storage volumes are exposed as NVMe block devices.
  scope: instances built on the AWS Nitro System.
  link: [use ENA for enhanced networking](../facts/ec2.md#ec2-nitro-ena-and-nvme)
  link: [exposed as NVMe block devices](../facts/ec2.md#ec2-nitro-ena-and-nvme)
  say: Nitro instances use ENA | volumes appear as NVMe devices
ec2-nitro-no-admin-access
  claim: The Nitro System offloads virtualization resources to dedicated hardware and software to minimize the attack surface, and its security model is locked down and prohibits administrative access.
  scope: AWS Nitro System.
  link: [minimizing the attack surface](../facts/ec2.md#ec2-nitro-no-admin-access)
  link: [prohibits administrative access](../facts/ec2.md#ec2-nitro-no-admin-access)
  say: virtualization moves to dedicated hardware | no administrative access to the host
ec2-nitro-shared-attachment-limit-28
  claim: Most Nitro instances support at most 28 attachments shared between EBS volumes, network interfaces and NVMe instance store volumes, so an m5.xlarge with only the primary network interface can attach 27 EBS volumes.
  scope: per instance; maximum; not adjustable; Nitro instance types with a shared volume limit; some newer types have a dedicated EBS volume limit that varies by size.
  link: [maximum of 28 attachments](../facts/ec2.md#ec2-nitro-shared-attachment-limit-28)
  link: [you can attach 27 EBS volumes](../facts/ec2.md#ec2-nitro-shared-attachment-limit-28)
  say: twenty-eight attachments on most Nitro instances | twenty-seven EBS volumes with one network interface
ec2-nitro-system-definition
  claim: The Nitro System is a collection of hardware and software components built by AWS that enable high performance, high availability and high security, and it provides bare metal capabilities that eliminate virtualization overhead.
  scope: the AWS Nitro System.
  link: [a collection of hardware and software components](../facts/ec2.md#ec2-nitro-system-definition)
  link: [high performance, high availability, and high security](../facts/ec2.md#ec2-nitro-system-definition)
  link: [eliminate virtualization overhead](../facts/ec2.md#ec2-nitro-system-definition)
  say: AWS-built hardware and software | for performance, availability and security | bare metal without virtualization overhead
ec2-odcr-future-dated-min-14-days
  claim: A future-dated Capacity Reservation has a minimum commitment duration of 14 days.
  scope: per future-dated On-Demand Capacity Reservation; minimum; not adjustable; only future-dated reservations; immediate reservations have no commitment.
  link: [14 days](../facts/ec2.md#ec2-odcr-future-dated-min-14-days)
  say: fourteen days
ec2-odcr-tied-to-one-az
  claim: An On-Demand Capacity Reservation is tied to one Availability Zone, so multi-AZ or disaster recovery designs create reservations in several Availability Zones.
  scope: per On-Demand Capacity Reservation.
  link: [tied to a specific Availability Zone](../facts/ec2.md#ec2-odcr-tied-to-one-az)
  say: each Capacity Reservation is in one Availability Zone
ec2-on-demand-billing-per-second-60s-minimum
  claim: On-Demand Instances are billed only for the seconds they are in the running state, with a 60-second minimum.
  scope: per On-Demand Instance; minimum.
  link: [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [You pay only for the seconds](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [are in the running state](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  say: a sixty-second minimum | only for the seconds the instance is running | while running
ec2-on-demand-p-quota-default-0
  claim: The Service Quotas default for Running On-Demand P instances is 0, and the quota is adjustable.
  scope: per account, per Region; measured in vCPUs; default; adjustable; P instance family.
  link: [Running On-Demand P instances | 0](../facts/ec2.md#ec2-on-demand-p-quota-default-0)
  say: a default of zero for P instances
ec2-on-demand-quota-any-combination-example
  claim: Any combination of instance types can be launched as long as the total vCPUs stay within the account quota; for example, a Standard quota of 256 vCPUs allows 32 m5.2xlarge instances or 16 c5.4xlarge instances.
  scope: per account, per Region.
  link: [256 vCPUs](../facts/ec2.md#ec2-on-demand-quota-any-combination-example)
  link: [any combination of instance types](../facts/ec2.md#ec2-on-demand-quota-any-combination-example)
  say: two hundred fifty-six vCPUs
ec2-on-demand-quota-auto-increase
  claim: Amazon EC2 automatically increases On-Demand Instance quotas based on usage, and you can also request a quota increase.
  scope: per account, per Region.
  link: [automatically increases your On-Demand Instance quotas](../facts/ec2.md#ec2-on-demand-quota-auto-increase)
  link: [request a quota increase if necessary](../facts/ec2.md#ec2-on-demand-quota-auto-increase)
  say: quotas increase automatically with usage
ec2-on-demand-quota-measured-in-vcpus
  claim: On-Demand Instance quotas apply per account per Region and are measured in the number of vCPUs that running On-Demand Instances use, regardless of instance type.
  scope: per account, per Region; maximum; adjustable; running On-Demand Instances.
  link: [number of virtual central processing units (vCPUs)](../facts/ec2.md#ec2-on-demand-quota-measured-in-vcpus)
  link: [per AWS account per Region](../facts/ec2.md#ec2-on-demand-quota-measured-in-vcpus)
  say: the number of vCPUs
ec2-on-demand-quota-states-not-counted
  claim: Instances in the pending, stopping, stopped and hibernated states do not count toward the On-Demand Instance quotas.
  scope: per account, per Region.
  link: [pending, stopping, stopped, and hibernated states](../facts/ec2.md#ec2-on-demand-quota-states-not-counted)
  link: [do not count towards your On-Demand Instance quotas](../facts/ec2.md#ec2-on-demand-quota-states-not-counted)
  say: pending, stopping, stopped and hibernated instances do not count | they do not count
ec2-on-demand-recommended-short-term-irregular
  claim: AWS recommends On-Demand Instances for applications with short-term, irregular workloads that cannot be interrupted.
  scope: On-Demand Instances.
  link: [short-term, irregular workloads that cannot be interrupted](../facts/ec2.md#ec2-on-demand-recommended-short-term-irregular)
  say: short-term, irregular work that must not be interrupted
ec2-on-demand-standard-quota-default-5
  claim: The Service Quotas default for Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances is 5, and the quota is adjustable; On-Demand Instance quotas are per AWS account per Region and are managed in vCPUs.
  scope: per account, per Region; measured in vCPUs; default; adjustable; Standard families A, C, D, H, I, M, R, T, Z.
  link: [Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances | 5](../facts/ec2.md#ec2-on-demand-standard-quota-default-5)
  say: a default of five for Standard instances
ec2-os-shutdown-instance-store-root-terminates
  claim: An operating system shutdown command always terminates an instance that has an instance store root volume; for an EBS root volume you can choose whether it stops or terminates.
  scope: instances with an instance store root volume; fixed.
  link: [always terminate an instance with an instance store](../facts/ec2.md#ec2-os-shutdown-instance-store-root-terminates)
  link: [whether operating system shutdown commands stop or terminate](../facts/ec2.md#ec2-os-shutdown-instance-store-root-terminates)
  say: an OS shutdown always terminates an instance store backed instance
ec2-per-second-billing-all-purchase-options
  claim: Amazon EC2 usage is billed in one-second increments with a minimum of 60 seconds, and per-second billing applies to all purchase options.
  scope: per instance, all purchase options; minimum; the EC2 pricing page lists per-second billing for Amazon Linux, Windows, Red Hat Enterprise Linux, Ubuntu and Ubuntu Pro instances.
  link: [one-second increments](../facts/ec2.md#ec2-per-second-billing-all-purchase-options)
  link: [minimum of 60 seconds](../facts/ec2.md#ec2-per-second-billing-all-purchase-options)
  link: [applies to all purchase options](../facts/ec2.md#ec2-per-second-billing-all-purchase-options)
  say: one-second increments | a minimum of sixty seconds
ec2-per-second-billing-irregular-workloads
  claim: Per-second billing removes the cost of unused compute time from the bill, which particularly helps workloads that run over irregular time periods.
  scope: EC2 per-second billing.
  link: [workloads that run over irregular time periods](../facts/ec2.md#ec2-per-second-billing-irregular-workloads)
  say: workloads that run at irregular times
ec2-placement-change-requires-stopped
  claim: Before you can change the placement group of an instance, the instance must be in the stopped state.
  scope: changing the placement group of an instance.
  link: [the instance must be in the `stopped` state](../facts/ec2.md#ec2-placement-change-requires-stopped)
  link: [change the placement group for an instance](../facts/ec2.md#ec2-placement-change-requires-stopped)
  say: stop the instance first | to change its placement group
ec2-placement-cluster-can-span-peered-vpcs
  claim: A cluster placement group is a logical grouping of instances within a single Availability Zone; instances are not isolated to a single rack, and the group can span peered VPCs in the same Region.
  scope: cluster placement groups; peered VPCs in the same Region.
  link: [within a single Availability Zone](../facts/ec2.md#ec2-placement-cluster-can-span-peered-vpcs)
  link: [can span peered virtual private networks (VPCs)](../facts/ec2.md#ec2-placement-cluster-can-span-peered-vpcs)
  say: one Availability Zone | it can span peered VPCs in the same Region
ec2-placement-cluster-capacity-error-stop-start-all
  claim: If a launch into a cluster placement group that already has running instances fails with a capacity error, stop and start all instances in the group and try again; starting them might move them to hardware with capacity for all requested instances.
  scope: cluster placement groups; the group already has running instances.
  link: [stop and start all of the instances](../facts/ec2.md#ec2-placement-cluster-capacity-error-stop-start-all)
  link: [try the launch again](../facts/ec2.md#ec2-placement-cluster-capacity-error-stop-start-all)
  say: stop and start every instance in the group | then try the launch again
ec2-placement-cluster-internet-dx-5-gbps
  claim: For cluster placement groups, network traffic to the internet and over a Direct Connect connection to on-premises resources is limited to 5 Gbps.
  scope: network traffic of cluster placement groups to the internet or over Direct Connect to on-premises resources; maximum; not adjustable.
  link: [limited to 5 Gbps](../facts/ec2.md#ec2-placement-cluster-internet-dx-5-gbps)
  say: five gigabits per second
ec2-placement-cluster-one-request-one-type
  claim: For a cluster placement group, AWS recommends launching all needed instances in a single launch request and using one instance type; adding instances later or mixing instance types increases the chance of an insufficient capacity error.
  scope: cluster placement groups.
  link: [Use a single launch request](../facts/ec2.md#ec2-placement-cluster-one-request-one-type)
  link: [Use the same instance type](../facts/ec2.md#ec2-placement-cluster-one-request-one-type)
  link: [getting an insufficient capacity error](../facts/ec2.md#ec2-placement-cluster-one-request-one-type)
  say: launch them all in one request | use one instance type | otherwise you risk a capacity error
ec2-placement-cluster-recommended-traffic-between-instances
  claim: Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput or both, and when most network traffic is between the instances in the group.
  scope: cluster placement groups.
  link: [low network latency, high network throughput, or both](../facts/ec2.md#ec2-placement-cluster-recommended-traffic-between-instances)
  link: [between the instances in the group](../facts/ec2.md#ec2-placement-cluster-recommended-traffic-between-instances)
  say: low latency and high throughput | when traffic is mostly between the instances
ec2-placement-cluster-single-az
  claim: A cluster placement group is a logical grouping of instances within a single Availability Zone and can't span multiple Availability Zones, but it can span peered VPCs in the same Region.
  scope: per cluster placement group; it can span peered VPCs in the same Region.
  link: [can't span multiple Availability Zones](../facts/ec2.md#ec2-placement-cluster-single-az)
  link: [within a single Availability Zone](../facts/ec2.md#ec2-placement-cluster-single-az)
  say: a cluster group stays in one Availability Zone | inside one Availability Zone
ec2-placement-cluster-single-flow-10-gbps
  claim: With enhanced networking, instances in a cluster placement group can use up to 10 Gbps for single-flow traffic, while instances outside a cluster placement group can use up to 5 Gbps.
  scope: per flow, per instance; maximum; not adjustable; instances enabled for enhanced networking.
  link: [up to 10 Gbps for single-flow traffic](../facts/ec2.md#ec2-placement-cluster-single-flow-10-gbps)
  link: [up to 5 Gbps](../facts/ec2.md#ec2-placement-cluster-single-flow-10-gbps)
  say: ten gigabits per second per flow inside the group | five gigabits per second per flow outside a cluster group
ec2-placement-group-no-charge
  claim: There is no charge for creating a placement group.
  scope: per placement group.
  link: [no charge for creating a placement group](../facts/ec2.md#ec2-placement-group-no-charge)
  say: placement groups are free to create
ec2-placement-groups-quota-500-per-region
  claim: You can create at most 500 placement groups per Region.
  scope: per account, per Region; maximum; not adjustable; stated as a limitation on the create page; the page names no increase process.
  link: [500 placement groups per Region](../facts/ec2.md#ec2-placement-groups-quota-500-per-region)
  say: five hundred placement groups per Region
ec2-placement-no-dedicated-hosts-or-stop-spot
  claim: Dedicated Hosts cannot be launched in placement groups, and a Spot Instance configured to stop or hibernate on interruption cannot be launched in a placement group.
  scope: per placement group.
  link: [You can't launch Dedicated Hosts in placement groups.](../facts/ec2.md#ec2-placement-no-dedicated-hosts-or-stop-spot)
  link: [configured to stop or hibernate on interruption](../facts/ec2.md#ec2-placement-no-dedicated-hosts-or-stop-spot)
  say: no Dedicated Hosts in placement groups | no stop-or-hibernate Spot Instances in placement groups
ec2-placement-one-group-per-instance
  claim: An instance can be in only one placement group at a time, and placement groups cannot be merged.
  scope: per instance.
  link: [one placement group at a time](../facts/ec2.md#ec2-placement-one-group-per-instance)
  link: [You can't merge placement groups.](../facts/ec2.md#ec2-placement-one-group-per-instance)
  say: one placement group at a time | placement groups cannot be merged
ec2-placement-optional-default-spread-out
  claim: Placement groups are optional; without one, EC2 tries to spread your instances out across the underlying hardware to minimize correlated failures.
  scope: instances launched without a placement group; default; adjustable.
  link: [Placement groups are optional](../facts/ec2.md#ec2-placement-optional-default-spread-out)
  link: [spread out across the underlying hardware](../facts/ec2.md#ec2-placement-optional-default-spread-out)
  say: a placement group is optional | by default EC2 spreads instances out
ec2-placement-partition-dedicated-max-2
  claim: A partition placement group with Dedicated Instances can have at most 2 partitions.
  scope: per partition placement group; maximum; not adjustable; the group uses Dedicated Instances.
  link: [maximum of two partitions](../facts/ec2.md#ec2-placement-partition-dedicated-max-2)
  say: two partitions at most
ec2-placement-partition-distributed-workloads
  claim: Partition placement groups can be used to deploy large distributed and replicated workloads, such as HDFS, HBase and Cassandra, across distinct racks.
  scope: partition placement groups.
  link: [large distributed and replicated workloads](../facts/ec2.md#ec2-placement-partition-distributed-workloads)
  link: [such as HDFS, HBase, and Cassandra](../facts/ec2.md#ec2-placement-partition-distributed-workloads)
  say: big distributed and replicated systems | for example HDFS, HBase and Cassandra
ec2-placement-partition-max-7-per-az
  claim: A partition placement group supports at most 7 partitions per Availability Zone, and the number of instances in it is limited only by the account limits.
  scope: per partition placement group, per Availability Zone; maximum; not adjustable; partitions can be in several Availability Zones of the same Region.
  link: [maximum of seven partitions per Availability Zone](../facts/ec2.md#ec2-placement-partition-max-7-per-az)
  link: [limited only by your account limits](../facts/ec2.md#ec2-placement-partition-max-7-per-az)
  say: up to seven partitions per Availability Zone | instance count limited only by account limits
ec2-placement-partition-multi-az-visibility
  claim: A partition placement group can have partitions in multiple Availability Zones of the same Region, and it offers visibility into the partitions, so you can see which instances are in which partitions and share this information with topology-aware applications such as HDFS, HBase and Cassandra.
  scope: partition placement groups.
  link: [partitions in multiple Availability Zones](../facts/ec2.md#ec2-placement-partition-multi-az-visibility)
  link: [visibility into the partitions](../facts/ec2.md#ec2-placement-partition-multi-az-visibility)
  say: partitions can be in several zones of one Region | you can see which instance is in which partition
ec2-placement-partition-separate-racks
  claim: In a partition placement group, each partition has its own set of racks with its own network and power source, and no two partitions share racks, which isolates the impact of a hardware failure within your application.
  scope: partition placement groups.
  link: [has its own set of racks](../facts/ec2.md#ec2-placement-partition-separate-racks)
  link: [share the same racks](../facts/ec2.md#ec2-placement-partition-separate-racks)
  link: [isolate the impact of hardware failure](../facts/ec2.md#ec2-placement-partition-separate-racks)
  say: each partition has its own racks | partitions never share racks | a hardware failure stays in one partition
ec2-placement-precision-time-group
  claim: A precision time placement group places instances on supported hardware with direct access to high-precision time sources and is recommended for applications that need microsecond-accurate clock synchronization; it has no additional charge, and a launch fails when there is not enough such hardware.
  scope: precision time placement group; supported instance families.
  link: [direct access to high-precision time sources](../facts/ec2.md#ec2-placement-precision-time-group)
  link: [require microsecond-accurate clock synchronization](../facts/ec2.md#ec2-placement-precision-time-group)
  link: [There is no additional charge](../facts/ec2.md#ec2-placement-precision-time-group)
  say: it gives instances high-precision time | for microsecond-accurate clocks | there is no extra charge
ec2-placement-spread-critical-instances
  claim: A spread placement group places each instance on distinct hardware; it is recommended for a small number of critical instances that should be kept separate, and it reduces the risk of simultaneous failures.
  scope: spread placement groups.
  link: [each placed on distinct hardware](../facts/ec2.md#ec2-placement-spread-critical-instances)
  link: [a small number of critical instances](../facts/ec2.md#ec2-placement-spread-critical-instances)
  link: [reduces the risk of simultaneous failures](../facts/ec2.md#ec2-placement-spread-critical-instances)
  say: every instance on different hardware | for a few critical instances | so they do not fail together
ec2-placement-spread-max-7-running-per-az
  claim: A rack-level spread placement group can span several Availability Zones in one Region but supports at most 7 running instances in each Availability Zone, so a Region with 3 Availability Zones allows 21 instances in one group.
  scope: per rack-level spread placement group, per Availability Zone; maximum; not adjustable; in AWS Regions; on AWS Outposts the limit is the number of racks or hosts.
  link: [seven running instances in each Availability Zone](../facts/ec2.md#ec2-placement-spread-max-7-running-per-az)
  link: [21 instances](../facts/ec2.md#ec2-placement-spread-max-7-running-per-az)
  say: seven running instances per Availability Zone | twenty-one instances across three Availability Zones
ec2-placement-spread-more-than-7-use-multiple-groups
  claim: When more than 7 instances are needed in one Availability Zone, AWS recommends using multiple spread placement groups; this does not guarantee spread across groups, only within each group.
  scope: per Availability Zone; rack-level spread placement groups.
  link: [use multiple spread placement groups](../facts/ec2.md#ec2-placement-spread-more-than-7-use-multiple-groups)
  say: use several spread placement groups
ec2-placement-spread-no-dedicated-instances
  claim: Spread placement groups are not supported for Dedicated Instances.
  scope: per spread placement group.
  link: [not supported for Dedicated Instances](../facts/ec2.md#ec2-placement-spread-no-dedicated-instances)
  say: spread groups do not support Dedicated Instances
ec2-private-subnet-for-non-internet-instances
  claim: Use private subnets for instances that should not be accessed directly from the internet.
  scope: EC2 network isolation.
  link: [Use private subnets for your instances](../facts/ec2.md#ec2-private-subnet-for-non-internet-instances)
  say: put it in a private subnet
ec2-public-ami-quota-5-per-region
  claim: An account can have at most 5 public AMIs per Region by default, including public AMIs in the Recycle Bin.
  scope: per account, per Region; default; adjustable; public AMIs, including those in the Recycle Bin.
  link: [5 public AMIs](../facts/ec2.md#ec2-public-ami-quota-5-per-region)
  say: five public AMIs per Region
ec2-purchasing-option-guidance
  claim: The guide's rule of thumb: Savings Plans when you can commit to a usage amount but not to an instance configuration; Reserved Instances or Capacity Reservations for a specific Availability Zone when you need a capacity reservation; Capacity Blocks to reserve a cluster of GPU instances; Spot Instances when you are flexible about timing and can be interrupted; Dedicated Hosts or Dedicated Instances for compliance and server-bound licenses.
  scope: Amazon EC2 purchasing options.
  link: [commit to a usage amount, purchase Savings Plans](../facts/ec2.md#ec2-purchasing-option-guidance)
  link: [purchase Reserved Instances or Capacity Reservations](../facts/ec2.md#ec2-purchasing-option-guidance)
  link: [reserve a cluster of GPU instances](../facts/ec2.md#ec2-purchasing-option-guidance)
  link: [flexible about when your applications run](../facts/ec2.md#ec2-purchasing-option-guidance)
  link: [help you address compliance requirements](../facts/ec2.md#ec2-purchasing-option-guidance)
ec2-purchasing-options-list
  claim: The EC2 guide lists these billing and purchasing options: On-Demand Instances (pay by the second), Savings Plans (commit to a usage amount in USD per hour for 1 or 3 years), Reserved Instances (commit to an instance configuration for 1 or 3 years), Spot Instances (unused capacity), Dedicated Hosts (a physical host for your instances and licenses), Dedicated Instances (single-tenant hardware, billed by the hour) and Capacity Reservations (reserve capacity in a specific Availability Zone).
  scope: Amazon EC2 purchasing options.
  link: [Pay, by the second](../facts/ec2.md#ec2-purchasing-options-list)
  link: [a commitment to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years](../facts/ec2.md#ec2-purchasing-options-list)
  link: [a commitment to a consistent instance configuration, including instance type and Region, for a term of 1 or 3 years](../facts/ec2.md#ec2-purchasing-options-list)
  link: [Request unused EC2 instances](../facts/ec2.md#ec2-purchasing-options-list)
  link: [a physical host that is fully dedicated](../facts/ec2.md#ec2-purchasing-options-list)
  link: [instances that run on single-tenant hardware](../facts/ec2.md#ec2-purchasing-options-list)
  link: [Reserve capacity for your EC2 instances in a specific Availability Zone](../facts/ec2.md#ec2-purchasing-options-list)
ec2-purchasing-vs-capacity-reservation-independent
  claim: Purchasing options (On-Demand, Savings Plans, Reserved Instances, Spot) decide how the compute bill is calculated, while Capacity Reservations (On-Demand Capacity Reservations and Capacity Blocks for ML) decide whether capacity is held for you, whether or not you use it.
  scope: EC2 purchasing options and Capacity Reservations.
  link: [determine how AWS calculates your bill](../facts/ec2.md#ec2-purchasing-vs-capacity-reservation-independent)
  link: [determine whether capacity is held for you](../facts/ec2.md#ec2-purchasing-vs-capacity-reservation-independent)
  say: purchasing options decide the bill | capacity reservations decide whether capacity is held for you
ec2-reboot-same-host-keeps-data
  claim: A reboot is the same as rebooting the operating system: the instance stays on the same host computer and keeps its public DNS name, private IP address and any data on its instance store volumes.
  scope: instance reboot.
  link: [The instance remains on the same host computer](../facts/ec2.md#ec2-reboot-same-host-keeps-data)
  link: [any data on its instance store volumes](../facts/ec2.md#ec2-reboot-same-host-keeps-data)
  link: [equivalent to rebooting an operating system](../facts/ec2.md#ec2-reboot-same-host-keeps-data)
  say: a reboot keeps the instance on the same host
ec2-recovery-keeps-id-ips-metadata
  claim: A recovered instance is identical to the original instance, including the instance ID, private IP addresses, Elastic IP addresses and all instance metadata; a public IP address is also retained after recovery.
  scope: a recovered instance.
  link: [including the instance ID](../facts/ec2.md#ec2-recovery-keeps-id-ips-metadata)
  link: [private IP addresses, Elastic IP addresses](../facts/ec2.md#ec2-recovery-keeps-id-ips-metadata)
  link: [retains the public IP address after recovery](../facts/ec2.md#ec2-recovery-keeps-id-ips-metadata)
  link: [all instance metadata](../facts/ec2.md#ec2-recovery-keeps-id-ips-metadata)
  say: it keeps the same instance ID | it keeps its private and Elastic IP addresses | it keeps its public IP address | and all its instance metadata
ec2-recovery-loses-ram-and-cw-instance-store
  claim: When AWS recovers an instance, data in volatile memory (RAM) is lost and operating system uptime starts over; with CloudWatch action based recovery, data on instance store volumes is also lost.
  scope: an instance recovered by AWS; instance store loss applies to CloudWatch action based recovery.
  link: [volatile memory (RAM) will be lost](../facts/ec2.md#ec2-recovery-loses-ram-and-cw-instance-store)
  link: [instance store volumes will also be lost](../facts/ec2.md#ec2-recovery-loses-ram-and-cw-instance-store)
  say: memory contents are lost | with CloudWatch recovery, instance store data is lost too
ec2-recovery-simplified-enabled-by-default
  claim: Simplified automatic recovery is enabled by default when an instance is launched; CloudWatch action based recovery is optional and you configure it after launch. A recovery mechanism must be configured before a system status check fails.
  scope: per instance; default; adjustable; supported instances only.
  link: [simplified automatic recovery is enabled during instance launch](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  link: [optionally configure Amazon CloudWatch action based recovery](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  link: [configured in advance](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  say: simplified automatic recovery is on by default | CloudWatch action based recovery is optional | set it up before a failure
ec2-recovery-simplified-excludes-metal
  claim: Simplified automatic recovery excludes metal instance sizes, while CloudWatch action based recovery includes them.
  scope: automatic instance recovery mechanisms; metal instance sizes.
  link: [Excluded](../facts/ec2.md#ec2-recovery-simplified-excludes-metal)
  link: [Included](../facts/ec2.md#ec2-recovery-simplified-excludes-metal)
  say: simplified recovery excludes metal sizes | CloudWatch action based recovery includes them
ec2-recovery-simplified-not-instance-store
  claim: Simplified automatic recovery is not supported for instances that attach instance store volumes at launch; CloudWatch action based recovery supports them on selected instance types, and the instance store data is lost during recovery.
  scope: automatic instance recovery mechanisms; instance store volumes attached at launch.
  link: [Not supported for instances that attach instance store](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  link: [Supported on selected instance types](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  link: [data on instance store volumes is lost](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  say: simplified recovery does not support instance store instances | CloudWatch recovery supports some of them | but the instance store data is lost
ec2-recovery-system-status-check-only
  claim: Automatic instance recovery recovers an instance that fails a system status check (a host hardware or software problem); it does not operate when only the instance status check fails.
  scope: automatic instance recovery.
  link: [fails a system status check](../facts/ec2.md#ec2-recovery-system-status-check-only)
  link: [if only the instance status check fails](../facts/ec2.md#ec2-recovery-system-status-check-only)
  say: it recovers after a failed system status check | not when only the instance status check fails
ec2-regions-isolated-not-replicated
  claim: Regions are isolated from each other and AWS doesn't automatically replicate resources across Regions, so you see only the resources tied to the Region you specify.
  scope: EC2 resources in AWS Regions.
  link: [Regions are isolated from each other](../facts/ec2.md#ec2-regions-isolated-not-replicated)
  link: [we don't automatically replicate resources across Regions](../facts/ec2.md#ec2-regions-isolated-not-replicated)
  say: Regions are isolated | nothing is copied between Regions for you
ec2-reserved-instances-older-option-savings-plans-recommended
  claim: AWS describes Reserved Instances as an older purchasing option that it generally recommends replacing with Savings Plans, and newer EC2 instance families might not support Reserved Instance pricing.
  scope: per purchasing decision.
  link: [generally recommend replacing with Savings Plans](../facts/ec2.md#ec2-reserved-instances-older-option-savings-plans-recommended)
  link: [might not support Reserved Instance pricing](../facts/ec2.md#ec2-reserved-instances-older-option-savings-plans-recommended)
  say: AWS now points to Savings Plans first | new families may have no Reserved Instance pricing
ec2-resize-change-instance-type
  claim: If an EC2 instance is too big or too small for its workload, you can resize it by changing its instance type, and AWS Compute Optimizer can recommend the instance type best able to handle the workload.
  scope: EC2 instance resizing; the new type must be compatible with the current configuration.
  link: [resize your instance by changing its instance type](../facts/ec2.md#ec2-resize-change-instance-type)
  link: [you can use AWS Compute Optimizer](../facts/ec2.md#ec2-resize-change-instance-type)
  say: change the instance type | Compute Optimizer suggests the type
ec2-resize-instance-store-root-migrate
  claim: For an instance with an instance store root volume, the instance type change table gives the compatibility as not applicable and says to migrate to a new instance type.
  scope: an instance with an instance store root volume.
  link: [Not applicable](../facts/ec2.md#ec2-resize-instance-store-root-migrate)
  link: [Migrate to a new instance type](../facts/ec2.md#ec2-resize-instance-store-root-migrate)
  say: compatibility is not applicable | you migrate to a new instance type
ec2-resize-moves-hardware-new-public-ipv4
  claim: When you stop and start an instance to change its type, EC2 moves it to new hardware; a public IPv4 address that is not an Elastic IP address is released and the instance gets a new public IPv4 address.
  scope: an instance that is stopped and started; the public IPv4 address is not an Elastic IP address.
  link: [we move the instance to new hardware](../facts/ec2.md#ec2-resize-moves-hardware-new-public-ipv4)
  link: [a new public IPv4 address](../facts/ec2.md#ec2-resize-moves-hardware-new-public-ipv4)
  say: the instance moves to new hardware | it gets a new public IP address unless it has an Elastic IP
ec2-resize-must-stop-instance
  claim: You must stop an EBS-backed instance before you can change its instance type, so you plan for downtime while it is stopped.
  scope: an Amazon EBS-backed instance; the new instance type is compatible with the current configuration.
  link: [You must stop your instance](../facts/ec2.md#ec2-resize-must-stop-instance)
  link: [before you can change its instance type](../facts/ec2.md#ec2-resize-must-stop-instance)
  link: [plan for downtime](../facts/ec2.md#ec2-resize-must-stop-instance)
  say: you must stop the instance first | before you change its instance type | plan for downtime
ec2-resize-requires-compatible-configuration
  claim: You can change the instance type only if the instance's current configuration is compatible with the new type; otherwise you launch a new compatible instance and migrate your application to it.
  scope: changing the instance type of an instance.
  link: [only if the instance's current configuration is compatible](../facts/ec2.md#ec2-resize-requires-compatible-configuration)
  link: [migrate your application to the new instance](../facts/ec2.md#ec2-resize-requires-compatible-configuration)
  say: only when the configuration is compatible | otherwise launch a new instance and migrate
ec2-resize-same-processor-architecture
  claim: Because AMIs are specific to the processor architecture, a resized instance must use an instance type with the same processor architecture as the current one.
  scope: changing the instance type of an instance.
  link: [the same processor architecture](../facts/ec2.md#ec2-resize-same-processor-architecture)
  link: [AMIs are specific to the architecture](../facts/ec2.md#ec2-resize-same-processor-architecture)
  say: the same processor architecture | an AMI is built for one processor architecture
ec2-retirement-ebs-stop-instance-store-terminate
  claim: When AWS detects irreparable failure of the underlying host, it schedules the instance to stop if it has an EBS root volume, or to terminate if it has an instance store root volume.
  scope: scheduled instance retirement; depends on the root volume type.
  link: [irreparable failure of the underlying host](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  link: [the instance is scheduled to stop](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  link: [the instance is scheduled to terminate](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  say: when the host fails for good | an EBS root instance is stopped | an instance store root instance is terminated
ec2-ri-az-flexibility
  claim: A regional Reserved Instance discount applies to instance usage in any Availability Zone of the Region; a zonal Reserved Instance discount applies only in the specified Availability Zone.
  scope: Reserved Instance scope.
  link: [in any Availability Zone in the specified Region](../facts/ec2.md#ec2-ri-az-flexibility)
  link: [No Availability Zone flexibility](../facts/ec2.md#ec2-ri-az-flexibility)
  say: a regional Reserved Instance covers any Availability Zone in the Region
ec2-ri-capacity-reservation-zonal-only
  claim: A regional Reserved Instance does not reserve capacity; a zonal Reserved Instance reserves capacity in the specified Availability Zone.
  scope: Reserved Instance scope.
  link: [A regional Reserved Instance does not reserve capacity](../facts/ec2.md#ec2-ri-capacity-reservation-zonal-only)
  link: [A zonal Reserved Instance reserves capacity](../facts/ec2.md#ec2-ri-capacity-reservation-zonal-only)
  say: a regional Reserved Instance does not reserve capacity | a zonal Reserved Instance reserves capacity in its Availability Zone
ec2-ri-convertible-exchange-standard-not
  claim: A Standard Reserved Instance can't be exchanged; a Convertible Reserved Instance can be exchanged during the term for another Convertible Reserved Instance with new attributes, including instance family, instance type, platform, scope, or tenancy.
  scope: EC2 Reserved Instances, Standard and Convertible offering classes.
  link: [Can't be exchanged.](../facts/ec2.md#ec2-ri-convertible-exchange-standard-not)
  link: [Can be exchanged during the term](../facts/ec2.md#ec2-ri-convertible-exchange-standard-not)
  say: a Standard Reserved Instance cannot be exchanged | a Convertible Reserved Instance can be exchanged during the term
ec2-ri-four-pricing-attributes
  claim: A Reserved Instance has four instance attributes that determine its price: instance type, Region, tenancy and platform.
  scope: per Reserved Instance.
  link: [four instance attributes that determine its price](../facts/ec2.md#ec2-ri-four-pricing-attributes)
  say: four attributes: instance type, Region, tenancy and platform
ec2-ri-instance-size-flexibility-regional-only
  claim: Instance size flexibility is supported only for regional Reserved Instances; it is not supported for zonal Reserved Instances, for Windows, RHEL and SUSE Reserved Instances, or for Reserved Instances with dedicated tenancy.
  scope: Reserved Instance size flexibility.
  link: [only supported for Regional Reserved Instances](../facts/ec2.md#ec2-ri-instance-size-flexibility-regional-only)
  link: [Linux/Unix Reserved Instances with default tenancy](../facts/ec2.md#ec2-ri-instance-size-flexibility-regional-only)
  link: [zonal Reserved Instances](../facts/ec2.md#ec2-ri-instance-size-flexibility-regional-only)
  say: only regional Reserved Instances have instance size flexibility
ec2-ri-is-billing-discount-not-instance
  claim: A Reserved Instance is not a physical instance but a billing discount applied to running On-Demand Instances in your account that match its specifications; a matching running instance gets the discount immediately and automatically, without a restart.
  scope: Reserved Instances.
  link: [Reserved Instances are not physical instances](../facts/ec2.md#ec2-ri-is-billing-discount-not-instance)
  link: [the billing discount is applied immediately and automatically](../facts/ec2.md#ec2-ri-is-billing-discount-not-instance)
  link: [You do not have to restart your instances](../facts/ec2.md#ec2-ri-is-billing-discount-not-instance)
  say: a Reserved Instance is a billing discount, not a separate instance
ec2-ri-marketplace-minimum-term-and-age
  claim: To sell a Reserved Instance in the Marketplace it must have at least one month remaining in its term and must have been active in the account for at least 30 days; the minimum listing price is $0.00.
  scope: Reserved Instance Marketplace; minimum; Standard Reserved Instances; an upfront payment must have been received by AWS.
  link: [at least one month remaining in the term](../facts/ec2.md#ec2-ri-marketplace-minimum-term-and-age)
  link: [active in your account for at least 30 days](../facts/ec2.md#ec2-ri-marketplace-minimum-term-and-age)
  link: [The minimum price allowed in the Reserved Instance Marketplace is $0.00](../facts/ec2.md#ec2-ri-marketplace-minimum-term-and-age)
  say: at least one month left | owned for at least thirty days
ec2-ri-marketplace-service-fee-12-percent
  claim: AWS charges a service fee of 12 percent of the total upfront price of each Standard Reserved Instance sold in the Reserved Instance Marketplace.
  scope: per Reserved Instance sold; fixed.
  link: [12 percent of the total upfront price](../facts/ec2.md#ec2-ri-marketplace-service-fee-12-percent)
  say: twelve percent of the upfront price
ec2-ri-marketplace-sold-then-on-demand
  claim: After a Reserved Instance is sold you give up its capacity reservation and discounted fees, and any instance you keep running is charged the On-Demand price from the time of the sale.
  scope: per Reserved Instance sold.
  link: [AWS charges you the On-Demand price](../facts/ec2.md#ec2-ri-marketplace-sold-then-on-demand)
  say: On-Demand price from the moment of sale
ec2-ri-marketplace-standard-only
  claim: Only Standard regional and zonal EC2 Reserved Instances can be sold in the Reserved Instance Marketplace; Convertible Reserved Instances cannot be sold.
  scope: Reserved Instance Marketplace.
  link: [Only Amazon EC2 Standard regional and zonal Reserved Instances can be sold](../facts/ec2.md#ec2-ri-marketplace-standard-only)
  link: [Convertible Reserved Instances can't be sold](../facts/ec2.md#ec2-ri-marketplace-standard-only)
  say: only Standard Reserved Instances | Convertible cannot be sold
ec2-ri-no-automatic-renewal
  claim: Reserved Instances do not renew automatically; when one expires the instance keeps running without interruption but is charged On-Demand rates.
  scope: per Reserved Instance.
  link: [do not renew automatically](../facts/ec2.md#ec2-ri-no-automatic-renewal)
  link: [charged On-Demand rates](../facts/ec2.md#ec2-ri-no-automatic-renewal)
  say: they do not renew automatically | you pay On-Demand rates
ec2-ri-no-upfront-needs-billing-history
  claim: A successful billing history is required before an account can purchase No Upfront Reserved Instances.
  scope: per account; No Upfront payment option.
  link: [a successful billing history is required](../facts/ec2.md#ec2-ri-no-upfront-needs-billing-history)
  say: a successful billing history
ec2-ri-payment-options
  claim: Reserved Instances offer the payment options All Upfront, Partial Upfront and No Upfront; in general a higher upfront payment saves more money.
  scope: per Reserved Instance.
  link: [All Upfront](../facts/ec2.md#ec2-ri-payment-options)
  link: [Partial Upfront](../facts/ec2.md#ec2-ri-payment-options)
  link: [No Upfront](../facts/ec2.md#ec2-ri-payment-options)
  link: [save more money making a higher upfront payment](../facts/ec2.md#ec2-ri-payment-options)
  say: a higher upfront payment saves more
ec2-ri-purchase-cannot-be-cancelled
  claim: A Reserved Instance purchase cannot be cancelled; depending on the offering class it may be modified, exchanged or sold instead.
  scope: per Reserved Instance.
  link: [cannot cancel your purchase](../facts/ec2.md#ec2-ri-purchase-cannot-be-cancelled)
  say: you cannot cancel the purchase
ec2-ri-purchase-quota-80-per-month-example
  claim: In a Region with three Availability Zones the default quota is 80 new Reserved Instances per month (regional plus zonal); a purchase with an instance count of 10 counts as 10, not 1.
  scope: per account, per Region, per month; default; adjustable; a Region with three Availability Zones.
  link: [80 new Reserved Instances per month](../facts/ec2.md#ec2-ri-purchase-quota-80-per-month-example)
  link: [counts towards your quota as 10, not 1](../facts/ec2.md#ec2-ri-purchase-quota-80-per-month-example)
  say: eighty new Reserved Instances per month
ec2-ri-quota-new-regional-per-month
  claim: The default quota for new regional Reserved Instances is 20 per Region per month.
  scope: per account, per Region, per month; default; adjustable; regional Reserved Instances.
  link: [20 per Region per month](../facts/ec2.md#ec2-ri-quota-new-regional-per-month)
  say: twenty per Region per month
ec2-ri-quota-new-zonal-per-month
  claim: The default quota for new zonal Reserved Instances is 20 per Availability Zone per month.
  scope: per account, per Availability Zone, per month; default; adjustable; zonal Reserved Instances.
  link: [20 per Availability Zone per month](../facts/ec2.md#ec2-ri-quota-new-zonal-per-month)
  say: twenty per Availability Zone per month
ec2-ri-scope-regional-or-zonal
  claim: When you buy a Reserved Instance you choose its scope, regional or zonal; the scope does not change the price.
  scope: per Reserved Instance.
  link: [The scope is either regional or zonal](../facts/ec2.md#ec2-ri-scope-regional-or-zonal)
  link: [The scope does not affect the price](../facts/ec2.md#ec2-ri-scope-regional-or-zonal)
  say: a Reserved Instance is either regional or zonal
ec2-ri-shared-across-consolidated-billing
  claim: Reserved Instance pricing benefits are shared across accounts billed under one consolidated billing payer account: they apply first to usage in the purchasing account, then to qualifying usage in any other account in the organization.
  scope: Reserved Instances in an organization with consolidated billing; the purchasing account is part of the consolidated billing family.
  link: [The pricing benefits of Reserved Instances are shared](../facts/ec2.md#ec2-ri-shared-across-consolidated-billing)
  link: [first applied to usage within the purchasing account](../facts/ec2.md#ec2-ri-shared-across-consolidated-billing)
  link: [any other account in the organization](../facts/ec2.md#ec2-ri-shared-across-consolidated-billing)
  say: RI discounts are shared in the organization | first in the buying account | then in other accounts
ec2-ri-size-flexibility-normalization-factor
  claim: Instance size flexibility uses the normalization factor of the instance size: the discount applies fully or partially to running instances of the same family in any Availability Zone of the Region, and only the instance family, tenancy and platform must match.
  scope: regional Reserved Instances.
  link: [the normalization factor of the instance size](../facts/ec2.md#ec2-ri-size-flexibility-normalization-factor)
  link: [instance family, tenancy, and platform](../facts/ec2.md#ec2-ri-size-flexibility-normalization-factor)
  say: the discount is spread by normalization factor across sizes in the family
ec2-ri-standard-biggest-discount-modify-only
  claim: Standard Reserved Instances give the most significant discount but can only be modified, not exchanged; Convertible Reserved Instances give a lower discount but can be exchanged for another Convertible Reserved Instance with different attributes, and can also be modified.
  scope: per Reserved Instance offering class.
  link: [the most significant discount](../facts/ec2.md#ec2-ri-standard-biggest-discount-modify-only)
  link: [Standard Reserved Instances can't be exchanged](../facts/ec2.md#ec2-ri-standard-biggest-discount-modify-only)
  link: [a lower discount than Standard Reserved Instances](../facts/ec2.md#ec2-ri-standard-biggest-discount-modify-only)
  link: [can be exchanged for another Convertible Reserved Instance](../facts/ec2.md#ec2-ri-standard-biggest-discount-modify-only)
  say: Standard: biggest discount, modify only | Convertible: lower discount, can be exchanged | Convertible can be exchanged
ec2-ri-term-one-or-three-years
  claim: A Reserved Instance is bought for a one-year or a three-year commitment, and the three-year commitment gives the bigger discount.
  scope: per Reserved Instance; fixed.
  link: [one-year or three-year commitment](../facts/ec2.md#ec2-ri-term-one-or-three-years)
  link: [three-year commitment offering a bigger discount](../facts/ec2.md#ec2-ri-term-one-or-three-years)
  say: a one-year or three-year commitment | three years gives the bigger discount
ec2-ri-year-defined-in-seconds
  claim: For Reserved Instances a year is defined as 31536000 seconds (365 days) and three years as 94608000 seconds (1095 days).
  scope: per Reserved Instance; fixed.
  link: [31536000 seconds (365 days)](../facts/ec2.md#ec2-ri-year-defined-in-seconds)
  link: [94608000 seconds (1095 days)](../facts/ec2.md#ec2-ri-year-defined-in-seconds)
  say: three hundred sixty-five days | one thousand ninety-five days
ec2-right-size-before-committing
  claim: Before committing to a purchasing option, right-size the instances with AWS Compute Optimizer, because oversized instances waste money under any purchasing model.
  scope: EC2 purchasing decisions.
  link: [Oversized instances waste money](../facts/ec2.md#ec2-right-size-before-committing)
  say: oversized instances waste money whatever you buy
ec2-root-volume-one-per-instance
  claim: Each instance has a single root volume, created at launch, that contains the image used to boot the instance; you can add storage volumes during or after launch.
  scope: per instance; fixed.
  link: [Each instance has a single root volume](../facts/ec2.md#ec2-root-volume-one-per-instance)
  link: [contains the image used to boot the instance](../facts/ec2.md#ec2-root-volume-one-per-instance)
ec2-s3-backed-ami-end-of-life
  claim: S3-backed (instance store-backed) AMIs are considered end of life, are not recommended for new use, and are supported only on older instance types (C1, C3, D2, I2, M1, M2, M3, R3 and X1).
  scope: Amazon S3-backed AMIs.
  link: [considered end of life](../facts/ec2.md#ec2-s3-backed-ami-end-of-life)
  link: [only supported on the following older instance types](../facts/ec2.md#ec2-s3-backed-ami-end-of-life)
  say: instance store backed AMIs are end of life
ec2-savings-plans-two-ec2-types-flexibility
  claim: Compute Savings Plans apply to any EC2 instance usage regardless of Region, instance family, operating system or tenancy, and also cover Fargate and Lambda; EC2 Instance Savings Plans apply to one instance family in one Region and give higher discounts.
  scope: Savings Plans that apply to Amazon EC2.
  link: [regardless of Region, instance family, operating system](../facts/ec2.md#ec2-savings-plans-two-ec2-types-flexibility)
  link: [a specific instance family within a Region](../facts/ec2.md#ec2-savings-plans-two-ec2-types-flexibility)
  link: [also cover Fargate and Lambda usage](../facts/ec2.md#ec2-savings-plans-two-ec2-types-flexibility)
  say: Compute Savings Plans follow you across Regions, families, operating systems and tenancy | EC2 Instance Savings Plans are tied to one family in one Region
ec2-savings-plans-vs-ri-any-region
  claim: Savings Plans offer savings over On-Demand like EC2 Reserved Instances, but they automatically reduce the bill on compute usage across any AWS Region, even as usage changes, without exchanges or modifications.
  scope: Savings Plans compared with EC2 Reserved Instances.
  link: [across any AWS region, even as usage changes](../facts/ec2.md#ec2-savings-plans-vs-ri-any-region)
  say: Savings Plans follow your usage, no exchanges needed
ec2-savings-plans-vs-ri-discounts-66-72
  claim: Compute Savings Plans give savings of up to 66% (like Convertible RIs) on any EC2 usage regardless of Region, family, size, OS or tenancy, and on Fargate and Lambda; EC2 Instance Savings Plans give up to 72% (like Standard RIs) within one instance family in a chosen Region.
  scope: Savings Plans for EC2 compared with Reserved Instances; maximum; discount compared with On-Demand.
  link: [up to 66%](../facts/ec2.md#ec2-savings-plans-vs-ri-discounts-66-72)
  link: [up to 72%](../facts/ec2.md#ec2-savings-plans-vs-ri-discounts-66-72)
  say: Compute Savings Plans: up to sixty-six percent | EC2 Instance Savings Plans: up to seventy-two percent
ec2-scheduled-events-reboot-stop-retire
  claim: AWS can schedule events to reboot, stop or retire your instances and notifies you in advance by email; an affected instance in an Auto Scaling group is eventually replaced by Amazon EC2 Auto Scaling as part of its health checks.
  scope: scheduled events for EC2 instances.
  link: [schedule events to reboot, stop, and retire](../facts/ec2.md#ec2-scheduled-events-reboot-stop-retire)
  link: [AWS notifies you in advance by email](../facts/ec2.md#ec2-scheduled-events-reboot-stop-retire)
  link: [Amazon EC2 Auto Scaling eventually replaces it](../facts/ec2.md#ec2-scheduled-events-reboot-stop-retire)
  say: AWS can schedule reboot, stop and retire events | you get an email first | Auto Scaling replaces it
ec2-secondary-private-ip-reassignable
  claim: Secondary private IPv4 addresses can be reassigned from one instance to another, unlike primary private IP addresses.
  scope: private IPv4 addresses on network interfaces.
  link: [secondary private IP addresses can be reassigned](../facts/ec2.md#ec2-secondary-private-ip-reassignable)
  link: [Unlike primary private IP addresses](../facts/ec2.md#ec2-secondary-private-ip-reassignable)
  say: secondary private IPs can move | the primary private IP cannot
ec2-security-group-default-and-change-after-launch
  claim: When you launch an instance you can specify one or more security groups; if you specify none, EC2 uses the default security group of the VPC, and you can change an instance's security groups after launch.
  scope: security groups of an EC2 instance; default; adjustable; no security group specified at launch.
  link: [you can specify one or more security groups](../facts/ec2.md#ec2-security-group-default-and-change-after-launch)
  link: [uses the default security group for the VPC](../facts/ec2.md#ec2-security-group-default-and-change-after-launch)
  link: [you can change its security groups](../facts/ec2.md#ec2-security-group-default-and-change-after-launch)
  say: one or more security groups | otherwise the VPC default security group | you can change them after launch
ec2-security-group-rules-apply-immediately-all-groups
  claim: New and modified security group rules are automatically applied to all instances associated with the group, and EC2 evaluates all rules from all security groups associated with an instance to decide whether to allow traffic.
  scope: security groups associated with instances.
  link: [automatically applied to all instances](../facts/ec2.md#ec2-security-group-rules-apply-immediately-all-groups)
  link: [evaluates all rules from all security groups](../facts/ec2.md#ec2-security-group-rules-apply-immediately-all-groups)
  say: rule changes apply automatically | all rules of all groups are combined
ec2-security-group-stateful
  claim: Security groups are stateful: response traffic to a request sent from the instance is allowed in regardless of inbound rules, and responses to allowed inbound traffic are allowed out regardless of outbound rules.
  scope: security groups associated with an instance.
  link: [Security groups are stateful](../facts/ec2.md#ec2-security-group-stateful)
  link: [regardless of inbound security group rules](../facts/ec2.md#ec2-security-group-stateful)
  say: security groups are stateful | responses come back in without an inbound rule
ec2-session-manager-no-inbound-ports-bastion-keys
  claim: Session Manager provides secure node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.
  scope: AWS Systems Manager Session Manager for EC2 instances; the instance is managed by Systems Manager.
  link: [without the need to open inbound ports](../facts/ec2.md#ec2-session-manager-no-inbound-ports-bastion-keys)
  link: [maintain bastion hosts, or manage SSH keys](../facts/ec2.md#ec2-session-manager-no-inbound-ports-bastion-keys)
  say: no open inbound ports | no bastion host and no SSH keys
ec2-session-manager-prereq-iam-role
  claim: To connect with Session Manager, the instance must be managed by SSM and must have an attached IAM role with the AmazonSSMManagedInstanceCore policy.
  scope: Session Manager connections to EC2 instances.
  link: [AmazonSSMManagedInstanceCore](../facts/ec2.md#ec2-session-manager-prereq-iam-role)
  say: an instance role with AmazonSSMManagedInstanceCore
ec2-shutdown-behavior-default-stop
  claim: For an EBS-backed instance, the InstanceInitiatedShutdownBehavior attribute decides whether a shutdown from inside the operating system stops or terminates the instance; the default is to stop the instance.
  scope: EBS-backed instances; default; adjustable; shutdown initiated from within the instance.
  link: [The default behavior is to stop the instance](../facts/ec2.md#ec2-shutdown-behavior-default-stop)
  link: [InstanceInitiatedShutdownBehavior](../facts/ec2.md#ec2-shutdown-behavior-default-stop)
  say: an OS shutdown stops an EBS-backed instance by default
ec2-source-dest-check-default-nat
  claim: By default, an instance cannot receive traffic that is not specifically addressed to it; to run NAT, routing or firewall services on the instance, you disable source/destination checking for the network interface.
  scope: per network interface of an EC2 instance; default; adjustable; source/destination checking enabled.
  link: [traffic that is not specifically addressed to it](../facts/ec2.md#ec2-source-dest-check-default-nat)
  link: [disable source/destination checking](../facts/ec2.md#ec2-source-dest-check-default-nat)
  say: by default traffic must be addressed to the instance | turn off the source/destination check
ec2-spot-be-flexible-types-and-azs
  claim: A Spot best practice is to be flexible about which instance types you request and in which Availability Zones you deploy, which gives Spot a better chance to find the capacity you need.
  scope: Spot Instances.
  link: [flexible about which instance types you request](../facts/ec2.md#ec2-spot-be-flexible-types-and-azs)
  say: be flexible about instance types and Availability Zones
ec2-spot-capacity-optimized-high-restart-cost
  claim: The capacity-optimized Spot allocation strategy works well for workloads with a higher cost of interruption from restarting work, such as long CI, image and media rendering, deep learning and HPC.
  scope: EC2 Fleet and Spot Fleet Spot allocation strategy.
  link: [a higher cost of interruption](../facts/ec2.md#ec2-spot-capacity-optimized-high-restart-cost)
  say: capacity-optimized when restarting work is expensive
ec2-spot-capacity-pool-definition
  claim: A Spot capacity pool is a set of unused EC2 instances with the same instance type and Availability Zone.
  scope: Spot Instances.
  link: [A set of unused EC2 instances](../facts/ec2.md#ec2-spot-capacity-pool-definition)
  link: [with the same instance type](../facts/ec2.md#ec2-spot-capacity-pool-definition)
  say: a pool is unused instances of one type in one Availability Zone | same instance type, same Availability Zone
ec2-spot-discount-up-to-90-percent
  claim: Spot Instances use spare EC2 capacity at a discount of up to 90% compared with On-Demand prices.
  scope: per Spot Instance; maximum; spare EC2 capacity; the Spot price varies with supply and demand.
  link: [up to 90%](../facts/ec2.md#ec2-spot-discount-up-to-90-percent)
  say: up to ninety percent off On-Demand
ec2-spot-discourage-failover-to-on-demand
  claim: For workloads that are inflexible, stateful, fault-intolerant or tightly coupled, AWS strongly discourages using Spot Instances, and also discourages attempting to fail over to On-Demand Instances to handle interruptions or periods of unavailability.
  scope: Spot Instances for interruption-intolerant workloads.
  link: [attempting to fail over to On-Demand Instances](../facts/ec2.md#ec2-spot-discourage-failover-to-on-demand)
  say: AWS strongly discourages failing over from Spot to On-Demand
ec2-spot-diversified-all-pools
  claim: With the diversified Spot allocation strategy, the Spot Instances are distributed across all Spot capacity pools.
  scope: EC2 Fleet and Spot Fleet Spot allocation strategy.
  link: [distributed across all Spot capacity pools](../facts/ec2.md#ec2-spot-diversified-all-pools)
  say: diversified spreads Spot Instances across all pools
ec2-spot-interrupted-by-aws-first-hour-free
  claim: For Linux and Windows (excluding SUSE) Spot Instances, when Amazon EC2 interrupts the instance in the first hour there is no charge, and after the first hour you are charged for the seconds used; when you stop or terminate it yourself you are charged for the seconds used in every hour.
  scope: per Spot Instance; Windows and Linux excluding SUSE; SUSE is billed by the full hour.
  link: [No charge](../facts/ec2.md#ec2-spot-interrupted-by-aws-first-hour-free)
  link: [Charged for the seconds used](../facts/ec2.md#ec2-spot-interrupted-by-aws-first-hour-free)
  say: no charge if AWS interrupts in the first hour | charged for the seconds used after the first hour
ec2-spot-interruption-default-terminate
  claim: When you create a Spot request you can choose the interruption behavior (stop, hibernate or terminate); by default Amazon EC2 terminates Spot Instances when they are interrupted.
  scope: Spot Instance interruption behavior; default; adjustable; set in the Spot request.
  link: [terminates the instance by default](../facts/ec2.md#ec2-spot-interruption-default-terminate)
  link: [you can specify the interruption behavior](../facts/ec2.md#ec2-spot-interruption-default-terminate)
  say: by default an interrupted Spot Instance is terminated | you can choose stop, hibernate or terminate
ec2-spot-interruption-notice-channels
  claim: Spot interruption notices are delivered as an EventBridge event and as items in the instance metadata of the Spot Instance; AWS recommends checking for them every 5 seconds.
  scope: per Spot Instance.
  link: [as an EventBridge event](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  link: [every 5 seconds](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  link: [as items in the instance metadata](../facts/ec2.md#ec2-spot-interruption-notice-channels)
  say: an EventBridge event and the instance metadata | every five seconds | and in the instance metadata
ec2-spot-interruption-notice-two-minutes
  claim: A Spot Instance interruption notice is a warning issued two minutes before Amazon EC2 stops or terminates the Spot Instance; with hibernation as the interruption behavior you get the notice but not a two-minute warning, because hibernation begins immediately.
  scope: per Spot Instance; fixed; interruption notices are emitted on a best effort basis.
  link: [two minutes before Amazon EC2 stops or terminates your Spot Instance](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  link: [you do not receive a two-minute warning](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  say: a two-minute warning | no two-minute warning for hibernation
ec2-spot-interruption-reasons
  claim: Amazon EC2 can interrupt a Spot Instance for capacity (it needs the capacity back), for price (the Spot price is higher than your maximum price), or for constraints (a launch group or Availability Zone group that can no longer be met).
  scope: Spot Instance interruptions.
  link: [Amazon EC2 can interrupt your Spot Instance when it needs it back](../facts/ec2.md#ec2-spot-interruption-reasons)
  link: [Spot price is higher than your maximum price](../facts/ec2.md#ec2-spot-interruption-reasons)
  link: [terminated as a group](../facts/ec2.md#ec2-spot-interruption-reasons)
  say: capacity: EC2 needs the capacity back | price: the Spot price is above your maximum price | constraints: a launch group is terminated together
ec2-spot-launch-group-all-or-none
  claim: A launch group in a Spot request tells Amazon EC2 to launch the set of Spot Instances only if it can launch them all, and if the Spot service must terminate one instance in the group it must terminate them all.
  scope: Spot Instance launch groups; launch group specified.
  link: [only if it can launch them all](../facts/ec2.md#ec2-spot-launch-group-all-or-none)
  link: [it must terminate them all](../facts/ec2.md#ec2-spot-launch-group-all-or-none)
  say: a launch group launches all instances or none | and terminates them all together
ec2-spot-max-price-default-on-demand-pay-spot-price
  claim: The maximum Spot price is the most you would pay for a Spot instance hour and by default it is set at the On-Demand price; you continue to pay the Spot market price, not your maximum price, charged in per-second increments.
  scope: Spot Instance maximum price; default; adjustable.
  link: [by default, is set at the On-Demand price](../facts/ec2.md#ec2-spot-max-price-default-on-demand-pay-spot-price)
  link: [pay the Spot market price](../facts/ec2.md#ec2-spot-max-price-default-on-demand-pay-spot-price)
  link: [not your maximum price](../facts/ec2.md#ec2-spot-max-price-default-on-demand-pay-spot-price)
  say: the default maximum price is the On-Demand price | you pay the Spot price, not your maximum price | not the maximum price
ec2-spot-max-price-more-interruptions
  claim: If you specify a maximum price in a Spot request, your instances are interrupted more frequently than if you do not specify one.
  scope: Spot requests; a maximum price is specified.
  link: [interrupted more frequently](../facts/ec2.md#ec2-spot-max-price-more-interruptions)
  link: [than if you do not specify it](../facts/ec2.md#ec2-spot-max-price-more-interruptions)
  say: a maximum price means more interruptions | leaving the maximum price empty is better
ec2-spot-no-guarantee-to-finish
  claim: Spot does not guarantee that you can keep your running instances long enough to finish your workloads.
  scope: Spot Instances.
  link: [Spot does not guarantee](../facts/ec2.md#ec2-spot-no-guarantee-to-finish)
  say: Spot gives no guarantee that the instance stays
ec2-spot-no-termination-protection
  claim: You cannot enable termination protection for Spot Instances.
  scope: Spot Instances.
  link: [You can't enable termination protection for Spot Instances](../facts/ec2.md#ec2-spot-no-termination-protection)
  link: [you must be prepared for interruptions](../facts/ec2.md#ec2-spot-no-termination-protection)
  say: Spot Instances cannot have termination protection | plan for interruptions instead
ec2-spot-not-covered-by-savings-plans
  claim: Spot Instances are not covered by Savings Plans: a Savings Plan gives no extra discount on Spot usage, and Spot spend does not count toward a Compute Savings Plans commitment.
  scope: per account.
  link: [Spot Instances are not covered by Savings Plans](../facts/ec2.md#ec2-spot-not-covered-by-savings-plans)
  say: Savings Plans do not cover Spot
ec2-spot-not-suitable-stateful-inflexible
  claim: Spot Instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes.
  scope: Spot Instances.
  link: [inflexible, stateful, fault-intolerant, or tightly coupled](../facts/ec2.md#ec2-spot-not-suitable-stateful-inflexible)
  say: not for stateful, inflexible or tightly coupled work
ec2-spot-one-time-request-closed
  claim: A one-time Spot Instance request remains active until Amazon EC2 launches the Spot Instance, the request expires, or you cancel it; if capacity is not available the Spot Instance is terminated and the request is closed.
  scope: one-time Spot Instance requests.
  link: [remains active until Amazon EC2 launches the Spot Instance](../facts/ec2.md#ec2-spot-one-time-request-closed)
  link: [the Spot Instance request is closed](../facts/ec2.md#ec2-spot-one-time-request-closed)
  say: a one-time request ends once the instance launches | after an interruption the one-time request is closed
ec2-spot-only-difference-interruption-two-minutes
  claim: The only difference between On-Demand Instances and Spot Instances is that Amazon EC2 can interrupt Spot Instances, with two minutes of notice, when it needs to reclaim the capacity.
  scope: Spot Instances versus On-Demand Instances; when Amazon EC2 needs to reclaim the capacity.
  link: [two minutes of notice](../facts/ec2.md#ec2-spot-only-difference-interruption-two-minutes)
  link: [Spot Instances can be interrupted by Amazon EC2](../facts/ec2.md#ec2-spot-only-difference-interruption-two-minutes)
  say: two minutes of notice | Amazon EC2 can take a Spot Instance back
ec2-spot-persistent-request-resubmitted
  claim: A persistent Spot Instance request stays active until it expires or you cancel it; after an interruption, when capacity returns, the instance is started if stopped or resumed if hibernated, and if the instance is terminated the request is opened again and EC2 launches a new Spot Instance.
  scope: persistent Spot Instance requests.
  link: [remains active until it expires](../facts/ec2.md#ec2-spot-persistent-request-resubmitted)
  link: [the Spot Instance request is opened again](../facts/ec2.md#ec2-spot-persistent-request-resubmitted)
  say: a persistent request stays until it expires or is cancelled | if the instance is terminated, the request opens again
ec2-spot-placement-score-recommendation-only
  claim: A Spot placement score indicates how likely a Spot request is to succeed in a Region or Availability Zone; it serves only as a recommendation and gives no guarantee of capacity or interruption risk.
  scope: Spot placement score.
  link: [that a Spot request will succeed](../facts/ec2.md#ec2-spot-placement-score-recommendation-only)
  link: [serves only as a recommendation](../facts/ec2.md#ec2-spot-placement-score-recommendation-only)
  say: the score says how likely a Spot request is to succeed | it is only a recommendation, not a guarantee
ec2-spot-price-capacity-optimized-recommended
  claim: AWS recommends the price-capacity-optimized Spot allocation strategy, because it provisions instances from the most-available Spot capacity pools that also have the lowest possible price.
  scope: Spot allocation strategy in Auto Scaling groups and EC2 Fleet.
  link: [price-capacity-optimized](../facts/ec2.md#ec2-spot-price-capacity-optimized-recommended)
  link: [the most-available Spot capacity pools](../facts/ec2.md#ec2-spot-price-capacity-optimized-recommended)
  say: price-capacity-optimized | it picks the most available pools at the lowest price
ec2-spot-price-history-three-months
  claim: The lowest current Spot price per Region and instance type is updated every five minutes, and the Spot price history covers the past three months.
  scope: per Region, per instance type; maximum; not adjustable.
  link: [updated every five minutes](../facts/ec2.md#ec2-spot-price-history-three-months)
  link: [the past three months](../facts/ec2.md#ec2-spot-price-history-three-months)
  say: updated every five minutes | three months of history
ec2-spot-price-set-by-ec2-not-bid
  claim: The Spot price of each instance type in each Availability Zone is set by Amazon EC2 and adjusted gradually based on long-term supply and demand; the Spot Instance runs whenever capacity is available.
  scope: per instance type, per Availability Zone.
  link: [set by Amazon EC2, and is adjusted gradually based on the long-term supply of and demand](../facts/ec2.md#ec2-spot-price-set-by-ec2-not-bid)
  say: set by EC2 and adjusted gradually with long-term supply and demand
ec2-spot-quota-exceeded-error
  claim: If you submit a Spot Instance request and receive the error Max spot instance count exceeded, you can request a quota increase, which you do in the Service Quotas console.
  scope: per account, per Region.
  link: [Max spot instance count exceeded](../facts/ec2.md#ec2-spot-quota-exceeded-error)
  say: max spot instance count exceeded
ec2-spot-quota-measured-in-vcpus
  claim: Spot Instance quotas apply per account per Region and are measured in vCPUs that running Spot Instances use or that open Spot requests will use; uncancelled requests for terminated Spot Instances keep counting until EC2 closes them.
  scope: per account, per Region; maximum; adjustable; running Spot Instances plus pending Spot requests.
  link: [number of virtual central processing units (vCPUs)](../facts/ec2.md#ec2-spot-quota-measured-in-vcpus)
  link: [the requests count against your Spot Instance vCPU quota until Amazon EC2 detects the Spot Instance terminations](../facts/ec2.md#ec2-spot-quota-measured-in-vcpus)
  say: the number of vCPUs
ec2-spot-rebalance-recommendation-channels
  claim: Rebalance recommendations are made available as an EventBridge event and as an item in the instance metadata of the Spot Instance, and events are emitted on a best effort basis.
  scope: Spot Instance rebalance recommendations.
  link: [made available as a EventBridge event](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  link: [as an item in the instance metadata](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  link: [emitted on a best effort basis](../facts/ec2.md#ec2-spot-rebalance-recommendation-channels)
  say: you get it as an EventBridge event | and in the instance metadata
ec2-spot-rebalance-recommendation-earlier-signal
  claim: A rebalance recommendation is a signal that a Spot Instance is at elevated risk of interruption; it can arrive sooner than the two-minute interruption notice, but it is not always sent first and can arrive together with the notice.
  scope: Spot Instances.
  link: [at elevated risk of interruption](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  link: [The signal can arrive sooner](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  link: [can arrive along with the two-minute interruption notice](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  say: a rebalance recommendation warns of elevated interruption risk | it can come before the two-minute notice
ec2-spot-recommended-stateless-fault-tolerant-flexible
  claim: AWS recommends Spot Instances for stateless, fault-tolerant, flexible applications, such as big data, containerized workloads, CI/CD, stateless web servers, high performance computing (HPC) and rendering.
  scope: Spot Instances.
  link: [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  link: [big data, containerized workloads, CI/CD](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  say: Spot is for stateless, fault-tolerant, flexible applications
ec2-spot-rule-of-thumb-10-instance-types
  claim: A good rule of thumb for Spot is to be flexible across at least 10 instance types for each workload.
  scope: per Spot workload; minimum; a rule of thumb, not a quota.
  link: [at least 10 instance types](../facts/ec2.md#ec2-spot-rule-of-thumb-10-instance-types)
  say: at least ten instance types
ec2-spot-standard-quota-default-5
  claim: The Service Quotas default for All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests is 5, and the quota is adjustable; Spot Instance quotas are per AWS account per Region and are managed in vCPUs.
  scope: per account, per Region; measured in vCPUs; default; adjustable; Standard families A, C, D, H, I, M, R, T, Z; EC2 adjusts the quota automatically based on usage.
  link: [All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests | 5](../facts/ec2.md#ec2-spot-standard-quota-default-5)
  say: a default of five for Standard Spot requests
ec2-spot-stop-behavior-needs-persistent-request
  claim: To have interrupted Spot Instances stopped instead of terminated, the Spot Instance request type must be persistent and the request cannot specify a launch group; for EC2 Fleet or Spot Fleet the request type must be maintain.
  scope: Spot Instances with the stop interruption behavior.
  link: [The Spot Instance request type must be persistent](../facts/ec2.md#ec2-spot-stop-behavior-needs-persistent-request)
  link: [the request type must be maintain](../facts/ec2.md#ec2-spot-stop-behavior-needs-persistent-request)
  link: [You can't specify a launch group](../facts/ec2.md#ec2-spot-stop-behavior-needs-persistent-request)
  say: stop on interruption needs a persistent Spot request | for a fleet the type must be maintain
ec2-spot-stopped-charged-only-for-ebs
  claim: While an interrupted Spot Instance is stopped you are charged only for its preserved EBS volumes.
  scope: per Spot Instance; interruption behavior stop.
  link: [charged only for the EBS volumes](../facts/ec2.md#ec2-spot-stopped-charged-only-for-ebs)
  say: only the EBS volumes
ec2-spot-stopped-restart-only-by-ec2
  claim: Only Amazon EC2 can restart a Spot Instance that was stopped by an interruption; for a persistent request it restarts the instance when capacity is available in the same Availability Zone and for the same instance type, and the same launch specification must be used.
  scope: interrupted Spot Instances with the stop behavior; persistent Spot Instance request; the same launch specification must be used.
  link: [Only Amazon EC2 can restart](../facts/ec2.md#ec2-spot-stopped-restart-only-by-ec2)
  link: [capacity is available in the same Availability Zone](../facts/ec2.md#ec2-spot-stopped-restart-only-by-ec2)
  say: only EC2 can restart an interrupted stopped Spot Instance | it comes back in the same Availability Zone and instance type
ec2-spot-unavailable-capacity-request-keeps-trying
  claim: If capacity is not available, a Spot Instance request keeps making the launch request automatically until capacity becomes available, whereas an On-Demand launch request gets an insufficient capacity error (ICE).
  scope: Spot Instances compared with On-Demand Instances; capacity not available.
  link: [continues to automatically make the launch request](../facts/ec2.md#ec2-spot-unavailable-capacity-request-keeps-trying)
  link: [you get an insufficient capacity error (ICE)](../facts/ec2.md#ec2-spot-unavailable-capacity-request-keeps-trying)
  say: a Spot request keeps trying until capacity appears | On-Demand returns an insufficient capacity error
ec2-spot-vs-savings-plans-guideline
  claim: As a general guideline, Spot Instances suit flexible workloads with variable demand that can tolerate interruptions, while Savings Plans suit steady-state, predictable workloads that need uninterrupted availability.
  scope: Spot Instances versus Savings Plans.
  link: [can tolerate interruptions](../facts/ec2.md#ec2-spot-vs-savings-plans-guideline)
  link: [a better fit for steady-state workloads](../facts/ec2.md#ec2-spot-vs-savings-plans-guideline)
  say: Spot when the work can tolerate interruptions | Savings Plans for steady-state work
ec2-ssm-agent-outbound-https-443-no-inbound
  claim: Without a VPC endpoint, Systems Manager managed instances need outbound internet access and must allow HTTPS (port 443) outbound traffic to the Systems Manager endpoints listed on the page; SSM Agent initiates all connections to the Systems Manager service, so you don't need to allow inbound traffic to your instances for Systems Manager.
  scope: Systems Manager managed instances without VPC endpoints; outbound internet access is used instead of a VPC endpoint.
  link: [HTTPS (port 443) outbound traffic](../facts/ec2.md#ec2-ssm-agent-outbound-https-443-no-inbound)
  link: [SSM Agent initiates all connections](../facts/ec2.md#ec2-ssm-agent-outbound-https-443-no-inbound)
  link: [allow inbound traffic to your instances](../facts/ec2.md#ec2-ssm-agent-outbound-https-443-no-inbound)
  say: outbound HTTPS on port four forty-three | the agent starts every connection | no inbound rule needed
ec2-state-diff-elastic-ip
  claim: An Elastic IP address remains associated with the instance through a reboot, a stop/start and a hibernate, and is disassociated from the instance when it is terminated.
  scope: Elastic IP address (IPv4).
  link: [remains associated with the instance](../facts/ec2.md#ec2-state-diff-elastic-ip)
  link: [The Elastic IP address is disassociated](../facts/ec2.md#ec2-state-diff-elastic-ip)
  link: [disassociated from the instance](../facts/ec2.md#ec2-state-diff-elastic-ip)
  say: an Elastic IP stays associated through a stop | terminate disassociates the Elastic IP
ec2-state-diff-host-computer
  claim: A reboot keeps the instance on the same host computer; a stop/start or hibernate moves it to a new host computer, though in some cases it remains on the current host.
  scope: EBS-backed instances.
  link: [The instance stays on the same host computer](../facts/ec2.md#ec2-state-diff-host-computer)
  link: [moved to a new host computer](../facts/ec2.md#ec2-state-diff-host-computer)
ec2-state-diff-instance-store-data
  claim: Data on instance store volumes is preserved by a reboot but erased by a stop, a hibernate and a terminate.
  scope: instance store volumes.
  link: [The data is preserved](../facts/ec2.md#ec2-state-diff-instance-store-data)
  link: [The data is erased](../facts/ec2.md#ec2-state-diff-instance-store-data)
  say: a reboot keeps instance store data | stop, hibernate and terminate erase instance store data
ec2-state-diff-private-ipv4
  claim: The instance keeps its private IPv4 address through a reboot, a stop/start and a hibernate; a terminated instance has none.
  scope: primary private IPv4 address.
  link: [The instance keeps its private IPv4 address](../facts/ec2.md#ec2-state-diff-private-ipv4)
  link: [keeps its private IPv4 address](../facts/ec2.md#ec2-state-diff-private-ipv4)
  say: the private IP v4 address stays the same across stop and start
ec2-state-diff-public-ipv4
  claim: A reboot keeps the public IPv4 address; after a stop/start or hibernate the instance gets a new public IPv4 address, unless it has a secondary network interface or a secondary private IPv4 address that is associated with an Elastic IP address.
  scope: auto-assigned public IPv4 address; not when an Elastic IP is associated.
  link: [The instance gets a new public IPv4 address](../facts/ec2.md#ec2-state-diff-public-ipv4)
  link: [The instance keeps its public IPv4 address](../facts/ec2.md#ec2-state-diff-public-ipv4)
  link: [new public IPv4 address](../facts/ec2.md#ec2-state-diff-public-ipv4)
  say: a stop and start gives the instance a new public IP v4 address
ec2-state-diff-ram
  claim: RAM contents are erased by a reboot, a stop and a terminate; only hibernate saves the RAM to a file on the root volume.
  scope: instance memory (RAM).
  link: [The RAM is erased](../facts/ec2.md#ec2-state-diff-ram)
  link: [saved to a file on the root volume](../facts/ec2.md#ec2-state-diff-ram)
ec2-state-diff-root-volume
  claim: The root volume is preserved by a reboot, a stop and a hibernate; on terminate it is deleted by default.
  scope: EBS root volume; default; terminate deletes it only while DeleteOnTermination is true.
  link: [The volume is preserved](../facts/ec2.md#ec2-state-diff-root-volume)
  link: [The volume is deleted by default](../facts/ec2.md#ec2-state-diff-root-volume)
  link: [deleted by default](../facts/ec2.md#ec2-state-diff-root-volume)
ec2-state-pending-not-billed
  claim: An instance in the pending state is preparing to enter the running state (after a launch or a start from stopped) and is not billed.
  scope: per instance.
  link: [pending](../facts/ec2.md#ec2-state-pending-not-billed)
  link: [Not billed](../facts/ec2.md#ec2-state-pending-not-billed)
  say: pending is not billed
ec2-state-running-billed
  claim: An instance in the running state is ready for use and its instance usage is billed.
  scope: per instance.
  link: [The instance is running and ready for use](../facts/ec2.md#ec2-state-running-billed)
  link: [Billed](../facts/ec2.md#ec2-state-running-billed)
  say: running is the billed state | it is billed
ec2-state-shutting-down-not-billed
  claim: An instance in the shutting-down state is preparing to be terminated and is not billed.
  scope: per instance.
  link: [shutting-down](../facts/ec2.md#ec2-state-shutting-down-not-billed)
  say: shutting down is not billed
ec2-state-stopped-not-billed
  claim: A stopped instance is shut down, cannot be used, can be started at any time, and its instance usage is not billed.
  scope: per instance; EBS volumes and Elastic IP addresses are still charged.
  link: [stopped](../facts/ec2.md#ec2-state-stopped-not-billed)
  link: [The instance can be started at any time](../facts/ec2.md#ec2-state-stopped-not-billed)
  say: stopped is not billed
ec2-state-stopping-billed-only-when-hibernating
  claim: An instance in the stopping state is not billed, except that when you hibernate an instance you are billed while it is in the stopping state.
  scope: per instance; hibernation.
  link: [If you hibernate an instance, you're billed](../facts/ec2.md#ec2-state-stopping-billed-only-when-hibernating)
  say: stopping is free unless you are hibernating
ec2-state-terminated-ri-billed-to-end-of-term
  claim: A terminated instance is permanently deleted, cannot be started and is not billed, but Reserved Instances that applied to it are still billed until the end of their term according to their payment option.
  scope: per instance; a Reserved Instance applied to the terminated instance.
  link: [billed until the end of their term](../facts/ec2.md#ec2-state-terminated-ri-billed-to-end-of-term)
  link: [terminated](../facts/ec2.md#ec2-state-terminated-ri-billed-to-end-of-term)
  say: the Reserved Instance is billed to the end of its term
ec2-status-check-instance-needs-you
  claim: Instance status checks monitor the software and network connectivity of your individual instance and detect problems that need your involvement to repair, for example by rebooting the instance or changing its configuration.
  scope: instance status checks.
  link: [require your involvement to repair](../facts/ec2.md#ec2-status-check-instance-needs-you)
  link: [by rebooting the instance](../facts/ec2.md#ec2-status-check-instance-needs-you)
  say: an instance check problem is yours to fix | for example by rebooting
ec2-status-check-system-needs-aws
  claim: System status checks monitor the AWS systems your instance runs on and detect problems that need AWS involvement to repair; for an EBS-backed instance you can stop and start it yourself, which in most cases migrates it to a new host.
  scope: system status checks; stop and start applies to instances backed by Amazon EBS.
  link: [require AWS involvement to repair](../facts/ec2.md#ec2-status-check-system-needs-aws)
  link: [stop and start the instance yourself](../facts/ec2.md#ec2-status-check-system-needs-aws)
  link: [migrated to a new host](../facts/ec2.md#ec2-status-check-system-needs-aws)
  say: a system check problem needs AWS to fix it | or you stop and start the instance | which moves it to a new host
ec2-status-checks-every-minute
  claim: EC2 performs status checks every minute, and each check returns a pass or a fail status.
  scope: EC2 status checks.
  link: [performed every minute](../facts/ec2.md#ec2-status-checks-every-minute)
  link: [returning a pass or a fail status](../facts/ec2.md#ec2-status-checks-every-minute)
  say: every minute | each check passes or fails
ec2-status-checks-four-types-application-opt-in
  claim: Amazon EC2 has four types of status checks: system, instance, attached EBS and application; the first three are managed by Amazon EC2, run automatically on every instance and cannot be disabled, while application status checks are opt-in and monitor HTTP or HTTPS responses.
  scope: per instance.
  link: [four types of status checks](../facts/ec2.md#ec2-status-checks-four-types-application-opt-in)
  link: [Application status checks are opt-in](../facts/ec2.md#ec2-status-checks-four-types-application-opt-in)
  link: [run automatically on every instance](../facts/ec2.md#ec2-status-checks-four-types-application-opt-in)
  say: four kinds of status checks | application checks are opt-in | system, instance and EBS checks run on every instance
ec2-steady-state-savings-plans
  claim: Steady-state workloads with consistent, predictable usage, such as databases and core infrastructure, benefit most from long-term commitments through Savings Plans.
  scope: steady-state EC2 workloads.
  link: [benefit most from long-term commitments through Savings Plans](../facts/ec2.md#ec2-steady-state-savings-plans)
  say: steady work gets the most from Savings Plans
ec2-stop-protection-not-instance-store-or-spot
  claim: You can't enable stop protection for an instance with an instance store root volume, or for Spot Instances.
  scope: stop protection.
  link: [an instance with an instance store root volume](../facts/ec2.md#ec2-stop-protection-not-instance-store-or-spot)
  link: [You can't enable stop protection for Spot Instances](../facts/ec2.md#ec2-stop-protection-not-instance-store-or-spot)
  say: not on instance store root instances | and not on Spot Instances
ec2-stop-protection-scope
  claim: Stop protection prevents accidental stops and also accidental termination, but it does not prevent a shutdown started from the operating system on the instance, or Amazon EC2 Auto Scaling from terminating an instance when the instance is unhealthy or during scale-in events.
  scope: stop protection on an EC2 instance.
  link: [also protects your instance from accidental termination](../facts/ec2.md#ec2-stop-protection-scope)
  link: [initiating a shutdown from the instance](../facts/ec2.md#ec2-stop-protection-scope)
  link: [does not prevent Amazon EC2 Auto Scaling](../facts/ec2.md#ec2-stop-protection-scope)
  say: stop protection also blocks accidental termination | but not a shutdown from the operating system | and not Auto Scaling termination
ec2-stop-start-fix-for-failed-status-check
  claim: If an instance fails a status check and its root volume is an EBS volume, you can stop and start the instance to try to fix the problem.
  scope: instances with an EBS root volume.
  link: [to try to fix the problem](../facts/ec2.md#ec2-stop-start-fix-for-failed-status-check)
  link: [stop and start](../facts/ec2.md#ec2-stop-start-fix-for-failed-status-check)
  say: stop and start it to try to fix the problem
ec2-stop-start-moves-host-loses-instance-store
  claim: When you start a stopped instance it is moved to a new host computer (in some cases it remains on the current host), and any data on the instance store volumes of the previous host is lost.
  scope: EBS-backed instances.
  link: [moved to a new host computer](../facts/ec2.md#ec2-stop-start-moves-host-loses-instance-store)
  link: [you lose any data on the instance store](../facts/ec2.md#ec2-stop-start-moves-host-loses-instance-store)
ec2-stop-start-new-billing-period-one-minute-minimum
  claim: Charges stop as soon as an instance enters the stopping state (for hibernation, only when it reaches stopped); each transition from stopped to running starts a new billing period with a minimum of one minute, and a reboot does not change the billing hour.
  scope: per instance; minimum; Amazon EBS-backed instances for stop/start and hibernate.
  link: [a minimum of one minute](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  link: [as soon as its state changes to stopping](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  link: [The instance billing hour doesn't change](../facts/ec2.md#ec2-stop-start-new-billing-period-one-minute-minimum)
  say: a one-minute minimum on every start | charges stop at stopping | a reboot does not change the billing hour
ec2-stopped-instance-type-change
  claim: While an instance is in the stopped state you can modify certain attributes of the instance, including the instance type; you are charged for EBS storage but not for instance usage.
  scope: stopped EBS-backed instances.
  link: [modify certain attributes of the instance](../facts/ec2.md#ec2-stopped-instance-type-change)
  link: [Charges are incurred for the storage](../facts/ec2.md#ec2-stopped-instance-type-change)
  link: [including the instance type](../facts/ec2.md#ec2-stopped-instance-type-change)
  say: you change the instance type while the instance is stopped
ec2-suse-billed-full-hour
  claim: Partial instance-hours are billed per second for Linux, Windows, RHEL and Ubuntu Pro, but SUSE Linux Enterprise Server instances are billed as a full hour.
  scope: per instance; SUSE Linux Enterprise Server.
  link: [billed as a full hour](../facts/ec2.md#ec2-suse-billed-full-hour)
  link: [billed per-second](../facts/ec2.md#ec2-suse-billed-full-hour)
  say: billed as a full hour
ec2-tenancy-change-stopped-instance-only
  claim: You can change the tenancy of an instance after launch only while it is stopped, and not with the AWS Management Console; the change takes effect the next time the instance starts.
  scope: EC2 instance tenancy change.
  link: [The instance must be in the stopped state](../facts/ec2.md#ec2-tenancy-change-stopped-instance-only)
  link: [take effect the next time the instance starts](../facts/ec2.md#ec2-tenancy-change-stopped-instance-only)
  link: [using the AWS Management Console](../facts/ec2.md#ec2-tenancy-change-stopped-instance-only)
  say: yes, but the instance must be stopped | the change applies at the next start
ec2-terminated-instance-cannot-recover
  claim: You cannot connect to or recover a terminated instance; it stays visible in the console for a short while and is then deleted automatically.
  scope: terminated instances.
  link: [You can't connect to or recover](../facts/ec2.md#ec2-terminated-instance-cannot-recover)
  link: [visible in the console for a short while](../facts/ec2.md#ec2-terminated-instance-cannot-recover)
  say: a terminated instance cannot be recovered
ec2-termination-protection-blocks-api
  claim: With termination protection enabled, the instance cannot be terminated using the console, CLI or API.
  scope: per instance; termination protection is enabled.
  link: [you can't terminate the instance](../facts/ec2.md#ec2-termination-protection-blocks-api)
  link: [termination protection](../facts/ec2.md#ec2-termination-protection-blocks-api)
  link: [using the console, CLI, or API](../facts/ec2.md#ec2-termination-protection-blocks-api)
  say: termination protection blocks terminate calls from the console, the CLI and the API | from the console, CLI or API
ec2-termination-protection-default-off-not-asg
  claim: Termination protection is disabled by default; when enabled, it does not prevent AWS from terminating the instance for a scheduled event or Amazon EC2 Auto Scaling from terminating it when unhealthy or during scale-in.
  scope: termination protection on an EC2 instance; default; adjustable.
  link: [termination protection is disabled for your instance](../facts/ec2.md#ec2-termination-protection-default-off-not-asg)
  link: [does not prevent Amazon EC2 Auto Scaling](../facts/ec2.md#ec2-termination-protection-default-off-not-asg)
  link: [does not prevent AWS from terminating the instance](../facts/ec2.md#ec2-termination-protection-default-off-not-asg)
  say: termination protection is off by default | it does not stop Auto Scaling | or a scheduled AWS termination
ec2-unpredictable-bursts-on-demand-or-spot
  claim: Systems with random or unpredictable spikes can benefit from the flexibility of On-Demand or Spot capacity.
  scope: EC2 workloads with unpredictable bursts.
  link: [maximum flexibility through On-Demand or Spot capacity](../facts/ec2.md#ec2-unpredictable-bursts-on-demand-or-spot)
  say: On-Demand or Spot for unpredictable spikes
ec2-user-data-16-kb-limit
  claim: User data is limited to 16 KB in raw form, before it is base64-encoded.
  scope: per instance; maximum; not adjustable; measured in raw form, before base64 encoding.
  link: [limited to 16 KB](../facts/ec2.md#ec2-user-data-16-kb-limit)
  say: sixteen kilobytes before encoding
ec2-user-data-not-in-ami
  claim: User data is an instance attribute, and it is not included in an AMI created from the instance.
  scope: per AMI.
  link: [user data is not included in the AMI](../facts/ec2.md#ec2-user-data-not-in-ami)
  say: user data is not part of the AMI
ec2-user-data-runs-as-root
  claim: Scripts entered as user data run as the root user, so they should not use sudo.
  scope: per instance; Linux shell scripts.
  link: [run as the root user](../facts/ec2.md#ec2-user-data-runs-as-root)
  say: user data runs as root
ec2-user-data-runs-at-first-launch-by-default
  claim: By default, user data scripts and cloud-init directives run only during the boot cycle of the first launch; you can configure them to run at every restart.
  scope: per instance; default; adjustable; the configuration can be changed to run at every restart.
  link: [run only during the boot cycle](../facts/ec2.md#ec2-user-data-runs-at-first-launch-by-default)
  say: only at the first boot, by default
ec2-user-data-update-needs-stop-ebs-root
  claim: User data is specified at launch; if the root volume is an EBS volume you can stop the instance and update it, and the updated user data does not run automatically at the next start.
  scope: per instance; root volume is an EBS volume; Windows instances can be configured to run updated user data.
  link: [stop the instance and update its user data](../facts/ec2.md#ec2-user-data-update-needs-stop-ebs-root)
  link: [the updated user data is not run automatically](../facts/ec2.md#ec2-user-data-update-needs-stop-ebs-root)
  say: stop it, then edit the user data | the new user data does not run by itself
ec2-vcpu-limits-not-for-reserved-purchases
  claim: The vCPU-based limits apply only to running On-Demand Instances and Spot Instances, not to purchasing Reserved Instances.
  scope: per account, per Region.
  link: [running On-Demand instances and Spot Instances](../facts/ec2.md#ec2-vcpu-limits-not-for-reserved-purchases)
  say: only running On-Demand and Spot Instances
ec2-volume-attachment-limit-by-type-and-size
  claim: The maximum number of EBS volumes that can be attached to an instance depends on the instance type and instance size; exceeding it fails with AttachmentLimitExceeded.
  scope: per instance.
  link: [depends on the instance type and instance size](../facts/ec2.md#ec2-volume-attachment-limit-by-type-and-size)
  say: it depends on instance type and size
ec2-vpc-tenancy-default-and-dedicated
  claim: A VPC has a tenancy of default or dedicated; by default VPCs have default tenancy, and all instances in a VPC with dedicated tenancy run as Dedicated Instances.
  scope: per VPC; default; adjustable.
  link: [your VPCs have `default` tenancy](../facts/ec2.md#ec2-vpc-tenancy-default-and-dedicated)
  link: [the VPC run as Dedicated Instances](../facts/ec2.md#ec2-vpc-tenancy-default-and-dedicated)
  say: VPCs have default tenancy unless you choose dedicated | a dedicated VPC makes every instance dedicated
ec2-wa-evaluate-cost-and-management-overhead
  claim: When selecting a compute option, evaluate its cost (like hourly charge or data transfer) and its management overhead (like patching and scaling).
  scope: Well-Architected PERF02-BP01.
  link: [cost (like hourly charge or data transfer)](../facts/ec2.md#ec2-wa-evaluate-cost-and-management-overhead)
  link: [management overhead (like patching and scaling)](../facts/ec2.md#ec2-wa-evaluate-cost-and-management-overhead)
  say: the cost | the management overhead
ec2-wa-multiple-compute-types-one-workload
  claim: The performance pillar says you can use multiple types of compute solutions in a single workload, because each one has its own advantages and drawbacks.
  scope: Well-Architected PERF02-BP01.
  link: [multiple types of compute solutions](../facts/ec2.md#ec2-wa-multiple-compute-types-one-workload)
  say: mix compute types in one workload
ec2-wa-over-under-provisioning-effects
  claim: Over-provisioning cloud resources can lead to extra costs, while under-provisioning can result in poor performance and a negative customer experience.
  scope: Well-Architected PERF02-BP04.
  link: [Over-provisioning cloud resources can lead to extra costs](../facts/ec2.md#ec2-wa-over-under-provisioning-effects)
  link: [under-provisioning can result in poor performance](../facts/ec2.md#ec2-wa-over-under-provisioning-effects)
  say: too big costs money | too small hurts performance
ec2-wa-pricing-model-per-component
  claim: The Well-Architected cost pillar says to analyze each workload component: resources that run for extended periods suit commitment discounts, and dynamic, short-running ones suit Spot or On-Demand.
  scope: Well-Architected COST07-BP01.
  link: [extended periods (for commitment discounts)](../facts/ec2.md#ec2-wa-pricing-model-per-component)
  link: [dynamic and short-running (for spot or on-demand)](../facts/ec2.md#ec2-wa-pricing-model-per-component)
  say: long-running parts get commitment discounts | short, changing parts use Spot or On-Demand
ec2-wa-region-price-reasons
  claim: Resource pricing is different in each Region because each Region operates within local market conditions, such as the cost of land, fiber, electricity and taxes.
  scope: AWS Regions.
  link: [local market conditions](../facts/ec2.md#ec2-wa-region-price-reasons)
  say: local costs such as land, power and taxes
ec2-wa-region-pricing-differs
  claim: Resource pricing may be different in each Region; the cost pillar says to deploy in higher-cost Regions only to meet latency, data residency and data sovereignty requirements.
  scope: Well-Architected COST07-BP02.
  link: [Resource pricing may be different in each Region](../facts/ec2.md#ec2-wa-region-pricing-differs)
  link: [latency, data residency and data sovereignty requirements](../facts/ec2.md#ec2-wa-region-pricing-differs)
  say: prices differ by Region | only for latency, residency or sovereignty
ec2-wa-ri-strategy-move-to-savings-plans
  claim: The cost pillar says you can keep using EC2 Reserved Instances for the time being, but recommends working on a strategy to use Savings Plans in the future as a more flexible cost savings mechanism.
  scope: EC2 Reserved Instances.
  link: [a more flexible cost savings mechanism](../facts/ec2.md#ec2-wa-ri-strategy-move-to-savings-plans)
  say: plan to move to Savings Plans
ec2-wa-sandbox-on-demand-environments-savings-plans
  claim: The cost pillar suggests Savings Plans for production, quality and development environments, and an On-Demand model for sandbox resources that are powered on only when needed.
  scope: Well-Architected COST07-BP01.
  link: [you might choose an on-demand model](../facts/ec2.md#ec2-wa-sandbox-on-demand-environments-savings-plans)
  link: [production, quality, and development environments](../facts/ec2.md#ec2-wa-sandbox-on-demand-environments-savings-plans)
  say: On-Demand for a sandbox that is on only when needed | Savings Plans for production, quality and development
ec2-wa-scale-dynamically
  claim: The performance pillar says to use the elasticity of the cloud to scale compute resources up or down dynamically to match your needs and avoid over- or under-provisioning capacity.
  scope: Well-Architected PERF02-BP05.
  link: [scale your compute resources up or down dynamically](../facts/ec2.md#ec2-wa-scale-dynamically)
  say: scale up and down with demand
ec2-wa-stable-workloads-rightsizing-tools
  claim: For stable workloads, the performance pillar says to check AWS rightsizing tools such as AWS Compute Optimizer and AWS Trusted Advisor at regular intervals to find opportunities to right-size compute.
  scope: stable workloads, Well-Architected PERF02-BP04.
  link: [AWS Compute Optimizer and AWS Trusted Advisor](../facts/ec2.md#ec2-wa-stable-workloads-rightsizing-tools)
  say: Compute Optimizer and Trusted Advisor
ec2-wa-turn-off-after-hours-70-percent
  claim: Turning off EC2 and RDS instances when they are not used (after hours and weekends) can reduce costs by 70% or more compared with running them all the time.
  scope: EC2 and RDS instances turned off after hours and weekends; minimum; compared with running them 24/7.
  link: [70% or more](../facts/ec2.md#ec2-wa-turn-off-after-hours-70-percent)
  say: seventy percent or more
ec2-zonal-ri-attributes-must-match
  claim: For a zonal Reserved Instance, the discount applies to matching usage in that Availability Zone, and the tenancy, platform, Availability Zone, instance family and instance size of the running instance must all match.
  scope: zonal Reserved Instances.
  link: [platform, Availability Zone, instance family, and instance size](../facts/ec2.md#ec2-zonal-ri-attributes-must-match)
  link: [matching instance usage in that Availability Zone](../facts/ec2.md#ec2-zonal-ri-attributes-must-match)
  say: tenancy, platform, Availability Zone, family and size must match
