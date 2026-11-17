import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/numbers")
from mk import *
UG = "docs/AmazonRDS/latest/AuroraUserGuide/"
SV = "aurora-serverless"
fs = []
fs.append(F("aurora-serverless-acu-about-2-gib-memory", "limit",
 "Each Aurora capacity unit (ACU) is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking.",
 "How much memory does one Aurora capacity unit (ACU) provide?",
 [("memory", "approximately 2 gibibytes (GiB) of memory", "about two gibibytes of memory")],
 "per ACU of Aurora Serverless", "fixed", False, UG + "aurora-serverless-v2.how-it-works",
 "Each ACU is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking.",
 svc=SV, exam="core", bullets=["3.3.K8", "4.3.S3"], note="d27-075."))
fs.append(F("aurora-serverless-cluster-cache-management-not-available", "restriction",
 "The cluster cache management feature for Aurora PostgreSQL is not available for Aurora Serverless DB instances; the apg_ccm_enabled configuration parameter does not apply to them.",
 "Is Aurora PostgreSQL cluster cache management available for Aurora Serverless DB instances?",
 [("no", "doesn't apply to Aurora serverless DB instances")],
 "per Aurora Serverless DB instance", "", False, UG + "aurora-serverless-v2.requirements",
 "Cluster cache management for Aurora PostgreSQL. The `apg_ccm_enabled` configuration parameter doesn't apply to Aurora serverless DB instances.",
 svc=SV, exam="reference", bullets=["3.3.K8"], note="d27-084."))
write("n05.json", fs)
