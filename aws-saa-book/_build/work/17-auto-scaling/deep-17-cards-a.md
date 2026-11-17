facts card: 30 facts
ec2-auto-scaling-lifecycle-hook-abandon-continue
  claim: A lifecycle action ends with continue or abandon: at launch, continue puts the instance in service and abandon lets the group terminate and replace it; at termination both let the instance terminate, and abandon skips remaining hooks.
  scope: per lifecycle hook.
  link: [abandon indicates that your custom actions were unsuccessful](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-abandon-continue)
  link: [both abandon and continue allow the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-abandon-continue)
ec2-auto-scaling-scale-in-protection-not-health-replacement
  claim: Instance scale-in protection does not protect an instance from health check replacement when it fails health checks.
  scope: per instance with scale-in protection.
  link: [Health check replacement](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-not-health-replacement)
  link: [does not protect Auto Scaling instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-not-health-replacement)
ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual
  claim: Scale-in protection does not stop manual termination through the EC2 console, CLI or API; to protect group instances from manual termination, enable EC2 termination protection.
  scope: per instance with scale-in protection.
  link: [enable Amazon EC2 termination protection](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual)
  link: [To protect Auto Scaling instances from manual termination](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scale-in-protection-ec2-termination-protection-for-manual)
ec2-auto-scaling-faq-launch-configuration-change-existing-unaffected
  claim: When you change a group's launch configuration, new instances launch with the new configuration, but existing instances are not affected.
  scope: per Auto Scaling group that uses a launch configuration.
  link: [existing instances are not affected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-launch-configuration-change-existing-unaffected)
