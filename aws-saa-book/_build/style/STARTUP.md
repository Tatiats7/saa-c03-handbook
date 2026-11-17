# STARTUP: the story bible (version 1.0)

One fictional startup runs through the book. Its AWS architecture grows chapter by chapter. Every writer follows this file, so that names, numbers and the timeline never contradict each other.

- **Part A** (about 4,000 words): read all of it. **Part B** is the timeline: read its first section, the entry of your chapter and the entries of the other chapters in your wave.
- The full record is `aws-saa-book/data/startup.json`. It holds everything in this file, plus the full sentences for each Decision record, the `later` and `note` lines of each chapter, and the numbers that each chapter uses. If the two files differ, the JSON wins: report the difference.
- Precedence: `RULINGS.md`, then `CONVENTIONS.md`, `SPEC.json` and `STYLE.md`, then this file for everything about the startup.
- The working name in the planning reports was Harken. The name is now **Callvale** (A2). The data file is `data/startup.json`.

## Part A: the bible

### A1. The company in five lines

1. **Callvale** (say CALL-vale) sells a call-intelligence service. Customers send recorded or live support calls and get transcripts, sentiment, topics, summaries, search and dashboards.
2. The customers are customer-support teams: first of small software companies, later of a bank and a hospital group.
3. The customers care about **compliance** because recordings contain personal data, card numbers and health information, and regulators ask the customers for proof.
4. The customers care about **private connectivity** because a bank does not send customer calls through the public internet.
5. The customers care about **recovery** because support teams work from the recordings every day, and the bank's contract sets an RPO of 15 minutes and an RTO of 1 hour.

Ana and Ben founded Callvale in San Francisco. Callvale builds in US East (N. Virginia), because its first customers are on the US East Coast.

### A2. Name check

Checked with WebSearch on 2026-10-04.

- **Harken: collision.** HarkenAI (harkenai.com) sells conversation capture with summaries and action items. Harken AI (harken.ai) and Harken Data (harkendata.com) also exist.
- **Rejected after a search** (a real company in voice, calls or AI has the name): Zari, Tellaro, Listra, Vokari, Calvora, Telvia, Notiva, Hovor, Sonvia.
- **Callvale: no collision** in three searches (the plain name; with "AI", "software", "call analytics", "conversation intelligence"; with "company"). The only match is @CallVale, the social-media handle of a building-maintenance firm in England.
- **Customer names.** Rejected: Tavrin (family name of a sanctioned Russian businessman), Halden Health and Morlen Health (real health companies). Kept: Ostell Bank, Dorrin Health, Peldon Systems.

**Decision.** Callvale in every reader-facing text. "Vale" is an old word for valley: the place where the calls collect. Never write "Harken".

### A3. Cast

| Name | Role | How the person talks | Always asks |
|---|---|---|---|
| **Ana** (she) | CEO, co-founder. Cares about cost and customers. | In customers, money and dates. She uses no AWS terms and asks you to explain each term that you use. | "What does it cost each month, and what do I tell the customer?" |
| **Ben** (he) | CTO, co-founder. Cares about speed and simplicity. | In short technical sentences. He prefers the option with the fewest parts and distrusts everything that he must operate at night. | "What is the simplest thing that works, and what do we have to run ourselves?" |
| **Chen** (she) | Security lead, from month 18. Cares about controls and evidence. | In controls and evidence. She quotes the bank's questionnaire by question number. | "Who can access it, and how do we prove it?" |
| **you** | Their AWS Solutions Architect. | In four moves: the short answer, how it works, the thing to watch, and "in your case" with a question back. | "What is the requirement, in one sentence?" |

Chen appears only in chapters of stage 3 and stage 4. "You" never has a name. No other person has a name.

### A4. Fact sheet

These are Callvale's own numbers, invented and fixed. An AWS limit, price or behaviour never appears here: AWS facts come only from the fact canon. Months count from the founding. Clock times are US Eastern time. Units are decimal (1 TB is 1,000 GB).

**Growth by stage**

| Number | Stage 0 | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
|---|---|---|---|---|---|
| Starts at month | 3 | 6 | 11 | 18 | 24 |
| People (engineers) | 2 (1) | 4 (3) | 8 (6) | 20 (14) | 45 (30) |
| Paying customers | 0 | 10 | 120 | 260 | 700 |
| Call minutes a month | 1,200 | 60,000 | 1.5 million | 4.2 million | 9 million |
| Calls a month | 200 | 10,000 | 250,000 | 700,000 | 1.5 million |
| Calls a weekday | | | 11,400 | 31,800 | 68,200 |
| Peak uploads a minute | | | 40 | 105 | 225 |
| New audio a month | 2.4 GB | 120 GB | 3 TB | 8.4 TB | 18 TB |
| Database size | on the instance | 20 GB | 400 GB | 1.2 TB | 3 TB |
| Conversion workers, maximum | | | 40 | 40 | 60 |
| Services on AWS Fargate | | | | 6 | 7 |
| AWS accounts | 1 | 1 | 1 | 7 | 9 |
| Availability Zones in use | 1 | 2 | 3 | 3 | 3 |

Launch: month 12. End of the story: month 31. Stage 0 has 3 pilot teams that do not pay. Stage 4 includes Peldon's 300 customers and 4 engineers, and 3 machine learning (ML) engineers.

**Workload**

- Call: 6 minutes and 12 MB on average (2 MB a minute). Longest recording: 4 hours, 480 MB. Average transcript: 30 KB.
- Peak window: 09:00 to 11:00, Monday to Friday, with 40% of a weekday's uploads. Night rate at stage 2: 2 uploads a minute.
- Pipeline: 6 steps (convert, transcribe, analyze, summarize, save, notify) and about 12 updates of the job record for each call. Conversion: 90 seconds on average, up to 25 minutes.
- Users: 40 for each customer; 4,800 at stage 2, with 600 signed in at the peak. Outside the United States: 20% at stage 2, 30% at stage 4 (Dublin and Manila).
- Web requests per second: 50 at a normal peak; 150 broke the single instance in the load test (month 11); 400 for 3 hours on launch day, 8 times the normal peak. Static files: 70% of requests.
- Web Auto Scaling group: minimum 3, maximum 12, scheduled capacity 6 at 08:45 from Monday to Friday. A new instance serves traffic after 4 minutes. Conversion workers: minimum 0.
- Demo-day instance: 9% CPU use on average, 85% on weekday mornings.
- API (month 14): 30 customers asked; one test program sent 200 requests per second; the limit is 20 requests per second for each customer.
- Fargate: minimum 3 tasks for each service, 1 task for each service in the standby Region.
- One release took 40 minutes (month 20). Templates took 3 weeks, and 40 workers need a patch each month (month 24).
- Callvale Live (month 26): 3,000 live calls at the peak; 1 event for each call every 2 seconds; 1,500 events per second, 1 KB each; replay of the last 6 hours.

**Promises, retention and settings**

- Promises: a transcript within 10 minutes for 95% of calls; a dashboard page in under 2 seconds; search in under 1 second (up to 9 seconds in PostgreSQL at month 26); a live insight within 3 seconds; 99.9% availability a month.
- Recordings and transcripts are kept 7 years. 2% of recordings are opened after 90 days.
- Lifecycle rule: S3 Standard-IA after 90 days (stage 1); S3 Glacier Deep Archive after 1 year (stage 4); delete after 7 years. Customers request 200 archived recordings a month and accept a wait of 48 hours.
- Links: 15 minutes for an upload; 5 minutes for playback (an S3 presigned URL at stage 1, a CloudFront signed URL from stage 2).
- A job record is deleted after 90 days. A cached result lives 60 seconds. The 20 most common dashboard queries cause 80% of database reads. A message moves to the dead-letter queue after 3 failed receives.
- Application logs: 90 days. Record of API calls: 7 years. Backups: daily kept 30 days, monthly kept 7 years. Stage 1 snapshots: daily, kept 30 days. Database credentials rotate every 30 days.
- Database: 90% of queries are reads. The read replica was 40 seconds behind at the stage 3 peak. Aurora: 1 writer, 2 Aurora Replicas. Dev and staging are used 50 hours a week.

**Recovery**

