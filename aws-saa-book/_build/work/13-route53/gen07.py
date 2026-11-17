import json

def ev(sid, quote, url=None, header=None):
    if url is None:
        if sid.startswith("docs/"):
            url = "https://docs.aws.amazon.com/" + sid[5:] + ".html"
        elif sid.startswith("www/"):
            url = "https://aws.amazon.com/" + sid[4:] + "/"
    return {"source_id": sid, "url": url, "quote": quote, "table_header": header}

R = "docs/Route53/latest/DeveloperGuide/"
HIST = R + "History"
WP = "docs/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/"

def fact(id, kind, claim, question, values, scope, evidence, hard=True, tier0=False, rel="extended", bullets=None,
         note="", vol="stable", dom="", adj=False, cond="", change_items=None, changed=None):
    f = {"id": id, "service": "route53", "home_chapter": "13", "kind": kind, "claim": claim, "question": question,
         "values": [{"key": k, "display": d} for k, d in values],
         "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
         "evidence": evidence, "source_tier": 1, "hard": hard, "tier0": tier0, "volatility": vol, "changed": changed,
         "exam_relevance": rel, "bullets": bullets or []}
    if change_items:
        f["change_items"] = change_items
    if note:
        f["note"] = note
    return f

facts = []

# ---- hybrid DNS (whitepaper) ----
facts.append(fact("route53-hybrid-resolver-endpoints-no-extra-dns-servers", "capability",
 "Route 53 Resolver endpoints and forwarding rules forward traffic between your Amazon VPC and your on-premises data center without having to deploy additional DNS servers.",
 "What does the hybrid DNS whitepaper recommend for forwarding queries between a VPC and on-premises?",
 [("rule", "without having to deploy additional DNS servers")], "Route 53 VPC Resolver endpoints and forwarding rules",
 [ev(WP + "route-53-resolver-endpoints-and-forwarding-rules", "Route 53 Resolver endpoints and forwarding rules allow you to forward traffic between your Amazon VPC and on-premises data center without having to deploy additional DNS servers.")],
 tier0=True, rel="core", bullets=["3.4.S1"], note="d13-080. The whitepaper uses the former name Route 53 Resolver and is marked historical (route53-hybrid-whitepaper-historical-banner)."))

facts.append(fact("route53-hybrid-one-outbound-endpoint-shared-by-rules", "capability",
 "You need only one outbound endpoint for multiple VPCs: you share the outbound endpoint by sharing the Resolver rules created for it with other accounts using RAM, instead of creating an outbound endpoint in each VPC.",
 "How many outbound endpoints do many VPCs need, and how are they shared?",
 [("one", "You need only one outbound endpoint for multiple VPCs.")], "Route 53 VPC Resolver outbound endpoints and rules",
 [ev(WP + "route-53-resolver-endpoints-and-forwarding-rules", "You need only one outbound endpoint for multiple VPCs. You don’t have to create an outbound endpoint in each VPC. Instead, you share an outbound endpoint by sharing the rules created for that endpoint with additional accounts using RAM.")],
 rel="extended", bullets=["3.4.S1"], note="d13-080."))

facts.append(fact("route53-hybrid-endpoints-not-across-regions", "restriction",
 "Resolver endpoints cannot be used across Regions.",
 "Can a Resolver endpoint serve VPCs in another Region?",
 [("region", "Endpoints cannot be used across Regions.")], "Route 53 VPC Resolver endpoints",
 [ev(WP + "route-53-resolver-endpoints-and-forwarding-rules", "Endpoints cannot be used across Regions.")],
 rel="extended", bullets=["3.4.S1"], note="d13-080."))

