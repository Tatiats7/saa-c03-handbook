import json
ids = json.load(open("mine-bd-ids.json"))
def pick(*subs):
    out = [i for i in ids if any(s in i for s in subs)]
    return out
P = "api-gateway-"
d = {}
def item(did, status, facts, note=""):
    d[did] = {"status": status, "facts": facts, "note": note}
item("d017", "filled", pick("service-definition", "front-door", "manages-traffic", "rest-api-definition", "http-api-definition", "websocket-api-definition", "http-api-backends", "case-study"))
item("d018", "filled", pick("rest-resource-method", "rest-method-and-integration", "deployment-needs-stage", "stage-lifecycle", "stage-named-reference", "stage-variables-like", "stage-variables-different", "mapping-template", "mock-integration-no"))
item("d019", "filled", pick("edge-optimized-default-rest", "edge-optimized-uses", "regional-endpoint", "private-endpoint", "private-api-isolated", "table-edge-optimized", "table-private-endpoint", "table-regional-endpoint", "custom-domain-all-regions", "regional-custom-domain"))
item("d020", "filled", pick("table-", "http-api-lower-latency", "http-api-minimal", "choose-rest-or-http", "http-api-oidc"), "One fact per decisive row of the seven comparison tables; Cognito row skipped (footnote line cannot be quoted separately).")
item("d021", "filled", pick("throttling-", "http-throttling-route-level"), "Order is stated: usage plan per-client or per-method, then per-method stage, then account per Region, then AWS Regional. Stage and method limits cannot be higher than the AWS throttling limits; per-client limits cannot be higher than per-account limits.")
item("d022", "filled", pick("usage-plan-not-hard-limits", "throttling-best-effort"))
item("d023", "filled", pick("usage-plan-definition", "usage-plan-rest-or-websocket", "usage-plan-throttle-limit", "usage-plan-limits-aggregate", "table-api-keys"), "NOT FOUND in the saved pages: 'quota per day, week or month'. The create-usage-plans page only shows an example with period=MONTH and says a quota limit applies within 'a specified time interval'; no sentence lists day, week and month. Looked in api-gateway-api-usage-plans, api-gateway-create-usage-plans, faq (faq lens).")
item("d024", "filled", pick("api-keys-not-for-authentication", "api-keys-shared", "api-keys-generated", "api-keys-with-authorizers"))
item("d025", "filled", pick("api-key-request-must", "api-key-source-header", "lambda-authorizer-usage-identifier"), "The page says 'enable API keys on API methods' and 'You can configure individual API methods to require API key authorization based on usage plan configuration'.")
item("d026", "filled", pick("access-control-", "whitepaper-three-authorization", "whitepaper-api-keys-usage"))
item("d027", "filled", pick("resource-policy-", "private-api-needs-resource", "private-api-whitepaper-cross", "table-resource-policies"))
item("d028", "filled", pick("auth-flow-", "waf-evaluated-before"), "Same-account and cross-account outcomes kept in separate facts; the claim names the scope.")
item("d029", "filled", pick("iam-"))
item("d030", "filled", pick("lambda-authorizer-"), "Default TTL 300 s, maximum 3600 s from the cross-account Lambda authorizer page (fetched for this item). REQUEST/TOKEN types and returned policy plus principal covered.")
item("d031", "filled", pick("cognito-authorizer-method-needs"), "Reuse: cognito-api-gateway-cognito-user-pools-authorizer, cognito-api-gateway-validates-user-pool-token, cognito-api-gateway-id-vs-access-token-scopes, cognito-api-gateway-aws-iam-with-identity-pool.")
item("d032", "filled", pick("jwt-authorizer-", "table-jwt"), "The REST API has no JWT authorizer type; a Lambda authorizer can validate JWTs for REST APIs (footnote of the comparison table).")
item("d033", "filled", pick("private-api-", "vpc-endpoint-policy-", "access-control-vpc-endpoint-policies"), "Private DNS note quoted with its scope (private DNS on: the default endpoint for public APIs cannot be accessed). The note is on the private APIs page, not on the important-notes page.")
item("d034", "filled", pick("waf-", "table-waf"), "Reuse: waf-faq-api-gateway-rest-apis, waf-api-associate-web-acl-rate, waf-rate-based-default-key-ip, waf-rate-based-counts-and-limits.")
item("d035", "filled", pick("mtls-", "table-mutual-tls", "access-control-client-ssl"))
item("d036", "filled", pick("integration-", "lambda-proxy-", "proxy-resource", "whitepaper-lambda-proxy"))
item("d037", "filled", pick("lambda-custom-integration-sync", "lambda-async-"), "The page does not state what the client receives for asynchronous invocation beyond 'the front-end REST API method doesn't return the result'. Not found: a sentence about the HTTP status the client gets, and about the integration timeout. Searched set-up-lambda-integration-async and the guide full text for InvocationType and X-Amz-Invocation-Type.")
item("d038", "filled", pick("http-api-first-class", "rest-api-dynamodb", "integration-aws-type", "wa-rel05-bp02-use-sqs"))
item("d039", "filled", pick("caching-", "metrics-cache"), "TTL default and maximum are in the numbers lens (api-gateway-cache-ttl). HTTP APIs do not have caching: table-caching-rest-yes-http-no.")
item("d040", "filled", pick("canary-", "stage-variables-", "stage-named", "table-canary"))
item("d041", "filled", pick("websocket-stateful", "websocket-two-way", "websocket-json-routes", "websocket-route-key", "websocket-three-predefined", "websocket-connect-route", "websocket-disconnect-route", "websocket-default-route", "websocket-no-servers", "websocket-chat", "decision-guide-websocket"))
item("d042", "filled", pick("websocket-connections-", "websocket-send-data", "websocket-access", "websocket-recommend", "websocket-lambda-authorizer", "websocket-binary"))
item("d043", "filled", pick("custom-domain-", "regional-custom-domain", "edge-optimized-custom-domain", "mtls-disable-default"), "Reuse: acm-api-gateway-certificate-region (edge-optimized: us-east-1; Regional: same Region as the API), acm-api-gateway-custom-domain, route53-alias-target-api-gateway, route53-api-gateway-regional-edge-private-alias, route53-api-gateway-needs-matching-custom-domain-name.")
item("d044", "filled", pick("cors-", "whitepaper-cors"))
item("d045", "filled", pick("resilience-"))
item("d046", "filled", pick("whitepaper-logic", "whitepaper-api-gateway-lambda", "whitepaper-serverless", "whitepaper-lambda-proxy", "whitepaper-built-in", "whitepaper-pay", "whitepaper-cache", "whitepaper-microservice", "whitepaper-cors"), "The whitepapers are marked 'for historical reference only' by AWS; facts are tier 2 and describe the pattern, not numbers. The claim 'each deployment includes a CloudFront distribution' in the stable-performance page was left out because it is not true for Regional or private endpoints.")
item("d047", "filled", pick("decision-guide-"), "Reuse: lambda-furl-recommended-simple-apps, lambda-furl-auth-public-or-iam, lambda-furl-no-endpoint-charge, lambda-furl-429-no-queue, lambda-function-url-auth-types, lambda-apigw-better-for-production, lambda-apigw-extra-features-waf-keys, lambda-apigateway-api-types, lambda-trigger-apigateway-sync, lambda-apigateway-sync-proxy-event, lambda-faq-https-via-api-gateway.")
item("d048", "partial", ["elb-lambda-target-request-body-max", "elb-lambda-target-response-json-max", "elb-lambda-target-same-account-region"], "Size limits found (1 MB request body, 1 MB response JSON for an ALB Lambda target). NOT FOUND: any AWS sentence saying what the ALB does not offer compared with API Gateway (usage plans, API keys, caching, request validation); the ELB page lists none. Reuse lambda-trigger-alb-sync.")
item("d049", "filled", pick("wa-rel05-bp02-"), "The page says the throttled client can 'handle the error and retry later'; it does not mention exponential backoff.")
item("d050", "filled", pick("metrics-", "logging-", "xray-", "monitoring-", "security-best-practice-cloudtrail", "table-xray", "table-execution", "table-access-logs", "table-cloudwatch"))
item("d051", "filled", pick("encryption-", "whitepaper-transit", "caching-encryption", "private-api-tls", "security-best-practice"), "Cache encryption is optional (caching-encryption-optional-for-sensitive-responses). HTTP APIs and WebSocket APIs support only TLS 1.2; private APIs support only TLS 1.2. The list of REST API security policy names is not on the saved pages.")
item("d052", "filled", pick("case-study-"), "Travelex and DoorDash used (quotes of 17 and 19 words naming API Gateway). CyberArk skipped: the only sentence that names API Gateway is longer than 25 words.")
out = {"label": "mine-33-behavior+decisions", "lens": "behavior+decisions", "chapter": "33", "facts_added": len(ids) + 0, "demand": d,
       "not_found": [
         {"item": "d023", "what": "quota period options (day, week, month)", "looked": ["api-gateway-api-usage-plans", "api-gateway-create-usage-plans"]},
         {"item": "d037", "what": "what status or body the client receives for an asynchronous (Event) invocation", "looked": ["set-up-lambda-integration-async", "full guide search InvocationType"]},
         {"item": "d048", "what": "AWS sentence on what an ALB with Lambda targets lacks compared with API Gateway", "looked": ["elasticloadbalancing/latest/application/lambda-functions"]}],
       "contradicted": [
         {"item": "d049", "expected": "retry with backoff", "page_says": "the consumer can handle the error and retry later (no mention of backoff)"},
         {"item": "d033", "expected": "private DNS note on the important-notes page", "page_says": "the note stands on the private APIs page (apigateway-private-apis)"}],
       "cross_service_facts": ["elb-lambda-target-request-body-max", "elb-lambda-target-response-json-max", "elb-lambda-target-same-account-region"]}
json.dump(out, open("mine-behavior+decisions.json", "w"), indent=1)
print({k: len(v["facts"]) for k, v in d.items()})
