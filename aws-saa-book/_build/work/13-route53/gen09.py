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
WN = "whats-new-v2#about-aws-whats-new-"

def fact(id, kind, claim, question, values, scope, evidence, hard=True, tier0=False, rel="extended", bullets=None,
         note="", vol="frequently-changing", dom="", adj=False, cond="", change_items=None, changed=None, tier=1):
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

def hist(idx, claim, question, date_disp, scope, quote, items, rel="extended", bullets=None, note="", extra=None, tier0=False):
    evs = [ev(HIST, quote)]
    if extra:
        evs += extra
    facts.append(fact(idx, "change", claim, question, [("date", date_disp)], scope, evs, rel=rel, bullets=bullets or ["4.4.K7"],
                      note=note, change_items=items, tier0=tier0))

hist("route53-change-ip-based-routing-2022-06",
     "On June 1, 2022 the IP-based routing option became available in Amazon Route 53.",
     "When was IP-based routing added to Route 53?", "June 1, 2022", "Amazon Route 53 routing policies",
     "June 1, 2022 IP-based routing option is now available in Amazon Route 53.", [],
     bullets=["3.4.S1"], note="Dated just before the mid-2022 window. Older questions list no IP-based policy. Current truth: route53-choose-ip-based-routing-known-client-ips.")

hist("route53-change-phz-geolocation-latency-2022-03",
     "On March 16, 2022 geolocation and latency-based routing became supported for private hosted zones in Amazon Route 53.",
     "Since when can geolocation and latency routing be used in a private hosted zone?", "March 16, 2022", "Amazon Route 53 private hosted zones",
     "March 16, 2022 Geolocation and latency-based routing options are now supported for private hosted zones in Amazon Route 53.", [],
     rel="core", bullets=["3.4.S1"], tier0=True,
     note="Dated before the mid-2022 window; older questions may assume private hosted zones support only some policies. Current truth: route53-phz-routing-policy-support.",
     extra=[ev(R + "routing-policy-geo", "You can use geolocation routing for records in both public and private hosted zones.")])

facts.append(fact("route53-phz-routing-policy-support", "restriction",
 "In a private hosted zone you can use simple, failover, geolocation, geoproximity, latency, multivalue answer and weighted routing, but you cannot use IP-based routing.",
 "Which routing policies work in a private hosted zone?",
 [("no", "You cannot use IP-based routing policy for records in a private hosted zone.")], "Amazon Route 53 private hosted zones",
 [ev(R + "routing-policy", "You can use simple routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use failover routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use geolocation routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use geoproximity routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use latency routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use multivalue answer routing to create records in a private hosted zone."),
  ev(R + "routing-policy", "You can use weighted routing to create records in a private hosted zone."),
  ev(R + "routing-policy-ipbased", "You cannot use IP-based routing policy for records in a private hosted zone.")],
 tier0=True, rel="core", bullets=["3.4.S1"], vol="frequently-changing", change_items=[],
 note="Current truth after the 2022-03-16 change (route53-change-phz-geolocation-latency-2022-03)."))

hist("route53-change-record-set-permissions-2022-09",
     "On September 21, 2022 you could start to use IAM policy conditions to give users fine-grained access to updating resource record sets in Amazon Route 53.",
     "Since when can an IAM policy limit which record sets a user can change?", "September 21, 2022", "Amazon Route 53 IAM policies",
     "September 21, 2022 You can now use policy conditions for giving users fine-grained access to updating resource record sets in Amazon Route 53.",
     [WN + "2022-09-amazon-route-53-support-dns-resource-record-set-permissions"], rel="extended", bullets=["3.4.S1"],
     note="Security dimension. The What's New post is blocked by robots.txt; the History row is the quote.")

hist("route53-change-vpcs-condition-2024-09",
     "On September 3, 2024 the route53:VPCs policy condition could be used to grant fine-grained access to managing hosted zone associations to VPCs.",
     "Which IAM condition limits which VPCs a user can associate with a hosted zone?", "September 3, 2024", "Amazon Route 53 IAM policies",
     "September 3, 2024 You can now use `route53:VPCs` policy condition to grant fine-grained access to managing hosted zone associations to VPCs.", [],
     rel="extended", bullets=["3.4.S1"], note="Security dimension.")

