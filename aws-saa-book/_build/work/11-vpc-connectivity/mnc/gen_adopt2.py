import json, os
OUT = os.path.dirname(os.path.abspath(__file__))
TH = "docs/vpc/latest/tgw/doc-history"
PH = "docs/vpc/latest/privatelink/doc-history"
GH = "docs/vpc/latest/peering/doc-history"


def mk(i, service, claim, question, values, items, note=None, rel="extended", bullet="4.4.K6"):
    return {
        "id": i, "service": service, "home_chapter": "11", "kind": "change", "claim": claim, "question": question,
        "values": [{"key": k, "display": d, **({"spoken": s} if s else {})} for k, d, s in values],
        "qualifiers": {"scope": "", "default_or_max": "", "adjustable": False, "condition": ""},
        "source_tier": 1, "hard": True, "tier0": False, "volatility": "stable", "changed": None,
        "exam_relevance": rel, "bullets": [bullet], "note": note, "change_items": items,
    }


T = "transit-gateway"
specs = []
specs.append((TH, 0, 0, mk("transit-gateway-change-pbr-2026", T,
    "The Transit Gateway document history lists Policy-Based Routing for transit gateways on July 28, 2026: policy tables forward traffic across a transit gateway based on packet attributes such as source and destination IP addresses, ports, and protocol.",
    "When did Policy-Based Routing arrive for transit gateways?",
    [("date", "July 28, 2026", "late July 2026")],
    ["docs/vpc/latest/tgw/doc-history#10", "whats-new-v2#launch-pahjucn5xzkrlgqypk2nik"],
    note="NOT EXAMINABLE YET: GA after 2026-07-15 (What's New of 2026-07-30). Label as not examinable yet; never use it as a current-truth value for routing questions.",
    rel="reference")))
specs.append((TH, 1, 0, mk("transit-gateway-change-client-vpn-attachments-2026", T,
    "The Transit Gateway document history lists Client VPN attachments on April 20, 2026: you create a Client VPN attachment to connect a transit gateway to a Client VPN endpoint.",
    "When did Client VPN attachments arrive for transit gateways?",
    [("date", "April 20, 2026", "April 2026")],
    ["docs/vpc/latest/tgw/doc-history#11", "whats-new-v2#launch-w3r3xlmgyitelkwytry5g8"],
    note="Examinable (before 2026-07-15). The What's New post is dated 2026-04-23.", rel="extended", bullet="3.4.K4")))
specs.append((TH, 2, 0, mk("transit-gateway-change-flexible-cost-allocation-history-2025", T,
    "The Transit Gateway document history lists Flexible Cost Allocation on November 20, 2025: you configure flexible cost allocation policies to control how data processing and transfer costs are allocated across your organization.",
    "When was Flexible Cost Allocation added to the Transit Gateway guide?",
    [("date", "November 20, 2025", "November 2025")],
    ["docs/vpc/latest/tgw/doc-history#12", "whats-new-v2#launch-6xhxsc88takkvaeqaq3rk4"],
    note="The What's New post is dated 2025-11-21. Current truth: transit-gateway-fca-allocation-options-default-source.", rel="extended", bullet="4.4.S3")))
specs.append((TH, 3, 0, mk("transit-gateway-change-encryption-support-2025", T,
    "The Transit Gateway document history lists Encryption Support for transit gateways on November 20, 2025: managing Encryption Support on transit gateways to enforce encryption-in-transit for all traffic.",
    "When did Encryption Support arrive for transit gateways?",
    [("date", "November 20, 2025", "November 2025")],
    ["docs/vpc/latest/tgw/doc-history#13"],
    note="Current truth: transit-gateway-encryption-* facts and vpc-encryption-controls-tgw-charges-attached-vpcs.", rel="extended", bullet="4.4.K6")))
specs.append((TH, 4, 0, mk("transit-gateway-change-network-function-attachments-2025", T,
    "The Transit Gateway document history lists Network function attachments on June 16, 2025: you create a network function attachment to connect a transit gateway directly to AWS Network Firewall.",
    "When did network function attachments arrive for transit gateways?",
    [("date", "June 16, 2025", "June 2025")],
    ["docs/vpc/latest/tgw/doc-history#14", "whats-new-v2#v1789696919"],
    note="Current truth: transit-gateway-network-function-* facts and network-firewall-tgw-appliance-mode-always.", rel="extended", bullet="4.4.K6")))
specs.append((TH, 5, 0, mk("transit-gateway-change-security-group-referencing-2024", T,
    "The Transit Gateway document history lists Security group referencing support on September 25, 2024: you can now reference a security group across VPCs attached to a transit gateway.",
    "When did security group referencing across a transit gateway arrive?",
    [("date", "September 25, 2024", "September 2024")],
    ["docs/vpc/latest/tgw/doc-history#15", "whats-new-v2#p105573989"],
    note="Current truth: transit-gateway-sg-referencing-* facts and vpc-sg-reference-across-peering-and-tgw.", rel="extended", bullet="4.4.K6")))
