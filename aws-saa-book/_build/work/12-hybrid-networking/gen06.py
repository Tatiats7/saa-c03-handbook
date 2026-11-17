import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
D="direct-connect"
FAQ="www/directconnect/faqs"
CO="docs/directconnect/latest/UserGuide/connection_options"
VR="docs/directconnect/latest/UserGuide/vif-rate-limiters"
LG="docs/directconnect/latest/UserGuide/lags"
SLA="www/directconnect/sla"
PP="www/directconnect/pricing/pay-as-you-go"
F=[]
# FAQ numbers
F.append(fact("direct-connect-limit-bgp-session-down-over-100-routes",D,"limit",
 "A Direct Connect BGP session goes down if you advertise over 100 routes over it, which stops all network traffic over that virtual interface until you reduce the number of routes.",
 "What happens if you advertise more than 100 routes over a Direct Connect BGP session?",
 [("max","over 100 routes","over one hundred routes")],
 "per BGP session","max",True,
 [ev(FAQ,"Your Border Gateway Protocol session will go down if you advertise over 100 routes over a Border Gateway Protocol session. This will prevent all network traffic flowing over that virtual interface until you reduce the number of routes to less than 100.")],
 tier=2,exam="core",bullets=["3.4.S1"],note="d12-043. FAQ 91. The FAQ states no virtual interface type; the quotas page gives 100 for private/transit and 1,000 for public.",
 vol="frequently-changing",change_items=[cid('dx','inbound prefix controls')]))
