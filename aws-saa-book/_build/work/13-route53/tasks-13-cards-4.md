facts card: 14 facts
route53-faq-insync-means-all-servers
  claim: When the status of a change is INSYNC, the change has been performed on all of the Route 53 DNS servers.
  scope: ChangeResourceRecordSets calls.
  link: [INSYNC](../facts/route53.md#route53-faq-insync-means-all-servers)
route53-default-unique-delegation-set-per-zone
  claim: By default, Route 53 assigns a unique set of four name servers, called a delegation set, to each hosted zone that you create.
  scope: each hosted zone you create; default; not adjustable; reusable delegation set not used.
  link: [a unique set of four name servers](../facts/route53.md#route53-default-unique-delegation-set-per-zone)
  link: [called a delegation set](../facts/route53.md#route53-default-unique-delegation-set-per-zone)
  say: four name servers
route53-public-zone-creates-ns-and-soa
  claim: For each public hosted zone that you create, Amazon Route 53 automatically creates a name server (NS) record and a start of authority (SOA) record.
  scope: per public hosted zone.
  link: [automatically creates a name server (NS) record](../facts/route53.md#route53-public-zone-creates-ns-and-soa)
route53-zone-creates-ns-and-soa
  claim: When you create a hosted zone, Route 53 creates a name server (NS) record and a start of authority (SOA) record for it. The NS record lists the four name servers that you give to your registrar or DNS service so that DNS queries reach Route 53 name servers.
  scope: public hosted zone.
  link: [a start of authority (SOA) record](../facts/route53.md#route53-zone-creates-ns-and-soa)
  link: [lists the four name servers](../facts/route53.md#route53-zone-creates-ns-and-soa)
  say: four name servers
route53-cname-not-allowed-at-zone-apex
  claim: You cannot create a CNAME record that has the same name as the hosted zone (the zone apex). This is true for hosted zones for domain names and for hosted zones for subdomains.
  scope: CNAME record.
  link: [You can't create a CNAME record](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
  link: [the same name as the hosted zone](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
route53-alias-apex-exception-cname-target
  claim: The one exception for an alias record at the zone apex is a redirect to a record of type CNAME in the same hosted zone; the alias record must have the same type as the record it routes to, and a CNAME record for the zone apex is not supported even for an alias record.
  scope: Amazon Route 53 alias record at the zone apex; The alias target is a record in the same hosted zone..
  link: [a type of CNAME](../facts/route53.md#route53-alias-apex-exception-cname-target)
  link: [must have the same type](../facts/route53.md#route53-alias-apex-exception-cname-target)
route53-alias-to-record-in-zone-uses-target-ttl
  claim: If an alias record points to another record in the same hosted zone, Route 53 uses the TTL of the target record.
  scope: alias record to another record in the same hosted zone.
  link: [uses the TTL of the target record](../facts/route53.md#route53-alias-to-record-in-zone-uses-target-ttl)
route53-pricing-alias-to-record-in-zone-standard-rate
  claim: Amazon Route 53 charges the standard rate for a query that matches an alias record whose target is a non-alias record in the same hosted zone, but a chain of alias records that ends at an AWS resource such as an Elastic Load Balancer is free.
  scope: Amazon Route 53 alias queries.
  link: [We charge the standard rate](../facts/route53.md#route53-pricing-alias-to-record-in-zone-standard-rate)
  link: [a chain of alias records](../facts/route53.md#route53-pricing-alias-to-record-in-zone-standard-rate)
route53-migrate-alias-records-last
  claim: When you migrate a hosted zone by editing the exported records file, and the zone contains aliases that refer to other records in the same hosted zone, move the alias records to the bottom of the file, because Route 53 must create the record that an alias record refers to before it can create the alias record. If an alias record refers to another alias record, the alias target must appear first in the file.
  scope: hosted zone migration by file; the hosted zone contains aliases that refer to other records in the same hosted zone.
  link: [Move the alias records to the bottom](../facts/route53.md#route53-migrate-alias-records-last)
  link: [must create the record that an alias record](../facts/route53.md#route53-migrate-alias-records-last)
route53-changes-propagate-within-60-seconds
  claim: Changes to Route 53 records generally propagate to all Route 53 servers within 60 seconds.
  scope: record changes in Route 53; maximum; generally.
  link: [within 60 seconds](../facts/route53.md#route53-changes-propagate-within-60-seconds)
  link: [Changes generally propagate to all Route 53 servers](../facts/route53.md#route53-changes-propagate-within-60-seconds)
  say: within sixty seconds
route53-faq-alias-type-a-or-aaaa-like-cname
  claim: An alias record usually has the type A or AAAA but works like a CNAME record.
  scope: alias records.
  link: [type of A or AAAA](../facts/route53.md#route53-faq-alias-type-a-or-aaaa-like-cname)
route53-alias-answers-only-on-matching-name-and-type
  claim: Route 53 answers a query for an alias record only when the name and the type of the alias record match the name and type in the DNS query.
  scope: alias record.
  link: [the name and type in the DNS query](../facts/route53.md#route53-alias-answers-only-on-matching-name-and-type)
  link: [responds to a DNS query only when](../facts/route53.md#route53-alias-answers-only-on-matching-name-and-type)
route53-health-check-alias-record-not-recommended
  claim: You can associate health checks with alias records, but AWS recommends associating health checks only with non-alias records.
  scope: health checks and alias records.
  link: [associate health checks only with non-alias records](../facts/route53.md#route53-health-check-alias-record-not-recommended)
  link: [You can associate health checks with alias records](../facts/route53.md#route53-health-check-alias-record-not-recommended)
route53-faq-domain-delegation-set-four-name-servers
  claim: When a domain is created it is automatically associated with four unique Amazon Route 53 name servers, known as a delegation set, and by default each hosted zone gets a new, unique delegation set.
  scope: per domain, per hosted zone; default.
  link: [four unique Route 53 name servers](../facts/route53.md#route53-faq-domain-delegation-set-four-name-servers)
