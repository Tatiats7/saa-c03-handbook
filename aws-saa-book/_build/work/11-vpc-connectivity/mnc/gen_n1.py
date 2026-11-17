from mklib import *

T = "transit-gateway"
CP = "(Optional) not"
f1 = []

f1.append(F("transit-gateway-quotas-are-region-specific", T, "behavior",
    "Unless a Transit Gateway quota is noted otherwise, the quota is Region-specific.",
    "Are transit gateway quotas counted per Region?",
    [("scope", "Region-specific", "counted per Region")],
    [ev(TGWQ, "Unless otherwise noted, each quota is Region-specific.")],
    scope="Transit Gateway quotas", rel="reference"))

f1.append(F("transit-gateway-one-vpc-attachment-per-vpc", T, "restriction",
    "A transit gateway cannot have more than one VPC attachment to the same VPC.",
    "How many VPC attachments can one transit gateway have to the same VPC?",
    [("rule", "one VPC attachment to the same VPC", "only one VPC attachment per VPC")],
    [ev(TGWQ, "A transit gateway cannot have more than one VPC attachment to the same VPC.")],
    scope="per transit gateway, per VPC", rel="extended"))

f1.append(F("transit-gateway-bandwidth-beyond-default-attempt", T, "behavior",
    "For VPC attachments, Direct Connect gateways and peered transit gateway attachments, AWS says it will attempt to provide additional bandwidth beyond the default value.",
    "Can a transit gateway VPC attachment get more bandwidth than the default?",
    [("note", "additional bandwidth beyond the default value", "AWS will try to give more bandwidth")],
    [ev(TGWQ, "For VPC attachments, Direct Connect gateways, or peered transit gateway attachments, we will attempt to provide additional bandwidth beyond the default value.")],
    scope="VPC attachments, Direct Connect gateways, peered transit gateway attachments", rel="reference"))

f1.append(F("transit-gateway-ecmp-vpn-dynamic-routing-only", T, "restriction",
    "ECMP across VPN tunnels on a transit gateway needs a VPN connection configured for dynamic routing; ECMP is not supported on VPN connections that use static routing.",
    "Which VPN routing type supports ECMP on a transit gateway?",
    [("needs", "configured for dynamic routing", "dynamic routing is required"),
     ("not", "not supported on VPN connections", None)],
    [ev(TGWQ, "To use ECMP, the VPN connection must be configured for dynamic routing. ECMP is not supported on VPN connections that use static routing.")],
    scope="Site-to-Site VPN connections attached to a transit gateway", rel="extended"))

f1.append(F("transit-gateway-connect-peers-20-gbps", T, "limit",
    "You can create up to 4 Connect peers per Connect attachment, for up to 20 Gbps in total bandwidth per Connect attachment, as long as the underlying transport (VPC or Direct Connect) attachment supports the required bandwidth.",
    "How many Connect peers and how much total bandwidth can one Connect attachment have?",
    [("peers", "up to 4 Connect peers per Connect attachment", "up to four Connect peers"),
     ("bandwidth", "up to 20 Gbps in total bandwidth per Connect attachment", "up to twenty gigabits per second in total")],
    [ev(TGWQ, "You can create up to 4 Connect peers per Connect attachment (up to 20 Gbps in total bandwidth per Connect attachment), as long as the underlying transport (VPC or Direct Connect) attachment supports the required bandwidth.")],
    scope="per Connect attachment", dom="max", adj=False,
    cond="the underlying transport (VPC or Direct Connect) attachment must support the required bandwidth", rel="reference"))

f1.append(F("transit-gateway-mtu-8500-bytes", T, "limit",
    "A transit gateway supports an MTU of 8500 bytes for traffic between VPCs, Direct Connect, Transit Gateway Connect and peering attachments, including intra-Region, inter-Region and Cloud WAN peering attachments.",
    "What MTU does a transit gateway support between VPCs and over peering attachments?",
    [("mtu", "MTU of 8500 bytes", "an M T U of eighty-five hundred bytes")],
    [ev(TGWQ, "A transit gateway supports an MTU of 8500 bytes for traffic between VPCs, Direct Connect, Transit Gateway Connect, and peering attachments (intra-Region, inter-Region, and Cloud WAN peering attachments).")],
    scope="traffic between VPCs, Direct Connect, Connect and peering attachments", dom="max", adj=False, rel="core", tier0=True))

f1.append(F("transit-gateway-mtu-vpn-1500-bytes", T, "limit",
    "Traffic over VPN connections on a transit gateway can have an MTU of 1500 bytes.",
    "What MTU can traffic over VPN connections have on a transit gateway?",
    [("mtu", "MTU of 1500 bytes", "an M T U of fifteen hundred bytes")],
    [ev(TGWQ, "Traffic over VPN connections can have an MTU of 1500 bytes.")],
    scope="VPN connections attached to a transit gateway", dom="max", adj=False, rel="extended"))

