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
C="docs/lambda/latest/dg/lambda-concurrency"; CC="docs/lambda/latest/dg/configuration-concurrency"; SB="docs/lambda/latest/dg/scaling-behavior"
A="docs/lambda/latest/dg/invocation-async-configuring"; RS="docs/lambda/latest/dg/configuration-response-streaming"; L="docs/lambda/latest/dg/adding-layers"
f("lambda-concurrency-formula", "behavior", "Concurrency is estimated by multiplying average requests per second by the average request duration in seconds.",
  "How do you calculate the concurrency a Lambda function needs?", [("formula","average requests per second with the average request duration in seconds")], "per function", "", False,
  [ev(CC, "Multiplying average requests per second with the average request duration in seconds gives you a rough estimate of how much concurrency you need to reserve.")], tier0=True, bullets=["3.2.S4","2.2.K10"])
f("lambda-concurrency-example-100-rps-500-ms", "behavior", "At an average duration of 500 ms, one instance handles two requests per second, so a load of 100 requests per second needs 50 instances, that is, a concurrency of 50.",
  "What concurrency does 100 requests per second at 500 ms average duration need?", [("example","50 instances of your function to handle a load of 100 requests per second")], "per function", "", False,
  [ev(C, "What does a concurrency of 50 mean in practice? If the average request duration is 500 ms, then you can think of an instance of your function as being able to handle two requests per second. Then, it takes 50 instances of your function to handle a load of 100 requests per second.")], rel="extended")
f("lambda-unreserved-concurrency-100-always", "limit", "Regardless of the account concurrency limit, Lambda always keeps 100 units of concurrency for functions that do not reserve concurrency; with a limit of 2,000 you can reserve up to 1,900 units at the function level.",
  "Can you reserve all of an account's Lambda concurrency for specific functions?", [("kept","100 units of concurrency"),("example","reserve up to 1,900 units")], "per account, per Region", "fixed", False,
  [ev(C, "Regardless of your total account concurrency limit, Lambda always reserves 100 units of concurrency for your functions that don't explicitly reserve concurrency. For example, if you increased your account concurrency limit to 2,000, then you can reserve up to 1,900 units of concurrency at the function level.")], tier0=True, bullets=["2.2.K10"])
f("lambda-reserve-up-to-900-default", "limit", "At the function level, you can reserve up to 900 units of concurrency across all your functions by default.",
  "How much concurrency can be reserved across functions in an account with the default quota?", [("max","up to 900 units of concurrency")], "per account, per Region, function-level reserved concurrency", "default", True,
  [ev(C, "you can reserve up to 900 units of concurrency across all your functions by default")], bullets=["2.2.K10"], rel="extended")
f("lambda-reserve-not-all-1000", "restriction", "With an account concurrency limit of 1,000 you cannot reserve all 1,000 units for a single function; the remaining 100 units stay for functions without reserved concurrency.",
  "Why does the console refuse a reserved concurrency of 1,000 on a default account?", [("kept","remaining 100 units"),("rule","cannot reserve all 1,000 units of concurrency to a single function")], "per account, per Region", "max", False,
  [ev(CC, "The remaining 100 units of concurrency are for functions that aren't using reserved concurrency. For example, if your account has a concurrency limit of 1,000, you cannot reserve all 1,000 units of concurrency to a single function.")], bullets=["2.2.K10"])
f("lambda-reserved-concurrency-zero-throttles", "behavior", "Setting a function's reserved concurrency to 0 throttles it on purpose: it stops processing any events until the limit is removed.",
  "How do you stop a Lambda function from processing events without deleting it?", [("rule","set its reserved concurrency to 0")], "per function", "", True,
  [ev(CC, "To intentionally throttle a function, set its reserved concurrency to 0. This stops your function from processing any events until you remove the limit.")], bullets=["2.2.K10","2.1.K5"])
f("lambda-reserved-concurrency-no-charge", "pricing-dimension", "Configuring reserved concurrency for a function incurs no additional charges.",
  "Does reserved concurrency cost money?", [("rule","incurs no additional charges")], "per function, reserved concurrency", "", False,
  [ev(CC, "Configuring reserved concurrency for a function incurs no additional charges.")], bullets=["4.2.S3"])
f("lambda-provisioned-concurrency-charges", "pricing-dimension", "Configuring provisioned concurrency incurs additional charges to your AWS account.",
  "Does provisioned concurrency cost money?", [("rule","incurs additional charges to your AWS account")], "per function, provisioned concurrency", "", False,
  [ev(C, "Both reserved concurrency and provisioned concurrency count towards your account concurrency limit and [Regional quotas](gettingstarted-limits.md). In other words, allocating reserved and provisioned concurrency can impact the concurrency pool that's available to other functions. Configuring provisioned concurrency incurs charges to your AWS account.")], bullets=["4.2.S3"])
