facts card: 13 facts
vpc-public-ipv4-hourly-in-use-or-idle
  claim: A public IPv4 address is billed at an hourly rate per address, calculated in one-second increments with a minimum of 60 seconds, and the price is the same whether the address is in use on a resource or idle in the account.
  scope: per public IPv4 address.
  link: [You pay an hourly rate for each public IPv4 address used by your AWS account](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [minimum of 60 seconds](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [The price is the same whether the public IPv4 address is in-use](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
ec2-change-public-ipv4-charge-2024-02
  claim: AWS charges for all public IPv4 addresses, including the public IPv4 addresses of running instances and Elastic IP addresses. Before February 1, 2024, an in-use public IPv4 address (Amazon-provided or Elastic IP) assigned to resources in your VPC had no charge, while an additional (secondary) Elastic IP address on a running EC2 instance and an idle Elastic IP address were already charged.
  scope: per public IPv4 address; the pre-2024 no-charge row covered in-use addresses assigned to resources in your VPC, not a secondary or idle Elastic IP.
  link: [AWS charges for all public IPv4 addresses](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02)
  link: [No charge](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02)
  say: every public IPv4 address is charged | an in-use public IPv4 address used to be free
  changed: 2024-02-01: was No charge
ec2-state-running-billed
  claim: An instance in the running state is ready for use and its instance usage is billed.
  scope: per instance.
  link: [The instance is running and ready for use](../facts/ec2.md#ec2-state-running-billed)
  link: [Billed](../facts/ec2.md#ec2-state-running-billed)
  say: running is the billed state | it is billed
ec2-faq-billing-running-state
  claim: Instance usage is billed for any time the instance is in the running state; to stop instance usage charges, stop or terminate the instance.
  scope: per instance.
  link: [in a "running" state](../facts/ec2.md#ec2-faq-billing-running-state)
  link: [Billing starts when an instance transitions into](../facts/ec2.md#ec2-faq-billing-running-state)
  say: billed while running | billing starts on the move to running
aws-auto-scaling-faq-free-cloudwatch-fees-apply
  claim: AWS Auto Scaling is free to use; because it is enabled by Amazon CloudWatch, service fees apply for CloudWatch and for your application resources, such as EC2 instances and Elastic Load Balancing load balancers.
  scope: per account; fixed.
  link: [free to use](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-free-cloudwatch-fees-apply)
  say: free to use
ec2-auto-scaling-scheduled-utc-default-time-zone
  claim: Recurring scheduled actions use UTC by default; you can set a local IANA time zone, and a location-based time zone adjusts automatically for Daylight Saving Time.
  scope: per recurring scheduled action; default; adjustable.
  link: [Coordinated Universal Time (UTC)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-utc-default-time-zone)
  link: [the action automatically adjusts for DST](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-utc-default-time-zone)
ec2-auto-scaling-scheduled-action-sets-capacities
  claim: A scheduled action sets the group's desired, minimum and maximum capacity at a specified date and time; you give a new desired capacity and optionally a new minimum and maximum.
  scope: per scheduled action.
  link: [desired, minimum, and maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
  link: [optionally a new minimum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities)
ec2-auto-scaling-default-no-policies-fixed-size
  claim: By default an Auto Scaling group has no scaling policy or scheduled action, so it keeps a fixed size: it maintains its desired capacity and replaces an instance that becomes unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [maintain a fixed size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-no-policies-fixed-size)
  link: [continues to maintain its desired capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-default-no-policies-fixed-size)
ec2-auto-scaling-target-tracking-no-manual-alarms
  claim: Target tracking policies remove the need to define CloudWatch alarms and scaling adjustments by hand; EC2 Auto Scaling handles them from the target you set.
  scope: per target tracking scaling policy.
  link: [remove the need to manually define CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-no-manual-alarms)
ec2-auto-scaling-step-simple-you-manage-alarms
  claim: With step scaling and simple scaling, you create and manage the CloudWatch alarms that start scaling.
  scope: per step scaling policy.
  link: [you create and manage the CloudWatch alarms](../facts/ec2-auto-scaling.md#ec2-auto-scaling-step-simple-you-manage-alarms)
ec2-auto-scaling-lb-default-ec2-checks-only
  claim: By default EC2 Auto Scaling replaces only instances that are unhealthy or unreachable by the Amazon EC2 health checks; with Elastic Load Balancing health checks turned on it can also replace a running instance that an attached load balancer reports as unhealthy.
  scope: per Auto Scaling group; default; adjustable.
  link: [only replaces instances that are unhealthy or unreachable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
  link: [report it as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only)
ec2-auto-scaling-min-max-never-crossed
  claim: An Auto Scaling group has a minimum size and a maximum size; EC2 Auto Scaling ensures the group never goes below the minimum and never goes above the maximum.
  scope: per Auto Scaling group.
  link: [never goes below this size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [never goes above this size](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [minimum number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
  link: [maximum number of instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-min-max-never-crossed)
ec2-auto-scaling-desired-within-min-max
  claim: The desired capacity must be equal to or greater than the minimum size and equal to or less than the maximum size of the group.
  scope: per Auto Scaling group.
  link: [within the range of your minimum and maximum](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-within-min-max)
  say: within the minimum and maximum
