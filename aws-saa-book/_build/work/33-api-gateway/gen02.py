import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
HE = "| Endpoint types | REST API | HTTP API |"
HS = "| Security features | REST API | HTTP API |"
HA = "| Authorization options | REST API | HTTP API |"
HM = "| Features | REST API | HTTP API |"
HF = "| Feature | REST API | HTTP API |"
fs = []
fs.append(F("edge-optimized-default-rest", "default",
 "The edge-optimized endpoint is the default endpoint type for API Gateway REST APIs; it typically routes requests to the nearest CloudFront Point of Presence (POP).",
 "Which endpoint type is the default for a new REST API?",
 ["default endpoint type for API Gateway REST APIs", "nearest CloudFront Point of Presence (POP)"],
 [ev("api-gateway-api-endpoint-types", "An edge-optimized API endpoint typically routes requests to the nearest CloudFront Point of Presence (POP), which could help in cases where your clients are geographically distributed. This is the default endpoint type for API Gateway REST APIs.")],
 scope="REST APIs", dm="default", bullets=["2.1.K1"], tier0=True))
fs.append(F("edge-optimized-uses-cloudfront-global-clients", "behavior",
 "An edge-optimized API endpoint is the default hostname of an API deployed to the specified Region that uses a CloudFront distribution to facilitate client access, typically from across AWS Regions, and it typically improves connection time for geographically diverse clients.",
 "What does an edge-optimized API endpoint do and when does it help?",
 ["routed to the nearest CloudFront Point of Presence (POP)", "geographically diverse clients"],
 [ev("api-gateway-basic-concept", "The default hostname of an API Gateway API that is deployed to the specified Region while using a CloudFront distribution to facilitate client access typically from across AWS Regions. API requests are routed to the nearest CloudFront Point of Presence (POP), which typically improves connection time for geographically diverse clients.")],
 scope="edge-optimized API endpoints", bullets=["2.1.K1"]))
fs.append(F("regional-endpoint-same-region-clients", "behavior",
 "A Regional API endpoint is intended for clients in the same Region; when a client on an EC2 instance calls an API in the same Region, or an API serves a small number of clients with high demands, a Regional API reduces connection overhead.",
 "Which endpoint type fits clients in the same Region as the API?",
 ["intended for clients in the same Region", "reduces connection overhead"],
 [ev("api-gateway-api-endpoint-types", "A Regional API endpoint is intended for clients in the same Region. When a client running on an EC2 instance calls an API in the same Region, or when an API is intended to serve a small number of clients with high demands, a Regional API reduces connection overhead.")],
 scope="REST APIs, Regional endpoints", bullets=["2.1.K1"], tier0=True))
fs.append(F("regional-endpoint-bypasses-cloudfront", "behavior",
 "API requests to a Regional API endpoint are targeted directly to the Region-specific API without going through any CloudFront distribution, so for in-Region requests a Regional endpoint bypasses the unnecessary round trip to a CloudFront distribution.",
 "Does a Regional API endpoint route requests through CloudFront?",
 ["without going through any CloudFront distribution", "bypasses the unnecessary round trip to a CloudFront distribution"],
 [ev("api-gateway-basic-concept", "API requests are targeted directly to the Region-specific API Gateway API without going through any CloudFront distribution. For in-Region requests, a Regional endpoint bypasses the unnecessary round trip to a CloudFront distribution.")],
 scope="Regional API endpoints", bullets=["2.1.K1"]))
fs.append(F("regional-endpoint-own-cloudfront-distribution", "behavior",
 "When API clients are geographically dispersed, it may still make sense to use a Regional API endpoint together with your own Amazon CloudFront distribution, so that API Gateway does not associate the API with service-controlled CloudFront distributions.",
 "How can you serve geographically dispersed clients with a Regional API and your own CloudFront distribution?",
 ["your own Amazon CloudFront distribution", "service-controlled CloudFront distributions"],
 [ev("api-gateway-api-endpoint-types", "In cases where API clients are geographically dispersed, it may still make sense to use a Regional API endpoint, together with your own Amazon CloudFront distribution to ensure that API Gateway does not associate the API with service-controlled CloudFront distributions.")],
 scope="REST APIs, Regional endpoints", bullets=["2.1.K1"]))
fs.append(F("private-endpoint-vpc-only-interface-endpoint", "restriction",
 "A private API endpoint can only be accessed from your Amazon VPC using an interface VPC endpoint, which is an endpoint network interface (ENI) that you create in your VPC.",
 "From where can a private REST API endpoint be reached?",
 ["can only be accessed from your Amazon Virtual Private Cloud (VPC)", "using an interface VPC endpoint"],
 [ev("api-gateway-api-endpoint-types", "A private API endpoint is an API endpoint that can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network interface (ENI) that you create in your VPC.")],
 scope="REST APIs, private endpoints", bullets=["1.2.K4", "2.1.K1"], tier0=True))
fs.append(F("private-api-isolated-from-internet", "restriction",
 "Private APIs are isolated from the public internet and can only be accessed using VPC endpoints for API Gateway that have been granted access.",
 "How are private APIs isolated, and what grants access to them?",
 ["isolated from the public internet", "VPC endpoints for API Gateway that have been granted access"],
 [ev("api-gateway-basic-concept", "An API endpoint that is exposed through interface VPC endpoints and allows a client to securely access private API resources inside a VPC. Private APIs are isolated from the public internet, and they can only be accessed using VPC endpoints for API Gateway that have been granted access.")],
 scope="REST APIs, private endpoints", bullets=["1.2.K4", "2.1.K1"]))
