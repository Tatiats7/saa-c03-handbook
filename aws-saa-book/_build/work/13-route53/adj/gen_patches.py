"""adjudicate-13: build one `facts amend` patch per disputed fact (writes adj/p/<id>.json). Spec only; no tool calls."""
import json, os, copy

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SNAP = os.path.join(B, "_build/corpus/snap")
OUT = os.path.join(HERE, "p")
os.makedirs(OUT, exist_ok=True)

facts = {}
for line in open(os.path.join(B, "data/facts/route53.jsonl")):
    f = json.loads(line)
    facts[f["id"]] = f

WN_AR = "www/about-aws/whats-new/2025/11/amazon-route-53-accelerated-recovery-managing-public-dns-records"
AR = "docs/Route53/latest/DeveloperGuide/accelerated-recovery"
WN_FW = "www/about-aws/whats-new/2026/05/amazon-route-53-resolver-dns"
GEO = "docs/Route53/latest/DeveloperGuide/routing-policy-geoproximity"
GEOV = "docs/Route53/latest/DeveloperGuide/resource-record-sets-values-geoprox"
FWO = "docs/Route53/latest/DeveloperGuide/resolver-dns-firewall-overview"
FWA = "docs/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-actions"
REG = "docs/Route53/latest/DeveloperGuide/welcome-domain-registration"
FAQ = "www/route53/faqs"
RQL = "docs/Route53/latest/DeveloperGuide/resolver-query-logs"
WP = "docs/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/decentralized-conditional-forwarders"
MIG = "docs/Route53/latest/DeveloperGuide/MigratingDNS"
LL = "docs/Route53/latest/DeveloperGuide/resolver-availability-scaling"

S = {}

S["route53-accelerated-recovery-60-minute-rto"] = dict(
    claim="Since 2025-11-26 you can turn on accelerated recovery for a Route 53 public hosted zone. It targets a 60-minute Recovery Time Objective (RTO) for making DNS changes again if the US East (N. Virginia) Region becomes unavailable, using a copy of the zone kept in the US West (Oregon) Region, and you must turn it on before any issues with that Region occur. Before it, customers could not modify or recreate DNS records while AWS services in US East (N. Virginia) were unavailable.",
    rep={0: "Route 53 accelerated recovery for managing public DNS records helps you achieve a 60-minute Recovery Time Objective (RTO) if the US East (N. Virginia) Region becomes unavailable. When you turn on this feature for a Route 53 public hosted zone, you can resume making DNS changes within about 60 minutes after AWS detects that the US East (N. Virginia) Region is impaired."},
    add=[(WN_AR, "Posted on: Nov 26, 2025 Amazon Route 53 is excited to release the accelerated recovery option for managing DNS records in public hosted zones."),
         (AR, "You must turn on accelerated recovery before any issues with the US East (N. Virginia) Region occur.")])

S["route53-accelerated-recovery-data-plane-keeps-answering"] = dict(
    claim="DNS query resolution from the Route 53 data plane continues to work normally during Regional service impairment. Accelerated recovery is about regaining the ability to make DNS changes: during a failover, Route 53 routes control plane requests for enabled hosted zones to the US West (Oregon) Region.",
    add=[(WN_AR, "Accelerated recovery targets a 60-minute recovery time objective (RTO) for regaining the ability to make DNS changes to your DNS records in Route 53 public hosted zones, if AWS services in US East (N. Virginia) become temporarily unavailable.")])

S["route53-alias-evaluate-target-health-weighted-branch"] = dict(
    claim="If an alias record has Evaluate Target Health set to Yes and its alias target is a group of weighted records that all have nonzero weights, Route 53 considers the alias record healthy as long as at least one of the weighted records is healthy, and unhealthy if none of the weighted records is healthy. Route 53 stops considering records in that branch of the tree until at least one weighted record becomes healthy again.",
    qual={"condition": "the weighted records all have nonzero weights"},
    add=[(0, "You can also configure health checking for alias records by setting **Evaluate Target Health** to **Yes** for each alias record."),
         (0, "For example, suppose the alias target for an alias record is a group of weighted records that all have nonzero weights:"),
         (0, "Route 53 stops considering records in that branch of the tree until at least one weighted record becomes healthy again.")])

S["route53-alias-target-another-record-all-types-except-ns-soa"] = dict(
    claim="For an alias to another record in the same hosted zone, all record types are supported except NS and SOA. At the zone apex, an alias record can't route traffic to a record whose type is CNAME.",
    qual={"condition": "at the zone apex, not to a CNAME record"},
    add=[(0, "If you're creating an alias record that has the same name as the hosted zone (known as the *zone apex*), you can't route traffic to a record for which the value of **Type** is **CNAME**.")])

S["route53-case-intraway-multi-region-availability"] = dict(
    claim="The Intraway case study says that by activating on AWS in more than one Region, Intraway could multiply the availability of its existing resources instead of dividing them; the case study lists Amazon Route 53 among the AWS services that Intraway uses.")

S["route53-change-dns-firewall-categories-2026-05"] = dict(
    add=[(0, "The new category lists are available under the expanded DNS Firewall Advanced rule tier, while existing Managed Domain Lists remain under the DNS Firewall Foundational rule tier.")])

S["route53-change-geoproximity-local-zones-2023-07"] = dict(
    claim="On July 19, 2023 the Route 53 guide history recorded that you could use Local Zones with geoproximity routing (traffic flow only) after you enable them. The current guide also offers Local Zone Groups for geoproximity records: for AWS resources you specify the AWS Region or Local Zone Group that you created the resource in, and you must first enable Local Zones.",
    qual={"condition": "Local Zones must be enabled first"},
    add=[(GEO, "If you're using AWS resources, specify the AWS Region or Local Zone Group that you created the resource in."),
         (GEO, "To use AWS Local Zones, you have to first enable them."),
         (GEOV, "**AWS Local Zone Group** Choose an available Local Zone Group from the **Location** list.")])

