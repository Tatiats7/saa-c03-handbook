"""adjudicate-12: build one amend patch per disputed chapter 12 fact from the decisions below.

Reads the current facts, writes adj-12/<id>.json (full evidence list when evidence changes).
Read-only on data; writes only into the work folder.
"""
import copy, json, os
ROOT = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book"
W = ROOT + "/_build/work/12-hybrid-networking/"
OUT = W + "adj-12/"
os.makedirs(OUT, exist_ok=True)
SVCS = ["site-to-site-vpn", "direct-connect", "client-vpn"]
facts = {}
for s in SVCS:
    for line in open(ROOT + "/data/facts/%s.jsonl" % s):
        line = line.strip()
        if line:
            f = json.loads(line)
            facts[f["id"]] = f

def ev_of(f):
    out = []
    for e in f["evidence"]:
        d = {"source_id": e["source_id"], "url": e["url"], "quote": e["quote"], "table_header": e.get("table_header")}
        if e.get("heading"):
            d["heading"] = e["heading"]
        out.append(d)
    return out

def url_of(sid):
    for f in facts.values():
        for e in f["evidence"]:
            if e["source_id"] == sid:
                return e["url"]
    raise SystemExit("no url for " + sid)

def E(sid, quote, th=None, heading=None, url=None):
    d = {"source_id": sid, "url": url or url_of(sid), "quote": quote, "table_header": th}
    if heading:
        d["heading"] = heading
    return d

def posted(sid, date, heading):
    return E(sid, "Posted on: " + date, heading=heading)

VPC_VPN_URL = "https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"
VPN_LIMITS_URL = "https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-limits.html"
DX_HIST_URL = "https://docs.aws.amazon.com/directconnect/latest/UserGuide/AboutThisGuide.html"
VGW_DEF = "Virtual private gateway: A virtual private gateway is the VPN endpoint on the Amazon side of your Site-to-Site VPN connection that can be attached to a single VPC."

# each decision: dict with optional keys claim, add_ev (list), replace_ev (list, full), quals (dict merged), values (list), reason
D = {}
D["client-vpn-authorization-rule-group-limits-access-to-network"] = dict(
    claim="For each network you want to enable access to, you configure authorization rules with the Active Directory group or SAML-based IdP group that is allowed, and only users who belong to that group can access that network. If you do not use Active Directory or SAML-based federated authentication, or you want to open access to all users, you can specify a rule that grants access to all clients.",
    add_ev=[E("docs/vpn/latest/clientvpn-admin/client-authorization", "If you are not using Active Directory or SAML-based federated authentication, or you want to open access to all users, you can specify a rule that grants access to all clients.")],
    reason="entail partial: added the all-clients exception from the next sentence")
D["client-vpn-change-concurrent-connections-per-client"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/01/aws-client-vpn-concurrent-vpn-connections", "Jan 22, 2025", "AWS Client VPN announces support for concurrent VPN connections")],
    quals={"scope": "AWS-supplied Client VPN client"},
    reason="entail partial: added the Posted on line for the date; scope taken from the quote")
D["client-vpn-change-device-posture-2026-10"] = dict(
    add_ev=[E("www/about-aws/whats-new/2026/10/aws-client-vpn-device-posture", "This feature requires AWS VPN Client version 6.2.0 or later.")],
    reason="entail partial: added the quote for the version 6.2.0 condition")
D["client-vpn-change-ipv6-support"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/08/aws-client-vpn-connectivity-ipv6-resources", "Aug 26, 2025", "AWS Client VPN now supports connectivity to IPv6 resources")],
    reason="entail partial: added the Posted on line for the date")
D["client-vpn-change-transit-gateway-integration"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2026/04/aws-client-vpn-transit-gateway", "Apr 23, 2026", "AWS Client VPN now supports native AWS Transit Gateway integration")],
    reason="entail partial: added the Posted on line for the date")
D["client-vpn-connection-logging-cloudwatch-logs"] = dict(
    add_ev=[E("docs/vpn/latest/clientvpn-admin/connection-logging", "A connection log contains *connection log entries* that capture information about connection events, such as when a client (end user) connects, attempts to connect, or disconnects from your Client VPN endpoint.")],
    reason="entail partial: added the sentence that names the connection events")
