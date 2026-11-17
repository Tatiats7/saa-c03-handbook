import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
D="direct-connect"
DC="docs/directconnect/latest/UserGuide/dedicated_connection"
HC="docs/directconnect/latest/UserGuide/hosted_connection"
VI="docs/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces"
FAQ="www/directconnect/faqs"
F=[]
F.append(fact("direct-connect-limit-dedicated-port-speeds",D,"limit",
 "A Direct Connect dedicated connection has a port speed of 1 Gbps, 10 Gbps, 100 Gbps, or 400 Gbps.",
 "Which port speeds can a Direct Connect dedicated connection have?",
 [("list","1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps","one, ten, one hundred and four hundred gigabits per second"),("max","400 Gbps","four hundred gigabits per second")],
 "per dedicated connection","fixed",False,
 [ev(DC,"The possible values are 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps."),
  ev(FAQ,"For Dedicated Connections, 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps ports are available.")],
 vol="frequently-changing",exam="core",tier0=True,bullets=["4.4.S7"],note="d12-032, d12-070. 400 Gbps added 2024-07-18 (history); the old list is not stated verbatim, so no changed.was.",
 change_items=[cid('dx','Support for 400G'),cid('dx','native 400 Gbps')]))
F.append(fact("direct-connect-limit-hosted-port-speeds",D,"limit",
 "A Direct Connect hosted connection has a speed of 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps.",
 "Which speeds can a Direct Connect hosted connection have?",
 [("list","50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps","fifty megabits per second up to twenty-five gigabits per second"),("min","50 Mbps","fifty megabits per second"),("max","25 Gbps","twenty-five gigabits per second")],
 "per hosted connection","fixed",False,
 [ev(HC,"For hosted connections, the possible values are 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps."),
  ev(FAQ,"For Hosted Connections, connection speeds of 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, and 25 Gbps may be ordered from approved AWS Direct Connect Partners.")],
 vol="frequently-changing",exam="core",tier0=True,bullets=["4.4.S7"],note="d12-032, d12-071. 25 Gbps hosted added 2024-04-24 (feed pointer only; the post is blocked by robots.txt).",
 change_items=[cid('dx','25 Gbps hosted')]))
F.append(fact("direct-connect-restriction-hosted-high-speeds-select-partners",D,"restriction",
 "Only Direct Connect partners that have met specific requirements may create a 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps hosted connection.",
 "Which hosted connection speeds can only some partners offer?",
 [("rule","1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps","")],
 "per hosted connection","fixed",False,
 [ev(HC,"Note that only those Direct Connect partners who have met specific requirements may create a 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps, or 25 Gbps hosted connection.")],
 exam="extended",bullets=["4.4.S7"],note="d12-032"))
F.append(fact("direct-connect-restriction-hosted-25g-needs-100g-location",D,"restriction",
 "25 Gbps hosted connections are available only in Direct Connect locations where 100 Gbps port speeds are available.",
 "Where are 25 Gbps hosted connections available?",
 [("rule","only in Direct Connect locations where 100 Gbps port speeds are available","")],
 "per Direct Connect location","fixed",False,
 [ev(HC,"25 Gbps connections are available only in Direct Connect locations where 100 Gbps port speeds are available.")],
 exam="reference",bullets=["4.4.S7"],note="d12-032"))
F.append(fact("direct-connect-restriction-dedicated-port-speed-fixed",D,"restriction",
 "You cannot change the port speed of a dedicated connection after you create the connection request; to change it, you create and configure a new connection.",
 "Can you change the port speed of an existing dedicated connection?",
 [("rule","can't change the port speed after you create the connection request","")],
 "per dedicated connection","fixed",False,
 [ev(DC,"You can't change the port speed after you create the connection request. To change the port speed, you must create and configure a new connection.")],
 exam="extended",bullets=["4.4.S7"],note="d12-032"))
F.append(fact("direct-connect-restriction-hosted-speed-change-by-partner",D,"restriction",
 "Only your AWS Direct Connect Partner can change the port speed of a hosted connection.",
 "Who can change the speed of a hosted connection?",
 [("rule","only be changed by your AWS Direct Connect Partner","")],
 "per hosted connection","fixed",False,
 [ev(HC,"Connection port speeds can only be changed by your AWS Direct Connect Partner.")],
 exam="extended",bullets=["4.4.S7"],note="d12-032"))
