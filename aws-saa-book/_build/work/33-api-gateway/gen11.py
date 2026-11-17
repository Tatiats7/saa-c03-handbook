import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
DGD = "docs/decision-guides/latest/decision-guides/choosing-aws-serverless-service"
WA = "docs/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_throttle_requests"
ALB = "docs/elasticloadbalancing/latest/application/lambda-functions"
B = ["2.1.K12"]
fs = []
fs.append(F("decision-guide-http-api-lightweight-lower-cost", "behavior",
 "AWS describes the API Gateway HTTP API as lightweight, lower-cost API routing optimized for Lambda and HTTP backends with automatic deployments.",
 "When does the AWS decision guide point to an API Gateway HTTP API?",
 ["Lightweight, lower-cost API routing", "optimized for Lambda and HTTP backends"],
 [ev(DGD, "Amazon API Gateway HTTP API: Lightweight, lower-cost API routing optimized for Lambda and HTTP backends with automatic deployments.")],
 scope="HTTP APIs", bullets=B, tier0=True))
fs.append(F("decision-guide-rest-api-full-featured", "behavior",
 "AWS describes the API Gateway REST API as full-featured API management with request validation, response streaming, caching, AWS WAF integration, usage plans, API keys, and private endpoints.",
 "When does the AWS decision guide point to an API Gateway REST API?",
 ["Full-featured API management", "usage plans, API keys, and private endpoints"],
 [ev(DGD, "Amazon API Gateway REST API: Full-featured API management with request validation, response streaming, caching, AWS WAF integration, usage plans, API keys, and private endpoints.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("decision-guide-function-urls-single-function-no-api-management", "behavior",
 "Lambda function URLs are dedicated HTTPS endpoints for individual Lambda functions without API Gateway, suited for single-function microservices or webhooks where API management features are not needed.",
 "When are Lambda function URLs enough instead of API Gateway?",
 ["Dedicated HTTPS endpoints for individual Lambda functions without API Gateway", "where API management features aren't needed"],
 [ev(DGD, "Lambda function URLs: Dedicated HTTPS endpoints for individual Lambda functions without API Gateway. Suited for single-function microservices or webhooks where API management features aren't needed.")],
 scope="Lambda function URLs versus API Gateway", bullets=B, tier0=True))
fs.append(F("decision-guide-websocket-apis-push-without-polling", "behavior",
 "AWS describes API Gateway WebSocket APIs as persistent, bidirectional connections between clients and backend services, for chat applications, real-time dashboards, multiplayer games or financial trading platforms where the server needs to push data to clients without polling.",
 "When does the AWS decision guide point to WebSocket APIs?",
 ["Persistent, bidirectional connections between clients and backend services", "push data to clients without polling"],
 [ev(DGD, "Amazon API Gateway WebSocket APIs: Persistent, bidirectional connections between clients and backend services. Use for chat applications, real-time dashboards, multiplayer games, or financial trading platforms where the server needs to push data to clients without polling.")],
 scope="WebSocket APIs", bullets=B))
fs.append(F("decision-guide-proxy-vs-non-proxy-integration", "behavior",
 "API Gateway proxy integrations directly pass all request information to a Lambda function, which is simpler to configure, while non-proxy (custom) integrations can transform data before it reaches your function and before output returns to clients.",
 "When do you pick a proxy versus a non-proxy integration?",
 ["Proxy integrations directly pass all request information to a Lambda function", "Non-proxy (custom) integrations can transform data"],
 [ev(DGD, "API Gateway offers two integration approaches. Proxy integrations directly pass all request information to a Lambda function for processing, which is simpler to configure. Non-proxy (custom) integrations can transform data before it reaches your function and before output returns to clients, which is useful for legacy code migration or keeping function code focused on business logic.")],
 scope="REST APIs", bullets=B))
fs.append(F("decision-guide-rest-broadest-http-lowest-latency-cost", "behavior",
 "The decision guide says the REST API provides the broadest feature set including caching, request validation and WAF, the HTTP API provides the lowest latency and cost, and Lambda function URLs provide the simplest single-function HTTPS endpoint without requiring API Gateway.",
 "Which API Gateway API type has the broadest features and which has the lowest latency and cost?",
 ["REST API provides the broadest feature set", "HTTP API provides the lowest latency and cost"],
 [ev(DGD, "REST API provides the broadest feature set including caching, request validation, and WAF. HTTP API provides the lowest latency and cost. AWS AppSync provides real-time subscriptions and GraphQL. Lambda function URLs provide the simplest single-function HTTPS endpoint without requiring API Gateway.")],
 scope="API Gateway REST APIs and HTTP APIs", bullets=B+["4.4.S6"], tier0=True))
fs.append(F("decision-guide-api-gateway-per-request-pricing", "behavior",
 "The decision guide calls API Gateway pricing hybrid pricing: per-request pricing that scales linearly without upfront commitment, which gives cost predictability without capacity forecasting but can become expensive at very high throughput compared with provisioned alternatives.",
 "How does the AWS decision guide characterize API Gateway pricing and its drawback?",
 ["per-request pricing that scales linearly without upfront commitment", "can become expensive at very high throughput"],
 [ev(DGD, "Hybrid pricing (DynamoDB on-demand, API Gateway) offers per-request pricing that scales linearly without upfront commitment. This provides cost predictability without the need to forecast capacity, but can become expensive at very high throughput compared to provisioned alternatives.")],
 scope="API Gateway", bullets=["2.1.K12"], tier=1))
fs.append(F("wa-rel05-bp02-throttle-protect-resources", "behavior",
 "The Well-Architected practice REL05-BP02 says to throttle requests to mitigate resource exhaustion due to unexpected increases in demand: requests below throttling rates are processed and those over the limit are rejected with a message that they were throttled.",
 "Why does the Well-Architected Framework recommend throttling requests?",
 ["mitigate resource exhaustion due to unexpected increases in demand", "rejected with a return message indicating the request was throttled"],
 [ev(WA, "Throttle requests to mitigate resource exhaustion due to unexpected increases in demand. Requests below throttling rates are processed while those over the defined limit are rejected with a return message indicating the request was throttled.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"], tier0=True))
fs.append(F("wa-rel05-bp02-client-handles-error-retries-later", "behavior",
 "When request arrival rates exceed limits, the appropriate response signals that a request has been throttled, which allows the consumer to handle the error and retry later.",
 "What should a throttled client do according to the Well-Architected guidance?",
 ["signals that a request has been throttled", "handle the error and retry later"],
 [ev(WA, "If request arrival rates exceed limits, the appropriate response signals that a request has been throttled. This allows the consumer to handle the error and retry later.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"]))
fs.append(F("wa-rel05-bp02-api-gateway-token-bucket-usage-plans-waf", "behavior",
 "Amazon API Gateway implements the token bucket algorithm according to account and Region limits and can be configured per client with usage plans; SQS and Kinesis can buffer requests, and AWS WAF can rate-limit specific API consumers that generate unusually high load.",
 "Which AWS services does the Well-Architected throttling practice name for API throttling, buffering and per-consumer limits?",
 ["implements the token bucket algorithm according to account and region limits", "configured per-client with usage plans"],
 [ev(WA, "Amazon API Gateway implements the token bucket algorithm according to account and region limits and can be configured per-client with usage plans. Additionally, Amazon Simple Queue Service (Amazon SQS) and Amazon Kinesis can buffer requests to smooth out the request rate, and allow higher throttling rates for requests that can be addressed. Finally, you can implement rate limiting with AWS WAF to throttle specific API consumers that generate unusually high load.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"], tier0=True))
fs.append(F("wa-rel05-bp02-429-and-waf-per-ip-and-queue-bursting", "behavior",
 "You can configure API Gateway with throttling limits that return 429 Too Many Requests errors when limits are exceeded, use AWS WAF with API Gateway endpoints for rate limiting on a per IP address basis, and put messages into a queue or stream where asynchronous processing is tolerable to burst to higher throttle rates.",
 "How does the Well-Architected guidance combine API Gateway throttling, WAF and queues?",
 ["return `429 Too Many Requests` errors when limits are exceeded", "rate limiting on a per IP address basis"],
 [ev(WA, "You can configure API Gateway with throttling limits for your APIs and return `429 Too Many Requests` errors when limits are exceeded. You can use AWS WAF with your AWS AppSync and API Gateway endpoints to enable rate limiting on a per IP address basis. Additionally, where your system can tolerate asynchronous processing, you can put messages into a queue or stream to speed up responses to service clients, which allows you to burst to higher throttle rates.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"]))
fs.append(F("wa-rel05-bp02-use-sqs-kinesis-integrations-to-buffer", "capability",
 "AWS recommends using API Gateway with native service integrations to Amazon SQS or Kinesis to buffer requests.",
 "How can API Gateway buffer requests to protect a backend?",
 ["native service integrations to Amazon SQS or Kinesis", "buffer requests"],
 [ev(WA, "Use API Gateway with native service integrations to Amazon SQS or Kinesis to buffer requests.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6", "2.1.K12"]))
fs.append(F("wa-rel05-bp02-throttle-levels-account-stage-key", "behavior",
 "The Well-Architected practice says to understand and configure API Gateway throttling limits at the account level per Region, API per stage, and API key per usage plan levels.",
 "At which levels should API Gateway throttling limits be configured?",
 ["account level per region, API per stage, and API key per usage plan levels", "Understand and configure API Gateway throttling limits"],
 [ev(WA, "Understand and configure API Gateway throttling limits at the account level per region, API per stage, and API key per usage plan levels.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"], tier0=True))
fs.append(F("wa-rel05-bp02-anti-pattern-default-throttles", "behavior",
 "A listed anti-pattern of the throttling best practice is that API endpoint throttles are not implemented or are left at default values without considering expected volumes.",
 "Which throttling anti-pattern concerns default values?",
 ["left at default values without considering expected volumes", "throttles are not implemented"],
 [ev(WA, "API endpoint throttles are not implemented or are left at default values without considering expected volumes.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"], exam="extended"))
fs.append(F("wa-rel05-bp02-anti-pattern-usage-plans-a2a-per-ip", "behavior",
 "Listed anti-patterns of the throttling best practice include not configuring or considering usage plans for application-to-application API consumers, and not implementing rate limiting on a per IP address basis.",
 "Which throttling anti-patterns concern usage plans and per-IP rate limiting?",
 ["Usage plans have not been configured or considered", "Rate limiting on a per IP address basis has not been implemented"],
 [ev(WA, "Usage plans have not been configured or considered for application to application (A2A) API consumers."),
  ev(WA, "Rate limiting on a per IP address basis has not been implemented.")],
 scope="Reliability pillar, REL05-BP02", bullets=["4.4.S6"], exam="extended"))
fs.append(F("elb-lambda-target-request-body-max", "limit",
 "For a Lambda function that is a target of an Application Load Balancer, the maximum size of the request body that can be sent to the function is 1 MB.",
 "What is the maximum request body size for an ALB Lambda target?",
 ["request body that you can send to a Lambda function is 1 MB", "1 MB"],
 [ev(ALB, "The maximum size of the request body that you can send to a Lambda function is 1 MB. For related size limits, see HTTP header limits.")],
 scope="Application Load Balancer, Lambda target", dm="max", bullets=["2.1.K12"], svc="elb", home="14"))
fs.append(F("elb-lambda-target-response-json-max", "limit",
 "For a Lambda function that is a target of an Application Load Balancer, the maximum size of the response JSON that the function can send is 1 MB.",
 "What is the maximum response size for an ALB Lambda target?",
 ["response JSON that the Lambda function can send is 1 MB", "1 MB"],
 [ev(ALB, "The maximum size of the response JSON that the Lambda function can send is 1 MB.")],
 scope="Application Load Balancer, Lambda target", dm="max", bullets=["2.1.K12"], svc="elb", home="14"))
fs.append(F("elb-lambda-target-same-account-region", "restriction",
 "A Lambda function used as a target of an Application Load Balancer and its target group must be in the same account and in the same Region.",
 "Can an ALB use a Lambda function from another account or Region?",
 ["must be in the same account and in the same Region", "Lambda function and target group"],
 [ev(ALB, "The Lambda function and target group must be in the same account and in the same Region.")],
 scope="Application Load Balancer, Lambda target", bullets=["2.1.K12"], svc="elb", home="14"))
fs.append(F("case-study-travelex-api-gateway-near-real-time-apis", "case-study",
 "Travelex developed 10–15 near real-time APIs using Integration on AWS and connected them through Amazon API Gateway.",
 None,
 ["10–15 near real-time APIs", "connected these using Amazon API Gateway"],
 [ev("www/solutions/case-studies/travelex-integration-on-aws", "Travelex developed 10–15 near real-time APIs using Integration on AWS and connected these using Amazon API Gateway.")],
 scope="Travelex", bullets=["2.1.K12"], exam="reference", hard=False))
fs.append(F("case-study-doordash-lambda-api-gateway-event-driven", "case-study",
 "DoorDash scaled the implementation of an event-driven architecture using AWS Lambda and Amazon API Gateway.",
 None,
 ["event-driven architecture using AWS Lambda and Amazon API Gateway", "rapidly scaled the implementation"],
 [ev("www/solutions/case-studies/doordash-serverless-case-study", "Learn how DoorDash rapidly scaled the implementation of an event-driven architecture using AWS Lambda and Amazon API Gateway.")],
 scope="DoorDash", bullets=["2.1.K12"], exam="reference", hard=False))
write("facts-behavior-11.json", fs)