fs.append(F("edge-optimized-custom-domain-all-regions", "behavior",
 "Any custom domain name that you use for an edge-optimized API applies across all Regions.",
 "Is a custom domain name for an edge-optimized API specific to one Region?",
 ["applies across all regions", "custom domain name that you use for an edge-optimized API"],
 [ev("api-gateway-api-endpoint-types", "Any custom domain name that you use for an edge-optimized API applies across all regions.")],
 scope="REST APIs, edge-optimized endpoints", bullets=["2.1.K1"]))
fs.append(F("regional-custom-domain-region-specific", "behavior",
 "For a Regional API, any custom domain name that you use is specific to the Region where the API is deployed, and if you deploy a Regional API in multiple Regions it can have the same custom domain name in all Regions.",
 "Can the same custom domain name be used for a Regional API deployed in several Regions?",
 ["specific to the Region where the API is deployed", "same custom domain name in all Regions"],
 [ev("api-gateway-api-endpoint-types", "For a Regional API, any custom domain name that you use is specific to the Region where the API is deployed. If you deploy a Regional API in multiple Regions, it can have the same custom domain name in all Regions.")],
 scope="REST APIs, Regional endpoints", bullets=["2.1.K1", "2.2.K10"], tier0=True))
fs.append(F("regional-latency-routing-route53", "capability",
 "You can apply latency-based routing on Regional endpoints to deploy an API to multiple Regions with the same custom domain name and use latency-based DNS records in Route 53 to route client requests to the Region that has the lowest latency.",
 "How do you route clients to the lowest-latency Region for a multi-Region Regional API?",
 ["latency-based DNS records in Route 53", "Region that has the lowest latency"],
 [ev("api-gateway-basic-concept", "In addition, you can apply latency-based routing on Regional endpoints to deploy an API to multiple Regions using the same Regional API endpoint configuration, set the same custom domain name for each deployed API, and configure latency-based DNS records in Route 53 to route client requests to the Region that has the lowest latency.")],
 scope="Regional API endpoints", bullets=["2.1.K1", "2.2.K10"]))
fs.append(F("endpoint-header-names-edge-capitalized", "behavior",
 "Edge-optimized APIs capitalize the names of HTTP headers (for example, Cookie), while Regional and private API endpoints pass all header names through as-is.",
 "How do edge-optimized and Regional endpoints differ in HTTP header names?",
 ["capitalize the names of HTTP headers", "pass all header names through as-is"],
 [ev("api-gateway-api-endpoint-types", "Edge-optimized APIs capitalize the names of HTTP headers (for example, Cookie)."),
  ev("api-gateway-api-endpoint-types", "Regional API endpoints pass all header names through as-is.")],
 scope="REST APIs", bullets=["2.1.K1"], exam="reference"))
fs.append(row("table-edge-optimized-rest-yes-http-no", "Edge-optimized endpoint", "Yes", "No", HE, "Which endpoint types does an HTTP API support, and is edge-optimized one of them?", rowlabel="Edge-optimized", tier0=True))
fs.append(row("table-private-endpoint-rest-yes-http-no", "Private endpoint", "Yes", "No", HE, "Do HTTP APIs support private endpoints?", rowlabel="Private", tier0=True))
fs.append(row("table-regional-endpoint-rest-and-http", "Regional endpoint", "Yes", "Yes", HE, "Which API types support a Regional endpoint?", rowlabel="Regional"))
fs.append(row("table-waf-rest-yes-http-no", "AWS WAF", "Yes", "No", HS, "Which API type can be protected with AWS WAF: REST or HTTP?", bullets=["1.2.K4", "2.1.K1"], tier0=True))
fs.append(row("table-backend-certificates-rest-yes-http-no", "Certificates for backend authentication", "Yes", "No", HS, "Which API type supports certificates for backend authentication?", bullets=["1.2.K4", "2.1.K1"]))
fs.append(row("table-mutual-tls-rest-and-http", "Mutual TLS authentication", "Yes", "Yes", HS, "Do both REST and HTTP APIs support mutual TLS authentication?", bullets=["1.2.K4", "2.1.K1"], rowlabel="Mutual TLS authentication"))
fs.append(row("table-resource-policies-rest-yes-http-no", "Resource policies", "Yes", "No", HA, "Do HTTP APIs support resource policies?", bullets=["1.2.K4", "2.1.K1"], tier0=True))
fs.append(row("table-iam-auth-rest-and-http", "IAM authorization", "Yes", "Yes", HA, "Do both REST and HTTP APIs support IAM authorization?", bullets=["1.2.K4"], rowlabel="IAM"))
fs.append(row("table-lambda-authorizer-rest-and-http", "Custom authorization with an AWS Lambda function", "Yes", "Yes", HA, "Do both REST and HTTP APIs support Lambda authorizers?", bullets=["1.2.K4"]))
fs.append(F("table-jwt-authorizer-http-yes-rest-no", "capability",
 "A JSON Web Token (JWT) authorizer is available for HTTP APIs, not REST APIs: the AWS comparison table lists No for REST APIs and Yes for HTTP APIs, and a Lambda authorizer can validate JWTs for REST APIs.",
 "Does the REST API have a JWT authorizer type?",
 ["JSON Web Token (JWT)", "Lambda authorizer can validate JWTs for REST APIs"],
 [T("http-api-vs-rest", "| JSON Web Token (JWT) 2 | No | Yes |", HA),
  ev("http-api-vs-rest", "You can use a Lambda authorizer to validate JWTs for REST APIs.")],
 scope="REST APIs versus HTTP APIs", bullets=["1.2.K4", "2.1.K1"], tier0=True, hard=True))
write("facts-behavior-02.json", fs)
