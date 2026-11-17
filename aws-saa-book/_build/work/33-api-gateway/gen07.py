import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
WAF = "apigateway-control-access-aws-waf"; MT = "rest-api-mutual-tls"
B = ["1.2.K4"]
fs = []
fs.append(F("waf-protects-rest-api-sql-injection-xss", "capability",
 "You can use AWS WAF to protect your API Gateway REST API from common web exploits such as SQL injection and cross-site scripting (XSS) attacks.",
 "Which API Gateway API type can AWS WAF protect, and from what?",
 ["common web exploits, such as SQL injection and cross-site scripting (XSS) attacks", "API Gateway REST API"],
 [ev(WAF, "You can use AWS WAF to protect your API Gateway REST API from common web exploits, such as SQL injection and cross-site scripting (XSS) attacks.")],
 scope="REST APIs", bullets=B, tier0=True))
fs.append(F("waf-rules-ip-cidr-country-sql-script", "capability",
 "AWS WAF rules for an API can allow or block requests from specified IP address ranges, CIDR blocks, a specific country or region, requests that contain malicious SQL code, and requests that contain malicious script.",
 "What kinds of requests can AWS WAF rules block for an API Gateway API?",
 ["specified IP address ranges, requests from CIDR blocks", "requests that contain malicious SQL code"],
 [ev(WAF, "For example, you can create rules to allow or block requests from specified IP address ranges, requests from CIDR blocks, requests that originate from a specific country or region, requests that contain malicious SQL code, or requests that contain malicious script.")],
 scope="REST APIs with AWS WAF", bullets=B))
fs.append(F("waf-rate-based-rules-per-client-ip", "capability",
 "With AWS WAF you can use rate-based rules to specify the number of web requests that are allowed by each client IP in a trailing, continuously updated, 5-minute period.",
 "How does an AWS WAF rate-based rule limit clients of an API?",
 ["rate-based rules", "each client IP in a trailing, continuously updated, 5-minute period"],
 [ev(WAF, "Additionally, you can create rules to block attacks from specific user agents, bad bots, and content scrapers. For example, you can use rate-based rules to specify the number of web requests that are allowed by each client IP in a trailing, continuously updated, 5-minute period.")],
 scope="REST APIs with AWS WAF", bullets=B+["4.4.S6"]))
fs.append(F("waf-requires-regional-web-acl", "restriction",
 "API Gateway requires an AWS WAFV2 web ACL for a Regional application or an AWS WAF Classic Regional web ACL.",
 "What kind of web ACL does API Gateway require?",
 ["AWS WAFV2 web ACL for a Regional application", "AWS WAF Classic Regional web ACL"],
 [ev(WAF, "API Gateway requires an AWS WAFV2 web ACL for a Regional application or an AWS WAF Classic Regional web ACL.")],
 scope="REST APIs with AWS WAF", bullets=B))
fs.append(F("waf-web-acl-same-region-as-api", "restriction",
 "The AWS WAFV2 web ACL and any other AWS WAFV2 resources that it uses must be located in the same Region as your API.",
 "Must the web ACL be in the same Region as the API?",
 ["must be located in the same Region as your API", "AWS WAFV2 resources"],
 [ev(WAF, "If you are using AWS WAFV2, select an AWS WAFV2 web ACL for a Regional application. The web ACL and any other AWS WAFV2 resources that it uses must be located in the same Region as your API.")],
 scope="REST APIs with AWS WAF", bullets=B))
fs.append(F("waf-web-acl-associated-with-stage", "behavior",
 "You enable AWS WAF for an API by associating a web ACL with an API stage, using the AWS WAF console, AWS SDK, CLI, or the API Gateway console.",
 "To what API Gateway resource do you attach an AWS WAF web ACL?",
 ["Associate the AWS WAF web ACL with an API stage", "AWS WAF console, AWS SDK, CLI"],
 [ev(WAF, "Associate the AWS WAF web ACL with an API stage. You can do this by using the AWS WAF console, AWS SDK, CLI, or by using the API Gateway console.")],
 scope="REST APIs with AWS WAF", bullets=B))
