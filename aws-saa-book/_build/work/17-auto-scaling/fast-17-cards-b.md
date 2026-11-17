facts card: 35 facts
ec2-auto-scaling-health-elb-check-must-be-turned-on
  claim: The Elastic Load Balancing health check type checks whether the load balancer reports the instance as healthy and able to handle requests; you must turn it on for the group.
  scope: per Auto Scaling group; default; adjustable.
  link: [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
  link: [Elastic Load Balancing health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on)
ec2-auto-scaling-faq-suspend-health-checks
  claim: You can temporarily suspend EC2 Auto Scaling health checks with the SuspendProcesses API, for example to inspect an unhealthy instance, and resume them with ResumeProcesses.
  scope: per Auto Scaling group (scaling processes).
  link: [SuspendProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
  link: [ResumeProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
ec2-auto-scaling-standby-no-lb-traffic
  claim: A Standby instance remains part of the group but does not handle load balancer traffic, and the group will not terminate it through health checks or scale-in events.
  scope: per instance in Standby.
  link: [do not actively handle load balancer traffic](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
  link: [during scale-in events](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times
  claim: Both scheduled and predictive scaling implement time-based supply; predictive scaling scales out from observed patterns, while scheduled scaling scales out at times you define in advance.
  scope: AWS Well-Architected guidance.
  link: [Predictive scaling uses patterns to scale out](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times)
  link: [scheduled scaling uses pre-defined times to scale out](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-predictive-patterns-vs-scheduled-times)
ec2-auto-scaling-faq-target-tracking-definition
  claim: With target tracking you select a load metric such as CPU utilization or request count and set a target value; EC2 Auto Scaling then adjusts the number of instances to maintain that target, like a home thermostat.
  scope: per target tracking scaling policy.
  link: [adjusts the number of EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-definition)
  link: [home thermostat](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-definition)
ec2-auto-scaling-sqs-backlog-per-instance
  claim: Backlog per instance is the queue length (ApproximateNumberOfMessages) divided by the number of InService instances; the target tracking target is the acceptable backlog per instance.
  scope: per Auto Scaling group that processes an Amazon SQS queue.
  link: [backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [Divide that number by the fleet's running capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
  link: [acceptable backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance)
ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies
  claim: In the AWS example of an Auto Scaling group that processes images from an SQS queue, a fixed-size group works if the upload rate does not vary; if the number of uploads changes over time, AWS suggests dynamic scaling of the group.
  scope: per Auto Scaling group that processes an SQS queue; the number of uploads changes over time.
  link: [you might consider using dynamic scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-dynamic-scaling-when-load-varies)
ec2-auto-scaling-warm-pool-definition
  claim: A warm pool is a pool of pre-initialized EC2 instances beside an Auto Scaling group; on scale out the group draws on the pool, and instances count toward desired capacity only as they leave the pool.
  scope: per warm pool.
  link: [pool of pre-initialized EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
  link: [count toward the desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition)
ec2-auto-scaling-warm-pool-unnecessary-cost
  claim: Creating a warm pool when it is not required can lead to unnecessary costs: if first boot time does not cause noticeable latency issues for the application, you probably do not need a warm pool.
  scope: per warm pool.
  link: [can lead to unnecessary costs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-unnecessary-cost)
ec2-auto-scaling-spot-price-capacity-optimized-recommended
  claim: For Spot Instances in a mixed instances group, AWS recommends the price-capacity-optimized allocation strategy: it chooses the Spot pools that are least likely to be interrupted and have the lowest possible price.
  scope: per Auto Scaling group with Spot Instances.
  link: [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
  link: [least likely to be interrupted](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended)
ec2-spot-not-suitable-stateful-inflexible
  claim: Spot Instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes.
  scope: Spot Instances.
  link: [inflexible, stateful, fault-intolerant, or tightly coupled](../facts/ec2.md#ec2-spot-not-suitable-stateful-inflexible)
  say: not for stateful, inflexible or tightly coupled work
ec2-auto-scaling-instance-refresh-use-cases
  claim: An instance refresh can help you deploy a new AMI or user data script across the group, migrate instances to new instance types, or switch a group from a launch configuration to a launch template.
  scope: per instance refresh.
  link: [Deploying a new Amazon Machine Image (AMI)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-use-cases)
  link: [roll out the updates immediately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-use-cases)
ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes
  claim: To roll out code changes to multiple instances in a group, use AWS CodeDeploy or CloudFormation.
  scope: per Auto Scaling group (code deployment).
  link: [AWS CodeDeploy or CloudFormation](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes)
ec2-auto-scaling-termination-hook-extends-life
  claim: A termination lifecycle hook extends the life of an instance already selected for termination, giving time to finish in-progress work or save it and transfer it to another instance.
  scope: per termination lifecycle hook.
  link: [extends the life of your Amazon EC2 instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-extends-life)
  link: [transfer the work to another instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-extends-life)
ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice
  claim: A lifecycle hook does not prevent a Spot Instance from terminating when capacity is no longer available, which can happen at any time with a two-minute interruption notice.
  scope: per Spot Instance in an Auto Scaling group.
  link: [two-minute interruption notice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice)
  link: [does not prevent an instance from terminating](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice)
  say: two-minute interruption notice
ec2-auto-scaling-elb-health-checks-ignored-by-default
  claim: By default, Amazon EC2 Auto Scaling ignores the results of Elastic Load Balancing health checks.
  scope: per Auto Scaling group; default; adjustable.
  link: [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default)
  say: ignores the load balancer health checks
ec2-auto-scaling-lb-default-ec2-checks-only
  claim: By default EC2 Auto Scaling replaces only instances that are unhealthy or unreachable by the Amazon EC2 health checks; with Elastic Load Balancing health checks turned on it can also replace a running instance that an attached load balancer reports as unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [only replaces instances that are unhealthy or unreachable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
  link: [report it as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
ec2-auto-scaling-termination-az-balance-first
  claim: EC2 Auto Scaling always balances instances across Availability Zones first, whatever termination policy is used, so some newer instances can be terminated before older ones.
  scope: per Auto Scaling group during scale in.
  link: [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
  link: [regardless of which termination policy is used](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
ec2-auto-scaling-termination-default-zone-with-most
  claim: With the default termination policy, EC2 Auto Scaling first picks the Availability Zone with the most instances that also has at least one instance not protected from scale in.
  scope: per Auto Scaling group during scale in.
  link: [has the most instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-zone-with-most)
  link: [at least one instance that is not protected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-zone-with-most)
ec2-auto-scaling-termination-default-outdated-first
  claim: The default termination policy of an Auto Scaling group is designed to terminate instances that use outdated configurations first; you can change the policy.
  scope: per Auto Scaling group; default; adjustable.
  link: [terminate instances that are using outdated configurations first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-outdated-first)
ec2-auto-scaling-termination-default-billing-hour-then-random
  claim: After the outdated-configuration check, the default termination policy picks the instance closest to the next billing hour, and chooses at random among instances that are equally close.
  scope: per Auto Scaling group during scale in.
  link: [closest to the next billing hour](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-billing-hour-then-random)
  link: [terminate one at random](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-billing-hour-then-random)
ec2-auto-scaling-termination-policy-oldest-instance
  claim: The OldestInstance termination policy terminates the oldest instance in the group; it is useful when you move the group to a new EC2 instance type.
  scope: per Auto Scaling group during scale in.
  link: [OldestInstance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
  link: [Terminate the oldest instance in the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
ec2-auto-scaling-cannot-hibernate-group-instance
  claim: You cannot hibernate an instance that is in an Auto Scaling group: if you try, Auto Scaling marks the stopped instance unhealthy and might terminate it and launch a replacement.
  scope: per instance in an Auto Scaling group.
  link: [You can't hibernate an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance)
ec2-auto-scaling-warm-pool-hibernated-ram
  claim: A Hibernated warm pool instance saves its RAM contents to the EBS root volume; while hibernated you pay only for EBS volumes (including the RAM storage) and Elastic IP addresses.
  scope: per warm pool.
  link: [save the contents of your RAM](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-hibernated-ram)
  link: [pay only for the EBS volumes](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-hibernated-ram)
ec2-auto-scaling-warm-pool-states
  claim: Warm pool instances can be kept in one of three states: Stopped, Running or Hibernated; keeping them Stopped is an effective way to minimize costs, because you pay only for the volumes and the attached Elastic IP addresses.
  scope: per warm pool.
  link: [Stopped, Running, or Hibernated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
  link: [pay only for the volumes that you use](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
  link: [an effective way to minimize costs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-states)
ec2-auto-scaling-faq-data-not-copied-to-new-instances
  claim: Data is not automatically copied from existing instances to new instances the group launches; use lifecycle hooks to copy data, or an Amazon RDS database with replicas.
  scope: per newly launched instance.
  link: [Data is not automatically copied](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-data-not-copied-to-new-instances)
  link: [lifecycle hooks to copy the data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-data-not-copied-to-new-instances)
ec2-auto-scaling-faq-persist-data-off-instance
  claim: If data on an instance must survive scale-in, store it off the instance in a service such as S3, RDS or DynamoDB.
  scope: per instance data that must survive scale in.
  link: [S3, RDS, or DynamoDB](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-persist-data-off-instance)
  link: [stored off the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-persist-data-off-instance)
ec2-auto-scaling-faq-regional-spans-azs-not-regions
  claim: An Auto Scaling group is a Regional construct: it can span Availability Zones, but not Regions.
  scope: per Auto Scaling group.
  link: [regional constructs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-regional-spans-azs-not-regions)
  link: [can span Availability Zones, but not AWS regions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-regional-spans-azs-not-regions)
elb-unhealthy-target-stop-resume
  claim: When the load balancer detects an unhealthy target it stops routing traffic to it, and it resumes routing when the target is healthy again.
  scope: registered target.
  link: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
  link: [resumes routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
ec2-auto-scaling-launch-configurations-blocked-for-new-accounts
  claim: An account created on or after October 1, 2024 cannot create a launch configuration by any method (console, API, AWS CLI, or CloudFormation).
  scope: per account, by account creation date.
  link: [October 1, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts)
  link: [cannot create new launch configurations using any method](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts)
ec2-auto-scaling-launch-config-immutable
  claim: A launch configuration cannot be modified after it is created; to change it you create a new launch configuration and update the group, and a group uses only one launch configuration at a time.
  scope: per launch configuration.
  link: [can't modify a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
  link: [only specify one launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
  link: [must create a launch configuration](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-config-immutable)
ec2-auto-scaling-change-price-capacity-optimized-2022
  claim: The price-capacity-optimized Spot allocation strategy was added on November 10, 2022; it requests Spot Instances from the pools least likely to be interrupted that also have the lowest possible price, and AWS now recommends it when you are getting started.
  scope: per Auto Scaling group with Spot Instances.
  link: [November 10, 2022](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-price-capacity-optimized-2022)
  link: [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-price-capacity-optimized-2022)
ec2-auto-scaling-change-predictive-forecasts-every-six-hours
  claim: Since January 6, 2023, predictive scaling forecasts update every six hours instead of daily.
  scope: per predictive scaling policy.
  link: [update every six hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours)
  link: [daily](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours)
  changed: 2023-01-06: was daily
ec2-auto-scaling-quota-groups-per-region
  claim: An account can have 500 Auto Scaling groups per Region by default.
  scope: per Region, per account; default; adjustable.
  link: [500 Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-groups-per-region)
  say: five hundred Auto Scaling groups
ec2-auto-scaling-suspend-processes-purpose
  claim: Suspending processes lets you investigate or troubleshoot without interference from scaling policies or scheduled actions, and stops EC2 Auto Scaling from marking instances unhealthy and replacing them while you change the group.
  scope: per Auto Scaling group (scaling processes).
  link: [investigate or troubleshoot an issue without interference](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
  link: [marking instances unhealthy and replacing them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
