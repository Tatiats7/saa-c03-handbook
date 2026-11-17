# Spot check spot-37: chapter 37 (CloudWatch, CloudTrail and X-Ray)

Date: 2026-10-22 (ledger clock 2026-10-23). Checker: Opus spot check after the first entail vote round, before adjudication.
Pool: 646 facts with home_chapter 37 and status mech-pass in cloudwatch, cloudtrail, x-ray, health-dashboard, managed-grafana and managed-prometheus. Seed 20261013 + 37 = 20261050; 30 picked with `random.Random(seed).sample` over the sorted ids. Sample file: `spot-37.sample.json`.

## Result

- Checked: 30
- Not positive (my verdict partial or unsure): 10, all partial
- Voter misses (first-round entail vote `support`, my verdict not positive): 2
- Partials the first-round voter had already caught: 8
- Amended: 10 (all with `--by spot-37`; each now mech-pass at a new rev with no votes, for a fresh vote at adjudication)

## Sample and verdicts

| # | Fact | First-round entail | Spot verdict |
|---|------|--------------------|--------------|
| 1 | cloudtrail-lake-migrate-to-cloudwatch-recommended | partial | partial |
| 2 | cloudwatch-dashboard-cross-account-graph-and-alarms | partial | partial |
| 3 | cloudwatch-ec2-status-check-failed-system-metric-one-minute-free | support | support |
| 4 | cloudtrail-console-trails-are-multi-region | partial | partial |
| 5 | cloudwatch-wa-rel06-synthetic-canaries-monitor-external-endpoints | partial | partial |
| 6 | cloudtrail-advanced-event-selectors-control-costs | support | support |
| 7 | cloudwatch-agent-default-namespace-cwagent | partial | partial |
| 8 | cloudwatch-alarm-missing-data-treatment-options | support | support |
| 9 | managed-prometheus-quota-labels-per-series | support | support |
| 10 | health-dashboard-rebranded-from-phd-and-shd | support | support |
| 11 | cloudwatch-logs-centralize-all-sources-in-one-service | support | support |
| 12 | cloudwatch-pricing-composite-alarm-flat-per-alarm | support | support |
| 13 | x-ray-service-integration-levels-active-passive-header-tooling | support | support |
| 14 | managed-prometheus-faq-powered-by-cortex | support | support |
| 15 | cloudwatch-recommended-alarms-page-lists-metrics-per-service | partial | partial |
| 16 | managed-prometheus-same-data-model-and-promql | support | support |
| 17 | cloudwatch-logs-centralization-rules-managed-by-management-account | support | support |
| 18 | cloudwatch-logs-vended-catalog-route-53-resolver | support | **partial (voter miss)** |
| 19 | cloudwatch-monitoring-guide-three-data-sources | support | support |
| 20 | cloudtrail-digest-file-hourly-hash-of-log-files | support | support |
| 21 | x-ray-pricing-first-1000000-traces-retrieved-or-scanned-free | support | support |
| 22 | cloudtrail-single-region-trail-data-events-regional-resources | support | support |
| 23 | cloudwatch-faq-old-data-console-and-api-granularity | support | **partial (voter miss)** |
| 24 | health-dashboard-api-needs-business-or-enterprise-support | partial | partial |
| 25 | cloudwatch-faq-application-signals-service-maps | support | support |
| 26 | managed-prometheus-pricing-collector-hours-and-samples | support | support |
| 27 | x-ray-sdk-sends-segments-to-daemon-over-udp | support | support |
| 28 | health-dashboard-service-history-last-12-months | partial | partial |
| 29 | cloudwatch-database-insights-database-performance | support | support |
| 30 | cloudtrail-quota-trails-per-region | support | support |

## Non-positive verdicts, with reasons and repairs

