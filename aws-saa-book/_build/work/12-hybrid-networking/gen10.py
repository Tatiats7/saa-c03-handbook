import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
C="client-vpn"
WN="www/about-aws/whats-new/"
WH="docs/vpn/latest/clientvpn-admin/WhatsNew"
HH="| Change | Description | Date |"
TG="docs/vpn/latest/clientvpn-admin/cvpn-tgw"
PR="www/vpn/pricing"
F=[]
F.append(fact("client-vpn-change-transit-gateway-integration",C,"change",
 "On April 23, 2026 Client VPN added native Transit Gateway integration: the endpoint attaches to a transit gateway, which removes the intermediate VPC that connecting Client VPN to multiple VPCs needed.",
 "What changed about connecting Client VPN to multiple VPCs?",
 [("new","native Transit Gateway integration","")],"per Client VPN endpoint","fixed",False,
 [ev(WN+"2026/04/aws-client-vpn-transit-gateway","Native Transit Gateway attachment eliminates the need for an intermediate VPC, letting you provide centralized remote access to multiple VPCs and on-premises networks directly from your Client VPN endpoint."),
  ev(WN+"2026/04/aws-client-vpn-transit-gateway","Previously, connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC, adding operational complexity as you needed to manage additional resources.")],
 tier=3,vol="changed-since-2022",changed={"date":"2026-04-23","was":"connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC","was_evidence":1},
 change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="extended",bullets=["3.4.S1"],note="d12-089. Examinable but recent (announced 2026-04-23; the history row of 2026-04-20 is not in the saved history page): label Changed recently."))
F.append(fact("client-vpn-restriction-tgw-no-mixing-associations",C,"restriction",
 "You cannot mix VPC subnet associations and Transit Gateway associations in a single Client VPN endpoint; you choose one association type when you create the endpoint.",
 "Can one Client VPN endpoint have both subnet associations and a Transit Gateway association?",
 [("rule","cannot mix VPC subnet associations and Transit Gateway associations","")],"per Client VPN endpoint","fixed",False,
 [ev(TG,"You cannot mix VPC subnet associations and Transit Gateway associations in a single Client VPN endpoint. Choose one association type when you create the endpoint.")],
 vol="frequently-changing",change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="extended",bullets=["3.4.S1"],note="d12-089"))
F.append(fact("client-vpn-restriction-tgw-no-security-group-authorization",C,"restriction",
 "For Client VPN endpoints attached to a Transit Gateway, security group-based authorization is not supported; you use network-based authorization rules only.",
 "Can Client VPN endpoints attached to a Transit Gateway use security group-based authorization?",
 [("rule","Security group-based authorization is not supported","")],"per Client VPN endpoint","fixed",False,
 [ev(TG,"Security group-based authorization is not supported for Transit Gateway endpoints.")],
 vol="frequently-changing",change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="reference",bullets=["3.4.S1"],note="d12-089"))
F.append(fact("client-vpn-restriction-tgw-no-route-propagation",C,"restriction",
 "For Client VPN endpoints attached to a Transit Gateway, automatic route propagation from the Transit Gateway is not supported.",
 "Does a Client VPN endpoint attached to a Transit Gateway learn routes automatically from the Transit Gateway?",
 [("rule","Automatic route propagation from Transit Gateway is not supported","")],"per Client VPN endpoint","fixed",False,
 [ev(TG,"Automatic route propagation from Transit Gateway is not supported.")],
 vol="frequently-changing",change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="reference",bullets=["3.4.S1"],note="d12-089"))
F.append(fact("client-vpn-limit-tgw-availability-zones",C,"limit",
 "A Client VPN endpoint attached to a Transit Gateway can specify up to 5 Availability Zones.",
 "How many Availability Zones can a Client VPN endpoint attached to a Transit Gateway use?",
 [("max","up to 5 Availability Zones","up to five Availability Zones")],"per Client VPN endpoint","max",False,
 [ev(TG,"You can specify up to 5 Availability Zones per endpoint.")],
 vol="frequently-changing",change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="reference",bullets=["3.4.S1"],note="d12-089"))
