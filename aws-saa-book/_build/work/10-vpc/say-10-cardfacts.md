facts card: 34 facts
vpc-gateway-endpoint-no-hourly-or-processing-charge
  claim: Gateway VPC endpoints have no data processing or hourly charges, so routing S3 traffic through a gateway endpoint instead of the NAT gateway avoids the NAT gateway data processing charge.
  scope: per gateway endpoint.
  link: [There are no data processing or hourly charges for using Gateway Type VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
  link: [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
vpc-sg-vs-nacl-rule-type
  claim: A security group supports allow rules only; a network ACL supports allow and deny rules.
  link: [Allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
  link: [Allow and deny rules](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
vpc-sg-vs-nacl-return-traffic
  claim: In a security group return traffic is automatically allowed (stateful); in a network ACL return traffic must be explicitly allowed (stateless).
  link: [Automatically allowed (stateful)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic)
  link: [Must be explicitly allowed (stateless)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic)
vpc-subnet-single-az
  claim: Each subnet must reside entirely within one Availability Zone and cannot span zones.
  scope: per subnet; fixed.
  link: [must reside entirely within one Availability Zone](../facts/vpc.md#vpc-subnet-single-az)
  link: [cannot span zones](../facts/vpc.md#vpc-subnet-single-az)
  say: lives entirely in one Availability Zone | cannot span zones
vpc-cidr-cannot-resize
  claim: You cannot increase or decrease the size of an existing VPC CIDR block; to get more addresses you associate a secondary IPv4 CIDR block, which must not overlap any CIDR block already associated with the VPC.
  scope: per VPC; fixed.
  link: [cannot increase or decrease the size of an existing CIDR block](../facts/vpc.md#vpc-cidr-cannot-resize)
  link: [must not overlap with any existing CIDR block that's associated with the VPC](../facts/vpc.md#vpc-cidr-cannot-resize)
  say: an existing CIDR block cannot be resized | a secondary CIDR must not overlap
vpc-natgw-shared-across-azs-loses-internet
  claim: If resources in several Availability Zones share one NAT gateway and that gateway's Availability Zone goes down, resources in the other Availability Zones lose internet access; create a NAT gateway in each Availability Zone and route each zone to its own gateway.
  scope: zonal NAT gateways used by resources in several Availability Zones; zonal NAT gateways (a regional NAT gateway expands into each Availability Zone that has resources: vpc-regional-natgw-vs-zonal).
  link: [resources in the other Availability Zones lose internet access](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
  link: [create a NAT gateway in each Availability Zone, and configure your routing to ensure that resources use the NAT gateway in the same Availability Zone](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
vpc-regional-natgw-vs-zonal
  claim: A standard (zonal) NAT gateway operates in a single Availability Zone; a regional NAT gateway automatically expands across Availability Zones as workloads appear there and contracts when a zone has no active workloads.
  link: [which operate in a single Availability Zone](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
  link: [regional NAT gateways follow your workloads to provide automatic high availability](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
  link: [automatically expands across Availability Zones based on your workload presence](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
vpc-public-vs-private-subnet-by-igw-route
  claim: A subnet is public when its route table has a route to an internet gateway and private when it does not; instances in a private subnet cannot reach the internet even if they have public IP addresses.
  scope: per subnet.
  link: [If a subnet is associated with a route table that has a route to an internet gateway, it's known as a *public subnet*](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  link: [If a subnet is associated with a route table that does not have a route to an internet gateway, it's known as a *private subnet*](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  link: [instances in the private subnet can't communicate with the internet, even if they have public IP addresses](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  say: public means a route to the internet gateway | private means no route to the internet gateway
vpc-ipv4-cidr-size-addresses
  claim: A VPC IPv4 CIDR block can be between a /16 netmask (65,536 IP addresses) and a /28 netmask (16 IP addresses).
  scope: per VPC IPv4 CIDR block; maximum; not adjustable; /16 is the largest block and /28 the smallest.
  link: [/16 netmask (65,536 IP addresses)](../facts/vpc.md#vpc-ipv4-cidr-size-addresses)
  link: [/28 netmask (16 IP addresses)](../facts/vpc.md#vpc-ipv4-cidr-size-addresses)
  say: slash sixteen, about sixty-five thousand addresses | slash twenty-eight, sixteen addresses
vpc-faq-subnet-reserved-addresses
  claim: You cannot use every address in a subnet: Amazon reserves the first four (4) IP addresses and the last one (1) IP address of every subnet for IP networking purposes.
  scope: per subnet; fixed.
  link: [the first four (4) IP addresses](../facts/vpc.md#vpc-faq-subnet-reserved-addresses)
  link: [the last one (1) IP address](../facts/vpc.md#vpc-faq-subnet-reserved-addresses)
  say: the first four addresses | and the last one
vpc-nacl-ephemeral-open-1024-65535
  claim: To cover all the client types that might reach public-facing instances, you can open ephemeral ports 1024-65535 in a network ACL and add deny rules for malicious ports in that range, placed earlier in the table than the allow rule.
  scope: per network ACL; public-facing instances with many client types.
  link: [open ephemeral ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-open-1024-65535)
  say: open ten twenty-four to sixty-five five thirty-five
vpc-nat-bandwidth-100-gbps
  claim: A zonal NAT gateway, which is created in one Availability Zone, supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps; since June 15, 2022 the ceiling is 100 Gbps, up from 45 Gbps. If you need more, split resources into several subnets with a NAT gateway each.
  scope: per zonal NAT gateway; maximum; not adjustable; automatic scaling; split subnets for more; the NAT gateway basics page describes NAT gateways created in one Availability Zone (zonal), and no saved page gives a figure for regional NAT gateways.
  link: [5 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  link: [up to 100 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  link: [45 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  say: five gigabits per second | up to one hundred gigabits per second | forty-five gigabits per second (old value)
  changed: 2022-06-15: was 45 Gbps
vpc-nat-55000-connections-per-ip
  claim: Each IPv4 address on a NAT gateway supports up to 55,000 simultaneous connections to each unique destination (destination IP, destination port and protocol); you can raise the limit by associating up to 8 IPv4 addresses (1 primary and 7 secondary) with a zonal NAT gateway, while a regional NAT gateway supports up to 32 IP addresses per Availability Zone.
  scope: per NAT gateway IPv4 address, per unique destination; maximum; not adjustable; 8 addresses for a zonal NAT gateway; a regional NAT gateway supports up to 32 IP addresses per Availability Zone.
  link: [55,000 simultaneous connections](../facts/vpc.md#vpc-nat-55000-connections-per-ip)
  link: [up to 8 IPv4 addresses](../facts/vpc.md#vpc-nat-55000-connections-per-ip)
  say: fifty-five thousand simultaneous connections per IP address | up to eight IPv4 addresses on a zonal NAT gateway, one primary and seven secondary
vpc-quota-vpcs-per-region
  claim: The default quota is 5 VPCs per Region; it is adjustable, and raising it raises the quota for internet gateways per Region by the same amount.
  scope: per Region, per account; default; adjustable.
  link: [5 VPCs per Region](../facts/vpc.md#vpc-quota-vpcs-per-region)
  link: [increases the quota on internet gateways per Region by the same amount](../facts/vpc.md#vpc-quota-vpcs-per-region)
  say: five VPCs per Region by default | raising it also raises the internet gateway quota
vpc-quota-internet-gateways-per-region
  claim: The default quota is 5 internet gateways per Region; to raise it, raise the quota for VPCs per Region. Only one internet gateway can be attached to a VPC at a time.
  scope: per Region, per account; default; adjustable; raised through the VPCs per Region quota.
  link: [5 internet gateways per Region](../facts/vpc.md#vpc-quota-internet-gateways-per-region)
  link: [only one internet gateway to a VPC at a time](../facts/vpc.md#vpc-quota-internet-gateways-per-region)
  say: five internet gateways per Region | one internet gateway per VPC
vpc-natgw-no-security-group-use-nacl
  claim: You cannot associate a security group with a NAT gateway; control traffic with the security groups of the instances behind it and with the network ACL of the NAT gateway's subnet, where NAT gateways use ports 1024 to 65535.
  scope: per NAT gateway.
  link: [You can't associate a security group with a NAT gateway](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
  link: [You can use a network ACL to control the traffic to and from the subnet for your NAT gateway](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
  link: [NAT gateways use ports 1024–65535](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
vpc-eigw-ipv6-outbound-only
  claim: An egress-only internet gateway allows outbound IPv6 communication from instances to the internet and prevents the internet from initiating IPv6 connections to them; it is for IPv6 only, and for outbound-only IPv4 you use a NAT gateway instead.
  scope: per egress-only internet gateway.
  link: [allows outbound communication over IPv6 from instances in your VPC to the internet, and prevents the internet from initiating an IPv6 connection with your instances](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  link: [for use with IPv6 traffic only](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  link: [To enable outbound-only internet communication over IPv4, use a NAT gateway instead](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  say: outbound-only internet access for IPv6 | IPv6 only
vpc-faq-flow-logs-vs-traffic-mirroring
  claim: Flow logs record metadata about flows (allowed and denied traffic, source and destination addresses, ports, protocol number, packet and byte counts, accept or reject); traffic mirroring copies the actual traffic content, including payload, for packet-level analysis.
  scope: flow logs versus traffic mirroring.
  link: [allowed and denied traffic, source and destination IP addresses, ports, protocol number, packet and byte counts, and an action (accept or reject)](../facts/vpc.md#vpc-faq-flow-logs-vs-traffic-mirroring)
  link: [analyze actual traffic content, including payload](../facts/vpc.md#vpc-faq-flow-logs-vs-traffic-mirroring)
  say: flow logs give metadata: addresses, ports, counts, accept or reject | traffic mirroring gives the packets themselves
vpc-gateway-endpoint-no-onprem-cross-region-tgw
  claim: An S3 gateway endpoint does not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway; for those cases you use an interface endpoint, at additional cost.
  link: [gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  link: [you must use an interface endpoint, which is available for an additional cost](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  say: not from on premises, other Regions or a transit gateway | use an interface endpoint instead
vpc-route-longest-prefix-match
  claim: When several routes match, the VPC uses the most specific route, the longest prefix match, to decide where to send the traffic.
  scope: per route table.
  link: [we use the most specific route that matches the traffic (longest prefix match)](../facts/vpc.md#vpc-route-longest-prefix-match)
  link: [longest prefix match](../facts/vpc.md#vpc-route-longest-prefix-match)
  say: the most specific route wins
vpc-natgw-vs-instance-bastion
  claim: A NAT gateway cannot serve as a bastion server; a NAT instance can.
  scope: per NAT gateway.
  link: [Not supported](../facts/vpc.md#vpc-natgw-vs-instance-bastion)
  link: [Use as a bastion server](../facts/vpc.md#vpc-natgw-vs-instance-bastion)
vpc-nat-instance-disable-source-dest-check
  claim: Each EC2 instance performs source/destination checks by default, so you must disable source/destination checks on a NAT instance, which sends and receives traffic that is not addressed to or from itself.
  link: [Each EC2 instance performs source/destination checks by default](../facts/vpc.md#vpc-nat-instance-disable-source-dest-check)
  link: [you must disable source/destination checks on the NAT instance](../facts/vpc.md#vpc-nat-instance-disable-source-dest-check)
  say: turn off the source/destination check
vpc-public-ip-from-amazon-pool-released
  claim: A public IPv4 address comes from Amazon's pool and is not associated with your account; when it is disassociated from your instance it goes back to the pool and you cannot get it again.
  scope: per instance.
  link: [assigned from Amazon's pool of public IP addresses; it's not associated with your account](../facts/vpc.md#vpc-public-ip-from-amazon-pool-released)
  link: [released back into the pool, and is no longer available for you to use](../facts/vpc.md#vpc-public-ip-from-amazon-pool-released)
  say: it belongs to Amazon's pool, not to your account | once released you cannot get it back
vpc-public-ipv4-hourly-in-use-or-idle
  claim: A public IPv4 address is billed at an hourly rate per address, calculated in one-second increments with a minimum of 60 seconds, and the price is the same whether the address is in use on a resource or idle in the account.
  scope: per public IPv4 address.
  link: [You pay an hourly rate for each public IPv4 address used by your AWS account](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [minimum of 60 seconds](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [The price is the same whether the public IPv4 address is in-use](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
vpc-faq-network-acl-same-subnet
  claim: Network ACLs do not filter traffic between instances in the same subnet.
  scope: per network ACL; instances in the same subnet.
  link: [do not filter traffic between instances in the same subnet](../facts/vpc.md#vpc-faq-network-acl-same-subnet)
  say: not between instances in the same subnet
vpc-regional-natgw-no-public-subnet
  claim: A regional NAT gateway is a standalone resource with its own route table and does not need a public subnet to host it; it uses a single NAT ID across all Availability Zones that have network interfaces, so subnets in different Availability Zones can use the same route entry.
  link: [you don't need to create a public subnet to host it](../facts/vpc.md#vpc-regional-natgw-no-public-subnet)
  link: [Use a single NAT ID across all Availability Zones that have network interfaces](../facts/vpc.md#vpc-regional-natgw-no-public-subnet)
vpc-regional-nat-no-private-nat
  claim: Regional NAT gateways do not support private NAT and are not supported in constrained Availability Zones; for private NAT use a zonal NAT gateway.
  scope: per regional NAT gateway.
  link: [do not support private NAT](../facts/vpc.md#vpc-regional-nat-no-private-nat)
  say: no private NAT; use a zonal NAT gateway for that
vpc-natgw-metric-errorportallocation
  claim: The NAT gateway CloudWatch metric ErrorPortAllocation counts the times the NAT gateway could not allocate a source port; a value greater than zero means too many concurrent connections are open through the NAT gateway.
  scope: per NAT gateway.
  link: [ErrorPortAllocation](../facts/vpc.md#vpc-natgw-metric-errorportallocation)
  link: [too many concurrent connections are open through the NAT gateway](../facts/vpc.md#vpc-natgw-metric-errorportallocation)
  say: error port allocation | too many concurrent connections through the NAT gateway
vpc-sg-rule-change-tracked-connections-continue
  claim: When you change a security group rule, its tracked connections are not immediately interrupted: the security group keeps allowing packets until existing connections time out; to interrupt traffic immediately you can use a network ACL, and adding a network ACL that blocks traffic breaks existing connections.
  link: [its tracked connections are not immediately interrupted](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  link: [continues to allow packets until existing connections time out](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  link: [you can use a network ACL for your subnet](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  say: existing tracked connections keep working | use a network ACL to cut traffic at once
vpc-sg-rule-sources
  claim: The source or destination of a security group rule can be a single IPv4 or IPv6 address, an IPv4 or IPv6 CIDR range, the ID of a prefix list, or the ID of a security group.
  link: [The ID of a prefix list](../facts/vpc.md#vpc-sg-rule-sources)
  link: [The ID of a security group](../facts/vpc.md#vpc-sg-rule-sources)
  link: [A range of IPv4 addresses, in CIDR block notation](../facts/vpc.md#vpc-sg-rule-sources)
  say: another security group
vpc-main-route-table-rules
  claim: Every VPC automatically has a main route table; you can change its routes but you cannot delete it, and by default the main route table of a nondefault VPC contains only a local route.
  scope: per VPC; default.
  link: [When you create a VPC, it automatically has a main route table](../facts/vpc.md#vpc-main-route-table-rules)
  link: [can't delete the main route table](../facts/vpc.md#vpc-main-route-table-rules)
  link: [the main route table contains only a local route](../facts/vpc.md#vpc-main-route-table-rules)
  say: every VPC comes with a main route table | the main route table cannot be deleted | a new VPC's main route table has only the local route
vpc-route-table-implicit-main-association
  claim: Every subnet must be associated with a route table; a subnet you do not explicitly associate is implicitly associated with the main route table, a subnet can be associated with only one route table at a time, and many subnets can share one route table.
  scope: per subnet; maximum.
  link: [the subnet is implicitly associated with the main route table](../facts/vpc.md#vpc-route-table-implicit-main-association)
  link: [A subnet can only be associated with one route table at a time](../facts/vpc.md#vpc-route-table-implicit-main-association)
  link: [associate multiple subnets with the same subnet route table](../facts/vpc.md#vpc-route-table-implicit-main-association)
  say: no explicit choice means the main route table | one route table per subnet | one route table can serve many subnets
vpc-sharing-same-az-transfer-free
  claim: Data transfer within the same Availability Zone, identified by AZ ID, is free whichever accounts own the communicating resources.
  link: [is free irrespective of account ownership of the communicating resources](../facts/vpc.md#vpc-sharing-same-az-transfer-free)
  say: same-AZ transfer is free
vpc-faq-cross-az-data-transfer-charge
  claim: Traffic between instances in subnets in different Availability Zones is charged $0.01 per GB for data transfer.
  scope: per GB, between Availability Zones in one Region; fixed; instances in subnets in different Availability Zones.
  link: [$0.01 per GB](../facts/vpc.md#vpc-faq-cross-az-data-transfer-charge)
  say: one cent per gigabyte
