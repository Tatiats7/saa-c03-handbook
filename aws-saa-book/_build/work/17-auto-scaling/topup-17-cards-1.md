facts card: 17 facts
ec2-auto-scaling-faq-works-with-alb-nlb-health-checks
  claim: EC2 Auto Scaling works with Application Load Balancers and Network Load Balancers, including their health check feature.
  scope: per Auto Scaling group with a load balancer.
  link: [including their health check feature](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-works-with-alb-nlb-health-checks)
ec2-auto-scaling-health-cannot-remove-ec2-checks
  claim: The EC2 status checks and scheduled events cannot be removed from a group's health checks; to stop replacements, AWS recommends suspending the ReplaceUnhealthy and HealthCheck processes.
  scope: per Auto Scaling group (health checks).
  link: [does not provide a way of removing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-cannot-remove-ec2-checks)
  link: [suspend the `ReplaceUnhealthy` and `HealthCheck` process](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-cannot-remove-ec2-checks)
ec2-auto-scaling-faq-elb-requests-before-detection-fail
  claim: When ELB notices that an instance is unhealthy it stops routing requests to it, but before it discovers that the instance is unhealthy, some requests to that instance fail.
  scope: per Auto Scaling group with a load balancer.
  link: [some requests to that instance will fail](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
  link: [stop routing requests to it](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-elb-requests-before-detection-fail)
ec2-auto-scaling-process-replace-unhealthy
  claim: The ReplaceUnhealthy process terminates instances marked unhealthy and launches new instances to replace them.
  scope: per Auto Scaling group (scaling processes).
  link: [ReplaceUnhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-replace-unhealthy)
  link: [Terminates instances that are marked as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-process-replace-unhealthy)
ec2-auto-scaling-faq-suspend-health-checks
  claim: You can temporarily suspend EC2 Auto Scaling health checks with the SuspendProcesses API, for example to inspect an unhealthy instance, and resume them with ResumeProcesses.
  scope: per Auto Scaling group (scaling processes).
  link: [SuspendProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
  link: [ResumeProcesses](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-suspend-health-checks)
ec2-auto-scaling-health-not-running-immediate
  claim: If EC2 Auto Scaling detects that an instance is no longer in the running state, it treats this as an immediate failure, marks the instance Unhealthy at once and replaces it.
  scope: per Auto Scaling group (health checks).
  link: [treated as an immediate failure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-not-running-immediate)
  link: [immediately marks the instance as `Unhealthy`](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-not-running-immediate)
ec2-auto-scaling-standby-no-health-checks
  claim: EC2 Auto Scaling does not perform health checks on an instance in Standby; its health status stays what it was before standby until you return it to service.
  scope: per instance in Standby.
  link: [does not perform health checks](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-health-checks)
  link: [health status reflects the status](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-health-checks)
ec2-auto-scaling-standby-no-lb-traffic
  claim: A Standby instance remains part of the group but does not handle load balancer traffic, and the group will not terminate it through health checks or scale-in events.
  scope: per instance in Standby.
  link: [do not actively handle load balancer traffic](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
  link: [during scale-in events](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-no-lb-traffic)
ec2-auto-scaling-standby-preferred-over-detach
  claim: To take an instance out of a group temporarily, AWS recommends the standby procedure rather than detaching and re-attaching it to the same group.
  scope: per instance in Standby.
  link: [recommend using the standby procedure](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-preferred-over-detach)
  link: [Instead of detaching and re-attaching an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-preferred-over-detach)
ec2-auto-scaling-standby-still-managed
  claim: An instance in Standby is still managed by the Auto Scaling group but is not an active part of the application until you return it to service.
  scope: per instance in Standby.
  link: [continue to be managed](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-still-managed)
  link: [not an active part of your application](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-still-managed)
ec2-auto-scaling-standby-billed
  claim: You are billed for instances that are in a standby state.
  scope: per instance in Standby.
  link: [You are billed for instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-billed)
  link: [standby state](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-billed)
ec2-auto-scaling-standby-decrement-choice
  claim: When you put an instance on standby you choose whether to decrement desired capacity; if you do not, EC2 Auto Scaling launches a replacement instance, and if you do, no replacement is launched.
  scope: per instance in Standby.
  link: [launches an instance to replace the one](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-decrement-choice)
  link: [prevents the launch of an instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-standby-decrement-choice)
ec2-auto-scaling-suspend-processes-purpose
  claim: Suspending processes lets you investigate or troubleshoot without interference from scaling policies or scheduled actions, and stops EC2 Auto Scaling from marking instances unhealthy and replacing them while you change the group.
  scope: per Auto Scaling group (scaling processes).
  link: [investigate or troubleshoot an issue without interference](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
  link: [marking instances unhealthy and replacing them](../facts/ec2-auto-scaling.md#ec2-auto-scaling-suspend-processes-purpose)
ec2-auto-scaling-vertical-stop-required
  claim: You must stop an EBS-backed instance before you can change its instance type, so plan for downtime while the instance is stopped.
  scope: per EBS-backed EC2 instance.
  link: [You must stop your instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stop-required)
  link: [plan for downtime](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stop-required)
ec2-auto-scaling-decision-guide-horizontal-for-fluctuating
  claim: The AWS compute decision guide calls horizontal scalability (adding instances) essential for dynamic workloads with fluctuating demand.
  scope: AWS compute decision guide.
  link: [essential for dynamic workloads with fluctuating demands](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-horizontal-for-fluctuating)
ec2-auto-scaling-wa-stateless-servers-replaceable
  claim: Well-Architected REL05-BP06: a system that keeps no state on local disk or memory between requests lets servers be replaced at will without an availability impact.
  scope: AWS Well-Architected guidance.
  link: [replaced at will without causing an availability impact](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-servers-replaceable)
ec2-auto-scaling-vertical-stopped-group-instance-unhealthy
  claim: If you stop an instance in an Auto Scaling group to change its type, EC2 Auto Scaling marks it unhealthy and might replace it; suspend the scaling processes to prevent this.
  scope: per instance in an Auto Scaling group.
  link: [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
  link: [suspend the scaling processes for the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stopped-group-instance-unhealthy)
