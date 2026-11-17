from mklib import *

T = "transit-gateway"
WN_FCA = "www/about-aws/whats-new/2025/11/aws-transit-gateway-flexible-cost-allocation"
MP = "docs/vpc/latest/tgw/metering-policy"
ES = "docs/vpc/latest/tgw/tgw-encryption-support"
NF = "docs/vpc/latest/tgw/tgw-nf-fw"
HW = "docs/vpc/latest/tgw/how-transit-gateways-work"
VA = "docs/vpc/latest/tgw/tgw-vpc-attachments"
CV = "docs/vpc/latest/tgw/tgw-client-vpn-attachments"
WN_CV = "www/about-aws/whats-new/2026/04/aws-client-vpn-transit-gateway"
WN_PBR = "www/about-aws/whats-new/2026/07/aws-transit-gateway-policy-based-routing"
PT = "docs/vpc/latest/tgw/tgw-policy-tables"
WN_NF = "www/about-aws/whats-new/2025/06/aws-network-firewall-transit-gateway-native-integration"
f = []

FCA_ITEMS = ["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"]

f.append(F("transit-gateway-change-fca-sender-pay-to-flexible-2025", T, "change",
    "On November 21, 2025 AWS announced general availability of Flexible Cost Allocation on Transit Gateway; before it, Transit Gateway only used a sender-pay model, where the source attachment account owner was responsible for all data usage related costs.",
    "What changed for who pays Transit Gateway data usage costs with Flexible Cost Allocation?",
    [("date", "November 21, 2025", "November 2025"), ("was", "only used a sender-pay model", "before, only the sender paid")],
    [ev(WN_FCA, "AWS announces general availability of Flexible Cost Allocation on AWS Transit Gateway, enhancing how you can distribute Transit Gateway costs across your organization."),
     ev(WN_FCA, "Previously, Transit Gateway only used a sender-pay model, where the source attachment account owner was responsible for all data usage related costs.")],
    changed={"date": "2025-11-21", "was": "Transit Gateway only used a sender-pay model", "was_evidence": 1},
    vol="changed-since-2022", items=FCA_ITEMS, rel="extended", bullets=("4.4.S3",),
    note="The Transit Gateway document history dates the same feature November 20, 2025 (transit-gateway-change-flexible-cost-allocation-history-2025)."))

f.append(F("transit-gateway-fca-allocation-options-default-source", T, "default",
    "By default a transit gateway allocates data processing charges to the account that owns the source attachment; since Flexible Cost Allocation (November 21, 2025) a metering policy can instead allocate charges to the destination attachment owner or the transit gateway owner.",
    "Which accounts can a transit gateway metering policy charge for data processing, and which is the default?",
    [("default", "account that owns the source attachment", "the source attachment owner pays by default"),
     ("dest", "owns the destination attachment", "the destination attachment owner"),
     ("tgw", "owns the transit gateway", "the transit gateway owner")],
    [ev(MP, "By default, transit gateway uses a sender-based cost allocation model where data processing charges are allocated to the account that owns the source attachment."),
     ev(MP, "**Destination attachment owner** - Charges are allocated to the account that owns the destination attachment"),
     ev(MP, "**Transit Gateway owner** - Charges are allocated to the account that owns the transit gateway"),
     ev(WN_FCA, "Previously, Transit Gateway only used a sender-pay model, where the source attachment account owner was responsible for all data usage related costs.")],
    scope="transit gateway data processing charges", dom="default", adj=True,
    cond="a metering policy rule can name the source attachment owner, the destination attachment owner or the transit gateway owner",
    changed={"date": "2025-11-21", "was": "Transit Gateway only used a sender-pay model", "was_evidence": 3},
    vol="changed-since-2022", items=FCA_ITEMS, rel="core", bullets=("4.4.S3",), tier0=True,
    note="Older exam questions assume the sender always pays. Checked against the metering-policy page and the What's New post."))

f.append(F("transit-gateway-fca-no-additional-charge", T, "pricing-dimension",
    "There is no additional charge for using Flexible Cost Allocation on Transit Gateway.",
    "Does Flexible Cost Allocation cost extra on Transit Gateway?",
    [("rule", "no additional charge for using FCA", None)],
    [ev(WN_FCA, "There is no additional charge for using FCA on Transit Gateway.")],
    scope="Flexible Cost Allocation (FCA)", rel="reference", bullets=("4.4.S3",), vol="frequently-changing", items=FCA_ITEMS))

