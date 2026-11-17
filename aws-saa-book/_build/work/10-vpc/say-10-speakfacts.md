facts card: 20 facts
vpc-natgw-one-az-redundant-in-zone
  claim: Each NAT gateway is created in one specific Availability Zone and is implemented with redundancy inside that zone.
  scope: per zonal NAT gateway; zonal NAT gateways (a regional NAT gateway expands across Availability Zones: vpc-regional-natgw-vs-zonal).
  link: [Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone](../facts/vpc.md#vpc-natgw-one-az-redundant-in-zone)
vpc-regional-natgw-billed-per-az-hour
  claim: A Regional NAT gateway is charged for each hour that it is configured in each Availability Zone: running across three Availability Zones for one hour bills three NAT Gateway-hours, and billing stops for an AZ when the gateway removes support from it.
  scope: per Regional NAT gateway, per Availability Zone.
  link: [charged for each hour that the NAT Gateway is configured in each availability zone](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
  link: [three 'NAT Gateway-hours'](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
  link: [billing automatically adjusts](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
vpc-regional-nat-expand-60-minutes
  claim: A regional NAT gateway can take up to 60 minutes to expand to a new Availability Zone after a resource appears there; until then that traffic is handled across zones by the gateway in an existing Availability Zone.
  scope: per regional NAT gateway.
  link: [up to 60 minutes](../facts/vpc.md#vpc-regional-nat-expand-60-minutes)
  say: up to sixty minutes
vpc-regional-nat-ip-per-az
  claim: A regional NAT gateway supports up to 32 IP addresses per Availability Zone, compared with 8 for a zonal NAT gateway; each IP address increases the limit on concurrent connections to a popular destination, identified by a unique combination of destination IP, destination port and protocol, by 55,000.
  scope: per regional NAT gateway, per Availability Zone; maximum; not adjustable.
  link: [32 IP addresses per Availability Zone](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  link: [8 for zonal NAT gateways](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  link: [55,000](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  say: thirty-two IP addresses per Availability Zone | eight for a zonal NAT gateway | fifty-five thousand connections per IP address
vpc-public-ipv4-avoid-per-instance-with-elb-nat
  claim: To reduce the public IPv4 charge, AWS points to Elastic Load Balancers for inbound traffic and NAT gateways for outbound traffic instead of a public IPv4 address on each instance, and to faster adoption of IPv6.
  scope: per workload.
  link: [use Elastic Load Balancers and NAT Gateways for ingress and egress traffic](../facts/vpc.md#vpc-public-ipv4-avoid-per-instance-with-elb-nat)
  say: load balancer in, NAT gateway out, no public IP per instance
vpc-public-subnet-only-if-reachable
  claim: A server that does not need to be directly reachable from the internet should not be deployed in a public subnet.
  link: [If a server doesn't need to be directly reachable from the internet, you should not deploy it into a public subnet](../facts/vpc.md#vpc-public-subnet-only-if-reachable)
vpc-nondefault-subnet-no-public-ip-by-default
  claim: By default an instance launched into a nondefault subnet has a private IPv4 address but no public IPv4 address, unless you assign one at launch or change the subnet's public IP address attribute; such instances can talk to each other but cannot reach the internet.
  scope: per nondefault subnet; default; adjustable.
  link: [has a private IPv4 address, but no public IPv4 address](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  link: [unless you specifically assign one at launch, or you modify the subnet's public IP address attribute](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  link: [can communicate with each other, but can't access the internet](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  say: private address only, no public address
vpc-public-ip-insights-no-cost
  claim: Public IP Insights, a feature of Amazon VPC IP Address Manager (IPAM) available at no cost, helps you monitor, analyze and audit your use of public IPv4 addresses; it launched with the announcement of the public IPv4 charge.
  link: [Public IP Insights](../facts/vpc.md#vpc-public-ip-insights-no-cost)
  say: Public IP Insights in VPC IPAM, free
vpc-nacl-stateless-needs-response-rule
  claim: Network ACLs are stateless, so an outbound rule that allows responses to inbound traffic is required; security groups are stateful, so no response rule is needed.
  link: [Network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
  link: [you must include a rule that allows responses to the inbound traffic](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
  link: [Security groups are stateful](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
vpc-sg-allow-rules-only
  claim: A security group holds allow rules only; it cannot hold deny rules. A network ACL can hold both allow and deny rules.
  scope: per security group.
  link: [You can specify allow rules, but not deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
  link: [Network ACLs can be used to set both Allow and Deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
vpc-natgw-each-active-az-in-production
  claim: In production AWS recommends deploying a NAT gateway in each active Availability Zone.
  scope: per active Availability Zone of a production VPC; zonal NAT gateways.
  link: [deploy a NAT gateway in each active AZ](../facts/vpc.md#vpc-natgw-each-active-az-in-production)
vpc-natgw-route-from-private-subnet
  claim: To give instances in a private subnet internet access, you create a NAT gateway (or NAT instance) in a public subnet and add a route in the private subnet's route table that sends 0.0.0.0/0 to the NAT device.
  scope: per private subnet route table; zonal NAT gateway or NAT instance (a regional NAT gateway does not need a public subnet: vpc-regional-natgw-no-public-subnet).
  link: [create a NAT gateway or launch a NAT instance in a public subnet](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  link: [routes IPv4 internet traffic (`0.0.0.0/0`) to the NAT device](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  say: the NAT gateway sits in a public subnet | the private subnet's default route points at the NAT gateway
vpc-natgw-connections-originate-inside-vpc
  claim: Connections through a NAT gateway must always be initiated from within the VPC that contains the NAT gateway.
  scope: per NAT gateway; fixed.
  link: [Connections must always be initiated from within the VPC containing the NAT gateway](../facts/vpc.md#vpc-natgw-connections-originate-inside-vpc)
  say: connections always start inside the VPC
vpc-sg-reference-no-rules-copied
  claim: Referencing a security group in a rule does not add any rules from the referenced security group to the security group that references it.
  link: [No rules from the referenced security group are added to the security group that references it](../facts/vpc.md#vpc-sg-reference-no-rules-copied)
  say: no rules are copied
vpc-sg-vs-nacl-rule-evaluation
  claim: A security group evaluates all rules before deciding whether to allow traffic; a network ACL evaluates rules in ascending order until a match is found.
  link: [Evaluates all rules before deciding whether to allow traffic](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation)
  link: [Evaluates rules in ascending order until a match for the traffic is found](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation)
vpc-natgw-vs-instance-availability
  claim: A NAT gateway is highly available with redundancy inside its Availability Zone, and you create one per Availability Zone for a zone-independent design; a NAT instance needs a script to manage failover between instances.
  link: [Highly available](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Use a script to manage failover between instances](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Create a NAT gateway in each Availability Zone to ensure zone-independent architecture](../facts/vpc.md#vpc-natgw-vs-instance-availability)
vpc-faq-private-instances-nat
  claim: Instances without public IP addresses reach the internet through a NAT gateway or a NAT instance, using the NAT device's public IP address; the NAT device allows outbound communication but does not let machines on the internet initiate a connection to the private instances.
  scope: instances in a private subnet; no public IP address.
  link: [route their traffic through a NAT gateway or a NAT instance to access the Internet](../facts/vpc.md#vpc-faq-private-instances-nat)
  link: [allows outbound communication but doesn’t allow machines on the Internet to initiate a connection to the privately addressed instances](../facts/vpc.md#vpc-faq-private-instances-nat)
  say: through a NAT gateway or a NAT instance | outbound only; nothing from the internet can start a connection
vpc-default-subnet-public-ip-and-dns
  claim: An instance launched into a default subnet receives a public IPv4 address, a private IPv4 address and both public and private DNS hostnames; an instance launched into a nondefault subnet of a default VPC does not receive a public IPv4 address or a DNS hostname.
  scope: per subnet; default; adjustable; you can change the subnet's public IP addressing attribute.
  link: [receive both a public IPv4 address and a private IPv4 address, and both public and private DNS hostnames](../facts/vpc.md#vpc-default-subnet-public-ip-and-dns)
  link: [don't receive a public IPv4 address or a DNS hostname](../facts/vpc.md#vpc-default-subnet-public-ip-and-dns)
  say: a default subnet gives the instance a public address and a public hostname | a nondefault subnet gives no public address
vpc-sg-new-no-inbound-rules
  claim: A newly created security group has no inbound rules, so no inbound traffic is allowed until you add inbound rules.
  scope: per new security group; default; not adjustable.
  link: [it has no inbound rules](../facts/vpc.md#vpc-sg-new-no-inbound-rules)
  link: [no inbound traffic is allowed until you add inbound rules to the security group](../facts/vpc.md#vpc-sg-new-no-inbound-rules)
  say: no inbound rules at first
vpc-default-nacl-allows-all-traffic
  claim: A VPC automatically comes with a default network ACL, configured to allow all traffic to flow in and out of the subnets associated with it; you can modify it by adding rules or removing the default numbered rules.
  scope: default network ACL; default; not adjustable.
  link: [configured to allow all traffic to flow in and out of the subnets with which it is associated](../facts/vpc.md#vpc-default-nacl-allows-all-traffic)
  link: [You can modify a default network ACL by adding rules or removing the default numbered rules](../facts/vpc.md#vpc-default-nacl-allows-all-traffic)
  say: it allows all traffic in and out
