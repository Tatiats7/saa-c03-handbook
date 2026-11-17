facts card: 31 facts
ec2-bp-separate-ebs-for-os-and-data
  claim: The EC2 best practices say to use separate EBS volumes for the operating system and for your data, and to make sure the data volume persists after instance termination.
  scope: EC2 storage best practices.
  link: [separate Amazon EBS volumes for the operating system](../facts/ec2.md#ec2-bp-separate-ebs-for-os-and-data)
  say: one volume for the OS, another for data
ec2-ebs-optimized-default-current-generation
  claim: For current generation instance types, EBS optimization is enabled by default at no additional cost.
  scope: per instance; default; not adjustable; current generation instance types; previous generation types have their own prices.
  link: [enabled by default at no additional cost](../facts/ec2.md#ec2-ebs-optimized-default-current-generation)
  say: on by default, no extra cost
ec2-faq-stopped-instance-ebs-still-charged
  claim: For a stopped instance, AWS does not charge hourly usage or data transfer fees, but it does charge for the storage of any attached Amazon EBS volumes.
  scope: a stopped instance.
  link: [we do charge for the storage](../facts/ec2.md#ec2-faq-stopped-instance-ebs-still-charged)
  link: [don't charge hourly usage for a stopped instance](../facts/ec2.md#ec2-faq-stopped-instance-ebs-still-charged)
  say: EBS storage is still charged | no instance-hour charge while stopped
ec2-state-diff-instance-store-data
  claim: Data on instance store volumes is preserved by a reboot but erased by a stop, a hibernate and a terminate.
  scope: instance store volumes.
  link: [The data is preserved](../facts/ec2.md#ec2-state-diff-instance-store-data)
  link: [The data is erased](../facts/ec2.md#ec2-state-diff-instance-store-data)
  say: a reboot keeps instance store data | stop, hibernate and terminate erase instance store data
ec2-state-diff-root-volume
  claim: The root volume is preserved by a reboot, a stop and a hibernate; on terminate it is deleted by default.
  scope: EBS root volume; default; terminate deletes it only while DeleteOnTermination is true.
  link: [The volume is preserved](../facts/ec2.md#ec2-state-diff-root-volume)
  link: [The volume is deleted by default](../facts/ec2.md#ec2-state-diff-root-volume)
  link: [deleted by default](../facts/ec2.md#ec2-state-diff-root-volume)
ec2-faq-instance-store-for-temporary-data
  claim: AWS recommends the local instance store for temporary data, and EBS volumes or backups to Amazon S3 for data that needs higher durability.
  scope: instance store and EBS data placement.
  link: [use the local instance store for temporary data](../facts/ec2.md#ec2-faq-instance-store-for-temporary-data)
  link: [using Amazon EBS volumes or backing up](../facts/ec2.md#ec2-faq-instance-store-for-temporary-data)
  say: instance store is for temporary data | durable data: EBS or a backup to S3
ec2-stop-start-moves-host-loses-instance-store
  claim: When you start a stopped instance it is moved to a new host computer (in some cases it remains on the current host), and any data on the instance store volumes of the previous host is lost.
  scope: EBS-backed instances.
  link: [moved to a new host computer](../facts/ec2.md#ec2-stop-start-moves-host-loses-instance-store)
  link: [you lose any data on the instance store](../facts/ec2.md#ec2-stop-start-moves-host-loses-instance-store)
ec2-retirement-ebs-stop-instance-store-terminate
  claim: When AWS detects irreparable failure of the underlying host, it schedules the instance to stop if it has an EBS root volume, or to terminate if it has an instance store root volume.
  scope: scheduled instance retirement; depends on the root volume type.
  link: [irreparable failure of the underlying host](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  link: [the instance is scheduled to stop](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  link: [the instance is scheduled to terminate](../facts/ec2.md#ec2-retirement-ebs-stop-instance-store-terminate)
  say: when the host fails for good | an EBS root instance is stopped | an instance store root instance is terminated
ec2-volume-attachment-limit-by-type-and-size
  claim: The maximum number of EBS volumes that can be attached to an instance depends on the instance type and instance size; exceeding it fails with AttachmentLimitExceeded.
  scope: per instance.
  link: [depends on the instance type and instance size](../facts/ec2.md#ec2-volume-attachment-limit-by-type-and-size)
  say: it depends on instance type and size
ec2-nitro-shared-attachment-limit-28
  claim: Most Nitro instances support at most 28 attachments shared between EBS volumes, network interfaces and NVMe instance store volumes, so an m5.xlarge with only the primary network interface can attach 27 EBS volumes.
  scope: per instance; maximum; not adjustable; Nitro instance types with a shared volume limit; some newer types have a dedicated EBS volume limit that varies by size.
  link: [maximum of 28 attachments](../facts/ec2.md#ec2-nitro-shared-attachment-limit-28)
  link: [you can attach 27 EBS volumes](../facts/ec2.md#ec2-nitro-shared-attachment-limit-28)
  say: twenty-eight attachments on most Nitro instances | twenty-seven EBS volumes with one network interface
ec2-hibernate-saves-ram-to-root-volume
  claim: Hibernation signals the operating system to suspend to disk, which saves the contents of RAM to the EBS root volume; when the instance starts again the root volume is restored, the RAM contents are reloaded and the instance keeps its instance ID.
  scope: hibernated EBS-backed instances.
  link: [saves the contents from the instance memory (RAM)](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the RAM contents are reloaded](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the instance retains its instance ID](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  say: hibernation saves the RAM to the EBS root volume
ec2-hibernate-root-volume-requirements
  claim: Hibernation requires the root volume to be an EBS volume, not an instance store volume, and that root volume must be encrypted.
  scope: per instance.
  link: [EBS volume](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  link: [must be encrypted](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  say: EBS volume | must be encrypted
ec2-hibernate-ebs-volume-types
  claim: Hibernation supports only General Purpose SSD (gp2 and gp3) and Provisioned IOPS SSD (io1 and io2) EBS volume types.
  scope: per instance.
  link: [gp2 and gp3](../facts/ec2.md#ec2-hibernate-ebs-volume-types)
  link: [io1 and io2](../facts/ec2.md#ec2-hibernate-ebs-volume-types)
  say: gp two and gp three | io one and io two
ec2-faq-hibernate-stop-ebs-backed-only
  claim: Stop and hibernate are available only for Amazon EBS-backed instances, and local instance storage is not persisted.
  scope: stop and hibernate actions.
  link: [available for Amazon EBS backed instances only](../facts/ec2.md#ec2-faq-hibernate-stop-ebs-backed-only)
  link: [Local instance storage is not persisted](../facts/ec2.md#ec2-faq-hibernate-stop-ebs-backed-only)
  say: only EBS-backed instances | instance store data is lost
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
ec2-delete-on-termination-defaults
  claim: Each EBS volume has a DeleteOnTermination attribute; by default the root volume is deleted when the instance terminates and any other EBS volume is preserved.
  scope: per EBS volume attached to an instance; default; adjustable.
  link: [The default is to delete the root volume](../facts/ec2.md#ec2-delete-on-termination-defaults)
  link: [DeleteOnTermination](../facts/ec2.md#ec2-delete-on-termination-defaults)
  link: [preserve any other EBS volumes](../facts/ec2.md#ec2-delete-on-termination-defaults)
  say: by default the root volume is deleted and other EBS volumes are kept | other EBS volumes are kept
ec2-root-volume-one-per-instance
  claim: Each instance has a single root volume, created at launch, that contains the image used to boot the instance; you can add storage volumes during or after launch.
  scope: per instance; fixed.
  link: [Each instance has a single root volume](../facts/ec2.md#ec2-root-volume-one-per-instance)
  link: [contains the image used to boot the instance](../facts/ec2.md#ec2-root-volume-one-per-instance)
ec2-create-ami-snapshots-all-ebs-volumes
  claim: Creating an EBS-backed AMI snapshots the root volume and every other attached EBS volume, and you are charged for those snapshots until you deregister the AMI and delete them; instance store data is not kept in the AMI.
  scope: EBS-backed AMI creation.
  link: [creates snapshots of your instance's root volume](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
  link: [You're charged for the snapshots](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
  link: [don't contain any data from the instance store](../facts/ec2.md#ec2-create-ami-snapshots-all-ebs-volumes)
ec2-ami-root-volume-types
  claim: Every AMI is either EBS-backed (root volume is an EBS volume created from a snapshot; Linux and Windows) or S3-backed (root volume is an instance store volume created from a template in S3; Linux only).
  scope: AMI root volume type.
  link: [created from an Amazon EBS snapshot](../facts/ec2.md#ec2-ami-root-volume-types)
  link: [a template stored in Amazon S3](../facts/ec2.md#ec2-ami-root-volume-types)
  link: [Windows AMIs do not support instance store](../facts/ec2.md#ec2-ami-root-volume-types)
  say: Windows cannot use an instance store root volume
ec2-s3-backed-ami-end-of-life
  claim: S3-backed (instance store-backed) AMIs are considered end of life, are not recommended for new use, and are supported only on older instance types (C1, C3, D2, I2, M1, M2, M3, R3 and X1).
  scope: Amazon S3-backed AMIs.
  link: [considered end of life](../facts/ec2.md#ec2-s3-backed-ami-end-of-life)
  link: [only supported on the following older instance types](../facts/ec2.md#ec2-s3-backed-ami-end-of-life)
  say: instance store backed AMIs are end of life
kms-ebs-encryption-status-fixed-at-create
  claim: An EBS volume's encryption status is set when the volume is created and cannot be changed; you can apply a new encryption status while copying a snapshot. Snapshots of encrypted volumes, and volumes made from them, are encrypted automatically.
  link: [cannot change the encryption status](../facts/kms.md#kms-ebs-encryption-status-fixed-at-create)
  link: [while copying a snapshot](../facts/kms.md#kms-ebs-encryption-status-fixed-at-create)
kms-unusable-key-ebs-attach-fails
  claim: Making a KMS key unusable has no immediate effect on an attached encrypted EBS volume, but after the volume is detached, the next attachment fails because EBS cannot decrypt the volume's data key.
  link: [no immediate effect on the EC2 instance](../facts/kms.md#kms-unusable-key-ebs-attach-fails)
  link: [the attachment fails](../facts/kms.md#kms-unusable-key-ebs-attach-fails)
kms-ebs-default-key-aws-ebs-or-cmk
  claim: Encryption by default is a Region-specific setting of your AWS account. When you enable it, you keep the AWS managed key aws/ebs as the default encryption key or choose a symmetric customer managed key.
  scope: per Region, per account; default; not adjustable.
  link: [the AWS managed key with the alias aws/ebs](../facts/kms.md#kms-ebs-default-key-aws-ebs-or-cmk)
  link: [a symmetric customer managed encryption key](../facts/kms.md#kms-ebs-default-key-aws-ebs-or-cmk)
kms-ebs-encryption-by-default-region-setting
  claim: EBS encryption by default is a Region-specific setting; once enabled for a Region, you cannot disable it for individual volumes or snapshots in that Region, and it has no effect on existing volumes or snapshots.
  link: [a Region-specific setting](../facts/kms.md#kms-ebs-encryption-by-default-region-setting)
  link: [no effect on existing EBS volumes or snapshots](../facts/kms.md#kms-ebs-encryption-by-default-region-setting)
efs-faq-use-case-file-vs-block-vs-object
  claim: EFS is a file storage service, Amazon EBS is a block-level storage service for use with EC2, and Amazon S3 is an object storage service.
  scope: EFS vs EBS vs S3.
  link: [file storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [block-level storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
  link: [object storage service](../facts/efs.md#efs-faq-use-case-file-vs-block-vs-object)
efs-decision-guide-block-row-single-instance
  claim: In the AWS storage decision guide table, block storage (Amazon EBS and the EC2 instance store) is for low-latency, high-performance durable storage attached to single Amazon EC2 instances or containers, such as databases.
  scope: storage type table of the decision guide.
  link: [attached to single Amazon EC2 instances or containers](../facts/efs.md#efs-decision-guide-block-row-single-instance)
ec2-auto-scaling-health-ebs-volumes-detached-on-terminate
  claim: When an instance is terminated, its EBS volumes are detached (or deleted, depending on DeleteOnTermination) and are not attached to the replacement; you attach them yourself or with a lifecycle hook.
  scope: per replaced instance.
  link: [attached EBS volumes are detached](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-volumes-detached-on-terminate)
  link: [lifecycle hook-based solution](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-volumes-detached-on-terminate)
ec2-recovery-simplified-not-instance-store
  claim: Simplified automatic recovery is not supported for instances that attach instance store volumes at launch; CloudWatch action based recovery supports them on selected instance types, and the instance store data is lost during recovery.
  scope: automatic instance recovery mechanisms; instance store volumes attached at launch.
  link: [Not supported for instances that attach instance store](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  link: [Supported on selected instance types](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  link: [data on instance store volumes is lost](../facts/ec2.md#ec2-recovery-simplified-not-instance-store)
  say: simplified recovery does not support instance store instances | CloudWatch recovery supports some of them | but the instance store data is lost
ec2-family-storage-optimized
  claim: Storage optimized instances are designed for workloads that need high, sequential read and write access to very large data sets on local storage, and they deliver tens of thousands of low-latency random I/O operations per second (IOPS).
  scope: storage optimized instance family.
  link: [high, sequential read and write access](../facts/ec2.md#ec2-family-storage-optimized)
  link: [very large data sets on local storage](../facts/ec2.md#ec2-family-storage-optimized)
  link: [low-latency, random I/O operations per second (IOPS)](../facts/ec2.md#ec2-family-storage-optimized)
  say: heavy sequential reads and writes | on large local storage | many fast random I O operations
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