- Stage 1 targets: RPO 24 hours, RTO 8 hours.
- Bank contract: RPO 15 minutes, RTO 1 hour for the loss of a Region. First test due 9 months after signing (month 27), then every 6 months.
- Test 1, month 26, pilot light: 2 hours 40 minutes, failed. Test 2, month 27, warm standby: 42 minutes, passed. Data loss under 1 minute in both.

**Incidents**

- Month 3: the first Well-Architected review lists 12 high-risk findings (A9).
- Month 6: the root user's access key is in the code and on 3 laptops. A pilot customer finds the public bucket.
- Month 6, Tuesday, 09:40: the only volume fills up. The database stops for 3 hours. The newest backup is 9 days old.
- Month 12, launch day, 10:20: the pipeline fails for 47 minutes. 1,900 uploads fail. The database reaches 900 connections. The one worker is 6 hours behind.
- Month 19: 60,000 automated sign-in attempts in 1 hour from 1,400 IP addresses.
- Month 19: transcripts are 6 hours late one night; a customer notices first.
- Month 19: the first Amazon Macie job finds card numbers in 1,300 transcripts.

**Customers and Peldon**

- **Ostell Bank** ("the bank"; New York, data center in New Jersey). Signs at month 18 for 3 years. 30% of revenue at signing; 25% of call minutes at stage 3. 400 supervisors use the dashboard. Questionnaire: 180 questions, 43 "no" answers at first. Starts 3 weeks after signing; requires a private connection within 6 months. Auditors visit at month 24, with 4 weeks of notice. From stage 4: 4,000 scanned pages a month.
- Bank connectivity: VPN ready in 5 days; Direct Connect ready 10 weeks after the order (month 21).
- Bank archive: 80 TB, 6.7 million recordings, 40 million call minutes, a limit of 30 days. 100 Mbps in a VPN test: 74 days. 500 Mbps allowed on Direct Connect: 15 days.
- **Dorrin Health** ("the hospital group"; 6 hospitals). Signs at month 21. One SFTP batch each night at 01:00: 6,000 recordings, about 70 GB, processed by 06:00. 18% of its calls are in Spanish.
- **Peldon Systems** ("Peldon"), an on-premises call-recording vendor. Acquired at month 25. 300 customers, 4 engineers. 40 servers on VMware (28 Windows, 12 Linux), Oracle 600 GB, MongoDB 200 GB, Windows file shares 12 TB, 1 ActiveMQ broker. The lease ends after 6 months (month 31). Cutover at month 30: Sunday, 02:00 to 06:00 (4 hours).
- Bulk job (month 27): the 6.7 million archive recordings in 30 days.

**Accounts and network**

- Regions: US East (N. Virginia), `us-east-1`, primary. US West (Oregon), `us-west-2`, standby from stage 4. These are the 2 approved Regions.
- Accounts (7 at stage 3, in 3 organizational units): `management`; `log-archive`, `security` (Security); `network` (Infrastructure); `dev`, `staging`, `prod` (Workloads). Stage 4 adds `analytics` and `peldon` (Workloads).
- CIDR blocks: prod `10.20.0.0/16`; standby `10.30.0.0/16`; dev `10.40.0.0/16`; staging `10.50.0.0/16`; network `10.60.0.0/16`; peldon `10.70.0.0/16`. The bank's VPC: `10.20.0.0/16`, the same as prod. The bank's data center: `172.16.0.0/16`. Peldon's data center: `192.168.0.0/16`.
- Prod subnets for AZ 1, AZ 2, AZ 3. Public: `10.20.0.0/24`, `10.20.1.0/24`, `10.20.2.0/24`. Private application: `10.20.16.0/20`, `10.20.32.0/20`, `10.20.48.0/20`. Private data: `10.20.100.0/24`, `10.20.101.0/24`, `10.20.102.0/24`. Stage 1 uses AZ 1 and AZ 2.

**Cost**

