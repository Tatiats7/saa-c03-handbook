facts card: 13 facts
route53-record-without-health-check-always-healthy
  claim: If a record in a group of records with the same name and type has no associated health check, Route 53 always considers it healthy and always includes it among possible responses.
  scope: records without a health check.
  link: [always considers it healthy](../facts/route53.md#route53-record-without-health-check-always-healthy)
  link: [always includes it among possible responses](../facts/route53.md#route53-record-without-health-check-always-healthy)
route53-failover-secondary-health-check-optional
  claim: When you configure the secondary failover record, adding a health check is optional. If you omit it and the primary endpoint is unhealthy, Route 53 always answers with the secondary record, even if the secondary record is unhealthy.
  scope: secondary failover record.
  link: [adding a health check is optional](../facts/route53.md#route53-failover-secondary-health-check-optional)
  link: [by using the secondary record](../facts/route53.md#route53-failover-secondary-health-check-optional)
route53-failover-needs-one-primary-one-secondary
  claim: For failover to work correctly, you must create one primary and one secondary failover record.
  scope: failover routing.
  link: [one primary and one secondary failover record](../facts/route53.md#route53-failover-needs-one-primary-one-secondary)
  link: [For failover to function correctly](../facts/route53.md#route53-failover-needs-one-primary-one-secondary)
route53-failover-routing-primary-or-secondary
  claim: With failover routing, you route traffic to a resource when it is healthy, or to a different resource when the first one is unhealthy. The primary and secondary records can route traffic to anything from an S3 website bucket to a complex tree of records.
  scope: failover routing.
  link: [when the first one is unhealthy](../facts/route53.md#route53-failover-routing-primary-or-secondary)
  link: [anything from an Amazon S3 bucket set up as a website to a complex tree of records](../facts/route53.md#route53-failover-routing-primary-or-secondary)
route53-complex-config-omitted-health-check-assumed-healthy
  claim: In a complex configuration, a non-alias record without a health check is assumed to be healthy, because Route 53 has no way to know whether the resource is healthy. It is important to associate health checks with all non-alias records.
  scope: complex configurations.
  link: [Route 53 assumes that the resource is healthy](../facts/route53.md#route53-complex-config-omitted-health-check-assumed-healthy)
  link: [associate health checks with all the non-alias records](../facts/route53.md#route53-complex-config-omitted-health-check-assumed-healthy)
route53-hc-calculated-monitors-other-health-checks
  claim: A calculated health check monitors whether Route 53 considers other health checks healthy or unhealthy. It can notify you only when the number of available resources drops below a threshold.
  scope: calculated health check.
  link: [monitors whether Route 53 considers other health checks healthy or unhealthy](../facts/route53.md#route53-hc-calculated-monitors-other-health-checks)
  link: [available web resources drops below a specified threshold](../facts/route53.md#route53-hc-calculated-monitors-other-health-checks)
route53-failover-record-health-check-checks-its-own-endpoint
  claim: Amazon Route 53 does not check the health of the endpoint in the record value; when you select a health check for a record, Route 53 checks the endpoint that you specified in the health check.
  scope: Amazon Route 53 records and health checks.
  link: [endpoint that you specified in the health check](../facts/route53.md#route53-failover-record-health-check-checks-its-own-endpoint)
route53-dns-failover-routes-traffic-away-from-unhealthy-record
  claim: For multiple resources that perform the same function, you can configure DNS failover: associate a health check with each record, and if a health check finds the resource unhealthy, Route 53 routes traffic away from the associated record.
  scope: DNS failover.
  link: [Associate a health check with each record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record)
  link: [Route 53 routes traffic away from the associated record](../facts/route53.md#route53-dns-failover-routes-traffic-away-from-unhealthy-record)
route53-rel10-failover-records-short-ttl
  claim: For DNS records used for failover, the Well-Architected reliability pillar says to specify a short time to live (for example, 60 seconds or less) so record caching does not impede recovery, and notes that Amazon Route 53 alias records supply appropriate TTLs for you.
  scope: DNS records used for failover; maximum; adjustable; Applies to non-alias records; alias records supply appropriate TTLs..
  link: [60 seconds or less](../facts/route53.md#route53-rel10-failover-records-short-ttl)
route53-faq-failover-returns-only-healthy-answers
  claim: With DNS failover, Amazon Route 53 returns answers only for resources that are healthy and reachable from the outside world, so end users are routed away from a failed or unhealthy part of the application.
  scope: DNS Failover.
  link: [only returns answers for resources that are healthy](../facts/route53.md#route53-faq-failover-returns-only-healthy-answers)
route53-hc-calculated-no-nesting
  claim: A calculated health check cannot monitor other calculated health checks.
  scope: per calculated health check.
  link: [can't configure a calculated health check](../facts/route53.md#route53-hc-calculated-no-nesting)
route53-quota-calculated-child-health-checks
  claim: One calculated health check can monitor up to 255 child health checks.
  scope: per calculated health check; maximum; not adjustable.
  link: [255 child health checks](../facts/route53.md#route53-quota-calculated-child-health-checks)
route53-hc-calculated-healthy-count-compare
  claim: For a calculated health check, Route 53 adds up the number of child health checks that are considered healthy and compares that number with the number of child health checks that must be healthy for the parent health check to be considered healthy.
  scope: per calculated health check.
  link: [child health checks that must be healthy](../facts/route53.md#route53-hc-calculated-healthy-count-compare)
