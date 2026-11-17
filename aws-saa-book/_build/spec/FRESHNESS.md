# AWS changes from January 2024 to October 2026 that affect SAA-C03 prep material (checked against AWS pages on 2026-10-04)

**How this was built.** I read the document-history pages of about 60 AWS user guides as `.md` with curl. I also read AWS's lifecycle lists (Maintenance, Sunset and Full Shutdown), the current SAA-C03 exam guide, and AWS What's New and blog posts.

**Two things to know before you write:**
- The Product Lifecycle URL you gave now redirects to https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html. AWS now announces closures in batches: 2025-10-07, 2025-11-07, 2026-03-31, 2026-06-30 and 2026-09-29.
- **The current SAA-C03 exam guide is out of step with AWS.** It already uses the new names Amazon Quick, Amazon SageMaker AI and Amazon Data Firehose. But it still lists Amazon Elastic Transcoder (fully shut down 2025-11-13) and AWS Snow Family (no longer sold to new customers) as in scope. Source: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html

**Status codes used in the tables:**
- **V** means I confirmed it on an AWS page I opened (user guide, document history, What's New, or AWS blog).
- **S** means I found an AWS What's New or blog link but only read it through a search-result summary.
- **3P** means only third-party sources confirm it.
- "V (date S)" means the fact is confirmed on an AWS page but the date comes from a search summary.
- "DH" means a user guide's document-history page.

## 2026 at a glance
- **01-15:** You can now change an EBS volume up to 4 times in 24 hours, without the old 6-hour wait.
- **01-27:** Kinesis Data Analytics for SQL fully shut down.
- **01-29:** EventBridge events can be up to 1 MB (S).
- **02-02:** IAM Identity Center can run in more than one Region.
- **02-03:** DynamoDB global tables can replicate across AWS accounts.
- **02-16:** EC2 nested virtualization no longer needs a bare-metal instance.
- **02-18:** ACM public certificates now last 198 days.
- **02-24:** IMDSv2 can be enforced for a whole account.
- **02-25:** X-Ray SDKs and daemon went into maintenance mode.
- **03-12:** S3 account-regional bucket namespaces (date S).
- **03-31:** Lifecycle batch: App Runner, CloudTrail Lake, SNS message data protection, ARC readiness check, RDS Custom for Oracle (sunset).
- **April:** S3 turned SSE-C off by default for new buckets.
- **04-07:** S3 Files (date 3P).
- **04-20:** Client VPN can attach directly to a Transit Gateway.
- **05-15:** SCP quotas went to 10 per node and 10,240 characters.
- **05-20:** Inspector Classic and DMS Fleet Advisor fully shut down.
- **05-31:** CloudTrail Lake closed to new customers.
- **06-30:** Lifecycle batch: Simple AD, Cognito Sync, Kendra, SSM Application Manager. Amazon Linux 2 reached end of support.
- **07-01:** RDS no longer restores snapshots to magnetic storage. The Systems Manager advanced-instances tier was removed.
- **07-15:** Lambda code storage default went from 75 GB to 300 GB.
- **08-19:** IAM roles default to 20 managed policies.
- **08-29:** Kinesis Data Streams can deliver straight to S3.
- **09-09:** Lambda Managed Instances allow a 90-minute timeout for async and event-source-mapping invocations.
- **09-18:** SNS messages can be up to 1 MiB if you opt in.
- **09-24:** EventBridge launched a new Custom Event Bus.
- **09-29:** Lifecycle batch. ElastiCache Serverless gained public endpoints.

---

## 1. Watchlist by service

### EC2, Auto Scaling, purchasing, hibernation, Spot
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Public IPv4 addresses are charged | 2024-02-01 | In-use public IPs and attached Elastic IPs were free → every public IPv4 address is billed ($0.005/IP-hour) | [VPC IP addressing](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html), [AWS blog](https://aws.amazon.com/blogs/aws/new-aws-public-ipv4-address-charge-public-ip-insights/) | Cost answers now favor IPv6 or a NAT/ALB front end. "An attached EIP is free" is wrong. | V (date S) |
| Launch configurations blocked | 2024-10-01 | Accounts created on or after this date can't create launch configurations by any method. Console was blocked from 2023-06-01; no new instance types since 2023-01-01 | [Launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html) | Only launch templates are a valid answer | V |
| IMDSv2 becomes the norm | 2024-03-25 account default; mid-2024 new instance types are IMDSv2-only; 2026-02-24 account-level enforcement | IMDSv1 allowed by default → IMDSv2 default, and can be enforced | [EC2 DH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/DocumentHistory.html), [AWS blog](https://aws.amazon.com/blogs/aws/amazon-ec2-instance-metadata-service-imdsv2-by-default/) | Questions on SSRF and credential theft | V (mid-2024 item: S) |
| Hibernation on Graviton | 2024-07-30 | Intel/AMD only → also C6g/C7g/M6g/M7g/R6g. Limits unchanged: Linux RAM under 150 GiB, Windows 16 GiB or less, 60 days max, not allowed in an Auto Scaling group or ECS | [Hibernation limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html) | Keep the limits; drop "x86 only" | V |
| Capacity Blocks for ML | 2024-11-21 (up to 182 days, instant start, extend); 2026-02-02 (share across organization); 2026-02-25 (Local Zones) | Up to 14 days → up to 6 months | EC2 DH | A new purchasing option to teach alongside RI, Savings Plans, ODCR and Spot | V |
| On-Demand Capacity Reservations (ODCR) | 2024-11-21 future-dated; 2025-11-21 interruptible; 2026-06-02 cancel a future-dated one | Start immediately only → can be booked for a future date | EC2 DH | "Guarantee capacity for a planned event" now has a native answer | V |
| Allowed AMIs, plus Organizations declarative policies | 2024-12-01 | SCP or Config workarounds → native account setting, enforceable across the organization | EC2 DH | Governance answers | V |
| Nested virtualization on virtual instances | 2026-02-16 | Needed a `.metal` instance → works on normal virtual instances | EC2 DH | "Use bare metal" is no longer the only answer | V |
| Precision-time placement group | 2026-06-29 | Cluster/partition/spread → adds a fourth type | EC2 DH | Low exam risk | V |
| Auto Scaling: AZ distribution strategies, zonal shift, Capacity Reservation preference, high-resolution target tracking | 2024-11-07 / 11-18 / 11-20 / 11-22 | — | [ASG DH](https://docs.aws.amazon.com/autoscaling/ec2/userguide/DocumentHistory.html) | Resilience and scaling answers | V |
| Auto Scaling lifecycle hooks can target Lambda directly | 2025-07-28 | Via EventBridge, SNS or SQS → Lambda directly | ASG DH | Simpler hook design | V |
| Auto Scaling: root-volume replacement during instance refresh; synchronous `LaunchInstances` API; "reservations then balanced" | 2025-11-20; 2025-11-18; 2026-06-30 | — | ASG DH | Patching and placement | V |
| Spot allocation guidance | Current doc | `lowest-price` → `price-capacity-optimized` is "recommended"; `lowest-price` is "not recommended" | [Allocation strategies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html) | Spot best practice | V |
| Amazon Linux 2 end of support | 2026-06-30 | Supported → reached end of support; use AL2023 | [AL2 FAQ](https://aws.amazon.com/amazon-linux-2/faqs/) | Which AMI a scenario should use | V |
| EC2 Global View renamed AWS Global View | 2026-06-30 | Name change | EC2 DH | Trivia | V |

### EBS
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| gp3 limits raised | 2025-09-26 | 16 TiB / 16,000 IOPS / 1,000 MiB/s → **64 TiB / 80,000 IOPS / 2,000 MiB/s**. Ratio is 500 IOPS per GiB; baseline still 3,000 IOPS and 125 MiB/s | [gp3](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html), [EBS DH](https://docs.aws.amazon.com/ebs/latest/userguide/doc-history.html) | Changes memorized numbers and the "when to move up to io2" threshold | V |
| Every io2 volume is io2 Block Express | 2025-04-30 | io2 had lower limits than Block Express → all io2 volumes get up to 256,000 IOPS (on Nitro), 64 TiB, average latency under 500 µs | [Provisioned IOPS](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html) | Max-IOPS questions; io1 is legacy | V |
| Elastic Volumes frequency | 2026-01-15 | Wait 6 hours between changes → start a new change as soon as the last completes, up to 4 per rolling 24 hours | [Modify requirements](https://docs.aws.amazon.com/ebs/latest/userguide/modify-volume-requirements.html) | A classic memorized number is now wrong | V |
| Recycle Bin covers EBS volumes | 2025-11-20 | Snapshots and AMIs only → volumes too | EBS DH | Accidental-deletion answers | V |
| Instant volume copy (same AZ); set an initialization rate when creating a volume | 2025-10-14; 2025-05-06 | Snapshot then restore, or Fast Snapshot Restore → direct copy, or a chosen fill rate | EBS DH | An alternative to Fast Snapshot Restore | V |
| Time-based snapshot and AMI copies | 2024-11-26; 2025-02-25 | Best effort → you choose a completion deadline | EBS DH | DR answers with an RPO | V |
| Declarative policy for snapshot Block Public Access | 2024-12-01 | — | EBS DH | Organization-wide governance | V |
| Multi-Attach (unchanged) | — | io1 and io2 only, up to 16 Nitro instances in the same AZ; on Windows, io2 only | [Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html) | Still valid | V |

### S3 and Glacier
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Default bucket quota | 2024-11-14 | 100 per account → **10,000**, can be raised to 1 million | [Bucket quotas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-s3-up-1-million-buckets-per-aws-account/) | Number | V (date S) |
| Maximum object size | 2025-12-02 | 5 TB → **50 TB**. Must use multipart upload; single PUT still 5 GB; console upload 160 GB; a single GET is limited to 5 TB | [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html), [S3 DH](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WhatsNew.html) | Number | V |
| Conditional writes and deletes | 2024-08-20 (`If-None-Match`); 2024-11-25 (`If-Match`, plus bucket-policy condition keys); 2025-09-16 (conditional delete) | Last write wins → S3 can refuse an overwrite or delete | S3 DH | Concurrency and "prevent overwrite" answers | V |
| Default data-integrity checksums (CRC) | 2024-12-01 | Checksums optional → computed by default | S3 DH | A default changed | V |
| Lifecycle transitions skip small objects | 2024-09-24 | Objects under 128 KB are no longer transitioned by default | S3 DH | A default changed | V |
| Express One Zone: SSE-KMS support, then up to 85% price cut | 2024-09-17; 2025-04-10 | — | S3 DH, [AWS blog](https://aws.amazon.com/blogs/aws/up-to-85-price-reductions-for-amazon-s3-express-one-zone/) | Cost and latency answers | V (price cut S) |
| S3 Tables; S3 Metadata GA; S3 Vectors preview then GA | 2024-12-03; 2025-01-27; 2025-07-15 then 2025-12-02 | New bucket types (table buckets, vector buckets) | S3 DH, [re:Invent 2025 roundup](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025/) | New services in "analytics on S3" answers | V |
| S3 Select and Glacier Select closed to new customers | 2024-07-25 | — | S3 DH, [Maintenance list](https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html) | Remove from answers | V |
| S3 Object Lambda closed to new customers | 2025-11-07 | — | [Object Lambda change](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html) | Remove from answers | V |
| Account-regional bucket namespaces | 2026-03-12 | Names must be globally unique → optional namespace reserved for your account and Region (name gets an account/Region suffix) | [Namespaces](https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-s3-account-regional-namespaces) | Softens "bucket names are globally unique" | V (date S) |
| **SSE-C disabled by default** | April 2026 | SSE-C allowed → off for new buckets, and for existing buckets in accounts with no SSE-C objects; turn it on with `PutBucketEncryption` | [SSE-C FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-s3-c-encryption-setting-faq.html) | A default changed | V |
| S3 Files (mount a bucket as an NFS file system) | 2026-04-07 | Mountpoint or a gateway → managed file-system access to a bucket | [S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html) | Muddies "S3 vs EFS" answers | V (date 3P) |
| Original Glacier vault service ("Amazon Glacier") closed to new customers | Announced 2025-10-07; closed 2025-12-15 | Glacier vault API → use S3 Glacier storage classes | [Glacier guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) | Teach only the storage classes | V (closure date 3P) |
| Earlier changes many notes still miss: SSE-S3 default encryption (2023-01-05); Block Public Access on and ACLs off for new buckets (2023-04-27); Object Lock on existing buckets (2023-11-20) | — | — | [Default encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html), S3 DH | Defaults | V |

### EFS and FSx
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| EFS file system types and Archive class; replicate into an existing file system (failback) | 2023-11-26 / 11-27 | Standard-IA / One Zone-IA wording → Regional or One Zone file systems with Standard, IA and Archive classes | [EFS DH](https://docs.aws.amazon.com/efs/latest/ug/document-history.html) | Naming and DR | V |
| EFS cross-account replication | 2024-11-19 | Same account only → cross-account | EFS DH | DR | V |
| EFS Elastic throughput raised in steps (2024-03 to 2025-05) | — | Regional Elastic now: 20–60 GiBps read, 1–5 GiBps write, 0.9–2.5 million read IOPS, 1,500 MiBps per client | [EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) | Numbers | V |
| EFS quotas | 2024-05-15; 2025-02-10 | Mount targets per VPC 400 → 1,400; access points per file system 1,000 → 10,000 | EFS DH | Numbers | V |
| FSx for Lustre Intelligent-Tiering | 2025-05-29 | SSD or HDD only → elastic tiered storage | [Lustre DH](https://docs.aws.amazon.com/fsx/latest/LustreGuide/doc-history.html) | Cost-optimized HPC | V |
| FSx for OpenZFS Single-AZ (HA) and Intelligent-Tiering | 2024-07-09; 2024-12-01 | — | [OpenZFS DH](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/document-history.html) | — | V |
| FSx for ONTAP second generation | 2024-03-04; 2024-07-09 | Up to 12 HA pairs and 72 GBps on scale-out | [ONTAP DH](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/document-history.html) | Numbers | V |
| S3 access points attached to FSx | 2025-06-25 (OpenZFS); 2025-12-02 (ONTAP) | NFS/SMB only → S3 API access to the same file data | DH pages above | Analytics on file data without copying | V |

### VPC, NAT, endpoints, PrivateLink, Transit Gateway, peering, Lattice
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| **Regional NAT gateway** | 2025-11-19 | One zonal NAT gateway per AZ in a public subnet, with per-AZ routes → one regional NAT gateway, **no public subnet needed**. It spreads across AZs on its own (taking up to 60 min to reach a new AZ) and supports up to 32 IPs per AZ (zonal: 8). No private NAT; not in constrained AZs | [Regional NAT](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html) | Overturns "HA NAT means one gateway per AZ" | V |
| VPC Block Public Access, plus declarative policy | 2024-11-19; 2024-12-01 | Security groups, NACLs, SCPs → one account-level block on internet-gateway traffic, with exclusions | [VPC BPA](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) | "Block internet access everywhere" answers | V |
| Security groups can attach to multiple VPCs and be shared | 2024-10-30 | One VPC per security group → several VPCs in a Region; shareable across the organization | [VPC DH](https://docs.aws.amazon.com/vpc/latest/userguide/WhatsNew.html) | Multi-VPC designs | V |
| VPC Route Server; VPC encryption controls | 2025-03-31; 2025-11-21 (paid from 2026-03-01) | — | VPC DH | Appliance failover; encryption-in-transit compliance | V (pricing date S) |
| **Interface endpoints across Regions** | 2024-11-26 (endpoint services); **2025-11-19 (some AWS services, e.g. S3, ECR, Route 53)** | Same Region only → cross-Region | [PrivateLink DH](https://docs.aws.amazon.com/vpc/latest/privatelink/doc-history.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services) | Private cross-Region access no longer needs peering or a Transit Gateway | V |
| Resource endpoints and service-network endpoints (PrivateLink + VPC Lattice) | 2024-12-01 | Needed an NLB in front of an endpoint service → share a resource (e.g. a database) directly | PrivateLink DH, [Lattice DH](https://docs.aws.amazon.com/vpc-lattice/latest/ug/doc-history.html) | Cross-account access to a database without an NLB | V |
| DynamoDB interface endpoints (PrivateLink) | 2024-03-19 | Gateway endpoint only → interface endpoint too, reachable from on-premises | [DynamoDB DH](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html) | Private on-premises access to DynamoDB | V |
| Transit Gateway: security-group referencing; direct Network Firewall attachment; encryption support and flexible cost allocation; Client VPN attachment; policy-based routing | 2024-09-25; 2025-06-16; 2025-11-20; 2026-04-20; 2026-07-28 | Inspection VPC → Network Firewall attaches to the Transit Gateway itself | [TGW DH](https://docs.aws.amazon.com/vpc/latest/tgw/doc-history.html) | Peering vs Transit Gateway comparisons; centralized inspection | V |
| Transit Gateway bandwidth per VPC attachment | Date unknown | 50 Gbps → up to 100 Gbps per AZ | [TGW quotas](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html) | Number | V (value only) |
| VPC peering | — | No document-history entries for 2024–2026 | [Peering DH](https://docs.aws.amazon.com/vpc/latest/peering/doc-history.html) | Unchanged | V |

### Elastic Load Balancing
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| LCU reservation (set a minimum capacity) | 2024-11-20 (ALB, NLB); 2025-04-10 (GWLB) | Ask Support to pre-warm → set it yourself | [ALB DH](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/doc-history.html), [NLB DH](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/doc-history.html), [GWLB DH](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/doc-history.html) | Flash-sale and event-traffic answers | V |
| ALB: header changes on all response codes; URL and host rewrites; JWT validation | 2025-02-28; 2025-10-15; 2025-11-21 | — | ALB DH | ALB can now validate machine-to-machine tokens | V |
| NLB: disable an AZ; QUIC; weighted target groups; listener rules; wider zonal shift | 2025-02-13; 2025-11-13; 2025-11-19; 2026-07-10; 2026-09-24 | One target group per action → weighted target groups | NLB DH | Native blue/green on an NLB | V |
| Earlier changes notes often miss: NLB security groups (2023-08-10); ALB mutual TLS (2023-11-26) | — | — | NLB/ALB DH | — | V |

### Route 53, CloudFront, Global Accelerator
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Route 53 Profiles; new record types (HTTPS, SVCB, SSHFP, TLSA); DNS Firewall Advanced | 2024-04-22; 2024-10-29; 2024-11-15 | — | [R53 DH](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/History.html) | DNS sharing across accounts | V |
| Accelerated recovery for public DNS changes | 2025-11-26 | DNS changes depend on us-east-1 → optional failover to us-west-2 with a 60-minute RTO | [What's New](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-route-53-accelerated-recovery-managing-public-dns-records) | Nuance on "Route 53 control plane is in us-east-1" | S |
| "Route 53 Resolver" renamed "VPC Resolver"; Global Resolver in preview | 2025-11 | Name change | R53 DH uses the new name | Name | V (date 3P) |
| CloudFront Origin Access Control (OAC) for Lambda function URLs (OAC preferred over OAI) | 2024-04-11 | OAI → OAC | [CloudFront DH](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/WhatsNew.html), [S3 origin page](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) | OAI is legacy | V |
| **CloudFront VPC origins** | 2024-11-20; cross-account sharing 2025-11-05 | Public ALB plus a secret header and prefix list → private ALB, NLB or EC2 origin | CloudFront DH | Best-answer change | V |
| Anycast static IPs; standard logging v2; gRPC | 2024-11-20 (apex domains 2025-04-04) | — | CloudFront DH | "Static IP" questions (CloudFront vs Global Accelerator) | V |
| Multi-tenant distributions (CloudFront SaaS Manager) | 2025-04-28 | One distribution per customer → tenants share a template distribution | CloudFront DH | SaaS designs | V |
| Flat-rate pricing plans (Free, Pro, Business, Premium); bundle CDN, WAF, DDoS protection, Route 53 and S3 credits with no overage charges | 2025-11-18 | Pay-as-you-go only → optional monthly flat plan | [Flat-rate plans](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/flat-rate-pricing-plan.html) | Cost answers (tier prices from 3P) | V |
| Viewer mutual TLS at CloudFront | 2025-11-24 | — | CloudFront DH | — | V |
| Global Accelerator | 2024-03-25 (cross-account bring-your-own-IP) | Otherwise no significant change | [GA DH](https://docs.aws.amazon.com/global-accelerator/latest/dg/WhatsNew.html) | Stable | V |

### Direct Connect, Site-to-Site VPN, Client VPN
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Direct Connect 400 Gbps dedicated connections | 2024-07-18 | 1/10/100 → adds 400 Gbps | [DX DH](https://docs.aws.amazon.com/directconnect/latest/UserGuide/AboutThisGuide.html) | Port speeds | V |
| Direct Connect inbound prefix controls | Date unknown | Hard limit of 100 prefixes per private/transit BGP session → 100 by default, can be allocated up to 1,000 | [DX quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) | Number | V (value only) |
| Direct Connect BGP route visibility; flat-rate billing | 2026-07-30; 2026-09-15 | — | DX DH | Cost | V |
| Site-to-Site VPN: pre-shared keys in Secrets Manager; IPv6 outer tunnel IPs; large-bandwidth tunnels; VPN Concentrators | 2025-05-27; 2025-07-01; **2025-09-25**; 2025-11-15 | 1.25 Gbps per tunnel → **up to 5 Gbps** for large tunnels on Transit Gateway or Cloud WAN. Standard tunnels still 1.25 Gbps; concentrator tunnels 100 Mbps | [VPN DH](https://docs.aws.amazon.com/vpn/latest/s2svpn/WhatsNew.html), [VPN quotas](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-limits.html) | Bandwidth numbers | V |
| Client VPN: higher quotas, IPv6, Transit Gateway attachment | 2024-12-19 / 2025-03-13; 2025-08-25; 2026-04-20 | Authorization rules 50 → 200; routes 10 → 100 | [Client VPN DH](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/WhatsNew.html) | Numbers | V |

### IAM, STS, IAM Identity Center
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Root-user MFA is mandatory | 2024-05 (management accounts); 2024-06 (standalone); 2025-06 (member accounts) | Optional → required for every account type; must register within 35 days | [Root MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2025/06/aws-iam-mfa-root-users-across-all-account-types) | Security baseline | V (dates S) |
| Central root access management for member accounts | 2024-11-14 | — → delete member-account root credentials and run privileged tasks centrally | [IAM DH](https://docs.aws.amazon.com/IAM/latest/UserGuide/document-history.html) | New answer for "remove root credentials across the organization" | V |
| Managed policies per role | 2026-08-19 | 10 default (max 20) → **20 default (max 25)** | [IAM quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iam-quota-increase/) | Number | V |
| Access Analyzer internal-access analyzers; required claim checks for shared OIDC providers | 2025-06-16; 2025-06-06 | — | IAM DH | Least-privilege and trust-policy questions | V |
| STS global endpoint answers in the caller's Region | Rolled out from early 2025 | Always served from us-east-1 → served locally in default-enabled Regions | [AWS Security blog](https://aws.amazon.com/blogs/security/announcing-upcoming-changes-to-the-aws-security-token-service-global-endpoint) | Resilience nuance | S |
| **IAM Identity Center multi-Region** | 2026-02-02 (expanded 07-28, 08-06, 09-30) | One home Region → replicate to additional Regions | [Identity Center DH](https://docs.aws.amazon.com/singlesignon/latest/userguide/doc-history.html) | Sign-in resilience answers | V |
| Identity Center: separate 7,000 quotas for accounts and apps; optional multi-account permissions; customer managed KMS keys; old AD Sync deprecated | 2026-06-22; 2026-08-04; 2025-09-17; 2025-04-17 | — | Identity Center DH | — | V |

### Organizations and Control Tower
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| **Resource control policies (RCPs)** | 2024-11-13 (more services 2026-01-23) | SCPs only → RCPs cap what resource policies can allow (S3, STS, KMS, SQS, Secrets Manager at launch) | [Org DH](https://docs.aws.amazon.com/organizations/latest/userguide/document-history.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2024/11/resource-control-policies-restrict-access-aws-resources) | Data-perimeter answers | V |
| Declarative policies | 2024-12-01 | — → enforce EC2/VPC/EBS settings (IMDS, serial console, Block Public Access, Allowed AMIs) | Org DH | Governance answers | V |
| **SCPs accept the full IAM policy language** | 2025-09-19 | Allow statements couldn't use Condition, resource ARNs or NotAction → all allowed, plus NotResource and wildcards anywhere | [SCP syntax](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies) | Memorized SCP limitations are wrong | V |
| **SCP quotas** | 2026-05-15 | 5 SCPs per root/OU/account and 5,120 characters → **10 and 10,240**. RCPs stay at 5 and 5,120 | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-organizations-increased-scp-quotas/), [Org quotas](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) | Numbers | V |
| Accounts per organization | 2024-08-14 | 5,000 → 10,000 without extra checks (quota page now says up to 50,000) | Org DH and quotas | Number | V |
| New policy types: chat apps, Security Hub, GuardDuty | 2024-09-26; 2025-06-17; 2026-09-25 | — | Org DH | Lists of policy types | V |
| Control Tower: controls built on RCPs and declarative policies; AWS Backup integration; automatic account enrollment | 2024-11 / 12; 2024-11-25; 2025-10-15 | — | [CT DH](https://docs.aws.amazon.com/controltower/latest/userguide/doc-history.html) | — | V |

### RDS, Aurora, Aurora DSQL
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| RDS Extended Support enrolls automatically and is billed | Charges from 2024-03-01 | Forced upgrade at end of standard support → paid Extended Support for up to 3 years unless you opt out | [Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) | Cost answers | V |
| Aurora Serverless v2 ceiling raised | 2024-10-03 | 128 → 256 ACU | [Aurora DH](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/WhatsNew.html) | Number | V |
| **Aurora Serverless v2 scales to zero** | 2024-11-20 | Minimum 0.5 ACU → 0 ACU (auto-pause) | Aurora DH, [How it works](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html) | No longer a reason to pick v1 | V |
| Aurora Serverless v1 end of life | 2025-03-31 | — | Aurora DH | Remove v1 answers | V |
| Aurora PostgreSQL Limitless Database GA | 2024-10-31 | — | Aurora DH | Horizontal write scaling | V |
| Global Database writer endpoint; **up to 10 secondary Regions** | 2024-10-22; 2025-05-21 | 5 → 10 secondaries | [Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-aurora-global-database-support-10-secondary-region-clusters/) | Number | V |
| Aurora storage | 2025-07 (needs Aurora PostgreSQL 17.5/16.9/15.13+ or Aurora MySQL 3.10+) | 128 TiB → 256 TiB | [Aurora quotas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html) | Number | V (date S) |
| **Aurora DSQL** | Preview 2024-12-03; GA 2025-05-27 | — → serverless distributed SQL, active-active across Regions with strong consistency | [DSQL DH](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/doc-history.html) | New best answer for multi-Region active-active relational databases | V |
| RDS for Oracle and SQL Server up to 256 TiB; magnetic storage deprecated | 2025-11-14; no restore to magnetic from 2026-07-01 | 64 TiB → 256 TiB (other engines stay at 64 TiB) | [RDS storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) | Numbers; drop "standard" storage | V |
| Performance Insights end of life → CloudWatch Database Insights | 2025-11-30 | — | [RDS DH](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/WhatsNew.html) | Monitoring answers | V |
| Zero-ETL to Redshift GA (RDS MySQL; Aurora PostgreSQL; RDS PostgreSQL and Oracle) | 2024-09-12; 2024-10-15; 2025-07-23 | Build an ETL pipeline → zero-ETL integration | RDS and Aurora DH | Analytics answers | V |
| RDS blue/green can change storage in the green environment | 2024-11-20 | — | RDS DH | — | V |

### DynamoDB, ElastiCache, Redshift
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Resource-based policies; on-demand maximum throughput | 2024-03-20; 2024-05-01 | — | [DynamoDB DH](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html) | Cross-account access; cost guardrail | V |
| **On-demand price cut of 50%; global tables up to 67%** | Effective 2024-11-01 | On-demand was the premium option → AWS calls it "the default and recommended throughput option for most workloads" | [Capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/capacity-mode.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-dynamo-db-reduces-prices-on-demand-throughput-global-tables) | Best answer flips toward on-demand | V |
| Warm throughput (pre-warming) | 2024-11-13 | — | DynamoDB DH | Launch-event answers | V |
| **Global tables with multi-Region strong consistency** | Preview 2024-12-03; GA 2025-06-30 | Last writer wins only → strong consistency across exactly 3 Regions (3 replicas, or 2 plus a witness), RPO 0 | [Global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html) | RPO-zero DR answers | V |
| Point-in-time recovery window configurable from 1 to 35 days; switch capacity modes 4 times per 24 h (was once) | 2025-01-07; 2025-08-12 | — | DynamoDB DH | Numbers | V |
| Global tables across accounts | 2026-02-03 | Same account only → multi-account | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/02/dynamodb-gt-multi-account/) | Account-isolation DR | V |
| ElastiCache: "Redis" is now "Redis OSS"; Valkey engine; Memcached auto-scaling; **public endpoints for Serverless** | 2024; 2024-10-08; 2025-04-10; 2026-09-29 | "ElastiCache is VPC-only" → Serverless for Valkey can be reached over the internet | [ElastiCache DH](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatsNew.html) | Engine choice; network answers | V (Valkey prices 3P) |
| Redshift secure defaults | After 2025-01-10 | New clusters: public access off, encryption on, SSL required | [What's New](https://aws.amazon.com/about-aws/whats-new/2025/01/amazon-redshift-default-security-configurations-new-warehouses) | Defaults | S |

### Lambda
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Faster scaling | 2023-11-26 | Account-wide burst of 500–3,000, then +500 per minute → each function adds 1,000 concurrent executions every 10 seconds | [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), [AWS blog](https://aws.amazon.com/blogs/aws/aws-lambda-functions-now-scale-12-times-faster-when-handling-high-volume-requests/) | Number | V |
| SnapStart for Python 3.12+ and .NET 8+ (container images 2026-07) | 2024-11-18 | Java only → Java, Python, .NET | [Lambda DH](https://docs.aws.amazon.com/lambda/latest/dg/lambda-releases.html) | Cold-start answers | V |
| Streamed responses | 2025-07-31 | 20 MB → **200 MB** | Lambda quotas | Number | V (date S) |
| **Asynchronous payload** | 2025-10-24 | 256 KB → **1 MB** | Lambda quotas, [What's New](https://aws.amazon.com/about-aws/whats-new/2025/10/aws-lambda-payload-size-256-kb-1-mb-invocations) | Number | V (date S) |
| Tenant isolation mode | 2025-11-19 | One function per tenant → a tenant ID routes requests to isolated execution environments | [What's New](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-tenant-isolation-mode) | SaaS designs | S |
| Lambda Managed Instances | 2025-11-30; 32 GB / 16 vCPU (2026-03); **90-minute timeout for async and event-source-mapping calls (2026-09-09)** | Synchronous calls keep the 15-minute limit | [Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-lambda-90-minute-function/) | "15 minutes is absolute" is no longer true | V |
| Durable functions | re:Invent, 2025-12 | Step Functions for long workflows → durable executions lasting up to 1 year | [Durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) | Workflow answers | V |
| Lambda MicroVMs | 2026-06-22 | — → isolated sandboxes that keep state for up to 8 hours | Lambda quotas | New compute option | V (date S) |
| Code storage | 2026-07-15 | 75 GB → **300 GB** per Region; code can also stay in your own S3 bucket | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/07/lambda-self-managed-code-storage/) | Number | V |
| Unchanged limits | — | 15 minutes (standard), 128–10,240 MB memory, `/tmp` up to 10,240 MB, 6 MB synchronous payload, 50 MB zipped / 250 MB unzipped, 5 layers, 10 GB container image | Lambda quotas | Still valid | V |

### API Gateway
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| **Integration timeout over 29 s** | 2024-06-04 | Hard 29 s → can be raised for Regional and private REST APIs (may lower your throttle quota). Edge-optimized REST and HTTP APIs (30 s) unchanged | [REST quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-execution-service-limits-table.html), [What's New](https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-api-gateway-integration-timeout-limit-29-seconds/) | Best-answer change | V |
| Private custom domain names; dual-stack; routing rules | 2024-11-21; 2025-03-28; 2025-06-03 | — | [API Gateway DH](https://docs.aws.amazon.com/apigateway/latest/developerguide/history.html) | — | V |
| **REST response streaming** | 2025-11-19 | 10 MB response and 29 s → stream for up to 15 minutes and past 10 MB (first 10 MB unthrottled, then 2 MB/s) | [Streaming](https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html) | GenAI and large-response answers | V |
| **Private integration directly to an ALB** | 2025-11-21 | REST VPC link required an NLB → VPC link v2 to an ALB or NLB | [Private integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html) | Drops the "NLB in front of ALB" pattern | V |
| REST vs HTTP API | Current | HTTP APIs still lack WAF, API keys and usage plans, caching, private and edge endpoints, and X-Ray. REST gained developer portals and streaming, so the gap grew | [Comparison](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html) | Feature choice | V |

### SQS, SNS, EventBridge, Step Functions
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| SQS `SendMessage` to a KMS-encrypted queue needs only `kms:GenerateDataKey` | 2024-07-24 | Also needed `kms:Decrypt` | [SQS release notes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-release-notes.html) | Permission questions | V |
| SQS fair queues | 2025-07-21 | — | SQS release notes | Noisy-neighbor answers | V |
| **SQS maximum message size** | 2025-08-04 | 256 KiB → **1 MiB** (the Extended Client is only needed above 1 MiB) | [SQS quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html) | Number | V (date S) |
| SQS FIFO high-throughput limits (current) | — | Up to 70,000 requests/s unbatched (700,000 messages/s batched) in us-east-1, us-west-2 and eu-west-1 | SQS quotas | Numbers | V |
| SNS FIFO throughput scope | 2025-01-21 | Topic-wide limit → can scope throughput per message group (300 msg/s per group; 3,000 msg/s or 20 MB/s per topic) | [SNS release notes](https://docs.aws.amazon.com/sns/latest/dg/sns-release-notes.html), [SNS quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html) | Numbers | V |
| **SNS 1 MiB messages (opt-in)** | 2026-09-18 | 256 KiB → up to 1 MiB with the `MaximumMessageSize` attribute; default stays 256 KiB; only SQS, Firehose and Lambda subscribers | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-sns-1mib-support/) | Number | V |
| EventBridge event size | 2026-01-29 | 256 KB → 1 MB | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-eventbridge-increases-event-payload-size-256-kb-1-mb) | Number | S |
| **EventBridge new Custom Event Bus** | 2026-09-24 | Rules-and-targets bus is now "Custom event bus – classic" → new bus with subscribers, retention (24 h, up to 1 year), ordering, RAM sharing, per-GB pricing | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/09/eventbridge-relaunches-custom-event-buses/), [Docs](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-what-is.html) | Event-bus designs | V |
| Step Functions variables and JSONata; EventBridge Pipes and Scheduler | 2024-11-22; no significant change found | — | [Step Functions DH](https://docs.aws.amazon.com/step-functions/latest/dg/document-history.html) | — | V |

### Kinesis, Firehose, MSK, Athena, Glue, Lake Formation
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Kinesis Data Firehose renamed Amazon Data Firehose; Apache Iceberg destination GA | 2024-02-09; 2024-09-30 | — | [Firehose DH](https://docs.aws.amazon.com/firehose/latest/dev/history.html) | Name | V |
| Kinesis Data Streams records up to 10 MiB | 2025-10-28 | 1 MiB hard limit → configurable up to 10 MiB (default still 1 MiB; 1 MB/s write per shard unchanged) | [Large records](https://docs.aws.amazon.com/streams/latest/dev/large-records.html) | Number | V (date S) |
| Kinesis Data Streams On-demand Advantage mode | 2025-11-04 | — → account-level mode with pre-warmed capacity and data prices at least 60% lower | [Capacity modes](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html) | Cost | V (date S) |
| **Kinesis Data Streams delivers directly to S3** | 2026-08-29 | Firehose was needed to land data in S3 → Data Streams can do it | [What's New](https://aws.amazon.com/about-aws/whats-new/2026/08/kinesis/data-delivery-general-purpose-s3-buckets/) | Data Streams vs Firehose answers | V |
| Kinesis Data Analytics for SQL fully shut down; Lake Formation Governed Tables shut down; Glue Ray jobs closed to new customers | 2026-01-27; 2024-12-31; announced 2026-03-31 | — | [Full Shutdown list](https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html) | Remove from answers | V |
| MSK Express brokers; Kafka 4.x (KRaft only) | 2025 | — | [MSK DH](https://docs.aws.amazon.com/msk/latest/developerguide/doc-history.html) | Low | V |
| Athena managed query results | 2025-06-02 | — | [Athena DH](https://docs.aws.amazon.com/athena/latest/ug/DocHistory.html) | Low | V |

### ECS, EKS, Fargate, ECR
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| ECS: EBS volume per task (including Fargate); Fargate Spot on Arm; VPC Lattice integration; predictive scaling | 2024-01-11; 2024-09-06; 2024-11-18; 2024-11-21 | — | [ECS DH](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html) | Storage and scaling | V |
| ECS native blue/green, then canary and linear deployments | 2025-07-15; 2025-10-28 | Needed CodeDeploy → built into ECS | ECS DH | Deployment answers | V |
| **ECS Managed Instances** | 2025-09-30 | Self-managed EC2 or Fargate → AWS-managed EC2 capacity | ECS DH | Changes the ECS-on-EC2 vs Fargate tradeoff | V |
| ECS Express Mode (AWS points App Runner users here) | 2025-11-21 | App Runner → ECS Express Mode | [What's New](https://aws.amazon.com/about-aws/whats-new/2025/11/announcing-amazon-ecs-express-mode/) | Simple container hosting | S |
| **EKS Auto Mode**; EKS Hybrid Nodes | 2024-12-01 | Managed node groups or self-run Karpenter → AWS manages compute, storage and networking | [EKS DH](https://docs.aws.amazon.com/eks/latest/userguide/doc-history.html) | "Least operational overhead with EKS" answer | V |
| EKS Pod Identity cross-account roles; EKS Capabilities (Argo CD, ACK, kro); warm pools for managed node groups | 2025-06-11; 2025-11-30; 2026-04-07 | — | EKS DH | — | V |
| ECR: pull-through cache from other ECR registries; image archive; managed signing; Clair basic scanning removed | 2025-03-12; 2025-11-19; 2025-11-21; 2026-02-02 | — | [ECR DH](https://docs.aws.amazon.com/AmazonECR/latest/userguide/doc-history.html) | — | V |

### KMS, ACM, CloudHSM, Secrets Manager
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| **KMS hardware validation level** | Current docs | "KMS is FIPS 140-2 Level 2" → KMS HSMs are **FIPS 140-3 Security Level 3** (certificate 4884) | [KMS overview](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) | Changes the KMS vs CloudHSM decision | V (date unverified) |
| **KMS rotation** | 2024-04-12 | Yearly only → custom period of 90–2,560 days (default 365) plus on-demand rotation (up to 25 per key). AWS managed keys still rotate yearly | [Key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html), [EnableKeyRotation API](https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKeyRotation.html) | Rotation questions | V |
| KMS on-demand rotation for imported key material (multi-Region keys too) | 2025-06-05; 2025-11-26 | — | [KMS DH](https://docs.aws.amazon.com/kms/latest/developerguide/dochistory.html) | Bring-your-own-key answers | V |
| **ACM exportable public certificates** | 2025-06-17 | Only usable on integrated services → exportable (paid) for EC2 and on-premises | [ACM DH](https://docs.aws.amazon.com/acm/latest/userguide/dochistory.html) | Best-answer change | V |
| **ACM public certificate lifetime** | 2026-02-18 | 13 months (395 days) → **198 days** | ACM DH | Number | V |
| ACM: ACME automation; certificate-transparency opt-out removed; HTTP validation for CloudFront | 2026-06-18; 2026-06-01; 2025-04-24 | — | ACM DH | — | V |
| CloudHSM; Secrets Manager | — | CloudHSM is FIPS 140-2 or 140-3 Level 3 depending on HSM type. No exam-relevant Secrets Manager change found | [CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) | — | V |

### WAF, Shield, Network Firewall, GuardDuty, Inspector, Macie, Security Hub
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| WAF Classic sunset | End of support 2026-10-07 | — → use AWS WAF (v2) | [Sunset list](https://docs.aws.amazon.com/general/latest/gr/sunset_services.html) | Remove Classic | V |
| Network Firewall: VPC endpoint associations; Transit Gateway attachment; managed active threat defense rules; URL and domain categories; forward-proxy mode | 2025-05-28; 2025-06-16; 2025-06-17; 2026-01-16; 2026-08-03 | — | [Network Firewall DH](https://docs.aws.amazon.com/network-firewall/latest/developerguide/document-history.html) | Centralized inspection answers | V |
| **GuardDuty Malware Protection for S3** | 2024-06-11 | Build it yourself with Lambda and antivirus → managed scanning of new uploads | [GuardDuty DH](https://docs.aws.amazon.com/guardduty/latest/ug/doc-history.html) | Best answer | V |
| GuardDuty Extended Threat Detection; malware scanning of AWS Backup; AI Protection | 2024-12-01; 2025-11-19; 2026-07-13 | — | GuardDuty DH | — | V |
| Inspector Classic fully shut down; Inspector VM Scanner | 2026-05-20; 2026-05-29 | Agent-based assessment templates are gone | [Inspector DH](https://docs.aws.amazon.com/inspector/latest/user/doc-history.html) | Remove Classic | V |
| Security Hub renamed "Security Hub CSPM"; new unified Security Hub GA; CSPM keeps archived findings 30 days (was 90) | 2025-06; 2025-12-02; 2025-06-20 | — | [Security Hub DH](https://docs.aws.amazon.com/securityhub/latest/userguide/doc-history.html) | Name and scope | V |
| Macie (VPC endpoints 2025-07-02); Shield | — | No exam-relevant change found | [Macie DH](https://docs.aws.amazon.com/macie/latest/user/doc-history.html) | — | V |

### Config, CloudWatch, CloudTrail, Systems Manager, CloudFormation, X-Ray
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| CloudTrail network activity events GA; CloudTrail Lake closed to new customers | 2025-02-13; 2026-05-31 | — | [CloudTrail DH](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-document-history.html) | Drop Lake answers | V |
| CloudWatch Logs centralization across accounts and Regions; Database Insights | 2025-09-17; 2024-12 / 2025-02 | — | [CloudWatch DH](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/DocumentHistory.html) | Central logging answers | V |
| Systems Manager: Incident Manager and Change Manager closed; Application Manager closed; **advanced-instances tier removed** | 2025-11-07; 2026-07-30; 2026-07-01 | 1,000 hybrid-node limit and paid tier → removed | [SSM DH](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-release-history.html) | Hybrid management | V |
| X-Ray SDKs and daemon: maintenance, then end of support | 2026-02-25; 2027-02-25 | X-Ray SDK → OpenTelemetry / AWS Distro for OpenTelemetry (the X-Ray service continues) | [X-Ray DH](https://docs.aws.amazon.com/xray/latest/devguide/document-history.html) | Instrumentation answer | V |
| CloudFormation IaC generator; stack refactoring; AWS Config | 2024-02-02; 2025-02-06; none for Config | — | [CloudFormation DH](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/doc-history.html) | Low | V |

### Backup, Storage Gateway, DataSync, Snow, Transfer Family, DMS, Application Migration Service
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| **Logically air-gapped backup vault** GA; FSx support; multi-party approval; customer managed KMS keys; usable as the primary backup target | 2024-08-07; 2025-03-12; 2025-06-17; 2025-11-06; 2025-11-17 | — | [Backup DH](https://docs.aws.amazon.com/aws-backup/latest/devguide/doc-history.html) | Ransomware-resilient backup answer | V |
| AWS Backup: Redshift Serverless; DSQL; EKS; S3 backup tiering; more than 1,000 S3 buckets | 2025-03-31; 2025-05-27; 2025-11-10; 2025-11-18; 2026-09-01 | — | Backup DH | Coverage lists | V |
| DataSync Enhanced mode (S3 first, more location types in 2026); dropped Snowball Edge; Discovery removed | 2024-10-30 / 2026-07-28; 2024-11-12; 2025-05-20 | — | [DataSync DH](https://docs.aws.amazon.com/datasync/latest/userguide/doc-history.html) | Transfer answers | V |
| AWS Data Transfer Terminal (physical upload sites) | 2024-12 | — → AWS's named alternative for offline transfer | [Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html) | Replaces Snow in answers | V (date S) |
| Transfer Family web apps; web apps hosted in a VPC | 2024-12-01; 2025-11-19 | — | [Transfer DH](https://docs.aws.amazon.com/transfer/latest/userguide/doc-history.html) | Browser access to S3 | V |
| Application Migration Service: FSx for ONTAP as a target (GA) | 2026-08-30 | — | [MGN DH](https://docs.aws.amazon.com/mgn/latest/ug/doc-history.html) | Low | V |

### Cost tools and Free Tier
| Change | Date | Old → New | Source | Why it matters | Status |
|---|---|---|---|---|---|
| Savings Plans can be returned (commitment ≤ $100/hour, within 7 days, same month); Purchase Analyzer | 2024-03-20; 2024-11-21 | Non-cancellable → limited return window | [Savings Plans DH](https://docs.aws.amazon.com/savingsplans/latest/userguide/doc-history.html) | — | V |
| **Database Savings Plans** | re:Invent 2025 (2025-12) | Reserved Instances only for databases → up to 35% off across Aurora, RDS, DynamoDB, ElastiCache, DocumentDB, Neptune, Keyspaces, Timestream, DMS and OpenSearch | [Plan types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html) | Cost best answer | V |
| **Free Tier redesigned for new accounts** | 2025-07-15 | 12-month free tier → $100 credit plus up to $100 more. "Free plan" lasts up to 6 months, then the account closes (90 days to upgrade). "Paid plan" also available | [Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier.html), [Plans](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html) | Changes your book's lab setup instructions | V (date S) |
| Budgets and Cost Explorer | — | Not researched in depth | — | — | — |

---

## 2. Renamed services
| Old name | Current name | Date | Status |
|---|---|---|---|
| Amazon Kinesis Data Firehose | Amazon Data Firehose | 2024-02-09 | V |
| Amazon Kinesis Data Analytics (Flink) | Amazon Managed Service for Apache Flink (the SQL flavor was shut down 2026-01-27) | 2023-08-30 | 3P (copy of AWS blog) |
| Amazon QuickSight | Amazon Quick Suite (2025-10-09), then **Amazon Quick**; the BI part is called "Amazon Quick Sight" | 2025–2026 | V for current name (docs and exam guide); dates S/3P |
| Amazon SageMaker (the ML service) | **Amazon SageMaker AI**; "Amazon SageMaker" now means the combined data and AI platform | 2024-12 | V for name; date 3P |
| AWS Single Sign-On | AWS IAM Identity Center | 2022-07 (before the window) | Not re-checked |
| Amazon Elasticsearch Service | Amazon OpenSearch Service; no newer rename found | 2021 | Not re-checked |
| AWS Security Hub (original) | AWS Security Hub CSPM; a new unified "AWS Security Hub" went GA 2025-12-02 | 2025-06 | V |
| Route 53 Resolver | Route 53 VPC Resolver (a separate Global Resolver is in preview) | 2025-11 | V for name; date 3P |
| Amazon S3 Glacier (the original vault service) | Amazon Glacier (closed to new customers) | 2025 | V |
| ElastiCache for Redis | ElastiCache for Redis OSS (Valkey added 2024-10-08) | 2024 | V for name |
| Aurora Serverless v2 | "Aurora Serverless" in the docs (v1 retired 2025-03-31) | 2025 | V |
| EC2 Global View | AWS Global View | 2026-06-30 | V |
| EventBridge custom event bus | "Custom event bus – classic"; the new bus is the "Custom Event Bus" | 2026-09-24 | V |
| Route 53 Application Recovery Controller | Amazon Application Recovery Controller (ARC) | Date unverified | V for name |
| Performance Insights | CloudWatch Database Insights | 2024-12 to 2025-11 | V |
| Pinpoint SMS and voice | AWS End User Messaging (Pinpoint itself ends 2026-10-30) | 2024 | V |
| AWS Application Composer | AWS Infrastructure Composer (now itself being retired) | Date unverified | Partial |

## 3. Closed to new customers, retired, or end of support (SAA scope or close to it)
| Service / feature | Status and dates | AWS-recommended replacement | Status |
|---|---|---|---|
| **Amazon Elastic Transcoder** | Fully shut down 2025-11-13. **Still listed as in scope in the SAA-C03 exam guide** | AWS Elemental MediaConvert ([migration blog](https://aws.amazon.com/blogs/media/migrating-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/)) | V |
| AWS Snowmobile | Fully shut down 2024-03-14 | — | V |
| Snowcone, plus older Snowball Edge models (80 TB storage-optimized, 52 vCPU compute-optimized, GPU) | Ordering stopped 2024-11-12; support ended 2025-11-12 | Current Snowball Edge, for existing customers only ([Storage blog](https://aws.amazon.com/blogs/storage/aws-snow-device-updates)) | V |
| **AWS Snowball Edge** (all current models) | Closed to new customers 2025-11-07. AWS says it "will no longer offer any AWS Snow Family devices for new customers" | DataSync (optionally over a Direct Connect hosted connection), Data Transfer Terminal, partner devices; Outposts for edge compute ([page](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)) | V |
| Amazon FSx File Gateway | Closed 2024-10-28 | FSx for Windows File Server accessed directly | V |
| Amazon Glacier vault API | Closed 2025-12-15 | S3 Glacier storage classes | V (date 3P) |
| S3 Select and S3 Glacier Select | Closed 2024-07-25 | AWS blog "How to optimize querying your data in Amazon S3" (Athena etc.) | V (replacement not opened) |
| S3 Object Lambda | Closed 2025-11-07 | Lambda behind CloudFront, API Gateway or a function URL | V |
| AWS Data Pipeline | Closed 2024-07-25 ([docs](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html)) | Glue, Step Functions, Managed Workflows for Apache Airflow | V (replacements S) |
| AWS OpsWorks (all variants) | Fully shut down 2024-05 | Not re-checked | V |
| Amazon QLDB | Fully shut down 2025-07-31 | Not re-checked | V |
| AWS App Mesh | End of support 2026-09-30 (already passed) | ECS Service Connect | V |
| AWS Cloud9 / Amazon CloudSearch / Amazon Forecast | Closed 2024-07-25 / 2024-07-25 / 2024-07-29 | IDE toolkits or CloudShell / OpenSearch Service / SageMaker Canvas | V |
| AWS CodeCommit (out of SAA scope) | Closed mid-2024, **reopened to new customers 2025-11-24**; no longer on the Maintenance list | — | 3P (plus V: not on list) |
| Amazon Fraud Detector | Closed 2025-11-07 | SageMaker AI / AutoGluon; AWS WAF Fraud Control | V |
| Timestream for LiveAnalytics | Closed 2025-06-20 | Timestream for InfluxDB | V |
| Kinesis Data Analytics for SQL | Fully shut down 2026-01-27 | Managed Service for Apache Flink | V |
| Amazon Inspector Classic | Fully shut down 2026-05-20 | Amazon Inspector | V |
| AWS WAF Classic | End of support 2026-10-07 (per-Region dates in the Health Dashboard) | AWS WAF | V |
| **Directory Service Simple AD** | Announced 2026-06-30; new customers can't onboard | AWS Managed Microsoft AD, AD Connector ([page](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple-ad-availability-change.html)) | V |
| Amazon Cognito Sync | Announced 2026-06-30 | AppSync, DynamoDB | V |
| CloudTrail Lake; Systems Manager Incident Manager and Change Manager; Application Manager | Closed 2026-05-31; 2025-11-07; 2026-07-30 | Not checked | V |
| Migration Hub; Application Discovery Service | Closed 2025-11-07 | AWS Transform | V |
| DMS Fleet Advisor | Fully shut down 2026-05-20 | — | V |
| AWS App Runner | Announced 2026-03-31; closed 2026-04-30 | ECS Express Mode | V (closure date and replacement 3P) |
| Amazon Kendra (no longer on the SAA in-scope list) | Closed 2026-07-30 | Bedrock Knowledge Bases | V |
| Aurora Serverless v1; RDS magnetic storage; Performance Insights console | End of life 2025-03-31; no restore to magnetic from 2026-07-01; 2025-11-30 | Aurora Serverless (v2); gp3 or io2; CloudWatch Database Insights | V |
| RDS Custom for Oracle | End of support 2027-03-31 | — | V |
| EC2 launch configurations; Amazon Linux 2; X-Ray SDKs | Blocked for new accounts 2024-10-01; end of support 2026-06-30; end of support 2027-02-25 | Launch templates; AL2023; OpenTelemetry | V |
| SNS message data protection; ARC readiness check; Glue Ray jobs | Closed 2026-04-30; 2026-03-31 batch | — | V |
| Out of SAA scope but on the lists | Pinpoint (end 2026-10-30), Proton (end 2026-10-07), DevOps Guru (sunset), WorkDocs, MediaStore and CodeStar (fully shut down) | — | V |

## 4. Top 15 facts older prep material gets wrong
1. **"S3 objects max out at 5 TB" and "100 buckets per account."** Now 50 TB via multipart upload (a single PUT is still 5 GB) and 10,000 buckets by default.
2. **"gp3 maxes at 16 TiB, 16,000 IOPS and 1,000 MiB/s."** Now 64 TiB, 80,000 IOPS and 2,000 MiB/s. Every io2 volume is now Block Express with up to 256,000 IOPS. The 6-hour wait between EBS volume changes is gone (now up to 4 per 24 hours).
3. **"Messages and events are capped at 256 KB."** SQS is now 1 MiB, Lambda async 1 MB and EventBridge 1 MB. SNS goes to 1 MiB if you opt in. Kinesis records can be up to 10 MiB if you opt in.
4. **"API Gateway's 29-second timeout is a hard limit."** It can be raised for Regional and private REST APIs, and REST response streaming runs up to 15 minutes. REST private integrations can now target an ALB.
5. **SCP facts.** 5 per node and 5,120 characters became 10 and 10,240. Allow statements now accept conditions and resource ARNs. Teach RCPs and declarative policies alongside SCPs.
6. **"KMS is FIPS 140-2 Level 2, so use CloudHSM when you need Level 3."** KMS is now FIPS 140-3 Level 3. KMS rotation is configurable (90–2,560 days) and can be triggered on demand.
7. **Aurora.** v2 now scales to 0 ACU and up to 256 ACU, and v1 is retired. Storage went from 128 to 256 TiB. Global Database went from 5 to 10 secondary Regions.
8. **"DynamoDB provisioned mode is cheaper; use on-demand only for spiky traffic."** On-demand is now AWS's default and recommended mode. Global tables can be strongly consistent across Regions (RPO 0) and can span accounts.
9. **Snow Family answers.** Snowmobile and Snowcone are retired, and Snowball Edge is closed to new customers. Default to DataSync (plus Direct Connect) or Data Transfer Terminal.
10. **"Highly available NAT needs one NAT gateway per AZ in public subnets."** A Regional NAT gateway (from 2025-11-19) needs no public subnet and spans AZs on its own.
11. **"An attached Elastic IP or public IP is free."** Every public IPv4 address has been billed since 2024-02-01.
12. **"Free Tier means 12 months of 750 hours on t2/t3.micro."** Accounts created since 2025-07-15 get credits instead, and the Free plan lasts at most 6 months.
13. **"Interface endpoints only reach services in the same Region."** PrivateLink went cross-Region for endpoint services (2024) and some AWS services (2025).
14. **"ACM certificates last 13 months and can't be exported for EC2."** Validity is now 198 days, and public certificates can be exported.
15. **Retired services still shown as answers:** Elastic Transcoder, S3 Select, Data Pipeline, Inspector Classic, Kinesis Data Analytics for SQL, OpsWorks, CloudSearch, launch configurations, Aurora Serverless v1, Simple AD (for new customers).

Close behind:
- Lambda code storage 75 GB → 300 GB.
- IAM managed policies per role 10 → 20.
- CloudFront VPC origins replace the "public ALB plus secret header" trick.
- LCU reservation replaces asking Support to pre-warm an ALB.
- S3 turned SSE-C off by default.
- Kinesis Data Streams can write straight to S3.
- Root-user MFA is mandatory.
- Identity Center can be multi-Region.
- S3 Files muddies "S3 vs EFS".
- Site-to-Site VPN large tunnels reach 5 Gbps.
- Transit Gateway allows 100 Gbps per VPC attachment.

## 5. What I could not verify
- **Missing change dates:** Transit Gateway's move from 50 to 100 Gbps per attachment; Direct Connect prefix controls; when KMS reached FIPS 140-3 Level 3 (AWS says it reached 140-2 Level 3 in May 2023); the exact 2026 date "Quick Suite" became "Quick"; the exact dates of the SageMaker AI and VPC Resolver renames; the Redis OSS rename.
- **Dates or facts from search summaries or third parties only:**
  - S3 Files launch (2026-04-07) and Glacier vault closure (2025-12-15).
  - App Runner closure (2026-04-30) and ECS Express Mode as its official replacement.
  - EventBridge 1 MB (2026-01-29), Lambda tenant isolation, Lambda MicroVMs launch date.
  - Route 53 accelerated recovery, STS global endpoint change, Redshift secure defaults.
  - Valkey price discounts, CloudFront flat-rate tier prices.
  - Database Savings Plans terms (1-year, no upfront).
  - Root-MFA phase dates, IMDSv2-only new instance types (mid-2024).
- **Seen only as aws.amazon.com links in search results, not opened:** Lambda full IAM resource-based policies (2026-08), Lambda AZ metadata (2026-03), Lambda Managed Instances at 32 GB (2026-03), SnapStart for container images (2026-07), DynamoDB strong-consistency Region expansion (2026-09), RDS Multi-AZ ENA Express (2026-05).
- **Replacements not re-checked:** OpsWorks, QLDB, CloudTrail Lake, Systems Manager Incident/Change/Application Manager, DMS Fleet Advisor, Lake Formation Governed Tables.
- **Not researched in depth:** AWS Budgets and Cost Explorer; DocumentDB, Neptune and Keyspaces; Amazon MQ, AppFlow, EMR, OpenSearch; Cognito user-pool feature plans; Outposts, Wavelength, Batch, Elastic Beanstalk; Shield Advanced details.
- **Not knowable from the docs:** whether exam items have been updated to reflect any of these changes.

Note: the claude.ai Excalidraw, Gmail, Google Calendar and Google Drive connectors need to be authorized in your claude.ai connector settings before they can be used. They weren't needed for this research.