hist("route53-change-geoproximity-records-console-2024-01",
     "On January 9, 2024 the Quick create record and the Create record wizard began to support creating geoproximity routing records.",
     "Since when can you create geoproximity records without Traffic Flow?", "January 9, 2024", "Amazon Route 53 geoproximity routing",
     "January 9, 2024 You can now use the Quick create record or the Create record wizard to create geoproximity routing records.",
     [WN + "2024-01-amazon-route-53-expands-geoproximity-routing"], rel="extended", bullets=["3.4.S1"],
     note="Older material says geoproximity needs Traffic Flow; the History row does not say this verbatim, so no old value is recorded. The geoproximity page still says the maps are available only with Traffic Flow.")

hist("route53-change-geoproximity-local-zones-2023-07",
     "On July 19, 2023 AWS Local Zones could be used with geoproximity routing, in Traffic Flow only, after you enable them.",
     "Can geoproximity routing target Local Zones?", "July 19, 2023", "Amazon Route 53 geoproximity routing",
     "July 19, 2023 You can now use Local Zones with geoproximity routing (traffic flow only) after you enable them.",
     [WN + "2023-10-amazon-route-53-traffic-flow-geoproximity-routing-local-zones"], rel="reference", bullets=["3.4.S1"],
     note="The What's New feed dates the Local Zones post 2023-10-19; the History page dates it July 19, 2023.")

hist("route53-change-dns-over-https-resolver-2023-12",
     "On December 20, 2023 DNS over HTTPS became usable with Resolver endpoints.",
     "Since when can Resolver endpoints use DNS over HTTPS?", "December 20, 2023", "Route 53 VPC Resolver endpoints",
     "December 20, 2023 You can now use DNS over HTTPS with Resolver endpoints.",
     [WN + "2023-12-amazon-route-53-resolver-endpoints-doh"], rel="reference", bullets=["3.4.S1"], note="Security dimension.")

hist("route53-change-resolver-delegation-2025-06",
     "On June 24, 2025 inbound and outbound delegation became usable with VPC Resolver.",
     "Since when can you delegate a private hosted zone subdomain through Resolver endpoints?", "June 24, 2025", "Route 53 VPC Resolver endpoints",
     "June 24, 2025 You can now use inbound and outbound delegation with VPC Resolver.",
     ["whats-new-v2#v1717268361"], rel="extended", bullets=["3.4.S1"],
     note="The What's New post says delegation lets you delegate authority for a subdomain between on-premises DNS and Resolver, instead of conditional forwarding rules.",
     extra=[ev("www/about-aws/whats-new/2025/06/amazon-route-53-resolver-endpoints-dns-delegation-private-hosted-zones", "With today’s release, customers can instead delegate authority of subdomains to Route 53 using name server records and vice versa, achieving compatibility with common, on-premises DNS infrastructure and removing the need for teams to use conditional forwarding rules throughout their organization.", "https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-route-53-resolver-endpoints-dns-delegation-private-hosted-zones")])

hist("route53-change-alias-vpc-lattice-2025-06",
     "On June 25, 2025 Amazon Route 53 began to support alias records for VPC Lattice service custom domain endpoints.",
     "Since when can an alias record point to a VPC Lattice service?", "June 25, 2025", "Amazon Route 53 alias records",
     "June 25, 2025 Amazon Route 53 now supports alias records for VPC Lattice service custom domain endpoints.", [],
     rel="reference", bullets=["4.4.K7"], note="The pricing page free-alias list does not include VPC Lattice.")

hist("route53-change-alias-cloudfront-tenant-2025-04",
     "On April 28, 2025 you could start to add an alias record to a CloudFront distribution tenant.",
     "Since when can an alias record point to a CloudFront distribution tenant?", "April 28, 2025", "Amazon Route 53 alias records",
     "April 28, 2025 You can now add an alias record to a CloudFront distribution tenant.", [],
     rel="reference", bullets=["4.4.K7"])

hist("route53-change-alias-opensearch-2025-01",
     "On January 14, 2025 Amazon Route 53 began to support alias records for OpenSearch Service custom domain endpoints.",
     "Since when can an alias record point to an OpenSearch Service domain?", "January 14, 2025", "Amazon Route 53 alias records",
     "January 14, 2025 Amazon Route 53 now supports alias records for OpenSearch Service custom domain endpoints.", [],
     rel="reference", bullets=["4.4.K7"])