D["client-vpn-cre-enforces-routes-on-connected-device"] = dict(
    quals={"scope": "Client VPN Client Route Enforcement"},
    reason="entail partial: removed the scope 'with AWS provided clients' that no quote states")
D["client-vpn-limit-baseline-bandwidth-50-mbps"] = dict(
    add_ev=[E("docs/vpn/latest/clientvpn-admin/what-is-best-practices", "If you are hitting the maximum bandwidth limit, you can request an increase through AWS Support.")],
    reason="entail partial: added the quote for the increase through AWS Support")
D["client-vpn-quota-authorization-rules-per-endpoint"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/03/aws-client-vpn-authorization-rules-route-quotas", "Mar 18, 2025", "AWS Client VPN increases authorization rules and route quotas")],
    reason="entail partial: added the Posted on line for March 2025")
D["client-vpn-quota-groups-per-user"] = dict(
    add_ev=[E("docs/vpn/latest/clientvpn-admin/limits", "When you configure users and groups for Active Directory or a SAML-based IdP, the following quotas apply:")],
    reason="entail partial: added the lead-in sentence that carries the Active Directory or SAML scope")
D["client-vpn-restriction-tgw-no-security-group-authorization"] = dict(
    add_ev=[E("docs/vpn/latest/clientvpn-admin/cvpn-tgw", "Security group-based authorization is not supported for Transit Gateway-associated Client VPN endpoints. You must use network-based authorization rules to control client access.")],
    reason="entail partial: added the Important note that requires network-based authorization rules")
D["direct-connect-change-400g-dedicated"] = dict(
    quals={"scope": "Direct Connect connections"},
    reason="entail partial: scope narrowed to what the history row says (400G connections)")
D["direct-connect-change-prefix-controls"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2026/08/aws-direct-connect-new-prefix-controls", "Aug 20, 2026", "AWS Direct Connect introduces inbound prefix controls and higher prefix scale")],
    reason="entail partial: added the Posted on line for the date")
D["direct-connect-design-dxgw-with-tgw-multi-region-public-vif-for-s3"] = dict(
    claim="In the Direct Connect gateway with transit gateways design for multiple Regions, a Direct Connect public virtual interface is used to access AWS public resources such as Amazon S3 directly over the Direct Connect connections, and the design scales up to thousands of VPCs per AWS Transit Gateway over a single BGP session.",
    reason="entail partial: claim keeps the 'per AWS Transit Gateway' scope of the quote")
f = facts["direct-connect-dxgw-no-direct-traffic-between-attached-vifs"]
ev = ev_of(f)
ev[2]["quote"] = "A Direct Connect gateway supports communication between attached private virtual interfaces and associated virtual private gateways only, and may enable a virtual private gateway to another private gateway. The following traffic flows are not supported:"
D["direct-connect-dxgw-no-direct-traffic-between-attached-vifs"] = dict(
    claim="A Direct Connect gateway supports communication between attached private virtual interfaces and associated virtual private gateways only, and may enable a virtual private gateway to another private gateway. Traffic flows that are not supported include direct communication between the virtual interfaces attached to a single Direct Connect gateway, and between those virtual interfaces and a VPN connection on a virtual private gateway associated with the same Direct Connect gateway.",
    replace_ev=ev,
    reason="entail partial: quote 3 now carries the 'not supported' lead-in; claim keeps the caveat and drops the on-premises inference")
D["direct-connect-faq-cloudfront-origin-needs-public-vif"] = dict(
    claim="If you use Amazon CloudFront with an origin in your own data center, you can use Direct Connect to transfer the objects stored there. You must have a Direct Connect public VIF, you must import all Anycast routes if you filter route imports, and you must advertise your custom origin's prefix to AWS.",
    replace_ev=[E("www/directconnect/faqs", "Yes, if you are using Amazon CloudFront and your origin is in your own data center, you can use AWS Direct Connect to transfer the objects stored in your own data center. You must have a Direct Connect Public VIF and if you are filtering your route imports, you must ensure you import all Anycast routes. You also must advertise your custom origins prefix to AWS.")],
    reason="entail partial: quote widened to the whole FAQ answer, which names CloudFront and the origin")
