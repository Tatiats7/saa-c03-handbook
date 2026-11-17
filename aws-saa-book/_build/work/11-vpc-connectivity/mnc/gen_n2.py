from mklib import *

E = "vpc-endpoints"
P = "vpc-peering"
EK = ("1.2.K2",)
f = []

f.append(F("vpc-endpoints-quotas-are-region-specific", E, "behavior",
    "Unless a PrivateLink quota is noted otherwise, the quota is Region-specific.",
    "Are VPC endpoint quotas counted per Region?",
    [("scope", "Region-specific", "counted per Region")],
    [ev(EPQ, "Unless otherwise noted, each quota is Region-specific.")],
    scope="AWS PrivateLink and VPC endpoint quotas", rel="reference", bullets=EK))

f.append(F("vpc-endpoints-bandwidth-10-gbps-per-az-scales-to-100", E, "default",
    "By default each VPC endpoint can support a bandwidth of up to 10 Gbps per Availability Zone, and it automatically scales up to 100 Gbps.",
    "How much bandwidth does a VPC endpoint support by default, and how far does it scale?",
    [("default", "up to 10 Gbps per Availability Zone", "up to ten gigabits per second per Availability Zone"),
     ("scale", "automatically scales up to 100 Gbps", "scales automatically up to one hundred gigabits per second")],
    [ev(EPQ, "By default, each VPC endpoint can support a bandwidth of up to 10 Gbps per Availability Zone, and automatically scales up to 100 Gbps."),
     ev(PLF, "Each VPC endpoint can support 10 Gbps continuous bandwidth per Availability Zone, by default, after which additional capacity is added automatically up to 100 Gbps.")],
    scope="per VPC endpoint, per Availability Zone", dom="default", adj=False, rel="core", bullets=EK, tier0=True))

f.append(F("vpc-endpoints-bandwidth-max-is-az-count-times-100", E, "limit",
    "The maximum bandwidth of a VPC endpoint, when the load is spread across all Availability Zones, is the number of Availability Zones multiplied by 100 Gbps; for higher throughput you contact AWS support.",
    "What is the maximum bandwidth of a VPC endpoint spread across all Availability Zones?",
    [("max", "the number of Availability Zones multiplied by 100 Gbps", "the number of zones times one hundred gigabits per second")],
    [ev(EPQ, "The maximum bandwidth for a VPC endpoint, when distributing the load across all Availability Zones, is the number of Availability Zones multiplied by 100 Gbps. If your application needs higher throughput, contact AWS support.")],
    scope="per VPC endpoint, across all Availability Zones", dom="max", adj=False,
    cond="if your application needs higher throughput, contact AWS support", rel="extended", bullets=EK))

f.append(F("vpc-endpoints-mtu-8500-larger-packets-dropped", E, "limit",
    "A VPC endpoint supports an MTU of 8500 bytes, and packets larger than 8500 bytes that arrive at the VPC endpoint are dropped.",
    "What MTU does a VPC endpoint support, and what happens to larger packets?",
    [("mtu", "MTU of 8500 bytes", "an M T U of eighty-five hundred bytes"),
     ("drop", "larger than 8500 bytes", None)],
    [ev(EPQ, "A VPC endpoint supports an MTU of 8500 bytes. Packets with a size larger than 8500 bytes that arrive at the VPC endpoint are dropped.")],
    scope="per VPC endpoint", dom="max", adj=False, rel="extended", bullets=EK))

f.append(F("vpc-endpoints-no-path-mtu-discovery", E, "restriction",
    "Path MTU Discovery (PMTUD) is not supported on VPC endpoints.",
    "Do VPC endpoints support Path MTU Discovery?",
    [("pmtud", "Path MTU Discovery (PMTUD) is not supported", None)],
    [ev(EPQ, "Path MTU Discovery (PMTUD) is not supported.")],
    scope="VPC endpoints", rel="reference", bullets=EK))

f.append(F("vpc-endpoints-mss-clamping-all-packets", E, "behavior",
    "VPC endpoints enforce Maximum Segment Size (MSS) clamping for all packets.",
    "Do VPC endpoints clamp the Maximum Segment Size?",
    [("mss", "Maximum Segment Size (MSS) clamping", None)],
    [ev(EPQ, "VPC endpoints enforce Maximum Segment Size (MSS) clamping for all packets.")],
    scope="all packets through a VPC endpoint", rel="reference", bullets=EK))

