# SAA-C03 prep book: verified research (checked 2026-10-04)

Everything below was fetched live today, and every fact has its source URL. Anything from a non-AWS site is marked **[third-party]**. I wrote no files; all curl output went to stdout.

## Five findings that change the book plan

1. **SAA-C03 is still the current exam.** The official September 2026 update post lists only three exams changing: MLA-C02, SAP-C03 and DVA-C03. SAA is not among them. Third-party sites (citadelcloudmanagement.com, spoto.net) claim an "SAA-C04" was released in March 2024. That is contradicted by every official page, which still links the SAA-C03 guide.
   - https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/
   - https://aws.amazon.com/certification/certified-solutions-architect-associate/
2. **Snowball reaches end of support on December 31, 2026** in all commercial Regions. "AWS Snow Family" is still in the SAA-C03 in-scope services list.
   - https://aws.amazon.com/snowball/
   - https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.md
3. **The Amazon Builders' Library is moving to AWS Builder Center** (builder.aws.com). Most article URLs now redirect to pages that build their content in the browser with JavaScript. Raw HTML has no article text, and WebFetch returned nothing. The legacy PDFs still work (details in Part 3).
4. **The Aurora FAQ has moved into the docs.** https://aws.amazon.com/rds/aurora/faqs/ now redirects to a new docs guide, "Aurora Extended Content", which has its own `llms.txt` and `full.md`.
5. **Several prep sites have moved:**
   - workshops.aws redirects to builder.aws.com/build/workshops (JavaScript-only page).
   - The Cloud Quest, Builder Labs and Escape Room pages redirect to aws.amazon.com/training/digital/immersive-learning/.
   - Decision guides now live under one path: `/decision-guides/latest/decision-guides/`.
   - AWS Cloud Quest v2.0 launched on August 11, 2026.

---

## Part 1: Exam policies and logistics

### 1. ESL +30 (still offered in 2026)

Official wording, verbatim from https://aws.amazon.com/certification/policies/before-testing/ (page © 2026):

> "A 30-minute exam extension is available upon request to non-native English speakers when taking an exam in English. The accommodation, "ESL +30," only needs to be requested once, prior to registering for an exam. It will apply to all future exam registrations with all test delivery providers. To request this accommodation, follow these steps: Sign in to aws.training/Certification. Select the Go to your Account button. Select the Request Exam Accommodations button, followed by Request Accommodation. Using the Accommodation Type dropdown, select ESL +30 MINUTES. Select the Create button."

