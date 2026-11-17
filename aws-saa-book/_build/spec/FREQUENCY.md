I could not read Reddit at all. Reddit blocks this tool's user agent for both search and fetch, so every Reddit signal below is secondhand (T8, T9). Medium (403) and Udemy (403) were also blocked. The usable first-hand exam reports from 2023 to 2026 number about 11, and most of them list "what to study" more than "what I saw". Official AWS pages and instructor syllabi carry the rest. Source codes ([F], [C], [T], [A]) link to URLs in the Source key at the end.

Several 2026 sites still claim an SAA-C04 exists. These include the 2026 update of [C10], [T11], and two sites seen only in search results ([citadelcloudmanagement](https://www.citadelcloudmanagement.com/blog/aws-saa-c04-exam-guide-2026-format-domains-and-pass-score), [signalthirty](https://www.signalthirty.com/post/aws-solutions-architect-certification-2026-study-guide)). I treat the "2026 additions" on those sites as unreliable.

## Audit summary
- **Her top tier matches the most-reported topics.** S3, VPC, IAM, EC2, RDS/Aurora, DynamoDB, ELB/ASG and Lambda lead every source type, including AWS's own sample questions [A3].
- **Biggest gaps in her list:**
  - FSx
  - Kinesis
  - The analytics stack: Athena, Glue, Redshift, EMR, Lake Formation
  - Global Accelerator
  - DR strategy patterns and Elastic Disaster Recovery
  - Security detection services and AWS Config
  - Cognito, IAM Identity Center and Directory Service
  - DMS, Application Migration Service (MGN) and Transfer Family
  - Step Functions
  - Systems Manager
  - Cost tools and Savings Plans types
  - ML services, at recognition level only
- **Possible re-tiering:**
  - SQS/SNS/EventBridge and KMS deserve top-tier depth.
  - Containers, especially EKS scaling, show up more than candidates expect [F1][F2][F7].
- **Facts have changed since many practice questions were written.** S3 objects can now be 50 TB, SQS/SNS messages 1 MiB, some Lambda invocations can run 90 minutes, and Snowball Edge is closed to new customers. Exam items may still use the old numbers (section 5).

---

## 1. Ranked topics (about 40)

"FH n" = number of first-hand reports naming the topic. "Syl" = instructor or vendor syllabi that emphasise it. The depth column is my own inference: D = deep scenario trade-offs, M = know the use cases plus 2–3 key features, S = keyword recognition.

| # | Topic | Evidence | Sub-topics people report or emphasise | Depth | Sources |
|---|---|---|---|---|---|
| 1 | S3 | FH 6; 2 of the 10 official sample questions; all syllabi. Very strong | Storage classes and minimum durations; lifecycle; Intelligent-Tiering; versioning; CRR/SRR; Object Lock; SSE-S3/SSE-KMS/SSE-C/client-side; presigned URLs; CORS; Access Points; event notifications; Transfer Acceleration; multipart; S3 Select; Requester Pays (exam guide). One report calls S3 "extremely important" | D | F1 F4 F6 F8 F9 F11 A3 C1 T2 |
| 2 | VPC core | FH 5; official sample (NAT). Very strong | Subnets, route tables, IGW, NAT gateway (one per AZ vs shared), security groups vs NACLs, bastion, gateway vs interface endpoints | D | F3 F6 F8 F9 F11 A3 A2 C1 |
| 3 | IAM | FH 5. Very strong | Roles vs users, cross-account roles and trust policies, identity- vs resource-based policies, reading policy JSON, SCP interplay, least privilege | D | F2 F4 F6 F8 F9 C1 T12 |
| 4 | EC2 and purchasing | FH 4; 4 of the 10 official sample questions. Strong | On-Demand vs RI vs Spot; hibernation; secondary ENI failover; instance families; placement groups; instance store | D | A3 F6 F9 F11 C1 C4 C10 |
| 5 | Containers (ECS/EKS/Fargate/ECR) | FH 5, "more than expected" [F2]. Strong | Fargate vs EC2 launch type, task roles, ECS/EKS Anywhere, EKS Cluster Autoscaler/Metrics Server [F1], Karpenter [F2], migrating apps to containers | M+ | F1 F2 F7 F8 F9 C1 A2 |
| 6 | Lambda / serverless | FH 4. Strong | Limits and memory sizing (exam guide), triggers, SQS→Lambda, function URLs [F1], Lambda@Edge, RDS Proxy pairing | D | F1 F6 F8 F9 A2 C1 |
| 7 | RDS | FH 3; official sample. Strong | Multi-AZ (instance vs cluster), read replicas, backups/PITR, encryption, RDS Proxy (named in the exam guide), MySQL vs PostgreSQL | D | A3 F4 F6 F8 A2 C1 C4 |
| 8 | Aurora | FH 3; official sample. Strong | Replicas plus reader endpoint, shared storage, Aurora Serverless v2 [F6], Global Database (TD scenario: RPO 1 s / RTO under 1 min) | D | A3 F4 F6 F8 C1 T18 |
| 9 | DynamoDB | FH 3. Strong | On-demand vs provisioned, global tables [F6], DAX, Streams, TTL, GSI/LSI, Standard-IA table class | D | F4 F6 F8 C1 C4 C10 |
| 10 | ELB | FH 3. Strong | ALB vs NLB vs GWLB (exam-guide skill), health checks, sticky sessions, TLS offload | D | F2 F6 F8 A2 C1 |
| 11 | EC2 Auto Scaling | FH 2; 2 official sample questions. Strong | Target tracking / step scaling with warm-up / scheduled actions; ELB health checks; lifecycle hooks; multi-AZ | D | A3 F6 F8 C1 T4 |
| 12 | SQS | FH 3; official sample. Strong | Buffering DB writes, Standard vs FIFO, visibility timeout, DLQ, long polling, retention period [F2] | D | A3 F2 F6 F8 C1 C10 |
| 13 | Data migration / hybrid storage | FH 3. Strong | DataSync vs Storage Gateway types, Snowball, Snowmobile (retired), Transfer Family | D/M | F3 F4 F8 C1 C3 C4 T2 |
| 14 | CloudFront | FH 2; reported as students' recurring exam topic. Strong | Latency scenarios, path-based behaviours, Lambda@Edge [F4], OAC/OAI, signed URLs and cookies | D | F4 F8 C6 C1 T2 |
| 15 | Analytics / data lake | FH 4. Moderate–strong | Athena, Glue (CSV→Parquet), Redshift, EMR/Spark/Hive, Kafka [F1], Lake Formation | M | F1 F4 F6 F7 A2 C1 |
| 16 | DR strategies / RTO-RPO | FH 2; many syllabi. Moderate–strong | Backup & restore / pilot light / warm standby / multi-site, Elastic Disaster Recovery [F1], AWS Backup | D | F1 F8 C3 C8 T7 A2 |
| 17 | KMS and encryption | FH 1; official sample (SSE-C). Moderate–strong | Customer-managed vs AWS-managed keys, rotation, audit, multi-Region keys | D | F4 A3 C1 C10 A2 |
| 18 | EventBridge / SNS | FH 3. Moderate | SNS→SQS fan-out, EventBridge rules and schedules; the SNS/SQS/EventBridge trio is a common confusion [F4] | M | F4 F6 F8 C1 |
| 19 | Route 53 | FH 1; recurring in student feedback [C6]. Moderate–strong | All routing policies, health checks, alias vs CNAME, private hosted zones | D/M | F8 C1 C4 C6 |
| 20 | Kinesis | FH 2. Moderate | Data Streams vs Data Firehose vs Video Streams; SQS vs Kinesis | M | F6 F7 C1 C3 C9 |
| 21 | FSx family | FH 2; 5 syllabi. Moderate | Windows (SMB/AD), Lustre (HPC, S3-linked), ONTAP, OpenZFS | M | F2 F8 C1 C3 C4 C9 C10 |
| 22 | Global Accelerator | FH 1 (named as a hardest comparison); exam guide examples. Moderate | Static anycast IPs, TCP/UDP, regional failover, vs CloudFront | M | F8 A2 C3 C7 C9 |
| 23 | EBS / instance store | FH 1; syllabi. Moderate | gp3 vs io2 [C8], SSD vs HDD, snapshots, Multi-Attach, ephemeral instance store | M/D | F8 C1 C3 C4 C8 |
| 24 | EFS | FH 1. Moderate | Shared Linux NFS, storage classes and lifecycle, vs FSx | M | F8 C1 C3 |
| 25 | Organizations / SCP / Control Tower / Identity Center | FH 1; exam guide task 1.1. Moderate | SCPs cap permissions but do not grant them; permission sets; Control Tower guardrails | M/D | F4 A2 C1 C3 T8 |
| 26 | Hybrid connectivity (DX, VPN) | FH 2. Moderate | DX vs VPN provisioning time and performance [C9], VPN over DX, DX resilience, bandwidth choice | M/D | F6 F8 C1 C9 A2 |
| 27 | Transit Gateway / peering / PrivateLink / endpoints | FH 2. Moderate | Transitive routing, segmentation, PrivateLink, RAM | M/D | F6 F11 C1 C9 A2 |
| 28 | CloudWatch / CloudTrail / Config | FH 2. Moderate | Alarms, custom metrics, agent, org trail, Config rules | M | F2 F6 C1 C3 |
| 29 | WAF / Shield / ACM | FH 1. Moderate | SQL injection/XSS, rate rules, Shield Advanced, certificates on ALB/CloudFront | M | F6 A2 C1 C10 |
| 30 | Secrets Manager vs Parameter Store | FH 1. Moderate | Automatic rotation, avoiding hard-coded credentials | M | F4 C3 C4 |
| 31 | ElastiCache | FH 0; exam guide ("caching strategies"); syllabi. Moderate | Redis vs Memcached, lazy loading vs write-through, session store | M | A2 C3 C10 |
| 32 | API Gateway | FH 1. Moderate | Throttling, authorizers, caching, REST vs HTTP | M | F6 A2 C1 |
| 33 | CloudFormation / Beanstalk | FH 2. Moderate–weak | StackSets, least-ops deployment | S/M | F6 F9 C1 C2 C3 |
| 34 | ML managed services | FH 2. Moderate–weak | Rekognition, Comprehend, Transcribe, Translate, Lex, Textract, Polly, SageMaker AI | S | F1 F4 C1 A1 |
| 35 | Cognito / federation / Directory Service | FH 0; exam guide; syllabi | User pools vs identity pools, AD Connector vs Managed AD | M/S | A2 C1 C3 C9 |
| 36 | DMS / SCT / MGN | FH 1 (generic). Moderate–weak | Heterogeneous migration, CDC, rehost | M/S | F3 A2 C1 C9 |
| 37 | Security detection (GuardDuty, Macie, Inspector, Security Hub, Detective, Network Firewall, Firewall Manager) | FH 0; exam guide names GuardDuty and Macie | "Which service detects / scans / classifies…" | S/M | A2 C1 C10 T3 T7 |
| 38 | Step Functions / Amazon MQ / AppFlow | FH 0; exam guide names Step Functions | Orchestration; migrating a broker without code changes | S/M | A2 C1 C3 C9 |
| 39 | Systems Manager | FH 0; practice-question pattern | Session Manager vs bastion, Parameter Store, patching | S/M | C1 C3 T4 |
| 40 | Cost tools | FH 1 (generic); exam guide repeats them in every Domain 4 task | Cost Explorer, Budgets, CUR, tags, Savings Plans, Compute Optimizer, Trusted Advisor | M/S | A2 C4 C6 T7 |
| 41 | Edge / HPC compute | FH 0 | Outposts, Local Zones, Wavelength, Batch, placement groups | S | A2 C1 C6 C10 |
| 42 | Purpose-built databases | FH 0 | Neptune, DocumentDB, Keyspaces; "columnar" and "time-series" (exam guide) | S | A2 C6 C7 T3 |

The official sample questions [A3] cover:
- NAT gateway plus route table (Select TWO)
- Hibernation to keep in-memory state
- Secondary ENI failover
- S3 CORS
- SSE-C or client-side encryption when keys stay on-premises
- On-Demand rather than Spot for jobs that must not be interrupted
- An SQS buffer for a database that can't keep up
- New-AZ subnets + ASG/ALB + RDS Multi-AZ (Select TWO)
- Step scaling with warm-up
- Aurora replica plus reader endpoint

---

## 2. Reported topics missing from her list (ranked)

| # | Missing service(s) | Evidence | Where it shows up | Sources |
|---|---|---|---|---|
| 1 | Athena, Glue, Lake Formation, Redshift, EMR, MSK, OpenSearch, Quick (formerly QuickSight) | FH 4; exam guide task 3.5 | SQL on S3 with least ops; CSV→Parquet ETL; data-lake permissions; BI warehouse; existing Spark/Hive or Kafka jobs | F1 F4 F6 F7 A2 C1 |
| 2 | Kinesis (Data Streams, Data Firehose, Video Streams) | FH 2 + syllabi | Streaming ingestion; real-time vs near-real-time; ordering and replay; delivering logs to S3 | F6 F7 C3 C9 |
| 3 | FSx (all types) | FH 2 + 5 syllabi | Protocol or workload match: SMB/AD, HPC, NetApp | F2 F8 C3 C9 |
| 4 | DR patterns and Elastic Disaster Recovery (she only has AWS Backup) | FH 2 | RTO/RPO → cheapest pattern that meets them | F1 F8 C3 T7 |
| 5 | Global Accelerator | FH 1 + exam guide | Static IP or allow-listing, non-HTTP traffic, multi-Region failover | F8 A2 C3 |
| 6 | Config, GuardDuty, Macie, Inspector, Security Hub, Detective, Network Firewall, Firewall Manager, GWLB | Exam guide examples + syllabi | One-line "which service detects/records/inspects…"; third-party firewall appliances → GWLB | A2 C10 T3 T4 |
| 7 | Cognito, IAM Identity Center, Directory Service, STS/federation, CloudHSM | Exam guide tasks 1.1 and 1.2 | App users vs workforce single sign-on; on-prem AD; dedicated HSM | A2 C1 C3 T4 |
| 8 | DMS/SCT, Application Migration Service (MGN), Transfer Family | FH 1 + exam guide | Database migration with minimal downtime; heterogeneous engines; rehost; SFTP clients | F3 A2 C1 C9 T2 |
| 9 | Step Functions (also Amazon MQ, AppFlow) | Exam guide + syllabi | Orchestration, retries, human approval; JMS/AMQP broker migration | A2 C1 C9 |
| 10 | Systems Manager | Practice patterns | Access without a bastion; fleet patching; parameters | T4 C3 |
| 11 | Cost Explorer, Budgets, CUR, cost allocation tags, Compute Optimizer, Trusted Advisor, Savings Plans types | Exam guide Domain 4 | Alerts, chargeback, right-sizing | A2 C4 |
| 12 | ML managed services | FH 2 | Pick the managed AI service | F1 F4 C1 |
| 13 | CloudFormation (StackSets), Elastic Beanstalk | FH 2 | Repeatable infrastructure across accounts/Regions; least-ops deployment | F6 F9 C1 |
| 14 | Neptune, DocumentDB, Keyspaces | Syllabi | Keyword → database mapping | C6 C7 T3 |
| 15 | Outposts, Local Zones, Wavelength, Batch, placement groups | Exam guide + syllabi | Edge/residency/latency; long batch jobs; HPC | A2 C1 C10 |
| 16 | RAM, X-Ray | Exam guide / ACG list | Sharing TGW or subnets across accounts; tracing | A2 C9 |

---

## 3. "X vs Y" discriminators

The sources show where a pair is flagged as exam-relevant. The deciding rules are standard AWS behaviour; where a source gives a different rule, I say so.

**Networking**
| Pair | Decides it | Sources |
|---|---|---|
| Security group vs NACL | Stateful / allow-only / ENI-level vs stateless / allow+deny / subnet-level; "block an IP range" → NACL | C3 T1 T3 T5 |
| NAT gateway vs NAT instance; one NAT per AZ vs shared | Managed and AZ-resilient vs cheaper self-managed; HA → one per AZ | A2 T6 T3 |
| NAT gateway vs gateway endpoint | Private-subnet traffic to S3/DynamoDB without internet or NAT charges → gateway endpoint | F8 T3 T4 |
| Gateway vs interface vs GWLB endpoint | S3/DynamoDB, free, route-table target vs ENI-based for most services (reachable from on-prem) vs inline appliance inspection | C3 T3 T5 |
| Peering vs Transit Gateway vs PrivateLink | Few VPCs, non-transitive vs hub-and-spoke at scale, transitive vs exposing one service to many consumers (overlapping CIDRs OK) | A2 C1 C9 |
| Site-to-Site VPN vs Direct Connect | Fast and encrypted over the internet vs consistent private bandwidth with weeks of lead time; encryption on DX → VPN over DX; DX backup → VPN; maximum resilience → two DX locations | C1 C9 C3 |
| Client VPN vs Site-to-Site VPN | Individual users vs network-to-network (now listed separately in scope) | A1 |
| ALB vs NLB vs GWLB | L7 path/host routing, WAF, Lambda targets vs L4 TCP/UDP, static IPs, extreme performance vs third-party appliances | A2 C1 T4 T5 |
| CloudFront vs Global Accelerator | HTTP(S) caching at the edge vs TCP/UDP, 2 static anycast IPs, fast failover, no caching | C3 F8 T5 |
| Static IP required | ALB has none → NLB with EIPs, or Global Accelerator | T5 |
| Route 53 latency vs geolocation vs geoproximity (plus weighted/failover/multivalue) | Best performance vs user location (compliance, localisation) vs resource-location bias; canary → weighted; active-passive → failover | C3 C4 C1 |
| Alias vs CNAME | Zone apex and AWS targets → alias | C1 |
| ELB vs Route 53 vs EC2 health checks | ASG should use the ELB health check type for app-level health; DNS failover → Route 53 | C3 C1 F6 |
| S3 presigned URL vs CloudFront signed URL vs signed cookies vs OAC | Direct S3 object vs via CDN vs many files; "bucket only via CloudFront" → OAC (OAI is legacy) | C3 T2 C1 |
| S3 Transfer Acceleration vs CloudFront vs multipart | Long-distance uploads vs global downloads vs large objects | T2 F6 C3 |
| Lambda@Edge vs CloudFront Functions | Heavier logic or network calls vs lightweight header/URL rewrites. Only Lambda@Edge is sourced; CloudFront Functions is my addition | F4 C1 |

**Compute**
| Pair | Decides it | Sources |
|---|---|---|
| Lambda vs Fargate vs ECS on EC2 vs EC2 vs Batch | Event-driven ≤15 min vs serverless containers vs control/GPU vs full OS vs long batch jobs | C3 C8 C6 A2 |
| ECS vs EKS | Existing Kubernetes, portability, EKS Anywhere vs simplest AWS-native | C3 F1 F2 |
| On-Demand vs RI/Savings Plans vs Spot vs Dedicated Host vs Capacity Reservation | Uninterruptible/short vs steady-state vs interruptible vs BYOL per-socket licences vs guaranteed AZ capacity | A3 C4 C10 |
| Compute Savings Plans vs EC2 Instance Savings Plans vs RI | Flexible across families, Regions, Fargate and Lambda vs one family in one Region. New since Dec 2025: Database Savings Plans | C10 A12 |
| Placement groups: cluster vs spread vs partition | Low-latency HPC vs isolating critical instances vs Hadoop/Kafka racks | C10 C1 C4 |
| Target tracking vs step vs scheduled vs predictive scaling | Keep a metric at target vs tiered with warm-up vs known calendar vs forecast cycles | A3 T4 C1 |
| Hibernate vs stop vs instance store | Keep RAM state → hibernate; instance store is lost on stop | A3 |
| Beanstalk vs CloudFormation | Least-ops app deployment vs IaC and StackSets. TD's version also includes OpsWorks/CodeDeploy, which are out of scope | C3 C1 |
| Step Functions vs SQS vs chained Lambdas | Orchestration with state/retries/approvals → Step Functions (Standard ≤1 yr, Express ≤5 min) | C3 T5 A2 |

**Storage**
| Pair | Decides it | Sources |
|---|---|---|
| S3 vs EBS vs EFS vs instance store | Object vs single-AZ block vs shared Linux NFS vs ephemeral highest IOPS | C3 C1 F8 |
| EFS vs FSx Windows vs Lustre vs ONTAP | Linux NFS vs SMB/AD/DFS vs HPC/ML with S3 link vs multi-protocol NetApp | C3 C10 C4 |
| gp3 vs io2 vs st1 vs sc1 | Default/cost-effective vs sustained high IOPS and Multi-Attach vs sequential throughput vs cold; HDD can't be a boot volume | C8 C3 |
| S3 classes | Unknown access pattern → Intelligent-Tiering; rare access with ms retrieval → Glacier Instant Retrieval; minutes–hours → Glacier Flexible; 12–48 h → Deep Archive; re-creatable data → One Zone-IA; know minimum durations and retrieval fees | C3 T1 T2 C6 |
| Intelligent-Tiering and tiny objects | Correction: [T1]'s "tiny files → Intelligent-Tiering" trap is shaky. Objects under 128 KB are never auto-tiered and are billed at Frequent Access rates [A7] | A7 T1 |
| Object Lock (compliance vs governance) vs versioning/MFA Delete vs lifecycle | Write-once (WORM), even root can't delete → compliance mode; lifecycle can't *protect* data | T2 C1 T8 |
| SSE-S3 vs SSE-KMS (+ bucket keys) vs SSE-C vs client-side | Default vs audit/rotation/key policies vs keys supplied per request vs encrypt before upload; keys kept on-premises → SSE-C or client-side | A3 F4 T2 |
| DataSync vs Storage Gateway | Migration or scheduled copy vs ongoing hybrid access with local cache | C3 C4 T2 |
| File vs Volume (cached / stored) vs Tape Gateway | NFS/SMB to S3 vs iSCSI with primary data in S3 vs primary on-prem with backups to S3 vs VTL | C10 C4 C1 |
| DataSync vs Snowball vs Transfer Family | Enough bandwidth vs PB-scale with weak links vs SFTP/FTPS clients that can't change. Snowball is closed to new customers (section 5) | T2 C3 A5 |
| AWS Backup vs native snapshots | Central, cross-account/Region, Vault Lock | C1 C4 A2 |

**Database**
| Pair | Decides it | Sources |
|---|---|---|
| Multi-AZ vs read replica | Availability (sync, same endpoint) vs read scaling (async, cross-Region). The Multi-AZ *cluster* option has readable standbys | T1 T5 C1 F8 |
| RDS vs Aurora | Up to 15 replicas, 6-copy storage, fast failover, Global Database | C3 F4 T1 |
| Aurora Global DB vs cross-Region replica vs DynamoDB Global Tables | Relational RPO ~1 s / RTO <1 min vs a cheaper DR copy vs multi-active NoSQL | T18 F6 C10 |
| RDS/Aurora vs DynamoDB | Joins, transactions, SQL vs key-value at any scale | C3 T1 |
| DynamoDB on-demand vs provisioned | Spiky or unknown traffic vs steady and cheaper | F6 T6 T1 |
| DAX vs ElastiCache | Microsecond DynamoDB reads with no code change vs a general cache | T1 T5 |
| Redis vs Memcached | Persistence, replication, pub/sub, sorted sets vs simple multithreaded cache | C3 T5 T15 |
| GSI vs LSI | Any time, different partition key vs only at table creation, same partition key, strong consistency option | C3 C4 |
| RDS Proxy | Lambda connection storms, "too many connections", faster failover | A2 C1 T20 |
| Neptune / DocumentDB / Keyspaces / Redshift | Graph / MongoDB / Cassandra / columnar warehouse. Timestream and QLDB are now out of scope | T3 A2 A1 |

**Integration and analytics**
| Pair | Decides it | Sources |
|---|---|---|
| SQS vs SNS vs EventBridge | Pull-based buffer vs push fan-out vs rules, SaaS/AWS events, schedules | F8 F4 T6 |
| SQS Standard vs FIFO | Strict ordering and exactly-once processing → FIFO | T5 T3 C10 |
| SQS vs Kinesis Data Streams | Ordering per shard, replay, multiple consumers → Kinesis | C9 C3 |
| Kinesis Data Streams vs Data Firehose | Custom real-time consumers vs managed near-real-time delivery to S3/Redshift/OpenSearch | C3 T5 C10 |
| Amazon MQ vs SQS/SNS | Existing JMS/AMQP/MQTT broker with no code changes → MQ | C9 C1 [MQ guide](https://docs.aws.amazon.com/pdfs/amazon-mq/latest/migration-guide/amazon-mq-mg.pdf) |
| Athena vs Redshift vs EMR vs Glue | Ad-hoc SQL on S3 vs warehouse/BI vs Spark/Hive clusters vs serverless ETL and catalog | T6 A2 F1 F6 |
| MSK vs Kinesis | Existing Kafka → MSK | F1 A1 |

**Security and identity**
| Pair | Decides it | Sources |
|---|---|---|
| IAM policy vs SCP vs permissions boundary | SCPs cap permissions and never grant them; they don't apply to the management account | C3 T8 T12 |
| Identity-based vs resource-based policy; cross-account | Role in the resource account, trust policy naming the principal | F4 T7 T4 |
| Roles/STS vs IAM user access keys | Temporary credentials always win | T5 |
| IAM Identity Center vs Cognito user pools vs identity pools | Workforce SSO across accounts vs app sign-in vs temporary AWS credentials for app users | T4 C3 |
| AD Connector vs Managed Microsoft AD vs Simple AD | Proxy to on-prem AD vs real AD in AWS with trusts vs Samba-based (Simple AD is now in maintenance) | C1 A4 |
| KMS vs CloudHSM | Since KMS reached FIPS 140-3 Level 3, the decider is single-tenant, customer-exclusive control or PKCS#11, not FIPS level (third-party source; verify) | T16 C1 |
| Secrets Manager vs Parameter Store | Native rotation → Secrets Manager | C3 C4 F4 |
| WAF vs Shield Std/Adv vs Network Firewall vs Firewall Manager | L7 SQL injection/XSS/rate limits vs DDoS (Advanced adds response team and cost protection) vs VPC traffic inspection vs central multi-account policy | C10 T4 |
| GuardDuty / Macie / Inspector / Detective / Security Hub / Config | Threats / PII in S3 / vulnerability scans / investigation / aggregated findings / configuration compliance | T3 T6 A2 |
| CloudTrail vs CloudWatch vs Config | Who called the API vs metrics/logs/alarms vs config history and rules | C3 T3 |
| Session Manager vs bastion | No open ports, IAM-based, audited | T4 C1 |

**Ops, DR and cost**
| Pair | Decides it | Sources |
|---|---|---|
| Backup & restore vs pilot light vs warm standby vs multi-site | RTO/RPO and budget, hours → near-zero | C3 T7 C8 T5 |
| High availability vs fault tolerance vs DR | Brief failover acceptable vs no degradation vs recovery from disaster | C1 C4 |
| Cost Explorer vs Budgets vs CUR vs Compute Optimizer vs Trusted Advisor | Analyse vs alert vs raw detail vs right-size vs best-practice checks | A2 C4 T7 |
| CloudWatch agent vs SSM agent | OS metrics and logs vs management | C3 |

---

## 4. Qualifier phrases in question stems

| Phrase | Selects for | Sources |
|---|---|---|
| "LEAST operational overhead" / "MOST operationally efficient" / "LEAST effort" | Managed or serverless and native features (Secrets Manager rotation, Session Manager, Firehose, Fargate, DynamoDB, Aurora Serverless) over custom code or EC2. Reported as the most frequent qualifier | T1 T4 T18 C12 |
| "MOST cost-effective" / "as cost-effectively as possible" | The cheapest option that still meets *every* constraint. Spot is wrong if the job can't be interrupted [A3]; Glacier IR when access is rare but retrieval must be in ms | A3 T1 C6 |
| "MOST secure" | Private paths, least privilege, customer-managed keys, temporary credentials | C6 |
| "highly available" vs "fault tolerant" | Multi-AZ ASG + ALB + RDS Multi-AZ [A3] vs no-impact redundancy | A3 C1 C4 |
| "without downtime" / "minimize downtime" | Multi-AZ (not read replicas); SQS buffering | T1 A3 |
| "MOST resilient" / "durable" | Multi-AZ or multi-Region, DX at two locations | T18 C1 |
| "minimize latency for global users" | CloudFront, Global Accelerator, latency routing, DAX/ElastiCache | T18 T5 |
| "real-time" vs "near real-time" | Kinesis Data Streams vs Firehose | T5 |
| "decouple" / "can't keep up" / "spikes" | SQS (scale workers on queue depth) | A3 A2 |
| "privately" / "without traversing the internet" | VPC endpoints, PrivateLink, DX | T2 T3 |
| "cannot be deleted or modified" / "WORM" | Object Lock compliance mode, Backup Vault Lock | T2 |
| "unpredictable" / "spiky" | Lambda, DynamoDB on-demand, Aurora Serverless v2 | T1 |
| "steady-state" / "1–3 years" | RIs or Savings Plans | A3 T6 |
| "can tolerate interruption" | Spot | A3 |
| "minimal code changes" / "cannot modify the application" | MGN, same-engine RDS, Amazon MQ, EFS/FSx, Storage Gateway | A2 C9 |
| "temporary credentials" | IAM roles/STS | T5 |
| "audit who did" / "track config" / "detect threats" / "find PII" | CloudTrail / Config / GuardDuty / Macie | T3 T6 |
| "existing on-premises AD" | Identity Center + AD Connector or Managed AD | A2 C1 |
| "static IPs" / "allow-list" | NLB with EIPs or Global Accelerator | T5 |
| "(Select TWO.)" | Each chosen option must be independently necessary. AWS does not publish partial-credit rules; "no partial credit" is a third-party claim only | A3 A2 |

**Wording style**
- AWS uses fixed stem patterns: "A company… A solutions architect must… Which solution meets these requirements?", "Which combination of steps… (Select TWO.)", "in the most efficient manner and without downtime" [A3].
- Answer options are often full sentences that combine several services [F1].
- Japanese reports describe 3–5-line stems with 1–3-line options. This comes from a search summary of Qiita posts, so it is weak evidence.
- A common technique is to read the constraint sentence (usually the last) first [T1][T18].

---

## 5. New in 2025–2026, and topics that faded

**Reported in exam-taker posts (moderate confidence)**
- Aurora Serverless v2 [F6]. Serverless v1 reached end of life on 31 Mar 2025 [A14].
- DynamoDB global tables and capacity modes [F6].
- More container/EKS depth: Karpenter [F2], Cluster Autoscaler and Metrics Server [F1], "ECS family" named as a gap [F7].
- Lambda function URLs and Elastic Disaster Recovery [F1]. These were new in 2023; I found no 2025–26 confirmation.
- Apache-ecosystem analytics (Spark, Parquet, Kafka, Hive) [F1].
- AI-service integration [F4]. This rests on one vendor-authored source.

**What vendors emphasise (not proof of exam content)**
- TD says it added Network Firewall, Security Hub, MFA, IPSec and Object Lock [C5].
- The same TD page also still lists Forecast, Fraud Detector, Kendra, Data Pipeline and AppSync, which suggests it is partly stale.

**Renamed in the current official list [A1] compared with v1.0 [A2]**
- AWS SSO → IAM Identity Center
- Kinesis Data Firehose → Amazon Data Firehose
- SageMaker → SageMaker AI
- QuickSight → Amazon Quick
- Personal Health Dashboard → AWS Health Dashboard
- "AWS VPN" is now split into Client VPN and Site-to-Site VPN
- Kinesis Data Analytics → Managed Service for Apache Flink (not re-verified this session)

**Unverified "new" claims (no first-hand evidence, and absent from [A1])**
- Bedrock, Amazon Q, Nova
- VPC Lattice, Verified Access, Verified Permissions
- DataZone, Aurora DSQL, S3 Express One Zone, zero-ETL
- Graviton emphasis, IPAM, "Sustainability (NEW 2025)"
- Sources: T11, T12 (which itself says "not primary targets"), C10's 2026 update (which also wrongly announces SAA-C04).
- Amazon Q Business has been in maintenance since 30 Jun 2026 [A4].
- No new question types on SAA-C03: ordering, matching and case-study questions launched on AIF-C01 and MLA-C01 only [A13].

**Facts that changed; exam items may still use the old values**

| Fact | Old (practice-question era) | Current | Source |
|---|---|---|---|
| S3 max object size | 5 TB | 50 TB (2 Dec 2025) | A11 |
| SQS max message | 256 KB | 1 MiB (Aug 2025) | A10 |
| SNS max message | 256 KB | Optional 1 MiB, default 256 KiB (18 Sep 2026) | A9 |
| Lambda timeout | 15 min | 15 min for synchronous calls; 90 min on Lambda Managed Instances for async/event-source invocations (9 Sep 2026) | A8 |
| Snowball Edge | Standard offline-transfer answer | Closed to new customers 7 Oct 2025; AWS points to DataSync, Data Transfer Terminal, Outposts | A5 A21 |

Snow Family is still in the official in-scope list [A1], so expect Snowball to remain the exam answer. That is my inference.

Other changes:
- S3 Select and Glacier Select are closed to new customers (Jul 2024), so Athena is the answer for SQL on S3.
- S3 Object Lambda closed (Nov 2025).
- The Glacier vault API is in maintenance (Oct 2025); the storage classes are unaffected.
- FSx File Gateway is in maintenance (Oct 2024).
- Simple AD is in maintenance (Jun 2026).
- Sources: [A4].

**Rarely or no longer appearing (de-prioritise)**
- Removed from the official in-scope list between v1.0 (Feb 2022) [A2] and today [A1]:
  - QLDB (end of support 31 Jul 2025, per [InfoQ](https://www.infoq.com/news/2024/07/aws-kill-qldb/))
  - Timestream (LiveAnalytics in maintenance)
  - Forecast
  - Fraud Detector
  - Kendra
  - AppSync
  - Data Pipeline
  - Pinpoint
  - Proton
  - Audit Manager
  - Application Discovery Service
  - Migration Hub
  - Server Migration Service
- Most of these are now in maintenance [A4].
- They still appear in TD's product page [C5], Cantrill's ML section [C1], DCT [C6], ExamPro [C7] and Coding N Concepts ("time series → Timestream") [T3].

---

## 6. Hardest areas and common reasons people fail

1. **Breadth and unfamiliar services.**
   - "Wide, not deep" [F6].
   - Lost points on unfamiliar services [F3].
   - About 10 questions with unfamiliar terminology [F10].
   - Content not covered in Maarek's course [F7].
   - An AWS Academy instructor suggests deep study of about 40 services, basic knowledge of 60, and a skim of 31 [C12].
2. **Several workable answers; picking the "most correct".**
   - "Half of AWS seemed capable of solving the exact same problem"; CloudFront vs GA and NAT vs endpoint were the hardest pairs [F8].
   - SNS/SQS/EventBridge, Aurora vs RDS, and S3 encryption options [F4].
   - Answers often differ by a single qualifier [T8].
   - Red herrings [F13].
3. **Missing qualifier words under time pressure** [T13][T14].
4. **Security depth: IAM policy logic, cross-account access, SCPs, KMS.**
   - [F4]; one report names security as the hardest area [F9].
   - Vendors claim IAM is the most-missed topic [T12][T15]. Weak evidence.
5. **Networking: Transit Gateway vs peering vs PrivateLink, DX/VPN performance and provisioning.**
   - [C9]; [F8].
   - Search-snippet sources [T17] are weak.
6. **Multiple-response questions** [F6]; 2–3 correct answers out of 5+ [F1].
7. **Time and reading load.**
   - One candidate used nearly the full time, and online-proctoring lag and a crash cost minutes [F10].
   - Two reports recommend a test centre [F3][F6].
   - For her specifically: AWS gives non-native speakers +30 minutes (ESL +30). Request it once, *before* registering [A6]. One 2026 candidate says "there is no downside" [F7].
8. **Outdated material** [T13][T14]; see the facts-drift table in section 5.
9. **Pass rates.** AWS publishes no pass rate; "40% fail" figures are unverified [T14].

---

## 7. Practice-exam vendors and score predictors

| Vendor | Reported closeness to the real exam | Sources |
|---|---|---|
| Tutorials Dojo (Bonso) | The most-cited benchmark; usually a bit harder and wordier than the real exam. "Highly resemble" [F5]; real exam "less wordy and easier" [F3]; one real question matched a TD review set [F2]; 2026 reviews split between "nearly same difficulty" and "harder" [F12]; Reddit-synthesis #1 [T8]; vendor blogs agree [T9][T10][T11] | F2 F3 F5 F12 T8 |
| Digital Cloud Training (Neal Davis) | "Highly resemble" (single first-hand source) | F5 |
| Maarek practice exams (Udemy) | Mixed. "Do not resemble" [F5]; real exam "easier than Stephane's practice tests" [F7]; vendor blog says about exam difficulty [T9] | F5 F7 T9 |
| Whizlabs | Only self-interested evidence | F4 C12 |
| AWS official (20-question free set; full practice exam on Skill Builder) | Recommended for format; no score-correlation data found | A15 F5 F7 |
| ping-t (Japanese) | Difficulty ≈ real exam for Japanese candidates | F10 F11 F9 |

**Score → outcome data points (all anecdotal)**

| Practice result | Real result | Source |
|---|---|---|
| ~50% first attempt → ~80% second attempt | 832 | F6 |
| ≥80% on TD, Davis and Maarek | 863 | F5 |
| 70–80% on Maarek | 823 | F7 |
| 76–80% on Whizlabs | 812 | F4 |
| 58% on TD first attempt (review mode) | 791 | F2 |

**Pass thresholds people advise**

| Advice | Source | Strength |
|---|---|---|
| TD 80–100% consistently | TD reviewer [F12] | Anecdotal |
| TD ≥90% | TD's own advice [C5] | Vendor |
| Consistent 85% on TD | [T11] | Unsourced |
| 65% on TD ≈ 73–78% real | [T9] | Vendor, anecdotal |
| 80%+ on timed full-length sets | [T10][T15] | Vendors |

The modal advice is about 80% on *first-attempt, timed* TD sets. That repeated attempts inflate scores is my inference.

[T8] (secondhand Reddit synthesis) flags SkillCertPro promotion as astroturf. I excluded dump sites per your instruction.

---

## Source key

**Official AWS**
- A1 [Current in-scope list](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html)
- A2 [Exam guide v1.0 (2022)](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide_C03.pdf)
- A3 [Official sample questions](https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Sample-Questions.pdf)
- A4 [Services in maintenance](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html)
- A5 [Snowball Edge change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- A6 [ESL +30](https://aws.amazon.com/certification/policies/before-testing)
- A7 [S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
- A8 [Lambda 90 min](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/)
- A9 [SNS 1 MiB](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sns-1mib-support/)
- A10 [SQS 1 MiB](https://www.amazonaws.cn/en/new/2025/amazon-sqs-increases-maximum-message-payload-size-to-1mib/)
- A11 [S3 50 TB](https://aws-news.com/article/2025-12-02-amazon-s3-increases-the-maximum-object-size-to-50-tb)
- A12 [Database Savings Plans](https://aws.amazon.com/about-aws/whats-new/2025/12/database-savings-plans-savings)
- A13 [New question types](https://aws.amazon.com/blogs/training-and-certification/aws-certification-new-exam-question-types)
- A14 [Aurora Serverless v1 EOL](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-serverless-v1-ending-soon)
- A15 [Skill Builder SAA-C03](https://skillbuilder.aws/category/exam-prep/solutions-architect-associate-SAA-C03)
- A21 [Data Transfer Terminal](https://aws.amazon.com/about-aws/whats-new/2024/12/aws-data-transfer-terminal-high-speed-data-uploads/)

**First-hand exam reports**
- F1 [Bonso, Sep 2023](https://www.linkedin.com/pulse/saa-c03-aws-certified-solution-architect-associate-exam-jon-bonso)
- F2 [tklevits, Jul 2024](https://dev.to/tklevits/studying-for-the-aws-saa-4000)
- F3 [iamdete, Jul 2024](https://dev.to/iamdete/from-zero-to-saa-c03-certified-how-i-passed-the-aws-certification-on-my-first-attempt-20m6)
- F4 [Whizlabs author (vendor)](https://www.whizlabs.com/blog/how-i-passed-the-aws-solutions-architect-associate-exam-sa-c03/)
- F5 [nishath, Sep 2025](https://dev.to/nishath_jp/how-i-passed-the-aws-solutions-architect-associate-saa-c03-exam-with-863-marks-102a)
- F6 [NashTech, Dec 2025](https://blog.nashtechglobal.com/sharing-my-experience-passing-the-aws-solutions-architect-associate-saa-c03/)
- F7 [dwye, Jan 2026](https://dwye.dev/en/post/saa-c03/)
- F8 [Perera, exam Sep 2026](https://dev.to/gimnathperera/i-survived-aws-saa-c03-heres-what-actually-helped-me-pass-jc)
- F9 [QES, Sep 2026](https://www.qes.co.jp/media/aws/a1089)
- F10 [Qiita, Feb 2025](https://qiita.com/yuuki_0524/items/284076e4ce05e7d50f19)
- F11 [Qiita, Apr 2025](https://qiita.com/Lambwool_711/items/6b9d0fa5f430664433e8)
- F12 [TD reviews 2026](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-associate-practice-exams/)
- F13 [Suchit, 2023](https://www.linkedin.com/pulse/how-i-prepared-passed-aws-solutions-architect-saa-c03-suchit-y8uxe)

**Course syllabi and vendor topic lists**
- C1 [Cantrill](https://learn.cantrill.io/p/aws-certified-solutions-architect-associate-saa-c03)
- C2 [Maarek sections](https://dev.to/franciscojeg78/aws-saa-c03-30-day-learning-plan-using-stephane-maareks-ultimate-aws-certified-solutions-architect-17j3)
- C3 [TD comparisons](https://tutorialsdojo.com/comparison-of-aws-services/) / [TOC](https://gist.github.com/Mirakurun/caddfaf9f7a6587545fb1dfaece43dc1)
- C4 [TD video course](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-associate-exam-video-course/)
- C5 [TD product page](https://portal.tutorialsdojo.com/product/aws-certified-solutions-architect-associate-practice-exams/)
- C6 [DCT](https://digitalcloud.training/aws-certified-solutions-architect-saa-c03/)
- C7 [ExamPro outline](https://www.freecodecamp.org/news/pass-the-aws-certified-solutions-architect-associate-certification/)
- C8 [Whizlabs top-15](https://www.whizlabs.com/blog/top-15-aws-architect-associate-exam/)
- C9 [ACG 6 areas](https://www.pluralsight.com/resources/blog/cloud/aws-solutions-architect-associate-exam-blueprint-6-areas-to-master) / [ACG SAA-C03](https://www.pluralsight.com/resources/blog/cloud/new-aws-saa-c03-exam)
- C10 [Jayendra Patil](https://jayendrapatil.com/aws-certified-solutions-architect-associate-saa-c03-exam-learning-path/)
- C12 [Pothecary](https://dev.to/ryanpothecary/sitting-the-aws-solution-architect-associate-saa-c03-exam-60-times-2e7p)

**Third-party guides (weaker)**
- T1 [DevCloudLab](http://www.devcloudlab.com/blog/aws-saa-c03-exam-guide/)
- T2 [theinfinity S3](https://theinfinity.dev/articles/amazon-s3-saa-c03-exam-guide)
- T3 [CodingNConcepts notes](https://codingnconcepts.com/aws/aws-certified-solutions-architect-associate/)
- T4 [CodingNConcepts question set](https://codingnconcepts.com/aws/aws-certified-solutions-architect-associate-exam-questions/) (provenance unclear; used for phrase patterns only)
- T5 [quick-ref card](https://github.com/ChathurangaVKD/AWS-Certified-Solutions-Architect-Associate-SAA-C03/blob/main/exam-reviews/quick-reference/ULTRA-QUICK-REFERENCE-CARD.md)
- T6 [Community Builder cheat sheet](https://dev.to/aws-builders/technologies-and-concepts-cheat-sheet-for-solutions-architect-associate-saa-c03-h52)
- T7 [towardsthecloud](https://towardsthecloud.com/blog/aws-solutions-architect-associate-exam-guide)
- T8 [Reddit synthesis](https://jake-kelley.github.io/study-materials/saa/index.html)
- T9 [readroo.st](https://readroo.st/blog/tutorial-dojo-vs-stephane-maarek-practice-tests-saa-c03)
- T10 [certsqill](https://www.certsqill.com/blog/best-aws-solutions-architect-practice-exams/)
- T11 [learnersink](https://www.learnersink.com/blog/aws-saa-vs-saa-c03-changes)
- T12 [open-exam-prep](https://open-exam-prep.com/blog/aws-solutions-architect-associate-exam-guide-2026)
- T13 [sailor.sh](https://sailor.sh/blog/aws-solutions-architect-common-mistakes/)
- T14 [evolveskill](https://evolveskill4.com/blog/aws/why-candidates-fail-saa-c03-exam-how-to-pass-guide)
- T15 [examcert](https://www.examcert.app/blog/aws-saa-c03-complete-guide/)
- T16 [KMS vs CloudHSM](https://tocconsulting.fr/compare/kms-vs-cloudhsm-vs-acm)
- T17 [studytech](https://studytech.ai/blog/aws-solutions-architect-associate-study-guide-2026) / [certscope](https://www.certscope.com/blog/aws-saa-c03-pass-rate-and-how-to-beat-it) (search snippets only)
- T18 [TD study path](https://tutorialsdojo.com/aws-certified-solutions-architect-associate-exam-saa-c03-study-path/) (search snippet only)
- T20 [RDS Proxy planning](https://docs.aws.amazon.com/en_us/AmazonRDS/latest/AuroraUserGuide/rds-proxy-planning.html)

The claude.ai Excalidraw, Gmail, Google Calendar and Google Drive connectors need to be authorized in your claude.ai connector settings before they can be used.
