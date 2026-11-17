"""adjudicate-35: repair or reject the disputed facts of chapter 35 through the saa.py CLI, one command at a time.
Each repair narrows the claim and qualifiers to what the quotes carry, or adds the quote that carries the missing
clause, scope or exception. Patches go to adj-patches/<id>.json; a log goes to adj-apply-log.jsonl.
A rerun skips the steps that already succeeded. Usage: python3 adj_apply.py [--dry] [ID ...]"""
import copy, json, os, subprocess, sys

REPO = "/Users/tatiatsmindashvili/Desktop/tatia/2026-plans"
ROOT = REPO + "/aws-saa-book"
W = ROOT + "/_build/work/35-analytics/"
PD = W + "adj-patches/"
LOG = W + "adj-apply-log.jsonl"
BY = "adjudicate-35"
SERVICES = ["athena", "glue", "lake-formation", "emr", "opensearch", "quick", "data-exchange"]

R = "reject"

SPEC = {
 "athena-acid-compatible-with-emr-and-spark-shared-formats": {"qual": {"scope": "Athena ACID transactions"}},
 "athena-acid-no-custom-locking-delete-for-erasure": {"qual": {"scope": "Athena ACID transactions"}},
 "athena-adhoc-queries-no-load-needed": {"claim": "You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena."},
 "athena-capacity-100-reservations-1000-dpus": {
   "claim": "You can create up to 100 Athena capacity reservations with up to 1,000 total DPUs per account and Region; if you require more than 1,000 DPUs for your use case, you reach out to athena-feedback@amazon.com.",
   "replace_ev": {0: "You can create up to 100 capacity reservations with up to 1,000 total DPUs per account and region. If you require more than 1,000 DPUs for your use case, please reach out to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com?subject=Athena Provisioned Capacity DPU Limit Request)."},
   "qual": {"condition": "", "adjustable": True}},
 "athena-capacity-dpu-definition-compute-and-memory": {"claim": "One DPU typically provides 4 vCPUs and 16 GB of memory, and the number of DPUs that you hold in Athena capacity reservations influences the number of queries that you can run concurrently."},
 "athena-capacity-min-4-dpus": {"qual": {"condition": ""}},
 "athena-change-2022-10-engine-version-3": {"qual": {"scope": "Athena engine version 3", "condition": ""}},
 "athena-change-2023-04-capacity-reservations": {"qual": {"condition": ""}},
 "athena-change-2025-06-managed-query-results": {"qual": {"condition": ""}},
 "athena-change-2026-02-capacity-1-minute-4-dpu": {"qual": {"condition": ""}},
 "athena-change-2026-04-managed-federated-connectors": {"qual": {"condition": ""}},
 "athena-cloudtrail-query-in-place-in-s3-two-ways": {"claim": "You can create Athena tables for CloudTrail log files directly from the CloudTrail console, or by manually creating tables for CloudTrail log files in the Athena console."},
 "athena-compression-zlib-default-orc-gzip-default-parquet-text": {
   "claim": "For Hive tables in Athena engine versions 2 and 3, and Iceberg tables in Athena engine version 2, GZIP is the default write compression format for files in the Parquet and text file storage formats.",
   "drop_values": ["orc"], "drop_ev": [1],
   "qual": {"scope": "Parquet and text files of Hive tables (engine versions 2 and 3) and Iceberg tables (engine version 2)"}},
 "athena-ctas-insert-into-workaround-up-to-100-each": {"qual": {"condition": ""}},
 "athena-ctas-write-limit-100-partitions": {"qual": {"condition": ""}},
 "athena-datalake-wp-cleaned-zone-permanent-original-format-replay": {
   "replace_ev": {0: "**Cleaned zone** – After the preliminary quality checks, the data from the raw zone is moved to the cleaned zone for permanent storage where the data is stored in its original format. Having all data from all sources permanently stored in the cleaned zone provides the ability to replay downstream data processing in case of errors or data loss in downstream storage zones."}},
 "athena-datalake-wp-in-place-query-no-extra-infrastructure-pay-per-query": {"claim": "Users can query S3 data without any additional infrastructure, and only pay for the queries that they run."},
 "athena-datalake-wp-raw-zone-transient-as-is": {
   "replace_ev": {0: "**Raw zone** – The storage area where components from the ingestion layer land data. This is a transient area where data is ingested from sources as-is."}},
 "athena-datalake-wp-s3-decouples-storage-from-compute-one-copy": {"claim": "With Amazon S3 as the data lake storage platform, storage is decoupled from compute and data processing (in traditional Hadoop and data warehouse solutions, storage and compute are tightly coupled), and multiple users can run different analytical tools against the same copy of the data."},
 "athena-datalake-wp-six-logical-layers": {"claim": "You can think of a data lake centric analytics architecture as a stack of six logical layers, where each layer is composed of multiple components."},
 "athena-decision-guide-serverless-abstracts-infrastructure-auto-scales": {"claim": "According to the AWS analytics decision guide, serverless services abstract infrastructure management, relieving users from provisioning, scaling and maintenance tasks, and automatically scale resources based on workload demands."},
 "athena-dml-timeout-max-240": {"qual": {"condition": ""}},
 "athena-faq-catalog-glue-data-catalog": {
   "claim": "Athena for SQL uses a managed AWS Glue Data Catalog to store information and schemas about the databases and tables that you create for your data stored in S3; in Regions where AWS Glue is not available, Athena uses an internal catalog.",
   "add_ev": ["In Regions where AWS Glue is not available, Athena uses an internal catalog."]},
 "athena-faq-less-data-scanned-pay-less": {
   "claim": "With per query billing, Athena charges based on the amount of data scanned per query, so if you compress your data, partition it, or convert it to a columnar storage format, you pay less because your queries scan less data; with Capacity Reservations, you pay an hourly price for query processing capacity, not data scanned.",
   "add_ev": ["With per query billing, Athena charges based the amount of data scanned per query.",
              "With Capacity Reservations, you pay an hourly price for query processing capacity, not data scanned."],
   "qual": {"scope": "Athena per query billing"}},
 "athena-faq-optimize-data-also-for-capacity-reservations": {
   "claim": "Compressing, partitioning and converting data into columnar formats each reduce the amount of data scanned and the time required for execution, and these operations are also recommended when using Capacity Reservations, because they often reduce the amount of time a query spends executing.",
   "replace_ev": {0: "With per query billing, you can save 30% to 90% per query and get better performance by compressing, partitioning, and converting your data into columnar formats. Each of these operations reduces the amount of data scanned and time required for execution. These operations are also recommended when using Capacity Reservations, because they often reduce the amount of time a query spends executing."}},
 "athena-lens-right-tool-for-the-job-purpose-built-services": {"claim": "AWS has multiple analytics processing services that are built for specific purposes, including Amazon Redshift for data warehousing, Amazon Kinesis for streaming data, and Quick for data visualization."},
 "athena-limits-string-partition-type-prunes-at-metastore": {"claim": "Athena may time out when querying a table that has many thousands of partitions, which can happen when the table has many partitions that are not of type string. With type string, Athena prunes partitions at the metastore level; with other data types, Athena prunes partitions on the server side."},
 "athena-managed-results-console-download-over-200mb-use-unload": {
   "claim": "When you use Athena managed query results, you cannot download query result files larger than 200 MB from the console; use the UNLOAD statement to write results larger than 200 MB to a location that you can download separately.",
   "qual": {"scope": "console download of query result files with managed query results"}},
 "athena-results-location-from-workgroup-and-client-settings": {
   "claim": "The query result location that Athena uses is determined by a combination of workgroup settings and client-side settings. Each workgroup configuration has an Override client-side settings option; when it is enabled, the workgroup settings take precedence over the applicable client-side settings when an IAM principal associated with that workgroup runs the query.",
   "add_ev": ["Each workgroup configuration has an Override client-side settings option that can be enabled."]},
 "athena-service-logs-datasets-you-can-query": {"claim": "Athena can query popular AWS service log datasets, such as AWS CloudTrail logs, Amazon CloudFront logs, Classic Load Balancer logs, Application Load Balancer logs, Amazon VPC flow logs, and Network Load Balancer logs."},
 "athena-sla-monthly-uptime-99-9": {"qual": {"condition": "AWS uses commercially reasonable efforts."}},
 "athena-tune-combine-small-files-before-they-are-written": {"claim": "The best time to combine small files is before they are written; you can also put files in a location on Amazon S3, use a tool like Glue ETL to combine them into larger files, and then move the larger files into the location that the table points to."},
 "athena-tune-explain-shows-partitions-scanned": {"claim": "You can check in advance which partitions an Athena query will scan by using the EXPLAIN statement."},
 "athena-tune-unload-for-large-result-sets": {
   "claim": "When a query finishes, Athena stores the result as a single uncompressed CSV file on Amazon S3, which takes longer than UNLOAD because the result is uncompressed and the operation cannot be parallelized; UNLOAD writes results directly from the worker nodes and makes full use of the parallelism of the compute cluster.",
   "qual": {"condition": ""}},
 "athena-vpc-endpoint-also-glue-endpoint-and-policy": {"claim": "You can improve the security posture of your VPC by using an interface VPC endpoint (AWS PrivateLink) for Athena and an AWS Glue VPC endpoint; for trusted identities, use the aws:PrincipalOrgId condition to restrict access to credentials that are part of your AWS organization."},
 "athena-vpc-flow-logs-query-gzip-directly": {
   "claim": "Amazon VPC flow logs capture information about the IP traffic going to and from network interfaces in a VPC, and the logs are created in a GZIP compression format that Athena lets you query directly.",
   "qual": {"condition": ""}},
 "athena-whitepaper-ideal-ad-hoc-web-log-queries": {"claim": "The big data analytics whitepaper gives the example of using Athena to run a query on web and application logs to troubleshoot a performance issue, and says Athena integrates with Amazon Quick for easy visualization."},
 "athena-workgroup-per-query-limit-range-10mb-7eb": {
   "claim": "For the per-query data usage control of an Athena workgroup (only one per workgroup, applying to each query that runs in it), you edit the Data scanned limit and specify a value between 10 MB (minimum) and 7 EB (maximum).",
   "add_ev": ["You can create only one per-query control limit in a workgroup and it applies to each query that runs in it.",
              "Edit the value for **Data scanned limit**."],
   "qual": {"scope": "Data scanned limit of the per-query control limit of an Athena workgroup", "condition": ""}},
 "athena-workgroups-workgroup-limit-hourly-daily-aggregates": {
   "claim": "The workgroup-wide query limit lets you set multiple thresholds on hourly or daily aggregates on data scanned by queries running in the workgroup.",
   "drop_values": ["disable"], "drop_ev": [1]},
 "data-exchange-api-assets-proxied-through-managed-endpoints": {"claim": "With AWS Data Exchange, you can make API calls to AWS Data Exchange-managed endpoints, which are then proxied through to API-owner endpoints."},
 "data-exchange-change-2023-12-data-grants": {"qual": {"condition": ""}},
 "data-exchange-limit-cross-region-export-1000-gb": {"qual": {"condition": ""}},
 "data-exchange-open-data-300-free-datasets-not-maintained-by-aws": {"claim": "The Open Data on AWS program is a collection of over 300 free, publicly available data sets, and unless specifically stated in the applicable data set documentation, data sets available through the Registry of Open Data on AWS are not provided and maintained by AWS."},
 "data-exchange-price-data-grants-hourly": {"qual": {"condition": ""}},
 "data-exchange-price-provider-tiered-fulfillment-fees": {"qual": {"condition": ""}},
 "data-exchange-price-s3-data-access-requester-pays": {"qual": {"condition": ""}},
 "data-exchange-price-storage-byte-hours": {"qual": {"scope": "storage of data loaded to AWS Data Exchange", "condition": ""}},
 "data-exchange-quota-assets-per-revision": {R: "The General Reference table gives lower type-specific per-revision quotas (20 Lake Formation, API Gateway and Redshift datashare assets, 5 S3 data access assets) next to this row; the general 10,000 claim does not carry them, and the quota has no exam value."},
 "data-exchange-quota-assets-per-s3-export-job": {"qual": {"condition": ""}},
 "data-exchange-quota-revisions-per-data-set": {R: "Nearby rows give lower type-specific revision quotas that the general 10,000 claim does not carry; no exam value."},
 "emr-app-master-runs-only-on-core-nodes-default": {
   "claim": "Amazon EMR has default functionality that allows application master processes to run only on core nodes, so that running jobs do not fail when task nodes running on Spot Instances are terminated. Beginning with the Amazon EMR 6.x release series, the YARN node labels feature is disabled by default, and application primary processes can run on both core and task nodes by default.",
   "add_ev": ["Beginning with Amazon EMR 6.x release series, the YARN node labels feature is disabled by default. The application primary processes can run on both core and task nodes by default."],
   "qual": {"scope": "Amazon EMR on EC2 YARN scheduling of application master processes"}},
 "emr-billing-starts-when-cluster-ready": {"qual": {"condition": ""}},
 "emr-bpa-accounts-after-july-2019-on-before-off": {"qual": {"scope": "per AWS account, by account age"}},
 "emr-faq-failed-master-replaced-same-config": {
   "claim": "In an EMR cluster (version 5.23 or later) launched with three master nodes, in the event of a failover Amazon EMR automatically replaces the failed master node with a new master node with the same configuration and boot-strap actions.",
   "add_ev": ["You can launch an EMR cluster (version 5.23 or later) with three master nodes and support high availability of applications like YARN Resource Manager, HDFS Name Node, Spark, Hive, and Ganglia."],
   "qual": {"scope": "EMR on EC2 clusters with three master nodes", "condition": ""}},
 "emr-faq-failover-to-standby-master": {
   "claim": "In an EMR cluster (version 5.23 or later) launched with three master nodes, Amazon EMR automatically fails over to a standby master node if the primary master node fails or if critical processes, like Resource Manager or Name Node, crash.",
   "add_ev": ["You can launch an EMR cluster (version 5.23 or later) with three master nodes and support high availability of applications like YARN Resource Manager, HDFS Name Node, Spark, Hive, and Ganglia."],
   "qual": {"scope": "EMR on EC2 clusters with three master nodes", "condition": ""}},
 "emr-faq-s3-access-user-role-mapper": {R: "The FAQ says the next sentence: the feature is available only through AWS Labs; an AWS Labs tool is not an EMR feature for the exam, and the claim without that scope is not supported."},
 "emr-faq-spot-instances-emr-on-ec2-eks-more-cost-effective": {
   "claim": "Compared with EMR Serverless: if you run EMR clusters on EC2 On-Demand Instances, EMR Serverless offers a lower total cost of ownership (TCO) if your cluster utilization is less than 70%; with EC2 Savings Plans, if utilization is less than 50%; and if you use EC2 Spot Instances, Amazon EMR on EC2 and Amazon EMR on EKS continue to be more cost effective.",
   "replace_ev": {0: "If you are running EMR clusters using EC2 On-Demand Instances, EMR Serverless will offer a lower total cost of ownership (TCO) if your current cluster utilization is less than 70%. If you are using the EC2 Savings Plans, EMR Serverless will offer a lower TCO if your current cluster utilization is less than 50%. And if you use EC2 Spot Instances, Amazon EMR on EC2 and Amazon EMR on EKS will continue to be more cost effective."},
   "qual": {"scope": "cost of EMR Serverless compared with EMR on EC2 and EMR on EKS"}},
 "emr-fleet-allocation-strategies-capacity-optimized-lowest-price": {
   "claim": "Instance fleets let you set a Spot timeout that specifies an action to take if Spot capacity can't be provisioned, a Spot capacity-optimized allocation strategy and an On-Demand lowest-price allocation strategy; if you use a service role that is not the EMR default service role, or an EMR managed policy in your service role, you need to add permissions to the custom cluster service role to enable the allocation strategy option.",
   "add_ev": ["If you use a service role that is not the EMR default service role, or use an EMR managed policy in your service role, you need to add additional permissions to the custom cluster service role to enable the allocation strategy option."]},
 "emr-fleet-primary-target-always-one": {R: "Contradicted by other saved EMR pages: emr-plan-ha says high availability (three primary nodes) is supported for instance fleets from release 5.36.1, so 'the primary fleet is always one instance' is not current truth for every cluster."},
 "emr-lake-formation-prerequisite-glue-catalog": {"claim": "To integrate Amazon EMR with Lake Formation, turn on runtime role authorization on your Amazon EMR cluster and use the AWS Glue Data Catalog as your metadata store."},
 "emr-long-running-use-cases": {"claim": "A long-running EMR cluster fits when you need to interactively or automatically query data, or when you periodically process a data set so large or so frequently that it is inefficient to launch new clusters and load data each time."},
 "emr-managed-scaling-automatic-by-workload": {
   "claim": "With Amazon EMR versions 5.30.0 and higher (except Amazon EMR 6.0.0), you can enable EMR managed scaling, which automatically increases or decreases the number of instances or units in your cluster based on workload; managed scaling is available for clusters composed of either instance groups or instance fleets.",
   "add_ev": ["With Amazon EMR versions 5.30.0 and higher (except for Amazon EMR 6.0.0), you can enable Amazon EMR managed scaling."]},
 "emr-private-subnet-supported-4-2": {"claim": "You can launch Amazon EMR clusters in both public and private VPC subnets, so you do not need internet connectivity to run a cluster, but you may need NAT or VPN gateways to access services or resources outside the VPC, such as public AWS service endpoints like AWS KMS; Amazon EMR supports launching clusters in private subnets only in release version 4.2 and later."},
 "emr-serverless-multiple-applications-use-cases": {"claim": "You can create multiple EMR Serverless applications to provide separate logical environments for different teams with independent cost controls and usage tracking, or to maintain separate logical environments for test and production scenarios."},
 "emr-serverless-worker-sizes-pricing-page": {R: "Currency vote outdated: the What's New post of 2026-07-07 offers 32 vCPU workers with up to 244 GB, so the 16 vCPU / 120 GB ceiling of the pricing page is no longer the largest worker; current truth is emr-serverless-larger-workers-2026-07."},
 "emr-unhealthy-node-45-minutes-gracefully-replace": {
   "claim": "If unhealthy node replacement is turned on and any nodes are unhealthy for more than 45 minutes, Amazon EMR will gracefully replace the nodes; the time it takes before a node is gracefully decommissioned or terminated can be subject to change.",
   "add_ev": ["If unhealthy node replacement is turned on, Amazon EMR terminates an unhealthy core node and provisions a new instance, based on the number of instances in the instance group, or based on the target capacity for instance fleets.",
              "Note that the time it takes before a node is gracefully decommissioned or terminated can be subject to change."],
   "qual": {"condition": "unhealthy node replacement is turned on"}},
 "glue-catalog-compaction-dpu-hour-1-minute-minimum": {
   "claim": "AWS Glue Data Catalog table compaction is charged an hourly rate based on the number of DPUs used (a DPU provides 4 vCPU and 16 GB of memory), billed in increments of 1 second, rounded up to the nearest second, with a 1-minute minimum duration per run.",
   "qual": {"scope": "AWS Glue Data Catalog table compaction"}},
 "glue-catalog-metadata-object-definition": {"claim": "In the AWS Glue Data Catalog, a metadata object is a table, table version, partition, partition indexes, statistics, database, or catalog."},
 "glue-change-2022-08-flex-execution-class": {
   "claim": "On August 9, 2022 the AWS Glue documentation history added support for the configuration of flexible job runs for non-urgent jobs such as pre-production jobs, testing, and one-time data loads.",
   "qual": {"condition": ""}},
 "glue-crawler-default-updates-schema-can-be-prevented": {
   "claim": "By default, AWS Glue crawlers update the schema in the Data Catalog to match the data source being crawled, and you can prevent AWS Glue crawlers from making any schema changes to the Data Catalog when they run.",
   "qual": {"condition": ""}},
 "glue-crawler-first-matching-custom-classifier-then-built-in": {"claim": "The first custom classifier to successfully recognize the structure of your data is used to create a schema, and custom classifiers lower in the list are skipped. If no custom classifier matches, built-in classifiers, such as one that recognizes JSON, try to recognize your data's schema."},
 "glue-crawler-schema-change-options-add-new-columns-only-or-log": {"claim": "To stop a Glue crawler from changing an existing schema in the console, choose Add new columns only or Ignore the change and don't update the table in the Data Catalog under Advance options; if you don't want a table schema to change at all when a crawler runs, set the schema change policy to LOG."},
 "glue-cross-account-resource-owned-by-creating-target-account": {"claim": "When a user in Account A creates a resource such as a database in Account B, that resource is then owned by Account B; storage costs and other costs directly associated with it are billed to Account B, and the cost of requests from the user who created it is billed to the requester's account, Account A."},
 "glue-data-catalog-populate-crawler-recommended-manual-hive-services": {"claim": "Crawlers are the most common and recommended method to populate the Data Catalog; manual entry is useful when you want to catalog data sources that cannot be crawled; and you can use AWS Glue to import metadata from an existing metadata store like Apache Hive Metastore into the Data Catalog."},
 "glue-data-quality-min-2-dpus": {
   "claim": "For AWS Glue Data Quality Tasks on datasets cataloged in the Data Catalog, you require a minimum of 2 DPUs with a 1 minute minimum billing duration.",
   "add_ev": ["Pricing for managing data quality of datasets cataloged in the Data Catalog:",
              "These tasks are called Data Quality Tasks for which you will provision DPUs."]},
 "glue-datalake-wp-transform-csv-to-parquet-reduce-size-optimize-athena": {"claim": "Transformations might involve aggregating data from different sources or changing the file format of the data received, such as from CSV to Parquet format, to reduce the file size and optimize the Athena query; the data is stored in a raw bucket."},
 "glue-decision-guide-visual-etl-and-query-cataloged-data": {
   "claim": "With AWS Glue, you can discover and connect to more than 100 diverse data sources and manage your data in a centralized data catalog, visually create, run, and monitor ETL pipelines to load data into your data lakes, and immediately search and query cataloged data using Athena, Amazon EMR, and Amazon Redshift Spectrum.",
   "add_ev": ["With AWS Glue, you can discover and connect to more than 100 diverse data sources and manage your data in a centralized data catalog."]},
 "glue-encryption-vpc-jobs-need-route-to-kms-nat-or-endpoint": {"claim": "When you add a security configuration to a Glue crawler or job that accesses JDBC data stores, AWS Glue must have a route to the AWS KMS endpoint, which you can provide with a network address translation (NAT) gateway or with an AWS KMS VPC endpoint."},
 "glue-eol-versions-no-job-runs": {
   "claim": "When an AWS Glue version reaches end of life (EOL), you can no longer start job runs on these AWS Glue versions.",
   "add_ev": ["**End of Life (EOL) -** When an AWS Glue version reaches EOL:"],
   "qual": {"condition": ""}},
 "glue-eventbridge-catalog-events-best-effort-no-order-guarantee": {
   "claim": "When a Glue Data Catalog table is created or deleted, a notification is sent to EventBridge; these events are emitted on a best effort basis, so you cannot write a program that depends on the order or existence of notification events, as they might be out of sequence or missing.",
   "replace_ev": {0: "For example, if a table is created or deleted, a notification is sent to EventBridge. Note that you cannot write a program that depends on the order or existence of notification events, as they might be out of sequence or missing. Events are emitted on a best effort basis."},
   "qual": {"scope": "Glue Data Catalog table create and delete notifications sent to EventBridge"}},
 "glue-flex-price-example-0-29": {R: "Entail partial (the data quality job scope stands outside the quote) and currency unsure (the Glue 6.0 price change of 2026-08-21 may change the example prices); example prices are not exam material."},
 "glue-interactive-session-default-5-dpu": {"claim": "An AWS Glue Interactive Session has 5 DPU by default.", "qual": {"scope": "AWS Glue Interactive Sessions"}},
 "glue-job-bookmark-jdbc-primary-key-default-case-sensitive-unsupported": {
   "claim": "AWS Glue by default uses a table's primary key as the job bookmark key, provided that it is sequentially increasing or decreasing (with no gaps), and AWS Glue doesn't support using columns with case-sensitive names as job bookmark keys.",
   "qual": {"scope": "AWS Glue job bookmark keys"}},
 "glue-job-bookmark-rewind-or-reset-does-not-clean-targets": {"claim": "You can rewind your job bookmarks for your AWS Glue Spark ETL jobs to any previous job run. When you rewind or reset a bookmark, AWS Glue does not clean the target files, because there could be multiple targets and targets are not tracked with job bookmarks; only source files are tracked."},
 "glue-job-max-concurrency-default-one": {"qual": {"condition": ""}},
 "glue-job-script-python-or-scala-generated-or-own": {"claim": "A Glue job script can be coded in Python or Scala, and you can choose whether the script that the job runs is generated by AWS Glue or provided by you."},
 "glue-job-security-configuration-s3-target-encryption-options": {
   "claim": "A Glue security configuration specifies how the data at the Amazon S3 target is encrypted: no encryption, server-side encryption with AWS KMS-managed keys (SSE-KMS), or Amazon S3-managed encryption keys (SSE-S3).",
   "drop_values": ["ignored"], "drop_ev": [1]},
 "glue-lake-formation-fgac-adds-latency-fta-optimized": {"add_ev": ["AWS Glue 5.0 and above supports two models for accessing data through AWS Lake Formation:"]},
 "glue-lake-formation-fgac-column-row-level-vs-fta-full-table": {"add_ev": ["AWS Glue 5.0 and above supports two models for accessing data through AWS Lake Formation:"]},
 "glue-partition-index-items-charged-as-catalog-storage": {"claim": "For each partition added to a table, there is a corresponding partition index item created, and each partition index item is charged according to the current AWS Glue pricing policy for data catalog storage."},
 "glue-price-etl-per-dpu-hour-example": {R: "Currency unsure: the Glue 6.0 price change of 2026-08-21 may change the $0.44 example and the page does not say which Glue version it prices; example prices are not exam material."},
 "glue-python-shell-dpu-values": {
   "claim": "For a Glue Python shell job, you can set the maximum number of DPUs that can be allocated when the job runs to 0.0625 or 1; the default is 0.0625, and in either case the local disk for the instance will be 20GB.",
   "add_ev": ["The maximum number of AWS Glue data processing units (DPUs) that can be allocated when this job runs."],
   "qual": {"condition": ""}},
 "glue-python-shell-jobs-single-ec2-instance-limited": {"claim": "AWS Glue Python shell jobs run native Python data integrations on a single Amazon EC2 instance and are limited by the capacity of that instance."},
 "glue-ray-closed-to-new-customers": {"qual": {"condition": ""}},
 "glue-relationalize-array-becomes-table-with-foreign-key": {"claim": "When AWS Glue converts a semi-structured schema to a relational schema, a single value converts directly to a relational column, and an array converts to a relational column with a foreign key (FK) that points to another relational table."},
 "glue-sla-monthly-uptime-99-9": {"qual": {"scope": "each Included Service of the AWS Glue SLA, per AWS Region, per monthly billing cycle"}},
 "glue-streaming-any-output-format-s3-or-jdbc": {R: "The quotes are bare value lines whose labels (data store, format, Create tables in your data target) stand only outside the quotes; the console option has no exam value."},
 "glue-streaming-auto-detects-compressed-data": {"qual": {"condition": ""}},
 "glue-streaming-catalog-table-created-manually-glue-console-only": {"claim": "A Data Catalog table that specifies source data stream properties, including the data schema, can be manually created for a streaming source and is used as the data source for the streaming ETL job; you can't use the AWS Lake Formation console to create the table, you must use the AWS Glue console."},
 "glue-trigger-three-types-scheduled-conditional-on-demand": {"claim": "AWS Glue triggers include a time-based trigger based on cron, a trigger that fires when a previous job or crawler or multiple jobs or crawlers satisfy a list of conditions, and a trigger that fires when you activate it, which never enters the ACTIVATED or DEACTIVATED state and always remains in the CREATED state."},
 "glue-vpc-eni-private-ip-needs-nat-for-internet": {"claim": "Each elastic network interface that AWS Glue creates is assigned a private IP address from the subnets that you specify and no public IP addresses. AWS Glue requires internet access (for example, to access AWS services that don't have VPC endpoints), which you can provide with a network address translation (NAT) instance inside your VPC or the Amazon VPC NAT gateway."},
 "glue-worker-r-types-for-memory-intensive-out-of-memory": {
   "claim": "Each AWS Glue R.1X worker maps to 1 DPU with a memory-optimized configuration, and AWS recommends this worker type for memory-intensive workloads that frequently encounter out-of-memory errors or require high memory-to-CPU ratios.",
   "qual": {"scope": "R.1X worker type"}},
 "glue-worker-r1x-spec": {"claim": "An AWS Glue R.1X worker provides 1 DPU per node, with 4 vCPU and 32 GB of memory, 94 GB of disk and 44 GB of approximate free disk space, and 1 Spark executor per node."},
 "glue-workflow-eventbridge-batch-window-default-900-seconds": {
   "claim": "For Glue workflow batch conditions, you must specify the batch size (number of events) and can optionally specify a batch window (number of seconds); the default and maximum batch window is 900 seconds (15 minutes), and the batch condition that is met first starts the workflow.",
   "qual": {"scope": "Glue workflow batch conditions"}},
 "glue-workflow-start-triggers-schedule-on-demand-eventbridge": {"claim": "A Glue workflow can be started according to a schedule that you define (daily, weekly, monthly, and so on, or a custom schedule based on a cron expression), on demand from the AWS Glue console, API, or AWS CLI, or upon a single Amazon EventBridge event or a batch of Amazon EventBridge events."},
 "glue-workflows-preferred-for-complex-multi-job-etl": {"claim": "In AWS Glue, workflows are preferred for creating complex multi-job ETL operations."},
 "glue-zero-etl-no-additional-fee": {
   "claim": "AWS does not charge an additional fee for the zero-ETL integration, and you pay for source and target resources used to create and process the changed data; for application sources, AWS Glue charges a fee for the ingestion of application source data supported by zero-ETL integration.",
   "add_ev": ["AWS Glue charges a fee for the ingestion of application source data supported by zero-ETL integration."],
   "qual": {"condition": ""}},
 "glue-zero-etl-targets-and-self-managed-redshift-only": {
   "claim": "AWS Glue zero-ETL targets include Amazon S3 Tables via the Lakehouse architecture of Amazon SageMaker; for self-managed database sources, you can replicate data only to an Amazon Redshift data warehouse, and other targets are not supported."},
 "lake-formation-case-fujitsu-chose-lake-formation-orchestration": {
   "claim": "Fujitsu selected AWS to build its data use solution, and in its comparison of major cloud services it focused on AWS Lake Formation for its orchestration functions.",
   "add_ev": ["Fujitsu selected AWS to build its data use solution."]},
 "lake-formation-case-fujitsu-daily-updates-in-3-months": {"claim": "Fujitsu released the service on OneData in 3 months and shortened the data updates from monthly to daily."},
 "lake-formation-cell-level-not-on-nested-columns-views-resource-links": {"add_ev": ["Keep in mind the following notes and restrictions for row-level and cell-level filtering."]},
 "lake-formation-change-2022-11-cross-account-direct-principals": {"qual": {"condition": ""}},
 "lake-formation-change-2023-06-cross-region-access": {"qual": {"condition": ""}},
 "lake-formation-change-2024-11-lf-tag-expressions": {"qual": {"condition": ""}},
 "lake-formation-change-2024-12-governed-tables-shutdown": {"qual": {"condition": ""}},
 "lake-formation-change-2026-02-enhanced-cross-account-sharing": {
   "claim": "On Feb 11, 2026 AWS Lake Formation enhanced cross-account sharing: Lake Formation sets up a single AWS Resource Access Manager resource share for an unlimited number of tables to another account, eliminating previous resource association limits per resource type.",
   "set_display": {"date": "Feb 11, 2026"},
   "add_ev_heading": [["Posted on: Feb 11, 2026", "AWS Lake Formation enhances cross-account sharing"]],
   "qual": {"condition": ""}},
 "lake-formation-change-2026-06-table-permissions-underlying-s3": {"qual": {"condition": ""}},
 "lake-formation-credential-vending-engine-filters-columns-rows": {"qual": {"condition": "the user is authorized to access the table"}},
 "lake-formation-data-access-permissions-select-insert-delete": {
   "claim": "After you register an Amazon S3 location, you can start granting Lake Formation data access permissions (SELECT, INSERT, and DELETE) on Data Catalog tables that point to that location, and data location permissions on that location.",
   "add_ev": ["After you register an Amazon S3 location, you can start granting the following Lake Formation permissions:"]},
 "lake-formation-datalake-wp-raw-bucket-immutable-copy": {
   "claim": "In the data lake foundation of the Building Data Lakes whitepaper, raw data is data ingested from the data sources in the raw data format, which is the immutable copy of the data.",
   "qual": {"scope": "data lake foundation, as stated in the AWS Building Data Lakes whitepaper"}},
 "lake-formation-decision-guide-vpc-endpoints-avoid-public-internet": {"claim": "The AWS analytics decision guide advises considering services that support Amazon VPC endpoints to avoid exposing resources to the public internet."},
 "lake-formation-effective-permissions-are-union-of-policies": {
   "claim": "When you grant permissions to a principal, Lake Formation evaluates permissions as a union of all the policies for that user.",
   "drop_values": ["example"]},
 "lake-formation-initial-settings-super-to-iamallowedprincipals-use-only-iam": {
   "add_ev": ["To maintain backward compatibility with AWS Glue, AWS Lake Formation has the following initial security settings:"],
   "qual": {"condition": ""}},
 "lake-formation-integrated-service-enforces-filtering-after-fetching-data": {"claim": "The integrated service performs the necessary enforcement of Lake Formation policies, such as column level, row level and/or cell level filtering."},
 "lake-formation-move-to-lf-permissions-two-steps-new-and-existing-resources": {
   "add_ev": ["To change security settings so that access to Data Catalog resources (databases and tables) is managed by Lake Formation permissions, do the following:"]},
 "lake-formation-new-databases-tables-get-iamallowedprincipal-by-default": {"qual": {"condition": ""}},
 "lake-formation-pipeline-wp-kms-access-iam-audit-cloudtrail": {"claim": "In the serverless data analytics pipeline whitepaper, access to the encryption keys is controlled using IAM and is monitored through detailed audit trails in CloudTrail."},
 "lake-formation-price-permissions-no-charge": {"qual": {"condition": ""}},
 "lake-formation-price-storage-api-bytes-scanned": {"qual": {"condition": ""}},
 "lake-formation-putdatalakesettings-new-resources-lf-or-iam-only": {
   "claim": "With the Lake Formation PutDataLakeSettings API operation you can change default security settings: to enforce metadata and underlying data access control by Lake Formation on new databases and tables, which revokes all Lake Formation permissions from the IAMAllowedPrincipals group on them, or to enforce access control only by IAM, which grants the Super Lake Formation permission to the IAMAllowedPrincipals group. When you create a database, you can override this setting.",
   "add_ev": ["You can also change default security settings by using the Lake Formation PutDataLakeSettings API operation.",
              "To enforce metadata and underlying data access control by Lake Formation on new databases and tables, code the `DataLakeSettings` structure as follows.",
              "To enforce metadata and underlying data access control only by IAM on new databases and tables, code the `DataLakeSettings` structure as follows."]},
 "lake-formation-registration-role-trust-and-passrole": {
   "claim": "If you create a registration role using a different path, ensure that the role has a trust relationship with lakeformation.amazonaws.com; the data lake administrator who registers the location must have the iam:PassRole permission on the role.",
   "qual": {"scope": "user-defined roles used to register Lake Formation locations"}},
 "lake-formation-row-level-security-by-column-values": {"claim": "Granting permissions on a Data Catalog table with row-level security (row filtering) allows users to view only specific rows of data that they have access to in the table, and the filtering is based on the values of one or more columns."},
 "lake-formation-two-permission-levels-metadata-and-storage": {"add_ev": ["In Lake Formation, you can implement permissions on two levels:"]},
 "lake-formation-user-defined-role-required-cross-account-aws-managed-key-emr": {"add_ev": ["You must use a user-defined role in the following circumstances:"]},
 "lake-formation-workflow-created-in-lf-runs-in-glue": {"claim": "A Lake Formation workflow is a container for a set of related AWS Glue jobs, crawlers, and triggers; you create the workflow in Lake Formation, and it executes in the AWS Glue service."},
 "opensearch-auto-detects-replaces-failed-nodes": {"claim": "Amazon OpenSearch Service automatically detects and replaces failed OpenSearch Service nodes, and you can scale your cluster with a single API call or a few clicks in the console."},
 "opensearch-case-hapag-lloyd-troubleshoot-faster-better-decisions": {
   "add_ev": ["Using Amazon OpenSearch Service, which securely unlocks near-real-time search, monitoring, and analysis of business and operational data, the Hapag-Lloyd Web & Mobile team built a centralized logging solution to monitor its applications."]},
 "opensearch-change-2023-01-serverless-ga": {"claim": "On January 25, 2023 the Amazon OpenSearch Service documentation history recorded that Amazon OpenSearch Serverless is now generally available.", "qual": {"condition": ""}},
 "opensearch-encryption-at-rest-kms-aes-256-what-is-encrypted": {"claim": "Encryption of data at rest in OpenSearch Service uses AWS Key Management Service (AWS KMS) to store and manage encryption keys and the Advanced Encryption Standard algorithm with 256-bit keys (AES-256) to perform the encryption."},
 "opensearch-encryption-at-rest-not-manual-snapshots-slow-logs": {"claim": "You currently can't use AWS KMS keys to encrypt OpenSearch Service manual snapshots."},
 "opensearch-extended-support-flat-fee-per-nih": {"qual": {"scope": "OpenSearch Service domains running Extended Support", "condition": ""}},
 "opensearch-faq-az-options-one-two-three": {
   "claim": "OpenSearch Service lets you deploy instances across one, two, or three AZs: development or test workloads can pick the single AZ option, and production-grade workloads should use two or three AZs; the three AZ option is only available in Regions where there are three or more AZs.",
   "add_ev": ["Note: The three AZ option is only available in regions where there are three or more AZs."]},
 "opensearch-master-nodes-distributed-across-three-azs": {
   "claim": "Even if you select two Availability Zones when configuring your Amazon OpenSearch Service domain, OpenSearch Service automatically distributes dedicated master nodes across three Availability Zones; if you choose an older-generation instance type that is not available in three Availability Zones and chose two zones, it distributes the dedicated master nodes across two zones.",
   "add_ev": ["If you choose an older-generation instance type that is not available in three Availability Zones, the following scenarios apply:",
              "If you chose two Availability Zones for the domain, OpenSearch Service distributes the dedicated master nodes across two zones."],
   "qual": {"condition": ""}},
 "opensearch-multiaz-standby-recommended-production-config": {
   "claim": "For domains that run production workloads, AWS recommends the Multi-AZ with Standby deployment option, which creates this configuration: the domain deployed across three zones; current-generation instance types for dedicated master nodes and data nodes; three dedicated master nodes and three (or a multiple of three) data nodes; and at least two replicas for each index, or a multiple of three copies of data.",
   "add_ev": ["For domains that run production workloads, we recommend the Multi-AZ with Standby deployment option, which creates the following configuration:",
              "Current-generation instance types for dedicated master nodes and data nodes.",
              "Three dedicated master nodes and three (or a multiple of three) data nodes."]},
 "opensearch-node-to-node-encryption-tls-1-2-default-unencrypted": {
   "claim": "Each OpenSearch Service domain resides within its own, dedicated VPC; by default, traffic within that VPC is unencrypted, and node-to-node encryption enables TLS 1.2 encryption for all communications within the VPC.",
   "add_ev": ["Each OpenSearch Service domain—regardless of whether the domain uses VPC access—resides within its own, dedicated VPC."]},
 "opensearch-price-serverless-classic-minimum-2-ocus": {
   "claim": "For Amazon OpenSearch Serverless Classic collections, you are billed at least for a minimum of 2 OCUs (1 OCU indexing including primary and standby, and 1 OCU search including one replica for HA) for the first collection in an account; the minimum varies based on your data size and collections type in use.",
   "add_ev": ["With Amazon OpenSearch Serverless Classic collections, you only pay for the resources consumed by the workload.",
              "However, the minimum varies based on your data size and collections type in use."],
   "qual": {"condition": ""}},
 "opensearch-price-serverless-nextgen-scale-to-zero-10-minutes": {
   "add_ev": ["With Amazon OpenSearch Serverless NextGen collections, you only pay for the resources consumed by the workload."],
   "qual": {"condition": ""}},
 "opensearch-serverless-use-cases-log-analytics-full-text-search": {"claim": "OpenSearch Serverless use cases include log analytics, which analyzes large volumes of semi-structured, machine-generated time series data, and full-text search; when you create a collection, you choose one of these use cases."},
 "opensearch-snapshots-manual-s3-charges": {
   "claim": "OpenSearch Service manual snapshots, which you have to initiate, are stored in your own Amazon S3 bucket and standard S3 charges apply.",
   "replace_ev": {0: "You have to initiate manual snapshots. These snapshots are stored in your own Amazon S3 bucket and standard S3 charges apply."}},
 "quick-athena-results-bucket-and-kms-decrypt-permission": {"claim": "Amazon Quick Sight needs permissions to access the bucket Athena is currently using, and if your data file is encrypted with an AWS KMS key, you grant permissions to the Amazon Quick Sight IAM role to decrypt the key."},
 "quick-change-2022-11-spice-1-billion-rows": {R: "Currency vote outdated: the 1 billion rows or 1 TB SPICE quota was raised (2 billion rows, 2 TB); current truth is quick-spice-enterprise-dataset-limit, whose change items carry the history."},
 "quick-change-2026-04-free-and-plus-plans": {
   "claim": "On Apr 28, 2026 new Free and Plus pricing plans for Amazon Quick started, allowing you to sign up in minutes using your personal email address or existing Google, Apple, Github, or Amazon credentials, with no AWS account required.",
   "qual": {"condition": ""}},
 "quick-direct-query-visual-timeout-2-minutes": {
   "claim": "For visualizing with direct queries, Amazon Quick Sight generates a timeout after 2 minutes; however, not all database drivers react to the 2-minute timeout, for example Amazon Redshift.",
   "add_ev": ["However, not all database drivers react to the 2-minute timeout, for example Amazon Redshift."],
   "qual": {"condition": ""}},
 "quick-faq-four-plans-free-plus-professional-enterprise": {R: "Currency vote outdated: the Quick Max plan (2026-09-03) makes five plans on the pricing page; the FAQ count of four is stale, and Quick Max is not examinable yet."},
 "quick-faq-free-plan-single-user-no-cost": {R: "Currency unsure: the pricing page lists the Free plan without some extensions and shared knowledge bases, so the FAQ list may be stale; the Free plan detail has no exam value."},
 "quick-faq-no-aws-account-needed-to-sign-up": {R: "The next FAQ sentence says Professional and Enterprise plans are available through the AWS Console, an exception to the general claim; quick-change-2026-04-free-and-plus-plans states the no-AWS-account sign-up with its scope (Free and Plus plans)."},
 "quick-fully-managed-no-infrastructure": {"claim": "With Amazon Quick there is no infrastructure to provision, no models to host, and no ML expertise required."},
 "quick-lake-formation-adds-permissions-model-to-iam": {"claim": "Lake Formation adds to the AWS Identity and Access Management (IAM) permissions model its own centrally defined permissions model with a simple grant and revoke mechanism, and you can use Lake Formation instead of, or in addition to, using scoped-down policies with IAM."},
 "quick-pricing-infrastructure-fee-250": {"qual": {"condition": ""}},
 "quick-pricing-overage-professional-vs-enterprise": {"qual": {"condition": ""}},
 "quick-spice-benefits-faster-reuse-without-query-cost": {
   "claim": "Data stored in SPICE can be reused multiple times without incurring additional costs; if you use a data source that charges per query, you're charged for querying the data when you first create the dataset and later when you refresh the dataset.",
   "drop_values": ["v0"], "drop_ev": [0]},
 "quick-spice-capacity-per-region-shared": {"qual": {"adjustable": False, "condition": ""}},
 "quick-spice-enterprise-dataset-limit": {"qual": {"condition": ""}},
 "quick-spice-hourly-refresh-enterprise-only": {"qual": {"condition": ""}},
 "quick-spice-incremental-refresh-sql-sources": {
   "claim": "For SQL-based data sources, such as Amazon Redshift, Amazon Athena, PostgreSQL, or Snowflake, you can refresh a SPICE dataset incrementally within a look-back window of time.",
   "qual": {"condition": ""}},
 "quick-spice-logical-size-bytes-per-cell": {"qual": {"scope": "estimating the logical size of one SPICE dataset"}},
 "quick-spice-schedules-five-per-dataset": {"qual": {"condition": ""}},
 "quick-trial-30-days-25-users": {"qual": {"scope": "Amazon Quick free trial", "condition": ""}},
}


