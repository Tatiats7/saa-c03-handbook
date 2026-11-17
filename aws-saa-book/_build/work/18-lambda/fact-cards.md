facts card: 436 facts
lambda-account-rps-10000-default
  claim: Across all functions in an account, Lambda enforces a requests-per-second limit of 10 times the account concurrency, so with the default concurrency limit of 1,000 the functions can handle at most 10,000 requests per second.
  scope: per account, all functions together; default; adjustable; at the default account concurrency limit.
  link: [10,000 requests per second](../facts/lambda.md#lambda-account-rps-10000-default)
  link: [10 times your account concurrency](../facts/lambda.md#lambda-account-rps-10000-default)
lambda-addpermission-limited-condition-keys
  claim: Individual permissions added with the console or the AddPermission API are single Allow statements that support only aws:SourceArn, aws:SourceAccount and aws:PrincipalOrgID as condition keys; a full JSON policy (PutResourcePolicy) supports all IAM global condition keys, multiple principals and explicit Deny statements.
  scope: function resource-based policy.
  link: [add single Allow statements](../facts/lambda.md#lambda-addpermission-limited-condition-keys)
  link: [only a limited set of condition keys](../facts/lambda.md#lambda-addpermission-limited-condition-keys)
  link: [create explicit Deny statements](../facts/lambda.md#lambda-addpermission-limited-condition-keys)
  say: AddPermission adds single allow statements
lambda-alb-target-rules-sync
  claim: An Application Load Balancer can use a Lambda function as a target, with listener rules that route HTTP requests to the function by path or header values; Elastic Load Balancing invokes the function synchronously with an event that holds the request body and metadata.
  scope: Application Load Balancer with Lambda.
  link: [Lambda functions as a target](../facts/lambda.md#lambda-alb-target-rules-sync)
  link: [based on path or header values](../facts/lambda.md#lambda-alb-target-rules-sync)
  link: [invokes your Lambda function synchronously](../facts/lambda.md#lambda-alb-target-rules-sync)
  say: Lambda as a load balancer target
lambda-alias-pointer-to-version
  claim: An alias is a pointer to a function version that you can update; users invoke the alias ARN, and when you deploy a new version you move the alias to it or split traffic between two versions.
  scope: per alias.
  link: [a pointer to a function version](../facts/lambda.md#lambda-alias-pointer-to-version)
  link: [split traffic between two versions](../facts/lambda.md#lambda-alias-pointer-to-version)
  say: a movable pointer to a version
lambda-apigateway-api-types
  claim: API Gateway has three API types that invoke Lambda functions (HTTP API, a lightweight low-latency RESTful API; REST API, a customizable feature-rich RESTful API; WebSocket API, with persistent full-duplex connections), and an API can serve traffic over the internet or only within your VPC.
  scope: API Gateway with Lambda.
  link: [A lightweight, low-latency RESTful API](../facts/lambda.md#lambda-apigateway-api-types)
  link: [A customizable, feature-rich RESTful API](../facts/lambda.md#lambda-apigateway-api-types)
  link: [maintains persistent connections with clients](../facts/lambda.md#lambda-apigateway-api-types)
  link: [accessible only within your VPC](../facts/lambda.md#lambda-apigateway-api-types)
  say: HTTP API, lightweight and low latency
lambda-apigateway-relays-error
  claim: Services that proxy requests from an upstream client may relay a function's error back to the requester; API Gateway always relays the error response back to the requester.
  scope: API Gateway in front of a Lambda function.
  link: [always relays the error response back](../facts/lambda.md#lambda-apigateway-relays-error)
  link: [API Gateway](../facts/lambda.md#lambda-apigateway-relays-error)
  say: API Gateway passes the error back to the caller
lambda-apigateway-sync-proxy-event
  claim: Amazon API Gateway invokes the function synchronously with a JSON representation of the HTTP request; with a custom integration the event is the request body, and with a proxy integration the event has a defined structure.
  scope: API Gateway with Lambda.
  link: [invokes your function synchronously](../facts/lambda.md#lambda-apigateway-sync-proxy-event)
  link: [the event has a defined structure](../facts/lambda.md#lambda-apigateway-sync-proxy-event)
  say: API Gateway calls it synchronously
lambda-apigw-better-for-production
  claim: API Gateway is the better choice for production applications at scale or when you need advanced features such as OpenAPI support, a choice of authentication options, custom domain names, or request/response handling with throttling, caching and transformation.
  scope: HTTP invocation of a Lambda function.
  link: [production applications at scale](../facts/lambda.md#lambda-apigw-better-for-production)
lambda-apigw-extra-features-waf-keys
  claim: Features that API Gateway adds and function URLs lack include API versioning, stage management, API keys for usage plans, WebSocket APIs, private APIs within a VPC, WAF integration and canary deployments.
  scope: API Gateway versus Lambda function URLs.
  link: [API keys for usage plans](../facts/lambda.md#lambda-apigw-extra-features-waf-keys)
  link: [WAF integration for additional security](../facts/lambda.md#lambda-apigw-extra-features-waf-keys)
lambda-arm64-better-price-performance
  claim: Functions on the arm64 architecture (AWS Graviton2 processor) can achieve significantly better price and performance than the equivalent function on x86_64; the guide suggests arm64 for compute-intensive applications such as high-performance computing, video encoding and simulation workloads.
  scope: Lambda function architecture.
  link: [significantly better price and performance](../facts/lambda.md#lambda-arm64-better-price-performance)
  link: [compute-intensive applications](../facts/lambda.md#lambda-arm64-better-price-performance)
  say: better price performance than x86
lambda-async-default-two-retries
  claim: For an asynchronous invocation that returns an error, Lambda by default tries two more times, with a wait of a minute before the second attempt and two minutes before the third.
  scope: per function, asynchronous invocation; default; adjustable.
  link: [two more times](../facts/lambda.md#lambda-async-default-two-retries)
  link: [two minutes between the second and third attempts](../facts/lambda.md#lambda-async-default-two-retries)
lambda-async-destination-targets
  claim: Lambda can send records of asynchronous invocations to a standard SQS queue, a standard SNS topic, an Amazon S3 bucket (on failure only), a Lambda function, or an EventBridge event bus.
  scope: asynchronous invocation destinations; an S3 bucket only for failed invocations.
  link: [A standard SQS queue](../facts/lambda.md#lambda-async-destination-targets)
  link: [A standard SNS topic](../facts/lambda.md#lambda-async-destination-targets)
  link: [An Amazon S3 bucket (on failure only)](../facts/lambda.md#lambda-async-destination-targets)
  link: [A Lambda function](../facts/lambda.md#lambda-async-destination-targets)
  link: [An EventBridge event bus](../facts/lambda.md#lambda-async-destination-targets)
  say: a standard SQS queue
lambda-async-discard-then-destination
  claim: When an asynchronous event exceeds its maximum age or fails all retry attempts, Lambda discards it; a failed-event destination keeps a copy.
  scope: asynchronous invocation.
  link: [Lambda discards it](../facts/lambda.md#lambda-async-discard-then-destination)
  link: [configure a failed-event destination](../facts/lambda.md#lambda-async-discard-then-destination)
lambda-async-event-age-api-range
  claim: In the PutFunctionEventInvokeConfig API, MaximumEventAgeInSeconds (the maximum age of a request that Lambda sends to a function for processing) has a valid range with a minimum value of 60 and a maximum value of 21600, and MaximumRetryAttempts has a valid range with a minimum value of 0 and a maximum value of 2.
  scope: asynchronous invocation settings of a function, a version or an alias; maximum; not adjustable; MaximumEventAgeInSeconds is in seconds.
  link: [Minimum value of 60. Maximum value of 21600.](../facts/lambda.md#lambda-async-event-age-api-range)
  link: [Minimum value of 0. Maximum value of 2.](../facts/lambda.md#lambda-async-event-age-api-range)
lambda-async-event-request-billing
  claim: An asynchronous event is billed as 1 request for its first 256 KB, plus 1 additional request for each 64 KB beyond that, up to 1 MB.
  scope: per asynchronous event.
  link: [1 request per each asynchronous Event for first 256 KB](../facts/lambda.md#lambda-async-event-request-billing)
  link: [1 additional request for each 64 KB](../facts/lambda.md#lambda-async-event-request-billing)
lambda-async-max-event-age-6-hours
  claim: The maximum age of an asynchronous event, the time Lambda keeps it in the asynchronous event queue, can be set up to 6 hours.
  scope: asynchronous invocation settings of a function, a version or an alias; maximum; adjustable.
  link: [up to 6 hours](../facts/lambda.md#lambda-async-max-event-age-6-hours)
lambda-async-queue-eventually-consistent
  claim: Because the asynchronous event queue is eventually consistent, a function can receive the same event more than once even without errors, so handle duplicates gracefully.
  scope: asynchronous invocation.
  link: [the queue itself is eventually consistent](../facts/lambda.md#lambda-async-queue-eventually-consistent)
lambda-async-queue-then-separate-process
  claim: For an asynchronous invocation, Lambda places the event in a queue and returns a success response without additional information; a separate process reads events from the queue and sends them to the function.
  scope: asynchronous invocation.
  link: [places the event in a queue](../facts/lambda.md#lambda-async-queue-then-separate-process)
  link: [returns a success response](../facts/lambda.md#lambda-async-queue-then-separate-process)
  link: [A separate process reads events from the queue](../facts/lambda.md#lambda-async-queue-then-separate-process)
  say: Lambda puts the event in a queue
lambda-async-requests-per-env
  claim: For asynchronous invocations, each instance of the execution environment can serve an unlimited number of requests, so the invocation limit depends only on the concurrency available to the function.
  scope: per function, per Region, asynchronous invocations.
  link: [unlimited number of requests](../facts/lambda.md#lambda-async-requests-per-env)
lambda-async-retry-attempts-0-to-2
  claim: The number of retries for an asynchronous invocation that returns an error can be set between 0 and 2.
  scope: asynchronous invocation settings of a function, a version or an alias; maximum; adjustable.
  link: [between 0 and 2](../facts/lambda.md#lambda-async-retry-attempts-0-to-2)
lambda-async-retry-logic-same-any-source
  claim: For asynchronous invocation, the retry logic is the same regardless of the invocation source.
  scope: asynchronous invocation.
  link: [the retry logic is the same](../facts/lambda.md#lambda-async-retry-logic-same-any-source)
  link: [regardless of the invocation source](../facts/lambda.md#lambda-async-retry-logic-same-any-source)
  say: the retry logic is the same for every source
lambda-async-s3-destination-on-failure-only
  claim: For asynchronous invocation destinations, S3 buckets are supported only as on-failure destinations; to keep records of successful invocations you use another destination type.
  scope: per asynchronous invocation configuration.
  link: [S3 buckets are supported only for on-failure destinations](../facts/lambda.md#lambda-async-s3-destination-on-failure-only)
lambda-async-service-gets-no-function-response
  claim: When a service invokes a function asynchronously, Lambda queues the event and immediately sends a success response to that service; after the function processes the event, Lambda does not return a response to the service that generated the event.
  scope: asynchronous invocation by an AWS service.
  link: [immediately sends a success response](../facts/lambda.md#lambda-async-service-gets-no-function-response)
  link: [Lambda doesn't return a response](../facts/lambda.md#lambda-async-service-gets-no-function-response)
  say: Lambda answers success right away
lambda-async-sns-destination-256-kb
  claim: Amazon SNS has a maximum message size of 256 KB, so when an asynchronous payload approaches 1 MB the invocation record sent to an SNS destination might exceed that limit and fail; Amazon SQS or Amazon S3 destinations are suggested for larger payloads.
  scope: per invocation record sent to an SNS destination; maximum; not adjustable; asynchronous invocation with an Amazon SNS destination.
  link: [maximum message size limit of 256 KB](../facts/lambda.md#lambda-async-sns-destination-256-kb)
  link: [approaches 1 MB](../facts/lambda.md#lambda-async-sns-destination-256-kb)
lambda-async-throttle-retry-6-hours
  claim: For throttling errors (429) and system errors (500-series) on asynchronous invocations, Lambda returns the event to the queue and keeps retrying for up to 6 hours by default, with the interval growing from 1 second to a maximum of 5 minutes.
  scope: per function, asynchronous invocation; default; adjustable.
  link: [up to 6 hours by default](../facts/lambda.md#lambda-async-throttle-retry-6-hours)
  link: [from 1 second after the first attempt to a maximum of 5 minutes](../facts/lambda.md#lambda-async-throttle-retry-6-hours)
lambda-best-suited-short-invocations
  claim: A standard Lambda invocation can last up to 15 minutes, but Lambda is best suited for short invocations that last one second or less.
  scope: per invocation, standard functions; maximum.
  link: [up to 15 minutes](../facts/lambda.md#lambda-best-suited-short-invocations)
  link: [one second or less](../facts/lambda.md#lambda-best-suited-short-invocations)
  say: up to fifteen minutes | best for one second or less
lambda-bp-least-privilege-role
  claim: Use most-restrictive permissions when setting IAM policies: understand the resources and operations the function needs and limit the execution role to these permissions.
  scope: Lambda execution role.
  link: [Use most-restrictive permissions](../facts/lambda.md#lambda-bp-least-privilege-role)
  link: [limit the execution role to these permissions](../facts/lambda.md#lambda-bp-least-privilege-role)
  say: least privilege for the execution role
lambda-bp-no-user-data-in-environment
  claim: To avoid data leaks across invocations, do not use the execution environment to store user data, events or other information with security implications.
  scope: Lambda function code.
  link: [avoid potential data leaks across invocations](../facts/lambda.md#lambda-bp-no-user-data-in-environment)
  link: [store user data, events, or other information](../facts/lambda.md#lambda-bp-no-user-data-in-environment)
  say: to avoid leaking data between invocations
lambda-bp-reserved-protects-downstream
  claim: Lambda functions scale with load, but upstream and downstream dependencies might not have the same throughput; to limit how high a function can scale, configure reserved concurrency on it.
  scope: per function.
  link: [limit how high your function can scale](../facts/lambda.md#lambda-bp-reserved-protects-downstream)
  link: [configure reserved concurrency](../facts/lambda.md#lambda-bp-reserved-protects-downstream)
  say: cap how far the function scales
lambda-bp-runaway-reserved-zero
  claim: AWS advises avoiding recursive invocations, which can cause an unintended volume of invocations and escalated costs; if that happens, set the function's reserved concurrency to 0 immediately to throttle all invocations while you update the code.
  scope: per function; unintended volume of invocations.
  link: [set the function reserved concurrency to 0](../facts/lambda.md#lambda-bp-runaway-reserved-zero)
  link: [throttle all invocations to the function](../facts/lambda.md#lambda-bp-runaway-reserved-zero)
  say: set reserved concurrency to zero
lambda-case-cyberark-18-weeks-3-hours
  claim: CyberArk chose to be serverless-first because of the low operational overhead; with serverless technologies and infrastructure-as-code blueprints, its platform team cut the time to onboard new services from 18 weeks to 3 hours.
  scope: CyberArk case study.
  link: [from 18 weeks to 3 hours](../facts/lambda.md#lambda-case-cyberark-18-weeks-3-hours)
  link: [because of the low operational overhead](../facts/lambda.md#lambda-case-cyberark-18-weeks-3-hours)
lambda-case-doordash-10-million-entries
  claim: Using serverless services on AWS, DoorDash processed more than 10 million sweepstakes entries in five hours with virtually no downtime; its partner chose a serverless approach because it did not want to deal with servers or hardware management.
  scope: DoorDash case study.
  link: [more than 10 million entries in five hours](../facts/lambda.md#lambda-case-doordash-10-million-entries)
  link: [didn’t want to deal with any servers](../facts/lambda.md#lambda-case-doordash-10-million-entries)
lambda-case-doordash-sqs-buffer
  claim: DoorDash connected Amazon API Gateway to Amazon SQS to decouple submission processing, and ran a Lambda function that retrieved data from SQS and sent it to Amazon Data Firehose (named Kinesis Data Firehose in the case study).
  scope: DoorDash case study.
  link: [to decouple submission processing](../facts/lambda.md#lambda-case-doordash-sqs-buffer)
lambda-case-fannie-mae-15000-concurrent
  claim: In an AWS whitepaper marked as for historical reference only, Fannie Mae's Lambda platform scaled to 15,000 concurrent function executions during testing and ran one simulation on 20 million mortgages in 2 hours, three times faster than the old system, without paying for idle compute resources.
  scope: Fannie Mae, whitepaper case study; the whitepaper is for historical reference only.
  link: [15,000 concurrent function executions](../facts/lambda.md#lambda-case-fannie-mae-15000-concurrent)
  link: [doesn’t pay for idle compute resources](../facts/lambda.md#lambda-case-fannie-mae-15000-concurrent)
lambda-case-finra-cost-50-percent
  claim: In an AWS whitepaper marked as for historical reference only, FINRA used Lambda for a serverless data processing solution that performs half a trillion data validations on 37 billion stock market events daily, and reported costs reduced by over 50 percent.
  scope: FINRA, whitepaper case study; the whitepaper is for historical reference only.
  link: [37 billion stock market events daily](../facts/lambda.md#lambda-case-finra-cost-50-percent)
  link: [reduced our costs by over 50 percent](../facts/lambda.md#lambda-case-finra-cost-50-percent)
lambda-case-prezzee-40x-67-percent
  claim: By moving to AWS Lambda, AWS Fargate and Amazon Aurora, Prezzee reports 40 times more scalability, 99.99 percent availability for customer-facing applications, over 90 percent fewer technical incidents and 67 percent lower time to market.
  scope: Prezzee case study.
  link: [40 times more scalability](../facts/lambda.md#lambda-case-prezzee-40x-67-percent)
  link: [lowered time to market by 67 percent](../facts/lambda.md#lambda-case-prezzee-40x-67-percent)
lambda-chaining-anti-pattern-sqs-or-step-functions
  claim: Lambda functions directly calling other Lambda functions is generally an anti-pattern because of cost and complexity (except for durable functions); the two common alternatives are an Amazon SQS queue between the functions or AWS Step Functions.
  scope: Lambda application design; does not apply to durable functions.
  link: [generally an anti-pattern](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  link: [use an Amazon SQS queue between Lambda functions](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  link: [use AWS Step Functions](../facts/lambda.md#lambda-chaining-anti-pattern-sqs-or-step-functions)
  say: function chaining is an anti-pattern
lambda-chaining-cost-wait-state
  claim: With Lambda you pay for the duration of an invocation, so in a chain of synchronous calls the calling functions keep running in a wait state while the last function runs, and their concurrency must all be equal.
  scope: Lambda application design.
  link: [you pay for the duration of an invocation](../facts/lambda.md#lambda-chaining-cost-wait-state)
  link: [running in a wait state](../facts/lambda.md#lambda-chaining-cost-wait-state)
  say: you pay while callers wait
lambda-change-async-payload-1-mb-2025
  claim: On 2025-10-24 Lambda raised the maximum payload size for asynchronous invocations from 256 KB to 1 MB.
  scope: per asynchronous invocation; maximum.
  link: [1 MB](../facts/lambda.md#lambda-change-async-payload-1-mb-2025)
  link: [256 KB](../facts/lambda.md#lambda-change-async-payload-1-mb-2025)
  link: [2025-10-24](../facts/lambda.md#lambda-change-async-payload-1-mb-2025)
  say: one megabyte | two hundred fifty-six kilobytes | October twenty-fourth, twenty twenty-five
  changed: 2025-10-24: was 256 KB
lambda-change-bandwidth-3000-mbps-2026
  claim: On 2026-08-05 Lambda added scalable network bandwidth for functions outside a VPC with 2 GB of memory or more: bandwidth scales from 625 Mbps at 2 GB up to 3,000 Mbps at 10 GB, where before the limit was 625 Mbps; you enable it with a request through AWS Service Quotas under the Network bandwidth per execution environment quota.
  scope: per execution environment, functions outside a VPC; maximum; after a Service Quotas request; functions with 2 GB of memory or more.
  link: [up to 3,000 Mbps at 10 GB](../facts/lambda.md#lambda-change-bandwidth-3000-mbps-2026)
  link: [existing limit of 625 Mbps](../facts/lambda.md#lambda-change-bandwidth-3000-mbps-2026)
  link: [2026-08-05](../facts/lambda.md#lambda-change-bandwidth-3000-mbps-2026)
  say: August fifth, twenty twenty-six
  changed: 2026-08-05: was 625 Mbps
lambda-change-code-storage-300-gb-2026
  claim: On 2026-07-15 Lambda raised the default limit for Lambda-managed code storage from 75GB to 300GB per Region per account, and added self-managed code storage in your own S3 bucket.
  scope: per Region per account, Lambda-managed code storage; default.
  link: [300GB per Region per account](../facts/lambda.md#lambda-change-code-storage-300-gb-2026)
  link: [75GB](../facts/lambda.md#lambda-change-code-storage-300-gb-2026)
  link: [2026-07-15](../facts/lambda.md#lambda-change-code-storage-300-gb-2026)
  say: three hundred gigabytes per Region | seventy-five gigabytes | July fifteenth, twenty twenty-six
  changed: 2026-07-15: was 75GB
lambda-change-durable-functions-2025
  claim: On 2025-12-02 Lambda announced durable functions, which checkpoint progress, suspend execution for up to one year during long-running tasks, and recover from failures without extra infrastructure; before, multi-step applications needed custom state management or external orchestration services.
  scope: Lambda durable functions; maximum.
  link: [suspend execution for up to one year](../facts/lambda.md#lambda-change-durable-functions-2025)
  link: [2025-12-02](../facts/lambda.md#lambda-change-durable-functions-2025)
  say: December second, twenty twenty-five
lambda-change-full-iam-resource-policies-2026
  claim: On 2026-08-25 Lambda functions gained full IAM resource-based policies, so you can define permissions for multiple principals and actions in one policy document with the full range of IAM condition keys; before, permissions had to be added individually per principal.
  scope: Lambda function resource-based policies.
  link: [multiple principals and actions](../facts/lambda.md#lambda-change-full-iam-resource-policies-2026)
  link: [2026-08-25](../facts/lambda.md#lambda-change-full-iam-resource-policies-2026)
  say: August twenty-fifth, twenty twenty-six
lambda-change-managed-instances-32-gb-2026
  claim: On 2026-03-27 Lambda Managed Instances gained up to 32 GB of memory and 16 vCPUs per function, with a choice of 2:1, 4:1 or 8:1 memory-to-vCPU ratio; before, function execution environments were limited to 10 GB of memory and about 6 vCPUs.
  scope: functions on Lambda Managed Instances; maximum.
  link: [up to 32 GB of memory and 16 vCPUs](../facts/lambda.md#lambda-change-managed-instances-32-gb-2026)
  link: [10 GB of memory and approximately 6 vCPUs](../facts/lambda.md#lambda-change-managed-instances-32-gb-2026)
  link: [2026-03-27](../facts/lambda.md#lambda-change-managed-instances-32-gb-2026)
  say: March twenty-seventh, twenty twenty-six
  changed: 2026-03-27: was 10 GB of memory and approximately 6 vCPUs
lambda-change-managed-instances-90-min-2026
  claim: On 2026-09-09 Lambda Managed Instances gained a 90-minute function timeout for asynchronous and event source mapping invocations, up from the previous 15-minute limit; synchronous invocations keep the 15-minute maximum.
  scope: Lambda Managed Instances, asynchronous and ESM invocations; maximum; synchronous invocations keep 15 minutes.
  link: [90-minute function timeout](../facts/lambda.md#lambda-change-managed-instances-90-min-2026)
  link: [previous 15-minute limit](../facts/lambda.md#lambda-change-managed-instances-90-min-2026)
  link: [2026-09-09](../facts/lambda.md#lambda-change-managed-instances-90-min-2026)
  say: September ninth, twenty twenty-six
  changed: 2026-09-09: was 15-minute limit
lambda-change-managed-instances-launch-2025
  claim: On 2025-11-30 Lambda added Managed Instances, which run Lambda functions on EC2 instances in your account for specialized hardware or for steady-state, predictable workloads that want EC2 pricing.
  scope: Lambda Managed Instances.
  link: [November 30, 2025](../facts/lambda.md#lambda-change-managed-instances-launch-2025)
  link: [steady-state or predictable workloads](../facts/lambda.md#lambda-change-managed-instances-launch-2025)
  say: November thirtieth, twenty twenty-five
lambda-change-microvms-launch-2026
  claim: On 2026-06-22 AWS introduced Lambda MicroVMs, a serverless compute primitive with VM-level isolation, near-instant launch and resume, and state preservation for running user or AI-generated code, with suspend and resume for up to 8 hours.
  scope: Lambda MicroVMs; maximum.
  link: [a new serverless compute primitive](../facts/lambda.md#lambda-change-microvms-launch-2026)
  link: [2026-06-22](../facts/lambda.md#lambda-change-microvms-launch-2026)
  say: June twenty-second, twenty twenty-six
lambda-change-recursion-all-regions-2026
  claim: On 2026-08-31 Lambda recursive loop detection, which is on by default and stops recursive invocations between Lambda functions and other supported services, expanded to all commercial AWS Regions.
  scope: Lambda recursive loop detection; default; turned off per function with PutFunctionRecursionConfig.
  link: [all commercial AWS Regions](../facts/lambda.md#lambda-change-recursion-all-regions-2026)
  link: [2026-08-31](../facts/lambda.md#lambda-change-recursion-all-regions-2026)
  say: August thirty-first, twenty twenty-six
lambda-change-s3-files-mount-2026
  claim: On 2026-04-21 Lambda added support for Amazon S3 Files, so functions can mount Amazon S3 buckets as file systems and perform standard file operations without downloading data for processing; S3 Files is built using Amazon EFS.
  scope: Lambda functions.
  link: [mount Amazon S3 buckets as file systems](../facts/lambda.md#lambda-change-s3-files-mount-2026)
  link: [2026-04-21](../facts/lambda.md#lambda-change-s3-files-mount-2026)
  say: April twenty-first, twenty twenty-six
lambda-change-scaling-per-function-2023
  claim: Each synchronously invoked Lambda function now scales by 1,000 concurrent executions every 10 seconds, and each function scales independently of other functions, until the aggregate concurrency across all functions reaches the account concurrency limit. Before this update, functions scaled at the account level by 500–3,000 concurrent executions (depending on the Region) in the first minute, then by 500 concurrent executions every minute.
  scope: per function (new); at the account level (old); maximum; until the aggregate concurrency reaches the account concurrency limit.
  link: [1,000 concurrent executions every 10 seconds](../facts/lambda.md#lambda-change-scaling-per-function-2023)
  link: [followed by 500 concurrent executions every minute](../facts/lambda.md#lambda-change-scaling-per-function-2023)
  say: a thousand every ten seconds, per function | the old rule: a burst, then five hundred per minute
  changed: 2023-12-06: was 500–3,000 concurrent executions (depending on the Region) in the first minute, followed by 500 concurrent executions every minute
lambda-change-self-managed-code-storage-2026
  claim: Lambda added self-managed S3 code storage: Lambda references function and layer code directly in your own S3 bucket instead of copying it, which removes the Lambda-managed storage limit for that code. The guide's history dates it 2026-04-30; the What's New post is dated 2026-07-15.
  scope: functions and layers using self-managed S3 code storage; you pay standard S3 storage; no additional Lambda charge.
  link: [self-managed S3 buckets](../facts/lambda.md#lambda-change-self-managed-code-storage-2026)
  link: [April 30, 2026](../facts/lambda.md#lambda-change-self-managed-code-storage-2026)
  say: April thirtieth, twenty twenty-six
lambda-change-snapstart-python-dotnet-2024
  claim: On 2024-11-18 Lambda SnapStart became available for the Python and .NET managed runtimes, beginning with python3.12 and dotnet8; when SnapStart launched on 2022-11-28 it was for Java functions.
  scope: SnapStart managed runtimes.
  link: [now available for Python and .NET managed runtimes](../facts/lambda.md#lambda-change-snapstart-python-dotnet-2024)
  link: [Java functions](../facts/lambda.md#lambda-change-snapstart-python-dotnet-2024)
  link: [November 18, 2024](../facts/lambda.md#lambda-change-snapstart-python-dotnet-2024)
  say: November eighteenth, twenty twenty-four
  changed: 2024-11-18: was Java functions
lambda-change-sqs-provisioned-mode-2025
  claim: On 2025-11-14 Lambda added provisioned mode for SQS event source mappings, which provisions a minimum and maximum number of event pollers that stay ready for traffic spikes; at launch AWS stated 3x faster scaling (up to 1000 concurrent executions per minute) and 16x higher concurrency (up to 20,000 concurrent executions) than the default SQS ESM.
  scope: SQS event source mappings in provisioned mode; maximum; figures stated in the launch announcement.
  link: [minimum and maximum number of polling resources](../facts/lambda.md#lambda-change-sqs-provisioned-mode-2025)
  link: [2025-11-14](../facts/lambda.md#lambda-change-sqs-provisioned-mode-2025)
  say: November fourteenth, twenty twenty-five
lambda-change-streaming-200-mb-2025
  claim: On 2025-07-31 Lambda response streaming raised its default maximum response payload size from 20 MB to 200 MB.
  scope: per streamed response, Lambda response streaming; default.
  link: [200 MB](../facts/lambda.md#lambda-change-streaming-200-mb-2025)
  link: [20 MB](../facts/lambda.md#lambda-change-streaming-200-mb-2025)
  link: [2025-07-31](../facts/lambda.md#lambda-change-streaming-200-mb-2025)
  say: two hundred megabytes | twenty megabytes | July thirty-first, twenty twenty-five
  changed: 2025-07-31: was 20 MB
lambda-change-tenant-isolation-2025
  claim: On 2025-11-19 Lambda added tenant isolation mode, which extends Lambda's isolation boundary from a single function to each tenant invoking that function; before, customers built custom solutions such as a dedicated function per tenant with their own request routing.
  scope: Lambda functions with tenant isolation mode.
  link: [from a single function to each tenant](../facts/lambda.md#lambda-change-tenant-isolation-2025)
  link: [2025-11-19](../facts/lambda.md#lambda-change-tenant-isolation-2025)
  say: November nineteenth, twenty twenty-five
lambda-choose-fargate-containers-persistent
  claim: The decision guide says to consider Fargate when you need to run containerized applications with specific resource needs or persistent processes.
  scope: Fargate versus Lambda.
  link: [specific resource needs or persistent processes](../facts/lambda.md#lambda-choose-fargate-containers-persistent)
  say: containers with persistent processes
lambda-choose-functions-event-driven-unpredictable
  claim: The Fargate-or-Lambda decision guide says to consider Lambda functions for event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows.
  scope: Lambda functions versus Lambda Managed Instances versus Fargate.
  link: [event-driven tasks, unpredictable workloads](../facts/lambda.md#lambda-choose-functions-event-driven-unpredictable)
  say: event-driven, unpredictable work
lambda-choose-managed-instances-steady-state
  claim: The decision guide says Lambda Managed Instances might be well suited when workloads are steady-state or predictable and benefit from EC2 pricing and specialized compute.
  scope: Lambda Managed Instances.
  link: [steady-state or predictable](../facts/lambda.md#lambda-choose-managed-instances-steady-state)
  say: steady, predictable traffic
lambda-code-storage-quota
  claim: Lambda-managed storage for uploaded .zip functions and layers is 300 GB (unzipped) per Region and is not increasable; use self-managed S3 code storage instead.
  scope: per account, per Region; maximum; not adjustable.
  link: [300 GB (unzipped)](../facts/lambda.md#lambda-code-storage-quota)
  link: [Not increasable](../facts/lambda.md#lambda-code-storage-quota)
lambda-cold-start-definition
  claim: A cold start is the time Lambda spends downloading your code and setting up a new execution environment before the handler runs. Cold starts typically occur in under 1% of invocations and last from under 100 ms to over 1 second.
  scope: per new execution environment.
  link: [under 1% of invocations](../facts/lambda.md#lambda-cold-start-definition)
  link: [from under 100 ms to over 1 second](../facts/lambda.md#lambda-cold-start-definition)
  link: [downloads your code, starts the environment](../facts/lambda.md#lambda-cold-start-definition)
  say: under one percent of invocations | from under a hundred milliseconds to over a second
lambda-compute-optimizer-x86-only
  claim: AWS Compute Optimizer can give Lambda memory setting recommendations after you opt in, but it supports only functions that use the x86_64 architecture.
  scope: AWS Compute Optimizer for Lambda; opt in first.
  link: [supports only functions that use x86_64 architecture](../facts/lambda.md#lambda-compute-optimizer-x86-only)
  link: [Lambda function memory setting recommendations](../facts/lambda.md#lambda-compute-optimizer-x86-only)
  say: only x86 functions
lambda-compute-savings-plans-apply
  claim: Compute Savings Plans lower prices on Amazon EC2 instance usage, and they also apply to AWS Fargate and AWS Lambda usage; Savings Plans can save up to 72% on AWS compute workloads.
  scope: Compute Savings Plans; maximum.
  link: [AWS Fargate and AWS Lambda usage](../facts/lambda.md#lambda-compute-savings-plans-apply)
  link: [up to 72%](../facts/lambda.md#lambda-compute-savings-plans-apply)
lambda-concurrency-example-100-rps-500-ms
  claim: At an average duration of 500 ms, one instance handles two requests per second, so a load of 100 requests per second needs 50 instances, that is, a concurrency of 50.
  scope: per function.
  link: [50 instances of your function to handle a load of 100 requests per second](../facts/lambda.md#lambda-concurrency-example-100-rps-500-ms)
lambda-concurrency-formula
  claim: Concurrency is estimated by multiplying average requests per second by the average request duration in seconds.
  scope: per function.
  link: [Multiplying average requests per second](../facts/lambda.md#lambda-concurrency-formula)
lambda-concurrent-executions-default
  claim: The default quota for concurrent executions is 1,000 per account per Region, and it can be increased up to tens of thousands.
  scope: per account, per Region; default; adjustable.
  link: [1,000](../facts/lambda.md#lambda-concurrent-executions-default)
  link: [Tens of thousands](../facts/lambda.md#lambda-concurrent-executions-default)
lambda-config-quotas-not-changeable
  claim: The function configuration, deployment and execution quotas (memory, timeout, payload, package size and so on) cannot be changed, except where the quotas page notes otherwise.
  scope: function configuration, deployment and execution quotas; maximum.
  link: [Except as noted, they can't be changed](../facts/lambda.md#lambda-config-quotas-not-changeable)
lambda-console-editor-3-mb
  claim: The Lambda console editor accepts a deployment package or layer archive of up to 3 Megabytes; larger files go through Amazon S3.
  scope: per deployment package, console editor upload; maximum; not adjustable.
  link: [3 Megabytes](../facts/lambda.md#lambda-console-editor-3-mb)
lambda-console-trigger-adds-resource-policy
  claim: When you create a trigger using the Lambda console, Lambda automatically adds the required permissions to the function's resource-based policy.
  scope: trigger created in the Lambda console.
  link: [Lambda automatically adds the required permissions](../facts/lambda.md#lambda-console-trigger-adds-resource-policy)
  link: [resource-based policy](../facts/lambda.md#lambda-console-trigger-adds-resource-policy)
  say: the console adds the permission for you
lambda-container-image-10-gb
  claim: A container image for Lambda is limited to 10 GB, measured as the maximum uncompressed image size including all layers.
  scope: per function, container image, uncompressed including all layers; maximum; not adjustable.
  link: [10 GB](../facts/lambda.md#lambda-container-image-10-gb)
lambda-container-image-ecr-same-region
  claim: A container image function is created from an image in an Amazon ECR repository that must be in the same AWS Region as the function; the image can be in a different AWS account if it is in the same Region.
  scope: Lambda function defined as a container image.
  link: [in the same AWS Region](../facts/lambda.md#lambda-container-image-ecr-same-region)
  link: [an image in a different AWS account](../facts/lambda.md#lambda-container-image-ecr-same-region)
  say: an ECR repository in the same Region
lambda-container-image-settings-16-kb
  claim: The container image settings of a function are limited to 16 KB.
  scope: per function, container image settings; maximum; not adjustable.
  link: [16 KB](../facts/lambda.md#lambda-container-image-settings-16-kb)
lambda-container-image-single-architecture
  claim: Lambda provides multi-architecture base images, but a function's image must target only one architecture; Lambda does not support functions that use multi-architecture container images.
  scope: Lambda function defined as a container image.
  link: [must target only one of the architectures](../facts/lambda.md#lambda-container-image-single-architecture)
  link: [multi-architecture container images](../facts/lambda.md#lambda-container-image-single-architecture)
  say: one architecture per image
lambda-control-plane-api-rate
  claim: The remaining control plane APIs (excluding invocation, GetFunction and GetPolicy) share one limit of 15 requests per second across all APIs, and it cannot be increased.
  scope: all remaining control plane APIs together, not per API; maximum; not adjustable; excludes invocation, GetFunction and GetPolicy requests.
  link: [15 requests per second across all APIs](../facts/lambda.md#lambda-control-plane-api-rate)
lambda-cpu-proportional-to-memory
  claim: Lambda allocates CPU power in proportion to the amount of memory configured; memory is the one setting that changes both.
  scope: per function.
  link: [in proportion to the amount of memory](../facts/lambda.md#lambda-cpu-proportional-to-memory)
lambda-cpu-up-to-6-vcpu
  claim: In Lambda, CPU is allocated in proportion to memory, which ranges from 128 MB to 10 GB in 1 MB increments, and CPU scales with memory up to 6 vCPU; you have no direct control over CPU.
  scope: per function; maximum; not adjustable.
  link: [up to 6 vCPU](../facts/lambda.md#lambda-cpu-up-to-6-vcpu)
  link: [between 128 MB and 10 GB](../facts/lambda.md#lambda-cpu-up-to-6-vcpu)
lambda-cross-account-resource-policy
  claim: To share a function with another AWS account, you add a cross-account permissions statement to the function's resource-based policy.
  scope: cross-account access to a function.
  link: [add a cross-account permissions statement](../facts/lambda.md#lambda-cross-account-resource-policy)
  link: [the function's resource-based policy](../facts/lambda.md#lambda-cross-account-resource-policy)
  say: add a cross-account statement to the resource-based policy
lambda-customer-managed-key-optional
  claim: You can optionally configure Lambda to use a customer managed key to encrypt environment variables, .zip deployment packages, filter criteria objects and durable execution data.
  scope: Lambda encryption at rest; optional.
  link: [use a customer managed key](../facts/lambda.md#lambda-customer-managed-key-optional)
  link: [.zip deployment packages](../facts/lambda.md#lambda-customer-managed-key-optional)
  say: a customer managed key
lambda-data-transfer-ec2-rates
  claim: Data transferred in to and out of Lambda functions from outside the Region is charged at Amazon EC2 data transfer rates.
  scope: data transfer from outside the Region.
  link: [charged at the Amazon EC2 data transfer rates](../facts/lambda.md#lambda-data-transfer-ec2-rates)
lambda-data-transfer-free-same-region
  claim: Data transfer between Lambda and S3, DynamoDB, SQS, SNS, Kinesis, ECR, EFS, SES and SimpleDB is free within the same Region.
  scope: data transfer, same Region.
  link: [free in the same AWS Region](../facts/lambda.md#lambda-data-transfer-free-same-region)
lambda-ddb-http-api-no-connections
  claim: DynamoDB uses an HTTP API, so functions make requests without maintaining connections, which helps cold starts; Amazon RDS uses traditional database connections that need connection pooling and possibly RDS Proxy, which costs extra.
  scope: database choice for Lambda applications.
  link: [DynamoDB uses an HTTP API](../facts/lambda.md#lambda-ddb-http-api-no-connections)
  link: [using Amazon RDS Proxy incurs additional costs](../facts/lambda.md#lambda-ddb-http-api-no-connections)
lambda-ddb-recommended-for-serverless
  claim: AWS recommends DynamoDB for serverless applications that need consistent low-latency performance and automatic scaling and do not require complex joins or transactions; Amazon RDS is the better choice for complex SQL queries, joins, or existing relational applications.
  scope: database choice for Lambda applications.
  link: [don't require complex joins or transactions](../facts/lambda.md#lambda-ddb-recommended-for-serverless)
  link: [complex SQL queries, joins](../facts/lambda.md#lambda-ddb-recommended-for-serverless)
lambda-ddb-stream-partition-key-order
  claim: For a DynamoDB stream, a parallelization factor between 1 (default) and 10 lets Lambda poll several concurrent batches from one shard; records that share a partition key still go to the same concurrent batch and are processed in order.
  scope: DynamoDB stream event source mapping, per shard; default.
  link: [from 1 (default) to 10](../facts/lambda.md#lambda-ddb-stream-partition-key-order)
  link: [are processed in order](../facts/lambda.md#lambda-ddb-stream-partition-key-order)
  say: from one, the default, to ten
lambda-ddb-streams-poll-4-per-second
  claim: Lambda polls the shards of a DynamoDB stream for records at a base rate of 4 times per second.
  scope: per DynamoDB stream shard; default.
  link: [base rate of 4 times per second](../facts/lambda.md#lambda-ddb-streams-poll-4-per-second)
lambda-destination-fifo-unsupported
  claim: An Amazon SQS FIFO queue or an Amazon SNS FIFO topic is an unsupported destination type for asynchronous invocation records; when Lambda cannot send a record to a configured destination, it sends a DestinationDeliveryFailures metric to Amazon CloudWatch.
  scope: asynchronous invocation destinations.
  link: [unsupported destination type](../facts/lambda.md#lambda-destination-fifo-unsupported)
  link: [an Amazon SQS FIFO queue](../facts/lambda.md#lambda-destination-fifo-unsupported)
  link: [DestinationDeliveryFailures metric](../facts/lambda.md#lambda-destination-fifo-unsupported)
  say: FIFO queues and FIFO topics are not supported
lambda-destinations-per-version-alias
  claim: A function can have multiple destinations, so successful and failed events can go to separate destinations, and destinations can be configured on a function, a function version or an alias.
  scope: asynchronous invocation destinations.
  link: [Each function can have multiple destinations](../facts/lambda.md#lambda-destinations-per-version-alias)
  link: [function version, or alias](../facts/lambda.md#lambda-destinations-per-version-alias)
  say: a function can have several destinations
lambda-dlq-content-only-vs-destinations
  claim: You can configure separate destinations for successfully processed events and for events that fail all processing attempts; alternatively, a standard SQS queue or standard SNS topic can be a dead-letter queue for discarded events, and Lambda sends a dead-letter queue only the content of the event, without details about the response.
  scope: asynchronous invocation.
  link: [separate destinations](../facts/lambda.md#lambda-dlq-content-only-vs-destinations)
  link: [a dead-letter queue for discarded events](../facts/lambda.md#lambda-dlq-content-only-vs-destinations)
  link: [only sends the content of the event](../facts/lambda.md#lambda-dlq-content-only-vs-destinations)
  say: destinations for success and for failure
lambda-durable-operations-per-execution
  claim: One durable execution can have at most 3,000 durable operations, and this quota cannot be increased.
  scope: per durable execution; maximum; not adjustable.
  link: [3,000](../facts/lambda.md#lambda-durable-operations-per-execution)
lambda-durable-pricing-dimensions
  claim: Durable functions add charges for durable operations (such as starting executions, completing steps and creating waits), for the data these operations write (per GB) and for data retention during and after execution (per GB-month, prorated), on top of normal Lambda compute charges.
  scope: Lambda durable functions.
  link: [you are charged for durable operations](../facts/lambda.md#lambda-durable-pricing-dimensions)
lambda-durable-running-executions
  claim: Durable functions allow at most 5,000,000 running durable executions per Region by default (10,000,000 in US East (N. Virginia), US West (Oregon) and Europe (Ireland)); this is a soft limit that can be increased.
  scope: per account, per Region; default; adjustable; higher default in US East (N. Virginia), US West (Oregon), and Europe (Ireland).
  link: [5,000,000 per Region](../facts/lambda.md#lambda-durable-running-executions)
  link: [10,000,000](../facts/lambda.md#lambda-durable-running-executions)
lambda-durable-storage-100-mb
  claim: A durable execution can persist at most 100 MB of cumulative payload (storage written), and this quota cannot be increased.
  scope: per durable execution; maximum; not adjustable.
  link: [100 MB](../facts/lambda.md#lambda-durable-storage-100-mb)
lambda-durable-vs-fargate-wait-heavy
  claim: For long-running workloads, durable functions are cost-effective for workflows that spend most of their time waiting (human approvals, scheduled delays, external callbacks) because waits incur no compute charges; Fargate fits workloads that need continuous compute.
  scope: Lambda durable functions versus Fargate.
  link: [spend most of their time waiting](../facts/lambda.md#lambda-durable-vs-fargate-wait-heavy)
  link: [require continuous compute](../facts/lambda.md#lambda-durable-vs-fargate-wait-heavy)
lambda-durable-vs-step-functions-focus
  claim: Durable functions are optimized for application development within Lambda where workflows are tightly coupled with business logic; Step Functions is built for workflow orchestration across AWS services, with visual design, native integrations to more than 220 services, and zero-maintenance infrastructure.
  scope: Lambda durable functions versus AWS Step Functions.
  link: [application development within Lambda](../facts/lambda.md#lambda-durable-vs-step-functions-focus)
  link: [workflow orchestration across AWS services](../facts/lambda.md#lambda-durable-vs-step-functions-focus)
lambda-duration-includes-init-code
  claim: In the Provisioned Concurrency pricing section, duration charges apply to code that runs in the handler and to initialization code declared outside of the handler; with Lambda extensions, duration also includes the time the last running extension takes to finish during the shutdown phase.
  scope: functions with Provisioned Concurrency (pricing page note); stated in the Provisioned Concurrency Pricing section.
  link: [declared outside of the handler](../facts/lambda.md#lambda-duration-includes-init-code)
lambda-duration-rounded-1-ms
  claim: For a function with Provisioned Concurrency, duration is calculated from the time the code begins executing until it returns or otherwise terminates, rounded up to the nearest 1ms.
  scope: functions with Provisioned Concurrency, per invocation; stated in the Provisioned Concurrency Pricing section.
  link: [rounded up to the nearest 1ms](../facts/lambda.md#lambda-duration-rounded-1-ms)
lambda-eda-not-for-consistent-low-latency
  claim: Event-driven applications communicate across networks and so introduce variable latency; workloads that need consistent low-latency performance, such as high-frequency trading or sub-millisecond robotics automation, are not good candidates for event-driven architecture.
  scope: event-driven architectures.
  link: [This design introduces variable latency](../facts/lambda.md#lambda-eda-not-for-consistent-low-latency)
  link: [are not good candidates for event-driven architecture](../facts/lambda.md#lambda-eda-not-for-consistent-low-latency)
  say: variable latency
lambda-eda-polling-inefficient
  claim: Polling can be highly inefficient for fetching updates because of the lag between new data becoming available and synchronization with downstream services, and webhooks are not always supported and might need custom authorization and authentication; both mechanisms can be replaced by events, which can be filtered, routed and pushed downstream.
  scope: event-driven architectures.
  link: [Polling can be highly inefficient](../facts/lambda.md#lambda-eda-polling-inefficient)
  link: [Webhooks are not always supported](../facts/lambda.md#lambda-eda-polling-inefficient)
  say: polling wastes effort and adds lag
lambda-edge-event-sources-row
  claim: CloudFront Functions run only on viewer request and viewer response events, while Lambda@Edge also runs on origin request and origin response events.
  scope: CloudFront Functions versus Lambda@Edge.
  link: [Origin request](../facts/lambda.md#lambda-edge-event-sources-row)
lambda-edge-network-access-row
  claim: CloudFront Functions have no network access, while Lambda@Edge functions do.
  scope: CloudFront Functions versus Lambda@Edge.
  link: [Network access | No](../facts/lambda.md#lambda-edge-network-access-row)
  say: CloudFront Functions have no network access
lambda-edge-request-price
  claim: Lambda@Edge requests cost $0.60 per 1 million requests.
  scope: Lambda@Edge, per request.
  link: [$0.60 per 1 million requests](../facts/lambda.md#lambda-edge-request-price)
lambda-efs-mount-target-every-az
  claim: For Lambda, create the EFS file system with a mount target in every Availability Zone the function connects to, use at least two Availability Zones for performance and resilience, and allow NFS traffic (port 2049) in the security groups of the function and the mount targets.
  scope: Amazon EFS file system used by Lambda.
  link: [a mount target in every Availability Zone](../facts/lambda.md#lambda-efs-mount-target-every-az)
  link: [use at least two Availability Zones](../facts/lambda.md#lambda-efs-mount-target-every-az)
  link: [NFS traffic (port 2049)](../facts/lambda.md#lambda-efs-mount-target-every-az)
  say: a mount target in every Availability Zone
lambda-efs-role-permissions
  claim: If the EFS file system has a user-configured IAM policy, the function's execution role needs the matching elasticfilesystem permissions (included in the AmazonElasticFileSystemClientReadWriteAccess managed policy) and the permissions required to connect to the file system's VPC.
  scope: execution role of a function that uses Amazon EFS; the file system has a user-configured IAM policy.
  link: [AmazonElasticFileSystemClientReadWriteAccess](../facts/lambda.md#lambda-efs-role-permissions)
  link: [connect to the file system's VPC](../facts/lambda.md#lambda-efs-role-permissions)
  say: the EFS client read-write managed policy
lambda-efs-shared-mount-in-vpc
  claim: A function can mount an Amazon EFS file system to a local directory, so the function code can access and modify shared resources safely and at high concurrency; the function connects to the file system over the local network in a VPC.
  scope: Lambda function with an Amazon EFS file system; the function connects to a VPC.
  link: [mount an Amazon Elastic File System](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  link: [access and modify shared resources safely](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  link: [over the local network in a VPC](../facts/lambda.md#lambda-efs-shared-mount-in-vpc)
  say: mount an EFS file system
lambda-encryption-at-rest-always
  claim: Lambda always encrypts at rest environment variables, the files you upload (deployment packages and layer archives), event source mapping filter criteria objects and durable execution data.
  scope: Lambda data at rest.
  link: [always provides at-rest encryption](../facts/lambda.md#lambda-encryption-at-rest-always)
  link: [Environment variables](../facts/lambda.md#lambda-encryption-at-rest-always)
  link: [including deployment packages and layer archives](../facts/lambda.md#lambda-encryption-at-rest-always)
  say: Lambda always encrypts it at rest
lambda-eni-per-subnet-sg-combination
  claim: Lambda creates one network interface for each combination of subnet and security group that functions connect to; the quota of 3,000 network interfaces per VPC is adjustable.
  scope: per VPC; default; adjustable.
  link: [each combination of subnet and security group](../facts/lambda.md#lambda-eni-per-subnet-sg-combination)
  link: [3,000](../facts/lambda.md#lambda-eni-per-subnet-sg-combination)
lambda-eni-per-vpc-quota
  claim: Lambda's quota for elastic network interfaces per VPC is 3,000 by default and can be increased to thousands; the quota is shared with other services such as Amazon EFS.
  scope: per VPC; default; adjustable; shared with other services, such as Amazon EFS.
  link: [3,000](../facts/lambda.md#lambda-eni-per-vpc-quota)
  link: [Thousands](../facts/lambda.md#lambda-eni-per-vpc-quota)
lambda-env-vars-size
  claim: All environment variables of a function together are limited to 4 KB in aggregate.
  scope: per function, all environment variables in aggregate; maximum; not adjustable.
  link: [4 KB](../facts/lambda.md#lambda-env-vars-size)
lambda-environment-not-persistent
  claim: Lambda terminates execution environments every few hours to allow for runtime updates and maintenance, even for functions that are invoked continuously, so you should not assume that an execution environment persists indefinitely.
  scope: per execution environment.
  link: [terminates execution environments every few hours](../facts/lambda.md#lambda-environment-not-persistent)
  say: environments are recycled every few hours
lambda-ephemeral-storage-512-mb-free
  claim: 512 MB of ephemeral storage comes with every function at no additional cost; you pay only for additional ephemeral storage you configure, by duration.
  scope: per function, /tmp ephemeral storage; default.
  link: [512 MB of ephemeral storage is available to each Lambda function at no additional cost](../facts/lambda.md#lambda-ephemeral-storage-512-mb-free)
lambda-ephemeral-storage-price
  claim: In the pricing-page example (US East (N. Virginia)), ephemeral storage above the free 512 MB costs $0.0000000309 per GB-second.
  scope: per GB-second of ephemeral storage above 512 MB; pricing-page example priced in US East (N. Virginia).
  link: [$0.0000000309 for every GB-second](../facts/lambda.md#lambda-ephemeral-storage-price)
lambda-epu-pricing
  claim: In the Lambda pricing page example with 10 Kafka event source mappings in provisioned mode in US East (N. Virginia), the EPU-hours price is $0.185 per hour and an EPU supports 10 event pollers.
  scope: per EPU-hour; pricing example for Kafka event source mappings in US East (N. Virginia); pricing example, not a general rate for every event source.
  link: [$0.185/hour](../facts/lambda.md#lambda-epu-pricing)
  link: [10 event pollers per EPU](../facts/lambda.md#lambda-epu-pricing)
lambda-esm-at-least-once
  claim: Event source mappings process each event at least once, so duplicates can occur and function code should be idempotent.
  scope: event source mappings.
  link: [process each event at least once](../facts/lambda.md#lambda-esm-at-least-once)
  link: [duplicate processing of records can occur](../facts/lambda.md#lambda-esm-at-least-once)
lambda-esm-batch-triggers-three-criteria
  claim: An event source mapping invokes the function when the batching window reaches its maximum value, when the batch size is met, or when the payload size reaches 6 MB; the 6 MB payload limit cannot be modified.
  scope: per event source mapping batch; maximum; the payload limit cannot be modified.
  link: [The batching window reaches its maximum value](../facts/lambda.md#lambda-esm-batch-triggers-three-criteria)
  link: [The batch size is met](../facts/lambda.md#lambda-esm-batch-triggers-three-criteria)
  link: [6 MB](../facts/lambda.md#lambda-esm-batch-triggers-three-criteria)
  say: the batching window ends | six megabytes
lambda-esm-batches-records
  claim: Stream and queue services such as Kinesis and SQS use an event source mapping instead of a standard trigger: the mapping polls the source, batches records together, and invokes the function with the batch.
  scope: event source mappings.
  link: [batch records together](../facts/lambda.md#lambda-esm-batches-records)
  link: [invoke your function with the batched events](../facts/lambda.md#lambda-esm-batches-records)
  say: it polls the source and batches records
lambda-esm-batching-window-0-to-300
  claim: For Kinesis, DynamoDB and Amazon SQS event sources the default batching window is 0 seconds, so Lambda invokes the function as soon as records are available; you can set it from 0 to 300 seconds in increments of 1 second.
  scope: per event source mapping (Kinesis, DynamoDB, Amazon SQS); default; adjustable.
  link: [0 seconds](../facts/lambda.md#lambda-esm-batching-window-0-to-300)
  link: [from 0 to 300 seconds](../facts/lambda.md#lambda-esm-batching-window-0-to-300)
lambda-esm-lambda-polls-source
  claim: With an event source mapping, Lambda itself fetches events from a queue or stream: Lambda handles the polling and invokes your function, so the source service does not push events.
  scope: event source mappings.
  link: [Lambda handles the polling](../facts/lambda.md#lambda-esm-lambda-polls-source)
  link: [Lambda actively fetches](../facts/lambda.md#lambda-esm-lambda-polls-source)
  say: Lambda does the polling for you
lambda-esm-retry-excludes-throttles
  claim: Service errors or throttles where the batch does not reach the function do not count toward an event source mapping's retry attempts, and the mapping can send an invocation record to a destination when it discards an event batch.
  scope: event source mapping.
  link: [do not count toward retry attempts](../facts/lambda.md#lambda-esm-retry-excludes-throttles)
  link: [when it discards an event batch](../facts/lambda.md#lambda-esm-retry-excludes-throttles)
  say: throttles do not use up the retries
lambda-esm-stream-reprocess-batch-pause-shard
  claim: By default, if the function returns an error, an event source mapping reprocesses the entire batch until the function succeeds or the items in the batch expire, and it pauses processing for the affected shard until the error is resolved to keep in-order processing.
  scope: event source mapping for a stream (DynamoDB, Kinesis); default; for DynamoDB and Kinesis you can set a maximum number of retries.
  link: [reprocesses the entire batch](../facts/lambda.md#lambda-esm-stream-reprocess-batch-pause-shard)
  link: [pauses processing for the affected shard](../facts/lambda.md#lambda-esm-stream-reprocess-batch-pause-shard)
  say: Lambda retries the whole batch
lambda-event-push-or-pull
  claim: An event is anything that triggers a Lambda function to run. An event reaches a function in two ways: direct invocation, where a service pushes the event, or an event source mapping, where Lambda pulls events from a queue or stream.
  scope: per invocation.
  link: [direct invocation (push)](../facts/lambda.md#lambda-event-push-or-pull)
  link: [event source mappings (pull)](../facts/lambda.md#lambda-event-push-or-pull)
  link: [anything that triggers a Lambda function to run](../facts/lambda.md#lambda-event-push-or-pull)
  say: push, by direct invocation | pull, by an event source mapping
lambda-exec-role-least-privilege
  claim: As a best practice, before publishing a function to production, adjust its execution role policy to include only the required permissions.
  scope: Lambda execution role.
  link: [include only the required permissions](../facts/lambda.md#lambda-exec-role-least-privilege)
lambda-execution-role-required-logs
  claim: Every Lambda function must have an execution role, and at a minimum the role needs access to Amazon CloudWatch because functions log to CloudWatch Logs by default; the AWSLambdaBasicExecutionRole managed policy satisfies this.
  scope: every Lambda function.
  link: [must have an execution role](../facts/lambda.md#lambda-execution-role-required-logs)
  link: [AWSLambdaBasicExecutionRole](../facts/lambda.md#lambda-execution-role-required-logs)
  link: [log to CloudWatch Logs by default](../facts/lambda.md#lambda-execution-role-required-logs)
  say: every function needs an execution role
lambda-execution-role-trust-lambda-principal
  claim: Lambda automatically assumes the execution role when the function is invoked, and the role's trust policy must name the Lambda service principal (lambda.amazonaws.com) as a trusted service.
  scope: Lambda execution role.
  link: [lambda.amazonaws.com](../facts/lambda.md#lambda-execution-role-trust-lambda-principal)
  link: [Lambda automatically assumes your execution role](../facts/lambda.md#lambda-execution-role-trust-lambda-principal)
  say: the Lambda service principal
lambda-faq-advanced-logging-no-charge
  claim: Advanced logging controls add no charge; you still pay CloudWatch Logs for ingestion and storage of the logs.
  scope: Lambda advanced logging controls.
  link: [no additional charge](../facts/lambda.md#lambda-faq-advanced-logging-no-charge)
lambda-faq-code-encrypted-at-rest
  claim: Lambda stores function code in Amazon S3 and encrypts it at rest.
  scope: function code stored by Lambda.
  link: [encrypts it at rest](../facts/lambda.md#lambda-faq-code-encrypted-at-rest)
lambda-faq-code-signing-corrupt-signature
  claim: A corrupt signature occurs at deployment if the code artifact has been altered since signing.
  scope: per deployment; code signing is enabled for the function.
  link: [Corrupt signature](../facts/lambda.md#lambda-faq-code-signing-corrupt-signature)
lambda-faq-code-signing-existing-functions
  claim: You can enable code signing for an existing Lambda function by attaching a code signing configuration to the function.
  scope: per function.
  link: [attaching a code signing configuration to the function](../facts/lambda.md#lambda-faq-code-signing-existing-functions)
lambda-faq-code-signing-mismatched-signature
  claim: A mismatched signature occurs at deployment if the code artifact is signed by a signing profile that is not approved.
  scope: per deployment; code signing is enabled for the function.
  link: [Mismatched signature](../facts/lambda.md#lambda-faq-code-signing-mismatched-signature)
lambda-faq-code-signing-no-additional-cost
  claim: Code Signing for Lambda has no additional cost; you pay the standard price for Lambda.
  scope: Code Signing for Lambda.
  link: [no additional cost](../facts/lambda.md#lambda-faq-code-signing-no-additional-cost)
lambda-faq-code-signing-warn-or-reject
  claim: A Code Signing Configuration specifies the approved signing profiles and whether to warn or reject deployments if signature checks fail.
  scope: per code signing configuration; if signature checks fail.
  link: [warn or reject deployments](../facts/lambda.md#lambda-faq-code-signing-warn-or-reject)
lambda-faq-code-signing-what
  claim: Code Signing for Lambda verifies that only unaltered code from approved developers is deployed, using AWS Signer to sign artifacts and the function to verify signatures at deployment.
  scope: Code Signing for Lambda.
  link: [AWS Signer](../facts/lambda.md#lambda-faq-code-signing-what)
lambda-faq-code-signing-zip-only
  claim: Code Signing for Lambda is currently only available for functions packaged as ZIP archives.
  scope: per function.
  link: [only available for functions packaged as ZIP archives](../facts/lambda.md#lambda-faq-code-signing-zip-only)
lambda-faq-default-limit-account-level
  claim: The default maximum concurrent execution limit applies at the account level, and you can also set limits on individual functions.
  scope: per account; per function with reserved concurrency.
  link: [account level](../facts/lambda.md#lambda-faq-default-limit-account-level)
lambda-faq-deploy-zip-or-image
  claim: A function can be deployed as a .zip file archive or as a container image; both give the same execution environment, scaling, and operational simplicity.
  scope: function deployment packages.
  link: [.zip file archives](../facts/lambda.md#lambda-faq-deploy-zip-or-image)
  link: [container images](../facts/lambda.md#lambda-faq-deploy-zip-or-image)
lambda-faq-dlq-after-retries
  claim: When an asynchronous invocation exhausts its retry policy, the event goes to a configured dead letter queue (DLQ); without a DLQ the event may be rejected.
  scope: asynchronous invocations.
  link: [dead letter queue](../facts/lambda.md#lambda-faq-dlq-after-retries)
lambda-faq-dlq-sqs-or-sns
  claim: A Lambda dead letter queue can be an Amazon SQS queue or an Amazon SNS topic.
  scope: per function, dead letter queue.
  link: [Amazon SQS queue or an Amazon SNS topic](../facts/lambda.md#lambda-faq-dlq-sqs-or-sns)
lambda-faq-durable-beyond-15-minutes
  claim: The per-invocation timeout stays 15 minutes, but a durable function can suspend and resume across invocations, and when invoked asynchronously its durable execution timeout can extend up to one year.
  scope: per durable execution, asynchronous invocation; maximum.
  link: [up to one year](../facts/lambda.md#lambda-faq-durable-beyond-15-minutes)
lambda-faq-durable-checkpoint-256-kb
  claim: Each checkpointed operation of a durable function, such as a step or callback, can store up to 256 KB of data, counted on the data the operation returns.
  scope: per checkpointed operation; maximum; not adjustable.
  link: [256 KB](../facts/lambda.md#lambda-faq-durable-checkpoint-256-kb)
lambda-faq-durable-concurrency-released-on-wait
  claim: Durable functions share the account-level concurrency pool with standard functions, and concurrency slots are released during waits.
  scope: durable functions, account concurrency pool.
  link: [released during waits](../facts/lambda.md#lambda-faq-durable-concurrency-released-on-wait)
lambda-faq-durable-languages
  claim: You can create durable functions for Node.js, Python, Java and C# (.NET) using managed runtimes; durable functions are also available through OCI container images.
  scope: durable functions.
  link: [Node.js, Python, Java](../facts/lambda.md#lambda-faq-durable-languages)
lambda-faq-durable-no-charge-while-waiting
  claim: For on-demand durable functions there are no compute charges during suspension when the function waits with the durable execution SDK.
  scope: on-demand durable functions.
  link: [no compute charges during suspension](../facts/lambda.md#lambda-faq-durable-no-charge-while-waiting)
lambda-faq-durable-timeout-and-retention
  claim: When you invoke a durable function asynchronously, the durable execution timeout can be up to 1 year; the retention period for history and checkpoint data after the execution reaches a terminal state is up to 90 days.
  scope: per durable execution; maximum; not adjustable; the one-year execution timeout applies when the durable function is invoked asynchronously.
  link: [up to 1 year](../facts/lambda.md#lambda-faq-durable-timeout-and-retention)
  link: [up to 90 days](../facts/lambda.md#lambda-faq-durable-timeout-and-retention)
lambda-faq-durable-vs-step-functions
  claim: Use Lambda durable functions to build logic in Lambda's programming model with local testing and your language; use Step Functions for visual workflow design, cross-team visibility, native service integrations, or zero-maintenance infrastructure.
  scope: choice between durable functions and Step Functions.
  link: [visual workflow design](../facts/lambda.md#lambda-faq-durable-vs-step-functions)
lambda-faq-edge-cloudfront-triggers
  claim: Lambda@Edge runs Node.js or Python code in response to CloudFront requests: when a viewer request lands, when a request is forwarded to or received back from the origin, and right before responding to the end-user.
  scope: Lambda@Edge with CloudFront.
  link: [Amazon CloudFront requests](../facts/lambda.md#lambda-faq-edge-cloudfront-triggers)
lambda-faq-edge-existing-functions
  claim: You can associate existing Lambda functions with CloudFront events for global invocation if the function satisfies the Lambda@Edge service requirements and limits.
  scope: per function; the function satisfies the Lambda@Edge service requirements and limits.
  link: [satisfies the Lambda@Edge service requirements and limits](../facts/lambda.md#lambda-faq-edge-existing-functions)
lambda-faq-edge-function-version
  claim: To use Lambda@Edge, you upload your code to AWS Lambda and associate a function version to be triggered in response to Amazon CloudFront requests.
  scope: Lambda@Edge association with CloudFront.
  link: [function version](../facts/lambda.md#lambda-faq-edge-function-version)
lambda-faq-edge-runtimes
  claim: Lambda@Edge supports Node.js and Python for global invocation by CloudFront events.
  scope: Lambda@Edge.
  link: [Node.js and Python](../facts/lambda.md#lambda-faq-edge-runtimes)
lambda-faq-edge-when
  claim: Lambda@Edge is for latency-sensitive use cases with globally distributed viewers, where everything needed for the decision is available at the CloudFront edge, within the function and the request.
  scope: Lambda@Edge use cases.
  link: [latency-sensitive use cases](../facts/lambda.md#lambda-faq-edge-when)
  link: [distributed globally](../facts/lambda.md#lambda-faq-edge-when)
lambda-faq-env-vars-supported
  claim: Lambda supports environment variables, which you can create and modify from the console, CLI, or SDKs.
  scope: per function, environment variables.
  link: [environment variables](../facts/lambda.md#lambda-faq-env-vars-supported)
lambda-faq-event-source-push-or-poll
  claim: Some services publish events to Lambda by invoking the function directly (for example Amazon S3); Lambda can also poll resources in services that do not publish events to it.
  scope: event sources.
  link: [invoking the cloud function directly](../facts/lambda.md#lambda-faq-event-source-push-or-poll)
  link: [poll resources](../facts/lambda.md#lambda-faq-event-source-push-or-poll)
lambda-faq-execution-role
  claim: A function gets access to other AWS resources through an IAM role that Lambda assumes while the function runs, so you always keep control of which resources it can use.
  scope: per function, execution role.
  link: [IAM role](../facts/lambda.md#lambda-faq-execution-role)
lambda-faq-failure-sync-exception
  claim: On failure, a synchronously invoked function responds with an exception to the caller.
  scope: synchronous invocations.
  link: [respond with an exception](../facts/lambda.md#lambda-faq-failure-sync-exception)
lambda-faq-high-availability
  claim: Lambda uses replication and redundancy for high availability of the service and of your functions; there are no maintenance windows or scheduled downtimes for either.
  scope: Lambda service and functions.
  link: [no maintenance windows or scheduled downtimes](../facts/lambda.md#lambda-faq-high-availability)
lambda-faq-https-via-api-gateway
  claim: You can invoke a function over HTTPS by defining a custom RESTful API with Amazon API Gateway, which gives the function an endpoint that can respond to REST calls like GET, PUT, and POST.
  scope: HTTPS invocation through API Gateway.
  link: [Amazon API Gateway](../facts/lambda.md#lambda-faq-https-via-api-gateway)
lambda-faq-invoke-api-owner-or-granted
  claim: Only the function owner, or another AWS account the owner has granted permission, can invoke a function through the Invoke API.
  scope: per function.
  link: [Only the function owner](../facts/lambda.md#lambda-faq-invoke-api-owner-or-granted)
lambda-faq-isolated-environment
  claim: Each Lambda function runs in its own isolated environment, with its own resources and file system view.
  scope: per function, execution environment.
  link: [own isolated environment](../facts/lambda.md#lambda-faq-isolated-environment)
lambda-faq-languages
  claim: Lambda natively supports Java, Go, PowerShell, Node.js, C#, Python, and Ruby, and a Runtime API lets you use any additional programming language.
  scope: Lambda runtimes.
  link: [Runtime API](../facts/lambda.md#lambda-faq-languages)
lambda-faq-layers-share-code
  claim: You can package any code (frameworks, SDKs, libraries) as a Lambda Layer and share it across multiple functions.
  scope: Lambda layers.
  link: [Lambda Layer](../facts/lambda.md#lambda-faq-layers-share-code)
lambda-faq-limit-increase-service-quotas
  claim: A request to increase the concurrent execution limit goes through Service Quotas.
  scope: per account, per Region, concurrent executions.
  link: [Service Quotas](../facts/lambda.md#lambda-faq-limit-increase-service-quotas)
lambda-faq-logging-custom-log-group
  claim: You can set which Amazon CloudWatch log group Lambda sends logs to, which makes it easier to aggregate logs from multiple functions of an application in one place.
  scope: per function.
  link: [set which Amazon CloudWatch log group](../facts/lambda.md#lambda-faq-logging-custom-log-group)
lambda-faq-logging-json-structured
  claim: Lambda advanced logging controls can capture function logs in JSON structured format without your own logging libraries.
  scope: per function.
  link: [JSON structured format](../facts/lambda.md#lambda-faq-logging-json-structured)
lambda-faq-logging-level-no-code-changes
  claim: You can control the log level filtering of Lambda function logs without making any code changes.
  scope: per function.
  link: [without making any code changes](../facts/lambda.md#lambda-faq-logging-level-no-code-changes)
lambda-faq-memory-cpu-proportional
  claim: You choose the memory for a function and Lambda allocates proportional CPU power: 256MB of memory gets about twice the CPU power of 128MB and half the CPU power of 512MB.
  scope: per function.
  link: [proportional CPU power](../facts/lambda.md#lambda-faq-memory-cpu-proportional)
  link: [256MB](../facts/lambda.md#lambda-faq-memory-cpu-proportional)
lambda-faq-memory-range
  claim: The FAQ states that function memory can be set from 128MB to 10,240MB.
  scope: per function; maximum; not adjustable.
  link: [128MB](../facts/lambda.md#lambda-faq-memory-range)
  link: [10,240MB](../facts/lambda.md#lambda-faq-memory-range)
lambda-faq-microvm-32-gb-16-vcpu
  claim: A Lambda MicroVM supports up to 32 GB of memory and 16 vCPUs.
  scope: per MicroVM; maximum; not adjustable.
  link: [32 GB](../facts/lambda.md#lambda-faq-microvm-32-gb-16-vcpu)
  link: [16 vCPUs](../facts/lambda.md#lambda-faq-microvm-32-gb-16-vcpu)
lambda-faq-microvm-sla-99-5
  claim: Lambda MicroVMs are covered by the Lambda SLA with a Monthly Uptime Percentage commitment of at least 99.5% for instance-level availability.
  scope: per MicroVM, monthly.
  link: [99.5%](../facts/lambda.md#lambda-faq-microvm-sla-99-5)
lambda-faq-microvm-suspend-8-hours
  claim: A suspended MicroVM keeps its full memory and disk state for up to 8 hours and is not charged for compute while suspended.
  scope: per MicroVM; maximum; not adjustable.
  link: [up to 8 hours](../facts/lambda.md#lambda-faq-microvm-suspend-8-hours)
lambda-faq-microvm-what
  claim: Lambda MicroVMs is a serverless compute primitive that combines VM-level isolation, near-instant launch and resume, and state persistence across interactions, built for workloads that execute user- or AI-generated code.
  scope: Lambda MicroVMs.
  link: [VM-level isolation](../facts/lambda.md#lambda-faq-microvm-what)
lambda-faq-monitoring-cloudwatch
  claim: Lambda automatically reports real-time metrics to Amazon CloudWatch, including total requests, account-level and function-level concurrency usage, latency, error rates, and throttled requests.
  scope: Lambda metrics in CloudWatch.
  link: [Amazon CloudWatch](../facts/lambda.md#lambda-faq-monitoring-cloudwatch)
lambda-faq-parallel-no-limit-safety-throttle
  claim: There is no limit on how many instances of a function run in parallel, but Lambda has a default safety throttle on the number of concurrent executions per account per Region.
  scope: per account, per Region; default; adjustable.
  link: [default safety throttle](../facts/lambda.md#lambda-faq-parallel-no-limit-safety-throttle)
lambda-faq-pay-per-use
  claim: Lambda is priced on a pay-per-use basis.
  scope: Lambda pricing.
  link: [pay-per-use](../facts/lambda.md#lambda-faq-pay-per-use)
lambda-faq-pc-adjust-or-off
  claim: You can raise Provisioned Concurrency during high demand and lower it, or turn it off completely, when demand decreases.
  scope: per function, Provisioned Concurrency.
  link: [turn it off completely](../facts/lambda.md#lambda-faq-pc-adjust-or-off)
lambda-faq-pc-application-auto-scaling
  claim: Application Auto Scaling can adjust Provisioned Concurrency on a schedule or automatically in real time as demand changes.
  scope: per function, Provisioned Concurrency.
  link: [Application Auto Scaling](../facts/lambda.md#lambda-faq-pc-application-auto-scaling)
lambda-faq-pc-pricing
  claim: With Provisioned Concurrency you pay for the amount of concurrency you configure and for how long you configure it, and you still pay for Requests and execution Duration when the function runs.
  scope: per function, Provisioned Concurrency.
  link: [Provisioned Concurrency](../facts/lambda.md#lambda-faq-pc-pricing)
lambda-faq-pc-what
  claim: Provisioned Concurrency keeps functions initialized and ready to respond in double-digit milliseconds.
  scope: per function, Provisioned Concurrency.
  link: [double-digit milliseconds](../facts/lambda.md#lambda-faq-pc-what)
lambda-faq-pc-when
  claim: Provisioned Concurrency is for latency-sensitive applications such as web or mobile backends, synchronously invoked APIs, and interactive microservices.
  scope: Provisioned Concurrency use cases.
  link: [latency-sensitive applications](../facts/lambda.md#lambda-faq-pc-when)
lambda-faq-per-function-concurrency-control
  claim: You can cap the maximum concurrent executions of an individual function, either to reserve part of the account concurrency for critical functions or to cap traffic to downstream resources.
  scope: per function, concurrency limit.
  link: [reserve a subset of your account concurrency limit](../facts/lambda.md#lambda-faq-per-function-concurrency-control)
  link: [cap traffic rates to downstream resources](../facts/lambda.md#lambda-faq-per-function-concurrency-control)
lambda-faq-poll-controlled-by-role
  claim: Which DynamoDB table or Kinesis stream a function can poll is controlled by the function's role.
  scope: DynamoDB and Kinesis stream event sources.
  link: [Lambda function role](../facts/lambda.md#lambda-faq-poll-controlled-by-role)
lambda-faq-s3-notifications-indirect-sources
  claim: Services such as AWS CloudTrail can act as Lambda event sources by logging to Amazon S3 and using S3 bucket notifications to trigger Lambda functions.
  scope: event sources through S3 bucket notifications.
  link: [using S3 bucket notifications](../facts/lambda.md#lambda-faq-s3-notifications-indirect-sources)
lambda-faq-s3-trigger-resource-policy
  claim: When you configure an S3 bucket to send messages to a Lambda function, a resource policy rule is created that grants access.
  scope: S3 bucket notifications to a function.
  link: [resource policy rule](../facts/lambda.md#lambda-faq-s3-trigger-resource-policy)
lambda-faq-scaling-limit-per-function
  claim: The concurrency scaling limit is a function-level limit, so each function in the account scales independently of the others.
  scope: per function, concurrency scaling.
  link: [function-level limit](../facts/lambda.md#lambda-faq-scaling-limit-per-function)
lambda-faq-scaling-rate-1000-per-10s
  claim: Each synchronously invoked function can scale at a rate of up to 1000 concurrent executions every 10 seconds.
  scope: per function; maximum; not adjustable.
  link: [1000 concurrent executions every 10 seconds](../facts/lambda.md#lambda-faq-scaling-rate-1000-per-10s)
lambda-faq-sensitive-env-vars-kms
  claim: For sensitive values such as database passwords, AWS recommends client-side encryption with AWS KMS, storing the ciphertext in the environment variable; the function code then needs logic to decrypt it.
  scope: per function, environment variables.
  link: [client-side encryption using AWS Key Management Service](../facts/lambda.md#lambda-faq-sensitive-env-vars-kms)
  link: [ciphertext in your environment variable](../facts/lambda.md#lambda-faq-sensitive-env-vars-kms)
lambda-faq-snapstart-how
  claim: SnapStart snapshots the function's initialized memory and disk state and caches it; later invocations resume execution environments from that pre-initialized snapshot instead of initializing from scratch.
  scope: SnapStart.
  link: [pre-initialized snapshot](../facts/lambda.md#lambda-faq-snapstart-how)
lambda-faq-snapstart-java-no-charge
  claim: SnapStart pricing does not apply to supported Java managed runtimes, which can only cache a snapshot for up to 14 days.
  scope: Java managed runtimes; maximum.
  link: [up to 14 days](../facts/lambda.md#lambda-faq-snapstart-java-no-charge)
  link: [does not apply to supported Java managed runtimes](../facts/lambda.md#lambda-faq-snapstart-java-no-charge)
lambda-faq-snapstart-pc-exclusive
  claim: SnapStart and Provisioned Concurrency cannot be enabled at the same time on the same function.
  scope: per function.
  link: [cannot be enabled at the same time](../facts/lambda.md#lambda-faq-snapstart-pc-exclusive)
lambda-faq-snapstart-pricing
  claim: SnapStart is charged for caching a snapshot while the function version is active (a minimum of 3 hours, then per millisecond) and for each restore of the snapshot, with both prices depending on the function's memory.
  scope: per function version.
  link: [minimum of 3 hours](../facts/lambda.md#lambda-faq-snapstart-pricing)
lambda-faq-snapstart-runtimes
  claim: SnapStart supports Java 11 and newer, Python 3.12 and newer, and .NET 8 and newer.
  scope: SnapStart managed runtimes.
  link: [Java 11](../facts/lambda.md#lambda-faq-snapstart-runtimes)
  link: [Python 3.12](../facts/lambda.md#lambda-faq-snapstart-runtimes)
  link: [.NET 8](../facts/lambda.md#lambda-faq-snapstart-runtimes)
lambda-faq-snapstart-startup-gain
  claim: SnapStart can improve startup performance from several seconds to as low as sub-second for latency sensitive applications.
  scope: SnapStart.
  link: [sub-second](../facts/lambda.md#lambda-faq-snapstart-startup-gain)
lambda-faq-snapstart-vpc
  claim: A SnapStart function can be configured to access resources in a VPC.
  scope: SnapStart functions.
  link: [virtual private cloud (VPC)](../facts/lambda.md#lambda-faq-snapstart-vpc)
lambda-faq-snapstart-vs-pc
  claim: SnapStart is a best-effort optimization that does not guarantee the elimination of cold starts; for strict double-digit millisecond startup requirements AWS recommends Provisioned Concurrency.
  scope: SnapStart and Provisioned Concurrency.
  link: [best-effort optimization](../facts/lambda.md#lambda-faq-snapstart-vs-pc)
  link: [double-digit millisecond](../facts/lambda.md#lambda-faq-snapstart-vs-pc)
lambda-faq-sqs-poll-role-or-queue-policy
  claim: Which SQS queue a function can poll is controlled by the function role or by a resource policy on the queue; when both are present, the more restrictive one applies.
  scope: SQS event sources.
  link: [more restrictive of the two](../facts/lambda.md#lambda-faq-sqs-poll-role-or-queue-policy)
lambda-faq-stateless
  claim: Lambda's programming model is stateless; keeping functions stateless lets Lambda launch as many copies as needed, and the code reaches stateful data by calling services such as Amazon S3 or Amazon DynamoDB.
  scope: Lambda programming model.
  link: [stateless](../facts/lambda.md#lambda-faq-stateless)
lambda-faq-streams-retry-until-expiry
  claim: Events from Kinesis streams and DynamoDB streams are retried until the function succeeds or the data expires; both retain data for a minimum of 24 hours.
  scope: stream event sources.
  link: [succeeds or the data expires](../facts/lambda.md#lambda-faq-streams-retry-until-expiry)
  link: [minimum of 24 hours](../facts/lambda.md#lambda-faq-streams-retry-until-expiry)
lambda-faq-throttle-s3-retry-24-hours
  claim: When a function is invoked by Amazon S3 events, events that Lambda rejects may be retained and retried by S3 for 24 hours.
  scope: Amazon S3 event invocations.
  link: [24 hours](../facts/lambda.md#lambda-faq-throttle-s3-retry-24-hours)
lambda-faq-throttle-sync-429
  claim: When the concurrent executions limit is exceeded, synchronous invocations return a throttling error with a 429 error code.
  scope: synchronous invocations, throttling.
  link: [429 error code](../facts/lambda.md#lambda-faq-throttle-sync-429)
lambda-faq-timeout-15-minutes
  claim: A Lambda function can run up to 15 minutes per execution; the timeout can be set to any value between 1 second and 15 minutes.
  scope: per function, per execution; maximum; not adjustable.
  link: [15 minutes](../facts/lambda.md#lambda-faq-timeout-15-minutes)
  link: [1 second](../facts/lambda.md#lambda-faq-timeout-15-minutes)
lambda-faq-update-brief-window
  claim: A function stays available while you update it; for a brief window, typically less than a minute, requests may be served by either the old or the new version.
  scope: per function, code or configuration update.
  link: [typically less than a minute](../facts/lambda.md#lambda-faq-update-brief-window)
lambda-faq-versioning
  claim: Lambda supports versioning: by default each function has a single current version, and clients can call a specific version or get the latest implementation.
  scope: per function; default.
  link: [a single, current version](../facts/lambda.md#lambda-faq-versioning)
lambda-faq-vpc-ipv4-default-ipv6-option
  claim: By default a function talks to resources in a dual-stack VPC over IPv4; it can be configured to use IPv6.
  scope: per function; default; adjustable.
  link: [over IPv4](../facts/lambda.md#lambda-faq-vpc-ipv4-default-ipv6-option)
lambda-faq-vpc-no-internet-by-default
  claim: A Lambda function configured to access resources in a VPC does not have access to the internet as its default configuration.
  scope: per VPC-attached function; default; adjustable.
  link: [not have access to the internet](../facts/lambda.md#lambda-faq-vpc-no-internet-by-default)
lambda-faq-vpc-subnet-security-group
  claim: To reach resources in a VPC, you specify the subnet and security group in the function configuration.
  scope: VPC-attached functions.
  link: [subnet and security group](../facts/lambda.md#lambda-faq-vpc-subnet-security-group)
lambda-fargate-long-running-lambda-short
  claim: The decision guide positions Fargate as ideal for long-running applications, microservices or batch processing, while Lambda functions are optimized for short-lived, event-driven tasks with a maximum execution time of 15 minutes per invocation.
  scope: Fargate versus Lambda.
  link: [long-running applications, microservices, or batch processing](../facts/lambda.md#lambda-fargate-long-running-lambda-short)
  link: [short-lived, event-driven tasks](../facts/lambda.md#lambda-fargate-long-running-lambda-short)
lambda-fargate-no-execution-time-limit
  claim: Containers in Fargate can run indefinitely because Fargate has no hard limit on execution time, while a Lambda function has a maximum execution time of 15 minutes per invocation.
  scope: per Fargate task container, compared with one Lambda invocation; maximum.
  link: [no hard limit on execution time](../facts/lambda.md#lambda-fargate-no-execution-time-limit)
  link: [15 minutes per invocation](../facts/lambda.md#lambda-fargate-no-execution-time-limit)
lambda-fault-tolerant-other-az
  claim: Lambda is fault-tolerant: if a service invokes a function during a service disruption, Lambda invokes the function in a different Availability Zone, and if the function throws an error Lambda retries the invocation.
  scope: per Region.
  link: [in a different Availability Zone](../facts/lambda.md#lambda-fault-tolerant-other-az)
  link: [fault-tolerant and designed to handle failures](../facts/lambda.md#lambda-fault-tolerant-other-az)
  say: it runs the function in another Availability Zone
lambda-file-descriptors
  claim: A Lambda execution environment is limited to 1,024 file descriptors; Lambda Managed Instances use a higher file descriptor limit of 4,096.
  scope: per execution environment; maximum; not adjustable; Lambda Managed Instances use 4,096.
  link: [1,024](../facts/lambda.md#lambda-file-descriptors)
  link: [4,096](../facts/lambda.md#lambda-file-descriptors)
lambda-filter-five-ored-discard
  claim: By default an event source mapping can have up to 5 filters, which are logically ORed; a record that satisfies none of them is discarded by Lambda and not sent to the function. A quota increase allows up to 10 filters for each event source.
  scope: per event source mapping; default; adjustable; a quota increase allows up to 10 filters for each event source.
  link: [up to five different filters](../facts/lambda.md#lambda-filter-five-ored-discard)
  link: [up to 10 filters](../facts/lambda.md#lambda-filter-five-ored-discard)
  link: [logically ORed together](../facts/lambda.md#lambda-filter-five-ored-discard)
  link: [Lambda discards the record](../facts/lambda.md#lambda-filter-five-ored-discard)
  say: five filters by default | up to ten with a quota increase
lambda-filter-sources-not-documentdb
  claim: Event filtering works only with certain event source mappings, and Lambda does not support event filtering for Amazon DocumentDB.
  scope: event source mapping filters.
  link: [works only with certain event source mappings](../facts/lambda.md#lambda-filter-sources-not-documentdb)
  link: [doesn't support event filtering for Amazon DocumentDB](../facts/lambda.md#lambda-filter-sources-not-documentdb)
  say: filtering works only with some event source mappings
lambda-filter-sqs-removes-unmatched
  claim: For an Amazon SQS event source, if a message does not satisfy the filter criteria, Lambda automatically removes the message from the queue, so you do not delete it manually.
  scope: Amazon SQS event source mapping with filters.
  link: [automatically removes the message from the queue](../facts/lambda.md#lambda-filter-sqs-removes-unmatched)
  link: [You don't have to manually delete these messages](../facts/lambda.md#lambda-filter-sqs-removes-unmatched)
  say: Lambda deletes it from the queue for you
lambda-free-tier
  claim: The Lambda free tier includes one million requests and 400,000 GB-seconds per month.
  scope: per account, per month.
  link: [one million requests](../facts/lambda.md#lambda-free-tier)
  link: [400,000 GB-seconds per month](../facts/lambda.md#lambda-free-tier)
lambda-function-single-handler
  claim: The function handler is the method in your code that processes events; a Lambda function can contain many methods but can only have one handler.
  scope: per function; fixed.
  link: [only have one handler](../facts/lambda.md#lambda-function-single-handler)
  link: [method in your function code that processes events](../facts/lambda.md#lambda-function-single-handler)
  say: only one handler per function
lambda-function-url-403-without-policy
  claim: If a function's resource-based policy does not grant lambda:InvokeFunctionUrl and lambda:InvokeFunction, callers get a 403 Forbidden error from the function URL, even when the auth type is NONE.
  scope: Lambda function URL.
  link: [403 Forbidden](../facts/lambda.md#lambda-function-url-403-without-policy)
  link: [uses the NONE auth type](../facts/lambda.md#lambda-function-url-403-without-policy)
  say: four oh three, forbidden
lambda-function-url-auth-types
  claim: A function URL's AuthType is either AWS_IAM, where IAM authenticates and authorizes requests using the principal's identity policy and the function's resource-based policy, or NONE, where Lambda performs no authentication but the resource-based policy must still grant public access.
  scope: Lambda function URL.
  link: [AWS_IAM](../facts/lambda.md#lambda-function-url-auth-types)
  link: [Lambda doesn't perform any authentication](../facts/lambda.md#lambda-function-url-auth-types)
  link: [must grant public access](../facts/lambda.md#lambda-function-url-auth-types)
  say: AWS IAM auth
lambda-functions-vs-microvms-best-for
  claim: Lambda Functions are best for request-response or event-driven workloads such as APIs, data processing and automation; Lambda MicroVMs are best for persistent environments that run untrusted code produced by users or AI.
  scope: Lambda Functions versus Lambda MicroVMs.
  link: [Request-response or event-driven workloads](../facts/lambda.md#lambda-functions-vs-microvms-best-for)
  link: [running user or AI-produced untrusted code](../facts/lambda.md#lambda-functions-vs-microvms-best-for)
lambda-furl-429-no-queue
  claim: A function URL scales only up to the function's concurrency limit; after that Lambda answers extra requests with HTTP 429, and there is no built-in queuing, whereas API Gateway adds request queuing and throttling controls.
  scope: Lambda function URLs.
  link: [HTTP 429 responses](../facts/lambda.md#lambda-furl-429-no-queue)
  link: [There's no built-in queuing mechanism](../facts/lambda.md#lambda-furl-429-no-queue)
lambda-furl-auth-public-or-iam
  claim: A function URL endpoint can be either public (no authentication) or require IAM authentication; API Gateway provides a more comprehensive range of authentication options: as well as IAM authentication, Lambda authorizers, Amazon Cognito user pools and OAuth flows.
  scope: Lambda function URLs.
  link: [public (no authentication)](../facts/lambda.md#lambda-furl-auth-public-or-iam)
  link: [require IAM authentication](../facts/lambda.md#lambda-furl-auth-public-or-iam)
lambda-furl-cors-no-validation
  claim: Function URLs include built-in CORS support but do not offer request transformation or validation; the client receives the response exactly as the function returns it.
  scope: Lambda function URLs.
  link: [built-in cross-origin resource sharing (CORS) support](../facts/lambda.md#lambda-furl-cors-no-validation)
  link: [don't offer request transformation or validation](../facts/lambda.md#lambda-furl-cors-no-validation)
lambda-furl-no-endpoint-charge
  claim: Function URLs follow standard Lambda pricing: you pay only for invocations and compute time, with no additional charge for the URL endpoint itself.
  scope: Lambda function URLs.
  link: [no additional charges for the URL endpoint](../facts/lambda.md#lambda-furl-no-endpoint-charge)
lambda-furl-none-public-invoke
  claim: When a function URL uses auth type NONE and the function's resource-based policy grants public access, any unauthenticated user who has the URL can invoke the function.
  scope: Lambda function URLs, auth type NONE; the resource-based policy must grant public access.
  link: [any unauthenticated user with your function URL](../facts/lambda.md#lambda-furl-none-public-invoke)
lambda-furl-recommended-simple-apps
  claim: AWS recommends Lambda function URLs for simple applications or prototyping that need only basic authentication and request/response handling and want minimal cost and complexity.
  scope: HTTP invocation of a Lambda function.
  link: [simple applications or prototyping](../facts/lambda.md#lambda-furl-recommended-simple-apps)
  say: simple apps and prototypes
lambda-getfunction-api-rate
  claim: The GetFunction API is limited to 100 requests per second and cannot be increased.
  scope: per account, per Region, GetFunction API; maximum; not adjustable.
  link: [100 requests per second](../facts/lambda.md#lambda-getfunction-api-rate)
lambda-getpolicy-api-rate
  claim: The GetPolicy API is limited to 15 requests per second and cannot be increased.
  scope: per account, per Region, GetPolicy API; maximum; not adjustable.
  link: [15 requests per second](../facts/lambda.md#lambda-getpolicy-api-rate)
lambda-hyperplane-eni-65000-connections
  claim: Each Hyperplane ENI supports up to 65,000 connections/ports; above that, Lambda scales the number of ENIs automatically based on network traffic and concurrency.
  scope: per Hyperplane ENI; maximum; not adjustable; Lambda adds ENIs automatically above this.
  link: [65,000 connections/ports](../facts/lambda.md#lambda-hyperplane-eni-65000-connections)
  say: sixty-five thousand connections
lambda-hyperplane-eni-shared-by-subnet-sg
  claim: Lambda creates a Hyperplane ENI the first time a function is attached to a VPC with a particular subnet and security group combination, and other functions in the account that use the same combination can share that ENI.
  scope: per subnet and security group combination.
  link: [Lambda creates a Hyperplane ENI](../facts/lambda.md#lambda-hyperplane-eni-shared-by-subnet-sg)
  link: [same subnet and security group combination](../facts/lambda.md#lambda-hyperplane-eni-shared-by-subnet-sg)
  say: Lambda creates a Hyperplane ENI
lambda-idempotent-functions
  claim: The same event can be received more than once, so functions should be idempotent: receiving an event several times does not change the result beyond the first time. A DynamoDB table that tracks recently processed identifiers is the guide's way to implement this.
  scope: per function.
  link: [does not change the result](../facts/lambda.md#lambda-idempotent-functions)
  link: [DynamoDB table to track recently processed identifiers](../facts/lambda.md#lambda-idempotent-functions)
  say: the same event twice gives the same result
lambda-init-10-seconds-exceptions
  claim: The 10-second Init timeout does not apply to functions using provisioned concurrency, SnapStart or Lambda Managed Instances; their initialization code can run for up to 15 minutes, with a time limit of 130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher.
  scope: per execution environment, Init phase; maximum; not adjustable; functions using provisioned concurrency, SnapStart or Lambda Managed Instances.
  link: [provisioned concurrency, SnapStart, or Lambda Managed Instances](../facts/lambda.md#lambda-init-10-seconds-exceptions)
  link: [up to 15 minutes](../facts/lambda.md#lambda-init-10-seconds-exceptions)
  link: [130 seconds or the configured function timeout (maximum 900 seconds), whichever is higher](../facts/lambda.md#lambda-init-10-seconds-exceptions)
lambda-init-phase-10-seconds
  claim: The Init phase is limited to 10 seconds; if it does not complete within 10 seconds, Lambda retries the Init phase at the first invocation with the configured function timeout. The 10-second timeout does not apply to functions that use provisioned concurrency, SnapStart or Lambda Managed Instances.
  scope: per execution environment, Init phase; maximum; not adjustable; not for functions that use provisioned concurrency, SnapStart or Lambda Managed Instances.
  link: [10 seconds](../facts/lambda.md#lambda-init-phase-10-seconds)
lambda-interface-endpoint-pricing
  claim: There is no additional Lambda cost to access a function through an interface endpoint, but standard AWS PrivateLink pricing applies: each hour the endpoint is provisioned in each Availability Zone and the data processed through it.
  scope: interface endpoint for Lambda.
  link: [no additional cost to access a Lambda function](../facts/lambda.md#lambda-interface-endpoint-pricing)
  link: [Standard pricing for AWS PrivateLink applies](../facts/lambda.md#lambda-interface-endpoint-pricing)
  say: no extra Lambda charge
lambda-interface-endpoint-private-invoke
  claim: An interface VPC endpoint (AWS PrivateLink) for Lambda lets resources in a VPC call Lambda APIs, including Invoke, without an internet gateway, NAT device, VPN connection or Direct Connect, and without public IP addresses; the traffic does not leave the AWS network.
  scope: interface endpoint for Lambda.
  link: [interface VPC endpoint](../facts/lambda.md#lambda-interface-endpoint-private-invoke)
  link: [without an internet gateway, NAT device](../facts/lambda.md#lambda-interface-endpoint-private-invoke)
  link: [does not leave the AWS network](../facts/lambda.md#lambda-interface-endpoint-private-invoke)
  say: an interface VPC endpoint
lambda-invocation-15-minutes-10240-mb
  claim: Code can run for up to 15 minutes in a single invocation (up to 90 minutes for Lambda Managed Instances functions invoked asynchronously or through any event source mapping except Amazon MQ and Amazon DocumentDB), and a single function can use up to 10,240 MB of memory.
  scope: per invocation and per function; maximum; not adjustable; 90 minutes only for Lambda Managed Instances functions invoked asynchronously or through an event source mapping other than Amazon MQ and Amazon DocumentDB.
  link: [up to 15 minutes](../facts/lambda.md#lambda-invocation-15-minutes-10240-mb)
  link: [up to 10,240 MB](../facts/lambda.md#lambda-invocation-15-minutes-10240-mb)
  link: [up to 90 minutes](../facts/lambda.md#lambda-invocation-15-minutes-10240-mb)
lambda-invoke-phase-limited-by-timeout
  claim: The function's timeout setting limits the duration of the entire Invoke phase, so the function and all extensions must complete within the timeout.
  scope: per invocation.
  link: [limits the duration of the entire Invoke phase](../facts/lambda.md#lambda-invoke-phase-limited-by-timeout)
  link: [the function and all extensions](../facts/lambda.md#lambda-invoke-phase-limited-by-timeout)
  say: the timeout covers the whole invoke phase
lambda-kinesis-bad-record-block-one-week
  claim: With the default settings, a bad record can block processing on its Kinesis shard for up to one week; when the error handling measures fail, Lambda discards the records and continues processing batches from the stream.
  scope: Kinesis event source mapping, per shard; default; adjustable; set a retry limit and a maximum record age to avoid this.
  link: [up to one week](../facts/lambda.md#lambda-kinesis-bad-record-block-one-week)
  link: [Lambda discards the records and continues processing batches](../facts/lambda.md#lambda-kinesis-bad-record-block-one-week)
  say: up to one week
lambda-kinesis-batch-size-100
  claim: For a Kinesis event source mapping, the batch size defaults to 100 records and can be at most 10,000.
  scope: per Kinesis event source mapping; default; adjustable.
  link: [100](../facts/lambda.md#lambda-kinesis-batch-size-100)
  link: [10,000](../facts/lambda.md#lambda-kinesis-batch-size-100)
lambda-kinesis-batching-window-5-minutes-6-mb
  claim: A stream event source can buffer records for up to 5 minutes with a batching window; Lambda invokes when the batch is full, the window expires, or the batch reaches the 6 MB payload limit.
  scope: per event source mapping, Kinesis; maximum; adjustable.
  link: [up to 5 minutes](../facts/lambda.md#lambda-kinesis-batching-window-5-minutes-6-mb)
  link: [payload limit of 6 MB](../facts/lambda.md#lambda-kinesis-batching-window-5-minutes-6-mb)
lambda-kinesis-bisect-default-false
  claim: For a Kinesis event source mapping, BisectBatchOnFunctionError (split a failed batch) is off by default (false).
  scope: per Kinesis event source mapping; default; adjustable.
  link: [false](../facts/lambda.md#lambda-kinesis-bisect-default-false)
lambda-kinesis-failure-destination-sqs-sns
  claim: A Kinesis event source mapping can send discarded records to an Amazon SQS queue or Amazon SNS topic destination.
  scope: per Kinesis event source mapping.
  link: [Amazon SQS queue or Amazon SNS topic](../facts/lambda.md#lambda-kinesis-failure-destination-sqs-sns)
lambda-kinesis-in-order-stops-on-error
  claim: Lambda processes the records of each Kinesis shard in order and stops processing additional records in a shard if the function returns an error; with more shards, more batches are processed at once, which lowers the impact of errors on concurrency.
  scope: per shard, Kinesis event source mapping.
  link: [stops processing additional records in a shard](../facts/lambda.md#lambda-kinesis-in-order-stops-on-error)
lambda-kinesis-max-record-age
  claim: For a Kinesis event source mapping, MaximumRecordAgeInSeconds defaults to -1, which means infinite: Lambda does not discard records (Kinesis data retention still applies); the minimum is -1 and the maximum 604,800.
  scope: per Kinesis event source mapping; default; adjustable; Kinesis Data Streams data retention settings still apply.
  link: [-1 means infinite](../facts/lambda.md#lambda-kinesis-max-record-age)
  link: [604,800](../facts/lambda.md#lambda-kinesis-max-record-age)
lambda-kinesis-max-retry-attempts
  claim: For a Kinesis event source mapping, MaximumRetryAttempts defaults to -1, which means infinite: failed records are retried until the record expires; the minimum is -1 and the maximum 10,000.
  scope: per Kinesis event source mapping; default; adjustable.
  link: [failed records are retried until the record expires](../facts/lambda.md#lambda-kinesis-max-retry-attempts)
  link: [10,000](../facts/lambda.md#lambda-kinesis-max-retry-attempts)
lambda-kinesis-on-failure-destination-targets
  claim: To retain records of failed invocations from a Kinesis event source mapping, you add a destination, which can be an Amazon SNS topic, an Amazon SQS queue, an Amazon S3 bucket, or Kafka.
  scope: Kinesis event source mapping.
  link: [Amazon SNS topic, Amazon SQS queue](../facts/lambda.md#lambda-kinesis-on-failure-destination-targets)
  link: [or Kafka as a destination](../facts/lambda.md#lambda-kinesis-on-failure-destination-targets)
  link: [Amazon S3 bucket](../facts/lambda.md#lambda-kinesis-on-failure-destination-targets)
  say: an SNS topic, an SQS queue, an S3 bucket or Kafka
lambda-kinesis-parallelization-factor-1-to-10
  claim: The parallelization factor sets how many concurrent batches Lambda polls from one Kinesis shard, from 1 (default) to 10; with a factor of 2, 100 shards can drive up to 200 concurrent invocations.
  scope: per Kinesis event source mapping, per shard; default; adjustable.
  link: [from 1 (default) to 10](../facts/lambda.md#lambda-kinesis-parallelization-factor-1-to-10)
  link: [200 concurrent Lambda invocations at maximum to process 100 Kinesis data shards](../facts/lambda.md#lambda-kinesis-parallelization-factor-1-to-10)
lambda-kinesis-poll-once-per-second
  claim: With a standard iterator, Lambda polls each Kinesis shard at a base rate of once per second and shares the shard's read throughput with other consumers.
  scope: per shard, standard iterator.
  link: [base rate of once per second](../facts/lambda.md#lambda-kinesis-poll-once-per-second)
lambda-kinesis-tumbling-window-900
  claim: For a Kinesis event source mapping, TumblingWindowInSeconds can be set from a minimum of 0 to a maximum of 900.
  scope: per Kinesis event source mapping; maximum; not adjustable.
  link: [900](../facts/lambda.md#lambda-kinesis-tumbling-window-900)
lambda-layer-cross-account-policy
  claim: Layers can be shared across functions in your account, and to use a layer from another account, the owner of that account must grant your account permission in a resource-based policy.
  scope: Lambda layer sharing.
  link: [any number of functions in your account](../facts/lambda.md#lambda-layer-cross-account-policy)
  link: [grant your account permission](../facts/lambda.md#lambda-layer-cross-account-policy)
  say: share it across functions
lambda-layer-version-immutable
  claim: A layer version is an immutable snapshot of a layer; each published update creates a new layer version with an incremented version number and its own ARN.
  scope: Lambda layer version.
  link: [an immutable snapshot](../facts/lambda.md#lambda-layer-version-immutable)
  link: [creates a new layer version](../facts/lambda.md#lambda-layer-version-immutable)
  say: each layer version is immutable
lambda-layer-zip-contents
  claim: A Lambda layer is a .zip file archive with supplementary code or data, usually library dependencies, a custom runtime or configuration files; Lambda extracts the layer contents into the /opt directory of the execution environment.
  scope: Lambda layer.
  link: [.zip file archive that contains supplementary code](../facts/lambda.md#lambda-layer-zip-contents)
  link: [into the /opt directory](../facts/lambda.md#lambda-layer-zip-contents)
  say: a zip archive with extra code or data
lambda-layers-five-and-250-mb
  claim: A function can use up to five layers, and the unzipped size of the function plus all its layers cannot exceed the 250 MB unzipped deployment package quota.
  scope: per function, layers; maximum; not adjustable.
  link: [up to five layers](../facts/lambda.md#lambda-layers-five-and-250-mb)
  link: [250 MB](../facts/lambda.md#lambda-layers-five-and-250-mb)
lambda-layers-per-function
  claim: A function can have at most 5 layers.
  scope: per function; maximum; not adjustable.
  link: [5 layers](../facts/lambda.md#lambda-layers-per-function)
lambda-layers-zip-only
  claim: Layers work only with functions deployed as a .zip file archive (up to five per function); a container-image function must package its runtime and dependencies in the image.
  scope: per function, layers; maximum.
  link: [up to five layers per function](../facts/lambda.md#lambda-layers-zip-only)
  link: [use layers only with Lambda functions](../facts/lambda.md#lambda-layers-zip-only)
lambda-lifecycle-phases
  claim: An execution environment goes through an Init phase (Lambda starts extensions, bootstraps the runtime and runs the function's static code), an Invoke phase (Lambda sends an Invoke event to the runtime and each extension) and a Shutdown phase (Lambda sends a Shutdown event to each registered external extension before it shuts the runtime down).
  scope: per execution environment.
  link: [Init phase](../facts/lambda.md#lambda-lifecycle-phases)
  link: [sends an Invoke event to the runtime](../facts/lambda.md#lambda-lifecycle-phases)
  link: [sends a Shutdown event](../facts/lambda.md#lambda-lifecycle-phases)
  say: the init phase
lambda-managed-instances-best-suited-row
  claim: Lambda (default) suits functions with bursty traffic that can handle some cold-start time, or without sustained load, that benefit from scale to zero; Lambda Managed Instances suit high-volume, predictable-traffic functions that want the flexibility, pricing plans and hardware options of EC2.
  scope: Lambda (default) versus Lambda Managed Instances.
  link: [benefit from scale to zero](../facts/lambda.md#lambda-managed-instances-best-suited-row)
  link: [High volume predictable traffic functions](../facts/lambda.md#lambda-managed-instances-best-suited-row)
lambda-managed-instances-doubling-five-minutes
  claim: Lambda Managed Instances scale to handle traffic doubling within five minutes by default.
  scope: Lambda Managed Instances; default; adjustable.
  link: [traffic doubling within five minutes by default](../facts/lambda.md#lambda-managed-instances-doubling-five-minutes)
lambda-managed-instances-fee-and-ec2-discounts
  claim: Lambda Managed Instances use EC2-based pricing with a 15% management fee on top of the EC2 instance cost, and this pricing supports EC2 Savings Plans, Reserved Instances and other discounts applied to your EC2 usage.
  scope: Lambda Managed Instances; EC2 discounts apply to the EC2 compute, not to the management fee.
  link: [15% management fee](../facts/lambda.md#lambda-managed-instances-fee-and-ec2-discounts)
  say: a fifteen percent management fee
lambda-managed-instances-isolation-row
  claim: Lambda (default) is multi-tenant and isolates execution environments on shared Lambda fleets with Firecracker MicroVMs; Lambda Managed Instances run in your account and use EC2 Nitro for isolation, with capacity providers as the security boundary and functions running in containers within instances.
  scope: Lambda (default) versus Lambda Managed Instances.
  link: [using Firecracker MicroVM technology](../facts/lambda.md#lambda-managed-instances-isolation-row)
  link: [Capacity providers serve as the security boundary](../facts/lambda.md#lambda-managed-instances-isolation-row)
lambda-managed-instances-multi-concurrency-row
  claim: With Lambda (default) one execution environment supports at most one invocation at a time; with Lambda Managed Instances one execution environment can handle multiple invocations simultaneously, which raises throughput especially for IO-heavy applications.
  scope: per execution environment.
  link: [a maximum of one invocation at a time](../facts/lambda.md#lambda-managed-instances-multi-concurrency-row)
  link: [multiple invocations simultaneously](../facts/lambda.md#lambda-managed-instances-multi-concurrency-row)
lambda-managed-instances-no-duration-charge
  claim: Lambda Managed Instances functions do not pay separately for the execution duration of each request, unlike default Lambda functions.
  scope: Lambda Managed Instances.
  link: [not be paying separately for the execution duration](../facts/lambda.md#lambda-managed-instances-no-duration-charge)
lambda-managed-instances-pricing-components
  claim: Lambda Managed Instances pricing has three parts: $0.20 per million requests, a 15% management fee on the EC2 On-Demand instance price, and standard EC2 instance charges.
  scope: Lambda Managed Instances.
  link: [$0.20 per million requests](../facts/lambda.md#lambda-managed-instances-pricing-components)
  link: [15% premium on the EC2 on-demand instance price](../facts/lambda.md#lambda-managed-instances-pricing-components)
lambda-managed-instances-savings-plans
  claim: Lambda Managed Instances can use EC2 pricing options including EC2 Instance Savings Plans, Compute Savings Plans and Reserved Instances.
  scope: Lambda Managed Instances.
  link: [EC2 Instance Savings Plans](../facts/lambda.md#lambda-managed-instances-savings-plans)
lambda-managed-instances-scaling-row
  claim: Lambda (default) scales when no free execution environment is available for an incoming invocation (a cold start) and scales to zero without traffic; Lambda Managed Instances do not scale when invocations arrive and do not support cold starts: they scale asynchronously based on CPU resource utilization and multi-concurrency saturation, and scale to the configured minimum execution environments without traffic.
  scope: Lambda (default) versus Lambda Managed Instances.
  link: [Scales to zero without traffic](../facts/lambda.md#lambda-managed-instances-scaling-row)
  link: [CPU resource utilization and multi-concurrency saturation](../facts/lambda.md#lambda-managed-instances-scaling-row)
lambda-managed-instances-three-instances-default
  claim: When you publish a function version with a capacity provider, Lambda launches three Managed Instances by default for AZ resiliency and starts three execution environments before marking the version ACTIVE; if the function is attached to an existing capacity provider that already runs other functions, Lambda might not launch new instances when the available instances have capacity.
  scope: per function version published to a capacity provider, Lambda Managed Instances; a new capacity provider; an existing one with spare capacity might launch no new instances.
  link: [three instances by default](../facts/lambda.md#lambda-managed-instances-three-instances-default)
lambda-managed-instances-timeout-90-min
  claim: For functions using AWS Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum timeout of 5,400 seconds (90 minutes).
  scope: per function on Lambda Managed Instances; maximum; not adjustable; asynchronous invocations and event source mapping invocations, except Amazon MQ and Amazon DocumentDB.
  link: [5,400 seconds](../facts/lambda.md#lambda-managed-instances-timeout-90-min)
  link: [90 minutes](../facts/lambda.md#lambda-managed-instances-timeout-90-min)
lambda-mb-means-1024-kb
  claim: In the Lambda documentation, log messages and console, MB (rather than MiB) means 1,024 KB.
  scope: Lambda documentation, logs and console.
  link: [MB (rather than MiB) to refer to 1,024 KB](../facts/lambda.md#lambda-mb-means-1024-kb)
lambda-memory-default
  claim: The default memory setting, 128 MB, is the lowest possible setting; AWS recommends it only for simple functions that transform and route events.
  scope: per function; default; adjustable.
  link: [128 MB](../facts/lambda.md#lambda-memory-default)
lambda-memory-range
  claim: A Lambda function's memory can be set between 128 MB and 10,240 MB, in 1-MB increments.
  scope: per function; maximum; not adjustable.
  link: [128 MB](../facts/lambda.md#lambda-memory-range)
  link: [10,240 MB](../facts/lambda.md#lambda-memory-range)
  link: [1-MB increments](../facts/lambda.md#lambda-memory-range)
  say: one hundred twenty-eight megabytes | ten thousand two hundred forty megabytes | one-megabyte increments
lambda-memory-tuning-cpu-bound
  claim: For CPU-bound and IO-bound functions, increasing the memory can help resolve compute or network bottlenecks; AWS recommends the open source AWS Lambda Power Tuning tool, which runs the function at different memory allocations and measures performance, to find the right memory configuration.
  scope: Lambda memory configuration.
  link: [increasing the memory can help resolve the compute](../facts/lambda.md#lambda-memory-tuning-cpu-bound)
  link: [AWS Lambda Power Tuning](../facts/lambda.md#lambda-memory-tuning-cpu-bound)
  say: more memory can fix compute bottlenecks
lambda-microvm-max-duration-8-hours
  claim: A Lambda MicroVM can run for at most 8 hours (28,800 seconds), and this quota is not adjustable.
  scope: per MicroVM; maximum; not adjustable.
  link: [8 hours](../facts/lambda.md#lambda-microvm-max-duration-8-hours)
  link: [28,800 seconds](../facts/lambda.md#lambda-microvm-max-duration-8-hours)
lambda-microvms-priced-per-instance-second
  claim: Lambda Functions are priced per request and execution duration, while Lambda MicroVMs are priced per instance-second.
  scope: Lambda MicroVMs.
  link: [priced per instance-second](../facts/lambda.md#lambda-microvms-priced-per-instance-second)
lambda-monolith-breaks-least-privilege
  claim: A monolithic Lambda function makes least privilege hard to enforce, because its execution role must allow every resource needed for every path; the preferred alternative maps a single Lambda function to a single, well-defined task.
  scope: Lambda application design.
  link: [Hard to enforce least privilege](../facts/lambda.md#lambda-monolith-breaks-least-privilege)
  link: [a single, well-defined task](../facts/lambda.md#lambda-monolith-breaks-least-privilege)
  say: least privilege becomes hard
lambda-mq-default-concurrency
  claim: Functions linked to an Amazon MQ event source mapping have a default maximum concurrency of 5 concurrent instances for Apache ActiveMQ and 1 for RabbitMQ; reserved or provisioned concurrency does not change this.
  scope: per function with an Amazon MQ event source mapping; default; adjustable; increase by contacting Support.
  link: [5](../facts/lambda.md#lambda-mq-default-concurrency)
  link: [1](../facts/lambda.md#lambda-mq-default-concurrency)
lambda-multiple-triggers-one-per-event
  claim: A function can have multiple triggers; each trigger invokes the function independently, and each event that Lambda passes to the function has data from only one trigger.
  scope: per function.
  link: [can have multiple triggers](../facts/lambda.md#lambda-multiple-triggers-one-per-event)
  link: [has data from only one trigger](../facts/lambda.md#lambda-multiple-triggers-one-per-event)
  say: one function can have several triggers
lambda-network-bandwidth-per-env
  claim: Network bandwidth per execution environment is 625 Mbps.
  scope: per execution environment; maximum; adjustable; for functions not attached to a VPC, an increase can be requested through the Service Quotas console.
  link: [625 Mbps](../facts/lambda.md#lambda-network-bandwidth-per-env)
lambda-network-bandwidth-raised
  claim: After an approved increase, for functions not attached to a VPC, network bandwidth scales with memory starting at 2,048 MB and reaches a maximum of up to 3,000 Mbps at 10,240 MB.
  scope: per execution environment, functions not attached to a VPC; maximum; adjustable; after approval of a Service Quotas increase.
  link: [3,000 Mbps](../facts/lambda.md#lambda-network-bandwidth-raised)
  link: [2,048 MB](../facts/lambda.md#lambda-network-bandwidth-raised)
lambda-new-account-reduced-quotas
  claim: New AWS accounts have reduced concurrency and memory quotas for Lambda functions, and AWS raises these quotas automatically based on usage.
  scope: per new AWS account; default.
  link: [reduced concurrency and memory quotas](../facts/lambda.md#lambda-new-account-reduced-quotas)
  link: [raises these quotas automatically](../facts/lambda.md#lambda-new-account-reduced-quotas)
lambda-no-pay-for-idle-capacity
  claim: Lambda pricing suits unpredictable or bursty traffic: you pay only for actual function invocations and execution time, and you do not provision or pay for idle capacity.
  scope: Lambda pricing model.
  link: [pay for idle capacity](../facts/lambda.md#lambda-no-pay-for-idle-capacity)
  say: no charge for idle capacity
lambda-one-vcpu-at-1769-mb
  claim: At 1,769 MB of memory, a function has the equivalent of one vCPU.
  scope: per function.
  link: [1,769 MB](../facts/lambda.md#lambda-one-vcpu-at-1769-mb)
  link: [one vCPU](../facts/lambda.md#lambda-one-vcpu-at-1769-mb)
lambda-os-only-runtime-other-languages
  claim: To use other languages in Lambda, such as Go or Rust, you use an OS-only runtime, and you can deploy other languages by implementing a custom runtime alongside the function code or in a layer.
  scope: Lambda runtimes.
  link: [use an OS-only runtime](../facts/lambda.md#lambda-os-only-runtime-other-languages)
  link: [implementing a custom runtime](../facts/lambda.md#lambda-os-only-runtime-other-languages)
  say: an OS-only runtime
lambda-package-250-mb-unzipped
  claim: The unzipped contents of a deployment package, including layers and custom runtimes, are limited to 250 MB.
  scope: per function, deployment package contents including layers and custom runtimes, unzipped; maximum; not adjustable.
  link: [250 MB](../facts/lambda.md#lambda-package-250-mb-unzipped)
lambda-payload-async
  claim: An asynchronous invocation's payload is limited to 1 MB.
  scope: per invocation (asynchronous); maximum; not adjustable.
  link: [1 MB](../facts/lambda.md#lambda-payload-async)
lambda-payload-streamed-response
  claim: A streamed response (synchronous) is limited to 200 MB.
  scope: per invocation (synchronous), streamed response; maximum; not adjustable.
  link: [200 MB](../facts/lambda.md#lambda-payload-streamed-response)
lambda-payload-sync
  claim: A synchronous invocation's request and response payloads are each limited to 6 MB.
  scope: per invocation (synchronous), request and response each; maximum; not adjustable.
  link: [6 MB](../facts/lambda.md#lambda-payload-sync)
lambda-pc-autoscaling-burst-3-minutes
  claim: Both Application Auto Scaling alarms for provisioned concurrency use the average statistic by default; Application Auto Scaling needs a burst load to last at least 3 minutes before it provisions more environments, and both CloudWatch alarms need 3 data points that hit the target average. For quick bursts of traffic, the Maximum statistic can be more effective than Average.
  scope: per provisioned concurrency target tracking policy; alarms use the average statistic by default.
  link: [at least 3 minutes](../facts/lambda.md#lambda-pc-autoscaling-burst-3-minutes)
  link: [3 data points](../facts/lambda.md#lambda-pc-autoscaling-burst-3-minutes)
lambda-pc-autoscaling-target-10-to-90
  claim: With Application Auto Scaling, a target tracking policy can keep provisioned concurrency utilization at any value between 10% and 90%; the documentation example uses 70 percent.
  scope: per alias or version with provisioned concurrency; maximum; adjustable; target tracking scaling policy.
  link: [between 10% and 90%](../facts/lambda.md#lambda-pc-autoscaling-target-10-to-90)
  link: [70 percent](../facts/lambda.md#lambda-pc-autoscaling-target-10-to-90)
lambda-pc-costs-while-idle
  claim: Provisioned concurrency keeps a set number of function instances warm to cut cold-start latency, but it increases costs: you pay for the provisioned instances even when they are not handling requests.
  scope: provisioned concurrency.
  link: [it increases costs](../facts/lambda.md#lambda-pc-costs-while-idle)
lambda-pc-event-source-alias
  claim: If a function has an event source, the event source must point to the alias or version that has provisioned concurrency; otherwise the function does not use the provisioned concurrency environments.
  scope: provisioned concurrency with an event source.
  link: [points to the correct function alias or version](../facts/lambda.md#lambda-pc-event-source-alias)
  link: [won't use provisioned concurrency environments](../facts/lambda.md#lambda-pc-event-source-alias)
  say: point the event source at the right alias or version
lambda-pc-excess-at-on-demand-rate
  claim: If a function exceeds its configured provisioned concurrency, the excess executions are billed at the on-demand Lambda rate.
  scope: per function, provisioned concurrency.
  link: [billed for excess function execution](../facts/lambda.md#lambda-pc-excess-at-on-demand-rate)
lambda-pc-no-free-tier
  claim: The Lambda free tier does not apply to functions that enable provisioned concurrency.
  scope: per function, provisioned concurrency.
  link: [free tier does not apply](../facts/lambda.md#lambda-pc-no-free-tier)
lambda-pc-not-latest-no-cold-start
  claim: A function using provisioned concurrency does not show cold start behavior because the execution environment is prepared ahead of invocation, but provisioned concurrency must be applied to a specific version or alias of a function, not the $LATEST version.
  scope: provisioned concurrency.
  link: [a specific version or alias of a function](../facts/lambda.md#lambda-pc-not-latest-no-cold-start)
  link: [not the $LATEST version](../facts/lambda.md#lambda-pc-not-latest-no-cold-start)
  link: [does not exhibit cold start behavior](../facts/lambda.md#lambda-pc-not-latest-no-cold-start)
  say: a published version or an alias
lambda-pc-price-per-gb-second
  claim: In the pricing-page examples (US East (N. Virginia)), provisioned concurrency costs $0.0000041667 per GB-s on top of request and duration charges.
  scope: per GB-second, provisioned concurrency; pricing-page example priced in US East (N. Virginia).
  link: [$0.0000041667 per GB-s](../facts/lambda.md#lambda-pc-price-per-gb-second)
lambda-pc-pricing-dimensions
  claim: With provisioned concurrency you pay for the concurrency configured and the period it is configured, plus requests and duration when the function runs.
  scope: per function, provisioned concurrency.
  link: [amount of concurrency you configure](../facts/lambda.md#lambda-pc-pricing-dimensions)
lambda-pc-rounded-5-minutes
  claim: Provisioned concurrency is billed from the time it is enabled until disabled, rounded up to the nearest five minutes; the price depends on memory and the configured concurrency.
  scope: per function, provisioned concurrency.
  link: [rounded up to the nearest five minutes](../facts/lambda.md#lambda-pc-rounded-5-minutes)
lambda-pc-scales-beyond-setting
  claim: Provisioned concurrency is the number of pre-initialized execution environments Lambda allocates to a function; Lambda serves requests with them when available and can also scale the function above the provisioned concurrency setting if required.
  scope: provisioned concurrency.
  link: [pre-initialized execution environments](../facts/lambda.md#lambda-pc-scales-beyond-setting)
  link: [above and beyond your provisioned concurrency setting](../facts/lambda.md#lambda-pc-scales-beyond-setting)
  say: environments that are already initialized
lambda-price-per-gb-second
  claim: In the pricing-page examples for US East (N. Virginia), the on-demand compute price is $0.0000166667 per GB-s, with 400,000 GB-s free per month.
  scope: per GB-second, on-demand functions, first pricing tier; pricing-page example priced in US East (N. Virginia), x86 architecture, first tier.
  link: [$0.0000166667 per GB-s](../facts/lambda.md#lambda-price-per-gb-second)
lambda-price-per-million-requests
  claim: The request price is $0.20 per one million requests (pricing-page example, US East (N. Virginia)).
  scope: per request, on-demand functions; pricing-page example priced in US East (N. Virginia).
  link: [$0.20 per one million requests](../facts/lambda.md#lambda-price-per-million-requests)
lambda-pricing-dimensions
  claim: Lambda functions are priced on the number of requests and on duration measured in GB-seconds; you choose the memory and get proportional CPU.
  scope: Lambda functions.
  link: [number of requests served](../facts/lambda.md#lambda-pricing-dimensions)
  link: [measured in GB-seconds](../facts/lambda.md#lambda-pricing-dimensions)
lambda-pricing-first-tier-6-billion
  claim: The first on-demand duration pricing tier covers up to 6 billion GB-seconds per month (example: US East (Ohio)).
  scope: per account, per architecture, per Region, per month; maximum.
  link: [up to 6 billion GB-seconds / month](../facts/lambda.md#lambda-pricing-first-tier-6-billion)
lambda-pricing-tiers-aggregate
  claim: Duration pricing tiers apply to the aggregate monthly duration of functions on the same architecture in the same Region within the account, or across the organization's accounts with consolidated billing.
  scope: per architecture, per Region.
  link: [same architecture (x86 or Arm, respectively), in the same region, within the account](../facts/lambda.md#lambda-pricing-tiers-aggregate)
  link: [across the accounts in the organization](../facts/lambda.md#lambda-pricing-tiers-aggregate)
lambda-processes-threads-1024
  claim: A function's execution environment is limited to 1,024 execution processes and threads; Lambda Managed Instances use the Bottlerocket default process and thread limits instead.
  scope: per execution environment; maximum; not adjustable; Lambda Managed Instances use Bottlerocket defaults.
  link: [1,024](../facts/lambda.md#lambda-processes-threads-1024)
lambda-provisioned-concurrency-allocation-rate
  claim: Provisioned concurrency does not come online immediately: Lambda starts allocating it after a minute or two, and for each function it can provision up to 6,000 execution environments every minute.
  scope: per function; maximum; not adjustable.
  link: [up to 6,000 execution environments every minute](../facts/lambda.md#lambda-provisioned-concurrency-allocation-rate)
lambda-provisioned-concurrency-charges
  claim: Configuring provisioned concurrency incurs charges to your AWS account, and provisioned concurrency counts toward the account concurrency limit.
  scope: per function, provisioned concurrency.
  link: [incurs charges to your AWS account](../facts/lambda.md#lambda-provisioned-concurrency-charges)
lambda-provisioned-concurrency-rps
  claim: A function version or alias with provisioned concurrency can be invoked at up to 10 x its allocated provisioned concurrency in requests per second.
  scope: per function version or alias; maximum; not adjustable; applies only to functions that use provisioned concurrency.
  link: [10 x allocated provisioned concurrency](../facts/lambda.md#lambda-provisioned-concurrency-rps)
lambda-provisioned-not-above-reserved
  claim: You cannot allocate more provisioned concurrency than reserved concurrency for a function.
  scope: per function; maximum.
  link: [can't allocate more provisioned concurrency than reserved concurrency](../facts/lambda.md#lambda-provisioned-not-above-reserved)
lambda-put-resource-policy-overwrites
  claim: Using put-resource-policy replaces any existing resource-based policy on the function, including permissions added with add-permission, while add-permission appends a statement without overwriting.
  scope: function resource-based policy.
  link: [replaces any existing resource-based policy](../facts/lambda.md#lambda-put-resource-policy-overwrites)
  link: [Adds a statement to the existing policy](../facts/lambda.md#lambda-put-resource-policy-overwrites)
  say: it replaces the whole policy
lambda-queue-esm-retry-set-on-queue
  claim: For an event source mapping that reads from a queue, the visibility timeout and redrive policy on the source queue determine the time between retries and the destination for failed events.
  scope: event source mapping that reads from a queue.
  link: [visibility timeout and redrive policy](../facts/lambda.md#lambda-queue-esm-retry-set-on-queue)
  link: [on the source queue](../facts/lambda.md#lambda-queue-esm-retry-set-on-queue)
  say: the queue's visibility timeout and redrive policy
lambda-quota-scope-region-vs-vpc
  claim: Quotas for concurrent executions and storage apply per AWS Region, while elastic network interface (ENI) quotas apply per VPC regardless of Region.
  scope: per account.
  link: [per AWS Region](../facts/lambda.md#lambda-quota-scope-region-vs-vpc)
  link: [per virtual private cloud (VPC), regardless of Region](../facts/lambda.md#lambda-quota-scope-region-vs-vpc)
lambda-quotas-hard-vs-soft
  claim: Service quotas consist of hard limits, which you cannot change, and soft limits, for which you can request increases.
  scope: AWS service quotas.
  link: [hard limits, which you cannot change](../facts/lambda.md#lambda-quotas-hard-vs-soft)
  link: [soft limits, which you can request increases for](../facts/lambda.md#lambda-quotas-hard-vs-soft)
lambda-rds-connection-quota-spikes
  claim: Amazon RDS has fixed capacity based on the instance size, so if many Lambda functions connect at the same time you might exceed the database connection quota.
  scope: Lambda with Amazon RDS.
  link: [you might exceed your connection quota](../facts/lambda.md#lambda-rds-connection-quota-spikes)
lambda-rds-proxy-hourly-charge
  claim: Amazon RDS charges an hourly rate for RDS Proxy, based on the database instance size.
  scope: RDS Proxy.
  link: [an hourly rate for proxies](../facts/lambda.md#lambda-rds-proxy-hourly-charge)
lambda-rds-proxy-recommended-production
  claim: Lambda can connect to Amazon RDS directly or through RDS Proxy; direct connections suit simple scenarios and proxies are recommended for production, because a proxy manages a pool of shared connections so the function can reach high concurrency without exhausting database connections.
  scope: Lambda with Amazon RDS.
  link: [proxies are recommended for production](../facts/lambda.md#lambda-rds-proxy-recommended-production)
lambda-recursion-on-by-default-free
  claim: Recursive loop detection is turned on by default for all AWS customers, costs nothing, and does not need X-Ray active tracing; by default, when Lambda detects a recursive loop it stops the function being invoked and notifies you, and a function that is recursive by design can be configured to allow recursive invocation.
  scope: per function; default; adjustable; a function can be configured to allow recursive invocation.
  link: [turned on by default for all AWS customers](../facts/lambda.md#lambda-recursion-on-by-default-free)
  link: [There is no charge to use the feature](../facts/lambda.md#lambda-recursion-on-by-default-free)
  link: [allow it to be invoked recursively](../facts/lambda.md#lambda-recursion-on-by-default-free)
  say: it is on by default
lambda-recursion-stops-about-16
  claim: If a function is invoked approximately 16 times in the same chain of requests, Lambda automatically stops the next function invocation in that chain and notifies you; invocations from the function's other triggers are not affected.
  scope: per chain of requests; recursive loop detection turned on (the default).
  link: [approximately 16 times](../facts/lambda.md#lambda-recursion-stops-about-16)
  link: [automatically stops the next function invocation](../facts/lambda.md#lambda-recursion-stops-about-16)
  say: about sixteen times
lambda-recursion-supported-services
  claim: Lambda can detect only recursive loops that include certain supported services, and the function must use a supported AWS SDK; it currently detects loops between functions, Amazon SQS, Amazon S3, Amazon SNS and Amazon EventBridge custom event buses, and loops made only of Lambda functions.
  scope: recursive loop detection; the function uses a supported AWS SDK.
  link: [Amazon SQS, Amazon S3, Amazon SNS](../facts/lambda.md#lambda-recursion-supported-services)
  link: [Amazon EventBridge Custom event buses](../facts/lambda.md#lambda-recursion-supported-services)
  link: [use one of the supported AWS SDKs](../facts/lambda.md#lambda-recursion-supported-services)
  say: SQS, S3, SNS and EventBridge custom event buses
lambda-recursion-unintended-cost-concurrency
  claim: Unintentional recursive loops can bill unexpected charges to your account and can make Lambda scale and use all of the account's available concurrency.
  scope: recursive invocation loops.
  link: [unexpected charges being billed to your AWS account](../facts/lambda.md#lambda-recursion-unintended-cost-concurrency)
  link: [use all of your account's available concurrency](../facts/lambda.md#lambda-recursion-unintended-cost-concurrency)
  say: unexpected charges
lambda-requests-out-of-order
  claim: Because Lambda scales by running more instances of a function, incoming requests might be processed out of order or concurrently, and you should not rely on an instance being long lived; store application state elsewhere.
  scope: per function; unless noted otherwise for a specific event source.
  link: [processed out of order or concurrently](../facts/lambda.md#lambda-requests-out-of-order)
  link: [store your application's state elsewhere](../facts/lambda.md#lambda-requests-out-of-order)
  say: requests can arrive out of order or at the same time
lambda-reserve-not-all-1000
  claim: With an account concurrency limit of 1,000 you cannot reserve all 1,000 units for a single function; the remaining 100 units stay for functions without reserved concurrency.
  scope: per account, per Region; maximum.
  link: [remaining 100 units](../facts/lambda.md#lambda-reserve-not-all-1000)
  link: [cannot reserve all 1,000 units of concurrency to a single function](../facts/lambda.md#lambda-reserve-not-all-1000)
lambda-reserve-up-to-900-default
  claim: At the function level, you can reserve up to 900 units of concurrency across all your functions by default.
  scope: per account, per Region, function-level reserved concurrency; default; adjustable.
  link: [up to 900 units of concurrency](../facts/lambda.md#lambda-reserve-up-to-900-default)
lambda-reserved-concurrency-no-charge
  claim: Configuring reserved concurrency for a function incurs no additional charges.
  scope: per function, reserved concurrency.
  link: [incurs no additional charges](../facts/lambda.md#lambda-reserved-concurrency-no-charge)
lambda-reserved-concurrency-zero-throttles
  claim: Setting a function's reserved concurrency to 0 throttles it on purpose: it stops processing any events until the limit is removed.
  scope: per function.
  link: [set its reserved concurrency to 0](../facts/lambda.md#lambda-reserved-concurrency-zero-throttles)
lambda-reserved-zero-async-to-dlq-no-retry
  claim: When reserved concurrency is set to zero for an asynchronously invoked function, Lambda begins sending new events to the configured dead-letter queue or on-failure destination without any retries.
  scope: asynchronously invoked function; a dead-letter queue or on-failure destination is configured.
  link: [set reserved concurrency to zero](../facts/lambda.md#lambda-reserved-zero-async-to-dlq-no-retry)
  link: [without any retries](../facts/lambda.md#lambda-reserved-zero-async-to-dlq-no-retry)
  say: reserved concurrency set to zero
lambda-resource-policy-grants-accounts-services
  claim: A resource-based policy on a function can grant other AWS accounts, users, organizations and AWS services access to the function, and each statement can apply to the function, a version or an alias.
  scope: function resource-based policy.
  link: [grant other AWS accounts, users, organizations](../facts/lambda.md#lambda-resource-policy-grants-accounts-services)
  link: [The Lambda function, version, or alias](../facts/lambda.md#lambda-resource-policy-grants-accounts-services)
  say: other accounts, organizations and AWS services
lambda-resource-policy-size
  claim: A function's resource-based policy is limited to 20 KB.
  scope: per function; maximum; not adjustable.
  link: [20 KB](../facts/lambda.md#lambda-resource-policy-size)
lambda-right-size-memory-power-tuning
  claim: To pick the memory size, analyze the Max Memory Used field in the CloudWatch REPORT log line to see whether a function needs more memory or is over-provisioned; AWS recommends the open source AWS Lambda Power Tuning project to find the right memory configuration.
  scope: Lambda memory configuration.
  link: [AWS Lambda Power Tuning project](../facts/lambda.md#lambda-right-size-memory-power-tuning)
lambda-rps-limit-10x-concurrency-quota
  claim: At both the account level and the function level, Lambda enforces a requests-per-second limit equal to 10 times the corresponding concurrency quota.
  scope: per account and per function, per Region; maximum; not adjustable.
  link: [10 times the corresponding concurrency quota](../facts/lambda.md#lambda-rps-limit-10x-concurrency-quota)
lambda-runs-in-lambda-managed-vpc
  claim: Every Lambda function runs inside a VPC that is owned and managed by the Lambda service and is not visible to customers; configuring the function to access resources in your own VPC has no effect on that Lambda-managed VPC.
  scope: every Lambda function.
  link: [owned and managed by the Lambda service](../facts/lambda.md#lambda-runs-in-lambda-managed-vpc)
  link: [not visible to customers](../facts/lambda.md#lambda-runs-in-lambda-managed-vpc)
  say: a VPC that Lambda owns and manages
lambda-runtime-patching-managed-vs-image
  claim: By default Lambda applies security updates automatically to functions that use managed runtimes, but for functions deployed as container images you are responsible for rebuilding the image from the latest base image and redeploying it.
  scope: runtime security updates; default; default automatic runtime update setting.
  link: [apply these updates automatically](../facts/lambda.md#lambda-runtime-patching-managed-vs-image)
  link: [you're responsible for rebuilding your function's container image](../facts/lambda.md#lambda-runtime-patching-managed-vs-image)
  say: Lambda patches managed runtimes for you
lambda-scaling-rate-10000-rps
  claim: Every 10 seconds, Lambda can add at most 1,000 execution environment instances, or 10,000 additional requests per second, to each function.
  scope: per function, per Region; maximum; not adjustable.
  link: [1,000 additional execution environment instances](../facts/lambda.md#lambda-scaling-rate-10000-rps)
  link: [10,000 additional requests per second](../facts/lambda.md#lambda-scaling-rate-10000-rps)
lambda-scaling-rate-not-accrued
  claim: Unused scaling capacity does not accumulate: at any instant the scaling rate is at most 1,000 concurrency units.
  scope: per function; maximum.
  link: [always 1,000 concurrency units at maximum](../facts/lambda.md#lambda-scaling-rate-not-accrued)
lambda-scaling-rate-not-adjustable
  claim: The concurrency scaling rate quota is 1,000 and is not adjustable: every 10 seconds, each synchronously invoked function can scale by an additional 1,000 concurrent executions until the total concurrency across functions in the Region reaches the account concurrency limit.
  scope: per function, per Region; maximum; not adjustable; until the account concurrency limit is reached.
  link: [additional 1,000 concurrent executions](../facts/lambda.md#lambda-scaling-rate-not-adjustable)
  link: [Every 10 seconds](../facts/lambda.md#lambda-scaling-rate-not-adjustable)
lambda-scheduler-cron-rate-retries
  claim: Amazon EventBridge Scheduler can invoke a Lambda function on cron or rate schedules or once, with flexible time windows, retry limits and a maximum retention time for unprocessed events, and it invokes the function asynchronously.
  scope: Amazon EventBridge Scheduler with Lambda.
  link: [cron and rate expressions](../facts/lambda.md#lambda-scheduler-cron-rate-retries)
  link: [flexible time windows for delivery](../facts/lambda.md#lambda-scheduler-cron-rate-retries)
  link: [invokes your Lambda function asynchronously](../facts/lambda.md#lambda-scheduler-cron-rate-retries)
  say: cron and rate expressions
lambda-sdk-cli-auto-retry
  claim: When you invoke a function directly, you can check the response for errors and retry; the AWS CLI and AWS SDK also automatically retry on client timeouts, throttling, and service errors.
  scope: direct invocation through the AWS CLI or an AWS SDK.
  link: [automatically retry on client timeouts](../facts/lambda.md#lambda-sdk-cli-auto-retry)
  link: [check the response for errors and retry](../facts/lambda.md#lambda-sdk-cli-auto-retry)
  say: the CLI and SDKs retry on timeouts, throttling and service errors
lambda-secrets-manager-not-env-vars
  claim: AWS recommends AWS Secrets Manager instead of environment variables for database credentials and other sensitive information such as API keys or authorization tokens.
  scope: secrets used by a Lambda function.
  link: [use AWS Secrets Manager instead of environment variables](../facts/lambda.md#lambda-secrets-manager-not-env-vars)
  link: [database credentials and other sensitive information](../facts/lambda.md#lambda-secrets-manager-not-env-vars)
  say: Secrets Manager, not environment variables
lambda-self-managed-storage-250-mb-unchanged
  claim: Self-managed S3 code storage does not change the maximum .zip deployment package size, which remains 250 MB (unzipped).
  scope: per deployment package (.zip), self-managed S3 code storage; maximum.
  link: [250 MB (unzipped)](../facts/lambda.md#lambda-self-managed-storage-250-mb-unchanged)
lambda-self-managed-storage-not-counted
  claim: With self-managed S3 code storage, Lambda references the code in your S3 bucket and does not store a copy, so that code does not count against the Lambda-managed storage quota.
  scope: per function or layer using self-managed S3 code storage.
  link: [does not count against your Lambda-managed storage quota](../facts/lambda.md#lambda-self-managed-storage-not-counted)
lambda-serverless-manages-infrastructure
  claim: AWS Lambda is a serverless compute service: you run code without provisioning or managing servers, and Lambda manages the underlying infrastructure, including server maintenance, capacity provisioning, scaling and patching.
  scope: AWS Lambda.
  link: [run code without provisioning or managing servers](../facts/lambda.md#lambda-serverless-manages-infrastructure)
  link: [server maintenance, capacity provisioning, scaling, and patching](../facts/lambda.md#lambda-serverless-manages-infrastructure)
  link: [serverless compute service](../facts/lambda.md#lambda-serverless-manages-infrastructure)
  say: you run code without provisioning or managing servers
lambda-service-caller-resource-policy-only
  claim: When a user accesses a Lambda resource, Lambda evaluates both the user's identity-based policies and the resource-based policy, but when an AWS service such as Amazon S3 calls the function, Lambda considers only the resource-based policy.
  scope: invocation by an AWS service.
  link: [Lambda considers only the resource-based policy](../facts/lambda.md#lambda-service-caller-resource-policy-only)
  link: [considers both the user's identity-based policies](../facts/lambda.md#lambda-service-caller-resource-policy-only)
  say: only the function's resource-based policy counts
lambda-snapstart-pricing
  claim: SnapStart charges for caching a snapshot while the function version is active, for a minimum of 3 hours and per millisecond after that, plus a charge each time Lambda restores the snapshot; this SnapStart pricing does not apply to supported Java managed runtimes.
  scope: per function version with SnapStart; not for supported Java managed runtimes.
  link: [minimum of 3 hours](../facts/lambda.md#lambda-snapstart-pricing)
  link: [does not apply to supported Java managed runtimes](../facts/lambda.md#lambda-snapstart-pricing)
lambda-snapstart-published-versions-only
  claim: SnapStart can be used only on published function versions and on aliases that point to versions, not on the unpublished version ($LATEST); Lambda runs the initialization when you publish a function version.
  scope: Lambda SnapStart.
  link: [only on published function versions](../facts/lambda.md#lambda-snapstart-published-versions-only)
  link: [can't use SnapStart on a function's unpublished version](../facts/lambda.md#lambda-snapstart-published-versions-only)
  link: [when you publish a function version](../facts/lambda.md#lambda-snapstart-published-versions-only)
  say: only on published versions and their aliases
lambda-snapstart-runtimes-guide
  claim: The guide lists SnapStart support for the managed runtimes Java 11 and later, Python 3.12 and later and .NET 8 and later, with the matching AWS base images, across both ZIP and container image deployment formats; other managed runtimes such as Node.js and Ruby, and OS-only runtimes, are not supported.
  scope: Lambda SnapStart.
  link: [Java 11 and later](../facts/lambda.md#lambda-snapstart-runtimes-guide)
  link: [Python 3.12 and later](../facts/lambda.md#lambda-snapstart-runtimes-guide)
  link: [.NET 8 and later](../facts/lambda.md#lambda-snapstart-runtimes-guide)
  link: [across ZIP and container image deployment format](../facts/lambda.md#lambda-snapstart-runtimes-guide)
  say: Java eleven and later
lambda-snapstart-snapshot-encrypted-cached
  claim: For SnapStart, Lambda takes a Firecracker MicroVM snapshot of the memory and disk state of the initialized execution environment, encrypts it and caches it; it keeps several copies of each snapshot for resiliency and patches them with runtime and security updates automatically.
  scope: Lambda SnapStart.
  link: [snapshot of the memory and disk state](../facts/lambda.md#lambda-snapstart-snapshot-encrypted-cached)
  link: [encrypts the snapshot](../facts/lambda.md#lambda-snapstart-snapshot-encrypted-cached)
  link: [maintains several copies of each snapshot](../facts/lambda.md#lambda-snapstart-snapshot-encrypted-cached)
  say: a snapshot of memory and disk
lambda-snapstart-unsupported-features
  claim: SnapStart does not support provisioned concurrency, Amazon EFS, Amazon S3 Files, or ephemeral storage greater than 512 MB.
  scope: Lambda SnapStart.
  link: [does not support provisioned concurrency](../facts/lambda.md#lambda-snapstart-unsupported-features)
  link: [ephemeral storage greater than 512 MB](../facts/lambda.md#lambda-snapstart-unsupported-features)
  say: not with provisioned concurrency, EFS or large ephemeral storage
lambda-snapstart-vs-pc-guide
  claim: SnapStart reduces one-time initialization latency from several seconds to as low as sub-second in optimal scenarios and works best at scale; provisioned concurrency keeps functions initialized and ready in double-digit milliseconds and is the choice when strict cold start latency requirements cannot be met by SnapStart.
  scope: SnapStart versus provisioned concurrency.
  link: [as low as sub-second](../facts/lambda.md#lambda-snapstart-vs-pc-guide)
  link: [ready to respond in double-digit milliseconds](../facts/lambda.md#lambda-snapstart-vs-pc-guide)
  link: [strict cold start latency requirements](../facts/lambda.md#lambda-snapstart-vs-pc-guide)
  say: down to under a second
lambda-sp-ec2-instance-plans-exclude-lambda
  claim: Compute Savings Plans automatically apply to Lambda usage; EC2 Instance Savings Plans, Convertible RIs and Standard RIs do not. Compute Savings Plans give savings up to 66% off On-Demand.
  scope: Lambda usage; maximum.
  link: [Compute Savings Plans](../facts/lambda.md#lambda-sp-ec2-instance-plans-exclude-lambda)
  link: [up to 66%](../facts/lambda.md#lambda-sp-ec2-instance-plans-exclude-lambda)
  say: Compute Savings Plans | up to sixty-six percent
lambda-sqs-batch-over-10-needs-window
  claim: For an SQS event source, a standard queue allows a batch size of up to 10,000 records and a FIFO queue a maximum of 10; a batch size over 10 also requires a batching window of at least 1 second.
  scope: per SQS event source mapping; maximum; batch size over 10 needs MaximumBatchingWindowInSeconds of at least 1 second.
  link: [up to 10,000 records](../facts/lambda.md#lambda-sqs-batch-over-10-needs-window)
  link: [the maximum is 10](../facts/lambda.md#lambda-sqs-batch-over-10-needs-window)
  link: [at least 1 second](../facts/lambda.md#lambda-sqs-batch-over-10-needs-window)
lambda-sqs-batch-size
  claim: The SQS event source batch size defaults to 10; the maximum is 10,000 for standard queues and 10 for FIFO queues.
  scope: per SQS event source mapping; default; adjustable.
  link: [10](../facts/lambda.md#lambda-sqs-batch-size)
  link: [For standard queues, the maximum is 10,000](../facts/lambda.md#lambda-sqs-batch-size)
  link: [For FIFO queues, the maximum is 10](../facts/lambda.md#lambda-sqs-batch-size)
lambda-sqs-batch-window-20-second-wait
  claim: With a batch window on a low-traffic SQS queue, Lambda may wait up to 20 seconds before invoking, even if the batch window is set lower than 20 seconds.
  scope: per SQS event source mapping, batch window on a low-traffic queue; maximum.
  link: [up to 20 seconds](../facts/lambda.md#lambda-sqs-batch-window-20-second-wait)
lambda-sqs-batching-window-default
  claim: MaximumBatchingWindowInSeconds defaults to 0 for an SQS event source mapping, and a batching window is not supported for FIFO queues.
  scope: per SQS event source mapping; default; adjustable.
  link: [0](../facts/lambda.md#lambda-sqs-batching-window-default)
  link: [not supported for FIFO queues](../facts/lambda.md#lambda-sqs-batching-window-default)
lambda-sqs-code-error-backoff
  claim: When the function code causes the error on an SQS batch, Lambda stops processing and retrying the invocation, gradually backs off by reducing the concurrency allocated to the SQS event source mapping, and the message reappears in the queue after the visibility timeout runs out.
  scope: Amazon SQS event source mapping; function code error.
  link: [Lambda gradually backs off](../facts/lambda.md#lambda-sqs-code-error-backoff)
  link: [the message reappears in the queue](../facts/lambda.md#lambda-sqs-code-error-backoff)
  say: Lambda slowly reduces its concurrency
lambda-sqs-default-10-messages-batch-window-5-minutes
  claim: By default Lambda polls up to 10 messages in an SQS queue at once and sends that batch to the function; a batch window can buffer records for up to 5 minutes. Before invoking the function, Lambda keeps polling the standard queue until the batch window expires, the invocation payload size quota is reached, or the configured maximum batch size is reached.
  scope: per SQS event source mapping, standard queue; default; adjustable.
  link: [up to 10 messages](../facts/lambda.md#lambda-sqs-default-10-messages-batch-window-5-minutes)
  link: [up to 5 minutes](../facts/lambda.md#lambda-sqs-default-10-messages-batch-window-5-minutes)
lambda-sqs-dlq-maxreceivecount-5
  claim: If the function fails to process a message multiple times, Amazon SQS can send it to a dead-letter queue; AWS recommends setting maxReceiveCount on the source queue's redrive policy to at least 5 so Lambda gets a few retries first.
  scope: Amazon SQS queue used as a Lambda event source; minimum; a recommendation for the redrive policy.
  link: [send it to a dead-letter queue](../facts/lambda.md#lambda-sqs-dlq-maxreceivecount-5)
  link: [at least 5](../facts/lambda.md#lambda-sqs-dlq-maxreceivecount-5)
  say: SQS moves it to the queue's dead-letter queue | at least five
lambda-sqs-esm-1250-default-100000-provisioned
  claim: By default an SQS event source mapping can invoke up to 1,250 concurrent function instances; provisioned mode scales up to 100,000 concurrent invocations.
  scope: per SQS event source mapping; maximum; not adjustable.
  link: [up to 1,250 concurrent function instances](../facts/lambda.md#lambda-sqs-esm-1250-default-100000-provisioned)
  link: [up to 100,000 concurrent function invocations](../facts/lambda.md#lambda-sqs-esm-1250-default-100000-provisioned)
lambda-sqs-execution-role-read-permissions
  claim: The Lambda testing guide lists, as an example of a configuration problem with Amazon SQS and Lambda, a function execution role that doesn't allow reading messages from the queue (through sqs:ReceiveMessage, sqs:DeleteMessage or sqs:GetQueueAttributes).
  scope: execution role of a function with an SQS event source mapping.
  link: [sqs:ReceiveMessage](../facts/lambda.md#lambda-sqs-execution-role-read-permissions)
  link: [doesn't allow reading messages from the queue](../facts/lambda.md#lambda-sqs-execution-role-read-permissions)
lambda-sqs-fifo-concurrency-message-groups
  claim: For a FIFO queue, concurrent invocations are capped by the number of message group IDs or the maximum concurrency setting, whichever is lower: six message groups with maximum concurrency 10 give at most six concurrent invocations.
  scope: per SQS FIFO event source mapping; maximum.
  link: [six message group IDs and maximum concurrency is set to 10, your function can have a maximum of six concurrent invocations](../facts/lambda.md#lambda-sqs-fifo-concurrency-message-groups)
lambda-sqs-max-concurrency-no-charge
  claim: There is no charge for configuring maximum concurrency on an Amazon SQS event source.
  scope: per SQS event source mapping.
  link: [no charge for configuring maximum concurrency](../facts/lambda.md#lambda-sqs-max-concurrency-no-charge)
lambda-sqs-max-concurrency-provisioned-exclusive
  claim: The SQS maximum concurrency setting and provisioned mode cannot be used at the same time.
  scope: per SQS event source mapping.
  link: [cannot use the maximum concurrency setting](../facts/lambda.md#lambda-sqs-max-concurrency-provisioned-exclusive)
lambda-sqs-max-concurrency-range
  claim: The maximum concurrency setting of an SQS event source accepts a number between 2 and 1,000; leaving it empty turns it off.
  scope: per SQS event source mapping; maximum; not adjustable; an empty value turns maximum concurrency off.
  link: [between 2 and 1,000](../facts/lambda.md#lambda-sqs-max-concurrency-range)
lambda-sqs-max-concurrency-vs-reserved
  claim: Maximum concurrency and reserved concurrency are two independent settings; do not set maximum concurrency higher than the function's reserved concurrency, and if you configure maximum concurrency, keep reserved concurrency greater than or equal to the total maximum concurrency for all SQS event sources on the function, or Lambda might throttle messages.
  scope: per function with SQS event sources.
  link: [reserved concurrency is greater than or equal to](../facts/lambda.md#lambda-sqs-max-concurrency-vs-reserved)
lambda-sqs-partial-batch-response
  claim: With a partial batch response, turned on by specifying ReportBatchItemFailures in FunctionResponseTypes, an SQS event source mapping makes only the failed messages of a batch visible again instead of reprocessing the successful ones.
  scope: Amazon SQS event source mapping; ReportBatchItemFailures is specified.
  link: [partial batch response](../facts/lambda.md#lambda-sqs-partial-batch-response)
  link: [ReportBatchItemFailures](../facts/lambda.md#lambda-sqs-partial-batch-response)
  link: [make only the failed messages visible again](../facts/lambda.md#lambda-sqs-partial-batch-response)
  say: a partial batch response
lambda-sqs-provisioned-mode-3x-80x
  claim: SQS provisioned mode scales 3x faster (up to 1,000 concurrent invokes per minute) and supports 80x higher concurrency (up to 100,000 concurrent invokes) than the default SQS event source mapping.
  scope: per SQS event source mapping, provisioned mode; maximum.
  link: [3x faster (up to 1,000 concurrent invokes per minute)](../facts/lambda.md#lambda-sqs-provisioned-mode-3x-80x)
  link: [80x higher concurrency (up to 100,000 concurrent invokes)](../facts/lambda.md#lambda-sqs-provisioned-mode-3x-80x)
lambda-sqs-provisioned-mode-poller-capacity
  claim: In provisioned mode, each SQS event poller handles up to 1 MB/sec, up to 10 concurrent invokes, or up to 10 SQS polling API calls per second, and Lambda adds up to 1,000 concurrency per minute between your minimum and maximum pollers.
  scope: per event poller, SQS provisioned mode; maximum; not adjustable.
  link: [up to 1 MB/sec of throughput](../facts/lambda.md#lambda-sqs-provisioned-mode-poller-capacity)
  link: [up to 10 concurrent invokes](../facts/lambda.md#lambda-sqs-provisioned-mode-poller-capacity)
  link: [up to 1,000 concurrency per minute](../facts/lambda.md#lambda-sqs-provisioned-mode-poller-capacity)
lambda-sqs-provisioned-mode-pollers-range
  claim: In provisioned mode the minimum number of SQS event pollers is between 2 and 200 (default 2) and the maximum is between 2 and 10,000 (default 200); MaximumPollers must be at least MinimumPollers.
  scope: per SQS event source mapping, provisioned mode; default; adjustable.
  link: [between 2 and 200, with default of 2](../facts/lambda.md#lambda-sqs-provisioned-mode-pollers-range)
  link: [between 2 and 10,000, with default of 200](../facts/lambda.md#lambda-sqs-provisioned-mode-pollers-range)
lambda-sqs-reserved-concurrency-min-five
  claim: If you configure reserved concurrency on a function that processes an SQS queue, the guide says to set a minimum of five concurrent executions to reduce the chance of throttling errors when Lambda invokes the function.
  scope: per function with an SQS event source mapping; when reserved concurrency is configured; a recommendation, not an enforced limit.
  link: [a minimum of five concurrent executions](../facts/lambda.md#lambda-sqs-reserved-concurrency-min-five)
lambda-sqs-same-region
  claim: A Lambda function and its SQS queue must be in the same AWS Region, though they can be in different AWS accounts.
  scope: SQS event source mapping.
  link: [must be in the same AWS Region](../facts/lambda.md#lambda-sqs-same-region)
lambda-sqs-scale-back-to-2
  claim: When traffic is low, Lambda scales SQS processing back to five concurrent invokes and can go as low as 2 to reduce SQS calls and cost, unless maximum concurrency is set.
  scope: per SQS event source mapping, standard queue; minimum.
  link: [as few as 2 concurrent invokes](../facts/lambda.md#lambda-sqs-scale-back-to-2)
lambda-sqs-scaling-5-batches-300-per-minute-1250
  claim: For a standard SQS queue, Lambda starts with five batches and five concurrent invocations, adds up to 300 more concurrent invokes per minute while messages remain, and one event source mapping can process at most 1,250 invokes simultaneously.
  scope: per SQS event source mapping, standard queue; maximum; not adjustable.
  link: [five batches at a time with five concurrent invocations](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
  link: [up to 300 more concurrent invokes per minute](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
  link: [1,250](../facts/lambda.md#lambda-sqs-scaling-5-batches-300-per-minute-1250)
lambda-sqs-throttle-drop-after-visibility
  claim: If an SQS invocation fails because of throttling, Lambda gradually backs off retries by reducing the concurrency of the event source mapping and keeps retrying the message until its timestamp exceeds the queue's visibility timeout, at which point Lambda drops the message.
  scope: Amazon SQS event source mapping; throttling errors.
  link: [Lambda continues to retry the message](../facts/lambda.md#lambda-sqs-throttle-drop-after-visibility)
  link: [Lambda drops the message](../facts/lambda.md#lambda-sqs-throttle-drop-after-visibility)
  say: Lambda keeps retrying
lambda-sqs-timeout-not-above-visibility
  claim: A function's timeout must be less than or equal to the queue's visibility timeout; Lambda validates this when you create or update an SQS event source mapping and returns an error if the function timeout exceeds the visibility timeout.
  scope: Amazon SQS event source mapping.
  link: [must be less than or equal to](../facts/lambda.md#lambda-sqs-timeout-not-above-visibility)
  link: [returns an error](../facts/lambda.md#lambda-sqs-timeout-not-above-visibility)
  say: the function timeout must not exceed the visibility timeout
lambda-sqs-visibility-six-times-timeout
  claim: AWS recommends setting the source queue's visibility timeout to at least six times the function's configured timeout, so that Lambda has time to retry if the function is throttled while processing a previous batch.
  scope: Amazon SQS queue used as a Lambda event source; minimum; a recommendation, not an enforced value.
  link: [at least six times](../facts/lambda.md#lambda-sqs-visibility-six-times-timeout)
  link: [visibility timeout](../facts/lambda.md#lambda-sqs-visibility-six-times-timeout)
  say: at least six times the function timeout
lambda-sqs-visibility-timeout-retry
  claim: SQS messages in a batch stay hidden for the queue's visibility timeout; if the function errors on the batch, by default all messages in it become visible again after the timeout expires, so the code must tolerate repeats.
  scope: per SQS event source mapping; default.
  link: [become visible in the queue again](../facts/lambda.md#lambda-sqs-visibility-timeout-retry)
lambda-stateless-store-state-elsewhere
  claim: A standard function should assume its environment exists only for a single invocation: commit permanent data changes to a durable store such as Amazon S3, DynamoDB or Amazon SQS before exiting, and do not rely on temporary files or internal state kept across invocations.
  scope: standard functions.
  link: [exists only for a single invocation](../facts/lambda.md#lambda-stateless-store-state-elsewhere)
  link: [durable store such as Amazon S3](../facts/lambda.md#lambda-stateless-store-state-elsewhere)
  link: [should not rely on any existing data structures](../facts/lambda.md#lambda-stateless-store-state-elsewhere)
  say: treat each invocation as if the environment is new
lambda-static-init-reuse-connections
  claim: Initialization code is not run again when an invocation uses a warm execution environment, so static initialization is often the best place to open database connections that later invocations in the same execution environment reuse.
  scope: per execution environment.
  link: [is not run again](../facts/lambda.md#lambda-static-init-reuse-connections)
  link: [reuse connections over multiple invocations](../facts/lambda.md#lambda-static-init-reuse-connections)
  say: init code runs once per environment
lambda-step-functions-orchestrate-errors
  claim: AWS Step Functions provides visual workflow orchestration for Lambda functions and other AWS services: each task gets its own function, and Step Functions coordinates the flow of data between functions and handles errors at each step.
  scope: Step Functions with Lambda.
  link: [visual workflow orchestration](../facts/lambda.md#lambda-step-functions-orchestrate-errors)
  link: [handles errors at each step](../facts/lambda.md#lambda-step-functions-orchestrate-errors)
  say: visual workflow orchestration
lambda-stream-bisect-batch-on-error
  claim: For function errors on a Kinesis event source mapping, BisectBatchOnFunctionError splits a failed batch into two smaller batches to isolate bad records and avoid timeouts, and splitting does not consume the retry quota.
  scope: Kinesis event source mapping; function errors.
  link: [BisectBatchOnFunctionError](../facts/lambda.md#lambda-stream-bisect-batch-on-error)
  link: [splits a failed batch into two smaller batches](../facts/lambda.md#lambda-stream-bisect-batch-on-error)
  link: [doesn't consume the retry quota](../facts/lambda.md#lambda-stream-bisect-batch-on-error)
  say: bisect batch on function error
lambda-streaming-200-mb-vs-6-mb
  claim: Response streaming functions can return payloads up to 200 MB, compared with the 6 MB maximum for buffered responses.
  scope: per invocation, response payload; maximum; not adjustable.
  link: [up to 200 MB](../facts/lambda.md#lambda-streaming-200-mb-vs-6-mb)
  link: [6 MB maximum](../facts/lambda.md#lambda-streaming-200-mb-vs-6-mb)
lambda-streaming-bandwidth-2-mbps
  claim: The first 6 MB of a streamed response has uncapped bandwidth; after that Lambda streams at a maximum of 2 MBps, and responses that never exceed 6 MB never hit the cap.
  scope: per invocation, streamed response payload; maximum; not adjustable.
  link: [maximum rate of 2 MBps](../facts/lambda.md#lambda-streaming-bandwidth-2-mbps)
  link: [first 6 MB](../facts/lambda.md#lambda-streaming-bandwidth-2-mbps)
lambda-streaming-furl-not-in-vpc
  claim: Lambda function URLs do not support response streaming within a VPC environment.
  scope: function URLs in a VPC.
  link: [do not support response streaming](../facts/lambda.md#lambda-streaming-furl-not-in-vpc)
lambda-streaming-nodejs-managed-runtimes
  claim: Lambda supports response streaming natively on Node.js managed runtimes; other languages need a custom runtime or the Lambda Web Adapter.
  scope: response streaming.
  link: [Node.js managed runtimes](../facts/lambda.md#lambda-streaming-nodejs-managed-runtimes)
lambda-streaming-paths
  claim: A function can stream its response through a Lambda function URL, through the InvokeWithResponseStream API, or through the API Gateway proxy integration that uses that API.
  scope: response streaming.
  link: [InvokeWithResponseStream](../facts/lambda.md#lambda-streaming-paths)
  link: [Lambda function URLs](../facts/lambda.md#lambda-streaming-paths)
lambda-sync-error-caller-retries
  claim: When a synchronous invocation fails, the error comes back in the response and the caller must retry manually; Lambda does not retry synchronous invocations for you.
  scope: synchronous invocations.
  link: [retry the invocation manually](../facts/lambda.md#lambda-sync-error-caller-retries)
  link: [view the error message in the response](../facts/lambda.md#lambda-sync-error-caller-retries)
  say: the caller retries, not Lambda
lambda-sync-invocation-waits
  claim: In a synchronous invocation Lambda runs the function and the caller waits for the response; the Invoke API uses InvocationType RequestResponse for synchronous and Event for asynchronous invocation.
  scope: per invocation.
  link: [runs the function and waits for a response](../facts/lambda.md#lambda-sync-invocation-waits)
  link: [a value of Event indicates asynchronous invocation](../facts/lambda.md#lambda-sync-invocation-waits)
  link: [RequestResponse](../facts/lambda.md#lambda-sync-invocation-waits)
  say: the caller waits for the response
lambda-sync-requests-per-env
  claim: For synchronous invocations, each instance of the execution environment can serve up to 10 requests per second, so the total invocation limit is 10 times the concurrency limit.
  scope: per function, per Region, synchronous invocations; maximum; not adjustable.
  link: [10 requests per second](../facts/lambda.md#lambda-sync-requests-per-env)
  link: [10 times your concurrency limit](../facts/lambda.md#lambda-sync-requests-per-env)
lambda-sync-service-controls-error-strategy
  claim: When a service invokes a function synchronously, that service waits for the function's response, defines the data the function needs to return, and controls the error strategy, such as whether to retry on errors.
  scope: synchronous invocation by an AWS service.
  link: [waits for the response from your function](../facts/lambda.md#lambda-sync-service-controls-error-strategy)
  link: [The service controls the error strategy](../facts/lambda.md#lambda-sync-service-controls-error-strategy)
  say: the calling service waits for the response
lambda-sync-status-200-with-function-error
  claim: For a synchronous invocation, the status code from Lambda is 200 whenever Lambda was able to run the function, even if the function itself returned an error.
  scope: synchronous invocations; Lambda was able to run the function.
  link: [status code is 200, even if the function returned an error](../facts/lambda.md#lambda-sync-status-200-with-function-error)
  link: [200](../facts/lambda.md#lambda-sync-status-200-with-function-error)
  say: two hundred, even when the function code failed
lambda-tenant-isolation-create-time-only
  claim: Tenant isolation is an immutable function property that can only be enabled when you create the function.
  scope: functions with tenant isolation mode.
  link: [can only be enabled when creating a function](../facts/lambda.md#lambda-tenant-isolation-create-time-only)
lambda-tenant-isolation-env-never-shared
  claim: With tenant isolation, execution environments are never reused across different tenants; without it, execution environments might be reused across invocations of the same function.
  scope: functions with tenant isolation mode.
  link: [never reused across different tenants](../facts/lambda.md#lambda-tenant-isolation-env-never-shared)
lambda-tenant-isolation-pricing-dimension
  claim: With tenant isolation you are charged each time Lambda creates a new tenant-isolated execution environment; the price depends on the memory you allocate and the CPU architecture, in addition to standard Lambda pricing.
  scope: functions with tenant isolation mode.
  link: [creates a new tenant-isolated execution environment](../facts/lambda.md#lambda-tenant-isolation-pricing-dimension)
lambda-tenant-isolation-routing
  claim: With tenant isolation mode, Lambda uses a customer-specified tenant identifier to route requests so that a function's execution environments serve invocations from only that end-user or tenant.
  scope: functions created with tenant isolation mode.
  link: [customer-specified tenant identifier](../facts/lambda.md#lambda-tenant-isolation-routing)
  say: a tenant ID on each invoke
lambda-tenant-isolation-unsupported-features
  claim: Tenant isolation mode is not supported with functions that use function URLs, provisioned concurrency, or SnapStart.
  scope: functions with tenant isolation mode.
  link: [function URLs](../facts/lambda.md#lambda-tenant-isolation-unsupported-features)
lambda-test-events-console
  claim: The console editor keeps at most 10 test events per function.
  scope: per function, console editor; maximum; not adjustable.
  link: [10](../facts/lambda.md#lambda-test-events-console)
lambda-throttle-429
  claim: When requests arrive faster than the function can scale, or the function is at maximum concurrency, additional requests fail with a throttling error (429 status code).
  scope: per function.
  link: [throttling error (429 status code)](../facts/lambda.md#lambda-throttle-429)
lambda-timeout-default
  claim: The default function timeout is 3 seconds; you can adjust it in increments of 1 second up to a maximum of 900 seconds (15 minutes). For functions on Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) allow a maximum of 5,400 seconds (90 minutes).
  scope: per function; default; adjustable; Lambda Managed Instances allow 5,400 seconds for asynchronous and most event source mapping invocations.
  link: [3 seconds](../facts/lambda.md#lambda-timeout-default)
  link: [increments of 1 second](../facts/lambda.md#lambda-timeout-default)
  link: [900 seconds (15 minutes)](../facts/lambda.md#lambda-timeout-default)
lambda-timeout-max
  claim: The maximum function timeout is 900 seconds (15 minutes); for functions on Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) allow a maximum of 5,400 seconds (90 minutes).
  scope: per function; maximum; not adjustable; 5,400 seconds only for Lambda Managed Instances, asynchronous and event source mapping invocations except Amazon MQ and Amazon DocumentDB.
  link: [900 seconds](../facts/lambda.md#lambda-timeout-max)
  link: [15 minutes](../facts/lambda.md#lambda-timeout-max)
  link: [5,400 seconds (90 minutes)](../facts/lambda.md#lambda-timeout-max)
lambda-tmp-encrypted-at-rest
  claim: All data stored in /tmp is encrypted at rest with a key managed by AWS.
  scope: per execution environment, /tmp directory.
  link: [encrypted at rest](../facts/lambda.md#lambda-tmp-encrypted-at-rest)
lambda-tmp-storage-range
  claim: The /tmp directory storage can be set between 512 MB and 10,240 MB, in 1-MB increments.
  scope: per function, /tmp directory; maximum; not adjustable.
  link: [512 MB](../facts/lambda.md#lambda-tmp-storage-range)
  link: [10,240 MB](../facts/lambda.md#lambda-tmp-storage-range)
  link: [1-MB increments](../facts/lambda.md#lambda-tmp-storage-range)
lambda-tmp-transient-cache
  claim: Each execution environment has between 512 MB and 10,240 MB of disk space in the /tmp directory; its content remains while the environment is frozen, so /tmp works as a transient cache across invocations of the same environment, not as durable storage.
  scope: per execution environment.
  link: [between 512 MB and 10,240 MB](../facts/lambda.md#lambda-tmp-transient-cache)
  link: [transient cache](../facts/lambda.md#lambda-tmp-transient-cache)
  link: [remains when the execution environment is frozen](../facts/lambda.md#lambda-tmp-transient-cache)
  say: from five hundred twelve megabytes to ten gigabytes
lambda-tmp-unique-per-environment
  claim: The /tmp ephemeral storage is temporary and unique to each execution environment.
  scope: per execution environment, /tmp directory.
  link: [temporary and unique to each execution environment](../facts/lambda.md#lambda-tmp-unique-per-environment)
lambda-trigger-alb-sync
  claim: Elastic Load Balancing (an Application Load Balancer) is an event-driven trigger that invokes a Lambda function synchronously.
  scope: Application Load Balancer as a Lambda trigger.
  link: [Event-driven; synchronous invocation](../facts/lambda.md#lambda-trigger-alb-sync)
  link: [Application Load Balancer](../facts/lambda.md#lambda-trigger-alb-sync)
  say: event-driven, synchronous invocation
lambda-trigger-apigateway-sync
  claim: Amazon API Gateway is an event-driven trigger that invokes a Lambda function synchronously.
  scope: Amazon API Gateway as a Lambda trigger.
  link: [Event-driven; synchronous invocation](../facts/lambda.md#lambda-trigger-apigateway-sync)
  link: [Amazon API Gateway](../facts/lambda.md#lambda-trigger-apigateway-sync)
  say: event-driven, synchronous invocation
lambda-trigger-cloudwatch-logs-async
  claim: Amazon CloudWatch Logs is an event-driven trigger that invokes a Lambda function asynchronously.
  scope: Amazon CloudWatch Logs as a Lambda trigger.
  link: [Event-driven; asynchronous invocation](../facts/lambda.md#lambda-trigger-cloudwatch-logs-async)
  link: [Amazon CloudWatch Logs](../facts/lambda.md#lambda-trigger-cloudwatch-logs-async)
  say: event-driven, asynchronous invocation
lambda-trigger-cognito-sync
  claim: Amazon Cognito is an event-driven trigger that invokes a Lambda function synchronously.
  scope: Amazon Cognito as a Lambda trigger.
  link: [Event-driven; synchronous invocation](../facts/lambda.md#lambda-trigger-cognito-sync)
  link: [Amazon Cognito](../facts/lambda.md#lambda-trigger-cognito-sync)
  say: event-driven, synchronous invocation
lambda-trigger-dynamodb-esm
  claim: Amazon DynamoDB invokes Lambda through an event source mapping.
  scope: Amazon DynamoDB as a Lambda event source.
  link: [Event source mapping](../facts/lambda.md#lambda-trigger-dynamodb-esm)
  link: [Amazon DynamoDB](../facts/lambda.md#lambda-trigger-dynamodb-esm)
  say: an event source mapping
lambda-trigger-eventbridge-async-rules
  claim: EventBridge invokes a Lambda function asynchronously from event buses and rules, and synchronously or asynchronously from pipes.
  scope: Amazon EventBridge as a Lambda trigger.
  link: [asynchronous invocation (event buses and rules)](../facts/lambda.md#lambda-trigger-eventbridge-async-rules)
  link: [synchronous or asynchronous invocation (pipes)](../facts/lambda.md#lambda-trigger-eventbridge-async-rules)
  say: asynchronous for event buses and rules
lambda-trigger-kinesis-esm
  claim: Amazon Kinesis invokes Lambda through an event source mapping.
  scope: Amazon Kinesis as a Lambda event source.
  link: [Event source mapping](../facts/lambda.md#lambda-trigger-kinesis-esm)
  link: [Amazon Kinesis](../facts/lambda.md#lambda-trigger-kinesis-esm)
  say: an event source mapping
lambda-trigger-s3-async
  claim: Amazon S3 is an event-driven trigger that invokes a Lambda function asynchronously.
  scope: Amazon S3 as a Lambda trigger.
  link: [Event-driven; asynchronous invocation](../facts/lambda.md#lambda-trigger-s3-async)
  link: [Amazon Simple Storage Service (Amazon S3)](../facts/lambda.md#lambda-trigger-s3-async)
  say: event-driven, asynchronous invocation
lambda-trigger-scheduler-async
  claim: Amazon EventBridge Scheduler is a time-based, event-driven trigger that invokes a Lambda function asynchronously.
  scope: Amazon EventBridge Scheduler as a Lambda trigger.
  link: [Event-driven (time based); asynchronous invocation](../facts/lambda.md#lambda-trigger-scheduler-async)
  link: [Amazon EventBridge Scheduler](../facts/lambda.md#lambda-trigger-scheduler-async)
  say: time based, asynchronous invocation
lambda-trigger-sns-async
  claim: Amazon SNS is an event-driven trigger that invokes a Lambda function asynchronously.
  scope: Amazon SNS as a Lambda trigger.
  link: [Event-driven; asynchronous invocation](../facts/lambda.md#lambda-trigger-sns-async)
  link: [Amazon Simple Notification Service](../facts/lambda.md#lambda-trigger-sns-async)
  say: event-driven, asynchronous invocation
lambda-trigger-sqs-esm
  claim: Amazon SQS invokes Lambda through an event source mapping.
  scope: Amazon SQS as a Lambda event source.
  link: [Event source mapping](../facts/lambda.md#lambda-trigger-sqs-esm)
  link: [Amazon Simple Queue Service](../facts/lambda.md#lambda-trigger-sqs-esm)
  say: an event source mapping
lambda-trigger-sqs-sns-eventbridge-model
  claim: In their communication model, Amazon SQS is pull-based (consumers poll messages from the queue), Amazon SNS is push-based (subscribers receive messages when published), and EventBridge is event-driven (rules match events and route them to targets).
  scope: Amazon SQS versus Amazon SNS versus Amazon EventBridge.
  link: [Pull-based (consumers poll messages from the queue)](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
  link: [Push-based (subscribers receive messages when published)](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
  link: [rules match events and route to targets](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-model)
lambda-trigger-sqs-sns-eventbridge-use-cases
  claim: Typical uses: SQS for decoupling microservices, buffering requests and processing tasks asynchronously; SNS for fanout notifications and pub/sub messaging; EventBridge for event-driven architectures, real-time stream processing and cross-account event sharing.
  scope: Amazon SQS versus Amazon SNS versus Amazon EventBridge.
  link: [buffering requests](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
  link: [Fanout notifications](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
  link: [cross-account event sharing](../facts/lambda.md#lambda-trigger-sqs-sns-eventbridge-use-cases)
lambda-trigger-step-functions-sync-or-async
  claim: AWS Step Functions can invoke a Lambda function either synchronously or asynchronously.
  scope: AWS Step Functions as a Lambda trigger.
  link: [Event-driven; synchronous or asynchronous invocation](../facts/lambda.md#lambda-trigger-step-functions-sync-or-async)
  link: [AWS Step Functions](../facts/lambda.md#lambda-trigger-step-functions-sync-or-async)
  say: synchronous or asynchronous invocation
lambda-trigger-stored-by-source-esm-in-lambda
  claim: A trigger is stored and managed by the service that generates the events, not by Lambda, whereas an event source mapping is a Lambda resource created and managed within the Lambda service.
  scope: triggers versus event source mappings.
  link: [stored and managed by the service](../facts/lambda.md#lambda-trigger-stored-by-source-esm-in-lambda)
  link: [created and managed within the Lambda service](../facts/lambda.md#lambda-trigger-stored-by-source-esm-in-lambda)
  say: the trigger lives in the source service
lambda-two-programming-models
  claim: Lambda offers two programming models: standard functions that run up to 15 minutes, and Durable Functions that can run up to one year.
  scope: per function; maximum.
  link: [standard functions that run up to 15 minutes](../facts/lambda.md#lambda-two-programming-models)
  link: [Durable Functions that can run up to one year](../facts/lambda.md#lambda-two-programming-models)
  say: standard functions, up to fifteen minutes | durable functions, up to one year
lambda-unreserved-concurrency-100-always
  claim: Regardless of the account concurrency limit, Lambda always keeps 100 units of concurrency for functions that do not reserve concurrency; with a limit of 2,000 you can reserve up to 1,900 units at the function level.
  scope: per account, per Region; fixed; not adjustable.
  link: [100 units of concurrency](../facts/lambda.md#lambda-unreserved-concurrency-100-always)
  link: [reserve up to 1,900 units](../facts/lambda.md#lambda-unreserved-concurrency-100-always)
lambda-version-immutable-latest-unpublished
  claim: After you publish a function version, its code, runtime, architecture, memory, layers and most other settings are immutable; to change them you publish a new version from $LATEST, the unpublished version.
  scope: per function version.
  link: [immutable](../facts/lambda.md#lambda-version-immutable-latest-unpublished)
  link: [without publishing a new version](../facts/lambda.md#lambda-version-immutable-latest-unpublished)
  link: [unpublished version is named $LATEST](../facts/lambda.md#lambda-version-immutable-latest-unpublished)
  say: a published version cannot be changed
lambda-vpc-additional-charges
  claim: Using a VPC or VPC peering with Lambda functions incurs additional charges as explained on the EC2 On-Demand pricing page.
  scope: functions attached to a VPC.
  link: [will incur additional charges](../facts/lambda.md#lambda-vpc-additional-charges)
lambda-vpc-attach-private-subnets
  claim: You give a Lambda function access to resources in an Amazon VPC by attaching the function to the VPC through the private subnets that contain the resources.
  scope: Lambda function attached to a VPC.
  link: [attaching your function to the VPC](../facts/lambda.md#lambda-vpc-attach-private-subnets)
  link: [through the private subnets that contain the resources](../facts/lambda.md#lambda-vpc-attach-private-subnets)
  say: attach the function to the VPC
lambda-vpc-attached-only-vpc-resources
  claim: By default, Lambda functions have access to the public internet; once a function is attached to a VPC it can only access resources available within that VPC, and the VPC itself must have internet access for the function to reach the internet.
  scope: Lambda function attached to a VPC; default; adjustable; internet access needs the VPC configured for it.
  link: [have access to the public internet](../facts/lambda.md#lambda-vpc-attached-only-vpc-resources)
  link: [can only access resources available within that VPC](../facts/lambda.md#lambda-vpc-attached-only-vpc-resources)
  link: [configure the VPC to have internet access](../facts/lambda.md#lambda-vpc-attached-only-vpc-resources)
  say: by default a function can reach the internet
lambda-vpc-condition-keys-require-vpc
  claim: Lambda-specific IAM condition keys for VPC settings can, for example, require that all functions in your organization are connected to a VPC, and can specify which subnets and security groups users can and cannot use.
  scope: IAM policies for Lambda.
  link: [Lambda-specific condition keys for VPC settings](../facts/lambda.md#lambda-vpc-condition-keys-require-vpc)
  link: [require that all functions in your organization](../facts/lambda.md#lambda-vpc-condition-keys-require-vpc)
  say: Lambda condition keys for VPC settings
lambda-vpc-db-connections-rds-proxy
  claim: Because Lambda scales by creating many concurrent execution environments that each keep their own database connection, high concurrency can exhaust database connection limits; for relational databases the guide says to use Amazon RDS Proxy to pool and manage connections.
  scope: Lambda functions that access a relational database.
  link: [exhaust database connection limits](../facts/lambda.md#lambda-vpc-db-connections-rds-proxy)
  link: [to pool and manage connections](../facts/lambda.md#lambda-vpc-db-connections-rds-proxy)
lambda-vpc-ec2-permissions-scope
  claim: The EC2 network-interface permissions in the execution role are needed only to create the network interfaces, not to invoke the function, and granting them to the role also implicitly grants them to the function's code.
  scope: execution role of a VPC-attached function.
  link: [not to invoke your function](../facts/lambda.md#lambda-vpc-ec2-permissions-scope)
  link: [implicitly granting these permissions to your function's code](../facts/lambda.md#lambda-vpc-ec2-permissions-scope)
  say: they are needed to create the interfaces, not to invoke
lambda-vpc-execution-role-policy
  claim: To attach a function to a VPC, Lambda needs permissions to create and manage network interfaces; you can attach the AWS managed policy AWSLambdaVPCAccessExecutionRole to the execution role, and the Lambda console adds it automatically when you create a function attached to a VPC.
  scope: Lambda function attached to a VPC.
  link: [AWSLambdaVPCAccessExecutionRole](../facts/lambda.md#lambda-vpc-execution-role-policy)
  link: [Lambda automatically adds this permissions policy](../facts/lambda.md#lambda-vpc-execution-role-policy)
  say: the AWS Lambda VPC access execution role policy
lambda-vpc-idle-14-days-inactive
  claim: If a VPC-attached function stays idle for 14 days, Lambda reclaims its unused Hyperplane ENIs and sets the function to Inactive; the next invocation fails and the function is Pending until an ENI is ready again.
  scope: per VPC-attached function; default; function attached to a VPC.
  link: [idle for 14 days](../facts/lambda.md#lambda-vpc-idle-14-days-inactive)
lambda-vpc-new-function-pending
  claim: While Lambda creates a Hyperplane ENI for a new function, the function stays in the Pending state and cannot be invoked; it becomes Active only when the ENI is ready, which can take several minutes.
  scope: new function attached to a VPC.
  link: [remains in the Pending state](../facts/lambda.md#lambda-vpc-new-function-pending)
  link: [can take several minutes](../facts/lambda.md#lambda-vpc-new-function-pending)
  say: it stays pending
lambda-vpc-no-dedicated-tenancy
  claim: Lambda functions cannot connect directly to a VPC with dedicated instance tenancy; to reach resources there, peer it to a second VPC with default tenancy.
  scope: VPC with dedicated instance tenancy.
  link: [can't connect directly to a VPC](../facts/lambda.md#lambda-vpc-no-dedicated-tenancy)
  link: [dedicated instance tenancy](../facts/lambda.md#lambda-vpc-no-dedicated-tenancy)
  say: it cannot attach directly
lambda-vpc-public-subnet-no-internet
  claim: Connecting a function to a public subnet doesn't give it internet access or a public IP address. In the guide's setup for internet access, the function uses private subnets, which access the internet through a NAT gateway; the Create VPC workflow creates the subnets, NAT gateway, internet gateway and route table entries for this.
  scope: Lambda function attached to a VPC; the NAT gateway path is the guide's internet-access setup for VPC-connected functions.
  link: [doesn't give it internet access](../facts/lambda.md#lambda-vpc-public-subnet-no-internet)
  link: [access the internet through the NAT gateway](../facts/lambda.md#lambda-vpc-public-subnet-no-internet)
  say: a public subnet does not give internet access
lambda-vpc-remove-eni-20-minutes
  claim: After you remove a function's VPC configuration, Lambda needs up to 20 minutes to delete the attached Hyperplane ENI, and deletes it only if no other function or published version uses it.
  scope: per Hyperplane ENI; maximum; not adjustable; only if no other function or published function version uses the ENI.
  link: [up to 20 minutes](../facts/lambda.md#lambda-vpc-remove-eni-20-minutes)
lambda-vs-fargate-billing
  claim: Fargate is billed per second for the vCPU and memory you select, with a one-minute minimum charge, whether or not the application is processing requests; Lambda is charged by the number of requests and the execution duration, measured in milliseconds.
  scope: Fargate versus Lambda.
  link: [billed per second, with a one-minute minimum charge](../facts/lambda.md#lambda-vs-fargate-billing)
  link: [number of requests and execution duration](../facts/lambda.md#lambda-vs-fargate-billing)
lambda-vs-fargate-cost-by-volume
  claim: The decision guide says you typically pay less with Lambda at lower traffic volumes, while Fargate's per-second resource billing tends to be more economical for sustained, high-throughput workloads; Lambda costs scale linearly with request volume.
  scope: Fargate versus Lambda cost.
  link: [pay less with Lambda at lower traffic volumes](../facts/lambda.md#lambda-vs-fargate-cost-by-volume)
  link: [sustained, high-throughput workloads](../facts/lambda.md#lambda-vs-fargate-cost-by-volume)
lambda-vs-fargate-cpu-memory-ceilings
  claim: With Fargate you can select CPU values from 0.25 vCPUs to 32 vCPUs, and memory ranges from 0.5 GB to 244 GB per task, depending on your configuration; with Lambda, CPU scales with memory, up to 6 vCPU.
  scope: per Fargate task, compared with a Lambda function; maximum; not adjustable; Fargate memory range depends on the task configuration.
  link: [0.25 vCPUs to 32 vCPUs](../facts/lambda.md#lambda-vs-fargate-cpu-memory-ceilings)
  link: [0.5 GB to 244 GB per task](../facts/lambda.md#lambda-vs-fargate-cpu-memory-ceilings)
lambda-vs-fargate-state
  claim: For standard Lambda functions each invocation is independent and stateless, so state that must persist between invocations is managed externally, for example in a database or storage service.
  scope: Fargate versus Lambda.
  link: [each invocation is independent and stateless](../facts/lambda.md#lambda-vs-fargate-state)
lambda-wa-quotas-failover-region
  claim: The Well-Architected reliability pillar advises ensuring a sufficient gap between current quotas and maximum usage to accommodate failover (REL01-BP06), and establishing an automated, programmatic check for a service quota that has been changed in one Region but not in other Regions of the same account.
  scope: service quotas across Regions.
  link: [a sufficient gap exists between the current quotas](../facts/lambda.md#lambda-wa-quotas-failover-region)
  link: [changed in one region but not in other regions](../facts/lambda.md#lambda-wa-quotas-failover-region)
  say: keep headroom in quotas for failover
lambda-wa-quotas-not-auto-increased
  claim: Well-Architected REL01-BP01 lists assuming that quotas will automatically be increased as a common anti-pattern; Service Quotas lets you look up quota values and request and track quota increases from the console or the AWS SDK.
  scope: service quotas, all services.
  link: [Assuming that quotas will automatically be increased](../facts/lambda.md#lambda-wa-quotas-not-auto-increased)
  link: [request and track quota increases](../facts/lambda.md#lambda-wa-quotas-not-auto-increased)
  say: do not assume quotas rise on their own
lambda-wa-vpc-only-when-necessary
  claim: The Well-Architected Serverless Lens says to configure VPC access for Lambda functions only when necessary, and to set up a NAT gateway if a VPC-enabled function needs internet access.
  scope: Lambda VPC access.
  link: [only when necessary](../facts/lambda.md#lambda-wa-vpc-only-when-necessary)
lambda-warm-start-environment-reuse
  claim: After an invocation the execution environment is frozen and kept for a period of time; if another request for the same function arrives, Lambda can reuse the environment, which is called a warm start and typically finishes more quickly.
  scope: per execution environment.
  link: [Lambda can reuse the environment](../facts/lambda.md#lambda-warm-start-environment-reuse)
  link: [warm start](../facts/lambda.md#lambda-warm-start-environment-reuse)
  link: [the execution environment is frozen](../facts/lambda.md#lambda-warm-start-environment-reuse)
  say: Lambda reuses the warm environment
lambda-weighted-alias-canary
  claim: A weighted alias sends a small percentage of traffic to a new version so you can test it and quickly roll back (a canary deployment); if you give the additional version 10 percent, the first version gets the remaining 90 percent automatically.
  scope: per alias.
  link: [small percentage of traffic](../facts/lambda.md#lambda-weighted-alias-canary)
  link: [quickly roll back](../facts/lambda.md#lambda-weighted-alias-canary)
  link: [10 percent to Additional version, the first version is assigned 90 percent automatically](../facts/lambda.md#lambda-weighted-alias-canary)
  say: a small share of traffic goes to the new version
lambda-weighted-alias-two-versions-not-latest
  claim: A weighted alias can point to a maximum of two function versions, both of which must be published; the alias cannot point to $LATEST.
  scope: per alias; maximum.
  link: [maximum of two Lambda function versions](../facts/lambda.md#lambda-weighted-alias-two-versions-not-latest)
  link: [cannot point to $LATEST](../facts/lambda.md#lambda-weighted-alias-two-versions-not-latest)
  link: [Both versions must be published](../facts/lambda.md#lambda-weighted-alias-two-versions-not-latest)
  say: at most two versions
lambda-xray-active-tracing
  claim: Lambda supports the X-Ray tracing modes Active and PassThrough; with Active tracing Lambda automatically creates trace segments for invocations and sends them to X-Ray, and the execution role needs permission to upload trace data (the console adds it, or attach AWSXRayDaemonWriteAccess).
  scope: Lambda with AWS X-Ray.
  link: [Active and PassThrough](../facts/lambda.md#lambda-xray-active-tracing)
  link: [automatically creates trace segments](../facts/lambda.md#lambda-xray-active-tracing)
  link: [AWSXRayDaemonWriteAccess](../facts/lambda.md#lambda-xray-active-tracing)
  say: active and pass-through
lambda-xray-sampling-fixed
  claim: X-Ray does not trace every request to a Lambda function: the sampling rate is 1 request per second and 5 percent of additional requests, and you cannot configure the X-Ray sampling rate for your functions.
  scope: Lambda functions with X-Ray tracing; fixed; not adjustable.
  link: [1 request per second and 5 percent of additional requests](../facts/lambda.md#lambda-xray-sampling-fixed)
  link: [You can't configure the X-Ray sampling rate](../facts/lambda.md#lambda-xray-sampling-fixed)
  say: one request per second plus five percent
lambda-zip-over-50-mb-from-s3
  claim: In the console, a .zip archive smaller than 50 MB can be uploaded from your machine; a larger file must be uploaded to the function from an Amazon S3 bucket.
  scope: per deployment package (.zip), console upload; maximum.
  link: [smaller than 50 MB](../facts/lambda.md#lambda-zip-over-50-mb-from-s3)
  link: [from an Amazon S3 bucket](../facts/lambda.md#lambda-zip-over-50-mb-from-s3)
lambda-zip-package-50-mb
  claim: A .zip deployment package is limited to 50 MB (zipped) when uploaded directly through the Lambda API, SDKs or console; larger files must be uploaded through Amazon S3.
  scope: per deployment package (.zip), direct upload; maximum; not adjustable.
  link: [50 MB](../facts/lambda.md#lambda-zip-package-50-mb)
  link: [Upload larger files with Amazon S3](../facts/lambda.md#lambda-zip-package-50-mb)
