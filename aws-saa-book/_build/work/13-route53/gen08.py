import json

def ev(sid, quote, url=None, header=None):
    if url is None:
        if sid.startswith("docs/"):
            url = "https://docs.aws.amazon.com/" + sid[5:] + ".html"
        elif sid.startswith("www/"):
            url = "https://aws.amazon.com/" + sid[4:] + "/"
    return {"source_id": sid, "url": url, "quote": quote, "table_header": header}

R = "docs/Route53/latest/DeveloperGuide/"
PR = "www/route53/pricing"

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
PD = "pricing-dimension"
B = ["4.4.K7"]

facts.append(fact("route53-pricing-hosted-zone-monthly-not-prorated", PD,
 "Each Amazon Route 53 hosted zone is billed per month, at a lower price for hosted zones beyond the first 25; the monthly price is not prorated for partial months, and the zone is charged when it is created and on the first day of each later month.",
 "How is a Route 53 hosted zone billed, and is the monthly price prorated?",
 [("notprorated", "not prorated for partial months"), ("tiers", "for the first 25 hosted zones")], "per hosted zone per month",
 [ev(PR, "$0.50 per hosted zone per month for the first 25 hosted zones"),
  ev(PR, "$0.10 per hosted zone per month for additional hosted zones"),
  ev(PR, "The monthly hosted zone prices listed above are not prorated for partial months. A hosted zone is charged at the time it is created and on the first day of each subsequent month.")],
 tier0=True, rel="core", bullets=B, note="d13-099. Dimension only; the dollar amounts are in the quotes, not in the claim."))

facts.append(fact("route53-pricing-hosted-zone-deleted-in-12-hours-free", PD,
 "To allow testing, a hosted zone deleted within 12 hours of creation is not charged for the zone, but queries on its public hosted zone are still charged.",
 "Is a hosted zone deleted right after creation charged?",
 [("window", "deleted within 12 hours of creation")], "per hosted zone",
 [ev(PR, "To allow testing, a hosted zone that is deleted within 12 hours of creation is not charged, however, any queries on public hosted zones will still incur charges at the rates below.")],
 rel="extended", bullets=B, note="d13-099."))

facts.append(fact("route53-pricing-private-zone-queries-no-charge", PD,
 "Queries on private hosted zones are provided at no additional cost to Amazon Route 53 customers.",
 "Does Route 53 charge for DNS queries on a private hosted zone?",
 [("free", "Queries on private hosted zones are provided at no additional cost")], "DNS queries on private hosted zones",
 [ev(PR, "Queries on private hosted zones are provided at no additional cost to Route 53 customers.")],
 tier0=True, rel="core", bullets=B, note="d13-099."))

facts.append(fact("route53-pricing-hosted-zone-includes-10000-records", PD,
 "A hosted zone includes up to 10,000 records; each record beyond 10,000 per hosted zone is charged per month.",
 "How many records does a hosted zone price include?",
 [("included", "up to 10,000 records")], "per hosted zone",
 [ev(PR, "A hosted zone includes up to 10,000 records. For each record greater than 10,000 per hosted zone, you will be charged $0.0015 per month.")],
 rel="extended", bullets=B, dom="default", note="d13-099. Compare with the quotas page for the records limit per zone (numbers lens)."))

facts.append(fact("route53-pricing-query-types-four-rates", PD,
 "Amazon Route 53 bills public DNS queries by query type: standard queries (failover, multivalue answer and weighted records), latency-based routing queries, geo routing queries (geolocation and geoproximity) and IP-based routing queries.",
 "Which query types does Route 53 bill separately?",
 [("standard", "Intra-AWS-DNS-Queries"), ("latency", "Intra-AWS-LBR-Queries"), ("geo", "Intra-AWS-Geo-Queries"), ("ip", "Intra-AWS-Cidr-Queries")], "per million queries by query type",
 [ev(PR, "Standard queries (records with failover, multivalue answer, and weighted routing policies), listed as “Intra-AWS-DNS-Queries” on the Route 53 usage report"),
  ev(PR, "Latency-based routing queries (records with latency routing policies), listed as “Intra-AWS-LBR-Queries” on the Route 53 usage report"),
  ev(PR, "Geo routing queries (records with geolocation and geoproximity routing policies), listed as “Intra-AWS-Geo-Queries” on the Route 53 usage report"),
  ev(PR, "IP-based routing queries (records with IP-based routing policies), listed as “Intra-AWS-Cidr-Queries” on the Route 53 usage report")],
 tier0=True, rel="core", bullets=B, note="d13-099. Cost angle: routing policies other than standard bill at a higher per-query rate (see the rates table; amounts not recorded here)."))

