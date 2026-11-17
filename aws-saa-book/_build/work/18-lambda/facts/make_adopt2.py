import json, os
D = "aws-saa-book/_build/work/18-lambda/facts/adopt2"
os.makedirs(D, exist_ok=True)
base = {"service": "lambda", "home_chapter": "18", "source_tier": 1, "hard": True, "tier0": False,
        "volatility": "stable", "changed": None}
GL = "docs/lambda/latest/dg/gettingstarted-limits"
GR = "docs/general/latest/gr/lambda-service"
KP = "docs/lambda/latest/dg/services-kinesis-parameters"
cmds = []


def f(src, t, r, id, kind, claim, question, values, scope, dom, adj, cond="", bullets=None, rel="reference",
      vol="stable", note=None):
    d = dict(base)
    d.update({"id": id, "kind": kind, "claim": claim, "question": question,
              "values": [{"key": k, "display": v} for k, v in values],
              "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
              "bullets": bullets or ["3.2.S4"], "exam_relevance": rel, "volatility": vol})
    if note:
        d["note"] = note
    p = f"{D}/{id}.json"
    json.dump(d, open(p, "w"), indent=1)
    cmds.append(f"python3 aws-saa-book/tools/saa.py facts adopt --source {src} --table {t} --row {r} --file {p} --by mine-18-numbers")


f(GL, 1, 15, "lambda-processes-threads-1024", "limit",
  "A function's execution environment is limited to 1,024 execution processes and threads; Lambda Managed Instances use the Bottlerocket default process and thread limits instead.",
  "How many processes and threads can a Lambda execution environment run?", [("max", "1,024")],
  "per execution environment", "max", False, cond="Lambda Managed Instances use Bottlerocket defaults")
f(GL, 1, 10, "lambda-container-image-settings-16-kb", "limit",
  "The container image settings of a function are limited to 16 KB.",
  "What is the size limit of a Lambda function's container image settings?", [("max", "16 KB")],
  "per function, container image settings", "max", False)
f(GL, 3, 0, "lambda-durable-running-executions", "quota",
  "Durable functions allow at most 5,000,000 running durable executions per Region by default (10,000,000 in US East (N. Virginia), US West (Oregon) and Europe (Ireland)); this is a soft limit that can be increased.",
  "How many durable executions can run at the same time in one Region?",
  [("default", "5,000,000 per Region"), ("large-regions", "10,000,000")],
  "per account, per Region", "default", True, cond="higher default in US East (N. Virginia), US West (Oregon), and Europe (Ireland)",
  bullets=["2.1.S1"])
f(GL, 3, 1, "lambda-durable-operations-per-execution", "limit",
  "One durable execution can have at most 3,000 durable operations, and this quota cannot be increased.",
  "How many durable operations can one Lambda durable execution have?", [("max", "3,000")],
  "per durable execution", "max", False, bullets=["2.1.S1"])
f(GL, 3, 2, "lambda-durable-storage-100-mb", "limit",
  "A durable execution can persist at most 100 MB of cumulative payload (storage written), and this quota cannot be increased.",
  "How much data can one Lambda durable execution persist?", [("max", "100 MB")],
  "per durable execution", "max", False, bullets=["2.1.S1"])
f(GL, 4, 1, "lambda-microvm-max-duration-8-hours", "limit",
  "A Lambda MicroVM can run for at most 8 hours (28,800 seconds), and this quota is not adjustable.",
  "What is the maximum execution duration of a Lambda MicroVM?", [("max", "8 hours"), ("seconds", "28,800 seconds")],
  "per MicroVM", "max", False, vol="frequently-changing",
  note="Lambda MicroVMs are new (What's New items about them are dated 2026-08); treat as not examinable yet unless a launch date before 2026-07-15 is found.")
f(GR, 1, 11, "lambda-scaling-rate-not-adjustable", "limit",
  "The concurrency scaling rate quota is 1,000 and is not adjustable: every 10 seconds, each synchronously invoked function can scale by an additional 1,000 concurrent executions until the total concurrency across functions in the Region reaches the account concurrency limit.",
  "Can you raise the Lambda concurrency scaling rate?",
  [("rate", "additional 1,000 concurrent executions"), ("period", "Every 10 seconds")],
  "per function, per Region", "max", False, cond="until the account concurrency limit is reached", bullets=["2.2.K10", "3.2.S4"],
  rel="extended")
f(GR, 1, 23, "lambda-eni-per-subnet-sg-combination", "quota",
  "Lambda creates one network interface for each combination of subnet and security group that functions connect to; the quota of 3,000 network interfaces per VPC is adjustable.",
  "How many network interfaces does Lambda create for VPC-attached functions?",
  [("rule", "each combination of subnet and security group"), ("default", "3,000")],
  "per VPC", "default", True, bullets=["2.2.K10", "2.1.S1"], rel="extended")
f(KP, 0, 0, "lambda-kinesis-batch-size-100", "default",
  "For a Kinesis event source mapping, the batch size defaults to 100 records and can be at most 10,000.",
  "What are the default and maximum batch sizes for a Lambda Kinesis event source?",
  [("default", "100"), ("max", "10,000")], "per Kinesis event source mapping", "default", True, bullets=["2.1.K5"],
  rel="extended")
f(KP, 0, 1, "lambda-kinesis-bisect-default-false", "default",
  "For a Kinesis event source mapping, BisectBatchOnFunctionError (split a failed batch) is off by default (false).",
  "Does Lambda split a failed Kinesis batch by default?", [("default", "false")],
  "per Kinesis event source mapping", "default", True, bullets=["2.1.K5"], rel="extended")
f(KP, 0, 2, "lambda-kinesis-failure-destination-sqs-sns", "capability",
  "A Kinesis event source mapping can send discarded records to an Amazon SQS queue or Amazon SNS topic destination.",
  "Where can Lambda send records it discards from a Kinesis stream?",
  [("dest", "Amazon SQS queue or Amazon SNS topic")], "per Kinesis event source mapping", "", True,
  bullets=["2.1.K5"], rel="extended")
f(KP, 0, 8, "lambda-kinesis-max-record-age", "default",
  "For a Kinesis event source mapping, MaximumRecordAgeInSeconds defaults to -1, which means infinite: Lambda does not discard records (Kinesis data retention still applies); the minimum is -1 and the maximum 604,800.",
  "How long does Lambda keep retrying old Kinesis records by default?",
  [("default", "-1 means infinite"), ("max", "604,800")], "per Kinesis event source mapping", "default", True,
  cond="Kinesis Data Streams data retention settings still apply", bullets=["2.1.K5"], rel="extended")
f(KP, 0, 9, "lambda-kinesis-max-retry-attempts", "default",
  "For a Kinesis event source mapping, MaximumRetryAttempts defaults to -1, which means infinite: failed records are retried until the record expires; the minimum is -1 and the maximum 10,000.",
  "How many times does Lambda retry a failed Kinesis batch by default?",
  [("default", "failed records are retried until the record expires"), ("max", "10,000")],
  "per Kinesis event source mapping", "default", True, bullets=["2.1.K5"], rel="extended")
f(KP, 0, 13, "lambda-kinesis-tumbling-window-900", "limit",
  "For a Kinesis event source mapping, TumblingWindowInSeconds can be set from a minimum of 0 to a maximum of 900.",
  "What is the range of the tumbling window for a Lambda Kinesis event source?",
  [("max", "900")], "per Kinesis event source mapping", "max", False, bullets=["2.1.K5"])

open(f"{D}/cmds.txt", "w").write("\n".join(cmds) + "\n")
print("\n".join(cmds))
