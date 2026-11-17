import json

def ev(sid, quote, url=None, header=None):
    if url is None:
        if sid.startswith("docs/"):
            url = "https://docs.aws.amazon.com/" + sid[5:] + ".html"
        elif sid.startswith("www/"):
            url = "https://aws.amazon.com/" + sid[4:] + "/"
    return {"source_id": sid, "url": url, "quote": quote, "table_header": header}

R = "docs/Route53/latest/DeveloperGuide/"
DG = "docs/decision-guides/latest/decision-guides/choosing-networking-and-content-delivery-service"
REL = "docs/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system"

def fact(id, kind, claim, question, values, scope, evidence, hard=True, tier0=False, rel="extended", bullets=None,
         note="", vol="stable", dom="", adj=False, cond="", change_items=None, changed=None, tier=1):
    f = {"id": id, "service": "route53", "home_chapter": "13", "kind": kind, "claim": claim, "question": question,
         "values": [{"key": k, "display": d} for k, d in values],
         "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
         "evidence": evidence, "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol, "changed": changed,
         "exam_relevance": rel, "bullets": bullets or []}
    if change_items:
        f["change_items"] = change_items
    if note:
        f["note"] = note
    return f

facts = []

facts.append(fact("route53-decision-guide-edge-category-vs-elb", "capability",
 "In the AWS networking decision guide, edge networking services provide higher performance through caching and optimized transport, Amazon Route 53 routes customer traffic for availability, AWS Global Accelerator routes traffic to make the most of the AWS global infrastructure, and Elastic Load Balancing helps workloads in your VPCs scale and stay highly available.",
 "How does the decision guide place Route 53 next to CloudFront, Global Accelerator and Elastic Load Balancing?",
 [("edge", "higher performance through caching and optimized transport"), ("ga", "make the most of the AWS global infrastructure"), ("elb", "scale and provide high availability")], "AWS networking and content delivery decision guide",
 [ev(DG, "Services in this category help ensure higher performance through caching and optimized transport."),
  ev(DG, "You'll also want to see customer traffic optimally routed to provide availability using services such as Amazon Route 53."),
  ev(DG, "Additionally, it's important that customer traffic is routed to make the most of the AWS global infrastructure using services such as AWS Global Accelerator."),
  ev(DG, "As customer demand increases, you can help ensure that the workloads in your VPCs can scale and provide high availability by using Elastic Load Balancing.")],
 tier0=True, rel="core", bullets=["4.4.K7"], note="d13-107."))

facts.append(fact("route53-decision-guide-ga-reliability-latency", "capability",
 "The networking decision guide says AWS Global Accelerator can help you improve the reliability, security and latency of your workloads, and recommends it for gaming, IoT and VoIP workloads.",
 "When does the decision guide point to Global Accelerator?",
 [("ga", "improve the reliability, security, and latency of your workloads")], "AWS Global Accelerator in the networking decision guide",
 [ev(DG, "AWS Global Accelerator can help you improve the reliability, security, and latency of your workloads."),
  ev(DG, "If you’re running gaming, Internet of Things (IoT), or Voice over IP (VoIP) workloads, consider using AWS Global Accelerator.")],
 rel="extended", bullets=["4.4.K7"], note="d13-067, d13-107."))

facts.append(fact("route53-primarily-global-regional-features", "behavior",
 "Amazon Route 53 is primarily a global service, but VPC Resolver endpoints and rules, health checks of resources in specific Regions, and the choice of Regions that health checks run from are Regional.",
 "Is Route 53 a global or a Regional service?",
 [("global", "Route 53 is primarily a global service")], "Amazon Route 53",
 [ev(R + "disaster-recovery-resiliency", "Route 53 is primarily a global service, but the following features support AWS Regions:"),
  ev(R + "disaster-recovery-resiliency", "For outbound endpoints, you create rules in the same Region where you created the endpoint."),
  ev(R + "disaster-recovery-resiliency", "You can configure Route 53 health checks to check the health of resources that you create in specific Regions, such as Amazon EC2 instances and Elastic Load Balancing load balancers.")],
 tier0=True, rel="core", bullets=["2.2.K1"], note="d13-006."))

facts.append(fact("route53-rel10-distribute-across-azs-or-regions", "behavior",
 "REL10-BP01 says to distribute workload data and resources across multiple Availability Zones or, where necessary, across AWS Regions, and its list of common anti-patterns includes implementing a multi-Region architecture when a multi-AZ architecture would satisfy business requirements.",
 "What does REL10-BP01 say about multiple Availability Zones and Regions?",
 [("rule", "across multiple Availability Zones or, where necessary, across AWS Regions"), ("anti", "when a multi-AZ architecture would satisfy business requirements")], "Well-Architected REL10-BP01",
 [ev(REL, "Distribute workload data and resources across multiple Availability Zones or, where necessary, across AWS Regions."),
  ev(REL, "You implement a multi-Region architecture when a multi-AZ architecture would satisfy business requirements.")],
 rel="extended", bullets=["2.2.S2"], note="d13-070."))

