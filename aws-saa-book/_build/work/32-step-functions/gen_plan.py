"""Writes brief.v0.json and mine-plan.json for chapter 32 (plan stage). Run: python3 -I gen_plan.py"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-10-14"
S = "docs/step-functions/latest/dg/"
M = "docs/amazon-mq/latest/developer-guide/"
MG = "docs/amazon-mq/latest/migration-guide/"
A = "docs/appflow/latest/userguide/"
L = "docs/lambda/latest/dg/"
DG = "docs/decision-guides/latest/decision-guides/"
WN = "www/about-aws/whats-new/"
CS = "www/solutions/case-studies/"
NUM, BEH, FAQ = "numbers+changes", "behavior+decisions", "faq"

# (id, bullet, lens, service, question, sources, note, reuse)
D = []


def d(bullet, lens, service, question, sources, note=None, reuse=None):
    D.append((bullet, lens, service, question, sources, note, reuse))


# ---------------- numbers + changes: Step Functions ----------------
d("2.1.K16", NUM, "step-functions",
  "Maximum execution duration of a Standard workflow and of an Express workflow (and maximum execution idle time of each).",
  [S + "service-quotas", S + "choosing-workflow-type"],
  "Exam pair Standard vs Express. Quote the quota row with its header (Quota | Standard | Express) or the comparison row 'Maximum duration'. FREQUENCY says Standard 1 year, Express 5 minutes: hypothesis only.")
d("2.1.K16", NUM, "step-functions",
  "Maximum execution history size of a Standard workflow (events) and of an Express workflow; how long Step Functions keeps the execution history of a closed Standard execution, and whether that can be reduced.",
  [S + "service-quotas", S + "choosing-workflow-type", S + "sfn-best-practices"],
  "The history quota row names the consequence (the execution fails); keep it in the claim.")
d("2.1.K16", NUM, "step-functions",
  "Maximum input or output size for a task, state or execution; what Step Functions recommends when a payload is larger (pass an Amazon S3 location).",
  [S + "service-quotas", S + "sfn-best-practices"],
  "The quota row is the same for Standard and Express; the S3 ARN advice is in sfn-best-practices.")
d("2.1.K16", NUM, "step-functions",
  "Account quotas: registered state machines and activities (default and increased maximum), maximum state machine definition size, maximum request size, maximum open executions per account and Region (and that it does not apply to Express).",
  [S + "service-quotas", WN + "2025/02/aws-step-functions-100-000-state-machines-activities-account"],
  "The account quota table is raw HTML (<tr><td>...) and `tables` does not list it: quote one whole <tr> line or the cell text with --sentence; check M4 accepts it before writing many.")
d("2.1.K16", NUM, "step-functions",
  "State transition throttling: bucket size and refill rate for Standard workflows in the large Regions and in other Regions; Express state transitions; are Standard transition quotas soft?",
  [S + "service-quotas", S + "choosing-workflow-type"],
  "Rows have two header lines (Standard/Express, then Bucket size/Refill rate). Quote the row plus the header text; name the Region scope.")
d("2.1.K16", NUM, "step-functions",
  "StartExecution throttling for Standard vs Express workflows; how StartSyncExecution (Synchronous Express) capacity is handled.",
  [S + "service-quotas", S + "choosing-workflow-type"])
d("2.1.K16", NUM, "step-functions",
  "Distributed Map numbers: maximum parallel child executions in one Map Run, dispatch rates for Express and Standard child executions, maximum open Map Runs; inline Map concurrency limit; is Distributed Map supported in Express workflows?",
  [S + "service-quotas", S + "state-map", S + "state-map-distributed", S + "choosing-workflow-type"])
d("2.1.K16", NUM, "step-functions",
  "Redrive: how long after a Standard execution ends it can be redriven; is redrive supported for Express workflows; maximum redrives of a Map Run.",
  [S + "service-quotas", S + "redrive-executions"])
d("2.1.K16", NUM, "step-functions",
  "Task limits: maximum task execution time and maximum time a task stays in the queue (Standard vs Express); how long a task waiting for a task token can wait; what the Wait state maximum is for each workflow type.",
  [S + "service-quotas", S + "state-wait", S + "connect-to-resource"])
d("2.1.K16", NUM, "step-functions",
  "HTTP Task (call HTTPS APIs) quotas: maximum duration of one HTTP request and the HTTP Task throttle bucket.",
  [S + "service-quotas", S + "call-https-apis"])
d("2.1.K16", NUM, "step-functions",
  "Versions and aliases: maximum published versions and maximum aliases per state machine; tags per resource.",
  [S + "service-quotas", S + "concepts-cd-aliasing-versioning"],
  "Low exam weight; one or two facts are enough.")
d("2.1.S5", NUM, "step-functions",
  "Synchronous Express workflows: what happens when you start one from the console (request expiry) versus the SDK or CLI; how you get the result of an Asynchronous Express workflow.",
  [S + "choosing-workflow-type", S + "synchronous-execution"])
d("2.1.S5", NUM, "step-functions",
  "Step Functions pricing dimensions: Standard is charged per state transition (what counts, retries included); Express is charged per request, duration (rounding) and memory (chunk size); the free tier (state transitions per month, does it expire?).",
  [S + "choosing-workflow-type", "www/step-functions/pricing"],
  "Prefer dimension facts and the free-tier number over per-Region unit prices. The Callvale decision accepts 'a charge for each state transition'.")
d("2.1.K16", NUM, "step-functions",
  "Change: 2025-02-05 registered state machines and activities per account raised (to 100,000); what was the old value, if a saved page states it verbatim.",
  [WN + "2025/02/aws-step-functions-100-000-state-machines-activities-account", S + "service-quotas", S + "document-history"],
  "Change fact with date from the What's New page; current value from service-quotas. Old value only if verbatim on a saved page.")
d("2.1.K16", NUM, "step-functions",
  "Change: Distributed Map (large-scale parallel workflows) launched 2022-12-01; date from the document history row.",
  [S + "document-history", S + "state-map-distributed"],
  "What's New 2022/12 page is robots-disallowed (fetch_failures); use the document-history row of 2022-12-01.")
d("2.1.K16", NUM, "step-functions",
  "Change (FRESHNESS hypothesis): variables and JSONata transformations launched 2024-11-22; date from the document-history row.",
  [S + "document-history", S + "workflow-variables", S + "transforming-data"],
  "What's New 2024/11 page is robots-disallowed; use the history row.")
d("2.1.K16", NUM, "step-functions",
  "Change: redrive (restart failed workflows from the point of failure) launched 2023-11-15; date from the document-history row.",
  [S + "document-history", S + "redrive-executions"],
  "What's New 2023/11 page is robots-disallowed; use the history row.")
d("2.1.K16", NUM, "step-functions",
  "Change: customer managed AWS KMS keys for Step Functions data at rest (2024-07-25); what Step Functions uses by default when no key is chosen.",
  [S + "document-history", S + "encryption-at-rest"])
d("2.1.K16", NUM, "step-functions",
  "Changes: HTTPS endpoints (HTTP Task) and the TestState API (2023-11-26); versions and aliases (2023-06-22); IPv6 dual-stack endpoints (2025-09-18); dates from the history rows or the change feed.",
  [S + "document-history", S + "recent-launches", S + "call-https-apis", S + "concepts-cd-aliasing-versioning"],
  "Low exam weight; one change fact each at most. The dual-stack item has a What's New row only (change feed).")
d("2.1.K16", NUM, "step-functions",
  "Changes after 2026-06: AgentCore agentic reasoning step (2026-06-03) and automatic new AWS service integrations starting with Lambda MicroVMs (What's New page in the corpus); which of them are GA after 2026-07-15 and so 'not examinable yet'?",
  [WN + "2026/06/aws-step-functions-integrations", S + "recent-launches", S + "connect-bedrockagentcore"],
  "Label anything GA after 2026-07-15 not examinable yet.")
d("2.1.S5", NUM, "lambda",
  "Neighbour change (FRESHNESS hypothesis): AWS Lambda durable functions (2025-12-02) let a function run multi-step work for up to one year; how AWS positions durable functions against Step Functions.",
  [L + "durable-functions", L + "durable-step-functions", WN + "2025/12/lambda-durable-multi-step-applications-ai-workflows"],
  "Neighbour facts already exist in data/facts/lambda.jsonl: reuse them; add a fact only when none answers the question.",
  ["lambda-change-durable-functions-2025", "lambda-durable-vs-step-functions-focus", "lambda-faq-durable-vs-step-functions", "lambda-faq-durable-timeout-and-retention"])

# ---------------- numbers + changes: Amazon MQ ----------------
d("2.2.S7", NUM, "mq",
  "Amazon MQ quotas: brokers per Region, connections per broker, destinations per broker, users per broker, configurations, storage per broker, API throttling; which are adjustable?",
  [M + "amazon-mq-limits"],
  "Five tables (Brokers, Configurations, Users, Data Storage, API Throttling) with header 'Limit | Description': adopt rows; the engine (ActiveMQ or RabbitMQ) and instance type often sit inside the description, keep that scope in the claim.")
d("2.2.S7", NUM, "mq",
  "ActiveMQ storage types: Amazon EFS versus Amazon EBS (durability, Availability Zones, latency, throughput); which storage type supports active/standby?",
  [M + "broker-storage", M + "amazon-mq-broker-architecture"])
d("2.2.S7", NUM, "mq",
  "Broker instance types: which instance types each engine supports; which small instance type is for evaluation only or single-instance only; instance types reaching end of support.",
  [M + "broker-instance-types", M + "rmq-broker-instance-types", M + "amazon-mq-release-notes"],
  "Low exam weight; keep to 2 or 3 facts.")
d("2.2.S7", NUM, "mq",
  "Amazon MQ pricing dimensions: broker instance hours, storage, data transfer; pricing differences between single-instance and active/standby or cluster brokers.",
  ["www/amazon-mq/pricing"],
  "Dimension facts, not per-Region prices. FAQ pricing questions are in the faq lens.")
d("2.2.S7", NUM, "mq",
  "Change: cross-Region data replication (CRDR) for ActiveMQ brokers (June 2023); ActiveMQ 5.18 (2024) and 5.19 (2026-02-19) minor versions.",
  [M + "amazon-mq-release-notes", M + "crdr-for-active-mq", M + "activemq-version-management"],
  "What's New 2023/06 CRDR page is robots-disallowed; use the release-notes row (2023-06-21 or 2023-06-23).")
d("2.2.S7", NUM, "mq",
  "Changes for RabbitMQ: quorum queues (2024-07-22, 3.13 and later), RabbitMQ 4.2 with native AMQP 1.0 (2025-11-20), JMS support for RabbitMQ 4.2 and later (2026-01-22), LDAP, HTTP, OAuth 2.0 and mTLS authentication (2025-09 to 2026-01).",
  [M + "amazon-mq-release-notes", M + "quorum-queues", M + "rabbitmq-jms-support", M + "rabbitmq-supported-protocols",
   WN + "2025/11/amazon-mq-rabbitmq-42", WN + "2026/01/amazon-mq-jms-spec-rabbitmq"],
  "These change the old exam assumption 'RabbitMQ on Amazon MQ means AMQP 0-9-1 only, JMS means ActiveMQ'. One change fact per item.")
d("2.2.S7", NUM, "mq",
  "Changes in networking and security: AWS PrivateLink for the Amazon MQ API (2024-12-10), dual-stack endpoints (2024-11, 2025-04), AWS KMS customer managed keys for RabbitMQ (2023-02), private networking for RabbitMQ (2026-06-18), configurable storage for RabbitMQ (2026-07-15 What's New; 2026-07-14 history row).",
  [M + "amazon-mq-release-notes", M + "connect-to-amazonmq", M + "private-networking", M + "data-protection",
   M + "best-practices-configurable-storage", WN + "2026/07/amazon-mq-rabbitmq-configurable-storage"],
  "Configurable storage sits on the 2026-07-15 boundary: record both dates verbatim and let the adjudicator apply the 'GA after 2026-07-15' rule.")
d("2.2.S7", NUM, "mq",
  "Engine version support: what happens when an engine version reaches end of support; how minor version upgrades are managed for RabbitMQ 3.13 and later.",
  [M + "activemq-version-management", M + "rabbitmq-version-support", M + "amazon-mq-release-notes"],
  "Low exam weight.")

# ---------------- numbers + changes: AppFlow ----------------
d("2.1.S3", NUM, "appflow",
  "AppFlow quotas: flows per account, flow runs per month, concurrent flow runs, maximum flow run time, connector profiles per account (soft quota).",
  [A + "service-quotas"],
  "The page uses list lines ('Number of flows per account: 1,000'); quote the whole line with --heading or --sentence. Check the scope (Region-specific unless noted).")
d("2.1.S3", NUM, "appflow",
  "AppFlow schedule frequency (up to once per minute; Salesforce limit), Salesforce event buffer and export size per flow run, EventBridge event size limit.",
  [A + "service-quotas", A + "salesforce", A + "EventBridge"])
d("2.1.S3", NUM, "appflow",
  "AppFlow pricing dimensions: price per flow run and per GB of data processed; extra charges (for example AWS PrivateLink, AWS KMS).",
  ["www/appflow/pricing"])
d("2.1.S3", NUM, "appflow",
  "AppFlow changes since 2022-07: AWS Glue Data Catalog integration (2022-11-17), CloudWatch metrics (2022-11-18), over 50 connectors (2022-11-30), Salesforce record deletion (2022-09), JWT for Salesforce (2023-05).",
  [A + "doc-history", A + "flows-catalog", A + "monitoring-cloudwatch"],
  "Low exam weight: one or two change facts.")

# ---------------- behavior + decisions: Step Functions ----------------
d("2.1.K16", BEH, "step-functions",
  "What Step Functions is in one sentence (workflows, state machines, states, tasks); is it serverless?",
  [S + "welcome", S + "concepts-statemachines", DG + "choosing-aws-serverless-service", "docs/whitepapers/latest/aws-overview/application-integration"],
  "Existing fact step-functions-decision-workflows-category (mech-pass) may be reused.",
  ["step-functions-decision-workflows-category"])
d("2.1.K16", BEH, "step-functions",
  "Execution semantics: Standard exactly-once, Asynchronous Express at-least-once, Synchronous Express at-most-once; which workflow type suits non-idempotent actions such as payments; idempotency behaviour when starting an execution with the same name.",
  [S + "choosing-workflow-type"])
d("2.1.K16", BEH, "step-functions",
  "What Express workflows cannot do: the .sync (Run a Job) and .waitForTaskToken (callback) patterns, Distributed Map, activities; can the workflow type be changed after creation?",
  [S + "choosing-workflow-type", S + "connect-to-resource"])
d("2.1.K16", BEH, "step-functions",
  "Typical uses of each type: Standard for long-running, durable, auditable workflows; Express for high-volume event processing (IoT ingestion, streaming, mobile backends); how each is billed.",
  [S + "choosing-workflow-type", S + "welcome", DG + "choosing-aws-serverless-service", "docs/wellarchitected/latest/serverless-applications-lens/step-functions-workflows"])
d("2.1.K16", BEH, "step-functions",
  "Error handling: what Retry does (fields and their defaults: MaxAttempts, IntervalSeconds, BackoffRate, MaxDelaySeconds, JitterStrategy), what Catch does, what happens to the execution when a state fails with no Retry or Catch; States.ALL.",
  [S + "concepts-error-handling", S + "sfn-best-practices"],
  "Defaults are 'default' facts: quote the field description that states the default. Each retry is billed as a state transition (pricing page; see the pricing demand item).")
d("2.1.K16", BEH, "step-functions",
  "Timeouts: TimeoutSeconds and HeartbeatSeconds on a Task state; the default when no timeout is set and why AWS recommends setting one (stuck executions).",
  [S + "state-task", S + "sfn-best-practices", S + "connect-to-resource"])
d("2.1.K16", BEH, "step-functions",
  "State types and what each does: Task, Choice, Parallel, Map, Wait, Pass, Succeed, Fail.",
  [S + "workflow-states", S + "state-task", S + "state-choice", S + "state-parallel", S + "state-map", S + "state-wait"],
  "One short capability fact per state type, quoted from its own page.")
d("2.1.K16", BEH, "step-functions",
  "Service integration patterns: Request Response, Run a Job (.sync), Wait for a Callback with a Task Token (.waitForTaskToken); what each waits for.",
  [S + "connect-to-resource", S + "integrate-services"])
d("2.1.K16", BEH, "step-functions",
  "Human approval: how a workflow pauses for a person (task token, SendTaskSuccess or SendTaskFailure), how long it can wait, and the heartbeat option.",
  [S + "tutorial-human-approval", S + "connect-to-resource"],
  "FREQUENCY sub-topic 'human approval'.")
d("2.1.K16", BEH, "step-functions",
  "Activities: what an activity is, where an activity worker can run (EC2, on premises, any compute), how the worker gets work (GetActivityTask polling).",
  [S + "concepts-activities"])
d("2.1.K16", BEH, "step-functions",
  "Integrations: optimized integrations versus AWS SDK integrations (how many AWS services the SDK integrations reach), and the HTTP Task for third-party HTTPS APIs (EventBridge connection for authentication).",
  [S + "integrate-services", S + "supported-services-awssdk", S + "call-https-apis", L + "with-step-functions"],
  "Counts of services ('over 200', '220+') drift: quote the page as it stands today and mark volatility frequently-changing.")
d("2.1.K16", BEH, "step-functions",
  "Map state: Inline mode versus Distributed mode (what each is for, input from an S3 bucket or a large JSON or CSV file, child workflow executions).",
  [S + "state-map", S + "state-map-distributed"])
d("2.1.K16", BEH, "step-functions",
  "Choice and Parallel states: branching on input values; running branches in parallel and how a failure in one branch affects the Parallel state.",
  [S + "state-choice", S + "state-parallel"])
d("2.1.S3", BEH, "step-functions",
  "How executions start: EventBridge rules, EventBridge Scheduler, API Gateway, Lambda, a parent workflow (nested workflows), the SDK; and Step Functions sends execution status-change events to EventBridge.",
  [S + "statemachine-starting", S + "using-eventbridge-scheduler", S + "concepts-nested-workflows", S + "eventbridge-integration", S + "choosing-workflow-type"])
d("2.1.S5", BEH, "step-functions",
  "Synchronous Express workflows behind API Gateway: what they return and why they suit microservice orchestration without extra code for retries and parallel tasks.",
  [S + "synchronous-execution", S + "choosing-workflow-type"])
d("2.1.K16", BEH, "step-functions",
  "Visibility of each run: console graph and event history for Standard; Express history only through CloudWatch Logs; X-Ray tracing; CloudWatch metrics such as ExecutionsFailed and ExecutionThrottled.",
  [S + "concepts-view-execution-details", S + "cw-logs", S + "concepts-xray-tracing", S + "monitoring-logging", S + "choosing-workflow-type"],
  "Callvale's need: 'a visible history for each call'.")
d("2.1.K16", BEH, "step-functions",
  "Redrive and long workflows: redrive restarts a failed Standard execution from the failed step (not from the start); continue-as-new by starting a new execution to stay under the history quota.",
  [S + "redrive-executions", S + "tutorial-continue-new", S + "sfn-best-practices"])
d("2.1.K16", BEH, "step-functions",
  "Security: the state machine's IAM execution role; interface VPC endpoints (AWS PrivateLink) so resources in a VPC reach Step Functions without the internet; encryption at rest (AWS owned key by default, customer managed key option); cross-account access.",
  [S + "procedure-create-iam-role", S + "vpc-endpoints", S + "encryption-at-rest"],
  "Secure domain is the reader's weakest (45%): cover role and VPC endpoint carefully.")
d("2.1.K16", BEH, "step-functions",
  "Best practices that become exam answers: set timeouts, pass large payloads through S3, avoid the history quota, choose Express for high-volume short work to cut cost, handle transient Lambda service exceptions with Retry.",
  [S + "sfn-best-practices"])
d("2.1.S3", BEH, "step-functions",
  "Loose coupling: Step Functions as an intermediate layer between components (Well-Architected REL04-BP02); the decision guide's 'Choose' rows for orchestration versus queues and event buses.",
  ["docs/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system", DG + "application-integration-on-aws-how-to-choose", DG + "sns-or-sqs-or-eventbridge"],
  "A neighbour fact already exists: sqs-wa-loose-coupling-via-intermediate-durable-layer.",
  ["sqs-wa-loose-coupling-via-intermediate-durable-layer"])
d("2.1.S5", BEH, "step-functions",
  "Step Functions versus chained Lambda functions: why one Lambda function calling another is an anti-pattern; when the Lambda guide recommends Step Functions (sequencing, complex error handling, waiting); Lambda maximum timeout as the contrast.",
  [L + "concepts-event-driven-architectures", L + "with-step-functions", L + "durable-step-functions"],
  "Neighbour facts exist in lambda.jsonl: reuse them first.",
  ["lambda-chaining-anti-pattern-sqs-or-step-functions", "lambda-step-functions-orchestrate-errors", "lambda-timeout-max", "lambda-trigger-step-functions-sync-or-async"])
d("2.1.K16", BEH, "step-functions",
  "Step Functions versus Amazon MWAA (Apache Airflow): when AWS points to MWAA (open source, portability) and when to Step Functions; the decision guide's orchestration row.",
  ["docs/whitepapers/latest/microservices-on-aws/distributed-systems-components", DG + "application-integration-on-aws-how-to-choose"],
  "The microservices whitepaper paragraph 'Orchestration and state management' may sit on distributed-systems-components or a sub-page; if it is not on the saved page, search the snapshot and record where it is.")
d("2.1.S5", BEH, "step-functions",
  "Serverless decision guide: Step Functions as the orchestration choice; Standard versus Express summaries; pay-per-use for Express; no servers to manage.",
  [DG + "choosing-aws-serverless-service"])
d("2.1.K16", BEH, "step-functions",
  "Facts behind Callvale's decision (STARTUP.md chapter 32): managed retries without hand-written loops (Retry), waiting without paying for compute (Wait state or callback; Standard billed per transition, not per second), a visible history for each call (execution history), a Standard workflow for six steps that can run longer than five minutes, and the accepted costs: a workflow language (Amazon States Language, JSON) and a charge for each state transition.",
  [S + "concepts-error-handling", S + "state-wait", S + "choosing-workflow-type", S + "concepts-amazon-states-language", S + "concepts-view-execution-details", "www/step-functions/pricing"],
  "Story values (six steps, month 13) are story data, never facts. Ground only the AWS behaviour each reason names; if a reason has no AWS sentence, record not-found and the writer changes the stated reason.")
d("2.1.K16", BEH, "step-functions",
  "Amazon States Language: what it is (JSON-based, structured); JSONPath versus JSONata query languages and workflow variables.",
  [S + "concepts-amazon-states-language", S + "transforming-data", S + "workflow-variables"])
d("2.1.S3", BEH, "step-functions",
  "Use cases AWS lists for Step Functions: orchestrating Lambda functions, branching, error handling, human-in-the-loop, parallel processing, dynamic parallelism (Map), data processing and machine learning pipelines.",
  [S + "use-cases", S + "welcome"])

# ---------------- behavior + decisions: Amazon MQ ----------------
d("2.2.S7", BEH, "mq",
  "What Amazon MQ is: a managed message broker service for Apache ActiveMQ and RabbitMQ; migrating existing brokers without rewriting messaging code; what AWS manages for you.",
  [M + "welcome", DG + "application-integration-on-aws-how-to-choose"],
  "Existing fact mq-welcome-migrate-without-rewriting-messaging-code (mech-pass) may be reused.",
  ["mq-welcome-migrate-without-rewriting-messaging-code"])
d("2.2.S7", BEH, "mq",
  "Protocols and APIs: which protocols Amazon MQ for ActiveMQ supports (JMS, NMS, AMQP, STOMP, MQTT, OpenWire, WebSocket) and which Amazon MQ for RabbitMQ supports (AMQP 0-9-1, AMQP 1.0 on 4.2 and later; JMS through the RabbitMQ JMS client on 4.2 and later).",
  [M + "welcome", M + "working-with-activemq", M + "amazon-mq-basic-elements", M + "rabbitmq-supported-protocols", M + "rabbitmq-jms-support", M + "working-with-rabbitmq"],
  "Stem signal 'existing JMS, AMQP or MQTT application' points to Amazon MQ. Version conditions (4.2 and later) belong in the claim.")
d("2.2.S7", BEH, "mq",
  "ActiveMQ deployment modes: single-instance broker versus active/standby broker (two brokers in two Availability Zones, a redundant pair); how clients fail over (failover transport, two endpoints, one active); network of brokers.",
  [M + "amazon-mq-broker-architecture", M + "amazon-mq-basic-elements", M + "network-of-brokers"])
d("2.2.S7", BEH, "mq",
  "RabbitMQ deployment modes: single-instance broker versus cluster deployment (three nodes behind a Network Load Balancer, across Availability Zones); quorum queues as the replicated queue type.",
  [M + "rabbitmq-broker-architecture", M + "working-with-rabbitmq", M + "quorum-queues"])
d("2.2.S7", BEH, "mq",
  "Cross-Region data replication (CRDR) for ActiveMQ: asynchronous replication from a primary broker to a replica broker in another Region; only for active/standby brokers; how promotion or failover is started.",
  [M + "crdr-for-active-mq", M + "create-replica-broker", M + "initate-failover"])
d("2.2.S7", BEH, "mq",
  "Networking: brokers run in your VPC; public versus private brokers (can accessibility change after creation?); subnets in different Availability Zones for active/standby and cluster; security groups; AWS PrivateLink only for the Amazon MQ API.",
  [M + "configuring-private-broker", M + "connect-to-amazonmq", M + "amazon-mq-access", M + "private-networking"])
d("2.2.S7", BEH, "mq",
  "Security: encryption at rest with AWS KMS (AWS owned key by default, customer managed key option) and in transit with TLS; broker authentication (native users, LDAP for ActiveMQ; OAuth 2.0, IAM, LDAP, HTTP, certificates for RabbitMQ); IAM for the Amazon MQ API.",
  [M + "data-protection", M + "amazon-mq-access", M + "security-authentication-authorization"])
d("2.2.S7", BEH, "mq",
  "Maintenance and resilience: what happens during the maintenance window for a single-instance broker versus an active/standby or cluster broker; Amazon MQ resilience statement.",
  [M + "maintaining-brokers", M + "disaster-recovery-resiliency"])
d("2.1.S3", BEH, "mq",
  "Amazon MQ versus Amazon SQS and Amazon SNS: when AWS recommends Amazon MQ (existing applications on standard protocols and APIs) and when SQS or SNS (new applications); consumers stay connected to the broker (unlike SQS); the decision guide's statements about message size and retention.",
  [DG + "application-integration-on-aws-how-to-choose", M + "welcome", M + "amazon-mq-basic-elements"],
  "FREQUENCY pair 'Amazon MQ vs SQS/SNS'. The FAQ answer lives in the faq lens; record here the guide and decision-guide sentences.")
d("2.2.S7", BEH, "mq",
  "Migration: the migration guide's approaches (re-platforming a self-managed ActiveMQ, RabbitMQ, IBM MQ or TIBCO EMS broker to Amazon MQ), and migrating without service interruption.",
  [MG + "concept-chapter-about", MG + "migration-approaches", MG + "interruption-scenarios", MG + "rabbitmq-migration-guide"])
d("2.2.S7", BEH, "mq",
  "Well-Architected and serverless guidance: Amazon MQ as a bridge (service bus) when redesigning legacy applications (REL03-BP01); Lambda event source mappings that read from Amazon MQ.",
  ["docs/wellarchitected/latest/reliability-pillar/rel_service_architecture_monolith_soa_microservice", DG + "choosing-aws-serverless-service"])
d("2.2.S7", BEH, "mq",
  "Facts behind Callvale's Peldon decision (stage 4): an existing ActiveMQ broker whose application code cannot change moves to Amazon MQ for ActiveMQ; an active/standby broker across two Availability Zones; clients connect with the failover transport.",
  [M + "welcome", M + "amazon-mq-broker-architecture", M + "amazon-mq-basic-elements"],
  "Story values (1 ActiveMQ broker, month 25, 4 engineers) are story data, never facts.")

# ---------------- behavior + decisions: AppFlow ----------------
d("2.1.S3", BEH, "appflow",
  "What Amazon AppFlow is: a fully managed integration service that transfers data between SaaS applications (Salesforce, SAP, Slack, ...) and AWS services (Amazon S3, Amazon Redshift) without code; in both directions.",
  [A + "what-is-appflow", A + "app-specific", "docs/whitepapers/latest/aws-overview/application-integration"])
d("2.1.S3", BEH, "appflow",
  "Flow triggers: run on demand, on a schedule (full or incremental transfer), or on an event from the source application.",
  [A + "flow-triggers", A + "flows", A + "general"])
d("2.1.S3", BEH, "appflow",
  "Data transformation in a flow: field mapping, filtering, validation, masking, partitioning and aggregation of output; cataloging output in the AWS Glue Data Catalog.",
  [A + "what-is-appflow", A + "flows", A + "flows-catalog", A + "s3"])
d("2.1.S3", BEH, "appflow",
  "Security: encryption in transit and at rest with AWS KMS (AWS managed key by default, customer managed key option); private flows over AWS PrivateLink; how connection credentials are stored.",
  [A + "data-protection", A + "private-flows", A + "connections", A + "infrastructure-security"])
d("2.1.S3", BEH, "appflow",
  "Salesforce connector: Salesforce as source and destination; Salesforce events (change data capture) as an event trigger; which Salesforce API AppFlow uses for large transfers.",
  [A + "salesforce"])
d("2.1.S3", BEH, "appflow",
  "Facts behind Callvale's AppFlow use (stage 4): scheduled flows from Salesforce to Amazon S3 for the data lake, no code to write, encryption by default.",
  [A + "what-is-appflow", A + "flow-triggers", A + "s3", A + "salesforce", A + "data-protection"],
  "Story only names 'Amazon AppFlow from Salesforce to the data lake'; ground the AWS behaviour only.")

# ---------------- behavior: case studies ----------------
d("2.1.K16", BEH, "step-functions",
  "Real company example: Step Functions Distributed Map at scale (Vertex Pharmaceuticals or Capital One): what they did and one measured result.",
  [CS + "vertex-pharmaceuticals-distributed-map", CS + "capital-one-distributed-map"],
  "Case-study facts: kind case-study, quote at most 25 words.")
d("2.1.K16", BEH, "step-functions",
  "Real company example close to a startup: CyberGRX (startup, Distributed Map for ML workflows) or OneMain Financial (Step Functions for security forensics).",
  [CS + "cybergrx-step-functions-case-study", CS + "onemain-financial-aws-sfn-case-study"],
  "Case-study facts: kind case-study, quote at most 25 words.")
d("2.2.S7", BEH, "mq",
  "Real company example: Shgardi used Amazon MQ for backend connectivity between microservices on Amazon EKS.",
  [CS + "shgardi"],
  "Armut and Qivos redirect to the listing page (fetch_failures). Quote at most 25 words.")
d("2.1.S3", BEH, "appflow",
  "Real company example: Save the Children Spain used Amazon AppFlow to ingest Salesforce data into Amazon S3.",
  [CS + "save-the-children-spain-devoteam"],
  "Quote at most 25 words.")

# ---------------- FAQ: Step Functions ----------------
SF = "www/step-functions/faqs"
d("2.1.K16", FAQ, "step-functions", "FAQ: What is AWS Step Functions; what are the benefits of orchestration; common use cases; how does it work? (FAQ 1 to 4)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: How does Step Functions connect to and coordinate other AWS services and third-party applications? (FAQ 5, 18, 19)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: My workflow has properties of both Standard and Express workflows; how do I get the best of both? (FAQ 8)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: How does Step Functions support parallelism; how does it process a large dataset in Amazon S3? (FAQ 9, 21)", [SF])
d("2.1.S3", FAQ, "step-functions", "FAQ: When should I use Step Functions versus Amazon SQS? (FAQ 15)", [SF], "Key comparison for the Signals table.")
d("2.1.K16", FAQ, "step-functions", "FAQ: When should I use Step Functions versus Amazon SWF? (FAQ 16)", [SF])
d("2.1.S3", FAQ, "step-functions", "FAQ: How do Step Functions HTTPS endpoints relate to EventBridge API destinations? (FAQ 17)", [SF])
d("2.1.S3", FAQ, "step-functions", "FAQ: How does Step Functions work with Amazon API Gateway and with Amazon EventBridge? (FAQ 22, 23)", [SF])
d("2.1.S5", FAQ, "step-functions", "FAQ: What is Step Functions versus AWS Lambda; is Step Functions serverless? (FAQ 24, 25)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: How do logging and monitoring work; what happens if an Express workflow fails because of exhausted retries or an unmanaged exception? (FAQ 26, 27)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: Can I access Step Functions from resources in my VPC without connecting to the internet? (FAQ 29)", [SF])
d("2.1.K16", FAQ, "step-functions", "FAQ: Variables and JSONata: what they are and whether existing workflows can use them. (FAQ 10 to 14; one or two facts)", [SF], "Low exam weight.")

# ---------------- FAQ: Amazon MQ ----------------
MF = "www/amazon-mq/faqs"
d("2.2.S7", FAQ, "mq", "FAQ: What is Amazon MQ; who should use it (versus Amazon SQS and Amazon SNS); what does it manage; when use it versus running ActiveMQ or RabbitMQ on EC2 yourself? (FAQ 1 to 4)", [MF], "FAQ 2 holds the MQ versus SQS/SNS guidance.")
d("2.2.S7", FAQ, "mq", "FAQ: How do I migrate if I use a different message broker than ActiveMQ or RabbitMQ? (FAQ 7)", [MF])
d("2.2.S7", FAQ, "mq", "FAQ: What storage types are available for ActiveMQ; what is a network of brokers? (FAQ 15, 16)", [MF])
d("2.1.S3", FAQ, "mq", "FAQ: How does Amazon MQ work with other AWS services? (FAQ 25)", [MF])
d("2.2.S7", FAQ, "mq", "FAQ: How do I ensure high availability; do the underlying EC2 instances show in my console; what do I provision? (FAQ 26 to 28)", [MF])
d("2.2.S7", FAQ, "mq", "FAQ: Can I change broker configurations; how do I use my own keys to encrypt data? (FAQ 29, 30)", [MF])
d("2.2.S7", FAQ, "mq", "FAQ: How am I charged; do I pay for inter-node data transfer on RabbitMQ; is there Reserved Instance pricing; do I pay for boot volumes? (FAQ 31 to 34)", [MF])
d("2.2.S7", FAQ, "mq", "FAQ: Engine versions: which versions are supported, how new versions arrive, what happens at end of support. (FAQ 9 to 13, 18 to 22; one or two facts)", [MF], "Low exam weight; prefer the end-of-support behaviour.")

# ---------------- FAQ: AppFlow ----------------
AF = "www/appflow/faqs"
d("2.1.S3", FAQ, "appflow", "FAQ: What is Amazon AppFlow; what are its benefits; example flows. (FAQ 1, 2, 5)", [AF])
d("2.1.S3", FAQ, "appflow", "FAQ: Which AWS services and SaaS applications are supported as sources and destinations? (FAQ 4, 9)", [AF])
d("2.1.S3", FAQ, "appflow", "FAQ: What trigger mechanisms are available for flows? (FAQ 6)", [AF])
d("2.1.S3", FAQ, "appflow", "FAQ: Public APIs exist for my SaaS application; what additional value does AppFlow bring? (FAQ 8)", [AF])
d("2.1.S3", FAQ, "appflow", "FAQ: Is AWS PrivateLink required for AppFlow to connect to a SaaS application; how do I set up encryption keys? (FAQ 12, 13)", [AF])
d("2.1.S3", FAQ, "appflow", "FAQ: When should I use AppFlow versus AWS Glue, AWS DataSync or Amazon EventBridge? (FAQ 14 to 16)", [AF], "Key comparisons for the Signals table.")
d("2.1.S3", FAQ, "appflow", "FAQ: Does AppFlow have an SLA; can it be deployed with CloudFormation; does it support CloudTrail? (FAQ 7, 17, 18)", [AF], "Low exam weight.")

demand = []
for i, (bullet, lens, service, q, sources, note, reuse) in enumerate(D, 1):
    item = {"id": "d%03d" % i, "bullet": bullet, "lens": lens, "service": service, "question": q,
            "status": "open", "facts": [], "sources": sources}
    if note:
        item["note"] = note
    if reuse:
        item["reuse_candidates"] = reuse
    demand.append(item)

fetch_failures = [
    {"url": "https://aws.amazon.com/about-aws/whats-new/2023/11/aws-step-functions-restarting-workflows-failure/",
     "reason": "robots.txt disallows (exit 4); use the document-history row of 2023-11-15 and redrive-executions"},
    {"url": "https://aws.amazon.com/about-aws/whats-new/2022/12/aws-step-functions-large-scale-parallel-workflows-data-processing-serverless-applications/",
     "reason": "robots.txt disallows (exit 4); use the document-history row of 2022-12-01 and state-map-distributed"},
    {"url": "https://aws.amazon.com/about-aws/whats-new/2024/11/aws-step-functions-variables-jsonata-transformations/",
     "reason": "robots.txt disallows (exit 4); use the document-history row of 2024-11-22, workflow-variables and transforming-data"},
    {"url": "https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-mq-cross-region-data-replication-activemq/",
     "reason": "robots.txt disallows (exit 4); use the Amazon MQ release-notes rows of 2023-06-21 and 2023-06-23 and crdr-for-active-mq"},
    {"url": "https://aws.amazon.com/solutions/case-studies/armut-case-study/",
     "reason": "redirects to the generic case-study listing page (464,207 bytes, title 'Customer Success Stories'); not usable as evidence"},
    {"url": "https://aws.amazon.com/solutions/case-studies/Qivos-Case-Study/",
     "reason": "redirects to the generic case-study listing page; not usable as evidence"},
]

batch_files = ["urls-a.txt", "urls-b.txt", "urls-c.txt", "urls-d.txt", "urls-e.txt"]
sources_ok = []
for bf in batch_files:
    for line in open(os.path.join(HERE, bf)):
        u = line.strip()
        if u and u not in [f["url"] for f in fetch_failures]:
            sources_ok.append(u)

brief = {
    "chapter": "32",
    "title": "Step Functions, Amazon MQ and AppFlow",
    "template": "medium",
    "made_by": "plan-32",
    "made": TODAY,
    "sources_fetched": len(sources_ok),
    "fetch_failures": fetch_failures,
    "sources": {
        "registry_urls": "all 14 URLs of sources.pages, faq, history, quotas and pricing are in the corpus (batch A)",
        "batch_files": ["_build/work/32-step-functions/" + b for b in batch_files],
        "batch_results": ["_build/work/32-step-functions/fetch-%s.txt" % c for c in "abcde"],
        "guide_indexes": ["_build/corpus/index/step-functions-dg.json", "_build/corpus/index/amazon-mq-developer-guide.json",
                          "_build/corpus/index/amazon-mq-migration-guide.json", "_build/corpus/index/appflow-userguide.json"],
        "feeds": {
            "faq_index": ["_build/corpus/faq/step-functions.jsonl", "_build/corpus/faq/amazon-mq.jsonl", "_build/corpus/faq/appflow.jsonl"],
            "changes_feed": ["_build/corpus/changes/step-functions.jsonl", "_build/corpus/changes/mq.jsonl", "_build/corpus/changes/appflow.jsonl"],
            "cases_index": "_build/corpus/cases/index.jsonl"},
        "work_files": ["faq-step-functions.txt", "faq-mq.txt", "faq-appflow.txt", "changes-step-functions.txt", "changes-mq.txt",
                       "changes-appflow.txt", "cases-step-functions.txt", "cases-mq.txt", "cases-appflow.txt", "pages-sfn.txt"],
        "reused_from_corpus": ["docs/lambda/latest/dg/with-step-functions", "docs/lambda/latest/dg/durable-step-functions",
                               "docs/lambda/latest/dg/durable-functions", "docs/lambda/latest/dg/concepts-event-driven-architectures",
                               "docs/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system",
                               "docs/whitepapers/latest/microservices-on-aws/communication-mechanisms",
                               DG + "sns-or-sqs-or-eventbridge", DG + "choosing-aws-serverless-service"],
    },
    "research_input": {
        "frequency": "FREQUENCY.md rank 38 of 42 (no first-hand report); the exam guide names Step Functions in 2.1.K16. Sub-topics: orchestration with state, retries and human approval; migrating an existing broker without code changes. Pairs: Step Functions vs SQS vs chained Lambda functions; Standard vs Express (durations from the guide); Amazon MQ vs SQS/SNS (existing JMS, AMQP or MQTT broker that cannot change). Stem signals: 'minimal code changes', 'cannot modify the application' (Amazon MQ). Step Functions is the medium-depth service; Amazon MQ and AppFlow are recognise-only service cards.",
        "freshness": "FRESHNESS.md: Step Functions variables and JSONata (2024-11-22); Lambda durable functions (2025-12) as a new option for long workflows. Amazon MQ and AppFlow were not researched in depth. Found at plan, not in FRESHNESS: Distributed Map (2022-12-01), redrive (2023-11-15), HTTPS endpoints and TestState (2023-11-26), versions and aliases (2023-06-22), customer managed keys (2024-07-25), 100,000 state machines per account (2025-02-05), IPv6 (2025-09-18), AgentCore step (2026-06-03), automatic new integrations (2026-09-15, not examinable yet); Amazon MQ CRDR for ActiveMQ (2023-06), KMS for RabbitMQ (2023-02), quorum queues (2024-07-22), PrivateLink for the MQ API (2024-12-10), RabbitMQ 4.2 with AMQP 1.0 (2025-11-20), JMS for RabbitMQ (2026-01-22), RabbitMQ private networking (2026-06-18), configurable storage (2026-07-15, boundary), RabbitMQ 4.3 (2026-09-10, not examinable yet); AppFlow Glue Data Catalog and CloudWatch metrics (2022-11).",
        "naming": "Current names: AWS Step Functions (Standard workflows, Express workflows), Amazon MQ (Amazon MQ for ActiveMQ, Amazon MQ for RabbitMQ), Amazon AppFlow. Amazon States Language. AWS SDK integrations and optimized integrations.",
        "story": "STARTUP.md chapter 32 (stage 2, month 13): the function chain of P2 waits in loops and nobody sees where a call stopped. Six steps: convert, transcribe, analyze, summarize, save, notify. Needs managed retries, waiting at no compute cost, a visible history per call. Decision: more logging / a workflow engine on EC2 / AWS Step Functions state machine call-pipeline (Standard workflow). Accepts a workflow language and a charge per state transition. Stage 4: Amazon MQ for Peldon's ActiveMQ broker; Amazon AppFlow from Salesforce to the data lake. Story numbers are story data, never facts."
    },
    "demand": demand,
}

LENSES = {
    NUM: {"file_prefix": "facts-numbers-", "by": "mine-32-numbers",
          "job": "Every number, limit, default and price dimension for Step Functions, Amazon MQ and AppFlow: adopt rows from the three quota pages first, then the workflow-type comparison, the Map, redrive and HTTP Task pages, then the pricing pages for dimensions and the Step Functions free tier. Then one change fact per change item with the date from the document-history or release-notes row (verbatim) or the What's New page in the corpus, and a pointer to the current-truth fact. Kinds: limit, quota, default, price, change."},
    BEH: {"file_prefix": "facts-behavior-", "by": "mine-32-behavior",
          "job": "Can / cannot / only / by default claims and decision facts: Standard vs Express semantics and restrictions, error handling, timeouts, state types, integration patterns, human approval, activities, Map, starting executions, observability, redrive, security; Amazon MQ engines, protocols, deployment modes, CRDR, networking, security, maintenance, migration, MQ vs SQS/SNS; AppFlow triggers, transformations, security, Salesforce; neighbour comparisons (SQS, chained Lambda functions, durable functions, MWAA); the facts behind Callvale's decisions; four case-study facts. Kinds: behavior, capability, restriction, default, decision, case-study."},
    FAQ: {"file_prefix": "facts-faq-", "by": "mine-32-faq",
          "job": "Verbatim FAQ answers for the FAQ quick-fire section (pick the 8 to 10 strongest, mostly Step Functions, plus the MQ and AppFlow comparisons) and for the Signals table. Quote whole sentences from the FAQ snapshots. Where an FAQ answer disagrees with a guide, record the guide as current truth and note the FAQ wording in the demand record instead of adding a contradicting fact."},
}

lens_pages = {NUM: [], BEH: [], FAQ: []}
lens_demand = {NUM: [], BEH: [], FAQ: []}
for item in demand:
    lens_demand[item["lens"]].append(item["id"])
    for s in item["sources"]:
        if s not in lens_pages[item["lens"]]:
            lens_pages[item["lens"]].append(s)
# extra pages each lens should read
for extra in [S + "document-history", M + "amazon-mq-release-notes", MG + "amazon-mq-mig-guide-release-notes", A + "doc-history", S + "recent-launches"]:
    if extra not in lens_pages[NUM]:
        lens_pages[NUM].append(extra)
for extra in [S + "connect-lambda", S + "connect-sqs", "docs/whitepapers/latest/microservices-on-aws/communication-mechanisms"]:
    if extra not in lens_pages[BEH]:
        lens_pages[BEH].append(extra)

TOOLS = {
    NUM: ["tables docs/step-functions/latest/dg/service-quotas",
          "show docs/step-functions/latest/dg/service-quotas --around \"Quotas related to accounts\" --chars 4000",
          "tables docs/step-functions/latest/dg/choosing-workflow-type",
          "tables docs/amazon-mq/latest/developer-guide/amazon-mq-limits",
          "show docs/appflow/latest/userguide/service-quotas --chars 5000",
          "show www/step-functions/pricing --around \"state transitions\" --chars 3000",
          "show www/amazon-mq/pricing --around \"broker instance\"",
          "show www/appflow/pricing --around \"flow run\"",
          "tables docs/step-functions/latest/dg/document-history",
          "tables docs/amazon-mq/latest/developer-guide/amazon-mq-release-notes",
          "changes for step-functions --since 2022-07-01 --verbose --find TEXT",
          "changes for mq --since 2022-07-01 --verbose --find TEXT"],
    BEH: ["tables docs/step-functions/latest/dg/choosing-workflow-type",
          "show docs/step-functions/latest/dg/concepts-error-handling --around \"MaxAttempts\"",
          "show docs/step-functions/latest/dg/connect-to-resource --around \"waitForTaskToken\"",
          "show docs/step-functions/latest/dg/state-task --around \"TimeoutSeconds\"",
          "show docs/lambda/latest/dg/concepts-event-driven-architectures --around \"Lambda functions calling Lambda functions\" --chars 3000",
          "show docs/amazon-mq/latest/developer-guide/amazon-mq-broker-architecture --chars 4000",
          "show docs/decision-guides/latest/decision-guides/application-integration-on-aws-how-to-choose --around \"Amazon MQ offer\"",
          "facts list --service lambda", "facts list --service sqs"],
    FAQ: ["faq https://aws.amazon.com/step-functions/faqs/ --find TEXT",
          "faq https://aws.amazon.com/amazon-mq/faqs/ --find TEXT",
          "faq https://aws.amazon.com/appflow/faqs/ --find TEXT",
          "show www/step-functions/faqs --around TEXT"],
}

WATCH = {
    NUM: ["Step Functions quota tables have two header lines (Standard/Express, then Bucket size/Refill rate). Quote the row plus the header text and name the Region scope (US East (N. Virginia), US West (Oregon), Europe (Ireland) versus all other Regions).",
          "The account quota table on service-quotas is raw HTML; `tables` does not list it. Quote one <tr> line only if M4 accepts it; otherwise use `facts adopt --sentence` on a cell sentence. Test with one fact before writing many.",
          "'Hard quota' versus soft: the quota pages say which; put adjustable true or false in the fact.",
          "Pricing pages vary by Region: prefer dimensions, the free tier (4,000 state transitions) and rounding rules (100 ms, 64-MB chunks) over unit prices.",
          "Change items: current truth comes from the guide, quota and pricing pages; history rows and What's New pages give dates and deltas only. A What's New page after 2026-07-15 gets the note 'not examinable yet'. Configurable storage for RabbitMQ is dated 2026-07-15 (What's New) and 2026-07-14 (history): record both and flag it for the adjudicator.",
          "Old values (for example the state machine quota before 2025-02-05) only when a saved page states them verbatim; else mark the old value not-found."],
    BEH: ["Scope matters: many statements hold only for Standard or only for Express workflows, only for ActiveMQ or only for RabbitMQ, or only for engine version 4.2 and later. Put that scope in the claim and make sure the quote states it (a table row plus its header, or the heading).",
          "Express restrictions sit in one comparison table row ('Express Workflows do not support Job-run (.sync) or Callback (.waitForTaskToken) service integration patterns'); quote the row with its header.",
          "Amazon MQ deployment pages repeat the active/standby sentence on several pages; quote from amazon-mq-broker-architecture and do not add duplicates.",
          "The decision guide says Amazon MQ offers 'unlimited retention' and bigger payloads: quote the whole sentence with its 'However' clause if the claim uses it; keep the hedge.",
          "Neighbour facts: reuse lambda, sqs and well-architected facts named in reuse_candidates after `facts list --service <key>`; add a neighbour fact only when none answers the question, under its own service key (lambda, sqs, eventbridge, well-architected).",
          "Callvale story values (six steps, month 13, one ActiveMQ broker, 300 customers) are story data, never facts.",
          "Case studies: kind case-study, quote at most 25 words; Armut and Qivos redirect to the listing page (fetch_failures)."],
    FAQ: ["FAQ lists: work files faq-step-functions.txt (31 questions, item 31 'NA' is empty), faq-mq.txt (36, item 36 empty), faq-appflow.txt (19, item 19 empty).",
          "FAQ facts use ids <service>-faq-<slug> under service keys step-functions, mq, appflow.",
          "Express duration or history numbers in an FAQ answer must agree with service-quotas; if not, note the FAQ wording in the demand record and do not add the FAQ number as a fact."],
}

INDEX = {FAQ: ["_build/corpus/faq/step-functions.jsonl", "_build/corpus/faq/amazon-mq.jsonl", "_build/corpus/faq/appflow.jsonl"]}

all_pages = set()
for v in lens_pages.values():
    all_pages.update(v)

plan = {
    "chapter": "32",
    "made_by": "plan-32",
    "made": TODAY,
    "brief": "_build/work/32-step-functions/brief.v0.json",
    "how_to_mine": [
        "Follow this plan exactly. Each lens agent reads only its pages (all are in the corpus unless the note says 'fetch on demand'; read them with `show <source_id> --around TEXT` or `--lines A:B`, tables with `tables <source_id>`), answers its demand items, and records each item as filled (fact ids), contradicted (what the page says instead) or not-found (where you looked).",
        "Write facts in files of 10 to 25 facts: _build/work/32-step-functions/facts-<lens>-NN.json (lens file names: numbers, behavior, faq), then `facts add --file <that file> --by mine-32-<lens>`. Table rows and value lines: prefer `facts adopt` (--table/--row, --sentence, --heading). Every quote is copied verbatim from the page snapshot (.txt), never from full.md (full.md hits are pointers) and never from memory.",
        "Each quote must carry every clause, scope, condition and exception of the claim on its own. When the condition stands in the next sentence (for example 'This doesn't apply to Express Workflows.' or 'Redrive is not supported for Express workflows.'), include that sentence in the quote; otherwise narrow the claim. Entail votes run on Opus and mark a clause found only in the surrounding text as partial.",
        "Fact service keys: `step-functions`, `mq`, `appflow`; ids start with the key, for example `step-functions-express-max-duration`, `mq-activemq-active-standby-two-azs`, `appflow-quota-flows-per-account`. Two facts already exist (mech-pass): step-functions-decision-workflows-category and mq-welcome-migrate-without-rewriting-messaging-code; reuse them, do not duplicate. Neighbour facts: lambda (chapter 18), sqs, sns, eventbridge (chapter 31), well-architected; add one only after `facts list --service <key>` shows no fact that already answers it, and reuse the existing id in the demand record when one exists.",
        "Every hard fact (number, limit, default, price, date, can/cannot, only/always/never) carries `question` (the demand question it answers) and at least two displays for kinds behavior, capability, restriction and default (brief gate B12). A display of a number-free fact is a verbatim phrase of at most 8 words from its quote (RULINGS 2026-10-11).",
        "Changes: a fact touched by a change item sets `changed` (date, old value only if a saved page states it verbatim) and `change_items`. A feature GA after 2026-07-15 gets the note `not examinable yet`. Current truth comes from the guide, quotas and pricing pages; history rows and What's New pages give dates and deltas only.",
        "Case-study facts have kind `case-study` and a quote of at most 25 words.",
    ],
    "lenses": {},
    "all_pages_count": len(all_pages),
    "not_in_corpus": [],
    "rules": [
        "Quote from page snapshots only; full.md hits are pointers.",
        "A demand item becomes filled, contradicted (with what the page says) or not-found.",
        "Current truth comes from the guide, quotas and pricing pages; What's New pages and history rows give dates and deltas only.",
        "Files of 10 to 25 facts; every quote verbatim and complete for its claim; `--by mine-32-<lens>`.",
    ],
}
for lens in (NUM, BEH, FAQ):
    entry = dict(LENSES[lens])
    entry["pages"] = lens_pages[lens]
    entry["demand"] = lens_demand[lens]
    entry["tools"] = TOOLS[lens]
    entry["watch"] = WATCH[lens]
    if lens in INDEX:
        entry["index"] = INDEX[lens]
    plan["lenses"][lens] = entry

json.dump(brief, open(os.path.join(HERE, "brief.v0.json"), "w"), indent=1, ensure_ascii=False)
json.dump(plan, open(os.path.join(HERE, "mine-plan.json"), "w"), indent=1, ensure_ascii=False)
print("demand", len(demand), {k: len(v) for k, v in lens_demand.items()}, "sources_fetched", len(sources_ok), "pages", len(all_pages))
