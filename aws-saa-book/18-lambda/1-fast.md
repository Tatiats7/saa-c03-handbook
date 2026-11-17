---
id: "18"
slug: lambda
title: AWS Lambda
file: fast
tier: deep
domains: [2, 3, 4]
tasks: ["2.1", "3.2", "4.2", "2.2"]
services: [lambda]
minutes: {fast: 20, pass: 78, full: 178}
status: ready
updated: 2026-10-13
---

# AWS Lambda

## Predict (2 min)
<!-- section: role=predict; route=fast; minutes=2 -->

Guess before you read. The answers are in the Check section.

**Predict 1.** A job inside a function needs 20 minutes. Can the team raise the timeout so that the job fits? <!-- gist-trap -->

**Predict 2.** A function is slow because its code does heavy calculations. Does giving it more memory also give it more CPU?

**Predict 3.** An upload to Amazon S3 invokes a function, and the function throws an error. Does Lambda try again by itself?

## Look first (3 min)
<!-- section: role=task; route=fast; minutes=3 -->

Open AWS CloudShell and read the concurrency quota of your account in two Regions. Then list which Lambda quotas you can raise; the task creates nothing.

<!-- task:start id=lambda-t01 -->

Look

**It kills the belief.** "Lambda scales without limit, in every Region the same."

> **Cost:** $0.

**Permissions.** `lambda:GetAccountSettings`, `servicequotas:ListAWSDefaultServiceQuotas`

**No permission to create resources?** This task is read-only. It needs no alternative.

1. Open AWS CloudShell. Read the concurrency quota of your account in the current Region, and the part of it that no function reserves.

   ```bash
   aws lambda get-account-settings --query "AccountLimit.{Quota:ConcurrentExecutions,Unreserved:UnreservedConcurrentExecutions}"
   ```

   Expect: Two numbers, Quota and Unreserved. They are equal when no function in this Region reserves concurrency. A new account can show a lower Quota than the chapter: new accounts start with reduced quotas that AWS raises with usage.

2. Run the same command for a second Region, <OTHER_REGION>. Choose a Region you do not work in, for example eu-west-1.

   ```bash
   aws lambda get-account-settings --region <OTHER_REGION> --query "AccountLimit.{Quota:ConcurrentExecutions,Unreserved:UnreservedConcurrentExecutions}"
   ```

   Expect: The two numbers of that Region. Compare them with step 1: each Region shows its own pair.

3. List the default Lambda quotas of the current Region and read the Adjustable column.

   ```bash
   aws service-quotas list-aws-default-service-quotas --service-code lambda --query "Quotas[].[QuotaName,Value,Adjustable]" --output table
   ```

   Expect: A table of quota names, default values and True or False. True marks a quota you can ask to increase. False marks a quota you cannot change.

**Label.** checked against docs, not run in a real account. Checked 2026-10-13.

<!-- task:end -->

## In one breath (3 min)
<!-- section: role=breath; route=fast; minutes=3 -->