S["route53-change-resolver-dns64-ipv6-2026-05"] = dict(
    add=[(0, "With DNS64 enabled on inbound endpoints, you can synthesize AAAA (IPv6) responses for domains that only have A (IPv4) records, allowing IPv6-only clients on-premises to reach IPv4 services on AWS without changes to those services.")])

S["route53-change-vpc-resolver-rename-2025-11"] = dict(
    add=[(0, "Posted on: Nov 30, 2025 Today, AWS announced the preview of Amazon Route 53 Global Resolver, a new internet-reachable DNS resolver that provides easy, secure, and reliable DNS resolution from anywhere for queries made by your authorized clients.")])

S["route53-cloudfront-alias-evaluate-target-health-default-no"] = dict(
    rep={0: "**Evaluate target health** Accept the default value of **No**."})

S["route53-cname-target-need-not-be-route53"] = dict(
    claim="A CNAME record can redirect DNS queries to any DNS record, for example from acme.example.com to zenith.example.com or to acme.example.org, and you don't need to use Route 53 as the DNS service for the domain that you're redirecting queries to.",
    rep={0: "A CNAME record can redirect DNS queries to any DNS record. For example, you can create a CNAME record that redirects queries from acme.example.com to zenith.example.com or to acme.example.org. You don't need to use Route 53 as the DNS service for the domain that you're redirecting queries to."})

S["route53-complex-config-health-check-and-eth-both-must-pass"] = dict(
    claim="If you assign a health check to a latency alias record whose alias target is a group of weighted records, and set Evaluate Target Health to Yes for that latency alias record, both of the following must be true before Route 53 returns the value of a weighted record: the health check associated with the latency alias record must pass, and at least one weighted record must be considered healthy.",
    qual={"scope": "latency alias record with a health check and Evaluate Target Health, whose alias target is a group of weighted records"},
    add=[(0, "You assign a health check to a latency alias record for which the alias target is a group of weighted records."),
         (0, "You set the value of **Evaluate Target Health** to **Yes** for the latency alias record."),
         (0, "At least one weighted record must be considered healthy, either because it's associated with a health check that passes or because it's not associated with a health check.")])

S["route53-complex-config-latency-alias-weighted-tree"] = dict(
    add=[(0, "For example, you might use latency alias records to select a Region close to a user and use weighted records for two or more resources within each Region to protect against the failure of a single endpoint or an Availability Zone.")])

S["route53-cross-account-auth-by-hosted-zone-account"] = dict(
    claim="The account that created the hosted zone authorizes the association of the VPC with the private hosted zone. Then the account that created the VPC associates the VPC with the hosted zone. For both steps you can use the AWS SDK, Tools for Windows PowerShell, the AWS CLI, or the Route 53 API.",
    rep={1: "Using the account that created the VPC, associate the VPC with the hosted zone. As with authorizing the association, you can use the AWS SDK, Tools for Windows PowerShell, the AWS CLI, or the Route 53 API."})

S["route53-cross-account-delete-authorization-recommended"] = dict(
    rep={0: "*Recommended* – Delete the authorization to associate the VPC with the hosted zone. Deleting the authorization does not affect the association, it just prevents you from reassociating the VPC with the hosted zone in the future."})

S["route53-dangling-delegate-only-to-zones-you-control"] = dict(
    claim="If you delegate a domain or subdomain to Route 53 name servers before you create a corresponding hosted zone, this creates dangling delegation records, and Route 53 cannot protect against this. To mitigate the risk, only delegate to Route 53 name servers that belong to a public hosted zone that you control.",
    rep={0: "Route 53 cannot protect against this because no hosted zone has ever existed to establish a hold on those name servers for that domain name. To mitigate the risk, only delegate to Route 53 name servers that belong to a public hosted zone that you control."},
    add=[(0, "You delegate a domain or subdomain to Route 53 name servers before creating a corresponding hosted zone, this creates dangling delegation records.")])

S["route53-dangling-delegation-match-parent-ns-to-delegation-set"] = dict(
    claim="There are dangling delegation record risks that Route 53 can't protect against. To protect yourself against them, make sure the parent NS records match the delegation set of the Route 53 hosted zone. Enabling DNSSEC signing for the hosted zone can serve as another layer of protection.",
    rep={0: "However, there are other dangling delegation record risks, which Route 53 can't protect against, as detailed in scenarios 2 through 5 in the following examples. To protect yourself against this broader set of risks, make sure the parent NS records match the delegation set for the Route 53 hosted zone."})

S["route53-decision-guide-edge-category-vs-elb"] = dict(
    claim="In the AWS networking and content delivery decision guide, edge networking and content delivery services help ensure higher performance through caching and optimized transport; Amazon Route 53 routes customer traffic to provide availability, AWS Global Accelerator routes customer traffic to make the most of the AWS global infrastructure, and Elastic Load Balancing helps the workloads in your VPCs scale and provide high availability.",
    rep={0: "**Edge networking and content delivery** Services in this category help ensure higher performance through caching and optimized transport."})

S["route53-dnsfw-action-block-responses"] = dict(
    rep={3: "** OVERRIDE **– Provide a custom override in the response. This option requires the following additional settings:"},
    add=[(0, "** Record type **– The DNS record's type. This determines the format of the record value. This must be `CNAME`.")])