f("lambda-provisioned-not-above-reserved", "restriction", "You cannot allocate more provisioned concurrency than reserved concurrency for a function.",
  "Can provisioned concurrency exceed a function's reserved concurrency?", [("rule","can't allocate more provisioned concurrency than reserved concurrency")], "per function", "max", False,
  [ev(C, "You can't allocate more provisioned concurrency than reserved concurrency for a function.")], bullets=["2.2.K10"], rel="extended")
f("lambda-provisioned-concurrency-allocation-rate", "limit", "Provisioned concurrency does not come online immediately: Lambda starts allocating it after a minute or two, and for each function it can provision up to 6,000 execution environments every minute.",
  "How fast does Lambda allocate provisioned concurrency after you configure it?", [("rate","up to 6,000 execution environments every minute")], "per function", "max", False,
  [ev(C, "Provisioned concurrency doesn't come online immediately after you configure it. Lambda starts allocating provisioned concurrency after a minute or two of preparation. For each function, Lambda can provision up to 6,000 execution environments every minute, regardless of AWS Region.")], rel="extended")
f("lambda-rps-limit-10x-concurrency-quota", "limit", "At both the account level and the function level, Lambda enforces a requests-per-second limit equal to 10 times the corresponding concurrency quota.",
  "What is the requests-per-second limit tied to a Lambda concurrency quota?", [("rule","10 times the corresponding concurrency quota")], "per account and per function, per Region", "max", False,
  [ev(C, "At both the account level and the function level, Lambda also enforces a requests per second limit of equal to 10 times the corresponding concurrency quota.")], bullets=["2.2.K10"], rel="extended")
f("lambda-scaling-rate-10000-rps", "limit", "Every 10 seconds, Lambda can add at most 1,000 execution environment instances, or 10,000 additional requests per second, to each function.",
  "What is the per-function concurrency scaling rate in environments and in requests per second?", [("envs","1,000 additional execution environment instances"),("rps","10,000 additional requests per second")], "per function, per Region", "max", False,
  [ev(SB, "every 10 seconds, Lambda can allocate at most 1,000 additional execution environment instances, or accommodate 10,000 additional requests per second, to each of your functions.")], bullets=["2.2.K10"], rel="extended", vol="frequently-changing")
f("lambda-scaling-rate-not-accrued", "behavior", "Unused scaling capacity does not accumulate: at any instant the scaling rate is at most 1,000 concurrency units.",
  "If a function does not scale for a while, can it burst by more than 1,000 later?", [("rule","always 1,000 concurrency units at maximum")], "per function", "max", False,
  [ev(SB, "Lambda doesn't accrue unused portions of your concurrency scaling rate. This means that at any instant in time, your scaling rate is always 1,000 concurrency units at maximum.")], rel="reference")
f("lambda-throttle-429", "behavior", "When requests arrive faster than the function can scale, or the function is at maximum concurrency, additional requests fail with a throttling error (429 status code).",
  "What error does a throttled Lambda invocation return?", [("error","throttling error (429 status code)")], "per function", "", False,
  [ev(SB, "If requests come in faster than your function can scale, or if your function is at maximum concurrency, then additional requests fail with a throttling error (429 status code).")], tier0=True, bullets=["2.2.K10","2.1.K5"])
f("lambda-async-max-event-age-6-hours", "limit", "The maximum age of an asynchronous event, the time Lambda keeps it in the asynchronous event queue, can be set up to 6 hours.",
  "How long can Lambda keep an asynchronous event in its queue before discarding it?", [("max","up to 6 hours")], "per function, version or alias; asynchronous invocation", "max", True,
  [ev(A, "The maximum amount of time Lambda retains an event in the asynchronous event queue, up to 6 hours.")], bullets=["2.1.K5"],
  note="d039 asks for the lower bound (60 seconds) and the default (6 hours); this page states only the 6-hour maximum. Minimum and default not found on the saved configuring page.")
f("lambda-async-retry-attempts-0-to-2", "limit", "The number of retries for an asynchronous invocation that returns an error can be set between 0 and 2.",
  "How many times can Lambda retry a failed asynchronous invocation?", [("range","between 0 and 2")], "per function, version or alias; asynchronous invocation", "max", True,
  [ev(A, "The number of times Lambda retries when the function returns an error, between 0 and 2.")], tier0=True, bullets=["2.1.K5"],
  note="The Lambda FAQ says asynchronous invocations are 'retried at least 3 times'; the guide's 0 to 2 retries (that is, up to three attempts) is current truth.")