facts.append(fact("route53-pricing-alias-free-for-listed-aws-services", PD,
 "Alias A and AAAA records mapped to Elastic Load Balancers, CloudFront distributions, Elastic Beanstalk environments, API Gateways, VPC endpoints, S3 website buckets, App Runner, AppSync, OpenSearch, Lightsail and Global Accelerator do not incur a query charge.",
 "Which alias targets make Route 53 queries free?",
 [("list", "do not incur a charge")], "Amazon Route 53 alias A/AAAA queries",
 [ev(PR, "Alias A/AAAA records that are mapped to the following AWS services do not incur a charge: Elastic Load Balancers, Amazon CloudFront distributions, AWS Elastic Beanstalk environments, Amazon API Gateways, Amazon VPC endpoints, Amazon S3 buckets that are configured as website endpoints, Amazon AppRunner, Amazon AppSync, Amazon OpenSearch, Amazon LightSail, and Amazon Global Accelerator.")],
 tier0=True, rel="core", bullets=B, vol="frequently-changing", note="d13-013. The list grows over time (History: OpenSearch 2025-01-14, VPC Lattice 2025-06-25 are not on this pricing list)."))

facts.append(fact("route53-pricing-alias-free-when-name-type-match-and-target-aws", PD,
 "DNS queries are free only when the domain name and record type in the query match an alias record and the alias target is an AWS resource other than another Route 53 record.",
 "When are alias queries free in Route 53?",
 [("cond1", "match an alias record"), ("cond2", "an AWS resource other than another Route 53 record")], "Amazon Route 53 alias queries",
 [ev(PR, "The domain or subdomain name (example.com or acme.example.com) and the record type (A) in the query match an alias record."),
  ev(PR, "The alias target is an AWS resource other than another Route 53 record.")],
 tier0=True, rel="core", bullets=B, note="d13-013."))

facts.append(fact("route53-pricing-alias-to-record-in-zone-standard-rate", PD,
 "Amazon Route 53 charges the standard rate for a query that matches an alias record whose target is a non-alias record in the same hosted zone, but a chain of alias records that ends at an AWS resource such as an Elastic Load Balancer is free.",
 "Is an alias to another record in the same hosted zone free?",
 [("charged", "We charge the standard rate"), ("chain", "a chain of alias records")], "Amazon Route 53 alias queries",
 [ev(PR, "We charge the standard rate for DNS queries for which the domain name and type match a record, but the alias target of the record is a non-alias record in the same hosted zone."),
  ev(PR, "We do not charge for DNS queries if you create a chain of alias records that reference other alias records, and the last alias record in the chain references an AWS resource such as an Elastic Load Balancer.")],
 rel="extended", bullets=B, note="d13-013."))

facts.append(fact("route53-pricing-missing-record-and-type-mismatch-charged", PD,
 "Amazon Route 53 charges the standard rate for queries for a record that does not exist and for queries whose name matches a record but whose type does not, so creating both A and AAAA records is recommended where applicable.",
 "Are queries for a missing record or the wrong record type charged?",
 [("missing", "Queries for a record that doesn't exist"), ("both", "create both A and AAAA records")], "Amazon Route 53 DNS queries",
 [ev(PR, "Queries for a record that doesn't exist (w.example.com)."),
  ev(PR, "Some browsers automatically send both A and AAAA queries for a specified domain or subdomain name, so we recommend that you create both A and AAAA records where applicable.")],
 rel="extended", bullets=B, note="d13-013."))

