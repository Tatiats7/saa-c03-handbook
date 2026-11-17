facts card: 7 facts
ec2-hibernate-ram-limits-linux-windows
  claim: A Linux instance cannot be hibernated if it has more than 150 GiB of RAM, and a Windows instance cannot be hibernated if it has more than 16 GiB of RAM.
  scope: per instance; maximum; not adjustable; Linux 150 GiB; Windows 16 GiB.
  link: [150 GiB](../facts/ec2.md#ec2-hibernate-ram-limits-linux-windows)
  link: [16 GiB](../facts/ec2.md#ec2-hibernate-ram-limits-linux-windows)
  say: one hundred fifty gibibytes for Linux | sixteen gibibytes for Windows
ec2-hibernate-max-duration
  claim: An instance cannot stay hibernated for more than 60 days; to keep it longer you must start the hibernated instance, stop it and start it again.
  scope: per instance; maximum; not adjustable.
  link: [60 days](../facts/ec2.md#ec2-hibernate-max-duration)
  say: sixty days
ec2-hibernate-root-volume-requirements
  claim: Hibernation requires the root volume to be an EBS volume, not an instance store volume, and that root volume must be encrypted.
  scope: per instance.
  link: [EBS volume](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  link: [must be encrypted](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  say: EBS volume | must be encrypted
ec2-hibernate-supported-families-no-bare-metal
  claim: Hibernation needs an instance family that supports hibernation, and bare metal instances are not supported; the supported list covers general purpose families (including T2, T3, T3a, T4g and T8i), compute optimized, memory optimized and storage optimized families. Hibernation works with instances in all AWS Regions.
  scope: per instance.
  link: [bare metal instances are not supported](../facts/ec2.md#ec2-hibernate-supported-families-no-bare-metal)
  link: [all AWS Regions](../facts/ec2.md#ec2-hibernate-supported-families-no-bare-metal)
  say: no bare metal | every Region
ec2-hibernate-saves-ram-to-root-volume
  claim: Hibernation signals the operating system to suspend to disk, which saves the contents of RAM to the EBS root volume; when the instance starts again the root volume is restored, the RAM contents are reloaded and the instance keeps its instance ID.
  scope: hibernated EBS-backed instances.
  link: [saves the contents from the instance memory (RAM)](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the RAM contents are reloaded](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  link: [the instance retains its instance ID](../facts/ec2.md#ec2-hibernate-saves-ram-to-root-volume)
  say: hibernation saves the RAM to the EBS root volume
ec2-hibernate-no-instance-fee-ebs-rates
  claim: A hibernated instance is charged at standard EBS storage rates and, like a stopped instance, incurs no instance usage fee; any Elastic IP addresses associated with it are still charged.
  scope: per hibernated instance.
  link: [charged at standard EBS rates for storage](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  link: [you do not incur instance usage fees](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  link: [charged for any Elastic IP addresses](../facts/ec2.md#ec2-hibernate-no-instance-fee-ebs-rates)
  say: only EBS storage | Elastic IPs are still charged
ec2-spot-interruption-notice-two-minutes
  claim: A Spot Instance interruption notice is a warning issued two minutes before Amazon EC2 stops or terminates the Spot Instance; with hibernation as the interruption behavior you get the notice but not a two-minute warning, because hibernation begins immediately.
  scope: per Spot Instance; fixed; interruption notices are emitted on a best effort basis.
  link: [two minutes before Amazon EC2 stops or terminates your Spot Instance](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  link: [you do not receive a two-minute warning](../facts/ec2.md#ec2-spot-interruption-notice-two-minutes)
  say: a two-minute warning | no two-minute warning for hibernation
