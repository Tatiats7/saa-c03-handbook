import json
F=[]
def ev(src, quote, th=None):
    url = "https://docs.aws.amazon.com/" + src[len("docs/"):] + ".html" if src.startswith("docs/") else "https://aws.amazon.com/" + src[len("www/"):] + "/"
    return {"source_id": src, "url": url, "quote": quote, "table_header": th}
def f(id, kind, claim, question, values, scope, dom, adj, evs, cond="", tier0=False, bullets=None, rel="core", vol="stable", tier=1, hard=True, note=None):
    d={"id": id, "service": "lambda", "home_chapter": "18", "kind": kind, "claim": claim, "question": question,
       "values": [{"key": k, "display": v} for k, v in values],
       "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
       "evidence": evs, "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol, "changed": None,
       "exam_relevance": rel, "bullets": bullets or ["3.2.S4"]}
    if note: d["note"]=note
    F.append(d)
M="docs/lambda/latest/dg/configuration-memory"; T="docs/lambda/latest/dg/configuration-timeout"; E="docs/lambda/latest/dg/configuration-ephemeral-storage"
R="docs/lambda/latest/dg/lambda-runtime-environment"; Z="docs/lambda/latest/dg/configuration-function-zip"; S="docs/lambda/latest/dg/configuration-self-managed-storage"
Q="docs/lambda/latest/dg/gettingstarted-limits"
f("lambda-timeout-default", "default", "The default function timeout is 3 seconds; you can raise it in increments of 1 second up to the maximum of 900 seconds (15 minutes).",
  "What is the default timeout of a Lambda function?", [("default","3 seconds"),("increment","increments of 1 second"),("max","900 seconds (15 minutes)")], "per function", "default", True,
  [ev(T, "The default value for this setting is 3 seconds, but you can adjust this in increments of 1 second up to a maximum value of 900 seconds (15 minutes).")], tier0=True)
f("lambda-memory-default", "default", "The default memory setting, 128 MB, is the lowest possible setting; AWS recommends it only for simple functions that transform and route events.",
  "What is the default memory of a Lambda function?", [("default","128 MB")], "per function", "default", True,
  [ev(M, "The default setting, 128 MB, is the lowest possible setting. We recommend that you only use 128 MB for simple Lambda functions, such as those that transform and route events to other AWS services.")])
f("lambda-cpu-proportional-to-memory", "behavior", "Lambda allocates CPU power in proportion to the amount of memory configured; memory is the one setting that changes both.",
  "How do you give a Lambda function more CPU?", [("rule","CPU power in proportion to the amount of memory configured")], "per function", "", True,
  [ev(M, "Lambda allocates CPU power in proportion to the amount of memory configured.")], tier0=True)
f("lambda-one-vcpu-at-1769-mb", "behavior", "At 1,769 MB of memory, a function has the equivalent of one vCPU.",
  "At what memory setting does a Lambda function get the equivalent of one vCPU?", [("threshold","1,769 MB"),("cpu","one vCPU")], "per function", "", False,
  [ev(M, "At 1,769 MB, a function has the equivalent of one vCPU (one vCPU-second of credits per second).")])
f("lambda-init-phase-10-seconds", "limit", "The Init phase is limited to 10 seconds; if it does not complete in 10 seconds, Lambda retries the Init phase at the first invocation with the configured function timeout.",
  "How long may a Lambda function's initialization code run?", [("max","10 seconds")], "per execution environment, Init phase", "max", False,
  [ev(R, "The `Init` phase is limited to 10 seconds. If all three tasks do not complete within 10 seconds, Lambda retries the `Init` phase at the time of the first function invocation with the configured function timeout.")], bullets=["3.2.K5"], rel="extended")
f("lambda-init-10-seconds-exceptions", "limit", "The 10-second Init timeout does not apply to functions using provisioned concurrency, SnapStart or Lambda Managed Instances; their initialization code can run for up to 15 minutes, with a time limit of 130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher.",
  "Which Lambda functions are exempt from the 10-second Init limit, and how long may their initialization run?", [("exempt","provisioned concurrency, SnapStart, or Lambda Managed Instances"),("max","up to 15 minutes"),("rule","130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher")], "per execution environment, Init phase", "max", False,
  [ev(R, "The 10-second timeout doesn't apply to functions that are using provisioned concurrency, SnapStart, or Lambda Managed Instances. For provisioned concurrency, SnapStart, and Managed Instances functions, your initialization code can run for up to 15 minutes. The time limit is 130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher.")],
  cond="functions using provisioned concurrency, SnapStart or Lambda Managed Instances", bullets=["3.2.K5"], rel="extended")
f("lambda-tmp-unique-per-environment", "behavior", "The /tmp ephemeral storage is temporary and unique to each execution environment.",
  "Is Lambda's /tmp storage shared between execution environments?", [("rule","temporary and unique to each execution environment")], "per execution environment, /tmp directory", "", False,
  [ev(E, "Lambda provides ephemeral storage for functions in the `/tmp` directory. This storage is temporary and unique to each execution environment.")], bullets=["3.2.S4","3.2.K5"])
f("lambda-tmp-encrypted-at-rest", "behavior", "All data stored in /tmp is encrypted at rest with a key managed by AWS.",
  "Is Lambda's /tmp storage encrypted?", [("rule","encrypted at rest with a key managed by AWS")], "per execution environment, /tmp directory", "", False,
  [ev(E, "All data stored in `/tmp` is encrypted at rest with a key managed by AWS.")], bullets=["1.4.S3"], rel="extended")
