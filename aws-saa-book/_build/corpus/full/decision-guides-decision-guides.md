# AWS Decision Guides Consolidated Reference

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
+ [What are AWS decision guides?](#what-are-decision-guides)
+ [How to use this guide](#how-to-use-this-guide)
+ [Choosing an AWS analytics service](#analytics-on-aws-how-to-choose)
+ [Compute](#compute)
   + [Choosing an AWS compute service](#choosing-aws-compute-service)
   + [Choosing an AWS container service](#choosing-aws-container-service)
   + [AWS Fargate or AWS Lambda?](#fargate-or-lambda)
   + [Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2?](#lightsail-elastic-beanstalk-ec2)
   + [Choosing a modern application strategy](#modern-apps-strategy-on-aws-how-to-choose)
   + [Choosing a purchasing option for Amazon EC2](#ec2-purchasing-options-aws-how-to-choose)
+ [Storage & Databases](#storage-databases)
   + [Choosing an AWS storage service](#choosing-aws-storage-service)
   + [Choosing an AWS database service](#databases-on-aws-how-to-choose)
+ [Choosing AWS frontend web and mobile services](#front-end-mobile)
+ [Machine Learning](#machine-learning)
   + [Choosing a generative AI service](#genai-guide)
   + [Choosing an AWS machine learning service](#ml-guide)
   + [Amazon Bedrock or Amazon SageMaker AI?](#bedrock-or-sagemaker)
+ [Management & Governance](#management-governance)
   + [Choosing an AWS monitoring and observability service](#monitoring-on-aws-how-to-choose)
   + [AWS CloudTrail or Amazon CloudWatch?](#cloudtrail-or-cloudwatch)
   + [Choosing an AWS cloud governance service](#cloud-governance-on-aws-how-to-choose)
   + [Choosing an AWS cost management strategy](#cost-management-on-aws-how-to-choose)
+ [Migration & IoT](#migration-and-iot)
   + [Choosing AWS migration services and tools](#migration-on-aws-how-to-choose)
   + [Choosing an AWS IoT service](#iot)
+ [Choosing an AWS networking and content delivery service](#choosing-networking-and-content-delivery-service)
+ [Security, identity, and compliance](#security-identity-compliance)
   + [Choosing AWS security, identity, and governance services](#choosing-aws-security-services)
   + [Choosing an AWS identity service](#identity-on-aws-how-to-choose)
   + [Choosing an AWS cryptography service](#guide)
   + [AWS WAF or AWS Shield?](#waf-or-shield)
+ [Serverless & Application Integration](#application-integration)
   + [Choosing an AWS serverless service](#choosing-aws-serverless-service)
   + [Choosing an AWS application integration service](#application-integration-on-aws-how-to-choose)
   + [Amazon SQS, Amazon SNS, or Amazon EventBridge?](#sns-or-sqs-or-eventbridge)
+ [Additional resources](#additional-resources)
+ [Document history](#document-history)

-----



# What are AWS decision guides?
<a name="what-are-decision-guides"></a>

Decision guides are designed to provide you with a detailed overview of the services offered by AWS, and structured guidance on how to choose the services that might be right for your use cases. Decision guides can also help you articulate and consider the criteria that will inform your choices. AWS offers services across many technology categories, and choosing the right service for your workload can be challenging. Decision guides simplify this process by organizing services into categories and providing structured frameworks for evaluation.

Some guides cover an entire service category, such as compute or databases, and help you choose among multiple options. Others compare two or three specific services head-to-head when you've narrowed your choices and need to understand the detailed differences.

## Who should use decision guides?
<a name="who-should-use"></a>

Decision guides are useful for the following audiences:
+ **Technical decision makers** — CTOs, solutions architects, and engineering leads evaluating and selecting AWS services for their organizations.
+ **Developers** — Software engineers choosing between services for specific implementation requirements.
+ **Cloud practitioners** — People getting started with AWS who need guidance on which services to use for common workloads.

# How to use this guide
<a name="how-to-use-this-guide"></a>

This guide organizes all AWS decision guides into a decision tree. Start with your high-level goal, then navigate to the section that matches your needs.

## Analytics
<a name="category-analytics"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Analyze data at scale | [Choosing an AWS analytics service](#analytics-on-aws-how-to-choose) | 

## Compute
<a name="category-compute"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Run compute workloads (VMs, containers, serverless) | [Choosing an AWS compute service](#choosing-aws-compute-service) | 
| Run containerized workloads | [Choosing an AWS container service](#choosing-aws-container-service) | 
| Choose between AWS Fargate and AWS Lambda | [AWS Fargate or AWS Lambda?](#fargate-or-lambda) | 
| Choose between Amazon Lightsail, AWS Elastic Beanstalk, and Amazon EC2 | [Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2?](#lightsail-elastic-beanstalk-ec2) | 
| Modernize applications | [Choosing a modern application strategy](#modern-apps-strategy-on-aws-how-to-choose) | 

**Tip**  
The comparison guides for Fargate vs. Lambda and Lightsail vs. Elastic Beanstalk vs. EC2 provide deeper guidance after you've used the compute category guide to narrow your options.

## Databases
<a name="category-databases"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Choose a database service | [Choosing an AWS database service](#databases-on-aws-how-to-choose) | 

## Front-End Web & Mobile
<a name="category-frontend"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Build frontend web or mobile apps | [Choosing AWS frontend web and mobile services](#front-end-mobile) | 

## Internet of Things (IoT)
<a name="category-iot"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Build IoT solutions | [Choosing an AWS IoT service](#iot) | 

## Machine Learning
<a name="category-machine-learning"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Build generative AI applications | [Choosing a generative AI service](#genai-guide) | 
| Build or deploy ML models | [Choosing an AWS machine learning service](#ml-guide) | 
| Choose between Amazon Bedrock and Amazon SageMaker AI | [Amazon Bedrock or Amazon SageMaker AI?](#bedrock-or-sagemaker) | 

**Tip**  
The Amazon Bedrock or Amazon SageMaker AI comparison guide provides deeper guidance after you've used the generative AI or machine learning category guides to narrow your options.

## Management & Governance
<a name="category-management"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Monitor and observe workloads | [Choosing an AWS monitoring and observability service](#monitoring-on-aws-how-to-choose) | 
| Choose between AWS CloudTrail and Amazon CloudWatch | [AWS CloudTrail or Amazon CloudWatch?](#cloudtrail-or-cloudwatch) | 
| Manage cloud governance | [Choosing an AWS cloud governance service](#cloud-governance-on-aws-how-to-choose) | 
| Manage costs | [Choosing an AWS cost management strategy](#cost-management-on-aws-how-to-choose) | 

**Tip**  
The AWS CloudTrail or Amazon CloudWatch comparison guide helps you understand the differences between audit logging and operational monitoring.

## Migration & Transfer
<a name="category-migration"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Migrate workloads to AWS | [Choosing AWS migration services and tools](#migration-on-aws-how-to-choose) | 

## Networking & Content Delivery
<a name="category-networking"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Set up networking, VPNs, CDN, or load balancing | [Choosing an AWS networking and content delivery service](#choosing-networking-and-content-delivery-service) | 

## Security, Identity, & Compliance
<a name="category-security"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Choose security and governance services | [Choosing AWS security, identity, and governance services](#choosing-aws-security-services) | 
| Choose an identity service | [Choosing an AWS identity service](#identity-on-aws-how-to-choose) | 
| Choose a cryptography service | [Choosing an AWS cryptography service](#guide) | 
| Choose between AWS WAF and AWS Shield | [AWS WAF or AWS Shield?](#waf-or-shield) | 

**Tip**  
The AWS WAF or AWS Shield comparison guide provides deeper guidance on choosing between web application firewall and DDoS protection services.

## Serverless & Application Integration
<a name="category-app-integration"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Choose serverless services for your workload | [Choosing an AWS serverless service](#choosing-aws-serverless-service) | 
| Integrate applications (queues, events, workflows) | [Choosing an AWS application integration service](#application-integration-on-aws-how-to-choose) | 
| Choose between Amazon Simple Queue Service, Amazon Simple Notification Service, and Amazon EventBridge | [Amazon Simple Queue Service, Amazon Simple Notification Service, or EventBridge?](#sns-or-sqs-or-eventbridge) | 

## Storage
<a name="category-storage"></a>


| Your goal | Recommended guide | 
| --- | --- | 
| Choose a storage service | [Choosing an AWS storage service](#choosing-aws-storage-service) | 

# Choosing an AWS analytics service
<a name="analytics-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS analytics services are the best fit for your organization. | 
| **Last updated** | September 24, 2025 | 
| **Covered services** |  +  [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) <br />+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html#first-time-user) <br />+   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) <br />+  [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html) <br />+  [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) <br />+  [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html) <br />+  [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/examples.html) <br />+  [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) <br />+  [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) <br />+  [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) <br />+  [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) <br />+  [Quick](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html) <br />+  [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) <br />+  [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) <br />+  [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker/)   | 

## Introduction
<a name="intro"></a>

Data is foundational to modern business. People and applications need to securely access and analyze data, which comes from new and diverse sources. The volume of data is also constantly increasing, which can cause organizations to struggle with capturing, storing, and analyzing all the necessary data.

Meeting these challenges means building a modern data architecture that breaks down all of your data silos for analytics and insights--including third-party data--and makes it accessible to everyone in the organization, in one place, with end-to-end governance. It's also increasingly important to connect your analytics and machine learning (ML) systems to enable predictive analytics. 

This decision guide helps you ask the right questions to build your modern data architecture on AWS services. It explains how to break down your data silos (by connecting your data lake and data warehouses), your system silos (by connecting ML and analytics), and your people silos (by putting data in the hands of everyone in your organization).

[![AWS Videos](https://img.youtube.com/vi/9Y1bwAmx0Do?start=397&end=848/0.jpg)](https://www.youtube.com/watch?v=9Y1bwAmx0Do?start=397&end=848)


## Understand AWS analytics services
<a name="understand"></a>

A modern data strategy is built with a set of technology building blocks that help you manage, access, analyze, and act on data. It also gives you multiple options to connect to data sources. A modern data strategy should empower your teams to:
+ Use your preferred tools or techniques
+ Use artificial intelligence (AI) to assist with finding answers to specific questions about your data
+ Manage who has access to data with the proper security and data governance controls
+ Break down data silos to give you the best of both data lakes and purpose-built data stores
+ Store any amount of data, at low-cost, and in open, standards-based data formats
+ Connect your data lakes, data warehouses, operational databases, applications, and federated data sources into a coherent whole

AWS offers a variety of services to help you achieve a modern data strategy. The following diagram depicts the AWS services for analytics that this guide covers. The tabs that follow provide additional details.

![Diagram showing the AWS analytics services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/analytics-services.png)


------
#### [ Unified analytics and AI ]

The next generation of [Amazon SageMaker](https://aws.amazon.com/sagemaker/) combines widely adopted AWS machine learning (ML) and analytics capabilities to deliver an integrated experience for analytics and AI, providing unified access to all your data. Using [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html), you can collaborate and build faster with familiar AWS tools for model development, generative AI application development, data processing, and SQL analytics, all accelerated by Amazon Q Developer, our generative AI assistant for software development. Access your data from data lakes, data warehouses, or third-party and federated sources, with built-in governance to meet enterprise security requirements. 

------
#### [ Data processing ]
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) helps you analyze unstructured, semi-structured, and structured data stored in Amazon S3. Examples include CSV, JSON, or columnar data formats such as Apache Parquet and Apache ORC. You can use Athena to run ad-hoc queries using ANSI SQL, without the need to aggregate or load the data into Athena. Athena integrates with Quick, AWS Glue Data Catalog, and [other AWS services](https://docs.aws.amazon.com/athena/latest/ug/athena-aws-service-integrations.html). You can also analyze data at scale with [Trino](https://trino.io/), without needing to manage infrastructure, and build real-time analytics using Apache Flink and Apache Spark.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data. Using these frameworks and related open-source projects, you can process data for analytics purposes and business intelligence workloads. Amazon EMR also lets you transform and move large amounts of data into and out of other AWS data stores and databases, such as Amazon S3.
+ With [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html), you can discover and connect to more than 100 diverse data sources and manage your data in a centralized data catalog. You can visually create, run, and monitor ETL pipelines to load data into your data lakes. Also, you can immediately search and query cataloged data using Athena, Amazon EMR, and Amazon Redshift Spectrum. 
+ [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) (MWAA) is a fully managed implementation of Apache Airflow that makes it easier to create, schedule, and monitor data workflows in the cloud. MWAA automatically scales workflow capacity to meet your needs and integrates with AWS security services. You can use MWAA to orchestrate workflows across your analytics services, including data processing, ETL jobs, and machine learning pipelines.

------
#### [ Data streaming ]
+ With [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) (Amazon MSK), you can build and run applications that use Apache Kafka to process streaming data. Amazon MSK provides the control-plane operations, such as those for creating, updating, and deleting clusters. It lets you use Apache Kafka data-plane operations, such as those for producing and consuming data.
+ With [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/examples.html), you can collect and process large streams of data records in real time. The type of data used can include IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) is a fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Splunk, and Apache Iceberg Tables. You can also send data to any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, Coralogix, and Elastic. 
+  With [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html), you can use Java, Scala, Python, or SQL to process and analyze streaming data. You can author and run code against streaming sources and static sources to perform time-series analytics, feed real-time dashboards, and metrics. 

------
#### [ Business intelligence ]

[Quick](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html) gives decision-makers the opportunity to explore and interpret information in an interactive visual environment. In a single data dashboard, Quick can include AWS data, third-party data, big data, spreadsheet data, SaaS data, B2B data, and more. With Quick Q, you can use natural language to ask questions about your data and receive a response. For example, "What are the top-selling categories in California?"

------
#### [ Search analytics ]

[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) provisions all the resources for your OpenSearch cluster and launches it. It also automatically detects and replaces failed OpenSearch Service nodes, reducing the overhead associated with self-managed infrastructures. You can use OpenSearch Service direct query to analyze data in Amazon S3 and other AWS services. 

------
#### [ Data governance ]

With [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html), you can manage and govern access to data by using fine-grained controls. These controls help ensure access with the right level of privileges and context. Amazon DataZone simplifies your architecture by integrating data management services, including Amazon Redshift, Athena, Quick, AWS Glue, on-premises sources, and third-party sources.

------
#### [ Data collaboration ]

[AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html) is a secure collaboration workspace where you can analyze collective datasets without providing access to the raw data. You can collaborate with other companies by choosing the partners with whom you want to collaborate, selecting their datasets, and configuring privacy-enhancing controls for those partners. When you run queries, AWS Clean Rooms reads data from that data's original location and applies built-in analysis rules to help you maintain control over that data.

------
#### [ Data lake and data warehouse ]
+ [The next generation of Amazon SageMaker](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/lakehouse-get-started.html) is fully compatible with Apache Iceberg, allowing you to unify data across Amazon Simple Storage Service (Amazon S3) data lakes and Amazon Redshift data warehouses. This enables building analytics and AI and machine learning (ML) applications on a single data copy. Through zero-ETL integrations, you can stream data from operational sources in near real-time, run federated queries across multiple sources, and access data with Apache Iceberg–compatible tools. You can secure your data by defining fine-grained permissions that are enforced across all your analytics and ML tools and engines.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) can store and protect virtually any amount and kind of data, which you can use for your data lake foundation. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements. Amazon S3 Tables provide S3 storage that’s optimized for analytics workloads. Using standard SQL statements, you can query your tables with query engines that support Iceberg, such as Athena, Amazon Redshift, and Apache Spark.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) is a fully managed, petabyte-scale data warehouse service. Amazon Redshift can be connected to a data lakehouse in Amazon SageMaker, allowing you to use its powerful SQL analytic capabilities on your unified data across Amazon Redshift data warehouses and Amazon S3 data lakes. You can also use Amazon Q in Amazon Redshift, which simplifies SQL authoring through natural language. 

------

## Consider criteria for AWS analytics services
<a name="consider"></a>

There are many reasons for building data analytics on AWS. You might need to support a greenfield or pilot project as a first step in your cloud migration journey. Alternatively, you might be migrating an existing workload with as little disruption as possible. Whatever your goal, the following considerations can be useful in making your choice.

------
#### [ Assess data sources and data types ]

Analyze available data sources and data types to gain a comprehensive understanding of data diversity, frequency, and quality. Understand any potential challenges in processing and analyzing the data. This analysis is crucial because:
+ Data sources are diverse and come from various systems, applications, devices, and external platforms.
+ Data sources have unique structure, format, and frequency of data updates. Analyzing these sources helps in identifying suitable data collection methods and technologies.
+ Analyzing data types, such as structured, semi-structured, and unstructured data determines the appropriate data processing and storage approaches.
+ Analyzing data sources and types facilitates data quality assessment, helps you anticipate potential data quality issues—missing values, inconsistencies, or inaccuracies.

------
#### [ Data processing requirements ]

Determine data processing requirements for how data is ingested, transformed, cleansed, and prepared for analysis. Key considerations include:
+ **Data transformation:** Determine the specific transformations needed to make the raw data suitable for analysis. This involves tasks like data aggregation, normalization, filtering, and enrichment.
+ **Data cleansing:** Assess data quality and define processes to handle missing, inaccurate, or inconsistent data. Implement data cleansing techniques to ensure high-quality data for reliable insights.
+ **Processing frequency:** Determine whether real-time, near real-time, or batch processing is required based on the analytical needs. Real-time processing enables immediate insights, while batch processing may be sufficient for periodic analyses.
+ **Scalability and throughput:** Evaluate the scalability requirements for handling data volumes, processing speed, and the number of concurrent data requests. Ensure that the chosen processing approach can accommodate future growth.
+ **Latency:** Consider the acceptable latency for data processing and the time it takes from data ingestion to analysis results. This is particularly important for real-time or time-sensitive analytics.

------
#### [ Storage requirements ]

Determine storage needs by determining how and where data is stored throughout the analytics pipeline. Important considerations include:
+ **Data volume:** Assess the amount of data being generated and collected, and estimate future data growth to plan for sufficient storage capacity.
+ **Data retention:** Define the duration for which data should be retained for historical analysis or compliance purposes. Determine the appropriate data retention policies.
+ **Data access patterns:** Understand how data will be accessed and queried to choose the most suitable storage solution. Consider read and write operations, data access frequency, and data locality.
+ **Data security:** Prioritize data security by evaluating encryption options, access controls, and data protection mechanisms to safeguard sensitive information.
+ **Cost optimization:** Optimize storage costs by selecting the most cost-effective storage solutions based on data access patterns and usage.
+ **Integration with analytics services:** Ensure seamless integration between the chosen storage solution and the data processing and analytics tools in the pipeline.

------
#### [ Types of data ]

When deciding on analytics services for the collection and ingestion of data, consider various types of data that are relevant to your organization's needs and objectives. Common types of data that you might need to consider includes:
+ **Transactional data:** Includes information about individual interactions or transactions, such as customer purchases, financial transactions, online orders, and user activity logs.
+ **File-based data:** Refers to structured or unstructured data that is stored in files, such as log files, spreadsheets, documents, images, audio files, and video files. Analytics services should support the ingestion of different file formats.
+ **Event data:** Captures significant occurrences or incidents, such as user actions, system events, machine events, or business events. Events can include any data that is arriving in high velocity that is captured for onstream or downstream processing.

------
#### [ Operational considerations ]

Operational responsibility is shared between you, and AWS, with the division of responsibility varying across different levels of modernization. You have the option of self-managing your analytics infrastructure on AWS or leveraging the numerous serverless analytics services to lesson your infrastructure management burden.

Self-managed options grant users greater control over the infrastructure and configurations, but they require more operational effort.

Serverless options abstract away much of the operational burden, providing automatic scalability, high availability, and robust security features, allowing users to focus more on building analytical solutions and driving insights rather than managing infrastructure and operational tasks. Consider these benefits of serverless analytics solutions:
+ **Infrastructure abstraction:** Serverless services abstract infrastructure management, relieving users from provisioning, scaling, and maintenance tasks. AWS handles these operational aspects, reducing management overhead.
+ **Auto-scaling and performance:** Serverless services automatically scale resources based on workload demands, ensuring optimal performance without manual intervention.
+ **High availability and disaster recovery:** AWS provides high availability for serverless services. AWS manages data redundancy, replication, and disaster recovery to enhance data availability and reliability.
+ **Security and compliance:** AWS manages security measures, data encryption, and compliance for serverless services, adhering to industry standards and best practices.
+ **Monitoring and logging:** AWS offers built-in monitoring, logging, and alerting capabilities for serverless services. Users can access detailed metrics and logs through Amazon CloudWatch.

------
#### [ Type of workload ]

When building a modern analytics pipeline, deciding on the types of workload to support is crucial to meet different analytical needs effectively. Key decision points to consider for each type of workload includes:

**Batch workload**
+ **Data volume and frequency:** Batch processing is suitable for large volumes of data with periodic updates.
+  **Data latency:** Batch processing might introduce some delay in delivering insights compared to real-time processing.

**Interactive analysis**
+ **Data query complexity:** Interactive analysis requires low-latency responses for quick feedback.
+ **Data visualization:** Evaluate the need for interactive data visualization tools to enable business users to explore data visually.

**Streaming workloads**
+ **Data velocity and volume:** Streaming workloads require real-time processing to handle high-velocity data.
+ **Data windowing:** Define data windowing and time-based aggregations for streaming data to extract relevant insights.

------
#### [ Type of analysis needed ]

Clearly define the business objectives and the insights you aim to derive from the analytics. Different types of analytics serve different purposes. For example:
+ Descriptive analytics is ideal for gaining a historical overview
+ Diagnostic analytics helps understand the reasons behind past events
+ Predictive analytics forecasts future outcomes
+ Prescriptive analytics provides recommendations for optimal actions

Match your business goals with the relevant types of analytics. Here are some key decision criteria to help you choose the right types of analytics:
+ **Data availability and quality:** Descriptive and diagnostic analytics rely on historical data, while predictive and prescriptive analytics require sufficient historical data and high-quality data to build accurate models.
+ **Data volume and complexity:** Predictive and prescriptive analytics require substantial data processing and computational resources. Ensure that your infrastructure and tools can handle the data volume and complexity.
+ **Decision complexity:** If decisions involve multiple variables, constraints, and objectives, prescriptive analytics may be more suitable to guide optimal actions.
+ **Risk tolerance:** Prescriptive analytics may provide recommendations, but come with associated uncertainties. Ensure that decision-makers understand the risks associated with the analytics outputs.

------
#### [ Evaluate scalability and performance ]

Assess the scalability and performance needs of the architecture. The design must handle increasing data volumes, user demands, and analytical workloads. Key decision factors to consider includes:
+ **Data volume and growth:** Assess the current data volume and anticipate future growth. 
+ **Data velocity and real-time requirements:** Determine if the data needs to be processed and analyzed in real-time or near real-time.
+ **Data processing complexity:** Analyze the complexity of your data processing and analysis tasks. For computationally intensive tasks, services such as Amazon EMR provide a scalable and managed environment for big data processing.
+ **Concurrency and user load:** Consider the number of concurrent users and the level of user load on the system. 
+ **Auto-scaling capabilities:** Consider services that offer auto-scaling capabilities, allowing resources to automatically scale up or down based on demand. This ensures efficient resource utilization and cost optimization.
+ **Geographic distribution:** Consider services with global replication and low-latency data access if your data architecture needs to be distributed across multiple regions or locations.
+ **Cost-performance trade-off:** Balance the performance needs with cost considerations. Services with high performance may come at a higher cost.
+ **Service-level agreements (SLAs):** Check the SLAs provided by AWS services to ensure they meet your scalability and performance expectations.

------
#### [ Data governance ]

Data governance is the set of processes, policies, and controls you need to implement to ensure effective management, quality, security, and compliance of your data assets. Key decision points to consider includes:
+ **Data retention policies:** Define data retention policies based on regulatory requirements and business needs and establish processes for secure data disposal when it is no longer needed.
+ **Audit trail and logging:** Decide on the logging and auditing mechanisms to monitor data access and usage. Implement comprehensive audit trails to track data changes, access attempts, and user activities for compliance and security monitoring.
+ **Compliance requirements:** Understand the industry-specific and geographic data compliance regulations that apply to your organization. Ensure that the data architecture aligns with these regulations and guidelines.
+ **Data classification:** Classify data based on its sensitivity and define appropriate security controls for each data class. 
+ **Disaster recovery and business continuity:** Plan for disaster recovery and business continuity to ensure data availability and resilience in case of unexpected events or system failures.
+ **Third-party data sharing:** If sharing data with third-party entities, implement secure data sharing protocols and agreements to protect data confidentiality and prevent data misuse.

------
#### [ Security ]

The security of data in the analytics pipeline involves protecting data at every stage of the pipeline to ensure its confidentiality, integrity, and availability. Key decision points to consider includes:
+ **Access control and authorization:** Implement robust authentication and authorization protocols to ensure that only authorized users can access specific data resources.
+ **Data encryption:** Choose appropriate encryption methods for data stored in databases, data lakes, and during data movement between different components of the architecture.
+ **Data masking and anonymization:** Consider the need for data masking or anonymization to protect sensitive data, such as PII or sensitive business data, while allowing certain analytical processes to continue.
+ **Secure data integration:** Establish secure data integration practices to ensure that data flows securely between different components of the architecture, avoiding data leaks or unauthorized access during data movement.
+ **Network isolation:** Consider services that support [Amazon VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) to avoid exposing resources to the public internet.

------
#### [ Plan for integration and data flows ]

Define the integration points and data flows between various components of the analytics pipeline to ensure seamless data flow and interoperability. Key decision points to consider includes:
+ **Data source integration:** Identify the data sources from which data will be collected, such as databases, applications, files, or external APIs. Decide on the data ingestion methods (batch, real-time, event-based) to bring data into the pipeline efficiently and with minimal latency.
+ **Data transformation:** Determine the transformations required to prepare data for analysis. Decide on the tools and processes to clean, aggregate, normalize, or enrich the data as it moves through the pipeline.
+ **Data movement architecture:** Choose the appropriate architecture for data movement between pipeline components. Consider batch processing, stream processing, or a combination of both based on the real-time requirements and data volume.
+ **Data replication and sync:** Decide on data replication and synchronization mechanisms to keep data up-to-date across all components. Consider real-time replication solutions or periodic data syncs depending on data freshness requirements.
+ **Data quality and validation:** Implement data quality checks and validation steps to ensure the integrity of data as it moves through the pipeline. Decide on the actions to be taken when data fails validation, such as alerting or error handling.
+ **Data security and encryption:** Determine how data will be secured during transit and at rest. Decide on the encryption methods to protect sensitive data throughout the pipeline, considering the level of security required based on data sensitivity.
+ **Scalability and resilience:** Ensure that the data flow design allows for horizontal scalability and can handle increased data volumes and traffic. 

------
#### [ Architect for cost optimization ]

Building your analytics pipeline on AWS provides various cost optimization opportunities. To ensure cost efficiency, consider the following strategies:
+ **Resource sizing and selection:** Right-size your resources based on actual workload requirements. Choose AWS services and instance types that match the workloads performance needs while avoiding overprovisioning.
+ **Auto-scaling:** Implement auto-scaling for services that experience varying workloads. Auto-scaling dynamically adjusts the number of instances based on demand, reducing costs during low-traffic periods.
+ **Spot Instances:** Use Amazon EC2 Spot Instances for non-critical and fault-tolerant workloads. Spot Instances can significantly reduce costs compared to on-demand instances.
+ **Reserved instances:** Consider purchasing AWS Reserved Instances to achieve significant cost savings over on-demand pricing for stable workloads with predictable usage.
+ **Data storage tiering:** Optimize data storage costs by using different storage classes based on data access frequency.
+ **Data lifecycle policies:** Establish data lifecycle policies to automatically move or delete data based on its age and usage patterns. This helps manage storage costs and keeps data storage aligned with its value.

------

## Choose AWS analytics services
<a name="choose"></a>

Now that you know the criteria to evaluate your analytics needs, you are ready to choose which AWS analytics services are right for your organizational needs. The following table aligns sets of services with common capabilities and business goals.




- ****Unified analytics and AI****
  - **What is it optimized for?:** **Analytics and AI development**<br />Optimized for using a single development environment, Amazon SageMaker Unified Studio, to access data, analytics, and AI capabilities.
  - **Services:** [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker)

- ** **Data processing** **
  - **What is it optimized for?:** **Interactive analytics**<br />Optimized for performing real-time data analysis and exploration, which allows users to interactively query and visualize data. / **Services:** [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
  - **What is it optimized for?:** **Big data processing**<br />Optimized for processing, moving, and transforming large amounts of data. / **Services:** [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
  - **What is it optimized for?:** **Data catalog**<br />Optimized for providing detailed information about the available data, its structure, characteristics, and relationships. / **Services:** [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
  - **What is it optimized for?:** **Workflow orchestration**<br />Optimized for creating, scheduling, and monitoring data workflows using Apache Airflow to coordinate analytics processes and ETL jobs. / **Services:** [Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)

- ****Data streaming****
  - **What is it optimized for?:** **Apache Kafka processing of streaming data**<br />Optimized for using Apache Kafka data-plane operations and running open source versions of Apache Kafka.  / **Services:** [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
  - **What is it optimized for?:** **Real-time processing**<br />Optimized for rapid and continuous data intake and aggregation, including IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data. / **Services:** [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
  - **What is it optimized for?:** **Real-time streaming data delivery**<br />Optimized for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, OpenSearch Service, Splunk, Apache Iceberg Tables, and any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers. / **Services:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
  - **What is it optimized for?:** **Building Apache Flink applications**<br />Optimized for using Java, Scala, Python, or SQL to process and analyze streaming data. / **Services:** [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)

- ****Business intelligence****
  - **What is it optimized for?:** **Dashboards and visualizations**<br />Optimized for visually representing complex datasets, and providing natural language query of your data. 
  - **Services:** [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

- ****Search analytics****
  - **What is it optimized for?:** **Managed OpenSearch clusters**<br />Optimized for log analytics, real-time application monitoring, and clickstream analysis.
  - **Services:** [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)

- ****Data governance****
  - **What is it optimized for?:** **Managing data access**<br />Optimized for setting up the proper management, availability, usability, integrity, and security of data throughout its lifecycle.
  - **Services:** [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html)

- ****Data collaboration****
  - **What is it optimized for?:** **Secure data clean rooms**<br />Optimized for collaborating with other companies without sharing raw underlying data.
  - **Services:** [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html)

- ****Data lake and warehouse****
  - **What is it optimized for?:** **Unified access to data lakes and data warehouses**<br />Built on a lakehouse architecture to optimize for unifying data access across Amazon S3 data lakes, Amazon Redshift data warehouses, operational databases, and third-party and federated data sources. / **Services:** [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker)
  - **What is it optimized for?:** **Object storage for data lakes**<br />Optimized for providing a data lake foundation with virtually unlimited scalability and high durability.  / **Services:** [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
  - **What is it optimized for?:** **Data warehousing**<br />Optimized for centrally storing, organizing, and retrieving large volumes of structured and sometimes semi-structured data from various sources within an organization. / **Services:** [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)



## Use AWS analytics services
<a name="use"></a>

You should now have a clear understanding of your business objectives, and the volume and velocity of data you will be ingesting and analyzing to begin building your data pipelines.

To explore how to use and learn more about each of the available services—we have provided a pathway to explore how each of the services work. The following sections provides links to in-depth documentation, hands-on tutorials, and resources to get you started from basic usage to more advanced deep dives.

------
#### [ Amazon Athena ]
+ **Getting started with Amazon Athena**

  Learn how to use Amazon Athena to query data and create a table based on sample data stored in Amazon S3, query the table, and check the results of the query.

  [Get started with the tutorial](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)
+ **Get started with Apache Spark on Athena**

  Use the simplified notebook experience in Athena console to develop Apache Spark applications using Python or Athena notebook APIs.

  [Get started with the tutorial](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html)
+ **Catalog and govern Athena federated queries with Amazon SageMaker lakehouse architecture**

  Learn how to connect to, govern, and run federated queries on data stored in Amazon Redshift, DynamoDB, and Snowflake via the data lakehouse in Amazon SageMaker.

  [Read the blog](https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/)
+ **Analyzing data in Amazon S3 using Athena**

  Explore how to use Athena on logs from Elastic Load Balancers, generated as text files in a pre-defined format. We show you how to create a table, partition the data in a format used by Athena, convert it to Parquet, and compare query performance.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/analyzing-data-in-s3-using-amazon-athena/)

------
#### [ AWS Clean Rooms ]
+  **Setting up AWS Clean Rooms** 

  Learn how to set up AWS Clean Rooms in your AWS acccount.

   [Read the guide](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html) 
+  **Unlock data insights across multi-party datasets using AWS Entity Resolution on AWS Clean Rooms without sharing underlying data** 

  Learn how to use preparation and matching to help improve data matching with collaborators.

   [Read the blog post](https://aws.amazon.com/blogs/industries/unlock-data-insights-across-multi-party-datasets-using-aws-entity-resolution-on-aws-clean-rooms-without-sharing-underlying-data/) 
+  **How differential privacy helps unlock insights without revealing data at the individual-level** 

  Learn how AWS Clean Rooms Differential Privacy simplifies applying differential privacy and helps protect the privacy of your users.

   [Read the blog](https://aws.amazon.com/blogs/industries/how-differential-privacy-helps-unlock-insights-without-revealing-data-at-the-individual-level/) 

------
#### [ Amazon Data Firehose ]
+  **Tutorial: Create a Firehose stream from console** 

  Learn how to use the AWS Management Console or an AWS SDK to create a Firehose stream to your chosen destination.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) 
+  **Send data to a Firehose stream** 

  Learn how to use different data sources to send data to your Firehose stream.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html) 
+  **Transform source data in Firehose** 

  Learn how to invoke your Lambda function to transform incoming source data and deliver the transformed data to destinations.

   [Read the guide](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html) 

------
#### [ Amazon DataZone ]
+ **Getting started with Amazon DataZone **

  Learn how to create the Amazon DataZone root domain, obtain the data portal URL, walk through the basic Amazon DataZone workflows for data producers and data consumers.

  [Get started with the tutorial](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html)
+ **Announcing the general availability of data lineage in the next generation of Amazon SageMaker and Amazon DataZone **

  Learn how Amazon DataZone uses automated lineage capture to focus on automatically collecting and mapping lineage information from AWS Glue and Amazon Redshift.

  [Read the blog](https://aws.amazon.com/blogs/aws/announcing-the-general-availability-of-data-lineage-in-the-next-generation-of-amazon-sagemaker-and-amazon-datazone/)

------
#### [ Amazon EMR ]
+ **Getting started with Amazon EMR**

  Learn how to launch a sample cluster using Spark, and how to run a simple PySpark script stored in an Amazon S3 bucket.

  [Get started with the tutorial](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
+ **Getting started with Amazon EMR on Amazon EKS**

  We show you how to get started using Amazon EMR on Amazon EKS by deploying a Spark application on a virtual cluster.

  [Explore the guide](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.html)
+ **Get started with EMR Serverless**

  Explore how Amazon EMR Serverless provides a serverless runtime environment that simplifies the operation of analytics applications that use the latest open source frameworks.

  [Get started with the tutorial](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)

------
#### [ AWS Glue ]
+ **Getting started with AWS Glue DataBrew**

  Learn how to create your first DataBrew project. You load a sample dataset, run transformations on that dataset, build a recipe to capture those transformations, and run a job to write the transformed data to Amazon S3.

  [Get started with the tutorial](https://docs.aws.amazon.com/databrew/latest/dg/getting-started.html)
+ **Transform data with AWS Glue DataBrew**

  Learn about AWS Glue DataBrew, a visual data preparation tool that makes it easy for data analysts and data scientists to clean and normalize data to prepare it for analytics and machine learning. Learn how to construct an ETL process using AWS Glue DataBrew.

  [Get started with the lab](https://catalog.workshops.aws/introduction-to-analytics-on-aws/en-US/lab-guide/transform-glue-databrew)
+ **AWS Glue DataBrew immersion day**

  Explore how to use AWS Glue DataBrew to clean and normalize data for analytics and machine learning. 

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6532bf37-3ad2-4844-bd26-d775a31ce1fa/en-US)
+ **Getting started with the AWS Glue Data Catalog**

  Learn how to create your first AWS Glue Data Catalog, which uses an Amazon S3 bucket as your data source.

  [Get started with the tutorial](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html)
+ **Data catalog and crawlers in AWS Glue**

  Discover how you can use the information in the Data Catalog to create and monitor your ETL jobs.

  [Explore the guide](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

------
#### [ Amazon Kinesis Data Streams ]
+ **Getting started tutorials for Amazon Kinesis Data Streams**

  Learn how to process and analyze real-time stock data.

  [Get started with the tutorials](https://docs.aws.amazon.com/streams/latest/dev/examples.html)
+ **Architectural patterns for real-time analytics using Amazon Kinesis Data Streams, part 1**

  Learn about common architectural patterns of two use cases: time series data analysis and event driven microservices.

  [Read the blog](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-1/)
+ **Architectural Patterns for real-time analytics using Amazon Kinesis Data Streams, part 2**

  Learn about AI applications with Kinesis Data Streams in three scenarios: real-time generative business intelligence, real-time recommendation systems, and Internet of Things data streaming and inferencing.

  [Read the blog](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-2-ai-applications/)

------
#### [ Amazon Managed Service for Apache Flink ]
+ **What is Amazon Managed Service for Apache Flink?**

  Understand the fundamental concepts of Amazon Managed Service for Apache Flink.

  [Explore the guide](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
+ **Amazon Managed Service for Apache Flink Workshop**

  In this workshop, you will learn how to deploy, operate, and scale a Flink application with Amazon Managed Service for Apache Flink.

  [Attend the virtual workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2437ee74-38ed-4817-94b9-45b920cb168a/en-US)

------
#### [ Amazon MSK ]
+ **Getting Started with Amazon MSK**

  Learn how to create an Amazon MSK cluster, produce and consume data, and monitor the health of your cluster using metrics.

  [Get started with the guide](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
+ **Amazon MSK Workshop**

  Go deep with this hands-on Amazon MSK workshop. 

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c2b72b6f-666b-4596-b8bc-bafa5dcca741/en-US)

------
#### [ Amazon MWAA ]
+ **Getting started with Amazon MWAA**

  Learn how to create your first MWAA environment, upload a DAG to Amazon S3, and run your first workflow.

  [Get started with the tutorial](https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html)
+ **Building data pipelines with Amazon MWAA**

  Learn how to build end-to-end data pipelines that orchestrate other AWS analytics services like Glue, EMR, and Redshift. This blog post explores a streamlined, configuration-driven approach to orchestrating dbt Core jobs using MWAA and Cosmos, with jobs running transformations on Amazon Redshift.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/build-data-pipelines-with-dbt-in-amazon-redshift-using-amazon-mwaa-and-cosmos/)
+ **Amazon MWAA workshop**

  Explore hands-on exercises to learn how to deploy, configure, and use Amazon MWAA for data workflow orchestration.

  [Get started with the workshop](https://catalog.workshops.aws/amazon-mwaa-for-analytics/en-US)
+ **Best practices for Amazon MWAA**

  Learn architectural patterns and best practices for using Amazon MWAA in your analytics workflows.

  [Read the guide](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices.html)

------
#### [ OpenSearch Service ]
+ **Getting started with OpenSearch Service **

  Learn how to use Amazon OpenSearch Service to create and configure a test domain.

  [Get started with the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html)
+ **Visualizing customer support calls with OpenSearch Service and OpenSearch Dashboards**

  Discover a full walkthrough of the following situation: a business receives some number of customer support calls and wants to analyze them. What is the subject of each call? How many were positive? How many were negative? How can managers search or review the the transcripts of these calls?

  [Get started with the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/walkthrough.html)
+ **Getting started with Amazon OpenSearch Serverless workshop**

  Learn how to set up a new Amazon OpenSearch Serverless domain in the AWS console. Explore the different types of search queries available, and design eye-catching visualizations, and learn how you can secure your domain and documents based on assigned user privileges.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/f8d2c175-634d-4c5d-94cb-d83bbc656c6a/en-US)
+ **Cost Optimized Vector Database: Introduction to Amazon OpenSearch Service quantization techniques**

  Learn how OpenSearch Service supports scalar and product quantization techniques to optimize memory usage and reduce operational costs.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/cost-optimized-vector-database-introduction-to-amazon-opensearch-service-quantization-techniques/)

------
#### [ Quick ]
+ **Getting started with Quick data analysis**

  Learn how to create your first analysis. Use sample data to create either a simple or a more advanced analysis. Or you can connect to your own data to create an analysis.

  [Explore the guide](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html)
+ **Visualizing with Quick**

  Discover the technical side of business intelligence (BI) and data visualization with AWS. Learn how to embed dashboards into applications and websites, and securely manage access and permissions.

  [Get started with the course](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/41/visualizing-with-quicksight)
+ **Quick workshops**

  Get a head start on your Quick journey with workshops

  [Get started with the workshops](https://catalog.workshops.aws/quicksight/en-US)

------
#### [ Amazon Redshift ]
+ **Getting started with Amazon Redshift Serverless**

  Understand the basic flow of Amazon Redshift Serverless to create serverless resources, connect to Amazon Redshift Serverless, load sample data, and then run queries on the data.

  [Explore the guide](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html)
+ **Amazon Redshift deep dive workshop**

  Explore a series of exercises which help users get started using the Amazon Redshift platform.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/380e0b8a-5d4c-46e3-95a8-82d68cf5789a/en-US)

------
#### [ Amazon S3 ]
+ **Getting started with Amazon S3**

  Learn how to create your first DataBrew project. You load a sample dataset, run transformations on that dataset, build a recipe to capture those transformations, and run a job to write the transformed data to Amazon S3.

  [Get started with the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)

------
#### [ Amazon SageMaker ]
+  **Getting started with SageMaker** 

  Learn how to create a project, add members, and use the sample JupyterLab notebook to begin building.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html) 
+  **Introducing the next generation of Amazon SageMaker: The center for all your data, analytics, and AI** 

  Learn how to get started with data processing, model development, and generative AI app development.

   [Read the blog](https://aws.amazon.com/blogs/aws/introducing-the-next-generation-of-amazon-sagemaker-the-center-for-all-your-data-analytics-and-ai/) 
+  **What is SageMaker Unified Studio?** 

  Learn about the capabilities of SageMaker Unified Studio and how to access them when you use Amazon SageMaker.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/what-is-sagemaker-unified-studio.html) 
+  **Getting started with the lakehouse architecture of Amazon SageMaker** 

  Learn how to create a project and to browse, upload, and query data for your business use cases in Amazon SageMaker.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-get-started.html) 
+  **Data connections in the lakehouse architecture of Amazon SageMaker** 

  Learn how the lakehouse architecture provides a unified approach to managing data connections across AWS services and enterprise applications.

   [Read the guide](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.html) 
+  **Catalog and govern Athena federated queries with the SageMaker lakehouse architecture**

  Learn how to connect to, govern, and run federated queries on data stored in Amazon Redshift, DynamoDB, and Snowflake for your Amazon SageMaker projects.

   [Read the blog](https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/) 

------

## Explore ways to use AWS analytics services
<a name="explore"></a>

------
#### [ Editable architecture diagrams ]

**Reference architecture diagrams** 

Explore architecture diagrams to help you develop, scale, and test your analytics solutions on AWS.

[ Explore analytics reference architectures](https://aws.amazon.com/architecture/reference-architecture-diagrams/?achp_navlib4&ams%23interactive-card-vertical%23pattern-data--366709333.filter=%257B%2522search%2522%253A%2522analytics%2522%257D)

------
#### [ Ready-to-use code ]



|  |  | 
| --- |--- |
| *Featured solution*<br />**Scalable Analytics Using Apache Druid on AWS**<br />Deploy AWS-built code to help you set up, operate, and manage Apache Druid on AWS, a cost-effective, highly available, resilient, and fault tolerant hosting environment.<br />[Explore this solution](https://aws.amazon.com/solutions/implementations/scalable-analytics-using-apache-druid-on-aws/) | **AWS Solutions**<br />Explore pre-configured, deployable solutions and their implementation guides, built by AWS.<br />[Explore all AWS security, identity, and governance solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23analytics&awsf.industries=*all&awsf.business-category=*all) | 

------
#### [ Documentation ]



|  |  | 
| --- |--- |
| **Analytics whitepapers** <br />Explore whitepapers for further insights and best practices on choosing, implementing, and using the analytics services that best fit your organization. <br />[Explore analytics whitepapers ](https://aws.amazon.com/whitepapers/?ams%23interactive-card-vertical%23pattern-data-1858756679.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523aws-tech-category.and%2522%252C%2522value%2522%253A%255B%2522analytics%2522%255D%257D%255D%257D) | **AWS Big Data Blog** <br />Explore blog posts that address specific big data use cases. <br /> [Explore the AWS Big Data blog](https://aws.amazon.com/blogs/big-data/)  | 

------

# Compute
<a name="compute"></a>

The following decision guides help you choose AWS services for running compute workloads, including virtual machines, containers, serverless functions, and modern applications.

**Topics**
+ [Choosing an AWS compute service](#choosing-aws-compute-service)
+ [Choosing an AWS container service](#choosing-aws-container-service)
+ [AWS Fargate or AWS Lambda?](#fargate-or-lambda)
+ [Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2?](#lightsail-elastic-beanstalk-ec2)
+ [Choosing a modern application strategy](#modern-apps-strategy-on-aws-how-to-choose)
+ [Choosing a purchasing option for Amazon EC2](#ec2-purchasing-options-aws-how-to-choose)

## Choosing an AWS compute service
<a name="choosing-aws-compute-service"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS compute service is the best fit for your organization. | 
| **Last updated** | February 17, 2025 | 
| **Covered services** |  +  [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) <br />+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) <br />+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) <br />+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br />+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br />+  [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br />+  [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) <br />+  [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) <br />+  [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) <br />+  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) <br />+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/) <br />+  [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) <br />+  [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html) <br />+  [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br />+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br />+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) <br />+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) <br />+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)   | 

### Introduction
<a name="intro"></a>

AWS compute services are designed to meet the varied demands of modern applications, from small-scale projects to enterprise-grade solutions. These services provide scalable computing power that helps you to build, deploy, and manage applications. 

To get the most from your investment in these services, it's important to choose the right services for the right task or use case, whether it involves processing simple web app requests or running complex, data-intensive algorithms.

 You can, for example, use:
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) to launch and manage virtual servers
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/) to quickly deploy and manage web applications with minimal management of the infrastructure that runs those applications
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs) to run code without having to provision or manage servers
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) to run and manage [containers](https://aws.amazon.com/what-are-containers)
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) to run containers on AWS managed compute, or [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) to process large volumes of data in parallel

 You can also use multiple types of compute solutions in a single workload, as each one has its own advantages. 

 This guide will help you select the AWS compute services and tools that are the best fit for your needs and your organization. 

[![AWS Videos](https://img.youtube.com/vi/E0dYLPXrX_w?si=UdTT-QeG3-TCNAOx&start=1577&end=1704/0.jpg)](https://www.youtube.com/watch?v=E0dYLPXrX_w?si=UdTT-QeG3-TCNAOx&start=1577&end=1704)


### Understand
<a name="understand"></a>

 AWS compute services provide secure and resizable compute capacity in the cloud. AWS offers a range of compute services to meet various application requirements. These include Amazon EC2 for resizable virtual servers, Elastic Beanstalk for deploying web applications on your choice of a number of popular platforms, AWS Lambda for serverless computing, Amazon ECS and EKS for container orchestration, and AWS Fargate for serverless containers. 

 Furthermore, AWS Batch facilitates batch computing. AWS hybrid and edge services such as [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) and [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) bring AWS infrastructure and services to metropolitan areas, on-premises locations, and edge sites, addressing requirements for low latency, digital sovereignty, and local data processing. Additionally, Amazon EC2 Auto Scaling automatically adjusts capacity. These services cater to different workload needs, from basic virtual machines (VMs) to fully managed serverless and container solutions. 

![](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/understand.png)


 **Amazon EC2 services** 

 Amazon EC2 offers a wide range of instance types tailored to different workloads and applications. You can choose from a range of configurations, including different combinations of CPU, memory, storage, and networking capacity. EC2 provides a large variety of compute capacity options optimized for various workloads: general purpose, compute optimized, memory optimized, storage optimize, accelerated computing, and high-performance computing. 
+  [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html): Amazon EC2 provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud, including AWS Graviton4 instances for improved price-performance and lower latency in compute-intensive applications, Trn2 instances for high-performance AI/ML training and inference, and P5eN instances optimized for deep learning (DL), high-performance computing (HPC) workloads, and generative AI applications. 
+  [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html): Amazon EC2 Auto Scaling helps you maintain application availability and lets you automatically add or remove Amazon EC2 instances by using scaling policies that you define. 
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html): EC2 Image Builder is a fully managed AWS service that helps you to automate the creation, management, and deployment of customized, secure, and up-to-date server images. 
+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html): AWS Elastic Beanstalk supports applications developed in Python, Node.js, Java, .NET, PHP, Ruby, and GO. Elastic Beanstalk also supports Docker platforms. With Docker containers you can choose your own programming language and application dependencies that may not be supported by the other Elastic Beanstalk platforms. 
+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html): Amazon Lightsail provides an easy way to build web applications providing instances, container services, managed databases, content delivery network distributions, load balancers, SSD-based storage, and DNS management. 

 **Container services** 

 AWS container compute options are designed to help you deploy, manage, and scale containerized applications efficiently. Amazon ECS, for example, allows you to run and manage Docker containers at scale, handling cluster management and orchestration of containers. Amazon EKS provides a fully managed Kubernetes service, simplifying the deployment, management, and scaling of containerized applications using Kubernetes. 

 You have the option of running containers on EC2 instances that you manage, or you can run them on Fargate on AWS managed compute. Additionally, AWS offers Amazon Elastic Container Registry (Amazon ECR), a fully managed Docker container registry. 
+  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html): Amazon ECS is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications. 
+  [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html): Amazon ECS Anywhere provides support for registering an *external instance* such as an on-premises server or VM, to your Amazon ECS cluster. 
+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html): Amazon EKS is a managed service that helps you easily deploy, manage, and scale containerized applications using Kubernetes on AWS infrastructure. Amazon EKS removes the need to install, operate, and maintain your own Kubernetes control plane on AWS. 
+  [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/): Amazon EKS Anywhere is a container management software built by AWS that makes it easier to run and manage Kubernetes clusters on-premises and at the edge. 
+  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html): Amazon ECR is an AWS managed container image registry service that is secure, scalable, and reliable. 
+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html): AWS Batch is a fully managed batch computing service that plans, schedules, and runs your containerized batch machine learning, simulation, and analytics workloads across the full range of AWS compute offerings, such as Amazon ECS, Amazon EKS, Fargate, and Spot or On-Demand Instances. 

 **Serverless compute** 

 AWS offers serverless compute options, including AWS Lambda and AWS Fargate, which allow you to run your workloads without provisioning or managing servers. As a result, developers can focus on writing code by shifting as much management of the underlying infrastructure resources to AWS. 
+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html): AWS Fargate is a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. 
+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html): Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. 

 **On-premises and edge compute** 

 AWS provides hybrid and edge compute options that allow you to extend AWS infrastructure and services to your premises and the edge. These edge and hybrid compute options provide flexibility and scalability for a wide range of use cases across different network environments. 
+  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html): AWS Local Zones places compute, storage, database, and other select AWS resources close to large population and industry centers. You can use Local Zones to provide your users with low-latency access to your applications. 
+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/): AWS Dedicated Local Zones are a type of AWS Infrastructure that is fully managed by AWS, built for exclusive use by a customer or community, and placed in a customer-specified location or data center to comply with regulatory requirements. 
+  [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html): AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. 
+  [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html): AWS Wavelength helps developers to build applications that deliver ultra-low latencies to mobile devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of communications service providers' (CSPs') 5G networks. 

 **Cost optimization** 

 AWS provides cost optimization services that allow you to reduce your AWS costs by committing to a usage level and generating recommendations to reduce the cost of your workloads. 
+  [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html): Savings Plans is a flexible pricing model that can help you reduce your bill compared to On-Demand prices, in exchange for a one- or three-year hourly spend commitment. 
+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html): AWS Compute Optimizer provides artificial intelligence and machine learning-based analytics to help you right size your workloads, reduce costs, and improve the performance of your workloads. 
+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html): Amazon EC2 Spot Instances let you take advantage of unused EC2 capacity at a significant discount to On-Demand pricing, allowing you to lower your Amazon EC2 costs significantly.

 **Elastic Load Balancing** 

 [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. 
+  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html): An Application Load Balancer functions at the application layer, the seventh layer of the OSI model. After the load balancer receives a request, it evaluates the listener rules in priority order to determine which rule to apply, and then selects a target from the target group for the rule action. 
+  [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html): A Network Load Balancer functions at the fourth layer of the Open Systems Interconnection (OSI) model. It can handle millions of requests per second. After the load balancer receives a connection request, it selects a target from the target group for the default rule. 
+  [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html): Gateway Load Balancers help you to deploy, scale, and manage virtual appliances, such as firewalls, intrusion detection and prevention systems, and deep packet inspection systems. 

### Consider
<a name="consider"></a>

 Here are some key factors to consider when choosing an AWS compute service. Choosing the right AWS compute service involves balancing these factors to match your specific workload needs, technical requirements, and business objectives, to help you optimize for performance, cost, and ease of management. 

------
#### [ Workload type and requirements ]

 Workload planning involves understanding the operational patterns and technical demands of your applications. For instance, **batch processing jobs**, which often involve running a series of tasks or a program on a large volume of data, require robust compute capacity, which can be scaled down upon job completion to manage costs effectively. 

 **Web applications**, on the other hand, demand high availability and consistent performance to serve end-user requests at any scale. These workloads typically need a compute service that can dynamically adjust to fluctuating traffic patterns, ensuring smooth user experiences during demand surges and cost savings during quieter periods. Elastic Beanstalk is specifically designed for running web applications. It provides the runtime on EC2 instances so you just need to deploy your application code. 

 **Machine learning models** introduce a different set of requirements, with distinct phases for training and inference. Training is computationally intensive and often requires specialized hardware accelerators such as GPUs or custom chips for a limited duration but at a high-performance level. Inference, however, might call for a highly available environment that can quickly respond to prediction requests, often benefitting from optimized compute services that support auto-scaling and low-latency processing. 

 Choosing the right compute service entails matching these workload characteristics with the specific capabilities of each service to achieve operational efficiency, performance optimization, and cost management. 

------
#### [ Performance needs ]

 Performance encompasses the compute power—CPU and GPU capabilities—for processing, the memory for data caching and operations, storage I/O for data throughput, and network bandwidth for data transfer. 

 **High-performance applications**, such as those involving complex calculations or data-intensive processing, might require robust and fast CPUs or GPUs, found in compute-optimized or GPU-based EC2 instances. In contrast, **memory-intensive applications**, like those running large databases or in-memory caches, necessitate memory-optimized instances with a higher memory-to-CPU ratio. 

 Furthermore, applications with **heavy input/output operations**, such as high-traffic web applications or big data processing systems, need storage-optimized instances with high I/O throughput. Lastly, network performance is crucial for **distributed systems and applications** that require rapid data transfer across instances or services. 

 Optimizing for performance means choosing services that not only meet your current demands but can also scale with your application's growth, ensuring consistent, high-quality user experiences without overspending on resources. 

------
#### [ Scalability ]

 Scalability is a critical criterion in the selection of AWS compute services, as it defines the ability of the system to handle growth and manage increased demand. Effective scalability ensures that your application can accommodate more users, handle more transactions, and process larger datasets without degrading performance. 

 The scalability of a service can be **vertical**, allowing you to scale up by adding more power to your existing infrastructure (like increasing the CPU or memory of an instance), or **horizontal**, helping you to scale out by adding more instances to handle the load. Horizontal scalability is essential for dynamic workloads with fluctuating demands. 

 Choosing a service that can automatically adjust its scale, like AWS's Auto Scaling or serverless offerings, can provide the flexibility to seamlessly manage workload spikes and lulls. This not only maintains performance levels but also optimizes costs, as you only pay for the resources you use. Scalability considerations help you make sure that your infrastructure is resilient, cost-effective, and capable of supporting your application as it evolves. 

------
#### [ Management overhead ]

 Management overhead refers to the amount of effort and resources required to manage and maintain your computing infrastructure. In AWS, this can range from hands-on management of virtual servers to AWS managed services. 

 For instance, **managing** EC2 instances involves responsibility for setup, scaling, patching, and securing servers. This can be resource-intensive, requiring a dedicated operations team. However, for use cases where granular control over the compute environment is necessary, the overhead is often justified. 

 On the other hand, AWS offers services that **abstract** away much of the infrastructure management. Serverless computing options like AWS Lambda run code in response to events without the need to manage servers, reducing the operational burden. Managed container services help to optimize deployment and scaling of containers, providing a middle ground between control and convenience. Elastic Beanstalk provides managed updates for OS patches, runtime and framework on EC2 instances it manages so customers can just run their application code. 

 Balancing management overhead involves assessing your organization's operational capacity and expertise, the need for control versus convenience, and the overall cost of ownership, including the hidden costs of operational labor. Selecting a service that aligns with your management capabilities ensures operational efficiency and allows you to focus on innovation and building applications. 

------
#### [ Cost optimization ]

 Cost optimization is a key consideration when using AWS compute services, as it helps you make sure that you're obtaining the most economical solution for your specific needs without sacrificing performance and scalability. Consider the following to save money on compute on AWS. 

1. **Selecting the right instance**

   AWS has more than 750 instance types, with most of these instances built on the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/). Each instance type provides a choice of processor, storage, networking, operating system, and size, so you can choose the instance configuration that best fits your specific workload and budget.

    [AWS Graviton-based Instances](https://aws.amazon.com/ec2/instance-explorer/?ec2-instances-cards.sort-by=item.additionalFields.category-order&ec2-instances-cards.sort-order=desc&awsf.ec2-instances-filter-category=*all&awsf.ec2-instances-filter-processors=*all&awsf.ec2-instances-filter-accelerators=*all&awsf.ec2-instances-filter-additional-capabilities=*all&awsf.ec2-instances-filter-workload-tags=*all) are designed to deliver the best price performance for your cloud workloads running in Amazon EC2. EC2 instances powered by AWS Graviton processors deliver up to 40% better price performance than comparable non-Graviton-based instances. 

    [Accelerated computing instances](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing) such as AWS Trainium-based EC2 Trn1 instances and AWS Inferentia-based Inf2 instances are designed to deliver high performance at the lowest cost in EC2 for your machine learning training and deployment needs. 

1. **Choosing the right purchase plans**

   You have several purchase models to choose from to maximize saving.

   [On-Demand Instances](https://aws.amazon.com/ec2/pricing/on-demand/) let you pay for compute capacity by the hour or second with no long-term commitments. This frees you from the costs and complexities of planning, purchasing, and maintaining hardware. 

   [Savings Plans](https://aws.amazon.com/savingsplans/) is a flexible pricing model that can help you reduce your bill by up to 72% compared to On-Demand prices, in exchange for a one- or three-year hourly spend commitment. 

   [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) let you take advantage of unused EC2 capacity in the AWS Cloud and are available at a discount of up to 90% compared to On-Demand prices.

1. **Right size your workloads**

   With AWS, you scale up or down as demand fluctuates. The following tools help you to right size your workload.

   **Amazon EC2 Auto Scaling** helps you maintain application availability and helps you to automatically add or remove EC2 instances by using scaling policies that you define.

   **Compute Optimizer** provides artificial intelligence and machine learning-based analytics to help you right size your workloads and reduce costs by up to 25%. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) can help you identify unused resources and opportunities to lower your costs. 

------
#### [ Latency and throughput ]

 Latency and throughput are crucial performance metrics that influence the responsiveness and data handling capacity of your applications. **Low latency** is essential for time-sensitive applications, ensuring that user interactions or transactions are processed rapidly. **High throughput** is necessary for applications that need to process large volumes of data quickly, such as video streaming services or big data analysis platforms. 

 When selecting AWS compute services, consider the **geographical distribution** of your user base and the location of AWS data centers. Proximity to users can drastically reduce latency. Additionally, services that offer edge computing capabilities can further minimize latency by processing data closer to the source. 

 For throughput, you'll need to evaluate **network bandwidth** and the **I/O capacity** of the compute service, ensuring that the service can handle peak data loads efficiently. The right selection can prevent bottlenecks, ensuring data is processed, analyzed, and transferred without delays, thus maintaining optimal application performance. 

------
#### [ Compliance and security ]

 Compliance and security are critical factors when choosing AWS compute services, as they ensure that the infrastructure adheres to regulatory standards and protects data integrity. Compliance with industry-specific frameworks, such as [Health Insurance Portability and Accountability Act (HIPAA)](https://aws.amazon.com/compliance/hipaa-compliance/) for healthcare, [General Data Protection Regulation (GDPR)](https://aws.amazon.com/compliance/gdpr-center/) for data protection in the EU, or [AWS System and Organization Controls (SOC)](https://aws.amazon.com/compliance/soc-faqs/) for service organizations, is non-negotiable for many businesses. AWS provides a suite of services designed to meet these rigorous standards, offering features like data encryption, identity and access management, and logging and monitoring. 

 Security encompasses not just compliance but also the broader protection of your infrastructure from unauthorized access and cyber threats. The chosen service should offer robust security features, including network security groups, firewalls, and options for private connectivity. Additionally, AWS regularly attains third-party validations for its security and compliance controls, providing an assurance that its infrastructure can support the necessary compliance and protect sensitive data, thereby maintaining trust and integrity. Choosing a compute service that aligns with these requirements is essential for risk management and maintaining customer trust. 

 AWS Nitro System provides enhanced security that continuously monitors, protects, and verifies the instance hardware and firmware. Virtualization resources are offloaded to dedicated hardware and software minimizing the attack surface. Nitro System's security model is locked down and prohibits administrative access, eliminating the possibility of human error and tampering. AWS Local Zones, AWS Dedicated Local Zones, AWS Outposts, and AWS Wavelength are all built on the same Nitro System that powers modern EC2 instances in the AWS Regions today. 

------
#### [ Integration ]

 Integration within AWS pertain to how compute services work in concert with other AWS offerings and third-party applications. It's crucial to select a compute service that seamlessly connects with databases, analytics, machine learning, or other services that form the backbone of your cloud architecture. This approach should allow for a cohesive workflow, where data and processes can move smoothly across services, facilitating automation and reducing the need for manual intervention. 

 The chosen compute service should offer APIs, SDKs, and integration points that align with your existing tools and practices, enabling straightforward implementation into your development pipeline. AWS breadth of services and its extensive [partner network](https://aws.amazon.com/partners/) can enhance application capabilities and accelerate innovation. Additionally, the availability of pre-built integrations can save development time and resources. Therefore, evaluating the compatibility of the compute service with the broader use is essential for building a scalable, agile, and efficient cloud environment. 

------
#### [ Reliability and availability ]

 Reliability and availability are paramount when selecting AWS compute services, as they determine the resilience and uptime of your applications. Reliability ensures that the service can consistently perform its intended function correctly under specific conditions, while availability measures the proportion of time the service is operational and accessible. 

 In assessing these criteria, consider the service's track record for stability and its ability to recover from failures. Look for features such as redundancy, failover processes, and backup capabilities that ensure continuous operation. AWS services often come with Service Level Agreements (SLAs) that guarantee a certain percentage of uptime. 

 Moreover, the ability to deploy across multiple Availability Zones can mitigate the impact of outages, while the global spread of AWS Regions can help ensure that your application remains available to users worldwide even during regional disruptions. The choice of a compute service with high reliability and availability minimizes potential downtime, maintaining business continuity and safeguarding user experience. 

------
#### [ Development and deployment experience ]

 The development and deployment experience are important when choosing AWS compute services, as it directly impacts the efficiency and agility of your development team. Services that offer streamlined workflows, comprehensive documentation, and robust tooling can significantly reduce the time to market for new features and applications. 

 Consider whether the service integrates well with your existing CI/CD pipelines, supports your preferred development languages and frameworks, and provides easy-to-use SDKs and APIs for seamless application integration. Services that offer containerization and serverless computing can simplify deployment and management, allowing developers to focus more on writing code and less on infrastructure concerns. 

 Moreover, the availability of detailed monitoring, logging, and debugging tools within the AWS Cloud can enhance the development experience, enabling quick identification and resolution of issues. Choosing a compute service that aligns with your team's skills and workflows can foster a more productive and innovative development environment, ultimately driving business success. 

------

### Choose
<a name="choose"></a>

Now that you know the criteria by which you're evaluating your compute options, you're ready to choose which AWS compute services might be a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances.


|  Compute category  |  What is it optimized for?  |  Compute services  | 
| --- | --- | --- | 
|  Amazon EC2  |  Providing scalable high-performance computing resources for CPU-intensive workloads.  |  [Amazon EC2](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) <br /> [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) <br /> [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) <br /> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br /> [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)  | 
|  Container services  |  Helping your teams focus on building applications rather than the runtime environment or managing a control plane.  |  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br /> [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br /> [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) <br /> [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br /> [Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/) <br /> [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br /> [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)  | 
|  Serverless compute  |  Minimizing your AWS management overhead, allowing you to focus on implementing your business logic.  |  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) <br /> [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)  | 
|  On-premises and edge compute  |  Allowing you to run familiar AWS interfaces to your premises and the edge, providing lower latency and local data processing needs.  |  [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) <br /> [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/faqs/) <br /> [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) <br /> [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/what-is-wavelength.html)  | 
|  Cost and savings optimization  |  Helping you reduce your AWS costs for your workloads.  |  [AWS Savings Plan](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br /> [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br /> [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)  | 
|  Elastic Load Balancing  |  Increasing the availability and fault tolerance of your applications.  |  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) <br /> [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) <br /> [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)  | 

### Use
<a name="use"></a>

You should now have a clear understanding of each AWS compute service (and the supporting AWS tools and services) and which one might be the best fit for your organization and use case. 

 To explore how to use and learn more about each of the available AWS compute services, we have provided a pathway to learn how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started. 

#### Amazon EC2
<a name="amazon-ec2-section"></a>

------
#### [ Amazon EC2 ]
+  **Tutorial: Get started with Amazon EC2 Linux instances** 

   Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Linux instance. 

   [Use the tutorial ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) 
+  **Tutorial: Get started with Amazon EC2 Windows instances** 

   Use this tutorial to get started with Amazon EC2. You'll learn how to launch, connect to, and use a Windows instance. 

   [Use the tutorial](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html) 
+  **Amazon EC2 instance types** 

   This guide will give you an overview of the various families of EC2 instance types and discuss the appropriate application for each family. 

   [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) 
+  **Get Started with Amazon EC2 Graviton instances** 

   This guide will help you get started with Amazon EC2 Graviton instances and provides steps-by-step instructions to migrate your workload to Graviton. 

   [Explore the guide](https://aws.amazon.com/ec2/graviton/getting-started/) 

------
#### [ Amazon EC2 Auto Scaling ]
+  **Get started with Amazon EC2 Auto Scaling** 

   In this tutorial, you will setup an Auto Scaling group, terminate your instance and verify the instance was removed from service and replaced. 

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html) 
+  **Tutorial: Scale the size of your Auto Scaling Group** 

   In this tutorial, you will learn how to scale your Auto Scaling group using either manual scaling, scheduled scaling, dynamic scaling, or predictive scaling. 

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html) 
+  **Amazon EC2 Auto Scaling FAQs** 

   Dive deep into the intricacies of EC2 Auto Scaling by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/ec2/autoscaling/faqs/) 

------
#### [ EC2 Image Builder ]
+  **Get started with EC2 Image Builder** 

   This guide will help you set up your environment to create an automated image pipeline for the first time. 

   [Use the tutorial](https://docs.aws.amazon.com/imagebuilder/latest/userguide/set-up-ib-env.html) 
+  **Building golden images using Amazon EC2 Image Builder workshop** 

   This workshop will guide you through creating an EC2 Image Builder pipeline and then developing your own custom components. 

   [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d6c7ecdc-c75f-4ad1-910f-fdd994cc4aed/en-US/100-ec2-ib) 
+  **Implementing up-to-date images with automated EC2 Image Builder pipelines** 

   This post demonstrates how to automatically keep your base or standard images current, incorporating patches and any other changes using EC2 Image Builder pipelines. 

   [Read the blog](https://aws.amazon.com/blogs/compute/implementing-up-to-date-images-with-automated-ec2-image-builder-pipelines/) 

------
#### [ AWS Elastic Beanstalk ]
+  **Get started with AWS Elastic Beanstalk** 

   This tutorial walks you through creating, exploring, updating, and deleting an Elastic Beanstalk application. It takes less than an hour to complete. 

   [Use the tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html) 
+  **Security best practices for Elastic Beanstalk** 

   This guide provides you with general guidelines for securing your Elastic Beanstalk application. 

   [Read the guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-best-practices.html) 
+  **Creating an ECS managed Docker environment with the Elastic Beanstalk console** 

   In this tutorial, you’ll implement an ECS managed Docker environment that uses two containers. 

   [Use the tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecstutorial.html) 

------
#### [ Amazon Lightsail ]
+  **Launch a Linux virtual machine with Amazon Lightsail** 

   In this tutorial, you create an Amazon Linux instance in Amazon Lightsail in seconds. After the instance is up and running, you connect to it via SSH within the Lightsail console using the browser-based SSH terminal. 

   [Use the tutorial](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/) 

------

#### Container services
<a name="container-services-section"></a>

------
#### [ AWS Batch ]
+  **Getting started with AWS Batch – Amazon EC2** 

   In this tutorial, you will set up an AWS Batch compute environment using Amazon EC2 orchestration. 

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-ec2.html) 
+  **Getting started with AWS Batch - Fargate** 

   In this tutorial, you will set up an AWS Batch compute environment using AWS Fargate. 

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-fargate.html) 
+  **Getting started with AWS Batch - Amazon EKS** 

   In this tutorial, you will set up an AWS Batch compute environment using Amazon EKS. 

   [Use the tutorial](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks.html) 
+  **AWS Batch Deep Dive workshop** 

   This workshop provides a deep dive into the basic concepts and use of AWS Batch. 

   [Use the workshop](https://catalog.workshops.aws/aws-batch-deep-dive/en-US) 

------
#### [ Amazon Elastic Container Service ]
+  **Getting started with Amazon ECS** 

   We provide an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers. 

   [Explore the guides](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html) 
+  **Tutorials for Amazon ECS** 

   Explore more than a dozen tutorials on how to perform common tasks - including the creation of clusters and VPCs. 

   [Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html) 
+  **What's new and what's next with Amazon ECS** 

   Learn what's new since the launch of Amazon ECS Anywhere, new features of AWS Fargate, and a look ahead at the exciting enhancements to Amazon ECS. 

   [Watch the video ](https://youtu.be/El64yANTmIA) 
+  **Amazon ECS deployment** 

   This guide offers an overview of Amazon ECS deployment options on AWS and shows how it can be used to manage a simple containerized application. 

   [* *Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html) 
+  **Amazon ECS workshop** 

   This workshop is designed to educate those that might not be familiar with AWS Fargate, Amazon ECS, and Docker container workflow. 

   [Explore the workshop ](https://ecsworkshop.com/) 
+  **Deploy Docker containers on Amazon ECS** 

   Learn how to run a Docker-enabled sample application on an Amazon ECS cluster behind a load balancer, test the application, and delete your resources to avoid charges. 

   [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/) 

------
#### [ Amazon ECS Anywhere ]
+  **Amazon ECS Anywhere FAQs** 

   Answers to frequently-asked questions about Amazon ECS Anywhere. 

   [Read the FAQ](https://aws.amazon.com/ecs/anywhere/faqs/) 
+  **Registering an external instance with Amazon ECS Anywhere** 

   Amazon ECS Anywhere provides support for registering an external instance such as an on-premises server or VM, to your Amazon ECS cluster. Here’s how to use that support. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html) 
+  **Getting Started with Amazon ECS Anywhere ** 

   Amazon ECS Anywhere provides consistent tooling and APIs for all container-based applications and the same Amazon ECS experience for cluster management, workload scheduling, and monitoring both in the cloud and on customer-managed infrastructure. This blog details how and why you might want to use it. 

   [Read the blog](https://aws.amazon.com/blogs/aws/getting-started-with-amazon-ecs-anywhere-now-generally-available/) 

------
#### [ Amazon EKS ]
+  **Getting started with Amazon EKS** 

   Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. 

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) 
+  **Amazon EKS deployment** 

   Explore Amazon EKS deployment options on AWS and learn how it can be used to manage a general containerized application. 

   [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html) 
+  **Amazon EKS cluster deployment ** 

   Use this guide to create an Amazon EKS cluster. 

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) 
+  **Deploy a Kubernetes application** 

   Learn how to deploy a containerized application onto a Kubernetes cluster managed by Amazon EKS. 

   [Expolre the guide](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html) 
+  **Amazon EKS workshop ** 

   Explore practical exercises to learn about Amazon Elastic Kubernetes Service. 

   [Visit the workshop](https://www.eksworkshop.com/) 

------
#### [ Amazon EKS Anywhere ]
+  **Getting started with Amazon EKS Anywhere** 

   This guide helps you get started with Amazon EKS Anywhere, container management software built by AWS that makes it easier to run and manage Kubernetes clusters on-premises and at the edge. 

   [Explore the guide](https://anywhere.eks.amazonaws.com/docs/overview/) 
+  **Amazon EKS Anywhere FAQs** 

   Get answers to your frequently asked questions about Amazon EKS. 

   [Read the FAQs](https://aws.amazon.com/eks/eks-anywhere/faqs/) 
+  **Running Hybrid Container workloads with Amazon EKS Anywhere** 

   This whitepaper provides cloud engineers and architects best practices for operating Amazon EKS Anywhere on customer-managed infrastructure. 

   [Read the whitepaper](https://d1.awsstatic.com/kubernetes-pmm/eks-a/getting-started/AWS_Whitepaper_Running_Hybrid_Container_Workloads_with_Amazon_EKS_Anywhere.pdf) 

------
#### [ Amazon ECR ]
+  **Getting started with Amazon ECR** 

   This guide explains how to use Amazon ECR, an AWS managed container image registry service that is secure, scalable, and reliable. 

   [Explore the guide](https://aws.amazon.com/ecr/getting-started/) 
+  **Amazon ECR FAQs** 

   Answers to frequently-asked questions about Amazon ECR. 

   [Read the FAQs](https://aws.amazon.com/ecr/faqs/) 

------

#### Serverless
<a name="serverless-section"></a>

------
#### [ AWS Fargate ]
+  **AWS Fargate for Amazon ECS** 

   Understand the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) 
+  **Learn how to create an Amazon ECS Linux task for the Fargate launch type** 

   Get started with Amazon ECS on Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html) 
+  **Creating a cluster with a Fargate Linux task using the AWS CLI ** 

   Learn how to set up a cluster, register a task definition, run a Linux task, and perform other common scenarios in Amazon ECS with the AWS CLI. 

   [Get started with the tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html) 

------
#### [ AWS Lambda ]
+  **What is AWS Lambda?** 

   Learn more about AWS Lambda, a compute service that lets you run code without provisioning or managing servers. 

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
+  **Guide to AWS Lambda Pricing** 

   Explore and understand AWS Lambda pricing. You are charged based on the number of requests for your functions and the duration it takes for your code to start. 

   [Visit the page](https://aws.amazon.com/lambda/pricing/) 
+  **Using AWS Lambda with other services** 

   Explore common use cases and learn how invocation works. Navigate a table that covers the services that work with Lambda and how it can be invoked from that service. 

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html) 

------

#### On-premises and hybrid
<a name="on-premises-hybrid-section"></a>

------
#### [ AWS Outposts ]
+  **Get started with AWS Outposts** 

   This guide will demonstrate how to order AWS Outposts and launch an Amazon EC2 instance on your on-premises network. 

   [Explore the guide](https://docs.aws.amazon.com/outposts/latest/userguide/get-started-outposts.html) 
+  **Planning an AWS Outposts implementation** 

   In this free AWS Skill Builder course, you learn about implementation planning for AWS Outposts, including security responsibilities, facilities requirements, networking requirements, and where to deploy your code. 

   [Start the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/75/planning-an-aws-outposts-implementation) 
+  **AWS Outposts Rack FAQs ** 

   Dive deep into AWS Outposts Rack by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/outposts/rack/faqs/) 
+  **AWS Outposts Server FAQs ** 

   Dive deep into AWS Outposts Servers by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/outposts/servers/faqs/) 

------
#### [ AWS Local Zones ]
+  **Get started with AWS Local Zones** 

   This guide will walk you through the steps to enable a Local Zone through the Amazon EC2 console and create resources in the Local Zone subnet. 

   [Explore the guide](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html) 
+  **Connectivity options for Local Zones** 

   This guide discusses the various ways to connect users and applications to resources running in a Local Zone. 

   [Use the workshop](https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity.html) 
+  **Deploying your first 5G enabled application with AWS Wavelength** 

   In this blog, you will walk you through deploying one of the most common Wavelength use cases: machine learning inference. 

   [Read the blog](https://aws.amazon.com/blogs/compute/deploying-your-first-5g-enabled-application-with-aws-wavelength/) 

------

#### Cost and savings optimization
<a name="cost-savings-optimization-section"></a>

------
#### [ AWS Savings Plans  ]
+  **Get started with AWS Savings Plans** 

   This guide will walk you through enabling your settings and permissions in Cost Explorer before using the AWS Billing and AWS Cost Management Console to view, analyze, and manage your Savings Plans. 

   [Explore the guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/get-started.html) 
+  **Blog post: Getting Started with AWS Savings Plans** 

   This post covers how you can use the AWS Cost Management product suite to purchase, manage, and monitor Savings Plans. 

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-savings-plans/) 
+  **Savings Plans FAQ ** 

   Dive deep in to the details of AWS Savings Plans FAQ by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/savingsplans/faq/) 
+  **AWS cost management decision guide** 

   Get what you need to decide how best to optimize AWS costs. 

   [Read the guide](https://aws.amazon.com/getting-started/decision-guides/cost-management-on-aws-how-to-choose/) 

------
#### [ Amazon EC2 Spot Instances ]
+  **Best practices for Amazon EC2 Spot Instances** 

   This guide will cover the best practices to have the best experience using Amazon EC2 Spot Instances. 

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) 
+  **Work with Spot Instances** 

   This guide will cover the details on use and work with Spot Instances. 

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html) 
+  **Amazon EC2 Spot Instances workshop** 

   This set of workshops are designed to get you familiar with Amazon EC2 Spot Instances and how to use them in different scenarios, highlighting best practices to follow when using Spot Instances. 

   [Use the workshops ](https://ec2spotworkshops.com/) 

------
#### [ Amazon EC2 Auto Scaling ]
+  **Get started with Amazon EC2 Auto Scaling** 

   In this tutorial, you will setup an Auto Scaling group, terminate your instance and verify that the instance was removed from service and replaced. 

   [Use the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html) 
+  **Increase or decrease compute capacity of your application with scaling** 

   Learn how to scale your Auto Scaling group using either manual scaling, scheduled scaling, dynamic scaling, or predictive scaling. 

   [Explore the guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html) 
+  **Amazon EC2 Auto Scaling FAQs** 

   Dive deep into the intricacies of EC2 Auto Scaling by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/ec2/autoscaling/faqs/) 

------
#### [ AWS Compute Optimizer ]
+  **Get started with AWS Compute Optimizer** 

   This guide will walk you through opting into AWS Compute Optimizer. 

   [Explore the guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html) 
+  **AWS Compute Optimizer workshop** 

   The goal of this lab is to use AWS Compute Optimizer to gain insights into rightsizing recommendations to optimize your migrated environment on AWS. 

   [Use the workshop](https://catalog.workshops.aws/well-architected-migration/en-US/3-post-migration/compute-optimizer) 
+  **AWS Compute Optimizer FAQs** 

   Dive deep in to the details of AWS Compute Optimizer FAQ by reviewing the FAQ. 

   [Explore the FAQ](https://aws.amazon.com/compute-optimizer/faqs/) 

------

#### Elastic Load Balancing
<a name="elastic-load-balancing-section"></a>

------
#### [ Elastic Load Balancing  ]
+  **Get started with Application Load Balancers** 

   This tutorial provides a hands-on introduction to Application Load Balancers through the AWS Management Console, a web-based interface. 

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancer-getting-started.html) 
+  **Getting started with Network Load Balancers** 

   This tutorial provides a hands-on introduction to Network Load Balancers through the AWS Management Console, a web-based interface. 

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-getting-started.html) 
+  **Getting started with Gateway Load Balancers ** 

   In this tutorial, you’ll implement an inspection system using a Gateway Load Balancer and a Gateway Load Balancer endpoint. 

   [Use the tutorial](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html) 

------

### Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams for compute on AWS.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23compute&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started and learn best practices for compute services and use cases.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=content-type%23whitepaper&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23compute&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for compute.

  [Explore solutions](https://aws.amazon.com/solutions/compute/?nc=sn&loc=3&dn=cp)

## Choosing an AWS container service
<a name="choosing-aws-container-service"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Determine which AWS container service is the best fit for your organization. | 
| **Last updated** | May 16, 2025 | 
| **Covered services** |  +  [Amazon EC2](https://docs.aws.amazon.com/ec2/index.html) <br />+  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) <br />+  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) <br />+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services.html) <br />+  [AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html) <br />+  [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html) <br />+  [AWS Outposts](https://docs.aws.amazon.com/outposts/) <br />+  [Red Hat OpenShift Service on AWS (ROSA)](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)   | 

### Introduction
<a name="intro"></a>

Containers are a key component of modern application development. They are the standard for organizing compute resources, and managing the content of your application deployments.

Containers provide a discrete reproducible compute environment for building software to deploy in the cloud. They also simplify packaging and dependency management. You can use them for everything from orchestrating web applications or very large multi-cluster estates to testing your work and doing a proof of concept on your laptop.

This decision guide helps you get started and choose the right AWS container service for your modern application development.

[![AWS Videos](https://img.youtube.com/vi/xpFI6Jkdnhc?start=177&end=382/0.jpg)](https://www.youtube.com/watch?v=xpFI6Jkdnhc?start=177&end=382)


### Understand
<a name="understand"></a>

Containers offer a number of advantages for packaging, deploying, and running applications:
+ **Portability:** Benefit from a consistent runtime environment that can run on any platform that supports the container runtime. 
+ **Scalability:** Scale applications up or down, based on demand, with lightweight and easily replicated containers.
+ **Consistency:** Ensure that the application runs the same way in all environments with a consistent runtime environment.
+ **Efficiency:** Use fewer resources than traditional virtual machines with lightweight containers.
+ **Isolation:** Improve security and reliability with containers' process-level isolation, with which applications running in separate containers cannot interfere with each other, improving security and reliability.
+ **Agility:** Reduce the time that it takes to bring new features or applications to market by quickly packaging and deploying applications.

![Diagram showing the options available for running containers on AWS](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/container-options-on-aws.png)


You can think about the universe of AWS container services in three distinct layers:
+ The **Compute capacity layer** is where your containers actually run. This layer consists of:
  + **Amazon Elastic Compute Cloud (Amazon EC2) instances:** These instances provide the underlying compute capacity for running containers. You can choose from a wide range of instance types and sizes to match your application requirements. EC2 instances can be used as the compute layer for both Amazon ECS and Amazon EKS.
  + **AWS Fargate:** Fargate is a serverless compute engine for containers with which you can run containers without managing the underlying infrastructure. It removes the need to provision and manage EC2 instances. You can use Fargate with both Amazon ECS and Amazon EKS.
  + **AWS Outposts:** AWS Outposts is a fully managed service that extends AWS infrastructure and services to your on-premises or hybrid environment. With AWS Outposts, you can run containers on AWS infrastructure deployed in your own data center.
+ The **orchestration layer** schedules and scales your environment. This layer includes:
  + ** Amazon Elastic Container Service (Amazon ECS):** Amazon ECS is a fully managed container orchestration service that simplifies the deployment, management, and scaling of containerized applications. You can use Amazon ECS to define tasks and services, handle service discovery, and manage the lifecycle of containers.
  + ** Amazon Elastic Kubernetes Service (Amazon EKS):** Amazon EKS is a managed Kubernetes service with which you can deploy, manage, and scale containerized applications using Kubernetes. It provides a highly available and secure Kubernetes control plane.
  + ** Red Hat OpenShift Service on AWS (ROSA):** ROSA is a fully managed service with which you can deploy and run Red Hat OpenShift clusters on AWS infrastructure. OpenShift is a popular enterprise-grade Kubernetes platform that extends the capabilities of Kubernetes with additional features and tools for building, deploying, and managing containerized applications.
+ The **Vertical solutions layer** is a set of vertical integration services that provide higher-level and bundled services that simplify the process of deploying and managing applications. The AWS services in this layer are:
  + **AWS App Runner:** AWS App Runner is a fully managed service designed to simplify the deployment and use of containerized web applications and APIs. You provide your container image, and App Runner automatically builds, deploys, and scales your application. It handles the provisioning of the underlying compute resources, load balancing, and automatic scaling based on incoming traffic.
  + **Amazon Lightsail:** Amazon Lightsail is a cloud platform that offers pre-configured virtual private servers (instances) and other resources for running applications. It provides pre-defined configurations for quickly provisioning compute instances, databases, storage, and networking resources. Lightsail supports running containerized applications by provisioning instances with Docker pre-installed, aimed at easing the deployment and management of your containers.
  + **AWS Batch:** AWS Batch is a fully managed service with which you can run batch computing workloads on AWS. It dynamically provisions the optimal compute resources based on the volume and specific resource requirements of the batch jobs that you submit. It automatically handles job scheduling, resource provisioning, and scaling based on the workload requirements.
  + **Amazon Elastic Container Registry (Amazon ECR): ** Amazon ECR is a fully managed container registry with which you can store, manage, and deploy container images. It is designed to provide secure and scalable storage for your container images and simplify provisioning containers with the desired images.

**Note**  
AWS provides a variety of ways to deploy and run containers. One of the first considerations is your preference for either a serverless operational model or a Kubernetes operation model. In practice, most customers use both to varying degrees.  
The choice of operating model is explored in-depth in the [Choosing a modern application strategy decision guide](https://aws.amazon.com/getting-started/decision-guides/modern-apps-strategy-on-aws-how-to-choose/), which is a useful resource for anyone who wants to explore this question further. In addition, the [Containers and Serverless Recommendation Guide](https://aws.amazon.com/modern-apps/recommendation-guide/) takes you through the choices to make when choosing your operating model.

### Consider
<a name="consider"></a>

It's important to choose a container service that aligns to your application requirements and operational preferences. The following section outlines some of the key criteria to consider when choosing a container service, as well as supporting tools and services.

------
#### [ Managed service and operation overhead ]

Organizations might choose to build on managed container services to reduce their operational overhead. This approach allows developers and operators to focus on their unique activities that add value, instead of on undiﬀerentiated tasks.

------
#### [ Workload characteristics ]

Understanding your workload patterns can help you make architecture choices. Workload patterns can include web applications, API-based microservices, event-driven applications, streaming and messaging, data pipelines, IT automations, and more. Some workloads perform better or are more cost effective in one compute environment versus another type.

------
#### [ Application portability ]

Many customers want to ensure that their applications can run in—and be migrated or moved to—a different environment. It's important for them to be able to preserve choice, or run an application both on premises and in the cloud.

We recommend building competency in software architectures and build packaging with which you can readily port differentiating business logic between compute services.

Applications built using some technologies might run more effectively on some compute services rather than others.

------
#### [ Organization size and skills ]

The skills of your organization are a major factor when deciding which container services you use. The approach you take can require some investment in DevOps and Site Reliability Engineer (SRE) teams. Building out an automated pipeline to deploy applications is common for most modern application development.

Some choices elevate the amount of management you need to do. For example, some organizations have skills and resources to run and manage a Kubernetes implementation, because they invest in strong SRE teams to manage Kubernetes clusters and find value in the associated skill portability. These teams handle frequent cluster upgrades. For example, Kubernetes has three major releases a year, and deprecates old versions.

Organization size is a key factor, as smaller organizations might have a more limited IT team made up of people fulfilling multiple roles, while larger enterprises can support hundreds of workloads in production at once.

------
#### [ Ease of deployment ]

Different AWS container services meet unique needs in terms of deployment complexity. Here's how each service is optimized for its own role:
+ **AWS App Runner** offers the most straightforward path for you to deploy your application on the internet without managing or customizing the underlying infrastructure.
+ **Amazon ECS** is a good choice if you need more control over the network and security configurations without sacrificing scale or features.
+ **Amazon EKS** provides flexibility and control over application deployment and orchestration provided by Kubernetes technology.

------

### Choose
<a name="choose"></a>

Now that you know the criteria by which you are evaluating your container options, you are ready to choose which AWS container services might be a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine which container services and tools are.



| Containers category | When would you use it? | Services | 
| --- |--- |--- |
| Capacity | Use when you want to run your containers on self-managed or AWS managed compute. | [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)<br />[Amazon EC2](https://docs.aws.amazon.com/ec2/index.html)<br />[AWS Outposts](https://docs.aws.amazon.com/outposts/) | 
|  Orchestration  |  Use when you need the capacity to deploy and manage up to thousands of containers.   |  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) [Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)  | 
| --- |--- |--- |
| Vertical solutions | Use when you or your team don't have a lot of experience with containers or infrastructure.  | [AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)<br />[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)<br />[Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)<br />[AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) | 
|  Tools and services with container support  |  Use for supporting your container operations.  |  [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)  | 
| --- |--- |--- |
| On-premises | Use these services for flexibility in where you run your container-based applications. | [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)<br />[Amazon EKS Anywhere](https://anywhere.eks.amazonaws.com/docs/overview/)<br />[Amazon EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html) | 

### Use
<a name="use"></a>

You should now have a clear understanding of each AWS container service (and the supporting AWS tools and services) and which one might be the best fit for your organization and use case.

To explore how to use and learn more about each of the available AWS container services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

#### Capacity
<a name="capacity"></a>

------
#### [ Amazon EC2 ]
+ **What is Amazon EC2?**

  Get an overview of Amazon EC2. This guide not only provides an introduction to the service, but also covers how to get started using it and then provides in-depth descriptions of key features and how to use them.

  [Explore the guides](https://docs.aws.amazon.com/ec2/index.html)
+ **Amazon EC2 instance types**

  When you launch an EC2 instance, the instance type that you specify determines the hardware of the host computer used for your instance. Each instance type offers different compute, memory, and storage capabilities, and is grouped in an instance family based on these capabilities. This guide walks you through EC2 instance types.

  [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html)
+ **Amazon EC2 Auto Scaling with EC2 Spot Instances**

  Learn how to create a stateless, fault-tolerant workload using Amazon EC2 Auto Scaling with launch templates to request Amazon EC2 Spot Instances.

  [Get started with the tutorial ](https://aws.amazon.com/getting-started/hands-on/ec2-auto-scaling-spot-instances/)

------
#### [ AWS Fargate ]
+ **Getting started with AWS Fargate**

  This guide explains the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of Amazon EC2 instances.

  [Explore the guide ](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
+ **Getting started with the console using Linux containers on AWS Fargate**

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate.

  [Explore the guide](https://aws.amazon.com/getting-started/hands-on/recommendation-engine-for-games-amazon-neptune/)
+ **Creating a cluster with a Fargate Linux task using the AWS CLI**

  Set up a cluster, register a task definition, run a Linux task, and perform other common scenarios in Amazon ECS with the AWS CLI.

  [Explore the guide](https://aws.amazon.com/getting-started/hands-on/recommendation-engine-for-games-amazon-neptune/)

------
#### [ AWS Outposts ]
+ **Getting started with AWS Outposts**

  Access the complete set of AWS Outposts technical documentation.

  [Explore the guides](https://docs.aws.amazon.com/outposts/)
+ **What is AWS Outposts?**

  Get an introduction to this fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises.

  [Explore the guide](https://docs.aws.amazon.com/outposts/latest/server-userguide/what-is-outposts.html)
+ **AWS Outposts servers pricing**

  Get details on the pricing of AWS Outposts servers.

  [Get details on pricing](https://aws.amazon.com/outposts/servers/pricing/)

------

#### Orchestration
<a name="orchestration"></a>

------
#### [ Amazon ECS ]
+ **Getting started with Amazon ECS**

  Get an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+ **Tutorials for Amazon ECS**

  Learn how to perform common tasks—including the creation of clusters and VPCs—when using Amazon ECS.

  [ Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)
+ **Amazon ECS Immersion Day**

  This workshop expands on your foundational understanding of containers and provides practical experience scaling, monitoring, and managing container workflows using Amazon ECS and AWS Fargate.

  [Explore the workshop](https://catalog.workshops.aws/ecs-immersion-day/en-US)
+ **Deploy containers on Amazon ECS**

  Learn how to run a sample application on an Amazon ECS cluster behind a load balancer, test the sample application, and delete your resources to avoid charges.

  [ Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)

------
#### [ Amazon EKS ]
+ **Getting started with Amazon EKS **

  Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes. 

  [Explore the guide ](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+ **Amazon EKS deployment **

  Explore Amazon EKS deployment options on AWS and learn how to use it to manage a general containerized application.

  [Explore the guide ](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html)
+ **Amazon EKS workshop **

  Explore practical exercises to learn about Amazon EKS.

  [ Visit the workshop ](https://www.eksworkshop.com/)

------
#### [ Red Hat OpenShift Service on AWS ]
+ **What is Red Hat OpenShift Service on AWS?**

  Learn how to use this managed service to build, scale, and deploy containerized applications with the Red Hat OpenShift enterprise Kubernetes platform on AWS. 

  [Explore the guide](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html)
+ **Getting started with Red Hat OpenShift Service on AWS**

  Learn how to get started using Red Hat OpenShift Service on AWS (ROSA).

  [Explore the guide](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)
+ **Why would you use ROSA?**

  Watch a video to learn when to use Red Hat OpenShift over standard Kubernetes and explore ROSA in depth.

  [ Watch the video](https://pages.awscloud.com/apn-tv-596.html)

------

#### Vertical solutions
<a name="vertical-solutions"></a>

------
#### [ AWS App Runner ]
+ **What is AWS App Runner?**

  Learn when to use this service to deploy from source code or a container image directly to a scalable and secure web application in the AWS Cloud.

  [Explore the guide](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)
+ **Getting started with AWS App Runner**

  Use this tutorial to configure the source code and deployment, the service build, and the service runtime to deploy your application to AWS App Runner.

  [Use the tutorial](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html)
+ **Deploy a web app using AWS App Runner**

  Follow these step-by-step instructions to deploy a containerized web application using AWS App Runner.

  [Use the tutorial](https://aws.amazon.com/getting-started/guides/deploy-webapp-apprunner/)

------
#### [ AWS Lambda ]
+ **What is AWS Lambda?**

  Learn how to use Lambda to run your code on a high-availability compute infrastructure and perform all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ **AWS Lambda documentation**

  Work with AWS Lambda documentation to understand how you can use this service to run code without provisioning or managing servers and only pay for the compute time that you consume.

  [Explore the guides](https://docs.aws.amazon.com/lambda/)
+ **Working with Lambda container images locally**

  Learn how you can use a deployment package to deploy your function code to Lambda. Lambda supports two types of deployment packages: container images and `.zip` file archives.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)

------
#### [ Amazon Lightsail ]
+ **What is Amazon Lightsail?**

  Get the full story on Amazon Lightsail, including what it does and how you can benefit from it. This guide also includes step-by-step guidance to help you get started using Lightsail and then configure it to meet your needs.

  [Explore the guide](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html)
+ **Creating Lightsail container service images**

  Learn how to create a container image on your local machine using a Dockerfile. You can then push it to your Lightsail container service to deploy it.

  [Explore the guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images.html)
+ **Amazon Lightsail resource center**

  Explore Lightsail tutorials, videos, and links to core concept documentation.

  [Visit the resource center](https://aws.amazon.com/lightsail/resources/)

------
#### [ AWS Batch ]
+ **What is AWS Batch?**

  Learn how to use AWS Batch to run batch computing workloads in the AWS Cloud.

  [Explore the guide](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
+ **Best practices for AWS Batch**

  Consider this guidance on how to run and optimize your workloads when using AWS Batch.

  [Explore the guide](https://docs.aws.amazon.com/batch/latest/userguide/best-practices.html)
+ **AWS Batch workshops center**

  Use these workshops, organized in a progressive manner from beginner to advanced, to explore and learn AWS Batch.

  [Explore the workshops](https://batch.hpcworkshops.com)

------

#### Tools and services with container support
<a name="tools-and-services"></a>

------
#### [ Amazon ECR ]
+ **Amazon ECR documentation**

  Use the Amazon ECR documentation to explore the best ways to use this fully managed container registry. 

  [Explore the guides](https://docs.aws.amazon.com/ecr/)
+ **What is Amazon Elastic Container Registry (Amazon ECR)?**

  A guide to getting started with—and using—Amazon ECR. 

  [Explore the guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
+ **Amazon ECR in Multi-Account and Multi-Region Architectures**

  Explore key considerations for Amazon ECR architectures that span across AWS accounts and AWS Regions, and architectures related to hypothetical customer use cases.

  [Read the blog post](https://aws.amazon.com/blogs/containers/amazon-ecr-in-multi-account-and-multi-region-architectures/)

------

#### On-premises
<a name="on-premises"></a>

------
#### [ Amazon ECS Anywhere ]
+ **What is Amazon ECS Anywhere?**

  Learn how Amazon ECS Anywhere provides support for registering an *external instance*, such as an on-premises server or virtual machine (VM), to your Amazon ECS cluster.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)
+ **Amazon ECS Anywhere pricing**

  Use this pricing guide to understand Amazon ECS Anywhere pricing, which is based on a model in which you are charged based on the amount of time the instances you have registered to an Amazon ECS cluster are connected to the ECS control plane, rounded up to the nearest second. 

  [Explore the pricing guide](https://aws.amazon.com/ecs/anywhere/pricing/)
+ **Amazon ECS Anywhere FAQs**

  Get answers to frequently asked questions about Amazon ECS Anywhere.

  [Explore the FAQs](https://aws.amazon.com/ecs/anywhere/faqs/)

------
#### [ Amazon EKS Anywhere ]
+ **Amazon EKS Anywhere documentation**

  Use the documentation to understand the use of and best practices for Amazon EKS Anywhere.

  [Read the documentation](https://anywhere.eks.amazonaws.com/docs/)
+ **Amazon EKS Anywhere pricing**

  Use this pricing guide to understand Amazon EKS Anywhere pricing.

  [Explore the pricing guide](https://aws.amazon.com/eks/eks-anywhere/pricing/)
+ **Amazon EKS Anywhere FAQs**

  Get answers to frequently asked questions about Amazon EKS Anywhere.

  [Explore the FAQs](https://aws.amazon.com/eks/eks-anywhere/faqs/)

------
#### [ Amazon EKS Hybrid Nodes ]
+ **Amazon EKS Hybrid Nodes overview**

  Use the documentation to understand the use of and best practices for Amazon EKS Hybrid Nodes.

  [Read the documentation](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html)
+ **Amazon EKS Hybrid Nodes pricing**

  Use the pricing guide to understand Amazon EKS Hybrid Nodes pricing.

  [Explore the pricing guide](https://aws.amazon.com/eks/pricing/)
+ **A deep dive into Amazon EKS Hybrid Nodes**

  Explore how you can use your existing on-premises and edge infrastructure as nodes in Amazon EKS clusters.

  [Read the blog post](https://aws.amazon.com/blogs/containers/a-deep-dive-into-amazon-eks-hybrid-nodes/)

------

### Explore
<a name="explore"></a>
+ **For your role**
  + [Developers](https://aws.amazon.com/getting-started/hands-on/?intClick=dev-center-2021_main&getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=category%23containers&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all)
  + [Solution Architects](https://aws.amazon.com/architecture/containers/?achp_navtc3&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)
  + [Professional development](https://explore.skillbuilder.aws/learn/public/learning_plan/view/83/containers-learning-plan)
  + [Startups](https://aws.amazon.com/startups/start-building/how-to-choose-compute-option/)
  + [Decision makers](https://aws.amazon.com/free/containers/)
+ **For an introduction**
  + [Docker](https://aws.amazon.com/docker/)
  + [Kubernetes](https://aws.amazon.com/kubernetes/)
  + [Breaking a monolith into microservices](https://aws.amazon.com/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2/?e=gs2020&p=deepdivecontainers&p=gsrc&c=dd_c)
+ **For a video**
  + [Containers from the couch](https://containersfromthecouch.com/)
  + [How to containerize anything\!](https://youtu.be/JpHlAV7P-Sw)
  + [Building a container CI/CD pipeline](https://youtu.be/b16Gpvjxxnc)
  + [Building a container app with AWS CDK](https://youtu.be/64DzoDM_kQc)
+ **Architecture diagrams**

  Explore reference architecture diagrams for containers on AWS.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23containers&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started and learn best practices.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=content-type%23whitepaper&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23containers&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS solutions**

  Explore vetted solutions and architectural guidance for common use cases for containers.

  [Explore solutions](https://aws.amazon.com/solutions/compute/containers-orchestration-operations/)

## AWS Fargate or AWS Lambda?
<a name="fargate-or-lambda"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | To explore whether AWS Fargate or AWS Lambda meet your needs for a serverless compute service. | 
| **Last updated** | August 21, 2026 | 
| **Covered services** |  +  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)  <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)   | 

### Introduction
<a name="fl-introduction"></a>

You might have already considered the broader range of AWS compute services. These are covered in the [Choosing an AWS compute service decision guide](https://docs.aws.amazon.com/decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.html). If you narrowed your choice to AWS Lambda and AWS Fargate, you are likely looking for a serverless compute service. Both services share the following benefits:

**Note**  
This guide covers Lambda functions and Lambda Managed Instances. Lambda MicroVMs, which provide session-based isolated sandboxes for running untrusted code, are a distinct compute primitive not covered in this guide. For information about Lambda MicroVMs, see [Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) in the Lambda Developer Guide.

**Note**  
AWS also offers related compute options not covered in this guide, including Amazon ECS Express Mode for simplified container deployment and Amazon ECS Managed Instances for running containers on specific EC2 instance types with managed infrastructure. For a complete view of container compute options, see [the Amazon ECS Developer Guide](https://docs.aws.amazon.com/ecs/latest/developerguide/AWS_Fargate.html).
+  **Reduced operational overhead:** Both Lambda and Fargate abstract away server management. This reduces the need for patching, maintenance, and capacity planning. 
+  **Pay-per-use pricing:** You only pay for the compute resources you actually use. This can lower costs for variable workloads. 
+  **Faster deployment:** These services typically offer quicker deployment times. This is compared to provisioning and configuring EC2 instances. 
+  **Built-in high availability:** Both services handle infrastructure redundancy automatically. 
+  **Simplified compliance:** A reduced attack surface and built-in security features can ease compliance efforts. 
+  **Focus on code:** Developers can concentrate on writing application code rather than managing infrastructure. 

 While Lambda and Fargate are both serverless options, there are significant differences between them. 

**AWS Fargate**  
AWS Fargate is a serverless compute engine for containers. It is primarily used with Amazon ECS. With Fargate, you can focus on deploying and scaling containerized applications without managing the underlying infrastructure. Fargate is ideal for long-running applications, microservices, or batch processing. It gives you fine-grained control over resource allocation (CPU, memory) without managing underlying servers.

**AWS Lambda**  
AWS Lambda is a serverless computing service that runs your code as functions in response to events. It manages the underlying compute resources for you. Lambda functions are best suited for event-driven applications. Examples include processing files uploaded to Amazon S3, responding to HTTP requests, running scheduled tasks, or processing data streams. Data stream sources include Amazon Kinesis and Amazon DynamoDB. Lambda functions have a maximum execution time of 15 minutes per invocation. Lambda also offers durable functions, a programming model for workflows that can run for up to 1 year using checkpoint-and-replay execution. With Lambda Managed Instances, you can run functions on a wide range of EC2 instance types. You retain the operational simplicity of Lambda.

Use the following guidelines to help you choose between the two services:
+ If your project involves event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows, consider Lambda functions.
+ If your workloads are steady-state or predictable and benefit from EC2 pricing and specialized compute, Lambda Managed Instances might be well suited.
+ If you need to run containerized applications with specific resource needs or persistent processes, Fargate is worth considering.

You can also combine both services in a hybrid architecture. For patterns that combine Lambda and Fargate, see [Run event-driven and scheduled workloads at scale with Fargate](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-event-driven-and-scheduled-workloads-at-scale-with-aws-fargate.html) in AWS Prescriptive Guidance.

The following table provides a side-by-side comparison of key differences between these services.


|  |  |  | 
| --- |--- |--- |
|  Feature  |  AWS Fargate  |  AWS Lambda  | 
|  Execution model  |  Container-based, serverless compute  |  Event-driven, serverless functions (with optional durable orchestration)  | 
|  Supported languages  |  Any language that can run in a container  |  Node.js, Python, Java, C\#, Go, Ruby, and PowerShell. You can also [build a custom runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html) for other languages. | 
|  Use case  |  Long-running, containerized applications  |  Short-duration, event-driven tasks (or workflows up to 1 year with durable functions)  | 
|  Execution pattern  |  Continuous compute (long-running processes, persistent connections)  |  Event-driven with optional wait-heavy orchestration (durable functions)  | 
|  Scaling  |  Automatic scaling based on desired task count, with predictive scaling support  |  Automatic scaling per request  | 
|  Cold start  |  Varies by image size and configuration  |  Varies by runtime and package size  | 
|  Execution time limit  |  No hard limit  |  15 minutes per invocation (durable functions orchestrate workflows up to 1 year)  | 
|  Memory allocation  |  Up to 244 GiB  |  Up to 10 GiB  | 
|  CPU allocation  |  Up to 32 vCPU  |  Proportional to memory, up to 6 vCPU  | 
|  Networking  |  Runs in VPC with ENIs; supports Amazon VPC Lattice and IPv6-only configurations  |  Can run in AWS managed VPC or attached to a customer-managed VPC using AWS Hyperplane | 
|  State management  |  Containers can maintain in-memory state across requests while running. External storage is recommended for critical data.  |  Stateless by design (state must be managed externally, for example, Amazon S3, Amazon DynamoDB, Amazon EFS). Durable functions can persist workflow state for up to 1 year.  | 
|  Container support  |  Full container support  |  Limited container support (via container image deployments)  | 
|  Orchestration  |  Integrated with Amazon ECS |  No orchestration required  | 
|  Deployment strategies  |  Native blue/green, canary, and linear deployments  |  Weighted aliases for gradual deployments  | 
|  Pricing model  |  Per second billing for vCPU and memory used; Fargate Spot available for x86 and ARM  |  Per invocation and duration (GB-seconds); Lambda Managed Instances offer EC2-based pricing  | 
|  Concurrency limits  |  Based on cluster capacity  |  1000 concurrent executions by default (can be increased)  | 
|  Event-driven invocation  |  Requires additional setup  |  Native support for various AWS event sources  | 
|  Cold start mitigation  |  Lazy loading images with Seekable OCI (SOCI) can speed up starting Fargate tasks  |  Provisioned concurrency, SnapStart (for Java, Python, and .NET), and Lambda Managed Instances available  | 
|  Package size limit  |  No specific limit (container size limited by configured ephemeral storage, 200 GiB maximum)  |  250 MB unzipped, including layers, 10 GB for container image deployments  | 

### Differences between Fargate and Lambda
<a name="fl-differences"></a>

 Explore the differences between Fargate and Lambda in a number of key areas. 

------
#### [ Languages supported ]

 **Fargate**: AWS Fargate is a serverless compute engine for containers, used with Amazon ECS for orchestration. It supports any programming language or runtime environment that can be packaged into a Docker container. This flexibility means you can use virtually any language, framework, or library that suits your application needs. You can use Python, Java, Node.js, Go, .NET, Ruby, PHP, or even custom languages and environments. Fargate can run them as long as they are encapsulated in a container. This broad language support makes Fargate ideal for running diverse applications. These include legacy systems, multi-language microservices, and modern cloud-native applications. 

 **Lambda**: AWS Lambda offers native support for a more limited set of languages compared to Fargate. Lambda functions are purpose-built for event-driven workloads. Lambda officially supports the following languages and runtimes: 
+  Node.js 
+  Python 
+  Java 
+  Go 
+  Ruby 
+  C\# 
+  PowerShell 

 Lambda also supports custom runtimes. With custom runtimes, you can bring your own language or runtime environment. However, this requires more setup and management compared to using natively supported options. If you deploy your Lambda function from a container image, you can write your function in Rust. Use an AWS OS-only base image and include the Rust runtime client in your image. If you use a language without an AWS-provided runtime interface client, you must create your own.

------
#### [ Event-driven invocation ]

 **Lambda** is inherently designed for event-driven computing. Lambda functions are triggered in response to changes in data, user actions, or scheduled tasks. It integrates natively with many AWS services. These include Amazon S3 (for example, invoking a function when a file is uploaded), DynamoDB (for example, triggering on data updates), and API Gateway (for example, handling HTTP requests). The Lambda event-driven architecture is ideal for applications that need to respond immediately to events. These applications do not require persistent compute resources. 

 **Fargate** is not natively event-driven. However, with some additional boilerplate logic, it can integrate with event sources such as Amazon SQS and Kinesis. Lambda handles the bulk of this integration logic for you. With Fargate, you must implement this integration yourself using the APIs for these services. 

------
#### [ Runtime/use cases ]

 **Fargate** is designed to run containerized applications. It provides a flexible runtime environment where you can define the CPU, memory, and networking settings for your containers. Fargate operates on a container-based model. It supports long-running processes, persistent services, and applications with specific runtime requirements. The containers in Fargate can run indefinitely because there is no hard limit on execution time. This makes it ideal for applications that need to run continuously. With container restart policies in Fargate, individual containers within a task can restart automatically without restarting the entire task. This improves resilience for multi-container workloads. Fargate integrates with CloudWatch Container Insights with enhanced observability. With this feature, you get detailed per-container metrics and traces for monitoring application performance. 

 **Lambda** functions are optimized for short-lived, event-driven tasks. Lambda functions have a maximum execution time of 15 minutes per invocation. This makes Lambda functions well-suited for scenarios such as file processing, real-time data streaming, and HTTP request handling. These tasks are brief and do not require long-running processes. 

 With durable functions in Lambda, you can build long-running workflows that can persist state across multiple invocations for up to 1 year. Durable functions provide built-in error handling, automatic retries, and recovery after failures. A durable functions SDK is available for JavaScript, TypeScript, Python, Java, and C\# (.NET). During wait periods, your function suspends without incurring compute charges. With durable functions, you can address use cases that previously required persistent compute environments. 

 When choosing between durable functions and Fargate for long-running workloads, consider the execution pattern. Durable functions are cost-effective for workflows that spend most of their time waiting, such as human approvals, scheduled delays, or external API callbacks. You do not incur compute charges during wait periods. Fargate is more appropriate for workloads that require continuous compute, such as data processing, persistent network connections, or services that must remain active without interruption. 

 In Lambda, the runtime environment is more abstracted. You have less control over the underlying infrastructure. For standard functions, each invocation is independent and stateless. Any state or data that needs to persist between invocations must be managed externally. Examples include databases or storage services. 

------
#### [ Scaling ]

 **Fargate** scales by adjusting the number of running tasks. This is based on the desired state defined in your container orchestration service (Amazon ECS). Scaling can be done manually or automatically through Amazon EC2 Auto Scaling. For more information, see [Under the hood: Amazon ECS and Fargate increase task launch rates](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-elastic-container-service-and-aws-fargate-increase-task-launch-rates/) on the AWS Containers blog.

 In Fargate, each task runs in its isolated environment. Scaling involves launching additional tasks or stopping them based on the load. The Amazon ECS service scheduler can launch up to 500 tasks in less than a minute per service. This applies to web and other long-running services. Amazon ECS also supports predictive scaling. It uses historical patterns to proactively increase tasks before demand spikes occur. Target tracking policies for CPU and memory utilization support 20-second metric resolution. This enables faster scaling signal detection. Amazon ECS can also automatically rebalance service tasks across Availability Zones. This maintains high availability. Fargate integrates with AWS Fault Injection Service (FIS). With FIS, you can run controlled fault injection experiments to test application resilience.

![Diagram showing task launch differences between Fargate and Lambda.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/task-launches.png)


 For **Lambda**, *concurrency* is the number of in-flight requests that your AWS Lambda function is handling at the same time. This differs from concurrency in Fargate. Each Fargate task can handle concurrent requests as long as there are available compute and network resources. For each concurrent request, Lambda provisions a separate instance of your execution environment. As your functions receive more requests, Lambda automatically scales the number of execution environments. This continues until you reach your account concurrency limit. By default, Lambda provides your account with a total concurrency limit of 1,000 concurrent executions. This limit applies across all functions in an AWS Region. You can request a quota increase if needed. 

 With Lambda Managed Instances, scaling works differently. Instead of provisioning a new execution environment for each concurrent request, Managed Instances scale asynchronously based on CPU resource utilization. Each execution environment can handle multiple concurrent invocations. This approach maximizes resource utilization. It is well-suited for steady-state or predictable workloads.

 For each Lambda function using the default compute type, the concurrency scaling rate is 1,000 execution instances every 10 seconds. This continues up to the maximum account concurrency. For more information, see [Lambda functions now scale 12 times faster when handling high-volume requests](https://aws.amazon.com/blogs/aws/aws-lambda-functions-now-scale-12-times-faster-when-handling-high-volume-requests/) on the AWS Compute blog. If the number of requests in a 10 second period exceeds 1,000, the additional requests are throttled. The following graph demonstrates how Lambda scaling works assuming an account concurrency of 7000. 

![Bar graph showing how instances are throttled when number exceeds 1000.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/instance-throttling.png)


------
#### [ Cold start and cold-start mitigation ]

 **Lambda** functions can experience cold starts. These occur when a function is invoked after being idle for some time. During a cold start, the Lambda service initializes a new execution environment. This includes loading the runtime, dependencies, and the function code. Cold start duration varies from under 100 milliseconds to over 1 second, depending on runtime, package size, and initialization logic. For runtimes with longer initialization times such as Java or C\#, cold starts can be longer without optimization. Cold starts can impact performance of applications that require low-latency responses. 

 To mitigate cold starts in Lambda, consider the following strategies: 
+  **Minimize function size**: Reduce the size of your function package and its dependencies. This can decrease the time needed for initialization. 
+  **Increase memory allocation**: Higher memory allocations increase CPU capacity. This can reduce initialization time. 
+  **Keep functions warm**: Periodically invoke your Lambda functions (for example, using CloudWatch Events). This keeps them active and reduces the likelihood of cold starts. 
+  **Lambda SnapStart**: Use [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) for Java, Python, and .NET functions to reduce startup time. SnapStart takes a snapshot of the initialized execution environment. Subsequent invocations resume from the snapshot rather than performing a full cold start. 
+  **Provisioned concurrency**: This feature keeps a specified number of function instances warm and ready to serve requests. This reduces cold start latency. However, it increases costs. You pay for the provisioned instances even if they are not actively handling requests. 
+  **Lambda Managed Instances**: Run functions on a wide range of EC2 instance types. These include processors such as Graviton4 and high-bandwidth networking options. Pre-provisioned execution environments eliminate cold starts. Lambda handles instance lifecycle, OS and runtime patching, routing, load balancing, and automatic scaling. Lambda Managed Instances also support multi-concurrent invocations per execution environment. They offer EC2 pricing advantages such as Compute Savings Plans and Reserved Instances. 

 **Fargate** is not generally impacted by cold starts in the same way as Lambda. The time to start a Fargate task correlates directly to the time it takes to [pull the container images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-pull-behavior.html) defined in the task from the image registry. Fargate also supports lazy loading of container images that have been indexed with [Seekable OCI (SOCI)](https://aws.amazon.com/blogs/aws/aws-fargate-enables-faster-container-startup-using-seekable-oci/). Lazy loading container images with SOCI reduces the time to launch Amazon ECS tasks on Fargate. Fargate uses SOCI index manifest v2. This provides improved performance for lazy loading. After a task starts on Fargate, it is a long-running process. It is always ready to handle requests. If you need to start new tasks in response to scaling events, there might be some delay during initialization. This is typically less significant compared to Lambda cold starts. 

------
#### [ Memory and CPU options ]

 **Fargate** provides granular control over both memory and CPU resources for your containerized applications. When you launch a task in Fargate, you can specify the exact CPU and memory requirements for your application. The CPU and memory allocations are independent. You can choose combinations that best suit your workload. You can select CPU values ranging from 0.25 vCPUs to 32 vCPUs. Memory ranges from 0.5 GB to 244 GB per task, depending on your configuration. 

 This flexibility is ideal for applications with specific performance characteristics. Examples include memory-intensive databases or CPU-bound computation tasks. Fargate allows you to optimize your resource allocation. You can balance cost and performance effectively. 

 In **Lambda**, memory and CPU are linked. The CPU is automatically allocated in proportion to the amount of memory you select. You can choose memory allocations between 128 MB and 10 GB, in 1 MB increments. The CPU scales with the memory, up to 6 vCPU. Higher memory settings result in more CPU power. However, you do not have direct control over the CPU allocation itself. 

 This model is designed for simplicity. You can quickly adjust memory settings without managing CPU configurations. However, it might be less flexible for workloads that require a specific balance between CPU and memory resources. The Lambda model is suitable for tasks where you want straightforward scaling based on memory needs. It might not be optimal for applications with complex or highly specific resource demands. 

------
#### [ Networking ]

 When you deploy tasks in **Fargate**, they run in an Amazon VPC (Amazon Virtual Private Cloud). This gives you full control over the networking environment. You can configure security groups, network access control lists (ACLs), and routing tables. Each Fargate task gets its own network interface with a dedicated private IP address. You can assign a public IP address if needed. 

 Fargate supports advanced networking features such as load balancing (using AWS Elastic Load Balancing), VPC peering, and direct access to other AWS services within the VPC. You can also use AWS PrivateLink for secure, private connectivity to supported AWS services. This avoids traversing the internet. Fargate tasks also support Amazon VPC Lattice. This provides standardized service-to-service connectivity, security, and observability. Fargate tasks can run in IPv6-only configurations. This allows tasks to communicate exclusively over IPv6. 

 By default, **Lambda** functions run in a managed network environment. You do not have direct control over network interfaces or IP addresses. However, Lambda can be attached to a customer-managed VPC using AWS Hyperplane. This enables you to control access to resources inside your VPC. 

 When Lambda functions are attached to a customer-managed VPC, they inherit the VPC security groups and subnet configurations. This allows them to interact securely with other AWS services (such as RDS databases) within the same VPC. Because Lambda scales by creating many concurrent execution environments, each maintains its own database connection. High concurrency can exhaust database connection limits. For relational database access, use [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) to pool and manage connections. This avoids connection exhaustion during high concurrency. 

 The Lambda service uses a Network Function Virtualization platform to provide NAT capabilities. This connects the Lambda VPC to customer VPCs. It configures the required elastic network interfaces (ENIs) when Lambda functions are created or updated. It also enables ENIs from your account to be shared across multiple execution environments. This allows Lambda to make more efficient use of network resources when functions scale. 

ENIs are an exhaustible resource with a soft limit of 250 per Region. Monitor elastic network interface usage if you configure Lambda functions for VPC access. Lambda functions in the same AZ and same security group can share ENIs. If you increase concurrency limits in Lambda, evaluate if you need an elastic network interface increase. If the limit is reached, invocations of VPC-enabled Lambda functions are throttled. 

------
#### [ Pricing model ]

 **Fargate** pricing is based on the resources allocated to your containers. Specifically, this means the vCPU and memory you select for each task. You are billed per second, with a one-minute minimum charge. Costs are directly tied to the resources your application consumes. You pay for what you provision, regardless of whether the application is actively processing requests. Fargate is well-suited for predictable workloads where you need specific resource configurations. You can optimize costs by adjusting the allocated resources. Fargate Spot is available for both x86 and ARM-based Linux workloads. This provides significant cost savings for fault-tolerant applications. There might be additional charges for related services. These include data transfer, storage, and networking (for example, VPC, Elastic Load Balancing). 

 **Lambda** has a different pricing structure that is event-driven and pay-per-execution. You are charged based on the number of requests and execution duration. Duration is measured in milliseconds. Lambda also factors in the amount of memory you allocate to your function. Costs scale based on the memory used and the execution time. The pricing model includes a free tier. It offers 1 million free requests and 400,000 GB-seconds of compute time per month. This makes Lambda particularly cost-effective for low-volume, sporadic workloads. 

 The Lambda pricing model is ideal for applications with unpredictable or bursty traffic patterns. You only pay for actual function invocations and execution time. You do not need to provision or pay for idle capacity. 

 With Lambda Managed Instances, Lambda offers instance-based pricing that uses EC2 pricing models. These include On-Demand, Reserved Instances, and Compute Savings Plans. This can drive cost efficiency for steady-state or predictable workloads. 

 Both Fargate and Lambda are eligible for [Compute Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html). These can reduce costs by up to 66% in exchange for a commitment to a consistent amount of compute usage. This is measured in dollars per hour for a 1- or 3-year term. 

 When you compare costs between the two services, you typically pay less with Lambda at lower traffic volumes. However, the per-second resource billing of Fargate tends to be more economical for sustained, high-throughput workloads. As request volume grows, Lambda costs scale linearly. In contrast, Fargate costs remain relatively stable regardless of requests handled within the provisioned resources. 

------

### Use
<a name="fl-use"></a>

Now that you've read about the criteria for choosing between AWS Fargate and AWS Lambda, you can select the service that meets your needs, and use the following information to help you get started using each of them. 

------
#### [ AWS Fargate ]
+  **Learn how to create an Amazon ECS Linux task for the Fargate launch type** 

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your Linux tasks.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html) 
+  **Learn how to create an Amazon ECS Windows task for the Fargate launch type** 

   Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your Windows tasks. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Windows_fargate-getting_started.html) 
+  **Getting started with Fargate and Amazon EKS** 

   This guide describes how to get started running your pods on AWS Fargate with your Amazon EKS cluster. 

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html) 
+  **AWS Fargate pricing**

   Use this guide to understand how vCPU, memory, storage, and operating system configurations impact AWS Fargate pricing. 

   [Explore the guide](https://aws.amazon.com/fargate/pricing/) 
+  **AWS Fargate frequently asked questions**

   Get answers to common questions about AWS Fargate capabilities, and best practices for implementation. 

   [Explore the guide](https://aws.amazon.com/fargate/faqs/) 

------
#### [ AWS Lambda ]
+  **Create a serverless file-processing app** 

   A step-by-step walkthrough of setting up and using Amazon SNS. It covers topics such as creating a topic, subscribing endpoints to a topic, publishing messages, and configuring access permissions. 

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/file-processing-app.html) 
+  **Serverless Developer Guide** 

   This guide helps you develop a better conceptual understanding of serverless application development, and how various AWS services fit into together to create *application patterns* that form the core of your cloud applications. 

   [Explore the guide](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html) 
+  **Serverless Land** 

   This site brings together the latest information, blogs, videos, code, and learning resources for AWS Serverless. Learn to use and build apps that scale automatically on low-cost, fully managed serverless architecture. 

   [Explore the site](https://serverlessland.com/lambda) 
+  **AWS Lambda pricing**

   Use this guide to estimate expenses and optimize costs based on function usage and configuration. It includes a pricing calculator to calculate your AWS Lambda and architecture cost in a single estimate. 

   [Explore the guide](https://aws.amazon.com/lambda/pricing/) 
+  **AWS Lambda frequently asked questions**

   Get answers to common questions about AWS Lambda capabilities, and best practices for implementation. 

   [Explore the guide](https://aws.amazon.com/lambda/faqs/) 

------

## Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2?
<a name="lightsail-elastic-beanstalk-ec2"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | To explore whether Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2 meets your needs for a cloud platform or compute web service. | 
| **Last updated** | September 29, 2026 | 
| **Covered services** |  +  [Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html) <br />+  [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) <br />+  [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)   | 

### Introduction
<a name="introduction"></a>

 Amazon Web Services (AWS) offers services that can meet your needs for a cloud platform or compute web service. Three services that are often considered alongside one another are:
+ **Amazon Lightsail** — a set of services designed to help you build websites or web applications. Consider Lightsail if you want a simple unified platform with foundational services, including virtual servers, HTTP load balancing, managed databases, public container deployment, content delivery network (CDN), DNS management, and domain registration. Lightsail provides fixed and predictable monthly pricing. 
+ **AWS Elastic Beanstalk** — a service that makes it easy to deploy, manage, and scale web applications and services. It supports several programming languages such as Python, Java, PHP, Node.js, Ruby, .NET, and Go. With Elastic Beanstalk, you simply upload your application code, and AWS handles the underlying infrastructure, including provisioning resources like Amazon EC2 instances, load balancers, and databases, as well as auto-scaling and monitoring. Elastic Beanstalk offers two deployment modes. Standard runs your application on Amazon EC2 instances. Cluster (also called Cluster Mode) runs your application as containers on an Amazon EKS cluster that Elastic Beanstalk creates and operates. It provides built-in integration with AWS services like RDS, Amazon S3, and CloudWatch. Elastic Beanstalk offers a balance between control and automation, giving developers the ability to customize infrastructure while offloading operational overhead. There is no additional charge for Elastic Beanstalk. You pay for AWS resources (e.g. Amazon EC2 instances or Amazon S3 buckets) you create to store and run your application. 
+ **Amazon Elastic Compute Cloud (Amazon EC2)** — an AWS service that provides on-demand, scalable computing capacity, with the goal of allowing you to develop, deploy, and scale applications faster. You can use it to launch as many or as few compute instances as you need, configure security and networking, and manage storage. You can also add capacity by provisioning larger instances (up to hundreds of cores and thousands of GiB memory) or load balancing clusters of smaller instances. Several different pricing models are available depending on your requirements. 

 When choosing between Lightsail, Elastic Beanstalk, and Amazon EC2, keep in mind the future growth of your workload and how you intend to grow your AWS environment. If your future deployment requires advanced networking or integration with AWS services such as Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, or AWS Lambda, you should strongly consider using Amazon EC2. 

Here's a high-level view of the key differences between these services to get you started. 


|  |  ![](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Amazon_Lightsail_64.png) **Amazon Lightsail**  |  ![](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/aeb.png) **Elastic Beanstalk**  |  ![](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Amazon_EC2_64.png) **Amazon EC2**  | 
| --- | --- | --- | --- | 
| **Instance Size** | Multiple instance types. General-purpose instances range from 512 MiB to 256 GiB of RAM, and 2 to 64 vCPUs. Compute-optimized instances provide up to 72 vCPUs, and memory-optimized instances provide up to 512 GB of memory. For more information, see the *compute and block storage* tab in the [differences](#lse-differences) section below.<br /> | 400\+ instance types, from 0.5 GiB to 24 TiB of RAM, and 1 to 448 vCPUs.<br /> | 400\+ instance types, from 0.5 GiB to 24 TiB of RAM, and 1 to 448 vCPUs.<br /> | 
| **Block Storage** | Preconfigured disks up to 1280 GB per instance (storage size is tied to instance type). Attach additional disks up to 16 TB with variable pricing.<br /> | Amazon EBS volumes up to 64 TB per volume. Input/output operations per second (IOPS) up to 64,000 per volume (storage size is independent of instance type).<br /> | Amazon EBS volumes up to 64 TB per volume. Input/output operations per second (IOPS) up to 64,000 per volume (storage size is independent of instance type).<br /> | 
| **Application Blueprints** | 34 pre-configured blueprints, including WordPress, Magento, Drupal, Node.js, and more.<br /> | A number of managed platforms on Amazon Linux (Docker, Go, Java, Ruby, Python, .NET core, Tomcat), and .NET/IIS on Windows Server.<br /> | Common operating systems and with pre-configured software and services in the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?prevFilters=%257B%2522ref_%2522%3A%2522hmpg_categories_all%3Fref_%3Dhmpg_categories_promo%2522%257D&searchTerms=ec2&FULFILLMENT_OPTION_TYPE=AMAZON_MACHINE_IMAGE%2CCONTAINER&filters=FULFILLMENT_OPTION_TYPE).<br /> | 
| **Container Support** | Simple deployment of public container images for a fixed monthly cost including data transfer.  | Supports individual Docker containers and multiple containers with Docker Compose. With Cluster Mode, Elastic Beanstalk runs container-based applications on an Amazon EKS cluster that it creates and operates.  |  Run container workloads natively on Amazon EC2 using self-managed Docker or Kubernetes, or deploy containers to separate AWS container services such as Amazon ECS (including ECS Express Mode), Amazon EKS, AWS Fargate, AWS Elastic Beanstalk, and Lambda. As of April 30, 2026, AWS App Runner no longer accepts new customers; existing services continue to run. <br /> | 
| **Data Transfer** |  Generous data transfer allocation included with the fixed monthly fee for every Lightsail compute instance. <br /> |  Pay per GB data transfer (out) with ﬂexible pricing tiers and no cost for ingress traﬃc. <br /> | Pay per GB data transfer (out) with flexible pricing tiers and no cost for ingress traffic.<br /> | 
| **Load Balancing** | Basic load balancing of HTTP/HTTPS for low volume web traffic (up to 5 GB per hour). | Flexible load balancing for any type of networking use case, including HTTP, HTTPS, TCP, UDP, health checks, auto scaling, and more. | Flexible load balancing for any type of networking use case, including HTTP, HTTPS, TCP, UDP, health checks, auto scaling, and more.<br /> | 
| **CDN Support** | Global content delivery from Lightsail sources for a fixed monthly fee (up to 50 GB per month included for the first year). | Amazon CloudFront integration provides flexible content delivery from Amazon EC2 or other AWS or external sources on a pay per GB basis (1 TB per month included for the first year).  | Amazon CloudFront integration provides flexible content delivery from Amazon EC2 or other AWS or external sources on a pay per GB basis (1 TB per month included for the first year). <br /> | 
| **Performance** | Choose from 2 to 64 vCPUs (1 to 32 cores) and 512 MiB to 256 GiB memory for general-purpose instances, up to 72 vCPUs with compute-optimized instances, and up to 512 GB of memory with memory-optimized instances.<br /> | Unlimited scaling from a single shared to hundreds of CPU cores, and 1 to 1000s of GiB memory.<br /> | Unlimited scaling from a single shared to hundreds of CPU cores, and 1 to 1000s of GiB memory.<br /> | 
| **Pricing** | Fixed and predictable monthly pricing. | There is no additional charge for AWS Elastic Beanstalk. You pay for AWS resources (e.g. Amazon EC2 instances or Amazon S3 buckets) you create to store and run your application.  | Flexible pay-per-use hourly, or commit-based pricing.<br /> | 

### Details on the differences
<a name="lse-differences"></a>

Explore differences between Lightsail, AWS Elastic Beanstalk, and Amazon EC2 in six areas. These cover ease of use, compute and block storage, container deployments, load balancing, content delivery network, and managed database support. 

------
#### [ Ease of use ]

**Ease of use**

Lightsail offers a set of core services to deploy web servers and database backed applications, with support for load balancing, containers, content delivery network (CDN), DNS management, and domain registration. You can also choose from a set of application blueprints to deploy standard applications such as a WordPress site, or LAMP stack application. Lightsail is a good fit for organizations with simple website and application requirements, and those who prefer fixed, predictable monthly pricing.

 Elastic Beanstalk, on the other hand, is a more flexible service for deploying and scaling web applications. It supports multiple programming languages and web servers, automatically handles capacity provisioning, load balancing, auto-scaling, and application health monitoring. Elastic Beanstalk integrates seamlessly with other AWS services like RDS and CloudWatch, allowing for more complex architectures and fine-grained control over the underlying resources. To help you troubleshoot faster, Elastic Beanstalk also offers AI-powered environment analysis, using Amazon Bedrock, to interpret environment health and logs. This analysis is available in the console and through the EB CLI. 

With Amazon EC2, you have greater flexibility to configure workloads over a broader set of compute capacities, features, and integrations with other AWS services. Amazon EC2 provides more flexible purchase options including on-demand hourly and lower commit-based pricing. A typical deployment of Amazon EC2 may require the use of other AWS services, such as databases and load balancers, that each have their own pricing models and configuration details. 



------
#### [ Compute and block storage ]

**Compute and block storage**

Lightsail provides multiple options for your instance size, ranging from 2 vCPUs, 512 MiB memory, and 20 GB of SSD storage, up to 64 vCPUs, 256 GiB of memory, and 1280 GB of SSD storage. Lightsail also offers compute-optimized instances with up to 72 vCPUs, and memory-optimized instances with up to 512 GB of memory. Lightsail compute instances also include a generous free data transfer allocation, and are billed with fixed, predictable pricing. 

Elastic Beanstalk and Amazon EC2 support hundreds of instance types supporting any workload, with 1 to 100s of vCPUs, and 1000s of GiB RAM. Multiple individually sized storage volumes can be attached to Elastic Beanstalk and Amazon EC2 instances with various performance tiers. Elastic Beanstalk and Amazon EC2 both support Spot Instances and Graviton-based instances. These include Graviton4 families such as C8gd, M8gd, and R8gd, along with network-optimized C8gn and R8gn variants that provide up to 600 Gbps of network bandwidth. Graviton4-based instances provide up to 30 percent higher compute performance than Graviton3-based instances. 



------
#### [ Container deployments ]

**Container deployments**

Lightsail containers provide a straightforward way to get started deploying public container images on AWS compute instances, with 0.25 vCPUs and 512 MiB RAM, to 4 vCPUs and 8 GiB RAM. Every Lightsail container deployment comes with 500 GB of data transfer for a fixed monthly fee. 

Elastic Beanstalk can run individual Docker containers, multiple containers with Docker Compose, or deploy to Amazon ECS, a fully managed container orchestration service which manages and scales the Amazon EC2 instances running containers. With Cluster Mode, Elastic Beanstalk runs your application as containers on an Amazon EKS cluster that it creates and operates. You provide a container image, or source code that Elastic Beanstalk builds into an image. Elastic Beanstalk then provisions the cluster, deploys your application, and applies rolling updates. It also scales the number of running replicas and reports environment health. Multiple applications can share pooled infrastructure in your account, which can lower per-application compute cost as your applications scale. Cluster Mode uses Amazon EKS Auto Mode for node capacity and is available in all commercial AWS Regions where Elastic Beanstalk is available.

Containers can be self-managed on Amazon EC2, or deployed to a fully managed AWS container service such as Amazon ECS, Amazon EKS, Elastic Beanstalk, and Lambda. These services support both public and private images, more flexible hourly or commit-based billing, and greater vertical and horizontal scaling capabilities. As of April 30, 2026, AWS App Runner no longer accepts new customers; existing services continue to run. 

Amazon ECS includes ECS Express Mode, a simplified path to deploy a container from an image, with AWS Fargate compute, an HTTPS endpoint, an Application Load Balancer, automatic scaling, and monitoring. Amazon EKS includes EKS Auto Mode, which manages the compute, storage, and networking for a Kubernetes cluster and supports Linux nodes only. 



------
#### [ Load balancing ]

**Load balancing**

Lightsail provides a simple HTTP or HTTPS load balancer for low volume web traffic (up to 5 GB and 400k connections per hour). Lightsail load balancers handle certificate management and are available for a fixed monthly cost. 

 You can [enable load balancing](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-types.html#using-features.managing.changetype) for your Elastic Beanstalk environment, which will create an [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/) load balancer dedicated to your environment. Elastic Beanstalk fully manages this load balancer, taking care of security settings and of terminating the load balancer when you terminate your environment. 

 Alternatively, you can choose to share a load balancer across several Elastic Beanstalk environments. With a shared load balancer, you save on operational cost by avoiding a dedicated load balancer for each environment. Elastic Beanstalk supports the Classic Load Balancer, the Application Load Balancer, and the Network Application Load Balancer types. 

Amazon EC2 Elastic Load Balancing (ELB) offers a broader and more scalable range of load balancer options using more flexible on demand or commit pricing. Amazon EC2 load balancers support both application (HTTP, HTTPS, WebSockets) and network (TCP, UDP) traffic. 



------
#### [ Content delivery network ]

**Content delivery network**

To improve web content load time, Lightsail lets you add a content delivery network (CDN) distribution to your website or application. Lightsail CDN distributions are available in three monthly data transfer tiers, including 50 GB included for the first year, 200 GB, and 500 GB, for a fixed monthly price. 

After you have created and deployed your Elastic Beanstalk application you can sign up for CloudFront and start using CloudFront to distribute your content.

Amazon EC2 and Elastic Load Balancing work directly with the Amazon CloudFront CDN (the same CDN used by Lightsail). Using CloudFront directly offers more integration possibilities with other AWS services or external origins. It also offers more flexible on demand and commit-based pricing than Lightsail. 



------
#### [ Managed database support ]

**Managed database support**

Lightsail offers managed databases in six standard, and six high availability configurations, ranging from 1 to 4 processor cores, 1 GiB to 32 GiB RAM, and 40 GB to 960 GB storage. Lightsail databases are billed using a fixed, predictable monthly price. 

Elastic Beanstalk provides integration with [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/). You can use Elastic Beanstalk to add a MySQL, PostgreSQL, Oracle, or SQL Server database to an existing environment or a new one when you create it. When you add a database instance, Elastic Beanstalk provides the connection information to your application. It does this by setting the environment properties for the database hostname, port, user name, password, and database name. You can also connect to an external database managed outside of Elastic Beanstalk which allows you to use database types that aren't supported with integrated databases. This option will require additional security group and connection string configuration.

Amazon EC2 works directly with Amazon RDS and NoSQL services, such as Amazon DynamoDB. Amazon RDS offers a more scalable and broader range of configurations, including fixed instance types ranging from 2 to dozens of vCPUs, and 100s of GiB RAM, unlimited storage, and seamlessly scalable serverless options. 



------

 Here's a decision table comparing **Amazon Lightsail, AWS Elastic Beanstalk, and Amazon EC2** based on key decision factors: 


|   **Criteria**   |  **Amazon Lightsail**  |  **AWS Elastic Beanstalk**  |  **Amazon EC2**  | 
| --- | --- | --- | --- | 
|  Best For  |  Simple deployments with fixed, predictable pricing  |  Web applications with automated deployment  |  Full control over infrastructure  | 
|  Ease of Use  |  Very easy, simplified UI, preconfigured instances  |  Easy, managed deployment with minimal setup  |  Complex, requires manual setup and management  | 
|  Scalability  |  Simplified scaling options across a range of instance sizes  |  Supports auto scaling. Cluster Mode adds event-driven autoscaling on shared infrastructure.  |  Fully customizable auto-scaling  | 
|  Customization  |  Limited configuration options  |  Moderate customization with platform choices  |  Full control over OS, networking, and resources  | 
|  Pricing  |  Fixed pricing, budget-friendly  |  No additional charge for Elastic Beanstalk. You pay for the underlying resources (for example, Amazon EC2, Amazon EKS, and CloudWatch).  |  Pay-as-you-go, can be expensive if mismanaged  | 
|  Performance  |  Best for low to medium workloads  |  Beanstalk Standard runs on Amazon EC2 instances. Beanstalk Cluster runs multiple applications on shared Amazon EKS infrastructure.  |  Best for high-performance and compute-intensive workloads  | 
|  Management  |  Fully managed, minimal maintenance  |  You manage your application. Elastic Beanstalk manages infrastructure, observability, and monitoring.  |  Fully self-managed, requires expertise  | 
|  Supported Languages  |  Limited, works best with common stacks (LAMP, Node.js, etc.)  |  Supports multiple runtimes (Node.js, Python, Java, .NET, and more) on Linux and Windows Server, with support for custom AMIs. Cluster Mode can also build applications into container images from your source code, or run a container image that you provide.  |  Any OS and runtime supported  | 
|  Integration  |  Limited integrations with AWS services  |  Integrates with AWS services including Amazon RDS, Amazon S3, CloudWatch, AWS Secrets Manager, and AWS Certificate Manager.  |  Full AWS integration  | 
|  Security  |  Basic security features, simpler to manage  |  Automated security updates, but still needs monitoring  |  Full control over security settings  | 
|  Use Case Examples  |  Personal blogs, small websites, MVPs, prototyping  |  Web applications, APIs, SaaS platforms  |  Large-scale applications, databases, custom networking  | 

 **Decision Guidelines:** 
+  Choose **Lightsail** if you want a simple, budget-friendly solution with minimal setup. 
+  Choose **Elastic Beanstalk** if you want to focus on your application while AWS manages infrastructure, observability, monitoring, and security patches. 
+  Choose **EC2** if you need full control over your infrastructure, high performance, or custom configurations. 

### Use
<a name="use"></a>

Now that you’ve learned about what these services (and the supporting AWS tools and services) are optimized for, you can now dive deeper into how best to use them. 

------
#### [ Amazon Lightsail ]
+ **What is Amazon Lightsail?** 

  Get the full story on Amazon Lightsail, including what it does, and how you can benefit from it. This guide also includes step-by-step guidance to help you get started using Lightsail — and then configure it to meet your needs. 

  [Explore the guide](https://docs.aws.amazon.com/lightsail/latest/userguide/what-is-amazon-lightsail.html) 

  
+ **Creating Lightsail container service images** 

  Learn how to create a container image on your local machine using a Dockerfile. You can then push it to your Lightsail container service to deploy it. 

  [Use the tutorial](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images.html) 

  
+ **Amazon Lightsail resource center** 

  Explore Lightsail tutorials, videos, and links to core concept documentation. 

  [Visit the resource center](https://aws.amazon.com/lightsail/resources/) 

  

------
#### [ Elastic Beanstalk ]
+ **What is Elastic Beanstalk?** 

  Get an overview of AWS Elastic Beanstalk. This guide not only provides an introduction of the service, but also covers how to get started using it and then provides in-depth descriptions of key features and how to use them. 

  [Explore the guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) 

  
+ **Getting started with Elastic Beanstalk** 

  To help you understand how AWS Elastic Beanstalk works, this tutorial walks you through creating, exploring, updating, and deleting an Elastic Beanstalk application. It takes less than an hour to complete. 

  [Use the tutorial](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html) 

  
+ **Set up the Elastic Beanstalk command line interface** 

  In this step-by-step tutorial, you will set up the Elastic Beanstalk Command Line Interface (EB CLI).

  [Use the tutorial](https://aws.amazon.com/getting-started/hands-on/set-up-command-line-elastic-beanstalk/) 

  

------
#### [ Amazon EC2 ]
+ **What is Amazon EC2?** 

  Get an overview of Amazon EC2. This guide not only provides an introduction of the service, but also covers how to get started using it and then provides in-depth descriptions of key features and how to use them. 

  [Explore the guide](https://docs.aws.amazon.com/ec2/index.html) 

  
+ **Amazon EC2 instance types** 

  When you launch an EC2 instance, the instance type that you specify determines the hardware of the host computer used for your instance. Each instance type offers different compute, memory, and storage capabilities, and is grouped in an instance family based on these capabilities. This guide walks you through EC2 instance types. 

  [Explore the guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) 

  
+ **Amazon EC2 Auto Scaling with EC2 Spot Instances** 

  Learn how to create a stateless, fault tolerant workload using Amazon EC2 Auto Scaling with launch templates to request Amazon EC2 Spot Instances. 

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/ec2-auto-scaling-spot-instances/) 

  

------

## Choosing a modern application strategy
<a name="modern-apps-strategy-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which modern application development approach is the best fit for your organization. | 
| **Last updated** | May 16, 2025 | 
| **Covered services** |  +  [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html) <br />+  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) <br />+  [AWS App Runner](https://docs.aws.amazon.com/apprunner/) <br />+  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html) <br />+  [Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)   | 

### Introduction
<a name="intro"></a>

Amazon Web Services (AWS) provides you with the flexibility to choose different compute options to build and run modern applications that map to your business needs. We provide you with access to the right operational model for your compute choice.

Developers and data engineers prefer a level of autonomy when choosing which compute models match which workloads. When initially developing modern applications, development teams need to manage and operate their applications directly.

As more workloads are developed, you might decide to create central platform or operations teams. The function of these central teams varies—some provide standard architectures and templated patterns for development teams to use, and others operate and manage workloads on behalf of multiple development teams. 

These central teams strive to create standards for controlling costs, achieving the right performance and security, simplifying operations, and providing common architecture patterns. Achieving the right balance between autonomy and standardization is a challenge that enterprises and other large organizations often deal with. 

It is common to choose one of two operational models to meet this challenge: [serverless compute](https://aws.amazon.com/serverless/) or [Kubernetes](https://aws.amazon.com/kubernetes/). 

[![AWS Videos](https://img.youtube.com/vi/OJD3UMuU8Zk/0.jpg)](https://www.youtube.com/watch?v=OJD3UMuU8Zk)


### Understand
<a name="understand"></a>

Developers and data engineers might have different compute requirements. For example, a developer might choose AWS Lambda because it is optimized for event-driven patterns and gives access to hundreds of managed integrations.

Alternatively, a data engineer might choose an open-source framework like KubeFlow or Ray on [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) (Amazon EKS) because it simplifies deployment of machine-learning models but allows access to the right high-powered instances.

[![AWS Videos](https://img.youtube.com/vi/1hN9SuRsnNQ/0.jpg)](https://www.youtube.com/watch?v=1hN9SuRsnNQ)


Each role tends to develop skills in technology stacks over time and has preferences about the tools they use. Both developers and data engineers look at their compute choice on a workload-by-workload basis, which means operational roles need to support a variety of workloads since they often work across teams. These roles include platform engineers, cloud administrators, or site reliability engineers (SREs).

Those in operational roles are challenged to provide autonomy for developers and data engineers while making sure they can deploy, operate, and monitor all workloads consistently to meet security, performance, resiliency, and cost requirements. Over time, as you develop more modern applications, these roles need to standardize on the tools to automate the deployment and monitoring of their workloads.

![Diagram showing the operational models for modular architecture patterns.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/operational-models-for-modular-architecture.png)


The choice between serverless compute and Kubernetes as an operational model is often driven by the need to have the right balance between autonomy and standardization with the number of resources one dedicates to running and operating workloads. Many workloads can be built successfully using either of these options. But, for some workloads, there are inherent advantages of one over the other.

A good team can make the compute choice entirely transparent to developers. Poor choices can limit developers' options, and lead to sub-standard outcomes. Operators are always affected by the selected operating model and it will determine needs such as common libraries and networking configuration—as well as how the organization will interact with underlying services it needs to configure.

The operational model will often be determined by your organizational structure and skill around automation and operations. These roles might be distributed across development teams, different parts of your organization, or be centralized. The structure and skills of these teams are often among the most important considerations when choosing between a serverless or Kubernetes operational model. 

The serverless operational model prioritizes shifting much of the work involved in provisioning and managing compute resources to AWS. This model includes services such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and the [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

The second model, Kubernetes on AWS, meets an important need for organizations that prioritize the [Cloud Native Computing Foundation (CNCF) ecosystem](https://www.cncf.io/) with a managed experience using [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html). 

### Consider
<a name="consider"></a>

For developers and data engineers, we recommend that you evaluate the most appropriate compute option on a workload-by-workload basis within your operational strategy. Here are some of the key criteria to consider when determining your strategy.

------
#### [ Organizational structure and skill ]

Enterprises tend to organize their development teams around one of the following models:
+ **Distributed:** Each team owns their development, deployment, and operational functions. This model provides a great level of autonomy and allow teams to innovate at their own pace.
+ **Centralized:** A centralized team maintains standards, creates automations, and facilitates the sharing of knowledge and best practices.

These are separate ends of a spectrum, and organizations can start with a distributed model and later migrate towards a centralized model as the number of workloads increases and the need for consistency across cost, performance and security of workloads becomes an important factor. However, in both models, serverless can reduce the infrastructure management overhead.

Another model organizations adopt, especially in the Kubernetes space, are the formation of central teams that specialize in platform engineering. These skilled engineering teams have developer skills and build and maintain platforms made up of common automation, deployment, and observability tools. Amazon EKS is often the choice for these organizations.

Identifying the structure and skill of your development teams can be critical to choosing the appropriate platform.

------
#### [ Operational model ]

Organizations standardize on automation technologies to take full benefit of the cloud. The strategy and tools used by infrastructure, platform, and DevOps teams often drives decisions.

For example, organizations have choices for tooling that automates the creation, configuration, and maintenance of infrastructure, resources, and workloads. These tools include infrastructure as code (IaC) tools such as Terraform, AWS CDK, CloudFormation, and other community tools. 

Organizations that use Kubernetes might use Kubernetes-based tools for automation using GitOps tools such as ArgoCD, and Kubernetes API-based cloud provisioning tools like [AWS Controllers for Kubernetes (ACK)](https://github.com/aws-controllers-k8s/community), [Kube Resource Controller (kro)](https://github.com/kro-run/kro), or the [CNCF Crossplane project](https://www.cncf.io/projects/crossplane/).

These tooling choices extend to tools that extend to security, testing, networking, observability, performance, and more. For each of these categories, there is a stack of available tools.

These automation tools often have built in integrations and accelerators for compute choices. For example, AWS Serverless Application Model (AWS SAM) is optimized for serverless developers to build and quickly deploy Lambda functions. Other tools, such as ArgoCD, automate the deployment and configuration of Kubernetes workloads.

As customers increase workloads, it can be a burden to support a large number of tooling choices. We recommend standardizing a set that support the most workload patterns.

------
#### [ Workload characteristics ]

It is important to evaluate the most appropriate compute option on a workload-by-workload basis within the default strategy. You should always strive to achieve the desired performance, security, and cost benefit for each workload.

A good standardization strategy will allow for different use cases such as microservices, modernized monoliths, event driven architectures, tools built by operation teams, and data processing workloads, such as machine learning, batch processing, and stream processing.

These workloads have different architectural characteristics. The strategy adopted should allow flexibility to support all the stages of a developer or data scientist workflow.
+ **Application developer:** Needs to run multiple environments such as development, prototyping, test, staging, and production.
+ **Data engineer:** These workflows involve streaming and acting on large data models, cleaning, training, running inference with models, and building applications and data pipelines that experiment with the data, including Jupyter Notebooks.
+ **AI/ML scientist:** Generative Artificial Intelligence (AI) Large Language Models (LLM) might require specialized compute instances such as AWS Trainium or other GPU-based architecture.

------
#### [ Integrations ]

Applications do not exist in isolation. They are supported by technologies such as databases, messaging, streaming, orchestration, and other services. An effective modern app development strategy requires integration with these services. Managed integrations simplify operational overhead as much as management of the underlying infrastructure.

AWS [serverless compute options](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html), such as AWS Lambda, are integrated into the AWS ecosystem. Lambda can subscribe to events from more than 250 other services.

AWS-managed offerings for Kubernetes also provide integrations with many AWS managed offerings. For example, you can use AWS Controllers for Kubernetes to provision native AWS resources using a Kubernetes API. In addition, Kubernetes has a rich ecosystem, offering integration with numerous open-source projects. Amazon EKS works [with many other AWS services](https://docs.aws.amazon.com/eks/latest/userguide/eks-integrations.html) to provide additional solutions for business challenges.

------
#### [ Prototyping ]

Many organizations need to create experiments to validate ideas. The ability to provide an environment where you can quickly write, deploy, and validate ideas is essential for a healthy environment.

This environment is often overlooked when developing a modern app development strategy, but the ability to innovate can depend on it. Enabling teams to use services that allow builders to rapidly build, test, and iterate help in discovering new business opportunities and receive feedback faster.

Serverless compute options like AWS Lambda and AWS App Runner are optimized to enable organizations write code quickly, deploy it, and change it. These capabilities provide useful options for doing fast prototyping work that doesn’t require making a lot of choices upfront. Developers can quickly turn an idea into a modern, working application. The [AWS serverless compute option](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html) provides choices to prototype with minimal cost or operational overhead.

Other options can be used for prototyping: for Amazon ECS, you can create dedicated clusters and use AWS Fargate or dedicated nodes for prototyping, for Kubernetes, platform teams can create dedicated clusters or have namespaces within a cluster dedicated to prototyping teams. Open source projects such as [CNCF BuildPacks](https://buildpacks.io/) or [Knative](https://knative.dev/docs/) can be used to simplify the configuration experience.

------

### Choose
<a name="choose"></a>

AWS offers different container options, such as Amazon ECS, serverless containers with AWS Fargate, and AWS App Runner, and different Kubernetes options, such as Amazon EKS, ROSA, and self-managed Kubernetes on Amazon EC2.

The following comparison table can help you determine your approach based on your workload requirements. You might choose pieces of both approaches, or have different teams that use different approaches. It is not uncommon to see very large organizations have departments with different strategies. 



| Modern application approach | When would you use it? | What workload is it optimized for? | Serverless services | 
| --- |--- |--- |--- |
| Serverless | Use when AWS managed services and tools are your first choice, such as AWS Lambda, AWS App Runner, and Amazon ECS. | Optimized for enabling developers to focus solely on writing code without the need to manage or provision servers, minimizing operational overhead. | [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)<br />[AWS App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html)<br />[AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)<br />[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) | 
|  Kubernetes  |  Use when Kubernetes is your primary compute platform interface.  |  Optimized for teams with central platforms teams that invest in platform engineering skills. Platform engineers are skilled at keeping clusters up to date with the fast-moving CNCF Kubernetes versioning strategy.  |  [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) [Red Hat OpenShift Service on AWS (ROSA)](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html)  | 
| --- |--- |--- |--- |

### Use
<a name="use"></a>

Now that you have determined which approach best fits your workload for your environment, we recommend that you review the following service-specific resources to help you begin implementing your approach. This includes links to in-depth documentation, hands-on tutorials, and other key assets to help get you started.

------
#### [ Amazon ECS ]
+ **Getting started with Amazon ECS**

  We provide an introduction to the tools available to access Amazon ECS and introductory step-by-step procedures to run containers.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)
+ **Tutorials for Amazon ECS**

  Explore more than a dozen tutorials on how to perform common tasks—including the creation of clusters and VPCs.

  [Get started with the tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)
+ **Containers on AWS**

  Learn about containers on AWS through blog posts, code patterns, and visuals.

  [Explore the site](https://containersonaws.com/)
+ **Amazon ECS deployment**

  This guide offers an overview of Amazon ECS deployment options on AWS and shows how it can be used to manage a simple containerized application.

  [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-container-service.html)
+ **Amazon ECS Immersion Day**

  This workshop expands on your foundational understanding of containers and provides practical experience scaling, monitoring, and managing container workflows using Amazon ECS and AWS Fargate.

  [Explore the workshop](https://catalog.workshops.aws/ecs-immersion-day/en-US)

------
#### [ AWS App Runner ]
+ **Getting started with AWS App Runner**

  Learn how to configure the source code and deployment, service build, and service runtime to deploy your application to App Runner.

  [Get started with the tutorial](https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html)
+ **AWS App Runner: From code to a scalable, secure web application in minutes**

  Explore how AWS App Runner was designed to make it easier for you to deploy web apps and APIs to the cloud, regardless of the language they are written in, even for teams that lack prior experience deploying and managing containers or infrastructure.

  [Read the blog](https://aws.amazon.com/blogs/aws/app-runner-from-code-to-scalable-secure-web-apps/)
+ **Deploy a web app using AWS App Runner**

  Learn how to deploy a containerized web app using AWS App Runner. Start with your source code or a container image. App Runner automatically builds and deploys the web application and load balances traffic with encryption.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/guides/deploy-webapp-apprunner/)

------
#### [ AWS Fargate ]
+ **Getting started with AWS Fargate**

  Understand the basics of AWS Fargate, a technology that you can use with Amazon ECS to run containers without having to manage servers or clusters of EC2 instances.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
+ **Getting started with the console using Linux containers on AWS Fargate**

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your tasks in the Regions where Amazon ECS supports AWS Fargate.

  [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/getting-started-fargate.html)

------
#### [ AWS Lambda ]
+ **What is AWS Lambda**

  Learn more about AWS Lambda, a compute service that lets you run code without provisioning or managing servers.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ **Using AWS Lambda with other services**

  Explore common use cases, learn how invocation works and includes a table that covers the services that work with Lambda and how it can be invoked from that service.

  [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
+ **Serverless Land**

  Get the latest information, blogs, videos, code, and resources for AWS serverless.

  [Explore the site](https://serverlessland.com/)
+ **Guide to AWS Lambda Pricing**

  Explore and understand AWS Lambda pricing. You are charged based on the number of requests for your functions and the duration it takes for your code to start.

  [Explore the guide](https://aws.amazon.com/lambda/pricing/)

------
#### [ Amazon EKS ]
+ **Getting started with Amazon EKS**

  Learn more about Amazon EKS, a managed service that you can use to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane or nodes.

  [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
+ **Amazon EKS deployment**

  Explore Amazon EKS deployment options on AWS and learn how it can be used to manage a general containerized application. 

  [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/amazon-elastic-kubernetes-service.html)
+ **Deploy a Kubernetes application on Linux**

  Learn how to deploy a containerized application to a Kubernetes cluster managed by Amazon EKS on Linux nodes.

  [Get started with the tutorial](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html)
+ **Deploy a Kubernetes application on Windows**

  Learn how to deploy a containerized application onto a Kubernetes cluster managed by Amazon EKS on Windows nodes.

  [Get started with the tutorial](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment-win.html)
+ **Amazon EKS workshop**

  Explore practical exercises to learn about Amazon EKS.

  [Visit the workshop](https://www.eksworkshop.com/)
+ **Streamline Kubernetes cluster management with Amazon EKS Auto Mode**

  Learn how you can automate cluster management without deep Kubernetes expertise using Amazon EKS Auto Mode.

  [Read the blog](https://aws.amazon.com/blogs/aws/streamline-kubernetes-cluster-management-with-new-amazon-eks-auto-mode/)
+ **Use your on-premises infrastructure in Amazon EKS clusters with Amazon EKS Hybrid Nodes**

  With Amazon EKS Hybrid Nodes, you can unify Kubernetes management across your cloud and on-premises environments, and take advantage of the scale and availability of Amazon EKS in all the places your applications need to run. 

  [Read the blog](https://aws.amazon.com/blogs/aws/use-your-on-premises-infrastructure-in-amazon-eks-clusters-with-amazon-eks-hybrid-nodes/)

------
#### [ ROSA ]
+ **Getting started with Red Hat OpenShift Service on AWS**

  Learn how to get started using Red Hat OpenShift Service on AWS

  [Explore the guide](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html)
+ **Why would you use ROSA?**

  Learn when you might use Red Hat OpenShift over standard Kubernetes and explores ROSA on AWS in depth.

  [Watch the video](https://pages.awscloud.com/apn-tv-596.html)

------

### Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you implement your modern app development approach.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&amp;cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless%7Ctech-category%23containers&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=1)
+ **Whitepapers**

  Explore whitepapers to learn best practices in implementing your modern app development approach.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=2)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common modern app development use cases.

  [Explore solutions](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23modern-applications%7Ctech-category%23serverless%7Ctech-category%23containers&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=1)

## Choosing a purchasing option for Amazon EC2
<a name="ec2-purchasing-options-aws-how-to-choose"></a>


|  |  | 
| --- |--- |
| **Purpose** | Help determine which [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) purchasing option is the best fit for your budget and business needs. | 
| **Last updated** | June 22, 2026 | 
| **Audience** | Cloud architects, engineers, and finance teams evaluating EC2 cost optimization strategies. | 
| **Covered purchasing options** |  +  [EC2 On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html) <br />+  [EC2 Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br />+  [EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) <br />+  [EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)   | 

### Introduction
<a name="ec2-po-introduction"></a>

[Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) offers scalable computing capacity in the AWS Cloud that enables you to develop and deploy applications faster without upfront hardware investments. As a cornerstone of the AWS cloud computing platform, Amazon EC2 offers the flexibility to launch any number of virtual servers, configure security and networking, manage storage, and scale resources up or down based on changing demand.

To accommodate diverse workloads, we offer multiple Amazon EC2 purchasing options spanning different operational requirements and preferences. When considering purchasing options for Amazon EC2, you must weigh several factors, including budget, demand and workload patterns, term commitment flexibility, and configuration conditions, such as Region requirements. Each purchasing option helps you optimize costs, performance, and operational efficiency based on specific use cases and instance needs.

In this guide, we explain the available Amazon EC2 purchasing options, walk through the key factors to consider when choosing between them, and provide resources to help you get started with your selected approach.

### Understanding Amazon EC2 purchase offerings
<a name="ec2-po-understand"></a>

Amazon EC2 offers multiple purchasing options so you can balance cost, commitment, and flexibility for each workload. Some options trade upfront commitment for deeper discounts, while others preserve flexibility at a higher rate. Combining them strategically across your portfolio reduces overall spend without compromising performance or availability. The following sections describe each option.

Before you continue, note that two concepts are often confused but are independent. Purchasing options (On-Demand, Savings Plans, Reserved Instances, Spot) determine how AWS calculates your bill for the compute you use. Capacity Reservations (On-Demand Capacity Reservations and Capacity Blocks for ML) determine whether capacity is held for you when you need it, regardless of whether you use it. These two dimensions are independent, and you commonly layer them: a Capacity Reservation is billed at the equivalent On-Demand rate whether or not you consume the capacity. You can then discount that bill by combining the reservation with Savings Plans or a Regional Reserved Instance. The sections that follow cover purchasing options first, then dedicated hardware, and finally Capacity Reservations as a complementary capacity-availability tool.

------
#### [ Primary purchasing options ]
+ **[On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html)** provide pay-as-you-go pricing with no long-term commitments or upfront payments. They offer maximum flexibility, allowing you to start, stop, and terminate instances at any time while paying only for the compute time you use, with billing granularity as low as per-second for Linux, RHEL, and Windows instances.
+ **[Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/)** are a flexible pricing model that offers significant discounts in exchange for a commitment to a specific amount of compute usage (measured in $/hour) for a one or three-year period. Savings Plans relevant to Amazon EC2 come in two varieties: Compute Savings Plans automatically apply to any Amazon EC2 instance usage regardless of Region, instance family, operating system, or tenancy, and also cover Fargate and Lambda usage. Amazon EC2 Instance Savings Plans apply to a specific instance family within a Region, offering higher discounts in exchange for a more targeted commitment.
**Note**  
There are four Savings Plan types: Compute Savings Plans (up to 66% off), Amazon EC2 Instance Savings Plans (up to 72% off), [Database Savings Plans](https://aws.amazon.com/savingsplans/database-pricing/) (up to 35% off for Amazon RDS, Aurora, DynamoDB, ElastiCache, and more), and [SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/) (up to 64% off). This guide covers only the Savings Plans relevant to Amazon EC2.
+ **[Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)** provide access to interruptible compute capacity based on demand at up to 90% discount. This capacity is made available by Amazon EC2 and can be reclaimed by AWS when necessary. Spot Instances are ideal for fault-tolerant, flexible workloads such as batch processing, data analytics, CI/CD pipelines, and stateless web servers. They work best when your applications can handle potential interruptions or when used with services that can automatically request replacement capacity. As a general guideline, Spot Instances are best suited for flexible workloads with variable demand that can tolerate interruptions, whereas Savings Plans are a better fit for steady-state workloads with predictable, consistent usage patterns where uninterrupted availability is required. Spot Instance pricing is independent of Savings Plans - Savings Plans discounts do not apply to Spot Instance usage.
+ **[Reserved Instances (RIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)** are an older purchasing option that we generally recommend replacing with Savings Plans, and newer Amazon EC2 instance families might not support Reserved Instance pricing. The set of services where RIs remain the only commitment-based discount has narrowed sharply: most database and analytics services are now covered by Database Savings Plans (Amazon RDS, Aurora, ElastiCache, DynamoDB, DocumentDB, Neptune, Keyspaces, Timestream, DMS, and OpenSearch, up to 35% off). Redshift uses its own commitment models rather than Savings Plans: Reserved Nodes for provisioned clusters (up to 75% off) and Serverless Reservations for Redshift Serverless (up to 45% off). For most workloads, Savings Plans (or the relevant service-specific reservation) are now the default.

------
#### [ Dedicated hardware ]

If you have compliance, regulatory, or operational requirements that require your instances to run on Amazon EC2 hardware dedicated to you, two options are available:
+ **[Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html)** provide physical Amazon EC2 servers dedicated exclusively to your use. They offer visibility into the underlying server's physical cores and sockets, enabling you to deploy your instances on specific servers and maintain them there over time. Dedicated Hosts can help meet compliance requirements that might necessitate physical server isolation and provide more predictable performance. This option is particularly valuable for bringing your own existing server-bound software licenses (such as Windows Server, SQL Server, or SUSE Linux Enterprise Server) that are licensed per core or per socket, allowing you to reduce costs by avoiding the license fees normally included in standard Amazon EC2 pricing. Dedicated Hosts are priced per physical host rather than per instance, so cost efficiency depends on how fully you utilize the available instance capacity on each host.
+ **[Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)** run on hardware dedicated to a single AWS account but differ from Dedicated Hosts in that they do not provide visibility or control over instance placement. They offer physical isolation at the host hardware level from instances belonging to other AWS accounts, making them suitable for workloads with regulatory or compliance requirements that mandate tenant isolation.

Dedicated hardware pricing options include On-Demand rates, Dedicated Host Reservations, and coverage by Savings Plans. For more information, refer to the [Amazon EC2 pricing page](https://aws.amazon.com/ec2/pricing/).

------
#### [ Capacity Reservations ]

Capacity Reservations allow you to reserve compute capacity in specific Availability Zones for any duration without making long-term commitments. You can create a Capacity Reservation at any time, and you can choose whether it starts immediately or at a future date. There are two types:
+ **[On-Demand Capacity Reservations (ODCR)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html)** provide flexibility for workloads that have strict capacity requirements, such as business-critical events, high-availability requirements, regulatory compliance, or disaster recovery scenarios. They can be created and canceled as needed. Capacity Reservations can be configured along two dimensions:

  **By access scope:**
  + **Open Capacity Reservations:** Any running instance within the owning account that matches the reservation attributes, such as instance type, platform, and Availability Zone, automatically uses the reserved capacity without needing to explicitly target the reservation. To share an Open Capacity Reservation with other accounts in your organization, use AWS Resource Access Manager (RAM).
  + **Targeted Capacity Reservations:** Only instances that have matching attributes (instance type, platform, Availability Zone, and tenancy) and that explicitly target the reservation can use the reserved capacity, providing more granular control over capacity allocation.

  **By start time:**
  + **Immediate Capacity Reservations:** Start within minutes upon creation and reserve capacity right away, ensuring instant availability for your workloads.
  + **Future-dated Capacity Reservations:** Start at a specified future date and time, with a required commitment duration, allowing you to plan and reserve capacity in advance for scheduled events or anticipated demand spikes. The minimum commitment duration is 14 days.

  Capacity Reservations are priced at the equivalent On-Demand rate regardless of whether the reserved capacity is used, and can be combined with Savings Plans or Regional Reserved Instances to reduce costs.
+ **[Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html)** enable you to reserve GPU and accelerated instances for specific time windows, particularly valuable for ML workloads with predictable scheduling needs. Capacity Blocks can be reserved for durations ranging from 1 to 182 days, with the option to start within minutes from purchase or at a scheduled future date. This option is ideal for model training, fine-tuning, experimentation, and handling temporary inference demand spikes. Capacity Blocks are priced based on supply and demand trends, with rates updated periodically, and the reservation fee is charged upfront at the time of purchase. Pricing is not a discount mechanism: rates can be at, above, or below On-Demand depending on instance family, region, and demand, and for popular GPU instances Capacity Blocks often carry a premium over On-Demand as the price of assured availability. Unlike On-Demand Capacity Reservations, Capacity Block pricing cannot be combined with Savings Plans or Reserved Instance discounts.

------

### Consider
<a name="ec2-po-consider"></a>

**Tip**  
If you are new to Amazon EC2 or are not sure about your usage patterns, consider starting with On-Demand Instances and using tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) and [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to monitor and analyze your usage before committing to a specific purchasing option. For more information, see the [AWS Cost Optimization documentation](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/) and [Tips for Right Sizing](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/tips-for-right-sizing-your-workloads.html).

When selecting Amazon EC2 purchasing options, evaluate these key factors:

------
#### [ Commitment or term ]

Think of Amazon EC2 purchasing options as existing on a spectrum from pay-as-you-go flexibility to longer-term commitments of up to three years, with increasing cost savings as the commitment duration grows:
+ **No commitment with On-Demand or Spot:** Pay-as-you-go pricing with no term and no upfront payment.
  + On-Demand suits uncertain, temporary, or variable needs that require uninterrupted capacity.
  + Spot offers up to 90% off the same zero-commitment model, in exchange for interruptibility. Best suited to fault-tolerant, scalable, or bursty workloads that can resume elsewhere when capacity is reclaimed.
+ **Flexible commitment with Compute Savings Plans:** Commit to a specific hourly spend (in USD/hour) for a 1- or 3-year term for up to 66% off. The commitment applies flexibly across instance families, Regions, operating systems, and tenancy, and also covers Fargate and Lambda.
+ **Targeted commitment with Amazon EC2 Instance Savings Plans:** Commit to a specific hourly spend on a chosen instance family within a Region for up to 72% off. Deeper discount than Compute Savings Plans, in exchange for reduced flexibility. Reserved Instances offer a similar trade-off but are a legacy option; consider them only for services not yet covered by any Savings Plan type (such as Redshift Reserved Nodes for provisioned clusters).

**Commitment as strategy**

Commitment decisions do not need to be one-time decisions. Start by analyzing past usage to identify always-on services with stable, predictable baselines. These are strong candidates for Savings Plans coverage today. From there, you can layer additional commitments as new services stabilize, top up coverage as baselines grow, and choose between 1- and 3-year terms based on your confidence in each tranche.

Within each tranche, match the plan type to how stable the workload is. Amazon EC2 Instance Savings Plans offer the deepest discounts when you are confident you will stay on the same instance family and Region for the term. Compute Savings Plans trade some discount for the freedom to shift across instance families, Regions, and even Fargate and Lambda, which is the safer choice when architectural change is likely or when you want to take advantage of newer instance types that typically offer better price/performance over time.

In practice, a single purchasing option is rarely optimal. You can layer them: Savings Plans or other committed options for the predictable baseline, and On-Demand or Spot Instances for variable demand on top. See [Hybrid EC2 purchasing strategy: Accelerating workloads with Spot without risking deadlines](#ec2-po-choose-spot) for how to blend them.

------
#### [ Continuity and demand ]

Understanding how critical a workload is and how its demand varies over time can help determine which purchasing options best serve it.

**Workload criticality**

Match the purchasing option to how critical the workload is:
+ **Mission-critical systems:** For applications where downtime means significant business impact (payment processing, trading platforms, core customer experiences), layer a capacity assurance mechanism on top of your chosen purchasing option. On-Demand Capacity Reservations provide assurance that the required resources are available when needed, and you can combine them with Savings Plans or Regional Reserved Instances to optimize the cost of that reserved capacity.
+ **Important but resilient systems:** For services that matter but have built-in resilience (distributed systems with redundancy), a balanced approach using a mix of Savings Plans and On-Demand provides both cost efficiency and reliability, or Spot Instances where the workload is fault-tolerant.
+ **Background or batch processing:** For workloads that can be delayed or rescheduled without significant impact, Spot Instances offer significant cost savings, as the occasional interruption presents minimal business risk.

**Note**  
Where the workload is fault-tolerant, Spot Instances can further reduce costs.

**Demand patterns**

Your workload's demand pattern can be used to guide your Amazon EC2 purchasing decisions:
+ **Steady-state workloads:** Applications with consistent, predictable usage patterns (databases, core infrastructure) benefit most from long-term commitments through Savings Plans.
+ **Cyclical patterns:** Workloads with predictable but variable patterns (day/night cycles, weekly patterns, seasonal spikes) benefit from a layered approach: Savings Plans for the baseline and On-Demand Capacity Reservations or Capacity Blocks for predictable peaks.
+ **Unpredictable bursts:** Systems with random or unpredictable spikes can benefit from maximum flexibility through On-Demand or Spot capacity.

**Cost of readiness**

Maintaining reserved but unused capacity represents a strategic choice between immediate availability and cost efficiency. Consider not just the direct cost of idle resources, but also the business impact of delayed capacity availability. For mission-critical use cases, reserving capacity through On-Demand Capacity Reservations even when not fully utilized can be the right business decision. To reduce the cost of readiness, combine Capacity Reservations with Savings Plans to apply billing discounts to both used and unused reserved capacity.

------
#### [ Cost considerations ]

Cost considerations for Amazon EC2 extend beyond price comparisons. Understanding the full economic impact of your Amazon EC2 purchasing decisions requires a multidimensional perspective.

**The broader cost equation**

The visible price of an Amazon EC2 instance is just one component of its true cost. When evaluating options, consider the following:
+ **Operational overhead:** Savings Plans offer a straightforward path to cost optimization, discounts apply automatically with minimal ongoing management beyond periodic reviews of your commitment level. Reserved Instances can yield higher savings for specific configurations but require more active management of instance attributes, modifications, and renewals.
+ **Opportunity cost:** Capital committed to upfront payments cannot be invested elsewhere. Consider your cost of capital and alternative uses for those funds when evaluating payment options.
+ **Risk-adjusted cost:** The lowest nominal price is not always the lowest risk-adjusted cost. Spot Instances offer significant savings but introduce operational overhead that could result in increased engineering effort spent building resilience, or costs from service disruptions if not implemented correctly or not applied for the right workload.

When multiple commitment types are active, AWS applies them in a fixed order: Reserved Instances first, then Amazon EC2 Instance Savings Plans, then Compute Savings Plans, which might affect how discounts are allocated across your usage.

**Strategic payment timing**

Payment structure decisions should align with your business's financial strategy:
+ **Maximizing cost efficiency:** If you have available capital and focus on maximum efficiency, you benefit most from All Upfront payments when available, effectively prepaying for compute at the highest discount.
+ **Balanced approach:** Partial Upfront payments offer a middle ground, reducing the monthly commitment while still capturing significant discounts, ideal for most established businesses.
+ **Growth-focused, cash-preserving:** If you prioritize growth and cash flow preservation, you might benefit from No Upfront options, accepting slightly lower discounts to maintain capital flexibility for business expansion.

**Granular efficiency**

Per-second billing fundamentally changes the economics of short-duration workloads. Tasks that run for minutes rather than hours (batch processing, CI/CD pipelines, data transformations) can achieve dramatic cost reductions through precise resource allocation and immediate termination when work completes. This granularity rewards architectural patterns that emphasize rapid startup, efficient processing, and prompt shutdown.

------
#### [ Instance flexibility ]

Instance flexibility represents your ability to adapt to changing requirements, new technologies, and evolving best practices. The value of flexibility varies dramatically based on your pace of change and innovation.

**Flexibility as strategic value**

Flexibility is a strategic asset with tangible business value:
+ **High-innovation environments:** If you are rapidly evolving your architecture, adopting new services, or frequently changing workload characteristics, prioritize flexibility with Compute Savings Plans even at slightly lower discounts in exchange for the ability to adopt new, more efficient instance types or shift workloads between services, which often delivers greater long-term value than maximum short-term discounts.
+ **Stable, mature workloads:** Applications with well-understood, stable requirements can lock in deeper discounts through Amazon EC2 Instance Savings Plans (or Reserved Instances, where applicable), trading scope for savings, since significant changes are unlikely during the commitment period.

**Geographic flexibility**

Geographic flexibility considerations extend beyond simple regional versus zonal decisions:
+ **Discount portability:** Compute Savings Plans apply across all Regions, so the discount follows the workload, whether it rotates between Regions daily (follow-the-sun), fails over for resilience, or shifts geographically over time. Amazon EC2 Instance Savings Plans are scoped to a specific Region, offering higher discounts in exchange for that geographic commitment.
+ **Capacity across Availability Zones:** On-Demand Capacity Reservations are tied to a specific Availability Zone. For multi-AZ architectures or disaster recovery scenarios, consider creating Capacity Reservations across multiple Availability Zones to ensure failover capacity is available when needed.
+ **Data gravity:** Compute resources tend to remain in the same Region as the data they process. Cross-Region egress costs, replication lag, locality requirements (Amazon S3, Amazon RDS, DynamoDB, and other services), and storage lifecycle commitments anchor stateful workloads to a specific Region. For data-heavy workloads, geographic flexibility matters less because the workload is unlikely to move. Stateless or compute-only workloads can shift more freely and benefit more from Region-portable discounts.
+ **Regulatory evolution:** Data residency and compliance requirements continue to evolve globally. If you operate in multiple jurisdictions or face changing regulatory landscapes, you might need the flexibility to relocate workloads to different Regions as requirements change.

**Specialized requirements as constraints**

Workloads pinned to specific hardware (particular CPU architectures, GPUs, accelerators, or memory configurations) have little flexibility to shift across instance families, which actually makes commitment-based discounts attractive: you are not giving up flexibility you would have used. For steady use of a known family in a Region, Amazon EC2 Instance Savings Plans (or Reserved Instances, where applicable) deliver the deepest discount. For instance types where capacity availability is limited and launch failure is unacceptable, layer On-Demand Capacity Reservations on top to reserve capacity, and discount the resulting On-Demand-equivalent charges with Savings Plans or a Regional Reserved Instance. For scheduled GPU or accelerated workloads such as ML training and fine-tuning, Capacity Blocks for ML reserve accelerator capacity for a defined window and bill only for that window.

------
#### [ Usage predictability ]

Usage predictability fundamentally shapes your optimal purchasing strategy. Understanding the patterns, confidence levels, and variability in your workloads enables more strategic decisions about commitments and flexibility.

**Predictability spectrum**

Workloads exist on a predictability spectrum that directly influences optimal purchasing strategies:
+ **Highly predictable workloads:** Core infrastructure, databases, and steady-state applications with consistent, well-understood usage patterns represent ideal candidates for maximum commitment through Savings Plans. The predictability of these workloads transforms what would otherwise be a risk (long-term commitment) into an opportunity for substantial savings.
+ **Seasonally predictable workloads:** Applications with identifiable patterns that vary by time of day, day of week, or season benefit from a layered approach. The predictable baseline is ideal for Savings Plans, while the predictable peaks might leverage On-Demand Capacity Reservations or Capacity Blocks for ML workloads.
+ **Growing but predictable workloads:** For applications with steady growth trajectories, staggered commitments can be effective. Rather than committing to the full capacity at once, implement a rolling commitment strategy where portions of your capacity are committed at different times, creating a ladder effect that accommodates growth while maintaining discounts.
+ **Unpredictable workloads:** Highly variable or unpredictable workloads benefit from maximum flexibility through On-Demand or Spot Instances.

**Architectural adaptability**

The design of your applications significantly impacts your ability to leverage different pricing models:
+ **Stateless versus stateful:** Stateless applications that can easily scale horizontally across diverse instance types enable much greater purchasing flexibility than stateful applications with specific instance requirements.
+ **Resilience patterns:** Applications designed with resilience patterns (circuit breakers, retry mechanisms, graceful degradation) can more effectively utilize Spot Instances, potentially accessing the deepest discounts available.
+ **Resource efficiency:** Applications optimized for efficient resource utilization can often run on smaller or more diverse instance types, increasing flexibility in purchasing options and reducing overall costs. For example, a containerized microservices architecture that right-sizes each service independently can spread workloads across multiple smaller instance types rather than requiring a few large, specialized ones enabling broader use of Spot Instances and Compute Savings Plans.

------
#### [ At-scale patterns ]

At scale, purchasing decisions are not based on a single workload. Instead, you must consider the combined requirements of multiple workloads distributed across different AWS accounts, Regions, and time zones. Patterns emerge at scale that create unique optimization opportunities:
+ **Portfolio effect:** Across hundreds or thousands of workloads, individual spikes and dips tend to cancel out, producing a steadier aggregate baseline than any single workload would show. That stability supports larger Savings Plans commitments with less forecasting risk.
+ **Cross-account optimization:** If you use consolidated billing, you can optimize across multiple AWS accounts by centralizing purchasing decisions through AWS Organizations. This allows Savings Plans and Regional Reserved Instance discounts to be shared across accounts, maximizing utilization rates. On-Demand Capacity Reservations can also be shared across accounts using AWS Resource Access Manager. For shared Capacity Reservations, billing for unused capacity can be assigned to a specific consumer account, helping you align costs with the teams that requested the capacity. Additionally, [Interruptible Capacity Reservations](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-ec2-interruptible-capacity-reservations/) allow teams to make unused reserved capacity temporarily available to other workloads within the organization the capacity owner retains control to reclaim it when needed, while other teams can use it for fault-tolerant workloads in the interim.
+ **Seasonal aggregation:** While individual applications may have unpredictable seasonal patterns, large portfolios often exhibit more stable aggregate seasonal trends. Retail workloads peak during holidays, while educational workloads peak during enrollment periods. Understanding these combined patterns enables more strategic capacity planning.
+ **Risk distribution:** At scale, you can implement more aggressive cost optimization strategies because you can distribute risk across your portfolio. A portion of workloads can leverage maximum Spot Instance usage while others maintain reserved capacity, achieving overall cost optimization while maintaining business continuity.

------

### Choose
<a name="ec2-po-choose"></a>

**Tip**  
Before committing to a purchasing option, ensure your instances are right-sized using [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/). Oversized instances waste money regardless of the purchasing model you choose.

Selecting the right EC2 purchasing strategy requires balancing financial considerations with operational requirements. Most organizations implement a hybrid approach, combining multiple purchasing options to optimize both cost and performance. A common pattern is to use commitment-based options such as Savings Plans for baseline capacity, On-Demand or Spot Instances for fluctuating workloads, and On-Demand Capacity Reservations for mission-critical applications that require capacity assurance.

The following table helps you determine the broader purchasing options based on your specific requirements and usage patterns:


| 
| 
|  | Instant Requests | Discount Vehicles | Capacity Assurance | 
| --- |--- |--- |--- |
|  | On-Demand Instances | Spot Instances | Compute Savings Plans | Amazon EC2 Instance Savings Plans | On-Demand Capacity Reservations | Capacity Blocks for ML | 
| --- |--- |--- |--- |--- |--- |--- |
| Term | No commitment (60-second billing minimum) | No commitment | 1-year or 3-year hourly spend commitment | No commitment required for immediate-use. Future-dated CRs require a commitment duration after start date | Defined reservation window (up to 6 months duration) | 
| --- |--- |--- |--- |--- |--- |
| Minimum duration | None | 1 year | None (immediate-use), minimum 14 days if future-dated | Minimum 1 day. 1-day increments up to 14 days, 7-day increments up to 6 months. Reservation offerings available starting as soon as 30 minutes | 
| --- |--- |--- |--- |--- |
| Capacity benefit | No capacity reserved | Open-ended reservation in a specific AZ (instance type \+ tenancy \+ platform fixed) | Time-boxed reservation in a specific AZ for a defined window | 
| --- |--- |--- |--- |
| Billing discount | No discount (baseline pricing) | Up to 90% discount vs On-Demand | Up to 66% discount vs On-Demand | Up to 72% discount vs On-Demand | No billing discount (can combine with Savings Plans or Regional RIs for discounts) | Prices based on supply and demand, updated periodically | 
| --- |--- |--- |--- |--- |--- |--- |
| Flexibility | High, any available instance type | Highest: works across Amazon EC2, Fargate, Lambda; any region, AZ, instance family, OS, tenancy | Specific instance family and region | AZ-specific, exact instance type matching | Limited to supported GPU/accelerator instance types | 
| --- |--- |--- |--- |--- |--- |
| Payment options | Per-second (60s min) for Linux, Windows, Windows\+SQL, RHEL, Ubuntu, Ubuntu Pro; per-hour for SUSE | No Upfront, Partial Upfront, All Upfront | Per-second On-Demand-rate billing for the entire life of the reservation, whether or not an instance is launched into it | Reservation fee charged upfront at time of purchase \+ OS fee while running | 
| --- |--- |--- |--- |--- |
| Availability assurance | Available subject to capacity | Subject to availability of unused Amazon EC2 capacity; can be interrupted | No capacity assurance | Capacity reserved in specified AZ | Capacity reserved for the scheduled window | 
| --- |--- |--- |--- |--- |--- |
| Interruption risk | No interruption | Can be interrupted with 2-minute notice; instance is terminated by default (or stopped/hibernated if configured at launch) | No interruption | No interruption during reservation window | 
| --- |--- |--- |--- |--- |
| Billing start | When Amazon EC2 instance enters running state | When purchased (or on queued start date) | When reservation becomes active | Upfront at time of purchase (reservation fee); OS billed when instances run | 
| --- |--- |--- |--- |--- |
| Modification flexibility | No commitment terms to modify | Existing plans cannot be modified; can queue future purchases | Immediate-use: modify count/instance attributes, split, or share via RAM. AZ binding is fixed at creation. Future-dated CRs restricted during commitment period | Cannot cancel or modify after purchase. Can purchase consecutive blocks (subject to availability). | 
| --- |--- |--- |--- |--- |
| Regional scope | All regions/AZs (instance type availability varies) | Global (any region any AZ) | Specific region | Single AZ only | Single AZ only (select regions) | 
| --- |--- |--- |--- |--- |--- |
| Capacity planning | No planning required | Specify hourly spend commitment (USD/hr) | Must specify instance type, count, AZ, platform, and tenancy | Specify instance type, count (1-64), start date, and duration | 
| --- |--- |--- |--- |--- |
| Sharing across AWS accounts | Not applicable | Automatically applies across all accounts in AWS Organizations (by default) | AWS Resource Access Manager | Instance CBs: Yes (via AWS RAM, same Org). UltraServer CBs: No | 
| --- |--- |--- |--- |--- |
| Queuing support | Not applicable | Yes (up to 3 years ahead) | Yes - future-dated CRs up to 120 days ahead (min 14-day commitment) | Reserve up to 8 weeks in advance | 
| --- |--- |--- |--- |--- |
| Cancellation policy | Can terminate anytime | Cannot cancel (7-day return for plans ≤USD 100/hr) | Immediate-use: can cancel anytime. Future-dated: cannot cancel during commitment period | Cannot cancel after purchase | 
| --- |--- |--- |--- |--- |
| Best use cases | New applications; short-term, irregular workloads that cannot be interrupted; proof of concepts | Batch processing; Fault-tolerant applications; CI/CD pipelines; Workloads flexible on time or instance type; Containerized workloads | Mixed compute usage (Amazon EC2, Fargate, Lambda); Multi-region workloads; Modernization initiatives; Organizations wanting simplest commitment model | Consistent Amazon EC2 usage within specific instance family; Regional workloads with predictable instance needs | Critical workloads needing capacity assurance; Seasonal capacity planning; Disaster recovery; Compliance requirements | ML model training and fine-tuning; ML experiments and prototypes; Temporary GPU/accelerator capacity needs | 
| --- |--- |--- |--- |--- |--- |--- |
| Combination strategy | Use for burst or variable capacity | Use as supplement to committed or On-Demand capacity. Best practice: diversify across instance types and AZs | Can combine with On-Demand Capacity Reservations for capacity assurance | Combine with Savings Plans or Regional RIs for billing discounts | Cannot combine with Savings Plans or RI discounts; standalone pricing | 
| --- |--- |--- |--- |--- |--- |

The following diagram shows recommended EC2 purchasing strategies for common workload types.

![Amazon EC2 purchasing options for common workload types](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/diagram_ec2_purchase_strategy.png)


#### Hybrid EC2 purchasing strategy: Accelerating workloads with Spot without risking deadlines
<a name="ec2-po-choose-spot"></a>

**Important**  
Adopt a hybrid EC2 purchasing approach: use On-Demand or committed options such as Savings Plans for baseline capacity that meets your deadlines, then supplement with Spot Instances to accelerate performance and reduce costs.

A common pattern is to define your workload's completion deadline, then provision baseline capacity using On-Demand Instances or committed options such as Savings Plans that can independently meet this timeline. During runtime, supplement this foundation with Spot Instances to accelerate completion. For example, adding Spot capacity equal to your baseline can reduce completion time significantly while lowering overall costs, even if some Spot capacity is reclaimed. This approach provides workload reliability through assured baseline capacity while capturing additional cost savings through Spot supplementation, particularly effective for batch processing, data analytics, and other fault-tolerant workloads.

### Use your purchasing options
<a name="ec2-po-use"></a>

After you have determined which Amazon EC2 purchasing options best fit your workload requirements, the following resources can help you get started—from launching instances and reserving capacity to monitoring, analyzing, and optimizing your costs over time.

------
#### [ Purchase & Setup ]
+ **Get started with the Amazon EC2 tutorial **

  Learn how to launch and configure your first Amazon EC2 instance using the Amazon EC2 launch instance wizard in the Amazon EC2 console.

  [Get started with the Amazon EC2 tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-launch-tutorials.html)
+ **Launch On-Demand Instances**

  Provision instances at the standard per-second On-Demand rate with no upfront commitment, using the launch wizard, CLI, or SDK.

  [Get started with Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)
+ **Purchase Savings Plans**

   Commit to a consistent amount of compute usage ($/hour) for a 1-year or 3-year term. 

  [Explore the guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchasing.html)
+ **Create a Spot Instance request**

  Request spare Amazon EC2 capacity at discounts of up to 90% off On-Demand prices; instances can be interrupted with a two-minute notice when AWS needs the capacity back.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)
+ **Create an Auto Scaling group**

  Configure an Auto Scaling group that combines On-Demand and Spot Instances using a single configuration. Define your instance type diversification, allocation strategies, and the proportion of On-Demand to Spot capacity. Auto Scaling handles provisioning, scaling, and automatic replacement of interrupted Spot Instances.

  [Read the guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)

------
#### [ Monitoring & Analysis ]

Monitor your instance performance and usage patterns for opportunities to right-size your Amazon EC2 instances.
+ **Monitor Savings Plans utilization and coverage**

   Regularly check your Savings Plans utilization and coverage metrics to ensure you are maximizing the value of your commitments.

  [Read the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/sp-utilization-coverage.html)
+ **Build Custom CloudWatch dashboards**

  Visualize your Amazon EC2 cost and utilization and application metrics in one place with customizable dashboards with custom widgets that help identify trends and optimization opportunities for more informed decision-making.

  [Read the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
+ **Monitor and optimize capacity with Amazon EC2 Capacity Manager**

  Use Amazon EC2 Capacity Manager to monitor, analyze, and manage your On-Demand, Spot, and Capacity Reservation usage across all accounts and Regions from a single interface. Identify underutilized Capacity Reservations, analyze usage patterns, and take action to optimize your Amazon EC2 capacity and costs.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager.html)

------
#### [ Scaling & Automation ]
+ **Get started with Amazon EC2 Auto Scaling**

  Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. 

  [Get started with the tutorial](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
+ **Scheduled scaling**

  Set up time-based scaling for predictable workload patterns, such as business hours, weekends, or seasonal traffic variations.

  [Read the guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
+ **Target tracking scaling policies**

  Learn how to automatically adjust your Amazon EC2 capacity based on demand metrics like CPU utilization, network traffic, or custom application metrics to maintain optimal performance and high utilization for your Amazon EC2 instances for better cost efficiency without manual intervention.

  [Read the guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

------
#### [ Budget & Cost Controls ]
+ **Set spending thresholds with AWS Budgets**

   Establish budget thresholds and automated alerts to maintain visibility and control over your Amazon EC2 spending.

  [Read the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
+ **Resource tagging strategies**

  Implement consistent tagging across your Amazon EC2 resources early in your deployment to accurately track costs by department, project, environment, or other business dimensions, enabling detailed cost allocation and analysis.

  [Read the guide](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)

------
#### [ Right-sizing & Continuous Optimization ]
+ **Use AWS Compute Optimizer to find right-size candidates**

   Learn how to monitor and analyze your current Amazon EC2 instance performance and usage patterns to strategize how you can right size your Amazon EC2 instances and optimize your costs over time.

  [Read the guide](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.html)
+ **AWS Billing and Cost Management**

  Use [AWS Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) to identify savings opportunities, including tailored Savings Plans recommendations based on your historical usage. Monitor your Savings Plans utilization and coverage in [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to maximize the value of your commitments over time.

  [Read the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)

------

#### Spot optimizations
<a name="ec2-po-spot-instances"></a>

AWS offers a broad and continuously expanding selection of Amazon EC2 instance types to fit virtually any workload. A set of unused Amazon EC2 instances with the same instance type (for example, m5.large) in a particular Availability Zone (for example, us-east-1a) constitute a single Spot capacity pool. When you request Spot capacity, AWS allocates compute resources from matching capacity pools that have unused Amazon EC2 instances in your specified Availability Zones. By including multiple instance types and Availability Zones in your Spot requests, you expand the number of capacity pools available to fulfill your request, significantly increasing your chances of obtaining the compute capacity you need.

We use capacity-allocation strategies to launch instances from the deepest Spot capacity pools (pools with the largest spare capacity), which inherently reduces the likelihood of Spot interruptions. With Spot Instances, you can maximize compute cost savings while learning how to minimize the impact of interruptions through proper planning and implementation strategies.

------
#### [ Requesting and maintaining Spot capacity ]
+ **Getting started with Spot Instances**

  Learn the fundamentals of Amazon EC2 Spot Instances, including how to request Spot capacity, understand pricing dynamics, and identify suitable workloads for this pricing model.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
+ **Understanding pricing model**

  Spot Instances use a simplified pricing model where prices are set by Amazon Amazon EC2 and adjusted gradually based on long-term supply and demand trends. This approach provides predictable pricing without the complexity of bidding mechanisms that were used historically. If a Spot Instance is interrupted within the first hour of use, you are not charged for that partial hour of usage.

  [View current Spot prices](https://aws.amazon.com/ec2/spot/pricing/) \| [View pricing history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) \| [Savings calculator](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html) \| [Billing for interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html)
+ **Requesting and maintaining Spot capacity**

  AWS provides APIs for requesting Spot capacity: RunInstances, Amazon EC2 Fleet, and Auto Scaling Groups. RunInstances offers basic functionality with limited options, while Amazon EC2 Fleet and Auto Scaling Groups provide extensive configuration capabilities for large-scale production deployments.

  [RunInstances API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#using-spot-instances-request) \| [Amazon EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html) \| [Amazon EC2 Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
+ **Spot allocation strategies**

  The Spot allocation strategy determines how Amazon EC2 selects and prioritizes Spot capacity pools (combinations of instance types and Availability Zones) when launching Spot Instances. When launching instances, the API uses the allocation strategy that you specify to select the specific pools from all possible pools. There are five allocation strategies: Price capacity optimized, Capacity optimized, Capacity Optimized Prioritized, Diversified, and Lowest price (not recommended). These strategies have significant impact on which capacity pools will be selected to provision the requested capacity. In most cases, the recommended strategy is Price capacity optimized strategy, which balances cost and reduces the possibility of interruptions. This strategy requests Spot Instances from the pools that have the lowest chance of interruption in the near term, then requests Spot Instances from the lowest priced of these pools.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html)
+ **Implement observability and monitoring**

  Implement observability and cost management practices to make data-driven decisions about workload suitability and cost savings maximization. Cost allocation tags enable detailed tracking of Spot workloads by categorizing them across teams, projects, and environments, helping quantify actual savings and identify new opportunities. Setting up budgets, alerts, and dashboards with tagged resources allows you to analyze interruption patterns, implement governance controls, and optimize your Spot strategy based on usage trends and cost metrics.

  [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) \| [Filtering the AWS costs data that you want to view](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) \| [Savings from purchasing Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html)

------
#### [ Minimizing interruption risks ]
+ **Instance diversification**

  Instance diversification is the most straightforward recommendation to implement that delivers the biggest improvement in Spot experience. Leverage a combination of Spot allocation strategies (such as Price Capacity Optimized) and broad instance types and Availability Zones to maximize access to Spot capacity. Reduce interruption risk by spreading your workload across multiple instance types, sizes, and Availability Zones. Applications that can run on diverse instance types have significantly higher availability and lower interruption rates.
+ **Attribute-based instance selection**

  Attribute-based instance selection lets you specify compute requirements (vCPU, memory, architecture) rather than exact instance types. This allows your fleet to automatically select from a much larger pool of suitable instances, improving availability and Spot capacity access. It simplifies configuration while enabling broad diversification across instance families, sizes, and generations, including newly launched types.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html)
+ **Implementing geographic flexibility**

  Expand your Spot Instance deployments across multiple Availability Zones and Regions to access more spare capacity and reduce the impact of capacity constraints in any single location. Use the Spot placement score API to identify the most promising Regions and Availability Zones for your workload requirements.

  [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) \| [Spot placement score tracker](https://github.com/aws-solutions-library-samples/guidance-for-ec2-spot-placement-score-tracker)
+ **Flexibility on time**

  Schedule your Spot workloads during periods of lower demand to increase the likelihood of obtaining and maintaining Spot capacity with fewer interruptions.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html)

------
#### [ Minimizing interruption impacts ]
+ **Leveraging notices for Amazon EC2 Spot interruptions**

  Two minutes before a Spot Instance is interrupted by AWS, Amazon EC2 issues a Spot Instance interruption notice as an EventBridge event and as items in the instance metadata. Leverage the time to gracefully save state, drain connections, and redirect traﬃc to maintain application availability.

  [Spot Instance interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html) \| [Taking Advantage of Amazon EC2 Spot Instance Interruption Notices](https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/)
+ **Responding to rebalance recommendations**

  EC2 rebalance recommendations signal when Spot Instances are at elevated interruption risk. This lets you proactively migrate workloads to new or existing Spot Instances. Auto Scaling Groups can automatically rebalance Spot capacity based on these recommendations.

  [Amazon EC2 instance rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html) \| [Capacity rebalancing in auto scaling to replace at-risk Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html)
+ **Reducing compute time of individual tasks**

  Leverage a divide-and-conquer approach to break large jobs into smaller, faster-completing tasks. This reduces the chance of interruption before task completion and minimizes interruption impact, as tasks that are completed within two minutes are unaffected by Spot interruptions.

  [Explore the guide](https://aws.amazon.com/ec2/spot/getting-started/#best-practices)
+ **Workload checkpointing**

  Implement a checkpointing mechanism to save your job's current state (files, progress, and parameters) to persistent storage at regular intervals, or when receiving a Spot interruption notice. You can resume work from the last saved checkpoint on a different Amazon EC2 instance.

  [Checkpointing HPC Applications](https://aws.amazon.com/blogs/hpc/checkpointing-hpc-applications-using-the-spot-instance-two-minute-notification-from-amazon-ec2) \| [Save Up to 90% with Long-Running HPC Jobs](https://aws.amazon.com/blogs/hpc/save-up-to-90-using-ec2-spot-even-for-long-running-hpc-jobs) \| [Cost Optimization with Ansys LS-DYNA](https://aws.amazon.com/blogs/hpc/cost-optimization-on-spot-instances-using-checkpoints-for-ansys-ls-dyna/)

------
#### [ Advanced Spot practices ]
+ **Spot hibernation**

  Use Spot Instance hibernation to save in-memory state during interruptions for faster recovery. Hibernated instances can only resume in the same capacity pool (instance type and Availability Zone), and if that pool never regains availability the instance may never resume. Consider whether indefinite waiting is acceptable versus restarting on new instances elsewhere. Hibernation comes with constraints: RAM under 150 GB, 60-day maximum duration before termination, EC2-only resumption, plus restrictions on instance family, root volume type, and encryption. See the link below for more details.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html)
+ **Workload prioritization**

  Implement workload prioritization so that critical tasks run on On-Demand or committed instances.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)
+ **Spot placement score**

  Maximize your chances of securing Amazon EC2 Spot Instances by leveraging the Spot placement score feature, which helps you identify the most promising Regions and Availability Zones for your workload requirements.

  [Read the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html)
+ **Test Spot Instance interruptions using AWS FIS**

  Learn how to simulate Spot Instance interruptions using AWS Fault Injection Service (FIS) and build more reliable, cost-effective applications that can handle Amazon EC2 capacity reclamation gracefully.

  [Get started with the tutorial](https://docs.aws.amazon.com/fis/latest/userguide/fis-tutorial-spot-interruptions.html)

------

### Explore
<a name="ec2-po-explore"></a>
+ **AWS Compute Optimizer**

  Get recommendations to optimize the performance and cost of your AWS resources.

  [Explore Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+ **AWS Well-Architected Cost Optimization Workshop**

  Learn cost optimization best practices from the AWS Well-Architected Framework.

  [AWS Well-Architected Labs cost optimization workshop](https://wellarchitectedlabs.com/cost/)

# Storage & Databases
<a name="storage-databases"></a>

The following decision guides help you choose AWS services for persisting and managing your data, including object, file, and block storage as well as purpose-built databases.

**Topics**
+ [Choosing an AWS storage service](#choosing-aws-storage-service)
+ [Choosing an AWS database service](#databases-on-aws-how-to-choose)

## Choosing an AWS storage service
<a name="choosing-aws-storage-service"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS storage service is the best fit for your organization. | 
| **Last updated** | June 26, 2024 | 
| **Covered services** |  +  [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) <br />+  [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) <br />+  [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html) <br />+  [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) <br />+  [Amazon File Cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html) <br />+  [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html) <br />+  [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html) <br />+  [AWS Snow Family](https://docs.aws.amazon.com/snowball/) <br />+  [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/) <br />+  [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html)   | 

### Introduction
<a name="intro"></a>

AWS offers a broad portfolio of reliable, scalable, and secure storage services for storing, accessing, protecting, and analyzing your data. This makes it easier to match your storage methods with your needs, and provides storage options that are not easily achievable with on-premises infrastructure. When selecting a storage service, ensuring that it aligns with your access patterns will be critical to achieving the performance you want.

You can select from block, file, and object storage services as well as cloud data migration options for your workload. Choosing the right storage service for your workload requires you to make a series of decisions based on your business needs.

This decision guide will help you ask the right questions, provide a clear path for implementation, and help you migrate from your existing on-premises storage.

[![AWS Videos](https://img.youtube.com/vi/A14EbSrZeFM?start=16&end=377/0.jpg)](https://www.youtube.com/watch?v=A14EbSrZeFM?start=16&end=377)


### Understand
<a name="understand"></a>

Data is a cornerstone of successful application deployments, analytics workflows, and machine learning innovations. Well-architected systems use multiple storage services and enable different features to improve performance.

In many cases, however, choosing the right storage service will start with how well it aligns with what you're already using (or are familiar with). Working with storage services that you are familiar with will make it easier for you to get started - and can make migration of your data easier and potentially faster.

![Diagram showing data protection, data at work, and data in motion with the Amazon FSx data storage family.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/amazon-fsx-data-storage-family.png)


For example, services in the Amazon FSx data storage family come in four options that align to popular file systems:
+ **Amazon FSx for Windows File Server** provides fully managed Microsoft Windows file servers, backed by a fully native Windows file system.
+ **Amazon FSx for Lustre** allows you to launch and run the high-performance Lustre file system.
+ **Amazon FSx for OpenZFS** a fully managed file storage service that enables you to move data to AWS from on-premises ZFS or other Linux-based file servers.
+ **Amazon FSx for NetApp ONTAP** a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp's popular ONTAP file system.

#### Definitions
<a name="definitions"></a>

There are AWS service options for the following storage types: 
+ **Block** — Block storage is technology that controls data storage and storage devices. It takes any data, like a file or database entry, and divides it into blocks of equal sizes. The block storage system then stores the data block on underlying physical storage in a manner that is optimized for fast access and retrieval.
+ **File system** — File systems store data in a hierarchical structure of files and folders. In network environments, file-based storage often uses network-attached storage (NAS) technology. NAS allows users to access network storage data in similar ways to a local hard drive. File storage is user-friendly and allows users to manage file-sharing control.
+ **Object** — Object storage is a technology that stores and manages data in an unstructured format called objects. Each object is tagged with a unique identifier and contains metadata that describes the underlying content.
+ **Cache** — A cache is a high-speed data storage layer used to temporarily store frequently accessed or recently used data closer to the point of access, with the aim of improving system performance and reducing latency. It serves as a buffer between the slower and larger primary storage (such as disks or remote storage) and the computing resources that need to access the data.
+ **Hybrid/Edge** — Hybrid/Edge storage combines on-premises storage infrastructure with cloud storage services, allowing data mobility between the two environments based on requirements like performance, cost, and compliance. It provides benefits such as low-latency access, cost optimization, data sovereignty, cloud scalability, and business continuity.

#### Migration options
<a name="migration_options"></a>

In addition to choosing a storage service, you will need to make choices about how you migrate your data to live within the chosen services. AWS offers several choices to migrate your data - based on whether it needs to live online or offline. 
+ **Online migration** involves transferring data and applications over the internet while they are still running in the on-premises data center. This approach can be more efficient than offline migration since it minimizes downtime and enables organizations to start using cloud resources sooner. However, it requires a reliable internet connection and may not be suitable for large amounts of data or mission-critical applications.
+ **Offline migration** involves moving data and applications without any connection to the internet. This approach requires physically transporting the data on external hard drives or other storage media to the cloud provider’s data center. This method is typically used when there are large amounts of data to transfer, limited bandwidth or connectivity, or concerns about security and privacy.

There are two key considerations:
+ **Speed - ** Choose online migration when speed matters. Online is measured in minutes or hours, and offline can be measured by days. If data is frequently updated and time-critical, choose online. Choose offline when it’s a one-time move, and not time-critical.
+ **Bandwidth -** Moving data online takes away from available bandwidth used for day-to-day. Choose offline when there are network constraints, and data can be offline while in transit without disrupting your business. AWS services in the Snow Family offer an option for offline migration. 

### Consider
<a name="consider"></a>

You might be considering AWS storage services because you are migrating an existing application to the cloud or building a new application in the cloud. When moving data to the cloud, it is important for you to understand where you are moving it, the potential use cases, the type of data you are moving, and the network resources available.

Here's some of the criteria to consider when choosing an AWS storage service.

------
#### [ Protocol ]

AWS storage services offer multiple protocol options:
+ **Block storage** offers high-performance storage that is direct-attached to a compute instance with low-latency access, making it suitable for applications that require fast and consistent I/O operations.
+ **File-based storage ** is natively mountable from virtually any operating system using industry-standard protocols like NFS and SMB. It provides simple storage for workloads that need access to shared data across multiple compute instances.
+ **Object storage** provides easy access to data through an application programming interface (API) over the internet and is well-suited to read-heavy workloads (such as streaming applications and services).

Protocols play a crucial role when considering AWS storage services as they determine how data is accessed, transferred, and managed within the storage environment.

------
#### [ Client type ]

It's important to consider the operating system of the clients that will be accessing the data. Windows-based clients can use file-based storage options such as Amazon FSx for Windows File Server. It provides highly available storage to your Windows applications with full Server Message Block (SMB) support.

Amazon FSx for Lustre (for high-performance file systems) is designed for use with Unix/Linux-based file systems. FSx for Lustre is optimized for workloads where speed matters, such as machine learning, high performance computing (HPC), video processing, and financial modeling.

The choice of client type for an AWS storage service is critical to ensure easy access and sharing of data across workloads. Selecting a service that is compatible with the file systems and protocols used by your clients is key to avoiding compatibility issues and ensuring seamless data access and transfer.

------
#### [ Performance ]

Performance is a critical factor to consider when choosing an AWS storage service. There are several factors to consider when evaluating storage performance, including IOPS (input/output operations per second), access patterns, latency, and throughput or bandwidth. It is important to ask questions such as:
+ Is your workload latency sensitive?
+ Do other metrics (such as IOPS or throughput) dominate your applications performance profile?
+ Is your workload read or write-heavy?

------
#### [ Migration strategy and risks ]

The skills of your organization are a major factor when deciding which container services you use. The approach you take can require some investment in DevOps and Site Reliability Engineer (SRE) teams. Building out an automated pipeline to deploy applications is common for most modern application development.

Some factors to consider when migrating your on-premises storage to AWS are:
+ **Data transfer**: what is the most efficient method to transfer your data to AWS?
+ **Compatibility**: For example, if you already leverage NetApp ONTAP appliances on-premises services (such as Amazon FSx for NetApp ONTAP) provide a seamless migration path.
+ **Application integration**: Evaluate how your applications will integrate with AWS storage services. Consider any necessary modifications or configurations required to enable seamless connectivity and functionality between your applications and the AWS environment.
+ **Data Management and lifecycle:** Plan for data management tasks such as backup, replication, and lifecycle management in the AWS environment. Consider AWS services and features that can help automate these tasks, such as versioning, lifecycle policies, and cross-region replication.
+ **Security and compliance**: Ensure that your data remains secure during the migration process. Implement appropriate security measures, such as encryption and access controls, to protect your data both in transit and at rest.
+ **Cost optimization**: Analyze the cost implications of migrating your storage solution to AWS. Consider factors such as storage pricing, data transfer costs, and any associated services or features required to optimize costs.

By carefully considering these factors, you can ensure a successful migration from an on-premises storage solution to AWS storage services, minimizing disruptions, and maximizing the benefits of cloud storage.

------
#### [ Backup and protection requirements ]

Backup and protection requirements are critical factors to consider when choosing an AWS storage service because they help ensure the availability and durability of your data.

Without adequate backup and protection measures, data can be lost due to accidental deletion, hardware failure, or natural disasters, which can have severe consequences for your business.

Familiarize yourself with services such as [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/getting-started.html), which can backup your data on demand or automatically as part of a scheduled backup plan. AWS Backup also offers cross-region replication which can be particularly valuable if you have business continuity or compliance requirements to store backups a minimum distance away from your production data.

------
#### [ Disaster recovery ]

Disaster recovery is a critical consideration when choosing an AWS storage service because it helps ensure business continuity in the event of a disaster or outage. A disaster can be caused by various factors, such as natural disasters, human error, or cyber attacks, and can result in significant data loss and downtime.

Choosing a storage service that provides disaster recovery features, such as replication across multiple availability zones, can help minimize the impact of a disaster on your business. It's important to consider factors such as recovery time objectives (RTO) and recovery point objectives (RPO) when evaluating disaster recovery options and choose a storage service that meets your business needs.

------
#### [ Cost ]

Beyond the base storage costs, there are other factors that impact pricing such as storage capacity, data transfer, and availability that impacts the total cost of storage. The following can help you reduce cost when using an AWS storage service:
+ Use the appropriate storage service for your workload type.
+ Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and other [billing tools](https://aws.amazon.com/aws-cost-management/) to monitor organizational speed.
+ Understand your data and how it is being used.

We also recommend that you use the [AWS Pricing Calculator](https://calculator.aws/#/) to estimate your cost when choosing an AWS storage service.

------
#### [ Security ]

Security at AWS is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/). AWS provides a secure foundation for customers to build and deploy their applications, but customers are responsible for implementing their own security measures to protect their data, applications, and infrastructure.

You should consider aspects of security such as access control, data encryption, compliance requirements, monitoring and logging, and incident response when choosing an AWS storage service. By doing so, you can help ensure that your data is protected while using AWS services.

------

### Choose
<a name="choose"></a>

Now that you know the criteria you should use to evaluate your storage options, you are ready to choose which AWS storage services are right for your business needs.

The following table highlights which storage options are optimized for which circumstances. Use it to help determine the one that is the best fit for your use case.



| Storage type | What is it optimized for? | Storage services or tools | 
| --- |--- |--- |
| Block | Applications requiring low-latency, high-performance durable storage attached to single Amazon EC2 instances or containers, such as databases and general-purpose local instance storage. | [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html)<br />[ Amazon EC2 instance store ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) | 
|  File system  |  Applications and workloads requiring shared read and write access across multiple Amazon EC2 instances or containers, or from multiple on-prem servers, such as team file shares, highly-available enterprise applications, analytics workloads, and ML training.  |  [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) [Amazon FSx](https://docs.aws.amazon.com/fsx/) [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html) [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html) [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) [Amazon S3 File Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) [Amazon FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html)  | 
| --- |--- |--- |
| Object | Read-heavy workloads such as content distribution, web hosting, big data analytics, and ML workflows. Well-suited for scenarios where data needs to be stored, accessed, and distributed globally over the internet. | [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) | 
|  Cache  |  Fully managed, scalable, and high-speed cache on AWS for processing file data stored in disparate locations—including on premises NFS file systems, and/or in cloud file systems (Amazon FSx for OpenZFS, Amazon FSx for NetApp ONTAP), and Amazon S3.  |  [Amazon File Cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html)  | 
| --- |--- |--- |
| Hybrid/Edge | Deliver low-latency data to on-premises applications and providing on-premises applications access to cloud-backed storage. | [AWS Storage Gateway Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html)<br />[AWS Storage Gateway Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) | 

The following table provides a detailed look at your online and offline options.



| Migration options | When speed is the priority | When bandwidth is important | Storage services or tools | 
| --- |--- |--- |--- |
| Online | Online is optimized for frequent updates to data. Use it for time-critical or ongoing workloads. | Consider scheduling your transfer during off hours when you have sufficient bandwidth. | [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html)<br />[AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html)<br />[ Amazon FSx for NetApp ONTAP SnapMirror ](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html)<br />[AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/) | 
|  Offline  | Suitable for one-time or periodic uploads - and when data can be static in transit. |  This choice makes sense when you need to use only the minimum available bandwidth - and you prefer the predictability of physical moves.   |  [AWS Snowball](https://docs.aws.amazon.com/snowball/)  | 
| --- |--- |--- |--- |

### Use
<a name="use"></a>

Now that you have determined the best protocol you need to work with your data, your performance requirements, and other criteria discussed in this guide, you should also have an understanding of which storage service would be the best fit for your needs. 

To explore how to use and learn more about each of the available AWS storage services - we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ Amazon S3 ]
+  **Getting started with Amazon S3** 

  This guide will help you get started with Amazon S3 by working with buckets and objects. A bucket is a container for objects. An object is a file and any metadata that describes that file.

   [Explore the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) 
+  **Optimizing Amazon S3 performance** 

  When building applications that upload and retrieve storage from Amazon S3, follow the AWS best practices guidelines in this paper to optimize performance.

   [Read the whitepaper](https://docs.aws.amazon.com/whitepapers/latest/s3-optimizing-performance-best-practices/welcome.html) 
+  **Amazon S3 tutorials** 

  The following tutorials present complete end-to-end procedures for common Amazon S3 tasks. These tutorials are intended for a lab-type environment and provide general guidance.

   [Get started with the tutorials ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorials.html) 

------
#### [ Amazon EBS ]
+  **Getting started with Amazon EBS** 

  Amazon EBS is recommended for data that must be quickly accessible and requires long-term persistence.

   [Explore the guide ](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) 
+  **Create an Amazon EBS volume** 

  An Amazon EBS volume is a durable, block-level storage device that you can attach to your instances.

   [Get started with the tutorial](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html) 
+  **Use Amazon EBS direct APIs to access the contents of an Amazon EBS snapshot ** 

  You can use the direct APIs to create Amazon EBS snapshots, write and read data on your snapshots, and identify differences. 

   [Explore the guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-accessing-snapshot.html) 

------
#### [ Amazon EFS ]
+  **Getting started with Amazon EFS** 

  Learn how to create an Amazon EFS file system. You will mount your file system on an Amazon EC2 instance in your VPC, and test the end-to-end setup.

   [Get started with the tutorial](https://docs.aws.amazon.com/efs/latest/ug/getting-started.html) 
+  **Create a Network File System** 

  Learn how to store files and create an Amazon EFS file system, launch a Linux virtual machine on Amazon EC2, mount the file system, create a file, terminate the instance, and delete the file system.

   [Get started with the tutorial](https://aws.amazon.com/getting-started/tutorials/create-network-file-system/) 
+  **Set up an Apache web server and serve Amazon EFS files** 

  Learn how to set up an Apache web server on an Amazon EC2 instance and set up an Apache web server on multiple Amazon EC2 instances by creating an Auto Scaling group.

   [Get started with the tutorial](https://docs.aws.amazon.com/efs/latest/ug/wt2-apache-web-server.html) 

------
#### [ Amazon FSx ]
+  **Getting started with Amazon FSx** 

  This getting started guide walks you through what you'll need to do to begin using Amazon FSx.

   [Explore the guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) 
+  **Getting started with Amazon FSx for Lustre** 

  Learn how to use your Amazon FSx for Lustre file system to process the data in your Amazon S3 bucket with your file-based applications.

   [Explore the guide](https://docs.aws.amazon.com/fsx/latest/LustreGuide/getting-started.html) 
+  **What is Amazon FSx for Windows File Server?** 

  This guide provides an introduction to Amazon FSx for Windows File Server.

   [Explore the guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) 
+  **Getting started with Amazon FSx for NetApp ONTAP** 

  Learn how to get started using Amazon FSx for NetApp ONTAP.

   [Get started with the tutorial](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/getting-started.html) 
+  **Learn how to get started with Amazon FSx for OpenZFS** 

  This guide provides an introduction to Amazon FSx for OpenZFS.

   [Get started with the tutorial](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/getting-started.html) 

------
#### [ Amazon File Cache ]
+  **Getting started with Amazon File Cache** 

  Learn how to create an Amazon File Cache resource and access it from your compute instances.

   [Get started with the tutorial](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html) 
+  **Amazon File Cache in action** 

  This video shows how Amazon File Cache can be used as a temporary high performance storage location for data stored in on premises file systems.

   [Watch the video](https://www.youtube.com/watch?v=6G4DapCmNG4&t=41s) 

------
#### [ AWS Storage Gateway ]
+  **User guide for Amazon S3 File Gateway** 

  Describes Amazon S3 File Gateway concepts and provides instructions on using the various features with both the console and the API.

   [Explore the guide](https://docs.aws.amazon.com/filegateway/latest/files3/what-is-file-s3.html) 
+  **User guide for Amazon FSx File Gateway** 

  Describes Amazon FSx File Gateway, which provides access to in-cloud Amazon FSx for Windows File Server shares from on-premises facilities. Includes instructions on working with the console and the API.

   [Explore the guide](https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html) 
+  **User guide for Tape Gateway** 

  Describes Tape Gateway, a durable, cost-effective tape-based solution for archiving data in the AWS cloud. Provides concepts and instructions on using the various features with both the console and the API.

   [Explore the guide](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html) 
+  **User guide for Volume Gateway** 

  Describes Volume Gateway concepts, including details about cached and stored volume architectures, and provides instructions on using their features with both the console and the API.

   [Explore the guide](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) 

------
#### [ AWS DataSync ]
+  **Getting started with AWS DataSync** 

  This guide walks through how you can get started with AWS DataSync by using the AWS Management Console.

   [Explore the guide](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html) 
+  **Simplify multicloud data movement wherever data is stored with AWS DataSync** 

  AWS DataSync supports incremental transfers, integration with IAM for access control, and use cases like data migration, replication, and distribution across AWS Regions or accounts.

   [Read the blog](https://aws.amazon.com/blogs/storage/simplify-multicloud-data-movement-wherever-data-is-stored-with-aws-datasync/) 
+  **AWS DataSync tutorials** 

  These tutorials walk you through some real-world scenarios with AWS DataSync and transferring data.

   [Get started with the tutorials](https://docs.aws.amazon.com/datasync/latest/userguide/tutorials.html) 

------
#### [ AWS Transfer Family ]
+  **Getting started with AWS Transfer Family** 

  Learn how to create an SFTP-enabled server with publicly accessible endpoint using Amazon S3 storage, add a user with service-managed authentication, and transfer a file with Cyberduck.

   [Get started with the tutorial](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html) 
+  **AWS Transfer Family in action** 

  This video shows how the AWS Transfer Family can be used for each of the three supported protocols (SFTP, FTPS, and FTP), both over the public internet, as well as within a VPC.

   [Watch the video](https://www.youtube.com/watch?v=AQtTG2N_QCg) 
+  **AWS Transfer Family for AS2** 

  Learn how to set up an Applicability Statement 2 (AS2) configuration with AWS Transfer Family.
+  **AWS Transfer Family SFTP Connectors** 

  Learn how to set up an SFTP connector, and then transfer files between Amazon S3 storage and an SFTP server.

------
#### [ AWS Snow Family ]
+  **Getting started with AWS Snow Family** 

  These guides provide links to documentation covering all current services in the Snow Family.

   [Explore the guides](https://docs.aws.amazon.com/snowball/) 
+  **AWS Snowball Edge developer guide** 

  This guide includes guidance for local storage and compute, clustering, importing and exporting data into Amazon S3, and other features of a Snowball Edge device. 

   [Explore the guide](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) 

------

### Explore
<a name="explore"></a>
+ [Developers](https://aws.amazon.com/getting-started/hands-on/?intClick=dev-center-2021_main&getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=category%23storage&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all)
+ [Solution Architects](https://aws.amazon.com/architecture/storage/?achp_navtc3&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)
+ [Decision makers](https://aws.amazon.com/free/storage/)
+ **Architecture diagrams**

  Explore reference architecture diagrams for containers on AWS.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23storage&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started and learn best practices.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=content-type%23whitepaper&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23storage&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for containers.

  [Explore solutions](https://aws.amazon.com/solutions/storage/)

## Choosing an AWS database service
<a name="databases-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** |  Help determine which AWS database or databases are the best fit for your organization.  | 
| **Last updated** | June 2, 2026 | 
| **Covered services** |  +  [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) <br />+  [Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html) <br />+  [Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) <br />+  [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html) <br />+  [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) <br />+  [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) <br />+  [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html) <br />+  [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html) <br />+  [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) <br />+  [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) <br />+  [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html)   | 

### Introduction
<a name="db-intro"></a>

AWS offers a growing number of database options (15\+) with diverse data models to support a variety of workloads. These include relational, key-value, document, in-memory, graph, time series, vector, and wide-column. 

 Choosing the right database, or multiple databases, requires you to make a series of decisions based on your organizational needs. This decision guide will help you ask the right questions, provide a clear path for implementation, and help you migrate from your existing database.

[![AWS Videos](https://img.youtube.com/vi/MSB_mHUJUaA/0.jpg)](https://www.youtube.com/watch?v=MSB_mHUJUaA)


### Understand
<a name="db-understand"></a>

 Databases are essential backend systems that efficiently store, manage, and retrieve data, ensuring integrity, scalability, and performance for applications of all types and sizes. 

 This decision guide is designed to help you understand the range of choices that are available, establish the criteria for making your database choice, and provide you with detailed information on the unique properties of each database. Then you can learn more about the capabilities that each database offers. 

![Overview of AWS database services.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/aws-database-services.png)


**What are the properties of applications that people build with AWS databases?** 
+ **Internet-scale applications:** These applications can handle 100 million\+ requests per second over hundreds of terabytes of data. They automatically scale vertically and horizontally to provide flexibility for your workloads. 
+ **Real-time applications:** Real-time applications such as caching, session stores, gaming leaderboards, ride hailing, ad targeting, and real-time analytics need microsecond latency and high throughput to support a trillion\+ requests per second. 
+ **Enterprise applications:** Enterprise applications manage core business processes (such as sales, billing, customer service, and human resources) and line-of-business processes (such as a reservation system at a hotel chain or a risk-management system at an insurance company). These applications need databases that are fast, scalable, secure, available, and reliable. 
+ **Vector databases and vector search for use with generative AI applications:** Whatever database service you use will likely contain a wealth of domain-specific data (such as financial records, health records, genomic data, and supply chain information). This data can provide you with a unique and valuable perspective on your business and the broader industry that you work within. For generative AI usage, the domain-specific data you plan to use for semantic context must be encoded as a set of elements, each expressed internally as a “vector”. This contextually relevant data typically comes from your internal databases, data lakes, or unstructured data or document stores—the data stores that host your domain-specific data or knowledge. These data stores are generically called knowledge bases. [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) is the process for retrieving facts from these knowledge bases to ground [large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) with up-to-date, accurate, and insightful data. As outlined in the following diagram, [AWS has added vector capabilities to AWS database and search services](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/) so you can store vector datasets where your data is, simplify your application architecture, and use tried, tested, and familiar tools. A vector database, or vector data store, simply means a database with vector capabilities. Such a database can also provide additional enhancements to the ways you use your data with generative AI. 

![AWS vector databases and vector search.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/vector-db-new.png)


**Note**  
This guide focuses on databases that are suitable for online transaction processing (OLTP) applications. If you need to store and analyze massive amounts of data quickly and efficiently (a requirement that is typically met by an OLAP application), AWS offers [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html). Amazon Redshift is a fully managed, cloud-based data warehousing service that is designed to handle large-scale analytics workloads.  

 There are two high-level categories of AWS OLTP databases—relational and non-relational. 
+  The AWS relational database family includes nine popular engines for Amazon Aurora and Amazon RDS. The Amazon Aurora engines include Amazon Aurora with PostgreSQL-Compatible Edition, Amazon Aurora MySQL-Compatible Edition, and Amazon Aurora DSQL. The Amazon RDS engines include PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2. 
+  The non-relational database options are designed for specific data models. These include key-value, document, caching, in-memory, graph, time series, and wide-column data models. 

 We explore all of these in detail in the [Choose](#db-choose) section of this guide. 

 **Database migration** 

 Before deciding which database service you want to use, you should consider your business objective, database selection, and how you're going to migrate your existing databases. 

 The best database migration strategy helps you to take full advantage of the AWS Cloud. This might involve migrating your applications to use purpose-built cloud databases. You might just want the benefit of using a fully managed version of your existing database, such as RDS for PostgreSQL or RDS for MySQL. 

Alternatively, you might want to migrate from your commercially licensed databases, such as Oracle or SQL Server, to Amazon Aurora. Consider modernizing your applications and choosing the databases that best suit your applications' workflow requirements.

[Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html) is a serverless distributed SQL database with active-active multi-Region replication, strong consistency, and no infrastructure to provision or manage. Aurora DSQL is PostgreSQL-compatible and automatically scales compute, I/O, and storage based on your workload. Aurora DSQL supports transactional workloads in microservice, serverless, and event-driven architectures where you need the benefits of a relational data model without managing database infrastructure.

[Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) provides automated horizontal scaling through sharding, processing millions of write transactions per second and managing petabytes of data while maintaining the simplicity of operating inside a single database. Use Limitless Database when your relational workload requires write throughput or storage beyond the limits of a single Aurora instance.

 If you choose to first transition your applications and then transform them, you might decide to re-platform. This process makes no changes to the application that you use, but lets you take advantage of a fully managed service in the cloud. When your databases are fully in the AWS Cloud, you can start working to modernize your application. This strategy can help you exit your current on-premises environment quickly, and then focus on modernization. 

 You can use [AWS Database Migration Service](https://aws.amazon.com/dms/) to move data to Amazon Aurora. For resources to help with your migration strategy, see the [Explore](#db-explore) section.

### Consider
<a name="db-consider"></a>

 You're considering hosting a database on AWS. This might be to support a greenfield/pilot project as a first step in your cloud migration journey, or you might want to migrate an existing workload with as little disruption as possible. Or perhaps you might want to port your workload to managed AWS services, or even refactor it to be fully cloud focused. 

 Of course, the first major consideration when choosing your database is your business objective. What is the strategic direction that is driving your organization to change? Consider whether you want to rehost an existing workload, or refactor to a new platform so that you don't have to commit to commercial licenses. 

 Whatever your goal is, considering the right criteria can make your database decision easier. Here's a summary of the key criteria to consider. 

------
#### [ Migration strategy ]

 You can choose a rehosting strategy to deploy to the cloud faster, with fewer data migration problems. Install your database engine software on Amazon Elastic Compute Cloud (Amazon EC2), migrate your data, and manage your database in a similar way to how you manage on premises. While rehosting is a fast path to the cloud, you're still left with the operational tasks such as upgrades, patches, backups, capacity planning and management, maintaining performance, and availability targets. 

 Alternatively, you can choose a re-platform strategy where you migrate your on-premises relational database to a fully managed Amazon RDS instance. 

 You might consider this an opportunity to refactor your workload to be cloud focused. For example, you could use Amazon Aurora or purpose-built NoSQL databases such as Amazon DynamoDB, Amazon Neptune, or Amazon DocumentDB (with MongoDB compatibility). 

 Finally, AWS offers serverless databases, which can scale to an application's demands with a pay-for-use pricing model and built-in high availability. With serverless databases, you can increase agility and optimize costs. In addition to removing the need to provision, patch, or manage servers, many AWS serverless databases provide maintenance options that reduce downtime. 

 AWS serverless offerings include Amazon Aurora DSQL, Amazon Aurora Serverless, Amazon DynamoDB, Amazon ElastiCache, Amazon Keyspaces (for Apache Cassandra), Amazon Timestream for LiveAnalytics, and Amazon Neptune Serverless. 

------
#### [ Characteristics of your data ]

 The core of any database choice includes the characteristics of the data that you need to store, retrieve, analyze, and work with. This includes: 
+ Your data model. For example, is it relational, structured, semi-structured, time series, vector, or using a highly connected dataset?
+ Data access. How do you need to access your data?
+ The extent to which you need real-time data.
+ Whether there is a particular data record size you have in mind.

------
#### [ Operational considerations ]

Your primary operational considerations are where your data is going to be located and how it will be managed. The two key choices that you need to make are: 
+  **Will your database be self-hosted or fully managed?**: The core question here is where is your team going to provide the most value to the business? If your database is self-hosted, you'll be responsible for the day-to-day maintenance, monitoring, and patching of the database. 

  Choosing a fully managed AWS database simplifies your work by removing undifferentiated database management tasks. This option allows your team to focus on delivering value by improving schema design, query construction, and query optimization. Your team can also develop applications that align with your business objectives. 
+  **Do you need a serverless or provisioned database?**: To start with, review these links to [Amazon Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html), [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html), [Amazon Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html), [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html), [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html), and [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html); documentation on how to think about provisioned throughput capacity and scaling. Additionally, this guidance for [Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) explains why it is suitable for highly variable workloads (meaning, for example, that your database usage might be heavy for a short period of time, followed by long periods of light activity or no activity at all). 

------
#### [ Resiliency, performance, and security ]

 It's important to ensure that your choice of database provides the resiliency, performance, and levels of security that you need.
+ Resiliency - Database resiliency is key for any business. To achieve resiliency, you have to pay attention to a number of key factors, including capabilities for backup and restore, replication, failover, and point-in-time recovery (PITR).
+ Performance - Consider whether your database will need to support a high concurrency of transactions (10,000 or more), and whether it needs to be deployed in multiple geographic regions. If your workload requires extremely high read performance with a response time measured in microseconds (rather than single-digit milliseconds), you might want to consider using in- memory caching solutions such as [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) alongside your database, or a fully durable, persistent in-memory database such as [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html). 
+ Security - Security is a [shared responsibility](https://aws.amazon.com/compliance/shared-responsibility-model/) between AWS and you. The AWS shared responsibility model describes this as security of the cloud that AWS manages, and security in the cloud that the customer manages. Specific security considerations include data protection at all levels of your data, authentication, compliance, data security, storage of sensitive data, and support for auditing requirements.

------
#### [ Vector database and vector search considerations ]

 When choosing an AWS service with vector database or vector search capabilities, start by thinking about how familiar your team is with the service you are exploring. When developer teams are already familiar with a particular database engine, using the same database engine for vector search helps them make better use of existing knowledge and develop faster. Instead of learning a new skillset, developers can use their current skills, tools, frameworks, and processes to include a new feature of an existing database engine. Here’s how that may apply to your situation:
+  Your team of database engineers may already manage a set of 100 relational databases hosted on [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) PostgreSQL. If they want to support a new database with vector search requirement for their applications, they should first start with evaluating the pgvector extension on their existing Amazon Aurora PostgreSQL databases. Meanwhile, if your team prefers using the community versions of PostgreSQL, [Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) also supports the [pgvector](https://github.com/pgvector/pgvector) extension.
+  Similarly, if your team is working with graph data, consider using [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html), which seamlessly integrates with your existing AWS infrastructure and provides useful graph querying and visualization features. It is ideal for [GraphRAG](https://aws.amazon.com/blogs/database/using-knowledge-graphs-to-build-graphrag-applications-with-amazon-bedrock-and-amazon-neptune/) use cases, or in analyzing large amounts of graph data to get insights and find trends.
+  If you work with popular open source data stores Valkey and Redis OSS and need a highly scalable, in-memory database for real-time applications, consider using [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html). It provides a familiar interface, allowing the team to use their existing Valkey and Redis OSS knowledge and client libraries while benefiting from the fully managed, durable, and scalable capabilities of Amazon MemoryDB. Vector search for Amazon MemoryDB extends the functionality of Amazon MemoryDB. It can be used in conjunction with existing Amazon MemoryDB functionality. Applications that do not use vector search are unaffected by its presence. Vector search is available in all Regions that Amazon MemoryDB is available. Vector search for Amazon MemoryDB is ideal for use cases where peak performance and scale are the most important selection criteria. You can use your existing Amazon MemoryDB data, or a Valkey or Redis OSS API, to build machine learning and generative AI use cases. This includes retrieval-augmented generation, anomaly detection, document retrieval, and real-time recommendations.
+  If your current tech stack lacks vector search support, you can take advantage of serverless offerings to help fill the gap in your vector search needs. For example, [OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) lets you [quickly create](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) an experience on the [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) console without having to create or manage a cluster. If your data is stored in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), OpenSearch Serverless can be an excellent choice for vector search using zero-ETL integration.
+  For cost-optimized vector storage at scale, [Amazon S3 Vectors](https://aws.amazon.com/s3/features/vectors/) provides native support for storing and querying vector data directly in Amazon S3. S3 Vectors supports AI agents, inference, RAG, and semantic search workloads at billion-vector scale.

The following table summarizes vector capabilities across AWS database services to help you select the right option for your generative AI workload.



| Service | Vector capability | Latency | Best for | 
| --- | --- | --- | --- | 
| OpenSearch Service | Native k-NN | Low–Medium | RAG at scale, hybrid search, log analytics | 
| Amazon Aurora PostgreSQL | pgvector extension | Low | Relational apps needing vector \+ transactional data in a single database | 
| Amazon MemoryDB | Native vector search | Sub-millisecond | Semantic caching, real-time inference, ultra-low-latency retrieval | 
| Amazon Neptune Analytics | Vector similarity \+ graph analytics | Medium | GraphRAG, knowledge-graph-enhanced RAG pipelines | 
| Amazon DocumentDB | Native vector search (HNSW/IVFFlat indexes) | Low | MongoDB-compatible apps with vector search requirements | 
| Amazon S3 Vectors | Native vector storage and query | Higher | Cost-optimized bulk vector storage at billion-vector scale | 
| Amazon DynamoDB | Native vector search (vector indexes) \+ zero-ETL to OpenSearch | Varies | Operational store where vector search is a complementary workload | 

 Additional criteria to consider include ease of implementation, scalability, and performance. They are discussed in-depth in this blog: [Key considerations when choosing a database for your generative AI applications](https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/).

------

### Choose
<a name="db-choose"></a>

Now that you know the criteria for evaluating your database options, you're ready to choose which AWS database services might be a good fit for your organization.

This table lists each AWS database engine along with its data model, use cases, and optimizations. Use it to help determine the database that is the best fit for your use case.



|  Database engine  |  Data model  |  When would you use it?  |  What is it optimized for?  | 
| --- |--- |--- |--- |
| [**Amazon Aurora**](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) | Relational | Use when you're migrating or modernizing an on-premises relational workload, or if your workload has less predictable query patterns. Supports MySQL and PostgreSQL-compatible engines with up to five times the throughput of standard MySQL. | Optimized for structured data that is stored in tables, rows, and columns. Relational databases support complex queries through joins. | 
|  [**Amazon Aurora DSQL**](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html)  |  Relational  |  Use when your application needs distributed SQL with active-active multi-Region replication, strong consistency, and no servers to manage.  |  OLTP workloads requiring ACID transactions, a relational model, and serverless auto-scaling. PostgreSQL-compatible.  | 
| --- |--- |--- |--- |
| [**Amazon Aurora PostgreSQL Limitless Database**](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) | Relational | Use when your relational workload requires write throughput or storage beyond the limits of a single Aurora instance, while maintaining a single-database experience. | Millions of write transactions per second and petabyte-scale storage via automated sharding. PostgreSQL-compatible. | 
|  [**Amazon RDS**](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)  |  Relational  |  Use when you need a fully managed relational database with your choice of six popular engines: PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2.  |  Optimized for structured data with full SQL support, automated backups, software patching, and Multi-AZ deployments for high availability.  | 
| --- |--- |--- |--- |
| [**Amazon DynamoDB**](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) | Key-value | Use for workloads such as session stores or shopping carts. Key-value databases can scale to large amounts of data and extremely high throughput of requests, while servicing millions of simultaneous users through distributed processing and storage. | Optimized to provide a serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale. | 
|  [**Amazon DocumentDB (with MongoDB compatibility)**](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)  |  Document  |  Use when you want to store JSON-like documents with rich querying abilities across the fields of the documents.  |  Optimized for storing semi-structured data as documents with multilayered attributes.  | 
| --- |--- |--- |--- |
| [**Amazon Keyspaces (for Apache Cassandra)**](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html) | Wide-column | Use when you need to migrate your on-premises Cassandra workloads, or when you need to process data at high speeds for applications that require single-digit millisecond latency. | Optimized for workloads that require heavy reads/writes and high throughput, coupled with low latency and linear scalability. | 
|  [**Amazon Neptune**](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)  |  Graph  |  Use when you have to model complex networks of objects, such as social networks, fraud detection, and recommendation engine use cases.  |  Optimized for traversing and evaluating large numbers of relationships, and identifying patterns with minimal latency.  | 
| --- |--- |--- |--- |
| [**Amazon ElastiCache**](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) | In-memory | Use when you need a caching layer to improve read performance. Supports Valkey, Memcached, and Redis OSS engines with serverless and node-based deployment options. | Optimized to support microsecond reads and sub-millisecond writes as an ephemeral cache for frequently accessed data. | 
|  [**Amazon MemoryDB**](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html)  |  In-memory  |  Use when you need full data persistence with sub-millisecond read latencies. Suitable as a high-performance primary database for microservices architectures.  |  Optimized as a durable in-memory database with microsecond reads and single-digit millisecond writes, with Multi-AZ durability.  | 
| --- |--- |--- |--- |
| [**Amazon Timestream**](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html) | Time series | Use when you have a large amount of time series data, potentially from a number of sources, such as Internet of Things (IoT) data, application metrics, and asset tracking. | Optimized for storing and querying data that is associated with timestamps and trend lines. | 

### Use
<a name="db-use"></a>

This section helps you learn more about the database service or services that you've chosen, and how to get started with them. 

The database you've chosen might not satisfy all of your requirements perfectly, so it's important to consider your needs and workload requirements carefully. 

Prioritize based on the considerations covered in this guide, your own specific “must have” requirements, and the requirements for which you have some flexibility. This will help you make effective trade-offs and lead to the best possible outcome for your needs. 

 Also consider that, usually, you can cover your application requirements with a mix of best-fit databases. By building a solution with multiple database types, you can use the strengths that each type provides. 

 For example, in an ecommerce use case, you might use Amazon DocumentDB (for product catalogs and user profiles) for the flexibility that is provided by semi-structured data—but then combine it with the low, predictable latency provided by DynamoDB (for when your users are browsing your product catalog). You might also add Aurora into the mix for inventory and order processing, where a relational data model and transaction support are needed.

 To help you learn more about each of the available AWS database services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to help you get started. 

------
#### [ Amazon Aurora ]
+  **Getting started with Amazon Aurora** 

   This guide includes tutorials and covers more advanced Aurora concepts and procedures, such as the different kinds of endpoints and how to scale Aurora clusters up and down. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.html) 
+  **Amazon Aurora PostgreSQL express configuration** 

  Get started in seconds with a streamlined database creation experience using preconfigured defaults optimized for common workloads.

   [Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.html) 
+  **High availability for Amazon Aurora** 

   Amazon Aurora includes high availability features that help your data remain safe even if some or all of the DB instances in the cluster become unavailable. These features also make sure that at least one DB instance is ready to handle database requests from your application. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html) 
+  **Use Amazon Aurora global databases** 

   Get started using Aurora global databases. This guide outlines the supported engines and AWS Region availability for Aurora global databases with Aurora MySQL and Aurora PostgreSQL. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html) 

------
#### [ Amazon Aurora DSQL ]
+  **Getting started with Amazon Aurora DSQL** 

  Create your first Aurora DSQL cluster and connect using PostgreSQL-compatible drivers and tools. Aurora DSQL is serverless with no infrastructure to manage.

   [Get started with Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html) 
+  **Multi-Region clusters** 

  Set up active-active multi-Region clusters with strong consistency, automatic failure recovery, and 99.999% availability.

   [Explore multi-Region setup](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/multi-region.html) 
+  **SQL feature compatibility** 

  Review the PostgreSQL features, expressions, and data types supported by Aurora DSQL.

   [Explore the guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-postgresql-compatibility.html) 

------
#### [ Amazon Aurora Limitless ]
+  **Using Amazon Aurora PostgreSQL Limitless Database** 

  Scale beyond single-instance Aurora limits with automated horizontal sharding. It processes millions of write transactions per second and manages petabytes of data while maintaining a single-database experience.

   [Explore Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) 
+  **Limitless Database architecture** 

  Understand the two-layer architecture of routers and shards that enables distributed processing while presenting a single database image to clients.

   [Explore the architecture](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-architecture.html) 
+  **Getting started with Limitless Database** 

  Create your first Limitless Database DB shard group and configure sharding for your tables.

   [Get started with sharding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-get-started.html) 

------
#### [ Amazon RDS ]
+  **Getting started with Amazon RDS ** 

   Create and connect to a DB instance using Amazon RDS. You learn to create a DB instance that uses DB2, MariaDB, MySQL, Microsoft SQL Server, Oracle, or PostgreSQL.

   [Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html) 
+  **Create and connect to a PostgreSQL database ** 

  Create an environment to run your PostgreSQL database (we call this environment a DB instance), connect to the database, and delete the DB instance. 

   [Get started with the tutorial ](https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/) 
+  **Create a web server and an Amazon RDS DB instance ** 

   Learn how to install an Apache web server with PHP and create a MySQL database. The web server runs on an Amazon EC2 instance using Amazon Linux. The MySQL database is a MySQL DB instance.

   [Use the tutorial ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html) 

------
#### [ Amazon DocumentDB ]
+  **Getting started with Amazon DocumentDB** 

   We help you get started using Amazon DocumentDB in just seven steps. This guide uses AWS Cloud9 to connect and query your cluster using the MongoDB shell directly from the AWS Management Console. 

   [Explore the guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html) 
+  **Setting up a document database with Amazon DocumentDB** 

   This tutorial helps you to get started connecting to your Amazon DocumentDB cluster from your AWS Cloud9 environment with a MongoDB shell, and then run a few queries. 

   [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/getting-started-amazon-documentdb-with-aws-cloud9/) 
+  **Best practices for working with Amazon DocumentDB** 

  Learn best practices for working with Amazon DocumentDB, along with the basic operational guidelines when working with it.

   [ Explore the guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/best_practices.html) 
+  **Migrate from MongoDB to Amazon DocumentDB  ** 

  Learn how to migrate an existing self-managed MongoDB database to a fully managed database on Amazon DocumentDB.

   [Get started with the tutorial](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.html) 
+  **Assessing MongoDB compatibility  ** 

  Use the Amazon DocumentDB compatibility tool to help you assess the compatibility of a MongoDB application by using the application's source code or MongoDB server profile logs.

   [Use the tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/compat-tool) 

------
#### [ Amazon DynamoDB ]
+  **What is Amazon DynamoDB? ** 

  This guide explains how you can use this fully managed NoSQL database service to offload the administrative burdens of operating and scaling a distributed database (including hardware provisioning, setup and configuration, replication, software patching, and cluster scaling).

   [ Explore the guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) 
+  **Getting started with DynamoDB** 

  This guide includes hands-on tutorials that show you how to connect to, create, and manage DynamoDB tables. 

   [ Explore the guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html) 
+  **Programming with Amazon DynamoDB and the AWS SDKs** 

  This guide explains how to program with Amazon DynamoDB and the AWS SDKs, as well as error handling. You can run the code examples on either the downloadable version of DynamoDB or the DynamoDB web service. 

   [Explore the guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.html) 

------
#### [ Amazon ElastiCache ]
+  **Documentation for Amazon ElastiCache  ** 

   Explore the full set of Amazon ElastiCache documentation, including user guides as well as specific AWS CLI and API references.

   [Explore the guide](https://docs.aws.amazon.com/elasticache/index.html) 
+  **Getting started with Amazon ElastiCache  ** 

   Learn how to create, grant access to, connect to, and delete a Valkey (cluster mode disabled) cluster using the Amazon ElastiCache console.

   [Explore the guide](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.html) 

------
#### [ Amazon MemoryDB ]
+  **Getting started with Amazon MemoryDB** 

   We guide you through the steps to create, grant access to, connect to, and delete a MemoryDB cluster using the MemoryDB console. 

   [Use the guide](https://docs.aws.amazon.com/memorydb/latest/devguide/getting-started.html) 
+  **Get started with Amazon MemoryDB for Valkey** 

   Get an overview of MemoryDB for Valkey, its benefits, and how you can upgrade your MemoryDB for Redis OSS database to MemoryDB for Valkey database. 

   [Read the blog](https://aws.amazon.com/blogs/database/get-started-with-amazon-memorydb-for-valkey/) 
+  **Integrating Amazon MemoryDB with Java-based AWS Lambda** 

   We discuss some of the common use cases for the data store, Amazon MemoryDB, which is built to provide durability and faster reads and writes. 

   [Read the blog](https://aws.amazon.com/blogs/compute/integrating-amazon-memorydb-for-redis-with-java-based-aws-lambda/) 

------
#### [ Amazon Keyspaces ]
+  **Getting started with Amazon Keyspaces (for Apache Cassandra)** 

   This guide is for those who are new to Apache Cassandra and Amazon Keyspaces (for Apache Cassandra). It walks you through installing all the programs and drivers that you need to successfully use Amazon Keyspaces. 

   [Explore the guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.html) 
+  **Beginner course on using Amazon Keyspaces (for Apache Cassandra)** 

   Learn the benefits, typical use cases, and technical concepts of Amazon Keyspaces. You can try the service through the sample code provided or the interactive tool in the AWS Management Console. 

   [Take the course (requires sign-in)](https://skillbuilder.aws/learn/KHGZNGWXKV/getting-started-with-amazon-keyspaces/MXK17GET8G) 
+  **Working with change data capture (CDC) streams** 

  Capture real-time data changes in your Amazon Keyspaces tables for event-driven architectures, analytics, and AI applications.

   [Explore CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html) 

------
#### [ Amazon Neptune ]
+  **Getting started with Amazon Neptune** 

   We help you get started using Amazon Neptune, a fully managed graph database service. This guide shows you how to create a Neptune database. 

   [Explore the guide](https://docs.aws.amazon.com/neptune/latest/userguide/graph-get-started.html) 
+  **Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune** 

   Build GraphRAG applications using Amazon Bedrock and Amazon Neptune with [LlamaIndex](https://www.llamaindex.ai/) framework.

   [Read the blog](https://aws.amazon.com/blogs/database/using-knowledge-graphs-to-build-graphrag-applications-with-amazon-bedrock-and-amazon-neptune/) 
+  **Build a real-time fraud detection solution using Amazon Neptune** 

  We demonstrate how businesses can use Amazon Neptune ML and the real-time inductive inference capability to get real-time alerts for fraudulent transactions that can reduce their fraud loss and increase their revenue. 

   [Read the blog](https://aws.amazon.com/blogs/database/build-a-real-time-fraud-detection-solution-using-amazon-neptune-ml/) 

------
#### [ Amazon Timestream ]
+  **Getting started with Amazon Timestream ** 

   We help you get started with Amazon Timestream. This guide provides instructions for setting up a fully functional sample application.

   [Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started.html) 
+  **Best practices with Amazon Timestream ** 

   We explore best practices, including the practices that relate to data modeling, security, configuration, data ingestion, queries, client applications, and supported integrations.

   [Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices.html) 
+  **Accessing Amazon Timestream using AWS SDKs ** 

   Learn how to access Amazon Timestream using the AWS SDKs in the language of your choice: Java, Go, Python, Node.js, or .NET. 

   [Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started-sdks.html) 
+  **Understanding time-series data and why it matters ** 

   Explore the nature of time-series data, its presence across different types of industries and various use cases it enables.

   [Read the blog](https://aws.amazon.com/blogs/database/understanding-time-series-data-and-why-it-matters/) 
+  **Amazon Timestream for InfluxDB 3** 

  A managed time series database service based on InfluxDB 3, providing enhanced performance and capabilities for time series workloads.

   [Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/influxdb3.html) 

------

### Explore
<a name="db-explore"></a>



|  |  | 
| --- |--- |
| **Role**<br /> [Developers](https://aws.amazon.com/getting-started/hands-on/?intClick=dev-center-2021_main&getting-started-all.sort-by=item.additionalFields.content-latest-publish-date&getting-started-all.sort-order=desc&awsf.getting-started-category=category%23databases&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all) <br />[Solution architects](https://aws.amazon.com/architecture/databases/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)<br />[Professional development](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13585/introduction-to-building-with-aws-databases)<br />[Startups](https://aws.amazon.com/startups/start-building/how-to-choose-a-database/)<br />[Decision makers](https://aws.amazon.com/free/database/) | **Migration strategy**<br />[Getting started with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)<br />[Using the AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/)<br />[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)<br />[Selecting the right database and database migration plan for your workloads](https://aws.amazon.com/blogs/architecture/selecting-the-right-database-and-database-migration-plan-for-your-workloads/) | 
+ **Architecture diagrams**

   Explore reference architecture diagrams to help you develop, scale, and test your databases on AWS. 

   [Explore architecture diagrams ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23databases&awsf.industries=*all&awsf.business-category=*all&awsm.page-cards-all=1) 
+ **Whitepapers**

   Explore whitepapers to help you get started, learn best practices, and migrate your databases. 

   [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23databases&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all&awsm.page-whitepapers-main=1) 
+ **AWS solutions**

   Explore vetted solutions and architectural guidance for common use cases for databases. 

   [Explore solutions ](https://aws.amazon.com/solutions/databases/) 

# Choosing AWS frontend web and mobile services
<a name="front-end-mobile"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Time to read** | 14 minutes | 
| **Purpose** | Help determine which AWS services to use when building your web or mobile application. | 
| **Last updated** | June 25, 2024 | 
| **Services covered** |  +  [AWS Amplify](https://docs.amplify.aws/how-amplify-works/) <br />+  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) <br />+  [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) <br />+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) <br />+  [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) <br />+  [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/welcome.html) <br />+  [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html)   | 

## Introduction
<a name="intro"></a>

AWS offers purpose-built tools and services to support frontend development workflows for native iOS, Android, React Native, and JavaScript developers. You can use these tools to develop, deploy, test, operate, and monitor your app.

In addition to using these services and tools to develop your app, you can:
+ Take advantage of a built-in software development lifecycle
+ Host your app globally
+ Combine these tools with other AWS services for storage, caching, authorization, and other components of your app

This decision guide helps you ask the right questions to build your web or mobile app on AWS. It explores how to articulate your business requirements and guides you through the architecture and hosting decisions you’ll need to make as you use AWS services to build your app. 

[![AWS Videos](https://img.youtube.com/vi/ihEZmQsz8zE?start=168&end=452/0.jpg)](https://www.youtube.com/watch?v=ihEZmQsz8zE?start=168&end=452)


## Understand
<a name="understand"></a>

Modern web and mobile apps require high performance and an engaging user experience. In addition, you probably have your own set of business requirements that support or extend upon these common needs. Along the app lifecycle, you develop, deliver, test, and monitor your app, and engage with end users, as shown in the following image.

![Diagram showing the options available for running front-end and mobile services on AWS](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/front-end-mobile-services.png)


AWS offers a variety of services to support each stage of this lifecycle. The following provides a high-level description of these services. Later, this document guides you through choosing which services you want to use.

**What AWS services can you use to develop your app frontend?**


|  |  |  | 
| --- |--- |--- |
| [AWS Amplify](https://docs.amplify.aws/react/how-amplify-works/)<br />AWS service service for frontend developers to develop and deploy fullstack applications. Amplify provides a fully managed CI/CD and hosting service to deploy your frontend, along with libraries that make it easy to add cloud services to your app for features such as authentication, real-time data, files, and generative AI. | [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)<br />Fully managed API service that automates the operation and maintenance of GraphQL backends. | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)<br />AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs. | 

**What AWS services can you use to deliver your app frontend?**


|  | 
| --- |
| [AWS Amplify](https://docs.amplify.aws/react/how-amplify-works/)<br />Fully managed service for deploying and hosting full stack web applications, with built-in CI/CD workflows that accelerate your application release cycle. Choose from flexible deployment options, including custom pipelines, monorepos, or multiple repos. | 

**What AWS services can you use to test and monitor your app frontend?**


|  |  | 
| --- |--- |
| [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)<br />App testing service. You can test your web and mobile apps across desktop browsers and real mobile devices hosted in the AWS Cloud. | [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />AWS service that collects and visualizes logs and metrics from your app hosted in the AWS Cloud. | 

**What AWS services can you use to engage with end users?**


|  | 
| --- |
| [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html)<br />AWS service that helps you send push notifications, in-app notifications, emails, text messages, and voice messages. | 

## Consider
<a name="consider"></a>

It's important that you choose the frontend web and mobile services that best meet your needs. But how do you articulate those needs and then map them to the services that fit? The following table is designed to help you do just that.

------
#### [ Business requirements ]

To make a great choice about the services you’ll need for your app, you’ll need to answer a few questions about your business requirements first.
+ **Why are you building it?** Articulate the business need that you’re trying to meet by creating your app. This informs your choices about services. 
+ **What capabilities will your app users need?** The answer to this question might be a roadmap, where you have a minimum set of launch features and then plan for when to add new capabilities.
+ **Where will your customers be using this app?** If your users are international, you might need to offer specific features and plan for associated regulatory considerations.
+ **When and how will users need to access data from the app?** This will have implications for when and how the data is both stored and accessed.

These are just a few of the questions that you might ask to articulate your business requirements. Each answer will help you explore the other criteria involved in your choice.

------
#### [ Framework ]

**Are you developing an app for web or mobile?** Your answer will guide your choices in design and tooling. In addition, your answers to the business requirements questions on the previous tab will guide and inform your decision about which development framework you want to use.

If you are developing:
+ A **web app**, consider the frontend JavaScript framework you will be using. Common examples are React, Next.js, Vue, Angular, Astro, and Svelte.
+ A **mobile app**, your choice of framework will depend on which mobile operating system you're developing for – including popular choices such as Android, iOS, or Unity.

Your choice of framework is important, but it’s worth noting that it might actually not be a choice. In many cases, your business requirements will indicate that you need to develop for both. For example, if your app is designed to host an online store, you’ll likely want customers to be able to access it with a mobile app and on the web.

------
#### [ Hosting strategy ]

To keep your app’s asset delivery times quick, you’ll want to **host your static assets close to your users**. Consider using [AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html), a fully managed hosting service, powered by Amazon CloudFrontwith hundreds of points of presence globally, for static and server-side rendered apps. 

AWS Amplify Hosting supports:
+ Client-side rendered (single-page application), including frameworks such as React, Angular, and Vue
+ Server-side rendered (SSR), including frameworks such as Next, Nuxt, and Gatsby
+ Static site generators (SSGs), including solutions such as Gatsby, Eleventy, Hugo, VuePress, and Jekyll

------
#### [ Data querying ]

You’ll probably design an [application programming interface](https://aws.amazon.com/what-is/api/) (API) to allow users to query data for your app on AWS. You can use GraphQL or REST. The key [differences between these two approaches](https://aws.amazon.com/compare/the-difference-between-graphql-and-rest/) are:
+ **GraphQL** is an API query language that defines specifications of how a client application should request data from a remote server. For frontend development, AWS AppSync supports GraphQL.
+ **REST** enables client applications to exchange data with a server using HTTP verbs, which is the standard communication protocol of the internet. For frontend development, AWS Amplify, Amazon API Gateway, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) together support REST.

[GraphQL speeds up application development](https://aws.amazon.com/graphql/guide/) by providing a single endpoint to query and update data from multiple databases, microservices, and APIs. It can improve your performance by making fewer network requests to query data from the backend and reduces the amount of data sent to web and mobile clients.

------
#### [ Client-server communication models ]

Another key consideration is **how your client will communicate with your server**—and how quickly. Consider how often your client will request or need data, and how fresh that data needs to be. You'll likely communicate using one of two common scenarios:
+ **In real time** – If you need real-time or near real-time communication, such as with a chat app or a dashboard for monitoring IoT device health, consider using the following communication models: 
  + Constantly active WebSockets
  + Very frequent timed polling

  Keep in mind that these options require more battery life and memory usage, so they’ll probably increase your cost.
+ **Not in real time** – If it doesn’t significantly degrade usability for your users to refresh their view manually, or if you need new data loaded only on application or view entry, consider a simple **unidirectional** communication model.

Your choice will help guide you when you start looking at the capabilities of each AWS frontend web and mobile service.

------
#### [ Database services ]

Consider what kind of **database** best supports your use case. If you have flexibility in choosing your database, consider what native integrations exist with AWS services. For example, both AWS Amplify and AWS AppSync natively support integration with [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) and [Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html). Read [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html) for more information about the database options that AWS offers.

Your database selection might not be an option. If this is the case, consider how to connect your existing database to the AWS services for building and deploying your app. 

------
#### [ User profile ]

**Do you want users to have access to their data when they're offline?** If so, you might want to build offline support for the app and asynchronous data loading into the app to help users get what they need in near real time. [Amplify DataStore](https://docs.amplify.aws/lib/datastore/getting-started/), for example, provides a persistent on-device storage engine to support offline access. 

**Where will your users be located when they use your app?** Consider where your app users will need to access their data. If you plan to support users globally or in a specific locale, that information will help you plan your latency and your required points of presence.

In addition, you might consider adding geospatial data and location functionality to your app. You can use [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/welcome.html), for example, to add capabilities to your app such as maps, points of interest, geocoding, routing, geofences, and tracking.

------
#### [ Development strategy ]

When building apps on AWS, you can use a [serverless](https://aws.amazon.com/serverless/) approach or [containers](https://aws.amazon.com/containers/) approach. Overall, building serverless-first helps you harness more efficiency in the cloud, while a containers approach gives you more control. This guide focuses on a **serverless** development strategy.

Your development strategy might not be initially a choice if it’s already determined in your business requirements. If you’re planning to use a containers approach, see [Containers at AWS](https://aws.amazon.com/containers/) for resources.

------

## Choose
<a name="choose"></a>

Now that you know the criteria for evaluating your options, you're ready to choose which AWS frontend web and mobile service or services might be a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine which services might best fit your organization and use case.




- **Develop**
  - **Capabilities:** Develop your Android, iOS, or web app with features such as authentication, on-device and cloud storage, analytics, AI/ML, IoT, and notifications. Natively integrate with other AWS services. / **AWS tools and services:** [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html)
  - **Capabilities:** Use GraphQL APIs, and choose from supported frameworks and protocols. / **AWS tools and services:** [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)
  - **Capabilities:** Use REST APIs, and choose from supported frameworks and protocols. / **AWS tools and services:** [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)

- ** Deliver **
  - **Capabilities:** Deliver your app using a git-based workflow. Connect private and public repositories from GitHub, BitBucket, GitLab, and AWS CodeCommit.
  - **AWS tools and services:** [AWS Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)

- **Test and monitor**
  - **Capabilities:** Test your app by using automated testing or remote access. / **AWS tools and services:** [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
  - **Capabilities:** Monitor app health with traces, metrics, logs, alarms, and other resources. / **AWS tools and services:** [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

- ** Engage **
  - **Capabilities:** Engage with customers by designing user journeys and analyzing user behavior. / **AWS tools and services:** [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html)
  - **Capabilities:** Use maps, points of interest, geocoding, and tracking to target your audience. / **AWS tools and services:** [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/welcome.html)



## Use
<a name="use"></a>

You should now have a clear understanding of what each AWS front-end web and mobile service (and the supporting AWS tools and services) does—and which might be right for you.

To explore how to use and learn more about each of these services, we have provided a pathway to explore how they work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ AWS Amplify ]
+ **Getting started with AWS Amplify**

  Learn how to continuously build, deploy, and host a modern web app. 

  [Get started with the tutorial](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started.html)
+ **Develop your mobile or web app with Amplify Studio **

  Develop a "to-do app" that syncs app data to the cloud and take off from there. 

  [Explore the guide](https://sandbox.amplifyapp.com/getting-started)
+ **Build a GraphQL API in the Amplify Dev Center**

  Define a GraphQL schema that you can use to provision backend resources, store data locally, sync to a cloud database, as well as receive updates over a real-time subscription.

  [Get started with the tutorial](https://docs.amplify.aws/start/q/integration/ios/)
+ **Build an iOS app using a cloud-based backend**

  Create a data-driven native iOS app, integrated with a cloud-based backend. 

  [Explore the workshop](https://amplify-ios-workshop.go-aws.com/)
+ **Dive deep with the AWS Amplify Core workshop**

  Build a retail store web application in React using Amplify.

  [Explore the workshop](https://catalog.workshops.aws/amplify-core/en-US)

------
#### [ AWS AppSync ]
+ **Getting started with AWS AppSync**

  Use the AWS AppSync console to launch a sample event app schema, automatically provision a DynamoDB data source and connect resolvers, write GraphQL queries and mutations, and use the API in a sample app.

  [Explore the guide](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html)
+ **GraphQL Real-time Race workshop**

  Build a fully functioning application for a fast-paced sports event called the GraphQL Real-time Race. Connect the frontend of your application to a robust, performant cloud-enabled backend that delivers real-time updates.

  [Explore the workshop](https://pages.awscloud.com/GLOBAL_OTT_WEBINAR_2021-VW-s16-MBL-DG-OPS_GraphQL-Virtual-Workshop.html)
+ **AWS AppSync immersion day workshop**

  Manage the service in the AWS Management Console and deploy advanced functionality using the AWS Cloud Development Kit (AWS CDK).

  [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/67662c95-2007-4281-ae51-5313cd7caa67/en-US)
+ **GraphQL decision guide**

  Determine if GraphQL is right for your organization.

  [Explore the guide](https://aws.amazon.com/graphql/guide/)

------
#### [ Amazon API Gateway ]
+ **Getting started with the REST API console**

  Create a serverless REST API using the API Gateway REST API console. This exercise takes less than 20 minutes to complete, and is possible within the AWS Free Tier.

  [Explore the guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started.html)
+ **Build an API Gateway REST API with HTTP integration**

  Build an API with HTTP proxy integration or the HTTP custom integration.

  [Get started with the tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-http-integrations.html)
+ **Build an API Gateway REST API with Lambda integration**

  Build an API with Lambda proxy integration or Lambda non-proxy integration.

  [Get started with the tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)
+ **Use API Gateway for creating endpoints to support your microservices**

  [Explore the guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/api-gateway.html)

------
#### [ Amazon CloudWatch ]
+ **Getting started with Amazon CloudWatch**

  Use the CloudWatch console to see key metrics from all AWS services, and focus on specific metrics and alarms.

  [Explore the guide](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html)
+ **Analyzing log data with CloudWatch Logs Insights**

  Use CloudWatch Logs Insights to search and analyze your log data. Query for operational issues, identify potential causes, and validate deployed fixes.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
+ **Using CloudWatch anomaly detection**

  Enable anomaly detection that continuously analyzes you app's metrics, determines baselines, and surfaces anomalies with minimal user intervention.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
+ **Using Amazon CloudWatch dashboards**

  Use CloudWatch dashboards to monitor your resources in a single view, and create customized views of the metrics and alarms for your AWS resources.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)

------
#### [ AWS Device Farm ]
+ **Getting started with AWS Device Farm**

  Use AWS Device Farm to test a native Android or iOS app. Create a project, upload an `.apk` or `.ipa` file, run a suite of standard tests, and then view the results.

  [Explore the guide](https://docs.aws.amazon.com/devicefarm/latest/developerguide/getting-started.html)
+ **AWS Device Farm test devices list**

  View a list of devices available for testing on AWS Device Farm.

  [Explore the list](https://aws.amazon.com/device-farm/device-list/)
+ **Access your private network from real mobile devices using AWS Device Farm**

  Use the VPC-ENI connectivity feature of AWS Device Farm to connect to a web application that is hosted in Amazon VPC.

  [Read the blog](https://aws.amazon.com/blogs/mobile/access-your-private-network-from-real-mobile-devices-using-aws-device-farm/)

------
#### [ Amazon Location Service ]
+ **Quick start: Creating a web app**

  Create a static webpage with a map and the ability to search at a location.

  [Get started with the tutorial](https://docs.aws.amazon.com/location/latest/developerguide/qs-web.html)
+ **Creating an Android app**

  Create an Android application with a map and the ability to search at a location. 

  [Get started with the tutorial](https://docs.aws.amazon.com/location/latest/developerguide/qs-android.html)
+ **Create a Custom Map Style with Amazon Location Service**

  Style an existing map using Maputnik to help visualize the changes in real-time.

  [Read the blog](https://aws.amazon.com/blogs/mobile/create-a-custom-map-style-with-amazon-location-service/)

------
#### [ Amazon Pinpoint ]
+ **Getting started with Amazon Pinpoint**

  Start sending targeted messages in Amazon Pinpoint, including creating segments that target certain customers and using analytics dashboards.

  [Explore the guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/gettingstarted.html)
+ **Using Postman with the Amazon Pinpoint API**

  Set up and use Postman with Amazon Pinpoint. Postman is a popular tool for testing APIs in an easy-to-use graphical environment.

  [Get started with the tutorial](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tutorials-using-postman.html)
+ **Setting up an SMS registration system**

  Set up a web form to capture customers' contact information. Amazon Pinpoint then sends the customer a message asking them to confirm their subscription and opts them in to receiving your messages.

  [Get started with the tutorial](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tutorials-two-way-sms.html)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you develop, scale, test, and deploy your front-end and mobile applications.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23mobile&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your front-end and mobile applications options on AWS.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23mobile&awsf.industries=*all&awsf.business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for front-end and mobile applications.

  [Explore solutions](https://aws.amazon.com/solutions/app-development/?nc=sn&loc=3&dn=ad)

# Machine Learning
<a name="machine-learning"></a>

The following decision guides help you choose AWS services for generative AI, machine learning, and foundation models.

**Topics**
+ [Choosing a generative AI service](#genai-guide)
+ [Choosing an AWS machine learning service](#ml-guide)
+ [Amazon Bedrock or Amazon SageMaker AI?](#bedrock-or-sagemaker)

## Choosing a generative AI service
<a name="genai-guide"></a>

**Taking the first step** 


|  |  | 
| --- |--- |
|  Purpose  |  Determine which AWS generative AI services are the best fit for your organization.  | 
|  Last updated  |  February 14, 2025  | 
|  Covered services  |  +   [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)  <br />+   [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html)  <br />+   [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)  <br />+   [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html.html) <br />+   [Amazon Nova foundation models](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html) <br />+  [Amazon Titan foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html)  <br />+   [Public foundation models](https://aws.amazon.com/what-is/foundation-models/) <br />+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) <br />+   [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)   | 

### Introduction
<a name="introduction"></a>

Generative AI is a set of artificial intelligence (AI) systems and models designed to generate content such as code, text, images, music, or other forms of data. These systems can produce new content based on patterns and knowledge learned from existing data. Increasingly, organizations and businesses are using generative AI to:
+  **Automate creative workflows** — Use generative AI services to automate the workflows of time-consuming creative processes such as writing, image or video creation, and graphic design. 
+  **Customize and personalize content** — Generate targeted content, product recommendations, and customized offerings for an audience-specific context. 
+  **Augment data** — Synthesize large training datasets for other ML models to *unlock* scenarios where human-labeled data is scarce. 
+  **Reduce cost** — Potentially lower costs by using synthesized data, content, and digital assets.
+  **Faster experimentation** — Test and iterate on more content variations and creative concepts than would be possible manually. 

 This guide helps you select the AWS generative AI services and tools that are the best fit for your needs and your organization. 

[![AWS Videos](https://img.youtube.com/vi/WEKTpzvJiec?si=39jHcyiMGTfiO2zB/0.jpg)](https://www.youtube.com/watch?v=WEKTpzvJiec?si=39jHcyiMGTfiO2zB)


### Understand
<a name="understand"></a>

Amazon offers a range of generative AI services, applications, tools, and supporting infrastructure. Which of these you use depends a lot on the following factors:
+ What you’re trying to do
+ How much choice you need in the foundation models that you use
+ The degree of customization you need in your generative AI applications
+ The expertise within your organization



![Diagram showing the AWS generative AI stack. This diagram shows the infrastructure to build and train AI models at the bottom of the stack, models and tools to build generative AI apps in the middle, and applications that use LLMs and other FMs to boost productivity, at the top.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/gen-ai-stack-dec-2024.png)


 **Amazon Q Business and Amazon Q Developer— Applications to boost productivity** 

At the top of Amazon's generative AI stack, Amazon Q Business and Amazon Q Developer use large language models (LLMs) and foundation models. However, they don’t require that you explicitly choose a model. Each of these applications support different use cases, and all are powered by [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html). 

 Learn more about the primary generative AI–powered assistants currently available: 

------
#### [ Amazon Q Business ]

[Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) can answer questions, provide summaries, generate content, and securely complete tasks based on the data in your enterprise systems. It supports the general use case of using generative AI to start making the most of the information in your enterprise. With Amazon Q Business, you can make English-language queries about that information. It provides responses in a manner appropriate to your team’s needs. In addition, you can create lightweight, purpose-built [Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html) within your Amazon Q Business Pro subscription.

------
#### [ Amazon Q Developer ]

With [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html), you can understand, build, extend, and operate AWS applications. The supported use cases include tasks that range from coding, testing, and upgrading applications, to diagnosing errors, performing security scanning and fixes, and optimizing AWS resources. The advanced, multistep planning and reasoning capabilities in Amazon Q Developer are aimed at reducing the work involved in common tasks (such as performing Java version upgrades). These capabilities can also help implement new features generated from developer requests. 

Amazon Q Developer features are available as part of your workflows in [other AWS services](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/features.html), including Amazon Q Developer in chat applications, Amazon CodeCatalyst, Amazon EC2, AWS Glue, and VPC Reachability Analyzer.

[Chat with Amazon Q Developer](https://aws.amazon.com/blogs/devops/chat-about-your-aws-account-resources-with-amazon-q-developer/) to query and explore your AWS infrastructure directly from the AWS Management Console. Using natural language prompts to interact with your AWS account, you can get specific resource details and ask about relationships between resources.

------
#### [ Amazon Q in Quick ]

 [Amazon Q in Quick](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-gen-bi.html) is aimed at meeting the needs of a specific use case: getting actionable insights from your data by connecting Amazon Q to the Amazon Q Quick business intelligence (BI) service. You can use it to build visualizations of your data, summarize insights, answer data questions, and build data stories using natural language.

------
#### [ Amazon Q in Connect ]

 [Amazon Q in Connect](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-q-connect.html) can automatically detect customer issues. It provides your customer service agents with contextual customer information along with suggested responses and actions for faster resolution of issues. It combines the capabilities of the [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html) cloud contact center service with Amazon Q. Amazon Q in Connect can use your real-time conversations with your customers, along with relevant company content, to recommend what to say or what actions an agent should take to assist customers.

------

**Amazon Bedrock — Build and scale your generative AI application with FMs**

If you're developing custom AI applications, need access to multiple foundation models, and want more control over the AI models and outputs, then [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) could be the service that meets your needs. Amazon Bedrock is a fully managed service for building generative AI applications, with support for  [popular foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html), including [Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), [Amazon Titan](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html), [Anthropic Claude](https://aws.amazon.com/bedrock/claude/), [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1), [Cohere Command & Embed](https://aws.amazon.com/bedrock/cohere-command-embed/), [AI21 Labs Jurassic](https://aws.amazon.com/bedrock/jurassic/), [Meta Llama](https://aws.amazon.com/bedrock/llama/), [Mistral AI](https://aws.amazon.com/bedrock/mistral/), and [Stable Diffusion XL](https://aws.amazon.com/bedrock/stable-diffusion/).

Use the [ Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to discover, test, and use over 100 popular, emerging, and specialized FMs. [Supported FMs](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) are updated on a regular basis. 

![Diagram showing Amazon Bedrock's broad choice of models, from Amazon and leading model providers.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/amazon-bedrock-models-feb-2025.jpg)


In addition, Amazon Bedrock provides what you need to build generative AI applications with security, privacy, and responsible AI—regardless of the foundation model you choose. It also offers model-independent, single API access and the flexibility to use different foundation models and upgrade to the latest model versions, with minimal code changes.

 Learn more about the key features of Amazon Bedrock: 

------
#### [ Model customization ]

 [Model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) can deliver differentiated and personalized user experiences. To customize models for specific tasks, you can privately fine-tune FMs using your own labeled datasets. Custom models include capabilities such as fine-tuning and continued pre-training using unlabeled datasets. The list of FMs for which Amazon Bedrock supports fine-tuning includes Amazon Nova Micro, Lite, and Pro, Anthropic Claude 3 Haiku, Cohere Command, Meta Llama 2, Amazon Titan Text Lite and Express, Amazon Titan Multimodal Embeddings, and Amazon Titan Image Generator. The list of supported FMs is updated on an ongoing basis. 

In addition, you can use [Amazon Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) to bring your own custom models and use them within Amazon Bedrock. 

------
#### [ Knowledge Bases ]

[Amazon Bedrock Knowledge Bases ](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is a fully managed capability that you can use to implement the entire Retrieval Augmented Generation (RAG) workflow—from ingestion to retrieval and prompt augmentation—without having to build custom integrations to data sources, and manage data flows. Session context management is built in, so your application can support multi-turn conversations. You can use the Retrieve API to fetch relevant results for a user query from knowledge bases.

With RAG, you can provide a model with new knowledge or up-to-date info from multiple sources, including document repositories, databases, and APIs. For example, the model might use RAG to retrieve search results from Amazon OpenSearch Service or documents from Amazon Simple Storage Service. Amazon Bedrock Knowledge Bases fully manages this experience by connecting to your private data sources, including [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/), MongoDB, Pinecone, and Redis Enterprise Cloud. This list includes connectors for Salesforce, Confluence, and SharePoint (in preview), so you can access more business data to customize models for your specific needs. 

------
#### [ Agents ]

 [Amazon Bedrock Agents ](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) helps you plan and create multistep tasks using company systems and data sources—from answering customer questions about your product availability to taking their orders. You can create an agent by first selecting an FM and then providing it access to your enterprise systems, knowledge bases, and AWS Lambda functions to run your APIs securely. An agent analyzes the user request, and a Lambda function or your application can automatically call the necessary APIs and data sources to fulfill the request.

Agents [can retain memory](https://aws.amazon.com/blogs/aws/agents-for-amazon-bedrock-now-support-memory-retention-and-code-interpretation-preview/) across multiple interactions to remember where you last left off and provide better recommendations based on prior interactions. Agents can also interpret code to tackle complex data-driven use cases, such as data analysis, data visualization, text processing, solving equations, and optimization problems.

------
#### [ Guardrails ]

[Amazon Bedrock Guardrails ](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) evaluates user inputs and FM responses based on use case specific policies, and provides an additional layer of safeguards, regardless of the underlying FM. Using a short natural language description, you can use Amazon Bedrock Guardrails to define a set of topics to avoid within the context of your application. Guardrails detects and blocks user inputs and FM responses that fall into the restricted topics.

Guardrails supports [contextual grounding checks](https://aws.amazon.com/blogs/aws/guardrails-for-amazon-bedrock-can-now-detect-hallucinations-and-safeguard-apps-built-using-custom-or-third-party-fms/), to detect hallucinations in model responses for applications using Retrieval Augmented Generation (RAG) and summarization applications. Contextual grounding checks add to the safety protection in Guardrails to make sure the LLM response is based on the right enterprise source data, and evaluates the LLM response to confirm that it’s relevant to the user’s query or instruction. Contextual grounding checks can detect and filter over 75% hallucinated responses for RAG and summarization workloads. 

------
#### [ Converse API ]

Use the [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) to create conversational applications that send and receive messages to and from an Amazon Bedrock model. For example, you can create a chatbot that maintains a conversation over many turns and uses a persona or tone customization that is unique to your needs, such as a helpful technical support assistant. 

------
#### [ Tool use (function calling) ]

[Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) gives a model access to tools that can help it generate responses for messages that you send to the model. For example, you might have a chat application that lets users find out the most popular song played on a radio station. To answer a request for the most popular song, a model needs a tool that can query and return the song information. 

------
#### [ Amazon Bedrock IDE ]

Use [Amazon Bedrock IDE](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html), a development experience in Amazon SageMaker Unified Studio (in preview), that lets you discover Amazon Bedrock models and build generative AI apps that use Amazon Bedrock models and features. For example, you can use a chat playground to try a [prompt](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/explore-prompts.html) with an Anthropic Claude model without having to write any code. Later, you can use Amazon Bedrock IDE to create a generative AI app that uses an Amazon Bedrock model and features, such as a knowledge base or a guardrail, again without having to write any code.

------
#### [ Prompt management ]

Use Amazon Bedrock to create and save your own prompts using [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html), so that you can save time by applying the same prompt to different workflows. When you create a prompt, you can select a model to run inference on it and modify the inference parameters to use. You can include variables in the prompt so that you can adjust the prompt for different use case.

------
#### [ Prompt flows ]

[Prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) for Amazon Bedrock offers the ability for you to use supported FMs to build workflows by linking prompts, foundational models, and other AWS services to create comprehensive solutions.

With prompt flows, you can quickly build complex generative AI workflows using a visual builder. You can integrate with Amazon Bedrock offerings such as FMs, knowledge bases, and other AWS services such as AWS Lambda by transferring data between them. You can also deploy immutable workflows to move from testing to production in few clicks.

------

**Amazon SageMaker AI (formerly Amazon SageMaker) — Build custom models and control the full ML lifecycle, from data preparation to model deployment and monitoring**

With [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), you can build, train, and deploy machine learning models, including FMs, at scale. Consider this option when you have use cases that can benefit from extensive training, fine-tuning, and customization of foundation models. It also streamlines the sometimes-challenging task of evaluating which FM is the best fit for your use case.

Amazon SageMaker AI also provides infrastructure and purpose-built tools for use throughout the ML lifecycle, including integrated development environments (IDEs), distributed training infrastructure, governance tools, machine learning operations (MLOps) tools, inference options and recommendations, and model evaluation.

![Diagram that provides an overview of SageMaker AI's key features, including access to foundatio models (FMs), building and customizing FMs, running inference, and implementing FMOps and governance](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/sagemaker-ai-overview.jpg)


Use [Amazon SageMaker Partner AI Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html) to access generative AI and machine learning (ML) development applications built, published, and distributed by industry-leading application providers. Partner AI Apps are certified to run on SageMaker AI. With Partner AI Apps, you can improve how you build solutions based on foundation models (FM) and classic ML models without compromising the security of your sensitive data. The data stays completely within your trusted security configuration and is never shared with a third party.

SageMaker AI is part of the next generation of Amazon SageMaker, which includes:
+ [Amazon SageMaker Unified Studio ](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html) (in preview), a unified development experience that brings together AWS data, analytics, artificial intelligence (AI), and machine learning (ML) services.
+ AWS tools for complete development workflows, including model development, generative AI app development, data processing, and SQL analytics, in a single governed environment. Create or join projects to collaborate with your teams, securely share AI and analytics artifacts, and access your data stored in Amazon Simple Storage Service (Amazon S3), Amazon Redshift, and more data sources through the [Amazon SageMaker Lakehouse](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/lakehouse.html).

Explore key features of SageMaker AI that may help you determine when to use it:

------
#### [ Amazon SageMaker JumpStart ]

[Amazon SageMaker JumpStart ](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) is an ML hub that provides access to publicly available foundation models. Those models include Mistral, Llama 3, CodeLlama, and Falcon 2. They can be customized with advanced fine-tuning and deployment techniques such as Parameter Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA). 

This following screenshot shows some of the available models in Amazon SageMaker JumpStart within the AWS Management Console. 

![Diagram showing Amazon SageMaker JumpStart in the AWS Management Console, including a broad choice of models from Amazon and leading model providers.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/sagemaker-jumpstart-console.jpg)


------
#### [ Amazon SageMaker Clarify ]

 [Amazon SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate.html) addresses the all-important decision of which foundation model to use. Use Amazon SageMaker Clarify to create model evaluation jobs. A model evaluation job evaluates and compares model quality and responsibility metrics for text-based foundation models from JumpStart. Model evaluation jobs also support the use of JumpStart models that have already been deployed to an endpoint. 

------
#### [ Amazon SageMaker Canvas ]

With [Amazon SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html), you can use machine learning to generate predictions without writing any code. You can also use Amazon SageMaker Canvas in collaboration with Amazon Bedrock to fine-tune and deploy language models.

[This blog post](https://aws.amazon.com/blogs/machine-learning/fine-tune-and-deploy-language-models-with-amazon-sagemaker-canvas-and-amazon-bedrock/) describes how you can use them to optimize customer interaction by working with your own datasets (such as your product FAQs) in Amazon Bedrock and Amazon SageMaker JumpStart The following diagram, from this blog post, demonstrates how Amazon SageMaker Canvas and Amazon Bedrock can be used together to fine-tune and deploy language models. 

![Diagram showing Amazon SageMaker Canvas and Amazon Bedrock used together to fine-tune and deploy language models.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/sagemaker-bedrock-scenario.jpg)


------
#### [ Amazon SageMaker Studio ]

Amazon SageMaker Studio is a web-based experience for running ML workflows. Studio offers a suite of integrated development environments (IDEs). These include Code Editor, based on Code-OSS, Visual Studio Code - Open Source, a new JupyterLab application, RStudio, and Amazon SageMaker Studio Classic. For more information, see [Applications supported in Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html).

The web-based UI in Studio provides access to all SageMaker AI resources, including jobs and endpoints, in one interface. ML practitioners can also choose their preferred IDE to accelerate ML development. A data scientist can use JupyterLab to explore data and tune models. In addition, a machine learning operations (MLOps) engineer can use Code Editor with the pipelines tool in Studio to deploy and monitor models in production.

Amazon SageMaker Studio includes generative AI assistance, powered by Amazon Q Developer right within your JupyterLab Integrated Development Environment (IDE). With Q Developer, you can access expert guidance on SageMaker AI features, code generation, and troubleshooting.

------

 **Infrastructure to build and train AI models** 

 AWS offers specialized, accelerated hardware for high performance ML training and inference. 
+ AWS Trainium2-powered [Amazon EC2 Trn2 instances](https://aws.amazon.com/ec2/instance-types/trn2/) and Trn2 UltraServers deliver the highest performance for AI training and inference on AWS.
+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) is the second-generation ML accelerator that AWS has purpose-built for deep learning (DL) training of 100B\+ parameter models. 
+  [AWS Inferentia2-based Amazon EC2 Inf2 instances](https://aws.amazon.com/machine-learning/inferentia/) are designed to deliver high performance at the lowest cost in Amazon EC2 for your DL and generative AI inference applications. 
+  [Amazon EC2 P5 and P5e](https://aws.amazon.com/ec2/instance-types/p5/) instances, powered by NVIDIA H100 and NVIDIA H200 Tensor Core GPUs, which are well-suited for both training and inference tasks in machine learning. 
+  [Amazon EC2 G6e](https://aws.amazon.com/ec2/instance-types/g6e/) instances feature up to 8 NVIDIA L40S Tensor Core GPUs, and third generation AMD EPYC processors, for a wide range of graphics-intensive and machine learning use cases.

### Consider
<a name="consider"></a>

After you've decided on a generative AI service, choose the foundation model (FM) that gives you the best results for your use case. 

Amazon Bedrock has a [ model evaluation capability](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html) that can assist in evaluating, comparing, and selecting the best FMs for your use case.

 Here are some critical factors to consider when choosing an appropriate FM for your use case: 

------
#### [ Modality ]

**Identify use cases/modality** 

**What it is:** Modality refers to the type of data the model processes: text, images (vision), or embeddings. 

**Why it matters:** The choice of modality should align with the data that you're working with. For example, if your project involves processing natural language, a text-based model like Claude, Llama 3.1, or Titan Text G1 is suitable. If you want to create embeddings, then you might use a model like [Titan Embeddings G1](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html). Similarly, for image-related tasks, models such as Stable Diffusion XL, and Titan Image Generator v2, are more appropriate. Your use case might also involve considering your data source and the support for data source connectors, such as [those provided in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-connectors.html). 

------
#### [ Model size ]

**Model Size** 

**What it is:** This criterion refers to the number of parameters in a model. A *parameter* is a configuration variable that is internal to the model. Its values can be estimated (trained) during the training phase from the given training data. Parameters are crucial as they directly define the model's capability to learn from data. Large models often have more than 50 billion parameters. 

**Why it matters:** The number of parameters is a key indicator of the model's complexity. More parameters mean that the model can capture more intricate patterns and nuances in the data, which generally leads to better performance. However, these models are not only expensive to train, but also require more computational resources to operate. 

------
#### [ Inference latency ]

**Inference latency** 

**What it is:** *Inference speed*, or *latency*, is the time it takes for a model to process input (often measured in tokens) and return an output. This processing time is crucial when the model's responses are part of an interactive system, like an Amazon Q Developer in chat applications. 

**Why it matters:** Quick response times are essential for real-time applications such as interactive chatbots or *instant translation* services. These applications depend on the model's ability to process and respond to prompts rapidly to maintain a smooth user experience. Although larger FMs typically offer more detailed and accurate responses, their complex architectures can lead to slower inference speeds. This slower processing might frustrate users expecting immediate interaction. 

To address this challenge, you can choose models optimized for quicker responses, even if it means compromising somewhat on the responses' depth or accuracy. 

------
#### [ Context window ]

**Maximizing context window** 

**What it is:** A large language model's *context window* is the amount of text (in tokens) that the model can consider at any one time when generating responses. 

**Why it matters:** Larger context windows enable the model to remember and process more information in a single run. This ability is particularly valuable in complex tasks such as understanding long documents, engaging in detailed conversations, or generating contextually accurate text over larger spans. 

For example, in a conversation, a model with a larger context window can remember more of the earlier dialogue, and provide responses that are more relevant to the entire conversation. This leads to a more natural and satisfying user experience, as the model can maintain the thread of discussion without losing context. 

------
#### [ Pricing ]

**Pricing considerations** 

**What it is:** The cost of using an FM is influenced by the model's complexity and the model provider’s pricing structure. 

**Why it matters:** Deploying high-performance models often comes with high costs due to increased computational needs. While these models provide advanced capabilities, their operational expenses can be high, particularly for startups or smaller projects on tight budgets. 

Smaller, less resource-intensive models offer a more budget-friendly option without significantly compromising performance. Weigh the model’s cost against its benefits to ensure it fits within your project's financial constraints and gets you the best value for your investment. 

------
#### [ Fine-tuning ]

**Fine-tuning and continuous pre-training capability** 

**What it is:** Fine-tuning is a specialized training process in which a pre-trained model that has been trained on a large, generic dataset is further trained (or fine-tuned) on a smaller, specific dataset. This process adapts the model to particularities of the new data, improving its performance on related tasks. Continuous pre-training, on the other hand, involves extending the initial pre-training phase with additional training on new, emerging data that wasn't part of the original training set, helping the model stay relevant as data evolves. You can also use [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) to retrieve data from outside an FM and augment your prompts by adding the relevant retrieved data in context. 

**Why it matters:** With fine-tuning, you can increase model accuracy by providing your own task-specific labeled training dataset and further specialize your FMs. With continued pre-training, you can train models using your own unlabeled data in a secure and managed environment. Continuous pre-training helps models become more domain-specific by accumulating more robust knowledge and adaptability beyond their original training. 

------
#### [ Data quality ]

**Data quality** 

Data quality is a critical factor in the success of a generative AI application. Consider the following quality factors: 
+ **Relevance:** Ensure that the data you use for training your generative AI model is relevant to your application. Irrelevant or noisy data can lead to poor model performance. 
+ **Accuracy:** The data should be accurate and free from errors. Inaccurate data can mislead your model and result in incorrect outputs. 
+ **Consistency:** Maintain consistency in your data. Inconsistencies in the data can confuse the model and hinder its ability to learn patterns. 
+ **Bias and fairness:** Be aware of biases in your data, as they can lead to biased model outputs. Take steps to mitigate bias and help ensure fairness in your generative AI system. 
+ **Annotation and labeling:** If your application requires labeled data, verify that the annotations or labels are of high quality and created by experts. 
+ **Data preprocessing:** Prepare your data by cleaning and preprocessing it. This might involve text tokenization, image resizing, or other data-specific transformations to make it suitable for training. 

------
#### [ Data quantity ]

**Data quantity** 

 Quantity along with quality goes hand in hand. Consider the following quantity factors: 
+ **Sufficient data:** In most cases, more data is better. Larger datasets allow your model to learn a wider range of patterns and generalize better. However, the required amount of data can vary depending on the complexity of your application. 
+ **Data augmentation:** If you have limitations on the quantity of available data, consider data augmentation techniques. These techniques involve generating additional training examples by applying transformations to existing data. For example, you can rotate, crop, or flip images or paraphrase text to create more training samples. 
+ **Balancing data:** Ensure that your dataset is balanced, especially if your generative AI application is expected to produce outputs with equal representation across different categories or classes. Imbalanced datasets can lead to biased model outputs. 
+ **Transfer learning:** For certain applications, you can use pre-trained models. With transfer learning, you can use models that were trained on massive datasets and fine-tune them with your specific data, often requiring less data for fine-tuning. 

It's also important to continuously monitor and update your dataset as your generative AI applications evolve and as new data becomes available. 

------
#### [ Quality of response ]

**Quality of response** 

**What it is:** The most essential criterion is the quality of response. This is where you evaluate the output of a model based on several quality metrics, including accuracy, relevance, toxicity, fairness, and robustness against adversarial attacks. 
+ *Accuracy* measures how often the model's responses are correct (and you would typically measure this against a pre-configured standard or baseline). 
+ *Relevance* assesses how appropriate the responses are to the context or question posed. 
+ *Toxicity* checks for harmful biases or inappropriate content in the model's outputs. 
+ *Fairness* evaluates whether the model's responses are unbiased across different groups. 
+ *Robustness* indicates how well the model can handle intentionally misleading or malicious inputs designed to confuse it. 

**Why it matters:** The reliability and safety of model outputs are paramount, especially in applications that interact directly with users or make automated decisions that can affect people's lives. High-quality responses ensure user trust and satisfaction, reducing the risk of miscommunication and enhancing the overall user experience, thus earning the trust of your customers. 

------

### Choose
<a name="choose"></a>


|  Generative AI category  |  What is it optimized for?  |  Generative AI services  | 
| --- | --- | --- | 
| Amazon Q | Generating code and providing responses to questions across business data by connecting to enterprise data repositories to summarize the data logically, analyze trends, and engage in dialogue about the data. |  [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) <br /> [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)  | 
| Amazon Bedrock | Offering a choice of foundation models, customizing them with your own data, and building generative AI applications with the builder tools that Amazon Bedrock offers. | [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)<br />[Amazon Bedrock IDE](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html)<br />[Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)<br />[Amazon Titan](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html) | 
| Amazon SageMaker AI | Building, training, and deploying machine learning models, including foundation models, at scale. | [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html) | 
| Infrastructure for FM training and inference | Offering services that maximize the price performance benefits in FM training and inference. |  [AWS Trainium](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html) <br /> [AWS Inferentia](https://docs.aws.amazon.com/eks/latest/userguide/inferentia-support.html)  | 

### Use
<a name="use"></a>

Now that we've covered the criteria you need to apply in choosing an AWS generative AI service, you can select which services are optimized for your needs and explore how you might get started using each of them. 

------
#### [ Amazon Q Business ]
+ **What is Amazon Q Business?** 

  Get an overview of Amazon Q Business, with explanations of what it is, how it works, and how to get started using it. 

   [Explore the guide](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html)

  
+ **Create an Amazon Q Business application** 

  Learn how to create your first Amazon Q Business application in either the AWS Management Console or using the command line interface (CLI). 

  [Explore the guide](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-app.html)

  
+ **Combine Amazon Q Business and AWS IAM Identity Center to build generative AI apps** 

  Build private and secure enterprise generative AI apps with Amazon Q Business and AWS IAM Identity Center. 

   [Read the blog post](https://aws.amazon.com/blogs/machine-learning/build-private-and-secure-enterprise-generative-ai-apps-with-amazon-q-business-and-aws-iam-identity-center/)

  

------
#### [ Amazon Q Developer ]
+ **What is Amazon Q Developer?** 

  Get an overview of Amazon Q Developer, with explanations of what it is, how it works, and how to get started using it. 

   [Explore the guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)

  
+ **Understanding tiers of service for Amazon Q Developer** 

  Review the following information to understand the tiers of service for Amazon Q Developer, including Amazon Q Developer Pro and Amazon Q Developer at the free tier.

   [Explore the guide](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-tiers.html)

  
+ **Working with agentic AI** 

  Use the Builder Center for fast access to key articles, blog posts, videos, and tips on building, deploying, and scaling AI agents with AWS. 

   [Explore agentic AI in the Builder Center](https://aws.amazon.com/developer/generative-ai/amazon-q/)

  

------
#### [ Amazon Bedrock ]
+ **What is Amazon Bedrock?** 

  Learn how to use this fully managed service to make foundation models (FMs) from Amazon and third parties available for your use through a unified API. 

   [Explore the guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

  
+ **Frequently asked questions about Amazon Bedrock** 

  Get answers to the most commonly-asked questions about Amazon Bedrock, including how to use agents, security considerations, details on Amazon Bedrock software development kits (SDKs), Retrieval Augmented Generation (RAG), how to use model evaluation, and how billing works. 

   [Read the FAQs](https://aws.amazon.com/bedrock/faqs/)

  
+ **Guidance for generating product descriptions with Amazon Bedrock** 

  Learn how to use Amazon Bedrock as part of a solution to automate your product review and approval process for an ecommerce marketplace or retail website. 

   [Explore the solution](https://aws.amazon.com/solutions/guidance/generating-product-descriptions-with-amazon-bedrock/)

  

------
#### [ Amazon Bedrock in SageMaker Unified Studio ]

**Note**  
Amazon Bedrock IDE is renamed to Amazon Bedrock in SageMaker Unified Studio.
+  **What is Amazon Bedrock in SageMaker Unified Studio?** 

   Use this IDE to discover Amazon Bedrock models, and build generative AI apps that use Amazon Bedrock models and features.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html) 

  
+  **Build generative AI applications with Amazon Bedrock in SageMaker Unified Studio** 

  This blog post describes how you can build applications using a wide array of top performing models. It then explains how to evaluate and share your generative AI apps with Amazon Bedrock IDE.

   [Read the blog](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-quickly-with-amazon-bedrock-ide-in-amazon-sagemaker-unified-studio/) 

  
+  **Building a chat app with Amazon Bedrock in SageMaker Unified Studio** 

  Build a chat agent app that allows users to chat with an Amazon Bedrock model through a conversational interface.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-chat-app.html) 

  

------
#### [ Amazon SageMaker AI ]
+ **What is Amazon SageMaker AI?** 

  Learn how you can use this fully managed machine learning (ML) service to build, train, and deploy ML models into a production-ready hosted environment. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

  
+ **Get started with Amazon SageMaker AI** 

  Learn how to join an Amazon SageMaker AI domain, giving you access to Amazon SageMaker AI Studio and RStudio on SageMaker AI. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)

  
+ **Get started with Amazon SageMaker JumpStart** 

  Explore Amazon SageMaker JumpStart solution templates that set up infrastructure for common use cases, and executable example notebooks for machine learning with SageMaker AI. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

  

------
#### [ Amazon SageMaker Unified Studio ]
+ **What is Amazon SageMaker Unified Studio?** 

  Learn how you can use Amazon SageMaker Unified Studio (in preview) to build, deploy, execute, and monitor workflows from a single interface.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html)

  
+ **An integrated experience for all your data and AI with Amazon SageMaker Unified Studio** 

  Learn about the new Amazon SageMaker Unified Studio and explore how it unifies your analytic workloads.

   [Read the blog post](https://aws.amazon.com/blogs/big-data/an-integrated-experience-for-all-your-data-and-ai-with-amazon-sagemaker-unified-studio-preview/)

  
+ **Get started with Amazon SageMaker Unified Studio** 

  Learn how to gain access to Amazon SageMaker Unified Studio, create a project, and then add members to the project and use the sample JupyterLab notebook to begin building with a variety of tools and resources.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html)

  

------
#### [ Amazon Nova ]
+ **What is Amazon Nova?** 

  Explore Amazon Nova, a new generation of foundation models available on Amazon Bedrock.

   [Explore the guide](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)

  
+ **Introducing Amazon Nova foundation models: Frontier intelligence and industry leading price performance** 

  Learn about the new Amazon Nova models, including examples of using Amazon Nova models to analyze complex documents and videos, understand charts and diagrams, generate engaging video content, and build sophisticated AI agents.

   [Read the blog post](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/)

  
+ **Get started with Amazon Nova in the Amazon Bedrock console** 

  Learn how to use the playgrounds in the AWS Management Console to submit a text prompt to Amazon Nova models and generate a text or image response

   [Explore the guide](https://docs.aws.amazon.com/nova/latest/userguide/getting-started-console.html)

  

------
#### [ Amazon Titan ]
+ **Amazon Titan in Amazon Bedrock overview** 

  Get an overview of Amazon Titan foundation models (FMs) to support your use cases.

   [Explore the guide](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html)

  
+ **Cost-effective document classification using the Amazon Titan Multimodal Embeddings Model** 

  Learn how you can use this model to categorize and extract insights from high volumes of documents of different formats. This blog explores how you can use it to help determine the next set of actions to take, depending on the type of document. 

   [Read the blog post](https://aws.amazon.com/blogs/machine-learning/cost-effective-document-classification-using-the-amazon-titan-multimodal-embeddings-model/)

  
+ **Build generative AI applications with Amazon Titan Text Premier, Amazon Bedrock, and AWS CDK** 

  Explore building and deploying two sample applications powered by Amazon Titan Text Premier in this blog post. 

   [Read the blog post](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-with-amazon-titan-text-premier-amazon-bedrock-and-aws-cdk/)

  

------
#### [ AWS Trainium ]
+ **Overview of AWS Trainium** 

  Learn about AWS Trainium, the second-generation machine learning (ML) accelerator that AWS purpose built for deep learning training of 100B\+ parameter models. Each Amazon EC2 Trn1 instance deploys up to 16 AWS Trainium accelerators to deliver a high-performance, low-cost solution for deep learning (DL) training in the cloud. 

   [Explore the guide](https://aws.amazon.com/machine-learning/trainium/)

  
+ **Recommended Trainium Instances** 

  Explore how AWS Trainium instances are designed to provide high performance and cost efficiency for deep learning model inference workloads. 

   [Explore the guide](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html)

  
+ **Scaling distributed training with AWS Trainium and Amazon EKS** 

  If you're deploying your deep learning (DL) workloads using Amazon Elastic Kubernetes Service (Amazon EKS), learn how you can benefit from the general availability of Amazon EC2 Trn1 instances powered by AWS Trainium—a purpose-built ML accelerator optimized to provide a high-performance, cost-effective, and massively scalable platform for training DL models in the cloud. 

   [Read the blog post](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/)

  

------
#### [ AWS Inferentia ]
+ **Overview of AWS Inferentia** 

  Understand how AWS designs accelerators to deliver high performance at the lowest cost for your deep learning (DL) inference applications.   

   [Explore the guide ](https://aws.amazon.com/machine-learning/inferentia/)

  
+ **AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency** 

  Understand what AWS Inferentia2 is optimized for and how it was designed to deliver higher performance, while lowering the cost of LLMs and generative AI inference. 

   [Read the blog post](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/)

  
+ **Machine learning inference using AWS Inferentia** 

  Learn how to create an Amazon EKS cluster with nodes running Amazon EC2 Inf1 instances and optionally deploy a sample application. Amazon EC2 Inf1 instances are powered by AWS Inferentia chips, which are custom built by AWS to provide high-performance and low-cost inference in the cloud. 

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/inferentia-support.html)

  

------

### Explore
<a name="explore"></a>
+  **Architecture diagrams** 

   These reference architecture diagrams show examples of AWS AI and ML services in use. 

   [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

  
+  **Whitepapers** 

   Explore whitepapers to help you get started and learn best practices in choosing and using AI and ML services. 

  [ Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

  
+  **AWS solutions** 

   Explore vetted solutions and architectural guidance for common use cases for AI and ML services. 

   [ Explore solutions](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

  

### Resources
<a name="resources"></a>

 **Public foundation models** 

Supported foundation models are updated on a regular basis, and currently include:
+ [Anthropic Claude](https://aws.amazon.com/bedrock/claude/)
+ [Cohere Command & Embed](https://aws.amazon.com/bedrock/cohere-command-embed/)
+ [AI21 Labs Jurassic](https://aws.amazon.com/bedrock/jurassic/)
+ [Meta Llama](https://aws.amazon.com/bedrock/llama/)
+ [ Mistral AI](https://aws.amazon.com/bedrock/mistral/)
+ [Stable Diffusion XL ](https://aws.amazon.com/bedrock/stable-diffusion/)
+ [Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/)
+ [Amazon Titan](https://aws.amazon.com/bedrock/titan/)

Use Amazon Bedrock and Amazon SageMaker AI to experiment with a variety of foundation models, and privately customize them with your data. To explore generative AI quickly, you also have the option of using [PartyRock, an Amazon Bedrock Playground](https://partyrock.aws/). PartyRock is a generative AI app building playground with which you can experiment hands-on with prompt engineering. 

 **Associated blog posts** 
+  [ Build private and secure enterprise generative AI apps with Amazon Q Business and IAM Identity Center](https://aws.amazon.com/blogs/machine-learning/build-private-and-secure-enterprise-generative-ai-apps-with-amazon-q-business-and-aws-iam-identity-center/) 
+  [ Amazon Q Developer, now generally available, includes previews of new capabilities to reimagine developer experience](https://aws.amazon.com/blogs/aws/amazon-q-developer-now-generally-available-includes-new-capabilities-to-reimagine-developer-experience/) 
+  [ Chat about your AWS account resources with Amazon Q Developer](https://aws.amazon.com/blogs/devops/chat-about-your-aws-account-resources-with-amazon-q-developer/) 
+  [ Build enterprise-grade applications with natural language using AWS App Studio (preview)](https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview/) 
+  [ Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/) 
+  [ Build generative AI applications with Amazon Bedrock Studio (preview)](https://aws.amazon.com/blogs/aws/build-generative-ai-applications-with-amazon-bedrock-studio-preview/) 
+  [ Fine-tune and deploy language models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/fine-tune-and-deploy-language-models-with-amazon-sagemaker-canvas-and-amazon-bedrock/) 

## Choosing an AWS machine learning service
<a name="ml-guide"></a>

**Pick the right ML services and frameworks to support your work** 


|  |  | 
| --- |--- |
|  Purpose  |  Help determine which AWS ML services are the best fit for your needs.  | 
|  Last updated  |  May 3, 2024  | 
|  Covered services  |  +  [Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html) <br />+  [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/) <br />+  [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) <br />+  [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) <br />+  [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html) <br />+  [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) <br />+  [Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) <br />+  [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) <br />+  [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) <br />+  [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) <br />+  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/) <br />+  [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) <br />+  [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) <br />+  [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)   | 

### Introduction
<a name="introduction"></a>

 At its most basic, machine learning (ML) is designed to provide digital tools and services to learn from data, identify patterns, make predictions, and then act on those predictions. Almost all artificial intelligence (AI) systems today are created using ML. ML uses large amounts of data to create and validate decision logic. This decision logic forms the basis of the AI *model*. 

 Scenarios where AWS machine learning services may be applied include: 
+  **Specific use cases** — AWS machine learning services can support your AI powered use cases with a broad range of pre-built algorithms, models, and solutions for common use cases and industries. You have a choice of 23 pre-trained services, including Amazon Personalize, Amazon Kendra, and Amazon Monitron. 
+  **Customizing and scaling machine learning** — Amazon SageMaker AI is designed to help you build, train, and deploy ML models for any use case. You can build your own or access open source foundational models on AWS through Amazon SageMaker AI and Amazon Bedrock. 
+  **Accessing specialized infrastructure** — Use the ML frameworks and infrastructure provided by AWS when you require even greater flexibility and control over your machine learning workflows, and are willing to manage the underlying infrastructure and resources yourself. 

 This decision guide will help you ask the right questions, evaluate your criteria and business problem, and determine which services are the best fit for your needs. 

[![AWS Videos](https://img.youtube.com/vi/GBIkeMemh2E?start=110&end=495/0.jpg)](https://www.youtube.com/watch?v=GBIkeMemh2E?start=110&end=495)


### Understand
<a name="understand"></a>

 As organizations continue to adopt AI and ML technologies, the importance of understanding and choosing among AWS ML services is an on-going challenge. 

 AWS provides a range of ML services designed to help organizations to build, train, and deploy ML models more quickly and easily. These services can be used to solve a wide range of business problems such as customer churn prediction, fraud detection, and image and speech recognition. 

![Diagram describing how machine learning (ML) and generative AI fit within artificial intelligence (AI).](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/what-is-ai-ml.png)


 Before diving deeper into AWS ML services, let's look at the relationship between AI and ML. 
+  At a high level, *artificial intelligence *is a way to describe any system that can replicate tasks that previously required human intelligence. Most AI use cases are looking for a probabilistic outcome—making a prediction or decision with a high degree of certainty, similar to human judgement. 
+  Almost all AI systems today are created using *machine learning*. ML uses large amounts of data to create and validate decision logic, which is known as a model. 
+  Classification AI is a subset of ML that recognizes patterns to identify something. Predictive AI is a subset of ML that predicts future trends based on statistical patterns an historical data. 
+  Finally, generative AI is a subset of deep learning that can create new content and ideas, like conversations, stories, images, videos, and music. Generative AI is powered by very large models that are pretrained on vast corpora of data, called the Foundation Models or FMs. [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-Amazon Bedrock.html) is a fully managed service that offers a choice of high-performing FMs for building and scaling generative AI applications. [Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html) and  [Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html) are generative-AI powered assistants for specific use cases. 

 This guide is designed primarily to cover services in the *Classification AI* and *Predictive AI *machine learning categories. 

 In addition, AWS offers specialized, accelerated hardware for high performance ML training and inference. 
+  [Amazon EC2 P5](https://aws.amazon.com/ec2/instance-types/p5/) instances are equipped with NVIDIA H100 Tensor Core GPUs, which are well-suited for both training and inference tasks in machine learning. [Amazon EC2 G5](https://aws.amazon.com/ec2/instance-types/g5/) instances feature up to 8 NVIDIA A10G Tensor Core GPUs, and second generation AMD EPYC processors, for a wide range of graphics-intensive and machine learning use cases. 
+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) is the second-generation ML accelerator that AWS has purpose-built for deep learning (DL) training of 100B\+ parameter models. 
+  [AWS Inferentia2-based Amazon EC2 Inf2 instances](https://aws.amazon.com/machine-learning/inferentia/) are designed to deliver high performance at the lowest cost in Amazon EC2 for your DL and generative AI inference applications. 

### Consider
<a name="consider"></a>

 When solving a business problem with AWS ML services, consideration of several key criteria can help ensure success. The following section outlines some of the key criteria to consider when choosing a ML service. 

------
#### [ Problem definition ]

 **Problem definition** 

 The first step in the ML lifecycle is to frame the business problem. Understanding the problem you are trying to solve is essential for choosing the right AWS ML service, as different services are designed to address different problems. It is also important to determine whether ML is the best fit for your business problem. 

 Once you have determined that ML is the best fit, you can start by choosing from a range of purpose-built AWS AI services (in areas such as speech, vision and documents). 

 Amazon SageMaker AI provides fully managed infrastructure if you need to build and train your own models. AWS offers an array of advanced ML frameworks and infrastructure choices for the cases where you require highly customized and specialized ML models. AWS also offers a broad set of popular foundation models for building new applications with generative AI. 

------
#### [ ML algorithm ]

 **ML algorithm** 

 Choosing the ML algorithm for the business problem you are trying to solve depends on the type of data you are working with, as well as the desired outcomes. The following information outlines how each of the major AWS AI/ML service categories empowers you to work with its algorithms: 
+  Specialized AI services: These services offer a limited ability to customize the ML algorithm, as they are pre-trained models optimized for specific tasks. You can typically customize the input data and some parameters, but do not have access to the underlying ML models or the ability to build your own models. 
+  Amazon SageMaker AI: This service provides the most flexibility and control over the ML algorithm. You can use SageMaker AI to build custom models using your own algorithms and frameworks, or use pre-built models and algorithms provided by AWS. This allows for a high degree of customization and control over the ML process. 
+  Lower-level ML frameworks and infrastructure: These services offer the most flexibility and control over the ML algorithm. You can use these services to build highly customized ML models using their own algorithms and frameworks. However, using these services requires significant ML expertise and may not be feasible for all every use case. 

------
#### [ Security ]

 **Security** 

 If you need a private endpoint in your VPC, your options will vary based on the layer of AWS ML services you are using. These include: 
+  Specialized AI services: Most specialized AI services do not currently support private endpoints in VPCs. However, Amazon Rekognition Custom Labels and Amazon Comprehend Custom can be accessed using VPC endpoints. 
+  Core AI services: Amazon Translate, Amazon Transcribe, and Amazon Comprehend all support VPC endpoints. 
+  Amazon SageMaker AI: SageMaker AI provides built-in support for VPC endpoints, allowing you to deploy their trained models as an endpoint accessible only from within their VPC. 
+  Lower-level ML frameworks and infrastructure: You can deploy your models on Amazon EC2 instances or in containers within your VPC, providing complete control over the networking configuration. 

------
#### [ Latency ]

 **Latency** 

 Higher-level AI services, such as Amazon Rekognition and Amazon Transcribe, are designed to handle a wide variety of use cases and offer high performance in terms of speed. However, they might not meet certain latency requirements. 

 If you are using lower-level ML frameworks and infrastructure, we recommended leveraging Amazon SageMaker AI. This option is generally faster than building custom models due to its fully managed service and optimized deployment options. While a highly optimized custom model may outperform SageMaker AI, it will require significant expertise and resources to build. 

------
#### [ Accuracy ]

 **Accuracy** 

 The accuracy of AWS ML services varies based on the specific use case and level of customization required. Higher-level AI services, such as Amazon Rekognition, are built on pre-trained models that have been optimized for specific tasks and offer high accuracy in many use cases. 

 In some cases, you can choose to use Amazon SageMaker AI, which provides a more flexible and customizable platform for building and training custom ML models. By building your own models, you may be able to achieve even higher accuracy than what is possible with pre-trained models. 

 You can also choose to use ML frameworks and infrastructure, such as TensorFlow and Apache MXNet, to build highly customized models that offer the highest possible accuracy for your specific use case. 

------
#### [ AWS and responsible AI ]

 **AWS and responsible AI** 

 AWS builds foundation models (FMs) with responsible AI in mind at each stage of its development process. Throughout design, development, deployment, and operations we consider a range of factors including: 

1.  Accuracy (how closely a summary matches the underlying document; whether a biography is factually correct) 

1.  Fairness, (whether outputs treat demographic groups similarly) 

1.  Intellectual property and copyright considerations 

1.  Appropriate usage (filtering out user requests for legal advice, or medical diagnoses, or illegal activities) 

1.  Toxicity (hate speech, profanity, and insults) 

1.  Privacy (protecting personal information and customer prompts) 

 AWS builds solutions to address these issues into the processes used for acquiring training data, into the FMs themselves, and into the technology used to pre-process user prompts and post-process outputs. 

------

### Choose
<a name="choose"></a>

Now that you know the criteria by which you will be evaluating your ML service options, you are ready to choose which AWS ML service is right for your organizational needs. The following table highlights which ML services are optimized for which circumstances. Use it to help determine the AWS ML service that is the best fit for your use case.


|  **Categories**  |  **When would you use it?**  |  **What is it optimized for?**  |  **Related AI/ML services or environments**  | 
| --- | --- | --- | --- | 
|  **Specific use cases** <br /> These artificial intelligence services are intended to meet specific needs. They include personalization, forecasting, anomaly detection, speech transcription, and others. Since they are delivered as services, they can be embedded into applications without requiring any ML expertise.  |  Use the AI services provided by AWS when you require specific, pre-built functionalities to be integrated into your applications, without the need for extensive customizations or machine learning expertise. These services are designed to be easy to use and do not require much coding or configuration.  |  These services are designed to be easy to use and do not require much coding, configuration, or ML expertise.  |  [Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html) <br /> [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/) <br /> [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) <br /> [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html) <br /> [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) <br /> [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html) <br /> [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) <br /> [Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) <br /> [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) <br /> [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) <br /> [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html) <br /> [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) <br /> [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) <br /> [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)  | 
|  **ML services** <br /> These services can be used to develop customized machine learning models or workflows that go beyond the pre-built functionalities offered by the core AI services.  |  Use these services when when you need more customized machine learning models or workflows that go beyond the pre-built functionalities offered by the core AI services.  |  These services are optimized for building and training custom machine learning models, large-scale training on multiple instances or GPU clusters, more control over machine learning model deployment, real-time inference, and for building end-to-end workflows.  |  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) <br /> [Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) <br /> [SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) <br /> [SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) <br /> [SageMaker AI Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html) <br /> [SageMaker AI Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) <br /> [PyTorch on AWS](https://aws.amazon.com/pytorch/getting-started/) <br /> [Apache MxNet](https://aws.amazon.com/mxnet/) <br /> [Hugging Face](https://aws.amazon.com/machine-learning/hugging-face/) <br /> [TensorFlow on AWS](https://aws.amazon.com/tensorflow/)  | 
|  **Infrastructure** <br /> To deploy machine learning in production, you need cost-effective infrastructure, which Amazon enables with AWS-built silicon.  |  Use when you want to achieve the lowest cost for training models and need to run inference in the cloud.  |  Optimized for supporting the cost-effective deployment of machine learning.  |  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) <br /> [AWS Inferentia and Inferentia2](https://aws.amazon.com/machine-learning/inferentia/) <br /> [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)  | 
|  **Tools and associated services** <br /> These tools and associated services are designed to help you ease deployment of machine learning.  |  These services and tools are designed to help you accelerate deep learning in the cloud, providing Amazon machine images, docker images and entity resolution.  |  Optimized for helping you accelerate deep learning in the cloud.  |  [AWS Deep Learning AMIss](https://docs.aws.amazon.com/dlami/latest/devguide/what-is-dlami.html) <br /> [AWS Deep Learning Containers](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html) <br /> [AWS Entity Resolution](https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html)  | 

### Use
<a name="use"></a>

 Now that you have a clear understanding of the criteria you need to apply in choosing an AWS ML service, you can select which AWS AI/ML service(s) are optimized for your business needs. 

 To explore how to use and learn more about the service(s) you have chosen, we have provided three sets of pathways to explore how each service works. The first set of pathways provides in-depth documentation, hands-on tutorials, and resources to get started with Amazon Comprehend, Amazon Textract, Amazon Translate, Amazon Lex V2, Amazon Polly, Amazon Rekognition, and Amazon Transcribe. 

------
#### [ Amazon Comprehend ]
+ **Get started with Amazon Comprehend **

  Use the Amazon Comprehend console to create and run an asynchronous entity detection job. 

  [Get started with the tutorial »](https://docs.aws.amazon.com/comprehend/latest/dg/getting-started.html)

  
+ **Analyze insights in text with Amazon Comprehend **

  Learn how to use Amazon Comprehend to analyze and derive insights from text.   

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/analyze-sentiment-comprehend/)

  
+ **Amazon Comprehend Pricing **

  Explore information on Amazon Comprehend pricing and examples. 

  [Explore the guide »](https://aws.amazon.com/comprehend/pricing/)

  

------
#### [ Amazon Textract ]
+ **Getting Started with Amazon Textract** 

  Learn how Amazon Textract can be used with formatted text to detect words and lines of words that are located close to  each other, as well as analyze a document for items such as related text, tables, key-value pairs, and selection elements. 

  [Explore the guide »](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

  
+ **Extract text and structured data with Amazon Textract** 

  Learn how to use Amazon Textract to extract text and structured data from a document. 

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/extract-text-with-amazon-textract/?ref=gsrchandson)

  
+ **AWS Power Hour: Machine Learning** 

  Dive into Amazon Textract in this episode, spend time in the AWS Management Console, and review code samples that will help you understand how to make the most of service APIs.

  [ Watch the video »](https://youtu.be/TEX9ka1CAwA)

  

------
#### [ Amazon Translate ]
+ **Getting started with Amazon Translate using the console** 

  The easiest way to get started with Amazon Translate is to use the console to translate some text. Learn how to translate up to 10,000 characters using the console. 

  [Explore the guide »](https://docs.aws.amazon.com/translate/latest/dg/get-started-console.html)

  
+ **Translate Text Between Languages in the Cloud** 

  In this tutorial example, as part of an international luggage manufacturing firm, you need to understand what customers are saying about your product in reviews in the local market language - French. 

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/translate-text-between-languages-cloud/)

  
+ **Amazon Translate pricing**

  Explore Amazon Translate pricing, including Free Tier - which provides 2 million characters per month for 12 months. 

  [ Explore the guide »](https://aws.amazon.com/translate/pricing/)

  

------
#### [ Amazon Lex V2 ]
+ **Amazon Lex V2 V2 Developer Guide** 

  Explore information about getting started, how it works, and pricing information for Amazon Lex V2 V2. 

  [Explore the guide »](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)

  
+ **Introduction to Amazon Lex V2** We introduce you to the Amazon Lex V2 conversational service, and walk you through examples that show you how to create a bot and deploy it to different chat services. 

  [Take the course »](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/249/introduction-to-amazon-lex) (sign-in required)
+ **Exploring Generative AI in conversational experiences** 

  Explore the use of generative AI in conversation experiences.

  [ Read the blog »](https://aws.amazon.com/blogs/machine-learning/exploring-generative-ai-in-conversational-experiences-an-introduction-with-amazon-lex-langchain-and-sagemaker-jumpstart/)

  

------
#### [ Amazon Polly ]
+ **What is Amazon Polly?** 

  Explore a complete overview of the cloud service that converts text into lifelike speech, and can be used to develop applications to increase your customer engagement and accessibility. 

  [Explore the guide »](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)

  
+ **Highlight text as it’s being spoken using Amazon Polly** 

  We introduce you to approaches for highlighting text as it’s being spoken to add visual capabilities to audio in books, websites, blogs, and other digital experiences. 

  [Read the blog »](https://aws.amazon.com/blogs/machine-learning/highlight-text-as-its-being-spoken-using-amazon-polly/)

  
+ **Create audio for content in multiple languages with the same TTS voice persona in Amazon Polly** 

  We explain Neural Text-to-Speech (NTTS) and discuss how a broad portfolio of available voices, providing a range of distinct speakers in supported languages, can work for you. 

  [Read the blog »](https://aws.amazon.com/blogs/machine-learning/create-audio-for-content-in-multiple-languages-with-the-same-tts-voice-persona-in-amazon-polly/)

  

------
#### [ Amazon Rekognition ]
+ **What is Amazon Rekognition?** 

  Explore how you can use this service to add image and video analysis to your applications.   

  [Explore the guide »](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)

  
+ **Hands-on Rekognition: Automated Image and Video Analysis** 

  Learn how facial recognition works with streaming video, along with code examples and key points at a self-guided pace.   

  [Get started with the tutorial »](https://explore.skillbuilder.aws/learn/course/external/view/elearning/263/hands-on-rekognition-automated-image-and-video-analysis)

  
+ **Amazon Rekognition FAQs** 

  Learn the basics of Amazon Rekognition and how it can help you improve your deep learning and visually analyze your applications. 

  [Read the FAQs »](https://aws.amazon.com/rekognition/faqs/)

  

------
#### [ Amazon Transcribe ]
+ **What is Amazon Transcribe?** 

  Explore the AWS automatic speech recognition service using ML to convert audio to text. Learn how to use this service as a standalone transcription or add speech-to-text capability to any application. 

  [Explore the guide »](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html)

  
+ **Amazon Transcribe Pricing** 

  We introduce you to the AWS pay-as-you-go transcription, including custom language model options and the Amazon Transcribe Free Tier.

  [ Explore the guide »](https://aws.amazon.com/transcribe/pricing/)

  
+ **Create an audio transcript with Amazon Transcribe** 

  Learn how to use Amazon Transcribe to create a text transcript of recorded audio files using a real-world use case scenario for testing against your needs. 

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/create-audio-transcript-transcribe/)

  
+ **Build an Amazon Transcribe streaming app** 

  Learn how to build an app to record, transcribe, and translate live audio in real-time, with results emailed directly to you. 

  [Explore the guide »](https://docs.aws.amazon.com/transcribe/latest/dg/example_cross_TranscriptionStreamingApp_section.html)

  

------

 The second set of AI/ML AWS service pathways provide in-depth documentation, hands-on tutorials, and resources to get started with the services in the Amazon SageMaker AI family. 

------
#### [ SageMaker AI ]
+ **How Amazon SageMaker AI works** 

  Explore the overview of machine learning and how SageMaker AI works. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html#how-it-works)

  
+ **Getting started with Amazon SageMaker AI** 

  Learn how to join an Amazon SageMaker AI Domain, giving you access to Amazon SageMaker AI Studio and RStudio on SageMaker AI.  

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html)

  
+ **Use Apache Spark with Amazon SageMaker AI** 

  Learn how to use Apache Spark for preprocessing data and SageMaker AI for model training and hosting.  

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark.html)

  
+ **Use Docker containers to build models**

  Explore how Amazon SageMaker AI makes extensive use of Docker containers for build and runtime tasks. Learn how to deploy the pre-built Docker images for its built-in algorithms and the supported deep learning frameworks used for training and inference. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)

  
+ **Machine learning frameworks and languages**

   Learn how to get started with SageMaker AI using the Amazon SageMaker AI Python SDK.

  [ Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html)

  

------
#### [ SageMaker AI Autopilot ]
+ **Create an Amazon SageMaker AI Autopilot experiment for tabular data**

   Learn you how to create an Amazon SageMaker AI Autopilot experiment to explore, pre-process, and train various model candidates on a tabular dataset. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html)

  
+ **Automatically create machine learning models**

   Learn how to use Amazon SageMaker AI Autopilot to automatically build, train, and tune a ML model, and deploy the model to make predictions. 

  [Get started with the tutorial »](https://aws.amazon.com/tutorials/machine-learning-tutorial-automatically-create-models/)

  
+ **Explore modeling with Amazon SageMaker AI Autopilot with these example notebooks**

   Explore example notebooks for direct marketing, customer churn prediction and how to bring your own data processing code to Amazon SageMaker AI Autopilot. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-samples.html)

  

------
#### [ SageMaker AI Canvas ]
+ **Get started using Amazon SageMaker AI Canvas** 

  Learn how to get started with using SageMaker AI Canvas. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html)

  
+ **Generate machine learning predictions without writing code** 

  This tutorial explains how to use Amazon SageMaker AI Canvas to build ML models and generate accurate predictions without writing a single line of code. 

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/machine-learning-tutorial-generate-predictions-without-writing-code/)

  
+ **Dive deeper into SageMaker AI Canvas **

   Explore an in-depth look at SageMaker AI Canvas and its visual, no code ML capabilities. 

  [Read the blog  »](https://aws.amazon.com/blogs/aws/announcing-amazon-sagemaker-canvas-a-visual-no-code-machine-learning-capability-for-business-analysts/)

  
+ **Use Amazon SageMaker AI Canvas to make your first ML Model** 

  Learn how to use Amazon SageMaker AI Canvas to create an ML model to assess customer retention, based on an email campaign for new products and services. 

  [Get started with the lab »](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/14786/use-amazon-sagemaker-canvas-to-make-your-first-ml-model-amazon)

  

------
#### [ SageMaker AI Data Wrangler ]
+ **Getting started with Amazon SageMaker AI Data Wrangler**

   Explore how set up SageMaker AI Data Wrangler and then provides a walkthrough using an existing example dataset.

  [ Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html)

  
+ **Prepare training data for machine learning with minimal code** 

  Learn how to prepare data for ML using Amazon SageMaker AI Data Wrangler.

  [ Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/machine-learning-tutorial-prepare-data-with-minimal-code/)

  
+ **SageMaker AI Data Wrangler deep dive workshop** 

  Learn how to apply appropriate analysis types on your dataset to detect anomalies and issues, use the derived results/insights to formulate remedial actions in the course of transformations on your dataset, and test the right choice and sequence of transformations using quick modeling options provided by SageMaker AI Data Wrangler. 

  [Get started with the workshop »](https://catalog.us-east-1.prod.workshops.aws/workshops/327375b8-425b-49d4-b0da-241da0595ecf/en-US#the-challenges-of-data-prep)

  

------
#### [ SageMaker AI Ground Truth ]
+ **Getting Started with Amazon Ground Truth** 

  Explore how to use the console to create a labeling job, assign a public or private workforce, and send the labeling job to your workforce. Learn how to monitor the progress of a labeling job. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-getting-started.html)

  
+ **Label Training Data for Machine Learning** 

  Learn how to set up a labeling job in Amazon SageMaker AI Ground Truth to annotate training data for your ML model. 

  [Get started with the tutorial »](https://aws.amazon.com/tutorials/machine-learning-tutorial-label-training-data/)

  
+ **Getting started with Amazon Ground Truth Plus** Explore how to complete the necessary steps to start an Amazon SageMaker AI Ground Truth Plus project, review labels, and satisfy SageMaker AI Ground Truth Plus prerequisites. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp-getting-started.html)

  
+ **Get started with Amazon Ground Truth** Watch how to get started with labeling your data in minutes through the SageMaker AI Ground Truth console. 

  [Watch the video »](https://www.youtube.com/watch?v=_FPI6KjDlCI)

  
+ **Amazon SageMaker AI Ground Truth Plus – create training datasets without code or in-house resources** 

  Learn about Ground Truth Plus, a turn-key service that uses an expert workforce to deliver high-quality training datasets fast, and reduces costs by up to 40 percent. 

  [Read the blog »](https://www.youtube.com/watch?v=_FPI6KjDlCI)

  

------
#### [ SageMaker AI JumpStart ]
+ **Get started with machine learning with SageMaker AI JumpStart** 

  Explore SageMaker AI JumpStart solution templates that set up infrastructure for common use cases, and executable example notebooks for machine learning with SageMaker AI. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

  
+ **Get Started with your machine learning project quickly using Amazon SageMaker AI JumpStart** 

  Learn how to fast-track your ML project using pretrained models and prebuilt solutions offered by Amazon SageMaker AI JumpStart. You can then deploy the selected model through Amazon SageMaker AI Studio notebooks. 

  [Get started with the tutorial »](https://aws.amazon.com/getting-started/hands-on/machine-learning-tutorial-get-started-with-your-project-quickly/)

  
+ **Get hands-on with Amazon SageMaker AI JumpStart with this Immersion Day workshop** 

  Learn how the low-code ML capabilities found in Amazon SageMaker AI Data Wrangler, Autopilot and Jumpstart, make it easier to experiment faster and bring highly accurate models to production. 

  [Get started with the workshop »](https://catalog.us-east-1.prod.workshops.aws/workshops/f560a788-af64-4e5a-a02c-a6c88516ab02/en-US/)

  

------
#### [ SageMaker AI Pipelines ]
+ **Getting Started with Amazon SageMaker AI Pipelines** 

  Learn how to create end-to-end workflows that manage and deploy SageMaker AI jobs. SageMaker AI Pipelines comes with SageMaker AI Python SDK integration, so you can build each step of your pipeline using a Python-based interface. 

  [Explore the guide »](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-build.html)

  
+ **Automate machine learning workflows**

   Learn how to create and automate end-to-end machine learning (ML) workflows using Amazon SageMaker AI Pipelines, Amazon SageMaker AI Model Registry, and Amazon SageMaker AI Clarify. 

  [Get started with the tutorial »](https://aws.amazon.com/tutorials/machine-learning-tutorial-mlops-automate-ml-workflows/)

  
+ **How to create fully automated ML workflows with Amazon SageMaker AI Pipelines** 

  Learn about Amazon SageMaker AI Pipelines, the world’s first ML CI/CD service designed to be accessible for every developer and data scientist. SageMaker AI Pipelines brings CI/CD pipelines to ML, reducing the coding time required. 

  [Watch the video »](https://www.youtube.com/watch?v=W7uabCTfLrg)

  

------
#### [ SageMaker AI Studio ]
+ **Build and train a machine learning model locally** 

  Learn how to build and train a ML model locally within your Amazon SageMaker AI Studio notebook. 

  [Get started with the tutorial »](https://aws.amazon.com/tutorials/machine-learning-tutorial-build-model-locally/)

  
+ **SageMaker AI Studio integration with EMR workshop**

   Learn how to utilize distributed processing at scale to prepare data and subsequently train machine learning models. 

  [Get started with the workshop »](https://catalog.workshops.aws/sagemaker-studio-emr/en-US)

  

------

 The third set of AI/ML AWS service pathways provide in-depth documentation, hands-on tutorials, and resources to get started with AWS Trainium, AWS Inferentia, and Amazon Titan. 

------
#### [ AWS Trainium ]
+ **Scaling distributed training with AWS Trainium and Amazon EKS** 

  Learn how you can benefit from the general availability of Amazon EC2 Trn1 instances powered by AWS Trainium—a purpose-built ML accelerator optimized to provide a high-performance, cost-effective, and massively scalable platform for training deep learning models in the cloud.   

  [Read the blog »](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/)

  
+ **Overview of AWS Trainium** 

  Learn about AWS Trainium, the second-generation machine learning (ML) accelerator that AWS purpose built for deep learning training of 100B\+ parameter models. Each Amazon Elastic Compute Cloud (EC2) Trn1 instance deploys up to 16 AWS Trainium accelerators to deliver a high-performance, low-cost solution for deep learning (DL) training in the cloud. 

  [Explore the guide »](https://aws.amazon.com/machine-learning/trainium/)

  
+ **Recommended Trainium Instances** 

  Explore how AWS Trainium instances are designed to provide high performance and cost efficiency for deep learning model inference workloads.

  [ Explore the guide »](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html)

  

------
#### [ AWS Inferentia ]
+ **Overview of AWS Inferentia** 

  Understand  how accelerators are designed by AWS to deliver high performance at the lowest cost for your deep learning (DL) inference applications.   

  [Explore the guide  »](https://aws.amazon.com/machine-learning/inferentia/)

  
+ **AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency** 

  Understand what AWS Inferentia2 is optimized for - and explores how it was designed from the ground up to deliver higher performance while lowering the cost of LLMs and generative AI inference. 

  [Read the blog »](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/)

  
+ **Machine learning inference using AWS Inferentia** 

  Learn how to create an Amazon EKS cluster with nodes running Amazon EC2 Inf1 instances and (optionally) deploy a sample application. Amazon EC2 Inf1 instances are powered by AWS Inferentia chips, which are custom built by AWS to provide high performance and lowest cost inference in the cloud. 

  [Explore the guide »](https://docs.aws.amazon.com/eks/latest/userguide/inferentia-support.html)

  

------
#### [ Amazon Titan ]
+ **Overview of Amazon Titan** 

  Explore how Amazon Titan FMs are pretrained on large datasets, making them powerful, general-purpose models. Learn how you can use them as is - or privately - to customize them with your own data for a particular task without annotating large volumes of data. 

  [Explore the guide »](https://aws.amazon.com/bedrock/titan/)

  

------

### Explore
<a name="explore"></a>
+ **Architecture diagrams **

  These reference architecture diagrams show examples of AWS AI and ML services in use. 

   [Explore architecture diagrams »](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers **

  Explore whitepapers to help you get started and learn best practices in choosing and using AI/ML services. 

   [Explore whitepapers »](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)
+ **AWS Solutions **

  Explore vetted solutions and architectural guidance for common use cases for AI and ML services. 

   [Explore solutions »](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23ai-ml&awsf.industries=*all&awsf.business-category=*all)

### Resources
<a name="resources"></a>

 **Foundation models** 

 Supported foundation models include: 
+  [Anthropic Claude](https://aws.amazon.com/bedrock/claude/) 
+  [Cohere Command & Embed](https://aws.amazon.com/bedrock/cohere-command-embed/) 
+  [AI21 Labs Jurassic](https://aws.amazon.com/bedrock/ai21/) 
+  [Meta Llama](https://aws.amazon.com/bedrock/llama/) 
+  [Mistral AI](https://aws.amazon.com/bedrock/mistral/) 
+  [Stable Diffusion XL](https://aws.amazon.com/bedrock/stable-diffusion/) 
+  [Amazon Titan](https://aws.amazon.com/bedrock/titan/) 

 Using Amazon Bedrock, you can experiment with a variety of foundation models and privately customize them with your data. 

 **Use case or industry-specific services** 
+  [Amazon Comprehend Medical](https://aws.amazon.com/comprehend/medical/) 
+  [Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/) 
+  [AWS HealthLake](https://aws.amazon.com/healthlake/) 
+  [Amazon Lookout for Equipment](https://aws.amazon.com/lookout-for-equipment/) 
+  [Amazon Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/) 
+  [Amazon Lookout for Vision](https://aws.amazon.com/lookout-for-vision/) 
+  [Amazon Monitron](https://aws.amazon.com/monitron/) 
+  [AWS HealthOmics](https://aws.amazon.com/healthomics/) 
+  [AWS Panorama](https://aws.amazon.com/panorama/) 

 **Associated blog posts** 
+  [Significant new capabilities make it easier to use Amazon Bedrock to build and scale generative AI applications – and achieve impressive results](https://aws.amazon.com/blogs/machine-learning/new-capabilities-make-it-easier-to-use-amazon-bedrock-to-build-and-scale-generative-ai-applications-and-deliver-impact/) 
+  [AWS Inferentia and AWS Trainium deliver lowest cost to deploy Llama 3 models in Amazon SageMaker AI JumpStart](https://aws.amazon.com/blogs/machine-learning/aws-inferentia-and-aws-trainium-deliver-lowest-cost-to-deploy-llama-3-models-in-amazon-sagemaker-jumpstart/) 
+  [Revolutionize Customer Satisfaction with tailored reward models for your business on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/revolutionize-customer-satisfaction-with-tailored-reward-models-for-your-business-on-amazon-sagemaker/) 
+  [Amazon Personalize launches new recipes supporting larger item catalogs with lower latency](https://aws.amazon.com/blogs/machine-learning/amazon-personalize-launches-new-recipes-supporting-larger-item-catalogs-with-lower-latency/) 

## Amazon Bedrock or Amazon SageMaker AI?
<a name="bedrock-or-sagemaker"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | Understand the differences between Amazon Bedrock and Amazon SageMaker AI, and determine which service is the best fit for your needs. | 
| **Last updated** | July 23, 2026 | 
| **Covered services** |  +  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) <br />+  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)   | 

### Introduction
<a name="introduction"></a>

Amazon Web Services (AWS) offers managed services to help you build AI applications and agents. For an overview of how these services work together across the generative AI stack, from custom silicon to agentic solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html).

The following diagram shows the AWS AI stack from silicon to agentic solutions.

![Diagram showing the AWS AI stack from silicon to agentic solutions. From bottom to top: global infrastructure (39 Regions), AI chips (Trainium, Graviton, NVIDIA GPUs), data foundation, models training and inferencing (SageMaker, Bedrock), agent development and orchestration (Bedrock AgentCore), and agentic solutions (Kiro, Quick, Connect, Marketplace). Security, governance, and agent store span the full stack.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/gen-ai-stack-dec-2024.png)


When choosing which generative AI services to use, two services are often compared: 

**Amazon Bedrock**
+ Choose [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) if you need a fully managed, serverless platform to build, run, and operate AI applications and agents at production scale. Amazon Bedrock provides access to frontier models from leading AI labs, agent development paths that work with any framework, and governance controls that extend the AWS security stack to AI wherever it runs.
+ Amazon Bedrock provides [additional capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/additional-capabilities.html) to enhance your generative AI applications, including [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for retrieval augmented generation (RAG), [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) for implementing safeguards, [AgentCore](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) for building, deploying, and operating AI agents at scale, [Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html) for building end-to-end workflows, [Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for transforming unstructured data, and [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) for constructing reusable prompts.
+ Use [ Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to discover, test, and use popular, emerging, and specialized foundation models (FMs). 

**Amazon SageMaker AI**
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) (formerly Amazon SageMaker) is a fully managed service designed to help you build, train, and deploy AI, predictive ML, and classical ML models at scale. This includes building models from scratch using tools such as notebooks, pipelines, and ModelOps solutions. Serverless MLflow supports tracking experiments and tracing agents. Consider SageMaker AI when you have use cases that can benefit from extensive training, fine-tuning, customization, and inference of open, proprietary, and custom models. Also consider SageMaker AI for deploying models when you need to manage cost, throughput, and latency tradeoffs. SageMaker AI provides managed infrastructure with native optimizations for workload-optimized inference. It can also help you through the potentially challenging task of evaluating which model is the best fit for your use case. Custom models trained on SageMaker AI can deploy to SageMaker AI endpoints for managed inference, to Amazon SageMaker HyperPod for large-scale inference, or to Amazon Bedrock for serverless inference.
+ In addition to the managed infrastructure provided by SageMaker AI training and SageMaker AI inference, Amazon SageMaker HyperPod provides resilient, scalable infrastructure for training and deploying AI models at scale with access to the orchestration layer: Kubernetes (EKS) for training and inference, or Slurm for training.

This guide is focused on understanding the differences between Amazon SageMaker AI and Amazon Bedrock. For more information about how Amazon Bedrock and SageMaker AI fit into Amazon’s generative AI services and solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html). 

While both Amazon Bedrock and Amazon SageMaker AI enable the development of AI applications and agents, they serve different purposes. This guide helps you understand which of these services is the best fit for your needs, including scenarios in which both services can be used together to build generative AI applications.

The following is a high-level view of the key differences between these services to get you started. 


|  **Category**  |  ![Amazon Bedrock service icon.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-Bedrock_48.png) **Amazon Bedrock**  |  ![Brain icon with interconnected nodes representing artificial intelligence or machine learning.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-SageMaker_48.png) **Amazon SageMaker AI**  | 
| --- | --- | --- | 
|  Use Cases  | Fully managed, serverless platform for building, running, and operating AI applications and agents at production scale | Optimized for convenient training, customizing, and deploying AI models with maximum user control for AI applications, predictive ML, and classical ML at production scale | 
|  Target Users  | Optimized for technical decision makers, developers, and teams building AI applications and agents | Optimized for ML practitioners, ML engineers, Data Scientists, AI platform teams and developers | 
|  Customization  | Automated customization with fine-tuning, distillation, and custom model import; minimal infrastructure management | Serverless customization with SFT, DPO, RLVR, and RLAIF; managed training with Training Jobs; full control with HyperPod | 
|  Pricing  | Pay-as-you-go per-token pricing based on input and output tokens processed, with Priority, Flex, and Reserved service tiers available | Per-token pricing for serverless customization; usage-based pricing for compute resources with training jobs, inference, and HyperPod | 
|  Integration  | Integrate pre-trained models into applications through API calls, including OpenAI-compatible endpoints | Integrate custom models into applications, with more customization options | 
|  Expertise Required  | Basic level of ML expertise needed to use pre-trained models | Guided UI and AI agent-assisted workflows simplify customization; deeper ML expertise helpful for advanced training jobs | 
| Management | Amazon Bedrock provides a simplified API-based approach with minimal infrastructure management. | Serverless model customization requires no infrastructure management. Inference, training jobs, and HyperPod offer full infrastructure control with extensive [monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) and [control](https://docs.aws.amazon.com/sagemaker/latest/dg/governance.html) capabilities. | 
| Deployment and Hosting | Amazon Bedrock is serverless, meaning you do not have to manage infrastructure. | Serverless for model customization; custom models deploy to SageMaker AI dedicated endpoints for managed inference or Amazon Bedrock for serverless inference. Training jobs and HyperPod support train-to-serve continuity with granular node-level resource control. Endpoints scale to zero with built-in observability and operational simplicity, including serverless MLflow. | 

### Differences between Amazon Bedrock and SageMaker AI
<a name="differences"></a>

The following sections examine and compare the capabilities of Amazon Bedrock and Amazon SageMaker AI. 

------
#### [ Use cases ]

Amazon Bedrock and Amazon SageMaker AI address different use cases based on your specific requirements and resources. 

 **Amazon Bedrock** 
+ Amazon Bedrock is designed for use cases where you want to build AI applications and agents without investing heavily in custom model development. For example, a content moderation system for a social media platform could use Amazon Bedrock's pre-trained models to automatically identify and flag inappropriate text or images. Similarly, a customer support chatbot could use Amazon Bedrock's natural language processing capabilities to understand and respond to user inquiries. Amazon Bedrock is particularly useful if you have limited machine learning (ML) expertise or resources, as it helps you to benefit from AI without the need for extensive in-house development. 

 **Amazon SageMaker AI** 
+ SageMaker AI is a good choice for convenient training, customizing, and deploying AI, predictive ML, and classical ML models with maximum control. Choose SageMaker AI when you need to access the container or orchestration layer to directly manage cost-latency-throughput and other tradeoffs. Examples include a healthcare company developing a model to predict patient outcomes based on specific biomarkers. Another example is a financial institution creating a fraud detection system tailored to their unique data and risk factors. Another scenario is a large-scale LLM deployment where you want to maximize GPU utilization while balancing cost against desired throughput and latency metrics.

------
#### [ Target users ]

Rather than choosing one service over the other, consider what level of customization you need. A common path is to start with Amazon Bedrock and progress to SageMaker AI as your customization requirements grow.

 **Amazon Bedrock** 
+ Choose Amazon Bedrock if you want to build AI applications and agents using pre-trained models, prompt engineering, and RAG — without needing deep ML expertise.

 **Amazon SageMaker AI** 
+ SageMaker AI serves two audiences. If you need to change model behavior through serverless customization, the guided UI and AI agent-assisted workflow require no ML expertise. If you need full control over training workflows, model deployment, frameworks, and infrastructure, use training jobs, dedicated endpoints, and HyperPod.

------
#### [ Choice of FMs ]

 While both Amazon Bedrock and Amazon SageMaker AI offer a broad set of FMs for your applications, there are differences in the set of FMs that each service offers.

 **Amazon Bedrock** 
+ Amazon Bedrock provides access to FMs including proprietary models such as Anthropic Claude and Amazon Nova, open models from Meta (Llama), Mistral AI, Qwen, and OpenAI (GPT-OSS), Stability AI models for image generation, and many others. See the [ list of available FMs](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html), which is updated frequently.
+ Use the [ Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html) to rapidly test and incorporate over 100 publicly available and proprietary FMs.
+ Amazon Bedrock provides access to certain proprietary models, including Claude, that are not available in Amazon SageMaker JumpStart.

 **Amazon SageMaker AI** 
+ Amazon SageMaker JumpStart offers built-in publicly available and proprietary foundation models to customize and integrate into your generative AI, classical ML, and predictive ML workflows, with nearly 1,000 models available, including models optimized for specific use cases.
+ JumpStart offers publicly available FMs, including models from Hugging Face, Stability AI, Meta, and Amazon, and proprietary FMs from Amazon (Nova models for both customization and inference), AI21 Labs, Cohere, and LightOn. See the [ list of publicly available and proprietary FMs](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-latest.html), which is updated frequently.

------
#### [ Customization ]

Amazon Bedrock and Amazon SageMaker AI offer different levels of customization capabilities that you can tailor to your specific needs and expertise. 

 **Amazon Bedrock** 
+ Amazon Bedrock offers a set of models from leading providers that you can use to build generative AI applications with automated customization options. You have access to a set of API calls that you use to enter data and receive predictions from these pre-trained models. This approach simplifies the process of incorporating AI capabilities into applications. Amazon Bedrock supports fine-tuning, [model distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html), reinforcement fine-tuning, and [custom model import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html), with minimal infrastructure management.

 **Amazon SageMaker AI** 
+ Amazon SageMaker AI provides serverless model customization with a guided interface and AI agent-assisted workflow, offering control with guardrails while eliminating infrastructure management. The AI agent handles the full customization lifecycle — technique selection, data preparation, training, evaluation, and deployment — through natural language, so developers can complete workflows without specialized ML knowledge. SageMaker AI also supports IDE portability with VS Code, Kiro, and other development environments. SageMaker AI supports a broad set of serverless customization techniques available for open-weight models, including supervised fine-tuning (SFT), direct preference optimization (DPO), reinforcement learning with verifiable rewards (RLVR), reinforcement learning with AI feedback (RLAIF), and managed multi-turn reinforcement learning. For full infrastructure control, SageMaker AI managed training jobs, managed inference and HyperPod provide complete flexibility over the training and inferencing workflows, frameworks, and compute resources.
+ Use [ Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) to evaluate, compare, and select models based on pre-defined quality and responsibility. 
+ Use [Amazon Nova customization recipes](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model.html) on SageMaker AI for comprehensive model customization, including fine-tuning and training Nova models that can be imported into Amazon Bedrock. With [Amazon Nova Forge](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-forge.html), you can build your own frontier models using Nova by starting from early model checkpoints, blending proprietary data with Amazon Nova-curated training data, and hosting custom models securely on AWS.

------
#### [ Pricing ]

 Amazon Bedrock and Amazon SageMaker AI have different pricing models that reflect their target users and the services they provide. 

 **Amazon Bedrock** 
+ Amazon Bedrock uses per-token [pricing](https://aws.amazon.com/bedrock/pricing/) for model inference, based on input and output tokens processed. Additional features such as Knowledge Bases, Guardrails, and Data Automation are priced separately based on usage. This pricing structure makes it efficient to estimate and control costs. Amazon Bedrock also offers service tiers for inference: Priority for latency-sensitive workloads, Flex for cost-optimized batch processing, and Reserved for committed capacity with predictable pricing. Batch inference offers up to 50% savings for non-real-time workloads, and Provisioned Throughput provides committed capacity at reduced rates. The pricing model for Amazon Bedrock is particularly well-suited for applications with predictable workloads, or for cases where you want more transparency in your AI-related expenses. 

 **Amazon SageMaker AI** 
+ SageMaker AI offers per-token [pricing](https://aws.amazon.com/sagemaker/pricing/) for serverless model customization, providing the same pricing simplicity as Amazon Bedrock. For managed training jobs, inference, and HyperPod, SageMaker AI follows usage-based pricing for compute resources, storage, and other services consumed during the AI development process, with prices varying depending on the instance type and size. SageMaker AI Savings Plans can reduce costs by up to 64% with 1- or 3-year commitments. SageMaker AI also supports cost-optimized hardware including AWS Trainium for training and AWS Inferentia for inference.

------
#### [ Integration ]

 Amazon Bedrock and Amazon SageMaker AI offer different approaches to integrating AI models into applications, catering to your specific needs and expertise. 

 **Amazon Bedrock** 
+ Amazon Bedrock simplifies the integration process by providing pre-trained models that you can access directly through API calls. Use the Amazon Bedrock SDK, REST API, or OpenAI-compatible API endpoints to send input data and receive predictions from the models without needing to manage the underlying infrastructure. The OpenAI-compatible endpoints support the Responses API and Chat Completions API. With these endpoints, you can migrate existing OpenAI applications by updating the base URL and API key. This approach significantly reduces the complexity and time required to integrate AI capabilities into applications, making it accessible to a broad range of developers. 

 **Amazon SageMaker AI** 
+ SageMaker AI provides a comprehensive platform for building, training, and deploying custom AI models. For managed inference on SageMaker AI endpoints, you use the SageMaker AI SDK or API to access deployed models. SageMaker AI provides tools such as GenAI inference recommendations and benchmarking to simplify instance type selection. For serverless customization, custom models can also deploy to Amazon Bedrock for serverless inference with no additional infrastructure setup.

------
#### [ Expertise required ]

 Amazon Bedrock and Amazon SageMaker AI offer different paths depending on your level of expertise and the degree of control you need. 

 **Amazon Bedrock** 
+ Amazon Bedrock is more accessible to a broader range of users, including developers and businesses with limited ML expertise. By providing pre-trained models that can be easily integrated into applications through API calls, Amazon Bedrock abstracts away much of the complexity associated with building and deploying AI models. For the serverless path, both Amazon Bedrock and SageMaker AI serverless customization handle data preprocessing, model selection, and infrastructure management. You can focus on integrating AI capabilities into your applications without deep ML expertise. 

 **Amazon SageMaker AI** 
+ SageMaker AI provides guided experiences that simplify model customization for a broad range of users. The guided UI and AI agent-assisted workflow (in preview) enable developers to complete customization workflows in a few clicks or through natural language, including technique selection, data preparation, and model evaluation. For advanced use cases such as custom training jobs and HyperPod clusters, deeper ML expertise is helpful for optimizing training workflows, frameworks, and infrastructure configurations.

------
#### [ Features ]

 Amazon Bedrock and Amazon SageMaker AI offer complementary capabilities for building AI applications and agents. 

 **Amazon Bedrock** 
+ Amazon Bedrock offers a suite of features to help you build and scale AI applications and agents, including model choice features (evaluation), cost and latency optimization features (prompt caching, intelligent prompt routing, service tiers), customization features (knowledge bases, model distillation, reinforcement fine-tuning), safeguards (guardrails with automated reasoning checks, organizational safeguards, image content filters, and cross-platform support for non-Amazon Bedrock models), agentic features (Amazon Bedrock AgentCore for building, deploying, and operating AI agents at scale, multi-agent collaboration, AWS Agent Registry, and framework-agnostic compatibility with LangGraph, CrewAI, and LlamaIndex), and data processing features (Amazon Bedrock Data Automation for documents, images, audio, and video). Amazon Bedrock also offers custom model import, OpenAI-compatible API endpoints, and a serverless, unified API for accessing foundation models. Prompt caching can reduce costs by up to 90% and latency by up to 85% for supported models. Intelligent prompt routing can reduce costs by up to 30% without compromising accuracy. Distilled models are up to 500% faster and up to 75% less expensive than original models, with less than 2% accuracy loss for use cases such as RAG. Guardrails with automated reasoning checks help reduce factual errors due to hallucinations to near zero.

 **Amazon SageMaker AI** 
+ SageMaker AI offers a comprehensive platform for the full AI development lifecycle. Key capabilities include: serverless model customization with SFT, DPO, RLVR, and RLAIF through a guided UI and AI agent-assisted workflow; Amazon SageMaker JumpStart as a model hub with nearly 1,000 models available including open-source, proprietary, and custom models; support for predictive ML and classical ML in addition to generative AI; and IDE portability with support for VS Code, Kiro, and other development environments. Amazon SageMaker HyperPod provides an end-to-end experience for large-scale AI development, supporting training and inference on managed clusters with checkpointless training, elastic training, and task governance. HyperPod reduces training time by up to 40%, task governance reduces costs by up to 40%, and checkpointless training enables upwards of 95% training goodput. HyperPod scales across thousands of AI accelerators. SageMaker AI endpoints support scaling to zero instances to reduce costs when idle, stateful sessions for maintaining context across inference requests, and inference optimization techniques such as EAGLE-based speculative decoding for up to 2.5x throughput improvement. SageMaker AI supports advanced deployment options including heterogeneous instance clusters and cross-region inference for higher availability, A/B testing, canary deployments, blue/green deployments, and shadow testing. Inference Components reduce model deployment costs by hosting multiple models behind a single endpoint.
+ Amazon SageMaker HyperPod provides resilient, scalable infrastructure for training and deploying AI models at scale with access to the orchestration layer: Kubernetes (EKS) for training and inference, or Slurm for training. For inference, HyperPod also offers built-in capabilities such as distributed KV caching, capacity-aware inference, and intelligent routing, reducing latency by 40%.

------

The choice between Amazon Bedrock and Amazon SageMaker AI is not always mutually exclusive. You may benefit from using both services together in a progressive customization pipeline:
+ **Start with Amazon Bedrock**: Begin with prompt engineering and retrieval augmented generation (RAG) using Amazon Bedrock Knowledge Bases to quickly build and iterate on your generative AI application.
+ **Move to SageMaker AI serverless customization**: When you need to change model behavior beyond what prompting can achieve, use SageMaker AI serverless customization with techniques such as SFT and DPO to fine-tune models on your data.
+ **Advance to reinforcement learning**: For reward-signal optimization, use RLVR and RLAIF on SageMaker AI to further align model outputs with your specific quality and accuracy requirements.
+ **Deploy across both services**: Custom models trained on SageMaker AI can be deployed in SageMaker AI inference or imported to Amazon Bedrock through custom model import for serverless inference, or to SageMaker AI endpoints for managed inference with granular control over cost, throughput, and latency. You can also prototype on Amazon Bedrock serverless inference and move to SageMaker AI endpoints or HyperPod when you need production-level control over infrastructure to manage cost-latency-throughput tradeoffs.

The following table maps common use case patterns to recommended service approaches.


| **Use case pattern** | **Recommended approach** | 
| --- | --- | 
| Rapid FM prototyping with prompt engineering and RAG | Amazon Bedrock | 
| Enterprise AI agents with security and observability | Amazon Bedrock AgentCore with Amazon Bedrock and/or SageMaker AI for inference | 
| Serverless model customization (SFT, DPO, RL) | SageMaker AI serverless customization | 
| Custom model training at scale | SageMaker AI training jobs or HyperPod | 
| Large-scale GenAI inference | Amazon Bedrock and/or SageMaker AI depending on the need to directly manage cost-latency-throughput tradeoffs | 
| Full ML lifecycle with governance | SageMaker AI | 
| Production GenAI apps with cost optimization | Both services together | 

Ultimately, the decision between Amazon Bedrock and Amazon SageMaker AI depends on your specific requirements. Evaluating these factors helps you choose the service that best fits your needs. 

For more information about Amazon’s generative AI services and solutions, see the [generative AI decision guide](https://docs.aws.amazon.com/decision-guides/latest/generative-ai-on-aws-how-to-choose/guide.html). 

### Use
<a name="use"></a>

A common approach is to follow a progressive journey: start with Amazon Bedrock for prompt engineering and RAG, then move to SageMaker AI serverless customization when you need to change model behavior, and advance to training jobs or HyperPod when you need full infrastructure control. Use the following resources to get started at any point in this journey.

------
#### [ Amazon Bedrock ]
+  **What is Amazon Bedrock?** 

  Use this fully managed, serverless platform to build, run, and operate AI applications and agents at production scale. 

   [Explore the guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) 

  
+  **Frequently asked questions about Amazon Bedrock** 

  Get answers to the most commonly-asked questions about Amazon Bedrock. These include how to use agents, security considerations, details about Amazon Bedrock software development kits (SDKs), retrieval augmented generation, how to use model evaluation, and billing. 

   [Read the FAQs](https://aws.amazon.com/bedrock/faqs/) 

  
+  **Guidance for generating product descriptions with Amazon Bedrock** 

  Use Amazon Bedrock in your solution to automate your product review and approval process for an e-commerce marketplace or retail website. 

   [Explore the solution](https://aws.amazon.com/solutions/guidance/generating-product-descriptions-with-amazon-bedrock/) 

  

------
#### [ Amazon Bedrock IDE ]

**Note**  
Amazon Bedrock Studio, renamed to Amazon Bedrock IDE, is available in Amazon SageMaker Unified Studio
+  **What is Amazon Bedrock IDE?** 

   Use Amazon Bedrock IDE to discover Amazon Bedrock models, and build generative AI apps that use Amazon Bedrock models and features.

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html) 

  
+  **Build generative AI applications with Amazon Bedrock IDE** 

  This blog post describes how you can build applications using a wide array of top performing models. It then explains how to evaluate and share your generative AI apps with Amazon Bedrock IDE.

   [Read the blog](https://aws.amazon.com/blogs/machine-learning/build-generative-ai-applications-quickly-with-amazon-bedrock-ide-in-amazon-sagemaker-unified-studio/) 

  
+  **Building a chat app with Amazon Bedrock IDE** 

  Build an Amazon Bedrock IDE chat agent app that allows users to chat with an Amazon Bedrock model through a conversational interface. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-chat-app.html) 

  

------
#### [ Amazon SageMaker AI ]
+  **What is Amazon SageMaker AI?** 

  Use this fully managed AI service to build, train, and deploy AI models into a production-ready hosted environment. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) 

  
+  **Get started with Amazon SageMaker AI** 

   Set up access to Amazon SageMaker AI, including quick or custom setup steps. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html) 

  
+  **Get started with Amazon SageMaker JumpStart** 

   Explore Amazon SageMaker JumpStart solution templates that set up infrastructure for common use cases, and executable example notebooks for AI with SageMaker AI. 

   [Explore the guide](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) 

  
+  **Model customization with Amazon SageMaker AI** 

  Accelerate AI model customization with serverless reinforcement learning and an AI agent-guided workflow.

   [Explore model customization](https://aws.amazon.com/sagemaker/ai/model-customization/) 

  

------

# Management & Governance
<a name="management-governance"></a>

The following decision guides help you choose AWS services for monitoring, governance, and cost management.

**Topics**
+ [Choosing an AWS monitoring and observability service](#monitoring-on-aws-how-to-choose)
+ [AWS CloudTrail or Amazon CloudWatch?](#cloudtrail-or-cloudwatch)
+ [Choosing an AWS cloud governance service](#cloud-governance-on-aws-how-to-choose)
+ [Choosing an AWS cost management strategy](#cost-management-on-aws-how-to-choose)

## Choosing an AWS monitoring and observability service
<a name="monitoring-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS monitoring and observability services are the best fit for your organization. | 
| **Last updated** | January 12, 2024 | 
| **Covered services** |  +  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/getting-started/) <br />+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/getting-started/) <br />+  [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) <br />+  [AWS Config](https://aws.amazon.com/config/getting-started/) <br />+  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) <br />+  [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html) <br />+  [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-getting-started.html) <br />+  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/getting-started/) <br />+  [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/getting-started/collector) <br />+  [AWS X-Ray](https://aws.amazon.com/xray/getting-started/)   | 

### Introduction
<a name="intro"></a>

Monitoring and observability are critical components for ensuring the availability, performance, reliability, and security of your cloud-based workloads and data.
+ Monitoring involves the systematic collection and analysis of data, such as metrics, logs, and traces, to track the health and efficiency of cloud resources as well as supporting reactive incident management.
+ Observability focuses on understanding the internal state of a system through dynamic, real-time insights, allowing for proactive issue identification and resolution.

AWS offers a range of tools and services for both monitoring and observability. They can be used to collect data, analyze metrics, and create alarms to notify you of issues. In addition, they can provide logs and metrics that you can use to identify and troubleshoot the root cause of problems.

 These services integrate with more than 120 other AWS services (including Amazon EC2, Amazon EKS, Amazon ECS, Lambda, and Amazon S3) and partners, and integrates with a wide range of third-party observability and cloud management tools that use near real-time feeds of AWS-native telemetry.

This guide will help you select the AWS monitoring and observability services and tools that are the best fit for your needs and your organization.

[![AWS Videos](https://img.youtube.com/vi/7PQv9eYCJW8?start=104&end=338/0.jpg)](https://www.youtube.com/watch?v=7PQv9eYCJW8?start=104&end=338)


### Understand
<a name="understand"></a>

To choose the right AWS monitoring and observability tools for your needs, it may help to first understand the range of options available to you and how the main services fit together.

![Diagram showing the available options for AWS monitoring and observability](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/monitoring-and-observability.png)


Start with your three key data sources: logs, metrics, and traces. The data from those sources can be consumed using Amazon CloudWatch, AWS X-Ray, or AWS Distro for OpenTelemetry (ADOT) agents.

Here’s when you might use each of these data collection sources:
+ Use Amazon CloudWatch to [collect custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) from your own applications to monitor operational performance, troubleshoot issues, and spot trends. You can also use the CloudWatch agent for collecting log, metrics and traces.. In addition, you can use open source tools such as Fluent D or FluentBit to collect logs and send them to CloudWatch logs.
+ Use AWS X-Ray to perform [distributed tracing across multiple applications](https://docs.aws.amazon.com/xray/latest/devguide/xray-services.html) and systems to help find latency in a system and target it for improvement. You can use the CloudWatch agent to collect traces and send them to X-Ray.
+ Use AWS Distro for OpenTelemetry to collect metrics and traces.

**Instrumentation**

There are two major categories of instrumentation available within AWS monitoring and observability services: AWS Native Services and Open Source Managed Services.
+ AWS Native Services include Amazon CloudWatch and AWS X-Ray. CloudWatch offers these key features of [Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), [Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html), [Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html), and [Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html), that contribute to how you contextualize your data for insights and analysis.
+ Open Source Managed Services include Amazon Managed Service for Prometheus (a managed monitoring service based on and compatible with the popular Prometheus open source monitoring and alerting solution), Amazon OpenSearch Service, and AWS Distro for OpenTelemetry (which not only supports AWS X-Ray, but also Jaeger and Zipkin Tracing).

**Visualization and analysis**

The data you collect and ingest with these AWS services can be visualized and analysed using the [Amazon CloudWatch Service Map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html), the [AWS X-Ray trace map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html), Amazon Managed Grafana and [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html). 

**Other services**

Other services important to monitoring and observability include:
+ AWS Config provides a detailed view of your resource configurations in your AWS account. This view includes the relationship between your resources and the past configurations of your resources, so you can see how the relationships and configurations of your resources change over time. If you are using [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html), AWS Config evaluates your resource configurations for desired settings.
+ AWS CloudTrail helps you enable operational and risk auditing, governance, and compliance by recording events of actions taken by users, roles or AWS services. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

In addition, you can select from a range of [machine learning](https://aws.amazon.com/getting-started/decision-guides/machine-learning-on-aws-how-to-choose/) and [analytics services](https://aws.amazon.com/getting-started/decision-guides/analytics-on-aws-how-to-choose/) to gain further benefit from your monitoring and observability data.

### Consider
<a name="consider"></a>

Choosing the right monitoring and observability services on AWS depends on your specific requirements and use cases. Here are some criteria to consider when making your decision. 

------
#### [ Monitoring service capabilities ]

Consider whether the service provides [a comprehensive set of tools that encompass metrics, logs, and traces](https://aws-observability.github.io/observability-best-practices/guides/). Metrics offer quantitative data on system performance, logs provide detailed event information, and traces allow you to follow transactions across your infrastructure.

Also assess whether the service supports diverse data types and formats. Additionally, look for advanced features such as anomaly detection, machine learning-driven insights, and the ability to correlate data from different sources. A well-rounded solution should enable holistic visibility into your AWS environment, aiding in efficient troubleshooting, performance optimization, and proactive problem resolution.

The more versatile and integrated the service capabilities, the better equipped you are to gain deep insights into your applications and infrastructure. Review the [AWS Observability section of the Management and Governance Cloud Environment Guide](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html) (part of the AWS Well-Architected Framework) for more details on service capabilities.

------
#### [ Ease of integration ]

Assess how seamlessly the service integrates with your existing AWS infrastructure, applications, and deployment processes.

Look for compatibility with popular programming languages, frameworks, and third-party tools that your organization uses. Also evaluate the availability of SDKs, APIs, and plugins that simplify the integration process. Better integration can facilitate the collection and analysis of data without imposing significant overhead on your applications.

Additionally, [consider whether the service supports common protocols for data ingestion](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/interoperable-functions-5.html). Services that provide better integration can help ensure a smoother onboarding experience, allowing your team to more quickly start monitoring and gaining valuable insights into your AWS environment.

------
#### [ Data retention and storage ]

Data retention and storage capabilities are pivotal considerations in selecting AWS monitoring and observability services. For any service you are considering, examine policies on storing and retaining historical data, as well as scalability to handle increasing data volumes over time.

Assess whether the service supports long-term storage of metrics, logs, and traces, enabling you to perform retrospective analysis and meet compliance requirements. Consider also the ease with which you can access and retrieve archived data.

The service (or services) you use should achieve a balance between providing sufficient retention periods for meaningful trend analysis and managing storage costs effectively. A clear understanding of data retention and storage policies is important when considering how your monitoring setup aligns with both operational needs and regulatory obligations.

------
#### [ Scalability ]

Evaluate how well the service can scale alongside your evolving infrastructure and growing workloads. A scalable solution should seamlessly handle increases in data volume, user activity, and the complexity of your applications.

Consider the elasticity of the service, its ability to accommodate spikes in demand, and whether it supports auto-scaling features to adapt to changing requirements dynamically. Robust scalability helps ensure that your monitoring system remains responsive and effective, providing timely insights even as your AWS environment expands.

By choosing a service with strong scalability, you can confidently support the continuous growth of your applications and infrastructure without compromising on performance or incurring unnecessary operational challenges.

------
#### [ Alerting and notification ]

Assess the alerting capabilities of the service, including the ability to set up alerts based on predefined thresholds, anomalies, or specific events. Look for flexibility in configuring alert conditions and the ease of managing notification channels such as email, SMS, or integrations with collaboration tools.

The service (or services) you choose should provide timely and actionable alerts, enabling your team to respond promptly to potential issues. Consider features such as escalation policies and the ability to acknowledge or suppress alerts.

Integration with popular incident management platforms can enhance the overall incident response workflow. Prioritize a monitoring service that empowers your team to proactively address issues, minimizing downtime and ensuring the continuous health of your AWS environment.

------
#### [ Cost ]

Understand the pricing model of each service, considering factors such as data volume, storage, and any additional features. Review cost information for any service you are considering (such as [this billing and cost summary for Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_billing.html)).

Evaluate whether the pricing structure aligns with your budget and usage patterns. Some services may offer a pay-as-you-go model, while others may have tiered pricing or subscription plans. Consider the potential impact of all costs – including data transfer fees or charges for accessing historical data.

Additionally, assess whether the pricing scales efficiently with the growth of your infrastructure. A clear understanding of costs ensures that your monitoring solution remains cost-effective without compromising on essential features, allowing you to optimize your budget while meeting your operational requirements on AWS.

------
#### [ Customization and extensibility ]

Assess whether the service allows you to tailor dashboards, reports, and alerts to meet your needs. Look for the flexibility to create custom metrics, queries, and visualizations. Integration with third-party tools and support for common APIs enhance the service's extensibility. Evaluate whether the monitoring solution can adapt to the unique needs of your applications and infrastructure.

A highly customizable and extensible service empowers your team to fine-tune monitoring parameters, adapt to evolving use cases, and integrate seamlessly with your existing workflows and tools. Prioritize solutions that provide a high degree of configurability, allowing you to optimize monitoring for your specific AWS environment and operational preferences.

------
#### [ Security and compliance ]

Evaluate how a service provides [adherence to AWS security best practices](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/securityoperations.html), ensuring data confidentiality, integrity, and availability. Check for features such as encryption in transit and at rest, access controls, and secure authentication mechanisms. Assess whether the service supports compliance with relevant regulations and standards applicable to your industry.

Look for audit trail capabilities and the ability to generate compliance reports. The goal is to help safeguard sensitive data by using monitoring practices to align with regulatory requirements.

Prioritize services that provide a robust security posture, enabling your organization to maintain a secure and compliant AWS environment while gaining insights into your applications and infrastructure.

------
#### [ Machine learning and analytics ]

Evaluate whether the service uses machine learning (ML) to provide advanced insights, anomaly detection, and predictive analytics. Look for features that automatically identify patterns, trends, and potential issues within your data.

A robust machine learning component can enhance the accuracy of anomaly detection, reducing false positives and improving the overall effectiveness of your monitoring system. Additionally, consider the depth of analytics provided, such as root cause analysis and trend forecasting. A service with strong machine learning and analytics capabilities empowers your team to proactively address issues, optimize performance, and gain deeper insights into the behavior of your AWS applications and infrastructure.

------
#### [ Global reach ]

Global reach is a critical criterion for AWS monitoring and observability services, particularly if your infrastructure is distributed across multiple Regions. Assess whether the monitoring service provides visibility into the performance and health of your resources across different AWS Regions.

Consider the ability to aggregate and analyze data from diverse geographical locations, ensuring a comprehensive understanding of your global infrastructure. Look for features that support centralized management and monitoring, allowing you to efficiently oversee operations on a global scale.

 A service with strong global reach helps ensure that you can maintain consistent monitoring practices, troubleshoot issues, and optimize performance seamlessly across the entire spectrum of your AWS deployment, irrespective of geographical boundaries. This capability is particularly valuable for organizations with a geographically distributed or multi-cloud infrastructure.

------

### Choose
<a name="choose"></a>

Now that you know the criteria by which you will be evaluating your monitoring and observability options, you are ready to choose which AWS monitoring and observability services might be a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine the service that is the best fit for your organization and use case.



| Use case | What is it optimized for? | Monitoring and observability services | 
| --- |--- |--- |
| Monitoring and alerting | These services are optimized to provide real-time visibility, proactive issue detection, resource optimization, and efficient incident response, contributing to overall application and infrastructure health.  | [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br />[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) | 
|  Application performance monitoring  |  These services provide comprehensive insights into application behavior, offer tools for identifying and resolving performance bottlenecks, aid in efficient troubleshooting, and contribute to delivering modern user experiences across distributed and web applications.   |  [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)  | 
| --- |--- |--- |
| Infrastructure observability | These services provide a holistic view of your cloud resources, helping you make more informed decisions about resource utilization, performance optimization, and cost-efficiency.  | [Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)<br />[Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) | 
|  Logging and analysis  |  These services help you efficiently manage and analyze log data, troubleshoot, detect anomalies, support security, meeting compliance requirements, and get actionable insights into your applications and infrastructure.   |  [Amazon Cloudwatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) [Amazon CloudWatch Logs Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)  | 
| --- |--- |--- |
| Security and compliance monitoring | Optimized to provide a robust security framework, enabling proactive threat detection, continuous monitoring, compliance tracking, and audit capabilities to help safeguard your AWS resources and maintain a secure and compliant environment.  | [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)<br />[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)<br />[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) | 
|  Network monitoring  |  These services provide visibility into network traffic, enhance security by detecting and preventing threats, enable efficient network traffic management, and support incident response activities.   |  [Amazon CloudWatch Network Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)  | 
| --- |--- |--- |
| Distributed tracing | These services provide a comprehensive view of the interactions and dependencies within your distributed applications. They enable you to diagnose performance bottlenecks, optimize application performance, and support the smooth functioning of complex systems by offering insights into how different parts of your application communicate and interact.  | [AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction)<br />[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)<br />[Amazon CloudWatch Application Signals (Preview)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) | 
|  Hybrid and multicloud observability  |  Maintain reliable operations, provide modern digital experiences for your customers, and get help to meet service level objectives and performance commitments.   |  [Amazon CloudWatch (hybrid and multicloud support)](https://aws.amazon.com/about-aws/whats-new/2023/11/cloudwatch-hybrid-multicloud-metrics-querying-alarming/)  | 
| --- |--- |--- |

### Use
<a name="use"></a>

You should now have a clear understanding of what each AWS monitoring and observability service (and the supporting AWS tools and services) does, and which might be right for you.

To explore how to use and learn more about each of the available AWS observability services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ Amazon CloudWatch ]
+  **Getting Started with Amazon CloudWatch** 

  Monitor your AWS resources and the applications you run on AWS in real time using Amazon CloudWatch. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  **Getting started with Amazon CloudWatch Metrics** 

  This guide discusses basic monitoring and detailed monitoring, how to graph metrics, and how to use CloudWatch anomaly detection.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  **Set up Container Insights on Amazon EKS and Kubernetes** 

  Set up the Amazon CloudWatch Observability ESK add-on and ADTO on your EKS cluster to send metrics to CloudWatch. You will also learn how to set up Fluent Bit or Fluentd to send logs to CloudWatch Logs.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) 
+  **Getting started with Amazon CloudWatch Application Insights** 

  Learn how to use the console to enable CloudWatch Application Insights to manage your applications for monitoring.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-getting-started.html) 
+  **Using Container Insights** 

  Learn how CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your containerized applications and microservices.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) 
+  **Setting up Container Insights on Amazon ECS** 

  Learn to configure cluster and service level metrics, deploy ADOT to collect EC2 instance level metrics, and set up FireLens to send logs to CloudWatch Logs.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html) 

------
#### [ Amazon CloudWatch Application Insights ]
+  **Getting started with Amazon CloudWatch Application Signals** 

  In this guide, you will learn how to automatically instrument your applications on AWS so that you can monitor current application health and track long-term application performance against your business objectives.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) 
+  **Amazon CloudWatch Application Signals for automatic instrumentation of your applications** 

  This blog post provides an in-depth walk-through the AWS Management Console for Amazon CloudWatch Application Signals demonstrating how to collect telemetry for your EKS clusters.

   [Read the blog post](https://aws.amazon.com/blogs/aws/amazon-cloudwatch-application-signals-for-automatic-instrumentation-of-your-applications-preview/) 
+  **How to monitor application health using SLOs with Amazon CloudWatch Application Signals** 

  This blog post demonstrates how Amazon CloudWatch Application signals enables you to automatically instrument and operate applications on AWS to track application performance against your most important objectives.

   [Read the blog post](https://aws.amazon.com/blogs/mt/how-to-monitor-application-health-using-slos-with-amazon-cloudwatch-application-signals/) 

------
#### [ Amazon CloudWatch Lambda Insights ]
+  **Introducing CloudWatch Lambda Insights** 

  Learn how to create a few “Hello World” Lambda functions and monitor them using Lambda Insights. You will be using the AWS CDK to deploy the architecture.

   [Read the blog](https://aws.amazon.com/blogs/mt/introducing-cloudwatch-lambda-insights/) 
+  **Using Amazon CloudWatch Lambda Insights to Improve Operational Visibility** 

  Learn how to use Lambda Insights to provide simple and convenient operation oversight and visibility into the behavior of your AWS Lambda functions.

   [Read the blog](https://aws.amazon.com/blogs/aws/using-amazon-cloudwatch-lambda-insights-to-improve-operational-visibility/) 

------
#### [ Amazon CloudWatch Logs ]
+  **Getting started with Amazon CloudWatch Logs** 

  Learn how to install the unified CloudWatch agent and how to configure metrics collection with CloudFormation.

   [Read the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html) 
+  **Analyzing log data with CloudWatch Logs Insights** 

  This guide will demonstrate to get started with Logs Insights queries, visualize log data in in graphs, and adding queries to your dashboard.

   [Get started with the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) 
+  **Amazon CloudWatch Logs Insights – Fast, Interactive Log Analytics** 

  Use Logs Insights to utilize the data points, patterns, trends, and insights present in all the various logs created by AWS services to understand how your applications and AWS resources are behaving, identify room for improvement, and address operational issues.

   [Read the blog post](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-logs-insights-fast-interactive-log-analytics/) 

------
#### [ Amazon CloudWatch Synthetics ]
+  **Using synthetic monitoring** 

  This guide demonstrates how to create canaries, configurable scripts that run on a schedule, providing sample code for canary scripts.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 
+  **Secure monitoring of user workflow experience using Amazon CloudWatch Synthetics and AWS Secrets Manager** 

  How to create, deploy, and monitor synthetic monitoring solutions using Amazon CloudWatch Synthetics.

   [Read the blog post](https://aws.amazon.com/blogs/mt/secure-monitoring-of-user-workflow-experience-using-amazon-cloudwatch-synthetics-and-aws-secrets-manager/) 

------
#### [ Amazon EventBridge ]
+  **Getting started with Amazon EventBridge** 

  Learn to create a basic rule to route events to a target.

   [Explore the guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) 
+  **Archive and replay Amazon EventBridge events** 

  Create a function to use as the target for the EventBridge rule using the Lambda console.

   [Explore the guide](https://docs.aws.amazon.com/latest/userguide/eb-get-started.html) 
+  **Log the state of an Amazon EC2 instance using EventBridge** 

  Create an AWS Lambda function to log state changes for an Amazon EC2 instance. You will log the launch of any new EC2 instance.

   [Use the tutorial](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-log-ec2-instance-state.html) 
+  **Building an event-driven application with Amazon EventBridge** 

  Learn how to build and deploy and event-driving application using the AWS Serverless Application Model (AWS SAM) CLI.

   [Read the blog](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/) 

------

------
#### [ AWS CloudTrail ]
+  **Getting started with AWS CloudTrail** 

  AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Here's how to get started with it.

   [Explore the guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
+  **Review AWS account activity** 

  Learn how to review the AWS API activity in your AWS account for services that support CloudTrail.

   [Use the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html) 
+  **Create a trail** 

  Learn how to create a trail to log AWS API activity in all Regions including data and Insights events.

   [Use the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html) 
+  **AWS CloudTrail Log Monitoring workshop** 

  Learn how to integrate CloudTrail logs into CloudWatch and use features such as CloudWatch Log Insights, CloudWatch Metric Filters, CloudWatch Metric Alarms and CloudWatch Dashboards.

   [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2e48b9fc-f721-4417-b811-962b7f31b61c/en-US) 
+  **AWS CloudTrail best practices** 

  Best practices for using CloudTrail to enable auditing across your organization.

   [Read the blog](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/) 

------
#### [ AWS Config ]
+  **Getting started with AWS Config** 

  AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This explains how to get started using it.

   [Explore the guide](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 
+  **Setting up AWS Config (console)** 

  Learn how to set up AWS Config in your AWS accounts using the AWS Management Console.

   [Explore the guide](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) 
+  **Setting up AWS Config with the AWS CLI** 

  Learn how to set up AWS Config in your AWS accounts using the AWS CLI.

   [Explore the guide](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html) 

------
#### [ Amazon Managed Grafana ]
+  **Getting started with Amazon Managed Grafana** 

  Learn how to get started with Amazon Managed Grafana and create your first workspace and then connect to the Grafana console in that workspace.

   [Explore the guide](https://docs.aws.amazon.com/grafana/latest/userguide/getting-started-with-AMG.html) 
+  **Amazon Managed Grafana - Getting Started** 

  Learn how to integrate with Amazon Managed Service for Prometheus and how to create custom dashboards.

   [Read the blog](https://aws.amazon.com/blogs/mt/amazon-managed-grafana-getting-started/) 
+  **Visualize and gain insights into your AWS cost and usage with Amazon Managed Grafana** 

  Learn how to visualize and analyze your AWS cost and usage data with Amazon Managed Grafana.

   [Read the blog](https://aws.amazon.com/blogs/mt/visualize-and-gain-insights-into-your-aws-cost-and-usage-with-amazon-managed-grafana/) 

------
#### [ Amazon Managed Service for Prometheus ]
+  **Getting started with Amazon Managed Service for Prometheus** 

  Create Amazon Managed Service for Prometheus workspaces, set up the ingestion of Prometheus metrics to those workspaces, and query those metrics.

   [Explore the guide](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-getting-started.html) 
+  **Container Insights Prometheus metrics monitoring** 

  Learn how to automate the discovery of Prometheus metrics from containerized workloads using CloudWatch Container Insights.

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus.html) 
+  **Amazon Managed Service for Prometheus FAQs** 

  Frequently asked questions about Amazon Managed Service for Prometheus.

   [Read the FAQs](https://aws.amazon.com/prometheus/faqs/) 

------
#### [ Amazon OpenSearch Service ]
+  **Getting started with Amazon OpenSearch Service** 

  Use Amazon OpenSearch Service to create and configure a test domain. An OpenSearch Service domain is synonymous with an OpenSearch cluster.

   [Explore the guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) 
+  **Getting started with Amazon OpenSearch Serverless** 

  This tutorial walks you through the basic steps to get an Amazon OpenSearch Serverless search collection up and running quickly

   [Use the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html) 
+  **Creating and searching for documents in Amazon OpenSearch Service** 

  Learn how to create and search for a document in Amazon OpenSearch Service. 

   [Use the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/quick-start.html) 
+  **Getting started with Amazon OpenSearch Ingestion ** 

  Learn how to use Amazon OpenSearch Ingestion to ingest data into a domain and also a collection.

   [Explore the guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-getting-started-tutorials.html) 
+  **SIEM on Amazon OpenSearch Service Workshop** 

  Build a security log analysis platform on Amazon OpenSearch Service and get started with building a cost-efficient solution for log ingestion, analysis and dashboarding.

   [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/60a6ee4e-e32d-42f5-bd9b-4a2f7c135a72/en-US) 
+  **Creating and searching for documents in Amazon OpenSearch Service** 

  Learn how to create and search for a document in Amazon OpenSearch Service. 

   [Use the tutorial](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/quick-start.html) 

------
#### [ AWS Distro for OpenTelemetry ]
+  **Getting Started with the AWS Distro for OpenTelemetry (ADOT) Collector** 

  Walk through the steps to build the ADOT Collection locally.

   [Explore the guide](https://aws-otel.github.io/docs/getting-started/collector) 
+  **AWS Distro for OpenTelemetry JavaScript** 

  Learn how to instrument your JavaScript applications and send correlated metrics to various AWS monitoring solutions.

   [Explore the guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-js-opentel-sdk.html) 
+  **AWS Distro for OpenTelemetry Python** 

  This guide will demonstrate how to instrument your Python applications and send correlated metrics to various AWS monitoring solutions.

   [Explore the guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-python-opentel-sdk.html) 

------
#### [ AWS X-Ray ]
+  **Getting started with AWS X-Ray** 

  This guide will walk you through launching a sample application. Then you will learn how to instrument your application and explore other services that are integrated with X-Ray.

   [Explore the guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html) 
+  **One Observability Workshop** 

  This workshop provides you a hands-on experience with a wide variety of tool AWS offers for monitoring and observability including AWS X-Ray and ADOT.

   [Use the workshop](https://catalog.workshops.aws/observability/en-US) 
+  **Application logging and monitoring using AWS X-Ray** 

  Learn how AWS X-Ray collects data about requests that your application serves, and it helps you view, filter, and gain insights into that data to identify issues and opportunities for optimization.

   [Explore the guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/x-ray.html) 

------

### Explore
<a name="explore"></a>
+ **Solutions**

  Explore solutions to help you implement monitoring and observability on AWS.

  [ Explore solutions](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram%7Ccontent-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your monitoring and observability options.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all)
+ **Video, patterns, and guidance**

  Explore additional architectural guidance covering common use cases for monitoring and observability services.

  [Explore additional assets](https://aws.amazon.com/architecture/management-governance/?achp_navtc9&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)

## AWS CloudTrail or Amazon CloudWatch?
<a name="cloudtrail-or-cloudwatch"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | To help you determine whether AWS CloudTrail or Amazon CloudWatch is the right choice for maintaining the visibility, security, and operational efficiency of your cloud environment. | 
| **Last updated** | September 20, 2024 | 
| **Covered services** |  +  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) <br />+  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)   | 

### Introduction
<a name="introduction"></a>

 When deploying critical business workloads to the AWS Cloud, it is essential to maintain visibility, security, and operational efficiency in your cloud environment. There are a number of key areas to address: 
+  **Operational transparency** — Tracking who is doing what in your cloud environment and monitoring the performance of your resources. 
+  **Security assurance** — Detecting unusual API calls or resource utilization that might indicate a security threat. 
+  **Regulatory compliance** — Maintaining detailed logs of user activities and infrastructure changes for audit purposes. 
+  **Performance management** — Monitoring resource utilization and application performance metrics. 
+  **Incident response** — data and alerts to quickly identify and respond to operational issues. 
+  **Cost control** — insights into resource usage to help manage cloud spending. 
+  **Automation** — automated responses to specific events or performance thresholds. 

 AWS offers two key services to assist in addressing these concerns:
+ **[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)** is primarily focused on governance, compliance, and operational auditing. It logs all API calls made within your AWS environment. Key features: 
  +  Tracks all AWS account activities, including API calls, actions taken in the AWS Management Console, AWS SDKs, command line tools, and other AWS services. 
  +  Provides a detailed log of every action, including who made the call, the service used, and what resources were affected. 
  +  Useful for security auditing, tracking user activity, and identifying potentially malicious actions. 
+  **[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)** is a monitoring and observability service that provides data and actionable insights for AWS, on-premises, and hybrid applications and infrastructure. Key features include: 
  +  Monitors AWS resources and the applications running on AWS in real-time, including metrics, logs, and alarms. 
  +  Provides detailed insights into system performance, error rates, resource utilization, and more. 
  +  Allows setting up alarms to trigger actions (for example, scaling resources) based on specific conditions. 

While both services are critical to a robust, secure cloud environment, they differ in their use cases, and the capabilities they offer. 

Here's a high-level view of the key differences between these services to get you started.


| **Category**  | **CloudTrail**  | **CloudWatch**  | 
| --- | --- | --- | 
| Primary purpose  | API activity tracking and auditing  | Real-time monitoring and performance management  | 
| Data collected  | Logs of API calls, including who made the call, when, and what resources were affected  | Metrics, logs, and events related to resource performance and application behavior  | 
| Use cases  | Security auditing, compliance, and tracking changes in the environment  | Monitoring resource utilization, setting alarms, and performance management  | 
| Security and compliance  | Helps meet security and compliance requirements by providing detailed activity logs  |  Monitors system performance for security anomalies and helps maintain operational integrity  | 
| Log retention  | Last 90 days of event history. Can create trails and event data stores (using CloudTrail Lake) to keep a record of activity for longer than 90 days.  | Short-term data retention for real-time monitoring and troubleshooting  | 
| Alarms and notifications  | Not primarily used for alarms, but can trigger actions based on API activity  | Enables setting alarms for specific metrics or log events, with automated responses  | 
| Integration  | Often used with security services like AWS Config and IAM for enhanced security management  |  Integrates with a wide range of AWS services for comprehensive monitoring and automation  | 
| Cost considerations  | Costs based on the volume of logs generated and stored  | Costs based on the number of metrics, logs, and alarms monitored  | 
| Data granularity  | Provides detailed logs of every API call with granular information  | Provides aggregated metrics and log data for real-time monitoring  | 
| Access control  | Allows you to track access patterns and changes in user permissions  | Helps you monitor and optimize access to resources based on performance metrics  | 
| Resource coverage  | AWS account-wide  | Individual AWS resources  | 
|  Real-time tracking  | Near real-time (within 5 minutes)  | Real-time or near real-time  | 
| Visualization  | Limited; often used with other tools  | Built-in dashboards and graphing  | 

### Differences between CloudTrail and CloudWatch
<a name="ct-cw-differences"></a>

 Explore the differences between CloudTrail and CloudWatch in a number of key areas. 

------
#### [ Primary purpose ]

**AWS CloudTrail**
+ Provides a comprehensive audit trail of all API activity within an AWS account. Focuses on recording who did what, when, and from where. This includes actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. CloudTrail answers questions like "Who terminated this EC2 instance?" or "What changes were made to this IAM policy?" 

**Amazon CloudWatch**
+ Monitors the operational health and performance of AWS resources and applications. CloudWatch collects and tracks metrics, collects and monitors log files, and sets alarms. It helps you understand how your applications are performing and respond to system-wide performance changes. CloudWatch answers questions like "Is my Amazon EC2 instance's CPU utilization too high?" or "How many errors is my Lambda function generating?"

**Summary**

CloudTrail helps you track and audit user activity for security and compliance, while CloudWatch is about monitoring and optimizing system performance and operational health. Both tools serve distinct, yet complementary, roles in managing a cloud environment. 

------
#### [ Data collected ]

**AWS CloudTrail**
+ Focuses on capturing detailed logs of all API activity within your AWS environment. This includes information on who made the API call, when it was made, the action taken, and the resources involved. CloudTrail's logs provide a comprehensive audit trail, essential for tracking changes, ensuring compliance, and investigating security incidents. 

**Amazon CloudWatch**
+ Collects performance and operational data from your AWS resources and applications. This includes metrics such as CPU usage, memory utilization, network traffic, and application logs, as well as custom metrics you can define. The data collected by CloudWatch is used for real-time monitoring, performance optimization, and setting alarms to trigger automated actions based on specific conditions. 

**Summary**

CloudTrail collects data related to user activity and API usage for auditing and security purposes, while CloudWatch collects metrics and logs to monitor, manage, and optimize system performance and operational health. Both provide critical insights but serve different aspects of cloud management.

------
#### [ Use cases ]

**AWS CloudTrail**
+ Primarily used for security auditing, compliance, and operational auditing. CloudTrail provides a detailed record of API calls and user activity within your AWS environment, making it essential for tracking changes, investigating security incidents, and ensuring that your organization meets regulatory requirements. For example, CloudTrail is useful in scenarios where you need to monitor who accessed specific resources, track changes made to configurations, or audit activity across multiple AWS accounts. 

**Amazon CloudWatch**
+ Designed for real-time monitoring, performance management, and operational efficiency. CloudWatch is used to monitor the health of your AWS resources and applications by collecting and tracking metrics, logs, and events. CloudWatch enables you to set alarms that trigger automated actions, such as scaling resources or sending notifications when certain thresholds are met. Use cases for CloudWatch include monitoring application performance, managing resource utilization, detecting anomalies, and ensuring your systems are running optimally to prevent downtime. 

------
#### [ Security and compliance ]

**AWS CloudTrail**
+ Crucial for maintaining security and compliance in AWS environments. CloudTrail provides a comprehensive audit trail of all API calls, including who made the call, when it was made, and the actions taken. This detailed logging is essential for meeting compliance standards, conducting security audits, and investigating incidents. By tracking user activity and changes to resources, CloudTrail helps ensure accountability and transparency, which are key requirements for many regulatory frameworks.

**Amazon CloudWatch**
+ Plays a role in security by enabling the detection of operational anomalies. For example, you can use CloudWatch to monitor metrics that indicate potential security issues, such as unusual spikes in network traffic or CPU usage. Additionally, CloudWatch can trigger alarms and automated responses when certain thresholds are met, allowing for proactive incident management. Logs captured in CloudWatch can also be used to track operational events, which can be vital for understanding the context of security incidents. 

**Summary**

Together, CloudTrail provides the audit logs necessary for compliance, while CloudWatch offers real-time monitoring that helps detect and respond to security threats, contributing to a secure and compliant cloud environment. 

------
#### [ Log retention ]

**AWS CloudTrail**
+ By default, the CloudTrail event history records the last 90 days of management events for your account. 
+ Users can create a trail to store logs indefinitely in an S3 bucket. 
+ There's no automatic deletion of logs stored in Amazon S3, allowing for long-term retention. 
+ Users can implement lifecycle policies on S3 buckets to manage long-term storage costs. 
+ CloudTrail can be configured to send logs to CloudWatch Logs for more flexible retention options. 

**Amazon CloudWatch**
+ Log retention in CloudWatch Logs is more flexible and configurable. 
+ Default retention period varies by log group, typically set to "Never Expire". 
+ Users can set custom retention periods ranging from one day to 10 years, or choose indefinite retention. 
+ Different log groups can have different retention periods. 
+ After the retention period, logs are automatically deleted to manage storage costs. 
+ CloudWatch Logs can be exported to Amazon S3 for longer-term storage if needed. 

------
#### [ Alarms and notifications ]

**AWS CloudTrail**
+ Primarily focuses on logging API activity and does not have built-in alarm or notification capabilities. However, you can integrate with CloudWatch Logs and CloudWatch alarms to configure alarms for CloudTrail events. This setup is typically used to alert you about security-related events, such as unauthorized access attempts or changes to critical resources. 

**Amazon CloudWatch**
+ Specifically designed for real-time monitoring and includes robust alarm and notification features. CloudWatch allows you to set alarms based on metrics, log data, or custom-defined thresholds. When these thresholds are breached, CloudWatch can send notifications via Amazon SNS (Amazon Simple Notification Service), trigger automated actions like scaling instances, or perform custom remediation steps using AWS Lambda. This makes CloudWatch an essential tool for proactive system management, alerting you to performance issues or operational anomalies as they happen. 

------
#### [ Integration ]

CloudTrail and CloudWatch offer extensive integration options with other AWS services and external tools, enhancing their functionality and utility.

**CloudTrail integrations**
+ Amazon S3: Store logs long-term for archival and analysis 
+ CloudWatch Logs: Enable real-time log analysis and alerting 
+ Amazon EventBridge: Trigger automated actions based on API events 
+ AWS Config: Provide input for configuration tracking and compliance 
+ AWS Security Hub CSPM: Contribute to centralized security posture management 
+ AWS Lake Formation: Enable data lake governance of CloudTrail logs 
+ Amazon Athena: Perform SQL queries on CloudTrail logs stored in Amazon S3 

**CloudWatch integrations**
+ Amazon SNS: Send notifications for alarms and events 
+ AWS Lambda: Trigger serverless functions based on metrics or logs 
+ Amazon EC2 Auto Scaling: Adjust capacity based on performance metrics 
+ AWS Systems Manager: Automate operational tasks based on CloudWatch data 
+ AWS X-Ray: Combine with trace data for in-depth application insights 
+ Container services (Amazon ECS, Amazon EKS): Monitor containerized applications 
+ Third-party tools: Export metrics and logs to external monitoring platforms 

------
#### [ Cost considerations ]

**AWS CloudTrail**
+ CloudTrail is priced primarily on the number of events logged and stored. By default, CloudTrail event history records and stores, without charge, the last 90 days of management events for your account. However, if you enable data events (such as S3 object-level actions) or create multiple trails, you incur charges based on the volume of events and the storage required in Amazon S3. Additional costs might arise if you use advanced features like CloudTrail Insights, which provide deeper analysis of unusual API activity. 

**Amazon CloudWatch**
+ CloudWatch has a more complex pricing structure based on several factors, including the number of custom metrics you monitor, the number of log events ingested and stored, and the use of alarms and dashboards. Basic monitoring for AWS services is without charge, but detailed monitoring and custom metrics incur charges. Log storage is priced based on the volume of data ingested and retained, with additional costs for setting up and maintaining alarms or using CloudWatch Logs Insights for advanced log analysis. 

------
#### [ Data granularity ]

**AWS CloudTrail**
+ CloudTrail provides high granularity by logging every individual API call made within your AWS environment. Each log entry includes detailed information such as who made the request, the action performed, the resources affected, and the time of the action. This level of detail is crucial for auditing, security monitoring, and compliance, as it allows you to trace specific user actions and changes down to the exact API call. 

**Amazon CloudWatch**
+ CloudWatch focuses on aggregated data for monitoring and performance management. It collects metrics at regular intervals (typically every minute or five minutes) and logs operational data from AWS resources. While CloudWatch provides detailed insights into system performance and application behavior, its data is more aggregated compared to CloudTrail. For instance, you can monitor average CPU usage over time rather than individual requests or actions. CloudWatch Logs, however, can provide more granular data similar to CloudTrail but is often used for analyzing operational logs rather than tracking API calls. 

------
#### [ Real-time tracking ]

**AWS CloudTrail**
+ CloudTrail is not inherently designed for real-time tracking but can be configured to provide near-real-time alerts. By default, CloudTrail records API activity, but there is a slight delay in log delivery. For more immediate tracking, you can integrate CloudTrail with Amazon CloudWatch Events or AWS Lambda to trigger actions based on specific API calls or activities as soon as they are logged. This setup allows for near-real-time monitoring of critical security events or configuration changes. 

**Amazon CloudWatch**
+ CloudWatch, on the other hand, is built for real-time tracking of system and application performance. It continuously monitors metrics from AWS resources and can instantly trigger alarms or notifications when predefined thresholds are exceeded. CloudWatch also collects and analyzes log data in real-time, enabling you to monitor application logs, detect anomalies, and respond to operational issues as they occur. This makes CloudWatch an essential tool for maintaining the health and performance of your AWS environment in real time. 

------

### Use
<a name="use"></a>

Now that you've read about the criteria for choosing between AWS CloudTrail and Amazon CloudWatch, you can select the service that meets your needs, and use the following information to help you get started using each of them. 

------
#### [ AWS CloudTrail ]
+  **Getting started with AWS CloudTrail** 

   AWS CloudTrail is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Here's how to get started with it. 

   [Explore the guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
+  **Review AWS account activity** 

   Learn how to review recent AWS API activity in your AWS account using CloudTrail's event history feature. 

   [Use the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) 
+  **Create a trail** 

   Learn how to create a trail to log AWS API activity in all Regions including data and Insights events. 

   [Use the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html) 
+  **Security best practices in AWS CloudTrail** 

   This guide provides detective and preventative security best practices for using AWS CloudTrail in your organization. 

   [Explore the guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html) 

------
#### [ Amazon CloudWatch ]
+  **Getting Started with Amazon CloudWatch** 

   Monitor your AWS resources and the applications you run on AWS in real time using Amazon CloudWatch. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  **Getting started with Amazon CloudWatch Metrics** 

   This guide discusses basic monitoring and detailed monitoring, how to graph metrics, and how to use CloudWatch anomaly detection. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) 
+  **Set up Container Insights on Amazon EKS and Kubernetes** 

   Set up the Amazon CloudWatch Observability ESK add-on and ADTO on your EKS cluster to send metrics to CloudWatch. You will also learn how to set up Fluent Bit or Fluentd to send logs to CloudWatch Logs. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) 
+  **Getting started with Amazon CloudWatch Application Insights** 

   Learn how to use the console to enable CloudWatch Application Insights to manage your applications for monitoring. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-getting-started.html) 
+  **Using Container Insights** 

   Learn how CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your containerized applications and microservices. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html) 
+  **Setting up Container Insights on Amazon ECS** 

   Learn to configure cluster and service level metrics, deploy ADOT to collect EC2 instance level metrics, and set up FireLens to send logs to CloudWatch Logs. 

   [Explore the guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html) 

------

## Choosing an AWS cloud governance service
<a name="cloud-governance-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS cloud governance services are the best fit for your organization. | 
| **Last updated** | December 23, 2024 | 
| **Covered services** | + [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)<br />+ [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)<br />+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)<br />+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)<br />+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)<br />+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)<br />+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br />+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) <br />+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)<br />+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)<br />+ [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)  | 

### Introduction to AWS cloud governance
<a name="introduction"></a>

 Cloud governance is a set of rules, processes, and reports that helps you align your AWS Cloud use toward your business objectives. 

 This covers security, by enabling multi-account strategies, continuous monitoring, and control policies. It covers compliance, by automating checks, reporting, and remediation. It covers operations, by applying controls enterprise wide. It covers identity by centralizing identity and access management at scale. It covers cost, by facilitating usage reports and policy enforcement. And it covers resilience, by helping integrate assessments and testing into CI/CD pipelines for validation. 

 We offer a range of services to help you set up, manage, monitor, and control the use of accounts, services, and resources in the cloud, thereby implementing cloud governance best practices. 

 The guide is designed to help you decide which AWS cloud governance services are the best fit for your organization, to strengthen operational resilience, optimize costs, and build controls to help comply with regulations or corporate standards, while maintaining development speed and accelerating innovation. 

[![AWS Videos](https://img.youtube.com/vi/U0y9l5V3mMQ?start=131&end=501/0.jpg)](https://www.youtube.com/watch?v=U0y9l5V3mMQ?start=131&end=501)


### Understand AWS cloud governance
<a name="understand"></a>

![Diagram showing AWS services used in cloud governance applications, including defining requirements, deploying and operating, and measuring and assessing.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cloudgov-understanding.png)


 The previous diagram shows how cloud governance draws on multiple AWS services, which allow you to define your governance requirements, deploy and operate your systems, and measure and assess their performance. The services provide built-in governance control, resource provisioning to align with your governance policies, and operations tools to help you monitor and manage your environment. 

 Harnessing AWS cloud governance services helps you ensure your cloud use supports your business objectives, Specifically, they enable you to improve speed and agility for developers, operate in a dynamic regulatory environment, streamline mergers and acquisitions, and strengthen operational resilience: 
+  **Improve speed and agility for developers —** Quickly spin new environments through APIs making sure your developers are not waiting on weeks long provisioning cycles, and accelerate provisioning of CI/CD pipeline. Find and prevent defects early in the software delivery process, using pre-built controls and rules, and infrastructure-as-code templates for provisioning common resources efficiently. 
+  **Operate in a dynamic regulatory environment —** Create always-on boundaries to protect and control access to data across AWS, codify your compliance requirements, and automate the assessment of your resource configurations across your organization. 
+  **Streamline mergers and acquisitions —** Migrate workloads faster by building a secure, well-architected, multi-account environment. Centralize account creation, allocate resources, group accounts, and apply governance policies and controls easily and quickly. Adopt a programmatic approach to multi-account management at scale. 
+  **Strengthen operational resilience —** Set up a secure, well-architected, resilient multi-account environment quickly. Run assessments of your workloads to uncover potential resilience-related weaknesses. Conducts automated checks against five key areas – cost optimization, performance, security, fault tolerance, and service limits – and receive recommendations that enable you to follow known best practices. 
+  **Optimize costs —** Visualize, understand, and manage costs and usage over time. Continuously analyze resource utilization, identify underutilized resources, and terminate idle resources. 

 Cloud governance best practices can effectively be built in when you set up and operate your workloads on AWS. Interoperable services help you achieve consistent, centralized governance over your IT estate, including AWS and third-party products. Breadth and depth of controls across AWS services help you meet evolving regulatory requirements and minimize security risks. 

### Consider AWS cloud governance criteria
<a name="consider"></a>

 The following section outlines some of the key criteria to consider when choosing a cloud governance strategy. In particular, it discusses the different kinds of cloud environment, control regime, and developer support opportunities that might be applicable to your organization and business objectives. 

------
#### [ Multi-account strategy ]

 **What it is:** Implementing cloud environment best practices hinges on adopting a secure multi-account strategy. Use accounts as building blocks, and group them into [organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html#:~:text=You%20can%20use%20organizational%20units,OU%20automatically%20inherit%20the%20policy.), such as foundational OUs for security and infrastructure, and additional OUs for sandboxing and workloads. 

 **Why it matters:** A multi-account strategy provides natural boundaries and isolation in your cloud environment. This in turn allows you to manage quotas and account limits, automate the provisioning and customization of accounts, and apply the principle of least privilege by restricting access to your management account. It enables visibility to track user activity and risk across your environment. Your multi-account strategy acts as the foundation on which you can build for migration projects or organizational changes like mergers and acquisitions. 

 Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to consolidate multiple AWS accounts into an organization, which you can use to allocate resources, group accounts, and apply governance policies. 

 Use [AWS Control Tower](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-CTower.html) as an orchestration service, layered on top of AWS Organizations, to help structure your AWS estate, and extend governance over OUs and your multi-account environment.

------
#### [ Controls management best practices ]

 **What it is:** Implementing controls management best practices can include a range of approaches. Detective controls catch resources that violate defined security policies. Preventive controls protect security baselines by blocking specific actions. And proactive control scan resources before they are provisioned, stop non-compliant code from being deployed, and instruct developers to remediate them. Interoperable AWS services give you centralized governance and control over your entire IT estate, including AWS and third-party products, as you grow into new markets. 

 **Why it matters:** Controls management best practices allow you to programmatically implement controls at scale, and automatically configure compliance or remediate non-compliance. This is particularly important if your organization operates in a regulated industry, such healthcare, life sciences, financial services, or the public sector, where specific regulatory frameworks apply, or adheres to specific corporate standards, or data residency and digital sovereignty requirements. 

 Consider opportunities for orchestrating multiple AWS services to ensure your organization's security and compliance needs, using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), defining configuration settings and detecting deviation from them, using [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html), and auditing AWS usage and compliance with regulations and industry standards, with [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html). 

------
#### [ Cloud governance for developers ]

 **What it is:** Implementing cloud governance best practices for developers can include using infrastructure as code (IaC) to ensure repeatability and consistency in their work, and establishing processes to detect security vulnerabilities. 

 **Why it matters:** This helps teams move fast while being confident in their governance processes. It gives developers a single source of truth that can be deployed to the whole stack, infrastructure that they can replicate, redeploy, and repurpose, the ability to control versioning on infrastructure and applications together, and a choice of self-service actions. 

 Cloud governance for developers can also involve detecting security vulnerabilities in code. This helps them improve code quality, identify critical issues, ensure consistent release pipelines, and launch projects with blueprints. 

 Consider how you might provide builders with pre-approved infrastructure-as-code templates, and corresponding IAM policies that dictate who, where, and how they can be used, using an AWS service like [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html). 

------
#### [ Scalability and flexibility ]

 **What it is:** Choose AWS services that will help your cloud governance measures grow seamlessly with your infrastructure and adapt to evolving requirements. Consider how your organization will grow, and how fast. 

 **Why it matters:** Considering scalability and flexibility helps you ensure that your cloud governance arrangements are robust, responsive, and capable of supporting dynamic business environments. 

 To help you scale quickly, AWS Control Tower orchestrates the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations and AWS IAM Identity Center, to build a landing zone in less than an hour. Control Tower sets up and manages resources on your behalf. 

 AWS Organizations enables you to manage [40\+ services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)' resources across multiple accounts. This gives individual application teams the flexibility and visibility to manage cloud governance needs that are specific to their workload, while also giving them visibility to centralized teams. 

------

### Choose an AWS cloud governance service
<a name="choose"></a>

 Now you know the criteria by which you will be evaluating your cloud governance options, you are ready to choose which AWS cloud governance service may be a good fit for your organizational needs. The following table highlights which services are optimized for which circumstances. Use it to help determine the service that is the best fit for your organization and use case. 


|  Type of use case  |  When would you use it?  |  Recommended service  | 
| --- | --- | --- | 
|  Defining requirements  |  To provide on-demand downloads of AWS security and compliance documents.  |  [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)  | 
|  Deploying and operating  |  To speed up cloud provisioning with infrastructure as code.  |  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)  | 
|   |  To represent your ideal configuration settings and detect if AWS resources drift from it.  |  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)  | 
|   |  To setup and orchestrate multiple AWS services on your behalf while helping you meet the security and compliance needs of your organization.  |  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)  | 
|   |  To consolidate multiple AWS accounts into an organization, which you can use to allocate resources, group accounts, apply governance policies, and manage centrally and at scale.  |  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)  | 
|   |  To run automated and continuous checks against the rules in a set of supported security standards.  |  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)  | 
|   |  To provide builders with pre-approved infrastructure-as-code templates, and corresponding IAM policies, that dictate who, where, and how they can be used.  |  [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html)  | 
|   |  To provide secure end-to-end management of resources on AWS and in multicloud and hybrid environments.  |  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)  | 
|  Measuring and assessing  |  To audit AWS usage and assess risking and compliance with regulations and industry standards.  |  [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)  | 
|   |  To enable operational and risk auditing, governance, and compliance of your AWS account.  |  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)  | 
|   |  To monitor your AWS resources and the applications you run on AWS in real time.  |  [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)  | 
|   |  To manage software licenses from vendors centrally across AWS and your on-premises environments.  |  [AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)  | 
|   |  To evaluate usage and configuration against best practices.  |  [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)  | 

### Use an AWS cloud governance service
<a name="use"></a>

 You should now have a clear understanding of what each AWS cloud governance service does, and which ones might be right for you. 

 To explore how to use and learn more about each of the available AWS cloud governance services, we have provided a pathway to explore how each of them works. The following sections provide links to in-depth documentation, hands-on tutorials, and other resources to get you started. 

------
#### [ AWS Artifact ]
+ **Getting started with AWS Artifact**

  Download security and compliance reports, manage legal agreements, and manage notifications.

   [Explore the guide »](https://docs.aws.amazon.com/artifact/latest/ug/getting-started.html)
+ **Managing agreements in AWS Artifact**

  Use the AWS Management Console to review, accept, and manage agreements for your account or organization.

   [Explore the guide »](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)
+ **Prepare for an Audit in AWS Part 1 – AWS Audit Manager, AWS Config, and AWS Artifact**

  Use AWS services services to help you automate the collection of evidence that's used in audits.

   [Read the blog »](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/)

------
#### [ AWS Audit Manager ]
+  **Getting started with AWS Audit Manager** 

   Enable Audit Manager by using the AWS Management Console, the Audit Manager API, or the AWS CLI. 

   [Explore the guide »](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html) 
+  **Tutorial for Audit Owners: Creating an assessment** 

   Create an assessment by using the Audit Manager Sample Framework. 

   [Get started with the tutorial »](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-audit-owners.html) 
+  **Tutorial for Delegates: Reviewing a control set** 

   Review a control set that was shared with you by an audit owner in Audit Manager. 

   [Get started with the tutorial »](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-delegates.html) 

------
#### [ AWS CloudTrail ]
+  **View event history** 

   Review the AWS API activity in your AWS account for services that support CloudTrail. 

   [Get started with the tutorial »](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html) 
+  **Create a trail to log management events** 

   Create a trail to log management events in all Regions. 

   [Get started with the tutorial »](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html) 

------
#### [ AWS Config ]
+  **AWS Config features** 

   Explore the resource tracking capabilities of AWS Config, from configuration histories and snapshots to customizable rules and conformance packs. 

   [Explore the guidance »](https://aws.amazon.com/config/features/) 
+  **How AWS Config Works** 

   Dive deeper on AWS Config, and learn how the service discovers and tracks resources, and delivers configuration items through various channels. 

   [Explore the guide »](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html) 
+  **Risk and Compliance workshop** 

   Automate controls by using AWS Config and AWS Managed Config Rules. 

   [Explore the workshop »](https://catalog.us-east-1.prod.workshops.aws/workshops/dd2bea89-dc7a-4bda-966a-70b4ff6e90e0/en-US/3-detective-controls-config/1-config-setup) 
+  **AWS Config Rule Development Kit library: Build and operate rules at scale** 

   Use the Rule Development Kit (RDK) to build a custom AWS Config rule and deploy it with the RDKLib. 

   [Read the blog »](https://aws.amazon.com/blogs/mt/aws-config-rule-development-kit-library-build-and-operate-rules-at-scale/) 

------
#### [ AWS Control Tower ]
+  **Getting started with AWS Control Tower** 

   Learn how to set up your landing zone using the AWS Control Tower console or APIs. 

   [Explore the guide »](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) 
+  **AWS Control Tower controls management workshop** 

   Learn how to set up governance on your multi-account environment to align with AWS best practices and common compliance frameworks. 

   [Explore the workshop »](https://catalog.workshops.aws/control-tower/en-US/controls) 
+  **Modernizing Account Management with Amazon Bedrock and AWS Control Tower** 

   Provision a security tooling account and leverage generative AI to expedite the AWS account setup and management process. 

   [Read the blog »](https://aws.amazon.com/blogs/mt/modernizing-account-management-with-amazon-bedrock-and-aws-control-tower/) 
+  **Building a well-architected AWS GovCloud (US) environment with AWS Control Tower** 

   Set up your governance in the AWS GovCloud (US) Regions, including governing your AWS workloads by using Organizational Units (OUs) and AWS accounts. 

   [Read the blog »](https://aws.amazon.com/blogs/mt/building-a-well-architected-aws-govcloud-us-environment-with-aws-control-tower/) 

------
#### [ AWS Organizations ]
+  **Getting started with AWS Organizations** 

   Learn how to start using AWS Organizations, including reviewing terminology and concepts, using consolidated billing, and applying organization policies. 

   [Explore the guide »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html) 
+  **Creating and configuring an organization** 

   Create your organization and configure it with two AWS member accounts. 

   [Get started with the tutorial »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) 
+  **Organizing Your AWS Environment Using Multiple Accounts** 

   Learn how using multiple AWS accounts can help isolate and manage your business applications and data, and optimize across the AWS Well-Architected Framework pillars. 

   [Read the whitepaper »](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  **Services that work with AWS Organizations** 

   Understand which AWS services services you can use with AWS Organizations and the benefits of using each service on an organization-wide level. 

   [Explore the guide »](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) 
+  **Best Practices for Organizational Units with AWS Organizations** 

   Dive deep into the recommended architecture of AWS best practices when building your organization, for OU structure and specific implementation examples. 

   [Read the blog »](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/?org_product_gs_OUBlog) 
+  **Achieving operational excellence with design considerations for AWS Organizations SCPs** 

   Learn how SCPs help control access to AWS services and resources provisioned across multiple accounts created within an organization. 

   [Read the blog »](https://aws.amazon.com/blogs/mt/achieving-operational-excellence-with-design-considerations-for-aws-organizations-scps/) 

------
#### [ AWS Security Hub CSPM ]
+  **Enabling AWS Security Hub CSPM** 

   Enable AWS Security Hub CSPM with AWS Organizations or in a standalone account. 

   [Explore the guide »](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) 
+  **Cross-Region aggregation** 

   Aggregate AWS Security Hub CSPM findings from multiple AWS Regions to a single aggregation Region. 

   [Explore the guide »](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) 
+  **AWS Security Hub CSPM workshop** 

   Learn how to use AWS Security Hub CSPM and to manage and improve the security posture of your AWS environments. 

   [Explore the workshop »](https://catalog.workshops.aws/security-hub/en-US) 
+  **Three recurring Security Hub CSPM usage patterns and how to deploy them** 

   Learn about the three most common AWS Security Hub CSPM usage patterns and how to improve your strategy for identifying and managing findings. 

   [Read the blog »](https://aws.amazon.com/blogs/security/three-recurring-security-hub-usage-patterns-and-how-to-deploy-them/) 

------

### Explore AWS cloud governance resources
<a name="explore"></a>

 **Architecture diagrams** 

 Explore reference architecture diagrams to help you develop your security, identity, and governance strategy. 

[ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all) 

 **Whitepapers** 

 Explore whitepapers for more insights and best practices on choosing, implementing, and using the security, identity, and governance services that best fit your organization. 

 [Explore whitepapers](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all) 

 **Solutions** 

 Use these solutions to further develop and refine your security, identity, and governance strategy. 

 [Explore solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23mgmt-govern&awsf.industries=*all&awsf.business-category=*all) 

## Choosing an AWS cost management strategy
<a name="cost-management-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which cost management services and tools are the best fit for your needs. | 
| **Last updated** | December 20, 2024 | 
| **Covered services** |  +  [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) <br />+  [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) <br />+  [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) <br />+  [AWS Budget Actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) <br />+  [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) <br />+  [AWS Consolidated Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) <br />+  [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) <br />+  [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) <br />+  [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) <br />+  [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) <br />+  [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/) <br />+  [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) <br />+  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) <br />+  [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) <br />+  [AWS Purchase Order Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-purchaseorders.html) <br />+  [Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) <br />+  [AWS Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) <br />+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) <br />+  [Amazon S3 Intelligent Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) <br />+  [Migration Evaluator](https://aws.amazon.com/migration-evaluator/features)   | 

### Introduction to AWS cost management
<a name="intro"></a>

Cost management and optimization in the cloud are important for businesses of all sizes. An effective cost management strategy ensures that you only pay for what you need and that you maximize the return on your cloud investment.

With cloud services, costs are dynamic and can escalate if not monitored closely. Financial planning, coupled with a clear understanding of the cost models for each service that you use, lets you allocate resources strategically, aligning spending with your business goals. This includes choosing the right pricing models, such as pay-as-you-go or Reserved Instances, and using auto-scaling to match resource provisioning with actual demand.

We offer services and tools to help you with cost management and optimization, including resources to: 
+ Organize and track your cost and usage data.
+ Improve control through consolidated billing and access permissions.
+ Enable better planning through budgeting and forecasts.
+ Lower your costs by using the right resources and pricing optimizations.



This decision guide will help you determine which cost management services and tools are the best fit for your needs. 

[![AWS Videos](https://img.youtube.com/vi/0aYZUqpwJKE?start=192&end=611/0.jpg)](https://www.youtube.com/watch?v=0aYZUqpwJKE?start=192&end=611)


### Understand AWS cost management
<a name="understand"></a>

AWS cost management strategy can be broken down into several key areas:

**Plan and evaluate:** When planning for future cloud spend, start by defining your key performance indicators (KPIs), such as the monthly cost of a specific project. Make sure that cloud resources related to a project are properly tagged with cost allocation tags, cost categories, or both. Then calculate and track the monthly cost of the project with the cost and usage data available in your AWS Cost Explorer and AWS Cost and Usage Report.

![Diagram showing the AWS Cloud Financial Management Portfolio.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cfm-portfolio.png)


Decide the project budget based on the trend shown by your KPIs, and the available funds set aside for the project. Set the budget thresholds using AWS Budgets for cost or resource usage.

**Manage and control:** As your organization evolves, you need the freedom to experiment and innovate in the cloud, while maintaining control over cost, governance, and security. One way to do that is to establish centralized ownership through a center of excellence or cloud business team. While cost management is a shared responsibility across an organization, a centralized team can design policies and governance mechanisms, implement and monitor the effort, and drive best practices.

This team can be supported by services such as [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) and [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

Use the [AWS Billing Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/billinginfo.html) to track your overall spend, view your cost breakdown by service and by account on your billing dashboard, and handle data exports with AWS CloudFormation.

![Diagram showing the AWS Billing Conductor and AWS Application Cost Profiler.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/billing-console-cost-profiler.png)


**Track and allocate:** Tracking spending and allocating that spending to the right team can be vital to effective cost optimization. It's useful to know when you're spending more than you planned, but even more useful when you can clearly identify where that spending is happening. We offer several tools to help you get started.

AWS Cost Explorer (when paired with Cost Allocation Tags) lets you categorize your resources and spending to fit your organization’s needs, while AWS Billing Conductor lets you customize your pricing and billing report to align with your business logic.

**Optimize and save:** Cost optimization is about making sure that you pay only for what you need. Two of the more useful strategies for optimizing spending are:
+ **Using the right pricing models.**
+ **Identifying and removing any idle or over-provisioned resources.** Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html) resource recommendations to see top-level KPIs for rightsizing and instance selection recommendations. 

Focus on these four areas to manage your AWS costs more effectively, maintain financial control, and optimize your cloud operations for maximum efficiency and value.

### Consider AWS cost management criteria
<a name="consider"></a>

The following section outlines some of the key criteria to consider when choosing a cost management strategy and supporting tools and services. 

------
#### [ Business goals and priorities ]

How you manage the costs of your cloud investment depends on what you’re trying to do, as well as how you’re tracking performance. If your organization is in a growth phase, then your KPIs may focus on market share, customer growth, and getting the best return on investment. If your focus is on reducing operating costs, then you will concentrate more on achieving the right balance between spending and delivering for your customers.

Set your budget based on the trend shown by your KPIs, as well as your available funds. Then set the budget thresholds using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) for cost or resource usage and to set utilization or coverage targets for your [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) (RIs) and [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html).

Monitor how the budget portfolio is progressing in your AWS Budgets Reports dashboard. Create notification alerts, which will be sent whenever cost and usage either reach your forecasts or exceed your threshold limits.

------
#### [ Budget policy and control ]

One key strategy for controlling cost is to have control over which services can be used by which members of your organization. If you need this kind of access control, use [IAM](https://aws.amazon.com/iam/getting-started/) to control individual and group access to your resources. This involves being able to create, manage, and grant permissions to IAM users to let them access the appropriate resources for their role and location. Use [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) to enable automatic policy-based account creation, management, and billing at scale.

------
#### [ Budget target tracking ]

It’s useful to get alerts that let you know if you’ve exceeded your budget, but it’s even more useful to see what is causing your bill to exceed your budget. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), to see which AWS services are increasing your spend.

To see which parts of your organization drive increased spend and usage, you can categorize your resources and spending using Cost Allocation Tags with AWS Cost Explorer.

------
#### [ Detailed reporting ]

If you want your cost management strategy to scale with your usage, it is important to get detailed reporting when you have multiple users working with multiple AWS services. 

You can use the billing dashboard on the [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) to:
+ Track your overall spend.
+ View your cost breakdown by service and account.
+ Get a unified view of spend in a single bill.
+ Establish rules for how to organize costs.
+ Share discount benefits associated with RIs and Savings Plans.

------
#### [ Business logic alignment ]

It’s not only about the numbers. Your cost optimization strategy must also align with the logic of your business. [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) lets you customize your AWS pricing and billing report to provide that alignment with your business logic. To help address your cost allocation needs, group accounts according to their financial relationships, adjust ratings, share credits and savings, or add overhead costs.

With AWS Billing Conductor, you can customize a second, alternative version of your monthly billing data. This alternative version models the billing relationship between you and your customers or business units, but doesn't change the way that AWS bills you. Using the alternative version provides you with a mechanism to configure, generate, and display rates to certain customers over a given billing period. Analyze the difference between the rates that you apply to your groupings, relative to the actual rates for those same accounts from AWS.

------
#### [ Pricing model ]

Customers with predictable, steady workloads on Amazon EC2, Amazon SageMaker AI, and Amazon RDS should consider [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) (RIs) to save up to 75% over equivalent on-demand capacity. RIs are available in three options: all upfront, partial upfront, and no upfront. To maximize your savings, when you buy RIs, the larger the upfront payment, the greater the discount. Partial upfront RIs offer lower discounts, but give you the option to spend less up front. Lastly, you can choose to spend nothing up front and receive a smaller discount, which lets you free up capital to spend on other projects.

We offer Reserved Instance and Savings Plans purchase recommendations through [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), based on your past usage. AWS Cost Explorer identifies and recommends the commitment value that it estimates will result in the largest savings.

------
#### [ Rightsizing services ]

Another key element of cost management is identifying and removing any idle or over-provisioned resources. [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) resource recommendations let you view top-level KPIs for rightsizing and instance selection recommendations.

These recommendations identify idle and underutilized instances, and search for smaller instance sizes in the same instance family.

------

### Choose an AWS cost management service
<a name="choose"></a>

Now that you know the criteria by which you will evaluate your cost management options, you are ready to choose which AWS cost management service is a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine the service that is the best fit for your organization and use case.



| Service category | What is it optimized for? | Cost management services | 
| --- |--- |--- |
|  **Plan and evaluate**  |  **Services optimized for improving planning, to create accurate forecasting of variable usage.**  |  | 
| --- |--- |--- |
|  | Helps you create a directional business case for AWS Cloud planning and migration. | [Migration Evaluator](https://aws.amazon.com/migration-evaluator/features/) | 
|  | Provides a free web-based planning tool for creating cost estimates for using AWS services. | [AWS Pricing Calculator](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/what-is-pricing-calculator.html) | 
|  | Provides improved planning and cost control with flexible budgeting and forecasting. | [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) | 
|  | Helps you centrally govern your AWS environment as you grow and scale on AWS. | [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) | 
|  **Manage and control**  |  **Services optimized to provide centralized billing, automatic cost governance, and a streamlined procure-to-purchase process.**  |   | 
| --- |--- |--- |
|  | Provides a dashboard to track overall spend and view cost breakdown by service and account. | [AWS Billing Console](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) | 
|  | Helps you to configure multiple purchase orders (POs), define how POs are mapped to their invoices, and access invoices generated against those POs. | [AWS Purchase Order Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-purchaseorders.html) | 
|  | Provides functionality to run an action when a budget exceeds a certain cost or usage threshold, either automatically or after manual approval. | [AWS Budget Actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) | 
|  | Helps you use machine learning models to detect and alert on anomalous spend patterns in your deployed AWS services. | [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) | 
|  | Consolidates billing and payment for multiple AWS accounts, allowing shared volume discounts across all accounts. | [AWS Consolidated Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) | 
|  | Enables you to create billing and cost management data exports using basic SQL, and visualize data by integrating with Amazon Quick. | [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) | 
|  **Track and allocate**  |  **Services optimized to track and analyze cost trends and drivers in aggregate.**  |  | 
| --- |--- |--- |
|  | Provides visualization of cost and utilization with default reports, and creates specific views with filters and grouping. | [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) | 
|  | Delivers cost and usage data to an S3 bucket where it can be integrated into other AWS tools or ERP for further analysis. | [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) | 
|  | Group accounts, tags, services, and charge types into meaningful categories with custom rules. | [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) | 
|  | Supports the showback and chargeback workflows of AWS Solution Providers and Enterprise customers. | [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html) | 
|  **Optimize and save**  |  **Services optimized for resource right-sizing, reserve capacity planning, and data transfer and storage optimization.**  |   | 
| --- |--- |--- |
|  | Provides a flexible pricing model that can help reduce your bill by up to 72% over on-demand prices. | [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) | 
|  | Offers a billing discount that provides savings on Amazon EC2 costs compared to on-demand instance pricing. | [Amazon EC2 Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) | 
|  | Recommends optimal AWS compute resources for your workloads, helping you reduce costs and improve performance. | [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) | 
|  | Provides Amazon EC2 instances that use spare Amazon EC2 capacity that is available for less than the on-demand price. | [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) | 
|  | Optimizes storage costs by automatically moving data to the most cost-effective access tier when access patterns change.  | [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) | 
|  | Provides you with a comprehensive view of your cost optimization recommendations across your AWS Regions and AWS accounts within your organization. | [AWS Cost Optimization Hub](https://aws.amazon.com/aws-cost-management/cost-optimization-hub/faqs/) | 

### Use an AWS cost management service
<a name="use"></a>

You should now have a clear understanding of what each AWS cost management service (and the supporting AWS tools and services) does—and which might be right for you.

We have provided a pathway to explore how each of the available AWS cost management services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ AWS Billing Conductor ]
+  **Getting started with AWS Billing Conductor** 

  Learn how to create billing groups, pricing configurations, and custom line items in AWS Billing Conductor.

   [Explore the guide ](https://docs.aws.amazon.com/billingconductor/latest/userguide/creating-abc.html) 
+  **Getting Started with AWS Billing Conductor** 

  Learn how to customize billing data and reporting in a way that aligns with your unique business logic.

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-billing-conductor/) 
+  **Best practices for AWS Billing Conductor** 

  Explore best practices when working with AWS Billing Conductor.

   [Explore the guide](https://docs.aws.amazon.com/billingconductor/latest/userguide/best-practices.html) 
+  **AWS Billing Conductor FAQs** 

  Learn about Billing Groups, configuring pricing, custom line items, and more.

   [Explore the guide](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/faqs/) 
+  **AWS Billing Conductor pricing** 

  Learn about pricing options, examples, and calculation resources.

   [Explore the guide](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/) 

------
#### [ AWS Budgets ]
+  **Best practices for AWS Budgets** 

  Explore best practices to use when working with AWS Budgets.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html) 
+  **Getting Started with AWS Budgets** 

  Use AWS Budgets to set a custom cost budget that tracks your costs at a monthly level, and to configure alerts that will notify you when you reach your user-defined spend thresholds.

   [Explore the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/getting-started-with-aws-budgets/) 
+  **Control your AWS costs** 

  Control your costs while exploring AWS service offerings using the AWS Free Tier, and how to use AWS Budgets to set up a cost budget to monitor usage.

   [Get started with the tutorial ](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets/) 
+  **AWS Budgets FAQs** 

  Learn how AWS Budgets works, and how to add alerts and subscribers.

   [Explore the guide ](https://aws.amazon.com/aws-cost-management/aws-budgets/faqs/) 
+  **AWS Budgets Pricing** 

  Learn about pricing options and request quotes.

   [Explore the guide ](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/) 

------
#### [ Compute Optimizer ]
+  **Getting started with AWS Compute Optimizer** 

  Learn how to access AWS Compute Optimizer for the first time, and how to opt in your accounts.

   [Explore the guide ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html) 
+  **Rightsizing recommendation preferences ** 

  Learn how the rightsizing recommendation feature allows you to customize the settings you want Compute Optimizer to consider when generating Amazon EC2 and Auto Scaling group instance recommendations.

   [Explore the guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html) 
+  **AWS Graviton-based instance recommendations** 

  Learn how to view the price and performance impact of running your workload on AWS Graviton-based instances.

   [Explore the guide ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/graviton-recommendations.html) 

------
#### [ Cost Explorer ]
+  **Getting started with Cost Explorer** 

  Explore how to get started with Cost Explorer from the AWS Cost Management Console.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html) 
+  **Exploring your data using Cost Explorer** 

  Discover how to see your estimated costs for the month to date, your forecasted costs for the month, a graph of daily costs, your top five cost trends, and a list of recently viewed reports.

   [Explore the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html) 
+  **Exploring more data for advanced cost analysis** 

  Learn how to enable multi-year data (at monthly granularity) and more granular data (at hourly and daily granularity) for the previous 14 days.

   [Explore the guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-advanced-cost-analysis.html) 
+  **Forecasting with Cost Explorer** 

  Learn how to create a forecast, a prediction of how much you will use AWS services over a selected forecast time period. 

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) 

------
#### [ AWS Data Exports ]
+  **Creating Data Exports** 

  Learn how to use Data Exports in the AWS Billing and Cost Management console.

   [Explore the guide ](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create.html) 
+  **Migrating from CUR to Data Exports CUR 2.0** 

  Learn how to create exports of AWS Cost and Usage Report 2.0 (CUR 2.0) for more consistent schema and nested data.

   [Explore the guide](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-migrate.html) 
+  **Data Exports for FOCUS 1.0 is now in general availability** 

  Standardize exports of your AWS cost and usage data with the FOCUS 1.0 (FinOps Open Cost and Usage Standard) schema.

   [Read the blog](https://aws.amazon.com/blogs/aws-cloud-financial-management/data-exports-for-focus-1-0-is-now-generally-available/) 

------
#### [ RI Reporting ]
+  **Getting started with Amazon EC2 Reserved Instances** 

  Dive deeper into the details of how RIs work.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) 
+  **Reserved Instance (RI) Reporting FAQs** 

  Get answers to frequently asked questions about Reserved Instance reporting and recommended best practices.

   [Explore the FAQs](https://aws.amazon.com/aws-cost-management/reserved-instance-reporting/faqs/) 
+  **Accessing Reserved Instance Recommendations** 

  If you enable Cost Explorer, you automatically get Amazon EC2, Amazon RDS, ElastiCache, OpenSearch Service, Amazon Redshift, and Amazon MemoryDB Reserved Instance (RI) purchase recommendations that could help you reduce your costs. Learn how to use those recommendations.

   [Explore the guide ](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html) 

------
#### [ Savings Plans ]
+  **Getting started with Savings Plans** 

  Learn how to get started with optimizing your AWS costs with Savings Plans.

   [Explore the guide ](https://docs.aws.amazon.com/savingsplans/latest/userguide/get-started.html) 
+  **Developing a compute Savings Plans** 

  Explore the overview of Savings Plans for Amazon EC2, AWS Fargate, and AWS Lambda.

   [Explore the guide](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/savings-plans.html) 
+  **Savings Plans FAQs** 

  Get answers to frequently asked questions about Savings Plans.

   [Explore the FAQs ](https://aws.amazon.com/savingsplans/faq/) 
+  **Announcing Savings Plans Purchase Analyzer** 

  Model Savings Plans purchases and evaluate the impact on cost, coverage, and utilization in the AWS Billing and Cost Management AWS Billing and Cost Management Console.

   [Read the blog ](https://aws.amazon.com/blogs/aws-cloud-financial-management/announcing-savings-plans-purchase-analyzer/) 

------
#### [ Amazon EC2 Spot Instances ]
+  **Getting started with EC2 Spot Instances ** 

  Learn how to get started with optimizing your AWS costs with Amazon EC2 Spot Instances.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) 
+  **Best practices for EC2 Spot Instances** 

  Learn the best practices for utilizing Amazon EC2 Spot Instances to save up to 90% over on-demand instances.

   [Explore the guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) 
+  **Spot Instance pricing history** 

  Learn how pricing history works and see links to the latest pricing options.

   [Explore the guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html) 

------
#### [ S3 Intelligent Tiering ]
+  **How S3 Intelligent-Tiering works** 

  Dive deeper into how Amazon S3 Intelligent-Tiering works.

   [Explore the guide ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html) 
+  **Using S3 Intelligent-Tiering** 

  Learn how to move data to Amazon S3 Inteligent-Tiering.

   [Explore the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html) 

------

### Explore AWS cost management resources
<a name="explore"></a>
+ **Patterns**

  Explore patterns to help you develop your AWS cost management strategy.

  [ Explore patterns](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23pattern&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all&cards-all.q=cost&cards-all.q_operator=AND)
+ **Whitepapers**

  Explore whitepapers to help you get started in developing your cost management strategy.

  [Explore whitepapers ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=*all&awsf.industries=*all&awsf.business-category=*all&cards-all.q=cost&cards-all.q_operator=AND)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common cost control and management use cases.

  [Explore solutions](https://aws.amazon.com/solutions/cloud-operations/cost-control-management/)

# Migration & IoT
<a name="migration-and-iot"></a>

The following decision guides help you choose AWS services for migrating workloads to the cloud and building IoT solutions that connect devices and process data at the edge.

**Topics**
+ [Choosing AWS migration services and tools](#migration-on-aws-how-to-choose)
+ [Choosing an AWS IoT service](#iot)

## Choosing AWS migration services and tools
<a name="migration-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS migration and transfer services are the best fit for your organization. | 
| **Last updated** | October 16, 2025 | 
| **Covered services** |  +  [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) <br />+  [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) <br />+  [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html) <br />+  [Direct Connect](https://aws.amazon.com/directconnect/getting-started/) <br />+  [DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) <br />+  [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-getting-started.html) <br />+  [AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html) <br />+  [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/setting-up.html) <br />+  [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html)   | 

### Introduction
<a name="intro"></a>

Migration and modernization in the Amazon Web Services (AWS) Cloud involves the process of relocating an organization's digital infrastructure, applications, and data to AWS. This shift allows you to not only modernize applications, but also use the range of scalable and secure cloud services and infrastructure offered by AWS to reduce reliance on physical hardware and optimize resource allocation.

The migration process typically begins with a comprehensive assessment of your existing IT assets and requirements, followed by strategic planning and architecture design to ensure an optimal transition. This may involve re-hosting, re-platforming, or re-architecting applications to best use AWS services.

Once you have a migration plan in place, data is transferred to AWS, and applications are deployed in the cloud environment. Post-migration, ongoing management, monitoring, and optimization are crucial to maximize benefits.

AWS offers a wide range of tools, resources, and support to help with this process, catering to diverse migration strategies, such as lift-and-shift, re-platforming, and refactoring. This guide is designed to help you choose the right tools and services to do your migration.

[![AWS Videos](https://img.youtube.com/vi/9FjxnEoH5wg?start=134&end=436/0.jpg)](https://www.youtube.com/watch?v=9FjxnEoH5wg?start=134&end=436)


### Understand
<a name="understand"></a>

Moving applications and data from on-premises infrastructure to AWS involves a strategic progression through key phases.

It starts with a phase of assessment and mobilization, where you [build a business case for migrating to the cloud](https://d1.awsstatic.com/AWS_Navigating_the_Cloud_Migration_and_Modernization_Executive_Guidance.pdf). 

![Diagram showing AWS data migration services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/migration-approach.png)


An assessment takes a snapshot of your current on-premises footprint to fine-tune licensing, view server and application dependencies, and deliver recommendations for migration and modernization scenarios.

In the mobilize phase, you’ll build a strategy for optimizing infrastructure selection, creating landing zones and establishing cloud best practices within your team to begin a migration.

Here's more detail on each of those phases.

**Assess and mobilize**

The first phase of migrating on-premises workloads to AWS involves assessing your existing infrastructure and understanding the specific requirements. You can use tools such as [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) to create an inventory of applications and dependencies, or request a free [migration assessment](https://pages.awscloud.com/GLOBAL-entstrategy-PT-AWS-Migration-Evaluator-Request-2023-interest.html) to build your business case. This initial step is crucial for formulating a comprehensive migration strategy. The [AWS Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program/) can also help in the development of such a strategy.

**Migrating applications and databases**

In this phase, applications and databases are moved to AWS, and the migration strategy is executed. AWS provides services like MGN for large-scale application migration and [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) for seamless migration of databases. AWS Transform uses generative AI and agentic AI capabilities to automate, accelerate, and optimize the migration process. Transform orchestrates migration for VMware workloads, mainframes, and .NET applications. Organizations might choose to re-host (lift-and-shift) or re-architect applications for optimal performance in the cloud. The [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) aids in building serverless applications.

**Hybrid cloud storage**

To provide a smoother transition, you might choose to adopt a hybrid cloud storage approach during migration. [AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html) can be used to provide integration of on-premises environments with cloud storage, enabling a unified data management strategy. This hybrid model is designed to offer data accessibility and availability, and help minimize disruptions during the migration process.

**Online data transfer**

For continuous operations, online data transfer mechanisms play a pivotal role. [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html), for instance, enables efficient and secure transfer of large datasets between on-premises environments and AWS storage services. This ensures minimal downtime and maintains data integrity throughout the migration.

By navigating through these phases, you can realize the benefits of AWS, and make best use of the scalability, security, and services it provides, while minimizing disruptions to ongoing business operations.

### Consider
<a name="consider"></a>

In the domain of migration and transfer to AWS, organizations face a spectrum of challenges and concerns that AWS services are strategically designed to address. In the following, we will explore some of the criteria to consider for a timely, secure, and cost-effective migration to AWS.

------
#### [ Diverse migration scenarios ]

Migrating on-premises workloads to AWS demands a nuanced approach, primarily due to the diverse migration scenarios organizations encounter. These scenarios range from simple lift-and-shift migrations, where existing applications are moved with minimal changes, to more complex re-platforming or re-architecting, which involve optimizing applications for AWS services. Hybrid cloud deployments are another common scenario, allowing organizations to maintain on-premises infrastructure while leveraging AWS capabilities.

Organizations must assess their speciﬁc needs, balancing factors like downtime tolerance, cost-eﬃciency, and data integrity. Data sensitivity, compliance requirements, and industry regulations also inﬂuence migration strategies.

AWS offers a suite of tools and services to address this diversity, providing organizations with the flexibility to choose the most suitable migration approach for their unique circumstances. Navigating these diverse scenarios effectively ensures a successful transition to AWS, unlocking the full potential of cloud computing while aligning with organizational goals and constraints.

------
#### [ Minimizing downtime ]

Minimizing downtime is a critical consideration in migrating on-premises workloads to AWS, because any interruption in business operations can result in significant financial and operational setbacks. To achieve minimal downtime, organizations employ several strategies.

First, they often opt for gradual migration approaches, such as the lift-and-shift method, where existing workloads are moved to AWS with minimal modification. This minimizes downtime but might not fully leverage all of the capabilities AWS offers.

Second, implementing hybrid cloud solutions can maintain business continuity during migration. By keeping critical components on-premises while migrating non-essential workloads to AWS, companies can mitigate downtime risks.

Moreover, AWS offers tools like AWS DataSync and AWS Snowball to facilitate efficient data transfer, reducing the time data spends in transit during migration, thereby minimizing downtime.

Finally, thorough testing and validation of the migration plan are essential to identify potential issues before they impact production systems, ensuring a smoother transition with minimal disruption. Overall, minimizing downtime is a top priority in the migration process to AWS, enabling businesses to maintain operational efficiency throughout the migration journey.

------
#### [ Large data transfer challenges ]

Large data transfer poses a significant challenge in migrating on-premises workloads to AWS. When dealing with massive datasets, bandwidth limitations and time constraints become major concerns. AWS provides solutions to address these challenges.

For online data transfer, services like AWS DataSync employ optimized protocols to maximize data transfer speeds, reducing the time required to move data to the cloud. However, this method might be insufficient for extremely large datasets or environments with limited bandwidth.

Direct Connect provides a dedicated private network connection from your premises to AWS, offering consistent and high-bandwidth connectivity for large data transfers, especially when ongoing, high-volume data movement is required. For migrating databases, including large databases, AWS DMS can help.

Strategically combining these data transfer options helps organizations efficiently migrate large volumes of data to AWS while minimizing disruption to business operations and ensuring data integrity.

------
#### [ Database compatibility and heterogeneity ]

Database compatibility and heterogeneity present significant challenges during the migration of on-premises workloads to AWS. Organizations often rely on various database management systems, and ensuring seamless compatibility with AWS services is crucial.

To address these complexities, AWS offers tools like AWS Database Migration Service (AWS DMS) and DMS Schema Conversion (DMS SC). AWS DMS supports the migration of a wide range of databases to AWS, facilitating data replication with minimal downtime. DMS SC helps convert database schemas, ensuring that they are compatible with AWS database services, which can vary in structure and behavior.

Additionally, AWS provides managed database services like Amazon RDS and Amazon Aurora, which are compatible with popular database engines, simplifying the migration process.

Organizations must carefully assess their database landscape, plan for potential incompatibilities, and choose the right AWS database service or conversion approach to maintain data integrity and functionality during migration.

------
#### [ File transfer workloads ]

Migrating file transfer workloads from on-premises environments to AWS requires thoughtful planning to ensure seamless data movement and continuity of operations. File transfer workloads often involve large volumes of critical data, which necessitates a well-executed strategy.

AWS offers services like AWS Transfer Family, which includes AWS Transfer for SFTP and AWS Transfer for FTPS, allowing organizations to easily migrate and manage file transfer workloads securely in the cloud. These services provide compatibility with existing file transfer protocols, reducing migration complexities.

Organizations can also leverage AWS DataSync for efficient, high-speed data transfers. It helps synchronize on-premises file systems with AWS storage services, minimizing downtime and ensuring data consistency.

Furthermore, optimizing network connectivity and bandwidth is crucial for maintaining file transfer performance during migration. Direct Connect and [AWS VPN solutions](https://aws.amazon.com/vpn/) can help establish reliable connections between on-premises environments and AWS, addressing potential challenges related to latency and bandwidth limitations.

In summary, a well-structured plan, the right AWS services, and a focus on network optimization are key considerations to ensure a smooth migration of file transfer workloads to AWS, preserving data integrity and minimizing disruption.

------
#### [ Visibility and monitoring ]

Visibility and monitoring are crucial during migration to ensure a smooth transition of on- premises workloads to AWS. 

AWS Transform plays a pivotal role in this regard by offering a centralized platform for tracking and managing the migration and modernization journey. This tool provides organizations with real-time insights into the progress of their migration projects, allowing them to identify any bottlenecks or issues promptly. It offers visibility into the health and performance of migrated resources, ensuring that applications run smoothly in the cloud environment. 

Furthermore, AWS Transform enhances security by providing visibility into access control and auditing through AWS Identity and Access Management (IAM) and AWS CloudTrail. This ensures that security measures are maintained throughout the migration process. 

In essence, AWS Transform empowers organizations to make informed decisions, optimize their migration strategy, and maintain the integrity of their workloads. Its role in enhancing visibility and monitoring is instrumental in achieving a successful and secure migration to AWS.

------
#### [ Application capability ]

It can be challenging to ensure that applications, especially legacy applications, are compatible with the cloud environment. Ensuring that existing applications seamlessly function within the AWS Cloud environment is essential for a smooth transition. This often involves assessing and, if necessary, modifying applications to align with AWS services and infrastructure. AWS Transform aids in this process.

Compatibility challenges can arise due to differences in operating systems, dependencies, or network configurations. Therefore, meticulous testing and validation are vital to identify and resolve any compatibility issues prior to migration. By addressing application compatibility proactively, organizations can minimize disruptions, maintain business continuity, and fully harness the benefits of the scalable and secure cloud infrastructure in AWS.

------
#### [ Dependency mapping ]

Dependency mapping, a crucial aspect of migrating on-premises workloads to AWS, involves identifying the intricate relationships and interdependencies between applications. These connections can be complex, encompassing data flows, service dependencies, and communication patterns.

AWS offers AWS Transform to assist in this process. This service automatically discovers, maps, and documents dependencies, providing organizations with a clear understanding of how different components interact.

By accurately mapping dependencies, organizations can make informed decisions about migration strategies, ensuring that all associated elements are moved together to maintain functionality. This reduces the risk of post-migration issues and helps organizations plan for the sequencing of migration activities, minimizing disruptions and downtime.

------
#### [ Performance optimization ]

Performance optimization is a vital consideration when migrating on-premises workloads to AWS. It involves assessing and enhancing the efficiency and speed of applications in the cloud environment. This process often starts with a thorough analysis of the existing application's performance characteristics, including resource utilization, latency, and scalability.

AWS provides various tools and services to aid in performance optimization, such as Amazon CloudWatch for monitoring, AWS Auto Scaling for dynamic resource allocation, and Elastic Load Balancing for distributing traffic. Additionally, AWS Trusted Advisor and AWS Compute Optimizer offer recommendations for cost optimization and performance improvement.

------
#### [ Security and compliance ]

Security and compliance are paramount when migrating on-premises workloads to AWS. Organizations must maintain data integrity, confidentiality, and compliance with industry regulations during and after migration. AWS offers a robust set of security services, including AWS Identity and Access Management (IAM), AWS Key Management Service (AWS KMS), and AWS Security Hub CSPM, to help organizations establish strong security postures.

Compliance with standards such as GDPR, HIPAA, and PCI DSS is simplified through AWS compliance programs and extensive documentation. AWS Artifact provides access to compliance reports, while AWS Config helps monitor and maintain compliance.

Furthermore, AWS provides tools like IAM and AWS Key Management Service (AWS KMS) for fine-grained control over access and encryption of data. To safeguard workloads during migration and beyond, it's essential to implement security best practices and conduct regular audits, ensuring a secure and compliant environment in AWS.

------
#### [ Testing and validation ]

Thorough testing is essential to validate that migrated applications function as expected in the new cloud environment. This includes performance testing, functionality testing, and security testing to identify and address any issues or discrepancies.

AWS offers a range of tools and services, such as AWS CodeBuild and AWS CodeDeploy, for automated testing and deployment of applications in the cloud.

Comprehensive testing and validation not only mitigate potential risks but also provide the confidence that the migrated workloads will perform as expected, minimizing disruptions and ensuring a successful transition to AWS. Regular testing and ongoing validation post-migration are also essential to adapt to changing business needs and maintain optimal performance and security.

------
#### [ Cost management ]

Managing costs effectively during and after migration is crucial for budget considerations. Organizations must carefully plan and optimize their cloud spending to maximize cost efficiency. AWS offers tools like AWS Cost Explorer and AWS Budgets to monitor and forecast expenses.

Cost management involves selecting the right AWS pricing models, such as On-Demand, Reserved Instances, or Savings Plans, based on workload usage patterns. Right-sizing resources and leveraging auto-scaling capabilities can help align costs with actual demand, avoiding overprovisioning.

Additionally, AWS Trusted Advisor and AWS Compute Optimizer provide recommendations for cost optimization, and AWS Cost Anomaly Detection can identify unusual spending patterns.

By proactively managing costs, organizations can harness the benefits of the scalability and flexibility in AWS while ensuring that their migration remains within budgetary constraints. Cost management is an ongoing process, and regular monitoring and adjustment are essential to control and optimize cloud expenditure over time.

------

### Choose
<a name="choose"></a>

Now that you have reviewed the key criteria to consider in your migration to AWS you are ready to start planning your migration and choosing the appropriate AWS services to assist in your migration. Here are some things to consider: 
+ You must assess your existing infrastructure and create an inventory of assets to mobilize resources effectively.
+ Will you be choosing a lift-and-shift strategy, re-platforming (that is, on-premises database to Amazon RDS), or modernizing your workloads by re-architecting?
+ Will you operate in a hybrid mode, with some workloads remaining on-premises?
+ What are your data transfer needs?

The following table walks you through the relevant services on AWS that will help you to achieve a successful migration.



| Migration category | What is it optimized for? | Migration services | 
| --- |--- |--- |
| Assess and mobilize | These services are optimized to accelerate decision-making and discover on-premises assets to plan your AWS migration. | [Experience-Based Acceleration (EBA)](https://aws.amazon.com/experience-based-acceleration/)<br />[AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/)<br />[Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/)<br />[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) | 
|  Migrate your applications  |  These services are optimized to simplify and expedite the migration on on-premises servers and databases to AWS.  |  [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) [DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)  | 
| --- |--- |--- |
| Hybrid cloud storage | These services are optimized for on-premises applications that require low-latency data access or rapid data transfer to the cloud. | [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/)<br />[Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) | 
|  Online data transfer  |  These services are optimized to make it simple and easy to transfer your data into and out of AWS via online methods.  |  [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html) [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)  | 
| --- |--- |--- |

### Use
<a name="use"></a>

To explore how to use and learn more about each of the available AWS migration and transfer services, we have provided a pathway to explore how each of the services work. The following sections provide links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ AWS Transform ]
+  **What is AWS Transform?** 

  This guide provides an overview of AWS Transform.

   [Explore the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html) 
+  **Getting started with AWS Transform for VMware migration** 

  This guide will help you get started with migrating your VMware environment to Amazon EC2 with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html) 
+  **Modernize your mainframe applications with AWS Transform** 

  This guide will help you modernize your mainframe applications with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html) 
+  **Modernize your .NET applications with AWS Transform** 

  This guide will help you modernize your .NET applications with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html) 

------
#### [ AWS Transform MGN ]
+  **Introduction to AWS Transform MGN** 

  This short video (1:35) gives a brief introduction to AWS Transform MGN

   [Watch the video](https://www.youtube.com/watch?v=KVV5Hd70Uc8) 
+  **Getting started with AWS Transform MGN** 

  This guide will help you get started with MGN including how to use it with AWS Migration Hub.

   [Explore the guide](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) 
+  **How to use AWS Transform MGN for lift-and-shift migrations** 

  This blog posts shows you how to simplify your lift-and-shift migration using AWS Transform MGN.

   [Read the blog post](https://aws.amazon.com/blogs/aws/how-to-use-the-new-aws-application-migration-service-for-lift-and-shift-migrations/) 
+  **Automate setup of AWS Transform MGN and Elastic Disaster Recovery** 

  This blog post discusses how to combine AWS Transform MGN and AWS Elastic Disaster Recovery Service to increase the resilience of your migrated workloads.

   [Read the blog post](https://aws.amazon.com/blogs/mt/automate-setup-of-aws-application-migration-service-and-elastic-disaster-recovery/) 
+  **AWS Transform MGN best practices** 

  This blog post shares best practices for accelerating and successfully implementing your migration using a highly automated list-and-shift solution, AWS Transform MGN.

   [Read the blog post](https://aws.amazon.com/blogs/mt/aws-application-migration-service-best-practices/) 

------
#### [ AWS Database Migration Service ]
+  **Getting started with AWS Database Migration Service** 

  In this guide, you will learn how to perform a database migration with AWS DMS. 

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) 
+  **Getting started with DMS Schema Conversion** 

  In this tutorial, you will learn how to set up DMS Schema Conversion, create a migration project, and connect to your data providers.

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html) 
+  **Database migration step-by-step walkthroughs** 

  In this guide, you can find step-by-step walkthroughs that go through the process of schema conversion and data migration for eight different source databases supported by AWS Database Migration Service.

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/sbs/dms-sbs-welcome.html) 
+  **How to migrate from Oracle to Amazon Aurora** 

  In this hands-on lesson, you will migrate a legacy Oracle database to a cloud-native database with Amazon Aurora.

   [Start the lesson](https://aws.amazon.com/tutorials/break-free-from-legacy-databases/migrate-oracle-to-amazon-aurora/) 

------
#### [ AWS DataSync ]
+  **Getting started with AWS DataSync** 

  This guide focuses on getting started with DataSync using the AWS Management Console.

   [Explore the guide](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html) 
+  **Tutorial: Transferring data from on-premises storage to Amazon S3 in a different AWS account** 

  In this tutorial, you will learn how to transfer data to from on-premises storage to an S3 bucket in a different account from the DataSync agent.

   [Start the tutorial](https://docs.aws.amazon.com/datasync/latest/userguide/s3-cross-account-transfer.html) 
+  **Tutorial: Transferring data from Amazon S3 to Amazon S3 in a different AWS account** 

  In this tutorial, you will learn how to use DataSync to transfer data from an S3 bucket in one account to another S3 bucket in a different account.

   [Start the tutorial](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_s3-s3-cross-account-transfer.html) 

------
#### [ Direct Connect ]
+  **Using the Direct Connect Resiliency Toolkit to get started** 

  This guide discusses how to use the Direct Connect Resiliency Toolkit to help you determine and then place your order for the number of dedicated connections to achieve your SLA objective.

   [Read the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) 
+  **Continuous on-premises data migration with Direct Connect** 

  This guide discusses using Direct Connect as part of an on-going data migration in a hybrid cloud deployment.

   [Read the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-data-migration-services/use-case-2-continuous-on-premises-data-migration.html) 
+  **Working with Direct Connect Gateways** 

  This guide shows how to use Direct Connect gateways to connect your VPCs using either a transit gateway or a virtual private gateway.

   [Read the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) 

------

------
#### [ Amazon S3 Transfer Acceleration ]
+  **Getting started with Amazon S3 Transfer Acceleration** 

  This guide will demonstrate how to get started with Amazon S3 Transfer Acceleration.

   [Explore the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-getting-started.html) 
+  **Amazon S3 Transfer Acceleration speed comparison tool** 

  This guide will demonstrate how to enable Transfer Acceleration on an S3 bucket and transfer data to and from the acceleration-enabled bucket.

   [Explore the guide](https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html) 
+  **Uploading large objects to Amazon S3 using multipart upload and transfer acceleration** 

  This tool allows you to compare the speed of multi-part file uploads for various Amazon S3 regions with and without the use of Amazon S3 Transfer Acceleration.

   [Go to the tool](https://aws.amazon.com/blogs/compute/uploading-large-objects-to-amazon-s3-using-multipart-upload-and-transfer-acceleration/) 

------
#### [ DMS Schema Conversion ]
+  **Getting started with DMS Schema Conversion** 

  This guide provides instructions for setting up DMS Schema Conversion.

   [Get started with the tutorial](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html) 

------
#### [ AWS Storage Gateway ]
+  **Getting started with AWS Storage Gateway (Amazon S3 File Gateway)** 

  This guide provides instructions for setting up S3 File Gateway and accessing it with Storage Gateway.

   [Get started with the tutorial](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html) 
+  **Getting started with AWS Storage Gateway (Amazon FSx File Gateway) ** 

  This guide provides instructions for setting up FSx File Gateway and accessing it with Storage Gateway.

   [Get started with the tutorial](https://docs.aws.amazon.com/filegateway/latest/filefsxw/setting-up.html) 
+  **Data migration and cost saving at scale with Amazon S3 File Gateway** 

  This blog walks through how Amazon S3 File Gateway helps migrate your data to the cloud while keeping metadata attributes intact, optimizing storage cost, and providing access to data in the cloud from on-premises application using standard SMB (Server Message Block) and NFS (Network File System) file protocols.

   [Read the blog post](https://aws.amazon.com/blogs/storage/data-migrations-at-scale-with-amazon-s3-file-gateway/) 

------
#### [ AWS Transfer Family ]
+  **What is AWS Transfer Family? ** 

  This guide provides an overview of the Transfer Family service.

   [Read the guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) 
+  **Tutorial: Getting started with AWS Transfer Family server endpoints** 

  Use this tutorial to get started with Transfer Family. You'll learn how to create an SFTP-enabled server with a publicly accessible endpoint using Amazon S3 storage, add a user with service-managed authentication, and transfer a file with Cyberduck.

   [Get started with the tutorial](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html) 
+  **Tutorial: Setting up a managed workflow for decrypting a file** 

  This tutorial illustrates how to set up a managed workflow that contains a decrypt step. The tutorial also shows how to upload an encrypted file to an Amazon S3 bucket and then view the decrypted file in that same bucket.

   [Get started with the tutorial](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-decrypt-tutorial.html) 

------

### Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you develop your migration and transfer solutions on AWS.

  [Explore architecture diagrams](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&ams%23interactive-card-vertical%23pattern-data-398312969.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523local-tags-content-type.and%2522%252C%2522value%2522%253A%255B%2522reference-arch-diagram%2522%255D%257D%255D%257D)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your migration and transfer options.

  [Explore whitepapers ](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&ams%23interactive-card-vertical%23pattern-data-398312969.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523local-tags-content-type.and%2522%252C%2522value%2522%253A%255B%2522whitepaper%2522%255D%257D%255D%257D)
+ **Videos, patterns, AWS Solutions, and guidance**

  Explore additional architectural guidance for common use cases for migration and transfer services.

  [Explore additional assets](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)

## Choosing an AWS IoT service
<a name="iot"></a>

**Understand the differences and pick the one that's right for you** 


<table>
<tbody>
  <tr><td><b>Purpose</b></td><td colspan="2">Help determine which AWS IoT services are the best fit for your organization.</td></tr>
  <tr><td><b>Last updated</b></td><td colspan="2">June 28, 2024</td></tr>
  <tr><td><b>Covered services</b></td><td><b>Foundational services</b></td><td><b>Use case or industry-specific services</b></td></tr>
  <tr><td></td><td><i>Device and design</i><ul><li> <a href="https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html">FreeRTOS</a> </li><li> <a href="https://docs.aws.amazon.com/iot-expresslink/">AWS IoT ExpressLink</a> </li><li> <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html">AWS IoT Greengrass</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html">AWS IoT Device SDKs</a> </li></ul><br /><i>Connect, manage and monitor</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html">AWS IoT Core</a> </li><li> <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html">Amazon Kinesis Video Streams</a> </li><li> <a href="https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html">AWS IoT Device Defender</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html">AWS IoT Device Management</a> </li></ul><br /><i>Analyze and act</i><ul><li> <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html">AWS IoT Events</a> </li></ul><br /><i>Design and validate</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html">AWS IoT Core Device Advisor</a> </li><li> <a href="https://docs.aws.amazon.com/greengrass/v2/developerguide/device-tester-for-greengrass-ug.html">AWS IoT Device Tester</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html">AWS IoT Device Client</a> </li></ul></td><td><i>Smart manufacturing</i><ul><li> <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html">AWS IoT SiteWise</a> </li><li> <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html">AWS IoT SiteWise Edge</a> </li><li> <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html">AWS IoT TwinMaker</a> </li></ul><br /><i>Connected vehicles</i><ul><li> <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/getting-started-console-tutorial.html">AWS IoT FleetWise</a> </li></ul><br /><i>Public infrastructure</i><ul><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html">AWS IoT Core for Amazon Sidewalk</a> </li><li> <a href="https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html">AWS IoT Core for LoRaWAN</a> </li></ul></td></tr>
</tbody>
</table>


### Introduction
<a name="introduction"></a>

Internet of Things (IoT) technologies have become a transformative force in the business world. They offer a wide range of opportunities for innovation, efficiency, and customer-centric strategies. IoT provides the foundation for smart devices, smart homes, smart buildings, next-generation vehicles, smart manufacturing, and public infrastructure. Businesses can use IoT technologies to increase efficiency with automation, gain visibility into their supply chains, get insights from their data, and offer smart connected experiences for their customers. 

AWS offers a variety of purpose-built IoT services. The foundational services help you to design and simplify complex IoT tasks. These services provide device-to-cloud connectivity, secure data ingestion, data processing, analytics, and the ability to run machine learning (ML) inferences on the edge. In addition, AWS offers IoT services that are designed for particular industries or use cases, including smart manufacturing, connected vehicles, and public infrastructure. 

This decision guide will help you ask the right questions, evaluate your criteria, and determine which IoT services are the best fit for your needs. 

[![AWS Videos](https://img.youtube.com/vi/o4Rr_lDFWfA?si=D-ZdUEJx0FOE6az0/0.jpg)](https://www.youtube.com/watch?v=o4Rr_lDFWfA?si=D-ZdUEJx0FOE6az0)


### Understand
<a name="understand"></a>

IoT is sometimes described as a bridge between the physical and digital worlds. 

It is a network of connected devices and sensors that communicate with each other and the cloud. These devices and sensors (sometimes called things) collect data from a very broad range of sources. 

![Diagram showing an introduction to Internet of Things (IoT).](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/what-is-iot.jpg)


The devices collect data from sources that are connected to home appliances, buildings, machines, vehicles, hardware, factory production lines, pipelines, and connected people (for example, people wearing smart, connected devices for monitoring their health and fitness).

IoT services are designed to help you:
+ Securely connect your IoT devices to the cloud. 
+ Process the data locally on the devices. 
+ Securely capture and ingest data in the cloud for additional processing or for added intelligence. 
+ Manage structured and unstructured data, such as video streams. 
+ Analyze that data and enrich it further using analytics and machine learning services to generate actionable insights. 
+ Develop plans that you can act on (such as exercise recommendations for individuals, or predictive machine maintenance strategies for industrial assets or fleets of vehicles). 
+ Perform remote over-the-air updates to keep your devices and systems up to date. 
+ Scale your operations from an initial set of devices up to billions globally, while achieving higher reliability, quality of service, and availability. 
+ Monitor your organization’s security posture across your entire device fleet. 

![Diagram showing the AWS IoT stack.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/IoT-stack.png)


When asking how AWS IoT services can be useful to your organization, it's important to think about how these services are organized. 

If you think about these services as a stack, as shown in the previous image, the foundational AWS Cloud services you need are at the base. These include services that provide compute, storage, database, containers, system management, networking management, and security. These services can also provide the analytics, ML, and artificial intelligence (AI) capabilities required to make the most of the insights you get from your IoT data. 

Moving up the stack, you see a range of purpose-built IoT services (including industry-specific services) and IoT solutions from both AWS and AWS Partners. 

#### Generative AI and IoT
<a name="understand-genAI"></a>

While IoT-specific generative AI is still evolving, we see two broad categories of use cases: 
+ Use cases that help IoT solution developers build more capable solutions faster and with higher quality. 
+ Use cases that help end users naturally interact with IoT devices to generate recommendations and insights from their data. 

There are a wide range of possibilities when you connect a vast amount of IoT data with generative AI technology. Your initial focus, however, is likely to be on tangible use cases where you can find value today. 

![Diagram showing a comprehensive set of AWS IoT services.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/iot-services.png)


For example, developers can provide a description of the application function with details about an IoT circuit board and sensors. Then, a generative AI-powered function can produce prototype code with associated infrastructure as code (IaC) and installation steps. It can also provide generic prototype code for one type of board and automatically convert it to working code for another. 

Consider also [this sample app](https://aws.amazon.com//blogs/iot/building-an-ai-assistant-for-smart-manufacturing-with-aws-iot-twinmaker-and-amazon-bedrock/) for using AWS IoT TwinMaker with Amazon Bedrock in manufacturing as an example of what you can accomplish when combining AI and IoT. 

Further, generative AI models can create infrastructure code (such as CloudFormation templates) that define asset models in AWS IoT SiteWise, device metadata in AWS IoT Device Management, and other associated AWS infrastructure. 

This can reduce proof of concept (PoC) development time and lower the barrier of entry to create customized AWS solutions. You can then use generative AI models to audit environments and provide recommendations to save on costs and improve your organization's security posture. 

Finally, you can synthetically create realistic and unidentifiable user data to comprehensively test IoT applications with a small sample of data and description of user behavior. This can help you to test unforeseen edge cases. This testing results in better products, accelerated release cycles, and fewer production issues. 

### Consider
<a name="consider"></a>

Here are some of the key criteria to consider when you’re choosing which IoT services are the best fit for your organization. 

------
#### [ Business outcome ]

 ![Business applications icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch-Category_Business-Applications_48.png) 

**Business outcome**

 Start by articulating the problem that you want to solve, along with the desired business outcome that will result from solving that problem. AWS offers a number of purpose-built services that are specific in what they can provide to help you get to the business outcome you want.

For example, you might run a logistics company and use robots in your warehouses to automate the movement of packages within the facility. To reduce downtime, it’s important to be able to quickly get reports of a malfunction and react right away. It’s even better to reliably get data that signals a potential upcoming malfunction. An AWS monitoring service such as [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html) is designed specifically with that kind of scenario in mind. Similarly, [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) is designed to help you analyze and get value from the vast amount of data coming in from your connected sites (where you might be receiving data from industrial sites and equipment). 



------
#### [ Scale, reliability, and quality of service ]

 ![Auto scaling icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_Amazon-EC2_Auto-Scaling_48.png) 

**Scale, reliability, and quality of service**

To properly consider the issues of scale, reliability, and quality of service in AWS IoT, it's important to know that the AWS global infrastructure is built around AWS Regions and Availability Zones. 

AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

To ensure availability in the event of a disruption, AWS IoT operates across multiple Availability Zones. In terms of the scale, reliability, and quality of service attributes of specific AWS services, here are some useful things to know: 
+ [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) provides fully managed [MQTT (Message Queuing Telemetry Transport)](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) -based messaging features. You can use these features to help you build adaptive IoT architectures. It also provides native support for a managed MQTT broker that supports persistent, always-on connections and advanced message retention policies. The broker also handles millions of devices and topics simultaneously. AWS IoT and the AWS IoT Device SDKs support the MQTT Quality of Service (QoS) levels 0 and 1. 
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started.html) provides support for data resiliency and backup with features that allow devices to communicate over the local network, even after losing internet connectivity. This allows the core to receive messages that are sent while the core is offline. Stream manager processes data locally until the connection is restored, and sends data to the cloud or local storage. 
+ With [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), you can update devices in the field while using Amazon Amazon S3 versioning for all firmware and software, and update manifests for devices. 
+ With [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), you can document your IoT infrastructure as code and provision cloud resources using a CloudFormation template. 

------
#### [ Lifecycle management ]

 ![Lifecycle management icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_AWS-Systems-Manager_Change-Manager_48.png) 

**Lifecycle management**

From initial deployment to eventual retirement, your IoT devices have a finite lifespan. You need to manage them effectively, reliably, and securely during that lifespan to achieve your business goals. How you address IoT product lifecycle management (PLM) is important in considering the AWS IoT services that you’ll need. Services such as [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html), [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), and [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) all provide important pieces of lifecycle management ([as described in this blog post](https://aws.amazon.com/blogs/iot/navigating-iot-product-lifecycle-management-with-aws-iot/)). 

------
#### [ Edge support ]

 ![Edge support icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Res_Amazon-CloudFront_Edge-Location_48.png) 

**Edge support**

In many IoT scenarios, you're working with devices that might rely on an [edge computing model](https://aws.amazon.com//what-is/edge-computing/) — and you need services that support running workloads at the edge. 

A great example of this is [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html). It’s an open source IoT edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices. 

You can use it to build software that enables your devices to act locally on the data that they generate, run predictions based on ML models, and filter and aggregate device data. It enables your devices to collect and analyze data closer to where that data is generated, react autonomously to local events, and communicate securely with other devices on the local network.

Similarly, [AWS IoT ExpressLink](https://docs.aws.amazon.com/iot-expresslink/) powers a range of connectivity modules that are developed and offered by AWS Partners. These modules include software that implements AWS mandated security requirements. This makes it faster and easier for you to securely connect devices to the cloud, and to seamlessly integrate with a range of AWS services. 

[AWS IoT SiteWise Edge](https://aws.amazon.com/iot-sitewise/sitewise-edge/) brings features of AWS IoT SiteWise in the cloud to the factory premises. Specifically, you can use asset models that are defined in the cloud service to process data in the SiteWise Edge gateway locally. You can also visualize equipment data by using local SiteWise Monitor dashboards that are served from the SiteWise Edge gateway. 

[AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) are also a great resource for edge support. They include open source libraries, developer guides with samples, and porting guides. 

Finally, the [AWS IoT Lens for the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/edge-layer.html) offers further guidance about the edge layer in IoT systems and what you need to support it. 

------
#### [ Digital twin capabilities ]

 ![Digital twin capabilities icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_AWS-IoT-TwinMaker_48.png) 

**Digital twin capabilities**

A digital twin is a live digital representation of a system and all of its physical and digital components. It is dynamically updated with data to mimic the true structure, state, and behavior of the system. 

The AWS IoT service that provides digital twin capabilities is [AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html). You can use it to build operational digital twins of physical and digital systems. 

With AWS IoT TwinMaker, you can create digital visualizations to help you keep track of your physical factory, building, or industrial plant. The visualizations use measurements and analyses from a variety of real-world sensors, cameras, and enterprise applications. You can use this real-world data to monitor operations, diagnose and correct errors, and optimize operations. 

------
#### [ Development time ]

 ![Development time icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Dev-Tools_48.png) 

**Development time**

To develop an IoT solution, you will likely need to structure your work into multiple phases, from proof of concept (PoC) to production and scale. You start getting benefits from IoT sooner if you use the right tools to prepare for your PoC, and prove the value of what you’re developing to get the support needed for broader implementation. The AWS tools that you can use for this include:
+ [AWS IoT Core Device Advisor](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html) — This tool provides a cloud-based, fully managed test capability for validating IoT devices during device software development. It includes pre- built tests that you can use to validate IoT devices for reliable and secure connectivity with AWS IoT Core, before deploying devices to production. 
+ [AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) — The SDKs include open source libraries, developer guides with samples, and porting guides. You can use these to build IoT products or solutions on your choice of hardware platforms. 
+ [AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html) — This tool provides code to help your device connect to AWS IoT, perform fleet provisioning tasks, support device security policies, connect using secure tunneling, and process jobs on your device. 
+ [AWS IoT Sensors](https://apps.apple.com/us/app/aws-iot-sensors/id6447531633) (IOS app) — You can use this tool to visualize sensor data from your device with 1-click. 

------
#### [ Video streaming support ]

 ![Video streaming support icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_Amazon-Kinesis-Video-Streams_48.png) 

**Video streaming support**

IoT implementations increasingly have video as a key data source. Those sources can include everything from smartphones, security cameras, and webcams to drones and cameras embedded in cars. In industrial settings, video inputs have become a critical component for automating defect detection sequences on the production line. Here are a couple of the AWS IoT services that you might consider to manage and make effective use of video inputs:
+ [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) — You can use this fully managed AWS service to stream live video from devices to the AWS Cloud, or to build applications for real-time video processing or batch-oriented video analytics. You can also use it to capture massive amounts of live video data from millions of sources. These sources include smartphones, security cameras, webcams, cameras embedded in cars, and drones. 

  In addition, you can use Kinesis Video Streams to send non-video, time series data such as audio data, thermal imagery, depth data, and radar data. Using live video streams from these sources into a Kinesis video stream, you can build applications to access the data, frame-by-frame, in real time for low-latency processing. 
+ [AWS IoT FleetWise](https://aws.amazon.com/blogs/iot/announcing-aws-iot-fleetwise-vision-system-data-preview/) vision system data — Announced in preview at re:Invent 2023, AWS IoT FleetWise supports vision system data collection for vehicles. With this feature, you can collect metadata, object list and detection data, and images or videos from camera, lidar, radar, and other vision subsystems. 

------
#### [ Security ]

 ![Security icon](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch-Category_Security-Identity-Compliance_48.png) 

**Security**

Security is a vital component of any IoT implementation. It's important for any IoT service to ensure that all elements of an IoT connection are encrypted and incorporate security best practices—whether it’s handling data at the edge or in transit to the cloud. 

All traffic to and from [AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/security.html), for example, is sent securely over Transport Layer Security (TLS). AWS cloud security mechanisms protect data as it moves between AWS IoT and other AWS services. AWS IoT services address every layer of your application and device security. 

You can safeguard your device data with preventative mechanisms, like encryption and access control, and consistently audit and monitor your configurations with [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/dd-tutorials.html). You can use AWS IoT Device Defender to proactively assess the cloud configuration of your IoT device fleet, provide ongoing monitoring of device activities through rule-based and ML-based capabilities, and trigger alarms when an audit violation or behavior anomaly is identified. 

------

### Choose
<a name="choose"></a>

Now that you know the criteria that you’ll use to evaluate your IoT service options, you're ready to choose which services might be a good fit.

Use the following table to help determine the services that are the best fit for your organization and use case.

------
#### [ Foundational services ]

These services are foundational to the implementation of Internet of Things (IoT) solutions on AWS.


|  **What is it optimized for?**  |  **Service**  | 
| --- | --- | 
| **Device and design**<br />AWS IoT device software services are optimized to:+  Build and manage IoT applications at the edge <br />+  Quickly transform any embedded device into an IoT-connected device  | [FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html) <br />[AWS IoT ExpressLink](https://docs.aws.amazon.com/iot-expresslink/) <br />[AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) <br />[AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html) <br />[AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)  | 
| **Connect, manage, and monitor**<br />AWS connectivity, control, and monitoring services are optimized to:+  Connect IoT devices to AWS <br />+  Audit IoT configurations <br />+  Secure IoT devices <br />+  Easily monitor and remotely manage IoT devices  | [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) <br />[Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) <br />[AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/dd-tutorials.html) <br />[AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) | 
| **Analyze and act**<br />AWS IoT Events services are optimized to:+  Detect and respond to events from IoT sensors  | [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html)  | 
| **Validate**<br />These tools help you validate your designs. | [AWS IoT Device Tester](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-tester-for-greengrass-ug.html) <br />[AWS IoT Core Device Advisor](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html)  | 

------
#### [ Use case or industry-specific services ]

These services are designed to meet the needs of specific industries or use cases.


|  **What is it optimized for?**  |  **Service**  | 
| --- | --- | 
| **Smart manufacturing**<br />These services are optimized for combining machine data from a single line, a factory, or a network of sites (such as manufacturing plants, assembly facilities, and refineries) to proactively improve performance. | [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started.html) <br />[AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html) <br />[AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html)  | 
| **Connected vehicles**<br />This service is optimized for providing applications that analyze vehicle fleet health, which can help you to more quickly identify potential maintenance issues or make in-vehicle infotainment systems more capable. | [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/getting-started-console-tutorial.html)  | 
| **Public infrastructure**<br />These services are used in smart cities and transportation systems to:+  Support the use of smart metering technologies <br />+  Improve operations and logistics <br />+  Support the tactical edge <br />+  Manage traffic and public safety  | [AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) <br />[AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)  | 

------

### Use
<a name="use"></a>

To get started with the AWS IoT services, we have provided a pathway to explore each service. The following sections provide links to in-depth documentation, hands-on tutorials, and resources.

The first section provides links to resources for the key foundational IoT services: FreeRTOS, AWS IoT Greengrass, AWS IoT ExpressLink, AWS IoT Core, AWS IoT Device Defender, AWS IoT Device Management, AWS IoT Events, Amazon Kinesis Video Streams, and AWS IoT Analytics. 

------
#### [ FreeRTOS ]
+ **What is FreeRTOS?** 

  Learn about the microcontroller operating system that makes small, low-powered edge devices easy to program, deploy, secure, and maintain. 

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html) 

  
+ **AWS IoT Device Tester for FreeRTOS** 

  Use AWS IoT Device Tester for FreeRTOS to qualify data throughput rate with the FreeRTOS operating system. 

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/userguide/device-tester-for-freertos-ug.html) 

  
+ **FreeRTOS Porting Guide** 

  Port FreeRTOS to a microcontroller platform. 

  [Explore the guide](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-guide.html) 

  

------
#### [ AWS IoT Greengrass ]
+ **What is AWS IoT Greengrass** 

  Set up AWS IoT Greengrass and integrate it with other services. 

  [Explore the guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) 

  
+ **AWS IoT Greengrass V2 workshop** 

  Build a virtual environment and an edge gateway that runs AWS IoT Greengrass Core software V2. 

  [Use the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/5ecc2416-f956-4273-b729-d0d30556013f/en-US/chapter1-introduction/10-what-you-are-going-to-build) 

  
+ **AWS IoT Greengrass API Reference** 

  Learn about all the API operations for AWS IoT Greengrass V2 in detail. Read sample requests, responses, and errors for the supported web services protocols. 

  [Explore the API reference](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html) 

  

------
#### [ AWS IoT ExpressLink ]
+ **What is AWS IoT ExpressLink?** 

  Learn how ExpressLink hardware modules are preprogrammed to connect to AWS IoT services and are preloaded with security credentials. 

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/programmersguide/elpg-overview.html) 

  
+ **AWS IoT ExpressLink Onboarding-by-Claim Customer/OEM Guide** 

  Learn about an onboarding-by-claim mechanism that was specifically created to make the most of an AWS IoT ExpressLink module's capabilities. 

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/oemog.html) 

  
+ **Start working with AWS IoT ExpressLink** 

  Explore the AWS IoT ExpressLink development kit and resources to help you start using it. 

  [Explore the guide](https://docs.aws.amazon.com/iot-expresslink/latest/gettingstartedguide/elgsg.html) 

  

------
#### [ AWS IoT Core ]
+ **Get started with AWS IoT Core** 

  Learn about AWS IoT concepts and terms that will help you start using AWS IoT. 

  [Explore the guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) 

  
+ **AWS IoT Core API Reference** 

  Explore the API operations for AWS IoT Core, including the data plane, jobs, and secure tunneling. It also provides sample requests, responses, and errors. 

  [Explore the API reference](https://docs.aws.amazon.com/iot/latest/apireference/index.html) 

  
+ **AWS IoT Core tutorials** 

  Discover AWS IoT tutorials and choose the best learning path for your goal. 

  [Get started with the tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html) 

  

------
#### [ AWS IoT Device Defender ]
+ **What is AWS IoT Device Defender?** 

  Learn about AWS IoT Device Defender, a security and monitoring service you can use to audit the configuration of your devices, monitor connected devices, and mitigate security risks. 

  [Explore the guide](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html) 

  
+ **Use the disconnected duration metric in AWS IoT Device Defender** 

  The disconnected duration metric in AWS IoT Device Defender provides AWS IoT Device Defender Detect customers the ability to monitor Internet of Things (IoT) device connectivity status and duration of disconnection. This blog explains how to use it. 

  [Read the blog](https://aws.amazon.com/blogs/iot/how-to-get-started-with-the-new-disconnected-duration-metric-in-aws-iot-device-defender/) 

  
+ **AWS IoT Device Defender pricing guide** 

  Learn how the pricing elements of the service work. 

  [Explore the pricing guide](https://aws.amazon.com/iot-device-defender/pricing/) 

  

------
#### [ AWS IoT Device Management ]
+ **Get started with AWS IoT Device Management** 

  Start managing devices (also known as "things") and see an example of how information about things is stored in your registry as JSON data. 

  [Explore the guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) 

  
+ **AWS IoT Device Management FAQs** 

  Learn about where, how, when, and why you might use AWS IoT Device Management. 

  [Explore the FAQs](https://aws.amazon.com/iot-device-management/faq/) 

  
+ **Secure Internet of Things (IoT) with AWS** 

  Get a detailed look at how you can use AWS security services to secure your IoT workloads in consumer and industrial environments. 

  [Explore the whitepaper](https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/securing-iot-with-aws.html) 

  

------
#### [ AWS IoT Events ]
+ **What is AWS IoT Events?** 

  Use AWS IoT Events to monitor your equipment or device fleets for failures or changes in operation, and to initiate actions when such events occur. 

  [Explore the guide](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html) 

  
+ **AWS IoT Events pricing guide** 

  Learn how AWS IoT Events pricing works. 

  [Explore the pricing guide](https://aws.amazon.com/iot-events/pricing/) 

  
+ **AWS IoT Events FAQs** 

  Learn about where, how, when and why you might use AWS IoT Events. 

  [Explore the FAQs](https://aws.amazon.com/iot-events/faqs/) 

  

------
#### [ Amazon Kinesis Video Streams ]
+ **What is Amazon Kinesis Video Streams?** 

  Use Kinesis Video Streams to stream live video from devices to the AWS Cloud, or to build applications for real-time video processing or batch-oriented video analytics. 

  [Explore the guide](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) 

  
+ **Amazon Kinesis Video Streams pricing** 

  Learn how Kinesis Video Streams pricing works. 

  [Explore the pricing guide](https://aws.amazon.com/kinesis/video-streams/pricing/) 

  
+ **Amazon Kinesis Video Streams with WebRTC Developer Guide** 

  Use Kinesis Video Streams with WebRTC to build applications for live peer-to-peer media streaming, or for real-time audio or video interactivity between camera IoT devices, web browsers, and mobile devices. 

  [Explore the guide](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/what-is-kvswebrtc.html) 

  

------

This section links to resources about use case or industry-specific AWS IoT services, including AWS IoT SiteWise, AWS IoT TwinMaker, and AWS IoT FleetWise.

------
#### [ AWS IoT SiteWise ]
+ **What is AWS IoT SiteWise?** 

  Use AWS IoT SiteWise to collect, model, analyze, and visualize data from industrial equipment at scale. 

  [Explore the guide](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) 

  
+ **AWS IoT SiteWise pricing guide** 

  Learn how AWS IoT SiteWise pricing works—with separate charges for usage of Messaging, Data Processing, Data Storage, Data Export, AWS IoT SiteWise Monitor, AWS IoT SiteWise Edge, and Alarms. 

  [Explore the pricing guide](https://aws.amazon.com/iot-sitewise/pricing/) 

  
+ **AWS IoT SiteWise FAQs** 

  Learn about where, how, when and why you might use AWS IoT SiteWise. 

  [Explore the FAQs](https://aws.amazon.com/iot-sitewise/faqs/) 

  

------
#### [ AWS IoT TwinMaker ]
+ **What is AWS IoT TwinMaker?** 

  Use AWS IoT TwinMaker to build operational digital twins of physical and digital systems. 

  [Explore the guide](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html) 

  
+ **AWS IoT TwinMaker pricing guide** 

  Learn how AWS IoT TwinMaker pricing works. You can choose between the basic, standard, and tiered bundle pricing plans, depending upon the size and unique characteristics of your workloads. 

  [Explore the pricing guide](https://aws.amazon.com/iot-twinmaker/pricing/) 

  
+ **AWS IoT TwinMaker FAQs** 

  Learn about where, how, when and why you might use AWS IoT TwinMaker. 

  [Explore the FAQs](https://aws.amazon.com/iot-twinmaker/faqs/) 

  

------
#### [ AWS IoT FleetWise ]
+ **What is AWS IoT FleetWise?** 

  Use AWS IoT FleetWise to collect, transform, and transfer vehicle data to the cloud in near real time. 

  [Explore the guide](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html) 

  
+ **AWS IoT FleetWise pricing guide** 

  Learn how pricing works for AWS IoT FleetWise. It describes how it works on two dimensions: by number of vehicles and by number of messages. 

  [Explore the pricing guide](https://aws.amazon.com/iot-fleetwise/pricing/) 

  
+ **AWS IoT FleetWise FAQs** 

  Learn about where, how, when and why you might use AWS IoT FleetWise. 

  [Explore the FAQs](https://aws.amazon.com/iot-fleetwise/faqs/) 

  

------

### Explore
<a name="explore"></a>
+ **Architecture diagrams** 

  Explore reference architecture diagrams to help you develop your IoT solutions on AWS. 

  [Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all) 

  
+ **Whitepapers** 

  Explore whitepapers to help you get started, learn best practices, and understand your IoT options. 

  [Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all) 

  
+ **AWS videos** 

  Explore videos that will help you better use and understand the available AWS IoT services. 

  [Watch the videos](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23video&awsf.methodology=*all&awsf.tech-category=tech-category%23iot&awsf.industries=*all&awsf.business-category=*all) 

  

# Choosing an AWS networking and content delivery service
<a name="choosing-networking-and-content-delivery-service"></a>


|  |  | 
| --- |--- |
| **Purpose:** | Help determine which AWS networking and content delivery services are the best fit for your organization. | 
| **Last updated:** | January 16, 2025 | 
| **Covered services:** |  +  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) <br />+  [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html) <br />+  [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) <br />+  [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) <br />+  [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) <br />+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) <br />+  [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) <br />+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) <br />+  [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) <br />+  [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) <br />+  [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) <br />+  [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) <br />+  [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) <br />+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) <br />+  [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) <br />+  [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html) <br />+  [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) <br />+  [Amazon VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) <br />+  [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) <br />+  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)   | 

Deciding on an approach to cloud networking and content delivery can be complex, especially if you’re used to managing and configuring networks with on-premises hardware. Fortunately, [building networks in the cloud](https://aws.amazon.com/what-is/computer-networking/) shares core concepts with building on-premises, such as IP addressing, load balancing, and routing. Familiarity with these concepts will help you understand what AWS services you need.

Amazon Web Services (AWS) offers 20\+ purpose-built networking and content delivery services that you can use to build, operate, and secure your cloud networks across all your cloud environments and distributed cloud and edge locations globally. You can also build network infrastructure that extends your on-premises environment to AWS. 

This decision guide will help you ask the right questions to choose the networking and content delivery services and tools that fit your needs.

[![AWS Videos](https://img.youtube.com/vi/cRdDCkbE4es?start=123&end=373/0.jpg)](https://www.youtube.com/watch?v=cRdDCkbE4es?start=123&end=373)


## Understand
<a name="understand"></a>

What you build in AWS depends on your business needs. In this guide, we use the term *workloads* to refer to any collection of resources and code that delivers business value, such as a customer-facing application or a backend process.

Networking and content delivery services at AWS fall into four categories: networking foundations, global and hybrid connectivity, edge networking and content delivery, and application networking.

![Diagram showing AWS networking services for every application and workload](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/cloud-networking-from-aws.png)


**Networking foundations**

In AWS, your workloads run inside one or more [Amazon Virtual Private Cloud (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). After your workloads are running in VPCs, you can connect the workloads to other VPCs—such as an [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)—or you can connect them to software as a service (SaaS) services including other AWS services, such as [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). Amazon VPC lets you provision a private, isolated section of the AWS Cloud where you can launch AWS resources in a virtual network using customer-defined IP address ranges. Amazon VPC gives you several options for connecting your AWS virtual networks with other remote networks.

**Global and hybrid connectivity**

You can use the services in this category to securely connect from on-premises networks to your workloads in the AWS Cloud. You can create a [virtual private network (VPN)](https://aws.amazon.com/what-is/vpn/) to connect remote users by using [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html), connect on-premises networks using [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), or build a global wide area network (WAN) with [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html). You can also set up a direct, private connection to the AWS Cloud using [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), providing a direct, secure connection to the cloud with predictable performance. You may also need to connect your on-premises data centers, remote sites, and the cloud. [A hybrid network](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html) can connect these different environments. 

**Edge networking and content delivery**

Services in this category help ensure higher performance through caching and optimized transport. A good example of this is [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). You'll also want to see customer traffic optimally routed to provide availability using services such as [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html). Additionally, it's important that customer traffic is routed to make the most of the AWS global infrastructure using services such as [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html). [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) is a network-ready, physical location where you can bring your data storage devices for fast data transfer to and from the AWS Cloud.

**Application networking**

As you increase adoption of the AWS Cloud, you’ll want to consider how to connect workloads at scale, by using [AWS App Mesh](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html) and [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html), integrate the workloads in your VPCs with [APIs](https://aws.amazon.com/what-is/api/) by using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), and manage the IP address usage of the resources running in your VPCs by using [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html). As customer demand increases, you can help ensure that the workloads in your VPCs can scale and provide high availability by using [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html).

**Networking security and remote access**

While Amazon VPC helps you secure access to your workloads, the services in this category offer enhanced protection against threat actors and unauthorized users by using [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html), [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html), and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). To help ensure network security, consider using Amazon Route 53 DNS Firewall, [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html), [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and security groups.

## Consider
<a name="consider"></a>

It's important that you choose the networking services that fit your business needs. The following are some of the criteria to consider when choosing networking services.

------
#### [ Business objectives ]

The networking services that you choose will depend on your business objectives. Assess where you are now and where you want to be when it comes to the security, reliability, accessibility, and performance of your workloads running in the AWS Cloud.
+ Consider how the network services you use fit with your migration and integration strategies. A [hybrid networking architecture](https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/definition.html) can help you meet this need by integrating your on-premises data center and AWS.
+ Review the [networking and content delivery blogs](https://aws.amazon.com/blogs/networking-and-content-delivery/) in the *Let’s architect\!* AWS blog series to see what others are building in the AWS Cloud.
+ Examine the third-party options available to help you accelerate your networking service adoption. The [AWS Marketplace](https://aws.amazon.com/marketplace/solutions/infrastructure-software/cloud-networking) provides a curated digital catalog that you can use to find, buy, and deploy networking solutions.
+ Decide if working with an [AWS Partner](https://aws.amazon.com/partners/work-with-partners/) that specializes in networking and content delivery would be beneficial. Members of the AWS Partner Network are strategic experts and experienced builders that can help you meet your needs with the AWS Cloud.
+ Explore taking [AWS networking online courses](https://explore.skillbuilder.aws/learn/public/learning_plan/view/1944/networking-core-knowledge-badge-readiness-path) on AWS Skill Builder that cover services such as Amazon VPC, AWS Cloud WAN, and Amazon Route 53.

------
#### [ Workload characteristics ]

The networking services that you choose will depend on the characteristics of your workloads.
+ Networking services each have a particular role. Services such as AWS Cloud WAN and AWS Transit Gateway are suited for connecting workloads that are running in VPCs. Amazon API Gateway creates public APIs so that your customers can connect to your workloads. AWS Global Accelerator can help you improve the reliability, security, and latency of your workloads. 
+ As the internet continues to grow, so does the need for IP addresses for devices. The most common format for IP addresses is IPv4. The latest format for IP addresses is IPv6. IPv6 provides more address space and solves the problem of [IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion). AWS services support for IPv6 includes support for dual stack configuration (IPv4 or IPv6) or IPv6 only configurations. The number of AWS services that support IPv6 is growing continuously. To view the current services that support IPv6, see [AWS services that support IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ipv6-support.html).

------
#### [ Data protection ]

It’s important to consider the protection of your data in the AWS Cloud.
+ Businesses must protect customer data against evolving cyber risks. While Amazon VPC helps you to secure access to the workloads running in VPCs, consider enhanced data protection measures, such as AWS Network Firewall, AWS Shield, AWS WAF, and Amazon Route 53 Resolver DNS Firewall.
+ It's recommended that you employ application-level encryption (TLS), irrespective of the transport, as a defense in depth measure to help ensure confidentiality end-to-end.
+ If the workloads in your VPCs need to connect to other AWS services, you can connect to those services programmatically by using API endpoints over the public internet. However, if you want to send data over a private connection, use AWS PrivateLink. Many members of the AWS Partner Network offer their SaaS solutions through AWS PrivateLink.

------
#### [ Availability ]

*Availability* is an application’s ability to maintain uptime. It’s important that your customers can use the products and services that you build in your VPCs with minimal or no downtime.
+ The AWS global infrastructure is built on [AWS Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/?p=ngi&loc=2&refid=67adb321-e6e5-4750-92f4-b5d8e229d6bf). When you deploy your workloads to your VPCs, you should deploy to multiple Availability Zones to ensure that your workload is still available in the event of a single Availability Zone failure.
+ To improve the availability, scalability, security, and performance of the workloads running in your VPCs, consider [load balancing](https://aws.amazon.com/what-is/load-balancing/) (Elastic Load Balancing). You can use different types of load balancers depending on the needs of your applications. Each load balancer supports different types of traffic over different protocols and network layers aligned to the [Open Systems Interconnection (OSI)](https://aws.amazon.com/what-is/osi-model/) model. For more information about the differences between load balancer types, see [product comparisons](https://aws.amazon.com/elasticloadbalancing/features/#Product_comparisons).

------
#### [ Performance ]

You can use networking services to optimize for the latency, throughput, and bandwidth requirements of your workloads running on the AWS global infrastructure.
+ If you want to minimize latency to local customers using web applications around the globe, consider using Amazon CloudFront. CloudFront is a [content delivery network](https://aws.amazon.com/what-is/cdn/) that delivers content to customers with the lowest latency possible.
+ If you’re running gaming, Internet of Things (IoT), or Voice over IP (VoIP) workloads, consider using AWS Global Accelerator. This service helps you improve your workloads’ availability and performance.
+ If the workloads in your VPCs need to connect to other AWS Regions, you can connect to those services programmatically using public API endpoints. 

------
#### [ Operational excellence ]

As you increase AWS Cloud adoption, you’ll want to understand what is happening across your workloads at any time. Tools and services such as [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) and [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) can help you keep pace with changing business needs and priorities as your workloads grow.
+ Managing IP addresses of workloads running in multiple VPCs can be difficult. Consider if you need to automate IP address management across your workloads (Amazon VPC IPAM).
+ If you’re using a [microservice architecture](https://aws.amazon.com/microservices/), managing the connectivity, security, and monitoring between microservices can be a challenge. Consider if you need to automate microservice interaction (AWS App Mesh and Amazon VPC Lattice).

------
#### [ Connectivity ]

You can use networking services to connect to the AWS Cloud, connect workloads, or connect networks.
+ Consider the following for connecting to the AWS Cloud:
  + If you want to securely connect remote users to your VPCs, consider using AWS Client VPN.
  + If you want to securely connect an entire on-premises network to your VPCs, consider using AWS Site-to-Site VPN.
  + If you require more consistent performance than the internet can provide, consider a direct connection from your on-premises network to AWS (Direct Connect).
  + If you need to quickly move data into or out of the AWS Cloud, consider using AWS Data Transfer Terminal.
+ Consider the following for connecting networks:
  + If you operate in multiple AWS Regions, want to manage your own routing configurations, or prefer to use your own automation, consider using AWS Transit Gateway.
  + If you want to unify your data center, branch, and AWS networks with a WAN, consider using AWS Cloud WAN. It is also worth considering if you don't want to manage complex routing configurations or build your own automations for multi-Region connectivity.

------
#### [ Security ]

AWS provides a secure foundation for you to build and deploy your applications, but you are responsible for implementing your own security measures to protect your data, applications, and networking infrastructure, no differently than you would in an on-site data center.
+ Review and understand the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) and how it applies to security in the AWS Cloud.
+ AWS security groups and network access control lists (NACLs) can be used together or on their own to secure a network, helping you to create a defense in depth security strategy.
+ Businesses must protect their network applications against evolving cyber risks. Consider if you will need to protect your workloads against malicious attacks or malware (with [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)), distributed denial of service (DDoS) attacks (with AWS Shield), or SQL injection and cross-site scripting attacks (with AWS WAF).

  Amazon Route 53, [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html), [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html), and security groups are also important to consider in ensuring network security. 

------

## Choose
<a name="choose"></a>

Now that you know the criteria by which you will be evaluating your networking service options, you are ready to choose which services may be a good fit.



| Service category | What is it optimized for? | AWS networking and content delivery services | 
| --- |--- |--- |
| Network foundations | Optimized for getting started with AWS networking services and connecting your VPCs securely. | [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)<br />[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)<br />[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) | 
|  Global and hybrid connectivity  |  Optimized to ensure private, secure, and global network connectivity.  |  [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html) [AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html) [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)  | 
| --- |--- |--- |
| Edge networking and content delivery | Optimized for low latency, reliable traffic routing to and from your workloads. | [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)<br />[AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)<br />[Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)<br />[AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html) | 
|  Application networking  |  Optimized to ensure that your workloads are highly available, adapt to demand, and can communicate with each other.  |  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) [Amazon VPC IPAM ](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)  | 
| --- |--- |--- |
| Network security and remote access | Optimized to protect your workloads against malware, DDoS, SQL injection, and cross-site scripting attacks. | [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)<br />[AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)<br />[AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)<br />[AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html)<br />[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) | 

## Use
<a name="use"></a>

To explore how to use and learn more about each of the available AWS network services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

The following services cover global networking and VPC connectivity.

------
#### [ Amazon CloudFront ]
+ **What is Amazon CloudFront?**

  Learn about speeding up content distribution.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+ **Getting started with Amazon CloudFront**

  Learn the basic steps to delivering content with CloudFront.

  [Explore the guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html)
+ **Hosting on-demand streaming video with Amazon S3, Amazon CloudFront, and Amazon Route 53**

  Learn how to host videos for on-demand viewing in a secure and scalable way.

  [Get started with the tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-cloudfront-route53-video-streaming.html)
+ **Deliver content faster with Amazon CloudFront**

  Learn how to decrease the end user latency of your web applications.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/deliver-content-faster/?ref=gsrchandson)

------
#### [ AWS Cloud WAN ]
+ **What is AWS Cloud WAN?**

  Learn how to build, manage, and monitor a unified global network.

  [Explore the guide](https://docs.aws.amazon.com/network-manager/latest/cloudwan/what-is-cloudwan.html)
+ **Introducing AWS Cloud WAN**

  Learn about the main use cases for AWS Cloud WAN and how to get started.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-cloud-wan-preview/)
+ **Getting started with AWS Cloud WAN**

  Create your first global network and attach a VPC.

  [Get started with the tutorial](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-getting-started.html)

------
#### [ Direct Connect ]
+ **What is Direct Connect?**

  Learn about connecting an on-premises network to AWS.

  [Explore the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+ **Getting started with Direct Connect**

  Watch a brief introduction to AWS Direct Connect and how to prepare your on-premises network to connect to AWS.

  [Watch the video](https://www.youtube.com/watch?v=y4rIwSbdlS0)
+ **Connect your data center to AWS**

  Connect your data center to AWS using Direct Connect.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/connect-data-center-to-aws/?ref=gsrchandson&id=itprohandson)

------
#### [ AWS Global Accelerator ]
+ **What is AWS Global Accelerator?**

  Learn about improving the performance of your workloads.

  [Explore the guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
+ **Getting started with a standard accelerator**

  Create an accelerator to improve the network performance of a workload running on an EC2 instance.

  [Get started with the tutorial](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started-standard.html)
+ **Improve global application availability and performance for your traffic**

  Watch a brief demonstration on setting up AWS Global Accelerator to improve network performance.

  [Watch the video](https://www.youtube.com/watch?v=Docl4julOQw)

------
#### [ AWS PrivateLink ]
+ **What is AWS PrivateLink?**

  Learn how to privately connect your VPC to services.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
+ **Get started with AWS PrivateLink**

  Send a request from an EC2 instance in a private subnet to Amazon CloudWatch using PrivateLink.

  [Get started with the tutorial](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)
+ **Expedite your IPv6 adoption with PrivateLink services and endpoints**

  Customers with large internet footprints feel the strain of public IPv4 address exhaustion. Learn how you can increase IPv6 usage within VPCs using PrivateLink.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/)

------
#### [ Amazon Route 53 ]
+ **What is Amazon Route 53?**

  Learn about highly available and scalable domain name resolution.

  [Explore the guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
+ **Amazon Route 53 use case tutorials**

  How to use Route 53 for use cases based on traffic and latency.

  [Get started with the tutorial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Tutorials.html)
+ **How to register a domain name with Amazon Route 53**

  This tutorial helps you register a new domain name for a web application.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/get-a-domain/?ref=gsrchandson&id=updated)
+ **Amazon Route 53 introduction**

  Watch a brief introduction to domain name resolution and Route 53.

  [Watch the video](https://www.youtube.com/watch?v=RGWgfhZByAI)

------
#### [ AWS Data Transfer Terminal ]
+ **What is AWS Data Transfer Terminal?**

  Learn how you can quickly upload or download large datasets to the AWS Cloud using your own storage devices.

  [Explore the guide](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)
+ **Introducing AWS Data Transfer Terminal**

  Learn about the main use cases and how to get started.

  [Read the blog](https://aws.amazon.com/blogs/aws/new-physical-aws-data-transfer-terminals-let-you-upload-to-the-cloud-faster/)

------
#### [ AWS Site-to-Site VPN ]
+ **What is AWS Site-to-Site VPN?**

  Learn about connecting remote users to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+ **Getting started with AWS Site-to-Site VPN**

  Set up a Site-to-Site VPN connection between an on-premises device and AWS.

  [Get started with the tutorial](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)
+ **AWS Site-to-Site VPN, choosing the right options to optimize performance**

  Choose the best options when setting up a VPN connection to AWS.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-site-to-site-vpn-choosing-the-right-options-to-optimize-performance/)

------
#### [ AWS Transit Gateway ]
+ **What is a transit gateway?**

  Learn how to connect VPCs with transit gateways.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+ **Example transit gateway use cases**

  View common use cases for transit gateways.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html)
+ **AWS Transit Gateway workshop**

  In this hands-on workshop, learn how to deploy Transit Gateway in single Region and single account, multi-account, and multi-Region setups.

  [Start the workshop](https://tgw.networking-workshop.com/#/README)

------
#### [ Amazon VPC ]
+ **What is Amazon VPC?**

  Learn about virtual private clouds and the features of Amazon VPC.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+ **Get started with Amazon VPC**

  A guide to quickly getting started with Amazon VPC.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html)
+ **Example VPC configurations**

  View example VPC configurations based on different use cases.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-examples-intro.html)
+ **Modular and scalable VPC architecture**

  Build a virtual networking foundation based on AWS best practices for your AWS Cloud infrastructure.

  [Get started with the tutorial](https://aws.amazon.com/quickstart/architecture/vpc/?ref=gsrchandson)

------
#### [ Amazon VPC IPAM ]
+ **What is IPAM?**

  Learn how to track and manage IP address usage.

  [Explore the guide](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
+ **Amazon VPC IP Address Manager (IPAM) best practices**

  Learn how to create a scalable IP address management plan.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/)
+ **Creating pools to manage your IP space**

  Watch a brief video introduction to VPC IPAM.

  [Watch the video](https://www.youtube.com/watch?v=11BqzuUDTMM)

------

The following services relate to application level networking.

------
#### [ Amazon API Gateway ]
+ **What is Amazon API Gateway?**

  Learn about creating APIs for your workloads.

  [Explore the guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
+ **Building APIs with Amazon API Gateway**

  Learn how to get started building APIs in AWS.

  [Watch the video](https://www.youtube.com/watch?v=XwfpPEFHKtQ)
+ **Configuring private integrations with Amazon API Gateway HTTP APIs**

  Learn how to create an API to control private access to resources in a VPC.

  [Read the blog](https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/)

------
#### [ AWS Client VPN ]
+ **What is AWS Client VPN?**

  Learn about connecting networks to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
+ **Getting started with AWS Client VPN**

  Download the AWS Client VPN application and connect to AWS over VPN.

  [Explore the guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/user-getting-started.html)
+ **Scenarios and examples for AWS Client VPN**

  See examples for creating and configuring Client VPN access for your clients.

  [Explore the examples](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/how-it-works.html#scenario)

------
#### [ Elastic Load Balancing ]
+ **What is Elastic Load Balancing?**

  Learn about distributing incoming traffic across your workloads.

  [Explore the guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
+ **Getting started with Elastic Load Balancing**

  Learn the difference between the different types of load balancers and create a load balancer.

  [Explore the guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-getting-started.html)
+ **How to choose the right load balancer for your AWS workloads**

  Choose the right option to load balance traffic to your workloads.

  [Watch the video](https://www.youtube.com/watch?v=p0YZBF03r5A)

------
#### [ AWS Firewall Manager ]
+ **Getting started with AWS Firewall Manager policies**

  Learn how to use AWS Firewall Manager to enable a number of different types of security policies.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)
+ **How to continuously audit and limit security groups with AWS Firewall Manager**

  This blog post demonstrates how to use AWS Firewall Manager to limit security groups to help ensure that only required ports are open.

  [Explore the guide](https://aws.amazon.com/blogs/security/how-to-continuously-audit-and-limit-security-groups-with-aws-firewall-manager/)
+ **Use AWS Firewall Manager to deploy protection at scale in AWS Organizations**

  This post provides step-by-step instructions to deploy and manage security policies across your AWS Organizations implementation by using AWS Firewall Manager.

  [Explore the guide](https://aws.amazon.com/blogs/security/use-aws-firewall-manager-to-deploy-protection-at-scale-in-aws-organizations/)

------
#### [ AWS Network Firewall ]
+ **What is AWS Network Firewall?**

  Learn about network firewall and intrusion detection.

  [Explore the guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
+ **Getting started with AWS Network Firewall**

  Quickly create and manage a network firewall for a VPC.

  [Get started with the tutorial](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html)
+ **AWS Network Firewall animated explainer video**

  Watch a brief video introduction to AWS Network Firewall.

  [Watch the video](https://www.youtube.com/watch?v=Y7-37tkO1CA)

------
#### [ AWS Shield ]
+ **What is AWS Shield?**

  Learn about DDoS protection.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#ddos-intro)
+ **Examples of basic DDoS resilient architectures**

  Learn about some common DDoS-resilient architectures.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency.html)
+ **AWS Shield animated explainer video**

  Watch a brief video introduction to AWS Shield.

  [Watch the video](https://www.youtube.com/watch?v=7rgiXEa0_jE)

------
#### [ AWS Verified Access ]
+ **Tutorial: Getting started with Verified Access**

  In this tutorial, you will learn how to create and configure Verified Access resources.

  [Explore the guide](https://docs.aws.amazon.com/verified-access/latest/ug/getting-started.html)
+ **AWS Verified Access Integration with third party identity providers**

  This blog post shows you how to integrate Verified Access (AVA) with the third party Okta identity provider.

  [Explore the guide](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-verified-access-integration-with-3rd-party-identity-providers/)
+ **Integrating AWS Verified Access with device trust providers**

  This blog post discusses how to architect Zero Trust based remote connectivity on AWS.

  [Explore the examples](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-verified-access-with-device-trust-providers/)

------
#### [ Amazon VPC Lattice ]
+ **What is Amazon VPC Lattice?**

  Learn about connecting, securing, and monitoring the microservices in your workloads.

  [Explore the guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
+ **Setting up Amazon VPC Lattice**

  Set up and launch VPC Lattice for the first time.

  [Explore the guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/setting-up.html)
+ **Build secure multi-account multi-VPC connectivity for your applications with Amazon VPC Lattice**

  An introduction to how you can use VPC Lattice to solve VPC connectivity challenges.

  [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/build-secure-multi-account-multi-vpc-connectivity-for-your-applications-with-amazon-vpc-lattice/)
+ **Amazon VPC Lattice animated explainer**

  Watch a brief animated video about VPC Lattice.

  [Watch the video](https://www.youtube.com/watch?v=fyb20oApiZw)

------
#### [ AWS WAF ]
+ **What is AWS WAF?**

  Learn about controlling access to your workloads.

  [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#waf-intro)
+ **Getting started with AWS WAF**

  Watch a brief video on how you can use AWS WAF to protect your workloads against web exploits and bots.

  [Watch the video](https://www.youtube.com/watch?v=R5XMny416vo)
+ **Video introduction to AWS WAF**

  Watch a brief video introduction to AWS WAF.

  [Watch the video](https://www.youtube.com/watch?v=nUI7G9UzyN8)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you build your networking and content delivery architectures on AWS.

  [Explore architecture diagrams ](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23networking-content-dev&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your networking and content delivery options.

  [Explore whitepapers](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23networking-content-dev&awsf.industries=*all&awsf.business-category=*all)
+ **AWS Solutions**

  Explore vetted solutions and architectural guidance for common use cases for networking and content delivery.

  [Explore AWS Solutions ](https://aws.amazon.com/solutions/networking/)

# Security, identity, and compliance
<a name="security-identity-compliance"></a>

The following decision guides help you choose AWS services for security, identity, cryptography, and web application protection.

**Topics**
+ [Choosing AWS security, identity, and governance services](#choosing-aws-security-services)
+ [Choosing an AWS identity service](#identity-on-aws-how-to-choose)
+ [Choosing an AWS cryptography service](#guide)
+ [AWS WAF or AWS Shield?](#waf-or-shield)

## Choosing AWS security, identity, and governance services
<a name="choosing-aws-security-services"></a>

**Taking the first step**


<table>
<tbody>
  <tr><td><b>Time to read</b></td><td colspan="2">27 minutes</td></tr>
  <tr><td><b>Purpose</b></td><td colspan="2">Help you determine which AWS security, identity, and governance services are the best fit for your organization.</td></tr>
  <tr><td><b>Last updated</b></td><td colspan="2">December 30, 2024</td></tr>
  <tr><td><b>Services covered</b></td><td> <ul><li> <a href="https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html">AWS Artifact</a> </li><li> <a href="https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html">AWS Audit Manager</a> </li><li> <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html">AWS Certificate Manager</a>  </li><li> <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html">AWS CloudHSM</a>  </li><li>  <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html">AWS CloudTrail</a>  </li><li>  <a href="https://docs.aws.amazon.com/cognito">Amazon Cognito</a>  </li><li>  <a href="https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html">AWS Config</a>  </li><li>  <a href="https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html">AWS Control Tower</a>  </li><li>  <a href="https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html">Amazon Detective</a>  </li><li>  <a href="https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html">AWS Firewall Manager</a>  </li><li>  <a href="https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html">Amazon GuardDuty</a>  </li><li>  <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html">AWS IAM</a>  </li><li>  <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html">AWS IAM Identity Center</a>  </li><li>  <a href="https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html">Amazon Inspector</a>  </li></ul> </td><td> <ul><li>  <a href="https://docs.aws.amazon.com/kms/latest/developerguide/overview.html">AWS KMS</a>  </li><li>  <a href="https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html">Amazon Macie</a>  </li><li>  <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html">AWS Network Firewall</a>  </li><li>  <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html">AWS Organizations</a>  </li><li>  <a href="https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html">AWS Payment Cryptography</a>  </li><li>  <a href="https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html">AWS Private CA</a>  </li><li>  <a href="https://docs.aws.amazon.com/ram/latest/userguide/what-is.html">AWS RAM</a>  </li><li>  <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html">AWS Secrets Manager</a>  </li><li>  <a href="https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html">AWS Security Hub CSPM</a>  </li><li>  <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html">Amazon Security Lake</a>  </li><li>  <a href="https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html">AWS Security Incident Response</a>  </li><li>  <a href="https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html">AWS Shield</a>  </li><li>  <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html">AWS WAF</a>  </li></ul> </td></tr>
</tbody>
</table>


### Introduction
<a name="intro"></a>

Security, identity, and governance in the cloud are important components for you in achieving and maintaining integrity and safety for your data and services. This is especially relevant as more businesses migrate to cloud providers such as Amazon Web Services (AWS). 

 This guide helps you select the AWS security, identity, and governance services and tools that are the best fit for your needs and your organization. 

 First, let's explore what we mean by security, identity, and governance: 
+  [Cloud security](https://aws.amazon.com/security/) refers to using measures and practices to protect digital assets from threats. This includes both the physical security of data centers and cybersecurity measures to guard against online threats. AWS prioritizes security through encrypted data storage, network security, and continuous monitoring of potential threats. 
+  [Identity](https://aws.amazon.com/identity/) services help you securely manage identities, resources, and permissions in a scalable way. AWS provides identity services designed for workforce and customer-facing applications, and for managing access to your workloads and applications. 
+  [Cloud governance](https://aws.amazon.com/cloudops/cloud-governance/) is a set of rules, processes, and reports that guide your organization to follow best practices. You can establish cloud governance across your AWS resources, use built-in best practices and standards, and automate compliance and auditing processes. [Compliance](https://aws.amazon.com/compliance/) in the cloud refers to adhering to laws and regulations governing data protection and privacy. [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) provides information about the certifications, regulations, and frameworks that AWS aligns with. 

[![AWS Videos](https://img.youtube.com/vi/T4svAhNLNfc/0.jpg)](https://www.youtube.com/watch?v=T4svAhNLNfc)


### Understand AWS security, identity, and governance services
<a name="understand"></a>

#### Security and compliance are shared responsibilities
<a name="security-and-compliance-are-shared-responsibilities"></a>

Before choosing your AWS security, identity, and governance services, it's important for you to understand that security and compliance are [shared responsibilities](https://aws.amazon.com/compliance/shared-responsibility-model/) between you and AWS. 

The nature of this shared responsibility helps relieve your operational burden, and it provides you with flexibility and control over your deployment. This differentiation of responsibility is commonly referred to as *security "of" the cloud* and *security "in" the cloud*. 

With an understanding of this model, you can understand the range of options available to you, and how the applicable AWS services fit together. 

#### You can combine AWS tools and services to help safeguard your workloads
<a name="you-can-combine-aws-tools-and-services-to-help-safeguard-your-workloads"></a>

![The five domains across security, identity, and governance include identity and access management, network and app protection, data protection, detection and response, and governance and compliance.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/security-identity-governance-services.png)


As shown in the previous diagram, AWS offers tools and services across five domains to help you achieve and maintain robust security, identity management, and governance in the cloud. You can use AWS services across these five domains to help you do the following: 
+ Form a multilayered approach to safeguarding your data and environments
+ Fortify your cloud infrastructure against evolving threats
+ Adhere to strict regulatory standards

 To learn more about AWS security, including security documentation for AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/). 

 In the following sections, we examine each domain further. 

##### Understand AWS identity and access management services
<a name="identity-and-access-management-2"></a>

At the center of AWS security is the principle of least privilege: individuals and services have only the access that they need. [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) is the recommended AWS service for managing user access to AWS resources. You can use this service to manage access to your accounts and permissions within those accounts, including identities from external identity providers. 

The following table summarizes the identity and access management offerings discussed in this guide: 

------
#### [ AWS IAM Identity Center ]

 [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you connect your source of identities, or create users. You can centrally manage workforce access to multiple AWS accounts and applications. 

------
#### [ Amazon Cognito ]

 [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides an identity tool for web and mobile apps to authenticate and authorize users from the built-in user directory, your enterprise directory, and consumer identity providers. 

------
#### [ AWS RAM ]

 [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts, within your organization, and with IAM roles and users. 

------
#### [ IAM ]

 [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) enables secure, fine-grained control over access to AWS workload resources. 

------

##### Understand AWS data protection services
<a name="data-protection-2"></a>

Data protection is vital in the cloud, and AWS provides services that help you protect your data, accounts, and workloads. For example, encrypting your data both in transit and at rest helps protect it from exposure. With [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) (AWS KMS) and [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) you can create and control the cryptographic keys that you use to protect your data. 

The following table summarizes the data protection offerings discussed in this guide: 

------
#### [ Amazon Macie ]

 [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) discovers sensitive data by using machine learning and pattern matching, and enables automated protection against associated risks. 

------
#### [ AWS KMS ]

 [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) creates and controls the cryptographic keys that you use to protect your data. 

------
#### [ AWS CloudHSM ]

 [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) provides highly available, cloud-based hardware security modules (HSMs). 

------
#### [ AWS Certificate Manager ]

 [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys. 

------
#### [ AWS Private CA ]

 [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) helps you create private certificate authority hierarchies, including root and subordinate certificate authorities (CAs). 

------
#### [ AWS Secrets Manager ]

 [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets. 

------
#### [ AWS Payment Cryptography ]

 [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html) provides access to cryptographic functions and key management used in payment processing in accordance with payment card industry (PCI) standards. 

------

##### Understand AWS network and application protection services
<a name="network-and-app-protection-2"></a>

AWS offers several services to protect your networks and applications. [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) provides you with protection against Distributed Denial of Service (DDoS) attacks, and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) helps you protect web applications from common web exploitation attacks. 

The following table summarizes the network and application protection offerings discussed in this guide: 

------
#### [ AWS Firewall Manager ]

 [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) simplifies your administration and maintenance tasks across multiple accounts and resources for protection. 

------
#### [ AWS Network Firewall ]

 [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) provides a stateful, managed network firewall and intrusion detection and prevention service with your VPC. 

------
#### [ AWS Shield ]

 [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) provides protections against DDoS attacks for AWS resources at the network, transport, and application layers. 

------
#### [ AWS WAF ]

 [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) provides a web application firewall so you can monitor the HTTP(S) requests that are forwarded to your protected web application resources. 

------

##### Understand AWS detection and response services
<a name="detection-and-response-2"></a>

AWS provides tools to help you streamline security operations across your AWS environment, including [multi-account environments](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html). For example, you can use [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) for intelligent threat detection, and you can use [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) to identify and analyze security findings by collecting log data. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) supports multiple security standards and provides an overview of security alerts and compliance status across AWS accounts. [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) tracks user activity and application programming interface (API) usage, which is crucial for understanding and responding to security events. 

The following table summarizes the detection and response offerings discussed in this guide: 

------
#### [ AWS Config ]

 [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account. 

------
#### [ AWS CloudTrail ]

 [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) records actions taken by a user, role, or AWS service. 

------
#### [ AWS Security Hub CSPM ]

 [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. 

------
#### [ Amazon GuardDuty ]

 [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) continuously monitors your AWS accounts, workloads, runtime activity, and data for malicious activity.

------
#### [ Amazon Inspector ]

 [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) scans your AWS workloads for software vulnerabilities and unintended network exposure. 

------
#### [ Amazon Security Lake ]

 [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) automatically centralizes security data from AWS environments, SaaS providers, on-premises environments, cloud sources, and third-party sources into a data lake. 

------
#### [ Amazon Detective ]

 [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) helps you analyze, investigate, and quickly identify the root cause of security findings or suspicious activities. 

------
#### [ AWS Security Incident Response ]

 [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) 

Helps you quickly prepare for, respond to, and receive guidance to help recover from security incidents. 

------

##### Understand AWS governance and compliance services
<a name="governance-and-compliance-2"></a>

AWS provides tools that help you adhere to your security, operational, compliance, and cost standards. For example, you can use [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to set up and govern a multi-account environment with prescriptive controls. With [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), you can set up policy-based management for multiple accounts within your organization. 

AWS also gives you a comprehensive view of your compliance status and continuously monitors your environment by using automated compliance checks based on the AWS best practices and industry standards that your organization follows. For example, [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides on-demand access to compliance reports, and [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) automates evidence collection so that you can more easily assess whether your controls are operating effectively. 

The following table summarizes the governance and compliance offerings discussed in this guide: 

------
#### [ AWS Organizations ]

 [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps you consolidate multiple AWS accounts into an organization that you create and centrally manage. 

------
#### [ AWS Control Tower ]

 [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment that's based on best practices. 

------
#### [ AWS Artifact ]

 [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides on-demand downloads of AWS security and compliance documents. 

------
#### [ AWS Audit Manager ]

 [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) 

Helps you continuously audit your AWS usage to simplify how you assess risk and compliance. 

------

### Consider AWS security, identity, and governance criteria
<a name="consider"></a>

Choosing the right security, identity, and governance services on AWS depends on your specific requirements and use cases. [Deciding to adopt an AWS security service](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-evaluating-security-service/introduction.html) provides a decision tree to help you decide if adopting AWS services for security, identity, and governance is suitable for your organization. In addition, here are some criteria to consider when making your decision about which services to use. 

------
#### [ Security requirements and threat landscape ]

Conduct a comprehensive assessment of your organization's **specific vulnerabilities and threats**. This involves identifying the types of data that you handle, such as personal customer information, financial records, or proprietary business data. Understand the potential risks associated with each. 

Assess your application and infrastructure **architecture**. Determine whether your applications are public-facing and what kind of web traffic they handle. This factors into your need for services such as AWS WAF to protect against web exploitation. For internal applications, consider the importance of internal threat detection and continuous monitoring with Amazon GuardDuty, which can identify unusual access patterns or unauthorized deployments. 

Finally, consider the sophistication of your **existing security posture** and the expertise of your security team. If your team has limited resources, choosing services that offer more automation and integration can provide you with effective security enhancements, without overwhelming your team. Example services include AWS Shield for DDoS protection and AWS Security Hub CSPM for centralized security monitoring. 

------
#### [ Compliance and regulatory requirements ]

Identify the **relevant laws and standards** for your industry or geographic region, such as [General Data Protection Regulation](https://aws.amazon.com/compliance/gdpr-center/) (GDPR), the [U.S. Health Insurance Portability and Accountability Act of 1996](https://aws.amazon.com/compliance/hipaa-compliance/) (HIPAA), or [Payment Card Industry Data Security Standard](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) (PCI DSS). 

AWS offers services such as AWS Config and AWS Artifact to help you manage compliance with various standards. With AWS Config, you can assess, audit, and evaluate the configurations of your AWS resources, making it easier for you to ensure compliance with internal policies and regulatory requirements. AWS Artifact provides on-demand access to AWS compliance documentation, aiding you with audits and compliance reporting. 

Choosing services that align with your specific compliance needs can help your organization meet legal requirements and build a secure and trustworthy environment for your data. Explore [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) to learn more. 

------
#### [ Scalability and flexibility ]

Consider how your organization will grow, and how fast. Choose AWS services that will help your security measures grow seamlessly with your infrastructure and adapt to evolving threats. 

To help you **scale quickly**, AWS Control Tower orchestrates the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations and AWS IAM Identity Center, to build a landing zone in less than an hour. Control Tower sets up and manages resources on your behalf. 

AWS also designs many services to **automatically scale** with an application's traffic and usage patterns, such as Amazon GuardDuty for threat detection and AWS WAF for protecting web applications. As your business scales up, these services scale with it, without requiring manual adjustments or causing bottlenecks. 

In addition, it's critical that you can **customize your security controls** to match your business requirements and threat landscapes. Consider managing your accounts with AWS Organizations, so you can manage [40\+ services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)' resources across multiple accounts. This gives individual application teams the flexibility and visibility to manage security needs that are specific to their workload, while also giving them governance and visibility to centralized security teams. 

Considering scalability and flexibility helps you ensure that your security posture is robust, responsive, and capable of supporting dynamic business environments. 

------
#### [ Integration with existing systems ]

Consider security measures that enhance, rather than disrupt, your current operations. For example, consider the following: 
+ Streamline your workflows by **aggregating** security data and alerts from AWS services and analyzing them alongside existing security information and event management (SIEM) systems. 
+ Create a **unified view** of security threats and vulnerabilities across both AWS and on-premises environments. 
+ Integrate AWS CloudTrail with existing log management solutions for **comprehensive monitoring** of user activities and API usage across your AWS infrastructure and existing applications. 
+ Examine ways that you can optimize **resource utilization** and consistently apply security policies across environments. This helps you reduce the risk of gaps in security coverage. 

------
#### [ Cost and budget considerations ]

Review the [pricing models](https://aws.amazon.com/pricing) for each service that you're considering. AWS often charges based on usage, such as the number of API calls, the volume of data processed, or the amount of data stored. For example, Amazon GuardDuty charges based on the amount of log data analyzed for threat detection, while AWS WAF bills are based on the number of rules deployed and the number of web requests received. 

Estimate your expected usage to **forecast costs** accurately. Consider both current needs and potential growth or spikes in demand. For example, scalability is a key feature of AWS services, but it can also lead to increased costs if not managed carefully. Use the [AWS Pricing Calculator](https://calculator.aws/) to model different scenarios and assess their financial impact. 

Evaluate the **total cost of ownership** (TCO), which includes both direct costs and indirect costs, such as the time and resources needed for management and maintenance. Opting for managed services can reduce operational overhead, but it might come at a higher price point. 

Lastly, **prioritize** your security investments based on risk assessment. Not all security services will be equally critical to your infrastructure, so focus your budget on the areas that will have the most significant impact on reducing risk and ensuring compliance. Balancing cost-effectiveness with the level of security that you need is key to a successful AWS security strategy. 

------
#### [ Organizational structure and access needs ]

Evaluate how your organization is structured and operates, and how your access needs might vary by team, project, or location. This factors in to how you manage and authenticate user identities, assign roles, and enforce access controls across your AWS environment. Implement [best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), such as the applying least-privilege permissions and requiring multi-factor authentication (MFA). 

Most organizations need a **multi-account** environment. Review [best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) for this type of environment, and consider using AWS Organizations and AWS Control Tower to help you implement it. 

Another aspect that you should consider is the management of **credentials and access keys**. Consider using IAM Identity Center for centralizing access management across multiple AWS accounts and business applications, which enhances both security and user convenience. To help you smoothly manage access across your organization's accounts, IAM Identity Center [integrates](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-sso.html) with AWS Organizations. 

Additionally, evaluate how these identity and access management services **integrate** with your existing directory services. If you have an existing identity provider, you can integrate it with IAM Identity Center by using [SAML 2.0](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html) or [OpenID Connect](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html) (OIDC). IAM Identity Center also has support for [System for Cross-domain Identity Management](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html) (SCIM) provisioning to help keep your directories synchronized. This helps you ensure a seamless and secure user experience while accessing AWS resources. 

 

------

### Choose an AWS security, identity, and governance service
<a name="choose"></a>

Now that you know the criteria for evaluating your security options, you're ready to choose which AWS security services might be a good fit for your organizational requirements. 

The following table highlights which services are optimized for which circumstances. Use the table to help determine the service that is the best fit for your organization and use case. 

**Note**  
1 Integrates with AWS Security Hub CSPM ([full list](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html))  
2 Integrates with Amazon GuardDuty ([full list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_integrations.html))  
3 Integrates with Amazon Security Lake ([full list](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-integrations.html))

#### Choose AWS identity and access management services
<a name="identity-and-access-management"></a>

Grant appropriate individuals the appropriate level of access to systems, applications, and data. 



- **Use these services to help you securely manage and govern access for your customers, workforce, and workloads. **
  - ****What is it optimized for?**:** Helps you connect your source of identities, or create users. You can centrally manage workforce access to multiple AWS accounts and applications. / ****Security, identity, and governance services**:** [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) 
  - ****What is it optimized for?**:** Optimized for authenticating and authorizing users for web and mobile applications.  / ****Security, identity, and governance services**:** [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) 
  - ****What is it optimized for?**:** Optimized for securely sharing resources within AWS.  / ****Security, identity, and governance services**:** [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) 
  - ****What is it optimized for?**:** Enables secure, fine-grained control over access to AWS workload resources.  / ****Security, identity, and governance services**:** [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) 1



#### Choose AWS data protection services
<a name="data-protection"></a>

Automate and simplify data protection and security tasks that range from key management and sensitive data discovery to credential management. 



- **Use these services to help you achieve and maintain the confidentiality, integrity, and availability of sensitive data stored and processed within AWS environments. **
  - ****What is it optimized for?**:** Optimized for discovering sensitive data.  / ****Data protection services**:** [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) 1
  - ****What is it optimized for?**:** Optimized for cryptographic keys.  / ****Data protection services**:** [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
  - ****What is it optimized for?**:** Optimized for HSMs.  / ****Data protection services**:** [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) 
  - ****What is it optimized for?**:** Optimized for private SSL/TLS X.509 certificates and keys.  / ****Data protection services**:** [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) 
  - ****What is it optimized for?**:** Optimized for creating private certificate authority hierarchies.  / ****Data protection services**:** [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) 
  - ****What is it optimized for?**:** Optimized for database credentials, application credentials, OAuth tokens, API keys, and other secrets.  / ****Data protection services**:** [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 
  - ****What is it optimized for?**:** Optimized for providing access to cryptographic functions and key management used in payment processing in accordance with PCI standards.  / ****Data protection services**:** [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html) 



#### Choose AWS network and application protection services
<a name="network-and-application-protection"></a>

Centrally protect your internet resources against common DDoS and application attacks. 



- **Use these services to help you enforce detailed security policies at every network control point. **
  - ****What is it optimized for?**:** Optimized for centrally configuring and managing firewall rules.  / ****Network and application protection services**:** [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) 1
  - ****What is it optimized for?**:** Optimized for providing a stateful, managed network firewall and intrusion detection and prevention service.  / ****Network and application protection services**:** [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) 
  - ****What is it optimized for?**:** Optimized for protecting against DDoS attacks for AWS resources at the network, transport, and application layers.  / ****Network and application protection services**:** [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) 
  - ****What is it optimized for?**:** Optimized for providing a web application firewall.  / ****Network and application protection services**:** [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) 



#### Choose AWS detection and response services
<a name="detection-and-response"></a>

Continuously identify and prioritize security risks, while integrating security best practices early. 



- **Use these services to help you detect and respond to security risks [across your accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html), so you can protect your workloads at scale. **
  - ****What is it optimized for?**:** Optimized for automating security checks and centralizing security alerts with AWS and third-party integrations.  / ****Detection and response services**:** [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 2, 3
  - ****What is it optimized for?**:** Optimized for assessing, auditing, and evaluating the configuration of your resources.  / ****Detection and response services**:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 1 
  - ****What is it optimized for?**:** Optimized for logging events from other AWS services as an audit trail.  / ****Detection and response services**:** [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
  - ****What is it optimized for?**:** Optimized for intelligent threat detection and detailed reporting.  / ****Detection and response services**:** [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) 1
  - ****What is it optimized for?**:** Optimized for vulnerability management.  / ****Detection and response services**:** [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) 1
  - ****What is it optimized for?**:** Optimized for centralizing security data.  / ****Detection and response services**:** [ Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) 1
  - ****What is it optimized for?**:** Optimized for aggregating and summarizing potential security issues.  / ****Detection and response services**:** [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) 1, 2, 3
  - ****What is it optimized for?**:** Optimized for helping you triage findings, escalate security events, and manage cases that require your immediate attention.  / ****Detection and response services**:** [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html) 



#### Choose AWS governance and compliance services
<a name="governance-and-compliance"></a>

Establish cloud governance across your resources, and automate your compliance and auditing processes. 



- **Use these services to help you implement best practices and meet industry standards when using AWS. **
  - ****What is it optimized for?**:** Optimized for centrally managing multiple accounts and consolidated billing.  / ****Governance and compliance services**:** [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) 
  - ****What is it optimized for?**:** Optimized for providing on-demand downloads of AWS security and compliance documents.  / ****Governance and compliance services**:** [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) 
  - ****What is it optimized for?**:** Optimized for auditing AWS usage.  / ****Governance and compliance services**:** [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) 1
  - ****What is it optimized for?**:** Optimized for setting up and governing an AWS multi-account environment.  / ****Governance and compliance services**:** [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) 



 

### Use AWS security, identity, and governance services
<a name="use"></a>

You should now have a clear understanding of what each AWS security, identity, and governance service (and the supporting AWS tools and services) does, and which ones might be right for you. 

To explore how to use and learn more about each of the available AWS security, identity, and governance services, we have provided a pathway to explore how each of the services works. The following sections provide links to in-depth documentation, hands-on tutorials, and resources to get you started. 

#### Use AWS identity and access management services
<a name="identity-and-access-management-1"></a>

The following tables show some useful identity and access management resources, organized by service, to help you get started. 

------
#### [ AWS IAM Identity Center ]
+  **Enabling AWS IAM Identity Center** 

  Enable IAM Identity Center and begin using it with your AWS Organizations. 

   [Explore the guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) 
+  **Configure user access with the default IAM Identity Center directory** 

  Use the default directory as your identity source and set up and test user access. 

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html) 
+  **Using Active Directory as an identity source** 

  Complete the basic setup for using Active Directory as an IAM Identity Center identity source. 

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-ad.html) 
+  **Configure SAML and SCIM with Okta and IAM Identity Center** 

  Set up a SAML connection with Okta and IAM Identity Center. 

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-okta.html) 

------
#### [ Amazon Cognito ]
+  **Getting started with Amazon Cognito** 

  Learn about the most common Amazon Cognito tasks. 

   [Explore the guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-getting-started.html) 
+  **Tutorial: Creating a user pool** 

  Create a user pool, which allows your users to sign in to your web or mobile app. 

   [Get started with the tutorial](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool.html) 
+  **Tutorial: Creating an identity pool** 

  Create an identity pool, which allows your users to obtain temporary AWS credentials to access AWS services. 

   [Get started with the tutorial](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) 
+  **Amazon Cognito workshop** 

  Practice using Amazon Cognito to build an authentication solution for a hypothetical pet store. 

   [Get started with the tutorial](https://www.cognitobuilders.training/) 

------
#### [ AWS RAM ]
+  **Getting started with AWS RAM** 

  Learn about AWS RAM terms and concepts. 

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/getting-started.html) 
+  **Working with shared AWS resources** 

  Share AWS resources that you own, and access AWS resources that are shared with you. 

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/working-with.html) 
+  **Managing permissions in AWS RAM** 

  Learn about the two types of managed permissions: AWS managed permissions and customer managed permissions. 

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/security-ram-permissions.html) 
+  **Configure detailed access to your resources that are shared using AWS RAM** 

  Use customer managed permissions to customize your resource access and achieve the best practice of least privilege. 

   [Read the blog](https://aws.amazon.com/blogs/security/configure-fine-grained-access-to-your-resources-shared-using-aws-resource-access-manager/) 

------
#### [ IAM ]
+  **Getting started with IAM** 

  Create IAM roles, users, and policies using the AWS Management Console. 

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html) 
+  **Delegate access across AWS accounts using roles** 

  Use a role to delegate access to resources in different AWS accounts that you own called **Production** and **Development**. 

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) 
+  **Create a customer managed policy** 

  Use the AWS Management Console to create a [customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) and then attach that policy to an IAM user in your AWS account. 

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html) 
+  **Define permissions to access AWS resources based on tags** 

  Create and test a policy that allows IAM roles with principal tags to access resources with matching tags. 

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) 
+  **Security best practices in IAM** 

  Help secure your AWS resources by using IAM best practices. 

   [Explore the guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 

------

#### Use AWS data protection services
<a name="data-protection-1"></a>

The following section provides you with links to detailed resources that describe AWS data protection. 

------
#### [ Macie ]
+  **Getting started with Amazon Macie** 

  Enable Macie for your AWS account, assess your Amazon S3 security posture, and configure key settings and resources for discovering and reporting sensitive data in your S3 buckets. 

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/getting-started.html) 
+  **Monitoring data security and privacy with Amazon Macie** 

  Use Amazon Macie to monitor Amazon S3 data security and assess your security posture. 

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3.html) 
+  **Analyzing Amazon Macie findings** 

  Review, analyze, and manage Amazon Macie findings. 

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/findings.html) 
+  **Retrieving sensitive data samples with Amazon Macie findings** 

  Use Amazon Macie to retrieve and reveal samples of sensitive data that are reported by individual findings. 

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd.html) 
+  **Discovering sensitive data with Amazon Macie** 

  Automate the discovery, logging, and reporting of sensitive data in your Amazon S3 data estate. 

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) 

------
#### [ AWS KMS ]
+  **Getting started with AWS KMS** 

  Manage symmetric encryption KMS keys, from creation to deletion. 

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) 
+  **Special-purpose keys** 

  Learn about the different types of keys that AWS KMS supports, in addition to symmetric encryption KMS keys. 

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/key-types.html) 
+  **Scaling your encryption at rest capabilities with AWS KMS** 

  Learn about the encryption at rest options available within AWS. 

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/05f16f1a-0bbf-45a7-a304-4fcd7fca3d1f/en-US) 

------
#### [ AWS CloudHSM ]
+  **Getting started with AWS CloudHSM** 

  Create, initialize, and activate an AWS CloudHSM cluster. 

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) 
+  **Managing AWS CloudHSM clusters** 

  Connect to your AWS CloudHSM cluster and the various administrative tasks in managing your cluster. 

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-clusters.html) 
+  **Managing HSM users and keys in AWS CloudHSM** 

  Create users and keys on the HSMs in your cluster. 

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-and-keys.html) 
+  **Automate the deployment of an NGINX web service using Amazon ECS with TLS offload in CloudHSM** 

  Use AWS CloudHSM to store your private keys for your websites that are hosted in the cloud. 

   [Read the blog](https://aws.amazon.com/blogs/security/automate-the-deployment-of-an-nginx-web-service-using-amazon-ecs-with-tls-offload-in-cloudhsm/) 

------
#### [ AWS Certificate Manager ]
+  **Requesting a public certificate** 

  Use the AWS Certificate Manager (ACM) console or AWS CLI to request a public ACM certificate. 

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) 
+  **Best practices for AWS Certificate Manager** 

  Learn best practices based on real-world experience from current ACM customers. 

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html) 
+  **How to use AWS Certificate Manager to enforce certificate issuance controls** 

  Use IAM condition keys to ensure that your users are issuing or requesting TLS certificates in accordance with your organization's guidelines. 

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-use-aws-certificate-manager-to-enforce-certificate-issuance-controls/) 

------
#### [ AWS Private CA ]
+  **Planning your AWS Private CA deployment** 

  Prepare AWS Private CA for use before you create a private certificate authority. 

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html) 
+  **AWS Private CA administration** 

  Create an entirely AWS hosted hierarchy of root and subordinate certificate authorities for internal use by your organization. 

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/creating-managing.html) 
+  **Certificate administration** 

  Perform basic certificate administration tasks with AWS Private CA, such as issuing, retrieving, and listing private certificates. 

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaUsing.html) 
+  **AWS Private CA workshop** 

  Develop hands-on experience with various use cases of private certificate authorities. 

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/1d889b6d-52c9-49be-95a0-5e5e97c37f81/en-US) 
+  **How to simplify certificate provisioning in Active Directory with AWS Private CA** 

  Use AWS Private CA to more easily provision certificates for users and machines within your Microsoft Active Directory environment. 

   [Read the blog](https://aws.amazon.com/blogs/modernizing-with-aws/simplify-certificate-provisioning-in-ad-with-aws-private-ca/) 
+  **How to enforce DNS name constraints in AWS Private CA** 

   Apply DNS name constraints to a subordinate CA by using the AWS Private CA service. 

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-enforce-dns-name-constraints-in-aws-private-ca/) 

------
#### [ AWS Secrets Manager ]
+  **AWS Secrets Manager concepts** 

  Perform basic certificate administration tasks with AWS Private CA, such as issuing, retrieving, and listing private certificates. 

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html) 
+  **Set up alternating users rotation for AWS Secrets Manager** 

  Set up an alternating users rotation for a secret that contains database credentials. 

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-alternating.html) 
+  **Using AWS Secrets Manager secrets with Kubernetes** 

  Show secrets from Secrets Manager as files mounted in Amazon EKS pods by using the AWS Secrets and Configuration Provider (ASCP). 

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/manage-secrets.html) 

------
#### [ AWS Payment Cryptography ]
+  **Getting started with AWS Payment Cryptography** 

   Create keys and use them in various cryptographic operations. 

   [Explore the guide](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/getting-started.html) 
+  **AWS Payment Cryptography FAQs** 

  Understand the basics of AWS Payment Cryptography.

   [Explore the FAQs](https://aws.amazon.com/payment-cryptography/faqs/) 

------

#### Use AWS network and application protection services
<a name="network-and-application-protection-1"></a>

The following tables provide links to detailed resources that describe AWS network and application protection. 

------
#### [ AWS Firewall Manager ]
+  **Getting started with AWS Firewall Manager policies** 

  Use AWS Firewall Manager to activate different types of security policies. 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html) 
+  **How to continuously audit and limit security groups with AWS Firewall Manager** 

  Use AWS Firewall Manager to limit security groups, ensuring that only required ports are open. 

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-continuously-audit-and-limit-security-groups-with-aws-firewall-manager/) 
+ **Use AWS Firewall Manager to deploy protection at scale in AWS Organizations** 

  Use AWS Firewall Manager to deploy and manage security policies across your AWS Organizations. 

   [Read the blog](https://aws.amazon.com/blogs/security/use-aws-firewall-manager-to-deploy-protection-at-scale-in-aws-organizations/) 

------
#### [ AWS Network Firewall ]
+  **Getting started with AWS Network Firewall** 

  Configure and implement an AWS Network Firewall firewall for a VPC with a basic internet gateway architecture. 

   [Explore the guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html) 
+  **AWS Network Firewall Workshop** 

  Deploy an AWS Network Firewall by using infrastructure as code. 

   [Explore the workshop](https://catalog.workshops.aws/networkfirewall/en-US) 
+ **Hands-on walkthrough of the AWS Network Firewall flexible rules engine – Part 1** 

  Deploy a demonstration of AWS Network Firewall within your AWS account to interact with its rules engine. 

   [Read the blog](https://aws.amazon.com/blogs/security/hands-on-walkthrough-of-the-aws-network-firewall-flexible-rules-engine/) 
+ **Hands-on walkthrough of the AWS Network Firewall flexible rules engine – Part 2** 

  Create a firewall policy with a strict rule order and set one or more default actions. 

   [Read the blog](https://aws.amazon.com/blogs/security/hands-on-walkthrough-of-the-aws-network-firewall-flexible-rules-engine-part-2/) 
+  **Deployment models for AWS Network Firewall** 

  Learn deployment models for common use cases where you can add AWS Network Firewall to the traffic path. 

   [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/) 
+ **Deployment models for AWS Network Firewall with VPC routing enhancements** 

  Use enhanced VPC routing primitives to insert AWS Network Firewall between workloads in different subnets of the same VPC. 

   [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/) 

------
#### [ AWS Shield ]
+  **How AWS Shield works** 

  Learn how AWS Shield Standard and AWS Shield Advanced provide protections against DDoS attacks for AWS resources at the network and transport layers (layer 3 and 4) and the application layer (layer 7). 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html) 
+  **Getting started with AWS Shield Advanced** 

  Get started with AWS Shield Advanced by using the Shield Advanced console. 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html) 
+  **AWS Shield Advanced workshop** 

  Protect internet-exposed resources against DDoS attacks, monitor DDoS attacks against your infrastructure, and notify the appropriate teams. 

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6396761b-6d1f-4a4d-abf1-ffb69dee6995/en-US) 

------
#### [ AWS WAF ]
+  **Getting started with AWS WAF** 

  Set up AWS WAF, create a web ACL, and protect Amazon CloudFront by adding rules and rules groups to filter web requests. 

   [Get started with the tutorial](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html) 
+  **Analyzing AWS WAF Logs in Amazon CloudWatch Logs** 

  Set up native AWS WAF logging to Amazon CloudWatch logs and visualize and analyze the data in the logs. 

   [Read the blog](https://aws.amazon.com/blogs/mt/analyzing-aws-waf-logs-in-amazon-cloudwatch-logs/) 
+  **Visualize AWS WAF logs with an Amazon CloudWatch dashboard** 

  Use Amazon CloudWatch to monitor and analyze AWS WAF activity by using CloudWatch metrics, Contributor Insights, and Logs Insights. 

   [Read the blog](https://aws.amazon.com/blogs/security/visualize-aws-waf-logs-with-an-amazon-cloudwatch-dashboard/) 

------

#### Use AWS detection and response services
<a name="detection-and-response-1"></a>

The following tables provide links to detailed resources that describe AWS detection and response services. 

------
#### [ AWS Config ]
+  **Getting started with AWS Config** 

  Set up AWS Config and work with AWS SDKs. 

   [Explore the guide](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) 
+  **Risk and Compliance workshop** 

  Automate controls by using AWS Config and AWS Managed Config Rules. 

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dd2bea89-dc7a-4bda-966a-70b4ff6e90e0/en-US/3-detective-controls-config/1-config-setup) 
+ **AWS Config Rule Development Kit library: Build and operate rules at scale** 

  Use the Rule Development Kit (RDK) to build a custom AWS Config rule and deploy it with the RDKLib. 

   [Read the blog](https://aws.amazon.com/blogs/mt/aws-config-rule-development-kit-library-build-and-operate-rules-at-scale/) 

------
#### [ AWS CloudTrail ]
+  **View event history** 

  Review the AWS API activity in your AWS account for services that support CloudTrail. 

   [Get started with the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html) 
+  **Create a trail to log management events** 

  Create a trail to log management events in all Regions. 

   [Get started with the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html) 

------
#### [ AWS Security Hub CSPM ]
+  **Enabling AWS Security Hub CSPM** 

  Enable AWS Security Hub CSPM with AWS Organizations or in a standalone account. 

   [Explore the guide](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) 
+  **Cross-Region aggregation** 

  Aggregate AWS Security Hub CSPM findings from multiple AWS Regions to a single aggregation Region. 

   [Explore the guide](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) 
+  **AWS Security Hub CSPM workshop** 

  Learn how to use AWS Security Hub CSPM and to manage and improve the security posture of your AWS environments. 

   [Explore the workshop](https://catalog.workshops.aws/security-hub/en-US) 
+ **Three recurring Security Hub CSPM usage patterns and how to deploy them** 

  Learn about the three most common AWS Security Hub CSPM usage patterns and how to improve your strategy for identifying and managing findings. 

   [Read the blog](https://aws.amazon.com/blogs/security/three-recurring-security-hub-usage-patterns-and-how-to-deploy-them/) 

------
#### [ Amazon GuardDuty ]
+  **Getting started with Amazon GuardDuty** 

  Enable Amazon GuardDuty, generate sample findings, and set up alerts. 

   [Explore the tutorial](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html) 
+  **EKS protection in Amazon GuardDuty** 

  Use Amazon GuardDuty to monitor your Amazon Elastic Kubernetes Service (Amazon EKS) audit logs. 

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html) 
+  **Lambda protection in Amazon GuardDuty** 

  Identify potential security threats when you invoke an AWS Lambda function. 

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html) 
+  **GuardDuty Amazon RDS protection** 

  Use Amazon GuardDuty to analyze and profile Amazon Relational Database Service (Amazon RDS) login activity for potential access threats to your Amazon Aurora databases. 

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html) 
+  **Amazon S3 protection in Amazon GuardDuty** 

  Use GuardDuty to monitor CloudTrail data events and to identify potential security risks within your S3 buckets. 

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) 
+ **Threat detection and response with Amazon GuardDuty and Amazon Detective** 

   Learn the basics of Amazon GuardDuty and Amazon Detective. 

   [Explore the workshop](https://catalog.workshops.aws/guardduty/en-US) 

------
#### [ Amazon Inspector ]
+  **Getting started with Amazon Inspector** 

  Activate Amazon Inspector scans to understand findings in the console. 

   [Get started with the tutorial](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html) 
+  **Vulnerability management with Amazon Inspector** 

  Use Amazon Inspector to scan Amazon EC2 instances and container images in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities. 

   [Explore the workshop](https://catalog.workshops.aws/inspector/en-US) 
+  **How to scan EC2 AMIs by using Amazon Inspector** 

  Build a solution by using multiple AWS services to scan your AMIs for known vulnerabilities. 

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-scan-ec2-amis-using-amazon-inspector/) 

------
#### [ Amazon Security Lake ]
+  **Getting started with Amazon Security Lake** 

   Enable and start using Amazon Security Lake. 

   [Explore the guide](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html) 
+  **Managing multiple accounts with AWS Organizations** 

   Collect security logs and events from multiple AWS accounts. 

   [Explore the guide](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html) 
+ **Ingest, transform, and deliver events that are published by Amazon Security Lake to Amazon OpenSearch Service** 

  Ingest, transform, and deliver Amazon Security Lake data to Amazon OpenSearch Service for use by your SecOps teams. 

   [Read the blog](https://aws.amazon.com/blogs/big-data/ingest-transform-and-deliver-events-published-by-amazon-security-lake-to-amazon-opensearch-service/) 
+ **How to visualize Amazon Security Lake findings with Quick** 

   Query and visualize data from Amazon Security Lake by using Amazon Athena and Quick. 

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-visualize-amazon-security-lake-findings-with-amazon-quicksight/) 

------
#### [ Amazon Detective ]
+  **Amazon Detective terms and concepts** 

   Learn the key terms and concepts that are important for understanding Amazon Detective and how it works. 

   [Explore the guide](https://docs.aws.amazon.com/detective/latest/userguide/detective-terms-concepts.html) 
+  **Setting up Amazon Detective** 

   Enable Amazon Detective from the Amazon Detective console, Amazon Detective API, or AWS CLI. 

   [Explore the guide](https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html) 
+ **Threat detection and response with Amazon GuardDuty and Amazon Detective** 

   Learn the basics of Amazon GuardDuty and Amazon Detective. 

   [Explore the workshop](https://catalog.workshops.aws/guardduty/en-US) 

------

#### Use AWS governance and compliance services
<a name="governance-and-compliance-1"></a>

The following tables provide links to detailed resources that describe governance and compliance. 

------
#### [ AWS Organizations ]
+  **Creating and configuring an organization** 

  Create your organization and configure it with two AWS member accounts. 

   [Get started with the tutorial](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) 
+  **Services that work with AWS Organizations** 

   Understand which AWS services you can use with AWS Organizations and the benefits of using each service on an organization-wide level. 

   [Explore the guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html) 
+  **Organizing your AWS environment by using multiple accounts** 

  Implement best practices and current recommendations for organizing your overall AWS environment. 

   [Read the whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.pdf) 

------
#### [ AWS Artifact ]
+  **Getting started with AWS Artifact ** 

  Download security and compliance reports, manage legal agreements, and manage notifications. 

   [Explore the guide](https://docs.aws.amazon.com/artifact/latest/ug/getting-started.html) 
+  **Managing agreements in AWS Artifact** 

  Use the AWS Management Console to review, accept, and manage agreements for your account or organization. 

   [Explore the guide](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html) 
+ **Prepare for an Audit in AWS Part 1 – AWS Audit Manager, AWS Config, and AWS Artifact** 

  Use AWS services to help you automate the collection of evidence that's used in audits. 

   [Read the blog](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/) 

------
#### [ AWS Audit Manager ]
+  **Enabling AWS Audit Manager** 

   Enable Audit Manager by using the AWS Management Console, the Audit Manager API, or the AWS CLI. 

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html) 
+  **Tutorial for Audit Owners: Creating an assessment** 

   Create an assessment by using the Audit Manager Sample Framework. 

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-audit-owners.html) 
+  **Tutorial for Delegates: Reviewing a control set** 

   Review a control set that was shared with you by an audit owner in Audit Manager. 

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-delegates.html) 

------
#### [ AWS Control Tower ]
+  **Getting started with AWS Control Tower** 

  Set up and launch a multi-account environment, called a landing zone, that follows prescriptive best practices. 

   [Explore the guide](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) 
+ **Modernizing Account Management with Amazon Bedrock and AWS Control Tower** 

  Provision a security tooling account and leverage generative AI to expedite the AWS account setup and management process. 

   [Read the blog](https://aws.amazon.com/blogs/mt/modernizing-account-management-with-amazon-bedrock-and-aws-control-tower/) 
+ **Building a well-architected AWS GovCloud (US) environment with AWS Control Tower** 

  Set up your governance in the AWS GovCloud (US) Regions, including governing your AWS workloads by using Organizational Units (OUs) and AWS accounts. 

   [Read the blog](https://aws.amazon.com/blogs/mt/building-a-well-architected-aws-govcloud-us-environment-with-aws-control-tower/) 

------

### Explore AWS security, identity, and governance services
<a name="explore"></a>

------
#### [ Editable architecture diagrams ]

**Reference architecture diagrams** 

Explore reference architecture diagrams to help you develop your security, identity, and governance strategy. 

[Explore security, identity, and governance reference architectures](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all) 

------
#### [ Ready-to-use code ]



|  |  | 
| --- |--- |
| *Featured solution*<br />**Security Insights on AWS**<br />Deploy AWS-built code to help you visualize data in Amazon Security Lake to more rapidly investigate and respond to security events.<br />[Explore this solution](https://aws.amazon.com/solutions/implementations/security-insights-on-aws/) | **AWS Solutions**<br />Explore pre-configured, deployable solutions and their implementation guides, built by AWS.<br />[Explore all AWS security, identity, and governance solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all) | 

------
#### [ Documentation ]



|  |  | 
| --- |--- |
| **Security, identity, and governance whitepapers** <br />Explore whitepapers for further insights and best practices on choosing, implementing, and using the security, identity, and governance services that best fit your organization. <br /> [Explore security, identity, and governance whitepapers](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all)  | **AWS Security Blog** <br />Explore blog posts that address specific security use cases. <br /> [Explore the AWS Security blog](https://aws.amazon.com/blogs/security/)  | 

------

## Choosing an AWS identity service
<a name="identity-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Time to read** |  10 minutes  | 
| **Purpose** | Help determine which AWS identity service is the best fit for your organization. | 
| **Last updated** | August 15, 2025 | 

### Introduction
<a name="intro"></a>

 Identity and access management helps ensure that only authenticated and authorized users can access only the cloud resources that they need to perform their tasks, and that they can do it in a secure and compliant way.

![Diagram showing identity, authentication, and authorization.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/understand-identity-services.png)


As shown in the preceding diagram, identity is the unique identification of an entity, authentication is the process of verifying the identity, and authorization is the process of determining what the authenticated entity is allowed to do.

 AWS offers multiple services that help you manage access to your resources on AWS. These include the following: 


|  |  | 
| --- |--- |
| **Services covered** |  +  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.htm) <br />+  [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) <br />+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) <br />+  [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) <br />+  [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) <br />+  [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) <br />+  [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)   | 

 Though there are similarities between some identity services, these services address different scenarios. This decision guide helps you get started and choose the right AWS identity service for your use case. 

### Understand AWS identity and access management
<a name="understand"></a>

 Understanding the foundations of IAM can help you meet your needs. 

Principals, including human users, workloads, federated users, and assumed roles, access AWS services by using APIs. All AWS compute environments deliver credentials that applications use to sign their API calls and request access to AWS services. API requests are authenticated and authorized by a system of identities (such as IAM roles), actions (IAM policies), and resources that are defined in IAM. Every AWS customer configures these to use AWS APIs. IAM roles are identities with temporary and conditional permissions to perform scoped actions on AWS resources. IAM policies define the actions that IAM roles can perform on specific AWS resources.

By carefully crafting IAM policies, you can ensure that the permissions available to an IAM role allow access only to the resources needed to fulfill a task: a concept known as *least privilege*. 




### Consider criteria for choosing an AWS identity service
<a name="consider"></a>

 Choosing the right AWS services depends on your needs, and on the following considerations: 
+ **Who requires access** - you and your workforce, a machine and your workloads, or the applications you build.
+ **What they want to access** - AWS accounts; AWS applications and services, and the data in them; or data in the applications you build.
+ **Where they want to access it from** - from within AWS, from your on-premises environment, from another cloud environment, or from AWS IoT devices.

### Choose which AWS identity services to use
<a name="choose"></a>

The following table helps you find recommended AWS services for your use cases. For best results, consider the additional services and capabilities recommended for your objective. 



| I am a... | I want to... | AWS identity service | Additional services and capabilities to consider | 
| --- | --- | --- | --- | 
| Cloud/Identity administrator | Make it easier for my team to grant and audit access to AWS applications, such as Amazon Q and Amazon SageMaker AI. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) | [Trusted identity propagation in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)<br />[AWS Lake Formation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html)<br />[Amazon S3 Access Grants](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html) | 
| Cloud/Identity administrator | Make it easier for the owners of my organization's data to grant data access by workforce user or group. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) | [Trusted identity propagation in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)<br />[AWS Lake Formation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html)<br />[Amazon S3 Access Grants](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html) | 
| Cloud/Identity administrator<br />OR<br />Developer | Configure workforce access to AWS accounts and the resources in them, such as Amazon S3 buckets. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br />[Federation with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam) | [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)<br />[Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)<br />[Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) | 
| Cloud/Identity administrator | Run Active Directory dependent workloads in AWS. | [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), also known as AWS Managed Microsoft AD | [Integrations with AWS services and applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) | 
| Cloud/Identity administrator | Join my AWS workloads to my on-premises Microsoft Active Directory Domain Services. | [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), also known as AWS Managed Microsoft AD | [Integrations with AWS services and applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) | 
| Cloud/Identity administrator | Configure the access of my workloads to AWS resources. | [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) | [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) | 
| Cloud/Identity administrator | Establish a data perimeter to enforce my organization's security requirements. | [IAM permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) | [Data perimeters on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/) | 
| Cloud/Identity administrator | Verify which IAM roles and users within my organization have access to critical AWS resources. | [IAM Access Analyzer internal access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-internal-access-analysis) |  | 
| Cloud/Identity administrator | Analyze and refine permissions to drive towards least privilege. | [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) |  | 
| Cloud/Identity administrator | Grant on-premises workloads access to AWS. | [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)<br />(requires PKI, the ability to issue and manage certificates) |  | 
| Cloud/Identity administrator | Grant an IoT device access to AWS. | [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) |  | 
| Developer | Grant code in any external-to-AWS cloud environment access to AWS. | [AWS Security Token Service`AssumeRoleWithWebIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) | [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)<br />[AWS Security Token Service CLI V2 Reference](https://docs.aws.amazon.com/cli/latest/reference/sts/) | 
| Developer | Perform service-to-service authentication and authorization in my application running solely in AWS. | [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) with [AWS Signature Version 4 authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)<br />[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) | 
| Developer | Perform service-to-service authentication and authorization in my application with components in various cloud environments. | [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html) | [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) | 
| Developer | Enable your customers to access your AI application and manage the identities of AI agents. | [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) | [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) | 
| Developer | Build and manage IoT device software on AWS. | [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) |  | 
| Developer | Build an authentication mechanism into my own application. | [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) |  | 
| Developer | Build an authorization mechanism into an application. | [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) |  | 

### Use AWS identity services
<a name="use"></a>

#### For you and your workforce
<a name="for-your-workforce"></a>

##### IAM Identity Center
<a name="for-your-workforce-identity-center"></a>

IAM Identity Center helps you configure the single sign-on experience of your employees from your existing identity provider to user-facing AWS applications, such as Amazon Q and Amazon SageMaker AI, and to the AWS Management Console, including any AWS accounts that are assigned to your employees. With a single connection of your identity provider, you can scale your use of AWS applications as much as your business requires, and offer a continuous user experience across applications.

With IAM Identity Center, AWS applications such as Amazon Q can provide your users with personalized experiences, such as a dashboard showing what a user was working on when they last signed in. Data service owners, such as an Amazon Redshift administrator, can define permissions and audit access to data in AWS by the users in your directory. AWS data and analytics services can recognize your employees by their directory identities. For more information, see [Application access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html) in the AWS IAM Identity Center User Guide. 

An [*organization instance*](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html) of IAM Identity Center can help you manage your workforce access to AWS accounts as well. It lets you assign permissions to users and provision the permissions to multiple accounts from a central place. For more information, see [AWS account access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html) in the AWS IAM Identity Center User Guide.

##### Federation with IAM
<a name="federation-with-iam"></a>

You can also use IAM to federate workforce users through your identity provider to specific AWS accounts. Users assume IAM roles to perform scoped actions on the AWS resources in the account. You can federate with an identity provider that provides identity information using either OpenID Connect (OIDC) or SAML 2.0. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html).

#### For your workloads
<a name="for-your-workloads"></a>

##### IAM
<a name="for-your-workloads-iam"></a>

IAM lets your workload assume IAM roles with temporary security credentials to use AWS APIs and perform scoped actions on AWS resources. For example, they let workloads run code on compute services such as Amazon EC2 or Lambda. For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the IAM User Guide.

##### IAM Access Analyzer
<a name="for-your-workloads-access-analyzer"></a>

IAM Access Analyzer guides you to least privilege by providing features to set, verify, and refine permissions. It helps you implement your access management strategy by analyzing external, internal, and unused access, and validating that your IAM policies match your specified security standards. Use IAM Access Analyzer to do the following:
+ [Generate least-privilege policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) based on access activity
+ [Validate that your policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html) match IAM best practices and your security standards 
+ Verify who can access what and [detect unintended public and cross-account access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-external)
+ [Verify internal access to critical resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-internal) by identifying which IAM roles and users within your AWS organization have access to critical resources such as Amazon S3 buckets, Amazon DynamoDB tables, and Amazon RDS snapshots.
+ Refine permissions by [identifying unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-unused) in your IAM policies

The following image shows the IAM Access Analyzer dashboard with external and internal access findings.

![Dashboard showing external and internal access findings in IAM Access Analyzer](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/analyzer-findings-01.png)


The following image shows unused access findings in the IAM Access Analyzer dashboard.

![Dashboard showing unused access findings analysis with 100 active findings, including 40 unused roles, 15 unused credentials, and 45 unused permissions.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/unused-access-analyzer-dashboard.png)


##### IAM Roles Anywhere
<a name="for-your-workloads-iam-roles-anywhere"></a>

IAM Roles Anywhere extends the capabilities of IAM to on-premises and hybrid cloud workloads. Use it to get temporary security credentials and to use the same IAM policies and IAM roles that you use for AWS workloads.

##### AWS Directory Service
<a name="for-your-workloads-ad"></a>

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, is a highly available, fully managed Microsoft Active Directory (AD) service. It extends your on-premises Microsoft AD configurations to AWS so that your Microsoft Windows on-premises workloads can communicate with your AWS resources. Using AWS Managed Microsoft AD, you can join to your domain AWS resources such as Amazon EC2 instances, Amazon WorkSpaces managed desktops, and Amazon RDS for Microsoft SQL Server.

#### For the applications you build
<a name="for-your-applications"></a>

##### Amazon Cognito
<a name="for-your-applications-cognito"></a>

Amazon Cognito helps your developers implement customer identity and access management (CIAM) in the web and mobile applications that they develop. It is a scalable service they can use in your applications to manage users, authenticate, and authorize their access. In addition to CIAM, Amazon Cognito supports service-to-service authentication and authorization within your applications. It scales to millions of users across devices, and processes more than 100 billion authentications per month. 

##### Verified Permissions
<a name="for-your-applications-verified-permissions"></a>

Verified Permissions is a fully managed authorization service, which uses the easy-to-understand [Cedar policy language](https://www.cedarpolicy.com/en) for fine-grained permissions. Authorization decisions are verified formally by using automated reasoning. With Verified Permissions, developers can externalize authorization, align it with [Zero Trust principles](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html), and centralize policy management. Security and audit teams can better analyze and audit who has access to what within your applications.

The following image shows an example of permissions policy details from Verified Permissions and to whom the policy grants access.

![An AWS policy configuration showing a permission that allows SalesTeam members to maintain customer account data.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/customer-data-policy.png)


### Explore other AWS services
<a name="explore"></a>

This section suggests additional services you should consider.
+ [AWS Control Tower](https://aws.amazon.com/controltower) - Lets you set up a well-architected, multi-account AWS environment based on security and compliance best practices, and to manage it at scale.
+ [AWS Resource Access Manager](https://aws.amazon.com/ram) - Helps you share your resources across AWS accounts.
+ [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice) - Lets you connect, secure, and monitor services and resources for your application.
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway) - Lets you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs.
+ [AWS IoT Device Management](https://aws.amazon.com/iot-device-management) - Lets you onboard, organize, and manage Internet of Things (IoT) devices.
+ [AWS IoT Greengrass](https://aws.amazon.com/greengrass) - Lets you build, deploy, and manage IoT device software.

### Additional resources
<a name="resources"></a>

 User guides with specific deployment guidance for AWS identity services:
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.htm)
  + [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
  + [IAM federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam)
  + [AWS STS API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
  + [Policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)
  + [Policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html)
  + [Unused permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-unused)
  + [External access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-external)
  + [Internal access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-internal)
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
+ [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
+ [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)

 AWS Security Blog posts with use case specific guidance:
+ [How to use AWS managed applications with IAM Identity Center (Amazon Q)](https://aws.amazon.com/blogs/security/how-to-use-aws-managed-applications-with-iam-identity-center/)
+ [Cloud infrastructure entitlement management in AWS](https://aws.amazon.com/blogs/security/cloud-infrastructure-entitlement-management-in-aws/)
+ [Customize the scope of IAM Access Analyzer unused access analysis](https://aws.amazon.com/blogs/security/customize-the-scope-of-iam-access-analyzer-unused-access-analysis/)
+ [Use IAM roles to connect GitHub actions to actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)
+ [Planning for your IAM Roles Anywhere deployment](https://aws.amazon.com/blogs/security/planning-for-your-iam-roles-anywhere-deployment/)
+ [How to monitor, optimize, and secure Amazon Cognito machine-to-machine authorization](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/)
+ [How to support OpenID AuthZEN requests with Amazon Verified Permissions](https://aws.amazon.com/blogs/security/how-to-support-openid-authzen-requests-with-amazon-verified-permissions/)
+ [Approaches for authenticating external applications in a machine-to-machine scenario](https://aws.amazon.com/blogs/security/approaches-for-authenticating-external-applications-in-a-machine-to-machine-scenario/)
+ [Blog Post Series: Establishing a Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/)
+ [Verify internal access to critical AWS resources with new IAM Access Analyzer capabilities](https://aws.amazon.com/blogs/aws/verify-internal-access-to-critical-aws-resources-with-new-iam-access-analyzer-capabilities/)

## Choosing an AWS cryptography service
<a name="guide"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS cryptography services are the best fit for your organization. | 
| **Last updated** | January 31, 2025 | 
| **Covered services** |  + [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) <br />+ [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) <br />+ [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html) <br />+ [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) <br />+ [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) <br />+ [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) <br />+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)   | 
| **Related guides** | [ Choosing AWS security, identity, and governance services](https://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html) | 

### Introduction
<a name="introduction"></a>

 Cryptography is a cornerstone of security in cloud computing, helping to ensure data confidentiality, integrity, and authenticity. In a cloud environment, sensitive data may traverse public networks and reside on shared infrastructure, making robust cryptographic measures essential for protecting against unauthorized access or tampering. 

 AWS offers a comprehensive range of cryptographic services to secure data, manage encryption keys, and protect sensitive information. These include AWS Key Management Service (KMS) for centralized key management, AWS CloudHSM for PKCS11 applications and dedicated hardware security modules, and the AWS Encryption SDK for client-side encryption. AWS Secrets Manager is a service that enables you to securely store, manage, and retrieve sensitive information such as database credentials, API keys, and other secrets throughout their lifecycle. AWS Certificate Manager (ACM) simplifies the process of provisioning, managing, and deploying publicly trusted transport layer security (TLS) certificates for use with AWS services. The AWS Private Certificate Authority (PCA) enables you to generate and distribute x509 certificates for your internal resources. 

 The guide is designed to help you choose the AWS cryptography services and tools that are the best fit for your needs and your organization. 

[![AWS Videos](https://img.youtube.com/vi/1vqaZBgPOiE?si=SoAZe1zQCWUlqF0K&start=475&end=535/0.jpg)](https://www.youtube.com/watch?v=1vqaZBgPOiE?si=SoAZe1zQCWUlqF0K&start=475&end=535)


### Understand
<a name="understand"></a>

![A diagram showing the suite of AWS services that enable data protection on AWS.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/data-protection-on-aws-jan-2024.png)


 Choosing the right AWS cryptography services depends on your specific use case, data security requirements, compliance obligations, and operational preferences as outlined in the following tables. 

------
#### [ Key management  ]

 If you need to securely manage encryption keys, consider AWS Key Management Service (KMS). It allows you to create, rotate, and manage cryptographic keys integrated with other AWS services. KMS uses FIPS-validated HSMs to help you meet compliance rewuirements and to provide assurance on the correctness of the implementation of the cryptographic primitives exposed by KMS. Some applications require certain cryptographic functions or application interfaces that are only available with a traditional HSM and AWS CloudHSM provides dedicated hardware security modules (HSMs) in the cloud which gives you full control over your cryptographic keys and operations. 

------
#### [ Data encryption  ]

 For encrypting sensitive data such as customer details or intellectual property, AWS KMS is tightly integrated with AWS storage, database, and messaging services (e.g. S3, RDS, or EBS). If you require client-side encryption, the AWS Encryption SDK is an open-source library that makes it easy to encrypt data within your application before sending it to the cloud. 

------
#### [ Secure communications  ]

 To protect data in transit, AWS Certificate Manager (ACM) simplifies the management of publicly trusted TLS certificates. Use it for asserting the identity of your internet-facing applications and facilitating encrypting communications between your application, users, and cloud services without worrying about certificate renewals. For internal applications, you can use AWS Private Certificate Authority (PCA) for generating and distributing x509 certificates for your internal resources, including both clients and servers. 

------
#### [ Secrets and credentials management  ]

 For securely storing and retrieving application secrets such as database credentials, API keys, or certificates, consider AWS Secrets Manager. It provides automated secret rotation and fine-grained access controls. Alternatively, AWS Systems Manager Parameter Store is a lower-cost option for managing non-sensitive configurations and can integrate with AWS Secrets Manager. 

------
#### [ Compliance and auditing  ]

 For regulatory compliance work, consider AWS KMS and AWS CloudHSM to help ensure encryption standards are met. AWS Artifact is a self-service portal that provides on-demand access to AWS's security and compliance reports, such as ISO certifications and SOC reports, as well as the ability to review and accept agreements such as the Business Associate Addendum (BAA). You can also use services like AWS Config, AWS Security Hub CSPM, and AWS Audit Manager to monitor compliance and produce the appropriate artifacts for your own use or for consumption by your stakeholders. 

------

 When choosing between AWS cryptography services, consider the following requirements. 


|  Requirement  |  Service  | 
| --- | --- | 
|  Low effort, fully managed  |  AWS KMS or AWS Secrets Manager  | 
|  Require specific application interfaces or cryptographic algorithms not supported by KMS  |  AWS CloudHSM  | 
|  Encrypting/decrypting data in your applications  |  AWS Encryption SDK  | 
|  Simplified public TLS Certificate Management  |  AWS Certificate Manager  | 
|  Secrets management  |  AWS Secrets Manager  | 

 By aligning your requirements with these options, you can implement cryptographic solutions tailored to your security and operational needs. 

### Consider
<a name="consider"></a>

 Choosing the right AWS cryptography service involves understanding your specific security, operational, and compliance needs. AWS offers a variety of cryptographic services, each designed to address different use cases, from key management to data encryption and secure communication. To make an informed decision, you should evaluate your requirements based on several critical criteria, including your use case, control and flexibility needs, compliance obligations, cost considerations, and integration with AWS services. These criteria will help you align your choice with your organization’s security goals and operational workflows. 

------
#### [ Use case  ]

 Consider what you need the cryptographic service for: data encryption, key management, secure communication, or secrets management. For example, AWS KMS is ideal for encryption integrated into AWS services, while AWS CloudHSM suits organizations who need certain cryptographic capabilities, application interfaces, or a single-tenant HSM, often due to stringent compliance or specific application needs. Clarifying the purpose ensures you select a service suitable for for your requirements, optimizing both functionality and cost. 

------
#### [ Control and flexibility  ]

 Evaluate the level of control you need over your cryptographic operations. Managed services like AWS KMS provide ease of use with minimal management overhead with a multi-tenant HSM while maintaining full control over your key material. In contrast, AWS CloudHSM offers a single-tenant model for specific application, cryptographic, or compliance needs. 

------
#### [ Compliance requirements  ]

 If you operate in a regulated industry, ensure the service aligns with standards like GDPR, PCI DSS, or HIPAA. AWS KMS and AWS CloudHSM are both FIPS 140-2 Level 3 certified. Selecting a service that meets your non-functional requirements helps maintain trust and may avoid potential legal or financial penalties. 

------
#### [ Cost considerations  ]

 Assess your budget against the service’s pricing model. AWS KMS is cost-effective for general encryption needs, while AWS CloudHSM incurs higher costs due to dedicated hardware. Understanding cost implications helps you optimize your security expenditure. 

------
#### [ Integration with AWS ecosystem  ]

 If you heavily use AWS services, prioritize a cryptography solution like AWS KMS or ACM that integrates seamlessly with S3, RDS, or Lambda. This ensures smoother workflows and reduces development effort. Integration capabilities can significantly enhance operational efficiency. 

------

### Choose
<a name="choose"></a>

 Choosing the right AWS cryptography service involves understanding your specific security, operational, and compliance needs. AWS offers a variety of cryptographic services, each designed to address different use cases, from key management to data encryption and secure communication. To make an informed decision, you should evaluate your requirements based on several critical criteria, including your use case, control and flexibility needs, compliance obligations, cost considerations, and integration with AWS services. These criteria will help you align your choice with your organization’s security goals and operational workflows. 


|  Target use case  |  When would you use it?  |  Recommended service  | 
| --- | --- | --- | 
|  Key management  |  To securely create, rotate, and manage cryptographic keys integrated with other AWS services  |  [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)  | 
|  Key management  |  For specific application integrations or cryptographic primitives  |  [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)  | 
|  Data encryption  |  To implement client-side encryption to protect sensitive data such as customer details or intellectual property.  |  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) <br /> [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html)  | 
|  Secure communications  |  To protect data in transit and simplify the management of SSL/TLS certificates.  |  [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) <br /> [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)  | 
|  Secrets and credential management  |  To securely store and retrieve application secrets like database credentials, API keys, or certificates.  |  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) <br /> [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)  | 

### Use
<a name="use"></a>

 You should now have a clear understanding of what each AWS cryptography service does, and which ones might be right for you. 

 To explore how to use and learn more about each of the available AWS cryptography services, we have provided a pathway to explore how each of them works. The following sections provide links to in-depth documentation, hands-on tutorials, and other resources to get you started. 

------
#### [ AWS Certificate Manager  ]
+  **Get started with AWS Certificate Manager **

   Start using AWS Certificate Manager, including working with both public and private certificates. 

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/setup.html) 
+  **Best practices for AWS Certificate Manager **

   Review recommendations that can help you use AWS Certificate Manager more effectively. 

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html) 
+  **AWS Certificate Manager FAQ **

   Review the AWS Certificate Manager (ACM) FAQ page for detailed answers to common questions about ACM's features, capabilities, and usage. It covers topics such as the types of certificates ACM manages, integration with other AWS services, and guidance on provisioning and managing SSL/TLS certificates. 

   [Explore the FAQs](https://aws.amazon.com/certificate-manager/faqs/) 

------
#### [ AWS CloudHSM  ]
+  **Get started with AWS CloudHSM **

   Learn how to create, initialize, and activate a cluster in AWS CloudHSM. After you complete these procedures, you'll be ready to manage users, manage clusters, and use the included software libraries to perform cryptographic operations. 

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html) 
+  **Best practices for AWS CloudHSM **

   Explore best practices for managing and monitoring your AWS CloudHSM cluster. 

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/best-practices.html) 
+  **AWS CloudHSM pricing **

   Review the pricing page to learn about AWS CloudHSM pricing. There are no upfront costs to use AWS CloudHSM. With AWS CloudHSM, you pay an hourly fee for each HSM you launch until you terminate the HSM. This guide provides the hourly rate for each AWS region. 

   [Explore the pricing page](https://aws.amazon.com/cloudhsm/pricing/) 
+ ** AWS CloudHSM FAQ **

   Review the AWS CloudHSM FAQ page for detailed answers to common questions about AWS CloudHSM, including its features, pricing, provisioning, security, compliance, performance, and integration with third-party applications. 

   [Explore the FAQs](https://aws.amazon.com/cloudhsm/faqs/) 

------
#### [ AWS Encryption SDK  ]
+  **Get started with the AWS Encryption SDK **

   Learn how to use the AWS Encryption SDK with AWS KMS. 

   [Explore the guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html) 
+  **Best practices for the AWS Encryption SDK **

   Review the AWS Encryption SDK Best Practices page for guidance on effectively utilizing the AWS Encryption SDK to secure your data. Adhering to these best practices helps ensure the confidentiality and integrity of your encrypted data. 

   [Explore the guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html) 
+  **AWS Encryption SDK FAQ **

   Review the AWS Encryption SDK FAQ page for answers to common questions about the AWS Encryption SDK, including its features, supported programming languages, and best practices for implementation. 

   [Explore the FAQ](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/faq.html) 

------
#### [ AWS Database Encryption SDK  ]
+ ** Get started with the AWS Database Encryption SDK **

   Learn how to use the AWS Database Encryption SDK with AWS KMS. 

   [Explore the guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-kms.html) 
+  **Configure the AWS Database Encryption SDK **

   Learn how to configure the AWS Database Encryption SDK, including selecting a programming language and selecting wrapping keys. 

   [Explore the guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure.html) 

------
#### [ AWS KMS  ]
+  **Get started with AWS KMS **

   Learn how to create KMS keys, including symmetric and asymmetric encryption keys. 

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) 
+  **Best practices for AWS KMS **

   Learn encryption best practices for AWS KMS. 

   [Explore the guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html) 
+  **AWS KMS pricing **

   Review the AWS Key Management Service (KMS) Pricing page to learn about the costs associated with using AWS KMS, including charges for key storage, API requests, and optional features like custom key stores. 

   [Explore the pricing page](https://aws.amazon.com/kms/pricing/) 
+  **AWS KMS FAQ **

   The AWS Key Management Service (KMS) FAQ page provides detailed answers to common questions about AWS KMS, including its features, security measures, billing practices, key management options, and integration with other AWS services. 

   [Explore the FAQs](https://aws.amazon.com/kms/faqs/) 

------
#### [ AWS Private CA  ]
+  **Best practices for AWS Private CA **

   Review recommendations that can help you use AWS Private CA effectively. 

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/ca-best-practices.html) 
+  **Get started with AWS Private CA **

   Learn how to create and activate a root CA programmatically. 

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ActivateRootCA.html) 
+  **AWS Private CA pricing **

   Review costs associated with operating private CAs and issuing private certificates. 

   [Explore the pricing page](https://aws.amazon.com/private-ca/pricing/) 
+  **AWS Private CA FAQ **

   Get detailed answers to common questions about AWS Private CA, including its features, pricing, provisioning, security, compliance, performance, and integration with other AWS services. 

   [Explore the FAQs](https://aws.amazon.com/private-ca/faqs/) 

------
#### [ AWS Secrets Manager  ]
+  **Get started with AWS Secrets Manager **

   Learn how to create an AWS Secrets Manager secret. 

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) 
+  **Best practices for AWS Secrets Manager **

   Learn about best practices you should consider when using AWS Secrets Manager. 

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html) 
+  **AWS Secrets Manager pricing **

   Review the AWS Secrets Manager pricing page to learn about costs associated with securely storing, managing, and retrieving secrets such as database credentials and API keys. 

   [Explore the pricing page](https://aws.amazon.com/secrets-manager/pricing) 
+  **AWS Secrets Manager FAQ **

   Review the AWS Secrets Manager FAQ page for detailed answers to common questions about AWS Secrets Manager, including its features, security measures, pricing, and integration capabilities. 

   [Explore the FAQs](https://aws.amazon.com/secrets-manager/faqs) 

------

### Explore
<a name="explore"></a>
+  **Research and resources** 

  Explore AWS blogs, videos and tools on cryptography. 

   [ Review resources](https://aws.amazon.com/security/cryptographic-computing/)
+  **Videos** 

  Watch these videos from the AWS Developers channel on YouTube to further develop and refine your cryptography strategy.

  [Explore cryptography videos](http://www.youtube.com/@awsdevelopers/search?query=cryptography)

## AWS WAF or AWS Shield?
<a name="waf-or-shield"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | To help you determine whether AWS WAF or AWS Shield meets your needs for a web application security service. | 
| **Last updated** | September 17, 2024 | 
| **Covered services** |  +  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) <br />+  [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)   | 

### Introduction
<a name="introduction"></a>

 [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) (Web Application Firewall) and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) can help you protect your web applications against various types of cyberattacks, such as Distributed Denial of Service (DDoS) attacks and other web application vulnerabilities.
+  **AWS WAF** focuses on protecting your web applications from common web exploits. Use AWS WAF to create customizable web security rules to filter malicious traffic, protect against attacks such as SQL injection and cross-site scripting (XSS), and integrate with other AWS services. 
+  **AWS Shield** is a managed DDoS protection service. Use AWS Shield to turn on always-on detection and automatic mitigations, and protect against common DDoS attacks at the network and transport layers. 

While AWS Shield defends against large-scale, network-level attacks, with AWS Shield Advanced, you can associate an AWS WAF web ACL with a resource to provide protection at the application layer. AWS WAF provides more granular protection against application-specific vulnerabilities. Use both services in tandem for a multi-layered defense strategy, safeguarding your applications from a broader range of potential threats across different network layers.

Here's a high-level view of the key differences between these services.


|  **Category**  |  ![Image displaying AWS WAF logo](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_AWS-WAF_48.png) **AWS WAF**  |  ![Image displaying AWS Shield logo](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/Arch_AWS-Shield_48.png) **AWS Shield**  | 
| --- | --- | --- | 
| Primary Purpose  | Protects against exploits on web applications (such as SQL injection or XSS)  | Protects against DDoS attacks (such as SYN or UDP floods)  | 
| Layer of protection  | Application layer (L7)  | Network, transport, and application layers (L3/L4/L7)  | 
| Deployment  | Must be explicitly set up  | AWS Shield Standard protection included for all customer accounts  | 
| Customization  | Highly customizable with custom rules  | Turn on or disable AWS Shield Advanced, with options to turn on automatic mitigation of application layer DDoS protections | 
| Managed Rules  | Includes AWS Managed Rules and third-party rules  | Not applicable  | 
| Pricing model  | Pay-as-you-go pricing based on number of rules and requests  | AWS Shield Standard included; AWS Shield Advanced incurs additional cost  | 
| Attack Response Team  | Not applicable  | Available with AWS Shield Advanced (24/7 DDoS Response Team)  | 
| Real-time monitoring  | Yes  | Yes  | 
| Traffic Inspection  | Request-level  | Packet-level  | 

### Differences between AWS WAF and AWS Shield
<a name="waf-shield-differences"></a>

Explore eight key areas of difference between AWS Shield and AWS WAF, covering layer of protection, deployment, customization, managed rules, pricing model, attack response team, real-time monitoring, and traffic inspection.

------
#### [ Layer of protection ]

 **AWS WAF** 
+ Operates at the application layer (Layer 7). It protects web applications by filtering and monitoring HTTP/S traffic. AWS WAF defends against common web exploits such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF). You can create custom rules to block malicious requests based on various criteria like IP addresses, query strings, and headers. 

 **AWS Shield** 
+ Operates primarily at the network (Layer 3) and transport (Layer 4) layers. It is designed to mitigate Distributed Denial of Service (DDoS) attacks that aim to overwhelm network resources, such as SYN/ACK floods, UDP reflection attacks, and volumetric attacks. AWS Shield ensures that network traffic reaching your AWS resources remains available even under attack. AWS Shield's protection works by analyzing network traffic patterns and automatically mitigating identified threats at the AWS network edge. 

------
#### [ Deployment ]

 **AWS WAF** 
+ Requires explicit setup and configuration. It can be deployed on multiple AWS services, including Amazon CloudFront, Application Load Balancer (ALB), Amazon API Gateway, and AWS AppSync. You must create and associate web ACLs (Access Control Lists) with your resources, defining rules to allow, block, or monitor specific web requests. AWS WAF offers customizable deployment options, allowing you to tailor security policies to your specific application needs. 

 **AWS Shield** 
+ Automatically integrated with AWS services and is always on, requiring no additional setup for basic protection. AWS Shield Standard is automatically included with all AWS accounts, protecting resources like Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, and Route 53. For enhanced protection with AWS Shield Advanced, you must explicitly turn it on for specific resources. Deployment is seamless, and no additional configuration is necessary once AWS Shield is turned on. 

------
#### [ Customization ]

 **AWS WAF** 
+ Provides extensive customization capabilities. You can create custom web ACLs (Access Control Lists) with rules that define specific conditions for allowing, blocking, or counting web requests based on IP addresses, HTTP headers, query string parameters, and more. AWS WAF supports managed rule groups from AWS or third parties, which can be customized further to suit your specific application needs. You can also set up rate-based rules to limit the number of requests from a single IP address and integrate AWS WAF with AWS Lambda for advanced request inspection and response. 

 **AWS Shield** 
+ Offers limited customization options. With AWS Shield Standard, protection is automatic and non-configurable. AWS Shield Advanced allows for some customization, such as enabling advanced metrics and alerts, setting up Health Checks, and accessing the AWS DDoS Response Team (DRT) for tailored mitigation support. However, its focus remains on automated DDoS protection rather than user-defined settings. You can associate an [AWS WAF web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-protections.html) with resources to turn on application layer protection. 

------
#### [ Managed rules ]

 **AWS WAF** 
+ Offers a range of managed rules that can be applied to web applications to protect against common web threats. These managed rules are pre-configured by AWS or third-party security vendors and cover various security scenarios such as SQL injection, cross-site scripting (XSS), and known bad IP addresses. You can subscribe to and apply these managed rule groups to your web ACLs, providing out-of-the-box protection that is regularly updated to address new vulnerabilities and threats. Managed rules can be customized and combined with custom rules to tailor security policies to specific application needs. AWS WAF also provides [managed intelligent threat mitigation features](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections.html). These are advanced, specialized protections that you can implement to protect against threats such as malicious bots and account takeover attempts. 

 **AWS Shield** 
+ Primarily focused on DDoS protection, and doesn't offer traditional managed rules. AWS Shield Standard automatically applies a set of predefined protections against common network and transport layer DDoS attacks. AWS Shield Advanced enhances these protections but doesn't provide customizable managed rules. Instead, it offers more advanced mitigation techniques and access to the DDoS Response Team for tailored assistance. 

------
#### [ Pricing model ]

 **AWS WAF** 
+ Uses a [pay-as-you-go pricing model](https://aws.amazon.com/waf/pricing/). You are charged based on the number of web ACLs you create, the number of rules you deploy within each ACL, and the number of web requests processed by the rules. This model allows for scalable costs based on actual usage, meaning you only pay for the resources you need. Additional charges apply for managed rule groups provided by AWS or third-party vendors. AWS WAF also provides managed rules for Bot control and fraud control with a similar per request pricing model. AWS WAF also offers a captcha/challenge feature which is charged by the number of captcha attempts and challenge responses served. 

 **AWS Shield** 
+ Has a tiered pricing model. AWS Shield Standard is included at no additional cost with all AWS accounts, providing basic DDoS protection. AWS Shield Advanced incurs a fee based on a monthly subscription and additional charges for data transfer and mitigation beyond a certain threshold. This subscription includes 24/7 access to the AWS DDoS Response Team (DRT), advanced attack diagnostics, and cost protection during attacks. 

------
#### [ Attack response team ]

 **AWS WAF** 
+ Does not include a dedicated attack response team as part of its service. Instead, it provides tools and features that allow you to create, manage, and adjust security rules themselves. You can monitor traffic and make real-time changes to your web ACLs based on the threat landscape, but you don't have direct access to a specialized support team for attack mitigation. 

 **AWS Shield** 
+ Offers access to the AWS DDoS Response Team (DRT) as part of its AWS Shield Advanced service. The DRT is a 24/7 team of experts that assists with real-time attack mitigation and response. When under a DDoS attack, you can contact the DRT for customized advice and support to manage and mitigate the threat effectively. This includes guidance on best practices, incident analysis, and coordinated responses to minimize the impact on your AWS resources. 

------
#### [ Real-time monitoring ]

 **AWS WAF** 
+ Offers real-time monitoring by integrating with AWS CloudWatch, allowing you to track metrics such as blocked or allowed requests, request rates, and the effectiveness of specific rules. AWS WAF provides near real-time visibility into web traffic and security events through the AWS Management Console or APIs. You can set up custom CloudWatch alarms based on your AWS WAF metrics to respond quickly to potential threats or unusual traffic patterns. 

 **AWS Shield** 
+ Provides real-time monitoring primarily through AWS Shield Advanced. It integrates with AWS CloudWatch to deliver near real-time metrics and alerts related to DDoS attacks. You can monitor attack diagnostics, traffic patterns, and the effectiveness of mitigations. AWS Shield Advanced also offers detailed reports and visibility into attack vectors and scales automatically in response to threats, providing insights through the AWS Management Console. 

Both services provide dashboards for visualizing attack patterns and traffic trends. AWS Shield's monitoring focuses on network-level anomalies and volumetric attacks, while AWS WAF provides deeper insights into application-layer requests and rule effectiveness. 

------
#### [ Traffic inspection ]

 **AWS WAF** 
+ Inspects traffic at the application layer (Layer 7), analyzing the contents of HTTP/S requests. It evaluates web traffic against user-defined rules, checking for specific attack patterns such as SQL injection, cross-site scripting (XSS), or other malicious payloads within the request body, headers, or URL parameters. 

 **AWS Shield** 
+ Focuses on protecting against DDoS attacks, primarily inspecting traffic at the network (Layer 3) and transport (Layer 4) layers. It does not inspect the contents of application layer traffic (HTTP/S), but rather looks for patterns typical of DDoS attacks, such as unusually high traffic volumes or protocol misuse. AWS Shield automatically mitigates these threats without user-defined rules or content-based inspection, ensuring the availability of AWS services under attack. 

------

### Use
<a name="use"></a>

------
#### [ AWS WAF ]
+  **What is AWS WAF?** 

   Learn how you can use AWS WAF to monitor and protect your web applications from common web exploits. 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)  
+  **Analyzing AWS WAF Logs in Amazon CloudWatch Logs** 

   Set up native AWS WAF logging to Amazon CloudWatch logs and visualize and analyze the data in the logs. 

   [Read the blog](https://aws.amazon.com/blogs/mt/analyzing-aws-waf-logs-in-amazon-cloudwatch-logs/) 
+  **Visualize AWS WAF logs with an Amazon CloudWatch dashboard** 

   Use Amazon CloudWatch to monitor and analyze AWS WAF activity by using CloudWatch metrics, Contributor Insights, and Logs Insights. 

   [Read the blog](https://aws.amazon.com/blogs/security/visualize-aws-waf-logs-with-an-amazon-cloudwatch-dashboard/)  

------
#### [ AWS Shield ]
+  **What is AWS Shield?** 

   Learn how you can use AWS Shield to protect your web applications against common DDoS attacks at the network and transport layers. 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) 
+  **Getting started with AWS Shield Advanced** 

   Get started with AWS Shield Advanced by using the AWS Shield Advanced console. 

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html) 
+  **AWS Shield Advanced workshop** 

   Protect internet-exposed resources against DDoS attacks, monitor DDoS attacks against your infrastructure, and notify the appropriate teams. 

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6396761b-6d1f-4a4d-abf1-ffb69dee6995/en-US) 

------

# Serverless & Application Integration
<a name="application-integration"></a>

The following decision guides help you choose AWS serverless services and application integration services for queues, events, and workflows.

**Topics**
+ [Choosing an AWS serverless service](#choosing-aws-serverless-service)
+ [Choosing an AWS application integration service](#application-integration-on-aws-how-to-choose)
+ [Amazon SQS, Amazon SNS, or Amazon EventBridge?](#sns-or-sqs-or-eventbridge)

## Choosing an AWS serverless service
<a name="choosing-aws-serverless-service"></a>


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS serverless services are the best fit for your workload. | 
| **Last updated** | September 4, 2026 | 
| **Audience** | Developers and architects evaluating AWS serverless services for new or existing workloads. | 
| **Covered services** |  + [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) (Event Functions, MicroVMs, Durable Functions)<br />+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)<br />+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)<br />+ [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)<br />+ [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)<br />+ [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)<br />+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)<br />+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)<br />+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)<br />+ [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br />+ [Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)<br />+ [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)<br />+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)<br />+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)  | 

### Introduction
<a name="serverless-intro"></a>

With AWS serverless services, you can build and run applications without provisioning or managing servers. You pay only for the resources you consume, and services scale automatically in response to demand.

AWS offers serverless options across compute, API management, application integration, orchestration, and data storage, that you can use to assemble complete applications from managed services. You can build applications ranging from microservices that handle discrete business logic as a part of your application backend, to event-driven workflows that perform data transformations or processing.

![Core serverless services grouped by category: compute, API layer, application integration, data storage, deployment, and observability.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/core-services-serverless.png)


 Traditional application frameworks bundle routing, data access, and integrations into a single codebase that you scale and maintain as one unit. This approach works well for getting started quickly, and frameworks like Express, Django, and Spring Boot provide familiar tools that boost initial productivity. However, as applications grow and rely on more external systems, complexity increases. The monolithic model makes scaling individual features difficult and slows down both development and troubleshooting. Serverless development addresses these challenges by composing independent services that each handle a specific function. Instead of building common distributed patterns from scratch, you use purpose-built AWS services for queues, event buses, publish/subscribe, orchestration, and APIs.

 There are well-established patterns in distributed architectures, including queues, event buses, publish/subscribe, orchestration, APIs, and event streams, that you can implement using purpose-built AWS services rather than building from scratch. When your application needs one of these patterns, use the corresponding AWS service:


| Pattern | AWS service | 
| --- | --- | 
| Queue | Amazon SQS | 
| Event bus | Amazon EventBridge | 
| Publish/subscribe (fan-out) | Amazon SNS | 
| Orchestration | Step Functions | 
| API | Amazon API Gateway | 
| Event streams | Amazon Kinesis | 

This guide helps you select the AWS serverless services and tools that are the best fit for your workload patterns and organizational requirements.

### Understand
<a name="serverless-understand"></a>

These services communicate through events, which are messages that represent a change in state. For example, when a customer uploads a photo to Amazon S3, Amazon S3 publishes an event that triggers a Lambda function to generate a thumbnail, without the upload service needing to know about the thumbnail service. You can also handle long-running tasks asynchronously. For example, you can implement a queue using Amazon SQS to manage order submissions. Then use Step Functions to manage a workflow that updates user information and inventory counts after every order is processed. Along the way, you use Amazon CloudWatch to log actions, monitor application activity, and AWS X-Ray to trace data flows for debugging. Event producers don't need to know which downstream services will respond. This decoupling allows each component to scale, deploy, and evolve independently. For information about advantages of a decoupled architecture, see [What is EDA (Event-Driven Architecture)?](https://aws.amazon.com/what-is/eda/).

![Serverless event-driven architecture with Lambda at the center, connected through events to the full ecosystem of serverless services.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/serverless-conceptual.png)


The following sections describe the services available in each category of a serverless architecture, and what they are optimized for.

------
#### [ Serverless compute ]
+ **Lambda Event Functions**: Run code in response to events without provisioning servers. Event functions scale automatically from zero to thousands of concurrent executions and charge per request and execution duration. Optimized for event-driven, short-lived workloads with a maximum duration of 15 minutes per invocation. Lambda also supports response streaming for progressive delivery of results, which is useful for generative AI and large payload responses. For workflows that need to run longer, Lambda durable functions automatically persist state across multiple invocations, enabling long-running executions while staying within the per-invocation time limit.
+ **Lambda MicroVMs**: A different compute form factor under the Lambda service, distinct from Event Functions in timeout, programming model, concurrency model, and billing. MicroVMs run isolated, stateful execution environments for user or AI-generated code. Each MicroVM provides VM-level isolation powered by Firecracker with full operating system capabilities (installing packages, mounting filesystems), snapshot-based rapid startup, and up to 8-hour lifetimes. MicroVMs support suspend and resume to reduce idle costs while preserving memory and disk state, port-listening protocols (HTTP/2, gRPC, WebSocket), and flexible resource allocation with baseline capacity that can burst to 4x during peak activity. Unlike Event Functions, MicroVMs use a Dockerfile-based programming model and allocate one environment per session rather than scaling per request. Suited for AI coding sandboxes, interactive development environments, data analytics notebooks, multi-tenant CI executors, security scanning, reinforcement learning environments, and game servers. Each MicroVM gets a dedicated HTTPS endpoint without requiring load balancers or ingress infrastructure, and supports configurable egress networking for VPC access and public internet connectivity.
+ **AWS Fargate**: Run containers without managing servers or clusters. Fargate handles provisioning and scaling of compute for containerized workloads. Suited for long-running services, batch processing, or workloads that need custom runtimes and fine-grained resource control.

**Tip**  
For a deeper comparison of serverless compute options, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ API layer ]
+ **Amazon API Gateway HTTP API**: Lightweight, lower-cost API routing optimized for Lambda and HTTP backends with automatic deployments.
+ **Amazon API Gateway REST API**: Full-featured API management with request validation, response streaming, caching, AWS WAF integration, usage plans, API keys, and private endpoints.
+ **AWS AppSync**: Managed GraphQL service with real-time subscriptions, offline sync, and automatic data source integration (DynamoDB, Lambda, HTTP). Best for mobile and web apps with complex data requirements. AWS AppSync Events provides serverless WebSocket APIs for real-time publish/subscribe messaging, allowing applications to both publish and subscribe to events over a single WebSocket connection with data source integrations for processing published events.
+ **Lambda function URLs**: Dedicated HTTPS endpoints for individual Lambda functions without API Gateway. Suited for single-function microservices or webhooks where API management features aren't needed.
+ **Amazon API Gateway WebSocket APIs**: Persistent, bidirectional connections between clients and backend services. Use for chat applications, real-time dashboards, multiplayer games, or financial trading platforms where the server needs to push data to clients without polling.

------
#### [ Application integration ]
+ **Amazon Simple Queue Service**: Fully managed message queue for decoupling services. Supports standard (at-least-once, best-effort ordering) and FIFO (exactly-once, strict ordering) queues. Use for buffering, load leveling, and asynchronous processing.
+ **Amazon Simple Notification Service**: Publish/subscribe messaging for fan-out to multiple subscribers (Lambda, Amazon SQS, HTTP, email, SMS). Use when one event needs to trigger multiple downstream actions. Supports message filtering with subscription filter policies including wildcard and prefix matching, allowing subscribers to receive only relevant messages without custom filtering logic.
+ **Amazon EventBridge**: Serverless event bus for routing events from AWS services, SaaS apps, and custom sources using content-based filtering rules. Use for event-driven architectures with complex routing or third-party integrations.

**Tip**  
For a deeper comparison, see [Amazon SQS, Amazon SNS, or Amazon EventBridge?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html)

------
#### [ Orchestration ]
+ **AWS Step Functions Standard Workflows**: Coordinate multi-step processes with exactly-once execution, full execution history, and up to one year duration. Use for order processing, human approvals, and ETL pipelines.
+ **AWS Step Functions Express Workflows**: High-volume, short-duration orchestration (up to 5 minutes) with at-least-once execution. Use for IoT data ingestion, streaming transforms, and high-rate event processing.

Step Functions supports variables for assigning data in one state and using it in subsequent states, and JSONata transformations for advanced data manipulation including date formatting and mathematical operations. These features simplify data sharing across states and reduce the need for intermediate processing steps. For large-scale batch processing, Distributed Map runs the same process across millions of items from Amazon S3, Athena, or JSON datasets in parallel without provisioning compute infrastructure.

------
#### [ Data storage ]
+ **Amazon DynamoDB**: Serverless NoSQL key-value and document database with single-digit millisecond response times at any scale. No connection pooling needed. Use for high-throughput, low-latency data access with flexible schemas.
+ **Amazon Simple Storage Service**: Object storage with unlimited capacity. Use for file storage, data lakes, static assets, and event-driven processing (Amazon S3 triggers Lambda on upload).
+ **Amazon Aurora Serverless**: On-demand, auto-scaling relational database compatible with MySQL and PostgreSQL. Use when you need SQL semantics, complex joins, or ACID transactions with serverless scaling.

**Tip**  
For a deeper comparison, see [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html).

------
#### [ Deployment and infrastructure as code ]
+ **AWS Serverless Application Model**: CloudFormation extension with shorthand syntax for Lambda, API Gateway, DynamoDB, and Step Functions. Includes local testing through the SAM CLI. Best for serverless-first applications.
+ **AWS Cloud Development Kit (AWS CDK)**: Define infrastructure using programming languages (TypeScript, Python, Java, C\#, Go). Best for complex applications that benefit from loops, conditionals, and reusable constructs.
+ **Terraform**: Multi-cloud IaC using HashiCorp Configuration Language (HCL). Best for platform teams managing infrastructure across providers.

------
#### [ Observability ]
+ **Amazon CloudWatch**: Metrics, logs, alarms, and dashboards for monitoring Lambda functions, API Gateway, and other services.
+ **AWS X-Ray**: Distributed tracing for understanding request flow across Lambda functions and integrated services. Essential for debugging event-driven architectures.

**Tip**  
For a deeper comparison, see [Choosing an AWS monitoring and observability service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/monitoring-on-aws-how-to-choose.html).

------

### Consider
<a name="serverless-consider"></a>

Here are some key factors to consider when choosing AWS serverless services. Choosing the right combination involves balancing these factors to match your workload patterns, technical requirements, and organizational goals. This helps you optimize for performance, cost, and operational simplicity.

------
#### [ Workload pattern ]

Understanding the operational pattern of your application is the most important factor in selecting serverless services. Different workload patterns demand different service combinations. Serverless data processing largely falls within the following patterns:
+ **Asynchronous processing**: File processing, image manipulation, batch transformations, and webhooks. These workloads process events that don't require an immediate response and benefit from queues for buffering and fan-out for parallel processing.
+ **Synchronous request/response**: Web APIs, mobile backends, and microservices. These workloads need low-latency compute that responds to individual HTTP requests and scales with concurrent traffic.
+ **Streaming**: IoT telemetry, click-stream analysis, real-time analytics, and transaction processing. These workloads ingest high-velocity, continuous data that must be processed in near-real time.
+ **Orchestration**: Multi-step approval flows, ETL pipelines, and saga patterns. These workloads coordinate tasks with branching logic, error handling, and state management.

Each pattern uses a different combination of serverless services. For detailed examples and recommended service combinations for each pattern, see the Choose section.

------
#### [ Execution duration and concurrency ]

Serverless compute services differ significantly in how long they allow a single execution to run and how they handle concurrency. Unlike traditional servers, Lambda event functions do not run constantly. When a function is triggered by an event, this is called an invocation. Lambda event functions are limited to 15 minutes in duration, but on average, across all AWS customers, most invocations last for less than a second.

**Short-lived, event-driven invocations** are best served by Lambda, which supports execution durations up to 15 minutes and scales automatically per-request to thousands of concurrent invocations. The Lambda service runs instances of your function only when needed and scales automatically from zero requests per day to thousands per second. You pay only for the compute time that is actually used, so there is no charge when your code is not running. The per-millisecond billing of Lambda can reduce cost for short-duration workloads.

There are many types of invocation events that can trigger short-lived functions. Some examples include an HTTP request from API Gateway, a schedule managed by an EventBridge rule, a message from an IoT device, or a notification that a file was uploaded to an Amazon S3 bucket.

**Stateful, interactive sessions**, such as AI coding sandboxes, interactive notebooks, and multi-tenant CI environments, need isolated environments that retain state across user interactions. Lambda MicroVMs are a different compute form factor from Event Functions: they use a Dockerfile-based programming model, allocate one environment per session (not per request), and bill on a baseline plus burst model rather than per-millisecond. MicroVMs provide VM-level isolation with full OS capabilities, snapshot-based rapid startup, up to 8-hour lifetimes, and suspend/resume to reduce idle costs.

**Long-running or steady-state processes**, such as batch jobs, persistent WebSocket connections, or services that require more than 15 minutes of continuous processing, are better served by Fargate, which can run indefinitely. For details on how Fargate and Lambda scale differently, see the Scaling model and latency tab. Fargate provides consistent resource allocation for workloads that exceed the timeout or compute limits of Lambda. Additionally, Lambda durable functions enable multi-step, long-running executions that persist state across multiple invocations. Each individual invocation still respects the 15-minute limit. Durable functions automatically checkpoint progress and resume where they left off, so total workflow durations can far exceed 15 minutes without requiring Fargate or external orchestration.

Consider both the average and maximum execution time of your workloads. A Lambda function that occasionally exceeds 15 minutes fails unpredictably and requires architectural redesign. Your application architecture and needs determine how to invoke a function. For example, batch-processing patterns have different requirements than on-demand data processing. Fargate suits a microservice that primarily handles batch data processing. Lambda is simpler to deploy and maintain for on-demand processing.

------
#### [ Cost model and predictability ]

One of the key advantages of serverless development is that you pay only for the resources you consume. Serverless technologies are pay-as-you-go, which means you can scale up and down as your application needs change without paying for idle capacity. However, different AWS serverless services use different pricing models that favor different usage patterns.

**Pay-per-use pricing** (Lambda, Step Functions Express, EventBridge) charges based on actual invocations and duration, with no cost when idle. For Lambda, you are charged based on the number of requests for your functions and the duration it takes for your code to run. There is no charge when your code is not running. This model suits unpredictable or spiky workloads where traffic can drop to zero, and for early-stage applications where demand is uncertain.

**Capacity-based pricing** (Fargate, Amazon Aurora Serverless, DynamoDB provisioned mode) charges for reserved compute or throughput capacity. While this might incur costs during low-traffic periods, it becomes more cost-effective at sustained, predictable scale where per-request pricing would exceed the equivalent reserved capacity. For example, DynamoDB provisioned mode lets you adjust your tables' throughput capacity as needed, which can be more economical for workloads with consistent traffic patterns.

**Hybrid pricing** (DynamoDB on-demand, API Gateway) offers per-request pricing that scales linearly without upfront commitment. This provides cost predictability without the need to forecast capacity, but can become expensive at very high throughput compared to provisioned alternatives.

**Baseline plus burst pricing** (Lambda MicroVMs) charges for configured baseline resources while the MicroVM is running, with the ability to burst to 4x baseline during peak activity. Suspended MicroVMs reduce cost while preserving state. This model suits interactive workloads with variable activity and idle periods.

Model your expected traffic patterns across daily, weekly, and seasonal cycles. Workloads with high peak-to-average ratios favor per-use pricing. Steady-state workloads might benefit from capacity-based pricing. You can also use a combination: for example, Lambda with pay-per-use for variable compute alongside DynamoDB provisioned mode for predictable data access patterns.

------
#### [ Operational complexity ]

Traditional web application frameworks bundle routing, data access, connection pools, and integrations into a single codebase that you deploy and maintain as one unit. Setting up, configuring, and maintaining the frameworks, runtime environments, and infrastructure slows down your delivery of features and bug fixes. As applications grow and rely on more external systems, this complexity increases ramp-up time for new developers, makes tracking down the source of bugs more challenging, and delays the delivery of new features.

Serverless services exist on a spectrum of operational responsibility that reduces or eliminates this overhead. Instead of managing everything in one package, you compose loosely connected services where each one does one thing well with as few dependencies as possible.

**Minimal management**: Lambda, API Gateway, DynamoDB, Amazon SQS, Amazon SNS, EventBridge, and Step Functions require no server provisioning, patching, or capacity planning. You don't need to set up connection pools, configure runtime environments, or manage scaling infrastructure. You can focus entirely on writing or generating code that solves business problems.

**Container management**: Fargate requires building and maintaining container images, configuring task definitions, and managing deployment pipelines. You don't manage the underlying infrastructure, but you own the container lifecycle. This model suits teams that need custom runtimes or have existing containerized workloads they want to run without managing clusters.

**Infrastructure as code complexity**: AWS Serverless Application Model minimizes IaC complexity for serverless-only architectures with shorthand syntax and local testing. AWS Cloud Development Kit (AWS CDK) and Terraform provide more power for complex applications at the cost of steeper learning curves and more code to maintain.

Consider your team's existing skills, the number of services to manage, and your organization's operational standards. If your teams are spending more time maintaining infrastructure than building features, moving toward the minimal management end of the spectrum can free up resources for higher-value work.

------
#### [ Scaling model and latency ]

How a service scales directly impacts your application's responsiveness under load. In serverless architectures, scaling happens automatically, but different services use different mechanisms that affect latency and throughput.

**Per-request scaling** (Lambda) creates a new execution environment for each concurrent request. Lambda invokes your function in an execution environment, which provides a secure and isolated runtime environment that manages the processes and resources required to run the function. This provides near-instant response to traffic spikes, scaling from zero to thousands of concurrent executions in seconds.

However, per-request scaling introduces cold starts, which are initialization delays that occur when Lambda creates a new execution environment. The largest contributor to cold start time is the time that Lambda spends initializing the function, which includes loading the function's code, starting the runtime, and initializing the function code. For Java, Python, and .NET workloads, Lambda SnapStart can improve startup performance by up to 10x at no extra cost by taking a snapshot of the initialized execution environment and caching it for low-latency access. For other runtimes, you can mitigate cold starts with Provisioned Concurrency at additional cost.

**Task-level scaling** (Fargate) adds or removes container instances based on metrics such as CPU utilization, memory usage, or request count. Scaling adds new tasks in seconds to minutes and avoids cold starts for requests handled by existing tasks. Once a task is running, it stays warm for its entire lifetime, providing consistent latency for all requests it handles.

**Throughput-based scaling** (DynamoDB, Kinesis) adjusts read/write capacity or shard count based on demand. DynamoDB on-demand mode scales instantly to accommodate your workload's traffic patterns. Provisioned mode requires auto-scaling configuration but provides predictable throughput at lower per-request costs. With serverless architecture and DynamoDB, connection pools are not necessary to rapidly connect and scale the database. Instead, you adjust your tables' throughput capacity as needed.

For strict latency requirements (sub-100ms P99), evaluate cold-start behavior carefully. Lambda with Provisioned Concurrency or SnapStart, or Fargate with pre-warmed tasks, provides predictable latency for API workloads. For data processing workloads where latency is less critical, standard Lambda scaling is typically sufficient.

------
#### [ Integration and composability ]

Serverless architectures are composed from multiple services that communicate through events. An event represents a change in state, or an update. For example, an item placed in a shopping cart, a file uploaded to a storage system, or an order becoming ready to ship. The depth of native integration between services affects how quickly you can build and how much custom code you need to write.

**Deep native integration**: Lambda integrates with over 200 AWS services as event sources. Some services can trigger Lambda functions directly. For example, when an image is added to an Amazon S3 bucket, Lambda can be triggered to resize it. Some services cannot invoke Lambda directly, but you can use an event source mapping, which is a polling mechanism that reads from an event source and invokes a Lambda function. You can use event source mappings to process items from a stream or queue in: DynamoDB Streams, Amazon Kinesis, Amazon MQ, Amazon MSK, self-managed Apache Kafka, and Amazon SQS.

**Event routing flexibility**: EventBridge provides content-based routing with filtering rules, allowing a single event bus to route events to different targets based on event content. Amazon SNS provides topic-based fan-out to deliver messages to multiple subscribers simultaneously. Amazon SQS provides point-to-point buffering where consumers actively poll messages from the queue. Common combinations include routing EventBridge or Amazon SNS events to an Amazon SQS queue as a buffer for downstream consumers, pulling events from a stream or queue with EventBridge Pipes, and routing events to Kinesis for analytics.

**API integration patterns**: API Gateway offers two integration approaches. Proxy integrations directly pass all request information to a Lambda function for processing, which is simpler to configure. Non-proxy (custom) integrations can transform data before it reaches your function and before output returns to clients, which is useful for legacy code migration or keeping function code focused on business logic. REST API provides the broadest feature set including caching, request validation, and WAF. HTTP API provides the lowest latency and cost. AWS AppSync provides real-time subscriptions and GraphQL. Lambda function URLs provide the simplest single-function HTTPS endpoint without requiring API Gateway. For bidirectional communication where the server needs to push data to clients, API Gateway WebSocket APIs provide persistent connections suited for chat, real-time dashboards, and multiplayer games.

Due to the loose coupling between components of an event-driven system, your compute functions are not aware of other activities in the architecture. You can scale components independently, one service can fail without impacting other services, and events can be flexibly routed, buffered, and provide a log for audit.

------
#### [ Portability and standards ]

Your choice of serverless services affects how portable your architecture is across environments. Serverless applications usually comprise several AWS services, integrated with custom code run in Lambda functions. While Lambda can be integrated with most AWS services, you should consider the trade-off between deep platform integration and the ability to run workloads in other environments.

**AWS native services** (Lambda, Step Functions, EventBridge, DynamoDB) provide the deepest integration and lowest operational overhead. You can use any of these services through the AWS SDK without needing to install applications or configure servers. Becoming proficient with using these services through code in your Lambda functions is an important step to producing well-designed serverless applications. However, these services create coupling to AWS-specific APIs and event formats, meaning migrating to another cloud requires significant refactoring.

**Standards-based services** (Fargate with Docker containers, Amazon MQ with AMQP, Amazon MSK with Apache Kafka) run on open protocols or open-source technologies. If you need a custom runtime that is not provided by AWS, you can create and deploy a custom container image on Fargate. Amazon MSK provides Apache Kafka compatibility for teams with existing Kafka expertise. These options make workload portability more feasible at the cost of higher operational complexity and less tight integration with other AWS services.

**Deployment frameworks**: AWS Serverless Application Model and AWS Cloud Development Kit (AWS CDK) generate CloudFormation templates and are AWS-only. AWS Serverless Application Model extends CloudFormation with shorthand syntax focused on speeding up serverless development, offering optimized definitions for API Gateway, Lambda, and Step Functions resources, plus local Lambda testing through the SAM CLI. Terraform provides multi-cloud infrastructure definition using a single workflow across providers but with less serverless-specific tooling and limited local Lambda testing capabilities.

Containers and standards-based messaging can improve portability for multi-cloud requirements. Native serverless services offer close integration with other AWS services, which can simplify development when your workload runs primarily on AWS.

------

### Choose
<a name="serverless-choose"></a>

The following information can help you evaluate which AWS serverless services fit your workload requirements.

The following table highlights which services are optimized for which circumstances.


| Serverless category | What is it optimized for? | Serverless services | 
| --- | --- | --- | 
| Compute | Running code in response to events with minimal operational overhead, scaling per-request with no idle cost. Running isolated, stateful execution environments for user or AI-generated code. | [Lambda Event Functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)<br />[Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html)<br />[AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) | 
| API layer | Routing HTTP and WebSocket requests to backend services, managing authentication, throttling, and caching. | [Amazon API Gateway HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)<br />[Amazon API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)<br />[AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)<br />[Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)<br />[Amazon API Gateway WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html) | 
| Application integration | Decoupling services through messaging, publish/subscribe, and event routing for asynchronous, loosely-coupled architectures. | [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)<br />[Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)<br />[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) | 
| Orchestration | Coordinating multi-step workflows with branching, error handling, retries, and state management. | [AWS Step Functions Standard Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)<br />[AWS Step Functions Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) | 
| Data storage | Storing and retrieving data with automatic scaling, no server management, and pay-per-use pricing. | [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)<br />[Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br />[Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) | 
| Deployment and IaC | Defining, deploying, and managing serverless infrastructure and application code as code. | [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)<br />[AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)<br />[Terraform getting-started tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) on the HashiCorp website | 
| Observability | Monitoring performance, tracing requests across services, and diagnosing issues in event-driven architectures. | [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) | 

The following tabs provide detailed guidance based on your specific workload needs. Choose the tab that best describes what you need to build, and review the recommended services and examples for that use case.

------
#### [ Synchronous API backend ]

You need to handle HTTP requests from web or mobile clients, process them, and return responses with low latency.

For web APIs and mobile backends, API Gateway routes HTTP requests to Lambda functions. DynamoDB handles low-latency data access. HTTP API provides simple routing at lower cost, while REST API adds caching, request validation, and WAF integration. You can handle authentication with Amazon Cognito, and AWS Serverless Application Model can define these resources with shorthand syntax.

To implement synchronous processing, use AWS Lambda for compute and Amazon API Gateway Gateway for routing requests. Use AWS Step Functions to orchestrate microservice workflows. Store data and files with DynamoDB and Amazon S3, and authenticate users with Amazon Amazon Cognito.

For example, suppose you want to build a microservices application that looks up weather data by zip code. The client resolves the hostname through Amazon Route 53. The HTTP GET request routes to API Gateway, which verifies an access token through Amazon Cognito, then sends the request to a Lambda function. The function queries DynamoDB, customizes the data, sends an event to Amazon SQS for analytics, and another to Amazon SNS for alerts. After traffic slows, Lambda tears down the execution environment. You pay only for actual function usage.

![Weather microservice architecture: a mobile client's request flows through Route 53, API Gateway, Cognito, Lambda, DynamoDB, SQS, and SNS, with CloudWatch monitoring throughout.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/weather-microservice-serverless.png)


**Tip**  
For deeper guidance on compute selection, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ Asynchronous event processing ]

You need to handle events that don't require an immediate response, with reliable delivery and the ability to absorb traffic spikes.

For workloads that process events without an immediate response, Amazon SQS handles buffering and load leveling. Amazon SNS can fan out a single event to multiple subscribers in parallel. EventBridge filters events by content and integrates with SaaS applications. Step Functions coordinates multi-step processing, with DynamoDB or Amazon S3 for storing results.

To implement asynchronous processing, use AWS Lambda for compute and AWS Step Functions for orchestration. Route messages with Amazon Simple Notification Service for fan-out and Amazon Simple Queue Service for durable queuing. Store results in DynamoDB and Amazon S3.

For example, when a user uploads a photo to Amazon S3, Amazon S3 publishes an event that invokes a Lambda function to generate a thumbnail. If you also need to categorize the image and notify the user, use Amazon SNS to fan out that single upload event to multiple Lambda functions processing in parallel.

**Tip**  
For deeper guidance on integration services, see [Amazon SQS, Amazon SNS, or Amazon EventBridge?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html)

------
#### [ Multi-step workflow orchestration ]

You need to coordinate a sequence of tasks with branching logic, error handling, retries, and human approval steps.

Standard Workflows handle processes that run up to 1 year with exactly-once execution and full audit history. For high-volume, short-duration processing (up to 5 minutes), Express Workflows operate at lower cost per execution.

Step Functions is useful when you have workflows with more than one state, need to branch, or run tasks in parallel. The Step Functions service acts as the state model for your application. Standard Workflows provide exactly-once execution with a full, auditable execution history, making them well-suited for order processing, human approval workflows, and ETL pipelines. Express Workflows provide at-least-once execution at higher volume and lower cost, making them well-suited for IoT data ingestion, streaming transforms, and high-rate event processing.

**Tip**  
For deeper guidance, see [Choosing an AWS application integration service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/application-integration-on-aws-how-to-choose.html).

------
#### [ Real-time streaming data ]

You need to ingest, process, and analyze high-velocity continuous data in near-real time. Lambda and Amazon Kinesis can process real-time streaming data. Use cases include activity tracking, click-stream analysis, log filtering, IoT telemetry, and metering.

For native AWS integration, Kinesis Data Streams handles stream ingestion. Amazon MSK can ingest streams with Apache Kafka compatibility. Either Lambda or Fargate processes the stream data, with DynamoDB or Amazon S3 for storing results.

To implement serverless streaming, use AWS Lambda for compute and Amazon Kinesis for collecting and analyzing real-time data. Store results with DynamoDB and Amazon S3.

For example, when items are written to a DynamoDB table, DynamoDB Streams publishes events that invoke a Lambda function to generate real-time analytics. For higher-volume ingestion like IoT telemetry from millions of devices, use Kinesis Data Streams to collect and buffer the data before processing.

------
#### [ Long-running or batch processing ]

You need processing that exceeds the 15-minute limit of Lambda, requires persistent connections, or benefits from custom container runtimes.

For workflows that exceed 15 minutes but consist of discrete steps, Lambda durable functions checkpoint progress and resume across invocations. Step Functions Distributed Map can process millions of items from Amazon S3, Athena, or JSON in parallel without provisioning compute. Fargate supports continuous processing, persistent connections, and fine-grained CPU/memory control.

For example, a nightly data pipeline that processes 10 million Amazon S3 objects uses Step Functions Distributed Map to parallelize the work. A video transcoding service that processes files for 30\+ minutes uses Fargate. A multi-step loan approval workflow that spans days uses Lambda durable functions to persist state between human review steps.

**Tip**  
For deeper guidance on compute selection, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ Isolated execution environments ]

You need to run user-supplied or AI-generated code in isolated environments with strong tenant separation and state preservation.

Lambda MicroVMs provide VM-level isolation powered by Firecracker, with full operating system capabilities, snapshot-based rapid startup, and up to 8-hour lifetimes. Each MicroVM gets a dedicated HTTPS URL supporting HTTP/2, gRPC, and WebSocket protocols. MicroVMs can be suspended when idle to reduce costs while preserving memory and disk state. Unlike Event Functions, MicroVMs use a Dockerfile-based programming model, allocate one environment per session, and bill on a baseline plus burst model (up to 4x baseline during peak activity). Each MicroVM supports configurable egress networking for VPC access and public internet connectivity, without requiring load balancers or ingress infrastructure.

For example, an AI coding assistant gives each user session its own MicroVM to safely execute generated code. An interactive notebook platform runs each student's code in an isolated MicroVM that persists state between interactions.

------

### Use
<a name="serverless-use"></a>

You should now have a clear understanding of each AWS serverless service and which one might be the best fit for your organization and use case. To explore how to use and learn more about each available service, the following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ Serverless compute ]

**AWS Lambda**
+ **Get started with AWS Lambda** Learn how to create your first Lambda function using the console. [Lambda getting-started tutorial](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
+ **Using AWS Lambda with other services** Explore common use cases and learn how Lambda integrates with other AWS services. [Lambda service integrations](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
+ **Serverless Patterns Workshop** Build a serverless microservice with Lambda, API Gateway, and DynamoDB in a hands-on workshop. [Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns) on the AWS Workshops website.
+ **AWS Lambda Pricing** Understand the per-request and per-duration pricing model. [Lambda pricing page](https://aws.amazon.com/lambda/pricing/)

**AWS Fargate**
+ **Getting started with Fargate on Amazon ECS** Learn how to run containers on Fargate without managing servers. [Fargate getting-started guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
+ **Creating a cluster with a Fargate Linux task using the AWS CLI** Set up a cluster, register a task definition, and run a task. [Fargate CLI tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html)

**Lambda MicroVMs**
+ **Create your first MicroVM** Build an isolated execution environment with VM-level isolation. [MicroVMs getting-started guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html)

------
#### [ API layer ]

**Amazon API Gateway REST API**
+ **Build a REST API with Lambda integration** Create a REST API that integrates with a Lambda function. [REST API with Lambda tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html)
+ **Controlling and managing access to a REST API** Learn about authentication and authorization options. [REST API access control guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)

**Amazon API Gateway HTTP API**
+ **Build an HTTP API with Lambda and DynamoDB** Create a low-latency, low-cost HTTP API with a Lambda backend. [HTTP API with DynamoDB tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
+ **Choosing between REST APIs and HTTP APIs** Understand the feature and pricing differences between the two API types. [REST vs HTTP API comparison](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)

**AWS AppSync**
+ **Getting started with AWS AppSync** Build a GraphQL API with real-time data synchronization. [AppSync quickstart guide](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html)

**Lambda function URLs**
+ **Creating and managing Lambda function URLs** Add a dedicated HTTPS endpoint to a Lambda function without API Gateway. [Lambda function URLs guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)

------
#### [ Application integration ]

**Amazon Simple Queue Service**
+ **Getting started with Amazon SQS** Create a queue, send messages, and receive messages using the console. [SQS getting-started guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+ **Orchestrate Queue-based Microservices** Design a serverless workflow that orchestrates a message queue-based microservice. [Queue-based microservices tutorial](https://aws.amazon.com/getting-started/hands-on/orchestrate-microservices-with-message-queues-on-step-functions/) on the AWS website

**Amazon Simple Notification Service**
+ **Getting started with Amazon SNS** Create a topic, subscribe endpoints, and publish messages. [SNS getting-started guide](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)
+ **Send Fanout Event Notifications** Implement a fanout messaging scenario using Amazon SNS and Amazon SQS. [Fanout notifications tutorial](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/) on the AWS website

**Amazon EventBridge**
+ **Getting started with Amazon EventBridge** Create a basic rule that routes events to a target. [EventBridge getting-started guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html)
+ **Building event-driven architectures workshop** Learn event-driven design with EventBridge and other serverless services. [Event-Driven Architecture Workshop](https://event-driven-architecture.workshop.aws/) on the AWS Workshops website.

------
#### [ Orchestration ]

**AWS Step Functions**
+ **Getting started with AWS Step Functions** Create a basic workflow for processing credit card applications. [Step Functions tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)
+ **AWS Step Functions Workshop** Explore the primary features of Step Functions through interactive modules. [Step Functions Workshop](https://catalog.workshops.aws/stepfunctions/en-US) on the AWS Workshops website.
+ **Standard vs. Express Workflows** Understand differences between Standard and Express workflow types. [Standard vs Express guide](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
+ **Design Patterns for AWS Step Functions** Learn how to implement design patterns in your state machines. [Design Patterns for Step Functions](https://explore.skillbuilder.aws/learn/course/external/view/elearning/10471/design-patterns-for-aws-step-functions) on AWS Skill Builder.

------
#### [ Data storage ]

**Amazon DynamoDB**
+ **Getting started with DynamoDB** Create a table, write, read, update, and query data using the AWS CLI. [DynamoDB getting-started tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)
+ **Choosing an AWS database service** Use our database decision guide for deeper guidance on database selection. [Database decision guide](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html)

**Amazon Simple Storage Service**
+ **Getting started with Amazon S3** Create a bucket, upload objects, and configure access. [S3 getting-started tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
+ **Using an Amazon S3 trigger to invoke a Lambda function** Process files automatically when they're uploaded to a bucket. [S3 trigger with Lambda tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)

**Amazon Aurora Serverless**
+ **Using Amazon Aurora Serverless v2** Learn how Amazon Aurora Serverless automatically adjusts capacity based on demand. [Aurora Serverless v2 guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)

------
#### [ Deployment and IaC ]

**AWS Serverless Application Model**
+ **Getting started with AWS Serverless Application Model** Initialize, build, and deploy a serverless application with the SAM CLI. [SAM getting-started tutorial](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)
+ **Testing locally with SAM CLI** Invoke Lambda functions locally and run API Gateway locally for development. [SAM CLI local testing guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local.html)

**AWS Cloud Development Kit (AWS CDK)**
+ **Getting started with the AWS Cloud Development Kit (AWS CDK)** Create your first CDK app and deploy infrastructure using your preferred programming language. [CDK getting-started tutorial](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

**Terraform**
+ **Getting started with Terraform on AWS** Learn how to provision AWS infrastructure with Terraform. [Terraform getting-started tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) on the HashiCorp website.

------
#### [ Observability ]

**Amazon CloudWatch**
+ **Getting started with CloudWatch** Set up dashboards, alarms, and log groups for your serverless application. [CloudWatch getting-started guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html)

**AWS X-Ray**
+ **Getting started with AWS X-Ray** Trace requests across Lambda, API Gateway, and downstream services. [X-Ray getting-started guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html)
+ **Choosing an AWS monitoring and observability service** Use our monitoring decision guide for deeper guidance on observability tooling. [Monitoring decision guide](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/monitoring-on-aws-how-to-choose.html)

------

### Explore
<a name="serverless-explore"></a>

Once you have determined which approach best fits your workload, review these resources to help you begin implementing. You can find service-specific resources in the previous section, and general serverless architecture resources in the following section.
+ **Architecture diagrams** Explore reference architecture diagrams for serverless on AWS. [ Explore architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/)
+ **Serverless Patterns Workshop** Build serverless microservices with hands-on exercises covering unit and integration testing, infrastructure as code, and common architectural patterns. [Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns) on the AWS Workshops website.
+ **Serverless Land** Explore serverless patterns, blogs, videos, and learning resources from the AWS serverless community. [Serverless Land patterns and resources](https://serverlessland.com/)
+ **Whitepapers** Explore whitepapers for serverless best practices, architecture guidance, and cost optimization. [ Explore whitepapers](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23serverless&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS Solutions** Explore vetted solutions and architectural guidance for common serverless use cases. [Explore solutions](https://aws.amazon.com/solutions/serverless/)

## Choosing an AWS application integration service
<a name="application-integration-on-aws-how-to-choose"></a>

**Taking the first step**


|  |  | 
| --- |--- |
| **Purpose** | Help determine which AWS application integration services are the best fit for your workloads. | 
| **Last updated** | April 16, 2025 | 
| **Covered services** |  +  [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) <br />+  [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) <br />+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) <br />+  [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-getting-started.html) <br />+  [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html) <br />+  [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) <br />+  [Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) <br />+  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)   | 

### Introduction
<a name="intro"></a>

Application integration is a suite of services that enables communication between decoupled components within microservices, distributed systems, and serverless applications. Amazon Web Services (AWS) offers more than half a dozen application integration services to support a diverse set of workloads running in the cloud.

Choosing an integration service that is the best fit for your organization and workloads can become difficult. This decision guide will help you ask the right questions to discover your requirements and provides clear guidance on how to evaluate and choose the right integration services for your workloads.

[![AWS Videos](https://img.youtube.com/vi/Zrj7RD7G24Q?start=58&end=567/0.jpg)](https://www.youtube.com/watch?v=Zrj7RD7G24Q?start=58&end=567)


### Understand
<a name="understand"></a>

One of the key benefits of modernization is the ability to shift operational responsibilities, allowing you to free up resources to do more value-add and innovation-led activities.

There is a spectrum of shared responsibility options across different levels of modernization, ranging from hosting your message broker on Amazon Elastic Compute Cloud (Amazon EC2)—where you are managing scaling, security configurations, provisioning, patching, and more—to serverless offerings where all of the underlying infrastructure is managed.

![Diagram showing operational responsibility between AWS application integration services.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/operational-responsibility.png)


As you start to explore and understand your criteria, environment, and the suite of integration services that AWS offers, we recommend that you review some best practices. These best practices are applicable regardless of which service (or suite of services) you choose.

**Understand integration in your environment**

It's common that some organizations spend more time than they would like on maintaining open-source integrations. We recommend that you consider community sources, and/or backing from enterprises or foundations when making these investments. An investment in these projects is not just financial, but also an investment in knowledge capital and potentially technical debt, as these components and associated integrations will typically need updating. For more information, see the [AWS Open Source blog](https://aws.amazon.com/blogs/opensource/).

**Understand your architecture characteristics**

The ability to support a wide range of architectures is important. We recommend that you use the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) as a guide to help you understand the decisions you make when building architectures on AWS. Additionally, using the Well-Architected Framework allows you to learn architectural best practices for designing and operating reliable, scalable, secure, efficient, and cost-effective systems in the Cloud.

**Use a combination of integration services**

If you are using purpose-built services, a combination of services might be the best fit for your use case. The following lists out a few common ways AWS customers are using a combination of services.
+ Routing Amazon EventBridge or Amazon Simple Notification Service (Amazon SNS) events to an Amazon Simple Queue Service (Amazon SQS) queue as a buffer for downstream consumers.
+ Pulling events directly from a stream (Amazon Kinesis Data Streams or Amazon Managed Streaming for Apache Kafka (Amazon MSK)) or a queue (Amazon SQS or Amazon MQ) with EventBridge Pipes and sending events to an EventBridge bus to push out to consumers.
+ Routing EventBridge or Amazon SNS events to a Kinesis Data Streams or Amazon MSK for gathering and viewing analytics.

### Define
<a name="define"></a>

Once you have a clearer picture of your criteria, environment, strategic direction, and available services (including both deployment hosted and managed modalities), you need to identify your integration requirements. You might already know some of your requirements if you are migrating to an existing integration platform or message broker. However, you need to establish how these requirements would change if you move to a cloud environment, if at all. 

**Messaging or streaming platforms**

These platforms are expected to fulfill a certain business functionality. Use the following example use cases when considering which functionalities you will need. 

**Example 1:**

Consider an insurance company which receives different claims as messages for different claim types (auto, home, or life) with different business rules. It might mean that the message consumer should have the functionality to route claims to a different destination based on header properties in the message.

**Example 2:**

Consider an airline in which a flight status update needs to notify all connected systems such as baggage or gate operations using a protocol such as Advanced Messaging Queuing Protocol (AMQP). The big question with functional and business use case primitives is what constitutes a best fit messaging platform. We have multiple choices that can determine the suitability of the platform based on the use case.
+ **Market adoption:** This platform is widely adopted by a huge customer community and a good enough fit for most use cases. It is tried and tested with a vibrant support community for any issues that might be encountered. It is a low-risk decision with enough training available for the development resources.
+ **Best fit for use case: **These platforms will be tailored for specific industry use cases such as airlines, logistics, or healthcare. They might be the best fit for those use cases with ready-made templates available for adoption. These platforms can be easy to get started but can lack the level of adoption in the market as well as flexibility. Adopting this type of platform might require extensive time and resources for validation and building in house expertise.
+ **Modern: ** These platforms are built with the next generation architecture to address cloud-scale deployments, multi-tenancy, disaster recovery, and serverless type of pricing. Using this type of platform might require some refactoring of workloads for long-term viability. It uses a cloud-native platform and focuses on using the well-architected principles of modern applications.

**Example 3:**

If the messaging platform is part of a bigger loan processing workflow which needs to be multi-region, the messaging platform also needs to support the same business requirements. If the business needs the ability to recover and rollback to a previous state in rainy day situations, the underlying messaging or streaming platform also needs capability to have some snapshotting or replay capability to recreate the state of the system.

The integration platform you choose should facilitate asynchronous processing of loan applications or act as the store and forward channel for a multi-step media processing workflow. The criticality of the business process would determine the capabilities needed from the messaging or streaming platform.

### Consider
<a name="consider"></a>

When considering a major application integration architecture in the cloud, there are different ways to determine the functional requirements for each of the integration points. 

The following is some of the criteria to consider when choosing an application integration service. 

------
#### [ Managed service and operation overhead ]

Consider moving to the cloud to reduce operational cost by standardizing on managed services that shift the operational burden to AWS. Higher levels of abstraction allow developers and operators to focus on their own unique value-add activities, instead of undifferentiated tasks.

------
#### [ Open source ]

Consider standardization on [open source technologies](https://aws.amazon.com/blogs/opensource/category/application-integration/). Open source can enable an organization to find the right skills—and avoid some risk around lock-in.

 Making the wrong choices in an open-source ecosystem can lead to being locked into abstractions and homegrown integrations. Additionally, the responsibility for making different open-source components work together often sits with the organization making the choice. This can lead to organizations to spending significant time maintaining open-source integrations.

------
#### [ Workload characteristics ]

When choosing the right integration service, it is important to understand the characteristics of the messages that need to be sent between the applications. Key characteristics like the message format, size, retention and priority can drive the decision of the integration service.

 Some integration services are better suited for small text based messages whereas some are designed to support multiple formats such as text and binary and offer bigger message sizes. The need to have a replay capability can also be an important factor alongside ordering of messages in some scenarios.

 For example, message ordering can be implemented by using the FIFO functionality offered by Amazon SNS and Amazon SQS. There is also a consideration of having a pull or push based architecture, such as EventBridge or Amazon SNS invoking a Lambda function asynchronously.

 A pull based architecture could use services such as Amazon SQS or Kinesis Data Streams, where messages are stored on a queue or a stream and then can be retrieved by a consuming system. Messaging services like Amazon MQ offer capabilities around bigger message payloads and have unlimited retention. However, they do not offer replay capability.

------
#### [ Rapid iteration and feature velocity ]

If your primary focus is building and iterating quickly, serverless services might provide the best value. Serverless services let you build applications without managing infrastructure. They provide managed functionality and integrations to reduce time spent writing boiler plate code.

Another benefit of serverless when testing new ideas is that these services offer usage based pricing. Your code only runs when the service is invoked, so an experiment does not require an upfront investment.

------
#### [ Application portability ]

Many applications use certain protocols - such as Advanced Message Queuing Protocol (AMQP) or MQ Telemetry Transport (MQTT) - to connect to a messaging service. Alternatively, they have some library dependency which uses a certain messaging protocol. Examples of such libraries or frameworks include Spring Boot, Celery, or MassTransit.

 You might want to preserve such applications for different reasons. In these cases, the choice of your integration service also depends on the support of the required protocols to have portability with your applications.

------
#### [ Automation portability ]

You might need to have a service that provides compatibility with your infrastructure and deployment tools - and run the same integration system that you host on-premises (such as Apache ActiveMQ, RabbitMQ, and Apache Kafka).

 Managed open source services (such as Amazon MQ and Amazon MSK) provide the benefits of the cloud, while being compatible with many popular deployment tools used for on-premises deployments.

 If refactoring the application is an option, you can benefit from using serverless services for providing this capability natively, as well as rich integration with a variety of AWS services.

------
#### [ Organization size and skills ]

The skills of your organization are a major factor when deciding on the right integration service. If your teams are familiar with a self managed product and it meets your needs, then having a managed service for the same provides the path of least impact. Doing so, can help you apply the best practices for the service and focus on value add activities.

------

### Choose
<a name="choose"></a>

Now that you know the criteria you will use to evaluate your application integration needs, you are ready to choose which AWS service or services are right for your workloads in your environment.



| Service type | When would you use it? | What is it optimized for? | Associated services | 
| --- |--- |--- |--- |
| Capacity | Use when you need to decouple publishers and subscribers and send events to multiple subscribers simultaneously. | Optimized for asynchronous, loosely coupled communication between publishers and subscribers. Events provide flexibility in message routing and delivery and are well-suited for event-driven architectures where events play a central role in initiating actions or workflows. | [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html)<br />[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) | 
|  Messaging  |  Use when you need either pub/sub messaging to broadcast messages to multiple recipients simultaneously, or point-to-point messaging when you need reliable and asynchronous communication between components.  |  Optimized for high-throughput, scalable, and reliable asynchronous pub/sub and point-to-point messaging between distributed components.  |  [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-getting-started.html)  | 
| --- |--- |--- |--- |
| Streaming | Use streaming services such as Amazon Kinesis Data Streams and Amazon Managed Streaming for Apache Kafka (MSK) in scenarios that involve handling and processing real-time streaming data. | Optimized for ingesting, processing, and analyzing large volumes of real-time streaming data for use cases that require real-time analytics, real-time monitoring, data exploration, and other applications that demand the processing of high-velocity data streams. | [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)<br />[Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) | 
|  Workflows  |  Use when you need to design, coordinate, and manage workflows or sequences of tasks in an organized and scalable manner.  |  Optimized for use cases such as business process management, application orchestration, data pipeline automation, and microservices coordination. Workflows abstract the underlying infrastructure complexity, allowing you to focus on designing and managing your workflows effectively. They are capable of handling dependencies and sequencing, allowing for parallelism and conditional branching while providing fault tolerance, error handling, and retries to ensure reliable workflow execution.  |  [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) [Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)  | 
| --- |--- |--- |--- |
| Scheduling | Use scheduling when you need to automate routine tasks such as data processing, backups, or system health checks. Tasks often need to be run at specific times or intervals, such as every night, hour, or minute. | Optimized for reliable, time-based tasks with built-in retry logic. Suitable for workflows requiring precise scheduling and integration with various AWS services. | [Amazon EventBridge](https://docs.aws.amazon.com/scheduler/latest/UserGuide/getting-started.html) | 

### Use
<a name="use"></a>

You should now have a clear understanding of what each AWS application integration service does—and which one might be right for you. To explore how to use and learn more about each of the available AWS application integration services—we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ Amazon SNS ]
+ **Filter Messages Published to Topics with Amazon SNS and Amazon SQS**

  Learn how to use the message filtering feature of Amazon SNS. 

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/filter-messages-published-to-topics/)
+ **Amazon SNS - Troubleshooting**

  Learn how to view configuration information, monitor processes, and gather diagnostic data about Amazon SNS.

  [Explore the guide](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14124/amazon-simple-notification-service-amazon-sns-troubleshooting)
+ **Build a turn-based game with Amazon DynamoDB and Amazon SNS**

  Learn how to build a multiplayer, turn-based game using Amazon DynamoDB and Amazon Amazon SNS.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/turn-based-game-dynamodb-amazon-sns/)
+ **Building event driven architectures**

  Learn how to build on a simple pub/sub implementation using Amazon SNS as our publishing service and Amazon SQS as a subscriber.

  [Explore the guide](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US/sns)
+ **Archiving and replaying messages with Amazon SNS FIFO**

  Learn how to archive and replay messages published to Amazon SNS FIFO, which can be useful in failure recovery and state replication scenarios.

  [Read the blog post](https://aws.amazon.com/blogs/compute/archiving-and-replaying-messages-with-amazon-sns-fifo/)

------
#### [ Amazon SQS ]
+ **Getting started with Amazon SQS**

  This guide shows you how to manage queues and messages using the Amazon SQS console.

  [Explore the guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+ **Send Fanout Event Notifications**

  Learn how to implement a fanout messaging scenario using Amazon SNS and Amazon SQS. 

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/)
+ **Orchestrate Queue-based Microservices**

  Learn how to design and run a serverless workflow that orchestrates a message queue-based microservice.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/orchestrate-microservices-with-message-queues-on-step-functions/)
+ **Send Messages Between Distributed Applications**

  Use the Amazon SQS console to create and configure a message queue, send a message, receive and delete that message, and then delete the queue.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/send-messages-distributed-applications/)

------
#### [ Amazon EventBridge ]
+ **Get started with Amazon EventBridge**

  The basis of EventBridge is to create rules that route events to a target. In this guide, you create a basic rule.

  [Explore the guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html)
+ **Amazon EventBridge get started tutorials**

  These tutorials will help you explore the features of EventBridge and how to use them.

  [Get started with the tutorials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-gs-tutorials.html)
+ **Integrating with other AWS services**

  The following tutorials show you how to integrate EventBridge with other AWS services.

  [Get started with the tutorials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-aws-tutorials.html)
+ **Build event-driven architectures**

  Learn the basics of event-driven design, how to choose the right AWS service for the job, as well as how to optimize for both cost and performance.

  [Get started with the tutorial](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US/)
+ **Building event-driven applications with Amazon EventBridge**

  Learn how to build event-driven applications by connecting multiple applications, including SaaS applications and AWS services, using the serverless event bus provided by Amazon EventBridge.

  [Get started with the tutorial](https://explore.skillbuilder.aws/learn/course/external/view/elearning/15008/building-event-driven-applications-with-amazon-eventbridge)
+ **Kafka connector for Amazon EventBridge**

  This connector allows you to convert records from one or more Kafka topics into events, and send those events to the event bus of your choice.

  [Explore the guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/kafka-connector.html)
+ **Introducing cross-account targets for Amazon EventBridge Event Buses**

  Learn how you can use Event Buses to send events directly to targets in other AWS accounts, such as Amazon SQS, Amazon SNS, and AWS Lambda.

  [Read the blog post](https://aws.amazon.com/blogs/compute/introducing-cross-account-targets-for-amazon-eventbridge-event-buses/)

------
#### [ Amazon MQ ]
+ **Create a connected message broker**

  Learn how to set up an Amazon MQ message broker and connect a Java application without rewriting your code.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/create-a-connected-message-broker/)
+ **Migrate to a message broker in the cloud **

  Amazon MQ makes it easy to migrate to a message broker in the cloud, such as Apache ActiveMQ and RabbitMQ.

  [Read the guide](https://docs.aws.amazon.com/amazon-mq/latest/migration-guide/concept-chapter-about.html)
+ **Creating and connecting to a RabbitMQ broker**

  Learn how you can use the AWS Management Console to create a RabbitMQ broker and attach your application to it.

  [Get started with the tutorial](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-rabbitmq.html)
+ **RabbitMQ workshop**

  This workshop is a collection of labs covering different aspects and patterns of messaging using RabbitMQ.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/88db3818-a8bb-4f5c-acf9-e57fa7a129b6/en-US)
+ **Introducing quorum queues in Amazon MQ for RabbitMQ**

  Discover how using quorum queues with RabbitMQ can provide higher availability and data security.

  [Read the blog post](https://aws.amazon.com/blogs/compute/introducing-quorum-queues-on-amazon-mq-for-rabbitmq/)
+ **Creating and connecting to an ActiveMQ broker**

  Learn how you can use the AWS Management Console to create a basic broker.

  [Get started with the tutorial](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-activemq.html)
+ **ActiveMQ workshop**

  Explore messaging concepts such as queues, topics and features of Amazon MQ such as failover, network of brokers.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/0b534eb9-fdfb-49f0-8df4-ebccca71a9eb/en-US)
+ **Deploy and publish to an Amazon MQ broker using AWS serverless**

  We walk you through deploying a serverless backend and an Amazon MQ broker in one step using the AWS SAM.

  [Read the blog post](https://aws.amazon.com/blogs/compute/deploy-and-publish-to-an-amazon-mq-broker-using-aws-serverless/)
+ **Measuring Amazon MQ throughput using Maven 2 benchmark and AWS CDK**

  Learn how to evaluate the throughput for Amazon MQ using the ActiveMQ Classic Maven Performance test plugin.

  [Read the blog post](https://aws.amazon.com/blogs/compute/measuring-amazon-mq-throughput-using-maven-2-benchmark-and-aws-cdk/)

------
#### [ Amazon Kinesis Data Streams ]
+ **Getting started with Amazon Kinesis Data Streams **

  Learn fundamental Kinesis Data Streams data flow principles and the steps necessary to put and get data from an Kinesis data stream.

  [Explore the guide](https://docs.aws.amazon.com/streams/latest/dev/getting-started.html)
+ **Build highly available streams with Amazon Kinesis Data Streams**

  We compare and contrast different strategies for creating a highly available Kinesis data stream in case of service interruptions, delays, or outages in the primary Region of operation.

  [Read the blog post](https://aws.amazon.com/blogs/big-data/build-highly-available-streams-with-amazon-kinesis-data-streams/)
+ **Example Tutorials for Amazon Kinesis Data Streams**

  These tutorials are designed to further assist you in understanding Amazon Kinesis Data Streams concepts and functionality.

  [Get started with the tutorials](https://docs.aws.amazon.com/streams/latest/dev/examples.html)
+ **Using AWS Lambda with Amazon Kinesis**

  Learn how to create a Lambda function to consume events from a Kinesis stream.

  [Get started with the tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html)
+ **Real Time Streaming with Amazon Kinesis**

  Explore a series of lab exercises which help users build a streaming analytics application on AWS.

  [Get started with the tutorials](https://catalog.us-east-1.prod.workshops.aws/workshops/2300137e-f2ac-4eb9-a4ac-3d25026b235f/en-US)

------
#### [ Amazon MSK ]
+ **Getting started using Amazon MSK**

  This tutorial shows you an example of how you can create an MSK cluster, produce and consume data, and monitor the health of your cluster using metrics.

  [Get started with the tutorial](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html)
+ **Getting started using MSK Serverless clusters **

  This tutorial shows you an example of how you can create an MSK Serverless cluster, create a client machine that can access it, and use the client to create topics on the cluster and to write data to those topics.

  [Get started with the tutorial](https://docs.aws.amazon.com/msk/latest/developerguide/serverless-getting-started.html)
+ **Amazon MSK Labs**

  These labs can either be run on personal or corporate AWS accounts or accounts provisioned by AWS Account teams for events that use workshop studio.

  [Get started with the labs](https://catalog.workshops.aws/msk-labs/en-US)
+ **Introducing Express brokers for Amazon MSK to deliver high throughput and faster scaling for your Kafka cluster**

  Learn how Express brokers can lower costs, provide higher resiliency, and lower operational overhead for your Kafka workloads. 

  [Read the blog post](https://aws.amazon.com/blogs/aws/introducing-express-brokers-for-amazon-msk-to-deliver-high-throughput-and-faster-scaling-for-your-kafka-clusters/)

------
#### [ AWS Step Functions ]
+ **Getting started with AWS Step Functions**

  These tutorials walk you through creating a basic workflow for processing credit card applications.

  [Get started with the tutorials](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)
+ **Introduction to Step Functions**

  This course introduces the key components of Step Functions to help you get started managing workflows within an application.

  [Get started with the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8819/introduction-to-step-functions)
+ **Large-scale data processing with AWS Step Functions**

  Learn how large-scale data processing applications can be built using Step Functions.

  [Get started with the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2a22e604-2f2e-4d7b-85a8-33b38c999234/en-US)
+ **Design Patterns for AWS Step Functions**

  Learn how to implement design patterns in your Step Functions state machines and why to use each one.

  [Get started with the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/10471/design-patterns-for-aws-step-functions)
+ **Schedule a Serverless Workflow with AWS Step Functions and Amazon EventBridge Scheduler**

  We show you how to invoke a state machine using EventBridge Scheduler based on the schedule you define.

  [Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/scheduling-a-serverless-workflow-step-functions-amazon-eventbridge-scheduler/)
+ **AWS Step Functions Workshop**

  Learn how to use the primary features of AWS Step Functions through a series of interactive modules.

  [Get started with the workshop](https://catalog.workshops.aws/stepfunctions/en-US)
+ **Securely share AWS resources across VPC and account boundaries with PrivateLink, VPC Lattice, EventBridge, and Step Functions**

  Learn how to share AWS resources, such as EC2 instances and Amazon EKS container services, across Amazon VPC and AWS account boundaries with AWS Step Functions.

  [Read the blog post](https://aws.amazon.com/blogs/aws/securely-share-aws-resources-across-vpc-and-account-boundaries-with-privatelink-vpc-lattice-eventbridge-and-step-functions/)
+ **Simplifying developer experience with variables and JSONata in AWS Step Functions**

  Explore using variables and JSONata, an open source query and transformation language, to simplify data sharing across states and reduce the complexity of data manipulation.

  [Read the blog post](https://aws.amazon.com/blogs/compute/simplifying-developer-experience-with-variables-and-jsonata-in-aws-step-functions/)

------
#### [ Amazon MWAA ]
+ **Get started with Amazon Managed Workflows for Apache Airflow**

  This guide describes the prerequisites and the required AWS resources needed to get started with Amazon MWAA.

  [Explore the guide](https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html)
+ **Configuring the `aws-mwaa-local-runner` in a CD pipeline**

  This tutorial guides you through the process of building a continuous delivery (CD) pipeline in GitHub using Amazon Managed Workflows for Apache Airflow's `aws-mwaa-local-runner` to test your Apache Airflow code locally.

  [Get started with the tutorial](https://docs.aws.amazon.com/mwaa/latest/userguide/tutorials-docker.html)
+ **Restricting an Amazon MWAA user's access to a subset of DAGs**

  We show how you can restrict individual Amazon MWAA users to only view and interact with a specific DAG or a set of DAGs.

  [Get started with the tutorial](https://docs.aws.amazon.com/mwaa/latest/userguide/limit-access-to-dags.html)
+ **Amazon MWAA for Analytics Workshop**

  Learn to build and orchestrate data and ML pipelines that include many of the above mentioned services, and with that you will gain familiarity and a better understanding of the hooks and operators available as part of Airflow to manage your pipelines/workflows on AWS.

  [Get started with the workshop](https://catalog.workshops.aws/amazon-mwaa-for-analytics/en-US)

------

### Explore
<a name="explore"></a>

Once you have determined which approach best fits your workload for your environment, we recommend that you review these resources to help you begin implementing your approach. You can find service-specific resources in the previous section, and general event-driven architecture resources in the following section.
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you create a highly available, secure, flexible, and cost effective architectures.

  [ Explore architecture diagrams](https://aws.amazon.com/architecture/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23app-integration&awsf.industries=*all&awsf.business-category=*all)
+ **Whitepapers**

  Explore whitepapers to help you get started, and learn best practices around event driven architectures.

  [Explore whitepapers ](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23app-integration&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all&awsm.page-whitepapers-main=1)
+ **Blogs**

  Explore blogs to help you stay up to date on the latest technologies, and modernize your applications.

  [Explore blogs](https://aws.amazon.com/blogs/?awsf.blog-master-category=category%23application-integration&awsf.blog-master-learning-levels=*all&awsf.blog-master-industry=*all&awsf.blog-master-analytics-products=*all&awsf.blog-master-artificial-intelligence=*all&awsf.blog-master-aws-cloud-financial-management=*all&awsf.blog-master-blockchain=*all&awsf.blog-master-business-applications=*all&awsf.blog-master-compute=*all&awsf.blog-master-customer-enablement=*all&awsf.blog-master-customer-engagement=*all&awsf.blog-master-database=*all&awsf.blog-master-developer-tools=*all&awsf.blog-master-devops=*all&awsf.blog-master-end-user-computing=*all&awsf.blog-master-mobile=*all&awsf.blog-master-iot=*all&awsf.blog-master-management-governance=*all&awsf.blog-master-media-services=*all&awsf.blog-master-migration-transfer=*all&awsf.blog-master-migration-solutions=*all&awsf.blog-master-networking-content-delivery=*all&awsf.blog-master-programming-language=*all&awsf.blog-master-sector=*all&awsf.blog-master-security=*all&awsf.blog-master-storage=*all)

## Amazon SQS, Amazon SNS, or Amazon EventBridge?
<a name="sns-or-sqs-or-eventbridge"></a>

**Understand the differences and pick the one that's right for you** 


|  |  | 
| --- |--- |
| **Purpose** | Understand the differences between Amazon SQS, Amazon SNS, and EventBridge and determine which service is the best fit for your needs. | 
| **Last updated** | November, 2025 | 
| **Covered services** |  +  [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) <br />+  [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) <br />+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)   | 

### Introduction
<a name="introduction"></a>

 This decision guide helps you to choose the best AWS service for message handling, event-driven architectures, and decoupling components for your application. AWS offers three key services for these purposes: 
+  **Amazon SQS** is a fully managed message queuing service that enables decoupling and scaling of microservices, distributed systems, and serverless applications. 
+  **Amazon SNS** is a fully managed publish-subscribe (pub/sub) messaging model that delivers messages to subscribed endpoints such as HTTP/HTTPS endpoints, email addresses, SMS, Amazon SQS queues, and AWS Lambda functions. 
+  **Amazon EventBridge**(formerly known as CloudWatch Events) is a fully managed event bus service for event-driven architectures that can send and receive event data from a variety of sources including Lambda functions, Amazon SQS queues, Amazon SNS topics, and integrated SaaS applications. 

All three of these services facilitate communication between decoupled components, but differ in underlying architecture, use cases, and capabilities.

The following table compares these services at a high level.


|  **Category**  |  **Amazon SQS**  |  **Amazon SNS**  |  **EventBridge**  | 
| --- | --- | --- | --- | 
|  Communication model  |  Pull-based (consumers poll messages from the queue)  |  Push-based (subscribers receive messages when published)  |  Event-driven (rules match events and route to targets)  | 
|  Persistence  |  Messages persist until consumed or expired  |  Messages do not persist; delivered in real-time to subscribers  |  Events do not persist; processed in real-time  | 
|  Delivery guarantees  |  At-least-once delivery  |  At-least-once delivery for HTTP/S, exactly-once for Lambda and Amazon SQS  |  At-least-once delivery  | 
|  Message ordering  |  FIFO (First-In-First-Out) queues ensure strict ordering  |  Amazon SNS FIFO topics guarantee order  |  No ordering guarantees  | 
|  Message filtering  |  Amazon SQS can’t decide consumer based on message. Use Amazon SNS message filtering with Amazon SQS to achieve.  |  Message filtering using subscription filter policies based on message metadata and for FIFO topics, message content  |  Complex event pattern matching and content-based filtering  | 
|  Supported subscribers  |  Pull-based consumers (such as Amazon EC2 or Lambda)  |  HTTP/S endpoints, email, SMS, mobile push, Lambda, Amazon SQS  |  AWS services, Lambda, API destinations, event buses in other AWS accounts  | 
|  Typical use cases  |  Decoupling microservices, buffering requests, processing tasks asynchronously  |  Fanout notifications, pub/sub messaging, mobile push notifications  |  Event-driven architectures, real-time stream processing, cross-account event sharing  | 
|  Integration with other AWS services  |  Lambda, CloudWatch, AWS KMS, IAM  |  Lambda, Amazon SQS, Mobile Push, AWS KMS, IAM  |  Lambda, Step Functions, Amazon SQS, Amazon SNS, Kinesis, SageMaker AI, CloudWatch, IAM  | 

### Details on the differences
<a name="sqs-sns-eb-differences"></a>

 The following tabbed sections compare Amazon SQS, Amazon SNS, and EventBridge in eight key areas. 

------
#### [ Communication model ]

**Amazon SQS**

Pull-based model where consumers actively poll messages from the queue, allowing for fine-grained control over message processing rates and independent scaling of consumers. Amazon SQS supports both short polling (immediate response) and long polling, with a maximum wait time of up to 20 seconds. Long polling helps control the cost of using Amazon SQS by reducing the potential for empty responses.

**Amazon SNS**

 Push-based model that delivers messages to subscriptions such as HTTP/HTTPS endpoints, email addresses, SMS, Amazon SQS queues, and AWS Lambda functions. Messages are delivered asynchronously with built-in retry logic and dead-letter queue support. 

**Amazon EventBridge**

 Event-driven model that matches events against rules, delivering messages to targets such as AWS services, integrated SaaS applications, and custom applications, enabling loosely-coupled, event-driven architectures. 

------
#### [ Persistence and delivery guarantees ]

**Amazon SQS**

Messages are persisted in the queue until successfully processed or expired (up to 14 days retention). Provides at-least-once delivery, guaranteeing that every message is delivered at least once, with the possibility of duplicates.

**Amazon SNS**

Messages are not persisted and are delivered to subscribers in real-time. Offers at-least-once delivery for HTTP/S subscribers and exactly-once delivery for Lambda and Amazon SQS subscribers. 

**Amazon EventBridge**

Amazon EventBridge processes events in real-time and doesn't persist events. At-least-once delivery is guaranteed to targets, which means events may be delivered multiple times. By default, Amazon EventBridge retries sending events for 24 hours and up to 185 times with an exponential back off and jitter, or randomized delay.

------
#### [ Message ordering ]

**Amazon SQS and Amazon SNS**

Amazon SQS FIFO queues and Amazon SNS FIFO topics support First-In-First-Out guaranteed message ordering, making them suitable for scenarios requiring sequential processing. See [message ordering details for FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/fifo-topic-message-ordering.html) for more information on message ordering using Amazon SNS and Amazon SQS.

**Amazon EventBridge**

EventBridge does not provide message ordering guarantees, instead delivering events to targets in an arbitrary order.

------
#### [ Message filtering and routing ]

**Amazon SQS**

Offers basic filtering capabilities through visibility timeouts (to prevent duplicate processing) and dead-letter queues (to handle failed messages). 

**Amazon SNS**

Provides message filtering using subscription filter policies, allowing subscribers to selectively receive messages based on message attributes. 

**Amazon EventBridge**

Supports advanced event pattern matching and content-based filtering, enabling fine-grained event processing and routing based on event content. 

------
#### [ Supported subscribers and integrations ]

**Amazon SQS**

Supports pull-based consumers, such as Amazon EC2 instances or Lambda functions, which actively retrieve messages from the queue. 

**Amazon SNS**

Supports a wide range of subscribers, including HTTP/S endpoints, email, SMS, mobile push notifications, Lambda functions, and Amazon SQS queues. 

**Amazon EventBridge**

Integrates with numerous AWS services, such as Lambda, Step Functions, Amazon SQS, Amazon SNS, Kinesis, and SageMaker AI, allowing event routing based on predefined rules. EventBridge also has numerous built-in integrations with third party products such as PagerDuty, DataDog, New Relic. To see the complete list visit [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html). 

------
#### [ Typical use cases ]

**Amazon SQS**

Commonly used for decoupling microservices, buffering requests, and processing tasks asynchronously, enabling independent scaling and graceful failure handling. 

**Amazon SNS**

Often used for fanout notifications, pub/sub messaging, and mobile push notifications, facilitating the broadcasting of messages to multiple subscribers simultaneously. 

**Amazon EventBridge**

Ideal for building event-driven architectures, real-time stream processing, and cross-account event sharing, allowing reactive systems to be built across multiple services. 

------
#### [ Scalability and performance ]

**Amazon SQS**

Highly scalable, automatically scaling based on the number of messages and consumers, providing high throughput for message processing. 

**Amazon SNS**

Highly scalable, capable of delivering messages to a large number of subscribers, with elastic scaling to handle increasing publish and subscribe demands. 

**Amazon EventBridge**

Automatically scales based on incoming event traffic, offering low-latency event processing and near real-time delivery to targets. 

------
#### [ Pricing ]

**Amazon SQS**

Pricing based on the number of API requests and data transferred, with a free tier including a monthly allowance of free API requests and data transfer. 

**Amazon SNS**

Pricing is based on the number of API requests, notifications delivered, and data transferred. Amazon SNS SMS messages are billed through AWS End User Messaging. 

**Amazon EventBridge**

Pricing based on the number of events published and target invocations, with a free tier that includes a monthly allowance of free events and invocations. 

------

### Use
<a name="use"></a>

------
#### [ Amazon SQS ]
+  **Get started with Amazon SQS** 

  Get step-by-step instructions on setting up and using Amazon SQS. It covers topics such as creating a queue, sending and receiving messages, and configuring queue properties.

  [Explore the guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) 
+  **Amazon SQS tutorial** 

  Walk through a practical example of using Amazon SQS to decouple the components of a simple application. It demonstrates how to create a queue, send messages to the queue, and process messages from the queue using AWS SDKs.

  [Explore the tutorial](https://aws.amazon.com/getting-started/hands-on/send-messages-distributed-applications/) 
+  **Send Fanout Event Notifications** 

  Learn how to implement a fanout messaging scenario using Amazon SQS and Amazon SNS.

  [Explore the tutorial](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/)

------
#### [ Amazon SNS ]
+  **Get started with Amazon SNS** 

  A step-by-step walkthrough of setting up and using Amazon SNS. It covers topics such as creating a topic, subscribing endpoints to a topic, publishing messages, and configuring access permissions.

  [Explore the guide](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)  
+  **Amazon SNS - Troubleshooting** 

  Learn how to view configuration information, monitor processes, and gather diagnostic data about Amazon SNS.

  [Explore the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14124/amazon-simple-notification-service-amazon-sns-troubleshooting)

------
#### [ EventBridge ]
+  **Amazon EventBridge User Guide** 

  This comprehensive documentation covers topics such as creating event buses, defining event rules, setting up targets, and integrating with various AWS services. 

   [Explore the guide ](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
+  **Amazon EventBridge Tutorials** 

  The AWS documentation offers a series of tutorials that walk users through different use cases and scenarios using Amazon EventBridge. These tutorials cover topics like scheduling automated tasks, reacting to changes in AWS resources, and integrating with AWS services. 

   [Explore the tutorials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial.html)
+  **AWS Serverless Workshops - Event-Driven Architecture**

  Build event-driven architectures using Amazon EventBridge and other AWS serverless services. This workshop guides participants through the process of creating event buses, defining event rules, and triggering actions based on events. 

  [Explore the workshop](https://event-driven-architecture.workshop.aws/)
+  **AWS Online Tech Talk - Introduction to Amazon EventBridge** 

  Get an introduction to Amazon EventBridge, explaining key concepts, features, and use cases. The tech talk includes demonstrations and practical examples to help users understand how to leverage EventBridge in their applications. 

  [Watch the video](https://www.youtube.com/watch?v=TXh5oU_yo9M)
+  **Building Event-Driven Applications with Amazon EventBridge** 

  This blog post explores the process of building event-driven applications using Amazon EventBridge. It provides a step-by-step guide on creating event buses, defining event patterns, and setting up targets to process events.

   [Read the blog post](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/)
+  **Create Point-to-Point Integrations Between Event Producers and Consumers with Amazon EventBridge Pipes** 

  Explore Amazon EventBridge Pipes, a feature of EventBridge that makes it easier for you to build event-driven applications by providing a consistent and cost-effective way to create point-to-point integrations between event producers and consumers, removing the need to write undifferentiated glue code.

   [Read the blog post](https://aws.amazon.com/blogs/aws/new-create-point-to-point-integrations-between-event-producers-and-consumers-with-amazon-eventbridge-pipes/)

------

# Additional resources
<a name="additional-resources"></a>

The following resources can help you learn more about AWS services and make informed decisions about your architecture.
+ [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) — Provides architectural best practices for building secure, high-performing, resilient, and efficient infrastructure.
+ [AWS Architecture Center](https://aws.amazon.com/architecture/) — Provides reference architecture diagrams, vetted architecture solutions, and best practices.
+ [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) — Provides technical whitepapers and guides on a wide range of topics.
+ [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/) — Provides strategies, guides, and patterns to help you accelerate your cloud migration and modernization.
+ [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/) — Provides tutorials and resources to help you get started with AWS.
+ [AWS Documentation](https://docs.aws.amazon.com/) — Provides technical documentation for all AWS services.
+ [AWS Training and Certification](https://aws.amazon.com/training/) — Provides training courses and certification programs to build your AWS skills.

# Document history
<a name="document-history"></a>

The following table describes important changes to the *AWS Decision Guides*.


**Document history**  

| Change | Description | Date | 
| --- | --- | --- | 
| Updated Lightsail, Elastic Beanstalk, or EC2 guide | Updated the Amazon Lightsail, AWS Elastic Beanstalk, or Amazon EC2 decision guide to add AWS Elastic Beanstalk Cluster Mode (container deployments on Amazon EKS), Amazon Lightsail compute-optimized and memory-optimized instance families, Amazon ECS Express Mode and Amazon EKS Auto Mode, an AWS App Runner end-of-support note, Amazon EC2 Graviton4 families, and AWS Elastic Beanstalk AI-powered environment analysis. | September 29, 2026 | 
| Added serverless decision guide | Added a new decision guide: Choosing an AWS serverless service. Covers Lambda (Event Functions and MicroVMs), Fargate, API Gateway (HTTP, REST, and WebSocket APIs), AWS AppSync, Amazon SQS, Amazon SNS, EventBridge, Step Functions, DynamoDB, Amazon S3, Amazon Aurora Serverless, AWS Serverless Application Model, AWS Cloud Development Kit (AWS CDK), CloudWatch, and AWS X-Ray. Content converted from the deprecated AWS Serverless Developer Guide. | September 4, 2026 | 
| Updated AWS Fargate or AWS Lambda guide | Updated the Fargate vs Lambda decision guide to reflect current service capabilities including Lambda durable functions, Managed Instances, SnapStart for Python and .NET, Fargate resource limit increases, container restart policies, predictive scaling, hybrid architecture guidance, and cost comparison. | August 21, 2026 | 
| Initial publication | Initial publication of the consolidated decision guides reference. | July 31, 2026 | 