# Encryption support
ES_ITEMS = ["docs/vpc/latest/tgw/doc-history#13"]
f.append(F("transit-gateway-encryption-support-enforces-in-transit", T, "capability",
    "Encryption Support on a transit gateway lets you enforce encryption-in-transit for traffic between VPCs attached to the transit gateway; you activate it manually with the modify-transit-gateway command.",
    "What does Encryption Support on a transit gateway do, and how is it turned on?",
    [("what", "enforce encryption-in-transit for traffic between VPCs", None)],
    [ev(ES, "Encryption Support on Transit Gateway allows you to enforce encryption-in-transit for traffic between VPCs attached to a Transit Gateway."),
     ev(ES, "You will need to manually activate Encryption Support on the Transit Gateway using the [modify-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway.html) command to encrypt traffic between the VPCs.")],
    scope="per transit gateway", rel="extended", bullets=("4.4.K6",), vol="frequently-changing", items=ES_ITEMS))

f.append(F("transit-gateway-encryption-support-unsupported-features", T, "restriction",
    "Connect attachments, peering attachments, Network Firewall attachments, VPN Concentrator attachments, Client VPN attachments, security group references and multicast features are not supported with Encryption Support.",
    "Which transit gateway features cannot be used with Encryption Support?",
    [("rule", "not supported with Encryption Support", None)],
    [ev(ES, "Connect attachments, Peering attachments, Network Firewall attachments, VPN Concentrator attachments, Client VPN attachments, security group references, and multicast features are not supported with Encryption Support.")],
    scope="a transit gateway with Encryption Support enabled", rel="extended", bullets=("4.4.K6",), vol="frequently-changing", items=ES_ITEMS))

# Network function attachments
NF_ITEMS = ["docs/vpc/latest/tgw/doc-history#14", "whats-new-v2#v1789696919"]
f.append(F("transit-gateway-change-network-firewall-direct-attachment-2025", T, "change",
    "Since June 16, 2025 you can create a network function attachment that connects a transit gateway directly to AWS Network Firewall, which eliminates the need to create and manage inspection VPCs.",
    "How do you connect AWS Network Firewall to a transit gateway without an inspection VPC?",
    [("date", "June 16, 2025", "June 2025"), ("what", "the need to create and manage inspection VPCs", None)],
    [ev(NF, "You can create a network function attachment to connect your transit gateway directly to AWS Network Firewall. This eliminates the need to create and manage inspection VPCs.")],
    changed={"date": "2025-06-16", "was": "create and manage inspection VPCs", "was_evidence": 0},
    vol="changed-since-2022", items=NF_ITEMS, rel="extended", bullets=("4.4.K6",),
    note="The date comes from the Transit Gateway document history row of June 16, 2025 (transit-gateway-change-network-function-attachments-2025); see also network-firewall-change-tgw-attached-2025."))

f.append(F("transit-gateway-network-function-static-routing-only", T, "restriction",
    "A transit gateway supports only static routing on Network Firewall attachments.",
    "What routing does a transit gateway support on Network Firewall attachments?",
    [("rule", "only static routing on Network Firewall attachments", None)],
    [ev(HW, "Transit Gateway supports only static routing on Network Firewall attachments.")],
    scope="Network Firewall (network function) attachments", rel="extended", bullets=("4.4.K6",), vol="frequently-changing", items=NF_ITEMS))

f.append(F("transit-gateway-network-function-appliance-mode-automatic", T, "behavior",
    "A Network Firewall attachment on a transit gateway is created with appliance mode automatically enabled, which eliminates the need to explicitly manage inspection VPCs.",
    "Is appliance mode enabled on a Network Firewall attachment to a transit gateway?",
    [("rule", "created with appliance mode automatically enabled", None)],
    [ev(HW, "A Network Firewall attachment is created with appliance mode automatically enabled. This eliminates the need to explicitly manage inspection VPCs.")],
    scope="Network Firewall attachments", rel="extended", bullets=("4.4.K6",), vol="frequently-changing", items=NF_ITEMS))

f.append(F("transit-gateway-network-function-no-third-party-firewalls", T, "restriction",
    "The Network Firewall integration note on the transit gateway page says third-party firewalls are not supported.",
    "Can a third-party firewall use a Network Firewall attachment to a transit gateway?",
    [("rule", "Third-party firewalls are not supported", None)],
    [ev(HW, "Third-party firewalls are not supported.")],
    scope="AWS Network Firewall integration with a transit gateway", rel="reference", bullets=("4.4.K6",), vol="frequently-changing", items=NF_ITEMS))