D["direct-connect-faq-dxgw-share-private-vif-up-to-20-vpcs"] = dict(
    add_ev=[E("www/directconnect/faqs", "An AWS Direct Connect gateway performs several functions:")],
    reason="entail partial: added the list lead-in that scopes the 20 VPCs to a Direct Connect gateway")
D["direct-connect-faq-two-charges-port-hours-data-transfer"] = dict(
    claim="The Direct Connect FAQ says AWS Direct Connect has two separate charges, port hours and data transfer; pricing is per port-hour consumed for each port type, partial port hours are billed as full hours, and the account that owns the port is charged the port-hour charges. Since September 15, 2026 Direct Connect also supports flat-rate billing, a fixed-price billing mode for dedicated connections that you set per connection.",
    add_ev=[E("docs/directconnect/latest/UserGuide/AboutThisGuide", "| [Flat-rate billing for dedicated connections](#AboutThisGuide) | Direct Connect now supports flat-rate billing, a fixed-price billing mode for dedicated connections that you set per connection. For more information, see [Flat-rate billing for dedicated connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/flat-rate-connections.html). | September 15, 2026 |", th="| Change | Description | Date |", url=DX_HIST_URL)],
    reason="currency unsure: claim now names the flat-rate billing mode of 2026-09-15 (not examinable yet) next to the FAQ's two charges")
for fid in ["direct-connect-limit-mtu-private-vif", "direct-connect-limit-mtu-transit-vif"]:
    vals = copy.deepcopy(facts[fid]["values"])
    for v in vals:
        if v["key"] == "default":
            v["key"] = "standard"
    D[fid] = dict(values=vals, reason="entail partial: value key 'default' renamed 'standard'; no quote says 1500 is the default")
PFX_NOTE = E("docs/directconnect/latest/UserGuide/prefix-controls", "Public VIFs are not managed by inbound prefix controls.")
D["direct-connect-limit-prefix-controls-default-allocation"] = dict(
    claim="With inbound prefix controls, the default allocation per virtual interface is 100 per address family (IPv4 and IPv6). Public VIFs are not managed by inbound prefix controls.",
    add_ev=[PFX_NOTE], quals={"scope": "per VIF", "condition": "public VIFs are not managed by inbound prefix controls"},
    reason="entail partial: added the public-VIF exception sentence after the table")
D["direct-connect-limit-prefix-controls-max-allocation"] = dict(
    claim="With inbound prefix controls, the maximum allocation per virtual interface is 1,000 per address family (IPv4 and IPv6). Public VIFs are not managed by inbound prefix controls.",
    add_ev=[PFX_NOTE], quals={"scope": "per VIF", "condition": "public VIFs are not managed by inbound prefix controls"},
    reason="entail partial: added the public-VIF exception sentence after the table")
D["direct-connect-limit-prefix-controls-dxgw-total"] = dict(
    claim="With inbound prefix controls, total allocations per Direct Connect gateway are 10,000, counting IPv4 and IPv6 together. Public VIFs are not managed by inbound prefix controls.",
    add_ev=[PFX_NOTE], quals={"condition": "public VIFs are not managed by inbound prefix controls"},
    reason="entail partial: added the public-VIF exception sentence after the table")
D["direct-connect-limit-prefix-controls-pool-per-connection"] = dict(
    claim="With inbound prefix controls, the prefix pool per dedicated connection is 5,000 for 1 and 10 Gbps, 30,000 for 100 Gbps and 50,000 for 400 Gbps. Public VIFs are not managed by inbound prefix controls.",
    add_ev=[PFX_NOTE], quals={"condition": "public VIFs are not managed by inbound prefix controls"},
    reason="entail partial: added the public-VIF exception sentence after the table")
D["direct-connect-quota-rate-limiters-per-dedicated"] = dict(
    claim="A Direct Connect dedicated connection supports 10 rate limiters. For more, the quotas page says to contact your Solutions Architect or Technical Account Manager, while the VIF rate limiters page says you can request a limit increase through AWS Service Quotas.",
    add_ev=[E("docs/directconnect/latest/UserGuide/vif-rate-limiters", "Each dedicated connection supports up to **10 rate limiters**. You can request a limit increase through AWS Service Quotas.")],
    quals={"condition": ""},
    reason="currency unsure: claim now states both increase paths that the two AWS pages give; absorbs direct-connect-limit-rate-limiters-10-per-dedicated")
