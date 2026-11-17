facts card: 511 facts
vpc-api-is-part-of-ec2-api
  claim: To connect programmatically to an AWS service you use an endpoint; the API actions that manage Amazon VPC resources are part of the Amazon EC2 API, so VPC uses the Amazon EC2 service endpoints.
  link: [To connect programmatically to an AWS service, you use an endpoint](../facts/vpc.md#vpc-api-is-part-of-ec2-api)
  link: [are part of the Amazon EC2 API](../facts/vpc.md#vpc-api-is-part-of-ec2-api)
  say: VPC actions are EC2 API actions
vpc-az-at-least-three-per-region
  claim: Each AWS Region has at least three Availability Zones; newer accounts can access two Availability Zones in US West (N. California).
  scope: per Region; minimum; not adjustable; newer accounts can access two Availability Zones in US West (N. California).
  link: [at least three Availability Zones](../facts/vpc.md#vpc-az-at-least-three-per-region)
  say: at least three Availability Zones
vpc-az-id-same-location-every-account
  claim: An AZ ID such as use1-az1 names the same physical location in every AWS account, while an Availability Zone code such as us-east-1a can point to different physical locations in different accounts in the oldest Regions for accounts created before November 2025; use AZ IDs to line up Availability Zones across accounts.
  scope: per Availability Zone, across AWS accounts; independent code mapping applies in the oldest Regions for accounts created before November 2025.
  link: [the same physical location in every AWS account](../facts/vpc.md#vpc-az-id-same-location-every-account)
  link: [might not be the same physical location](../facts/vpc.md#vpc-az-id-same-location-every-account)
  say: the same physical place in every account | the zone letter can differ between accounts
vpc-best-practice-guardduty-uses-flow-logs
  claim: Amazon GuardDuty detects potential threats, and its foundational threat detection includes monitoring the VPC flow logs of your EC2 instances.
  link: [monitoring the VPC flow logs associated with your Amazon EC2 instances](../facts/vpc.md#vpc-best-practice-guardduty-uses-flow-logs)
vpc-best-practice-iam-access
  claim: The VPC security best practices say to manage access to AWS resources in a VPC with IAM identity federation, users and roles.
  link: [IAM) identity federation, users, and roles](../facts/vpc.md#vpc-best-practice-iam-access)
vpc-best-practice-network-access-analyzer
  claim: The VPC security best practices suggest Network Access Analyzer to identify unintended network access to resources in VPCs.
  link: [identify unintended network access](../facts/vpc.md#vpc-best-practice-network-access-analyzer)
vpc-best-practice-network-firewall-filtering
  claim: The VPC security best practices suggest AWS Network Firewall to monitor and protect a VPC by filtering inbound and outbound traffic.
  link: [filtering inbound and outbound traffic](../facts/vpc.md#vpc-best-practice-network-firewall-filtering)
vpc-billing-code-ipam-ip-hours
  claim: The usage code IPAddressManager-IP-Hours measures, hourly, the time that IP addresses are managed by IPAM Advanced Tier.
  scope: per Region; IPAM Advanced Tier only.
  link: [IPAddressManager-IP-Hours](../facts/vpc.md#vpc-billing-code-ipam-ip-hours)
  say: IP address manager IP hours
vpc-billing-code-public-ipv4-idle
  claim: The usage code PublicIPv4:IdleAddress measures, in hours with per-second granularity, the time that public IPv4 addresses are not in use by a resource.
  scope: per Region, per public IPv4 address.
  link: [PublicIPv4:IdleAddress](../facts/vpc.md#vpc-billing-code-public-ipv4-idle)
  say: public IPv4 idle address
vpc-billing-code-public-ipv4-in-use
  claim: The billing code {{region}}-PublicIPv4:InUseAddress records the hours that public IPv4 addresses are in use by a resource, at per-second granularity.
  scope: per Region, billing and usage reports.
  link: [PublicIPv4:InUseAddress](../facts/vpc.md#vpc-billing-code-public-ipv4-in-use)
  say: public IPv4 in-use address
vpc-billing-code-vpc-endpoint-bytes
  claim: The usage code VpcEndpoint-Bytes measures, in GB, the data processed by interface VPC endpoints.
  scope: per Region, interface VPC endpoints.
  link: [VpcEndpoint-Bytes](../facts/vpc.md#vpc-billing-code-vpc-endpoint-bytes)
  say: VPC endpoint bytes
vpc-billing-code-vpc-endpoint-hours
  claim: The billing code {{region}}-VpcEndpoint-Hours records the hours that interface VPC endpoints are provisioned, at hourly granularity.
  scope: per Region, billing and usage reports; interface endpoints.
  link: [VpcEndpoint-Hours](../facts/vpc.md#vpc-billing-code-vpc-endpoint-hours)
  say: VPC endpoint hours
vpc-blog-cross-region-transfer-charged
  claim: Traffic that crosses a Regional boundary typically incurs a data transfer charge, so avoid cross-Region transfer unless the business case requires it.
  scope: per Region pair.
  link: [Traffic that crosses a Regional boundary will typically incur a data transfer charge](../facts/vpc.md#vpc-blog-cross-region-transfer-charged)
vpc-blog-gateway-endpoints-no-transfer-interface-charged
  claim: Gateway endpoints let a VPC reach Amazon S3 and DynamoDB without data transfer charges inside the Region, while interface endpoints incur hourly and data transfer charges.
  scope: per endpoint.
  link: [VPC gateway endpoints allow communication to Amazon S3 and Amazon DynamoDB without incurring data transfer charges within the same Region](../facts/vpc.md#vpc-blog-gateway-endpoints-no-transfer-interface-charged)
  link: [This type of endpoint incurs hourly service charges and data transfer charges](../facts/vpc.md#vpc-blog-gateway-endpoints-no-transfer-interface-charged)
vpc-blog-igw-free-natgw-processing-same-region
  claim: Reaching an AWS service's public endpoint in the same Region through an internet gateway has no data transfer charge, while reaching it through a NAT gateway adds a per-gigabyte data processing charge.
  scope: same Region.
  link: [there are no data transfer charges](../facts/vpc.md#vpc-blog-igw-free-natgw-processing-same-region)
  link: [there is a data processing charge (per gigabyte (GB)) for data that passes through the gateway](../facts/vpc.md#vpc-blog-igw-free-natgw-processing-same-region)
vpc-blog-inbound-free-outbound-charged
  claim: Inbound data transfer from the internet is free for all services in all Regions; data transfer out from AWS to the internet is charged per service at rates specific to the originating Region.
  scope: per Region.
  link: [There is no charge for inbound data transfer across all services in all Regions](../facts/vpc.md#vpc-blog-inbound-free-outbound-charged)
  link: [Data transfer from AWS to the internet is charged per service, with rates specific to the originating Region](../facts/vpc.md#vpc-blog-inbound-free-outbound-charged)
vpc-blog-same-az-free-cross-az-charged
  claim: Data transfer within the same Availability Zone is free, and traffic that crosses an Availability Zone boundary typically incurs a data transfer charge, so use resources from the local Availability Zone where possible.
  scope: per Availability Zone pair.
  link: [Data transfer within the same Availability Zone is free](../facts/vpc.md#vpc-blog-same-az-free-cross-az-charged)
  link: [Traffic that crosses an Availability Zone boundary typically incurs a data transfer charge](../facts/vpc.md#vpc-blog-same-az-free-cross-az-charged)
vpc-bpa-change
  claim: VPC Block Public Access (BPA), added November 19, 2024, blocks resources in the VPCs and subnets you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways; it is one account-level setting per Region, with exclusions.
  scope: per account, per Region.
  link: [November 19, 2024](../facts/vpc.md#vpc-bpa-change)
  link: [block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways](../facts/vpc.md#vpc-bpa-change)
  say: November nineteenth, twenty twenty-four | one switch that blocks internet gateway traffic for a whole account in a Region
vpc-bpa-declarative-policy-change
  claim: Since December 1, 2024 an AWS Organizations declarative policy can enforce VPC BPA on every account in the organization; the policy can decide whether exclusions are allowed, but exclusions themselves must still be created in the account that owns the VPC.
  scope: per AWS Organization.
  link: [December 1, 2024](../facts/vpc.md#vpc-bpa-declarative-policy-change)
  link: [cannot create exclusions with the policy](../facts/vpc.md#vpc-bpa-declarative-policy-change)
  say: December first, twenty twenty-four | the policy cannot create exclusions
vpc-bpa-exclusions-max-50
  claim: You can create a maximum of 50 VPC BPA exclusions per account per Region (adjustable); an exclusion for a VPC applies to all subnets in that VPC, and exclusions can be created before BPA is turned on.
  scope: per account, per Region; maximum; adjustable.
  link: [maximum of 50 exclusions](../facts/vpc.md#vpc-bpa-exclusions-max-50)
  say: fifty exclusions per account per Region
vpc-bpa-modes
  claim: VPC BPA has two modes: bidirectional blocks all traffic to and from internet gateways and egress-only internet gateways in the Region (except excluded VPCs and subnets); ingress-only blocks internet traffic into the VPCs but still allows traffic through NAT gateways and egress-only internet gateways, because those only allow outbound connections.
  scope: per account, per Region.
  link: [blocks all traffic to and from internet gateways and egress-only internet gateways](../facts/vpc.md#vpc-bpa-modes)
  link: [Only traffic to and from NAT gateways and egress-only internet gateways is allowed](../facts/vpc.md#vpc-bpa-modes)
  say: bidirectional: nothing in or out through the internet gateway | ingress-only: outbound through NAT or egress-only gateway still works
vpc-case-aws-multiple-ips-fewer-natgws
  claim: In its Network Firewall migration AWS used multiple IP address support on NAT gateways to reduce the number of NAT gateways needed in large environments.
  link: [AWS used multiple IP address support to minimize the number of NAT gateways needed in larger environments](../facts/vpc.md#vpc-case-aws-multiple-ips-fewer-natgws)
vpc-case-aws-network-firewall-migration
  claim: By 2023 AWS shifted the TCP/IP traffic of its internal microservices to AWS Network Firewall; within a few months it migrated more than 10 Tbps of traffic and more than 250 billion connections per day globally to the cloud, and 2,600 NAT gateways and 1,300 AWS Network Firewalls were deployed.
  link: [more than 10 Tbps of traffic](../facts/vpc.md#vpc-case-aws-network-firewall-migration)
  link: [more than 250 billion connections per day](../facts/vpc.md#vpc-case-aws-network-firewall-migration)
  link: [2,600 NAT gateways](../facts/vpc.md#vpc-case-aws-network-firewall-migration)
  link: [1,300 AWS Network Firewalls](../facts/vpc.md#vpc-case-aws-network-firewall-migration)
vpc-case-aws-small-firewalls-shrink-fault-domain
  claim: AWS deployed many small firewalls per network segment instead of large clusters, which shrinks the fault domain from an entire Availability Zone to individual services inside it.
  link: [shrinks the size of the fault domain from the entire Availability Zone to individual services within the Availability Zone](../facts/vpc.md#vpc-case-aws-small-firewalls-shrink-fault-domain)
vpc-case-carrier-hub-and-spoke-tgw
  claim: Carrier Global used AWS Transit Gateway, which connects Amazon VPCs, AWS accounts and on-premises networks, to connect its VPCs in a hub-and-spoke model.
  link: [to connect its VPCs in a hub-and-spoke model](../facts/vpc.md#vpc-case-carrier-hub-and-spoke-tgw)
vpc-case-carrier-ipam-account-vending
  claim: Carrier Global used Amazon VPC IPAM to set standard CIDR ranges for VPCs and subnets in new accounts, cutting the time to provision an account from 3 days to minutes and gaining visibility into IP address use.
  link: [specifying classless inter-domain routing ranges for VPCs and subnets](../facts/vpc.md#vpc-case-carrier-ipam-account-vending)
  link: [from 3 days to just minutes](../facts/vpc.md#vpc-case-carrier-ipam-account-vending)
  link: [gaining greater visibility into IP address use](../facts/vpc.md#vpc-case-carrier-ipam-account-vending)
vpc-centralized-egress-reduces-natgw-cost
  claim: Centralizing NAT gateways in a separate egress VPC, with spoke VPCs routing egress traffic to them through a transit gateway or Cloud WAN, is a way to reduce the cost of a NAT gateway in every spoke VPC.
  link: [Centralizing NAT gateways can be a viable option to reduce costs](../facts/vpc.md#vpc-centralized-egress-reduces-natgw-cost)
  link: [create a separate egress VPC in the network services account](../facts/vpc.md#vpc-centralized-egress-reduces-natgw-cost)
vpc-centralized-egress-tgw-processing-tradeoff
  claim: Centralizing NAT gateways behind a transit gateway adds a transit gateway data processing charge compared with a NAT gateway in every VPC; for a VPC that sends huge amounts of data, keeping the NAT gateway local can be more cost-effective.
  link: [you pay an extra Transit Gateway data processing charge](../facts/vpc.md#vpc-centralized-egress-tgw-processing-tradeoff)
  link: [keeping the NAT local in the VPC to avoid the Transit Gateway data processing charge might be a more cost-effective option](../facts/vpc.md#vpc-centralized-egress-tgw-processing-tradeoff)
vpc-cidr-cannot-resize
  claim: You cannot increase or decrease the size of an existing VPC CIDR block; to get more addresses you associate a secondary IPv4 CIDR block, which must not overlap any CIDR block already associated with the VPC.
  scope: per VPC; fixed.
  link: [cannot increase or decrease the size of an existing CIDR block](../facts/vpc.md#vpc-cidr-cannot-resize)
  link: [must not overlap with any existing CIDR block that's associated with the VPC](../facts/vpc.md#vpc-cidr-cannot-resize)
  say: an existing CIDR block cannot be resized | a secondary CIDR must not overlap
vpc-cidr-link-local-range-cannot-be-vpc-cidr
  claim: CIDR blocks from the link-local block 169.254.0.0/16 are reserved (RFC 5735) and cannot be assigned to VPCs.
  scope: per VPC CIDR block.
  link: [169.254.0.0/16](../facts/vpc.md#vpc-cidr-link-local-range-cannot-be-vpc-cidr)
  link: [cannot be assigned to VPCs](../facts/vpc.md#vpc-cidr-link-local-range-cannot-be-vpc-cidr)
  say: one sixty-nine dot two fifty-four, the link-local range | cannot be used as a VPC CIDR
vpc-cidr-publicly-routable-allowed
  claim: Most VPC ranges come from the RFC 1918 private ranges, but you can create a VPC with a publicly routable CIDR block outside RFC 1918; whatever the range, there is no direct internet access from the VPC CIDR and you must go through a gateway.
  scope: per VPC.
  link: [you can use publicly routable CIDR blocks for your VPC](../facts/vpc.md#vpc-cidr-publicly-routable-allowed)
  link: [we do not support direct access to the internet from your VPC's CIDR block, including a publicly-routable CIDR block](../facts/vpc.md#vpc-cidr-publicly-routable-allowed)
  link: [Most VPC IP address ranges fall within the private (non-publicly routable) IP address ranges specified in RFC 1918](../facts/vpc.md#vpc-cidr-publicly-routable-allowed)
  say: a public range is allowed | a public range still needs an internet gateway
vpc-connect-site-to-site-vpn-two-tunnels
  claim: You can connect a VPC to a corporate data center with an IPsec AWS Site-to-Site VPN connection, which consists of two VPN tunnels between a virtual private gateway or transit gateway on the AWS side and a customer gateway device on your side.
  link: [an IPsec AWS Site-to-Site VPN connection](../facts/vpc.md#vpc-connect-site-to-site-vpn-two-tunnels)
  link: [two VPN tunnels between a virtual private gateway or transit gateway on the AWS side, and a customer gateway device](../facts/vpc.md#vpc-connect-site-to-site-vpn-two-tunnels)
  say: two tunnels
vpc-connect-transit-gateway-regional-router
  claim: A transit gateway interconnects VPCs and on-premises networks and acts as a Regional virtual router for traffic between its attachments, which can include VPCs, VPN connections, Direct Connect gateways and transit gateway peering connections.
  link: [acts as a Regional virtual router for traffic flowing between its attachments](../facts/vpc.md#vpc-connect-transit-gateway-regional-router)
  say: a Regional virtual router
vpc-create-two-azs-for-production
  claim: When you create a VPC with subnets, AWS recommends provisioning subnets in at least two Availability Zones for a production environment, and a NAT gateway in each AZ with resources that need internet access.
  link: [provision subnets in at least two Availability Zones for a production environment](../facts/vpc.md#vpc-create-two-azs-for-production)
  link: [deploy a NAT gateway in each AZ with resources that need access to the public internet](../facts/vpc.md#vpc-create-two-azs-for-production)
  say: at least two AZs
vpc-create-vpc-and-more-resources
  claim: The VPC and more option of the console creates a VPC plus the resources an application needs, such as subnets, route tables, internet gateways and NAT gateways, and can optionally add an egress-only internet gateway and an S3 gateway endpoint.
  link: [create a VPC plus the additional VPC resources that you need to run your application, such as subnets, route tables, internet gateways, and NAT gateways](../facts/vpc.md#vpc-create-vpc-and-more-resources)
  link: [This creates a gateway VPC endpoint for Amazon S3](../facts/vpc.md#vpc-create-vpc-and-more-resources)
  say: a VPC with subnets, route tables and gateways
vpc-custom-route-table-delete-only-without-associations
  claim: You can add, remove and modify routes in a custom route table, and you can delete a custom route table only if it has no associations; leaving the main route table in its default state and explicitly associating each subnet with a custom table gives you explicit control over routing.
  scope: per route table.
  link: [delete a custom route table only if it has no associations](../facts/vpc.md#vpc-custom-route-table-delete-only-without-associations)
  link: [leave the main route table in its original default state](../facts/vpc.md#vpc-custom-route-table-delete-only-without-associations)
  say: delete it only when no subnet uses it | keep the main route table untouched
vpc-data-transfer-ec2-to-s3-same-region-free
  claim: Data transfer from an EC2 instance to Amazon S3 in the same Region has no data transfer charge, but if the traffic passes through a NAT gateway the NAT gateway data processing charge still applies.
  scope: per GB, EC2 to S3 in the same Region; same Region; NAT gateway processing is a separate charge.
  link: [There was no charge for the data transfer from the EC2 instance to S3](../facts/vpc.md#vpc-data-transfer-ec2-to-s3-same-region-free)
  say: no transfer charge from EC2 to S3 in the same Region
vpc-data-transfer-out-100-gb-free
  claim: AWS customers get 100 GB of data transfer out to the internet free each month, aggregated across all AWS services and Regions except China and GovCloud.
  scope: per account, per month, across all services and Regions; maximum; except China and GovCloud Regions.
  link: [100 GB of free data transfer out to the internet](../facts/vpc.md#vpc-data-transfer-out-100-gb-free)
  say: one hundred gigabytes a month free
vpc-data-transfer-out-internet-example-rate
  claim: In the VPC pricing example for US East (Ohio), Data Transfer Out to the internet is charged at $0.09 per GB, on top of the NAT gateway charges.
  scope: per GB out to the internet, US East (Ohio) example; example rate; the tiered rates are on the EC2 pricing page.
  link: [$0.09 per GB](../facts/vpc.md#vpc-data-transfer-out-internet-example-rate)
  say: nine cents per gigabyte
vpc-data-transfer-public-ip-regional-rate
  claim: Regional Data Transfer rates apply to traffic between EC2 instances when the other instance is in a different Availability Zone, whatever address type is used, or when public or Elastic IP addresses are used, whichever Availability Zone the other instance is in; you are charged only once for a given instance even if both are true.
  scope: traffic between EC2 instances in one Region; Regional Data Transfer rates; the rate itself is on the EC2 pricing page.
  link: [Public or Elastic IP addresses are used, regardless of which Availability Zone the other instance is in](../facts/vpc.md#vpc-data-transfer-public-ip-regional-rate)
  link: [The other instance is in a different Availability Zone, regardless of which type of address is used](../facts/vpc.md#vpc-data-transfer-public-ip-regional-rate)
  link: [you are only charged once for a given instance even if both are true](../facts/vpc.md#vpc-data-transfer-public-ip-regional-rate)
  say: public or Elastic IP addresses cost Regional data transfer, even in the same zone | a different Availability Zone costs Regional data transfer, whatever the address | you pay once, not twice
vpc-decision-guide-connect-to-aws-options
  claim: To connect to VPCs, the decision guide suggests AWS Client VPN for remote users, AWS Site-to-Site VPN for an entire on-premises network, and Direct Connect when you need more consistent performance than the internet can provide.
  link: [consider using AWS Client VPN](../facts/vpc.md#vpc-decision-guide-connect-to-aws-options)
  link: [consider using AWS Site-to-Site VPN](../facts/vpc.md#vpc-decision-guide-connect-to-aws-options)
  link: [more consistent performance than the internet can provide](../facts/vpc.md#vpc-decision-guide-connect-to-aws-options)
vpc-decision-guide-deploy-multiple-azs
  claim: The networking decision guide says to deploy workloads in your VPCs to multiple Availability Zones so that the workload stays available if a single Availability Zone fails.
  link: [deploy to multiple Availability Zones](../facts/vpc.md#vpc-decision-guide-deploy-multiple-azs)
vpc-decision-guide-enhanced-protection-services
  claim: Amazon VPC secures access to workloads, and for enhanced protection the decision guide names AWS Network Firewall, AWS Shield, AWS WAF and Amazon Route 53 Resolver DNS Firewall.
  link: [AWS Network Firewall, AWS Shield, AWS WAF, and Amazon Route 53 Resolver DNS Firewall](../facts/vpc.md#vpc-decision-guide-enhanced-protection-services)
vpc-decision-guide-ipam-automate
  claim: Managing the IP addresses of workloads in multiple VPCs can be difficult; Amazon VPC IPAM automates IP address management across workloads.
  link: [Amazon VPC IPAM](../facts/vpc.md#vpc-decision-guide-ipam-automate)
vpc-decision-guide-privatelink-private-connection
  claim: Workloads in a VPC can call other AWS services through their API endpoints over the public internet; to send that data over a private connection instead, the decision guide says to use AWS PrivateLink.
  link: [API endpoints over the public internet](../facts/vpc.md#vpc-decision-guide-privatelink-private-connection)
  link: [if you want to send data over a private connection, use AWS PrivateLink](../facts/vpc.md#vpc-decision-guide-privatelink-private-connection)
vpc-decision-guide-sg-and-nacl-together
  claim: Security groups and network ACLs can be used together or on their own to secure a network, which supports a defense in depth strategy.
  link: [can be used together or on their own](../facts/vpc.md#vpc-decision-guide-sg-and-nacl-together)
vpc-decision-guide-tgw-vs-cloud-wan
  claim: For connecting networks, the decision guide suggests AWS Transit Gateway if you operate in multiple Regions, want to manage your own routing configurations, or prefer to use your own automation; it suggests AWS Cloud WAN to unify data center, branch and AWS networks with a WAN, and also when you don't want to manage complex routing or build your own multi-Region automation.
  link: [want to manage your own routing configurations, or prefer to use your own automation, consider using AWS Transit Gateway](../facts/vpc.md#vpc-decision-guide-tgw-vs-cloud-wan)
  link: [consider using AWS Cloud WAN](../facts/vpc.md#vpc-decision-guide-tgw-vs-cloud-wan)
vpc-decision-guide-tls-any-transport
  claim: AWS recommends application-level encryption (TLS) regardless of the network transport, as defense in depth for end-to-end confidentiality.
  link: [employ application-level encryption (TLS), irrespective of the transport](../facts/vpc.md#vpc-decision-guide-tls-any-transport)
vpc-decision-guide-vpc-definition
  claim: The networking decision guide describes Amazon VPC as a private, isolated section of the AWS Cloud where you launch resources in a virtual network with customer-defined IP ranges, with several options to connect it to other remote networks.
  link: [provision a private, isolated section of the AWS Cloud where you can launch AWS resources in a virtual network using customer-defined IP address ranges](../facts/vpc.md#vpc-decision-guide-vpc-definition)
  link: [Amazon VPC gives you several options for connecting your AWS virtual networks with other remote networks](../facts/vpc.md#vpc-decision-guide-vpc-definition)
vpc-def-flow-log
  claim: A flow log captures information about the IP traffic going to and from network interfaces in a VPC.
  scope: per flow log.
  link: [captures information about the IP traffic going to and from network interfaces in your VPC](../facts/vpc.md#vpc-def-flow-log)
  say: records information about the IP traffic to and from network interfaces
vpc-def-network-acl
  claim: A network ACL allows or denies specific inbound or outbound traffic at the subnet level.
  scope: per network ACL.
  link: [allows or denies specific inbound or outbound traffic at the subnet level](../facts/vpc.md#vpc-def-network-acl)
  say: an allow-and-deny filter on the subnet
vpc-def-route-table
  claim: Route tables determine where network traffic from a subnet or gateway is directed.
  scope: per route table.
  link: [to determine where network traffic from your subnet or gateway is directed](../facts/vpc.md#vpc-def-route-table)
  say: decides where traffic from a subnet or gateway goes
vpc-def-security-group
  claim: A security group controls the traffic that is allowed to reach and leave the resources it is associated with.
  scope: per security group.
  link: [controls the traffic that is allowed to reach and leave the resources that it is associated with](../facts/vpc.md#vpc-def-security-group)
  say: a virtual firewall on the resource
vpc-default-nacl-allows-all-traffic
  claim: A VPC automatically comes with a default network ACL, configured to allow all traffic to flow in and out of the subnets associated with it; you can modify it by adding rules or removing the default numbered rules.
  scope: default network ACL; default; not adjustable.
  link: [configured to allow all traffic to flow in and out of the subnets with which it is associated](../facts/vpc.md#vpc-default-nacl-allows-all-traffic)
  link: [You can modify a default network ACL by adding rules or removing the default numbered rules](../facts/vpc.md#vpc-default-nacl-allows-all-traffic)
  say: it allows all traffic in and out
vpc-default-service-endpoints-public
  claim: The default AWS service endpoints are public interfaces, so a VPC needs an internet gateway to reach them unless you use AWS PrivateLink, which connects the VPC to AWS services as if they were in the VPC.
  link: [The default service endpoints are public interfaces](../facts/vpc.md#vpc-default-service-endpoints-public)
  link: [you can use AWS PrivateLink to connect your VPC to AWS services as if they were in your VPC, without the use of an internet gateway](../facts/vpc.md#vpc-default-service-endpoints-public)
  say: service endpoints are public by default
vpc-default-sg-cannot-delete
  claim: You can change the rules of a default security group, but you cannot delete a default security group.
  link: [You can't delete a default security group](../facts/vpc.md#vpc-default-sg-cannot-delete)
  link: [You can change the rules for a default security group](../facts/vpc.md#vpc-default-sg-cannot-delete)
  say: the default security group cannot be deleted
vpc-default-sg-inbound-self
  claim: The default inbound rule of a default security group allows inbound traffic from all resources that are assigned to the same security group; the source is the ID of the group itself.
  scope: default security group; default; not adjustable.
  link: [Allows inbound traffic from all resources that are assigned to this security group](../facts/vpc.md#vpc-default-sg-inbound-self)
  say: inbound only from members of the same group
vpc-default-sg-no-internet-inbound
  claim: With its default rules unchanged, the default security group does not let instances receive traffic from the internet gateway or the NAT gateway; AWS recommends a new security group with the required rules instead.
  link: [The default rules do not allow the instances to receive traffic from the internet gateway or the NAT gateway](../facts/vpc.md#vpc-default-sg-no-internet-inbound)
  say: no inbound traffic from the internet with default rules
vpc-default-sg-outbound-all
  claim: The default outbound rules of a default security group allow all outbound IPv4 traffic (0.0.0.0/0), and all outbound IPv6 traffic (::/0) only when the VPC has an IPv6 CIDR block.
  scope: default security group; default; not adjustable.
  link: [Allows all outbound IPv4 traffic](../facts/vpc.md#vpc-default-sg-outbound-all)
  link: [This rule is added only if your VPC has an associated IPv6 CIDR block](../facts/vpc.md#vpc-default-sg-outbound-all)
  say: all outbound traffic
vpc-default-sg-used-when-none-specified
  claim: If you launch an EC2 instance without specifying a security group, AWS associates it with the default security group of its VPC; every default VPC and every VPC you create comes with a default security group named default.
  scope: per VPC; default; not adjustable.
  link: [we associate the instance with the default security group for its VPC](../facts/vpc.md#vpc-default-sg-used-when-none-specified)
  link: [Your default VPCs and any VPCs that you create come with a default security group](../facts/vpc.md#vpc-default-sg-used-when-none-specified)
  say: it gets the VPC default security group
vpc-default-subnet-one-per-az
  claim: You can have only one default subnet per Availability Zone, and you cannot create a default subnet in a nondefault VPC.
  scope: per Availability Zone, per default VPC; maximum.
  link: [only one default subnet per Availability Zone](../facts/vpc.md#vpc-default-subnet-one-per-az)
  link: [cannot create a default subnet in a nondefault VPC](../facts/vpc.md#vpc-default-subnet-one-per-az)
  say: one default subnet per Availability Zone
vpc-default-subnet-per-az
  claim: A default VPC gets a /20 default subnet in each Availability Zone, each with up to 4,096 addresses, a few of which are reserved by AWS.
  scope: per default VPC; default; not adjustable.
  link: [size `/20` default subnet in each Availability Zone](../facts/vpc.md#vpc-default-subnet-per-az)
  link: [up to 4,096 addresses per subnet](../facts/vpc.md#vpc-default-subnet-per-az)
  say: a slash twenty subnet in every Availability Zone
vpc-default-subnet-public-ip-and-dns
  claim: An instance launched into a default subnet receives a public IPv4 address, a private IPv4 address and both public and private DNS hostnames; an instance launched into a nondefault subnet of a default VPC does not receive a public IPv4 address or a DNS hostname.
  scope: per subnet; default; adjustable; you can change the subnet's public IP addressing attribute.
  link: [receive both a public IPv4 address and a private IPv4 address, and both public and private DNS hostnames](../facts/vpc.md#vpc-default-subnet-public-ip-and-dns)
  link: [don't receive a public IPv4 address or a DNS hostname](../facts/vpc.md#vpc-default-subnet-public-ip-and-dns)
  say: a default subnet gives the instance a public address and a public hostname | a nondefault subnet gives no public address
vpc-default-vpc-cidr
  claim: A default VPC is created with a /16 IPv4 CIDR block, 172.31.0.0/16, which provides up to 65,536 private IPv4 addresses.
  scope: per default VPC; default; not adjustable; the default VPC that AWS creates.
  link: [172.31.0.0/16](../facts/vpc.md#vpc-default-vpc-cidr)
  link: [up to 65,536 private IPv4 addresses](../facts/vpc.md#vpc-default-vpc-cidr)
  say: one seventy-two dot thirty-one slash sixteen | about sixty-five thousand addresses
vpc-default-vpc-delete-and-recreate
  claim: If you delete your default VPC you can create a new one, but you cannot restore the deleted default VPC and you cannot mark an existing nondefault VPC as the default VPC.
  scope: per Region, per account.
  link: [If you delete your default VPC, you can create a new one](../facts/vpc.md#vpc-default-vpc-delete-and-recreate)
  link: [cannot restore a previous default VPC that you deleted](../facts/vpc.md#vpc-default-vpc-delete-and-recreate)
  link: [cannot mark an existing nondefault VPC as a default VPC](../facts/vpc.md#vpc-default-vpc-delete-and-recreate)
  say: you can create a new default VPC after deleting it | you cannot turn a normal VPC into the default VPC
vpc-default-vpc-in-each-region
  claim: When you start using Amazon VPC, you have a default VPC in each AWS Region; it comes with a public subnet in each Availability Zone, an internet gateway and settings to enable DNS resolution, so you can start launching EC2 instances into it immediately.
  scope: per Region, per account; default; not adjustable; when you start using Amazon VPC.
  link: [a default VPC in each AWS Region](../facts/vpc.md#vpc-default-vpc-in-each-region)
  link: [a public subnet in each Availability Zone, an internet gateway, and settings to enable DNS resolution](../facts/vpc.md#vpc-default-vpc-in-each-region)
  say: one default VPC per Region
vpc-default-vpc-includes-igw
  claim: A default VPC includes an internet gateway, and each default subnet is a public subnet; an instance launched into a default subnet gets a private IPv4 address and a public IPv4 address and can reach the internet through the internet gateway.
  scope: per default VPC; default; adjustable.
  link: [A default VPC includes an internet gateway](../facts/vpc.md#vpc-default-vpc-includes-igw)
  link: [each default subnet is a public subnet](../facts/vpc.md#vpc-default-vpc-includes-igw)
  say: the default VPC already has an internet gateway | every default subnet is public
vpc-default-vpc-launch-without-subnet
  claim: If a Region has a default VPC and you launch an EC2 instance there without specifying a subnet, AWS chooses one of the default subnets for the instance.
  scope: per Region; the Region has a default VPC.
  link: [we choose one of the default subnets and launch the instance into that subnet](../facts/vpc.md#vpc-default-vpc-launch-without-subnet)
  link: [an EC2 instance that is launched in a default subnet automatically has access to the internet](../facts/vpc.md#vpc-default-vpc-launch-without-subnet)
  say: AWS picks a default subnet for you
vpc-default-vpc-main-route-to-igw
  claim: The main route table of a default VPC has a route that sends all traffic, 0.0.0.0/0, to the internet gateway.
  scope: main route table of a default VPC; default; adjustable; you can remove the route to make the default subnets private.
  link: [points all traffic (`0.0.0.0/0`) to the internet gateway](../facts/vpc.md#vpc-default-vpc-main-route-to-igw)
  link: [0.0.0.0/0](../facts/vpc.md#vpc-default-vpc-main-route-to-igw)
  say: a default route to the internet gateway
vpc-default-vpc-one-per-region
  claim: If you already have a default VPC in a Region, you cannot create another one; an account has at most one default VPC per Region.
  scope: per Region, per account; maximum.
  link: [If you already have a default VPC in the Region, you cannot create another one](../facts/vpc.md#vpc-default-vpc-one-per-region)
  link: [one default VPC per Region](../facts/vpc.md#vpc-default-vpc-one-per-region)
  say: one default VPC per Region
vpc-default-vpc-other-components
  claim: When AWS creates a default VPC it also creates a default security group, a default network ACL and associates the account's default DHCP options set with the VPC.
  scope: per default VPC; default; adjustable.
  link: [Create a default security group and associate it with your default VPC](../facts/vpc.md#vpc-default-vpc-other-components)
  link: [Create a default network access control list (ACL) and associate it with your default VPC](../facts/vpc.md#vpc-default-vpc-other-components)
  link: [Associate the default DHCP options set for your AWS account with your default VPC](../facts/vpc.md#vpc-default-vpc-other-components)
vpc-definition-isolated-virtual-network
  claim: A VPC is a virtual network dedicated to your AWS account and logically isolated from other virtual networks in the AWS Cloud; inside it you specify an IP address range, add subnets, add gateways and associate security groups.
  scope: per VPC.
  link: [a virtual network dedicated to your AWS account](../facts/vpc.md#vpc-definition-isolated-virtual-network)
  link: [logically isolated from other virtual networks in the AWS Cloud](../facts/vpc.md#vpc-definition-isolated-virtual-network)
  link: [specify an IP address range for the VPC, add subnets, add gateways, and associate security groups](../facts/vpc.md#vpc-definition-isolated-virtual-network)
  say: a virtual network dedicated to your account | logically isolated from other virtual networks
vpc-dev-test-one-az-saves-money
  claim: For a development or test environment you might choose to save money by deploying resources in only one Availability Zone.
  link: [save money by deploying your resources in only one Availability Zone](../facts/vpc.md#vpc-dev-test-one-az-saves-money)
vpc-dhcp-default-set-amazonprovideddns
  claim: Each Region has a default DHCP option set that every VPC uses unless you associate a custom set or choose no DHCP option set; the domain name servers of the default set are always AmazonProvidedDNS.
  scope: per Region; default; not adjustable.
  link: [Each Region has a default DHCP option set](../facts/vpc.md#vpc-dhcp-default-set-amazonprovideddns)
  link: [For a default DHCP option set, this is always `AmazonProvidedDNS`](../facts/vpc.md#vpc-dhcp-default-set-amazonprovideddns)
  say: a default option set per Region
vpc-dhcp-new-set-no-restart
  claim: When you associate a new DHCP option set with a VPC, existing and new instances use the new options without a restart or relaunch, picking up the change within a few hours as they renew their DHCP leases.
  link: [You don't need to restart or relaunch your instances](../facts/vpc.md#vpc-dhcp-new-set-no-restart)
  link: [Instances automatically pick up the changes within a few hours](../facts/vpc.md#vpc-dhcp-new-set-no-restart)
  say: no restart needed
vpc-dhcp-one-option-set-per-vpc
  claim: A DHCP option set can be associated with many VPCs, but each VPC can have only one DHCP option set at a time.
  scope: per VPC; maximum.
  link: [each VPC can have only one associated DHCP option set](../facts/vpc.md#vpc-dhcp-one-option-set-per-vpc)
  link: [associate a DHCP option set with multiple VPCs](../facts/vpc.md#vpc-dhcp-one-option-set-per-vpc)
  say: one DHCP option set per VPC
vpc-dhcp-option-set-controls
  claim: DHCP option sets control the DNS servers, domain names and NTP servers that devices in your VPC use, and whether DNS resolution is enabled in the VPC; to use your own DNS server instead of the Amazon DNS server you create a new DHCP option set.
  scope: per VPC.
  link: [The DNS servers, domain names, or Network Time Protocol (NTP) servers used by the devices in your VPC](../facts/vpc.md#vpc-dhcp-option-set-controls)
  link: [To use your own DNS server instead, create a new set of DHCP options for your VPC](../facts/vpc.md#vpc-dhcp-option-set-controls)
  say: DNS servers, domain name and NTP servers | to use your own DNS server, create a new DHCP option set
vpc-dhcp-option-set-delete-in-use
  claim: You cannot delete a DHCP option set while it is in use; first associate a different set, or no set, with each VPC that uses it.
  link: [You can't delete a DHCP option set if it's in use](../facts/vpc.md#vpc-dhcp-option-set-delete-in-use)
  say: not while a VPC uses it
vpc-dhcp-option-set-immutable
  claim: After you create a DHCP option set you cannot modify it; to update the DHCP options of a VPC you create a new option set and associate it with the VPC.
  link: [After you create a DHCP option set, you can't modify it](../facts/vpc.md#vpc-dhcp-option-set-immutable)
  link: [you must create a new DHCP option set and then associate it with your VPC](../facts/vpc.md#vpc-dhcp-option-set-immutable)
  say: a DHCP option set cannot be changed | create a new set and associate it
vpc-dns-attributes-both-needed-for-public-hostnames
  claim: Only when both VPC DNS attributes (enableDnsHostnames and enableDnsSupport) are enabled does an instance with a public IPv4 or Elastic IP address receive a public DNS hostname; if at least one is false, instances with public IP addresses get no public DNS hostname.
  scope: per VPC; enableDnsHostnames and enableDnsSupport.
  link: [If both attributes are enabled, an instance launched into the VPC receives a public DNS hostname if it is assigned a public IPv4 address or an Elastic IP address at creation](../facts/vpc.md#vpc-dns-attributes-both-needed-for-public-hostnames)
  link: [Instances with public IP addresses do not receive corresponding public DNS hostnames](../facts/vpc.md#vpc-dns-attributes-both-needed-for-public-hostnames)
  say: both DNS attributes must be on for public hostnames
vpc-dns-attributes-required-for-private-hosted-zones
  claim: To use custom DNS names from a private hosted zone, or private DNS with interface VPC endpoints (AWS PrivateLink), you must set both enableDnsHostnames and enableDnsSupport to true.
  scope: per VPC; private hosted zone or interface endpoint private DNS.
  link: [must set both the `enableDnsHostnames` and `enableDnsSupport` attributes to `true`](../facts/vpc.md#vpc-dns-attributes-required-for-private-hosted-zones)
  link: [custom DNS domain names defined in a private hosted zone in Amazon Route 53, or use private DNS with interface VPC endpoints (AWS PrivateLink)](../facts/vpc.md#vpc-dns-attributes-required-for-private-hosted-zones)
  say: both DNS attributes must be true
vpc-dns-hostnames-attribute-default
  claim: The enableDnsHostnames attribute determines whether the VPC supports assigning public DNS hostnames to instances with public IP addresses; its default is false unless the VPC is a default VPC.
  scope: per VPC; default; adjustable; true in a default VPC.
  link: [Determines whether the VPC supports assigning public DNS hostnames to instances with public IP addresses](../facts/vpc.md#vpc-dns-hostnames-attribute-default)
  link: [default is false unless the VPC is a default VPC](../facts/vpc.md#vpc-dns-hostnames-attribute-default)
  say: it controls public DNS hostnames | off by default, on in a default VPC
vpc-dns-resolver-1024-pps-per-eni
  claim: Each EC2 instance can send 1024 packets per second per network interface to Route 53 Resolver (the .2 address or 169.254.169.253), and this quota cannot be increased.
  scope: per network interface, per EC2 instance; fixed; not adjustable; traffic to Route 53 Resolver.
  link: [1024 packets per second per network interface](../facts/vpc.md#vpc-dns-resolver-1024-pps-per-eni)
  link: [This quota cannot be increased](../facts/vpc.md#vpc-dns-resolver-1024-pps-per-eni)
  say: one thousand twenty-four packets per second per network interface | it cannot be raised
vpc-dns-resolver-addresses
  claim: The Route 53 Resolver (Amazon DNS server) of a VPC is reachable at 169.254.169.253 over IPv4, at fd00:ec2::253 over IPv6, and at the primary private IPv4 CIDR range of the VPC plus two (for a 10.0.0.0/16 VPC, 10.0.0.2).
  scope: per VPC; fixed; not adjustable; the plus-two address is in the primary IPv4 CIDR block.
  link: [169.254.169.253](../facts/vpc.md#vpc-dns-resolver-addresses)
  link: [plus two](../facts/vpc.md#vpc-dns-resolver-addresses)
  link: [10.0.0.2](../facts/vpc.md#vpc-dns-resolver-addresses)
  say: one sixty-nine dot two fifty-four dot one sixty-nine dot two fifty-three | the VPC base address plus two | ten dot zero dot zero dot two
vpc-dns-resolver-built-into-each-az
  claim: The Route 53 Resolver, also called the Amazon DNS server or AmazonProvidedDNS, is a DNS resolver service built into each Availability Zone in a Region.
  scope: per Availability Zone.
  link: [The Route 53 Resolver (also called "Amazon DNS server" or "AmazonProvidedDNS")](../facts/vpc.md#vpc-dns-resolver-built-into-each-az)
  link: [built into each Availability Zone in an AWS Region](../facts/vpc.md#vpc-dns-resolver-built-into-each-az)
  say: the Route 53 Resolver, also called AmazonProvidedDNS
vpc-dns-server-not-filterable
  claim: You cannot filter traffic to or from the Amazon DNS server with network ACLs or security groups.
  scope: per VPC; fixed.
  link: [cannot filter traffic to or from the Amazon DNS server using network ACLs or security groups](../facts/vpc.md#vpc-dns-server-not-filterable)
  link: [Amazon DNS server](../facts/vpc.md#vpc-dns-server-not-filterable)
  say: security groups and network ACLs do not filter traffic to the Amazon DNS server
vpc-dns-support-attribute-default
  claim: The enableDnsSupport attribute determines whether the VPC supports DNS resolution through the Amazon provided DNS server; its default is true.
  scope: per VPC; default; adjustable.
  link: [Determines whether the VPC supports DNS resolution through the Amazon provided DNS server](../facts/vpc.md#vpc-dns-support-attribute-default)
  link: [its default is true](../facts/vpc.md#vpc-dns-support-attribute-default)
  say: it turns Amazon DNS resolution on or off | on by default
vpc-dns64-per-subnet-synthesizes
  claim: DNS64 is enabled per subnet and applies to all resources in it; when a DNS record has no IPv6 address, Route 53 Resolver synthesizes one by prepending the well-known 64:ff9b::/96 prefix to the IPv4 address.
  link: [you can enable DNS64 for a subnet and it applies to all the AWS resources within that subnet](../facts/vpc.md#vpc-dns64-per-subnet-synthesizes)
  link: [64:ff9b::/96](../facts/vpc.md#vpc-dns64-per-subnet-synthesizes)
  say: turn it on per subnet
vpc-ec2-classic-retired
  claim: EC2-Classic, a single flat network shared with other customers, is deprecated and Amazon VPC replaces it: instances run in a VPC that is logically isolated to your AWS account. The VPC FAQ announced the retirement of EC2-Classic for August 15, 2022, and the VPC guide history marks the deprecation on July 31, 2023.
  scope: all AWS accounts.
  link: [August 15, 2022](../facts/vpc.md#vpc-ec2-classic-retired)
  link: [Amazon VPC replaces EC2-Classic](../facts/vpc.md#vpc-ec2-classic-retired)
  say: August fifteenth, twenty twenty-two (announced retirement date) | every instance now lives in a VPC
vpc-eic-private-ipv4-admin-access
  claim: EC2 Instance Connect can connect to instances using their private IPv4 addresses, so you no longer need public IPv4 addresses for administrative access (generally SSH or RDP).
  scope: per instance.
  link: [you no longer need to use public IPv4 addresses for administrative purposes](../facts/vpc.md#vpc-eic-private-ipv4-admin-access)
  say: no public IP needed for admin access
vpc-eigw-ipv6-outbound-only
  claim: An egress-only internet gateway allows outbound IPv6 communication from instances to the internet and prevents the internet from initiating IPv6 connections to them; it is for IPv6 only, and for outbound-only IPv4 you use a NAT gateway instead.
  scope: per egress-only internet gateway.
  link: [allows outbound communication over IPv6 from instances in your VPC to the internet, and prevents the internet from initiating an IPv6 connection with your instances](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  link: [for use with IPv6 traffic only](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  link: [To enable outbound-only internet communication over IPv4, use a NAT gateway instead](../facts/vpc.md#vpc-eigw-ipv6-outbound-only)
  say: outbound-only internet access for IPv6 | IPv6 only
vpc-eigw-stateful-no-security-group
  claim: An egress-only internet gateway is stateful: it forwards outbound traffic and returns the responses; you cannot attach a security group to it, but a network ACL on the subnet can control its traffic, and there is no charge for the gateway.
  scope: per egress-only internet gateway.
  link: [An egress-only internet gateway is stateful](../facts/vpc.md#vpc-eigw-stateful-no-security-group)
  link: [can't associate a security group with an egress-only internet gateway](../facts/vpc.md#vpc-eigw-stateful-no-security-group)
  link: [no charge for an egress-only internet gateway](../facts/vpc.md#vpc-eigw-stateful-no-security-group)
  say: it is stateful | no security group on it
vpc-eip-ipv6-not-supported
  claim: Elastic IP addresses for IPv6 are not supported; IPv6 addresses are globally unique and therefore public by default.
  scope: IPv6; fixed.
  link: [Elastic IP addresses for IPv6 are not supported](../facts/vpc.md#vpc-eip-ipv6-not-supported)
  link: [IPv6 addresses are globally unique, and therefore public by default](../facts/vpc.md#vpc-eip-ipv6-not-supported)
  say: no Elastic IPs for IPv6 | an IPv6 address is already public
vpc-eip-persistent-until-released
  claim: An Elastic IP address is a persistent public IPv4 address allocated to your account that you can assign to and remove from instances as you need; it stays allocated to your account until you explicitly release it.
  scope: per Elastic IP address.
  link: [a persistent public IP address allocated to your account](../facts/vpc.md#vpc-eip-persistent-until-released)
  link: [remains allocated to your AWS account until you explicitly release it](../facts/vpc.md#vpc-eip-persistent-until-released)
  say: a static public address that belongs to your account
vpc-eip-regional
  claim: Elastic IP addresses are regional: an Elastic IP address belongs to one Region.
  scope: per Elastic IP address; fixed.
  link: [Elastic IP addresses are regional](../facts/vpc.md#vpc-eip-regional)
  link: [regional](../facts/vpc.md#vpc-eip-regional)
  say: an Elastic IP is Regional
vpc-eip-single-association-and-move
  claim: An Elastic IP address can be associated with a single instance or network interface at a time, and you can move it from one instance or network interface to another.
  scope: per Elastic IP address; maximum.
  link: [associated with a single instance or network interface at a time](../facts/vpc.md#vpc-eip-single-association-and-move)
  link: [move an Elastic IP address from one instance or network interface to another](../facts/vpc.md#vpc-eip-single-association-and-move)
  say: one instance or interface at a time | you can move it between instances
vpc-eip-transfer-change
  claim: Since October 31, 2022 you can transfer Elastic IP addresses from one AWS account to another.
  scope: per Elastic IP address.
  link: [October 31, 2022](../facts/vpc.md#vpc-eip-transfer-change)
  link: [transfer Elastic IP addresses from one AWS account to another](../facts/vpc.md#vpc-eip-transfer-change)
  say: October thirty-first, twenty twenty-two | Elastic IPs can be transferred between accounts
vpc-encryption-controls-change
  claim: VPC Encryption Controls, added November 21, 2025, let you audit and enforce encryption in transit for traffic within and across VPCs; the feature can be used in two modes, monitor mode and enforce mode.
  scope: per VPC.
  link: [November 21, 2025](../facts/vpc.md#vpc-encryption-controls-change)
  link: [monitor mode and enforce mode](../facts/vpc.md#vpc-encryption-controls-change)
  say: November twenty-first, twenty twenty-five | two modes: monitor and enforce
vpc-encryption-controls-declarative-policy
  claim: An AWS Organizations declarative policy can turn on VPC Encryption Controls in monitor or enforce mode across all VPCs of an account, an organizational unit or the whole organization.
  scope: per AWS Organization, OU or account.
  link: [use declarative policies to turn on VPC Encryption Controls in monitor or enforce mode across all VPCs](../facts/vpc.md#vpc-encryption-controls-declarative-policy)
  say: a declarative policy switches it on for every VPC in the organization
vpc-encryption-controls-enforce-existing-vpc
  claim: You cannot turn on VPC Encryption Controls enforce mode directly on an existing VPC: you must start in monitor mode, fix or exclude the non-compliant resources, and then switch to enforce mode. A new VPC can be created in enforce mode.
  scope: per VPC.
  link: [cannot enable Encryption Controls in enforce mode directly on your existing VPCs](../facts/vpc.md#vpc-encryption-controls-enforce-existing-vpc)
  say: existing VPCs start in monitor mode; only new VPCs can be created in enforce mode
vpc-encryption-controls-exclusions-8
  claim: Only 8 resource types can be excluded from VPC Encryption Controls enforce mode: internet gateway, NAT gateway, egress-only internet gateway, VPC peering, virtual private gateway, Lambda, VPC Lattice and Elastic File System; no other resource can be excluded.
  scope: per VPC in enforce mode; fixed; not adjustable.
  link: [only 8 supported exclusions](../facts/vpc.md#vpc-encryption-controls-exclusions-8)
  link: [Internet Gateway, NAT Gateway, Egress-only Internet Gateway, VPC Peering, Virtual Private Gateway, Lambda, VPC Lattice, and Elastic File System](../facts/vpc.md#vpc-encryption-controls-exclusions-8)
  say: exactly eight exclusion types | internet gateway, NAT gateway, egress-only gateway, peering, virtual private gateway, Lambda, Lattice and EFS
vpc-encryption-controls-flow-log-field
  claim: You can audit the encryption status of traffic flows inside a VPC with the encryption-status field of VPC Flow Logs; the encryption-status field is not automatically added to existing flow logs.
  scope: per flow log.
  link: [encryption-status](../facts/vpc.md#vpc-encryption-controls-flow-log-field)
  say: the encryption-status flow log field
vpc-encryption-controls-pricing-change
  claim: Starting March 1, 2026, VPC Encryption Controls moved from a free preview to a paid feature: a fixed hourly rate for every non-empty VPC (one with network interfaces) that has Encryption Controls on in monitor or enforce mode; empty VPCs with Encryption Controls on are not charged.
  scope: per non-empty VPC, per hour, per Region; Encryption Controls enabled in monitor or enforce mode.
  link: [March 1, 2026](../facts/vpc.md#vpc-encryption-controls-pricing-change)
  link: [free preview](../facts/vpc.md#vpc-encryption-controls-pricing-change)
  link: [fixed hourly rate for every non-empty VPC](../facts/vpc.md#vpc-encryption-controls-pricing-change)
  say: March first, twenty twenty-six | it used to be a free preview | a fixed hourly rate for each VPC that has network interfaces
  changed: 2026-03-01: was free preview
vpc-encryption-controls-pricing-dimension
  claim: VPC Encryption Controls is charged a flat hourly rate, set per Region, for every non-empty VPC (one that has a network interface) running in monitor or enforce mode.
  scope: per non-empty VPC, per hour.
  link: [flat rate (based on region) per hour for every non-empty VPC](../facts/vpc.md#vpc-encryption-controls-pricing-dimension)
  say: a flat hourly rate per non-empty VPC
vpc-encryption-controls-tgw-charges-attached-vpcs
  claim: When you enable encryption support on a transit gateway, VPC Encryption Controls charges apply to every VPC attached to that transit gateway, whatever its Encryption Controls mode (monitor, enforce or off), even an empty VPC.
  scope: per VPC attached to a transit gateway with encryption support; encryption support enabled on the transit gateway.
  link: [standard VPC Encryption Controls charges apply to all VPCs attached to that Transit Gateway](../facts/vpc.md#vpc-encryption-controls-tgw-charges-attached-vpcs)
  say: every attached VPC is billed, even empty ones
vpc-endpoint-policy-default-full-access
  claim: You can attach a single endpoint policy to an interface or gateway endpoint for an AWS service, and for an S3 gateway endpoint the default policy allows full access.
  scope: per VPC endpoint; default; not adjustable.
  link: [you can attach a single endpoint policy to the endpoint](../facts/vpc.md#vpc-endpoint-policy-default-full-access)
  link: [The default policy allows full access](../facts/vpc.md#vpc-endpoint-policy-default-full-access)
  say: one policy per endpoint | full access by default
vpc-endpoint-policy-definition
  claim: An endpoint policy is a resource-based policy attached to a VPC endpoint that controls which AWS principals can use the endpoint to reach an AWS service; it does not override or replace identity-based or resource-based policies.
  link: [a resource-based policy that you attach to a VPC endpoint to control which AWS principals can use the endpoint to access an AWS service](../facts/vpc.md#vpc-endpoint-policy-definition)
  link: [An endpoint policy does not override or replace identity-based policies or resource-based policies](../facts/vpc.md#vpc-endpoint-policy-definition)
  say: a resource policy on the endpoint
vpc-eni-one-eip-per-private-ip
  claim: You can associate one Elastic IP address with each private IPv4 address of a network interface.
  link: [You can associate one Elastic IP address with each private IPv4 address](../facts/vpc.md#vpc-eni-one-eip-per-private-ip)
  say: one Elastic IP per private IP
vpc-eni-primary-cannot-detach
  claim: Each instance has a default primary network interface that you cannot detach; you can attach secondary network interfaces, up to a maximum that varies by instance type.
  link: [You can't detach a primary network interface from an instance](../facts/vpc.md#vpc-eni-primary-cannot-detach)
  link: [The maximum number of network interfaces varies by instance type](../facts/vpc.md#vpc-eni-primary-cannot-detach)
  say: the primary interface stays
vpc-eni-public-ip-released-on-stop
  claim: AWS releases the public IP address of an instance when it is stopped, hibernated or terminated, and assigns a new one when it starts again, unless it has a secondary network interface or secondary private IPv4 address associated with an Elastic IP address.
  link: [We release the public IP address when the instance is stopped, hibernated, or terminated](../facts/vpc.md#vpc-eni-public-ip-released-on-stop)
  link: [We assign a new public IP address when you start your stopped or hibernated instance](../facts/vpc.md#vpc-eni-public-ip-released-on-stop)
  say: it is released on stop | a new one on start
vpc-eni-same-az-attributes-move
  claim: An elastic network interface is a logical networking component of a VPC that represents a virtual network card; you can attach it to instances in the same Availability Zone, and its attributes follow it when you detach it and attach it to another instance.
  link: [a logical networking component in a VPC that represents a virtual network card](../facts/vpc.md#vpc-eni-same-az-attributes-move)
  link: [attach them to instances that you launch in the same Availability Zone](../facts/vpc.md#vpc-eni-same-az-attributes-move)
  link: [The attributes of a network interface follow it as it's attached or detached from an instance and reattached to another instance](../facts/vpc.md#vpc-eni-same-az-attributes-move)
  say: a virtual network card
vpc-eni-secondary-private-ip-reassignable
  claim: Unlike primary private IP addresses, secondary private IPv4 addresses can be reassigned from one instance to another.
  link: [secondary private IP addresses can be reassigned from one instance to another](../facts/vpc.md#vpc-eni-secondary-private-ip-reassignable)
  say: secondary private IPs can move
vpc-eni-source-dest-check-default-on
  claim: Source/destination checks are enabled by default on a network interface, and you must disable them if the instance runs services such as network address translation, routing or firewalls.
  scope: per network interface; default; not adjustable.
  link: [Source/destination checks are enabled by default](../facts/vpc.md#vpc-eni-source-dest-check-default-on)
  link: [You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls](../facts/vpc.md#vpc-eni-source-dest-check-default-on)
  say: on by default
vpc-example-private-route-table
  claim: In the private-subnet example the console creates a route table for the private subnets with the local route plus routes to the NAT gateway, the egress-only internet gateway and the gateway VPC endpoint, and a separate route table for the public subnets with routes to the internet gateway.
  link: [a route table for the public subnets with local routes and routes to the internet gateway](../facts/vpc.md#vpc-example-private-route-table)
  link: [a route table for the private subnets with local routes, and routes to the NAT gateway, egress-only internet gateway, and gateway VPC endpoint](../facts/vpc.md#vpc-example-private-route-table)
vpc-example-private-servers-nat-both-azs
  claim: The guide's private-subnet production example places the servers in private subnets behind a load balancer, gives them internet access through a NAT gateway, and deploys the NAT gateway in both Availability Zones for resiliency.
  link: [For additional security, you deploy the servers in private subnets](../facts/vpc.md#vpc-example-private-servers-nat-both-azs)
  link: [you deploy the NAT gateway in both Availability Zones](../facts/vpc.md#vpc-example-private-servers-nat-both-azs)
vpc-example-s3-gateway-endpoint-no-cost-default
  claim: In the VPC guide's example of a VPC with servers in private subnets and NAT, S3 Gateway is the default VPC endpoint option and there is no cost for this option; the guide says that otherwise the instances in that example's private subnet can't access Amazon S3.
  scope: the VPC guide example of a VPC with servers in private subnets and NAT.
  link: [There is no cost for this option](../facts/vpc.md#vpc-example-s3-gateway-endpoint-no-cost-default)
  link: [Otherwise, instances in your private subnet can't access Amazon S3](../facts/vpc.md#vpc-example-s3-gateway-endpoint-no-cost-default)
vpc-example-web-db-two-tier-layout
  claim: The guide's two-tier example puts public and private subnets in two Availability Zones: web servers in public subnets receive client traffic through a load balancer, database servers in private subnets receive traffic from the web servers (their security group allows traffic from the web servers), and the database servers reach Amazon S3 through a gateway VPC endpoint.
  link: [The VPC has public subnets and private subnets in two Availability Zones](../facts/vpc.md#vpc-example-web-db-two-tier-layout)
  link: [The database servers run in the private subnets and receive traffic from the web servers](../facts/vpc.md#vpc-example-web-db-two-tier-layout)
  link: [The database servers can connect to Amazon S3 by using a gateway VPC endpoint](../facts/vpc.md#vpc-example-web-db-two-tier-layout)
vpc-faq-assign-ip-conditions
  claim: An IP address you assign to an instance must be part of the subnet's IP address range, must not be reserved by Amazon for IP networking purposes, and must not be currently assigned to another interface.
  scope: per instance.
  link: [Part of the associated subnet's IP address range](../facts/vpc.md#vpc-faq-assign-ip-conditions)
  link: [Not reserved by Amazon for IP networking purposes](../facts/vpc.md#vpc-faq-assign-ip-conditions)
  link: [Not currently assigned to another interface](../facts/vpc.md#vpc-faq-assign-ip-conditions)
  say: inside the subnet range | not one of the reserved addresses | not already used by another interface
vpc-faq-available-multiple-azs-all-regions
  claim: Amazon VPC is available in multiple Availability Zones in all Amazon EC2 Regions.
  scope: per Region.
  link: [available in multiple Availability Zones in all Amazon EC2 regions](../facts/vpc.md#vpc-faq-available-multiple-azs-all-regions)
  say: every EC2 Region, across several AZs
vpc-faq-byoip-eip-release-returns-to-pool
  claim: A released BYOIP Elastic IP goes back to the BYOIP address pool it was allocated from.
  scope: per BYOIP Elastic IP.
  link: [it goes back to the BYOIP IP pool from which it was allocated](../facts/vpc.md#vpc-faq-byoip-eip-release-returns-to-pool)
  say: it returns to your BYOIP pool
vpc-faq-byoip-many-vpcs-same-account
  claim: You can use a BYOIP prefix with any number of VPCs in the same account.
  scope: per BYOIP prefix; same account.
  link: [any number of VPCs in the same account](../facts/vpc.md#vpc-faq-byoip-many-vpcs-same-account)
  say: any number of VPCs in the same account
vpc-faq-byoip-max-five-ranges
  claim: You can bring a maximum of five IP ranges to your account with BYOIP.
  scope: per account; maximum; not adjustable.
  link: [a maximum of five IP ranges](../facts/vpc.md#vpc-faq-byoip-max-five-ranges)
  say: five ranges per account
vpc-faq-byoip-most-specific-prefix
  claim: The most specific prefix you can bring with BYOIP is a /24 for IPv4 and a /56 for IPv6.
  scope: per BYOIP prefix; minimum; not adjustable; an IPv6 prefix advertised to the internet must be /48 or larger.
  link: [/24 IPv4 prefix](../facts/vpc.md#vpc-faq-byoip-most-specific-prefix)
  link: [/56 IPv6 prefix](../facts/vpc.md#vpc-faq-byoip-most-specific-prefix)
  say: slash twenty-four for IPv4 | slash fifty-six for IPv6
vpc-faq-byoip-move-region
  claim: To move a BYOIP prefix to another Region, you deprovision it from the current Region and then provision it in the new Region.
  scope: per BYOIP prefix.
  link: [de-provisioning the BYOIP prefix from the current region and then provisioning it to the new region](../facts/vpc.md#vpc-faq-byoip-move-region)
  say: deprovision, then provision in the new Region
vpc-faq-byoip-reasons
  claim: One reason to bring your own IP addresses is IP allow lists: BYOIP lets you move workloads that rely on allow-listed IP addresses to AWS without re-establishing the lists with new addresses.
  scope: per BYOIP range.
  link: [move workloads that rely on IP address whitelisting to AWS without the need to re-establish the whitelists with new IP addresses](../facts/vpc.md#vpc-faq-byoip-reasons)
  say: keep partners' allow lists working
vpc-faq-byoip-what
  claim: Bring Your Own IP (BYOIP) lets you move all or part of your existing publicly routable IPv4 or IPv6 address space to AWS for use with your AWS resources, and you continue to own the IP range.
  scope: per account; publicly routable address space.
  link: [move all or part of their existing publicly routable IPv4 or IPv6 address space to AWS](../facts/vpc.md#vpc-faq-byoip-what)
  link: [Customers will continue to own the IP range](../facts/vpc.md#vpc-faq-byoip-what)
  say: bring your own public address space to AWS | you still own the range
vpc-faq-connectivity-to-aws-services
  claim: A VPC can connect to other AWS services through an internet gateway, NAT, a virtual private gateway or VPC endpoints.
  scope: per VPC.
  link: [Other AWS services (via internet gateway, NAT, virtual private gateway, or VPC endpoints)](../facts/vpc.md#vpc-faq-connectivity-to-aws-services)
  say: internet gateway, NAT, virtual private gateway or endpoints
vpc-faq-cross-az-data-transfer-charge
  claim: Traffic between instances in subnets in different Availability Zones is charged $0.01 per GB for data transfer.
  scope: per GB, between Availability Zones in one Region; fixed; instances in subnets in different Availability Zones.
  link: [$0.01 per GB](../facts/vpc.md#vpc-faq-cross-az-data-transfer-charge)
  say: one cent per gigabyte
vpc-faq-cross-region-instance-communication
  claim: Instances in VPCs in different Regions can communicate using inter-Region VPC peering, public IP addresses, NAT gateways, NAT instances, VPN connections or Direct Connect connections.
  scope: VPCs in different Regions.
  link: [Inter-Region VPC Peering, public IP addresses, NAT gateway, NAT instances, VPN Connections or Direct Connect connections](../facts/vpc.md#vpc-faq-cross-region-instance-communication)
  say: inter-Region peering, public IPs, NAT, VPN or Direct Connect
vpc-faq-def-egress-only-internet-gateway
  claim: An egress-only internet gateway is a stateful gateway that gives IPv6 traffic egress-only access from the VPC to the internet.
  scope: per egress-only internet gateway; IPv6 traffic.
  link: [A stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet](../facts/vpc.md#vpc-faq-def-egress-only-internet-gateway)
  say: a stateful, outbound-only gateway for IPv6
vpc-faq-def-internet-gateway
  claim: An internet gateway is the VPC side of a connection to the public internet.
  scope: per internet gateway.
  link: [The Amazon VPC side of a connection to the public Internet](../facts/vpc.md#vpc-faq-def-internet-gateway)
  say: the VPC side of a connection to the public internet
vpc-faq-def-nat-gateway
  claim: A NAT gateway is a highly available, managed network address translation service that lets resources in a private subnet access the internet.
  scope: per NAT gateway.
  link: [A highly available, managed Network Address Translation (NAT) service for your resources in a private subnet to access the Internet](../facts/vpc.md#vpc-faq-def-nat-gateway)
  say: a managed, highly available NAT service for private subnets
vpc-faq-def-subnet
  claim: A subnet is a segment of a VPC's IP address range where you place groups of isolated resources.
  scope: per subnet.
  link: [A segment of a VPC's IP address range where you can place groups of isolated resources](../facts/vpc.md#vpc-faq-def-subnet)
  say: a segment of the VPC's IP address range
vpc-faq-def-virtual-private-gateway
  claim: A virtual private gateway is the VPC side of a VPN connection.
  scope: per virtual private gateway.
  link: [The Amazon VPC side of a VPN connection](../facts/vpc.md#vpc-faq-def-virtual-private-gateway)
  say: the VPC side of a VPN connection
vpc-faq-def-vpc
  claim: A VPC is a logically isolated virtual network in the AWS cloud; you define its IP address space from ranges you select.
  scope: per VPC.
  link: [A logically isolated virtual network in the AWS cloud](../facts/vpc.md#vpc-faq-def-vpc)
  link: [You define a VPC's IP address space from ranges you select](../facts/vpc.md#vpc-faq-def-vpc)
  say: a logically isolated virtual network in the AWS cloud
vpc-faq-def-vpc-endpoints
  claim: VPC endpoints give private connectivity from your VPC to services hosted in AWS without an internet gateway, VPN, NAT device or firewall proxy.
  scope: per VPC endpoint.
  link: [Enables private connectivity to services hosted in AWS, from within your VPC without using an Internet Gateway, VPN, Network Address Translation (NAT) devices, or firewall proxies](../facts/vpc.md#vpc-faq-def-vpc-endpoints)
  say: private connectivity to AWS services from inside the VPC, with no internet gateway or NAT
vpc-faq-default-route-per-subnet
  claim: Each subnet can have its own default route, which sends traffic out of the VPC through the internet gateway, the virtual private gateway or the NAT gateway.
  scope: per subnet.
  link: [You may create a default route for each subnet](../facts/vpc.md#vpc-faq-default-route-per-subnet)
  link: [the Internet gateway, the virtual private gateway, or the NAT gateway](../facts/vpc.md#vpc-faq-default-route-per-subnet)
  say: one default route per subnet
vpc-faq-default-vpc-nondefault-subnets
  claim: You can add nondefault subnets, such as private subnets, to a default VPC; to launch into one you target it with the console or the --subnet option of the CLI, API or SDK.
  scope: per default VPC.
  link: [target your launches using the console or the --subnet option from the CLI, API, or SDK](../facts/vpc.md#vpc-faq-default-vpc-nondefault-subnets)
  say: name the subnet at launch
vpc-faq-default-vpc-what
  claim: A default VPC is a logically isolated virtual network that AWS creates automatically for your account the first time you provision EC2 resources; an instance launched without a subnet ID goes into the default VPC.
  scope: per account, per Region.
  link: [automatically created for your AWS account the first time you provision Amazon EC2 resources](../facts/vpc.md#vpc-faq-default-vpc-what)
  link: [When you launch an instance without specifying a subnet-ID, your instance will be launched in your default VPC](../facts/vpc.md#vpc-faq-default-vpc-what)
  say: AWS creates it for you automatically | no subnet given means the default VPC
vpc-faq-eip-internet-only-not-vpn
  claim: You can assign Elastic IP addresses to instances in a VPC, but those addresses are reachable only from the internet, not over the VPN connection.
  scope: per Elastic IP address.
  link: [the EIP addresses will only be reachable from the Internet (not over the VPN connection)](../facts/vpc.md#vpc-faq-eip-internet-only-not-vpn)
  say: reachable from the internet only, not over the VPN
vpc-faq-eip-not-behind-nat
  claim: Elastic IPs should be used only on instances in subnets that route directly to the internet gateway; they cannot be used on instances in subnets that reach the internet through a NAT gateway or NAT instance.
  scope: per Elastic IP address; IPv4.
  link: [only be used on instances in subnets configured to route their traffic directly to the Internet gateway](../facts/vpc.md#vpc-faq-eip-not-behind-nat)
  link: [cannot be used on instances in subnets configured to use a NAT gateway or a NAT instance to access the Internet](../facts/vpc.md#vpc-faq-eip-not-behind-nat)
  say: only in subnets that route to the internet gateway | not behind a NAT gateway
vpc-faq-encryption-controls-enforce-blocks
  claim: Once a VPC is in Enforce mode it prevents the creation or attachment of resources that allow unencrypted traffic within the VPC boundary, and you are blocked from running instances that do not support native Nitro encryption.
  scope: per VPC; Enforce mode enabled.
  link: [prevents the creation or attachment of resources that allow unencrypted traffic within the VPC boundary](../facts/vpc.md#vpc-faq-encryption-controls-enforce-blocks)
  link: [blocked from running instances that don’t support native nitro encryption](../facts/vpc.md#vpc-faq-encryption-controls-enforce-blocks)
  say: no new unencrypted resources
vpc-faq-encryption-controls-what
  claim: VPC Encryption Controls is a security and compliance feature that gives centralized control to monitor and enforce encryption of traffic flows within and across VPCs in a Region, with a Monitor mode for visibility and an Enforce mode that prevents unencrypted traffic.
  scope: per VPC.
  link: [centralized control to monitor and enforce encryption of traffic flows within and across VPCs in a region](../facts/vpc.md#vpc-faq-encryption-controls-what)
  link: [Monitor mode (for visibility, assessment and initiate migration) and Enforce mode (for preventing unencrypted traffic)](../facts/vpc.md#vpc-faq-encryption-controls-what)
  say: central monitoring and enforcement of traffic encryption | Monitor mode and Enforce mode
vpc-faq-endpoint-types-gateway-interface
  claim: The FAQ lists two VPC endpoint types, gateway and interface; gateway endpoints are available only for AWS services including S3 and DynamoDB and work by adding an entry to the route table you select.
  scope: per VPC endpoint.
  link: [gateway type endpoints and interface type endpoints](../facts/vpc.md#vpc-faq-endpoint-types-gateway-interface)
  link: [available only for AWS services including S3 and DynamoDB](../facts/vpc.md#vpc-faq-endpoint-types-gateway-interface)
  link: [add an entry to your route table you selected](../facts/vpc.md#vpc-faq-endpoint-types-gateway-interface)
  say: gateway endpoints and interface endpoints | gateway endpoints: S3 and DynamoDB | they work through a route table entry
vpc-faq-endpoints-no-igw-nat-needed
  claim: VPC endpoints connect a VPC privately to services hosted on AWS without an internet gateway, NAT device, VPN or firewall proxy, and they are horizontally scalable, highly available virtual devices.
  scope: per VPC endpoint.
  link: [without requiring an Internet gateway, a NAT device, VPN, or firewall proxies](../facts/vpc.md#vpc-faq-endpoints-no-igw-nat-needed)
  link: [horizontally scalable and highly available virtual devices](../facts/vpc.md#vpc-faq-endpoints-no-igw-nat-needed)
  say: no internet gateway, NAT, VPN or proxy
vpc-faq-eni-not-for-multiple-websites
  claim: Hosting several websites with separate IP addresses on one instance is not a good use of multiple network interfaces; AWS says to assign additional private IP addresses to the instance and associate Elastic IPs with them as needed.
  scope: per instance.
  link: [assign additional private IP addresses to the instance and then associate EIPs to the private IPs as needed](../facts/vpc.md#vpc-faq-eni-not-for-multiple-websites)
  say: extra private IPs plus Elastic IPs, not extra interfaces
vpc-faq-eni-same-account-only
  claim: A network interface can be attached only to instances in VPCs in the same account.
  scope: per network interface.
  link: [only be attached to instances in VPCs in the same account](../facts/vpc.md#vpc-faq-eni-same-account-only)
  say: same account only
vpc-faq-eni-same-az-only
  claim: A network interface can be attached only to instances in the same Availability Zone.
  scope: per network interface.
  link: [only be attached to instances residing in the same Availability Zone](../facts/vpc.md#vpc-faq-eni-same-az-only)
  say: same Availability Zone only
vpc-faq-flow-logs-analysis-tools
  claim: You can analyze VPC flow logs delivered to CloudWatch Logs with tools like CloudWatch Logs Insights or CloudWatch Contributor Insights, and query flow logs delivered to Amazon S3 with tools like Amazon Athena.
  scope: per flow log destination.
  link: [CloudWatch Log Insights or CloudWatch Contributor Insights](../facts/vpc.md#vpc-faq-flow-logs-analysis-tools)
  link: [Amazon Athena](../facts/vpc.md#vpc-faq-flow-logs-analysis-tools)
  say: CloudWatch Logs Insights or Contributor Insights | Athena for flow logs in S3
vpc-faq-flow-logs-cost-allocation-tags
  claim: You can track the charges from publishing flow logs with cost allocation tags.
  scope: per flow log.
  link: [track charges from publishing flow logs using cost allocation tags](../facts/vpc.md#vpc-faq-flow-logs-cost-allocation-tags)
  say: with cost allocation tags
vpc-faq-flow-logs-create-delete-no-impact
  claim: You can create or delete flow logs without any risk of impact to network performance.
  scope: per flow log.
  link: [create or delete flow logs without any risk of impact to network performance](../facts/vpc.md#vpc-faq-flow-logs-create-delete-no-impact)
  say: no impact on network performance
vpc-faq-flow-logs-nat-gateway-packet-source
  claim: The enriched metadata in flow logs can show who initiated a TCP connection and the actual packet-level source and destination for traffic that passes through intermediate layers such as a NAT gateway.
  scope: per flow log; enriched metadata fields selected.
  link: [the actual packet-level source and destination for traffic flowing through intermediate layers such as the NAT Gateway](../facts/vpc.md#vpc-faq-flow-logs-nat-gateway-packet-source)
  say: the real source and destination behind the NAT gateway
vpc-faq-flow-logs-subscription-options
  claim: When you create a flow log subscription, you choose the metadata fields to capture, the maximum aggregation interval and the log destination.
  scope: per flow log.
  link: [the metadata fields you wish to capture, the maximum aggregation interval, and your preferred log destination](../facts/vpc.md#vpc-faq-flow-logs-subscription-options)
  say: fields, aggregation interval, destination
vpc-faq-flow-logs-transit-gateway
  claim: You can create a VPC flow log for a transit gateway or for an individual transit gateway attachment.
  scope: per transit gateway or attachment.
  link: [for a Transit Gateway or for an individual Transit Gateway attachment](../facts/vpc.md#vpc-faq-flow-logs-transit-gateway)
  say: yes, per transit gateway or per attachment
vpc-faq-flow-logs-troubleshoot-rules
  claim: Flow logs help you troubleshoot connectivity and security issues and make sure that network access rules work as expected.
  scope: per flow log.
  link: [troubleshoot connectivity and security issues and to make sure that the network access rules are working as expected](../facts/vpc.md#vpc-faq-flow-logs-troubleshoot-rules)
  say: check that access rules work
vpc-faq-flow-logs-use-cases
  claim: You can monitor VPC flow logs to see network dependencies and traffic patterns, detect anomalies and prevent data leakage, troubleshoot connectivity and configuration issues, and archive them to meet compliance requirements.
  scope: per flow log.
  link: [detect anomalies and prevent data leakage, or troubleshoot network connectivity and configuration issues](../facts/vpc.md#vpc-faq-flow-logs-use-cases)
  link: [archive your flow logs to meet compliance requirements](../facts/vpc.md#vpc-faq-flow-logs-use-cases)
  say: find anomalies and troubleshoot connectivity | archive for compliance
vpc-faq-flow-logs-vs-traffic-mirroring
  claim: Flow logs record metadata about flows (allowed and denied traffic, source and destination addresses, ports, protocol number, packet and byte counts, accept or reject); traffic mirroring copies the actual traffic content, including payload, for packet-level analysis.
  scope: flow logs versus traffic mirroring.
  link: [allowed and denied traffic, source and destination IP addresses, ports, protocol number, packet and byte counts, and an action (accept or reject)](../facts/vpc.md#vpc-faq-flow-logs-vs-traffic-mirroring)
  link: [analyze actual traffic content, including payload](../facts/vpc.md#vpc-faq-flow-logs-vs-traffic-mirroring)
  say: flow logs give metadata: addresses, ports, counts, accept or reject | traffic mirroring gives the packets themselves
vpc-faq-igw-and-egress-only
  claim: You connect a VPC to the internet with an internet gateway, which lets EC2 instances in the VPC access the internet directly; an egress-only internet gateway is the stateful, outbound-only option for IPv6 traffic.
  scope: per VPC.
  link: [This gateway enables Amazon EC2 instances in the VPC to directly access the Internet](../facts/vpc.md#vpc-faq-igw-and-egress-only)
  link: [a stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet](../facts/vpc.md#vpc-faq-igw-and-egress-only)
  say: an egress-only internet gateway for IPv6
vpc-faq-instance-az-from-subnet
  claim: When you launch an EC2 instance you specify its subnet, and the instance is launched in the Availability Zone of that subnet.
  scope: per instance.
  link: [The instance will be launched in the Availability Zone associated with the specified subnet](../facts/vpc.md#vpc-faq-instance-az-from-subnet)
  say: the subnet decides the Availability Zone
vpc-faq-instances-per-vpc-unbounded
  claim: For instances that require IPv4 addressing, you can run any number of EC2 instances in a VPC as long as the VPC is sized to give each instance an IPv4 address; for IPv6-only instances, a /56 VPC lets you launch a virtually unlimited number of instances.
  scope: per VPC; IPv4: the VPC must be sized to give each instance an IPv4 address; the /56 statement is for IPv6-only instances.
  link: [any number of Amazon EC2 instances within a VPC, so long as your VPC is appropriately sized to have an IPv4 address assigned to each instance](../facts/vpc.md#vpc-faq-instances-per-vpc-unbounded)
  link: [virtually unlimited number of Amazon EC2 instances](../facts/vpc.md#vpc-faq-instances-per-vpc-unbounded)
  say: as many as the address space allows
vpc-faq-inter-region-peering-ipv6
  claim: Inter-Region VPC peering supports IPv6.
  scope: per inter-Region peering connection.
  link: [Inter-Region VPC Peering supports IPv6](../facts/vpc.md#vpc-faq-inter-region-peering-ipv6)
  say: yes
vpc-faq-interface-endpoints-privatelink
  claim: Interface endpoints give private connectivity to services powered by PrivateLink, whether AWS services, your own services or SaaS solutions, and support connectivity over Direct Connect.
  scope: per interface endpoint.
  link: [services powered by PrivateLink, being AWS services, your own services or SaaS solutions](../facts/vpc.md#vpc-faq-interface-endpoints-privatelink)
  link: [supports connectivity over Direct Connect](../facts/vpc.md#vpc-faq-interface-endpoints-privatelink)
  say: AWS services, your own services or SaaS over PrivateLink
vpc-faq-ipam-contiguous-ipv6-only-in-ipam
  claim: Amazon-provided contiguous IPv6 CIDR blocks are supported only in IPAM.
  scope: per IPv6 CIDR block.
  link: [Amazon Provided Contiguous IPv6 CIDR blocks are currently only supported in IPAM](../facts/vpc.md#vpc-faq-ipam-contiguous-ipv6-only-in-ipam)
  say: no, only through IPAM
vpc-faq-ipam-share-with-ram
  claim: IPAM pools can be shared with other accounts in your AWS Organization through AWS Resource Access Manager (RAM), and also with accounts outside your primary Organization.
  scope: per IPAM pool.
  link: [share IPAM pools with other accounts in your AWS Organization using AWS Resource Access Manager (RAM)](../facts/vpc.md#vpc-faq-ipam-share-with-ram)
  say: with RAM across the Organization
vpc-faq-ipam-what
  claim: Amazon VPC IP Address Manager (IPAM) is a managed service for planning, tracking and monitoring IP addresses for AWS workloads, and it can automate IP address assignment to VPCs.
  scope: per IPAM.
  link: [a managed service that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads](../facts/vpc.md#vpc-faq-ipam-what)
  link: [automate IP address assignment to VPCs](../facts/vpc.md#vpc-faq-ipam-what)
  say: a managed service to plan, track and monitor IP addresses
vpc-faq-monitor-traffic-two-features
  claim: You can monitor the network traffic in a VPC with VPC traffic mirroring and VPC flow logs.
  scope: per VPC.
  link: [Amazon VPC traffic mirroring and Amazon VPC flow logs](../facts/vpc.md#vpc-faq-monitor-traffic-two-features)
  say: traffic mirroring and flow logs
vpc-faq-multiple-private-ips
  claim: You can assign one or more secondary private IP addresses to a network interface or an EC2 instance; how many depends on the instance type.
  scope: per network interface or instance.
  link: [one or more secondary private IP addresses](../facts/vpc.md#vpc-faq-multiple-private-ips)
  link: [depends on the instance type](../facts/vpc.md#vpc-faq-multiple-private-ips)
  say: yes, secondary private addresses | the instance type sets the limit
vpc-faq-network-acl-same-subnet
  claim: Network ACLs do not filter traffic between instances in the same subnet.
  scope: per network ACL; instances in the same subnet.
  link: [do not filter traffic between instances in the same subnet](../facts/vpc.md#vpc-faq-network-acl-same-subnet)
  say: not between instances in the same subnet
vpc-faq-no-charge-for-vpc-itself
  claim: There are no additional charges for creating and using a VPC itself; usage charges for other services such as EC2, including data transfer charges, still apply at published rates.
  scope: per VPC.
  link: [no additional charges for creating and using the VPC itself](../facts/vpc.md#vpc-faq-no-charge-for-vpc-itself)
  link: [still apply at published rates for those resources, including data transfer charges](../facts/vpc.md#vpc-faq-no-charge-for-vpc-itself)
  say: the VPC itself is free | you pay for what runs inside it and for data transfer
vpc-faq-nondefault-vpc-needs-subnet-id
  claim: To launch an instance into a nondefault VPC, you must specify a subnet ID during launch.
  scope: per instance launch; nondefault VPC.
  link: [you must specify a subnet-ID during instance launch](../facts/vpc.md#vpc-faq-nondefault-vpc-needs-subnet-id)
  say: you must name the subnet
vpc-faq-overlapping-vpc-cidrs
  claim: You can create multiple VPCs with overlapping IP address ranges, but doing so prohibits you from connecting these VPCs to a common home network via the hardware VPN connection.
  scope: multiple VPCs with overlapping IP address ranges; connection to a common home network via the hardware VPN connection.
  link: [prohibit you from connecting these VPCs to a common home network via the hardware VPN connection](../facts/vpc.md#vpc-faq-overlapping-vpc-cidrs)
  say: they cannot both connect to the same home network
vpc-faq-primary-cidr-any-ipv4-range
  claim: The primary CIDR block can be any IPv4 range, RFC 1918 or publicly routable, but publicly routable blocks are reachable only through the virtual private gateway and cannot be reached over the internet through the internet gateway.
  scope: per VPC, primary IPv4 CIDR; secondary CIDR blocks have extra restrictions.
  link: [any IPv4 address range, including RFC 1918 or publicly routable IP ranges, for the primary CIDR block](../facts/vpc.md#vpc-faq-primary-cidr-any-ipv4-range)
  link: [only reachable via the Virtual Private Gateway and cannot be accessed over the Internet through the Internet gateway](../facts/vpc.md#vpc-faq-primary-cidr-any-ipv4-range)
  say: any IPv4 range, private or public | public blocks are reachable only over the virtual private gateway
vpc-faq-primary-private-ip-retained
  claim: In an IPv4 or dual-stack subnet, the primary private IPv4 address stays with the instance or interface for its lifetime; secondary private IPv4 addresses can be assigned, unassigned or moved between interfaces or instances at any time.
  scope: per instance or network interface; IPv4 or dual-stack subnet.
  link: [the primary private IPv4 address is retained for the instance's or interface's lifetime](../facts/vpc.md#vpc-faq-primary-private-ip-retained)
  link: [Secondary private IPv4 addresses can be assigned, unassigned, or moved between interfaces or instances at any time](../facts/vpc.md#vpc-faq-primary-private-ip-retained)
  say: the primary private address never changes | secondary addresses can move
vpc-faq-private-instances-nat
  claim: Instances without public IP addresses reach the internet through a NAT gateway or a NAT instance, using the NAT device's public IP address; the NAT device allows outbound communication but does not let machines on the internet initiate a connection to the private instances.
  scope: instances in a private subnet; no public IP address.
  link: [route their traffic through a NAT gateway or a NAT instance to access the Internet](../facts/vpc.md#vpc-faq-private-instances-nat)
  link: [allows outbound communication but doesn’t allow machines on the Internet to initiate a connection to the privately addressed instances](../facts/vpc.md#vpc-faq-private-instances-nat)
  say: through a NAT gateway or a NAT instance | outbound only; nothing from the internet can start a connection
vpc-faq-private-instances-via-vgw
  claim: With a Site-to-Site VPN or Direct Connect connection, private instances can instead send their internet traffic down the virtual private gateway to the on-premises data center and use its existing egress points.
  scope: instances in a private subnet; VPC has a hardware VPN or Direct Connect connection.
  link: [route their Internet traffic down the virtual private gateway to your existing datacenter](../facts/vpc.md#vpc-faq-private-instances-via-vgw)
  say: out through the on-premises data center over the virtual private gateway
vpc-faq-public-ip-definition
  claim: An IP address on an instance or service in a VPC that can be accessed over the internet is a public IP address; only public IPv4 addresses, including Elastic IPs, and IPv6 GUA can be routable on the internet.
  scope: per IP address.
  link: [that can be accessed over the internet is considered a public IP address](../facts/vpc.md#vpc-faq-public-ip-definition)
  link: [Only public IPv4 addresses, including Elastic IP addresses (EIPs) and IPv6 GUA can be routable on the internet](../facts/vpc.md#vpc-faq-public-ip-definition)
  say: public IPv4, Elastic IPs and IPv6 global addresses
vpc-faq-public-ip-inbound-and-outbound
  claim: Public IP addresses, including Elastic IPs and IPv6 GUA, let instances in a VPC both send traffic directly out to the internet and receive unsolicited inbound traffic from the internet, as web servers need.
  scope: per instance.
  link: [both directly communicate outbound to the internet and to receive unsolicited inbound traffic from the internet](../facts/vpc.md#vpc-faq-public-ip-inbound-and-outbound)
  say: outbound and unsolicited inbound
vpc-faq-public-ip-needs-igw-and-route
  claim: For a public IP address to be reachable to and from the internet, you first connect the VPC to the internet and then update the route table.
  scope: per VPC.
  link: [first connect the VPC to the internet and then update the route table](../facts/vpc.md#vpc-faq-public-ip-needs-igw-and-route)
  say: attach to the internet, then add the route
vpc-faq-s3-access-options
  claim: Instances in a VPC can reach Amazon S3 through a VPC endpoint for S3, which keeps all traffic inside Amazon's network and lets you apply extra access policies, or through an internet gateway, or over Direct Connect or VPN via the data center.
  scope: per VPC.
  link: [VPC Endpoint for S3, which makes sure all traffic remains within Amazon's network](../facts/vpc.md#vpc-faq-s3-access-options)
  link: [use an Internet gateway to enable Internet access from your VPC and instances in the VPC can communicate with Amazon S3](../facts/vpc.md#vpc-faq-s3-access-options)
  say: a VPC endpoint for S3 keeps the traffic on the AWS network
vpc-faq-s3-via-igw-no-data-transfer-charge
  claim: Data transfer charges are not incurred when instances reach AWS services such as Amazon S3 through the VPC's internet gateway, but AWS resources reached over the VPN connection incur internet data transfer charges.
  scope: per VPC; access through the VPC's internet gateway.
  link: [Data transfer charges are not incurred when accessing Amazon Web Services, such as Amazon S3, via your VPC's Internet gateway](../facts/vpc.md#vpc-faq-s3-via-igw-no-data-transfer-charge)
  link: [you will incur Internet data transfer charges](../facts/vpc.md#vpc-faq-s3-via-igw-no-data-transfer-charge)
  say: through the internet gateway, no data transfer charge | over the VPN, you pay internet data transfer
vpc-faq-security-group-allow-only
  claim: A security group specifies the inbound and outbound traffic that is allowed to or from each EC2 instance; traffic that is not explicitly allowed is automatically denied.
  scope: per security group.
  link: [specify both inbound and outbound network traffic that is allowed to or from each Amazon EC2 instance](../facts/vpc.md#vpc-faq-security-group-allow-only)
  link: [Traffic which is not explicitly allowed to or from an instance is automatically denied](../facts/vpc.md#vpc-faq-security-group-allow-only)
  say: anything not explicitly allowed is denied
vpc-faq-site-to-site-vpn-ipsec
  claim: An AWS Site-to-Site VPN connection connects a VPC to your data center over an encrypted IPsec VPN connection, and no internet gateway is required to establish it.
  scope: per Site-to-Site VPN connection.
  link: [connects your VPC to your datacenter](../facts/vpc.md#vpc-faq-site-to-site-vpn-ipsec)
  link: [Internet Protocol Security (IPSec) VPN connections](../facts/vpc.md#vpc-faq-site-to-site-vpn-ipsec)
  link: [An internet gateway is not required to establish an AWS Site-to-Site VPN connection](../facts/vpc.md#vpc-faq-site-to-site-vpn-ipsec)
  say: it connects the VPC to your data center | IPsec | no internet gateway needed
vpc-faq-software-vpn-via-igw
  claim: You can connect to a VPC with a third-party software VPN, as a site-to-site or remote-access VPN, through the internet gateway.
  scope: per VPC; requires an internet gateway.
  link: [a third-party software VPN to create a site to site or remote access VPN connection with your VPC via the Internet gateway](../facts/vpc.md#vpc-faq-software-vpn-via-igw)
  say: yes, a software VPN through the internet gateway
vpc-faq-stateful-filtering-defined
  claim: Stateful filtering tracks the origin of a request and can automatically allow the reply to be returned to the originating computer; in the FAQ's web server example, only one rule is required on the filtering device: allow traffic inbound to the web server on TCP port 80.
  scope: a stateful filtering device (the FAQ's general definition).
  link: [tracks the origin of a request and can automatically allow the reply to the request to be returned to the originating computer](../facts/vpc.md#vpc-faq-stateful-filtering-defined)
  link: [Only one rule is required on the filtering device](../facts/vpc.md#vpc-faq-stateful-filtering-defined)
  say: it remembers the request and lets the reply back automatically | only one rule is needed
vpc-faq-stateful-vs-stateless
  claim: Network ACLs perform stateless filtering while security groups perform stateful filtering.
  scope: security groups and network ACLs.
  link: [network ACLs perform stateless filtering](../facts/vpc.md#vpc-faq-stateful-vs-stateless)
  link: [security groups perform stateful filtering](../facts/vpc.md#vpc-faq-stateful-vs-stateless)
  say: network ACLs are stateless | security groups are stateful
vpc-faq-stateless-filtering-defined
  claim: Stateless filtering examines only the source or destination IP address and the destination port and ignores whether traffic is a new request or a reply, so in the FAQ's web server example two rules are needed on the filtering device: one rule to allow traffic inbound to the web server on TCP port 80, and another rule to allow the outbound traffic from the web server.
  scope: a stateless filtering device (the FAQ's general definition).
  link: [ignoring whether the traffic is a new request or a reply to a request](../facts/vpc.md#vpc-faq-stateless-filtering-defined)
  link: [two rules would need to be implemented on the filtering device](../facts/vpc.md#vpc-faq-stateless-filtering-defined)
  say: it does not know a reply from a new request | two rules, inbound and outbound
vpc-faq-stopped-instance-ip-not-reusable
  claim: An IPv4 address assigned to a running instance can be used again by another instance only after the original instance is in the terminated state; a stopped instance keeps its address.
  scope: per IPv4 address; the original instance is stopped, not terminated.
  link: [can only be used again by another instance once that original running instance is in a “terminated” state](../facts/vpc.md#vpc-faq-stopped-instance-ip-not-reusable)
  say: only after the first instance is terminated
vpc-faq-subnet-az-no-preference
  claim: You choose a subnet's Availability Zone when you create it; if you do not specify one, the default "No Preference" option places the subnet in an available Availability Zone in the Region.
  scope: per subnet; default; adjustable; no Availability Zone specified at creation.
  link: [the default "No Preference" option will be selected and the subnet will be created in an available Availability Zone in the region](../facts/vpc.md#vpc-faq-subnet-az-no-preference)
  say: AWS picks an available Availability Zone for you
vpc-faq-subnet-reserved-addresses
  claim: You cannot use every address in a subnet: Amazon reserves the first four (4) IP addresses and the last one (1) IP address of every subnet for IP networking purposes.
  scope: per subnet; fixed.
  link: [the first four (4) IP addresses](../facts/vpc.md#vpc-faq-subnet-reserved-addresses)
  link: [the last one (1) IP address](../facts/vpc.md#vpc-faq-subnet-reserved-addresses)
  say: the first four addresses | and the last one
vpc-faq-traffic-mirroring-eni-level
  claim: Traffic mirroring captures packets at the elastic network interface level for EC2 instances, and only supported instance types can be mirrored.
  scope: per network interface; supported EC2 instances only.
  link: [network packet captures at the Elastic Network Interface (ENI) level for EC2 instances](../facts/vpc.md#vpc-faq-traffic-mirroring-eni-level)
  say: at the network interface
vpc-faq-traffic-mirroring-what
  claim: VPC traffic mirroring replicates network traffic to and from an EC2 instance and forwards it to out-of-band security and monitoring appliances for content inspection, threat monitoring and troubleshooting; the appliances can be a single EC2 instance or a fleet behind a Network Load Balancer with a UDP listener.
  scope: per mirrored network interface.
  link: [replicate network traffic to and from an Amazon EC2 instance and forward it to out-of-band security and monitoring appliances](../facts/vpc.md#vpc-faq-traffic-mirroring-what)
  link: [a fleet of instances behind a Network Load Balancer (NLB) with User Datagram Protocol (UDP) listener](../facts/vpc.md#vpc-faq-traffic-mirroring-what)
  say: copies the packets to monitoring appliances | one instance or an NLB with a UDP listener
vpc-faq-vpn-connection-hour-billing
  claim: A hardware VPN connection to a VPC is priced per VPN connection-hour while the connection is in the available state, partial hours are billed as full hours, and data over the VPN is charged at standard data transfer rates.
  scope: per VPN connection; connection in the available state.
  link: [pricing is per VPN connection-hour](../facts/vpc.md#vpc-faq-vpn-connection-hour-billing)
  link: [Partial hours are billed as full hours](../facts/vpc.md#vpc-faq-vpn-connection-hour-billing)
  link: [charged at standard AWS Data Transfer rates](../facts/vpc.md#vpc-faq-vpn-connection-hour-billing)
  say: per VPN connection-hour
vpc-flow-logs-250-subscriptions-per-resource
  claim: VPC Flow Logs supports at most 250 subscriptions per resource per account; to add more you must first delete existing subscriptions.
  scope: per resource, per account; maximum; not adjustable.
  link: [a maximum of 250 subscriptions per resource per account](../facts/vpc.md#vpc-flow-logs-250-subscriptions-per-resource)
  say: two hundred fifty flow log subscriptions per resource
vpc-flow-logs-aggregation-interval
  claim: By default the maximum aggregation interval of a flow log is 10 minutes; when you create the flow log you can choose a maximum aggregation interval of 1 minute instead, which produces a higher volume of flow log records.
  scope: per flow log; default; adjustable; set when the flow log is created.
  link: [the maximum aggregation interval is 10 minutes](../facts/vpc.md#vpc-flow-logs-aggregation-interval)
  link: [maximum aggregation interval of 1 minute](../facts/vpc.md#vpc-flow-logs-aggregation-interval)
  say: ten minutes by default | one minute as an option
vpc-flow-logs-athena-query
  claim: You can query flow logs stored in Amazon S3 with Amazon Athena, using standard SQL.
  link: [analyze data in Amazon S3, such as your flow logs, using standard SQL](../facts/vpc.md#vpc-flow-logs-athena-query)
  say: query them with Athena in standard SQL
vpc-flow-logs-config-immutable
  claim: After you create a flow log, you cannot change its configuration or its record format (for example the IAM role or the fields); instead you delete it and create a new one.
  link: [you can't change its configuration or the flow log record format](../facts/vpc.md#vpc-flow-logs-config-immutable)
  link: [you can delete the flow log and create a new one with the required configuration](../facts/vpc.md#vpc-flow-logs-config-immutable)
  say: you cannot change a flow log | delete it and create a new one
vpc-flow-logs-cwl-iam-role
  claim: A flow log that publishes to CloudWatch Logs needs an associated IAM role with permissions to publish to the log group, and the role must belong to your AWS account.
  link: [The IAM role must belong to your AWS account](../facts/vpc.md#vpc-flow-logs-cwl-iam-role)
  link: [must have sufficient permissions to publish flow logs to the specified log group in CloudWatch Logs](../facts/vpc.md#vpc-flow-logs-cwl-iam-role)
  say: the role must be in your own account
vpc-flow-logs-cwl-log-stream-per-eni
  claim: When publishing to CloudWatch Logs, flow log data goes to a log group, with a unique log stream for each network interface.
  link: [each network interface has a unique log stream in the log group](../facts/vpc.md#vpc-flow-logs-cwl-log-stream-per-eni)
  say: one log stream per network interface
vpc-flow-logs-default-format-fixed
  claim: You cannot customize or change the default flow log format; to capture additional or different fields you specify a custom format.
  link: [You cannot customize or change the default format](../facts/vpc.md#vpc-flow-logs-default-format-fixed)
  link: [specify a custom format instead](../facts/vpc.md#vpc-flow-logs-default-format-fixed)
  say: the default format is fixed
vpc-flow-logs-delete-keeps-data
  claim: Deleting a flow log stops new flow log records but does not delete existing flow log data, which you delete from the destination yourself.
  link: [Deleting a flow log does not delete any existing flow log data](../facts/vpc.md#vpc-flow-logs-delete-keeps-data)
  say: the data stays
vpc-flow-logs-delivery-best-effort
  claim: The flow log service typically delivers logs to CloudWatch Logs in about 5 minutes and to Amazon S3 in about 10 minutes, but delivery is best effort and can be delayed.
  link: [about 5 minutes](../facts/vpc.md#vpc-flow-logs-delivery-best-effort)
  link: [about 10 minutes](../facts/vpc.md#vpc-flow-logs-delivery-best-effort)
  link: [log delivery is on a best effort basis](../facts/vpc.md#vpc-flow-logs-delivery-best-effort)
  say: about five minutes to CloudWatch Logs | about ten minutes to S3
vpc-flow-logs-destinations
  claim: Flow log data can be published to Amazon CloudWatch Logs, Amazon S3 or Amazon Data Firehose; the Firehose destination was added September 8, 2022.
  scope: per flow log.
  link: [Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose](../facts/vpc.md#vpc-flow-logs-destinations)
  link: [September 8, 2022](../facts/vpc.md#vpc-flow-logs-destinations)
  say: CloudWatch Logs, S3 or Data Firehose | Firehose delivery since September twenty twenty-two
vpc-flow-logs-diagnose-stateless-nacl
  claim: When a security group allows a ping in and the network ACL allows inbound but not outbound ICMP, the flow log shows an ACCEPT record for the incoming ping and a REJECT record for the response that the network ACL denied, because network ACLs are stateless.
  link: [An ACCEPT record for the originating ping](../facts/vpc.md#vpc-flow-logs-diagnose-stateless-nacl)
  link: [A REJECT record for the response ping that the network ACL denied](../facts/vpc.md#vpc-flow-logs-diagnose-stateless-nacl)
  link: [Because network ACLs are stateless, the response ping is dropped](../facts/vpc.md#vpc-flow-logs-diagnose-stateless-nacl)
  say: a reject record for the response
vpc-flow-logs-firehose-cross-account
  claim: Flow logs can publish to an Amazon Data Firehose delivery stream in the same account or in a different account; cross-account delivery needs an IAM role in the source account and one in the destination account.
  link: [or in a different account (the destination account)](../facts/vpc.md#vpc-flow-logs-firehose-cross-account)
  link: [you must create an IAM role in the source account and an IAM role in the destination account](../facts/vpc.md#vpc-flow-logs-firehose-cross-account)
  say: a stream in another account
vpc-flow-logs-metadata-fields-2026
  claim: VPC Flow Logs now support EC2 resource tag fields and next-hop interface metadata fields (version 11 fields such as next-hop-interface-id), so records no longer have to be joined with separate tag or topology data.
  scope: per flow log, custom format.
  link: [EC2 resource tags and next-hop interface metadata](../facts/vpc.md#vpc-flow-logs-metadata-fields-2026)
  link: [next-hop-interface-id](../facts/vpc.md#vpc-flow-logs-metadata-fields-2026)
  say: resource tags and next-hop interface fields | the next-hop interface id field
vpc-flow-logs-nitro-one-minute
  claim: For a network interface attached to a Nitro-based instance, the flow log aggregation interval is always 1 minute or less, whatever maximum aggregation interval you set.
  scope: per network interface attached to a Nitro-based instance; maximum; Nitro-based instances only.
  link: [always 1 minute or less](../facts/vpc.md#vpc-flow-logs-nitro-one-minute)
  say: one minute or less
vpc-flow-logs-no-performance-impact
  claim: Flow log data is collected outside the path of network traffic, so flow logs do not affect network throughput or latency.
  link: [collected outside of the path of your network traffic](../facts/vpc.md#vpc-flow-logs-no-performance-impact)
  link: [does not affect network throughput or latency](../facts/vpc.md#vpc-flow-logs-no-performance-impact)
  say: it is collected outside the traffic path
vpc-flow-logs-nodata-skipdata
  claim: A flow log record with log status NODATA means no data was recorded during the aggregation interval; SKIPDATA means VPC Flow Logs skipped records because it could not capture data within internal capacity.
  link: [no data was recorded during the aggregation interval](../facts/vpc.md#vpc-flow-logs-nodata-skipdata)
  link: [VPC Flow Logs skips records when it can't capture flow log data during an aggregation interval because it exceeds internal capacity](../facts/vpc.md#vpc-flow-logs-nodata-skipdata)
  say: no traffic in the interval
vpc-flow-logs-not-captured-amazon-dns
  claim: Flow logs do not capture all IP traffic: traffic that instances generate when they contact the Amazon DNS server is not logged, but if you use your own DNS server, all traffic to that DNS server is logged.
  link: [Flow logs do not capture all IP traffic](../facts/vpc.md#vpc-flow-logs-not-captured-amazon-dns)
  link: [If you use your own DNS server, then all traffic to that DNS server is logged](../facts/vpc.md#vpc-flow-logs-not-captured-amazon-dns)
  say: flow logs miss some traffic
vpc-flow-logs-not-captured-metadata-timesync-router
  claim: Flow logs do not log traffic to and from 169.254.169.254 for instance metadata, traffic to and from 169.254.169.123 for the Amazon Time Sync Service, traffic to the reserved IP address of the default VPC router, or Windows license activation traffic.
  link: [169.254.169.254](../facts/vpc.md#vpc-flow-logs-not-captured-metadata-timesync-router)
  link: [169.254.169.123](../facts/vpc.md#vpc-flow-logs-not-captured-metadata-timesync-router)
  link: [Traffic to the reserved IP address for the default VPC router](../facts/vpc.md#vpc-flow-logs-not-captured-metadata-timesync-router)
  say: the instance metadata address
vpc-flow-logs-not-real-time
  claim: After you create a flow log, it can take several minutes to begin collecting and publishing data, and flow logs do not capture real-time log streams for network interfaces.
  link: [it can take several minutes to begin collecting and publishing data](../facts/vpc.md#vpc-flow-logs-not-real-time)
  link: [Flow logs do not capture real-time log streams for your network interfaces](../facts/vpc.md#vpc-flow-logs-not-real-time)
  say: it takes several minutes to start | not real time
vpc-flow-logs-other-service-enis
  claim: You can create flow logs for network interfaces created by other AWS services, such as Elastic Load Balancing, Amazon RDS, NAT gateways and transit gateways.
  link: [You can create flow logs for network interfaces that are created by other AWS services](../facts/vpc.md#vpc-flow-logs-other-service-enis)
  say: also for service-created network interfaces
vpc-flow-logs-peered-vpc-same-account-only
  claim: You cannot enable flow logs for VPCs that are peered with your VPC unless the peer VPC is in your account.
  link: [You can't enable flow logs for VPCs that are peered with your VPC unless the peer VPC is in your account](../facts/vpc.md#vpc-flow-logs-peered-vpc-same-account-only)
  say: only for peer VPCs in your own account
vpc-flow-logs-s3-existing-bucket
  claim: When publishing to Amazon S3, flow log data goes to an existing S3 bucket that you specify, as a series of log file objects.
  link: [published to an existing Amazon S3 bucket that you specify](../facts/vpc.md#vpc-flow-logs-s3-existing-bucket)
  say: an existing bucket you choose
vpc-flow-logs-three-levels
  claim: You can create a flow log for a VPC, a subnet or a network interface; a flow log for a subnet or VPC monitors each network interface in it.
  link: [a VPC, a subnet, or a network interface](../facts/vpc.md#vpc-flow-logs-three-levels)
  link: [each network interface in that subnet or VPC is monitored](../facts/vpc.md#vpc-flow-logs-three-levels)
  say: VPC, subnet or network interface
vpc-flow-logs-traffic-type-choice
  claim: When you create a flow log, you choose the type of traffic to capture: accepted traffic, rejected traffic, or all traffic.
  link: [accepted traffic, rejected traffic, or all traffic](../facts/vpc.md#vpc-flow-logs-traffic-type-choice)
  say: accepted, rejected or all traffic
vpc-flow-logs-vended-log-charges
  claim: Publishing flow logs incurs the data ingestion and archival charges for vended logs.
  link: [Data ingestion and archival charges for vended logs apply when you publish flow logs](../facts/vpc.md#vpc-flow-logs-vended-log-charges)
  say: vended log ingestion and archival charges
vpc-gateway-endpoint-applies-per-route-table
  claim: All instances in subnets whose route table is associated with a gateway endpoint use the endpoint to reach the service; instances in other subnets use the public service endpoint.
  link: [automatically use the gateway endpoint to access the service](../facts/vpc.md#vpc-gateway-endpoint-applies-per-route-table)
  link: [use the public service endpoint, not the gateway endpoint](../facts/vpc.md#vpc-gateway-endpoint-applies-per-route-table)
  say: subnets with the route use it
vpc-gateway-endpoint-beats-igw-default-route
  claim: Because routing uses the longest prefix match, a gateway endpoint route takes precedence over a 0.0.0.0/0 route to an internet gateway for traffic to the service in the same Region, while traffic to the service in a different Region still goes to the internet gateway because prefix lists are Regional.
  link: [the endpoint route takes precedence for traffic destined for the service (Amazon S3 or DynamoDB) in the current Region](../facts/vpc.md#vpc-gateway-endpoint-beats-igw-default-route)
  link: [prefix lists are specific to a Region](../facts/vpc.md#vpc-gateway-endpoint-beats-igw-default-route)
  say: the endpoint route wins in the same Region
vpc-gateway-endpoint-no-hourly-or-processing-charge
  claim: Gateway VPC endpoints have no data processing or hourly charges, so routing S3 traffic through a gateway endpoint instead of the NAT gateway avoids the NAT gateway data processing charge.
  scope: per gateway endpoint.
  link: [There are no data processing or hourly charges for using Gateway Type VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
  link: [avoid the NAT Gateway Data Processing charge](../facts/vpc.md#vpc-gateway-endpoint-no-hourly-or-processing-charge)
vpc-gateway-endpoint-no-onprem-cross-region-tgw
  claim: An S3 gateway endpoint does not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway; for those cases you use an interface endpoint, at additional cost.
  link: [gateway endpoints do not allow access from on-premises networks, from peered VPCs in other AWS Regions, or through a transit gateway](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  link: [you must use an interface endpoint, which is available for an additional cost](../facts/vpc.md#vpc-gateway-endpoint-no-onprem-cross-region-tgw)
  say: not from on premises, other Regions or a transit gateway | use an interface endpoint instead
vpc-gateway-endpoint-one-route-per-service-per-table
  claim: A route table can have endpoint routes to both Amazon S3 and DynamoDB, but not multiple endpoint routes to the same service.
  link: [You can't have multiple endpoint routes to the same service (Amazon S3 or DynamoDB) in a single route table](../facts/vpc.md#vpc-gateway-endpoint-one-route-per-service-per-table)
  say: one endpoint route per service per table
vpc-gateway-endpoint-route-auto-added
  claim: When you create a gateway endpoint you choose the subnet route tables it uses, and a route with the service's prefix list ID as destination and the endpoint ID as target is added to each of them automatically; you cannot delete or modify that route yourself.
  scope: per gateway endpoint.
  link: [a destination that specifies the prefix list ID of the service (`pl-{{xxxxxxxx}}`), and a target with the endpoint ID (`vpce-{{xxxxxxxxxxxxxxxxx}}`)](../facts/vpc.md#vpc-gateway-endpoint-route-auto-added)
  link: [cannot explicitly delete or modify the endpoint route](../facts/vpc.md#vpc-gateway-endpoint-route-auto-added)
  say: destination is the service prefix list, target is the endpoint | the endpoint route cannot be edited by hand
vpc-gateway-endpoint-s3-dynamodb-no-privatelink
  claim: Gateway VPC endpoints give connectivity to Amazon S3 and DynamoDB without an internet gateway or NAT device, and, unlike other VPC endpoint types, they do not use AWS PrivateLink.
  link: [Gateway VPC endpoints provide reliable connectivity to Amazon S3 and DynamoDB without requiring an internet gateway or a NAT device for your VPC](../facts/vpc.md#vpc-gateway-endpoint-s3-dynamodb-no-privatelink)
  link: [Gateway endpoints do not use AWS PrivateLink, unlike other types of VPC endpoints](../facts/vpc.md#vpc-gateway-endpoint-s3-dynamodb-no-privatelink)
  say: gateway endpoints reach S3 and DynamoDB without an internet gateway or NAT
vpc-gateway-route-table-ingress-routing
  claim: A gateway route table is a route table associated with an internet gateway or a virtual private gateway; it lets you intercept traffic entering the VPC and redirect it to a middlebox appliance such as a security appliance, and it cannot be the main route table.
  scope: per internet gateway or virtual private gateway.
  link: [You can associate a route table with an internet gateway or a virtual private gateway](../facts/vpc.md#vpc-gateway-route-table-ingress-routing)
  link: [intercept the traffic that enters your VPC through an internet gateway by redirecting that traffic to a middlebox appliance (such as a security appliance) in your VPC](../facts/vpc.md#vpc-gateway-route-table-ingress-routing)
  link: [can't set a gateway route table as the main route table](../facts/vpc.md#vpc-gateway-route-table-ingress-routing)
  say: a route table attached to the internet gateway or virtual private gateway | it sends incoming traffic through a security appliance first
vpc-igw-attach-not-enough
  claim: Attaching an internet gateway does not by itself make instances reachable: the subnet route table needs a route to the internet gateway, the instances need public IP addresses, and a security group must allow the traffic.
  link: [Attaching an internet gateway to a VPC does not automatically make your instances accessible from the internet](../facts/vpc.md#vpc-igw-attach-not-enough)
  link: [you must update the subnet route table with a route to the internet gateway](../facts/vpc.md#vpc-igw-attach-not-enough)
  link: [You must also ensure that the instances have public IP addresses and an associated security group that allows traffic from the internet over specific ports and protocols required by your application](../facts/vpc.md#vpc-igw-attach-not-enough)
vpc-igw-definition-scaled-redundant
  claim: An internet gateway is a horizontally scaled, redundant and highly available VPC component that lets the VPC and the internet communicate over IPv4 and IPv6, and it does not add availability risk or bandwidth constraints.
  scope: per internet gateway.
  link: [a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet](../facts/vpc.md#vpc-igw-definition-scaled-redundant)
  link: [does not cause availability risks or bandwidth constraints on your network traffic](../facts/vpc.md#vpc-igw-definition-scaled-redundant)
  link: [supports IPv4 and IPv6 traffic](../facts/vpc.md#vpc-igw-definition-scaled-redundant)
  say: a horizontally scaled, redundant, highly available gateway to the internet | no bandwidth limit
vpc-igw-ingress-routing-ip-pools-change
  claim: Since August 13, 2025 an internet gateway can route inbound traffic for a large pool of public IP addresses (for example a BYOIP pool) to a single network interface; previously it only accepted traffic for public IP addresses directly associated with network interfaces in the VPC.
  scope: per internet gateway.
  link: [August 13, 2025](../facts/vpc.md#vpc-igw-ingress-routing-ip-pools-change)
  link: [route inbound internet traffic destined for large pools of public IP addresses to a single elastic network interface](../facts/vpc.md#vpc-igw-ingress-routing-ip-pools-change)
  say: August thirteenth, twenty twenty-five | a whole public IP pool to one network interface
  changed: 2025-08-13: was only accepted traffic destined for public IP addresses that were directly associated with network interfaces in the VPC
vpc-igw-ipv4-and-ipv6-nat-for-ipv4
  claim: An internet gateway supports IPv4 and IPv6 traffic, and for communication using IPv4 it also performs network address translation (NAT); IPv6 addresses are globally unique, and therefore public by default.
  link: [It supports IPv4 and IPv6 traffic](../facts/vpc.md#vpc-igw-ipv4-and-ipv6-nat-for-ipv4)
  link: [For communication using IPv4, the internet gateway also performs network address translation (NAT)](../facts/vpc.md#vpc-igw-ipv4-and-ipv6-nat-for-ipv4)
  say: it does NAT for IPv4
vpc-igw-ipv6-needs-cidr-and-address
  claim: To communicate over the internet with IPv6, the VPC and subnet must have an associated IPv6 CIDR block and the instance must have an IPv6 address from the subnet range.
  link: [your VPC and subnet must have an associated IPv6 CIDR block](../facts/vpc.md#vpc-igw-ipv6-needs-cidr-and-address)
  say: an IPv6 CIDR on the VPC and subnet
vpc-igw-no-charge
  claim: There is no charge for an internet gateway itself; EC2 instances that use it pay data transfer charges.
  scope: per internet gateway.
  link: [There is no charge for an internet gateway](../facts/vpc.md#vpc-igw-no-charge)
  link: [data transfer charges for EC2 instances that use internet gateways](../facts/vpc.md#vpc-igw-no-charge)
vpc-igw-one-to-one-nat
  claim: The instance only knows its private IP address; the internet gateway performs one-to-one NAT so outbound traffic carries the instance's public IPv4 or Elastic IP address and inbound traffic to that public address is translated to the private address.
  scope: per internet gateway; an instance with a public IPv4 address or Elastic IP address.
  link: [Your instance is only aware of the private (internal) IP address space defined within the VPC and subnet](../facts/vpc.md#vpc-igw-one-to-one-nat)
  link: [The internet gateway logically provides the one-to-one NAT on behalf of your instance](../facts/vpc.md#vpc-igw-one-to-one-nat)
  say: the instance sees only its private address | the internet gateway does one-to-one NAT
vpc-igw-requires-attach-and-route
  claim: To use an internet gateway you must attach it to the VPC and configure routing; for IPv4 the instance must also have a public IPv4 address or an Elastic IP address.
  scope: per VPC; IPv4.
  link: [you must attach it to a VPC and configure routing](../facts/vpc.md#vpc-igw-requires-attach-and-route)
  link: [your instance must have a public IPv4 address](../facts/vpc.md#vpc-igw-requires-attach-and-route)
  link: [automatically assign public IPv4 addresses to your instances, or you can assign Elastic IP addresses to your instances](../facts/vpc.md#vpc-igw-requires-attach-and-route)
  say: attach it to the VPC and add a route | the instance needs a public or Elastic IP
vpc-igw-route-destination
  claim: You make a subnet public by attaching an internet gateway to the VPC and adding a route with destination 0.0.0.0/0 for IPv4 or ::/0 for IPv6 and the internet gateway as target.
  scope: per subnet route table.
  link: [a route with a destination of `0.0.0.0/0` for IPv4 traffic or `::/0` for IPv6 traffic, and a target of the internet gateway ID](../facts/vpc.md#vpc-igw-route-destination)
  link: [0.0.0.0/0](../facts/vpc.md#vpc-igw-route-destination)
  link: [::/0](../facts/vpc.md#vpc-igw-route-destination)
  say: zero dot zero dot zero dot zero slash zero to the internet gateway
vpc-interface-endpoint-billed-hour-per-az-and-gb
  claim: An interface VPC endpoint is billed for each hour it is provisioned in each Availability Zone and per GB of data processed.
  link: [billed for each hour that your interface VPC endpoint is provisioned in each Availability Zone](../facts/vpc.md#vpc-interface-endpoint-billed-hour-per-az-and-gb)
  link: [You are also billed per GB of data processed](../facts/vpc.md#vpc-interface-endpoint-billed-hour-per-az-and-gb)
  say: per hour per Availability Zone | and per GB processed
vpc-interface-endpoint-eni-per-subnet
  claim: For each subnet you choose (one subnet per Availability Zone), an interface endpoint gets an endpoint network interface, a requester-managed network interface with a private IP address from the subnet range.
  link: [You can choose one subnet per Availability Zone for your interface endpoint](../facts/vpc.md#vpc-interface-endpoint-eni-per-subnet)
  link: [we create an endpoint network interface in the subnet and assign it a private IP address from the IP address range of the subnet](../facts/vpc.md#vpc-interface-endpoint-eni-per-subnet)
  say: one subnet per AZ | a network interface with a private IP
vpc-interface-endpoint-security-groups
  claim: Security groups associated with the network interfaces of an interface endpoint control the traffic allowed to the endpoint network interface from resources in the VPC.
  link: [The security group rules control the traffic that is allowed to the endpoint network interface from the resources in your VPC](../facts/vpc.md#vpc-interface-endpoint-security-groups)
  say: security groups on the endpoint
vpc-ipam-tiers-and-advanced-price
  claim: Amazon VPC IP Address Manager (IPAM) has a Free Tier for a single Region and account, with no charge for IPAM use, and an Advanced Tier for two or more Regions or accounts that adds private IPv4 management and IP history auditing and costs an hourly rate of $0.00027 for each active IP address managed.
  scope: per active IP address managed in IPAM, per hour (Advanced Tier).
  link: [an hourly rate of $0.00027 for each active IP address](../facts/vpc.md#vpc-ipam-tiers-and-advanced-price)
  link: [a single AWS Region and account](../facts/vpc.md#vpc-ipam-tiers-and-advanced-price)
  say: a small fraction of a cent per active IP address per hour | Free Tier: one Region and one account
vpc-ipv4-cannot-be-disabled
  claim: You cannot disable IPv4 support for a VPC and its subnets; a VPC can run in dual-stack mode, with IPv4 and IPv6 communication independent of each other.
  link: [You cannot disable IPv4 support for your VPC and subnets](../facts/vpc.md#vpc-ipv4-cannot-be-disabled)
  link: [Your VPC can operate in dual-stack mode](../facts/vpc.md#vpc-ipv4-cannot-be-disabled)
  say: IPv4 cannot be turned off | dual-stack
vpc-ipv4-cidr-required-ipv6-optional
  claim: A VPC must have an IPv4 CIDR block; additional IPv4 CIDR blocks and one or more IPv6 CIDR blocks are optional.
  scope: per VPC; minimum.
  link: [A VPC must have an associated IPv4 CIDR block](../facts/vpc.md#vpc-ipv4-cidr-required-ipv6-optional)
  link: [optionally associate additional IPv4 CIDR blocks and one or more IPv6 CIDR blocks](../facts/vpc.md#vpc-ipv4-cidr-required-ipv6-optional)
  say: every VPC needs an IPv4 CIDR | IPv6 is optional
vpc-ipv4-cidr-size-addresses
  claim: A VPC IPv4 CIDR block can be between a /16 netmask (65,536 IP addresses) and a /28 netmask (16 IP addresses).
  scope: per VPC IPv4 CIDR block; maximum; not adjustable; /16 is the largest block and /28 the smallest.
  link: [/16 netmask (65,536 IP addresses)](../facts/vpc.md#vpc-ipv4-cidr-size-addresses)
  link: [/28 netmask (16 IP addresses)](../facts/vpc.md#vpc-ipv4-cidr-size-addresses)
  say: slash sixteen, about sixty-five thousand addresses | slash twenty-eight, sixteen addresses
vpc-ipv6-add-step1-associate-cidr
  claim: The first step to add IPv6 to a VPC is to associate an Amazon-provided or BYOIP IPv6 CIDR block with the VPC and with its subnets.
  link: [Associate an Amazon-provided or BYOIP IPv6 CIDR block with your VPC and with your subnets](../facts/vpc.md#vpc-ipv6-add-step1-associate-cidr)
  say: associate an IPv6 CIDR block
vpc-ipv6-add-step2-routes
  claim: The second step to add IPv6 is to update the route tables: in a public subnet, route all IPv6 traffic to the internet gateway; in a private subnet, route all internet-bound IPv6 traffic to an egress-only internet gateway.
  link: [For a public subnet, create a route that routes all IPv6 traffic from the subnet to the internet gateway](../facts/vpc.md#vpc-ipv6-add-step2-routes)
  link: [create a route that routes all internet-bound IPv6 traffic from the subnet to an egress-only internet gateway](../facts/vpc.md#vpc-ipv6-add-step2-routes)
  say: public subnet: IPv6 to the internet gateway | private subnet: IPv6 to the egress-only internet gateway
vpc-ipv6-add-step3-sg-nacl-rules
  claim: The third step to add IPv6 is to update security group rules to include rules for IPv6 addresses, and to add IPv6 rules to any custom network ACL rules.
  link: [Update your security group rules to include rules for IPv6 addresses](../facts/vpc.md#vpc-ipv6-add-step3-sg-nacl-rules)
  link: [you must include rules for IPv6 traffic](../facts/vpc.md#vpc-ipv6-add-step3-sg-nacl-rules)
vpc-ipv6-add-step4-assign-addresses
  claim: The fourth step to add IPv6 is to assign IPv6 addresses to the instances from the IPv6 address range of their subnet.
  link: [Assign IPv6 addresses to your instances from the IPv6 address range of your subnet](../facts/vpc.md#vpc-ipv6-add-step4-assign-addresses)
vpc-ipv6-addresses-public-by-default
  claim: IPv6 addresses are globally unique and therefore public by default; to let an instance reach the internet over IPv6 without being reachable from it, you use an egress-only internet gateway.
  link: [IPv6 addresses are globally unique, and are therefore public by default](../facts/vpc.md#vpc-ipv6-addresses-public-by-default)
  link: [you can use an egress-only internet gateway](../facts/vpc.md#vpc-ipv6-addresses-public-by-default)
  say: IPv6 addresses are public
vpc-ipv6-amazon-provided-block-56
  claim: When you request an Amazon-provided IPv6 CIDR block for a VPC, Amazon provides a fixed block size of /56; for an IPv6 block from an IPAM pool, the possible netmask lengths are /44 to /60 in increments of /4.
  scope: per Amazon-provided IPv6 CIDR block of a VPC; fixed; not adjustable; Amazon-provided block; IPAM pool blocks can be /44 to /60 in increments of /4.
  link: [fixed block size of /56](../facts/vpc.md#vpc-ipv6-amazon-provided-block-56)
  say: a fixed slash fifty-six
vpc-ipv6-amazon-provided-public
  claim: Amazon-provided IPv6 addresses are always advertised on the internet and are globally unique, so they are reachable over the internet; you control reachability with subnet routing, security groups and network ACLs.
  scope: Amazon-provided public IPv6 addresses.
  link: [always advertised on the internet](../facts/vpc.md#vpc-ipv6-amazon-provided-public)
  say: public IPv6 is always advertised; routing and security groups decide reachability
vpc-ipv6-auto-sg-outbound-rule
  claim: When you associate an IPv6 CIDR block with a VPC, AWS automatically adds an outbound rule allowing all IPv6 traffic to the VPC security groups, unless you modified their original outbound rules; it also adds IPv6 allow rules to an unmodified default network ACL.
  scope: per VPC; default; not adjustable.
  link: [we automatically add an outbound rule to the security groups for the VPC that allows all IPv6 traffic](../facts/vpc.md#vpc-ipv6-auto-sg-outbound-rule)
  link: [we automatically add rules to the default network ACL to allow IPv6 traffic](../facts/vpc.md#vpc-ipv6-auto-sg-outbound-rule)
vpc-ipv6-cidr-amazon-assigned
  claim: You can request an IPv6 CIDR block from Amazon's pool of IPv6 addresses for your VPC, but you cannot choose the IPv6 range yourself.
  scope: per VPC; Amazon-provided IPv6 CIDR block.
  link: [request an IPv6 CIDR block from Amazon's pool of IPv6 addresses](../facts/vpc.md#vpc-ipv6-cidr-amazon-assigned)
  link: [cannot choose the range of IP addresses yourself](../facts/vpc.md#vpc-ipv6-cidr-amazon-assigned)
  say: Amazon assigns the IPv6 range
vpc-ipv6-cidr-sizes
  claim: A VPC's IPv6 CIDR blocks can be sized from /44 to /60 in increments of /4, and an IPv6 subnet can be sized from /44 to /64 in increments of /4; you can associate a single IPv6 CIDR block when you create a new VPC.
  scope: per VPC IPv6 CIDR block and per IPv6 subnet.
  link: [from /44 to /60 in increments of /4](../facts/vpc.md#vpc-ipv6-cidr-sizes)
  link: [between /44 and /64 in increments of /4](../facts/vpc.md#vpc-ipv6-cidr-sizes)
  say: VPC: slash forty-four to slash sixty | subnet: slash forty-four to slash sixty-four
vpc-ipv6-no-migration-ipv4-only-to-ipv6-only
  claim: There is no migration path from IPv4-only subnets to IPv6-only subnets.
  link: [There is no migration path from IPv4-only subnets to IPv6-only subnets](../facts/vpc.md#vpc-ipv6-no-migration-ipv4-only-to-ipv6-only)
  say: no migration path
vpc-ipv6-no-network-fragmentation
  claim: The IPv6 protocol does not support fragmentation in the network; a device that receives a packet larger than the path MTU drops it and returns ICMPv6 Packet Too Big (type 2).
  link: [The IPv6 protocol does not support fragmentation in the network](../facts/vpc.md#vpc-ipv6-no-network-fragmentation)
  link: [ICMPv6 Packet Too Big (PTB)](../facts/vpc.md#vpc-ipv6-no-network-fragmentation)
  say: IPv6 does not fragment in the network
vpc-ipv6-only-subnet-link-local-ipv4
  claim: Resources in an IPv6-only subnet are assigned IPv4 link-local addresses from 169.254.0.0/16; these addresses are used to communicate with services that are available only in the VPC.
  scope: per IPv6-only subnet.
  link: [IPv4 link-local addresses from CIDR block 169.254.0.0/16](../facts/vpc.md#vpc-ipv6-only-subnet-link-local-ipv4)
  link: [used to communicate with services that are available only in the VPC](../facts/vpc.md#vpc-ipv6-only-subnet-link-local-ipv4)
  say: link-local addresses from one sixty-nine dot two fifty-four
vpc-ipv6-only-subnets-nitro-ec2
  claim: Amazon VPC supports IPv6-only subnets, and Amazon EC2 supports launching instances based on the Nitro System into IPv6-only subnets.
  link: [Amazon VPC supports creating IPv6-only subnets](../facts/vpc.md#vpc-ipv6-only-subnets-nitro-ec2)
  link: [Amazon EC2 supports launching instances based on the Nitro System into IPv6-only subnets](../facts/vpc.md#vpc-ipv6-only-subnets-nitro-ec2)
  say: Nitro instances
vpc-ipv6-route-not-both-igw-and-eigw
  claim: A route table cannot have the same destination (::/0) pointing to both an internet gateway and an egress-only internet gateway at the same time.
  link: [cannot have the same destination (::/0) pointing to both an internet gateway and an egress-only internet gateway simultaneously](../facts/vpc.md#vpc-ipv6-route-not-both-igw-and-eigw)
  say: not both in one route table
vpc-ipv6-router-addresses-change
  claim: Since November 11, 2022, three IPv6 addresses are reserved for the default VPC router: the subnet's ::1 address plus two link-local addresses (one in the FE80::/10 range and FE80:ec2::1).
  scope: per IPv6 subnet.
  link: [November 11, 2022](../facts/vpc.md#vpc-ipv6-router-addresses-change)
  link: [Three IPv6 addresses are now reserved for use by the default VPC router](../facts/vpc.md#vpc-ipv6-router-addresses-change)
  say: November eleventh, twenty twenty-two | three router addresses
vpc-ipv6-routes-separate-from-ipv4
  claim: IPv4 and IPv6 CIDR blocks are treated separately in route tables: a 0.0.0.0/0 route does not cover IPv6, so you must add a separate ::/0 route for all IPv6 addresses.
  scope: per route table.
  link: [CIDR blocks for IPv4 and IPv6 are treated separately](../facts/vpc.md#vpc-ipv6-routes-separate-from-ipv4)
  link: [a route with a destination CIDR of `0.0.0.0/0` does not automatically include all IPv6 addresses](../facts/vpc.md#vpc-ipv6-routes-separate-from-ipv4)
  link: [must create a route with a destination CIDR of `::/0` for all IPv6 addresses](../facts/vpc.md#vpc-ipv6-routes-separate-from-ipv4)
  say: IPv4 and IPv6 routes are separate | the IPv4 default route does not include IPv6
vpc-ipv6-support-table-s3
  claim: Amazon S3 supports IPv6 for gateway and interface VPC endpoints (What's New, posted Nov 10, 2025): you configure the IP address type of a new or existing S3 gateway or interface endpoint to IPv6 or Dualstack.
  scope: Amazon S3 gateway and interface VPC endpoints.
  link: [supports IPv6 for gateway and interface VPC endpoints](../facts/vpc.md#vpc-ipv6-support-table-s3)
  link: [Nov 10, 2025](../facts/vpc.md#vpc-ipv6-support-table-s3)
  link: [IPv6 or Dualstack](../facts/vpc.md#vpc-ipv6-support-table-s3)
  say: S3 gateway and interface endpoints support IPv6 | November tenth, twenty twenty-five | set the endpoint IP address type to IPv6 or dual stack
vpc-isolated-subnet-definition
  claim: An isolated subnet has no routes to destinations outside its VPC, so its resources can only reach, or be reached by, other resources in the same VPC; the subnet type is decided by how its routing is configured.
  scope: per subnet.
  link: [The subnet has no routes to destinations outside its VPC](../facts/vpc.md#vpc-isolated-subnet-definition)
  link: [The subnet type is determined by how you configure routing for your subnets](../facts/vpc.md#vpc-isolated-subnet-definition)
  say: no routes outside the VPC | the route table decides the subnet type
vpc-lb-sg-from-anywhere-targets-from-lb
  claim: In the guide's example the load balancer's security group must allow inbound traffic from clients on the listener port, with 0.0.0.0/0 as the source to accept traffic from anywhere on the internet, and the web servers' security group rules allow HTTP and HTTPS traffic from the load balancer.
  scope: the VPC guide example for web and database servers.
  link: [To accept traffic from anywhere on the internet, specify 0.0.0.0/0 as the source](../facts/vpc.md#vpc-lb-sg-from-anywhere-targets-from-lb)
  link: [allow the web servers to receive HTTP and HTTPS traffic from the load balancer](../facts/vpc.md#vpc-lb-sg-from-anywhere-targets-from-lb)
vpc-local-route-in-every-route-table
  claim: Every route table contains a local route for communication within the VPC, added by default to all route tables; a VPC with more than one IPv4 CIDR block gets a local route for each IPv4 CIDR block, and associating an IPv6 CIDR block automatically adds a local route for IPv6.
  scope: per route table; default.
  link: [Every route table contains a local route for communication within the VPC](../facts/vpc.md#vpc-local-route-in-every-route-table)
  link: [This route is added by default to all route tables](../facts/vpc.md#vpc-local-route-in-every-route-table)
  link: [automatically add a local route to each route table for the VPC to allow IPv6 traffic within the VPC](../facts/vpc.md#vpc-local-route-in-every-route-table)
  say: every route table has a local route
vpc-local-zone-no-endpoints
  claim: You cannot create VPC endpoints in Local Zone subnets, and public IP addresses provisioned for a Local Zone network border group cannot move between the Local Zone and its parent Region.
  link: [You can't create VPC endpoints in Local Zone subnets](../facts/vpc.md#vpc-local-zone-no-endpoints)
  link: [you cannot move them between the Local Zone and the parent Region](../facts/vpc.md#vpc-local-zone-no-endpoints)
  say: no VPC endpoints in Local Zone subnets
vpc-local-zone-subnet-extends-vpc
  claim: When you create a subnet in a Local Zone you extend the VPC to that Local Zone; Local Zone subnets follow the same routing rules as Availability Zone subnets, and outbound internet traffic leaves from the Local Zone.
  link: [When you create a subnet in a Local Zone, you extend the VPC to that Local Zone](../facts/vpc.md#vpc-local-zone-subnet-extends-vpc)
  link: [Outbound internet traffic leaves a Local Zone from the Local Zone](../facts/vpc.md#vpc-local-zone-subnet-extends-vpc)
  say: a Local Zone subnet extends the VPC
vpc-main-route-table-rules
  claim: Every VPC automatically has a main route table; you can change its routes but you cannot delete it, and by default the main route table of a nondefault VPC contains only a local route.
  scope: per VPC; default.
  link: [When you create a VPC, it automatically has a main route table](../facts/vpc.md#vpc-main-route-table-rules)
  link: [can't delete the main route table](../facts/vpc.md#vpc-main-route-table-rules)
  link: [the main route table contains only a local route](../facts/vpc.md#vpc-main-route-table-rules)
  say: every VPC comes with a main route table | the main route table cannot be deleted | a new VPC's main route table has only the local route
vpc-more-specific-routes-avoid-natgw-charges
  claim: More specific routes than 0.0.0.0/0, for example a prefix list to a gateway endpoint or a peer CIDR to a peering connection, avoid unnecessary NAT gateway data processing charges and keep that traffic private.
  link: [create more specific routes to other targets to avoid unnecessary data processing charges for using a NAT gateway](../facts/vpc.md#vpc-more-specific-routes-avoid-natgw-charges)
vpc-mtu-1500-all-instance-types
  claim: All EC2 instance types support an MTU of 1500, the largest Ethernet packet size supported over most of the internet; the maximum MTU an instance supports depends on its instance type.
  scope: per EC2 instance; fixed; not adjustable; the maximum supported MTU depends on the instance type.
  link: [1500 MTU](../facts/vpc.md#vpc-mtu-1500-all-instance-types)
  say: fifteen hundred bytes
vpc-mtu-jumbo-frames-caution-outside-vpc
  claim: Packets over their MTU limit are fragmented, or dropped if the Don't Fragment flag is set, so jumbo frames should be used with caution for internet-bound traffic or any traffic that leaves a VPC.
  scope: per network path.
  link: [Jumbo frames should be used with caution for internet-bound traffic](../facts/vpc.md#vpc-mtu-jumbo-frames-caution-outside-vpc)
  say: be careful with jumbo frames outside the VPC
vpc-multi-vpc-reasons
  claim: The number of VPCs a customer creates usually follows its number of accounts, users and staged environments such as production, development and test.
  link: [usually related to their number of accounts, users, and staged environments (production, development, test, and so on)](../facts/vpc.md#vpc-multi-vpc-reasons)
vpc-nacl-asterisk-rule-denies-unmatched
  claim: Every network ACL, default or custom, includes an inbound and an outbound rule whose number is an asterisk (*), which denies any packet that matches no other rule; you cannot delete the asterisk rules.
  scope: per network ACL; fixed; not adjustable.
  link: [if a packet doesn't match any of the other rules, it's denied](../facts/vpc.md#vpc-nacl-asterisk-rule-denies-unmatched)
  link: [You can't delete a rule where the rule number is an asterisk](../facts/vpc.md#vpc-nacl-asterisk-rule-denies-unmatched)
  say: anything that matches no rule is denied
vpc-nacl-backup-layer-for-sg-mistake
  claim: A network ACL is a backup layer of defense: if a security group is accidentally updated to allow SSH from anywhere, the network ACL still restricts access to the remote computer's IP range and denies SSH from other addresses.
  link: [relying on the network ACL as a backup layer of defense](../facts/vpc.md#vpc-nacl-backup-layer-for-sg-mistake)
  link: [the network ACL still restricts access to only the IP address range of the remote computer](../facts/vpc.md#vpc-nacl-backup-layer-for-sg-mistake)
vpc-nacl-cannot-block-dns-or-imds
  claim: Network ACLs cannot block DNS requests to or from the Route 53 Resolver (AmazonProvidedDNS), and cannot block traffic to the Instance Metadata Service (IMDS).
  link: [Network ACLs can't block DNS requests to or from the Route 53 Resolver](../facts/vpc.md#vpc-nacl-cannot-block-dns-or-imds)
  link: [Network ACLs can't block traffic to the Instance Metadata Service (IMDS)](../facts/vpc.md#vpc-nacl-cannot-block-dns-or-imds)
  say: no blocking of Amazon DNS
vpc-nacl-changes-short-delay
  claim: Network ACL rule changes apply automatically to the associated subnets and take effect after a short period.
  link: [the changes are automatically applied to the subnets that it's associated with](../facts/vpc.md#vpc-nacl-changes-short-delay)
  link: [The changes take effect after a short period](../facts/vpc.md#vpc-nacl-changes-short-delay)
  say: after a short delay
vpc-nacl-custom-initial-rules-block-all
  claim: A new custom network ACL starts with initial rules that block all inbound and outbound traffic, and it is not associated with a subnet until you associate it explicitly.
  scope: per network ACL; default; not adjustable; custom network ACL, before you add rules.
  link: [block all inbound and outbound traffic](../facts/vpc.md#vpc-nacl-custom-initial-rules-block-all)
  say: blocks everything in and out
vpc-nacl-deny-rule-lower-number
  claim: To deny some ports inside a wide allowed port range, give the deny rule a lower number than the rule that allows the wider range.
  link: [give the deny rule a lower number than the rule that allows the wider range of port traffic](../facts/vpc.md#vpc-nacl-deny-rule-lower-number)
  say: the deny rule needs the lower number
vpc-nacl-elb-health-check-deny
  claim: If the subnet of the backend instances has a network ACL deny rule for all traffic from 0.0.0.0/0 or from the subnet CIDR, the load balancer cannot carry out health checks on the instances.
  link: [your load balancer can't carry out health checks on the instances](../facts/vpc.md#vpc-nacl-elb-health-check-deny)
  say: health checks fail
vpc-nacl-ephemeral-linux-32768-61000
  claim: The client that starts a connection chooses the ephemeral port range, which depends on its operating system: many Linux kernels, including the Amazon Linux kernel, use ports 32768-61000.
  scope: per client operating system; default; not adjustable; many Linux kernels, including Amazon Linux.
  link: [ports 32768-61000](../facts/vpc.md#vpc-nacl-ephemeral-linux-32768-61000)
  say: thirty-two thousand seven sixty-eight to sixty-one thousand
vpc-nacl-ephemeral-natgw-elb-lambda-1024-65535
  claim: A NAT gateway, requests from Elastic Load Balancing, and AWS Lambda functions use ephemeral ports 1024-65535, so network ACL rules for their return traffic must allow that range.
  scope: per NAT gateway, load balancer or Lambda function; fixed; not adjustable.
  link: [ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-natgw-elb-lambda-1024-65535)
  say: ten twenty-four to sixty-five five thirty-five
vpc-nacl-ephemeral-open-1024-65535
  claim: To cover all the client types that might reach public-facing instances, you can open ephemeral ports 1024-65535 in a network ACL and add deny rules for malicious ports in that range, placed earlier in the table than the allow rule.
  scope: per network ACL; public-facing instances with many client types.
  link: [open ephemeral ports 1024-65535](../facts/vpc.md#vpc-nacl-ephemeral-open-1024-65535)
  say: open ten twenty-four to sixty-five five thirty-five
vpc-nacl-ephemeral-windows-49152-65535
  claim: Windows Server 2008 and later use ephemeral ports 49152-65535, so for a request from a Windows 10 client to a web server in a VPC, the network ACL needs an outbound rule for ports 49152-65535.
  scope: per client operating system; default; not adjustable; Windows Server 2008 and later; Windows Server 2003 and earlier used 1025-5000.
  link: [ports 49152-65535](../facts/vpc.md#vpc-nacl-ephemeral-windows-49152-65535)
  say: forty-nine one fifty-two to sixty-five five thirty-five
vpc-nacl-every-subnet-associated
  claim: Each subnet must be associated with a network ACL, and every subnet you create is automatically associated with the default network ACL of the VPC, which allows all inbound and outbound traffic.
  scope: per subnet; default; not adjustable.
  link: [each subnet must be associated with a network ACL](../facts/vpc.md#vpc-nacl-every-subnet-associated)
  link: [automatically associated with the default network ACL for the VPC](../facts/vpc.md#vpc-nacl-every-subnet-associated)
  link: [The default network ACL allows all inbound and outbound traffic](../facts/vpc.md#vpc-nacl-every-subnet-associated)
  say: every subnet has a network ACL | a new subnet gets the default network ACL
vpc-nacl-ipv4-ipv6-separate
  claim: Network ACLs evaluate IPv4 and IPv6 traffic separately, so no rule for IPv4 traffic applies to IPv6 traffic.
  link: [IPv4 and IPv6 traffic are evaluated separately](../facts/vpc.md#vpc-nacl-ipv4-ipv6-separate)
  link: [none of the rules for IPv4 traffic apply to IPv6 traffic](../facts/vpc.md#vpc-nacl-ipv4-ipv6-separate)
  say: IPv4 and IPv6 are checked separately
vpc-nacl-no-charge
  claim: There is no additional charge for using network ACLs.
  link: [There is no additional charge for using network ACLs](../facts/vpc.md#vpc-nacl-no-charge)
  say: network ACLs cost nothing extra
vpc-nacl-no-prefix-lists
  claim: You cannot reference prefix lists in network ACL rules; you can instead get the IP address ranges of a service from its prefix list.
  link: [You can't reference prefix lists in network ACL rules](../facts/vpc.md#vpc-nacl-no-prefix-lists)
  say: network ACLs do not take prefix lists
vpc-nacl-one-per-subnet-many-subnets
  claim: One network ACL can be associated with several subnets, but a subnet can be associated with only one network ACL at a time; a new association removes the previous one.
  scope: per subnet.
  link: [You can associate a network ACL with multiple subnets](../facts/vpc.md#vpc-nacl-one-per-subnet-many-subnets)
  link: [a subnet can be associated with only one network ACL at a time](../facts/vpc.md#vpc-nacl-one-per-subnet-many-subnets)
  link: [the previous association is removed](../facts/vpc.md#vpc-nacl-one-per-subnet-many-subnets)
  say: one network ACL per subnet at a time
vpc-nacl-pmtud-icmp-type3-code4
  claim: When the MTU between hosts in your subnets differs, or instances talk to peers over the internet, you must add a network ACL rule, inbound and outbound, that allows the ICMP message Destination Unreachable: Fragmentation Needed (type 3, code 4) so that Path MTU Discovery works.
  link: [(Type 3, Code 4)](../facts/vpc.md#vpc-nacl-pmtud-icmp-type3-code4)
  link: [you must add the following network ACL rule, both inbound and outbound](../facts/vpc.md#vpc-nacl-pmtud-icmp-type3-code4)
  say: ICMP type three, code four | add it inbound and outbound
vpc-nacl-rule-number-increments
  claim: AWS recommends creating network ACL rules in increments, for example of 10 or 100, so that you can insert new rules later.
  link: [increments of 10 or 100](../facts/vpc.md#vpc-nacl-rule-number-increments)
  say: steps of ten or a hundred
vpc-nacl-rule-order-first-match
  claim: Each network ACL rule allows or denies traffic and has a number from 1 to 32766; rules are evaluated in order starting with the lowest number, and the first rule that matches is applied without evaluating any further rules.
  scope: per network ACL rule.
  link: [a number from 1 to 32766](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  link: [starting with the lowest numbered rule](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  link: [we do not evaluate any additional rules](../facts/vpc.md#vpc-nacl-rule-order-first-match)
  say: rule numbers one to thirty-two thousand seven hundred sixty-six | lowest number first | the first match wins
vpc-nacl-stateless-needs-response-rule
  claim: Network ACLs are stateless, so an outbound rule that allows responses to inbound traffic is required; security groups are stateful, so no response rule is needed.
  link: [Network ACLs are stateless](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
  link: [you must include a rule that allows responses to the inbound traffic](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
  link: [Security groups are stateful](../facts/vpc.md#vpc-nacl-stateless-needs-response-rule)
vpc-nat-55000-connections-per-ip
  claim: Each IPv4 address on a NAT gateway supports up to 55,000 simultaneous connections to each unique destination (destination IP, destination port and protocol); you can raise the limit by associating up to 8 IPv4 addresses (1 primary and 7 secondary) with a zonal NAT gateway, while a regional NAT gateway supports up to 32 IP addresses per Availability Zone.
  scope: per NAT gateway IPv4 address, per unique destination; maximum; not adjustable; 8 addresses for a zonal NAT gateway; a regional NAT gateway supports up to 32 IP addresses per Availability Zone.
  link: [55,000 simultaneous connections](../facts/vpc.md#vpc-nat-55000-connections-per-ip)
  link: [up to 8 IPv4 addresses](../facts/vpc.md#vpc-nat-55000-connections-per-ip)
  say: fifty-five thousand simultaneous connections per IP address | up to eight IPv4 addresses on a zonal NAT gateway, one primary and seven secondary
vpc-nat-ami-end-of-support
  claim: The NAT AMI is built on Amazon Linux AMI 2018.03, which reached the end of standard support on December 31, 2020 and the end of maintenance support on December 31, 2023.
  link: [end of maintenance support on December 31, 2023](../facts/vpc.md#vpc-nat-ami-end-of-support)
vpc-nat-bandwidth-100-gbps
  claim: A zonal NAT gateway, which is created in one Availability Zone, supports 5 Gbps of bandwidth and automatically scales up to 100 Gbps; since June 15, 2022 the ceiling is 100 Gbps, up from 45 Gbps. If you need more, split resources into several subnets with a NAT gateway each.
  scope: per zonal NAT gateway; maximum; not adjustable; automatic scaling; split subnets for more; the NAT gateway basics page describes NAT gateways created in one Availability Zone (zonal), and no saved page gives a figure for regional NAT gateways.
  link: [5 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  link: [up to 100 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  link: [45 Gbps](../facts/vpc.md#vpc-nat-bandwidth-100-gbps)
  say: five gigabits per second | up to one hundred gigabits per second | forty-five gigabits per second (old value)
  changed: 2022-06-15: was 45 Gbps
vpc-nat-device-maps-many-to-one
  claim: A NAT device maps multiple private IPv4 addresses to a single public IPv4 address, letting instances start outbound connections to the internet while preventing unsolicited inbound connections.
  link: [NAT maps multiple private IPv4 addresses to a single public IPv4 address](../facts/vpc.md#vpc-nat-device-maps-many-to-one)
  say: many private addresses to one public address
vpc-nat-instance-disable-source-dest-check
  claim: Each EC2 instance performs source/destination checks by default, so you must disable source/destination checks on a NAT instance, which sends and receives traffic that is not addressed to or from itself.
  link: [Each EC2 instance performs source/destination checks by default](../facts/vpc.md#vpc-nat-instance-disable-source-dest-check)
  link: [you must disable source/destination checks on the NAT instance](../facts/vpc.md#vpc-nat-instance-disable-source-dest-check)
  say: turn off the source/destination check
vpc-nat-instance-public-subnet-and-ip
  claim: A NAT instance must have internet access, so it must be in a public subnet and must have a public IP address or an Elastic IP address.
  link: [it must be in a public subnet](../facts/vpc.md#vpc-nat-instance-public-subnet-and-ip)
  link: [it must have a public IP address or an Elastic IP address](../facts/vpc.md#vpc-nat-instance-public-subnet-and-ip)
  say: in a public subnet
vpc-nat-mtu-8500
  claim: NAT gateways support an MTU of 8500 (documented September 10, 2024); packets larger than 8500 bytes are dropped or fragmented, and instances that reach the internet through a public NAT gateway should keep their MTU at 1500 bytes or less.
  scope: per NAT gateway; maximum; not adjustable.
  link: [8500](../facts/vpc.md#vpc-nat-mtu-8500)
  link: [should not exceed 1500 bytes](../facts/vpc.md#vpc-nat-mtu-8500)
  say: eighty-five hundred bytes | keep the instance MTU at fifteen hundred bytes for internet traffic
vpc-nat-packets-per-second
  claim: A zonal NAT gateway, which is created in one Availability Zone, processes 1 million packets per second and automatically scales up to 10 million packets per second; beyond that it drops packets. Since June 15, 2022 the ceiling is 10 million, up from 4 million packets per second.
  scope: per zonal NAT gateway; maximum; not adjustable; the NAT gateway basics page describes NAT gateways created in one Availability Zone (zonal); no saved page gives a figure for regional NAT gateways.
  link: [up to 10 million packets per second](../facts/vpc.md#vpc-nat-packets-per-second)
  link: [one million packets per second](../facts/vpc.md#vpc-nat-packets-per-second)
  say: up to ten million packets per second | one million packets per second to start
  changed: 2022-06-15: was four million packets
vpc-nat-private-ip-choice-change
  claim: Since November 17, 2022 you can pick the primary private IPv4 address of a NAT gateway when you create it; previously the address was assigned automatically from the subnet range. You cannot change or remove it later, but you can add secondary private IPv4 addresses.
  scope: per NAT gateway.
  link: [November 17, 2022](../facts/vpc.md#vpc-nat-private-ip-choice-change)
  link: [can't change or remove the primary private IPv4 address](../facts/vpc.md#vpc-nat-private-ip-choice-change)
  say: November seventeenth, twenty twenty-two | the primary private address cannot be changed later
  changed: 2022-11-17: was the private IP address was automatically assigned from the IP address range of the subnet
vpc-nat-secondary-addresses-change
  claim: Since January 31, 2023 you can add secondary private IPv4 addresses to public and private NAT gateways; they add ports and so raise the number of concurrent connections the gateway can hold.
  scope: per NAT gateway.
  link: [January 31, 2023](../facts/vpc.md#vpc-nat-secondary-addresses-change)
  link: [increase the number of available ports](../facts/vpc.md#vpc-nat-secondary-addresses-change)
  say: January thirty-first, twenty twenty-three | more ports, so more concurrent connections
vpc-nat64-always-on
  claim: NAT64 is automatically available on existing and new NAT gateways and is not something you enable or disable; the subnet of the NAT gateway does not need to be dual-stack.
  link: [NAT64 is automatically available on your existing NAT gateways or on any new NAT gateways you create](../facts/vpc.md#vpc-nat64-always-on)
  link: [It's not a feature you enable or disable](../facts/vpc.md#vpc-nat64-always-on)
  say: always available
vpc-nat64-ipv6-to-ipv4
  claim: A NAT gateway supports NAT64, translation from IPv6 to IPv4, so IPv6 resources can communicate with IPv4 resources in the same or another VPC, on premises or over the internet; NAT64 works with DNS64 on the Amazon resolver or with your own DNS64 server.
  link: [A NAT gateway supports network address translation from IPv6 to IPv4, popularly known as NAT64](../facts/vpc.md#vpc-nat64-ipv6-to-ipv4)
  link: [use your own DNS64 server](../facts/vpc.md#vpc-nat64-ipv6-to-ipv4)
  say: NAT64 on a NAT gateway
vpc-natgw-cloudwatch-1-minute-15-months
  claim: CloudWatch delivers NAT gateway metric data at 1-minute intervals and retains it for 15 months.
  link: [1-minute intervals](../facts/vpc.md#vpc-natgw-cloudwatch-1-minute-15-months)
  link: [15 months](../facts/vpc.md#vpc-natgw-cloudwatch-1-minute-15-months)
  say: every minute | fifteen months
vpc-natgw-connections-originate-inside-vpc
  claim: Connections through a NAT gateway must always be initiated from within the VPC that contains the NAT gateway.
  scope: per NAT gateway; fixed.
  link: [Connections must always be initiated from within the VPC containing the NAT gateway](../facts/vpc.md#vpc-natgw-connections-originate-inside-vpc)
  say: connections always start inside the VPC
vpc-natgw-cross-az-transfer-charge
  claim: Traffic between a NAT gateway and an EC2 instance in the same Availability Zone over private IP addresses has no data transfer charge; if they are in different Availability Zones, data transfer charges apply.
  scope: per NAT gateway and instance pair.
  link: [no charge for the data transfer between the NAT gateway and the EC2 instance since the traffic stays in the same Availability Zone using private IP addresses](../facts/vpc.md#vpc-natgw-cross-az-transfer-charge)
  link: [data transfer charges between your NAT gateway and EC2 instance if they are in a different Availability Zone](../facts/vpc.md#vpc-natgw-cross-az-transfer-charge)
vpc-natgw-data-processing-any-destination
  claim: NAT gateway data processing charges apply to each gigabyte processed through the gateway regardless of the traffic's source or destination, and standard data transfer charges apply on top.
  scope: per NAT gateway.
  link: [regardless of the traffic's source or destination](../facts/vpc.md#vpc-natgw-data-processing-any-destination)
  link: [You also incur standard AWS data transfer charges for all data transferred via the NAT gateway](../facts/vpc.md#vpc-natgw-data-processing-any-destination)
vpc-natgw-each-active-az-in-production
  claim: In production AWS recommends deploying a NAT gateway in each active Availability Zone.
  scope: per active Availability Zone of a production VPC; zonal NAT gateways.
  link: [deploy a NAT gateway in each active AZ](../facts/vpc.md#vpc-natgw-each-active-az-in-production)
vpc-natgw-endpoints-for-aws-services
  claim: If most NAT gateway traffic goes to AWS services that support interface or gateway endpoints, AWS suggests creating an endpoint for those services instead of sending the traffic through the NAT gateway.
  link: [consider creating an interface endpoint or gateway endpoint for these services](../facts/vpc.md#vpc-natgw-endpoints-for-aws-services)
vpc-natgw-metric-activeconnectioncount
  claim: The ActiveConnectionCount metric is the total number of concurrent active TCP connections through the NAT gateway, and its most useful statistic is Max.
  scope: per NAT gateway.
  link: [ActiveConnectionCount](../facts/vpc.md#vpc-natgw-metric-activeconnectioncount)
  say: active connection count
vpc-natgw-metric-errorportallocation
  claim: The NAT gateway CloudWatch metric ErrorPortAllocation counts the times the NAT gateway could not allocate a source port; a value greater than zero means too many concurrent connections are open through the NAT gateway.
  scope: per NAT gateway.
  link: [ErrorPortAllocation](../facts/vpc.md#vpc-natgw-metric-errorportallocation)
  link: [too many concurrent connections are open through the NAT gateway](../facts/vpc.md#vpc-natgw-metric-errorportallocation)
  say: error port allocation | too many concurrent connections through the NAT gateway
vpc-natgw-metric-idletimeoutcount-350-seconds
  claim: The NAT gateway metric IdleTimeoutCount counts connections that moved from active to idle; a connection becomes idle when it was not closed gracefully and had no activity for the last 350 seconds.
  scope: per NAT gateway; fixed; connection not closed gracefully.
  link: [IdleTimeoutCount](../facts/vpc.md#vpc-natgw-metric-idletimeoutcount-350-seconds)
  link: [350 seconds](../facts/vpc.md#vpc-natgw-metric-idletimeoutcount-350-seconds)
  say: idle timeout count | three hundred fifty seconds
vpc-natgw-metric-packetsdropcount
  claim: The PacketsDropCount metric is the number of packets dropped by the NAT gateway; if dropped packets exceed 0.01 percent of the total traffic on the NAT gateway, there may be an issue with the Amazon VPC service.
  scope: per NAT gateway.
  link: [PacketsDropCount](../facts/vpc.md#vpc-natgw-metric-packetsdropcount)
  link: [0.01 percent](../facts/vpc.md#vpc-natgw-metric-packetsdropcount)
  say: packets drop count | zero point zero one percent
vpc-natgw-no-security-group-use-nacl
  claim: You cannot associate a security group with a NAT gateway; control traffic with the security groups of the instances behind it and with the network ACL of the NAT gateway's subnet, where NAT gateways use ports 1024 to 65535.
  scope: per NAT gateway.
  link: [You can't associate a security group with a NAT gateway](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
  link: [You can use a network ACL to control the traffic to and from the subnet for your NAT gateway](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
  link: [NAT gateways use ports 1024–65535](../facts/vpc.md#vpc-natgw-no-security-group-use-nacl)
vpc-natgw-not-via-peering-or-vgw
  claim: You cannot route traffic to a NAT gateway through a VPC peering connection, nor from Site-to-Site VPN or Direct Connect through a virtual private gateway; with a transit gateway instead of a virtual private gateway, VPN or Direct Connect traffic can use the NAT gateway.
  scope: per NAT gateway; fixed.
  link: [can't route traffic to a NAT gateway through a VPC peering connection](../facts/vpc.md#vpc-natgw-not-via-peering-or-vgw)
  link: [can't route traffic to a NAT gateway from Site-to-Site VPN or Direct Connect using a virtual private gateway](../facts/vpc.md#vpc-natgw-not-via-peering-or-vgw)
  link: [You can route traffic to a NAT gateway from Site-to-Site VPN or Direct Connect if you use a transit gateway instead of a virtual private gateway](../facts/vpc.md#vpc-natgw-not-via-peering-or-vgw)
  say: no NAT gateway sharing over peering | with a transit gateway it works
vpc-natgw-one-az-redundant-in-zone
  claim: Each NAT gateway is created in one specific Availability Zone and is implemented with redundancy inside that zone.
  scope: per zonal NAT gateway; zonal NAT gateways (a regional NAT gateway expands across Availability Zones: vpc-regional-natgw-vs-zonal).
  link: [Each NAT gateway is created in a specific Availability Zone and implemented with redundancy in that zone](../facts/vpc.md#vpc-natgw-one-az-redundant-in-zone)
vpc-natgw-partial-hour-full-hour
  claim: Each partial NAT Gateway-hour consumed is billed as a full hour.
  scope: per NAT gateway.
  link: [Each partial NAT Gateway-hour consumed is billed as a full hour](../facts/vpc.md#vpc-natgw-partial-hour-full-hour)
vpc-natgw-preferred-over-nat-instance
  claim: AWS recommends a NAT gateway over a NAT instance because it provides better availability, higher bandwidth and needs less administrative effort.
  link: [NAT gateways provide better availability, higher bandwidth, and requires less administrative effort](../facts/vpc.md#vpc-natgw-preferred-over-nat-instance)
vpc-natgw-price-example-ohio
  claim: In the pricing example for US East (Ohio), a NAT gateway costs $0.045 per hour while it is provisioned and available, and $0.045 for 1 GB data processed by the NAT gateway.
  scope: per NAT gateway, US East (Ohio); example rates on the pricing page; rates vary by Region.
  link: [$0.045 per hour](../facts/vpc.md#vpc-natgw-price-example-ohio)
  link: [$0.045 for 1 GB data processed](../facts/vpc.md#vpc-natgw-price-example-ohio)
  say: four and a half cents per hour | four and a half cents per gigabyte processed
vpc-natgw-pricing-dimensions
  claim: A NAT gateway is charged for each hour that it is available and for each gigabyte of data that it processes.
  scope: per NAT gateway.
  link: [charged for each hour that your NAT gateway is available](../facts/vpc.md#vpc-natgw-pricing-dimensions)
  link: [each gigabyte of data that it processes](../facts/vpc.md#vpc-natgw-pricing-dimensions)
vpc-natgw-private-connectivity-type
  claim: A private NAT gateway sends traffic to other VPCs or an on-premises network through a transit gateway or a virtual private gateway; you cannot associate an Elastic IP address with it, and if its traffic is routed to an internet gateway, the internet gateway drops the traffic.
  scope: per NAT gateway; connectivity type private.
  link: [to other VPCs or on-premises networks using Transit Gateway or a virtual private gateway](../facts/vpc.md#vpc-natgw-private-connectivity-type)
  link: [You can't associate an Elastic IP address with a private NAT gateway](../facts/vpc.md#vpc-natgw-private-connectivity-type)
  link: [if you route traffic from the private NAT gateway to the internet gateway, the internet gateway drops the traffic](../facts/vpc.md#vpc-natgw-private-connectivity-type)
  say: it reaches other VPCs or on premises, not the internet | no Elastic IP on a private NAT gateway
vpc-natgw-protocols-tcp-udp-icmp
  claim: A NAT gateway supports the TCP, UDP and ICMP protocols, and works for IPv4 or IPv6 traffic (NAT64 for IPv6).
  scope: per NAT gateway.
  link: [TCP, UDP, and ICMP](../facts/vpc.md#vpc-natgw-protocols-tcp-udp-icmp)
  link: [NAT gateways are supported for IPv4 or IPv6 traffic](../facts/vpc.md#vpc-natgw-protocols-tcp-udp-icmp)
  say: TCP, UDP and ICMP
vpc-natgw-public-connectivity-type
  claim: A public NAT gateway, the default connectivity type, is created in a public subnet, must get an Elastic IP address at creation, and routes its traffic to the VPC's internet gateway; the instances behind it cannot receive unsolicited inbound connections from the internet.
  scope: per NAT gateway; default; not adjustable; connectivity type public; zonal NAT gateway (a regional NAT gateway does not need a public subnet: vpc-regional-natgw-no-public-subnet).
  link: [**Public** – (Default)](../facts/vpc.md#vpc-natgw-public-connectivity-type)
  link: [must associate an Elastic IP address with the NAT gateway at creation](../facts/vpc.md#vpc-natgw-public-connectivity-type)
  link: [You create a public NAT gateway in a public subnet](../facts/vpc.md#vpc-natgw-public-connectivity-type)
  say: public is the default type | it needs an Elastic IP at creation
vpc-natgw-purpose
  claim: A NAT gateway lets instances in a private subnet connect to services outside the VPC while external services cannot initiate a connection to those instances.
  scope: per NAT gateway.
  link: [instances in a private subnet can connect to services outside your VPC but external services can't initiate a connection with those instances](../facts/vpc.md#vpc-natgw-purpose)
  link: [a Network Address Translation (NAT) service](../facts/vpc.md#vpc-natgw-purpose)
  say: outbound only: private instances go out, nothing comes in uninvited
vpc-natgw-route-from-private-subnet
  claim: To give instances in a private subnet internet access, you create a NAT gateway (or NAT instance) in a public subnet and add a route in the private subnet's route table that sends 0.0.0.0/0 to the NAT device.
  scope: per private subnet route table; zonal NAT gateway or NAT instance (a regional NAT gateway does not need a public subnet: vpc-regional-natgw-no-public-subnet).
  link: [create a NAT gateway or launch a NAT instance in a public subnet](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  link: [routes IPv4 internet traffic (`0.0.0.0/0`) to the NAT device](../facts/vpc.md#vpc-natgw-route-from-private-subnet)
  say: the NAT gateway sits in a public subnet | the private subnet's default route points at the NAT gateway
vpc-natgw-same-az-reduces-charges
  claim: If your resources send or receive a significant volume of traffic across Availability Zones, keep them in the same Availability Zone as the NAT gateway, or create a NAT gateway in each Availability Zone with resources, to reduce cross-AZ data transfer charges.
  scope: a significant volume of traffic across Availability Zones.
  link: [ensure that the resources are in the same Availability Zone as the NAT gateway](../facts/vpc.md#vpc-natgw-same-az-reduces-charges)
  link: [create a NAT gateway in each Availability Zone with resources](../facts/vpc.md#vpc-natgw-same-az-reduces-charges)
vpc-natgw-shared-across-azs-loses-internet
  claim: If resources in several Availability Zones share one NAT gateway and that gateway's Availability Zone goes down, resources in the other Availability Zones lose internet access; create a NAT gateway in each Availability Zone and route each zone to its own gateway.
  scope: zonal NAT gateways used by resources in several Availability Zones; zonal NAT gateways (a regional NAT gateway expands into each Availability Zone that has resources: vpc-regional-natgw-vs-zonal).
  link: [resources in the other Availability Zones lose internet access](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
  link: [create a NAT gateway in each Availability Zone, and configure your routing to ensure that resources use the NAT gateway in the same Availability Zone](../facts/vpc.md#vpc-natgw-shared-across-azs-loses-internet)
vpc-natgw-stateful-allows-outbound
  claim: A NAT gateway itself allows all outbound traffic and the traffic received in response to an outbound request, so it is stateful.
  link: [it is therefore stateful](../facts/vpc.md#vpc-natgw-stateful-allows-outbound)
  say: it is stateful
vpc-natgw-troubleshoot-no-internet-causes
  claim: When instances behind a public NAT gateway cannot reach the internet, the cause may be that the NAT gateway is not ready, the route tables are wrong, security groups or network ACLs block the traffic, or the protocol is not supported.
  link: [The NAT gateway is not ready to serve traffic](../facts/vpc.md#vpc-natgw-troubleshoot-no-internet-causes)
  link: [Your route tables are not configured correctly](../facts/vpc.md#vpc-natgw-troubleshoot-no-internet-causes)
  link: [Your security groups or network ACLs are blocking inbound or outbound traffic](../facts/vpc.md#vpc-natgw-troubleshoot-no-internet-causes)
  say: wrong routes
vpc-natgw-troubleshoot-route-placement
  claim: For internet access through a public NAT gateway, the NAT gateway must be in a public subnet whose route table sends internet traffic to an internet gateway, and the instance must be in a private subnet whose route table sends internet traffic to the NAT gateway.
  scope: a public zonal NAT gateway and the instances behind it; zonal NAT gateway (a regional NAT gateway has its own route table and needs no public subnet: vpc-regional-natgw-no-public-subnet).
  link: [The NAT gateway must be in a public subnet with a route table that routes internet traffic to an internet gateway](../facts/vpc.md#vpc-natgw-troubleshoot-route-placement)
  link: [Your instance must be in a private subnet with a route table that routes internet traffic to the NAT gateway](../facts/vpc.md#vpc-natgw-troubleshoot-route-placement)
  say: NAT gateway in a public subnet | instance in a private subnet
vpc-natgw-vs-instance-availability
  claim: A NAT gateway is highly available with redundancy inside its Availability Zone, and you create one per Availability Zone for a zone-independent design; a NAT instance needs a script to manage failover between instances.
  link: [Highly available](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Use a script to manage failover between instances](../facts/vpc.md#vpc-natgw-vs-instance-availability)
  link: [Create a NAT gateway in each Availability Zone to ensure zone-independent architecture](../facts/vpc.md#vpc-natgw-vs-instance-availability)
vpc-natgw-vs-instance-bandwidth
  claim: A NAT gateway scales up to 100 Gbps; a NAT instance's bandwidth depends on its instance type.
  scope: per NAT gateway; maximum.
  link: [Scale up to 100 Gbps](../facts/vpc.md#vpc-natgw-vs-instance-bandwidth)
  link: [Depends on the bandwidth of the instance type](../facts/vpc.md#vpc-natgw-vs-instance-bandwidth)
vpc-natgw-vs-instance-bastion
  claim: A NAT gateway cannot serve as a bastion server; a NAT instance can.
  scope: per NAT gateway.
  link: [Not supported](../facts/vpc.md#vpc-natgw-vs-instance-bastion)
  link: [Use as a bastion server](../facts/vpc.md#vpc-natgw-vs-instance-bastion)
vpc-natgw-vs-instance-cost
  claim: A NAT gateway is charged by the number of gateways, the duration of use and the data sent through them; a NAT instance is charged by the number of instances, the duration of use and the instance type and size.
  scope: per NAT gateway or NAT instance.
  link: [Charged depending on the number of NAT gateways you use, duration of usage, and amount of data that you send through the NAT gateways](../facts/vpc.md#vpc-natgw-vs-instance-cost)
  link: [Charged depending on the number of NAT instances that you use, duration of usage, and instance type and size](../facts/vpc.md#vpc-natgw-vs-instance-cost)
vpc-natgw-vs-instance-flow-logs
  claim: Both NAT gateways and NAT instances support flow logs to capture their traffic.
  scope: per NAT gateway.
  link: [Use flow logs to capture the traffic](../facts/vpc.md#vpc-natgw-vs-instance-flow-logs)
vpc-natgw-vs-instance-ip-fragmentation
  claim: A NAT gateway forwards IP-fragmented packets only for UDP and drops fragmented TCP and ICMP packets; a NAT instance reassembles fragmented packets for UDP, TCP and ICMP.
  scope: per NAT gateway.
  link: [Supports forwarding of IP fragmented packets for the UDP protocol](../facts/vpc.md#vpc-natgw-vs-instance-ip-fragmentation)
  link: [Fragmented packets for these protocols will get dropped](../facts/vpc.md#vpc-natgw-vs-instance-ip-fragmentation)
  link: [Supports reassembly of IP fragmented packets for the UDP, TCP, and ICMP protocols](../facts/vpc.md#vpc-natgw-vs-instance-ip-fragmentation)
vpc-natgw-vs-instance-maintenance
  claim: A NAT gateway is managed by AWS with no maintenance on your side; a NAT instance is managed by you, including software updates and operating system patches.
  link: [Managed by AWS](../facts/vpc.md#vpc-natgw-vs-instance-maintenance)
  link: [Managed by you, for example, by installing software updates or operating system patches on the instance](../facts/vpc.md#vpc-natgw-vs-instance-maintenance)
vpc-natgw-vs-instance-network-acls
  claim: For both a NAT gateway and a NAT instance, you use a network ACL to control the traffic to and from the subnet in which the NAT device resides.
  scope: per NAT gateway.
  link: [Use a network ACL to control the traffic to and from the subnet in which your NAT gateway resides](../facts/vpc.md#vpc-natgw-vs-instance-network-acls)
vpc-natgw-vs-instance-performance
  claim: NAT gateway software is optimized for NAT traffic; a NAT instance is a generic AMI configured to perform NAT.
  link: [Software is optimized for handling NAT traffic](../facts/vpc.md#vpc-natgw-vs-instance-performance)
  link: [A generic AMI that's configured to perform NAT](../facts/vpc.md#vpc-natgw-vs-instance-performance)
vpc-natgw-vs-instance-port-forwarding
  claim: A NAT gateway does not support port forwarding; a NAT instance can be customized manually to support it.
  scope: per NAT gateway.
  link: [Not supported](../facts/vpc.md#vpc-natgw-vs-instance-port-forwarding)
  link: [Manually customize the configuration to support port forwarding](../facts/vpc.md#vpc-natgw-vs-instance-port-forwarding)
vpc-natgw-vs-instance-private-ip
  claim: A NAT gateway's private IP address is selected automatically from the subnet's IP address range when you create it; for a NAT instance you assign a specific private IP address from the subnet's range when you launch it.
  scope: per NAT gateway; row of the NAT gateway versus NAT instance table; since November 17, 2022 you can also choose the primary private IPv4 address at creation (vpc-nat-private-ip-choice-change).
  link: [Automatically selected from the subnet's IP address range](../facts/vpc.md#vpc-natgw-vs-instance-private-ip)
  link: [Assign a specific private IP address from the subnet's IP address range](../facts/vpc.md#vpc-natgw-vs-instance-private-ip)
vpc-natgw-vs-instance-public-ip
  claim: For a public NAT gateway you choose the Elastic IP address to associate at creation; a NAT instance uses an Elastic IP address or a public IP address, and you can change it at any time by associating a new Elastic IP address with the instance.
  scope: per NAT gateway.
  link: [Choose the Elastic IP address to associate with a public NAT gateway at creation](../facts/vpc.md#vpc-natgw-vs-instance-public-ip)
  link: [You can change the public IP address at any time by associating a new Elastic IP address with the instance](../facts/vpc.md#vpc-natgw-vs-instance-public-ip)
vpc-natgw-vs-instance-security-groups
  claim: You cannot associate security groups with a NAT gateway, only with the resources behind it; a NAT instance can have its own security group.
  scope: per NAT gateway.
  link: [You cannot associate security groups with NAT gateways](../facts/vpc.md#vpc-natgw-vs-instance-security-groups)
  link: [Associate with your NAT instance and the resources behind your NAT instance to control inbound and outbound traffic](../facts/vpc.md#vpc-natgw-vs-instance-security-groups)
vpc-natgw-vs-instance-timeout
  claim: When a connection times out, a NAT gateway returns an RST packet to resources that try to continue the connection and does not send a FIN; a NAT instance sends a FIN packet to close the connection.
  link: [a NAT gateway returns an RST packet to any resources behind the NAT gateway that attempt to continue the connection (it does not send a FIN packet)](../facts/vpc.md#vpc-natgw-vs-instance-timeout)
  link: [a NAT instance sends a FIN packet to resources behind the NAT instance to close the connection](../facts/vpc.md#vpc-natgw-vs-instance-timeout)
vpc-natgw-vs-instance-traffic-metrics
  claim: A NAT gateway has its own CloudWatch metrics; for a NAT instance you view the CloudWatch metrics of the instance.
  scope: per NAT gateway.
  link: [CloudWatch metrics for the NAT gateway](../facts/vpc.md#vpc-natgw-vs-instance-traffic-metrics)
  link: [View CloudWatch metrics for the instance](../facts/vpc.md#vpc-natgw-vs-instance-traffic-metrics)
vpc-natgw-vs-instance-type-and-size
  claim: A NAT gateway is a uniform offering with no type or size to choose; for a NAT instance you choose an instance type and size for the predicted workload.
  link: [Uniform offering; you don't need to decide on the type or size](../facts/vpc.md#vpc-natgw-vs-instance-type-and-size)
  link: [Choose a suitable instance type and size, according to your predicted workload](../facts/vpc.md#vpc-natgw-vs-instance-type-and-size)
vpc-nau-lambda-function-six-units
  claim: A Lambda function counts as 6 NAU units toward the Network Address Usage of a VPC.
  scope: per Lambda function in the VPC; fixed.
  link: [6](../facts/vpc.md#vpc-nau-lambda-function-six-units)
  say: six NAU units
vpc-nau-metrics-change
  claim: Since October 4, 2022 you can enable Network Address Usage (NAU) metrics for a VPC; NAU is a metric applied to resources in the VPC that helps you plan for and monitor the size of the VPC.
  scope: per VPC.
  link: [October 4, 2022](../facts/vpc.md#vpc-nau-metrics-change)
  link: [plan for and monitor the size of your VPC](../facts/vpc.md#vpc-nau-metrics-change)
  say: October fourth, twenty twenty-two | a size metric for a VPC
vpc-nau-nat-gateway-six-units
  claim: A NAT gateway counts as 6 NAU units.
  scope: per NAT gateway; fixed.
  link: [6 NAU units](../facts/vpc.md#vpc-nau-nat-gateway-six-units)
  say: six NAU units per NAT gateway
vpc-nau-nlb-per-az-six-units
  claim: A Network Load Balancer counts as 6 NAU units per Availability Zone toward the Network Address Usage of a VPC.
  scope: per Network Load Balancer, per Availability Zone; fixed.
  link: [6](../facts/vpc.md#vpc-nau-nlb-per-az-six-units)
  say: six NAU units per Availability Zone
vpc-nau-one-unit-per-ip-address
  claim: Each private or public IPv4 address and each IPv6 address assigned to a network interface of an EC2 instance in the VPC counts as 1 NAU unit.
  scope: per IP address on an instance network interface; fixed.
  link: [1 NAU unit](../facts/vpc.md#vpc-nau-one-unit-per-ip-address)
  say: one NAU unit per address
vpc-nau-tgw-attachment-six-units
  claim: A transit gateway attachment counts as 6 NAU units toward the Network Address Usage of a VPC.
  scope: per transit gateway attachment; fixed.
  link: [6](../facts/vpc.md#vpc-nau-tgw-attachment-six-units)
  say: six NAU units
vpc-nau-vpc-endpoint-six-units-per-az
  claim: A VPC endpoint counts as 6 NAU units per Availability Zone.
  scope: per VPC endpoint, per Availability Zone; fixed.
  link: [6 NAU units per Availability Zone](../facts/vpc.md#vpc-nau-vpc-endpoint-six-units-per-az)
  say: six NAU units per AZ for each endpoint
vpc-network-firewall-stateful-managed
  claim: AWS Network Firewall filters network traffic at the perimeter of a VPC; it is a stateful, managed network firewall and intrusion detection and prevention service.
  link: [filter network traffic at the perimeter of your VPC](../facts/vpc.md#vpc-network-firewall-stateful-managed)
  link: [a stateful, managed, network firewall and intrusion detection and prevention service](../facts/vpc.md#vpc-network-firewall-stateful-managed)
  say: a stateful managed firewall with intrusion prevention
vpc-nondefault-subnet-no-public-ip-by-default
  claim: By default an instance launched into a nondefault subnet has a private IPv4 address but no public IPv4 address, unless you assign one at launch or change the subnet's public IP address attribute; such instances can talk to each other but cannot reach the internet.
  scope: per nondefault subnet; default; adjustable.
  link: [has a private IPv4 address, but no public IPv4 address](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  link: [unless you specifically assign one at launch, or you modify the subnet's public IP address attribute](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  link: [can communicate with each other, but can't access the internet](../facts/vpc.md#vpc-nondefault-subnet-no-public-ip-by-default)
  say: private address only, no public address
vpc-outposts-subnet-local-gateway
  claim: You extend a VPC to an Outpost by creating a subnet for the Outpost in that VPC; on an Outposts rack a local gateway handles connectivity between the VPC and on-premises networks.
  link: [you can extend any VPC in the Region to your Outpost by creating a subnet for the Outpost in that VPC](../facts/vpc.md#vpc-outposts-subnet-local-gateway)
  link: [A local gateway handles the network connectivity between your VPC and on-premises networks](../facts/vpc.md#vpc-outposts-subnet-local-gateway)
  say: create a subnet on the Outpost | a local gateway connects to on premises
vpc-prefix-list-definition
  claim: A managed prefix list is a set of one or more CIDR blocks that you can reference as a set in security group rules and routes instead of referencing each CIDR block individually.
  link: [A managed prefix list is a set of one or more CIDR blocks](../facts/vpc.md#vpc-prefix-list-definition)
  link: [reference them as a set in security group rules and routes](../facts/vpc.md#vpc-prefix-list-definition)
  say: a named set of CIDR blocks
vpc-prefix-list-rules-region-single-family
  claim: A customer-managed prefix list supports one type of IP addressing only (IPv4 or IPv6), applies only to the Region where you created it, and needs a maximum number of entries set at creation, which counts against the entry quota of each resource that references it.
  link: [You cannot combine IPv4 and IPv6 CIDR blocks in a single prefix list](../facts/vpc.md#vpc-prefix-list-rules-region-single-family)
  link: [A prefix list applies only to the Region where you created it](../facts/vpc.md#vpc-prefix-list-rules-region-single-family)
  link: [the maximum number of entries for the prefix lists counts against the quota for the number of entries for the resource](../facts/vpc.md#vpc-prefix-list-rules-region-single-family)
  say: one Region only
vpc-prefix-list-types
  claim: Customer-managed prefix lists are IP ranges that you define, manage and can share with other accounts; AWS-managed prefix lists are IP ranges of AWS services that you cannot create, modify, share or delete.
  link: [You can share your prefix list with other AWS accounts](../facts/vpc.md#vpc-prefix-list-types)
  link: [You cannot create, modify, share, or delete an AWS-managed prefix list](../facts/vpc.md#vpc-prefix-list-types)
  say: AWS-managed lists are read-only
vpc-primary-cidr-cannot-disassociate
  claim: You can disassociate a secondary CIDR block from a VPC, but you cannot disassociate the primary CIDR block the VPC was created with.
  scope: per VPC; fixed.
  link: [cannot disassociate the CIDR block with which you originally created the VPC (the primary CIDR block)](../facts/vpc.md#vpc-primary-cidr-cannot-disassociate)
  link: [You can disassociate a CIDR block that you've associated with your VPC](../facts/vpc.md#vpc-primary-cidr-cannot-disassociate)
  say: the primary CIDR block cannot be removed
vpc-private-ip-persists-until-termination
  claim: A private IPv4 address stays associated with the network interface when the instance is stopped and restarted, and is released only when the instance is terminated.
  scope: per network interface.
  link: [remains associated with the network interface when the instance is stopped and restarted](../facts/vpc.md#vpc-private-ip-persists-until-termination)
  link: [released when the instance is terminated](../facts/vpc.md#vpc-private-ip-persists-until-termination)
  say: the private address survives a stop and start
vpc-private-ipv6-change
  claim: VPCs and subnets can use private IPv6 addresses, which are not advertised and cannot be advertised on the internet from AWS, are only available in Amazon VPC IP Address Manager (IPAM), and have no charge; the VPC guide added this information on August 8, 2024.
  scope: per VPC or subnet; allocated from an IPAM pool.
  link: [August 8, 2024](../facts/vpc.md#vpc-private-ipv6-change)
  link: [not advertised and cannot be advertised on the Internet from AWS](../facts/vpc.md#vpc-private-ipv6-change)
  link: [no charge for private IPv6 addresses](../facts/vpc.md#vpc-private-ipv6-change)
  say: August eighth, twenty twenty-four | private IPv6: never advertised to the internet | private IPv6 addresses are free
vpc-private-nat-allow-listed-and-overlapping
  claim: Use cases for a private NAT gateway include reaching an on-premises network through a pool of allow-listed addresses and enabling communication between networks with overlapping CIDR ranges.
  link: [using a pool of allow-listed addresses](../facts/vpc.md#vpc-private-nat-allow-listed-and-overlapping)
  link: [enable communication between networks even if they have overlapping CIDR ranges](../facts/vpc.md#vpc-private-nat-allow-listed-and-overlapping)
  say: allow-listed source addresses | overlapping CIDR ranges
vpc-privatelink-no-igw-or-nat-for-aws-services
  claim: With AWS PrivateLink, resources in a VPC connect to AWS services using private IP addresses, so you do not need an internet gateway or NAT device to access AWS services; gateway VPC endpoints give connectivity to Amazon S3 and DynamoDB without an internet gateway or NAT device.
  link: [you do not need to use an internet gateway or NAT device to access AWS services](../facts/vpc.md#vpc-privatelink-no-igw-or-nat-for-aws-services)
  link: [without requiring an internet gateway or a NAT device for your VPC](../facts/vpc.md#vpc-privatelink-no-igw-or-nat-for-aws-services)
vpc-prod-at-least-two-azs
  claim: For a production environment AWS recommends selecting at least two Availability Zones and deploying resources evenly in each active Availability Zone.
  link: [at least two Availability Zones](../facts/vpc.md#vpc-prod-at-least-two-azs)
  link: [deploy your AWS resources evenly in each active Availability Zone](../facts/vpc.md#vpc-prod-at-least-two-azs)
vpc-public-ip-from-amazon-pool-released
  claim: A public IPv4 address comes from Amazon's pool and is not associated with your account; when it is disassociated from your instance it goes back to the pool and you cannot get it again.
  scope: per instance.
  link: [assigned from Amazon's pool of public IP addresses; it's not associated with your account](../facts/vpc.md#vpc-public-ip-from-amazon-pool-released)
  link: [released back into the pool, and is no longer available for you to use](../facts/vpc.md#vpc-public-ip-from-amazon-pool-released)
  say: it belongs to Amazon's pool, not to your account | once released you cannot get it back
vpc-public-ip-insights-no-cost
  claim: Public IP Insights, a feature of Amazon VPC IP Address Manager (IPAM) available at no cost, helps you monitor, analyze and audit your use of public IPv4 addresses; it launched with the announcement of the public IPv4 charge.
  link: [Public IP Insights](../facts/vpc.md#vpc-public-ip-insights-no-cost)
  say: Public IP Insights in VPC IPAM, free
vpc-public-ip-traffic-stays-on-aws-network
  claim: Packets that start on the AWS network with a destination on the AWS network stay on the AWS global network, whether the destination is a private or a public IP address, except traffic to or from AWS China Regions and the AWS European Sovereign Cloud Region.
  link: [stay on the AWS global network](../facts/vpc.md#vpc-public-ip-traffic-stays-on-aws-network)
  link: [This is true whether the destination is a private IP address or a public IP address](../facts/vpc.md#vpc-public-ip-traffic-stays-on-aws-network)
  link: [if EC2 instances in two VPCs communicate using public IP addresses, the traffic stays in the private global network](../facts/vpc.md#vpc-public-ip-traffic-stays-on-aws-network)
  say: it stays on the AWS network
vpc-public-ipv4-avoid-per-instance-with-elb-nat
  claim: To reduce the public IPv4 charge, AWS points to Elastic Load Balancers for inbound traffic and NAT gateways for outbound traffic instead of a public IPv4 address on each instance, and to faster adoption of IPv6.
  scope: per workload.
  link: [use Elastic Load Balancers and NAT Gateways for ingress and egress traffic](../facts/vpc.md#vpc-public-ipv4-avoid-per-instance-with-elb-nat)
  say: load balancer in, NAT gateway out, no public IP per instance
vpc-public-ipv4-charge-2024
  claim: Since February 1, 2024 AWS charges $0.005 per IP per hour for public IPv4 addresses, whether in use or idle, including the public IPv4 addresses of running instances and Elastic IP addresses; before that date an in-use public IPv4 address had no charge. Addresses in an Amazon-provided contiguous IPv4 block have their own hourly rate.
  scope: per public IPv4 address, per hour; the Amazon-provided contiguous IPv4 block has a separate hourly rate.
  link: [$0.005 per IP per hour](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [February 1, 2024](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [AWS charges for all public IPv4 addresses](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [No charge](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  say: half a cent per address per hour | February first, twenty twenty-four | every public IPv4 address is billed, attached or not | no charge
  changed: 2024-02-01: was No charge
vpc-public-ipv4-contiguous-block-price
  claim: Each public IPv4 address in an Amazon-provided contiguous IPv4 block is charged $0.008 per public IPv4 address per hour, and all addresses in the block are charged from the time the block is provisioned, without separate in-use and idle charges.
  scope: per public IPv4 address in an Amazon-provided contiguous block; the whole block is charged when it is provisioned.
  link: [$0.008 per public IPv4 address per hour](../facts/vpc.md#vpc-public-ipv4-contiguous-block-price)
  say: under one cent per address per hour
vpc-public-ipv4-hourly-in-use-or-idle
  claim: A public IPv4 address is billed at an hourly rate per address, calculated in one-second increments with a minimum of 60 seconds, and the price is the same whether the address is in use on a resource or idle in the account.
  scope: per public IPv4 address.
  link: [You pay an hourly rate for each public IPv4 address used by your AWS account](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [minimum of 60 seconds](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
  link: [The price is the same whether the public IPv4 address is in-use](../facts/vpc.md#vpc-public-ipv4-hourly-in-use-or-idle)
vpc-public-ipv4-idle-and-secondary-eip-charged-before-2024
  claim: Even before February 1, 2024, an idle Elastic IP address in the account and an additional (secondary) Elastic IP address on a running EC2 instance were charged at $0.005 per IP per hour; the change on that date added the charge for in-use public IPv4 addresses.
  scope: per Elastic IP address.
  link: [$0.005](../facts/vpc.md#vpc-public-ipv4-idle-and-secondary-eip-charged-before-2024)
  link: [February 1, 2024](../facts/vpc.md#vpc-public-ipv4-idle-and-secondary-eip-charged-before-2024)
  say: half a cent per hour | February first, twenty twenty-four
vpc-public-subnet-only-if-reachable
  claim: A server that does not need to be directly reachable from the internet should not be deployed in a public subnet.
  link: [If a server doesn't need to be directly reachable from the internet, you should not deploy it into a public subnet](../facts/vpc.md#vpc-public-subnet-only-if-reachable)
vpc-public-vs-private-subnet-by-igw-route
  claim: A subnet is public when its route table has a route to an internet gateway and private when it does not; instances in a private subnet cannot reach the internet even if they have public IP addresses.
  scope: per subnet.
  link: [If a subnet is associated with a route table that has a route to an internet gateway, it's known as a *public subnet*](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  link: [If a subnet is associated with a route table that does not have a route to an internet gateway, it's known as a *private subnet*](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  link: [instances in the private subnet can't communicate with the internet, even if they have public IP addresses](../facts/vpc.md#vpc-public-vs-private-subnet-by-igw-route)
  say: public means a route to the internet gateway | private means no route to the internet gateway
vpc-quota-carrier-gateways-per-vpc
  claim: A VPC can have 1 carrier gateway, and this quota is not adjustable.
  scope: per VPC; maximum; not adjustable.
  link: [1 carrier gateway](../facts/vpc.md#vpc-quota-carrier-gateways-per-vpc)
  say: one carrier gateway per VPC
vpc-quota-egress-only-igw-per-region
  claim: The default quota is 5 egress-only internet gateways per Region; to raise it, raise the quota for VPCs per Region. Only one egress-only internet gateway can be attached to a VPC at a time.
  scope: per Region, per account; default; adjustable; raised through the VPCs per Region quota.
  link: [5 egress-only internet gateways per Region](../facts/vpc.md#vpc-quota-egress-only-igw-per-region)
  link: [only one egress-only internet gateway to a VPC at a time](../facts/vpc.md#vpc-quota-egress-only-igw-per-region)
  say: five egress-only internet gateways per Region | one per VPC at a time
vpc-quota-eips-per-public-nat-gateway
  claim: A public NAT gateway can have 2 Elastic IP addresses by default; you can request a quota increase up to 8.
  scope: per public NAT gateway; default; adjustable; zonal NAT gateway (a regional NAT gateway supports up to 32 IP addresses per Availability Zone: vpc-regional-nat-ip-per-az).
  link: [2 Elastic IP addresses](../facts/vpc.md#vpc-quota-eips-per-public-nat-gateway)
  link: [up to 8](../facts/vpc.md#vpc-quota-eips-per-public-nat-gateway)
  say: two Elastic IP addresses by default | up to eight
vpc-quota-elastic-ips-per-region
  claim: The default quota is 5 Elastic IP addresses per Region; it is adjustable and applies to individual account VPCs and shared VPCs.
  scope: per Region, per account; default; adjustable.
  link: [5 Elastic IP addresses per Region](../facts/vpc.md#vpc-quota-elastic-ips-per-region)
  say: five Elastic IP addresses per Region
vpc-quota-enis-per-instance-varies
  claim: The number of network interfaces per instance varies by instance type and is not adjustable.
  scope: per EC2 instance; maximum; not adjustable; set by the instance type.
  link: [Varies by instance type](../facts/vpc.md#vpc-quota-enis-per-instance-varies)
  say: it depends on the instance type
vpc-quota-internet-gateways-per-region
  claim: The default quota is 5 internet gateways per Region; to raise it, raise the quota for VPCs per Region. Only one internet gateway can be attached to a VPC at a time.
  scope: per Region, per account; default; adjustable; raised through the VPCs per Region quota.
  link: [5 internet gateways per Region](../facts/vpc.md#vpc-quota-internet-gateways-per-region)
  link: [only one internet gateway to a VPC at a time](../facts/vpc.md#vpc-quota-internet-gateways-per-region)
  say: five internet gateways per Region | one internet gateway per VPC
vpc-quota-ipv4-cidr-blocks-per-vpc
  claim: The default quota is 5 IPv4 CIDR blocks per VPC, counting the primary and all secondary CIDR blocks; it is adjustable up to 50.
  scope: per VPC; default; adjustable; primary and secondary CIDR blocks both count.
  link: [5 IPv4 CIDR blocks per VPC](../facts/vpc.md#vpc-quota-ipv4-cidr-blocks-per-vpc)
  link: [up to 50](../facts/vpc.md#vpc-quota-ipv4-cidr-blocks-per-vpc)
  say: five IPv4 CIDR blocks per VPC | up to fifty
vpc-quota-ipv6-cidr-blocks-per-vpc
  claim: The default quota is 5 IPv6 CIDR blocks per VPC; it is adjustable up to 50.
  scope: per VPC; default; adjustable.
  link: [5 IPv6 CIDR blocks per VPC](../facts/vpc.md#vpc-quota-ipv6-cidr-blocks-per-vpc)
  link: [up to 50](../facts/vpc.md#vpc-quota-ipv6-cidr-blocks-per-vpc)
  say: five IPv6 CIDR blocks per VPC | up to fifty
vpc-quota-nat-gateways-per-az
  claim: The default quota is 5 NAT gateways per Availability Zone; it is adjustable. NAT gateways count toward the quota only in the pending, active, and deleting states.
  scope: per Availability Zone, per account; default; adjustable; counts gateways in the pending, active and deleting states.
  link: [5 NAT gateways per Availability Zone](../facts/vpc.md#vpc-quota-nat-gateways-per-az)
  say: five NAT gateways per Availability Zone
vpc-quota-nau-per-vpc
  claim: A VPC can have 64,000 NAU units (Network Address Usage) by default; the quota is adjustable up to 256,000.
  scope: per VPC; default; adjustable.
  link: [64,000 NAU units](../facts/vpc.md#vpc-quota-nau-per-vpc)
  link: [up to 256,000](../facts/vpc.md#vpc-quota-nau-per-vpc)
  say: sixty-four thousand NAU units per VPC | up to two hundred fifty-six thousand
vpc-quota-network-acls-per-vpc
  claim: The default quota is 200 network ACLs per VPC; it is adjustable. One network ACL can be associated with one or more subnets.
  scope: per VPC; default; adjustable.
  link: [200 network ACLs per VPC](../facts/vpc.md#vpc-quota-network-acls-per-vpc)
  say: two hundred network ACLs per VPC
vpc-quota-network-interfaces-per-region
  claim: The default quota is 5,000 network interfaces per Region, enforced per Availability Zone: with network interfaces in three AZs, each AZ has a limit of 5,000 and the Region a limit of 15,000.
  scope: per Region, per account; enforced per Availability Zone; default; adjustable; applies to individual account VPCs and shared VPCs.
  link: [5,000 network interfaces per Region](../facts/vpc.md#vpc-quota-network-interfaces-per-region)
  say: five thousand network interfaces per Region, enforced per Availability Zone
vpc-quota-peered-nau
  claim: A VPC and all of its intra-Region peered VPCs can have 128,000 NAU units combined by default; the quota is adjustable up to 512,000. VPCs peered across Regions do not count.
  scope: per VPC plus its intra-Region peered VPCs; default; adjustable; cross-Region peers do not count.
  link: [128,000 NAU units](../facts/vpc.md#vpc-quota-peered-nau)
  link: [up to 512,000](../facts/vpc.md#vpc-quota-peered-nau)
  say: one hundred twenty-eight thousand NAU units for the peered group | up to five hundred twelve thousand
vpc-quota-prefix-list-entries-counted-as-rules
  claim: A customer-managed prefix list can have up to 1,000 entries, and when a resource references a prefix list, its maximum number of entries counts against the entry quota of that resource: a prefix list with 20 maximum entries referenced in a security group rule counts as 20 security group rules.
  scope: per customer-managed prefix list; maximum; adjustable; the maximum entries of the list count against the referencing resource.
  link: [1,000](../facts/vpc.md#vpc-quota-prefix-list-entries-counted-as-rules)
  link: [this counts as 20 security group rules](../facts/vpc.md#vpc-quota-prefix-list-entries-counted-as-rules)
  say: one thousand entries | a twenty-entry list counts as twenty rules
vpc-quota-prefix-lists-per-region
  claim: The default quota is 100 customer-managed prefix lists per Region; it is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [100](../facts/vpc.md#vpc-quota-prefix-lists-per-region)
  say: one hundred prefix lists per Region
vpc-quota-private-ips-per-nat-gateway
  claim: A NAT gateway can have 8 private IP addresses by default; the quota is adjustable.
  scope: per NAT gateway; default; adjustable; zonal NAT gateway (a regional NAT gateway supports up to 32 IP addresses per Availability Zone: vpc-regional-nat-ip-per-az).
  link: [8 private IP addresses](../facts/vpc.md#vpc-quota-private-ips-per-nat-gateway)
  say: eight private IP addresses per NAT gateway
vpc-quota-propagated-routes-per-route-table
  claim: A route table can hold at most 100 propagated routes; this quota is not adjustable. If you need more prefixes, advertise a default route.
  scope: per route table; maximum; not adjustable; propagated routes only.
  link: [100 propagated routes](../facts/vpc.md#vpc-quota-propagated-routes-per-route-table)
  say: one hundred propagated routes, not adjustable
vpc-quota-route-tables-per-vpc
  claim: The default quota is 200 route tables per VPC, and the main route table counts toward it; it is adjustable. A subnet can be associated with only one route table.
  scope: per VPC; default; adjustable; the main route table counts.
  link: [200 route tables per VPC](../facts/vpc.md#vpc-quota-route-tables-per-vpc)
  link: [a subnet can only be associated with a single route table](../facts/vpc.md#vpc-quota-route-tables-per-vpc)
  say: two hundred route tables per VPC | one route table per subnet
vpc-quota-routes-per-route-table
  claim: The default quota is 500 routes per route table (non-propagated routes), enforced separately for IPv4 and IPv6 routes; it can be raised to a maximum of 1,000, but network performance might be impacted.
  scope: per route table; IPv4 and IPv6 routes counted separately; default; adjustable; non-propagated routes; maximum 1,000.
  link: [500 routes per route table](../facts/vpc.md#vpc-quota-routes-per-route-table)
  link: [up to a maximum of 1,000](../facts/vpc.md#vpc-quota-routes-per-route-table)
  say: five hundred routes per route table | up to one thousand
vpc-quota-rules-per-network-acl
  claim: The default quota is 20 rules per network ACL, which is the maximum for inbound rules and for outbound rules; it can be raised to at most 40 inbound rules and 40 outbound rules (80 in total), but network performance might be impacted.
  scope: per network ACL; default; adjustable; maximum 40 inbound and 40 outbound; performance might be impacted.
  link: [20 rules per network ACL](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  link: [40 inbound rules and 40 outbound rules](../facts/vpc.md#vpc-quota-rules-per-network-acl)
  say: twenty rules per network ACL | up to forty inbound and forty outbound
vpc-quota-rules-per-security-group
  claim: The default quota is 60 inbound or outbound rules per security group, enforced separately for inbound and outbound rules and separately for IPv4 and IPv6 rules: a security group can have 60 inbound rules and 60 outbound rules.
  scope: per security group; inbound and outbound counted separately; IPv4 and IPv6 counted separately; default; adjustable.
  link: [60 inbound or outbound rules per security group](../facts/vpc.md#vpc-quota-rules-per-security-group)
  link: [60 inbound rules and 60 outbound rules](../facts/vpc.md#vpc-quota-rules-per-security-group)
  say: sixty inbound and sixty outbound rules per security group
vpc-quota-security-groups-per-network-interface
  claim: The default quota is 5 security groups per network interface, adjustable up to 16; this quota multiplied by the quota for rules per security group cannot exceed 1,000.
  scope: per network interface; default; adjustable; security groups per interface times rules per group at most 1,000.
  link: [5 security groups per network interface](../facts/vpc.md#vpc-quota-security-groups-per-network-interface)
  link: [up to 16](../facts/vpc.md#vpc-quota-security-groups-per-network-interface)
  link: [cannot exceed 1,000](../facts/vpc.md#vpc-quota-security-groups-per-network-interface)
  say: five security groups per network interface | up to sixteen | groups times rules cannot exceed one thousand
vpc-quota-security-groups-per-region
  claim: The default quota is 2,500 VPC security groups per Region; it is adjustable and applies to individual account VPCs and shared VPCs.
  scope: per Region, per account; default; adjustable.
  link: [2,500 VPC security groups per Region](../facts/vpc.md#vpc-quota-security-groups-per-region)
  say: two thousand five hundred security groups per Region
vpc-quota-sharing-participant-accounts-per-vpc
  claim: The default quota is 100 distinct participant accounts that the subnets of one VPC can be shared with; it is adjustable and applies across all shared subnets of the VPC.
  scope: per VPC, across all shared subnets; default; adjustable.
  link: [100](../facts/vpc.md#vpc-quota-sharing-participant-accounts-per-vpc)
  say: one hundred participant accounts per VPC
vpc-quota-subnets-per-vpc
  claim: The default quota is 200 subnets per VPC; it is adjustable.
  scope: per VPC; default; adjustable.
  link: [200 subnets per VPC](../facts/vpc.md#vpc-quota-subnets-per-vpc)
  say: two hundred subnets per VPC
vpc-quota-subnets-shared-with-account
  claim: The default quota is 100 subnets that can be shared with one AWS account; it is adjustable.
  scope: per participant AWS account; default; adjustable.
  link: [100](../facts/vpc.md#vpc-quota-subnets-shared-with-account)
  say: one hundred subnets per account
vpc-quota-vpcs-per-region
  claim: The default quota is 5 VPCs per Region; it is adjustable, and raising it raises the quota for internet gateways per Region by the same amount.
  scope: per Region, per account; default; adjustable.
  link: [5 VPCs per Region](../facts/vpc.md#vpc-quota-vpcs-per-region)
  link: [increases the quota on internet gateways per Region by the same amount](../facts/vpc.md#vpc-quota-vpcs-per-region)
  say: five VPCs per Region by default | raising it also raises the internet gateway quota
vpc-reachability-analyzer-price-per-analysis
  claim: Reachability Analyzer is charged per analysis; in the pricing example the price per analysis processed is $0.10.
  scope: per analysis; example rate on the pricing page.
  link: [the price per analysis processed is $0.10](../facts/vpc.md#vpc-reachability-analyzer-price-per-analysis)
  say: ten cents per analysis
vpc-reachability-analyzer-static
  claim: Reachability Analyzer is a static configuration analysis tool that analyzes reachability between two resources in a VPC, giving hop-by-hop details of the virtual path when they are reachable and naming the blocking component when they are not.
  link: [Reachability Analyzer is a static configuration analysis tool](../facts/vpc.md#vpc-reachability-analyzer-static)
  link: [identifies the blocking component otherwise](../facts/vpc.md#vpc-reachability-analyzer-static)
  say: a static configuration analysis tool | it names the blocking component
vpc-regional-nat-expand-60-minutes
  claim: A regional NAT gateway can take up to 60 minutes to expand to a new Availability Zone after a resource appears there; until then that traffic is handled across zones by the gateway in an existing Availability Zone.
  scope: per regional NAT gateway.
  link: [up to 60 minutes](../facts/vpc.md#vpc-regional-nat-expand-60-minutes)
  say: up to sixty minutes
vpc-regional-nat-gateway-change
  claim: Regional NAT gateways were introduced on November 19, 2025: one NAT gateway that automatically expands across Availability Zones based on your workload footprint, instead of one zonal NAT gateway per Availability Zone.
  scope: per VPC.
  link: [November 19, 2025](../facts/vpc.md#vpc-regional-nat-gateway-change)
  link: [automatically expand across Availability Zones based on your workload footprint](../facts/vpc.md#vpc-regional-nat-gateway-change)
  say: November nineteenth, twenty twenty-five | expands across Availability Zones on its own as the workload grows
  changed: 2025-11-19: was operate in a single Availability Zone
vpc-regional-nat-ip-per-az
  claim: A regional NAT gateway supports up to 32 IP addresses per Availability Zone, compared with 8 for a zonal NAT gateway; each IP address increases the limit on concurrent connections to a popular destination, identified by a unique combination of destination IP, destination port and protocol, by 55,000.
  scope: per regional NAT gateway, per Availability Zone; maximum; not adjustable.
  link: [32 IP addresses per Availability Zone](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  link: [8 for zonal NAT gateways](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  link: [55,000](../facts/vpc.md#vpc-regional-nat-ip-per-az)
  say: thirty-two IP addresses per Availability Zone | eight for a zonal NAT gateway | fifty-five thousand connections per IP address
vpc-regional-nat-modes
  claim: A regional NAT gateway runs in automatic mode, where AWS automatically manages IP addresses and Availability Zone expansion (recommended), or in manual mode, where you are responsible for expanding and contracting the NAT gateway across Availability Zones.
  scope: per regional NAT gateway.
  link: [AWS automatically manages IP addresses and Availability Zone expansion](../facts/vpc.md#vpc-regional-nat-modes)
  link: [you are responsible for expanding and contracting your NAT gateway across Availability Zones](../facts/vpc.md#vpc-regional-nat-modes)
  say: automatic mode: AWS manages addresses and zone expansion | manual mode: you expand and contract it yourself
vpc-regional-nat-no-private-nat
  claim: Regional NAT gateways do not support private NAT and are not supported in constrained Availability Zones; for private NAT use a zonal NAT gateway.
  scope: per regional NAT gateway.
  link: [do not support private NAT](../facts/vpc.md#vpc-regional-nat-no-private-nat)
  say: no private NAT; use a zonal NAT gateway for that
vpc-regional-natgw-billed-per-az-hour
  claim: A Regional NAT gateway is charged for each hour that it is configured in each Availability Zone: running across three Availability Zones for one hour bills three NAT Gateway-hours, and billing stops for an AZ when the gateway removes support from it.
  scope: per Regional NAT gateway, per Availability Zone.
  link: [charged for each hour that the NAT Gateway is configured in each availability zone](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
  link: [three 'NAT Gateway-hours'](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
  link: [billing automatically adjusts](../facts/vpc.md#vpc-regional-natgw-billed-per-az-hour)
vpc-regional-natgw-example-total-charge
  claim: In the Regional NAT gateway pricing example, where a gateway spans three Availability Zones and one instance sends a 1 GB file to the internet, the total charge is $0.27: $0.135 hourly NAT gateway usage, $0.045 data processing and $0.09 Data Transfer Out.
  scope: one worked example, US East (Ohio); 1 GB to the internet, three Availability Zones, one hour.
  link: [a total charge of $0.27](../facts/vpc.md#vpc-regional-natgw-example-total-charge)
  say: twenty-seven cents in total
vpc-regional-natgw-no-public-subnet
  claim: A regional NAT gateway is a standalone resource with its own route table and does not need a public subnet to host it; it uses a single NAT ID across all Availability Zones that have network interfaces, so subnets in different Availability Zones can use the same route entry.
  link: [you don't need to create a public subnet to host it](../facts/vpc.md#vpc-regional-natgw-no-public-subnet)
  link: [Use a single NAT ID across all Availability Zones that have network interfaces](../facts/vpc.md#vpc-regional-natgw-no-public-subnet)
vpc-regional-natgw-price-example-three-azs
  claim: In the US East (Ohio) pricing example, a Regional NAT gateway costs $0.045 per hour per Availability Zone, so across three Availability Zones the hourly charge is $0.135 per hour.
  scope: per Regional NAT gateway, per Availability Zone, US East (Ohio); example rates on the pricing page; data processing is charged on top.
  link: [$0.045 per hour per AZ](../facts/vpc.md#vpc-regional-natgw-price-example-three-azs)
  link: [$0.135 per hour](../facts/vpc.md#vpc-regional-natgw-price-example-three-azs)
  say: four and a half cents per hour per Availability Zone | thirteen and a half cents per hour for three zones
vpc-regional-natgw-vs-zonal
  claim: A standard (zonal) NAT gateway operates in a single Availability Zone; a regional NAT gateway automatically expands across Availability Zones as workloads appear there and contracts when a zone has no active workloads.
  link: [which operate in a single Availability Zone](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
  link: [regional NAT gateways follow your workloads to provide automatic high availability](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
  link: [automatically expands across Availability Zones based on your workload presence](../facts/vpc.md#vpc-regional-natgw-vs-zonal)
vpc-regional-natgw-when-to-use
  claim: AWS suggests regional NAT gateways for all use cases except private connectivity: regional NAT gateways do not support private NAT, so private NAT use cases keep zonal NAT gateways.
  link: [Consider using Regional NAT Gateways for all use cases except those that require private connectivity](../facts/vpc.md#vpc-regional-natgw-when-to-use)
  link: [Regional NAT gateways do not support private NAT](../facts/vpc.md#vpc-regional-natgw-when-to-use)
vpc-resilience-azs-fail-over
  claim: AWS Regions provide multiple physically separated and isolated Availability Zones connected by low-latency, high-throughput, highly redundant networking, so applications can fail over between zones without interruption.
  link: [multiple physically separated and isolated Availability Zones](../facts/vpc.md#vpc-resilience-azs-fail-over)
  link: [automatically fail over between zones without interruption](../facts/vpc.md#vpc-resilience-azs-fail-over)
  say: separate, isolated Availability Zones
vpc-resource-map-shows-relationships
  claim: The VPC resource map shows relationships between resources inside a VPC and how traffic flows from subnets to NAT gateways, the internet gateway and gateway endpoints.
  link: [how traffic flows from subnets to NAT gateways, internet gateway and gateway endpoints](../facts/vpc.md#vpc-resource-map-shows-relationships)
  say: it shows how traffic flows
vpc-rfc1918-ten-range-example
  claim: The RFC 1918 range 10.0.0.0 to 10.255.255.255 (the 10/8 prefix) is a recommended private source for a VPC CIDR; 10.0.0.0/16 is the example block.
  link: [10.0.0.0 - 10.255.255.255 (10/8 prefix)](../facts/vpc.md#vpc-rfc1918-ten-range-example)
  link: [10.0.0.0/16](../facts/vpc.md#vpc-rfc1918-ten-range-example)
vpc-route-longest-prefix-match
  claim: When several routes match, the VPC uses the most specific route, the longest prefix match, to decide where to send the traffic.
  scope: per route table.
  link: [we use the most specific route that matches the traffic (longest prefix match)](../facts/vpc.md#vpc-route-longest-prefix-match)
  link: [longest prefix match](../facts/vpc.md#vpc-route-longest-prefix-match)
  say: the most specific route wins
vpc-route-more-specific-than-local
  claim: You can add a route more specific than the local route, but its destination must match the entire CIDR block of a subnet in the VPC and its target must be a NAT gateway, a network interface or a Gateway Load Balancer endpoint.
  scope: per route table; middlebox routing.
  link: [add a route to your route tables that is more specific than the local route](../facts/vpc.md#vpc-route-more-specific-than-local)
  link: [The target must be a NAT gateway, network interface, or Gateway Load Balancer endpoint](../facts/vpc.md#vpc-route-more-specific-than-local)
  link: [The destination must match the entire IPv4 or IPv6 CIDR block of a subnet in your VPC](../facts/vpc.md#vpc-route-more-specific-than-local)
  say: a more specific route than local is allowed
vpc-route-propagation-from-vgw
  claim: With a virtual private gateway attached and route propagation enabled on a subnet route table, the routes for the Site-to-Site VPN connection appear automatically as propagated routes, so you do not add or remove VPN routes by hand.
  scope: per route table; a virtual private gateway is attached and route propagation is enabled.
  link: [routes representing your Site-to-Site VPN connection automatically appear as propagated routes in your route table](../facts/vpc.md#vpc-route-propagation-from-vgw)
  link: [you don't need to manually add or remove VPN routes](../facts/vpc.md#vpc-route-propagation-from-vgw)
  say: VPN routes show up automatically as propagated routes
vpc-route-server-change
  claim: Amazon VPC Route Server (in the VPC guide since March 31, 2025) dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for workloads, so you can automatically reroute traffic within a VPC.
  scope: per VPC.
  link: [March 31, 2025](../facts/vpc.md#vpc-route-server-change)
  link: [dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes](../facts/vpc.md#vpc-route-server-change)
  say: March thirty-first, twenty twenty-five | dynamic route updates inside a VPC for routing fault tolerance
vpc-route-static-beats-propagated
  claim: If the destination of a propagated route is identical to the destination of a static route, the static route takes priority.
  scope: per route table; identical destinations.
  link: [If the destination of a propagated route is identical to the destination of a static route, the static route takes priority](../facts/vpc.md#vpc-route-static-beats-propagated)
  link: [the static route takes priority](../facts/vpc.md#vpc-route-static-beats-propagated)
  say: the static route wins over the propagated one
vpc-route-table-implicit-main-association
  claim: Every subnet must be associated with a route table; a subnet you do not explicitly associate is implicitly associated with the main route table, a subnet can be associated with only one route table at a time, and many subnets can share one route table.
  scope: per subnet; maximum.
  link: [the subnet is implicitly associated with the main route table](../facts/vpc.md#vpc-route-table-implicit-main-association)
  link: [A subnet can only be associated with one route table at a time](../facts/vpc.md#vpc-route-table-implicit-main-association)
  link: [associate multiple subnets with the same subnet route table](../facts/vpc.md#vpc-route-table-implicit-main-association)
  say: no explicit choice means the main route table | one route table per subnet | one route table can serve many subnets
vpc-route-target-types
  claim: Each route names a destination (the IP range the traffic is going to) and a target (the gateway, network interface or connection that carries it, for example an internet gateway).
  scope: per route.
  link: [The range of IP addresses where you want traffic to go (destination CIDR)](../facts/vpc.md#vpc-route-target-types)
  link: [The gateway, network interface, or connection through which to send the destination traffic](../facts/vpc.md#vpc-route-target-types)
  say: destination is where the traffic goes | target is what carries it
vpc-routes-per-route-table-default-500
  claim: Since June 23, 2025 a route table holds 500 non-propagated routes by default, up from 50; the quota can be raised to a maximum of 1,000, and propagated routes are limited to 100 per route table.
  scope: per route table; default; adjustable; enforced separately for IPv4 and IPv6 routes.
  link: [500](../facts/vpc.md#vpc-routes-per-route-table-default-500)
  link: [from 50 to 500 entries](../facts/vpc.md#vpc-routes-per-route-table-default-500)
  link: [maximum of 1,000](../facts/vpc.md#vpc-routes-per-route-table-default-500)
  link: [100](../facts/vpc.md#vpc-routes-per-route-table-default-500)
  say: five hundred routes per route table by default | it used to be fifty | up to one thousand on request | one hundred propagated routes
  changed: 2025-06-23: was 50
vpc-secondary-cidr-adds-local-route
  claim: When you associate a CIDR block with a VPC, a local route for that block is added automatically to the VPC route tables so that traffic can be routed within the VPC.
  scope: per VPC.
  link: [a route is automatically added to your VPC route tables to enable routing within the VPC](../facts/vpc.md#vpc-secondary-cidr-adds-local-route)
  link: [the destination is the CIDR block and the target is `local`](../facts/vpc.md#vpc-secondary-cidr-adds-local-route)
  say: a local route is added automatically
vpc-secondary-cidr-restrictions-10-range
  claim: When a VPC's existing IPv4 range is in 10.0.0.0/8, you cannot associate a secondary CIDR block from the other RFC 1918 ranges (172.16.0.0/12 and 192.168.0.0/16) or from 198.19.0.0/16, and if any associated block is from 10.0.0.0/15 you cannot add a block from 10.0.0.0/16; you can add any other block from 10.0.0.0/8 that is not restricted, a publicly routable block, or a block from 100.64.0.0/10, each between a /16 netmask and a /28 netmask.
  scope: per VPC, secondary IPv4 CIDR association; existing range in 10.0.0.0/8; other rows of the same table cover 172.16.0.0/12, 192.168.0.0/16, 198.19.0.0/16 and publicly routable ranges.
  link: [CIDR blocks from other RFC 1918 ranges (172.16.0.0/12 and 192.168.0.0/16)](../facts/vpc.md#vpc-secondary-cidr-restrictions-10-range)
  link: [100.64.0.0/10](../facts/vpc.md#vpc-secondary-cidr-restrictions-10-range)
  say: not the other private ranges, one seventy-two sixteen or one ninety-two one sixty-eight | one hundred dot sixty-four slash ten is allowed
vpc-secondary-cidr-vs-existing-routes
  claim: A new VPC CIDR block must not be the same as or larger than the destination of any route already in the VPC's route tables.
  scope: per VPC; adding an IPv4 CIDR block.
  link: [must not be the same or larger than a destination CIDR range in a route in any of the VPC route tables](../facts/vpc.md#vpc-secondary-cidr-vs-existing-routes)
  say: it cannot cover an existing route destination
vpc-security-best-practice-multi-az-subnets
  claim: The VPC security best practices say to create subnets in multiple Availability Zones, use security groups for instance traffic, network ACLs for subnet-level traffic, and VPC Flow Logs to monitor IP traffic.
  link: [create them in multiple Availability Zones](../facts/vpc.md#vpc-security-best-practice-multi-az-subnets)
  link: [Use security groups to control traffic to EC2 instances in your subnets](../facts/vpc.md#vpc-security-best-practice-multi-az-subnets)
  link: [Use network ACLs to control inbound and outbound traffic at the subnet level](../facts/vpc.md#vpc-security-best-practice-multi-az-subnets)
  link: [Use VPC Flow Logs to monitor the IP traffic going to and from a VPC, subnet, or network interface](../facts/vpc.md#vpc-security-best-practice-multi-az-subnets)
vpc-security-group-assoc-rules
  claim: A security group VPC association requires the VPC and the security group to be in the same AWS Region; a default security group cannot be associated with another VPC, and a security group cannot be associated with a default VPC.
  scope: per security group VPC association.
  link: [must be in the same AWS Region](../facts/vpc.md#vpc-security-group-assoc-rules)
  link: [cannot associate a default security group with another VPC or associate a security group with a default VPC](../facts/vpc.md#vpc-security-group-assoc-rules)
  say: same Region only | default security groups and default VPCs are excluded
vpc-security-group-multi-vpc-change
  claim: Since October 30, 2024 the Security Group VPC Associations feature lets you associate a security group with multiple VPCs in the same Region, so you can manage security groups in one place for multiple VPCs in your account.
  scope: per security group, same Region.
  link: [October 30, 2024](../facts/vpc.md#vpc-security-group-multi-vpc-change)
  link: [associate a security group with multiple VPCs in the same Region](../facts/vpc.md#vpc-security-group-multi-vpc-change)
  say: October thirtieth, twenty twenty-four | one security group, several VPCs in the same Region
vpc-security-group-sharing-change
  claim: Since October 30, 2024 the Shared Security Group feature lets you share a security group with other AWS Organizations accounts in the same AWS Region, so those accounts can use it; the account that shares the security group must own both the VPC and the security group.
  scope: per security group, accounts in one AWS Organization, same Region.
  link: [October 30, 2024](../facts/vpc.md#vpc-security-group-sharing-change)
  link: [share a security group with other AWS Organizations accounts within the same AWS Region](../facts/vpc.md#vpc-security-group-sharing-change)
  say: October thirtieth, twenty twenty-four | share a security group with other accounts in the organization, same Region
vpc-security-group-sharing-defaults-excluded
  claim: You cannot share default security groups, and you cannot share security groups that are in a default VPC.
  scope: per shared security group.
  link: [cannot share default security groups](../facts/vpc.md#vpc-security-group-sharing-defaults-excluded)
  say: default security groups cannot be shared
vpc-security-groups-for-many-resource-types
  claim: The security groups you create for a VPC control traffic to and from the associated resources, such as compute resources, database resources and load balancers, while each subnet has a network ACL that controls traffic entering and leaving the subnet.
  link: [such as compute resources, database resources, and load balancers](../facts/vpc.md#vpc-security-groups-for-many-resource-types)
  say: compute, database and load balancer resources
vpc-sg-allow-rules-only
  claim: A security group holds allow rules only; it cannot hold deny rules. A network ACL can hold both allow and deny rules.
  scope: per security group.
  link: [You can specify allow rules, but not deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
  link: [Network ACLs can be used to set both Allow and Deny rules](../facts/vpc.md#vpc-sg-allow-rules-only)
vpc-sg-chain-db-allows-web-sg
  claim: In the guide's web and database example, the database security group allows inbound MySQL on TCP 3306 only from the web server security group, by referencing that group's ID as the source.
  link: [Allows inbound MySQL Server access from the web servers](../facts/vpc.md#vpc-sg-chain-db-allows-web-sg)
  link: [ID of the web server security group](../facts/vpc.md#vpc-sg-chain-db-allows-web-sg)
vpc-sg-chain-web-allows-lb-sg
  claim: In the guide's web and database example, the web server security group allows inbound HTTPS on TCP 443 only from the load balancer's security group.
  link: [Allows inbound HTTPS access from the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
  link: [ID of the security group for the load balancer](../facts/vpc.md#vpc-sg-chain-web-allows-lb-sg)
vpc-sg-changes-apply-automatically
  claim: When you add, update or remove security group rules, the changes are automatically applied to all resources associated with the security group.
  link: [your changes are automatically applied to all resources associated with the security group](../facts/vpc.md#vpc-sg-changes-apply-automatically)
  say: changes apply to every associated resource automatically
vpc-sg-connection-tracking-stateful
  claim: Security groups use connection tracking, which makes them stateful: responses to inbound traffic may leave the instance regardless of the outbound rules, and the reverse.
  link: [security groups are stateful](../facts/vpc.md#vpc-sg-connection-tracking-stateful)
  link: [responses to inbound traffic are allowed to flow out of the instance regardless of outbound security group rules, and vice versa](../facts/vpc.md#vpc-sg-connection-tracking-stateful)
  say: security groups are stateful
vpc-sg-multiple-groups-rules-aggregated
  claim: You can assign several security groups to one resource; their rules are aggregated into a single set of rules that decides whether to allow access.
  link: [assign multiple security groups to a single resource](../facts/vpc.md#vpc-sg-multiple-groups-rules-aggregated)
  link: [aggregated to form a single set of rules](../facts/vpc.md#vpc-sg-multiple-groups-rules-aggregated)
  say: several security groups on one resource | the rules are added together
vpc-sg-name-description-immutable
  claim: You cannot change the name and description of a security group after it is created.
  link: [You can't change the name and description of a security group after it is created](../facts/vpc.md#vpc-sg-name-description-immutable)
  say: name and description are fixed
vpc-sg-new-no-inbound-rules
  claim: A newly created security group has no inbound rules, so no inbound traffic is allowed until you add inbound rules.
  scope: per new security group; default; not adjustable.
  link: [it has no inbound rules](../facts/vpc.md#vpc-sg-new-no-inbound-rules)
  link: [no inbound traffic is allowed until you add inbound rules to the security group](../facts/vpc.md#vpc-sg-new-no-inbound-rules)
  say: no inbound rules at first
vpc-sg-new-outbound-allow-all
  claim: A newly created security group has one outbound rule that allows all outbound traffic; you can remove it, and a security group with no outbound rules allows no outbound traffic.
  scope: per new security group; default; not adjustable.
  link: [an outbound rule that allows all outbound traffic from the resource](../facts/vpc.md#vpc-sg-new-outbound-allow-all)
  link: [If your security group has no outbound rules, no outbound traffic is allowed](../facts/vpc.md#vpc-sg-new-outbound-allow-all)
  say: one outbound rule that allows everything
vpc-sg-no-charge
  claim: There is no additional charge for using security groups.
  link: [There is no additional charge for using security groups](../facts/vpc.md#vpc-sg-no-charge)
  say: security groups cost nothing extra
vpc-sg-not-filter-amazon-services
  claim: Security groups do not filter traffic to and from a set of Amazon-provided services that the VPC guide lists, among them Amazon DNS, Amazon DHCP, EC2 instance metadata, Windows license activation, Amazon Time Sync Service and the reserved IP addresses of the default VPC router.
  link: [Security groups do not filter traffic destined to and from the following](../facts/vpc.md#vpc-sg-not-filter-amazon-services)
  say: security groups do not filter some Amazon service traffic
vpc-sg-primary-nacl-secondary
  claim: Security groups are the more versatile control because they filter statefully and can reference other security groups; network ACLs serve as a secondary control, for example to deny a subset of traffic, or as subnet-level guard rails.
  link: [Security groups are more versatile than network ACLs](../facts/vpc.md#vpc-sg-primary-nacl-secondary)
  link: [Network ACLs can be effective as a secondary control (for example, to deny a specific subset of traffic) or as high-level subnet guard rails](../facts/vpc.md#vpc-sg-primary-nacl-secondary)
vpc-sg-reference-across-peering-and-tgw
  claim: You can reference a security group in an inbound rule of another security group when both are associated with the same VPC, or with VPCs joined by a peering connection or a transit gateway; outbound references work for the same VPC or a peering connection.
  link: [You can reference a security group in the inbound rule of another security group if any of the following is true](../facts/vpc.md#vpc-sg-reference-across-peering-and-tgw)
  link: [You can reference a security group in the outbound rule if any of the following is true](../facts/vpc.md#vpc-sg-reference-across-peering-and-tgw)
vpc-sg-reference-no-rules-copied
  claim: Referencing a security group in a rule does not add any rules from the referenced security group to the security group that references it.
  link: [No rules from the referenced security group are added to the security group that references it](../facts/vpc.md#vpc-sg-reference-no-rules-copied)
  say: no rules are copied
vpc-sg-reference-sg-private-ips
  claim: When a security group is the source or destination of a rule, the rule affects all instances associated with that security group, and they communicate over the private IP addresses of the instances.
  link: [the rule affects all instances that are associated with the security groups](../facts/vpc.md#vpc-sg-reference-sg-private-ips)
  link: [using the private IP addresses of the instances](../facts/vpc.md#vpc-sg-reference-sg-private-ips)
  say: the rule covers every instance in the referenced group
vpc-sg-rule-change-tracked-connections-continue
  claim: When you change a security group rule, its tracked connections are not immediately interrupted: the security group keeps allowing packets until existing connections time out; to interrupt traffic immediately you can use a network ACL, and adding a network ACL that blocks traffic breaks existing connections.
  link: [its tracked connections are not immediately interrupted](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  link: [continues to allow packets until existing connections time out](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  link: [you can use a network ACL for your subnet](../facts/vpc.md#vpc-sg-rule-change-tracked-connections-continue)
  say: existing tracked connections keep working | use a network ACL to cut traffic at once
vpc-sg-rule-counts-toward-quota
  claim: A rule that references a CIDR block or another security group counts as one rule; a rule that references a customer-managed prefix list counts as the maximum size of the prefix list, and one that references an AWS-managed prefix list counts as its weight.
  scope: per security group rule.
  link: [A rule that references a CIDR block counts as one rule](../facts/vpc.md#vpc-sg-rule-counts-toward-quota)
  link: [counts as one rule, no matter the size of the referenced security group](../facts/vpc.md#vpc-sg-rule-counts-toward-quota)
  link: [counts as the maximum size of the prefix list](../facts/vpc.md#vpc-sg-rule-counts-toward-quota)
  link: [counts as the weight of the prefix list](../facts/vpc.md#vpc-sg-rule-counts-toward-quota)
  say: a customer-managed prefix list counts as its maximum size
vpc-sg-rule-source-type-immutable
  claim: When you update a security group rule you can change its protocol, description and source, but not the source type; for example an IPv4 CIDR source cannot become an IPv6 CIDR block, a prefix list or a security group.
  link: [you can't change the source type](../facts/vpc.md#vpc-sg-rule-source-type-immutable)
  say: the source type is fixed
vpc-sg-rule-sources
  claim: The source or destination of a security group rule can be a single IPv4 or IPv6 address, an IPv4 or IPv6 CIDR range, the ID of a prefix list, or the ID of a security group.
  link: [The ID of a prefix list](../facts/vpc.md#vpc-sg-rule-sources)
  link: [The ID of a security group](../facts/vpc.md#vpc-sg-rule-sources)
  link: [A range of IPv4 addresses, in CIDR block notation](../facts/vpc.md#vpc-sg-rule-sources)
  say: another security group
vpc-sg-stale-rule-peer-deleted
  claim: A security group rule that references a security group in a peer VPC or shared VPC is marked as stale when the referenced security group or the VPC peering connection is deleted.
  link: [the rule is marked as stale](../facts/vpc.md#vpc-sg-stale-rule-peer-deleted)
  say: the rule becomes stale
vpc-sg-untracked-flow-cut-immediately
  claim: Not all security group flows are tracked, and an untracked flow is interrupted immediately when the rule that enables it is removed or modified, unlike a tracked connection.
  link: [Not all flows of traffic are tracked](../facts/vpc.md#vpc-sg-untracked-flow-cut-immediately)
  link: [An untracked flow of traffic is immediately interrupted if the rule that enables the flow is removed or modified](../facts/vpc.md#vpc-sg-untracked-flow-cut-immediately)
  say: an untracked flow is cut at once
vpc-sg-vs-nacl-level
  claim: A security group operates at the instance level; a network ACL operates at the subnet level.
  link: [Instance level](../facts/vpc.md#vpc-sg-vs-nacl-level)
  link: [Subnet level](../facts/vpc.md#vpc-sg-vs-nacl-level)
vpc-sg-vs-nacl-return-traffic
  claim: In a security group return traffic is automatically allowed (stateful); in a network ACL return traffic must be explicitly allowed (stateless).
  link: [Automatically allowed (stateful)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic)
  link: [Must be explicitly allowed (stateless)](../facts/vpc.md#vpc-sg-vs-nacl-return-traffic)
vpc-sg-vs-nacl-rule-evaluation
  claim: A security group evaluates all rules before deciding whether to allow traffic; a network ACL evaluates rules in ascending order until a match is found.
  link: [Evaluates all rules before deciding whether to allow traffic](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation)
  link: [Evaluates rules in ascending order until a match for the traffic is found](../facts/vpc.md#vpc-sg-vs-nacl-rule-evaluation)
vpc-sg-vs-nacl-rule-type
  claim: A security group supports allow rules only; a network ACL supports allow and deny rules.
  link: [Allow rules only](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
  link: [Allow and deny rules](../facts/vpc.md#vpc-sg-vs-nacl-rule-type)
vpc-sg-vs-nacl-scope
  claim: A security group applies to all instances associated with it; a network ACL applies to all instances in the associated subnets.
  link: [Applies to all instances associated with the security group](../facts/vpc.md#vpc-sg-vs-nacl-scope)
  link: [Applies to all instances in the associated subnets](../facts/vpc.md#vpc-sg-vs-nacl-scope)
vpc-sharing-no-default-vpc-subnets
  claim: VPC owners can share subnets only with accounts or organizational units in the same organization, and cannot share subnets that are in a default VPC.
  link: [VPC owners can share subnets only with other accounts or organizational units that are in the same organization from AWS Organizations](../facts/vpc.md#vpc-sharing-no-default-vpc-subnets)
  link: [VPC owners can't share subnets that are in a default VPC](../facts/vpc.md#vpc-sharing-no-default-vpc-subnets)
  say: same organization only | not from a default VPC
vpc-sharing-owner-manages-network-resources
  claim: The VPC owner creates, manages and deletes the network resources of a shared VPC, such as subnets, route tables, network ACLs, gateways, endpoints and transit gateway attachments; participants can create a limited set, such as network interfaces and security groups.
  link: [VPC owners are responsible for creating, managing, and deleting the resources associated with a shared VPC](../facts/vpc.md#vpc-sharing-owner-manages-network-resources)
  link: [participants can create network interfaces and security groups](../facts/vpc.md#vpc-sharing-owner-manages-network-resources)
  say: the owner manages the network
vpc-sharing-owner-pays-nat-endpoints-ipv4
  claim: In a shared VPC, the VPC owner pays the hourly, data processing and data transfer charges of NAT gateways, virtual private gateways, transit gateways, AWS PrivateLink and VPC endpoints, and the public IPv4 addresses used in the shared VPC are billed to the owner.
  link: [VPC owners pay hourly charges (where applicable), data processing and data transfer charges across NAT gateways](../facts/vpc.md#vpc-sharing-owner-pays-nat-endpoints-ipv4)
  link: [public IPv4 addresses used in shared VPCs are billed to VPC owners](../facts/vpc.md#vpc-sharing-owner-pays-nat-endpoints-ipv4)
  say: the owner pays for NAT gateways and endpoints
vpc-sharing-owner-shares-subnets-same-org
  claim: With VPC subnet sharing, the account that owns the VPC shares one or more subnets with participant accounts in the same organization in AWS Organizations; participants can then create, modify and delete their own application resources in those subnets.
  link: [the account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong to the same organization from AWS Organizations](../facts/vpc.md#vpc-sharing-owner-shares-subnets-same-org)
  link: [the participants can view, create, modify, and delete their application resources in the subnets shared with them](../facts/vpc.md#vpc-sharing-owner-shares-subnets-same-org)
  say: the owner shares subnets with accounts in the same organization
vpc-sharing-participant-no-default-sg
  claim: Participants cannot launch instances with the default security group of a shared VPC, because it belongs to the owner.
  link: [Participants can't launch instances using the default security group for the VPC because it belongs to the owner](../facts/vpc.md#vpc-sharing-participant-no-default-sg)
  say: not the default security group
vpc-sharing-participant-pays-resources
  claim: In a shared VPC, each participant pays for its own application resources and for data transfer across Availability Zones, VPC peering connections, internet gateways and Direct Connect gateways.
  link: [each participant pays for their application resources](../facts/vpc.md#vpc-sharing-participant-pays-resources)
  say: participants pay for their own resources
vpc-sharing-participants-cannot-modify-vpc-subnets
  claim: Participants in a shared VPC cannot modify the VPC, the shared subnets or their attributes; only the VPC owner can.
  link: [Participants cannot modify shared subnets or their related attributes](../facts/vpc.md#vpc-sharing-participants-cannot-modify-vpc-subnets)
  link: [Participants cannot modify VPCs or their related attributes](../facts/vpc.md#vpc-sharing-participants-cannot-modify-vpc-subnets)
  link: [Only the VPC owner can](../facts/vpc.md#vpc-sharing-participants-cannot-modify-vpc-subnets)
  say: participants cannot change shared subnets
vpc-sharing-same-az-transfer-free
  claim: Data transfer within the same Availability Zone, identified by AZ ID, is free whichever accounts own the communicating resources.
  link: [is free irrespective of account ownership of the communicating resources](../facts/vpc.md#vpc-sharing-same-az-transfer-free)
  say: same-AZ transfer is free
vpc-size-ipv4-vs-ipv6-cidrs
  claim: A VPC can have up to 5 IPv4 CIDRs, each from /16 to /28, and up to 5 IPv6 CIDRs from /44 to /60 in increments of /4; both quotas are adjustable.
  scope: per VPC; default; adjustable; the CIDR count quota is adjustable.
  link: [Up to 5 CIDRs from /16 to /28](../facts/vpc.md#vpc-size-ipv4-vs-ipv6-cidrs)
  link: [Up to 5 CIDRs from /44 to /60 in increments of /4](../facts/vpc.md#vpc-size-ipv4-vs-ipv6-cidrs)
  say: up to five IPv4 CIDRs, slash sixteen to slash twenty-eight | up to five IPv6 CIDRs, slash forty-four to slash sixty
vpc-spans-all-azs-in-region
  claim: A VPC spans all of the Availability Zones in its Region, and you can add one or more subnets in each Availability Zone.
  scope: per VPC.
  link: [spans all of the Availability Zones in a Region](../facts/vpc.md#vpc-spans-all-azs-in-region)
  link: [one or more subnets in each Availability Zone](../facts/vpc.md#vpc-spans-all-azs-in-region)
  say: spans every Availability Zone in the Region
vpc-subnet-24-usable-251
  claim: A /24 subnet has 256 IP addresses, of which 251 can be assigned to resources, because five addresses are reserved.
  scope: per /24 IPv4 subnet; fixed; not adjustable; not for BYOIP ranges, where every address can be used.
  link: [251 can be assigned to resources](../facts/vpc.md#vpc-subnet-24-usable-251)
  say: two hundred fifty-one usable addresses
vpc-subnet-byoip-all-addresses-usable
  claim: For an IPv4 range brought to AWS with BYOIP, you can use every address in the range, including the first (network) address and the last (broadcast) address.
  scope: per BYOIP IPv4 range; only for BYOIP ranges.
  link: [you can use all of the IP addresses in the range](../facts/vpc.md#vpc-subnet-byoip-all-addresses-usable)
  say: every address in a BYOIP range can be used
vpc-subnet-cidr-reservation-definition
  claim: A subnet CIDR reservation is a range of IPv4 or IPv6 addresses in a subnet that AWS will not assign to network interfaces, so you can use it for prefixes or explicit addresses on network interfaces.
  link: [a range of IPv4 or IPv6 addresses that you set aside so that AWS won't assign them to your network interfaces](../facts/vpc.md#vpc-subnet-cidr-reservation-definition)
  say: addresses AWS will not assign
vpc-subnet-cidr-reservation-keeps-used-ips
  claim: Creating or deleting a subnet CIDR reservation does not unassign IP addresses that are already in use.
  link: [Creating a subnet reservation does not unassign any IP addresses that are already in use](../facts/vpc.md#vpc-subnet-cidr-reservation-keeps-used-ips)
  link: [Deleting a subnet reservation does not unassign any IP addresses that are in use](../facts/vpc.md#vpc-subnet-cidr-reservation-keeps-used-ips)
vpc-subnet-cidr-same-or-subset-of-vpc
  claim: A subnet CIDR block is either the same as the VPC CIDR block (one subnet for the whole VPC) or a subset of it (several subnets).
  scope: per subnet.
  link: [the same as the CIDR block for the VPC](../facts/vpc.md#vpc-subnet-cidr-same-or-subset-of-vpc)
  say: the same as the VPC range or a part of it
vpc-subnet-cidrs-cannot-overlap
  claim: When a VPC has more than one subnet, the CIDR blocks of the subnets cannot overlap.
  scope: per VPC.
  link: [the CIDR blocks of the subnets cannot overlap](../facts/vpc.md#vpc-subnet-cidrs-cannot-overlap)
  say: subnet ranges cannot overlap
vpc-subnet-definition
  claim: A subnet is a range of IP addresses in your VPC; you launch AWS resources such as EC2 instances into subnets and route their traffic with route tables.
  scope: per subnet.
  link: [a range of IP addresses in your VPC](../facts/vpc.md#vpc-subnet-definition)
  link: [launch AWS resources, such as Amazon EC2 instances, into your subnets](../facts/vpc.md#vpc-subnet-definition)
  say: a range of IP addresses inside the VPC
vpc-subnet-ip-attribute-override-at-launch
  claim: The subnet's auto-assign IP attribute decides whether a new network interface in that subnet gets a public IPv4 address (and, if applicable, an IPv6 address), but you can override it for a specific instance at launch.
  scope: per subnet.
  link: [a modifiable attribute that determines whether a network interface created in that subnet is assigned a public IPv4 address](../facts/vpc.md#vpc-subnet-ip-attribute-override-at-launch)
  link: [you can still override this setting for a specific instance during launch](../facts/vpc.md#vpc-subnet-ip-attribute-override-at-launch)
  say: you can override it per instance at launch
vpc-subnet-ipv6-attribute-default-false
  claim: By default all subnets have the IPv6 addressing attribute set to false; when you enable it, network interfaces created in the subnet receive an IPv6 address from the subnet's range, and the subnet must have an associated IPv6 CIDR block.
  scope: per subnet; default; adjustable; the subnet must have an associated IPv6 CIDR block.
  link: [all subnets have the IPv6 addressing attribute set to `false`](../facts/vpc.md#vpc-subnet-ipv6-attribute-default-false)
  link: [network interfaces created in the subnet receive an IPv6 address from the range of the subnet](../facts/vpc.md#vpc-subnet-ipv6-attribute-default-false)
  say: auto-assign IPv6 is off by default
vpc-subnet-ipv6-five-reserved
  claim: In an IPv6 subnet the first four IPv6 addresses and the last IPv6 address of the subnet CIDR block are reserved and cannot be assigned to an EC2 instance.
  scope: per IPv6 subnet CIDR block; fixed.
  link: [The first four IPv6 addresses and the last IPv6 address](../facts/vpc.md#vpc-subnet-ipv6-five-reserved)
  say: the first four and the last IPv6 address
vpc-subnet-one-az-protects-from-zone-failure
  claim: Each subnet lives entirely in one Availability Zone and cannot span zones; launching resources in separate Availability Zones protects an application from the failure of a single zone.
  link: [Each subnet must reside entirely within one Availability Zone and cannot span zones](../facts/vpc.md#vpc-subnet-one-az-protects-from-zone-failure)
  link: [protect your applications from the failure of a single Availability Zone](../facts/vpc.md#vpc-subnet-one-az-protects-from-zone-failure)
vpc-subnet-public-ip-attribute-default
  claim: The subnet attribute that auto-assigns public IPv4 addresses is false for nondefault subnets and true for default subnets by default; the exception is a nondefault subnet created by the EC2 launch instance wizard, which sets it to true.
  scope: per subnet; default; adjustable; you can modify the attribute in the Amazon VPC console.
  link: [nondefault subnets have the IPv4 public addressing attribute set to `false`](../facts/vpc.md#vpc-subnet-public-ip-attribute-default)
  link: [default subnets have this attribute set to `true`](../facts/vpc.md#vpc-subnet-public-ip-attribute-default)
  link: [a nondefault subnet created by the Amazon EC2 launch instance wizard — the wizard sets the attribute to `true`](../facts/vpc.md#vpc-subnet-public-ip-attribute-default)
  say: off for subnets you create | on for default subnets
vpc-subnet-reserved-address-roles
  claim: In a 10.0.0.0/24 subnet AWS reserves five addresses, including 10.0.0.1 for the VPC router, 10.0.0.2 (reserved by AWS; the IP address of the DNS server is the base of the VPC network range plus two), 10.0.0.3 for future use, and 10.0.0.255, the network broadcast address, which is reserved because a VPC does not support broadcast.
  scope: per IPv4 subnet; fixed; example subnet 10.0.0.0/24; the pattern is the first four and the last address of each subnet CIDR block.
  link: [five IP addresses are reserved](../facts/vpc.md#vpc-subnet-reserved-address-roles)
  link: [Reserved by AWS for the VPC router](../facts/vpc.md#vpc-subnet-reserved-address-roles)
  link: [Reserved by AWS for future use](../facts/vpc.md#vpc-subnet-reserved-address-roles)
  link: [We do not support broadcast in a VPC](../facts/vpc.md#vpc-subnet-reserved-address-roles)
  say: five reserved addresses | the plus-one address is the VPC router | the plus-three address is for future use | the last address, because there is no broadcast
vpc-subnet-single-az
  claim: Each subnet must reside entirely within one Availability Zone and cannot span zones.
  scope: per subnet; fixed.
  link: [must reside entirely within one Availability Zone](../facts/vpc.md#vpc-subnet-single-az)
  link: [cannot span zones](../facts/vpc.md#vpc-subnet-single-az)
  say: lives entirely in one Availability Zone | cannot span zones
vpc-subnet-size-ipv4-vs-ipv6
  claim: A subnet IPv4 CIDR block is from /16 to /28; a subnet IPv6 CIDR block is from /44 to /64 in increments of /4.
  scope: per subnet; fixed; not adjustable.
  link: [From /16 to /28](../facts/vpc.md#vpc-subnet-size-ipv4-vs-ipv6)
  link: [From /44 to /64 in increments of /4](../facts/vpc.md#vpc-subnet-size-ipv4-vs-ipv6)
  say: slash sixteen to slash twenty-eight for IPv4 | slash forty-four to slash sixty-four for IPv6
vpc-subnet-types-dual-stack-ipv6-only
  claim: A dual-stack subnet has both an IPv4 and an IPv6 CIDR block and its resources can communicate over both; an IPv6-only subnet has only an IPv6 CIDR block and its resources must communicate over IPv6.
  scope: per subnet.
  link: [The subnet has both an IPv4 CIDR block and an IPv6 CIDR block](../facts/vpc.md#vpc-subnet-types-dual-stack-ipv6-only)
  link: [The subnet has an IPv6 CIDR block but does not have an IPv4 CIDR block](../facts/vpc.md#vpc-subnet-types-dual-stack-ipv6-only)
  link: [Resources in an IPv6-only subnet must communicate over IPv6](../facts/vpc.md#vpc-subnet-types-dual-stack-ipv6-only)
  say: dual stack has both IPv4 and IPv6 | IPv6-only has no IPv4 block
vpc-subnets-isolate-tiers
  claim: Use separate VPCs to isolate infrastructure by workload or organization, and subnets to isolate the web, application and database tiers inside one VPC.
  link: [Use separate VPCs to isolate infrastructure by workload or organizational entity](../facts/vpc.md#vpc-subnets-isolate-tiers)
  link: [Use subnets to isolate the tiers of your application (for example, web, application, and database) within a single VPC](../facts/vpc.md#vpc-subnets-isolate-tiers)
vpc-traffic-mirroring-price-per-eni-hour
  claim: Traffic Mirroring is charged per hour for each network interface with an active mirroring session; in the US East (Ohio) example the hourly rate is $0.015, and the charge continues until every active traffic mirror session is deleted.
  scope: per mirrored network interface, per hour, US East (Ohio); example rate on the pricing page.
  link: [the hourly rate is $0.015](../facts/vpc.md#vpc-traffic-mirroring-price-per-eni-hour)
  say: one and a half cents per session-hour
vpc-vpn-only-subnet-route
  claim: A subnet whose route table sends all traffic to a virtual private gateway but has no route to the internet gateway is a VPN-only subnet.
  link: [which is what makes the subnet a VPN-only subnet](../facts/vpc.md#vpc-vpn-only-subnet-route)
  say: a route to the virtual private gateway and none to the internet gateway
vpc-wa-cost08-flow-logs-for-transfer-analysis
  claim: The cost pillar recommends CloudWatch and VPC Flow Logs to capture data transfer and network usage, and Cost Explorer or CloudWatch to understand the data transfer cost of a workload.
  link: [Use Amazon CloudWatch and VPC flow logs to capture details about your data transfer and network usage](../facts/vpc.md#vpc-wa-cost08-flow-logs-for-transfer-analysis)
  link: [Use metering and reporting tools such as AWS Cost Explorer, CUDOS Dashboards, or CloudWatch to understand data transfer cost of your workload](../facts/vpc.md#vpc-wa-cost08-flow-logs-for-transfer-analysis)
vpc-wa-cost08-vpc-endpoints-avoid-internet
  claim: The Well-Architected cost pillar says to use VPC endpoints for private connections to supported AWS services, avoiding the public internet path that can lead to data transfer costs.
  link: [VPC endpoints allow for private connections between your VPC and supported AWS services](../facts/vpc.md#vpc-wa-cost08-vpc-endpoints-avoid-internet)
  link: [This allows you to avoid using the public internet, which can lead to data transfer costs](../facts/vpc.md#vpc-wa-cost08-vpc-endpoints-avoid-internet)
vpc-wa-rel02-bp03-cidr-cannot-change
  claim: The initial VPC CIDR block cannot be changed or deleted, though additional non-overlapping blocks can be added; subnet IPv4 CIDRs cannot be changed, while IPv6 CIDRs can.
  scope: per VPC and per subnet.
  link: [the initial VPC CIDR block allocated to your VPC cannot be changed or deleted](../facts/vpc.md#vpc-wa-rel02-bp03-cidr-cannot-change)
  link: [Subnet IPv4 CIDRs cannot be changed, however IPv6 CIDRs can](../facts/vpc.md#vpc-wa-rel02-bp03-cidr-cannot-change)
vpc-wa-rel02-bp03-ipv6-for-ephemeral-fleets
  claim: Well-Architected suggests IPv6 addressing for subnets in a dual-stack VPC, especially private subnets with fleets of ephemeral instances or containers that would otherwise need many IPv4 addresses.
  link: [IPv6 is well suited to being used in private subnets containing fleets of ephemeral instances or containers](../facts/vpc.md#vpc-wa-rel02-bp03-ipv6-for-ephemeral-fleets)
vpc-wa-rel02-bp03-plan-cidr-for-growth
  claim: When allocating CIDR space, leave room for more than one VPC per Region, for several subnets across Availability Zones, and for unused CIDR space inside the VPC for future expansion.
  link: [Allow IP address space for more than one VPC per Region](../facts/vpc.md#vpc-wa-rel02-bp03-plan-cidr-for-growth)
  link: [allow space for multiple subnets so that you can cover multiple Availability Zones](../facts/vpc.md#vpc-wa-rel02-bp03-plan-cidr-for-growth)
  link: [Consider leaving unused CIDR block space within a VPC for future expansion](../facts/vpc.md#vpc-wa-rel02-bp03-plan-cidr-for-growth)
vpc-wa-rel02-bp03-ranges-large-enough
  claim: VPC IP address ranges must be large enough for workload requirements, including future expansion and subnets across Availability Zones, counting load balancers, EC2 instances and container-based applications.
  link: [must be large enough to accommodate workload requirements](../facts/vpc.md#vpc-wa-rel02-bp03-ranges-large-enough)
vpc-wa-rel02-bp03-rfc1918-and-larger-blocks
  claim: Well-Architected says to allocate a private RFC 1918 range to each VPC and, when growth is unknown, to err on the side of larger CIDR blocks to reduce future reconfiguration, while warning that excessively large ranges make peering with overlapping networks difficult.
  link: [Private IP address ranges (following RFC 1918 guidelines) should be allocated for each VPC](../facts/vpc.md#vpc-wa-rel02-bp03-rfc1918-and-larger-blocks)
  link: [err on the side of larger CIDR blocks to reduce the potential for future reconfiguration](../facts/vpc.md#vpc-wa-rel02-bp03-rfc1918-and-larger-blocks)
  link: [Defining excessively large CIDR ranges well beyond future growth expectations, which can lead to difficulty peering with other networks with overlapping address ranges](../facts/vpc.md#vpc-wa-rel02-bp03-rfc1918-and-larger-blocks)
vpc-wa-rel02-bp03-subnet-anti-patterns
  claim: Well-Architected lists as anti-patterns: CIDR blocks too small for future growth (reconfiguration, possible downtime), misestimating how many IP addresses a load balancer uses, many high-traffic load balancers in the same subnets, and automatic scaling without monitoring IP address consumption.
  link: [CIDR blocks that are too small and requiring reconfiguration, potentially causing downtime](../facts/vpc.md#vpc-wa-rel02-bp03-subnet-anti-patterns)
  link: [Incorrectly estimating how many IP addresses an elastic load balancer can use](../facts/vpc.md#vpc-wa-rel02-bp03-subnet-anti-patterns)
vpc-wa-rel02-bp03-transient-fleets-and-eks-pods
  claim: Plan IP space for transient EC2 fleets such as Spot Fleets, Amazon EMR clusters or Amazon Redshift clusters, and for Amazon EKS, because each Kubernetes pod is assigned a routable address from the VPC CIDR block by default.
  link: [transient fleets of Amazon EC2 instances](../facts/vpc.md#vpc-wa-rel02-bp03-transient-fleets-and-eks-pods)
  link: [each Kubernetes pod is assigned a routable address from the VPC CIDR block by default](../facts/vpc.md#vpc-wa-rel02-bp03-transient-fleets-and-eks-pods)
vpc-wa-rel02-bp04-hub-and-spoke
  claim: When connecting several VPCs and on-premises networks, Well-Architected says to prefer a hub-and-spoke topology over a mesh, with AWS Transit Gateway as the hub; a mesh grows harder to manage as the number of networks increases.
  link: [opt for a hub-and-spoke topology over a meshed one](../facts/vpc.md#vpc-wa-rel02-bp04-hub-and-spoke)
  link: [As the number of connected networks increases, management and expansion of meshed connectivity becomes increasingly challenging](../facts/vpc.md#vpc-wa-rel02-bp04-hub-and-spoke)
vpc-wa-rel02-bp05-ipam-anti-patterns
  claim: The Well-Architected reliability pillar names reusing the on-premises IP range in a VPC, not tracking VPC ranges, and managing IP addresses in spreadsheets as anti-patterns, and points to an IPAM to automate allocation.
  link: [Using the same IP range in your VPC as you have on premises, in your corporate network, or other cloud providers](../facts/vpc.md#vpc-wa-rel02-bp05-ipam-anti-patterns)
  link: [Relying on manual IP address management processes, such as spreadsheets](../facts/vpc.md#vpc-wa-rel02-bp05-ipam-anti-patterns)
  link: [An IP address management (IPAM) system can help with automating this](../facts/vpc.md#vpc-wa-rel02-bp05-ipam-anti-patterns)
vpc-wa-rel02-bp05-non-overlapping-ranges
  claim: The IP ranges of VPCs must not overlap when they are peered, connected through a transit gateway or connected over VPN, and must not conflict with on-premises networks or other cloud providers.
  link: [The IP address ranges of each of your VPCs must not overlap when peered, connected via Transit Gateway, or connected over VPN](../facts/vpc.md#vpc-wa-rel02-bp05-non-overlapping-ranges)
  link: [Avoid IP address conflicts between a VPC and on-premises environments or with other cloud providers that you use](../facts/vpc.md#vpc-wa-rel02-bp05-non-overlapping-ranges)
vpc-wa-rel10-bp01-avoid-single-points-of-failure
  claim: A fundamental AWS design principle is to avoid single points of failure, including the physical infrastructure; a production workload that exists in only one Availability Zone is an anti-pattern.
  link: [avoid single points of failure, including the underlying physical infrastructure](../facts/vpc.md#vpc-wa-rel10-bp01-avoid-single-points-of-failure)
  link: [Your production workload exists only in a single Availability Zone](../facts/vpc.md#vpc-wa-rel10-bp01-avoid-single-points-of-failure)
vpc-wa-sec05-bp01-anti-pattern-single-vpc
  claim: The Well-Architected security pillar lists creating all resources in a single VPC or subnet as an anti-pattern.
  link: [You create all resources in a single VPC or subnet](../facts/vpc.md#vpc-wa-sec05-bp01-anti-pattern-single-vpc)
vpc-wa-sec05-bp01-data-layer-private-subnets
  claim: In the Well-Architected security pillar, the data layer, which hosts resources such as databases and shared file systems, can reside in different private subnets from the application layer, and at each layer boundary you can deploy controls that allow only authorized traffic to cross.
  link: [can reside in different private subnets from the resources of your application layer](../facts/vpc.md#vpc-wa-sec05-bp01-data-layer-private-subnets)
  link: [you can deploy controls that allow only authorized traffic to traverse across those boundaries](../facts/vpc.md#vpc-wa-sec05-bp01-data-layer-private-subnets)
vpc-wa-sec05-bp01-network-layers
  claim: The Well-Architected security pillar says to segment the network into layers by data sensitivity and access requirements, separating components that need inbound internet access, such as public web endpoints, from those that need only internal access, such as databases.
  link: [Segment your network topology into different layers based on logical groupings of your workload components according to their data sensitivity and access requirements](../facts/vpc.md#vpc-wa-sec05-bp01-network-layers)
  link: [Distinguish between components that require inbound access from the internet, such as public web endpoints, and those that only need internal access, such as databases](../facts/vpc.md#vpc-wa-sec05-bp01-network-layers)
vpc-wa-sec05-bp02-sg-references-sg
  claim: Network layers in AWS are mainly subnets; a security group can allow traffic from another security group by its identifier, so rules need few updates as the resources in the group change.
  link: [network layers are primarily defined using subnets according to IP address ranges within an Amazon VPC](../facts/vpc.md#vpc-wa-sec05-bp02-sg-references-sg)
  link: [a security group can have a rule that allows traffic from another security group by its identifier, minimizing updates as resources within the group change over time](../facts/vpc.md#vpc-wa-sec05-bp02-sg-references-sg)
vpc-wa-sec05-bp03-inspection-points
  claim: The Well-Architected security pillar asks for traffic inspection points between network layers, and says that AWS Network Firewall and vendor solutions that use a Gateway Load Balancer (GWLB) support different inline inspection deployment models.
  link: [Set up traffic inspection points between your network layers to make sure data in transit matches the expected categories and patterns](../facts/vpc.md#vpc-wa-sec05-bp03-inspection-points)
vpc-wa-sec06-no-ssh-rdp-use-session-manager
  claim: Well-Architected says security group ingress rules for EC2 instances should not allow port 22/tcp (SSH) or 3389/tcp (RDP), and to use AWS Systems Manager Session Manager for interactive access when needed, with session logging to CloudWatch Logs or Amazon S3.
  link: [do not permit access on port 22/tcp (SSH) or port 3389/tcp (RDP)](../facts/vpc.md#vpc-wa-sec06-no-ssh-rdp-use-session-manager)
  link: [Use AWS Systems Manager Session Manager to provide interactive access to instances when necessary](../facts/vpc.md#vpc-wa-sec06-no-ssh-rdp-use-session-manager)
vpc-wavelength-carrier-gateway
  claim: A VPC extends to a Wavelength Zone when you create a subnet associated with it; instances there get a carrier IP address, and a carrier gateway translates it with NAT for traffic to the carrier network and the internet.
  link: [A VPC extends to a Wavelength Zone when you create a subnet in the VPC and associate it with the Wavelength Zone](../facts/vpc.md#vpc-wavelength-carrier-gateway)
  link: [The carrier gateway uses NAT to translate the address](../facts/vpc.md#vpc-wavelength-carrier-gateway)
  say: a carrier gateway does NAT
vpc-wavelength-zones-no-direct-communication
  claim: EC2 instances in different Wavelength Zones of the same VPC cannot communicate with each other; AWS recommends one VPC per Wavelength Zone connected through a transit gateway, and a transit gateway attachment cannot be created in a Wavelength Zone subnet.
  link: [EC2 instances that are in different Wavelength Zones in the same VPC are not allowed to communicate with each other](../facts/vpc.md#vpc-wavelength-zones-no-direct-communication)
  link: [You can't create a transit gateway attachment to a subnet in a Wavelength Zone](../facts/vpc.md#vpc-wavelength-zones-no-direct-communication)
  say: not within one VPC
vpc-whitepaper-centralized-egress-ha-per-az
  claim: For high availability in centralized egress, use more than one NAT gateway, one per Availability Zone; if a NAT gateway is unavailable, traffic in that Availability Zone that traverses it may be dropped.
  link: [you should use more than one NAT gateway (one in each Availability Zone)](../facts/vpc.md#vpc-whitepaper-centralized-egress-ha-per-az)
  link: [traffic might be dropped in that Availability Zone that is traversing the affected NAT gateway](../facts/vpc.md#vpc-whitepaper-centralized-egress-ha-per-az)
vpc-whitepaper-tgw-keeps-traffic-in-az
  claim: A transit gateway generally does not act as a load balancer and would not distribute traffic evenly across NAT gateways in several Availability Zones; traffic across the transit gateway stays within an Availability Zone, if possible.
  link: [Transit Gateway generally does not act as a load balancer and would not distribute your traffic evenly across NAT gateways in the multiple Availability Zones](../facts/vpc.md#vpc-whitepaper-tgw-keeps-traffic-in-az)
  link: [The traffic across the Transit Gateway will stay within an Availability Zone, if possible](../facts/vpc.md#vpc-whitepaper-tgw-keeps-traffic-in-az)
