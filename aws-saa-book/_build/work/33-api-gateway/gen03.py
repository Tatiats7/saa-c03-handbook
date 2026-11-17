import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
HA = "| Authorization options | REST API | HTTP API |"
HM = "| Features | REST API | HTTP API |"
HF = "| Feature | REST API | HTTP API |"
fs = []
fs.append(F("table-jwt-authorizer-http-yes-rest-no", "capability",
 "A JSON Web Token (JWT) authorizer is available for HTTP APIs, not REST APIs: the AWS comparison table lists No for REST APIs and Yes for HTTP APIs, and a Lambda authorizer can validate JWTs for REST APIs.",
 "Does the REST API have a JWT authorizer type?",
 ["JSON Web Token (JWT)", "Lambda authorizer to validate JWTs for REST APIs"],
 [T("http-api-vs-rest", "| JSON Web Token (JWT) 2 | No | Yes |", HA),
  ev("http-api-vs-rest", "2 You can use a Lambda authorizer to validate JWTs for REST APIs.")],
 scope="REST APIs versus HTTP APIs", bullets=["1.2.K4", "2.1.K1"], tier0=True, hard=True))
fs.append(row("table-api-keys-rest-yes-http-no", "API keys", "Yes", "No", HM, "Do HTTP APIs support API keys?", bullets=["4.4.S6","2.1.K1"], tier0=True))
fs.append(row("table-per-client-rate-limiting-rest-yes-http-no", "Per-client rate limiting", "Yes", "No", HM, "Do HTTP APIs support per-client rate limiting?", bullets=["4.4.S6","2.1.K1"], tier0=True))
fs.append(row("table-per-client-usage-throttling-rest-yes-http-no", "Per-client usage throttling", "Yes", "No", HM, "Do HTTP APIs support per-client usage throttling?", bullets=["4.4.S6","2.1.K1"]))
fs.append(row("table-developer-portal-rest-yes-http-no", "Developer portal", "Yes", "No", HM, "Which API type supports a developer portal?", exam="extended"))
fs.append(row("table-caching-rest-yes-http-no", "Caching", "Yes", "No", HM.replace("Features","Features"), "Is caching available for HTTP APIs?", tier0=True))
fs.append(row("table-automatic-deployments-http-yes-rest-no", "Automatic deployments", "No", "Yes", HM, "Which API type offers automatic deployments?"))
fs.append(row("table-canary-release-rest-yes-http-no", "Canary release deployments", "Yes", "No", HM, "Do HTTP APIs support canary release deployments?", tier0=True))
fs.append(row("table-request-validation-rest-yes-http-no", "Request validation", "Yes", "No", HM, "Which API type supports request validation?"))
fs.append(row("table-request-body-transformation-rest-yes-http-no", "Request body transformation", "Yes", "No", HM, "Which API type supports request body transformation?", exam="extended"))
fs.append(row("table-custom-gateway-responses-rest-yes-http-no", "Custom gateway responses", "Yes", "No", HM, "Which API type supports custom gateway responses?", exam="reference"))
fs.append(row("table-xray-tracing-rest-yes-http-no", "AWS X-Ray tracing", "Yes", "No", HF, "Which API type supports AWS X-Ray tracing?", bullets=["2.2.K10","2.1.K1"]))
fs.append(row("table-execution-logs-rest-yes-http-no", "Execution logs", "Yes", "No", HF, "Which API type supports execution logs?", bullets=["2.2.K10","2.1.K1"]))
fs.append(row("table-access-logs-firehose-rest-yes-http-no", "Access logs to Amazon Data Firehose", "Yes", "No", HF, "Which API type can send access logs to Amazon Data Firehose?", bullets=["2.2.K10","2.1.K1"], exam="extended"))
fs.append(row("table-cloudwatch-metrics-rest-and-http", "Amazon CloudWatch metrics", "Yes", "Yes", HF, "Do both REST and HTTP APIs publish CloudWatch metrics?", bullets=["2.2.K10"]))
fs.append(row("table-private-integration-nlb-rest-and-http", "Private integrations with Network Load Balancers", "Yes", "Yes", HF, "Which API types support private integrations with Network Load Balancers?", exam="extended"))
fs.append(row("table-private-integration-alb-rest-and-http", "Private integrations with Application Load Balancers", "Yes", "Yes", HF, "Which API types support private integrations with Application Load Balancers?", exam="extended"))
fs.append(row("table-private-integration-cloud-map-http-yes-rest-no", "Private integrations with AWS Cloud Map", "No", "Yes", HF, "Which API type supports private integrations with AWS Cloud Map?", exam="extended"))
fs.append(row("table-mock-integrations-rest-yes-http-no", "Mock integrations", "Yes", "No", HF, "Which API type supports mock integrations?", exam="reference"))
fs.append(row("table-response-streaming-rest-yes-http-no", "Response streaming", "Yes", "No", HF, "Which API type supports response streaming?", exam="reference"))
write("facts-behavior-03.json", fs)
