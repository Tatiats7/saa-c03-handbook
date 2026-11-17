import sys; sys.path.insert(0,'aws-saa-book/_build/work/12-hybrid-networking')
from mk import *
C="client-vpn"
L="docs/vpn/latest/clientvpn-admin/limits"
H="| Name | Default | Adjustable |"
WN="www/about-aws/whats-new/"
F=[]
F.append(fact("client-vpn-quota-authorization-rules-per-endpoint",C,"quota",
 "The default quota is 200 authorization rules per Client VPN endpoint, shared between IPv4 and IPv6 routes on dual-stack endpoints, and you can request an increase. Before March 2025 the default was 50.",
 "How many authorization rules can a Client VPN endpoint have by default?",
 [("default","200 authorization rules","two hundred")],"per Client VPN endpoint","default",True,
 [ev(L,row(L,"| Authorization rules per Client VPN endpoint"),H),
  ev(WN+"2025/03/aws-client-vpn-authorization-rules-route-quotas","Previously, you were given default quota of 10 routes per association and 50 authorization rules per endpoint.")],
 vol="changed-since-2022",changed={"date":"2025-03-18","was":"50 authorization rules per endpoint","was_evidence":1},
 change_items=[cid('cvpn','increases authorization rules and route quotas'),cid('cvpn','Increased Client VPN quota'),cid('cvpn','Increased quotas')],
 exam="extended",bullets=["4.4.S7"],note="d12-086, d12-094. The history row of 2024-12-19 says 50 to 100 and the row of 2025-03-13 says 50 to 200; the post of 2025-03-18 gives old 50, new 200."))
F.append(fact("client-vpn-quota-endpoints-per-region",C,"quota",
 "The default quota is 5 Client VPN endpoints per Region, and you can request an increase.",
 "How many Client VPN endpoints can an account have per Region by default?",
 [("default","5 Client VPN endpoints","five")],"per Region, per account","default",True,
 [ev(L,row(L,"| Client VPN endpoints per Region"),H)],
 exam="reference",bullets=["4.4.S7"],note="d12-086"))
F.append(fact("client-vpn-quota-concurrent-connections-per-endpoint",C,"quota",
 "The concurrent client connections per Client VPN endpoint depend on the number of subnet associations: 7,000 with 1 subnet, 36,500 with 2, 66,500 with 3, 96,500 with 4 and 126,000 with 5; on dual-stack endpoints the limit is shared between IPv4 and IPv6 connections, and you can request an increase.",
 "How many concurrent client connections does a Client VPN endpoint support for each number of associated subnets?",
 [("one-subnet","7,000","seven thousand"),("two-subnets","36,500","thirty-six thousand five hundred"),("three-subnets","66,500","sixty-six thousand five hundred"),("four-subnets","96,500","ninety-six thousand five hundred"),("five-subnets","126,000","one hundred twenty-six thousand")],
 "per Client VPN endpoint, by number of subnet associations","default",True,
 [ev(L,row(L,"| Concurrent client connections per Client VPN endpoint"),H)],
 exam="core",tier0=True,bullets=["4.4.S7"],note="d12-086. Also in scaling-considerations as an HTML table.",cond="depends on the number of subnet associations per endpoint"))
F.append(fact("client-vpn-quota-concurrent-operations",C,"quota",
 "The quota is 10 concurrent operations per Client VPN endpoint, and it cannot be increased.",
 "How many concurrent operations can a Client VPN endpoint run?",
 [("max","10 concurrent operations","ten")],"per Client VPN endpoint","max",False,
 [ev(L,row(L,"| Concurrent operations per Client VPN endpoint"),H)],
 exam="reference",bullets=["4.4.S7"],note="d12-086. Operations include associating or disassociating subnets and creating or deleting security groups."))
F.append(fact("client-vpn-quota-crl-entries",C,"quota",
 "A client certificate revocation list for Client VPN endpoints can have 20,000 entries; this quota cannot be increased.",
 "How many entries can a client certificate revocation list for a Client VPN endpoint have?",
 [("max","20,000 entries","twenty thousand")],"per client certificate revocation list","max",False,
 [ev(L,row(L,"| Entries in a client certificate revocation list"),H)],
 exam="reference",bullets=["4.4.S7"],note="d12-086"))
