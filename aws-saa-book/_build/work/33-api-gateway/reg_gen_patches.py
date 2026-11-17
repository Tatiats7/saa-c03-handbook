"""Registrar register-33: builds the amend patches for chapter 33 (one JSON file per fact)
and reg-decisions.json (supersedes). Checks every number-free display against the quotes
(<= 8 words, verbatim after normalize_text) before writing.
Run: python3 -I aws-saa-book/_build/work/33-api-gateway/reg_gen_patches.py <repo root>"""
import json, os, re, sys, copy

ROOT = sys.argv[1]
sys.path.insert(0, ROOT + "/aws-saa-book/tools")
from saalib import common, lint  # noqa: E402

W = ROOT + "/aws-saa-book/_build/work/33-api-gateway/"
OUT = W + "reg-patches"
os.makedirs(OUT, exist_ok=True)
N = common.normalize_text
P = "api-gateway-"

facts = {}
for line in open(ROOT + "/aws-saa-book/data/facts/api-gateway.jsonl", encoding="utf-8"):
    if line.strip():
        f = json.loads(line)
        facts[f["id"]] = f

# id (without prefix) -> {old display: new display or None (remove)}; key "+" adds displays
D = {
 "access-control-client-ssl-certificate-backend": {"verify that HTTP requests to your backend system are from API Gateway": "verify that HTTP requests to your backend system"},
 "access-control-cors-not-authentication": {"how your REST API responds to cross-domain resource requests": "responds to cross-domain resource requests"},
 "access-control-iam-listed-auth": {"who can create and manage your APIs, as well as who can invoke them": "who can create and manage your APIs"},
 "access-control-lambda-authorizers-listed-auth": {"headers, paths, query strings, stage variables, or context variables": "headers, paths, query strings, stage variables"},
 "access-control-resource-policies-listed-auth": {"allow or deny access to your APIs and methods": "allow or deny access to your APIs"},
 "access-control-usage-plans-track-limit": {"track and limit usage of your API stages and methods for each API key": "track and limit usage of your API stages"},
 "access-control-waf-not-authentication": {"protect your API Gateway API from common web exploits": "from common web exploits"},
 "api-key-one-usage-plan-per-stage": {"only be associated with one usage plan for each stage": "one usage plan for each stage"},
 "api-key-request-must-contain-key-else-403": {"every incoming request to the API must contain an API key": "must contain an API key"},
 "api-keys-not-for-authentication": {"use an IAM role, a Lambda authorizer, or an Amazon Cognito user pool": "use an IAM role, a Lambda authorizer"},
 "api-keys-shared-usage-plan-access-all-apis": {"valid API key for one API in that usage plan can access all APIs": "can access all APIs in that usage plan"},
 "api-keys-with-authorizers-iam-cognito": {"together with Lambda authorizers, IAM roles, or Amazon Cognito": "Lambda authorizers, IAM roles, or Amazon Cognito"},
 "auth-flow-cross-account-silent-denied": {"requires that both the resource policy and the IAM policy": "both the resource policy and the IAM policy"},
 "auth-flow-iam-cross-account-both-allow": {"both the IAM policies and the resource policy explicitly allow the caller": "both the IAM policies and the resource policy"},
 "auth-flow-iam-same-account-either-allow": {"either the IAM user policies or the resource policy": "IAM user policies or the resource policy"},
 "auth-flow-resource-policy-only": {"An implicit denial or any explicit denial results in denying the caller": "An implicit denial or any explicit denial"},
 "caching-charged-hourly-no-free-tier": {"charged by the hour based on the cache size that you select": "charged by the hour"},
 "caching-dedicated-instance-capacity-tradeoff": {"larger capacity gives a better performance, but also costs more": "a better performance, but also costs more"},
 "caching-invalidate-entry-cache-control-max-age-0": {"provided that the client is authorized to do so": "provided that the client is authorized"},
 "caching-reduces-calls-and-latency": {"reduce the number of calls made to your endpoint": "reduce the number of calls"},
 "canary-random-traffic-split-small-percentage": {"separated at random into a production release and a canary release": "traffic is separated at random"},
 "canary-separate-logs-and-metrics": {"its own logs and metrics generated for all canary requests": "has its own logs and metrics"},
 "case-study-doordash-lambda-api-gateway-event-driven": {"event-driven architecture using AWS Lambda and Amazon API Gateway": "using AWS Lambda and Amazon API Gateway"},
 "custom-domain-certificate-in-acm-or-import": {"import a certificate to API Gateway in that Region": "import a certificate to API Gateway"},
 "custom-domain-friendlier-url-base-path": {"set up your API's hostname, and choose a base path": "choose a base path"},
 "custom-domain-migrate-edge-regional-not-private": {"migrate your custom domain name between edge-optimized and Regional endpoints": "between edge-optimized and Regional endpoints",
                                                     "can't migrate a public custom domain to a private custom domain name": "can't migrate a public custom domain"},
 "custom-domain-not-shared-rest-and-websocket": {"does not support sharing a custom domain name across REST and WebSocket APIs": "does not support sharing a custom domain name"},
 "custom-domain-regional-for-rest-and-http": {"Regional custom domain name can be associated with REST APIs and HTTP APIs": "associated with REST APIs and HTTP APIs"},
 "custom-domain-unique-per-region-across-accounts": {"must be unique within a Region across all AWS accounts": "unique within a Region across all AWS accounts"},
 "custom-domain-wildcard-acm-validated": {"validated using either the DNS or the email validation method": "the DNS or the email validation method"},
 "decision-guide-function-urls-single-function-no-api-management": {"Dedicated HTTPS endpoints for individual Lambda functions without API Gateway": "Dedicated HTTPS endpoints for individual Lambda functions"},
 "decision-guide-proxy-vs-non-proxy-integration": {"Proxy integrations directly pass all request information to a Lambda function": "directly pass all request information"},
 "deployment-needs-stage": {"must be associated with one or more API stages": "associated with one or more API stages"},
 "edge-optimized-custom-domain-all-regions": {"custom domain name that you use for an edge-optimized API": "custom domain name that you use"},
 "edge-optimized-uses-cloudfront-global-clients": {"routed to the nearest CloudFront Point of Presence (POP)": "nearest CloudFront Point of Presence (POP)"},
 "encryption-tls-min-version-custom-domain-http-ws-tls12": {"choose a minimum Transport Layer Security (TLS) protocol version": "minimum Transport Layer Security (TLS) protocol version"},
 "faq-api-keys-not-for-authorization": {"do not recommend you use API keys for authorization": "do not recommend you use API keys"},
 "faq-billing-websocket-messages-and-minutes": {"number of minutes a client is connected to the API": "minutes a client is connected"},
 "faq-caching-off-by-default": {"does not set any cache on your API methods": "does not set any cache"},
 "faq-cloudtrail-logs-management-calls": {"full auditable history of the changes to your REST APIs": "full auditable history",
                                          "create, modify, delete, or deploy REST APIs are logged to CloudTrail": "create, modify, delete, or deploy REST APIs"},
 "faq-no-cache-no-throttle-all-pass-through": {"all requests will pass through to your backend service": "all requests will pass through"},
 "faq-private-api-vpc-resource-policy": {"restrict access to a specific Amazon VPC or VPC endpoint": "a specific Amazon VPC or VPC endpoint",
                                         "from a different account access to the Private API": "VPC endpoint from a different account"},
 "faq-private-apis-vpc-endpoints-only": {"can only be accessible by resources within your Amazon VPC": "accessible by resources within your Amazon VPC"},
 "faq-resource-policy-definition": {"JSON policy document that you attach to an API": "JSON policy document"},
 "faq-stage-custom-domain-direct": {"custom domain names to point directly to a stage": "point directly to a stage"},
 "faq-stage-defines-path": {"define the path through which the deployment is accessible": "the path through which the deployment is accessible"},
 "faq-throttle-per-method-or-route": {"a standard rate limit and a burst rate limit per second": "standard rate limit and a burst rate limit"},
 "faq-throttle-sheds-requests-to-limit": {"send only the defined limit to your back-end service": "send only the defined limit"},
 "faq-vpc-links-private-integration": {"proxy requests to backend HTTP/HTTPS resources running in your Amazon VPC": "backend HTTP/HTTPS resources running in your Amazon VPC"},
 "faq-websocket-backend-integrations": {"AWS Lambda functions, Amazon Kinesis, or any HTTP endpoint": "Amazon Kinesis, or any HTTP endpoint"},
 "faq-websocket-callback-url": {"send messages to the client from the backend service": "send messages to the client"},
 "faq-websocket-routing-key": {"The routing key is an attribute in the message body": "an attribute in the message body"},
 "http-api-first-class-aws-service-integrations": {"send a message to an Amazon Simple Queue Service queue, or to start an AWS Step Functions state machine": "start an AWS Step Functions state machine"},
 "http-api-first-class-integration-needs-iam-role": {"create an IAM role that grants API Gateway permissions": "an IAM role that grants API Gateway permissions"},
 "http-api-oidc-oauth-cors-auto-deploy": {"built-in support for cross-origin resource sharing (CORS) and automatic deployments": "built-in support for cross-origin resource sharing (CORS)"},
 "iam-caller-permission-invoke-or-refresh-cache": {"call a deployed API or to refresh the API caching": "refresh the API caching"},
 "iam-service-role-for-backend-access": {"IAM role of the AWS service for API Gateway type": "AWS service for API Gateway"},
 "integration-aws-proxy-lambda-no-mapping": {"you do not set the integration request or the integration response": "do not set the integration request",
                                             "passes the incoming request from the client as the input": "passes the incoming request from the client"},
 "integration-http-custom-needs-mappings": {"lets an API expose HTTP endpoints in the backend": "expose HTTP endpoints in the backend",
                                            "must configure both the integration request and integration response": "configure both the integration request and integration response"},
 "integration-http-proxy-passes-through": {"passes the outgoing response from the HTTP endpoint to the client": "passes the outgoing response from the HTTP endpoint"},
 "integration-mock-no-backend-no-charges": {"return a response without sending the request further to the backend": "without sending the request further to the backend"},
 "integration-type-values-aws-proxy-http-mock": {"For the Lambda proxy integration, the value is `AWS_PROXY`": "the value is `AWS_PROXY`"},
 "jwt-authorizer-claims-issuer-audience-expiry": {"exp – Must be after the current time in UTC": "Must be after the current time in UTC"},
 "jwt-authorizer-claims-passed-to-backend": {"passes the claims in the token to the API route’s integration": "passes the claims in the token",
                                             "Lambda functions can access the JWT claims": "can access the JWT claims"},
 "lambda-authorizer-caching-policy-must-apply-all-methods": {"must return a policy that is applicable to all methods across an API": "applicable to all methods across an API"},
 "lambda-authorizer-custom-scheme-oauth-saml": {"bearer token authentication strategy such as OAuth or SAML": "bearer token authentication strategy"},
 "lambda-proxy-function-must-return-format": {"the Lambda function must return the result in this format": "must return the result in this format",
                                              "pass the Lambda output as the API response to the client": "pass the Lambda output as the API response"},
 "lambda-proxy-passes-event-object": {"request headers, query string parameters, URL path variables, payload, and API configuration data": "request headers, query string parameters, URL path variables"},
 "logging-execution-and-access-independent": {"enable execution logging and access logging independently of each other": "execution logging and access logging independently"},
 "manages-traffic-auth-monitoring": {"traffic management, authorization and access control, monitoring, and API version management": "traffic management, authorization and access control"},
 "mapping-template-vtl": {"transforms a request body from the frontend data format to the backend data format": "transforms a request body"},
 "metrics-4xx-error-client-side": {"number of client-side errors captured in a given period": "number of client-side errors"},
 "metrics-5xx-error-server-side": {"number of server-side errors captured in a given period": "number of server-side errors"},
 "metrics-cache-hit-count": {"requests served from the API cache in a given period": "requests served from the API cache"},
 "metrics-cache-miss-count": {"requests served from the backend in a given period": "requests served from the backend"},
 "metrics-latency-includes-integration-latency": {"includes the integration latency and other API Gateway overhead": "integration latency and other API Gateway overhead"},
 "monitoring-access-and-execution-logging-alarms": {"CloudTrail logging and monitoring of API usage and API changes": "CloudTrail logging and monitoring of API usage"},
 "pricing-http-rest-dimensions": {"the API calls you receive and the amount of data transferred out": "pay only for the API calls you receive"},
 "pricing-websocket-dimensions": {"messages sent and received and the total number of connection minutes": "the total number of connection minutes",
                                  "+": ["messages sent and received"]},
 "private-api-cannot-convert-to-edge-optimized": {"cannot convert a private API to an edge-optimized API": "cannot convert a private API"},
 "private-api-isolated-from-internet": {"VPC endpoints for API Gateway that have been granted access": "have been granted access"},
 "private-api-needs-resource-policy": {"don't need to create a custom VPC endpoint policy": "custom VPC endpoint policy"},
 "private-api-private-dns-blocks-public-default-endpoint": {"you can’t access the default endpoint for public APIs": "can’t access the default endpoint for public APIs",
                                                            "create a private hosted zone for each private API": "a private hosted zone for each private API"},
 "private-api-whitepaper-cross-account-vpcs": {"from selected VPCs and VPC endpoints, including across AWS accounts": "including across AWS accounts",
                                               "Each endpoint can be used to access multiple private APIs": "access multiple private APIs"},
 "private-endpoint-vpc-only-interface-endpoint": {"can only be accessed from your Amazon Virtual Private Cloud (VPC)": "accessed from your Amazon Virtual Private Cloud (VPC)"},
 "private-integration-expose-vpc-resources-outside": {"expose your HTTP/HTTPS resources within an Amazon VPC for access by clients outside of the VPC": "clients outside of the VPC"},
 "private-integration-http-api-targets-alb-nlb-cloud-map": {"Application Load Balancer, Network Load Balancer, or resources registered with an AWS Cloud Map service": "Application Load Balancer, Network Load Balancer",
                                                            "+": ["registered with an AWS Cloud Map service"]},
 "private-integration-needs-vpc-link-v2-alb": {"connect your REST API to Application Load Balancers without using an Network Load Balancer": "connect your REST API to Application Load Balancers"},
 "private-integration-vpc-links-v1-nlb-multi-az": {"routes traffic to resources in more than one Availability Zone": "more than one Availability Zone"},
 "regional-custom-domain-region-specific": {"specific to the Region where the API is deployed": "the Region where the API is deployed"},
 "regional-endpoint-bypasses-cloudfront": {"bypasses the unnecessary round trip to a CloudFront distribution": "bypasses the unnecessary round trip"},
 "resilience-alarm-health-check-in-secondary-region": {"secondary Region should contain the alarm and health check": "should contain the alarm and health check",
                                                       "you don't depend on the primary Region to perform failover": "don't depend on the primary Region"},
 "resilience-evaluate-target-health-only-service-unavailable": {"fail only when the API Gateway service is unavailable in the Region": "only when the API Gateway service is unavailable"},
 "resilience-failover-prerequisites": {"An ACM certificate for that domain name in two AWS Regions": "for that domain name in two AWS Regions"},
 "resilience-failover-resources-ready-before": {"won't be ready for traffic in the secondary Region": "ready for traffic in the secondary Region"},
 "resilience-failover-same-custom-domain-name-two-regions": {"custom domain names with the same name in two AWS Regions": "with the same name in two AWS Regions"},
 "resilience-regional-multi-az-auto-recover": {"automatically recover from the failure of an Availability Zone": "recover from the failure of an Availability Zone"},
 "rest-api-definition": {"backend HTTP endpoints, Lambda functions, or other AWS services": "Lambda functions, or other AWS services"},
 "rest-resource-method-definition": {"logical entity that an app can access through a resource path": "access through a resource path"},
 "security-best-practice-cloudtrail-records-actions": {"record of actions taken by a user, role, or an AWS service": "record of actions taken by a user"},
 "stage-lifecycle-reference": {"logical reference to a lifecycle state of your API": "logical reference to a lifecycle state"},
 "stage-named-reference-to-deployment": {"enable caching, customize request throttling, configure logging, define stage variables": "enable caching, customize request throttling, configure logging"},
 "stage-variables-different-backend-or-lambda-per-stage": {"can't use a stage variable to set a different integration endpoint": "can't use a stage variable"},
 "stage-variables-lambda-permissions-manual": {"must configure the permissions on the Lambda function manually": "permissions on the Lambda function manually"},
 "throttling-account-level-default-rps-burst": {"across all APIs within an AWS account, per Region": "across all APIs within an AWS account",
                                                "+": ["the maximum bucket size"]},
 "throttling-aws-limits-not-changeable": {"applied across all accounts and clients in a Region": "across all accounts and clients in a Region"},
 "throttling-stage-method-limits-cap": {"applied at the API method level for a stage": "at the API method level for a stage"},
 "throttling-stage-or-usage-plan-options": {"usage plans to set throttles on client request submissions": "set throttles on client request submissions"},
 "throttling-account-limit-increase-on-request": {"+": ["shorter timeouts and smaller payloads"]},
 "usage-plan-definition": {"who can access one or more deployed API stages and methods": "access one or more deployed API stages"},
 "usage-plan-not-hard-limits-use-budgets-waf": {"AWS Budgets to monitor costs and AWS WAF to manage API requests": "AWS Budgets to monitor costs",
                                                "+": ["AWS WAF to manage API requests"]},
 "vpc-endpoint-policy-definition": {"IAM resource policy that you attach to a VPC endpoint": "IAM resource policy that you attach"},
 "wa-rel05-bp02-anti-pattern-usage-plans-a2a-per-ip": {"Rate limiting on a per IP address basis has not been implemented": "per IP address basis has not been implemented"},
 "wa-rel05-bp02-api-gateway-token-bucket-usage-plans-waf": {"implements the token bucket algorithm according to account and region limits": "implements the token bucket algorithm"},
 "wa-rel05-bp02-throttle-levels-account-stage-key": {"account level per region, API per stage, and API key per usage plan levels": "account level per region, API per stage"},
 "wa-rel05-bp02-throttle-protect-resources": {"mitigate resource exhaustion due to unexpected increases in demand": "mitigate resource exhaustion",
                                              "rejected with a return message indicating the request was throttled": "indicating the request was throttled"},
 "waf-evaluated-before-other-access-controls": {"AWS WAF rules are evaluated before other access control features": "evaluated before other access control features"},
 "waf-protects-rest-api-sql-injection-xss": {"common web exploits, such as SQL injection and cross-site scripting (XSS) attacks": "SQL injection and cross-site scripting (XSS) attacks"},
 "waf-web-acl-associated-with-stage": {"Associate the AWS WAF web ACL with an API stage": "web ACL with an API stage"},
 "waf-web-acl-same-region-as-api": {"must be located in the same Region as your API": "located in the same Region as your API"},
 "websocket-connect-route-called-on-initiation": {"persistent connection between the client and a WebSocket API is being initiated": "a WebSocket API is being initiated"},
 "websocket-connection-persistent-client-side-only": {"no persistent connection between API Gateway and backend integrations": "no persistent connection between API Gateway and backend"},
 "websocket-connections-api-callback-status-disconnect": {"send a callback message to a connected client, get connection information, or disconnect the client": "get connection information, or disconnect the client"},
 "websocket-disconnect-route-called-on-disconnect": {"when the client or the server disconnects from the API": "the client or the server disconnects"},
 "websocket-json-routes-default-for-non-json": {"incoming JSON messages are directed to backend integrations based on routes": "incoming JSON messages are directed to backend integrations"},
 "websocket-lambda-authorizer-connect-route-only": {"only use a Lambda authorizer function for the `$connect` route": "only use a Lambda authorizer function",
                                                    "WebSocket APIs": "for the `$connect` route"},
 "websocket-route-key-selection-expression": {"JSON property that is expected to be present in the message payload": "JSON property that is expected to be present"},
 "websocket-send-data-via-route-response-or-connections-api": {"use the `@connections` API to send a POST request": "`@connections` API to send a POST request"},
 "websocket-stateful-frontend-for-backends": {"based on the content of the messages it receives from client apps": "based on the content of the messages"},
 "websocket-two-way-server-push": {"both send messages to each other at any time": "send messages to each other at any time"},
 "websocket-two-way-vs-rest-request-response": {"supports two-way communication between client apps and your backend": "supports two-way communication"},
 "whitepaper-api-gateway-lambda-scale-automatically": {"scale automatically to support exactly the needs of your application": "both API Gateway and Lambda scale automatically"},
 "whitepaper-api-keys-usage-plans-throttling-per-method": {"generation of API keys and association of these keys with a configurable usage plan": "generation of API keys",
                                                           "throttling, rate limits, and burst rate limits for each method": "burst rate limits for each method"},
 "whitepaper-cache-reduces-lambda-invocations": {"reduces the number of times your Lambda functions are invoked": "number of times your Lambda functions are invoked"},
 "whitepaper-cors-for-static-pages": {"CORS compliance allows web browsers to directly invoke your APIs": "web browsers to directly invoke your APIs"},
 "whitepaper-lambda-proxy-vs-non-proxy-integration": {"entire client HTTPS request is sent as-is to the Lambda function": "entire client HTTPS request is sent as-is",
                                                      "you configure how the parameters, headers, and body of the client request are passed": "you configure how the parameters, headers, and body"},
 "whitepaper-logic-tier-no-server-management": {"serverless application that is highly available, scalable, and secure": "highly available, scalable, and secure"},
 "whitepaper-pay-after-requests-begin": {"only incur infrastructure costs after your APIs begin receiving requests": "only incur infrastructure costs after your APIs"},
 "xray-passes-trace-through-from-traced-service": {"even if X-Ray tracing isn't enabled on the API": "X-Ray tracing isn't enabled on the API"},
 # second displays for hard facts with one display (brief gate B12)
 "http-throttle-429": {"+": ["begins to throttle requests"]},
 "http-throttle-token-bucket": {"+": ["a token counts for a request"]},
 "private-domain-not-unique": {"+": ["Custom domain names for private APIs"]},
 "private-domain-ram-sharing": {"+": ["to other AWS accounts"]},
 "private-domain-tls12-only": {"+": ["can’t set a minimum TLS version"]},
 "private-integration-default-http": {"+": ["contains a secure server name"]},
 "private-integration-same-account": {"+": ["load balancer, VPC link and REST API"]},
 "stream-proxy-only": {"+": ["Lambda proxy integrations and private integrations"]},
 "stream-rest-only": {"+": ["Request streaming isn't supported"]},
 "vpclink-v1-needs-nlb": {"+": ["must first create a Network Load Balancer"]},
 "vpclink-v2-immutable": {"+": ["can’t change its subnets or security groups"]},
 "vpclink-v2-inactive-60-days": {"+": ["depend on the VPC link to fail"]},
 "caching-only-get-methods-by-default": {},
}