S["route53-dnsfw-advanced-detects-threat-signatures"] = dict(
    claim="DNS Firewall Advanced protection detects suspicious DNS queries based on known threat signatures in DNS queries, such as DNS traffic associated with Domain Generation Algorithms (DGA) and DNS tunneling. Each rule in a rule group needs a single DNS Firewall Advanced protection setting, and the threat protection algorithms are managed and updated by AWS.",
    rep={0: "Detects suspicious DNS queries based on known threat signatures in DNS queries. Each rule in a rule group requires a single DNS Firewall Advanced protection setting."},
    add=[(WN_FW, "DNS Firewall Advanced extends this capability by detecting and blocking DNS traffic associated with Domain Generation Algorithms (DGA) and DNS Tunneling threats.")])

S["route53-dnsfw-advanced-rules-block-or-alert-only"] = dict(
    claim="In a DNS Firewall Advanced rule you can choose to either block, or alert on a query that matches the threat; the Allow action is not available for DNS Firewall Advanced.",
    values=[{"key": "only", "display": "choose to either block, or alert"}],
    rep={0: "In a DNS Firewall Advanced rule you can choose to either block, or alert on a query that matches the threat."},
    add=[(FWA, "** Allow ** – Stop inspecting the query and permit it to go through. Not available for DNS Firewall Advanced.")])

S["route53-dnsfw-query-type-default-all-types"] = dict(
    rep={0: "**Query type (Domain lists only)** The query type setting allows you to configure a DNS Firewall rule to filter a particular DNS query type. If you don't select a query type, the rule is applied to all DNS query types."})

S["route53-dnsfw-use-alert-to-test-blocking-rules"] = dict(
    rep={0: "When you first create a blocking rule, you can test it by configuring it with the action set to Alert. You can then look at the number of queries that the rule alerts on to see how many would be blocked if you set the action to Block."})

S["route53-dnssec-multi-vendor-not-supported"] = dict(
    claim="When you use DNSSEC signing, multi-vendor configurations are not supported. If you have configured white-label name servers, make sure those name servers are provided by a single DNS provider.",
    rep={0: "When you use DNSSEC signing, multi-vendor configurations are not supported. If you have configured white-label name servers (also known as vanity name servers or private name servers), make sure those name servers are provided by a single DNS provider."})

S["route53-domain-registration-makes-route53-the-dns-service"] = dict(
    add=[(0, "Assigns a set of four name servers to the hosted zone.")])

S["route53-domain-transfer-unlock-and-auth-code"] = dict(
    claim="To transfer a domain registration to Route 53, you must unlock the domain, because ICANN requires that you unlock your domain before you transfer it. An authorization code from the current registrar authorizes Route 53 to request the transfer; some top-level domains have additional requirements, for example a .co.za domain needs no authorization code.",
    qual={"condition": "some top-level domains have additional requirements; .co.za needs no authorization code"},
    rep={1: "An authorization code from the current registrar authorizes us to request that registration for the domain be transferred to Route 53. You'll enter this code in the Route 53 console later in the process. Some top-level domains have additional requirements:"},
    add=[(0, "You don't need to get an authorization code to transfer a .co.za domain to Route 53.")])

S["route53-dr-auto-failover-use-with-caution"] = dict(
    rep={0: "For an active/passive configuration such as pilot light, all traffic initially goes to the primary Region and switches to the disaster recovery Region if the primary Region is no longer available. This failover operation can be initiated either automatically or manually. Automatically initiated failover based on health checks or alarms should be used with caution. Even using the best practices discussed here, recovery time and recovery point will be greater than zero, incurring some loss of availability and data."})

S["route53-ec2-elastic-ip-recommended"] = dict(
    claim="When you use Route 53 to route traffic to an Amazon EC2 instance, AWS recommends that you also create an Elastic IP address and associate it with the instance, because an Elastic IP address ensures that the IP address of the instance will never change.")

S["route53-elb-health-check-routes-only-healthy-fails-open"] = dict(
    claim="An Application Load Balancer node routes requests only to the healthy targets in the enabled Availability Zones. If all targets fail health checks at the same time in all enabled Availability Zones, the load balancer fails open, which allows traffic to all targets in all enabled Availability Zones regardless of their health status.",
    add=[(0, "The effect of the fail-open is to allow traffic to all targets in all enabled Availability Zones, regardless of their health status, based on the load balancing algorithm.")])

S["route53-failover-weighted-zero-weight-caveat"] = dict(
    rep={0: "All the records with nonzero weights must be unhealthy before Route 53 starts to respond to DNS queries using records that have weights of zero. This can make your web application or website unreliable if the last healthy resource, such as a web server, can't handle all the traffic when other resources are unavailable."},
    add=[(0, "You can also use weighted records for active-passive failover, with caveats.")])

S["route53-faq-alias-is-route53-extension"] = dict(
    add=[(0, "You can create alias records to route traffic to selected AWS resources, including Amazon Elastic Load Balancing load balancers, Amazon CloudFront distributions, AWS Elastic Beanstalk environments, API Gateways, VPC interface endpoints, and Amazon S3 buckets that are configured as websites.")])

S["route53-faq-apex-alias-elb-three-types"] = dict(
    add=[(0, "Amazon Route 53 offers a special type of record called an 'Alias' record that lets you map your zone apex (example.com) DNS name to the DNS name for your ELB load balancer (such as my-loadbalancer-1234567890.us-west-2.elb.amazonaws.com).")])

S["route53-faq-authoritative-vs-recursive-dns"] = dict(
    add=[(0, "Instead, clients talk to recursive DNS services (also known as DNS resolvers) which find the correct authoritative answer for any DNS query.")])

S["route53-faq-bias-only-geoproximity-rules"] = dict(
    claim="Asked whether bias can be used for other Traffic Flow rules, the FAQ answers that bias can only be applied to geoproximity rules.",
    head={0: "Can I use bias for other Traffic Flow rules?"})