specs.append((TH, 6, 0, mk("transit-gateway-change-bandwidth-limits-added-2023", T,
    "The Transit Gateway document history lists AWS Transit Gateway Quotas on August 14, 2023 with the description that bandwidth limits were added; the row gives no earlier bandwidth value.",
    "What did the August 14, 2023 Transit Gateway quotas history row change?",
    [("date", "August 14, 2023", "August 2023"), ("what", "Bandwidth limits were added", None)],
    ["docs/vpc/latest/tgw/doc-history#16"],
    note="FRESHNESS.md hypothesis 'bandwidth per VPC attachment rose from 50 Gbps to up to 100 Gbps' is NOT supported: the history row says bandwidth limits were added, and no saved AWS page states a 50 Gbps value. Current value: transit-gateway-quota-vpc-attachment-bandwidth.",
    rel="extended", bullet="4.4.K6")))
specs.append((TH, 7, 0, mk("transit-gateway-change-flow-logs-2022", T,
    "The Transit Gateway document history lists AWS Transit Gateway Flow Logs on July 14, 2022: transit gateways support Transit Gateway Flow Logs, which let you monitor and log network traffic between transit gateways.",
    "When did Transit Gateway Flow Logs arrive?",
    [("date", "July 14, 2022", "July 2022")],
    ["docs/vpc/latest/tgw/doc-history#17", "whats-new-v2#about-aws-whats-new-2022-07-amazon-vpc-flow-logs-transit-gateway-improved-visibility-monitoring"],
    rel="reference", bullet="4.4.K6")))
specs.append((TH, 8, 0, mk("transit-gateway-change-policy-tables-2022", T,
    "The Transit Gateway document history lists Transit gateway policy tables on July 13, 2022, described as policy tables that set up dynamic routing for transit gateways, automatically exchanging routing and reachability information with peered transit gateway types.",
    "What did the July 13, 2022 Transit gateway policy tables history row describe?",
    [("date", "July 13, 2022", "July 2022")],
    ["docs/vpc/latest/tgw/doc-history#18"],
    note="The 2022 row describes policy tables for dynamic routing with peered transit gateways; the 2026 Policy-Based Routing row describes policy tables that forward traffic by packet attributes. Not examinable yet for the 2026 feature (GA after 2026-07-15).",
    rel="reference", bullet="4.4.K6")))

PL = "privatelink"
specs.append((PH, 0, 0, mk("privatelink-change-access-resources-and-service-networks-2024", PL,
    "The PrivateLink document history lists Access resources and service networks on December 1, 2024: AWS PrivateLink supports accessing resources and service networks across VPC and account boundaries.",
    "When did PrivateLink start supporting resource endpoints and service-network endpoints?",
    [("date", "December 1, 2024", "December 2024")],
    ["docs/vpc/latest/privatelink/doc-history#10", "whats-new-v2#launchmarketingintake-1355"],
    note="Current truth: privatelink-resource-endpoint-* facts.", rel="extended", bullet="3.4.K4")))
specs.append((PH, 1, 0, mk("privatelink-change-cross-region-access-2024", PL,
    "The PrivateLink document history lists Cross-Region access on November 26, 2024: a service provider can host a service in one Region and make it available in a set of AWS Regions, and a service consumer selects a service Region when creating an endpoint.",
    "When did PrivateLink endpoint services become available across Regions?",
    [("date", "November 26, 2024", "November 2024")],
    ["docs/vpc/latest/privatelink/doc-history#11", "whats-new-v2#p166216340"],
    note="Current truth: privatelink-cross-region-* facts. Related: 14 more Regions on 2024-12-19 and 6 more on 2025-03-18 are What's New items not saved in the corpus (robots.txt).",
    rel="extended", bullet="3.4.K4")))
specs.append((PH, 2, 0, mk("privatelink-change-designated-ip-addresses-2023", PL,
    "The PrivateLink document history lists Designated IP addresses on August 17, 2023: you can specify the IP addresses for your endpoint network interfaces when you create or modify your VPC endpoint.",
    "When could you start choosing the IP addresses of a VPC endpoint?",
    [("date", "August 17, 2023", "August 2023")],
    ["docs/vpc/latest/privatelink/doc-history#12", "whats-new-v2#about-aws-whats-new-2023-08-aws-privatelink-user-defined-ip-vpc-endpoints"],
    rel="reference", bullet="1.2.K2")))

PE = "vpc-peering"
specs.append((GH, 0, 0, mk("vpc-peering-change-newest-history-row-2020", PE,
    "The newest row in the VPC peering guide's document history is Tag on create, dated July 20, 2020: you can add tags when you create a VPC peering connection and route table.",
    "What is the newest entry in the VPC peering document history?",
    [("date", "July 20, 2020", "July 2020")],
    [],
    note="Hypothesis confirmed: the peering history has no row after July 20, 2020 and the change feed has 0 items since 2022-07-01. The writer may say 'unchanged since 2020' only as 'the document history shows no change since July 20, 2020'.",
    rel="reference", bullet="4.4.K6")))

cmds = []
for n, (src, row, tab, fact) in enumerate(specs):
    if not fact["change_items"]:
        del fact["change_items"]
    fn = f"ah{n:02d}.json"
    with open(os.path.join(OUT, fn), "w") as f:
        json.dump(fact, f, indent=1)
    cmds.append((n, src, tab, row, fn))
for c in cmds:
    print(*c)
