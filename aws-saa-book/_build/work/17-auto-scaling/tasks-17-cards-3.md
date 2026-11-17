facts card: 7 facts
ec2-auto-scaling-scheduled-unique-start-time
  claim: Each scheduled action in a group needs a unique time value; a call that schedules an action at a time already taken is rejected with an error.
  scope: per scheduled action.
  link: [must have a unique time value](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
  link: [the call is rejected](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-unique-start-time)
ec2-auto-scaling-target-tracking-insufficient-data-no-scaling
  claim: When the target tracking metric is missing data points, the alarm goes to INSUFFICIENT_DATA and EC2 Auto Scaling cannot scale the group until new data points arrive.
  scope: per target tracking scaling policy.
  link: [cannot scale your group until new data points](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
  link: [INSUFFICIENT_DATA](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-insufficient-data-no-scaling)
ec2-auto-scaling-target-tracking-creates-two-alarms
  claim: Amazon EC2 Auto Scaling creates and manages the CloudWatch alarms of a target tracking policy; in the AWS SQS walkthrough, creating the policy creates two alarms: one for scaling out and one for scaling in.
  scope: per target tracking scaling policy (AWS SQS CLI example).
  link: [two alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  link: [one for scaling in](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-creates-two-alarms)
  say: two alarms
ec2-auto-scaling-termination-default-outdated-first
  claim: The default termination policy of an Auto Scaling group is designed to terminate instances that use outdated configurations first; you can change the policy.
  scope: per Auto Scaling group; default; adjustable.
  link: [terminate instances that are using outdated configurations first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-outdated-first)
ec2-auto-scaling-termination-az-balance-first
  claim: EC2 Auto Scaling always balances instances across Availability Zones first, whatever termination policy is used, so some newer instances can be terminated before older ones.
  scope: per Auto Scaling group during scale in.
  link: [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
  link: [regardless of which termination policy is used](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first)
ec2-auto-scaling-require-imdsv2-launch-template
  claim: For extra security, you can set your users' permissions to require the use of a launch template that requires IMDSv2.
  scope: per launch template used by an Auto Scaling group.
  link: [a launch template that requires IMDSv2](../facts/ec2-auto-scaling.md#ec2-auto-scaling-require-imdsv2-launch-template)
ec2-auto-scaling-ssm-parameter-needs-getparameters
  claim: To specify a Parameter Store parameter in a launch template you need ssm:GetParameters on that parameter, and anyone who uses the launch template also needs it so the value can be validated.
  scope: per launch template used by an Auto Scaling group.
  link: [ssm:GetParameters](../facts/ec2-auto-scaling.md#ec2-auto-scaling-ssm-parameter-needs-getparameters)
