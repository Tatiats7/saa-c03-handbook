from mklib import *

L = "privatelink"
E = "vpc-endpoints"
SY = "docs/vpc/latest/privatelink/privatelink-share-your-services"
XR = "docs/vpc/latest/privatelink/aws-services-cross-region-privatelink-support"
WN_XR = "www/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services"
AR = "docs/vpc/latest/privatelink/privatelink-access-resources"
SN = "docs/vpc/latest/privatelink/privatelink-access-service-networks"
CR = "docs/vpc/latest/privatelink/privatelink-access-cidr-ranges"
WN_TUN = "www/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint"
DDB = "docs/vpc/latest/privatelink/vpc-endpoints-ddb"
CON = "docs/vpc/latest/privatelink/concepts"
WN_S3V6 = "www/about-aws/whats-new/2025/11/ipv6-amazon-s3-gateway-interface-vpc-endpoints"
f = []

XRS = ["docs/vpc/latest/privatelink/doc-history#11", "whats-new-v2#p166216340"]
XRA = ["whats-new-v2#launch-dmzg1pipv63agssprc4cqm-1"]
RES = ["docs/vpc/latest/privatelink/doc-history#10", "whats-new-v2#launchmarketingintake-1355"]
TUN = ["whats-new-v2#launch-8wzmmucrmrqah5dvavnmsn"]
NOT_EXAM = "NOT EXAMINABLE YET: tunnel endpoints were announced Sep 18, 2026, after 2026-07-15. Label as not examinable yet."

# ---- cross-Region for AWS services (2025-11-19)
f.append(F("privatelink-change-cross-region-aws-services-2025", L, "change",
    "On November 19, 2025 AWS PrivateLink added native cross-Region connectivity to AWS services: until then, interface VPC endpoints only supported connectivity to AWS services in the same Region, and now you can connect to select AWS services hosted in other Regions of the same AWS partition over interface endpoints.",
    "Can an interface endpoint reach an AWS service in another Region?",
    [("date", "November 19, 2025", "November 2025"), ("was", "connectivity to AWS services in the same Region", "before, same Region only")],
    [ev(WN_XR, "Until now, Interface VPC endpoints only supported connectivity to AWS services in the same Region. This launch enables customers to connect to select AWS services hosted in other Regions of the same AWS partition over Interface endpoints.")],
    changed={"date": "2025-11-19", "was": "Interface VPC endpoints only supported connectivity to AWS services in the same Region", "was_evidence": 0},
    vol="changed-since-2022", items=XRA, rel="core", bullets=("1.2.K2",), tier0=True,
    note="Older exam questions assume interface endpoints to AWS services are same-Region only. The number of supported Regions is not stated on the saved pages."))

f.append(F("privatelink-cross-region-aws-services-named-examples", L, "capability",
    "You can create an interface endpoint to reach the listed AWS services in another AWS Region privately, as if they were running in your own VPC; the announcement names Amazon S3, Route53 and Elastic Container Registry (ECR) among them.",
    "Which AWS services can an interface endpoint reach across Regions?",
    [("s3", "access Amazon S3, Route53, Elastic Container Registry (ECR)", None)],
    [ev(XR, "The following AWS services integrate with cross Region AWS PrivateLink. You can create an interface endpoint to connect to these services in another AWS Region, privately, as if they were running in your own VPC."),
     ev(WN_XR, "As a service consumer, you can access Amazon S3, Route53, Elastic Container Registry (ECR) and other services, privately without the need to setup cross-region peering or exposing your data over the public internet.")],
    scope="interface endpoints to cross-Region enabled AWS services", rel="extended", bullets=("1.2.K2",), vol="frequently-changing", items=XRA,
    note="The guide page lists Amazon S3, IAM, Amazon ECR, AWS KMS, Amazon ECS, AWS Lambda, Amazon Data Firehose, Amazon Managed Service for Apache Flink and Amazon Route 53."))

f.append(F("privatelink-cross-region-aws-services-regional-dns-only", L, "restriction",
    "You must use regional DNS when you access AWS services in another Region through an interface endpoint; zonal DNS is not supported.",
    "Which DNS names work for a cross-Region interface endpoint to an AWS service?",
    [("rule", "Zonal DNS is not supported", None)],
    [ev(XR, "You must use regional DNS. Zonal DNS is not supported when accessing AWS services in another Region.")],
    scope="interface endpoints to AWS services in another Region", rel="extended", bullets=("1.2.K2",), vol="frequently-changing", items=XRA))