facts.append(fact("route53-pricing-health-check-aws-vs-non-aws-endpoints", PD,
 "Route 53 health checks are priced per health check per month, separately for AWS endpoints and non-AWS endpoints, and calculated and metric based health checks are billed as health checks of an AWS endpoint.",
 "On what dimensions are Route 53 health checks priced?",
 [("aws", "AWS Endpoints"), ("nonaws", "Non-AWS Endpoints")], "per health check per month",
 [ev(PR, "| Basic health checks (including calculated health checks and metric based health checks) | $0.50 per health check per month | $0.75 per health check per month |", header="|  | AWS Endpoints | Non-AWS Endpoints |"),
  ev(PR, "Calculated health checks and metric based health checks are billed as health checks of an AWS endpoint.")],
 tier0=True, rel="core", bullets=["2.2.K6", "4.4.K7"], note="d13-061. Dimension only; amounts stay in the quote."))

facts.append(fact("route53-pricing-health-check-optional-features", PD,
 "Optional health check features, which include HTTPS, string matching, fast request interval and latency measurement, add a charge per optional feature per month, with separate rates for AWS endpoints and non-AWS endpoints.",
 "Which health check options add a charge?",
 [("features", "HTTPS, string matching; fast request interval, and latency measurement")], "per optional health check feature per month",
 [ev(PR, "| Optional health check features (including HTTPS, string matching; fast request interval, and latency measurement) | $1.00 per optional health check feature per month | $2.00 per optional health check feature per month |", header="|  | AWS Endpoints | Non-AWS Endpoints |")],
 tier0=True, rel="core", bullets=["2.2.K6", "4.4.K7"], note="d13-061."))

facts.append(fact("route53-pricing-health-checks-first-50-aws-endpoints-free", PD,
 "New and existing customers can create up to 50 health checks for AWS endpoints within or linked to the same AWS account at no charge, and health checks of Elastic Load Balancing resources and S3 website bucket endpoints are not billed.",
 "Which health checks are free?",
 [("free", "up to 50 health checks for AWS endpoints"), ("elb", "You are not billed for health checks of Elastic Load Balancing resources")], "per AWS account",
 [ev(PR, "New and existing customers can create up to 50 health checks for AWS endpoints that are within or linked to the same AWS account for free."),
  ev(PR, "You are not billed for health checks of Elastic Load Balancing resources or Amazon S3 buckets that are configured as website endpoints.")],
 tier0=True, rel="core", bullets=["2.2.K6", "4.4.K7"], dom="max", note="d13-061."))

facts.append(fact("route53-pricing-traffic-flow-per-policy-record", PD,
 "Traffic Flow is billed by policy record, which is a traffic policy associated with a domain name; the monthly price is prorated for partial months and a traffic policy that is not associated with a domain name through a policy record is not charged.",
 "What is the Traffic Flow pricing dimension?",
 [("unit", "You create a policy record")], "per Traffic Flow policy record per month",
 [ev(PR, "You create a policy record when you associate a Route 53 Traffic Flow policy with a specific domain name (such as www.example.com) so that the traffic policy manages traffic for this domain name."),
  ev(PR, "The monthly price listed above is prorated for partial months."),
  ev(PR, "There is no charge for traffic policies that are not associated with a domain name via a policy record.")],
 rel="extended", bullets=B, note="d13-099."))

facts.append(fact("route53-pricing-authoritative-query-logs-cloudwatch", PD,
 "Amazon Route 53 does not charge for authoritative DNS query logs, but when you configure DNS query logging you incur Amazon CloudWatch charges in the US East (Virginia) Region for ingestion, archival storage and analysis.",
 "Who charges for Route 53 public DNS query logs?",
 [("route53", "Route 53 does not charge for authoritative DNS query logs"), ("cw", "Amazon CloudWatch charges in the US East (Virginia) Region")], "Amazon Route 53 public DNS query logging",
 [ev(PR, "Route 53 does not charge for authoritative DNS query logs. However, when you configure DNS query logging, you incur Amazon CloudWatch charges in the US East (Virginia) Region including data ingestion, archival storage, and analysis.")],
 rel="extended", bullets=B, note="d13-099."))