- The AWS credits end at month 17. No credit amount and no dollar amount is ever stated.
- Month 29: the bill has doubled in 6 months. Shares: compute 38%, storage 21%, AI services 18%, databases 12%, data transfer 8%, other 3%. Target: 20% lower in 2 quarters.
- The Savings Plan covers 70% of the steady compute. 5% of the Spot workers were interrupted in one week (Callvale's measurement). The review finds 14 unattached volumes.
- Recordings at month 29: 190 TB; 140 TB uploaded more than 90 days ago; 87 TB moves to the archive storage class (the 80 TB bank archive and 7 TB older than 1 year).

**Fixed names.** Use these names and no others. Hands-on tasks use the reader's own names with the prefix `saa-`.

| Thing | Names |
|---|---|
| Hosts | `callvale.example` and `app.callvale.example` (dashboard), `api.callvale.example`, `sftp.callvale.example`, `live.callvale.example` |
| Buckets | `callvale-audio` (key `<customer-id>/<yyyy>/<mm>/<dd>/<call-id>.wav`), `callvale-transcripts`, `callvale-web`, `callvale-logs`, `callvale-lake`, `callvale-audio-dr` |
| Bank prefixes | `ostell/` (own KMS key, S3 Object Lock); `ostell/archive/` (the archive, in S3 Standard-IA) |
| Queues and topics | `uploads`, `convert`, `webhooks`, `indexing`, each with `<queue>-dlq`; `transcript-ready`, `ops-alerts` |
| Functions | `start-job`, `save-results`, `notify`, `live-insights` |
| State machine, table, stream | `call-pipeline`; `jobs` (partition key `call_id`; index `by-customer` on `customer_id`, `created_at`); `live-events` |
| Fargate services | `dashboard`, `upload`, `search`, `accounts`, `billing`, `admin`; stage 4 adds `live-ingest` |
| KMS key aliases | `alias/callvale-audio`, `alias/callvale-db`, `alias/ostell-audio` |
| Products | Callvale (dashboard and search), Callvale API, Callvale Live |
| Third-party names allowed | PostgreSQL, Oracle, MongoDB, ActiveMQ, VMware, Windows, Linux, Kubernetes, Salesforce, SAML, SFTP, JSON, Parquet |

**AI services and their roles**

| Service | Role in Callvale | From stage |
|---|---|---|
| Amazon Transcribe | Speech to text for every call; on live audio at stage 4. | 0 |
| Amazon Comprehend | Sentiment and topics; from stage 3 it finds card numbers, so that the pipeline can remove them. | 2 |
| Amazon Translate | Spanish transcripts into English for the dashboards. | 4 |
| Amazon Textract | Text from the bank's scanned complaint letters, so that search covers them. | 4 |
| Amazon Polly | A spoken daily summary for team leads. | 4 |
| Amazon Lex | A chat window in the dashboard that answers questions about calls. | 4 |
| Amazon Rekognition | Flags screenshots, attached to a call record, that show identity documents. | 4 |
| Amazon SageMaker AI | The one custom model: the churn-risk score. | 4 |
| Amazon Bedrock | The summarize step uses a foundation model. Always label it "outside the exam". | 2 |

### A5. Growth stages

| Stage | Months | Trigger | Architecture at the end of the stage |
|---|---|---|---|
| **0 Demo day** | 3 to 5 | A demo for investors works. Three pilot teams start to upload real calls. | One hand-built instance in the default VPC runs everything. Root access key in the code. Public audio bucket. This is the "before" picture. |
| **1 First ten customers** | 6 to 10 | Ten paying customers arrive with purchase forms about security. In the same month, the only volume fills up. | IAM roles; a private bucket with presigned URLs; a custom VPC in two Availability Zones with one NAT gateway and an S3 gateway endpoint; web and worker instances from an AMI; Amazon RDS for PostgreSQL with Multi-AZ. |
| **2 Launch week** | 11 to 17 | A load test at month 11 fails. The launch at month 12 brings 8 times the normal traffic: the web tier holds, but the pipeline fails. The AWS credits end at month 17. | CloudFront, Route 53, an Application Load Balancer and a web Auto Scaling group in three Availability Zones; queues, functions and a state machine; DynamoDB; Amazon EFS; ElastiCache; a public API with Cognito. |
| **3 First bank customer** | 18 to 23 | Ostell Bank signs for 3 years and sends a questionnaire of 180 questions. Chen joins. Dorrin Health signs at month 21. | Seven accounts; IAM Identity Center; customer managed keys; rotated secrets; AWS WAF; detection services; monitoring and an audit trail; PrivateLink, VPN and Direct Connect; Fargate; Aurora; AWS Backup; three bulk intake paths. |
| **4 Global and efficient** | 24 to 31 | The bank contract needs a second Region by month 27. Callvale Live starts. Callvale acquires Peldon. Ana orders a cost review. | Templates; warm standby in US West (Oregon); a live stream and a data lake; Peldon's systems in AWS; AWS Batch; five new AI features; a Savings Plan and Spot Instances. |

### A6. Final architecture (month 31)

- **Edge.** Amazon Route 53 (alias records, failover routing, health checks). Amazon CloudFront with origin access control and signed URLs. AWS WAF through AWS Firewall Manager. AWS Global Accelerator for live audio. ACM certificates.
- **Network.** One VPC in each Region, with public, private application and private data subnets in three Availability Zones. A NAT gateway in each Availability Zone. Gateway endpoints for Amazon S3 and Amazon DynamoDB; interface endpoints for other AWS services. A transit gateway. AWS Network Firewall for outbound traffic. An AWS PrivateLink endpoint service with a Network Load Balancer for the bank. AWS Direct Connect with a backup Site-to-Site VPN to the bank; a VPN to Peldon until month 31. AWS Client VPN.
- **Compute.** Amazon ECS on AWS Fargate: seven services behind an Application Load Balancer. An EC2 Auto Scaling group of Spot conversion workers (0 to 60) that scales on the `convert` backlog. AWS Lambda functions. AWS Batch on Spot Instances. Peldon's 40 rehosted EC2 instances.
- **Data.** Amazon S3 (versioning, SSE-KMS, lifecycle rules, S3 Object Lock on the bank's prefix). Amazon Aurora PostgreSQL; Aurora Serverless v2 for dev and staging. Amazon DynamoDB. Amazon ElastiCache. Amazon EFS. Amazon OpenSearch Service. For Peldon: Amazon FSx for Windows File Server and Amazon DocumentDB.
- **Integration.** S3 Event Notifications, Amazon SQS, Amazon SNS, Amazon EventBridge, AWS Step Functions. Amazon API Gateway (REST API; WebSocket API). Amazon Kinesis Data Streams and Amazon Data Firehose. Amazon MQ (Peldon). Amazon AppFlow (Salesforce). The AI services of A4.
- **Security.** AWS Organizations (nine accounts, service control policies), AWS Control Tower, AWS RAM. IAM Identity Center for people, IAM roles for workloads, no IAM users. Amazon Cognito with SAML federation. AWS KMS customer managed keys (multi-Region). AWS Secrets Manager; Parameter Store. AWS WAF, AWS Firewall Manager, AWS Network Firewall. Amazon GuardDuty, Amazon Inspector, Amazon Macie, AWS Security Hub, Amazon Detective, AWS Config, AWS Artifact. AWS Directory Service for Peldon.
- **Operations.** Amazon CloudWatch and AWS X-Ray. An AWS CloudTrail organization trail. AWS CloudFormation with StackSets. AWS Systems Manager (Session Manager, Patch Manager). AWS Trusted Advisor, AWS Compute Optimizer, AWS Well-Architected Tool. AWS Budgets, AWS Cost Explorer, AWS Cost and Usage Report, cost allocation tags, a Compute Savings Plan.
- **Analytics.** S3 data lake in Parquet format, AWS Glue, Amazon Athena, AWS Lake Formation, Amazon Quick. Amazon Redshift for finance reporting.
- **Recovery.** Three Availability Zones for every layer. Warm standby in US West (Oregon): Aurora Global Database, a DynamoDB global table, S3 Cross-Region Replication, one task of each service. Route 53 failover records and AWS Global Accelerator move traffic. AWS Backup with a locked vault and cross-account and cross-Region copies. A recovery test every 6 months. The cache and the search index are not replicated.

### A7. Continuity rules for writers

1. **Fixed names.** Callvale; Ana (she), Ben (he), Chen (she); you, their AWS Solutions Architect; Ostell Bank (the bank); Dorrin Health (the hospital group); Peldon Systems (Peldon). No other named person or company. Never write Harken. Resource names come from A4.
2. **Chen** appears only in chapters of stage 3 and stage 4.
3. **Fixed numbers.** Use only numbers from the fact sheet, with the same value and unit. If a scene needs a number that does not exist, write the scene without it and report a story request.
4. **Size.** At most 80 words of story in one section. The `Startup example` callout has at most 60 words with its label and at most 4 sentences. In a Decision record, the Context field has at most 80 words.
5. **The story never teaches a fact.** A story sentence states no AWS limit, price, default, or "can" and "cannot" rule. The fact stands in the explanatory text next to the story, with a fact link.
6. **Decisions.** Keep the options, the choice and the trade-off of the entry. A reason that is an AWS behaviour needs a fact link. If the canon does not support a reason, keep the decision, change the reason and report it.
7. **Order.** Each chapter states its stage and its trigger in one clause and stands alone. A component exists only from the chapter that adds it, in story order (B1).
8. **"Must".** In story text, "must" states a requirement of Callvale or of a customer, in exam English. It never states an AWS rule there.
9. **Question stems** and mock exams say "A company". They never name Callvale or the cast. A stem can reuse Callvale's situation and numbers.
10. **Money and time.** No dollar amount in story text: shares, targets and quantities only. Months count from the founding; no calendar dates.
11. **Regions.** Two Regions only: US East (N. Virginia) and US West (Oregon). Label Availability Zones AZ 1, AZ 2, AZ 3. The story names instance families by purpose only; an exact instance type needs a fact link.
12. **Real companies** appear only in the box "In the real world", from an AWS-published page. They never enter Callvale's story. Third-party product names are limited to the list in A4.
13. **Diagrams.** Name the story pair `<slug>-before` and `<slug>-after`. Flow runs from left to right: users and customer sites, edge, compute, data. Integration sits under compute. The second Region sits on the right. A component keeps its place in every diagram.
14. **Not used.** A service that is not in the timeline or in the final architecture is not used. Do not add one (A8).
15. **Synthesis chapters** (44 to 49, 52) can point to the final architecture. They add no story event.

### A8. What Callvale does not use

A service that was "weighed" can appear as an option in a Decision record. Every other service in this list appears only in its own card or comparison table, without Callvale.

- **Weighed, not chosen:** AWS CloudHSM (the bank accepts customer managed keys in AWS KMS); AWS Shield Advanced (stage 3, not bought); AWS Snow Family (the 80 TB archive goes through Direct Connect); Amazon MSK (the team has no Kafka skills); Amazon EKS (one engineer knows Kubernetes); VMware Cloud on AWS (Peldon is rehosted to Amazon EC2); Amazon DynamoDB Accelerator, DAX (the live screen does not need it); VPC peering connection (PrivateLink and a transit gateway are chosen); Reserved Instances (a Compute Savings Plan is chosen); AWS Outposts (the bank asked for processing inside its data center, and Callvale declined).
- **No workload:** Amazon ECS Anywhere, Amazon EKS Anywhere, Amazon EKS Distro; Amazon EMR; AWS Data Exchange; Amazon Neptune; Amazon Keyspaces; AWS Local Zones; AWS Wavelength; AWS Elastic Beanstalk; AWS Serverless Application Repository; Amazon Elastic Transcoder; Amazon Kinesis Video Streams; AWS Amplify; AWS Device Farm; Amazon FSx for Lustre, FSx for NetApp ONTAP, FSx for OpenZFS; Amazon Managed Grafana; Amazon Managed Service for Prometheus; AWS Service Catalog; AWS License Manager.
- **No vendor names:** the story names no third-party monitoring, firewall or identity product.

### A9. The flawed start

The first Well-Architected review (chapter 02) lists these 12 high-risk findings. Each one is repaired in a later chapter.

| # | The mistake at stage 0 | Fixed in |
|---|---|---|
| 1 | The root user's access key is in the application code and on three laptops. | 03 |
| 2 | Ana and Ben share the root user's password. MFA is not turned on. | 03 |
| 3 | The audio bucket is public, so that the browser can play recordings. | 21 |
| 4 | Everything runs in the default VPC with public IP addresses. The database port is open to the internet. | 10 |
| 5 | One hand-built instance that nobody can rebuild, with SSH open to the world. | 16 |
| 6 | One volume holds the operating system, the database and temporary files. No snapshots exist. | 22 |
| 7 | The database runs on the application instance. Nobody has tested a restore. | 26 |
| 8 | One instance in one Availability Zone serves all traffic. | 14, 17 |
| 9 | The upload request waits for the processing. A restart loses the work. | 31 |
| 10 | The database password is in a configuration file. Ben installed the TLS certificate by hand, and it expired one time. | 07 |
| 11 | No alarms, no log review, no record of who changed what. | 37 |
| 12 | Everything was created by hand in one account. No templates and no budget alert exist. | 38, 04, 41 |

## Part B: the timeline

### B1. Story order, pipeline states and waves

**Story order.** The reader meets the chapters in another order, so each chapter stands alone. For the writer, a component exists only from the chapter that adds it, in this order. The "before" picture of a chapter is the state after all earlier chapters.

- Stage 0: 02.
- Stage 1: 03, 21, 22 (month 6); 16, 10 (month 7); 26 (month 8).
- Stage 2: 14, 17, 15, 13 (month 11); 31, 18 (month 12); 32, 28, 23, 29 (month 13); 33 (month 14); 43 (month 15).
- Stage 3: 04, 05, 06, 07, 11, 12 (month 18); 08, 09, 37 (month 19); 19, 27 (month 20); 25 (month 21); 24 (month 22); 42 (month 23).
- Stage 4: 38, 40 (month 24); 39 (month 25); 34, 35 (month 26); 20 (month 27); 30, 36 (month 28); 41 (month 29).

**Pipeline states.** Chapters 31 and 18 share one "before" picture (P1) and one "after" picture (P2). Chapters 32 and 28 share P2 and P3. Each chapter highlights its own part.

- **P1, launch day.** The web application calls the one worker directly and waits. Scheduled jobs on the worker register uploads, save results and send notifications. Job status is in PostgreSQL.
- **P2, end of month 12.** S3 event, `uploads` queue, `start-job` function, `convert` queue, conversion workers in an Auto Scaling group (0 to 40, scales on the backlog). A chain of functions calls Amazon Transcribe and Amazon Comprehend and waits in loops. `save-results` stores the results. The topic `transcript-ready` fans out to the queues `webhooks` and `indexing`. Job status is still in PostgreSQL, through Amazon RDS Proxy.
- **P3, end of month 13.** `start-job` starts the state machine `call-pipeline`, which has six states: convert (through the `convert` queue), transcribe, analyze, summarize, save, notify. Job state is in the DynamoDB table `jobs`.

**Waves.** Chapters that are built together tell one piece of the story.

| Wave | Chapters | The piece of the story |
|---|---|---|
| W1 | 02, 03 | The flawed start and the first repair: identity. |
| W2 | 10, 21 | First paying customers: a private network and a private bucket. |
| W3 | 04 to 09 | The bank's questionnaire and Chen's first two months. |
| W4 | 16, 22, 14, 17 | From one hand-built instance to a web tier that passes the load test. |
| W5 | 26, 27, 28, 13 | Where the data lives at stages 1, 2 and 3, and the DNS move before launch. |
| W6 | 15, 18, 31, 23 | Launch week: the edge cache before it; queues, functions and shared files after it. |
| W7 | 40, 41 | The bank's recovery numbers and Ana's cost review. |
| W8 | 33, 29, 11, 12, 19 | The public API and the cache at stage 2, then private paths and container services at stage 3. |
| W9 | 32, 25, 24, 34, 35 | Moving data: the workflow (stage 2), bulk intake and backup (stage 3), the live stream and the data lake (stage 4). |
| W10 | 43, 37, 42, 38, 39 | Running the grown system: the launch-day review, monitoring, the audit walk-through, templates, the Peldon migration. |
| W11 | 20, 30, 36 | Smaller topics of stage 4: the bulk job, two special databases, the AI features. |

### B2. One entry for each chapter

Each entry is a headline. **Problem** and the **question** are word for word the same as in the JSON: use them as they are. Trigger, Adds, Decision and Diagram are short here; the JSON entry `chapters.<id>` has the full sentences, the `later` and `note` lines and `uses_numbers`. Read the JSON entry of your own chapter before you write.

| Field | Where it goes in the chapter |
|---|---|
| Trigger | `**Context.**` of the Decision record. |
| Problem | The `Startup example` callout in "In one breath" (pattern chapters: "The question behind it"; light family chapters: "The family in one picture"). |
| Adds | The "after" diagram. Service names only. |
| Decision | Options, with the choice in bold, then the accepted trade-off. `**Requirement.**` is the last requirement of the Problem, with the qualifier of the JSON in capitals. Light family chapters have no Decision record: use the decision in questions and in the spoken prompt. |
| Question | One speak item: `persona` is the name, `prompt` is the text. |
| Diagram | The story pair `<slug>-before` and `<slug>-after`. |

**02 AWS map** (stage 0, month 3, order 1, W1)
- Trigger: after demo day, an investor asks for a technical review.
- Problem: Callvale runs its whole product on one instance in one Availability Zone. Ben created everything by hand with the root user. Three pilot teams upload real customer calls. The founders must choose a Region and must learn which protections are their own responsibility.
- Adds: nothing. A Well-Architected review with 12 findings.
- Decision: US West (Oregon), near the founders / **US East (N. Virginia), near the first customers** / two Regions. Accepts: a Region failure stops the service until stage 4.
- Ana asks: "AWS says that it is secure. So why is the public bucket our problem and not theirs?"
- Diagram: the demo-day system with 12 marked findings; then the same Region with three planned Availability Zones.

**03 IAM** (stage 1, month 6, order 2, W1)
- Trigger: a purchase form asks who can access the recordings; Ben finds the root access key in the code and on 3 laptops.
- Problem: Callvale's application calls Amazon S3 and Amazon Transcribe with the root user's access key. The key is stored in the code. Ana and Ben share the root user's password. Callvale must remove long-term keys and must give each person and each workload least privilege.
- Adds: IAM role with an instance profile; IAM users with MFA in two groups; least-privilege policies; MFA on the root user.
- Decision: move the key out of the code / an IAM user with a key for each workload / **an IAM role on the instance**. Accepts: one tested policy for each workload; IAM users for people until stage 3.
- Ben asks: "If I delete the access key, how does the code on the instance get permission to read the bucket?"
- Diagram: one root key in the code and on laptops; then a role for the application, IAM users with MFA, a locked root user.

**04 Organizations** (stage 3, month 18, order 20, W3)
- Trigger: the bank's questionnaire asks how production is separated from testing; Chen joins.
- Problem: Callvale runs development, testing and production in one AWS account. The bank requires an isolated production environment and audit logs that operators cannot change. No workload can run outside two approved Regions. The rules must apply to every account, including future accounts.
- Adds: AWS Organizations; service control policies; AWS Control Tower; AWS RAM.
- Decision: one account with tags and IAM policies / accounts configured by hand / **AWS Control Tower with service control policies, 7 accounts**. Accepts: more design for access between accounts; rules that block engineers at first.
- Chen asks: "How do I make sure that even a production administrator cannot turn off the audit log?"
- Diagram: one account for everything; then 7 accounts in 3 organizational units.

**05 Identity federation** (stage 3, month 18, order 21, W3)
- Trigger: 7 accounts for each engineer; the bank wants its 400 supervisors to sign in with the bank's identity provider.
- Problem: Callvale's 14 engineers need one sign-in for seven AWS accounts, with no long-term credentials. Separately, 400 bank employees must sign in to the Callvale web application with their corporate identities. Callvale must not store their passwords.
- Adds: IAM Identity Center; Amazon Cognito federation with the bank's SAML identity provider. Stage 4: AWS Directory Service for Peldon.
- Decision: IAM users in every account / IAM users in one account who assume roles / **IAM Identity Center for engineers, Cognito federation for the bank**. Accepts: all access depends on the identity provider; one tested emergency path.
- Ben asks: "What is the difference between IAM Identity Center and Cognito? Both look like sign-in to me."
- Diagram: two sign-in paths: engineers through IAM Identity Center, bank supervisors through a Cognito user pool.

**06 KMS** (stage 3, month 18, order 22, W3)
- Trigger: the questionnaire asks who controls the keys for the bank's recordings.
- Problem: Callvale encrypts its buckets and its database with keys that AWS manages. The bank requires that Callvale controls who can use the key for the bank's recordings. Every use of the key must be logged. Access must end quickly when the contract ends.
- Adds: AWS KMS customer managed keys; key policies; automatic key rotation. Stage 4: multi-Region keys.
- Decision: keys that AWS manages / **customer managed keys in AWS KMS, one for the bank** / AWS CloudHSM. Accepts: a wrong key policy can stop the pipeline.
- Chen asks: "If an engineer has full S3 permissions, can that engineer still read the bank's recordings?"
- Diagram: one default lock on every store; then three keys with key policies.

**07 Secrets and certificates** (stage 3, month 18, order 23, W3)
- Trigger: the questionnaire asks how often database passwords change. The answer is never.
- Problem: Callvale stores the database password in a configuration file on each instance. The password has never changed. The bank requires rotation every 30 days with no downtime and no new deployment. Callvale also wants TLS certificates that renew without manual work.
- Adds: AWS Secrets Manager with rotation; Systems Manager Parameter Store; AWS Certificate Manager (ACM), in use from stage 2.
- Decision: an encrypted file in Amazon S3 / Parameter Store for everything / **Secrets Manager for credentials, Parameter Store for plain configuration**. Accepts: a cost for each secret; the application reconnects after a rotation.
- Ben asks: "Parameter Store or Secrets Manager? I want one place for configuration. Which one, and why?"
- Diagram: one password in a file on every instance; then a rotated secret that the application's role reads.

**08 Edge protection** (stage 3, month 19, order 26, W3)
- Trigger: the sign-in attack of month 19; the questionnaire asks about outbound traffic control.
- Problem: Callvale's sign-in page receives 60,000 automated attempts in one hour from 1,400 IP addresses. The bank also requires that production workloads connect only to approved outside domains. Callvale must block common web attacks and limit request rates in every account.
- Adds: AWS WAF; AWS Firewall Manager; AWS Network Firewall.
- Decision: block the IP addresses in network ACLs / **AWS WAF on CloudFront and the load balancer, through Firewall Manager** / add AWS Shield Advanced. Accepts: no paid DDoS support; rate limits need tuning.
- Ana asks: "The attack came from 1,400 addresses. Why can we not block those addresses?"
- Diagram: the flood reaches the application; then a web ACL at the edge, and outbound traffic through Network Firewall.

**09 Detection** (stage 3, month 19, order 27, W3)
- Trigger: most of the 43 "no" answers ask for detection and evidence.
- Problem: Callvale cannot answer the bank's questions about changes in production, card numbers in transcripts, software vulnerabilities and stolen credentials. Callvale needs continuous detection in all seven accounts. The findings must appear in one place.
- Adds: Amazon GuardDuty; Amazon Inspector; Amazon Macie; AWS Security Hub; Amazon Detective; AWS Config; AWS Artifact.
- Decision: a weekly manual checklist / open-source scanners on EC2 / **managed detection services for the organization, findings in Security Hub**. Accepts: every finding needs an owner; cost grows with data.
- Chen asks: "Seven services with similar names. Which one answers which of the bank's questions?"
- Diagram: a map from each question to one service; all findings flow into Security Hub.

**10 VPC** (stage 1, month 7, order 6, W2)
- Trigger: the purchase form asks if the database is reachable from the internet. It is.
- Problem: Callvale's web, worker and database instances run in the default VPC with public IP addresses. The database must not be reachable from the internet. The worker must still download software updates. Its large transfers to Amazon S3 must not pass through a NAT device.
- Adds: custom VPC with public and private subnets in two Availability Zones; internet gateway; NAT gateway; gateway endpoint for Amazon S3; security groups.
- Decision: default VPC with tighter security groups / **custom VPC, one NAT gateway, S3 gateway endpoint** / a NAT gateway in each Availability Zone. Accepts: outbound traffic depends on one Availability Zone until stage 2.
- Ben asks: "My worker only talks to S3. Why do I pay for a NAT gateway at all?"
- Diagram: three public instances in the default VPC; then public and private subnets, a NAT gateway and a gateway endpoint.

**11 VPC connectivity** (stage 3, month 18, order 24, W8)
- Trigger: the bank's application must call Callvale privately; both VPCs use 10.20.0.0/16.
- Problem: The bank's application, in the bank's VPC, must call Callvale's API without using the internet. Both VPCs use the CIDR block 10.20.0.0/16. The bank must not reach anything else in Callvale's VPC. Callvale's workloads must also call AWS services privately.
- Adds: AWS PrivateLink endpoint service; Network Load Balancer; interface endpoints; AWS Transit Gateway.
- Decision: a VPC peering connection / a shared transit gateway / **an AWS PrivateLink endpoint service**. Accepts: one service in one direction; fixed cost for each endpoint service.
- Chen asks: "With a peering connection, the two networks would be joined. How does PrivateLink limit the bank to the API?"
- Diagram: bank, internet, public API; then the bank's interface endpoint, the endpoint service, a Network Load Balancer, the API.

**12 Hybrid networking** (stage 3, month 18, order 25, W8)
- Trigger: the bank's recorder runs in a data center in New Jersey; the bank starts in 3 weeks.
- Problem: The bank's data center must send recordings to Callvale's VPC every night. An encrypted connection must be ready in 3 weeks. Within 6 months, the bank requires a private connection with consistent throughput. Callvale's engineers also need access to a private admin tool.
- Adds: AWS Site-to-Site VPN; AWS Direct Connect; AWS Client VPN. Stage 4: a second VPN, to Peldon.
- Decision: VPN only / wait for Direct Connect / **VPN in 5 days, Direct Connect after 10 weeks, VPN kept for backup**. Accepts: two connections to operate; a fixed monthly cost.
- Chen asks: "The bank says that Direct Connect is private. Does private mean encrypted?"
- Diagram: uploads through the internet; then Direct Connect with a backup VPN to the transit gateway.

**13 Route 53** (stage 2, month 11, order 11, W5)
- Trigger: before launch, callvale.example still points to the IP address of one old instance at the registrar.
- Problem: Callvale's domain is hosted at a registrar. The name callvale.example points to the IP address of one old instance. Before launch, callvale.example and app.callvale.example must point to AWS resources by name. Later, DNS must send users to a second Region after a failure.
- Adds: Amazon Route 53 public hosted zone; alias records; health checks. Stage 4: failover routing policy.
- Decision: registrar DNS with CNAME records / an Elastic IP address on one instance / **a Route 53 hosted zone with alias records**. Accepts: resolvers cache answers, so every change needs planning.
- Ben asks: "Why can I not point an A record at the IP address of the load balancer?"
- Diagram: a registrar record to one IP address; then alias records to CloudFront.

**14 Elastic Load Balancing** (stage 2, month 11, order 8, W4)
- Trigger: the load test fails at 150 requests per second; the launch date is fixed.
- Problem: Callvale's web application runs on one instance in one Availability Zone. A load test fails at 150 requests per second. The application must survive the loss of an instance or an Availability Zone. It must serve HTTPS and must route requests by URL path later.
- Adds: Application Load Balancer in three Availability Zones; target group with health checks; HTTPS listener with an ACM certificate. Stages 3 and 4: Network Load Balancers.
- Decision: a spare instance and an Elastic IP address / a Network Load Balancer / **an Application Load Balancer**. Accepts: cost at night; sticky sessions until chapter 29.
- Ben asks: "Application Load Balancer or Network Load Balancer: what decides it for a web application like ours?"
- Diagram: users to one instance; then users, load balancer, instances in three Availability Zones.

**15 CloudFront and Global Accelerator** (stage 2, month 11, order 10, W6)
- Trigger: before launch, 70% of requests are for static files and 20% of users are outside the United States.
- Problem: Instances in one Region serve every request, and 70% of requests are for static files. Recordings are in a private bucket. Only signed-in users can play a recording, for a limited time. Callvale must reduce instance load and latency without making the bucket public.
- Adds: Amazon CloudFront distribution; origin access control for the S3 origins; signed URLs for recordings. Stage 4: AWS Global Accelerator for live audio.
- Decision: a larger web tier / CloudFront for static files only / **CloudFront in front of everything, private S3 origins, signed URLs**. Accepts: cached files can be old after a release.
- Ana asks: "Does the bucket have to be public for CloudFront to serve our recordings?"
- Diagram: all users to one Region; then users, edge locations, origins.

**16 EC2** (stage 1, month 7, order 5, W4)
- Trigger: the demo-day instance is large, idle and hand-built, with port 22 open.
- Problem: Callvale's single instance was installed by hand. Average CPU use is 9%, with peaks of 85% on weekday mornings. Administrators connect with SSH from any IP address. Callvale must launch identical instances in minutes, pay less for idle capacity, and close the administration port.
- Adds: Amazon Machine Image (AMI); launch template; three right-sized instances (web, worker, database); Elastic IP address; Systems Manager Session Manager.
- Decision: keep the instance and restrict SSH / resize in place / **rebuild from an AMI, split the roles, connect with Session Manager**. Accepts: no more quick fixes on a running instance.
- Ana asks: "The instance is at 9% most of the day. Are we paying for a size that we do not need?"
- Diagram: one large instance with port 22 open; then three instances from one image, with no inbound port.

**17 EC2 Auto Scaling** (stage 2, month 11, order 9, W4)
- Trigger: the same load test; the peak comes at the same time every weekday.
- Problem: Callvale's web tier needs 3 instances at night and up to 12 at peak. The peak comes every weekday from 09:00 to 11:00. A new instance needs 4 minutes before it serves traffic. Callvale must replace failed instances automatically and must not pay for 12 instances all day.
- Adds: EC2 Auto Scaling group for the web tier; target tracking scaling policy; scheduled action. After launch day: a second group for conversion workers.
- Decision: 12 instances all day / scheduled scaling only / **target tracking plus a scheduled action at 08:45 (minimum 3, maximum 12)**. Accepts: a sudden spike is served about 4 minutes late.
- Ben asks: "The load balancer has health checks. Is it not the load balancer that replaces a broken instance?"
- Diagram: fixed capacity under a peak curve; then capacity that follows the curve.

**18 Lambda** (stage 2, month 12, order 13, W6)
- Trigger: launch day: the scheduled jobs on the worker stop when the worker is busy.
- Problem: Small jobs run on a schedule on Callvale's worker instance: register an upload, save results, send a notification. Each job runs for seconds, thousands of times in the morning and rarely at night. When the worker is busy, the jobs stop. Callvale wants them to run for each event at no idle cost.
- Adds: AWS Lambda functions (start-job, save-results, notify); execution roles; SQS event source mapping.
- Decision: a larger worker / containers that run all day / **Lambda functions that events invoke**. Accepts: long conversions stay on the workers; database access needs Amazon RDS Proxy.
- Ben asks: "Why not move the audio conversion to Lambda too, and delete the workers?"
- Diagram: pipeline P1, then P2, with the functions highlighted.

**19 Containers** (stage 3, month 20, order 29, W8)
- Trigger: 14 engineers release one application together; one release takes 40 minutes.
- Problem: Callvale's application runs on an Auto Scaling group of instances that the team must patch. 14 engineers release it together, and one release takes 40 minutes. Callvale wants six services that deploy and scale separately, with no instances to patch. One engineer knows Kubernetes.
- Adds: Amazon ECS with AWS Fargate; Amazon ECR; service auto scaling; task roles.
- Decision: six Auto Scaling groups / Amazon EKS / **Amazon ECS with AWS Fargate, six services**. Accepts: less control of the host; a higher price for each unit of compute.
- Ben asks: "ECS or EKS? My one Kubernetes engineer says that EKS is the standard."
- Diagram: one application on instances; then six Fargate services behind the load balancer.

**20 More compute** (stage 4, month 27, order 39, W11)
- Trigger: the bank buys analysis of its archive: 6.7 million recordings in 30 days.
- Problem: Callvale must process 6.7 million archived recordings within 30 days. Each recording is processed alone in about 90 seconds and can start again after an interruption. The job runs one time. Callvale wants the lowest compute cost and does not want to build a job scheduler.
- Adds: AWS Batch with Spot Instances.
- Decision: a larger worker Auto Scaling group / one Lambda invocation for each recording / **AWS Batch on Spot Instances**. Accepts: an interrupted job starts again.
- Ana asks: "It is a single job. What is the cheapest way to finish it in 30 days?"
- Diagram: a map of Callvale's four kinds of compute; the services that Callvale does not use are greyed.

**21 S3** (stage 1, month 6, order 3, W2)
- Trigger: a pilot customer finds that anyone who has the link can download a recording.
- Problem: Callvale stores recordings in a public bucket so that the browser can play them. Recordings contain personal data and must be private. Customers must still upload and play recordings from the browser. Callvale keeps recordings for 7 years, and 2% are opened after 90 days.
- Adds: S3 Block Public Access; presigned URLs; default encryption; S3 Versioning; S3 Lifecycle rule to S3 Standard-IA. Stage 3: SSE-KMS and S3 Object Lock. Stage 4: replication and S3 Glacier Deep Archive.
- Decision: a public bucket with random object names / all transfers through the instance / **a private bucket with presigned URLs (15 and 5 minutes)**. Accepts: a URL works for anyone who holds it until it expires.
- Ana asks: "How can a customer upload directly to our bucket if the bucket is private?"
- Diagram: browser to a public bucket; then browser, presigned URL, private bucket, lifecycle rule.

**22 EBS and instance store** (stage 1, month 6, order 4, W4)
- Trigger: the full volume of month 6.
- Problem: One volume holds the operating system, the database and temporary audio files. The volume filled up and the database stopped for 3 hours. The newest backup was 9 days old. Callvale must lose at most 24 hours of data and must recover within 8 hours.
- Adds: separate gp3 data volume; encrypted volumes; daily snapshots with Amazon Data Lifecycle Manager. Stage 2: instance store for workers.
- Decision: a larger single volume / **a separate data volume with daily snapshots kept 30 days** / a managed database now. Accepts: one instance in one Availability Zone until chapter 26.
- Ana asks: "If that instance fails tomorrow, what do we lose, and how long are we offline?"
- Diagram: one full volume; then a root volume, a data volume and a snapshot timeline.

**23 EFS and FSx** (stage 2, month 13, order 16, W6)
- Trigger: with several web instances, a report made on one instance cannot be downloaded from another.
- Problem: Callvale's application writes report files to the volume of the instance that creates them. A download request often reaches another instance. Linux conversion workers also need one shared directory for large temporary files. The application code that reads and writes files cannot change this year.
- Adds: Amazon EFS file system; mount targets in three Availability Zones. Stage 4: Amazon FSx for Windows File Server for Peldon.
- Decision: sticky sessions / change the code to use Amazon S3 / **a shared Amazon EFS file system**. Accepts: a higher price for each gigabyte than Amazon S3.
- Ben asks: "A volume, a file system or a bucket for these files: how do I decide?"
- Diagram: three instances with their own volumes; then one file system that all instances mount.

**24 AWS Backup** (stage 3, month 22, order 32, W9)
- Trigger: the bank asks for the backup policy, proof of last month's backups and a restore test.
- Problem: Callvale's data is in Amazon Aurora, Amazon DynamoDB, Amazon EFS and Amazon EBS, in several accounts. Each service has different backup settings. The bank requires daily backups kept for 30 days and monthly backups kept for 7 years. Administrators must not be able to delete backups.
- Adds: AWS Backup plans by tag; backup vault with AWS Backup Vault Lock; cross-account copy. Stage 4: cross-Region copy.
- Decision: each service's own settings / custom snapshot programs / **AWS Backup for the whole organization**. Accepts: a second policy layer; storage cost of seven-year copies.
- Chen asks: "If an attacker gets administrator access in production, can the attacker delete our backups?"
- Diagram: four stores with four settings; then one plan, one locked vault, a copy in a second account.

**25 Hybrid storage** (stage 3, month 21, order 31, W9)
- Trigger: the bank's 80 TB archive has 30 days; Dorrin Health wants a nightly SFTP batch.
- Problem: The bank holds 80 TB of old recordings in its data center, in 6.7 million files. The files must be in Amazon S3 within 30 days. A VPN test reached 100 Mbps. The bank allows 500 Mbps on the Direct Connect connection.
- Adds: AWS DataSync; AWS Storage Gateway (Amazon S3 File Gateway); AWS Transfer Family (SFTP).
- Decision: custom copy programs through the VPN (74 days) / an AWS Snow Family device / **AWS DataSync through Direct Connect (15 days)**. Accepts: the import uses the bank's allowance for about 15 days.
- Ana asks: "80 terabytes: do we send it through the network or do we ship storage devices?"
- Diagram: three paths into the audio bucket: DataSync, S3 File Gateway, SFTP endpoint.

**26 RDS** (stage 1, month 8, order 7, W5)
- Trigger: Ben patches PostgreSQL by hand; a second customer asks about recovery.
- Problem: Callvale runs PostgreSQL on one EC2 instance. Ben applies patches and checks backups by hand. If the instance or its Availability Zone fails, the application stops until Ben restores a snapshot. Callvale needs automatic failover and automatic backups without changes to the application.
- Adds: Amazon RDS for PostgreSQL; Multi-AZ DB instance deployment (one standby); automated backups. Stage 2: read replica and Amazon RDS Proxy.
- Decision: replication that Ben builds / **Amazon RDS for PostgreSQL with a Multi-AZ deployment** / move to Amazon DynamoDB. Accepts: paying for a standby that serves no queries.
- Ana asks: "We pay for two databases but we use one. What do we get for the second one?"
- Diagram: one database instance; then a primary and a standby behind one endpoint.

**27 Aurora** (stage 3, month 20, order 30, W5)
- Trigger: the database grows to 1.2 TB; at peak the read replica is 40 seconds behind.
- Problem: Callvale's PostgreSQL database holds 1.2 TB, and 90% of queries are reads. At peak, the one read replica is up to 40 seconds behind the primary. Callvale needs several replicas behind one endpoint, fast failover, and a path to a second Region. The application must stay PostgreSQL-compatible.
- Adds: Amazon Aurora PostgreSQL-Compatible Edition; two Aurora Replicas and the reader endpoint; Aurora Serverless v2 for dev and staging. Stage 4: Aurora Global Database.
- Decision: a larger RDS instance with more replicas / **Amazon Aurora PostgreSQL** / a cache for all dashboard reads. Accepts: a migration with a short cutover; a new cost model.
- Ben asks: "It is still PostgreSQL. What do I get from Aurora that RDS did not give me?"
- Diagram: RDS with one slow read replica; then an Aurora cluster with a reader endpoint.

**28 DynamoDB** (stage 2, month 13, order 15, W5)
- Trigger: launch day: 12 updates for each call and 900 connections stop PostgreSQL.
- Problem: Each call has one job record that the pipeline updates about 12 times. Writes are spiky, from 2 calls a minute at night to 40 at peak. The pipeline reads and writes by call ID and lists one customer's jobs by time. The pipeline needs no joins.
- Adds: Amazon DynamoDB table jobs; global secondary index by-customer; on-demand capacity mode; time to live (TTL). Stage 4: global tables; provisioned capacity with auto scaling.
- Decision: a larger PostgreSQL instance / **Amazon DynamoDB with on-demand capacity** / Amazon ElastiCache for job state. Accepts: access patterns are fixed first; no SQL joins.
- Ben asks: "On-demand or provisioned capacity? I do not know my traffic yet."
- Diagram: pipeline P2, then P3, with the job table highlighted.

**29 ElastiCache** (stage 2, month 13, order 17, W8)
- Trigger: launch day: users are signed out when the Auto Scaling group removes an instance.
- Problem: Callvale keeps user sessions in the memory of each web instance and uses sticky sessions. When an instance is removed, its users are signed out. The 20 most common dashboard queries cause 80% of database reads. Results can be up to 60 seconds old.
- Adds: Amazon ElastiCache replication group in two Availability Zones.
- Decision: sticky sessions and slow scale-in / sessions in DynamoDB plus a read replica / **Amazon ElastiCache for sessions and query results**. Accepts: results up to 60 seconds old; one more cluster.
- Ana asks: "On launch day, users were signed out in the middle of their work. Why, and can it happen again?"
- Diagram: sessions inside each instance; then stateless instances and a cache.

**30 More databases** (stage 4, month 28, order 40, W11)
- Trigger: board reports need complex joins; Peldon brings 200 GB in MongoDB.
- Problem: Callvale's finance team runs complex SQL joins on usage and billing data all day from a business intelligence tool. Separately, Peldon's application stores 200 GB in MongoDB, and its code cannot be rewritten this year. Callvale wants a managed service for each workload.
- Adds: Amazon Redshift; Amazon DocumentDB.
- Decision: everything in Amazon Aurora / MongoDB and a warehouse on EC2 / **Amazon Redshift for reporting, Amazon DocumentDB for the MongoDB workload**. Accepts: two more engines; compatibility tests.
- Ana asks: "We already have Athena on the data lake. Why do you propose a data warehouse too?"
- Diagram: a map of Callvale's data stores by data shape; Neptune and Keyspaces greyed.

**31 Messaging** (stage 2, month 12, order 12, W6)
- Trigger: the launch-day failure: 1,900 uploads fail in 47 minutes.
- Problem: After each upload, Callvale's web application calls the worker and waits. On launch day, the worker was overloaded and 1,900 uploads failed. No upload can be lost again, and one failed recording must not block the others. Several systems must learn when a transcript is ready.
- Adds: Amazon SQS queues (uploads, convert) with dead-letter queues; Amazon SNS topic transcript-ready with two subscribed queues (webhooks, indexing); Amazon EventBridge rules and schedules; S3 Event Notifications.
- Decision: more workers behind an internal load balancer / **SQS queues, an SNS topic for results, EventBridge for AWS events and schedules** / one stream for all events. Accepts: asynchronous processing; workers handle the same message twice without harm.
- Ben asks: "SQS, SNS, EventBridge: all three move messages. When do I use which?"
- Diagram: pipeline P1, then P2, with the queues and the topic highlighted.

**32 Step Functions** (stage 2, month 13, order 14, W9)
- Trigger: the function chain of P2 waits in loops; nobody can see where a call stopped.
- Problem: Callvale processes each call in six steps: convert, transcribe, analyze, summarize, save, notify. Functions call each other and wait in loops, with retries written by hand. Support cannot see where a call failed. Callvale needs managed retries, waiting at no compute cost, and a visible history for each call.
- Adds: AWS Step Functions state machine call-pipeline (Standard workflow). Stage 4: Amazon MQ for Peldon's ActiveMQ broker; Amazon AppFlow from Salesforce to the data lake.
- Decision: more logging on the chain / a workflow engine on EC2 / **AWS Step Functions**. Accepts: a workflow language to learn; a charge for each state transition.
- Ben asks: "I already have queues and Lambda. What does Step Functions add that I cannot write myself?"
- Diagram: pipeline P2, then P3, with the state machine highlighted.

**33 API Gateway** (stage 2, month 14, order 18, W8)
- Trigger: 30 customers ask for an API; one test program sends 200 requests per second.
- Problem: Callvale's customers want a public API. Each customer needs its own key and its own request limit, so that one customer cannot slow the others. Requests must use the customer's Callvale sign-in. Traffic is unpredictable, and Callvale does not want to run instances for the API.
- Adds: Amazon API Gateway REST API with usage plans and API keys; AWS Lambda integrations; Amazon Cognito user pool authorizer. Stage 4: a WebSocket API.
- Decision: new paths on the load balancer / API Gateway in front of the web tier / **API Gateway with Lambda, 20 requests per second for each customer**. Accepts: audio never passes through the API; functions stay small.
- Ana asks: "One customer's program sent 200 requests a second. How do we stop one customer from slowing all the others?"
- Diagram: customer programs on the shared web tier; then API Gateway with keys, limits and an authorizer.

**34 Streaming** (stage 4, month 26, order 37, W9)
- Trigger: Callvale Live starts: up to 3,000 calls are live at the same time.
- Problem: Callvale Live receives 1,500 events a second at peak, each about 1 KB. Two consumers read every event independently: one alerts the agent within 3 seconds, the other stores events for analytics. Events of one call must stay in order. A consumer must be able to read the last 6 hours again.
- Adds: Amazon Kinesis Data Streams stream live-events; AWS Lambda consumer live-insights; Amazon Data Firehose.
- Decision: one SQS queue for each consumer / **Kinesis Data Streams with Data Firehose** / Amazon MSK. Accepts: capacity planning; uneven load between shards.
- Ben asks: "Why not SQS? We already know it."
- Diagram: only the batch pipeline; then live audio, a stream and two consumers.

**35 Analytics** (stage 4, month 26, order 38, W9)
- Trigger: analysts slow the production database; transcript search takes up to 9 seconds.
- Problem: Callvale's analysts query the production database and slow it down. Two years of transcripts and call results are in Amazon S3 in JSON format. Analysts need SQL with no infrastructure to manage and must not see columns with personal data. Customers need transcript search in under 1 second.
- Adds: S3 data lake callvale-lake; AWS Glue Data Catalog, crawlers and jobs; Amazon Athena; AWS Lake Formation; Amazon OpenSearch Service; Amazon Quick.
- Decision: a larger replica for analysts / a data warehouse for all data / **a data lake with AWS Glue and Amazon Athena, OpenSearch Service for search**. Accepts: data must be converted; results are only up to date with the last load.
- Ana asks: "Why can the analysts not use the production database? It already has all the data."
- Diagram: everything on the production database; then a data lake and a search domain.

**36 AI and ML at a glance** (stage 4, month 28, order 41, W11)
- Trigger: five AI features in one quarter; the ML engineers want to train their own models.
- Problem: Callvale must ship five AI features in one quarter. The features translate Spanish transcripts, read 4,000 scanned pages a month, speak a daily summary, answer chat questions and flag identity documents in screenshots. A sixth feature, a churn-risk score, needs a custom model. Callvale has three ML engineers.
- Adds: Amazon Translate; Amazon Textract; Amazon Polly; Amazon Lex; Amazon Rekognition; Amazon SageMaker AI.
- Decision: own models for every feature / open-source models on GPU instances / **managed AI services, and SageMaker AI for the one custom model**. Accepts: less control of model quality; cost follows usage.
- Ben asks: "My ML engineers can build these models. Why should we pay an API for each call?"
- Diagram: a map from input type to AI service (the roles table in A4).

**37 Monitoring** (stage 3, month 19, order 28, W10)
- Trigger: transcripts are 6 hours late one night; the bank asks who changed a security group.
- Problem: Callvale's pipeline was 6 hours late and nobody was alerted. The bank asks who changed a security group last Tuesday, and Callvale cannot answer. Callvale needs alarms on waiting work, all logs in one place, and a record of every API call for 7 years.
- Adds: Amazon CloudWatch metrics, alarms, Logs and dashboards; AWS CloudTrail organization trail; AWS X-Ray; Amazon SNS topic ops-alerts.
- Decision: log files and a weekly review / Prometheus and Grafana on EC2 / **Amazon CloudWatch, AWS CloudTrail and AWS X-Ray**. Accepts: log volume becomes a cost; alarms need tuning.
- Chen asks: "CloudWatch or CloudTrail: which one tells me who changed the security group?"
- Diagram: two paths: what is happening (CloudWatch, X-Ray), and who did what (CloudTrail).

**38 Deploy and operate** (stage 4, month 24, order 34, W10)
- Trigger: the second Region cannot be built by hand.
- Problem: Callvale built its production environment by hand in two years. Callvale must now create a smaller copy in a second Region and keep both identical. Callvale must also patch 40 conversion workers each month without connecting to them, and wants advice on unused resources.
- Adds: AWS CloudFormation templates and StackSets; Systems Manager Patch Manager; AWS Trusted Advisor; AWS Compute Optimizer; AWS Well-Architected Tool.
- Decision: a runbook and console work / custom programs that call the AWS CLI / **AWS CloudFormation templates with StackSets**. Accepts: three weeks to bring resources under templates; no more manual changes.
- Ana asks: "Why do we need three weeks of templates before the team can start on the second Region?"
- Diagram: one hand-built Region; then the same stacks in two Regions and every account.

**39 Migration** (stage 4, month 25, order 36, W10)
- Trigger: Callvale acquires Peldon; the lease of Peldon's data center ends in 6 months.
- Problem: Peldon runs 40 servers on VMware and a 600 GB Oracle database in a data center whose lease ends in 6 months. The applications must move to AWS with a cutover of at most 4 hours. The database must become PostgreSQL-compatible. Four engineers know the applications.
- Adds: AWS Application Migration Service; AWS Database Migration Service (AWS DMS); AWS Schema Conversion Tool (AWS SCT).
- Decision: rebuild in containers first / VMware Cloud on AWS / **rehost the servers, convert Oracle to Aurora PostgreSQL with ongoing replication**. Accepts: old designs arrive unchanged; manual conversion work.
- Ana asks: "The lease ends in 6 months. What is the fastest safe way out of that data center?"
- Diagram: Peldon's data center; then replication to EC2 and Aurora, and a 4-hour cutover.

**40 High availability and disaster recovery** (stage 4, month 24, order 35, W7)
- Trigger: the bank's RPO and RTO for the loss of a Region; the first test is due at month 27.
- Problem: Callvale runs in one Region, across three Availability Zones. A bank contract requires an RPO of 15 minutes and an RTO of 1 hour if the whole Region fails. A test must prove it every 6 months. Ana wants the lowest cost that meets these numbers.
- Adds: second Region: US West (Oregon); Aurora Global Database; DynamoDB global tables; S3 Cross-Region Replication; Route 53 failover routing; multi-Region KMS keys; AWS Backup cross-Region copy.
- Decision: backup and restore / pilot light (the first design; test 1 failed) / **warm standby** / multi-site active/active. Accepts: paying all month for a small second copy of every service.
- Ana asks: "If the Virginia Region fails, what do I tell the bank, and what does the standby cost me in a normal month?"
- Diagram: the four strategies on one axis, with the RTO marker and the two test results.

**41 Cost optimization** (stage 4, month 29, order 42, W7)
- Trigger: the credits ended at month 17; the bill doubled in 6 months; Ana wants 20% less.
- Problem: Callvale's bill has doubled in 6 months. Fargate services run a steady load, and conversion workers vary from 0 to 60 instances and tolerate interruption. Dev and staging run all week but are used for 50 hours. Of 190 TB of recordings, 140 TB is older than 90 days.
- Adds: AWS Budgets; AWS Cost Explorer; AWS Cost and Usage Report with Amazon Athena; cost allocation tags; Compute Savings Plan; Spot Instances; S3 Lifecycle rule to S3 Glacier Deep Archive.
- Decision: Reserved Instances for everything / **a Compute Savings Plan for 70% of steady compute, Spot workers, lifecycle rules, schedules for dev and staging** / a cheaper Region. Accepts: a commitment that is paid even if usage falls; hours to restore archived recordings.
- Ana asks: "Where does the money go, and what can we cut this quarter with no effect on customers?"
- Diagram: the bill as one bar by category, with one saving for each category.

**42 Security patterns** (stage 3, month 23, order 33, W10)
- Trigger: the bank's auditors visit in 4 weeks.
- Problem: A bank auditor will follow one recording through four layers: identity, resource-based policy, network and encryption. At each layer the auditor asks who or what allows access. Callvale must show each control and the evidence that the control works.
- Adds: nothing new. A review of the controls of chapters 03 to 12, 21, 24 and 37.
- Decision: answer the 180 questions one by one / list every security service / **follow one recording through four layers**. Accepts: gaps become visible and must be closed before the audit.
- Chen asks: "For this one recording, show me every place where access could be allowed by mistake."
- Diagram: one recording's path from the bank's data center to a supervisor, with four control layers under it.

**43 Decoupling, scaling and caching patterns** (stage 2, month 15, order 19, W10)
- Trigger: Ben writes the review of launch day and lists five couplings.
- Problem: On launch day, Callvale's web tier scaled out and the system still failed. Uploads waited for one worker, and every step updated one database table. Sessions and report files lived on single instances. Callvale must remove each coupling with little change to the code.
- Adds: nothing new. A review of the launch-week changes of chapters 15, 17, 18, 23, 26, 28, 29, 31, 32 and 33.
- Decision: larger instances in every tier / rewrite in small services now / **fix the five couplings one by one**. Accepts: more parts; duplicate and late messages.
- Ben asks: "We scaled the web tier and the system still failed. What did we miss?"
- Diagram: the launch-day path, before and after, with five numbered couplings.

The five couplings of chapter 43, in fixed order: (1) the upload request waits for the worker; (2) one worker cannot grow with the backlog; (3) every step updates one PostgreSQL table; (4) sessions and report files live on single instances; (5) the pipeline calls the webhook sender and the search indexer one after the other.