F.append(fact("direct-connect-limit-loa-cfa-response-7-days",D,"limit",
 "If AWS asks for more information after you request a dedicated connection, you must respond within 7 days or the connection is deleted.",
 "How long do you have to answer a request for more information about a new dedicated connection?",
 [("max","7 days","seven days")],
 "per dedicated connection request","max",False,
 [ev(DC,"If you receive a request for more information, you must respond within 7 days or the connection is deleted.")],
 exam="reference",bullets=["4.4.S7"],note="LOA-CFA step of a dedicated connection.",cond="after you request a dedicated connection and AWS requests more information"))
F.append(fact("direct-connect-behavior-hosted-traffic-policing",D,"behavior",
 "AWS uses traffic policing on hosted connections: when the traffic rate reaches the configured maximum rate, excess traffic is dropped, so bursty traffic can get a lower throughput than non-bursty traffic.",
 "What happens to traffic above the configured rate on a hosted connection?",
 [("rule","excess traffic is dropped","")],
 "per hosted connection","fixed",False,
 [ev(HC,"AWS uses traffic policing on hosted connections, which means that when the traffic rate reaches the configured maximum rate, excess traffic is dropped. This might result in bursty traffic having a lower throughput than non-bursty traffic.")],
 exam="extended",bullets=["4.4.S7"],note="d12-073"))
F.append(fact("direct-connect-limit-mtu-private-vif",D,"limit",
 "The MTU of a Direct Connect private virtual interface can be either 1500 or 9001 (jumbo frames).",
 "Which MTU values can a Direct Connect private virtual interface use?",
 [("default","1500","fifteen hundred"),("jumbo","9001","ninety hundred one")],
 "per private virtual interface","max",True,
 [ev(VI,"The MTU of a private virtual interface can be either 1500 or 9001 (jumbo frames).")],
 exam="core",bullets=["4.4.S7"],note="d12-053"))
F.append(fact("direct-connect-limit-mtu-transit-vif",D,"limit",
 "The MTU of a Direct Connect transit virtual interface can be either 1500 or 8500 (jumbo frames).",
 "Which MTU values can a Direct Connect transit virtual interface use?",
 [("default","1500","fifteen hundred"),("jumbo","8500","eighty-five hundred")],
 "per transit virtual interface","max",True,
 [ev(VI,"The MTU of a transit virtual interface can be either 1500 or 8500 (jumbo frames)."),
  ev(FAQ,"Yes, a transit virtual interface will support jumbo frames. Maximum transmission unit (MTU) size will be limited to 8,500.")],
 exam="core",bullets=["4.4.S7"],note="d12-053"))
F.append(fact("direct-connect-behavior-jumbo-frames-update-30-seconds",D,"behavior",
 "Setting a virtual interface to jumbo frames can update the underlying physical connection, and that update disrupts connectivity for all virtual interfaces on the connection for up to 30 seconds.",
 "What happens to a connection when you enable jumbo frames on a virtual interface?",
 [("max","up to 30 seconds","up to thirty seconds")],
 "per connection","max",False,
 [ev(VI,"Setting the MTU of a virtual interface to 8500 (jumbo frames) or 9001 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds.")],
 exam="extended",bullets=["4.4.S7"],note="d12-053"))
F.append(fact("direct-connect-behavior-mtu-1500-when-routes-overlap",D,"behavior",
 "If two private virtual interfaces advertise the same route with different MTU values, or a Site-to-Site VPN advertises the same route, an MTU of 1500 is used.",
 "Which MTU is used when the same route is advertised over interfaces with different MTUs or over a VPN?",
 [("value","1500 MTU","fifteen hundred")],
 "per route","fixed",False,
 [ev(VI,"If you have two private virtual interfaces that advertise the same route but use different MTU values, or if you have a Site-to-Site VPN that advertise the same route, 1500 MTU is used.")],
 exam="extended",bullets=["4.4.S7"],note="d12-053"))
F.append(fact("direct-connect-limit-tgw-jumbo-frames-8500",D,"limit",
 "Jumbo frames on Transit Gateways support only 8500 bytes.",
 "What jumbo frame size does a transit gateway support over Direct Connect?",
 [("max","8500 bytes","eighty-five hundred bytes")],
 "per transit gateway","max",False,
 [ev(VI,"Jumbo frames on Transit Gateways support only 8500 bytes.")],
 exam="extended",bullets=["4.4.S7"],note="d12-053"))
dump(F,"facts-numbers-05.json")
