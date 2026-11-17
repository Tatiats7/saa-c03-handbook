facts card: 12 facts
route53-pricing-query-types-four-rates
  claim: The Route 53 usage report has four query types: standard queries (records with failover, multivalue answer and weighted routing policies) as Intra-AWS-DNS-Queries, latency-based routing queries as Intra-AWS-LBR-Queries, geo routing queries (geolocation and geoproximity) as Intra-AWS-Geo-Queries, and IP-based routing queries as Intra-AWS-Cidr-Queries.
  scope: query types on the Route 53 usage report.
  link: [Intra-AWS-DNS-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-LBR-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-Geo-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
  link: [Intra-AWS-Cidr-Queries](../facts/route53.md#route53-pricing-query-types-four-rates)
route53-faq-hosted-zone-billed-at-creation-and-monthly
  claim: A hosted zone is billed once when it is created and then on the first day of each month.
  scope: per hosted zone.
  link: [first day of each month](../facts/route53.md#route53-faq-hosted-zone-billed-at-creation-and-monthly)
route53-pricing-hosted-zone-monthly-not-prorated
  claim: Each Amazon Route 53 hosted zone is billed per month, at a lower price for hosted zones beyond the first 25; the monthly price is not prorated for partial months, and the zone is charged when it is created and on the first day of each later month.
  scope: per hosted zone per month.
  link: [not prorated for partial months](../facts/route53.md#route53-pricing-hosted-zone-monthly-not-prorated)
  link: [for the first 25 hosted zones](../facts/route53.md#route53-pricing-hosted-zone-monthly-not-prorated)
route53-faq-hosted-zone-12-hour-grace-period
  claim: If you delete a hosted zone within 12 hours after you create it, you are not charged for it; after the grace period the standard monthly fee applies immediately.
  scope: per hosted zone; fixed; zone deleted within 12 hours of creation.
  link: [grace period of 12 hours](../facts/route53.md#route53-faq-hosted-zone-12-hour-grace-period)
  say: twelve hours
route53-hc-disabled-still-charged
  claim: Charges for a health check still apply when the health check is disabled.
  scope: disabled health check.
  link: [Charges for a health check still apply](../facts/route53.md#route53-hc-disabled-still-charged)
route53-pricing-missing-record-and-type-mismatch-charged
  claim: Amazon Route 53 charges the standard rate for queries for a record that does not exist and for queries whose name matches a record but whose type does not, so creating both A and AAAA records is recommended where applicable.
  scope: Amazon Route 53 DNS queries.
  link: [Queries for a record that doesn't exist](../facts/route53.md#route53-pricing-missing-record-and-type-mismatch-charged)
  link: [create both A and AAAA records](../facts/route53.md#route53-pricing-missing-record-and-type-mismatch-charged)
route53-dangling-delegation-protection-on-zone-delete
  claim: After a hosted zone is deleted, if a new hosted zone is created with the same domain name, Route 53 checks whether the delegation records still point to the deleted zone and, if they do, prevents overlapping name servers from being assigned.
  scope: deleted hosted zones.
  link: [Route 53 will check if the delegation records pointing to the deleted hosted zone are still present](../facts/route53.md#route53-dangling-delegation-protection-on-zone-delete)
  link: [Route 53 will prevent any overlapping name servers from being assigned](../facts/route53.md#route53-dangling-delegation-protection-on-zone-delete)
route53-faq-pricing-dimensions-and-no-minimums
  claim: Amazon Route 53 charges are based on actual usage for hosted zones, queries, health checks and domain names, with no minimum fees, no minimum usage commitments and no overage charges.
  scope: Route 53 pricing.
  link: [Hosted Zones, Queries, Health Checks, and Domain Names](../facts/route53.md#route53-faq-pricing-dimensions-and-no-minimums)
route53-pricing-pay-per-zone-and-query-no-minimums
  claim: There are no contracts or minimum commitments for Amazon Route 53; you pay only for the hosted zones that you configure and the number of DNS queries that Route 53 answers.
  scope: Amazon Route 53 DNS.
  link: [pay only for the hosted zones](../facts/route53.md#route53-pricing-pay-per-zone-and-query-no-minimums)
route53-pricing-health-check-optional-features
  claim: Optional health check features, which include HTTPS, string matching, fast request interval and latency measurement, add a charge per optional feature per month, with separate rates for AWS endpoints and non-AWS endpoints.
  scope: per optional health check feature per month.
  link: [HTTPS, string matching; fast request interval, and latency](../facts/route53.md#route53-pricing-health-check-optional-features)
route53-faq-health-check-cloudwatch-metrics-free
  claim: CloudWatch metrics for Route 53 health checks are available free of charge.
  scope: CloudWatch metrics of health checks.
  link: [available free of charge](../facts/route53.md#route53-faq-health-check-cloudwatch-metrics-free)
route53-pricing-hosted-zone-includes-10000-records
  claim: A hosted zone includes up to 10,000 records; each record above 10,000 per hosted zone is charged a monthly fee.
  scope: per hosted zone; maximum; Each record above 10,000 per hosted zone is charged per month.
  link: [up to 10,000 records](../facts/route53.md#route53-pricing-hosted-zone-includes-10000-records)
