# Study calendar: preview

This is a preview, written on 2026-10-04 while the SAA-C03 Handbook is being built. Chapters arrive in the order of this calendar.

The final chapter 00 replaces this file.

## Before you book the exam

Do step 1 tonight.

1. **Request ESL +30 first.** ESL +30 is a [30-minute exam extension for non-native English speakers](https://aws.amazon.com/certification/policies/before-testing/). The exam has [65 questions in 130 minutes](https://aws.amazon.com/certification/certified-solutions-architect-associate/), so you get 160 minutes. You must request ESL +30 once, before you register for an exam.

   Path: sign in to `aws.training/Certification` > Go to your Account > Request Exam Accommodations > Request Accommodation > Accommodation Type: ESL +30 MINUTES > Create.

2. **Know the retake wait.** If you fail, you must [wait 14 calendar days](https://aws.amazon.com/certification/policies/after-testing/) before a retake. So a second attempt in October needs a first exam by Oct 17. Your plan of Oct 20 to 24 leaves no retake before Oct 31.

3. **Know the reschedule limits.** You can reschedule [up to 24 hours before the exam time, and only twice](https://aws.amazon.com/certification/policies/before-testing/). In the last 24 hours there are no changes and no refunds. So book after step 1, for Day 19 of the calendar. Move the date only if a gate at the end says so.

4. **Take the free official practice set on Day 1.** The set is [free and has 20 questions with feedback](https://aws.amazon.com/certification/certification-prep/). You reach it through the [SAA-C03 exam prep plan on AWS Skill Builder](https://skillbuilder.aws/category/exam-prep/solutions-architect-associate-SAA-C03). Take it before you study, as your baseline.

## How to use a chapter

A chapter is a folder of short files. Choose one route for each chapter.

- **Fast:** read `1-fast.md`. About 20 minutes for a deep chapter, 12 for a medium chapter.
- **Pass:** Fast, then the core questions in `5-quiz.md`. Read only the `2-deep.md` sections that your wrong answers point to. Give one spoken answer from `4-say.md`. About 50 minutes (65 for IAM, VPC, S3 and EC2), 22 for a medium chapter.
- **Full:** every file, with the tasks in `3-do.md`. About 2 hours 15 minutes, 1 hour for a medium chapter. Mostly for after the exam.

Speak out loud for 10 minutes every day, standing, in a private room. Take one prompt from a `4-say.md` file and use the same four moves.

| Move | Start with |
|---|---|
| 1 Answer | "The short answer is ..." |
| 2 How | "It works like this ..." |
| 3 Watch | "The thing to watch is ..." |
| 4 You | "In your case ...", then ask one question back |

First read the model answer aloud. Then answer without the text, with a 90-second timer.

## The calendar

Your diagnostic of 2026-09-18 sets the order and the routes.

- Security comes first, because Secure was your weakest domain (45%): 03 IAM on Day 1, the security block on Day 5.
- The topics that you know well are Fast only: 18 Lambda, 19 Containers (Fargate), 33 API Gateway, 41 Cost optimization.

If Day 1 is Monday Oct 5, the light days are Oct 7 and 8. The speaking rehearsal is Oct 12, before your spoken exam. Day 19 is Friday Oct 23.

| Day | How long | What to do |
|---|---|---|
| 1 | 2.75 h | First, request ESL +30 before booking. Then the official 20-question set, 01 How the exam asks (Fast), 02 The AWS map (Fast), 03 IAM (Pass). |
| 2 | 2.5 h | 10 VPC (Pass). 21 S3 (Pass). 8 more questions from the 03 IAM quiz. |
| 3 | 20 min | Light day. 8 quiz questions from 03, 10 or 21. 1 spoken answer. |
| 4 | 10 min | Light day. 1 spoken answer. |
| 5 | 3.25 h | Security block, all Pass: 04 Organizations, 05 Identity Center and Cognito, 06 KMS, 07 Secrets Manager and ACM, 08 WAF and Shield, 09 GuardDuty and detection. Then 16 EC2 (Pass). |
| 6 | 3.25 h | All Pass: 22 EBS, 14 Load balancing, 17 Auto Scaling, 26 RDS. |
| 7 | 3.25 h | All Pass: 27 Aurora, 28 DynamoDB, 13 Route 53, 15 CloudFront. |
| 8 | 2.5 h | Speaking rehearsal, 45 minutes: 10 random prompts from the `4-say.md` files, 90 seconds each. Then 31 SQS, SNS and EventBridge (Pass), 23 EFS and FSx (Pass). |
| 9 | 1 h | 18 Lambda (Fast). 40 High availability and disaster recovery (Pass). 41 Cost optimization (Fast). |
| 10 | 3 h | Mock 1 and review. |
| 11 | 1.75 h | Pass: 11 Connecting VPCs, 12 VPN and Direct Connect. Fast: 19 Containers, 29 ElastiCache, 33 API Gateway, 24 Backup, 25 Hybrid storage. |
| 12 | 3 h | Mock 2 and review. |
| 13 | 2.5 h | Pass: 37 CloudWatch and CloudTrail, 42 Security patterns. Fast: 32 Step Functions, 34 Streaming, 35 Analytics, 38 CloudFormation and Systems Manager, 39 Migration, 43 Decoupling patterns. Then 45 Decision atlas. |
| 14 | 3 h | Mock 3 and review. Gate 1. |
| 15 | 1.5 h | Repair day. Read the `2-deep.md` sections that your mock mistakes point to. Redo your wrong questions. Then 44 Reference architectures. |
| 16 | 3 h | Mock 4 and review. |
| 17 | 3 h | Mock 5 and review. Gate 2. |
| 18 | 1.25 h | Review sheets: 46 Signals and traps, 47 Numbers to know, 48 What changed recently, 52 Final week and exam day. Then your mistakes log. Stop by 18:00. |
| 19 | exam | Warm-up only: the traps list in 46. |

Total: about 41 hours, or 38 without mock 5 (see Gate 1). Your budget is 40.

- **Mock:** one full Tutorials Dojo practice exam in timed mode, in one quiet two-hour block, then about 1 hour of review. Pace: 2 minutes or less per question, then your flagged questions. Answer every question: there is [no penalty for guessing](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).
- **Optional, not in the total:** the tasks in `3-do.md`, and the Pass route for the Fast chapters of Days 11 and 13. Also the light chapters (20, 30, 36), 49 Speaking pack, the book's own mocks (50, 51), and Anki.

## If your date is different

**Earlier: exam by Saturday Oct 17 (Day 13), which keeps a retake in October.**

- Keep Days 1 to 8. Day 9: mock 1. Day 10: the chapters of Days 9 and 11, then 42 Security patterns and 45 Decision atlas. Day 11: mock 2. Day 12: the Day 18 review sheets. About 29 hours.
- Dropped: mocks 3 to 5, the repair day, 44 Reference architectures and the rest of Day 13. The gate is weaker: 70% or more on mock 1, 75% or more on mock 2.
- Choose it only if your Day 1 practice set is 70% or more and a recorded fail costs you nothing. Check the exact retake date in your certification account. If mock 2 is under 75%, move the exam to Day 19.

**Later: exam on Oct 27 or 28 (Day 23 or 24).**

- Keep Days 1 to 16. Add a repair day after each mock: mock 5 moves to Day 18, and mock 6 is new on Day 20. Review sheets on the last day before the exam. About 46 hours.
- The cost: no retake in October, and a conflict with your slides (Oct 24) and panel week (Oct 27).
- Results arrive [within five business days](https://aws.amazon.com/certification/policies/after-testing/), so the result can come in November. Do not choose Oct 30.

## Go or move

Gate 1 is after mock 3. Gate 2 is after mock 5. Only first attempts in timed mode count.

| Gate | If | Then |
|---|---|---|
| Gate 1 | Mocks 2 and 3 are both 80% or more | You are ahead. Mock 5 is optional. |
| Gate 1 | Mock 3 is under 65% | Move the exam now, to Oct 27 or 28. |
| Gate 1 | Anything between | Continue the calendar. |
| Gate 2 | Your last two mocks are both 80% or more | Go. This is your own rule. |
| Gate 2 | Both are 75% or more, no domain is under 65%, and you finished with 10 minutes left | Go. This is the softer rule. A later date leaves no retake either. |
| Gate 2 | Anything lower | Move the exam to Oct 27 or 28. |

A move must happen [at least 24 hours before your exam time](https://aws.amazon.com/certification/policies/before-testing/). So decide Gate 2 on the evening of Day 17.

The chapters appear in the folder `aws-saa-book/`, and soon in a web version.
