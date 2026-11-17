import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
D="direct-connect"
AB="docs/directconnect/latest/UserGuide/AboutThisGuide"
HH="| Change | Description | Date |"
PC="docs/directconnect/latest/UserGuide/prefix-controls"
FR="docs/directconnect/latest/UserGuide/flat-rate-connections"
VR="docs/directconnect/latest/UserGuide/vif-rate-limiters"
BV="docs/directconnect/latest/UserGuide/bgp-route-visibility"
WN="www/about-aws/whats-new/"
F=[]
NY=" Not examinable yet (GA after 2026-07-15): label as not examinable yet."
# --- prefix controls
F.append(fact("direct-connect-change-prefix-controls",D,"change",
 "Inbound prefix controls (announced 2026-08-20) let you allocate up to 1,000 prefixes each for IPv4 and IPv6 on a private or transit virtual interface; before, a VIF accepted a maximum of 100 route prefixes. The default allocation stays 100.",
 "What changed in how many routes a Direct Connect private or transit virtual interface accepts?",
 [("new","up to 1,000 prefixes each for IPv4 and IPv6","")],
 "per private or transit virtual interface","max",True,
 [ev(WN+"2026/08/aws-direct-connect-new-prefix-controls","Previously, Direct Connect VIFs accepted a maximum of 100 route prefixes advertised from your on-premises network to AWS on a private or transit VIF."),
  ev(WN+"2026/08/aws-direct-connect-new-prefix-controls","You can now allocate up to 1,000 prefixes each for IPv4 and IPv6 on your VIFs on dedicated and hosted connections."),
  ev(PC,"If you don't select any value, AWS applies the default allocation of 100 prefixes per address family.")],
 tier=3,vol="changed-since-2022",changed={"date":"2026-08-20","was":"a maximum of 100 route prefixes","was_evidence":0},
 change_items=[cid('dx','inbound prefix controls')],exam="extended",bullets=["3.4.S1"],
 note="d12-072."+NY+" Current-truth numbers fact: direct-connect-quota-routes-per-bgp-session-private-transit (examinable answer 100)."))
for fid,kind,claim,q,disp,sp,scope,dm,quote in [
 ("direct-connect-limit-prefix-controls-default-allocation","default","With inbound prefix controls, the default allocation per virtual interface is 100 per address family (IPv4 and IPv6).","What is the default prefix allocation per VIF with inbound prefix controls?","100 per address family","one hundred per address family","per virtual interface","default","| Default allocation per VIF | 100 per address family (IPv4 and IPv6) |"),
 ("direct-connect-limit-prefix-controls-max-allocation","limit","With inbound prefix controls, the maximum allocation per virtual interface is 1,000 per address family (IPv4 and IPv6).","What is the maximum prefix allocation per VIF with inbound prefix controls?","1,000 per address family","one thousand per address family","per virtual interface","max","| Maximum allocation per VIF | 1,000 per address family (IPv4 and IPv6) |"),
 ("direct-connect-limit-prefix-controls-dxgw-total","limit","With inbound prefix controls, total allocations per Direct Connect gateway are 10,000, counting IPv4 and IPv6 together.","What is the total prefix allocation limit per Direct Connect gateway?","10,000 combined","ten thousand combined","per Direct Connect gateway","max","| Total allocations per DXGW | 10,000 (combined IPv4 \\+ IPv6) |"),
 ("direct-connect-limit-prefix-controls-pool-per-connection","limit","With inbound prefix controls, the prefix pool per dedicated connection is 5,000 for 1 and 10 Gbps, 30,000 for 100 Gbps and 50,000 for 400 Gbps.","What is the inbound prefix pool of a dedicated connection by speed?","5,000 (1/10 Gbps), 30,000 (100 Gbps), 50,000 (400 Gbps)","five thousand, thirty thousand and fifty thousand","per dedicated connection","max","| Prefix pool per dedicated connection | 5,000 (1/10 Gbps), 30,000 (100 Gbps), 50,000 (400 Gbps) |")]:
    F.append(fact(fid,D,kind,claim,q,[("v",disp,sp)],scope,dm,True,[ev(PC,quote,"| Limit | Value |")],
      cond="inbound prefix controls apply to private and transit virtual interfaces",tier=1,vol="frequently-changing",change_items=[cid('dx','inbound prefix controls')],exam="reference",bullets=["3.4.S1"],note="d12-072."+NY))
