---
id: "13"
slug: route53
title: Amazon Route 53
file: fast
tier: deep
domains: [2, 3, 4]
tasks: ["2.2", "3.4", "4.4"]
services: [route53]
minutes: {fast: 20, pass: 76, full: 171}
status: ready
updated: 2026-10-13
---

# Amazon Route 53

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** You change the IP address in a Route 53 record. Does every user reach the new address within a minute? <!-- gist-trap -->

**Predict 2.** Can example.com, with no www in front, point to a load balancer?

**Predict 3.** Every endpoint behind one name fails its Route 53 health check. Does Route 53 stop answering for that name?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read the IP address ranges that Route 53 health checkers send their requests from. Then read two Route 53 quotas of your account; the task creates nothing.

<!-- task:start id=route53-t01 -->

Look

**It kills the belief.** "Route 53 health checks run inside my VPC, so they can test private addresses."

> **Cost:** $0.

**Permissions.** `route53:GetAccountLimit`, `route53:ListHostedZones`, `route53:ListHealthChecks`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read the first five IP address ranges that Route 53 health checkers send their requests from. Route 53 is a global service, so the Region of CloudShell does not matter here.

   ```bash
   aws route53 get-checker-ip-ranges --query "CheckerIpRanges[0:5]"
   ```

   Expect: Five ranges in CIDR notation. Each one is a range of public internet addresses, not a private range such as 10.0.0.0/8 or 192.168.0.0/16. The checkers send their requests over the internet, from outside your VPCs.

2. Read how many health checks this account can have, and how many it has now.

   ```bash
   aws route53 get-account-limit --type MAX_HEALTH_CHECKS_BY_OWNER --query "[Limit.Value,Count]"
   ```

   Expect: Two numbers. The first is the quota: 200 active health checks, unless someone raised it for this account. The second is the number of health checks that exist now, often 0.

3. Read the same two numbers for hosted zones.

   ```bash
   aws route53 get-account-limit --type MAX_HOSTED_ZONES_BY_OWNER --query "[Limit.Value,Count]"
   ```

   Expect: The quota of 500 hosted zones, unless someone raised it for this account, and the number of hosted zones that exist now.

4. List the hosted zones of the account and whether each one is private.

   ```bash
   aws route53 list-hosted-zones --query "HostedZones[].[Name,Config.PrivateZone]"
   ```

   Expect: Often an empty list in a learning account. Otherwise one row for each zone: its name, which ends with a dot, and true for a private hosted zone or false for a public hosted zone.

5. List the type and the IP address of every health check in the account.

   ```bash
   aws route53 list-health-checks --query "HealthChecks[].[HealthCheckConfig.Type,HealthCheckConfig.IPAddress]"
   ```

   Expect: Often an empty list. Every IP address in the output is a public address: Route 53 cannot check an endpoint whose address is in a private range. A row with null checks a domain name, or it is a calculated health check.

**Label.** checked against docs, not run in a real account. Checked 2026-10-14.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Amazon Route 53 is a [highly available and scalable](../facts/route53.md#route53-three-main-functions) DNS service with [three main functions](../facts/route53.md#route53-three-main-functions): domain registration, DNS routing and health checking.

**The problem it solves.** People type names, but browsers need IP addresses. Route 53 keeps a domain's records in a **hosted zone**, [a container for records](../facts/route53.md#route53-hosted-zone-container).

**Predict the picture.** Who answers, and who keeps the answer for its time to live (TTL)?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: a browser, a DNS resolver, the TLD name server for .com and a Route 53 name server. The browser asks the resolver. The resolver asks the TLD name server, which names the Route 53 name servers. The resolver asks a Route 53 name server, which returns the address from the hosted zone. The resolver returns it to the browser and keeps a copy.](../diagrams/svg/route53-hero.svg)

**Figure.** A resolver finds Route 53 through the top-level domain (TLD) name server, gets the answer from the hosted zone, and caches it.

