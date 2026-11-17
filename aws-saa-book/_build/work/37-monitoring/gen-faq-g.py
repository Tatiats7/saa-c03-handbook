from importlib.machinery import SourceFileLoader
L = SourceFileLoader("lib", "aws-saa-book/_build/work/37-monitoring/gen-faq-lib.py").load_module()
F, emit = L.F, L.emit
S = "cloudwatch"
B = ["2.2.S3", "3.2.S2"]
Q = "What is the retention period of all metrics?"
facts = [
F(S, "faq-retention-under-60-seconds-3-hours", "limit",
  "CloudWatch keeps data points with a period of less than 60 seconds for 3 hours.",
  Q, ["less than 60 seconds", "available for 3 hours"],
  "Data points with a period of less than 60 seconds are available for 3 hours.",
  "per data point, period under 60 seconds", B, "cw", dm="fixed", tier0=True),
F(S, "faq-retention-60-seconds-15-days", "limit",
  "CloudWatch keeps data points with a period of 60 seconds (1 minute) for 15 days.",
  Q, ["60 seconds (1 minute)", "available for 15 days"],
  "Data points with a period of 60 seconds (1 minute) are available for 15 days",
  "per data point, period 60 seconds", B, "cw", dm="fixed", tier0=True),
F(S, "faq-retention-300-seconds-63-days", "limit",
  "CloudWatch keeps data points with a period of 300 seconds (5 minute) for 63 days.",
  Q, ["300 seconds (5 minute)", "available for 63 days"],
  "Data points with a period of 300 seconds (5 minute) are available for 63 days",
  "per data point, period 300 seconds", B, "cw", dm="fixed", tier0=True),
F(S, "faq-retention-3600-seconds-455-days", "limit",
  "CloudWatch keeps data points with a period of 3600 seconds (1 hour) for 455 days (15 months).",
  Q, ["3600 seconds (1 hour)", "455 days (15 months)"],
  "Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months)",
  "per data point, period 3600 seconds", B, "cw", dm="fixed", tier0=True),
F("x-ray", "faq-trace-same-trace-id", "behavior",
  "An X-Ray trace is a set of data points sharing the same trace ID as a request travels through application services.",
  "What is a trace in X-Ray?", ["same trace ID", "as a request travels through application services"],
  "A set of data points sharing the same trace ID as a request travels through application services.",
  "AWS X-Ray concepts", ["2.2.K12"], "cw", tier0=True),
F("x-ray", "faq-annotation-definition", "behavior",
  "In X-Ray, an annotation is system-defined or user-defined metadata associated with a segment.",
  "What is an annotation in X-Ray?", ["System-defined or user-defined metadata", "associated with a segment"],
  "Annotation: System-defined or user-defined metadata associated with a segment.",
  "AWS X-Ray concepts", ["2.2.K12"], "cw", rel="extended"),
]
emit("facts-faq-07.json", facts)