f("lambda-zip-over-50-mb-from-s3", "restriction", "In the console, a .zip archive smaller than 50 MB can be uploaded from your machine; a larger file must be uploaded to the function from an Amazon S3 bucket.",
  "How do you deploy a Lambda .zip package larger than 50 MB?", [("max-direct","smaller than 50 MB"),("larger","upload the file to the function from an Amazon S3 bucket")], "per deployment package (.zip), console upload", "max", False,
  [ev(Z, "If the .zip file archive is smaller than 50 MB, you can upload the .zip file archive from your local machine. If the file is larger than 50 MB, upload the file to the function from an Amazon S3 bucket.")])
f("lambda-self-managed-storage-not-counted", "behavior", "With self-managed S3 code storage, Lambda references the code in your S3 bucket and does not store a copy, so that code does not count against the Lambda-managed storage quota.",
  "How do you avoid the Lambda code storage quota?", [("rule","does not count against your Lambda-managed storage quota")], "per function or layer using self-managed S3 code storage", "", False,
  [ev(S, "With self-managed S3 code storage, you can configure Lambda to reference your code directly from an S3 bucket in your account. Lambda does not store a copy of your code, so the code does not count against your Lambda-managed storage quota.")], bullets=["2.2.K10"], rel="extended", vol="frequently-changing",
  note="Self-managed S3 code storage is a 2026 feature; check the GA date against the 2026-07-15 cutoff (decisions+changes lens).")
f("lambda-self-managed-storage-250-mb-unchanged", "restriction", "Self-managed S3 code storage does not change the maximum .zip deployment package size, which remains 250 MB (unzipped).",
  "Does self-managed S3 code storage raise the deployment package size limit?", [("max","250 MB (unzipped)")], "per deployment package (.zip), self-managed S3 code storage", "max", False,
  [ev(S, "Self-managed S3 code storage does not change the maximum .zip deployment package size, which remains at 250 MB (unzipped).")], bullets=["2.2.K10"], rel="extended", vol="frequently-changing")
f("lambda-new-account-reduced-quotas", "behavior", "New AWS accounts have reduced concurrency and memory quotas for Lambda functions, and AWS raises these quotas automatically based on usage.",
  "Do new AWS accounts get the full default Lambda concurrency quota?", [("rule","reduced concurrency and memory quotas"),("raise","AWS raises these quotas automatically based on your usage")], "per new AWS account", "default", True,
  [ev(Q, "New AWS accounts have reduced concurrency and memory quotas for Lambda Functions and Lambda MicroVMs. AWS raises these quotas automatically based on your usage.")], bullets=["2.2.K10"], rel="extended")
f("lambda-invocation-15-minutes-10240-mb", "limit", "Code can run for up to 15 minutes in a single invocation, and a single function can use up to 10,240 MB of memory.",
  "What are the two ceilings that decide whether a job fits in one Lambda invocation?", [("duration","up to 15 minutes"),("memory","up to 10,240 MB")], "per invocation and per function", "max", False,
  [ev(Q, "Code can run for up to 15 minutes in a single invocation (up to 90 minutes for Lambda Managed Instances functions invoked asynchronously or through any event source mapping except Amazon MQ and Amazon DocumentDB) and a single function can use up to 10,240 MB of memory.")], tier0=True, bullets=["3.2.S4","2.1.S5"])
f("lambda-mb-means-1024-kb", "behavior", "In the Lambda documentation, log messages and console, MB (rather than MiB) means 1,024 KB.",
  "Does Lambda's MB mean 1,000 KB or 1,024 KB?", [("rule","MB (rather than MiB) to refer to 1,024 KB")], "Lambda documentation, logs and console", "", False,
  [ev(Q, "The Lambda documentation, log messages, and console use the abbreviation MB (rather than MiB) to refer to 1,024 KB.")], rel="reference")
f("lambda-quota-scope-region-vs-vpc", "behavior", "Quotas for concurrent executions and storage apply per AWS Region, while elastic network interface (ENI) quotas apply per VPC regardless of Region.",
  "At what scope do Lambda's concurrency, storage and ENI quotas apply?", [("region","per AWS Region"),("vpc","per virtual private cloud (VPC), regardless of Region")], "per account", "", False,
  [ev(Q, "Quotas for concurrent executions and storage apply per AWS Region. Elastic network interface (ENI) quotas apply per virtual private cloud (VPC), regardless of Region.")], bullets=["2.2.K10"], rel="extended")
f("lambda-config-quotas-not-changeable", "restriction", "The function configuration, deployment and execution quotas (memory, timeout, payload, package size and so on) cannot be changed, except where the quotas page notes otherwise.",
  "Can you request an increase to Lambda's memory, timeout or package-size limits?", [("rule","Except as noted, they can't be changed")], "function configuration, deployment and execution quotas", "max", False,
  [ev(Q, "The following quotas apply to function configuration, deployment, and execution. Except as noted, they can't be changed.")], bullets=["2.2.K10","3.2.S4"])
f("lambda-quotas-hard-vs-soft", "behavior", "Service quotas consist of hard limits, which you cannot change, and soft limits, for which you can request increases.",
  "What is the difference between a hard and a soft Lambda quota?", [("rule","hard limits, which you cannot change, and soft limits, which you can request increases for")], "AWS service quotas", "", False,
  [ev(Q, "Service quotas exist in all AWS services and consist of hard limits, which you cannot change, and soft limits, which you can request increases for.")], bullets=["2.2.K10"], rel="extended")
json.dump(F, open("aws-saa-book/_build/work/18-lambda/facts/n02-config.json","w"), indent=1)
print(len(F))
