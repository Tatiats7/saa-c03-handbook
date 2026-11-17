"""register-11: builds the registrar patch files (reg-patch/<id>.json) and the plan reg-plan.json.

Read-only on the canon; the tool applies each patch with `facts amend`.
"""
import json, os, copy
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/11-vpc-connectivity/"
P = W + "reg-patch/"
if not os.path.isdir(P):
    os.mkdir(P)
facts = {}
for s in ["vpc-peering", "transit-gateway", "vpc-endpoints", "privatelink"]:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if line:
            f = json.loads(line)
            facts[f["id"]] = f

# old -> kept (duplicates: same claim, same or weaker quote)
SUPERSEDE = {
    "vpc-peering-whitepaper-full-mesh-4950-connections": "vpc-peering-wp-full-mesh-4950-connections",
    "vpc-peering-faq-guide-quota-active-per-vpc": "vpc-peering-quota-active-connections-per-vpc",
    "vpc-peering-faq-inter-region-all-commercial-regions": "vpc-peering-faq-inter-region",
    "vpc-peering-failed-connection-visible-2-hours": "vpc-peering-failed-state",
    "vpc-peering-whitepaper-same-az-transfer-free": "vpc-peering-wp-data-transfer-free-in-az",
    "vpc-peering-whitepaper-cross-az-standard-in-region-rate": "vpc-peering-wp-data-transfer-free-in-az",
    "vpc-peering-whitepaper-inter-region-standard-rate": "vpc-peering-wp-data-transfer-free-in-az",
    "vpc-peering-private-routing": "vpc-peering-def-private-ipv4-ipv6",
    "vpc-peering-migrate-to-tgw-mtu-mismatch": "transit-gateway-mtu-mismatch-peering-migration",
    "transit-gateway-client-vpn-attachment-created-on-association": "transit-gateway-client-vpn-attachment-automatic",
    "transit-gateway-client-vpn-attachment-needs-route-propagation": "transit-gateway-client-vpn-route-propagation-required",
    "transit-gateway-default-route-table-created": "transit-gateway-default-route-table-association-propagation",
    "transit-gateway-network-function-no-third-party-firewalls": "transit-gateway-network-function-static-routing-only",
    "transit-gateway-sg-referencing-not-across-peering": "transit-gateway-sg-reference-not-across-peering",
    "transit-gateway-sg-referencing-not-for-privatelink-endpoints": "transit-gateway-sg-reference-not-privatelink-endpoints",
    "transit-gateway-sg-referencing-needs-both-enabled": "transit-gateway-sg-reference-enable-both-sides",
    "transit-gateway-sg-referencing-inbound-rules-only": "transit-gateway-sg-reference-inbound-only",
    "transit-gateway-sg-referencing-no-additional-cost": "transit-gateway-sg-reference-inbound-only",
    "transit-gateway-best-practice-attachment-subnet-28": "transit-gateway-separate-small-subnet-per-attachment",
    "transit-gateway-blog-peered-gateways-charged-one-side": "transit-gateway-blog-peered-gateways-one-side-charged",
    "transit-gateway-guide-overlapping-cidr-not-routed": "transit-gateway-no-routing-identical-or-overlapping-cidr",
    "vpc-endpoints-faq-guide-quota-gateway-per-region": "vpc-endpoints-quota-gateway-endpoints",
    "vpc-endpoints-faq-guide-quota-interface-gwlb-per-vpc": "vpc-endpoints-quota-interface-gwlb-per-vpc",
    "privatelink-faq-endpoints-per-vpc-100": "vpc-endpoints-faq-100-endpoints-per-vpc",
    "privatelink-faq-billing-data-processing-and-partial-hour": "privatelink-faq-billing-data-processing-per-gb",
    "privatelink-faq-billing-interface-gwlb-hour-per-az": "privatelink-faq-billing-interface-gwlb-hourly-per-az",
    "privatelink-faq-billing-resource-endpoint-hour-any-az": "privatelink-faq-billing-resource-endpoint-hourly-any-az-count",
    "privatelink-faq-peering-limited-125-privatelink-unlimited": "privatelink-faq-peering-limit-125-vs-unlimited-scale",
    "privatelink-cross-region-endpoint-service-failover-within-region-only": "privatelink-cross-region-failover-not-managed",
    "privatelink-cross-region-endpoint-service-only-privatelink-services": "privatelink-cross-region-only-privatelink-services",
    "privatelink-cross-region-endpoint-service-concept": "privatelink-cross-region-host-and-consumer-select",
    "privatelink-wp-consumer-only-initiates-short": "privatelink-wp-unidirectional-overlapping-ips",
}

