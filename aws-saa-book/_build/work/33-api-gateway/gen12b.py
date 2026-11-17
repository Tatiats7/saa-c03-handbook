import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
fs=[F("whitepaper-microservice-client-sdks", "capability",
 "Amazon API Gateway provides programmatically generated client SDKs in a number of popular languages to reduce integration overhead.",
 "How does API Gateway reduce client integration work for many microservices?",
 ["programmatically generated client SDKs", "reduce integration overhead"],
 [ev(WP+"microservices-with-lambda", "Finally, Amazon API Gateway provides programmatically generated client SDKs in a number of popular languages to reduce integration overhead.")],
 scope="API Gateway", bullets=["2.1.K12"], tier=2, exam="extended")]
write("facts-behavior-12b.json", fs)
