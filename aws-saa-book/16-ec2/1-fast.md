---
id: "16"
slug: ec2
title: Amazon EC2
file: fast
tier: deep
xl: true
domains: [2, 3, 4]
tasks: ["2.2", "3.2", "3.4", "4.2"]
services: [ec2]
minutes: {fast: 20, pass: 80, full: 179}
status: ready
updated: 2026-10-13
---

# Amazon EC2

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** You buy a one-year Reserved Instance. If the Region later runs short of capacity, does AWS keep capacity free for your instance? <!-- gist-trap -->

**Predict 2.** An instance with a public IP address is stopped and then started. Does it keep the same public IP address?

**Predict 3.** An instance is already running. Can you turn on hibernation for it now?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read three instance types: their virtual CPUs (vCPUs), memory, processor architecture, and whether each type can burst or hibernate. Then read two Amazon Linux AMI IDs, a few bare metal types and your metadata defaults; the task creates nothing.

<!-- task:start id=ec2-t01 -->

Look

**It kills the belief.** "A Graviton instance can run the same AMI as an x86 instance."

> **Cost:** $0.

**Permissions.** `ec2:DescribeInstanceTypes`, `ssm:GetParameters`, `ec2:GetInstanceMetadataDefaults`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read the processor architecture, vCPUs, memory in MiB, burstable flag and hibernation flag of three instance types. If AWS says a type is not offered in this Region, remove that type and run again.

   ```bash
   aws ec2 describe-instance-types --instance-types t3.micro t4g.micro r6g.large --query "InstanceTypes[].[InstanceType,ProcessorInfo.SupportedArchitectures[0],VCpuInfo.DefaultVCpus,MemoryInfo.SizeInMiB,BurstablePerformanceSupported,HibernationSupported]" --output table
   ```

   Expect: Three rows, in any order. t3.micro shows x86_64. t4g.micro and r6g.large show arm64: the g after the generation number means AWS Graviton processors. The two t types show True for burstable, r6g.large shows False. All three show True for hibernation.

2. Read the two public parameters that point to the latest Amazon Linux 2023 AMI: one for x86_64 and one for arm64.

   ```bash
   aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64 /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-arm64 --query "Parameters[].[Name,Value]" --output table
   ```

   Expect: Two rows with two different AMI IDs. One operating system has two AMIs, one for each processor architecture. An x86_64 AMI does not fit t4g.micro, and an arm64 AMI does not fit t3.micro.

3. List a few bare metal instance types and their hibernation flag.

   ```bash
   aws ec2 describe-instance-types --filters Name=bare-metal,Values=true --query "InstanceTypes[].[InstanceType,HibernationSupported]" --max-items 6 --output table
   ```

   Expect: Six rows or fewer. In every name, the size after the period starts with metal, and every row shows False for hibernation.

