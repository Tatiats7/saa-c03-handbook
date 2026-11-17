import json
F=[]
P="www/lambda/pricing"
def ev(src, quote, th=None):
    return {"source_id": src, "url": "https://aws.amazon.com/lambda/pricing/", "quote": quote, "table_header": th}
def f(id, kind, claim, question, values, scope, dom, adj, quote, cond="", tier0=False, bullets=None, rel="core", vol="frequently-changing", tier=2, hard=True, note=None):
    d={"id": id, "service": "lambda", "home_chapter": "18", "kind": kind, "claim": claim, "question": question,
       "values": [{"key": k, "display": v} for k, v in values],
       "qualifiers": {"scope": scope, "default_or_max": dom, "adjustable": adj, "condition": cond},
       "evidence": [ev(P, quote)], "source_tier": tier, "hard": hard, "tier0": tier0, "volatility": vol, "changed": None,
       "exam_relevance": rel, "bullets": bullets or ["4.2.S3"]}
    if note: d["note"]=note
    F.append(d)
f("lambda-pricing-dimensions", "pricing-dimension", "Lambda functions are priced on the number of requests and on duration measured in GB-seconds; you choose the memory and get proportional CPU.",
  "What are the two pricing dimensions of a Lambda function?", [("dims","number of requests served and the duration your code runs, measured in GB-seconds")], "Lambda functions", "", False,
  "Lambda Functions are priced based on the number of requests served and the duration your code runs, measured in GB-seconds. You choose the memory allocated to your function and get proportional CPU and resources.", tier0=True, vol="stable")
f("lambda-free-tier", "price", "The Lambda free tier includes one million requests and 400,000 GB-seconds per month.",
  "What does the Lambda free tier include?", [("requests","one million requests"),("duration","400,000 GB-seconds per month")], "per account, per month", "", False,
  "The free tier includes one million requests and 400,000 GB-seconds per month.", tier0=True)
f("lambda-price-per-million-requests", "price", "The request price is $0.20 per one million requests (pricing-page example, US East (N. Virginia)).",
  "What does Lambda charge per million requests?", [("price","$0.20 per one million requests")], "per request, on-demand functions", "", False,
  "The monthly request price is $0.20 per one million requests and the free tier provides 1 million requests per month.", cond="pricing-page example priced in US East (N. Virginia)")
f("lambda-price-per-gb-second", "price", "In the pricing-page examples for US East (N. Virginia), the on-demand compute price is $0.0000166667 per GB-s, with 400,000 GB-s free per month.",
  "What does Lambda charge per GB-second of duration?", [("price","$0.0000166667 per GB-s")], "per GB-second, on-demand functions, first pricing tier", "", False,
  "The monthly compute price is $0.0000166667 per GB-s and the free tier provides 400,000 GB-s.", cond="pricing-page example priced in US East (N. Virginia), x86 architecture, first tier", rel="extended")
f("lambda-async-event-request-billing", "pricing-dimension", "An asynchronous event is billed as 1 request for its first 256 KB, plus 1 additional request for each 64 KB beyond that, up to 1 MB.",
  "How are large asynchronous events billed after the payload limit rose to 1 MB?", [("first","1 request per each asynchronous Event for first 256 KB"),("extra","1 additional request for each 64 KB")], "per asynchronous event", "", False,
  "You are charged for 1 request per each asynchronous Event for first 256 KB. Individual event size beyond 256 KB is charged 1 additional request for each 64 KB of chunk upto 1 MB.", rel="extended")
f("lambda-duration-rounded-1-ms", "pricing-dimension", "Duration is billed from when the code starts executing until it returns or terminates, rounded up to the nearest 1ms.",
  "What is the billing granularity of Lambda duration?", [("rule","rounded up to the nearest 1ms")], "per invocation", "", False,
  "Duration is calculated from the time your code begins executing until it returns or otherwise terminates, rounded up to the nearest 1ms", tier0=True, vol="stable")