D["direct-connect-macsec-new-connections-default-should-encrypt"] = dict(
    add_ev=[E("docs/directconnect/latest/UserGuide/MACsec", "must_encrypt — In this mode, the connection requires MACsec encryption for all traffic. If MACsec negotiation fails or encryption cannot be established, the connection will not transmit any traffic.")],
    reason="entail partial: added the must_encrypt quote")
D["direct-connect-maintenance-notify-aws-health-email"] = dict(
    claim="Direct Connect emails notifications about planned and emergency maintenance events to the email address of the AWS account that owns the connection or virtual interface. For planned maintenance, you can also receive notifications in your monitoring or ticketing system by integrating with AWS Health.",
    reason="entail partial: AWS Health integration scoped to planned maintenance, where the quote stands")
D["direct-connect-not-encrypted-by-default-use-service-encryption"] = dict(
    quals={"condition": ""},
    reason="entail partial: removed the condition that named IPsec VPN and MACsec, which no quote states")
D["direct-connect-plus-vpn-public-vif-ipsec-more-consistent-than-internet-vpn"] = dict(
    claim="Direct Connect public virtual interfaces establish a dedicated network connection to public AWS resources such as a Site-to-Site VPN endpoint, and you can then create IPsec connections to the VPC virtual private gateways. This combines end-to-end IPsec security with the low latency and increased bandwidth of Direct Connect, for a more consistent network experience than internet-based VPN connections.",
    add_ev=[E("docs/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-site-to-site-vpn", "AWS Direct Connect public VIFs establish a dedicated network connection between your network and public AWS resources such as an AWS Site-to-Site VPN endpoint. Once you establish the connection to the service, you can create IPsec connections to the corresponding Amazon VPC virtual private gateways.")],
    reason="entail partial: added the quote for the public VIF and IPsec steps")
D["direct-connect-public-prefixes-global-by-default-without-scope-community"] = dict(
    quals={"condition": ""},
    reason="entail partial: removed the wrong community condition (7224:9300 is global, not narrowing)")
D["direct-connect-public-vif-access-all-public-regions-from-any-location"] = dict(
    claim="From any Direct Connect location in a public Region or AWS GovCloud (US), you can access all public AWS Regions (except those in China (Beijing and Ningxia)), AWS GovCloud (US) Regions, and AWS Local Zones.",
    reason="entail not-supported: misread fixed; only the China Regions are excepted, GovCloud (US) and Local Zones are reachable")
D["direct-connect-quota-routes-per-bgp-session-private-transit"] = dict(
    quals={"condition": "can be increased using prefix controls up to 1,000 each for IPv4 and IPv6"},
    reason="entail partial: condition restated in the words of the quotas row; 'not examinable yet' stays in the note")
D["direct-connect-quota-sitelink-prefix-limit"] = dict(
    quals={"condition": "configured using prefix controls"},
    reason="entail partial: condition restated in the words of the quotas row")
D["direct-connect-sla-not-for-hosted"] = dict(
    claim="The Direct Connect SLAs do not apply to Direct Connect services accessed through an APN Direct Connect Partner integration using a hosted connection or hosted virtual interfaces. They apply to dedicated connections that you access through services of an APN Direct Connect Partner, provided those dedicated connections are owned by your AWS account.",
    reason="entail partial: second sentence keeps the partner-access scope of the quote")
D["direct-connect-vs-vpn-selection-criteria-five-considerations"] = dict(
    claim="The considerations that affect the hybrid connectivity type you select include time to deploy, security, SLA, performance, and cost.",
    reason="entail partial: 'are' changed to 'include', as the quote says")
D["site-to-site-vpn-capability-modify-tunnel-bandwidth"] = dict(
    claim="Large Bandwidth Tunnels are available only for VPN connections attached to a transit gateway or to Cloud WAN, not for virtual private gateway attachments, and you can modify the tunnel bandwidth of existing VPN connections.",
    add_ev=[E("docs/vpn/latest/s2svpn/VPNTunnels", "Available only for VPN connections attached to a transit gateway or to Cloud WAN. Not supported for Virtual Private Gateway attachments.")],
    quals={"scope": "Large Bandwidth Tunnels; VPN connections on a transit gateway or Cloud WAN"},
    reason="entail partial: added the transit gateway or Cloud WAN scope of the Large Bandwidth Tunnels list")
