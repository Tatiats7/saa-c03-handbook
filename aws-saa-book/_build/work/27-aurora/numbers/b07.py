import sys
sys.path.insert(0, "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/27-aurora/numbers")
from mk import *
UG = "docs/AmazonRDS/latest/AuroraUserGuide/"
FAQ = "docs/rds/latest/auroraextendedcontent/"
fs = []
fs.append(F("aurora-free-plan-postgresql-serverless-4-acu-1-gib", "pricing-dimension",
 "The AWS Free Plan gives access to Aurora PostgreSQL serverless instances with up to 4 ACUs and 1 GiB of storage per cluster, and you can upgrade to the Paid plan at any time to scale up to 256 ACUs and 256 TiB of storage.",
 "What limits does the AWS Free Plan put on an Aurora PostgreSQL serverless cluster?",
 [("acu", "up to 4 ACUs", "up to four ACUs"), ("storage", "1 GiB of storage per cluster", "one gibibyte of storage")],
 "per Aurora PostgreSQL serverless cluster on the Free Plan", "max", False, FAQ + "aurora-features-cost-effective",
 "The Free plan gives you access to Aurora PostgreSQL serverless instances with up to 4 ACUs and 1 GiB of storage per cluster. You can upgrade to the Paid plan at any time to scale up to 256 ACUs and 256 TiB of storage.",
 vol="frequently-changing", exam="extended", bullets=["4.3.S3"], note="d27 cost. Aurora PostgreSQL joined the AWS Free Tier on 2026-03-25 (What's New), before the 2026-07-15 cutoff."))
fs.append(F("aurora-global-writer-endpoint-dns-ttl-low-such-as-5-seconds", "behavior",
 "When you use the Aurora Global Database writer endpoint and your application or networking layers cache DNS values, AWS recommends reducing the DNS cache time-to-live (TTL) to a low value such as 5 seconds.",
 "What DNS TTL does AWS suggest for applications that use the global writer endpoint?",
 [("ttl", "low value such as 5 seconds", "about five seconds")],
 "per application using the Aurora Global Database writer endpoint", "", False, UG + "aurora-global-database-disaster-recovery",
 "If you are using the global writer endpoint and your application or networking layers cache DNS values, reduce the time-to-live (TTL) of your DNS cache to a low value such as 5 seconds.",
 exam="reference", bullets=["2.2.S2"], note="extra."))
fs.append(F("aurora-global-failover-rebuild-secondaries-minutes-to-hours", "behavior",
 "After a managed failover, rebuilding the other secondary Region clusters can take a few minutes to several hours, depending on the size of the storage volume and the distance between the Regions.",
 "How long can it take Aurora to rebuild the other secondary Regions after a global database failover?",
 [("rebuild", "a few minutes to several hours", "from minutes to hours")],
 "per Aurora global database managed failover", "", False, UG + "aurora-global-database-disaster-recovery",
 "The duration of the complete rebuilding task can take a few minutes to several hours, depending on the size of the storage volume and the distance between the Regions.",
 exam="reference", bullets=["2.2.S2"], note="extra."))
fs.append(F("aurora-faq-cross-region-binlog-promotion-few-minutes", "behavior",
 "Promoting a cross-Region replica that uses logical (binlog) replication typically takes a few minutes depending on your workload, while promoting a secondary Region of Aurora Global Database takes under a minute.",
 "How long does promoting a cross-Region binlog replica take, compared with Aurora Global Database?",
 [("binlog", "typically takes a few minutes", "a few minutes"), ("global", "in under a minute", "under a minute")],
 "per cross-Region Aurora replica or secondary Region", "", False, FAQ + "aurora-faq-availability-and-durability",
 "Yes. For logical (binlog) replication, the promotion process typically takes a few minutes depending on your workload. With Amazon Aurora Global Database, you can promote a secondary Region to take full read/write workloads in under a minute.",
 exam="extended", bullets=["2.2.S2", "3.3.K7"], note="d27-047."))
fs.append(F("aurora-faq-cross-region-binlog-lag-under-a-minute-typical", "behavior",
 "For Aurora cross-Region replication that uses binlog-based logical replication, lag can grow indefinitely depending on change rate and network delays, but under typical conditions a replication lag of under a minute is common. Aurora Global Database physical replication has a typical lag of under a second.",
 "What replication lag is typical for binlog-based cross-Region replication and for Aurora Global Database?",
 [("binlog", "under a minute of replication lag is common", "under a minute"), ("global", "typical lag of under a second", "under a second")],
 "per cross-Region Aurora replica", "", False, FAQ + "aurora-faq-availability-and-durability",
 "For cross-Region replication, binlog-based logical replication lag can grow indefinitely based on change/apply rate and network delays, but under typical conditions, under a minute of replication lag is common. Cross-Region replicas using Aurora Global Database's physical replication will have a typical lag of under a second.",
 exam="extended", bullets=["3.3.K7", "2.2.S2"], note="d27-046."))
fs.append(F("aurora-faq-cross-region-cluster-up-to-15-replicas", "limit",
 "You can add up to 15 replicas on each cross-Region Aurora cluster; they share the same underlying storage as the cross-Region replica and typically lag behind the primary by tens of milliseconds.",
 "How many replicas can you add to a cross-Region Aurora cluster?",
 [("max", "up to 15 replicas on each cross-Region Aurora cluster", "fifteen replicas")],
 "per cross-Region Aurora cluster", "max", False, FAQ + "aurora-faq-availability-and-durability",
 "Yes, you can add up to 15 replicas on each cross-Region Aurora cluster. They share the same underlying storage as the cross-Region replica and typically lag behind the primary by tens of milliseconds.",
 exam="extended", bullets=["3.3.K7", "3.3.S1"], note="d27-118."))
write("n07.json", fs)
