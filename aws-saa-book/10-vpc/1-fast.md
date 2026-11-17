---
id: "10"
slug: vpc
title: Amazon VPC
file: fast
tier: deep
xl: true
domains: [1, 2, 3, 4]
tasks: ["1.1", "1.2", "2.2", "3.4", "4.4"]
services: [vpc]
minutes: {fast: 20, pass: 72, full: 172}
status: ready
updated: 2026-10-12
---

# Amazon VPC

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A **virtual private cloud** (vee-pee-SEE), or VPC, has an **internet gateway** attached. An **instance** in a new **subnet** (SUB-net) of that VPC has a public IP address. Can users on the internet reach the instance? <!-- gist-trap -->

**Predict 2.** Can one subnet cover two Availability Zones?

**Predict 3.** Instances in a private subnet upload large files to Amazon S3. Do they need a **NAT gateway** (NAT GAYT-way)?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read the default VPC of your **Region**, the geographic area that you work in. Find the default route, 0.0.0.0/0, to an internet gateway, and the subnet setting that gives each new instance a public IP address.

<!-- task:start id=vpc-t01 -->

Look

**It kills the belief.** "A new AWS account starts with a private network that you must open yourself."

> **Cost:** $0.

**Permissions.** `ec2:DescribeVpcs`, `ec2:DescribeRouteTables`, `ec2:DescribeSubnets`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Find the default VPC of the Region that CloudShell uses, and read its IPv4 CIDR block.

   ```bash
   aws ec2 describe-vpcs --filters Name=is-default,Values=true --query "Vpcs[].[VpcId,CidrBlock]"
   ```

   Expect: One VPC ID and the CIDR block 172.31.0.0/16. An empty list means that someone deleted the default VPC in this Region: use another Region, or stop here.

2. Copy the VPC ID from the output as <VPC_ID>. Read every route in the route tables of the default VPC.

   ```bash
   aws ec2 describe-route-tables --filters Name=vpc-id,Values=<VPC_ID> --query "RouteTables[].Routes[].[DestinationCidrBlock,GatewayId]"
   ```

   Expect: If nobody changed the default VPC: two routes, 172.31.0.0/16 with the target local, and 0.0.0.0/0 with a target that starts with igw-. The second route is the one that makes the default subnets public.

3. Read the default subnets: the Availability Zone of each one, and whether it gives each new instance a public IPv4 address.

   ```bash
   aws ec2 describe-subnets --filters Name=default-for-az,Values=true --query "Subnets[].[AvailabilityZone,MapPublicIpOnLaunch]"
   ```

   Expect: One row for each default subnet, each in a different Availability Zone, and each with true. The account did not start with a private network.