facts.append(fact("route53-pricing-resolver-endpoint-eni-hour", PD,
 "A Route 53 Resolver endpoint needs two or more IP addresses, each corresponding to one elastic network interface (ENI), and endpoints are billed per ENI per hour, and a single outbound endpoint can be used by multiple VPCs from multiple accounts in the same Region; only queries that pass through an inbound or outbound endpoint are charged.",
 "What are the Resolver endpoint pricing dimensions?",
 [("ips", "requires two or more IP addresses"), ("queries", "Only queries that pass through a Route 53 Resolver endpoint")], "per Resolver endpoint ENI per hour and per million endpoint queries",
 [ev(PR, "A Route 53 Resolver endpoint requires two or more IP addresses. Each IP address corresponds with one Elastic Network Interface (ENI)."),
  ev(PR, "A single outbound endpoint can be used by multiple VPCs that were created by multiple accounts within the same region. $0.125 per ENI per hour"),
  ev(PR, "Only queries that pass through a Route 53 Resolver endpoint (either inbound or outbound) will be charged. Queries that resolve locally using the Route 53 Resolver will not be charged.")],
 tier0=True, rel="core", bullets=["3.4.S1", "4.4.K7"], note="d13-099. Dimension only."))

facts.append(fact("route53-pricing-resolver-query-logs-destination-charges", PD,
 "Route 53 does not charge for VPC Resolver query logs, but the CloudWatch, S3 or Firehose charges of the chosen log destination apply.",
 "Who charges for Resolver query logs?",
 [("route53", "Route 53 does not charge for VPC Resolver query logs")], "VPC Resolver query logging",
 [ev(PR, "Route 53 does not charge for VPC Resolver query logs. However, when DNS query logging is configured, Amazon CloudWatch, Amazon S3 or Amazon Kinesis Data Firehose charges will be incurred depending upon the target destination chosen for your logs.")],
 rel="extended", bullets=B, note="d13-099. The pricing page still uses the former name Amazon Kinesis Data Firehose (now Amazon Data Firehose)."))

facts.append(fact("route53-pricing-dns-firewall-dimensions", PD,
 "DNS Firewall Foundational is billed for DNS queries from VPCs with rule group associations and for each domain name stored in a domain list (managed domain lists carry no domain name fee), while DNS Firewall Advanced is billed per hour for each rule group with Advanced rules, per VPC association in an AWS Region.",
 "What are the DNS Firewall pricing dimensions?",
 [("queries", "We charge for DNS queries originating from within VPCs"), ("domains", "each domain name stored in a domain list within a rule group"), ("advanced", "hourly fee for each DNS Firewall rule group")], "Resolver DNS Firewall",
 [ev(PR, "We charge for DNS queries originating from within VPCs that have firewall rule group associations and DNS queries traversing inbound Resolver endpoints from on-premises networks into VPCs that have firewall rule group associations."),
  ev(PR, "We charge a fee for each domain name stored in a domain list within a rule group. No fees are charged for domain names within managed domain lists."),
  ev(PR, "We charge an hourly fee for each DNS Firewall rule group which contains one or more DNS Firewall Advanced rules, per VPC association in an AWS Region.")],
 rel="extended", bullets=["4.4.K7"], note="d13-099. Dimension only."))

facts.append(fact("route53-pricing-profiles-per-account-hour-and-associations", PD,
 "Route 53 Profiles are billed at an hourly rate per AWS account that covers the first 100 Profile-VPC associations in an AWS Region, with a per-association hourly charge beyond those 100.",
 "What is the Route 53 Profiles pricing dimension?",
 [("base", "up to 100 Profile-VPC associations")], "per AWS account per Region per hour",
 [ev(PR, "For Route 53 Profiles, the hourly rate is $0.75 per AWS account for up to 100 Profile-VPC associations pertaining to the Profiles created by an account in an AWS Region."),
  ev(PR, "Beyond the initial 100 associations, there is a charge of $0.0014 per Profile-VPC association per hour per AWS Region.")],
 rel="extended", bullets=["3.4.S1", "4.4.K7"], note="d13-099. Dimension only."))

