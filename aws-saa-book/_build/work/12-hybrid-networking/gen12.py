import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
S="site-to-site-vpn"; D="direct-connect"
F=[]
F.append(fact("site-to-site-vpn-default-vgw-asn-64512-guide",S,"default",
 "If you do not specify an ASN when you create a virtual private gateway, it is created with the default ASN 64512, and you cannot change the ASN afterwards.",
 "Which ASN does a virtual private gateway get by default, and can it be changed?",
 [("default","default ASN (64512)","six four five one two")],"per virtual private gateway","default",False,
 [ev("docs/vpn/latest/s2svpn/how_it_works","If you don't specify an ASN, the virtual private gateway is created with the default ASN (64512). You cannot change the ASN after you've created the virtual private gateway.")],
 exam="reference",bullets=["3.4.S1"],note="d12-060. Guide page; the FAQ fact site-to-site-vpn-default-vgw-asn-64512 agrees."))
F.append(fact("site-to-site-vpn-limit-private-ip-vpn-route-scale",S,"limit",
 "Private IP VPN connections offer higher route limits (5000 outbound routes and 1000 inbound routes) than Direct Connect alone, which currently has a limit of 200 outbound and 100 inbound routes.",
 "How do the route limits of a private IP VPN compare with Direct Connect alone?",
 [("vpn-out","5000 outbound routes","five thousand outbound routes"),("vpn-in","1000 inbound routes","one thousand inbound routes"),("dx-out","200 outbound","two hundred outbound"),("dx-in","100 inbound","one hundred inbound")],
 "per private IP VPN connection","max",False,
 [ev("docs/vpn/latest/s2svpn/private-ip-dx","**Higher route scale:** Private IP VPN connections offer higher route limits (5000 outbound routes and 1000 inbound routes) as compared to Direct Connect alone, which currently has a limit of 200 outbound and 100 inbound routes.")],
 exam="extended",bullets=["3.4.S1"],note="d12-012, d12-043"))
F.append(fact("site-to-site-vpn-limit-cloudwatch-metrics-15-months",S,"limit",
 "CloudWatch statistics for Site-to-Site VPN tunnels are recorded for a period of 15 months.",
 "How long are Site-to-Site VPN CloudWatch statistics recorded?",
 [("max","15 months","fifteen months")],"per VPN tunnel","max",False,
 [ev("docs/vpn/latest/s2svpn/monitoring-cloudwatch-vpn","These statistics are recorded for a period of 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing.")],
 exam="reference",bullets=["1.2.S4"],note="Triaged from the monitoring page."))
F.append(fact("site-to-site-vpn-capability-logs-to-cloudwatch-logs",S,"capability",
 "Site-to-Site VPN logs give details on IPsec tunnel establishment, IKE negotiations, DPD protocol messages and BGP status and routing updates, and can be published to Amazon CloudWatch Logs.",
 "Where can Site-to-Site VPN connection logs be published?",
 [("rule","published to Amazon CloudWatch Logs","")],"per VPN connection","",True,
 [ev("docs/vpn/latest/s2svpn/monitoring-logs","AWS Site-to-Site VPN logs provide you with deeper visibility into your Site-to-Site VPN deployments. With this feature, you have access to Site-to-Site VPN connection logs that provide details on IP Security (IPsec) tunnel establishment, Internet Key Exchange (IKE) negotiations, dead peer detection (DPD) protocol messages, Border Gateway protocol (BGP) status and routing updates."),
  ev("docs/vpn/latest/s2svpn/monitoring-logs","Site-to-Site VPN logs can be published to Amazon CloudWatch Logs.")],
 vol="frequently-changing",change_items=[cid('s2s','connection logs using Amazon CloudWatch'),cid('s2s','BGP logging')],exam="reference",bullets=["1.2.S4"],note="d12-079. Launched 2022-08-19 (feed pointer; the What's New post is blocked by robots.txt)."))