F.append(fact("client-vpn-default-tgw-availability-zones-2",C,"default",
 "When you attach a Client VPN endpoint to a Transit Gateway and do not specify Availability Zones, AWS selects 2 Availability Zones automatically.",
 "How many Availability Zones does AWS select for a Transit Gateway Client VPN endpoint when you do not choose?",
 [("default","2 Availability Zones","two Availability Zones")],"per Client VPN endpoint","default",True,
 [ev(TG,"**Availability Zone selection** — You specify which Availability Zones to use, or AWS selects 2 Availability Zones automatically.")],
 vol="frequently-changing",change_items=[cid('cvpn','native AWS Transit Gateway integration')],exam="reference",bullets=["3.4.S1"],note="d12-089"))
F.append(fact("client-vpn-change-ipv6-support",C,"change",
 "On August 26, 2025 Client VPN added support for IPv6 resources through IPv6-only or dual-stack endpoints; before, it supported remote access only to IPv4-enabled AWS workloads.",
 "What changed about the IP versions Client VPN supports?",
 [("new","IPv6-only or dual-stack Client VPN endpoints","")],"per Client VPN endpoint","fixed",False,
 [ev(WN+"2025/08/aws-client-vpn-connectivity-ipv6-resources","Previously, Client VPN only supported remote access to IPv4-enabled AWS workloads. With this feature, administrators can now support IPv6-enabled resources using IPv6-only or dual-stack Client VPN endpoints.")],
 tier=3,vol="changed-since-2022",changed={"date":"2025-08-26","was":"Client VPN only supported remote access to IPv4-enabled AWS workloads","was_evidence":0},
 change_items=[cid('cvpn','connectivity to IPv6 resources'),cid('cvpn','IPv6 support')],exam="reference",bullets=["3.4.S1"],note="d12-095. History row 2025-08-25."))
F.append(fact("client-vpn-change-concurrent-connections-per-client",C,"change",
 "On January 22, 2025 Client VPN added concurrent VPN connections: a user can connect to multiple VPN profiles at the same time, with the AWS-supplied client version 5.0 or later; before, only one VPN profile at a time.",
 "What changed about how many VPN profiles one Client VPN user can connect to at once?",
 [("new","multiple VPN profiles simultaneously","")],"per client device","fixed",False,
 [ev(WN+"2025/01/aws-client-vpn-concurrent-vpn-connections","Previously, you could only connect to one VPN profile at a time."),
  ev(WN+"2025/01/aws-client-vpn-concurrent-vpn-connections","This feature is available only with AWS-supplied Client VPN client version 5.0+.")],
 tier=3,vol="changed-since-2022",changed={"date":"2025-01-22","was":"you could only connect to one VPN profile at a time","was_evidence":0},
 change_items=[cid('cvpn','concurrent VPN connections')],exam="reference",bullets=["3.4.S1"],note="d12-095"))
F.append(fact("client-vpn-change-disconnect-on-session-timeout",C,"change",
 "On January 13, 2025 Client VPN session timeout gained support for disconnect on session timeout, which applies when the maximum session duration is reached.",
 "When did Client VPN add disconnect on session timeout?",
 [("new","disconnect on session timeout","")],"per Client VPN endpoint","fixed",False,
 [ev(WH,row(WH,"| [Support for disconnect on session timeout]"),HH)],
 tier=3,vol="frequently-changing",change_items=[cid('cvpn','disconnect on session timeout')],exam="reference",bullets=["1.2.S4"],note="d12-090"))
F.append(fact("client-vpn-change-quota-increase-2024-12",C,"change",
 "On December 19, 2024 the Client VPN quotas for authorization rules per endpoint and routes per endpoint increased from 50 and 10 respectively to 100.",
 "What did the Client VPN quota increase of December 2024 change?",
 [("new","increased from 50 and 10 respectively to 100","")],"per Client VPN endpoint","fixed",False,
 [ev(WH,row(WH,"| [Increased quotas]"),HH)],
 tier=3,vol="changed-since-2022",changed={"date":"2024-12-19","was":"50 and 10 respectively","was_evidence":0},
 change_items=[cid('cvpn','Increased quotas')],exam="reference",bullets=["4.4.S7"],note="d12-094. Current values: client-vpn-quota-authorization-rules-per-endpoint and client-vpn-quota-routes-per-association."))