facts.append(fact("route53-pricing-domains-annual-by-tld", PD,
 "Domain name prices vary by top-level domain (TLD), domain names are registered in annual increments, and the default limit is 20 domain name registrations per account.",
 "How is domain registration priced and what is the default account limit?",
 [("tld", "Pricing for domain names varies by TLD"), ("limit", "default limit of 20 domain name registrations per account")], "per domain per year",
 [ev(PR, "Pricing for domain names varies by TLD. Domain names are registered in annual increments."),
  ev(PR, "There is a default limit of 20 domain name registrations per account. To request a higher limit, please contact us.")],
 rel="extended", bullets=B, dom="default", adj=True, note="d13-099."))

facts.append(fact("route53-pricing-dnssec-no-fee-but-kms", PD,
 "Amazon Route 53 does not charge to enable DNSSEC signing on public hosted zones or DNSSEC validation for Route 53 Resolver, but DNSSEC signing incurs AWS Key Management Service (KMS) charges for storing the private key and using it to sign your zones.",
 "What does DNSSEC signing cost in Route 53?",
 [("kms", "you incur AWS Key Management Service (KMS) charges")], "DNSSEC signing for public hosted zones",
 [ev(PR, "Route 53 does not charge you to enable DNSSEC signing on your public hosted zones or to enable DNSSEC validation for Route 53 Resolver. However, when you enable DNSSEC signing on your public hosted zones, you incur AWS Key Management Service (KMS) charges for storing the private key and using the instances of the key to sign your zones.")],
 tier0=True, rel="core", bullets=["4.4.K7"], note="d13-099."))

facts.append(fact("route53-pricing-console-s3-list-calls", PD,
 "Using the Route 53 console can send API calls to S3, for example to identify alias record targets, and depending on how often you do this the S3 LIST requests may appear in your S3 bill.",
 "Can using the Route 53 console add charges to the S3 bill?",
 [("s3", "may cause charges to appear in your S3 bill as LIST requests")], "Amazon Route 53 console and Amazon S3 API calls",
 [ev(PR, "Using the Route 53 console can generate API calls to S3. Actions such as identifying alias record targets send API calls to S3, such as LIST_ALL_MY_BUCKETS. Depending on how many times you initiate this workflow, the API calls made to S3 may cause charges to appear in your S3 bill as LIST requests.")],
 rel="reference", bullets=B, note="d13-099."))

facts.append(fact("route53-pricing-pay-per-zone-and-query-no-minimums", PD,
 "There are no contracts or minimum commitments for Amazon Route 53; you pay only for the hosted zones that you configure and the number of DNS queries that Route 53 answers.",
 "What do you pay for with Route 53 DNS?",
 [("pay", "You pay only for the hosted zones that you configure")], "Amazon Route 53 DNS",
 [ev(R + "Route53Pricing", "As with other AWS products, there are no contracts or minimum commitments for using Amazon Route 53. You pay only for the hosted zones that you configure and the number of DNS queries that Route 53 answers.")],
 tier0=True, rel="core", bullets=B, note="d13-099."))

facts.append(fact("route53-best-practice-alias-cheaper-faster-than-cname", "behavior",
 "DNS resolvers must make more queries to answer CNAME records, which increases latency and cost, so where possible a Route 53 alias record is a faster and cheaper alternative that gives a direct answer for AWS resources and for other domains in the same hosted zone.",
 "Why does AWS prefer an alias record to a CNAME record where possible?",
 [("cost", "increases latency and costs"), ("alias", "a faster and cheaper alternative is to use a Route 53 alias record")], "Amazon Route 53 alias and CNAME records",
 [ev(R + "best-practices-dns", "However, DNS resolvers must make more queries to answer CNAMEs, which increases latency and costs. Where possible, a faster and cheaper alternative is to use a Route 53 alias record. Alias records allow Route 53 to respond with a direct answer for AWS resources (for example, a load balancer) and for other domains within the same hosted zone.")],
 tier0=True, rel="core", bullets=B, note="d13-013, d13-017, d13-101."))

