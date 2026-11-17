facts card: 506 facts
privatelink-acceptance-required-manual
  claim: An endpoint service can accept connection requests automatically; otherwise you must accept or reject them manually, and a consumer whose request you do not accept cannot access the service.
  scope: AWS PrivateLink endpoint service.
  link: [accept connection requests automatically](../facts/privatelink.md#privatelink-acceptance-required-manual)
  link: [can't access your endpoint service](../facts/privatelink.md#privatelink-acceptance-required-manual)
privatelink-allow-everyone-accept-all-is-public
  claim: If you grant everyone permission to access the endpoint service and configure it to accept all requests, your load balancer will be public even if it has no public IP address.
  scope: AWS PrivateLink endpoint service.
  link: [your load balancer will be public](../facts/privatelink.md#privatelink-allow-everyone-accept-all-is-public)
privatelink-case-resilience-datasync-no-internet
  claim: Resilience transfers its lab data securely using AWS PrivateLink, which establishes connectivity between virtual private clouds and AWS services without exposing data to the internet.
  scope: Resilience.
  link: [using AWS PrivateLink](../facts/privatelink.md#privatelink-case-resilience-datasync-no-internet)
  link: [without exposing data to the internet](../facts/privatelink.md#privatelink-case-resilience-datasync-no-internet)
privatelink-change-access-resources-and-service-networks-2024
  claim: The PrivateLink document history lists Access resources and service networks on December 1, 2024: AWS PrivateLink supports accessing resources and service networks across VPC and account boundaries.
  link: [December 1, 2024](../facts/privatelink.md#privatelink-change-access-resources-and-service-networks-2024)
  say: December 2024
privatelink-change-cross-region-access-2024
  claim: The PrivateLink document history lists Cross-Region access on November 26, 2024: a service provider can host a service in one Region and make it available in a set of AWS Regions, and a service consumer selects a service Region when creating an endpoint.
  link: [November 26, 2024](../facts/privatelink.md#privatelink-change-cross-region-access-2024)
  say: November 2024
privatelink-change-cross-region-aws-services-2025
  claim: On November 19, 2025 AWS PrivateLink added native cross-Region connectivity to AWS services: until then, interface VPC endpoints only supported connectivity to AWS services in the same Region, and now you can connect to select AWS services hosted in other Regions of the same AWS partition over interface endpoints.
  link: [November 19, 2025](../facts/privatelink.md#privatelink-change-cross-region-aws-services-2025)
  link: [connectivity to AWS services in the same Region](../facts/privatelink.md#privatelink-change-cross-region-aws-services-2025)
  say: November 2025 | before, same Region only
  changed: 2025-11-19: was Interface VPC endpoints only supported connectivity to AWS services in the same Region
privatelink-change-designated-ip-addresses-2023
  claim: The PrivateLink document history lists Designated IP addresses on August 17, 2023: you can specify the IP addresses for your endpoint network interfaces when you create or modify your VPC endpoint.
  link: [August 17, 2023](../facts/privatelink.md#privatelink-change-designated-ip-addresses-2023)
  say: August 2023
privatelink-change-tunnel-endpoints-2026
  claim: On September 18, 2026 AWS PrivateLink announced tunnel endpoints, a new type of VPC endpoint for network segments; before it, customers who wanted to share resources with another party had to do it one at a time by creating a Resource Configuration for every resource.
  link: [September 18, 2026](../facts/privatelink.md#privatelink-change-tunnel-endpoints-2026)
  link: [a new type of VPC endpoint](../facts/privatelink.md#privatelink-change-tunnel-endpoints-2026)
  say: September 2026
  changed: 2026-09-18: was customers who wanted to share their resources with another party such as an external vendor had to do it one at a time by creating a Resource Configuration for every resource
privatelink-concepts-private-ip-as-if-hosted
  claim: AWS PrivateLink lets clients in your VPC connect to services and resources in other VPCs using private IP addresses, as if those services and resources were hosted directly in your VPC.
  scope: AWS PrivateLink.
  link: [use AWS PrivateLink to allow the clients](../facts/privatelink.md#privatelink-concepts-private-ip-as-if-hosted)
  link: [using private IP addresses](../facts/privatelink.md#privatelink-concepts-private-ip-as-if-hosted)
privatelink-consumer-endpoint-only-in-service-azs
  claim: A consumer can create interface VPC endpoints in the Availability Zones in which the endpoint service is available.
  scope: AWS PrivateLink endpoint service.
  link: [Availability Zones in which your endpoint service](../facts/privatelink.md#privatelink-consumer-endpoint-only-in-service-azs)
privatelink-contributor-insights-built-in-rules
  claim: AWS PrivateLink provides built-in Contributor Insights rules for your endpoint services to find which endpoints contribute most to each supported metric; you must enable a rule before it collects data.
  scope: AWS PrivateLink endpoint services.
  link: [built-in Contributor Insights rules](../facts/privatelink.md#privatelink-contributor-insights-built-in-rules)
  link: [you must enable it](../facts/privatelink.md#privatelink-contributor-insights-built-in-rules)
privatelink-cross-region-aws-services-iam-default-deny
  claim: By default IAM entities do not have permission to access an AWS service in another Region through PrivateLink; an IAM administrator grants it with a policy that allows the vpce:AllowMultiRegion permission-only action.
  scope: IAM entities, cross-Region access to AWS services; default; not adjustable.
  link: [vpce:AllowMultiRegion](../facts/privatelink.md#privatelink-cross-region-aws-services-iam-default-deny)
privatelink-cross-region-aws-services-named-examples
  claim: You can create an interface endpoint to reach the listed AWS services in another AWS Region privately, as if they were running in your own VPC; the announcement names Amazon S3, Route53 and Elastic Container Registry (ECR) among them.
  scope: interface endpoints to cross-Region enabled AWS services.
  link: [access Amazon S3, Route53, Elastic Container Registry (ECR)](../facts/privatelink.md#privatelink-cross-region-aws-services-named-examples)
privatelink-cross-region-aws-services-regional-dns-only
  claim: You must use regional DNS when you access AWS services in another Region through an interface endpoint; zonal DNS is not supported.
  scope: interface endpoints to AWS services in another Region.
  link: [Zonal DNS is not supported](../facts/privatelink.md#privatelink-cross-region-aws-services-regional-dns-only)
privatelink-cross-region-endpoint-service-iam-default-deny
  claim: By default IAM entities do not have permission to make an endpoint service available in multiple Regions or to access an endpoint service across Regions.
  scope: IAM entities, cross-Region endpoint services; default; not adjustable.
  link: [don't have permission to make an endpoint service](../facts/privatelink.md#privatelink-cross-region-endpoint-service-iam-default-deny)
privatelink-cross-region-endpoint-service-unsupported-azs
  claim: Cross-Region access to a PrivateLink endpoint service is not supported for the Availability Zones use1-az3, usw1-az2, apne1-az3, apne2-az2 and apne2-az4.
  scope: cross-Region access to a PrivateLink endpoint service.
  link: [use1-az3](../facts/privatelink.md#privatelink-cross-region-endpoint-service-unsupported-azs)
privatelink-cross-region-failover-not-managed
  claim: With cross-Region access AWS PrivateLink manages failover between Availability Zones but does not manage failover across Regions.
  scope: AWS PrivateLink cross-Region access.
  link: [does not manage failover across Regions](../facts/privatelink.md#privatelink-cross-region-failover-not-managed)
privatelink-cross-region-host-and-consumer-select
  claim: A service provider can host a service in one Region and make it available in a set of supported Regions, and a service consumer selects the service Region when creating an endpoint.
  scope: AWS PrivateLink cross-Region access.
  link: [host a service in one Region](../facts/privatelink.md#privatelink-cross-region-host-and-consumer-select)
  link: [selects a service Region when creating an endpoint](../facts/privatelink.md#privatelink-cross-region-host-and-consumer-select)
privatelink-cross-region-only-privatelink-services
  claim: Cross-Region access is only supported for services that you share through AWS PrivateLink.
  scope: AWS PrivateLink cross-Region access.
  link: [only supported for services that you share](../facts/privatelink.md#privatelink-cross-region-only-privatelink-services)
privatelink-cross-region-prefer-intra-region
  claim: AWS recommends that consumers access a service using intra-Region connectivity instead of cross-Region connectivity when possible, because intra-Region connectivity has lower latency and lower costs.
  scope: AWS PrivateLink cross-Region access.
  link: [intra-Region connectivity provides lower latency and lower costs](../facts/privatelink.md#privatelink-cross-region-prefer-intra-region)
privatelink-domain-verification-up-to-48-hours
  claim: After you add the TXT record to verify the domain of a private DNS name for an endpoint service, it can take up to 48 hours for DNS record updates to take effect, but they often take effect much sooner.
  scope: private DNS name verification for an endpoint service; maximum; not adjustable.
  link: [up to 48 hours](../facts/privatelink.md#privatelink-domain-verification-up-to-48-hours)
  say: up to forty-eight hours
privatelink-endpoint-service-az-names-differ-use-az-ids
  claim: Service consumers see only the Availability Zones they have in common with the provider, and an Availability Zone name such as us-east-1a can map to a different physical zone in each account, so use AZ IDs to identify zones consistently.
  scope: AWS PrivateLink endpoint service.
  link: [mapped to a different physical Availability Zone](../facts/privatelink.md#privatelink-endpoint-service-az-names-differ-use-az-ids)
  link: [use AZ IDs](../facts/privatelink.md#privatelink-endpoint-service-az-names-differ-use-az-ids)
privatelink-endpoint-service-needs-load-balancer
  claim: A service provider creates an endpoint service to make a service available in a Region and must specify a load balancer, a Network Load Balancer or a Gateway Load Balancer, that receives consumer requests and routes them to the service.
  scope: AWS PrivateLink endpoint service.
  link: [must specify a load balancer](../facts/privatelink.md#privatelink-endpoint-service-needs-load-balancer)
  link: [Network Load Balancer or a Gateway Load Balancer](../facts/privatelink.md#privatelink-endpoint-service-needs-load-balancer)
privatelink-endpoint-service-not-available-by-default
  claim: By default an endpoint service is not available to service consumers; you must add permissions that allow specific AWS principals to connect to it.
  scope: AWS PrivateLink endpoint service; default; not adjustable.
  link: [not available to service consumers](../facts/privatelink.md#privatelink-endpoint-service-not-available-by-default)
  link: [add permissions that allow specific AWS principals](../facts/privatelink.md#privatelink-endpoint-service-not-available-by-default)
privatelink-endpoint-service-regional-reach-options
  claim: An endpoint service is available in the Region where you created it; consumers can reach it from other Regions if you enable cross-Region access or if they use VPC peering or a transit gateway.
  scope: AWS PrivateLink endpoint service.
  link: [available in the Region where you created it](../facts/privatelink.md#privatelink-endpoint-service-regional-reach-options)
  link: [enable cross-Region access](../facts/privatelink.md#privatelink-endpoint-service-regional-reach-options)
privatelink-faq-billing-data-processing-per-gb
  claim: Data processing charges apply for each gigabyte processed through VPC endpoints, regardless of the source or destination of the traffic.
  scope: per VPC endpoint, per gigabyte.
  link: [for each gigabyte processed through the VPC endpoints](../facts/privatelink.md#privatelink-faq-billing-data-processing-per-gb)
  say: per gigabyte processed
privatelink-faq-billing-interface-gwlb-hourly-per-az
  claim: If you create an interface or Gateway Load Balancer VPC endpoint, you are charged for each hour that the endpoint is provisioned in each Availability Zone.
  scope: interface and Gateway Load Balancer endpoints, per Availability Zone, per hour.
  link: [provisioned in each Availability Zone](../facts/privatelink.md#privatelink-faq-billing-interface-gwlb-hourly-per-az)
privatelink-faq-billing-partial-hour-full-hour
  claim: Each partial VPC endpoint-hour consumed is billed as a full hour.
  scope: per VPC endpoint-hour.
  link: [billed as a full hour](../facts/privatelink.md#privatelink-faq-billing-partial-hour-full-hour)
  say: a partial hour counts as a full hour
privatelink-faq-billing-resource-endpoint-hourly-any-az-count
  claim: If you create a resource VPC endpoint, you are charged for each hour regardless of the number of Availability Zones the endpoint is provisioned in.
  scope: resource endpoints, per hour.
  link: [regardless of the number of Availability Zones](../facts/privatelink.md#privatelink-faq-billing-resource-endpoint-hourly-any-az-count)
privatelink-faq-consumer-initiates-allowlisted-customers
  claim: The service consumer always initiates the connection, so PrivateLink is a one-way service, and the service provider only provides service to allowlisted customers.
  scope: AWS PrivateLink connections (FAQ answer).
  link: [it is a one-way service](../facts/privatelink.md#privatelink-faq-consumer-initiates-allowlisted-customers)
  say: the consumer always starts the connection
privatelink-faq-encryption-controls-aws-services-only
  claim: With VPC Encryption Controls, PrivateLink is only supported for AWS services; VPC endpoints to non-AWS services cannot stay in a VPC where you enforce encryption, and you must delete them before switching the VPC to enforce mode.
  scope: per VPC in enforce mode.
  link: [only supported for AWS Services](../facts/privatelink.md#privatelink-faq-encryption-controls-aws-services-only)
  say: only AWS services
privatelink-faq-endpoint-bandwidth-default-10-gbps-per-az
  claim: Each VPC endpoint supports 10 Gbps of continuous bandwidth per Availability Zone by default; more capacity is then added automatically.
  scope: per VPC endpoint, per Availability Zone; default; not adjustable; Additional capacity is added automatically beyond this value..
  link: [10 Gbps continuous bandwidth per Availability Zone](../facts/privatelink.md#privatelink-faq-endpoint-bandwidth-default-10-gbps-per-az)
  say: ten gigabits per second per Availability Zone
privatelink-faq-endpoint-bandwidth-max-100-gbps
  claim: In each Availability Zone, VPC endpoint capacity scales automatically beyond the default, up to 100 Gbps; the scaling is fully managed.
  scope: per VPC endpoint, per Availability Zone (the FAQ sentence states the default per Availability Zone and then the ceiling); maximum; not adjustable; Capacity is added automatically after the default per Availability Zone; scaling is fully managed..
  link: [up to 100 Gbps](../facts/privatelink.md#privatelink-faq-endpoint-bandwidth-max-100-gbps)
  say: up to one hundred gigabits per second
privatelink-faq-endpoint-dns-resolves-to-local-ip
  claim: A VPC endpoint has DNS names that resolve to local IP addresses in your VPC; traffic sent to these names is routed through the endpoint to the service or resource, which can be in another account.
  link: [resolve to local IP addresses in your VPC](../facts/privatelink.md#privatelink-faq-endpoint-dns-resolves-to-local-ip)
  say: they resolve to private IPs in your VPC
privatelink-faq-nlb-provider
  claim: A service owner offers a service through PrivateLink by putting a Network Load Balancer in front of it and creating a PrivateLink service registered with that load balancer; a consumer creates an interface VPC endpoint, which appears as network interfaces with private IPs in the consumer VPC.
  scope: per PrivateLink service.
  link: [Elastic Network Interfaces (ENIs) with private IPs](../facts/privatelink.md#privatelink-faq-nlb-provider)
  link: [Network Load Balancer (NLB) to front your service](../facts/privatelink.md#privatelink-faq-nlb-provider)
  say: the consumer gets network interfaces with private IPs | the provider puts an NLB in front
privatelink-faq-no-encryption-by-default
  claim: PrivateLink does not provide any encryption by default for data in transit.
  scope: per PrivateLink connection; default; not adjustable.
  link: [does not provide any encryption by default](../facts/privatelink.md#privatelink-faq-no-encryption-by-default)
  say: no default encryption
privatelink-faq-over-direct-connect
  claim: On-premises applications can connect over AWS Direct Connect to service endpoints in a VPC and so reach services powered by AWS PrivateLink privately.
  scope: per interface endpoint.
  link: [endpoints in Amazon VPC over AWS Direct Connect](../facts/privatelink.md#privatelink-faq-over-direct-connect)
  say: yes, over Direct Connect
privatelink-faq-owners-register-nlb-or-share-resources
  claim: Service owners can register their Network Load Balancers to PrivateLink services to offer their services to other AWS customers; resource owners can share their resources directly without using Network Load Balancers.
  scope: sharing services and resources over AWS PrivateLink (FAQ answer).
  link: [directly without using Network Load Balancers](../facts/privatelink.md#privatelink-faq-owners-register-nlb-or-share-resources)
  say: resources can be shared without an NLB
privatelink-faq-path-stays-within-aws
  claim: The path between a VPC endpoint and a service stays within AWS and does not traverse the internet, so it remains out of reach of internet breaches.
  scope: path between a VPC endpoint and its service (FAQ answer).
  link: [does not traverse the Internet](../facts/privatelink.md#privatelink-faq-path-stays-within-aws)
  say: it never crosses the internet
privatelink-faq-peering-limit-125-vs-unlimited-scale
  claim: The PrivateLink FAQ says that VPC peering is limited to 125 VPC connections, while PrivateLink has virtually unlimited scale.
  scope: VPC peering connections versus PrivateLink (FAQ wording).
  link: [VPC peering is limited to 125 VPC connections](../facts/privatelink.md#privatelink-faq-peering-limit-125-vs-unlimited-scale)
  link: [virtually unlimited scale](../facts/privatelink.md#privatelink-faq-peering-limit-125-vs-unlimited-scale)
  say: peering tops out at one hundred twenty-five | virtually unlimited
privatelink-faq-public-service-name-not-supported
  claim: The PrivateLink FAQ answers no to using a service public endpoint DNS name to reach your VPC endpoints: it currently supports only private endpoint names.
  scope: DNS names used to reach VPC endpoints (FAQ answer).
  link: [only support private endpoint names](../facts/privatelink.md#privatelink-faq-public-service-name-not-supported)
  say: only private endpoint names
privatelink-faq-resource-owner-resource-configuration-ram
  claim: A resource owner onboards a resource to PrivateLink by creating a resource configuration that has a list of resources; customers can create endpoints in their VPC to connect to the resources after the owner shares the resource configuration with their accounts using AWS Resource Access Manager (RAM).
  link: [creating a resource configuration](../facts/privatelink.md#privatelink-faq-resource-owner-resource-configuration-ram)
  link: [AWS Resource Access Manager (RAM)](../facts/privatelink.md#privatelink-faq-resource-owner-resource-configuration-ram)
  say: a resource configuration | shared with RAM
privatelink-faq-service-owner-nlb-allowlist
  claim: A service owner onboards a service to PrivateLink by putting a Network Load Balancer in front of it and creating a PrivateLink service registered with that load balancer; customers can create endpoints in their VPC after the owner allow-lists their accounts and IAM roles.
  link: [a Network Load Balancer to front your service](../facts/privatelink.md#privatelink-faq-service-owner-nlb-allowlist)
  link: [allow-list their accounts and IAM roles](../facts/privatelink.md#privatelink-faq-service-owner-nlb-allowlist)
  say: a Network Load Balancer in front of the service | allow-list the consumer accounts and roles
privatelink-faq-what
  claim: AWS PrivateLink lets you access services hosted on AWS while keeping all network traffic within the AWS network; consumers reach PrivateLink-powered services from a VPC or on premises without public IPs and without traffic crossing the internet.
  scope: per PrivateLink service.
  link: [all the network traffic within the AWS network](../facts/privatelink.md#privatelink-faq-what)
  link: [without using public IPs](../facts/privatelink.md#privatelink-faq-what)
  link: [the traffic to traverse across the Internet](../facts/privatelink.md#privatelink-faq-what)
  say: traffic stays on the AWS network | no public IPs, no internet
privatelink-guide-private-connect-no-igw-nat
  claim: AWS PrivateLink privately connects your VPC to services and resources as if they were in your VPC, with no internet gateway, NAT device, public IP address, Direct Connect or Site-to-Site VPN needed from your private subnets, so you control which endpoints and resources are reachable.
  scope: AWS PrivateLink.
  link: [highly available, scalable technology](../facts/privatelink.md#privatelink-guide-private-connect-no-igw-nat)
  link: [control the specific API endpoints](../facts/privatelink.md#privatelink-guide-private-connect-no-igw-nat)
privatelink-interface-endpoint-sends-tcp-or-udp
  claim: An interface endpoint sends TCP or UDP traffic to an endpoint service.
  scope: interface endpoints.
  link: [TCP or UDP traffic to an endpoint service](../facts/privatelink.md#privatelink-interface-endpoint-sends-tcp-or-udp)
privatelink-ipv6-endpoint-service-needs-dualstack-nlb
  claim: To enable an endpoint service to accept IPv6 requests, all Network Load Balancers for the endpoint service must use the dualstack IP address type; the targets do not need to support IPv6 traffic.
  scope: IPv6 for a PrivateLink endpoint service.
  link: [must use the dualstack IP address type](../facts/privatelink.md#privatelink-ipv6-endpoint-service-needs-dualstack-nlb)
privatelink-metrics-published-for-which-endpoints
  claim: AWS PrivateLink publishes CloudWatch metrics for interface endpoints, Gateway Load Balancer endpoints and endpoint services, but not for gateway endpoints or for endpoint service consumers that use cross-Region access; metrics are sent every minute at no additional cost by default.
  scope: AWS PrivateLink monitoring.
  link: [not published for gateway endpoints](../facts/privatelink.md#privatelink-metrics-published-for-which-endpoints)
  link: [one-minute intervals, at no additional cost](../facts/privatelink.md#privatelink-metrics-published-for-which-endpoints)
privatelink-nlb-security-group-must-allow-clients
  claim: If the Network Load Balancer of an endpoint service has a security group, it must allow inbound traffic from the clients' IP addresses, or you can turn off evaluation of inbound security group rules for traffic through AWS PrivateLink.
  scope: AWS PrivateLink endpoint service.
  link: [must allow inbound traffic from the IP addresses](../facts/privatelink.md#privatelink-nlb-security-group-must-allow-clients)
privatelink-nlb-to-service-cardinality
  claim: A Network Load Balancer can be associated with a single endpoint service, but an endpoint service can be associated with multiple Network Load Balancers.
  scope: AWS PrivateLink endpoint service.
  link: [associated with a single endpoint service](../facts/privatelink.md#privatelink-nlb-to-service-cardinality)
privatelink-permissions-and-acceptance-control-access
  claim: Permissions and acceptance settings together control which consumers can access an endpoint service: you can grant trusted principals permission and accept all requests automatically, or grant a wider group permission and accept specific requests manually.
  scope: AWS PrivateLink endpoint service.
  link: [permissions and acceptance settings](../facts/privatelink.md#privatelink-permissions-and-acceptance-control-access)
  link: [manually accept specific connection requests](../facts/privatelink.md#privatelink-permissions-and-acceptance-control-access)
privatelink-pricing-cross-region-endpoint-owner-pays-both-directions
  claim: The interface endpoint owner is charged for each gigabyte transferred between Regions, regardless of the direction of the data transfer.
  scope: cross-Region interface endpoint, per GB.
  link: [regardless of the directionality of the data transfer](../facts/privatelink.md#privatelink-pricing-cross-region-endpoint-owner-pays-both-directions)
  say: both directions are charged
privatelink-pricing-cross-region-no-premium
  claim: Accessing a service in another Region over PrivateLink has no premium, but you pay the standard PrivateLink data processing and hourly charges plus cross-Region data transfer rates.
  scope: interface endpoint to a supported endpoint service in another Region.
  link: [no premium for accessing a service](../facts/privatelink.md#privatelink-pricing-cross-region-no-premium)
  say: no extra premium, but cross-Region transfer rates apply
privatelink-pricing-cross-region-provider-hourly-per-active-region
  claim: A service provider incurs a fixed hourly charge per active remote Region, whatever the number of VPC endpoints that use the service; a Region is active when at least one interface endpoint is connected to the service.
  scope: per active remote Region, per hour, service provider.
  link: [fixed hourly charge per active remote region](../facts/privatelink.md#privatelink-pricing-cross-region-provider-hourly-per-active-region)
  say: one hourly charge per active remote Region
privatelink-pricing-cross-region-provider-no-transfer-charge
  claim: The service provider does not incur any additional charges for inter-Region data transfer in cross-Region PrivateLink.
  scope: service provider, cross-Region access.
  link: [does not incur any additional charges](../facts/privatelink.md#privatelink-pricing-cross-region-provider-no-transfer-charge)
privatelink-pricing-resource-endpoint-example-hourly
  claim: In the PrivateLink pricing example for a resource endpoint (prices in USD for us-east-1), you pay an hourly charge of $0.02 per resource per hour.
  scope: resource endpoint example, us-east-1, per resource per hour.
  link: [$0.02 per resource per hour](../facts/privatelink.md#privatelink-pricing-resource-endpoint-example-hourly)
  say: two cents per resource per hour
privatelink-private-dns-domain-label-63-total-255
  claim: For a verified domain name of an endpoint service, each DNS label can have up to 63 characters and the whole domain name must not exceed a total length of 255 characters.
  scope: domain name for an endpoint service private DNS name; maximum; not adjustable.
  link: [up to 63 characters](../facts/privatelink.md#privatelink-private-dns-domain-label-63-total-255)
  link: [total length of 255 characters](../facts/privatelink.md#privatelink-private-dns-domain-label-63-total-255)
  say: up to sixty-three characters | a total length of two hundred fifty-five characters
privatelink-provider-cannot-disassociate-lb-with-endpoints
  claim: You cannot disassociate a load balancer from an endpoint service while endpoints are connected to the service.
  scope: AWS PrivateLink endpoint service.
  link: [can't disassociate a load balancer](../facts/privatelink.md#privatelink-provider-cannot-disassociate-lb-with-endpoints)
privatelink-provider-cross-zone-lb-tradeoff
  claim: Cross-zone load balancing is an alternative to hosting an endpoint service in several zones, but consumers lose access from both zones if the zone hosting the service fails, and EC2 data transfer charges apply.
  scope: AWS PrivateLink endpoint service.
  link: [consumers will lose access to the endpoint service](../facts/privatelink.md#privatelink-provider-cross-zone-lb-tradeoff)
  link: [EC2 data transfer charges apply](../facts/privatelink.md#privatelink-provider-cross-zone-lb-tradeoff)
privatelink-provider-dns-txt-record-verification
  claim: To verify a private DNS name, the provider adds a TXT record to the DNS server of its public domain, and verification completes when AWS detects that TXT record.
  scope: AWS PrivateLink endpoint service private DNS.
  link: [add a TXT record to the DNS server](../facts/privatelink.md#privatelink-provider-dns-txt-record-verification)
  link: [existence of the TXT record](../facts/privatelink.md#privatelink-provider-dns-txt-record-verification)
privatelink-provider-enable-two-azs-for-ha
  claim: An endpoint service is available in the Availability Zones enabled for its Network Load Balancer, and for high availability AWS recommends enabling the load balancer in at least two Availability Zones with EC2 instances registered in each enabled zone.
  scope: AWS PrivateLink endpoint service.
  link: [at least two Availability Zones](../facts/privatelink.md#privatelink-provider-enable-two-azs-for-ha)
  link: [register these instances with your load balancer](../facts/privatelink.md#privatelink-provider-enable-two-azs-for-ha)
privatelink-provider-nlb-billed-hourly-full-hour
  claim: A Network Load Balancer is charged for each hour or partial hour it is running, each partial hour is billed as a full hour, and you are also charged for the Network Load Balancer Capacity Units (NLCU) it uses per minute.
  scope: Network Load Balancer.
  link: [each hour or partial hour](../facts/privatelink.md#privatelink-provider-nlb-billed-hourly-full-hour)
  link: [billed as a full hour](../facts/privatelink.md#privatelink-provider-nlb-billed-hourly-full-hour)
privatelink-provider-no-private-dns-consumers-update-apps
  claim: If a provider does not enable private DNS, consumers might need to update their applications to use the public DNS name of the VPC endpoint service.
  scope: AWS PrivateLink endpoint service private DNS.
  link: [might need to update their applications](../facts/privatelink.md#privatelink-provider-no-private-dns-consumers-update-apps)
privatelink-provider-one-private-dns-name
  claim: An endpoint service can have only one private DNS name, and before you configure it you must prove that you own the domain with a domain ownership verification check.
  scope: AWS PrivateLink endpoint service.
  link: [only one private DNS name](../facts/privatelink.md#privatelink-provider-one-private-dns-name)
  link: [domain ownership verification check](../facts/privatelink.md#privatelink-provider-one-private-dns-name)
privatelink-provider-private-dns-same-as-public-name
  claim: If the provider uses the DNS name of its public endpoint as the private DNS name of the endpoint service, consumers can reach the public endpoint or the endpoint service with the same client application, without modification.
  scope: AWS PrivateLink endpoint service private DNS.
  link: [without modification](../facts/privatelink.md#privatelink-provider-private-dns-same-as-public-name)
  link: [private DNS name of the endpoint service](../facts/privatelink.md#privatelink-provider-private-dns-same-as-public-name)
privatelink-regional-name-round-robin-across-azs
  claim: When a request uses the regional endpoint name of a VPC endpoint service, AWS selects a healthy endpoint network interface by round robin across Availability Zones, and consumers can use the zonal endpoints to keep traffic in the same zone.
  scope: AWS PrivateLink endpoint service.
  link: [using the round robin algorithm](../facts/privatelink.md#privatelink-regional-name-round-robin-across-azs)
  link: [use the zonal endpoints](../facts/privatelink.md#privatelink-regional-name-round-robin-across-azs)
privatelink-remove-permission-keeps-existing-connections
  claim: Removing permissions from an endpoint service does not affect existing connections that were previously accepted.
  scope: AWS PrivateLink endpoint service.
  link: [does not affect existing connections](../facts/privatelink.md#privatelink-remove-permission-keeps-existing-connections)
privatelink-resource-endpoint-billing-hourly-and-per-gb
  claim: With resource endpoints you are billed for each hour that the resource VPC endpoint is provisioned and per GB of data processed when you access resources; the resource owner is billed per GB processed by its resource gateways.
  scope: resource endpoints and resource gateways.
  link: [resource VPC endpoint is provisioned](../facts/privatelink.md#privatelink-resource-endpoint-billing-hourly-and-per-gb)
privatelink-resource-endpoint-connections-start-from-endpoint-vpc
  claim: Network connections must be initiated from the VPC that contains the resource endpoint, not from the VPC that has the resource; the resource's VPC cannot initiate connections into the endpoint VPC.
  scope: resource endpoints.
  link: [from the VPC that contains the resource endpoint](../facts/privatelink.md#privatelink-resource-endpoint-connections-start-from-endpoint-vpc)
privatelink-resource-endpoint-no-load-balancer-needed
  claim: A resource endpoint lets you privately access a VPC resource, such as a database in another VPC, and resource endpoints don't require a load balancer; without resource endpoints you had to add an internet gateway or use an interface endpoint with a Network Load Balancer. The PrivateLink document history dates this to December 1, 2024.
  scope: resource VPC endpoints.
  link: [December 1, 2024](../facts/privatelink.md#privatelink-resource-endpoint-no-load-balancer-needed)
  link: [privately and securely access VPC resources](../facts/privatelink.md#privatelink-resource-endpoint-no-load-balancer-needed)
  say: December 2024
  changed: 2024-12-01: was access the resource using a AWS PrivateLink interface endpoint and a Network Load Balancer
privatelink-resource-endpoint-only-rds-arn-resources
  claim: The only supported ARN-based resources for a resource endpoint are Amazon RDS resources.
  scope: resource endpoints.
  link: [only supported ARN-based resources are Amazon RDS resources](../facts/privatelink.md#privatelink-resource-endpoint-only-rds-arn-resources)
privatelink-resource-endpoint-tcp-only
  claim: A resource endpoint supports TCP traffic and does not support UDP traffic.
  scope: resource endpoints.
  link: [UDP traffic is not supported](../facts/privatelink.md#privatelink-resource-endpoint-tcp-only)
privatelink-resource-gateway-default-16-ipv4-per-eni
  claim: By default, all resource gateways are assigned 16 IPv4 addresses per ENI.
  scope: per resource gateway ENI; default; not adjustable.
  link: [16 IPv4 addresses per ENI](../facts/privatelink.md#privatelink-resource-gateway-default-16-ipv4-per-eni)
  say: sixteen IPv4 addresses per network interface
privatelink-resource-gateways-max-100-per-vpc
  claim: A VPC can have a maximum of 100 resource gateways.
  scope: per VPC; maximum; not adjustable; the page points to the VPC Lattice quotas page for the quota.
  link: [maximum of 100 resource gateways](../facts/privatelink.md#privatelink-resource-gateways-max-100-per-vpc)
  say: a maximum of one hundred resource gateways
privatelink-saas-access-private-as-if-in-vpc
  claim: With AWS PrivateLink you can access SaaS products privately, as if they were running in your own VPC, and you can discover, purchase and provision SaaS products powered by PrivateLink through AWS Marketplace.
  scope: AWS PrivateLink SaaS access.
  link: [access SaaS products privately](../facts/privatelink.md#privatelink-saas-access-private-as-if-in-vpc)
  link: [through AWS Marketplace](../facts/privatelink.md#privatelink-saas-access-private-as-if-in-vpc)
privatelink-saas-provider-endpoint-service-consumer-interface-endpoint
  claim: For a SaaS product the service provider creates an endpoint service and grants customers access, and the consumer creates an interface endpoint that connects one or more subnets of its VPC to the endpoint service.
  scope: AWS PrivateLink SaaS access.
  link: [service provider creates an endpoint service](../facts/privatelink.md#privatelink-saas-provider-endpoint-service-consumer-interface-endpoint)
  link: [you create an interface VPC endpoint](../facts/privatelink.md#privatelink-saas-provider-endpoint-service-consumer-interface-endpoint)
privatelink-service-network-endpoint-billing
  claim: You are billed hourly for the resource configurations associated with your service network and per GB of data processed through the service network VPC endpoint; you are not billed hourly for the service-network VPC endpoint itself.
  scope: service-network endpoints.
  link: [not billed hourly for the service-network VPC endpoint](../facts/privatelink.md#privatelink-service-network-endpoint-billing)
privatelink-service-network-endpoint-concept
  claim: A service-network endpoint lets you privately and securely access the resources and services associated with a service network, so you can reach multiple resources and services through a single VPC endpoint.
  scope: service-network endpoints.
  link: [through a single VPC endpoint](../facts/privatelink.md#privatelink-service-network-endpoint-concept)
privatelink-source-ip-is-load-balancer-node
  claim: Through an interface endpoint the application sees the private IP addresses of the load balancer nodes as the source, not the consumers' addresses; with proxy protocol enabled on the load balancer you can read the consumer addresses and endpoint IDs from the proxy protocol header.
  scope: AWS PrivateLink endpoint service.
  link: [private IP addresses of the load balancer nodes](../facts/privatelink.md#privatelink-source-ip-is-load-balancer-node)
  link: [proxy protocol header](../facts/privatelink.md#privatelink-source-ip-is-load-balancer-node)
privatelink-tunnel-endpoint-geneve-encapsulation
  claim: Tunnel endpoints require you to tunnel into another VPC using GENEVE encapsulation, and GENEVE traffic must use UDP and port 6081 on the tunnel endpoint.
  scope: tunnel endpoints.
  link: [UDP and port 6081](../facts/privatelink.md#privatelink-tunnel-endpoint-geneve-encapsulation)
  link: [GENEVE encapsulation](../facts/privatelink.md#privatelink-tunnel-endpoint-geneve-encapsulation)
privatelink-vs-lattice-guide-single-or-multiple-vpcs
  claim: Amazon VPC Lattice is a fully managed application networking service to connect, secure and monitor the services and resources of an application, and it works with a single VPC or across multiple VPCs from one or more accounts.
  scope: Amazon VPC Lattice.
  link: [a single virtual private cloud (VPC)](../facts/privatelink.md#privatelink-vs-lattice-guide-single-or-multiple-vpcs)
privatelink-vs-lattice-wp-application-networking
  claim: Amazon VPC Lattice is a fully managed application networking service that is used to connect, monitor and secure services across various accounts and VPCs.
  scope: Amazon VPC Lattice.
  link: [fully managed application networking service](../facts/privatelink.md#privatelink-vs-lattice-wp-application-networking)
  link: [connect, monitor, and secure services across various accounts](../facts/privatelink.md#privatelink-vs-lattice-wp-application-networking)
privatelink-wa-rel02-bp05-overlap-remedy
  claim: If you must connect overlapping IP ranges, you can either migrate to a new range of addresses or use techniques such as a private NAT gateway or AWS PrivateLink.
  scope: REL02-BP05.
  link: [migrate to a new range of addresses](../facts/privatelink.md#privatelink-wa-rel02-bp05-overlap-remedy)
  link: [private NAT Gateway or AWS PrivateLink](../facts/privatelink.md#privatelink-wa-rel02-bp05-overlap-remedy)
privatelink-wp-consumer-and-provider-may-overlap
  claim: The consumer and the service are not required to be in the same VPC, and when the VPCs differ they can have overlapping IP address ranges.
  scope: AWS PrivateLink.
  link: [can have overlapping IP address ranges](../facts/privatelink.md#privatelink-wp-consumer-and-provider-may-overlap)
privatelink-wp-endpoints-reachable-over-peering-tgw-dx
  claim: You can access AWS PrivateLink endpoints over VPC peering, VPN, Transit Gateway, Cloud WAN and AWS Direct Connect.
  scope: AWS PrivateLink endpoints.
  link: [access AWS PrivateLink endpoints over VPC peering](../facts/privatelink.md#privatelink-wp-endpoints-reachable-over-peering-tgw-dx)
  link: [Transit Gateway, Cloud WAN](../facts/privatelink.md#privatelink-wp-endpoints-reachable-over-peering-tgw-dx)
privatelink-wp-good-solution-for-overlapping-ip
  claim: The connectivity-options whitepaper recommends PrivateLink for using services offered by another VPC securely within the AWS network over private IP addresses, and calls it a good solution when the VPCs have overlapping IP addresses.
  scope: AWS PrivateLink design.
  link: [good solution when the VPCs have overlapped](../facts/privatelink.md#privatelink-wp-good-solution-for-overlapping-ip)
privatelink-wp-mix-of-technologies
  claim: The whitepaper says an architecture will contain a mix of these technologies, which can be combined: for example, PrivateLink for API-style client-server connectivity, VPC peering for direct connectivity requirements where placement groups may still be desired within the Region or where inter-Region connectivity is needed, and Transit Gateway to simplify connectivity of VPCs at scale and for edge consolidation of hybrid connectivity.
  scope: AWS PrivateLink design.
  link: [AWS PrivateLink handling API style client-server connectivity](../facts/privatelink.md#privatelink-wp-mix-of-technologies)
  link: [Transit Gateway to simplify connectivity of VPCs](../facts/privatelink.md#privatelink-wp-mix-of-technologies)
privatelink-wp-only-consumer-initiates
  claim: The whitepaper describes PrivateLink as letting a provider privately expose a service in one VPC to other (consumer) VPCs within an AWS Region in a way that only the consumer VPCs initiate connections to the provider VPC.
  scope: AWS PrivateLink, within an AWS Region (as the whitepaper sentence states).
  link: [only consumer VPCs initiate connections](../facts/privatelink.md#privatelink-wp-only-consumer-initiates)
privatelink-wp-provider-nlb-consumer-endpoint-steps
  claim: To use PrivateLink the provider creates a Network Load Balancer for the application and a VPC endpoint service configuration that points to it; the consumer creates an interface endpoint, which puts a network interface with a private IP address in the consumer subnet as the entry point.
  scope: AWS PrivateLink endpoint service.
  link: [create a Network Load Balancer for your application](../facts/privatelink.md#privatelink-wp-provider-nlb-consumer-endpoint-steps)
  link: [creates an interface endpoint to your service](../facts/privatelink.md#privatelink-wp-provider-nlb-consumer-endpoint-steps)
privatelink-wp-security-groups-manage-endpoint-access
  claim: Interface endpoints are created inside your VPC with elastic network interfaces and IP addresses from your subnets, so VPC security groups can manage network access to the endpoints.
  scope: interface endpoints.
  link: [VPC Security Groups can be used to manage](../facts/privatelink.md#privatelink-wp-security-groups-manage-endpoint-access)
privatelink-wp-unidirectional-overlapping-ips
  claim: In PrivateLink only the clients in the consumer VPC can initiate a connection to the service, and it suits client and server VPCs with overlapping IP addresses because the endpoint network interfaces sit in the client VPC and cause no IP conflicts with the provider.
  scope: AWS PrivateLink design.
  link: [no IP conflicts with the service provider](../facts/privatelink.md#privatelink-wp-unidirectional-overlapping-ips)
  link: [overlapping IP addresses](../facts/privatelink.md#privatelink-wp-unidirectional-overlapping-ips)
transit-gateway-amazon-side-asn-16bit-range
  claim: A private Amazon side ASN for a transit gateway can be from 64512 to 65534 for 16-bit ASNs.
  scope: Amazon side ASN of a transit gateway, 16-bit; fixed; not adjustable.
  link: [64512 to 65534](../facts/transit-gateway.md#transit-gateway-amazon-side-asn-16bit-range)
  say: sixty-four five twelve to sixty-five five thirty-four
transit-gateway-amazon-side-asn-32bit-range
  claim: A private Amazon side ASN for a transit gateway can be from 4200000000 to 4294967294 for 32-bit ASNs.
  scope: Amazon side ASN of a transit gateway, 32-bit; fixed; not adjustable.
  link: [4200000000 to 4294967294](../facts/transit-gateway.md#transit-gateway-amazon-side-asn-32bit-range)
  say: four point two billion to four point two nine four billion
transit-gateway-appliance-mode-exactly-one-tgw
  claim: To guarantee flow stickiness you must connect exactly one transit gateway to the appliance VPC, because multiple transit gateways do not share flow state information.
  scope: transit gateway appliance mode.
  link: [connect exactly one transit gateway](../facts/transit-gateway.md#transit-gateway-appliance-mode-exactly-one-tgw)
  link: [do not share flow state information](../facts/transit-gateway.md#transit-gateway-appliance-mode-exactly-one-tgw)
transit-gateway-appliance-mode-flow-hash-symmetric
  claim: With appliance mode, a transit gateway uses a flow hash algorithm to pick one network interface in the appliance VPC for the life of the flow and uses the same interface for return traffic, so bidirectional traffic is routed symmetrically through the same Availability Zone.
  scope: transit gateway appliance mode.
  link: [flow hash algorithm](../facts/transit-gateway.md#transit-gateway-appliance-mode-flow-hash-symmetric)
  link: [routed symmetrically](../facts/transit-gateway.md#transit-gateway-appliance-mode-flow-hash-symmetric)
transit-gateway-appliance-mode-flow-source-any-attachment
  claim: Although appliance mode is supported only on VPC attachments, the network flow can come from any other transit gateway attachment type, including VPC, VPN and Connect attachments.
  scope: transit gateway appliance mode.
  link: [network flow can come from any other](../facts/transit-gateway.md#transit-gateway-appliance-mode-flow-source-any-attachment)
  link: [including VPC, VPN, and Connect attachments](../facts/transit-gateway.md#transit-gateway-appliance-mode-flow-source-any-attachment)
transit-gateway-appliance-mode-needs-route-propagation
  claim: For Availability Zone aware routing in appliance mode, route propagation must be enabled on the transit gateway route table associated with the appliance-mode VPC attachment; without it the transit gateway cannot determine the source and destination Availability Zones.
  scope: transit gateway appliance mode.
  link: [Route propagation must be enabled](../facts/transit-gateway.md#transit-gateway-appliance-mode-needs-route-propagation)
  link: [cannot determine the source and destination Availability Zones](../facts/transit-gateway.md#transit-gateway-appliance-mode-needs-route-propagation)
transit-gateway-appliance-mode-off-stays-in-az
  claim: When appliance mode is not enabled, traffic is kept to the originating Availability Zone; enabling it on an existing attachment might affect the attachment's current route because the flow can then use any Availability Zone.
  scope: transit gateway appliance mode; default; not adjustable.
  link: [When appliance mode is not enabled](../facts/transit-gateway.md#transit-gateway-appliance-mode-off-stays-in-az)
  link: [kept to the originating Availability Zone](../facts/transit-gateway.md#transit-gateway-appliance-mode-off-stays-in-az)
transit-gateway-appliance-mode-same-az-for-flow
  claim: With appliance mode enabled on the VPC attachment that holds a stateful network appliance, the transit gateway uses the same Availability Zone for that attachment for the lifetime of a flow between source and destination.
  scope: transit gateway VPC attachment.
  link: [enable appliance mode support for the VPC attachment](../facts/transit-gateway.md#transit-gateway-appliance-mode-same-az-for-flow)
  link: [same Availability Zone for that VPC attachment](../facts/transit-gateway.md#transit-gateway-appliance-mode-same-az-for-flow)
transit-gateway-appliance-mode-vpc-attachments-only
  claim: Appliance mode is supported only for VPC attachments.
  scope: transit gateway appliance mode.
  link: [Appliance mode is only supported for VPC attachments](../facts/transit-gateway.md#transit-gateway-appliance-mode-vpc-attachments-only)
transit-gateway-attachment-ipv6-support-default-disabled
  claim: IPv6 support on a transit gateway VPC attachment is disabled by default.
  scope: transit gateway VPC attachment; default; not adjustable.
  link: [The default value is `disable`](../facts/transit-gateway.md#transit-gateway-attachment-ipv6-support-default-disabled)
  link: [enable or disable IPv6 support](../facts/transit-gateway.md#transit-gateway-attachment-ipv6-support-default-disabled)
transit-gateway-attachment-no-ipv6-only-subnet
  claim: You cannot create a transit gateway attachment with IPv6-only subnets; the attachment subnets must also support IPv4 addresses.
  scope: transit gateway VPC attachment.
  link: [can't create a transit gateway attachment using IPv6-only subnets](../facts/transit-gateway.md#transit-gateway-attachment-no-ipv6-only-subnet)
transit-gateway-attachment-one-route-table-association
  claim: A transit gateway attachment can be associated with a single route table, while a route table can be associated with zero to many attachments.
  scope: transit gateway attachment.
  link: [associate a transit gateway attachment](../facts/transit-gateway.md#transit-gateway-attachment-one-route-table-association)
  link: [a single route table](../facts/transit-gateway.md#transit-gateway-attachment-one-route-table-association)
  link: [zero to many attachments](../facts/transit-gateway.md#transit-gateway-attachment-one-route-table-association)
transit-gateway-attachment-subnets-are-entry-and-exit
  claim: Only the subnets associated with a transit gateway attachment are entry and exit points for transit gateway traffic; routes in other subnets in the same Availability Zone do not enable traffic flow.
  scope: transit gateway VPC attachment.
  link: [Only the specific subnets associated with the](../facts/transit-gateway.md#transit-gateway-attachment-subnets-are-entry-and-exit)
  link: [entry/exit points for transit gateway traffic](../facts/transit-gateway.md#transit-gateway-attachment-subnets-are-entry-and-exit)
transit-gateway-az-without-attachment-cannot-reach
  claim: Only resources in Availability Zones where the VPC has a transit gateway attachment subnet can reach the transit gateway.
  scope: transit gateway VPC attachment.
  link: [only resources that reside in Availability Zones](../facts/transit-gateway.md#transit-gateway-az-without-attachment-cannot-reach)
  link: [where there is a transit gateway attachment](../facts/transit-gateway.md#transit-gateway-az-without-attachment-cannot-reach)
transit-gateway-bandwidth-beyond-default-attempt
  claim: For VPC attachments, Direct Connect gateways and peered transit gateway attachments, AWS says it will attempt to provide additional bandwidth beyond the default value.
  scope: VPC attachments, Direct Connect gateways, peered transit gateway attachments.
  link: [additional bandwidth beyond the default value](../facts/transit-gateway.md#transit-gateway-bandwidth-beyond-default-attempt)
  say: AWS will try to give more bandwidth
transit-gateway-bgp-multipath-as-path-relax-not-supported
  claim: BGP Multipath AS-Path Relax is not supported, so you cannot use ECMP over different Autonomous System Numbers.
  scope: transit gateway ECMP.
  link: [BGP Multipath AS-Path Relax is not supported](../facts/transit-gateway.md#transit-gateway-bgp-multipath-as-path-relax-not-supported)
transit-gateway-blackhole-prevents-inter-vpc
  claim: In a centralized egress design behind a transit gateway you can prevent inter-VPC communication by adding a blackhole route for each VPC CIDR in the transit gateway route table.
  scope: transit gateway egress scenario.
  link: [prevent inter-VPC communication by adding a blackhole route](../facts/transit-gateway.md#transit-gateway-blackhole-prevents-inter-vpc)
transit-gateway-blackhole-route-drops
  claim: You can create a blackhole route in a transit gateway route table to drop traffic that matches the route.
  scope: transit gateway route table.
  link: [blackhole route](../facts/transit-gateway.md#transit-gateway-blackhole-route-drops)
  link: [drops traffic that matches the route](../facts/transit-gateway.md#transit-gateway-blackhole-route-drops)
transit-gateway-blog-cost-elements-hourly-and-processing
  claim: Transit Gateway cost elements include an hourly charge for each attached VPC, Direct Connect or Site-to-Site VPN, and data processing charges for each GB sent from a VPC, Direct Connect or VPN to the transit gateway.
  scope: per attachment-hour and per GB sent to the transit gateway.
  link: [an hourly charge for each attached VPC](../facts/transit-gateway.md#transit-gateway-blog-cost-elements-hourly-and-processing)
  say: hourly per attachment
transit-gateway-blog-cross-region-extra-transfer
  claim: If workload components communicate across Regions with VPC peering or Transit Gateway, additional data transfer charges apply; for VPCs peered across Regions the standard inter-Region data transfer charges apply.
  scope: cross-Region VPC connectivity.
  link: [additional data transfer charges apply](../facts/transit-gateway.md#transit-gateway-blog-cross-region-extra-transfer)
  link: [standard inter-Region data transfer charges will apply](../facts/transit-gateway.md#transit-gateway-blog-cross-region-extra-transfer)
transit-gateway-blog-peered-gateways-one-side-charged
  claim: For peered transit gateways you incur data transfer charges on only one side of the peer, and data transfer charges do not apply for data sent from a peering attachment to a transit gateway.
  scope: AWS Transit Gateway peering.
  link: [data transfer charges on only one side](../facts/transit-gateway.md#transit-gateway-blog-peered-gateways-one-side-charged)
transit-gateway-case-carrier-static-routes-across-regions
  claim: Carrier Global's transit gateway hub-and-spoke network needed static routes for connectivity across multiple Regions, which relied on engineers making manual configuration changes, and the company then re-architected with AWS Cloud WAN.
  scope: Carrier Global.
  link: [required static routes for providing connectivity](../facts/transit-gateway.md#transit-gateway-case-carrier-static-routes-across-regions)
  link: [manual configuration changes](../facts/transit-gateway.md#transit-gateway-case-carrier-static-routes-across-regions)
transit-gateway-centralized-router-scenario
  claim: When all attachments are associated with and propagate to the transit gateway default route table, all attachments can route packets to each other and the transit gateway serves as a simple layer 3 IP router.
  scope: transit gateway centralized router scenario.
  link: [all attachments can route packets to each other](../facts/transit-gateway.md#transit-gateway-centralized-router-scenario)
  link: [simple layer 3 IP router](../facts/transit-gateway.md#transit-gateway-centralized-router-scenario)
transit-gateway-change-bandwidth-limits-added-2023
  claim: The Transit Gateway document history lists AWS Transit Gateway Quotas on August 14, 2023 with the description that bandwidth limits were added; the row gives no earlier bandwidth value.
  link: [August 14, 2023](../facts/transit-gateway.md#transit-gateway-change-bandwidth-limits-added-2023)
  link: [Bandwidth limits were added](../facts/transit-gateway.md#transit-gateway-change-bandwidth-limits-added-2023)
  say: August 2023
transit-gateway-change-client-vpn-attachments-2026
  claim: The Transit Gateway document history lists Client VPN attachments on April 20, 2026: you create a Client VPN attachment to connect a transit gateway to a Client VPN endpoint.
  link: [April 20, 2026](../facts/transit-gateway.md#transit-gateway-change-client-vpn-attachments-2026)
  say: April 2026
transit-gateway-change-client-vpn-native-integration-2026
  claim: On April 23, 2026 AWS announced native Transit Gateway integration for Client VPN: before it, connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC, and the native attachment eliminates the need for that intermediate VPC.
  link: [April 23, 2026](../facts/transit-gateway.md#transit-gateway-change-client-vpn-native-integration-2026)
  link: [eliminates the need for an intermediate VPC](../facts/transit-gateway.md#transit-gateway-change-client-vpn-native-integration-2026)
  say: April 2026
  changed: 2026-04-23: was connecting Client VPN to multiple VPCs required provisioning and managing an intermediate VPC
transit-gateway-change-encryption-support-2025
  claim: The Transit Gateway document history lists Encryption Support for transit gateways on November 20, 2025: managing Encryption Support on transit gateways to enforce encryption-in-transit for all traffic.
  link: [November 20, 2025](../facts/transit-gateway.md#transit-gateway-change-encryption-support-2025)
  say: November 2025
transit-gateway-change-fca-sender-pay-to-flexible-2025
  claim: On November 21, 2025 AWS announced general availability of Flexible Cost Allocation on Transit Gateway; before it, Transit Gateway only used a sender-pay model, where the source attachment account owner was responsible for all data usage related costs.
  link: [November 21, 2025](../facts/transit-gateway.md#transit-gateway-change-fca-sender-pay-to-flexible-2025)
  link: [only used a sender-pay model](../facts/transit-gateway.md#transit-gateway-change-fca-sender-pay-to-flexible-2025)
  say: November 2025 | before, only the sender paid
  changed: 2025-11-21: was Transit Gateway only used a sender-pay model
transit-gateway-change-flexible-cost-allocation-history-2025
  claim: The Transit Gateway document history lists Flexible Cost Allocation on November 20, 2025: you configure flexible cost allocation policies to control how data processing and transfer costs are allocated across your organization.
  link: [November 20, 2025](../facts/transit-gateway.md#transit-gateway-change-flexible-cost-allocation-history-2025)
  say: November 2025
transit-gateway-change-flow-logs-2022
  claim: The Transit Gateway document history lists AWS Transit Gateway Flow Logs on July 14, 2022: transit gateways support Transit Gateway Flow Logs, which let you monitor and log network traffic between transit gateways.
  link: [July 14, 2022](../facts/transit-gateway.md#transit-gateway-change-flow-logs-2022)
  say: July 2022
transit-gateway-change-network-firewall-direct-attachment-2025
  claim: You can create a network function attachment that connects a transit gateway directly to AWS Network Firewall, which eliminates the need to create and manage inspection VPCs; the Transit Gateway document history dates network function attachments to June 16, 2025.
  link: [June 16, 2025](../facts/transit-gateway.md#transit-gateway-change-network-firewall-direct-attachment-2025)
  link: [the need to create and manage inspection VPCs](../facts/transit-gateway.md#transit-gateway-change-network-firewall-direct-attachment-2025)
  say: June 2025
  changed: 2025-06-16: was create and manage inspection VPCs
transit-gateway-change-network-function-attachments-2025
  claim: The Transit Gateway document history lists Network function attachments on June 16, 2025: you create a network function attachment to connect a transit gateway directly to AWS Network Firewall.
  link: [June 16, 2025](../facts/transit-gateway.md#transit-gateway-change-network-function-attachments-2025)
  say: June 2025
transit-gateway-change-pbr-2026
  claim: The Transit Gateway document history lists Policy-Based Routing for transit gateways on July 28, 2026: policy tables forward traffic across a transit gateway based on packet attributes such as source and destination IP addresses, ports, and protocol.
  link: [July 28, 2026](../facts/transit-gateway.md#transit-gateway-change-pbr-2026)
  say: late July 2026
transit-gateway-change-pbr-ga-2026
  claim: On Jul 30, 2026 AWS announced Policy-Based Routing on Transit Gateway: forwarding decisions can use source and destination IP addresses, ports and protocol; before it, customers needing traffic steering or workload isolation had to build multi-VPC architectures with additional routing hops.
  link: [Jul 30, 2026](../facts/transit-gateway.md#transit-gateway-change-pbr-ga-2026)
  link: [rather than destination IP address alone](../facts/transit-gateway.md#transit-gateway-change-pbr-ga-2026)
  say: July 2026
  changed: 2026-07-30: was customers needing traffic steering or workload isolation had to build multi-VPC architectures with additional routing hops
transit-gateway-change-policy-tables-2022
  claim: The Transit Gateway document history lists Transit gateway policy tables on July 13, 2022, described as policy tables that set up dynamic routing for transit gateways, automatically exchanging routing and reachability information with peered transit gateway types.
  link: [July 13, 2022](../facts/transit-gateway.md#transit-gateway-change-policy-tables-2022)
  say: July 2022
transit-gateway-change-security-group-referencing-2024
  claim: The Transit Gateway document history lists Security group referencing support on September 25, 2024: you can now reference a security group across VPCs attached to a transit gateway.
  link: [September 25, 2024](../facts/transit-gateway.md#transit-gateway-change-security-group-referencing-2024)
  say: September 2024
transit-gateway-cidr-block-size
  claim: A transit gateway CIDR block can be a /24 block or larger for IPv4, or a /64 block or larger for IPv6.
  scope: transit gateway CIDR blocks; minimum; not adjustable.
  link: [/24 CIDR block or larger](../facts/transit-gateway.md#transit-gateway-cidr-block-size)
  link: [/64 CIDR block or larger](../facts/transit-gateway.md#transit-gateway-cidr-block-size)
  say: a slash twenty-four block or larger | a slash sixty-four block or larger
transit-gateway-client-vpn-attachment-automatic
  claim: When you associate a Client VPN endpoint with a transit gateway, a Client VPN attachment is created automatically, so traffic can route between your VPCs, on-premises networks and Client VPN endpoints; cross-account Client VPN attachments are supported.
  scope: transit gateway Client VPN attachment.
  link: [a Client VPN attachment is automatically created](../facts/transit-gateway.md#transit-gateway-client-vpn-attachment-automatic)
  link: [supports cross-account Client VPN attachments](../facts/transit-gateway.md#transit-gateway-client-vpn-attachment-automatic)
transit-gateway-client-vpn-attachment-needs-cidr-block
  claim: A transit gateway must have an assigned IPv4 or IPv6 CIDR block before you can create a Client VPN attachment.
  scope: Client VPN attachments.
  link: [assigned IPv4 or IPv6 CIDR block](../facts/transit-gateway.md#transit-gateway-client-vpn-attachment-needs-cidr-block)
transit-gateway-client-vpn-native-integration-no-extra-charge
  claim: The native Client VPN and Transit Gateway announcement states there are no additional charges for this integration beyond the standard pricing of AWS Client VPN and AWS Transit Gateway.
  scope: native Client VPN and Transit Gateway integration.
  link: [no additional charges for this native integration](../facts/transit-gateway.md#transit-gateway-client-vpn-native-integration-no-extra-charge)
transit-gateway-client-vpn-route-propagation-required
  claim: Route table propagation must be enabled for Client VPN attachments to allow traffic between the Client VPN endpoint and the transit gateway.
  scope: transit gateway Client VPN attachment.
  link: [Route table propagation must be enabled](../facts/transit-gateway.md#transit-gateway-client-vpn-route-propagation-required)
transit-gateway-cloudwatch-publishes-tgw-and-attachment
  claim: Amazon VPC publishes data points to Amazon CloudWatch for your transit gateways and for transit gateway attachments.
  scope: AWS Transit Gateway monitoring.
  link: [transit gateways and transit gateway attachments](../facts/transit-gateway.md#transit-gateway-cloudwatch-publishes-tgw-and-attachment)
transit-gateway-connect-peers-20-gbps
  claim: You can create up to 4 Connect peers per Connect attachment, for up to 20 Gbps in total bandwidth per Connect attachment, as long as the underlying transport (VPC or Direct Connect) attachment supports the required bandwidth.
  scope: per Connect attachment; maximum; not adjustable; the underlying transport (VPC or Direct Connect) attachment must support the required bandwidth.
  link: [up to 4 Connect peers per Connect attachment](../facts/transit-gateway.md#transit-gateway-connect-peers-20-gbps)
  link: [up to 20 Gbps in total bandwidth per Connect attachment](../facts/transit-gateway.md#transit-gateway-connect-peers-20-gbps)
  say: up to four Connect peers | up to twenty gigabits per second in total
transit-gateway-create-auto-accept-shared-attachments
  claim: The Auto accept shared attachments option automatically accepts cross-account attachments; without it, the transit gateway owner must accept or reject attachment requests.
  scope: shared transit gateway.
  link: [Auto accept shared attachments](../facts/transit-gateway.md#transit-gateway-create-auto-accept-shared-attachments)
  link: [automatically accept cross-account attachments](../facts/transit-gateway.md#transit-gateway-create-auto-accept-shared-attachments)
transit-gateway-create-default-route-table-association-option
  claim: The Default route table association option automatically associates transit gateway attachments with the default route table of the transit gateway.
  scope: transit gateway creation options.
  link: [automatically associate transit gateway attachments](../facts/transit-gateway.md#transit-gateway-create-default-route-table-association-option)
transit-gateway-create-default-route-table-propagation-option
  claim: The Default route table propagation option automatically propagates transit gateway attachments to the default route table of the transit gateway.
  scope: transit gateway creation options.
  link: [automatically propagate transit gateway attachments](../facts/transit-gateway.md#transit-gateway-create-default-route-table-propagation-option)
transit-gateway-create-dns-support-option
  claim: The DNS support option of a transit gateway lets a VPC resolve public IPv4 DNS host names to private IPv4 addresses when queried from instances in another VPC attached to the same transit gateway.
  scope: transit gateway creation options.
  link: [DNS support](../facts/transit-gateway.md#transit-gateway-create-dns-support-option)
  link: [public IPv4 DNS host names to private IPv4 addresses](../facts/transit-gateway.md#transit-gateway-create-dns-support-option)
transit-gateway-cross-az-internal-routing-no-extra-charge
  claim: If traffic comes from an Availability Zone where the destination attachment is not present, the transit gateway internally routes it to a random Availability Zone where the attachment is present, with no additional transit gateway charge for that cross-zone traffic.
  scope: transit gateway VPC attachment.
  link: [route that traffic to a random Availability Zone](../facts/transit-gateway.md#transit-gateway-cross-az-internal-routing-no-extra-charge)
  link: [no additional transit gateway charge](../facts/transit-gateway.md#transit-gateway-cross-az-internal-routing-no-extra-charge)
transit-gateway-dcg-single-connection-many-vpcs
  claim: Attaching a transit gateway to a Direct Connect gateway through a transit virtual interface lets you manage a single connection for multiple VPCs or VPNs in the same Region.
  scope: transit gateway Direct Connect gateway attachment.
  link: [Direct Connect gateway using a transit virtual interface](../facts/transit-gateway.md#transit-gateway-dcg-single-connection-many-vpcs)
  link: [single connection for multiple VPCs or VPNs](../facts/transit-gateway.md#transit-gateway-dcg-single-connection-many-vpcs)
transit-gateway-decision-guide-cloud-wan-when
  claim: The decision guide suggests AWS Cloud WAN if you want to unify your data center, branch and AWS networks with a WAN, and it is also worth considering if you do not want to manage complex routing configurations or build your own automations for multi-Region connectivity.
  scope: AWS Transit Gateway vs AWS Cloud WAN.
  link: [unify your data center, branch, and AWS networks](../facts/transit-gateway.md#transit-gateway-decision-guide-cloud-wan-when)
  link: [build your own automations for multi-Region connectivity](../facts/transit-gateway.md#transit-gateway-decision-guide-cloud-wan-when)
transit-gateway-decision-guide-suited-for-connecting-vpcs
  claim: The networking decision guide names AWS Cloud WAN and AWS Transit Gateway as examples of services suited for connecting workloads that run in VPCs.
  scope: AWS networking decision guide.
  link: [AWS Cloud WAN and AWS Transit Gateway](../facts/transit-gateway.md#transit-gateway-decision-guide-suited-for-connecting-vpcs)
transit-gateway-def-network-transit-hub
  claim: AWS Transit Gateway is a network transit hub that interconnects VPCs and on-premises networks.
  scope: AWS Transit Gateway.
  link: [a network transit hub](../facts/transit-gateway.md#transit-gateway-def-network-transit-hub)
  link: [interconnect virtual private clouds (VPCs) and on-premises networks](../facts/transit-gateway.md#transit-gateway-def-network-transit-hub)
transit-gateway-default-route-table-association-propagation
  claim: A transit gateway automatically comes with a default route table that is, by default, both the default association route table and the default propagation route table; if you disable both route propagation and route table association, AWS does not create a default route table.
  scope: transit gateway route tables; default; not adjustable; No default route table is created when both route propagation and route table association are disabled..
  link: [automatically comes with a default route table](../facts/transit-gateway.md#transit-gateway-default-route-table-association-propagation)
  link: [default association route table](../facts/transit-gateway.md#transit-gateway-default-route-table-association-propagation)
  link: [default propagation route table](../facts/transit-gateway.md#transit-gateway-default-route-table-association-propagation)
transit-gateway-ecmp-connect-automatic
  claim: Transit Gateway Connect attachments automatically support ECMP.
  scope: transit gateway ECMP.
  link: [automatically support ECMP](../facts/transit-gateway.md#transit-gateway-ecmp-connect-automatic)
transit-gateway-ecmp-dx-gateway-same-prefix
  claim: Direct Connect gateway attachments automatically support ECMP across multiple Direct Connect gateway attachments when the network prefix, prefix length and AS_PATH are exactly the same.
  scope: transit gateway ECMP.
  link: [automatically support ECMP across multiple](../facts/transit-gateway.md#transit-gateway-ecmp-dx-gateway-same-prefix)
  link: [prefix length, and AS\_PATH are exactly the same](../facts/transit-gateway.md#transit-gateway-ecmp-dx-gateway-same-prefix)
transit-gateway-ecmp-not-across-attachment-types
  claim: ECMP is not supported between different attachment types, for example between a VPN and a VPC attachment; the transit gateway instead evaluates its routes and routes traffic by the evaluated route.
  scope: transit gateway ECMP.
  link: [not supported between different attachment types](../facts/transit-gateway.md#transit-gateway-ecmp-not-across-attachment-types)
  link: [between a VPN and a VPC attachment](../facts/transit-gateway.md#transit-gateway-ecmp-not-across-attachment-types)
transit-gateway-ecmp-peering-not-supported
  claim: Transit gateway peering does not support ECMP, because it supports no dynamic routing and you cannot configure the same static route against two different targets.
  scope: transit gateway ECMP.
  link: [Transit gateway peering does not support ECMP](../facts/transit-gateway.md#transit-gateway-ecmp-peering-not-supported)
transit-gateway-ecmp-vpc-not-supported
  claim: A transit gateway does not support ECMP for VPC attachments, because VPC CIDR blocks cannot overlap, so you cannot attach a VPC and a second VPC with the same CIDR and load balance traffic between them.
  scope: transit gateway ECMP.
  link: [VPC does not support ECMP](../facts/transit-gateway.md#transit-gateway-ecmp-vpc-not-supported)
  link: [CIDR blocks cannot overlap](../facts/transit-gateway.md#transit-gateway-ecmp-vpc-not-supported)
transit-gateway-ecmp-vpn-concentrator-not-supported
  claim: A VPN Concentrator attachment does not support ECMP.
  scope: transit gateway ECMP.
  link: [VPN Concentrator does not support ECMP](../facts/transit-gateway.md#transit-gateway-ecmp-vpn-concentrator-not-supported)
transit-gateway-ecmp-vpn-dynamic-routing-only
  claim: ECMP across VPN tunnels on a transit gateway needs a VPN connection configured for dynamic routing; ECMP is not supported on VPN connections that use static routing.
  scope: Site-to-Site VPN connections attached to a transit gateway.
  link: [configured for dynamic routing](../facts/transit-gateway.md#transit-gateway-ecmp-vpn-dynamic-routing-only)
  link: [not supported on VPN connections](../facts/transit-gateway.md#transit-gateway-ecmp-vpn-dynamic-routing-only)
  say: dynamic routing is required
transit-gateway-ecmp-vpn-optional
  claim: A transit gateway supports ECMP for most attachments, and for a VPN attachment you can enable or disable ECMP support when you create or modify the transit gateway.
  scope: transit gateway ECMP.
  link: [Equal Cost Multipath (ECMP) routing for most attachments](../facts/transit-gateway.md#transit-gateway-ecmp-vpn-optional)
  link: [enable or disable ECMP support](../facts/transit-gateway.md#transit-gateway-ecmp-vpn-optional)
transit-gateway-elastic-layer-3-router
  claim: A transit gateway scales elastically with the volume of network traffic, and routing through it works at layer 3, sending each packet to a next-hop attachment based on the destination IP address.
  scope: AWS Transit Gateway.
  link: [scales elastically](../facts/transit-gateway.md#transit-gateway-elastic-layer-3-router)
  link: [operates at layer 3](../facts/transit-gateway.md#transit-gateway-elastic-layer-3-router)
transit-gateway-enable-multiple-azs
  claim: When you attach a VPC to a transit gateway, you must enable one or more Availability Zones for the attachment, and AWS recommends that you enable multiple Availability Zones to ensure availability.
  scope: transit gateway VPC attachment.
  link: [enable multiple Availability Zones to ensure availability](../facts/transit-gateway.md#transit-gateway-enable-multiple-azs)
transit-gateway-enable-propagation-for-dx-and-bgp-vpn
  claim: Enable route propagation for Direct Connect gateway attachments and BGP Site-to-Site VPN attachments.
  scope: AWS Transit Gateway design.
  link: [Enable route propagation](../facts/transit-gateway.md#transit-gateway-enable-propagation-for-dx-and-bgp-vpn)
  link: [BGP Site-to-Site VPN attachments](../facts/transit-gateway.md#transit-gateway-enable-propagation-for-dx-and-bgp-vpn)
transit-gateway-encryption-enabling-up-to-14-days
  claim: While a transit gateway is in the enabling encryption state, the process can take up to 14 days to complete.
  scope: per transit gateway, enabling encryption support; maximum; not adjustable.
  link: [up to 14 days](../facts/transit-gateway.md#transit-gateway-encryption-enabling-up-to-14-days)
  say: up to fourteen days
transit-gateway-encryption-only-on-existing-gateway
  claim: You can add encryption support only to an existing transit gateway, not while you are creating one.
  scope: per transit gateway.
  link: [encryption support to an existing transit gateway](../facts/transit-gateway.md#transit-gateway-encryption-only-on-existing-gateway)
transit-gateway-encryption-support-enforces-in-transit
  claim: Encryption Support on a transit gateway lets you enforce encryption-in-transit for traffic between VPCs attached to the transit gateway; you activate it manually with the modify-transit-gateway command.
  scope: per transit gateway.
  link: [enforce encryption-in-transit for traffic between VPCs](../facts/transit-gateway.md#transit-gateway-encryption-support-enforces-in-transit)
transit-gateway-encryption-support-unsupported-features
  claim: Connect attachments, peering attachments, Network Firewall attachments, VPN Concentrator attachments, Client VPN attachments, security group references and multicast features are not supported with Encryption Support.
  scope: a transit gateway with Encryption Support enabled.
  link: [not supported with Encryption Support](../facts/transit-gateway.md#transit-gateway-encryption-support-unsupported-features)
transit-gateway-faq-connect-no-static-routes
  claim: Transit Gateway Connect does not support static routes; BGP is a minimum requirement.
  scope: Transit Gateway Connect attachments.
  link: [BGP is a minimum requirement](../facts/transit-gateway.md#transit-gateway-faq-connect-no-static-routes)
  say: Connect needs BGP
transit-gateway-faq-connect-sdwan
  claim: AWS Transit Gateway Connect is a feature of AWS Transit Gateway that simplifies branch connectivity through native integration of SD-WAN network virtual appliances into the transit gateway.
  link: [native integration of SD-WAN](../facts/transit-gateway.md#transit-gateway-faq-connect-sdwan)
  say: it plugs SD-WAN appliances into the transit gateway
transit-gateway-faq-default-association
  claim: By default, VPC, VPN, Direct Connect gateway, Transit Gateway Connect and peered transit gateway attachments are associated with the default route table of the transit gateway; you can create additional route tables and associate these attachments with them.
  scope: per attachment on a transit gateway; default; adjustable; You can create additional route tables and associate attachments with them..
  link: [associated to the default route table](../facts/transit-gateway.md#transit-gateway-faq-default-association)
  say: they use the default route table
transit-gateway-faq-dx-gateway-cross-account
  claim: A transit gateway can be associated with a Direct Connect gateway from a different AWS account; only the transit gateway owner can create the association, and AWS Resource Access Manager cannot be used for it.
  scope: association of a transit gateway with a Direct Connect gateway.
  link: [Only the owner of the AWS Transit Gateway](../facts/transit-gateway.md#transit-gateway-faq-dx-gateway-cross-account)
  link: [You cannot use Resource Access Manager](../facts/transit-gateway.md#transit-gateway-faq-dx-gateway-cross-account)
  say: only the transit gateway owner | RAM cannot do this
transit-gateway-faq-dx-gateway-different-asn
  claim: You cannot use the same ASN for a transit gateway and the Direct Connect gateway it is associated with.
  scope: association of a transit gateway with a Direct Connect gateway.
  link: [you cannot use the same ASN](../facts/transit-gateway.md#transit-gateway-faq-dx-gateway-different-asn)
  say: they need different ASNs
transit-gateway-faq-encryption-enforce-peering-or-tgw
  claim: VPCs running in enforce mode can be connected with VPC peering or a transit gateway to guarantee end-to-end encryption.
  link: [VPC Peering or Transit Gateway](../facts/transit-gateway.md#transit-gateway-faq-encryption-enforce-peering-or-tgw)
  say: peering or a transit gateway
transit-gateway-faq-encryption-enforce-vpcs-end-to-end
  claim: Traffic between two VPCs in enforce mode, without exclusions, is end-to-end encrypted through the transit gateway; encryption on the transit gateway also lets you connect two VPCs that are in different Encryption Controls modes.
  scope: per pair of VPCs through a transit gateway; both VPCs are in enforce mode without exclusions.
  link: [end-to-end encrypted via the TGW](../facts/transit-gateway.md#transit-gateway-faq-encryption-enforce-vpcs-end-to-end)
  say: encrypted end to end through the transit gateway
transit-gateway-faq-encryption-incremental-migration
  claim: A transit gateway supports incremental migration of VPCs to encryption by handling both encrypted and unencrypted traffic during the transition.
  link: [TGW supports incremental migration](../facts/transit-gateway.md#transit-gateway-faq-encryption-incremental-migration)
  say: you can migrate step by step
transit-gateway-faq-encryption-non-disruptive
  claim: Enabling encryption on an existing transit gateway does not disrupt existing traffic flows, and VPC attachments migrate to encrypted lanes seamlessly and automatically.
  scope: per transit gateway.
  link: [non-disruptive to existing traffic flows](../facts/transit-gateway.md#transit-gateway-faq-encryption-non-disruptive)
  say: no disruption
transit-gateway-faq-encryption-same-region
  claim: The FAQ answer on end-to-end encryption between VPCs connected through a transit gateway with encryption support states that all VPCs must be in the same Region.
  scope: per transit gateway with encryption support.
  link: [All VPCs must be in the same region](../facts/transit-gateway.md#transit-gateway-faq-encryption-same-region)
  say: same Region
transit-gateway-faq-encryption-support-explicit
  claim: VPCs that have encryption controls enabled can use VPC peering or a transit gateway to encrypt traffic between them; on a transit gateway you must turn on encryption support explicitly, in the console or with the modify-transit-gateway command.
  scope: per transit gateway.
  link: [turn on encryption support explicitly](../facts/transit-gateway.md#transit-gateway-faq-encryption-support-explicit)
  say: turn encryption support on yourself
transit-gateway-faq-encryption-to-non-enforced-vpc
  claim: An encryption-enforced VPC can connect to a non-enforced VPC through a transit gateway; the traffic stays encrypted from the source until the transit gateway attachment in the destination VPC, whatever the encryption status of the destination VPC.
  link: [encrypted from the source until the TGW attachment](../facts/transit-gateway.md#transit-gateway-faq-encryption-to-non-enforced-vpc)
  say: encrypted up to the destination attachment
transit-gateway-faq-identical-cidr-not-routed
  claim: A transit gateway does not support routing between VPCs with identical CIDRs; if you attach a VPC whose CIDR is identical to an already attached VPC, its route is not propagated into the transit gateway route table.
  scope: transit gateway VPC attachments (FAQ answer on identical CIDRs).
  link: [identical CIDRs](../facts/transit-gateway.md#transit-gateway-faq-identical-cidr-not-routed)
  say: same CIDR ranges
transit-gateway-faq-limits-in-docs-support-case
  claim: The Transit Gateway FAQ says details on limits and quotas are in the AWS documentation, and that to exceed these limits you create a support case.
  link: [please create a support case](../facts/transit-gateway.md#transit-gateway-faq-limits-in-docs-support-case)
  say: open a support case
transit-gateway-faq-multicast-attachment-types
  claim: Multicast traffic can be routed within and between VPC attachments to a transit gateway; multicast routing is not supported over Direct Connect, Site-to-Site VPN and peering attachments.
  scope: transit gateway multicast routing.
  link: [within and between VPC attachments](../facts/transit-gateway.md#transit-gateway-faq-multicast-attachment-types)
  say: only VPC attachments
transit-gateway-faq-multiple-route-tables-optional
  claim: A transit gateway has a default route table, and using multiple route tables is optional.
  scope: per transit gateway.
  link: [The use of multiple route tables is optional](../facts/transit-gateway.md#transit-gateway-faq-multiple-route-tables-optional)
  say: extra route tables are optional
transit-gateway-faq-network-manager-what
  claim: AWS Transit Gateway Network Manager is a feature of AWS Transit Gateway that centralizes management and monitoring of networking resources and connections to remote branch locations.
  link: [centralizes management and monitoring of networking resources](../facts/transit-gateway.md#transit-gateway-faq-network-manager-what)
  say: one place to manage and monitor the network
transit-gateway-faq-no-propagation-to-vpc-route-table
  claim: Routes in the transit gateway route table are not propagated to the route table of the VPC; the VPC owner must create a static route in the VPC route table to send traffic to the transit gateway.
  scope: route tables of VPCs attached to a transit gateway.
  link: [needs to create a static route](../facts/transit-gateway.md#transit-gateway-faq-no-propagation-to-vpc-route-table)
  say: the VPC owner adds a static route
transit-gateway-faq-onprem-routes-bgp
  claim: When you connect a VPN or a Direct Connect gateway, routes propagate between the transit gateway and your on-premises router using BGP.
  link: [using Border Gateway Protocol (BGP)](../facts/transit-gateway.md#transit-gateway-faq-onprem-routes-bgp)
  say: with BGP
transit-gateway-faq-peering-attachment-static-routes
  claim: Peering attachments between transit gateways do not support route propagation; you must create static routes in the transit gateway route tables to send traffic over peering attachments.
  scope: transit gateway peering attachments.
  link: [do not support route propagation](../facts/transit-gateway.md#transit-gateway-faq-peering-attachment-static-routes)
  say: peering needs static routes
transit-gateway-faq-route-next-hop
  claim: Transit gateway routes decide the next hop from the destination IP address of the packet, and a route can point to a VPC, a VPN connection, a Direct Connect gateway, a Transit Gateway Connect attachment or a peered transit gateway.
  link: [next hop depending on the destination IP address](../facts/transit-gateway.md#transit-gateway-faq-route-next-hop)
  say: by destination IP address
transit-gateway-faq-route-tables-segment
  claim: You can segment a transit gateway network by creating multiple route tables and associating VPCs and VPNs with them; this makes isolated networks inside the transit gateway, similar to virtual routing and forwarding (VRFs) in traditional networks.
  scope: per transit gateway.
  link: [creating multiple route tables](../facts/transit-gateway.md#transit-gateway-faq-route-tables-segment)
  say: use several route tables
transit-gateway-faq-static-and-dynamic-routing
  claim: AWS Transit Gateway supports dynamic and static routing between attached VPCs and VPNs.
  link: [dynamic and static routing](../facts/transit-gateway.md#transit-gateway-faq-static-and-dynamic-routing)
  say: dynamic and static routes
transit-gateway-faq-vpc-cidr-propagation-not-bgp
  claim: When you attach a VPC to a transit gateway or resize an attached VPC, the VPC CIDR propagates into the transit gateway route table using internal APIs, not BGP.
  scope: VPC attachments of a transit gateway.
  link: [using internal APIs (not BGP)](../facts/transit-gateway.md#transit-gateway-faq-vpc-cidr-propagation-not-bgp)
  say: by internal APIs, not BGP
transit-gateway-fca-allocation-options-default-source
  claim: By default a transit gateway allocates data processing charges to the account that owns the source attachment; with Flexible Cost Allocation (announced November 21, 2025) you can create metering policies whose rules instead charge the account that owns the destination attachment or the account that owns the transit gateway.
  scope: transit gateway data processing charges; default; adjustable; a metering policy rule can name the source attachment owner, the destination attachment owner or the transit gateway owner.
  link: [account that owns the source attachment](../facts/transit-gateway.md#transit-gateway-fca-allocation-options-default-source)
  link: [owns the destination attachment](../facts/transit-gateway.md#transit-gateway-fca-allocation-options-default-source)
  link: [owns the transit gateway](../facts/transit-gateway.md#transit-gateway-fca-allocation-options-default-source)
  say: the source attachment owner pays by default | the destination attachment owner | the transit gateway owner
  changed: 2025-11-21: was Transit Gateway only used a sender-pay model
transit-gateway-fca-no-additional-charge
  claim: The Flexible Cost Allocation announcement states there is no additional charge for using FCA on Transit Gateway.
  scope: Flexible Cost Allocation (FCA).
  link: [no additional charge for using FCA](../facts/transit-gateway.md#transit-gateway-fca-no-additional-charge)
transit-gateway-flow-logs-destinations
  claim: Transit Gateway Flow Logs capture information about IP traffic going to and from your transit gateways, and the data can be published to Amazon CloudWatch Logs, Amazon S3 or Firehose.
  scope: AWS Transit Gateway Flow Logs.
  link: [Amazon CloudWatch Logs, Amazon S3, or Firehose](../facts/transit-gateway.md#transit-gateway-flow-logs-destinations)
  link: [IP traffic going to and from](../facts/transit-gateway.md#transit-gateway-flow-logs-destinations)
transit-gateway-flow-logs-no-performance-impact
  claim: Transit Gateway Flow Log data is collected outside the path of network traffic, so it does not affect network throughput or latency.
  scope: AWS Transit Gateway Flow Logs.
  link: [collected outside of the path](../facts/transit-gateway.md#transit-gateway-flow-logs-no-performance-impact)
  link: [does not affect network throughput or latency](../facts/transit-gateway.md#transit-gateway-flow-logs-no-performance-impact)
transit-gateway-ha-by-design-single-per-region
  claim: You do not need additional transit gateways for high availability because transit gateways are highly available by design; for redundancy and disaster recovery, use a single transit gateway in each Region.
  scope: AWS Transit Gateway design.
  link: [highly available by design](../facts/transit-gateway.md#transit-gateway-ha-by-design-single-per-region)
  link: [single transit gateway in each Region](../facts/transit-gateway.md#transit-gateway-ha-by-design-single-per-region)
transit-gateway-hub-and-spoke-managed
  claim: AWS Transit Gateway provides a hub and spoke design for connecting VPCs and on-premises networks as a fully managed service, with no third-party virtual appliances to provision and no VPN overlay required.
  scope: AWS Transit Gateway.
  link: [hub and spoke design](../facts/transit-gateway.md#transit-gateway-hub-and-spoke-managed)
  link: [No VPN overlay is required](../facts/transit-gateway.md#transit-gateway-hub-and-spoke-managed)
transit-gateway-hybrid-dx-regional-routers
  claim: A transit virtual interface attachment to a Direct Connect gateway enables your network to connect several regional centralized routers (transit gateways) over a private dedicated connection.
  scope: Direct Connect with AWS Transit Gateway.
  link: [several regional centralized routers](../facts/transit-gateway.md#transit-gateway-hybrid-dx-regional-routers)
transit-gateway-hybrid-vpn-managed-endpoint-many-vpcs
  claim: A Site-to-Site VPN attachment on a transit gateway is an AWS-managed VPN endpoint that connects to multiple VPCs in the same Region without the cost and management of a separate IPsec VPN connection to each VPC.
  scope: Site-to-Site VPN with AWS Transit Gateway.
  link: [AWS-managed VPN endpoint for connecting to multiple VPCs](../facts/transit-gateway.md#transit-gateway-hybrid-vpn-managed-endpoint-many-vpcs)
  link: [without the additional cost and management](../facts/transit-gateway.md#transit-gateway-hybrid-vpn-managed-endpoint-many-vpcs)
transit-gateway-inspection-appliance-mode-stateful-firewall
  claim: With a transit gateway in a centralized inspection design, traffic returns to the transit gateway in the same Availability Zone after AWS Network Firewall inspects it, which the transit gateway's appliance mode makes possible and which gives Network Firewall stateful inspection inside the security VPC.
  scope: centralized inspection with a transit gateway.
  link: [possible due to the appliance mode feature](../facts/transit-gateway.md#transit-gateway-inspection-appliance-mode-stateful-firewall)
  link: [stateful traffic inspection capability](../facts/transit-gateway.md#transit-gateway-inspection-appliance-mode-stateful-firewall)
transit-gateway-inspection-be-selective-zones
  claim: To reduce cost, be selective about which traffic passes through AWS Network Firewall or Gateway Load Balancer, for example by defining security zones and inspecting traffic between untrusted zones.
  scope: centralized inspection with a transit gateway.
  link: [be selective in what traffic passes](../facts/transit-gateway.md#transit-gateway-inspection-be-selective-zones)
  link: [inspect traffic between untrusted zones](../facts/transit-gateway.md#transit-gateway-inspection-be-selective-zones)
transit-gateway-inspection-gwlb-appliance-mode-east-west
  claim: Appliance mode should be enabled on the transit gateway when doing east-west inspection with Gateway Load Balancer, because Gateway Load Balancer endpoints are a routable target for traffic to and from the transit gateway and appliance mode ensures flow symmetry.
  scope: centralized inspection with a transit gateway.
  link: [Appliance mode should be enabled](../facts/transit-gateway.md#transit-gateway-inspection-gwlb-appliance-mode-east-west)
  link: [To ensure flow symmetry, appliance mode is enabled](../facts/transit-gateway.md#transit-gateway-inspection-gwlb-appliance-mode-east-west)
transit-gateway-inspection-gwlb-az-affinity-default
  claim: By default each Gateway Load Balancer in an Availability Zone distributes traffic only across the registered targets in the same zone (Availability Zone affinity), and with cross-zone load balancing enabled it distributes across all healthy targets in all enabled zones.
  scope: Gateway Load Balancer; default; not adjustable.
  link: [Availability Zone affinity](../facts/transit-gateway.md#transit-gateway-inspection-gwlb-az-affinity-default)
  link: [distributes traffic across all registered and healthy targets](../facts/transit-gateway.md#transit-gateway-inspection-gwlb-az-affinity-default)
transit-gateway-inspection-local-region-inspection-vpcs
  claim: For multi-Region deployments AWS recommends separate inspection VPCs in each local Region, inspecting traffic locally instead of centralizing inspection in another Region, to avoid inter-Region dependencies and data transfer costs.
  scope: centralized inspection with a transit gateway.
  link: [separate inspection VPCs in the respective local](../facts/transit-gateway.md#transit-gateway-inspection-local-region-inspection-vpcs)
transit-gateway-isolated-shared-services-scenario
  claim: In the isolated VPCs with shared services scenario, attachments of each isolated group can route packets to and receive packets from the shared services; use it when groups need to be isolated from each other but use a shared service such as a production system.
  scope: transit gateway isolated VPCs with shared services scenario.
  link: [route packets to or receive packets from](../facts/transit-gateway.md#transit-gateway-isolated-shared-services-scenario)
  link: [groups that need to be isolated](../facts/transit-gateway.md#transit-gateway-isolated-shared-services-scenario)
transit-gateway-isolated-vpcs-blocked-no-route
  claim: In the isolated VPCs scenario, a packet from one VPC to a subnet in another VPC reaches the transit gateway and is blocked because the transit gateway route table has no route for it.
  scope: transit gateway isolated VPCs scenario.
  link: [blocked because there is no route](../facts/transit-gateway.md#transit-gateway-isolated-vpcs-blocked-no-route)
transit-gateway-isolated-vpcs-scenario
  claim: With a transit gateway configured as multiple isolated routers, each with its own route table, attachments of one isolated router can route packets to each other but cannot route packets to or receive packets from attachments of another isolated router.
  scope: transit gateway isolated VPCs scenario.
  link: [each isolated router has a single route table](../facts/transit-gateway.md#transit-gateway-isolated-vpcs-scenario)
  link: [cannot route packets to or receive packets](../facts/transit-gateway.md#transit-gateway-isolated-vpcs-scenario)
transit-gateway-keep-attachment-subnet-nacl-open
  claim: Create one network ACL for all subnets associated with the transit gateway and keep it open in both the inbound and outbound directions.
  scope: transit gateway attachment subnets.
  link: [Keep the network ACL open](../facts/transit-gateway.md#transit-gateway-keep-attachment-subnet-nacl-open)
  link: [both the inbound and outbound directions](../facts/transit-gateway.md#transit-gateway-keep-attachment-subnet-nacl-open)
transit-gateway-limit-route-tables
  claim: Limit the number of transit gateway route tables unless your design requires multiple route tables.
  scope: AWS Transit Gateway design.
  link: [Limit the number of transit gateway route tables](../facts/transit-gateway.md#transit-gateway-limit-route-tables)
transit-gateway-metering-policy-max-10-middlebox
  claim: A metering policy can name a maximum of 10 middlebox attachments.
  scope: per transit gateway metering policy; maximum; not adjustable; the page does not say whether the maximum can be raised.
  link: [maximum of 10 middlebox attachments](../facts/transit-gateway.md#transit-gateway-metering-policy-max-10-middlebox)
  say: a maximum of ten middlebox attachments
transit-gateway-metering-policy-max-50-entries
  claim: A flexible cost allocation metering policy can contain up to 50 entries, evaluated in order from lowest to highest rule number.
  scope: per metering policy; maximum; not adjustable; the page does not say whether the maximum can be raised.
  link: [up to 50 entries](../facts/transit-gateway.md#transit-gateway-metering-policy-max-50-entries)
  say: up to fifty entries
transit-gateway-metering-policy-one-per-gateway
  claim: Each transit gateway can have only one metering policy.
  scope: per transit gateway; maximum; not adjustable.
  link: [only one metering policy](../facts/transit-gateway.md#transit-gateway-metering-policy-one-per-gateway)
  say: only one metering policy
transit-gateway-metric-bytesin-sum
  claim: The transit gateway CloudWatch metric BytesIn is the number of bytes received by the transit gateway, and the only meaningful statistic is Sum.
  scope: AWS/TransitGateway metrics.
  link: [BytesIn](../facts/transit-gateway.md#transit-gateway-metric-bytesin-sum)
  link: [The only meaningful statistic is `Sum`](../facts/transit-gateway.md#transit-gateway-metric-bytesin-sum)
transit-gateway-metric-packetdropcountblackhole
  claim: The transit gateway CloudWatch metric PacketDropCountBlackhole is the number of packets dropped because they matched a blackhole route, and the only meaningful statistic is Sum.
  scope: AWS/TransitGateway metrics.
  link: [PacketDropCountBlackhole](../facts/transit-gateway.md#transit-gateway-metric-packetdropcountblackhole)
  link: [matched a `blackhole` route](../facts/transit-gateway.md#transit-gateway-metric-packetdropcountblackhole)
transit-gateway-metric-packetdropcountnoroute
  claim: The transit gateway CloudWatch metric PacketDropCountNoRoute is the number of packets dropped because they did not match a route, and the only meaningful statistic is Sum.
  scope: AWS/TransitGateway metrics.
  link: [PacketDropCountNoRoute](../facts/transit-gateway.md#transit-gateway-metric-packetdropcountnoroute)
  link: [did not match a route](../facts/transit-gateway.md#transit-gateway-metric-packetdropcountnoroute)
transit-gateway-mss-clamping-all-packets
  claim: A transit gateway enforces Maximum Segment Size (MSS) clamping for all packets.
  scope: all packets through a transit gateway.
  link: [Maximum Segment Size (MSS) clamping](../facts/transit-gateway.md#transit-gateway-mss-clamping-all-packets)
transit-gateway-mtu-8500-bytes
  claim: A transit gateway supports an MTU of 8500 bytes for traffic between VPCs, Direct Connect, Transit Gateway Connect and peering attachments, including intra-Region, inter-Region and Cloud WAN peering attachments.
  scope: traffic between VPCs, Direct Connect, Connect and peering attachments; maximum; not adjustable.
  link: [MTU of 8500 bytes](../facts/transit-gateway.md#transit-gateway-mtu-8500-bytes)
  say: an M T U of eighty-five hundred bytes
transit-gateway-mtu-mismatch-peering-migration
  claim: When you migrate from VPC peering to a transit gateway, an MTU size mismatch between VPC peering and the transit gateway might drop some asymmetric traffic packets; the page says to update both VPCs at the same time to avoid dropped jumbo packets.
  scope: migration from VPC peering to a transit gateway.
  link: [MTU size mismatch](../facts/transit-gateway.md#transit-gateway-mtu-mismatch-peering-migration)
  link: [Update both VPCs at the same time](../facts/transit-gateway.md#transit-gateway-mtu-mismatch-peering-migration)
  say: an M T U size mismatch
transit-gateway-mtu-vpn-1500-bytes
  claim: Traffic over VPN connections on a transit gateway can have an MTU of 1500 bytes.
  scope: VPN connections attached to a transit gateway; maximum; not adjustable.
  link: [MTU of 1500 bytes](../facts/transit-gateway.md#transit-gateway-mtu-vpn-1500-bytes)
  say: an M T U of fifteen hundred bytes
transit-gateway-multicast-igmpv2-and-static
  claim: AWS supports the IGMPv2 protocol and both IGMP and static (API-based) group membership multicast domains on a transit gateway.
  scope: transit gateway multicast.
  link: [supports the IGMPv2 protocol](../facts/transit-gateway.md#transit-gateway-multicast-igmpv2-and-static)
  link: [static (API-based) group membership](../facts/transit-gateway.md#transit-gateway-multicast-igmpv2-and-static)
transit-gateway-multicast-overview
  claim: A transit gateway supports routing multicast traffic between subnets of attached VPCs and serves as a multicast router for instances that send traffic to multiple receiving instances.
  scope: transit gateway multicast.
  link: [routing multicast traffic between subnets of attached VPCs](../facts/transit-gateway.md#transit-gateway-multicast-overview)
  link: [serves as a multicast router](../facts/transit-gateway.md#transit-gateway-multicast-overview)
transit-gateway-nacl-same-subnet-one-acl
  claim: When EC2 instances and a transit gateway association are in the same subnet, the same network ACL is used for traffic from the instances to the transit gateway and for traffic from the transit gateway to the instances.
  scope: transit gateway network ACLs.
  link: [The same network ACL is used for both](../facts/transit-gateway.md#transit-gateway-nacl-same-subnet-one-acl)
transit-gateway-network-function-appliance-mode-automatic
  claim: A Network Firewall attachment on a transit gateway is created with appliance mode automatically enabled, which eliminates the need to explicitly manage inspection VPCs.
  scope: Network Firewall attachments.
  link: [created with appliance mode automatically enabled](../facts/transit-gateway.md#transit-gateway-network-function-appliance-mode-automatic)
transit-gateway-network-function-attachment-firewall
  claim: A network function attachment connects a transit gateway directly to AWS Network Firewall, which removes the need to create and manage inspection VPCs.
  scope: transit gateway network function attachment.
  link: [network function attachment](../facts/transit-gateway.md#transit-gateway-network-function-attachment-firewall)
  link: [eliminates the need to create and manage](../facts/transit-gateway.md#transit-gateway-network-function-attachment-firewall)
transit-gateway-network-function-static-routing-only
  claim: A transit gateway supports only static routing on Network Firewall attachments, and third-party firewalls are not supported on them.
  scope: transit gateway network function attachment.
  link: [supports only static routing on Network Firewall attachments](../facts/transit-gateway.md#transit-gateway-network-function-static-routing-only)
transit-gateway-network-services-account-ram
  claim: AWS recommends placing the organization's transit gateway in its Network Services account for centralized management and using AWS RAM to share it for connecting VPCs across accounts of the organization within the same Region.
  scope: AWS Transit Gateway design.
  link: [Network Services account](../facts/transit-gateway.md#transit-gateway-network-services-account-ram)
  link: [Use AWS Resource Access Manager (RAM) to share](../facts/transit-gateway.md#transit-gateway-network-services-account-ram)
transit-gateway-nfw-subnets-only-endpoints
  claim: In the whitepaper's centralized inspection design with Transit Gateway, AWS Network Firewall is deployed in a separate security VPC that has two subnets in each Availability Zone, one dedicated to the Transit Gateway attachment and one to the firewall endpoint; the whitepaper says the subnets in this VPC should only contain Network Firewall endpoints because Network Firewall can't inspect traffic in the same subnets as the endpoints.
  scope: centralized inspection with Network Firewall and Transit Gateway (whitepaper design).
  link: [can't inspect traffic in the same subnets](../facts/transit-gateway.md#transit-gateway-nfw-subnets-only-endpoints)
transit-gateway-no-default-table-if-both-disabled
  claim: If you disable both route propagation and route table association, AWS does not create a default route table for the transit gateway; if either is enabled, AWS creates one.
  scope: transit gateway route tables.
  link: [disable both route propagation and route table association](../facts/transit-gateway.md#transit-gateway-no-default-table-if-both-disabled)
transit-gateway-no-pmtud-vpn-dx-peering
  claim: Transit gateways do not support Path MTU Discovery on Site-to-Site VPN, Direct Connect and peering attachments.
  scope: Site-to-Site VPN, Direct Connect and peering attachments.
  link: [does not support PMTUD on Site-to-site VPN](../facts/transit-gateway.md#transit-gateway-no-pmtud-vpn-dx-peering)
transit-gateway-no-private-hosted-zone-resolution
  claim: A transit gateway does not support DNS resolution for the custom DNS names of attached VPCs that are set up with Amazon Route 53 private hosted zones.
  scope: transit gateway VPC attachment.
  link: [does not support DNS resolution](../facts/transit-gateway.md#transit-gateway-no-private-hosted-zone-resolution)
  link: [custom DNS names of attached VPCs](../facts/transit-gateway.md#transit-gateway-no-private-hosted-zone-resolution)
transit-gateway-no-routing-identical-or-overlapping-cidr
  claim: A transit gateway does not support routing between VPCs with identical or overlapping CIDRs: if a newly attached VPC has a CIDR identical to or overlapping an attached VPC, its routes are not propagated to the transit gateway route table.
  scope: transit gateway VPC attachment.
  link: [doesn't support routing between VPCs with identical CIDRs](../facts/transit-gateway.md#transit-gateway-no-routing-identical-or-overlapping-cidr)
  link: [aren't propagated to the transit gateway route table](../facts/transit-gateway.md#transit-gateway-no-routing-identical-or-overlapping-cidr)
transit-gateway-one-per-region-isolate-with-route-tables
  claim: Typically one transit gateway can connect all VPCs in a Region, with transit gateway route tables isolating them where needed; multiple gateways are valid to limit misconfiguration blast radius, separate control plane operations and ease administration.
  scope: AWS Transit Gateway design.
  link: [use just one Transit Gateway instance](../facts/transit-gateway.md#transit-gateway-one-per-region-isolate-with-route-tables)
  link: [limit misconﬁguration blast radius](../facts/transit-gateway.md#transit-gateway-one-per-region-isolate-with-route-tables)
transit-gateway-one-vpc-attachment-per-vpc
  claim: A transit gateway cannot have more than one VPC attachment to the same VPC.
  scope: per transit gateway, per VPC.
  link: [one VPC attachment to the same VPC](../facts/transit-gateway.md#transit-gateway-one-vpc-attachment-per-vpc)
  say: only one VPC attachment per VPC
transit-gateway-pbr-no-additional-charge
  claim: Policy-Based Routing for Transit Gateway is available at no additional charge beyond standard transit gateway fees.
  scope: Policy-Based Routing.
  link: [no additional charge beyond standard transit gateway fees](../facts/transit-gateway.md#transit-gateway-pbr-no-additional-charge)
transit-gateway-pbr-policy-table-or-route-table-not-both
  claim: A policy table replaces the standard route table on a transit gateway attachment, and an attachment can be associated with either a policy table or a route table, but not both.
  scope: per transit gateway attachment.
  link: [a route table, but not both](../facts/transit-gateway.md#transit-gateway-pbr-policy-table-or-route-table-not-both)
transit-gateway-peering-accepter-and-static-route
  claim: After you create a transit gateway peering attachment request, the owner of the peer transit gateway must accept it, and you add a static route to the transit gateway route table that points to the peering attachment.
  scope: transit gateway peering.
  link: [must accept the request](../facts/transit-gateway.md#transit-gateway-peering-accepter-and-static-route)
  link: [add a static route to the transit gateway](../facts/transit-gateway.md#transit-gateway-peering-accepter-and-static-route)
transit-gateway-peering-aes-256-double-encrypted
  claim: Inter-Region transit gateway peering uses the same network infrastructure as VPC peering, so traffic is encrypted with AES-256 at the virtual network layer between Regions and also at the physical layer outside AWS physical control, which makes it double encrypted there.
  scope: inter-Region transit gateway peering.
  link: [encrypted using AES-256 encryption at the virtual network layer](../facts/transit-gateway.md#transit-gateway-peering-aes-256-double-encrypted)
  link: [double encrypted](../facts/transit-gateway.md#transit-gateway-peering-aes-256-double-encrypted)
transit-gateway-peering-intra-and-inter-region-ipv4-ipv6
  claim: You can peer transit gateways within a Region and across Regions and route IPv4 and IPv6 traffic between them; the peer transit gateway can be in your account or another account.
  scope: transit gateway peering.
  link: [peer both intra-Region and inter-Region transit gateways](../facts/transit-gateway.md#transit-gateway-peering-intra-and-inter-region-ipv4-ipv6)
  link: [includes IPv4 and IPv6 traffic](../facts/transit-gateway.md#transit-gateway-peering-intra-and-inter-region-ipv4-ipv6)
transit-gateway-peering-same-infrastructure-as-vpc-peering
  claim: Transit Gateway peering lets you peer transit gateways in the same or multiple Regions and route traffic between them, using the same underlying infrastructure as VPC peering, and is therefore encrypted.
  scope: transit gateway peering.
  link: [same underlying infrastructure as VPC peering](../facts/transit-gateway.md#transit-gateway-peering-same-infrastructure-as-vpc-peering)
transit-gateway-peering-sender-pays-model
  claim: In general, the transit gateway has a sender pays model.
  scope: transit gateway charges.
  link: [sender pays model](../facts/transit-gateway.md#transit-gateway-peering-sender-pays-model)
transit-gateway-peering-static-routes-only
  claim: Transit gateway peering attachments support only static routes.
  scope: transit gateway peering attachment.
  link: [only static routes are supported](../facts/transit-gateway.md#transit-gateway-peering-static-routes-only)
transit-gateway-pmtud-vpc-and-connect
  claim: Transit gateways support Path MTU Discovery (PMTUD) for traffic ingressing on VPC and Connect attachments.
  scope: VPC and Connect attachments.
  link: [support Path MTU Discovery (PMTUD)](../facts/transit-gateway.md#transit-gateway-pmtud-vpc-and-connect)
transit-gateway-pricing-connect-attachment-owner-billed
  claim: For Transit Gateway Connect attachments (SD-WAN appliances), the transit gateway owner is billed hourly.
  scope: Connect attachments.
  link: [the Transit Gateway owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-connect-attachment-owner-billed)
  say: the transit gateway owner pays
transit-gateway-pricing-data-processing-per-gb-sent-to-gateway
  claim: Data processing charges apply for each gigabyte sent from a VPC, Direct Connect, VPN or Network Firewall to the transit gateway, where 1 gigabyte is 1024 megabytes.
  scope: per GB sent from a VPC, Direct Connect, VPN or Network Firewall attachment to the transit gateway.
  link: [each gigabyte sent from a VPC](../facts/transit-gateway.md#transit-gateway-pricing-data-processing-per-gb-sent-to-gateway)
  say: per gigabyte sent to the transit gateway
transit-gateway-pricing-default-allocation-source-attachment-owner
  claim: By default, transit gateway data processing charges are allocated to the account that owns the source attachment; you can use flexible cost allocation to customize how these charges are allocated.
  scope: transit gateway data processing charges; default; adjustable; flexible cost allocation can customize how these charges are allocated.
  link: [account that owns the source attachment](../facts/transit-gateway.md#transit-gateway-pricing-default-allocation-source-attachment-owner)
  say: the sender's account pays by default
transit-gateway-pricing-dx-attachment-owner-billed
  claim: For Direct Connect attachments to a transit gateway, the Direct Connect gateway owner is billed hourly.
  scope: Direct Connect attachments.
  link: [the Direct Connect Gateway owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-dx-attachment-owner-billed)
  say: the Direct Connect gateway owner pays
transit-gateway-pricing-hourly-attachment-and-data-processing
  claim: Transit Gateway is charged for the number of connections you make to it per hour and for the amount of traffic that flows through it.
  scope: per attachment-hour and per GB of traffic.
  link: [connections that you make to the Transit Gateway](../facts/transit-gateway.md#transit-gateway-pricing-hourly-attachment-and-data-processing)
  say: per hour for each attachment, plus per gigabyte of traffic
transit-gateway-pricing-inter-region-peering-example-total
  claim: In the pricing page example, 1 GB sent from an EC2 instance in a VPC attached to Transit Gateway #1 (N. Virginia) over a peering attachment to Transit Gateway #2 (Oregon) results in total traffic related charges of $0.04: $0.02 for Transit Gateway Data Processing on Transit Gateway #1 and $0.02 for outbound inter-Region data transfer charges.
  scope: pricing page example: 1 GB sent from a VPC on Transit Gateway #1 (N. Virginia) over a peering attachment to Transit Gateway #2 (Oregon).
  link: [$0.04](../facts/transit-gateway.md#transit-gateway-pricing-inter-region-peering-example-total)
  link: [$0.02 for Transit Gateway Data Processing](../facts/transit-gateway.md#transit-gateway-pricing-inter-region-peering-example-total)
  link: [$0.02 for outbound inter-Region data transfer charges](../facts/transit-gateway.md#transit-gateway-pricing-inter-region-peering-example-total)
  say: four cents | two cents for data processing | two cents for outbound inter-Region transfer
transit-gateway-pricing-inter-region-receiving-side-no-charge
  claim: In the inter-Region peering example, the receiving transit gateway does not incur data processing charges, and inbound inter-Region data transfer is free, so no further charges apply on the receiving side.
  scope: receiving transit gateway of an inter-Region peering attachment.
  link: [inbound inter-Region data transfer charges are free](../facts/transit-gateway.md#transit-gateway-pricing-inter-region-receiving-side-no-charge)
  say: inbound inter-Region transfer is free
transit-gateway-pricing-network-function-owner-billed
  claim: For network function attachments, the AWS Network Firewall owner is billed hourly.
  scope: network function attachments.
  link: [the AWS Network Firewall owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-network-function-owner-billed)
  say: the firewall owner pays
transit-gateway-pricing-no-processing-from-peering-attachment
  claim: Data processing charges do not apply for data sent from a peering attachment to a transit gateway.
  scope: data sent from a peering attachment to a transit gateway.
  link: [data sent from a peering attachment](../facts/transit-gateway.md#transit-gateway-pricing-no-processing-from-peering-attachment)
  say: no processing charge from a peering attachment
transit-gateway-pricing-partial-hour-billed-as-full
  claim: Hourly billing for a VPC attachment starts when the Transit Gateway owner accepts the VPC and stops when the attachment is deleted, and each partial VPC Transit Gateway hour consumed is billed as a full hour.
  scope: per VPC attachment-hour.
  link: [billed as a full hour](../facts/transit-gateway.md#transit-gateway-pricing-partial-hour-billed-as-full)
  say: a partial hour counts as a full hour
transit-gateway-pricing-peering-attachment-each-owner-billed
  claim: For peering attachments, each transit gateway owner is billed hourly for the peering attachment with the other transit gateway.
  scope: peering attachments.
  link: [each Transit Gateway owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-peering-attachment-each-owner-billed)
  say: both transit gateway owners pay
transit-gateway-pricing-processing-charged-to-sending-vpc-owner
  claim: In the pricing example, transit gateway data processing is charged to the VPC owner who sends the traffic to the transit gateway.
  scope: pricing example, VPC attachment.
  link: [the VPC owner who sends the traffic](../facts/transit-gateway.md#transit-gateway-pricing-processing-charged-to-sending-vpc-owner)
  say: the sending VPC owner pays
transit-gateway-pricing-standard-data-transfer-in-addition
  claim: You incur standard AWS data transfer charges in addition to any Transit Gateway charges.
  scope: data transfer.
  link: [standard AWS data transfer charges](../facts/transit-gateway.md#transit-gateway-pricing-standard-data-transfer-in-addition)
transit-gateway-pricing-vpc-attachment-owner-billed
  claim: The VPC account owner is billed hourly for each hour that their VPCs are attached to a transit gateway.
  scope: VPC attachments.
  link: [The VPC account owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-vpc-attachment-owner-billed)
  say: the VPC owner pays for the attachment
transit-gateway-pricing-vpn-attachment-owner-billed
  claim: For VPN attachments to a transit gateway, the transit gateway owner is billed hourly.
  scope: VPN attachments.
  link: [the Transit Gateway owner is billed hourly](../facts/transit-gateway.md#transit-gateway-pricing-vpn-attachment-owner-billed)
  say: the transit gateway owner pays
transit-gateway-propagate-to-multiple-route-tables
  claim: A transit gateway attachment can propagate its routes to one or more route tables, even though it is associated with only one.
  scope: transit gateway attachment.
  link: [propagate its routes](../facts/transit-gateway.md#transit-gateway-propagate-to-multiple-route-tables)
  link: [one or more route tables](../facts/transit-gateway.md#transit-gateway-propagate-to-multiple-route-tables)
transit-gateway-propagation-vpc-needs-static-route-in-vpc
  claim: With a Connect attachment routes propagate to the transit gateway route table by default, while with a VPC you must create static routes to send traffic to the transit gateway.
  scope: transit gateway route propagation.
  link: [With a Connect attachment, the routes are propagated](../facts/transit-gateway.md#transit-gateway-propagation-vpc-needs-static-route-in-vpc)
  link: [you must create static routes](../facts/transit-gateway.md#transit-gateway-propagation-vpc-needs-static-route-in-vpc)
transit-gateway-propagation-vpn-dx-peering-behavior
  claim: With a VPN connection routes are propagated from the transit gateway to the on-premises router using BGP, with a Direct Connect gateway allowed prefixes are originated to the on-premises router using BGP, and with a peering attachment you must create a static route to point to the peering attachment.
  scope: transit gateway route propagation.
  link: [propagated from the transit gateway](../facts/transit-gateway.md#transit-gateway-propagation-vpn-dx-peering-behavior)
  link: [you must create a static route](../facts/transit-gateway.md#transit-gateway-propagation-vpn-dx-peering-behavior)
transit-gateway-quota-attachments-per-gateway
  claim: A transit gateway has a default of 5,000 attachments, and the quota is adjustable.
  scope: attachments per transit gateway; default; adjustable.
  link: [5,000](../facts/transit-gateway.md#transit-gateway-quota-attachments-per-gateway)
  say: five thousand attachments per transit gateway
transit-gateway-quota-cidr-blocks-per-gateway
  claim: A transit gateway can have 5 CIDR blocks, and this quota is not adjustable.
  scope: CIDR blocks per transit gateway; fixed; not adjustable; the CIDR blocks are used by Connect attachments and Connect peers.
  link: [5](../facts/transit-gateway.md#transit-gateway-quota-cidr-blocks-per-gateway)
  say: five CIDR blocks per transit gateway
transit-gateway-quota-connect-peer-bandwidth
  claim: Maximum bandwidth per Connect peer (GRE tunnel) per Connect attachment is up to 5 Gbps, and this quota is not adjustable.
  scope: per Connect peer (GRE tunnel), per Connect attachment; maximum; not adjustable.
  link: [up to 5 Gbps](../facts/transit-gateway.md#transit-gateway-quota-connect-peer-bandwidth)
  say: up to five gigabits per second
transit-gateway-quota-connect-peer-pps
  claim: Maximum packets per second per Connect peer is up to 300,000, and this quota is not adjustable.
  scope: per Connect peer; maximum; not adjustable.
  link: [up to 300,000](../facts/transit-gateway.md#transit-gateway-quota-connect-peer-pps)
  say: up to three hundred thousand packets per second
transit-gateway-quota-connect-peers-per-attachment
  claim: A Connect attachment can have 4 Connect peers (GRE tunnels), and this quota is not adjustable.
  scope: Connect peers (GRE tunnels) per Connect attachment; fixed; not adjustable.
  link: [4](../facts/transit-gateway.md#transit-gateway-quota-connect-peers-per-attachment)
  say: four Connect peers per Connect attachment
transit-gateway-quota-dx-gateways-per-gateway
  claim: A transit gateway can have 20 Direct Connect gateways, and this quota is not adjustable.
  scope: Direct Connect gateways per transit gateway; fixed; not adjustable.
  link: [20](../facts/transit-gateway.md#transit-gateway-quota-dx-gateways-per-gateway)
  say: twenty Direct Connect gateways per transit gateway
transit-gateway-quota-dx-peering-bandwidth
  claim: Bandwidth for a Direct Connect gateway or peered transit gateway connection per available Availability Zone in the Region is up to 100 Gbps each direction (100 Gbps ingress and 100 Gbps egress).
  scope: per Direct Connect gateway or peered transit gateway connection, per available Availability Zone in the Region; maximum; not adjustable; the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance.
  link: [up to 100 Gbps](../facts/transit-gateway.md#transit-gateway-quota-dx-peering-bandwidth)
  say: up to one hundred gigabits per second in each direction
transit-gateway-quota-dx-peering-pps
  claim: Packets per second per transit gateway attachment (Direct Connect and peering attachments) per available Availability Zone in the Region is up to 7,500,000.
  scope: per Direct Connect or peering attachment, per available Availability Zone in the Region; maximum; not adjustable; the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance.
  link: [up to 7,500,000](../facts/transit-gateway.md#transit-gateway-quota-dx-peering-pps)
  say: up to seven and a half million packets per second
transit-gateway-quota-gateways-per-account
  claim: By default an account can have 5 transit gateways, and the quota is adjustable.
  scope: transit gateways per account; default; adjustable.
  link: [5](../facts/transit-gateway.md#transit-gateway-quota-gateways-per-account)
  say: five transit gateways per account
transit-gateway-quota-gateways-per-dx-gateway
  claim: A Direct Connect gateway can have 6 transit gateways, and this quota is not adjustable.
  scope: transit gateways per Direct Connect gateway; fixed; not adjustable.
  link: [6](../facts/transit-gateway.md#transit-gateway-quota-gateways-per-dx-gateway)
  say: six transit gateways per Direct Connect gateway
transit-gateway-quota-gateways-per-vpc
  claim: A VPC can be attached to 5 transit gateways, and this quota is not adjustable.
  scope: transit gateways per VPC; fixed; not adjustable.
  link: [5](../facts/transit-gateway.md#transit-gateway-quota-gateways-per-vpc)
  say: five transit gateways per VPC
transit-gateway-quota-peering-attachments
  claim: A transit gateway has a default of 50 peering attachments, and the quota is adjustable.
  scope: peering attachments per transit gateway; default; adjustable.
  link: [50](../facts/transit-gateway.md#transit-gateway-quota-peering-attachments)
  say: fifty peering attachments per transit gateway
transit-gateway-quota-peering-between-two-gateways
  claim: Two transit gateways, or one transit gateway and a Cloud WAN core network edge (CNE), can have 1 peering attachment between them, and this quota is not adjustable.
  scope: peering attachments between two transit gateways or between one transit gateway and a Cloud WAN core network edge (CNE); fixed; not adjustable.
  link: [1](../facts/transit-gateway.md#transit-gateway-quota-peering-between-two-gateways)
  say: one peering attachment between two transit gateways
transit-gateway-quota-pending-peering-attachments
  claim: A transit gateway has a default of 10 pending peering attachments, and the quota is adjustable.
  scope: pending peering attachments per transit gateway; default; adjustable.
  link: [10](../facts/transit-gateway.md#transit-gateway-quota-pending-peering-attachments)
  say: ten pending peering attachments
transit-gateway-quota-route-tables-per-gateway
  claim: A transit gateway has a default of 20 route tables, and the quota is adjustable.
  scope: transit gateway route tables per transit gateway; default; adjustable.
  link: [20](../facts/transit-gateway.md#transit-gateway-quota-route-tables-per-gateway)
  say: twenty route tables per transit gateway
transit-gateway-quota-static-routes-per-prefix-attachment
  claim: The Transit Gateway quota for static routes for a prefix to a single attachment is 1, and this quota is not adjustable.
  scope: static routes for a prefix to a single attachment; fixed; not adjustable.
  link: [1](../facts/transit-gateway.md#transit-gateway-quota-static-routes-per-prefix-attachment)
  say: one static route for a prefix to a single attachment
transit-gateway-quota-total-routes
  claim: The default for total combined routes (dynamic and static) across all route tables of a single transit gateway is 10,000.
  scope: total combined routes across all route tables of one transit gateway; default; not adjustable; no Service Quotas link: the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance.
  link: [10,000](../facts/transit-gateway.md#transit-gateway-quota-total-routes)
  say: ten thousand routes in total
transit-gateway-quota-vpc-attachment-bandwidth
  claim: Bandwidth per VPC attachment per Availability Zone is up to 100 Gbps each direction (100 Gbps ingress and 100 Gbps egress).
  scope: per VPC attachment, per Availability Zone; maximum; not adjustable; the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance.
  link: [up to 100 Gbps](../facts/transit-gateway.md#transit-gateway-quota-vpc-attachment-bandwidth)
  say: up to one hundred gigabits per second in each direction
transit-gateway-quota-vpc-attachment-pps
  claim: Packets per second per transit gateway VPC attachment per Availability Zone is up to 7,500,000.
  scope: per transit gateway VPC attachment, per Availability Zone; maximum; not adjustable; the Adjustable column says to contact your Solutions Architect (SA) or Technical Account Manager (TAM) for further assistance.
  link: [up to 7,500,000](../facts/transit-gateway.md#transit-gateway-quota-vpc-attachment-pps)
  say: up to seven and a half million packets per second
transit-gateway-quotas-are-region-specific
  claim: Unless a Transit Gateway quota is noted otherwise, the quota is Region-specific.
  scope: Transit Gateway quotas.
  link: [Region-specific](../facts/transit-gateway.md#transit-gateway-quotas-are-region-specific)
  say: counted per Region
transit-gateway-regional-resource-thousands-of-vpcs
  claim: Transit Gateway is a Regional resource that can connect thousands of VPCs within the same AWS Region.
  scope: AWS Transit Gateway.
  link: [Regional resource](../facts/transit-gateway.md#transit-gateway-regional-resource-thousands-of-vpcs)
  link: [connect thousands of VPCs](../facts/transit-gateway.md#transit-gateway-regional-resource-thousands-of-vpcs)
transit-gateway-route-evaluation-most-specific-first
  claim: The Transit Gateway guide lists the order in which transit gateway routes are evaluated: first the most specific route for the destination address, then, for routes with the same CIDR from different attachment types, a route priority by route type.
  scope: transit gateway route tables; for routes with the same CIDR from different attachment types, a route priority list applies next.
  link: [The most specific route for the destination address](../facts/transit-gateway.md#transit-gateway-route-evaluation-most-specific-first)
transit-gateway-route-table-association-supported-attachments
  claim: Transit gateway route tables can be associated with VPC, VPN, VPN Concentrator, Client VPN, Direct Connect gateway, peering and Connect attachments, and an attachment can be propagated to multiple route tables.
  scope: transit gateway route tables.
  link: [VPC, VPN, VPN Concentrator, Client VPN](../facts/transit-gateway.md#transit-gateway-route-table-association-supported-attachments)
  link: [propagated to multiple route tables](../facts/transit-gateway.md#transit-gateway-route-table-association-supported-attachments)
transit-gateway-separate-small-subnet-per-attachment
  claim: Use a separate subnet for each transit gateway VPC attachment and give it a small CIDR block such as /28, so more addresses remain for EC2 resources.
  scope: transit gateway VPC attachment subnets.
  link: [separate subnet for each transit gateway VPC attachment](../facts/transit-gateway.md#transit-gateway-separate-small-subnet-per-attachment)
  link: [small CIDR](../facts/transit-gateway.md#transit-gateway-separate-small-subnet-per-attachment)
  link: [/28](../facts/transit-gateway.md#transit-gateway-separate-small-subnet-per-attachment)
transit-gateway-sg-reference-enable-both-sides
  claim: Security group referencing on a transit gateway works only if it is enabled for both the transit gateway and its VPC attachments.
  scope: transit gateway security group referencing.
  link: [if it has been enabled for both](../facts/transit-gateway.md#transit-gateway-sg-reference-enable-both-sides)
transit-gateway-sg-reference-inbound-only
  claim: Security group referencing across VPCs attached to the same transit gateway works in inbound rules only; outbound security rules do not support it, and there is no additional cost for enabling or using it.
  scope: transit gateway security group referencing.
  link: [cross-reference security groups in inbound rules only](../facts/transit-gateway.md#transit-gateway-sg-reference-inbound-only)
  link: [no additional costs](../facts/transit-gateway.md#transit-gateway-sg-reference-inbound-only)
transit-gateway-sg-reference-not-across-peering
  claim: Security group referencing is not supported across transit gateway peering connections; both VPCs must be attached to the same transit gateway.
  scope: transit gateway security group referencing.
  link: [not supported across transit gateway peering connections](../facts/transit-gateway.md#transit-gateway-sg-reference-not-across-peering)
  link: [attached to the same transit gateway](../facts/transit-gateway.md#transit-gateway-sg-reference-not-across-peering)
transit-gateway-sg-reference-not-privatelink-endpoints
  claim: Security group referencing through a transit gateway is not supported for PrivateLink endpoints, so AWS recommends IP CIDR-based security rules instead.
  scope: transit gateway security group referencing.
  link: [not supported for PrivateLink endpoints](../facts/transit-gateway.md#transit-gateway-sg-reference-not-privatelink-endpoints)
  link: [IP CIDR-based security rules](../facts/transit-gateway.md#transit-gateway-sg-reference-not-privatelink-endpoints)
transit-gateway-sg-reference-not-through-inspection-vpc
  claim: With an inspection VPC, security group referencing through the transit gateway does not work across a Gateway Load Balancer or AWS Network Firewall.
  scope: transit gateway security group referencing.
  link: [does not work across AWS Gateway Load Balancer](../facts/transit-gateway.md#transit-gateway-sg-reference-not-through-inspection-vpc)
transit-gateway-sg-referencing-not-in-use1-az3
  claim: Security group referencing is not supported for transit gateway VPC attachments in the Availability Zone use1-az3.
  scope: security group referencing across VPCs attached to one transit gateway.
  link: [availability zone use1-az3](../facts/transit-gateway.md#transit-gateway-sg-referencing-not-in-use1-az3)
transit-gateway-share-accept-in-ram
  claim: An account added to a transit gateway resource share receives an invitation and must accept the resource share in the AWS RAM console before it can access the shared transit gateway.
  scope: shared transit gateway.
  link: [must accept the resource share](../facts/transit-gateway.md#transit-gateway-share-accept-in-ram)
  link: [before you can access the shared resources](../facts/transit-gateway.md#transit-gateway-share-accept-in-ram)
transit-gateway-share-with-ram-accounts-or-org
  claim: You can use AWS RAM to share a transit gateway for VPC attachments across accounts or across your organization in AWS Organizations.
  scope: shared transit gateway.
  link: [AWS Resource Access Manager (RAM) to share](../facts/transit-gateway.md#transit-gateway-share-with-ram-accounts-or-org)
  link: [across your organization in AWS Organizations](../facts/transit-gateway.md#transit-gateway-share-with-ram-accounts-or-org)
transit-gateway-shows-only-preferred-route
  claim: A transit gateway route table shows only the preferred route; a backup route, for example Site-to-Site VPN behind Direct Connect for the same prefix, appears only when the active route is no longer advertised.
  scope: transit gateway route table.
  link: [only shows a preferred route](../facts/transit-gateway.md#transit-gateway-shows-only-preferred-route)
  link: [only appear in the transit gateway route table](../facts/transit-gateway.md#transit-gateway-shows-only-preferred-route)
transit-gateway-static-route-beats-propagated
  claim: When a static route and a propagated route have the same destination, the static route has the higher priority and the propagated route is not included in the route table.
  scope: transit gateway route table.
  link: [the static route has the higher priority](../facts/transit-gateway.md#transit-gateway-static-route-beats-propagated)
  link: [the propagated route is not included](../facts/transit-gateway.md#transit-gateway-static-route-beats-propagated)
transit-gateway-unique-asn-per-gateway
  claim: For deployments with multiple transit gateways, AWS recommends a unique Autonomous System Number (ASN) for each transit gateway; you can also use inter-Region peering.
  scope: multiple transit gateways.
  link: [unique Autonomous System Number (ASN)](../facts/transit-gateway.md#transit-gateway-unique-asn-per-gateway)
  link: [for each of your transit gateways](../facts/transit-gateway.md#transit-gateway-unique-asn-per-gateway)
transit-gateway-vpc-attachment-eni-one-subnet-per-az
  claim: A transit gateway VPC attachment places a network interface in the subnet you specify for each enabled Availability Zone, and traffic can then be routed to all subnets in that zone, not only the one you specified.
  scope: transit gateway VPC attachment.
  link: [you specify exactly one subnet](../facts/transit-gateway.md#transit-gateway-vpc-attachment-eni-one-subnet-per-az)
  link: [not just the one you specified](../facts/transit-gateway.md#transit-gateway-vpc-attachment-eni-one-subnet-per-az)
transit-gateway-vpc-attachment-one-subnet-per-az-entry-exit
  claim: When you attach a VPC you specify one subnet from each Availability Zone for the transit gateway to route traffic; those subnets serve as the entry and exit points, and traffic reaches resources in other subnets of the zone only if the attachment subnets have routes to them.
  scope: transit gateway VPC attachment.
  link: [specify one subnet from each Availability Zone](../facts/transit-gateway.md#transit-gateway-vpc-attachment-one-subnet-per-az-entry-exit)
  link: [entry and exit points for transit gateway traffic](../facts/transit-gateway.md#transit-gateway-vpc-attachment-one-subnet-per-az-entry-exit)
transit-gateway-vpc-attachment-visible-2-hours
  claim: A failed or deleted VPC attachment remains visible for 2 hours and then is no longer visible.
  scope: per VPC attachment in the failed or deleted state; fixed; not adjustable.
  link: [remains visible for 2 hours](../facts/transit-gateway.md#transit-gateway-vpc-attachment-visible-2-hours)
  say: stays visible for two hours
transit-gateway-vpc-propagation-cidr-blocks
  claim: For a VPC attachment, the CIDR blocks of the VPC are propagated to the transit gateway route table, and you cannot filter on advertised routes.
  scope: transit gateway route propagation.
  link: [CIDR blocks of the VPC are propagated](../facts/transit-gateway.md#transit-gateway-vpc-propagation-cidr-blocks)
  link: [can't filter on advertised routes](../facts/transit-gateway.md#transit-gateway-vpc-propagation-cidr-blocks)
transit-gateway-vpc-route-to-tgw-required
  claim: After you attach a VPC to a transit gateway, you must add a route to the subnet route table for traffic to go through the transit gateway.
  scope: transit gateway VPC attachment.
  link: [add a route to your subnet route table](../facts/transit-gateway.md#transit-gateway-vpc-route-to-tgw-required)
transit-gateway-vpn-attachment-dynamic-static-ipv4-ipv6
  claim: A Site-to-Site VPN attachment on a transit gateway connects your VPCs and on-premises networks, and supports dynamic and static routes as well as IPv4 and IPv6.
  scope: transit gateway Site-to-Site VPN attachment.
  link: [Both dynamic and static routes are supported](../facts/transit-gateway.md#transit-gateway-vpn-attachment-dynamic-static-ipv4-ipv6)
  link: [as well as IPv4 and IPv6](../facts/transit-gateway.md#transit-gateway-vpn-attachment-dynamic-static-ipv4-ipv6)
transit-gateway-vpn-attachment-same-account-as-tgw
  claim: When a transit gateway is shared, an AWS Site-to-Site VPN attachment must be created in the same AWS account that owns the transit gateway.
  scope: shared transit gateway.
  link: [must be created in the same AWS account](../facts/transit-gateway.md#transit-gateway-vpn-attachment-same-account-as-tgw)
transit-gateway-vs-peering-wp-hub-and-spoke-thousands-of-vpcs-one-gateway
  claim: With Transit Gateway, each spoke VPC only needs to connect to the Transit Gateway to gain access to other connected VPCs, an attachments-based hub-and-spoke; the whitepaper's comparison table lists the architecture of VPC peering as a full mesh.
  scope: AWS Transit Gateway vs VPC peering.
  link: [Each spoke VPC only needs to connect](../facts/transit-gateway.md#transit-gateway-vs-peering-wp-hub-and-spoke-thousands-of-vpcs-one-gateway)
transit-gateway-wa-rel02-bp04-central-hub-simplifies
  claim: The Well-Architected reliability pillar prefers a hub-and-spoke topology over a many-to-many mesh, because the hub centralizes connections and simplifies the network structure while improving operability, scalability and control.
  scope: REL02-BP04.
  link: [hub-and-spoke architecture centralizes connections through a single hub](../facts/transit-gateway.md#transit-gateway-wa-rel02-bp04-central-hub-simplifies)
  link: [enhances its operability, scalability, and control](../facts/transit-gateway.md#transit-gateway-wa-rel02-bp04-central-hub-simplifies)
transit-gateway-wa-rel02-bp04-hub-in-network-services-account
  claim: Place the hub in the organization's Network Services account so network engineers can manage it centrally.
  scope: REL02-BP04.
  link: [Place the hub in the organization's Network](../facts/transit-gateway.md#transit-gateway-wa-rel02-bp04-hub-in-network-services-account)
transit-gateway-wa-rel02-bp04-managed-hub-service
  claim: AWS Transit Gateway is a managed, scalable and highly available service for building hub-and-spoke networks on AWS, serving as the central hub that provides network segmentation, centralized routing and simplified connection to cloud and on-premises environments.
  scope: REL02-BP04.
  link: [designed for construction of hub-and-spoke networks on AWS](../facts/transit-gateway.md#transit-gateway-wa-rel02-bp04-managed-hub-service)
transit-gateway-wa-rel02-bp04-routes-only-where-needed
  claim: Design transit gateway route tables so routes exist only between networks that should communicate, and omit routes between networks that should not, such as separate workloads with no inter-dependencies.
  scope: REL02-BP04.
  link: [routes are provided only between networks](../facts/transit-gateway.md#transit-gateway-wa-rel02-bp04-routes-only-where-needed)
transit-gateway-whitepaper-connects-thousands-of-vpcs
  claim: Transit Gateway enables customers to connect thousands of VPCs.
  scope: per transit gateway (whitepaper statement).
  link: [connect thousands of VPCs](../facts/transit-gateway.md#transit-gateway-whitepaper-connects-thousands-of-vpcs)
  say: thousands of VPCs
transit-gateway-wp-centralize-shared-services
  claim: The hub-and-spoke architecture of Transit Gateway can centralize access to shared services such as traffic inspection, interface VPC endpoint access, or egress through NAT gateways or NAT instances.
  scope: AWS Transit Gateway.
  link: [centralize access to shared services](../facts/transit-gateway.md#transit-gateway-wp-centralize-shared-services)
  link: [interface VPC endpoint access](../facts/transit-gateway.md#transit-gateway-wp-centralize-shared-services)
transit-gateway-wp-cloud-wan-replaces-tgw-peering-vpn
  claim: AWS Cloud WAN is a new way to connect networks that previously could be done with Transit Gateways, VPC peering and IPsec VPN tunnels; where network and security posture constructs used to be defined in one place and the networks in another, Cloud WAN centralizes all of these constructs in a single place.
  scope: AWS Cloud WAN.
  link: [connect networks together that we were previously](../facts/transit-gateway.md#transit-gateway-wp-cloud-wan-replaces-tgw-peering-vpn)
transit-gateway-wp-cloud-wan-segments-by-policy
  claim: AWS Cloud WAN lets you centralize network and security posture constructs in a single place and, by policy, segment your networks to determine who can talk to whom; network segments are routing domains that by default allow communication only within a segment.
  scope: AWS Cloud WAN.
  link: [Network segments are routing domains](../facts/transit-gateway.md#transit-gateway-wp-cloud-wan-segments-by-policy)
  link: [allow communication only within a segment](../facts/transit-gateway.md#transit-gateway-wp-cloud-wan-segments-by-policy)
transit-gateway-wp-consolidate-routing-hub-and-spoke
  claim: AWS Transit Gateway is a highly available and scalable service that consolidates the VPC routing configuration of a Region in a hub-and-spoke architecture, where each spoke VPC only needs to connect to the transit gateway to reach the other connected VPCs.
  scope: AWS Transit Gateway.
  link: [consolidate the AWS VPC routing configuration](../facts/transit-gateway.md#transit-gateway-wp-consolidate-routing-hub-and-spoke)
  link: [hub-and-spoke architecture](../facts/transit-gateway.md#transit-gateway-wp-consolidate-routing-hub-and-spoke)
transit-gateway-wp-many-vpcs-hub-and-spoke-no-mesh
  claim: A transit gateway lets you connect thousands of VPCs and attach all hybrid connectivity (VPN and Direct Connect) to one gateway, consolidating the organization's AWS routing configuration in one place.
  scope: AWS Transit Gateway.
  link: [connect thousands of VPCs](../facts/transit-gateway.md#transit-gateway-wp-many-vpcs-hub-and-spoke-no-mesh)
  link: [VPN and Direct Connect connections](../facts/transit-gateway.md#transit-gateway-wp-many-vpcs-hub-and-spoke-no-mesh)
transit-gateway-wp-segment-routing-domains
  claim: You can use several transit gateway route tables, associations and propagations to segment traffic within one transit gateway and manage routing domains, such as production and non-production traffic, from one point so they cannot communicate with each other.
  scope: AWS Transit Gateway.
  link: [segment your traffic within the same Transit Gateway](../facts/transit-gateway.md#transit-gateway-wp-segment-routing-domains)
  link: [routing domains](../facts/transit-gateway.md#transit-gateway-wp-segment-routing-domains)
transit-gateway-wp-simplifies-management-lower-ops-cost
  claim: The hub-and-spoke model of Transit Gateway simplifies management and reduces operational costs because VPCs only connect to the transit gateway to gain access to the connected networks.
  scope: AWS Transit Gateway.
  link: [simplifies management and reduces operational costs](../facts/transit-gateway.md#transit-gateway-wp-simplifies-management-lower-ops-cost)
  link: [VPCs only connect to the Transit Gateway instance](../facts/transit-gateway.md#transit-gateway-wp-simplifies-management-lower-ops-cost)
transit-gateway-wp-table-architecture-comparison
  claim: The whitepaper comparison table gives VPC peering a full-mesh architecture, a transit VPC a VPN-based hub-and-spoke, Transit Gateway an attachments-based hub-and-spoke, PrivateLink a provider or consumer model, Cloud WAN an attachments-based multi-Region architecture and VPC Lattice app-to-app connectivity.
  scope: VPC connectivity options.
  link: [Full mesh](../facts/transit-gateway.md#transit-gateway-wp-table-architecture-comparison)
  link: [Attachments-based hub-and-spoke](../facts/transit-gateway.md#transit-gateway-wp-table-architecture-comparison)
transit-gateway-wp-table-dx-plus-tgw-use-case
  claim: The connectivity-options table lists AWS Direct Connect plus AWS Transit Gateway as a dedicated network connection over private lines to a regional router for multiple VPCs.
  scope: Direct Connect with AWS Transit Gateway.
  link: [Dedicated network connection over private lines](../facts/transit-gateway.md#transit-gateway-wp-table-dx-plus-tgw-use-case)
transit-gateway-wp-table-latency-comparison
  claim: The whitepaper comparison table lists the lowest latency for VPC peering, extra latency for a transit VPC due to VPN encryption overhead, and an additional hop for Transit Gateway.
  scope: VPC connectivity options.
  link: [Lowest](../facts/transit-gateway.md#transit-gateway-wp-table-latency-comparison)
  link: [Additional Transit Gateway hop](../facts/transit-gateway.md#transit-gateway-wp-table-latency-comparison)
transit-gateway-wp-table-scope-comparison
  claim: The whitepaper comparison table lists the scope of VPC peering as Regional or global, transit VPC, Transit Gateway, PrivateLink and VPC Lattice as Regional, and Cloud WAN as global.
  scope: VPC connectivity options.
  link: [Regional/Global](../facts/transit-gateway.md#transit-gateway-wp-table-scope-comparison)
  link: [Global](../facts/transit-gateway.md#transit-gateway-wp-table-scope-comparison)
transit-gateway-wp-table-segmentation-comparison
  claim: The whitepaper comparison table lists security groups as the segmentation method for VPC peering, Transit Gateway route tables for Transit Gateway, no segmentation for PrivateLink, segments for Cloud WAN and service and service network policies for VPC Lattice.
  scope: VPC connectivity options.
  link: [Transit Gateway route tables](../facts/transit-gateway.md#transit-gateway-wp-table-segmentation-comparison)
  link: [No segmentation](../facts/transit-gateway.md#transit-gateway-wp-table-segmentation-comparison)
transit-gateway-wp-table-vpn-plus-tgw-use-case
  claim: The connectivity-options table lists AWS Transit Gateway plus AWS Site-to-Site VPN as an AWS managed IPsec VPN connection over the internet to a regional router for multiple VPCs.
  scope: Site-to-Site VPN with AWS Transit Gateway.
  link: [AWS managed IPsec VPN connection over the internet](../facts/transit-gateway.md#transit-gateway-wp-table-vpn-plus-tgw-use-case)
transit-gateway-wp-traffic-stays-on-backbone
  claim: Transit gateways can be peered within the same AWS Region or between different Regions, and traffic using Transit Gateway inter-Region peering always stays on the global AWS backbone and never traverses the public internet, which reduces threats such as common exploits and DDoS attacks.
  scope: AWS Transit Gateway peering traffic (inter-Region peering); Stated for traffic using Transit Gateway inter-Region peering; the whitepaper sentence follows its statement on transit gateway peering..
  link: [always stays on the global AWS backbone](../facts/transit-gateway.md#transit-gateway-wp-traffic-stays-on-backbone)
  link: [never traverses the public internet](../facts/transit-gateway.md#transit-gateway-wp-traffic-stays-on-backbone)
transit-gateway-wp-transit-vpc-challenges
  claim: A transit VPC has higher costs for third-party virtual appliances on EC2, limited throughput per VPN connection and extra configuration, management and resiliency work, because you manage high availability and redundancy of the appliance instances.
  scope: transit VPC (older pattern).
  link: [higher costs for running third-party vendor virtual appliances](../facts/transit-gateway.md#transit-gateway-wp-transit-vpc-challenges)
  link: [additional conﬁguration, management and resiliency overhead](../facts/transit-gateway.md#transit-gateway-wp-transit-vpc-challenges)
transit-gateway-wp-transit-vpc-vpn-overlay-hub
  claim: In a transit VPC, one central hub VPC connects to every spoke VPC through a VPN connection, and EC2 instances in the hub run software appliances that route traffic over the VPN overlay.
  scope: transit VPC (older pattern).
  link: [one central VPC (the hub VPC)](../facts/transit-gateway.md#transit-gateway-wp-transit-vpc-vpn-overlay-hub)
  link: [software appliances that route incoming traffic](../facts/transit-gateway.md#transit-gateway-wp-transit-vpc-vpn-overlay-hub)
vpc-endpoints-aws-services-integrating-list
  claim: The guide lists the AWS services that integrate with AWS PrivateLink, and you can create a VPC endpoint to connect to those services privately, as if they were running in your own VPC.
  scope: AWS PrivateLink integrations.
  link: [AWS services integrate with AWS PrivateLink](../facts/vpc-endpoints.md#vpc-endpoints-aws-services-integrating-list)
  link: [create a VPC endpoint to connect to these](../facts/vpc-endpoints.md#vpc-endpoints-aws-services-integrating-list)
vpc-endpoints-bandwidth-10-gbps-per-az-scales-to-100
  claim: By default each VPC endpoint can support a bandwidth of up to 10 Gbps per Availability Zone, and it automatically scales up to 100 Gbps.
  scope: per VPC endpoint, per Availability Zone; default; not adjustable.
  link: [up to 10 Gbps per Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-bandwidth-10-gbps-per-az-scales-to-100)
  link: [automatically scales up to 100 Gbps](../facts/vpc-endpoints.md#vpc-endpoints-bandwidth-10-gbps-per-az-scales-to-100)
  say: up to ten gigabits per second per Availability Zone | scales automatically up to one hundred gigabits per second
vpc-endpoints-bandwidth-max-is-az-count-times-100
  claim: The maximum bandwidth of a VPC endpoint, when the load is spread across all Availability Zones, is the number of Availability Zones multiplied by 100 Gbps; for higher throughput you contact AWS support.
  scope: per VPC endpoint, across all Availability Zones; maximum; not adjustable; if your application needs higher throughput, contact AWS support.
  link: [the number of Availability Zones multiplied by 100 Gbps](../facts/vpc-endpoints.md#vpc-endpoints-bandwidth-max-is-az-count-times-100)
  say: the number of zones times one hundred gigabits per second
vpc-endpoints-change-s3-ipv6-2025
  claim: Amazon S3 now supports IPv6 addresses for AWS PrivateLink gateway and interface VPC endpoints, and the IPv6 support for S3 VPC endpoints is available at no additional cost.
  link: [IPv6 addresses for AWS PrivateLink gateway and interface](../facts/vpc-endpoints.md#vpc-endpoints-change-s3-ipv6-2025)
vpc-endpoints-cmp-private-dns-public-name
  claim: When you create an interface VPC endpoint for an AWS service and enable private DNS, you can keep making requests to the DNS name of the service public endpoint while using private connectivity through the interface endpoint.
  scope: per interface endpoint to an AWS service; Private DNS is enabled on the endpoint..
  link: [the DNS name for its public endpoint](../facts/vpc-endpoints.md#vpc-endpoints-cmp-private-dns-public-name)
  say: keep the public service name
vpc-endpoints-ddb-gateway-vs-interface-choice
  claim: A DynamoDB gateway endpoint gives access from your VPC without an internet gateway or NAT device and at no additional cost, but it does not allow access from on-premises networks, from peered VPCs in other Regions or through a transit gateway; for those cases you must use an interface endpoint, which costs extra.
  scope: DynamoDB gateway endpoints and interface endpoints.
  link: [you must use an interface endpoint](../facts/vpc-endpoints.md#vpc-endpoints-ddb-gateway-vs-interface-choice)
  link: [available for an additional cost](../facts/vpc-endpoints.md#vpc-endpoints-ddb-gateway-vs-interface-choice)
vpc-endpoints-faq-100-endpoints-per-vpc
  claim: The AWS PrivateLink FAQ says you can create up to 100 VPC endpoints per VPC.
  scope: per VPC (FAQ answer); maximum; adjustable; the FAQ answer continues by inviting customers who need more to ask AWS; the quotas page (vpc-endpoints-quota-interface-gwlb-per-vpc) gives a different, adjustable default.
  link: [up to 100 VPC endpoints per VPC](../facts/vpc-endpoints.md#vpc-endpoints-faq-100-endpoints-per-vpc)
  say: up to one hundred VPC endpoints per VPC
vpc-endpoints-faq-benefit-limit-to-vpc-or-endpoint
  claim: You can limit access to resources provided by an Amazon service to traffic that comes from a specific VPC or through a specific VPC endpoint.
  link: [through a specific VPC endpoint](../facts/vpc-endpoints.md#vpc-endpoints-faq-benefit-limit-to-vpc-or-endpoint)
  say: one VPC or one endpoint
vpc-endpoints-faq-benefit-no-other-gateways
  claim: A VPC endpoint gives access to a specific service or resource without an internet gateway, NAT gateway, VPN connection or VPC peering connection, which reduces the risk of exposing your resources to the internet or other outside networks.
  scope: VPC endpoints (FAQ answer).
  link: [an internet gateway, NAT gateway, VPN connection](../facts/vpc-endpoints.md#vpc-endpoints-faq-benefit-no-other-gateways)
  say: no internet gateway, NAT, VPN or peering needed
vpc-endpoints-faq-benefit-restrict-users-actions-resources
  claim: When you access Amazon services over VPC endpoints, you can restrict access through the endpoint to specific users, actions and resources.
  link: [specific users, actions, and/or resources](../facts/vpc-endpoints.md#vpc-endpoints-faq-benefit-restrict-users-actions-resources)
  say: limit users, actions and resources
vpc-endpoints-faq-cloudwatch-metrics-types
  claim: Amazon CloudWatch metrics are available for VPC endpoints of the types interface and Gateway Load Balancer.
  link: [interface](../facts/vpc-endpoints.md#vpc-endpoints-faq-cloudwatch-metrics-types)
  say: interface and Gateway Load Balancer endpoints
vpc-endpoints-faq-endpoint-per-service-or-resource
  claim: Gateway, interface, Gateway Load Balancer and resource VPC endpoints each connect to a single endpoint service or resource; a service network endpoint connects to a service network that can hold multiple resources and VPC Lattice services.
  link: [connect to a single endpoint service or resource](../facts/vpc-endpoints.md#vpc-endpoints-faq-endpoint-per-service-or-resource)
  say: one service or resource per endpoint
vpc-endpoints-faq-five-types
  claim: Amazon VPC offers five types of VPC endpoints: gateway, interface, Gateway Load Balancer, resource and service network endpoints; every type except the gateway endpoint is powered by PrivateLink.
  link: [five different types of VPC endpoints](../facts/vpc-endpoints.md#vpc-endpoints-faq-five-types)
  link: [except gateway endpoint are powered by PrivateLink](../facts/vpc-endpoints.md#vpc-endpoints-faq-five-types)
  say: five endpoint types | only the gateway endpoint is not PrivateLink
vpc-endpoints-faq-gateway-endpoint-s3-ddb-route
  claim: Gateway endpoints are available only for AWS services including Amazon S3 and Amazon DynamoDB, and they do not enable PrivateLink; a gateway endpoint adds an entry to the route table you select and routes the traffic through the Amazon private network.
  scope: gateway VPC endpoints.
  link: [Amazon S3 and Amazon DynamoDB](../facts/vpc-endpoints.md#vpc-endpoints-faq-gateway-endpoint-s3-ddb-route)
  link: [add an entry to the route table](../facts/vpc-endpoints.md#vpc-endpoints-faq-gateway-endpoint-s3-ddb-route)
  say: S3 and DynamoDB | it adds a route
vpc-endpoints-faq-gwlb-endpoint-appliances
  claim: Gateway Load Balancer endpoints provide private connectivity to appliances fronted by a Gateway Load Balancer.
  link: [appliances fronted by a Gateway Load Balancer](../facts/vpc-endpoints.md#vpc-endpoints-faq-gwlb-endpoint-appliances)
  say: virtual appliances behind a Gateway Load Balancer
vpc-endpoints-faq-horizontally-scalable-highly-available
  claim: VPC endpoints are horizontally scalable and highly available virtual devices that allow communication between instances in your VPC and services or resources.
  link: [horizontally scalable and highly available virtual devices](../facts/vpc-endpoints.md#vpc-endpoints-faq-horizontally-scalable-highly-available)
  say: scalable and highly available
vpc-endpoints-faq-interface-endpoint-privatelink-services
  claim: Interface endpoints give private connectivity to services powered by PrivateLink, which can be AWS services, your own services or SaaS solutions, and they also support connectivity over AWS Direct Connect and VPN.
  link: [software as a service (SaaS) solutions](../facts/vpc-endpoints.md#vpc-endpoints-faq-interface-endpoint-privatelink-services)
  link: [connectivity over AWS Direct Connect and VPN](../facts/vpc-endpoints.md#vpc-endpoints-faq-interface-endpoint-privatelink-services)
  say: AWS, your own, or SaaS services | works over Direct Connect and VPN
vpc-endpoints-faq-onprem-dx-dns-returns-private-ip
  claim: You can access VPC endpoints from an on-premises network over Direct Connect; the DNS records of a VPC endpoint are publicly resolvable but return the private IP address within the associated VPC.
  scope: VPC endpoint DNS records reached from on premises.
  link: [the private IP address within the associated VPC](../facts/vpc-endpoints.md#vpc-endpoints-faq-onprem-dx-dns-returns-private-ip)
  say: the records return a private IP
vpc-endpoints-faq-resource-endpoint
  claim: Resource endpoints provide private connectivity to VPC resources such as databases, clusters, domain-name targets and IP addresses that do not require load balancing, and they support connectivity over Direct Connect and VPN.
  scope: resource VPC endpoints (FAQ answer).
  link: [databases, clusters, domain-name targets, and IP addresses](../facts/vpc-endpoints.md#vpc-endpoints-faq-resource-endpoint)
  say: databases, clusters, domain names and IPs
vpc-endpoints-faq-sdk-discovers-endpoints-latest
  claim: With the latest version of the AWS CLI or SDK you do not need to update your code to use VPC endpoints: the CLI or SDK automatically discovers your VPC endpoints and uses them by default.
  scope: latest versions of the AWS CLI and SDKs.
  link: [you do not need to update your code](../facts/vpc-endpoints.md#vpc-endpoints-faq-sdk-discovers-endpoints-latest)
  say: no code change needed
vpc-endpoints-faq-security-groups-association
  claim: The PrivateLink FAQ answers yes: you can associate security groups with VPC endpoints.
  scope: per VPC endpoint type named in the FAQ answer.
  link: [associate security groups with VPC endpoints](../facts/vpc-endpoints.md#vpc-endpoints-faq-security-groups-association)
  say: security groups can be attached
vpc-endpoints-faq-service-network-endpoint
  claim: Service network endpoints let you privately connect to services and resources in an Amazon VPC Lattice service network, and give access to multiple services and resources through a single VPC endpoint.
  link: [in an Amazon VPC Lattice service network](../facts/vpc-endpoints.md#vpc-endpoints-faq-service-network-endpoint)
  say: a VPC Lattice service network
vpc-endpoints-gateway-dns-attributes
  claim: If you use the Amazon DNS servers, you must enable both DNS hostnames and DNS resolution for the VPC to use a gateway endpoint; with your own DNS server, requests to Amazon S3 must resolve to the IP addresses AWS maintains.
  scope: gateway endpoint for Amazon S3.
  link: [must enable both](../facts/vpc-endpoints.md#vpc-endpoints-gateway-dns-attributes)
  link: [DNS hostnames and DNS resolution](../facts/vpc-endpoints.md#vpc-endpoints-gateway-dns-attributes)
vpc-endpoints-gateway-nacl-no-prefix-list
  claim: The network ACL of the instances' subnet must allow traffic to and from Amazon S3 through a gateway endpoint; you cannot reference prefix lists in network ACL rules, but you can get the IP address range from the prefix list.
  scope: gateway endpoint for Amazon S3.
  link: [can't reference prefix lists in network ACL rules](../facts/vpc-endpoints.md#vpc-endpoints-gateway-nacl-no-prefix-list)
vpc-endpoints-gateway-not-extended-past-vpc
  claim: Endpoint connections cannot be extended out of a VPC: resources on the other side of a VPN connection, VPC peering connection, transit gateway or Direct Connect connection cannot use a gateway endpoint to reach Amazon S3.
  scope: gateway endpoint for Amazon S3.
  link: [cannot be extended out of a VPC](../facts/vpc-endpoints.md#vpc-endpoints-gateway-not-extended-past-vpc)
vpc-endpoints-gateway-not-privatelink-concepts
  claim: A gateway endpoint sends traffic to Amazon S3 or DynamoDB, and unlike the other VPC endpoint types it does not use AWS PrivateLink.
  scope: VPC endpoint types.
  link: [Gateway endpoints do not use AWS PrivateLink](../facts/vpc-endpoints.md#vpc-endpoints-gateway-not-privatelink-concepts)
  link: [send traffic to Amazon S3 or DynamoDB](../facts/vpc-endpoints.md#vpc-endpoints-gateway-not-privatelink-concepts)
vpc-endpoints-gateway-region-only
  claim: A gateway endpoint is available only in the Region where you created it, so create it in the same Region as your S3 buckets or DynamoDB tables.
  scope: gateway endpoint for Amazon S3 and DynamoDB.
  link: [only in the Region where you created it](../facts/vpc-endpoints.md#vpc-endpoints-gateway-region-only)
  link: [same Region as your S3 buckets](../facts/vpc-endpoints.md#vpc-endpoints-gateway-region-only)
vpc-endpoints-gateway-s3-no-sourceip-use-vpcsourceip
  claim: You cannot use the aws:SourceIp condition in an identity policy or bucket policy for requests to Amazon S3 that traverse a VPC endpoint; use the aws:VpcSourceIp condition instead, or use route tables to control which EC2 instances can use the endpoint.
  scope: VPC endpoint for Amazon S3.
  link: [can't use the `aws:SourceIp` condition](../facts/vpc-endpoints.md#vpc-endpoints-gateway-s3-no-sourceip-use-vpcsourceip)
  link: [use the `aws:VpcSourceIp` condition](../facts/vpc-endpoints.md#vpc-endpoints-gateway-s3-no-sourceip-use-vpcsourceip)
vpc-endpoints-gateway-security-groups-must-allow
  claim: Instances that reach Amazon S3 or DynamoDB through a gateway endpoint use the service's public endpoint, so their security groups must allow traffic to and from the service.
  scope: gateway endpoint.
  link: [they access the service using its public endpoint](../facts/vpc-endpoints.md#vpc-endpoints-gateway-security-groups-must-allow)
  link: [must allow traffic to and from the service](../facts/vpc-endpoints.md#vpc-endpoints-gateway-security-groups-must-allow)
vpc-endpoints-gwlb-endpoint-bandwidth-10-gbps
  claim: Each Gateway Load Balancer endpoint can support a bandwidth of up to 10 Gbps per Availability Zone and automatically scales up to 100 Gbps.
  scope: per Gateway Load Balancer endpoint, per Availability Zone; default; not adjustable.
  link: [up to 10 Gbps per Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-bandwidth-10-gbps)
  link: [automatically scales up to 100 Gbps](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-bandwidth-10-gbps)
  say: up to ten gigabits per second per Availability Zone | scales up to one hundred gigabits per second
vpc-endpoints-gwlb-endpoint-one-az-cannot-change-subnet
  claim: A Gateway Load Balancer endpoint uses only one Availability Zone in the consumer VPC and its subnet cannot be changed later; to use a different subnet you must create a new Gateway Load Balancer endpoint.
  scope: Gateway Load Balancer endpoint.
  link: [choose only one Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-one-az-cannot-change-subnet)
  link: [You can't change this subnet later on](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-one-az-cannot-change-subnet)
vpc-endpoints-gwlb-endpoint-one-per-az-per-service
  claim: You can create a single Gateway Load Balancer endpoint per Availability Zone per service, and you must select an Availability Zone that the Gateway Load Balancer supports.
  scope: Gateway Load Balancer endpoint.
  link: [single Gateway Load Balancer endpoint per Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-one-per-az-per-service)
vpc-endpoints-gwlb-endpoint-returns-responses-only
  claim: A Gateway Load Balancer endpoint service cannot initiate requests to resources in your VPC through the endpoint, which only returns responses to traffic that resources in your VPC initiated; the provider must accept the connection request first.
  scope: Gateway Load Balancer endpoint.
  link: [can't initiate requests to resources in your VPC](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-returns-responses-only)
  link: [only returns responses to traffic that was initiated](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-returns-responses-only)
vpc-endpoints-gwlb-endpoint-route-target-no-prefix-list
  claim: You specify a Gateway Load Balancer endpoint as a route table target by its ID, and when it is the target you cannot specify a prefix list as the destination.
  scope: Gateway Load Balancer endpoint.
  link: [cannot specify a prefix list as a destination](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-route-target-no-prefix-list)
  link: [Gateway Load Balancer endpoint as a target](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-endpoint-route-target-no-prefix-list)
vpc-endpoints-gwlb-fleet-of-appliances-service
  claim: A Gateway Load Balancer distributes traffic to a fleet of network virtual appliances for security inspection, compliance, policy controls and other services; the provider specifies it when creating an endpoint service and other principals use it through a Gateway Load Balancer endpoint.
  scope: Gateway Load Balancer endpoint.
  link: [fleet of network virtual appliances](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-fleet-of-appliances-service)
  link: [creating a Gateway Load Balancer endpoint](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-fleet-of-appliances-service)
vpc-endpoints-gwlb-no-private-dns-names
  claim: Private DNS names are not supported for Gateway Load Balancer endpoints.
  scope: Gateway Load Balancer endpoint.
  link: [Private DNS names are not supported](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-no-private-dns-names)
vpc-endpoints-gwlb-routed-by-route-table
  claim: You route traffic from your VPC to a Gateway Load Balancer endpoint using route tables, and the Gateway Load Balancer distributes the traffic to the virtual appliances and can scale with demand.
  scope: Gateway Load Balancer endpoint.
  link: [route traffic from your VPC to the Gateway](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-routed-by-route-table)
  link: [using route tables](../facts/vpc-endpoints.md#vpc-endpoints-gwlb-routed-by-route-table)
vpc-endpoints-interface-aws-service-accepts-automatically
  claim: AWS services accept connection requests from interface endpoints automatically, and the service cannot initiate requests to resources through the VPC endpoint.
  scope: interface endpoint to an AWS service.
  link: [accept connection requests automatically](../facts/vpc-endpoints.md#vpc-endpoints-interface-aws-service-accepts-automatically)
  link: [can't initiate requests to resources](../facts/vpc-endpoints.md#vpc-endpoints-interface-aws-service-accepts-automatically)
vpc-endpoints-interface-dns-records-public-ips-private
  claim: The DNS names of an interface endpoint are publicly resolvable, but DNS requests from outside the VPC still return the private IP addresses of the endpoint network interfaces, which cannot be used to reach the service without access to the VPC.
  scope: interface endpoint DNS.
  link: [DNS names are publicly resolvable](../facts/vpc-endpoints.md#vpc-endpoints-interface-dns-records-public-ips-private)
  link: [unless you have access to the VPC](../facts/vpc-endpoints.md#vpc-endpoints-interface-dns-records-public-ips-private)
vpc-endpoints-interface-eni-ip-stable
  claim: The IP addresses of an endpoint network interface do not change during the lifetime of its VPC endpoint.
  scope: interface endpoint.
  link: [will not change during the lifetime](../facts/vpc-endpoints.md#vpc-endpoints-interface-eni-ip-stable)
vpc-endpoints-interface-multi-az-round-robin
  claim: In the guide's example of an interface endpoint for Amazon CloudWatch with endpoint network interfaces in two Availability Zones, a resource that accesses CloudWatch by its public endpoint is resolved to a healthy endpoint network interface selected with the round robin algorithm.
  scope: interface endpoint.
  link: [using the round robin algorithm](../facts/vpc-endpoints.md#vpc-endpoints-interface-multi-az-round-robin)
  link: [select a healthy endpoint network interface](../facts/vpc-endpoints.md#vpc-endpoints-interface-multi-az-round-robin)
vpc-endpoints-interface-one-subnet-per-az
  claim: You can select one subnet per Availability Zone for an interface endpoint, and you cannot select multiple subnets from the same Availability Zone.
  scope: interface endpoint.
  link: [one subnet per Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-interface-one-subnet-per-az)
  link: [can't select multiple subnets](../facts/vpc-endpoints.md#vpc-endpoints-interface-one-subnet-per-az)
vpc-endpoints-interface-private-dns-hidden-zone
  claim: If you enable private DNS for an interface endpoint and the VPC has both DNS hostnames and DNS resolution enabled, AWS creates a hidden AWS-managed private hosted zone that resolves the service's default DNS name to the private IP addresses of the endpoint network interfaces.
  scope: interface endpoint private DNS.
  link: [hidden, AWS-managed private hosted zone](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-hidden-zone)
  link: [DNS hostnames and DNS resolution](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-hidden-zone)
vpc-endpoints-interface-private-dns-no-app-change
  claim: If you enable private DNS for an interface endpoint and the VPC has both DNS hostnames and DNS resolution enabled, AWS creates a hidden, AWS-managed private hosted zone, so existing applications that send requests to the AWS service on its public Regional endpoint go through the endpoint network interfaces without any change to those applications.
  scope: interface endpoint private DNS; the VPC has both DNS hostnames and DNS resolution enabled.
  link: [without requiring that you make any changes](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-no-app-change)
  link: [public Regional endpoint](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-no-app-change)
vpc-endpoints-interface-private-dns-recommended
  claim: AWS recommends enabling private DNS names for VPC endpoints for AWS services, so that requests to the public service endpoints, such as requests made through an AWS SDK, resolve to your VPC endpoint.
  scope: interface endpoint private DNS.
  link: [recommend that you enable private DNS names](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-recommended)
  link: [resolve to your VPC endpoint](../facts/vpc-endpoints.md#vpc-endpoints-interface-private-dns-recommended)
vpc-endpoints-interface-single-az-impairment
  claim: An interface endpoint with a network interface in only one Availability Zone serves traffic from all subnets of the VPC, but if that zone is impaired, resources in the other zone lose access to the service.
  scope: interface endpoint.
  link: [lose access to Amazon CloudWatch](../facts/vpc-endpoints.md#vpc-endpoints-interface-single-az-impairment)
  link: [single Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-interface-single-az-impairment)
vpc-endpoints-interface-traffic-resolves-to-endpoint-eni
  claim: With an interface endpoint, you first create the endpoint, which connects the subnets of your VPC to the AWS service using network interfaces; traffic destined for the service is resolved by DNS to the private IP addresses of those network interfaces and then sent to the service over the endpoint connection.
  scope: interface endpoint.
  link: [resolved to the private IP addresses](../facts/vpc-endpoints.md#vpc-endpoints-interface-traffic-resolves-to-endpoint-eni)
  link: [establishes connections between the subnets in your VPC](../facts/vpc-endpoints.md#vpc-endpoints-interface-traffic-resolves-to-endpoint-eni)
vpc-endpoints-interface-two-azs-for-production
  claim: For high availability in production, configure at least two Availability Zones per VPC endpoint and deploy the AWS resources that must access the service in those zones.
  scope: interface endpoint.
  link: [at least two Availability Zones per VPC endpoint](../facts/vpc-endpoints.md#vpc-endpoints-interface-two-azs-for-production)
vpc-endpoints-mss-clamping-all-packets
  claim: VPC endpoints enforce Maximum Segment Size (MSS) clamping for all packets.
  scope: all packets through a VPC endpoint.
  link: [Maximum Segment Size (MSS) clamping](../facts/vpc-endpoints.md#vpc-endpoints-mss-clamping-all-packets)
vpc-endpoints-mtu-8500-larger-packets-dropped
  claim: A VPC endpoint supports an MTU of 8500 bytes, and packets larger than 8500 bytes that arrive at the VPC endpoint are dropped.
  scope: per VPC endpoint; maximum; not adjustable.
  link: [MTU of 8500 bytes](../facts/vpc-endpoints.md#vpc-endpoints-mtu-8500-larger-packets-dropped)
  link: [larger than 8500 bytes](../facts/vpc-endpoints.md#vpc-endpoints-mtu-8500-larger-packets-dropped)
  say: an M T U of eighty-five hundred bytes
vpc-endpoints-no-path-mtu-discovery
  claim: Path MTU Discovery (PMTUD) is not supported: VPC endpoints do not generate the ICMP Destination Unreachable, Fragmentation needed and Don't Fragment was Set message (Type 3, Code 4).
  scope: VPC endpoints.
  link: [Path MTU Discovery (PMTUD) is not supported](../facts/vpc-endpoints.md#vpc-endpoints-no-path-mtu-discovery)
vpc-endpoints-policy-default-allows-all-concepts
  claim: A VPC endpoint policy is an IAM resource policy attached to a VPC endpoint that determines which principals can use the endpoint to reach the service, and the default policy allows all actions by all principals on all resources over the endpoint.
  scope: VPC endpoint policy; default; not adjustable.
  link: [default VPC endpoint policy allows all actions](../facts/vpc-endpoints.md#vpc-endpoints-policy-default-allows-all-concepts)
  link: [IAM resource policy that you attach](../facts/vpc-endpoints.md#vpc-endpoints-policy-default-allows-all-concepts)
vpc-endpoints-policy-default-grants-full-access
  claim: The default endpoint policy grants full access to the endpoint.
  scope: VPC endpoint policy; default; not adjustable.
  link: [grants full access to the endpoint](../facts/vpc-endpoints.md#vpc-endpoints-policy-default-grants-full-access)
vpc-endpoints-policy-does-not-override-identity-or-resource-policies
  claim: An endpoint policy does not override or replace identity-based or resource-based policies; for example, with an interface endpoint to Amazon S3 you can still use S3 bucket policies to control access from specific endpoints or VPCs.
  scope: VPC endpoint policy.
  link: [does not override or replace identity-based policies](../facts/vpc-endpoints.md#vpc-endpoints-policy-does-not-override-identity-or-resource-policies)
vpc-endpoints-policy-gateway-principal-star-use-principalarn
  claim: With gateway endpoints the Principal element of the endpoint policy must be set to *, and you specify a principal with the aws:PrincipalArn condition key.
  scope: gateway endpoint policy.
  link: [Principal element must be set to](../facts/vpc-endpoints.md#vpc-endpoints-policy-gateway-principal-star-use-principalarn)
  link: [aws:PrincipalArn](../facts/vpc-endpoints.md#vpc-endpoints-policy-gateway-principal-star-use-principalarn)
vpc-endpoints-policy-json-iam-language-principal-required
  claim: An endpoint policy is a JSON policy document in the IAM policy language and must contain a Principal element.
  scope: VPC endpoint policy.
  link: [must contain a Principal element](../facts/vpc-endpoints.md#vpc-endpoints-policy-json-iam-language-principal-required)
  link: [JSON policy document](../facts/vpc-endpoints.md#vpc-endpoints-policy-json-iam-language-principal-required)
vpc-endpoints-policy-not-all-services-full-access-otherwise
  claim: Not all AWS services support endpoint policies, and if an AWS service does not support them, full access is allowed to any endpoint for that service.
  scope: VPC endpoint policy.
  link: [Not all AWS services support endpoint policies](../facts/vpc-endpoints.md#vpc-endpoints-policy-not-all-services-full-access-otherwise)
  link: [we allow full access to any endpoint](../facts/vpc-endpoints.md#vpc-endpoints-policy-not-all-services-full-access-otherwise)
vpc-endpoints-policy-other-endpoint-services-full-access
  claim: When you create a VPC endpoint for an endpoint service other than an AWS service, full access is allowed to the endpoint.
  scope: VPC endpoint policy.
  link: [other than an AWS service](../facts/vpc-endpoints.md#vpc-endpoints-policy-other-endpoint-services-full-access)
vpc-endpoints-policy-single-policy-default-if-none
  claim: When you create an interface or gateway endpoint for an AWS service you can attach a single endpoint policy, update it at any time, and if you attach none, AWS attaches the default endpoint policy.
  scope: VPC endpoint policy; default; not adjustable.
  link: [attach a single endpoint policy to the endpoint](../facts/vpc-endpoints.md#vpc-endpoints-policy-single-policy-default-if-none)
  link: [we attach the default endpoint policy](../facts/vpc-endpoints.md#vpc-endpoints-policy-single-policy-default-if-none)
vpc-endpoints-policy-update-takes-minutes
  claim: After you update an endpoint policy it can take a few minutes for the changes to take effect.
  scope: VPC endpoint policy.
  link: [it can take a few minutes](../facts/vpc-endpoints.md#vpc-endpoints-policy-update-takes-minutes)
vpc-endpoints-pricing-data-processing-per-gb-any-direction
  claim: Data processing charges apply for each gigabyte processed through a VPC endpoint, regardless of the traffic's source or destination.
  scope: per GB processed through a VPC endpoint.
  link: [each Gigabyte processed through the VPC endpoint](../facts/vpc-endpoints.md#vpc-endpoints-pricing-data-processing-per-gb-any-direction)
  say: per gigabyte processed, in any direction
vpc-endpoints-pricing-example-tier-rates-per-gb
  claim: In the PrivateLink pricing example for a resource endpoint (prices in USD for us-east-1), you pay a data processing charge of $0.01 per GB for the first PB, $0.006 per GB for next 4PB, and $0.004 per GB for 5+ PBs.
  scope: resource endpoint pricing example, data processing per GB, us-east-1.
  link: [$0.01 per GB for the first PB](../facts/vpc-endpoints.md#vpc-endpoints-pricing-example-tier-rates-per-gb)
  link: [$0.006 per GB for next 4PB](../facts/vpc-endpoints.md#vpc-endpoints-pricing-example-tier-rates-per-gb)
  link: [$0.004 per GB for 5+ PBs](../facts/vpc-endpoints.md#vpc-endpoints-pricing-example-tier-rates-per-gb)
  say: one cent per gigabyte for the first petabyte
vpc-endpoints-pricing-hourly-per-az-while-provisioned
  claim: You are billed for each hour that a VPC endpoint remains provisioned in each Availability Zone, whatever the state of its association with the service.
  scope: per VPC endpoint, per Availability Zone, per hour.
  link: [remains provisioned in each Availability Zone](../facts/vpc-endpoints.md#vpc-endpoints-pricing-hourly-per-az-while-provisioned)
  say: per hour per Availability Zone while provisioned
vpc-endpoints-pricing-hourly-stops-on-delete
  claim: Hourly billing for a VPC endpoint stops when you delete it.
  scope: per VPC endpoint.
  link: [stop when you delete it](../facts/vpc-endpoints.md#vpc-endpoints-pricing-hourly-stops-on-delete)
  say: billing stops when you delete the endpoint
vpc-endpoints-pricing-interface-tiers-apply-region-total
  claim: Interface endpoint data processing pricing tiers apply to the total data processed by all interface endpoints in an AWS Region.
  scope: all interface endpoints in one AWS Region, per month.
  link: [total data processed by all Interface Endpoints](../facts/vpc-endpoints.md#vpc-endpoints-pricing-interface-tiers-apply-region-total)
  say: tiers apply to the Region total
vpc-endpoints-pricing-partial-hour-billed-as-full
  claim: Each partial VPC endpoint hour is billed as a full hour.
  scope: per VPC endpoint-hour.
  link: [billed as a full hour](../facts/vpc-endpoints.md#vpc-endpoints-pricing-partial-hour-billed-as-full)
  say: a partial hour counts as a full hour
vpc-endpoints-pricing-resource-tunnel-tiers-separate
  claim: Resource and tunnel endpoint data processing tiers apply to the total data processed in a Region through those endpoints, separately for resource endpoints and for tunnel endpoints.
  scope: resource and tunnel endpoints in one AWS Region.
  link: [apply to Resource and Tunnel Endpoints separately](../facts/vpc-endpoints.md#vpc-endpoints-pricing-resource-tunnel-tiers-separate)
vpc-endpoints-public-endpoint-via-igw-stays-on-aws-network
  claim: Without an endpoint, traffic to an AWS service from an instance in a public subnet goes to the internet gateway and then to the service, and from a private subnet it goes to a NAT gateway, then the internet gateway, then the service; while this traffic traverses the internet gateway, it does not leave the AWS network.
  scope: public AWS service endpoints.
  link: [it does not leave the AWS network](../facts/vpc-endpoints.md#vpc-endpoints-public-endpoint-via-igw-stays-on-aws-network)
vpc-endpoints-quota-gateway-endpoints
  claim: A Region has a default of 20 gateway VPC endpoints, the quota is adjustable, and you can create up to 255 gateway endpoints per VPC.
  scope: gateway VPC endpoints per Region; default; adjustable; up to 255 gateway endpoints per VPC.
  link: [20](../facts/vpc-endpoints.md#vpc-endpoints-quota-gateway-endpoints)
  link: [up to 255 gateway endpoints per VPC](../facts/vpc-endpoints.md#vpc-endpoints-quota-gateway-endpoints)
  say: twenty gateway endpoints per Region | up to two hundred fifty-five gateway endpoints per VPC
vpc-endpoints-quota-interface-gwlb-per-vpc
  claim: A VPC has a default of 50 interface and Gateway Load Balancer endpoints, and the quota is adjustable; it is one combined quota for both endpoint types.
  scope: interface and Gateway Load Balancer endpoints per VPC; default; adjustable; combined quota for interface endpoints and Gateway Load Balancer endpoints.
  link: [50](../facts/vpc-endpoints.md#vpc-endpoints-quota-interface-gwlb-per-vpc)
  say: fifty interface and Gateway Load Balancer endpoints per VPC
vpc-endpoints-quota-policy-characters
  claim: A VPC endpoint policy can hold 20,480 characters including white space, and this quota is not adjustable.
  scope: characters per VPC endpoint policy; maximum; not adjustable; the maximum size of a VPC endpoint policy, including white space.
  link: [20,480](../facts/vpc-endpoints.md#vpc-endpoints-quota-policy-characters)
  say: twenty thousand four hundred eighty characters
vpc-endpoints-quota-resource-endpoints-per-vpc
  claim: A VPC has a default of 200 resource VPC endpoints, and the quota is adjustable.
  scope: resource VPC endpoints per VPC; default; adjustable.
  link: [200](../facts/vpc-endpoints.md#vpc-endpoints-quota-resource-endpoints-per-vpc)
  say: two hundred resource endpoints per VPC
vpc-endpoints-quota-service-network-endpoints-per-vpc
  claim: A VPC has a default of 50 service network VPC endpoints, and the quota is adjustable.
  scope: service network VPC endpoints per VPC; default; adjustable.
  link: [50](../facts/vpc-endpoints.md#vpc-endpoints-quota-service-network-endpoints-per-vpc)
  say: fifty service network endpoints per VPC
vpc-endpoints-quotas-are-region-specific
  claim: Unless a PrivateLink quota is noted otherwise, the quota is Region-specific.
  scope: AWS PrivateLink and VPC endpoint quotas.
  link: [Region-specific](../facts/vpc-endpoints.md#vpc-endpoints-quotas-are-region-specific)
  say: counted per Region
vpc-endpoints-resource-endpoint-no-load-balancer
  claim: Resource endpoints do not require a load balancer, so you can access the VPC resource directly.
  scope: resource VPC endpoint.
  link: [don't require a load balancer](../facts/vpc-endpoints.md#vpc-endpoints-resource-endpoint-no-load-balancer)
  link: [access the VPC resource directly](../facts/vpc-endpoints.md#vpc-endpoints-resource-endpoint-no-load-balancer)
vpc-endpoints-resource-endpoint-private-access
  claim: A resource endpoint lets you privately access a resource such as a database, an EC2 instance, an application endpoint, a domain-name target or an IP address in another VPC or on premises; without it you need an internet gateway or an interface endpoint with a Network Load Balancer.
  scope: resource VPC endpoint.
  link: [resource endpoint lets you privately and securely access](../facts/vpc-endpoints.md#vpc-endpoints-resource-endpoint-private-access)
  link: [Without resource endpoints](../facts/vpc-endpoints.md#vpc-endpoints-resource-endpoint-private-access)
vpc-endpoints-s3-bucket-policy-vpce-blocks-console
  claim: The guide's example bucket policy denies access to the specified bucket using the specified actions unless the specified gateway endpoint is used, and the guide notes that this policy also blocks access to the bucket using those actions through the AWS Management Console.
  scope: Amazon S3 bucket policy with a gateway endpoint.
  link: [unless the specified gateway endpoint is used](../facts/vpc-endpoints.md#vpc-endpoints-s3-bucket-policy-vpce-blocks-console)
  link: [blocks access to the specified bucket](../facts/vpc-endpoints.md#vpc-endpoints-s3-bucket-policy-vpce-blocks-console)
vpc-endpoints-s3-private-dns-default-pays-interface
  claim: If you configure private DNS for the S3 interface endpoint without the inbound-Resolver-only option, requests from both on premises and the VPC use the interface endpoint, so you pay for it for VPC traffic instead of using the free gateway endpoint.
  scope: Amazon S3 gateway and interface endpoints.
  link: [requests from both your on-premises network](../facts/vpc-endpoints.md#vpc-endpoints-s3-private-dns-default-pays-interface)
vpc-endpoints-s3-private-dns-inbound-resolver-saves-cost
  claim: With private DNS only for the inbound Resolver endpoint, on-premises requests use the interface endpoint for Amazon S3 and VPC requests use the gateway endpoint, so you pay for the interface endpoint only for traffic that cannot use the gateway endpoint.
  scope: Amazon S3 gateway and interface endpoints.
  link: [private DNS only for the inbound Resolver endpoint](../facts/vpc-endpoints.md#vpc-endpoints-s3-private-dns-inbound-resolver-saves-cost)
  link: [you optimize your costs](../facts/vpc-endpoints.md#vpc-endpoints-s3-private-dns-inbound-resolver-saves-cost)
vpc-endpoints-service-network-endpoint-one-network
  claim: A service-network endpoint connects your VPC to one service network and gives private access to the resources and services in it; to reach several service networks you create several service-network endpoints.
  scope: service-network VPC endpoint.
  link: [lets you connect to one service network](../facts/vpc-endpoints.md#vpc-endpoints-service-network-endpoint-one-network)
  link: [multiple service-network endpoints](../facts/vpc-endpoints.md#vpc-endpoints-service-network-endpoint-one-network)
vpc-endpoints-wa-cost08-bp02-look-for-alternatives
  claim: When selecting components to reduce data transfer cost, look for alternative architectures or additional components that remove or reduce the need for data transfer or lower its cost.
  scope: COST08-BP02.
  link: [alternative architectures or additional components](../facts/vpc-endpoints.md#vpc-endpoints-wa-cost08-bp02-look-for-alternatives)
vpc-endpoints-wa-cost08-bp03-review-where-costs-are
  claim: To choose network services that reduce data transfer cost, look at where the largest costs and highest volume flows are, and assess whether a service reduces or removes that transfer, specifically networking and content delivery services.
  scope: COST08-BP03.
  link: [largest costs and highest volume flows](../facts/vpc-endpoints.md#vpc-endpoints-wa-cost08-bp03-review-where-costs-are)
vpc-endpoints-wa-cost08-gateway-free-interface-hourly
  claim: Gateway VPC endpoints have no hourly charges and support Amazon S3 and DynamoDB, while interface VPC endpoints, provided by AWS PrivateLink, have an hourly fee and a per-GB usage cost.
  scope: VPC endpoints.
  link: [Gateway VPC endpoints have no hourly charges](../facts/vpc-endpoints.md#vpc-endpoints-wa-cost08-gateway-free-interface-hourly)
  link: [hourly fee and per-GB usage cost](../facts/vpc-endpoints.md#vpc-endpoints-wa-cost08-gateway-free-interface-hourly)
vpc-endpoints-wa-cost08-nat-gateway-vs-endpoints
  claim: Place NAT gateways in the same Availability Zones as high traffic instances and consider VPC endpoints for instances that access Amazon DynamoDB or Amazon S3 to reduce data transfer and processing costs.
  scope: NAT gateway and VPC endpoints.
  link: [consider using VPC endpoints for the instances that need to access Amazon DynamoDB or Amazon S3](../facts/vpc-endpoints.md#vpc-endpoints-wa-cost08-nat-gateway-vs-endpoints)
vpc-endpoints-wp-central-endpoints-cost-reason
  claim: An interface endpoint costs money for every hour it runs plus data processing, and by default you create one in every VPC that needs the service; hosting the interface endpoints in a centralized VPC lets spoke VPCs use them through a transit gateway.
  scope: centralized interface endpoints.
  link: [a cost is incurred for every hour](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-cost-reason)
  link: [host the interface endpoints in a centralized VPC](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-cost-reason)
vpc-endpoints-wp-central-endpoints-need-own-private-hosted-zone
  claim: The AWS-managed private hosted zone for an interface endpoint works only within the VPC that has the endpoint, so for centralized endpoints you turn off the automatic private DNS option, create your own Route 53 private hosted zone with an alias record to the endpoint, and associate it with the other VPCs.
  scope: centralized interface endpoints.
  link: [managed PHZ won’t work](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-need-own-private-hosted-zone)
  link: [disable the option that automatically creates](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-need-own-private-hosted-zone)
vpc-endpoints-wp-central-endpoints-policy-tradeoff
  claim: A distributed approach with an endpoint per VPC lets you apply least privilege policies on VPC endpoints, while in a centralized approach you manage the policies for all spoke VPC access on a single endpoint; the whitepaper says that with a growing number of VPCs the complexity of maintaining least privilege with a single policy document might grow, and a single policy document results in a larger blast radius.
  scope: centralized interface endpoints.
  link: [results in larger blast radius](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-policy-tradeoff)
  link: [least privilege policies on VPC endpoints](../facts/vpc-endpoints.md#vpc-endpoints-wp-central-endpoints-policy-tradeoff)
vpc-endpoints-wp-cross-region-endpoint-transfer-charges
  claim: Inter-Region data transfer charges apply when you access endpoints across Regions.
  scope: centralized interface endpoints across Regions.
  link: [Inter-Region data transfer charges do apply](../facts/vpc-endpoints.md#vpc-endpoints-wp-cross-region-endpoint-transfer-charges)
vpc-endpoints-wp-gateway-endpoint-no-additional-charge
  claim: There is no additional charge for using gateway endpoints, which are used to access Amazon S3 and DynamoDB privately; standard charges for data transfer and resource usage still apply.
  scope: gateway endpoints.
  link: [no additional charge for using gateway endpoints](../facts/vpc-endpoints.md#vpc-endpoints-wp-gateway-endpoint-no-additional-charge)
  link: [Standard charges for data transfer and resource usage](../facts/vpc-endpoints.md#vpc-endpoints-wp-gateway-endpoint-no-additional-charge)
vpc-endpoints-wp-interface-endpoints-reachable-from-onprem
  claim: Interface endpoints are also accessible from on-premises networks over VPN and Direct Connect, using conditional forwarding rules that send DNS traffic for the full service endpoint names to Route 53 Resolver inbound endpoints.
  scope: interface endpoints.
  link: [accessible from on-premises networks over VPN](../facts/vpc-endpoints.md#vpc-endpoints-wp-interface-endpoints-reachable-from-onprem)
  link: [Route 53 Resolver inbound endpoints](../facts/vpc-endpoints.md#vpc-endpoints-wp-interface-endpoints-reachable-from-onprem)
vpc-endpoints-wp-one-policy-per-endpoint-no-override
  claim: You cannot attach more than one endpoint policy to an endpoint, but you can modify it at any time; an endpoint policy does not override or replace IAM user policies or service-specific policies such as Amazon S3 bucket policies.
  scope: VPC endpoint policy.
  link: [cannot attach more than one policy](../facts/vpc-endpoints.md#vpc-endpoints-wp-one-policy-per-endpoint-no-override)
  link: [does not override or replace IAM user policies](../facts/vpc-endpoints.md#vpc-endpoints-wp-one-policy-per-endpoint-no-override)
vpc-peering-accept-not-own-request
  claim: You cannot accept a peering request that you sent to another AWS account; within one account you can create and accept the request yourself.
  scope: VPC peering connection request.
  link: [can't accept a VPC peering connection request](../facts/vpc-peering.md#vpc-peering-accept-not-own-request)
vpc-peering-accept-only-trusted-accounts
  claim: Do not accept VPC peering connection requests from unknown AWS accounts: a malicious user may send a request to gain unauthorized network access to your VPC, which is known as peer phishing; you can safely reject unwanted VPC peering connection requests without any risk of the requester gaining access to information about your account or VPC.
  scope: VPC peering connection request.
  link: [peer phishing](../facts/vpc-peering.md#vpc-peering-accept-only-trusted-accounts)
  link: [reject unwanted VPC peering connection requests](../facts/vpc-peering.md#vpc-peering-accept-only-trusted-accounts)
vpc-peering-accounts-and-regions
  claim: A VPC peering connection can join your own VPCs or a VPC in another AWS account, and the VPCs can be in different Regions (an inter-Region VPC peering connection).
  scope: VPC peering connection.
  link: [with a VPC in another AWS account](../facts/vpc-peering.md#vpc-peering-accounts-and-regions)
  link: [The VPCs can be in different Regions](../facts/vpc-peering.md#vpc-peering-accounts-and-regions)
vpc-peering-active-delete-not-reject
  claim: While a peering connection is active, either VPC owner can delete it but cannot reject it.
  scope: VPC peering connection in the active state.
  link: [either of the VPC owners can delete](../facts/vpc-peering.md#vpc-peering-active-delete-not-reject)
  link: [but cannot reject it](../facts/vpc-peering.md#vpc-peering-active-delete-not-reject)
vpc-peering-active-status-despite-regional-event
  claim: If an event in the Region of a peered VPC prevents the flow of traffic, the status of the peering connection remains Active.
  scope: VPC peering connection status.
  link: [remains `Active`](../facts/vpc-peering.md#vpc-peering-active-status-despite-regional-event)
  link: [prevents the flow of traffic](../facts/vpc-peering.md#vpc-peering-active-status-despite-regional-event)
vpc-peering-billing-usage-type-2025
  claim: Since April 11, 2025 the bill shows same-Region, cross-Availability Zone VPC peering data under its own VPC peering usage type instead of the intra-Region data transfer usage; the prices did not change.
  scope: VPC peering within one Region.
  link: [no changes to the pricing](../facts/vpc-peering.md#vpc-peering-billing-usage-type-2025)
  link: [April 11, 2025](../facts/vpc-peering.md#vpc-peering-billing-usage-type-2025)
  say: only the usage type changed; the price did not | April eleventh, twenty twenty-five
  changed: 2025-04-11: was intra-regional Data Transfer usage
vpc-peering-blog-same-az-free-cross-az-charged
  claim: Data transfer over a VPC peering connection that stays within an Availability Zone is free, and data transfer that crosses Availability Zones incurs a data transfer charge for ingress and egress traffic.
  scope: VPC peering data transfer.
  link: [stays within an Availability Zone is free](../facts/vpc-peering.md#vpc-peering-blog-same-az-free-cross-az-charged)
  link: [crosses Availability Zones will incur](../facts/vpc-peering.md#vpc-peering-blog-same-az-free-cross-az-charged)
vpc-peering-change-newest-history-row-2020
  claim: The VPC peering guide's document history lists Tag on create, dated July 20, 2020: you can add tags when you create a VPC peering connection and route table.
  link: [July 20, 2020](../facts/vpc-peering.md#vpc-peering-change-newest-history-row-2020)
  say: July 2020
vpc-peering-config-entire-vpc-route
  claim: With a route to the entire peer VPC, any resource in one VPC can communicate with any resource in the peer VPC and management is simpler, but all traffic between the VPCs flows through the peering connection.
  scope: VPC peering route configuration.
  link: [simplifying management](../facts/vpc-peering.md#vpc-peering-config-entire-vpc-route)
  link: [any resource in one VPC to communicate](../facts/vpc-peering.md#vpc-peering-config-entire-vpc-route)
vpc-peering-config-specific-routes
  claim: With specific routes, you send only traffic for particular subnets or resources of the peer VPC through the peering connection, which limits traffic to what is necessary but needs more maintenance when resources are added.
  scope: VPC peering route configuration.
  link: [more granular routes](../facts/vpc-peering.md#vpc-peering-config-specific-routes)
  link: [requires more maintenance](../facts/vpc-peering.md#vpc-peering-config-specific-routes)
vpc-peering-cross-az-data-transfer-price
  claim: Data sent over a VPC peering connection that crosses an Availability Zone within the same Region is charged $0.01/GB in both the In and the Out direction; peering traffic that stays within an Availability Zone is free.
  scope: per GB over a VPC peering connection in one Region; cross-AZ inside the same Region is charged; traffic that stays within an Availability Zone is free.
  link: [$0.01/GB in both "In" and "Out" direction](../facts/vpc-peering.md#vpc-peering-cross-az-data-transfer-price)
  link: [stays within an Availability Zone is free](../facts/vpc-peering.md#vpc-peering-cross-az-data-transfer-price)
  say: one cent per gigabyte each way | free inside one Availability Zone
vpc-peering-def-private-ipv4-ipv6
  claim: A VPC peering connection is a networking connection between two VPCs that routes traffic between them using private IPv4 or IPv6 addresses, so instances in either VPC communicate as if they were in the same network.
  scope: VPC peering connection.
  link: [route traffic between them using private IPv4 addresses or IPv6 addresses](../facts/vpc-peering.md#vpc-peering-def-private-ipv4-ipv6)
  link: [as if they are within the same network](../facts/vpc-peering.md#vpc-peering-def-private-ipv4-ipv6)
vpc-peering-delete-by-either-owner
  claim: An active peering connection can be deleted by either VPC owner, and a pending-acceptance request can be deleted by the requester VPC owner.
  scope: VPC peering connection.
  link: [deleted by either of the VPC owners](../facts/vpc-peering.md#vpc-peering-delete-by-either-owner)
  link: [deleted by the owner of the requester VPC](../facts/vpc-peering.md#vpc-peering-delete-by-either-owner)
vpc-peering-deleted-connection-visibility
  claim: A deleted VPC peering connection remains visible to the party that deleted it for 2 hours and to the other party for 2 days; if it was created within the same AWS account, the deleted request remains visible for 2 hours.
  scope: per deleted VPC peering connection; fixed; not adjustable.
  link: [visible to the party that deleted it for 2 hours](../facts/vpc-peering.md#vpc-peering-deleted-connection-visibility)
  link: [visible to the other party for 2 days](../facts/vpc-peering.md#vpc-peering-deleted-connection-visibility)
  say: two hours for the deleting party | two days for the other party
vpc-peering-dns-default-public-resolution
  claim: With the default peering connection options, a public DNS hostname of an instance in the peer VPC resolves to that instance's public IP address; you change this by enabling DNS hostname resolution for the peering connection.
  scope: VPC peering connection DNS setting; default; not adjustable.
  link: [With the default VPC peering connection options](../facts/vpc-peering.md#vpc-peering-dns-default-public-resolution)
  link: [resolves to the public IP address of the EC2 instance](../facts/vpc-peering.md#vpc-peering-dns-default-public-resolution)
vpc-peering-dns-each-owner-modifies-own-side
  claim: The requester VPC owner modifies the requester peering options and the accepter VPC owner modifies the accepter options; if both VPCs are in the same account you can enable both at the same time, in the same Region or across Regions.
  scope: VPC peering connection DNS setting.
  link: [must modify the requester VPC peering options](../facts/vpc-peering.md#vpc-peering-dns-each-owner-modifies-own-side)
  link: [at the same time](../facts/vpc-peering.md#vpc-peering-dns-each-owner-modifies-own-side)
vpc-peering-dns-enabled-private-resolution
  claim: After you enable DNS hostname resolution for the peering connection, a public DNS hostname of an instance in the peer VPC resolves to that instance's private IP address.
  scope: VPC peering connection DNS setting.
  link: [After enabling DNS hostname resolution](../facts/vpc-peering.md#vpc-peering-dns-enabled-private-resolution)
  link: [resolves to the private IP address of the EC2 instance](../facts/vpc-peering.md#vpc-peering-dns-enabled-private-resolution)
vpc-peering-dns-needs-active-not-at-creation
  claim: The peering connection must be in the active state to enable DNS resolution; you cannot enable DNS resolution when you create a peering connection.
  scope: VPC peering connection DNS setting.
  link: [can't enable DNS resolution when you create](../facts/vpc-peering.md#vpc-peering-dns-needs-active-not-at-creation)
  link: [must be in the `active` state](../facts/vpc-peering.md#vpc-peering-dns-needs-active-not-at-creation)
vpc-peering-dns-non-rfc1918-needs-resolution-support
  claim: If the IPv4 CIDR block of a peered VPC is outside the RFC 1918 private ranges, private DNS hostnames for that VPC cannot be resolved to private IP addresses unless you enable DNS resolution support for the peering connection.
  scope: VPC peering connection DNS setting.
  link: [private DNS hostnames for that VPC](../facts/vpc-peering.md#vpc-peering-dns-non-rfc1918-needs-resolution-support)
vpc-peering-dns-requires-vpc-attributes
  claim: To enable DNS resolution for a peering connection, both VPCs must be enabled for DNS hostnames and DNS resolution.
  scope: VPC peering connection DNS setting.
  link: [Both VPCs must be enabled for DNS hostnames](../facts/vpc-peering.md#vpc-peering-dns-requires-vpc-attributes)
vpc-peering-edge-no-direct-connect
  claim: If VPC A has a Direct Connect connection to a corporate network, resources in the peer VPC B cannot use that Direct Connect connection to reach the corporate network.
  scope: VPC peering connection, edge to edge routing.
  link: [can't use the Direct Connect connection](../facts/vpc-peering.md#vpc-peering-edge-no-direct-connect)
  link: [corporate network](../facts/vpc-peering.md#vpc-peering-edge-no-direct-connect)
vpc-peering-edge-no-gateway-endpoint
  claim: If VPC A has a gateway endpoint for Amazon S3, resources in the peer VPC B cannot use that gateway endpoint to reach Amazon S3.
  scope: VPC peering connection, edge to edge routing.
  link: [can't use the gateway endpoint to access Amazon S3](../facts/vpc-peering.md#vpc-peering-edge-no-gateway-endpoint)
  link: [gateway endpoint that provides connectivity to Amazon S3](../facts/vpc-peering.md#vpc-peering-edge-no-gateway-endpoint)
vpc-peering-edge-no-igw
  claim: If VPC A has an internet gateway, resources in the peer VPC B cannot use that internet gateway to reach the internet.
  scope: VPC peering connection, edge to edge routing.
  link: [can't use the internet gateway in VPC A](../facts/vpc-peering.md#vpc-peering-edge-no-igw)
  link: [resources in VPC B](../facts/vpc-peering.md#vpc-peering-edge-no-igw)
vpc-peering-edge-no-nat
  claim: If VPC A has a NAT device that gives its subnets internet access, resources in the peer VPC B cannot use that NAT device to reach the internet.
  scope: VPC peering connection, edge to edge routing.
  link: [can't use the NAT device in VPC A](../facts/vpc-peering.md#vpc-peering-edge-no-nat)
  link: [to access the internet](../facts/vpc-peering.md#vpc-peering-edge-no-nat)
vpc-peering-edge-no-vpn
  claim: If VPC A has a VPN connection to a corporate network, resources in the peer VPC B cannot use that VPN connection to reach the corporate network.
  scope: VPC peering connection, edge to edge routing.
  link: [can't use the VPN connection](../facts/vpc-peering.md#vpc-peering-edge-no-vpn)
  link: [corporate network](../facts/vpc-peering.md#vpc-peering-edge-no-vpn)
vpc-peering-expired-request-visible-2-days
  claim: An expired VPC peering connection request remains visible to both VPC owners for 2 days.
  scope: per expired VPC peering connection request; fixed; not adjustable.
  link: [visible to both VPC owners for 2 days](../facts/vpc-peering.md#vpc-peering-expired-request-visible-2-days)
  say: visible for two days
vpc-peering-failed-state
  claim: A failed peering connection cannot be accepted, rejected or deleted and stays visible to the requester for 2 hours.
  scope: VPC peering connection in the failed state.
  link: [cannot be accepted, rejected, or deleted](../facts/vpc-peering.md#vpc-peering-failed-state)
  link: [remains visible to the requester for 2 hours](../facts/vpc-peering.md#vpc-peering-failed-state)
vpc-peering-faq-bandwidth-same-as-vpc
  claim: Bandwidth between instances in peered VPCs is no different from bandwidth between instances in the same VPC.
  scope: per peering connection.
  link: [no different than bandwidth between instances](../facts/vpc-peering.md#vpc-peering-faq-bandwidth-same-as-vpc)
  say: the same as inside one VPC
vpc-peering-faq-cross-account-accept
  claim: You can peer your VPC with a VPC in another AWS account if the owner of the other VPC accepts the peering connection request.
  scope: per peering connection; the other VPC owner accepts the request.
  link: [the owner of the other VPC accepts](../facts/vpc-peering.md#vpc-peering-faq-cross-account-accept)
  say: yes, once the other owner accepts
vpc-peering-faq-definition
  claim: A peering connection routes traffic between two peered VPCs using private IP addresses.
  scope: per peering connection.
  link: [route traffic via private IP addresses](../facts/vpc-peering.md#vpc-peering-faq-definition)
  say: private-IP routing between two peered VPCs
vpc-peering-faq-either-side-terminates
  claim: Either side of a VPC peering connection can terminate it at any time, and after termination traffic no longer flows between the two VPCs.
  scope: per peering connection.
  link: [can terminate the peering connection at any time](../facts/vpc-peering.md#vpc-peering-faq-either-side-terminates)
  say: either owner can end it at any time
vpc-peering-faq-encryption-enforce-to-monitor-peering
  claim: You can switch a VPC from Enforce mode back to Monitor mode, except when VPC peering exists between two VPCs without any exclusions; then you must delete the peering between the two VPCs before moving to Monitor mode.
  scope: per VPC.
  link: [delete the VPC peering between the two VPCs](../facts/vpc-peering.md#vpc-peering-faq-encryption-enforce-to-monitor-peering)
  say: delete the peering first
vpc-peering-faq-inter-region
  claim: You can create peering connections with VPCs in different Regions; inter-Region VPC peering is available in all commercial Regions except China.
  scope: per peering connection; commercial Regions, excluding China.
  link: [VPCs in different regions](../facts/vpc-peering.md#vpc-peering-faq-inter-region)
  link: [all commercial regions (excluding China)](../facts/vpc-peering.md#vpc-peering-faq-inter-region)
  say: yes, across Regions
vpc-peering-faq-inter-region-dns-public
  claim: By default, a query for the public hostname of an instance in a peered VPC in another Region resolves to a public IP address; Route 53 private DNS can resolve it to a private IP address.
  scope: per inter-Region peering connection; default; adjustable.
  link: [will resolve to a public IP address](../facts/vpc-peering.md#vpc-peering-faq-inter-region-dns-public)
  link: [Route 53 private DNS can be used to resolve to a private IP address](../facts/vpc-peering.md#vpc-peering-faq-inter-region-dns-public)
  say: a public IP by default | use Route 53 private DNS for the private IP
vpc-peering-faq-inter-region-encrypted
  claim: Inter-Region VPC peering traffic is encrypted with AEAD algorithms, and AWS handles key agreement and key management.
  scope: per inter-Region peering connection.
  link: [encrypted using modern AEAD](../facts/vpc-peering.md#vpc-peering-faq-inter-region-encrypted)
  link: [key management is handled by AWS](../facts/vpc-peering.md#vpc-peering-faq-inter-region-encrypted)
  say: encrypted | AWS manages the keys
vpc-peering-faq-inter-region-no-internet-failover
  claim: Inter-Region VPC peering traffic goes over the AWS backbone with no single point of failure, and if an inter-Region peering connection goes down, the traffic is not routed over the internet.
  scope: per inter-Region peering connection.
  link: [traffic goes over the AWS backbone](../facts/vpc-peering.md#vpc-peering-faq-inter-region-no-internet-failover)
  link: [will not be routed over the internet](../facts/vpc-peering.md#vpc-peering-faq-inter-region-no-internet-failover)
  say: it uses the AWS backbone | it never falls back to the internet
vpc-peering-faq-inter-region-no-sg-reference
  claim: Security groups cannot be referenced across an inter-Region VPC peering connection.
  scope: per inter-Region peering connection.
  link: [Security groups cannot be referenced](../facts/vpc-peering.md#vpc-peering-faq-inter-region-no-sg-reference)
  say: no, not across Regions
vpc-peering-faq-intra-region-private
  claim: The FAQ answers 'No' to whether VPC peering traffic within a Region is encrypted, and says that traffic between instances in peered VPCs remains private and isolated, like traffic between two instances in the same VPC.
  scope: per same-Region peering connection.
  link: [remains private and isolated](../facts/vpc-peering.md#vpc-peering-faq-intra-region-private)
  say: not encrypted by peering, but private and isolated
vpc-peering-faq-no-creation-charge
  claim: There is no charge for creating a VPC peering connection, but data transfer across the peering connection is charged.
  scope: per peering connection.
  link: [no charge for creating VPC peering connections](../facts/vpc-peering.md#vpc-peering-faq-no-creation-charge)
  link: [data transfer across peering connections is charged](../facts/vpc-peering.md#vpc-peering-faq-no-creation-charge)
  say: creating a peering connection is free | you pay for data transfer across it
vpc-peering-faq-no-internet-gateway
  claim: VPC peering connections do not require an internet gateway.
  scope: per peering connection.
  link: [do not require an Internet Gateway](../facts/vpc-peering.md#vpc-peering-faq-no-internet-gateway)
  say: no internet gateway needed for peering
vpc-peering-faq-no-single-point-of-failure
  claim: A VPC peering connection uses the existing VPC infrastructure; it is neither a gateway nor a VPN connection, does not depend on separate physical hardware, and has no single point of failure or bandwidth bottleneck.
  scope: per peering connection.
  link: [neither a gateway nor a VPN connection](../facts/vpc-peering.md#vpc-peering-faq-no-single-point-of-failure)
  link: [no single point of failure for communication](../facts/vpc-peering.md#vpc-peering-faq-no-single-point-of-failure)
  say: no single point of failure, no bottleneck
vpc-peering-faq-not-transitive
  claim: Peering A to B and B to C does not peer A with C: transitive peering relationships are not supported.
  scope: VPC peering.
  link: [Transitive peering relationships are not supported](../facts/vpc-peering.md#vpc-peering-faq-not-transitive)
  say: peering is not transitive
vpc-peering-guide-existing-infrastructure-no-spof
  claim: AWS uses the existing infrastructure of a VPC to create a peering connection; it is neither a gateway nor a VPN connection and uses no separate physical hardware, so there is no single point of failure for communication or a bandwidth bottleneck.
  scope: VPC peering connection.
  link: [neither a gateway nor a VPN connection](../facts/vpc-peering.md#vpc-peering-guide-existing-infrastructure-no-spof)
  link: [no single point of failure for communication](../facts/vpc-peering.md#vpc-peering-guide-existing-infrastructure-no-spof)
vpc-peering-guide-inter-region-cost-effective-replication
  claim: Inter-Region VPC peering provides a simple and cost-effective way to share resources between Regions or replicate data for geographic redundancy.
  scope: inter-Region VPC peering connection.
  link: [simple and cost-effective way to share resources](../facts/vpc-peering.md#vpc-peering-guide-inter-region-cost-effective-replication)
vpc-peering-guide-inter-region-encrypted-backbone
  claim: All inter-Region VPC peering traffic is encrypted before leaving AWS facilities, always stays on the global AWS backbone and never traverses the public internet, which reduces threats such as common exploits and DDoS attacks.
  scope: inter-Region VPC peering connection.
  link: [inter-Region traffic is encrypted before leaving AWS](../facts/vpc-peering.md#vpc-peering-guide-inter-region-encrypted-backbone)
  link: [never traverses the public internet](../facts/vpc-peering.md#vpc-peering-guide-inter-region-encrypted-backbone)
vpc-peering-guide-not-through-internet-vpn-dx
  claim: VPC peering creates a direct network route between the two VPCs using private IPv4 or IPv6 addresses, and traffic between the connected VPCs does not traverse the internet, a VPN connection or an AWS Direct Connect connection.
  scope: VPC peering connection.
  link: [does not traverse the internet, a VPN connection](../facts/vpc-peering.md#vpc-peering-guide-not-through-internet-vpn-dx)
vpc-peering-guide-pricing-no-creation-charge-free-in-az
  claim: There is no charge to create a VPC peering connection; data transfer over it that stays within an Availability Zone is free even between accounts, and charges apply for data transfer that crosses Availability Zones and Regions.
  scope: VPC peering connection pricing.
  link: [no charge to create a VPC peering connection](../facts/vpc-peering.md#vpc-peering-guide-pricing-no-creation-charge-free-in-az)
  link: [even if it's between different accounts](../facts/vpc-peering.md#vpc-peering-guide-pricing-no-creation-charge-free-in-az)
vpc-peering-inter-region-request-region
  claim: For an inter-Region peering connection the request must be made from the Region of the requester VPC and accepted from the Region of the accepter VPC.
  scope: inter-Region VPC peering connection.
  link: [made from the Region of the requester VPC](../facts/vpc-peering.md#vpc-peering-inter-region-request-region)
  link: [accepted from the Region of the accepter VPC](../facts/vpc-peering.md#vpc-peering-inter-region-request-region)
vpc-peering-ipv6-requirements
  claim: Resources on both sides of a VPC peering connection can communicate over IPv6 if each VPC has an IPv6 CIDR block, the instances are enabled for IPv6, and IPv6 traffic for the peer VPC is routed to the peering connection.
  scope: VPC peering connection.
  link: [communicate over IPv6](../facts/vpc-peering.md#vpc-peering-ipv6-requirements)
  link: [associate an IPv6 CIDR block with each VPC](../facts/vpc-peering.md#vpc-peering-ipv6-requirements)
vpc-peering-mtu-inter-region-8500
  claim: The MTU for inter-Region VPC peering connections is 8500 bytes.
  scope: inter-Region VPC peering connection; maximum; not adjustable.
  link: [8500 bytes](../facts/vpc-peering.md#vpc-peering-mtu-inter-region-8500)
vpc-peering-mtu-same-region-9001
  claim: The MTU for jumbo frames between VPC peering connections within the same Region is 9001 bytes.
  scope: VPC peering connection within the same Region; maximum; not adjustable.
  link: [9001 bytes](../facts/vpc-peering.md#vpc-peering-mtu-same-region-9001)
vpc-peering-no-overlap-even-if-unused-cidr
  claim: If a VPC has multiple IPv4 CIDR blocks, you cannot create a peering connection when any of the CIDR blocks overlap, even if you intend to use only the non-overlapping CIDR blocks or only IPv6 CIDR blocks.
  scope: VPC peering connection.
  link: [use only the non-overlapping CIDR blocks](../facts/vpc-peering.md#vpc-peering-no-overlap-even-if-unused-cidr)
  link: [if any of the CIDR blocks overlap](../facts/vpc-peering.md#vpc-peering-no-overlap-even-if-unused-cidr)
vpc-peering-no-overlap-ipv4-ipv6
  claim: You cannot create a VPC peering connection between VPCs that have matching or overlapping IPv4 or IPv6 CIDR blocks.
  scope: VPC peering connection.
  link: [matching or overlapping IPv4 or IPv6 CIDR blocks](../facts/vpc-peering.md#vpc-peering-no-overlap-ipv4-ipv6)
  link: [cannot create a VPC peering connection](../facts/vpc-peering.md#vpc-peering-no-overlap-ipv4-ipv6)
vpc-peering-no-query-peer-dns-server
  claim: You cannot connect to or query the Amazon DNS server in a peer VPC.
  scope: VPC peering connection.
  link: [query the Amazon DNS server](../facts/vpc-peering.md#vpc-peering-no-query-peer-dns-server)
  link: [in a peer VPC](../facts/vpc-peering.md#vpc-peering-no-query-peer-dns-server)
vpc-peering-no-reverse-path-forwarding
  claim: Unicast reverse path forwarding in VPC peering connections is not supported; separately, if a VPC is peered with multiple VPCs that have overlapping or matching IPv4 CIDR blocks, configure its route tables to avoid sending response traffic to the incorrect VPC.
  scope: VPC peering connection.
  link: [Unicast reverse path forwarding](../facts/vpc-peering.md#vpc-peering-no-reverse-path-forwarding)
vpc-peering-no-transitive-example
  claim: VPC peering does not support transitive peering: if VPC A peers with B and with C, traffic cannot go from B to C through A, and B and C need their own peering connection.
  scope: VPC peering connection.
  link: [does not support transitive peering relationships](../facts/vpc-peering.md#vpc-peering-no-transitive-example)
  link: [route traffic from VPC B to VPC C](../facts/vpc-peering.md#vpc-peering-no-transitive-example)
vpc-peering-one-connection-between-two-vpcs
  claim: You cannot have more than one VPC peering connection between the same two VPCs at the same time.
  scope: two VPCs; maximum.
  link: [more than one VPC peering connection](../facts/vpc-peering.md#vpc-peering-one-connection-between-two-vpcs)
  link: [at the same time](../facts/vpc-peering.md#vpc-peering-one-connection-between-two-vpcs)
vpc-peering-one-to-one-relationship
  claim: A VPC peering connection is a one to one relationship between two VPCs, and you have no peering relationship with VPCs that your VPC is not directly peered with.
  scope: VPC peering connection.
  link: [a one to one relationship between two VPCs](../facts/vpc-peering.md#vpc-peering-one-to-one-relationship)
  link: [not directly peered with](../facts/vpc-peering.md#vpc-peering-one-to-one-relationship)
vpc-peering-overlap-status-failed
  claim: If the IPv4 CIDR blocks of the VPCs overlap, the status of the peering connection immediately goes to failed, even when the VPCs have unique IPv6 CIDR blocks.
  scope: VPC peering connection.
  link: [immediately goes to](../facts/vpc-peering.md#vpc-peering-overlap-status-failed)
  link: [applies even if the VPCs have unique IPv6 CIDR blocks](../facts/vpc-peering.md#vpc-peering-overlap-status-failed)
vpc-peering-pending-acceptance-expires
  claim: In the pending-acceptance state the requester can delete the request and the accepter can accept or reject it; if no one acts, the request expires after 7 days.
  scope: VPC peering request in the pending-acceptance state; fixed; state is pending-acceptance.
  link: [it expires after 7 days](../facts/vpc-peering.md#vpc-peering-pending-acceptance-expires)
  link: [can accept or reject the request](../facts/vpc-peering.md#vpc-peering-pending-acceptance-expires)
vpc-peering-quota-active-connections-per-vpc
  claim: A VPC has a default quota of 50 active VPC peering connections, and the quota is adjustable up to 125.
  scope: per VPC; default; adjustable; adjustable up to 125 through Service Quotas.
  link: [50](../facts/vpc-peering.md#vpc-peering-quota-active-connections-per-vpc)
  link: [up to 125](../facts/vpc-peering.md#vpc-peering-quota-active-connections-per-vpc)
  say: fifty active peering connections per VPC | adjustable up to one hundred twenty-five
vpc-peering-quota-outstanding-requests
  claim: A default of 25 outstanding VPC peering connection requests is allowed, and the quota is adjustable.
  scope: outstanding VPC peering connection requests; default; adjustable.
  link: [25](../facts/vpc-peering.md#vpc-peering-quota-outstanding-requests)
  say: twenty-five outstanding requests
vpc-peering-quota-request-expiry
  claim: An unaccepted VPC peering connection request expires after 1 week (168 hours), and this expiry time is not adjustable.
  scope: expiry time of an unaccepted VPC peering connection request; fixed; not adjustable.
  link: [1 week (168 hours)](../facts/vpc-peering.md#vpc-peering-quota-request-expiry)
  say: one week, which is a hundred and sixty-eight hours
vpc-peering-rejected-request-visibility
  claim: A rejected VPC peering connection remains visible to the requester VPC owner for 2 days and to the accepter VPC owner for 2 hours; if the request was created within the same AWS account, it remains visible for 2 hours.
  scope: per rejected VPC peering connection request; fixed; not adjustable.
  link: [visible to the owner of the requester VPC for 2 days](../facts/vpc-peering.md#vpc-peering-rejected-request-visibility)
  link: [visible to the owner of the accepter VPC for 2 hours](../facts/vpc-peering.md#vpc-peering-rejected-request-visibility)
  say: two days for the requester | two hours for the accepter
vpc-peering-route-pending-blackhole
  claim: You can add a route for a peering connection in the pending-acceptance state, but the route is a blackhole and has no effect until the connection is active.
  scope: VPC route table.
  link: [the route has a state of `blackhole`](../facts/vpc-peering.md#vpc-peering-route-pending-blackhole)
  link: [has no effect until](../facts/vpc-peering.md#vpc-peering-route-pending-blackhole)
vpc-peering-route-target-and-destination
  claim: To enable private IPv4 traffic between instances in peered VPCs, you add a route to the route tables of the subnets of both instances; the destination is the peer VPC CIDR block (or a portion of it) and the target is the peering connection ID.
  scope: VPC route tables of both peered VPCs.
  link: [add a route to the route tables](../facts/vpc-peering.md#vpc-peering-route-target-and-destination)
  link: [ID of the VPC peering connection](../facts/vpc-peering.md#vpc-peering-route-target-and-destination)
vpc-peering-scenario-active-directory-central-vpc
  claim: In a peering design with a central Active Directory VPC, specific instances in peer VPCs send requests to the directory servers and need full access to the central VPC, while the central VPC only needs to route response traffic to those instances.
  scope: VPC peering scenarios.
  link: [only needs to route response traffic](../facts/vpc-peering.md#vpc-peering-scenario-active-directory-central-vpc)
vpc-peering-scenario-central-vpc-spokes-isolated
  claim: In a central VPC scenario, other VPCs peer to the central VPC and do not send traffic to each other; a customer-facing central VPC lets each customer peer with it without routing to other customers' VPCs or seeing their routes.
  scope: VPC peering scenarios.
  link: [do not want the other VPCs](../facts/vpc-peering.md#vpc-peering-scenario-central-vpc-spokes-isolated)
  link: [nor are they aware of the other customers'](../facts/vpc-peering.md#vpc-peering-scenario-central-vpc-spokes-isolated)
vpc-peering-sg-reference-needs-active
  claim: To reference a security group in a peer VPC, the VPC peering connection must be in the active state.
  scope: VPC peering connection.
  link: [must be in the `active` state](../facts/vpc-peering.md#vpc-peering-sg-reference-needs-active)
vpc-peering-sg-reference-no-cross-region
  claim: You cannot reference the security group of a peer VPC that is in a different Region; use the CIDR block of the peer VPC instead.
  scope: inter-Region VPC peering connection.
  link: [can't reference the security group](../facts/vpc-peering.md#vpc-peering-sg-reference-no-cross-region)
  link: [use the CIDR block of the peer VPC](../facts/vpc-peering.md#vpc-peering-sg-reference-no-cross-region)
vpc-peering-sg-reference-other-account
  claim: To reference a security group in another AWS account in the same Region, you include the account number with the security group ID.
  scope: same-Region VPC peering connection.
  link: [include the account number](../facts/vpc-peering.md#vpc-peering-sg-reference-other-account)
  link: [another AWS account but the same Region](../facts/vpc-peering.md#vpc-peering-sg-reference-other-account)
vpc-peering-sg-reference-same-region
  claim: You can reference a security group of a peer VPC in the inbound or outbound rules of your security group, which allows traffic to and from instances associated with the referenced group; the peering connection must be in the active state, and you can't reference the security group of a peer VPC in a different Region (use the CIDR block of the peer VPC instead).
  scope: VPC peering connection in the same Region; the peering connection is active; the peer VPC is in the same Region.
  link: [reference security groups for peered VPCs](../facts/vpc-peering.md#vpc-peering-sg-reference-same-region)
  link: [security group in the peered VPC](../facts/vpc-peering.md#vpc-peering-sg-reference-same-region)
vpc-peering-shared-vpc-owner-only
  claim: In a shared VPC, only the VPC owner can describe, create, accept, reject, modify or delete peering connections; participants cannot work with peering connections.
  scope: shared VPCs and subnets.
  link: [Only VPC owners can work with](../facts/vpc-peering.md#vpc-peering-shared-vpc-owner-only)
  link: [Participants cannot work with peering connections](../facts/vpc-peering.md#vpc-peering-shared-vpc-owner-only)
vpc-peering-sharing-wp-benefits-no-transfer-charge-same-az
  claim: A benefit of VPC sharing is lower cost, because there are no data transfer charges between instances that belong to different accounts within the same Availability Zone.
  scope: VPC sharing.
  link: [no data transfer charges between instances belonging](../facts/vpc-peering.md#vpc-peering-sharing-wp-benefits-no-transfer-charge-same-az)
vpc-peering-sharing-wp-owner-shares-subnets-participants-manage-own
  claim: With VPC sharing, the VPC owner shares one or more subnets with other accounts (participants); participants can view, create, modify and delete their own application resources in the shared subnets but not those of other participants or the owner.
  scope: VPC sharing.
  link: [shares one or more subnets with other accounts](../facts/vpc-peering.md#vpc-peering-sharing-wp-owner-shares-subnets-participants-manage-own)
  link: [Participants cannot view, modify, or delete resources](../facts/vpc-peering.md#vpc-peering-sharing-wp-owner-shares-subnets-participants-manage-own)
vpc-peering-sharing-wp-reduces-vpc-count-instead-of-connecting
  claim: Sharing subnets uses the implicit routing within a VPC for applications that need a high degree of interconnectivity and share a trust boundary, which reduces the number of VPCs you create and manage while separate accounts keep billing and access control.
  scope: VPC sharing.
  link: [implicit routing within a VPC](../facts/vpc-peering.md#vpc-peering-sharing-wp-reduces-vpc-count-instead-of-connecting)
  link: [within the same trust boundaries](../facts/vpc-peering.md#vpc-peering-sharing-wp-reduces-vpc-count-instead-of-connecting)
vpc-peering-sharing-wp-use-when-isolation-managed-by-accounts
  claim: Sharing VPCs is useful when network isolation between teams does not need to be strictly managed by the VPC owner but the account-level users and permissions must be.
  scope: VPC sharing.
  link: [network isolation between teams does not need](../facts/vpc-peering.md#vpc-peering-sharing-wp-use-when-isolation-managed-by-accounts)
vpc-peering-specific-routes-longest-prefix
  claim: VPC route tables use longest prefix match to select the most specific route across the intended VPC peering connection, and all other traffic goes to the next matching route.
  scope: VPC route table with peering connections.
  link: [longest prefix match](../facts/vpc-peering.md#vpc-peering-specific-routes-longest-prefix)
  link: [select the most specific route](../facts/vpc-peering.md#vpc-peering-specific-routes-longest-prefix)
vpc-peering-spokes-may-overlap-each-other
  claim: A central VPC can be peered with at least two VPCs that have overlapping CIDR blocks, as in the guide's partial-access configuration examples.
  scope: VPC peering connections with a central VPC.
  link: [two VPCs that have overlapping CIDR blocks](../facts/vpc-peering.md#vpc-peering-spokes-may-overlap-each-other)
  link: [a central VPC is peered](../facts/vpc-peering.md#vpc-peering-spokes-may-overlap-each-other)
vpc-peering-step-accept
  claim: The owner of the accepter VPC must accept the request to activate the VPC peering connection.
  scope: VPC peering connection.
  link: [accepts the VPC peering connection request to activate](../facts/vpc-peering.md#vpc-peering-step-accept)
  link: [owner of the accepter VPC accepts](../facts/vpc-peering.md#vpc-peering-step-accept)
vpc-peering-step-request
  claim: The owner of the requester VPC sends a request to the owner of the accepter VPC to create the peering connection; the accepter VPC can be in another account and its CIDR block cannot overlap the requester's.
  scope: VPC peering connection request.
  link: [sends a request to the owner](../facts/vpc-peering.md#vpc-peering-step-request)
  link: [cannot have a CIDR block that overlaps](../facts/vpc-peering.md#vpc-peering-step-request)
vpc-peering-step-routes-manual
  claim: To enable the flow of traffic between peered VPCs using private IP addresses, the owner of each VPC in the peering connection must manually add a route to one or more of their VPC route tables that points to the IP address range of the peer VPC.
  scope: each VPC in a peering connection.
  link: [must manually add a route](../facts/vpc-peering.md#vpc-peering-step-routes-manual)
  link: [IP address range of the other VPC](../facts/vpc-peering.md#vpc-peering-step-routes-manual)
vpc-peering-step-security-groups
  claim: If required, you update the security group rules of your EC2 instance so traffic to and from the peer VPC is not restricted; when both VPCs are in the same Region, a rule can reference a security group of the peer VPC.
  scope: VPC peering connection.
  link: [update the security group rules](../facts/vpc-peering.md#vpc-peering-step-security-groups)
  link: [If both VPCs are in the same Region](../facts/vpc-peering.md#vpc-peering-step-security-groups)
vpc-peering-tags-local-only
  claim: Tags that you create for a VPC peering connection apply only in the account or Region in which you create them.
  scope: VPC peering connection tags.
  link: [only applied in the account or Region](../facts/vpc-peering.md#vpc-peering-tags-local-only)
vpc-peering-troubleshoot-nacls-and-reachability
  claim: When peered resources cannot connect, check that the network ACLs of the subnets allow the necessary traffic from the peer VPC, and use Reachability Analyzer to find whether a route table, security group or network ACL blocks the traffic.
  scope: VPC peering troubleshooting.
  link: [Reachability Analyzer](../facts/vpc-peering.md#vpc-peering-troubleshoot-nacls-and-reachability)
  link: [causing the connectivity problem between the two VPCs](../facts/vpc-peering.md#vpc-peering-troubleshoot-nacls-and-reachability)
vpc-peering-troubleshoot-routes
  claim: When resources in peered VPCs cannot connect, verify for each resource that its subnet route table has a route sending traffic for the peer VPC to the peering connection.
  scope: VPC peering troubleshooting.
  link: [route table for its subnet contains a route](../facts/vpc-peering.md#vpc-peering-troubleshoot-routes)
  link: [peer VPC to the VPC peering connection](../facts/vpc-peering.md#vpc-peering-troubleshoot-routes)
vpc-peering-troubleshoot-security-groups
  claim: When peered resources cannot connect, verify that the security groups of the involved EC2 instances allow inbound and outbound traffic from the peer VPC.
  scope: VPC peering troubleshooting.
  link: [security groups for those instances allow inbound](../facts/vpc-peering.md#vpc-peering-troubleshoot-security-groups)
vpc-peering-wa-rel02-bp05-no-overlap-when-connected
  claim: The IP address ranges of VPCs must not overlap when the VPCs are peered, connected through a transit gateway, or connected over VPN.
  scope: REL02-BP05.
  link: [must not overlap when peered](../facts/vpc-peering.md#vpc-peering-wa-rel02-bp05-no-overlap-when-connected)
vpc-peering-wa-rel02-bp05-use-ipam
  claim: Use an IP address management system such as Amazon VPC IP Address Manager to monitor and manage CIDR use, so VPC ranges do not overlap.
  scope: REL02-BP05.
  link: [Amazon VPC IP Address Manager](../facts/vpc-peering.md#vpc-peering-wa-rel02-bp05-use-ipam)
vpc-peering-whitepaper-max-125-active-connections
  claim: The multi-VPC whitepaper states a maximum limit of 125 active peering connections per VPC.
  scope: active peering connections per VPC (as the multi-VPC whitepaper states it); maximum; not adjustable.
  link: [125 active peering connections per VPC](../facts/vpc-peering.md#vpc-peering-whitepaper-max-125-active-connections)
  say: one hundred twenty-five active peering connections per VPC
vpc-peering-wp-best-for-few-controlled-vpcs
  claim: The whitepaper says VPC peering is best used when resources in one VPC must communicate with resources in another, the environment of both VPCs is controlled and secured, and fewer than 10 VPCs need to be connected so each connection can be managed individually.
  scope: VPC peering design.
  link: [the number of VPCs to be connected is less than 10](../facts/vpc-peering.md#vpc-peering-wp-best-for-few-controlled-vpcs)
  link: [environment of both VPCs is controlled and secured](../facts/vpc-peering.md#vpc-peering-wp-best-for-few-controlled-vpcs)
vpc-peering-wp-data-transfer-free-in-az
  claim: Data transfer over a VPC peering connection that stays within an Availability Zone is free; crossing Availability Zones is charged at the standard in-Region data transfer rates, and peering across Regions is charged the standard inter-Region data transfer rates.
  scope: VPC peering data transfer.
  link: [stays within an Availability Zone is free](../facts/vpc-peering.md#vpc-peering-wp-data-transfer-free-in-az)
  link: [standard in-region data transfer rates](../facts/vpc-peering.md#vpc-peering-wp-data-transfer-free-in-az)
  link: [standard inter-Region data transfer charges will apply](../facts/vpc-peering.md#vpc-peering-wp-data-transfer-free-in-az)
vpc-peering-wp-full-bidirectional-point-to-point
  claim: A VPC peering connection enables full bidirectional connectivity between the two VPCs; it is point-to-point and does not support transitive routing.
  scope: VPC peering connection.
  link: [full bidirectional connectivity between the VPCs](../facts/vpc-peering.md#vpc-peering-wp-full-bidirectional-point-to-point)
  link: [point-to-point connectivity](../facts/vpc-peering.md#vpc-peering-wp-full-bidirectional-point-to-point)
vpc-peering-wp-full-mesh-4950-connections
  claim: A full mesh of 100 VPCs with VPC peering takes 4,950 peering connections, using the formula n(n-1)/2 where n is the number of VPCs.
  scope: VPC peering full mesh.
  link: [4,950 peering connections](../facts/vpc-peering.md#vpc-peering-wp-full-mesh-4950-connections)
  link: [n(n-1)/2](../facts/vpc-peering.md#vpc-peering-wp-full-mesh-4950-connections)
vpc-peering-wp-lowest-cost-highest-performance
  claim: VPC peering offers the lowest overall cost and highest aggregate performance compared with the other options for inter-VPC connectivity.
  scope: VPC peering design.
  link: [lowest overall cost and highest aggregate performance](../facts/vpc-peering.md#vpc-peering-wp-lowest-cost-highest-performance)
vpc-peering-wp-many-to-many-vs-hub-and-spoke
  claim: In the many-to-many pattern traffic between each pair of VPCs is managed individually; in the hub-and-spoke pattern all inter-VPC traffic flows through a central resource that routes it by established rules.
  scope: VPC-to-VPC connectivity patterns.
  link: [many-to-many approach](../facts/vpc-peering.md#vpc-peering-wp-many-to-many-vs-hub-and-spoke)
  link: [all inter-VPC traffic flows through a central resource](../facts/vpc-peering.md#vpc-peering-wp-many-to-many-vs-hub-and-spoke)
vpc-peering-wp-onprem-link-to-each-vpc
  claim: With VPC peering, on-premises connectivity (VPN or Direct Connect) must be made to each VPC, because resources in a VPC cannot reach on-premises using the hybrid connectivity of a peered VPC.
  scope: VPC peering.
  link: [on-premises connectivity (VPN and/or Direct Connect)](../facts/vpc-peering.md#vpc-peering-wp-onprem-link-to-each-vpc)
vpc-peering-wp-use-non-overlapping-cidr-per-vpc
  claim: AWS advises giving each VPC a single, contiguous, non-overlapping CIDR block, because VPC-to-VPC connectivity works best with non-overlapping IP ranges for the VPCs being connected.
  scope: VPC-to-VPC connectivity.
  link: [non-overlapping IP ranges for each VPC being connected](../facts/vpc-peering.md#vpc-peering-wp-use-non-overlapping-cidr-per-vpc)
  link: [single, contiguous, non-overlapping CIDR block](../facts/vpc-peering.md#vpc-peering-wp-use-non-overlapping-cidr-per-vpc)
vpc-peering-wp-use-tgw-or-cloud-wan-as-hub
  claim: To let all VPCs talk to each other with VPC peering you need 1:1 peering connections between each pair; alternatively you can use AWS Transit Gateway or AWS Cloud WAN as a network transit hub.
  scope: VPC peering design.
  link: [create 1:1 VPC peering connections between each of them](../facts/vpc-peering.md#vpc-peering-wp-use-tgw-or-cloud-wan-as-hub)
  link: [AWS Transit Gateway or AWS Cloud WAN](../facts/vpc-peering.md#vpc-peering-wp-use-tgw-or-cloud-wan-as-hub)
