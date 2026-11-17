# Corpus harvest: change feeds and case studies

Date: 2026-10-11. Agent: corpus harvest (changes). Status: **complete**. 255 tool commands, all through `saa.py` (`changes harvest`, `changes history`, `cases harvest --tag`), one process at a time.

## What was done

1. Read `_build/spec/RULINGS.md`, `_build/style/TOOLS-corpus.md`, `TOOLS-feeds.md`.
2. Built the job list from `data/book.json` (`sources.whatsnew_tags`, `sources.history`, `sources.case_tags` of every chapter) and compared it with the feeds the chapter 16-30 mapping agent had already harvested under `_build/corpus/changes/` (77 service files):
   - 144 distinct What's New tags: 89 already in a feed file (skipped as complete), 55 run now, plus 2 chapter-40 tags run by hand.
   - 132 distinct document-history pages: 78 already parsed (skipped), 54 run now.
   - 133 distinct case tags: all run (`cases harvest --tag`), merged into the existing `cases/index.jsonl`.
3. Tag -> service file: the mapping agent's choice where a tag already existed; otherwise the chapter's service id, with hand overrides: `amazon-simple-notification-service` -> `sns`; `amazon-quicksight`, `amazon-quicksuite0` -> `quick`; `amazon-amp` -> `managed-prometheus`; `aws-support` -> `trusted-advisor`; `aws-database-migration-service` -> `dms`; `cloud-financial-management` -> `cost-management`; `aws-account-billing` -> `billing`; `aws-cloudformation-stacksets` -> `cloudformation`; `amazon-cloudwatch-logs` -> `cloudwatch`. History pages of synthesis chapters (40-45) go to `well-architected` (pillars and the WA Tool release notes), `whitepapers`, `prescriptive-guidance`, `decision-guides`, `elastic-disaster-recovery` (drs), `application-recovery-controller` (r53recovery), `service-quotas`; the EventBridge Scheduler page goes to `eventbridge`, the SCT page to `dms`, the Cost Management guide to `cost-explorer`, the Support guide to `trusted-advisor`.
4. Commands were run by a sequential driver, `_build/tmp/harvest-changes/run.py` (one `python3 aws-saa-book/tools/saa.py ...` child at a time, `--json`, each result logged to `run.log`). It is resumable: a second run skips every job already in the log. `summarize.py` there rebuilds the table below from the files on disk.

New feed files (43): sqs, sns, eventbridge, step-functions, mq, api-gateway, kinesis-data-streams, data-firehose, msk, athena, glue, lake-formation, emr, opensearch, quick, data-exchange, comprehend, lex, polly, rekognition, sagemaker-ai, textract, transcribe, translate, kinesis-video-streams, amplify, device-farm, cloudwatch, cloudtrail, x-ray, health-dashboard, managed-grafana, managed-prometheus, cloudformation, service-catalog, license-manager, trusted-advisor, compute-optimizer, dms, application-migration-service, cost-management, cost-explorer, budgets, cost-and-usage-report, billing, savings-plans, elastic-disaster-recovery, application-recovery-controller, service-quotas, whitepapers, prescriptive-guidance, decision-guides.

## Item counts per chapter (files on disk after the run)

Columns: tags / What's New rows across those tags; history pages / history rows across those pages; case tags / case studies in the index carrying those tags. Chapters without any source of these kinds (00, 01, 44, 46-52) are left out.