> **Say it:** Lambda is a [serverless compute service](../facts/lambda.md#lambda-serverless-manages-infrastructure) that runs code when an event arrives. You pay for the [number of requests served](../facts/lambda.md#lambda-pricing-dimensions) and their duration.

**The problem it solves.** Small jobs on a busy instance wait or stop. With Lambda, each event starts its own run of the code, and you do not [pay for idle capacity](../facts/lambda.md#lambda-no-pay-for-idle-capacity).

Lambda runs code in an **execution environment**. The **handler** is the method that processes each event. The number of requests a function handles at the same time is its **concurrency**.

**Predict the picture.** Two uploads arrive together. How many execution environments run the function?

<details>
<summary>Show the picture</summary>

![A sequence with four participants: an event source, the Lambda service, a warm execution environment and a new execution environment. Two events arrive together. The first goes to the warm environment; for the second, Lambda starts a new environment and runs its initialization first.](../diagrams/svg/lambda-hero.svg)

**Figure.** Each request runs in a free execution environment, and Lambda creates a new one when none is free.

1. An event source starts the function by [direct invocation (push)](../facts/lambda.md#lambda-event-push-or-pull), or Lambda polls a queue through [event source mappings (pull)](../facts/lambda.md#lambda-event-push-or-pull).
2. Lambda sends the request to a free execution environment, so if a warm one is free, [Lambda can reuse the environment](../facts/lambda.md#lambda-warm-start-environment-reuse).
3. When no environment is free, Lambda [downloads your code, starts the environment](../facts/lambda.md#lambda-cold-start-definition), and runs the initialization code: a cold start.
4. The handler processes the event with the permissions of the function's execution role, an [IAM role](../facts/lambda.md#lambda-faq-execution-role).
5. With standard Lambda, each environment supports [a maximum of one invocation at a time](../facts/lambda.md#lambda-managed-instances-multi-concurrency-row), so two requests at once need two environments.

</details>

> **Startup example:** Callvale's worker instance runs small scheduled jobs: register an upload, save results, notify. Each runs for seconds, often in the morning and rarely at night. When the worker is busy, they stop. Callvale wants them to run for each event at no idle cost.

## Words that go together (2 min)
<!-- section: role=words; route=fast; minutes=2 -->

<!-- table: words -->
| Term | Words that go with it | Plain meaning | Do not confuse with |
|---|---|---|---|
| function | **invoke** a function | Code that AWS Lambda runs when an event arrives | instance or container |
| serverless | a serverless **architecture** | You run code without managing servers; AWS manages them | stateless |
| cold start | **avoid** cold starts | The extra delay when Lambda prepares a new environment | warm standby |
| asynchronous (ay-SING-kruh-nus) | an asynchronous **invocation** | The caller does not wait for the function to finish | synchronous |
| idempotent (eye-dem-POH-tent) | **make** the consumer idempotent | The same request twice gives the same result | stateless |
| decouple (dee-KUP-ul) | decouple the tiers **with a queue** | Separate two parts, so one keeps working when the other is slow | decompose |
| stateless (STAYT-less) | a stateless **application tier** | Keeps no memory of earlier requests | serverless |
| latency (LAY-ten-see) | **low** latency | The time between a request and its response | throughput |

## Choose it or not (3 min)
<!-- section: role=choose; route=fast; minutes=3 -->

### A Lambda function or AWS Fargate or Amazon EC2

<!-- table: compare -->
| Question | Lambda function | AWS Fargate | Amazon EC2 |
|---|---|---|---|
| How long can one run last? | Up to [15 minutes per invocation](../facts/lambda.md#lambda-fargate-no-execution-time-limit) | There is [no hard limit on execution time](../facts/lambda.md#lambda-fargate-no-execution-time-limit) | As long as the instance runs |
| What do you pay for? | The [number of requests served](../facts/lambda.md#lambda-pricing-dimensions) and their duration | Per-second resource billing; tends to cost less for [sustained, high-throughput workloads](../facts/lambda.md#lambda-vs-fargate-cost-by-volume) | On-Demand: [You pay only for the seconds](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum) running, with a [60-second minimum](../facts/ec2.md#ec2-on-demand-billing-per-second-60s-minimum) |
| Which work fits? | [Event-driven tasks, unpredictable workloads](../facts/lambda.md#lambda-choose-functions-event-driven-unpredictable) | Containers with [specific resource needs or persistent processes](../facts/lambda.md#lambda-choose-fargate-containers-persistent) | Work that needs [granular control over the compute environment](../facts/ec2.md#ec2-compute-guide-ec2-overhead-justified-for-control) |
| Which servers do you manage? | None: you [run code without provisioning or managing servers](../facts/lambda.md#lambda-serverless-manages-infrastructure) | None: you [run containers without having to manage servers](../facts/ec2.md#ec2-compute-guide-fargate-no-servers-for-containers) | The instances |

**Deciding question:** Does each run finish within minutes after an event, or does the work run long, all day, or need control of the host?

### Function URL or API Gateway or Application Load Balancer

<!-- table: compare -->
| Question | Function URL | Amazon API Gateway | Application Load Balancer (ALB) |
|---|---|---|---|
| What is it best for? | [Simple applications or prototyping](../facts/lambda.md#lambda-furl-recommended-simple-apps) | [Production applications at scale](../facts/lambda.md#lambda-apigw-better-for-production) | An existing ALB that routes [based on path or header values](../facts/lambda.md#lambda-alb-target-rules-sync) |
| API keys and AWS WAF? | No | [API keys for usage plans](../facts/lambda.md#lambda-apigw-extra-features-waf-keys) and [WAF integration for additional security](../facts/lambda.md#lambda-apigw-extra-features-waf-keys) | AWS WAF: [AWS Web Application Firewall (WAF)](../facts/elb.md#elb-waf-integrates-with-alb) rules |
| Charge for the endpoint? | [No additional charges for the URL endpoint](../facts/lambda.md#lambda-furl-no-endpoint-charge) | See chapter 33 <!-- xref: 33 API Gateway pricing --> | See [Elastic Load Balancing](../14-elb/1-fast.md) |

**Deciding question:** Does the API need keys, usage plans or AWS WAF, or only an HTTPS address for one function?

### Reserved or provisioned concurrency

<!-- table: compare -->
| Question | Reserved concurrency | Provisioned concurrency |
|---|---|---|
| What does it do? | Sets aside and caps: you [reserve a subset of your account concurrency limit](../facts/lambda.md#lambda-faq-per-function-concurrency-control) | Keeps [pre-initialized execution environments](../facts/lambda.md#lambda-pc-scales-beyond-setting) ready |
| Does it remove cold starts? | No: the environments start as before | Yes: the function [does not exhibit cold start behavior](../facts/lambda.md#lambda-pc-not-latest-no-cold-start) |
| What does it cost? | It [incurs no additional charges](../facts/lambda.md#lambda-reserved-concurrency-no-charge) | [It increases costs](../facts/lambda.md#lambda-pc-costs-while-idle), also when idle |
| What does it apply to? | The function | A published version or `alias`, [not the $LATEST version](../facts/lambda.md#lambda-pc-not-latest-no-cold-start) |

**Deciding question:** Do you need to guarantee or cap capacity, or to remove cold starts?

## Signals and traps (3 min)
<!-- section: role=signals; route=fast; minutes=3 -->

<!-- table: signals -->
| The stem says | Think | Because | But not if |
|---|---|---|---|
| "runs for seconds after each upload; unpredictable traffic" | a function that events invoke | it suits [event-driven tasks, unpredictable workloads](../facts/lambda.md#lambda-choose-functions-event-driven-unpredictable) | one run lasts longer than [900 seconds](../facts/lambda.md#lambda-timeout-max): Fargate or AWS Batch |
| "must not overwhelm the database" | reserved concurrency | it can [limit how high your function can scale](../facts/lambda.md#lambda-bp-reserved-protects-downstream) | every request must be served: RDS Proxy |
| "first requests after a quiet period are slow" | provisioned concurrency | it is for [latency-sensitive applications](../facts/lambda.md#lambda-faq-pc-when) | Java, Python or .NET, best effort: SnapStart, [as low as sub-second](../facts/lambda.md#lambda-snapstart-vs-pc-guide) |
| "too many connections on the RDS database" | Amazon RDS Proxy | the [connection pooling offered by RDS Proxy](../facts/rds-proxy.md#rds-proxy-lambda-connection-pooling) | key-value data: DynamoDB, because [DynamoDB uses an HTTP API](../facts/lambda.md#lambda-ddb-http-api-no-connections) |
| "keep failed asynchronous events with details" | an on-failure destination | after the retries, [Lambda discards it](../facts/lambda.md#lambda-async-discard-then-destination) unless you [configure a failed-event destination](../facts/lambda.md#lambda-async-discard-then-destination) | an SQS trigger: the source queue's dead-letter queue |
| "reads a private database and calls an internet API" | private subnets and a NAT gateway | they [access the internet through the NAT gateway](../facts/lambda.md#lambda-vpc-public-subnet-no-internet) | the calls go only to S3 or DynamoDB: a virtual private cloud (VPC) gateway endpoint |
| "a simple HTTPS endpoint for one function, lowest cost" | a function URL | it is for [simple applications or prototyping](../facts/lambda.md#lambda-furl-recommended-simple-apps) | clients need API keys, request quotas or AWS WAF: API Gateway |
| "a CPU-heavy function is too slow" | more memory | [increasing the memory can help resolve the compute](../facts/lambda.md#lambda-memory-tuning-cpu-bound) bottleneck | more CPU than a function gets: Fargate, [0.25 vCPUs to 32 vCPUs](../facts/lambda.md#lambda-vs-fargate-cpu-memory-ceilings) |

### Traps

- **Wrong belief:** A quota request raises the timeout above 15 minutes. **Truth:** The maximum timeout is [900 seconds](../facts/lambda.md#lambda-timeout-max), and you cannot raise it. <!-- trap: lambda-trap-timeout-raisable -->
- **Wrong belief:** Reserved concurrency keeps environments warm. **Truth:** It sets aside and caps capacity. Provisioned concurrency keeps [pre-initialized execution environments](../facts/lambda.md#lambda-pc-scales-beyond-setting) ready, and [it increases costs](../facts/lambda.md#lambda-pc-costs-while-idle). <!-- trap: lambda-trap-reserved-keeps-warm -->
- **Wrong belief:** Lambda scales without limit. **Truth:** All functions of an account share one concurrency quota [per AWS Region](../facts/lambda.md#lambda-quota-scope-region-vs-vpc), [1,000](../facts/lambda.md#lambda-concurrent-executions-default) by default; new accounts start with [reduced concurrency and memory quotas](../facts/lambda.md#lambda-new-account-reduced-quotas). Requests above it get a [throttling error (429 status code)](../facts/lambda.md#lambda-throttle-429). <!-- trap: lambda-trap-scales-without-limit -->
- **Wrong belief:** A function in a public subnet reaches the internet. **Truth:** [Connecting a function to a public subnet](../facts/lambda.md#lambda-vpc-public-subnet-no-internet) gives it no internet access. Private subnets [access the internet through the NAT gateway](../facts/lambda.md#lambda-vpc-public-subnet-no-internet). <!-- trap: lambda-trap-public-subnet-internet -->
- **Wrong belief:** EC2 Instance Savings Plans also cover Lambda. **Truth:** [Compute Savings Plans](../facts/lambda.md#lambda-sp-ec2-instance-plans-exclude-lambda) apply to Lambda, but EC2 Instance Savings Plans and Reserved Instances do not. <!-- trap: lambda-trap-ec2-savings-plans-cover-lambda -->

## Changed recently (1 min)
<!-- section: role=changed; route=fast; minutes=1 -->

> **Changed recently:** (2023-12-06) Each function scales on its own.<br>
> **Old:** an account-wide burst, [followed by 500 concurrent executions every minute](../facts/lambda.md#lambda-change-scaling-per-function-2023).<br>
> **Now:** each function adds [1,000 concurrent executions every 10 seconds](../facts/lambda.md#lambda-change-scaling-per-function-2023).<br>
> **The exam probably expects:** the new rule; older questions describe an account-wide burst.<br>
> **Status:** examinable.

> **Changed recently:** (2024-11-18) SnapStart for more runtimes.<br>
> **Old:** [Java functions](../facts/lambda.md#lambda-change-snapstart-python-dotnet-2024).<br>
> **Now:** [now available for Python and .NET managed runtimes](../facts/lambda.md#lambda-change-snapstart-python-dotnet-2024).<br>
> **The exam probably expects:** older questions say that SnapStart is for Java only.<br>
> **Status:** examinable.

> **Changed recently:** (2025-10-24) Larger asynchronous payloads.<br>
> **Old:** [256 KB](../facts/lambda.md#lambda-change-async-payload-1-mb-2025).<br>
> **Now:** [1 MB](../facts/lambda.md#lambda-change-async-payload-1-mb-2025).<br>
> **The exam probably expects:** the old value in older questions; a larger event goes to Amazon S3.<br>
> **Status:** examinable.

> **Changed recently:** (2025-11-30) Lambda Managed Instances.<br>
> **Old:** not available.<br>
> **Now:** functions can run on EC2 instances in your account, for [steady-state or predictable workloads](../facts/lambda.md#lambda-change-managed-instances-launch-2025).<br>
> **The exam probably expects:** standard Lambda, one invocation per environment at a time.<br>
> **Status:** examinable.

## Check (2 min)
<!-- section: role=check; route=fast; minutes=2 -->

**Check 1.** After each upload, a video job runs for most of an hour, with no servers to manage. Where does it run?

<details>
<summary>Answer</summary>

In containers on AWS Fargate, which has [no hard limit on execution time](../facts/lambda.md#lambda-fargate-no-execution-time-limit).

**Predict 1:** No. The maximum timeout is [900 seconds](../facts/lambda.md#lambda-timeout-max), and you cannot raise it.

</details>

**Check 2.** At the largest memory setting, a function's math is still too slow. How much CPU can it get?

<details>
<summary>Answer</summary>

CPU grows [up to 6 vCPU](../facts/lambda.md#lambda-cpu-up-to-6-vcpu). For more, use AWS Fargate.

**Predict 2:** Yes. Lambda allocates CPU [in proportion to the amount of memory](../facts/lambda.md#lambda-cpu-proportional-to-memory).

</details>

**Check 3.** Amazon API Gateway invokes a function, and the function throws an error. Does Lambda try again by itself?

<details>
<summary>Answer</summary>

No. The caller must [retry the invocation manually](../facts/lambda.md#lambda-sync-error-caller-retries), and API Gateway [always relays the error response back](../facts/lambda.md#lambda-apigateway-relays-error).

**Predict 3:** Yes. Amazon S3 invokes it asynchronously, and Lambda tries [two more times](../facts/lambda.md#lambda-async-default-two-retries) by default.

</details>

## Recap from memory (1 min)
<!-- section: role=recap; route=fast; minutes=1 -->

**Recap 1.** Reserved or provisioned concurrency: which one removes cold starts, and which one has no extra charge?

<details>
<summary>Answer</summary>

Provisioned concurrency [does not exhibit cold start behavior](../facts/lambda.md#lambda-pc-not-latest-no-cold-start). Reserved concurrency [incurs no additional charges](../facts/lambda.md#lambda-reserved-concurrency-no-charge).

</details>

**Recap 2.** Which stem phrase points to Amazon API Gateway instead of a function URL?

<details>
<summary>Answer</summary>

"Clients need API keys, request quotas or AWS WAF": API Gateway adds [API keys for usage plans](../facts/lambda.md#lambda-apigw-extra-features-waf-keys).

</details>

**Recap 3.** How does a VPC-attached function reach the internet?

<details>
<summary>Answer</summary>

From private subnets, which [access the internet through the NAT gateway](../facts/lambda.md#lambda-vpc-public-subnet-no-internet).

</details>
