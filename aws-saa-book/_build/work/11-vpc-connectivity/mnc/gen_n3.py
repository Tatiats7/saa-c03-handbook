from mklib import *

T = "transit-gateway"
E = "vpc-endpoints"
L = "privatelink"
EK = ("4.4.S3",)
WNP = "docs/vpc/latest/tgw/what-is-transit-gateway"
f = []
HDR = "| Data Processed per month in an AWS Region | Pricing per GB of Data Processed ($) |"

# ---- Transit Gateway pricing
f.append(F("transit-gateway-pricing-hourly-attachment-and-data-processing", T, "pricing-dimension",
    "Transit Gateway is charged for the number of connections you make to it per hour and for the amount of traffic that flows through it.",
    "What are the two charge dimensions of AWS Transit Gateway?",
    [("dims", "connections that you make to the Transit Gateway", "per hour for each attachment, plus per gigabyte of traffic")],
    [ev(TGWP, "In AWS Transit Gateway you are charged for the number of connections that you make to the Transit Gateway per hour and the amount of traffic that flows through AWS Transit Gateway.")],
    scope="per attachment-hour and per GB of traffic", rel="core", bullets=("4.4.S3",), tier0=True, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-vpc-attachment-owner-billed", T, "pricing-dimension",
    "The VPC account owner is billed hourly for each hour that their VPCs are attached to a transit gateway.",
    "Who is billed for a VPC attachment to a transit gateway?",
    [("owner", "The VPC account owner is billed hourly", "the VPC owner pays for the attachment")],
    [ev(TGWP, "The VPC account owner is billed hourly for each hour that their Amazon VPCs are attached to an AWS Transit Gateway.")],
    scope="VPC attachments", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-vpn-attachment-owner-billed", T, "pricing-dimension",
    "For VPN attachments to a transit gateway, the transit gateway owner is billed hourly.",
    "Who is billed hourly for a VPN attachment to a transit gateway?",
    [("owner", "the Transit Gateway owner is billed hourly", "the transit gateway owner pays")],
    [ev(TGWP, "For AWS VPN attachments, the Transit Gateway owner is billed hourly.")],
    scope="VPN attachments", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-dx-attachment-owner-billed", T, "pricing-dimension",
    "For Direct Connect attachments to a transit gateway, the Direct Connect gateway owner is billed hourly.",
    "Who is billed hourly for a Direct Connect attachment to a transit gateway?",
    [("owner", "the Direct Connect Gateway owner is billed hourly", "the Direct Connect gateway owner pays")],
    [ev(TGWP, "For AWS Direct Connect attachments, the Direct Connect Gateway owner is billed hourly.")],
    scope="Direct Connect attachments", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-connect-attachment-owner-billed", T, "pricing-dimension",
    "For Transit Gateway Connect attachments (SD-WAN appliances), the transit gateway owner is billed hourly.",
    "Who is billed hourly for a Transit Gateway Connect attachment?",
    [("owner", "the Transit Gateway owner is billed hourly", "the transit gateway owner pays")],
    [ev(TGWP, "For Transit Gateway Connect attachments (SD-WAN appliances), the Transit Gateway owner is billed hourly.")],
    scope="Connect attachments", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-peering-attachment-each-owner-billed", T, "pricing-dimension",
    "For peering attachments, each transit gateway owner is billed hourly for the peering attachment with the other transit gateway.",
    "Who is billed hourly for a transit gateway peering attachment?",
    [("owner", "each Transit Gateway owner is billed hourly", "both transit gateway owners pay")],
    [ev(TGWP, "For peering attachments, each Transit Gateway owner is billed hourly for the peering attachment with the other Transit Gateway.")],
    scope="peering attachments", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-network-function-owner-billed", T, "pricing-dimension",
    "For network function attachments, the AWS Network Firewall owner is billed hourly.",
    "Who is billed hourly for a network function attachment to AWS Network Firewall?",
    [("owner", "the AWS Network Firewall owner is billed hourly", "the firewall owner pays")],
    [ev(TGWP, "For network function attachments, the AWS Network Firewall owner is billed hourly.")],
    scope="network function attachments", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-partial-hour-billed-as-full", T, "pricing-dimension",
    "Each partial transit gateway attachment hour is billed as a full hour.",
    "How is a partial hour of a transit gateway VPC attachment billed?",
    [("partial", "billed as a full hour", "a partial hour counts as a full hour")],
    [ev(TGWP, "Each partial VPC Transit Gateway hour consumed is billed as a full hour.")],
    scope="per VPC attachment-hour", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-data-processing-per-gb-sent-to-gateway", T, "pricing-dimension",
    "Data processing charges apply for each gigabyte sent from a VPC, Direct Connect, VPN or Network Firewall to the transit gateway, where 1 gigabyte is 1024 megabytes.",
    "Which traffic does Transit Gateway data processing charge for?",
    [("rule", "each gigabyte sent from a VPC", "per gigabyte sent to the transit gateway")],
    [ev(TGWP, "Data processing charges apply for each gigabyte sent from a VPC, Direct Connect or VPN or Network Firewall to the AWS Transit Gateway (1 gigabyte = 1024 megabytes).")],
    scope="per GB sent from a VPC, Direct Connect, VPN or Network Firewall attachment to the transit gateway", rel="core", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-no-processing-from-peering-attachment", T, "pricing-dimension",
    "Data processing charges do not apply for data sent from a peering attachment to a transit gateway.",
    "Is data sent from a peering attachment to a transit gateway charged for data processing?",
    [("rule", "data sent from a peering attachment", "no processing charge from a peering attachment")],
    [ev(TGWP, "Data processing charges do not apply for data sent from a peering attachment to a Transit Gateway.")],
    scope="data sent from a peering attachment to a transit gateway", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-standard-data-transfer-in-addition", T, "pricing-dimension",
    "You incur standard AWS data transfer charges in addition to any Transit Gateway charges.",
    "Does Transit Gateway pricing include standard data transfer charges?",
    [("rule", "standard AWS data transfer charges", None)],
    [ev(TGWP, "Data Transfer Charges: You will incur standard AWS data transfer charges, in addition to any Transit Gateway charges.")],
    scope="data transfer", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-default-allocation-source-attachment-owner", T, "default",
    "By default, transit gateway data processing charges are allocated to the account that owns the source attachment.",
    "Which account is charged for transit gateway data processing by default?",
    [("default", "account that owns the source attachment", "the sender's account pays by default")],
    [ev(WNP, "By default, data processing charges are allocated to the account that owns the source attachment.")],
    scope="transit gateway data processing charges", dom="default", adj=True,
    cond="flexible cost allocation can customize how these charges are allocated", rel="core", bullets=EK, tier0=True,
    vol="frequently-changing", items=["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"]))