f1.append(F("transit-gateway-mtu-mismatch-peering-migration", T, "behavior",
    "When you migrate from VPC peering to a transit gateway, an MTU size mismatch between VPC peering and the transit gateway might drop some asymmetric traffic packets; the page says to update both VPCs at the same time to avoid dropped jumbo packets.",
    "What MTU problem can happen when you migrate from VPC peering to a transit gateway?",
    [("risk", "MTU size mismatch", "an M T U size mismatch")],
    [ev(TGWQ, "When migrating from VPC peering to use a transit gateway, an MTU size mismatch between VPC peering and the transit gateway might result in some asymmetric traffic packets dropping. Update both VPCs at the same time to avoid jumbo packets dropping due to a size mismatch.")],
    scope="migration from VPC peering to a transit gateway", rel="extended", hard=False))

f1.append(F("transit-gateway-mss-clamping-all-packets", T, "behavior",
    "A transit gateway enforces Maximum Segment Size (MSS) clamping for all packets.",
    "Does a transit gateway clamp the Maximum Segment Size?",
    [("mss", "Maximum Segment Size (MSS) clamping", None)],
    [ev(TGWQ, "The transit gateway enforces Maximum Segment Size (MSS) clamping for all packets.")],
    scope="all packets through a transit gateway", rel="reference", hard=True))

f1.append(F("transit-gateway-pmtud-vpc-and-connect", T, "capability",
    "Transit gateways support Path MTU Discovery (PMTUD) for traffic ingressing on VPC and Connect attachments.",
    "On which attachment types does a transit gateway support Path MTU Discovery?",
    [("pmtud", "support Path MTU Discovery (PMTUD)", None)],
    [ev(TGWQ, "Transit gateways support Path MTU Discovery (PMTUD) for traffic ingressing on VPC and Connect attachments.")],
    scope="VPC and Connect attachments", rel="reference", hard=False,
    note="Related: the AWS What's New post of 2024-11-14 (Path MTU support) is blocked by robots.txt; this guide sentence is the current truth."))

f1.append(F("transit-gateway-no-pmtud-vpn-dx-peering", T, "restriction",
    "Transit gateways do not support Path MTU Discovery on Site-to-Site VPN, Direct Connect and peering attachments.",
    "On which attachment types does a transit gateway not support Path MTU Discovery?",
    [("no-pmtud", "does not support PMTUD on Site-to-site VPN", None)],
    [ev(TGWQ, "Transit gateways does not support PMTUD on Site-to-site VPN, Direct Connect, and Peering attachments.")],
    scope="Site-to-Site VPN, Direct Connect and peering attachments", rel="reference"))

MP = "docs/vpc/latest/tgw/metering-policy"
f1.append(F("transit-gateway-metering-policy-max-50-entries", T, "limit",
    "A flexible cost allocation metering policy can contain up to 50 entries, evaluated in order from lowest to highest rule number.",
    "How many entries can a transit gateway metering policy contain?",
    [("max", "up to 50 entries", "up to fifty entries")],
    [ev(MP, "A policy can contain up to 50 entries, evaluated in order from lowest to highest rule number.")],
    scope="per metering policy", dom="max", adj=False, cond="the page does not say whether the maximum can be raised",
    rel="reference", vol="frequently-changing",
    items=["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"]))

f1.append(F("transit-gateway-metering-policy-max-10-middlebox", T, "limit",
    "A metering policy can name a maximum of 10 middlebox attachments.",
    "How many middlebox attachments can a transit gateway metering policy name?",
    [("max", "maximum of 10 middlebox attachments", "a maximum of ten middlebox attachments")],
    [ev(MP, "You can specify a maximum of 10 middlebox attachments.")],
    scope="per transit gateway metering policy", dom="max", adj=False, cond="the page does not say whether the maximum can be raised",
    rel="reference", vol="frequently-changing",
    items=["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"]))

f1.append(F("transit-gateway-metering-policy-one-per-gateway", T, "limit",
    "Each transit gateway can have only one metering policy.",
    "How many metering policies can one transit gateway have?",
    [("max", "only one metering policy", "only one metering policy")],
    [ev(MP, "Each transit gateway can have only one metering policy.")],
    scope="per transit gateway", dom="max", adj=False, rel="reference", vol="frequently-changing",
    items=["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"]))

