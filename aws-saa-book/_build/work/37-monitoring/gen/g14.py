from lib import *
facts=[]
facts.append(F("cloudwatch-otel-metrics-otlp-promql-150-labels-15-months-storage","capability",
 "OpenTelemetry metrics in CloudWatch are ingested with OTLP and queried with PromQL; the model supports up to 150 labels per data point and includes 15 months of storage with no per-metric charges.",
 "What do OpenTelemetry metrics in CloudWatch support, and how long is storage included?",
 [("labels","up to 150 labels per data point"),("storage","15 months of storage")],"OpenTelemetry metrics","max",False,"Classic metrics support up to 30 dimensions per metric with per-metric-per-month pricing.",
 [E("docs/AmazonCloudWatch/latest/monitoring/metrics-otel-overview","OpenTelemetry metrics in CloudWatch use the OpenTelemetry Protocol (OTLP) for ingestion and PromQL for querying. This model supports open-source metric names, up to 150 labels per data point, and includes 15 months of storage with no per-metric charges.")],
 vol="frequently-changing",rel="extended",bullets=["2.2.S3"],
 note="Query Studio with PromQL went generally available on 2026-06-15 (cloudwatch-change-query-studio-ga-2026-06). Do not rewrite classic PutMetricData facts as OTel facts."))
facts.append(F("cloudtrail-log-file-validation-digest-file-every-hour","behavior",
 "With log file integrity validation enabled, CloudTrail creates and delivers a digest file every hour that references the log files of the last hour and contains a hash of each.",
 "How often does CloudTrail deliver digest files when log file integrity validation is enabled?",
 [("every","Every hour"),("what","contains a hash of each")],"trails with log file integrity validation","",False,"",
 [E("docs/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro","Every hour, CloudTrail also creates and delivers a file that references the log files for the last hour and contains a hash of each. This file is called a digest file.")],
 rel="extended",bullets=["1.3.S1"],service="cloudtrail"))
dump('../facts-numbers-14.json',facts); print(len(facts))
