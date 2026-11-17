import json, os
D = "aws-saa-book/_build/work/18-lambda/facts/adopt"
os.makedirs(D, exist_ok=True)
base = {"service": "lambda", "home_chapter": "18", "source_tier": 1, "hard": True, "tier0": False, "volatility": "stable", "changed": None, "exam_relevance": "core"}
F = []
def f(id, kind, claim, question, values, scope, dom, adj, cond="", tier0=False, bullets=None, rel="core", vol="stable", note=None):
    d = dict(base); d.update({"id": id, "kind": kind, "claim": claim, "question": question,
        "values": [{"key": k, "display": v} for k, v in values],
        "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
        "tier0": tier0, "bullets": bullets or ["3.2.S4"], "exam_relevance": rel, "volatility": vol})
    if note: d["note"] = note
    F.append(d)

Q = "docs/lambda/latest/dg/gettingstarted-limits"
# table 0
f("lambda-concurrent-executions-default", "quota", "The default quota for concurrent executions is 1,000 per account per Region, and it can be increased up to tens of thousands.",
  "What is the default Lambda concurrent executions quota, and how far can it be raised?", [("default", "1,000"), ("max", "Tens of thousands")], "per account, per Region", "default", True, tier0=True, bullets=["2.2.K10", "3.2.S4"])
f("lambda-code-storage-quota", "quota", "Lambda-managed storage for uploaded .zip functions and layers is 300 GB (unzipped) per Region and is not increasable; use self-managed S3 code storage instead.",
  "How much Lambda-managed code storage does an account get per Region, and can it be raised?", [("max", "300 GB (unzipped)"), ("not-increasable", "Not increasable")], "per account, per Region", "max", False, bullets=["2.2.K10"], rel="extended",
  note="The General Reference quotas table (docs/general/latest/gr/lambda-service, row 'Function and layer storage') lists the same 300 GB as Adjustable: Yes. The developer guide quotas page is taken as current truth per the mine plan.")
f("lambda-eni-per-vpc-quota", "quota", "Lambda's quota for elastic network interfaces per VPC is 3,000 by default and can be increased to thousands; the quota is shared with other services such as Amazon EFS.",
  "How many elastic network interfaces per VPC can Lambda create by default?", [("default", "3,000"), ("max", "Thousands")], "per VPC", "default", True, cond="shared with other services, such as Amazon EFS", bullets=["2.2.K10"], rel="extended")
# table 1
f("lambda-timeout-max", "limit", "The maximum function timeout is 900 seconds (15 minutes).",
  "What is the maximum timeout of a Lambda function?", [("max-seconds", "900 seconds"), ("max-minutes", "15 minutes")], "per function", "max", False, tier0=True)
f("lambda-managed-instances-timeout-90-min", "limit", "For functions using AWS Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum timeout of 5,400 seconds (90 minutes).",
  "What is the maximum timeout for a Lambda Managed Instances function invoked asynchronously or through an event source mapping?", [("max-seconds", "5,400 seconds"), ("max-minutes", "90 minutes")], "per function on Lambda Managed Instances", "max", False,
  cond="asynchronous invocations and event source mapping invocations, except Amazon MQ and Amazon DocumentDB", rel="reference", vol="frequently-changing", note="Not examinable yet: Lambda Managed Instances and the 90-minute timeout are GA after 2026-07-15 (see FRESHNESS 2026-09-09).")
f("lambda-env-vars-size", "limit", "All environment variables of a function together are limited to 4 KB in aggregate.",
  "What is the size limit for a Lambda function's environment variables?", [("max", "4 KB")], "per function, all environment variables in aggregate", "max", False, rel="extended")
f("lambda-resource-policy-size", "limit", "A function's resource-based policy is limited to 20 KB.",
  "What is the size limit of a Lambda function's resource-based policy?", [("max", "20 KB")], "per function", "max", False, rel="reference")
f("lambda-layers-per-function", "limit", "A function can have at most 5 layers.",
  "How many layers can a Lambda function use?", [("max", "5 layers")], "per function", "max", False, rel="core")
f("lambda-concurrency-scaling-rate", "limit", "Each function's concurrency scales by up to 1,000 execution environments every 10 seconds.",
  "How fast can one Lambda function scale its concurrency?", [("rate", "1,000 execution environments every 10 seconds")], "per function", "max", False, tier0=True, bullets=["2.2.K10", "3.2.S4"], vol="changed-since-2022",
  note="Replaced the old account-wide burst limits (500 to 3,000 per Region) in November 2023; the guide no longer states the old values. A change fact with the date is the decisions+changes lens's job.")