# number-free displays rewritten as verbatim phrases of at most 8 words from a quote
DISPLAYS = {
    "privatelink-faq-nlb-provider": {"consumer": "Elastic Network Interfaces (ENIs) with private IPs", "provider": "a Network Load Balancer (NLB) to front your service"},
    "privatelink-faq-over-direct-connect": {"dx": "endpoints in Amazon VPC over AWS Direct Connect"},
    "privatelink-faq-owners-register-nlb-or-share-resources": {"direct": "directly without using Network Load Balancers"},
    "privatelink-faq-what": {"aws-network": "all the network traffic within the AWS network", "no-public": "without using public IPs"},
    "privatelink-service-network-endpoint-concept": {"rule": "through a single VPC endpoint"},
    "transit-gateway-pbr-policy-table-or-route-table-not-both": {"rule": "a route table, but not both"},
    "vpc-endpoints-cmp-private-dns-public-name": {"private-dns": "the DNS name for its public endpoint"},
    "vpc-endpoints-faq-onprem-dx-dns-returns-private-ip": {"private-ip": "the private IP address within the associated VPC"},
    "vpc-peering-billing-usage-type-2025": {"what": "no changes to the pricing"},
    "vpc-peering-faq-bandwidth-same-as-vpc": {"bw": "no different than bandwidth between instances"},
    "vpc-peering-faq-cross-account-accept": {"accept": "the owner of the other VPC accepts"},
    "vpc-peering-faq-definition": {"what": "route traffic via private IP addresses"},
    "vpc-peering-faq-either-side-terminates": {"terminate": "can terminate the peering connection at any time"},
    "vpc-peering-faq-inter-region": {"regions": "VPCs in different regions"},
    "vpc-peering-faq-inter-region-encrypted": {"enc": "encrypted using modern AEAD", "keys": "key management is handled by AWS"},
    "vpc-peering-faq-inter-region-no-internet-failover": {"backbone": "traffic goes over the AWS backbone", "down": "will not be routed over the internet"},
    "vpc-peering-faq-inter-region-no-sg-reference": {"no": "Security groups cannot be referenced"},
    "vpc-peering-faq-intra-region-private": {"private": "remains private and isolated"},
    "vpc-peering-faq-no-internet-gateway": {"no": "do not require an Internet Gateway"},
    "vpc-peering-faq-no-single-point-of-failure": {"what": "neither a gateway nor a VPN connection", "spof": "no single point of failure for communication"},
    "transit-gateway-isolated-vpcs-scenario": {"v1": "each isolated router has a single route table"},
}
# displays added (key, display, spoken or None)
ADD_DISPLAYS = {
    "privatelink-faq-what": [("internet", "the traffic to traverse across the Internet", None)],
    "vpc-peering-faq-inter-region": [("commercial", "all commercial regions (excluding China)", None)],
    "transit-gateway-mtu-mismatch-peering-migration": [("fix", "Update both VPCs at the same time", None)],
    "transit-gateway-separate-small-subnet-per-attachment": [("size", "/28", None)],
    "vpc-peering-wp-data-transfer-free-in-az": [("v3", "standard inter-Region data transfer charges will apply", None)],
}