# Security group referencing
SG_ITEMS = ["docs/vpc/latest/tgw/doc-history#15", "whats-new-v2#p105573989"]
sgs = [
    ("inbound-rules-only", "You can reference a security group across VPCs attached to the same transit gateway in inbound rules only; outbound security rules do not support security group referencing.",
     "Can a transit gateway security group reference be used in outbound rules?", "inbound rules only", None,
     "You can cross-reference security groups in inbound rules only. Outbound security rules do not support security group referencing.", "core"),
    ("needs-both-enabled", "Security group referencing across a transit gateway works only if it has been enabled for both the transit gateway and its VPC attachments.",
     "Where must security group referencing be enabled for it to work across a transit gateway?", "will only work if it has been enabled", None,
     "Security group referencing support can be configured for both transit gateways and transit gateway VPC attachments and will only work if it has been enabled for both a transit gateway and its VPC attachments.", "extended"),
    ("not-across-peering", "Security group referencing is not supported across transit gateway peering connections; both VPCs must be attached to the same transit gateway.",
     "Does security group referencing work across transit gateway peering?", "not supported across transit gateway peering connections", None,
     "Security group referencing is not supported across transit gateway peering connections. Both VPCs must be attached to the same transit gateway.", "core"),
    ("no-additional-cost", "There are no additional costs associated with enabling or using security group referencing on a transit gateway.",
     "Does security group referencing on a transit gateway cost extra?", "no additional costs", None,
     "There are no additional costs associated with enabling or using security group referencing.", "extended"),
    ("not-for-privatelink-endpoints", "Security group referencing through a transit gateway is not supported for PrivateLink endpoints; AWS recommends IP CIDR-based security rules as an alternative.",
     "Does transit gateway security group referencing work for PrivateLink endpoints?", "not supported for PrivateLink endpoints", None,
     "Security group referencing is not supported for PrivateLink endpoints. We recommend using IP CIDR-based security rules as an alternative.", "extended"),
    ("not-in-use1-az3", "Security group referencing is not supported for transit gateway VPC attachments in the Availability Zone use1-az3.",
     "In which Availability Zone does transit gateway security group referencing not work for VPC attachments?", "availability zone use1-az3", None,
     "Security group referencing is not supported for VPC attachments in the availability zone use1-az3.", "reference"),
]
for slug, claim, q, disp, sp, quote, rel in sgs:
    f.append(F("transit-gateway-sg-referencing-" + slug, T, "restriction" if "no-additional" not in slug else "pricing-dimension",
        claim, q, [("rule", disp, sp)], [ev(VA, quote)],
        scope="security group referencing across VPCs attached to one transit gateway", rel=rel, bullets=("4.4.K6",),
        vol="frequently-changing", items=SG_ITEMS))

# Client VPN
CV_ITEMS = ["docs/vpc/latest/tgw/doc-history#11", "whats-new-v2#launch-w3r3xlmgyitelkwytry5g8"]
f.append(F("transit-gateway-change-client-vpn-native-integration-2026", T, "change",
    "On April 23, 2026 AWS announced native Transit Gateway integration for Client VPN: before it, connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC, and the native attachment eliminates the need for that intermediate VPC.",
    "How did connecting Client VPN to many VPCs change in April 2026?",
    [("date", "April 23, 2026", "April 2026"), ("what", "eliminates the need for an intermediate VPC", None)],
    [ev(WN_CV, "Previously, connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC, adding operational complexity as you needed to manage additional resources."),
     ev(WN_CV, "Native Transit Gateway attachment eliminates the need for an intermediate VPC, letting you provide centralized remote access to multiple VPCs and on-premises networks directly from your Client VPN endpoint.")],
    changed={"date": "2026-04-23", "was": "connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC", "was_evidence": 0},
    vol="changed-since-2022", items=CV_ITEMS, rel="extended", bullets=("3.4.K4",),
    note="Examinable (before 2026-07-15). The Transit Gateway document history dates the Client VPN attachment April 20, 2026."))

f.append(F("transit-gateway-client-vpn-attachment-created-on-association", T, "behavior",
    "When you associate a Client VPN endpoint with a transit gateway, a Client VPN attachment is created automatically, so you can route traffic between your VPCs, on-premises networks and Client VPN endpoints.",
    "What happens when you associate a Client VPN endpoint with a transit gateway?",
    [("rule", "a Client VPN attachment is automatically created", None)],
    [ev(CV, "When you associate a Client VPN endpoint with a transit gateway, a Client VPN attachment is automatically created, allowing you to route traffic between your VPCs, on-premises networks, and Client VPN endpoints.")],
    scope="Client VPN attachments", rel="extended", bullets=("3.4.K4",), vol="frequently-changing", items=CV_ITEMS))