hist("route53-change-record-types-https-sshfp-svcb-tlsa-2024-10",
     "On October 29, 2024 support was added for the HTTPS, SSHFP, SVCB and TLSA DNS record types in Amazon Route 53.",
     "Which record types did Route 53 add in October 2024?", "October 29, 2024", "Amazon Route 53 supported DNS record types",
     "October 29, 2024 Added support for HTTPS, SSHFP, SVCB, and TLSA DNS record types.",
     ["whats-new-v2#v1377891199"], rel="extended", bullets=["4.4.K7"],
     note="The What's New feed dates the post 2024-10-30; the History page says October 29, 2024. Current types list: Supported DNS record types page.",
     extra=[ev(R + "ResourceRecordTypes", "Amazon Route 53 supports the DNS record types that are listed in this section.")])

hist("route53-change-resolver-ipv6-dual-stack-2023-03",
     "On March 10, 2023 Route 53 VPC Resolver endpoints began to support IPv4, IPv6 and dual-stack endpoints for connecting to your resources.",
     "Since when can Resolver endpoints use IPv6?", "March 10, 2023", "Route 53 VPC Resolver endpoints",
     "March 10, 2023 You can now connect to your resources by using IPv4, IPv6, or dual-stack endpoints with Route 53 VPC Resolver.",
     [WN + "2023-03-amazon-route-53-resolver-endpoints-hybrid-cloud-ipv6-support"], rel="reference", bullets=["3.4.S1"],
     note="The History row uses the new name VPC Resolver for a 2023 event; the rename was announced 2025-11-30.")

hist("route53-change-dns-firewall-query-type-2024-01",
     "On January 9, 2024 the DNS query type became usable as an optional value of a DNS Firewall rule, to differentiate the rule's response for a specific query type.",
     "Since when can a DNS Firewall rule act on the DNS query type?", "January 9, 2024", "Resolver DNS Firewall",
     "January 9, 2024 You can now use the DNS query type as an optional value for DNS Firewall rule to differentiate the rule's response for a specific DNS query type.",
     [WN + "2024-01-amazon-route-53-resolver-dns-firewall-query-type-filtering"], rel="reference", bullets=["4.4.K7"])

hist("route53-change-dns-firewall-security-hub-2025-01",
     "On January 13, 2025 Resolver DNS Firewall findings were added to Security Hub CSPM.",
     "Since when does Resolver DNS Firewall send findings to Security Hub?", "January 13, 2025", "Resolver DNS Firewall",
     "January 13, 2025 Added Resolver DNS Firewall findings to the Security Hub CSPM.",
     ["whats-new-v2#p186343594"], rel="reference", bullets=["4.4.K7"], note="Security dimension.")

hist("route53-change-dns-firewall-eventbridge-2024-02",
     "On February 5, 2024 Amazon EventBridge could be used for real time alerts with DNS Firewall.",
     "Since when can DNS Firewall events go to EventBridge?", "February 5, 2024", "Resolver DNS Firewall",
     "February 5, 2024 You can now use Amazon EventBridge for real time alerts with DNS Firewall.", [],
     rel="reference", bullets=["4.4.K7"], note="Security dimension.")

hist("route53-change-resolver-detailed-metrics-2025-12",
     "On December 15, 2025 detailed CloudWatch metrics were added for Route 53 Resolver endpoints.",
     "When were detailed CloudWatch metrics added for Resolver endpoints?", "December 15, 2025", "Route 53 VPC Resolver endpoints",
     "December 15, 2025 Added detailed CloudWatch metrics for Route 53 Resolver endpoints.",
     ["whats-new-v2#launch-umqexyzlx93khoicw4km5x"], rel="reference", bullets=["3.4.S1"],
     note="The newest row of the History page. The What's New feed dates the post 2025-12-16.")

if __name__ == "__main__":
    json.dump(facts, open("aws-saa-book/_build/work/13-route53/facts-dc-09.json", "w"), indent=0, ensure_ascii=False)
    print(len(facts))