f("lambda-payload-sync", "limit", "A synchronous invocation's request and response payloads are each limited to 6 MB.",
  "What is the maximum payload size for a synchronous Lambda invocation?", [("max", "6 MB")], "per invocation (synchronous), request and response each", "max", False, tier0=True, bullets=["2.1.K5", "3.2.S4"])
f("lambda-payload-async", "limit", "An asynchronous invocation's payload is limited to 1 MB.",
  "What is the maximum payload size for an asynchronous Lambda invocation?", [("max", "1 MB")], "per invocation (asynchronous)", "max", False, bullets=["2.1.K5", "3.2.S4"], vol="changed-since-2022",
  note="Raised from 256 KB to 1 MB in 2025; the old value is not stated on this page. Change fact belongs to the decisions+changes lens.")
f("lambda-payload-streamed-response", "limit", "A streamed response (synchronous) is limited to 200 MB.",
  "What is the maximum size of a Lambda streamed response?", [("max", "200 MB")], "per invocation (synchronous), streamed response", "max", False, bullets=["2.1.S1", "3.2.S4"], rel="extended")
f("lambda-streamed-response-bandwidth", "limit", "Bandwidth for a streamed response is uncapped for the first 6 MB; for responses larger than 6 MB the remainder is limited to 2MBps.",
  "How fast can a Lambda streamed response be delivered?", [("uncapped", "Uncapped for the first 6 MB"), ("rest", "2MBps for the remainder")], "per streamed response", "max", False, bullets=["2.1.S1"], rel="extended")
f("lambda-network-bandwidth-per-env", "limit", "Network bandwidth per execution environment is 625 Mbps.",
  "How much network bandwidth does one Lambda execution environment get?", [("max", "625 Mbps")], "per execution environment", "max", True, cond="for functions not attached to a VPC, an increase can be requested through the Service Quotas console", rel="reference", vol="changed-since-2022",
  note="The raised ceiling (up to 3,000 Mbps at 10,240 MB, not in a VPC) is a FRESHNESS item of 2026-08-05: not examinable yet. See lambda-network-bandwidth-raised.")
f("lambda-network-bandwidth-raised", "limit", "After an approved increase, for functions not attached to a VPC, network bandwidth scales with memory starting at 2,048 MB and reaches a maximum of up to 3,000 Mbps at 10,240 MB.",
  "How high can Lambda network bandwidth go after a quota increase, and for which functions?", [("max", "3,000 Mbps"), ("start", "2,048 MB")], "per execution environment, functions not attached to a VPC", "max", True, cond="after approval of a Service Quotas increase", rel="reference", vol="frequently-changing",
  note="Not examinable yet: released 2026-08-05 (FRESHNESS), after the 2026-07-15 cutoff.")
f("lambda-zip-package-50-mb", "limit", "A .zip deployment package is limited to 50 MB (zipped) when uploaded directly through the Lambda API, SDKs or console; larger files must be uploaded through Amazon S3.",
  "What is the size limit of a Lambda .zip deployment package uploaded directly, and what do you do with a larger one?", [("max", "50 MB"), ("larger", "Upload larger files with Amazon S3")], "per deployment package (.zip), direct upload", "max", False, tier0=True)
f("lambda-package-250-mb-unzipped", "limit", "The unzipped contents of a deployment package, including layers and custom runtimes, are limited to 250 MB.",
  "What is the maximum unzipped size of a Lambda deployment package including layers?", [("max", "250 MB")], "per function, deployment package contents including layers and custom runtimes, unzipped", "max", False, tier0=True)
f("lambda-container-image-10-gb", "limit", "A container image for Lambda is limited to 10 GB, measured as the maximum uncompressed image size including all layers.",
  "What is the maximum container image size for a Lambda function?", [("max", "10 GB")], "per function, container image, uncompressed including all layers", "max", False, tier0=True)
f("lambda-tmp-storage-range", "limit", "The /tmp directory storage can be set between 512 MB and 10,240 MB, in 1-MB increments.",
  "How much /tmp ephemeral storage can a Lambda function have?", [("min", "512 MB"), ("max", "10,240 MB"), ("increment", "1-MB increments")], "per function, /tmp directory", "max", False, tier0=True)
f("lambda-file-descriptors", "limit", "A function's execution environment is limited to 1,024 file descriptors.",
  "How many file descriptors can a Lambda execution environment have open?", [("max", "1,024")], "per execution environment", "max", False, rel="reference")
