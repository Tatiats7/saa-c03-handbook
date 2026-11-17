facts card: 785 facts
route53-a-record-ipv4
  claim: An A record routes traffic to a resource, such as a web server, by using an IPv4 address in dotted decimal notation.
  scope: A record.
  link: [A record to route traffic to a resource](../facts/route53.md#route53-a-record-ipv4)
  link: [using an IPv4 address](../facts/route53.md#route53-a-record-ipv4)
route53-aaaa-record-ipv6
  claim: An AAAA record routes traffic to a resource, such as a web server, by using an IPv6 address in colon-separated hexadecimal format.
  scope: AAAA record.
  link: [AAAA record to route traffic to a resource](../facts/route53.md#route53-aaaa-record-ipv6)
  link: [using an IPv6 address](../facts/route53.md#route53-aaaa-record-ipv6)
route53-accelerated-recovery-60-minute-rto
  claim: Since 2025-11-26 you can turn on accelerated recovery for a Route 53 public hosted zone. It targets a 60-minute Recovery Time Objective (RTO) for making DNS changes again if the US East (N. Virginia) Region becomes unavailable, using a copy of the zone kept in the US West (Oregon) Region, and you must turn it on before any issues with that Region occur. Before it, customers could not modify or recreate DNS records while AWS services in US East (N. Virginia) were unavailable.
  scope: Route 53 public hosted zones with accelerated recovery turned on; The feature must be turned on before the US East (N. Virginia) Region is impaired..
  link: [60-minute Recovery Time Objective (RTO)](../facts/route53.md#route53-accelerated-recovery-60-minute-rto)
  link: [US West (Oregon) Region](../facts/route53.md#route53-accelerated-recovery-60-minute-rto)
  link: [2025-11-26](../facts/route53.md#route53-accelerated-recovery-60-minute-rto)
  changed: 2025-11-26: was customers would not be able to modify or recreate DNS records to point users and internal services to updated endpoints
route53-accelerated-recovery-data-plane-keeps-answering
  claim: DNS query resolution from the Route 53 data plane continues to work normally during Regional service impairment. Accelerated recovery is about regaining the ability to make DNS changes: during a failover, Route 53 routes control plane requests for enabled hosted zones to the US West (Oregon) Region.
  scope: Route 53 data plane.
  link: [continues to work normally during Regional service impairment](../facts/route53.md#route53-accelerated-recovery-data-plane-keeps-answering)
route53-accelerated-recovery-failover-limits
  claim: During an accelerated recovery failover you cannot create new hosted zones, delete hosted zones, or turn DNSSEC signing on or off; only a short list of API methods keeps working.
  scope: Route 53 public hosted zones during an accelerated recovery failover; Applies until failback to US East (N. Virginia)..
  link: [can't create new hosted zones, delete hosted zones](../facts/route53.md#route53-accelerated-recovery-failover-limits)
route53-accelerated-recovery-public-zones-only
  claim: Accelerated recovery is available only for public hosted zones; private hosted zones are not supported.
  scope: Route 53 accelerated recovery.
  link: [available only for public hosted zones](../facts/route53.md#route53-accelerated-recovery-public-zones-only)
route53-accelerated-recovery-turn-on-before-impairment
  claim: You must turn on accelerated recovery before any issue with the US East (N. Virginia) Region occurs; you cannot turn it on after a failover starts.
  scope: Route 53 accelerated recovery; You can turn it on through the console, CLI, SDK or API..
  link: [must turn on accelerated recovery before any issues](../facts/route53.md#route53-accelerated-recovery-turn-on-before-impairment)
  link: [cannot turn on accelerated recovery after a failover](../facts/route53.md#route53-accelerated-recovery-turn-on-before-impairment)
route53-active-active-failover-definition
  claim: In active-active failover, all the records that have the same name, type and routing policy are active unless Route 53 considers them unhealthy. Route 53 can answer a DNS query with any healthy record.
  scope: active-active failover.
  link: [all the records that have the same name](../facts/route53.md#route53-active-active-failover-definition)
  link: [a DNS query using any healthy record](../facts/route53.md#route53-active-active-failover-definition)
route53-active-active-use-all-resources-available
  claim: Use active-active failover when you want all of your resources to be available the majority of the time. When a resource becomes unavailable, Route 53 can detect that it is unhealthy and stop including it in responses.
  scope: active-active failover.
  link: [all of your resources to be available](../facts/route53.md#route53-active-active-use-all-resources-available)
  link: [stop including it when responding to queries](../facts/route53.md#route53-active-active-use-all-resources-available)
route53-active-passive-failover-definition
  claim: Use active-passive failover when you want a primary resource or group of resources to be available the majority of the time and a secondary resource or group to be on standby in case all the primary resources become unavailable.
  scope: active-passive failover.
  link: [a primary resource or group of resources](../facts/route53.md#route53-active-passive-failover-definition)
  link: [group of resources to be on standby](../facts/route53.md#route53-active-passive-failover-definition)
route53-active-passive-only-healthy-primary-then-secondary
  claim: In active-passive failover, Route 53 includes only the healthy primary resources in responses. If all the primary resources are unhealthy, it begins to include only the healthy secondary resources.
  scope: active-passive failover.
  link: [includes only the healthy primary resources](../facts/route53.md#route53-active-passive-only-healthy-primary-then-secondary)
  link: [begins to include only the healthy secondary resources](../facts/route53.md#route53-active-passive-only-healthy-primary-then-secondary)
route53-alias-allowed-at-zone-apex
  claim: Unlike a CNAME record, you can create an alias record at the zone apex, the top node of a DNS namespace. For example.com, the zone apex is example.com.
  scope: alias record at the zone apex.
  link: [the top node of a DNS namespace](../facts/route53.md#route53-alias-allowed-at-zone-apex)
  link: [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex)
  link: [also known as the zone apex](../facts/route53.md#route53-alias-allowed-at-zone-apex)
route53-alias-answers-only-on-matching-name-and-type
  claim: Route 53 answers a query for an alias record only when the name and the type of the alias record match the name and type in the DNS query.
  scope: alias record.
  link: [the name and type in the DNS query](../facts/route53.md#route53-alias-answers-only-on-matching-name-and-type)
  link: [responds to a DNS query only when](../facts/route53.md#route53-alias-answers-only-on-matching-name-and-type)
route53-alias-apex-exception-cname-target
  claim: The one exception for an alias record at the zone apex is a redirect to a record of type CNAME in the same hosted zone; the alias record must have the same type as the record it routes to, and a CNAME record for the zone apex is not supported even for an alias record.
  scope: Amazon Route 53 alias record at the zone apex; The alias target is a record in the same hosted zone..
  link: [a type of CNAME](../facts/route53.md#route53-alias-apex-exception-cname-target)
  link: [must have the same type](../facts/route53.md#route53-alias-apex-exception-cname-target)
route53-alias-cloudfront-alternate-domain-matches-record-name
  claim: For an alias to a CloudFront distribution, the distribution must include an alternate domain name that matches the name of the record.
  scope: alias to a CloudFront distribution.
  link: [must include an alternate domain name that matches](../facts/route53.md#route53-alias-cloudfront-alternate-domain-matches-record-name)
route53-alias-cloudfront-ipv6-two-records
  claim: If IPv6 is enabled for a CloudFront distribution, you create two alias records for it: one of type A for IPv4 and one of type AAAA for IPv6.
  scope: alias to a CloudFront distribution.
  link: [create two records](../facts/route53.md#route53-alias-cloudfront-ipv6-two-records)
  link: [AAAA — IPv6 address](../facts/route53.md#route53-alias-cloudfront-ipv6-two-records)
route53-alias-elb-no-query-charge
  claim: Amazon Route 53 does not charge for alias queries to ELB load balancers or other AWS resources.
  scope: Amazon Route 53 alias queries.
  link: [doesn't charge for alias queries to ELB](../facts/route53.md#route53-alias-elb-no-query-charge)
route53-alias-evaluate-target-health-weighted-branch
  claim: If an alias record has Evaluate Target Health set to Yes and its alias target is a group of weighted records that all have nonzero weights, Route 53 considers the alias record healthy as long as at least one of the weighted records is healthy, and unhealthy if none of the weighted records is healthy. Route 53 stops considering records in that branch of the tree until at least one weighted record becomes healthy again.
  scope: alias record with Evaluate Target Health set to Yes; the weighted records all have nonzero weights.
  link: [at least one of the weighted records](../facts/route53.md#route53-alias-evaluate-target-health-weighted-branch)
  link: [none of the weighted records is healthy](../facts/route53.md#route53-alias-evaluate-target-health-weighted-branch)
route53-alias-extension-targets
  claim: Alias records route traffic to selected AWS resources, such as CloudFront distributions and S3 buckets, and from one record in a hosted zone to another record.
  scope: alias record.
  link: [route traffic to selected AWS resources](../facts/route53.md#route53-alias-extension-targets)
  link: [one record in a hosted zone to another](../facts/route53.md#route53-alias-extension-targets)
route53-alias-follows-resource-ip-changes
  claim: When an alias record points to an AWS resource, Route 53 detects changes in the resource on its own. If the IP address of a load balancer changes, Route 53 starts answering with the new IP address.
  scope: alias record that points to an AWS resource.
  link: [Route 53 detects changes in the resource on its own](../facts/route53.md#route53-alias-follows-resource-ip-changes)
  link: [DNS queries with the new IP address](../facts/route53.md#route53-alias-follows-resource-ip-changes)
route53-alias-queries-free-cname-charged
  claim: Amazon Route 53 does not charge for alias queries to AWS resources, but it charges for CNAME queries.
  scope: Amazon Route 53 DNS queries; Alias queries are free when the alias target is an AWS resource..
  link: [doesn't charge for alias queries to AWS resources](../facts/route53.md#route53-alias-queries-free-cname-charged)
  link: [charges for CNAME queries](../facts/route53.md#route53-alias-queries-free-cname-charged)
route53-alias-s3-record-name-matches-bucket-and-website-hosting
  claim: For an alias to an S3 bucket, the name of the record must match the name of the bucket, and you must configure the bucket for website hosting.
  scope: alias to an S3 bucket.
  link: [The name of the record must match the name of your Amazon S3 bucket](../facts/route53.md#route53-alias-s3-record-name-matches-bucket-and-website-hosting)
  link: [you must configure the bucket for website hosting](../facts/route53.md#route53-alias-s3-record-name-matches-bucket-and-website-hosting)
route53-alias-target-another-record-all-types-except-ns-soa
  claim: For an alias to another record in the same hosted zone, all record types are supported except NS and SOA. At the zone apex, an alias record can't route traffic to a record whose type is CNAME.
  scope: alias to another record in the same hosted zone; at the zone apex, not to a CNAME record.
  link: [All types are supported except NS and SOA](../facts/route53.md#route53-alias-target-another-record-all-types-except-ns-soa)
route53-alias-target-api-gateway
  claim: An alias record can point to an API Gateway custom regional API or edge-optimized API. Route 53 answers with one or more IP addresses for the API.
  scope: alias target.
  link: [API Gateway custom regional API or edge-optimized API](../facts/route53.md#route53-alias-target-api-gateway)
route53-alias-target-cloudfront
  claim: An alias record can point to a CloudFront distribution. Route 53 answers with one or more IP addresses for CloudFront edge servers that can serve your content.
  scope: alias target.
  link: [A CloudFront distribution](../facts/route53.md#route53-alias-target-cloudfront)
  link: [IP addresses for CloudFront edge servers](../facts/route53.md#route53-alias-target-cloudfront)
route53-alias-target-elastic-beanstalk
  claim: An alias record can point to an Elastic Beanstalk environment. Route 53 answers with one or more IP addresses for the environment.
  scope: alias target.
  link: [An Elastic Beanstalk environment](../facts/route53.md#route53-alias-target-elastic-beanstalk)
route53-alias-target-elb-answer
  claim: An alias record can point to an Elastic Load Balancing load balancer, including an Application Load Balancer, a Classic Load Balancer and a Network Load Balancer. Route 53 answers with one or more IP addresses for the load balancer.
  scope: alias target.
  link: [An Elastic Load Balancing load balancer](../facts/route53.md#route53-alias-target-elb-answer)
  link: [This includes Application Load Balancer, Classic Load Balancer](../facts/route53.md#route53-alias-target-elb-answer)
route53-alias-target-global-accelerator
  claim: An alias record can point to an AWS Global Accelerator accelerator. Route 53 answers with the IP addresses for the accelerator.
  scope: alias target.
  link: [An AWS Global Accelerator accelerator](../facts/route53.md#route53-alias-target-global-accelerator)
route53-alias-target-s3-website
  claim: An alias record can point to an S3 bucket that is configured as a static website. Route 53 answers with one IP address for the bucket.
  scope: alias target.
  link: [An Amazon S3 bucket that is configured as a static website](../facts/route53.md#route53-alias-target-s3-website)
  link: [one IP address for the Amazon S3 bucket](../facts/route53.md#route53-alias-target-s3-website)
route53-alias-target-vpc-interface-endpoint
  claim: An alias record can point to a VPC interface endpoint. Route 53 answers with one or more IP addresses for the interface endpoint.
  scope: alias target.
  link: [An Amazon VPC interface endpoint](../facts/route53.md#route53-alias-target-vpc-interface-endpoint)
route53-alias-targets-only-selected-aws-resources
  claim: An alias record can only redirect queries to selected AWS resources, such as S3 buckets, CloudFront distributions or another record in the same hosted zone. A CNAME record, in contrast, can redirect to any DNS record.
  scope: alias record versus CNAME record.
  link: [can only redirect queries to selected AWS resources](../facts/route53.md#route53-alias-targets-only-selected-aws-resources)
  link: [can redirect DNS queries to any DNS record](../facts/route53.md#route53-alias-targets-only-selected-aws-resources)
route53-alias-to-aws-resource-ttl-not-settable
  claim: If an alias record points to an AWS resource, you cannot set the TTL. Route 53 uses the default TTL for the resource.
  scope: alias record to an AWS resource.
  link: [you can't set the time to live (TTL)](../facts/route53.md#route53-alias-to-aws-resource-ttl-not-settable)
  link: [Route 53 uses the default TTL for the resource](../facts/route53.md#route53-alias-to-aws-resource-ttl-not-settable)
route53-alias-to-aws-use-evaluate-target-health-not-health-check
  claim: For AWS resources that you can create alias records for, you should not create Amazon Route 53 health checks; you set Evaluate Target Health to Yes on the alias record instead.
  scope: Amazon Route 53 failover configuration with alias records; The resource is an AWS resource for which you can create alias records..
  link: [set Evaluate Target Health to Yes](../facts/route53.md#route53-alias-to-aws-use-evaluate-target-health-not-health-check)
route53-alias-to-record-in-zone-uses-target-ttl
  claim: If an alias record points to another record in the same hosted zone, Route 53 uses the TTL of the target record.
  scope: alias record to another record in the same hosted zone.
  link: [uses the TTL of the target record](../facts/route53.md#route53-alias-to-record-in-zone-uses-target-ttl)
route53-api-change-throughput-1500-burst-100-sustained
  claim: The change throughput bucket of an AWS account has a maximum capacity of 1,500 changes (burst) and refills at 100 changes per second (sustained).
  scope: per AWS account; maximum; not adjustable; Change throughput is limited per AWS account, not per API action.
  link: [maximum capacity of 1,500 changes](../facts/route53.md#route53-api-change-throughput-1500-burst-100-sustained)
route53-api-change-tokens-per-operation
  claim: ChangeResourceRecordSets consumes 1 change token per CREATE, 1 per DELETE and 2 per UPSERT.
  scope: per ChangeResourceRecordSets change; fixed; not adjustable.
  link: [2 per UPSERT](../facts/route53.md#route53-api-change-tokens-per-operation)
route53-api-createhealthcheck-one-per-two-seconds
  claim: You can submit one CreateHealthCheck request every 2 seconds per AWS account.
  scope: per AWS account; maximum; not adjustable.
  link: [every 2 seconds](../facts/route53.md#route53-api-createhealthcheck-one-per-two-seconds)
route53-api-gateway-needs-matching-custom-domain-name
  claim: To route traffic to an API Gateway API, the API must have a custom domain name that matches the name of the Route 53 record you want to create.
  scope: alias to API Gateway.
  link: [has a custom domain name](../facts/route53.md#route53-api-gateway-needs-matching-custom-domain-name)
route53-api-gateway-regional-edge-private-alias
  claim: For a Regional API endpoint you create an alias record that routes to the Regional endpoint. For an edge-optimized endpoint the alias routes to the CloudFront distribution associated with the API. For a private API endpoint the alias routes through an interface VPC endpoint in a private hosted zone.
  scope: routing to API Gateway.
  link: [routes traffic to the Regional API endpoint](../facts/route53.md#route53-api-gateway-regional-edge-private-alias)
  link: [associated with the edge-optimized API](../facts/route53.md#route53-api-gateway-regional-edge-private-alias)
  link: [interface VPC endpoint for API Gateway](../facts/route53.md#route53-api-gateway-regional-edge-private-alias)
route53-api-limit-increase-through-support
  claim: You can request an increase to the API request rate limit or the change throughput limit through AWS Support.
  scope: per AWS account.
  link: [through AWS Support](../facts/route53.md#route53-api-limit-increase-through-support)
route53-api-request-bucket-account-50-refill-10
  claim: All Amazon Route 53 API actions combined share an account-level request bucket with a maximum capacity of 50 and a refill rate of 10.
  scope: per AWS account, all Route 53 API actions combined; default; adjustable; Increase is requested through AWS Support.
  link: [maximum capacity of 50](../facts/route53.md#route53-api-request-bucket-account-50-refill-10)
  link: [refill rate of 10](../facts/route53.md#route53-api-request-bucket-account-50-refill-10)
route53-api-throttled-http-400
  claim: When a request is throttled, Amazon Route 53 returns an HTTP 400 error (Bad request).
  scope: per API request.
  link: [HTTP 400 error](../facts/route53.md#route53-api-throttled-http-400)
route53-asg-unhealthy-instance-replaced
  claim: When Amazon EC2 Auto Scaling decides an InService instance is unhealthy, it replaces the instance with a new one to keep the desired capacity of the group.
  scope: Amazon EC2 Auto Scaling group health checks.
  link: [it replaces it with a new instance](../facts/route53.md#route53-asg-unhealthy-instance-replaced)
route53-associate-same-account-console-ok
  claim: You can use the console to associate more VPCs with a private hosted zone if you created the hosted zone and the VPCs with the same AWS account.
  scope: private hosted zone, same account.
  link: [by using the same AWS account](../facts/route53.md#route53-associate-same-account-console-ok)
  link: [use the Amazon Route 53 console to associate more VPCs](../facts/route53.md#route53-associate-same-account-console-ok)
route53-authoritative-ns-definition
  claim: An authoritative name server has definitive information about one part of the Domain Name System and answers a DNS resolver with the applicable information.
  scope: DNS concept.
  link: [definitive information about one part](../facts/route53.md#route53-authoritative-ns-definition)
  link: [responds to requests from a DNS resolver](../facts/route53.md#route53-authoritative-ns-definition)
route53-authoritative-ns-for-route53-domains
  claim: Route 53 name servers are the authoritative name servers for every domain that uses Route 53 as the DNS service. They store the hosted zones of those domains.
  scope: domains that use Route 53 as DNS service.
  link: [the authoritative name servers](../facts/route53.md#route53-authoritative-ns-for-route53-domains)
  link: [store the hosted zones](../facts/route53.md#route53-authoritative-ns-for-route53-domains)
route53-auto-public-zone-on-registration
  claim: After you register a domain name with Route 53, Route 53 automatically creates a public hosted zone with the same name as the domain.
  scope: domain registered with Route 53.
  link: [automatically creates a public hosted zone](../facts/route53.md#route53-auto-public-zone-on-registration)
  link: [has the same name as the domain](../facts/route53.md#route53-auto-public-zone-on-registration)
route53-best-practice-alias-cheaper-faster-than-cname
  claim: DNS resolvers must make more queries to answer CNAME records, which increases latency and cost, so where possible a Route 53 alias record is a faster and cheaper alternative that gives a direct answer for AWS resources and for other domains in the same hosted zone.
  scope: Amazon Route 53 alias and CNAME records.
  link: [increases latency and costs](../facts/route53.md#route53-best-practice-alias-cheaper-faster-than-cname)
  link: [a faster and cheaper alternative is to use a Route 53 alias record](../facts/route53.md#route53-best-practice-alias-cheaper-faster-than-cname)
route53-best-practice-always-set-default-record
  claim: When you use geolocation, geoproximity or latency-based routing, always set a default, unless you want some clients to receive a no answer response.
  scope: Amazon Route 53 geolocation, geoproximity and latency-based routing.
  link: [always set a default](../facts/route53.md#route53-best-practice-always-set-default-record)
route53-best-practice-shorten-ttl-before-critical-change
  claim: Before you change critical DNS entries, temporarily shorten the TTLs, make the change, observe and roll back quickly if needed, then raise the TTL again once the change works as expected.
  scope: Amazon Route 53 record TTL best practice.
  link: [temporarily shorten the TTLs](../facts/route53.md#route53-best-practice-shorten-ttl-before-critical-change)
route53-bp-control-plane-prioritizes-consistency-not-availability
  claim: The control planes of Route 53 are generally very reliable but are designed in a more centralized way and prioritize durability and consistency rather than high availability. For failover during disaster recovery, rely on features that use data plane functionality, such as health checks.
  scope: failover and disaster recovery.
  link: [prioritize durability and consistency rather than high availability](../facts/route53.md#route53-bp-control-plane-prioritizes-consistency-not-availability)
  link: [features like Route 53 health checks and ARC routing control that rely on data plane functionality](../facts/route53.md#route53-bp-control-plane-prioritizes-consistency-not-availability)
route53-bp-health-check-interval-tradeoff
  claim: Shorter health check intervals provide faster failure detection but might increase Route 53 costs and load on your resources. Longer intervals reduce costs and resource load but might delay failure detection.
  scope: health checks.
  link: [Shorter intervals provide faster failure detection](../facts/route53.md#route53-bp-health-check-interval-tradeoff)
  link: [Longer intervals reduce costs and resource load](../facts/route53.md#route53-bp-health-check-interval-tradeoff)
route53-bp-health-checks-use-elastic-ips-delete-unused
  claim: Use Elastic IP addresses for health check endpoints to ensure consistent monitoring. If you no longer use an EC2 instance, delete any associated health checks to avoid potential security risks or data compromise.
  scope: health checks.
  link: [elastic IP addresses for your health check endpoints](../facts/route53.md#route53-bp-health-checks-use-elastic-ips-delete-unused)
  link: [delete any associated health checks](../facts/route53.md#route53-bp-health-checks-use-elastic-ips-delete-unused)
route53-bp-latency-for-performance-geo-for-predictability
  claim: To minimize application latency use latency-based routing, whose routing data can change frequently. To provide routing stability and predictability use geolocation or geoproximity routing.
  scope: routing policy choice.
  link: [To minimize application latency, use latency-based routing](../facts/route53.md#route53-bp-latency-for-performance-geo-for-predictability)
  link: [use either geolocation or geoproximity routing](../facts/route53.md#route53-bp-latency-for-performance-geo-for-predictability)
route53-bp-use-multiple-health-check-regions-for-critical-resources
  claim: Consider using multiple health check Regions for critical resources to improve reliability and reduce the impact of regional outages.
  scope: health checks.
  link: [using multiple health check regions for critical resources](../facts/route53.md#route53-bp-use-multiple-health-check-regions-for-critical-resources)
route53-caa-cname-same-name-not-allowed
  claim: You cannot create a CAA record and a CNAME record that have the same name, because DNS does not allow the same name for a CNAME record and any other type of record.
  scope: CAA and CNAME records.
  link: [can't create a CAA record and a CNAME](../facts/route53.md#route53-caa-cname-same-name-not-allowed)
route53-caa-record-purpose
  claim: A CAA record specifies which certificate authorities are allowed to issue certificates for a domain or subdomain.
  scope: CAA record.
  link: [certificate authorities (CAs) are allowed to issue certificates](../facts/route53.md#route53-caa-record-purpose)
route53-case-intraway-multi-region-availability
  claim: The Intraway case study says that by activating on AWS in more than one Region, Intraway could multiply the availability of its existing resources instead of dividing them; the case study lists Amazon Route 53 among the AWS services that Intraway uses.
  scope: Intraway (case study).
  link: [multiply the availability of its existing resources](../facts/route53.md#route53-case-intraway-multi-region-availability)
route53-case-sony-ps5-launch-without-downtime
  claim: Sony Interactive Entertainment delivered the PS5 launch without downtime to millions of players around the world, and its case study names Amazon Route 53 among the AWS services used.
  scope: Sony Interactive Entertainment (case study).
  link: [delivered PS5 without downtime to millions of players around the world](../facts/route53.md#route53-case-sony-ps5-launch-without-downtime)
route53-change-accelerated-recovery-2025-11
  claim: Amazon Route 53 announced accelerated recovery for managing public DNS records on 2025-11-26, as an option for public hosted zones that targets a 60-minute recovery time objective if AWS services in US East (N. Virginia) become temporarily unavailable, with no additional charge.
  scope: Route 53 public hosted zones.
  link: [2025-11-26](../facts/route53.md#route53-change-accelerated-recovery-2025-11)
  link: [60-minute recovery time objective (RTO)](../facts/route53.md#route53-change-accelerated-recovery-2025-11)
  link: [no additional charge for using this feature](../facts/route53.md#route53-change-accelerated-recovery-2025-11)
route53-change-alias-cloudfront-tenant-2025-04
  claim: On April 28, 2025 you could start to add an alias record to a CloudFront distribution tenant.
  scope: Amazon Route 53 alias records.
  link: [April 28, 2025](../facts/route53.md#route53-change-alias-cloudfront-tenant-2025-04)
route53-change-alias-opensearch-2025-01
  claim: On January 14, 2025 Amazon Route 53 began to support alias records for OpenSearch Service custom domain endpoints.
  scope: Amazon Route 53 alias records.
  link: [January 14, 2025](../facts/route53.md#route53-change-alias-opensearch-2025-01)
route53-change-alias-vpc-lattice-2025-06
  claim: On June 25, 2025 Amazon Route 53 began to support alias records for VPC Lattice service custom domain endpoints.
  scope: Amazon Route 53 alias records.
  link: [June 25, 2025](../facts/route53.md#route53-change-alias-vpc-lattice-2025-06)
route53-change-cloudfront-flat-rate-plans-route53-2025-11
  claim: On 2025-11-18 AWS announced flat-rate pricing plans, available with Amazon CloudFront, that combine content delivery with AWS WAF, DDoS protection and Amazon Route 53 DNS into a simple monthly price with no overage charges.
  scope: Amazon CloudFront flat-rate plans and Amazon Route 53 DNS.
  link: [2025-11-18](../facts/route53.md#route53-change-cloudfront-flat-rate-plans-route53-2025-11)
  link: [flat-rate pricing plans](../facts/route53.md#route53-change-cloudfront-flat-rate-plans-route53-2025-11)
route53-change-dns-analytics-2026-10
  claim: On 2026-10-01 Route 53 Global Resolver and DNS Firewall added DNS analytics and insights through native Amazon CloudWatch integration. Not examinable yet.
  scope: Route 53 Global Resolver and DNS Firewall; Not examinable yet..
  link: [2026-10-01](../facts/route53.md#route53-change-dns-analytics-2026-10)
route53-change-dns-firewall-advanced-2024-11
  claim: On 2024-11-15 Amazon Route 53 added Resolver DNS Firewall Advanced, which identifies and blocks DNS traffic tied to advanced DNS threats such as DNS tunneling, Domain Generation Algorithm (DGA) and Dictionary DGA based threats.
  scope: Resolver DNS Firewall.
  link: [2024-11-15](../facts/route53.md#route53-change-dns-firewall-advanced-2024-11)
  link: [Domain Generation Algorithm (DGA), and Dictionary DGA](../facts/route53.md#route53-change-dns-firewall-advanced-2024-11)
route53-change-dns-firewall-categories-2026-05
  claim: On 2026-05-11 DNS Firewall added new threat and content domain categories to the DNS Firewall Advanced rule tier, and the existing Managed Domain Lists and custom lists became the DNS Firewall Foundational rule tier.
  scope: Resolver DNS Firewall.
  link: [2026-05-11](../facts/route53.md#route53-change-dns-firewall-categories-2026-05)
  link: [DNS Firewall Foundational rule tier](../facts/route53.md#route53-change-dns-firewall-categories-2026-05)
route53-change-dns-firewall-dictionary-dga-2025-11
  claim: On 2025-11-17 DNS Firewall Advanced added protection against Dictionary-based Domain Generation Algorithm (DGA) attacks, which generate domain names by concatenating words from a predefined dictionary to evade detection.
  scope: Resolver DNS Firewall Advanced.
  link: [2025-11-17](../facts/route53.md#route53-change-dns-firewall-dictionary-dga-2025-11)
  link: [Dictionary-based Domain Generation Algorithm (DGA) attacks](../facts/route53.md#route53-change-dns-firewall-dictionary-dga-2025-11)
route53-change-dns-firewall-eventbridge-2024-02
  claim: On February 5, 2024 Amazon EventBridge could be used for real time alerts with DNS Firewall.
  scope: Resolver DNS Firewall.
  link: [February 5, 2024](../facts/route53.md#route53-change-dns-firewall-eventbridge-2024-02)
route53-change-dns-firewall-panw-ga-2026-09
  claim: On 2026-09-29 Amazon Route 53 Resolver DNS Firewall support for Palo Alto Networks (PANW) Advanced DNS Security became generally available. Not examinable yet.
  scope: Resolver DNS Firewall; Not examinable yet..
  link: [2026-09-29](../facts/route53.md#route53-change-dns-firewall-panw-ga-2026-09)
route53-change-dns-firewall-query-type-2024-01
  claim: On January 9, 2024 the DNS query type became usable as an optional value of a DNS Firewall rule, to differentiate the rule's response for a specific query type.
  scope: Resolver DNS Firewall.
  link: [January 9, 2024](../facts/route53.md#route53-change-dns-firewall-query-type-2024-01)
route53-change-dns-firewall-redirect-chain-2024-04
  claim: On April 30, 2024 DNS Firewall rules gained a setting that decides whether the rule will inspect (the default) or trust the DNS redirection chain.
  scope: Resolver DNS Firewall rule setting for the DNS redirection chain; default.
  link: [inspect (default)](../facts/route53.md#route53-change-dns-firewall-redirect-chain-2024-04)
route53-change-dns-firewall-security-hub-2025-01
  claim: On January 13, 2025 Resolver DNS Firewall findings were added to Security Hub CSPM.
  scope: Resolver DNS Firewall.
  link: [January 13, 2025](../facts/route53.md#route53-change-dns-firewall-security-hub-2025-01)
route53-change-dns-over-https-resolver-2023-12
  claim: On December 20, 2023 DNS over HTTPS became usable with Resolver endpoints.
  scope: Route 53 VPC Resolver endpoints.
  link: [December 20, 2023](../facts/route53.md#route53-change-dns-over-https-resolver-2023-12)
route53-change-domains-34-new-tlds-2026-05
  claim: On 2026-05-11 Amazon Route 53 Domains added registration and management for 34 new top-level domains, including .app, .dev and .health.
  scope: Amazon Route 53 Domains.
  link: [2026-05-11](../facts/route53.md#route53-change-domains-34-new-tlds-2026-05)
  link: [34 new top-level domains (TLDs)](../facts/route53.md#route53-change-domains-34-new-tlds-2026-05)
route53-change-domains-ai-and-nine-tlds-2026-01
  claim: On 2026-01-23 Amazon Route 53 Domains added registration and management for ten new top-level domains, including .ai, .nz and .shop.
  scope: Amazon Route 53 Domains.
  link: [2026-01-23](../facts/route53.md#route53-change-domains-ai-and-nine-tlds-2026-01)
  link: [ten new top-level domains (TLDs)](../facts/route53.md#route53-change-domains-ai-and-nine-tlds-2026-01)
route53-change-geoproximity-local-zones-2023-07
  claim: On July 19, 2023 the developer guide history recorded that you could use Local Zones with geoproximity routing (traffic flow only) after you enable them. The current guide also offers Local Zone Groups for geoproximity records: for AWS resources you specify the AWS Region or Local Zone Group that you created the resource in, and you must first enable Local Zones.
  scope: Amazon Route 53 geoproximity routing; Local Zones must be enabled first.
  link: [July 19, 2023](../facts/route53.md#route53-change-geoproximity-local-zones-2023-07)
route53-change-geoproximity-records-console-2024-01
  claim: On January 9, 2024 the Quick create record and the Create record wizard began to support creating geoproximity routing records.
  scope: Amazon Route 53 geoproximity routing.
  link: [January 9, 2024](../facts/route53.md#route53-change-geoproximity-records-console-2024-01)
route53-change-global-resolver-ga-2026-03
  claim: Amazon Route 53 Global Resolver became generally available on 2026-03-09, available across 30 AWS Regions with IPv4 and IPv6 DNS query traffic, after a preview in 11 AWS Regions.
  scope: Route 53 Global Resolver.
  link: [2026-03-09](../facts/route53.md#route53-change-global-resolver-ga-2026-03)
  link: [30 AWS Regions](../facts/route53.md#route53-change-global-resolver-ga-2026-03)
route53-change-global-resolver-preview-2025-11
  claim: On 2025-11-30 AWS announced the preview of Amazon Route 53 Global Resolver, a new internet-reachable DNS resolver that provides DNS resolution from anywhere for queries made by authorized clients.
  scope: Route 53 Global Resolver; Preview announcement; general availability was announced on 2026-03-09..
  link: [2025-11-30](../facts/route53.md#route53-change-global-resolver-preview-2025-11)
  link: [a new internet-reachable DNS resolver](../facts/route53.md#route53-change-global-resolver-preview-2025-11)
route53-change-ip-based-routing-2022-06
  claim: On June 1, 2022 the IP-based routing option became available in Amazon Route 53.
  scope: Amazon Route 53 routing policies.
  link: [June 1, 2022](../facts/route53.md#route53-change-ip-based-routing-2022-06)
route53-change-ipv6-api-endpoint-2025-11
  claim: On 2025-11-21 Amazon Route 53 added dual stack support for the Route 53 DNS service API endpoint at route53.global.api.aws, and the existing IPv4 API endpoint stays available for backwards compatibility.
  scope: Amazon Route 53 DNS service API endpoint.
  link: [2025-11-21](../facts/route53.md#route53-change-ipv6-api-endpoint-2025-11)
  link: [route53.global.api.aws](../facts/route53.md#route53-change-ipv6-api-endpoint-2025-11)
route53-change-phz-geolocation-latency-2022-03
  claim: On March 16, 2022 geolocation and latency-based routing became supported for private hosted zones in Amazon Route 53.
  scope: Amazon Route 53 private hosted zones.
  link: [March 16, 2022](../facts/route53.md#route53-change-phz-geolocation-latency-2022-03)
route53-change-privatelink-for-route53-api-2025-11
  claim: On 2025-11-19 Amazon Route 53 added AWS PrivateLink support for API requests to the route53.amazonaws.com service endpoint, so workloads can make changes to hosted zones, records and health checks without using the public internet.
  scope: Amazon Route 53 API (control plane) requests; Customers outside US East (N. Virginia) use cross-Region interface VPC endpoints..
  link: [2025-11-19](../facts/route53.md#route53-change-privatelink-for-route53-api-2025-11)
  link: [API requests to the route53.amazonaws.com service endpoint](../facts/route53.md#route53-change-privatelink-for-route53-api-2025-11)
route53-change-profiles-2024-04
  claim: On April 22, 2024 Route 53 Profiles were added, to share DNS-specific configurations with many VPCs and with AWS accounts.
  scope: Route 53 Profiles.
  link: [April 22, 2024](../facts/route53.md#route53-change-profiles-2024-04)
route53-change-profiles-granular-iam-2026-03
  claim: On 2026-03-25 Amazon Route 53 Profiles gained granular IAM permissions that control which users can manage specific resource types and VPC associations within a Profile.
  scope: Route 53 Profiles; Available at no additional charge in the Regions where Profiles is available, except Middle East (Bahrain) and Middle East (UAE)..
  link: [2026-03-25](../facts/route53.md#route53-change-profiles-granular-iam-2026-03)
route53-change-profiles-privatelink-2025-10
  claim: On 2025-10-14 Amazon Route 53 Profiles began to support AWS PrivateLink, so you can access and manage your Profiles privately, without going through the public internet.
  scope: Amazon Route 53 Profiles.
  link: [2025-10-14](../facts/route53.md#route53-change-profiles-privatelink-2025-10)
  link: [access and manage their Profiles privately](../facts/route53.md#route53-change-profiles-privatelink-2025-10)
route53-change-profiles-query-logging-2025-11
  claim: On 2025-11-17 Amazon Route 53 Profiles gained support for Resolver query logging configurations; before, Resolver query logging had to be set up by hand for each VPC in every AWS account.
  scope: Route 53 Profiles and Resolver query logging.
  link: [2025-11-17](../facts/route53.md#route53-change-profiles-query-logging-2025-11)
  changed: 2025-11-17: was required you to manually set it up for each VPC in every AWS account
route53-change-profiles-vpc-endpoints-2025-04
  claim: On April 28, 2025 you could start to associate interface VPC endpoints to Route 53 Profiles.
  scope: Route 53 Profiles.
  link: [April 28, 2025](../facts/route53.md#route53-change-profiles-vpc-endpoints-2025-04)
route53-change-record-set-permissions-2022-09
  claim: On September 21, 2022 you could start to use IAM policy conditions to give users fine-grained access to updating resource record sets in Amazon Route 53.
  scope: Amazon Route 53 IAM policies.
  link: [September 21, 2022](../facts/route53.md#route53-change-record-set-permissions-2022-09)
route53-change-record-types-https-sshfp-svcb-tlsa-2024-10
  claim: On October 29, 2024 support was added for the HTTPS, SSHFP, SVCB and TLSA DNS record types in Amazon Route 53.
  scope: Amazon Route 53 supported DNS record types.
  link: [October 29, 2024](../facts/route53.md#route53-change-record-types-https-sshfp-svcb-tlsa-2024-10)
route53-change-resolver-delegation-2025-06
  claim: On June 24, 2025 inbound and outbound delegation became usable with VPC Resolver.
  scope: Route 53 VPC Resolver endpoints.
  link: [June 24, 2025](../facts/route53.md#route53-change-resolver-delegation-2025-06)
route53-change-resolver-detailed-metrics-2025-12
  claim: On December 15, 2025 detailed CloudWatch metrics were added for Route 53 Resolver endpoints.
  scope: Route 53 VPC Resolver endpoints.
  link: [December 15, 2025](../facts/route53.md#route53-change-resolver-detailed-metrics-2025-12)
route53-change-resolver-dns64-ipv6-2026-05
  claim: On 2026-05-07 Amazon Route 53 Resolver endpoints added DNS64 on inbound endpoints, to synthesize AAAA responses for domains that only have A records, and IPv6 forwarding through the internet gateway on outbound endpoints.
  scope: Route 53 VPC Resolver endpoints.
  link: [2026-05-07](../facts/route53.md#route53-change-resolver-dns64-ipv6-2026-05)
  link: [DNS64 on inbound endpoints](../facts/route53.md#route53-change-resolver-dns64-ipv6-2026-05)
route53-change-resolver-gen2-outposts-ga-2026-09
  claim: On 2026-09-22 Amazon Route 53 Resolver became generally available on second-generation AWS Outposts racks, resolving DNS queries from workloads on the Outpost locally. Not examinable yet.
  scope: Route 53 Resolver on second-generation AWS Outposts racks; Not examinable yet..
  link: [2026-09-22](../facts/route53.md#route53-change-resolver-gen2-outposts-ga-2026-09)
route53-change-resolver-ipv6-dual-stack-2023-03
  claim: On March 10, 2023 Route 53 VPC Resolver endpoints began to support IPv4, IPv6 and dual-stack endpoints for connecting to your resources.
  scope: Route 53 VPC Resolver endpoints.
  link: [March 10, 2023](../facts/route53.md#route53-change-resolver-ipv6-dual-stack-2023-03)
route53-change-resolver-privatelink-2025-10
  claim: On 2025-10-31 Amazon Route 53 Resolver and its related features (Resolver endpoints, DNS Firewall, Resolver query logging, Resolver for AWS Outposts) became accessible and manageable through AWS PrivateLink, without going through the public internet.
  scope: Route 53 VPC Resolver and its features.
  link: [2025-10-31](../facts/route53.md#route53-change-resolver-privatelink-2025-10)
  link: [without going through the public internet](../facts/route53.md#route53-change-resolver-privatelink-2025-10)
route53-change-vpc-resolver-rename-2025-11
  claim: In its 2025-11-30 announcement of Route 53 Global Resolver, AWS said it is renaming Route 53 Resolver to Route 53 VPC Resolver, and the guide now says VPC Resolver was previously called Route 53 Resolver.
  scope: Route 53 VPC Resolver name.
  link: [Route 53 VPC Resolver](../facts/route53.md#route53-change-vpc-resolver-rename-2025-11)
  link: [Route 53 Resolver](../facts/route53.md#route53-change-vpc-resolver-rename-2025-11)
  link: [2025-11-30](../facts/route53.md#route53-change-vpc-resolver-rename-2025-11)
  changed: 2025-11-30: was Route 53 Resolver
route53-change-vpcs-condition-2024-09
  claim: On September 3, 2024 the route53:VPCs policy condition could be used to grant fine-grained access to managing hosted zone associations to VPCs.
  scope: Amazon Route 53 IAM policies.
  link: [September 3, 2024](../facts/route53.md#route53-change-vpcs-condition-2024-09)
route53-changes-propagate-within-60-seconds
  claim: Changes to Route 53 records generally propagate to all Route 53 servers within 60 seconds.
  scope: record changes in Route 53; maximum; generally.
  link: [within 60 seconds](../facts/route53.md#route53-changes-propagate-within-60-seconds)
  link: [Changes generally propagate to all Route 53 servers](../facts/route53.md#route53-changes-propagate-within-60-seconds)
  say: within sixty seconds
route53-choose-failover-routing-active-passive
  claim: Use the failover routing policy when you want to configure active-passive failover.
  scope: Amazon Route 53 failover routing policy.
  link: [configure active-passive failover](../facts/route53.md#route53-choose-failover-routing-active-passive)
route53-choose-geolocation-routing-user-location
  claim: Use the geolocation routing policy when you want to route traffic based on the location of your users.
  scope: Amazon Route 53 geolocation routing policy.
  link: [based on the location of your users](../facts/route53.md#route53-choose-geolocation-routing-user-location)
route53-choose-geoproximity-routing-resource-location-bias
  claim: Use the geoproximity routing policy when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another location.
  scope: Amazon Route 53 geoproximity routing policy.
  link: [shift traffic from resources in one location](../facts/route53.md#route53-choose-geoproximity-routing-resource-location-bias)
route53-choose-ip-based-routing-known-client-ips
  claim: Use the IP-based routing policy when you want to route traffic based on the location of your users and you have the IP addresses that the traffic originates from.
  scope: Amazon Route 53 IP-based routing policy.
  link: [the IP addresses that the traffic originates from](../facts/route53.md#route53-choose-ip-based-routing-known-client-ips)
route53-choose-latency-routing-best-latency-region
  claim: Use the latency routing policy when you have resources in multiple AWS Regions and want to route traffic to the Region that provides the best latency.
  scope: Amazon Route 53 latency routing policy.
  link: [the Region that provides the best latency](../facts/route53.md#route53-choose-latency-routing-best-latency-region)
route53-choose-multivalue-routing-up-to-eight-healthy
  claim: Use the multivalue answer routing policy when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
  scope: Amazon Route 53 multivalue answer routing policy.
  link: [up to eight healthy records selected at random](../facts/route53.md#route53-choose-multivalue-routing-up-to-eight-healthy)
route53-choose-simple-routing-single-resource
  claim: Use the simple routing policy for a single resource that performs a given function for your domain, for example a web server for a website.
  scope: Amazon Route 53 simple routing policy.
  link: [Use for a single resource](../facts/route53.md#route53-choose-simple-routing-single-resource)
route53-choose-weighted-routing-proportions
  claim: Use the weighted routing policy to route traffic to multiple resources in proportions that you specify; it can be useful for load balancing and testing new versions of software.
  scope: Amazon Route 53 weighted routing policy.
  link: [multiple resources in proportions that you specify](../facts/route53.md#route53-choose-weighted-routing-proportions)
  link: [testing new versions of software](../facts/route53.md#route53-choose-weighted-routing-proportions)
route53-cidr-collection-location-block-hierarchy
  claim: You group CIDR blocks (IP ranges) into CIDR locations, which are in turn grouped into reusable entities called CIDR collections. IP-based records reference a location in a collection.
  scope: IP-based routing.
  link: [CIDR blocks (or IP ranges) into CIDR locations](../facts/route53.md#route53-cidr-collection-location-block-hierarchy)
  link: [grouped into reusable entities called CIDR collections](../facts/route53.md#route53-cidr-collection-location-block-hierarchy)
  link: [must reference the same collection](../facts/route53.md#route53-cidr-collection-location-block-hierarchy)
route53-cloudfront-alias-evaluate-target-health-default-no
  claim: When you create an alias record for a CloudFront distribution, Evaluate target health is set to No by default.
  scope: alias record to CloudFront; default; not adjustable.
  link: [default value of No](../facts/route53.md#route53-cloudfront-alias-evaluate-target-health-default-no)
route53-cloudfront-alias-public-hosted-zones-only
  claim: You can route traffic to a CloudFront distribution only for public hosted zones.
  scope: routing to CloudFront.
  link: [only for public hosted zones](../facts/route53.md#route53-cloudfront-alias-public-hosted-zones-only)
  link: [CloudFront distribution only for public hosted zones](../facts/route53.md#route53-cloudfront-alias-public-hosted-zones-only)
route53-cloudfront-do-not-route-before-edge-propagation
  claim: Do not route queries to a CloudFront distribution that has not propagated to all edge locations, or your users will not be able to access the content.
  scope: alias to a CloudFront distribution.
  link: [has not propagated to all edge locations](../facts/route53.md#route53-cloudfront-do-not-route-before-edge-propagation)
route53-cloudfront-needs-matching-alternate-domain-name
  claim: The CloudFront distribution must include an alternate domain name that matches the domain name you want to use in your URLs instead of the domain name CloudFront assigned.
  scope: CloudFront distribution used with a Route 53 alias.
  link: [must include an alternate domain name](../facts/route53.md#route53-cloudfront-needs-matching-alternate-domain-name)
  link: [matches the domain name that you want](../facts/route53.md#route53-cloudfront-needs-matching-alternate-domain-name)
route53-cloudfront-requires-alias-record
  claim: You must create an alias record for the CloudFront distribution to work with your domain name.
  scope: routing to CloudFront.
  link: [You must create an Alias record](../facts/route53.md#route53-cloudfront-requires-alias-record)
  link: [for the CloudFront distribution to work](../facts/route53.md#route53-cloudfront-requires-alias-record)
route53-cname-dns-protocol-forbids-zone-apex
  claim: The DNS protocol does not allow a CNAME record for the zone apex. You cannot create a CNAME record for example.com, but you can create CNAME records for names such as www.example.com.
  scope: CNAME record.
  link: [DNS protocol does not allow you to create](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex)
  link: [for the top node of a DNS namespace](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex)
route53-cname-excludes-other-records-same-name
  claim: If you create a CNAME record for a subdomain, you cannot create any other records for that subdomain.
  scope: CNAME record.
  link: [cannot create any other records for that subdomain](../facts/route53.md#route53-cname-excludes-other-records-same-name)
  link: [create a CNAME record for a subdomain](../facts/route53.md#route53-cname-excludes-other-records-same-name)
route53-cname-not-allowed-at-zone-apex
  claim: You cannot create a CNAME record that has the same name as the hosted zone (the zone apex). This is true for hosted zones for domain names and for hosted zones for subdomains.
  scope: CNAME record.
  link: [You can't create a CNAME record](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
  link: [the same name as the hosted zone](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
route53-cname-only-for-subdomains
  claim: You can create CNAME records only for subdomains. An alias record works for both the root domain and subdomains.
  scope: CNAME record versus alias record.
  link: [CNAME records only for subdomains](../facts/route53.md#route53-cname-only-for-subdomains)
  link: [an alias record both for the root domain](../facts/route53.md#route53-cname-only-for-subdomains)
route53-cname-record-maps-name-to-name
  claim: A CNAME record maps DNS queries for the name of the current record to another domain or subdomain.
  scope: CNAME record.
  link: [queries for the name of the current record](../facts/route53.md#route53-cname-record-maps-name-to-name)
  link: [to another domain](../facts/route53.md#route53-cname-record-maps-name-to-name)
route53-cname-record-name-cannot-equal-zone-name
  claim: If you create a CNAME record, the name of the record cannot be the same as the name of the hosted zone.
  scope: CNAME record.
  link: [name of the record can't be the same](../facts/route53.md#route53-cname-record-name-cannot-equal-zone-name)
route53-cname-record-takes-one-value-only
  claim: For all record types except CNAME, you can enter more than one value in a record.
  scope: record values.
  link: [For all types except CNAME](../facts/route53.md#route53-cname-record-takes-one-value-only)
route53-cname-redirects-any-record-type
  claim: A CNAME record redirects DNS queries for a record name regardless of the record type in the query, such as A or AAAA.
  scope: CNAME record.
  link: [regardless of the record type](../facts/route53.md#route53-cname-redirects-any-record-type)
route53-cname-target-need-not-be-route53
  claim: A CNAME record can redirect DNS queries to any DNS record, for example from acme.example.com to zenith.example.com or to acme.example.org, and you don't need to use Route 53 as the DNS service for the domain that you're redirecting queries to.
  scope: CNAME record.
  link: [You don't need to use Route 53 as the DNS service](../facts/route53.md#route53-cname-target-need-not-be-route53)
route53-cname-to-route53-record-charged-two-queries
  claim: A CNAME that redirects to the name of another record in a Route 53 hosted zone is charged as two queries per DNS query. If it redirects to a record hosted with another DNS service, Route 53 charges for one query.
  scope: CNAME record.
  link: [each DNS query is charged as two queries](../facts/route53.md#route53-cname-to-route53-record-charged-two-queries)
  link: [Route 53 charges for one query](../facts/route53.md#route53-cname-to-route53-record-charged-two-queries)
  say: two queries
route53-complex-config-evaluate-target-health-no-keeps-routing
  claim: You should set Evaluate Target Health to Yes for all the alias records in a tree. If you set it to No, Route 53 continues to route traffic to the records the alias refers to even if their health checks are failing.
  scope: complex configurations.
  link: [set Evaluate Target Health to Yes](../facts/route53.md#route53-complex-config-evaluate-target-health-no-keeps-routing)
  link: [continues to route traffic to the records](../facts/route53.md#route53-complex-config-evaluate-target-health-no-keeps-routing)
route53-complex-config-health-check-and-eth-both-must-pass
  claim: If you assign a health check to a latency alias record whose alias target is a group of weighted records, and set Evaluate Target Health to Yes for that latency alias record, both of the following must be true before Route 53 returns the value of a weighted record: the health check associated with the latency alias record must pass, and at least one weighted record must be considered healthy.
  scope: latency alias record with a health check and Evaluate Target Health, whose alias target is a group of weighted records.
  link: [both of the following must be true](../facts/route53.md#route53-complex-config-health-check-and-eth-both-must-pass)
  link: [associated with the latency alias record must pass](../facts/route53.md#route53-complex-config-health-check-and-eth-both-must-pass)
route53-complex-config-latency-alias-weighted-tree
  claim: You can combine alias and non-alias records to build a decision tree, for example latency alias records that select a Region and weighted records inside each Region, with Evaluate Target Health set to Yes on the latency alias records.
  scope: complex configurations.
  link: [build a decision tree](../facts/route53.md#route53-complex-config-latency-alias-weighted-tree)
  link: [any healthy resources in a Region](../facts/route53.md#route53-complex-config-latency-alias-weighted-tree)
route53-complex-config-omitted-health-check-assumed-healthy
  claim: In a complex configuration, a non-alias record without a health check is assumed to be healthy, because Route 53 has no way to know whether the resource is healthy. It is important to associate health checks with all non-alias records.
  scope: complex configurations.
  link: [Route 53 assumes that the resource is healthy](../facts/route53.md#route53-complex-config-omitted-health-check-assumed-healthy)
  link: [associate health checks with all the non-alias records](../facts/route53.md#route53-complex-config-omitted-health-check-assumed-healthy)
route53-console-us-east-1-fallback-us-west-2
  claim: The Route 53 console is in us-east-1. If AWS finds an impairment in that Region, the console is served from us-west-2.
  scope: Route 53 console for public and private DNS.
  link: [located in the us-east-1 AWS Region](../facts/route53.md#route53-console-us-east-1-fallback-us-west-2)
  link: [served by the us-west-2 AWS Region](../facts/route53.md#route53-console-us-east-1-fallback-us-west-2)
route53-control-plane-us-east-1
  claim: For Route 53 public and private DNS and health checks, the control plane is in the us-east-1 Region and the data planes are globally distributed.
  scope: public and private DNS, health checks.
  link: [control plane is located in the us-east-1 AWS Region](../facts/route53.md#route53-control-plane-us-east-1)
  link: [data planes are globally distributed](../facts/route53.md#route53-control-plane-us-east-1)
route53-control-vs-data-plane-design
  claim: The control plane is optimized for data consistency and the data plane is optimized for availability. The data plane can stay available even when the control plane is unavailable, so use data plane functions where availability matters.
  scope: control plane and data plane.
  link: [optimized for data consistency](../facts/route53.md#route53-control-vs-data-plane-design)
  link: [optimized for availability](../facts/route53.md#route53-control-vs-data-plane-design)
  link: [use data plane functions](../facts/route53.md#route53-control-vs-data-plane-design)
route53-create-phz-needs-ec2-permissions
  claim: To create private hosted zones, you must grant IAM permissions for Amazon EC2 actions in addition to permissions for Route 53 actions.
  scope: creating private hosted zones.
  link: [IAM permissions for Amazon EC2 actions](../facts/route53.md#route53-create-phz-needs-ec2-permissions)
  link: [in addition to permissions for Route 53 actions](../facts/route53.md#route53-create-phz-needs-ec2-permissions)
route53-cross-account-association-needs-authorization-no-console
  claim: To associate a VPC from one account with a private hosted zone from another account, you must first authorize the association. You cannot use the AWS console to authorize or to make the association.
  scope: private hosted zone, VPC in a different account.
  link: [you first must authorize the association](../facts/route53.md#route53-cross-account-association-needs-authorization-no-console)
  link: [you can't use the AWS console](../facts/route53.md#route53-cross-account-association-needs-authorization-no-console)
route53-cross-account-auth-by-hosted-zone-account
  claim: The account that created the hosted zone authorizes the association of the VPC with the private hosted zone. Then the account that created the VPC associates the VPC with the hosted zone. For both steps you can use the AWS SDK, Tools for Windows PowerShell, the AWS CLI, or the Route 53 API.
  scope: cross-account private hosted zone association.
  link: [Using the account that created the hosted zone](../facts/route53.md#route53-cross-account-auth-by-hosted-zone-account)
  link: [Using the account that created the VPC, associate](../facts/route53.md#route53-cross-account-auth-by-hosted-zone-account)
route53-cross-account-delete-authorization-recommended
  claim: After you associate the VPC, AWS recommends deleting the authorization. Deleting it does not affect the association; it only prevents you from reassociating the VPC later.
  scope: cross-account association.
  link: [does not affect the association](../facts/route53.md#route53-cross-account-delete-authorization-recommended)
  link: [prevents you from reassociating the VPC](../facts/route53.md#route53-cross-account-delete-authorization-recommended)
route53-cross-account-one-authorization-per-vpc
  claim: To associate several VPCs from one account with a hosted zone from another account, you must submit one authorization request for each VPC. The private hosted zone must already exist, because you specify the hosted zone ID.
  scope: cross-account association.
  link: [one authorization request for each VPC](../facts/route53.md#route53-cross-account-one-authorization-per-vpc)
  link: [the private hosted zone must already exist](../facts/route53.md#route53-cross-account-one-authorization-per-vpc)
route53-custom-dns-servers-forward-to-vpc-plus-two
  claim: If you run custom DNS servers on EC2 instances in your VPC, you must configure them to route private DNS queries to the Amazon-provided DNS server of the VPC. Its address is the base of the VPC network range plus two.
  scope: custom DNS servers on EC2 instances.
  link: [Amazon-provided DNS servers for your VPC](../facts/route53.md#route53-custom-dns-servers-forward-to-vpc-plus-two)
  link: [base of the VPC network range "plus two."](../facts/route53.md#route53-custom-dns-servers-forward-to-vpc-plus-two)
route53-dangling-delegate-only-to-zones-you-control
  claim: If you delegate a domain or subdomain to Route 53 name servers before you create a corresponding hosted zone, this creates dangling delegation records, and Route 53 cannot protect against this. To mitigate the risk, only delegate to Route 53 name servers that belong to a public hosted zone that you control.
  scope: delegation records.
  link: [only delegate to Route 53 name servers that belong to a public hosted zone that you control](../facts/route53.md#route53-dangling-delegate-only-to-zones-you-control)
route53-dangling-delegation-match-parent-ns-to-delegation-set
  claim: There are dangling delegation record risks that Route 53 can't protect against. To protect yourself against them, make sure the parent NS records match the delegation set of the Route 53 hosted zone. Enabling DNSSEC signing for the hosted zone can serve as another layer of protection.
  scope: delegation records.
  link: [parent NS records match the delegation set](../facts/route53.md#route53-dangling-delegation-match-parent-ns-to-delegation-set)
  link: [enabling DNSSEC signing for a Route 53 hosted zone can serve as another layer of protection](../facts/route53.md#route53-dangling-delegation-match-parent-ns-to-delegation-set)
route53-dangling-delegation-protection-on-zone-delete
  claim: After a hosted zone is deleted, if a new hosted zone is created with the same domain name, Route 53 checks whether the delegation records still point to the deleted zone and, if they do, prevents overlapping name servers from being assigned.
  scope: deleted hosted zones.
  link: [Route 53 will check if the delegation records pointing to the deleted hosted zone are still present](../facts/route53.md#route53-dangling-delegation-protection-on-zone-delete)
  link: [Route 53 will prevent any overlapping name servers from being assigned](../facts/route53.md#route53-dangling-delegation-protection-on-zone-delete)
route53-decision-guide-edge-category-vs-elb
  claim: In the AWS networking and content delivery decision guide, edge networking and content delivery services help ensure higher performance through caching and optimized transport; Amazon Route 53 routes customer traffic to provide availability, AWS Global Accelerator routes customer traffic to make the most of the AWS global infrastructure, and Elastic Load Balancing helps the workloads in your VPCs scale and provide high availability.
  scope: AWS networking and content delivery decision guide.
  link: [higher performance through caching and optimized transport](../facts/route53.md#route53-decision-guide-edge-category-vs-elb)
  link: [make the most of the AWS global infrastructure](../facts/route53.md#route53-decision-guide-edge-category-vs-elb)
  link: [scale and provide high availability](../facts/route53.md#route53-decision-guide-edge-category-vs-elb)
route53-decision-guide-ga-reliability-latency
  claim: The networking decision guide says AWS Global Accelerator can help you improve the reliability, security and latency of your workloads, and recommends it for gaming, IoT and VoIP workloads.
  scope: AWS Global Accelerator in the networking decision guide.
  link: [reliability, security, and latency of your workloads](../facts/route53.md#route53-decision-guide-ga-reliability-latency)
route53-default-domains-existing-account-50
  claim: An existing account whose default domain limit is 50 keeps a limit of 50.
  scope: per AWS account; default; adjustable; Existing account with a default limit of 50.
  link: [remain at 50](../facts/route53.md#route53-default-domains-existing-account-50)
route53-default-domains-new-customers
  claim: The default limit on domains is 20 for new customers as of March 2021.
  scope: per AWS account; default; adjustable; New customers as of March 2021.
  link: [20 for new customers](../facts/route53.md#route53-default-domains-new-customers)
route53-default-random-name-servers-per-zone
  claim: By default, Route 53 assigns a random selection of name servers to each new hosted zone. You cannot change the name servers of an existing hosted zone.
  scope: each new hosted zone; default; not adjustable; existing hosted zone cannot change its name servers.
  link: [a random selection of name servers](../facts/route53.md#route53-default-random-name-servers-per-zone)
  link: [can't change the name servers](../facts/route53.md#route53-default-random-name-servers-per-zone)
route53-default-unique-delegation-set-per-zone
  claim: By default, Route 53 assigns a unique set of four name servers, called a delegation set, to each hosted zone that you create.
  scope: each hosted zone you create; default; not adjustable; reusable delegation set not used.
  link: [a unique set of four name servers](../facts/route53.md#route53-default-unique-delegation-set-per-zone)
  link: [called a delegation set](../facts/route53.md#route53-default-unique-delegation-set-per-zone)
  say: four name servers
route53-delegate-from-immediate-parent-zone
  claim: When you delegate multiple levels of subdomains, always delegate from the parent zone. Delegations from a grandparent to a child zone might not work at all or work only inconsistently.
  scope: subdomain delegation.
  link: [always delegate from the parent zone](../facts/route53.md#route53-delegate-from-immediate-parent-zone)
  link: [not work at all or work only inconsistently](../facts/route53.md#route53-delegate-from-immediate-parent-zone)
route53-dns-change-propagation-under-one-minute
  claim: DNS change propagation typically takes less than one minute globally, but occasional delays happen.
  scope: per DNS change; Typical time, not a guarantee.
  link: [less than one minute](../facts/route53.md#route53-dns-change-propagation-under-one-minute)
route53-dns-data-plane-pops
  claim: The data plane for public and private DNS is the authoritative DNS service. It runs across over 200 Points of Presence locations and answers queries from your hosted zones and health check data.
  scope: Route 53 public and private DNS data plane.
  link: [over 200 Points of Presence (PoP) locations](../facts/route53.md#route53-dns-data-plane-pops)
  link: [the authoritative DNS service](../facts/route53.md#route53-dns-data-plane-pops)
route53-dns-failover-routes-traffic-away-from-unhealthy-record
  claim: For multiple resources that perform the same function, you can configure DNS failover: associate a health check with each record, and if a health check finds the resource unhealthy, Route 53 routes traffic away from the associated record.
  scope: DNS failover.
  link: [Associate a health check with each record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record)
  link: [Route 53 routes traffic away from the associated record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record)
route53-dns-firewall-advanced-rule-tier
  claim: The DNS Firewall Advanced rule tier gives protections that help detect and monitor more advanced DNS threats, such as Domain Generation Algorithms (DGA) or DNS tunneling, and more granular protections based on threat and web-content categories.
  scope: Resolver DNS Firewall Advanced rule tier.
  link: [Domain Generation Algorithms (DGA) or DNS Tunneling](../facts/route53.md#route53-dns-firewall-advanced-rule-tier)
  link: [more granular protections based on threat and web-content](../facts/route53.md#route53-dns-firewall-advanced-rule-tier)
route53-dns-firewall-blocks-dns-exfiltration
  claim: A primary use of DNS Firewall is to help prevent DNS exfiltration of your data, which happens when a bad actor who compromises an application instance in your VPC uses DNS lookups to send data to a domain they control.
  scope: Resolver DNS Firewall.
  link: [help prevent DNS exfiltration of your data](../facts/route53.md#route53-dns-firewall-blocks-dns-exfiltration)
route53-dns-firewall-vs-network-firewall
  claim: DNS Firewall filters outbound DNS queries that pass through the Route 53 VPC Resolver from applications in your VPCs; Network Firewall filters network and application layer traffic but has no visibility into queries made by the Route 53 VPC Resolver.
  scope: Resolver DNS Firewall compared with AWS Network Firewall.
  link: [filtering for outbound DNS queries that pass through the Route 53 VPC Resolver](../facts/route53.md#route53-dns-firewall-vs-network-firewall)
  link: [does not have visibility into queries made by Route 53 VPC Resolver](../facts/route53.md#route53-dns-firewall-vs-network-firewall)
route53-dns-resolver-is-recursive-name-server
  claim: A DNS resolver, also called a recursive name server, sends requests to a sequence of authoritative name servers until it gets the answer, which it returns to the user's device.
  scope: DNS concept.
  link: [also known as a recursive name server](../facts/route53.md#route53-dns-resolver-is-recursive-name-server)
  link: [a sequence of authoritative DNS name servers](../facts/route53.md#route53-dns-resolver-is-recursive-name-server)
route53-dns-response-512-bytes-tcp-retry
  claim: If a DNS response is larger than 512 bytes, many resolvers must retry over TCP instead of UDP, which can reduce reliability and slow responses.
  scope: per DNS response; maximum; not adjustable.
  link: [larger than 512 bytes](../facts/route53.md#route53-dns-response-512-bytes-tcp-retry)
route53-dns-service-can-be-elsewhere-for-route53-domains
  claim: You do not have to use Route 53 as the DNS service provider for domains registered with Route 53. You can also migrate DNS service to another DNS service provider.
  scope: domain registration and DNS service.
  link: [You don't have to use Route 53 as the DNS service provider for domains registered with Route 53](../facts/route53.md#route53-dns-service-can-be-elsewhere-for-route53-domains)
  link: [migrate DNS service to another DNS service provider](../facts/route53.md#route53-dns-service-can-be-elsewhere-for-route53-domains)
route53-dns-udp-response-truncated-edns0-allows-more
  claim: If the resolver supports EDNS0 and advertises it to Route 53, Route 53 permits responses up to 4096 bytes over UDP without truncation.
  scope: DNS responses over UDP; maximum.
  link: [up to 4096 bytes over UDP, without truncation](../facts/route53.md#route53-dns-udp-response-truncated-edns0-allows-more)
route53-dnsfw-action-alert-permits-and-logs
  claim: The Alert action stops inspecting the query, permits it to go through, and logs an alert for the query in the VPC Resolver logs.
  scope: DNS Firewall rule actions.
  link: [and log an alert for the query](../facts/route53.md#route53-dnsfw-action-alert-permits-and-logs)
  link: [log an alert for the query](../facts/route53.md#route53-dnsfw-action-alert-permits-and-logs)
route53-dnsfw-action-allow-stops-inspection
  claim: The Allow action stops inspecting the query and permits it to go through. Allow is not available for DNS Firewall Advanced.
  scope: DNS Firewall rule actions.
  link: [Stop inspecting the query and permit it](../facts/route53.md#route53-dnsfw-action-allow-stops-inspection)
  link: [Not available for DNS Firewall Advanced](../facts/route53.md#route53-dnsfw-action-allow-stops-inspection)
route53-dnsfw-action-block-responses
  claim: The Block action discontinues inspection of the query, blocks it from going to its intended destination, and logs the block. The block response can be NODATA, NXDOMAIN, or an OVERRIDE with a custom CNAME record.
  scope: DNS Firewall rule actions.
  link: [block it from going to its intended destination](../facts/route53.md#route53-dnsfw-action-block-responses)
  link: [the query's domain name doesn't exist](../facts/route53.md#route53-dnsfw-action-block-responses)
route53-dnsfw-advanced-detects-threat-signatures
  claim: DNS Firewall Advanced protection detects suspicious DNS queries based on known threat signatures in DNS queries, such as DNS traffic associated with Domain Generation Algorithms (DGA) and DNS tunneling. Each rule in a rule group needs a single DNS Firewall Advanced protection setting, and the threat protection algorithms are managed and updated by AWS.
  scope: DNS Firewall Advanced.
  link: [suspicious DNS queries based on known threat signatures](../facts/route53.md#route53-dnsfw-advanced-detects-threat-signatures)
  link: [managed and updated by AWS](../facts/route53.md#route53-dnsfw-advanced-detects-threat-signatures)
route53-dnsfw-advanced-rules-block-or-alert-only
  claim: In a DNS Firewall Advanced rule you can choose to either block, or alert on a query that matches the threat; the Allow action is not available for DNS Firewall Advanced.
  scope: DNS Firewall Advanced rules.
  link: [choose to either block, or alert](../facts/route53.md#route53-dnsfw-advanced-rules-block-or-alert-only)
route53-dnsfw-can-block-private-hosted-zone-names
  claim: DNS Firewall can block resolution requests to resources in private hosted zones, shared or local, including VPC endpoint names.
  scope: Resolver DNS Firewall.
  link: [requests to resources in private hosted zones](../facts/route53.md#route53-dnsfw-can-block-private-hosted-zone-names)
route53-dnsfw-cloudwatch-monitors-filtered-queries
  claim: You can use Amazon CloudWatch to monitor the number of DNS queries that are filtered by DNS Firewall rule groups.
  scope: Resolver DNS Firewall.
  link: [DNS queries that are filtered by DNS Firewall](../facts/route53.md#route53-dnsfw-cloudwatch-monitors-filtered-queries)
route53-dnsfw-config-applies-when-rule-group-associated
  claim: VPC Resolver enforces the firewall configuration of a VPC whenever one or more DNS Firewall rule groups are associated with the VPC.
  scope: DNS Firewall VPC configuration.
  link: [one or more DNS Firewall rule groups associated](../facts/route53.md#route53-dnsfw-config-applies-when-rule-group-associated)
route53-dnsfw-custom-response-for-blocked-queries
  claim: You can customize the responses for the DNS queries that DNS Firewall blocks.
  scope: Resolver DNS Firewall.
  link: [customize the responses for the DNS queries](../facts/route53.md#route53-dnsfw-custom-response-for-blocked-queries)
route53-dnsfw-domain-lists-own-or-aws-managed
  claim: You can create your own domain lists and you can use domain lists that AWS manages for you.
  scope: DNS Firewall domain lists.
  link: [create your own domain lists](../facts/route53.md#route53-dnsfw-domain-lists-own-or-aws-managed)
  link: [domain lists that AWS manages for you](../facts/route53.md#route53-dnsfw-domain-lists-own-or-aws-managed)
route53-dnsfw-fail-closed-default-sends-servfail
  claim: By default the DNS Firewall failure mode is closed: VPC Resolver blocks any query for which it does not receive a reply from DNS Firewall and sends a SERVFAIL response. This favors security over availability.
  scope: DNS Firewall VPC configuration; default; adjustable.
  link: [By default, the failure mode is closed](../facts/route53.md#route53-dnsfw-fail-closed-default-sends-servfail)
  link: [favors security over availability](../facts/route53.md#route53-dnsfw-fail-closed-default-sends-servfail)
route53-dnsfw-fail-open-favors-availability
  claim: If you enable fail open, VPC Resolver allows queries through when it does not receive a reply from DNS Firewall. This favors availability over security.
  scope: DNS Firewall VPC configuration.
  link: [VPC Resolver allows queries through](../facts/route53.md#route53-dnsfw-fail-open-favors-availability)
  link: [favors availability over security](../facts/route53.md#route53-dnsfw-fail-open-favors-availability)
route53-dnsfw-feature-of-vpc-resolver-no-extra-setup
  claim: DNS Firewall is a feature of Route 53 VPC Resolver and does not require any additional VPC Resolver setup to use.
  scope: Resolver DNS Firewall.
  link: [DNS Firewall is a feature of Route 53 VPC Resolver](../facts/route53.md#route53-dnsfw-feature-of-vpc-resolver-no-extra-setup)
  link: [doesn't require any additional VPC Resolver setup](../facts/route53.md#route53-dnsfw-feature-of-vpc-resolver-no-extra-setup)
route53-dnsfw-filters-domain-name-only-not-other-protocols
  claim: DNS Firewall filters only on the domain name and does not resolve that name to an IP address to be blocked. It filters DNS traffic but not other application layer protocols such as HTTPS, SSH, TLS or FTP.
  scope: Resolver DNS Firewall.
  link: [DNS Firewall only filters on the domain name](../facts/route53.md#route53-dnsfw-filters-domain-name-only-not-other-protocols)
  link: [it doesn't filter other application layer protocols](../facts/route53.md#route53-dnsfw-filters-domain-name-only-not-other-protocols)
route53-dnsfw-filters-inbound-endpoint-queries-in-same-vpc
  claim: When a DNS Firewall rule group is associated with a VPC's Route 53 VPC Resolver, DNS Firewall filters the DNS queries that pass through Resolver endpoints from on-premises resources into that same VPC.
  scope: Resolver DNS Firewall.
  link: [pass through Resolver endpoints from on-premises resources](../facts/route53.md#route53-dnsfw-filters-inbound-endpoint-queries-in-same-vpc)
route53-dnsfw-filters-outbound-dns-for-vpc
  claim: Resolver DNS Firewall filters and regulates outbound DNS traffic for your VPC. You create rule groups of filtering rules, associate them with your VPC, and monitor activity in DNS Firewall logs and metrics.
  scope: Resolver DNS Firewall.
  link: [filter and regulate outbound DNS traffic](../facts/route53.md#route53-dnsfw-filters-outbound-dns-for-vpc)
  link: [filtering rules in DNS Firewall rule groups](../facts/route53.md#route53-dnsfw-filters-outbound-dns-for-vpc)
route53-dnsfw-firewall-manager-central-management
  claim: You can use AWS Firewall Manager to centrally configure and manage DNS Firewall rule group associations for your VPCs across your accounts in AWS Organizations.
  scope: Resolver DNS Firewall.
  link: [centrally configure and manage your DNS Firewall](../facts/route53.md#route53-dnsfw-firewall-manager-central-management)
route53-dnsfw-no-match-responds-as-normal
  claim: If DNS Firewall evaluates all rule groups without finding a match, it responds to the query as normal.
  scope: Resolver DNS Firewall.
  link: [responds to the query as normal](../facts/route53.md#route53-dnsfw-no-match-responds-as-normal)
route53-dnsfw-prevents-dns-exfiltration
  claim: A primary use of DNS Firewall protections is to help prevent DNS exfiltration of your data. You can deny the domains you know to be bad, or deny all domains except the ones you explicitly trust.
  scope: Resolver DNS Firewall.
  link: [help prevent DNS exfiltration of your data](../facts/route53.md#route53-dnsfw-prevents-dns-exfiltration)
  link: [except for the ones that you explicitly trust](../facts/route53.md#route53-dnsfw-prevents-dns-exfiltration)
route53-dnsfw-query-type-default-all-types
  claim: If you do not select a query type for a DNS Firewall rule with a domain list, the rule is applied to all DNS query types.
  scope: DNS Firewall rule with a domain list; default; adjustable.
  link: [rule is applied to all DNS query types](../facts/route53.md#route53-dnsfw-query-type-default-all-types)
route53-dnsfw-rule-actions-allow-block-alert
  claim: A DNS Firewall rule can allow, block, or alert on matching queries. Allow is available only for rules with domain lists.
  scope: DNS Firewall rules.
  link: [allow (rules with domain lists only)](../facts/route53.md#route53-dnsfw-rule-actions-allow-block-alert)
  link: [block, or alert on matching queries](../facts/route53.md#route53-dnsfw-rule-actions-allow-block-alert)
route53-dnsfw-rule-groups-processed-lowest-priority-first
  claim: If you associate multiple rule groups with one VPC, you set the processing order with the priority setting of each association, and DNS Firewall processes them from the lowest numeric priority up.
  scope: DNS Firewall rule groups.
  link: [from the lowest numeric priority setting on up](../facts/route53.md#route53-dnsfw-rule-groups-processed-lowest-priority-first)
  link: [the priority setting in each association](../facts/route53.md#route53-dnsfw-rule-groups-processed-lowest-priority-first)
route53-dnsfw-rules-exist-only-within-rule-group
  claim: DNS Firewall rules exist only in the context of the rule group in which they are defined. You cannot reuse a rule or reference it independent of its rule group.
  scope: DNS Firewall rules.
  link: [only in the context of the rule group](../facts/route53.md#route53-dnsfw-rules-exist-only-within-rule-group)
  link: [You can't reuse a rule](../facts/route53.md#route53-dnsfw-rules-exist-only-within-rule-group)
route53-dnsfw-use-alert-to-test-blocking-rules
  claim: When you first create a blocking rule, you can test it by setting the action to Alert, and then look at how many queries the rule alerts on to see how many would be blocked.
  scope: DNS Firewall rule actions.
  link: [configuring it with the action set to Alert](../facts/route53.md#route53-dnsfw-use-alert-to-test-blocking-rules)
route53-dnssec-cmk-in-us-east-1-asymmetric-ecc-nist-p256
  claim: The customer managed key for DNSSEC signing must be in the US East (N. Virginia) Region. It must be an asymmetric customer managed key with the ECC_NIST_P256 key spec, used only for signing and verification.
  scope: DNSSEC signing key.
  link: [be in the US East (N. Virginia) Region](../facts/route53.md#route53-dnssec-cmk-in-us-east-1-asymmetric-ecc-nist-p256)
  link: [ECC_NIST_P256](../facts/route53.md#route53-dnssec-cmk-in-us-east-1-asymmetric-ecc-nist-p256)
route53-dnssec-ds-support-needed-in-parent-zone
  claim: If your parent zone is hosted by a DNS provider that does not support DS queries, then when you enable DNSSEC in the child zone, the child zone becomes unresolvable.
  scope: DNSSEC signing.
  link: [the child zone will become unresolvable](../facts/route53.md#route53-dnssec-ds-support-needed-in-parent-zone)
route53-dnssec-ksk-based-on-customer-managed-kms-key
  claim: In Route 53 DNSSEC signing, each key-signing key (KSK) is based on an asymmetric customer managed key in AWS KMS that you own. You are responsible for KSK management, including rotation. Route 53 manages the zone-signing key (ZSK).
  scope: DNSSEC signing.
  link: [each KSK is based on an](../facts/route53.md#route53-dnssec-ksk-based-on-customer-managed-kms-key)
  link: [ZSK management is performed by Route 53](../facts/route53.md#route53-dnssec-ksk-based-on-customer-managed-kms-key)
route53-dnssec-multi-vendor-not-supported
  claim: When you use DNSSEC signing, multi-vendor configurations are not supported. If you have configured white-label name servers, make sure those name servers are provided by a single DNS provider.
  scope: DNSSEC signing.
  link: [multi-vendor configurations are not supported](../facts/route53.md#route53-dnssec-multi-vendor-not-supported)
route53-dnssec-signing-validates-responses-from-route53
  claim: DNSSEC signing lets DNS resolvers validate that a DNS response came from the DNS service and has not been tampered with. Every response for a signed hosted zone is signed using public key cryptography.
  scope: DNSSEC signing.
  link: [validate that a DNS response came from Amazon Route 53](../facts/route53.md#route53-dnssec-signing-validates-responses-from-route53)
  link: [every response for a hosted zone is signed](../facts/route53.md#route53-dnssec-signing-validates-responses-from-route53)
route53-dnssec-ttl-capped-at-one-week
  claim: When you enable DNSSEC signing for a hosted zone, Route 53 limits the TTL to one week. If you set a longer TTL you get no error, but Route 53 enforces a TTL of one week.
  scope: hosted zone with DNSSEC signing; maximum.
  link: [Route 53 limits the TTL to one week](../facts/route53.md#route53-dnssec-ttl-capped-at-one-week)
  say: one week
route53-domain-registrar-is-amazon-registrar-or-gandi
  claim: The domain registrar is either Amazon Registrar, Inc. or the registrar associate Gandi.
  scope: domain registration.
  link: [Amazon Registrar, Inc. or our registrar associate, Gandi](../facts/route53.md#route53-domain-registrar-is-amazon-registrar-or-gandi)
route53-domain-registration-control-plane-only-us-east-1
  claim: Route 53 domain registrations are managed only on the control plane in the us-east-1 Region.
  scope: domain registration.
  link: [managed only on the control plane](../facts/route53.md#route53-domain-registration-control-plane-only-us-east-1)
  link: [us-east-1 AWS Region](../facts/route53.md#route53-domain-registration-control-plane-only-us-east-1)
route53-domain-registration-makes-route53-the-dns-service
  claim: When you register a domain with Route 53, the service automatically makes itself the DNS service for the domain. It creates a hosted zone with the same name, assigns four name servers to it, and adds those name servers to the domain.
  scope: domain registered with Route 53.
  link: [makes itself the DNS service for the domain](../facts/route53.md#route53-domain-registration-makes-route53-the-dns-service)
  link: [the same name as your domain](../facts/route53.md#route53-domain-registration-makes-route53-the-dns-service)
route53-domain-transfer-not-required-for-other-features
  claim: If you already registered a domain with another registrar, you can transfer the registration to Route 53, but this is not required to use other Route 53 features.
  scope: domain registration.
  link: [This isn't required to use other Route 53 features](../facts/route53.md#route53-domain-transfer-not-required-for-other-features)
  link: [you can transfer the domain registration to Route 53](../facts/route53.md#route53-domain-transfer-not-required-for-other-features)
route53-domain-transfer-unlock-and-auth-code
  claim: To transfer a domain registration to Route 53, you must unlock the domain, because ICANN requires that you unlock your domain before you transfer it. An authorization code from the current registrar authorizes Route 53 to request the transfer; some top-level domains have additional requirements, for example a .co.za domain needs no authorization code.
  scope: domain transfer to Route 53; some top-level domains have additional requirements; .co.za needs no authorization code.
  link: [you unlock your domain before you transfer it](../facts/route53.md#route53-domain-transfer-unlock-and-auth-code)
  link: [An authorization code from the current registrar](../facts/route53.md#route53-domain-transfer-unlock-and-auth-code)
route53-dr-active-active-no-failover
  claim: With multi-site active/active, the workload runs in more than one Region, so there is no failover step; testing instead checks whether traffic is routed away from the failed Region and whether the other Regions can handle all the traffic.
  scope: multi-site active/active disaster recovery.
  link: [no such thing as failover in this scenario](../facts/route53.md#route53-dr-active-active-no-failover)
route53-dr-active-active-policies-by-user
  claim: For the multi-site active/active strategy, Amazon Route 53 and AWS Global Accelerator both let you define policies that decide which users go to which active Regional endpoint, and Amazon Route 53 also supports a percentage approach and other policies including geoproximity and latency based ones.
  scope: multi-site active/active disaster recovery.
  link: [which users go to which active regional endpoint](../facts/route53.md#route53-dr-active-active-policies-by-user)
  link: [including geoproximity and latency based ones](../facts/route53.md#route53-dr-active-active-policies-by-user)
route53-dr-active-passive-route53-or-ga
  claim: For the pilot light and warm standby strategies, both Amazon Route 53 and AWS Global Accelerator can route network traffic to the active Region.
  scope: pilot light and warm standby disaster recovery.
  link: [both Amazon Route 53 and AWS Global Accelerator can be used](../facts/route53.md#route53-dr-active-passive-route53-or-ga)
route53-dr-auto-failover-use-with-caution
  claim: For an active/passive setup such as pilot light, failover can be started automatically or manually; automatically initiated failover based on health checks or alarms should be used with caution because a false alarm costs availability and data.
  scope: active/passive disaster recovery.
  link: [should be used with caution](../facts/route53.md#route53-dr-auto-failover-use-with-caution)
route53-dr-failover-use-data-plane-only
  claim: For maximum resiliency, a failover operation should use only data plane operations, because data planes typically have higher availability design goals than control planes.
  scope: disaster recovery failover on AWS.
  link: [use only data plane operations](../facts/route53.md#route53-dr-failover-use-data-plane-only)
route53-dr-health-check-failover-data-plane
  claim: With Amazon Route 53 health checks you can configure automatically initiated DNS failover so that traffic goes only to healthy endpoints, which the DR whitepaper calls a highly reliable operation done on the data plane.
  scope: Amazon Route 53 DNS failover.
  link: [highly reliable operation done on the data plane](../facts/route53.md#route53-dr-health-check-failover-data-plane)
route53-dr-weight-change-is-control-plane
  claim: Changing the weights of a weighted routing policy to send all traffic to the recovery Region is a control plane operation, so the DR whitepaper calls it less resilient than the data plane approach.
  scope: manually initiated failover with a weighted routing policy.
  link: [this is a control plane operation](../facts/route53.md#route53-dr-weight-change-is-control-plane)
route53-ds-record-dnssec-chain-of-trust
  claim: A delegation signer (DS) record refers a zone key for a delegated subdomain zone. You might create it when you establish a chain of trust for DNSSEC signing.
  scope: DS record.
  link: [A delegation signer (DS) record](../facts/route53.md#route53-ds-record-dnssec-chain-of-trust)
  link: [establish a chain of trust](../facts/route53.md#route53-ds-record-dnssec-chain-of-trust)
route53-ec2-elastic-ip-recommended
  claim: When a DNS record routes traffic to an Amazon EC2 instance, AWS recommends that you also create an Elastic IP address and associate it with the instance, because an Elastic IP address ensures that the IP address of the instance will never change.
  scope: Amazon EC2 instance behind a Route 53 record; Pricing for Elastic IP addresses applies..
  link: [will never change](../facts/route53.md#route53-ec2-elastic-ip-recommended)
route53-ec2-route-with-a-record-ip-address
  claim: To route traffic to an EC2 instance, you create a record of type A (IPv4 address) whose value is the IP address of the instance.
  scope: routing a domain to an EC2 instance.
  link: [Enter the IP address that you got in step 1](../facts/route53.md#route53-ec2-route-with-a-record-ip-address)
  link: [Choose A – IPv4 address](../facts/route53.md#route53-ec2-route-with-a-record-ip-address)
route53-edns0-not-applicable-to-private-hosted-zones
  claim: EDNS0 is not applicable to private hosted zones. For private hosted zones, Route 53 uses data from the VPC Resolvers in the AWS Region of the private hosted zone for geolocation and latency routing decisions.
  scope: private hosted zones.
  link: [EDNS0 is not applicable to private hosted zones](../facts/route53.md#route53-edns0-not-applicable-to-private-hosted-zones)
  link: [from the VPC Resolvers in the AWS Region](../facts/route53.md#route53-edns0-not-applicable-to-private-hosted-zones)
route53-edns0-with-support-uses-user-subnet
  claim: When the DNS resolver supports edns-client-subnet, it sends Route 53 a shortened version of the user's IP address, and Route 53 finds the user's location from it instead of from the resolver's source IP address. This usually gives a more accurate location.
  scope: geolocation, geoproximity, IP-based and latency routing.
  link: [a shortened version of the user's IP address](../facts/route53.md#route53-edns0-with-support-uses-user-subnet)
  link: [usually gives a more accurate location](../facts/route53.md#route53-edns0-with-support-uses-user-subnet)
route53-edns0-without-support-uses-resolver-ip
  claim: When the DNS resolver does not support edns-client-subnet, Route 53 uses the source IP address of the DNS resolver to guess where the user is and answers geolocation queries with the record for the resolver's location.
  scope: geolocation, geoproximity, IP-based and latency routing.
  link: [the source IP address of the DNS resolver](../facts/route53.md#route53-edns0-without-support-uses-resolver-ip)
  link: [does not support edns-client-subnet](../facts/route53.md#route53-edns0-without-support-uses-resolver-ip)
route53-elb-alias-evaluate-target-health-yes-routes-by-health
  claim: For an alias record to a load balancer, choose Yes for Evaluate target health if you want Route 53 to route traffic based on the health of your resources.
  scope: alias record to an ELB load balancer.
  link: [choose Yes](../facts/route53.md#route53-elb-alias-evaluate-target-health-yes-routes-by-health)
  link: [traffic based on the health of your resources](../facts/route53.md#route53-elb-alias-evaluate-target-health-yes-routes-by-health)
route53-elb-alias-load-balancer-types
  claim: You can create an alias record to an ELB Classic, Application or Network Load Balancer.
  scope: alias record to an ELB load balancer.
  link: [ELB Classic, Application, or Network Load Balancer](../facts/route53.md#route53-elb-alias-load-balancer-types)
  link: [an ELB Classic, Application, or Network Load Balancer](../facts/route53.md#route53-elb-alias-load-balancer-types)
route53-elb-alias-record-for-root-and-subdomains
  claim: To route domain traffic to an ELB load balancer, you create an alias record. An alias record works for the root domain and for subdomains, while CNAME records work only for subdomains.
  scope: alias record to an ELB load balancer.
  link: [both for the root domain](../facts/route53.md#route53-elb-alias-record-for-root-and-subdomains)
  link: [CNAME records only for subdomains](../facts/route53.md#route53-elb-alias-record-for-root-and-subdomains)
route53-elb-dns-entry-updated-ttl-60
  claim: As traffic changes, Elastic Load Balancing scales the load balancer and updates its DNS entry, and that DNS entry specifies a time-to-live (TTL) of 60 seconds so the IP addresses can be remapped quickly.
  scope: Elastic Load Balancing DNS entry; fixed.
  link: [time-to-live (TTL) of 60 seconds](../facts/route53.md#route53-elb-dns-entry-updated-ttl-60)
  link: [load balancer and updates the DNS entry](../facts/route53.md#route53-elb-dns-entry-updated-ttl-60)
route53-elb-health-check-routes-only-healthy-fails-open
  claim: An Application Load Balancer node routes requests only to the healthy targets in the enabled Availability Zones. If all targets fail health checks at the same time in all enabled Availability Zones, the load balancer fails open, which allows traffic to all targets in all enabled Availability Zones regardless of their health status.
  scope: Application Load Balancer target group health checks; Fail-open applies when every registered target in every enabled Availability Zone is unhealthy..
  link: [routes requests only to the healthy targets](../facts/route53.md#route53-elb-health-check-routes-only-healthy-fails-open)
  link: [the load balancer fails open](../facts/route53.md#route53-elb-health-check-routes-only-healthy-fails-open)
route53-evaluate-target-health-benefit-for-elb-beanstalk
  claim: For load balancers (ELB) and Elastic Beanstalk environments with load balancers, setting Evaluate target health to Yes lets Route 53 route traffic away from unhealthy resources.
  scope: alias records with routing policies other than simple.
  link: [setting Evaluate target health to Yes](../facts/route53.md#route53-evaluate-target-health-benefit-for-elb-beanstalk)
  link: [route traffic away from unhealthy resources](../facts/route53.md#route53-evaluate-target-health-benefit-for-elb-beanstalk)
route53-evaluate-target-health-no-benefit-for-ha-services
  claim: For Amazon S3 buckets, VPC interface endpoints, API Gateway, Global Accelerator, OpenSearch Service and VPC Lattice, Evaluate target health gives no operational benefit because these services are designed for high availability.
  scope: alias records with routing policies other than simple.
  link: [provides no operational benefit](../facts/route53.md#route53-evaluate-target-health-no-benefit-for-ha-services)
  link: [designed for high availability](../facts/route53.md#route53-evaluate-target-health-no-benefit-for-ha-services)
route53-evaluate-target-health-no-effect-on-simple-routing
  claim: For a simple routing alias record, Evaluate target health has no effect. If you have only one record with a given name and type, Route 53 answers with that record even if the resource is unhealthy.
  scope: alias record with simple routing.
  link: [has no effect for Simple routing](../facts/route53.md#route53-evaluate-target-health-no-effect-on-simple-routing)
  link: [regardless of whether the resource is healthy](../facts/route53.md#route53-evaluate-target-health-no-effect-on-simple-routing)
route53-evaluate-target-health-other-policies-checks-resource
  claim: For routing policies other than simple, Evaluate target health determines whether Route 53 checks the health of the resource that the alias record refers to.
  scope: alias records with routing policies other than simple.
  link: [whether Route 53 checks the health of the resource](../facts/route53.md#route53-evaluate-target-health-other-policies-checks-resource)
  link: [the resource that the alias record refers to](../facts/route53.md#route53-evaluate-target-health-other-policies-checks-resource)
route53-failover-active-active-any-policy-but-failover
  claim: You configure active-active failover with any routing policy (or combination of routing policies) other than failover, and active-passive failover with the failover routing policy.
  scope: Amazon Route 53 health checking and failover.
  link: [configure active-passive failover using the failover routing policy](../facts/route53.md#route53-failover-active-active-any-policy-but-failover)
route53-failover-alias-health-check-and-evaluate-both-true
  claim: If you associate a health check with an alias record and also select Yes for Evaluate Target Health, both must evaluate to true for the record to be used.
  scope: Amazon Route 53 alias records with health checks.
  link: [both must evaluate to true](../facts/route53.md#route53-failover-alias-health-check-and-evaluate-both-true)
route53-failover-both-unhealthy-returns-primary
  claim: If you associate health checks with both failover records and Route 53 considers both the primary and the secondary unhealthy, Route 53 returns the primary record.
  scope: failover records that both have health checks.
  link: [Route 53 returns the primary record](../facts/route53.md#route53-failover-both-unhealthy-returns-primary)
  link: [both the primary and secondary records unhealthy](../facts/route53.md#route53-failover-both-unhealthy-returns-primary)
route53-failover-multiple-primary-healthy-if-one-healthy
  claim: When several resources are associated with the primary failover record, Amazon Route 53 considers the primary record healthy as long as at least one of the associated resources is healthy.
  scope: Amazon Route 53 active-passive failover.
  link: [at least one of the associated resources](../facts/route53.md#route53-failover-multiple-primary-healthy-if-one-healthy)
route53-failover-needs-one-primary-one-secondary
  claim: For failover to work correctly, you must create one primary and one secondary failover record.
  scope: failover routing.
  link: [one primary and one secondary failover record](../facts/route53.md#route53-failover-needs-one-primary-one-secondary)
  link: [For failover to function correctly](../facts/route53.md#route53-failover-needs-one-primary-one-secondary)
route53-failover-no-non-failover-record-same-name-type
  claim: You cannot create non-failover records that have the same record name and record type as failover records.
  scope: failover records.
  link: [You can't create non-failover records](../facts/route53.md#route53-failover-no-non-failover-record-same-name-type)
route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy
  claim: With one primary record and one secondary record, Route 53 answers with the primary record when the primary resource is healthy and with the secondary record when the primary resource is unhealthy.
  scope: failover routing with one primary and one secondary record.
  link: [responds to DNS queries using the primary record](../facts/route53.md#route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy)
  link: [responds to DNS queries using the secondary record](../facts/route53.md#route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy)
route53-failover-record-health-check-checks-its-own-endpoint
  claim: Amazon Route 53 does not check the health of the endpoint in the record value; when you select a health check for a record, Route 53 checks the endpoint that you specified in the health check.
  scope: Amazon Route 53 records and health checks.
  link: [endpoint that you specified in the health check](../facts/route53.md#route53-failover-record-health-check-checks-its-own-endpoint)
route53-failover-routing-primary-or-secondary
  claim: With failover routing, you route traffic to a resource when it is healthy, or to a different resource when the first one is unhealthy. The primary and secondary records can route traffic to anything from an S3 website bucket to a complex tree of records.
  scope: failover routing.
  link: [when the first one is unhealthy](../facts/route53.md#route53-failover-routing-primary-or-secondary)
  link: [anything from an Amazon S3 bucket set up as a website to a complex tree of records](../facts/route53.md#route53-failover-routing-primary-or-secondary)
route53-failover-secondary-health-check-optional
  claim: When you configure the secondary failover record, adding a health check is optional. If you omit it and the primary endpoint is unhealthy, Route 53 always answers with the secondary record, even if the secondary record is unhealthy.
  scope: secondary failover record.
  link: [adding a health check is optional](../facts/route53.md#route53-failover-secondary-health-check-optional)
  link: [by using the secondary record](../facts/route53.md#route53-failover-secondary-health-check-optional)
route53-failover-weighted-zero-weight-caveat
  claim: With weighted records used for active-passive failover, all the records with nonzero weights must be unhealthy before Route 53 answers with records that have weight zero. This can make a site unreliable if the last healthy resource cannot handle all the traffic.
  scope: weighted records used for failover.
  link: [records with nonzero weights must be unhealthy](../facts/route53.md#route53-failover-weighted-zero-weight-caveat)
route53-faq-a-record-multiple-ip-addresses
  claim: You can list multiple IP addresses for one A record, and the service answers DNS requests with the list of all configured IP addresses.
  scope: simple A records.
  link: [multiple IP addresses for an A record](../facts/route53.md#route53-faq-a-record-multiple-ip-addresses)
route53-faq-alias-can-point-at-traffic-policy-name
  claim: You can create an alias record that points to a DNS name that is managed by a traffic policy.
  scope: Traffic Flow policy records.
  link: [Alias record pointing to a DNS name](../facts/route53.md#route53-faq-alias-can-point-at-traffic-policy-name)
route53-faq-alias-elb-queries-no-charge
  claim: There is no additional charge for queries to alias records that are mapped to AWS ELB load balancers.
  scope: alias records mapped to ELB; queries are listed as Intra-AWS-DNS-Queries on the usage report.
  link: [no additional charge for queries to Alias records](../facts/route53.md#route53-faq-alias-elb-queries-no-charge)
route53-faq-alias-elb-s3-fixed-ttl-60-seconds
  claim: Alias records used for DNS failover with ELB and S3 website endpoints have a fixed TTL of 60 seconds, so you do not need to adjust TTLs for those endpoint types.
  scope: alias records to ELB and S3 website endpoints; fixed; not adjustable; used with DNS Failover.
  link: [fixed TTL of 60 seconds](../facts/route53.md#route53-faq-alias-elb-s3-fixed-ttl-60-seconds)
  say: sixty seconds
route53-faq-alias-for-subdomains
  claim: Alias records can map sub-domains such as www.example.com to ELB load balancers, CloudFront distributions or S3 website buckets.
  scope: alias records.
  link: [map your sub-domains](../facts/route53.md#route53-faq-alias-for-subdomains)
route53-faq-alias-is-route53-extension
  claim: Alias records are an Amazon Route 53-specific extension to DNS, used to route traffic to selected AWS resources.
  scope: alias records.
  link: [Amazon Route 53-specific extension to DNS](../facts/route53.md#route53-faq-alias-is-route53-extension)
route53-faq-alias-queries-free-beanstalk-apigw-vpce
  claim: There is no additional charge for queries to alias records mapped to Elastic Beanstalk environments, API Gateways or VPC endpoints.
  scope: alias records mapped to AWS resources.
  link: [no additional charge for queries to Alias records](../facts/route53.md#route53-faq-alias-queries-free-beanstalk-apigw-vpce)
route53-faq-alias-s3-cloudfront-queries-no-charge
  claim: Route 53 does not charge for queries to alias records that are mapped to a CloudFront distribution or to an S3 bucket configured as a website.
  scope: alias records mapped to CloudFront or S3 website buckets.
  link: [doesn't charge for queries to Alias records](../facts/route53.md#route53-faq-alias-s3-cloudfront-queries-no-charge)
route53-faq-alias-targets-list
  claim: Alias records can route traffic to Elastic Load Balancing load balancers, CloudFront distributions, Elastic Beanstalk environments, API Gateways, VPC interface endpoints and S3 buckets that are configured as websites.
  scope: alias records; list as stated in the FAQ.
  link: [S3 buckets that are configured as websites](../facts/route53.md#route53-faq-alias-targets-list)
route53-faq-alias-two-advantages-over-cname
  claim: Alias records have two advantages over CNAMEs: unlike a CNAME, an alias record can be created for the zone apex, and queries to alias records are free of charge.
  scope: alias records to CloudFront and S3 website buckets.
  link: [two advantages](../facts/route53.md#route53-faq-alias-two-advantages-over-cname)
  link: [queries to Alias records are free of charge](../facts/route53.md#route53-faq-alias-two-advantages-over-cname)
route53-faq-alias-type-a-or-aaaa-like-cname
  claim: An alias record usually has the type A or AAAA but works like a CNAME record.
  scope: alias records.
  link: [type of A or AAAA](../facts/route53.md#route53-faq-alias-type-a-or-aaaa-like-cname)
route53-faq-all-endpoints-unhealthy-acts-as-all-pass
  claim: If no healthy endpoints remain in a record set, Amazon Route 53 behaves as if all health checks are passing, because it can only fail over to an endpoint that is healthy.
  scope: resource record set with health checks; no healthy endpoints remaining.
  link: [behave as if all health checks are passing](../facts/route53.md#route53-faq-all-endpoints-unhealthy-acts-as-all-pass)
route53-faq-alternate-domain-name-on-bucket-or-distribution
  claim: To fully establish the alias between your domain name and an S3 bucket or CloudFront distribution, you must also configure the bucket or distribution with the alternate domain name entry.
  scope: S3 buckets and CloudFront distributions.
  link: [alternate domain name entry](../facts/route53.md#route53-faq-alternate-domain-name-on-bucket-or-distribution)
route53-faq-anycast-optimal-location
  claim: Amazon Route 53 uses anycast, a networking and routing technology that helps DNS queries get answered from the optimal Route 53 location given network conditions.
  scope: Route 53 DNS service.
  link: [optimal Route 53 location](../facts/route53.md#route53-faq-anycast-optimal-location)
route53-faq-apex-alias-api-gateway
  claim: An alias record can map the zone apex to an Amazon API Gateway DNS name.
  scope: alias records to API Gateway.
  link: [your Amazon API Gateway DNS name](../facts/route53.md#route53-faq-apex-alias-api-gateway)
route53-faq-apex-alias-cloudfront
  claim: An alias record can map the zone apex to an Amazon CloudFront distribution.
  scope: alias records to CloudFront.
  link: [your Amazon CloudFront distribution](../facts/route53.md#route53-faq-apex-alias-cloudfront)
route53-faq-apex-alias-elastic-beanstalk
  claim: An alias record can map the zone apex to an AWS Elastic Beanstalk environment DNS name.
  scope: alias records to Elastic Beanstalk.
  link: [your AWS Elastic Beanstalk DNS name](../facts/route53.md#route53-faq-apex-alias-elastic-beanstalk)
route53-faq-apex-alias-elb-three-types
  claim: An alias record can map the zone apex to a load balancer, and Route 53 supports alias records for three types of load balancers: Application, Network and Classic.
  scope: alias records to ELB.
  link: [three types of load balancers](../facts/route53.md#route53-faq-apex-alias-elb-three-types)
route53-faq-apex-alias-s3-website
  claim: An alias record can map the zone apex to an Amazon S3 website bucket, and Route 53 answers each request with one IP address for the bucket.
  scope: alias records to S3 website buckets; bucket configured as a website.
  link: [zone apex (example.com) DNS name to your Amazon S3 website bucket](../facts/route53.md#route53-faq-apex-alias-s3-website)
route53-faq-apex-alias-vpc-endpoint
  claim: An alias record can map the zone apex to an Amazon VPC endpoint DNS name.
  scope: alias records to VPC endpoints.
  link: [your Amazon VPC Endpoint DNS name](../facts/route53.md#route53-faq-apex-alias-vpc-endpoint)
route53-faq-authoritative-vs-recursive-dns
  claim: Amazon Route 53 is both an authoritative DNS service and a recursive DNS service; authoritative DNS holds the final answer to a query, and clients talk to recursive DNS services (resolvers), which find the correct authoritative answer.
  scope: Route 53 DNS and VPC Resolver; VPC Resolver is the recursive service.
  link: [an Authoritative DNS service and Recursive DNS service](../facts/route53.md#route53-faq-authoritative-vs-recursive-dns)
route53-faq-bias-only-geoproximity-rules
  claim: Asked whether bias can be used for other Traffic Flow rules, the FAQ answers that bias can only be applied to geoproximity rules.
  scope: Traffic Flow rules; as of the FAQ text.
  link: [bias can only be applied to geoproximity rules](../facts/route53.md#route53-faq-bias-only-geoproximity-rules)
route53-faq-calculated-health-check-combines-results
  claim: A calculated health check combines the results of metric based health checks with standard health checks, for example to fail away from an endpoint if its public web page is unavailable or internal metrics show the server is unhealthy.
  scope: calculated health checks.
  link: [calculated health check feature](../facts/route53.md#route53-faq-calculated-health-check-combines-results)
route53-faq-changes-complete-entirely-or-not
  claim: Amazon Route 53 changes to record sets are transactional: a change completes entirely on any individual DNS server, or not at all.
  scope: per DNS server.
  link: [complete entirely on any individual DNS server](../facts/route53.md#route53-faq-changes-complete-entirely-or-not)
route53-faq-cloudfront-ip-addresses-vary-by-location
  claim: IP addresses of Amazon CloudFront endpoints vary based on your end user's location and can change at any time. An Alias record lets you map your zone apex (example.com) to your CloudFront distribution, and Route 53 responds to each request for the Alias record with the IP addresses for the distribution.
  scope: CloudFront distributions.
  link: [vary based on your end user’s location](../facts/route53.md#route53-faq-cloudfront-ip-addresses-vary-by-location)
route53-faq-cloudtrail-records-api-calls-not-for-rollback
  claim: CloudTrail records the API call history for Route 53, but AWS recommends not using CloudTrail logs to roll back hosted zone changes because the reconstructed history may be incomplete.
  scope: hosted zone change history.
  link: [may be incomplete](../facts/route53.md#route53-faq-cloudtrail-records-api-calls-not-for-rollback)
route53-faq-conditional-forwarding-rules-definition
  claim: Conditional forwarding rules let VPC Resolver forward queries for specified domains to a target IP address you choose, typically an on-premises DNS resolver; rules apply at the VPC level and can be shared across accounts.
  scope: Resolver rules.
  link: [applied at the VPC level](../facts/route53.md#route53-faq-conditional-forwarding-rules-definition)
route53-faq-dns-failover-two-components
  claim: DNS Failover consists of two components: health checks and failover.
  scope: DNS Failover.
  link: [health checks and failover](../facts/route53.md#route53-faq-dns-failover-two-components)
route53-faq-dns-firewall-block-and-allow-domains
  claim: Amazon Route 53 Resolver DNS Firewall lets you quickly deploy DNS protections across all your VPCs, blocking queries for known malicious domains (denylists) and allowing queries for trusted domains (allowlists) when you use the Route 53 Resolver for recursive DNS resolution.
  scope: VPCs that use the Route 53 Resolver.
  link: [block queries made for known malicious domains](../facts/route53.md#route53-faq-dns-firewall-block-and-allow-domains)
route53-faq-dns-firewall-controls-amazon-provided-dns
  claim: DNS Firewall complements other AWS network and application security services by giving control and visibility over Route 53 Resolver DNS traffic (such as AmazonProvidedDNS) for the entire VPC.
  scope: per VPC.
  link: [Route 53 Resolver DNS traffic](../facts/route53.md#route53-faq-dns-firewall-controls-amazon-provided-dns)
route53-faq-dns-firewall-denylist-approach
  claim: If your organization prefers to allow all outbound DNS lookups by default and only needs to block known malicious domains, you can use DNS Firewall to create denylists of the malicious domain names you know.
  scope: DNS Firewall rules.
  link: [create denylists](../facts/route53.md#route53-faq-dns-firewall-denylist-approach)
route53-faq-dns-firewall-logs-to-s3-cloudwatch
  claim: You can log DNS Firewall activity to an Amazon S3 bucket or CloudWatch log groups, and use Amazon Kinesis Firehose to send logs to a third-party provider.
  scope: DNS Firewall.
  link: [Amazon S3 bucket or Amazon CloudWatch log groups](../facts/route53.md#route53-faq-dns-firewall-logs-to-s3-cloudwatch)
route53-faq-dns-firewall-managed-domain-lists
  claim: DNS Firewall comes with AWS Managed Domain Lists that help protect against suspicious domains and Command-and-Control (C&C) bots.
  scope: DNS Firewall.
  link: [AWS Managed Domain Lists](../facts/route53.md#route53-faq-dns-firewall-managed-domain-lists)
route53-faq-dns-firewall-pricing-dimensions
  claim: DNS Firewall pricing is based on the number of domain names stored in the firewall and the number of DNS queries inspected.
  scope: DNS Firewall.
  link: [number of domain names stored within your firewall](../facts/route53.md#route53-faq-dns-firewall-pricing-dimensions)
route53-faq-dns-firewall-regional-firewall-manager
  claim: DNS Firewall is a regional feature; for policy and governance across multiple AWS accounts you should use AWS Firewall Manager.
  scope: DNS Firewall.
  link: [regional feature](../facts/route53.md#route53-faq-dns-firewall-regional-firewall-manager)
route53-faq-dns-firewall-vs-network-firewall
  claim: DNS Firewall and AWS Network Firewall both protect against outbound DNS query threats but for different deployment models: DNS Firewall when you use Amazon Route 53 Resolver for DNS resolution, Network Firewall when you use an external DNS service.
  scope: DNS Firewall versus Network Firewall.
  link: [for different deployment models](../facts/route53.md#route53-faq-dns-firewall-vs-network-firewall)
route53-faq-dns-firewall-walled-garden
  claim: With strict DNS exfiltration requirements you can create DNS Firewall rules that deny all outbound DNS queries for domains that are not on your approved lists, a walled-garden approach to DNS security.
  scope: DNS Firewall rules.
  link: [walled-garden](../facts/route53.md#route53-faq-dns-firewall-walled-garden)
route53-faq-dns-firewall-works-with-firewall-manager
  claim: DNS Firewall works together with AWS Firewall Manager, so you can build policies based on DNS Firewall rules and apply them centrally across your VPCs and accounts.
  scope: DNS Firewall.
  link: [AWS Firewall Manager](../facts/route53.md#route53-faq-dns-firewall-works-with-firewall-manager)
route53-faq-dns-translates-names-to-ip-addresses
  claim: DNS is a globally distributed service that translates human readable names into the numeric IP addresses that computers use to connect to each other.
  scope: DNS concept.
  link: [globally distributed service](../facts/route53.md#route53-faq-dns-translates-names-to-ip-addresses)
route53-faq-dnssec-signing-public-zones
  claim: You can enable DNSSEC signing for existing and new public hosted zones, DNSSEC validation for Amazon Route 53 Resolver, and DNSSEC on domain registration.
  scope: public hosted zones, Resolver and domain registration.
  link: [signing for existing and new public hosted zones](../facts/route53.md#route53-faq-dnssec-signing-public-zones)
route53-faq-domain-delegation-set-four-name-servers
  claim: When a domain is created it is automatically associated with four unique Amazon Route 53 name servers, known as a delegation set, and by default each hosted zone gets a new, unique delegation set.
  scope: per domain, per hosted zone; default.
  link: [four unique Route 53 name servers](../facts/route53.md#route53-faq-domain-delegation-set-four-name-servers)
route53-faq-domain-registration-auto-creates-hosted-zone
  claim: When you register a new domain name with Route 53, Route 53 automatically creates a hosted zone that stores the DNS records for the domain.
  scope: domains registered with Route 53.
  link: [automatically creates a hosted zone](../facts/route53.md#route53-faq-domain-registration-auto-creates-hosted-zone)
route53-faq-domain-registration-creates-hosted-zone-and-charges
  claim: When you register a domain with Route 53, it creates a hosted zone for the domain. You are charged for that hosted zone and for the DNS queries against it that Route 53 serves; you can delete the hosted zone to stop these charges, but some TLDs require valid name servers, so for those you first get DNS service from another provider.
  scope: domains registered with Route 53; some TLDs require valid name servers, so keep DNS service elsewhere before deleting the zone.
  link: [charged for the hosted zone](../facts/route53.md#route53-faq-domain-registration-creates-hosted-zone-and-charges)
route53-faq-domain-registration-period-and-auto-renew
  claim: The initial registration period is typically one year, and a domain registered or transferred to Amazon Route 53 is configured to renew automatically.
  scope: per domain registration; default; not adjustable; registries for some TLDs have longer registration periods.
  link: [typically one year](../facts/route53.md#route53-faq-domain-registration-period-and-auto-renew)
route53-faq-domain-transfer-in-prerequisites
  claim: Before you start a domain transfer to Amazon Route 53, the domain must be unlocked at your current registrar, privacy protection must be disabled if it applies, and you must have the valid authorization code from your current registrar.
  scope: domain transfer to Route 53.
  link: [valid Authorization Code, or “authcode”](../facts/route53.md#route53-faq-domain-transfer-in-prerequisites)
route53-faq-domains-per-account-limit-20
  claim: The FAQ states that each new Amazon Route 53 account is limited to a maximum of 20 domains.
  scope: per new account; maximum; not adjustable; FAQ figure for new accounts; compare with the quotas page for the adjustable value.
  link: [20 domains](../facts/route53.md#route53-faq-domains-per-account-limit-20)
  say: twenty domains
route53-faq-elb-failover-alias-evaluate-target-health
  claim: To enable DNS failover for an ELB endpoint, create an alias record that points to the ELB and set Evaluate Target Health to true.
  scope: alias records to ELB.
  link: [“Evaluate Target Health” parameter to true](../facts/route53.md#route53-faq-elb-failover-alias-evaluate-target-health)
route53-faq-elb-failover-no-route53-health-check-metrics
  claim: When failover for ELB endpoints relies on Evaluate Target Health instead of your own health checks, Amazon Route 53 generates no specific CloudWatch metrics for those endpoints; Elastic Load Balancing publishes metrics that show the health of the load balancer and the number of healthy instances behind it.
  scope: alias records to ELB with Evaluate Target Health.
  link: [there are no specific CloudWatch metrics generated](../facts/route53.md#route53-faq-elb-failover-no-route53-health-check-metrics)
route53-faq-elb-health-checks-managed-automatically
  claim: For an ELB alias with Evaluate Target Health, Amazon Route 53 creates and manages the health checks automatically, so you do not need your own health check, and the ELB health check inherits the health of the backend instances.
  scope: alias records to ELB with Evaluate Target Health.
  link: [You do not need to create your own Route 53 health check of the ELB](../facts/route53.md#route53-faq-elb-health-checks-managed-automatically)
route53-faq-external-registrar-must-update-name-servers
  claim: If your domain name is not managed by Amazon Route 53, you must tell the registrar to update the domain's name servers to the ones associated with your hosted zone.
  scope: domains registered outside Route 53.
  link: [update the name servers for your domain](../facts/route53.md#route53-faq-external-registrar-must-update-name-servers)
route53-faq-failback-automatic-after-threshold
  claim: When a failed endpoint passes the configured number of consecutive observations (default three), Route 53 restores its DNS records automatically and traffic resumes with no action required.
  scope: per health check; default threshold is three observations.
  link: [no action required on your part](../facts/route53.md#route53-faq-failback-automatic-after-threshold)
route53-faq-failover-backup-site-s3
  claim: You can use DNS failover to keep a backup site, for example a static site on an Amazon S3 website bucket, and fail over to it when the primary site becomes unreachable.
  scope: DNS Failover.
  link: [maintain a backup site](../facts/route53.md#route53-faq-failover-backup-site-s3)
route53-faq-failover-endpoint-outside-aws
  claim: You can set up health checks for parts of an application running outside AWS and fail over to any endpoint you choose, regardless of location, for example from an on-premises legacy application to a backup instance in AWS.
  scope: DNS Failover.
  link: [regardless of location](../facts/route53.md#route53-faq-failover-endpoint-outside-aws)
route53-faq-failover-ignores-endpoint-load
  claim: Amazon Route 53 does not make routing decisions based on the load or available capacity of your endpoints, so you must make sure the other endpoints have capacity or can scale to take the traffic of a failed endpoint.
  scope: DNS Failover.
  link: [does not make routing decisions](../facts/route53.md#route53-faq-failover-ignores-endpoint-load)
route53-faq-failover-returns-only-healthy-answers
  claim: With DNS failover, Amazon Route 53 returns answers only for resources that are healthy and reachable from the outside world, so end users are routed away from a failed or unhealthy part of the application.
  scope: DNS Failover.
  link: [only returns answers for resources that are healthy](../facts/route53.md#route53-faq-failover-returns-only-healthy-answers)
route53-faq-failover-step-disables-records
  claim: When a health check fails and failover occurs, Route 53 disables the resource records for the failed endpoint and no longer serves them; this failover step causes traffic to be routed to the healthy endpoints instead.
  scope: DNS Failover; in the FAQ example, after the application fails three consecutive health checks.
  link: [disables the resource records for the failed endpoint](../facts/route53.md#route53-faq-failover-step-disables-records)
route53-faq-failover-ttl-60-seconds-or-less
  claim: The FAQ recommends a TTL of 60 seconds or less when using DNS failover, to shorten the time before traffic stops going to a failed endpoint.
  scope: records used with DNS Failover; maximum; recommendation.
  link: [TTL of 60 seconds or less](../facts/route53.md#route53-faq-failover-ttl-60-seconds-or-less)
  say: sixty seconds or less
route53-faq-failover-without-lbr-simple-primary-backup
  claim: DNS failover can be used without Latency Based Routing, for example in a simple scenario where Amazon Route 53 monitors the primary website and fails over to a backup site when the primary is unavailable.
  scope: DNS Failover.
  link: [simple failover scenario](../facts/route53.md#route53-faq-failover-without-lbr-simple-primary-backup)
route53-faq-four-name-servers-four-tlds
  claim: When you create a hosted zone you receive four Route 53 name servers across four different top-level domains, to help ensure a high level of availability.
  scope: per hosted zone; fixed; on creation of the hosted zone.
  link: [four Route 53 name servers](../facts/route53.md#route53-faq-four-name-servers-four-tlds)
  link: [four different Top-Level Domains](../facts/route53.md#route53-faq-four-name-servers-four-tlds)
  say: four Route 53 name servers
route53-faq-gandi-verify-contact-15-days
  claim: If Gandi is the registrar of record, you must verify your contact information when asked within the first 15 days of registration, or the domain name can be suspended.
  scope: domains registered through Gandi; maximum; only if Gandi requests the verification.
  link: [first 15 days of registration](../facts/route53.md#route53-faq-gandi-verify-contact-15-days)
  say: fifteen days
route53-faq-geo-dns-combines-with-latency-and-failover
  claim: You can combine Geo DNS with other routing types, such as Latency Based Routing and DNS Failover, to build low-latency and fault-tolerant architectures.
  scope: routing policies.
  link: [combine Geo DNS with other routing types](../facts/route53.md#route53-faq-geo-dns-combines-with-latency-and-failover)
route53-faq-geo-dns-consistent-endpoint
  claim: Geo DNS balances load across endpoints in a predictable way, so each end-user location is consistently routed to the same endpoint.
  scope: geolocation records.
  link: [consistently routed to the same endpoint](../facts/route53.md#route53-faq-geo-dns-consistent-endpoint)
route53-faq-geo-dns-global-record-recommended
  claim: AWS strongly recommends a global (default) Geo DNS record so Route 53 can answer queries from all possible locations; it is returned when the IP address is not in the Geo IP database or the location matches no specific record.
  scope: geolocation records.
  link: [strongly recommend that you configure a global record](../facts/route53.md#route53-faq-geo-dns-global-record-recommended)
route53-faq-geo-dns-localize-or-restrict-content
  claim: Geo DNS makes it possible to customize localized content, such as presenting detail pages in the right language, or to restrict distribution of content to only the markets you have licensed.
  scope: geolocation records.
  link: [restricting distribution of content to only the markets](../facts/route53.md#route53-faq-geo-dns-localize-or-restrict-content)
route53-faq-geo-dns-most-specific-record-wins
  claim: Geo DNS records can overlap, and Route 53 returns the most specific one: state first, then country, then continent, and finally the global record.
  scope: geolocation records.
  link: [most specific Geo DNS record](../facts/route53.md#route53-faq-geo-dns-most-specific-record-wins)
route53-faq-geo-dns-routes-by-location
  claim: Geolocation (Geo DNS) routing directs requests to specific endpoints based on the geographic location from which the request originates.
  scope: geolocation records.
  link: [geographic location from which the request originates](../facts/route53.md#route53-faq-geo-dns-routes-by-location)
route53-faq-geo-dns-three-levels-and-global
  claim: Geo DNS provides three levels of geographic granularity (continent, country and state) and a global record that is served when a user's location matches none of the specific records.
  scope: geolocation records; fixed.
  link: [three levels of geographic granularity](../facts/route53.md#route53-faq-geo-dns-three-levels-and-global)
  say: three levels of geographic granularity
route53-faq-geo-vs-latency-geography-not-latency
  claim: Geo DNS bases routing decisions on the geographic location of the requests, and in some cases geography is a good proxy for latency but in others it is not.
  scope: latency versus geolocation routing.
  link: [geographic location of the requests](../facts/route53.md#route53-faq-geo-vs-latency-geography-not-latency)
route53-faq-geoproximity-bias-expands-or-shrinks
  claim: Changing the geoproximity bias value on an endpoint expands or shrinks the area from which traffic is routed to that resource, but bias cannot accurately predict the load factor.
  scope: geoproximity bias.
  link: [expands or shrinks the area](../facts/route53.md#route53-faq-geoproximity-bias-expands-or-shrinks)
route53-faq-geoproximity-region-or-lat-long
  claim: When you create a traffic flow policy, you can specify either an AWS Region (if you use AWS resources) or the latitude and longitude for each endpoint. In the FAQ example, geoproximity routing sends the DNS query of a user in Seattle to EC2 instances in US West (Oregon) rather than US East (Ohio), because Oregon is closer geographically.
  scope: Traffic Flow geoproximity rules.
  link: [latitude and longitude for each endpoint](../facts/route53.md#route53-faq-geoproximity-region-or-lat-long)
route53-faq-global-anycast-low-latency
  claim: Using a global anycast network of DNS servers, Route 53 is designed to answer queries automatically from the optimal location depending on network conditions, which gives low query latency.
  scope: Route 53 DNS service.
  link: [global anycast network of DNS servers](../facts/route53.md#route53-faq-global-anycast-low-latency)
route53-faq-health-check-cloudwatch-metrics-free
  claim: CloudWatch metrics for Route 53 health checks are available free of charge.
  scope: CloudWatch metrics of health checks.
  link: [available free of charge](../facts/route53.md#route53-faq-health-check-cloudwatch-metrics-free)
route53-faq-health-check-does-not-follow-redirects
  claim: Health checks do not follow HTTP redirects: they treat an HTTP 3xx code as a successful response.
  scope: HTTP and HTTPS health checks.
  link: [HTTP 3xx code to be a successful response](../facts/route53.md#route53-faq-health-check-does-not-follow-redirects)
route53-faq-health-check-domain-name-uses-ipv4
  claim: If a health check endpoint is given as a domain name, Amazon Route 53 looks up its IPv4 address and connects over IPv4; to check over IPv6, use the IP address endpoint type with the IPv6 address.
  scope: health checks with a domain name endpoint.
  link: [connect to the endpoint using IPv4](../facts/route53.md#route53-faq-health-check-domain-name-uses-ipv4)
route53-faq-health-check-failure-threshold-default-3
  claim: By default an endpoint is considered failed after three consecutive failed health check observations, and Route 53 resumes sending traffic after it passes three consecutive observations.
  scope: per health check; default; adjustable; the threshold can be changed.
  link: [threshold of three health check observations](../facts/route53.md#route53-faq-health-check-failure-threshold-default-3)
  say: three consecutive observations
route53-faq-health-check-failure-threshold-range-1-to-10
  claim: You can change the health check failure threshold to any value between 1 and 10 observations.
  scope: per health check; maximum; adjustable; settable per health check.
  link: [between 1 and 10 observations](../facts/route53.md#route53-faq-health-check-failure-threshold-range-1-to-10)
  say: one to ten observations
route53-faq-health-check-fast-interval-10-seconds
  claim: You can optionally select a fast interval of 10 seconds between health check observations, which means three times more checks and three times the requests to your endpoint.
  scope: per health check; minimum; optional; priced separately.
  link: [fast interval of 10 seconds](../facts/route53.md#route53-faq-health-check-fast-interval-10-seconds)
  say: ten seconds
route53-faq-health-check-interval-default-30-seconds
  claim: By default, health check observations are conducted at an interval of 30 seconds.
  scope: per health check; default; adjustable; a fast interval can be selected.
  link: [interval of 30 seconds](../facts/route53.md#route53-faq-health-check-interval-default-30-seconds)
  say: thirty seconds
route53-faq-health-check-latency-measurement-optional
  claim: Health checks include an optional latency measurement feature that shows how long an endpoint takes to respond, and it produces a separate set of latency metrics for each AWS Region where checks are made.
  scope: health checks.
  link: [optional latency measurement feature](../facts/route53.md#route53-faq-health-check-latency-measurement-optional)
route53-faq-health-check-load-per-endpoint
  claim: Each health check runs from multiple locations around the world, and an endpoint should expect about one request every 2-3 seconds for standard interval checks and one or more per second for fast-interval checks.
  scope: per endpoint, on average; based on the current default number of health checking locations.
  link: [one request every 2-3 seconds](../facts/route53.md#route53-faq-health-check-load-per-endpoint)
route53-faq-health-check-protocols-https-http-tcp
  claim: Amazon Route 53 supports health checks over HTTPS, HTTP or TCP.
  scope: health checks.
  link: [HTTPS, HTTP or TCP](../facts/route53.md#route53-faq-health-check-protocols-https-http-tcp)
route53-faq-health-check-record-types-except-soa
  claim: The FAQ says a health check can be associated with any record type supported by Amazon Route 53 except SOA and "DNS" records, as it prints it.
  scope: health check association; FAQ wording; the second excluded type is printed as DNS records.
  link: [except SOA and DNS records](../facts/route53.md#route53-faq-health-check-record-types-except-soa)
route53-faq-health-check-results-in-cloudwatch
  claim: Each health check's results are published as Amazon CloudWatch metrics, and you can create CloudWatch alarms on the metric to send notifications when the health status changes.
  scope: health checks.
  link: [published as Amazon CloudWatch metrics](../facts/route53.md#route53-faq-health-check-results-in-cloudwatch)
route53-faq-health-check-status-console-and-api
  claim: You can view the current status of a health check and details on why it failed in the Amazon Route 53 console and through the API.
  scope: health checks.
  link: [console and via the Route 53 API](../facts/route53.md#route53-faq-health-check-status-console-and-api)
route53-faq-health-check-without-ip-elb-s3-automatic
  claim: For ELB and S3 website endpoints, Amazon Route 53 creates and manages the health checks automatically when you create an alias record with Evaluate Target Health enabled; for all other endpoints you give the DNS name or the IP address in the health check.
  scope: health check endpoints.
  link: [DNS name (e.g. www.example.com) or the IP address](../facts/route53.md#route53-faq-health-check-without-ip-elb-s3-automatic)
route53-faq-health-checks-are-automated-requests
  claim: Health checks are automated requests sent over the internet to your application to verify that it is reachable, available and functional; you can make them similar to the requests your users make, such as requesting a web page from a specific URL.
  scope: health checks.
  link: [reachable, available, and functional](../facts/route53.md#route53-faq-health-checks-are-automated-requests)
route53-faq-hosted-zone-12-hour-grace-period
  claim: If you delete a hosted zone within 12 hours after you create it, you are not charged for it; after the grace period the standard monthly fee applies immediately.
  scope: per hosted zone; fixed; zone deleted within 12 hours of creation.
  link: [grace period of 12 hours](../facts/route53.md#route53-faq-hosted-zone-12-hour-grace-period)
  say: twelve hours
route53-faq-hosted-zone-billed-at-creation-and-monthly
  claim: A hosted zone is billed once when it is created and then on the first day of each month.
  scope: per hosted zone.
  link: [first day of each month](../facts/route53.md#route53-faq-hosted-zone-billed-at-creation-and-monthly)
route53-faq-hosted-zone-is-route53-concept
  claim: A domain is a general DNS concept, while a hosted zone is an Amazon Route 53 concept.
  scope: Route 53 DNS.
  link: [hosted zone is an Amazon Route 53 concept](../facts/route53.md#route53-faq-hosted-zone-is-route53-concept)
route53-faq-hosted-zone-like-zone-file
  claim: A hosted zone is like a traditional DNS zone file: a collection of records that are managed together and belong to one parent domain name.
  scope: per hosted zone.
  link: [collection of records](../facts/route53.md#route53-faq-hosted-zone-like-zone-file)
route53-faq-https-health-check-no-certificate-validation
  claim: HTTPS health checks test whether a connection over SSL is possible and whether the endpoint returns a valid HTTP response code, but they do not validate the SSL certificate.
  scope: HTTPS health checks.
  link: [do not validate the SSL certificate](../facts/route53.md#route53-faq-https-health-check-no-certificate-validation)
route53-faq-https-health-check-supports-sni
  claim: HTTPS health checks support Server Name Indication (SNI).
  scope: HTTPS health checks.
  link: [HTTPS health checks support SNI](../facts/route53.md#route53-faq-https-health-check-supports-sni)
route53-faq-hz-own-virtual-name-servers
  claim: Each Amazon Route 53 hosted zone is served by its own set of virtual DNS servers, and the system assigns the DNS server names when the hosted zone is created.
  scope: per hosted zone.
  link: [its own set of virtual DNS servers](../facts/route53.md#route53-faq-hz-own-virtual-name-servers)
route53-faq-iam-controls-zone-and-record-access
  claim: You can control management access to a hosted zone and to individual resource record sets by using IAM.
  scope: hosted zones and record sets.
  link: [individual resource record sets](../facts/route53.md#route53-faq-iam-controls-zone-and-record-access)
route53-faq-insync-means-all-servers
  claim: When the status of a change is INSYNC, the change has been performed on all of the Route 53 DNS servers.
  scope: ChangeResourceRecordSets calls.
  link: [INSYNC](../facts/route53.md#route53-faq-insync-means-all-servers)
route53-faq-ipv6-aaaa-ptr-and-service-over-ipv6
  claim: Amazon Route 53 supports forward (AAAA) and reverse (PTR) IPv6 records, the service itself is available over IPv6, and health checks can monitor endpoints over IPv6.
  scope: Route 53 DNS and health checks.
  link: [forward (AAAA) and reverse (PTR) IPv6 records](../facts/route53.md#route53-faq-ipv6-aaaa-ptr-and-service-over-ipv6)
route53-faq-lbr-for-latency-geo-for-compliance
  claim: To minimize end-user latency the FAQ recommends Latency Based Routing; for compliance, localization or other cases that need stable routing from a geography to an endpoint, it recommends Geo DNS.
  scope: latency versus geolocation routing.
  link: [we recommend using Latency Based Routing](../facts/route53.md#route53-faq-lbr-for-latency-geo-for-compliance)
  link: [we recommend using Geo DNS](../facts/route53.md#route53-faq-lbr-for-latency-geo-for-compliance)
route53-faq-lbr-geo-no-extra-fee-pay-queries
  claim: There are no upfront fees or long term commitments to use Amazon Route 53 and Latency Based Routing (LBR); customers pay for the hosted zones and queries they actually use.
  scope: Latency Based Routing (LBR); see the pricing page for the per-query price of these routing types.
  link: [no upfront fees or long term commitments](../facts/route53.md#route53-faq-lbr-geo-no-extra-fee-pay-queries)
route53-faq-lbr-lowest-latency-region
  claim: Latency Based Routing lets you run applications in multiple AWS Regions, and Amazon Route 53 routes end users to the AWS Region that provides the lowest latency.
  scope: latency records.
  link: [region that provides the lowest latency](../facts/route53.md#route53-faq-lbr-lowest-latency-region)
route53-faq-lbr-uses-latency-measurements
  claim: Latency Based Routing uses latency measurements between viewer networks and AWS data centers to decide which endpoint to direct users to.
  scope: latency records.
  link: [latency measurements between viewer networks and AWS datacenters](../facts/route53.md#route53-faq-lbr-uses-latency-measurements)
route53-faq-limit-hosted-zones-per-account
  claim: The FAQ states that each Amazon Route 53 account is limited to a maximum of 500 hosted zones, and that a higher limit can be requested.
  scope: per account; maximum; adjustable; a higher limit can be requested.
  link: [500 hosted zones](../facts/route53.md#route53-faq-limit-hosted-zones-per-account)
  say: five hundred hosted zones
route53-faq-limit-records-per-hosted-zone
  claim: The FAQ states that each hosted zone is limited to a maximum of 10,000 resource record sets, and that a higher limit can be requested.
  scope: per hosted zone; maximum; adjustable; a higher limit can be requested.
  link: [10,000 resource record sets](../facts/route53.md#route53-faq-limit-records-per-hosted-zone)
  say: ten thousand resource record sets
route53-faq-manage-private-ips-with-private-dns
  claim: You can manage private IP addresses within VPCs by using the Private DNS feature of Amazon Route 53.
  scope: private hosted zones.
  link: [manage private IP addresses within Virtual Private Clouds](../facts/route53.md#route53-faq-manage-private-ips-with-private-dns)
route53-faq-metric-based-health-check-uses-cloudwatch-alarm
  claim: Metric based health checks let you do DNS failover on any CloudWatch metric, including custom metrics, and the health check becomes unhealthy whenever its CloudWatch metric enters an alarm state.
  scope: metric based health checks.
  link: [any metric that is available within Amazon CloudWatch](../facts/route53.md#route53-faq-metric-based-health-check-uses-cloudwatch-alarm)
route53-faq-multiple-hz-different-answers
  claim: Because each hosted zone has its own virtual set of name servers, Route 53 answers queries for the same domain differently depending on which name server receives the query.
  scope: hosted zones for the same domain.
  link: [depending on which name server you send](../facts/route53.md#route53-faq-multiple-hz-different-answers)
route53-faq-multiple-hz-same-domain
  claim: You can create multiple hosted zones for the same domain name, for example a test version and a production version, to verify DNS settings before copying them to production.
  scope: per domain name.
  link: [multiple hosted zones](../facts/route53.md#route53-faq-multiple-hz-same-domain)
route53-faq-multivalue-not-a-load-balancer-substitute
  claim: Returning multiple health-checkable IP addresses is not a substitute for a load balancer, but it is a way to use DNS to improve availability and load balancing.
  scope: multivalue answer records.
  link: [not a substitute for a load balancer](../facts/route53.md#route53-faq-multivalue-not-a-load-balancer-substitute)
route53-faq-multivalue-one-record-per-resource
  claim: To route traffic randomly to multiple resources, create one multivalue answer record for each resource and optionally associate an Amazon Route 53 health check with each record.
  scope: multivalue answer records.
  link: [one multivalue answer record for each resource](../facts/route53.md#route53-faq-multivalue-one-record-per-resource)
route53-faq-multivalue-up-to-eight-healthy
  claim: Amazon Route 53 supports up to eight healthy records in response to each DNS query for multivalue answer routing.
  scope: per DNS query response; maximum; not adjustable; multivalue answer records.
  link: [up to eight healthy records](../facts/route53.md#route53-faq-multivalue-up-to-eight-healthy)
  say: up to eight healthy records
route53-faq-no-default-ttl
  claim: Amazon Route 53 has no default TTL for any record type, so you must always specify a TTL for each record.
  scope: every record type; default; not adjustable; a TTL must be set on each record.
  link: [does not have a default TTL](../facts/route53.md#route53-faq-no-default-ttl)
route53-faq-no-website-hosting
  claim: Amazon Route 53 does not provide website hosting because it is an authoritative DNS service; a static website can be hosted on Amazon S3.
  scope: Route 53 service.
  link: [does not provide website hosting](../facts/route53.md#route53-faq-no-website-hosting)
route53-faq-phz-across-regions-needs-connectivity
  claim: Private DNS answers are available in every VPC associated with the private hosted zone, but VPCs in different Regions need connectivity with each other for resources to reach one another.
  scope: private hosted zones; connectivity between the VPCs is a separate requirement.
  link: [every VPC that you associate](../facts/route53.md#route53-faq-phz-across-regions-needs-connectivity)
route53-faq-phz-cross-account-vpcs
  claim: You can associate VPCs that belong to different AWS accounts with a single private hosted zone.
  scope: private hosted zones.
  link: [VPCs belonging to different accounts](../facts/route53.md#route53-faq-phz-cross-account-vpcs)
route53-faq-phz-failover-metric-based-health-checks
  claim: DNS failover works for private hosted zones; endpoints with only private IP addresses cannot use standard health checks, but can use metric based health checks that read a CloudWatch metric.
  scope: private hosted zones; endpoints with only private IP addresses.
  link: [metric based health checks](../facts/route53.md#route53-faq-phz-failover-metric-based-health-checks)
route53-faq-phz-multiple-vpcs
  claim: You can associate multiple VPCs with a single private hosted zone.
  scope: private hosted zones.
  link: [associate multiple VPCs with a single hosted zone](../facts/route53.md#route53-faq-phz-multiple-vpcs)
route53-faq-pricing-dimensions-and-no-minimums
  claim: Amazon Route 53 charges are based on actual usage for hosted zones, queries, health checks and domain names, with no minimum fees, no minimum usage commitments and no overage charges.
  scope: Route 53 pricing.
  link: [Hosted Zones, Queries, Health Checks, and Domain Names](../facts/route53.md#route53-faq-pricing-dimensions-and-no-minimums)
route53-faq-privacy-protection-no-additional-charge
  claim: Amazon Route 53 provides privacy protection for registered domains at no additional charge; it hides your phone number, email address and physical address.
  scope: registered domains; first and last name are hidden if the TLD registry and registrar allow it.
  link: [privacy protection at no additional charge](../facts/route53.md#route53-faq-privacy-protection-no-additional-charge)
route53-faq-private-dns-no-internet-exposure
  claim: Private DNS gives you authoritative DNS within your VPCs without exposing your DNS records, including resource names and IP addresses, to the internet.
  scope: private hosted zones.
  link: [authoritative DNS within your VPCs](../facts/route53.md#route53-faq-private-dns-no-internet-exposure)
route53-faq-private-dns-requires-vpc
  claim: To use Route 53 Private DNS you must configure a VPC and migrate your resources into it, because Private DNS uses a VPC to manage visibility and provide DNS resolution for private hosted zones.
  scope: private hosted zones.
  link: [uses VPC to manage visibility](../facts/route53.md#route53-faq-private-dns-requires-vpc)
route53-faq-private-dns-resolves-without-internet
  claim: Resources in a VPC that have no internet connectivity can still resolve internal DNS names from a private hosted zone.
  scope: resolution inside a VPC.
  link: [do not have Internet connectivity](../facts/route53.md#route53-faq-private-dns-resolves-without-internet)
route53-faq-private-dns-setup-steps
  claim: To set up Private DNS, create a hosted zone, choose the option to make it private, and associate it with one of your VPCs; afterwards you can associate it with additional VPCs.
  scope: private hosted zones.
  link: [hosted zone with one of your VPCs](../facts/route53.md#route53-faq-private-dns-setup-steps)
route53-faq-private-zone-answers-only-from-associated-vpcs
  claim: A private hosted zone returns its records only when queried from within the VPCs that are associated with it.
  scope: private hosted zones.
  link: [only return these records when queried from within](../facts/route53.md#route53-faq-private-zone-answers-only-from-associated-vpcs)
route53-faq-private-zone-block-domains-trick
  claim: You can block domains and specific DNS names by creating those names in one or more private hosted zones and pointing them to your own server or another location you manage.
  scope: private hosted zones.
  link: [block domains and specific DNS names](../facts/route53.md#route53-faq-private-zone-block-domains-trick)
route53-faq-profiles-integrated-with-ram
  claim: Route 53 Profiles integrate natively with AWS RAM, so you can share Profiles across accounts or with an AWS Organization, and RAM managed permissions let you attach different permissions to each resource.
  scope: Route 53 Profiles.
  link: [natively integrates with AWS RAM](../facts/route53.md#route53-faq-profiles-integrated-with-ram)
route53-faq-profiles-manage-what
  claim: Route 53 Profiles support private hosted zones and their settings, Route 53 Resolver rules (forwarding and system), and DNS Firewall rule groups.
  scope: Route 53 Profiles.
  link: [private hosted zones and the settings specified within](../facts/route53.md#route53-faq-profiles-manage-what)
route53-faq-profiles-not-shared-across-regions
  claim: You cannot share an Amazon Route 53 Profile across AWS Regions.
  scope: Route 53 Profiles.
  link: [cannot share a Profile across AWS Regions](../facts/route53.md#route53-faq-profiles-not-shared-across-regions)
route53-faq-profiles-one-per-vpc-at-a-time
  claim: You can create one or more Profiles per account, but you can associate only one Profile per VPC at a time.
  scope: per VPC; maximum.
  link: [only associate one Profile per VPC](../facts/route53.md#route53-faq-profiles-one-per-vpc-at-a-time)
route53-faq-profiles-share-dns-config
  claim: Route 53 Profiles let you combine private hosted zone associations, Resolver rules and DNS Firewall rule groups in one RAM-shareable configuration that you can share across accounts and associate with VPCs.
  scope: Route 53 Profiles.
  link: [one RAM-shareable configuration](../facts/route53.md#route53-faq-profiles-share-dns-config)
route53-faq-profiles-up-to-5000-vpcs
  claim: You can associate up to 5,000 VPCs to a single Route 53 Profile.
  scope: per Route 53 Profile; maximum; not adjustable; FAQ figure; compare with the quotas page.
  link: [up to 5,000 VPCs](../facts/route53.md#route53-faq-profiles-up-to-5000-vpcs)
  say: up to five thousand VPCs
route53-faq-propagation-within-60-seconds
  claim: Amazon Route 53 is designed to propagate record updates to its world-wide authoritative DNS servers within 60 seconds under normal conditions.
  scope: Route 53 authoritative DNS servers; maximum; under normal conditions.
  link: [within 60 seconds](../facts/route53.md#route53-faq-propagation-within-60-seconds)
  say: within sixty seconds
route53-faq-query-logging-to-cloudwatch-logs
  claim: You can configure Amazon Route 53 to log information about the queries that it receives, including date-time stamp, domain name, query type and location; when you configure query logging, Amazon Route 53 starts to send the logs to CloudWatch Logs.
  scope: Route 53 query logging.
  link: [send logs to CloudWatch Logs](../facts/route53.md#route53-faq-query-logging-to-cloudwatch-logs)
route53-faq-recommend-alias-over-cname-cf-s3
  claim: For CloudFront distributions and S3 buckets configured as static websites, AWS recommends an alias record instead of a CNAME.
  scope: CloudFront distributions and S3 website buckets.
  link: [we recommend creating an ‘Alias’ record](../facts/route53.md#route53-faq-recommend-alias-over-cname-cf-s3)
route53-faq-record-names-must-end-with-zone-name
  claim: All record sets in a hosted zone must have the hosted zone's domain name as a suffix, so the amazon.com zone cannot hold a record named www.amazon.ca.
  scope: per hosted zone.
  link: [domain name as a suffix](../facts/route53.md#route53-faq-record-names-must-end-with-zone-name)
route53-faq-register-domains-console-or-api
  claim: You can register new domain names with Amazon Route 53 by using the console or the API, and you can also transfer in existing domain names from other registrars.
  scope: Route 53 domain registration.
  link: [register new domain names](../facts/route53.md#route53-faq-register-domains-console-or-api)
route53-faq-registrar-must-use-hosted-zone-name-servers
  claim: Make sure your domain name registrar uses the name servers of your Amazon Route 53 hosted zone; if not, Amazon Route 53 is not authoritative for queries to your domain.
  scope: domains registered elsewhere.
  link: [will not be authoritative for queries](../facts/route53.md#route53-faq-registrar-must-use-hosted-zone-name-servers)
route53-faq-resolver-caches-by-ttl-outside-control
  claim: Caching DNS resolvers are outside the control of Amazon Route 53 and cache record sets according to their TTL, so INSYNC or PENDING describes only the state of the Route 53 authoritative servers.
  scope: caching DNS resolvers.
  link: [according to their time to live (TTL)](../facts/route53.md#route53-faq-resolver-caches-by-ttl-outside-control)
route53-faq-resolver-endpoint-enis-in-vpc
  claim: A Resolver endpoint includes one or more elastic network interfaces (ENIs) in your VPC, each with an IP address from the VPC subnet, and that IP address can be a forwarding target for on-premises DNS servers.
  scope: Resolver endpoints.
  link: [one or more elastic network interfaces (ENI)](../facts/route53.md#route53-faq-resolver-endpoint-enis-in-vpc)
route53-faq-resolver-endpoints-required-both-directions
  claim: Resolver endpoints are required both for DNS query traffic forwarded from VPCs to your network and from your network to your VPCs over AWS Direct Connect and Managed VPN.
  scope: hybrid DNS over Direct Connect and VPN.
  link: [Endpoints are required both for DNS query traffic](../facts/route53.md#route53-faq-resolver-endpoints-required-both-directions)
route53-faq-resolver-rules-shared-with-ram
  claim: Resolver rules can be created in one primary account and shared across accounts with AWS Resource Access Manager (RAM), but once shared they still need to be applied to VPCs in those accounts to take effect.
  scope: Resolver rules.
  link: [shared across multiple accounts using RAM](../facts/route53.md#route53-faq-resolver-rules-shared-with-ram)
route53-faq-reusable-delegation-set
  claim: You can use the Route 53 API to create a reusable delegation set and apply it to multiple hosted zones, which lets you point your registrar at the same name servers for all your domains.
  scope: hosted zones in one account; created through the API.
  link: [reusable delegation set](../facts/route53.md#route53-faq-reusable-delegation-set)
route53-faq-route53-still-global-service
  claim: Regional support for VPC Resolver does not make all of Amazon Route 53 regional: public and private DNS, traffic flow, health checks and domain name registration are all global services.
  scope: Route 53 public and private DNS, traffic flow, health checks, domain registration; VPC Resolver is regional.
  link: [all global services](../facts/route53.md#route53-faq-route53-still-global-service)
route53-faq-routes-to-aws-and-non-aws-infrastructure
  claim: Amazon Route 53 connects user requests to infrastructure running in AWS, such as EC2 instances, load balancers or S3 buckets, and can also route users to infrastructure outside of AWS.
  scope: Route 53 service.
  link: [infrastructure outside of AWS](../facts/route53.md#route53-faq-routes-to-aws-and-non-aws-infrastructure)
route53-faq-s3-non-website-bucket-cname
  claim: For an S3 bucket that is not configured to host a static website, you can create a CNAME record for your domain and the S3 bucket name.
  scope: S3 buckets not configured as websites.
  link: [create a CNAME record](../facts/route53.md#route53-faq-s3-non-website-bucket-cname)
route53-faq-s3-website-target-health-checks-s3-service
  claim: For an alias record to an S3 website bucket with Evaluate Target Health, Amazon Route 53 checks the health of the Amazon S3 service in the Region, not whether a specific bucket exists or has valid content.
  scope: alias records to S3 website buckets.
  link: [health checks of the Amazon S3 service itself in each AWS region](../facts/route53.md#route53-faq-s3-website-target-health-checks-s3-service)
route53-faq-sla-hosted-zone-unavailable-definition
  claim: For the Amazon Route 53 SLA, a hosted zone is unavailable in a given minute only if all four virtual name servers assigned to it fail to respond to all DNS queries throughout that minute.
  scope: per hosted zone, per minute; Route 53 authoritative DNS SLA.
  link: [all four virtual name servers](../facts/route53.md#route53-faq-sla-hosted-zone-unavailable-definition)
route53-faq-sla-service-credit-both-services
  claim: Both the Amazon Route 53 authoritative service and the Amazon Route 53 Resolver Endpoints service offer a service credit if a customer's monthly uptime percentage falls below the service commitment in a billing cycle.
  scope: Route 53 authoritative service and Resolver Endpoints service; monthly uptime percentage below the service commitment.
  link: [service credit](../facts/route53.md#route53-faq-sla-service-credit-both-services)
route53-faq-stop-sharing-rules-disassociates-vpcs
  claim: If you stop sharing Resolver rules, the accounts can no longer use them, and rules that were associated with VPCs in those accounts are disassociated from those VPCs.
  scope: shared Resolver rules.
  link: [disassociated from those VPCs](../facts/route53.md#route53-faq-stop-sharing-rules-disassociates-vpcs)
route53-faq-string-match-avoid-redirect-target
  claim: For string matching health checks, avoid pointing the health check at a location that returns an HTTP redirect, because the check searches for the string in the body of the redirect and never reaches the target.
  scope: string matching health checks.
  link: [a location that returns an HTTP redirect](../facts/route53.md#route53-faq-string-match-avoid-redirect-target)
route53-faq-string-matching-option
  claim: You can use health checks to check for the presence of a designated string in a server response by selecting the Enable String Matching option.
  scope: health checks.
  link: [“Enable String Matching” option](../facts/route53.md#route53-faq-string-matching-option)
route53-faq-traffic-flow-billed-per-policy-record
  claim: Traffic Flow is billed per policy record, monthly and prorated for partial months; a traffic policy without a policy record is not charged.
  scope: per policy record; billing is monthly and prorated for partial months.
  link: [billed per policy record](../facts/route53.md#route53-faq-traffic-flow-billed-per-policy-record)
route53-faq-traffic-flow-supports-all-policies-plus-bias
  claim: Traffic Flow supports all Amazon Route 53 DNS routing policies and also supports geoproximity routing with traffic biasing.
  scope: Traffic Flow.
  link: [geoproximity based routing with traffic biasing](../facts/route53.md#route53-faq-traffic-flow-supports-all-policies-plus-bias)
route53-faq-traffic-flow-what-it-is
  claim: Traffic Flow is a global traffic management service that connects users to the best endpoint based on latency, geography and endpoint health, using a visual policy builder in the console.
  scope: Traffic Flow.
  link: [global traffic management service](../facts/route53.md#route53-faq-traffic-flow-what-it-is)
route53-faq-traffic-policy-reuse-cname-not-at-apex
  claim: One traffic policy can manage several DNS names through extra policy records (each billed) or through CNAME records that point at one policy record, but the CNAME method is not possible at the zone apex, where you must create a policy record.
  scope: Traffic Flow policy records; CNAME method.
  link: [not possible for records at the zone apex](../facts/route53.md#route53-faq-traffic-policy-reuse-cname-not-at-apex)
route53-faq-traffic-policy-vs-policy-record
  claim: A traffic policy is the set of rules that you define to route end users' requests to one of your application's endpoints; by itself it does not affect how end users are routed, because it is not yet associated with your application's DNS name.
  scope: Traffic Flow.
  link: [a traffic policy doesn't affect how end users](../facts/route53.md#route53-faq-traffic-policy-vs-policy-record)
route53-faq-transfer-no-disruption-copy-zone-first
  claim: To move a domain without disrupting traffic, first get the DNS record data (zone file) from the existing provider and create a hosted zone with those records, then update the name servers at the registrar; queries are answered by Route 53 once the new delegations propagate.
  scope: DNS migration to Route 53.
  link: [get a list of the DNS record data](../facts/route53.md#route53-faq-transfer-no-disruption-copy-zone-first)
route53-faq-vpc-resolver-doh-inbound-outbound
  claim: Amazon Route 53 VPC Resolver supports the DNS over HTTPS (DoH) protocol for both inbound and outbound Resolver endpoints.
  scope: Resolver endpoints; FAQ states no launch date.
  link: [DNS over HTTPS (DoH) protocol](../facts/route53.md#route53-faq-vpc-resolver-doh-inbound-outbound)
route53-faq-vpc-resolver-hybrid-forwarding-direct-connect-vpn
  claim: For hybrid cloud, you can configure conditional forwarding rules and Resolver endpoints to enable DNS resolution across AWS Direct Connect and AWS Managed VPN.
  scope: hybrid DNS.
  link: [conditional forwarding rules and Resolver endpoints](../facts/route53.md#route53-faq-vpc-resolver-hybrid-forwarding-direct-connect-vpn)
route53-faq-vpc-resolver-on-outposts-local-resolution
  claim: Route 53 VPC Resolver on Outposts resolves DNS queries locally on AWS Outposts racks, stores DNS responses there, and keeps DNS resolution going during network disconnects to the parent AWS Region.
  scope: AWS Outposts racks; when Route 53 VPC Resolver is enabled on Outposts.
  link: [even during unexpected network disconnects](../facts/route53.md#route53-faq-vpc-resolver-on-outposts-local-resolution)
route53-faq-vpc-resolver-regional-recursive-default
  claim: Route 53 VPC Resolver is a regional DNS service that gives recursive DNS lookups for names hosted in EC2 and public names on the internet, and it is available by default in every VPC.
  scope: per VPC, per Region; default.
  link: [regional DNS service](../facts/route53.md#route53-faq-vpc-resolver-regional-recursive-default)
  link: [by default in every Amazon Virtual Private Cloud](../facts/route53.md#route53-faq-vpc-resolver-regional-recursive-default)
route53-faq-what-is-route53-dns-domains-health
  claim: Amazon Route 53 provides highly available and scalable DNS, domain name registration and health-checking web services.
  scope: Route 53 service.
  link: [highly available and scalable Domain Name System (DNS)](../facts/route53.md#route53-faq-what-is-route53-dns-domains-health)
route53-faq-wildcard-all-types-except-ns
  claim: Amazon Route 53 supports wildcard entries for all record types except NS records.
  scope: wildcard records.
  link: [all record types, except NS records](../facts/route53.md#route53-faq-wildcard-all-types-except-ns)
route53-faq-wildcard-matches-subdomains
  claim: A wildcard record such as *.example.com matches queries for names like www.example.com and subdomain.example.com.
  scope: wildcard records.
  link: [*.example.com](../facts/route53.md#route53-faq-wildcard-matches-subdomains)
route53-faq-wrr-weight-3-and-1-gives-75-25
  claim: With two weighted record sets of weight 3 and weight 1 for one DNS name, the weight 3 record is returned 75% of the time and the weight 1 record 25% of the time.
  scope: two weighted records for one DNS name; example from the FAQ.
  link: [75% of the time](../facts/route53.md#route53-faq-wrr-weight-3-and-1-gives-75-25)
  link: [25% of the time](../facts/route53.md#route53-faq-wrr-weight-3-and-1-gives-75-25)
route53-faq-wrr-weights-0-to-255
  claim: Weights in Weighted Round Robin routing can be any number between 0 and 255.
  scope: per weighted record; maximum; not adjustable; FAQ statement; check the developer guide for weight 0 behavior.
  link: [between 0 and 255](../facts/route53.md#route53-faq-wrr-weights-0-to-255)
  say: zero to two hundred fifty-five
route53-faq-wrr-weights-set-frequency
  claim: Weighted Round Robin assigns weights to record sets to set how often each response is served, for example for A/B testing with a small portion of traffic.
  scope: weighted records.
  link: [A/B testing](../facts/route53.md#route53-faq-wrr-weights-set-frequency)
route53-faq-zone-file-import-into-console
  claim: For new hosted zones, or existing zones that hold only the default NS and SOA records, you can paste a standard zone file into the console and the records are created automatically.
  scope: hosted zones empty except for default NS and SOA records; standard DNS zone files such as BIND.
  link: [paste your zone file directly into the Route 53 console](../facts/route53.md#route53-faq-zone-file-import-into-console)
route53-features-routing-one-line-summaries
  claim: The Amazon Route 53 features page sums up the routing choices: latency based routing sends users to the AWS Region with the lowest possible latency, Geo DNS sends users to an endpoint you specify by geographic location, geoproximity routing sends traffic to the geographically nearest resource and helps apply data residency preferences, and IP-based routing uses the CIDR block of the query-originating IP address.
  scope: Amazon Route 53 routing policies.
  link: [AWS region that provides the lowest possible latency](../facts/route53.md#route53-features-routing-one-line-summaries)
  link: [based on the end user’s geographic location](../facts/route53.md#route53-features-routing-one-line-summaries)
  link: [helps apply data residency preferences](../facts/route53.md#route53-features-routing-one-line-summaries)
  link: [Classless Inter-Domain Routing (CIDR) block](../facts/route53.md#route53-features-routing-one-line-summaries)
route53-features-traffic-flow-and-failover-and-private-dns
  claim: The Amazon Route 53 features page describes Traffic Flow as global traffic management that routes users to the best endpoint based on geoproximity, latency, health and other considerations, DNS failover as automatic rerouting of visitors to an alternate location to avoid site outages, and private DNS for Amazon VPC as managing custom domain names for internal AWS resources without exposing DNS data to the public internet.
  scope: Amazon Route 53 features.
  link: [route end users to the best endpoint](../facts/route53.md#route53-features-traffic-flow-and-failover-and-private-dns)
  link: [route your website visitors to an alternate location](../facts/route53.md#route53-features-traffic-flow-and-failover-and-private-dns)
  link: [without exposing DNS data to the public Internet](../facts/route53.md#route53-features-traffic-flow-and-failover-and-private-dns)
route53-fi-control-plane-apis-hosted-us-east-1
  claim: The Amazon Route 53 control plane is made of all the public Route 53 APIs for hosted zones, records, health checks, DNS query logs, reusable delegation sets, traffic policies and cost allocation tags, and it is hosted in us-east-1.
  scope: Amazon Route 53 control plane.
  link: [It is hosted in us-east-1](../facts/route53.md#route53-fi-control-plane-apis-hosted-us-east-1)
route53-fi-health-check-data-plane-global
  claim: Amazon Route 53 has a separate data plane for health checks, a globally distributed service across multiple AWS Regions that performs the checks, aggregates the results and delivers them to the data planes of Route 53 public and private DNS and Global Accelerator.
  scope: Amazon Route 53 health check data plane.
  link: [globally-distributed service across multiple AWS Regions](../facts/route53.md#route53-fi-health-check-data-plane-global)
route53-fi-impairment-dns-and-health-checks-keep-working
  claim: During a control plane impairment, create, read, update, delete and list operations for Amazon Route 53 may not work, but DNS resolution, health checks and the routing updates that result from health check changes continue to work.
  scope: Amazon Route 53 during a control plane impairment.
  link: [will continue to work](../facts/route53.md#route53-fi-impairment-dns-and-health-checks-keep-working)
  link: [CRUDL-type operations for Route 53 may not work](../facts/route53.md#route53-fi-impairment-dns-and-health-checks-keep-working)
route53-fi-no-control-plane-in-recovery-path
  claim: When you plan for dependencies on Amazon Route 53, do not rely on the Route 53 control plane in your recovery path; a statically stable design uses the status of health checks to fail over between Regions or to evacuate an Availability Zone.
  scope: Amazon Route 53 recovery design.
  link: [you should not rely on the Route 53 control plane in your recovery path](../facts/route53.md#route53-fi-no-control-plane-in-recovery-path)
  link: [status of health checks to perform failovers](../facts/route53.md#route53-fi-no-control-plane-in-recovery-path)
route53-fi-preprovision-for-multi-region-dr
  claim: If you use a multi-Region disaster recovery plan, pre-provision the resources that need DNS records, such as ELBs and RDS instances.
  scope: Amazon Route 53 multi-Region DR plan.
  link: [pre-provision resources that require DNS records](../facts/route53.md#route53-fi-preprovision-for-multi-region-dr)
route53-fi-record-edits-depend-on-control-plane
  claim: Updating a record value with the ChangeResourceRecordSets API, changing the weight of a weighted record, or creating new records to fail over are not statically stable, because they depend on the Amazon Route 53 control plane.
  scope: Amazon Route 53 failover design.
  link: [A non-statically-stable design](../facts/route53.md#route53-fi-record-edits-depend-on-control-plane)
route53-fqdn-trailing-dot-optional
  claim: For record types that include a domain name, enter a fully qualified domain name. The trailing dot is optional because Route 53 assumes the name is fully qualified, so www.example.com and www.example.com. are treated as identical.
  scope: record values that include a domain name.
  link: [The trailing dot is optional](../facts/route53.md#route53-fqdn-trailing-dot-optional)
  link: [treats www.example.com (without a trailing dot)](../facts/route53.md#route53-fqdn-trailing-dot-optional)
route53-geolocation-all-unhealthy-uses-smallest-region-record
  claim: If all applicable geolocation records are unhealthy, including the record for all locations, Route 53 responds using the value of the record for the smallest geographic region.
  scope: geolocation records with health checks.
  link: [record for the smallest geographic region](../facts/route53.md#route53-geolocation-all-unhealthy-uses-smallest-region-record)
route53-geolocation-default-record-handles-unmapped
  claim: A default geolocation record handles queries from IP addresses that are not mapped to a location and queries from locations where you have not created geolocation records.
  scope: geolocation routing.
  link: [handles both queries from unmapped IP addresses](../facts/route53.md#route53-geolocation-default-record-handles-unmapped)
  link: [locations where you haven't created geolocation records](../facts/route53.md#route53-geolocation-default-record-handles-unmapped)
route53-geolocation-location-levels
  claim: With geolocation routing you can specify geographic locations by continent, by country, or by state in the United States.
  scope: geolocation records.
  link: [by continent, by country, or by state](../facts/route53.md#route53-geolocation-location-levels)
  link: [You can specify geographic locations](../facts/route53.md#route53-geolocation-location-levels)
route53-geolocation-maps-ip-addresses-some-unmapped
  claim: Geolocation works by mapping IP addresses to locations. Some IP addresses are not mapped to a location, so even with records for all seven continents some queries come from locations that cannot be identified.
  scope: geolocation routing.
  link: [Geolocation works by mapping IP addresses to locations](../facts/route53.md#route53-geolocation-maps-ip-addresses-some-unmapped)
  link: [some IP addresses aren't mapped to a location](../facts/route53.md#route53-geolocation-maps-ip-addresses-some-unmapped)
route53-geolocation-no-default-no-answer
  claim: If you do not create a default geolocation record, Route 53 returns a no answer response for queries from locations without a geolocation record.
  scope: geolocation routing.
  link: [returns a "no answer" response](../facts/route53.md#route53-geolocation-no-default-no-answer)
  link: [If you don't create a default record](../facts/route53.md#route53-geolocation-no-default-no-answer)
route53-geolocation-private-zone-unhealthy-returns-default
  claim: In a private hosted zone, if the geolocation record for the query's Region is unhealthy, the default record is returned if it is healthy.
  scope: geolocation routing in a private hosted zone with health checks.
  link: [the default record will be returned](../facts/route53.md#route53-geolocation-private-zone-unhealthy-returns-default)
route53-geolocation-private-zone-uses-vpc-region
  claim: For private hosted zones, Route 53 answers geolocation queries based on the AWS Region of the VPC that the query came from. A query from an on-premises part of a hybrid network is treated as coming from the Region that the VPC is in.
  scope: geolocation routing in a private hosted zone.
  link: [based on the AWS Region of the VPC](../facts/route53.md#route53-geolocation-private-zone-uses-vpc-region)
  link: [Region that the VPC is located in](../facts/route53.md#route53-geolocation-private-zone-uses-vpc-region)
route53-geolocation-public-and-private-zones
  claim: You can use geolocation routing for records in both public and private hosted zones.
  scope: geolocation routing.
  link: [both public and private hosted zones](../facts/route53.md#route53-geolocation-public-and-private-zones)
  link: [You can use geolocation routing for records](../facts/route53.md#route53-geolocation-public-and-private-zones)
route53-geolocation-recommend-one-default-record
  claim: AWS recommends creating one geolocation record with the Location value Default. It covers geographic locations that you have not created records for and IP addresses whose location Route 53 cannot identify.
  scope: geolocation records.
  link: [a value of Default for Location](../facts/route53.md#route53-geolocation-recommend-one-default-record)
  link: [IP addresses that Route 53 can't identify a location for](../facts/route53.md#route53-geolocation-recommend-one-default-record)
route53-geolocation-routing-by-query-location
  claim: With geolocation routing, you choose the resources that serve your traffic based on where your users are located, meaning the location that the DNS queries come from.
  scope: geolocation routing.
  link: [where your users are located](../facts/route53.md#route53-geolocation-routing-by-query-location)
  link: [the location that DNS queries come from](../facts/route53.md#route53-geolocation-routing-by-query-location)
route53-geolocation-smallest-region-wins
  claim: If you create separate geolocation records for overlapping geographic regions, such as North America and Canada, priority goes to the smallest geographic region.
  scope: geolocation records.
  link: [priority goes to the smallest geographic region](../facts/route53.md#route53-geolocation-smallest-region-wins)
  link: [separate records for overlapping geographic regions](../facts/route53.md#route53-geolocation-smallest-region-wins)
route53-geolocation-unhealthy-looks-at-larger-region
  claim: For geolocation records, if an endpoint is unhealthy, Route 53 looks for a record for the larger, associated geographic region.
  scope: geolocation records with health checks.
  link: [the larger, associated geographic Region](../facts/route53.md#route53-geolocation-unhealthy-looks-at-larger-region)
  link: [if an endpoint is unhealthy](../facts/route53.md#route53-geolocation-unhealthy-looks-at-larger-region)
route53-geolocation-us-unmapped-ips-need-us-record
  claim: Some IP addresses are associated with the United States but not with a state. Without a record for the United States, Route 53 answers queries from those addresses with the default geolocation record, if there is one, or with a no answer response.
  scope: geolocation records for US states.
  link: [with a "no answer" response](../facts/route53.md#route53-geolocation-us-unmapped-ips-need-us-record)
  link: [default geolocation record (if you created one)](../facts/route53.md#route53-geolocation-us-unmapped-ips-need-us-record)
route53-geolocation-use-cases
  claim: Geolocation routing can show content in the language of your users, limit content to the locations where you have distribution rights, and balance load across endpoints in a predictable way so that each user location always goes to the same endpoint.
  scope: geolocation routing.
  link: [your content in the language of your users](../facts/route53.md#route53-geolocation-use-cases)
  link: [only the locations where you have distribution rights](../facts/route53.md#route53-geolocation-use-cases)
  link: [always goes to the same endpoint](../facts/route53.md#route53-geolocation-use-cases)
route53-geoproximity-aws-resource-location
  claim: For AWS resources in geoproximity routing, you specify the AWS Region or Local Zone Group where you created the resource.
  scope: per geoproximity record.
  link: [AWS Region or Local Zone Group](../facts/route53.md#route53-geoproximity-aws-resource-location)
route53-geoproximity-based-on-location
  claim: Geoproximity routing sends traffic to the closest available resource, based on the location of your users and your resources.
  scope: per geoproximity record.
  link: [closest available resource](../facts/route53.md#route53-geoproximity-based-on-location)
route53-geoproximity-bias-expands-or-shrinks-region
  claim: With geoproximity routing you can send more or less traffic to a resource by setting a bias, which expands or shrinks the geographic region from which traffic goes to that resource.
  scope: Amazon Route 53 geoproximity routing.
  link: [A bias expands or shrinks the geographic region](../facts/route53.md#route53-geoproximity-bias-expands-or-shrinks-region)
route53-geoproximity-bias-negative-range
  claim: A negative bias of -1 to -99 shrinks the geographic region of a resource and expands the adjacent regions.
  scope: per geoproximity record; maximum; not adjustable.
  link: [-1 to -99](../facts/route53.md#route53-geoproximity-bias-negative-range)
route53-geoproximity-bias-positive-range
  claim: A positive bias from 1 to 99 expands the geographic region of a resource and shrinks the adjacent regions.
  scope: per geoproximity record; maximum; not adjustable.
  link: [from 1 to 99](../facts/route53.md#route53-geoproximity-bias-positive-range)
route53-geoproximity-change-bias-in-small-steps
  claim: AWS suggests that you change the bias in small steps to avoid overwhelming your resources with a sudden shift in traffic.
  scope: geoproximity bias.
  link: [change the bias in small steps](../facts/route53.md#route53-geoproximity-change-bias-in-small-steps)
route53-geoproximity-maps-only-with-traffic-flow
  claim: The geoproximity routing page illustrates routing with maps of AWS Regions and notes that the maps are available only with Traffic Flow.
  scope: geoproximity maps.
  link: [The maps are available only with Traffic Flow](../facts/route53.md#route53-geoproximity-maps-only-with-traffic-flow)
route53-geoproximity-non-aws-resource-latlong
  claim: For non-AWS resources in geoproximity routing, you specify the latitude and longitude of the resource.
  scope: per geoproximity record.
  link: [latitude and longitude of the resource](../facts/route53.md#route53-geoproximity-non-aws-resource-latlong)
route53-geoproximity-positive-bias-50-halves-distance
  claim: A geoproximity record with a positive bias of 50 makes Route 53 halve the distance between the query source and the resource.
  scope: per geoproximity record.
  link: [positive bias of 50](../facts/route53.md#route53-geoproximity-positive-bias-50-halves-distance)
route53-geoproximity-unhealthy-endpoint-next-closest
  claim: For geoproximity records, if an endpoint is unhealthy, Route 53 looks for the closest endpoint that is still healthy.
  scope: per geoproximity record with a health check.
  link: [a closest endpoint that is still healthy](../facts/route53.md#route53-geoproximity-unhealthy-endpoint-next-closest)
route53-global-accelerator-alias-record
  claim: To route a domain to an accelerator, you create an alias record with the target Alias to Global Accelerator, using the DNS name of the accelerator, which can be from the current account or a different account.
  scope: alias to Global Accelerator.
  link: [Alias to Global Accelerator](../facts/route53.md#route53-global-accelerator-alias-record)
  link: [Choose the DNS name for the accelerator](../facts/route53.md#route53-global-accelerator-alias-record)
route53-global-resolver-vs-vpc-resolver
  claim: According to the Route 53 FAQ, Global Resolver is reachable over the internet with encryption of DNS queries in transit (DoH or DoT), while VPC Resolver is the default regional resolver for Amazon VPCs, reached by VPC clients or, through Resolver endpoints, by clients over VPN or Direct Connect.
  scope: Route 53 Global Resolver and Route 53 VPC Resolver.
  link: [reachable over the internet](../facts/route53.md#route53-global-resolver-vs-vpc-resolver)
  link: [Default regional resolver for Amazon VPCs](../facts/route53.md#route53-global-resolver-vs-vpc-resolver)
route53-hc-18-percent-may-change
  claim: The 18% healthy-checker value might change in a future release.
  scope: per health check of an endpoint.
  link: [might change in a future release](../facts/route53.md#route53-hc-18-percent-may-change)
route53-hc-18-percent-why-chosen
  claim: AWS chose the 18% value so that health checkers in multiple regions consider the endpoint healthy, which keeps network isolation from some health-checking locations from marking an endpoint unhealthy.
  scope: per health check of an endpoint.
  link: [18% value was chosen](../facts/route53.md#route53-hc-18-percent-why-chosen)
route53-hc-alarm-sns-default-notification
  claim: If you choose to create an alarm with a health check, CloudWatch sends an Amazon SNS notification when the endpoint status changes to unhealthy and Route 53 considers the endpoint unhealthy for one minute.
  scope: default health check alarm.
  link: [CloudWatch sends you an Amazon SNS notification](../facts/route53.md#route53-hc-alarm-sns-default-notification)
  link: [unhealthy for one minute](../facts/route53.md#route53-hc-alarm-sns-default-notification)
  say: one minute
route53-hc-allow-all-region-and-global-cidr-ranges
  claim: When you add health checker IP addresses to an allow list, add all the IP addresses in the CIDR range for each Region that you specified for the health checks, as well as the Global CIDR range. The source IP address in a Region can change at any time.
  scope: allow lists for health checkers.
  link: [add all the IP addresses in the CIDR](../facts/route53.md#route53-hc-allow-all-region-and-global-cidr-ranges)
  link: [as well as the Global CIDR range](../facts/route53.md#route53-hc-allow-all-region-and-global-cidr-ranges)
route53-hc-aws-managed-prefix-list-adds-all-ranges
  claim: To allow Route 53 health checks in a security group, you can allow each IP address range or use an AWS-managed prefix list. When you add the prefix list to your inbound security group, it automatically adds all necessary ranges.
  scope: security groups for Route 53 health checks.
  link: [AWS-managed prefix list](../facts/route53.md#route53-hc-aws-managed-prefix-list-adds-all-ranges)
  link: [it automatically adds all necessary ranges](../facts/route53.md#route53-hc-aws-managed-prefix-list-adds-all-ranges)
route53-hc-calculated-console-256
  claim: The console page for calculated health checks says you can add up to 256 health checks to Health checks to monitor.
  scope: per calculated health check; maximum; not adjustable; Differs from the 255 child health checks stated on the quotas page and the determine-health page.
  link: [up to 256 health checks](../facts/route53.md#route53-hc-calculated-console-256)
route53-hc-calculated-disabled-child-healthy
  claim: If you disable a health check that a calculated health check monitors, Amazon Route 53 considers the disabled health check to be healthy when it calculates whether the calculated health check is healthy.
  scope: per calculated health check; Choose Invert health check status to count it as unhealthy.
  link: [considers the disabled health check to be healthy](../facts/route53.md#route53-hc-calculated-disabled-child-healthy)
route53-hc-calculated-healthy-count-compare
  claim: For a calculated health check, Route 53 adds up the number of child health checks that are considered healthy and compares that number with the number of child health checks that must be healthy for the parent health check to be considered healthy.
  scope: per calculated health check.
  link: [child health checks that must be healthy](../facts/route53.md#route53-hc-calculated-healthy-count-compare)
route53-hc-calculated-monitors-other-health-checks
  claim: A calculated health check monitors whether Route 53 considers other health checks healthy or unhealthy. It can notify you only when the number of available resources drops below a threshold.
  scope: calculated health check.
  link: [monitors whether Route 53 considers other health checks healthy or unhealthy](../facts/route53.md#route53-hc-calculated-monitors-other-health-checks)
  link: [available web resources drops below a specified threshold](../facts/route53.md#route53-hc-calculated-monitors-other-health-checks)
route53-hc-calculated-no-nesting
  claim: A calculated health check cannot monitor other calculated health checks.
  scope: per calculated health check.
  link: [can't configure a calculated health check](../facts/route53.md#route53-hc-calculated-no-nesting)
route53-hc-calculated-report-healthy-rules
  claim: A calculated health check can report healthy when at least a chosen number of the child health checks are healthy, when all of them are healthy (AND), or when one or more of them are healthy (OR).
  scope: calculated health check.
  link: [x of y selected health checks are healthy](../facts/route53.md#route53-hc-calculated-report-healthy-rules)
  link: [Report healthy when all health checks are healthy](../facts/route53.md#route53-hc-calculated-report-healthy-rules)
  link: [when one or more health checks are healthy](../facts/route53.md#route53-hc-calculated-report-healthy-rules)
route53-hc-calculated-threshold-above-children-unhealthy
  claim: If the number of healthy children you require is greater than the number of child health checks, the calculated health check is always unhealthy.
  scope: per calculated health check.
  link: [always considers this health check to be unhealthy](../facts/route53.md#route53-hc-calculated-threshold-above-children-unhealthy)
route53-hc-calculated-threshold-zero-always-healthy
  claim: If the number of healthy children you require is 0, the calculated health check is always healthy.
  scope: per calculated health check.
  link: [always considers this health check to be healthy](../facts/route53.md#route53-hc-calculated-threshold-zero-always-healthy)
route53-hc-cannot-check-private-ip-ranges
  claim: Route 53 cannot check the health of endpoints for which the IP address is in local, private, nonroutable, or multicast ranges.
  scope: endpoint health checks.
  link: [local, private, nonroutable, or multicast ranges](../facts/route53.md#route53-hc-cannot-check-private-ip-ranges)
  link: [Route 53 cannot check the health of endpoints](../facts/route53.md#route53-hc-cannot-check-private-ip-ranges)
route53-hc-checkers-outside-vpc-need-public-ip
  claim: Route 53 health checkers are outside the VPC. To check an endpoint inside a VPC by IP address, you must assign a public IP address to the instance in the VPC.
  scope: failover records in a private hosted zone.
  link: [health checkers are outside the VPC](../facts/route53.md#route53-hc-checkers-outside-vpc-need-public-ip)
  link: [must assign a public IP address](../facts/route53.md#route53-hc-checkers-outside-vpc-need-public-ip)
route53-hc-cloudwatch-alarm-data-stream
  claim: A health check on a CloudWatch alarm monitors the same data stream that CloudWatch monitors for the alarm. Route 53 does not wait for the alarm to go into the ALARM state.
  scope: health check that monitors a CloudWatch alarm.
  link: [data stream that CloudWatch monitors for the alarm](../facts/route53.md#route53-hc-cloudwatch-alarm-data-stream)
  link: [doesn't wait for the CloudWatch alarm](../facts/route53.md#route53-hc-cloudwatch-alarm-data-stream)
route53-hc-cloudwatch-high-resolution-not-supported
  claim: For the CloudWatch alarms that Route 53 health checks can monitor, standard-resolution metrics are supported and high-resolution metrics aren't supported.
  scope: health check that monitors a CloudWatch alarm.
  link: [High-resolution metrics aren't supported](../facts/route53.md#route53-hc-cloudwatch-high-resolution-not-supported)
route53-hc-cloudwatch-insufficient-data-setting
  claim: If the data stream does not give enough information to determine the state of the alarm, the health check status depends on the Health check status setting: healthy, unhealthy, or last known status.
  scope: health check that monitors a CloudWatch alarm.
  link: [healthy, unhealthy, or last known status](../facts/route53.md#route53-hc-cloudwatch-insufficient-data-setting)
route53-hc-cloudwatch-same-account-only
  claim: A health check can only monitor a CloudWatch alarm that exists in the same AWS account as the health check.
  scope: health check that monitors a CloudWatch alarm.
  link: [same AWS account as the health check](../facts/route53.md#route53-hc-cloudwatch-same-account-only)
route53-hc-disabled-always-healthy
  claim: After you disable a health check, Route 53 considers its status to always be healthy. If you configured DNS failover, Route 53 continues to route traffic to the corresponding resources.
  scope: disabled health check.
  link: [the health check to always be healthy](../facts/route53.md#route53-hc-disabled-always-healthy)
  link: [continues to route traffic to the corresponding resources](../facts/route53.md#route53-hc-disabled-always-healthy)
route53-hc-disabled-invert-to-stop-traffic
  claim: After you disable a health check, Route 53 considers its status to always be healthy and, if you configured DNS failover, continues to route traffic to the corresponding resources. To stop routing traffic to a resource, invert the health check.
  scope: disabled health check.
  link: [invert the health check](../facts/route53.md#route53-hc-disabled-invert-to-stop-traffic)
route53-hc-disabled-still-charged
  claim: Charges for a health check still apply when the health check is disabled.
  scope: disabled health check.
  link: [Charges for a health check still apply](../facts/route53.md#route53-hc-disabled-still-charged)
route53-hc-domain-name-ipv4-only
  claim: If you specify the endpoint by domain name, Route 53 uses only IPv4 to send health checks to the endpoint.
  scope: health check with a domain name endpoint.
  link: [uses only IPv4 to send health checks](../facts/route53.md#route53-hc-domain-name-ipv4-only)
route53-hc-domain-name-not-record-name
  claim: If you check the health of failover, geolocation, geoproximity, latency, multivalue or weighted records and specify the endpoint by domain name, specify the domain name of each server for Domain name, not the name of the records. If the Domain name of a health check matches the name of the records and you associate the health check with those records, health check results will be unpredictable.
  scope: health check with a domain name endpoint.
  link: [health check results will be unpredictable](../facts/route53.md#route53-hc-domain-name-not-record-name)
route53-hc-domain-name-resolved-at-interval
  claim: If you specify the endpoint by domain name, Route 53 sends a DNS query to resolve the domain name at the request interval and then checks the health of the endpoint by using an IP address that DNS returns.
  scope: health check with a domain name endpoint.
  link: [DNS query to resolve the domain name](../facts/route53.md#route53-hc-domain-name-resolved-at-interval)
  link: [Using an IP address that DNS returns](../facts/route53.md#route53-hc-domain-name-resolved-at-interval)
route53-hc-endpoint-automated-requests-over-internet
  claim: At regular intervals that you specify, Route 53 submits automated requests over the internet to your application, server or other resource to verify that it is reachable, available and functional.
  scope: endpoint health check.
  link: [automated requests over the internet](../facts/route53.md#route53-hc-endpoint-automated-requests-over-internet)
  link: [reachable, available, and functional](../facts/route53.md#route53-hc-endpoint-automated-requests-over-internet)
route53-hc-endpoint-by-ip-or-domain
  claim: An endpoint health check monitors an endpoint that you specify either by IP address or by domain name.
  scope: endpoint health check.
  link: [either by IP address or by domain name](../facts/route53.md#route53-hc-endpoint-by-ip-or-domain)
  link: [monitors an endpoint that you specify](../facts/route53.md#route53-hc-endpoint-by-ip-or-domain)
route53-hc-failure-threshold-default-3
  claim: If you don't specify a FailureThreshold, the default is three health checks; FailureThreshold is not supported for health checks of type RECOVERY_CONTROL.
  scope: per health check; default; not adjustable; Not supported for health checks of type RECOVERY_CONTROL.
  link: [three health checks](../facts/route53.md#route53-hc-failure-threshold-default-3)
route53-hc-failure-threshold-definition
  claim: The failure threshold is the number of consecutive health checks that an endpoint must pass or fail for Route 53 to change its status between unhealthy and healthy.
  scope: per health check.
  link: [consecutive health checks](../facts/route53.md#route53-hc-failure-threshold-definition)
route53-hc-failure-threshold-range-1-10
  claim: The failure threshold can be between 1 and 10 consecutive checks, and an unhealthy endpoint must pass the same number of checks to be considered healthy.
  scope: per health check; maximum; not adjustable; Stated in the 2014 release note on the History page.
  link: [between 1 and 10 consecutive checks](../facts/route53.md#route53-hc-failure-threshold-range-1-10)
route53-hc-fast-interval-extra-charge
  claim: Choosing the Fast (10 seconds) request interval for a health check adds an additional charge.
  scope: per health check.
  link: [additional charge applies](../facts/route53.md#route53-hc-fast-interval-extra-charge)
route53-hc-global-service-no-region-for-health-checks
  claim: Route 53 is a global service, so you do not specify the Region in which you create health checks.
  scope: health checks.
  link: [Route 53 is a global service](../facts/route53.md#route53-hc-global-service-no-region-for-health-checks)
route53-hc-healthy-above-18-percent
  claim: If more than 18% of Route 53 health checkers report an endpoint as healthy, Route 53 considers the endpoint healthy.
  scope: per health check of an endpoint; minimum; not adjustable.
  link: [more than 18%](../facts/route53.md#route53-hc-healthy-above-18-percent)
route53-hc-http-https-status-2xx-3xx
  claim: For an HTTP health check, Route 53 tries to establish a TCP connection and, if successful, submits an HTTP request and waits for an HTTP status code of 2xx or 3xx. An HTTPS check works the same way with an HTTPS request.
  scope: HTTP and HTTPS health checks.
  link: [waits for an HTTP status code of 2xx or 3xx](../facts/route53.md#route53-hc-http-https-status-2xx-3xx)
  link: [Route 53 tries to establish a TCP connection](../facts/route53.md#route53-hc-http-https-status-2xx-3xx)
route53-hc-http-status-within-two-seconds
  claim: For HTTP and HTTPS health checks, the endpoint must respond with an HTTP status code of 2xx or 3xx within two seconds after connecting.
  scope: per HTTP or HTTPS health check; maximum; not adjustable.
  link: [within two seconds after connecting](../facts/route53.md#route53-hc-http-status-within-two-seconds)
route53-hc-http-tcp-connect-four-seconds
  claim: For HTTP and HTTPS health checks, Route 53 must be able to establish a TCP connection with the endpoint within four seconds.
  scope: per HTTP or HTTPS health check; maximum; not adjustable.
  link: [within four seconds](../facts/route53.md#route53-hc-http-tcp-connect-four-seconds)
route53-hc-https-does-not-validate-certificates
  claim: HTTPS health checks do not validate SSL/TLS certificates, so checks do not fail if a certificate is invalid or expired.
  scope: HTTPS health checks.
  link: [don't validate SSL/TLS certificates](../facts/route53.md#route53-hc-https-does-not-validate-certificates)
  link: [checks don't fail if a certificate is invalid](../facts/route53.md#route53-hc-https-does-not-validate-certificates)
route53-hc-https-requires-tls-1x
  claim: An HTTPS health check needs an endpoint that supports TLS v1.0, v1.1, or v1.2.
  scope: per HTTPS health check.
  link: [TLS v1.0, v1.1, or v1.2](../facts/route53.md#route53-hc-https-requires-tls-1x)
route53-hc-invert-reverses-status
  claim: If you invert a health check, Route 53 considers the health check unhealthy when the status is healthy, and the reverse.
  scope: inverted health check.
  link: [invert the status of a health check](../facts/route53.md#route53-hc-invert-reverses-status)
  link: [unhealthy when the status is healthy](../facts/route53.md#route53-hc-invert-reverses-status)
route53-hc-metrics-only-in-us-east-1
  claim: To view Route 53 health check metrics in CloudWatch, the current Region must be US East (N. Virginia). The metrics are not available in any other Region.
  scope: CloudWatch metrics for health checks.
  link: [not available if you select any other region](../facts/route53.md#route53-hc-metrics-only-in-us-east-1)
  link: [Route 53 metrics are not available](../facts/route53.md#route53-hc-metrics-only-in-us-east-1)
route53-hc-new-check-healthy-until-enough-data
  claim: Route 53 considers a new health check to be healthy until there is enough data to determine the real status. If the health check is inverted, a new health check is considered unhealthy until there is enough data.
  scope: new health check.
  link: [check to be healthy until there's enough data](../facts/route53.md#route53-hc-new-check-healthy-until-enough-data)
  link: [check to be unhealthy until there's enough data](../facts/route53.md#route53-hc-new-check-healthy-until-enough-data)
route53-hc-private-endpoint-cloudwatch-alarm-health-check
  claim: For instances in a VPC that have only private IP addresses, you can create a CloudWatch metric, associate an alarm with it, and create a health check that is based on the data stream for the alarm.
  scope: failover records in a private hosted zone.
  link: [CloudWatch metric, associate an alarm with the metric](../facts/route53.md#route53-hc-private-endpoint-cloudwatch-alarm-health-check)
  link: [based on the data stream for the alarm](../facts/route53.md#route53-hc-private-endpoint-cloudwatch-alarm-health-check)
route53-hc-protocol-fixed-after-creation
  claim: After you create a health check, you cannot change its protocol.
  scope: health check.
  link: [can't change the value of Protocol](../facts/route53.md#route53-hc-protocol-fixed-after-creation)
route53-hc-regions-at-least-three-customized
  claim: If you customize the health checker Regions, you must specify at least three Regions.
  scope: health checker regions; minimum.
  link: [You must specify at least three Regions](../facts/route53.md#route53-hc-regions-at-least-three-customized)
  link: [add a Region back to the list](../facts/route53.md#route53-hc-regions-at-least-three-customized)
  say: at least three Regions
route53-hc-regions-recommended-or-chosen
  claim: You can have Route 53 check the endpoint from the recommended Regions or from Regions that you specify.
  scope: endpoint health checks.
  link: [using health checkers in regions that you specify](../facts/route53.md#route53-hc-regions-recommended-or-chosen)
  link: [health checkers in the recommended regions](../facts/route53.md#route53-hc-regions-recommended-or-chosen)
route53-hc-removed-region-continues-up-to-an-hour
  claim: If you remove a Region from a health check, Route 53 continues to perform checks from that Region for up to an hour, so that some health checkers are always checking the endpoint.
  scope: health checker regions.
  link: [for up to an hour](../facts/route53.md#route53-hc-removed-region-continues-up-to-an-hour)
route53-hc-request-interval-10-or-30-seconds
  claim: You can set a Route 53 health check to run every 10 seconds or every 30 seconds.
  scope: per health check; maximum; not adjustable; Fast (10 seconds) costs extra.
  link: [every 10 seconds or every 30 seconds](../facts/route53.md#route53-hc-request-interval-10-or-30-seconds)
route53-hc-request-interval-default-30
  claim: If you don't specify a RequestInterval for a health check, the default is 30 seconds. You can't change RequestInterval after you create the health check, and RequestInterval is not supported for health checks of type RECOVERY_CONTROL.
  scope: per health check; default; not adjustable; Cannot be changed after the health check is created; not supported for type RECOVERY_CONTROL.
  link: [30 seconds](../facts/route53.md#route53-hc-request-interval-default-30)
route53-hc-request-interval-fixed-after-create
  claim: After you create a health check, you cannot change its request interval.
  scope: per health check.
  link: [can't change the value](../facts/route53.md#route53-hc-request-interval-fixed-after-create)
route53-hc-request-types-http-https-tcp-to-ip-and-port
  claim: When Route 53 checks the health of an endpoint, it sends an HTTP, HTTPS or TCP request to the IP address and port that you specified in the health check.
  scope: endpoint health checks.
  link: [an HTTP, HTTPS, or TCP request](../facts/route53.md#route53-hc-request-types-http-https-tcp-to-ip-and-port)
  link: [the IP address and port that you specified](../facts/route53.md#route53-hc-request-types-http-https-tcp-to-ip-and-port)
route53-hc-router-firewall-must-allow-health-checker-ips
  claim: For a health check to succeed, your router and firewall rules must allow inbound traffic from the IP addresses that the Route 53 health checkers use.
  scope: endpoint health checks.
  link: [must allow inbound traffic from the IP addresses that the Route 53 health checkers use](../facts/route53.md#route53-hc-router-firewall-must-allow-health-checker-ips)
  link: [your router and firewall rules](../facts/route53.md#route53-hc-router-firewall-must-allow-health-checker-ips)
route53-hc-search-string-max-255-characters
  claim: The search string of a string matching health check can be at most 255 characters long.
  scope: per health check search string; maximum; not adjustable.
  link: [255 characters](../facts/route53.md#route53-hc-search-string-max-255-characters)
route53-hc-sns-notification-may-take-minutes
  claim: Several minutes might pass between the time that a health check fails and the time that you receive the SNS notification.
  scope: health check notifications.
  link: [several minutes might elapse](../facts/route53.md#route53-hc-sns-notification-may-take-minutes)
route53-hc-sns-topic-must-be-us-east-1
  claim: An existing SNS topic used for health check notifications must be in the US East (N. Virginia) Region.
  scope: health check notifications.
  link: [US East (N. Virginia) Region](../facts/route53.md#route53-hc-sns-topic-must-be-us-east-1)
route53-hc-string-match-first-5120-bytes
  claim: In a string matching health check, the search string must appear entirely in the first 5,120 bytes of the response body or the endpoint fails the check.
  scope: per string matching health check; maximum; not adjustable.
  link: [first 5,120 bytes](../facts/route53.md#route53-hc-string-match-first-5120-bytes)
route53-hc-string-match-response-body-two-seconds
  claim: In a string matching health check, the health checker must receive the response body within two seconds after it receives the HTTP status code.
  scope: per string matching health check; maximum; not adjustable.
  link: [within the next two seconds](../facts/route53.md#route53-hc-string-match-response-body-two-seconds)
route53-hc-string-matching-body-search
  claim: With string matching, Route 53 submits an HTTP or HTTPS request and searches the response body for a specified string. If the body contains it, the endpoint is healthy; if not, or if the endpoint does not respond, it is unhealthy.
  scope: HTTP and HTTPS health checks.
  link: [searching the response body for a specified string](../facts/route53.md#route53-hc-string-matching-body-search)
  link: [If the response body contains the value](../facts/route53.md#route53-hc-string-matching-body-search)
route53-hc-string-matching-case-sensitive
  claim: Route 53 considers case when it searches for the search string in the response body.
  scope: string matching.
  link: [considers case when searching](../facts/route53.md#route53-hc-string-matching-case-sensitive)
route53-hc-string-matching-compressed-response
  claim: A Route 53 health checker uncompresses a response before searching for the string only if the web server used a compression algorithm that health checkers support. If the response is compressed using another algorithm, the health checker can't decompress the response before searching, so the search will almost always fail and Route 53 will consider the endpoint unhealthy.
  scope: string matching.
  link: [can't decompress the response before searching](../facts/route53.md#route53-hc-string-matching-compressed-response)
route53-hc-tcp-connect-ten-seconds
  claim: For TCP health checks, Route 53 must be able to establish a TCP connection with the endpoint within 10 seconds.
  scope: per TCP health check; maximum; not adjustable.
  link: [within ten seconds](../facts/route53.md#route53-hc-tcp-connect-ten-seconds)
route53-hc-tcp-only-connection
  claim: For a TCP health check, Route 53 tries to establish a TCP connection.
  scope: TCP health check.
  link: [Route 53 tries to establish a TCP connection](../facts/route53.md#route53-hc-tcp-only-connection)
  link: [establish a TCP connection](../facts/route53.md#route53-hc-tcp-only-connection)
route53-hc-unhealthy-18-percent-or-fewer
  claim: If 18% of health checkers or fewer report an endpoint as healthy, Route 53 considers the endpoint unhealthy.
  scope: per health check of an endpoint; maximum; not adjustable.
  link: [18% of health checkers or fewer](../facts/route53.md#route53-hc-unhealthy-18-percent-or-fewer)
route53-health-check-alias-record-not-recommended
  claim: You can associate health checks with alias records, but AWS recommends associating health checks only with non-alias records.
  scope: health checks and alias records.
  link: [associate health checks only with non-alias records](../facts/route53.md#route53-health-check-alias-record-not-recommended)
  link: [You can associate health checks with alias records](../facts/route53.md#route53-health-check-alias-record-not-recommended)
route53-health-check-can-monitor-other-health-checks-two-of-five
  claim: You can configure a health check to monitor the health of one or more other health checks. This tells you when a specified number of resources, such as two web servers out of five, are unavailable.
  scope: calculated health check.
  link: [health of one or more other health checks](../facts/route53.md#route53-health-check-can-monitor-other-health-checks-two-of-five)
  link: [when a specified number of resources](../facts/route53.md#route53-health-check-can-monitor-other-health-checks-two-of-five)
route53-health-check-endpoint-definition
  claim: A health check endpoint is the resource, such as a web server or email server, that the health check monitors. You can specify it by IPv4 address, IPv6 address or domain name.
  scope: Route 53 health check.
  link: [by IPv4 address](../facts/route53.md#route53-health-check-endpoint-definition)
  link: [by IPv6 address](../facts/route53.md#route53-health-check-endpoint-definition)
  link: [or by domain name](../facts/route53.md#route53-health-check-endpoint-definition)
route53-health-check-failure-threshold-counts-consecutive-failures
  claim: If the endpoint does not respond, Route 53 counts consecutive failed requests. When the count reaches the failure threshold, Route 53 considers the endpoint unhealthy. If the endpoint responds again before that, Route 53 resets the count to 0.
  scope: endpoint health checks.
  link: [value that you specified for the failure threshold](../facts/route53.md#route53-health-check-failure-threshold-counts-consecutive-failures)
  link: [Route 53 resets the count to 0](../facts/route53.md#route53-health-check-failure-threshold-counts-consecutive-failures)
route53-health-check-is-periodic-not-at-query-time
  claim: Route 53 periodically checks the health of the endpoint in a health check. It does not perform the health check when the DNS query arrives.
  scope: health checks.
  link: [periodically checks the health of the endpoint](../facts/route53.md#route53-health-check-is-periodic-not-at-query-time)
  link: [it doesn't perform the health check](../facts/route53.md#route53-health-check-is-periodic-not-at-query-time)
route53-health-check-notification-uses-cloudwatch-and-sns
  claim: When you configure notification for a health check, Route 53 sets a CloudWatch alarm, and CloudWatch uses Amazon SNS to notify users that an endpoint is unhealthy.
  scope: health check notification.
  link: [Route 53 sets a CloudWatch alarm](../facts/route53.md#route53-health-check-notification-uses-cloudwatch-and-sns)
  link: [CloudWatch uses Amazon SNS to notify users](../facts/route53.md#route53-health-check-notification-uses-cloudwatch-and-sns)
route53-health-check-private-resource-cloudwatch-alarm-broad-criteria
  claim: You can configure a health check to check the status of a CloudWatch alarm, so that you can be notified based on a broad range of criteria, not just whether a resource is responding to requests.
  scope: health check that monitors a CloudWatch alarm.
  link: [notified based on a broad range of criteria](../facts/route53.md#route53-health-check-private-resource-cloudwatch-alarm-broad-criteria)
route53-health-check-status-visible-in-console-without-notification
  claim: If you do not configure notification, you can still see the status of your Route 53 health checks in the Route 53 console.
  scope: health checks.
  link: [you can still see the status of your Route 53 health checks in the Route 53 console](../facts/route53.md#route53-health-check-status-visible-in-console-without-notification)
route53-health-check-useful-only-when-choosing-between-records
  claim: Associating a health check with a record is useful only when Route 53 is choosing between two or more records to respond to a DNS query and you want the choice to depend in part on the health check status.
  scope: health check association.
  link: [useful only when Route 53 is choosing between two or more records](../facts/route53.md#route53-health-check-useful-only-when-choosing-between-records)
  link: [in part on health check status](../facts/route53.md#route53-health-check-useful-only-when-choosing-between-records)
route53-hosted-zone-container
  claim: A hosted zone is a container for records that tell how to route traffic for a domain and all of its subdomains. The hosted zone has the same name as the domain.
  scope: hosted zone.
  link: [A container for records](../facts/route53.md#route53-hosted-zone-container)
  link: [same name as the domain](../facts/route53.md#route53-hosted-zone-container)
  link: [all of its subdomains](../facts/route53.md#route53-hosted-zone-container)
route53-hybrid-endpoints-not-across-regions
  claim: Resolver endpoints cannot be used across Regions.
  scope: Route 53 VPC Resolver endpoints.
  link: [Endpoints cannot be used across Regions](../facts/route53.md#route53-hybrid-endpoints-not-across-regions)
route53-hybrid-endpoints-two-subnets-two-azs
  claim: For high availability, create inbound or outbound endpoints with at least two subnets in different Availability Zones, and use both endpoint IP addresses in the on-premises DNS resolver for an inbound endpoint.
  scope: Route 53 VPC Resolver endpoints.
  link: [at least two subnets in different Availability Zones](../facts/route53.md#route53-hybrid-endpoints-two-subnets-two-azs)
route53-hybrid-one-outbound-endpoint-shared-by-rules
  claim: You need only one outbound endpoint for multiple VPCs: you share the outbound endpoint by sharing the Resolver rules created for it with other accounts using RAM, instead of creating an outbound endpoint in each VPC.
  scope: Route 53 VPC Resolver outbound endpoints and rules.
  link: [need only one outbound endpoint for multiple VPCs](../facts/route53.md#route53-hybrid-one-outbound-endpoint-shared-by-rules)
route53-hybrid-own-forwarders-on-ec2-alternative
  claim: As an alternative to Resolver endpoints, you can deploy and manage your own DNS infrastructure on EC2 instances to handle DNS requests from VPCs or on-premises, and the whitepaper names logging DNS queries as one reason to run your own forwarders.
  scope: hybrid DNS between a VPC and on-premises.
  link: [additional DNS infrastructure running on EC2 instances](../facts/route53.md#route53-hybrid-own-forwarders-on-ec2-alternative)
  link: [your own forwarders is to log DNS queries](../facts/route53.md#route53-hybrid-own-forwarders-on-ec2-alternative)
route53-hybrid-resolver-endpoints-no-extra-dns-servers
  claim: Route 53 Resolver endpoints and forwarding rules forward traffic between your Amazon VPC and your on-premises data center without having to deploy additional DNS servers.
  scope: Route 53 VPC Resolver endpoints and forwarding rules.
  link: [without having to deploy additional DNS servers](../facts/route53.md#route53-hybrid-resolver-endpoints-no-extra-dns-servers)
route53-hybrid-selection-cost
  claim: Cost is rated Low for Route 53 Resolver and secondary DNS in a VPC, High for highly distributed forwarders and Medium for zonal forwarders in the hybrid DNS whitepaper.
  scope: hybrid DNS solutions in the historical whitepaper; The whitepaper is for historical reference only..
  link: [Low](../facts/route53.md#route53-hybrid-selection-cost)
route53-hybrid-selection-implementation-complexity
  claim: Implementation complexity is rated Low for Route 53 Resolver, Medium for secondary DNS in a VPC, and High for both highly distributed forwarders and zonal forwarders in the hybrid DNS whitepaper.
  scope: hybrid DNS solutions in the historical whitepaper; The whitepaper is for historical reference only..
  link: [Low](../facts/route53.md#route53-hybrid-selection-implementation-complexity)
route53-hybrid-selection-management-overhead
  claim: Management overhead is rated Low for Route 53 Resolver and secondary DNS in a VPC, High for highly distributed forwarders and Medium for zonal forwarders in the hybrid DNS whitepaper.
  scope: hybrid DNS solutions in the historical whitepaper; The whitepaper is for historical reference only..
  link: [Low](../facts/route53.md#route53-hybrid-selection-management-overhead)
route53-hybrid-whitepaper-historical-banner
  claim: The hybrid cloud DNS whitepaper is for historical reference only, and some of its content might be outdated.
  scope: Hybrid Cloud DNS Options for Amazon VPC whitepaper.
  link: [for historical reference only](../facts/route53.md#route53-hybrid-whitepaper-historical-banner)
route53-hybrid-whitepaper-logging-reason-outdated
  claim: The hybrid DNS whitepaper, which is for historical reference only, gives logging DNS queries as one reason to run your own forwarders. The developer guide history shows that support for Resolver query logs was added on September 1, 2020, and Resolver query logging can log queries that originate in your VPCs, queries from inbound Resolver endpoints and queries that use outbound Resolver endpoints.
  scope: Route 53 VPC Resolver query logging.
  link: [Added support for Resolver query logs](../facts/route53.md#route53-hybrid-whitepaper-logging-reason-outdated)
  link: [your own forwarders is to log DNS queries](../facts/route53.md#route53-hybrid-whitepaper-logging-reason-outdated)
route53-ip-based-location-can-hold-ipv4-and-ipv6
  claim: A single CIDR location can have both IPv4 and IPv6 blocks, and it can be associated with both A and AAAA record sets.
  scope: CIDR locations.
  link: [both IPv4 and IPv6 blocks](../facts/route53.md#route53-ip-based-location-can-hold-ipv4-and-ipv6)
route53-ip-based-longer-cidr-query-matches-shorter-cidr
  claim: For DNS queries with a CIDR longer than the one specified in the CIDR collection, Route 53 matches it to the shorter CIDR. If the query CIDR is shorter than the one in the collection, it does not match and Route 53 answers with the record for the default location.
  scope: IP-based routing.
  link: [a CIDR longer than the one specified](../facts/route53.md#route53-ip-based-longer-cidr-query-matches-shorter-cidr)
  link: [will not match and Route 53 will answer with the record for the default](../facts/route53.md#route53-ip-based-longer-cidr-query-matches-shorter-cidr)
route53-ip-based-routing-geolocation-latency-use-aws-data
  claim: Geolocation and latency-based routing use data that Route 53 collects and keeps current. IP-based routing adds the ability to tune routing based on what you know about your customer base.
  scope: IP-based routing.
  link: [uses data that Route 53 collects and keeps current](../facts/route53.md#route53-ip-based-routing-geolocation-latency-use-aws-data)
  link: [tune routing based on what you know about](../facts/route53.md#route53-ip-based-routing-geolocation-latency-use-aws-data)
route53-ip-based-routing-not-in-private-hosted-zone
  claim: You cannot use the IP-based routing policy for records in a private hosted zone.
  scope: IP-based routing.
  link: [cannot use IP-based routing policy for records](../facts/route53.md#route53-ip-based-routing-not-in-private-hosted-zone)
  link: [You cannot use IP-based routing policy](../facts/route53.md#route53-ip-based-routing-not-in-private-hosted-zone)
route53-ip-based-routing-use-cases
  claim: Common use cases for IP-based routing are routing end users from certain ISPs to specific endpoints to optimize network transit costs or performance, and adding overrides to existing routing types such as geolocation.
  scope: IP-based routing.
  link: [from certain ISPs to specific endpoints](../facts/route53.md#route53-ip-based-routing-use-cases)
  link: [add overrides to existing Route 53 routing types](../facts/route53.md#route53-ip-based-routing-use-cases)
route53-ip-based-routing-uses-your-ip-to-endpoint-mappings
  claim: With IP-based routing you upload your data to Route 53 as user-IP-to-endpoint mappings, which gives you fine-grained control to boost performance or cut network costs; one common use case is routing end users from certain ISPs to specific endpoints.
  scope: IP-based routing.
  link: [uploading your data to Route 53 as user-IP-to-endpoint mappings](../facts/route53.md#route53-ip-based-routing-uses-your-ip-to-endpoint-mappings)
  link: [fine-grained control to boost performance](../facts/route53.md#route53-ip-based-routing-uses-your-ip-to-endpoint-mappings)
route53-last-resort-mode-all-unhealthy-returns-answer
  claim: Each request routing algorithm, such as weighted and failover, has a mode of last resort: when all records are considered unhealthy, the algorithm reverts to considering all records healthy. Route 53 returns an answer rather than no answer or an NXDOMAIN response.
  scope: routing algorithms with health checks.
  link: [a mode of last resort](../facts/route53.md#route53-last-resort-mode-all-unhealthy-returns-answer)
  link: [returning an NXDOMAIN (non-existent domain) response](../facts/route53.md#route53-last-resort-mode-all-unhealthy-returns-answer)
route53-latency-changes-over-time
  claim: Latency between hosts on the internet can change over time. Latency-based routing uses latency data taken over a period of time, so a request routed to one Region this week might go to another Region next week.
  scope: latency routing.
  link: [latency data taken over a period of time](../facts/route53.md#route53-latency-changes-over-time)
  link: [might go to the Singapore Region next week](../facts/route53.md#route53-latency-changes-over-time)
route53-latency-data-is-aws-traffic-not-your-resources
  claim: Latency data is based entirely on traffic between users and AWS data centers, so if you are not using resources in an AWS Region the actual latency between your users and your resources can vary significantly from AWS latency data.
  scope: Amazon Route 53 latency-based routing.
  link: [traffic between users and AWS data centers](../facts/route53.md#route53-latency-data-is-aws-traffic-not-your-resources)
route53-latency-no-non-latency-record-same-name-type
  claim: You cannot create non-latency records that have the same record name and record type as latency records.
  scope: latency records.
  link: [You can't create non-latency records](../facts/route53.md#route53-latency-no-non-latency-record-same-name-type)
route53-latency-not-all-regions-required
  claim: You are not required to create latency records for all Regions. Route 53 chooses the Region with the best latency from among the Regions that you create latency records for.
  scope: latency records.
  link: [aren't required to create latency records for all Amazon EC2 Regions](../facts/route53.md#route53-latency-not-all-regions-required)
  link: [chooses the Region with the best latency](../facts/route53.md#route53-latency-not-all-regions-required)
route53-latency-one-record-per-region
  claim: You can only create one latency record for each Amazon EC2 Region.
  scope: latency records; maximum.
  link: [only create one latency record for each Amazon EC2 Region](../facts/route53.md#route53-latency-one-record-per-region)
route53-latency-private-zone-outbound-forwarded-to-inbound
  claim: If an outbound endpoint forwards to an inbound endpoint, a latency record resolves based on where the inbound endpoint is, not the outbound endpoint.
  scope: latency routing in a private hosted zone.
  link: [based on where the inbound endpoint is](../facts/route53.md#route53-latency-private-zone-outbound-forwarded-to-inbound)
route53-latency-private-zone-unhealthy-next-lowest
  claim: With health checks in a private hosted zone, if the record with the lowest latency to the query's origin is unhealthy, a healthy endpoint with the next lowest latency is returned.
  scope: latency routing in a private hosted zone with health checks.
  link: [endpoint with the next lowest latency is returned](../facts/route53.md#route53-latency-private-zone-unhealthy-next-lowest)
route53-latency-private-zone-uses-vpc-region
  claim: For private hosted zones, Route 53 answers latency queries with an endpoint in the same AWS Region as the VPC the query came from, or closest to that Region.
  scope: latency routing in a private hosted zone.
  link: [same AWS Region, or is closest in distance](../facts/route53.md#route53-latency-private-zone-uses-vpc-region)
  link: [the AWS Region of the VPC](../facts/route53.md#route53-latency-private-zone-uses-vpc-region)
route53-latency-routing-lowest-latency-region
  claim: With latency-based routing, Route 53 checks which Regions you created latency records for, finds which Region gives the user the lowest latency, and responds with the value from the latency record for that Region.
  scope: latency routing.
  link: [Region gives the user the lowest latency](../facts/route53.md#route53-latency-routing-lowest-latency-region)
  link: [your resources in multiple AWS Regions](../facts/route53.md#route53-latency-routing-lowest-latency-region)
route53-matching-phz-no-record-returns-nxdomain
  claim: If a private hosted zone matches but has no record for the requested name and type, VPC Resolver does not forward the request to a public DNS resolver. It returns NXDOMAIN to the client.
  scope: private hosted zone that matches the name.
  link: [it returns NXDOMAIN (non-existent domain) to the client](../facts/route53.md#route53-matching-phz-no-record-returns-nxdomain)
  link: [doesn't forward the request to a public DNS](../facts/route53.md#route53-matching-phz-no-record-returns-nxdomain)
route53-migrate-alias-records-last
  claim: When you migrate a hosted zone by editing the exported records file, and the zone contains aliases that refer to other records in the same hosted zone, move the alias records to the bottom of the file, because Route 53 must create the record that an alias record refers to before it can create the alias record. If an alias record refers to another alias record, the alias target must appear first in the file.
  scope: hosted zone migration by file; the hosted zone contains aliases that refer to other records in the same hosted zone.
  link: [Move the alias records to the bottom](../facts/route53.md#route53-migrate-alias-records-last)
  link: [must create the record that an alias record](../facts/route53.md#route53-migrate-alias-records-last)
route53-migrate-dns-before-transfer-if-registrar-has-no-paid-dns
  claim: If your current registrar does not provide paid DNS service, you must migrate DNS service before you transfer the domain. Otherwise the registrar stops providing DNS service when you transfer the domain and the associated websites become unavailable.
  scope: domain transfer to Route 53.
  link: [migrate DNS service before you transfer the domain](../facts/route53.md#route53-migrate-dns-before-transfer-if-registrar-has-no-paid-dns)
  link: [stop providing DNS service when you transfer](../facts/route53.md#route53-migrate-dns-before-transfer-if-registrar-has-no-paid-dns)
route53-migrate-dns-in-use-quick-rollback
  claim: Your domain should remain available during the entire DNS migration. In the unlikely event that there are issues, the procedure for a domain that is in use (getting traffic) lets you roll back quickly; with the procedure for an inactive domain, the domain could be unavailable for a couple of days.
  scope: DNS migration to Route 53.
  link: [the first option lets you roll back quickly](../facts/route53.md#route53-migrate-dns-in-use-quick-rollback)
  link: [should remain available during the entire migration process](../facts/route53.md#route53-migrate-dns-in-use-quick-rollback)
route53-migrate-dnssec-setting-not-migrated
  claim: Route 53 does not currently support migrating the DNSSEC setting. Before the migration you disable DNSSEC validation by removing the DS record from the parent zone.
  scope: hosted zone migration.
  link: [does not currently support migrating the DNSSEC setting](../facts/route53.md#route53-migrate-dnssec-setting-not-migrated)
  link: [removing the DS record from the parent zone](../facts/route53.md#route53-migrate-dnssec-setting-not-migrated)
route53-migrate-health-checks-recreate
  claim: To migrate a Route 53 health check to a new account, you create new health checks in the new account with the same configuration as the existing ones.
  scope: hosted zone migration.
  link: [create new health checks in your new account](../facts/route53.md#route53-migrate-health-checks-recreate)
  link: [same configuration as your existing ones](../facts/route53.md#route53-migrate-health-checks-recreate)
route53-migrate-hosted-zone-large-export-edit-import
  claim: For a zone with a large number of records, you can export the records to a file, edit the file, and use it to create the records in the new hosted zone.
  scope: hosted zone migration.
  link: [export the records you want to migrate](../facts/route53.md#route53-migrate-hosted-zone-large-export-edit-import)
  link: [use the edited file to create records](../facts/route53.md#route53-migrate-hosted-zone-large-export-edit-import)
route53-migrate-hosted-zone-new-zone-copy-records
  claim: To migrate a hosted zone to another AWS account, you create the new hosted zone in the account that you migrate to, and then migrate the records from the old hosted zone to the new one.
  scope: hosted zone migration between accounts.
  link: [Create the new hosted zone in the account](../facts/route53.md#route53-migrate-hosted-zone-new-zone-copy-records)
  link: [migrate records from an AWS account to another](../facts/route53.md#route53-migrate-hosted-zone-new-zone-copy-records)
route53-migrate-hosted-zone-only-for-domain-you-administer
  claim: You can create a hosted zone only for a domain that you have permission to administer.
  scope: hosted zone.
  link: [a domain that you have permission to administer](../facts/route53.md#route53-migrate-hosted-zone-only-for-domain-you-administer)
route53-migrate-in-use-monitor-and-switch-back
  claim: After you change the name servers, monitor traffic for the domain, including website or application traffic and email. If the traffic slows or stops, use the method of the previous DNS service to change the name servers back to the previous name servers, then determine what went wrong. If the traffic is unaffected, change the TTL for the NS record back to a higher value.
  scope: DNS migration of a domain in use.
  link: [back to the previous name servers](../facts/route53.md#route53-migrate-in-use-monitor-and-switch-back)
route53-migrate-in-use-recreate-records-in-new-zone
  claim: When you migrate DNS service for a domain that is in use, you reproduce your current DNS configuration in Route 53: you create a hosted zone with the same name as your domain and create records in it.
  scope: DNS migration of a domain in use.
  link: [the same name as your domain](../facts/route53.md#route53-migrate-in-use-recreate-records-in-new-zone)
  link: [you reproduce your current DNS configuration in Route 53](../facts/route53.md#route53-migrate-in-use-recreate-records-in-new-zone)
route53-migrate-in-use-zone-file-import
  claim: If your current DNS configuration is complex, you can get a zone file from your current DNS provider and import it into Route 53. Not all DNS providers offer zone files.
  scope: DNS migration.
  link: [get a zone file from the current DNS service provider and import it into Route 53](../facts/route53.md#route53-migrate-in-use-zone-file-import)
route53-migrate-lower-ns-ttl-60-to-900-wait-two-days
  claim: When you migrate DNS service for a domain that is in use to Amazon Route 53, the guide recommends setting the NS record TTL to a value between 60 seconds and 900 seconds (15 minutes), then waiting two days after you lowered the TTL so that the migration happens all at one time.
  scope: NS record TTL during a DNS migration to Route 53.
  link: [a value between 60 seconds and 900 seconds](../facts/route53.md#route53-migrate-lower-ns-ttl-60-to-900-wait-two-days)
  link: [two days after you lowered the TTL](../facts/route53.md#route53-migrate-lower-ns-ttl-60-to-900-wait-two-days)
route53-migrate-lower-ns-ttl-both-providers
  claim: Lowering the TTL of the NS record, both with your current DNS service provider and with Route 53, reduces downtime for your domain if you find a problem while migrating DNS to Route 53.
  scope: DNS migration.
  link: [Lowering the TTL for the NS record](../facts/route53.md#route53-migrate-lower-ns-ttl-both-providers)
  link: [reduces downtime for your domain](../facts/route53.md#route53-migrate-lower-ns-ttl-both-providers)
route53-migrate-lower-ns-ttl-else-two-days-down
  claim: If you do not lower the NS record TTL before a DNS migration and something goes wrong, your domain could be unavailable on the internet for up to two days.
  scope: per migrated domain; maximum; NS record TTL of two days.
  link: [up to two days](../facts/route53.md#route53-migrate-lower-ns-ttl-else-two-days-down)
route53-multivalue-alias-not-supported
  claim: Multivalue answer alias records are not supported.
  scope: multivalue answer records.
  link: [not supported](../facts/route53.md#route53-multivalue-alias-not-supported)
route53-multivalue-all-unhealthy-up-to-eight
  claim: When all multivalue answer records are unhealthy, Route 53 answers with up to eight unhealthy records.
  scope: per multivalue answer group; maximum.
  link: [up to eight unhealthy records](../facts/route53.md#route53-multivalue-all-unhealthy-up-to-eight)
route53-multivalue-eight-or-fewer-all-returned
  claim: With eight or fewer healthy multivalue answer records, Route 53 answers every DNS query with all of them.
  scope: per multivalue answer group.
  link: [eight or fewer healthy records](../facts/route53.md#route53-multivalue-eight-or-fewer-all-returned)
route53-multivalue-no-health-check-always-healthy
  claim: A multivalue answer record without a health check is always considered healthy.
  scope: per multivalue answer record.
  link: [always considers the record to be healthy](../facts/route53.md#route53-multivalue-no-health-check-always-healthy)
route53-multivalue-one-record-per-resource-up-to-eight
  claim: For multivalue answer routing you create one multivalue answer record for each resource and, optionally, link a health check with each record. Route 53 responds with up to eight healthy records and gives different answers to different DNS resolvers.
  scope: multivalue answer routing; maximum.
  link: [up to eight healthy records](../facts/route53.md#route53-multivalue-one-record-per-resource-up-to-eight)
  link: [one multivalue answer record for each resource](../facts/route53.md#route53-multivalue-one-record-per-resource-up-to-eight)
  say: up to eight healthy records
route53-multivalue-purpose-not-lb-substitute
  claim: Multivalue answer routing returns multiple values, such as IP addresses, in response to DNS queries and checks the health of each resource, returning only values for healthy resources. It is not a substitute for a load balancer.
  scope: multivalue answer routing.
  link: [returns only values for healthy resources](../facts/route53.md#route53-multivalue-purpose-not-lb-substitute)
  link: [This isn't a substitute for a load balancer](../facts/route53.md#route53-multivalue-purpose-not-lb-substitute)
route53-multivalue-recommended-eight-within-512
  claim: To keep DNS responses within 512 bytes, AWS recommends multivalue answer routing, which this page says chooses eight healthy random IP addresses.
  scope: per multivalue answer group; The routing policy page itself says up to eight healthy records.
  link: [eight healthy random IP addresses](../facts/route53.md#route53-multivalue-recommended-eight-within-512)
route53-multivalue-record-type-not-ns-cname
  claim: A multivalue answer record can have any record type except NS or CNAME.
  scope: per multivalue answer record.
  link: [except NS or CNAME](../facts/route53.md#route53-multivalue-record-type-not-ns-cname)
route53-multivalue-up-to-eight-healthy
  claim: Multivalue answer routing returns up to eight healthy records per DNS query and gives different answers to different resolvers.
  scope: per DNS query; maximum; not adjustable.
  link: [up to eight healthy records](../facts/route53.md#route53-multivalue-up-to-eight-healthy)
route53-mx-record-mail-servers-priority
  claim: An MX record specifies the names of your mail servers and, if you have two or more, the priority order. The server with the lowest priority value takes precedence.
  scope: MX record.
  link: [specifies the names of your mail servers](../facts/route53.md#route53-mx-record-mail-servers-priority)
  link: [lowest value for the priority takes precedence](../facts/route53.md#route53-mx-record-mail-servers-priority)
route53-name-server-returns-value-from-hosted-zone
  claim: A Route 53 name server looks in the hosted zone for the record, gets the associated value, such as the IP address of a web server, and returns it to the DNS resolver.
  scope: DNS resolution.
  link: [example.com hosted zone for the www.example.com record](../facts/route53.md#route53-name-server-returns-value-from-hosted-zone)
  link: [returns the IP address to the DNS resolver](../facts/route53.md#route53-name-server-returns-value-from-hosted-zone)
route53-no-matching-phz-goes-public
  claim: If no private hosted zone matches the domain name in the request, VPC Resolver forwards the request to a public DNS resolver and the request is resolved as a regular DNS query.
  scope: queries from VPCs associated with a private hosted zone.
  link: [forwards the request to a public DNS resolver](../facts/route53.md#route53-no-matching-phz-goes-public)
  link: [resolved as a regular DNS query](../facts/route53.md#route53-no-matching-phz-goes-public)
route53-no-record-healthy-all-records-considered-healthy
  claim: If none of the records in a group are healthy, Route 53 considers all the records in the group to be healthy and selects one based on the routing policy and the values of each record.
  scope: group of records with health checks.
  link: [considers all the records in the group](../facts/route53.md#route53-no-record-healthy-all-records-considered-healthy)
  link: [selects one based on the routing policy](../facts/route53.md#route53-no-record-healthy-all-records-considered-healthy)
route53-ns-record-delegates-subdomain
  claim: You can create a separate hosted zone for a subdomain and delegate responsibility for it by creating another NS record in the hosted zone for the root domain.
  scope: subdomain delegation.
  link: [create a separate hosted zone for a subdomain](../facts/route53.md#route53-ns-record-delegates-subdomain)
  link: [creating another NS record in the hosted zone](../facts/route53.md#route53-ns-record-delegates-subdomain)
route53-ns-record-identifies-name-servers
  claim: An NS record identifies the name servers for the hosted zone. The most common use is to control how internet traffic is routed for a domain.
  scope: NS record.
  link: [identifies the name servers for the hosted zone](../facts/route53.md#route53-ns-record-identifies-name-servers)
  link: [how internet traffic is routed for a domain](../facts/route53.md#route53-ns-record-identifies-name-servers)
route53-ns-record-only-with-simple-routing
  claim: You can specify an NS record with only the simple routing policy.
  scope: NS records.
  link: [with only simple routing policy](../facts/route53.md#route53-ns-record-only-with-simple-routing)
route53-ns-record-typical-ttl-172800
  claim: The typical TTL setting for an NS record is 172800 seconds, or two days.
  scope: per NS record; default; adjustable; Typical value, not a fixed default.
  link: [172800 seconds](../facts/route53.md#route53-ns-record-typical-ttl-172800)
route53-outposts-and-vpc-resolver-feature-overview
  claim: VPC Resolver gives recursive DNS for your VPCs in AWS Regions, VPCs in AWS Outposts racks, or any other on-premises networks. You create conditional forwarding rules and endpoints to resolve custom names in private hosted zones or in your on-premises DNS servers.
  scope: Route 53 VPC Resolver.
  link: [Get recursive DNS for your Amazon VPCs](../facts/route53.md#route53-outposts-and-vpc-resolver-feature-overview)
  link: [Create conditional forwarding rules and Route 53 endpoints](../facts/route53.md#route53-outposts-and-vpc-resolver-feature-overview)
route53-overlap-private-zones-most-specific
  claim: If two or more private hosted zones have overlapping namespaces, VPC Resolver routes traffic based on the most specific match.
  scope: private hosted zones associated with the same VPC.
  link: [two or more private hosted zones](../facts/route53.md#route53-overlap-private-zones-most-specific)
  link: [most specific match](../facts/route53.md#route53-overlap-private-zones-most-specific)
route53-overlap-public-private-most-specific-match
  claim: If public and private hosted zones have overlapping namespaces, such as example.com and accounting.example.com, VPC Resolver routes traffic based on the most specific match.
  scope: queries from VPCs associated with the private hosted zone.
  link: [based on the most specific match](../facts/route53.md#route53-overlap-public-private-most-specific-match)
  link: [overlapping namespaces](../facts/route53.md#route53-overlap-public-private-most-specific-match)
route53-partition-location-healthy-if-some-checkers-healthy
  claim: During internet partitions, each Route 53 location considers an endpoint healthy when only a portion of reachable health checkers consider it healthy.
  scope: health checking during internet partitions.
  link: [only a portion of reachable health checkers](../facts/route53.md#route53-partition-location-healthy-if-some-checkers-healthy)
route53-phz-answers-only-from-associated-vpc-or-inbound-endpoint
  claim: To get an answer from a private hosted zone, you must run an EC2 instance in one of the associated VPCs or have an inbound endpoint from a hybrid setup. A query from outside the VPCs or the hybrid setup is resolved recursively on the internet.
  scope: private hosted zone.
  link: [running an EC2 instance in one of the associated VPCs](../facts/route53.md#route53-phz-answers-only-from-associated-vpc-or-inbound-endpoint)
  link: [resolved recursively on the internet](../facts/route53.md#route53-phz-answers-only-from-associated-vpc-or-inbound-endpoint)
  link: [an inbound endpoint from a hybrid setup](../facts/route53.md#route53-phz-answers-only-from-associated-vpc-or-inbound-endpoint)
route53-phz-can-edit-ns-record-set-not-recommended
  claim: You can change the NS record set in a private hosted zone and private DNS resolution still works. AWS does not recommend it; if you do, use reserved domain names that are not used by public DNS servers.
  scope: private hosted zone.
  link: [You can change the NS record set](../facts/route53.md#route53-phz-can-edit-ns-record-set-not-recommended)
  link: [We don't recommend doing so](../facts/route53.md#route53-phz-can-edit-ns-record-set-not-recommended)
route53-phz-create-with-one-vpc-associate-more-later
  claim: When you create a private hosted zone, you specify the VPC to associate with it. After you create the hosted zone, you can associate more VPCs with it.
  scope: private hosted zone.
  link: [specify the VPC that you want to associate](../facts/route53.md#route53-phz-create-with-one-vpc-associate-more-later)
  link: [you can associate more VPCs with it](../facts/route53.md#route53-phz-create-with-one-vpc-associate-more-later)
route53-phz-health-checks-routing-policies
  claim: In a private hosted zone you can associate Route 53 health checks only with failover, multivalue answer, weighted, latency, geolocation and geoproximity records.
  scope: records in a private hosted zone.
  link: [failover, multivalue answer, weighted, latency, geolocation, and geoproximity](../facts/route53.md#route53-phz-health-checks-routing-policies)
  link: [can associate Route 53 health checks only with](../facts/route53.md#route53-phz-health-checks-routing-policies)
route53-phz-no-transitive-vpn-access
  claim: Private hosted zones do not support transitive relationships outside the VPC, so you cannot reach resources by their private DNS names from the other side of a VPN connection.
  scope: per private hosted zone.
  link: [do not support transitive relationships](../facts/route53.md#route53-phz-no-transitive-vpn-access)
route53-phz-ns-delegation-supported
  claim: You can create NS records in a private hosted zone to delegate responsibility for a subdomain.
  scope: private hosted zone.
  link: [create NS records in a private hosted zone](../facts/route53.md#route53-phz-ns-delegation-supported)
  link: [delegate responsibility for a subdomain](../facts/route53.md#route53-phz-ns-delegation-supported)
route53-phz-parent-zone-counts-as-match
  claim: When VPC Resolver evaluates whether a private hosted zone matches the domain name in a request, a match is either an identical match or a zone whose name is a parent of the domain name in the request.
  scope: private hosted zone matching.
  link: [parent of the domain name in the request](../facts/route53.md#route53-phz-parent-zone-counts-as-match)
route53-phz-reserved-ns-not-reachable-from-internet
  claim: The name servers of a private hosted zone are reserved and never used by Route 53 public hosted zones. The private hosted zone information is not returned if you directly query the name servers over the internet; instead, VPC Resolver detects queries within a private namespace from the VPC to hosted zone associations and uses direct, private connectivity to reach the private DNS servers.
  scope: private hosted zone name servers.
  link: [reserved and never used by Route 53 public hosted zones](../facts/route53.md#route53-phz-reserved-ns-not-reachable-from-internet)
  link: [directly query the name servers over the internet](../facts/route53.md#route53-phz-reserved-ns-not-reachable-from-internet)
route53-phz-routing-policy-support
  claim: In a private hosted zone you can use simple, failover, geolocation, geoproximity, latency, multivalue answer and weighted routing, but you cannot use IP-based routing.
  scope: Amazon Route 53 private hosted zones.
  link: [cannot use IP-based routing policy for records](../facts/route53.md#route53-phz-routing-policy-support)
route53-phz-unsupported-routing-policies
  claim: A private hosted zone supports the simple, failover, multivalue answer, weighted, latency-based, geolocation and geoproximity routing policies. Creating records with other routing policies in a private hosted zone is not supported.
  scope: records in a private hosted zone.
  link: [using other routing policies is not supported](../facts/route53.md#route53-phz-unsupported-routing-policies)
  link: [You can use the following routing policies](../facts/route53.md#route53-phz-unsupported-routing-policies)
route53-pricing-alias-free-for-listed-aws-services
  claim: Alias A and AAAA records mapped to Elastic Load Balancers, CloudFront distributions, Elastic Beanstalk environments, API Gateways, VPC endpoints, S3 website buckets, App Runner, AppSync, OpenSearch, Lightsail and Global Accelerator do not incur a query charge.
  scope: Amazon Route 53 alias A/AAAA queries.
  link: [do not incur a charge](../facts/route53.md#route53-pricing-alias-free-for-listed-aws-services)
route53-pricing-alias-free-when-name-type-match-and-target-aws
  claim: DNS queries are free when both of the following are true: the domain name and record type in the query match an alias record, and the alias target is an AWS resource other than another Route 53 record.
  scope: Amazon Route 53 alias queries.
  link: [match an alias record](../facts/route53.md#route53-pricing-alias-free-when-name-type-match-and-target-aws)
  link: [an AWS resource other than another Route 53 record](../facts/route53.md#route53-pricing-alias-free-when-name-type-match-and-target-aws)
route53-pricing-alias-to-record-in-zone-standard-rate
  claim: Amazon Route 53 charges the standard rate for a query that matches an alias record whose target is a non-alias record in the same hosted zone, but a chain of alias records that ends at an AWS resource such as an Elastic Load Balancer is free.
  scope: Amazon Route 53 alias queries.
  link: [We charge the standard rate](../facts/route53.md#route53-pricing-alias-to-record-in-zone-standard-rate)
  link: [a chain of alias records](../facts/route53.md#route53-pricing-alias-to-record-in-zone-standard-rate)
route53-pricing-authoritative-query-logs-cloudwatch
  claim: Amazon Route 53 does not charge for authoritative DNS query logs, but when you configure DNS query logging you incur Amazon CloudWatch charges in the US East (Virginia) Region for ingestion, archival storage and analysis.
  scope: Amazon Route 53 public DNS query logging.
  link: [Route 53 does not charge for authoritative DNS query logs](../facts/route53.md#route53-pricing-authoritative-query-logs-cloudwatch)
  link: [CloudWatch charges in the US East (Virginia) Region](../facts/route53.md#route53-pricing-authoritative-query-logs-cloudwatch)
route53-pricing-console-s3-list-calls
  claim: Using the Route 53 console can send API calls to S3, for example to identify alias record targets, and depending on how often you do this the S3 LIST requests may appear in your S3 bill.
  scope: Amazon Route 53 console and Amazon S3 API calls.
  link: [may cause charges to appear in your S3 bill as LIST requests](../facts/route53.md#route53-pricing-console-s3-list-calls)
route53-pricing-dns-firewall-dimensions
  claim: Resolver DNS Firewall charges for DNS queries originating from within VPCs that have firewall rule group associations (and for queries through inbound Resolver endpoints into them) and a fee for each domain name stored in a domain list, with no domain name fee for managed domain lists. Rule groups that contain DNS Firewall Advanced rules add an hourly fee for each rule group, per VPC association in an AWS Region.
  scope: Resolver DNS Firewall.
  link: [charge for DNS queries originating from within VPCs](../facts/route53.md#route53-pricing-dns-firewall-dimensions)
  link: [each domain name stored in a domain list](../facts/route53.md#route53-pricing-dns-firewall-dimensions)
  link: [hourly fee for each DNS Firewall rule group](../facts/route53.md#route53-pricing-dns-firewall-dimensions)
route53-pricing-dnssec-no-fee-but-kms
  claim: Amazon Route 53 does not charge to enable DNSSEC signing on public hosted zones or DNSSEC validation for Route 53 Resolver, but DNSSEC signing incurs AWS Key Management Service (KMS) charges for storing the private key and using it to sign your zones.
  scope: DNSSEC signing for public hosted zones.
  link: [you incur AWS Key Management Service (KMS) charges](../facts/route53.md#route53-pricing-dnssec-no-fee-but-kms)
route53-pricing-domains-annual-by-tld
  claim: Domain name prices vary by top-level domain (TLD), domain names are registered in annual increments, and the default limit is 20 domain name registrations per account.
  scope: per domain per year; default.
  link: [Pricing for domain names varies by TLD](../facts/route53.md#route53-pricing-domains-annual-by-tld)
  link: [default limit of 20 domain name registrations per account](../facts/route53.md#route53-pricing-domains-annual-by-tld)
route53-pricing-health-check-aws-vs-non-aws-endpoints
  claim: Amazon Route 53 health checks are priced per health check per month, separately for AWS endpoints and non-AWS endpoints, and calculated and metric based health checks are billed as health checks of an AWS endpoint.
  scope: per health check per month.
  link: [AWS Endpoints](../facts/route53.md#route53-pricing-health-check-aws-vs-non-aws-endpoints)
  link: [Non-AWS Endpoints](../facts/route53.md#route53-pricing-health-check-aws-vs-non-aws-endpoints)
route53-pricing-health-check-optional-features
  claim: Optional health check features, which include HTTPS, string matching, fast request interval and latency measurement, add a charge per optional feature per month, with separate rates for AWS endpoints and non-AWS endpoints.
  scope: per optional health check feature per month.
  link: [HTTPS, string matching; fast request interval, and latency](../facts/route53.md#route53-pricing-health-check-optional-features)
route53-pricing-health-checks-first-50-aws-endpoints-free
  claim: New and existing customers can create up to 50 health checks for AWS endpoints within or linked to the same AWS account at no charge, and health checks of Elastic Load Balancing resources and S3 website bucket endpoints are not billed.
  scope: per AWS account; maximum.
  link: [up to 50 health checks for AWS endpoints](../facts/route53.md#route53-pricing-health-checks-first-50-aws-endpoints-free)
  link: [You are not billed for health checks](../facts/route53.md#route53-pricing-health-checks-first-50-aws-endpoints-free)
route53-pricing-hosted-zone-deleted-in-12-hours-free
  claim: To allow testing, a hosted zone deleted within 12 hours of creation is not charged for the zone, but queries on its public hosted zone are still charged.
  scope: per hosted zone.
  link: [deleted within 12 hours of creation](../facts/route53.md#route53-pricing-hosted-zone-deleted-in-12-hours-free)
route53-pricing-hosted-zone-includes-10000-records
  claim: A hosted zone includes up to 10,000 records; each record above 10,000 per hosted zone is charged a monthly fee.
  scope: per hosted zone; maximum; Each record above 10,000 per hosted zone is charged per month.
  link: [up to 10,000 records](../facts/route53.md#route53-pricing-hosted-zone-includes-10000-records)
route53-pricing-hosted-zone-monthly-not-prorated
  claim: Each Amazon Route 53 hosted zone is billed per month, at a lower price for hosted zones beyond the first 25; the monthly price is not prorated for partial months, and the zone is charged when it is created and on the first day of each later month.
  scope: per hosted zone per month.
  link: [not prorated for partial months](../facts/route53.md#route53-pricing-hosted-zone-monthly-not-prorated)
  link: [for the first 25 hosted zones](../facts/route53.md#route53-pricing-hosted-zone-monthly-not-prorated)
route53-pricing-missing-record-and-type-mismatch-charged
  claim: Amazon Route 53 charges the standard rate for queries for a record that does not exist and for queries whose name matches a record but whose type does not, so creating both A and AAAA records is recommended where applicable.
  scope: Amazon Route 53 DNS queries.
  link: [Queries for a record that doesn't exist](../facts/route53.md#route53-pricing-missing-record-and-type-mismatch-charged)
  link: [create both A and AAAA records](../facts/route53.md#route53-pricing-missing-record-and-type-mismatch-charged)
route53-pricing-pay-per-zone-and-query-no-minimums
  claim: There are no contracts or minimum commitments for Amazon Route 53; you pay only for the hosted zones that you configure and the number of DNS queries that Route 53 answers.
  scope: Amazon Route 53 DNS.
  link: [pay only for the hosted zones](../facts/route53.md#route53-pricing-pay-per-zone-and-query-no-minimums)
route53-pricing-private-zone-queries-no-charge
  claim: Queries on private hosted zones are provided at no additional cost to Amazon Route 53 customers.
  scope: DNS queries on private hosted zones.
  link: [provided at no additional cost](../facts/route53.md#route53-pricing-private-zone-queries-no-charge)
route53-pricing-profiles-per-account-hour-and-associations
  claim: Route 53 Profiles are billed at an hourly rate per AWS account that covers the first 100 Profile-VPC associations in an AWS Region, with a per-association hourly charge beyond those 100.
  scope: per AWS account per Region per hour.
  link: [up to 100 Profile-VPC associations](../facts/route53.md#route53-pricing-profiles-per-account-hour-and-associations)
route53-pricing-query-types-four-rates
  claim: The Route 53 usage report has four query types: standard queries (records with failover, multivalue answer and weighted routing policies) as Intra-AWS-DNS-Queries, latency-based routing queries as Intra-AWS-LBR-Queries, geo routing queries (geolocation and geoproximity) as Intra-AWS-Geo-Queries, and IP-based routing queries as Intra-AWS-Cidr-Queries.
  scope: query types on the Route 53 usage report.
  link: [Intra-AWS-DNS-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-LBR-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-Geo-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-Cidr-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
route53-pricing-resolver-endpoint-eni-hour
  claim: A Route 53 Resolver endpoint needs two or more IP addresses, each corresponding to one elastic network interface (ENI), and endpoints are billed per ENI per hour, and a single outbound endpoint can be used by multiple VPCs from multiple accounts in the same Region; only queries that pass through an inbound or outbound endpoint are charged.
  scope: per Resolver endpoint ENI per hour and per million endpoint queries.
  link: [requires two or more IP addresses](../facts/route53.md#route53-pricing-resolver-endpoint-eni-hour)
  link: [Only queries that pass through a Route 53 Resolver endpoint](../facts/route53.md#route53-pricing-resolver-endpoint-eni-hour)
route53-pricing-resolver-query-logs-destination-charges
  claim: Route 53 does not charge for VPC Resolver query logs, but the CloudWatch, S3 or Firehose charges of the chosen log destination apply.
  scope: VPC Resolver query logging.
  link: [Route 53 does not charge for VPC Resolver query logs](../facts/route53.md#route53-pricing-resolver-query-logs-destination-charges)
route53-pricing-traffic-flow-per-policy-record
  claim: Traffic Flow is billed by policy record, which is a traffic policy associated with a domain name; the monthly price is prorated for partial months and a traffic policy that is not associated with a domain name through a policy record is not charged.
  scope: per Traffic Flow policy record per month.
  link: [You create a policy record](../facts/route53.md#route53-pricing-traffic-flow-per-policy-record)
route53-private-dns-defined
  claim: Private DNS is a local version of DNS that routes traffic for a domain and its subdomains to EC2 instances inside one or more VPCs.
  scope: private hosted zone.
  link: [A local version of the Domain Name System](../facts/route53.md#route53-private-dns-defined)
  link: [within one or more Amazon virtual private clouds](../facts/route53.md#route53-private-dns-defined)
route53-private-hosted-zone-defined
  claim: A private hosted zone holds information about how DNS queries are answered for a domain and its subdomains within one or more VPCs that you create with Amazon VPC.
  scope: private hosted zone.
  link: [DNS queries for a domain and its subdomains](../facts/route53.md#route53-private-hosted-zone-defined)
  link: [within one or more VPCs](../facts/route53.md#route53-private-hosted-zone-defined)
route53-profiles-local-settings-win
  claim: When a DNS query matches both a Resolver rule for a private hosted zone directly associated with the VPC and one associated through the Profile, the local DNS settings take precedence; for a conflicting domain name the most specific one wins.
  scope: Route 53 Profiles and local VPC DNS settings.
  link: [the local DNS settings take precedence](../facts/route53.md#route53-profiles-local-settings-win)
  link: [the most specific one wins](../facts/route53.md#route53-profiles-local-settings-win)
route53-profiles-one-per-vpc
  claim: You can associate one Profile per VPC, and the number of resources you can associate per Profile varies.
  scope: per VPC; maximum; not adjustable; The number of resources per Profile varies; see the Profiles quotas..
  link: [one Profile per VPC](../facts/route53.md#route53-profiles-one-per-vpc)
route53-profiles-share-dns-config-across-vpcs-accounts
  claim: With Route 53 Profiles you can apply and manage DNS-related Route 53 configurations across many VPCs and different AWS accounts, and you can share a Profile with AWS accounts in the same Regions by using AWS RAM.
  scope: Route 53 Profiles.
  link: [across many VPCs and in different AWS accounts](../facts/route53.md#route53-profiles-share-dns-config-across-vpcs-accounts)
  link: [by using AWS RAM](../facts/route53.md#route53-profiles-share-dns-config-across-vpcs-accounts)
route53-profiles-supported-resources
  claim: The resources you can associate to a Route 53 Profile are private hosted zones, Resolver rules (forwarding and system), DNS Firewall rule groups, interface VPC endpoints and VPC Resolver query logging configurations.
  scope: Route 53 Profiles; Interface VPC endpoints were added 2025-04-28 and query logging configurations 2025-11-17..
  link: [Private hosted zones](../facts/route53.md#route53-profiles-supported-resources)
  link: [Resolver rules](../facts/route53.md#route53-profiles-supported-resources)
  link: [DNS Firewall rule groups](../facts/route53.md#route53-profiles-supported-resources)
route53-ptr-record-ip-to-name
  claim: A PTR record maps an IP address to the corresponding domain name.
  scope: PTR record.
  link: [IP address to the corresponding domain name](../facts/route53.md#route53-ptr-record-ip-to-name)
route53-public-hosted-zone-two-ways
  claim: A public hosted zone holds information about how to route internet traffic for a domain and its subdomains. You get one when you register a domain with Route 53, or you create it yourself when you transfer DNS service for an existing domain to Route 53.
  scope: public hosted zone.
  link: [route traffic on the internet](../facts/route53.md#route53-public-hosted-zone-two-ways)
  link: [Route 53 creates a hosted zone for you automatically](../facts/route53.md#route53-public-hosted-zone-two-ways)
  link: [creating a hosted zone for the domain](../facts/route53.md#route53-public-hosted-zone-two-ways)
route53-public-query-log-group-must-be-us-east-1
  claim: The CloudWatch Logs log group for public DNS query logging must be in the US East (N. Virginia) Region.
  scope: public DNS query logging.
  link: [be in the US East (N. Virginia) Region](../facts/route53.md#route53-public-query-log-group-must-be-us-east-1)
  link: [log group must be in the US East](../facts/route53.md#route53-public-query-log-group-must-be-us-east-1)
route53-public-query-logs-go-to-cloudwatch-logs
  claim: After you configure public DNS query logging, Route 53 sends the logs to CloudWatch Logs.
  scope: public DNS query logging.
  link: [Route 53 will send logs to CloudWatch Logs](../facts/route53.md#route53-public-query-logs-go-to-cloudwatch-logs)
  link: [After you configure query logging](../facts/route53.md#route53-public-query-logs-go-to-cloudwatch-logs)
route53-public-query-logs-only-queries-reaching-route53
  claim: Public query logs contain only the queries that DNS resolvers send to Route 53. A resolver that cached the response keeps answering from its cache until the TTL expires, so query logs might not capture every DNS query.
  scope: public DNS query logging.
  link: [only the queries that DNS resolvers send to Route 53](../facts/route53.md#route53-public-query-logs-only-queries-reaching-route53)
  link: [might not capture every DNS query](../facts/route53.md#route53-public-query-logs-only-queries-reaching-route53)
route53-public-zone-creates-ns-and-soa
  claim: For each public hosted zone that you create, Amazon Route 53 automatically creates a name server (NS) record and a start of authority (SOA) record.
  scope: per public hosted zone.
  link: [automatically creates a name server (NS) record](../facts/route53.md#route53-public-zone-creates-ns-and-soa)
route53-quota-calculated-child-health-checks
  claim: One calculated health check can monitor up to 255 child health checks.
  scope: per calculated health check; maximum; not adjustable.
  link: [255 child health checks](../facts/route53.md#route53-quota-calculated-child-health-checks)
route53-quota-changerrsets-resourcerecord-elements
  claim: A ChangeResourceRecordSets request cannot contain more than 1,000 ResourceRecord elements, including alias records.
  scope: per ChangeResourceRecordSets request; maximum; not adjustable; Each ResourceRecord element is counted twice when the Action is UPSERT.
  link: [1,000 ResourceRecord elements](../facts/route53.md#route53-quota-changerrsets-resourcerecord-elements)
route53-quota-changerrsets-upsert-counted-twice
  claim: When the Action of a ChangeResourceRecordSets request is UPSERT, each ResourceRecord element counts twice toward the limit.
  scope: per ChangeResourceRecordSets request; Action is UPSERT.
  link: [counted twice](../facts/route53.md#route53-quota-changerrsets-upsert-counted-twice)
route53-quota-changerrsets-value-characters
  claim: The sum of the characters, including spaces, in all Value elements of a ChangeResourceRecordSets request cannot exceed 32,000 characters.
  scope: per ChangeResourceRecordSets request; maximum; not adjustable; Each character counts twice when the Action is UPSERT.
  link: [32,000 characters](../facts/route53.md#route53-quota-changerrsets-value-characters)
route53-quota-cidr-blocks-per-collection
  claim: One CIDR collection can hold 1000 CIDR blocks, and you can request a higher quota.
  scope: per CIDR collection; default; adjustable.
  link: [1000 per CIDR collection](../facts/route53.md#route53-quota-cidr-blocks-per-collection)
route53-quota-cidr-collections
  claim: You can have 5 CIDR collections per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [5 per AWS account](../facts/route53.md#route53-quota-cidr-collections)
route53-quota-dnsfw-domain-lists-per-region
  claim: You can have 1000 DNS Firewall domain lists per AWS account per Region, and you can request a higher quota.
  scope: per account, per Region; default; adjustable.
  link: [1000 DNS Firewall domain lists](../facts/route53.md#route53-quota-dnsfw-domain-lists-per-region)
route53-quota-dnsfw-domains-across-lists
  claim: You can specify at most 100,000 domains across all domain lists for a single account per AWS Region, and you can request a higher quota.
  scope: across all domain lists, per account, per Region; default; adjustable.
  link: [100,000 domains](../facts/route53.md#route53-quota-dnsfw-domains-across-lists)
route53-quota-dnsfw-domains-per-s3-file
  claim: A single Amazon S3 file for DNS Firewall can hold 250,000 domains, and you can request a higher quota.
  scope: per S3 file, per account, per Region; default; adjustable.
  link: [250,000 domains](../facts/route53.md#route53-quota-dnsfw-domains-per-s3-file)
route53-quota-dnsfw-rule-groups-per-region
  claim: You can have 1,000 DNS Firewall rule groups per AWS account per Region, and you can request a higher quota.
  scope: per account, per Region; default; adjustable.
  link: [1,000 DNS Firewall rule groups](../facts/route53.md#route53-quota-dnsfw-rule-groups-per-region)
route53-quota-dnsfw-rule-groups-per-vpc
  claim: Each VPC can have 5 DNS Firewall rule groups associated, for a single account per AWS Region.
  scope: per VPC, per account, per Region; maximum; not adjustable.
  link: [5 DNS Firewall rule groups](../facts/route53.md#route53-quota-dnsfw-rule-groups-per-vpc)
route53-quota-dnsfw-rules-per-group
  claim: A DNS Firewall rule group can hold 100 rules per account per Region, and you can request a higher quota.
  scope: per rule group, per account, per Region; default; adjustable.
  link: [100 rules](../facts/route53.md#route53-quota-dnsfw-rules-per-group)
route53-quota-domains-per-account
  claim: For new customers as of March 2021 the default quota is 20 domains per AWS account; an existing account whose default limit is 50 keeps 50. You can request a higher quota.
  scope: per AWS account; default; adjustable; 20 for new customers as of March 2021; an existing account at 50 stays at 50.
  link: [20 domains per AWS account](../facts/route53.md#route53-quota-domains-per-account)
  link: [it will remain at 50](../facts/route53.md#route53-quota-domains-per-account)
route53-quota-health-check-response-headers-length
  claim: The maximum total length of headers in the response to a health check request is 16,384 bytes (16K).
  scope: per health check response; maximum; not adjustable.
  link: [16,384 bytes](../facts/route53.md#route53-quota-health-check-response-headers-length)
route53-quota-health-checks-per-account
  claim: You can have 200 active health checks per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [200 active health checks](../facts/route53.md#route53-quota-health-checks-per-account)
route53-quota-hosted-zones-per-account
  claim: The initial quota is 500 hosted zones per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [500 per AWS account](../facts/route53.md#route53-quota-hosted-zones-per-account)
route53-quota-ksk-per-hosted-zone
  claim: You can create at most 2 key signing keys (KSK) per hosted zone.
  scope: per hosted zone; maximum; not adjustable.
  link: [2 key signing keys](../facts/route53.md#route53-quota-ksk-per-hosted-zone)
route53-quota-private-zones-per-vpc
  claim: There is no quota on the number of private hosted zones that you can associate a VPC with.
  scope: per VPC; maximum; not adjustable; The page states no quota.
  link: [No quota](../facts/route53.md#route53-quota-private-zones-per-vpc)
route53-quota-private-zones-vpc-1500-example
  claim: With three accounts that each have 500 private hosted zones, you can link one VPC with all 1,500 private hosted zones.
  scope: per VPC; maximum; not adjustable; Example: three accounts, each at the default quota of 500 hosted zones.
  link: [1,500 private hosted zones](../facts/route53.md#route53-quota-private-zones-vpc-1500-example)
route53-quota-profile-dnsfw-rule-groups
  claim: A Profile can hold 5 DNS Firewall rule groups.
  scope: per Profile; maximum; not adjustable.
  link: [5 DNS Firewall rule groups](../facts/route53.md#route53-quota-profile-dnsfw-rule-groups)
route53-quota-profile-private-hosted-zones
  claim: A Profile can hold 5000 private hosted zones, and you can request a higher quota.
  scope: per Profile; default; adjustable.
  link: [5000 private hosted zones](../facts/route53.md#route53-quota-profile-private-hosted-zones)
route53-quota-profile-query-log-configs
  claim: A Profile can have 2 VPC Resolver query logging configurations.
  scope: per Profile; maximum; not adjustable.
  link: [2 VPC Resolver query logging configurations](../facts/route53.md#route53-quota-profile-query-log-configs)
route53-quota-profile-resolver-rules
  claim: A Profile can hold 1000 Resolver rules, and you can request a higher quota.
  scope: per Profile; default; adjustable.
  link: [1000 Resolver rules](../facts/route53.md#route53-quota-profile-resolver-rules)
route53-quota-profile-vpc-associations
  claim: Up to 1000 VPCs can be associated to a Profile, and you can request a higher quota.
  scope: per Profile; default; adjustable.
  link: [1000 VPCs](../facts/route53.md#route53-quota-profile-vpc-associations)
route53-quota-profiles-per-account-region
  claim: You can have 5 Profiles per AWS account in a Region, and you can request a higher quota.
  scope: per AWS account, per Region; default; adjustable.
  link: [5 Profiles](../facts/route53.md#route53-quota-profiles-per-account-region)
route53-quota-query-log-config-per-hosted-zone
  claim: A hosted zone can have 1 query log configuration.
  scope: per hosted zone; maximum; not adjustable.
  link: [1 per hosted zone](../facts/route53.md#route53-quota-query-log-config-per-hosted-zone)
route53-quota-records-per-hosted-zone
  claim: A hosted zone can hold 10,000 records by default; you can request a higher quota, and an additional charge applies for more than 10,000 records.
  scope: per hosted zone; default; adjustable; An additional charge applies for a quota greater than 10,000 records in a hosted zone.
  link: [10,000 records](../facts/route53.md#route53-quota-records-per-hosted-zone)
route53-quota-records-per-record-set
  claim: One record set can hold up to 400 records.
  scope: per record set; maximum; not adjustable.
  link: [400 per record set](../facts/route53.md#route53-quota-records-per-record-set)
route53-quota-resolver-api-five-per-second
  claim: VPC Resolver API requests are limited to five per second per AWS account per Region.
  scope: per AWS account, per Region; maximum; not adjustable.
  link: [Five requests per second](../facts/route53.md#route53-quota-resolver-api-five-per-second)
route53-quota-resolver-endpoint-ip-udp-qps
  claim: Each IP address in a VPC Resolver endpoint can process up to 10,000 UDP DNS queries per second (QPS).
  scope: per IP address in an endpoint; maximum; not adjustable; The actual QPS varies by query type, response size, target name server health, response times, round trip latency and protocol.
  link: [10,000 UDP DNS queries per second](../facts/route53.md#route53-quota-resolver-endpoint-ip-udp-qps)
route53-quota-resolver-endpoints-per-region
  claim: You can have 4 VPC Resolver endpoints per AWS Region per AWS account, and you can request a higher quota.
  scope: per AWS account, per Region; default; adjustable.
  link: [4 per AWS account](../facts/route53.md#route53-quota-resolver-endpoints-per-region)
route53-quota-resolver-ips-per-endpoint
  claim: One VPC Resolver endpoint can have up to 6 IP addresses, and you can request a higher quota.
  scope: per endpoint; default; adjustable.
  link: [6 IP addresses](../facts/route53.md#route53-quota-resolver-ips-per-endpoint)
route53-quota-resolver-ips-per-rule
  claim: One VPC Resolver rule can have up to 6 IP addresses.
  scope: per rule; maximum; not adjustable.
  link: [6 IP addresses](../facts/route53.md#route53-quota-resolver-ips-per-rule)
route53-quota-resolver-outpost-gen2-qps
  claim: Resolver on second-generation AWS Outposts handles up to 75,000 DNS queries per second.
  scope: Resolver on second-generation AWS Outposts; maximum; not adjustable.
  link: [Up to 75,000](../facts/route53.md#route53-quota-resolver-outpost-gen2-qps)
route53-quota-resolver-outpost-instances
  claim: Resolver on first-generation AWS Outposts has an instance limit of 6, with a minimum of 4 required.
  scope: Resolver on first-generation AWS Outposts; maximum; not adjustable.
  link: [6 (with a minimum of 4 required)](../facts/route53.md#route53-quota-resolver-outpost-instances)
route53-quota-resolver-query-log-configs-per-region
  claim: You can have 20 query log configurations per AWS Region for VPC Resolver, and you can request a higher quota.
  scope: per AWS Region; default; adjustable.
  link: [20 query log configurations](../facts/route53.md#route53-quota-resolver-query-log-configs-per-region)
route53-quota-resolver-query-log-vpc-associations-region
  claim: The quota is 100 query log configuration VPC associations per AWS Region, and you can request a higher quota.
  scope: per AWS Region; default; adjustable; The quota is Regional and applies across all query log configurations in the Region.
  link: [100 query log configuration VPC associations](../facts/route53.md#route53-quota-resolver-query-log-vpc-associations-region)
route53-quota-resolver-rule-vpc-associations
  claim: You can have 2000 associations between Resolver rules and VPCs per AWS account per Region, and you can request a higher quota.
  scope: per AWS account, per Region; default; adjustable.
  link: [2000 per AWS account](../facts/route53.md#route53-quota-resolver-rule-vpc-associations)
route53-quota-resolver-rules-per-region
  claim: You can have 1000 VPC Resolver rules per AWS account per Region, and you can request a higher quota.
  scope: per AWS account, per Region; default; adjustable.
  link: [1000 per AWS account](../facts/route53.md#route53-quota-resolver-rules-per-region)
route53-quota-reusable-delegation-set-zones
  claim: One reusable delegation set can be used by 100 hosted zones, and you can request a higher quota.
  scope: per reusable delegation set; maximum; adjustable.
  link: [100 hosted zones](../facts/route53.md#route53-quota-reusable-delegation-set-zones)
route53-quota-reusable-delegation-sets-per-account
  claim: You can have 100 reusable delegation sets per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [100 per AWS account](../facts/route53.md#route53-quota-reusable-delegation-sets-per-account)
route53-quota-same-name-type-geoproximity-records
  claim: Geoproximity routing can have up to 30 records that have the same name and type.
  scope: per name and type; maximum; not adjustable; Applies to geoproximity records.
  link: [30 records](../facts/route53.md#route53-quota-same-name-type-geoproximity-records)
route53-quota-same-name-type-routing-records
  claim: Geolocation, latency, multivalue answer, weighted and IP-based routing can have up to 100 records that have the same name and type.
  scope: per name and type; maximum; not adjustable; Applies to geolocation, latency, multivalue answer, weighted and IP-based records.
  link: [100 records](../facts/route53.md#route53-quota-same-name-type-routing-records)
route53-quota-traffic-policies-per-account
  claim: You can have 50 traffic policies per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [50 per AWS account](../facts/route53.md#route53-quota-traffic-policies-per-account)
route53-quota-traffic-policy-records
  claim: You can have 5 traffic policy records per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [5 per AWS account](../facts/route53.md#route53-quota-traffic-policy-records)
route53-quota-traffic-policy-versions
  claim: One traffic policy can have 1,000 versions.
  scope: per traffic policy; maximum; not adjustable.
  link: [1,000 per traffic policy](../facts/route53.md#route53-quota-traffic-policy-versions)
route53-quota-view-in-us-east-1
  claim: To view Route 53 quotas or request higher ones in Service Quotas, you must change the Region to US East (N. Virginia).
  scope: Service Quotas console for Route 53; VPC Resolver quotas are viewed in the applicable Region instead.
  link: [US East (N. Virginia)](../facts/route53.md#route53-quota-view-in-us-east-1)
route53-quota-vpc-association-authorizations
  claim: You can create up to 1000 authorizations that let you associate VPCs created by one account with a hosted zone created by another account.
  scope: cross-account VPC association authorizations; maximum; not adjustable.
  link: [1000 authorizations](../facts/route53.md#route53-quota-vpc-association-authorizations)
route53-quota-vpcs-per-private-zone
  claim: You can associate 300 Amazon VPCs with one private hosted zone, and the page recommends Route 53 Profiles if you want more than 300 associations.
  scope: per private hosted zone; maximum; not adjustable; The page shows no quota-increase link for this row; it recommends Route 53 Profiles for more than 300 associations.
  link: [300 Amazon VPCs](../facts/route53.md#route53-quota-vpcs-per-private-zone)
route53-record-defined
  claim: A record (DNS record) is an object in a hosted zone that defines how traffic is routed for a domain or a subdomain.
  scope: record in a hosted zone.
  link: [An object in a hosted zone](../facts/route53.md#route53-record-defined)
  link: [how you want to route traffic](../facts/route53.md#route53-record-defined)
route53-record-name-ends-with-zone-name
  claim: The name of every record in a hosted zone must end with the name of the hosted zone. In a zone named example.com, every record name must end in example.com.
  scope: every record in a hosted zone.
  link: [end with the name of the hosted zone](../facts/route53.md#route53-record-name-ends-with-zone-name)
  link: [all record names must end in example.com](../facts/route53.md#route53-record-name-ends-with-zone-name)
route53-record-set-permissions-iam-conditions
  claim: IAM policy conditions let you grant permissions on a single resource record set, all record sets of a specific record type, record sets whose names contain a specific string, and any or all of the CREATE, UPSERT and DELETE actions.
  scope: resource record set permissions.
  link: [route53:ChangeResourceRecordSetsNormalizedRecordNames](../facts/route53.md#route53-record-set-permissions-iam-conditions)
  link: [route53:ChangeResourceRecordSetsRecordTypes](../facts/route53.md#route53-record-set-permissions-iam-conditions)
  link: [route53:ChangeResourceRecordSetsActions](../facts/route53.md#route53-record-set-permissions-iam-conditions)
route53-record-type-determines-resource-type
  claim: The record type usually determines the type of resource that traffic is routed to. For example, you specify MX to route traffic to an email server and A to route traffic to a web server that has an IPv4 address.
  scope: record.
  link: [record type usually determines the type of resource](../facts/route53.md#route53-record-type-determines-resource-type)
  link: [you specify MX for Type](../facts/route53.md#route53-record-type-determines-resource-type)
route53-record-without-health-check-always-healthy
  claim: If a record in a group of records with the same name and type has no associated health check, Route 53 always considers it healthy and always includes it among possible responses.
  scope: records without a health check.
  link: [always considers it healthy](../facts/route53.md#route53-record-without-health-check-always-healthy)
  link: [always includes it among possible responses](../facts/route53.md#route53-record-without-health-check-always-healthy)
route53-registrar-register-and-transfer-domains
  claim: You can register a new domain with Route 53. You can also transfer the registration of existing domains from other registrars to Route 53, or transfer a domain registered with Route 53 to another registrar.
  scope: domain registration.
  link: [you can register it with Amazon Route 53](../facts/route53.md#route53-registrar-register-and-transfer-domains)
  link: [transfer the registration for existing domains from other registrars to Route 53](../facts/route53.md#route53-registrar-register-and-transfer-domains)
route53-rel10-distribute-across-azs-or-regions
  claim: REL10-BP01 says to distribute workload data and resources across multiple Availability Zones or, where necessary, across AWS Regions, and its list of common anti-patterns includes implementing a multi-Region architecture when a multi-AZ architecture would satisfy business requirements.
  scope: Well-Architected REL10-BP01.
  link: [where necessary, across AWS Regions](../facts/route53.md#route53-rel10-distribute-across-azs-or-regions)
  link: [when a multi-AZ architecture would satisfy business requirements](../facts/route53.md#route53-rel10-distribute-across-azs-or-regions)
route53-rel10-dns-route-to-closest-region
  claim: The Well-Architected reliability pillar says you can configure DNS records with Amazon Route 53 to direct traffic to the closest available Region to the user, or use an active/standby configuration with one primary Region.
  scope: Well-Architected REL10-BP01.
  link: [direct traffic to the closest available Region](../facts/route53.md#route53-rel10-dns-route-to-closest-region)
  link: [active/standby configuration](../facts/route53.md#route53-rel10-dns-route-to-closest-region)
route53-rel10-failover-records-short-ttl
  claim: For DNS records used for failover, the Well-Architected reliability pillar says to specify a short time to live (for example, 60 seconds or less) so record caching does not impede recovery, and notes that Amazon Route 53 alias records supply appropriate TTLs for you.
  scope: DNS records used for failover; maximum; adjustable; Applies to non-alias records; alias records supply appropriate TTLs..
  link: [60 seconds or less](../facts/route53.md#route53-rel10-failover-records-short-ttl)
route53-released-elastic-ip-delete-dns-record-dangling
  claim: If you release the Elastic IP address, you must also delete the DNS record that points to it. Otherwise you have a dangling DNS record that an unauthorized user can take over.
  scope: record that points to an Elastic IP address.
  link: [also delete the DNS record pointing to it](../facts/route53.md#route53-released-elastic-ip-delete-dns-record-dangling)
  link: [dangling DNS record that can be taken over](../facts/route53.md#route53-released-elastic-ip-delete-dns-record-dangling)
route53-resilience-primarily-global-some-features-regional
  claim: Route 53 is primarily a global service, but some features support AWS Regions: VPC Resolver endpoints are created in Regions you choose, and health checks can check resources in specific Regions and be run from Regions you specify.
  scope: Route 53.
  link: [Route 53 is primarily a global service](../facts/route53.md#route53-resilience-primarily-global-some-features-regional)
  link: [specify the Regions that you want Route 53 to perform health checks from](../facts/route53.md#route53-resilience-primarily-global-some-features-regional)
route53-resilience-resolver-endpoints-multiple-azs-rules-same-region
  claim: For VPC Resolver hybrid configurations, you create endpoints in the Regions that you choose and specify IP addresses in multiple Availability Zones. For outbound endpoints, you create rules in the same Region where you created the endpoint.
  scope: VPC Resolver endpoints.
  link: [you specify IP addresses in multiple Availability Zones](../facts/route53.md#route53-resilience-resolver-endpoints-multiple-azs-rules-same-region)
  link: [create rules in the same Region](../facts/route53.md#route53-resilience-resolver-endpoints-multiple-azs-rules-same-region)
route53-resolver-add-interfaces-above-50-percent
  claim: If your maximum query rate exceeds 50% of the capacity for any network interface in the endpoint, you can add more network interfaces to increase the endpoint capacity.
  scope: per network interface in an endpoint.
  link: [50% of the capacity](../facts/route53.md#route53-resolver-add-interfaces-above-50-percent)
route53-resolver-autodefined-rule-per-associated-private-hosted-zone
  claim: For each private hosted zone that you associate with a VPC, VPC Resolver creates a rule of type Forward and associates it with the VPC.
  scope: Resolver autodefined rules.
  link: [a rule and associates it with the VPC](../facts/route53.md#route53-resolver-autodefined-rule-per-associated-private-hosted-zone)
  link: [The rule has a type of Forward](../facts/route53.md#route53-resolver-autodefined-rule-per-associated-private-hosted-zone)
route53-resolver-autodefined-rules-created-automatically
  claim: VPC Resolver automatically creates autodefined rules and associates them with your VPCs. Most of these rules apply to the AWS-specific domain names that VPC Resolver answers queries for.
  scope: Resolver autodefined rules.
  link: [VPC Resolver automatically creates autodefined rules](../facts/route53.md#route53-resolver-autodefined-rules-created-automatically)
route53-resolver-autodefined-rules-keep-phz-and-ec2-names-resolving
  claim: For private hosted zones and EC2-specific domain names, autodefined rules make sure that your private hosted zones and EC2 instances continue to resolve if you create conditional forwarding rules for less specific domain names such as "." or "com".
  scope: Resolver autodefined rules.
  link: [autodefined rules make sure that your private hosted zones and EC2 instances continue to resolve](../facts/route53.md#route53-resolver-autodefined-rules-keep-phz-and-ec2-names-resolving)
route53-resolver-autodefined-system-rules-for-reverse-dns
  claim: When enableDnsHostnames and enableDnsSupport are set to true for a VPC, VPC Resolver automatically creates auto-defined system rules for reverse DNS queries.
  scope: Resolver system rules.
  link: [automatically creates auto-defined system rules for reverse DNS](../facts/route53.md#route53-resolver-autodefined-system-rules-for-reverse-dns)
route53-resolver-best-practice-avoid-rule-and-inbound-endpoint-loop
  claim: Prevent routing loops by making sure the same VPC is not associated with both a Resolver rule and its inbound endpoint.
  scope: Resolver endpoints.
  link: [not associated with both a Resolver rule](../facts/route53.md#route53-resolver-best-practice-avoid-rule-and-inbound-endpoint-loop)
route53-resolver-caches-answer-for-ttl-you-set
  claim: The DNS resolver also caches the IP address for a domain for an amount of time that you specify, so that it can respond more quickly the next time someone browses to the domain.
  scope: DNS resolution.
  link: [for an amount of time that you specify](../facts/route53.md#route53-resolver-caches-answer-for-ttl-you-set)
  link: [respond more quickly the next time](../facts/route53.md#route53-resolver-caches-answer-for-ttl-you-set)
route53-resolver-caches-ns-two-days
  claim: After the TLD name server for .com responds with the names of the four Route 53 name servers for example.com, the DNS resolver caches them, and the next time someone browses to example.com the resolver skips steps 3 and 4 (the root and TLD name servers). The name servers are typically cached for two days.
  scope: DNS resolver cache of name servers; default; typical.
  link: [cached for two days](../facts/route53.md#route53-resolver-caches-ns-two-days)
  link: [skips steps 3 and 4](../facts/route53.md#route53-resolver-caches-ns-two-days)
  say: two days
route53-resolver-cidr-plus-two-forwarding-unsupported
  claim: Forwarding private DNS queries from on-premises or other VPC DNS servers to a VPC CIDR+2 address is not supported and can cause unstable results. Use a Resolver inbound endpoint instead.
  scope: forwarding to VPC+2.
  link: [is not supported, and can cause unstable results](../facts/route53.md#route53-resolver-cidr-plus-two-forwarding-unsupported)
  link: [use a Resolver inbound endpoint](../facts/route53.md#route53-resolver-cidr-plus-two-forwarding-unsupported)
route53-resolver-custom-rules-forwarding-and-delegation
  claim: You can create two types of custom Resolver rules: conditional forwarding rules, also known as forwarding rules, and delegation rules. Forwarding rules cause VPC Resolver to forward DNS queries from your VPCs to the IP addresses of DNS resolvers on your network.
  scope: Resolver custom rules.
  link: [two types of custom rules](../facts/route53.md#route53-resolver-custom-rules-forwarding-and-delegation)
  link: [Forwarding rules cause VPC Resolver to forward DNS](../facts/route53.md#route53-resolver-custom-rules-forwarding-and-delegation)
route53-resolver-dot-rule-does-not-forward-everything
  claim: If you create a rule for "." to forward all queries to your network, VPC Resolver still does not forward all DNS queries, because using a DNS resolver outside of AWS would break some functionality.
  scope: Resolver forwarding rule for ".".
  link: [VPC Resolver still doesn't forward all DNS queries](../facts/route53.md#route53-resolver-dot-rule-does-not-forward-everything)
route53-resolver-endpoint-eni-per-az-subnet-ip
  claim: For each combination of Availability Zone, subnet and IP address that you specify, VPC Resolver creates an Amazon VPC elastic network interface.
  scope: per Resolver endpoint.
  link: [creates an Amazon VPC elastic network interface](../facts/route53.md#route53-resolver-endpoint-eni-per-az-subnet-ip)
route53-resolver-endpoint-ips-in-two-azs
  claim: You should specify inbound endpoint IP addresses in at least two Availability Zones for redundancy.
  scope: per inbound endpoint; minimum; Recommendation.
  link: [at least two Availability Zones](../facts/route53.md#route53-resolver-endpoint-ips-in-two-azs)
route53-resolver-endpoint-minimum-two-ips-inbound
  claim: You must specify a minimum of two IP addresses for an inbound endpoint, for redundancy.
  scope: per inbound endpoint; minimum; not adjustable.
  link: [minimum of two IP addresses](../facts/route53.md#route53-resolver-endpoint-minimum-two-ips-inbound)
route53-resolver-endpoint-one-spare-interface
  claim: If you need more than one endpoint network interface available at all times, AWS recommends creating at least one more than you need for traffic surges and maintenance.
  scope: per Resolver endpoint.
  link: [at least one more network interface](../facts/route53.md#route53-resolver-endpoint-one-spare-interface)
route53-resolver-forwarding-rule-covers-domain-and-subdomains
  claim: By default, forwarding rules apply to a domain name and all its subdomains. To skip some subdomains, create a system rule for them.
  scope: Resolver forwarding rules; default; not adjustable.
  link: [a domain name and all its subdomains](../facts/route53.md#route53-resolver-forwarding-rule-covers-domain-and-subdomains)
  link: [you create a system rule for the subdomains](../facts/route53.md#route53-resolver-forwarding-rule-covers-domain-and-subdomains)
route53-resolver-forwarding-rule-overrides-autodefined-rule
  claim: If you create a forwarding rule for the same domain as an autodefined rule, VPC Resolver forwards queries for that domain to the DNS resolvers on your network based on your forwarding rule.
  scope: Resolver rules.
  link: [to DNS resolvers on your network](../facts/route53.md#route53-resolver-forwarding-rule-overrides-autodefined-rule)
route53-resolver-hybrid-over-vpn-or-direct-connect
  claim: Through Resolver endpoints and conditional forwarding rules, you can resolve DNS queries between your on-premises resources and VPCs to create a hybrid cloud setup over VPN or Direct Connect.
  scope: hybrid DNS.
  link: [hybrid cloud setup over VPN or Direct Connect](../facts/route53.md#route53-resolver-hybrid-over-vpn-or-direct-connect)
  link: [Resolver endpoints and conditional forwarding rules](../facts/route53.md#route53-resolver-hybrid-over-vpn-or-direct-connect)
route53-resolver-inbound-40000-ip-port-combinations
  claim: The capacity of an inbound endpoint network interface is affected when over 40,000 unique IP address and port combinations generate the DNS traffic.
  scope: per inbound endpoint network interface; maximum; not adjustable.
  link: [over 40,000 unique IP address and port combinations](../facts/route53.md#route53-resolver-inbound-40000-ip-port-combinations)
route53-resolver-inbound-default-and-delegation-types
  claim: There are two types of inbound endpoints: a default inbound endpoint that forwards to IP addresses, and a delegation inbound endpoint that delegates the authority for a subdomain hosted in a Route 53 private hosted zone to VPC Resolver.
  scope: Resolver inbound endpoints.
  link: [default inbound endpoint that forwards to IP addresses](../facts/route53.md#route53-resolver-inbound-default-and-delegation-types)
  link: [delegation inbound endpoint that delegates the authority](../facts/route53.md#route53-resolver-inbound-default-and-delegation-types)
route53-resolver-inbound-endpoint-definition
  claim: Inbound Resolver endpoints allow DNS queries to your VPC from your on-premises network or another VPC.
  scope: Resolver inbound endpoint.
  link: [from your on-premises network or another VPC](../facts/route53.md#route53-resolver-inbound-endpoint-definition)
  link: [Inbound Resolver endpoints allow DNS queries](../facts/route53.md#route53-resolver-inbound-endpoint-definition)
route53-resolver-inbound-endpoint-no-behavior-change
  claim: Creating an inbound endpoint does not change the behavior of VPC Resolver. It only provides a path from outside the AWS network to VPC Resolver.
  scope: Resolver inbound endpoint.
  link: [from a location outside the AWS network](../facts/route53.md#route53-resolver-inbound-endpoint-no-behavior-change)
route53-resolver-inbound-ips-not-public-need-private-link
  claim: The IP addresses of an inbound endpoint are not public IP addresses, so you need to connect your VPC to your network with Direct Connect or a VPN for each inbound endpoint.
  scope: Resolver inbound endpoint.
  link: [aren't public IP addresses](../facts/route53.md#route53-resolver-inbound-ips-not-public-need-private-link)
  link: [Direct Connect connection or a VPN connection](../facts/route53.md#route53-resolver-inbound-ips-not-public-need-private-link)
route53-resolver-inbound-qps-low-1500
  claim: If connection tracking is enforced by restrictive security group rules, or queries are routed through Network Load Balancer, the maximum queries per second per IP address for an inbound endpoint can be as low as 1500.
  scope: per IP address of an inbound endpoint; minimum; not adjustable; Connection tracking enforced by restrictive security group rules, or queries routed through Network Load Balancer.
  link: [as low as 1500](../facts/route53.md#route53-resolver-inbound-qps-low-1500)
route53-resolver-inbound-security-group-tcp-udp-53
  claim: When you create a default inbound endpoint, you specify the IP addresses that the resolvers on your network forward queries to, along with a VPC security group with inbound rules allowing TCP and UDP access on port 53.
  scope: default inbound endpoint.
  link: [inbound rules allowing TCP and UDP access on port 53](../facts/route53.md#route53-resolver-inbound-security-group-tcp-udp-53)
route53-resolver-inbound-sg-port-53
  claim: The security group of an inbound endpoint must have inbound rules that allow TCP and UDP access on port 53.
  scope: per inbound endpoint.
  link: [TCP and UDP access on port 53](../facts/route53.md#route53-resolver-inbound-sg-port-53)
route53-resolver-internet-resolver-rule-cannot-delete
  claim: You cannot delete the default Internet Resolver rule, which has the type Recursive. It makes VPC Resolver act as a recursive resolver for domain names that have no custom or autodefined rule.
  scope: Resolver rules.
  link: [You can't delete the default Internet Resolver rule](../facts/route53.md#route53-resolver-internet-resolver-rule-cannot-delete)
  link: [a recursive resolver for any domain names](../facts/route53.md#route53-resolver-internet-resolver-rule-cannot-delete)
route53-resolver-link-local-1024-pps-shared
  claim: Each elastic network interface allows 1024 packets per second (PPS) destined to Link-Local services, which include the VPC Resolver.
  scope: per network interface; maximum; not adjustable; The limit is shared by VPC Resolver, Amazon Time Service, Instance Metadata Service and Windows Licensing Service.
  link: [1024 packets per second](../facts/route53.md#route53-resolver-link-local-1024-pps-shared)
route53-resolver-no-endpoint-in-dedicated-tenancy-vpc
  claim: When you create a Resolver endpoint, you cannot specify a VPC that has the instance tenancy attribute set to dedicated.
  scope: Resolver endpoints.
  link: [instance tenancy attribute set to dedicated](../facts/route53.md#route53-resolver-no-endpoint-in-dedicated-tenancy-vpc)
route53-resolver-no-per-vpc-query-limit
  claim: There is no per-VPC aggregate limit on the number of queries to Route 53 VPC Resolver.
  scope: per VPC.
  link: [no per-VPC aggregate limit](../facts/route53.md#route53-resolver-no-per-vpc-query-limit)
route53-resolver-only-vpc-owner-creates-endpoints
  claim: You cannot create Resolver endpoints in a VPC that you do not own. Only the VPC owner can create VPC-level resources such as inbound endpoints.
  scope: Resolver endpoints.
  link: [Only the VPC owner can create VPC-level resources](../facts/route53.md#route53-resolver-only-vpc-owner-creates-endpoints)
route53-resolver-outbound-endpoint-definition
  claim: Outbound Resolver endpoints allow DNS queries from your VPC to your on-premises network or another VPC.
  scope: Resolver outbound endpoint.
  link: [from your VPC to your on-premises network](../facts/route53.md#route53-resolver-outbound-endpoint-definition)
  link: [Outbound Resolver endpoints allow DNS queries](../facts/route53.md#route53-resolver-outbound-endpoint-definition)
route53-resolver-outbound-endpoint-shared-by-vpcs-in-region
  claim: You can use the same outbound endpoint for multiple VPCs in the same Region, or you can create multiple outbound endpoints.
  scope: Resolver outbound endpoint.
  link: [the same outbound endpoint for multiple VPCs](../facts/route53.md#route53-resolver-outbound-endpoint-shared-by-vpcs-in-region)
route53-resolver-outbound-ips-not-public-need-link-or-nat
  claim: The IP addresses of an outbound endpoint are not public, so you need to connect your VPC to your network with Direct Connect, a VPN, or a NAT gateway for each outbound endpoint.
  scope: Resolver outbound endpoint.
  link: [or a network address translation (NAT) gateway](../facts/route53.md#route53-resolver-outbound-ips-not-public-need-link-or-nat)
route53-resolver-outbound-path-private-connection
  claim: The outbound endpoint forwards the query to the on-premises DNS resolver through a private connection between AWS and the data center, which can be Direct Connect or AWS Site-to-Site VPN.
  scope: outbound forwarding.
  link: [private connection between AWS and the data center](../facts/route53.md#route53-resolver-outbound-path-private-connection)
  link: [either Direct Connect or AWS Site-to-Site VPN](../facts/route53.md#route53-resolver-outbound-path-private-connection)
route53-resolver-over-limit-packets-rejected
  claim: Each network interface allows 1024 packets per second (PPS) destined to Link-Local services, which include Route 53 VPC Resolver; packets exceeding this limit are rejected.
  scope: per network interface.
  link: [are rejected](../facts/route53.md#route53-resolver-over-limit-packets-rejected)
route53-resolver-query-logs-destinations
  claim: You can send VPC Resolver query logs to an Amazon CloudWatch Logs log group, an Amazon S3 bucket, or a Firehose delivery stream.
  scope: VPC Resolver query logging.
  link: [send VPC Resolver query logs to the following](../facts/route53.md#route53-resolver-query-logs-destinations)
  link: [An S3 bucket is economical for long-term log archiving](../facts/route53.md#route53-resolver-query-logs-destinations)
  link: [stream logs in real time to Amazon OpenSearch](../facts/route53.md#route53-resolver-query-logs-destinations)
route53-resolver-query-logs-only-unique-queries-not-cached
  claim: VPC Resolver query logging logs only unique queries, not queries that VPC Resolver answers from its cache.
  scope: VPC Resolver query logging.
  link: [logs only unique queries](../facts/route53.md#route53-resolver-query-logs-only-unique-queries-not-cached)
route53-resolver-query-logs-what-is-logged
  claim: Resolver query logging can log queries that originate in the VPCs that you specify (with their responses), queries from on-premises resources that use an inbound Resolver endpoint, queries that use an outbound Resolver endpoint for recursive DNS resolution, and queries that use Resolver DNS Firewall rules to block, allow, or monitor domain lists.
  scope: VPC Resolver query logging.
  link: [Queries that originate in Amazon Virtual Private Cloud](../facts/route53.md#route53-resolver-query-logs-what-is-logged)
  link: [on-premises resources that use an inbound Resolver endpoint](../facts/route53.md#route53-resolver-query-logs-what-is-logged)
  link: [Queries that use an outbound Resolver endpoint](../facts/route53.md#route53-resolver-query-logs-what-is-logged)
route53-resolver-recursive-queries-only
  claim: The Amazon Route 53 Resolver only supports recursive DNS queries.
  scope: per VPC.
  link: [only supports recursive DNS queries](../facts/route53.md#route53-resolver-recursive-queries-only)
route53-resolver-recursive-rule-internet-resolver
  claim: VPC Resolver automatically creates a recursive rule named Internet Resolver. It makes VPC Resolver act as a recursive resolver for domain names that have no custom or autodefined rule.
  scope: Resolver recursive rule.
  link: [a recursive rule named Internet Resolver](../facts/route53.md#route53-resolver-recursive-rule-internet-resolver)
route53-resolver-regional-endpoint-per-region
  claim: Like Amazon VPC, VPC Resolver is regional. In each Region where you have VPCs, you choose whether to forward queries from your VPCs to your network, from your network to your VPCs, or both.
  scope: VPC Resolver.
  link: [VPC Resolver is regional](../facts/route53.md#route53-resolver-regional-endpoint-per-region)
  link: [network to your VPCs (inbound queries), or both](../facts/route53.md#route53-resolver-regional-endpoint-per-region)
route53-resolver-rule-beats-phz-same-name
  claim: If a private hosted zone and a VPC Resolver rule that forwards to your network have the same domain name, the VPC Resolver rule takes precedence and queries are forwarded to your network.
  scope: VPC with both a private hosted zone and a forwarding rule.
  link: [the VPC Resolver rule takes precedence](../facts/route53.md#route53-resolver-rule-beats-phz-same-name)
  link: [for the same domain name](../facts/route53.md#route53-resolver-rule-beats-phz-same-name)
route53-resolver-rule-most-specific-match-wins
  claim: If a query matches multiple rules, such as example.com and acme.example.com, VPC Resolver chooses the rule with the most specific match and forwards the query to the IP addresses in that rule.
  scope: Resolver rules.
  link: [chooses the rule with the most specific match](../facts/route53.md#route53-resolver-rule-most-specific-match-wins)
  link: [If a query matches multiple rules](../facts/route53.md#route53-resolver-rule-most-specific-match-wins)
route53-resolver-rule-targets-chosen-at-random
  claim: VPC Resolver chooses the target IP of a rule at random, with no preference for a particular target IP. If a target does not respond, it retries to a random IP address among the targets.
  scope: forwarding rule targets.
  link: [chosen at random by VPC Resolver](../facts/route53.md#route53-resolver-rule-targets-chosen-at-random)
  link: [retries to a random IP address](../facts/route53.md#route53-resolver-rule-targets-chosen-at-random)
route53-resolver-rules-applied-to-vpc-shared-across-accounts
  claim: Resolver rules are applied directly to your VPC and can be shared across multiple accounts.
  scope: Resolver rules.
  link: [can be shared across multiple accounts](../facts/route53.md#route53-resolver-rules-applied-to-vpc-shared-across-accounts)
  link: [applied directly to your VPC](../facts/route53.md#route53-resolver-rules-applied-to-vpc-shared-across-accounts)
route53-resolver-rules-control-forwarding
  claim: Rules control which DNS queries a Resolver endpoint forwards to DNS resolvers on your network and which queries VPC Resolver answers itself.
  scope: Resolver rules.
  link: [DNS queries Resolver endpoint forwards to DNS resolvers](../facts/route53.md#route53-resolver-rules-control-forwarding)
  link: [which queries VPC Resolver answers itself](../facts/route53.md#route53-resolver-rules-control-forwarding)
route53-resolver-rules-shared-with-ram
  claim: You can share the Resolver rules that you created with other AWS accounts. To share rules, the VPC Resolver console integrates with AWS Resource Access Manager.
  scope: Resolver rules.
  link: [integrates with AWS Resource Access Manager](../facts/route53.md#route53-resolver-rules-shared-with-ram)
  link: [share the Resolver rules that you created](../facts/route53.md#route53-resolver-rules-shared-with-ram)
route53-resolver-system-rule-overrides-forwarding-rule
  claim: A system rule makes VPC Resolver selectively override a forwarding rule. When you create a system rule, VPC Resolver resolves queries for the specified subdomains that DNS resolvers on your network would otherwise resolve.
  scope: Resolver system rules.
  link: [System rules cause VPC Resolver to selectively override](../facts/route53.md#route53-resolver-system-rule-overrides-forwarding-rule)
  link: [resolves DNS queries for specified subdomains](../facts/route53.md#route53-resolver-system-rule-overrides-forwarding-rule)
route53-resolver-three-rule-types
  claim: There are three types of Resolver rules: forward, system, and delegation.
  scope: Resolver rules.
  link: [three types of rules, forward, system, and delegation](../facts/route53.md#route53-resolver-three-rule-types)
  say: three types of rules
route53-resolver-typically-managed-by-isp
  claim: A user's request for a domain name goes first to a DNS resolver, which is typically managed by the user's internet service provider (ISP) or a corporate network.
  scope: DNS resolution.
  link: [typically managed by the user's internet service provider](../facts/route53.md#route53-resolver-typically-managed-by-isp)
route53-reusable-delegation-set
  claim: A reusable delegation set is a set of four authoritative name servers that you can use with more than one hosted zone.
  scope: Route 53 reusable delegation set.
  link: [A set of four authoritative name servers](../facts/route53.md#route53-reusable-delegation-set)
  link: [more than one hosted zone](../facts/route53.md#route53-reusable-delegation-set)
  say: four name servers
route53-reusable-delegation-set-api-only-simplifies-migration
  claim: Reusable delegation sets are not available in the Amazon Route 53 console. A reusable delegation set lets you tell your registrar to use the same four name servers for all the domains that you want Route 53 to serve, which makes it simpler to migrate DNS service to Route 53.
  scope: reusable delegation sets.
  link: [aren't available in the Route 53 console](../facts/route53.md#route53-reusable-delegation-set-api-only-simplifies-migration)
  link: [simpler to migrate DNS service to Route 53](../facts/route53.md#route53-reusable-delegation-set-api-only-simplifies-migration)
  link: [same four name servers for all the domains](../facts/route53.md#route53-reusable-delegation-set-api-only-simplifies-migration)
route53-reusable-delegation-set-no-console
  claim: You create a reusable delegation set and associate it with a hosted zone programmatically. Using the Route 53 console is not supported for this.
  scope: reusable delegation set.
  link: [programmatically](../facts/route53.md#route53-reusable-delegation-set-no-console)
  link: [using the Route 53 console isn't supported](../facts/route53.md#route53-reusable-delegation-set-no-console)
route53-routing-policy-determines-response
  claim: When you create a record, you choose a routing policy, which determines how queries are answered.
  scope: record.
  link: [you choose a routing policy](../facts/route53.md#route53-routing-policy-determines-response)
  link: [determines how Amazon Route 53 responds to queries](../facts/route53.md#route53-routing-policy-determines-response)
route53-s3-alias-record-type-a
  claim: To route traffic to an S3 bucket that is configured as a website, you create a record of type A (IPv4 address), turn on Alias, and choose Alias to S3 website endpoint.
  scope: alias to an S3 website.
  link: [Alias to S3 website endpoint](../facts/route53.md#route53-s3-alias-record-type-a)
route53-s3-website-bucket-name-must-match
  claim: To route a domain to an S3 website, the bucket must have the same name as your domain or subdomain.
  scope: S3 static website with an alias record.
  link: [same name as your domain or subdomain](../facts/route53.md#route53-s3-website-bucket-name-must-match)
  link: [The bucket must have the same name](../facts/route53.md#route53-s3-website-bucket-name-must-match)
route53-s3-website-buckets-redirect-to-one-bucket
  claim: You can route a domain and its subdomains to a single S3 bucket by creating a bucket for the domain and each subdomain, and configuring all but one of the buckets to redirect traffic to the remaining bucket.
  scope: S3 website buckets.
  link: [all but one of the buckets to redirect](../facts/route53.md#route53-s3-website-buckets-redirect-to-one-bucket)
route53-s3-website-endpoint-no-https
  claim: An S3 bucket configured as a website endpoint does not support SSL/TLS. To serve it over HTTPS, route traffic to a CloudFront distribution and use the bucket as its origin.
  scope: S3 website endpoint.
  link: [doesn't support SSL/TLS](../facts/route53.md#route53-s3-website-endpoint-no-https)
  link: [use the S3 bucket as the origin for the distribution](../facts/route53.md#route53-s3-website-endpoint-no-https)
route53-same-name-hosted-zones-allowed
  claim: You can create more than one hosted zone with the same name and add different records to each. Route 53 assigns four name servers to every hosted zone, and by default the name servers differ for each one; with a reusable delegation set, created with the API, you can assign the same four name servers to several hosted zones.
  scope: public hosted zones.
  link: [more than one hosted zone](../facts/route53.md#route53-same-name-hosted-zones-allowed)
  link: [the name servers differ for each one](../facts/route53.md#route53-same-name-hosted-zones-allowed)
route53-same-name-zones-never-mix-records
  claim: Route 53 never returns values for records in other hosted zones that have the same name, so when you update your registrar's name server records, use the Route 53 name servers of the hosted zone that has the records you want Route 53 to use.
  scope: public hosted zones with the same name.
  link: [never returns values for records](../facts/route53.md#route53-same-name-zones-never-mix-records)
  link: [use the Route 53 name servers for the correct hosted zone](../facts/route53.md#route53-same-name-zones-never-mix-records)
route53-simple-alias-one-target
  claim: If you choose the simple routing policy for an alias record, you can specify only one AWS resource or one record in the current hosted zone.
  scope: simple alias record.
  link: [only one AWS resource or one record](../facts/route53.md#route53-simple-alias-one-target)
route53-simple-config-alias-targets-no-health-check-needed
  claim: When an alias record evaluates the health of an AWS resource, you do not need to create a health check for that resource. For resources you cannot create alias records for, such as EC2 instances, you create a record and a health check for each resource.
  scope: simple configurations.
  link: [don't need to create a health check](../facts/route53.md#route53-simple-config-alias-targets-no-health-check-needed)
  link: [record and a health check for each resource](../facts/route53.md#route53-simple-config-alias-targets-no-health-check-needed)
route53-simple-routing-multiple-values-one-record
  claim: If you choose the simple routing policy in the Route 53 console, you can't create multiple records with the same name and type, but you can specify multiple values in the same record, such as multiple IP addresses.
  scope: simple routing in the Route 53 console.
  link: [can specify multiple values in the same record](../facts/route53.md#route53-simple-routing-multiple-values-one-record)
  link: [can't create multiple records with the same name](../facts/route53.md#route53-simple-routing-multiple-values-one-record)
route53-simple-routing-multiple-values-random-order-no-health-check
  claim: If a simple record has multiple values, Route 53 returns all values to the recursive resolver in random order, and the client chooses one. The multiple IP addresses are not health checked.
  scope: simple routing record with multiple values.
  link: [to the recursive resolver in random order](../facts/route53.md#route53-simple-routing-multiple-values-random-order-no-health-check)
  link: [they are not health checked](../facts/route53.md#route53-simple-routing-multiple-values-random-order-no-health-check)
route53-simple-routing-no-special-routing
  claim: With simple routing you set up standard DNS records, with no special routing such as weighted or latency. You typically route traffic to a single resource, for example a web server.
  scope: simple routing.
  link: [set up standard DNS records](../facts/route53.md#route53-simple-routing-no-special-routing)
  link: [route traffic to a single resource](../facts/route53.md#route53-simple-routing-no-special-routing)
route53-sla-credit-starts-below-100-percent
  claim: The Amazon Route 53 SLA gives a 10% service credit when a hosted zone's monthly uptime is below 100% but at least 99.99%, a 25% credit below 99.99% but at least 99.95%, and a 100% credit below 99.95%.
  scope: Amazon Route 53 SLA, hosted zones outside GovCloud.
  link: [Less than 100% but greater than or equal to 99.99%](../facts/route53.md#route53-sla-credit-starts-below-100-percent)
  link: [Less than 99.95%](../facts/route53.md#route53-sla-credit-starts-below-100-percent)
route53-soa-record-ttl-default-900
  claim: The TTL of the SOA record defaults to 900 seconds.
  scope: per SOA record; default; adjustable; One of two values that set the negative caching duration; the lesser applies.
  link: [900 seconds](../facts/route53.md#route53-soa-record-ttl-default-900)
route53-spf-record-type-not-recommended
  claim: AWS no longer recommends creating records of type SPF. Instead, it recommends a TXT record that contains the applicable value.
  scope: SPF record type.
  link: [we no longer recommend that you create records](../facts/route53.md#route53-spf-record-type-not-recommended)
  link: [we recommend that you create a TXT record](../facts/route53.md#route53-spf-record-type-not-recommended)
route53-split-view-dns-definition
  claim: Split-view DNS (split-horizon DNS) uses the same domain name for internal and external uses. You create a public and a private hosted zone with the same name, associate VPCs with the private zone, and add records in each zone.
  scope: split-view DNS.
  link: [private hosted zones that have the same name](../facts/route53.md#route53-split-view-dns-definition)
  link: [split-view DNS, also known as split-horizon DNS](../facts/route53.md#route53-split-view-dns-definition)
  link: [control how traffic is routed](../facts/route53.md#route53-split-view-dns-definition)
route53-split-view-works-with-other-public-dns
  claim: Split-view DNS still works if you use another DNS service for the public hosted zone.
  scope: split-view DNS.
  link: [still works if you're using another DNS service](../facts/route53.md#route53-split-view-works-with-other-public-dns)
route53-subdomain-delegation-limits-access-by-iam
  claim: When you use a separate hosted zone for a subdomain, you can use IAM permissions to restrict access to that hosted zone. Creating a hosted zone for each subdomain can reduce the number of people who need access to the records of the domain's hosted zone.
  scope: subdomain delegation.
  link: [use IAM permissions to restrict access](../facts/route53.md#route53-subdomain-delegation-limits-access-by-iam)
  link: [multiple subdomains managed by different groups](../facts/route53.md#route53-subdomain-delegation-limits-access-by-iam)
route53-subdomain-delegation-steps-new-zone-and-ns-record
  claim: To delegate a subdomain, you create a hosted zone with the subdomain name, create records in it, and then create an NS record in the parent domain's hosted zone. The NS record name is the subdomain name and its values are the four name servers of the new zone.
  scope: subdomain delegation.
  link: [the same name as the subdomain](../facts/route53.md#route53-subdomain-delegation-steps-new-zone-and-ns-record)
  link: [NS record name must be the subdomain name](../facts/route53.md#route53-subdomain-delegation-steps-new-zone-and-ns-record)
route53-supports-ipv4-and-ipv6-records-and-health-checks
  claim: Route 53 supports both IPv4 and IPv6 addresses. You can create A and AAAA records, health checks that send requests to IPv4 or IPv6 addresses, and a resolver on an IPv6 network can use either IPv4 or IPv6 to submit requests.
  scope: Route 53.
  link: [a type of AAAA, for IPv6 addresses](../facts/route53.md#route53-supports-ipv4-and-ipv6-records-and-health-checks)
  link: [health checks that send requests either to IPv4 or to IPv6 addresses](../facts/route53.md#route53-supports-ipv4-and-ipv6-records-and-health-checks)
  link: [it can use either IPv4 or IPv6 to submit requests to Route 53](../facts/route53.md#route53-supports-ipv4-and-ipv6-records-and-health-checks)
route53-three-main-functions
  claim: Route 53 is a DNS web service that does three jobs: domain registration, DNS routing and health checking. You can use them in any combination, so they do not have to be used together.
  scope: Amazon Route 53.
  link: [three main functions](../facts/route53.md#route53-three-main-functions)
  link: [in any combination](../facts/route53.md#route53-three-main-functions)
  link: [highly available and scalable](../facts/route53.md#route53-three-main-functions)
  say: three main functions
route53-tld-returns-four-name-servers
  claim: The TLD name server answers with the names of the four Route 53 name servers associated with the domain.
  scope: per domain.
  link: [four Route 53 name servers](../facts/route53.md#route53-tld-returns-four-name-servers)
  link: [names of the four Route 53 name servers](../facts/route53.md#route53-tld-returns-four-name-servers)
  say: four name servers
route53-traffic-flow-alias-to-policy-record-reduces-charges
  claim: To minimize charges, create one or more alias records in a hosted zone that reference a traffic policy record in that hosted zone.
  scope: Traffic Flow.
  link: [hosted zone that reference a traffic policy record](../facts/route53.md#route53-traffic-flow-alias-to-policy-record-reduces-charges)
route53-traffic-flow-feature-overview-best-endpoint
  claim: Traffic Flow is easy-to-use and cost-effective global traffic management: you route end users to the best endpoint for your application based on geoproximity, latency, health, and other considerations.
  scope: Traffic Flow.
  link: [route end users to the best endpoint](../facts/route53.md#route53-traffic-flow-feature-overview-best-endpoint)
  link: [global traffic management](../facts/route53.md#route53-traffic-flow-feature-overview-best-endpoint)
route53-traffic-flow-monthly-charge-per-policy-record
  claim: There is a monthly charge for each traffic policy record. You can create as many traffic policies as you want at no charge.
  scope: Traffic Flow.
  link: [a monthly charge for each traffic policy record](../facts/route53.md#route53-traffic-flow-monthly-charge-per-policy-record)
  link: [traffic policies as you want at no charge](../facts/route53.md#route53-traffic-flow-monthly-charge-per-policy-record)
route53-traffic-flow-policy-record-creates-whole-tree
  claim: A traffic policy record automatically creates all the other records in the tree of a traffic policy. Only the root record appears in the list of records for your hosted zone, and Route 53 hides all the other records.
  scope: Traffic Flow.
  link: [creating a traffic policy record](../facts/route53.md#route53-traffic-flow-policy-record-creates-whole-tree)
  link: [Route 53 hides all the other records](../facts/route53.md#route53-traffic-flow-policy-record-creates-whole-tree)
route53-traffic-flow-policy-reuse-across-zones
  claim: You can use one traffic policy to automatically create records in multiple public hosted zones, for example when the same web servers serve several domain names.
  scope: Traffic Flow.
  link: [create records in multiple public hosted zones](../facts/route53.md#route53-traffic-flow-policy-reuse-across-zones)
route53-traffic-flow-public-hosted-zones-only
  claim: You can use Traffic Flow to create records only in public hosted zones.
  scope: Traffic Flow.
  link: [only in public hosted zones](../facts/route53.md#route53-traffic-flow-public-hosted-zones-only)
  link: [You can use Traffic Flow to create records](../facts/route53.md#route53-traffic-flow-public-hosted-zones-only)
route53-traffic-flow-purpose
  claim: Traffic Flow greatly simplifies creating and maintaining records in large and complex configurations.
  scope: Traffic Flow.
  link: [simplifies the process of creating and maintaining records](../facts/route53.md#route53-traffic-flow-purpose)
  link: [large and complex configurations](../facts/route53.md#route53-traffic-flow-purpose)
route53-traffic-flow-update-policy-record-rollback
  claim: When you update a traffic policy record, Route 53 automatically updates all the other records in the tree. You can quickly roll back by updating the traffic policy record to use a previous version of the traffic policy.
  scope: Traffic Flow.
  link: [Route 53 automatically updates all the other records in the tree](../facts/route53.md#route53-traffic-flow-update-policy-record-rollback)
  link: [quickly roll back changes](../facts/route53.md#route53-traffic-flow-update-policy-record-rollback)
route53-traffic-flow-versioning
  claim: You can create multiple versions of a traffic policy so you do not have to start over when your configuration changes. Old versions continue to exist until you delete them.
  scope: traffic policy.
  link: [create multiple versions of a traffic policy](../facts/route53.md#route53-traffic-flow-versioning)
  link: [Old versions continue to exist](../facts/route53.md#route53-traffic-flow-versioning)
route53-traffic-flow-visual-editor-traffic-policy
  claim: The Traffic Flow visual editor lets you create complex trees of records and see their relationships. Each configuration is known as a traffic policy.
  scope: Traffic Flow.
  link: [create complex trees of records](../facts/route53.md#route53-traffic-flow-visual-editor-traffic-policy)
  link: [known as a traffic policy](../facts/route53.md#route53-traffic-flow-visual-editor-traffic-policy)
route53-ttl-defined
  claim: TTL is the number of seconds that a DNS resolver caches the values of a record before it asks Route 53 for the current values again.
  scope: per record.
  link: [amount of time, in seconds](../facts/route53.md#route53-ttl-defined)
  link: [a DNS resolver to cache (store) the values](../facts/route53.md#route53-ttl-defined)
route53-ttl-definition-resolver-cache
  claim: The DNS TTL is the number of seconds that DNS resolvers use to decide how long a record can stay cached before they query Route 53 again.
  scope: per DNS record.
  link: [how long a record can be cached](../facts/route53.md#route53-ttl-definition-resolver-cache)
route53-ttl-health-check-60-seconds-or-less
  claim: If you associate a record with a health check, AWS recommends a TTL of 60 seconds or less so clients respond quickly to changes in health status.
  scope: per record associated with a health check; maximum; Recommendation, not enforced.
  link: [60 seconds or less](../facts/route53.md#route53-ttl-health-check-60-seconds-or-less)
route53-ttl-health-checked-60-or-120
  claim: For records that change as part of rapid failover, especially health-checked records, lower TTLs are appropriate, and a TTL of 60 or 120 seconds is a common choice.
  scope: per DNS record used for failover.
  link: [60 or 120 seconds](../facts/route53.md#route53-ttl-health-checked-60-or-120)
route53-ttl-longer-cheaper-shorter-faster-change
  claim: A longer TTL reduces Route 53 charges because charges depend in part on the number of DNS queries answered. A shorter TTL shortens the time that resolvers keep sending traffic to old values after you change a record.
  scope: per record.
  link: [A longer TTL reduces your Route 53 charges](../facts/route53.md#route53-ttl-longer-cheaper-shorter-faster-change)
  link: [A shorter TTL reduces the time](../facts/route53.md#route53-ttl-longer-cheaper-shorter-faster-change)
route53-ttl-longer-fewer-queries
  claim: The TTL is the number of seconds that recursive resolvers cache a record, and a longer value such as 172800 seconds (two days) reduces the number of calls that resolvers make to Route 53.
  scope: per DNS record.
  link: [172800 seconds](../facts/route53.md#route53-ttl-longer-fewer-queries)
route53-ttl-rarely-changing-one-hour-to-one-day
  claim: For delegations (NS record sets) and other rarely changing records such as MX records, longer TTLs are recommended, and a value between an hour (3600s) and a day (86,400s) is a common choice.
  scope: per DNS record that rarely changes.
  link: [between an hour (3600s) and a day (86,400s)](../facts/route53.md#route53-ttl-rarely-changing-one-hour-to-one-day)
route53-ttl-recommended-range
  claim: The recommended range for DNS TTL values is 60 to 172,800 seconds.
  scope: per DNS record.
  link: [60 to 172,800 seconds](../facts/route53.md#route53-ttl-recommended-range)
route53-ttl-required-on-all-records
  claim: All DNS records must have a TTL specified for them.
  scope: per DNS record.
  link: [must have a TTL](../facts/route53.md#route53-ttl-required-on-all-records)
route53-ttl-start-shorter-300-seconds-in-use
  claim: For a domain or subdomain that is already in use, AWS recommends a shorter TTL first, such as 300 seconds, and a higher value after you confirm the new settings are correct.
  scope: per DNS record.
  link: [such as 300 seconds](../facts/route53.md#route53-ttl-start-shorter-300-seconds-in-use)
route53-txt-record-strings
  claim: A TXT record contains one or more strings that are enclosed in double quotation marks.
  scope: TXT record.
  link: [strings that are enclosed in double quotation marks](../facts/route53.md#route53-txt-record-strings)
route53-vpc-interface-endpoint-alias-record
  claim: To route domain traffic to a VPC interface endpoint, you create an alias record.
  scope: routing to a VPC interface endpoint.
  link: [create an alias record](../facts/route53.md#route53-vpc-interface-endpoint-alias-record)
route53-vpc-permissions-iam-condition
  claim: With the IAM policy condition route53:VPCs you can grant permissions to associate a hosted zone with, or disassociate it from, a single VPC, any VPCs in the same Region, or multiple VPCs.
  scope: private hosted zone VPC permissions.
  link: [route53:VPCs](../facts/route53.md#route53-vpc-permissions-iam-condition)
  link: [grant granular administrative rights](../facts/route53.md#route53-vpc-permissions-iam-condition)
route53-vpc-resolver-public-names-recursive-lookup
  claim: For public domain names, VPC Resolver performs recursive lookups against public name servers on the internet.
  scope: VPC Resolver.
  link: [performs recursive lookups against public name servers](../facts/route53.md#route53-vpc-resolver-public-names-recursive-lookup)
route53-vpc-resolver-recursive-by-default-in-all-vpcs
  claim: Route 53 VPC Resolver responds recursively to DNS queries from AWS resources for public records, VPC-specific DNS names and private hosted zones, and it is available by default in all VPCs.
  scope: all VPCs; default; not adjustable.
  link: [is available by default in all VPCs](../facts/route53.md#route53-vpc-resolver-recursive-by-default-in-all-vpcs)
  link: [responds recursively to DNS queries from AWS resources](../facts/route53.md#route53-vpc-resolver-recursive-by-default-in-all-vpcs)
route53-vpc-resolver-regional
  claim: VPC Resolver is a Regional service. Its control plane and data plane run independently in each AWS Region.
  scope: Route 53 VPC Resolver.
  link: [VPC Resolver is a Regional service](../facts/route53.md#route53-vpc-resolver-regional)
  link: [run independently in each AWS Region](../facts/route53.md#route53-vpc-resolver-regional)
route53-vpc-resolver-vpc-plus-two-address
  claim: An Amazon VPC connects to a VPC Resolver at a VPC+2 IP address. This VPC+2 address connects to a VPC Resolver within an Availability Zone.
  scope: VPC DNS resolution.
  link: [VPC\+2 IP address](../facts/route53.md#route53-vpc-resolver-vpc-plus-two-address)
  link: [within an Availability Zone](../facts/route53.md#route53-vpc-resolver-vpc-plus-two-address)
route53-vs-ga-change-propagation-seconds
  claim: With AWS Global Accelerator, change propagation takes a matter of seconds, which reduces application downtime.
  scope: AWS Global Accelerator.
  link: [Change propagation takes a matter of seconds](../facts/route53.md#route53-vs-ga-change-propagation-seconds)
route53-vs-ga-dr-avoids-dns-caching
  claim: The DR whitepaper says AWS Global Accelerator avoids caching issues that can occur with DNS systems such as Amazon Route 53, and offers lower latencies because it puts traffic on the AWS network backbone as soon as possible.
  scope: AWS Global Accelerator compared with DNS-based routing.
  link: [avoids caching issues that can occur with DNS](../facts/route53.md#route53-vs-ga-dr-avoids-dns-caching)
route53-vs-ga-resolvers-cache-dns-answers
  claim: Some client devices and internet resolvers cache DNS answers for long periods, so after a configuration change or application failure you cannot know how long it takes before all users receive updated IP addresses; Global Accelerator does not rely on the IP address caching settings of client devices.
  scope: DNS-based traffic management compared with AWS Global Accelerator.
  link: [cache DNS answers for long periods of time](../facts/route53.md#route53-vs-ga-resolvers-cache-dns-answers)
  link: [don’t have to rely on the IP address](../facts/route53.md#route53-vs-ga-resolvers-cache-dns-answers)
route53-vs-ga-static-anycast
  claim: AWS Global Accelerator gives static IP addresses that are a fixed entry point to your application, which lets you move endpoints between Availability Zones or Regions without updating the DNS configuration or client-facing applications.
  scope: AWS Global Accelerator.
  link: [a fixed entry point to your applications](../facts/route53.md#route53-vs-ga-static-anycast)
route53-weighted-alias-elb-non-alias-ttl-60
  claim: If a group of weighted records includes weighted alias records that route to an ELB load balancer, give the non-alias weighted records of the same name and type a TTL of 60 seconds.
  scope: per group of weighted records; Other values change the effect of the Weight values.
  link: [TTL of 60 seconds](../facts/route53.md#route53-weighted-alias-elb-non-alias-ttl-60)
route53-weighted-all-zero-equal-probability
  claim: If every record in a weighted group has a Weight of 0, traffic goes to all resources with equal probability.
  scope: per group of weighted records.
  link: [equal probability](../facts/route53.md#route53-weighted-all-zero-equal-probability)
route53-weighted-example-1-and-255
  claim: With weights of 1 and 255, the resource with weight 1 gets 1/256th of the traffic and the other resource gets 255/256ths.
  scope: per group of weighted records.
  link: [1/256th of the traffic](../facts/route53.md#route53-weighted-example-1-and-255)
route53-weighted-ratio-of-weight-to-total
  claim: Route 53 sums the weights of the records that share a DNS name and type, then answers queries in the ratio of each record's weight to that total.
  scope: per group of weighted records.
  link: [ratio of a resource's weight to the total](../facts/route53.md#route53-weighted-ratio-of-weight-to-total)
route53-weighted-routing-purpose
  claim: With weighted routing, you link multiple resources to a single domain name or subdomain name and choose how much traffic goes to each resource. This can be useful for load balancing and for testing new versions of software.
  scope: weighted routing.
  link: [load balancing and testing new versions of software](../facts/route53.md#route53-weighted-routing-purpose)
  link: [choose how much traffic goes to each resource](../facts/route53.md#route53-weighted-routing-purpose)
route53-weighted-routing-share-of-total-weight
  claim: Traffic goes to a weighted record based on the weight of the record as a share of the total weight of all records in the group. You create records with the same name and type for each resource.
  scope: weighted records in a group.
  link: [a share of the total weight](../facts/route53.md#route53-weighted-routing-share-of-total-weight)
  link: [records with the same name and type](../facts/route53.md#route53-weighted-routing-share-of-total-weight)
route53-weighted-routing-weight-zero-stops-traffic
  claim: To stop sending traffic to a resource under weighted routing, change the weight of that record to 0.
  scope: weighted record.
  link: [change the weight for that record to 0](../facts/route53.md#route53-weighted-routing-weight-zero-stops-traffic)
  link: [stop sending traffic to a resource](../facts/route53.md#route53-weighted-routing-weight-zero-stops-traffic)
  say: weight of zero
route53-weighted-ttl-short-before-change
  claim: For a domain or subdomain that is already in use, set a shorter TTL first (for example 300 seconds) and raise it after you confirm the new settings; a longer TTL means recursive resolvers use cached values longer before asking Amazon Route 53 for the latest information.
  scope: Amazon Route 53 record TTL.
  link: [specify a shorter value first, such as 300 seconds](../facts/route53.md#route53-weighted-ttl-short-before-change)
route53-weighted-weight-range-0-255
  claim: A weighted record's Weight is an integer between 0 and 255.
  scope: per weighted record; maximum; not adjustable.
  link: [between 0 and 255](../facts/route53.md#route53-weighted-weight-range-0-255)
route53-weighted-zero-weight-health-nonzero-first
  claim: When all weighted records have health checks and some have a weight of zero, Route 53 initially considers only the nonzero weighted records.
  scope: per group of weighted records with health checks; Health checks on all records, with nonzero and zero weights mixed.
  link: [only the nonzero weighted records](../facts/route53.md#route53-weighted-zero-weight-health-nonzero-first)
route53-weighted-zero-weight-used-when-all-unhealthy
  claim: If all weighted records with a weight above 0 are unhealthy, Route 53 considers the zero-weighted records.
  scope: per group of weighted records with health checks.
  link: [considers the zero-weighted records](../facts/route53.md#route53-weighted-zero-weight-used-when-all-unhealthy)
route53-wildcard-not-allowed-for-ns-records
  claim: You cannot use the * wildcard for resource record sets that have the type NS.
  scope: NS records.
  link: [You can't use the \* wildcard](../facts/route53.md#route53-wildcard-not-allowed-for-ns-records)
route53-zone-creates-ns-and-soa
  claim: When you create a hosted zone, Route 53 creates a name server (NS) record and a start of authority (SOA) record for it. The NS record lists the four name servers that you give to your registrar or DNS service so that DNS queries reach Route 53 name servers.
  scope: public hosted zone.
  link: [a start of authority (SOA) record](../facts/route53.md#route53-zone-creates-ns-and-soa)
  link: [lists the four name servers](../facts/route53.md#route53-zone-creates-ns-and-soa)
  say: four name servers
