import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
PEER = "docs/vpc/latest/peering/vpc-peering-connection-quotas"
TGWQ = "docs/vpc/latest/tgw/transit-gateway-quotas"
EPQ = "docs/vpc/latest/privatelink/vpc-limits-endpoints"
CONTACT = "the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance"


def mk(i, service, kind, claim, question, values, scope, dom, adj, cond, rel, bullet, tier0=False, vol="stable", note=None):
    return {
        "id": i, "service": service, "home_chapter": "11", "kind": kind, "claim": claim, "question": question,
        "values": [{"key": k, "display": d, "spoken": s} for k, d, s in values],
        "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
        "source_tier": 1, "hard": True, "tier0": tier0, "volatility": vol, "changed": None,
        "exam_relevance": rel, "bullets": [bullet], "note": note,
    }


T = "transit-gateway"
E = "vpc-endpoints"
K = "4.4.K6"
specs = []  # (source, table, row, fact)

specs.append((PEER, 0, 1, mk(
    "vpc-peering-quota-outstanding-requests", "vpc-peering", "quota",
    "A default of 25 outstanding VPC peering connection requests is allowed, and the quota is adjustable.",
    "How many outstanding VPC peering connection requests are allowed by default?",
    [("default", "25", "twenty-five outstanding requests")],
    "outstanding VPC peering connection requests", "default", True, "", "reference", K)))
specs.append((PEER, 0, 2, mk(
    "vpc-peering-quota-request-expiry", "vpc-peering", "quota",
    "An unaccepted VPC peering connection request expires after 1 week (168 hours), and this expiry time is not adjustable.",
    "How long does an unaccepted VPC peering connection request stay open?",
    [("expiry", "1 week (168 hours)", "one week, which is a hundred and sixty-eight hours")],
    "expiry time of an unaccepted VPC peering connection request", "fixed", False, "", "extended", K)))

# Transit gateway: quotas
specs.append((TGWQ, 0, 0, mk(
    "transit-gateway-quota-gateways-per-account", T, "quota",
    "By default an account can have 5 transit gateways, and the quota is adjustable.",
    "How many transit gateways can an account have by default?",
    [("default", "5", "five transit gateways per account")],
    "transit gateways per account", "default", True, "", "extended", K, tier0=True)))
specs.append((TGWQ, 0, 1, mk(
    "transit-gateway-quota-cidr-blocks-per-gateway", T, "quota",
    "A transit gateway can have 5 CIDR blocks, and this quota is not adjustable.",
    "How many CIDR blocks can a transit gateway have?",
    [("default", "5", "five CIDR blocks per transit gateway")],
    "CIDR blocks per transit gateway", "fixed", False, "the CIDR blocks are used by Connect attachments and Connect peers", "reference", K)))
specs.append((TGWQ, 1, 0, mk(
    "transit-gateway-quota-route-tables-per-gateway", T, "quota",
    "A transit gateway has a default of 20 route tables, and the quota is adjustable.",
    "How many route tables can one transit gateway have by default?",
    [("default", "20", "twenty route tables per transit gateway")],
    "transit gateway route tables per transit gateway", "default", True, "", "extended", K)))
specs.append((TGWQ, 1, 3, mk(
    "transit-gateway-quota-total-routes", T, "quota",
    "The default for total combined routes (dynamic and static) across all route tables of a single transit gateway is 10,000.",
    "How many routes can one transit gateway hold across all its route tables?",
    [("default", "10,000", "ten thousand routes in total")],
    "total combined routes across all route tables of one transit gateway", "default", False,
    "no Service Quotas link: " + CONTACT, "extended", K)))
specs.append((TGWQ, 1, 6, mk(
    "transit-gateway-quota-static-routes-per-prefix-attachment", T, "quota",
    "A transit gateway route table can hold 1 static route for a prefix to a single attachment, and this quota is not adjustable.",
    "How many static routes for one prefix can point to a single attachment?",
    [("default", "1", "one static route for a prefix to a single attachment")],
    "static routes for a prefix to a single attachment", "fixed", False, "", "reference", K)))
specs.append((TGWQ, 2, 0, mk(
    "transit-gateway-quota-attachments-per-gateway", T, "quota",
    "A transit gateway has a default of 5,000 attachments, and the quota is adjustable.",
    "How many attachments can one transit gateway have by default?",
    [("default", "5,000", "five thousand attachments per transit gateway")],
    "attachments per transit gateway", "default", True, "", "core", K, tier0=True)))
specs.append((TGWQ, 2, 1, mk(
    "transit-gateway-quota-gateways-per-vpc", T, "quota",
    "A VPC can be attached to 5 transit gateways, and this quota is not adjustable.",
    "How many transit gateways can one VPC attach to?",
    [("default", "5", "five transit gateways per VPC")],
    "transit gateways per VPC", "fixed", False, "", "extended", K)))