f("lambda-test-events-console", "limit", "The console editor keeps at most 10 test events per function.",
  "How many test events can you save in the Lambda console editor?", [("max", "10")], "per function, console editor", "max", False, rel="reference")
# table 2
f("lambda-sync-requests-per-env", "limit", "For synchronous invocations, each instance of the execution environment can serve up to 10 requests per second, so the total invocation limit is 10 times the concurrency limit.",
  "How many synchronous requests per second can one Lambda execution environment serve?", [("rate", "10 requests per second"), ("total", "10 times your concurrency limit")], "per function, per Region, synchronous invocations", "max", False, bullets=["2.2.K10"], rel="extended")
f("lambda-async-requests-per-env", "limit", "For asynchronous invocations, each instance of the execution environment can serve an unlimited number of requests, so the invocation limit depends only on the concurrency available to the function.",
  "Is there a per-environment request rate limit for asynchronous Lambda invocations?", [("unlimited", "unlimited number of requests")], "per function, per Region, asynchronous invocations", "", False, bullets=["2.2.K10"], rel="reference")
f("lambda-provisioned-concurrency-rps", "limit", "A function version or alias with provisioned concurrency can be invoked at up to 10 x its allocated provisioned concurrency in requests per second.",
  "How many requests per second can a Lambda function with provisioned concurrency serve?", [("rate", "10 x allocated provisioned concurrency")], "per function version or alias", "max", False, cond="applies only to functions that use provisioned concurrency", bullets=["2.2.K10"], rel="extended")
f("lambda-getfunction-api-rate", "limit", "The GetFunction API is limited to 100 requests per second and cannot be increased.",
  "What is the rate limit for the Lambda GetFunction API?", [("rate", "100 requests per second")], "per account, per Region, GetFunction API", "max", False, bullets=["2.2.K10"], rel="reference")
f("lambda-getpolicy-api-rate", "limit", "The GetPolicy API is limited to 15 requests per second and cannot be increased.",
  "What is the rate limit for the Lambda GetPolicy API?", [("rate", "15 requests per second")], "per account, per Region, GetPolicy API", "max", False, bullets=["2.2.K10"], rel="reference")
f("lambda-control-plane-api-rate", "limit", "The remaining control plane APIs (excluding invocation, GetFunction and GetPolicy) share one limit of 15 requests per second across all APIs, and it cannot be increased.",
  "What is the rate limit for Lambda control plane API calls?", [("rate", "15 requests per second across all APIs")], "per account, per Region, all control plane APIs together", "max", False, bullets=["2.2.K10"], rel="reference")

rows = {"lambda-concurrent-executions-default": (0,0), "lambda-code-storage-quota": (0,1), "lambda-eni-per-vpc-quota": (0,3),
 "lambda-timeout-max": (1,1), "lambda-managed-instances-timeout-90-min": (1,1), "lambda-env-vars-size": (1,2), "lambda-resource-policy-size": (1,3),
 "lambda-layers-per-function": (1,4), "lambda-concurrency-scaling-rate": (1,5), "lambda-payload-sync": (1,6), "lambda-payload-async": (1,6),
 "lambda-payload-streamed-response": (1,6), "lambda-streamed-response-bandwidth": (1,7), "lambda-network-bandwidth-per-env": (1,8), "lambda-network-bandwidth-raised": (1,8),
 "lambda-zip-package-50-mb": (1,9), "lambda-package-250-mb-unzipped": (1,9), "lambda-container-image-10-gb": (1,11), "lambda-tmp-storage-range": (1,13),
 "lambda-file-descriptors": (1,14), "lambda-test-events-console": (1,12),
 "lambda-sync-requests-per-env": (2,0), "lambda-async-requests-per-env": (2,1), "lambda-provisioned-concurrency-rps": (2,2), "lambda-getfunction-api-rate": (2,3), "lambda-getpolicy-api-rate": (2,4), "lambda-control-plane-api-rate": (2,5)}
cmds = []
for d in F:
    t, r = rows[d["id"]]
    p = f"{D}/{d['id']}.json"
    json.dump(d, open(p, "w"), indent=1)
    cmds.append(f"python3 aws-saa-book/tools/saa.py facts adopt --source {Q} --table {t} --row {r} --file {p} --by mine-18-numbers")
open(f"{D}/cmds.txt", "w").write("\n".join(cmds) + "\n")
print(len(F))
