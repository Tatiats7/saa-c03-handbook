---
id: "17"
slug: auto-scaling
title: EC2 Auto Scaling
file: fast
tier: deep
domains: [2, 3, 4]
tasks: ["3.2", "2.1", "4.2", "2.2"]
services: [ec2-auto-scaling, aws-auto-scaling]
minutes: {fast: 20, pass: 76, full: 171}
status: ready
updated: 2026-10-13
---

# EC2 Auto Scaling

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** An application behind a load balancer stops answering requests, but its instance keeps running. Does EC2 Auto Scaling replace the instance? <!-- gist-trap -->

**Predict 2.** Traffic rises at 09:00 every weekday. Can the group have new instances ready before 09:00, or only after the traffic arrives?

**Predict 3.** Can you hibernate the instances of an Auto Scaling group at night to save cost?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and list the termination policies and the scaling processes that EC2 Auto Scaling offers. Then read the group quota of your account; the task creates nothing.

<!-- task:start id=auto-scaling-t01 -->

Look

**It kills the belief.** "On scale in, the group terminates its oldest instance first."

> **Cost:** $0.

**Permissions.** `autoscaling:DescribeTerminationPolicyTypes`, `autoscaling:DescribeScalingProcessTypes`, `autoscaling:DescribeAccountLimits`, `autoscaling:DescribeAutoScalingGroups`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. List the termination policies that EC2 Auto Scaling offers. A termination policy picks the instance that goes first when a group scales in.

   ```bash
   aws autoscaling describe-termination-policy-types
   ```

   Expect: Seven names: AllocationStrategy, ClosestToNextInstanceHour, Default, NewestInstance, OldestInstance, OldestLaunchConfiguration and OldestLaunchTemplate. Default and OldestInstance are two different entries: OldestInstance is a policy that you choose for a group, not the default.

2. List the scaling processes of a group. You can suspend each process, for example to investigate a problem without the group launching or replacing instances.

   ```bash
   aws autoscaling describe-scaling-process-types --query "Processes[].ProcessName" --output text
   ```

   Expect: One line of names, among them Launch, Terminate, HealthCheck, ReplaceUnhealthy, AZRebalance, AlarmNotification and ScheduledActions.

3. Read the Auto Scaling quotas of this account in this Region.

   ```bash
   aws autoscaling describe-account-limits
   ```

   Expect: Four numbers. NumberOfAutoScalingGroups is how many groups this account has in this Region now, and MaxNumberOfAutoScalingGroups is how many it can have. Compare MaxNumberOfAutoScalingGroups with the default quota in the chapter. The quota is adjustable, so your account can show a different value.

4. List the groups of this Region with their minimum, desired and maximum sizes and their first termination policy.

   ```bash
   aws autoscaling describe-auto-scaling-groups --query "AutoScalingGroups[].[AutoScalingGroupName,MinSize,DesiredCapacity,MaxSize,TerminationPolicies[0]]" --output table
   ```

   Expect: A table, or nothing if this Region has no group. A group whose termination policy nobody changed shows Default in the last column, not OldestInstance.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon EC2 Auto Scaling is a [fully managed service](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-definition) that launches and terminates EC2 instances to keep the right number running for the load.

**The problem it solves.** A fixed fleet is too large at night and too small at peak. With a desired capacity, EC2 Auto Scaling [ensures that your group has this many instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-desired-capacity-maintained).

**Predict the picture.** When traffic rises, what decides to add an instance, and what launches it?

<details>
<summary>Show the picture</summary>

![An architecture with users on the left, an Application Load Balancer, and an Auto Scaling group across two Availability Zones with one instance in each and a new instance starting. A CloudWatch alarm and a scaling policy sit above the group; a launch template sits beside it. Numbered arrows show the path.](../diagrams/svg/auto-scaling-hero.svg)

**Figure.** A policy changes the desired capacity, and the group launches, registers and replaces instances to keep that number.