F.append(fact("client-vpn-quota-routes-per-association",C,"quota",
 "The default quota is 100 routes per Client VPN target network association, shared between IPv4 and IPv6 routes on dual-stack endpoints, and you can request an increase. Before the increase the default was 10.",
 "How many routes can a Client VPN target network association have by default?",
 [("default","100 routes","one hundred")],"per Client VPN target network association","default",True,
 [ev(L,row(L,"| Routes per Client VPN target network association"),H),
  ev(WN+"2025/03/aws-client-vpn-authorization-rules-route-quotas","Previously, you were given default quota of 10 routes per association and 50 authorization rules per endpoint.")],
 vol="changed-since-2022",changed={"date":"2025-03-18","was":"10 routes per association","was_evidence":1},
 change_items=[cid('cvpn','increases authorization rules and route quotas'),cid('cvpn','Increased quotas')],
 exam="extended",bullets=["4.4.S7"],note="d12-086, d12-094."))
F.append(fact("client-vpn-quota-authorization-policy-size",C,"quota",
 "The authorization policy document of a Client VPN endpoint can be 10,000 bytes; this quota cannot be increased.",
 "How large can the authorization policy document of a Client VPN endpoint be?",
 [("max","10,000 bytes","ten thousand bytes")],"per Client VPN endpoint","max",False,
 [ev(L,row(L,"| Authorization policy document size"),H)],
 exam="reference",bullets=["1.2.S4"],note="d12-086"))
F.append(fact("client-vpn-quota-groups-per-user",C,"limit",
 "With Active Directory or a SAML-based identity provider, a user can belong to at most 200 groups, and Client VPN ignores any groups after the 200th group.",
 "How many groups can a Client VPN user belong to?",
 [("max","200 groups","two hundred")],"per user","max",False,
 [ev(L,"Users can belong to a maximum of 200 groups. We ignore any groups after the 200th group.")],
 exam="reference",bullets=["1.2.S4"],note="d12-086"))
F.append(fact("client-vpn-limit-device-posture-reevaluation-5-minutes",C,"limit",
 "With device posture, Client VPN evaluates the authorization policy when a device connects and again every 5 minutes for the life of the session.",
 "How often does Client VPN re-evaluate device posture during a session?",
 [("interval","every 5 minutes","every five minutes")],"per session","fixed",False,
 [ev(L,"Client VPN evaluates the authorization policy when a device connects and again every 5 minutes for the life of the session.")],
 exam="reference",bullets=["1.2.S4"],note="d12-092. Release date of device posture: not found."))
F.append(fact("client-vpn-limit-minimum-bandwidth-10-mbps",C,"limit",
 "A minimum bandwidth of 10 Mbps is supported per Client VPN user connection.",
 "What minimum bandwidth is supported per Client VPN user connection?",
 [("min","10 Mbps","ten megabits per second")],"per user connection","min",False,
 [ev("docs/vpn/latest/clientvpn-admin/test-throughput","A minimum bandwidth of 10 Mbps is supported per user connection.")],
 exam="extended",bullets=["4.4.S7"],note="d12-086. The best-practices page says each user connection has a maximum baseline bandwidth of 50 Mbps."))
F.append(fact("client-vpn-limit-baseline-bandwidth-50-mbps",C,"limit",
 "Each Client VPN user connection has a maximum baseline bandwidth of 50 Mbps; if you hit the maximum bandwidth limit you can request an increase through AWS Support.",
 "What is the maximum baseline bandwidth of a Client VPN user connection?",
 [("max","maximum baseline bandwidth of 50 Mbps","fifty megabits per second")],"per user connection","max",True,
 [ev("docs/vpn/latest/clientvpn-admin/what-is-best-practices","Each user connection has a maximum baseline bandwidth of 50 Mbps.")],
 exam="extended",bullets=["4.4.S7"],note="d12-086"))