ES = "docs/vpc/latest/tgw/tgw-encryption-support"
f1.append(F("transit-gateway-encryption-enabling-up-to-14-days", T, "limit",
    "While a transit gateway is in the enabling encryption state, the process can take up to 14 days to complete.",
    "How long can enabling encryption support on a transit gateway take?",
    [("max", "up to 14 days", "up to fourteen days")],
    [ev(ES, "**enabling** - The transit gateway is in the process of enabling encryption support. This process can take up to 14 days to complete.")],
    scope="per transit gateway, enabling encryption support", dom="max", adj=False, rel="reference", vol="frequently-changing",
    items=["docs/vpc/latest/tgw/doc-history#13"]))

f1.append(F("transit-gateway-encryption-only-on-existing-gateway", T, "restriction",
    "You can add encryption support only to an existing transit gateway, not while you are creating one.",
    "Can you enable encryption support while creating a transit gateway?",
    [("rule", "encryption support to an existing transit gateway", None)],
    [ev(ES, "You can only add encryption support to an existing transit gateway and not while you're creating one.")],
    scope="per transit gateway", rel="extended", vol="frequently-changing",
    items=["docs/vpc/latest/tgw/doc-history#13"]))

CT = "docs/vpc/latest/tgw/create-tgw"
f1.append(F("transit-gateway-default-route-table-created", T, "default",
    "When you create a transit gateway, AWS creates a default transit gateway route table and uses it as the default association route table and the default propagation route table.",
    "What route table does a new transit gateway get by default?",
    [("default", "default propagation route table", None)],
    [ev(CT, "When you create a transit gateway, we create a default transit gateway route table and use it as the default association route table and the default propagation route table.")],
    scope="per transit gateway", dom="default", adj=False, cond="you can choose not to create the default route table and create one later",
    rel="core"))

f1.append(F("transit-gateway-amazon-side-asn-16bit-range", T, "limit",
    "A private Amazon side ASN for a transit gateway can be from 64512 to 65534 for 16-bit ASNs.",
    "What is the range of a 16-bit private ASN for the Amazon side of a transit gateway?",
    [("range", "64512 to 65534", "sixty-four five twelve to sixty-five five thirty-four")],
    [ev(CT, "For **Amazon side Autonomous System Number (ASN)**, either leave the default value to use the default ASN or enter the private ASN for your transit gateway. This should be the ASN for the AWS side of a Border Gateway Protocol (BGP) session."),
     ev(CT, "The range is 64512 to 65534 for 16-bit ASNs.")],
    scope="Amazon side ASN of a transit gateway, 16-bit", dom="fixed", adj=False, rel="reference"))

f1.append(F("transit-gateway-amazon-side-asn-32bit-range", T, "limit",
    "A private Amazon side ASN for a transit gateway can be from 4200000000 to 4294967294 for 32-bit ASNs.",
    "What is the range of a 32-bit private ASN for the Amazon side of a transit gateway?",
    [("range", "4200000000 to 4294967294", "four point two billion to four point two nine four billion")],
    [ev(CT, "For **Amazon side Autonomous System Number (ASN)**, either leave the default value to use the default ASN or enter the private ASN for your transit gateway. This should be the ASN for the AWS side of a Border Gateway Protocol (BGP) session."),
     ev(CT, "The range is 4200000000 to 4294967294 for 32-bit ASNs.")],
    scope="Amazon side ASN of a transit gateway, 32-bit", dom="fixed", adj=False, rel="reference"))

f1.append(F("transit-gateway-cidr-block-size", T, "limit",
    "A transit gateway CIDR block can be a /24 block or larger for IPv4, or a /64 block or larger for IPv6.",
    "What CIDR block sizes can you give a transit gateway?",
    [("ipv4", "/24 CIDR block or larger", "a slash twenty-four block or larger"),
     ("ipv6", "/64 CIDR block or larger", "a slash sixty-four block or larger")],
    [ev(CT, "You can specify a size /24 CIDR block or larger (for example, /23 or /22) for IPv4, or a size /64 CIDR block or larger (for example, /63 or /62) for IPv6.")],
    scope="transit gateway CIDR blocks", dom="min", adj=False, rel="reference"))

VA = "docs/vpc/latest/tgw/tgw-vpc-attachments"
f1.append(F("transit-gateway-vpc-attachment-visible-2-hours", T, "limit",
    "A failed or deleted VPC attachment remains visible for 2 hours and then is no longer visible.",
    "How long does a failed or deleted transit gateway VPC attachment stay visible?",
    [("duration", "remains visible for 2 hours", "stays visible for two hours")],
    [ev(VA, "The failed VPC attachment remains visible for 2 hours, and then is no longer visible."),
     ev(VA, "The VPC attachment remains visible for 2 hours, and then is no longer visible.")],
    scope="per VPC attachment in the failed or deleted state", dom="fixed", adj=False, rel="reference"))

write("facts-numbers-01.json", f1)
write("facts-numbers-01b.json", [x for x in f1 if "asn" in x["id"]])