# comparison-table facts: the display becomes the feature cell of the row (verbatim)
TABLE = {
 "table-access-logs-firehose-rest-yes-http-no": "Access logs to Amazon Data Firehose",
 "table-api-keys-rest-yes-http-no": "API keys",
 "table-automatic-deployments-http-yes-rest-no": "Automatic deployments",
 "table-backend-certificates-rest-yes-http-no": "Certificates for backend authentication",
 "table-caching-rest-yes-http-no": "Caching",
 "table-canary-release-rest-yes-http-no": "Canary release deployments",
 "table-cloudwatch-metrics-rest-and-http": "Amazon CloudWatch metrics",
 "table-custom-gateway-responses-rest-yes-http-no": "Custom gateway responses",
 "table-developer-portal-rest-yes-http-no": "Developer portal",
 "table-edge-optimized-rest-yes-http-no": "Edge-optimized",
 "table-execution-logs-rest-yes-http-no": "Execution logs",
 "table-iam-auth-rest-and-http": "IAM",
 "table-lambda-authorizer-rest-and-http": "Custom authorization with an AWS Lambda function",
 "table-mock-integrations-rest-yes-http-no": "Mock integrations",
 "table-mutual-tls-rest-and-http": "Mutual TLS authentication",
 "table-per-client-rate-limiting-rest-yes-http-no": "Per-client rate limiting",
 "table-per-client-usage-throttling-rest-yes-http-no": "Per-client usage throttling",
 "table-private-endpoint-rest-yes-http-no": "Private",
 "table-private-integration-alb-rest-and-http": "Private integrations with Application Load Balancers",
 "table-private-integration-cloud-map-http-yes-rest-no": "Private integrations with AWS Cloud Map",
 "table-private-integration-nlb-rest-and-http": "Private integrations with Network Load Balancers",
 "table-regional-endpoint-rest-and-http": "Regional",
 "table-request-body-transformation-rest-yes-http-no": "Request body transformation",
 "table-request-validation-rest-yes-http-no": "Request validation",
 "table-resource-policies-rest-yes-http-no": "Resource policies",
 "table-response-streaming-rest-yes-http-no": "Response streaming",
 "table-waf-rest-yes-http-no": "AWS WAF",
 "table-xray-tracing-rest-yes-http-no": "AWS X-Ray tracing",
}