specs.append((TGWQ, 2, 2, mk(
    "transit-gateway-quota-peering-attachments", T, "quota",
    "A transit gateway has a default of 50 peering attachments, and the quota is adjustable.",
    "How many peering attachments can one transit gateway have by default?",
    [("default", "50", "fifty peering attachments per transit gateway")],
    "peering attachments per transit gateway", "default", True, "", "extended", K)))
specs.append((TGWQ, 2, 3, mk(
    "transit-gateway-quota-pending-peering-attachments", T, "quota",
    "A transit gateway has a default of 10 pending peering attachments, and the quota is adjustable.",
    "How many pending peering attachments can one transit gateway have by default?",
    [("default", "10", "ten pending peering attachments")],
    "pending peering attachments per transit gateway", "default", True, "", "reference", K)))
specs.append((TGWQ, 2, 4, mk(
    "transit-gateway-quota-peering-between-two-gateways", T, "quota",
    "Two transit gateways, or one transit gateway and a Cloud WAN core network edge (CNE), can have 1 peering attachment between them, and this quota is not adjustable.",
    "How many peering attachments can exist between two transit gateways?",
    [("max", "1", "one peering attachment between two transit gateways")],
    "peering attachments between two transit gateways or between one transit gateway and a Cloud WAN core network edge (CNE)", "fixed", False, "", "extended", K)))
specs.append((TGWQ, 2, 5, mk(
    "transit-gateway-quota-connect-peers-per-attachment", T, "quota",
    "A Connect attachment can have 4 Connect peers (GRE tunnels), and this quota is not adjustable.",
    "How many Connect peers can one Connect attachment have?",
    [("default", "4", "four Connect peers per Connect attachment")],
    "Connect peers (GRE tunnels) per Connect attachment", "fixed", False, "", "reference", K)))
specs.append((TGWQ, 3, 0, mk(
    "transit-gateway-quota-vpc-attachment-bandwidth", T, "quota",
    "Bandwidth per VPC attachment per Availability Zone is up to 100 Gbps each direction (100 Gbps ingress and 100 Gbps egress).",
    "How much bandwidth does a transit gateway VPC attachment get per Availability Zone?",
    [("max", "up to 100 Gbps", "up to one hundred gigabits per second in each direction")],
    "per VPC attachment, per Availability Zone", "max", False, CONTACT, "core", K, tier0=True,
    vol="frequently-changing", note="The history row of 2023-08-14 says bandwidth limits were added; no page states an older 50 Gbps value.")))
specs.append((TGWQ, 3, 1, mk(
    "transit-gateway-quota-vpc-attachment-pps", T, "quota",
    "Packets per second per transit gateway VPC attachment per Availability Zone is up to 7,500,000.",
    "How many packets per second can a transit gateway VPC attachment carry per Availability Zone?",
    [("max", "up to 7,500,000", "up to seven and a half million packets per second")],
    "per transit gateway VPC attachment, per Availability Zone", "max", False, CONTACT, "reference", K, vol="frequently-changing")))
specs.append((TGWQ, 3, 2, mk(
    "transit-gateway-quota-dx-peering-bandwidth", T, "quota",
    "Bandwidth for a Direct Connect gateway or peered transit gateway connection per available Availability Zone in the Region is up to 100 Gbps each direction (100 Gbps ingress and 100 Gbps egress).",
    "How much bandwidth does a Direct Connect gateway or peered transit gateway connection get per Availability Zone?",
    [("max", "up to 100 Gbps", "up to one hundred gigabits per second in each direction")],
    "per Direct Connect gateway or peered transit gateway connection, per available Availability Zone in the Region", "max", False, CONTACT, "extended", K, vol="frequently-changing")))
specs.append((TGWQ, 3, 3, mk(
    "transit-gateway-quota-dx-peering-pps", T, "quota",
    "Packets per second per transit gateway attachment (Direct Connect and peering attachments) per available Availability Zone in the Region is up to 7,500,000.",
    "How many packets per second can a Direct Connect or peering attachment carry per Availability Zone?",
    [("max", "up to 7,500,000", "up to seven and a half million packets per second")],
    "per Direct Connect or peering attachment, per available Availability Zone in the Region", "max", False, CONTACT, "reference", K, vol="frequently-changing")))
specs.append((TGWQ, 3, 4, mk(
    "transit-gateway-quota-connect-peer-bandwidth", T, "quota",
    "Maximum bandwidth per Connect peer (GRE tunnel) per Connect attachment is up to 5 Gbps, and this quota is not adjustable.",
    "How much bandwidth can one Connect peer (GRE tunnel) carry?",
    [("max", "up to 5 Gbps", "up to five gigabits per second")],
    "per Connect peer (GRE tunnel), per Connect attachment", "max", False, "", "extended", K)))