def load_facts():
    out = {}
    for s in SERVICES:
        for line in open(ROOT + "/data/facts/" + s + ".jsonl"):
            if line.strip():
                f = json.loads(line)
                out[f["id"]] = f
    return out


def ev_item(src, quote, heading=None):
    return {"source_id": src["source_id"], "url": src["url"], "quote": quote,
            "table_header": None, **({"heading": heading} if heading else {})}


def build(f, spec):
    p = {}
    ev = [{k: e[k] for k in ("source_id", "url", "quote", "table_header", "heading") if k in e} for e in f["evidence"]]
    ev_changed = False
    for i, q in spec.get("replace_ev", {}).items():
        ev[i]["quote"] = q
        ev_changed = True
    for i in sorted(spec.get("drop_ev", []), reverse=True):
        del ev[i]
        ev_changed = True
    base = f["evidence"][0]
    for q in spec.get("add_ev", []):
        ev.append(ev_item(base, q))
        ev_changed = True
    for q, h in spec.get("add_ev_heading", []):
        ev.append(ev_item(base, q, h))
        ev_changed = True
    if ev_changed:
        p["evidence"] = ev
    if "claim" in spec:
        p["claim"] = spec["claim"]
    if "drop_values" in spec or "set_display" in spec:
        vals = [copy.deepcopy(v) for v in f["values"] if v["key"] not in spec.get("drop_values", [])]
        for v in vals:
            if v["key"] in spec.get("set_display", {}):
                v["display"] = spec["set_display"][v["key"]]
        p["values"] = vals
    if "qual" in spec:
        q = copy.deepcopy(f["qualifiers"])
        old_cond = q.get("condition") or ""
        q.update(spec["qual"])
        p["qualifiers"] = q
        if old_cond and old_cond != q.get("condition"):
            note = f.get("note") or ""
            p["note"] = (note + " | " if note else "") + "adjudicate-35 moved from condition (not carried by the quote): " + old_cond
    return p