F.append(fact("direct-connect-limit-tgw-dxgw-association-40-minutes",D,"limit",
 "It can take up to 40 minutes to establish an association between a transit gateway and a Direct Connect gateway.",
 "How long can it take to associate a transit gateway with a Direct Connect gateway?",
 [("max","up to 40 minutes","up to forty minutes")],
 "per association","max",False,
 [ev(FAQ,"It can take up to 40 minutes to establish an association between AWS Transit Gateway and AWS Direct Connect gateway.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="d12-042. FAQ 112."))
F.append(fact("direct-connect-limit-ecmp-multipath-16-next-hops",D,"limit",
 "AWS multipaths traffic to your network per prefix at up to 16 next-hops wide, where each next-hop is a unique AWS endpoint.",
 "How wide does AWS multipath traffic to your network over Direct Connect?",
 [("max","up to 16 next-hops wide","up to sixteen next-hops wide")],
 "per prefix","max",False,
 [ev(FAQ,"We will multipath per prefix at up to 16 next-hops wide, where each next-hop is a unique AWS endpoint.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="FAQ 153."))
F.append(fact("direct-connect-limit-failover-test-duration",D,"limit",
 "For the Direct Connect failover test, you can set the test duration from a minimum of 1 minute to a maximum of 180 minutes.",
 "What minimum and maximum duration can you set for a Direct Connect failover test?",
 [("min","1 minute","one minute"),("max","180 minutes","one hundred eighty minutes")],
 "per failover test","max",True,
 [ev(FAQ,"Yes, you can configure the duration of the test by setting the minimum and maximum duration for the test to be 1 minute and 180 minutes, respectively.")],
 tier=2,exam="reference",bullets=["1.2.S4"],note="FAQ 25."))
F.append(fact("direct-connect-limit-failover-test-history-365-days",D,"limit",
 "AWS preserves the Direct Connect failover test history for 365 days, and deleting the virtual interface also deletes its test history.",
 "How long does Direct Connect keep failover test history?",
 [("max","365 days","three hundred sixty-five days")],
 "per virtual interface","max",False,
 [ev(FAQ,"We preserve your test history for 365 days. If you delete the virtual interface, your test history is also deleted.")],
 tier=2,exam="reference",bullets=["1.2.S4"],note="FAQ 26."))
F.append(fact("direct-connect-default-dxgw-asn-64512",D,"default",
 "If you do not choose an ASN for the AWS side of the BGP session, AWS provides an ASN of 64512 for the Direct Connect gateway.",
 "Which ASN does AWS give a Direct Connect gateway when you do not choose one?",
 [("default","ASN of 64512","six four five one two")],
 "per Direct Connect gateway","default",True,
 [ev(FAQ,"AWS will provide an ASN of 64512 for the AWS Direct Connect gateway if you don't choose one.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="d12-060. FAQ 164."))
F.append(fact("direct-connect-limit-private-asn-ranges",D,"limit",
 "For the AWS side of a Direct Connect gateway you can choose any private ASN: 64512 to 65534 for 16-bit ASNs, or 4200000000 to 4294967294 for 32-bit ASNs.",
 "Which private ASN ranges can you choose for the AWS side of a Direct Connect gateway?",
 [("16bit","64512 to 65534","six four five one two to six five five three four"),("32bit","4200000000 and 4294967294","")],
 "per Direct Connect gateway","max",False,
 [ev(FAQ,"You can choose any private ASN. Ranges for 16-bit private ASNs include 64512 to 65534. You can also provide 32-bit ASNs between 4200000000 and 4294967294.")],
 tier=2,exam="reference",bullets=["3.4.S1"],note="d12-060. FAQ 162."))
F.append(fact("direct-connect-limit-no-data-transfer-cap",D,"limit",
 "There is no limit on the amount of data you can transfer over Direct Connect other than the capacity of your selected port.",
 "Are there limits on the amount of data you can transfer using Direct Connect?",
 [("rule","any amount of data up to the limit of your selected port capacity","")],
 "per connection","max",False,
 [ev(FAQ,"No. You may transfer any amount of data up to the limit of your selected port capacity.")],
 tier=2,exam="reference",bullets=["4.4.S7"],note="FAQ 89."))
# LAG + rate limiters
F.append(fact("direct-connect-default-lag-minimum-links-0",D,"default",
 "New LAGs have the minimum-links attribute set to 0 by default; a higher value makes the whole LAG non-operational when fewer connections than that are operational.",
 "What is the default minimum links value of a new LAG?",
 [("default","set to 0","zero")],
 "per link aggregation group (LAG)","default",True,
 [ev(LG,"All LAGs have an attribute that determines the minimum number of connections in the LAG that must be operational for the LAG itself to be operational. By default, new LAGs have this attribute set to 0. You can update your LAG to specify a different value—doing so means that your entire LAG becomes non-operational if the number of operational connections falls below this threshold.")],
 exam="reference",bullets=["4.4.S7"],note="d12-045"))
F.append(fact("direct-connect-limit-rate-limiter-range-1g",D,"limit",
 "On a 1 Gbps dedicated connection you can set VIF rate limiters between 50 Mbps and 1 Gbps; on a LAG of 2 x 1 Gbps connections the range is 50 Mbps to 2 Gbps.",
 "Which bandwidth range can a VIF rate limiter have on a 1 Gbps dedicated connection?",
 [("min","50 Mbps","fifty megabits per second"),("max-1g","1 Gbps","one gigabit per second")],
 "per VIF rate limiter","max",True,
 [ev(VR,"On a 1 Gbps Dedicated connection, you can set Rate Limiters between 50 Mbps and 1 Gbps.\nOn a LAG combining 2×1 Gbps connections, you can set Rate Limiters between 50 Mbps and 2 Gbps.")],
 exam="reference",bullets=["4.4.S7"],note="d12-073",vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')]))
F.append(fact("direct-connect-limit-rate-limiters-10-per-dedicated",D,"limit",
 "Each Direct Connect dedicated connection supports up to 10 VIF rate limiters, and you can request an increase through AWS Service Quotas.",
 "How many VIF rate limiters does a dedicated connection support?",
 [("max","10 rate limiters","ten rate limiters")],
 "per dedicated connection","max",True,
 [ev(VR,"Each dedicated connection supports up to **10 rate limiters**. You can request a limit increase through AWS Service Quotas.")],
 exam="reference",bullets=["4.4.S7"],note="d12-073. The quotas page row says contact your Solutions Architect or Technical Account Manager; this page says Service Quotas.",vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')]))
# SLA
F.append(fact("direct-connect-sla-maximum-resiliency-99-99",D,"sla",
 "The Maximum Resiliency model of the Direct Connect Resiliency Toolkit lets you order dedicated connections to achieve an SLA of 99.99%, if you meet all requirements of the Direct Connect Service Level Agreement.",
 "Which availability SLA does the Direct Connect Maximum Resiliency model target?",
 [("sla","SLA of 99.99%","ninety-nine point nine nine percent")],
 "per Maximum Resiliency deployment","fixed",False,
 [ev(CO,"**Maximum Resiliency**: This model is available in the AWS Direct Connect Resiliency Toolkit and provides you a way to order dedicated connections to achieve an SLA of 99.99%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/).")],
 exam="core",tier0=True,bullets=["1.2.S4"],note="d12-047. The SLA page (updated 2026-07-24) names the deployments Multi-Site Redundant and Multi-Site Non-Redundant."))
F.append(fact("direct-connect-sla-high-resiliency-99-9",D,"sla",
 "The High Resiliency model of the Direct Connect Resiliency Toolkit lets you order dedicated connections to achieve an SLA of 99.9%, if you meet all requirements of the Direct Connect Service Level Agreement.",
 "Which availability SLA does the Direct Connect High Resiliency model target?",
 [("sla","SLA of 99.9%","ninety-nine point nine percent")],
 "per High Resiliency deployment","fixed",False,
 [ev(CO,"**High Resiliency**: This model is available in the AWS Direct Connect Resiliency Toolkit and provides you a way to order dedicated connections to achieve an SLA of 99.9%. It requires you to meet all of the requirements for achieving the SLA that are specified in the [Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/).")],
 exam="core",tier0=True,bullets=["1.2.S4"],note="d12-047"))
F.append(fact("direct-connect-sla-classic-95",D,"sla",
 "A Classic Direct Connect connection has a 95% SLA but does not provide resiliency or redundancy.",
 "Which SLA applies to a Classic Direct Connect connection?",
 [("sla","95% SLA","ninety-five percent")],
 "per Classic connection","fixed",False,
 [ev(CO,"**Classic**: A Classic connection creates a connection without the need of the AWS Direct Connect Resiliency Toolkit. It's intended for users that have existing connections and want to add additional connections without using the toolkit. This model has a 95% SLA but does not provide resiliency or redundancy.")],
 exam="extended",bullets=["1.2.S4"],note="d12-047"))
F.append(fact("direct-connect-sla-multi-site-redundant-definition",D,"sla",
 "A Multi-Site Redundant Deployment has at least four Connections across at least two Direct Connect locations, with at least two in each location and each on a unique AWS device; it needs an Enterprise Support plan and a completed Well-Architected Review.",
 "What does the Direct Connect SLA require for a Multi-Site Redundant Deployment?",
 [("min","at least four Connections","at least four")],
 "per deployment","min",False,
 [ev(SLA,"Multi-Site Redundant Deployment is a Deployment that comprises at least four Connections deployed across a minimum of two different Direct Connect locations, each of which is configured to access the same Endpoint, where no fewer than two Connections are deployed in each of the two Direct Connection locations, each Connection is on a unique AWS device, and, with respect to private Endpoints, the Endpoint is deployed in two or more Availability Zones. You must have an Enterprise Support plan in place for any Multi-Site Redundant Deployment and have completed a “Well-Architected Review” with an AWS Solutions Architect.")],
 exam="core",bullets=["1.2.S4"],note="d12-047. The SLA page was last updated 2026-07-24."))
F.append(fact("direct-connect-sla-multi-site-non-redundant-definition",D,"sla",
 "A Multi-Site Non-Redundant Deployment has at least two Connections across at least two different Direct Connect locations and needs an Enterprise Support plan.",
 "What does the Direct Connect SLA require for a Multi-Site Non-Redundant Deployment?",
 [("min","at least two Connections","at least two")],
 "per deployment","min",False,
 [ev(SLA,"Multi-Site Non-Redundant Deployment is a Deployment that comprises at least two Connections deployed across a minimum of two different Direct Connect locations, each of which is configured to access the same Endpoint, and, with respect to private Endpoints, the Endpoint is deployed in two or more Availability Zones. You must have an Enterprise Support plan in place for any Multi-Site Non-Redundant Deployment.")],
 exam="core",bullets=["1.2.S4"],note="d12-047"))
F.append(fact("direct-connect-sla-three-commitments",D,"sla",
 "AWS makes three SLA commitments for Direct Connect: a Multi-Site Redundant SLA, a Multi-Site Non-Redundant SLA, and a Single Connection SLA for individual Connections.",
 "Which SLA commitments does AWS make for Direct Connect?",
 [("count","three SLA commitments","three")],
 "per account","fixed",False,
 [ev(SLA,"AWS makes three SLA commitments for AWS Direct Connect: (1) a Multi-Site Redundant SLA that governs Multi-Site Redundant Deployments; (2) a Multi-Site Non-Redundant SLA that governs Multi-Site Non-Redundant Deployments; and (3) a Single Connection SLA that governs individual Connections.")],
 vol="frequently-changing",exam="core",bullets=["1.2.S4"],note="d12-047. SLA page last updated 2026-07-24."))
F.append(fact("direct-connect-sla-unavailable-120-seconds",D,"sla",
 "In the Direct Connect SLA, a Deployment or Connection is Unavailable after the complete inability to send or receive data through it for at least 120 consecutive seconds.",
 "How long must a Direct Connect outage last to count as Unavailable under the SLA?",
 [("min","at least 120 consecutive seconds","at least one hundred twenty consecutive seconds")],
 "per Deployment or Connection","min",False,
 [ev(SLA,"“Unavailable” or “Unavailability” means (i) for a given Deployment, the complete inability to send data to or receive data from the associated Endpoint through all Connections in the Deployment for at least 120 consecutive seconds or (ii) for a given Connection, the complete inability to send data to or receive data from the associated Endpoint through the Connection for at least 120 consecutive seconds.")],
 exam="reference",bullets=["1.2.S4"],note="d12-047"))
F.append(fact("direct-connect-sla-not-for-hosted",D,"sla",
 "The Direct Connect SLAs do not apply to services accessed through an APN Direct Connect Partner using hosted connections or hosted virtual interfaces; they apply to dedicated connections owned by your AWS account.",
 "Do the Direct Connect SLAs cover hosted connections?",
 [("rule","do not apply","")],
 "per connection","fixed",False,
 [ev(SLA,"Furthermore, the SLAs do not apply to AWS Direct Connect services accessed via an AWS Partner Network (APN) Direct Connect Partner integration using either a hosted connection or hosted virtual interfaces. The SLAs apply to dedicated connections that you access via services provided by an APN Direct Connect Partner, provided such dedicated connections are owned by your AWS account.")],
 exam="core",bullets=["1.2.S4"],note="d12-047"))
dump(F,"facts-numbers-06.json")