F.append(fact("client-vpn-change-quota-increase-2025-03",C,"change",
 "On March 13, 2025 the Client VPN authorization rules per endpoint quota increased from 50 to 200.",
 "What did the Client VPN quota increase of March 2025 change?",
 [("new","from 50 to 200","")],"per Client VPN endpoint","fixed",False,
 [ev(WH,row(WH,"| [Increased Client VPN quota]"),HH)],
 tier=3,vol="changed-since-2022",changed={"date":"2025-03-13","was":"from 50 to 200","was_evidence":0},
 change_items=[cid('cvpn','Increased Client VPN quota')],exam="reference",bullets=["4.4.S7"],note="d12-094. The history row of 2024-12-19 already says 100; this row says 50 to 200. The post of 2025-03-18 says 50 to 200 and 10 to 100."))
F.append(fact("client-vpn-change-client-route-enforcement",C,"change",
 "On April 20, 2025 Client VPN added the client route enforcement feature.",
 "When did Client VPN add client route enforcement?",
 [("new","client route enforcement feature","")],"per Client VPN endpoint","fixed",False,
 [ev(WH,row(WH,"| [Client route enforcement feature]"),HH)],
 tier=3,vol="frequently-changing",change_items=[cid('cvpn','Client route enforcement feature')],exam="reference",bullets=["1.2.S4"],note="Triaged from the document history."))
F.append(fact("client-vpn-change-vpn-client-v6",C,"change",
 "AWS Client VPN introduced a rebuilt AWS VPN Client v6.0.x with command-line interface support, enterprise administrative controls and faster connection establishment.",
 "What is new in AWS VPN Client v6.0.x?",
 [("new","AWS VPN Client v6.0.x","")],"per client device","fixed",False,
 [ev(WN+"2026/08/aws-client-vpn-cli","AWS Client VPN introduces a rebuilt AWS VPN Client v6.0.x which offers new features like command-line interface (CLI) support, enterprise administrative controls, and faster connection establishment time, making it easier you to automate VPN connectivity and centralize device management across your organization.")],
 tier=3,vol="frequently-changing",change_items=[cid('cvpn','CLI, administration controls')],exam="reference",bullets=["3.4.S1"],note="d12-095. Posted 2026-08-13. Not examinable yet (GA after 2026-07-15): label as not examinable yet."))
# pricing
F.append(fact("client-vpn-pricing-endpoint-and-connection-hourly-fees",C,"pricing-dimension",
 "In the AWS pricing example for Client VPN, you pay an endpoint hourly fee for the Client VPN endpoint and a connection hourly fee for the active Client VPN connections.",
 "Which hourly fees make up Client VPN pricing?",
 [("v","endpoint hourly fee and connection hourly fee","")],"per Client VPN endpoint and per connection","",False,
 [ev(PR,"AWS Client VPN endpoint hourly fee: For this AWS Region, you pay $0.10 per hour in AWS Client VPN endpoint hourly fees."),
  ev(PR,"AWS Client VPN connection hourly fee: Ten AWS Client VPN connections were active for 1 hour. You pay $0.50 per hour in AWS Client VPN connection fees.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-093. Example only: the page states no separate rule that the endpoint fee is per associated subnet; no dollar amount goes into the book."))
F.append(fact("client-vpn-pricing-software-client-free",C,"pricing-dimension",
 "The AWS Client VPN software client is provided free of charge; you are billed only for AWS Client VPN service usage.",
 "Is there an additional price to use the AWS Client VPN software client?",
 [("v","provided free of charge","")],"per client","",False,
 [ev("www/vpn/faqs","The software client is provided free of charge. You will only be billed for AWS Client VPN service usage.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-093. FAQ 82."))
F.append(fact("client-vpn-pricing-public-ipv4-address-charge",C,"pricing-dimension",
 "Each Client VPN connection uses a unique public IPv4 address for the tunnels, and you incur standard public IPv4 address charges on it.",
 "Do Client VPN connections incur public IPv4 address charges?",
 [("v","standard public IPv4 address charges","")],"per Client VPN connection","",False,
 [ev(PR,"Each Client VPN connection uses unique public IPv4 address for the tunnels. You will incur standard public IPv4 address charges on the IPv4 address that will be used for the tunnels.")],
 tier=2,exam="reference",bullets=["4.4.S2"],note="d12-093"))
dump(F,"facts-changes-02.json")