1. **cloudwatch-logs-vended-catalog-route-53-resolver** (voter miss). The claim says the page lists the service "among the AWS services that can publish logs to CloudWatch Logs". The table row only names the service and a setup guide. The same table also lists Amazon S3 (server access logs) and Network Load Balancer (access logs), which go to S3, so the table is a catalog of logging setup guides, not a list of CloudWatch Logs publishers. Amended (rev 3): claim says the catalog lists the service with a link to its logging setup guide; the lead sentence "Use the searchable catalog to find an AWS service and open its logging setup guide." added as a quote; question reworded; condition says the row does not state the destination.
2. **cloudwatch-faq-old-data-console-and-api-granularity** (voter miss). The claim matches the quote, but the qualifier scope "metric data older than 63 days" adds a number that is not in the quote or its context (the FAQ example says only "five months back"). A writer reading the scope line could print an unverified number. Amended (rev 2): scope set to the FAQ example; the preceding sentence on retention schedules added as a quote.
3. **cloudtrail-lake-migrate-to-cloudwatch-recommended** (voter caught). The claim dropped "for existing customers"; the closure of CloudTrail Lake to new customers stood only in the surrounding text. Amended (rev 2): added the closure note (May 31, 2026) and "Existing customers can continue to use the service as normal." as verbatim quotes; claim, condition and a date display added.
4. **cloudwatch-dashboard-cross-account-graph-and-alarms** (voter caught). The condition (cross-account observability, in a dashboard in a monitoring account) stood only in the list's lead-in sentence. Amended (rev 2): lead-in sentence added as the first quote.
5. **cloudtrail-console-trails-are-multi-region** (voter caught). The second quote ("This is the default option when you create a trail using the AWS CLI or the CloudTrail API.") does not name its subject; that it means a single-Region trail stands only in the paragraph. Amended (rev 2): second quote and the CLI-default clause dropped; claim narrowed to the first quote; kind changed from default to restriction (M6).
6. **cloudwatch-wa-rel06-synthetic-canaries-monitor-external-endpoints** (voter caught). "With synthetic transactions (user canaries)" stood only in the sentence between the two quotes. Amended (rev 2): first quote extended verbatim through that sentence.
7. **cloudwatch-agent-default-namespace-cwagent** (voter caught). "These metrics" refers to metrics the agent publishes as CloudWatch metrics (previous sentence); metrics forwarded to the OTLP endpoints use no CloudWatch namespace (next paragraph). The claim said "metrics collected by the CloudWatch agent". Amended (rev 2): quote extended with the previous sentence, OTLP sentence added as a second quote, claim and qualifiers scoped.
8. **cloudwatch-recommended-alarms-page-lists-metrics-per-service** (voter caught). "Per AWS service" is not in the quote (only the topic list shows it). Amended (rev 2): claim narrowed to the quote and names the page "Recommended alarms (Classic)".
9. **health-dashboard-api-needs-business-or-enterprise-support** (voter caught). "You need" turns a sufficient condition into a necessary one; the next sentence allows the API with Business, Enterprise On-Ramp or Enterprise Support plans in some Regions or before transition, and the qualifier condition (dashboard needs no plan) stood only nearby. Amended (rev 3): both sentences added as verbatim quotes, claim restated, display for the older plans added.
10. **health-dashboard-service-history-last-12-months** (voter caught). The "Service health page" scope stood only in the surrounding procedure. Amended (rev 2): claim narrowed to the page heading (AWS Health Dashboard) and the quote.

## Notes

- Positive but noted, not amended: cloudtrail-quota-trails-per-region says "an account" and the qualifier "per account"; the quota row says per AWS Region only. Correct reading of a service-quota page, so judged support. cloudtrail-advanced-event-selectors-control-costs and x-ray-pricing-first-1000000-traces-retrieved-or-scanned-free have qualifier scopes ("per trail or event data store", "per account per month") that the page does not state; the claims themselves are carried by the quotes.
- For the adjudicator (outside the sample, not touched): cloudwatch-logs-vended-catalog-cloudfront and cloudwatch-logs-vended-catalog-vpc-flow-logs use the same wording as fact 18 ("among the AWS services that can publish logs to CloudWatch Logs") on the same catalog table, so they likely have the same defect.
- Flag rule (voter misses only): 2 of 30, below the flag threshold of 3. The voter was strict on clause-in-context cases (8 of 8 caught); both misses were scope claims that the quote's table or qualifiers did not carry.
- Patch files: `_build/work/37-monitoring/spot-37/*.json`.
