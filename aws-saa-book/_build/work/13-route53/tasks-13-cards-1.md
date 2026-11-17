facts card: 19 facts
route53-hc-endpoint-automated-requests-over-internet
  claim: At regular intervals that you specify, Route 53 submits automated requests over the internet to your application, server or other resource to verify that it is reachable, available and functional.
  scope: endpoint health check.
  link: [automated requests over the internet](../facts/route53.md#route53-hc-endpoint-automated-requests-over-internet)
  link: [reachable, available, and functional](../facts/route53.md#route53-hc-endpoint-automated-requests-over-internet)
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
route53-quota-health-checks-per-account
  claim: You can have 200 active health checks per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [200 active health checks](../facts/route53.md#route53-quota-health-checks-per-account)
route53-quota-hosted-zones-per-account
  claim: The initial quota is 500 hosted zones per AWS account, and you can request a higher quota.
  scope: per AWS account; default; adjustable.
  link: [500 per AWS account](../facts/route53.md#route53-quota-hosted-zones-per-account)
route53-hc-global-service-no-region-for-health-checks
  claim: Route 53 is a global service, so you do not specify the Region in which you create health checks.
  scope: health checks.
  link: [Route 53 is a global service](../facts/route53.md#route53-hc-global-service-no-region-for-health-checks)
route53-cname-dns-protocol-forbids-zone-apex
  claim: The DNS protocol does not allow a CNAME record for the zone apex. You cannot create a CNAME record for example.com, but you can create CNAME records for names such as www.example.com.
  scope: CNAME record.
  link: [DNS protocol does not allow you to create](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex)
  link: [for the top node of a DNS namespace](../facts/route53.md#route53-cname-dns-protocol-forbids-zone-apex)
route53-alias-allowed-at-zone-apex
  claim: Unlike a CNAME record, you can create an alias record at the zone apex, the top node of a DNS namespace. For example.com, the zone apex is example.com.
  scope: alias record at the zone apex.
  link: [the top node of a DNS namespace](../facts/route53.md#route53-alias-allowed-at-zone-apex)
  link: [you can create an alias record](../facts/route53.md#route53-alias-allowed-at-zone-apex)
  link: [also known as the zone apex](../facts/route53.md#route53-alias-allowed-at-zone-apex)
route53-alias-extension-targets
  claim: Alias records route traffic to selected AWS resources, such as CloudFront distributions and S3 buckets, and from one record in a hosted zone to another record.
  scope: alias record.
  link: [route traffic to selected AWS resources](../facts/route53.md#route53-alias-extension-targets)
  link: [one record in a hosted zone to another](../facts/route53.md#route53-alias-extension-targets)
route53-alias-target-another-record-all-types-except-ns-soa
  claim: For an alias to another record in the same hosted zone, all record types are supported except NS and SOA. At the zone apex, an alias record can't route traffic to a record whose type is CNAME.
  scope: alias to another record in the same hosted zone; at the zone apex, not to a CNAME record.
  link: [All types are supported except NS and SOA](../facts/route53.md#route53-alias-target-another-record-all-types-except-ns-soa)
route53-pricing-hosted-zone-deleted-in-12-hours-free
  claim: To allow testing, a hosted zone deleted within 12 hours of creation is not charged for the zone, but queries on its public hosted zone are still charged.
  scope: per hosted zone.
  link: [deleted within 12 hours of creation](../facts/route53.md#route53-pricing-hosted-zone-deleted-in-12-hours-free)
route53-migrate-hosted-zone-only-for-domain-you-administer
  claim: You can create a hosted zone only for a domain that you have permission to administer.
  scope: hosted zone.
  link: [a domain that you have permission to administer](../facts/route53.md#route53-migrate-hosted-zone-only-for-domain-you-administer)
route53-hc-calculated-threshold-above-children-unhealthy
  claim: If the number of healthy children you require is greater than the number of child health checks, the calculated health check is always unhealthy.
  scope: per calculated health check.
  link: [always considers this health check to be unhealthy](../facts/route53.md#route53-hc-calculated-threshold-above-children-unhealthy)
route53-hc-calculated-threshold-zero-always-healthy
  claim: If the number of healthy children you require is 0, the calculated health check is always healthy.
  scope: per calculated health check.
  link: [always considers this health check to be healthy](../facts/route53.md#route53-hc-calculated-threshold-zero-always-healthy)
route53-hc-invert-reverses-status
  claim: If you invert a health check, Route 53 considers the health check unhealthy when the status is healthy, and the reverse.
  scope: inverted health check.
  link: [invert the status of a health check](../facts/route53.md#route53-hc-invert-reverses-status)
  link: [unhealthy when the status is healthy](../facts/route53.md#route53-hc-invert-reverses-status)
route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy
  claim: With one primary record and one secondary record, Route 53 answers with the primary record when the primary resource is healthy and with the secondary record when the primary resource is unhealthy.
  scope: failover routing with one primary and one secondary record.
  link: [responds to DNS queries using the primary record](../facts/route53.md#route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy)
  link: [responds to DNS queries using the secondary record](../facts/route53.md#route53-failover-one-primary-one-secondary-responds-secondary-when-unhealthy)
route53-failover-both-unhealthy-returns-primary
  claim: If you associate health checks with both failover records and Route 53 considers both the primary and the secondary unhealthy, Route 53 returns the primary record.
  scope: failover records that both have health checks.
  link: [Route 53 returns the primary record](../facts/route53.md#route53-failover-both-unhealthy-returns-primary)
  link: [both the primary and secondary records unhealthy](../facts/route53.md#route53-failover-both-unhealthy-returns-primary)
route53-pricing-health-check-aws-vs-non-aws-endpoints
  claim: Amazon Route 53 health checks are priced per health check per month, separately for AWS endpoints and non-AWS endpoints, and calculated and metric based health checks are billed as health checks of an AWS endpoint.
  scope: per health check per month.
  link: [AWS Endpoints](../facts/route53.md#route53-pricing-health-check-aws-vs-non-aws-endpoints)
  link: [Non-AWS Endpoints](../facts/route53.md#route53-pricing-health-check-aws-vs-non-aws-endpoints)
route53-pricing-health-checks-first-50-aws-endpoints-free
  claim: New and existing customers can create up to 50 health checks for AWS endpoints within or linked to the same AWS account at no charge, and health checks of Elastic Load Balancing resources and S3 website bucket endpoints are not billed.
  scope: per AWS account; maximum.
  link: [up to 50 health checks for AWS endpoints](../facts/route53.md#route53-pricing-health-checks-first-50-aws-endpoints-free)
  link: [You are not billed for health checks](../facts/route53.md#route53-pricing-health-checks-first-50-aws-endpoints-free)