facts.append(fact("route53-hybrid-endpoints-two-subnets-two-azs", "behavior",
 "For high availability, create inbound or outbound endpoints with at least two subnets in different Availability Zones, and use both endpoint IP addresses in the on-premises DNS resolver for an inbound endpoint.",
 "How do you make a Resolver endpoint highly available?",
 [("subnets", "at least two subnets in different Availability Zones")], "Route 53 VPC Resolver endpoints",
 [ev(WP + "route-53-resolver-endpoints-and-forwarding-rules", "When you create the inbound or outbound endpoints, we recommend that you use at least two subnets in different Availability Zones for high availability. For the inbound resolver, ensure that you use both endpoint IP addresses in your on-premises DNS resolver so the load can be spread across all available IP addresses.")],
 rel="extended", bullets=["3.4.S1"], note="d13-080."))

facts.append(fact("route53-hybrid-own-forwarders-on-ec2-alternative", "capability",
 "As an alternative to Resolver endpoints, you can deploy and manage your own DNS infrastructure on EC2 instances to handle DNS requests from VPCs or on-premises, and the whitepaper names logging DNS queries as one reason to run your own forwarders.",
 "What is the alternative to Resolver endpoints for hybrid DNS and why would you use it?",
 [("ec2", "additional DNS infrastructure running on EC2 instances"), ("log", "One reason to run your own forwarders is to log DNS queries.")], "hybrid DNS between a VPC and on-premises",
 [ev(WP + "secondary-dns-in-an-amazon-vpc", "Alternatively, you might decide to deploy and manage additional DNS infrastructure running on EC2 instances to handle DNS requests either from VPCs or on-premises, where you can still benefit from using AWS Managed Services."),
  ev(WP + "decentralized-conditional-forwarders", "While the Route 53 solution helps you avoid the complexities in running a hybrid DNS architecture, you might still prefer to configure your DNS infrastructure to use conditional forwarders within your VPCs. One reason to run your own forwarders is to log DNS queries.")],
 rel="extended", bullets=["3.4.S1"], note="d13-080. Compare with route53-hybrid-whitepaper-logging-reason-outdated."))

facts.append(fact("route53-hybrid-whitepaper-historical-banner", "behavior",
 "The hybrid cloud DNS whitepaper is for historical reference only, and some of its content might be outdated.",
 "Is the hybrid cloud DNS options whitepaper current?",
 [("banner", "for historical reference only")], "Hybrid Cloud DNS Options for Amazon VPC whitepaper",
 [ev(WP + "route-53-resolver-endpoints-and-forwarding-rules", "This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.")],
 rel="reference", bullets=["3.4.S1"], note="d13-080. Writers must not teach whitepaper limits as current."))

facts.append(fact("route53-hybrid-whitepaper-logging-reason-outdated", "behavior",
 "The hybrid DNS whitepaper gives logging DNS queries as a reason to run your own forwarders, but the guide history shows that support for Resolver query logs was added on September 1, 2020, so Resolver endpoints can now log queries.",
 "Can you log queries answered by the VPC Resolver without running your own forwarders?",
 [("added", "Added support for Resolver query logs."), ("reason", "One reason to run your own forwarders is to log DNS queries.")], "Route 53 VPC Resolver query logging",
 [ev(HIST, "September 1, 2020 Added support for Resolver query logs."),
  ev(WP + "decentralized-conditional-forwarders", "One reason to run your own forwarders is to log DNS queries.")],
 rel="extended", bullets=["3.4.S1"], vol="frequently-changing", note="d13-080. Dated before the mid-2022 window, recorded because the whitepaper (historical) still states the old reason."))

# ---- security: health checkers ----
facts.append(fact("route53-health-check-allow-health-checker-ips", "restriction",
 "For a Route 53 health check to succeed, your router and firewall rules must allow inbound traffic from the IP addresses that the Route 53 health checkers use.",
 "What must your firewall allow for a Route 53 health check to pass?",
 [("allow", "must allow inbound traffic from the IP addresses")], "Amazon Route 53 health checks",
 [ev(R + "dns-failover-router-firewall-rules", "For a health check to succeed, your router and firewall rules must allow inbound traffic from the IP addresses that the Route 53 health checkers use.")],
 tier0=True, rel="core", bullets=["2.2.K6"], note="Security dimension."))