F.append(fact("direct-connect-limit-maintenance-notice-14-days",D,"limit",
 "Planned Direct Connect maintenance events are scheduled 14 days in advance and typically occur during a four-hour window in low-traffic hours at the Direct Connect location.",
 "How far in advance is planned Direct Connect maintenance scheduled and how long is the window?",
 [("notice","14 days in advance","fourteen days in advance"),("window","four-hour window","four-hour window")],
 "per maintenance event","fixed",False,
 [ev("docs/directconnect/latest/UserGuide/dx-maintenance","These maintenance events are scheduled 14 days in advance and typically occur during a four-hour window in low-traffic hours at the Direct Connect location where the device endpoint resides.")],
 exam="reference",bullets=["1.2.S4"],note="Triaged from the maintenance page."))
F.append(fact("direct-connect-limit-loa-cfa-expires-90-days",D,"limit",
 "If the cross connect is not completed within 90 days, the authority granted by the LOA-CFA expires, and you can download it again from the Direct Connect console.",
 "How long is a Direct Connect LOA-CFA valid for the cross connect?",
 [("max","within 90 days","within ninety days")],"per LOA-CFA","max",False,
 [ev("docs/directconnect/latest/UserGuide/Colocation","If the cross connect is not completed within 90 days, the authority granted by the LOA-CFA expires. To renew a LOA-CFA that has expired, you can download it again from the Direct Connect console.")],
 exam="reference",bullets=["4.4.S7"],note="Triaged from the colocation page."))
F.append(fact("direct-connect-default-cloudwatch-5-minute-interval",D,"default",
 "By default, CloudWatch provides Direct Connect metric data in 5-minute intervals.",
 "What is the default CloudWatch interval for Direct Connect metrics?",
 [("default","5-minute intervals","five-minute intervals")],"per metric","default",True,
 [ev("docs/directconnect/latest/UserGuide/monitoring-cloudwatch","By default, CloudWatch provides Direct Connect metric data in 5-minute intervals.")],
 exam="reference",bullets=["1.2.S4"],note="Triaged from the monitoring page."))
F.append(fact("direct-connect-sla-whitepaper-formal-sla-recommended",D,"sla",
 "Direct Connect offers a formal SLA with service credits calculated as a percentage of port hour charges, and the hybrid connectivity whitepaper calls it the recommended transport if an SLA is required.",
 "Which hybrid transport does AWS recommend when an SLA with service credits is required?",
 [("rule","the recommended transport if an SLA is required","")],"per account","fixed",False,
 [ev("docs/whitepapers/latest/hybrid-connectivity/service-level-agreement-sla","AWS [Direct Connect offers a formal SLA](https://aws.amazon.com/directconnect/sla/) with service credits calculated as a percentage of the total AWS Direct Connect Port Hour charges paid by you for the applicable connections experiencing unavailability for the monthly billing cycle in which the SLA was not met. This is the recommended transport if an SLA is required.")],
 tier=2,exam="extended",bullets=["1.2.S4"],note="d12-047. Historical-reference whitepaper: decision reasoning only."))
F.append(fact("direct-connect-sla-whitepaper-responsibility-ends-at-port",D,"sla",
 "The AWS responsibility for Direct Connect ends at the Direct Connect location at the Direct Connect port; once AWS hands traffic off to your network, it is no longer the responsibility of AWS.",
 "Where does the AWS responsibility end for a Direct Connect connection?",
 [("rule","ends at the AWS Direct Connect location at the AWS Direct Connect port","")],"per connection","fixed",False,
 [ev("docs/whitepapers/latest/hybrid-connectivity/service-level-agreement-sla","The AWS responsibility ends at the AWS Direct Connect location at the AWS Direct Connect port. Once AWS hands traffic off to your organization’s network, it is no longer the responsibility of AWS.")],
 tier=2,exam="reference",bullets=["1.2.S4"],note="d12-047. Historical-reference whitepaper."))
dump(F,"facts-numbers-12.json")