f.append(F("privatelink-cross-region-aws-services-iam-default-deny", L, "default",
    "By default IAM entities do not have permission to access an AWS service in another Region through PrivateLink; an IAM administrator grants it with a policy that allows the vpce:AllowMultiRegion permission-only action.",
    "What permission does cross-Region access to an AWS service over PrivateLink need?",
    [("action", "vpce:AllowMultiRegion", None)],
    [ev(XR, "By default, IAM entities don't have permission to access an AWS service in another Region. To grant the permissions required for cross Region access, an IAM administrator can create IAM policies that allow the `vpce:AllowMultiRegion` permission-only action.")],
    scope="IAM entities, cross-Region access to AWS services", dom="default", adj=False, rel="reference", bullets=("1.2.K2",), vol="frequently-changing", items=XRA))

# ---- cross-Region for endpoint services (2024-11-26)
f.append(F("privatelink-cross-region-endpoint-service-concept", L, "capability",
    "A service provider can host a service in one Region and make it available in a set of supported Regions, and a service consumer selects a service Region when creating an endpoint.",
    "Can a PrivateLink endpoint service be used from another Region?",
    [("rule", "available in a set of supported Regions", None)],
    [ev(SY, "A service provider can host a service in one Region and make it available in a set of supported Regions. A service consumer selects a service Region when creating an endpoint.")],
    scope="PrivateLink endpoint services", rel="core", bullets=("3.4.K4",), tier0=True, vol="frequently-changing", items=XRS))

f.append(F("privatelink-cross-region-endpoint-service-failover-within-region-only", L, "restriction",
    "With cross-Region access, AWS PrivateLink manages failover between Availability Zones but does not manage failover across Regions.",
    "Does PrivateLink fail over between Regions for cross-Region access?",
    [("rule", "It does not manage failover across Regions", None)],
    [ev(SY, "With cross-Region access, AWS PrivateLink manages failover between Availability Zones. It does not manage failover across Regions.")],
    scope="cross-Region access to a PrivateLink endpoint service", rel="extended", bullets=("3.4.K4",), vol="frequently-changing", items=XRS))

f.append(F("privatelink-cross-region-endpoint-service-unsupported-azs", L, "restriction",
    "Cross-Region access to a PrivateLink endpoint service is not supported for the Availability Zones use1-az3, usw1-az2, apne1-az3, apne2-az2 and apne2-az4.",
    "Which Availability Zones do not support PrivateLink cross-Region access?",
    [("azs", "use1-az3", None)],
    [ev(SY, "Cross-Region access is not supported for the following Availability Zones: `use1-az3`, `usw1-az2`, `apne1-az3`, `apne2-az2`, and `apne2-az4`.")],
    scope="cross-Region access to a PrivateLink endpoint service", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=XRS))

f.append(F("privatelink-cross-region-endpoint-service-only-privatelink-services", L, "restriction",
    "Cross-Region access is only supported for services that you share through AWS PrivateLink.",
    "What kinds of services can be shared across Regions with PrivateLink?",
    [("rule", "services that you share through AWS PrivateLink", None)],
    [ev(SY, "Cross-Region access is only supported for services that you share through AWS PrivateLink.")],
    scope="cross-Region access", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=XRS))

f.append(F("privatelink-cross-region-endpoint-service-iam-default-deny", L, "default",
    "By default IAM entities do not have permission to make an endpoint service available in multiple Regions or to access an endpoint service across Regions.",
    "Is cross-Region access to an endpoint service allowed by default?",
    [("rule", "don't have permission to make an endpoint service", None)],
    [ev(SY, "By default, IAM entities don't have permission to make an endpoint service available in multiple Regions or access an endpoint service across Regions.")],
    scope="IAM entities, cross-Region endpoint services", dom="default", adj=False, rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=XRS))