1. The browser asks a DNS resolver, usually run by the internet service provider, for www.example.com.
2. The resolver asks the TLD name server for .com, which it finds through a DNS root name server.
3. The TLD name server answers with the [names of the four Route 53 name servers](../facts/route53.md#route53-tld-returns-four-name-servers) of the domain.
4. A Route 53 name server finds the record in the hosted zone and returns the IP address.
5. The resolver gives the address to the browser and caches it for the TTL of the record.

</details>

> **Startup example:** At a registrar, callvale.example points to the IP address of one old instance. Before launch, callvale.example and app.callvale.example must point to AWS resources by name.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| alias record (AY-lee-us) | **create** an alias record for a load balancer | A Route 53 record that points a name to an AWS resource | CNAME record |
| routing policy | **choose** a routing policy | The setting that decides which record answers a DNS query | route table |
| health check (HELTH chek) | **fail** a health check | A repeated test of whether an endpoint can serve requests | status check |
| fail over (FAYL OH-ver) | **fail over to** the standby | To move users from a failed resource to a standby resource | roll back |
| latency (LAY-ten-see) | **reduce** latency for users | The time between a request and its response | throughput |
| high availability (hy uh-vayl-uh-BIL-ih-tee) | **design** for high availability | A system that keeps working after a short interruption when one part fails | fault tolerance |
| hybrid (HY-brid) | a **hybrid** network | AWS and your own data center, used together | multi-Region |
| Elastic IP address | **associate** an Elastic IP address | A static public IPv4 address that you can move between instances | public IPv4 address |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### Alias record or CNAME record

<!-- table: compare -->
| Question | Alias record | CNAME record |
|---|---|---|
| Can it sit at the zone apex, such as example.com? | Yes: [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex) there | No: the [DNS protocol does not allow you to create](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex) one |
| What can it point to? | [Route traffic to selected AWS resources](../facts/route53.md#route53-alias-extension-targets), or [one record in a hosted zone to another](../facts/route53.md#route53-alias-extension-targets) | It [can redirect DNS queries to any DNS record](../facts/route53.md#route53-alias-targets-only-selected-aws-resources) |
| Is a query to an AWS resource charged? | No, for listed services: A and AAAA alias records [do not incur a charge](../facts/route53.md#route53-pricing-alias-free-for-listed-aws-services) | Yes: Route 53 [charges for CNAME queries](../facts/route53.md#route53-alias-queries-free-cname-charged) |
| Who sets the TTL? | For an AWS resource, [Route 53 uses the default TTL for the resource](../facts/route53.md#route53-alias-to-aws-resource-ttl-not-settable) | You do |

**Deciding question:** Does the name point to an AWS resource, or to a name outside AWS?

### Routing by latency or by location

<!-- table: compare -->
| Question | Routing policy | How it chooses |
|---|---|---|
| Which Region is fastest for this user? | Latency | [The Region that provides the best latency](../facts/route53.md#route53-choose-latency-routing-best-latency-region) |
| Must users of one country reach one endpoint? | Geolocation | [Based on the location of your users](../facts/route53.md#route53-choose-geolocation-routing-user-location), for example for distribution rights |
| Should one Region serve a larger or smaller area? | Geoproximity | By resource location. [A bias expands or shrinks the geographic region](../facts/route53.md#route53-geoproximity-bias-expands-or-shrinks-region) |
| Do you know the client networks? | IP-based | By [the IP addresses that the traffic originates from](../facts/route53.md#route53-choose-ip-based-routing-known-client-ips) |

**Deciding question:** Does the requirement name speed, a place where the user is, an area to grow or shrink around a Region, or known client networks?

### Which health check does what

<!-- table: compare -->
| Question | Route 53 health check | Elastic Load Balancing health check | EC2 Auto Scaling health check |
|---|---|---|---|
| What does a failed check change? | The DNS answer: [Route 53 routes traffic away from the associated record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record) | The requests: [it stops routing traffic to that target](../facts/elb.md#elb-unhealthy-target-stop-resume) | The instance: [it replaces it with a new instance](../facts/route53.md#route53-asg-unhealthy-instance-replaced) |
| Where is it taught? | This chapter | [Chapter 14](../14-elb/1-fast.md#in-one-breath-3-min) | [Chapter 17](../17-auto-scaling/1-fast.md#in-one-breath-3-min) |

**Deciding question:** Must the fix change the DNS answer, stop requests to one target, or replace the instance?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "zone apex", "root domain" | an alias record | [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex) at the zone apex | the target is outside AWS: an A record with its IP address |
| "lowest latency", "two or more Regions" | latency records | Route 53 picks [the Region that provides the best latency](../facts/route53.md#route53-choose-latency-routing-best-latency-region) | one country must stay in one Region: geolocation records |
| "a specific country", "distribution rights" | geolocation records and a default record | content for [only the locations where you have distribution rights](../facts/route53.md#route53-geolocation-use-cases) | one Region must serve a larger area: geoproximity records with a bias |
| "a small share of users on a new version" | weighted records | traffic to [multiple resources in proportions that you specify](../facts/route53.md#route53-choose-weighted-routing-proportions) | the second resource serves users after a failure: failover records |
| "active-passive", "static maintenance page" | failover records | you can [maintain a backup site](../facts/route53.md#route53-faq-failover-backup-site-s3) | cached answers delay failover: AWS Global Accelerator [avoids caching issues that can occur with DNS](../facts/route53.md#route53-vs-ga-dr-avoids-dns-caching) |
| "several healthy IP addresses, no load balancer" | multivalue answer records | [up to eight healthy records selected at random](../facts/route53.md#route53-choose-multivalue-routing-up-to-eight-healthy) | even load across instances: a load balancer |
| "on-premises servers resolve a private hosted zone" | an inbound Resolver endpoint | queries reach the VPC [from your on-premises network or another VPC](../facts/route53.md#route53-resolver-inbound-endpoint-definition) | instances resolve on-premises names: an outbound endpoint and a forwarding rule |
| "internal names inside the VPC" | a private hosted zone | it answers [within one or more VPCs](../facts/route53.md#route53-private-hosted-zone-defined) | users on the internet must resolve the name: a public hosted zone |

### Traps

- **Wrong belief:** A CNAME record can point example.com to a load balancer. **Truth:** The [DNS protocol does not allow you to create](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex) one at the zone apex, but [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex) there. <!-- trap: route53-trap-cname-at-apex -->
- **Wrong belief:** Every user gets a changed record within a minute. **Truth:** Route 53 servers update [within 60 seconds](../facts/route53.md#route53-faq-propagation-within-60-seconds) under normal conditions, but resolvers cache records [according to their time to live (TTL)](../facts/route53.md#route53-faq-resolver-caches-by-ttl-outside-control). <!-- trap: route53-trap-ttl-instant-change -->
- **Wrong belief:** Geolocation routing finds the fastest Region. **Truth:** It uses the [geographic location of the requests](../facts/route53.md#route53-faq-geo-vs-latency-geography-not-latency), not measured latency. <!-- trap: route53-trap-geolocation-for-performance -->
- **Wrong belief:** A Route 53 health check replaces a failed instance. **Truth:** [Route 53 routes traffic away from the associated record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record); EC2 Auto Scaling replaces instances. <!-- trap: route53-trap-health-check-replaces-instance -->
- **Wrong belief:** If every record is unhealthy, Route 53 returns no answer. **Truth:** It [considers all the records in the group](../facts/route53.md#route53-no-record-healthy-all-records-considered-healthy) healthy and answers. <!-- trap: route53-trap-all-unhealthy-no-answer -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2025-11-30) The DNS resolver of each VPC has a new name.<br>
> **Old:** [Route 53 Resolver](../facts/route53.md#route53-change-vpc-resolver-rename-2025-11).<br>
> **Now:** [Route 53 VPC Resolver](../facts/route53.md#route53-change-vpc-resolver-rename-2025-11).<br>
> **The exam probably expects:** the old name.<br>
> **Status:** examinable.

> **Changed recently:** (2025-11-26) Accelerated recovery for public hosted zones.<br>
> **Old:** not available.<br>
> **Now:** a [60-minute Recovery Time Objective (RTO)](../facts/route53.md#route53-accelerated-recovery-60-minute-rto) for record changes when us-east-1 is impaired, if turned on in advance.<br>
> **The exam probably expects:** no record changes then; failover records [will continue to work](../facts/route53.md#route53-fi-impairment-dns-and-health-checks-keep-working).<br>
> **Status:** examinable.

> **Changed recently:** (2024-01-09) Geoproximity records without Traffic Flow.<br>
> **Old:** [geoproximity routing (traffic flow only)](../facts/route53.md#route53-change-geoproximity-records-console-2024-01).<br>
> **Now:** you can [create geoproximity routing records](../facts/route53.md#route53-change-geoproximity-records-console-2024-01) like other records.<br>
> **The exam probably expects:** that geoproximity routing needs Traffic Flow, the Route 53 visual editor.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** A resolver cached a record ten minutes ago, and the TTL is 3600 seconds. When does it see a change that you make now?

<details>
<summary>Answer</summary>

When its cached copy expires: resolvers cache records [according to their time to live (TTL)](../facts/route53.md#route53-faq-resolver-caches-by-ttl-outside-control).

**Predict 1:** No. Route 53 servers generally update [within 60 seconds](../facts/route53.md#route53-changes-propagate-within-60-seconds), but resolvers keep their copies until the TTL ends.

</details>

**Check 2.** Which record makes example.com open a CloudFront distribution?

<details>
<summary>Answer</summary>

An alias record, which can map the zone apex to [your Amazon CloudFront distribution](../facts/route53.md#route53-faq-apex-alias-cloudfront).

**Predict 2:** Yes, with an alias record. The [DNS protocol does not allow you to create](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex) a CNAME record there.

</details>

**Check 3.** Both failover records have health checks, and both fail. What does Route 53 answer?

<details>
<summary>Answer</summary>

The primary: [Route 53 returns the primary record](../facts/route53.md#route53-failover-both-unhealthy-returns-primary).

**Predict 3:** No. Route 53 then [considers all the records in the group](../facts/route53.md#route53-no-record-healthy-all-records-considered-healthy) healthy and answers.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Which record can point the zone apex to a load balancer?

<details>
<summary>Answer</summary>

An alias record: [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex) at the zone apex.

</details>

**Recap 2.** Which stem phrases point to geolocation records?

<details>
<summary>Answer</summary>

"A specific country" and "distribution rights".

</details>

**Recap 3.** What does Route 53 answer when every record of a name is unhealthy?

<details>
<summary>Answer</summary>

It [considers all the records in the group](../facts/route53.md#route53-no-record-healthy-all-records-considered-healthy) healthy and answers by the routing policy.

</details>