S["route53-faq-calculated-health-check-combines-results"] = dict(
    add=[(0, "For example, you can create a configuration which fails away from an endpoint if either its public-facing web page is unavailable, or if internal metrics such as CPU load, network in/out, or disk reads show that the server itself is unhealthy.")])

S["route53-faq-cloudfront-ip-addresses-vary-by-location"] = dict(
    claim="IP addresses of Amazon CloudFront endpoints vary based on your end user's location and can change at any time. An Alias record lets you map your zone apex (example.com) to your CloudFront distribution, and Route 53 responds to each request for the Alias record with the IP addresses for the distribution.",
    add=[(0, "Amazon Route 53 offers a special type of record called an ‘Alias’ record that lets you map your zone apex (example.com) DNS name to your Amazon CloudFront distribution (for example, d123.cloudfront.net)."),
         (0, "Route 53 responds to each request for an Alias record with the IP address(es) for the distribution.")])

S["route53-faq-domain-registration-auto-creates-hosted-zone"] = dict(
    claim="When you register a new domain name with Route 53, Route 53 automatically creates a hosted zone that stores the DNS records for the domain.",
    add=[(0, "Use the AWS Management Console or the API to register your new domain name."),
         (REG, "When you register a domain with Route 53, the service automatically makes itself the DNS service for the domain. It does the following:"),
         (REG, "Creates a hosted zone that has the same name as your domain.")])

S["route53-faq-domain-registration-creates-hosted-zone-and-charges"] = dict(
    claim="When you register a domain with Route 53, it creates a hosted zone for the domain. You are charged for that hosted zone and for the DNS queries against it that Route 53 serves; you can delete the hosted zone to stop these charges, but some TLDs require valid name servers, so for those you first get DNS service from another provider.",
    add=[(REG, "When you register a domain with Route 53, the service automatically makes itself the DNS service for the domain. It does the following:"),
         (REG, "Creates a hosted zone that has the same name as your domain."),
         (0, "Please note that some TLDs require you to have valid name servers as part of your domain name registration. For a domain name under one of these TLDs, you will need to procure DNS service from another provider and enter that provider’s name server addresses before you can safely delete your Route 53 hosted zone for that domain name.")])

S["route53-faq-failover-endpoint-outside-aws"] = dict(
    add=[(0, "For example, you may have a legacy application running in a datacenter outside AWS and a backup instance of that application running within AWS."),
         (0, "You can set up health checks of your legacy application running outside AWS, and if the application fails the health checks, you can fail over automatically to the backup instance in AWS.")])

S["route53-faq-failover-step-disables-records"] = dict(
    claim="When a health check fails and failover occurs, Route 53 disables the resource records for the failed endpoint and no longer serves them; this failover step causes traffic to be routed to the healthy endpoints instead.",
    qual={"condition": "in the FAQ example, after the application fails three consecutive health checks"},
    rep={0: "Route 53 disables the resource records for the failed endpoint and no longer serves these records. This is the failover step, which causes traffic to begin being routed to your healthy endpoint(s) instead of your failed endpoint."},
    add=[(0, "In this example, your application fails three consecutive health checks, triggering the following events.")])

S["route53-faq-geoproximity-region-or-lat-long"] = dict(
    claim="When you create a traffic flow policy, you can specify either an AWS Region (if you use AWS resources) or the latitude and longitude for each endpoint. In the FAQ example, geoproximity routing sends the DNS query of a user in Seattle to EC2 instances in US West (Oregon) rather than US East (Ohio), because Oregon is closer geographically.",
    qual={"scope": "Traffic Flow geoproximity rules"},
    add=[(0, "For example, suppose you have EC2 instances in the AWS US East (Ohio) region and in the US West (Oregon) region.")])

S["route53-faq-lbr-geo-no-extra-fee-pay-queries"] = dict(
    claim="There are no upfront fees or long term commitments to use Amazon Route 53 and Latency Based Routing (LBR); customers pay for the hosted zones and queries they actually use.",
    qual={"scope": "Latency Based Routing (LBR)"})

S["route53-faq-phz-failover-metric-based-health-checks"] = dict(
    add=[(0, "Yes, it is possible to configure DNS Failover by associating health checks with resource record sets within a Private DNS hosted zone.")])

S["route53-faq-private-dns-requires-vpc"] = dict(
    claim="To use Route 53 Private DNS you must configure a VPC and migrate your resources into it, because Private DNS uses a VPC to manage visibility and provide DNS resolution for private hosted zones.",
    rep={0: "Route 53 Private DNS uses VPC to manage visibility and provide DNS resolution for private DNS hosted zones. To take advantage of Route 53 Private DNS, you must configure a VPC and migrate your resources into it."})

S["route53-faq-query-logging-to-cloudwatch-logs"] = dict(
    claim="You can configure Amazon Route 53 to log information about the queries that it receives, including date-time stamp, domain name, query type and location; when you configure query logging, Route 53 starts to send the logs to CloudWatch Logs.")

S["route53-faq-resolver-endpoint-enis-in-vpc"] = dict(
    add=[(0, "This IP address can then serve as a forwarding target for on-premises DNS servers to forward queries.")])

S["route53-faq-traffic-flow-what-it-is"] = dict(
    add=[(0, "With Amazon Route 53 Traffic Flow, you can improve the performance and availability of your application for your end users by running multiple endpoints around the world, using Amazon Route 53 Traffic Flow to connect your users to the best endpoint based on latency, geography, and endpoint health.")])

S["route53-faq-traffic-policy-reuse-cname-not-at-apex"] = dict(
    add=[(0, "You can reuse a policy to manage more than one DNS name in one of two ways. First, you can create additional policy records using the policy. Note that there is an additional charge for using this method because you are billed for each policy record that you create."),
         (0, "The second method is to create one policy record using the policy, and then for each additional DNS name that you want to manage using the policy, you create a standard CNAME record pointing at the DNS name of the policy record that you created.")])

