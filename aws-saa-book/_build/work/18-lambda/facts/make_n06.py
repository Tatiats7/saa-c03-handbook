import json
F=[]
def ev(src, quote, th=None):
    url = "https://docs.aws.amazon.com/" + src[len("docs/"):] + ".html"
    return {"source_id": src, "url": url, "quote": quote, "table_header": th}
def f(id, kind, claim, question, values, scope, dom, adj, evs, cond="", tier0=False, bullets=None, rel="core", vol="stable", tier=1, hard=True, note=None):
    d={"id": id, "service": "lambda", "home_chapter": "18", "kind": kind, "claim": claim, "question": question,
       "values": [{"key": k, "display": v} for k, v in values],
       "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
       "evidence": evs, "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol, "changed": None,
       "exam_relevance": rel, "bullets": bullets or ["2.1.K5"]}
    if note: d["note"]=note
    F.append(d)
SS="docs/lambda/latest/dg/services-sqs-scaling"; K="docs/lambda/latest/dg/with-kinesis"; AE="docs/lambda/latest/dg/invocation-async-error-handling"; MI="docs/lambda/latest/dg/lambda-managed-instances"
f("lambda-sqs-scaling-5-batches-300-per-minute-1250", "limit", "For a standard SQS queue, Lambda starts with five batches and five concurrent invocations, adds up to 300 more concurrent invokes per minute while messages remain, and one event source mapping can process at most 1,250 invokes simultaneously.",
  "How does Lambda scale its SQS pollers, and what is the ceiling per event source mapping?", [("start","five batches at a time with five concurrent invocations"),("rate","up to 300 more concurrent invokes per minute"),("max","1,250")], "per SQS event source mapping, standard queue", "max", False,
  [ev(SS, "When messages are available, Lambda starts processing five batches at a time with five concurrent invocations of your function. If messages are still available, Lambda increases the number of processes that are reading batches by up to 300 more concurrent invokes per minute. The maximum number of invokes that an event source mapping can process simultaneously is 1,250.")], tier0=True, bullets=["2.1.K5","3.2.S4"], vol="frequently-changing",
  note="d044 expected a ceiling of 1,000 batches; the saved guide page says 1,250 (and 100,000 with provisioned mode).")
f("lambda-sqs-scale-back-to-2", "behavior", "When traffic is low, Lambda scales SQS processing back to five concurrent invokes and can go as low as 2 to reduce SQS calls and cost, unless maximum concurrency is set.",
  "How low does Lambda scale an idle SQS event source mapping?", [("min","as few as 2 concurrent invokes")], "per SQS event source mapping, standard queue", "min", False,
  [ev(SS, "When traffic is low, Lambda scales back the processing to five concurrent invokes, and can optimize to as few as 2 concurrent invokes to reduce the Amazon SQS calls and corresponding costs. However, this optimization is not available when you enable the maximum concurrency setting.")], rel="reference")
f("lambda-sqs-max-concurrency-range", "limit", "The maximum concurrency setting of an SQS event source accepts a number between 2 and 1,000; leaving it empty turns it off.",
  "What range does the SQS event source maximum concurrency setting accept?", [("range","between 2 and 1,000")], "per SQS event source mapping", "max", True,
  [ev(SS, "For **Maximum concurrency**, enter a number between 2 and 1,000.")], tier0=True)
f("lambda-sqs-max-concurrency-no-charge", "pricing-dimension", "There is no charge for configuring maximum concurrency on an Amazon SQS event source.",
  "Does the SQS maximum concurrency setting cost anything?", [("rule","no charge for configuring maximum concurrency")], "per SQS event source mapping", "", False,
  [ev(SS, "There is no charge for configuring maximum concurrency on an Amazon SQS event source.")], bullets=["4.2.S3"], rel="extended")
f("lambda-sqs-max-concurrency-vs-reserved", "behavior", "Maximum concurrency (per SQS event source) and reserved concurrency (per function) are independent; keep reserved concurrency greater than or equal to the total maximum concurrency of all SQS event sources, or Lambda may throttle messages.",
  "How should SQS maximum concurrency relate to the function's reserved concurrency?", [("rule","reserved concurrency is greater than or equal to the total maximum concurrency for all Amazon SQS event sources")], "per function with SQS event sources", "", False,
  [ev(SS, "Don't set maximum concurrency higher than the function's reserved concurrency. If you configure maximum concurrency, make sure that your function's reserved concurrency is greater than or equal to the total maximum concurrency for all Amazon SQS event sources on the function. Otherwise, Lambda might throttle your messages.")], bullets=["2.1.K5","2.2.K10"], rel="extended")