4. Read the instance metadata defaults that this account sets for new instances in this Region.

   ```bash
   aws ec2 get-instance-metadata-defaults
   ```

   Expect: An AccountLevel block. It is empty when nobody set an account default here: each new instance then takes its settings from its launch settings or its AMI. If it shows HttpTokens required, new instances require IMDSv2 unless their launch settings say otherwise.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon EC2 rents [a virtual server in the AWS Cloud](../facts/ec2.md#ec2-instance-virtual-server-type-sets-hardware), billed [in a "running" state](../facts/ec2.md#ec2-faq-billing-running-state). Its instance type [determines the hardware available to your instance](../facts/ec2.md#ec2-instance-virtual-server-type-sets-hardware).

**The problem it solves.** Bought hardware sits idle after the peak. EC2 gives [on-demand, scalable computing capacity](../facts/ec2.md#ec2-concepts-elastic-scale-up-down): you launch [as many or as few virtual servers](../facts/ec2.md#ec2-concepts-elastic-scale-up-down) as you need from one Amazon Machine Image (AMI).

**Predict the picture.** When you launch an instance, which two choices decide its software and its hardware?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: a launch template, Amazon EC2, the instance, and the instance metadata service. The template names the AMI and the instance type, EC2 places the instance in a subnet in one zone, and the instance gets role credentials from the metadata service.](../diagrams/svg/ec2-hero.svg)

**Figure.** An instance starts from an AMI and an instance type, runs in one Availability Zone, and is billed while it runs.

1. You launch from a launch template that names the AMI, the instance type and the network settings.
2. Amazon EC2 places the instance in a subnet, which sits in one Availability Zone.
3. The AMI provides the software that the instance boots from.
4. The instance type determines the hardware that the instance gets.
5. Code on the instance gets temporary credentials of its role from the instance metadata service.
6. Billing runs for the seconds the instance is in the running state.

</details>

> **Startup example:** Callvale's single instance was installed by hand. Average CPU use is 9%, with peaks of 85% on weekday mornings. Administrators connect with SSH from any IP address. Callvale must launch identical instances in minutes, pay less for idle capacity, and close the administration port.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| instance | **launch** an instance | A virtual server that you run in Amazon EC2 | an AMI: the image that an instance starts from |
| terminate (TER-mih-nayt) | termination **protection** | To delete an instance permanently | stop: the instance can start again |
| instance store | an instance store **volume** | Temporary block storage on the host computer of an instance | EBS volume |
| ephemeral (ih-FEM-er-ul) | ephemeral **storage** | Temporary: the data is lost when the instance stops or ends | persistent |
| scale up | scale up the **database instance** | Move to a larger instance size | scale out: add more instances |
| scale out | scale out on a **metric** | Add more instances; the opposite is scale in | scale up: use a larger instance |
| Availability Zone | **across** Availability Zones | One or more separate data centers in a Region | Region |
| single point of failure | **remove** a single point of failure | One part whose failure stops the whole system | fault tolerance |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### EC2 or AWS Lambda or AWS Fargate

<!-- table: compare -->
| Question | EC2 | AWS Lambda | AWS Fargate |
|---|---|---|---|
| What do you manage? | The instances, with [granular control over the compute environment](../facts/ec2.md#ec2-compute-guide-ec2-overhead-justified-for-control) | Function code, [without the need to manage servers](../facts/ec2.md#ec2-compute-guide-lambda-no-servers) | Container tasks: you [run containers without having to manage servers](../facts/ec2.md#ec2-compute-guide-fargate-no-servers-for-containers) |
| How long can one run last? | As long as the instance runs | [15 minutes](../facts/lambda.md#lambda-faq-timeout-15-minutes) per invocation | Long work with [specific resource needs or persistent processes](../facts/lambda.md#lambda-choose-fargate-containers-persistent) |
| What does it fit? | Work that needs control of the operating system | [event-driven tasks, unpredictable workloads](../facts/lambda.md#lambda-choose-functions-event-driven-unpredictable) | Containers that you do not want to run on instances |

**Deciding question:** Must you control the operating system, does the work run longer than a Lambda function can, or does it run only when events arrive?

### On-Demand or Savings Plans or Spot

<!-- table: compare -->
| Question | On-Demand Instances | Savings Plans | Spot Instances |
|---|---|---|---|
| What do you commit to? | Nothing; billed per second with a [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum) | A steady spend per hour for a fixed term | Nothing |
| Largest discount? | None | [up to 72%](../facts/ec2.md#ec2-savings-plans-vs-ri-discounts-66-72) (EC2 Instance Savings Plans) | [up to 90%](../facts/ec2.md#ec2-spot-discount-up-to-90-percent) |
| Can EC2 take it back? | No | No | Yes, with [two minutes of notice](../facts/ec2.md#ec2-spot-only-difference-interruption-two-minutes) |
| Does it hold capacity? | No: purchasing options [determine how AWS calculates your bill](../facts/ec2.md#ec2-purchasing-vs-capacity-reservation-independent) | No: [Savings Plans do not provide a capacity reservation](../facts/ec2.md#ec2-faq-savings-plans-no-capacity-reservation) | No |
| What does it fit? | [short-term, irregular workloads that cannot be interrupted](../facts/ec2.md#ec2-on-demand-recommended-short-term-irregular) | Steady use, which will [benefit most from long-term commitments through Savings Plans](../facts/ec2.md#ec2-steady-state-savings-plans) | [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible) |

**Deciding question:** Can the work be interrupted, and will it run steadily for one to three years?

### Cluster or spread or partition placement group

<!-- table: compare -->
| Question | Cluster | Spread | Partition |
|---|---|---|---|
| Where do the instances sit? | Close together, for fast traffic between them | Instances [each placed on distinct hardware](../facts/ec2.md#ec2-placement-spread-critical-instances) | Each partition [has its own set of racks](../facts/ec2.md#ec2-placement-partition-separate-racks) |
| What is the limit? | All instances are [within a single Availability Zone](../facts/ec2.md#ec2-placement-cluster-single-az) | [seven running instances in each Availability Zone](../facts/ec2.md#ec2-placement-spread-max-7-running-per-az) | A [maximum of seven partitions per Availability Zone](../facts/ec2.md#ec2-placement-partition-max-7-per-az) |
| What does it fit? | [low network latency, high network throughput, or both](../facts/ec2.md#ec2-placement-cluster-recommended-traffic-between-instances) | [a small number of critical instances](../facts/ec2.md#ec2-placement-spread-critical-instances) | [large distributed and replicated workloads](../facts/ec2.md#ec2-placement-partition-distributed-workloads) |

**Deciding question:** Do the instances need to be close for speed, or apart so that one hardware fault cannot stop them all?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "can tolerate interruption" | Spot Instances | made for [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible) | the job is stateful or tightly coupled: On-Demand |
| "steady, predictable use for years" | a Savings Plan | steady work will [benefit most from long-term commitments through Savings Plans](../facts/ec2.md#ec2-steady-state-savings-plans) | capacity must be held too: add a Capacity Reservation |
| "licenses bound to sockets or cores" | Dedicated Hosts | [per-socket, per-core, or per-VM software licenses](../facts/ec2.md#ec2-dedicated-host-byol-per-socket-core) | the rule only keeps other accounts off the hardware: Dedicated Instances |
| "keep in-memory state; slow start-up" | hibernation | for applications that [take a long time to bootstrap](../facts/ec2.md#ec2-faq-hibernate-use-case-prewarm) | the instances are in an Auto Scaling group: a warm pool |
| "lowest latency between instances" | a cluster placement group | [low network latency, high network throughput, or both](../facts/ec2.md#ec2-placement-cluster-recommended-traffic-between-instances) | the instances must not fail together: spread |
| "standby with the same IP address" | move the network interface | it [maintains its private IP addresses, Elastic IP addresses](../facts/ec2.md#ec2-eni-hot-standby-failover) | the standby is in another zone: remap an Elastic IP address |
| "guaranteed capacity in one Availability Zone" | an On-Demand Capacity Reservation | holds capacity [in a specific Availability Zone for any duration](../facts/ec2.md#ec2-capacity-reservation-immediate-no-term) | GPUs for machine learning on future dates: Capacity Blocks |
| "no inbound ports, no SSH keys" | Session Manager | [without the need to open inbound ports](../facts/ec2.md#ec2-session-manager-no-inbound-ports-bastion-keys) | users need their own SSH client: EC2 Instance Connect Endpoint |

### Traps

- **Wrong belief:** A Savings Plan or a Reserved Instance holds capacity for you. **Truth:** [Savings Plans do not provide a capacity reservation](../facts/ec2.md#ec2-faq-savings-plans-no-capacity-reservation), and [a regional Reserved Instance does not reserve capacity](../facts/ec2.md#ec2-ri-capacity-reservation-zonal-only). [A zonal Reserved Instance reserves capacity](../facts/ec2.md#ec2-ri-capacity-reservation-zonal-only), and so does an On-Demand Capacity Reservation. <!-- trap: ec2-trap-reservation-holds-capacity -->
- **Wrong belief:** Spot is cheapest, so it fits any job. **Truth:** [Spot Instances can be interrupted by Amazon EC2](../facts/ec2.md#ec2-spot-only-difference-interruption-two-minutes), so Spot does not suit work that is [inflexible, stateful, fault-intolerant, or tightly coupled](../facts/ec2.md#ec2-spot-not-suitable-stateful-inflexible). <!-- trap: ec2-trap-spot-for-uninterruptible -->
- **Wrong belief:** A stop and start keeps the public IPv4 address. **Truth:** [The instance gets a new public IPv4 address](../facts/ec2.md#ec2-state-diff-public-ipv4). An Elastic IP address [remains associated with the instance](../facts/ec2.md#ec2-state-diff-elastic-ip). <!-- trap: ec2-trap-stop-keeps-public-ip -->
- **Wrong belief:** You can hibernate any running instance. **Truth:** You turn hibernation on only [when you launch it](../facts/ec2.md#ec2-hibernate-enable-only-at-launch). The root volume is an [EBS volume](../facts/ec2.md#ec2-hibernate-root-volume-requirements) that [must be encrypted](../facts/ec2.md#ec2-hibernate-root-volume-requirements). <!-- trap: ec2-trap-hibernate-any-instance -->
- **Wrong belief:** A Dedicated Instance fits licenses that count cores. **Truth:** A Dedicated Host shows [the number of sockets and physical cores](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility); Dedicated Instances show [no visibility](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility). <!-- trap: ec2-trap-dedicated-instance-for-byol -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2024-02-01) Every public IPv4 address has a charge.<br>
> **Old:** an in-use public IPv4 address had [No charge](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02).<br>
> **Now:** [AWS charges for all public IPv4 addresses](../facts/ec2.md#ec2-change-public-ipv4-charge-2024-02), in use or idle.<br>
> **The exam probably expects:** older questions treat an Elastic IP address on a running instance as free. Prefer an option that is right under both rules.<br>
> **Status:** examinable.

> **Changed recently:** (2026-02-16) Nested virtualization on virtual instances.<br>
> **Old:** not available.<br>
> **Now:** you can run hypervisors [inside virtualized Amazon EC2 instances](../facts/ec2.md#ec2-change-nested-virtualization-2026-02).<br>
> **The exam probably expects:** older questions put a hypervisor on a bare metal instance. Prefer an option that is right under both rules.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A worker keeps scratch files on an instance store volume and hibernates for the night. Are the files there in the morning?

<details>
<summary>Answer</summary>

No. Hibernation saves the memory, but instance store data is lost when the instance is [stopped, hibernated, or terminated](../facts/instance-store.md#instance-store-data-persists-reboot-not-stop).

**Predict 1:** Only if it is zonal: [a regional Reserved Instance does not reserve capacity](../facts/ec2.md#ec2-ri-capacity-reservation-zonal-only).

</details>

**Check 2.** A nightly simulation can restart, but its nodes share state and must all run together. Do Spot Instances fit it?

<details>
<summary>Answer</summary>

No. Spot does not suit work that is [inflexible, stateful, fault-intolerant, or tightly coupled](../facts/ec2.md#ec2-spot-not-suitable-stateful-inflexible).

**Predict 2:** No. [The instance gets a new public IPv4 address](../facts/ec2.md#ec2-state-diff-public-ipv4).

</details>

**Check 3.** A web tier in an Auto Scaling group loads a large cache at start-up. Can its instances hibernate at night?

<details>
<summary>Answer</summary>

No. Hibernation is not possible for an instance in an [Auto Scaling group or used by Amazon ECS](../facts/ec2.md#ec2-hibernate-not-in-auto-scaling-group). A warm pool of the group fits instead.

**Predict 3:** No. Hibernation is turned on [when you launch it](../facts/ec2.md#ec2-hibernate-enable-only-at-launch).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which purchasing option fits work that can be interrupted?

<details>
<summary>Answer</summary>

Spot Instances, for [stateless, fault-tolerant, flexible applications](../facts/ec2.md#ec2-spot-recommended-stateless-fault-tolerant-flexible).

</details>

**Recap 2.** Which placement group keeps a few critical instances on distinct hardware?

<details>
<summary>Answer</summary>

A spread placement group: instances are [each placed on distinct hardware](../facts/ec2.md#ec2-placement-spread-critical-instances).

</details>

**Recap 3.** A license counts the physical cores of the server. Which option shows them: a Dedicated Instance or a Dedicated Host?

<details>
<summary>Answer</summary>

A Dedicated Host: it shows [the number of sockets and physical cores](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility). A Dedicated Instance gives [no visibility](../facts/ec2.md#ec2-dedicated-host-socket-core-visibility).

</details>