f.append(F("transit-gateway-client-vpn-attachment-needs-cidr-block", T, "restriction",
    "A transit gateway must have an assigned IPv4 or IPv6 CIDR block before you can create a Client VPN attachment.",
    "What must a transit gateway have before you create a Client VPN attachment?",
    [("rule", "assigned IPv4 or IPv6 CIDR block", None)],
    [ev(CV, "Your transit gateway must have an assigned IPv4 or IPv6 CIDR block before you can create a Client VPN attachment.")],
    scope="Client VPN attachments", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=CV_ITEMS))

f.append(F("transit-gateway-client-vpn-attachment-needs-route-propagation", T, "restriction",
    "Route table propagation must be enabled for Client VPN attachments to allow traffic between the Client VPN endpoint and the transit gateway.",
    "What routing setting do Client VPN attachments need on a transit gateway?",
    [("rule", "Route table propagation must be enabled", None)],
    [ev(CV, "Route table propagation must be enabled for Client VPN attachments to allow traffic between your Client VPN endpoint and transit gateway. See [Enable route propagation](https://docs.aws.amazon.com/vpc/latest/tgw/enable-tgw-route-propagation.html).")],
    scope="Client VPN attachments", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=CV_ITEMS))

f.append(F("transit-gateway-client-vpn-native-integration-no-extra-charge", T, "pricing-dimension",
    "There are no additional charges for the native Client VPN and Transit Gateway integration beyond the standard pricing of AWS Client VPN and AWS Transit Gateway.",
    "Does the native Client VPN attachment to a transit gateway cost extra?",
    [("rule", "no additional charges for this native integration", None)],
    [ev(WN_CV, "There are no additional charges for this native integration beyond standard pricing of AWS Client VPN and AWS Transit Gateway.")],
    scope="native Client VPN and Transit Gateway integration", rel="reference", bullets=("3.4.K4",), vol="frequently-changing", items=CV_ITEMS))

# Policy-based routing: NOT EXAMINABLE YET
PBR_ITEMS = ["docs/vpc/latest/tgw/doc-history#10", "whats-new-v2#launch-pahjucn5xzkrlgqypk2nik"]
NOTE_PBR = "NOT EXAMINABLE YET: Policy-Based Routing is GA after 2026-07-15 (What's New of Jul 30, 2026; history row of July 28, 2026). Label it 'not examinable yet'."
f.append(F("transit-gateway-change-pbr-ga-2026", T, "change",
    "AWS announced general availability of Policy-Based Routing on AWS Transit Gateway (posted Jul 30, 2026), so forwarding decisions can use source and destination IP addresses, ports and protocol rather than destination IP address alone.",
    "What does Policy-Based Routing add to Transit Gateway?",
    [("date", "Jul 30, 2026", "July 2026"), ("what", "rather than destination IP address alone", None)],
    [ev(WN_PBR, "With PBR, forwarding decisions can be based on a combination of packet attributes including source and destination IP addresses, ports, and protocol rather than destination IP address alone."),
     ev(WN_PBR, "Posted on: Jul 30, 2026")],
    vol="stable", items=PBR_ITEMS, rel="reference", bullets=("4.4.K6",), note=NOTE_PBR))

f.append(F("transit-gateway-pbr-policy-table-or-route-table-not-both", T, "restriction",
    "A policy table replaces the standard route table on a transit gateway attachment, and an attachment can be associated with either a policy table or a route table, but not both.",
    "Can a transit gateway attachment use a policy table and a route table together?",
    [("rule", "either a policy table or a route table, but not both", None)],
    [ev(PT, "A policy table replaces the standard route table on an attachment. An attachment can be associated with either a policy table or a route table, but not both.")],
    scope="per transit gateway attachment", rel="reference", bullets=("4.4.K6",), vol="frequently-changing", items=PBR_ITEMS, note=NOTE_PBR))

f.append(F("transit-gateway-pbr-no-additional-charge", T, "pricing-dimension",
    "Policy-Based Routing for Transit Gateway is available at no additional charge beyond standard transit gateway fees.",
    "Does Policy-Based Routing cost extra on Transit Gateway?",
    [("rule", "no additional charge beyond standard transit gateway fees", None)],
    [ev(PT, "PBR is available in all AWS Regions where transit gateway is available at no additional charge beyond standard transit gateway fees.")],
    scope="Policy-Based Routing", rel="reference", bullets=("4.4.K6",), vol="frequently-changing", items=PBR_ITEMS, note=NOTE_PBR))

write("facts-changes-01.json", f)