S["route53-faq-transfer-no-disruption-copy-zone-first"] = dict(
    add=[(0, "With the DNS record data in hand, you can use Route 53’s Management Console or simple web-services interface to create a hosted zone that can store the DNS records for your domain name and follow its transfer process, which will include such steps as updating the name servers for your domain name to the ones associated with your hosted zone.")])

S["route53-faq-vpc-resolver-on-outposts-local-resolution"] = dict(
    add=[(0, "You can use Route 53 VPC Resolver to resolve Domain Name Server (DNS) queries locally on AWS Outposts racks, improving the availability and performance of your on-premises applications.")])

S["route53-fqdn-trailing-dot-optional"] = dict(
    rep={0: "For record types that include a domain name, enter a fully qualified domain name, for example, *www.example.com*. The trailing dot is optional; Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical."})

S["route53-geolocation-us-unmapped-ips-need-us-record"] = dict(
    add=[(0, "Some IP addresses are associated with the United States, but not with an individual state.")])

S["route53-geoproximity-maps-only-with-traffic-flow"] = dict(
    claim="The geoproximity routing page illustrates routing with maps of AWS Regions and notes that the maps are available only with Traffic Flow.",
    add=[(0, "The following map shows four AWS Regions (numbered 1 through 5):")])

S["route53-hc-calculated-healthy-count-compare"] = dict(
    claim="For a calculated health check, Route 53 adds up the number of child health checks that are considered healthy and compares that number with the number of child health checks that must be healthy for the parent health check to be considered healthy.",
    add=[(0, "Route 53 adds up the number of child health checks that are considered to be healthy.")])

S["route53-hc-cloudwatch-high-resolution-not-supported"] = dict(
    claim="For the CloudWatch alarms that Route 53 health checks can monitor, standard-resolution metrics are supported and high-resolution metrics aren't supported.",
    rep={0: "Route 53 supports CloudWatch alarms with the following features: Standard-resolution metrics. High-resolution metrics aren't supported."})

S["route53-hc-disabled-invert-to-stop-traffic"] = dict(
    claim="After you disable a health check, Route 53 considers its status to always be healthy and, if you configured DNS failover, continues to route traffic to the corresponding resources. To stop routing traffic to a resource, invert the health check.",
    rep={0: "After you disable a health check, Route 53 considers the status of the health check to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources. If you want to stop routing traffic to a resource, invert the health check."})

S["route53-hc-domain-name-not-record-name"] = dict(
    claim="If you check the health of failover, geolocation, geoproximity, latency, multivalue or weighted records and specify the endpoint by domain name, specify the domain name of each server for Domain name, not the name of the records. If the Domain name of a health check matches the name of the records and you associate the health check with those records, health check results will be unpredictable.",
    add=[(0, "If you want to check the health of failover, geolocation, geoproximity, latency, multivalue, or weighted records, and you choose to specify the endpoint by domain name, we recommend that you create a separate health check for each endpoint."),
         (0, "For the value of **Domain name**, specify the domain name of the server (such as us-east-2-www.example.com), not the name of the records (www.example.com).")])

S["route53-hc-failure-threshold-default-3"] = dict(
    claim="If you don't specify a FailureThreshold, the default is three health checks; FailureThreshold is not supported for health checks of type RECOVERY_CONTROL.",
    rep={0: "`FailureThreshold` is not supported when you specify a value for `Type` of `RECOVERY_CONTROL`. Otherwise, if you don't specify a value for `FailureThreshold`, the default value is three health checks."})

S["route53-hc-private-endpoint-cloudwatch-alarm-health-check"] = dict(
    add=[(0, "For example, you might create a CloudWatch metric that checks the status of the EC2 `StatusCheckFailed` metric, add an alarm to the metric, and then create a health check that is based on the data stream for the alarm to check instances within a Virtual Private Cloud (VPC) that only have private IP addresses.")])

S["route53-hc-removed-region-continues-up-to-an-hour"] = dict(
    rep={0: "If you update a health check to remove a Region that has been performing health checks, Route 53 continues to perform checks from that Region for up to an hour. This ensures that some health checkers are always checking the endpoint (for example, if you replace three Regions with four different Regions)."})

S["route53-hc-request-interval-default-30"] = dict(
    claim="If you don't specify a RequestInterval for a health check, the default is 30 seconds. You can't change RequestInterval after you create the health check, and RequestInterval is not supported for health checks of type RECOVERY_CONTROL.",
    qual={"condition": "Cannot be changed after the health check is created; not supported for type RECOVERY_CONTROL"},
    rep={0: "`RequestInterval` is not supported when you specify a value for `Type` of `RECOVERY_CONTROL`. You can't change the value of `RequestInterval` after you create a health check. If you don't specify a value for `RequestInterval`, the default value is `30` seconds."})

S["route53-hc-string-matching-compressed-response"] = dict(
    claim="A Route 53 health checker uncompresses a response before searching for the string only if the web server used a compression algorithm that health checkers support. If the response is compressed using another algorithm, the health checker can't decompress the response before searching, so the search will almost always fail and Route 53 will consider the endpoint unhealthy.",
    rep={0: "If the response is compressed using another algorithm, the health checker can't decompress the response before searching for the string. In this case, the search will almost always fail, and Route 53 will consider the endpoint unhealthy"},
    add=[(0, "If the endpoint is a web server that returns a response that is compressed, the Route 53 health checker will uncompress the response before checking for the specified search string only if the web server compressed the response using a compression algorithm that health checkers support.")])

S["route53-health-check-failure-threshold-counts-consecutive-failures"] = dict(
    add=[(0, "If the endpoint doesn't respond to a request, Route 53 starts to count the number of consecutive requests that the endpoint doesn't respond to:")])