# other field changes on facts that are kept
EXTRA = {
 "caching-only-get-methods-by-default": {"qualifiers": {"scope": "REST APIs, per stage", "default_or_max": "default", "adjustable": True,
                                                         "condition": "Other methods are cached by overriding method settings."}},
 "private-integration-vpc-links-v1-legacy": {"volatility": "frequently-changing",
                                             "note": "Merged with api-gateway-vpclink-v1-legacy (same sentence). VPC links V2 for REST APIs arrived on 2025-11-21 (api-gateway-change-alb-private-integration-2025); older questions assume a Network Load Balancer is required."},
 "private-integration-needs-vpc-link-v2-alb": {"volatility": "frequently-changing",
                                               "note": "Merged with api-gateway-vpclink-v2-rest-alb (same sentence). Changed 2025-11-21: see api-gateway-change-alb-private-integration-2025."},
 "throttling-429-too-many-requests-retry": {"hard": True},
}
LIGHT = {
 "change-alb-private-integration-2025": {"note": "Current truth: api-gateway-private-integration-needs-vpc-link-v2-alb and api-gateway-private-integration-vpc-links-v1-legacy. Older questions say a REST private integration needs a Network Load Balancer."},
}

SUPERSEDE = [
 ("cache-capacity-change-flushes", "caching-capacity-change-deletes-cached-data", "same sentence of api-gateway-caching; kept the fact with two displays"),
 ("cache-not-free-tier", "caching-charged-hourly-no-free-tier", "same quote of api-gateway-caching; kept the fact with both clauses as displays"),
 ("cache-get-only-by-default", "caching-only-get-methods-by-default", "same rule from api-gateway-caching; the kept quote holds both sentences; its qualifiers were completed"),
 ("rest-private-integration-no-cloudmap", "private-integration-cloud-map-not-supported-rest", "same sentence of private-integration"),
 ("vpclink-http-targets", "private-integration-http-api-targets-alb-nlb-cloud-map", "same sentence of http-api-develop-integrations-private"),
 ("vpclink-v1-legacy", "private-integration-vpc-links-v1-legacy", "same sentences of private-integration"),
 ("vpclink-v2-rest-alb", "private-integration-needs-vpc-link-v2-alb", "the kept quote holds this sentence plus the VPC link prerequisite"),
 ("throttle-429", "throttling-429-too-many-requests-retry", "the kept quote holds this sentence plus the retry sentence"),
 ("throttle-token-bucket", "throttling-token-bucket-per-account-region", "the kept quote holds this sentence plus the per-account, per-Region scope"),
 ("throttle-account-rate-adjustable", "throttling-account-limit-increase-on-request", "the kept quote holds this sentence plus the cap; its display was added to the kept fact"),
 ("throttle-burst-definition", "throttling-account-level-default-rps-burst", "the kept quote holds both sentences plus the RPS limit; its display was added to the kept fact"),
 ("usage-plan-throttle-rate-burst", "throttling-usage-plan-rate-and-burst", "the kept quote holds both sentences plus the per-method target"),
]