fs.append(F("mtls-two-way-x509-iot-b2b", "behavior",
 "Mutual TLS authentication requires two-way authentication between the client and the server: clients must present X.509 certificates to verify their identity to access your API, and it is a common requirement for IoT and business-to-business applications.",
 "What does mutual TLS require from the client?",
 ["two-way authentication between the client and the server", "clients must present X.509 certificates"],
 [ev(MT, "Mutual TLS authentication requires two-way authentication between the client and the server. With mutual TLS, clients must present X.509 certificates to verify their identity to access your API. Mutual TLS is a common requirement for Internet of Things (IoT) and business-to-business applications.")],
 scope="REST APIs, custom domain names", bullets=B, tier0=True, hard=True))
fs.append(F("mtls-with-other-auth-forwards-certificates", "behavior",
 "You can use mutual TLS along with other authorization and authentication operations that API Gateway supports, and API Gateway forwards the certificates that clients provide to Lambda authorizers and to backend integrations.",
 "Can mutual TLS be combined with other authorization, and who receives the client certificate?",
 ["along with other authorization and authentication operations", "forwards the certificates that clients provide"],
 [ev(MT, "You can use mutual TLS along with other authorization and authentication operations that API Gateway supports. API Gateway forwards the certificates that clients provide to Lambda authorizers and to backend integrations.")],
 scope="REST APIs", bullets=B))
fs.append(F("mtls-disable-default-execute-api-endpoint", "default",
 "By default, clients can invoke your API by using the execute-api endpoint that API Gateway generates; to ensure that clients can access the API only by using a custom domain name with mutual TLS, disable the default execute-api endpoint.",
 "Must the default execute-api endpoint be disabled when you require mutual TLS?",
 ["disable the default `execute-api` endpoint", "By default, clients can invoke your API"],
 [ev(MT, "By default, clients can invoke your API by using the `execute-api` endpoint that API Gateway generates for your API. To ensure that clients can access your API only by using a custom domain name with mutual TLS, disable the default `execute-api` endpoint.")],
 scope="REST APIs", dm="default", cond="mutual TLS on a custom domain name", bullets=B+["2.1.K1"], tier0=True))
fs.append(F("mtls-prerequisites-regional-domain-acm-s3-truststore", "restriction",
 "To configure mutual TLS you need a Regional custom domain name, at least one certificate configured in AWS Certificate Manager for the custom domain name, and a truststore configured and uploaded to Amazon S3.",
 "What do you need before you can configure mutual TLS for a REST API?",
 ["A Regional custom domain name", "truststore configured and uploaded to Amazon S3"],
 [ev(MT, "To configure mutual TLS you need: A Regional custom domain name At least one certificate configured in AWS Certificate Manager for your custom domain name A truststore configured and uploaded to Amazon S3")],
 scope="REST APIs", bullets=B+["2.1.K1"], tier0=True))
fs.append(F("mtls-truststore-pem-file-trusted-cas", "behavior",
 "A mutual TLS truststore is a text file with a .pem file extension that holds a trusted list of certificates from Certificate Authorities; you create it from the X.509 certificates that you trust to access your API.",
 "What is the truststore used for mutual TLS?",
 ["text files with a `.pem` file extension", "trusted list of certificates from Certificate Authorities"],
 [ev(MT, "Truststores are text files with a `.pem` file extension. They are a trusted list of certificates from Certificate Authorities. To use mutual TLS, create a truststore of X.509 certificates that you trust to access your API.")],
 scope="REST APIs, mutual TLS", bullets=B))
fs.append(F("mtls-lambda-authorizer-revocation-check", "capability",
 "API Gateway validates a number of certificate properties for mutual TLS, and you can use Lambda authorizers to perform additional checks when a client invokes an API, including checking whether a certificate has been revoked.",
 "How can you check whether a client certificate has been revoked with mutual TLS?",
 ["checking whether a certificate has been revoked", "use Lambda authorizers to perform additional checks"],
 [ev(MT, "API Gateway validates a number of certificate properties. You can use Lambda authorizers to perform additional checks when a client invokes an API, including checking whether a certificate has been revoked.")],
 scope="REST APIs, mutual TLS", bullets=B, exam="extended"))
write("facts-behavior-07.json", fs)