f("lambda-duration-includes-init-code", "pricing-dimension", "Duration charges cover the handler code and the initialization code declared outside the handler; with extensions, duration also includes the last running extension's shutdown time.",
  "Is Lambda initialization code billed?", [("rule","initialization code that is declared outside of the handler")], "per invocation", "", False,
  "Duration charges apply to code that runs in the handler of a function as well as initialization code that is declared outside of the handler. For Lambda functions with AWS Lambda Extensions, duration also includes the time it takes for code in the last running extension to finish executing during shutdown phase.", rel="extended", vol="stable")
f("lambda-pricing-first-tier-6-billion", "pricing-dimension", "The first on-demand duration pricing tier covers up to 6 billion GB-seconds per month (example: US East (Ohio)).",
  "Where does the first Lambda duration pricing tier end?", [("tier","up to 6 billion GB-seconds / month")], "per account, per architecture, per Region, per month", "max", False,
  "The table below contains a few examples of the price per 1 ms associated with different memory sizes, for usage falling within the first pricing tier – for example, up to 6 billion GB-seconds / month in US East (Ohio)", rel="extended")
f("lambda-pricing-tiers-aggregate", "pricing-dimension", "Duration pricing tiers apply to the aggregate monthly duration of functions on the same architecture in the same Region within the account, or across the organization's accounts with consolidated billing.",
  "How are Lambda duration pricing tiers aggregated?", [("rule","same architecture (x86 or Arm, respectively), in the same region, within the account"),("org","across the accounts in the organization")], "per architecture, per Region", "", False,
  "Lambda on-demand duration pricing tiers are applied to aggregate monthly duration of your functions running on the same architecture (x86 or Arm, respectively), in the same region, within the account. If you’re using consolidated billing in AWS Organizations, pricing tiers are applied to the aggregate monthly duration of your functions running on the same architecture, in the same region, across the accounts in the organization.", rel="extended")
f("lambda-pc-pricing-dimensions", "pricing-dimension", "With provisioned concurrency you pay for the concurrency configured and the period it is configured, plus requests and duration when the function runs.",
  "What do you pay for with Lambda provisioned concurrency?", [("rule","amount of concurrency you configure, and for the period of time you configure it")], "per function, provisioned concurrency", "", False,
  "You pay for the amount of concurrency you configure, and for the period of time you configure it. When Provisioned Concurrency is enabled and executed for your function, you also pay for Requests and Duration based on the prices below.", tier0=True, vol="stable")
f("lambda-pc-rounded-5-minutes", "pricing-dimension", "Provisioned concurrency is billed from the time it is enabled until disabled, rounded up to the nearest five minutes; the price depends on memory and the configured concurrency.",
  "What is the billing granularity of provisioned concurrency?", [("rule","rounded up to the nearest five minutes")], "per function, provisioned concurrency", "", False,
  "Provisioned Concurrency is calculated from the time you enable it on your function until it is disabled, rounded up to the nearest five minutes. The price depends on the amount of memory you allocate to your function and the amount of concurrency that you configure on it.", vol="stable")
f("lambda-pc-no-free-tier", "restriction", "The Lambda free tier does not apply to functions that enable provisioned concurrency.",
  "Does the free tier cover functions with provisioned concurrency?", [("rule","free tier does not apply to functions enabling Provisioned Concurrency")], "per function, provisioned concurrency", "", False,
  "The Lambda free tier does not apply to functions enabling Provisioned Concurrency.", vol="stable")
f("lambda-pc-excess-at-on-demand-rate", "pricing-dimension", "If a function exceeds its configured provisioned concurrency, the excess executions are billed at the on-demand Lambda rate.",
  "What happens to the bill when traffic exceeds the provisioned concurrency?", [("rule","billed for excess function execution at the rate outlined in the AWS Lambda Pricing section above")], "per function, provisioned concurrency", "", False,
  "If your function exceeds the configured concurrency, you will be billed for excess function execution at the rate outlined in the AWS Lambda Pricing section above.", rel="extended", vol="stable")