HARD_TRUE = [
    "vpc-peering-faq-bandwidth-same-as-vpc", "vpc-peering-faq-either-side-terminates", "vpc-peering-faq-inter-region-no-internet-failover",
    "vpc-peering-faq-intra-region-private", "vpc-peering-guide-existing-infrastructure-no-spof", "vpc-peering-one-to-one-relationship",
    "vpc-peering-route-pending-blackhole", "vpc-peering-sharing-wp-owner-shares-subnets-participants-manage-own",
    "vpc-peering-wp-full-bidirectional-point-to-point", "vpc-peering-blog-same-az-free-cross-az-charged",
    "vpc-peering-guide-pricing-no-creation-charge-free-in-az", "vpc-peering-sharing-wp-benefits-no-transfer-charge-same-az",
    "vpc-peering-wp-data-transfer-free-in-az",
    "transit-gateway-cross-az-internal-routing-no-extra-charge", "transit-gateway-faq-encryption-enforce-vpcs-end-to-end",
    "transit-gateway-faq-encryption-non-disruptive", "transit-gateway-faq-vpc-cidr-propagation-not-bgp",
    "transit-gateway-flow-logs-no-performance-impact", "transit-gateway-ha-by-design-single-per-region",
    "transit-gateway-hub-and-spoke-managed", "transit-gateway-hybrid-vpn-managed-endpoint-many-vpcs",
    "transit-gateway-isolated-vpcs-blocked-no-route", "transit-gateway-no-default-table-if-both-disabled",
    "transit-gateway-static-route-beats-propagated", "transit-gateway-mtu-mismatch-peering-migration",
    "transit-gateway-blog-cross-region-extra-transfer",
    "vpc-endpoints-faq-benefit-no-other-gateways", "vpc-endpoints-faq-resource-endpoint", "vpc-endpoints-interface-eni-ip-stable",
    "vpc-endpoints-interface-private-dns-no-app-change", "vpc-endpoints-public-endpoint-via-igw-stays-on-aws-network",
    "vpc-endpoints-resource-endpoint-no-load-balancer", "vpc-endpoints-wp-cross-region-endpoint-transfer-charges",
    "privatelink-faq-owners-register-nlb-or-share-resources", "privatelink-faq-path-stays-within-aws", "privatelink-faq-what",
    "privatelink-guide-private-connect-no-igw-nat", "privatelink-remove-permission-keeps-existing-connections",
    "privatelink-source-ip-is-load-balancer-node", "privatelink-wp-consumer-and-provider-may-overlap",
    "privatelink-faq-billing-data-processing-per-gb", "privatelink-faq-billing-partial-hour-full-hour",
    "privatelink-provider-nlb-billed-hourly-full-hour",
]

SCOPES = {
    "privatelink-faq-consumer-initiates-allowlisted-customers": "AWS PrivateLink connections (FAQ answer)",
    "privatelink-faq-peering-limit-125-vs-unlimited-scale": "VPC peering connections versus PrivateLink (FAQ wording)",
    "privatelink-faq-public-service-name-not-supported": "DNS names used to reach VPC endpoints (FAQ answer)",
    "privatelink-resource-endpoint-no-load-balancer-needed": "resource VPC endpoints",
    "transit-gateway-faq-connect-no-static-routes": "Transit Gateway Connect attachments",
    "transit-gateway-faq-dx-gateway-cross-account": "association of a transit gateway with a Direct Connect gateway",
    "transit-gateway-faq-dx-gateway-different-asn": "association of a transit gateway with a Direct Connect gateway",
    "transit-gateway-faq-identical-cidr-not-routed": "transit gateway VPC attachments (FAQ answer on identical CIDRs)",
    "transit-gateway-faq-multicast-attachment-types": "transit gateway multicast routing",
    "transit-gateway-faq-no-propagation-to-vpc-route-table": "route tables of VPCs attached to a transit gateway",
    "transit-gateway-faq-peering-attachment-static-routes": "transit gateway peering attachments",
    "vpc-endpoints-faq-gateway-endpoint-s3-ddb-route": "gateway VPC endpoints",
    "vpc-endpoints-faq-sdk-discovers-endpoints-latest": "latest versions of the AWS CLI and SDKs",
    "privatelink-faq-owners-register-nlb-or-share-resources": "sharing services and resources over AWS PrivateLink (FAQ answer)",
    "privatelink-faq-path-stays-within-aws": "path between a VPC endpoint and its service (FAQ answer)",
    "vpc-endpoints-faq-onprem-dx-dns-returns-private-ip": "VPC endpoint DNS records reached from on premises",
    "transit-gateway-faq-vpc-cidr-propagation-not-bgp": "VPC attachments of a transit gateway",
    "vpc-endpoints-faq-benefit-no-other-gateways": "VPC endpoints (FAQ answer)",
    "vpc-endpoints-faq-resource-endpoint": "resource VPC endpoints (FAQ answer)",
}

