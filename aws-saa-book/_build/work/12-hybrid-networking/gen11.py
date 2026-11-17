import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
S="site-to-site-vpn"
WN="www/about-aws/whats-new/"
WH="docs/vpn/latest/s2svpn/WhatsNew"
HH="| Change | Description | Date |"
VC="docs/vpn/latest/s2svpn/vpn-concentrator"
PR="www/vpn/pricing"
F=[]
F.append(fact("site-to-site-vpn-change-large-bandwidth-tunnels",S,"change",
 "On November 12, 2025 Site-to-Site VPN announced up to 5 Gbps bandwidth per tunnel, a 4x improvement from the existing limit of 1.25 Gbps; the document history lists Large Bandwidth Tunnels for transit gateway and Cloud WAN attachments on September 25, 2025.",
 "How much bandwidth per tunnel did Site-to-Site VPN add, and what was the old limit?",
 [("new","up to 5 Gbps bandwidth per tunnel","up to five gigabits per second per tunnel"),("was","1.25 Gbps","one point two five gigabits per second")],
 "per VPN tunnel","max",False,
 [ev(WN+"2025/11/aws-site-to-site-vpn-5-gbps-bandwidth-tunnels","AWS Site-to-Site VPN now supports VPN connections with up to 5 Gbps bandwidth per tunnel, a 4x improvement from existing limit of 1.25 Gbps."),
  ev(WH,row(WH,"| [Site-to-Site VPN support for Large Bandwidth Tunnels]"),HH),
  ev(WN+"2025/11/aws-site-to-site-vpn-5-gbps-bandwidth-tunnels","Until now, Site-to-Site VPN supported a maximum of 1.25Gbps bandwidth per tunnel and customers had to rely on ECMP (Equal cost multi path) to logically bond multiple tunnels to achieve higher bandwidth.")],
 tier=3,vol="changed-since-2022",changed={"date":"2025-11-12","was":"1.25 Gbps","was_evidence":0},
 change_items=[cid('s2s','5 Gbps bandwidth tunnels'),cid('s2s','Large Bandwidth Tunnels')],exam="core",bullets=["4.4.S7"],
 note="d12-078. Current-truth fact: site-to-site-vpn-limit-bandwidth-large-tunnel. Standard tunnels stay at 1.25 Gbps (site-to-site-vpn-limit-bandwidth-standard-tunnel)."))
F.append(fact("site-to-site-vpn-change-modify-tunnel-bandwidth",S,"change",
 "On May 6, 2026 Site-to-Site VPN added modifying tunnel bandwidth between standard (up to 1.25 Gbps) and large (up to 5 Gbps) on existing connections, preserving IP addresses, CIDR blocks, pre-shared keys and configuration; before, changing tunnel bandwidth required deleting and recreating the connection.",
 "What changed about changing the tunnel bandwidth of an existing Site-to-Site VPN connection?",
 [("new","modifying tunnel bandwidth on existing VPN connections","")],"per VPN connection","fixed",False,
 [ev(WN+"2026/05/aws-site-to-site-vpn-modify-bandwidth","Previously, changing tunnel bandwidth required deleting and recreating the connection, which generated new tunnel IP addresses and meant updating your on-premises VPN device configuration and firewall rules."),
  ev(WN+"2026/05/aws-site-to-site-vpn-modify-bandwidth","With this launch, tunnels are upgraded while preserving your IP addresses, CIDR blocks, pre-shared keys, and all configuration settings, eliminating the need to make any changes to your on-premises device."),
  ev(WN+"2026/05/aws-site-to-site-vpn-modify-bandwidth","AWS Site-to-Site VPN now supports modifying tunnel bandwidth between standard (up to 1.25 Gbps) and large (up to 5 Gbps) on existing connections, making it easier to update your VPN connections’ bandwidth per your organization’s need.")],
 tier=3,vol="changed-since-2022",changed={"date":"2026-05-06","was":"changing tunnel bandwidth required deleting and recreating the connection","was_evidence":0},
 change_items=[cid('s2s','modifying tunnel bandwidth')],exam="extended",bullets=["4.4.S7"],note="d12-009, d12-078. Examinable but recent (2026-05-06): label Changed recently."))