f("lambda-async-discard-then-destination", "behavior", "When an asynchronous event exceeds its maximum age or fails all retry attempts, Lambda discards it; a failed-event destination keeps a copy.",
  "What happens to an asynchronous Lambda event after all retries fail?", [("rule","Lambda discards it"),("keep","configure a failed-event destination")], "asynchronous invocation", "", False,
  [ev(A, "When an invocation event exceeds the maximum age or fails all retry attempts, Lambda discards it. To retain a copy of discarded events, configure a failed-event [destination](invocation-async-retain-records.md#invocation-async-destinations).")], bullets=["2.1.K5"])
f("lambda-streaming-200-mb-vs-6-mb", "limit", "Response streaming functions can return payloads up to 200 MB, compared with the 6 MB maximum for buffered responses.",
  "How much larger can a streamed Lambda response be than a buffered one?", [("streamed","up to 200 MB"),("buffered","6 MB maximum")], "per invocation, response payload", "max", False,
  [ev(RS, "Additionally, response streaming functions can return payloads up to 200 MB, compared to the 6 MB maximum for buffered responses.")], bullets=["2.1.S1","3.2.S4"], rel="extended")
f("lambda-streaming-paths", "capability", "A function can stream its response through a Lambda function URL, through the InvokeWithResponseStream API, or through the API Gateway proxy integration that uses that API.",
  "Which invocation paths support Lambda response streaming?", [("paths","Lambda function URLs or by using the InvokeWithResponseStream API")], "response streaming", "", False,
  [ev(RS, "Lambda functions can natively stream response payloads back to clients through [Lambda function URLs](urls-configuration.md) or by using the [InvokeWithResponseStream](https://docs.aws.amazon.com/lambda/latest/api/API_InvokeWithResponseStream.html) API (through the AWS SDK or direct API calls).")], bullets=["2.1.S1"], rel="extended", hard=False)
f("lambda-streaming-bandwidth-2-mbps", "limit", "The first 6 MB of a streamed response has uncapped bandwidth; after that Lambda streams at a maximum of 2 MBps, and responses that never exceed 6 MB never hit the cap.",
  "What bandwidth cap applies to a Lambda streamed response?", [("cap","maximum rate of 2 MBps"),("free","first 6 MB")], "per invocation, streamed response payload", "max", False,
  [ev(RS, "The first 6 MB of your function's response payload has uncapped bandwidth. After this initial burst, Lambda streams your response at a maximum rate of 2 MBps. If your function responses never exceed 6 MB, then this bandwidth limit never applies.")], bullets=["2.1.S1"], rel="extended")
f("lambda-streaming-nodejs-managed-runtimes", "restriction", "Lambda supports response streaming natively on Node.js managed runtimes; other languages need a custom runtime or the Lambda Web Adapter.",
  "Which managed runtimes support Lambda response streaming?", [("runtimes","Node.js managed runtimes")], "response streaming", "", False,
  [ev(RS, "Lambda supports response streaming on Node.js managed runtimes. For other languages, including Python, you can [use a custom runtime with a custom Runtime API integration](runtimes-custom.md#runtimes-custom-response-streaming) to stream responses or use the [Lambda Web Adapter](https://github.com/awslabs/aws-lambda-web-adapter).")], bullets=["2.1.S1"], rel="reference")
f("lambda-streaming-furl-not-in-vpc", "restriction", "Lambda function URLs do not support response streaming within a VPC environment.",
  "Can a function URL stream a response inside a VPC?", [("rule","do not support response streaming within a VPC environment")], "function URLs in a VPC", "", False,
  [ev(RS, "Lambda function URLs do not support response streaming within a VPC environment.")], rel="reference")
f("lambda-layers-five-and-250-mb", "limit", "A function can use up to five layers, and the unzipped size of the function plus all its layers cannot exceed the 250 MB unzipped deployment package quota.",
  "How many layers can a function have, and do layers get extra space?", [("count","up to five layers"),("total","250 MB")], "per function, layers", "max", False,
  [ev(L, "You can add up to five layers to a Lambda function. The total unzipped size of the function and all layers cannot exceed the unzipped deployment package size quota of 250 MB.")], tier0=True)
f("lambda-mq-default-concurrency", "default", "Functions linked to an Amazon MQ event source mapping have a default maximum concurrency of 5 concurrent instances for Apache ActiveMQ and 1 for RabbitMQ; reserved or provisioned concurrency does not change this.",
  "What is the default concurrency for a Lambda function triggered by Amazon MQ?", [("activemq","5"),("rabbitmq","1")], "per function with an Amazon MQ event source mapping", "default", True,
  [ev(CC, "Lambda functions linked to an Amazon MQ event source mapping have a default maximum concurrency. For Apache Active MQ, the maximum number of concurrent instances is 5. For Rabbit MQ, the maximum number of concurrent instances is 1. Setting reserved or provisioned concurrency for your function doesn't change these limits.")], cond="increase by contacting Support", rel="reference")
json.dump(F, open("aws-saa-book/_build/work/18-lambda/facts/n03-concurrency.json","w"), indent=1)
print(len(F))