S["route53-hybrid-whitepaper-logging-reason-outdated"] = dict(
    claim="The hybrid DNS whitepaper, which is for historical reference only, gives logging DNS queries as one reason to run your own forwarders. The Route 53 guide history shows that support for Resolver query logs was added on September 1, 2020, and Resolver query logging can log queries that originate in your VPCs, queries from inbound Resolver endpoints and queries that use outbound Resolver endpoints.",
    add=[(WP, "This whitepaper is for historical reference only."),
         (RQL, "You can log the following DNS queries: Queries that originate in Amazon Virtual Private Cloud VPCs that you specify, as well as the responses to those DNS queries. Queries from on-premises resources that use an inbound Resolver endpoint. Queries that use an outbound Resolver endpoint for recursive DNS resolution.")])

S["route53-ip-based-routing-uses-your-ip-to-endpoint-mappings"] = dict(
    claim="With IP-based routing you upload your data to Route 53 as user-IP-to-endpoint mappings, which gives you fine-grained control to boost performance or cut network costs; one common use case is routing end users from certain ISPs to specific endpoints.",
    add=[(0, "You want to route end users from certain ISPs to specific endpoints so you can optimize network transit costs or performance.")])

S["route53-latency-routing-lowest-latency-region"] = dict(
    add=[(0, "Route 53 responds with the value from the chosen record, such as the IP address for a web server.")])

S["route53-migrate-alias-records-last"] = dict(
    claim="When you migrate a hosted zone by editing the exported records file, and the zone contains aliases that refer to other records in the same hosted zone, move the alias records to the bottom of the file, because Route 53 must create the record that an alias record refers to before it can create the alias record. If an alias record refers to another alias record, the alias target must appear first in the file.",
    qual={"condition": "the hosted zone contains aliases that refer to other records in the same hosted zone"},
    add=[(0, "If the hosted zone contains any aliases that refer to other records in the same hosted zone, make the following changes:"),
         (0, "If one or more alias records refer to other alias records, the records that are the alias target must appear in the file before the referencing alias records.")])

S["route53-migrate-dns-in-use-quick-rollback"] = dict(
    claim="Your domain should remain available during the entire DNS migration. In the unlikely event that there are issues, the procedure for a domain that is in use (getting traffic) lets you roll back quickly; with the procedure for an inactive domain, the domain could be unavailable for a couple of days.",
    add=[(0, "If the domain is currently getting traffic—for example, if your users are using the domain name to browse to a website or access a web application—see Making Route 53 the DNS service for a domain that's in use."),
         (0, "If the domain isn't getting any traffic (or is getting very little traffic), see Making Route 53 the DNS service for an inactive domain.")])

S["route53-migrate-in-use-monitor-and-switch-back"] = dict(
    claim="After you change the name servers, monitor traffic for the domain, including website or application traffic and email. If the traffic slows or stops, use the method of the previous DNS service to change the name servers back to the previous name servers, then determine what went wrong. If the traffic is unaffected, change the TTL for the NS record back to a higher value.",
    rep={0: "**If the traffic slows or stops** – Use the method provided by the previous DNS service to change the name servers for the domain back to the previous name servers. These are the name servers that you made note of in step 7 of To update the NS record at the registrar, or the parent zone, to use Route 53 name servers. Then determine what went wrong."},
    add=[(0, "Monitor traffic for the domain, including website or application traffic, and email:"),
         (0, "**If the traffic is unaffected** – Continue to Step 9: Change the TTL for the NS record back to a higher value.")])

S["route53-migrate-lower-ns-ttl-60-to-900-wait-two-days"] = dict(
    claim="When you migrate DNS service for a domain that is in use to Amazon Route 53, the guide recommends setting the NS record TTL to a value between 60 seconds and 900 seconds (15 minutes), then waiting two days after you lowered the TTL so that the migration happens all at one time.")

S["route53-no-record-healthy-all-records-considered-healthy"] = dict(
    rep={0: "If none of the records in a group of records are healthy, Route 53 needs to return something in response to DNS queries, but it has no basis for choosing one record over another. In this circumstance, Route 53 considers all the records in the group to be healthy and selects one based on the routing policy and on the values that you specify for each record."})

S["route53-phz-parent-zone-counts-as-match"] = dict(
    claim="When VPC Resolver evaluates whether a private hosted zone matches the domain name in a request, a match is either an identical match or a zone whose name is a parent of the domain name in the request.",
    rep={0: "VPC Resolver evaluates whether the name of the private hosted zone matches the domain name in the request, such as accounting.example.com. A match is defined as either of the following: An identical match The name of the private hosted zone is a parent of the domain name in the request."})

S["route53-phz-reserved-ns-not-reachable-from-internet"] = dict(
    claim="The name servers of a private hosted zone are reserved and never used by Route 53 public hosted zones. The private hosted zone information is not returned if you directly query the name servers over the internet; instead, VPC Resolver detects queries within a private namespace from the VPC to hosted zone associations and uses direct, private connectivity to reach the private DNS servers.",
    add=[(0, "Instead, the VPC Resolver detects that queries are within a private namespace based on VPC to hosted zone associations and uses direct, private connectivity to reach the private DNS servers.")])

S["route53-phz-unsupported-routing-policies"] = dict(
    rep={0: "You can use the following routing policies when you create records in a private hosted zone: Simple routing Failover routing Multivalue answer routing Weighted routing Latency-based routing Geolocation routing Geoproximity routing Creating records in a private hosted zone using other routing policies is not supported."},
    drop=[1])

S["route53-pricing-alias-free-when-name-type-match-and-target-aws"] = dict(
    claim="DNS queries are free when both of the following are true: the domain name and record type in the query match an alias record, and the alias target is an AWS resource other than another Route 53 record.",
    add=[(0, "DNS queries are free when both of the following are true:")])