D["site-to-site-vpn-change-bgp-logging"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/11/site-to-site-vpn-bgp-logging-vpn-tunnels", "Nov 20, 2025", "AWS Site-to-Site VPN now supports BGP logging for VPN tunnels"),
            E("www/about-aws/whats-new/2025/11/site-to-site-vpn-bgp-logging-vpn-tunnels", "AWS Site-to-Site VPN now allows customers to publish Border Gateway Protocol (BGP) logs from VPN tunnels to AWS CloudWatch, providing enhanced visibility into VPN configurations and simplifying troubleshooting of connectivity issues.")],
    reason="entail partial: added the Posted on line and the CloudWatch sentence")
D["site-to-site-vpn-change-large-bandwidth-tunnels"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/11/aws-site-to-site-vpn-5-gbps-bandwidth-tunnels", "Nov 12, 2025", "AWS Site-to-Site VPN announces 5 Gbps bandwidth tunnels")],
    reason="entail partial: added the Posted on line for the date")
D["site-to-site-vpn-change-vpn-concentrator"] = dict(
    add_ev=[posted("www/about-aws/whats-new/2025/11/aws-site-to-site-vpn-concentrator", "Nov 19, 2025", "AWS Site-to-Site VPN announces VPN Concentrator")],
    reason="entail partial: added the Posted on line for the date")
D["site-to-site-vpn-cloudhub-hub-and-spoke-between-sites"] = dict(
    claim="AWS VPN CloudHub lets several Site-to-Site VPN connections give your sites secure communication with each other, not only with the VPC. It uses a hub-and-spoke model that works with or without a VPC, and the design suits multiple branch offices with existing internet connections that want a potentially low-cost hub-and-spoke model for primary or backup connectivity between the sites.",
    add_ev=[E("docs/vpn/latest/s2svpn/VPN_CloudHub", "This design is suitable if you have multiple branch offices and existing internet connections and would like to implement a convenient, potentially low-cost hub-and-spoke model for primary or backup connectivity between these sites.")],
    reason="entail partial: added the branch-office sentence")
D["site-to-site-vpn-cloudhub-unique-asn-per-customer-gateway"] = dict(
    add_ev=[E("docs/vpn/latest/s2svpn/VPN_CloudHub", "Create a single virtual private gateway."),
            E("docs/vpn/latest/s2svpn/VPN_CloudHub", "Create a dynamically routed Site-to-Site VPN connection from each customer gateway to the common virtual private gateway.")],
    reason="entail partial: added the quotes of steps 1 and 3")
D["site-to-site-vpn-concentrator-aggregate-5-gbps-site-100-mbps"] = dict(
    claim="Site-to-Site VPN Concentrators currently support 5 Gbps aggregate bandwidth, and each site can support a maximum of 100 Mbps; if you need higher bandwidth, reach out to AWS Support.",
    quals={"adjustable": True, "condition": "if you need higher bandwidth, reach out to AWS Support"},
    reason="entail partial: claim keeps the AWS Support exception; adjustable set true")
D["site-to-site-vpn-elc-control-schedule-of-endpoint-replacements"] = dict(
    claim="Tunnel endpoint lifecycle control gives you control over when AWS managed tunnel endpoint replacements happen. Use it if you have short-term business needs or can only support a single tunnel per VPN connection. In rare circumstances AWS might apply critical updates to tunnel endpoints immediately, even with the feature enabled.",
    add_ev=[E("docs/vpn/latest/s2svpn/tunnel-endpoint-lifecycle", "In rare circumstances, AWS might apply critical updates to tunnel endpoints immediately, even if the tunnel endpoint lifecycle control feature is enabled.")],
    reason="entail partial: added the critical-updates exception")