f("lambda-sqs-esm-1250-default-100000-provisioned", "limit", "By default an SQS event source mapping can invoke up to 1,250 concurrent function instances; provisioned mode scales up to 100,000 concurrent invocations.",
  "What is the concurrency ceiling of an SQS event source mapping, with and without provisioned mode?", [("default","up to 1,250 concurrent function instances"),("provisioned","up to 100,000 concurrent function invocations")], "per SQS event source mapping", "max", False,
  [ev(SS, "By default, Lambda can scale to invoke up to 1,250 concurrent function instances for an Amazon SQS event source mapping. If you need higher concurrency, enable provisioned mode, which scales up to 100,000 concurrent function invocations.")], rel="extended", vol="frequently-changing")
f("lambda-sqs-provisioned-mode-poller-capacity", "limit", "In provisioned mode, each SQS event poller handles up to 1 MB/sec, up to 10 concurrent invokes, or up to 10 SQS polling API calls per second, and Lambda adds up to 1,000 concurrency per minute between your minimum and maximum pollers.",
  "What can one SQS event poller handle in provisioned mode?", [("throughput","up to 1 MB/sec of throughput"),("invokes","up to 10 concurrent invokes"),("rate","up to 1,000 concurrency per minute")], "per event poller, SQS provisioned mode", "max", False,
  [ev(SS, "When using provisioned mode, each event poller can handle up to 1 MB/sec of throughput, up to 10 concurrent invokes, or up to 10 Amazon SQS polling API calls per second. Lambda scales the number of event pollers between your configured minimum and maximum, quickly adding up to 1,000 concurrency per minute to provide consistent, low-latency processing of your Amazon SQS events.")], rel="reference", vol="frequently-changing")
f("lambda-sqs-provisioned-mode-3x-16x", "capability", "Provisioned mode for SQS event source mappings gives dedicated pollers with minimum and maximum limits, 3 times faster scaling and up to 16 times higher processing capacity.",
  "What does provisioned mode for an SQS event source mapping buy you?", [("faster","3 times faster scaling"),("capacity","up to 16 times higher processing capacity")], "per SQS event source mapping, provisioned mode", "", False,
  [ev(SS, "Provisioned mode: You configure dedicated polling resources with minimum and maximum limits, enabling 3 times faster scaling and up to 16 times higher processing capacity.")], rel="reference", vol="frequently-changing")
f("lambda-sqs-fifo-concurrency-message-groups", "behavior", "For a FIFO queue, concurrent invocations are capped by the number of message group IDs or the maximum concurrency setting, whichever is lower: six message groups with maximum concurrency 10 give at most six concurrent invocations.",
  "What limits Lambda concurrency on a FIFO SQS queue?", [("example","six message group IDs and maximum concurrency is set to 10, your function can have a maximum of six concurrent invocations")], "per SQS FIFO event source mapping", "max", False,
  [ev(SS, "For example, if you have six message group IDs and maximum concurrency is set to 10, your function can have a maximum of six concurrent invocations.")], rel="extended")
f("lambda-sqs-max-concurrency-provisioned-exclusive", "restriction", "The SQS maximum concurrency setting and provisioned mode cannot be used at the same time.",
  "Can you combine SQS maximum concurrency with provisioned mode?", [("rule","cannot use the maximum concurrency setting and provisioned mode at the same time")], "per SQS event source mapping", "", False,
  [ev(SS, "You cannot use the maximum concurrency setting and provisioned mode at the same time.")], rel="reference")
f("lambda-kinesis-poll-once-per-second", "behavior", "With a standard iterator, Lambda polls each Kinesis shard at a base rate of once per second and shares the shard's read throughput with other consumers.",
  "How often does Lambda poll a Kinesis shard?", [("rate","base rate of once per second")], "per shard, standard iterator", "", False,
  [ev(K, "**Standard iterator:** Lambda polls each shard in your Kinesis stream for records at a base rate of once per second. When more records are available, Lambda keeps processing batches until the function catches up with the stream. The event source mapping shares read throughput with other consumers of the shard.")], rel="extended")
f("lambda-kinesis-batching-window-5-minutes-6-mb", "limit", "A stream event source can buffer records for up to 5 minutes with a batching window; Lambda invokes when the batch is full, the window expires, or the batch reaches the 6 MB payload limit.",
  "How long can a Kinesis event source mapping buffer records, and what ends a batch?", [("window","up to 5 minutes"),("payload","payload limit of 6 MB")], "per event source mapping, Kinesis", "max", True,
  [ev(K, "To avoid invoking the function with a small number of records, you can tell the event source to buffer records for up to 5 minutes by configuring a *batching window*. Before invoking the function, Lambda continues to read records from the event source until it has gathered a full batch, the batching window expires, or the batch reaches the payload limit of 6 MB.")], tier0=True, bullets=["2.1.K5","3.2.S4"])
