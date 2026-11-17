facts card: 20 facts
ec2-auto-scaling-termination-default-outdated-first
  claim: The default termination policy of an Auto Scaling group is designed to terminate instances that use outdated configurations first; you can change the policy.
  scope: per Auto Scaling group; default; adjustable.
  link: [terminate instances that are using outdated configurations first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-outdated-first)
ec2-auto-scaling-termination-az-balance-first
  claim: EC2 Auto Scaling always balances instances across Availability Zones first, whatever termination policy is used, so some newer instances can be terminated before older ones.
  scope: per Auto Scaling group during scale in.
  link: [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
  link: [regardless of which termination policy is used](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
ec2-auto-scaling-suspend-processes-purpose
  claim: Suspending processes lets you investigate or troubleshoot without interference from scaling policies or scheduled actions, and stops EC2 Auto Scaling from marking instances unhealthy and replacing them while you change the group.
  scope: per Auto Scaling group (scaling processes).
  link: [investigate or troubleshoot an issue without interference](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
  link: [marking instances unhealthy and replacing them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
ec2-auto-scaling-quota-groups-per-region
  claim: An account can have 500 Auto Scaling groups per Region by default.
  scope: per Region, per account; default; adjustable.
  link: [500 Auto Scaling groups](../facts/ec2-auto-scaling.md#ec2-auto-scaling-quota-groups-per-region)
  say: five hundred Auto Scaling groups
ec2-auto-scaling-termination-policy-oldest-instance
  claim: The OldestInstance termination policy terminates the oldest instance in the group; it is useful when you move the group to a new EC2 instance type.
  scope: per Auto Scaling group during scale in.
  link: [OldestInstance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
  link: [Terminate the oldest instance in the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance)
ec2-on-demand-billing-per-second-60s-minimum
  claim: On-Demand Instances are billed only for the seconds they are in the running state, with a 60-second minimum.
  scope: per On-Demand Instance; minimum.
  link: [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [You pay only for the seconds](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [are in the running state](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  say: a sixty-second minimum | only for the seconds the instance is running | while running
ec2-auto-scaling-pricing-page-no-additional-fees
  claim: Amazon EC2 Auto Scaling features have no additional fees beyond the fees for Amazon EC2, CloudWatch (for scaling policies) and the other AWS resources you use.
  scope: per account.
  link: [no additional fees](../facts/ec2-auto-scaling.md#ec2-auto-scaling-pricing-page-no-additional-fees)
  say: no additional fees
ec2-auto-scaling-ssm-parameter-sources
  claim: The AMI parameter in a launch template can be a parameter in your own account, a parameter shared from another account, or an AWS public parameter for a public AMI.
  scope: per launch template used by an Auto Scaling group.
  link: [a parameter shared from another AWS account](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-sources)
  link: [a public parameter for a public AMI](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-sources)
ec2-auto-scaling-health-unexpected-termination-replaced
  claim: When an instance terminates unexpectedly, for example from a Spot interruption or a manual termination, EC2 Auto Scaling launches a replacement to keep the desired capacity.
  scope: per Auto Scaling group (health checks).
  link: [terminates unexpectedly](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-unexpected-termination-replaced)
  link: [automatically launch a replacement instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-unexpected-termination-replaced)
ec2-auto-scaling-desired-capacity-maintained
  claim: If you set a desired capacity, EC2 Auto Scaling ensures the group has that many instances; scaling policies then launch or terminate instances as demand changes.
  scope: per Auto Scaling group.
  link: [ensures that your group has this many instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-capacity-maintained)
  link: [as demand on your application increases or decreases](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-capacity-maintained)
ec2-auto-scaling-faq-delete-group-terminates-instances
  claim: If you delete an Auto Scaling group that has running instances, the instances are terminated and the group is deleted.
  scope: per Auto Scaling group (deletion).
  link: [the instances will be terminated](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-delete-group-terminates-instances)
ec2-auto-scaling-billed-from-launch
  claim: You are billed for Auto Scaling instances as soon as they launch, including the time before they are in service.
  scope: per instance in an Auto Scaling group.
  link: [as soon as they are launched](../facts/ec2-auto-scaling.md#ec2-auto-scaling-billed-from-launch)
  link: [not yet in service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-billed-from-launch)
ec2-auto-scaling-faq-no-additional-fees
  claim: EC2 Auto Scaling fleet management and dynamic scaling carry no additional fees; EC2 and CloudWatch service fees apply and are billed separately.
  scope: per account; fixed.
  link: [no additional fees](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-additional-fees)
  link: [service fees apply and are billed separately](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-no-additional-fees)
  say: no additional fees
ec2-auto-scaling-target-tracking-predefined-metrics
  claim: Target tracking offers four predefined metrics: ASGAverageCPUUtilization, ASGAverageNetworkIn, ASGAverageNetworkOut and ALBRequestCountPerTarget; you can also use custom CloudWatch metrics.
  scope: per target tracking scaling policy.
  link: [ASGAverageCPUUtilization](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ASGAverageNetworkIn](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ASGAverageNetworkOut](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [ALBRequestCountPerTarget](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
  link: [either predefined metrics or custom metrics](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-predefined-metrics)
ec2-auto-scaling-target-tracking-creates-two-alarms
  claim: Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms of a target tracking policy; in the AWS SQS walkthrough, creating the policy creates two alarms: one for scaling out and one for scaling in.
  scope: per target tracking scaling policy (AWS SQS CLI example).
  link: [two alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  link: [one for scaling in](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  say: two alarms
ec2-auto-scaling-target-tracking-service-manages-alarms
  claim: With a target tracking policy, EC2 Auto Scaling creates and manages the CloudWatch alarms that start scaling when the metric moves away from the target.
  scope: per target tracking scaling policy.
  link: [creates and manages the CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-service-manages-alarms)
  link: [when the metric deviates from the target](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-service-manages-alarms)
ec2-auto-scaling-target-tracking-insufficient-data-no-scaling
  claim: When the target tracking metric is missing data points, the alarm goes to INSUFFICIENT_DATA and EC2 Auto Scaling cannot scale the group until new data points arrive.
  scope: per target tracking scaling policy.
  link: [cannot scale your group until new data points](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
  link: [INSUFFICIENT_DATA](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
ec2-auto-scaling-scheduled-unique-start-time
  claim: Each scheduled action in a group needs a unique time value; a call that schedules an action at a time already taken is rejected with an error.
  scope: per scheduled action.
  link: [must have a unique time value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
  link: [the call is rejected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
ec2-auto-scaling-target-tracking-do-not-edit-alarms
  claim: You should not create, edit or delete the CloudWatch alarms of a target tracking policy; EC2 Auto Scaling manages them and can edit, replace or delete them.
  scope: per target tracking scaling policy.
  link: [Do not create, edit, or delete](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-do-not-edit-alarms)
ec2-auto-scaling-scheduled-one-time-or-recurring
  claim: Scheduled actions can run one time only or on a recurring schedule described by a cron expression and a time zone.
  scope: per scheduled action.
  link: [scale one time only](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
  link: [on a recurring schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
  link: [specify a cron expression and a time zone](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-one-time-or-recurring)
