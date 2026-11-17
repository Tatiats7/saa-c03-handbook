facts card: 42 facts
acm-change-http-validation-cloudfront-2025
  claim: On 2025-04-24 ACM added HTTP validation of domain ownership for certificates issued for CloudFront distributions.
  scope: certificates for CloudFront distributions.
  link: [2025-04-24](../facts/acm.md#acm-change-http-validation-cloudfront-2025)
  say: April twenty-fourth, twenty twenty-five
acm-cloudfront-managed-certificates
  claim: Certificates that use HTTP validation with CloudFront show CLOUDFRONT in the ManagedBy field and can only be used through CloudFront.
  scope: per CloudFront-managed certificate.
  link: [These certificates can only be used through CloudFront](../facts/acm.md#acm-cloudfront-managed-certificates)
  link: [ManagedBy](../facts/acm.md#acm-cloudfront-managed-certificates)
acm-cloudfront-one-cert-per-distribution
  claim: You can associate only one certificate with each CloudFront distribution.
  scope: per CloudFront distribution; maximum.
  link: [only one certificate with each distribution](../facts/acm.md#acm-cloudfront-one-cert-per-distribution)
  link: [You can associate only one certificate](../facts/acm.md#acm-cloudfront-one-cert-per-distribution)
acm-cloudfront-origin-certificate-any-region
  claim: For HTTPS between CloudFront and an Elastic Load Balancing origin, the load balancer's certificate can be requested or imported in any AWS Region; only the viewer certificate must be in US East (N. Virginia).
  scope: per origin load balancer.
  link: [import the certificate in any AWS Region](../facts/acm.md#acm-cloudfront-origin-certificate-any-region)
  link: [US East (N. Virginia) Region](../facts/acm.md#acm-cloudfront-origin-certificate-any-region)
acm-cloudfront-same-cert-many-distributions
  claim: You can use the same certificate for any or all of the CloudFront distributions that serve HTTPS requests.
  scope: certificates for CloudFront distributions that serve HTTPS.
  link: [the same certificate for any or all](../facts/acm.md#acm-cloudfront-same-cert-many-distributions)
  link: [of the CloudFront distributions](../facts/acm.md#acm-cloudfront-same-cert-many-distributions)
acm-cloudfront-us-east-1
  claim: To use an ACM certificate with Amazon CloudFront, you must request or import it in the US East (N. Virginia) Region; it is then distributed to all locations of the distribution.
  scope: per CloudFront distribution.
  link: [US East (N. Virginia)](../facts/acm.md#acm-cloudfront-us-east-1)
  link: [distributed to all the geographic locations](../facts/acm.md#acm-cloudfront-us-east-1)
acm-http-validation-cloudfront-only
  claim: HTTP validation is for certificates used with CloudFront and is currently available only through the CloudFront Distribution Tenants feature; it uses HTTP redirects and offers automatic renewal like DNS validation.
  scope: per CloudFront certificate.
  link: [only available through the CloudFront Distribution Tenants feature](../facts/acm.md#acm-http-validation-cloudfront-only)
  link: [uses HTTP redirects to prove domain ownership](../facts/acm.md#acm-http-validation-cloudfront-only)
elb-alb-cloudfront-prefix-list-sg
  claim: As a security best practice, an internet-facing ALB behind CloudFront should have security groups that allow inbound traffic only from the AWS-managed prefix list for CloudFront, with other inbound rules removed.
  scope: internet-facing Application Load Balancer behind CloudFront.
  link: [AWS-managed prefix list for CloudFront](../facts/elb.md#elb-alb-cloudfront-prefix-list-sg)
  link: [remove any other inbound rules](../facts/elb.md#elb-alb-cloudfront-prefix-list-sg)
elb-alb-global-accelerator-static-ips
  claim: An accelerator for a load balancer directs traffic over the AWS global network to static IP addresses that serve as fixed endpoints in the Region nearest the client, and AWS Global Accelerator is protected by Shield Standard.
  scope: load balancer with AWS Global Accelerator.
  link: [static IP addresses that serve as fixed endpoints](../facts/elb.md#elb-alb-global-accelerator-static-ips)
  link: [protected by Shield Standard](../facts/elb.md#elb-alb-global-accelerator-static-ips)
elb-change-cloudfront-vpc-origins-2024-11
  claim: On 2024-11-20 Amazon CloudFront added VPC origins, which restrict access to an Application Load Balancer, Network Load Balancer or EC2 instance origin.
  scope: Amazon CloudFront origins.
  link: [2024-11-20](../facts/elb.md#elb-change-cloudfront-vpc-origins-2024-11)
  link: [Use CloudFront VPC origins to restrict access](../facts/elb.md#elb-change-cloudfront-vpc-origins-2024-11)
elb-cloudfront-vpc-origins-alb-nlb-private-subnets
  claim: CloudFront VPC origins let CloudFront deliver content from Application Load Balancers, Network Load Balancers and EC2 instances in private subnets, so the origins need no public access.
  scope: Amazon CloudFront VPC origins.
  link: [Application Load Balancers (ALBs), Network Load Balancers (NLBs)](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
  link: [in private subnets as VPC origins](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
  link: [private subnets with no public access](../facts/elb.md#elb-cloudfront-vpc-origins-alb-nlb-private-subnets)
elb-cloudfront-vpc-origins-nlb-restrictions
  claim: A Network Load Balancer used as a CloudFront VPC origin must have a security group attached, and a Network Load Balancer with TLS listeners cannot be a VPC origin.
  scope: Amazon CloudFront VPC origins.
  link: [with TLS listeners cannot be added](../facts/elb.md#elb-cloudfront-vpc-origins-nlb-restrictions)
  link: [must have a security group attached to it](../facts/elb.md#elb-cloudfront-vpc-origins-nlb-restrictions)
global-infrastructure-cloudfront-content-served-during-control-plane-impairment
  claim: During a CloudFront control plane impairment the CRUDL operations, including invalidations, may not work, but content continues to be cached and served and origin failovers continue to work.
  link: [your content will continue to be cached and served](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
  link: [origin failovers will continue to work](../facts/global-infrastructure.md#global-infrastructure-cloudfront-content-served-during-control-plane-impairment)
global-infrastructure-edge-location-services
  claim: Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield and AWS WAF are provided through AWS edge locations.
  scope: AWS edge locations.
  link: [Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS Shield, and AWS WAF services are provided through AWS Edge Locations](../facts/global-infrastructure.md#global-infrastructure-edge-location-services)
  say: CloudFront, Route 53, Firewall Manager, Shield and WAF are provided through the edge locations
global-infrastructure-edge-locations-connected-to-regions-by-backbone
  claim: Edge locations connect to the Regions through the AWS network backbone, a fully redundant, multiple 100GbE parallel fiber that circles the globe.
  link: [connected to the AWS Regions through the AWS network backbone](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
  link: [multiple 100GbE parallel fiber](../facts/global-infrastructure.md#global-infrastructure-edge-locations-connected-to-regions-by-backbone)
global-infrastructure-edge-network-global-services-route53-example
  claim: Edge network global services keep their control plane in the aws partition and run their data planes in the points of presence; Route 53, for example, has its control plane in us-east-1 and a data plane spread across hundreds of PoPs and every Region.
  link: [host their data planes in the global points of presence (PoP) infrastructure](../facts/global-infrastructure.md#global-infrastructure-edge-network-global-services-route53-example)
  link: [Route 53 operates its control plane in the us-east-1 Region, but its data plane is distributed across hundreds of PoPs globally](../facts/global-infrastructure.md#global-infrastructure-edge-network-global-services-route53-example)
global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator
  claim: AWS points of presence host Amazon CloudFront (a CDN), Amazon Route 53 (public DNS) and AWS Global Accelerator (edge networking optimization), in addition to the Regions and Availability Zones.
  scope: AWS edge network.
  link: [Amazon CloudFront](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [Amazon Route 53](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
  link: [AWS Global Accelerator](../facts/global-infrastructure.md#global-infrastructure-pop-hosts-cloudfront-route53-global-accelerator)
lambda-edge-event-sources-row
  claim: CloudFront Functions run only on viewer request and viewer response events, while Lambda@Edge also runs on origin request and origin response events.
  scope: CloudFront Functions versus Lambda@Edge.
  link: [Origin request](../facts/lambda.md#lambda-edge-event-sources-row)
lambda-edge-network-access-row
  claim: CloudFront Functions have no network access, while Lambda@Edge functions do.
  scope: CloudFront Functions versus Lambda@Edge.
  link: [Network access | No](../facts/lambda.md#lambda-edge-network-access-row)
  say: CloudFront Functions have no network access
lambda-faq-edge-cloudfront-triggers
  claim: Lambda@Edge runs Node.js or Python code in response to CloudFront requests: when a viewer request lands, when a request is forwarded to or received back from the origin, and right before responding to the end-user.
  scope: Lambda@Edge with CloudFront.
  link: [Amazon CloudFront requests](../facts/lambda.md#lambda-faq-edge-cloudfront-triggers)
lambda-faq-edge-existing-functions
  claim: You can associate existing Lambda functions with CloudFront events for global invocation if the function satisfies the Lambda@Edge service requirements and limits.
  scope: per function; the function satisfies the Lambda@Edge service requirements and limits.
  link: [satisfies the Lambda@Edge service requirements and limits](../facts/lambda.md#lambda-faq-edge-existing-functions)
lambda-faq-edge-function-version
  claim: To use Lambda@Edge, you upload your code to AWS Lambda and associate a function version to be triggered in response to Amazon CloudFront requests.
  scope: Lambda@Edge association with CloudFront.
  link: [function version](../facts/lambda.md#lambda-faq-edge-function-version)
lambda-faq-edge-runtimes
  claim: Lambda@Edge supports Node.js and Python for global invocation by CloudFront events.
  scope: Lambda@Edge.
  link: [Node.js and Python](../facts/lambda.md#lambda-faq-edge-runtimes)
lambda-faq-edge-when
  claim: Lambda@Edge is for latency-sensitive use cases with globally distributed viewers, where everything needed for the decision is available at the CloudFront edge, within the function and the request.
  scope: Lambda@Edge use cases.
  link: [latency-sensitive use cases](../facts/lambda.md#lambda-faq-edge-when)
  link: [distributed globally](../facts/lambda.md#lambda-faq-edge-when)
s3-cloudfront-oai-bucket-policy
  claim: A bucket policy can grant a CloudFront origin access identity (OAI) permission to get (read) all objects in the bucket, so that users can access the objects through CloudFront but not directly through Amazon S3.
  scope: per bucket policy.
  link: [through CloudFront but not directly through Amazon S3](../facts/s3.md#s3-cloudfront-oai-bucket-policy)
  link: [origin access identity (OAI)](../facts/s3.md#s3-cloudfront-oai-bucket-policy)
s3-faq-mrap-global-accelerator
  claim: Multi-Region Access Points, based on AWS Global Accelerator, route requests over the AWS network to the lowest-latency replicated copy and improve performance by up to 60%.
  scope: per Multi-Region Access Point.
  link: [up to 60%](../facts/s3.md#s3-faq-mrap-global-accelerator)
  link: [Based on AWS Global Accelerator](../facts/s3.md#s3-faq-mrap-global-accelerator)
  say: up to sixty percent
s3-faq-ta-edge-locations
  claim: S3 Transfer Acceleration uses CloudFront’s globally distributed edge locations; data arriving at an edge location is routed to the bucket over an optimized network path.
  scope: per accelerated transfer.
  link: [optimized network path](../facts/s3.md#s3-faq-ta-edge-locations)
s3-pricing-data-transfer-to-cloudfront-free
  claim: You pay for all bandwidth into and out of Amazon S3 except for some transfers; data transferred out to Amazon CloudFront is one of these exceptions.
  scope: data transfer out of S3; destination is Amazon CloudFront.
  link: [Data transferred out to Amazon CloudFront](../facts/s3.md#s3-pricing-data-transfer-to-cloudfront-free)
s3-transfer-acceleration-no-data-at-edge
  claim: Transfer Acceleration keeps the same security as regular S3 transfers, works over standard TCP without firewall changes, and never stores data at the edge locations.
  scope: per accelerated transfer.
  link: [No data is ever saved](../facts/s3.md#s3-transfer-acceleration-no-data-at-edge)
  link: [the same security as regular transfers](../facts/s3.md#s3-transfer-acceleration-no-data-at-edge)
s3-transfer-acceleration-vs-cloudfront-small-objects
  claim: Transfer Acceleration is the better choice when higher throughput is wanted. For objects smaller than 1 GB or a data set under 1 GB, AWS says to consider CloudFront PUT/POST instead.
  scope: upload path choice; object or data set size under 1 GB.
  link: [if a higher throughput is desired](../facts/s3.md#s3-transfer-acceleration-vs-cloudfront-small-objects)
  link: [smaller than 1 GB](../facts/s3.md#s3-transfer-acceleration-vs-cloudfront-small-objects)
s3-war-avoid-public-buckets-use-cloudfront
  claim: Well-Architected guidance: review bucket policies regularly, avoid publicly readable or writable buckets unless absolutely necessary, detect public buckets with AWS Config, and serve content from S3 through Amazon CloudFront.
  scope: S3 bucket policies.
  link: [Avoid using publicly readable or writeable buckets](../facts/s3.md#s3-war-avoid-public-buckets-use-cloudfront)
  link: [Amazon CloudFront to serve content from Amazon S3](../facts/s3.md#s3-war-avoid-public-buckets-use-cloudfront)
s3-website-sse-kms-needs-cloudfront-oac
  claim: A static website bucket encrypted with SSE-KMS must be served through a CloudFront distribution, because SSE-KMS does not support anonymous users; the distribution must use origin access control (OAC), since OAI does not support SSE-KMS.
  scope: static website buckets using SSE-KMS.
  link: [SSE-KMS doesn't support anonymous users](../facts/s3.md#s3-website-sse-kms-needs-cloudfront-oac)
  link: [you must use OAC instead](../facts/s3.md#s3-website-sse-kms-needs-cloudfront-oac)
shield-protect-sites-outside-aws-via-cloudfront
  claim: AWS Shield can protect websites not hosted in AWS, because it is integrated with Amazon CloudFront, which supports custom origins outside of AWS.
  scope: resources behind CloudFront; the site is served through CloudFront.
  link: [supports custom origins outside of AWS](../facts/shield.md#shield-protect-sites-outside-aws-via-cloudfront)
shield-standard-best-on-edge-resources
  claim: Shield Standard gives particular benefit to Amazon Route 53 hosted zones, CloudFront distributions and Global Accelerator standard accelerators, which receive comprehensive availability protection against all known network and transport layer attacks.
  scope: Route 53 hosted zones, CloudFront distributions, Global Accelerator standard accelerators.
  link: [you get particular benefit with Amazon Route 53 hosted zones](../facts/shield.md#shield-standard-best-on-edge-resources)
  link: [against all known network and transport layer attacks](../facts/shield.md#shield-standard-best-on-edge-resources)
shield-standard-every-region-edge
  claim: AWS Shield Standard is available on all AWS services in every AWS Region and AWS edge location worldwide.
  scope: AWS Shield Standard.
  link: [every AWS Region and AWS edge location worldwide](../facts/shield.md#shield-standard-every-region-edge)
waf-alb-behind-cloudfront-token-cookie
  claim: When a web ACL protects an Application Load Balancer that is the origin of a CloudFront distribution, you must configure CloudFront to forward the aws-waf-token cookie, because by default CloudFront removes cookies before forwarding a request to the origin.
  scope: web ACL on an ALB that is a CloudFront origin; rules that use tokens (CAPTCHA, Challenge, intelligent threat mitigation).
  link: [CloudFront removes cookies from the web request](../facts/waf.md#waf-alb-behind-cloudfront-token-cookie)
  link: [keep the token cookie with the web request](../facts/waf.md#waf-alb-behind-cloudfront-token-cookie)
waf-cloudfront-flat-rate-includes-waf
  claim: CloudFront flat-rate pricing plans combine the CloudFront CDN with several AWS services and features, including AWS WAF and DDoS protection, into a monthly price with no overage charges, regardless of traffic spikes or attacks.
  scope: CloudFront flat-rate pricing plans.
  link: [into a monthly price with no overage charges](../facts/waf.md#waf-cloudfront-flat-rate-includes-waf)
  link: [regardless of traffic spikes or attacks](../facts/waf.md#waf-cloudfront-flat-rate-includes-waf)
waf-cloudfront-flat-rate-keeps-web-acl
  claim: When a CloudFront distribution uses a flat-rate pricing plan, a valid AWS WAF web ACL must remain associated with it; you cannot remove the association unless you switch back to pay-as-you-go pricing.
  scope: CloudFront distributions on flat-rate pricing plans.
  link: [must remain associated with your CloudFront distribution](../facts/waf.md#waf-cloudfront-flat-rate-keeps-web-acl)
  link: [unless you switch back to pay-as-you-go pricing](../facts/waf.md#waf-cloudfront-flat-rate-keeps-web-acl)
waf-cloudfront-rules-run-at-edge
  claim: When you use AWS WAF on CloudFront, your rules run in all AWS edge locations close to end users, and blocked requests are stopped before they reach your web servers.
  scope: web ACLs on CloudFront distributions.
  link: [your rules run in all AWS Edge Locations](../facts/waf.md#waf-cloudfront-rules-run-at-edge)
  link: [stopped before they reach your web servers](../facts/waf.md#waf-cloudfront-rules-run-at-edge)
waf-cloudfront-standard-distribution-one-web-acl
  claim: For CloudFront standard distributions, AWS WAF adds protection with a single web ACL for each distribution, and you can enable it by associating an existing web ACL or with one-click protection in the CloudFront console.
  scope: CloudFront standard distributions.
  link: [single protection pack (web ACL) for each distribution](../facts/waf.md#waf-cloudfront-standard-distribution-one-web-acl)
  link: [by using one-click protection in the CloudFront console](../facts/waf.md#waf-cloudfront-standard-distribution-one-web-acl)
waf-cloudfront-web-acl-us-east-1
  claim: AWS WAF is available globally for CloudFront distributions, but you must use US East (N. Virginia) to create the web ACL and any resources it uses, such as rule groups, IP sets and regex pattern sets.
  scope: web ACLs for CloudFront distributions.
  link: [available globally for CloudFront distributions](../facts/waf.md#waf-cloudfront-web-acl-us-east-1)
  link: [use the Region US East (N. Virginia)](../facts/waf.md#waf-cloudfront-web-acl-us-east-1)
route53-global-accelerator-alias-record
  claim: To route a domain to an accelerator, you create an alias record with the target Alias to Global Accelerator, using the DNS name of the accelerator, which can be from the current account or a different account.
  scope: alias to Global Accelerator.
  link: [Alias to Global Accelerator](../facts/route53.md#route53-global-accelerator-alias-record)
  link: [Choose the DNS name for the accelerator](../facts/route53.md#route53-global-accelerator-alias-record)
