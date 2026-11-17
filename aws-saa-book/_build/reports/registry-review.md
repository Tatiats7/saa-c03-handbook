# Registry review (registry-critic, 2026-10-11)

Scope: completeness check of `data/book.json` after the three mapping agents (00-15, 16-30, 31-52). Checked by script (`registry check`, `registry check --urls`) and by judgment (every bullet text against the chapter titles and services; every in-scope entry; every chapter's guide, FAQ and history sources; the shared-topic owners of the task).

## 1. Final numbers

| Measure | Value |
|---|---|
| Exam-guide bullets | 189, all mapped (189 of 189) |
| Bullet links (bullet x chapter) | 361 (359 before this review; +2) |
| Task statements | 14, all in at least one chapter; 50 and 51 carry all 14 |
| In-scope entries | 118 unique (119 lines), all with a home chapter and a level |
| `registry check` | 0 errors, 3 warnings (R11, kept with reason below) |
| `registry check --urls` before | 61 R06 errors (snapshots missing), 7 warnings (3 R11, 4 R16) |
| `registry check --urls` after | 0 errors, 8 warnings (3 R11, 5 R16; 57 snapshots fetched, 2 dead URLs removed) |
| Gaps fixed | 6: bullet 1.1.S5 added to 21; bullet 1.3.K2 added to 40; 57 missing snapshots fetched for chapters 40 to 48; dead Elastic Transcoder guide page removed from 36; dead Builders' Library page removed from 40; Cost and Usage Report FAQ page added to 41 |

## 2. Bullets per chapter (after the review)

| Ch | Title | Bullets |
|---|---|---|
| 00 | Start here and study calendar | 0 (front) |
| 01 | How the exam asks, and exam English | 0 (front; owns fact namespace `exam`) |
| 02 | The AWS map | 6 |
| 03 | IAM | 11 |
| 04 | Organizations, SCPs, Control Tower and RAM | 3 |
| 05 | IAM Identity Center, Directory Service and Cognito | 5 |
| 06 | KMS and CloudHSM | 4 |
| 07 | Secrets Manager, Parameter Store and ACM | 5 |
| 08 | WAF, Shield, Firewall Manager and Network Firewall | 3 |
| 09 | GuardDuty, Inspector, Macie, Security Hub, Detective, Config and Artifact | 3 |
| 10 | Amazon VPC | 14 |
| 11 | Connecting VPCs | 6 |
| 12 | Site-to-Site VPN, Direct Connect and Client VPN | 6 |
| 13 | Amazon Route 53 | 5 |
| 14 | Elastic Load Balancing | 9 |
| 15 | CloudFront and Global Accelerator | 6 |
| 16 | Amazon EC2 | 13 |
| 17 | EC2 Auto Scaling | 11 |
| 18 | AWS Lambda | 9 |
| 19 | ECS, EKS, Fargate and ECR | 8 |
| 20 | More compute (light family) | 6 |
| 21 | Amazon S3 | 19 (18 + 1.1.S5 added) |
| 22 | EBS and instance store | 13 |
| 23 | EFS and FSx | 13 |
| 24 | AWS Backup and backup strategy | 8 |
| 25 | Storage Gateway, DataSync, Snow Family and Transfer Family | 8 |
| 26 | Amazon RDS | 17 |
| 27 | Amazon Aurora | 13 |
| 28 | Amazon DynamoDB | 13 |
| 29 | ElastiCache and caching | 7 |
| 30 | Redshift and purpose-built databases (light family) | 5 |
| 31 | SQS, SNS and EventBridge | 9 |
| 32 | Step Functions, Amazon MQ and AppFlow | 4 |
| 33 | Amazon API Gateway | 5 |
| 34 | Kinesis Data Streams, Data Firehose and MSK | 6 |
| 35 | Athena, Glue, Lake Formation, EMR, OpenSearch and Quick | 7 |
| 36 | AI/ML, media and front-end (light family) | 3 |
| 37 | CloudWatch, CloudTrail and X-Ray | 5 |
| 38 | CloudFormation, Systems Manager and operations tools | 3 |
| 39 | Migration: DMS, SCT and Application Migration Service | 4 |
| 40 | High availability and disaster recovery | 10 (9 + 1.3.K2 added) |
| 41 | Cost optimization | 18 |
| 42 | Security patterns | 8 |
| 43 | Decoupling, scaling and caching patterns | 8 |
| 44 | Reference architectures | 7 |
| 45 | Decision atlas | 15 |
| 46-49 | Signals and traps, Numbers, What changed, Speaking pack | 0 (synthesis; no bullet taught first there) |
| 50, 51 | Mock exams | 0 bullets, all 14 task statements |
| 52 | Final week and exam day | 0 |

Per task statement every bullet has at least one chapter where the bullet's example services are the chapter's own services (checked bullet by bullet; see section 4 for the ones that needed a decision).

## 3. In-scope services (118)

Every entry has `home_chapter` and `level` (deep 23 keys, medium, light, and `front` for AWS CLI and AWS Management Console as recognition cards in chapter 02). Keys mapped under a parent entry so questions can carry them: `sts` (IAM), `vpc-peering` and `vpc-endpoints` (Amazon VPC), `instance-store` (Amazon EC2), `rds-proxy` (Amazon RDS), `dax` (Amazon DynamoDB), `parameter-store` (AWS Systems Manager; home stays 38, taught in 07).

Shared-topic owners, verified in the registry:

| Topic | Owner | How it shows |
|---|---|---|
| VPC endpoints | 11 owns, 10 introduces | key `vpc-endpoints` in 11; bullet 1.2.K2 in 10, 11 (and 42); 4.4.S3 in 10, 11, 15, 41 |
| DAX | 28 | key `dax` in 28; caching bullets 3.3.K2 in 28 and 29 |
| RDS Proxy | 26 | key `rds-proxy` in 26; 2.2.K9, 3.3.K5, 4.3.K6 only in 26 |
| Global Accelerator | 15 | key in 15; 3.4.K1 in 15 (45 compares) |
| Elastic Disaster Recovery and DR strategies | 40 | DRS guide, DR whitepaper, DR FAQ and pricing in 40; 2.2.K4 and 2.2.S6 owned by 40 (24 carries 2.2.K4 for backup-and-restore only) |
| Data transfer cost and purchasing options | 41 | 4.2.K4 in 16 and 41; 4.4.S3 and the network pricing pages (VPC, ELB, Direct Connect, VPN, Transit Gateway, CloudFront, Route 53) in 41 |
| S3 Glacier storage classes | 21 | key `s3-glacier` in 21 with the Glacier guide, its history page and the storage-classes page |
| Exam policy facts | 01 | `book.fact_namespaces = {"exam": "01"}`; 01 carries the exam guide root and the three policy pages |

## 4. Judgment calls

Bullets (each was read against the chapter titles and service lists; "not covered" was the default when unsure):

1. **1.1.S5 "resource policies" added to 21 (S3).** It was in 03, 31, 42. Bucket policies are the resource policy the exam asks about most; S3 was the one service chapter with resource policies that did not carry the bullet. Chapter 21 is past mining, so this is an addition only (its brief stage re-reads the registry).
2. **1.3.K2 "Data recovery" added to 40 (HA and DR).** It was only in 24 (AWS Backup). Chapter 40 owns Elastic Disaster Recovery and the DR strategies, which is where recovery of workloads is taught; 24 keeps the data-backup half.
3. 2.1.K13 "Storage types (object, file, block)" is in 23 only, while its twins 3.1.K3 and 4.1.K11 are in 22 and 23: accepted, the same comparison is taught once in 22 and 23 and the three ids spread across the two chapters.
4. 2.2.S5 "durability and availability of data (backups)" is in 22, 24, 28 and not 21: accepted, 21 already carries 1.3.S5 (backups and replication) and 2.2.K11 (durability, replication).
5. 4.1.K4 "storage services with use cases (FSx, EFS, S3, EBS)" is in 22, 23 and not 21: accepted, 21 carries 3.1.K2 and 4.1.S10 with the same comparison.
6. 3.5.K5 "Secure access to ingestion access points" only in 34: accepted (Kinesis and Firehose VPC endpoints and IAM are taught there).
7. 2.1.S6 and 2.2.S8 ("recommend / use purpose-built services") are owned by 45 (decision atlas) with a light chapter each (20, 36): accepted, these are comparison bullets by nature.
8. The general bullets in 02 (1.1.K3, 1.1.K5, 2.2.K1, 3.2.K2, 3.3.K1, 4.2.K3) each also sit in a service chapter with questions (10, 03, 13 and 40, 15 and 20, 27 and 28, 16), because 02 is a front chapter without questions.
9. The Domain 4 cost bullets with repeated text (4.1.K2, 4.2.K1, 4.3.K1, 4.4.K1 and the K2 twins) are all in 41, with 04 (multi-account billing) and 38 (Compute Optimizer, Trusted Advisor) as second homes: accepted.
10. 4.3.S4 (time series, columnar) is in 30 only (Redshift). Timestream is not in scope and is in maintenance; accepted.

Services:

11. R11 warnings kept: `global-infrastructure` and `well-architected` (02) and `local-zones` (20) have no in-scope entry. Mapping them under a parent entry would retitle their fact sheets and cards to the parent's official name (lint L104), so they stay unmapped; questions must not carry these keys (Q111). Reason stated here, as the task allows.
12. Elastic Transcoder (36) has no developer guide: `elastictranscoder/latest/developerguide/introduction.html` answers 404 (the service is being discontinued; see the lifecycle page in 48). The page was removed from `sources.pages` of 36 (`--replace sources.pages`, 6 to 5 pages); the FAQ page stays as its source. The writer of 36 must treat Elastic Transcoder as recognition-only.
13. FAQ pages: every chapter with services has at least one FAQ page. Services without their own AWS FAQ page (checked by the mapping agents or here): DAX (404), RDS Proxy (product page recorded), instance store and VPC peering (covered by the EC2 and VPC FAQ), Client VPN (covered by the VPN FAQ), Health Dashboard, VMware Cloud on AWS (product page recorded), X-Ray (`aws.amazon.com/xray/faqs/` redirects to the CloudWatch Application Signals feature page, seen on 2026-10-05 and again today, so it was not added to 37). The Cost and Usage Report FAQ (`aws-cost-management/aws-cost-and-usage-reporting/faqs/`) exists and was missing: added to `sources.faq` of 41, the home chapter of `cost-and-usage-report`.
14. Shield and Firewall Manager (08) have no separate guide: the WAF developer guide is the combined "WAF, Firewall Manager and Shield Advanced" guide, which 08 carries, with the four FAQ pages. Trusted Advisor (38) is taught from the Support user guide and its change log. Accepted.
15. Chapter 40 has no service keys by design (pattern chapter); its DRS, Route 53 ARC and Service Quotas guides are sources, not keys, so no fact sheet is titled after them.

Sources:

16. `registry check --urls` found 61 snapshots missing from the corpus, all in chapters 36 and 40 to 48 (the 31-52 agent's fetch did not finish; it wrote no summary). 57 unique pages were fetched in two batches (40 and 19 URLs, with the two FAQ candidates); all answered 200 except two: the Elastic Transcoder guide page (404, removed from 36) and `aws.amazon.com/builders-library/static-stability-using-availability-zones/` (redirects to builder.aws.com, which is not on the allow-list; removed from `sources.pages` of 40, 24 to 23 pages; the other Builders' Library page in 43 fetched normally). After the fetch: 0 R06 errors.
17. R16 warnings (5) kept: three whitepaper pages in 08 and 15 now redirect into the WAF and CloudFront developer guides, the SCT product page in 39 redirects to `dms/features/`, and `aws.amazon.com/products/lifecycle/` in 48 redirects to `general/latest/gr/service-lifecycle.html`. The redirected content is saved under the original source id on an allowed host, so no evidence is lost; the writers should cite the final URL. Not rewritten here because each needs a whole-list `--replace` and the warning is informational.

## 5. Commands run

- `registry check` (before and after), `registry check --urls --json --out _build/tmp/registry-critic/check-urls-0.json` and `check-urls-1.json`.
- `registry set 21 --bullets 1.1.S5 --by registry-critic`; `registry set 40 --bullets 1.3.K2 --by registry-critic`; `registry set 36 --file patch-36-pages.json --replace sources.pages --by registry-critic`; `registry set 40 --file patch-40-pages.json --replace sources.pages --by registry-critic`; `registry set 41 --file patch-41.json --by registry-critic` (patches under `_build/tmp/registry-critic/`).
- `fetch --batch _build/tmp/registry-critic/batch-1.txt` (40 URLs) and `batch-2.txt` (19 URLs: the rest plus the X-Ray and CUR FAQ candidates); results in `fetch-1.txt`, `fetch-2.txt`.

Nothing was removed from any chapter. No seed-owned key was touched. `data/book.json` was changed only through `registry set`.
