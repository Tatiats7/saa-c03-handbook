# SAA-C03 study plan

Built from the diagnostic taken on 2026-09-18: 45/65 (69%), 35 correct-and-sure, 51 of 130 minutes used.

| Domain | Exam weight | Score |
|---|---|---|
| Secure architectures | 30% | 9/20 (45%) |
| Resilient architectures | 26% | 12/17 (71%) |
| High-performing architectures | 24% | 12/15 (80%) |
| Cost-optimized architectures | 20% | 12/13 (92%) |

Target: exam booked for the week of 2026-10-12 to 2026-10-16. About 45 hours total, 11 to 12 hours a week.

## Course sections: what to watch

**Skip** (100% and mostly sure): pricing models and cost tools, Lambda / API Gateway / Fargate.

**Watch, then drill**: the S3 sections (storage classes, lifecycle, replication, security). Scored 100% on the diagnostic but without confidence on tiering. After the videos, take the S3 Tiering Drill (https://claude.ai/artifact/9GSd7D25HMkxzvDrwA97Sa, source in s3-tiering-drill.html). Goal: 80% or more correct-and-sure; retake after 2 to 3 days if below.

**Cheat sheet only, no video** (right but marked not sure): EBS volume types (gp3, io2, st1, sc1), EFS vs FSx for Lustre vs FSx for Windows, Aurora Serverless, DynamoDB global tables.

**Watch at 1.5x**: VPC, load balancers, Route 53 / CloudFront / Global Accelerator, RDS and Aurora, DynamoDB, SQS / SNS / Kinesis, DR and AWS Backup.

**Watch fully, take notes**: IAM advanced, AWS Organizations, IAM Identity Center, Cognito, KMS and encryption, the security services section.

## Week 1 (Sep 19 to 25): security, 12 h

Security is 30% of the exam and the weakest domain, so it goes first.

- IAM: roles vs users, permissions boundaries, cross-account roles with STS
- AWS Organizations and SCPs: SCPs are the only control an account admin cannot remove
- IAM Identity Center = workforce sign-in to AWS accounts. Cognito = end users of your app. User pool = sign-up and sign-in; identity pool = temporary AWS credentials
- WAF (layer 7: SQL injection, XSS) vs Shield (DDoS) vs network ACL (deny an IP at the subnet) vs security group (allow only)
- GuardDuty vs Inspector vs Macie
- KMS: SSE-S3 vs SSE-KMS vs SSE-C, customer managed keys, Secrets Manager vs Parameter Store
- S3 Object Lock: governance (can be bypassed) vs compliance (nobody, not even root)
- Systems Manager Session Manager replaces bastion hosts
- CloudFront origin access control needs two parts: OAC on the distribution and a bucket policy

## Week 2 (Sep 26 to Oct 2): networking, resilience, databases, 12 h

- VPC endpoints: gateway (S3 and DynamoDB, free) vs interface (PrivateLink, paid)
- Load balancers: ALB (layer 7) vs NLB (layer 4, static IPs, extreme scale) vs Gateway LB (third-party appliances)
- Global Accelerator (static anycast IPs, TCP/UDP, fast failover) vs CloudFront (HTTP caching) vs Route 53 routing policies (DNS, TTL-bound)
- RDS Multi-AZ (availability, automatic failover, same endpoint) vs read replicas (read scaling, async, manual promotion)
- DR strategies in order: backup and restore, pilot light, warm standby, multi-site active/active
- AWS Backup (many services, cross-account) vs Data Lifecycle Manager (EBS snapshots and AMIs only)
- DynamoDB: DAX = microsecond read latency, not a cost tool; provisioned + auto scaling for steady load, on-demand for spiky
- SQS: dead-letter queue vs delay queue vs visibility timeout; FIFO message groups
- Kinesis Data Streams (replay, many consumers) vs Firehose (delivery) vs SQS
- One hands-on lab (2 h): build a VPC with public and private subnets, NAT gateway, and an S3 gateway endpoint

## Week 3 (Oct 3 to 9): practice exams in review mode, 11 h

- Tutorials Dojo sets 1 to 3 in review mode; read every explanation, including for correct answers
- Topic-based drills on anything under 70%
- Keep a one-page list of confusions as they appear

## Week 4 (Oct 10 to 16): timed exams, 10 h

- Sets 4 and 5 in timed mode, full review after each
- Set 6 and the Final Test as the go/no-go check
- Go: 75% or higher on first attempts. Below that, move the exam one week

## Exam technique

The diagnostic took 51 of 130 minutes. There is time to spare: read each scenario twice, underline the constraint words (MOST cost-effective, LEAST operational effort, automatic, without internet), and on Select TWO questions check that two boxes are ticked.