# ---- resource endpoints (2024-12-01)
f.append(F("privatelink-resource-endpoint-no-load-balancer-needed", L, "capability",
    "Since December 1, 2024 a resource endpoint lets you privately access a VPC resource such as a database in another VPC without a load balancer; without resource endpoints you had to add an internet gateway or use an interface endpoint with a Network Load Balancer.",
    "How can you privately reach a database in another VPC without a Network Load Balancer?",
    [("date", "December 1, 2024", "December 2024"), ("what", "privately and securely access VPC resources", None)],
    [ev(AR, "Without resource endpoints, you have to either add an internet gateway to your VPC or access the resource using a AWS PrivateLink interface endpoint and a Network Load Balancer."),
     ev(AR, "A resource endpoint lets you privately and securely access VPC resources such as a database, an Amazon EC2 instance, an application endpoint, a domain-name target, or an IP address that may be in a private subnet in another VPC or in an on premise environment.")],
    changed={"date": "2024-12-01", "was": "access the resource using a AWS PrivateLink interface endpoint and a Network Load Balancer", "was_evidence": 0},
    vol="changed-since-2022", items=RES, rel="core", bullets=("3.4.K4",), tier0=True,
    note="Date from the PrivateLink document history row 'Access resources and service networks' (December 1, 2024)."))

f.append(F("privatelink-resource-endpoint-tcp-only", L, "restriction",
    "A resource endpoint supports TCP traffic and does not support UDP traffic.",
    "Which protocols does a PrivateLink resource endpoint support?",
    [("rule", "UDP traffic is not supported", None)],
    [ev(AR, "TCP traffic is supported. UDP traffic is not supported.")],
    scope="resource endpoints", rel="extended", bullets=("3.4.K4",), vol="frequently-changing", items=RES))

f.append(F("privatelink-resource-endpoint-connections-start-from-endpoint-vpc", L, "restriction",
    "Network connections must be initiated from the VPC that contains the resource endpoint, not from the VPC that has the resource; the resource's VPC cannot initiate connections into the endpoint VPC.",
    "Which side can start connections through a resource endpoint?",
    [("rule", "from the VPC that contains the resource endpoint", None)],
    [ev(AR, "Network connections must be initiated from the VPC that contains the resource endpoint, and not from the VPC that has the resource. The resource's VPC can't initiate network connections into the endpoint VPC.")],
    scope="resource endpoints", rel="extended", bullets=("3.4.K4",), vol="frequently-changing", items=RES))

f.append(F("privatelink-resource-endpoint-only-rds-arn-resources", L, "restriction",
    "The only supported ARN-based resources for a resource endpoint are Amazon RDS resources.",
    "Which ARN-based resources can a resource endpoint reach?",
    [("rule", "only supported ARN-based resources are Amazon RDS resources", None)],
    [ev(AR, "The only supported ARN-based resources are Amazon RDS resources.")],
    scope="resource endpoints", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=RES))

f.append(F("privatelink-resource-endpoint-billing-hourly-and-per-gb", L, "pricing-dimension",
    "With resource endpoints you are billed for each hour that the resource VPC endpoint is provisioned and per GB of data processed when you access resources; the resource owner is billed per GB processed by its resource gateways.",
    "How are resource endpoints and resource gateways billed?",
    [("hourly", "resource VPC endpoint is provisioned", None)],
    [ev(AR, "When you access resources using resource endpoints, you are billed for each hour that your resource VPC endpoint is provisioned. You are also billed per GB of data processed when you access resources."),
     ev(AR, "When you enable access to your resources using resource configurations and resource gateways, you are billed per GB data processed by your resource gateways.")],
    scope="resource endpoints and resource gateways", rel="extended", bullets=("4.4.S3",), vol="frequently-changing", items=RES))

f.append(F("privatelink-service-network-endpoint-billing", L, "pricing-dimension",
    "You are billed hourly for the resource configurations associated with your service network and per GB of data processed through the service network VPC endpoint; you are not billed hourly for the service-network VPC endpoint itself.",
    "Is a service network VPC endpoint billed per hour?",
    [("rule", "not billed hourly for the service-network VPC endpoint", None)],
    [ev(SN, "You are billed hourly for the resource configurations that are associated with your service network. You are also billed per GB of data processed when you access resources through the service network VPC endpoint. You are not billed hourly for the service-network VPC endpoint itself.")],
    scope="service-network endpoints", rel="reference", bullets=("4.4.S3",), vol="frequently-changing", items=RES))

