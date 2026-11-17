# SAA-C03 Handbook: build status

Generated 2026-11-16 19:40 PST from the ledger by `status_report.py`.

## Progress

| Measure | Value |
|---|---|
| Overall, weighted by the 16 ledger stages | 56.0% |
| Chapters ready (final gate passed) | 26 of 53 |
| Fact bases verified (chapters that mine their own facts) | 35 of 44 |

| Book totals | Value |
|---|---|
| Verified facts | 18,290 |
| Hand-written words (fast and deep files) | 165,594 |

## Chapters

| Ch | Slug | Template | State | Next stage | Facts verified | Questions |
|---|---|---|---|---|---|---|
| 00 | start-here | front | ready | - | 0/0 | 0/0 |
| 01 | how-the-exam-asks | front | ready | - | 92/92 | 10/10 |
| 02 | aws-map | front | ready | - | 313/370 | 10/10 |
| 03 | iam | deep | ready | - | 384/384 | 18/18 |
| 04 | organizations | medium | ready | - | 305/320 | 10/10 |
| 05 | identity-federation | medium | ready | - | 410/410 | 10/10 |
| 06 | kms | medium | ready | - | 314/314 | 10/10 |
| 07 | secrets-certificates | medium | ready | - | 394/394 | 10/10 |
| 08 | edge-protection | medium | ready | - | 454/454 | 10/10 |
| 09 | detection | medium | ready | - | 423/423 | 10/10 |
| 10 | vpc | deep | ready | - | 511/511 | 18/18 |
| 11 | vpc-connectivity | medium | facts-verified | edit | 506/506 | 10/10 |
| 12 | hybrid-networking | medium | ready | - | 519/519 | 10/10 |
| 13 | route53 | deep | ready | - | 785/785 | 18/18 |
| 14 | elb | deep | ready | - | 440/441 | 18/18 |
| 15 | cloudfront | deep | ready | - | 744/744 | 18/18 |
| 16 | ec2 | deep | ready | - | 492/492 | 18/18 |
| 17 | auto-scaling | deep | ready | - | 522/522 | 18/18 |
| 18 | lambda | deep | ready | - | 435/438 | 18/18 |
| 19 | containers | medium | ready | - | 678/678 | 10/10 |
| 20 | more-compute | light | planned | plan | 0/0 | 0/6 |
| 21 | s3 | deep | ready | - | 607/615 | 18/18 |
| 22 | ebs | deep | ready | - | 412/413 | 18/18 |
| 23 | efs-fsx | deep | ready | - | 870/870 | 18/18 |
| 24 | backup | medium | facts-verified | prose | 532/532 | 0/10 |
| 25 | hybrid-storage | medium | facts-verified | brief | 718/718 | 0/10 |
| 26 | rds | deep | ready | - | 617/617 | 18/18 |
| 27 | aurora | deep | ready | - | 823/823 | 18/18 |
| 28 | dynamodb | deep | ready | - | 708/708 | 18/18 |
| 29 | elasticache | medium | facts-verified | brief | 455/455 | 0/10 |
| 30 | more-databases | light | planned | plan | 0/4 | 0/6 |
| 31 | messaging | deep | ready | - | 550/550 | 18/18 |
| 32 | step-functions | medium | facts-verified | brief | 501/501 | 0/10 |
| 33 | api-gateway | medium | facts-verified | brief | 458/458 | 0/10 |
| 34 | streaming | medium | facts-verified | brief | 630/630 | 0/10 |
| 35 | analytics | medium | facts-verified | brief | 1045/1045 | 0/10 |
| 36 | ai-ml-media | light | planned | plan | 0/0 | 0/6 |
| 37 | monitoring | medium | facts-verified | brief | 643/643 | 0/10 |
| 38 | deploy-operate | medium | planned | plan | 0/0 | 0/10 |
| 39 | migration | medium | planned | plan | 0/0 | 0/10 |
| 40 | ha-dr | deep | planned | plan | 0/0 | 0/10 |
| 41 | cost | deep | planned | plan | 0/7 | 0/10 |
| 42 | security-patterns | medium | planned | plan | 0/0 | 0/10 |
| 43 | decoupling-scaling | medium | planned | plan | 0/0 | 0/10 |
| 44 | reference-architectures | synthesis | planned | plan | 0/0 | 0/8 |
| 45 | decision-atlas | synthesis | planned | plan | 0/0 | 0/24 |
| 46 | signals-traps | synthesis | planned | plan | 0/0 | 0/0 |
| 47 | numbers | synthesis | planned | plan | 0/0 | 0/0 |
| 48 | changed-recently | synthesis | planned | plan | 0/0 | 0/0 |
| 49 | speaking-pack | synthesis | planned | plan | 0/0 | 0/0 |
| 50 | mock-exam-1 | mock | planned | plan | 0/0 | 0/65 |
| 51 | mock-exam-2 | mock | planned | plan | 0/0 | 0/65 |
| 52 | final-week | synthesis | planned | plan | 0/0 | 0/0 |

## Downloaded AWS pages (the corpus)

6,393 unique pages fetched with status 200, saved under `aws-saa-book/_build/corpus/` (19,716 snapshot files). Every verified fact quotes one of these snapshots and checks its SHA-256, so the corpus travels with the repository and is never re-fetched.

| Host | Pages |
|---|---|
| docs.aws.amazon.com | 5,293 |
| aws.amazon.com | 1,095 |
| repost.aws | 3 |
| d1.awsstatic.com | 2 |

Documentation guides covered: 142. Largest: cli (378), whitepapers (264), AmazonRDS (251), vpc (216), IAM (168), wellarchitected (163), AWSEC2 (150), amazondynamodb (139), elasticloadbalancing (125), Route53 (117), AmazonS3 (115), autoscaling (108), AmazonCloudWatch (107), waf (101), lambda (100).

Not downloaded yet: the pages for the chapters whose state is `planned` above. Their plan agents fetch them (only pages not already in the corpus).

