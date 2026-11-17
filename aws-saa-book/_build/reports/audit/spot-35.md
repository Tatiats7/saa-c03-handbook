# Spot check spot-35: chapter 35 (analytics), Opus, after the first entail round

Date: 2026-10-23. Population: 1,065 facts with home_chapter 35 and status mech-pass. Seed 20261048 (20261013 + 35), 30 picked (`spot-35.sample.json`). Strict ENTAIL test of TOOLS.md 5.4: the quote, in its context and under its heading, must carry every clause, scope, condition and qualifier of the fact.

## Result

- Checked: 30
- Not positive (my partial verdicts): 8
- Voter misses (first-round voter said support, I did not): 5 (flag: 3 or more)
- Partials the voter had already caught (agreed): 3
- Amended: 8 (all 8 non-positive facts, `--by spot-35`; each is now a new rev that needs a fresh vote)

## Sample and verdicts

| # | Fact | Voter | Spot-35 |
|---|---|---|---|
| 1 | athena-change-2023-12-iam-identity-center-workgroups | support | support |
| 2 | athena-cross-account-bucket-policy-grants-access | support | support |
| 3 | athena-decision-use-for-adhoc-sql-no-clusters | support | support |
| 4 | athena-lake-formation-denied-without-access-and-allowed-columns-list | support | support |
| 5 | athena-quota-workgroups-per-account | support | support |
| 6 | athena-reuse-results-not-for-fine-grained-or-lake-formation-tables | support | support |
| 7 | athena-tune-partition-keys-string-type | support | support |
| 8 | data-exchange-faq-aws-account-vs-no-authentication-open-data | support | support |
| 9 | data-exchange-faq-securely-exchange-third-party-data | support | support |
| 10 | emr-6x-yarn-node-labels-disabled-by-default | support | **partial (miss)** |
| 11 | emr-ebs-limit-25-volumes-per-instance | partial | partial |
| 12 | emr-faq-all-nodes-same-availability-zone | support | support |
| 13 | emr-faq-clusters-for-maximum-control | support | support |
| 14 | emr-serverless-larger-workers-2026-07 | support | **partial (miss)** |
| 15 | glue-data-quality-two-entry-points-catalog-reactive-etl-proactive | support | support |
| 16 | glue-faq-flex-not-for-downstream-dependencies | support | support |
| 17 | glue-faq-main-components | support | support |
| 18 | glue-quota-concurrent-job-runs-per-job | support | support |
| 19 | glue-quota-workflows-per-account | support | support |
| 20 | glue-streaming-schema-detection-no-joins | support | support |
| 21 | lake-formation-faq-lf-tbac-admins-set-tags-policies-enforce | support | support |
| 22 | lake-formation-lf-tbac-example-5-assignments-8-grants-17-permissions | partial | partial |
| 23 | lake-formation-what-is-central-govern-secure-share | support | support |
| 24 | opensearch-change-2023-05-multi-az-with-standby | support | support |
| 25 | opensearch-change-2026-08-serverless-10000-collections-per-group | support | **partial (miss)** |
| 26 | opensearch-price-reserved-instances-no-upfront-discounts | support | **partial (miss)** |
| 27 | opensearch-price-serverless-dev-test-half-cost | support | **partial (miss)** |
| 28 | quick-rls-enterprise-restrict-dataset-readers | support | support |
| 29 | quick-spice-in-memory-engine | support | support |
| 30 | quick-vpc-connection-enterprise-edition-private-data | partial | partial |

## Non-positive verdicts, reasons and repairs

1. **emr-6x-yarn-node-labels-disabled-by-default** (voter miss). The claim's clause "unless you enable it" stood only in the next sentence of the note ("You can enable the YARN node labels feature by configuring following properties"). Amended (rev 3): quote extended to that sentence; claim states the two defaults plus "you can enable the YARN node labels feature by configuring properties".
2. **emr-ebs-limit-25-volumes-per-instance** (voter caught it). The quote "There is a limit of 25 volumes per instance." does not name EBS or EMR; the scope stands only in the list lead-in. Amended (rev 2): lead-in sentence "Keep in mind these additional considerations when you use Amazon EBS with EMR clusters:" added as evidence; claim worded to match.
3. **emr-serverless-larger-workers-2026-07** (voter miss). The qualifier condition "Available in all AWS Regions where EMR Serverless is available" stood only in the last paragraph of the page, not in a quote; the condition also held an editorial remark. Amended (rev 2): the sentence "Larger workers are available in all AWS Regions where EMR Serverless is available." added as a third evidence item; the cutoff remark moved to `note`.
4. **lake-formation-lf-tbac-example-5-assignments-8-grants-17-permissions** (voter caught it). The scope "3 principals, 3 databases, 7 tables" stood only in the context. Amended (rev 3): the sentence "Consider the case where you must grant permissions to three principals on three databases and seven tables." added as evidence.
5. **opensearch-change-2026-08-serverless-10000-collections-per-group** (voter miss). Qualifier `adjustable: true` has no support anywhere on the page (the What's New post never says the limit is adjustable). Amended (rev 2): `adjustable` set to false (not stated); claim and quotes unchanged.
6. **opensearch-price-reserved-instances-no-upfront-discounts** (voter miss). Universal claim "one-year NURIs offer a 31% discount, three-year 48%" while the exception "For T3.medium, one-year NURIs offer a 18% discount and three-year NURIs offer a 28% discount" stands in the same bullet, outside the quote. Amended (rev 2): quote extended to the T3.medium sentence; claim and values carry the exception (18% and 28% added as values).
7. **opensearch-price-serverless-dev-test-half-cost** (voter miss). The scope "Classic collections" and the condition "the minimum varies based on your data size and collections type in use" stood only in the context. Amended (rev 2): the dev-test quote extended through "However, the minimum varies based on your data size and collections type in use."; the Classic-collections sentence added as evidence; claim names both.
8. **quick-vpc-connection-enterprise-edition-private-data** (voter caught it). The quotes named only the Quick network interfaces and their security group; Enterprise edition, the data source subnets and the route table were not in any quote. Amended (rev 3): claim rewritten to the page's component list, with evidence for the Enterprise edition sentence, the "components work together to allow network traffic to pass between Amazon Quick and your data source" sentence, the data source subnets, the Quick ENIs and their subnets, and the Quick ENI security group. The route table was dropped from the claim (a three-word list item fails M4).

## Borderline facts judged positive

- athena-cross-account-bucket-policy-grants-access: the KMS sub-section nearby adds key-policy and IAM-role steps for a custom-key bucket, but the claim does not say a bucket policy is sufficient or the only step; it restates the quote.
- glue-quota-concurrent-job-runs-per-job and glue-quota-workflows-per-account: the claim says "maximum of N" for a value in the Default column, but the same sentence says the quota is adjustable and the row's own description says "The maximum number of ..."; not a default-versus-maximum error.

## Notes for the adjudicator

- All 8 amended facts are mech-pass at a new rev with empty votes; spot-35 is an amender and cannot vote on them.
- The flag rule counts voter misses: 5 of 30 here, so this chapter is flagged. The misses are qualifier-level (conditions, exceptions and an unsupported `adjustable` flag) more than claim-level, which suggests the first-round voters read the claim sentence and skipped the qualifier fields.
- Patch files: `aws-saa-book/_build/work/35-analytics/spot-35/*.json`.