S["route53-pricing-dns-firewall-dimensions"] = dict(
    claim="Resolver DNS Firewall charges for DNS queries originating from within VPCs that have firewall rule group associations (and for queries through inbound Resolver endpoints into them) and a fee for each domain name stored in a domain list, with no domain name fee for managed domain lists. Rule groups that contain DNS Firewall Advanced rules add an hourly fee for each rule group, per VPC association in an AWS Region.",
    add=[(0, "When using managed domain lists within your DNS Firewall Foundation rules, you are not charged for the domain names fee above, but you are charged for the DNS queries that are inspected against the rules which use managed domain lists.")])

S["route53-pricing-hosted-zone-includes-10000-records"] = dict(
    claim="A hosted zone includes up to 10,000 records; each record above 10,000 per hosted zone is charged a monthly fee.",
    rep={0: "A hosted zone includes up to 10,000 records. For each record greater than 10,000 per hosted zone, you will be charged $0.0015 per month."})

S["route53-pricing-missing-record-and-type-mismatch-charged"] = dict(
    add=[(0, "We charge the standard rate for the following DNS queries:"),
         (0, "Queries for which the domain name or subdomain name matches a record name, but not the record type.")])

S["route53-pricing-query-types-four-rates"] = dict(
    claim="The Route 53 usage report has four query types: standard queries (records with failover, multivalue answer and weighted routing policies) as Intra-AWS-DNS-Queries, latency-based routing queries as Intra-AWS-LBR-Queries, geo routing queries (geolocation and geoproximity) as Intra-AWS-Geo-Queries, and IP-based routing queries as Intra-AWS-Cidr-Queries.",
    qual={"scope": "query types on the Route 53 usage report"},
    add=[(0, "You can create alias records for all of the query types that appear on your Route 53 usage report, namely:")])

S["route53-public-query-logs-only-queries-reaching-route53"] = dict(
    add=[(0, "If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response without sending the query to Route 53 until the TTL for the corresponding record expires.")])

S["route53-quota-domains-per-account"] = dict(
    claim="For new customers as of March 2021 the default quota is 20 domains per AWS account; an existing account whose default limit is 50 keeps 50. You can request a higher quota.",
    qual={"condition": "20 for new customers as of March 2021; an existing account at 50 stays at 50"},
    values=[{"key": "value", "display": "20 domains per AWS account"}, {"key": "old", "display": "it will remain at 50"}],
    add=[(0, "The limit is 20 for new customers as of March 2021."),
         (0, "If you have an existing account and your default limit is 50 now, it will remain at 50.")])

S["route53-record-set-permissions-iam-conditions"] = dict(
    add=[(0, "This allows you to grant someone permissions to: A single resource record set. All resource record sets of a specific DNS record type. Resource record sets where the names contain a specific string. Perform any, or all of the `CREATE | UPSERT | DELETE `actions when using the ChangeResourceRecordSets API, or the Route 53 console.")])

S["route53-resilience-primarily-global-some-features-regional"] = dict(
    add=[(0, "If you're using Route 53 VPC Resolver to set up hybrid configurations, you create endpoints in AWS Regions that you choose, and you specify IP addresses in multiple Availability Zones."),
         (0, "You can configure Route 53 health checks to check the health of resources that you create in specific Regions, such as Amazon EC2 instances and Elastic Load Balancing load balancers.")])

S["route53-resolver-caches-ns-two-days"] = dict(
    claim="After the TLD name server for .com responds with the names of the four Route 53 name servers for example.com, the DNS resolver caches them, and the next time someone browses to example.com the resolver skips steps 3 and 4 (the root and TLD name servers). The name servers are typically cached for two days.",
    add=[(0, "The DNS resolver for the ISP forwards the request for www.example.com to a DNS root name server."),
         (0, "The DNS resolver forwards the request for www.example.com again, this time to one of the TLD name servers for .com domains. The name server for .com domains responds with the names of the four Route 53 name servers associated with the example.com domain.")])

S["route53-resolver-dot-rule-does-not-forward-everything"] = dict(
    add=[(0, "If you want to forward all queries to your network, you create a rule, specify \".\" (dot) for the domain name, and associate the rule with the VPCs for which you want to forward all DNS queries to your network.")])

S["route53-resolver-link-local-1024-pps-shared"] = dict(
    add=[(0, "Link-Local services include Route 53 VPC Resolver, Amazon Time Service (NTP), Instance Metadata Service (IMDS) and Windows Licensing Service (for Windows instances).")])

S["route53-resolver-outbound-ips-not-public-need-link-or-nat"] = dict(
    add=[(0, "Those IP addresses, which you choose from the range of IP addresses available to your VPC, aren't public IP addresses.")])

S["route53-resolver-over-limit-packets-rejected"] = dict(
    claim="Each network interface allows 1024 packets per second (PPS) destined to Link-Local services, which include Route 53 VPC Resolver; packets exceeding this limit are rejected.",
    rep={0: "These services scale with each elastic network interface you create in your VPC, and each network interface allows 1024 packets per second (PPS) destined to Link-Local services. Packets exceeding this limit are rejected."},
    add=[(0, "Link-Local services include Route 53 VPC Resolver, Amazon Time Service (NTP), Instance Metadata Service (IMDS) and Windows Licensing Service (for Windows instances).")])

S["route53-resolver-query-logs-destinations"] = dict(
    rep={0: "You can send VPC Resolver query logs to the following AWS resources: **Amazon CloudWatch Logs (Amazon CloudWatch Logs) log group** You can analyze logs with Logs Insights and create metrics and alarms.",
         1: "**Amazon S3 (S3) bucket** An S3 bucket is economical for long-term log archiving. Latency is typically higher.",
         2: "**Firehose delivery stream** You can stream logs in real time to Amazon OpenSearch Service, Amazon Redshift, or other applications."})