F.append(fact("site-to-site-vpn-change-bgp-logging",S,"change",
 "On November 20, 2025 Site-to-Site VPN added BGP logs from VPN tunnels to CloudWatch; before, customers only had tunnel activity logs showing IKE and IPsec tunnel details.",
 "What did BGP logging add to Site-to-Site VPN logs?",
 [("new","BGP logs from VPN tunnels","")],"per VPN tunnel","fixed",False,
 [ev(WN+"2025/11/site-to-site-vpn-bgp-logging-vpn-tunnels","Until now, customers only had access to tunnel activity logs showing IKE/IPSec tunnel details. With this launch, customers can now access detailed BGP logs that provide visibility into BGP session status and transitions, routing updates, and detailed BGP error states.")],
 tier=3,vol="changed-since-2022",changed={"date":"2025-11-20","was":"customers only had access to tunnel activity logs showing IKE/IPSec tunnel details","was_evidence":0},
 change_items=[cid('s2s','BGP logging')],exam="reference",bullets=["1.2.S4"],note="d12-079. The 2022-08-19 CloudWatch logs post is blocked by robots.txt (feed pointer only): site-to-site-vpn-change-bgp-logging does not cover it."))
F.append(fact("site-to-site-vpn-change-secrets-manager-psk",S,"change",
 "On May 27, 2025 Site-to-Site VPN added AWS Secrets Manager for storing a pre-shared key; when stored there, VPN connection API responses redact the key and show the Secrets Manager ARN.",
 "Where can a Site-to-Site VPN pre-shared key be stored besides the VPN service?",
 [("new","AWS Secrets Manager for storing a pre-shared key","")],"per VPN connection","fixed",False,
 [ev(WH,row(WH,"| [Updated pre-shared key storage options]"),HH),
  ev(WN+"2025/06/aws-site-to-site-vpn-three-capabilities-enhanced-security","AWS Secrets Manager Integration: With the AWS Secrets Manager integration, when customers store their pre-shared keys (PSKs) in Secrets Manager, VPN connection API responses will redact the PSK and instead display the Secrets Manager ARN (Amazon Resource Name), providing enhanced security.")],
 tier=3,vol="frequently-changing",change_items=[cid('s2s','Updated pre-shared key storage options'),cid('s2s','three new capabilities')],exam="extended",bullets=["1.2.S4"],note="d12-079. Posted 2025-06-03."))
F.append(fact("site-to-site-vpn-change-recommended-configuration",S,"change",
 "Since the June 2025 security update, the GetVpnConnectionDeviceSampleConfiguration API has a recommended parameter that uses IKE version 2, DH group 20, SHA-384 integrity and AES-GCM-256 encryption.",
 "Which settings does the recommended Site-to-Site VPN configuration use?",
 [("rec","IKE version 2, DH group 20, SHA-384 integrity algorithm, and AES-GCM-256 encryption algorithm","")],"per customer gateway configuration","fixed",False,
 [ev(WN+"2025/06/aws-site-to-site-vpn-three-capabilities-enhanced-security","Recommended Configuration: “GetVpnConnectionDeviceSampleConfiguration” API now includes “recommended” parameter to help you use the best-practices security configuration - IKE version 2, DH group 20, SHA-384 integrity algorithm, and AES-GCM-256 encryption algorithm - on your customer gateway devices, reducing configuration time and potential errors.")],
 tier=3,vol="frequently-changing",change_items=[cid('s2s','three new capabilities')],exam="reference",bullets=["1.2.S4"],note="d12-079"))
