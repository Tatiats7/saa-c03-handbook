import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
fs=[F("waf-rate-based-rules-per-client-ip", "capability",
 "With AWS WAF you can use rate-based rules to specify the number of web requests that are allowed by each client IP in a trailing, continuously updated, 5-minute period.",
 "How does an AWS WAF rate-based rule limit clients of an API?",
 ["rate-based rules", "each client IP in a trailing, continuously updated, 5-minute period"],
 [ev("apigateway-control-access-aws-waf", "Additionally, you can create rules to block attacks from specific user agents, bad bots, and content scrapers. For example, you can use rate-based rules to specify the number of web requests that are allowed by each client IP in a trailing, continuously updated, 5-minute period.")],
 scope="REST APIs with AWS WAF", bullets=["1.2.K4","4.4.S6"])]
write("facts-behavior-07b.json", fs)