The FAQ says the same thing in shorter form: "Take the written exam in English and request an ESL accommodation for an additional 30-minutes to complete the exam." (https://aws.amazon.com/certification/faqs/)

- **When to request it:** before registering, meaning before scheduling. The official text does not say what happens if an exam is already booked.
  - A 2018 LinkedIn post from the PSI era says you must cancel first and that approval is automatic **[third-party, dated]**: https://www.linkedin.com/pulse/30-minute-extension-your-aws-certification-exam-garcia-lozano
  - Since the reader has not booked yet: request ESL +30 first, then schedule.
- **Per exam or permanent:** permanent on the account ("all future exam registrations").
  - Contrast: disability accommodations "must be requested prior to scheduling each exam" and are arranged directly with Pearson VUE. Same page.
- **Online vs test centre:** the official wording is "all test delivery providers". Pearson VUE is the only provider and runs both online and test-centre delivery. There is no separate explicit statement about online proctoring (OnVUE), so this is my inference.
- **Practical effect:** SAA-C03 goes from 130 to 160 minutes.

### 2. Exam facts and policies

| Item | Fact | Source |
|---|---|---|
| Format | 65 questions (50 scored + 15 unscored, not identified), multiple choice or multiple response, 130 minutes | https://aws.amazon.com/certification/certified-solutions-architect-associate/ ; https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.md |
| Scoring | Scaled 100–1,000, pass is 720. Compensatory: you only need to pass overall. No penalty for guessing. | exam guide (above) |
| Domains | Secure 30%, Resilient 26%, High-Performing 24%, Cost-Optimized 20% | exam guide |
| Price | 150 USD. Prices are updated at least annually in May for exchange rates. | https://aws.amazon.com/certification/policies/before-testing/ |
| Languages | English, French, Italian, Japanese, Korean, Portuguese (BR), Spanish (LatAm), Spanish (Spain), Simplified Chinese, Traditional Chinese. Italian retires after Dec 31, 2026. | SAA page |
| Delivery | Pearson VUE only. Test centre or online. Online proctoring is available for all exams. English proctors are available 24x7, and you must be able to communicate with the proctor. | before-testing |
| Online rules | You may not leave the camera view for any reason, including restroom breaks. | https://aws.amazon.com/certification/policies/during-testing/ |
| Online setup | Check in 30 minutes early. Pass the system test on the same device and network. Single monitor; 6 Mbps down / 2 Mbps up. | https://www.pearsonvue.com/us/en/aws/onvue.html (delivery-provider page) |
| Test-centre breaks | Unscheduled breaks are allowed but the exam timer keeps running. You may not leave the building. | during-testing |
| ID | Test centre: two primary IDs, or one primary plus one secondary. Online: one primary ID. Primary means original, unexpired, government-issued, name in Roman characters, photo and signature. | during-testing |
| Name changes | Allowed until 2 business days (48 hours) before your first exam | during-testing |
| Reschedule / cancel | Up to 24 hours before. Each appointment can be rescheduled at most twice. Within 24 hours there are no changes or refunds. A no-show forfeits the fee. Illness or emergency fees can be waived with documentation via Pearson VUE. | before-testing |
| Payment | Visa, AmEx, Mastercard, JCB, or voucher. Voucher expiry dates cannot be extended. | before-testing |
| Account | The AWS Certification Account (sign in at aws.training/Certification with an AWS Builder ID) is separate from an AWS account | before-testing |
| Results | "within five business days". The Credly badge email may arrive first, and most exams show no pass/fail on screen. | https://aws.amazon.com/certification/policies/after-testing/ ; FAQ |
| Retake | "wait 14 calendar days … no limit on exam attempts", full fee each time. After passing, you cannot retake the same exam for 2 years unless a new version is released. | after-testing |
| Validity | 3 years. Renew by passing the latest SAA, by passing SAP, or "maintain" for 1 more year via a Skill Builder subscription. | SAA page; https://aws.amazon.com/certification/recertification/ |
| Voucher after passing | "Get access to a 50% discount voucher to apply toward recertification or any other exam". It is in the Benefits section of the Certification Account. | https://aws.amazon.com/certification/benefits/ ; FAQ |
| UI practice | The "AWS Exam Demo" tool is on the AWS page at Pearson VUE. It covers the English-toggle and flag-for-review features. | before-testing |

### 3. AWS Service Names page

- **URL confirmed:** https://aws.amazon.com/certification/policies/general-information/ (the SAA page links to the `#AWS_Service_Names` anchor). The exam guide's page "Mentions of AWS Services on the Exam" links to it: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-service-mentions.md
- **Contents:** 24 short-name to full-name pairs. Examples: AWS CDK, AWS CLI, AWS DMS, Amazon DocumentDB, Amazon EBS/EC2/ECR/ECS/EFS/EKS, IAM, Amazon Keyspaces, AWS KMS, AWS Managed Microsoft AD, AWS Private CA, Amazon RDS, Amazon S3, AWS SAM, AWS SCT, Amazon SES, Amazon SNS, Amazon SQS, AWS STS, Amazon VPC.
- **How it works on exam day** (exam guide page):
  - The in-exam Help button shows the list.
  - Listed services that are out of scope will not appear.
  - Some abbreviations are never expanded (for example API Gateway, EMR).
- **Other sections on the same page:**
  - Exam development: every question is first used as an unscored beta question.
  - Certification verification: Credly badge, and a 16-digit validation number checked at aws.amazon.com/verification.

---

## Part 2: Official prep resources (names as of 2026)

Skill Builder subscription: **$29/month**, Individual annual **$449/year**, Team $449/year (https://aws.amazon.com/training/digital/). The $299/year figure in the 2022 launch blog is out of date.

The Skill Builder site builds its pages in the browser with JavaScript, so curl and WebFetch cannot read them. Item details from it are marked accordingly.

| Resource | URL | Cost | Size | 3-week priority |
|---|---|---|---|---|
| Exam guide (HTML / .md / full.md 36KB) | https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html | Free | — | **Essential** |
| 4-step Exam Prep Plan | https://skillbuilder.aws/category/exam-prep/solutions-architect-associate-SAA-C03 (linked from the SAA page) | Free plan; some items need a subscription | Steps: know the exam → refresh → review/practice → assess. Search-index summaries **[unverified]**: plan 18h25m, "~1 month at 3 hrs/week", AWS Solutions Architect Learning Plan 66h45m | Use steps 1, 3, 4 |
| Official Practice Question Set | via the plan | Free | 20 questions with feedback (https://aws.amazon.com/certification/certification-prep/) | **Day 1 diagnostic** |
| Official Practice Exam | via the plan | Subscription | Same style and rigor, scaled pass/fail result. Search snippet: SAA-C03 version is 2h10m **[unverified]** | **Essential, ~5–7 days before the exam** |
| Official Pretest | Product family confirmed (Feb 2024 blog: "official, full-length pretest" for DEA-C01, CLF-C02) https://aws.amazon.com/blogs/training-and-certification/feb-2024-new-offerings/ | Free (for those exams) | Full length | **Could not confirm one exists for SAA-C03** |
| Exam Prep Standard Course | via the plan | Free | Official page says "2-hour" generically; Class Central says 4.5 h for SAA-C03 **[third-party]** | Domain refresh |
| Exam Prep Enhanced Course | via the plan | Subscription | "6–8 hours … videos, hands-on labs, additional practice questions, and access to the Official Practice Exam" (certification-prep page) | High |
| AWS Escape Room: Exam Prep for SAA-C03 | Launched July 2025: https://aws.amazon.com/blogs/training-and-certification/july-2025-new-offerings/ | Subscription | "100+ exam-style questions, plus hands-on labs" (https://aws.amazon.com/training/digital/immersive-learning/). Search snippet: 2–3 hours | High (extra questions) |
| AWS Cloud Quest: Solutions Architect | https://docs.cloudquest.skillbuilder.aws/coming-soon/index.html | Subscription. Only the Cloud Practitioner and Generative AI Practitioner roles are free. | 27 assignments; v2.0 launched Aug 11, 2026; lab replay is now free for everyone | Low (too long for 3 weeks) |
| AWS Builder Labs | immersive-learning page | Subscription | "over 200 guided" labs, with a Learning Assistant | Selective, weak domains only |
| Sample questions PDF | https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Sample-Questions.pdf | Free | **Still live** (HTTP 200). 5 pages, 10 SAA-C03 questions with answers, © 2022. No longer linked from the SAA page. | Quick warm-up |
| Ramp-Up Guide: Solutions Architect | New canonical: https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/training/approved/pdfs/ramp-up-guides/Ramp-Up_Guide_Architect.pdf (index: https://aws.amazon.com/training/ramp-up-guides/). Old `/training-and-certification/ramp-up_guides/` URL also returns 200. | Free (some items $) | © October 2024 | Low (it is a catalogue) |
| Well-Architected Labs | https://www.wellarchitectedlabs.com/ (still the "hands-on labs" link on https://aws.amazon.com/architecture/well-architected/) | Free | Site is now slimmed: Dashbird 100 lab, Cost-Optimizations, CUR Query Library, CFM TIPs, Cloud Intelligence Dashboards. Pillar workshop at https://catalog.workshops.aws/well-architected-reliability/en-US returns 200 (JavaScript-only, content unverified). | Low |
| AWS Workshops | https://workshops.aws/ now redirects to https://builder.aws.com/build/workshops (JavaScript-only) | Free | — | Low |
| Exam Readiness webinars, AWS Training Live on Twitch | https://aws.amazon.com/training/events/ | Free | Live | Optional |

The old exam guide PDF (Version 1.1, Sept 2023) is still live at `…/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf`. Use the docs HTML as canonical.

**Most useful in 3 weeks:**
1. Exam guide and the service-names list.
2. Free Practice Question Set as a baseline.
3. One month of Individual ($29), covering the Enhanced Course domain reviews, Escape Room SAA, and the Official Practice Exam taken 5–7 days before the exam.
4. Sample PDF as a warm-up.

Timing: 65 questions in 130 min is 2.0 min per question; with ESL +30 it is about 2.5 min.

---

## Part 3: Canonical grounding documents

"HTML" and "MD" columns show HTTP status for the `.html` page and its `.md` twin.

| Document | Canonical URL | HTML | MD | Published |
|---|---|---|---|---|
| DR of Workloads on AWS (landing) | https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html | 200 | 200 (1KB, abstract only) | Feb 12, 2021 |
| DR: the four strategies | …/disaster-recovery-options-in-the-cloud.html (Backup and restore, Pilot light, Warm standby, Multi-site active/active) | 200 | 200 (35KB) | full.md 71KB |
| WA Framework | https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html ; six pillars: …/the-pillars-of-the-framework.html | 200 | 200 | Nov 6, 2024 |
| Reliability pillar | https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html | 200 | 200 | Nov 6, 2024 (full.md 665KB) |
| Security pillar | https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html | 200 | 200 | Nov 6, 2024 |
| Cost Optimization pillar | https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html | 200 | 200 | Jun 27, 2024 |
| Performance Efficiency pillar | https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html | 200 | 200 | Nov 6, 2024 |
| (OpEx, Sustainability) | …/operational-excellence-pillar/welcome.html ; …/sustainability-pillar/sustainability-pillar.html | 200 | 200 | — |
| AWS Fault Isolation Boundaries | https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html | 200 | 200 | Nov 16, 2022 |
| VPC Connectivity Options | https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html | 200 | 200 | (date not on page) |
| Multi-VPC network infrastructure | https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html | 200 | 200 | Apr 17, 2024 |
| Hybrid Connectivity | https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html | 200 | 200 | Jul 6, 2023 |
| Organizing Your AWS Environment | https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html | 200 | 200 | Apr 30, 2025 |
| AWS Security Reference Architecture | https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html (welcome.html is only a redirect stub; welcome.md returns 404) | 200 | 200 | llms.txt 200 |
| Overview of AWS | https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html | 200 | 200 | **Jun 2, 2026** |
| 7 Rs migration strategies | https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html (Retire, Retain, Rehost, Relocate, Repurchase, Replatform, Refactor or re-architect) | 200 | 200 | — |

**Decision guides.** https://aws.amazon.com/getting-started/decision-guides/ redirects to https://docs.aws.amazon.com/decision-guides/. All of the following return 200 for both `.html` and `.md`, under `https://docs.aws.amazon.com/decision-guides/latest/decision-guides/`:
- choosing-aws-storage-service
- databases-on-aws-how-to-choose
- choosing-aws-compute-service
- choosing-aws-container-service
- application-integration-on-aws-how-to-choose
- sns-or-sqs-or-eventbridge
- ec2-purchasing-options-aws-how-to-choose
- choosing-networking-and-content-delivery-service
- migration-on-aws-how-to-choose
- fargate-or-lambda
- choosing-aws-serverless-service
- identity-on-aws-how-to-choose
- choosing-aws-security-services
- waf-or-shield
- analytics, cost-management, monitoring, cloudtrail-or-cloudwatch

There is also an `llms.txt` (7.9KB).

**Builders' Library.** The index https://aws.amazon.com/builders-library/ redirects to https://builder.aws.com/learn/topics/builders-library, which builds its content with JavaScript.

| Topic | Article | Where it lives now | PDF fallback (`https://d1.awsstatic.com/builderslibrary/pdfs/<slug>.pdf`) |
|---|---|---|---|
| Timeouts / retries / backoff | Timeouts, retries, and backoff with jitter | builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/… (redirect) | 200 |
| Safe retries | Making retries safe with idempotent APIs (Malcolm Featonby) | aws.amazon.com, text in raw HTML | 403 |
| Static stability | Static stability using Availability Zones | aws.amazon.com, text in raw HTML | 200 |
| Avoiding fallback | Avoiding fallback in distributed systems | builder.aws.com/content/3EuS9Sakq7L3VLQIF3qzfMfke1Y/… | 200 |
| Shuffle sharding | Workload isolation using shuffle-sharding | builder.aws.com/content/3F06NpJ8YeoIGP8VHTw4n81pFn8/… | 200 |
| Also useful | Avoiding insurmountable queue backlogs; Using load shedding to avoid overload; Implementing health checks | builder.aws.com | 200 |
| Also useful | Caching challenges and strategies | aws.amazon.com | 200 |
| Also useful | Reliability, constant work, and a good cup of coffee | builder.aws.com | 403 |

**Shared Responsibility Model.** https://aws.amazon.com/compliance/shared-responsibility-model/ (200) defines "Security of the Cloud" versus "Security in the Cloud". It uses EC2 (IaaS: customer patches the guest OS and configures security groups) versus S3/DynamoDB (abstracted services: customer manages data, encryption options and IAM).

**Global Infrastructure.** https://aws.amazon.com/about-aws/global-infrastructure/ (also /regions_az/):
- "The AWS Cloud spans 124 Availability Zones within 39 Geographic Regions, with announced plans for 7 more Availability Zones and 2 more AWS Regions in the Kingdom of Saudi Arabia, and Chile."
- Tiles: 39 Regions; 124 AZs; 750+ CloudFront PoPs and 15 Regional edge caches; 46 Local Zones and 33 Wavelength Zones.
- North America: 31 AZs, 9 Regions, 31 Edge Network Locations, 3 Edge Cache Locations.
- **The page states no "as of" date.** Cite it as "retrieved 2026-10-04".

---

## Part 4: Real customer examples (all official AWS sources)

| Service | Company | What they did and the concept it shows | Numbers (from source) | URL |
|---|---|---|---|---|
| S3 | Snap | Moved S3 Standard-IA to Glacier Instant Retrieval: choosing a storage class by access pattern | >2 EB (~1.5 trillion files); "tens of millions of dollars" saved; 20–30% lower latency in some Regions; 99.99% availability | https://aws.amazon.com/solutions/case-studies/snap-case-study/ |
| S3 | BBC | Archive exit to Glacier Instant Retrieval | 25 PB in 10 months | https://aws.amazon.com/solutions/case-studies/bbc-s3-case-study/ |
| S3 | Photobox | Storage-class transitions | Moved 10 PB between classes in ~24 hours (Sep 15, 2022) | https://aws.amazon.com/blogs/storage/how-photobox-optimizes-storage-costs-for-over-12-billion-photos-with-amazon-s3-glacier-instant-retrieval/ |
| EC2 / ELB elasticity | Dream11, Code.org, PayU | ALB with EC2 scaling | Dream11: 100+ load balancers, >65 billion requests/day; Code.org: traffic up 400% on event morning; PayU: "scale our services 10x" | https://aws.amazon.com/elasticloadbalancing/customers/ |
| Scaling (containers) | Xero | Faster scale-out | Scale-up time from 55 to 6 min (−89%); MTTR −50% | https://aws.amazon.com/solutions/case-studies/xero-ecs-case-study/ |
| Spot | ITV | Spot on EKS, plus Savings Plans | Up to 60% saved vs On-Demand; $150,000 in 1 year; Spot share 9% → 24% | https://aws.amazon.com/solutions/case-studies/itv-case-study/ |
| Spot | amaysim | Diversified Spot fleet | Compute cost −75%; 100% of production on Spot across 6 instance families | https://aws.amazon.com/solutions/case-studies/amaysim-spot/ |
| Spot / HPC | Western Digital | Massive parallel batch | 2.5 million tasks in 8 hours on a million-vCPU Spot cluster (Jan 8, 2019) | https://aws.amazon.com/blogs/aws/western-digital-hdd-simulation-at-cloud-scale-2-5-million-hpc-tasks-40k-ec2-spot-instances/ |
| Lambda | FINRA, Toyota Connected | Serverless data validation and scale | FINRA: half a trillion validations on 37 billion events daily, costs −50%+. Toyota Connected: 18x traffic, 18 billion transactions/month | https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/case-studies.html |
| Many services | Amazon Prime Day 2025 | Scale and resilience testing | DynamoDB peak 151M req/s; Aurora 500B transactions; SQS 166M msg/s; Kinesis 807M records/s; ElastiCache >1.4T req/minute; Lambda >1.7T invocations/day; CloudFront >3T requests; Fargate 107.1M tasks/day (corrected 8/5/26); Graviton >40% of Amazon.com EC2 compute; 6,800 FIS experiments | https://aws.amazon.com/blogs/aws/aws-services-scale-to-new-heights-for-prime-day-2025-key-metrics-and-milestones/ |
| DynamoDB | Genesys | Multi-Region availability | 99.999% for the 12 months ending Jul 31, 2024; 15 primary + 5 satellite Regions | https://aws.amazon.com/solutions/case-studies/genesys-dynamodb-case-study/ |
| Aurora | Samsung | Oracle → Aurora PostgreSQL with DMS | 1.1B users, ~80,000 req/s, done in under 18 months; 85–90% of queries matched | https://aws.amazon.com/solutions/case-studies/samsung-migrates-off-oracle-to-amazon-aurora/ |
| Aurora + Graviton | Zendesk | Moved 1,200+ Aurora clusters to Graviton | Performance +30%; cost −42% | https://aws.amazon.com/solutions/case-studies/zendesk-graviton-case-study/ |
| RDS | Atlassian | Managed relational database at scale, Reserved Instances | 350,000 RDS databases by 2017; now >2.8M databases | https://aws.amazon.com/solutions/case-studies/atlassian-case-study-rds/ |
| CloudFront | FIFA World Cup 2022 broadcasters | Live-streaming edge | 19+ broadcasters; >49M unique IPs; >150 PB; just under 23 Tbps peak (Feb 1, 2023) | https://aws.amazon.com/blogs/networking-and-content-delivery/world-cup-2022-amazon-cloudfront-retrospective/ |
| CloudFront | (AWS Insights post) | Record traffic peak | 268 Tbps on Nov 1, 2025 | https://aws.amazon.com/blogs/aws-insights/powering-the-worlds-largest-events-how-amazon-cloudfront-delivers-at-scale/ |
| Route 53 / ARC | HashiCorp | Region switch with routing controls and health checks | One API call; traffic shifts in seconds; full propagation ~2 min (Jul 25, 2025) | https://aws.amazon.com/blogs/architecture/how-hashicorp-made-cross-region-switchover-seamless-with-amazon-application-recovery-controller/ |
| Multi-Region DR | Athenahealth | Aurora Global Database, S3 cross-Region replication, DNS failover, tested with AWS FIS, after the Oct 2025 us-east-1 event | 12–14 minute recovery (Sep 9, 2026) | https://aws.amazon.com/blogs/architecture/validating-multi-region-dr-for-terraform-enterprise-with-aws-fis/ |
| Multi-Region DR | US insurance company | 3-tier application DR | RTO and RPO under 15 min (Nov 11, 2024) | https://aws.amazon.com/blogs/architecture/how-an-insurance-company-implements-disaster-recovery-of-3-tier-applications/ |
| VPC / Cloud WAN / Direct Connect | IC | Replaced peering mesh with Cloud WAN policy; Direct Connect for trading | >40 VPC peering connections replaced by one policy; 6 Regions; MTTR −90% | https://aws.amazon.com/solutions/case-studies/ic-cloud-wan/ |
| Transit Gateway | ZS | Hub-and-spoke network orchestration (Jan 23, 2024) | Architecture only; no figures extracted | https://aws.amazon.com/blogs/networking-and-content-delivery/how-zs-used-network-orchestration-for-aws-transit-gateway-to-optimize-costs-and-scale-up/ |
| PrivateLink | Autodesk, Snowflake (quotes) | Private access to SaaS and shared services | Autodesk: "hundreds of developer teams … own accounts and VPCs" | https://aws.amazon.com/privatelink/customers/ |
| Direct Connect | Allergan | Hybrid connectivity to on-premises apps | 1-Gbps Direct Connect, "near-zero network latency" | https://aws.amazon.com/solutions/case-studies/allergan/ |
| EventBridge / event-driven | LEGO | Monolith to serverless event-driven, after a ~2-hour Black Friday outage | Transaction spikes up to 200x; user traffic up to 9.5x (May 15, 2023) | https://aws.amazon.com/blogs/industries/building-a-serverless-event-driven-retail-order-management-system/ |
| Kinesis | Comcast (Netflix and Zillow also on page) | Streaming data platform | — | https://aws.amazon.com/kinesis/data-streams/customers/ |
| ECS / Fargate | Smartsheet | Fargate on Graviton | Cost −20% | https://aws.amazon.com/solutions/case-studies/smartsheet-ecs-fargate-case-study/ |
| ElastiCache | Tinder | Self-managed Redis on EC2 → ElastiCache | 2B daily member actions; >30B matches (Jan 30, 2020) | https://aws.amazon.com/blogs/database/building-resiliency-at-scale-at-tinder-with-amazon-elasticache/ |
| DataSync | Globe Telecom | Online bulk migration of HDFS data | 7.2 PB; up to 72 TB/day at 85% network utilization | https://aws.amazon.com/blogs/storage/how-globe-telecom-used-aws-datasync-at-scale-to-migrate-7-2-pb-of-hadoop-data/ |
| DataSync | LSEG | Market data migration, landing in S3 Intelligent-Tiering | 30 PB in under 3 months | https://aws.amazon.com/blogs/storage/how-london-stock-exchange-group-migrated-30-pb-of-market-data-using-aws-datasync/ |
| Savings Plans | Alert Logic | Commitment coverage | SP ~80% coverage, RIs 16%; total spend −28% | https://aws.amazon.com/solutions/case-studies/alert-logic-case-study/ |
| Startups | Depot | EC2 at very high volume, Graviton4, S3 cache | Millions of EC2 instances per day; up to 30% faster builds; ~2 PB/day to and from S3 | https://startups.aws.com/learn/depot-and-aws-building-for-humans-and-machines |
| Startups | Retell | ECS, DynamoDB, ElastiCache | $4M ARR (2024) → $40M (end 2025) → ~$70M | https://startups.aws.com/learn/how-retell-built-ai-voice-agents-on-aws-that-feel-as-natural-as-talking-to-a-person |
| Startups | Pronto | EKS, RDS, ElastiCache, S3 | 25,000 daily bookings | https://startups.aws.com/learn/pronto-scales-home-services-platform-for-25000-daily-bookings |
| Startups | Porter (YC) | EC2, RDS, EKS | — | https://startups.aws.com/learn/from-yc-to-aws-porter-simplifies-infrastructure-for-scaling-startups |

The AWS startups showcase has moved to https://startups.aws.com/showcase, which is a self-promotion directory. The curated stories are at https://startups.aws.com/learn/featured-customers. That page includes a "Made in San Francisco" story, which suits this reader; I did not open it.

---

## Part 5: Feasibility checks for automated grounding

### FAQ pages

All 13 www pages return 200 with no redirect, and **questions and answers are in the raw HTML**. They are also embedded as JSON (`itemLongLoc`). I spot-checked answers on S3 ("11 nines") and EC2 (Elastic IP, hibernation).

Approximate visible text, which includes about 12KB of navigation:

| FAQ | Visible text | Approx. questions |
|---|---|---|
| S3 | 253KB | ~371 |
| EC2 | 253KB | ~523 |
| RDS | 126KB | ~196 |
| CloudFront | 133KB | ~200 |
| Route 53 | 94KB | ~164 |
| ELB | 55KB | ~145 |
| KMS | 55KB | ~87 |
| EFS (`/efs/faq/`) | 54KB | ~62 |
| SQS | 49KB | ~105 |
| DynamoDB | 40KB | ~73 |
| Lambda | 38KB | ~78 |
| EBS | 38KB | ~68 |
| IAM | 25KB | ~27 (short) |

**Aurora redirects** to https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq.html. That landing page holds about 12 questions; the FAQ is split into 10 sub-pages. Use `…/auroraextendedcontent/llms.txt` or `full.md` (192KB).

### Pricing pages

The pages are hybrid: the core price tables are placeholders filled in by JavaScript. Example from the raw S3 HTML:

`{priceOf!s3/s3-standard!Standard!Storage!First!50!TB!per!GB!Mo} per GB`

- Literal dollar figures appear only in prose and worked examples. For example, the VPC page's NAT gateway example says "the rate is $0.045 per hour".
- **EC2 On-Demand has no instance prices in its raw HTML** (`t3.micro` does not appear).
- The pages load their data from `b0.p.awsstatic.com` JSON. These endpoints are undocumented, need no authentication, and are gzip-encoded:
  - …/meteredUnitMaps/s3/USD/current/s3-standard.json (200, 378KB)
  - …/lambda/USD/current/lambda.json (200)
  - …/ec2/USD/current/ec2-ondemand-without-sec-sel/US%20East%20(N.%20Virginia)/Linux/index.json (200)
- **The official Price List Bulk API works.** https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json returns 200, with 272 offers and publicationDate 2026-10-05T00:07:45Z.
  - Offer codes include AmazonS3, AmazonEC2, AWSLambda, AmazonVPC, AmazonRDS, AmazonDynamoDB, AmazonCloudFront, AmazonRoute53, AWSQueueService, awskms, AmazonEFS, AWSELB, AmazonSNS, AmazonElastiCache, AWSDirectConnect and AmazonKinesis.
  - Each offer's `region_index.json` gives a `currentVersionUrl` per Region. The Lambda us-east-1 file loaded (724KB).
  - Savings Plans: `/savingsPlan/v1.0/aws/AWSComputeSavingsPlan/current/region_index.json` returns 200.

### `llms.txt` and `.md` pattern

Every guide below returns 200 for its `llms.txt`, a sample page's `.html`, and that page's `.md`:

| Guide | Root URL |
|---|---|
| S3 User Guide | https://docs.aws.amazon.com/AmazonS3/latest/userguide/ |
| EC2 User Guide | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ |
| EBS User Guide | https://docs.aws.amazon.com/ebs/latest/userguide/ |
| EFS User Guide | https://docs.aws.amazon.com/efs/latest/ug/ |
| RDS User Guide | https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ |
| Aurora User Guide | https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ |
| DynamoDB Developer Guide | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ |
| Lambda Developer Guide | https://docs.aws.amazon.com/lambda/latest/dg/ |
| IAM User Guide | https://docs.aws.amazon.com/IAM/latest/UserGuide/ |
| ELB guides (application, network, gateway, general) | https://docs.aws.amazon.com/elasticloadbalancing/latest/{application,network,gateway,userguide}/ |
| Auto Scaling User Guide | https://docs.aws.amazon.com/autoscaling/ec2/userguide/ |
| Route 53 Developer Guide | https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ |
| CloudFront Developer Guide | https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ |
| SQS Developer Guide | https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/ |
| SNS Developer Guide | https://docs.aws.amazon.com/sns/latest/dg/ |
| KMS Developer Guide | https://docs.aws.amazon.com/kms/latest/developerguide/ |
| Organizations User Guide | https://docs.aws.amazon.com/organizations/latest/userguide/ |
| AWS CLI User Guide | https://docs.aws.amazon.com/cli/latest/userguide/ |

- **Exception: the CLI command reference** (https://docs.aws.amazon.com/cli/latest/reference/) has no `llms.txt` and no `.md` (both 404). Its HTML is fully readable without JavaScript (the put-object page is 100KB). awscli.amazonaws.com/v2 redirects there.
- **Whole-guide files:** per-guide `full.md` exists (S3 is 6.8MB, Reliability pillar 665KB). There is also a site-wide index at https://docs.aws.amazon.com/llms.txt (418KB).

---

## Could not verify

1. **Skill Builder item details.** The site is JavaScript-only. Unconfirmed: exact deep links; whether an **SAA-C03 Official Pretest** exists; the sizes 18h25m, 2h10m and 66h45m (from search-engine summaries); the 4.5 h Standard Course (Class Central **[third-party]**); the Escape Room's 2–3 hours.
2. **ESL +30 for an already-booked exam.** Only the 2018 LinkedIn post (third-party, PSI era) says you must cancel first. There is also no explicit official statement that ESL +30 covers online proctoring; it is inferred from "all test delivery providers".
3. **Expiry date of the 50% voucher.** Not stated on the benefits, FAQ or recertification pages.
4. **Global Infrastructure "as of" date.** None is shown on the page.
5. **Builder Center article text.** builder.aws.com pages could not be read by curl or WebFetch; the PDF fallbacks were used. Content at catalog.workshops.aws and builder.aws.com/build/workshops was also not verified.
6. **Prime Day 2026 metrics post.** Not found as of today.
7. **Search-summary figures I did not confirm on the pages themselves:** Samsung's "44%" saving; Atlassian's Multi-AZ mention; GDIT's "700+ VPCs" (Transit Gateway customers page); Netflix and Zillow wording on the Kinesis page; Photobox's 10 PB via Snowball Edge; Rapid7's SQS volume.
8. **AWS-employee-specific benefits** (internal vouchers or Skill Builder access). These are not on public pages; check internal channels.
9. **This is My Architecture and Amazon Science** were not searched for Part 4.

Separately: Excalidraw, Gmail, Google Calendar and Google Drive need to be authorized in the claude.ai connector settings before they can be used. None were needed for this research.