F.append(fact("client-vpn-limit-client-cidr-size",C,"limit",
 "A Client VPN client CIDR range must have a block size of at least /22 and must not be greater than /12, and it cannot be changed after you create the endpoint.",
 "Which block sizes can the client CIDR range of a Client VPN endpoint have?",
 [("range","at least /22 and must not be greater than /12","")],"per Client VPN endpoint","max",False,
 [ev("docs/vpn/latest/clientvpn-admin/what-is-best-practices","Client CIDR ranges must have a block size of at least /22 and must not be greater than /12."),
  ev("docs/vpn/latest/clientvpn-admin/what-is-best-practices","The client CIDR range cannot be changed after you create the Client VPN endpoint.")],
 exam="extended",bullets=["4.4.S7"],note="d12-086. IPv4 client CIDR; IPv6 client CIDR is assigned by Amazon."))
F.append(fact("client-vpn-limit-username-length-1024-bytes",C,"limit",
 "The maximum username length is 1024 bytes, and Client VPN rejects connections with longer usernames.",
 "What is the maximum username length for Client VPN?",
 [("max","1024 bytes","one thousand twenty-four bytes")],"per user name","max",False,
 [ev("docs/vpn/latest/clientvpn-admin/what-is-best-practices","The maximum username length is 1024 bytes. Connections with longer usernames will be rejected.")],
 exam="reference",bullets=["1.2.S4"],note="d12-086"))
# defaults
F.append(fact("client-vpn-default-session-duration-24-hours",C,"default",
 "By default, the maximum VPN session duration of a Client VPN endpoint is 24 hours; you can configure a shorter maximum duration.",
 "What is the default maximum VPN session duration of a Client VPN endpoint?",
 [("default","24 hours","twenty-four hours")],"per Client VPN endpoint","default",True,
 [ev("docs/vpn/latest/clientvpn-admin/cvpn-working-max-duration","You can configure a shorter maximum VPN session duration to help meet security and compliance requirements. By default, the maximum VPN session duration is 24 hours.")],
 exam="extended",tier0=False,bullets=["1.2.S4"],note="d12-090. The allowed values are listed as options in the console and are not stated in the guide pages."))
F.append(fact("client-vpn-default-transport-udp",C,"default",
 "By default a Client VPN endpoint uses the UDP transport protocol; you can choose TCP at creation but cannot change the transport protocol afterwards.",
 "Which transport protocol does a Client VPN endpoint use by default?",
 [("default","UDP transport protocol","")],"per Client VPN endpoint","default",False,
 [ev("docs/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create","(Optional) By default, the Client VPN endpoint uses the `UDP` transport protocol. To use the `TCP` transport protocol instead, for **Transport Protocol**, select **TCP**."),
  ev("docs/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create","UDP typically offers better performance than TCP. You cannot change the transport protocol after you create the Client VPN endpoint.")],
 exam="reference",bullets=["1.2.S4"],note="d12-086"))
F.append(fact("client-vpn-default-split-tunnel-disabled",C,"default",
 "By default, split-tunnel on a Client VPN endpoint is disabled.",
 "Is split-tunnel enabled by default on a Client VPN endpoint?",
 [("default","split-tunnel on a Client VPN endpoint is disabled","")],"per Client VPN endpoint","default",True,
 [ev("docs/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create","(Optional) To have the endpoint be a split-tunnel Client VPN endpoint, turn on **Enable split-tunnel**. By default, split-tunnel on a Client VPN endpoint is disabled.")],
 exam="core",bullets=["1.2.S4"],note="d12-086"))
F.append(fact("client-vpn-default-vpn-port-443",C,"default",
 "The default VPN port of a Client VPN endpoint is 443.",
 "What is the default VPN port of a Client VPN endpoint?",
 [("default","The default is 443","four four three")],"per Client VPN endpoint","default",True,
 [ev("docs/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create","(Optional) For **VPN port**, choose the VPN port number. The default is 443.")],
 exam="reference",bullets=["1.2.S4"],note="d12-086"))
F.append(fact("client-vpn-limit-login-banner-1400-characters",C,"limit",
 "The client login banner text of a Client VPN endpoint can have a maximum of 1400 characters, in UTF-8 encoded characters only.",
 "How long can the Client VPN login banner text be?",
 [("max","1400 characters","fourteen hundred characters")],"per Client VPN endpoint","max",False,
 [ev("docs/vpn/latest/clientvpn-admin/cvpn-working-endpoint-create","For **Client login banner text**, enter the text that will be displayed in a banner on AWS provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.")],
 exam="reference",bullets=["1.2.S4"],note="Triaged from the endpoint creation page."))
dump(F,"facts-numbers-09.json")