def run(step, argv):
    p = subprocess.run([sys.executable, ROOT + "/tools/saa.py"] + argv, cwd=REPO, capture_output=True, text=True)
    rec = {"step": step, "rc": p.returncode, "out": (p.stdout or "")[-1500:], "err": (p.stderr or "")[-800:]}
    with open(LOG, "a") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(step, p.returncode, (p.stdout or p.stderr or "").strip()[:300].replace("\n", " | "), flush=True)
    return p.returncode


def main():
    dry = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    os.makedirs(PD, exist_ok=True)
    facts = load_facts()
    done = set()
    if os.path.exists(LOG) and not dry:
        for line in open(LOG):
            if line.strip():
                r = json.loads(line)
                if r.get("rc") == 0 and not r["step"].startswith("dry:"):
                    done.add(r["step"])
    for fid, spec in SPEC.items():
        if only and fid not in only:
            continue
        f = facts[fid]
        if R in spec:
            step = "reject:" + fid
            if step in done or f.get("status") == "rejected":
                continue
            if dry:
                continue
            run(step, ["facts", "amend", fid, "--reject", "--reason", "adjudicate-35: " + spec[R], "--by", BY])
            continue
        step = "repair:" + fid
        if step in done:
            continue
        if f.get("status") != "disputed":
            print("skip (status " + str(f.get("status")) + "):", fid)
            continue
        patch = build(f, spec)
        path = PD + fid + ".json"
        with open(path, "w") as fh:
            json.dump(patch, fh, ensure_ascii=False, indent=1)
        argv = ["facts", "amend", fid, "--file", "aws-saa-book/_build/work/35-analytics/adj-patches/" + fid + ".json",
                "--reason", "adjudicate-35: claim and qualifiers narrowed to what the quotes carry, or the quote that carries the missing clause added",
                "--by", BY]
        if dry:
            argv.append("--dry-run")
            step = "dry:" + fid
        run(step, argv)
    print("finished", flush=True)


if __name__ == "__main__":
    main()
