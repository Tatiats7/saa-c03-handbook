import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
DF = "dns-failover"
fs = []
fs.append(F("resilience-route53-health-checks-dns-failover", "capability",
 "You can use Amazon Route 53 health checks to control DNS failover from an API Gateway API in a primary Region to an API Gateway API in a secondary Region, which can help mitigate the impact of a Regional issue; with a custom domain you can fail over without requiring clients to change API endpoints.",
 "How do you fail over an API Gateway API to a second Region?",
 ["Amazon Route 53 health checks to control DNS failover", "without requiring clients to change API endpoints"],
 [ev(DF, "You can use Amazon Route 53 health checks to control DNS failover from an API Gateway API in a primary AWS Region to one in a secondary Region. This can help mitigate impacts in the event of a Regional issue. If you use a custom domain, you can perform failover without requiring clients to change API endpoints.")],
 scope="multi-Region API Gateway APIs", bullets=["2.2.K10"], tier0=True))
fs.append(F("resilience-evaluate-target-health-only-service-unavailable", "behavior",
 "When you choose Evaluate Target Health for an alias record, those records fail only when the API Gateway service is unavailable in the Region, so your own APIs can experience interruption before that; to control DNS failover directly, configure custom Amazon Route 53 health checks for your API Gateway APIs.",
 "Why use custom Route 53 health checks instead of Evaluate Target Health for an API Gateway alias record?",
 ["fail only when the API Gateway service is unavailable in the Region", "configure custom Route 53 health checks"],
 [ev(DF, "When you choose [Evaluate Target Health](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AliasTarget.html#Route53-Type-AliasTarget-EvaluateTargetHealth>Evaluate Target Health) for an alias record, those records fail only when the API Gateway service is unavailable in the Region. In some cases, your own API Gateway APIs can experience interruption before that time. To control DNS failover directly, configure custom Route 53 health checks for your API Gateway APIs.")],
 scope="Amazon Route 53 alias records to API Gateway", bullets=["2.2.K10"], hard=True, tier0=True))
fs.append(F("resilience-failover-prerequisites", "restriction",
 "To set up DNS failover for an API Gateway API you must have an ACM certificate for your domain name in two AWS Regions.",
 "What certificate setup does DNS failover between two Regions need?",
 ["An ACM certificate for that domain name in two AWS Regions", "certificate for that domain name"],
 [ev(DF, "An ACM certificate for that domain name in two AWS Regions. For more info, see Prerequisites for custom domain names.")],
 scope="multi-Region API Gateway APIs", bullets=["2.2.K10"], exam="extended"))
fs.append(F("resilience-failover-same-custom-domain-name-two-regions", "behavior",
 "In the DNS failover example you create API Gateway APIs in two AWS Regions, custom domain names with the same name in two Regions, API mappings that connect the APIs to the domain names, Amazon Route 53 failover DNS records, a CloudWatch alarm in the secondary Region and a Route 53 health check based on that alarm.",
 "Which resources make up a two-Region API Gateway failover setup?",
 ["custom domain names with the same name in two AWS Regions", "Route 53 failover DNS records for the domain names"],
 [ev(DF, "API Gateway APIs in two AWS Regions API Gateway custom domain names with the same name in two AWS Regions API Gateway API mappings that connect your API Gateway APIs to the custom domain names Route 53 failover DNS records for the domain names A CloudWatch alarm in the secondary Region A Route 53 health check based on the CloudWatch alarm in the secondary Region")],
 scope="multi-Region API Gateway APIs", bullets=["2.2.K10"], tier0=True, hard=True))
fs.append(F("resilience-alarm-health-check-in-secondary-region", "behavior",
 "In the DNS failover example the secondary Region contains the CloudWatch alarm and the Amazon Route 53 health check, so that you do not depend on the primary Region to perform failover.",
 "In which Region should the failover alarm and health check be placed?",
 ["secondary Region should contain the alarm and health check", "you don't depend on the primary Region to perform failover"],
 [ev(DF, "The secondary Region should contain the alarm and health check. This way, you don't depend on the primary Region to perform failover.")],
 scope="multi-Region API Gateway APIs", bullets=["2.2.K10"], exam="extended"))
write("facts-behavior-10b.json", fs)