D["site-to-site-vpn-faq-tunnel-max-pps"] = dict(
    claim="Each Site-to-Site VPN connection has two tunnels, and a standard VPN tunnel supports up to 140,000 packets per second (the VPN FAQ states this value for each tunnel; the quotas page gives it for a standard tunnel).",
    add_ev=[E("docs/vpn/latest/s2svpn/vpn-limits", "| Maximum packets per second (PPS) per standard VPN tunnel | Up to 140,000 | No |", th="| Name | Default | Adjustable |", url=VPN_LIMITS_URL)],
    quals={"scope": "per standard VPN tunnel; a connection has two tunnels"},
    reason="currency unsure: scoped to standard tunnels with the quotas row (large bandwidth tunnels differ)")
D["site-to-site-vpn-faq-tunnel-max-throughput"] = dict(
    claim="Each Site-to-Site VPN connection has two tunnels, and a standard VPN tunnel supports up to 1.25 Gbps (the VPN FAQ states this value for each tunnel; the quotas page gives it for a standard tunnel). For a connection to a virtual private gateway, aggregated throughput limits apply.",
    add_ev=[E("docs/vpn/latest/s2svpn/vpn-limits", "| Maximum bandwidth per standard VPN tunnel | Up to 1.25 Gbps | No |", th="| Name | Default | Adjustable |", url=VPN_LIMITS_URL)],
    quals={"scope": "per standard VPN tunnel; a connection has two tunnels"},
    reason="currency outdated: scoped to standard tunnels with the quotas row (large bandwidth tunnels reach 5 Gbps)")
D["site-to-site-vpn-faq-vgw-asn-private-only-reason"] = dict(
    claim="Amazon does not validate ownership of ASNs, so it limits the Amazon-side ASN to private ASNs, to protect customers from BGP spoofing; the exception is the legacy public ASN of the Region.",
    add_ev=[E("www/vpn/faqs", "We will ask you to re-enter a private ASN once you attempt to create the virtual gateway, unless it is the \"legacy public ASN\" of the region.")],
    reason="entail partial: added the legacy public ASN exception")
D["site-to-site-vpn-ipv4-inside-tunnel-by-default"] = dict(
    add_ev=[E("docs/vpn/latest/s2svpn/ipv4-ipv6", "Your Site-to-Site VPN connection on a transit gateway can support either IPv4 traffic or IPv6 traffic inside the VPN tunnels.")],
    reason="entail partial: added the sentence that carries the transit gateway scope")
D["site-to-site-vpn-limit-accelerated-unassociated-count-toward-total"] = dict(
    quals={"scope": "Site-to-Site VPN connections per Region quota", "adjustable": False},
    reason="entail partial: removed adjustable true, which the quote does not state")
D["site-to-site-vpn-longest-prefix-match-most-specific-route"] = dict(
    claim="The VPC uses the most specific route in the route table that matches the traffic to decide how to route it (longest prefix match). Exception: if propagated Site-to-Site VPN or Direct Connect routes overlap with the VPC local route, the local route is most preferred even if the propagated routes are more specific.",
    add_ev=[E("docs/vpn/latest/s2svpn/vpn-route-priority", "If propagated routes from a Site-to-Site VPN connection or Direct Connect connection overlap with the local route for your VPC, the local route is most preferred even if the propagated routes are more specific.")],
    reason="entail partial: added the local-route exception")
D["site-to-site-vpn-nat-device-needs-idr-identity"] = dict(
    claim="In the rules and limitations for Site-to-Site VPN tunnel initiation options: if the customer gateway device is behind a firewall or other device that uses NAT, it must have an identity (IDr) configured.",
    quals={"scope": "VPN tunnel initiation options (rules and limitations)"},
    reason="entail partial: claim scoped to the tunnel initiation rules list where the quote stands")
D["site-to-site-vpn-pricing-data-transfer-out-ec2-rates"] = dict(
    quals={"scope": "Site-to-Site VPN data transfer out"},
    reason="entail partial: removed the scope 'per gigabyte', which the quote does not state")
D["site-to-site-vpn-redundant-second-vpn-second-cgw-device"] = dict(
    claim="To protect against the loss of the customer gateway device, set up a second Site-to-Site VPN connection to the same virtual private gateway by adding a second customer gateway device. Both devices should advertise the same IP ranges; BGP routing decides the path, and if one device fails the virtual private gateway directs all traffic to the working device.",
    reason="entail partial: claim keeps the same-prefix and BGP condition of the quote")