f("lambda-pc-price-per-gb-second", "price", "In the pricing-page examples (US East (N. Virginia)), provisioned concurrency costs $0.0000041667 per GB-s, and compute while provisioned concurrency is enabled costs $0.0000097222 per GB-s.",
  "What does provisioned concurrency cost per GB-second?", [("pc","$0.0000041667 per GB-s"),("compute","$0.0000097222 per GB-s")], "per GB-second, provisioned concurrency", "", False,
  "The Provisioned Concurrency price is $0.0000041667 per GB-s\nTotal period of time for which Provisioned Concurrency is enabled (seconds): 8 hours * 3,600 seconds = 28,800 seconds", cond="pricing-page example priced in US East (N. Virginia)", rel="reference",
  note="Second price: the pricing page states 'The compute price is $0.0000097222 per GB-s' in the same example.")
f("lambda-ephemeral-storage-512-mb-free", "pricing-dimension", "512 MB of ephemeral storage comes with every function at no additional cost; you pay only for additional ephemeral storage you configure, by duration.",
  "How is Lambda ephemeral storage above 512 MB billed?", [("free","512 MB of ephemeral storage is available to each Lambda function at no additional cost")], "per function, /tmp ephemeral storage", "default", True,
  "512 MB of ephemeral storage is available to each Lambda function at no additional cost. You only pay for the additional ephemeral storage you configure.", vol="stable")
f("lambda-ephemeral-storage-price", "price", "In the pricing-page example (US East (N. Virginia)), ephemeral storage above the free 512 MB costs $0.0000000309 per GB-second.",
  "What does extra Lambda ephemeral storage cost?", [("price","$0.0000000309 for every GB-second")], "per GB-second of ephemeral storage above 512 MB", "", False,
  "The monthly ephemeral storage price is $0.0000000309 for every GB-second and Lambda provides 512 MB of storage at no additional cost.", cond="pricing-page example priced in US East (N. Virginia)", rel="reference")
f("lambda-managed-instances-pricing-components", "pricing-dimension", "Lambda Managed Instances pricing has three parts: $0.20 per million requests, a 15% management fee on the EC2 On-Demand instance price, and standard EC2 instance charges.",
  "What are the three charges for Lambda Managed Instances?", [("requests","$0.20 per million requests"),("fee","15% premium on the EC2 on-demand instance price")], "Lambda Managed Instances", "", False,
  "Request charges: $0.20 per million requests\n2. Compute management fee: 15% premium on the EC2 on-demand instance price for the instances provisioned and managed by Lambda (Premium for each instance type provided below)\n3. EC2 instance charges: Standard EC2 instance pricing applies for the instances provisioned in your capacity provider.", rel="reference",
  note="Not examinable yet: Lambda Managed Instances is GA after 2026-07-15.")
f("lambda-managed-instances-no-duration-charge", "pricing-dimension", "Lambda Managed Instances functions do not pay separately for the execution duration of each request, unlike default Lambda functions.",
  "Do Lambda Managed Instances functions pay per-request duration?", [("rule","will not be paying separately for the execution duration of each request")], "Lambda Managed Instances", "", False,
  "Note that Lambda Managed Instances functions will not be paying separately for the execution duration of each request unlike Lambda (default) compute type functions.", rel="reference", note="Not examinable yet: GA after 2026-07-15.")
f("lambda-managed-instances-savings-plans", "capability", "Lambda Managed Instances can use EC2 pricing options including EC2 Instance Savings Plans, Compute Savings Plans and Reserved Instances.",
  "Do Savings Plans apply to Lambda Managed Instances?", [("rule","EC2 Instance Savings Plans, Compute Savings Plans and Reserved Instances")], "Lambda Managed Instances", "", False,
  "With Lambda Managed Instances, you can select from a wide variety of current-generation EC2 instance type to match your workload requirements, benefit from EC2 pricing options including EC2 Instance Savings Plans, Compute Savings Plans and Reserved Instances, and process multiple requests concurrently within the same execution environment to maximize resource utilization.", rel="reference", hard=False, note="Not examinable yet: GA after 2026-07-15.")
