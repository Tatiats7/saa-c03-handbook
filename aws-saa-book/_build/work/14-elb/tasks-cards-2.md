facts card: 11 facts
elb-alb-503-no-registered-targets
  claim: Under the troubleshooting heading for the ALB 'Service unavailable' error, a listed possible cause is that the target groups have no registered targets, or all registered targets are in the unused state.
  scope: Application Load Balancer HTTP 503.
  link: [have no registered targets](../facts/elb.md#elb-alb-503-no-registered-targets)
  link: [in an `unused` state](../facts/elb.md#elb-alb-503-no-registered-targets)
elb-alb-faq-ip-target-ranges
  claim: IP targets of a load balancer can use any IP address from the load balancer's VPC CIDR inside its VPC, and any address from the RFC 1918 ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) or the RFC 6598 range (100.64.0.0/10) for targets outside that VPC, such as a peered VPC or on-premises locations reached over AWS Direct Connect or VPN.
  scope: Application Load Balancer IP targets.
  link: [IP address from the load balancer’s VPC CIDR](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [RFC 1918 ranges](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [RFC 6598 range (100.64.0.0/10)](../facts/elb.md#elb-alb-faq-ip-target-ranges)
  link: [reachable over AWS Direct Connect or VPN connection](../facts/elb.md#elb-alb-faq-ip-target-ranges)
elb-ip-targets-no-public-addresses
  claim: With the ip target type you cannot specify publicly routable IP addresses; the addresses must come from the subnets of the target group VPC or from a listed set of private CIDR blocks.
  scope: ip target type (ALB and NLB).
  link: [You can't specify publicly routable IP addresses](../facts/elb.md#elb-ip-targets-no-public-addresses)
elb-alb-target-state-initial
  claim: A target in the initial state is being registered, or the load balancer is running its initial health checks on it.
  scope: Application Load Balancer registered target.
  link: [`initial`](../facts/elb.md#elb-alb-target-state-initial)
  link: [performing the initial health checks on the target](../facts/elb.md#elb-alb-target-state-initial)
elb-alb-target-state-unhealthy
  claim: A target in the unhealthy state did not respond to a health check or failed the health check.
  scope: Application Load Balancer registered target.
  link: [`unhealthy`](../facts/elb.md#elb-alb-target-state-unhealthy)
  link: [did not respond to a health check](../facts/elb.md#elb-alb-target-state-unhealthy)
elb-alb-fail-open-all-unhealthy
  claim: If an ALB target group contains only unhealthy targets, the load balancer routes requests to all of them regardless of health: when all targets fail health checks at once in all enabled Availability Zones, the load balancer fails open.
  scope: Application Load Balancer target group; all registered targets unhealthy.
  link: [routes requests to all those targets](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
  link: [the load balancer fails open](../facts/elb.md#elb-alb-fail-open-all-unhealthy)
elb-alb-target-connection-timeout-10-seconds
  claim: An Application Load Balancer has a 10-second connection timeout for establishing a connection to a target.
  scope: per connection to a target; fixed; not adjustable.
  link: [connection timeout expired (10 seconds)](../facts/elb.md#elb-alb-target-connection-timeout-10-seconds)
  say: ten-second connection timeout
elb-alb-target-state-draining
  claim: A target in the draining state is deregistering and connection draining is in progress.
  scope: Application Load Balancer registered target.
  link: [`draining`](../facts/elb.md#elb-alb-target-state-draining)
  link: [connection draining is in process](../facts/elb.md#elb-alb-target-state-draining)
vpc-public-ipv4-charge-2024
  claim: Since February 1, 2024 AWS charges $0.005 per IP per hour for public IPv4 addresses, whether in use or idle, including the public IPv4 addresses of running instances and Elastic IP addresses; before that date an in-use public IPv4 address had no charge. Addresses in an Amazon-provided contiguous IPv4 block have their own hourly rate.
  scope: per public IPv4 address, per hour; the Amazon-provided contiguous IPv4 block has a separate hourly rate.
  link: [$0.005 per IP per hour](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [February 1, 2024](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [AWS charges for all public IPv4 addresses](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  link: [No charge](../facts/vpc.md#vpc-public-ipv4-charge-2024)
  say: half a cent per address per hour | February first, twenty twenty-four | every public IPv4 address is billed, attached or not | no charge
  changed: 2024-02-01: was No charge
elb-free-tier-750-hours-15-lcus
  claim: The ELB pricing page says new AWS customers receive 750 hours per month shared between Classic and Application Load Balancers, 15 GB of data processing for Classic Load Balancers, and 15 LCUs for Application Load Balancers.
  scope: per new AWS account, per month; pricing-page wording; the FAQ (elb-free-tier-faq-includes-nlb) also names Network Load Balancers; see elb-faq-free-tier-credits-from-2025-07-15 for the Free Tier credits of new customers from July 15, 2025.
  link: [750 hours per month](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  link: [15 LCUs](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  link: [15 GB](../facts/elb.md#elb-free-tier-750-hours-15-lcus)
  say: seven hundred fifty hours per month | fifteen LCUs | fifteen gigabytes
elb-capacity-units-billed-per-minute
  claim: Besides the hourly charge, Application, Network and Gateway Load Balancers are charged for the capacity units (LCU, NLCU or GLCU) used per minute.
  scope: per load balancer.
  link: [used per minute](../facts/elb.md#elb-capacity-units-billed-per-minute)
  link: [Load Balancer Capacity Units (LCU)](../facts/elb.md#elb-capacity-units-billed-per-minute)
  say: used per minute | Load Balancer Capacity Units