ec2-auto-scaling-instance-refresh-launch-before-terminate
  claim: During an instance refresh, if the minimum healthy percentage is 100 percent, EC2 Auto Scaling launches the new instances before terminating the old ones, so desired capacity is kept at all times.
  scope: per instance refresh.
  link: [Launch the new instances first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
  link: [minimum healthy percentage](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
  link: [100 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-launch-before-terminate)
ec2-auto-scaling-instance-refresh-one-at-a-time
  claim: To replace one instance at a time, set both the minimum and maximum healthy percentage of the instance refresh to 100 percent; the refresh then launches a new instance before terminating an old one.
  scope: per instance refresh.
  link: [100 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-one-at-a-time)
  say: one hundred percent
ec2-auto-scaling-instance-refresh-all-at-once
  claim: To replace all instances of the group at once, set the instance refresh minimum healthy percentage to 0 percent.
  scope: per instance refresh.
  link: [0 percent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-all-at-once)
  say: zero percent
ec2-auto-scaling-warm-pool-definition
  claim: A warm pool is a pool of pre-initialized EC2 instances beside an Auto Scaling group; on scale out the group draws on the pool, and instances count toward desired capacity only as they leave the pool.
  scope: per warm pool.
  link: [pool of pre-initialized EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
  link: [count toward the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
ec2-auto-scaling-vertical-stopped-group-instance-unhealthy
  claim: If you stop an instance in an Auto Scaling group to change its type, EC2 Auto Scaling marks it unhealthy and might replace it; suspend the scaling processes to prevent this.
  scope: per instance in an Auto Scaling group.
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
  link: [suspend the scaling processes for the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
ec2-auto-scaling-sqs-backlog-per-instance
  claim: Backlog per instance is the queue length (ApproximateNumberOfMessages) divided by the number of InService instances; the target tracking target is the acceptable backlog per instance.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [Divide that number by the fleet's running capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [acceptable backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
ec2-launch-template-versions-default
  claim: A launch template stores launch parameters such as the AMI ID, instance type and network settings in numbered versions; when you launch without naming a version, the default version is used, and the default version is the first version unless you set another one.
  scope: per launch template; default; adjustable; no version specified at launch.
  link: [the default version is used](../facts/ec2.md#ec2-launch-template-versions-default)
  link: [it's the first version of the launch template](../facts/ec2.md#ec2-launch-template-versions-default)
  say: without a version, the default version is used | the default is the first version unless you change it
ec2-auto-scaling-step-ranges-no-overlap-or-gap
  claim: The ranges of the step adjustments in a step scaling policy cannot overlap or leave a gap.
  scope: per step scaling policy.
  link: [can't overlap or have a gap](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-ranges-no-overlap-or-gap)
  say: can't overlap or have a gap
ec2-auto-scaling-lb-attach-target-group
  claim: For an Application, Network or Gateway Load Balancer you attach a target group to the Auto Scaling group, not the load balancer itself; a Classic Load Balancer is attached directly.
  scope: per Auto Scaling group with a load balancer.
  link: [attach a target group rather than](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-attach-target-group)
  link: [registered directly with the load balancer](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-attach-target-group)
ec2-auto-scaling-default-instance-warmup-not-on-by-default
  claim: The default instance warmup is not enabled by default; AWS strongly recommends enabling and configuring it to optimize target tracking and step scaling policies.
  scope: per Auto Scaling group; default; adjustable.
  link: [It is not enabled or configured by default.](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-not-on-by-default)
  link: [strongly recommend that you enable and configure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-instance-warmup-not-on-by-default)
ec2-auto-scaling-health-ebs-check-must-be-turned-on
  claim: The Amazon EBS health check type checks whether EBS volumes are reachable and pass I/O status checks; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [Amazon EBS health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
  link: [passing I/O status checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-ebs-check-must-be-turned-on)
ec2-auto-scaling-instance-refresh-retry-timeout
  claim: When an instance refresh cannot continue making replacements, because it is waiting to replace instances on standby or protected from scale in, or because the new instances do not pass their health checks, Amazon EC2 Auto Scaling keeps retrying for an hour; if the problem persists, the operation fails.
  scope: per instance refresh; maximum; not adjustable.
  link: [an hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-retry-timeout)
  say: an hour
ec2-auto-scaling-faq-termination-policy-and-instance-protection
  claim: A termination policy decides which instances EC2 Auto Scaling terminates first when it scales in; instance protection prevents EC2 Auto Scaling from selecting specific instances for termination when scaling in.
  scope: per Auto Scaling group during scale in.
  link: [termination policy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-termination-policy-and-instance-protection)
  link: [use instance protection to prevent](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-termination-policy-and-instance-protection)
ec2-auto-scaling-cooldown-elb-deregistration-300-seconds
  claim: By default, Elastic Load Balancing waits 300 seconds to complete deregistration (connection draining).
  scope: per load balancer deregistration; default; adjustable.
  link: [300 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cooldown-elb-deregistration-300-seconds)
  say: three hundred seconds
ec2-auto-scaling-max-instance-lifetime-min-one-day
  claim: The maximum instance lifetime must be at least 86,400 seconds (one day).
  scope: per Auto Scaling group; minimum; not adjustable; 0 clears a previously set value.
  link: [86,400 seconds](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-min-one-day)
  link: [at least 86,400 seconds (one day)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-max-instance-lifetime-min-one-day)
ec2-spot-discount-up-to-90-percent
  claim: Spot Instances use spare EC2 capacity at a discount of up to 90% compared with On-Demand prices.
  scope: per Spot Instance; maximum; spare EC2 capacity; the Spot price varies with supply and demand.
  link: [up to 90%](../facts/ec2.md#ec2-spot-discount-up-to-90-percent)
  say: up to ninety percent off On-Demand
ec2-auto-scaling-dynamic-target-tracking-definition
  claim: Target tracking scaling increases and decreases the group's current capacity based on a CloudWatch metric and a target value; it works similar to a thermostat: you select a temperature and the thermostat does the rest.
  scope: per target tracking scaling policy.
  link: [Target tracking scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-definition)
  link: [a Amazon CloudWatch metric and a target value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-dynamic-target-tracking-definition)
ec2-auto-scaling-cannot-hibernate-group-instance
  claim: You cannot hibernate an instance that is in an Auto Scaling group: if you try, Auto Scaling marks the stopped instance unhealthy and might terminate it and launch a replacement.
  scope: per instance in an Auto Scaling group.
  link: [You can't hibernate an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
ec2-auto-scaling-warm-pool-ebs-root-required
  claim: EC2 Auto Scaling can keep a warm pool instance Stopped or Hibernated only if its root device is an EBS volume; instance store-backed instances cannot be stopped or hibernated.
  scope: per warm pool.
  link: [only if it has an Amazon EBS volume](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-ebs-root-required)
  link: [cannot be stopped or hibernated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-ebs-root-required)
ec2-hibernate-root-volume-requirements
  claim: Hibernation requires the root volume to be an EBS volume, not an instance store volume, and that root volume must be encrypted.
  scope: per instance.
  link: [EBS volume](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  link: [must be encrypted](../facts/ec2.md#ec2-hibernate-root-volume-requirements)
  say: EBS volume | must be encrypted
ec2-faq-hibernate-vs-stop-ram
  claim: Hibernate persists the RAM data; stop shuts the instance down and clears RAM. In both cases data on the EBS root volume and attached EBS data volumes persists.
  scope: hibernate compared with stop.
  link: [the RAM data persisted](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  link: [RAM is cleared](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  say: hibernate keeps RAM | stop clears RAM
ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only
  claim: For stopped warm pool instances you pay only for the volumes and the attached Elastic IP addresses; keeping warm pool instances Running is possible but strongly discouraged because of the extra charges.
  scope: per warm pool.
  link: [pay only for the volumes that you use](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only)
  link: [highly discouraged](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-stopped-instances-pay-volumes-only)
ec2-auto-scaling-spot-capacity-optimized-pools
  claim: The capacity-optimized Spot allocation strategy launches into the pools with the most available capacity, using real-time capacity data, to reduce interruptions for workloads where restarting is expensive.
  scope: per Auto Scaling group with Spot Instances.
  link: [capacity-optimized](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-capacity-optimized-pools)
  link: [most available pools](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-capacity-optimized-pools)
ec2-auto-scaling-spot-price-capacity-optimized-recommended
  claim: For Spot Instances in a mixed instances group, AWS recommends the price-capacity-optimized allocation strategy: it chooses the Spot pools that are least likely to be interrupted and have the lowest possible price.
  scope: per Auto Scaling group with Spot Instances.
  link: [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
  link: [least likely to be interrupted](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
ec2-auto-scaling-faq-on-demand-base-spot-above
  claim: When combining purchase models, you can set the group's base capacity to be fulfilled by On-Demand Instances; as the group scales, anything beyond the base is fulfilled with only Spot Instances or with a specified percentage mix of On-Demand and Spot.
  scope: per Auto Scaling group.
  link: [base capacity be fulfilled with On-Demand instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-on-demand-base-spot-above)
  link: [specified percentage mix of On-Demand or Spot instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-on-demand-base-spot-above)
ec2-auto-scaling-multiple-policies-largest-desired-wins
  claim: When several scaling policies are active, each computes desired capacity independently and the group uses the largest value; for example 10 instances from target tracking and 8 from predictive scaling gives 10.
  scope: per Auto Scaling group with several scaling policies.
  link: [set to the maximum of those](../facts/ec2-auto-scaling.md#ec2-auto-scaling-multiple-policies-largest-desired-wins)
  say: set to the largest of those