F.append(fact("direct-connect-limit-prefix-controls-public-vif-1000",D,"limit",
 "Public virtual interfaces are not managed by inbound prefix controls and keep the existing limit of 1,000 inbound prefixes.",
 "Do inbound prefix controls change the 1,000 inbound prefix limit of a public virtual interface?",
 [("v","1,000 inbound prefixes","one thousand inbound prefixes")],"per public virtual interface","max",False,
 [ev(PC,"Public VIFs are not managed by inbound prefix controls. Public VIFs retain the existing limit of 1,000 inbound prefixes.")],
 vol="frequently-changing",change_items=[cid('dx','inbound prefix controls')],exam="reference",bullets=["3.4.S1"],note="d12-043."+NY))
# --- rate limiters
F.append(fact("direct-connect-change-vif-rate-limiters",D,"change",
 "VIF Rate Limiters (announced June 2026) let you set a maximum bandwidth for up to 10 VIFs on a dedicated connection, with increments from 50 Mbps to 1.6 Tbps when using a link aggregation group.",
 "What do Direct Connect VIF Rate Limiters do and how many VIFs can have one?",
 [("max","up to 10 VIFs","up to ten VIFs"),("range","50 Mbps to 1.6 Tbps","fifty megabits per second to one point six terabits per second")],
 "per dedicated connection","max",True,
 [ev(WN+"2026/06/aws-direct-connect-now-supports-vif-rate-limiters","With VIF Rate Limiters, you can set a maximum bandwidth allocation for up to 10 VIFs on a dedicated connection, choosing from a wide range available capacity increments from 50 Mbps to 1.6 Tbps when using a link aggregation group."),
  ev(VR,"Use virtual interface (VIF) Rate Limiters to set a maximum bandwidth allocation for individual VIFs on a Direct Connect Dedicated connection.")],
 tier=3,vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')],exam="extended",bullets=["4.4.S7"],
 note="d12-073. Posted 2026-06-01; examinable but recent: label Changed recently."))
