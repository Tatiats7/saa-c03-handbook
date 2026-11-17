facts card: 30 facts
s3-transfer-acceleration-when-to-use
  claim: Use Transfer Acceleration when customers upload to one central bucket from all over the world, when you move gigabytes to terabytes across continents regularly, or when you cannot use all your available bandwidth when uploading to S3.
  scope: per general purpose bucket.
  link: [upload to a centralized general purpose bucket](../facts/s3.md#s3-transfer-acceleration-when-to-use)
  link: [on a regular basis across continents](../facts/s3.md#s3-transfer-acceleration-when-to-use)
  link: [can't use all of your available bandwidth](../facts/s3.md#s3-transfer-acceleration-when-to-use)
s3-transfer-acceleration-how-it-works
  claim: Transfer Acceleration is a bucket-level feature for fast transfers over long distances between a client and a general purpose bucket. It uses CloudFront edge locations: data arrives at an edge location and is routed to S3 over an optimized network path.
  scope: per general purpose bucket.
  link: [secure transfers of files over long distances](../facts/s3.md#s3-transfer-acceleration-how-it-works)
  link: [globally distributed edge locations in Amazon CloudFront](../facts/s3.md#s3-transfer-acceleration-how-it-works)
  link: [over an optimized network path](../facts/s3.md#s3-transfer-acceleration-how-it-works)
s3-presigned-url-time-limited-creator-credentials
  claim: A presigned URL grants time-limited access to an object without changing the bucket policy. The URL uses the credentials of the IAM principal who generated it.
  scope: per presigned URL.
  link: [time-limited access to objects in Amazon S3](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
  link: [principal who generated the URL](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
  link: [time-limited access](../facts/s3.md#s3-presigned-url-time-limited-creator-credentials)
s3-presign-cli-sdk-expiration
  claim: A presigned URL created with the AWS CLI or an SDK can be valid for up to 7 days from the time of creation (Signature Version 4).
  scope: per presigned URL created with the AWS CLI or SDKs; maximum; not adjustable; AWS Signature Version 4; long-lived IAM user credentials.
  link: [7 days](../facts/s3.md#s3-presign-cli-sdk-expiration)
  say: seven days
elb-compare-static-elastic-ip-nlb-only
  claim: In the AWS feature table, only the Network Load Balancer has a static or Elastic IP address; the Application, Gateway and Classic Load Balancers do not.
  scope: Elastic Load Balancing.
  link: [IP address - Static, Elastic](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
  link: [Network Load Balancer](../facts/elb.md#elb-compare-static-elastic-ip-nlb-only)
elb-choose-nlb-for-layer4-extreme-performance-static-ip
  claim: AWS recommends a Network Load Balancer for network and transport protocol (TCP, UDP) load balancing, for extreme performance and low latency, and when the application needs a static IP.
  scope: Elastic Load Balancing.
  link: [network/transport protocols (layer4 – TCP, UDP)](../facts/elb.md#elb-choose-nlb-for-layer4-extreme-performance-static-ip)
  link: [extreme performance and static IP is needed](../facts/elb.md#elb-choose-nlb-for-layer4-extreme-performance-static-ip)
elb-alb-cloudfront-global-reach
  claim: CloudFront acts as a distributed, single point of entry for web applications that use Application Load Balancers and extends the load balancer's reach globally from nearby edge locations.
  scope: Application Load Balancer with CloudFront.
  link: [distributed, single point of entry](../facts/elb.md#elb-alb-cloudfront-global-reach)
  link: [extends your Application Load Balancer's reach globally](../facts/elb.md#elb-alb-cloudfront-global-reach)
elb-nlb-static-ip-per-az-optional-eip
  claim: For a Network Load Balancer, Elastic Load Balancing creates a network interface for each enabled Availability Zone and uses it to get a static IP address; you can optionally associate one Elastic IP address with each network interface when you create the load balancer.
  scope: Network Load Balancer, per enabled Availability Zone; Elastic IP association at creation.
  link: [uses it to get a static IP address](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
  link: [optionally associate one Elastic IP address](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
  link: [when you create the Network Load Balancer](../facts/elb.md#elb-nlb-static-ip-per-az-optional-eip)
route53-alias-target-cloudfront
  claim: An alias record can point to a CloudFront distribution. Route 53 answers with one or more IP addresses for CloudFront edge servers that can serve your content.
  scope: alias target.
  link: [A CloudFront distribution](../facts/route53.md#route53-alias-target-cloudfront)
  link: [IP addresses for CloudFront edge servers](../facts/route53.md#route53-alias-target-cloudfront)
route53-faq-apex-alias-cloudfront
  claim: An alias record can map the zone apex to an Amazon CloudFront distribution.
  scope: alias records to CloudFront.
  link: [your Amazon CloudFront distribution](../facts/route53.md#route53-faq-apex-alias-cloudfront)
route53-cloudfront-requires-alias-record
  claim: You must create an alias record for the CloudFront distribution to work with your domain name.
  scope: routing to CloudFront.
  link: [You must create an Alias record](../facts/route53.md#route53-cloudfront-requires-alias-record)
  link: [for the CloudFront distribution to work](../facts/route53.md#route53-cloudfront-requires-alias-record)
route53-alias-target-global-accelerator
  claim: An alias record can point to an AWS Global Accelerator accelerator. Route 53 answers with the IP addresses for the accelerator.
  scope: alias target.
  link: [An AWS Global Accelerator accelerator](../facts/route53.md#route53-alias-target-global-accelerator)
route53-latency-routing-lowest-latency-region
  claim: With latency-based routing, Route 53 checks which Regions you created latency records for, finds which Region gives the user the lowest latency, and responds with the value from the latency record for that Region.
  scope: latency routing.
  link: [Region gives the user the lowest latency](../facts/route53.md#route53-latency-routing-lowest-latency-region)
  link: [your resources in multiple AWS Regions](../facts/route53.md#route53-latency-routing-lowest-latency-region)
route53-faq-resolver-caches-by-ttl-outside-control
  claim: Caching DNS resolvers are outside the control of Amazon Route 53 and cache record sets according to their TTL, so INSYNC or PENDING describes only the state of the Route 53 authoritative servers.
  scope: caching DNS resolvers.
  link: [according to their time to live (TTL)](../facts/route53.md#route53-faq-resolver-caches-by-ttl-outside-control)
route53-faq-alias-s3-cloudfront-queries-no-charge
  claim: Route 53 does not charge for queries to alias records that are mapped to a CloudFront distribution or to an S3 bucket configured as a website.
  scope: alias records mapped to CloudFront or S3 website buckets.
  link: [doesn't charge for queries to Alias records](../facts/route53.md#route53-faq-alias-s3-cloudfront-queries-no-charge)
route53-cname-not-allowed-at-zone-apex
  claim: You cannot create a CNAME record that has the same name as the hosted zone (the zone apex). This is true for hosted zones for domain names and for hosted zones for subdomains.
  scope: CNAME record.
  link: [You can't create a CNAME record](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
  link: [the same name as the hosted zone](../facts/route53.md#route53-cname-not-allowed-at-zone-apex)
route53-ttl-definition-resolver-cache
  claim: The DNS TTL is the number of seconds that DNS resolvers use to decide how long a record can stay cached before they query Route 53 again.
  scope: per DNS record.
  link: [how long a record can be cached](../facts/route53.md#route53-ttl-definition-resolver-cache)
route53-choose-latency-routing-best-latency-region
  claim: Use the latency routing policy when you have resources in multiple AWS Regions and want to route traffic to the Region that provides the best latency.
  scope: Amazon Route 53 latency routing policy.
  link: [the Region that provides the best latency](../facts/route53.md#route53-choose-latency-routing-best-latency-region)
route53-decision-guide-ga-reliability-latency
  claim: The networking decision guide says AWS Global Accelerator can help you improve the reliability, security and latency of your workloads, and recommends it for gaming, IoT and VoIP workloads.
  scope: AWS Global Accelerator in the networking decision guide.
  link: [reliability, security, and latency of your workloads](../facts/route53.md#route53-decision-guide-ga-reliability-latency)
shield-advanced-resource-types
  claim: Shield Advanced protects CloudFront distributions, Route 53 hosted zones, Global Accelerator standard accelerators, EC2 Elastic IP addresses (and the EC2 instances and Network Load Balancers associated with them), Application Load Balancers and Classic Load Balancers.
  scope: Shield Advanced protections.
  link: [Amazon EC2 instances, through association to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [Network Load Balancers, through associations to Amazon EC2 Elastic IP addresses.](../facts/shield.md#shield-advanced-resource-types)
  link: [AWS Global Accelerator standard accelerators.](../facts/shield.md#shield-advanced-resource-types)
shield-advanced-paid-expanded-protection
  claim: Shield Advanced is a subscription that provides expanded DDoS attack protection for the resources you add protection to, and it incurs additional charges.
  scope: per protected resource; account subscribed and protection added to the resource.
  link: [provides expanded DDoS attack protection](../facts/shield.md#shield-advanced-paid-expanded-protection)
  link: [Shield Advanced incurs additional charges.](../facts/shield.md#shield-advanced-paid-expanded-protection)
waf-cloudfront-web-acl-not-other-types
  claim: A web ACL that you have associated with a CloudFront distribution cannot be associated with any other AWS resource type, though it can be associated with more CloudFront distributions.
  scope: global web ACLs.
  link: [with any other AWS resource type](../facts/waf.md#waf-cloudfront-web-acl-not-other-types)
  link: [one or more CloudFront distributions](../facts/waf.md#waf-cloudfront-web-acl-not-other-types)
waf-protect-sites-outside-aws-via-cloudfront
  claim: AWS WAF can protect websites not hosted in AWS, because it is integrated with Amazon CloudFront, which supports custom origins outside of AWS.
  scope: web ACLs on CloudFront distributions; the site is served through a CloudFront distribution.
  link: [supports custom origins outside of AWS](../facts/waf.md#waf-protect-sites-outside-aws-via-cloudfront)
  link: [integrated with Amazon CloudFront](../facts/waf.md#waf-protect-sites-outside-aws-via-cloudfront)
waf-geo-match-country-and-region
  claim: A geo match statement manages web requests by country and region of origin; it adds country and region labels to every request it evaluates, whether or not the statement matches, and matches against the country of origin.
  scope: per rule statement.
  link: [based on country and region of origin](../facts/waf.md#waf-geo-match-country-and-region)
waf-global-cloudfront-equals-us-east-1
  claim: Choosing the Region option "Global (CloudFront)" in an interface is identical to choosing US East (N. Virginia), us-east-1.
  scope: AWS WAF console and APIs.
  link: [identical to choosing Region US East (N. Virginia)](../facts/waf.md#waf-global-cloudfront-equals-us-east-1)
acm-cloudfront-no-acm-cert-from-other-account
  claim: With certificates provided by ACM, you cannot configure CloudFront to use a certificate that was created by a different AWS account.
  scope: ACM-provided certificates used with CloudFront; the certificate is provided by ACM (not a third-party certificate).
  link: [you can't configure CloudFront to use certificates](../facts/acm.md#acm-cloudfront-no-acm-cert-from-other-account)
  link: [created by a different AWS account](../facts/acm.md#acm-cloudfront-no-acm-cert-from-other-account)
acm-faq-copied-across-regions-only-cloudfront
  claim: ACM copies certificates across Regions only if the certificate is associated with a CloudFront distribution.
  scope: per certificate; associated with a CloudFront distribution.
  link: [only copied across Regions](../facts/acm.md#acm-faq-copied-across-regions-only-cloudfront)
  link: [associated with a CloudFront distribution](../facts/acm.md#acm-faq-copied-across-regions-only-cloudfront)
acm-imported-regional-cloudfront
  claim: Imported certificates are Regional too: import into each Region where a load balancer uses it, and into US East (N. Virginia) for CloudFront.
  scope: per Region.
  link: [including the certificates that you import](../facts/acm.md#acm-imported-regional-cloudfront)
  link: [US East (N. Virginia)](../facts/acm.md#acm-imported-regional-cloudfront)
waf-faq-custom-error-page-via-cloudfront
  claim: You can configure CloudFront to present a custom error page when AWS WAF blocks requests.
  scope: web ACLs on CloudFront distributions.
  link: [a custom error page when requests are blocked](../facts/waf.md#waf-faq-custom-error-page-via-cloudfront)
shield-cloudfront-route53-inline-mitigation
  claim: Applications that serve content with CloudFront and Route 53 are protected by an integrated, fully inline DDoS mitigation system that mitigates infrastructure layer attacks in real time.
  scope: CloudFront distributions and Route 53 hosted zones.
  link: [an integrated, fully inline DDoS mitigation system](../facts/shield.md#shield-cloudfront-route53-inline-mitigation)
  link: [mitigates infrastructure layer attacks in real time](../facts/shield.md#shield-cloudfront-route53-inline-mitigation)