f("lambda-data-transfer-free-same-region", "pricing-dimension", "Data transfer between Lambda and S3, DynamoDB, SQS, SNS, Kinesis, ECR, EFS, SES and SimpleDB is free within the same Region.",
  "Which services have free data transfer with Lambda in the same Region?", [("rule","free in the same AWS Region between the following services")], "data transfer, same Region", "", False,
  "Data transfer with AWS Lambda Functions is free in the same AWS Region between the following services: Amazon Simple Storage Service (S3), Amazon Glacier, Amazon DynamoDB, Amazon Simple Email Service (SES), Amazon Simple Queue Service (SQS), Amazon Kinesis, Amazon Elastic Container Registry (ECR), Amazon Simple Notification Service (SNS), Amazon Elastic File System (EFS), and Amazon SimpleDB.", rel="extended", vol="stable")
f("lambda-data-transfer-ec2-rates", "pricing-dimension", "Data transferred in to and out of Lambda functions from outside the Region is charged at Amazon EC2 data transfer rates.",
  "How is Lambda data transfer across Regions or to the internet charged?", [("rule","charged at the Amazon EC2 data transfer rates")], "data transfer from outside the Region", "", False,
  "Data transferred “in” to and “out” of your AWS Lambda functions, from outside the region the function executed, will be charged at the Amazon EC2 data transfer rates as listed under \"Data transfer\".", rel="extended", vol="stable")
f("lambda-vpc-additional-charges", "pricing-dimension", "Using a VPC or VPC peering with Lambda functions incurs additional charges as explained on the EC2 On-Demand pricing page.",
  "Does attaching a Lambda function to a VPC add charges?", [("rule","will incur additional charges as explained on the Amazon Elastic Compute Cloud (EC2) on-demand pricing page")], "functions attached to a VPC", "", False,
  "The usage of Amazon Virtual Private Cloud (VPC) or VPC peering, with AWS Lambda functions will incur additional charges as explained on the Amazon Elastic Compute Cloud (EC2) on-demand pricing page.", rel="extended", vol="stable")
f("lambda-epu-pricing", "price", "Provisioned mode for event source mappings is billed in event poller units (EPUs) at $0.185 per hour, each supporting 10 event pollers.",
  "How is provisioned mode for an event source mapping billed?", [("price","$0.185/hour"),("per-epu","10 event pollers per EPU")], "per EPU-hour, provisioned mode event source mappings", "", False,
  "EPU-hours price is $0.185/hour and supports 10 event pollers per EPU.", rel="reference")
f("lambda-snapstart-pricing", "pricing-dimension", "SnapStart charges for caching a snapshot while the function version is active, for a minimum of 3 hours and per millisecond after that, plus a charge per restore; SnapStart pricing does not apply to supported Java managed runtimes.",
  "What does SnapStart cost, and for which runtime is it free?", [("min","minimum of 3 hours"),("java","does not apply to supported Java managed runtimes")], "per function version with SnapStart", "", False,
  "You are charged for caching a snapshot over the period that your function version is active, for a minimum of 3 hours and per millisecond thereafter. The price depends on the amount of memory you allocate to your function. You are also charged each time Lambda resumes an execution environment by restoring your snapshot, with the price depending on the amount of memory you allocate to your function.\nSnapStart pricing does not apply to supported Java managed runtimes.", rel="extended")
f("lambda-edge-request-price", "price", "Lambda@Edge requests cost $0.60 per 1 million requests, metered at 1ms granularity.",
  "What does Lambda@Edge charge per million requests?", [("price","$0.60 per 1 million requests")], "Lambda@Edge, per request", "", False,
  "The monthly request price is $0.60 per 1 million requests..", rel="reference", note="Granularity sentence on the same page: 'Lambda@Edge functions are metered at a granularity of 1ms'.")
json.dump(F, open("aws-saa-book/_build/work/18-lambda/facts/n04-pricing.json","w"), indent=1)
print(len(F))