D["site-to-site-vpn-static-route-beats-propagated-same-cidr"] = dict(
    claim="When a propagated Site-to-Site VPN or Direct Connect route has the same destination CIDR block as an existing static route, the VPC prioritizes the static routes whose targets are an internet gateway, a virtual private gateway, a network interface, an instance ID, a VPC peering connection, a NAT gateway, a transit gateway, or a gateway VPC endpoint.",
    reason="entail partial: claim lists the static-route targets that the quote names")
D["site-to-site-vpn-target-gateway-generic-term"] = dict(
    add_ev=[E("docs/vpn/latest/s2svpn/VPC_VPN", VGW_DEF, url=VPC_VPN_URL)],
    reason="entail partial: added the virtual private gateway definition")
D["site-to-site-vpn-tgw-prefers-dx-gateway-route-over-vpn"] = dict(
    claim="A transit gateway shows only a preferred route. If you advertise the same routes over the Direct Connect gateway and over Site-to-Site VPN, the transit gateway shows only the routes received from the Direct Connect gateway (the preferred route); the VPN route is the backup and appears only when the Direct Connect gateway route is no longer advertised.",
    replace_ev=[E("docs/vpc/latest/tgw/how-transit-gateways-work", "AWS Transit Gateway only shows a preferred route. A backup route will only appear in the transit gateway route table if the previously active route is no longer advertised — for example, if you are advertising the same routes over the Direct Connect gateway and over Site-to-Site VPN. AWS Transit Gateway will only show the routes received from the Direct Connect gateway route, which is the preferred route. The Site-to-Site VPN, which is the backup route, will only display when the Direct Connect gateway is no longer advertised.")],
    reason="entail partial: quote widened to the whole paragraph with the same-routes condition")
D["site-to-site-vpn-vgw-attaches-to-single-vpc"] = dict(
    claim="A virtual private gateway can be attached to a single VPC, and you can attach one virtual private gateway to a VPC at a time. To connect the same Site-to-Site VPN connection to several VPCs, AWS recommends exploring a transit gateway instead.",
    add_ev=[E("docs/vpn/latest/s2svpn/VPC_VPN", VGW_DEF, url=VPC_VPN_URL)],
    reason="entail partial: added the definition that states one VPC per virtual private gateway")

REJECT = {
    "client-vpn-change-quota-increase-2024-12": "currency unsure: the dated 100 value was replaced by 200 (2025-03); current values and the 50 to 200 change are carried by client-vpn-quota-authorization-rules-per-endpoint",
    "direct-connect-faq-bgp-routes-limit-100": "currency outdated: FAQ 'up to 100 routes' is now only the default allocation; the current row is direct-connect-quota-routes-per-bgp-session-private-transit",
    "direct-connect-limit-bgp-session-down-over-100-routes": "currency outdated: FAQ threshold of 100 is now the default allocation; the idle/DOWN behaviour is in direct-connect-quota-routes-per-bgp-session-private-transit",
    "direct-connect-limit-rate-limiters-10-per-dedicated": "currency unsure: merged into direct-connect-quota-rate-limiters-per-dedicated, which now states both increase paths",
}

index = {}
for fid, d in D.items():
    f = facts[fid]
    assert f["status"] == "disputed", fid
    p = {}
    if "claim" in d:
        p["claim"] = d["claim"]
    if "values" in d:
        p["values"] = d["values"]
    if "quals" in d:
        q = copy.deepcopy(f["qualifiers"])
        q.update(d["quals"])
        p["qualifiers"] = q
    if "replace_ev" in d:
        p["evidence"] = d["replace_ev"]
    elif "add_ev" in d:
        p["evidence"] = ev_of(f) + d["add_ev"]
    json.dump(p, open(OUT + fid + ".json", "w"), indent=2, ensure_ascii=False)
    index[fid] = d["reason"]
json.dump({"repair": index, "reject": REJECT}, open(W + "adj-12-decisions.json", "w"), indent=1, ensure_ascii=False)
print("patches", len(D), "rejects", len(REJECT), "total", len(D) + len(REJECT))
