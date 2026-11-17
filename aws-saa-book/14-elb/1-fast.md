---
id: "14"
slug: elb
title: Elastic Load Balancing
file: fast
tier: deep
domains: [1, 2, 3, 4]
tasks: ["1.3", "2.1", "2.2", "3.4", "4.2", "4.4"]
services: [elb]
minutes: {fast: 20, pass: 46, full: 79}
status: ready
updated: 2026-10-13
---

# Elastic Load Balancing

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** One web instance behind a load balancer fails its health checks. Does the load balancer replace it with a new instance? <!-- gist-trap -->

**Predict 2.** Can you give an Application Load Balancer a fixed IP address that never changes?

**Predict 3.** The HTTPS listener of a load balancer has a certificate. Is the traffic between the load balancer and the instances encrypted too?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read the security policy of a new HTTPS listener: its TLS versions. Then read the load balancer quotas of your account; the task creates nothing.

<!-- task:start id=elb-t01 -->

Look

**It kills the belief.** "The certificate decides which TLS versions a client can use."

> **Cost:** $0.

**Permissions.** `elasticloadbalancing:DescribeSSLPolicies`, `elasticloadbalancing:DescribeAccountLimits`, `elasticloadbalancing:DescribeLoadBalancers`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read the TLS versions of the security policy ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09. The console gives this policy to a new HTTPS listener.

   ```bash
   aws elbv2 describe-ssl-policies --names ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 --query "SslPolicies[0].SslProtocols"
   ```

   Expect: Two versions, TLSv1.2 and TLSv1.3, in any order. The output names no certificate: the versions come from the policy.

2. Read the same list for ELBSecurityPolicy-2016-08. An HTTPS listener that you create with the AWS CLI gets this policy when the command names no policy.

   ```bash
   aws elbv2 describe-ssl-policies --names ELBSecurityPolicy-2016-08 --query "SslPolicies[0].SslProtocols"
   ```

   Expect: Three versions: TLSv1, TLSv1.1 and TLSv1.2, and no TLSv1.3. With this policy, a listener accepts older TLS versions than with the policy of step 1, whatever its certificate.

3. Read how many Application Load Balancers this account can have in the Region that CloudShell uses.

   ```bash
   aws elbv2 describe-account-limits --query "Limits[?Name=='application-load-balancers'].Max"
   ```

   Expect: ["50"], unless someone raised this quota for the account. The quota counts the load balancers of one Region.

