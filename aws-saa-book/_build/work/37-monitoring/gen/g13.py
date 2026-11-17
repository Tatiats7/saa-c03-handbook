from lib import *
facts=[]
facts.append(F("cloudwatch-graph-max-500-metrics-and-expressions","limit",
 "Each CloudWatch graph is limited to a maximum of 500 metrics and expressions, so a math expression can be added only if the graph has 499 or fewer metrics.",
 "How many metrics and expressions can one CloudWatch graph use?",
 [("max","maximum of 500 metrics and expressions"),("add","499 or fewer metrics")],"per graph","max",False,"Applies even if not all the metrics are displayed on the graph.",
 [E("docs/AmazonCloudWatch/latest/monitoring/using-metric-math","Each graph is limited to using a maximum of 500 metrics and expressions, so you can add a math expression only if the graph has 499 or fewer metrics.")],
 rel="extended",bullets=["2.2.S3"]))
facts.append(F("cloudwatch-getmetricdata-default-max-datapoints-100800","default",
 "If you omit MaxDatapoints in a GetMetricData request, the default of 100,800 data points is used before the response paginates.",
 "What is the default number of data points a GetMetricData request returns before paginating?",
 [("default","default of 100,800")],"per GetMetricData request","default",True,"",
 [E("docs/AmazonCloudWatch/latest/APIReference/API_GetMetricData","The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.")],
 rel="reference",bullets=["2.2.S3"],
 note="Not found: a limit on the number of metrics per GetMetricData call; the API reference page only mentions the message 'Maximum number of allowed metrics exceeded'."))
facts.append(F("cloudwatch-alarm-mute-rule-targets-up-to-100-alarms","limit",
 "A single alarm mute rule can target up to 100 alarms by alarm names.",
 "How many alarms can one CloudWatch alarm mute rule target by name?",
 [("max","up to 100 alarms")],"per alarm mute rule","max",False,"By alarm names.",
 [E("docs/AmazonCloudWatch/latest/monitoring/alarm-mute-rules","A single alarm mute rule can target up to 100 alarms by alarm names.")],
 rel="reference",bullets=["3.2.S2"],vol="frequently-changing"))
facts.append(F("cloudwatch-metrics-without-new-data-hidden-in-console-two-weeks","behavior",
 "Metrics that have had no new data points in the past two weeks do not appear in the console; retrieve them with get-metric-data or get-metric-statistics.",
 "Why does an old CloudWatch metric not show up in the console, and how can you still get its data?",
 [("hidden","no new data points in the past two weeks"),("how","get-metric-data")],"per metric","",False,"",
 [E("docs/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts","Metrics that have not had any new data points in the past two weeks do not appear in the console.")],
 rel="reference",bullets=["2.2.S3"],note="The same note adds that such metrics are not returned by list-metrics; the best way to retrieve them is get-metric-data or get-metric-statistics."))
facts.append(F("cloudwatch-database-insights-standard-7-days-included-retention-1-to-24-months","pricing-dimension",
 "CloudWatch Database Insights Standard Mode includes up to 7 days of detailed database and per-query metrics retention at no additional cost; beyond that, retention can be configured from 1 to 24 months.",
 "How long does Database Insights Standard Mode keep metrics at no extra cost, and how far can retention be extended?",
 [("incl","Up to 7 days"),("ext","from 1 to 24 months")],"per database","",False,"",
 [E("www/cloudwatch/pricing","Up to 7 days of detailed database and per-query metrics retention is included at no additional cost. Beyond that, retention can be configured from 1 to 24 months.")],
 tier=2,vol="frequently-changing",rel="reference",bullets=["2.2.S3"]))
SID="www/about-aws/whats-new/2026/05/cloudwatch-logs-query-results"
facts.append(F("cloudwatch-logs-change-insights-query-results-100000-2026-05","change",
 "On May 15, 2026 CloudWatch Logs Insights raised the number of results a query can retrieve to 100,000 (set with the LIMIT command); before that, queries were limited to 10,000 results.",
 "When did Logs Insights raise the maximum number of query results, and what was the old limit?",
 [("date","May 15, 2026"),("new","up to 100,000 results"),("old","limited to 10,000 results")],"per Logs Insights query","",False,"GetQueryResults returns up to 10,000 results per call and paginates.",
 [E(SID,"Posted on: May 15, 2026",None,"Amazon CloudWatch Logs announces increased query result limits"),
  E(SID,"Previously, customers were limited to 10,000 results and had to split their queries into smaller time ranges to retrieve all results.")],
 tier=3,vol="changed-since-2022",changed={"date":"2026-05-15","was":"10,000 results","was_evidence":1},rel="reference",bullets=["1.3.S1"],ci=[chg('2026/05/cloudwatch-logs-query-results')],
 note="Only this What's New post states the new result limit; the Logs Insights guide page saved here does not. Examinable by the date rule (before 2026-07-15) but new."))
dump('../facts-numbers-13.json',facts); print(len(facts))
