---
chapter: "10"
file: deep
title: Amazon VPC in depth
status: draft
updated: 2026-10-11
---

# Amazon VPC in depth

## How it works (10 min)
<!-- section: role=how; route=full; minutes=10 -->

### Security groups remember connections but network ACLs check every packet (5 min)
<!-- section: route=pass -->

You can filter traffic at the edge of a subnet and at each resource. AWS gives you a firewall for each.

The firewall of a resource is a **security group**. It [controls the traffic that is allowed to reach and leave the resources that it is associated with](../facts/vpc.md#vpc-def-security-group). The firewall at the subnet edge is a **network ACL** (NAK-ul). It [allows or denies specific inbound or outbound traffic at the subnet level](../facts/vpc.md#vpc-def-network-acl).

Now follow one HTTPS request from the internet to a web instance, and its reply.

1. **The request enters the subnet.** The network ACL [evaluates rules in ascending order until a match for the traffic is found](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation). [The default network ACL allows all inbound and outbound traffic](../facts/vpc.md#vpc-nacl-every-subnet-associated).
2. **The request reaches the instance.** The security group [evaluates all rules before deciding whether to allow traffic](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation). It holds [allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type), so a request that no rule allows is dropped.
3. **The reply leaves the instance.** The security group remembers the connection, so the reply needs no outbound rule. A firewall that remembers is **stateful** (STAYT-ful): [security groups are stateful](../facts/vpc.md#vpc-sg-connection-tracking-stateful).
4. **The reply leaves the subnet.** The network ACL remembers nothing, so it is **stateless** (STAYT-less): [Network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule). The reply goes to a short-lived **ephemeral** (ih-FEM-er-ul) port that the client chose. For many client types you [open ephemeral ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-open-1024-65535) outbound.

Each network ACL rule has [a number from 1 to 32766](../facts/vpc.md#vpc-nacl-rule-order-first-match), and the rules are checked [starting with the lowest numbered rule](../facts/vpc.md#vpc-nacl-rule-order-first-match).

<!-- table: compare -->
| Question | Security group | Network ACL |
|---|---|---|
| Where does it apply? | [Instance level](../facts/vpc.md#vpc-sg-vs-nacl-level) | [Subnet level](../facts/vpc.md#vpc-sg-vs-nacl-level) |
| Which rules? | [Allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type) | [Allow and deny rules](../facts/vpc.md#vpc-sg-vs-nacl-rule-type) |
| What about the reply? | [Automatically allowed (stateful)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic) | [Must be explicitly allowed (stateless)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic) |

**Deciding question:** Do you need to block a source, or only to allow the traffic that you expect?

Why two firewalls? A security group follows the resource. The source of a security group rule can be [the ID of a security group](../facts/vpc.md#vpc-sg-rule-sources). So a database group can allow the web group by name.

A network ACL guards the subnet edge, so one deny rule covers every resource behind it.

> **Exam signal:** "block one IP address" points to a deny rule in a network ACL, because a security group has [allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type).

<details>
<summary>Go deeper: rule order and live connections</summary>

To block part of a range, [give the deny rule a lower number than the rule that allows the wider range of port traffic](../facts/vpc.md#vpc-nacl-deny-rule-lower-number). Number rules in [increments of 10 or 100](../facts/vpc.md#vpc-nacl-rule-number-increments). After you change a security group rule, [its tracked connections are not immediately interrupted](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue). Network ACLs [do not filter traffic between instances in the same subnet](../facts/vpc.md#vpc-faq-network-acl-same-subnet).

</details>

**Spot the bug.** A team writes the network ACL of a web subnet. Inbound rule 100 allows TCP 443 from 0.0.0.0/0. Outbound rule 100 allows TCP 443 to 0.0.0.0/0. No other rule allows traffic. Users cannot load the page. What is wrong?

<details>
<summary>Answer</summary>

The replies leave on the port that the client chose, not on port 443. [Network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule), so the outbound rules must allow the reply ports too: [open ephemeral ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-open-1024-65535).

</details>

> **Say it:** The short answer is: a security group remembers connections, and a network ACL does not. The thing to watch is the reply ports.

**Stop and answer.** A database runs in a private subnet. The network ACL of that subnet allows inbound TCP 5432 from the application subnet, and outbound TCP 5432 to the application subnet. No other rule exists. An application on an Amazon Linux instance connects to the database. Does the application get an answer?

<details>
<summary>Answer</summary>

No. The reply goes to the port that the client chose, for example one of [ports 32768-61000](../facts/vpc.md#vpc-nacl-ephemeral-linux-32768-61000) on Amazon Linux. [Network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule), so the outbound rule must allow that range.

</details>

### A NAT gateway lets private instances start connections and charges hourly and per gigabyte (5 min)
<!-- section: route=pass -->

A worker in a private subnet has a private IP address and nothing else. It needs to download patches, and no host on the internet is allowed to start a connection to it. A **NAT gateway** is [a Network Address Translation (NAT) service](../facts/vpc.md#vpc-natgw-purpose) that solves both.

Now follow one packet from the worker to a package server on the internet.

1. **The worker sends the packet.** The route table of the private subnet sends internet traffic to the NAT gateway.
2. **The NAT gateway translates the address.** [You create a public NAT gateway in a public subnet](../facts/vpc.md#vpc-natgw-public-connectivity-type), and [NAT maps multiple private IPv4 addresses to a single public IPv4 address](../facts/vpc.md#vpc-nat-device-maps-many-to-one).
3. **The packet leaves the VPC.** The route table of the public subnet sends it to the internet gateway.
4. **The reply returns.** The NAT gateway lets replies to its own requests back in: [it is therefore stateful](../facts/vpc.md#vpc-natgw-stateful-allows-outbound).
5. **A stranger tries to connect.** Nothing arrives, because [connections must always be initiated from within the VPC containing the NAT gateway](../facts/vpc.md#vpc-natgw-connections-originate-inside-vpc).

Now count the charges for the same packet. Three charges can apply:

- each hour: you are [charged for each hour that your NAT gateway is available](../facts/vpc.md#vpc-natgw-pricing-dimensions);
- each gigabyte processed, [regardless of the traffic's source or destination](../facts/vpc.md#vpc-natgw-data-processing-any-destination), so Amazon S3 traffic pays it too;
- [data transfer charges between your NAT gateway and EC2 instance if they are in a different Availability Zone](../facts/vpc.md#vpc-natgw-cross-az-transfer-charge).

A **gateway endpoint** is a target in the route table. Instances in those subnets [automatically use the gateway endpoint to access the service](../facts/vpc.md#vpc-gateway-endpoint-applies-per-route-table), here Amazon S3. Why does it save money? It takes Amazon S3 traffic off the NAT path, and you [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge).

> **Exam heuristic:** "LEAST cost" points to one NAT gateway. "Highly available" points to one NAT gateway in each Availability Zone in older questions. A regional NAT gateway is the current answer when an option names it.

<details>
<summary>Go deeper: one zone or every zone</summary>

[Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone](../facts/vpc.md#vpc-natgw-one-az-redundant-in-zone). If that zone fails, [resources in the other Availability Zones lose internet access](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet). Regional NAT gateways [automatically expand across Availability Zones based on your workload footprint](../facts/vpc.md#vpc-regional-nat-gateway-change), but they [do not support private NAT](../facts/vpc.md#vpc-regional-nat-no-private-nat).

</details>

**Spot the bug.** A team creates a NAT gateway in a private subnet and points the route table of that subnet at it. The instances still cannot reach the internet. What is wrong?

<details>
<summary>Answer</summary>

[The NAT gateway must be in a public subnet with a route table that routes internet traffic to an internet gateway](../facts/vpc.md#vpc-natgw-troubleshoot-route-placement). Here it sits in the private subnet, next to the instances.

</details>

> **Say it:** The short answer is: a NAT gateway lets private instances start connections out. The thing to watch is the bill for each gigabyte.

**Stop and answer.** Callvale's worker runs in the Availability Zone AZ 2 and sends 120 GB of audio a month to Amazon S3. It also downloads a few patches. The only NAT gateway is in AZ 1. Which charges does the S3 traffic create, and which change removes them?

<details>
<summary>Answer</summary>

The S3 traffic pays NAT data processing, [regardless of the traffic's source or destination](../facts/vpc.md#vpc-natgw-data-processing-any-destination), and cross-zone transfer between AZ 2 and AZ 1. A gateway endpoint for Amazon S3 removes both, because [there are no data processing or hourly charges for using Gateway Type VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge). The NAT gateway stays for the patches.

If the large traffic went to a package server on the internet, a gateway endpoint would not help. Then you [create a NAT gateway in each Availability Zone with resources](../facts/vpc.md#vpc-natgw-same-az-reduces-charges).

</details>

## Numbers that decide answers (2 min)
<!-- section: role=numbers; route=full; minutes=2 -->

Not part of this sample.

## Decision record (2 min)
<!-- section: role=example; route=full; minutes=2 -->

Not part of this sample.

## FAQ quick-fire (2 min)
<!-- section: role=faq; route=full; minutes=2 -->

Not part of this sample.