S["route53-resolver-query-logs-what-is-logged"] = dict(
    claim="Resolver query logging can log queries that originate in the VPCs that you specify (with their responses), queries from on-premises resources that use an inbound Resolver endpoint, queries that use an outbound Resolver endpoint for recursive DNS resolution, and queries that use Resolver DNS Firewall rules to block, allow, or monitor domain lists.",
    add=[(0, "Queries that use Resolver DNS Firewall rules to block, allow, or monitor domain lists.")])

S["route53-s3-alias-record-type-a"] = dict(
    claim="To route traffic to an S3 bucket that is configured as a website, you create a record of type A (IPv4 address), turn on Alias, and choose Alias to S3 website endpoint.",
    rep={0: "**Record type** Choose **A – IPv4 address**. **Alias** Turn on **Alias**. **Route traffic to** Choose **Alias to S3 website endpoint**, then choose the Region that the endpoint is from."})

S["route53-same-name-hosted-zones-allowed"] = dict(
    claim="You can create more than one hosted zone with the same name and add different records to each. Route 53 assigns four name servers to every hosted zone, and by default the name servers differ for each one; with a reusable delegation set, created with the API, you can assign the same four name servers to several hosted zones.",
    add=[(0, "By default, Route 53 assigns a unique set of four name servers (called a delegation set) to each hosted zone that you create."),
         (0, "You can then create hosted zones with the API and assign the same four name servers to each one.")])

S["route53-same-name-zones-never-mix-records"] = dict(
    claim="Route 53 never returns values for records in other hosted zones that have the same name, so when you update your registrar's name server records, use the Route 53 name servers of the hosted zone that has the records you want Route 53 to use.")

S["route53-simple-routing-multiple-values-one-record"] = dict(
    claim="If you choose the simple routing policy in the Route 53 console, you can't create multiple records with the same name and type, but you can specify multiple values in the same record, such as multiple IP addresses.")

S["route53-simple-routing-multiple-values-random-order-no-health-check"] = dict(
    add=[(0, "The client then chooses a value and resends the query.")])

S["route53-split-view-dns-definition"] = dict(
    add=[(0, "In split-view DNS, you use the same domain name (example.com) for internal uses (accounting.example.com) and external uses, such as your public website (www.example.com)."),
         (0, "Associate one or more Amazon VPCs with the private hosted zone.")])

S["route53-subdomain-delegation-steps-new-zone-and-ns-record"] = dict(
    add=[(0, "You create records in the new hosted zone that define how you want to route traffic for the subdomain (acme.example.com) and its subdomains, such as backend.acme.example.com."),
         (0, "You get the name servers that Route 53 assigned to the new hosted zone when you created it.")])

S["route53-vpc-permissions-iam-condition"] = dict(
    add=[(0, "This allows you to grant someone permissions to associate hosted zone with, disassociate hosted zone from, create VPC association authorization for, delete VPC association authorization for, create hosted zone with or list hosted zones for: A single VPC. Any VPCs within the same Region. Multiple VPCs.")])

S["route53-vs-ga-resolvers-cache-dns-answers"] = dict(
    add=[(0, "So when you make a configuration update, or there’s an application failure or change in your routing preference, you don’t know how long it will take before all of your users receive updated IP addresses.")])

S["route53-weighted-zero-weight-health-nonzero-first"] = dict(
    add=[(0, "If you add health checks to all the records in a group of weighted records, but you give nonzero weights to some records and zero weights to others, health checks work the same as when all records have nonzero weights with the following exceptions:")])


def url_for(source_id, f):
    for ev in f["evidence"]:
        if ev["source_id"] == source_id:
            return ev["url"]
    meta = json.load(open(os.path.join(SNAP, source_id + ".meta.json")))
    return meta.get("url") or meta.get("final_url")


def clean(ev):
    out = {"source_id": ev["source_id"], "url": ev["url"], "quote": ev["quote"], "table_header": ev.get("table_header")}
    if ev.get("heading") is not None:
        out["heading"] = ev["heading"]
    return out


written = []
for fid, spec in S.items():
    f = facts[fid]
    patch = {}
    if "claim" in spec:
        patch["claim"] = spec["claim"]
    if "qual" in spec:
        q = copy.deepcopy(f["qualifiers"])
        q.update(spec["qual"])
        patch["qualifiers"] = q
    if "values" in spec:
        patch["values"] = spec["values"]
    if any(k in spec for k in ("rep", "add", "drop", "head")):
        evs = [clean(e) for e in f["evidence"]]
        for i, quote in spec.get("rep", {}).items():
            evs[i]["quote"] = quote
        for i, h in spec.get("head", {}).items():
            evs[i]["heading"] = h
        for item in spec.get("add", []):
            src, quote = item[0], item[1]
            sid = f["evidence"][src]["source_id"] if isinstance(src, int) else src
            ev = {"source_id": sid, "url": url_for(sid, f), "quote": quote, "table_header": None}
            if len(item) > 2:
                ev["heading"] = item[2]
            evs.append(ev)
        for i in sorted(spec.get("drop", []), reverse=True):
            del evs[i]
        patch["evidence"] = evs
    json.dump(patch, open(os.path.join(OUT, fid + ".json"), "w"), ensure_ascii=False, indent=1)
    written.append(fid)

disputed = json.load(open(os.path.join(B, "_build/work/13-route53/finalize.json")))["disputed"]
missing = [d for d in disputed if d not in S]
extra = [s for s in S if s not in disputed]
print("written", len(written), "missing", missing, "extra", extra)