specs.append((TGWQ, 3, 5, mk(
    "transit-gateway-quota-connect-peer-pps", T, "quota",
    "Maximum packets per second per Connect peer is up to 300,000, and this quota is not adjustable.",
    "How many packets per second can one Connect peer carry?",
    [("max", "up to 300,000", "up to three hundred thousand packets per second")],
    "per Connect peer", "max", False, "", "reference", K)))
specs.append((TGWQ, 4, 0, mk(
    "transit-gateway-quota-dx-gateways-per-gateway", T, "quota",
    "A transit gateway can have 20 Direct Connect gateways, and this quota is not adjustable.",
    "How many Direct Connect gateways can one transit gateway have?",
    [("default", "20", "twenty Direct Connect gateways per transit gateway")],
    "Direct Connect gateways per transit gateway", "fixed", False, "", "reference", K)))
specs.append((TGWQ, 4, 1, mk(
    "transit-gateway-quota-gateways-per-dx-gateway", T, "quota",
    "A Direct Connect gateway can have 6 transit gateways, and this quota is not adjustable.",
    "How many transit gateways can one Direct Connect gateway have?",
    [("default", "6", "six transit gateways per Direct Connect gateway")],
    "transit gateways per Direct Connect gateway", "fixed", False, "", "reference", K)))

# VPC endpoints and PrivateLink quotas
EK = "1.2.K2"
specs.append((EPQ, 0, 0, mk(
    "vpc-endpoints-quota-interface-gwlb-per-vpc", E, "quota",
    "A VPC has a default of 50 interface and Gateway Load Balancer endpoints, and the quota is adjustable; it is one combined quota for both endpoint types.",
    "How many interface endpoints can one VPC have by default?",
    [("default", "50", "fifty interface and Gateway Load Balancer endpoints per VPC")],
    "interface and Gateway Load Balancer endpoints per VPC", "default", True, "combined quota for interface endpoints and Gateway Load Balancer endpoints", "extended", EK, tier0=True)))
specs.append((EPQ, 0, 1, mk(
    "vpc-endpoints-quota-gateway-endpoints", E, "quota",
    "A Region has a default of 20 gateway VPC endpoints, the quota is adjustable, and you can create up to 255 gateway endpoints per VPC.",
    "How many gateway VPC endpoints can you have per Region and per VPC?",
    [("region", "20", "twenty gateway endpoints per Region"), ("vpc", "up to 255 gateway endpoints per VPC", "up to two hundred fifty-five gateway endpoints per VPC")],
    "gateway VPC endpoints per Region", "default", True, "up to 255 gateway endpoints per VPC", "extended", EK)))
specs.append((EPQ, 0, 2, mk(
    "vpc-endpoints-quota-resource-endpoints-per-vpc", E, "quota",
    "A VPC has a default of 200 resource VPC endpoints, and the quota is adjustable.",
    "How many resource VPC endpoints can one VPC have by default?",
    [("default", "200", "two hundred resource endpoints per VPC")],
    "resource VPC endpoints per VPC", "default", True, "", "reference", EK)))
specs.append((EPQ, 0, 3, mk(
    "vpc-endpoints-quota-service-network-endpoints-per-vpc", E, "quota",
    "A VPC has a default of 50 service network VPC endpoints, and the quota is adjustable.",
    "How many service network VPC endpoints can one VPC have by default?",
    [("default", "50", "fifty service network endpoints per VPC")],
    "service network VPC endpoints per VPC", "default", True, "", "reference", EK)))
specs.append((EPQ, 0, 4, mk(
    "vpc-endpoints-quota-policy-characters", E, "quota",
    "A VPC endpoint policy can hold 20,480 characters including white space, and this quota is not adjustable.",
    "What is the maximum size of a VPC endpoint policy?",
    [("max", "20,480", "twenty thousand four hundred eighty characters")],
    "characters per VPC endpoint policy", "max", False, "the maximum size of a VPC endpoint policy, including white space", "extended", EK)))

cmds = []
for n, (src, tab, row, fact) in enumerate(specs):
    fn = f"ad{n:02d}.json"
    with open(os.path.join(OUT, fn), "w") as f:
        json.dump(fact, f, indent=1)
    cmds.append(f"python3 aws-saa-book/tools/saa.py facts adopt --source {src} --table {tab} --row {row} --file aws-saa-book/_build/work/11-vpc-connectivity/mnc/{fn} --by mine-11-numbers+changes")
with open(os.path.join(OUT, "adopt-commands.txt"), "w") as f:
    f.write("\n".join(cmds) + "\n")
print(len(cmds))
