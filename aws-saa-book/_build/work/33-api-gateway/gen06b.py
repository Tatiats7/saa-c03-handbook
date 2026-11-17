import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
LA = "apigateway-use-lambda-authorizer"
fs=[F("lambda-authorizer-two-types-request-token", "behavior",
 "There are two types of Lambda authorizers: a request parameter-based REQUEST authorizer and a token-based TOKEN authorizer.",
 "What are the two types of Lambda authorizers?",
 ["Request parameter-based Lambda authorizer", "Token-based Lambda authorizer"],
 [ev(LA, "There are two types of Lambda authorizers: Request parameter-based Lambda authorizer (`REQUEST` authorizer) A `REQUEST` authorizer receives the caller's identity in a combination of headers, query string parameters, `stageVariables`, and `$context` variables."),
  ev(LA, "Token-based Lambda authorizer (`TOKEN` authorizer) A `TOKEN` authorizer receives the caller's identity in a bearer token, such as a JSON Web Token (JWT) or an OAuth token.")],
 scope="REST APIs, Lambda authorizers", bullets=["1.2.K4"], tier0=True)]
write("facts-behavior-06b.json", fs)