4. List the load balancers that already exist in this Region, with the type and the scheme of each one.

   ```bash
   aws elbv2 describe-load-balancers --query "LoadBalancers[].[LoadBalancerName,Type,Scheme]"
   ```

   Expect: Often an empty list in a learning account. Otherwise one row for each load balancer: its name, a type such as application or network, and the scheme internet-facing or internal.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Elastic Load Balancing [automatically distributes your incoming traffic](../facts/elb.md#elb-what-distributes-traffic-across-targets) across targets [in one or more Availability Zones](../facts/elb.md#elb-what-distributes-traffic-across-targets) and [routes traffic only to the healthy targets](../facts/elb.md#elb-routes-only-to-healthy-targets).

**The problem it solves.** With one instance, one failure stops everything. A load balancer puts one DNS name in front of many targets and [scales your load balancer capacity automatically](../facts/elb.md#elb-scales-capacity-automatically).

A **listener** is [a process that checks for connection requests](../facts/elb.md#elb-listener-checks-connection-requests). Its rules choose a **target group**.

**Predict the picture.** When one instance fails its health checks, where do the next requests go?

<details>
<summary>Show the picture</summary>

![An architecture with users on the left and an Application Load Balancer with a node in each of two Availability Zones. Each zone has one instance in a private subnet; the instance in the second zone is marked unhealthy. Numbered arrows run from the users to a node and on to the healthy instance.](../diagrams/svg/elb-hero.svg)

**Figure.** Each request reaches a load balancer node in one zone, and the node sends it to a healthy target.

1. The client resolves the DNS name and gets the [IP addresses of the load balancer nodes](../facts/elb.md#elb-dns-returns-node-ips).
2. The client connects to a node, whose listener is [configured with a protocol and port number](../facts/elb.md#elb-listener-checks-connection-requests).
3. The node [evaluates the listener rules in priority order](../facts/elb.md#elb-alb-rules-priority-then-algorithm) to choose a target group.
4. The node [selects a healthy registered target](../facts/elb.md#elb-node-sends-to-target-private-ip) and sends the request to its private IP address.
5. As long as other targets are healthy, a failed target gets no new requests until the load balancer [resumes routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume).

</details>

> **Startup example:** Callvale's web application runs on one instance in one zone and fails a load test at 150 requests per second. It must survive losing an instance or a zone, serve HTTPS, and route by URL path later.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| load balancer | **register** a target with a load balancer | Spreads incoming requests across several targets | Auto Scaling group |
| target group | **forward** requests to a target group | The set of targets that a load balancer sends requests to | security group |
| health check (HELTH chek) | **fail** a health check | A repeated test that shows whether a target can serve requests | status check |
| high availability (hy uh-vayl-uh-BIL-ih-tee) | **design** for high availability | Keeps working after a short interruption when one part fails | fault tolerance |
| fault tolerance (FAWLT TOL-er-uns) | **tolerate** the loss of an Availability Zone | Keeps working with no interruption when one part fails | high availability |
| encryption in transit | **enforce** encryption in transit | Protecting data that moves over a network | encryption at rest |
| stateless (STAYT-less) | a stateless **application tier** | Keeps no memory of earlier requests | serverless |
| latency (LAY-ten-see) | **low** latency | The time between a request and its response | throughput |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### The three load balancer types

<!-- table: compare -->
| Question | Application Load Balancer (ALB) | Network Load Balancer (NLB) | Gateway Load Balancer (GWLB) |
|---|---|---|---|
| Which layer does it read? | [Layer 7](../facts/elb.md#elb-compare-layer-per-type) | [Layer 4](../facts/elb.md#elb-compare-layer-per-type) | [Layer 3 Gateway + Layer 4 Load Balancing](../facts/elb.md#elb-compare-layer-per-type) |
| What does it listen for? | [HTTP, HTTPS, gRPC](../facts/elb.md#elb-compare-listener-protocols-per-type) | [TCP, UDP, TLS](../facts/elb.md#elb-compare-listener-protocols-per-type) | [IP](../facts/elb.md#elb-compare-listener-protocols-per-type) packets |
| Which targets can it have? | [IP, Instance, Lambda](../facts/elb.md#elb-compare-target-types-per-type) | [IP, Instance, Application Load Balancer](../facts/elb.md#elb-compare-target-types-per-type) | [IP, Instance](../facts/elb.md#elb-compare-target-types-per-type) |
| Static or Elastic IP address? | No | Yes: [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only) | No |
| When does AWS suggest it? | [If you need to load balance HTTP requests](../facts/elb.md#elb-choose-alb-for-http-flexible-management) | When [extreme performance and static IP is needed](../facts/elb.md#elb-choose-nlb-for-layer4-extreme-performance-static-ip) | To run [third-party virtual appliances](../facts/elb.md#elb-choose-gwlb-for-third-party-appliances) |

**Deciding question:** Does the traffic need HTTP routing, fixed addresses with TCP or UDP, or a path through appliances?

### What to put in front of an Application Load Balancer

<!-- table: compare -->
| Question | Amazon CloudFront | AWS Global Accelerator | NLB with the ALB as a target |
|---|---|---|---|
| What does it add? | A [distributed, single point of entry](../facts/elb.md#elb-alb-cloudfront-global-reach) near users | [static IP addresses that serve as fixed endpoints](../facts/elb.md#elb-alb-global-accelerator-static-ips) | [static IP addresses](../facts/elb.md#elb-nlb-alb-target-static-ip-privatelink) and [endpoint services (AWS PrivateLink)](../facts/elb.md#elb-nlb-alb-target-static-ip-privatelink) |
| When do you choose it? | Users are far away, and content can be cached | Fixed addresses for [load balancers in one or more AWS Regions](../facts/elb.md#elb-ga-alb-multiple-regions) | Fixed addresses or PrivateLink in front of one ALB |

**Deciding question:** Do you need caching near users, fixed addresses across Regions, or fixed addresses and PrivateLink in front of one VPC? <!-- xref: 15 CloudFront in front of the ALB, static anycast addresses -->

### Sticky sessions or a central session store

<!-- table: compare -->
| Question | Sticky sessions | Central session store |
|---|---|---|
| Where does the session live? | On one target: they [bind a user's session to a specific target](../facts/elb.md#elb-alb-sticky-sessions-what) | In a [database, cache, or external files](../facts/ec2-auto-scaling.md#ec2-auto-scaling-wa-offload-session-data) |
| What is the effect? | Can cause [uneven distribution of connections and flows](../facts/elb.md#elb-sticky-uneven-load-nat) | AWS calls it ideal [when your fleet of web servers is elastic](../facts/elb.md#elb-session-store-centralized-not-on-servers) |

**Deciding question:** Must a session survive the loss of the instance that created it? <!-- xref: 29 ElastiCache session store instead of sticky sessions -->

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "route by URL path or host name" | ALB listener rules | rules [forward requests based on the URL](../facts/elb.md#elb-alb-path-conditions-smaller-services) | fixed addresses too: keep the ALB, add an NLB in front |
| "static IP addresses, partner allow-list" | NLB | [optionally associate one Elastic IP address](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip) per zone [when you create the Network Load Balancer](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip) | several Regions: AWS Global Accelerator |
| "extremely low latency, huge request rates" | NLB | built for [millions of requests per second](../facts/elb.md#elb-nlb-faq-millions-rps-low-latency) | requests need AWS WAF rules: an ALB |
| "third-party firewalls inline" | GWLB | [deploy, scale, and manage virtual appliances](../facts/elb.md#elb-gwlb-virtual-appliances) | traffic is for the service itself: ALB or NLB |
| "offload TLS from the instances" | HTTPS listener, AWS Certificate Manager (ACM) certificate | it [performs the work of encrypting and decrypting](../facts/elb.md#elb-offload-encryption-to-lb) | instances must decrypt: [a Network Load Balancer with a TCP listener on port 443](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp) |
| "several HTTPS domains on one load balancer" | certificate list with Server Name Indication (SNI) | [support multiple domains on the same port](../facts/elb.md#elb-alb-sni-certificate-list-multiple-domains) | subdomains of one domain: [use a wildcard certificate](../facts/elb.md#elb-alb-cert-wildcard-or-san-single-cert) or SAN |
| "users return to the same server" | sticky sessions | useful for [servers that maintain state information](../facts/elb.md#elb-alb-sticky-for-stateful-servers) | sessions must outlive instances: a session store |
| "replace unhealthy instances automatically" | Auto Scaling group with ELB health checks | [Amazon EC2 Auto Scaling replaces the unhealthy instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace) | no Auto Scaling group: routing stops, nothing replaces it |

### Traps

- **Wrong belief:** An ALB can have fixed or Elastic IP addresses. **Truth:** Only the NLB has [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only). The ALB's [IP addresses can be remapped quickly](../facts/elb.md#elb-dns-ttl-60-seconds-remap). <!-- trap: elb-trap-alb-static-ip -->
- **Wrong belief:** The load balancer replaces unhealthy instances. **Truth:** For an unhealthy target, [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume). With ELB health checks, [Amazon EC2 Auto Scaling replaces the unhealthy instance](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-checks-reroute-and-replace). By default, Auto Scaling [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default) checks. <!-- trap: elb-trap-lb-replaces-instance --> <!-- xref: 17 EC2 Auto Scaling ELB health check type -->
- **Wrong belief:** An NLB has no security groups. **Truth:** You can add them, but only [when you create it](../facts/elb.md#elb-nlb-security-groups-only-at-creation). Targets that allow only that group get traffic only [through your Network Load Balancer](../facts/elb.md#elb-nlb-sg-reference-blocks-direct-access). <!-- trap: elb-trap-nlb-no-security-groups -->
- **Wrong belief:** If every target fails its health checks, requests stop. **Truth:** On an ALB, [the load balancer fails open](../facts/elb.md#elb-alb-fail-open-all-unhealthy) and [routes requests to all those targets](../facts/elb.md#elb-alb-fail-open-all-unhealthy). <!-- trap: elb-trap-all-unhealthy-stops-traffic -->
- **Wrong belief:** An HTTPS listener encrypts traffic up to the instances. **Truth:** The listener uses its certificate to [terminate the front-end connection](../facts/elb.md#elb-alb-https-listener-terminates-and-decrypts). An HTTPS target group, or an NLB that [passes encrypted traffic through to the targets](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp), protects the second hop. <!-- trap: elb-trap-https-listener-end-to-end -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-02-13) An NLB can remove an Availability Zone.<br>
> **Old:** you could add zones but [could not remove AZs](../facts/elb.md#elb-change-nlb-remove-az-2025-02).<br>
> **Now:** you can [disable an Availability Zone](../facts/elb.md#elb-change-nlb-remove-az-2025-02) of an NLB.<br>
> **The exam probably expects:** NLB zones are never removed.<br>
> **Status:** examinable.

> **Changed recently:** (2023-08-10) NLBs can have security groups.<br>
> **Old:** access was set by [security group rules at the instance level](../facts/elb.md#elb-change-nlb-security-groups-2023-08).<br>
> **Now:** you can [associate security groups with your Network Load Balancers](../facts/elb.md#elb-change-nlb-security-groups-2023-08) when you create them.<br>
> **The exam probably expects:** NLB targets must allow the client addresses.<br>
> **Status:** examinable.

> **Changed recently:** (2025-11-13) NLBs accept QUIC.<br>
> **Old:** not available.<br>
> **Now:** an NLB forwards the [QUIC protocol in passthrough mode](../facts/elb.md#elb-change-nlb-quic-2025-11).<br>
> **The exam probably expects:** TCP, TLS and UDP only.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

Answers to the three Predict questions:

<details>
<summary>Answer</summary>

**Predict 1:** No. On a failed check, [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume). An Auto Scaling group replaces it only with ELB health checks: by default, the group [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default) checks.

**Predict 2:** No. Only the [Network Load Balancer](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only) has static or Elastic IP addresses.

**Predict 3:** Not with an HTTP target group: the listener uses its certificate to [terminate the front-end connection](../facts/elb.md#elb-alb-https-listener-terminates-and-decrypts).

</details>

**Check 1.** An NLB with default settings has two targets in AZ 1 and six in AZ 2. Which targets run hot?

<details>
<summary>Answer</summary>

The two in AZ 1. On an NLB, [cross-zone load balancing is disabled by default](../facts/elb.md#elb-nlb-gwlb-cross-zone-off-by-default), so each node uses only the [registered targets in its Availability Zone](../facts/elb.md#elb-cross-zone-what-it-does).

</details>

**Check 2.** Scale-in deregisters an ALB target in the middle of a 10-minute upload. Does the upload finish with default settings?

<details>
<summary>Answer</summary>

No. The target drains [until in-flight requests have completed](../facts/elb.md#elb-deregister-stops-routing-draining), but only for the deregistration delay of [300 seconds](../facts/elb.md#elb-deregistration-delay-default-300-seconds) by default.

</details>

**Check 3.** The load balancer must never see decrypted traffic. Which listener fits?

<details>
<summary>Answer</summary>

[A Network Load Balancer with a TCP listener on port 443](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp), which [passes encrypted traffic through to the targets](../facts/elb.md#elb-alb-https-decrypt-at-target-use-nlb-tcp).

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which load balancer type has static or Elastic IP addresses?

<details>
<summary>Answer</summary>

The Network Load Balancer: [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only).

</details>

**Recap 2.** Which stem phrase points to a Gateway Load Balancer?

<details>
<summary>Answer</summary>

"Third-party firewalls inline": a GWLB lets you [deploy, scale, and manage virtual appliances](../facts/elb.md#elb-gwlb-virtual-appliances).

</details>

**Recap 3.** By default, does an Auto Scaling group act on the load balancer's health checks?

<details>
<summary>Answer</summary>

No. By default, Auto Scaling [ignores the results of the Elastic Load Balancing](../facts/ec2-auto-scaling.md#ec2-auto-scaling-elb-health-checks-ignored-by-default) checks.

</details>
