import sys; sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/33-api-gateway")
from fh import *
fs=[F("deployment-needs-stage", "behavior",
 "An API deployment is a point-in-time snapshot of your API; to be available for clients to use, the deployment must be associated with one or more API stages.",
 "Must an API be deployed to a stage before clients can call it?",
 ["point-in-time snapshot of your API Gateway API", "must be associated with one or more API stages"],
 [ev("api-gateway-basic-concept", "A point-in-time snapshot of your API Gateway API. To be available for clients to use, the deployment must be associated with one or more API stages.")],
 scope="API deployments", bullets=["2.1.K1"], tier0=True)]
write("facts-behavior-01b.json", fs)
