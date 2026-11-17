import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
fs=[]
fs.append(F("websocket-binary-media-types-not-supported", "restriction",
 "Binary media types are not supported for WebSocket APIs; API Gateway returns a close status code when an endpoint receives a binary media type.",
 "Do WebSocket APIs support binary media types?",
 ["Binary media types aren't supported for WebSocket APIs", "when an endpoint receives a binary media type"],
 [ev("apigateway-websocket-api-overview", "API Gateway returns this status code when an endpoint receives a binary media type. Binary media types aren't supported for WebSocket APIs.")],
 scope="WebSocket APIs", bullets=["2.1.K1"], exam="extended"))
fs.append(F("custom-domain-wildcard-acm-validated", "capability",
 "With a wildcard custom domain name you can support an almost infinite number of domain names without exceeding the default quota, and creating one requires an ACM-issued certificate validated by the DNS or email validation method.",
 "How can you support many customer subdomains with one custom domain name?",
 ["almost infinite number of domain names", "validated using either the DNS or the email validation method"],
 [ev("how-to-custom-domains", "With wildcard custom domain names, you can support an almost infinite number of domain names without exceeding the default quota."),
  ev("how-to-custom-domains", "To create a wildcard custom domain name, you must provide a certificate issued by ACM that has been validated using either the DNS or the email validation method.")],
 scope="custom domain names", bullets=["2.1.K1"], exam="extended"))
write("facts-behavior-09b.json", fs)