f.append(F("transit-gateway-pricing-processing-charged-to-sending-vpc-owner", T, "pricing-dimension",
    "In the pricing example, transit gateway data processing is charged to the VPC owner who sends the traffic to the transit gateway.",
    "Who is charged for transit gateway data processing in the pricing example?",
    [("payer", "the VPC owner who sends the traffic", "the sending VPC owner pays")],
    [ev(TGWP, "Data Processing is charged to the VPC owner who sends the traffic to Transit Gateway.")],
    scope="pricing example, VPC attachment", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("transit-gateway-pricing-inter-region-peering-example-total", T, "price",
    "In the pricing page example, 1 GB sent over a transit gateway peering attachment between two Regions costs $0.04 in traffic charges: $0.02 for Transit Gateway data processing on the first transit gateway and $0.02 for outbound inter-Region data transfer.",
    "What does 1 GB over an inter-Region transit gateway peering attachment cost in the pricing page example?",
    [("total", "$0.04", "four cents"), ("processing", "$0.02 for Transit Gateway Data Processing", "two cents for data processing"),
     ("transfer", "$0.02 for outbound inter-Region data transfer charges", "two cents for outbound inter-Region transfer")],
    [ev(TGWP, "The total traffic related charges will result in a charge of $0.04. This charge comprises $0.02 for Transit Gateway Data Processing on Transit Gateway #1 along with $0.02 for outbound inter-Region data transfer charges.")],
    scope="pricing page example: 1 GB from a VPC on transit gateway 1 (N. Virginia) over a peering attachment to transit gateway 2 (Oregon)",
    rel="extended", bullets=EK, vol="frequently-changing",
    note="Example amounts as printed by the pricing page; check the page before quoting a rate as current."))

f.append(F("transit-gateway-pricing-inter-region-receiving-side-no-charge", T, "pricing-dimension",
    "In the inter-Region peering example, the receiving transit gateway does not incur data processing charges, and inbound inter-Region data transfer is free, so no further charges apply on the receiving side.",
    "Is the receiving side of an inter-Region transit gateway peering charged?",
    [("rule", "inbound inter-Region data transfer charges are free", "inbound inter-Region transfer is free")],
    [ev(TGWP, "Here Transit Gateway #2 will not incur data processing charges, as they do not apply for data sent from a peering attachment to a Transit Gateway. As inbound inter-Region data transfer charges are free, no further charges apply to the Transit Gateway #2 (Oregon region) side.")],
    scope="receiving transit gateway of an inter-Region peering attachment", rel="extended", bullets=EK, vol="frequently-changing"))

# ---- Endpoint and PrivateLink pricing
f.append(F("vpc-endpoints-pricing-hourly-per-az-while-provisioned", E, "pricing-dimension",
    "You are billed for each hour that a VPC endpoint remains provisioned in each Availability Zone, whatever the state of its association with the service.",
    "How is an interface VPC endpoint billed per hour?",
    [("rule", "remains provisioned in each Availability Zone", "per hour per Availability Zone while provisioned")],
    [ev(PLP, "You will be billed for each hour that your VPC endpoint remains provisioned in each Availability Zone, irrespective of the state of its association with the service (learn more).")],
    scope="per VPC endpoint, per Availability Zone, per hour", rel="core", bullets=EK, tier0=True, vol="frequently-changing"))

f.append(F("vpc-endpoints-pricing-partial-hour-billed-as-full", E, "pricing-dimension",
    "Each partial VPC endpoint hour is billed as a full hour.",
    "How is a partial hour of a VPC endpoint billed?",
    [("partial", "billed as a full hour", "a partial hour counts as a full hour")],
    [ev(PLP, "Each partial VPC endpoint-hour consumed is billed as a full hour.")],
    scope="per VPC endpoint-hour", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("vpc-endpoints-pricing-data-processing-per-gb-any-direction", E, "pricing-dimension",
    "Data processing charges apply for each gigabyte processed through a VPC endpoint, regardless of the traffic's source or destination.",
    "Is data processed through a VPC endpoint charged per gigabyte?",
    [("rule", "each Gigabyte processed through the VPC endpoint", "per gigabyte processed, in any direction")],
    [ev(PLP, "Data processing charges apply for each Gigabyte processed through the VPC endpoint regardless of the traffic’s source or destination.")],
    scope="per GB processed through a VPC endpoint", rel="core", bullets=EK, vol="frequently-changing"))

f.append(F("vpc-endpoints-pricing-hourly-stops-on-delete", E, "pricing-dimension",
    "Hourly billing for a VPC endpoint stops when you delete it.",
    "When does hourly billing for a VPC endpoint stop?",
    [("stop", "stop when you delete it", "billing stops when you delete the endpoint")],
    [ev(PLP, "Such hourly billing for your VPC endpoint will stop when you delete it.")],
    scope="per VPC endpoint", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("vpc-endpoints-pricing-interface-tiers-apply-region-total", E, "pricing-dimension",
    "Interface endpoint data processing pricing tiers apply to the total data processed by all interface endpoints in an AWS Region.",
    "Over what total do interface endpoint data processing price tiers apply?",
    [("scope", "total data processed by all Interface Endpoints", "tiers apply to the Region total")],
    [ev(PLP, "Below pricing tiers apply on the total data processed by all Interface Endpoints in an AWS Region:")],
    scope="all interface endpoints in one AWS Region, per month", rel="extended", bullets=EK, vol="frequently-changing"))

f.append(F("vpc-endpoints-pricing-resource-tunnel-tiers-separate", E, "pricing-dimension",
    "Resource and tunnel endpoint data processing tiers apply to the total data processed in a Region through those endpoints, separately for resource endpoints and for tunnel endpoints.",
    "Do resource endpoints and tunnel endpoints share one data processing tier?",
    [("rule", "apply to Resource and Tunnel Endpoints separately", None)],
    [ev(PLP, "Below pricing tiers apply on the total data processed in an AWS Region through Resource/Tunnel Endpoints. They apply to Resource and Tunnel Endpoints separately.")],
    scope="resource and tunnel endpoints in one AWS Region", rel="reference", bullets=EK, vol="frequently-changing",
    note="Tunnel endpoints are GA on 2026-09-18 (not examinable yet); the sentence also covers resource endpoints."))

f.append(F("vpc-endpoints-pricing-example-tier-rates-per-gb", E, "price",
    "The resource endpoint pricing example charges $0.01 per GB for the first PB, $0.006 per GB for the next 4 PB and $0.004 per GB for 5 PB and more.",
    "What per-GB tier rates does the PrivateLink pricing example use for resource endpoint data processing?",
    [("first", "$0.01 per GB for the first PB", "one cent per gigabyte for the first petabyte"),
     ("next", "$0.006 per GB for next 4PB", None), ("over", "$0.004 per GB for 5+ PBs", None)],
    [ev(PLP, "You pay a data processing charge of $0.01 per GB for the first PB, $0.006 per GB for next 4PB, and $0.004 per GB for 5+ PBs.")],
    scope="resource endpoint data processing, per GB, monthly Region total", rel="reference", bullets=EK, vol="frequently-changing",
    note="The interface endpoint tier table on the same page lists the same three rates (first 1 PB, next 4 PB, anything over 5 PB)."))

f.append(F("privatelink-pricing-resource-endpoint-example-hourly", L, "price",
    "The PrivateLink pricing example for resource endpoints uses an hourly charge of $0.02 per resource per hour.",
    "What hourly charge does the PrivateLink resource endpoint pricing example use?",
    [("hourly", "$0.02 per resource per hour", "two cents per resource per hour")],
    [ev(PLP, "You pay an hourly charge of $0.02 per resource per hour")],
    scope="resource endpoint example, us-east-1, per resource per hour", rel="reference", bullets=EK, vol="frequently-changing"))

f.append(F("privatelink-pricing-cross-region-no-premium", L, "pricing-dimension",
    "Accessing a service in another Region over PrivateLink has no premium, but you pay the standard PrivateLink data processing and hourly charges plus cross-Region data transfer rates.",
    "What does PrivateLink cross-Region connectivity cost the consumer?",
    [("rule", "no premium for accessing a service", "no extra premium, but cross-Region transfer rates apply")],
    [ev(PLP, "There is no premium for accessing a service in another region. You incur standard PrivateLink charges for data processing and hours. In addition, AWS cross-region data transfer rates will apply.")],
    scope="interface endpoint to a supported endpoint service in another Region", rel="extended", bullets=EK, vol="frequently-changing",
    items=["docs/vpc/latest/privatelink/doc-history#11"]))

f.append(F("privatelink-pricing-cross-region-endpoint-owner-pays-both-directions", L, "pricing-dimension",
    "The interface endpoint owner is charged for each gigabyte transferred between Regions, regardless of the direction of the data transfer.",
    "Which direction of cross-Region PrivateLink traffic is charged to the endpoint owner?",
    [("rule", "regardless of the directionality of the data transfer", "both directions are charged")],
    [ev(PLP, "The Interface endpoint owner will be charged for each Gigabyte transferred inter-region regardless of the directionality of the data transfer.")],
    scope="cross-Region interface endpoint, per GB", rel="extended", bullets=EK, vol="frequently-changing",
    items=["docs/vpc/latest/privatelink/doc-history#11"]))

f.append(F("privatelink-pricing-cross-region-provider-hourly-per-active-region", L, "pricing-dimension",
    "A service provider incurs a fixed hourly charge per active remote Region, whatever the number of VPC endpoints that use the service; a Region is active when at least one interface endpoint is connected to the service.",
    "How is a PrivateLink service provider charged for cross-Region access?",
    [("rule", "fixed hourly charge per active remote region", "one hourly charge per active remote Region")],
    [ev(PLP, "The service provider incurs a fixed hourly charge per active remote region regardless of the number of VPC endpoints using your service. A region is considered active if it has at least one Interface endpoint connected to the service.")],
    scope="per active remote Region, per hour, service provider", rel="extended", bullets=EK, vol="frequently-changing",
    items=["docs/vpc/latest/privatelink/doc-history#11"]))

f.append(F("privatelink-pricing-cross-region-provider-no-transfer-charge", L, "pricing-dimension",
    "The service provider does not incur any additional charges for inter-Region data transfer in cross-Region PrivateLink.",
    "Does the PrivateLink service provider pay for inter-Region data transfer?",
    [("rule", "does not incur any additional charges", None)],
    [ev(PLP, "The service provider does not incur any additional charges for inter-region data transfer.")],
    scope="service provider, cross-Region access", rel="reference", bullets=EK, vol="frequently-changing",
    items=["docs/vpc/latest/privatelink/doc-history#11"]))

write("facts-numbers-03.json", f)