f("lambda-kinesis-parallelization-factor-1-to-10", "limit", "The parallelization factor sets how many concurrent batches Lambda polls from one Kinesis shard, from 1 (default) to 10; with a factor of 2, 100 shards can drive up to 200 concurrent invocations.",
  "How can one Kinesis shard be processed by more than one Lambda invocation at a time?", [("range","from 1 (default) to 10"),("example","200 concurrent Lambda invocations at maximum to process 100 Kinesis data shards")], "per Kinesis event source mapping, per shard", "default", True,
  [ev(K, "You can specify the number of concurrent batches that Lambda polls from a shard by using a parallelization factor from 1 (default) to 10. For example, when you set `ParallelizationFactor` to 2, you can have 200 concurrent Lambda invocations at maximum to process 100 Kinesis data shards (though in practice, you might see different values for the `ConcurrentExecutions` metric).")], tier0=True, bullets=["2.1.K5","3.2.S4"])
f("lambda-kinesis-in-order-stops-on-error", "behavior", "Lambda processes the records of each Kinesis shard in order and stops processing further records in that shard if the function returns an error; more shards mean more batches in parallel and less impact from errors.",
  "What happens to a Kinesis shard when the Lambda function returns an error?", [("rule","stops processing additional records in a shard if your function returns an error")], "per shard, Kinesis event source mapping", "", False,
  [ev(K, "Lambda processes records in each shard in order. It stops processing additional records in a shard if your function returns an error. With more shards, there are more batches being processed at once, which lowers the impact of errors on concurrency.")])
f("lambda-esm-at-least-once", "behavior", "Event source mappings process each event at least once, so duplicates can occur and function code should be idempotent.",
  "Can a Lambda event source mapping deliver the same record twice?", [("rule","process each event at least once, and duplicate processing of records can occur")], "event source mappings", "", False,
  [ev(K, "Lambda event source mappings process each event at least once, and duplicate processing of records can occur. To avoid potential issues related to duplicate events, we strongly recommend that you make your function code idempotent.")])
f("lambda-async-default-two-retries", "default", "For an asynchronous invocation that returns an error, Lambda by default tries two more times, waiting one minute before the second attempt and two minutes before the third.",
  "How many times does Lambda retry a failed asynchronous invocation by default, and with what waits?", [("retries","two more times"),("waits","one-minute wait between the first two attempts, and two minutes between the second and third attempts")], "per function, asynchronous invocation", "default", True,
  [ev(AE, "If the function returns an error, by default Lambda attempts to run it two more times, with a one-minute wait between the first two attempts, and two minutes between the second and third attempts.")], tier0=True)
f("lambda-async-throttle-retry-6-hours", "default", "For throttling errors (429) and system errors (500-series) on asynchronous invocations, Lambda returns the event to the queue and keeps retrying for up to 6 hours by default, with the interval growing from 1 second to a maximum of 5 minutes.",
  "How long does Lambda keep retrying a throttled asynchronous event?", [("max","up to 6 hours by default"),("backoff","from 1 second after the first attempt to a maximum of 5 minutes")], "per function, asynchronous invocation", "default", True,
  [ev(AE, "For throttling errors (429) and system errors (500-series), Lambda returns the event to the queue and attempts to run the function again for up to 6 hours by default. The retry interval increases exponentially from 1 second after the first attempt to a maximum of 5 minutes.")], tier0=True)
f("lambda-async-queue-eventually-consistent", "behavior", "Because the asynchronous event queue is eventually consistent, a function can receive the same event more than once even without errors, so handle duplicates gracefully.",
  "Why can an asynchronous Lambda event be delivered twice?", [("rule","the queue itself is eventually consistent")], "asynchronous invocation", "", False,
  [ev(AE, "Even if your function doesn't return an error, it's possible for it to receive the same event from Lambda multiple times because the queue itself is eventually consistent.")], rel="extended")
f("lambda-managed-instances-three-instances-default", "default", "When a function version is published to a capacity provider, Lambda launches three Managed Instances by default for AZ resiliency and starts three execution environments before marking the version ACTIVE.",
  "How many instances does Lambda Managed Instances launch by default?", [("count","three instances by default")], "per capacity provider, Lambda Managed Instances", "default", True,
  [ev(MI, "It launches three instances by default for AZ resiliency and starts three execution environments before marking your function version ACTIVE.")], rel="reference", vol="frequently-changing", note="Not examinable yet: GA after 2026-07-15.")
f("lambda-managed-instances-doubling-five-minutes", "default", "Lambda Managed Instances scale to handle traffic doubling within five minutes by default.",
  "How fast do Lambda Managed Instances scale by default?", [("rule","traffic doubling within five minutes by default")], "Lambda Managed Instances", "default", True,
  [ev(MI, "Lambda Managed Instances scale to handle traffic doubling within five minutes by default.")], rel="reference", vol="frequently-changing", note="Not examinable yet: GA after 2026-07-15.")