REL = {
    "vpc-peering-quota-active-connections-per-vpc": "core",
    "vpc-endpoints-quota-gateway-endpoints": "core",
    "vpc-endpoints-quota-interface-gwlb-per-vpc": "core",
    "vpc-endpoints-faq-100-endpoints-per-vpc": "extended",
}
NOTES = {
    "vpc-endpoints-faq-five-types": "register-11: the FAQ lists five types; tunnel endpoints (What's New 2026-09-18, not examinable yet) are a sixth type (privatelink-change-tunnel-endpoints-2026). Teach five for the exam.",
    "privatelink-faq-public-service-name-not-supported": "d11-111. Disagrees with the user guide: with private DNS, requests to the public service name use the interface endpoint (vpc-endpoints-cmp-private-dns-public-name). Teach the guide; quote this FAQ line only with that caveat.",
}

patches = {}
for i, m in DISPLAYS.items():
    f = facts[i]
    vals = copy.deepcopy(f["values"])
    for v in vals:
        if v["key"] in m:
            v["display"] = m[v["key"]]
    patches.setdefault(i, {})["values"] = vals
for i, adds in ADD_DISPLAYS.items():
    f = facts[i]
    vals = patches.get(i, {}).get("values") or copy.deepcopy(f["values"])
    for k, d, sp in adds:
        nv = {"key": k, "display": d}
        if sp:
            nv["spoken"] = sp
        vals.append(nv)
    patches.setdefault(i, {})["values"] = vals
for i in HARD_TRUE:
    if not facts[i]["hard"]:
        patches.setdefault(i, {})["hard"] = True
for i, sc in SCOPES.items():
    q = copy.deepcopy(facts[i].get("qualifiers") or {})
    if not (q.get("scope") or "").strip():
        q["scope"] = sc
        q.setdefault("default_or_max", "")
        q.setdefault("adjustable", False)
        q.setdefault("condition", "")
        patches.setdefault(i, {})["qualifiers"] = q
plan = {"supersede": SUPERSEDE, "amend": {}, "rel": REL, "notes": NOTES}
bad = [i for i in list(SUPERSEDE) + list(SUPERSEDE.values()) + list(patches) + list(REL) + list(NOTES) if i not in facts]
assert not bad, bad
for i in patches:
    assert i not in SUPERSEDE, i
for i, p in sorted(patches.items()):
    fn = P + i + ".json"
    json.dump(p, open(fn, "w"), indent=1)
    plan["amend"][i] = sorted(p.keys())
for i, r in REL.items():
    json.dump({"exam_relevance": r}, open(P + "rel-" + i + ".json", "w"))
for i, n in NOTES.items():
    json.dump({"note": n}, open(P + "note-" + i + ".json", "w"))
json.dump(plan, open(W + "reg-plan.json", "w"), indent=1)
# hard facts still without scope after the plan
miss = []
for i, f in facts.items():
    if f["status"] in ("rejected", "superseded") or i in SUPERSEDE:
        continue
    hard = patches.get(i, {}).get("hard", f["hard"])
    q = patches.get(i, {}).get("qualifiers", f.get("qualifiers") or {})
    if hard and f["kind"] != "change" and not (q.get("scope") or "").strip():
        miss.append(i)
print("supersede", len(SUPERSEDE), "amend", len(patches), "rel", len(REL), "notes", len(NOTES), "hard-without-scope", miss)