F.append(fact("site-to-site-vpn-change-ipv6-outer-tunnel-ips",S,"change",
 "On July 1, 2025 Site-to-Site VPN added IPv6 addresses for the outer tunnel IPs on Transit Gateway and Cloud WAN VPN connections.",
 "Which gateways support IPv6 outer tunnel IP addresses for Site-to-Site VPN?",
 [("new","IPv6 addresses for the outer tunnel IPs","")],"per VPN connection","fixed",False,
 [ev(WH,row(WH,"| [IPv6 support for AWS Site-to-Site VPN for outer tunnel IPs]"),HH)],
 tier=3,vol="frequently-changing",change_items=[cid('s2s','outer tunnel IPs')],exam="reference",bullets=["3.4.S1"],note="d12-079"))
F.append(fact("site-to-site-vpn-change-vpn-concentrator",S,"change",
 "On November 19, 2025 Site-to-Site VPN announced the VPN Concentrator, which lets customers connect up to 100 low-bandwidth sites through a single attachment to AWS Transit Gateway.",
 "What is the Site-to-Site VPN Concentrator and how many sites can connect to it?",
 [("new","up to 100 low-bandwidth sites","up to one hundred low-bandwidth sites")],"per VPN Concentrator","max",False,
 [ev(WN+"2025/11/aws-site-to-site-vpn-concentrator","With this launch, customers can now connect up to 100 low-bandwidth sites using a single VPN Concentrator to access their workloads in AWS. VPN Concentrator simplifies multi-site connectivity by allowing multiple remote sites to connect through a single attachment to AWS Transit Gateway, simplifying multi-site connectivity.")],
 tier=3,vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew'),cid('s2s','Site-to-Site VPN Concentrators','history')],exam="extended",bullets=["4.4.S7"],note="d12-011. Examinable but recent (Nov 2025)."))
F.append(fact("site-to-site-vpn-capability-concentrator-suitable-sites",S,"capability",
 "VPN Concentrator suits customers who need to connect 25+ remote sites to AWS, with each site needing low bandwidth (under 100 Mbps).",
 "When is a Site-to-Site VPN Concentrator the right choice?",
 [("sites","25+ remote sites","twenty-five or more remote sites"),("bw","under 100 Mbps","under one hundred megabits per second")],"per VPN Concentrator","min",False,
 [ev(VC,"VPN Concentrator is suitable for customers who need to connect 25\\+ remote sites to AWS, with each site needing low bandwidth (under 100 Mbps).")],
 vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew')],exam="extended",bullets=["4.4.S7"],note="d12-008"))
F.append(fact("site-to-site-vpn-limit-concentrator-aggregate-bandwidth",S,"limit",
 "Site-to-Site VPN Concentrators support 5 Gbps aggregate bandwidth and each site a maximum of 100 Mbps; for higher bandwidth you reach out to AWS Support.",
 "What bandwidth does a Site-to-Site VPN Concentrator support?",
 [("aggregate","5 Gbps aggregate bandwidth","five gigabits per second"),("site","maximum of 100 Mbps","one hundred megabits per second")],"per VPN Concentrator, and per site","max",True,
 [ev(VC,"Currently, Site-to-Site VPN Concentrators support 5 Gbps aggregate bandwidth. Each site can support a maximum of 100 Mbps bandwidth. However, if you need higher bandwidth, reach out to AWS Support.")],
 vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew')],exam="extended",bullets=["4.4.S7"],note="d12-008"))
F.append(fact("site-to-site-vpn-restriction-concentrator-transit-gateway-only",S,"restriction",
 "VPN Concentrators are supported only with Transit Gateway; this feature is not supported with Cloud WAN or a virtual private gateway.",
 "Which gateways support Site-to-Site VPN Concentrators?",
 [("rule","only supported with Transit Gateway","")],"per VPN Concentrator","fixed",False,
 [ev(VC,"VPN Concentrators are only supported with Transit Gateway. This feature is not supported with Cloud WAN or Virtual Private Gateway.")],
 vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew')],exam="extended",bullets=["4.4.S7"],note="d12-011. The quotas page row says 'per Transit Gateway or Cloud WAN'; recorded as a source disagreement."))
F.append(fact("site-to-site-vpn-restriction-concentrator-bgp-only",S,"restriction",
 "Site-to-Site VPN Concentrators support BGP routing only; static routing is not supported.",
 "Which routing does a Site-to-Site VPN Concentrator support?",
 [("rule","BGP (Border Gateway Protocol) routing only","")],"per VPN Concentrator","fixed",False,
 [ev(VC,"Site-to-Site VPN Concentrators support BGP (Border Gateway Protocol) routing only. Static routing is not supported.")],
 vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew')],exam="extended",bullets=["4.4.S7"],note="d12-011"))
F.append(fact("site-to-site-vpn-limit-concentrator-routes-per-site",S,"limit",
 "Each site connecting to a Site-to-Site VPN Concentrator can send a maximum of 5,000 routes from the transit gateway to a customer gateway and 1,000 routes from the customer gateway to the transit gateway.",
 "How many routes can each site of a VPN Concentrator exchange with the transit gateway?",
 [("tgw-to-cgw","5,000 routes","five thousand routes"),("cgw-to-tgw","1,000 routes","one thousand routes")],"per site connected to a VPN Concentrator","max",False,
 [ev(VC,"Each site connecting to the Site-to-Site VPN Concentrator can send a maximum of 5,000 routes from the transit gateway to a customer gateway and 1,000 routes from the customer gateway to the transit gateway.")],
 vol="frequently-changing",change_items=[cid('s2s','VPN Concentrator','whatsnew')],exam="reference",bullets=["3.4.S1"],note="d12-012"))
# defaults
F.append(fact("site-to-site-vpn-default-vgw-asn-64512",S,"default",
 "If you do not choose an ASN for the Amazon side of a virtual private gateway, then after June 30th 2018 Amazon provides an ASN of 64512.",
 "Which ASN does AWS assign to a virtual private gateway when you do not choose one?",
 [("default","ASN of 64512","six four five one two")],"per virtual private gateway","default",True,
 [ev("www/vpn/faqs","Amazon will provide an ASN for the virtual gateway if you don’t choose one. Until June 30th 2018, Amazon will continue to provide the “legacy public ASN” of the region. After June 30th 2018, Amazon will provide an ASN of 64512.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="d12-060. FAQ 102."))
F.append(fact("site-to-site-vpn-limit-vgw-private-asn-ranges",S,"limit",
 "For the Amazon side of a virtual private gateway you can choose any private ASN: 64512 to 65534 for 16-bit ASNs, or 4200000000 to 4294967294 for 32-bit ASNs.",
 "Which private ASN ranges can you choose for the Amazon side of a virtual private gateway?",
 [("16bit","64512 to 65534",""),("32bit","4200000000 and 4294967294","")],"per virtual private gateway","max",False,
 [ev("www/vpn/faqs","You can choose any private ASN. Ranges for 16-bit private ASNs include 64512 to 65534. You can also provide 32-bit ASNs between 4200000000 and 4294967294.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="d12-060. FAQ 100."))
# pricing
F.append(fact("site-to-site-vpn-pricing-5gbps-connection-hour",S,"pricing-dimension",
 "A Site-to-Site VPN 5Gbps connection is charged for each VPN connection-hour that it is provisioned and available, plus standard AWS data transfer charges for the data transferred via the VPN connection.",
 "What is a 5 Gbps Site-to-Site VPN connection charged for?",
 [("v","each VPN connection-hour","")],"per VPN connection","",False,
 [ev(PR,"If you create an AWS Site-to-Site VPN 5Gbps connection you are charged for each VPN connection-hour that your connection is provisioned and available. You also incur standard AWS data transfer charges for all data transferred via the VPN connection.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-025. The 5 Gbps connection has a higher hourly rate than the 1.25 Gbps connection; no amounts in the book."))
F.append(fact("site-to-site-vpn-pricing-concentrator-hours",S,"pricing-dimension",
 "A Site-to-Site VPN Concentrator is charged for each VPN Concentrator-hour that it is provisioned and available, and each VPN connection through the concentrator is also charged per connection-hour.",
 "What is a Site-to-Site VPN Concentrator charged for?",
 [("v","each VPN Concentrator-hour","")],"per VPN Concentrator","",False,
 [ev(PR,"If you create an AWS Site-to-Site VPN Concentrator you are charged for each VPN Concentrator-hour that your VPN Concentrator is provisioned and available. Additionally, you are also charged for each VPN connection-hour that your VPN connection (via VPN Concentrator) is provisioned and available.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-025"))
F.append(fact("site-to-site-vpn-pricing-accelerated-extra-charges",S,"pricing-dimension",
 "An accelerated Site-to-Site VPN connection pays the normal VPN connection price plus hourly charges for two Global Accelerators per VPN connection and Data Transfer Out Premium (DT-Premium) fees; non-accelerated VPNs have no Global Accelerator charges.",
 "What does an accelerated Site-to-Site VPN add to the price?",
 [("v","two Global Accelerators per VPN connection","")],"per accelerated VPN connection","",False,
 [ev(PR,"If you enable acceleration when creating an AWS Site-to-Site VPN connection to your Amazon VPC, Site-to-Site VPN connection pricing will apply as indicated above. You will also incur hourly charges for two Global Accelerators per VPN connection and Data Transfer Out Premium (DT-Premium) fees."),
  ev(PR,"You will not incur any AWS Global Accelerator charges for non-accelerated VPNs.")],
 tier=2,exam="core",bullets=["4.4.S2"],note="d12-025"))
F.append(fact("site-to-site-vpn-pricing-data-transfer-out-ec2-rates",S,"pricing-dimension",
 "Data transfer out on Site-to-Site VPN incurs data transfer out charges that the EC2 on-demand pricing page explains.",
 "How is data transfer out over Site-to-Site VPN charged?",
 [("v","data transfer out charges","")],"per gigabyte","",False,
 [ev(PR,"Data transfer out on AWS Site-to-Site VPN incurs data transfer out charges that are explained in the EC2 on-demand pricing page.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-025"))
F.append(fact("site-to-site-vpn-pricing-logs-no-extra-charge",S,"pricing-dimension",
 "There are no additional Site-to-Site VPN service-specific charges for enabling Site-to-Site VPN logs, but you pay standard CloudWatch charges for publishing the logs.",
 "Does enabling Site-to-Site VPN logs add a VPN charge?",
 [("v","no additional Site-to-Site VPN service-specific charges","")],"per VPN connection","",False,
 [ev(PR,"There are no additional Site-to-Site VPN service-specific charges for enabling Site-to-Site VPN logs. You will incur standard charges for using Amazon CloudWatch service (publishing Site-to-Site VPN logs to CloudWatch).")],
 tier=2,exam="reference",bullets=["4.4.S2"],note="d12-025"))
F.append(fact("site-to-site-vpn-pricing-public-ipv4-address-charge",S,"pricing-dimension",
 "Each Site-to-Site VPN connection uses a unique public IPv4 address for the tunnels, and you incur standard public IPv4 address charges on that address.",
 "Do Site-to-Site VPN connections incur public IPv4 address charges?",
 [("v","standard public IPv4 address charges","")],"per VPN connection","",False,
 [ev(PR,"Each Site-to-Site VPN connection uses unique public IPv4 address for the tunnels. You will incur standard public IPv4 address charges on the IPv4 address that will be used for the tunnels.")],
 tier=2,exam="reference",bullets=["4.4.S2"],note="d12-025"))
F.append(fact("site-to-site-vpn-pricing-transit-gateway-attachment-hourly",S,"pricing-dimension",
 "In the AWS pricing examples, a Site-to-Site VPN connection on a transit gateway also pays an hourly fee for the Transit Gateway attachment.",
 "Does a Site-to-Site VPN connection on a transit gateway also pay a transit gateway attachment fee?",
 [("v","hourly fee for creating AWS Transit Gateway attachment","")],"per transit gateway attachment","",False,
 [ev(PR,"AWS Transit Gateway fee: There is an hourly fee for creating AWS Transit Gateway attachment.")],
 tier=2,exam="extended",bullets=["4.4.S2"],note="d12-025. Pricing example text only."))
dump(F,"facts-changes-03.json")