facts.append(fact("route53-health-check-aws-managed-prefix-list", "capability",
 "To allow Route 53 health checks in a security group you can allow inbound traffic from each IP address range or use an AWS-managed prefix list, which automatically adds all necessary ranges.",
 "How do you allow Route 53 health checkers in a security group without listing every IP range?",
 [("list", "you can either allow inbound traffic from each IP address range, or you can use an AWS-managed prefix list"), ("auto", "it automatically adds all necessary ranges")], "Amazon Route 53 health checks and EC2 security groups",
 [ev(R + "dns-failover-router-firewall-rules", "When you add the AWS-managed prefix list to your inbound security group, it automatically adds all necessary ranges."),
  ev(R + "dns-failover-router-firewall-rules", "To configure your security groups to allow Route 53 health checks, you can either allow inbound traffic from each IP address range, or you can use an AWS-managed prefix list.")],
 tier0=True, rel="core", bullets=["2.2.K6"], vol="frequently-changing",
 change_items=["whats-new-v2#about-aws-whats-new-2023-09-amazon-route-53-managed-prefix-lists-health-checks"],
 note="Security dimension. The feed lists the change on 2023-09-08 (AWS-managed prefix lists for health checks); that What's New post is blocked by robots.txt, so no dated quote exists."))

# ---- SLA ----
facts.append(fact("route53-sla-unavailable-all-four-name-servers", "sla",
 "Under the Amazon Route 53 SLA a hosted zone is unavailable in a given minute only if all four virtual name servers assigned to it fail to respond to all DNS queries during that minute.",
 "When does the Route 53 SLA count a hosted zone as unavailable?",
 [("def", "all four virtual name servers assigned to the Hosted Zone fail to respond")], "Amazon Route 53 Authoritative DNS SLA, per hosted zone",
 [ev("www/route53/sla", "A Hosted Zone is “Unavailable” during a given minute if all four virtual name servers assigned to the Hosted Zone fail to respond to all DNS queries made to the Hosted Zone throughout the minute.")],
 rel="extended", bullets=["2.2.K6"], vol="frequently-changing", note="SLA page last updated April 16, 2025."))

facts.append(fact("route53-sla-credit-starts-below-100-percent", "sla",
 "The Amazon Route 53 SLA gives a 10% service credit when a hosted zone's monthly uptime is below 100% but at least 99.99%, a 25% credit below 99.99% but at least 99.95%, and a 100% credit below 99.95%.",
 "Which service credit does the Route 53 SLA give at each monthly uptime level?",
 [("tier1", "Less than 100% but greater than or equal to 99.99%"), ("tier3", "Less than 99.95%")], "Amazon Route 53 SLA, hosted zones outside GovCloud",
 [ev("www/route53/sla", "| Less than 100% but greater than or equal to 99.99% | 10% |", header="| Monthly Uptime Percentage for a Hosted Zone (other than a Hosted Zone in a GovCloud region) | Service Credit Percentage |"),
  ev("www/route53/sla", "| Less than 99.99% but greater than or equal to 99.95% | 25% |", header="| Monthly Uptime Percentage for a Hosted Zone (other than a Hosted Zone in a GovCloud region) | Service Credit Percentage |"),
  ev("www/route53/sla", "| Less than 99.95% | 100% |", header="| Monthly Uptime Percentage for a Hosted Zone (other than a Hosted Zone in a GovCloud region) | Service Credit Percentage |")],
 rel="extended", bullets=["2.2.K6"], vol="frequently-changing", note="Credits are a percentage of the Route 53 query charges for the affected hosted zone."))

if __name__ == "__main__":
    json.dump(facts, open("aws-saa-book/_build/work/13-route53/facts-dc-07.json", "w"), indent=0, ensure_ascii=False)
    print(len(facts))