facts.append(fact("route53-failover-active-passive-primary-then-secondary", "behavior",
 "In active-passive failover, Amazon Route 53 responds with the healthy primary resources, and only when all primary resources are unhealthy does it begin to answer with the healthy secondary resources.",
 "When does Route 53 answer with the secondary record in a failover setup?",
 [("primary", "Route 53 includes only the healthy primary resources"), ("secondary", "begins to include only the healthy secondary resources")], "Amazon Route 53 active-passive failover",
 [ev(R + "dns-failover-types", "When responding to queries, Route 53 includes only the healthy primary resources. If all the primary resources are unhealthy, Route 53 begins to include only the healthy secondary resources in response to DNS queries.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-104."))

facts.append(fact("route53-failover-active-active-any-policy-but-failover", "behavior",
 "You configure active-active failover with any routing policy (or combination of routing policies) other than failover, and active-passive failover with the failover routing policy.",
 "Which routing policy gives active-passive failover and which give active-active?",
 [("ap", "you configure active-passive failover using the failover routing policy")], "Amazon Route 53 health checking and failover",
 [ev(R + "dns-failover-types", "You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.")],
 tier0=True, rel="core", bullets=["2.2.S2"], note="d13-104."))

facts.append(fact("route53-failover-one-primary-one-secondary-required", "restriction",
 "For failover to work correctly you must create one primary and one secondary failover record, with the same name and the same record type.",
 "What records make up a failover configuration?",
 [("pair", "you must create one primary and one secondary failover record")], "Amazon Route 53 failover records",
 [ev(R + "resource-record-sets-values-failover", "For failover to function correctly, you must create one primary and one secondary failover record."),
  ev(R + "resource-record-sets-values-failover", "Select the same value for both the primary and secondary failover records."),
  ev(R + "resource-record-sets-values-failover", "Enter the same name for both of the records in the group of failover records.")],
 rel="core", bullets=["2.2.S2"], note="d13-104. The two later quotes say the record type and the record name are the same for both records."))

facts.append(fact("route53-failover-record-health-check-checks-its-own-endpoint", "behavior",
 "Amazon Route 53 does not check the health of the endpoint in the record value; when you select a health check for a record, Route 53 checks the endpoint that you specified in the health check.",
 "Which endpoint does Route 53 check when a record has a health check?",
 [("own", "Route 53 checks the health of the endpoint that you specified in the health check")], "Amazon Route 53 records and health checks",
 [ev(R + "resource-record-sets-values-failover", "Route 53 doesn't check the health of the endpoint specified in the record, for example, the endpoint specified by the IP address in the Value field. When you select a health check for a record, Route 53 checks the health of the endpoint that you specified in the health check.")],
 rel="extended", bullets=["2.2.K6"], note="d13-104."))

facts.append(fact("route53-failover-alias-health-check-and-evaluate-both-true", "behavior",
 "If you associate a health check with an alias record and also select Yes for Evaluate Target Health, both must evaluate to true for the record to be used.",
 "What happens when an alias record has both a health check and Evaluate Target Health set to Yes?",
 [("both", "both must evaluate to true")], "Amazon Route 53 alias records with health checks",
 [ev(R + "resource-record-sets-values-failover", "If you associate a health check with an alias record and also select Yes for Evaluate Target Health, both must evaluate to true.")],
 rel="extended", bullets=["2.2.K6"], note="d13-104."))

facts.append(fact("route53-failover-multiple-primary-healthy-if-one-healthy", "behavior",
 "When several resources are associated with the primary failover record, Amazon Route 53 considers the primary record healthy as long as at least one of the associated resources is healthy.",
 "When is a primary failover record with several resources considered healthy?",
 [("one", "as long as at least one of the associated resources is healthy")], "Amazon Route 53 active-passive failover",
 [ev(R + "dns-failover-types", "In this configuration, Route 53 considers the primary failover record to be healthy as long as at least one of the associated resources is healthy.")],
 rel="extended", bullets=["2.2.S2"], note="d13-104."))

facts.append(fact("route53-change-cloudfront-flat-rate-plans-route53-2025-11", "change",
 "On 2025-11-18 AWS announced flat-rate pricing plans, available with Amazon CloudFront, that combine content delivery with AWS WAF, DDoS protection and Amazon Route 53 DNS into a simple monthly price with no overage charges.",
 "Which pricing option bundles Route 53 DNS with CloudFront at a monthly price without overages?",
 [("date", "2025-11-18"), ("plans", "flat-rate pricing plans")], "Amazon CloudFront flat-rate plans and Amazon Route 53 DNS",
 [ev("www/about-aws/whats-new/2025/11/aws-flat-rate-pricing-plans", "Posted on: Nov 18, 2025 Amazon Web Services (AWS) is launching flat-rate pricing plans with no overages for website delivery and security.", "https://aws.amazon.com/about-aws/whats-new/2025/11/aws-flat-rate-pricing-plans"),
  ev("www/about-aws/whats-new/2025/11/aws-flat-rate-pricing-plans", "The flat-rate plans, available with Amazon CloudFront, combine global content delivery with AWS WAF, DDoS protection, Amazon Route 53 DNS, Amazon CloudWatch Logs ingestion, and serverless edge compute into a simple monthly price with no overage charges.", "https://aws.amazon.com/about-aws/whats-new/2025/11/aws-flat-rate-pricing-plans")],
 rel="extended", bullets=["4.4.K7"], vol="frequently-changing", note="Cost dimension. Chapter 15 owns CloudFront. Accelerated recovery does not support CloudFront flat-rate plans at this time (accelerated recovery page)."))

if __name__ == "__main__":
    json.dump(facts, open("aws-saa-book/_build/work/13-route53/facts-dc-10.json", "w"), indent=0, ensure_ascii=False)
    print(len(facts))