# ---- tunnel endpoints: NOT EXAMINABLE YET
f.append(F("privatelink-change-tunnel-endpoints-2026", L, "change",
    "On September 18, 2026 AWS PrivateLink announced tunnel endpoints, a new type of VPC endpoint for network segments; before it, customers who wanted to share resources with another party had to do it one at a time by creating a Resource Configuration for every resource.",
    "What do PrivateLink tunnel endpoints add?",
    [("date", "September 18, 2026", "September 2026"), ("what", "a new type of VPC endpoint", None)],
    [ev(WN_TUN, "They can use a ‘tunnel’ endpoint, a new type of VPC endpoint, to tunnel into the network segment and access resources located within it."),
     ev(WN_TUN, "Prior to this launch, customers who wanted to share their resources with another party such as an external vendor had to do it one at a time by creating a Resource Configuration for every resource.")],
    changed={"date": "2026-09-18", "was": "customers who wanted to share their resources with another party such as an external vendor had to do it one at a time by creating a Resource Configuration for every resource", "was_evidence": 1},
    vol="changed-since-2022", items=TUN, rel="reference", bullets=("3.4.K4",), note=NOT_EXAM))

f.append(F("privatelink-tunnel-endpoint-geneve-encapsulation", L, "restriction",
    "Tunnel endpoints require you to tunnel into another VPC using GENEVE encapsulation, and GENEVE traffic must use UDP and port 6081 on the tunnel endpoint.",
    "What encapsulation and port does a PrivateLink tunnel endpoint use?",
    [("port", "UDP and port 6081", None), ("encap", "GENEVE encapsulation", None)],
    [ev(CR, "Tunnel endpoints require you to tunnel into another VPC using GENEVE encapsulation."),
     ev(CR, "GENEVE traffic must use UDP and port 6081 on the tunnel endpoint.")],
    scope="tunnel endpoints", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=TUN, note=NOT_EXAM))

# ---- FAQ billing
f.append(F("privatelink-faq-billing-interface-gwlb-hourly-per-az", L, "pricing-dimension",
    "If you create an interface or Gateway Load Balancer VPC endpoint, you are charged for each hour that the endpoint is provisioned in each Availability Zone.",
    "How will I be charged for an interface or Gateway Load Balancer VPC endpoint?",
    [("rule", "provisioned in each Availability Zone", None)],
    [ev(PLF, "If you choose to create an interface or Gateway Load Balancer VPC endpoint in your VPC, you are charged for each hour that your VPC endpoint is provisioned in each Availability Zone.")],
    scope="interface and Gateway Load Balancer endpoints, per Availability Zone, per hour", rel="core", bullets=("4.4.S3",), vol="frequently-changing"))

f.append(F("privatelink-faq-billing-resource-endpoint-hourly-any-az-count", L, "pricing-dimension",
    "If you create a resource VPC endpoint, you are charged for each hour regardless of the number of Availability Zones the endpoint is provisioned in.",
    "How is a resource VPC endpoint billed per hour?",
    [("rule", "regardless of the number of Availability Zones", None)],
    [ev(PLF, "If you choose to create a resource VPC endpoint in your VPC, you are charged for each hour regardless of the number of Availability Zones your VPC endpoint is provisioned in.")],
    scope="resource endpoints, per hour", rel="extended", bullets=("4.4.S3",), vol="frequently-changing"))

f.append(F("privatelink-faq-billing-data-processing-and-partial-hour", L, "pricing-dimension",
    "Data processing charges apply for each gigabyte processed through VPC endpoints regardless of the traffic's source or destination, and each partial VPC endpoint-hour is billed as a full hour.",
    "Which data is charged by PrivateLink, and how are partial hours billed?",
    [("rule", "billed as a full hour", None)],
    [ev(PLF, "Data processing charges apply for each gigabyte processed through the VPC endpoints, regardless of the traffic’s source or destination. Each partial VPC endpoint-hour consumed is billed as a full hour.")],
    scope="VPC endpoints", rel="core", bullets=("4.4.S3",), vol="frequently-changing"))