json.dump(F, open("aws-saa-book/_build/work/18-lambda/facts/n06-esm.json","w"), indent=1)
# adopt files for SQS parameters table
D="aws-saa-book/_build/work/18-lambda/facts/adopt/"
base={"service":"lambda","home_chapter":"18","source_tier":1,"hard":True,"tier0":False,"volatility":"stable","changed":None,"exam_relevance":"core"}
def a(id, kind, claim, q, values, scope, dom, adj, cond="", tier0=False, bullets=None, rel="core", tier=1, note=None):
    d=dict(base); d.update({"id":id,"kind":kind,"claim":claim,"question":q,"values":[{"key":k,"display":v} for k,v in values],
      "qualifiers":{"scope":scope,"default_or_max":dom,"adjustable":adj,"condition":cond},"tier0":tier0,"bullets":bullets or ["2.1.K5"],"exam_relevance":rel,"source_tier":tier})
    if note: d["note"]=note
    json.dump(d,open(D+id+".json","w"),indent=1)
a("lambda-sqs-batch-size", "default", "The SQS event source batch size defaults to 10; the maximum is 10,000 for standard queues and 10 for FIFO queues.",
  "What is the default and maximum batch size for an SQS event source mapping?", [("default","10"),("standard-max","10,000"),("fifo-max","10")], "per SQS event source mapping", "default", True, tier0=True, bullets=["2.1.K5","3.2.S4"])
a("lambda-sqs-batching-window-default", "default", "MaximumBatchingWindowInSeconds defaults to 0 for an SQS event source mapping, and a batching window is not supported for FIFO queues.",
  "What is the default batching window for an SQS event source, and does it work with FIFO queues?", [("default","0"),("fifo","not supported for FIFO queues")], "per SQS event source mapping", "default", True, rel="extended")
a("lambda-sqs-provisioned-poller-config", "limit", "ProvisionedPollerConfig sets the minimum (2-200) and maximum (2-2000) dedicated event pollers for an SQS event source mapping; each poller handles up to 1 MB/sec and 10 concurrent invokes.",
  "What are the ranges for provisioned pollers on an SQS event source mapping?", [("min","2-200"),("max","2-2000"),("per-poller","1 MB/sec of throughput and 10 concurrent invokes")], "per SQS event source mapping, provisioned mode", "max", True, rel="reference")
a("lambda-fargate-cpu-ceilings", "limit", "Lambda CPU is proportional to memory, up to 6 vCPU, while Fargate offers up to 32 vCPU.",
  "What is the maximum CPU of a Lambda function compared with Fargate?", [("lambda","up to 6 vCPU"),("fargate","Up to 32 vCPU")], "per function (Lambda) and per task (Fargate)", "max", False, bullets=["3.2.S4"], rel="extended", tier=2)
a("lambda-fargate-memory-ceilings", "limit", "Lambda memory goes up to 10 GiB, while Fargate tasks go up to 244 GiB.",
  "What is the maximum memory of a Lambda function compared with a Fargate task?", [("lambda","Up to 10 GiB"),("fargate","Up to 244 GiB")], "per function (Lambda) and per task (Fargate)", "max", False, bullets=["3.2.S4"], rel="extended", tier=2)
a("lambda-fargate-execution-time", "limit", "A Lambda invocation is limited to 15 minutes, while Fargate has no hard execution time limit.",
  "Which compute option has no execution time limit, Lambda or Fargate?", [("lambda","15 minutes per invocation"),("fargate","No hard limit")], "per invocation (Lambda) and per task (Fargate)", "max", False, bullets=["3.2.S4","2.1.S5"], rel="core", tier=2)
a("lambda-fargate-package-size", "limit", "Lambda packages are limited to 250 MB unzipped including layers, or 10 GB for container images; Fargate has no specific package limit beyond its configured ephemeral storage of up to 200 GiB.",
  "How do Lambda and Fargate package size limits compare?", [("lambda","250 MB unzipped, including layers, 10 GB for container image deployments"),("fargate","200 GiB maximum")], "per function (Lambda) and per task (Fargate)", "max", False, bullets=["3.2.S4"], rel="extended", tier=2)
a("lambda-console-editor-3-mb", "limit", "The Lambda console editor accepts a deployment package or layer archive of up to 3 Megabytes; larger files go through Amazon S3.",
  "What is the size limit for code edited in the Lambda console editor?", [("max","3 Megabytes")], "per deployment package, console editor upload", "max", False, bullets=["3.2.S4"], rel="reference")
print(len(F))
