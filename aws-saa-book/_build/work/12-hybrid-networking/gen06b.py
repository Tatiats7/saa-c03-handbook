import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
D="direct-connect"
VR="docs/directconnect/latest/UserGuide/vif-rate-limiters"
SLA="www/directconnect/sla"
F=[]
F.append(fact("direct-connect-limit-rate-limiter-range-1g",D,"limit",
 "On a 1 Gbps dedicated connection you can set VIF rate limiters between 50 Mbps and 1 Gbps.",
 "Which bandwidth range can a VIF rate limiter have on a 1 Gbps dedicated connection?",
 [("min","50 Mbps","fifty megabits per second"),("max","1 Gbps","one gigabit per second")],
 "per VIF rate limiter","max",False,
 [ev(VR,"On a 1 Gbps Dedicated connection, you can set Rate Limiters between 50 Mbps and 1 Gbps.")],
 exam="reference",bullets=["4.4.S7"],note="d12-073",vol="frequently-changing",change_items=[cid('dx','VIF Rate Limiters')]))
F.append(fact("direct-connect-sla-multi-site-redundant-definition",D,"sla",
 "A Multi-Site Redundant Deployment has at least four Connections across at least two different Direct Connect locations, with no fewer than two in each location and each Connection on a unique AWS device.",
 "What does the Direct Connect SLA require for a Multi-Site Redundant Deployment?",
 [("min","at least four Connections","at least four")],
 "per deployment","min",False,
 [ev(SLA,"Multi-Site Redundant Deployment is a Deployment that comprises at least four Connections deployed across a minimum of two different Direct Connect locations, each of which is configured to access the same Endpoint, where no fewer than two Connections are deployed in each of the two Direct Connection locations, each Connection is on a unique AWS device, and, with respect to private Endpoints, the Endpoint is deployed in two or more Availability Zones.")],
 exam="core",bullets=["1.2.S4"],note="d12-047. The SLA page was last updated 2026-07-24."))
F.append(fact("direct-connect-sla-multi-site-redundant-support-and-review",D,"sla",
 "For a Multi-Site Redundant Deployment under the Direct Connect SLA you must have an Enterprise Support plan and have completed a Well-Architected Review with an AWS Solutions Architect.",
 "Which support plan and review does the Direct Connect Multi-Site Redundant SLA require?",
 [("rule","Enterprise Support plan in place","")],
 "per deployment","fixed",False,
 [ev(SLA,"You must have an Enterprise Support plan in place for any Multi-Site Redundant Deployment and have completed a “Well-Architected Review” with an AWS Solutions Architect.")],
 exam="extended",bullets=["1.2.S4"],note="d12-047"))
dump(F,"facts-numbers-06b.json")