# ---- DynamoDB and S3 endpoint choice, IPv6
f.append(F("vpc-endpoints-ddb-gateway-vs-interface-choice", E, "capability",
    "A DynamoDB gateway endpoint gives access from your VPC without an internet gateway or NAT device and at no additional cost, but it does not allow access from on-premises networks, from peered VPCs in other Regions or through a transit gateway; for those cases you must use an interface endpoint, which costs extra.",
    "When must you use an interface endpoint instead of a gateway endpoint for DynamoDB?",
    [("rule", "you must use an interface endpoint", None), ("cost", "available for an additional cost", None)],
    [ev(DDB, "With a gateway endpoint, you can access DynamoDB from your VPC, without requiring an internet gateway or NAT device for your VPC, and with no additional cost. However, gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway. For those scenarios, you must use an interface endpoint, which is available for an additional cost.")],
    scope="DynamoDB gateway endpoints and interface endpoints", rel="core", bullets=("1.2.K2",), tier0=True, vol="frequently-changing",
    items=["whats-new-v2#about-aws-whats-new-2024-03-amazon-dynamodb-aws-privatelink"],
    note="DynamoDB added interface endpoints (AWS PrivateLink) on 2024-03-19; see dynamodb-change-privatelink-interface-endpoints-2024-03."))

f.append(F("vpc-endpoints-ddb-gateway-endpoints-ipv4-only", E, "restriction",
    "The DynamoDB gateway endpoint page says gateway endpoints support only IPv4 traffic.",
    "Do DynamoDB gateway endpoints support IPv6 traffic?",
    [("rule", "Gateway endpoints support only IPv4 traffic", None)],
    [ev(DDB, "Gateway endpoints support only IPv4 traffic.")],
    scope="DynamoDB gateway endpoints", rel="reference", bullets=("1.2.K2",), vol="frequently-changing",
    note="Contrast: the S3 What's New post of Nov 10, 2025 adds IPv6 for S3 gateway and interface endpoints (vpc-endpoints-change-s3-ipv6-2025). The DynamoDB page still says IPv4 only."))

f.append(F("vpc-endpoints-change-s3-ipv6-2025", E, "change",
    "Amazon S3 now supports IPv6 addresses for AWS PrivateLink gateway and interface VPC endpoints, and the IPv6 support for S3 VPC endpoints is available at no additional cost.",
    "Do S3 gateway and interface endpoints support IPv6?",
    [("what", "IPv6 addresses for AWS PrivateLink gateway and interface", None)],
    [ev(WN_S3V6, "Amazon S3 now supports Internet Protocol version 6 (IPv6) addresses for AWS PrivateLink gateway and interface Virtual Private Cloud (VPC) endpoints."),
     ev(WN_S3V6, "IPv6 support for VPC endpoints for Amazon S3 is now available in all AWS Commercial Regions and the AWS GovCloud (US) Regions, at no additional cost.")],
    vol="stable", rel="extended", bullets=("1.2.K2",),
    note="What's New post dated Nov 10, 2025 (Posted on line). The post states no old value."))

f.append(F("privatelink-interface-endpoint-sends-tcp-or-udp", L, "capability",
    "An interface endpoint sends TCP or UDP traffic to an endpoint service.",
    "Which protocols does an interface endpoint carry to an endpoint service?",
    [("rule", "TCP or UDP traffic to an endpoint service", None)],
    [ev(CON, "`Interface` - Create an *interface endpoint* to send TCP or UDP traffic to an endpoint service.")],
    scope="interface endpoints", rel="extended", bullets=("1.2.K2",), vol="frequently-changing", items=["whats-new-v2#p153858256"],
    note="The What's New post of 2024-10-31 (UDP support and dual-stack Network Load Balancers) is blocked by robots.txt; the date of UDP support is not stated on any saved page."))

f.append(F("privatelink-ipv6-endpoint-service-needs-dualstack-nlb", L, "restriction",
    "To enable IPv6 for an endpoint service, all Network Load Balancers for the endpoint service must use the dualstack IP address type.",
    "What load balancer type does an IPv6 endpoint service need?",
    [("rule", "must use the dualstack IP address type", None)],
    [ev(SY, "All Network Load Balancers for the endpoint service must use the dualstack IP address type. The targets do not need to support IPv6 traffic. If the service processes source IP addresses from the proxy protocol version 2 header, it must process IPv6 addresses.")],
    scope="IPv6 for a PrivateLink endpoint service", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=["whats-new-v2#p153858256"]))

write("facts-changes-02.json", f)
