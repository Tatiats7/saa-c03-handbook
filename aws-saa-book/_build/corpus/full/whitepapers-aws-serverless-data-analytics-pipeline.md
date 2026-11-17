# AWS Serverless Data Analytics Pipeline AWS Whitepaper

-----
*****Copyright &copy; Amazon Web Services, Inc. and/or its affiliates. All rights reserved.*****

-----
Amazon's trademarks and trade dress may not be used in
connection with any product or service that is not Amazon's,
in any manner that is likely to cause confusion among customers,
or in any manner that disparages or discredits Amazon. All other
trademarks not owned by Amazon are the property of their respective
owners, who may or may not be affiliated with, connected to, or
sponsored by Amazon.

-----
## Contents
+ [AWS Serverless Data Analytics Pipeline](#aws-serverless-data-analytics-pipeline)
+ [Logical architecture of modern data lake centric analytics platforms](#logical-architecture-of-modern-data-lake-centric-analytics-platforms)
+ [Serverless data lake centric analytics architecture](#serverless-data-lake-centric-analytics-architecture)
+ [Ingestion layer](#ingestion-layer-1)
+ [Storage layer](#storage-layer-1)
+ [Cataloging and search layer](#cataloging-and-search-layer-1)
+ [Processing layer](#processing-layer-1)
+ [Consumption layer](#consumption-layer-1)
+ [Security and governance layer](#security-and-governance-layer-1)
+ [Conclusion](#conclusion)
+ [Further reading](#further-reading)
+ [Contributors](#contributors)
+ [Document revisions](#document-revisions)
+ [Notices](#notices)
+ [AWS Glossary](#glossary)

-----



 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Serverless Data Analytics Pipeline
<a name="aws-serverless-data-analytics-pipeline"></a>

Publication date: **April 7, 2021** ([Document revisions](#document-revisions))

## Abstract
<a name="abstract"></a>

 This whitepaper discusses a layered, component-oriented, and logical architecture of modern analytics platforms. It also includes a reference architecture for building a serverless data platform that includes a data lake, data processing pipelines, and a consumption layer that enables several ways to analyze the data in the data lake without moving it, including business intelligence (BI) dashboarding, exploratory interactive SQL, big data processing, predictive analytics, and machine learning (ML). 

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected) (sign-in required), you can review your workloads against these best practices by answering a set of questions for each pillar. 

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar. 

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/). 

## Introduction
<a name="introduction"></a>

 Onboarding new data or building new analytics pipelines in traditional analytics architectures usually require extensive coordination across multiple teams such as, business, data engineering, and data science and analytics. Before starting, these teams must first negotiate requirements, schema, infrastructure capacity needs, and workload management. 

 It is becoming increasingly difficult and inefficient to pre-define constantly changing schemas, time consuming to negotiate capacity slots on a shared infrastructure. For these reasons, business users, data scientists, and analysts want easy, frictionless, and self-service options to build end-to-end data pipelines. The exploratory nature of ML and many analytics tasks means you need to rapidly ingest new datasets and clean, normalize, and feature engineer them without worrying about operational overhead when you must think about the infrastructure that runs data pipelines. 

 A serverless data lake architecture enables agile and self-service data onboarding and analytics for all data consumer roles across a company. By using [AWS serverless technologies](https://aws.amazon.com/serverless/) as building blocks, you can rapidly and interactively build data lakes and data processing pipelines to ingest, store, transform, and analyze petabytes of structured and unstructured data from batch and streaming sources, without needing to manage any storage or compute infrastructure. 

 In this whitepaper, we discuss a layered, component-oriented logical architecture of modern analytics platforms and present a reference architecture for building a serverless data platform. This architecture includes a data lake, data processing pipelines, and a consumption layer that enables several ways to analyze the data in the data lake without moving it, including business intelligence (BI) dashboarding, exploratory interactive SQL, big data processing, predictive analytics, and ML. 

# Logical architecture of modern data lake centric analytics platforms
<a name="logical-architecture-of-modern-data-lake-centric-analytics-platforms"></a>

 The following diagram illustrates the architecture of a data lake centric analytics platform. 

![A diagram depicting architecture of a data lake centric analytics platform .](https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/images/dl-analytics.png)




 You can think of a data lake centric analytics architecture as a stack of six logical layers, where each layer is composed of multiple components. A layered, component-oriented architecture promotes separation of concerns, decoupling of tasks, and flexibility. This provides the agility needed to quickly integrate new data sources, support new analytics methods, and add tools required to keep up with the accelerating pace of changes in the analytics landscape. In the following sections, we look at the key responsibilities, capabilities, and integrations of each logical layer. 

## Ingestion layer
<a name="ingestion-layer"></a>

 The ingestion layer is responsible for bringing data into the data lake. It provides the ability to connect to internal and external data sources over a variety of protocols. It can ingest batch and streaming data into the storage layer. The ingestion layer is also responsible for delivering ingested data to a diverse set of targets in the data storage layer including the object store, databases, and warehouses. 

## Storage layer
<a name="storage-layer"></a>

 The storage layer is responsible for providing durable, scalable, secure, and money- saving components to store vast quantities of data. It supports storing unstructured data and datasets of a variety of structures and formats. It supports storing source data as-is without first needing to structure it to conform to a target schema or format. 

 Components from all other layers provide easy and native integration with the storage layer. To store data based on its consumption readiness for different personas across organization, the storage layer is organized into the following zones: 
+  **Raw zone** – The storage area where components from the ingestion layer land data. This is a transient area where data is ingested from sources as-is. Typically, data engineering personas interact with the data stored in this zone. 
+  **Cleaned zone** – After the preliminary quality checks, the data from the raw zone is moved to the cleaned zone for permanent storage where the data is stored in its original format. Having all data from all sources permanently stored in the cleaned zone provides the ability to replay downstream data processing in case of errors or data loss in downstream storage zones. Typically, data engineering and data science personas interact with the data stored in this zone. 
+  **Curated zone** – This zone hosts data that is in the most consumption-ready state and conforms to organizational standards and data models. Datasets in the curated zone are typically partitioned, cataloged, and stored in formats that support performant and cost-effective access by the consumption layer. The processing layer creates datasets in the curated zone after cleaning, normalizing, standardizing, and enriching data from the cleaned zone. All personas across organizations use the data stored in this zone to drive business decisions. 

## Cataloging and search layer
<a name="cataloging-and-search-layer"></a>

 The cataloging and search layer is responsible for storing business and technical metadata about datasets hosted in the storage layer. It provides the ability to track schema and the granular partitioning of dataset information in the lake. It also supports mechanisms to track versions to keep track of changes to the metadata. As the number of datasets in the data lake grows, this layer makes datasets in the data lake discoverable by providing search capabilities. 

## Processing layer
<a name="processing-layer"></a>

 The processing layer is responsible for transforming data into a consumable state through data validation, cleanup, normalization, transformation, and enrichment. It’s responsible for advancing the consumption readiness of datasets along the raw, cleaned, and curated zones and registering metadata for the cleaned and transformed data into the cataloging layer. The processing layer is composed of purpose-built data- processing components to match the right dataset characteristic and processing task at hand. The processing layer can handle large data volumes and support schema-on- read, partitioned data, and diverse data formats. The processing layer also provides the ability to build and orchestrate multi-step data processing pipelines that use purpose- built components for each step. 

## Consumption layer
<a name="consumption-layer"></a>

 The consumption layer is responsible for providing scalable and performant tools to gain insights from the vast amount of data in the data lake. It supports analytics across all personas across the organization through several purpose-built analytics tools that support analysis methods, including SQL, batch analytics, BI dashboards, reporting, and ML. The consumption layer natively integrates with the data lake’s storage, cataloging, and security layers. Components in the consumption layer support schema- on-read, a variety of data structures and formats, and use data partitioning for cost and performance optimization. 

## Security and governance layer
<a name="security-and-governance-layer"></a>

 The security and governance layer is responsible for protecting the data in the storage layer and processing resources in all other layers. It provides mechanisms for access control, encryption, network protection, usage monitoring, and auditing. The security layer also monitors activities of all components in other layers and generates a detailed audit trail. Components of all other layers provide native integration with the security and governance layer. 

# Serverless data lake centric analytics architecture
<a name="serverless-data-lake-centric-analytics-architecture"></a>

 To compose the layers described in our logical architecture, AWS introduces a reference architecture that uses AWS serverless and managed services. In this approach, AWS services provide the following capabilities: 
+  Providing and managing scalable, resilient, secure, and cost-effective infrastructural components 
+  Ensuring infrastructural components natively integrate with each other 

 This reference architecture enables you to focus more time on rapidly building data and analytics pipelines. It significantly accelerates new data onboarding and driving insights from your data. The AWS serverless and managed components enable self-service across all data consumer roles by providing the following key benefits: 
+  Easy configuration-driven use 
+  Freedom from infrastructure management 
+  Pay-per-use pricing model 

 The following diagram illustrates this architecture. 

![A diagram depicting an AWS serverless data analytics pipeline reference architecture .](https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/images/da-pipeline.png)


# Ingestion layer
<a name="ingestion-layer-1"></a>

 The ingestion layer in the presented serverless architecture is composed of a set of purpose-built AWS services to enable data ingestion from a variety of sources. Each of these services enables simple self-service data ingestion into the data lake landing zone and provides integration with other AWS services in the storage and security layers. Individual purpose-built AWS services match the unique connectivity, data format, data structure, and data velocity requirements of operational database sources, streaming data sources, and file sources. 

## Operational database sources
<a name="operational-database-sources"></a>

 Typically, organizations store their operational data in various relational and NoSQL databases. [AWS Data Migration Service](https://aws.amazon.com/dms/) (AWS DMS) can connect to a variety of operational RDBMS and NoSQL databases and ingest their data into [Amazon Simple](https://aws.amazon.com/s3) [Storage Service](https://aws.amazon.com/s3) (Amazon S3) buckets in the data lake landing zone. With AWS DMS, you can first perform a one-time import of the source data into the data lake and replicate ongoing changes happening in the source database. AWS DMS encrypts S3 objects using [AWS Key Management Service](https://aws.amazon.com/kms) (AWS KMS) keys as it stores them in the data lake. AWS DMS is a fully managed, resilient service and provides a wide choice of instance sizes to host database replication tasks. 

 [AWS Lake Formation](https://aws.amazon.com/lake-formation/) provides a scalable, serverless alternative, called blueprints, to ingest data from AWS native or on-premises database sources into the landing zone in the data lake. A Lake Formation blueprint is a predefined template that generates a data ingestion [AWS Glue workflow](https://aws.amazon.com/glue) based on input parameters such as source database, target Amazon S3 location, target dataset format, target dataset partitioning columns, and schedule. A blueprint-generated AWS Glue workflow implements an optimized and parallelized data ingestion pipeline consisting of crawlers, multiple parallel jobs, and triggers connecting them based on conditions. For more information, see [Integrating AWS Lake Formation with Amazon RDS for SQL Server](https://aws.amazon.com/blogs/big-data/integrating-aws-lake-formation-with-amazon-rds-for-sql-server/). 

## Streaming data sources
<a name="streaming-data-sources"></a>

 The ingestion layer uses Amazon Data Firehose to receive streaming data from internal and external sources. With a few clicks, you can configure a Firehose API endpoint where sources can send streaming data. This streaming data can be clickstreams, application and infrastructure logs and monitoring metrics, and IoT data such as devices telemetry and sensor readings. Firehose does the following: 
+  Buffers incoming streams 
+  Batches, compresses, transforms, and encrypts the streams 
+  Stores the streams as S3 objects in the landing zone in the data lake 

 Firehose natively integrates with the security and storage layers and can deliver data to Amazon S3, [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/) (OpenSearch Service) for real-time analytics use cases. Firehose is serverless, requires no administration, and has a cost model where you pay only for the volume of data you transmit and process through the service. Firehose automatically scales to adjust to the volume and throughput of incoming data. 

## File sources
<a name="file-sources"></a>

 Many applications store structured and unstructured data in files that are hosted on Network Attached Storage (NAS) arrays. Organizations also receive data files from partners and third-party vendors. Analyzing data from these file sources can provide valuable business insights. 

## Internal file shares
<a name="internal-file-shares"></a>

 [AWS DataSync](https://aws.amazon.com/datasync) can ingest hundreds of terabytes and millions of files from NFS and SMB enabled NAS devices into the data lake landing zone. DataSync automatically handles scripting of copy jobs, scheduling and monitoring transfers, validating data integrity, and optimizing network utilization. DataSync can perform one-time file transfers and monitor and sync changed files into the data lake. DataSync is fully managed and can be set up in minutes. 

### Partner data files
<a name="partner-data-files"></a>

 FTP is most common method for exchanging data files with partners. The [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) is a serverless, highly available, and scalable service that supports secure FTP endpoints and natively integrates with Amazon S3. Partners and vendors transmit files using SFTP protocol, and the AWS Transfer Family stores them as S3 objects in the landing zone in the data lake. The AWS Transfer Family supports encryption using AWS KMS and common authentication methods including [*AWS Identity and Access Management*](https://aws.amazon.com/iam) (IAM) and Active Directory. 

## Data APIs
<a name="data-apis"></a>

 Organizations today use SaaS and partner applications such as Salesforce, Marketo, and Google Analytics to support their business operations. Analyzing SaaS and partner data in combination with internal operational application data is critical to gaining 360- degree business insights. Partner and SaaS applications often provide API endpoints to share data. 

### SaaS APIs
<a name="saas-apis"></a>

 The ingestion layer uses [Amazon AppFlow](https://aws.amazon.com/appflow/) to easily ingest SaaS applications data into the data lake. With a few clicks, you can set up serverless data ingestion flows in Amazon AppFlow. Your flows can connect to SaaS applications (such as Salesforce, Marketo, and Google Analytics), ingest data, and store it in the data lake. You can schedule Amazon AppFlow data ingestion flows or trigger them by events in the SaaS application. Ingested data can be validated, filtered, mapped, and masked before storing in the data lake. Amazon AppFlow natively integrates with authentication, authorization, and encryption services in the security and governance layer. 

### Partner APIs
<a name="partner-apis"></a>

 To ingest data from partner and third-party APIs, organizations build or purchase custom applications that connect to APIs, fetch data, and create S3 objects in the landing zone by using [AWS SDKs](https://aws.amazon.com/tools/). These applications and their dependencies can be packaged into Docker containers and hosted on [AWS Fargate](https://aws.amazon.com/fargate/). Fargate is a serverless compute engine for hosting Docker containers without having to provision, manage, and scale servers. Fargate natively integrates with AWS security and monitoring services to provide encryption, authorization, network isolation, logging, and monitoring to the application containers. 

 AWS Glue Python shell jobs also provide serverless alternative to build and schedule data ingestion jobs that can interact with partner APIs by using native, open-source, or partner-provided Python libraries. AWS Glue provides out-of-the-box capabilities to schedule singular Python shell jobs or include them as part of a more complex data ingestion workflow built on AWS Glue workflows. 

### Third-party data sources
<a name="third-party-data-sources"></a>

 Your organization can gain a business edge by combining your internal data with third- party datasets such as historical demographics, weather data, and consumer behavior data. [AWS Data Exchange](https://aws.amazon.com/data-exchange/) provides a serverless way to find, subscribe to, and ingest third-party data directly into Amazon S3 buckets in the data lake landing zone. You can ingest a full third-party dataset and then automate detecting and ingesting revisions to that dataset. AWS Data Exchange is serverless and lets you find and ingest third-party datasets with a few clicks. 

# Storage layer
<a name="storage-layer-1"></a>

 Amazon S3 provides the foundation for the storage layer in our architecture. Amazon S3 provides virtually unlimited scalability at low cost for our serverless data lake. Data is stored as S3 objects organized into raw, cleaned, and curated zone buckets, and prefixes. Amazon S3 encrypts data using keys managed in AWS KMS. IAM policies control granular zone-level and dataset-level access to various users and roles. 

 Amazon S3 provides 99.99% of availability and 99.999999999% of durability, and charges only for the data it stores. To significantly reduce costs, Amazon S3 provides colder tier storage options called [Amazon Glacier and S3 Glacier Deep Archive](https://aws.amazon.com/glacier/). To automate cost optimizations, Amazon S3 provides configurable lifecycle policies and S3 Intelligent-Tiering options to automate moving older data to colder tiers. AWS services in our ingestion, cataloging, processing, and consumption layers can natively read and write S3 objects. Additionally, hundreds of third-party vendor and open-source products and services provide the ability to read and write S3 objects. 

 Data of any structure (including unstructured data) and any format can be stored as S3 objects without needing to predefine any schema. This enables services in the ingestion layer to quickly land a variety of source data into the data lake in its original source format. After the data is ingested into the data lake, components in the processing layer can define schema on top of Amazon S3 datasets and register them in the cataloging layer. Services in the processing and consumption layers can then use schema-on-read to apply the required structure to data read from S3 objects. Datasets stored in Amazon S3 are often partitioned to enable efficient filtering by services in the processing and consumption layers. 

# Cataloging and search layer
<a name="cataloging-and-search-layer-1"></a>

 A data lake typically hosts many datasets which have evolving schema and new data partitions. A central data catalog that manages metadata for all the datasets in the data lake is crucial to enabling self-service discovery of data in the data lake. Additionally, separating metadata from data into a central schema enables schema-on-read for the processing and consumption layer components. 

 In the presented architecture, Lake Formation provides the central catalog to store and manage metadata for all datasets hosted in the data lake. Organizations manage both technical metadata (such as versioned table schemas, partitioning information, physical data location, and update timestamps) and business attributes (such as data owner, data steward, column business definition, and column information sensitivity) of all their datasets in Lake Formation. Services such as AWS Glue, [Amazon EMR](https://aws.amazon.com/emr/), and [Amazon Athena](https://aws.amazon.com/athena/) natively integrate with Lake Formation and automate discovering and registering dataset metadata into the Lake Formation catalog. Additionally, Lake Formation provides APIs to enable metadata registration and management using custom scripts and third-party products. [AWS Glue crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) in the processing layer can track evolving schemas and newly added partitions of datasets in the data lake, and add new versions of corresponding metadata in the Lake Formation catalog. 

 Lake Formation provides the data lake administrator a central place to set up granular table and column level permissions for databases and tables hosted in the data lake. After Lake Formation permissions are set up, users and groups can access only authorized tables and columns using multiple processing and consumption layer services such as Athena, Amazon EMR, AWS Glue, and Amazon Redshift Spectrum. 

# Processing layer
<a name="processing-layer-1"></a>

 The processing layer in our architecture is composed of two types of components: 
+  Components used to create multi-step data processing pipelines. 
+  Components to orchestrate data processing pipelines on schedule or in response to event triggers (such as ingestion of new data into the landing zone). 

 AWS Glue and [AWS Step Functions](https://aws.amazon.com/step-functions/) provide serverless components to build, orchestrate, and run pipelines that can easily scale to process large data volumes. Multi-step workflows built using AWS Glue and Step Functions can catalog, validate, clean, transform, and enrich individual datasets and advance them from raw to cleaned and cleaned to curated zones in the storage layer. 

 AWS Glue is a serverless, pay-per-use ETL service for building and running Python or Spark jobs (written in [Scala](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-scala.html) or [Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html)) without requiring you to deploy or manage clusters. [AWS Glue automatically generates the code](https://aws.amazon.com/blogs/big-data/simplify-data-pipelines-with-aws-glue-automatic-code-generation-and-workflows/) to accelerate your data transformations and loading processes. AWS Glue ETL builds on top of Apache Spark and provides commonly used out-of-the-box data source connectors, [data structures](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html), and [ETL transformations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html) to validate, clean, transform, and flatten data stored in many open-source formats such as CSV, JSON, Parquet, and Avro. AWS Glue ETL also provides capabilities to incrementally process partitioned data. 

 Additionally, you can use AWS Glue to define and run [crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) that can crawl folders in the data lake, discover datasets and their partitions, infer schema, and define tables in the Lake Formation catalog. AWS Glue provides more than a dozen [built-in classifiers](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html) that can parse a variety of data structures stored in open-source formats. AWS Glue also provides [triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html) and [workflow capabilities](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) that you can use to build multi-step end- to-end data processing pipelines that include job dependencies and running parallel steps. You can schedule AWS Glue jobs and workflows or run them on demand. AWS Glue natively integrates with AWS services in storage, catalog, and [security](https://docs.aws.amazon.com/glue/latest/dg/security.html) layers. 

 To make it easy to clean and normalize data, Glue also provides a visual data preparation tool called AWS Glue DataBrew which is an interactive, point-and-click visual interface without requiring to write any code. 

 Step Functions is a serverless engine that you can use to build and orchestrate scheduled or event-driven data processing workflows. You use Step Functions to build complex data processing pipelines that involve orchestrating steps implemented by using multiple AWS services such as AWS Glue, [AWS Lambda](https://aws.amazon.com/lambda), [*Amazon Elastic Container Service*](https://aws.amazon.com/ecs) (Amazon ECS) containers, and more. Step Functions provides visual representations of complex workflows and their running state to make them easy to understand. It manages state, checkpoints, and restarts of the workflow for you to make sure that the steps in your data pipeline run in order and as expected. Built-in try/catch, retry, and rollback capabilities deal with errors and exceptions automatically. 

# Consumption layer
<a name="consumption-layer-1"></a>

 The consumption layer in the presented architecture is composed using fully managed, purpose-built, analytics services that enable interactive SQL, BI dashboarding, batch processing, and ML. 

## Interactive SQL
<a name="interactive-sql"></a>

 Amazon Athena is an interactive query service that enables you to run complex ANSI SQL against terabytes of data stored in Amazon S3 without needing to first load it into a database. Athena queries can analyze structured, semi-structured, and columnar data stored in open-source formats such as CSV, JSON, XML Avro, Parquet, and ORC. Athena uses table definitions from Lake Formation to apply schema-on-read to data read from Amazon S3. 

 Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the amount of data scanned by the queries you run. Athena provides faster results and lower costs by reducing the amount of data it scans by using [dataset partitioning information](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) stored in the Lake Formation catalog. You can run queries directly on the Athena console of submit them using [Athena JDBC or ODBC endpoints](https://docs.aws.amazon.com/athena/latest/ug/athena-bi-tools-jdbc-odbc.html). 

 Federated queries in Amazon Athena enable users to run SQL queries across data stored in relational, non-relational, object, and custom data sources. Athena can run federated queries using [Athena Data Source Connectors](https://docs.aws.amazon.com/athena/latest/ug/writing-federated-queries.html) that run on AWS Lambda. 

 Athena natively integrates with AWS services in the [security and monitoring layer](https://docs.aws.amazon.com/athena/latest/ug/security.html) to support authentication, authorization, encryption, logging, and monitoring. It supports table- and column-level access controls defined in the Lake Formation catalog. 

## Data warehousing and batch analytics
<a name="data-warehousing-and-batch-analytics"></a>

 Amazon Redshift is a fully managed data warehouse service that can host and process petabytes of data and run thousands highly performant queries in parallel. Amazon Redshift uses a cluster of compute nodes to run very low-latency queries to power interactive dashboards and high-throughput batch analytics to drive business decisions. You can run Amazon Redshift queries directly on the Amazon Redshift console or submit them using the JDBC/ODBC endpoints provided by Amazon Redshift. 

 Amazon Redshift provides the capability, called [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html), to perform in-place [queries on structured and semi-structured datasets in Amazon S3](https://aws.amazon.com/blogs/big-data/amazon-redshift-spectrum-extends-data-warehousing-out-to-exabytes-no-loading-required/) without needing to load it into the cluster. Amazon Redshift Spectrum can spin up thousands of query-specific temporary nodes to scan exabytes of data to deliver fast results. 

 Organizations typically load most frequently accessed dimension and fact data into an Amazon Redshift cluster and keep up to exabytes of structured, semi-structured, and unstructured historical data in Amazon S3. Amazon Redshift Spectrum enables running complex queries that combine data in a cluster with data on Amazon S3 in the same query. 

 Another capability to enable fast sharing between your data warehouse and data lake is [Amazon Redshift data lake export](https://aws.amazon.com/blogs/aws/new-for-amazon-redshift-data-lake-export-and-federated-queries/). You can now unload the result of an Amazon Redshift query to your Amazon S3 data lake as Apache Parquet. This enables you to save data transformation and enrichment you have done in Amazon Redshift into your Amazon S3 data lake in an open format. You can then analyze your data with Redshift Spectrum and other AWS services such as Amazon Athena, Amazon EMR, and Amazon SageMaker AI. 

 Amazon Redshift provides native integration with Amazon S3 in the storage layer, Lake Formation catalog, and AWS services in the security and monitoring layer. 

## Business intelligence
<a name="business-intelligence"></a>

 Quick provides a serverless BI capability to easily create and publish rich, interactive dashboards. QuickSight enriches dashboards and visuals with out-of-the- box, automatically generated ML insights such as forecasting, anomaly detection, and narrative highlights. QuickSight natively integrates with Amazon SageMaker AI to enable additional custom ML model-based insights to your BI dashboards. You can access QuickSight dashboards from any device using a QuickSight app, or you can [embed the dashboard into web applications, portals, and websites](https://docs.aws.amazon.com/quicksight/latest/user/embedding-dashboards.html). 

 QuickSight allows you to directly connect to and import data from a wide variety of cloud and on-premises data sources. 
+  SaaS applications, such as Salesforce, Square, ServiceNow, Twitter, GitHub, and JIRA 
+  Third-party databases, such as Teradata, MySQL, Postgres, and SQL Server 
+  Native AWS services, such as Amazon Redshift, Athena, Amazon S3, Amazon Relational Database Service (Amazon RDS), and [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 
+  Private VPC subnets 

 You can also upload a variety of file types including XLS, CSV, JSON, and Presto. 

 To achieve blazing fast performance for dashboards, QuickSight provides an in-memory caching and calculation engine called SPICE. SPICE automatically replicates data for high availability and enables thousands of users to simultaneously perform fast, interactive analysis while shielding your underlying data infrastructure. QuickSight automatically scales to tens of thousands of users and provides a cost-effective, pay- per-session pricing model. 

 QuickSight allows you to securely manage your users and content via a comprehensive set of security features, including role-based access control, Active Directory integration, [AWS CloudTrail](https://aws.amazon.com/cloudtrail) auditing, single sign-on (IAM or third-party), private VPC subnets, and data backup. 

## Predictive analytics and ML
<a name="predictive-analytics-and-ml"></a>

 Amazon SageMaker AI is a fully managed service that provides components to build, train, and deploy ML models using an interactive development environment (IDE) called [Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/aws/amazon-sagemaker-studio-the-first-fully-integrated-development-environment-for-machine-learning/). In Amazon SageMaker AI Studio, you can upload data, create new notebooks, train and tune models, move back and forth between steps to adjust experiments, compare results, and deploy models to production, all in one place by using a unified visual interface. Amazon SageMaker AI also provides [managed Jupyter notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) that you can spin up with just a few clicks. Amazon SageMaker AI notebooks provide elastic compute resources, git integration, easy sharing, pre-configured ML algorithms, dozens of out-of-the-box ML examples, and *AWS Marketplace* integration, which enables easy deployment of hundreds of pre-trained algorithms. Amazon SageMaker AI notebooks are preconfigured with all major deep learning frameworks, including TensorFlow, PyTorch, Apache MXNet, Chainer, Keras, Gluon, Horovod, Scikit-learn, and Deep Graph Library. 

 ML models are trained on Amazon SageMaker AI managed compute instances, including highly cost-effective Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances. 

 You can organize multiple training jobs by using [Amazon SageMaker AI Experiments](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/). You can build training jobs using Amazon SageMaker AI built-in algorithms, your custom algorithms, or hundreds of algorithms you can deploy from AWS Marketplace. Amazon SageMaker AI Debugger provides full visibility into model training jobs. Amazon SageMaker AI also provides automatic hyperparameter tuning for ML training jobs. 

 You can [deploy Amazon SageMaker AI trained models](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) into production with a few clicks and easily scale them across a fleet of fully managed EC2 instances. You can choose from multiple EC2 instance types and attach cost-effective [GPU-powered inference acceleration](https://docs.aws.amazon.com/sagemaker/latest/dg/ei.html). After the models are deployed, Amazon SageMaker AI can [monitor key model metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html) for inference accuracy and detect any concept drift. 

 Amazon SageMaker AI provides native integrations with AWS services in the storage and security layers. 

# Security and governance layer
<a name="security-and-governance-layer-1"></a>

 Components across all layers of the presented architecture protect data, identities, and processing resources by natively using the following capabilities provided by the security and governance layer. 

## Authentication and authorization
<a name="authentication-and-authorization"></a>

 AWS Identity and Access Management (IAM) provides user-, group-, and role-level identity to users and the ability to configure fine-grained access control for resources managed by AWS services in all layers of our architecture. IAM supports multi-factor authentication and single sign-on through integrations with corporate directories and open identity providers such as Google, Facebook, and Amazon. 

 [Lake Formation provides a simple and centralized authorization model](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html) for tables hosted in the data lake. After implemented in Lake Formation, authorization policies for databases and tables are enforced by [other AWS services](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html#service-integrations) such as Athena, Amazon EMR, QuickSight, and Amazon Redshift Spectrum. In Lake Formation, you can grant or revoke database-, table-, or column-level access for IAM users, groups, or roles defined in the same account hosting the Lake Formation catalog or [another AWS account](https://docs.aws.amazon.com/lake-formation/latest/dg/crosss-account-how-works.html). The simple grant/revoke-based authorization model of Lake Formation considerably simplifies the previous IAM-based authorization model that relied on separately securing S3 data objects and metadata objects in the AWS AWS Glue Data Catalog. 

## Encryption
<a name="encryption"></a>

 AWS KMS provides the capability to create and manage symmetric and asymmetric customer managed encryption keys. AWS services in all layers of our architecture natively integrate with AWS KMS to encrypt data in the data lake. It supports both creating new keys and importing existing customer keys. Access to the encryption keys is controlled using IAM and is monitored through detailed audit trails in CloudTrail. 

## Network protection
<a name="network-protection"></a>

 Our architecture uses [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) to provision a logically isolated section of the AWS Cloud (called VPC) that is isolated from the internet and other AWS customers. Amazon VPC provides the ability to choose your own IP address range, create subnets, and configure route tables and network gateways. AWS services from other layers in our architecture launch resources in this private VPC to protect all traffic to and from these resources. 

## Monitoring and logging
<a name="monitoring-and-logging"></a>

 AWS services in all layers of our architecture store detailed logs and monitoring metrics in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). CloudWatch provides the ability to analyze logs, visualize monitored metrics, define monitoring thresholds, and send alerts when thresholds are crossed. 

 All AWS services in our architecture also store extensive audit trails of user and service actions in CloudTrail. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console (login required), AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting. 

# Conclusion
<a name="conclusion"></a>

 With AWS serverless and managed services, you can build a modern, low-cost data lake centric analytics architecture in days. A decoupled, component-driven architecture enables you to start small and quickly add new purpose-built components to one of six architecture layers to address new requirements and data sources. 

# Further reading
<a name="further-reading"></a>

 The following posts contain detailed walkthroughs and sample code for building the components of the serverless data lake centric analytics architecture: 
+  [Load ongoing data lake changes with AWS DMS and AWS Glue](https://aws.amazon.com/blogs/big-data/loading-ongoing-data-lake-changes-with-aws-dms-and-aws-glue/) 
+  Discover metadata with AWS Lake Formation: [Part 1](https://aws.amazon.com/blogs/big-data/discovering-metadata-with-aws-lake-formation-part-1/) and [Part 2](https://aws.amazon.com/blogs/big-data/discover-metadata-with-aws-lake-formation-part-2/) 
+  [Build a Data Lake Foundation with AWS Glue and Amazon S3 ](https://aws.amazon.com/blogs/big-data/build-a-data-lake-foundation-with-aws-glue-and-amazon-s3/)
+  [Process data with varying data ingestion frequencies using AWS Glue job bookmarks](https://aws.amazon.com/blogs/big-data/process-data-with-varying-data-ingestion-frequencies-using-aws-glue-job-bookmarks/) 
+  [Orchestrate Amazon Redshift-Based ETL workflows with AWS Step Functions and AWS Glue](https://aws.amazon.com/blogs/big-data/orchestrate-amazon-redshift-based-etl-workflows-with-aws-step-functions-and-aws-glue/) 
+  [Analyze your Amazon S3 spend using AWS Glue and Amazon Redshift](https://aws.amazon.com/blogs/big-data/analyze-your-amazon-s3-spend-using-aws-glue-and-amazon-redshift/) 
+  [From Data Lake to Data Warehouse: Enhancing Customer 360 with Amazon Redshift Spectrum](https://aws.amazon.com/blogs/big-data/from-data-lake-to-data-warehouse-enhancing-customer-360-with-amazon-redshift-spectrum/) 
+  [Extract, Transform and Load data into S3 data lake using CTAS and INSERT INTO statements in Amazon Athena](https://aws.amazon.com/blogs/big-data/extract-transform-and-load-data-into-s3-data-lake-using-ctas-and-insert-into-statements-in-amazon-athena/) 
+  [Derive Insights from IoT in Minutes using AWS IoT, Amazon Kinesis Firehose, Amazon Athena, and Quick](https://aws.amazon.com/blogs/big-data/derive-insights-from-iot-in-minutes-using-aws-iot-amazon-kinesis-firehose-amazon-athena-and-amazon-quicksight/) 
+  [Our data lake story: How Woot.com built a serverless data lake on AWS](https://aws.amazon.com/blogs/big-data/our-data-lake-story-how-woot-com-built-a-serverless-data-lake-on-aws/) 
+  [Predicting all-cause patient readmission risk using AWS data lake and machine learning](https://aws.amazon.com/blogs/industries/predicting-all-cause-patient-readmission-risk-using-aws-data-lake-and-machine-learning/) 

# Contributors
<a name="contributors"></a>

 Contributors to this document include: 
+  Changbin Gong, Solutions Architect, Amazon Web Services 
+  Praful Kava, Solutions Architect, Amazon Web Services 

# Document revisions
<a name="document-revisions"></a>

To be notified about updates to this whitepaper, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#document-revisions) | Whitepaper published. | April 7, 2021 | 

# Notices
<a name="notices"></a>

 Customers are responsible for making their own independent assessment of the information in this document. This document: (a) is for informational purposes only, (b) represents current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers. 

 © 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. 

# AWS Glossary
<a name="glossary"></a>

For the latest AWS terminology, see the [AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary Reference*.