F.append(fact("direct-connect-restriction-rate-limiters-dedicated-only",D,"restriction",
 "VIF Rate Limiters are supported only on dedicated connections, not on hosted connections; hosted connections are always rate-limited to the purchased capacity.",
 "Which Direct Connect connection types support VIF Rate Limiters?",
 [("rule","only supported on Dedicated connections","")],"per connection","fixed",False,
 [ev(VR,"This feature is only supported on Dedicated connections. Hosted connections are always rate-limited to the purchased capacity.")],
 vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')],exam="extended",bullets=["4.4.S7"],note="d12-073"))
F.append(fact("direct-connect-default-vifs-use-100-percent-capacity",D,"default",
 "By default, all VIFs on a Direct Connect connection can use 100% of the underlying connection's capacity, which is why one VIF can congest the others.",
 "How much of a connection can one VIF use by default when no rate limiter is applied?",
 [("default","100%","one hundred percent")],"per VIF","default",True,
 [ev(VR,"By default, all VIFs on a connection can utilize 100% of the underlying connection's capacity. This means that a workload on one VIF can unexpectedly increase its utilization, causing congestion, packet loss, and potential disruption to workloads on other VIFs on that connection.")],
 vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')],exam="extended",bullets=["4.4.S7"],note="d12-073"))
# --- flat rate
F.append(fact("direct-connect-change-flat-rate-billing",D,"change",
 "On September 15, 2026 Direct Connect added flat-rate billing for dedicated connections: for 10 Gbps and 100 Gbps connections it gives a single fixed monthly price that eliminates data transfer out charges within the selected pricing tier. Before, billing was pay-as-you-go.",
 "What is Direct Connect flat-rate billing and what did it change?",
 [("new","single fixed monthly price","")],"per dedicated connection","fixed",True,
 [ev(AB,"| [Flat-rate billing for dedicated connections](#AboutThisGuide) | Direct Connect now supports flat-rate billing, a fixed-price billing mode for dedicated connections that you set per connection. For more information, see [Flat-rate billing for dedicated connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/flat-rate-connections.html). | September 15, 2026 |",HH),
  ev(WN+"2026/09/aws-direct-connect-announces-flat-rate-pricing","Flat-rate pricing for 10 Gbps and 100 Gbps dedicated connections introduces a single fixed monthly price that eliminates DTO charges within the selected pricing tier."),
  ev(WN+"2026/09/aws-direct-connect-announces-flat-rate-pricing","Customers value the flexibility of AWS Direct Connect's pay-as-you-go pricing, paying only for the port hours and data transfer out (DTO) they use, with no upfront commitment or long-term contracts.")],
 tier=3,vol="changed-since-2022",changed={"date":"2026-09-15","was":"pay-as-you-go pricing, paying only for the port hours and data transfer out (DTO) they use","was_evidence":2},
 change_items=[cid('dx','flat-rate pricing','whatsnew'),cid('dx','Flat-rate billing','history')],exam="reference",bullets=["4.4.S2"],
 note="d12-074."+NY+" Pay-as-you-go stays available; flat-rate is a per-connection billing mode."))
F.append(fact("direct-connect-restriction-flat-rate-dedicated-only",D,"restriction",
 "Flat-rate billing applies to dedicated connections only; hosted connections provisioned by a Direct Connect partner are not eligible.",
 "Which Direct Connect connections can use flat-rate billing?",
 [("rule","dedicated connections only","")],"per connection","fixed",False,
 [ev(FR,"Flat-rate billing applies to **dedicated** connections only. Hosted connections provisioned by a Direct Connect partner are not eligible.")],
 vol="frequently-changing",change_items=[cid('dx','flat-rate pricing','whatsnew')],exam="reference",bullets=["4.4.S2"],note="d12-074."+NY))
F.append(fact("direct-connect-behavior-flat-rate-port-pair-no-extra-bandwidth",D,"behavior",
 "In flat-rate billing the second port of a port-pair exists solely for redundancy and does not add throughput; a 10 Gbps port-pair gives 10 Gbps of usable capacity, not 20 Gbps.",
 "Does the second port of a flat-rate port-pair double the bandwidth?",
 [("rule","10 Gbps, not 20 Gbps","ten gigabits per second, not twenty")],"per port-pair","fixed",False,
 [ev(FR,"The usable capacity that you purchase is the capacity of a **single** port. The second port exists solely for redundancy and does not add throughput. For example, a 10 Gbps port-pair at any Direct Connect location gives you an effective usable capacity of **10 Gbps, not 20 Gbps**.")],
 vol="frequently-changing",change_items=[cid('dx','flat-rate pricing','whatsnew')],exam="reference",bullets=["4.4.S2"],note="d12-074."+NY))
F.append(fact("direct-connect-pricing-flat-rate-second-port-included",D,"pricing-dimension",
 "With flat-rate pricing the second connection of a port-pair is included at no additional charge.",
 "Is the second port of a flat-rate port-pair charged?",
 [("rule","included at no additional charge","")],"per port-pair","fixed",False,
 [ev(WN+"2026/09/aws-direct-connect-announces-flat-rate-pricing","One connection carries your traffic while the other stands by for redundancy. The second connection is included at no additional charge.")],
 tier=3,vol="frequently-changing",change_items=[cid('dx','flat-rate pricing','whatsnew')],exam="reference",bullets=["4.4.S2"],note="d12-074."+NY))
# --- bgp visibility
F.append(fact("direct-connect-change-bgp-route-visibility",D,"change",
 "On July 30, 2026 Direct Connect added BGP route visibility: you can view the BGP routes AWS accepted from your router and the routes AWS advertises to you on your virtual interfaces.",
 "What does Direct Connect BGP route visibility show?",
 [("new","BGP route visibility","")],"per virtual interface","fixed",False,
 [ev(AB,"| [BGP route visibility](#AboutThisGuide) | You can now view the BGP routes that AWS has accepted from your router and the routes that AWS is advertising to you on your Direct Connect virtual interfaces. For more information, see [BGP route visibility](https://docs.aws.amazon.com/directconnect/latest/UserGuide/bgp-route-visibility.html). | July 30, 2026 |",HH)],
 tier=3,vol="frequently-changing",change_items=[cid('dx','BGP route visibility','history')],exam="reference",bullets=["3.4.S1"],note="d12-075."+NY))
# --- long ASN
F.append(fact("direct-connect-change-4-byte-asn",D,"change",
 "Direct Connect virtual interfaces support 4-byte AS numbers, using the entire range supported by RFC 6793 up to 4,294,967,294; before, the limit was 65,536 possible 2-byte AS numbers.",
 "What changed about the AS numbers you can use on Direct Connect virtual interfaces?",
 [("new","up to 4,294,967,294","")],"per virtual interface","max",False,
 [ev(WN+"2025/09/aws-direct-connect-4-byte-autonomous-system-numbers","With 4-byte AS numbers, customers can now use the entire range supported by RFC 6793, up to 4,294,967,294."),
  ev(WN+"2025/09/aws-direct-connect-4-byte-autonomous-system-numbers","However, customers with complex, multi-tenant network topologies or who need to maintain consistent AS numbering across their entire network can run into challenges with the maximum limit of 65,536 possible 2-byte AS numbers.")],
 tier=3,vol="changed-since-2022",changed={"date":"2025-09-12","was":"65,536 possible 2-byte AS numbers","was_evidence":1},
 change_items=[cid('dx','4-byte Autonomous System'),cid('dx','long ASN')],exam="reference",bullets=["3.4.S1"],note="d12-077. Documentation history row 2025-07-24 'Support for long ASN'."))
# --- 400G and cloud wan association (history rows)
F.append(fact("direct-connect-change-400g-dedicated",D,"change",
 "On July 18, 2024 the Direct Connect guide added support for 400G connections; 400 Gbps is now a dedicated connection speed beside 1, 10 and 100 Gbps.",
 "When did Direct Connect add 400 Gbps dedicated connections?",
 [("new","400G","four hundred gigabits")],"per dedicated connection","fixed",False,
 [ev(AB,"| [Support for 400G](#AboutThisGuide) | Updated topics to include support for 400G connections. | July 18, 2024 |",HH)],
 tier=3,vol="frequently-changing",change_items=[cid('dx','Support for 400G','history'),cid('dx','native 400 Gbps','whatsnew')],exam="extended",bullets=["4.4.S7"],
 note="d12-070. Current-truth fact: direct-connect-limit-dedicated-port-speeds. The old speeds are not stated verbatim in the history row."))
F.append(fact("direct-connect-change-cloud-wan-association",D,"change",
 "On November 25, 2024 Direct Connect added the option to create a Direct Connect gateway association directly with an AWS Cloud WAN core network.",
 "Since when can a Direct Connect gateway associate directly with a Cloud WAN core network?",
 [("new","AWS Network Manager core network","")],"per Direct Connect gateway","fixed",False,
 [ev(AB,"| [Create an association between Direct Connect gateway and an AWS Network Manager core network](#AboutThisGuide) | You can now create a Direct Connect gateway association directly between Direct Connect and an AWS Cloud WAN core network. | November 25, 2024 |",HH)],
 tier=3,vol="frequently-changing",change_items=[cid('dx','AWS Network Manager core network')],exam="reference",bullets=["3.4.S1"],note="Triaged from the document history."))
# --- interconnect
F.append(fact("direct-connect-change-interconnect-last-mile-ga",D,"change",
 "AWS Interconnect - last mile became generally available on April 13, 2026 as a fully managed way to connect branch offices, data centers and remote locations to AWS.",
 "What is AWS Interconnect - last mile?",
 [("name","AWS Interconnect - last mile","")],"per account","fixed",False,
 [ev(WN+"2026/04/aws-announces-ga-AWS-interconnect-last-mile","AWS launches AWS Interconnect - last mile, a fully managed connectivity offering that allows customers to connect their branch offices, data centers, and remote locations to AWS with just a few clicks, eliminating the friction and complexity of network setup.")],
 tier=3,vol="frequently-changing",change_items=[cid('dx','general availability of AWS Interconnect - last mile')],exam="reference",bullets=["3.4.K4"],note="d12-076. Recognition only; GA 2026-04-13, before the 2026-07-15 cut."))
F.append(fact("direct-connect-change-interconnect-multicloud-ga",D,"change",
 "AWS Interconnect - multicloud became generally available on April 14, 2026, providing private, high-speed connections to other cloud service providers.",
 "What is AWS Interconnect - multicloud?",
 [("name","AWS Interconnect - multicloud","")],"per account","fixed",False,
 [ev(WN+"2026/04/aws-announces-ga-AWS-interconnect-multicloud","AWS announces general availability (GA) of AWS Interconnect - multicloud, providing simple, resilient, high-speed private connections to other cloud service providers (CSPs).")],
 tier=3,vol="frequently-changing",change_items=[cid('dx','general availability of AWS Interconnect - multicloud')],exam="reference",bullets=["3.4.K4"],note="d12-076. Recognition only; GA 2026-04-14. Azure and OCI partners arrive later in 2026 (OCI GA 2026-07-29; Azure preview 2026-08-31, not examinable yet)."))
dump(F,"facts-changes-01.json")