**Label.** checked against docs, not run in a real account. Checked 2026-10-12.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** A VPC is your own isolated network in a Region. A subnet [cannot span zones](../facts/vpc.md#vpc-subnet-single-az), and route tables decide where traffic goes.

**The problem it solves.** A web tier faces the internet, but a database does not. A **route table** (ROOT TAY-bul) decides which subnets reach the internet.

**Predict the picture.** Where does the NAT gateway go: next to the worker, or elsewhere?

<details>
<summary>Show the picture</summary>

![A VPC in one Region with an internet gateway. A public subnet holds a web instance and a NAT gateway. A private subnet holds a worker instance. Users reach the web instance through the internet gateway. The worker's requests go to the NAT gateway, then out through the internet gateway.](../diagrams/svg/vpc-hero.svg)

**Figure.** Route tables send a private subnet's internet traffic to a NAT gateway in a public subnet, and from there to the internet gateway.

1. A user's request reaches the internet gateway of the VPC.
2. The internet gateway delivers it to the web instance, which has a public IP address in a public subnet.
3. The worker in the private subnet sends a request to the internet, and its route table points to the NAT gateway.
4. The NAT gateway sends the request out through the internet gateway with its own public IP address.
5. Replies come back the same way, and no host on the internet can start a connection to the worker.

</details>

> **Startup example:** Callvale's web, worker and database instances run in the default VPC with public IP addresses. The database must not be reachable from the internet. The worker must still download software updates. Its large transfers to Amazon S3 must not pass through a NAT device.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| virtual private cloud (vee-pee-SEE) | **create** a VPC | Your own isolated network inside a Region | VPN, an encrypted link to another network |
| subnet (SUB-net) | **launch** an instance in a subnet | A range of VPC addresses in one **Availability Zone** | security group, a firewall |
| route table (ROOT TAY-bul) | **associate** a route table with a subnet | Rules that say where subnet traffic goes | root user |
| internet gateway | **attach** an internet gateway to a VPC | The VPC side of the connection to the internet | NAT gateway |
| NAT gateway (NAT GAYT-way) | **route** traffic through a NAT gateway | Lets private instances start connections out | internet gateway |
| security group | **reference** a security group in a rule | A **stateful** (STAYT-ful) firewall on a resource | network ACL |
| network ACL (NAK-ul) | **add** a deny rule to a network ACL | A **stateless** (STAYT-less) firewall at the subnet edge | security group |
| gateway endpoint | **add** a gateway endpoint to a route table | A route target for Amazon S3 or DynamoDB | **interface endpoint** |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### Security group or network ACL

<!-- table: compare -->
| Question | Security group | Network ACL |
|---|---|---|
| Where does it apply? | [Instance level](../facts/vpc.md#vpc-sg-vs-nacl-level) | [Subnet level](../facts/vpc.md#vpc-sg-vs-nacl-level) |
| Which rules? | [Allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type) | [Allow and deny rules](../facts/vpc.md#vpc-sg-vs-nacl-rule-type) |
| What about the reply? | [Automatically allowed (stateful)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic) | [Must be explicitly allowed (stateless)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic) |
| How are rules read? | [Evaluates all rules before deciding whether to allow traffic](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation) | [Evaluates rules in ascending order until a match for the traffic is found](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation) |

**Deciding question:** Do you need to deny a source, or only allow the traffic that you expect?

[The default network ACL allows all inbound and outbound traffic](../facts/vpc.md#vpc-nacl-every-subnet-associated). A new custom network ACL is different: its initial rules [block all inbound and outbound traffic](../facts/vpc.md#vpc-nacl-custom-initial-rules-block-all).

### NAT gateway or NAT instance

AWS prefers the NAT gateway, because [NAT gateways provide better availability, higher bandwidth, and requires less administrative effort](../facts/vpc.md#vpc-natgw-preferred-over-nat-instance).

<!-- table: compare -->
| Question | NAT gateway | NAT instance |
|---|---|---|
| Who maintains it? | [Managed by AWS](../facts/vpc.md#vpc-natgw-vs-instance-maintenance) | You: software updates and operating system patches |
| How available is it? | [Highly available](../facts/vpc.md#vpc-natgw-vs-instance-availability) in its Availability Zone | [Use a script to manage failover between instances](../facts/vpc.md#vpc-natgw-vs-instance-availability) |
| How much bandwidth? | [Scale up to 100 Gbps](../facts/vpc.md#vpc-natgw-vs-instance-bandwidth) | [Depends on the bandwidth of the instance type](../facts/vpc.md#vpc-natgw-vs-instance-bandwidth) |
| Security group on the device? | [You cannot associate security groups with NAT gateways](../facts/vpc.md#vpc-natgw-vs-instance-security-groups) | Yes, on the NAT instance itself |
| Port forwarding? | [Not supported](../facts/vpc.md#vpc-natgw-vs-instance-port-forwarding) | [Manually customize the configuration to support port forwarding](../facts/vpc.md#vpc-natgw-vs-instance-port-forwarding) |
| What do you pay for? | Hours, [each gigabyte of data that it processes](../facts/vpc.md#vpc-natgw-pricing-dimensions), and its public IPv4 address | Instance hours by type and size, and its public IPv4 address |

**Deciding question:** Does the design need port forwarding on the NAT device? If not, choose the NAT gateway.

### Which device carries outbound traffic

<!-- table: compare -->
| Question | NAT gateway | Gateway endpoint | Egress-only internet gateway |
|---|---|---|---|
| Where does the traffic go? | The internet, over IPv4 | Amazon S3 or DynamoDB | The internet, over IPv6 |
| What does the device itself charge? | Hours, and [each gigabyte of data that it processes](../facts/vpc.md#vpc-natgw-pricing-dimensions) | [There are no data processing or hourly charges for using Gateway Type VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge) | [No charge for an egress-only internet gateway](../facts/vpc.md#vpc-eigw-stateful-no-security-group), but data transfer is billed |
| Can the internet start a connection? | No: [connections must always be initiated from within the VPC containing the NAT gateway](../facts/vpc.md#vpc-natgw-connections-originate-inside-vpc) | No: it reaches AWS services, not the internet | No: it blocks connections that the internet starts |

**Deciding question:** Where is the traffic going, and over which IP version?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "block traffic from a specific IP address or range" | a deny rule in a network ACL | a security group has [allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type) | a same-subnet source: network ACLs [do not filter traffic between instances in the same subnet](../facts/vpc.md#vpc-faq-network-acl-same-subnet) |
| "instances in a private subnet must download updates from the internet" | a NAT gateway (a zonal one sits in a public subnet) | [NAT maps multiple private IPv4 addresses to a single public IPv4 address](../facts/vpc.md#vpc-nat-device-maps-many-to-one) | IPv6 traffic: an egress-only internet gateway |
| "private instances send large data to Amazon S3, MOST cost-effective" | a gateway endpoint for Amazon S3 in the same Region | you [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge) | on-premises access: an interface endpoint |
| "outbound internet access must survive an Availability Zone failure" | one NAT gateway per zone, or a regional one | if shared, [resources in the other Availability Zones lose internet access](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet) | a test environment: one gateway costs less |
| "the database must not be reachable from the internet" | a private subnet; allow only the app tier | a private subnet has no route to an internet gateway | admins need a shell: still private, add Session Manager |
| "the VPC is running out of IP addresses" | a secondary **CIDR block** (SY-der blok) and new subnets | you [cannot increase or decrease the size of an existing CIDR block](../facts/vpc.md#vpc-cidr-cannot-resize) | the VPC is still being designed: plan a larger block now |
| "identify which traffic to an instance is rejected" | VPC Flow Logs | records show accept or reject | packet contents matter: Traffic Mirroring |
| "requests arrive, but the replies never reach the clients" | an outbound network ACL rule for **ephemeral** (ih-FEM-er-ul) ports | [network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule) | no network ACL blocks it: check the routes |

### Traps

- **Wrong belief:** A security group can block one IP address. **Truth:** [You can specify allow rules, but not deny rules](../facts/vpc.md#vpc-sg-allow-rules-only). <!-- trap: vpc-trap-sg-deny -->
- **Wrong belief:** A network ACL lets replies out automatically. **Truth:** To cover every kind of client, [open ephemeral ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-open-1024-65535) outbound. <!-- trap: vpc-trap-nacl-reply -->
- **Wrong belief:** One NAT gateway is highly available for every zone. **Truth:** [Create a NAT gateway in each Availability Zone to ensure zone-independent architecture](../facts/vpc.md#vpc-natgw-vs-instance-availability), or a regional one. <!-- trap: vpc-trap-one-natgw-ha -->
- **Wrong belief:** Private instances need a NAT gateway to reach Amazon S3. **Truth:** In the same Region, a gateway endpoint reaches it, so you [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge). <!-- trap: vpc-trap-s3-needs-nat -->
- **Wrong belief:** An attached internet gateway makes the instances public. **Truth:** [You must update the subnet route table with a route to the internet gateway](../facts/vpc.md#vpc-igw-attach-not-enough). <!-- trap: vpc-trap-igw-attach-makes-public -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-11-19) Regional NAT gateways.<br>
> **Old:** one zonal NAT gateway and one route per zone.<br>
> **Now:** regional NAT gateways [automatically expand across Availability Zones based on your workload footprint](../facts/vpc.md#vpc-regional-nat-gateway-change).<br>
> **The exam probably expects:** a NAT gateway in each Availability Zone for **high availability** (hy uh-vayl-uh-BIL-ih-tee); a regional one if named, except for private connectivity.<br>
> **Status:** examinable.

> **Changed recently:** (2024-02-01) Charge for public IPv4 addresses that are in use.<br>
> **Old:** [No charge](../facts/vpc.md#vpc-public-ipv4-charge-2024) for an in-use public IPv4 address.<br>
> **Now:** [AWS charges for all public IPv4 addresses](../facts/vpc.md#vpc-public-ipv4-charge-2024), in use or idle.<br>
> **The exam probably expects:** older questions treat an address on a running instance as free.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A subnet's route table sends 0.0.0.0/0 to an internet gateway. Its instance has only a private IPv4 address. Can users reach it?

<details>
<summary>Answer</summary>

No: [your instance must have a public IPv4 address](../facts/vpc.md#vpc-igw-requires-attach-and-route) or an Elastic IP address.

**Predict 1:** Not from the gateway alone: [attaching an internet gateway to a VPC does not automatically make your instances accessible from the internet](../facts/vpc.md#vpc-igw-attach-not-enough).

</details>

**Check 2.** A database spans two Availability Zones. How many subnets at least?

<details>
<summary>Answer</summary>

Two, because a subnet [cannot span zones](../facts/vpc.md#vpc-subnet-single-az).

**Predict 2:** No: a subnet [must reside entirely within one Availability Zone](../facts/vpc.md#vpc-subnet-single-az).

</details>

**Check 3.** Private instances upload through a NAT gateway to Amazon S3 in another Region. You add a gateway endpoint for Amazon S3 to their route table. Do the uploads move to it?

<details>
<summary>Answer</summary>

No. [Prefix lists are specific to a Region](../facts/vpc.md#vpc-gateway-endpoint-beats-igw-default-route), so the uploads still use the NAT gateway.

**Predict 3:** Not for a bucket in the same Region: a gateway endpoint carries the uploads, so you [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** What route and what address does an instance need to be reachable over IPv4?

<details>
<summary>Answer</summary>

A route to the internet gateway, and a public IPv4 address or an Elastic IP address.

</details>

**Recap 2.** Which firewall needs an outbound rule for the reply ports, and why?

<details>
<summary>Answer</summary>

The network ACL, because [network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule).

</details>

**Recap 3.** Which two designs keep outbound access after an Availability Zone failure?

<details>
<summary>Answer</summary>

A NAT gateway in each Availability Zone, or one regional NAT gateway.

</details>
