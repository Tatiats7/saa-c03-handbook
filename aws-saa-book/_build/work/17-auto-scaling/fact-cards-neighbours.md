facts card: 25 facts
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
ec2-resize-must-stop-instance
  claim: You must stop an EBS-backed instance before you can change its instance type, so you plan for downtime while it is stopped.
  scope: an Amazon EBS-backed instance; the new instance type is compatible with the current configuration.
  link: [You must stop your instance](../facts/ec2.md#ec2-resize-must-stop-instance)
  link: [before you can change its instance type](../facts/ec2.md#ec2-resize-must-stop-instance)
  link: [plan for downtime](../facts/ec2.md#ec2-resize-must-stop-instance)
  say: you must stop the instance first | before you change its instance type | plan for downtime
ec2-resize-change-instance-type
  claim: If an EC2 instance is too big or too small for its workload, you can resize it by changing its instance type, and AWS Compute Optimizer can recommend the instance type best able to handle the workload.
  scope: EC2 instance resizing; the new type must be compatible with the current configuration.
  link: [resize your instance by changing its instance type](../facts/ec2.md#ec2-resize-change-instance-type)
  link: [you can use AWS Compute Optimizer](../facts/ec2.md#ec2-resize-change-instance-type)
  say: change the instance type | Compute Optimizer suggests the type
ec2-spot-recommended-stateless-fault-tolerant-flexible
  claim: AWS recommends Spot Instances for stateless, fault-tolerant, flexible applications, such as big data, containerized workloads, CI/CD, stateless web servers, high performance computing (HPC) and rendering.
  scope: Spot Instances.
  link: [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  link: [big data, containerized workloads, CI/CD](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible)
  say: Spot is for stateless, fault-tolerant, flexible applications
ec2-spot-rebalance-recommendation-earlier-signal
  claim: A rebalance recommendation is a signal that a Spot Instance is at elevated risk of interruption; it can arrive sooner than the two-minute interruption notice, but it is not always sent first and can arrive together with the notice.
  scope: Spot Instances.
  link: [at elevated risk of interruption](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  link: [The signal can arrive sooner](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  link: [can arrive along with the two-minute interruption notice](../facts/ec2.md#ec2-spot-rebalance-recommendation-earlier-signal)
  say: a rebalance recommendation warns of elevated interruption risk | it can come before the two-minute notice
ec2-spot-be-flexible-types-and-azs
  claim: A Spot best practice is to be flexible about which instance types you request and in which Availability Zones you deploy, which gives Spot a better chance to find the capacity you need.
  scope: Spot Instances.
  link: [flexible about which instance types you request](../facts/ec2.md#ec2-spot-be-flexible-types-and-azs)
  say: be flexible about instance types and Availability Zones
ec2-faq-hibernate-vs-stop-ram
  claim: Hibernate persists the RAM data; stop shuts the instance down and clears RAM. In both cases data on the EBS root volume and attached EBS data volumes persists.
  scope: hibernate compared with stop.
  link: [the RAM data persisted](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  link: [RAM is cleared](../facts/ec2.md#ec2-faq-hibernate-vs-stop-ram)
  say: hibernate keeps RAM | stop clears RAM
ec2-faq-hibernate-trigger-stopinstances
  claim: Hibernation must be enabled at launch; it is then triggered with the StopInstances API and its Hibernate parameter.
  scope: hibernation of an instance.
  link: [StopInstances API with an additional ‘Hibernate’ parameter](../facts/ec2.md#ec2-faq-hibernate-trigger-stopinstances)
  say: StopInstances with Hibernate
ec2-user-data-runs-at-first-launch-by-default
  claim: By default, user data scripts and cloud-init directives run only during the boot cycle of the first launch; you can configure them to run at every restart.
  scope: per instance; default; adjustable; the configuration can be changed to run at every restart.
  link: [run only during the boot cycle](../facts/ec2.md#ec2-user-data-runs-at-first-launch-by-default)
  say: only at the first boot, by default
ec2-on-demand-billing-per-second-60s-minimum
  claim: On-Demand Instances are billed only for the seconds they are in the running state, with a 60-second minimum.
  scope: per On-Demand Instance; minimum.
  link: [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [You pay only for the seconds](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  link: [are in the running state](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum)
  say: a sixty-second minimum | only for the seconds the instance is running | while running
ec2-recovery-simplified-enabled-by-default
  claim: Simplified automatic recovery is enabled by default when an instance is launched; CloudWatch action based recovery is optional and you configure it after launch. A recovery mechanism must be configured before a system status check fails.
  scope: per instance; default; adjustable; supported instances only.
  link: [simplified automatic recovery is enabled during instance launch](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  link: [optionally configure Amazon CloudWatch action based recovery](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  link: [configured in advance](../facts/ec2.md#ec2-recovery-simplified-enabled-by-default)
  say: simplified automatic recovery is on by default | CloudWatch action based recovery is optional | set it up before a failure
ec2-recovery-system-status-check-only
  claim: Automatic instance recovery recovers an instance that fails a system status check (a host hardware or software problem); it does not operate when only the instance status check fails.
  scope: automatic instance recovery.
  link: [fails a system status check](../facts/ec2.md#ec2-recovery-system-status-check-only)
  link: [if only the instance status check fails](../facts/ec2.md#ec2-recovery-system-status-check-only)
  say: it recovers after a failed system status check | not when only the instance status check fails
ec2-spot-discount-up-to-90-percent
  claim: Spot Instances use spare EC2 capacity at a discount of up to 90% compared with On-Demand prices.
  scope: per Spot Instance; maximum; spare EC2 capacity; the Spot price varies with supply and demand.
  link: [up to 90%](../facts/ec2.md#ec2-spot-discount-up-to-90-percent)
  say: up to ninety percent off On-Demand
ec2-spot-not-suitable-stateful-inflexible
  claim: Spot Instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes.
  scope: Spot Instances.
  link: [inflexible, stateful, fault-intolerant, or tightly coupled](../facts/ec2.md#ec2-spot-not-suitable-stateful-inflexible)
  say: not for stateful, inflexible or tightly coupled work
elb-routes-only-to-healthy-targets
  claim: Elastic Load Balancing monitors the health of its registered targets and routes traffic only to the healthy targets.
  scope: Elastic Load Balancing.
  link: [monitors the health of its registered targets](../facts/elb.md#elb-routes-only-to-healthy-targets)
  link: [routes traffic only to the healthy targets](../facts/elb.md#elb-routes-only-to-healthy-targets)
elb-unhealthy-target-stop-resume
  claim: When the load balancer detects an unhealthy target it stops routing traffic to it, and it resumes routing when the target is healthy again.
  scope: registered target.
  link: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
  link: [resumes routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume)
elb-alb-fail-open-all-unhealthy
  claim: If an ALB target group contains only unhealthy targets, the load balancer routes requests to all of them regardless of health: when all targets fail health checks at once in all enabled Availability Zones, the load balancer fails open.
  scope: Application Load Balancer target group; all registered targets unhealthy.
  link: [routes requests to all those targets](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
  link: [the load balancer fails open](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
elb-deregistration-delay-default-300-seconds
  claim: The deregistration delay of an Application, Network or Gateway Load Balancer target group is 300 seconds by default and can be set from 0 to 3600 seconds.
  scope: per target group (Application, Network and Gateway Load Balancers); default; adjustable.
  link: [300 seconds](../facts/elb.md#elb-deregistration-delay-default-300-seconds)
  link: [0 to 3600 seconds](../facts/elb.md#elb-deregistration-delay-default-300-seconds)
  say: three hundred seconds | zero to three thousand six hundred seconds
elb-node-per-enabled-az
  claim: When you enable an Availability Zone for a load balancer, Elastic Load Balancing creates a load balancer node in that Availability Zone.
  scope: per enabled Availability Zone.
  link: [creates a load balancer node](../facts/elb.md#elb-node-per-enabled-az)
  link: [in the Availability Zone](../facts/elb.md#elb-node-per-enabled-az)
elb-alb-sticky-sessions-what
  claim: Sticky sessions (session affinity) bind a user's session to a specific target so that all of the user's requests in the session go to the same target; the client must support cookies.
  scope: Application Load Balancer target group.
  link: [also known as session affinity](../facts/elb.md#elb-alb-sticky-sessions-what)
  link: [bind a user's session to a specific target](../facts/elb.md#elb-alb-sticky-sessions-what)
  link: [the client must support cookies](../facts/elb.md#elb-alb-sticky-sessions-what)
elb-alb-health-check-interval-default-30-seconds
  claim: The Application Load Balancer health check interval can be 5 to 300 seconds; the default is 30 seconds for instance or ip targets and 35 seconds for lambda targets.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [30 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  link: [35 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  link: [5 to 300 seconds](../facts/elb.md#elb-alb-health-check-interval-default-30-seconds)
  say: thirty seconds | thirty-five seconds | five to three hundred seconds
elb-alb-unhealthy-threshold-default-2
  claim: An Application Load Balancer target is considered unhealthy after 2 consecutive failed health checks by default; the range is 2 to 10.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [2 consecutive failed health checks](../facts/elb.md#elb-alb-unhealthy-threshold-default-2)
  link: [2 to 10](../facts/elb.md#elb-alb-unhealthy-threshold-default-2)
  say: two consecutive failed health checks | two to ten
elb-new-target-after-first-health-check
  claim: On Application Load Balancers and Network Load Balancers, the load balancer starts routing to a newly registered target as soon as registration completes and the target passes the first initial health check, irrespective of the configured threshold.
  scope: newly registered target, Application and Network Load Balancers.
  link: [passes the first initial health check](../facts/elb.md#elb-new-target-after-first-health-check)
  link: [irrespective of the configured threshold](../facts/elb.md#elb-new-target-after-first-health-check)
elb-alb-slow-start-30-to-900-seconds-default-off
  claim: Slow start for an Application Load Balancer target group can be set from 30 to 900 seconds (15 minutes); the default is 0 seconds, which means slow start is disabled.
  scope: per Application Load Balancer target group; default; adjustable.
  link: [30 to 900 seconds](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  link: [15 minutes](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  link: [0 seconds (disabled)](../facts/elb.md#elb-alb-slow-start-30-to-900-seconds-default-off)
  say: thirty to nine hundred seconds | fifteen minutes | zero seconds, disabled