1. CloudWatch alarms that the target tracking policy manages watch the group's metric.
2. When the metric moves away from the target, the policy [adjusts the desired capacity of the group](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scaling-policy-adjusts-desired).
3. The group launches a new instance from its launch template in [the Availability Zone with the fewest instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-in-az-with-fewest).
4. With a load balancer, the group [registers your instance with the load balancer before it marks the instance as InService](../facts/ec2-auto-scaling.md#ec2-auto-scaling-registers-with-lb-before-inservice).
5. The group [terminates the unhealthy instance and launches another](../facts/ec2-auto-scaling.md#ec2-auto-scaling-unhealthy-terminated-replaced) when an instance fails a check that the group uses: EC2 checks, and ELB checks after you turn them on.

</details>

> **Startup example:** Callvale's web tier needs 3 instances at night and up to 12 at peak. The peak comes every weekday from 09:00 to 11:00. A new instance needs 4 minutes before it serves traffic. Callvale must replace failed instances automatically and must not pay for 12 instances all day.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| Auto Scaling group | **set** the desired capacity | A group of instances that AWS keeps at a wanted size | load balancer |
| scale out | scale out on a **metric** | To add more instances; the opposite is scale in | scale up |
| scale up | scale up the database **instance** | To move to a larger instance size | scale out |
| health check (HELTH chek) | **fail** a health check | A repeated test that shows whether a target can serve requests | status check |
| stateless (STAYT-less) | a stateless application **tier** | Keeps no memory of earlier requests | serverless |
| desired capacity | **raise** the desired capacity | The number of instances the group tries to keep running | maximum capacity |
| single point of failure | **remove** a single point of failure | One part whose failure stops the whole system | bottleneck, which slows the system |
| lifecycle hook | **complete** a lifecycle action | A pause at launch or termination, so that your code can act | health check grace period |

## Choose it or not (4 min)
<!-- section: role=choose; route=fast; minutes=4 -->

### Which Auto Scaling service

<!-- table: compare -->
| Question | EC2 Auto Scaling | Application Auto Scaling | AWS Auto Scaling |
|---|---|---|---|
| What does it scale? | EC2 instances in Auto Scaling groups | ECS services and [provisioned read and write capacity for Amazon DynamoDB](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-application-auto-scaling-for-non-ec2) | It can [scale collections of related resources](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-definition) |
| Which policies? | Target tracking, step, simple, scheduled and predictive | [Target tracking scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-aas-policy-types), step, scheduled and predictive | Target tracking, and predictive scaling that [only generates schedules for EC2 instances](../facts/aws-auto-scaling.md#aws-auto-scaling-faq-predictive-ec2-only-in-plans) |
| Choose it when | You [only need to scale Amazon EC2 Auto Scaling](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling) groups | One other service: [for other AWS services, use Application Auto Scaling](../facts/aws-auto-scaling.md#aws-auto-scaling-wa-ec2-auto-scaling-for-instances-application-auto-scaling-for-other-services) | You scale [multiple resources across multiple services](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-use-ec2-vs-aws-auto-scaling) |

**Deciding question:** Does only an EC2 fleet scale, one other AWS resource, or several resources of one application together?

### Scale out or scale up

<!-- table: compare -->
| Question | Scale out (horizontal) | Scale up (vertical) |
|---|---|---|
| How? | Add instances to a group | [Resize your instance by changing its instance type](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-resize-instance-type) |
| Downtime? | Stateless servers are [replaced at will without causing an availability impact](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-servers-replaceable) | [You must stop your instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-vertical-stop-required) first, so plan for downtime |
| Fluctuating demand? | [Essential for dynamic workloads with fluctuating demands](../facts/ec2-auto-scaling.md#ec2-auto-scaling-decision-guide-horizontal-for-fluctuating) | One size all day |
| What does the application need? | Stateless applications, because [they can scale horizontally](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-stateless-scales-horizontally) | No change |

**Deciding question:** Can the application run as several identical copies, or must one instance grow?

### Which scaling method

<!-- table: compare -->
| Question | Target tracking | Scheduled action | Predictive scaling |
|---|---|---|---|
| When does it act? | [When the metric deviates from the target](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-service-manages-alarms) | At a date and time it sets [desired, minimum, and maximum capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-action-sets-capacities) | It can [proactively increase capacity ahead of upcoming demand](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-predictive-ahead-of-demand) |
| When does it fit? | The load changes at unexpected times | [The need arises on a predictable schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use) | Apps that [take a long time to initialize](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-long-initialization-fit) |
| Does it scale in? | Yes, [scaling in more gradually when traffic is decreasing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-target-tracking-scale-in-gradual) | Yes, when a later action lowers the numbers | No: [it will not scale in to remove capacity](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-does-not-scale-in) |
| What does it need? | A metric that falls as instances are added | A schedule | [At least 24 hours of data](../facts/ec2-auto-scaling.md#ec2-auto-scaling-predictive-needs-24-hours-of-data) |

**Deciding question:** Is the load change a surprise, a known time, or a pattern that repeats?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "instances fail the load balancer health checks but are never replaced" | Elastic Load Balancing (ELB) health check type | [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on) | the group has no load balancer: a custom health check |
| "traffic rises at the same time every weekday" | scheduled action plus target tracking | [the need arises on a predictable schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use) | the time moves, but the pattern repeats: predictive scaling |
| "keep average CPU utilization at 50%" | target tracking policy | it [adjusts the number of EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-target-tracking-definition) | the work waits in a queue: backlog per instance |
| "workers process queue messages at a varying rate" | target tracking on backlog per instance | the target is the [acceptable backlog per instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-sqs-backlog-per-instance) | the rate never changes: a fixed-size group |
| "instances take a long time to initialize" | warm pool | a [pool of pre-initialized EC2 instances](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-definition) | first boot is fast: a warm pool [can lead to unnecessary costs](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-unnecessary-cost) |
| "lowest cost for interruptible stateless workers" | Spot; an On-Demand base only if some must keep running | AWS recommends the [price and capacity optimized allocation strategy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-spot-price-capacity-optimized-recommended) | the work is stateful: On-Demand |
| "roll out a new AMI to every instance" | new template version plus instance refresh | it helps with [deploying a new Amazon Machine Image (AMI)](../facts/ec2-auto-scaling.md#ec2-auto-scaling-instance-refresh-use-cases) | only code changes: [AWS CodeDeploy or CloudFormation](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-codedeploy-cloudformation-for-changes) |
| "finish a job before termination" | termination lifecycle hook | it [extends the life of your Amazon EC2 instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-hook-extends-life) | a Spot interruption: act on the [two-minute interruption notice](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lifecycle-hook-spot-two-minute-notice) |

### Traps

- **Wrong belief:** A group replaces the instances that fail the load balancer's health checks. **Truth:** By default, the group [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default) checks. <!-- trap: auto-scaling-trap-elb-checks-on-by-default -->
- **Wrong belief:** Scale in removes the oldest instance first. **Truth:** The group [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first). The default policy then tries to [terminate instances that are using outdated configurations first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-default-outdated-first). [OldestInstance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-policy-oldest-instance) is a policy that you choose. <!-- trap: auto-scaling-trap-oldest-terminated-first -->
- **Wrong belief:** You can hibernate the instances of a group at night. **Truth:** The group [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance) and can replace it. Hibernated instances wait in a warm pool instead. <!-- trap: auto-scaling-trap-hibernate-group-instance -->
- **Wrong belief:** A new instance starts with the data of the running instances. **Truth:** [Data is not automatically copied](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-data-not-copied-to-new-instances). Keep data [stored off the instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-persist-data-off-instance). <!-- trap: auto-scaling-trap-new-instance-data-copied -->
- **Wrong belief:** One group can span two Regions for disaster recovery. **Truth:** A group [can span Availability Zones, but not AWS regions](../facts/ec2-auto-scaling.md#ec2-auto-scaling-faq-regional-spans-azs-not-regions). <!-- trap: auto-scaling-trap-group-spans-regions -->
## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2023-01-06) How often predictive scaling updates its forecast.<br>
> **Old:** forecasts were updated [daily](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours).<br>
> **Now:** forecasts [update every six hours](../facts/ec2-auto-scaling.md#ec2-auto-scaling-change-predictive-forecasts-every-six-hours).<br>
> **The exam probably expects:** either value; it rarely decides an answer, and a forecast still needs history first.<br>
> **Status:** examinable.

> **Changed recently:** (2024-10-01) Launch configurations in new accounts.<br>
> **Old:** accounts created on or after [June 1, 2023](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-console-blocked-2023) [cannot create new launch configurations using the console](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts).<br>
> **Now:** accounts created on or after [October 1, 2024](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts) [cannot create new launch configurations using any method](../facts/ec2-auto-scaling.md#ec2-auto-scaling-launch-configurations-blocked-for-new-accounts).<br>
> **The exam probably expects:** a launch template; older questions can show launch configurations.<br>
> **Status:** examinable.

## Check (1 min)
<!-- section: role=check; route=fast; minutes=1 -->

**Check 1.** Three instances behind an Application Load Balancer use default group settings. The application on one instance hangs. What happens to that instance?

<details>
<summary>Answer</summary>

It keeps running but gets no requests: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume). The group [only replaces instances that are unhealthy or unreachable](../facts/ec2-auto-scaling.md#ec2-auto-scaling-lb-default-ec2-checks-only) by the EC2 checks.

**Predict 1:** No. For the ELB health check type, [you must turn it on](../facts/ec2-auto-scaling.md#ec2-auto-scaling-health-elb-check-must-be-turned-on).

</details>

**Check 2.** A sale starts at 10:00, and target tracking runs on the group. Which number does a scheduled action at 09:45 raise to keep extra instances in service at 10:00?

<details>
<summary>Answer</summary>

The minimum. When you [use scheduled scaling and scaling policies together](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-plus-policies-together), target tracking keeps acting and can scale in a raised desired capacity before 10:00.

**Predict 2:** Before, with a scheduled action or predictive scaling.

</details>

**Check 3.** Instances must start fast, with their memory already loaded. Where can they wait?

<details>
<summary>Answer</summary>

In a warm pool, in the Hibernated state: the instances [save the contents of your RAM](../facts/ec2-auto-scaling.md#ec2-auto-scaling-warm-pool-hibernated-ram).

**Predict 3:** No. The group [marks the stopped instance as unhealthy](../facts/ec2-auto-scaling.md#ec2-auto-scaling-cannot-hibernate-group-instance).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which health checks does a group act on by default?

<details>
<summary>Answer</summary>

The EC2 checks. The group [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default) checks until you turn them on.

</details>

**Recap 2.** Which scaling method fits a load change at a known time?

<details>
<summary>Answer</summary>

A scheduled action, because [the need arises on a predictable schedule](../facts/ec2-auto-scaling.md#ec2-auto-scaling-scheduled-vs-dynamic-when-to-use).

</details>

**Recap 3.** On scale in, what does the group do first, whatever the termination policy?

<details>
<summary>Answer</summary>

It [always balances instances across Availability Zones first](../facts/ec2-auto-scaling.md#ec2-auto-scaling-termination-az-balance-first).

</details>