facts.append(fact("route53-best-practice-multivalue-keeps-reply-under-512-bytes", "behavior",
 "If DNS responses are larger than 512 bytes many resolvers must retry over TCP instead of UDP, which can reduce reliability; AWS recommends multivalue answer routing, which chooses eight healthy random IP addresses to keep responses within the 512 byte boundary.",
 "Why does AWS recommend multivalue answer routing for large answer sets?",
 [("size", "larger than 512 bytes"), ("mv", "chooses eight healthy random IP addresses")], "Amazon Route 53 DNS response size",
 [ev(R + "best-practices-dns", "Avoid creating large single responses. If responses are larger than 512 bytes, many DNS resolvers must retry over TCP instead of UDP, which can reduce reliability and lead to slower responses. We recommend using multivalue answer routing, which chooses eight healthy random IP addresses to keep responses within the 512 byte boundary.")],
 rel="extended", bullets=["2.2.S2"], note="Decision between multivalue and a long simple record."))

# ---- case studies ----
facts.append(fact("route53-case-intraway-multi-region-availability", "case-study",
 "Intraway says that by running on AWS in more than one Region it could multiply the availability of its existing resources instead of dividing them; its case study lists Amazon Route 53 among the AWS services it uses.",
 "How did Intraway gain availability by using more than one AWS Region?",
 [("multi", "multiply the availability of its existing resources instead of dividing them")], "Intraway (case study)",
 [ev("www/solutions/case-studies/intraway", "By activating on AWS in more than one region, Intraway could multiply the availability of its existing resources instead of dividing them.", "https://aws.amazon.com/solutions/case-studies/intraway/"),
  ev("www/solutions/case-studies/intraway", "Intraway also uses several AWS services, including Amazon Relational Database Service (Amazon RDS), Amazon Elastic Compute Cloud (Amazon EC2), Amazon Elastic Container Registry (ECR), and Amazon Route 53.", "https://aws.amazon.com/solutions/case-studies/intraway/")],
 hard=False, rel="extended", bullets=["2.2.S2"], tier=4, note="d13-105. The second quote is longer than 25 words because the sentence cannot be cut; use only the first quote in the book."))

facts.append(fact("route53-case-sony-ps5-launch-without-downtime", "case-study",
 "Sony Interactive Entertainment delivered the PlayStation 5 launch without downtime to millions of players around the world, and its case study names Amazon Route 53 among the AWS services used.",
 "Which company used Route 53 among other services to launch PS5 without downtime?",
 [("launch", "delivered PS5 without downtime to millions of players around the world")], "Sony Interactive Entertainment (case study)",
 [ev("www/solutions/case-studies/sony-interactive-entertainment-reinvent21-case-study", "Learn how Sony Interactive Entertainment (SIE) delivered PS5 without downtime to millions of players around the world.", "https://aws.amazon.com/solutions/case-studies/sony-interactive-entertainment-reinvent21-case-study/"),
  ev("www/solutions/case-studies/sony-interactive-entertainment-reinvent21-case-study", "Learn how SIE delivered PS5 without downtime to millions of players around the world using a coordinated-operations planned response program and a robust, scalable, and secure infrastructure using AWS services, including Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Compute Cloud (Amazon EC2), Amazon Route 53, and Amazon CloudWatch.", "https://aws.amazon.com/solutions/case-studies/sony-interactive-entertainment-reinvent21-case-study/")],
 hard=False, rel="extended", bullets=["2.2.S2"], tier=4, note="d13-105. The second quote is longer than 25 words because the sentence cannot be cut; use only the first quote in the book."))

if __name__ == "__main__":
    json.dump(facts, open("aws-saa-book/_build/work/13-route53/facts-dc-08.json", "w"), indent=0, ensure_ascii=False)
    print(len(facts))
