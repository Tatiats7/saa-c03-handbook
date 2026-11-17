facts card: 11 facts
elb-alb-security-policy-protocols-ciphers
  claim: A security policy is a combination of protocols and ciphers that Elastic Load Balancing uses to negotiate SSL connections between a client and the load balancer.
  scope: Application Load Balancer secure listener.
  link: [a combination of protocols and ciphers](../facts/elb.md#elb-alb-security-policy-protocols-ciphers)
  link: [negotiate SSL connections](../facts/elb.md#elb-alb-security-policy-protocols-ciphers)
elb-alb-https-default-security-policy
  claim: An HTTPS listener requires a security policy; if you do not specify one, the default is ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 in the console and ELBSecurityPolicy-2016-08 with other methods such as the AWS CLI or CloudFormation.
  scope: Application Load Balancer HTTPS listener; default; adjustable; no security policy specified.
  link: [An HTTPS listener requires a security policy](../facts/elb.md#elb-alb-https-default-security-policy)
  link: [ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09](../facts/elb.md#elb-alb-https-default-security-policy)
  link: [ELBSecurityPolicy-2016-08](../facts/elb.md#elb-alb-https-default-security-policy)
elb-tls-recommended-post-quantum-policy
  claim: For Application Load Balancer HTTPS listeners, AWS recommends the post-quantum TLS security policy ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09 or ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09.
  scope: Application Load Balancer HTTPS listeners.
  link: [ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09](../facts/elb.md#elb-tls-recommended-post-quantum-policy)
  link: [ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09](../facts/elb.md#elb-tls-recommended-post-quantum-policy)
elb-alb-quota-load-balancers-per-region
  claim: The default quota is 50 Application Load Balancers per Region; the quota is adjustable.
  scope: per Region, per account; default; adjustable.
  link: [50 Application Load Balancers](../facts/elb.md#elb-alb-quota-load-balancers-per-region)
  say: fifty Application Load Balancers
elb-alb-subnets-two-azs-different
  claim: For an Application Load Balancer you must select subnets in at least two Availability Zones, and each subnet must be from a different Availability Zone.
  scope: Application Load Balancer subnets.
  link: [at least two Availability Zone subnets](../facts/elb.md#elb-alb-subnets-two-azs-different)
  link: [from a different Availability Zone](../facts/elb.md#elb-alb-subnets-two-azs-different)
elb-alb-fixed-response-action
  claim: A fixed-response action drops the client request and returns a custom HTTP response with a 2XX, 4XX or 5XX code and an optional message.
  scope: Application Load Balancer fixed-response action.
  link: [returns a custom HTTP response](../facts/elb.md#elb-alb-fixed-response-action)
  link: [2XX, 4XX, or 5XX response code](../facts/elb.md#elb-alb-fixed-response-action)
elb-alb-default-rule-last-no-conditions
  claim: Every ALB listener has a default rule that cannot be deleted, has no conditions, and is performed last, when no other rule's conditions are met.
  scope: Application Load Balancer listener.
  link: [The default rule can't be deleted](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
  link: [is always performed last](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
  link: [The default rule can't have conditions](../facts/elb.md#elb-alb-default-rule-last-no-conditions)
elb-alb-rules-lowest-priority-first
  claim: ALB listener rules are evaluated in priority order from the lowest value to the highest, and the default rule is evaluated last.
  scope: Application Load Balancer listener rules.
  link: [from the lowest value to the highest value](../facts/elb.md#elb-alb-rules-lowest-priority-first)
  link: [The default rule is evaluated last](../facts/elb.md#elb-alb-rules-lowest-priority-first)
elb-alb-condition-types
  claim: ALB listener rules can route on host header, HTTP header, HTTP request method, path pattern, query string and source IP address conditions.
  scope: Application Load Balancer listener rules.
  link: [host-header](../facts/elb.md#elb-alb-condition-types)
  link: [path-pattern](../facts/elb.md#elb-alb-condition-types)
  link: [source-ip](../facts/elb.md#elb-alb-condition-types)
  link: [query-string](../facts/elb.md#elb-alb-condition-types)
elb-partial-hour-billed-as-full-hour
  claim: Application, Network and Gateway Load Balancers are charged for each hour or partial hour that they run, and each partial hour is billed as a full hour.
  scope: per load balancer.
  link: [billed as a full hour](../facts/elb.md#elb-partial-hour-billed-as-full-hour)
  link: [each hour or partial hour](../facts/elb.md#elb-partial-hour-billed-as-full-hour)
  say: billed as a full hour | each hour or partial hour
elb-pricing-public-ipv4-and-data-transfer-extra
  claim: On top of the load balancer charges, you pay standard AWS data transfer charges and standard public IPv4 address charges for all addresses your load balancers consume.
  scope: Elastic Load Balancing.
  link: [standard AWS data transfer charges](../facts/elb.md#elb-pricing-public-ipv4-and-data-transfer-extra)
  link: [standard public IPv4 address charges](../facts/elb.md#elb-pricing-public-ipv4-and-data-transfer-extra)