f.append(F("vpc-endpoints-faq-100-endpoints-per-vpc", E, "limit",
    "The AWS PrivateLink FAQ says you can create up to 100 VPC endpoints per VPC and should contact AWS if you need more; the quotas page instead lists a default of 50 interface and Gateway Load Balancer endpoints per VPC.",
    "How many VPC endpoints can I create in a single VPC, according to the FAQ?",
    [("faq", "up to 100 VPC endpoints per VPC", "up to one hundred VPC endpoints per VPC")],
    [ev(PLF, "You can create up to 100 VPC endpoints per VPC. If you need more than this, contact us and we will work on a solution with you.")],
    scope="per VPC (FAQ answer)", dom="max", adj=False,
    cond="the FAQ gives no adjustability; the quotas page vpc-endpoints-quota-interface-gwlb-per-vpc lists 50 by default and adjustable",
    rel="reference", bullets=EK,
    note="CONFLICT WITH QUOTAS PAGE: the FAQ says up to 100 endpoints per VPC; vpc-limits-endpoints lists a default of 50 interface and Gateway Load Balancer endpoints per VPC. Writers use the quotas page for the number and may mention that the FAQ differs."))

# ---- VPC peering (whitepaper)
WP = "docs/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-peering"
f.append(F("vpc-peering-whitepaper-same-az-transfer-free", P, "pricing-dimension",
    "All data transfer over a VPC peering connection that stays within an Availability Zone is free.",
    "Is data transfer over a VPC peering connection within one Availability Zone charged?",
    [("same-az", "stays within an Availability Zone is free", "free inside one Availability Zone")],
    [ev(WP, "All data transfer over a VPC peering connection that stays within an Availability Zone is free.")],
    scope="data transfer over a VPC peering connection inside one Availability Zone", rel="core", tier0=True))

f.append(F("vpc-peering-whitepaper-cross-az-standard-in-region-rate", P, "pricing-dimension",
    "All data transfer over a VPC peering connection that crosses Availability Zones is charged at the standard in-region data transfer rates.",
    "How is data transfer over a VPC peering connection across Availability Zones charged?",
    [("cross-az", "charged at the standard in-region data transfer rates", "charged at the normal in-Region rate")],
    [ev(WP, "All data transfer over a VPC peering connection that crosses Availability Zones is charged at the standard in-region data transfer rates.")],
    scope="data transfer over a VPC peering connection across Availability Zones in one Region", rel="extended"))

f.append(F("vpc-peering-whitepaper-inter-region-standard-rate", P, "pricing-dimension",
    "If VPCs are peered across Regions, standard inter-Region data transfer charges apply.",
    "How is data transfer over a VPC peering connection across Regions charged?",
    [("inter-region", "standard inter-Region data transfer charges will apply", "standard inter-Region transfer charges apply")],
    [ev(WP, "If the VPCs are peered across Regions, standard inter-Region data transfer charges will apply.")],
    scope="data transfer over an inter-Region VPC peering connection", rel="extended"))

f.append(F("vpc-peering-whitepaper-max-125-active-connections", P, "limit",
    "The multi-VPC whitepaper states a maximum limit of 125 active peering connections per VPC.",
    "What is the maximum number of active VPC peering connections per VPC?",
    [("max", "125 active peering connections per VPC", "one hundred twenty-five active peering connections per VPC")],
    [ev(WP, "There is a [maximum limit](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) of 125 active peering connections per VPC.")],
    scope="active peering connections per VPC", dom="max", adj=False,
    cond="the peering quotas page gives a default of 50 that can be raised up to 125", rel="extended"))

f.append(F("vpc-peering-whitepaper-full-mesh-4950-connections", P, "behavior",
    "A full mesh of peering between 100 VPCs takes 4,950 peering connections, which is n(n-1)/2 for n VPCs.",
    "How many peering connections does a full mesh of 100 VPCs need?",
    [("mesh", "4,950 peering connections", "four thousand nine hundred fifty peering connections")],
    [ev(WP, "For example, if you have 100 VPCs and you want to setup a full mesh peering between them, it will take 4,950 peering connections [`n(n-1)/2`] where `n` is the total number of VPCs.")],
    scope="full-mesh peering between 100 VPCs", rel="extended", hard=True))

write("facts-numbers-02.json", f)