| ch | slug | tags | What's New items | history pages | history rows | case tags | case studies |
|---|---|---|---|---|---|---|---|
| 02 | aws-map | 3 | 52 | 4 | 38 | 3 | 79 |
| 03 | iam | 3 | 91 | 1 | 66 | 1 | 135 |
| 04 | organizations | 4 | 134 | 3 | 160 | 3 | 90 |
| 05 | identity-federation | 4 | 142 | 3 | 132 | 3 | 133 |
| 06 | kms | 3 | 24 | 2 | 42 | 2 | 86 |
| 07 | secrets-certificates | 4 | 143 | 3 | 181 | 3 | 76 |
| 08 | edge-protection | 4 | 170 | 2 | 308 | 4 | 176 |
| 09 | detection | 7 | 255 | 7 | 659 | 7 | 257 |
| 10 | vpc | 3 | 154 | 1 | 23 | 1 | 238 |
| 11 | vpc-connectivity | 3 | 188 | 3 | 19 | 3 | 291 |
| 12 | hybrid-networking | 4 | 93 | 3 | 20 | 2 | 108 |
| 13 | route53 | 1 | 77 | 1 | 0 | 1 | 179 |
| 14 | elb | 1 | 40 | 3 | 38 | 1 | 232 |
| 15 | cloudfront | 2 | 99 | 2 | 91 | 2 | 416 |
| 16 | ec2 | 1 | 894 | 2 | 251 | 4 | 1741 |
| 17 | auto-scaling | 3 | 47 | 3 | 52 | 2 | 232 |
| 18 | lambda | 1 | 170 | 1 | 29 | 1 | 821 |
| 19 | containers | 5 | 434 | 3 | 306 | 4 | 829 |
| 20 | more-compute | 7 | 159 | 8 | 138 | 7 | 200 |
| 21 | s3 | 3 | 224 | 2 | 83 | 2 | 1475 |
| 22 | ebs | 2 | 76 | 1 | 32 | 1 | 254 |
| 23 | efs-fsx | 6 | 166 | 5 | 221 | 4 | 196 |
| 24 | backup | 1 | 118 | 1 | 132 | 1 | 33 |
| 25 | hybrid-storage | 7 | 133 | 7 | 117 | 9 | 135 |
| 26 | rds | 1 | 389 | 1 | 326 | 5 | 701 |
| 27 | aurora | 1 | 183 | 1 | 129 | 2 | 303 |
| 28 | dynamodb | 1 | 76 | 1 | 65 | 1 | 405 |
| 29 | elasticache | 1 | 59 | 1 | 15 | 3 | 232 |
| 30 | more-databases | 4 | 387 | 5 | 201 | 4 | 438 |
| 31 | messaging | 4 | 168 | 4 | 60 | 3 | 349 |
| 32 | step-functions | 3 | 100 | 4 | 133 | 3 | 111 |
| 33 | api-gateway | 1 | 20 | 1 | 13 | 1 | 238 |
| 34 | streaming | 4 | 182 | 3 | 58 | 4 | 333 |
| 35 | analytics | 8 | 817 | 7 | 434 | 7 | 852 |
| 36 | ai-ml-media | 12 | 535 | 11 | 264 | 12 | 912 |
| 37 | monitoring | 9 | 425 | 7 | 397 | 6 | 498 |
| 38 | deploy-operate | 9 | 287 | 8 | 441 | 7 | 311 |
| 39 | migration | 2 | 61 | 3 | 54 | 2 | 76 |
| 40 | ha-dr | 2 | 24 | 5 | 68 | 1 | 14 |
| 41 | cost | 5 | 208 | 5 | 117 | 4 | 88 |
| 42 | security-patterns | 0 | 0 | 2 | 20 | 0 | 0 |
| 43 | decoupling-scaling | 0 | 0 | 3 | 18 | 0 | 0 |
| 45 | decision-atlas | 0 | 0 | 2 | 21 | 0 | 0 |

Totals across chapters (a tag shared by two chapters is counted in both): 8,004 What's New rows since 2022-07-01, 5,972 history rows since 2022-07-01, 14,273 case-study tag hits. The case index stayed at 4,313 rows: every per-tag harvest found its items already present from the full-directory harvest (0 added each).

## Services for which no tag or history page worked

Real failures (nothing usable from either source):

- **Route 53**: the registered history page `docs/Route53/latest/DeveloperGuide/History` is not a dated table (`changes history` exit 1: "this is not a document-history table"). The What's New tag `amazon-route-53` works (77 rows). A writer who needs Route 53 doc-history dates should look for another page in `index/route53-developerguide.json` (`history_candidates`) or rely on the What's New feed.

Empty by the date cutoff, not an error (exit 0, every item older than 2022-07-01):

- `aws-serverless-application-repository` (19 items, newest 2019; the history page gave 1 row) -> `serverless-application-repository.jsonl` has 1 row.
- `amazon-elastic-transcoder` (15 items, all old; its history page has no dated table) -> `elastic-transcoder.jsonl` stays empty. Both services are effectively frozen; the book should say so from a guide page, not from these feeds.
- `aws-personal-health-dashboard` (6 old items) -> covered by `aws-health` in `health-dashboard.jsonl` (31 rows).
- History pages `vpc/latest/peering/doc-history` (7 rows, all before 2022-07), `textract/latest/dg/document-history` (16 rows, all before the cutoff; What's New covers Textract), `whitepapers/.../disaster-recovery-workloads-on-aws/document-revisions` (5 rows, all before the cutoff).

Warnings (rows kept, some skipped): `devicefarm/.../history` 2 undated rows skipped (8 kept); `awssupport/.../aws-trusted-advisor-change-log` 5 undated rows skipped (25 kept). Both exit 2.

Service ids in the registry with no feed file of their own: `aurora-serverless`, `dax`, `ecs-anywhere`, `eks-anywhere`, `instance-store`, `rds-proxy` (no tag or history page of their own; their parent service's feed covers them), `systems-manager` (its rows are in `parameter-store.jsonl`, tag `aws-systems-manager`, since chapter 07 mapped them first), `well-architected-tool` (rows in `well-architected.jsonl`). `changes for systems-manager` and `changes for well-architected-tool` will therefore exit 3; use `parameter-store` and `well-architected`.

## Notes

- No command was refused and no approval was asked. Nothing outside `aws-saa-book/` changed; `data/book.json`, `_build/work/`, `_build/ledger/` and `data/facts/` were not touched. Files written: `_build/corpus/changes/*.jsonl` (new and merged), `_build/corpus/snap/api/*` and `snap/docs/*` snapshots the tool made, `_build/tmp/harvest-changes/{plan.json,run.py,run.log,results.json,summarize.py,summary.json}`, this report.
- The driver ran one tool process at a time (never two in flight), so the shared limiter and file locks behaved as with hand-typed commands; the whole run took about 20 minutes at roughly one request per second shared with the IAM and VPC agents.
