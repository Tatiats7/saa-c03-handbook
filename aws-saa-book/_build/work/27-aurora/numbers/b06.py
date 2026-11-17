import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/numbers")
from mk import *
UG = "docs/AmazonRDS/latest/AuroraUserGuide/"
FAQ = "docs/rds/latest/auroraextendedcontent/"
fs = []
fs.append(F("aurora-throughput-up-to-6x-stock-mysql-and-postgresql", "behavior",
 "Aurora delivers up to 6x the throughput of stock PostgreSQL and up to 6x the throughput of stock MySQL on similar hardware.",
 "What throughput advantage does AWS claim for Aurora compared with stock MySQL and stock PostgreSQL on similar hardware?",
 [("mysql", "up to 6x the throughput of stock MySQL", "up to six times the throughput of MySQL"), ("postgres", "up to 6x the throughput of stock PostgreSQL", "up to six times the throughput of PostgreSQL")],
 "Aurora MySQL and Aurora PostgreSQL compared with stock engines on similar hardware", "max", False, UG + "CHAP_AuroraOverview",
 "Aurora delivers up to 6x the throughput of stock PostgreSQL and up to 6x the throughput of stock MySQL on similar hardware.",
 cond="benchmark claim; older material and the database decision guide say up to five times (MySQL) and up to three times (PostgreSQL)",
 more=[(FAQ + "aurora-features-performance", "Testing on standard benchmarks such as SysBench has shown an increase in throughput of up to 6x over stock PostgreSQL and stock MySQL on similar hardware.")],
 vol="frequently-changing", exam="core", bullets=["3.3.S2", "3.3.S4"], note="d27-002. The Aurora User Guide, FAQ and features page all say 6x; the expected 5x and 3x figures are not in those pages."))
fs.append(F("aurora-replicas-up-to-15-in-addition-to-primary", "limit",
 "Each Aurora DB cluster can have up to 15 Aurora Replicas in addition to the primary DB instance.",
 "How many Aurora Replicas can each Aurora DB cluster have in addition to the primary DB instance?",
 [("max", "up to 15 Aurora Replicas in addition to the primary DB instance", "fifteen Aurora Replicas besides the primary")],
 "per Aurora DB cluster", "max", False, UG + "Aurora.Overview",
 "Each Aurora DB cluster can have up to 15 Aurora Replicas in addition to the primary DB instance.",
 cond="the read replicas per primary quota cannot be adjusted for Amazon Aurora",
 more=[(UG + "Aurora.Replication", "An Aurora DB cluster can contain up to 15 Aurora Replicas.")],
 exam="core", bullets=["3.3.S1", "3.3.K7", "2.1.K15"], note="d27-004."))
fs.append(F("aurora-cluster-volume-max-256-tib-overview", "limit",
 "An Aurora cluster volume can grow to a maximum size of 256 tebibytes (TiB).",
 "What is the maximum size an Aurora cluster volume can grow to, according to the Aurora overview?",
 [("max", "maximum size of 256 tebibytes (TiB)", "two hundred fifty-six tebibytes")],
 "per Aurora DB cluster volume", "max", False, UG + "CHAP_AuroraOverview",
 "An Aurora cluster volume can grow to a maximum size of 256 tebibytes (TiB).",
 cond="engine-version dependent: the quotas and constraints page lists a 128 TiB maximum for earlier engine versions",
 vol="frequently-changing", exam="core", bullets=["3.3.S2"], note="d27-008."))
fs.append(F("aurora-custom-endpoint-name-max-63-characters", "limit",
 "The maximum length for an Aurora custom endpoint name is 63 characters.",
 "What is the maximum length of an Aurora custom endpoint name?",
 [("max", "63 characters", "sixty-three characters")],
 "per custom endpoint name", "max", False, UG + "Aurora.Endpoints.Custom.Considerations",
 "The maximum length for a custom endpoint name is 63 characters.",
 exam="reference", bullets=["3.3.S1"], note="d27-021."))
fs.append(F("aurora-features-replica-lag-single-digit-milliseconds", "behavior",
 "AWS states that Aurora read replicas share the same underlying storage as the primary instance and reduce the replica lag time, often down to single-digit milliseconds.",
 "What replica lag does the Aurora features page state for read replicas?",
 [("lag", "often down to single-digit milliseconds", "often single-digit milliseconds")],
 "per Aurora read replica in the same cluster", "", False, FAQ + "aurora-features-scalability",
 "This frees up more processing power to serve read requests and reduces the replica lag time—often down to single-digit milliseconds.",
 cond="typical value",
 exam="extended", bullets=["3.3.K7"], note="d27-023."))
fs.append(F("aurora-performance-guide-replica-lag-considerably-under-100-ms", "behavior",
 "You can achieve read scaling by creating up to 15 Aurora Replicas in a DB cluster. Each Aurora Replica returns the same data from the cluster volume with minimal replica lag, usually considerably less than 100 milliseconds after the primary instance has written an update.",
 "How many Aurora Replicas can you create for read scaling, and what lag does the User Guide state?",
 [("lag", "considerably less than 100 milliseconds", "well under a hundred milliseconds")],
 "per Aurora DB cluster", "max", False, UG + "Aurora.Managing.Performance",
 "You can achieve read scaling for your Aurora DB cluster by creating up to 15 Aurora Replicas in a DB cluster. Each Aurora Replica returns the same data from the cluster volume with minimal replica lag—usually considerably less than 100 milliseconds after the primary instance has written an update.",
 exam="core", bullets=["3.3.S1", "3.3.K7"], note="d27-004, d27-023."))
fs.append(F("aurora-replicas-need-not-match-primary-instance-class", "behavior",
 "Aurora Replicas do not have to be of the same DB instance class as the primary instance, although AWS recommends the same class for high-availability replicas.",
 "Must an Aurora Replica use the same DB instance class as the primary instance?",
 [("class", "don't have to be of the same DB instance class as the primary instance")],
 "per Aurora Replica", "", False, UG + "Aurora.Managing.Performance",
 "Aurora Replicas don't have to be of the same DB instance class as the primary instance.",
 more=[(UG + "Aurora.Replication", "These should be of the same DB instance class as the primary instance and in different Availability Zones for your Aurora DB cluster.")],
 exam="extended", bullets=["3.3.S1", "2.2.K6"], note="d27-026."))
fs.append(F("aurora-optimized-reads-postgresql-8x-latency-30-percent-savings", "behavior",
 "Optimized reads for Aurora PostgreSQL delivers up to 8x improved query latency and up to 30% cost savings compared to instances without it.",
 "What improvements does optimized reads for Aurora PostgreSQL deliver?",
 [("latency", "up to 8x improved query latency", "up to eight times better query latency"), ("savings", "up to 30% cost savings", "up to thirty percent cost savings")],
 "Aurora PostgreSQL instances with optimized reads", "max", False, FAQ + "aurora-faq-performance",
 "Optimized reads for Aurora PostgreSQL delivers up to 8x improved query latency and up to 30% cost savings compared to instances without it.",
 exam="reference", bullets=["3.3.S2"], note="extra."))
write("n06.json", fs)