problems, written = [], []


def check(fid, disp, quotes):
    if re.search(r"\d", disp):
        return
    if len(disp.split()) > 8:
        problems.append("%s: display over 8 words: %s" % (fid, disp))
    if not any(lint.holds_display(q, N(disp)) for q in quotes if q):
        problems.append("%s: display not in a quote: %s" % (fid, disp))


ids = set(D) | set(TABLE) | set(EXTRA) | set(LIGHT)
for short in sorted(ids):
    fid = P + short
    f = facts.get(fid)
    if f is None or f["status"] in ("rejected", "superseded"):
        problems.append("%s: missing or not live" % fid)
        continue
    quotes = [N(e["quote"]) for e in f["evidence"]] + [N(e.get("table_header") or "") for e in f["evidence"]]
    patch = {}
    vals = copy.deepcopy(f["values"])
    if short in D:
        m = D[short]
        olds = {v["display"] for v in vals}
        for o in m:
            if o != "+" and o not in olds:
                problems.append("%s: old display not found: %s" % (fid, o))
        new = []
        for v in vals:
            if v["display"] in m:
                nd = m[v["display"]]
                if nd is None:
                    continue
                v = dict(v, display=nd)
            new.append(v)
        keys = {v["key"] for v in new}
        for i, add in enumerate(m.get("+", [])):
            k = "r%d" % (i + 1)
            while k in keys:
                k += "x"
            new.append({"key": k, "display": add})
        if new != f["values"]:
            patch["values"] = new
    if short in TABLE:
        cell = TABLE[short]
        new = []
        for v in vals:
            d = v["display"]
            if re.search(r"\d", d) or (N(d) and any(lint.holds_display(q, N(d)) for q in quotes if q) and len(d.split()) <= 8 and d != cell):
                new.append(v)
        new = [dict(vals[0], display=cell)] + [v for v in new if v["display"] != cell and v["key"] != vals[0]["key"]]
        patch["values"] = new
    if short in EXTRA:
        patch.update(copy.deepcopy(EXTRA[short]))
    if short in LIGHT:
        patch.update(copy.deepcopy(LIGHT[short]))
    for v in patch.get("values", f["values"]):
        check(fid, v["display"], quotes)
    ds = [v["display"] for v in patch.get("values", f["values"])]
    if len(set(ds)) != len(ds):
        problems.append("%s: duplicate displays" % fid)
    if not patch:
        continue
    with open(os.path.join(OUT, fid + ".json"), "w", encoding="utf-8") as o:
        json.dump(patch, o, ensure_ascii=False, indent=1)
    light = all(k in ("exam_relevance", "tier0", "question", "note") for k in patch)
    written.append(fid)
    print("light" if light else "rev", fid, json.dumps(patch.get("values", ""), ensure_ascii=False)[:160])

sup = []
for old, new, why in SUPERSEDE:
    o, n = P + old, P + new
    if o not in facts or n not in facts:
        problems.append("supersede: unknown %s or %s" % (o, n))
    sup.append([o, n, why])
json.dump({"patch_ids": written, "supersede": sup}, open(W + "reg-decisions.json", "w"), indent=1)
for p in problems:
    print("PROBLEM", p)
print("written", len(written), "supersede", len(sup))
