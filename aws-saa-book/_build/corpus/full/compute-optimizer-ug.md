# AWS Compute Optimizer User Guide

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
+ [What is AWS Compute Optimizer?](#what-is-compute-optimizer)
+ [AWS resources supported by Compute Optimizer](#supported-resources)
+ [Resource requirements](#requirements)
+ [Getting started with AWS Compute Optimizer](#getting-started)
   + [Opting in to AWS Compute Optimizer](#account-opt-in)
      + [Opting out of Compute Optimizer](#account-opt-out)
   + [Identity and Access Management for AWS Compute Optimizer](#security-iam)
   + [AWS managed policies for AWS Compute Optimizer](#managed-policies)
   + [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles)
   + [Using service-linked roles for Automation](#using-service-linked-roles-automation)
+ [Metrics analyzed by AWS Compute Optimizer](#metrics)
   + [EC2 instance metrics](#ec2-metrics-analyzed)
   + [EBS volume metrics](#ebs-metrics-analyzed)
   + [Lambda function metrics](#lambda-metrics-analyzed)
   + [Metrics for Amazon ECS services on Fargate](#ecs-fargate-metrics-analyzed)
   + [Metrics for commercial software licenses](#license-metrics-analyzed)
   + [Aurora and RDS database metrics](#rds-metrics-analyzed)
+ [Using the AWS Compute Optimizer dashboard](#viewing-dashboard)
+ [Viewing resource recommendations](#viewing-recommendations)
   + [Viewing EC2 instance recommendations](#view-ec2-recommendations)
      + [Accessing EC2 instance recommendations and details](#ec2-view-recommendations)
   + [Viewing EC2 Auto Scaling group recommendations](#view-asg-recommendations)
      + [Accessing EC2 Auto Scaling group recommendations and details](#asg-view-recommendations)
   + [Viewing Amazon EBS volume recommendations](#view-ebs-recommendations)
      + [Accessing EBS volumes recommendations and details](#ebs-view-recommendations)
   + [Viewing Lambda function recommendations](#view-lambda-recommendations)
      + [Accessing Lambda function recommendations and details](#lambda-view-recommendations)
   + [Viewing Amazon ECS services on Fargate recommendations](#view-ecs-recommendations)
      + [Accessing ECS service recommendations and details](#ecs-view-recommendations)
   + [Viewing commercial software license recommendations](#view-license-recommendations)
      + [Accessing commercial software license recommendations and details](#license-view-recommendations)
   + [Viewing Aurora and RDS database recommendations](#view-rds-recommendations)
      + [Accessing Aurora and RDS database recommendations and details](#rds-view-recommendations)
   + [Viewing idle resource recommendations](#view-idle-recommendations)
+ [Apply optimization recommendations using Automation](#automation)
   + [Enabling Automation](#automation-enable)
   + [Enabling Automation for your organization](#automation-org)
   + [Recommended actions](#automation-rec)
      + [Viewing recommended actions](#automation-rec-view)
      + [Apply recommended actions](#automation-rec-apply)
   + [Automation rules](#automation-rules)
      + [Creating automation rules](#automation-rules-create)
      + [Viewing automation rule](#automation-rules-view)
      + [Updating automation rules](#automation-rules-update)
      + [Editing automation rule order](#automation-rules-edit)
      + [Deleting or disabling automation rules](#automation-rules-delete)
      + [Creating automation rules with CloudFormation](#creating-automation-rules-with-cloudformation)
   + [Automation events](#automation-events)
      + [View automation events](#automation-events-view-details)
         + [View automation events details](#automation-events-view)
      + [Roll back automation events](#automation-events-rb)
   + [Disabling Automation](#automation-disable)
+ [Recommendation preferences](#viewing-recommendation-preferences)
   + [Rightsizing recommendation preferences](#rightsizing-preferences)
      + [Setting your rightsizing recommendation preferences](#rightsizing-preferences-process)
   + [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics)
      + [Activating enhanced infrastructure metrics at the resource level](#activating-eim-resource-level)
      + [Activating enhanced infrastructure metrics at the organization or account level](#activating-eim-level)
   + [External metrics ingestion](#external-metrics-ingestion)
      + [Configuring external metrics ingestion](#configure-external-metrics-ingestion)
      + [Opting out of external metrics ingestion](#deactivate-external-metrics-ingestion)
   + [Inferred workload type](#inferred-workload-type)
      + [Activating inferred workload type](#activating-inferred-workload-type-steps)
   + [Savings estimation mode](#savings-estimation-mode)
      + [Activating savings estimation mode](#activate-savings-estimation-mode)
   + [AWS Graviton-based instance recommendations](#graviton-recommendations)
+ [Managing accounts and preferences](#viewing-accounts)
   + [Viewing the status of an organization's member accounts](#view-account-opt-in)
   + [Delegating an administrator account](#delegate-administrator-account)
+ [Exporting AWS Compute Optimizer recommendations](#exporting-recommendations)
   + [Specifying an existing S3 bucket for your recommendations export](#create-s3-bucket-policy-for-compute-optimizer)
      + [Using encrypted S3 buckets for your recommendations export](#using-encrypted-s3-buckets)
   + [Exporting your recommendations](#exporting-your-recommendations)
   + [Viewing your export jobs](#viewing-your-exports)
   + [Exported files](#exported-files)
+ [Troubleshooting in Compute Optimizer](#troubleshooting-account-opt-in)
+ [Security in AWS Compute Optimizer](#security)
   + [Data protection in AWS Compute Optimizer](#data-protection)
   + [Compliance validation for AWS Compute Optimizer](#compliance-validation)
   + [Monitoring Compute Optimizer Automation](#monitoring-overview)
      + [Logging AWS Compute Optimizer Automation API calls using AWS CloudTrail](#logging-using-cloudtrail)
+ [FAQs on supported protocols](#cbor-faq)
+ [Document history for AWS Compute Optimizer](#doc-history)

-----



# What is AWS Compute Optimizer?
<a name="what-is-compute-optimizer"></a>

AWS Compute Optimizer is a service that analyzes your AWS resources' configuration and utilization metrics to provide you with rightsizing recommendations and identify idle resources. It reports whether your resources are optimal, and generates optimization recommendations to reduce the cost and improve the performance of your workloads. Compute Optimizer also provides graphs showing recent utilization metric history data, as well as projected utilization for recommendations, which you can use to evaluate which recommendation provides the best price-performance trade-off. The analysis and visualization of your usage patterns can help you decide when to move or resize your running resources, stop or delete idle resources, and still meet your performance and capacity requirements.

Compute Optimizer provides a [console experience](https://console.aws.amazon.com/compute-optimizer), and a [set of APIs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/Welcome.html) that allows you to view the findings of the analysis and recommendations for your resources across multiple AWS Regions. You can also view findings and recommendations across multiple accounts, if you opt in the management account of an organization. The findings from the service are also reported in the consoles of the supported services, such as the Amazon EC2 console.

## Supported resources
<a name="intro-supported-resources"></a>

Compute Optimizer generates recommendations for the following resources:
+ Amazon Elastic Compute Cloud (Amazon EC2) instances
+ Amazon EC2 Auto Scaling groups
+ Amazon Elastic Block Store (Amazon EBS) volumes
+ AWS Lambda functions
+ Amazon Elastic Container Service (Amazon ECS) services on AWS Fargate 
+ Commercial software licenses
+ Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases
+ Amazon NAT Gateway
+ Amazon DynamoDB
+ Amazon ElastiCache
+ Amazon MemoryDB
+ Amazon DocumentDB
+ Amazon WorkSpaces
+ Amazon SageMaker

For Compute Optimizer to generate recommendations for these resources, they must meet a specific set of requirements, and must have accumulated sufficient metric data. For more information, see [Resource requirements](#requirements).

## Opting in
<a name="intro-opting-in"></a>

You must opt in to have Compute Optimizer analyze your AWS resources. The service supports standalone AWS accounts, member accounts of an organization, and the management account of an organization. For more information, see [Opting in to AWS Compute Optimizer](#account-opt-in).

## Analyzing metrics
<a name="intro-metrics-analyzed"></a>

After you opt in, Compute Optimizer begins analyzing the specifications and the utilization metrics of your resources from Amazon CloudWatch for the last 14 days. For example, for Amazon EC2 instances, Compute Optimizer analyzes the vCPUs, memory, storage, and other specifications. It also analyzes the CPU utilization, network in and out, disk read and write, and other utilization metrics of currently running instances. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

## Enhancing recommendations
<a name="intro-enhanced-infrastructure-metrics"></a>

After you opt in, you can enhance your recommendations by activating recommendation preferences, such as the enhanced infrastructure metrics (paid feature). This feature extends the metrics analysis lookback period for selected resources to 93 days (compared to the 14-day default). For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).

You can also customize your recommendations using rightsizing recommendation preferences, which allow you to adjust CPU and memory utilization headroom and thresholds, configure specific lookback periods, and set instance family preferences at the organization, account, or regional level. For more information, see [Rightsizing recommendation preferences](#rightsizing-preferences).

Additionally, Compute Optimizer can ingest and analyze external EC2 memory utilization metrics from observability products like Datadog and Dynatrace to generate more accurate EC2 rightsizing recommendations. For more information, see [External metrics ingestion](#external-metrics-ingestion).

## Viewing findings and recommendations
<a name="intro-analyzing-data"></a>

Optimization findings for your resources are displayed on the Compute Optimizer dashboard. For more information, see [Using the AWS Compute Optimizer dashboard](#viewing-dashboard).

The top optimization recommendations for each of your resources are listed on the recommendations page. The top 3 optimization recommendations and utilization graphs for a specific resource are listed on the resource details page. For more information, see [Viewing resource recommendations](#viewing-recommendations).

Export your optimization recommendations to record them over time, and share the data with others. For more information, see [Exporting AWS Compute Optimizer recommendations](#exporting-recommendations).

## Availability
<a name="intro-availability"></a>

To view the currently supported AWS Regions and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/compute-optimizer.html) in the *AWS General Reference*.

# AWS resources supported by Compute Optimizer
<a name="supported-resources"></a>

This chapter outlines the AWS resources that Compute Optimizer generates recommendations for. It also provides you with the specific resource types supported by Compute Optimizer.

AWS Compute Optimizer generates recommendations for the following AWS resources:
+ **Amazon Elastic Compute Cloud (Amazon EC2) instances**

  Compute Optimizer generates recommendations for many Amazon EC2 instance types. For more information about the specific instance types that Compute Optimizer supports, see [Supported Amazon EC2 instance types](#supported-ec2-instances).
+ **Amazon EC2 Auto Scaling groups **

  Compute Optimizer generates recommendations for EC2 Auto Scaling groups. For more information, see [Supported Amazon EC2 Auto Scaling groups](#supported-asg).
+ **Amazon Elastic Block Store (Amazon EBS) volumes**

  Compute Optimizer generates recommendations for various EBS volume types. For more information about the specific EBS volume types that Compute Optimizer supports, see [Supported Amazon EBS volume types](#supported-ebs-volumes).
+ **AWS Lambda functions**

  Compute Optimizer generates memory size recommendations for Lambda functions that meet specific requirements. For more information, see [Lambda function requirements](#requirements-lambda-functions).
+ **Amazon Elastic Container Service (Amazon ECS) services on AWS Fargate**

  Compute Optimizer generates recommendations for Amazon ECS services on Fargate that meet specific requirements. For more information, see [Requirements for Amazon ECS services on Fargate](#requirements-ecs-fargate).
+ **Commercial software licenses**

  Compute Optimizer generates license recommendations for Microsoft SQL Servers on Amazon EC2 that meet specific requirements. For more information, see [Commercial software license requirements](#requirements-license).
+ **Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases**

  Compute Optimizer generates Aurora and RDS DB instances, RDS DB instance storage, and Aurora DB cluster recommendations for RDS for MySQL, RDS for PostgreSQL, and Amazon Aurora databases. For more information about the specific Amazon RDS resources supported by Compute Optimizer, see [Supported Amazon Aurora and RDS databases](#supported-rds).
+ **Amazon NAT Gateway**

  Compute Optimizer generates idle recommendations for NAT Gateway. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon DynamoDB**

  Compute Optimizer generates idle recommendations for DynamoDB provisioned tables. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon ElastiCache**

  Compute Optimizer generates idle recommendations for ElastiCache clusters running Redis or Valkey engines. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon MemoryDB**

  Compute Optimizer generates idle recommendations for MemoryDB clusters. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon DocumentDB**

  Compute Optimizer generates idle recommendations for DocumentDB provisioned and serverless clusters. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon WorkSpaces**

  Compute Optimizer generates idle recommendations for WorkSpaces. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).
+ **Amazon SageMaker**

  Compute Optimizer generates idle recommendations for SageMaker endpoints. For more information, see [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).



**Note**  
In order to generate recommendations for each resource, the resources must meet Compute Optimizer's metric and resource-specific requirements. For a list of the requiremtents for each resource, see [Resource requirements](#requirements).

**Topics**
+ [Supported Amazon EC2 instance types](#supported-ec2-instances)
+ [Supported Amazon EC2 Auto Scaling groups](#supported-asg)
+ [Supported Amazon EBS volume types](#supported-ebs-volumes)
+ [Supported Amazon Aurora and RDS databases](#supported-rds)
+ [Additional resources](#supported-add-resources)

## Supported Amazon EC2 instance types
<a name="supported-ec2-instances"></a>

Compute Optimizer generates recommendations for the instance types listed in this section. The following table lists the EC2 instance types that are supported by Compute Optimizer. 


| Instance series | Instance family | 
| --- | --- | 
| **C** – Compute optimized | C1 \| C3 \| C4 \| C5 \| C5a \| C5ad \| C5d \| C5n \| C6a \| C6g \| C6gd \| C6gn \| C6i \| C6in \| C6id \| C7a \| C7g \| C7gd \| C7gn \| C7i \| C7i-flex \| C8a \| C8g \| C8gb \| C8gd \| C8gn \| C8i \| C8i-flex \| C8id | 
| **D** – Dense storage | D2 \| D3 \| D3en | 
| **G** – Graphics intensive | G4dn \| G5g \| G5 \| G6 \| Gr6 \| G6e | 
| **Hpc** – High performance computing | H1 \| Hpc6a \| Hpc6id \| Hpc7a \| Hpc7g | 
| **I** – Storage optimized | I2 \| I3 \| I3en \| I4g \| I4i \| I7i \| I7ie \| I8g \| I8ge \| Im4gn \| Is4gen | 
| **M** – General purpose | M1 \| M2 \| M3 \| M4 \| M5 \| M5a \| M5ad \| M5d \| M5dn \| M5n \| M5zn \| M6a \| M6g \| M6gd \| M6i \| M6id \| M6idn \| M6in \| M7a \| M7g \| M7gd \| M7i \| M7i-flex \| M8a \| M8azn \| M8g \| M8gb \| M8gd \| M8gn \| M8i \| M8i-flex \| M8id | 
| **P** – GPU accelerated | P3 \| P4 \| P4d \| P4de \| P5 \| P5e \| P5en | 
| **R** – Memory optimized | R3 \| R4 \| R5 \| R5a \| R5ad \| R5b \| R5d \| R5dn \| R5n \| R6a \| R6g \| R6gd \| R6i \| R6id \| R6idn \| R6in \| R7a \| R7g \| R7gd \| R7i \| R7iz \| R8a \| R8g \| R8gb \| R8gd \| R8gn \| R8i \| R8i-flex \| R8id | 
| **T** – Burstable performance | T1 \| T2 \| T3 \| T3a \| T4g | 
| **U** – High memory | U-3tb1 \| U-6tb1 \| U-9tb1 \| U-12tb1 \| U-18tb1 \| U-24tb1 \| U7i-6tb \| U7i-8tb \| U7i-12tb \| U7in-16tb \| U7in-24tb \| U7in-32tb | 
| **X** – Memory intensive | X1 \| X1e \| X2gd \| X2idn \| X2iedn \| X2iezn \| X8g \| X8i | 
| **Z** – High memory | z1d | 

**Note**  
If an EC2 instance isn't listed, then it isn't supported by Compute Optimizer.
Compute Optimizer doesn't generate EC2 rightsizing recommendations for Spot Instances.

## Supported Amazon EC2 Auto Scaling groups
<a name="supported-asg"></a>

Compute Optimizer generates rightsizing and idle recommendations for Amazon EC2 Auto Scaling groups. This section outlines what Compute Optimizer supports for both types of recommendations.

### Rightsizing recommendations
<a name="supported-asg-rightsizing"></a>

Compute Optimizer supports rightsizing recommendations for EC2 Auto Scaling groups that have the following:
+ Single EC2 instance types
+ Mixed EC2 instance types
+ One or multiple scaling policies based on CPU utilization:
  + Target tracking
  + Predictive scaling
  + Simple scaling
  + Step scaling
+ Scheduled scaling policies
+ No scaling policy

**Note**  
Compute Optimizer doesn't support rightsizing recommendations for EC2 Auto Scaling groups that have the following:  
EC2 instance types that aren’t [supported by Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-ec2-instances)
Spot Instances
Mixed instance types that contain any instances outside of the C, M, or R instance families
Amazon ECS or Amazon EKS workloads
Mixed instance types containing both AMD and Intel instances
Mixed instance types using instance weights
Mixed instance types containing both x86 and Graviton instances
Mixed instance types containing instances on different platforms, such as Windows, SQL Server, and Linux

### Idle recommendations
<a name="supported-asg-idle"></a>

Compute Optimizer supports idle recommendations for EC2 Auto Scaling groups that use most of the [Supported Amazon EC2 instance types](#supported-ec2-instances). This includes EC2 Auto Scaling groups that have the following:
+ EC2 Spot Instances
+ Mixed instance types containing any of the instance families that Compute Optimizer supports (including G and P instance families)
+ Amazon ECS or Amazon EKS workloads

## Supported Amazon EBS volume types
<a name="supported-ebs-volumes"></a>

Compute Optimizer generates recommendations for the following EBS volume types that are attached to an instance:
+ HDD `st1` and `sc1`
+ General Purpose SSD `gp2` and `gp3`
+ Provisioned IOPS SSD `io1`, `io2`, and `io2 Block Express`

Compute Optimizer also generates recommendations to move your data out from previous generation HDD Magnetic volumes. For more information, see [ Amazon EBS previous generation volumes](https://aws.amazon.com/ebs/previous-generation/).

## Supported Amazon Aurora and RDS databases
<a name="supported-rds"></a>

The following sections outline the Amazon Aurora and RDS resources supported by Compute Optimizer.

### Database engines
<a name="supported-rds-database"></a>

Compute Optimizer generates recommendations for Amazon Aurora and RDS databases running the following engines:
+ RDS for MySQL
+ RDS for PostgreSQL
+ Aurora MySQL-Compatible Edition
+ Aurora PostgreSQL-Compatible Edition

### RDS DB instances
<a name="supported-rds-instance"></a>

Compute Optimizer generates recommendations for several DB instance types. For more information about Aurora and RDS DB instance types, see [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass) in the *Amazon Relational Database Service User Guide* and [ DB instance class types](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.Types.html) in the *Amazon Aurora User Guide for Aurora*.

The following tables list the DB instance types for the databases that are supported by Compute Optimizer.

------
#### [ Amazon RDS ]

The DB instance types for the RDS for MySQL and RDS for PostgreSQL database engines supported by Compute Optimizer.


| DB instance class family | Type | 
| --- | --- | 
| **General purpose** | db.m5 \| db.m5d \| db.m6g \| db.m6gd \| db.m6i \| db.m6id \| db.m7g \| db.m7i \| db.m8g | 
| **Memory-optimized R family** | db.r5 \| db.r5b \| db.r5d \| db.r6g \| db.r6gd \| db.r6i \| db.r6id \| db.r7g \| db.r7i \| db.r8g | 
| **Burstable-performance** | db.t3 \| db.t4g | 
| **Memory-optimized Z family** | db.x1 \| db.x2g \| db.x2idn \| db.x2iedn | 
| **High frequency** | db.z1d | 

------
#### [ Amazon Aurora ]

The DB instance types for the Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition database engines supported by Compute Optimizer.


| DB instance class family | Type | 
| --- | --- | 
| **General purpose** | db.m8g | 
| **Memory-optimized R family** | db.r5 \| db.r6g \| db.r6i \| db.r7g \| db.r8g | 
| **Memory-optimized X family** | db.x2g  | 
| **Burstable-performance** | db.t3 \| db.t4g | 
| **Optimized Reads** | db.r6gd \| db.r6id | 

**Note**  
Compute Optimizer doesn't support **db.serverless – Aurora Serverless v2 instance class with automatic capacity scaling**.

------

### RDS DB instance storage
<a name="supported-rds-storage"></a>

Compute Optimizer generates recommendations for the following RDS DB instance storage volume types:
+ General Purpose SSD `gp2` and `gp3`
+ Provisioned IOPS SSD `io1`

### Aurora DB cluster storage
<a name="supported-aurora-cluster"></a>

Compute Optimizer generates recommendations for Aurora DB cluster storage Aurora Standard configurations.

**Note**  
Compute Optimizer only provides recommendations to switch from Aurora Standard to Aurora I/O-Optimized storage configurations. 

For more information about both configurations, see [Amazon Aurora storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html) in the *Amazon Aurora User Guide for Aurora*.

## Additional resources
<a name="supported-add-resources"></a>
+ [Resource requirements](#requirements)
+ [Metrics analyzed by AWS Compute Optimizer](#metrics)
+ [Getting started with AWS Compute Optimizer](#getting-started)

# Resource requirements
<a name="requirements"></a>

This page provides you with an overview of the resource requirements needed for AWS Compute Optimizer to generate optimization recommendations. For Compute Optimizer to generate recommendations, your AWS resources must meet Amazon CloudWatch metric and resource-specific requirements. Compute Optimizer has different CloudWatch metric data requirements for each resource type. 

If your resources don't have enough metric data, allow for more time before the recommendations start appearing in the Compute Optimizer console. For example, if your resources have enough metric data but the recommendations aren't showing up, this probably means that Compute Optimizer is still analyzing your resources. It can take up to 24 hours to complete the analysis. After the analysis is complete, resource recommendations appear in the Compute Optimizer console.

**Topics**
+ [Amazon EC2 instance and EC2 Auto Scaling group requirements](#requirements-ec2-instances)
+ [Amazon EBS volume requirements](#requirements-ebs-volumes)
+ [Lambda function requirements](#requirements-lambda-functions)
+ [Requirements for Amazon ECS services on Fargate](#requirements-ecs-fargate)
+ [Commercial software license requirements](#requirements-license)
+ [Amazon Aurora and RDS database requirements](#requirements-rds)
+ [Additional resources](#requirements-resources)

## Amazon EC2 instance and EC2 Auto Scaling group requirements
<a name="requirements-ec2-instances"></a>

Amazon EC2 instances and EC2 Auto Scaling groups both require at least 30 hours of CloudWatch metric data in the past 14 days.

If you enabled the enhanced infrastructure metrics feature, both EC2 instances and EC2 Auto Scaling require at least 30 hours of CloudWatch metric data over the past 93 days. For more information, see [ Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html).

For a list of the instance types supported by Compute Optimizer, see [Supported Amazon EC2 instance types](#supported-ec2-instances). For information about the EC2 Auto Scaling groups that Compute Optimizer supports, see [Supported Amazon EC2 Auto Scaling groups](#supported-asg).

**Important**  
You must enable Cost Explorer to allow Compute Optimizer to use Cost Explorer's billing data to calculate savings and populate pricing information for your recommendations. We recommend that you also opt in to Cost Optimization Hub to receive rightsizing recommendations that consider any Reserved Instances or Savings Plans pricing models that are active in your accounts. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Getting started with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) in the *AWS Cost Management User Guide*.

## Amazon EBS volume requirements
<a name="requirements-ebs-volumes"></a>

Compute Optimizer generates recommendations for EBS volume types that are attached to a running instance for at least 30 consecutive hours. Data is only reported to CloudWatch when the volume is attached to a running instance. If you detach an EBS volume from an EC2 instance, the recommendations for that volume will no longer be available.

For a list of Amazon EBS volume types supported by Compute Optimizer, see [Supported Amazon EBS volume types](#supported-ebs-volumes).

## Lambda function requirements
<a name="requirements-lambda-functions"></a>

Compute Optimizer generates memory size recommendations only for Lambda functions that meet the following requirements:
+ The configured memory is less than or equal to 1,792 MB.
+ The functions were invoked at least 50 times in the last 14 days.

Functions that don't meet these requirements are given a finding of **Unavailable**. The reason code of **Inconclusive** applies to functions that have configured memory greater than 1,792 MB. **Insufficient data** applies to functions that have been invoked fewer than 50 times in the last 14 days.

Functions with a finding of **Unavailable** don't appear in the Compute Optimizer console and don't receive recommendations.

**Note**  
Lambda functions don't require CloudWatch metric data.

## Requirements for Amazon ECS services on Fargate
<a name="requirements-ecs-fargate"></a>

To generate recommendations for Amazon ECS services on Fargate, Compute Optimizer requires the following:
+ Your services have at least 24 hours of CloudWatch and Amazon ECS utilization metrics in the past 14 days.
+ No step scaling policy is attached.
+ No target scaling policy is attached to CPU and memory.
**Note**  
If a target tracking policy is attached to the service’s CPU only, Compute Optimizer only generates memory size recommendations. Or, if a target tracking policy is attached to the service’s memory only, Compute Optimizer only generates CPU size recommendations. 
+ The service run status is **SteadyState** or **MoreWork**.

For more information about the metrics analyzed, see [Metrics for Amazon ECS services on Fargate](#ecs-fargate-metrics-analyzed).

## Commercial software license requirements
<a name="requirements-license"></a>

Compute Optimizer only generates license recommendations for Microsoft SQL Server on Amazon EC2. 

To generate recommendations for commercial software licenses, Compute Optimizer requires the following:
+ At least 30 *consecutive* hours of CloudWatch metric data.
+ Enable CloudWatch Application Insights using your Microsoft SQL Server database credentials.

  For more information about how to enable CloudWatch Application Insights, see [Set up Amazon CloudWatch Application Insights for monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up) in the *Amazon CloudWatch User Guide*.
+ Attach the required instance role and policy for CloudWatch Application Insights. For more information, see [Policies to enable commercial software license recommendations](#license-access).

For more information about the metrics analyzed, see [Metrics for commercial software licenses](#license-metrics-analyzed).

## Amazon Aurora and RDS database requirements
<a name="requirements-rds"></a>

Compute Optimizer generates Aurora and RDS DB instances, RDS DB instance storage, and Aurora DB cluster recommendations for RDS for MySQL, RDS for PostgreSQL, and Amazon Aurora databases. 

### Amazon Aurora and RDS instances
<a name="requirements-aurora-clusters"></a>

To generate recommendations for your Aurora and RDS DB instances, Compute Optimizer requires the following:
+ At least 30 hours of CloudWatch metric data in the past 14 days. If you enabled the enhanced infrastructure metrics feature, DB instances require at least 30 hours of metric data over the past 93 days. For more information, see [ Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html).
+ To receive recommendations for RDS DB instances that are over-provisioned, you need to enable Amazon RDS Performance Insights. To enable Performance Insights for your DB instances, see [ Turning Performance Insights on and off for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Relational Database Service User Guide*.

### Aurora DB clusters
<a name="requirements-aurora-clusters"></a>

To generate recommendations for your Aurora DB clusters, Compute Optimizer requires the following:
+ No application Auto Scaling policy is attached to the Aurora DB cluster. For more information about Aurora Auto Scaling, see [Amazon Aurora Auto Scaling with Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrations.AutoScaling.html) in the *Amazon Aurora User Guide*.
+ The Aurora DB cluster has at least 14 days of cost usage data.
+ The Aurora DB cluster has not used Aurora Parallel Query over the lookback period.
+ The Aurora DB cluster has not changed storage configuration in the last 30 days.

## Additional resources
<a name="requirements-resources"></a>
+ [AWS resources supported by Compute Optimizer](#supported-resources)
+ [Metrics analyzed by AWS Compute Optimizer](#metrics)
+ [Getting started with AWS Compute Optimizer](#getting-started)

# Getting started with AWS Compute Optimizer
<a name="getting-started"></a>

When you access the AWS Compute Optimizer console for the first time, you're asked to opt in using the account that you’re signed in with. Before you can use the service, you must opt in or out. In addition, you can also opt in or opt out using the Compute Optimizer API, AWS Command Line Interface (AWS CLI), or SDKs.

By opting in, you're authorizing Compute Optimizer to analyze the specifications and utilization metrics of your AWS resources. Examples include EC2 instances and EC2 Auto Scaling groups.

**Note**  
To improve the recommendation quality of Compute Optimizer, Amazon Web Services might use your CloudWatch metrics and configuration data. This includes up to three months (93 days) of metrics analysis when you activate the enhanced infrastructure metrics feature. Contact [AWS Support](https://console.aws.amazon.com/support) to request that AWS stop using your CloudWatch metrics and configuration data to improve the recommendation quality of Compute Optimizer.

## Required permissions
<a name="required-permissions"></a>

You must have the appropriate permissions to opt in to Compute Optimizer, to view its recommendations, and to opt out. For more information, see [Identity and Access Management for AWS Compute Optimizer](#security-iam).

When you opt in, Compute Optimizer automatically creates a Service-Linked Role in your account to access its data. For more information, see [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles).

## Accounts supported by Compute Optimizer
<a name="supported-accounts"></a>

The following AWS account types can opt in to Compute Optimizer:
+ **Standalone AWS account**

  A standalone AWS account that doesn't have AWS Organizations enabled. If you opt in to Compute Optimizer while signed in to a standalone account, Compute Optimizer analyzes the resources in the account and generates optimization recommendations for those resources.
+ **Member account of an organization**

  An AWS account that's a member of an organization. If you opt in to Compute Optimizer while signed in to a member account of an organization, Compute Optimizer only analyzes the resources in the member account and generates optimization recommendations for those resources.
+ **Management account of an organization**

  An AWS account that administers an organization. If you opt in to Compute Optimizer while signed in to a management account of an organization, Compute Optimizer gives you the option to opt in the management account only, or the management account and all member accounts of the organization.
**Important**  
To opt in all member accounts for an organization, make sure that the organization has all features enabled. For more information, see [Enabling All Features in Your Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.  
When you opt in using your organization's management account and include all member accounts within the organization, trusted access for Compute Optimizer is enabled in your organization account. For more information, see [Trusted access for AWS Organizations](#trusted-service-access).

## Next steps
<a name="next-steps-getting-started"></a>

For instructions on how to opt in your account, or the accounts within your organization, to AWS Compute Optimizer, see [Opting in to AWS Compute Optimizer](#account-opt-in).

## Additional resources
<a name="getting-started-resources"></a>
+ [Identity and Access Management for AWS Compute Optimizer](#security-iam)
+ [AWS managed policies for AWS Compute Optimizer](#managed-policies)
+ [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles)

## Opting in to AWS Compute Optimizer
<a name="account-opt-in"></a>

Use the following procedure to opt in your account, or the accounts within your organization, to AWS Compute Optimizer. You can opt in using the Compute Optimizer console or the AWS Command Line Interface (AWS CLI).

**Note**  
If your account is already opted in, but you want to opt in again to re-enable trusted access for Compute Optimizer in your organization. You can opt in again, but this must be done using the AWS CLI. When you opt in using the AWS CLI, run the `update-enrollment-status` command and specify the `--include-member-accounts` parameter. Alternatively, you can enable trusted access directly in the AWS Organizations console or by using AWS CLI or API. For more information, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*.

### Prerequisites
<a name="opt-in-prerequisites"></a>

Make sure your IAM identity has appropriate permissions to opt in to AWS Compute Optimizer. The suggested policy that grants this permission is [Policy to opt in to Compute Optimizer](#opting-in-access).

### Procedure
<a name="opt-in-procedure"></a>

------
#### [ Console ]

**To opt in to Compute Optimizer**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

   If this is your first time using the Compute Optimizer console, the **Compute Optimizer landing page** is displayed.

1. Choose **Get started**.

1. On the **Account setup** page, review the **Getting started** and **Setting up your account** sections.

1. The following options are displayed if the account that you're signed in to is the management account of your organization. Choose one before continuing to the next step.
   + **Only this account** - Choose this option to opt in only the account that you’re currently signed in to. If you choose this option, Compute Optimizer analyzes resources that are in the individual account, and generates optimization recommendations for those resources.
   + **All accounts within this organization** - Choose this option to opt in the account you’re currently signed in to, and all of its member accounts. If you choose this option, Compute Optimizer analyzes resources that are in all accounts in the organization, and generates optimization recommendations for those resources.
**Note**  
If you add any new member accounts to your organization after you opt in, Compute Optimizer automatically opts in those accounts.

1. Choose **Opt in**. By opting in, you indicate that you agree to and understand the requirements to opt in to Compute Optimizer.

After you opt in, you're redirected to the dashboard in the Compute Optimizer console. At the same time, the service immediately starts analyzing the configuration and utilization metrics of your AWS resources. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

**Note**  
When you complete the opt in process, it can up to 24 hours for the opted-in accounts to appear in the Compute Optimizer console.

------
#### [ CLI ]

**To opt in to Compute Optimizer**

1. Open a terminal or command prompt window.

   If you didn't already install the AWS CLI already, install and configure it to work with Compute Optimizer. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Quickly Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration) in the *AWS Command Line Interface User Guide*.

1. Enter one of the following commands. Choose if you want to opt in your individual account or the management account of your organization and all its member accounts.
   + To opt in your individual account:

     ```
     aws compute-optimizer update-enrollment-status --status Active
     ```
   + To opt in the management account of an organization and include all member accounts within the organization:

     ```
     aws compute-optimizer update-enrollment-status --status Active --include-member-accounts
     ```

After you opt in to Compute Optimizer using the previous command, the service begins analyzing the configuration and utilization metrics of your AWS resources. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

------

### Next steps
<a name="next-steps-opt-in"></a>
+ Make sure that your AWS resources meet the necessary requirements for Compute Optimizer to generate your receommendations. And allow for at least 24 hours for your optimization recommendations to be generated. be generated. For more information, see [Resource requirements](#requirements).
+ View the findings and recommendations in the dashboard and recommendation pages of the Compute Optimizer console. For more information, see [Using the AWS Compute Optimizer dashboard](#viewing-dashboard) and [Viewing resource recommendations](#viewing-recommendations).
+ Consider extending the lookback period from the 14-day default period to 93 days by activating the enhanced infrastructure metrics feature. For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).
+ Using the management account of your organization, you can delegate a member account as an administrator for Compute Optimizer. For more information, see [Delegating an administrator account](#delegate-administrator-account).

### Additional resources
<a name="opt-in-resources"></a>
+ [Identity and Access Management for AWS Compute Optimizer](#security-iam)
+ [AWS managed policies for AWS Compute Optimizer](#managed-policies)
+ [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles)
+ Troubleshooting — [Troubleshooting in Compute Optimizer](#troubleshooting-account-opt-in)

### Opting out of Compute Optimizer
<a name="account-opt-out"></a>

Use the following procedure to opt your account out of Compute Optimizer using the AWS CLI. This procedure also deletes your account's recommendations and related metrics data from Compute Optimizer. For more information, see [update-enrollment-status](https://docs.aws.amazon.com/cli/latest/reference/compute-optimizer/update-enrollment-status.html) in the *AWS CLI Command Reference*. 

**Note**  
You can't opt out using the Compute Optimizer console.

#### Procedure
<a name="opt-in-procedure"></a>

**To opt an account out of Compute Optimizer**

1. Open a terminal or command prompt window.

   If you haven't already, install the AWS CLI and configure it to work with Compute Optimizer. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Quickly Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration) in the *AWS Command Line Interface User Guide*.

1. Enter the following command.

   ```
   aws compute-optimizer update-enrollment-status --status Inactive
   ```
**Note**  
You can't specify the `--include-member-accounts` parameter when opting out with the `update-enrollment-status` command. If you specify this parameter when opting out with this command, an error occurs.

Your account is opted out of Compute Optimizer after running the previous command. At the same time, your account's recommendations and related metrics data are deleted from Compute Optimizer. If you access the Compute Optimizer console, the option to opt in again should be displayed.

## Identity and Access Management for AWS Compute Optimizer
<a name="security-iam"></a>

You can use AWS Identity and Access Management (IAM) to create identities (users, groups, or roles), and give those identities permissions to access the AWS Compute Optimizer console and APIs.

By default, IAM users don't have access to the Compute Optimizer console and APIs. You give users access by attaching IAM policies to a single user, a group of users, or a role. For more information, see [Identities (Users, Groups, and Roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) and [Overview of IAM Policies in the IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).

After you create IAM users, you can give those users individual passwords. Then, they can sign in to your account and view Compute Optimizer information by using an account-specific sign-in page. For more information, see [How Users Sign In to Your Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html).

**Important**  
To view recommendations for EC2 instances, an IAM user requires the `ec2:DescribeInstances` permission.
To view recommendations for EBS volumes, an IAM user requires the `ec2:DescribeVolumes` permission.
To view recommendations for EC2 Auto Scaling groups, an IAM user requires the `autoscaling:DescribeAutoScalingGroups` and `autoscaling:DescribeAutoScalingInstances` permissions.
To view recommendations for Lambda functions, an IAM user requires the `lambda:ListFunctions` and `lambda:ListProvisionedConcurrencyConfigs` permissions.
To view recommendations for Amazon ECS services on Fargate, an IAM user requires the `ecs:ListServices` and `ecs:ListClusters` permissions.
To view current CloudWatch metrics data in the Compute Optimizer console, an IAM user requires the `cloudwatch:GetMetricData` permission.
To view recommendations commercial software licenses, certain Amazon EC2 instance roles and IAM user permissions are required. For more information see, [Policies to enable commercial software license recommendations](#license-access).
To view recommendations for Amazon RDS, an IAM user requires the `rds:DescribeDBInstances` and `rds:DescribeDBClusters` permissions.

If the user or group that you want to give permissions to already has a policy, you can add one of the Compute Optimizer specific policy statements illustrated here to that policy.

**Topics**
+ [Trusted access for AWS Organizations](#trusted-service-access)
+ [Policy examples for Compute Optimizer](#CO-policy-examples)
+ [Policy examples for Automation](#COA-policy-example)
+ [Additional resources](#iam-resources)

### Trusted access for AWS Organizations
<a name="trusted-service-access"></a>

When you opt in using your organization's management account and include all member accounts within the organization, trusted access for Compute Optimizer is automatically enabled in your organization account. This allows Compute Optimizer to analyze compute resources in those member accounts, and generate recommendations for them.

Every time that you access recommendations for member accounts, Compute Optimizer verifies that trusted access is enabled in your organization account. If you disable Compute Optimizer trusted access after you opt in, Compute Optimizer denies access to recommendations for your organization's member accounts. Moreover, the member accounts within the organization aren't opted in to Compute Optimizer. To re-enable trusted access, opt in to Compute Optimizer again using your organization's management account and include all the member accounts within the organization. For more information, see [Opting in to AWS Compute Optimizer](#account-opt-in). For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*.

### Policy examples for Compute Optimizer
<a name="CO-policy-examples"></a>

**Topics**
+ [Policy to opt in to Compute Optimizer](#opting-in-access)
+ [Policies to grant access to Compute Optimizer for standalone AWS accounts](#standalone-account-access)
+ [Policies to grant access to Compute Optimizer for a management account of an organization](#organization-account-access)
+ [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions)
+ [Policies to enable commercial software license recommendations](#license-access)
+ [Policy to deny access to Compute Optimizer](#deny-access)

#### Policy to opt in to Compute Optimizer
<a name="opting-in-access"></a>

This policy statement grants the following:
+ Access to opt in to Compute Optimizer.
+ Access to create a service-linked role for Compute Optimizer. For more information, see [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles).
+ Access to update the enrollment status to the Compute Optimizer service.

**Important**  
This IAM role is required to opt in to AWS Compute Optimizer.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "organizations:DescribeOrganization",
            "Resource": "*"
        }
    ]
}
```

------

#### Policies to grant access to Compute Optimizer for standalone AWS accounts
<a name="standalone-account-access"></a>

The following policy statement grants full access to Compute Optimizer for standalone AWS accounts. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:*",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following policy statement grants read-only access to Compute Optimizer for standalone AWS accounts.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:GetEnrollmentStatus",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetRecommendationSummaries",
                "compute-optimizer:GetEC2InstanceRecommendations",
                "compute-optimizer:GetEC2RecommendationProjectedMetrics",
                "compute-optimizer:GetAutoScalingGroupRecommendations",
                "compute-optimizer:GetEBSVolumeRecommendations",
                "compute-optimizer:GetLambdaFunctionRecommendations",
                "compute-optimizer:DescribeRecommendationExportJobs",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetECSServiceRecommendations",
                "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
                "compute-optimizer:GetRDSDatabaseRecommendations",
                "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
                "compute-optimizer:GetIdleRecommendations",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "rds:DescribeDBInstances",
                "rds:DescribeDBClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Policies to grant access to Compute Optimizer for a management account of an organization
<a name="organization-account-access"></a>

The following policy statement grants full access to Compute Optimizer for a management account of your organization. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:*",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "organizations:ListAccounts",
                "organizations:DescribeOrganization",
                "organizations:DescribeAccount",
                "organizations:EnableAWSServiceAccess",
                "organizations:ListDelegatedAdministrators",
                "organizations:RegisterDelegatedAdministrator",
                "organizations:DeregisterDelegatedAdministrator"
            ],
            "Resource": "*"
        }
    ]
}
```

------

The following policy statement grants read-only access to Compute Optimizer for a management account of an organization.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:GetEnrollmentStatus",
                "compute-optimizer:GetEnrollmentStatusesForOrganization",
                "compute-optimizer:GetRecommendationSummaries",
                "compute-optimizer:GetEC2InstanceRecommendations",
                "compute-optimizer:GetEC2RecommendationProjectedMetrics",
                "compute-optimizer:GetAutoScalingGroupRecommendations",
                "compute-optimizer:GetEBSVolumeRecommendations",
                "compute-optimizer:GetLambdaFunctionRecommendations",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:GetECSServiceRecommendations",
                "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
                "compute-optimizer:GetRDSDatabaseRecommendations",
                "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
                "compute-optimizer:GetIdleRecommendations",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
                "ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "autoscaling:DescribeAutoScalingInstances",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "organizations:ListAccounts",
                "organizations:DescribeOrganization",
                "organizations:DescribeAccount",
                "organizations:ListDelegatedAdministrators",
                "rds:DescribeDBInstances",
                "rds:DescribeDBClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

------

#### Policies to grant access to manage Compute Optimizer recommendation preferences
<a name="enhanced-infrastructure-metrics-permissions"></a>

The following policy statements grant access to view and edit recommendation preferences. 

**Grant access to manage recommendation preferences for EC2 instances only**

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "Ec2Instance"
                }
            }            
        }
    ]
}
```

------

**Grant access to manage recommendation preferences for EC2 Auto Scaling groups only**

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "AutoScalingGroup"
                }
            }            
        }
    ]
}
```

------

**Grant access to manage recommendation preferences for RDS instances only**

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:DeleteRecommendationPreferences",
                "compute-optimizer:GetEffectiveRecommendationPreferences",
                "compute-optimizer:GetRecommendationPreferences",
                "compute-optimizer:PutRecommendationPreferences"
            ],
            "Resource": "*",
            "Condition" :  {
                "StringEquals" : {
                    "compute-optimizer:ResourceType" : "RdsDBInstance"
                }
            }            
        }
    ]
}
```

------

#### Policies to enable commercial software license recommendations
<a name="license-access"></a>

For Compute Optimizer to generate license recommendations, attach the following Amazon EC2 instance roles and policies.
+ The `AmazonSSMManagedInstanceCore` role to enable Systems Manager. For more information, see [AWS Systems Manager identity-based policy examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_id-based-policy-examples) in the *AWS Systems Manager User Guide*.
+ The `CloudWatchAgentServerPolicy` policy to enable the release of instance metrics and logs to CloudWatch. For more information, see [ Create IAM roles and users for use with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent) in the *Amazon CloudWatch User Guide*.
+ The following IAM inline policy statement to read the secret Microsoft SQL Server connection string stored in AWS Systems Manager. For more information about inline policies, see [ Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline) in the *AWS Identity and Access Management User Guide*.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue*"
            ],
            "Resource": "arn:aws:secretsmanager:*:*:secret:ApplicationInsights-*"
        }
    ]
}
```

------

Additionally, to enable and receive license recommendations, attach the following IAM policy to your user, group or role. For more information, [ IAM policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-iam) in the *Amazon CloudWatch User Guide*.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "applicationinsights:*",
                "iam:CreateServiceLinkedRole",
                "iam:ListRoles",
                "resource-groups:ListGroups"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

#### Policy to deny access to Compute Optimizer
<a name="deny-access"></a>

The following policy statement denies access to Compute Optimizer.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "compute-optimizer:*",
            "Resource": "*"
        }
    ]
}
```

------

### Policy examples for Automation
<a name="COA-policy-example"></a>

**Topics**
+ [Policy to enable Automation for your account](#policy-automation-enable)
+ [Policy to enable Automation across your organization](#automation-enable-org)
+ [Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts](#automation-account-full)
+ [Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts](#automation-account-read)
+ [Policy to grant full access to Compute Optimizer Automation for a management account of an organization](#automation-account-mgmt)
+ [Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization](#automation-account-mgmt-readonly)

#### Policy to enable Automation for your account
<a name="policy-automation-enable"></a>

The following policy statement enables Automation for your account.

```
{
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        }
    ]
}
```

#### Policy to enable Automation across your organization
<a name="automation-enable-org"></a>

The following policy statement enables Automation across your organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:AssociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:DisassociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:ListAccounts",
            "Resource": "*"
        }
    ]
}
```

#### Policy to grant full access to Compute Optimizer Automation for standalone AWS accounts
<a name="automation-account-full"></a>

The following policy grants full access to Compute Optimizer Automation for standalone AWS accounts.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:*",
            "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Policy to grant read-only access to Compute Optimizer Automation for standalone AWS accounts
<a name="automation-account-read"></a>

The following policy grants read-only access to Compute Optimizer Automation for standalone AWS accounts.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:GetEnrollmentConfiguration",
               "aco-automation:GetAutomationEvent",
               "aco-automation:GetAutomationRule",
               "aco-automation:ListAutomationEvents",
               "aco-automation:ListAutomationEventSteps",
               "aco-automation:ListAutomationEventSummaries",
               "aco-automation:ListAutomationRules",
               "aco-automation:ListAutomationRulePreview",
               "aco-automation:ListAutomationRulePreviewSummaries",
               "aco-automation:ListRecommendedActions",
               "aco-automation:ListRecommendedActionSummaries",
               "aco-automation:ListTagsForResource",
               "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Policy to grant full access to Compute Optimizer Automation for a management account of an organization
<a name="automation-account-mgmt"></a>

The following policy grants full access to Compute Optimizer Automation for a management account of an organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:*",
               "ec2:DescribeVolumes",
               "organizations:ListAccounts",
               "organizations:DescribeOrganization",
               "organizations:DescribeAccount",
               "organizations:EnableAWSServiceAccess",
               "organizations:ListDelegatedAdministrators",
               "organizations:RegisterDelegatedAdministrator",
               "organizations:DeregisterDelegatedAdministrator"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Policy to grant read-only access to Compute Optimizer Automation for a management account of an organization
<a name="automation-account-mgmt-readonly"></a>

The following policy grants read-only access to Compute Optimizer Automation for a management account of an organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "aco-automation:GetEnrollmentConfiguration",
               "aco-automation:GetAutomationEvent",
               "aco-automation:GetAutomationRule",
               "aco-automation:ListAccounts",
               "aco-automation:ListAutomationEvents",
               "aco-automation:ListAutomationEventSteps",
               "aco-automation:ListAutomationEventSummaries",
               "aco-automation:ListAutomationRules",
               "aco-automation:ListAutomationRulePreview",
               "aco-automation:ListAutomationRulePreviewSummaries",
               "aco-automation:ListRecommendedActions",
               "aco-automation:ListRecommendedActionSummaries",
               "aco-automation:ListTagsForResource",
               "ec2:DescribeVolumes"
            ],
            "Resource": "*"
        }
    ]
}
```

### Additional resources
<a name="iam-resources"></a>
+ Troubleshooting — [Troubleshooting in Compute Optimizer](#troubleshooting-account-opt-in)
+ [Opting in to AWS Compute Optimizer](#account-opt-in)
+ [AWS managed policies for AWS Compute Optimizer](#managed-policies)
+ [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles)
+ [Using service-linked roles for Automation](#using-service-linked-roles-automation)

## AWS managed policies for AWS Compute Optimizer
<a name="managed-policies"></a>

To add permissions to users, groups, and roles, consider using AWS managed policies rather than to writing your own policies. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services don't remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, Amazon Web Services supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: ComputeOptimizerServiceRolePolicy](#security-iam-awsmanpol-ComputeOptimizerServiceRolePolicy)
+ [AWS managed policy: ComputeOptimizerReadOnlyAccess](#security-iam-awsmanpol-ComputeOptimizerReadOnlyAccess)
+ [AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy](#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy)
+ [Compute Optimizer updates to AWS managed policies](#security-iam-awsmanpol-updates)

### AWS managed policy: ComputeOptimizerServiceRolePolicy
<a name="security-iam-awsmanpol-ComputeOptimizerServiceRolePolicy"></a>

The `ComputeOptimizerServiceRolePolicy` managed policy is attached to a service-linked role that allows Compute Optimizer to perform actions on your behalf. For more information, see [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles).

**Note**  
You can't attach `ComputeOptimizerServiceRolePolicy` to your IAM entities.

**Permissions details**

This policy includes the following permissions.
+ `compute-optimizer` – Grants full administrative permissions to all resources in Compute Optimizer.
+ `organizations` – Allows the management account of an AWS organization to opt in member accounts of the organization to Compute Optimizer.
+ `cloudwatch` – Grants access to CloudWatch resource metrics for the purpose of analyzing them and generating Compute Optimizer resource recommendations.
+ `autoscaling` – Grants access to EC2 Auto Scaling groups and the instances in EC2 Auto Scaling groups for validation purposes.
+ `Ec2` – Grants access to Amazon EC2 instances and volumes.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "ComputeOptimizerFullAccess",
			"Effect": "Allow",
			"Action": [
				"compute-optimizer:*"
			],
			"Resource": "*"
		},
		{
			"Sid": "AwsOrgsAccess",
			"Effect": "Allow",
			"Action": [
				"organizations:DescribeOrganization",
				"organizations:ListAccounts",
				"organizations:ListAWSServiceAccessForOrganization",
                                "organizations:ListDelegatedAdministrators"
			],
			"Resource": [
				"*"
			]
		},
		{
			"Sid": "CloudWatchAccess",
			"Effect": "Allow",
			"Action": [
				"cloudwatch:GetMetricData",
				"cloudwatch:DescribeAlarms"
			],
			"Resource": "*"
		},
		{
			"Sid": "AutoScalingAccess",
			"Effect": "Allow",
			"Action": [
				"autoscaling:DescribeAutoScalingInstances",
				"autoscaling:DescribeAutoScalingGroups",
				"autoscaling:DescribePolicies",
                                "autoscaling:DescribeScheduledActions"
			],
			"Resource": "*"
		},
		{
                        "Sid": "Ec2Access",
                        "Effect": "Allow",
                        "Action": [
                                "ec2:DescribeInstances",
                                "ec2:DescribeVolumes"
                        ],
                        "Resource": "*"
                }
	]
}
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ComputeOptimizerFullAccess",
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AwsOrgsAccess",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAccounts",
                "organizations:ListAWSServiceAccessForOrganization"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "CloudWatchAccess",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### AWS managed policy: ComputeOptimizerReadOnlyAccess
<a name="security-iam-awsmanpol-ComputeOptimizerReadOnlyAccess"></a>

You can attach the `ComputeOptimizerReadOnlyAccess` policy to your IAM identities.

This policy grants read-only permissions that allow IAM users to view Compute Optimizer resource recommendations.

**Permissions details**

This policy includes the following:
+ `compute-optimizer` – Grants read-only access to Compute Optimizer resource recommendations.
+ `ec2` – Grants read-only access to Amazon EC2 instances and Amazon EBS volumes.
+ `autoscaling` – Grants read-only access to EC2 Auto Scaling groups.
+ `lambda` – Grants read-only access to AWS Lambda functions and their configurations.
+ `cloudwatch` – Grants read-only access to Amazon CloudWatch metric data for resource types that are supported by Compute Optimizer.
+ `organizations` – Grants read-only access to member accounts of an AWS organization.
+ `ecs` – Grants access to Amazon ECS services on Fargate.
+ `rds` – Grants read-only access to Amazon RDS instances and clusters.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"compute-optimizer:DescribeRecommendationExportJobs",
				"compute-optimizer:GetEnrollmentStatus",
				"compute-optimizer:GetEnrollmentStatusesForOrganization",
				"compute-optimizer:GetRecommendationSummaries",
				"compute-optimizer:GetEC2InstanceRecommendations",
				"compute-optimizer:GetEC2RecommendationProjectedMetrics",
				"compute-optimizer:GetAutoScalingGroupRecommendations",
				"compute-optimizer:GetEBSVolumeRecommendations",
				"compute-optimizer:GetLambdaFunctionRecommendations",
				"compute-optimizer:GetRecommendationPreferences",
				"compute-optimizer:GetEffectiveRecommendationPreferences",
				"compute-optimizer:GetECSServiceRecommendations",
				"compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
				"compute-optimizer:GetLicenseRecommendations",
				"compute-optimizer:GetRDSDatabaseRecommendations",
                                "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
                                "compute-optimizer:GetIdleRecommendations",
				"ec2:DescribeInstances",
				"ec2:DescribeVolumes",
				"ecs:ListServices",
				"ecs:ListClusters",
				"autoscaling:DescribeAutoScalingGroups",
				"autoscaling:DescribeAutoScalingInstances",
				"lambda:ListFunctions",
				"lambda:ListProvisionedConcurrencyConfigs",
				"cloudwatch:GetMetricData",
				"organizations:ListAccounts",
				"organizations:DescribeOrganization",
				"organizations:DescribeAccount",
				"rds:DescribeDBInstances",
                                "rds:DescribeDBClusters"
			],
			"Resource": "*"
		}
	]
}
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "compute-optimizer:DescribeRecommendationExportJobs",
                "compute-optimizer:GetEnrollmentStatus",
                "compute-optimizer:GetEnrollmentStatusesForOrganization",
                "compute-optimizer:GetRecommendationSummaries",
                "compute-optimizer:GetEC2InstanceRecommendations",
                "compute-optimizer:GetEC2RecommendationProjectedMetrics",
                "compute-optimizer:GetAutoScalingGroupRecommendations",
                "compute-optimizer:GetEBSVolumeRecommendations",
                "compute-optimizer:GetLambdaFunctionRecommendations",
                "compute-optimizer:GetECSServiceRecommendations",
		"compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
				"compute-optimizer:GetLicenseRecommendations",
                "ec2:DescribeInstances",
                "ec2:DescribeVolumes",
                "ecs:ListServices",
		"ecs:ListClusters",
                "autoscaling:DescribeAutoScalingGroups",
                "lambda:ListFunctions",
                "lambda:ListProvisionedConcurrencyConfigs",
                "cloudwatch:GetMetricData",
                "organizations:ListAccounts",
                "organizations:DescribeOrganization",
                "organizations:DescribeAccount"
            ],
            "Resource": "*"
        }
    ]
}
```

------

**Note**  
The following policy statement only grants read-only access to Compute Optimizer for a management account of an organization to view org-level recommendations. If you're the delegated administrator and you want to view org-level recommendations, see [ Policies to grant access to Compute Optimizer for a management account of an organization](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#organization-account-access).

### AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy
<a name="security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy"></a>

The `ComputeOptimizerAutomationServiceRolePolicy` managed policy is attached to a service-linked role that allows Compute Optimizer to to implement optimization recommendations by managing AWS resources in your account. . For more information, see [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles).

**Note**  
You can't attach `ComputeOptimizerAutomationServiceRolePolicy` to your IAM entities.

**Permissions details**

This policy includes the following permissions:
+ `ec2:DescribeVolumes`, `ec2:DescribeSnapshots`, `ec2:DescribeVolumesModifications` – Grants read-only access to view Amazon EBS volumes, snapshots, and volume modification status for monitoring and validation purposes.
+ `ec2:ModifyVolume`, `ec2:DeleteVolume` – Allows modification and deletion of Amazon EBS volumes, but only for resources that do not have the `exclude-from-compute-optimizer-automation`tag. This allows you to exclude resources from automated optimization actions.
+ `ec2:CreateSnapshot` – Grants permission to create snapshots of Amazon EBS volumes for backup purposes before performing optimization actions.
+ `ec2:CreateVolume` – Allows creation of Amazon EBS volumes from snapshots to support rollback operations in case optimization actions need to be reverted.
+ `ec2:CreateTags` – Grants permission to add tags to Amazon EBS resources for tracking automation events and maintaining resource metadata.

To view the permissions for this policy, see [ComputeOptimizerAutomationServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ComputeOptimizerAutomationServiceRolePolicy.html) in the in the *AWS Managed Policy Reference*.

### Compute Optimizer updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Compute Optimizer since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed for this guide.


| Change | Description | Date | 
| --- | --- | --- | 
| Added new `ComputeOptimizerAutomationServiceRolePolicy` managed policy | Added a new `ComputeOptimizerAutomationServiceRolePolicy` service-linked role policy. | November 19, 2025 | 
| Edit to the `ComputeOptimizerServiceRolePolicy` managed policy | Added the `cloudwatch:DescribeAlarms`, `autoscaling:DescribePolicies`, and `autoscaling:DescribeScheduledActions` actions to the `ComputeOptimizerServiceRolePolicy` managed policy. | January 9, 2025 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `compute-optimizer:GetIdleRecommendations` actions to the `ComputeOptimizerReadOnlyAccess` managed policy. | November 20, 2024 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `compute-optimizer:GetRDSDatabaseRecommendations`, `compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics`, `rds:DescribeDBInstances`, and `rds:DescribeDBClusters` actions to the `ComputeOptimizerReadOnlyAccess` managed policy. | June 20, 2024 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `compute-optimizer:GetLicenseRecommendations` actions to the `ComputeOptimizerReadOnlyAccess` managed policy. | July 26, 2023 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `compute-optimizer:GetECSServiceRecommendations`, `compute-optimizer:GetECSServiceRecommendationProjectedMetrics`, `ecs:ListServices`, and `ecs:ListClusters` actions to the `ComputeOptimizerReadOnlyAccess` managed policy. | December 22, 2022 | 
| Edit to the ComputeOptimizerServiceRolePolicy managed policy | Added the ec2:DescribeInstances, ec2:DescribeVolumes, and organizations:ListDelegatedAdministrators actions to the ComputeOptimizerServiceRolePolicy managed policy. | July 25, 2022 | 
| Edit to the `ComputeOptimizerServiceRolePolicy` managed policy | Added the `autoscaling:DescribeAutoScalingInstances` and `autoscaling:DescribeAutoScalingGroups` actions to the `ComputeOptimizerServiceRolePolicy` managed policy. | November 29, 2021 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `compute-optimizer:GetRecommendationPreferences`, `compute-optimizer:GetEffectiveRecommendationPreferences`, and `autoscaling:DescribeAutoScalingInstances` actions to the `ComputeOptimizerReadOnlyAccess` managed policy. | November 29, 2021 | 
| Edit to the `ComputeOptimizerReadOnlyAccess` managed policy | Added the `GetEnrollmentStatusesForOrganization` action to the `ComputeOptimizerReadOnlyAccess` managed policy. | August 26, 2021 | 
| Compute Optimizer started tracking changes | Compute Optimizer started tracking changes for its AWS managed policies. | May 18, 2021 | 

## Using service-linked roles for AWS Compute Optimizer
<a name="using-service-linked-roles"></a>

AWS Compute Optimizer uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that's linked directly to Compute Optimizer. Service-linked roles are predefined by Compute Optimizer and include all of the permissions that the service requires to call other on your behalf. 

With a service-linked role,setting up Compute Optimizer doesn't require manually adding the necessary permissions. Compute Optimizer defines the permissions of its service-linked roles, and unless defined otherwise, only Compute Optimizer can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes ** in the ** Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for Compute Optimizer](#slr-permissions)
+ [Service-linked role permissions](#service-linked-role-permissions)
+ [Creating a Service-Linked Role for Compute Optimizer](#create-slr)
+ [Editing a Service-Linked Role for Compute Optimizer](#edit-slr)
+ [Deleting a Service-Linked Role for Compute Optimizer](#delete-slr)
+ [Supported Regions for Compute Optimizer service-linked Roles](#slr-regions)
+ [Additional resources](#slr-resources)

### Service-linked role permissions for Compute Optimizer
<a name="slr-permissions"></a>

Compute Optimizer uses the service-linked role that's named **AWSServiceRoleForComputeOptimizer** to access Amazon CloudWatch metrics for AWS resources in the account.

The AWSServiceRoleForComputeOptimizer service-linked role trusts the following services to assume the role:
+ `compute-optimizer.amazonaws.com`

The role permissions policy allows Compute Optimizer to complete the following actions on the specified resources:
+ Action: `cloudwatch:GetMetricData` on all AWS resources.
+ Action: `cloudwatch:DescribeAlarms` on all AWS resources.
+ Action: `organizations:DescribeOrganization` on all AWS resources.
+ Action: `organizations:ListAccounts` on all AWS resources.
+ Action: `organizations:ListAWSServiceAccessForOrganization` on all AWS resources.
+ Action: `organizations:ListDelegatedAdministrators` on all AWS resources.
+ Action: `autoscaling:DescribeAutoScalingInstances` on all AWS resources.
+ Action: `autoscaling:DescribeAutoScalingGroups` on all AWS resources.
+ Action: `autoscaling:DescribePolicies` on all AWS resources.
+ Action: `autoscaling:DescribeScheduledActions` on all AWS resources.
+ Action: `ec2:DescribeInstances` on all AWS resources.
+ Action: `ec2:DescribeSnapshots` on all AWS resources.
+ Action: `ec2:DescribeVolumesModifications` on all AWS resources.
+ Action: `ec2:CreateVolume` on all AWS resources.
+ Action: `ec2:ModifyVolume` on all AWS resources.
+ Action: `ec2:DeleteVolume` on all AWS resources.
+ Action: `ec2:CreateSnapshot` on all AWS resources.
+ Action: `ec2:createTags` on all AWS resources.
+ Action: `ec2:DescribeNatGateways` on all AWS resources.
+ Action: `ec2:DescribeRouteTables` on all AWS resources.
+ Action: `elasticache:DescribeCacheClusters` on all AWS resources.
+ Action: `elasticache:DescribeServerlessCaches` on all AWS resources.
+ Action: `memorydb:DescribeClusters` on all AWS resources.
+ Action: `rds:DescribeDBClusters` on all AWS resources.
+ Action: `dynamodb:ListTables` on all AWS resources.
+ Action: `dynamodb:DescribeTable` on all AWS resources.
+ Action: `workspaces:DescribeWorkspaces` on all AWS resources.
+ Action: `workspaces:DescribeWorkspacesConnectionStatus` on all AWS resources.
+ Action: `sagemaker:ListEndpoints` on all AWS resources.
+ Action: `sagemaker:DescribeEndpoint` on all AWS resources.

### Service-linked role permissions
<a name="service-linked-role-permissions"></a>

To create a service-linked role for Compute Optimizer, configure permissions to allow an IAM entity (such as a user, group, or role) to create the service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

**To allow an IAM entity to create a specific service-linked role for Compute Optimizer**

Add the following policy to the IAM entity that needs to create the service-linked role.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer*",
            "Condition": {"StringLike": {"iam:AWSServiceName": "compute-optimizer.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws-cn:iam::*:role/aws-service-role/compute-optimizer.amazonaws.com/AWSServiceRoleForComputeOptimizer"
        },
        {
            "Effect": "Allow",
            "Action": "compute-optimizer:UpdateEnrollmentStatus",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "organizations:DescribeOrganization",
            "Resource": "*"
        }
    ]
}
```

------

**To allow an IAM entity to create any service-linked role**

Add the following statement to the permissions policy for the IAM entity that needs to create a service-linked role, or any service role that includes the needed policies. This policy attaches a policy to the role.

```
{
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/*"
}
```

**To allow Compute Optimizer to perform recommended actions on behalf of customers**

Add a statement to the permissions policy for the IAM entity that needs to create a service-linked role, or any service role that includes the needed policies. This policy attaches a policy to the role. For more information, see [AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy](#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy) on the managed policy page.

### Creating a Service-Linked Role for Compute Optimizer
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you opt in to the Compute Optimizer service in the AWS Management Console, the AWS CLI, or the AWS API, Compute Optimizer creates the service-linked role for you. 

**Important**  
If you completed an action in another service that uses the features supported by the service-linked role, the role can appear in your account. For more information, see [A New Role Appeared in My IAM Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you opt in to the Compute Optimizer service, Compute Optimizer creates the service-linked role for you again. 

### Editing a Service-Linked Role for Compute Optimizer
<a name="edit-slr"></a>

Compute Optimizer doesn't allow you to edit the AWSServiceRoleForComputeOptimizer service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

### Deleting a Service-Linked Role for Compute Optimizer
<a name="delete-slr"></a>

We recommend that, if you no longer need to use Compute Optimizer, you delete the AWSServiceRoleForComputeOptimizer service-linked role. That way you don’t have an unused entity that's not actively monitored or maintained. However, before you can manually delete the service-linked role, you must opt out of Compute Optimizer.

**To opt out of Compute Optimizer**

For information about opting out of Compute Optimizer, see [Opting out of Compute Optimizer](#account-opt-out).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForComputeOptimizer service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Supported Regions for Compute Optimizer service-linked Roles
<a name="slr-regions"></a>

Compute Optimizer supports using service-linked roles in all of the Regions where the service is available. To view the currently supported AWS Regions and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/compute-optimizer.html) in the *AWS General Reference*.

### Additional resources
<a name="slr-resources"></a>
+ Troubleshooting — [Troubleshooting in Compute Optimizer](#troubleshooting-account-opt-in)
+ [AWS managed policies for AWS Compute Optimizer](#managed-policies)
+ [Opting in to AWS Compute Optimizer](#account-opt-in)
+ [Identity and Access Management for AWS Compute Optimizer](#security-iam)

## Using service-linked roles for Automation
<a name="using-service-linked-roles-automation"></a>

AWS Compute Optimizer uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) named AWSServiceRoleForComputeOptimizerAutomation. A service-linked role is a unique type of IAM role that's linked directly to Compute Optimizer Automation. Service-linked roles are predefined by Compute Optimizer Automation and include all of the permissions that the service requires to call other on your behalf. 

With a service-linked role, setting up Compute Optimizer Automation doesn't require manually adding the necessary permissions. Compute Optimizer Automation defines the permissions of its service-linked roles, and unless defined otherwise, only Compute Optimizer Automation can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes ** in the ** Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for Compute Optimizer Automation](#slr-permissions-automation)
+ [Service-linked role permissions](#service-linked-role-permissions-automation)
+ [Creating a Service-Linked Role for Compute Optimizer Automation](#create-slr-automation)
+ [Editing a Service-Linked Role for Compute Optimizer Automation](#edit-slr-automation)
+ [Deleting a Service-Linked Role for Compute Optimizer Automation](#delete-slr-automation)
+ [Supported Regions for Compute Optimizer Automation service-linked Roles](#slr-regions)

### Service-linked role permissions for Compute Optimizer Automation
<a name="slr-permissions-automation"></a>

Compute Optimizer Automation uses the service-linked role that's named **AWSServiceRoleForComputeOptimizerAutomation** which enables access to AWS services and resources used or managed by Compute Optimizer Automation. This service-linked role allows Compute Optimizer Automation to implement optimization recommendations by performing tasks such as creating, modifying, and deleting resources through other AWS services. 

The AWSServiceRoleForComputeOptimizerAutomation service-linked role trusts the `aco-automation.amazonaws.com` services to assume the role.

The `AWSServiceRoleForComputeOptimizerAutomation` service-linked role uses the managed policy `AWSComputeOptimizerAutomationRolePolicy`.

### Service-linked role permissions
<a name="service-linked-role-permissions-automation"></a>

To create a service-linked role for Compute Optimizer Automation, configure permissions to allow an IAM entity (such as a user, group, or role) to create the service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

Add the following policy to the IAM entity that needs to create the service-linked role.

```
{
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": "iam:PutRolePolicy",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        }
    ]
}
```

### Creating a Service-Linked Role for Compute Optimizer Automation
<a name="create-slr-automation"></a>

The AWSServiceRoleForComputeOptimizerAutomation service-linked role is created automatically when you enable Compute Optimizer Automation. You can enable the AWSServiceRoleForComputeOptimizerAutomation manually in the AWS CLI or the IAM API. 

The service-linked role created for a Compute Optimizer Automation management account does not apply to member accounts. Compute Optimizer Automation creates a separate service-linked role for each account when the feature is enabled. When a management account enables Automation for a member account, Compute Optimizer Automation creates the service-linked role on-demand the first time it implements a recommended action for that account. This occurs either when the management account or member account initiates the action directly or when an automation rule executes an action for that member account.

### Editing a Service-Linked Role for Compute Optimizer Automation
<a name="edit-slr-automation"></a>

Compute Optimizer Automation doesn't allow you to edit the AWSServiceRoleForComputeOptimizerAutomation service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

### Deleting a Service-Linked Role for Compute Optimizer Automation
<a name="delete-slr-automation"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete the role. That way, you don't have an unused entity that isn't actively monitored or maintained.

When you disable Compute Optimizer Automation, Compute Optimizer Automation doesn't automatically delete the AWSServiceRoleForComputeOptimizerAutomation service-linked role for you. If you enable Compute Optimizer Automation again, the service can then start using the existing service-linked role again. If you no longer need to use Compute Optimizer Automation, you can manually delete the service-linked role.

**Important**  
Before you delete the AWSServiceRoleForComputeOptimizerAutomation service-linked role, you must first disable Compute Optimizer Automation. If Compute Optimizer Automation isn't disabled when you try to delete the service-linked role, the deletion fails.

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForComputeOptimizerAutomation service-linked role. For more information, see [Deleting a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

### Supported Regions for Compute Optimizer Automation service-linked Roles
<a name="slr-regions"></a>

Compute Optimizer Automation supports using service-linked roles in all of the Regions where the service is available. To view the currently supported AWS Regions and endpoints for Compute Optimizer, see [Compute Optimizer Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/compute-optimizer.html) in the *AWS General Reference*.

# Metrics analyzed by AWS Compute Optimizer
<a name="metrics"></a>

After you [opt in](#getting-started), AWS Compute Optimizer analyzes the specifications, such as vCPUs, memory, or storage, and the Amazon CloudWatch metrics of your running resources from a period over the last 14 days. If you activate the [enhanced infrastructure metrics recommendation preference](#enhanced-infrastructure-metrics), AWS Compute Optimizer analyzes your resources for up to 93 days. 

The analysis can take up to 24 hours to complete. When the analysis is complete, the findings are displayed on the dashboard page of the Compute Optimizer console. For more information, see [Using the AWS Compute Optimizer dashboard](#viewing-dashboard).

**Note**  
To generate recommendations for Amazon EC2 instances, EC2 Auto Scaling groups, Amazon EBS volumes, Lambda functions, and commercial software licenses, Compute Optimizer uses the maximum utilization point within each five-minute time interval over the lookback period. For ECS services on Fargate recommendations, Compute Optimizer uses the maximum utilization point within each one-minute time interval.
AWS might use your utilization data to help improve the overall quality of Compute Optimizer's recommendations. To stop AWS using your utilization data, contact [AWS Support](https://console.aws.amazon.com/support).

**Topics**
+ [EC2 instance metrics](#ec2-metrics-analyzed)
+ [EBS volume metrics](#ebs-metrics-analyzed)
+ [Lambda function metrics](#lambda-metrics-analyzed)
+ [Metrics for Amazon ECS services on Fargate](#ecs-fargate-metrics-analyzed)
+ [Metrics for commercial software licenses](#license-metrics-analyzed)
+ [Aurora and RDS database metrics](#rds-metrics-analyzed)

## EC2 instance metrics
<a name="ec2-metrics-analyzed"></a>

**Topics**
+ [Metrics analyzed for EC2 instances](#ec2-metrics-list)
+ [Enabling memory utilization with the CloudWatch agent](#cw-agent)
+ [Enabling NVIDIA GPU utilization with the CloudWatch agent](#nvidia-cw-agent)
+ [Configure external metrics ingestion](#external-metrics)

### Metrics analyzed for EC2 instances
<a name="ec2-metrics-list"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your EC2 instances, including instances that are part of EC2 Auto Scaling groups.


| Metric | Description | 
| --- | --- | 
|  CPUUtilization  | The percentage of allocated EC2 compute units that are in use on the instance. This metric identifies the processing power that's required to run an application on an instance. | 
|  MemoryUtilization  | The percentage of memory that's used during the sample period. This metric identifies the memory that's required to run an application on an instance.<br />Memory utilization metrics are analyzed for the following resources:+  EC2 instances with the CloudWatch agent that's installed on them. For more information, see [Enabling memory utilization with the CloudWatch agent](#cw-agent). <br />+  External EC2 instances from one of the four observability products: Datadog, Dynatrace, Instana, and New Relic. For more information, see [ External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion).  | 
|  GPUUtilization  | The percentage of allocated GPUs that are currently in use on the instance. To allow Compute Optimizer analyze the GPU utilization metric of your instances, install the CloudWatch agent on your instances. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch agent](#nvidia-cw-agent).  | 
|  GPUMemoryUtilization  | The percentage of total GPU memory that's currently in use on the instance. | 
|  GPUEncoderStatsSessionCount  | The number of active encoding sessions on an NVIDIA GPU. | 
|  NetworkIn  | The number of bytes that's received on all network interfaces by the instance. This metric identifies the volume of incoming network traffic to an instance. | 
|  NetworkOut  | The number of bytes that are sent out on all network interfaces by the instance. This metric identifies the volume of outgoing network traffic from an instance. | 
|  NetworkPacketsIn  | The number of packets that are received by the instance. | 
|  NetworkPacketsOut  | The number of packets that are sent out by the instance. | 
|  DiskReadOps  | The read operations per second of the instance store volume of the instance. | 
|  DiskWriteOps  | The write operations per second of the instance store volume of the instance. | 
|  DiskReadBytes  | The read bytes per second of the instance store volume of the instance. | 
|  DiskWriteBytes  | The write bytes per second of the instance store volume of the instance. | 
|  VolumeReadBytes  | The read bytes per second of EBS volumes attached to the instance. Displayed as KiBs in the console. | 
|  VolumeWriteBytes  | The write bytes per second of EBS volumes attached to the instance. Displayed as KiBs in the console. | 
|  VolumeReadOps  | The read operations per second of EBS volumes attached to the instance. | 
|  VolumeWriteOps  | The write operations per second of EBS volumes attached to the instance. | 

For more information about instance metrics, see [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about EBS volume metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.

### Enabling memory utilization with the CloudWatch agent
<a name="cw-agent"></a>

To have Compute Optimizer analyze the memory utilization metric of your instances, install the CloudWatch agent on your instances. Enabling Compute Optimizer to analyze memory utilization data for your instances provides an additional measurement of data that further improves Compute Optimizer's recommendations. For more information about installing the CloudWatch agent, see [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) in the *Amazon CloudWatch User Guide*.

On Linux instances, Compute Optimizer analyses the `mem_used_percent` metric in the `CWAgent` namespace, or the legacy `MemoryUtilization` metric in the `System/Linux` namespace. On Windows instances, Compute Optimizer analyses the `Available MBytes` metric in the `CWAgent` namespace. If both the `Available MBytes` and `Memory % Committed Bytes In Use` metrics are configured in the `CWAgent` namespace, Compute Optimizer chooses `Available MBytes` as the primary memory metric to generate recommendations.

**Note**  
We recommend that you configure the `CWAgent` namespace to use `Available MBytes` as your memory metric for Windows instances.
Compute Optimizer also supports the `Available KBytes` and `Available Bytes` metrics, and prioritizes both over the `Memory % Committed Bytes In Use` metric when generating recommendations for Windows instances.

Additionally, the namespace must contain the `InstanceId` dimension. If the `InstanceId` dimension is missing or you overwrite it with a custom dimension name, Compute Optimizer can't collect memory utilization data for your instance. Namespaces and dimensions are defined in the CloudWatch agent configuration file. For more information, see [Create the CloudWatch agent Configuration File](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html) in the *Amazon CloudWatch User Guide*.

**Important**  
All of the CloudWatch namespaces and metric names are case sensitive.

**Example: CloudWatch agent configuration for memory collection**

```
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "root"
    },
    "metrics": {
        "namespace": "CWAgent",
        "append_dimensions": {
            "InstanceId": "${aws:InstanceId}"
        },
        "metrics_collected": {
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 60
            }
        }
    }
}
```

### Enabling NVIDIA GPU utilization with the CloudWatch agent
<a name="nvidia-cw-agent"></a>

To allow Compute Optimizer to analyze the NVIDIA GPU utilization metric of your instances, do the following:

1. Install the CloudWatch agent on your instances. For more information, see [Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) in the *Amazon CloudWatch User Guide*.

1. Allow the CloudWatch agent to collect NVIDIA GPU metrics. For more information, see [Collect NVIDIA GPU metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) in the *Amazon CloudWatch User Guide*.

Compute Optimizer analyzes the following NVIDIA GPU metrics:
+ `nvidia_smi_utilization_gpu`
+ `nvidia_smi_memory_used`
+ `nvidia_smi_encoder_stats_session_count`
+ `nvidia_smi_encoder_stats_average_fps`
+ `nvidia_smi_encoder_stats_average_latency`
+ `nvidia_smi_temperature_gpu`

The namespace must contain the `InstanceId` dimension and `index` dimensions. If the dimensions are missing or you overwrite them with a custom dimension name, Compute Optimizer can't collect GPU utilization data for your instance. Namespaces and dimensions are defined in the CloudWatch agent configuration file. For more information, see [Create the CloudWatch agent Configuration File](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html) in the *Amazon CloudWatch User Guide*.

### Configure external metrics ingestion
<a name="external-metrics"></a>

You can use the external metrics ingestion feature to configure AWS Compute Optimizer to ingest EC2 memory utilization metrics from one of the four observability products: Datadog, Dynatrace, Instana, and New Relic. When you enable external metrics ingestion, Compute Optimizer analyzes your external EC2 memory utilization metrics in addition to your CPU, disk, network, IO, and throughput data to generate EC2 rightsizing recommendations. These recommendations can provide you with additional savings and enhanced performance. For more information, see [External metrics ingestion](#external-metrics-ingestion).

## EBS volume metrics
<a name="ebs-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your EBS volumes.


| Metric | Description | 
| --- | --- | 
|  VolumeReadBytes  | The read bytes per second of the EBS volume. | 
|  VolumeWriteBytes  | The write bytes per second of the EBS volume. | 
|  VolumeReadOps  | The read operations per second of the EBS volume. | 
|  VolumeWriteOps  | The write operations per second of the EBS volume. | 
|  VolumeIOPSExceededCheck  | Reports whether an application consistently attempted to drive IOPS that exceeds the volume's provisioned IOPS performance within the last minute. This metric can be either 0 (provisioned IOPS not exceeded) or 1 (provisioned IOPS exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 
|  VolumeThroughputExceededCheck  | Reports whether an application consistently attempted to drive throughput that exceeds the volume's provisioned throughput performance within the last minute. This metric can be either 0 (provisioned throughput not exceeded) or 1 (provisioned throughput exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 

For more information about these metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Lambda function metrics
<a name="lambda-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your Lambda functions.


| Metric | Description | 
| --- | --- | 
|  Invocations  | The number of times your function code is executed, including successful executions and executions that result in a function error. | 
|  Duration  | The amount of time that your function code spends processing an event. | 
|  Errors  | The number of invocations that result in a function error. Function errors include exceptions thrown by your code and exceptions thrown by the Lambda runtime. The runtime returns errors for issues such as timeouts and configuration errors. | 
|  Throttles  | The number of invocation requests that are throttled. | 

For more information about these metrics, see [Working with AWS Lambda function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html) in the *AWS Lambda Developer Guide*.

In addition to these metrics, Compute Optimizer analyzes the memory utilization of your function during the look-back period. For more information about memory utilization for Lambda functions, see [Understanding AWS Lambda behavior using Amazon CloudWatch Logs Insights](https://aws.amazon.com/blogs/mt/understanding-aws-lambda-behavior-using-amazon-cloudwatch-logs-insights/) in the *AWS Management & Governance Blog* and [Using Lambda Insights in CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-insights.html) in the *AWS Lambda Developer Guide*.

## Metrics for Amazon ECS services on Fargate
<a name="ecs-fargate-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch and Amazon ECS utilization metrics of your Amazon ECS services on Fargate.


| Metric | Description | 
| --- | --- | 
|  CPUUtilization  | The percentage of CPU capacity that's used in the service. | 
|  MemoryUtilization  | The percentage of memory that's used in the service. | 

For more information about these metrics, see [Amazon ECS CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/userguide/cloudwatch-metrics.html) in the *Amazon ECS User Guide for AWS Fargate*.

## Metrics for commercial software licenses
<a name="license-metrics-analyzed"></a>

Compute Optimizer analyzes the following metric to generate recommendations for commercial software licenses.

**`mssql_enterprise_features_used`** — the number of Microsoft SQL Server Enterprise edition features in use. The features are as follows:
+ More than 128GB of memory for the buffer pool extension
+ More than 48 vCPUs
+ Always On availability groups with more than 1 database
+ Asynchronous commit replicas
+ Read-only replicas
+ Asynchronous database mirroring
+ `tempdb` memory-optimized metadata is enabled
+ R or Python extensions
+ Peer-to-peer replication
+ Resource Governor

## Aurora and RDS database metrics
<a name="rds-metrics-analyzed"></a>

Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora and RDS databases.

------
#### [ RDS DB instances ]

Compute Optimizer analyzes the following CloudWatch metrics of your Amazon RDS DB instances.


| Metric | Description | 
| --- | --- | 
|  CPUUtilization  | The percentage of allocated compute units that are in use on the DB instance. This metric identifies the processing power that's required to run an application on an instance. | 
|  DatabaseConnections  | The number of client sessions that are connected to the DB instance. | 
|  NetworkReceiveThroughput  | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
|  NetworkTransmitThroughput  | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
|  ReadIOPS  | The average number of disk read I/O operations per second. | 
|  WriteIOPS  | The average number of disk write I/O operations per second. | 
|  ReadThroughput  | The average number of bytes read from disk per second. | 
|  WriteThroughput  | The average number of bytes written to disk per second. | 
|  EBSIOBalance%  | The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
|  EBSByteBalance%  | The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
|  FreeStorageSpace  | The amount of available storage space. | 

If you enabled Amazon RDS Performance Insights, Compute Optimizer also analyzes the following metrics of your Amazon RDS DB instance. To enable Performance Insights for your DB instances, see [ Turning Performance Insights on and off for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Relational Database Service User Guide*.

**Note**  
If Performance Insights isn’t enabled, Compute Optimizer doesn’t provide recommendations to reduce vCPU capacity.


| Metric | Description | 
| --- | --- | 
|  DBLoad  | The level of session activity in your database. For more information, see [ Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html) in the *Amazon Relational Database Service User Guide*. | 
|  os.swap.in  | The amount of memory, in kilobytes, swapped in from disk. | 
|  os.swap.out  | The amount of memory, in kilobytes, swapped out to disk. | 

For more information about Amazon RDS metrics, see [ Metrics reference for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/metrics-reference.html) in the *Amazon Relational Database Service User Guide*.

------
#### [ Aurora DB instances ]

Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora DB instances.


| Metric | Description | 
| --- | --- | 
|  CPUUtilization  | The percentage of CPU used by an Aurora DB instance. | 
|  DatabaseConnections  | The number of client network connections to the database instance. | 
|  NetworkReceiveThroughput  | The amount of network throughput received from clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the Aurora DB cluster and the cluster volume. | 
|  NetworkTransmitThroughput  | The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | 
|  StorageNetworkReadThroughput  | The amount of network throughput received from the Aurora storage subsystem by each instance in the DB cluster. | 
|  StorageNetworkWriteThroughput  | The amount of network throughput sent to the Aurora storage subsystem by each instance in the Aurora DB cluster. | 
|  AuroraMemoryHealthState  | Indicates the memory health state. A value of `0` equals `NORMAL`. A value of `10` equals `RESERVED`, which means that the server is approaching a critical level of memory usage.  This metric applies to Aurora MySQL only.  | 
|  AuroraMemoryNumDeclinedSqlTotal  | The total number of queries declined as part of out-of-memory (OOM) avoidance. This metric applies to Aurora MySQL only.  | 
|  AuroraMemoryNumKillConnTotal  | The total number of connections closed as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
|  AuroraMemoryNumKillQueryTotal  | The total number of queries ended as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
|  ReadIOPSEphemeralStorage  | The average number of disk read I/O operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
|  WriteIOPSEphemeralStorage  | The average number of disk write I/O operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
|  ReadIOPS  | The average number of disk I/O operations per second but the reports read and write separately, in 1-minute intervals. | 
|  WriteIOPS  | The number of Aurora storage write records generated per second. This is more or less the number of log records generated by the database. These do not correspond to 8K page writes, and do not correspond to network packets sent. | 

For more information, see [ Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*.

If you enabled Performance Insights for Aurora, Compute Optimizer also analyzes the following metrics of your Aurora DB instances. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*.


| Metric | Description | 
| --- | --- | 
|  DBLoad  | The number of active sessions for the database. Typically, you want the data for the average number of active sessions. In Performance Insights, this data is queried as db.load.avg. | 
|  os.memory.outOfMemoryKillCount  | The number of OOM kills that happened over the last collection interval. | 

For more information about Aurora metrics, see [ Metrics reference for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/metrics-reference.html) in the *Amazon Aurora User Guide*.

------
#### [ Aurora DB clusters ]

Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora DB clusters.


| Metric | Description | 
| --- | --- | 
|  VolumeReadIOPs  | The number of billed read I/O operations from a cluster volume within a 5-minute interval. | 
|  VolumeWriteIOPs  | The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals. | 

**Note**  
Compute Optimizer analyzes these metrics to estimate the I/O cost variability over the lookback period. The Aurora DB cluster storage recommendations are based on analyzing instance costs, storage costs, and I/O costs.

------

# Using the AWS Compute Optimizer dashboard
<a name="viewing-dashboard"></a>

Use the dashboard in the Compute Optimizer console to evaluate and prioritize the optimization opportunities for the supported resource types in your account. The dashboard displays the following information, which is refreshed daily and generated by analyzing the specifications and utilization metrics of your resources.

**Topics**
+ [Savings opportunity](#dashboard-savings-opportunities)
+ [Performance improvement opportunity](#dashboard-performance-improvement-opportunities)
+ [Optimization options per resource](#dashboard-optimization-options)
+ [Viewing the dashboard](#viewing-the-dashboard)

## Savings opportunity
<a name="dashboard-savings-opportunities"></a>

The savings opportunity section displays the total estimated monthly USD amount and percentage that you could save if you implement the Compute Optimizer recommendations for resources in your account. You can choose to display the estimated monthly savings by resource type or savings type. If you prefer to evaluate your resources for cost savings, then prioritize the resource type that has the greatest savings opportunity.

Using EC2 as an example, the estimated monthly savings and savings opportunity for individual EC2 instances are listed in the EC2 instances recommendations page under the **Estimated monthly savings (after discounts)**, **Estimated monthly savings (On-Demand)**, and **Savings opportunity (%)** columns. For more information, including how estimated monthly savings is calculated, see [Estimated monthly savings and savings opportunity](#ec2-savings-calculation).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

![Performance risk reduction opportunity in the Compute Optimizer dashboard](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/dashboard-savings-opportunities.png)


## Performance improvement opportunity
<a name="dashboard-performance-improvement-opportunities"></a>

The performance improvement opportunity section displays a count and percentage of the resources in your account that Compute Optimizer found to be at risk of not meeting your workload performance needs. It also displays the performance risk classifications per resource type. Resources can have a performance risk of high, medium, and very low. If you prefer to evaluate your resources for performance improvements, then prioritize the resource types that have a high performance risk.

![Savings opportunity in the Compute Optimizer dashboard](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/dashboard-performance-improvement-opportunities.png)


## Optimization options per resource
<a name="dashboard-optimization-options"></a>

This table in the dashboard provides a breakdown of optimization opportunities across your different resource types. It outlines the potential savings that you can achieve by identifying and addressing resources that are not optimized, idle, or inefficiently sized.
+ The **Savings opportunity** column displays the potential cost savings that you can achieve through optimization. Note that the saving opportunity might not be equal to the sum of the idle, rightsize, and license savings figures.
+ The **Optimized**, **Not optimized**, and **Idle** columns indicate the current state of your resources utilization, helping to identify areas for improvement.
+ The **Idle savings**, **Rightsizing savings**, and **License savings** columns quantify the potential cost savings that you can achieve by addressing your idle clean-up opportunities, rightsizing your resources, and using our recommended license configurations.

You can use this table as a comprehensive guide to identify optimization opportunities, prioritize areas for improvement, and estimate the financial impact of various optimization strategies for your AWS resources.

## Viewing the dashboard
<a name="viewing-the-dashboard"></a>

Use the following procedure to view the dashboard and the optimization findings for your resources.

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Dashboard** in the navigation pane.

   By default, the dashboard displays an overview of optimization findings for AWS resources across all AWS Regions in the account that you're currently signed in to.

1. You can perform the following actions on the dashboard:
   + To view the optimization findings for resources in another account, choose **Account**, and then select a different account ID.
**Note**  
The ability to view optimization findings for resources in other accounts is available only if you're signed in to a management account of an organization, you opted in all member accounts of the organization, and trusted access with Compute Optimizer is enabled. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + To show or hide the savings opportunity and performance improvement opportunity sections of the dashboard, choose the gear icon, choose the sections that you want to show or hide, and choose **Apply**.
   + To filter findings on the dashboard to one or more AWS Regions, enter the name of the Region in the **Filter by one or more Regions** text box, or choose one or more Regions in the drop-down list that appears.
   + To clear the selected filters, choose **Clear filters** next to the filter.
   + To view optimization recommendations, choose the **View recommendations** link for one of the resource types displayed, or choose the number of resources listed next to a findings classification to view the resources for that classification. For more information, see [Viewing resource recommendations](#viewing-recommendations).

# Viewing resource recommendations
<a name="viewing-recommendations"></a>

Recommendations for your AWS resources are displayed in the following pages of the AWS Compute Optimizer console.
+ The **resources recommendations** page lists each of your running resources, along with their top recommendation generated by Compute Optimizer.
+ The **resource details** page lists the top recommendation options for a specific resource, along with utilization metric graphs for the resource. You can access this page from the recommendations page.

The recommendations and resource details pages are available for each of the following AWS resources that are supported by Compute Optimizer:
+ [ Amazon EC2 instances](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html)
+ [ EC2 Auto Scaling groups](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-asg-recommendations.html)
+  [ Amazon EBS volumes](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html)
+  [AWS Lambda functions](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html)
+  [ Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ecs-recommendations.html) 
+  [ Commercial software licenses](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations.html) 
+  [ Amazon RDS DB instances](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html) 
+  [ Idle resources](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html) 

## Viewing EC2 instance recommendations
<a name="view-ec2-recommendations"></a>

AWS Compute Optimizer generates instance type recommendations for Amazon Elastic Compute Cloud (Amazon EC2) instances. Recommendations for your Amazon EC2 instances are displayed on the following pages of the Compute Optimizer console:
+ The **EC2 instances recommendations** page lists each of your current instances, their [finding classifications](#ec2-recommendations-findings), [finding reasons](#ec2-finding-reasons), [platform differences](#ec2-platform-differences), current instance type, and current hourly price for the selected purchasing option. The top recommendation from Compute Optimizer is listed next to each of your instances. This recommendation includes the recommended instance type, the hourly price for the selected purchasing option, and the price difference between your current instance. Use the recommendations page to compare your current instances with their top recommendation. Doing this can help you to decide if you want to up-size or down-size your instances.
+ The **EC2 instance details** page lists up to three optimization recommendations for a specific instance. You can access this page from the EC2 instances recommendations page. The page specifically lists the specifications for each recommendation, their [performance risk](#ec2-performance-risk), and their hourly prices for the selected purchasing option. The details page also displays utilization metric graphs for the current instance, overlaid with the projected utilization metrics for the recommendation options.

The recommendations are refreshed daily. These recommendations are generated by analyzing the specifications and utilization metrics of the current instance over a period of the last 14 days. Or, if you activate the [enhanced infrastructure metrics paid feature](#enhanced-infrastructure-metrics), the recommendations are generated by analyzing a longer period of time. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

Keep in mind that Compute Optimizer generates recommendations for EC2 instances that meet a specific set of requirements. Recommendations can take up to 24 hours to be generated. Moreover, sufficient metric data must be accumulated for recommendations to be generated. For more information, see [Resource requirements](#requirements).

**Topics**
+ [Finding classifications](#ec2-recommendations-findings)
+ [Finding reasons](#ec2-finding-reasons)
+ [AWS Graviton-based instance recommendations](#ec2-graviton-recommendations)
+ [Inferred workload types](#ec2-inferred-workload-types)
+ [Migration effort](#ec2-migration-effort)
+ [Platform differences](#ec2-platform-differences)
+ [Estimated monthly savings and savings opportunity](#ec2-savings-calculation)
+ [Performance risk](#ec2-performance-risk)
+ [Utilization graphs](#ec2-utilization-graphs)
+ [Accessing EC2 instance recommendations and details](#ec2-view-recommendations)

### Finding classifications
<a name="ec2-recommendations-findings"></a>

The **Finding** column on the **EC2 instances recommendations** page provides a summary of how each of your instances performed during the analyzed period.

The following findings classifications apply to EC2 instances.


| Classification | Description | 
| --- | --- | 
| Under-provisioned | An EC2 instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned EC2 instances might lead to poor application performance. | 
| Over-provisioned | An EC2 instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and when no specification is under-provisioned. Over-provisioned EC2 instances might lead to unnecessary infrastructure cost. | 
| Optimized | An EC2 instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload, and the instance is not over-provisioned. For optimized instances, Compute Optimizer might sometimes recommend a new generation instance type. | 

### Finding reasons
<a name="ec2-finding-reasons"></a>

The **Finding reasons** column on the **EC2 instances recommendations** and **EC2 instance details** pages shows which specification of an instance is under-provisioned or over-provisioned.

The following finding reasons apply to instances:


| Finding reason | Description | 
| --- | --- | 
| CPU over-provisioned | The instance’s CPU configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period. | 
| CPU under-provisioned | The instance’s CPU configuration doesn't meet the performance requirements of your workload and there's an alternative instance type that provides better CPU performance. This is identified by analyzing the `CPUUtilization` metric of the current instance during the look-back period. | 
| Memory over-provisioned | The instance’s memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the memory utilization metric of the current instance during the look-back period. Memory utilization is analyzed only for resources with the unified CloudWatch agent installed. For more information, see [Enabling memory utilization with the Amazon CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent).  | 
| Memory under-provisioned | The instance’s memory configuration doesn't meet the performance requirements of your workload and there's an alternative instance type that provides better memory performance. This is identified by analyzing the memory utilization metric of the current instance during the look-back period. | 
| GPU over-provisioned | The instance’s GPU and GPU memory configurations can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `GPUUtilization` and `GPUMemoryUtilization` metrics of the current instance during the look-back period. The GPU utilization and GPU memory utilization metrics are analyzed only for resources with the unified CloudWatch agent installed. For more information, see [Enabling NVIDIA GPU utilization with the CloudWatch agent](#nvidia-cw-agent).  | 
| GPU under-provisioned | The instance’s GPU and GPU memory configurations don't meet the performance requirements of your workload and there's an alternative instance type that provides better memory performance. This is identified by analyzing the `GPUUtilization` and `GPUMemoryUtilization` metrics of the current instance during the look-back period. | 
| EBS throughput over-provisioned | The instance’s EBS throughput configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes attached to the current instance during the look-back period. | 
| EBS throughput under-provisioned | The instance’s EBS throughput configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes that are attached to the current instance during the look-back period. | 
| EBS IOPS over-provisioned | The instance’s EBS IOPS configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the look-back period. | 
| EBS IOPS under-provisioned | The instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better EBS IOPS performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the look-back period. | 
| Network bandwidth over-provisioned | The instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `NetworkIn` and `NetworkOut `metrics of the current instance during the look-back period. | 
| Network bandwidth under-provisioned | The instance’s network bandwidth configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better network bandwidth performance. This is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the look-back period. This finding reason happens when the `NetworkIn` or `NetworkOut` performance of an instance is impacted. | 
| Network PPS over-provisioned | The instance’s network PPS (packets per second) configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsOut` metrics of the current instance during the look-back period. | 
| Network PPS under-provisioned | The instance’s network PPS (packets per second) configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better network PPS performance. This is identified by analyzing the `NetworkPacketsIn` and `NetworkPacketsOut` metrics of the current instance during the look-back period. | 
| Disk IOPS over-provisioned | The instance’s disk IOPS configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period. | 
| Disk IOPS under-provisioned | The instance’s disk IOPS configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better disk IOPS performance. This is identified by analyzing the `DiskReadOps` and `DiskWriteOps` metrics of the current instance during the look-back period. | 
| Disk throughput over-provisioned | The instance’s disk throughput configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period. | 
| Disk throughput under-provisioned | The instance’s disk throughput configuration doesn't meet the performance requirements of your workload. And, there's an alternative instance type that provides better disk throughput performance. This is identified by analyzing the `DiskReadBytes` and `DiskWriteBytes` metrics of the current instance during the look-back period. | 

**Note**  
For more information about instance metrics, see [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about EBS volume metrics, see [Amazon CloudWatch metrics for Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.

You can change an instance's CPU, local disk, memory, or network specifications by changing the type of the instance. For example, you can change the instance type from C5 to C5n to help improve network performance. For more information, see [Change the instance type guide for Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) and [Change the instance type guide for Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-resize.html) in the *EC2 User Guides*.

You can change an EBS volume's IOPS or throughput specifications by using Amazon EBS Elastic Volumes. For more information, see [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html) in the *Amazon Elastic Compute Cloud User Guide*.

### AWS Graviton-based instance recommendations
<a name="ec2-graviton-recommendations"></a>

When viewing Amazon EC2 instance recommendations, you can view the price and performance impact of running your workload on AWS Graviton-based instances. To do so, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, choose **Current** to view recommendations that are based on the same CPU vendor and architecture as the current instance.

![Graviton based instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/ec2-graviton-based-recommendations.png)


**Note**  
The **Current price**, **Recommended price**, **Price difference**, **Price difference (%)**, and **Estimated monthly savings** columns are updated to provide a price comparison between the current instance type and the instance type of the selected CPU architecture preference. For example, if you choose **Graviton (aws-arm64)**, prices are compared between the current instance type and the recommended Graviton-based instance type.

### Inferred workload types
<a name="ec2-inferred-workload-types"></a>

The **Inferred workload types** column on the **EC2 instances recommendations** page lists the applications that might be running on the instance as inferred by Compute Optimizer. This column does this by analyzing the attributes of your instances. These attributes include the instance name, tags, and configuration. Compute Optimizer can currently infer if your instances are running Amazon EMR, Apache Cassandra, Apache Hadoop, Memcached, NGINX, PostgreSQL, Redis, Kafka, or SQLServer. By inferring the applications that run on your instances, Compute Optimizer can identify the effort to migrate your workloads from x86-based instance types to Arm-based AWS Graviton instances types. For more information, see [Migration effort](#ec2-migration-effort) in the next section of this guide.

**Note**  
You can't infer the SQLServer application in the Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hong Kong), Europe (Milan), and Asia Pacific (Jakarta) Regions.

### Migration effort
<a name="ec2-migration-effort"></a>

The **Migration effort** column on the **EC2 Auto Scaling groups recommendations** and **EC2 Auto Scaling groups details** pages lists the level of effort that might be required to migrate from the current instance type to the recommended instance type. The following shows examples of the different levels of migration effort.
+ **Very low** — The recommended instance type has the same CPU architecture as the current instance type.
+ **Low** — Amazon EMR is the inferred workload type and an AWS Graviton instance type is recommended
+ **Medium** — A workload type can't be inferred but an AWS Graviton instance type is recommended.
+ **High** — The recommended instance type has different CPU architecture from the current instance type, and the workload has no known compatible version on the recommended CPU architecture.

For more information about migrating from x86-based instance types to Arm-based AWS Graviton instances type, see [Considerations when transitioning workloads to AWS Graviton2 based Amazon EC2 instances ](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md) in the *AWS Graviton Getting Starged GitHub*.

### Platform differences
<a name="ec2-platform-differences"></a>

The **Platform differences** column on the **EC2 instance details** page describes the differences between the current instance and the recommended instance type. Consider the configuration differences before migrating your workloads from the current instance to the recommended instance type.

The following platform differences apply to EC2 instances:


| Platform difference | Description | 
| --- | --- | 
| Architecture | The CPU architecture of the recommended instance type is different than that of the current instance type. For example, the recommended instance type might use an Arm CPU architecture and the current instance type might use a different one, such as x86. Before migrating, consider recompiling the software on your instance for the new architecture. Alternatively, you might switch to an Amazon Machine Image (AMI) that supports the new architecture. For more information about the CPU architecture for each instance type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/). | 
| Hypervisor | The hypervisor of the recommended instance type is different than that of the current instance. For example, the recommended instance type might use a Nitro hypervisor and the current instance might use a Xen hypervisor. For information about the differences that you can consider between these hypervisors, see [Nitro Hypervisor](https://aws.amazon.com/ec2/faqs/#Nitro_Hypervisor) section of the Amazon EC2 FAQs. For more information, see [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide for Linux*, or [Instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide for Windows*. | 
| Instance store availability | The recommended instance type doesn't support instance store volumes, but the current instance does. Before migrating, you might need to back up the data on your instance store volumes if you want to preserve them. For more information, see [How do I back up an instance store volume on my Amazon EC2 instance to Amazon EBS?](https://aws.amazon.com/premiumsupport/knowledge-center/back-up-instance-store-ebs/) in the *AWS Premium Support Knowledge Base*. For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Linux*, or see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Windows*. | 
| Network interface | The network interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type might use enhanced networking and the current instance might not. To enable enhanced networking for the recommended instance type, install the Elastic Network Adapter (ENA) driver or the Intel 82599 Virtual Function driver. For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Enhanced networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) in the *Amazon EC2 User Guide for Linux*, or [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Enhanced networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html) in the *Amazon EC2 User Guide for Windows*. | 
| Storage interface | The storage interface of the recommended instance type is different than that of the current instance. For example, the recommended instance type uses an NVMe storage interface and the current instance doesn't such this interface. To access NVMe volumes for the recommended instance type, install or upgrade the NVMe driver. For more information, see [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-networking-storage) and [Amazon EBS and NVMe on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html) in the *Amazon EC2 User Guide for Linux*, or [Networking and storage features](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instance-types.html#instance-networking-storage) and [Amazon EBS and NVMe on Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/nvme-ebs-volumes.html) in the *Amazon EC2 User Guide for Windows*. | 
| Virtualization type | The recommended instance type uses the hardware virtual machine (HVM) virtualization type and the current instance uses the paravirtual (PV) virtualization type. For more information about the differences between these virtualization types, see [Linux AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html) in the *Amazon EC2 User Guide for Linux*, or [Windows AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html#virtualization-types) in the *Amazon EC2 User Guide for Windows*. | 

### Estimated monthly savings and savings opportunity
<a name="ec2-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current instance type to the recommended instance type under the Savings Plans and Reserved Instances pricing models. To receive recommendations with Savings Plans and Reserved Instances discounts, the savings estimation mode preference needs to be activated. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current instance type to the recommended instance type under the On-Demand pricing model. 

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current instance and the price of the recommended instance type. If savings estimation mode is activated, Compute Optimizer analyzes the Savings Plans and Reserved Instances pricing discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

#### Estimated monthly savings calculation
<a name="ec2-estimated-monthly-savings-calculation"></a>

For each recommendation, the cost to operate a new instance using the recommended instance type is calculated. Estimated monthly savings are calculated based on the number of running hours for the current instance and the difference in rates between the current instance type and the recommended instance type. The estimated monthly savings for instances that are displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all over-provisioned instances in the account.

### Performance risk
<a name="ec2-performance-risk"></a>

The performance risk columns on the **EC2 instance details** page and the **EC2 instance recommendations** page define the likelihood of the current and recommended instance type not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the current and recommended instance. This includes specifications such as CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the current and recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A very low performance risk means that the instance type is predicted to always provide enough capability. The higher the performance risk means that you should validate whether the instance type meets the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. For more information, see [Changing the Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Note**  
In the Compute Optimizer API, the AWS Command Line Interface (AWS CLI), and the AWS SDKs, performance risk is measured on a scale of `0` (very low) to `4` (very high).

### Utilization graphs
<a name="ec2-utilization-graphs"></a>

The **EC2 instance details** page displays utilization metric graphs for your current instance. The graphs display data for the analyzed period. Compute Optimizer uses the maximum utilization point within each 5 minute time interval to generate EC2 instance recommendations.

You can change the graphs to display data for the last 24 hours, 3 days, 1 week, or 2 weeks. If you activate the [enhanced infrastructure metrics paidfeature](#enhanced-infrastructure-metrics), you can view 3 months. You can also change the statistic of the graphs between average and maximum.

**Note**  
For periods of time when your instances are in a stopped state, the utilization graphs show a value of 0.

The following utilization graphs are displayed on the details page:


| Graph name | Description | 
| --- | --- | 
| CPU utilization (percent) | The percentage of allocated EC2 compute units used by the instance.<br />The CPU utilization graph includes a comparison of the CPU utilization data of your current instance type against that of the selected recommended instance type. The comparison shows you what the CPU utilization is if you use the selected recommended instance type during the analyzed period. This comparison can help you to identify if the recommended instance type is within your workload's performance threshold. The **Burstable baseline** only displays for T-instances. You can use this baseline performance to learn how your CPU utilization relates to the baseline utilization of the specific T-instance. For more information, see [ Key concepts and definitions for burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html) in the *Amazon EC2 User Guide for Linux Instances*.  | 
| Memory utilization (percent) | The percentage of memory allocated by applications and the operating system as used.<br />The memory utilization graph includes a comparison of the memory utilization data of your current instance type against that of the selected recommended instance type. The comparison shows you what the memory utilization is if you use the selected recommended instance type during the analyzed period. This comparison can help you to identify if the recommended instance type is within your workload's performance threshold. The memory utilization graph is populated only for instances that have the unified CloudWatch agent installed on them. For more information, see [Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) in the *Amazon CloudWatch User Guide*.  | 
| Network in (MiB/second) | The number of mebibytes (MiB) per second received on all network interfaces by the instance. | 
| Network out (MiB/second) | The number of mebibytes (MiB) per second sent out on all network interfaces by the instance. | 
| Network packets in (per second) | The number of packets received by the instance on all network interfaces. | 
| Network packets out (per second) | The number of packets sent out by the instance on all network interfaces. | 
| Disk read operations (per second) | The completed read operations per second from the instance store volumes of the instance. | 
| Disk write operations (per second) | The completed write operations per second from the instance store volumes of the instance. | 
| Disk read bandwidth (MiB/second) | The read mebibytes (MiB) per second from the instance store volumes of the instance. | 
| Disk write bandwidth (MiB/second) | The write mebibytes (MiB) per second from the instance store volumes of the instance. | 
| EBS read operations (per second) | The completed read operations per second from all EBS volumes attached to the instance.<br />For Xen instances, data is reported only when there is read activity on the volume. | 
| EBS write operations (per second) | The completed write operations per second to all EBS volumes attached to the instance.<br />For Xen instances, data is reported only when there is write activity on the volume. | 
| EBS read bandwidth (MiB/second) | The read mebibytes (MiB) per second from all EBS volumes attached to the instance. | 
| EBS write bandwidth (MiB/second) | The written mebibytes (MiB) per second to all EBS volumes attached to the instance. | 

### Accessing EC2 instance recommendations and details
<a name="ec2-view-recommendations"></a>

You can use one of the following procedures to access either the **EC2 instances recommendations** or the **EC2 instance details** pages in the AWS Console.

On the **EC2 instances recommendations** page you can view the recommendations for your current instances. On the **EC2 instance details** page you can view the details of a specific instance and its recommendations.

#### Procedures
<a name="ec2-view-process"></a>

##### Accessing EC2 instance recommendations page
<a name="w2aac23c11c35b7b3b1"></a>

**To access the EC2 instances recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EC2 instances** in the navigation pane.

   The recommendations page lists the specifications and finding classifications of your current instances and the specifications of the recommended instances. The current instances listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations page:
   + View the price and performance impact of running your workload on AWS Graviton-based instances. To do this, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown list. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current instance.
   + Filter recommendations by AWS Regions, Findings, Finding reasons, or Inferred Workload Type. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the dropdown list that appears.
   + Filter your recommendations by tags. To do this, first select the **Tag key** or **Tag value** text box. Then, enter the key or value that you want to filter your EC2 instance recommendations by.

     For example, to find all the recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View recommendations for instances in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.
   + Access the **EC2 instance details** page for a specific instance. To do this, choose the finding classification listed next to the instance that you want to access.

##### Accessing EC2 instance details page
<a name="ec2-viewing-details"></a>

**To access the EC2 instance details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EC2 instances** in the navigation pane.

1. Choose the finding classification listed next to the instance that you want to view detailed information for.

   The details page lists up to three optimization recommendations for the instance that you chose. The page lists the specifications of your current instance, the specifications and performance risks of the recommended instances, and utilization metric graphs.

1. You can perform the following actions on the details page:
   + To view the price and performance impact of running your workload on AWS Graviton-based instances, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current instance.
   + Activate the enhanced infrastructure metrics paid feature to extend the metrics analysis look-back period for the EC2 instance you're viewing up to three months (compared to the 14-day default). For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).
   + Choose a recommendation option to view the utilization comparison between your current instance and a recommended instance.

     The utilization metric graphs for your current instance are displayed at the bottom of the page. The solid blue line is the utilization of your current instance. The dotted orange line is the projected utilization of the selected recommended instance if you use that instance during the analyzed period. The dotted orange line is displayed in the CPU utilization and memory utilization graphs.
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**. If you activate the [enhanced infrastructure metrics recommendation preference](#enhanced-infrastructure-metrics), you can also choose **Last 3 months**.

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.
   + To change the statistic value of the graphs, choose **Statistics**, and then choose **Average** or **Maximum**.

     You can use this option to determine the typical instance utilization of your workload over time. To view the highest value observed during the specified period, change the selection to **Maximum**. This way, you can determine the peak instance usage of your workload over time.

## Viewing EC2 Auto Scaling group recommendations
<a name="view-asg-recommendations"></a>

AWS Compute Optimizer generates instance type recommendations for Amazon EC2 Auto Scaling groups. Recommendations for your EC2 Auto Scaling groups are displayed on the following pages of the AWS Compute Optimizer console.
+ **EC2 Auto Scaling group recommendations**

  This page lists each of your current EC2 Auto Scaling groups, their finding classifications, current instance type(s), current hourly price for the selected purchasing option, and current configuration. The top recommendation from Compute Optimizer is listed next to each of your EC2 Auto Scaling groups, and it includes the recommended instance type, the hourly price for the selected purchasing option, and the price difference between your current instance type(s) and the recommendation. Use the recommendations page to compare the current instance type(s) of your EC2 Auto Scaling groups with our top recommendation, which can help you to decide if you should upsize or downsize your instances.
+ **EC2 Auto Scaling group details**

  Depending on the specific EC2 Auto Scaling group, this page provides you with rightsizing recommendations and/or recommendations to scale in an idle group. It lists the specifications for each rightsizing recommendation such as the performance risk and hourly prices for the selected purchasing option. The details page also displays utilization metric graphs that can be used to compare the current EC2 Auto Scaling group with the projected utilization metrics for the recommendation option(s).

The recommendations are refreshed daily. They're generated by analyzing the specifications and utilization metrics of the current EC2 Auto Scaling group over the default lookback period of 14 days or a 32-day lookback period. You can extend the lookback period to 93 days if you enable enhanced infrastructure metrics. For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics), [Rightsizing recommendation preferences](#rightsizing-preferences), and [Metrics analyzed by AWS Compute Optimizer](#metrics).

Keep in mind that Compute Optimizer generates recommendations for EC2 Auto Scaling groups that meet a specific set of requirements, recommendations could take up to 24 hours to be generated, and sufficient metric data must be accumulated. For more information, see [Resource requirements](#requirements).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

**Topics**
+ [How an EC2 Auto Scaling group recommendation is generated](#asg-recommendations-generate)
+ [Finding classifications](#asg-recommendations-findings)
+ [Allocation strategy](#asg-recommendations-allocation)
+ [Estimated monthly savings and savings opportunity](#asg-savings-calculation)
+ [Idle](#asg-recommendations-idle)
+ [AWS Graviton-based instance recommendations](#asg-graviton-recommendations)
+ [Inferred workload types](#asg-inferred-workload-types)
+ [Migration effort](#asg-migration-effort)
+ [Performance risk](#asg-performance-risk)
+ [Utilization graphs](#asg-utilization-graphs)
+ [Accessing EC2 Auto Scaling group recommendations and details](#asg-view-recommendations)

### How an EC2 Auto Scaling group recommendation is generated
<a name="asg-recommendations-generate"></a>

AWS Compute Optimizer generates recommendations for EC2 Auto Scaling groups using a three-step evaluation process designed to optimize cost and performance:

1. **Assessing whether an EC2 Auto Scaling group is idle**

   Compute Optimizer assesses whether your EC2 Auto Scaling group is idle by analyzing its resource utilization patterns over the lookback period. If all instances in an EC2 Auto Scaling group meet the idle criteria, Compute Optimizer finds your group to be idle and estimates the potential savings of scaling in the idle group. For more information, see [Idle criteria per resource](#idle-criteria).

1. **Assessing the scalability of an EC2 Auto Scaling group**

   Compute Optimizer assesses the instance capacity settings and scaling policies to determine whether your EC2 Auto Scaling group is used to maintain a fixed pool of instances (with no scaling policies or disabled scaling policies), scale dynamically to meet your workload demands (using target tracking, predictive scaling, simple scaling, or step scaling policies based on CPU utilization), or follow a fixed schedule of scaling events (with scheduled scaling policies).

1. **Identifying rightsizing opportunities**

   Compute Optimizer analyzes the resource utilization and current configuration of your EC2 Auto Scaling group, including allocation strategy settings, scaling policies, instance types, pricing, and instance capacity to find suitable rightsizing opportunities.
   + For EC2 Auto Scaling groups maintaining a fixed pool of instances, Compute Optimizer recommends instance types that meet your workload requirements while maintaining the current instance count. This can improve your workload performance and provide cost savings.
   + For EC2 Auto Scaling groups that scale dynamically based on demand, Compute Optimizer recommends upgrading to newer instance generations that can provide increased savings. If memory metrics are enabled, it can also suggest memory downsizing opportunities for additional savings.
   + For EC2 Auto Scaling groups that follow a fixed schedule of scaling events, Compute Optimizer recommends instance types that can provide increased savings while meeting your resource workload requirements based on scheduled scaled capacity. This ensures that the recommendations align with the specific scaling strategies and workload demands of each group.

**Note**  
For rightsizing recommendations, Compute Optimizer doesn’t provide recommendations to modify scaling policy or instance capacity settings.

### Finding classifications
<a name="asg-recommendations-findings"></a>

The **Finding** column on the **EC2 Auto Scaling groups recommendations** page provides a summary of how each of your EC2 Auto Scaling groups performed during the lookback period.

The following findings classifications apply to EC2 Auto Scaling groups.


| Classification | Description | 
| --- | --- | 
| Not optimized | EC2 Auto Scaling groups that maintain a fixed pool of instances are considered not optimized when the group is either oversized or running workloads that might cause performance issues. <br />EC2 Auto Scaling groups that scale dynamically or follow a fixed schedule of scaling events are considered not optimized when there are other instance types that can meet the demand at a lower cost.  | 
| Optimized | An EC2 Auto Scaling group is considered optimized when all specifications of your group, such as CPU, memory, and network, meet the performance requirements of your workload. For optimized groups, Compute Optimizer might recommend a new generation instance type. | 

### Allocation strategy
<a name="asg-recommendations-allocation"></a>

The allocation strategy columns on the EC2 Auto Scaling groups recommendations and details pages displays the current and recommended allocation strategy for the EC2 Auto Scaling group. The allocation strategy sets the order in which the EC2 Auto Scaling group deploys its mixed instance types. Compute Optimizer can find an allocation strategy to be one of the following:
+ **Prioritized** — The EC2 Auto Scaling group prioritizes the instance types based on the order you have listed in your instance type requirements.
+ **Lowest-price** — The EC2 Auto Scaling group automatically deploys the lowest priced instance types in each Availability Zone based on the current On-Demand price.
+ **No allocation strategy** — You have not set an allocation strategy for your EC2 Auto Scaling group. 
+ **Not applicable** — An allocation strategy isn’t applicable to an EC2 Auto Scaling group with a single instance type.

Compute Optimizer recommends using a **Prioritized** allocation strategy and prioritize our recommended instance types above your current instance types within your instance type requirements. Prioritizing Compute Optimizer’s recommendation enables your EC2 Auto Scaling group to deploy instance types that optimize both cost and performance. We also recommended that you keep your current instance types within your instance type requirements to make sure there is sufficient capacity to support your workloads.

You can update your EC2 Auto Scaling groups with our recommended instance types by using an instance refresh. For more information, see [Use an instance refresh to update instances in an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in the *Amazon EC2 Auto Scaling* user guide.

For more information about allocation strategies, see [Allocation strategies for multiple instance types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html#on-demand-allocation-strategy) in the *Amazon EC2 Auto Scaling* user guide.

### Estimated monthly savings and savings opportunity
<a name="asg-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the estimated monthly savings for the EC2 Auto Scaling group if you had used the recommended instance type(s) during the lookback period. After discount savings consider any Reserved Instances or Savings Plans pricing models that are active in your accounts. To receive recommendations with Savings Plans and Reserved Instances discounts, the savings estimation mode preference needs to be activated. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings for the EC2 Auto Scaling group if you had used Compute Optimizer’s recommendation during the lookback period, and purchased under the On-Demand instance pricing.

**Savings opportunity (%)**

This column lists the estimated monthly savings percentage of the current monthly cost that you can save by adopting the recommended instance type(s) for your EC2 Auto Scaling group. If savings estimation mode is activated, Compute Optimizer analyzes any Reserved Instances or Savings Plans pricing models that are active in your accounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

#### Estimated monthly savings calculation
<a name="asg-estimated-monthly-savings-calculation"></a>

For each recommendation, we calculate the cost to operate a new instance using the recommended instance type. Estimated monthly savings are calculated based on the number of running hours for current instances in the EC2 Auto Scaling group and the difference in rates between the current instance type and the recommended instance type. The estimated monthly savings for EC2 Auto Scaling groups displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all over-provisioned instances in EC2 Auto Scaling groups, in the account.

### Idle
<a name="asg-recommendations-idle"></a>

The **Idle** column on the **EC2 Auto Scaling groups recommendations** page displays whether your EC2 Auto Scaling group is idle or not.

**Idle criteria for EC2 Auto Scaling groups** — The group has no instances with more than 5% peak CPU utilization or 5 MB/day network utilization over the 14-day lookback period.

**Idle criteria for EC2 Auto Scaling groups that use G or P instance types** — If the group's instances meet the following criteria over the 14-day lookback period:
+ GPU isn’t actively working for more than 99% of the lookback period
+ GPU encoder isn't used for 99% or more of the instance's runtime
+ GPU memory usage at instance level is less than 5% 
+ CPU maximum utilization is less than 5%
+ Network utilization is less than 5 MB/day

### AWS Graviton-based instance recommendations
<a name="asg-graviton-recommendations"></a>

When viewing EC2 Auto Scaling group recommendations, you can view the price and performance impact of running your workload on AWS Graviton-based instances. To do so, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, choose **Current** to view recommendations that are based on the same CPU vendor and architecture as the current instance.

**Note**  
The **Current price**, **Recommended price**, **Price difference**, **Price difference (%)**, and **Estimated monthly savings** columns are updated to provide a price comparison between the current instance type and the instance type of the selected CPU architecture preference. For example, if you choose **Graviton (aws-arm64)**, prices are compared between the current instance type and the recommended Graviton-based instance type.

### Inferred workload types
<a name="asg-inferred-workload-types"></a>

 The **Inferred workload types** column on the **EC2 Auto Scaling groups recommendations** page lists the applications that might be running on instances in the EC2 Auto Scaling group as inferred by Compute Optimizer. It does this by analyzing the attributes of instances in the EC2 Auto Scaling group, such as the instance name, tags, and configuration. Compute Optimizer can currently infer if your instances are running Amazon EMR, Apache Cassandra, Apache Hadoop, Memcached, NGINX, PostgreSQL, Redis, Kafka, or SQLServer. By inferring the applications running on your instances, Compute Optimizer is able to identify the effort to migrate your workloads from x86-based instance types to Arm-based AWS Graviton instances types. For more information, see [Migration effort](#asg-migration-effort).

**Note**  
You can't infer the SQLServer application in the Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hong Kong), Europe (Milan), and Asia Pacific (Jakarta) Regions.

### Migration effort
<a name="asg-migration-effort"></a>

The **Migration effort** column on the **EC2 Auto Scaling groups recommendations** and **EC2 Auto Scaling groups details** pages lists the level of effort that might be required to migrate from the current instance type to the recommended instance type. The following shows examples of the different levels of migration effort.
+ **Very low** — The recommended instance type has the same CPU architecture as the current instance type.
+ **Low** — Amazon EMR is the inferred workload type and an AWS Graviton instance type is recommended
+ **Medium** — A workload type can't be inferred but an AWS Graviton instance type is recommended.
+ **High** — The recommended instance type has different CPU architecture from the current instance type, and the workload has no known compatible version on the recommended CPU architecture.

For more information about migrating from x86-based instance types to Arm-based AWS Graviton instances type, see [Considerations when transitioning workloads to AWS Graviton2 based Amazon EC2 instances ](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md) in the *AWS Graviton Getting Started GitHub*.

### Performance risk
<a name="asg-performance-risk"></a>

The performance risk columns on the **EC2 Auto Scaling groups details** page and the **EC2 Auto Scaling groups recommendations** page define the likelihood of the current and recommended instance type(s) running in your EC2 Auto Scaling group not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the EC2 Auto Scaling group, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the current and recommended EC2 Auto Scaling group is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A very low performance risk means that the instance type(s) is predicted to always provide enough capability. A higher the performance risk means that you should validate whether the instance type(s) running in your EC2 Auto Scaling group will meet the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. For more information, see [Changing the Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Note**  
In the Compute Optimizer API, the AWS Command Line Interface (AWS CLI), and AWS SDKs, performance risk is measured on a scale of `0` (very low) to `4` (very high).

### Utilization graphs
<a name="asg-utilization-graphs"></a>

The **EC2 Auto Scaling group details** page displays utilization metric graphs for current instances in the group. The graphs display data for the analysis period. Compute Optimizer uses the maximum utilization point within each five-minute time interval to generate EC2 Auto Scaling group recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks. If you activate the [enhanced infrastructure metrics paid feature](#enhanced-infrastructure-metrics), you can view data from the last three months.

The following utilization graphs are displayed on the details page:


| Graph name | Description | 
| --- | --- | 
| Average CPU utilization (percent) | The average percentage of allocated EC2 compute units used by instances in the EC2 Auto Scaling group. | 
| Average network in (MiB/second) | The number of mebibytes (MiB) per second received on all network interfaces by instances in the EC2 Auto Scaling group. | 
| Average network out (MiB/second) | The number of mebibytes (MiB) per second sent out on all network interfaces by instances in the EC2 Auto Scaling group. | 
| Instance capacity |  This is the number of running instances with an EC2 Auto Scaling group at any given time. | 

### Accessing EC2 Auto Scaling group recommendations and details
<a name="asg-view-recommendations"></a>

You can use one of the following procedures to access either the **EC2 Auto Scaling groups recommendations** or the **EC2 Auto Scaling group details** pages in the AWS Console.

On the **EC2 Auto Scaling groups recommendations** page you can view the recommendations for your current EC2 Auto Scaling groups. On the **EC2 Auto Scaling group details** page you can view the details of a specific group and its recommendations.

#### Procedures
<a name="asg-view-process"></a>

##### Accessing EC2 Auto Scaling group recommendations page
<a name="asg-view-recommendations"></a>

**To access the EC2 Auto Scaling group recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EC2 Auto Scaling groups** in the navigation pane.

   The recommendations page lists the specifications and finding classifications of your EC2 Auto Scaling groups, along with the specifications of the recommended groups. The current EC2 Auto Scaling groups listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations page:
   + View the price and performance impact of running your workload on AWS Graviton-based instances. To do this, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown list. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current instance.
   + Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the dropdown list that appears.
   + View recommendations for instances in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.
   + Access the **EC2 Auto Scaling group details** page for a specific EC2 Auto Scaling group. To do this, choose the finding classification listed next to the desired group.

##### Accessing EC2 Auto Scaling group details page
<a name="asg-viewing-details"></a>

**To access the EC2 Auto Scaling group details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EC2 Auto Scaling groups** in the navigation pane.

1. To view the details of a recommendation, select an EC2 Auto Scaling group and choose **View details**. Or, choose the EC2 Auto Scaling group link.

   The details page lists up to three optimization recommendations for the EC2 Auto Scaling group that you chose. It lists the specifications of current instances in the EC2 Auto Scaling group, the specifications and performance risks of the recommended instances, and utilization metric graphs.

1. You can perform the following actions on the details page:
   + To view the price and performance impact of running your workload on AWS Graviton-based instances, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current instance.
   + Activate the enhanced infrastructure metrics paid feature to extend the metrics analysis look-back period for the Auto Scaling group you're viewing up to three months (compared to the 14-day default). For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).
   + The utilization metric graphs for your current instance are displayed at the bottom of the page. The solid blue line is the utilization of current instances in the Auto Scaling group.
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**. If you activate the [enhanced infrastructure metrics recommendation preference](#enhanced-infrastructure-metrics), you can also choose **Last 3 months**. Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.

## Viewing Amazon EBS volume recommendations
<a name="view-ebs-recommendations"></a>

AWS Compute Optimizer generates volume type, volume size, IOPS, and throughput recommendations for Amazon Elastic Block Store (Amazon EBS) volumes. Recommendations for your EBS volumes are displayed in the following pages of the AWS Compute Optimizer console:
+ The **EBS volumes recommendations** page lists each of your current volumes, their [finding classifications](#ebs-recommendations-findings), their current volume type, and their current hourly price. The top recommendation from Compute Optimizer is listed next to each of your volumes, and it includes the recommended volume type, recommended volume size, recommended IOPS, the monthly price of the recommendation, and the price difference between your current volume and the recommendation. Use the recommendations page to compare your current volumes with their top recommendation, which can help you to decide if you should up-size or down-size your volume.
+ The **EBS volume details** page, which you can access from the EBS volume recommendations page, lists up to three optimization recommendations for a specific volume. It lists the specifications for each recommendation, their [performance risk](#ebs-performance-risk), and their monthly prices. The details page also displays utilization metric graphs for the current volume.

The recommendations are refreshed daily. They're generated by analyzing the specifications and utilization metrics of the current volume over a period of the last 14 days. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

Keep in mind that Compute Optimizer generates recommendations for EBS volumes that meet a specific set of requirements, recommendations could take up to 24 hours to be generated, and sufficient metric data must be accumulated. For more information, see [Resource requirements](#requirements).

**Topics**
+ [Finding classifications](#ebs-recommendations-findings)
+ [Estimated monthly savings and savings opportunity](#ebs-savings-calculation)
+ [Performance risk](#ebs-performance-risk)
+ [Utilization graphs](#ebs-utilization-graphs)
+ [Accessing EBS volumes recommendations and details](#ebs-view-recommendations)

### Finding classifications
<a name="ebs-recommendations-findings"></a>

The **Finding** column on the **EBS volumes recommendations** page provides a summary of how each of your volumes performed during the analyzed period.

The following findings classifications apply to EBS volumes.


| Classification | Description | 
| --- | --- | 
| Not optimized | An EBS volume is considered not optimized when Compute Optimizer has identified a volume type, volume size, or IOPS specification that can provide better performance or cost for your workload. | 
| Optimized | An EBS volume is considered optimized when Compute Optimizer determines that the volume is correctly provisioned to run your workload, based on the chosen volume type, volume size, and IOPS specification. For optimized resources, Compute Optimizer might sometimes recommend a new generation volume type. | 

### Estimated monthly savings and savings opportunity
<a name="ebs-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience by migrating your EBS volumes from the current specifications to the recommended specifications under specific discounts. To receive recommendations with specific discounts, the savings estimation mode preference needs to be activated. For more information, see [ Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you will experience by migrating your EBS volumes from the current specifications to the recommended specifications. 

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current EBS volume specification and the price of the recommended volume specification. If savings estimation mode is activated, Compute Optimizer analyzes specific discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

#### Estimated monthly savings calculation
<a name="ebs-estimated-monthly-savings-calculation"></a>

For each recommendation, we calculate the cost to operate a new EBS volume using the recommended volume specifications. Estimated monthly savings are calculated based on the number of running hours for the current volume and the difference in rates between the current volume specifications and the recommended volume specifications. The estimated monthly savings for EBS volumes displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all EBS volumes in the account with a finding classification of *Not optimized*.

### Performance risk
<a name="ebs-performance-risk"></a>

The performance risk columns on the **EBS volume details** page the **EBS volume recommendations** page define the likelihood of the current and recommended EBS volume not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the EBS volume, including volume type, volume size, baseline IOPS, burst IOPS, baseline throughput, and burst throughput. The performance risk of the current and recommended EBS volume is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A performance risk of very low means that the EBS volume is predicted to always provide enough capability. The higher the performance risk means that you should validate whether the volume meets the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. For more information, see [Requesting modifications to your EBS Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Note**  
If Compute Optimizer doesn’t display a risk value for your current Amazon EBS volume, this means that the volume is predicted to provide enough performance capability and is considered to have a very low performance risk.

### Utilization graphs
<a name="ebs-utilization-graphs"></a>

The **EBS volume details** page displays utilization metric graphs for your current volume. The graphs display data for the analysis period. Compute Optimizer uses the maximum utilization point within each five-minute time interval to generate EBS volume recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks. You can also change the statistic of the graphs between average and maximum.

The following utilization graphs are displayed on the details page:


| Graph name | Description | 
| --- | --- | 
| Read operations (per second) | The completed read operations per second for the current EBS volume.<br />For Xen instances, data is reported only when there is read activity on the volume. | 
| Write operations (per second) | The completed write operations per second to the current EBS volume.<br />For Xen instances, data is reported only when there is write activity on the volume. | 
| Read bandwidth (KiB/second) | The read kibibytes (KiB) per second from the current EBS volume. | 
| Write bandwidth (KiB/second) | The written kibibytes (KiB) per second to the current EBS volume. | 
| Burst balance (percent) | The percentage of I/O credits remaining in the burst bucket for the current EBS volume.<br />This metric is displayed only for General Purpose SSD (`gp2`) volumes in the Compute Optimizer console. | 
| IOPS exceeded check | Reports whether an application consistently attempted to drive IOPS that exceeds the volume's provisioned IOPS performance within the last minute. This metric can be either 0 (provisioned IOPS not exceeded) or 1 (provisioned IOPS exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 
| Throughput exceeded check | Reports whether an application consistently attempted to drive throughput that exceeds the volume's provisioned throughput performance within the last minute. This metric can be either 0 (provisioned throughput not exceeded) or 1 (provisioned throughput exceeded). Supported for all volume types, except magnetic (standard), attached to Nitro instances. Not supported with Multi-Attach enabled volumes. Not published for volumes attached to Amazon ECS and Fargate tasks.  | 

### Accessing EBS volumes recommendations and details
<a name="ebs-view-recommendations"></a>

You can use one of the following procedures to access either the **EBS volumes recommendations** or the **EBS volume details** pages in the AWS Console.

On the **EBS volumes recommendations** page you can view the recommendations for your current EBS volumes. On the **EBS volume details** page you can view the details of a specific volume and its recommendations.

#### Procedures
<a name="ebs-view-process"></a>

##### Accessing EBS volumes recommendations page
<a name="ebs-view-recommendations-process"></a>

**To access the EBS volume recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EBS volumes** in the navigation pane.

   The recommendations page lists the specifications and finding classifications of your volumes, along with the specifications of the recommended volumes. The current volumes listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations page:
   + Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the drop-down list that appears.
   + Filter your recommendations by tags. To do this, select the **Tag key** or **Tag value** text box. Then, enter the key or value you want to filter your EBS volume recommendations by.

     For example, to find all recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View recommendations for volumes in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.
   + Access the **EBS volume details** page for a specific volume. To do this, choose the finding classification listed next to the desired volume.

   When you're ready, use Amazon EBS Elastic Volumes to modify the configuration of your volumes. For more information, see [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html) in the *Amazon Elastic Compute Cloud User Guide*.

##### Accessing EBS volume details page
<a name="ebs-viewing-details"></a>

**To access the EBS volume details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EBS volumes** in the navigation pane.

1. Choose the finding classification listed next to the volume for which you wish to view detailed information.

   The details page lists up to three optimization recommendations for the volume that you chose. It lists the specifications of your current volume, the specifications and performance risks of the recommended volumes, and utilization metric graphs.

1. You can perform the following actions on the details page:
   + Choose a recommendation option to view the utilization comparison between your current volume and a recommended volume.

     The utilization metric graphs for your current volume are displayed at the bottom of the page.
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**.

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.
   + To change the statistic value of the graphs, choose **Statistics**, and then choose **Average** or **Maximum**.

     You can use this option to determine the typical volume utilization of your workload over time. To view the highest value observed during the specified period, change the selection to **Maximum**. This allows you to determine the peak volume usage of your workload over time.

   When you're ready, use Amazon EBS Elastic Volumes to modify the configuration of your volumes. For more information, see [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Viewing Lambda function recommendations
<a name="view-lambda-recommendations"></a>

AWS Compute Optimizer generates memory size recommendations for AWS Lambda functions. Recommendations for your functions are displayed in the following pages of the Compute Optimizer console:
+ The **Lambda functions recommendations** page lists each of your current functions, their [finding classifications](#lambda-recommendations-findings), finding reasons, current configured memory, current usage, and current cost. The top recommendation from Compute Optimizer is listed next to each of your functions, and it includes the recommended configured memory, recommended cost, and the price difference between your current function and the recommendation. Note that the recommended cost is a range that is displayed under the **Recommended cost (high)** and **Recommended cost (low)** columns in the console. Use the recommendations page to compare your current functions with their top recommendation, which can help you to decide if you should up-size or down-size the configured memory of your function.
+ The **Lambda function details** page, which you can access from the Lambda function recommendations page, lists the top optimization recommendation for a function. It lists the configuration for your current function and the recommendation option. The details page also displays utilization metric graphs for the current function.

The recommendations are refreshed daily. They're generated by analyzing the specifications and utilization metrics of the current function over a period of the last 14 days. For more information, see [Metrics analyzed by AWS Compute Optimizer](#metrics).

Keep in mind that Compute Optimizer generates recommendations for Lambda functions that meet a specific set of requirements, recommendations could take up to 24 hours to be generated, and sufficient metric data must be accumulated. For more information, see [Resource requirements](#requirements).

**Topics**
+ [Finding classifications](#lambda-recommendations-findings)
+ [Estimated monthly savings and savings opportunity](#lambda-savings-calculation)
+ [Current performance risk](#lambda-current-performance-risk)
+ [Utilization graphs](#lambda-utilization-graphs)
+ [Accessing Lambda function recommendations and details](#lambda-view-recommendations)

### Finding classifications
<a name="lambda-recommendations-findings"></a>

The **Finding** column on the **Lambda functions recommendations** page provides a summary of how each of your functions performed during the analyzed period.

The following findings classifications apply to Lambda functions.


| Classification | Description | 
| --- | --- | 
| Not optimized | A Lambda function is considered not optimized when Compute Optimizer has identified that its configured memory or CPU power (which is proportional to the configured memory) is under-provisioned or over-provisioned. In this case, Compute Optimizer generates a recommendation that can provide better performance or cost for your workload.<br />When a function is not optimized, Compute Optimizer displays a finding reason of either **Memory under-provisioned** or **Memory over-provisioned**. | 
| Optimized | A Lambda function is considered optimized when Compute Optimizer determines that its configured memory or CPU power (which is proportional to the configured memory) is correctly provisioned to run your workload. | 
| Unavailable | Compute Optimizer was unable to generate a recommendation for the function. This could be because the function has not met the [requirements of Compute Optimizer for Lambda functions](#requirements-lambda-functions), or the function does not qualify for a recommendation.<br />For this finding classification, Compute Optimizer displays one of the following finding reasons:+  **Insufficient data** when the function does not have sufficient metric data for Compute Optimizer to generate a recommendation. <br />+  **Inconclusive** when the function does not qualify for a recommendation because the function has configured memory greater than 1,792 MB, or Compute Optimizer cannot generate a recommendation with a high degree of confidence.  Functions with a finding of **Unavailable** are not listed in the Compute Optimizer console.  | 

### Estimated monthly savings and savings opportunity
<a name="lambda-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current Lambda function memory specification to the recommended memory specification under the Savings Plans pricing model. To receive recommendations with Savings Plans discounts, the savings estimation mode preference needs to be activated. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current Lambda function memory specification to the recommended memory specification under the On-Demand pricing model. 

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current Lambda function memory specification and the price of the recommended specification. If savings estimation mode is activated, Compute Optimizer analyzes the Savings Plans pricing discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

#### Estimated monthly savings calculation
<a name="lambda-estimated-monthly-savings-calculation"></a>

For each recommendation, we calculate the cost to operate a new Lambda function using the recommended memory specification. Estimated monthly savings are calculated based on the number of running hours for the current Lambda function and the difference in rates between the current memory specification and the recommended memory specification. The estimated monthly savings for Lambda functions displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all Lambda functions in the account with a finding classification of *Not optimized*.

### Current performance risk
<a name="lambda-current-performance-risk"></a>

The **Current performance risk** column on the **Lambda functions recommendations** page defines the likelihood of each current Lambda function not meeting the resource needs of its workload. The current performance risk values range from very low, low, medium, and high. A very low performance risk means that the current Lambda function is predicted to always provide enough capability. The higher the performance risk is, the more likely you should consider the recommendation generated by Compute Optimizer.

### Utilization graphs
<a name="lambda-utilization-graphs"></a>

The **Lambda function details** page displays utilization metric graphs for your current function. The graphs display data for the analysis period. Compute Optimizer uses the maximum utilization point within each five-minute time interval to generate Lambda function recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks.

The following utilization graphs are displayed on the details page:


| Graph name | Description | 
| --- | --- | 
| Duration (milliseconds) | The amount of time that your function code spends processing an event. | 
| Errors (count) | The number of invocations that result in a function error. Function errors include exceptions thrown by your code and exceptions thrown by the Lambda runtime. The runtime returns errors for issues such as timeouts and configuration errors. | 
| Invocations (count) | The number of times your function code is executed, including successful executions and executions that result in a function error. | 

### Accessing Lambda function recommendations and details
<a name="lambda-view-recommendations"></a>

You can use one of the following procedures to access either the **Lambda function recommendations** or the **Lambda function details** pages in the AWS Console.

On the **Lambda function recommendations** page you can view the recommendations for your current functions. On the **Lambda function details** page you can view the details of a specific function and its recommendations.

#### Procedures
<a name="lambda-view-process"></a>

##### Accessing Lambda function recommendations page
<a name="lambda-view-recommendations-process"></a>

**To access the Lambda function recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Lambda functions** in the navigation pane.

   The recommendations page lists the specifications and finding classifications of your functions, along with the specifications of the recommended functions. The current functions listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations page:
   + Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the dropdown list that appears.
   + Filter your recommendations by tags. To do this, select the **Tag key** or **Tag value** text box. Then, enter the key or value you want to filter your Lambda function recommendations by.

     For example, to find all recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View recommendations for functions in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.
   + Access the **Lambda function details** page for a specific function. To do this, choose the finding classification listed next to the function that you want to access.

   Modify the configured memory of your Lambda function when you're ready. For more information, see [Configuring Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html) in the *AWS Lambda Developer Guide*.

##### Accessing Lambda function details page
<a name="lambda-viewing-details"></a>

**To access the Lambda function details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Lambda functions** in the navigation pane.

1. Choose the finding classification listed next to the function for which you wish to view detailed information.

   The details page lists the top optimization recommendation for the function that you chose. It lists the specifications of your current function, the recommended function configuration, and utilization metric graphs.

1. You can perform the following actions on the details page:
   + Choose a recommendation option to view the utilization comparison between your current function and a recommended function.

     The utilization metric graphs for your current function are displayed at the bottom of the page.
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**.

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.

   Modify the configured memory of your Lambda function when you're ready. For more information, see [Configuring Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html) in the *AWS Lambda Developer Guide*.

## Viewing Amazon ECS services on Fargate recommendations
<a name="view-ecs-recommendations"></a>

AWS Compute Optimizer generates recommendations for Amazon ECS services on Fargate. These recommendations are displayed on the following pages of the Compute Optimizer console.

The **Recommendations for Amazon ECS services on Fargate** page lists the following information for each of your ECS services:
+ Finding classifications
+ Finding reasons
+ Estimated monthly savings
+ Savings opportunity
+ Current performance risk

The recommendations from Compute Optimizer are listed next to each of your Amazon ECS services. The information that's provided includes the recommended CPU and memory size within an Amazon ECS service, the hourly price for the selected purchasing option, and the price difference between your current Amazon ECS service and the service with Compute Optimizer's recommended configurations. This information can help you decide if you up-size or down-size your Amazon ECS services on Fargate. For more information about how to view your recommendations for Amazon ECS services on Fargate, see [Accessing ECS service recommendations and details](#ecs-view-recommendations).

**Note**  
The recommendations are refreshed daily and they can take up to 24 hours to generate. Keep in mind that Compute Optimizer requires 24 hours of metrics in the past 14 days to generate recommendations for Amazon ECS service on Fargate. For more information, see [Requirements for Amazon ECS services on Fargate](#requirements-ecs-fargate).

The **Amazon ECS service details** page provides the following information for your Amazon ECS service:
+ Your current Amazon ECS service task size settings and Compute Optimizer's recommended task size settings. Use the table to compare your current task settings, such as CPU size, memory size, and pricing details, with Compute Optimizer recommendations.
+ Your current container size settings and Compute Optimizer's recommended container size settings. Use the table to compare your current container settings, such as CPU size, memory size, and memory reserved, with Compute Optimizer recommendations.
+ Use the utilization graphs to compare your current Amazon ECS service CPU and memory utilization metrics with Compute Optimizer’s recommendation. The graphs show visually the impact of these recommendations.

For more information about how to view the details for your Amazon ECS service on Fargate, see [Accessing ECS service details page](#ecs-viewing-details).

**Topics**
+ [Finding classifications](#ecs-recommendations-findings)
+ [Finding reasons](#ecs-finding-reasons)
+ [Estimated monthly savings and savings opportunity](#ecs-savings-calculation)
+ [Current performance risk](#ecs-current-performance-risk)
+ [Compare current settings with recommended task size](#ecs-task-table)
+ [Compare current settings with recommended container size](#ecs-container-table)
+ [Utilization graphs](#ecs-utilization-graphs)
+ [Accessing ECS service recommendations and details](#ecs-view-recommendations)

### Finding classifications
<a name="ecs-recommendations-findings"></a>

The **Findings** column on the **Recommendations for Amazon ECS services on Fargate** page provides a summary of how each of your services performed during the analysis period.

The following findings classifications apply to Amazon ECS services on Fargate.


| Classification | Description | 
| --- | --- | 
| Under-provisioned | When Compute Optimizer detects that there’s not enough memory or CPU, an Amazon ECS service is considered under-provisioned. Compute Optimizer displays a finding reason of **CPU under-provisioned** or **Memory under-provisioned**. An under-provisioned Amazon ECS service might result in poor application performance. | 
| Over-provisioned | When Compute Optimizer detects that there’s excessive memory or CPU, an Amazon ECS service is considered over-provisioned. Compute Optimizer displays a finding reason of **CPU over-provisioned** or ** Memory over-provisioned**. An over-provisioned Amazon ECS service might result in additional infrastructure costs. | 
| Optimized | When both the CPU and memory of your Amazon ECS service meet the performance requirements of your workload, the service is considered optimized. | 

For more information about under-provisioned and over-provisioned Amazon ECS services on Fargate, see [Finding reasons](#ecs-finding-reasons) in the [Viewing Amazon ECS services on Fargate recommendations](#view-ecs-recommendations) topic.

### Finding reasons
<a name="ecs-finding-reasons"></a>

The **Finding reasons** column on the **Recommendations for Amazon ECS services on Fargate** page shows which specification of an Amazon ECS service on Fargate is under-provisioned or over-provisioned.

The following finding reasons apply to Amazon ECS services on Fargate.


| Finding reason | Description | 
| --- | --- | 
| CPU over-provisioned | The ECS service CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period. | 
| CPU under-provisioned | The ECS service CPU configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period. | 
| Memory over-provisioned | The ECS service memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period. | 
| Memory under-provisioned | The ECS service memory configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period. | 

For more information about these metrics, see [Amazon ECS CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/userguide/cloudwatch-metrics.html) in the *Amazon ECS User Guide for AWS Fargate*.

### Estimated monthly savings and savings opportunity
<a name="ecs-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience after you adjust the configurations of your Amazon ECS service on Fargate to the recommended configurations under the Savings Plans pricing model. To receive recommendations with Savings Plans discounts, the savings estimation mode preference needs to be activated. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column displays the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you experience after you adjust the configurations of your Amazon ECS service on Fargate to the recommended configurations under the On-Demand pricing model. 

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current ECS service on Fargate and the price of the service with the recommended configurations. If savings estimation mode is activated, Compute Optimizer analyzes the Savings Plans pricing discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

#### Estimated monthly savings calculation
<a name="ecs-estimated-monthly-savings-calculation"></a>

For each recommendation, Compute Optimizer calculates the cost to operate a new Amazon ECS service on Fargate by using the recommended service specifications. Estimated monthly savings are calculated based on the estimated monthly running time of the current Amazon ECS service. The savings are also based on the difference in rates between the current Amazon ECS service and the service with the recommended configurations.

**Note**  
 To calculate the estimated monthly running time of your Amazon ECS services on Fargate, Compute Optimizer analyzes your utilization data over the past 14 days. Then, Compute Optimizer uses the analysis results to estimate your monthly usage. 

The estimated monthly savings for Amazon ECS services that are displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all over-provisioned services in the account.

### Current performance risk
<a name="ecs-current-performance-risk"></a>

The **Current performance risk** column on the **Recommendations for Amazon ECS services on Fargate** page defines how likely each current Amazon ECS service doesn’t meet workload resource needs. The values for current performance risk are Very low, Low, Medium, and High. 

A very low performance risk means that the current Amazon ECS service is predicted to consistently provide enough capability. A high performance risk is likely due to high CPU or memory utilization. If your Amazon ECS service is always running at capacity, it increases the chances of your service suffering from higher latency or lower performance. Compute Optimizer’s recommendations provides you with enough capacity to run your workloads efficiently. 

### Compare current settings with recommended task size
<a name="ecs-task-table"></a>

On the **Amazon ECS service details** page, compare the current Amazon ECS service task size with Compute Optimizer's recommended task size for your resources. Savings and performance risk information for your Amazon ECS service is also provided in the table. The following table provides a description for each column section in the console.


| Column | Description | 
| --- | --- | 
| CPU size | The CPU size of the current Amazon ECS service tasks and Compute Optimizer's recommended CPU size configurations. | 
| Memory size | The memory size of the current Amazon ECS service tasks and Compute Optimizer's recommended memory size configurations. | 
| Pricing details | The On-Demand price of the current Amazon ECS service on Fargate and Compute Optimizer's recommended configurations. For more information, see [AWS Fargate Pricing](https://aws.amazon.com/../fargate/pricing/). | 
| Estimated monthly savings | The approximate monthly cost savings after you adjust the configurations of your Amazon ECS service to Compute Optimizer's recommended configurations. For more information, see [Estimated monthly savings and savings opportunity](#ecs-savings-calculation). | 
| Savings opportunity (%) | The percentage difference between the price of your current Amazon ECS service and the price of the service with Compute Optimizer's recommended configurations. For more information, see [Estimated monthly savings and savings opportunity](#ecs-savings-calculation). | 
| Price difference | The difference between the public pricing of the current Amazon ECS service on Fargate and the service with Compute Optimizer's recommended configurations. For more information, see [AWS Fargate Pricing](https://aws.amazon.com/../fargate/pricing/). | 
| Performance risk | This defines how likely your current Amazon ECS service and Compute Optimizer's recommendation doesn’t meet workload resource needs. The values for performance risk are Very low, Low, Medium, and High. For more information, see [Current performance risk](#ecs-current-performance-risk).  | 
| Auto Scaling configuration | The Auto Scaling configuration of your current Amazon ECS service and Compute Optimizer's recommended task size. If your service has a step scaling policy or a target tracking policy on both CPU and memory, Compute Optimizer can’t generate any Auto Scaling recommendations. <br />If a target tracking policy is on the service’s CPU only, Compute Optimizer only generates memory size recommendations. Or, if a target tracking policy is on the service’s memory only, Compute Optimizer only generates CPU size recommendations. <br />For more information about step scaling and target scaling policies, see [ Step scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) and [ Target tracking scaling policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) in the *Application Auto Scaling User Guide*. | 

### Compare current settings with recommended container size
<a name="ecs-container-table"></a>

On the **Amazon ECS service details** page, compare the current Amazon ECS service container size with the recommended container size options. The table provides your current and Compute Optimizer’s recommended CPU size, memory size, and memory reserved configurations. Compute Optimizer generates container-level recommendations that are compatible with the recommended task size. 

**Note**  
Compute Optimizer only provides container size setting recommendations for when container size settings need to adjust to fit within an Amazon ECS service task. For example, suppose that Compute Optimizer recommends downsizing a task size. Then, Compute Optimizer provides container-level setting recommendations to make sure that the task size and container size settings are compatible with each other. 

### Utilization graphs
<a name="ecs-utilization-graphs"></a>

The **Amazon ECS service details** page displays utilization metric graphs for your Amazon ECS services on Fargate and Compute Optimizer recommendations. The graphs display the current and recommended CPU and memory data for the analysis period. Compute Optimizer uses the maximum utilization point within each one-minute time interval to generate recommendations ECS services on Fargate.

The solid blue line is the utilization of your current service. If you used the recommendations during the analysis period, the green line is the projected upper bound value and the grey line is the projected lower bound value.

**Note**  
The utilization values of an Amazon ECS service can vary based on the infrastructure Fargate uses. Compute Optimizer provides a utilization range to help you consider all possible operating conditions.

You can change the graphs to display data for the last 24 hours, 3 days, 1 week, or 2 weeks. You can also change the statistic of the graphs between average and maximum.

The following utilization graphs are displayed on the details page.


| Graph name | Description | 
| --- | --- | 
| CPU utilization (percent) | The percentage of CPU capacity that's used in the service.<br />The graph compares the CPU utilization data of your current Amazon ECS service with the service when the recommended configurations are applied. The comparison shows you what the CPU utilization is if you configured your CPU to the recommended settings during the analysis period. This comparison shows if the recommended Amazon ECS service settings are within your workload's performance threshold. | 
| Memory utilization (percent) | The percentage of memory that's used in the service.<br />The graph compares the memory utilization data of your current Amazon ECS service with the service when the recommended configurations are applied. The comparison shows you what the memory utilization is if you configured your memory to the recommended settings during the analysis period. This comparison shows if the recommended Amazon ECS service settings are within your workload's performance threshold. | 

### Accessing ECS service recommendations and details
<a name="ecs-view-recommendations"></a>

You can use one of the following procedures to access either the **Recommendations for Amazon ECS services on Fargate** or the **Amazon ECS service details** pages in the AWS Console.

On the **Recommendations for Amazon ECS services on Fargate** page you can view the recommendations for your current services. On the **Amazon ECS service details** page you can view the details of a specific service and its recommendations.

#### Procedures
<a name="ecs-view-process"></a>

##### Accessing ECS service recommendations page
<a name="ecs-viewing-recommendations-process"></a>

**To access the ECS service recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **ECS services on Fargate**.
**Note**  
The current services listed are from the AWS Region that's currently selected in the selected account.

1. You can perform the following actions on the recommendations page:
   + Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the dropdown list that appears.
   + Filter your recommendations by tags. To do this, select the **Tag key** or **Tag value** text box. Then, enter the key or value you want to filter your ECS service recommendations by.

     For example, to find all recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View recommendations for services in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.

##### Accessing ECS service details page
<a name="ecs-viewing-details"></a>

**To access the ECS service details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **ECS services on Fargate**.

1. Select the service name you want to view detailed information for. Then, choose **View details**.

1. You can perform the following actions on the details page:
   + On the utilization graphs, you can hover over the graph to see exact values on specific dates over the analysis period. 
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**.

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.
   + To change the statistic value of the graphs, choose **Statistics**, and then choose **Average** or **Maximum**.

     You can use this option to determine the typical Amazon ECS service utilization of your workload over time. To view the highest value observed during the specified period, change the selection to **Maximum**. This way, you can determine the peak service usage of your workload over time.

## Viewing commercial software license recommendations
<a name="view-license-recommendations"></a>

AWS Compute Optimizer generates license recommendations for commercial software that run on Amazon EC2. These recommendations are displayed on the following pages of the Compute Optimizer console.

The **Recommendations for commercial software licenses** page lists the following information for each of your EC2 instances with licenses.
+ Finding classifications
+ Finding reasons
+ Estimated monthly savings
+ Savings opportunity
+ On-Demand prices
+ BYOL hourly license prices

The recommendations from Compute Optimizer are listed next to each of your EC2 instances with commercial software licenses. The information that's provided includes recommended saving opportunities, EC2 instance On-Demand prices, and hourly bring your own license (BYOL) prices. This information can help you decide if you should down-size your license edition. For more information about how to view your license recommendations for commercial software, see [Accessing commercial software license recommendations and details](#license-view-recommendations).

**Note**  
The recommendations are refreshed daily and they can take up to 24 hours to generate. Keep in mind that Compute Optimizer requires 24 hours of metrics in the past 14 days to generate license recommendations. For more information, see [Commercial software license requirements](#requirements-license).

The **License details** page provides the following information for your license recommendation:
+ Your current license settings and Compute Optimizer's recommended licence configurations. Use the table to compare your current license configurations, such as edition, model, and number of instance cores, with Compute Optimizer recommendations.
+ Use the utilization graphs to access the utilization of the current license during the analysis period.

For more information about how to view the details for your license recommendation, see [Accessing commercial software license details page](#license-viewing-details).

**Topics**
+ [Finding classifications](#license-recommendations-findings)
+ [Finding reasons](#license-finding-reasons)
+ [Estimated monthly savings and savings opportunity](#license-savings-calculation)
+ [Inferred workload types](#license-inferred-workload-types)
+ [Compare current license edition with recommended license edition](#compare-license-table)
+ [Utilization graphs](#license-utilization-graphs)
+ [Accessing commercial software license recommendations and details](#license-view-recommendations)

### Finding classifications
<a name="license-recommendations-findings"></a>

The **Findings** column on the **Commercial software license recommendations ** page provides a summary of how each of your licenses performed during the analyzed period.

The following findings classifications apply to Microsoft SQL Server licenses.


| Classification | Description | 
| --- | --- | 
| Insufficient metrics | When Compute Optimizer detects that your CloudWatch Application Insights isn't enabled or is enabled with insufficient permissions. Compute Optimizer displays a finding reason of `InvalidCloudwatchApplicationInsights` or `CloudwatchApplicationInsightsError`. | 
| Not optimized | When Compute Optimizer detects that your EC2 infrastructure isn't using any of the Microsoft SQL server license features you're paying for, a license is considered not optimized. Compute Optimizer displays a finding reason of `LicenseOverprovisioned`. A license that isn't optimized might result in unnecessary additional costs. | 
| Optimized | When the license for your SQL server database meets your performance requirements, the license is considered optimized. | 

For more information about these finding classifications, see [Finding reasons](#license-finding-reasons).

### Finding reasons
<a name="license-finding-reasons"></a>

The **Finding reasons** column on the **EC2 instances recommendations** and **EC2 instance details** pages shows which specification of an instance is under-provisioned or over-provisioned.

The following finding reasons apply to Microsoft SQL server license recommendations.


| Finding reason | Description | 
| --- | --- | 
| `LicenseOverprovisioned` | A license is considered over-provisioned when any of the current license features aren't in use. CloudWatch Application Insights analyzes the `mssql_enterprise_features_used` metric to identify this.<br />If your license is over-provisioned, you can consider downgrading your Microsoft SQL Server license. If you meet certain eligibility requirements you can downgrade from SQL Server Enterprise edition to SQL Server Standard edition, or Developer edition if it is a non-production workload. For more information, see [Downgrade your Microsoft SQL Server edition](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/downgrade-sql-server-on-ec2) in the *Microsoft SQL Server on Amazon EC2 User Guide*. | 
| `InvalidCloudwatchApplicationInsights` | The backend exporter of your CloudWatch Application Insights isn't configured properly. For more information about how to configure CloudWatch Application Insights, see [Set up Amazon CloudWatch Application Insights for monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-setting-up) in the *Amazon CloudWatch User Guide*. | 
| `CloudwatchApplicationInsightsError` | You have configured CloudWatch Application Insights but it hasn't identified the number of Enterprise edition features in use. It can take a few hours to identify the features. If the features aren't identified after a few hours, contact Support. | 

### Estimated monthly savings and savings opportunity
<a name="license-savings-calculation"></a>

The **Estimated monthly savings (On-Demand)** column lists the approximate monthly cost savings after you downgrade your license edition based on Compute Optimizer’s recommendations. To calculate this, Compute Optimizer multiplies the savings per hour by the estimated monthly running hours.

The **Savings opportunity (%)** column lists the percentage difference between your current Microsoft SQL server license and Compute Optimizer’s recommended license. The Bring Your Own License (BYOL) savings calculation is based on the license price. The License Included savings calculation is based on the On-Demand pricing.

**Important**  
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.

### Inferred workload types
<a name="license-inferred-workload-types"></a>

The **Inferred workload types** column on the **EC2 instances recommendations** page lists the applications that might be running on the instance as inferred by Compute Optimizer. This column does this by analyzing the attributes of your instances. These attributes include the instance name, tags, and configuration. Compute Optimizer can currently infer if your instances are running Amazon EMR, Apache Cassandra, Apache Hadoop, Memcached, NGINX, PostgreSQL, Redis, Kafka, or SQLServer. By inferring the applications that run on your instances, Compute Optimizer can identify the effort to migrate your workloads from x86-based instance types to Arm-based AWS Graviton instances types. For more information, see [Migration effort](#ec2-migration-effort) in the next section of this guide.

**Note**  
You can't infer the SQLServer application in the Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hong Kong), Europe (Milan), and Asia Pacific (Jakarta) Regions.

### Compare current license edition with recommended license edition
<a name="compare-license-table"></a>

On the **License details** page, compare the configurations of your current license edition with Compute Optimizer’s recommended license edition. The following table provides a description for each column section in the console.


| Column | Description | 
| --- | --- | 
| License edition | The current license edtion and the recommended license edition. For example, Enterprise, Standard, and Free. | 
| Instance On-Demand price | The current and recommended On-Demand instance prices. | 
| BYOL price (hourly) | The current and recommended Bring your own license (BYOL) hourly price.  | 
| Estimated monthly savings | The approximate monthly cost savings after you downgrade your license edition based on Compute Optimizer’s recommendations. For more information, see [Estimated monthly savings and savings opportunity](#license-savings-calculation). | 
| Savings opportunity (%) | The percentage difference between your current Microsoft SQL server license and Compute Optimizer’s recommended license. For more information, see [Estimated monthly savings and savings opportunity](#license-savings-calculation). | 
| Instance cores | The current and recommended number of physical cores for an instance. Number of instance cores are used in licensing calculations.  | 

### Utilization graphs
<a name="license-utilization-graphs"></a>

The **License details** page displays current resource utilization of the current commercial software license. The graph only displays the number of Enterprise editon features that were used data over the analysis period. 

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks.

### Accessing commercial software license recommendations and details
<a name="license-view-recommendations"></a>

You can use one of the following procedures to access either the **Recommendations for commercial software licenses** or the **License details** pages in the AWS Console.

On the **Recommendations for commercial software licenses** page you can view the recommendations for your current licenses. On the **License details** page you can view the details of a specific license recommendation.

#### Procedures
<a name="license-view-process"></a>

##### Accessing commercial software license recommendations page
<a name="license-view-recommendations-process"></a>

**To access the commercial software license recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Licenses** in the navigation pane.

1. (Optional) You can also access the license recommendations from the EC2 instances page. To do this, first select the Filter by one or more properties. From the dropdown list that appears, choose the **Inferred workload type** property and then choose the **Inferred workload type = SQL Server value**.
**Note**  
The current licenses listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations for commercial software licenses page:
   + Filter recommendations by AWS Regions, Findings, or Finding reasons. To do this, first select the **Filter by one or more properties** text box. Then, choose the property and a value in the dropdown list that appears.
   + Filter your recommendations by tags. To do this, select the **Tag key** or **Tag value** text box. Then, enter the key or value you want to filter your licesne recommendations by.

     For example, to find all recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View recommendations for functions in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.

##### Accessing commercial software license details page
<a name="license-viewing-details"></a>

**To access the commercial software license details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Licenses** in the navigation pane.

1. Choose the **Instance ID** you want to view detailed information.

1. You can perform the following actions on the details page:
   + On the utilization graphs, you can hover over the graph to see exact values on specific dates over the analysis period. 
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**.

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.
   + To change the statistic value of the graphs, choose **Statistics**, and then choose **Average** or **Maximum**.

## Viewing Aurora and RDS database recommendations
<a name="view-rds-recommendations"></a>

Compute Optimizer generates DB instances, RDS DB instance storage, and Aurora DB cluster storage recommendations for RDS for MySQL, RDS for PostgreSQL, Amazon Aurora databases. These recommendations are displayed on the **Recommendations for Aurora and RDS databases** and **Aurora and RDS databases details** pages of the Compute Optimizer console. Both of these pages are divided into two separate tabs: **Instance** and **Storage**.
+ **Recommendations for Aurora and RDS databases** page

  **Instance**

  This tab displays each of your current Aurora and RDS DB instances, finding classifications, finding reasons, current instance type, estimated savings, and saving opportunities. The top recommendation from Compute Optimizer is listed next to each of your instances. This recommendation includes the recommended instance type, On-Demand pricing, and the price difference between your current instance. Use the recommendations page to compare your current instances with the top recommendation. Doing this can help you to decide if you want to upsize or downsize your instances.

  **Storage**

  This tab displays each of your current RDS instance storage volumes and Aurora DB cluster storage configurations, finding classifications, current storage type, and current price. The top recommendation from Compute Optimizer is listed next to each of your volumes or clusters. For RDS DB instance storage, it includes the recommended volume type, recommended IOPS, the price of the recommendation, and the price difference between your current volume and the recommendation. For Aurora DB clusters, it includes the recommended storage type, estimated cluster costs (instance, storage, and I/O), and potential savings. You can use the recommendations page to compare your current storage configurations with their top recommendation, which can help you to decide if you should change your storage type.

  For more information about how to view your Aurora and RDS database recommendations, see [Accessing Aurora and RDS database recommendations and details](#rds-view-recommendations).
+ **Aurora and RDS database details** page

  **Instance**

  This tab displays optimization recommendations for a specific RDS DB instance or Aurora DB instance. It lists the specifications for each recommendation including performance risk, price difference, and On-Demand pricing. 

  **Storage**

  This tab displays the optimization recommendation for an RDS DB instance storage or Aurora DB cluster storage. For RDS DB instance storage, it lists the specifications for each recommendation including allocated storage, provisioned IOPS, throughput, and storage price difference. For Aurora DB clusters, it shows storage type recommendations with estimated costs broken down by instance, storage, and I/O components, along with I/O cost variability information when enhanced infrastructure metrics is enabled.

  Both detail pages display utilization metric graphs that you can use to compare the current instance or storage with the projected utilization metrics for the recommendation options. The graphs can help you to better understand the impact of these recommendations.

  For more information about how to view your Aurora and RDS database details, see [Accessing Aurora and RDS database details page](#rds-viewing-details).

The recommendations are refreshed daily and they can take up to 12 hours to generate. Keep in mind that Compute Optimizer requires at least 30 hours of Amazon CloudWatch metrics to generate recommendations for Amazon RDS DB instances. For more information, see [Resource requirements](#requirements).

**Topics**
+ [Finding classifications](#rds-recommendations-findings)
+ [Finding reasons](#rds-finding-reasons)
+ [AWS Graviton-based instance recommendations](#rds-graviton-recommendations)
+ [Estimated monthly savings and savings opportunity](#rds-savings-calculation)
+ [Performance risk](#rds-performance-risk)
+ [Comparison graphs](#rds-utilization-graphs)
+ [Accessing Aurora and RDS database recommendations and details](#rds-view-recommendations)

### Finding classifications
<a name="rds-recommendations-findings"></a>

The **Finding** column on the **Recommendations for Aurora and RDS databases** page provides a summary of how your Amazon Aurora and RDS DB instances, RDS DB instances storage, and Aurora DB clusters performed during the lookback period.

------
#### [ Aurora and RDS DB instances ]

The following findings classifications apply to DB instances.


| Classification | Description | 
| --- | --- | 
| Under-provisioned | When Compute Optimizer detects that there isn't enough CPU, memory, network bandwidth, EBS IOPS, or EBS throughput, an RDS DB instance is considered under-provisioned. Compute Optimizer displays finding reasons, such as **CPU under-provisioned**, **Memory under-provisioned**, **EBS IOPS under-provisioned**, and **Network bandwidth under-provisioned**. An under-provisioned RDS DB instance might result in poor application performance. | 
| Over-provisioned | When Compute Optimizer detects that there is excessive CPU, EBS IOPS, network bandwidth, or EBS throughput, an RDS DB instance is considered over-provisioned. Compute Optimizer displays finding reasons, such as **CPU over-provisioned**, **EBS IOPS over-provisioned**, **Network bandwidth over-provisioned**, and **EBS throughput over-provisioned**. An over-provisioned RDS DB instance might result in additional infrastructure costs. | 
| Optimized | When the specifications of your RDS DB instance meet the performance requirements of your workload, the RDS DB instance is considered optimized. For optimized instances, Compute Optimizer might recommend a new generation DB instance class or that a new engine version is available. | 

------
#### [ RDS DB instance storage ]

The following findings classifications apply to RDS DB storage.


| Classification | Description | 
| --- | --- | 
| Under-provisioned | When Compute Optimizer detects that there isn't enough allocated storage or EBS throughput, an RDS storage volume is considered under-provisioned. Compute Optimizer displays a finding reason of **EBS volume allocated storage under-provisioned** or **EBS volume throughput under-provisioned**. An under-provisioned RDS DB instance storage volume might result in poor application performance. | 
| Over-provisioned | When Compute Optimizer detects that there is excessive IOPS or EBS throughput, an RDS DB instance storage volume is considered over-provisioned. Compute Optimizer displays a finding reason of **EBS volume IOPS over-provisioned** or **EBS volume throughput over-provisioned**. An over-provisioned DB instance storage volume might result in additional infrastructure costs. | 
| Optimized | When the specifications of your RDS DB instance storage volume meet the performance requirements of your workload, the storage is considered optimized. For optimized DB instance storage, Compute Optimizer might recommend a new generation storage type. | 

For more information about under and over-provisioned RDS DB instances, see [Finding reasons](#rds-finding-reasons) in the [Viewing Aurora and RDS database recommendations](#view-rds-recommendations) topic.

------
#### [ Aurora DB clusters ]

The following findings classifications apply to Aurora DB clusters.


| Classification | Description | 
| --- | --- | 
| Optimized | Compute Optimizer found the configurations of your Aurora DB cluster storage to be optimized from a cost perspective. | 
| Not optimized | Compute Optimizer found potential cost savings if you switch your Aurora DB cluster from Aurora Standard storage to Aurora I/O-Optimized storage. Compute Optimizer displays a finding reason of **DBClusterStorageSavingsAvailable** when Aurora I/O-Optimized is identified as the top option. | 

For more information about Amazon Aurora DB clusters, see [Amazon Aurora storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html) in the *Amazon Aurora User Guide for Aurora*.

------

### Finding reasons
<a name="rds-finding-reasons"></a>

The **Finding reasons** column on the **Recommendations for RDS DB instances** and **RDS DB instance details** pages shows the specifications of Compute Optimizer findings for Amazon Aurora and RDS DB instances, RDS DB instances storage, and Aurora DB clusters.

------
#### [ Aurora and RDS DB instances ]

The following finding reasons apply to RDS DB instances:


| Finding reason | Description | 
| --- | --- | 
| CPU over-provisioned | The DB instance’s CPU configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current instance during the lookback period. | 
| CPU under-provisioned | The DB instance’s CPU configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance. This is identified by analyzing the `CPUUtilization` metric of the current instance during the lookback period. | 
| Memory under-provisioned | The DB instance’s memory configuration doesn't meet the performance requirements of your workload and there isn't an alternative instance type that provides better memory performance.<br />For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `os.swap.in` and `os.swap.out` metrics of the current instance if Amazon RDS Performance Insights is enabled. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*.<br />For Aurora DB instances, this is identified by analyzing the `os.memory.outOfMemoryKillCount` metric of the current instance if Amazon RDS Performance Insights is enabled. For Aurora MySQL DB instances, Compute Optimizer also analyzes Aurora memory health state metrics. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*. | 
| EBS throughput over-provisioned | The DB instance’s EBS throughput configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes attached to the current instance during the lookback period. | 
| EBS throughput under-provisioned | The DB instance’s EBS throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes that are attached to the current instance during the lookback period. | 
| EBS IOPS over-provisioned | The DB instance’s EBS IOPS configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS IOPS under-provisioned | The DB instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| Network bandwidth over-provisioned | The DB instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `NetworkIn` and `NetworkOut `metrics of the current instance during the lookback period. | 
| Network bandwidth under-provisioned | The DB instance’s network bandwidth configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance.<br />For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the lookback period. <br />For Aurora DB instances, this is identified by analyzing the `NetworkThroughput` and `StorageNetworkThroughput` metrics of the current instance during the lookback period. | 
| Instance storage read IOPS under-provisioned | The DB instance's instance storage read IOPS limit doesn't meet the performance requirement of your workload and there is an alternative instance type that provides better performance. For Aurora DB instances, this is identified by analyzing the `ReadIOPSEphemeralStorage` metric during the lookback period. | 
| Instance storage write IOPS under-provisioned | The DB instance's instance storage write IOPS limit doesn't meet the performance requirement of your workload and there is an alternative instance type that provides better performance. For Aurora DB instances, this is identified by analyzing the `WriteIOPSEphemeralStorage` metric during the lookback period. | 
| DB cluster writer under-provisioned | This indicates that Compute Optimizer has synchornized the recommendation for this Aurora DB instance read replica with the DB cluster's writer because it has a promotion tier < or = to 1. Compute Optimizer does this to help you maintain your failover capacity. | 
| New generation DB instance class available | If the current DB instance is a previous generation instance type, Compute Optimizer generates this finding reason to indicate that there is a new generation DB instance type available. We encourage you to use current generation instance types to get the best performance. | 
| New engine version available | If the current engine version is deprecated, Compute Optimizer generates this finding reason to indicate that there is a new engine version available.  | 

------
#### [ RDS DB instance storage ]

The following finding reasons apply to RDS DB instance storage.


| Finding reason | Description | 
| --- | --- | 
| EBS volume allocated storage under-provisioned | The amount EBS volume allocated storage space attached to the DB instance doesn't meet the performance requirements of your workload and there is an alternative volume type that provides better allocated storage performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS volume IOPS over-provisioned | The EBS volume IOPS configuration attached the DB instance can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS volume throughput under-provisioned | The size of the EBS volume throughput attached the DB instance doesn't meet the performance requirements of your workload and there is an alternative volume type that provides better volume throughput performance. | 
| EBS volume throughput over-provisioned | The EBS volume throughput attached the DB instance can be sized down and also meet the performance requirements of your workload.  | 
| New generation storage type available | If the current DB instance storage is a previous generation storage type, Compute Optimizer generates this finding reason to indicate that there is a new generation storage type available. We encourage you to use current generation storage types to get the best performance.  | 

------
#### [ Aurora DB clusters ]

The following finding reasons apply to Aurora DB clusters.


| Classification | Description | 
| --- | --- | 
| DBClusterStorageSavingsAvailable | Potential cost savings were found by switching your Aurora DB cluster from Aurora Standard storage to Aurora I/O-Optimized storage. Your cluster's I/O usage pattern suggests that the predictable pricing model of Aurora I/O-Optimized would be more cost-effective than the variable I/O costs of Aurora Standard. This finding reason appears when I/O Optimized is identified as the top recommended option for your cluster. | 
| DBClusterStorageOptionAvailable | Aurora I/O-Optimized was found to be a viable alternative storage option for your Aurora DB cluster. While your current storage configuration is considered optimized from a cost perspective, switching to Aurora I/O-Optimized could provide benefits such as more predictable monthly costs and simplified budgeting by eliminating variable I/O charges. This finding reason appears when I/O-Optimized is displayed as the second recommended option for your cluster. | 

------

### AWS Graviton-based instance recommendations
<a name="rds-graviton-recommendations"></a>

When viewing Amazon RDS DB instance recommendations, you can view the price and performance impact of running your workload on AWS Graviton-based instances. To do so, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, choose **Current** to view recommendations that are based on the same CPU vendor and architecture as the current RDS DB instance.

The **Current price**, **Recommended price**, **Price difference**, **Price difference (%)**, and **Estimated monthly savings** columns are updated to provide a price comparison between the current DB instance type and the instance type of the selected CPU architecture preference. For example, if you choose **Graviton (aws-arm64)**, prices are compared between the current DB instance type and the recommended Graviton-based instance type.

### Estimated monthly savings and savings opportunity
<a name="rds-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

**Instance tab**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current DB instance or type to the recommended type under the Reserved Instances pricing models. To receive recommendations with Reserved Instances discounts, activate the savings estimation mode preference.

**Storage tab**

This column lists the approximate monthly cost savings that you experience by migrating your RDS DB instance storage volumes from the current specifications to the recommended specifications under specific discounts. For Aurora DB clusters, this represents the savings from changing between Aurora Standard and Aurora I/O-Optimized storage types, considering all cost components (instance, storage, and I/O costs). To receive recommendations with specific discounts, activate the savings estimation mode preference.

For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column on both the Instance and Storage tabs display the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

**Instance tab**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current DB instance type to the recommended instance type under the On-Demand pricing model.

**Storage tab**

This column lists the approximate monthly cost savings that you experience by migrating your RDS DB instance storage volumes from the current specifications to the recommended specifications. For Aurora DB clusters, this includes the difference in total costs between your current storage type and the recommended storage type, considering instance, storage, and I/O cost components.

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current instance and the price of the recommended DB instance type. If savings estimation mode is activated, Compute Optimizer analyzes the Reserved Instances pricing discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

For Aurora DB cluster storage recommendations, this represents the percentage difference in total costs (instance, storage, and I/O) between the current and recommended storage types.

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

#### Estimated monthly savings calculation
<a name="rds-estimated-monthly-savings-calculation"></a>

For each recommendation, Compute Optimizer calculate the cost to operate a new RDS DB instance or storage using the recommended specifications. Estimated monthly savings are calculated based on the number of running hours for the current instance or storage and the difference in rates between the current specifications and the recommended specifications. The estimated monthly savings for RDS DB instances and storage that are displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all over-provisioned findings in the account.

### Performance risk
<a name="rds-performance-risk"></a>

The performance risk columns on the **RDS DB instance details** page and the **RDS DB instance recommendations** page define the likelihood of the current and recommended instance type not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the current and recommended instance. This includes specifications such as CPU, EBS throughput, and EBS IOPS. The performance risk of the current and recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A very low performance risk means that the instance type is predicted to always provide enough capability. The higher the performance risk means that you should validate whether the instance meets the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. 

### Comparison graphs
<a name="rds-utilization-graphs"></a>

The **Amazon RDS database details** page displays utilization metric graphs for your current and recommended RDS DB instance and storage data for the lookback period. Compute Optimizer uses the maximum utilization point within each 5-minute time interval to generate RDS DB instance and storage recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks. You can also change the statistic of the graphs between average and maximum.

The following comparison graphs are displayed on the **Aurora and RDS database details** page.

------
#### [ RDS DB instances ]

The following graphs are displayed for RDS DB instances:


| Graph name | Description | 
| --- | --- | 
| CPU utilization | The percentage of allocated compute units that are in use on the DB instance. This metric identifies the processing power that's required to run an application on an instance. | 
| Database connections (count) | The number of client sessions that are connected to the DB instance. | 
| Network receive throughput (MiB/second) | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
| Network transmit throughput (MiB/second) | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
| EBS read operations (per second) | The average number of disk read I/O operations per second. | 
| EBS write operations (per second) | The average number of disk write I/O operations per second. | 
| EBS read throughput (MiB/second) | The average number of bytes read from disk per second. | 
| EBS write throughput (MiB/second) | The average number of bytes written to disk per second. | 
| EBS IO balance (percent) | The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
| EBS Byte Balance (percent) | The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
| Free storage space | The amount of available storage space. | 
| DB Load | The level of session activity in your database. For more information, see [ Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html) in the *Amazon Relational Database Service User Guide*. | 
| Swap in (KB) | The amount of memory, in kilobytes, swapped in from disk. | 
| Swap out (KB) | The amount of memory, in kilobytes, swapped out to disk. | 

**Note**  
The **DB Load**, **Swap in (KB)**, and **Swap out (KB)** metrics are only available if you enabled Amazon RDS Performance Insights. To enable Performance Insights for your DB instances, see [ Turning Performance Insights on and off for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Relational Database Service User Guide*.

------
#### [ Aurora DB instances ]

The following graphs are displayed for Aurora DB instances:


| Graph name | Description | 
| --- | --- | 
| CPU utilization | The percentage of CPU used by an Aurora DB instance. | 
| Memory utilization | The percentage of memory allocated by applications and the operating system as used. | 
| Database connections (count) | The number of client sessions that are connected to the DB instance. | 
| Network receive throughput (MiB/second) | The amount of network throughput received from clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the Aurora DB cluster and the cluster volume. | 
| Network transmit throughput (MiB/second) | The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | 
| Storage network read throughput (MiB/second) | The amount of network throughput received from the Aurora storage subsystem by each instance in the DB cluster. | 
| Storage network write throughput (MiB/second) | The amount of network throughput sent to the Aurora storage subsystem by each instance in the Aurora DB cluster. | 
| Aurora memory health state | Indicates the memory health state. A value of `0` equals `NORMAL`. A value of `10` equals `RESERVED`, which means that the server is approaching a critical level of memory usage.  This metric applies to Aurora MySQL only.  | 
| Aurora memory number of declined SQL queries | The total number of queries declined as part of out-of-memory (OOM) avoidance. This metric applies to Aurora MySQL only.  | 
| Aurora memory number of connections closed | The total number of connections closed as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
| Aurora memory number of queries killed | The total number of queries ended as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
| Buffer cache hit ratio | The percentage of requests that are served by the buffer cache. This graph is shown when an Optimized Reads DB instance class type is recommended an as option to help you evaluate whether it is the right fit for your workload. | 
| Read IOPS ephermal storage | The average number of disk read operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
| Write IOPS ephermal storage | The average number of disk write operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
| Read IOPS | The average number of disk read operations per second.  | 
| Write IOPS | The number of Aurora storage write records generated per second. This is more or less the number of log records generated by the database. These do not correspond to 8K page writes, and do not correspond to network packets sent. | 
| DB Load | The number of active sessions for the database. Typically, you want the data for the average number of active sessions. In Performance Insights, this data is queried as db.load.avg. | 

For more information, see [ Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*.

**Note**  
The **DB Load** graph is only available if you enabled Performance Insights for Aurora. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*.

------
#### [ Aurora DB clusters ]

The following graphs are displayed for Aurora DB clusters:


| Graph name | Description | 
| --- | --- | 
| VolumeBytesUsed | The amount of storage used by your Aurora DB cluster. | 
| VolumeReadIOPs | The number of billed read I/O operations from a cluster volume within a 5-minute interval. | 
| VolumeWriteIOPs | The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals. | 

------

### Accessing Aurora and RDS database recommendations and details
<a name="rds-view-recommendations"></a>

You can use one of the following procedures to access either the **Aurora and RDS database recommendations** or the **Aurora and RDS database details** pages in the AWS Console.

On the **Aurora and RDS database recommendations** page you can view the recommendations for your RDS DB instances. On the **Aurora and RDS database details** page you can view the details of a specific instance or storage and its recommendations.

#### Procedures
<a name="rds-view-process"></a>

##### Accessing Aurora and RDS database recommendations page
<a name="rds-view-recommendations-process"></a>

**To access the Aurora and RDS database recommendations page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Aurora and RDS databases** in the navigation pane.
**Note**  
The current instances listed are from the AWS Region that is currently selected, in the selected account.

1. You can perform the following actions on the recommendations page:
   + View your instance or storage recommendations by choosing the **Instance** or **Storage** tab.
   + In the **Instance** tab only, you can view the price and performance impact of running your workload on AWS Graviton-based instances. To do this, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown list. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current RDS DB instance.
   + Filter instance or storage recommendations to one or mores AWS Regions. To do this, enter the name of the Region in the **Filter by one or more properties** text box, or choose one or more Regions in the drop-down list that appears.
   + Filter your instance or storage recommendations by tags. To do this, first select the **Tag key** or **Tag value** text box. Then, enter the key or value that you want to filter your RDS instance recommendations by.

     For example, to find all the recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
   + View instance or storage recommendations in another account. To do this, choose **Account**, and then select a different account ID.
**Note**  
If you're signed in to a management account of an organization and trusted access with Compute Optimizer is enabled, you can view recommendations for resources in other accounts. For more information, see [Accounts supported by Compute Optimizer](#supported-accounts) and [Trusted access for AWS Organizations](#trusted-service-access).
   + Clear the selected filters. To do this, choose **Clear filters** next to the filter.

##### Accessing Aurora and RDS database details page
<a name="rds-viewing-details"></a>

**To access the Aurora and RDS database details page**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Aurora and RDS databases** in the navigation pane.

1. Choose the finding classification listed next to the RDS DB instance or storage volume that you want to view.

1. You can perform the following actions on the details page:
   + View your instance or storage recommendations by choosing the **Instance** or **Storage** tab.
   + In the **Instance** tab only, you can view the price and performance impact of running your workload on AWS Graviton-based instances, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, the **Current** (default) option displays recommendations that are based on the same CPU vendor and architecture as the current RDS DB instance.
   + On the comparison graphs, you can hover over the graph to see exact values on specific dates over the analysis period. 
   + To change the time range of the graphs, choose **Time Range**, and then choose **Last 24 hours**, **Last 3 days**, **Last week**, or **Last 2 weeks**. 

     Choosing a shorter time range displays the data points at a higher granularity, which provides a higher level of detail.
   + To change the statistic value of the graphs, choose **Statistics**, and then choose **Average** or **Maximum**.

     You can use this option to determine the typical utilization of your workload over time. To view the highest value observed during the specified period, change the selection to **Maximum**. This way, you can determine the peak instance usage of your workload over time.

## Viewing idle resource recommendations
<a name="view-idle-recommendations"></a>

Compute Optimizer helps you identify idle resources that can be deleted or stopped to reduce your AWS cloud costs. Idle recommendations can be accessed through the Compute Optimizer console and our [ set of APIs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetIdleRecommendations.html). Idle recommendations are available for the following supported AWS resources:
+ Amazon EC2 instances
+ Amazon EC2 Auto Scaling groups
+ Amazon EBS volumes
+ Amazon ECS services on Fargate
+ Amazon Aurora and RDS databases
+ Amazon NAT Gateway
+ Amazon DynamoDB
+ Amazon ElastiCache
+ Amazon MemoryDB
+ Amazon DocumentDB
+ Amazon WorkSpaces
+ Amazon SageMaker endpoints

The recommendations are refreshed daily. These recommendations are generated by analyzing the specifications and utilization metrics of your AWS resources over the lookback period. The lookback period depends on the supported resource and your recommendation preference settings. If you don't have any recommednation preferences set, we use the default lookback period of 14 days. For more information, see [Idle criteria per resource](#idle-criteria).

**Note**  
For EBS volumes and NAT Gateway we analyze the attachment status over a 32-day lookback period. For WorkSpaces, we analyze user connection activity over a 63-day lookback period.
Changing the lookback period for EBS volume recommendations to 14 days does not affect the 32-day lookback period used to determine whether an EBS volume is unattached.
For ElastiCache, it may take up to 48 hours for recommendations to appear after opting in to Compute Optimizer.

**Topics**
+ [Idle criteria per resource](#idle-criteria)
+ [Estimated monthly savings](#idle-savings-calculation)

### Idle criteria per resource
<a name="idle-criteria"></a>

Each of the supported resources eligible for idle recommendations has its own criteria to be found idle. The following table breaks down the idle criteria for each resource and also provides Compute Optimizer’s recommended action for the idle resource.


| Resource | Metric analyzed | Idle criteria | Recommended action | 
| --- | --- | --- | --- | 
| Amazon EC2 instances | CPU utilization, network IO, GPU utilization, GPU encoder usage, and GPU memory usage | The peak CPU utilization is below 5% and your network I/O is less than 5MB/day over the 14-day lookback period.<br />G or P instance types are considered idle if they meet the following criteria over the 14-day lookback period:+  GPU isn’t actively working for more than 99% of the lookback period <br />+  GPU encoder isn't used for 99% or more of the instance's runtime <br />+  GPU memory usage at instance level is less than 5%  <br />+  CPU maximum utilization is less than 5% <br />+  Network utilization is less than 5 MB/day  | Verify whether you need this instance. If you don't need it, consider deleting this instance. | 
| EC2 Auto Scaling groups | CPU utilization, network IO, GPU utilization, GPU encoder usage, and GPU memory usage | The EC2 Auto Scaling group has no instances with more than 5% peak CPU utilization or 5 MB/day network utilization over the 14-day lookback period.<br />EC2 Auto Scaling groups that use G or P instance types are considered idle if the instances meet the following criteria over the 14-day lookback period:+  GPU isn’t actively working for more than 99% of the lookback period <br />+  GPU encoder isn't used for 99% or more of the instance's runtime <br />+  GPU memory usage at instance level is less than 5%  <br />+  CPU maximum utilization is less than 5% <br />+  Network utilization is less than 5 MB/day  | Verify whether you need this group. Consider scaling down this group to one instance or consider deleting it. | 
| Amazon EBS volumes | Read/Write operations and attachment status | Compute Optimizer can find an EBS volume to be idle or unattached.+  **Idle** — If the sum of read/write operations is less than 1 per day over the look-back period, and the volume is not a root volume. The default look-back period is 14 days, which you can extend up to 32 days. <br />+  **Unattached** — If the volume isn’t attached to any EC2 instance over the 32-day lookback period.    Changing the lookback period for EBS volume recommendations to 14 days does not affect the 32-day lookback period used to determine whether an EBS volume is unattached.    | Verify whether you need this volume. If you don't need it, we recommend that you create a snapshot of the volume and consider deleting it. | 
| Amazon ECS services on Fargate | CPU utilization and memory utilization | The peak CPU and memory utilization is below 1% over the lookback period. The default lookback period is 14 days, which you can extend up to 32 days. | Verify whether your containerized application is running as expected. If the application is not running, consider deleting this service. | 
| Amazon Aurora and RDS databases | Database connections, read/write IOPS, and CPU utilization | **RDS for MySQL and RDS for PostgreSQL**<br />The DB instance is not a read replica, and had no database connections, low CPU usage, and low read/write activity over the lookback period.<br />**Aurora MySQL and Aurora PostgreSQL**<br />The DB instance is not part of a secondary cluster in an Aurora Global Database, and had no database connections, low CPU usage, and low read/write activity over the lookback period. | Verify whether you need this DB instance. If you don’t need this instance temporarily, you can stop RDS MySQL and RDS PostgreSQL DB instances for up to 7 days. If you no longer need this instance, you can create a DB snapshot and delete the instance. For idle Aurora MySQL and Aurora PostgreSQL instances, you can also change the DB instance class to db.serverless. | 
| Amazon NAT Gateway | Active connection count, Packets in from source, Packets in from destination | The NAT Gateway is in available state, is not associated with any AWS Route Tables, and has no active connection, no Packets in from both source and destination over the lookback period. | Verify whether you need this NAT Gateway. Check if it's part of a disaster recovery setup or serves as a backup in your network architecture. | 
| Amazon DynamoDB | Consumed read capacity units and consumed write capacity units | Applies to provisioned tables only. A table is considered idle when there are no consumed read or write capacity units at both the table level and all Global Secondary Index (GSI) levels over the 14-day lookback period. | Verify whether this table is unused. Consider switching to on-demand mode or minimize provisioned capacity. If no longer needed, consider exporting data to S3 and deleting the resource. | 
| Amazon ElastiCache | New connections, engine CPU utilization, cache hits, cache misses, get commands, and set commands | Applies to Redis and Valkey engines only.<br />**Node-based (provisioned)**<br />The cluster has no new connections, engine CPU utilization is below 1%, and no cache hits, misses, get commands, or set commands over the 14-day lookback period. Metrics are evaluated at the node level; a cluster is idle only if all nodes are idle.<br />**Serverless**<br />The cluster has no processing units consumed, no current or new connections, and no cache hits, misses, get commands, or set commands over the 14-day lookback period. | Verify whether your application still requires this caching layer. For provisioned clusters, consider switching to ElastiCache Serverless for variable workloads. If not required, consider deleting the resource. | 
| Amazon MemoryDB | New connections, engine CPU utilization, keyspace hits, and keyspace misses | The cluster has no new connections, engine CPU utilization is below 1%, and no keyspace hits or misses over the 14-day lookback period. The cluster must be in available status. | Verify whether your application still requires this caching layer. If not required, consider deleting the resource. | 
| Amazon DocumentDB | Database connections | Applies to both provisioned and serverless clusters. Elastic clusters are excluded.<br />The cluster has no database connections over the 14-day lookback period. The cluster must be in available status. | **Provisioned**<br />Verify whether you need this cluster. If not needed temporarily, you can stop the resource for up to 7 days or consider switching to DocumentDB Serverless. If no longer needed, create a DB snapshot and delete the resource.<br />**Serverless**<br />Verify whether you need this cluster. If not needed temporarily, you can stop the resource for up to 7 days. If no longer needed, create a DB snapshot and delete the resource. | 
| Amazon WorkSpaces | User connection activity | Applies to Always On WorkSpaces only. Auto Stop and Standby WorkSpaces are excluded.<br />No user has connected to the WorkSpace over the 63-day lookback period. | Verify whether this WorkSpace is still needed by the assigned user. If temporarily not needed, consider switching to Auto Stop mode. If the user no longer requires access, consider deleting the resource. | 
| Amazon SageMaker endpoints | Invocations | The endpoint had zero invocations over the 14-day lookback period. | Verify whether this endpoint is still in use. If infrequently used, consider enabling scale-to-zero functionality for inference components if supported. If no longer required, consider deleting the resource. | 

### Estimated monthly savings
<a name="idle-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience by taking Compute Optimizer’s recommended action per idle resource under the supported pricing models. The supported pricing models depends on the specific AWS resource. For example, EC2 instances supports Savings Plans and Reserved Instances discounts but ECS services only supports the Savings Plans pricing model. To receive recommendations with supported pricing models, the savings estimation mode preference needs to be activated. For more information, see [ Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column on both the Instance and Storage tabs display the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you experience by taking Compute Optimizer’s recommended action per idle resource under the On-Demand pricing model.

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

# Apply optimization recommendations using Automation
<a name="automation"></a>

Automation is a feature within AWS Compute Optimizer that enables you to apply optimization recommendations to your AWS resources, which can help you reduce cost and improve performance. You can apply recommended actions directly or create automation rules that implement recommendations on a recurring schedule when they match your specified criteria. With automation rules, set criteria such as AWS Region and Resource Tags to target specific geographies and workloads. Configure rules to run daily, weekly, or monthly, and Compute Optimizer continuously evaluates new recommendations against your criteria. Track automation events over time, examine detailed step history, estimate savings achieved, and reverse actions directly from Compute Optimizer when needed.

## Enabling Automation
<a name="automation-enable"></a>

When you access the Automation section of the Compute Optimizer console for the first time, you're asked to enable the feature using the account that you’re signed in with. You can also opt in using the Compute Optimizer Automation API, AWS Command Line Interface (AWSCLI), or SDKs.

By enabling this feature, you authorize Compute Optimizer to implement optimization recommendations by managing AWS resources in your account. This includes creating Amazon EBS snapshots, deleting EBS volumes, and modifying EBS volumes. In the future, AWS may expand the types of optimization recommendations that AWS Compute Optimizer can implement and the AWS resources it can manage. 

To enable Automation, you need specific permissions to update the Automation enrollment configuration and create the necessary service-linked role. For more information on service-linked roles, see [Using service-linked roles for AWS Compute Optimizer](#using-service-linked-roles).

**To enable Automation**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose any page under the **Automation** section.

1. On the feature landing page, choose **Enable Automation**.

1. When prompted, review the note on service-linked role permissions and choose **Enable Automation**.

To enable Automation using IAM policies, see [Enabling Automation](#automation-enable).

If you're enabling Automation for member accounts in your organization, the management account also needs permissions to associate and disassociate accounts. These permissions allow the management account to enable Automation for member accounts and configure whether the management account can implement optimizations on behalf of the member account. For more information, see [Enabling Automation for your organization](#automation-org). 

### Policy to enable Automation for your account
<a name="policy-automation-enable-coa"></a>

The following policy statement enables Automation for your account.

```
{
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        }
    ]
}
```

## Enabling Automation for your organization
<a name="automation-org"></a>

When you enable Automation for your organization’s management account, you can also configure Automation for your organization’s member accounts, enabling centralized implementation of optimization actions across your organization. This centralized approach can help you optimize for cost and performance at scale.

### Policy to enable Automation across your organization
<a name="automation-enable-org-coa"></a>

The following policy statement enables Automation across your organization.

```
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:AssociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:DisassociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:ListAccounts",
            "Resource": "*"
        }
    ]
}
```

### Trusted access for AWS Organizations
<a name="automation-org-access"></a>

You must have trusted access enabled to manage automation for your member accounts. When you opt in to Compute Optimizer using your organization's management account and include all member accounts, trusted access is automatically enabled. This allows Compute Optimizer to analyze resources and generate recommendations for member accounts. Trusted access also allows Compute Optimizer to implement recommendations for member accounts that have also enabled the Automation feature.

Compute Optimizer verifies that trusted access is enabled each time you access recommendations or apply recommendations for member accounts. If you disable trusted access, the management account loses access to recommendations and automation for your organization's member accounts. To re-enable trusted access, opt in to Compute Optimizer again using your organization's management account and include all the member accounts. For more information, see [Opting in to AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html). For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the AWS Organizations User Guide.

### Configure automation for member accounts
<a name="automation-org-configure"></a>

To enable Automation for member accounts, the management account needs permissions to associate and disassociate accounts. These permissions allow the management account to enable Automation for member accounts and configure whether the management account can implement optimizations on behalf of member accounts. For more information , see [Policy to enable Automation across your organization](#automation-enable-org).

Once a member account is associated, the management account or delegated administrator can view and apply recommended actions to the member account. When you associate a member account, its organization rule mode is automatically set to Any Allowed, which permits the management account to create Automation rules that automatically apply actions to that account. If the member account has not previously enabled the Automation feature, the association process automatically enables it.

**To enable Automation for member accounts**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. Search for the account using its account Id.

1. Select the account and choose Add. You can enable Automation for up to 50 accounts at a time.

### Organization rule mode
<a name="automation-org-rule"></a>

This setting controls whether the management account can implement automated optimization actions for the member account. When set to Any Allowed, the management account can directly implement recommended actions or create Automation rules that apply to the member account. When set to None Allowed, only the member account can act on its own recommendations, and management account rules will not apply. When you enable Automation for a member account, its organization rule mode is automatically set to Any Allowed.

Organization rules targeting a member account automatically start or stop applying based on the organization rule mode setting. Rules apply when the mode is set to Any Allowed and stop applying when set to None Allowed. If you change the mode to None allowed, any in-progress automation steps initiated by organization rules will continue to completion, but no new automation steps will be triggered by organization rules for that account.

**To configure organization rule mode for member accounts**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. Select the accounts that you want to configure.

1. Choose **Actions** and select `Allow organization rules `or `Disallow organization rules`. You can select and update the configuration for up to 50 accounts at a time.

## Recommended actions
<a name="automation-rec"></a>

Recommended actions are optimization opportunities that you can implement through Compute Optimizer. They are a subset of Compute Optimizer's recommendations. You can view and apply each recommended action directly or create automation rules to implement them on a recurring schedule when they match your specified criteria.

### Recommended actions summary
<a name="automation-rec-view-summary"></a>

This section of the Recommended actions page summarizes the estimated monthly savings for your selected recommended actions and the total opportunity available based on your filters. You can select and apply up to 10 actions at a time.

### Recommended action types
<a name="automation-rec-view-type"></a>

In the recommended actions table, you will find a list of optimization opportunities. The following recommended action types are supported:
+ Snapshot and delete unattached EBS volumes: This action is recommended for volumes unattached from EC2 instances for 32 or more days. Compute Optimizer creates a snapshot to back up your data before deleting the volume. For more information about this recommendation criteria, see [Idle criteria per resource](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html#idle-criteria).
+ Upgrade EBS volume type: This action is recommended for volumes using previous generation volume types with an `Optimized` finding. Volumes with a `NotOptimized` finding are not eligible. Upgrading to newer generation volume types, such as gp3 and io2, provides better performance and cost efficiency with improved IOPS and throughput capabilities at lower prices. For the definition of each finding, see [EBS volume finding classifications](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html#ebs-recommendations-findings).

There are several considerations when applying recommended actions:
+ The estimated monthly savings considers the snapshot cost based on the volume's provisioned size. Actual snapshot cost depends on the incremental EBS snapshot size. 
+ When Compute Optimizer implements recommended actions that involve creating EBS snapshots, it automatically applies an AWS-generated tag to each snapshot. The tag key is `aws:compute-optimizer:automation-event-id`, and its value contains the unique identifier of the corresponding automation event. Compute Optimizer applies this tag to EBS snapshots created on or after February 24, 2026.
+ Amazon EBS supports up to four Elastic Volumes modifications per volume within a rolling 24-hour period. Volume modifications applied through Compute Optimizer count toward this limit. After Compute Optimizer completes a volume modification, you can initiate additional modifications as long as the total number of modifications remains within the limit. For more information, see the [Amazon EBS User Guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html).
+ Snapshot and delete unattached EBS volumes does not modify resource properties. A later deployment cannot silently reset an optimized property value. If the volume is declared in an infrastructure-as-code (IaC) template (for example, a CloudFormation stack or a Terraform configuration), the IaC tool reports drift after the deletion. Remove the resource definition from your template to reconcile the state.

### Estimated monthly savings
<a name="automation-rec-savings"></a>

**Estimated monthly savings (after discounts)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. If you have savings estimation mode enabled, the estimated monthly savings include your specific discounts. To receive recommended actions that include your specific discounts, enable the savings estimation mode preference. For more information, see Savings estimation mode.

**Note**  
If you don't enable the savings estimation mode preference, this column displays estimated monthly savings based on On-Demand pricing.

**Estimated monthly savings (On-Demand)**

This column in the recommended actions table displays the estimated monthly savings from implementing the recommended action. The estimated monthly savings calculation is based on On-Demand pricing.

### Viewing recommended actions
<a name="automation-rec-view"></a>

The Recommended actions page displays a summary of your recommended actions and a table with details for individual actions. Recommended actions help you optimize your resources for performance and cost savings.

**Note**  
Your organization’s management account and delegated administrator can view recommended actions for member accounts with Automation enabled and configured to allow centralized optimization. For more information, see [Enabling Automation for your organization](#automation-org).

**To access recommended actions**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Recommended actions** under the **Automation ** section.

1. You can perform the following actions on the **Recommended actions** page:

   - View recommended actions.

   - Filter recommended actions by one or more properties such as AWS Region or Resource Tag key-values.

   - Select the recommended actions that you want to apply.

   - View a summary of the estimated monthly savings for your selected recommended actions and the total opportunity available based on your filters.

   - Create automation rule from your selected filters. This pre-fills the rule creation form with your selected filters in the recommended actions table.

### Apply recommended actions
<a name="automation-rec-apply"></a>

You can select up to 10 recommended actions at a time to apply. Once you apply the recommended action, it will be removed from the Recommended action page and an automation event will be created. You can view and monitor the status of the action in the [Automation events](#automation-events) page. Automation events awaiting execution will be in Ready status. You can have up to 100 automation events in Ready status per account per region.

**To apply recommended actions**

1. On the **Recommended actions** page, select up to 10 recommended actions that you want to apply.

1. Choose **Review and apply**. You will be able to review and confirm your selection on the next page before implementing actions.

1. Review your selection. You can remove selected recommended by clicking on the in-line remove icon.

1. Choose **Confirm and apply**.

1. When prompted to confirm, type `“confirm”` and choose **Apply changes**.

## Automation rules
<a name="automation-rules"></a>

Automation rules automatically implement recommended actions based on your defined criteria and schedule. Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available. You can create, update, and delete automation rules from any AWS Region where Compute Optimizer Automation is available.

### Rule type
<a name="automation-rules-type"></a>

There are two types of rules:
+ Account rules: Rules that apply recommended actions only to your account.
+ Organization rules: Rules that centrally apply recommended actions across member accounts. 

**Note**  
Only the management account or delegated administrator can create organization rules. You can only select member accounts with Automation enabled and organization rules allowed can be selected for the rule to apply. Member accounts can view the details of organization rules that apply to their account but cannot edit them. Organization rules can be configured to apply before or after member account rules.

### Rule criteria
<a name="automation-rules-criteria"></a>

When configuring a rule, choose the recommended action types you want your rule to implement, such as snapshot and delete unattached Amazon EBS volumes and upgrade Amazon EBS volume type. Refine your selection using criteria such as AWS Region and Resource Tags. Then preview the current matching recommended actions to validate your criteria.

**Important**  
If you don't specify rule criteria, Compute Optimizer applies all the selected recommended actions types in the accounts you select in your rule scope, including recommended actions in all AWS Regions where Compute Optimizer Automation is available. 

The following recommended action attributes and comparison operators are supported for automation rules:


| Attribute | Operator | Field type | 
| --- | --- | --- | 
| Current volume size (GiB) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Integer | 
| Current volume type | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Estimated savings ($) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Double | 
| Lookback period (days) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Integer | 
| AWS Region | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Resource ARN | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Resource tags | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | Resource Tag | 
| Restart needed | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 

You can specify up to 20 conditions per attribute and 20 values per condition. For more information, see [Criteria](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Criteria.html) in the AWS Compute Optimizer Automation API Reference.

#### Comparison operators
<a name="automation-rules-comparison-operators"></a>

Use comparison operators in rule criteria to match recommended action attributes against the values you specify.

**Important**  
If the attribute that you specify in your rule criteria is not present on the recommended action, the values do not match, the condition is false, and the recommended action is excluded from the rule. This logic applies to all comparison operators except the `...IfExists` operators, which evaluate to true when the attribute is not present. The `...IfExists` operators test whether the attribute is present (exists) on the recommended action.

##### String condition operators
<a name="automation-rules-string-operators"></a>

String condition operators let you define rule criteria that compare a recommended action attribute to a string you specify.


| Condition operator | Description | 
| --- | --- | 
| `StringEquals` | Exact matching, case sensitive. | 
| `StringNotEquals` | Negated exact matching, case sensitive. | 
| `StringEqualsIgnoreCase` | Exact matching, ignoring case. | 
| `StringNotEqualsIgnoreCase` | Negated matching, ignoring case. | 
| `StringLike` | Case-sensitive matching. The values can include multi-character match wildcards (`*`) anywhere in the string. You must specify wildcards to achieve partial string matches. | 
| `StringNotLike` | Negated case-sensitive matching. The values can include multi-character match wildcards (`*`) anywhere in the string. | 

**Note**  
Using `*` alone as a value with `StringLike` matches any value that is present. When combined with `StringNotLike`, a value of `*` means "does not match anything" — effectively excluding all recommended actions where the attribute is present. For example, using `StringNotLike` on a tag key `Application` with value `*` excludes any recommended action that has the `Application` tag, regardless of the tag's value.

##### Numeric condition operators
<a name="automation-rules-numeric-operators"></a>

Numeric condition operators let you define rule criteria that compare a recommended action attribute to an integer or decimal number.


| Condition operator | Description | 
| --- | --- | 
| `NumericEquals` | Exact numeric matching. | 
| `NumericNotEquals` | Negated numeric matching. | 
| `NumericLessThan` | "Less than" matching. | 
| `NumericLessThanEquals` | "Less than or equals" matching. | 
| `NumericGreaterThan` | "Greater than" matching. | 
| `NumericGreaterThanEquals` | "Greater than or equals" matching. | 

For example, you can use `NumericGreaterThanEquals` with the **Lookback period** attribute to create a rule that only automates recommended actions where the lookback period used to generate the recommendation is at least 32 days.

#### IfExists operators
<a name="automation-rules-ifexists-operators"></a>

Append `IfExists` to any comparison operator (for example, `StringLikeIfExists`) to change how a condition is evaluated when the attribute you specify is **absent** from a recommended action:
+ With a base operator, an absent attribute evaluates to **false**, and the recommended action is **excluded** from the rule.
+ With the `...IfExists` variant, an absent attribute evaluates to **true**, and the recommended action is **included**.

`IfExists` is helpful when you want to exclude a specific group of resources from a rule but still include the resources that don't carry the tag you're filtering on. For example, you might want to include everything except the resources owned by one team. A base `StringNotEquals` on `team` = `TeamA` excludes TeamA's resources, but it also excludes every resource that doesn't carry the `team` tag at all — leaving out resources you intended to include. Add `IfExists` to keep those untagged resources in scope:
+ **StringNotEquals** matches only resources that have the `team` tag set to a value other than `TeamA`. Untagged resources are excluded.
+ **StringNotEqualsIfExists** matches resources without the `team` tag *and* resources where it is set to any value other than `TeamA`. Only resources tagged `team` = `TeamA` are excluded.

`IfExists` is also helpful when you want to let resource owners exclude their own resources from automation. You can designate a dedicated opt-out tag, such as `automation-opt-out`, that an owner applies to any resource they want to leave out. In this case, the presence of the tag matters, not its value, so use `StringNotLikeIfExists` with the value `*` on the `automation-opt-out` tag key. The `*` wildcard matches any value, so Compute Optimizer excludes every resource that carries the tag. The `IfExists` variant keeps the resources that don't carry the tag in scope; without it, every untagged resource would be excluded as well.

#### Rule criteria examples
<a name="automation-rules-criteria-examples"></a>

##### Example: Include only recommended actions in specific Regions
<a name="automation-rules-criteria-examples-regions"></a>

The following rule criteria uses `StringEquals` on the **AWS Region** attribute to match recommended actions for resources in `us-east-1` or `us-west-2`. When you specify more than one value for a condition, the values have an OR relationship — a recommended action matches the condition if its attribute value matches any one of the values.

Criteria configuration:


| Attribute | Operator | Values | 
| --- | --- | --- | 
| AWS Region | `StringEquals` | `us-east-1`, `us-west-2` | 

Evaluation:


| Attribute value | Result | 
| --- | --- | 
| `us-east-1` | Match | 
| `us-west-2` | Match | 
| `eu-west-1` | No match | 

##### Example: Include only recommended actions generated with a minimum lookback period
<a name="automation-rules-criteria-examples-lookback"></a>

The following rule criteria uses `NumericGreaterThanEquals` on the **Lookback period (days)** attribute to only automate recommended actions where the lookback period used to generate the recommendation is at least 32 days. This lets you require a longer observation window before a recommended action is automated.

Criteria configuration:


| Attribute | Operator | Values | 
| --- | --- | --- | 
| Lookback period (days) | `NumericGreaterThanEquals` | `32` | 

Evaluation:


| Attribute value | Result | 
| --- | --- | 
| `32` | Match | 
| `14` | No match | 

##### Example: Include recommended actions unless the resource belongs to a specific team
<a name="automation-rules-criteria-examples-team"></a>

Consider a platform team that enables Compute Optimizer Automation across many accounts but wants to leave one team's resources out of the rule. The team already tags resources with a `team` tag for other purposes, but not every resource carries it. They want automation applied broadly while excluding any resource tagged `team` = `TeamA`.

The following rule criteria uses `StringNotEqualsIfExists` on the **Resource tags** attribute, with the tag key `team` and the value `TeamA`. A recommended action is included when the resource doesn't have the `team` tag at all, or when the tag is set to any value other than `TeamA`. Because many resources won't carry the tag, `IfExists` is what keeps them in scope — without it, every untagged resource would be excluded.

Criteria configuration:


| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotEqualsIfExists` | `team` | `TeamA` | 

Evaluation:


| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource does not have the `team` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `team` = `web` | Match | The tag is present and the value does not match `TeamA`. | 
| The resource has tag `team` = `TeamA` | No match | The tag is present and the value matches `TeamA`, so the recommended action is excluded. | 

##### Example: Include recommended actions unless the resource has an opt-out tag
<a name="automation-rules-criteria-examples-optout"></a>

You can let resource owners exclude individual resources from automation by applying a dedicated opt-out tag. In this example, an owner adds the `automation-opt-out` tag to any resource they want to leave out.

The following rule criteria uses `StringNotLikeIfExists` on the **Resource tags** attribute, with the tag key `automation-opt-out` and the value `*`. The `*` wildcard matches any value, so any resource that carries the tag is excluded. A recommended action is included when the resource doesn't have the `automation-opt-out` tag.

Criteria configuration:


| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotLikeIfExists` | `automation-opt-out` | `*` | 

Evaluation:


| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource does not have the `automation-opt-out` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `automation-opt-out` = `true` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 
| The resource has tag `automation-opt-out` = `temporary` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 

##### Example: Exclude recommended actions on infrastructure-as-code (IaC) managed resources
<a name="automation-rules-criteria-examples-iac"></a>

If you manage resources using an infrastructure-as-code (IaC) tool such as CloudFormation or Terraform, you can create an exclusion rule that filters out IaC-managed resources based on resource tags.

###### CloudFormation
<a name="automation-rules-criteria-examples-iac-cfn"></a>

Resources managed using CloudFormation have the system tags `aws:cloudformation:stack-id`, `aws:cloudformation:stack-name`, and `aws:cloudformation:logical-id`. You can filter on one of these tags to identify CloudFormation-managed resources. This example filters on `aws:cloudformation:stack-id`.

The following rule criteria uses `StringNotLikeIfExists` on the **Resource tags** attribute, with the tag key `aws:cloudformation:stack-id` and the value `*`. The `*` wildcard matches any value, so any resource that carries the tag is excluded. A recommended action is included when the resource does not have the `aws:cloudformation:stack-id` tag.

Criteria configuration:


| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotLikeIfExists` | `aws:cloudformation:stack-id` | `*` | 

Evaluation:


| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource has tag `aws:cloudformation:stack-id` = `arn:aws:cloudformation:us-east-1:123456789012:stack/my-stack/2ac98f30-5bdd-11e4-949b-50fa5262a838` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 
| The resource does not have the `aws:cloudformation:stack-id` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `Environment` = `production`, but not the `aws:cloudformation:stack-id` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 

###### Terraform
<a name="automation-rules-criteria-examples-iac-terraform"></a>

To exclude Terraform-managed resources from automated actions, add a user tag (for example, `ManagedBy` = `terraform`) to those resources in your Terraform configuration. After tagging, you can apply tag-based rule criteria to exclude them, similar to the preceding CloudFormation example.

##### Example: Combine multiple criteria
<a name="automation-rules-criteria-examples-combine"></a>

You can combine multiple criteria to narrow the scope of your rule. All criteria must match for a recommended action to be included in the rule (AND logic).

The following configuration automates EBS volume recommended actions that:

1. Are in us-east-1 and us-west-2

1. Were generated with a lookback period of at least 32 days; and

1. Are not opted out of automation (no `automation-opt-out` tag).

This rule includes a recommended action only when all three conditions are met simultaneously.

Criteria configuration:


| Attribute | Operator | Values | 
| --- | --- | --- | 
| AWS Region | `StringEquals` | `us-east-1`, `us-west-2` | 
| Lookback period (days) | `NumericGreaterThanEquals` | `32` | 
| Resource tags (key: `automation-opt-out`) | `StringNotLikeIfExists` | `*` | 

### Schedule
<a name="automation-rules-schedule"></a>

Set a schedule for when your rule runs by specifying the frequency (daily, weekly, or monthly), start time, end time, and timezone. During this window, Compute Optimizer will start implementing recommended actions that match your specified criteria. The number of actions that get initiated depends on the duration of your scheduled time window, Compute Optimizer Automation's concurrency limit, and the time required to complete each action. Automated actions will show as "In-Progress" until all steps in the automation workflow are fully completed. Up to 100 actions can be in-progress concurrently per account per AWS Region.

### Rule order
<a name="automation-rules-order"></a>

By default, rules are created with rule order 1 (highest priority) within their rule group. For example, when a management account creates an organization rule configured to apply after member account rules, it receives a rule order of 1, the highest priority among all rules in that group. Rule group and rule order determine which rule applies when a recommended action in an account matches multiple rules. Compute Optimizer assigns the action to the active rule with the lowest rule order value (highest priority), regardless of when that rule is scheduled to run.

For example, if a recommended action matches all of the rules in the following table, Compute Optimizer assigns it to Rule-C and implements it according to Rule-C's schedule.



- ** Organization rules evaluated before member account rules **
  - **Rule order:** 1 / **Rule name:** Rule-A / **Status:** Inactive / **Schedule:** Weekly on Mondays from 12:00 to 13:00 UTC
  - **Rule order:** 2 / **Rule name:** Rule-B / **Status:** Inactive / **Schedule:** Daily from 12:00 to 13:00 UTC

- ** Member account rules **
  - **Rule order:** 1 / **Rule name:** Rule-C / **Status:** Active / **Schedule:** Monthly on 15th from 12:00 to 13:00 UTC
  - **Rule order:** 2 / **Rule name:** Rule-D / **Status:** Inactive / **Schedule:** Monthly on 15th from 12:00 to 13:00 UTC

- ** Organization rules after before member account rules **
  - **Rule order:** 1 / **Rule name:** Rule-E / **Status:** Inactive / **Schedule:** Weekly on Mondays from 12:00 to 13:00 UTC
  - **Rule order:** 2 / **Rule name:** Rule-F / **Status:** Active / **Schedule:** Daily from 12:00 to 13:00 UTC



### Creating automation rules
<a name="automation-rules-create"></a>

You can use an automation rule to manage automated implementation of recommended actions in Compute Optimizer. For background information about how automation rules work, see [Automation rules](#automation-rules).

Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available.

You can only create one automation rule at a time. To create multiple automation rules, follow the console procedures multiple times, or call the API or command multiple times with your desired parameters.

When you create an automation rule in the Compute Optimizer console, you can preview the current recommended actions that match your rule criteria. This can help you validate and iterate on your rule criteria.

**Important**  
When you create an organization rule in the management account and apply it to member accounts, those member accounts will be able to see the details of the rule from their account. AWS recommends that you don't include personally identifying, confidential, or sensitive information in your rule name, description, or other fields.

**To create an automation rule**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose **Create Automation rule**.

1. If you are creating a rule in the management account or delegated administrator, you can choose the **rule type**, the **member accounts** you want to apply the rule, and whether to apply the rule **before** or **after member account rules**. You can only select member accounts with Automation enabled and organization rules allowed can be selected for the rule to apply.

1. Choose the **action types** you want this rule to implement.

1. (Optional) You can specify **rule criteria** to refine which recommended actions will be automatically implemented. For each criteria, use the `Attribute`, `Operator`, and `Value` drop down menus and input fields to specify your rule criteria.

   You can also configure the following optional checkboxes for each criteria:
   + **If exists** – Select this to also match recommended actions where the attribute field is absent. For more information, see [Rule criteria](#automation-rules-criteria).
   + **Ignore case** – Select this for case-insensitive matching. Available only when the operator is `Equals` or `Does not equal` and the attribute uses free-form input (Resource ARN, Resource tags).
**Important**  
If you don't specify rule criteria, Compute Optimizer applies all recommended action types across the accounts in your rule scope, including recommended actions in all AWS Regions where Compute Optimizer Automation is available. 

1. (Optional) Choose **Refresh matching actions** to get a preview of the recommended actions that match your rule criteria.

1. Set a recurring **Schedule** for your rule to automatically implement matching actions. This includes the frequency (daily, weekly, or monthly), start time, end time, and time zone.

1. (Optional) You can add **Tags** as key-value pairs to your rule to help you easily identify the rule.

1. Provide a rule **name** and a **description** (optional) for your rule.

1. For **Rule status**, choose whether you want the rule to be `Active` or `Inactive` after it's created.

1. Choose **Create Automation rule**.

**Note**  
By default, rules are created with the rule order 1 (highest priority) in their rule group. You can update the rule order from the Automation rules page. To learn more more, see [Editing automation rule order](#automation-rules-edit).

### Viewing automation rule
<a name="automation-rules-view"></a>

The Automation rules page displays your automation rules and allows you to create and manage them. You can click on each rule to get more details, including the specific rule criteria used to match recommended actions.

**To view automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose the **rule name** of the rule you want to view details for.

1. You can perform the following actions on the **rule details** page:

   - View rule details and criteria.

   - Enable and disable the rule.

   - Edit the rule.

   - Delete the rule.

   - Manage tags for the rule.

### Updating automation rules
<a name="automation-rules-update"></a>

You can update rules at any time. You can only update the configuration of one rule at a time. Before you enable a rule by changing the rule status from `Inactive` to `Active`, review and confirm your rule criteria. You can preview the matching recommended actions before saving your updated rule criteria. If you change the mode to `Inactive`, any in-progress automation steps initiated by the rule will continue to completion, but no new automation steps will be triggered by the rule.

**To update automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the rule that you want to update.

1. Choose **Actions** and select **Edit**.

1. Update your rule configuration as needed.

1. Choose **Save changes**.

### Editing automation rule order
<a name="automation-rules-edit"></a>

Rule order determines which rule applies when a recommended action in an account matches multiple rules. Compute Optimizer assigns the action to the active rule with the lowest rule order value (highest priority), regardless of when that rule is scheduled to run. You can edit the rule order at any time. You can only edit one rule at a time. For organization rules, you can also edit the rule group to specify whether the rule applies before or after member account rules.

**To reorder automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Find the rule that you want to reorder.

1. Choose the **Rule order** cell for the rule you want to reorder, then use the menu to select the new rule order and choose the check mark icon.

1. When prompted choose Save changes. 

**To edit the rule group (organization rules only)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the rule that you want to edit.

1. In the **Apply rule** section, choose **Before member account rules** or **After member account rules**.

1. Choose **Save changes**.

1. Review the rule order on the **Automation rules** page to ensure that it matches your intended priority.

### Deleting or disabling automation rules
<a name="automation-rules-delete"></a>

When you delete an automation rule, Compute Optimizer permanently removes it from your account, and it no longer implements recommended actions. Previously implemented actions remain unchanged. To restore the automation rule, you must create a new rule. As an alternative to deletion, you can disable a rule. This retains the rule for future use, but Compute Optimizer won't apply the rule to any matching recommendations until you enable it.

**To delete or disable automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the rules that you want to delete. You can select up to 10 at a time.

1. Choose Actions and select Delete (to retain a rule and disable it, choose Disable).

1. When prompted, choose Delete (or Disable).

### Creating automation rules with CloudFormation
<a name="creating-automation-rules-with-cloudformation"></a>

AWS Compute Optimizer integrates with AWS CloudFormation, enabling you to define and deploy automation rules with infrastructure-as-code. You can create a template that describes the automation rules you want, and CloudFormation provisions and configures those rules for you. When you use CloudFormation, you can reuse your template to set up your automation rules consistently and repeatedly across multiple AWS accounts.

#### Compute Optimizer and CloudFormation templates
<a name="cfn-automation-rules-templates"></a>

To provision and configure automation rules, you must understand how [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) work. Templates are text files in JSON or YAML format. These templates describe the resources that you want to provision in your CloudFormation stacks.

If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

You can create CloudFormation templates for the following types of automation rules:
+ Account rules that apply recommended actions only to your account
+ Organization rules that centrally apply recommended actions across member accounts

For more information, including examples of JSON and YAML templates for automation rules, see [AWS::ComputeOptimizer::AutomationRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html) in the *AWS CloudFormation User Guide*.

#### Learn more about CloudFormation
<a name="cfn-automation-rules-learn-more"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

## Automation events
<a name="automation-events"></a>

The Automation events page is centralized dashboard that displays information about the automated actions initiated through Compute Optimizer. You can review summary information and get details for individual automation events. By default, the dashboard shows information automation events from the last 6 months. You can view events from the past year using the date filter.

The Events summary section summarizes the estimated monthly savings and count for your automation events by status.

You can track events completed over time by viewing the Monthly events summary chart, which summarizes the estimated monthly savings and count for your automation events, grouped by status and the month in which the automation event was created. The chart displays estimated monthly savings (not cumulative savings) for events executed in each month. These savings estimates represent the potential monthly savings calculated at the time of modification and do not reflect actual realized savings in that month or any subsequent months. The Monthly events summary chart shows the sum of all events shown in the Automation events table based on your selected filters. Estimated monthly savings are only displayed for events with Complete and Rollback Complete status.

This Automation events table displays automation events implemented by Compute Optimizer. Review details such as event type, description, status, and estimated monthly savings. These savings estimates represent the potential monthly savings calculated at the time of modification and do not reflect actual realized savings in that month or any subsequent months.

Select an automation event ID to view Event details and step history. The step history table provides a chronological record of operations performed during the automation event. Each step shows the specific action taken to modify your resource, along with its own step status, start time, and completion time.

### Rollback
<a name="automation-events-rollback"></a>

Rollback capabilities that allow you to reverse automated optimization actions if needed. You can initiate rollback from the Automation events page, where you can select and roll back up to 10 automation events at a time. You can only initiate rollback for events with Complete status. 

The specific rollback steps depend on the event type:
+ Snapshot and delete unattached EBS volume: Rolling back volume deletion creates a new EBS volume from the snapshot of the deleted volume. The new volume will have a different volume ID, and all user-created tags on the original volume will be restored to the new volume.
+ Upgrade EBS volume type: Rolling back volume type upgrades will modify the volume to the previous volume type configuration.

There are several considerations for rollback:
+ Compute Optimizer requires the original EBS snapshot created by Compute Optimizer to perform rollback operations for volume deletions. If you delete this snapshot and attempt to roll back the automation event, the rollback operation will fail. 
+ Amazon EBS supports up to four Elastic Volumes modifications per volume within a rolling 24-hour period. Volume modifications applied through Compute Optimizer count toward this limit. After Compute Optimizer completes a volume modification, you can roll back the event as long as the total number of volume modifications in the past 24 hours is fewer than four. Similarly, after a rollback completes, you can initiate additional modifications as long as the total number of modifications remains within the limit. For more information, see the [Amazon EBS User Guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html).
+ Compute Optimizer validates that the current Amazon EBS volume configuration matches the configuration at the time the automation event completed. If you modify the volume configuration after Compute Optimizer completes the automation event and then attempt to roll back the automation event, the rollback operation will fail.

### Automation event statuses
<a name="automation-events-status"></a>

Automation events reports the following status details:


| Event status | Event status reason | 
| --- | --- | 
| Ready | The automation has not started running. | 
| In-Progress | The automation is running. | 
| Complete | The automation completed successfully. | 
| Failed | The automation did not complete successfully. | 
| Rollback Ready | The rollback has not started running. | 
| Rollback In-Progress | The rollback is running. | 
| Rollback Complete | The rollback has completed successfully. | 
| Rollback Failed | The rollback did not complete successfully. | 

### View automation events
<a name="automation-events-view-details"></a>

This **Automation events** page displays automation events initiated by Compute Optimizer. Review details such as event type, description, status, and estimated savings.

**To view automation event details**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. You can perform the following actions on the **Automation events **page:

   View total estimated monthly savings and count summary by event status.

   - View monthly summary of automation events by status.

   - (Optional) Filter by date range, account ID (management account only), event status, event type, AWS Region, or Resource type.

   - Review history of automation events, including details on event status, estimated savings, created time, and completed time.

#### View automation events details
<a name="automation-events-view"></a>

Select an automation event ID to view more details and step history on **Event details** page.

**To view automation event details**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose the event ID of the automation event you want to get details for.

1. You can perform the following actions on the **Event details** page:

   - View details such as event status, estimated savings, created time, and completed time

   - View step history of operations performed during the automation event. Each step shows the specific action taken to modify your resource, along with its own step status, start time, and completion time. 

   - Initiate a roll back for the automation event.

### Roll back automation events
<a name="automation-events-rb"></a>

You can also initiate rollback for automation events if necessary. You can select and roll back up to 10 automation events at a time. You can only initiate rollback for events with Complete status. 

**To roll back an automation event**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the automation events that you want to roll back. You can select up to 10 events at a time to roll back.

1. Choose **Rollback events**.

1. Review your selected automation events to roll back.

1. Choose **Confirm all rollbacks**.

## Disabling Automation
<a name="automation-disable"></a>

You can disable the Automation feature at any time. However, the management account can't disable Automation for all member accounts in the organization. Each member must disable the feature at the account level.

**Note**  
Disabling Automation stops all of the automation rules in your account. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.

When the management account disables the Automation feature, Compute Optimizer retains the associations between the management account and its member accounts. If the management account opts back in later, Compute Optimizer automatically restores these associations. However, if a member account opted out independently during the period when the management account had the feature disabled, that member account will not be re-associated when the management account opts back in. 

**To disable the Automation feature**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose the **Automation** tab.

1. Choose **Disable Automation for account**

1. When prompted for confirmation, choose **Disable Automation**

# Recommendation preferences
<a name="viewing-recommendation-preferences"></a>

Recommendation preferences are features that you can activate so that Compute Optimizer generates resources recommendations that align more with your workload requirements. Following are the features that are currently available as recommendation preferences in Compute Optimizer.
+ [Rightsizing recommendation preferences](#rightsizing-preferences)
+ [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics)
+ [External metrics ingestion](#external-metrics-ingestion)
+ [Inferred workload type](#inferred-workload-type)
+ [Savings estimation mode](#savings-estimation-mode)
+ [AWS Graviton-based instance recommendations](#graviton-recommendations)

## Rightsizing recommendation preferences
<a name="rightsizing-preferences"></a>

The rightsizing recommendation preferences feature allows you to customize the settings you want Compute Optimizer to consider when generating your Amazon EC2, EC2 Auto Scaling group, Amazon EBS volumes, Amazon ECS service, and Aurora and RDS database recommendations. This feature allows you to do the following:
+ Adjust both the headroom and threshold of your CPU utilization
+ Adjust the headroom of your memory utilization
+ Configure a specific lookback period option
+ Set instance family preferences at the organization, account, or regional level 

This provides you with greater transparency on how your recommendations are generated, and the ability for you to configure resource rightsizing recommendations for higher savings and performance sensitivity. For instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer, see [Setting your rightsizing recommendation preferences](#rightsizing-preferences-process).

If you’re the account manager or the delegated administrator of an AWS Organization, you can choose the account or organization you want the rightsizing recommendation preferences to be applied to. If you’re an individual AWS account holder (not within an organization), the rightsizing recommendation preferences you set only apply to your recommendations.

**Note**  
The rightsizing preferences for CPU and memory utilization are only available for Amazon EC2 instances.
For RDS DB instances, Amazon EBS volumes, and Amazon ECS services, you can only specify lookback period preferences.

### Preferred EC2 instances
<a name="rightsizing-preferences-preferred-resources"></a>

Rightsizing recommendation preferences allows you to specify the EC2 instances you want in your recommendation output. You can define a custom instance consideration set which controls the instance types and families recommended by Compute Optimizer for migration. This preference ensures that Compute Optimizer only recommends instances that are aligned with your specific requirements. This doesn’t prevent Compute Optimizer from generating recommendations for any of your workloads.

You can customize your instance type selection based on your organizational guidelines or requirements. For example, if you have purchased Savings Plans and Reserved Instances, you can specify instances only covered by those pricing models. Or, if you only want to use instances equipped with certain processors or non-burstable instances due to your application design, you can specify those instances for your recommendation output.

This feature also gives you the option to automatically consider future variations of your chosen instance families. This ensures that your preferences are using the latest version of your preferred instance families which can provide the best price-to-performance ratio. For instructions on how to specify your preferred EC2 instances, see [Step 3: Specify preferred EC2 instances](#rightsizing-preferences-preferred-resources-process) in the next section of this user guide.

**Note**  
We recommend that you avoid limiting instance candidates too much. This can reduce your potential savings and rightsizing opportunities.

### Lookback period and metrics
<a name="rightsizing-preferences-lookback-metrics"></a>

Rightsizing recommendation preferences allows you to specify the lookback period, and the CPU and memory utilization preferences you want Compute Optimizer to use when generating your custom recommendations. For instructions on how to set your lookback period and metrics utilization, see [Step 4: Specify lookback period and metrics](#rightsizing-preferences-lookback-metrics-process) in the next section of this user guide.

**Topics**
+ [Lookback period](#rightsizing-preferences-lookback)
+ [CPU and memory utilization](#rightsizing-preferences-metrics)

#### Lookback period
<a name="rightsizing-preferences-lookback"></a>

Choose a metric analysis lookback period for your rightsizing recommendation preferences. Compute Optimizer analyzes your utilization preference settings for the number of days that you specify. We recommend that you set a lookback period that captures critical signals from your workload utilization history which can allow Compute Optimizer to identify rightsizing opportunities with higher savings and lower performance risk.

In Compute Optimizer, you can choose from the following lookback period options: 14 days (default), 32 days, or 93 days. The 14-day and 32-day lookback periods require no additional payments. If you have monthly cycles, the 32-day lookback period can capture monthly workload patterns. The 93-day lookback period requires additional payment. To use the 93-day option, you need to enable the enhanced infrastructure metrics preference. For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).

**Note**  
For RDS DB instances, you can only specify lookback period preferences.

#### CPU and memory utilization
<a name="rightsizing-preferences-metrics"></a>

The rightsizing recommendation preferences feature allows you to customize your utilization settings: CPU threshold, CPU headroom, and memory headroom so your instance recommendations meet your specific workload requirements. Depending on the utilization settings you choose, your recommendations can be tailored to increased savings opportunities, more performance headroom, or have a higher tolerance for performance risks.

##### CPU utilization threshold
<a name="rightsizing-preferences-metrics-threshold"></a>

Threshold is the percentile value that Compute Optimizer uses to process utilization data before generating recommendations. If you set a CPU threshold preference, Compute Optimizer removes the peak usage data points above this threshold. A lower percentile value removes more peak usage from the data. 

Compute Optimizer offers three options for CPU utilization threshold: P90, P95, and P99.5. By default, Compute Optimizer uses a P99.5 threshold for its rightsizing recommendations. This means that Compute Optimizer only ignores the top 0.5% of the highest utilization data points from your utilization history. The P99.5 threshold might be more suited for highly sensitive production workloads where peak utilization significantly affects application performance. If you set the utilization threshold to P90, Compute Optimizer ignores the top 10% of your highest data points from your utilization history. P90 might be a suitable threshold for workloads less sensitive to peak utilization, such as non-production environments.

##### CPU utilization headroom
<a name="rightsizing-preferences-metrics-headroom"></a>

Utilization headroom is added CPU capacity within Compute Optimizer’s recommendation to account for any future increases in CPU usage requirements. It represents the gap between the instance's current usage and its maximum capabilities. 

Compute Optimizer provides three options for CPU utilization headroom: 30%, 20%, and 0%. By default, Compute Optimizer uses a 20% headroom for its rightsizing recommendations. If you need additional capacity to account for any unexpected future increases in CPU utilization, you can set the headroom to 30%. Or, suppose that your utilization is expected to remain constant with a low chance of future increases, then you can reduce the headroom. This generates recommendations with less added CPU capacity and increased cost savings.

##### Memory utilization headroom
<a name="rightsizing-preferences-metrics-memory-headroom"></a>

Memory utilization headroom is added memory capacity within Compute Optimizer’s recommendation to account for any future increases in memory usage. It represents the gap between the instance's current usage and its maximum capabilities. Compute Optimizer provides three options for memory utilization headroom: 30%, 20%, and 10%. By default, Compute Optimizer uses a 20% headroom for its rightsizing recommendations. If you need additional capacity to account for any unexpected future increases in memory utilization, you can set the headroom to 30%. Or, suppose that your usage is expected to remain constant with a low chance of future increases, then you can reduce the headroom. This generates recommendations with less added memory capacity and increased cost savings. 

**Note**  
To receive EC2 instance recommendations that consider the memory utilization metric, you need to enable memory utilization with the CloudWatch agent. You can also configure Compute Optimizer to ingest EC2 memory utilization metrics from your preferred observability product. For more information, see [Enabling memory utilization with the CloudWatch agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent) and [ Configure external metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html#configure-external-metrics-ingestion).

##### Utilization presets
<a name="rightsizing-preferences-metrics-presets"></a>

Compute Optimizer provides four preset options for CPU and memory utilization: 
+ **Maximum savings** - CPU threshold is set to **P90**, CPU headroom is set to **0%**, and memory headroom is set to **10%**. This provides recommendations with no added CPU capacity and reserves the lowest added memory capacity for future usage growth. It also removes the top 10% of the highest data points from your CPU utilization history. As a result, this preset might generate recommendations with a higher latency or greater degradation risk. 
+ **Balanced** - CPU threshold is set to **P95**, CPU headroom is set to **30%**, and memory headroom is set to **30%**. The recommendations target CPU utilization to remain below 70% for more than 95% of the time, and target memory utilization to remain below 70%. This is suitable for most workloads and can identify more savings opportunities than the default settings. If your workloads aren't particularly sensitive to CPU or memory utilization spikes, this is a good alternative to the default settings. 
+ **Default** - Compute Optimizer uses a **P99.5** CPU threshold, a **20%** CPU headroom, and a **20%** memory headroom to generate recommendations for all EC2 instances. These settings aim to ensure that CPU utilization remains below 80% for more than 99.5% of the time, and target memory utilization to remain below 80%. This provides a very low risk of performance issues but potentially limits savings opportunities.
+ **Maximum performance** - CPU threshold is set to **P99.5**, CPU headroom is set to **30%**, and memory headroom is set to **30%**. This provides recommendations with high performance sensitivity and added capacity for future increases in CPU and memory usage.

**Note**  
Compute Optimizer might update these threshold and headroom values to reflect the latest technological updates and maintain recommendation quality. Compute Optimizer might adjust your chosen parameters based on your workload characteristics to ensure suitable instance recommendations for you.

You can use the simulated graphs in the console to get a representation of how your CPU and memory usage interacts with the threshold and headroom settings across the lookback period. The graph displays how the threshold and headroom values you set are applied to utilization data of the example workload before Compute Optimizer uses the data to generate recommendations. As you adjust the headroom and threshold, the graph updates to show how Compute Optimizer generates recommendations based on your custom preferences.

![CPU and memory usage graph](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-graph.png)


**Important**  
The data shown in the simulated graph is representative and for illustrative purposes only. The graph isn’t based on your utilization data.

### Next steps
<a name="rightsizing-preferences-next-steps"></a>

For instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer, see [Setting your rightsizing recommendation preferences](#rightsizing-preferences-process).

### Setting your rightsizing recommendation preferences
<a name="rightsizing-preferences-process"></a>

This section provides you with instructions on how to set your rightsizing recommendation preferences in AWS Compute Optimizer.

#### Procedure
<a name="rightsizing-preferences-procedure"></a>

**Topics**
+ [Step 1: Set preference level (Organizations only)](#rightsizing-preference-level)
+ [Step 2: Set regional scope](#rightsizing-preferences-regions)
+ [Step 3: Specify preferred EC2 instances](#rightsizing-preferences-preferred-resources-process)
+ [Step 4: Specify lookback period and metrics](#rightsizing-preferences-lookback-metrics-process)

##### Step 1: Set preference level (Organizations only)
<a name="rightsizing-preference-level"></a>

If you're the account manager or the delegated administrator of your organization, you can choose all the accounts in an organization or specific accounts to which you want to apply rightsizing recommendation preferences. 

**Note**  
If you’re an individual AWS account holder, skip to [Step2: Regional scope](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html#rightsizing-preferences-regions).<a name="rightsizing-step-1"></a>

**To set the preference level for your rightsizing recommendation preferences**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Rightsizing** in the navigation pane.

1. Choose the resource type you want from the **Resource type** dropdown menu.

1. In your chosen resource section, choose the ** All opted-in accounts** dropdown menu.
   + To opt in all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt in an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt in for rightsizing preferences. Then, choose **Set account level**.  
![Choose the account for rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-preference-level.png)

##### Step 2: Set regional scope
<a name="rightsizing-preferences-regions"></a>

In this step you can specify the AWS Regions where you want Compute Optimizer to apply your rightsizing recommendation preferences. For example, if you select the US East (N. Virginia) Region and US East (Ohio) Region, we only apply the preferences to those Regions.<a name="rightsizing-step-2"></a>

**To set the regional scope of your rightsizing recommendation preferences**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Rightsizing** in the navigation pane.

1. Choose the resource type you want from the **Resource type** dropdown menu.

1. On the **Rightsizing preferences** page, choose **Edit**.

1. Choose either **Any Region** or **Custom Regions** based on your requirements.

1. If you choose **Custom Regions**, select the AWS Regions where you want Compute Optimizer to apply your preferences. Then, choose **Next**.  
![Choose the Regions for rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-regions.png)

##### Step 3: Specify preferred EC2 instances
<a name="rightsizing-preferences-preferred-resources-process"></a>

Use the following procedure to specify your preferred instance types and sizes for member accounts of an organization or an individual AWS account holder.<a name="rightsizing-step-3"></a>

**To set the instances you want in your recommendation output**

1. Follow the steps outlined in [Step2: Regional scope](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html#rightsizing-preferences-regions).

1. On the **Preferred EC2 instances** page, choose either **Any instance type** (default) or **Limit to specific instance types and sizes** based on your requirements.

1. If you choose **Limit to specific instance types and sizes**, select the instance types you want in your recommendation output.
   + Use the **Search by instance families** dropdown menu. When you select any of the instance families, the list only displays the available instance types within those families that you selected.
   + Use the **Find instance types** search bar to enter the specific instance types you want.  
![Choose the preferred instances for rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-all-instances.png)

1. (Optional) To specify the sizes of each instance type, do the following:

   1. Choose the edit icon on the instance type you want.

   1. Select **X** on the instance sizes that you don’t want.

   1. Select **✔** to confirm your selections.

1. (Optional) If you don't want Compute Optimizer to automatically consider future variations of your chosen instance families, turn off **Automatically consider future variations of the instance families selected**.  
![Automatically consider future variations of the instance families toggle](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-future-instances.png)

1. Choose **Next**.

##### Step 4: Specify lookback period and metrics
<a name="rightsizing-preferences-lookback-metrics-process"></a>

Use the following procedure to specify the lookback period, and the CPU and memory utilization preferences you want Compute Optimizer to use when generating your custom recommendations.<a name="rightsizing-step-4"></a>

**To set the lookback period, and CPU and memory preferences**

1. Follow the steps outlined in [Step 4: Preferred EC2 instances](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html#preferred-resources-steps).

1. On the **Lookback period and metrics** page, choose a lookback period option based on your requirements.
   + If you want to use the 93-day lookback period (paid feature), you need to enable the enhanced infrastructure metrics preference. To do this, choose **Enable enhanced infrastructure metrics**. Then, in the prompt that appears, choose **Enable enhanced infrastructure metrics**.
   + If the enhanced infrastructure metrics preference is already enabled and you want to choose a 14-day or 32-day lookback period, you need to disable the enhanced infrastructure metrics preference. To do this, choose **Disable enhanced infrastructure metrics**. Then, in the prompt that appears, choose **Disable enhanced infrastructure metrics**.

1. Choose a utilization preset: **Max savings**, **Balanced**, **Default**, or **Max performance**.

   Alternatively, you can customize your own specific CPU and memory utilization preferences.  
![Choose from preset options](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/rightsizing-custom-configuration.png)

1. Choose **Next**.

1. On the **Review and save** page, review all the preferences you have set. Then, choose **Save preferences**.

Within 24 hours your new recommendations start to appear with the rightsizing preferences that you set.

## Enhanced infrastructure metrics
<a name="enhanced-infrastructure-metrics"></a>

Enhanced infrastructure metrics is a paid feature of Compute Optimizer that applies to Amazon EC2 instances, instances that are part of EC2 Auto Scaling groups, and Amazon RDS DB instances. This recommendation preference extends the utilization metrics analysis lookback period to up to 93 days, compared to the default 14-day period. This gives Compute Optimizer a longer history of utilization metrics data to analyze. You need to activate the enhanced infrastructure metrics preference. For more information, see [Organization, account, and resource level](#activating-enhanced-infrastructure-metrics).

### Required permissions
<a name="enhanced-infrastructure-metrics-required-permissions"></a>

You must have the appropriate permissions to activate and deactivate enhanced infrastructure metrics. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

### Organization, account, and resource level
<a name="activating-enhanced-infrastructure-metrics"></a>

You can activate enhanced infrastructure metrics using the Compute Optimizer console, AWS Command Line Interface (AWS CLI), and AWS SDKs. In the console, you can activate the feature in the following three areas, with each providing a different level of activation.
+ At the resource level, you can activate enhanced infrastructure metrics for the individual resource that you're viewing. For example, the **Instance details** page for an individual EC2 instance provides the option to activate the enhanced infrastructure metrics feature only for that EC2 instance. For more information, see [Activating enhanced infrastructure metrics at the resource level](#activating-eim-resource-level) later in this guide.
**Note**  
Resource-level preferences override account-level preferences, and account-level preferences override organization-level preferences. For an EC2 instance that is part of an EC2 Auto Scaling group, the EC2 Auto Scaling group recommendation preference overrides that of the individual instance.
+ For an individual AWS account holder, you can activate the enhanced infrastructure metrics feature for all EC2 instances in the account that meet your resource type and AWS Region criteria. EC2 instance preferences at the account level apply to standalone instances and instances that are part of EC2 Auto Scaling groups. For more information, see [Activating enhanced infrastructure metrics at the organization or account level](#activating-eim-level) later in this guide.
+ The account manager or the delegated administrator of an AWS Organization can activate the enhanced infrastructure metrics feature for all resources in all member accounts of the organization that meet your resource type and AWS Region criteria. EC2 instance preferences at the organization level apply to standalone instances and instances that are part of EC2 Auto Scaling groups in all member accounts. For more information, see [Activating enhanced infrastructure metrics at the organization or account level](#activating-eim-level) later in this guide.

After you activate the enhanced infrastructure metrics feature, Compute Optimizer applies the preference the next time recommendations are refreshed. This can take up to 24 hours. To confirm that your resource recommendations have enhanced infrastructure metrics enabled, see [Confirming the status of enhanced infrastructure metrics](#confirm-eim-status).

Compute Optimizer considers updated preferences the next time that it generates recommendations. Until then, a **pending** status is affixed to your update preference (for example, **Active-pending** or **Inactive-pending**). To confirm if your resource recommendations are taking enhanced infrastructure metrics into consideration, see [Confirming the status of enhanced infrastructure metrics](#confirm-eim-status).

#### Confirming the status of enhanced infrastructure metrics
<a name="confirm-eim-status"></a>

After you activate the enhanced infrastructure metrics recommendation preference, Compute Optimizer applies the preference the next time that recommendations are refreshed. This can take up to 24 hours. The **Effective enhanced infrastructure metrics** column in the Resource Recommendations page confirms that the recommendations listed are taking the three-month look-back period into consideration. An **Active** status confirms the recommendation listed is considering the longer look-back period. An **Inactive** status confirms that the recommendation isn't yet considering the longer look-back period.

### Next steps
<a name="eim-next-steps"></a>

For instructions on how activate or deactivate enhanced infrastructure metrics at the resource level, see [Activating enhanced infrastructure metrics at the resource level](#activating-eim-resource-level).

For instructions on how activate or deactivate enhanced infrastructure metrics at the organization or account level, see [Activating enhanced infrastructure metrics at the organization or account level](#activating-eim-level).

### Activating enhanced infrastructure metrics at the resource level
<a name="activating-eim-resource-level"></a>

This section provides you with instructions on how to activate or deactivate enhanced infrastructure metrics at the resource level. Recommendation preferences activated at the resource level apply only to the individual resource.

#### Prerequisites
<a name="eim-resource-prerequisites"></a>

Make sure that you have the appropriate permissions to activate and deactivate enhanced infrastructure metrics. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

#### Procedure
<a name="eim-resource-activate"></a>

**To activate or deactivate enhanced infrastructure metrics at the resource level**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the left navigation pane under **Recommendations** and **Rightsizing**, choose the resource type that you want to activate or deactivate enhanced infrastructure metrics.
**Note**  
For an EC2 instance that's part of an EC2 Auto Scaling group, the EC2 Auto Scaling group recommendation preference overrides the preference of the individual instance.

1. In the resource recommendations page, select the resource for which you want to activate or deactivate enhanced infrastructure metrics. Then, choose **View details**.

1. In the **Recommendation preferences** section of the **Resource details** page, choose **Enhanced infrastructure metrics**.

1. In the prompt that appears, select the **Enhanced infrastructure metrics - paid feature** checkbox. Then, choose **Save** to activate enhanced infrastructure metrics for the resource.

1. (Optional) If you want to deactivate the the enhanced infrastructure metrics, unselect the **Enhanced infrastructure metrics - paid feature** checkbox. Then, choose **Save**.
**Note**  
Saving the preference initiates metering for enhanced infrastructure metrics for the individual resource. For more information about pricing for this feature, see [Compute Optimizer pricing](https://aws.amazon.com/compute-optimizer/pricing/).

Compute Optimizer considers updated preferences the next time that it generates recommendations. Until then, a **pending** status is affixed to your updated preference (for example, **Active-pending** or **Inactive-pending**). To confirm if your resource recommendations are taking enhanced infrastructure metrics into consideration, see [Confirming the status of enhanced infrastructure metrics](#confirm-eim-status).

#### Additional resources
<a name="eim-resources"></a>
+ Troubleshooting — [Failed to get or update enhanced infrastructure metrics recommendation preferences](#accounts-eim-missing-permissions)
+ [Activating enhanced infrastructure metrics at the organization or account level](#activating-eim-level)

### Activating enhanced infrastructure metrics at the organization or account level
<a name="activating-eim-level"></a>

This section provides you with instructions on how to activate or deactivate enhanced infrastructure metrics for member accounts of an AWS Organization or an individual AWS account holder.

#### Prerequisites
<a name="eim-level-prerequisites"></a>

Make sure that you have the appropriate permissions to activate and deactivate enhanced infrastructure metrics. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

#### Procedure
<a name="eim-level-activate"></a>

**To activate or deactivate enhanced infrastructure metrics at the organization or account level**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane. Then, choose the **Enhanced infrastructure metrics** tab.

1. If you’re an individual AWS account holder, skip to step 4. 

   If you’re the account manager or delegated administrator of your organization, you can manage all member accounts or an individual member account for enhanced infrastructure metrics. 
   + To opt in all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt in an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt in for rightsizing preferences. Then, choose **Set account level**.  
![Account level preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/eim-accounts.png)

1. Choose **Edit**.

1. In the prompt that appears, choose **Add a preference**.

1. Select a **Resource type**, **Region**, and the **Activate** checkbox. Then, choose **Save**.

1. (Optional) If you want to deactivate enhanced infrastructure metrics, unselect the **Activate** checkbox. Then, choose **Save**.

Compute Optimizer considers updated preferences the next time that it generates recommendations. Until then, a **pending** status is affixed to your update preference (for example, **Active-pending** or **Inactive-pending**). To confirm that your resource recommendations are taking enhanced infrastructure metrics into consideration, see [Confirming the status of enhanced infrastructure metrics](#confirm-eim-status).

#### Additional resources
<a name="eim-level-resources"></a>
+ Troubleshooting — [Failed to get or update enhanced infrastructure metrics recommendation preferences](#accounts-eim-missing-permissions)
+ [Activating enhanced infrastructure metrics at the resource level](#activating-eim-resource-level)

## External metrics ingestion
<a name="external-metrics-ingestion"></a>

You can use the external metrics ingestion feature to configure AWS Compute Optimizer to ingest EC2 memory utilization metrics from one of the four observability products: Datadog, Dynatrace, Instana, and New Relic. When you enable external metrics ingestion, Compute Optimizer analyzes your external EC2 memory utilization metrics in addition to your CPU, disk, network, IO, and throughput data to generate EC2 rightsizing recommendations. These recommendations can provide you with additional savings and enhanced performance. For more information, see [Configuring external metrics ingestion](#configure-external-metrics-ingestion).

**Note**  
External metrics ingestion doesn't support EC2 instances that are part of EC2 Auto Scaling groups.

### Metric requirements
<a name="external-metrics-ingestion-metrics"></a>

To generate EC2 rightsizing recommendations with external memory utilization metrics, Compute Optimizer requires at least 30 consecutive hours of memory utilization metrics from your observability product. If you don’t have enough hours of external memory utilization metrics, Compute Optimizer analyzes and generates recommendations from your CloudWatch metrics until you reach the external memory metric requirements.

**Note**  
When external metrics ingestion is enabled, Compute Optimizer prioritizes your external memory utilization metrics over your CloudWatch memory data. If you opt out of external metrics ingestion, Compute Optimizer defaults back to analyze and generate recommendations based on your CloudWatch metrics.

### Organization and account level
<a name="org-account-external-metrics-ingestion"></a>

You can configure external metric ingestion at both the organization and account level. If you're a member account of an AWS organization that configured external metrics ingestion, you can opt out of this feature. For more information, see [Opting out of external metrics ingestion](#deactivate-external-metrics-ingestion).

Suppose that you're a new member of an AWS organization that already configured external metrics ingestion. Then, you must configure external metrics ingestion for your AWS account manually. For more information, see [Configuring external metrics ingestion](#configure-external-metrics-ingestion).

### Next steps
<a name="emi-next-steps"></a>

For instructions on how to configure external metric ingestion, see [Configuring external metrics ingestion](#configure-external-metrics-ingestion).

### Configuring external metrics ingestion
<a name="configure-external-metrics-ingestion"></a>

This section provides you with instructions on how to configure external metric ingestion. You can configure external metric ingestion using the Compute Optimizer console or the AWS CLI.

#### Prerequisites
<a name="emi-prerequisites"></a>

Make sure that you understand the metric requirments in order for Compute Optimizer to generate EC2 rightsizing recommendations with external memory utilization. For more information, see [Metric requirements](#external-metrics-ingestion-metrics).

#### Procedure
<a name="emi-configure"></a>

------
#### [ Console ]

**To configure external metrics ingestion**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane. Then, choose the **External metrics ingestion** tab.

1. If you’re an individual AWS account holder, skip to step 4.

   If you’re the account manager or delegated administrator of your organization, you can opt-in all member accounts or an individual member account for external metrics ingestion. 
   + To opt-in all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt-in an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt-in. Then, choose **Set account level**.  
![Choose preference level](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/external-metrics-preference.png)

1. Choose **Edit**.

1. In the prompt that appears, select your external metrics provider for EC2 instances. Then, choose **Enable**.

1. Navigate to your external metrics provider's website. To do this, choose **Configure with provider** or the external metrics source link.  
![Choose metrics source link](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/external-metrics-choose.png)

1.  Complete the configuration process on your external metrics provider’s website. 
**Important**  
If you don't complete the configuration process with your external metrics provider, Compute Optimizer can't receive your external metrics.

------
#### [ CLI ]

**To configure external metrics ingestion**

1. Open a terminal or command prompt window.

1. Call the following API operation.
   + Replace {{myRegion}} with the source AWS Region.
   + Replace {{123456789012}} with your account ID.
   + Replace {{ExternalMetricsProvider}} with your external metrics provider.

   ```
   aws compute-optimizer put-recommendation-preferences --region {{myRegion}} --resource-type=Ec2Instance --scope='{"name":"AccountId", "value":"{{123456789012}}"}' --external-metrics-preference='{"source":"{{ExternalMetricsProvider}}"}'
   ```

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Accounts** in the navigation pane.

1. In the **Organization-level preferences for external metrics ingestion** or the **Account-level preferences for external metrics ingestion** section, navigate to your external metrics provider's website. To do this, choose **Configure with provider** or the external metrics source link.  
![Choose metrics source link](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/external-metrics-choose.png)

1.  Complete the configuration process on your external metrics provider’s website. 
**Important**  
If you don't complete the configuration process with your external metrics provider, Compute Optimizer can't receive your external metrics.

------

#### Additional resources
<a name="emi-resources"></a>
+ [Opting out of external metrics ingestion](#deactivate-external-metrics-ingestion)
+ [External metrics ingestion](#external-metrics-ingestion)

### Opting out of external metrics ingestion
<a name="deactivate-external-metrics-ingestion"></a>

This section provides you with instructions on how to opt out of external metric ingestion. You can opt out external metric ingestion using the Compute Optimizer console or the AWS CLI.

#### Procedure
<a name="emi-opt-out"></a>

------
#### [ Console ]

**To opt out of external metric ingestion**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane. Then, choose the **External metrics ingestion** tab.

1. If you’re an individual AWS account holder, skip to step 4.

   If you’re the account manager or delegated administrator of your organization, you can opt out all member accounts or an individual member account for external metrics ingestion. 
   + To opt out all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt out an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt out. Then, choose **Set account level**.

1. Choose **Edit**.

1. In the prompt that appears, select **No external metrics provider**. Then, choose **Confirm**.

------
#### [ CLI ]

**To opt out of external metric ingestion**

1. Open a terminal or command prompt window.

1. Call the following API operation.
   + Replace {{myRegion}} with the source AWS Region.
   + Replace {{123456789012}} with your account ID.

   ```
   aws compute-optimizer delete-recommendation-preferences --region {{myRegion}} --resource-type=Ec2Instance --recommendation-preference-names='["ExternalMetricsPreference"]' --scope='{"name":"AccountId", "value":"{{123456789012}}"}'
   ```

------

#### Additional resources
<a name="emi-out-resources"></a>
+ [Configuring external metrics ingestion](#configure-external-metrics-ingestion)
+ [External metrics ingestion](#external-metrics-ingestion)

## Inferred workload type
<a name="inferred-workload-type"></a>

 Inferred workload type is a feature that's included with AWS Compute Optimizer that infers the applications that might be running on your AWS resources, such as EC2 instances and EC2 Auto Scaling groups. Inferred workload type does this by analyzing the attributes of your resources. These resources include resource names, tags, and configuration. Compute Optimizer currently can infer if your instances are running Amazon EMR, Apache Cassandra, Apache Hadoop, Memcached, NGINX, PostgreSQL, Redis, Kafka, or SQL Server. By inferring the applications that are running on your instances, Compute Optimizer can identify the effort to migrate your workloads from x86-based instance types to Arm-based AWS Graviton instances types. By default, the inferred workload type feature is activated. But, you can create a recommendation preference to deactivate the feature.

**Note**  
You can't infer the SQL Server application in the Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hong Kong), Europe (Milan), and Asia Pacific (Jakarta) Regions.

The inferred workload types and migration effort are listed in the **Inferred workload types** and **Migration effort** columns of the EC2 instances and EC2 Auto Scaling groups recommendations pages. For more information, see [Viewing EC2 instance recommendations](#view-ec2-recommendations) and [Viewing EC2 Auto Scaling group recommendations](#view-asg-recommendations).

### Required permissions
<a name="inferred-workload-type-required-permissions"></a>

You must have the appropriate permissions to activate the inferred workload type feature. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

### Organization and account level
<a name="activating-inferred-workload-type"></a>

By default, inferred workload type is activated. However, you can create a recommendation preference to deactivate the feature. You can deactivate inferred workload type using the Compute Optimizer console, AWS Command Line Interface (AWS CLI), or AWS SDKs. In the console, you can deactivate the feature in the following areas. Deactivating in each area provides a different level of deactivation.
+ For an individual AWS account holder, you can deactivate the inferred workload type feature for all AWS resources in the account that meet your AWS Region criteria. For more information, see [Activating inferred workload type](#activating-inferred-workload-type-steps)
+ The account manager or the delegated administrator of an AWS Organization can deactivate the inferred workload type feature for all resources in all member accounts of the organization that meet your AWS Region criteria. For more information, see [Activating inferred workload type](#activating-inferred-workload-type-steps).

After you deactivate the inferred workload type feature, Compute Optimizer stops inferring workload types the next time that recommendations are refreshed. This can take up to 24 hours to take effect.

### Next steps
<a name="inferred-next-steps"></a>

For instructions on how to activate inferred workload type, see [Activating inferred workload type](#activating-inferred-workload-type-steps).

### Activating inferred workload type
<a name="activating-inferred-workload-type-steps"></a>

This section provides you with instructions on how to activate the inferred workload type feature for member accounts of an AWS Organization or an individual AWS account holder.

#### Prerequisites
<a name="inferred-prerequisites"></a>

Make sure that you have the appropriate permissions to activate the inferred workload type feature. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

#### Procedure
<a name="inferred-activate"></a>

**To activate the inferred workload type feature for member accounts of an AWS Organization or an individual AWS account holder**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane. Then, choose the **Inferred workload type** tab.

1. If you’re an individual AWS account holder, skip to step 4. 

   If you’re the account manager or delegated administrator of your organization, you can manage all member accounts or an individual member account for inferred workload type. 
   + To opt in all member accounts, choose **All opted-in accounts** from the Preference level dropdown. 
   + To opt in an individual member account, choose **Choose account** from the Preference level dropdown. In the prompt that appears, select the account you want to opt in for rightsizing preferences. Then, choose **Set account level**.  
![Account level preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/iwt-accounts.png)

1. Choose **Edit**.

1. To deactivate the inferred workload type preference in an AWS Region, unselect the **Activate** checkbox. Then, choose **Save**.

1. (Optional) If you want to activate the inferred workload type preference in an AWS Region select the **Activate** checkbox. Then, choose **Save**..

1. (Optional) To add a new inferred workload type preference in an AWS Region, choose **Add a preference**. Then, select a **Region** and the **Activate** checkbox. Finally, choose **Save**.

#### Additional resources
<a name="inferred-resources"></a>
+ [Opting out of external metrics ingestion](#deactivate-external-metrics-ingestion)
+ [External metrics ingestion](#external-metrics-ingestion)

## Savings estimation mode
<a name="savings-estimation-mode"></a>

The savings estimation mode preference allows Compute Optimizer to analyze specific pricing discounts when generating the estimated cost savings of rightsizing recommendations. Compute Optimizer offers the savings estimation mode for the following pricing discounts per AWS resource:
+ Amazon EC2 and EC2 Auto Scaling group instances — Savings Plans and Reserved Instances pricing discounts.
+ AWS Lambda functions and Amazon ECS services — Saving Plans pricing discounts.
+ Amazon EBS volumes — other specific pricing discounts.
+ Aurora and RDS databases — Reserved Instances pricing discounts and other specific pricing discounts.

**Note**  
The savings estimation mode preference is only available for accounts within AWS Organizations that enable Cost Optimization Hub in AWS Cost Explorer. For more information, see [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the *AWS Cost Management User Guide*.

**Important**  
When you use Billing Transfer as a bill source account, the `AfterDiscounts` functionality is disabled and you can't enable it. Bill source accounts must validate rightsizing recommendations against their Reserved Instance and Savings Plans inventory to consider any unused commitment before making optimization decisions.

### Default behavior
<a name="sem-default-behavior"></a>

Compute Optimizer applies a default savings estimation mode based on your account type and Cost Optimization Hub enrollment status.

When a management account opts in to Cost Optimization Hub, all member accounts in the organization automatically default to `AfterDiscounts`. This means Compute Optimizer uses your organization's pricing discounts, such as Savings Plans and Reserved Instances, when estimating potential cost savings. If the management account opts out of Cost Optimization Hub or disables savings estimation mode in Cost Optimization Hub, member accounts without an explicit preference revert to `BeforeDiscounts`.

The following table describes the default behavior when no explicit savings estimation mode preference is set.


| Account type | Default savings estimation mode | 
| --- | --- | 
| Management account or Delegated Administrator | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Standalone account | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Member account (management account opted in to Cost Optimization Hub) | AfterDiscounts — Compute Optimizer uses pricing discounts in savings estimates. | 
| Member account (management account not opted in to Cost Optimization Hub) | BeforeDiscounts — Compute Optimizer uses On-Demand pricing only. | 

**Note**  
If you have Linked account discounts disabled in Cost Explorer, Compute Optimizer will be set to `BeforeDiscounts`.

### Overriding default preferences
<a name="sem-explicit-preferences"></a>

You can override the default behavior by explicitly setting a savings estimation mode preference using the `PutRecommendationPreferences` API or the Compute Optimizer console. An explicit preference always takes precedence over the default behavior described above.

Only the account manager or delegated administrator of your organization can activate member accounts in specific AWS Regions to receive recommendations with pricing discounts. For the account manager and the delegated administrator, the savings estimation mode preference is activated by default.

If the savings estimation mode preference isn't activated and the account doesn't qualify for a default of `AfterDiscounts`, Compute Optimizer uses the default On-Demand pricing information.

### Next steps
<a name="sem-next-steps"></a>

For instructions on how to activate or deactivate the savings estimation mode preference for member accounts, see [Activating savings estimation mode](#activate-savings-estimation-mode).

### Activating savings estimation mode
<a name="activate-savings-estimation-mode"></a>

This section provides you with instructions on how to activate or deactivate the savings estimation mode preference for member accounts within specific AWS Regions.

#### Procedure
<a name="sem-configure"></a>

**To activate savings estimation mode**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **General** in the navigation pane.

1. Choose the **Savings estimation mode** tab. Then, choose **Edit**.  
![Choose the Edit button](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/sem-edit.png)

1. In the pop-up window that appears, select the AWS Regions where you want to activate the savings estimation mode preference. Then, choose **Save**.  
![Select the AWS Regions and save](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/sem-activate-save.png)

1. (Optional) Unselect the AWS Regions where you want to deactivate the savings estimation mode preference.

When you activate the savings estimation mode preference, it can take up to 24 hours for your new recommendations with specific discounts to appear. You can view your specific discount recommendations in the **Estimated monthly savings (after discounts)** column of a given AWS resource. For more information, see [ Estimated monthly savings and savings opportunity](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-savings-calculation).

## AWS Graviton-based instance recommendations
<a name="graviton-recommendations"></a>

When viewing Amazon EC2 instance, EC2 Auto Scaling group, and Aurora and RDS database recommendations, you can view the price and performance impact of running your workload on AWS Graviton-based instances. 

**To view recommendations for AWS Graviton-based instances**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **EC2 instances**, **EC2 Auto Scaling groups**, or **RDS databases** in the navigation pane.

1. On the recommendation page of the resource that you selected, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown.

1. (Optional) Otherwise, choose **Current** to view recommendations that are based on the same CPU vendor and architecture as the current instance. 

**Note**  
The **Current price**, **Recommended price**, **Price difference**, **Price difference (%)**, and **Estimated monthly savings** columns are updated to provide a price comparison between the current instance type and the instance type of the selected CPU architecture preference. For example, if you choose **Graviton (aws-arm64)**, prices are compared between the current instance type and the recommended Graviton-based instance type.

### Additional resources
<a name="emi-resources"></a>
+ [Viewing EC2 instance recommendations](#view-ec2-recommendations)
+ [Viewing EC2 Auto Scaling group recommendations](#view-asg-recommendations)
+ [Viewing Aurora and RDS database recommendations](#view-rds-recommendations)

# Managing accounts and preferences
<a name="viewing-accounts"></a>

The Accounts page of the Compute Optimizer console lists the recommendation preferences that are activated for the account or organization, such as [enhanced infrastructure metrics]().

For the management account of an organization, the Accounts page also lists your organization's member accounts and their opt-in status to Compute Optimizer. Management accounts can [opt in](#getting-started) member accounts of the organization to AWS Compute Optimizer. When a member account is opted in, Compute Optimizer analyzes the member account's supported resources for potential optimization.

**Topics**
+ [Viewing the status of an organization's member accounts](#view-account-opt-in)
+ [Delegating an administrator account](#delegate-administrator-account)

## Viewing the status of an organization's member accounts
<a name="view-account-opt-in"></a>

This section provides you with instructions on how to view member accounts of an organization that are opted in to Compute Optimizer.

**Note**  
This option is only available to the account manager or delegated administrator of an organization who opted in member accounts to Compute Optimizer.

### Prerequisites
<a name="view-account-prerequisites"></a>

The following procedure assumes that you have already completed the [Opting in to AWS Compute Optimizer](#account-opt-in) procedure.

### Procedure
<a name="view-account-process"></a>

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Account management** in the navigation pane.

   The **Account management** page lists the member accounts of the organization and their current Compute Optimizer opt-in status. The **Opt-in status** and **Status description** columns describe the status of each account ID that are listed. To delegate an administrator account, see [Delegating an administrator account](#delegate-administrator-account).  
![Accounts page in the Compute Optimizer console](https://docs.aws.amazon.com/compute-optimizer/latest/ug/images/accounts-page.png)

### Additional resources
<a name="view-account-resources"></a>
+ [Delegating an administrator account](#delegate-administrator-account)
+ [Opting in to AWS Compute Optimizer](#account-opt-in)

## Delegating an administrator account
<a name="delegate-administrator-account"></a>

You can delegate a member account in your organization as an administrator for Compute Optimizer. A delegated administrator can access and manage Compute Optimizer recommendations. A delegated administrator can also set recommendation preferences for your entire organization without the need to access the management account. The management account controls the delegated administrator option for its organization. Each organization can only have one delegated administrator for Compute Optimizer at a time.

The delegated administrator can get and export recommendations, set recommendation preferences, set member account opt-in status, and get projected utilization metrics.

**Note**  
You can limit your delegated administrator’s access to Compute Optimizer actions by setting up appropriate IAM permissions in your IAM policy. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).
If you're the delegated administrator and you want to view org-level recommendations, see [ Policies to grant access to Compute Optimizer for a management account of an organization](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#organization-account-access).

### Procedure
<a name="da-process"></a>

Use the following procedures to register, update, or deregister an account as a delegated administrator. You can do this using the Compute Optimizer console or the AWS CLI.

#### Registering or updating a delegated administrator
<a name="register-da"></a>

------
#### [ Console ]

**To register or update an account as a delegated administrator**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Account management** in the navigation pane.

1. In the **Organization opt-in by account** section, choose the account ID that you want to add as the delegated administrator.

1. For **Delegate**, choose **Register as delegated administrator**.

1. In the prompt that appears, choose **Confirm** if you agree to the change and to add the delegated administrator.

------
#### [ CLI ]

**To register or update an account as a delegated administrator**

1. Log in as the management account of your organization.

1. Open a terminal or command prompt window.

1. Call the following API operation. Replace {{123456789012}} with your account ID.

   ```
   aws organizations register-delegated-administrator \
                                           --account-id {{123456789012}} \
                                           --service-principal compute-optimizer.amazonaws.com
   ```

------

#### Deregistering a delegated administrator
<a name="deregister-da"></a>

------
#### [ Console ]

**To deregister a member account as a delegated administrator**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Account management** in the navigation pane.

1. In the **Organization opt-in by account** section, choose the current delegated administrator's account ID.

1. For **Delegate**, choose **Deregister as delegated administrator**.

1. In the prompt that appears, choose **Confirm** if you agree to the change and to remove the delegated administrator.

------
#### [ CLI ]

**To deregister a member account as a delegated administrator**

1. Log in as the management account of your organization.

1. Open a terminal or command prompt window.

1. Call the following API operation. Replace {{123456789012}} with your account ID.

   ```
   aws organizations deregister-delegated-administrator \ 
                                           --account-id {{123456789012}} \
                                           --service-principal compute-optimizer.amazonaws.com
   ```

------

### Additional resources
<a name="da-resources"></a>
+ [Viewing the status of an organization's member accounts](#view-account-opt-in)

# Exporting AWS Compute Optimizer recommendations
<a name="exporting-recommendations"></a>

You can export your recommendations to record them over time, and share the data with others. Recommendations are exported in a CSV file, and its metadata in a JSON file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify.

**Topics**
+ [Specifying an existing S3 bucket for your recommendations export](#create-s3-bucket-policy-for-compute-optimizer)
+ [Exporting your recommendations](#exporting-your-recommendations)
+ [Viewing your export jobs](#viewing-your-exports)
+ [Exported files](#exported-files)

## Specifying an existing S3 bucket for your recommendations export
<a name="create-s3-bucket-policy-for-compute-optimizer"></a>

You can export your Compute Optimizer recommendations to an Amazon Simple Storage Service (Amazon S3) bucket. Your recommendations are exported as CSV file and the metadata is exported as a JSON file. This section provides you with instructions on how to specify an Amazon S3 bucket for your recommendation export by adding a policy to the bucket. The policy that you add allows Compute Optimizer to write recommendations export files to your Amazon S3 bucket.

### Prerequisites
<a name="s3-export-prerequisites"></a>

Make sure that you create a destination S3 bucket for your recommendations export. The S3 bucket that you specify for your recommendations export files must not be publicly accessible, and can't be configured as a [Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) bucket. As a security best practice, create a dedicated S3 bucket for Compute Optimizer export files. For more information, see [How Do I Create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket.html) in the *Amazon S3 Console User Guide*.

### Procedure
<a name="specify-an-existing-bucket-for-cloudtrail-log-delivery"></a>

After you create your S3 bucket, follow these steps to add a policy to the S3 bucket that allows Compute Optimizer to write recommendations export files to your bucket.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the bucket where you want Compute Optimizer to deliver your export files.

1. Choose **Permissions**.

1. Choose **Bucket Policy**.

1. Copy one of the following policies, and paste it into the **Bucket Policy Editor** text box.

1. Replace the following placeholder text in the policy:
   + Replace {{amzn-s3-demo-bucket}} with the name of your bucket.
   + Replace {{optionalPrefix}} with the optional object prefix.
   + Replace {{myRegion}} with the source AWS Region.
   + Replace {{myAccountID}} with the account number of the requester of the export job.

     

1. Include all three of the following statements in the policy: 

   1. The first statement (for the `GetBucketAcl` action) allows Compute Optimizer to get the access control list (ACL) of your bucket.

   1. The second statement (for the `GetBucketPolicyStatus` action) allows Compute Optimizer to get the policy status of your bucket, indicating whether the bucket is public.

   1. The third statement (for the `PutObject` action) gives Compute Optimizer full control to put the export file in your bucket.

   Your export request fails if any of these statements are missing or if the bucket name and optional object prefix in the policy don't match what you specify in your export request. Your export also fails if the account number in the policy doesn't match the account number of the requester of the export job. 
**Note**  
If the existing bucket already has one or more policies attached, add the statements for Compute Optimizer access to that policy or policies. Evaluate the resulting set of permissions to ensure that they're appropriate for the users who access the bucket. 

**Policy option 1: Using an optional prefix** 

The object prefix is an optional addition to the S3 object key that organizes your export files in your S3 bucket. If you want to specify an object prefix when you create your recommendations export, use the following policy.

------
#### [ JSON ]

****  

```
{
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketAcl",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketPolicyStatus",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{optionalPrefix}}/compute-optimizer/{{myAccountID}}/*",
                    "Condition": {"StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control",
                            "aws:SourceAccount": "{{myAccountID}}"
                        },
                        "ArnLike": {
                              "aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"
                         }
                    }
                 }
            ]
        }
```

------

**Note**  
The {{compute-optimizer/myAccountID/}} component isn’t part of the optional prefix. Compute Optimizer creates the {{optimizer/myAccountID/}} part of the bucket path for you that's added to the prefix that you specify.

**Policy option 2: No object prefix **

If you don't want to specify an object prefix, use the following policy.

------
#### [ JSON ]

****  

```
{
            "Version":"2012-10-17",		 	 	 
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketAcl",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:GetBucketPolicyStatus",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": "{{myAccountID}}"},
                        "ArnLike": {"aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"}
                    }
                },
                {
                    "Effect": "Allow",
                    "Principal": {"Service": "compute-optimizer.amazonaws.com"},
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/compute-optimizer/{{myAccountID}}/*",
                    "Condition": {"StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control",
                            "aws:SourceAccount": "{{myAccountID}}"
                        },
                        "ArnLike": {
                             "aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"
                         }
                     }
                 }
            ]
        }
```

------

### Next steps
<a name="s3-export-next-steps"></a>

For instructions on how to export your AWS Compute Optimizer recommendations, see [Exporting your recommendations](#exporting-your-recommendations).

Additionally, you can specify S3 buckets that are encrypted with either Amazon S3 customer managed keys or AWS Key Management Service (KMS) keys. For instructions on how to do this, see [Using encrypted S3 buckets for your recommendations export](#using-encrypted-s3-buckets).

### Additional resources
<a name="cloudtrail-S3-bucket-policy-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](#troubleshooting-exports)
+ [Exported files](#exported-files)
+ [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

### Using encrypted S3 buckets for your recommendations export
<a name="using-encrypted-s3-buckets"></a>

For the destination of your Compute Optimizer recommendations exports, you can specify S3 buckets that are encrypted with either Amazon S3 customer managed keys or AWS Key Management Service (KMS) keys.

#### Prerequisites
<a name="encrypted-s3-buckets-prerequisites"></a>

To use an S3 bucket with AWS KMS encryption enabled, you must create a symmetric KMS key. Symmetric KMS keys are the only KMS keys that Amazon S3 supports. For instructions, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS KMS Developer Guide*.

After you create the KMS key, apply it to the S3 bucket that you plan to use for your recommendations export. For more information, see [Enabling Amazon S3 default bucket encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) in the *Amazon Simple Storage Service User Guide*.

#### Procedure
<a name="using-encrypted-s3-buckets-procedure"></a>

Use the following procedure to grant Compute Optimizer the required permission to use your KMS key. This permission is specific for encrypting your recommendations export file when saving it to your encrypted S3 bucket.

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. In the left navigation menu, choose **Customer-managed keys**.
**Note**  
Compute Optimizer recommendation exports aren't permitted for S3 buckets encrypted with **AWS managed keys**.

1. Choose the name of the KMS key that you used to encrypt the export S3 bucket.

1. Choose the **Key policy** tab, then choose **Switch to policy view**.

1. Choose **Edit** to edit the key policy.

1. Copy one of the following policies, and paste it into the statements section of the key policy.

1. Replace the following placeholder text in the policy:
   + Replace {{myRegion}} with the source AWS Region.
   + Replace {{myAccountID}} with the account number of the export requester.

   The `GenerateDataKey` statement allows Compute Optimizer to call the AWS KMS API to obtain the data key for encrypting the recommendation files. This way, the uploaded data format can accommodate the bucket encryption setting. Otherwise, Amazon S3 rejects the export request.
**Note**  
If the existing KMS key already has one or more policies attached, add the statements for Compute Optimizer access to those policies. Evaluate the resulting set of permissions to ensure that they're appropriate for the users who access the KMS key.

Use the following policy to allow Amazon S3 bucket keys. This policy must be used regardless of whether S3 bucket keys are enabled or disabled. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) in the *Amazon Simple Storage Service User Guide*.

```
{
                "Sid": "Allow use of the key to Compute Optimizer",
                "Effect": "Allow",
                "Principal": {
                    "Service": "compute-optimizer.amazonaws.com"
                },
                "Action": [
                    "kms:GenerateDataKey",
                    "kms:Decrypt"
                ],
                "Resource": "*",
                "Condition": {"StringEquals": {
                        "aws:SourceAccount": "{{myAccountID}}"
                    },
                    "StringLike": {
                         "aws:SourceArn": "arn:aws:compute-optimizer:{{myRegion}}:{{myAccountID}}:*"
                     }
                }
            }
```

#### Next steps
<a name="encrypted-s3-buckets-next-steps"></a>

For instructions on how to export your AWS Compute Optimizer recommendations, see [Exporting your recommendations](#exporting-your-recommendations).

#### Additional resources
<a name="encrypted-s3-buckets-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](#troubleshooting-exports)
+ [Exported files](#exported-files)
+ [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## Exporting your recommendations
<a name="exporting-your-recommendations"></a>

This section provides you with instructions on how to export your AWS Compute Optimizer recommendations. Recommendations are exported in a CSV file, and its metadata in a JSON file.

### Prerequisites
<a name="exporting-your-recommendations-prerequisites"></a>
+ The following procedures assumes that you have already completed the [Specifying an existing S3 bucket for your recommendations export](#create-s3-bucket-policy-for-compute-optimizer) procedure.
+ Make sure that you understand the following restrictions that apply to exporting Compute Optimizer recommendations.
  + You can't export recommendations from multiple AWS Regions into a single Amazon S3 bucket. To export recommendations from multiple AWS Regions, you must create separate Amazon S3 buckets for your recommendations in each AWS Region. 
  + You can have only one recommendations export job in progress for each resource type, and for each AWS Region. Before creating a new export job, confirm that all previous export jobs are complete. For more information about viewing your export jobs, including those that are in progress, see [Viewing your export jobs](#viewing-your-exports).
  + Recommendations for each resource type and in each are exported in separate CSV files. You can't export recommendations from multiple resource types and Regions into a single file.
  + Large export jobs can take up to a few hours to complete. To lower your wait time, consider limiting the recommendation columns that you include in your export job. Additionally, if your account is the management account of an organization, consider limiting the number of member accounts to include in your export job.

### Procedure
<a name="exporting-your-recommendations-procedure"></a>

**To export your recommendations**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose a resource type in the navigation pane. For example, choose **EC2 instances**, **Auto Scaling groups**, **EBS volume**, **Lambda function**, or **ECS services on Fargate**.

1. On the **Recommendations** page, choose the **Action** dropdown menu, and choose **Export Recommendations**.

1. On the **Export Recommendations** page, under **Export destination settings**, specify the following:

   1. For **Region**, specify an AWS Region for your export.

   1. For **Destination S3 bucket name**, specify the name of an existing S3 bucket in the specific Region.

   1. (Optional) Choose **Add Region** to export the recommendations for another AWS Region.

   1. (Optional) Choose **Remove** next to a specific Region and S3 bucket name to remove the destination from the export job.

   1. (Optional) For **Object prefix**, specify a prefix to use in the destination S3 bucket for all of the export files. The prefix is an optional addition to the S3 object key that organizes your export files in your S3 bucket. You can specify a date prefix (for example, `2020/april`), a resource type prefix (for example, `ec2-instances`), or a combination of both (for example, `2020/april/ec2-instances`).

1. Under **Export filters**, specify the following:

   1. For **Resource type**, choose the resource type to include in your recommendations export.

   1. For **Accounts**, choose if you want to include recommendations for all member accounts of the organization. This option is available only if your account is the management account of an organization.

   1. For **CPU architecture preference**, choose **Graviton (`aws-arm64`)** to export recommendations that are based on the 64-bit ARM architecture (AWS Graviton). Otherwise, choose **Current** to export recommendations that are based on the CPU architecture of your current instances.

1. Under **Columns to include**, choose the recommendations data to include in your recommendations export. For more information about the columns to include, see [Exported files](#exported-files).

1. After confirming that the export job is configured correctly, choose **Export**. Or, to return to the **Recommendations** page without creating the export job, choose **Cancel**. If you cancel the export job configuration, the configuration is deleted.
**Note**  
If you export recommendations for multiple AWS Regions at one time, they're treated as separate export jobs. Compute Optimizer tries to start all of them at once. If an export job fails to start, the **Export Recommendations** page displays an error. Export jobs that successfully start continue to process. But, before trying to start them again, you must resolve the errors for the failed jobs.

Your recommendations export job might take up to a few hours to complete. Check the status of your export jobs by viewing the **Exports** page. For more information, see [Viewing your export jobs](#viewing-your-exports). Your recommendations export file and its associated metadata file are saved to the specified S3 bucket when the export job is complete. The following are examples of the full Amazon S3 object key for the export file and its associated metadata file. The account ID in the object keys is the account of the requester of the export job. For more information, see [Exported files](#exported-files).

```
s3://{{amzn-s3-demo-bucket}}/{{OptionalPrefix}}/compute-optimizer/{{AccountId}}/{{AWSRegion}}-{{CreatedTimestamp}}-{{UniqueJobID}}.csv
```

```
s3://{{amzn-s3-demo-bucket}}/{{OptionalPrefix}}/compute-optimizer/{{AccountId}}/{{AWSRegion}}-{{CreatedTimestamp}}-{{UniqueJobID}}-metadata.json
```

**Example:**

```
s3://{{compute-optimizer-exports}}/{{ec2-instance-recommendations}}/compute-optimizer/{{111122223333}}/{{us-west-2}}-{{2020-03-03T133027}}-{{3e496c549301c8a4dfcsdX}}.csv
```

```
s3://{{compute-optimizer-exports}}/{{ec2-instance-recommendations}}/compute-optimizer/{{111122223333}}/{{us-west-2}}-{{2020-03-03T133027}}-{{3e496c549301c8a4dfcsdX}}-metadata.json
```

### Next steps
<a name="exporting-your-recommendations-next-steps"></a>

For instructions on how to view the export jobs that you created, see [Viewing your export jobs](#viewing-your-exports).

### Additional resources
<a name="exporting-your-recommendations-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](#troubleshooting-exports)
+ [Exported files](#exported-files)
+ [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## Viewing your export jobs
<a name="viewing-your-exports"></a>

This section provides you with instructions on how to view the export jobs that you created in the last seven days.

### Prerequisites
<a name="viewing-your-exports-prerequisites"></a>

The following procedures assumes that you have already completed the [Exporting your recommendations](#exporting-your-recommendations) procedure.

### Procedure
<a name="viewing-your-exports-procedure"></a>

**To view your export jobs**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Exports** in the navigation pane.

   The **Exports** page displays the recommendation export jobs that were created in the last seven days.

   Export jobs can have one of the following statuses.
   + **Queued** - The export job didn't start yet. You can have only one recommendations export job in progress for each resource type, and for each AWS Region.
   + **In progress** - The export job started but isn't complete. Export jobs can take anywhere from a few minutes to a few hours to complete. This depends on the number of recommendations and fields that the export job includes.
   + **Complete** - The export job is complete. A link to the export CSV file in the destination Amazon S3 bucket is displayed for each complete export job under the export destination column.
   + **Failed** - The export job failed to start or complete. The message that's displayed under the failure reason column for the export job provides additional information about why the export job failed. For example, the export might have failed because the destination Amazon S3 bucket didn't have the required permissions. After resolving the issue, try to export your recommendations again. For more information, see [Troubleshooting failed export jobs](#troubleshooting-exports).

1. You can perform the following actions on the page:
   + Choose the export destination link for a completed job to access the destination S3 bucket. The export destination displays only for successful export jobs. A dash (-) displays for export jobs that are in progress or that failed.
   + Scroll right to view the failure reason for failed export jobs. Use the failure reason to determine why your export job isn't complete.

### Additional resources
<a name="viewing-your-exports-resources"></a>
+ Troubleshooting — [Troubleshooting failed export jobs](#troubleshooting-exports)
+ [Exported files](#exported-files)

## Exported files
<a name="exported-files"></a>

Recommendations are exported in a CSV file, and the metadata in a JSON file, to the Amazon S3 bucket that you specified when you created the export job.

**Topics**
+ [Recommendations file](#recommendations-file)
+ [Metadata file](#metadata-file)

### Recommendations file
<a name="recommendations-file"></a>

The recommendations file includes the recommendation data for the recommendation columns that you choose to include when you create the export job. The following tables list all of the recommendation columns that can be included in the export file for each resource type.

In the following tables, *API field name* column represents the fields that you can specify when requesting a recommendations export using the API. The *Description* column describes the data of each field, the name of the column as displayed in the Compute Optimizer console, and the name of the column as listed in the export CSV file. The recommendation data columns in the CSV file are numbered when multiple recommendations are generated for each resource. Ranked recommendation columns, in which {{<rank>}} is replaced with a ranking, correspond to each other. For example, recommendationOptions\_{{1}}\_memory, recommendationOptions\_{{1}}\_network, and recommendationOptions\_{{1}}\_vcpus correspond to each other, and are for the same recommendation.

**Note**  
By default, all export files include the following columns:  
**recommendations\_count** - The number of recommendations included in the export file.
**errorCode** - The error code for when a recommendation wasn't generated for a resource.
**errorMessage** - The error message that corresponds to the error in the errorCode column.

#### EC2 instance recommendation fields
<a name="recommendations-file-ec2"></a>


| API field name | Description | 
| --- | --- | 
| AccountId | The account ID that the current instance was created under.<br />This field is displayed as the **Account ID** column in the EC2 instances recommendations and instance details pages of the Compute Optimizer console. This field is labeled **Account ID** on the Export recommendations page of the Compute Optimizer console, and as **accountId** in the export CSV file. | 
| CurrentInstanceType | The instance type of the current instance.<br />This field is displayed as the **Current instance type** column in the EC2 instances recommendations and instance details pages of the Compute Optimizer console. This field is labeled **Current instance type** on the Export recommendations page of the Compute Optimizer console, and as **currentInstanceType** in the export CSV file. | 
| CurrentMemory | The memory of the current instance.<br />This field is displayed as the **Memory** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Current memory** on the Export recommendations page of the Compute Optimizer console, and as **current\_memory** in the export CSV file. | 
| CurrentNetwork | The network performance, or rate of data transfer, of the current instance.<br />This field is displayed as the **Network** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Current network** on the Export recommendations page of the Compute Optimizer console, and as **current\_network** in the export CSV file. | 
| CurrentOnDemandPrice | The On-Demand price of the current instance. The price listed might not reflect the actual price you pay for the instance.<br />This field is displayed as the **Current On-Demand price** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Current On-Demand price** on the Export recommendations page of the Compute Optimizer console, and as **current\_onDemandPrice** in the export CSV file. | 
| CurrentStandardOneYearNoUpfrontReservedPrice | The Reserved Instances, standard 1-year no upfront price of the current instance. The price listed might not reflect the actual price you pay for the instance.<br />This field is displayed as the **Current 1-year RI price** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Current 1-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **current\_standardOneYearNoUpfrontReservedPrice** in the export CSV file. | 
| CurrentStandardThreeYearNoUpfrontReservedPrice | The Reserved Instances, standard 3-year no upfront price of the current instance. The price listed might not reflect the actual price you pay for the instance.<br />This field is displayed as the **Current 3-year RI price** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Current 3-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **current\_standardThreeYearNoUpfrontReservedPrice** in the export CSV file. | 
| CurrentStorage | The local storage volume of the current instance.<br />This field is displayed as the **Storage** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Current storage** on the Export recommendations page of the Compute Optimizer console, and as **current\_storage** in the export CSV file. | 
| CurrentVCpus | The number of vCPUs of the current instance.<br />This field is displayed as the **vCPUs** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Current vCPUs** on the Export recommendations page of the Compute Optimizer console, and as **current\_vcpus** in the export CSV file. | 
| Finding | The finding classification for the current instance. Instances can be classified as under-provisioned, over-provisioned, or optimized. For more information, see [Instance finding classifications](#ec2-recommendations-findings).<br />This field is displayed as the **Finding** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Finding** on the Export recommendations page of the Compute Optimizer console, and as **finding** in the export CSV file. | 
| FindingReasonCodes | The finding reasons describe which specifications of the current instance were under-provisioned or over-provisioned. Specifications include CPU, memory, local disk throughput, local disk IOPS, EBS volume throughput, EBS volume IOPS, network bandwidth, or network packets-per-second.<br />This field is displayed as the **Finding reasons** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Finding reason codes** on the Export recommendations page of the Compute Optimizer console, and as **findingReasonCodes\_{{<code>}}** in the export CSV file. The {{<code>}} portion of the label identifies the instance specifications (CPU, memory, network, etc.) that are over-provisioned or under-provisioned. | 
| InstanceArn | The Amazon Resource Name (ARN) of the current instance.<br />This field is not displayed in the Compute Optimizer console. This field is labeled **Instance ARN** on the Export recommendations page of the Compute Optimizer console, and as **instanceArn** in the export CSV file. | 
| InstanceState | The state of the instance when the recommendation was generated.<br />This field is displayed as the **Recommendation instance state** column in the EC2 instance recommendation and detail pages of the Compute Optimizer console. This field is labeled **Recommendation instance state** on the Export recommendations page of the Compute Optimizer console, and labeled **instanceArn** in the export CSV file. | 
| InstanceName | The name of the current instance.<br />This field is displayed as the **Instance name** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Instance name** on the Export recommendations page of the Compute Optimizer console, and as **instanceName** in the export CSV file. | 
| LastRefreshTimestamp | The timestamp of when the instance recommendation was last refreshed.<br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Last refresh timestamp** on the Export recommendations page of the Compute Optimizer console, and as **lastRefreshTimestamp\_UTC** in the export CSV file. | 
| LookbackPeriodInDays | The number of preceding days for which Compute Optimizer analyzed metric data from the current instance to generate the recommendation.<br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Lookback period in days** on the Export recommendations page of the Compute Optimizer console, and as **lookBackPeriodInDays** in the export CSV file. | 
| RecommendationOptionsInstanceType | The instance type of the instance recommendation.<br />This field is displayed as the **Recommended instance type** column in the EC2 instances recommendations page of the Compute Optimizer console. This field is labeled **Recommendation options Instance type** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_instanceType** in the export CSV file. | 
| RecommendationOptionsMemory | The memory of the instance recommendation.<br />This field is displayed as the **Memory** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options memory** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_memory** in the export CSV file. | 
| RecommendationOptionsNetwork | The network performance or rate of data transfer of the instance recommendation.<br />This field is displayed as the **Network** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options network** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_network** in the export CSV file. | 
| RecommendationOptionsOnDemandPrice | The On-Demand price of the instance recommendation.<br />This field is displayed as the **Recommended On-Demand price** column in the EC2 instance recommendations page of the Compute Optimizer console. This field is labeled **Recommendation options On-Demand price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_onDemandPrice** in the export CSV file. | 
| RecommendationOptionsPerformanceRisk | The performance risk of the instance recommendation.<br />This field is displayed as the **Performance risk** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options performance risk** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_performanceRisk** in the export CSV file. | 
| RecommendationOptionsPlatformDifferences | The platform differences column displays the configuration differences between the current instance and each recommended instance type option. The recommended instance type might use a different CPU architecture, hypervisor, instance store, network interface, storage interface, and virtualization type.<br />This field is displayed as the **Platform differences** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options platform differences** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_platformDifferences\_{{<difference>}}** in the export CSV file. The {{<difference>}} portion of the label identifies the configuration that's different between the current instance and recommended instance type. | 
| RecommendationOptionsProjectedUtilizationMetricsCpuMaximum | The projected maximum CPU utilization metric of the instance recommendation. This value defines the maximum CPU utilization of the recommended instance type if you used the recommended instance type during the look-back period.<br />This field is displayed as an overlay on the **CPU utilization (percent)** metric graph in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics CPU maximum** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum | The projected maximum memory utilization metric of the instance recommendation. This value defines the maximum memory utilization of the recommended instance type if you used the recommended instance type during the look-back period.<br />This field is displayed as an overlay on the **Memory utilization (percent)** metric graph in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics memory maximum** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 
| RecommendationOptionsStandardOneYearNoUpfrontReservedPrice | The Reserved Instances, standard 1-year no upfront price for the instance recommendation.<br />This field is displayed as the **Recommended 1-year RI price** column in the EC2 instance recommendations page of the Compute Optimizer console. This field is labeled **Recommended options 1-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_standardOneYearNoUpfrontReservedPrice** in the export CSV file. | 
| RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice | The Reserved Instances, standard 3-year no upfront price for the instance recommendation.<br />This field is displayed as the **Recommended 3-year RI price** column in the EC2 instance recommendations page of the Compute Optimizer console. This field is labeled **Recommended options 3-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_standardThreeYearNoUpfrontReservedPrice** in the export CSV file. | 
| RecommendationOptionsStorage | The local storage volume of the instance recommendation.<br />This field is displayed as the **Storage** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options storage** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_storage** in the export CSV file. | 
| RecommendationOptionsVcpus | The vCPUs of the instance recommendation.<br />This field is displayed as the **vCPUs** column in the EC2 instance details page of the Compute Optimizer console. This field is labeled **Recommendation options vCPUs** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_vcpus** in the export CSV file. | 
| RecommendationsSourcesRecommendationSourceArn | The Amazon Resource Name (ARN) of the current resource.<br />This field is not displayed in the Compute Optimizer console. This field is labeled **Recommendation source ARN** on the Export recommendations page of the Compute Optimizer console, and as **recommendationsSources\_{{<rank>}}\_recommendationSourceArn** in the export CSV file. | 
| RecommendationsSourcesRecommendationSourceType | The resource type of the current resource (for example, instance).<br />This field is not displayed in the Compute Optimizer console. This field is labeled **Recommendation source type** on the Export recommendations page of the Compute Optimizer console, and as **recommendationsSources\_{{<rank>}}\_recommendationSourceType** in the export CSV file. | 
| UtilizationMetricsCpuMaximum | The maximum CPU utilization metric of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **CPU utilization (percent)** graph in the EC2 instance details page. This field is labeled **Utilization metrics CPU maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskReadBytesPerSecondMaximum | The maximum disk read bytes per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Disk read (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk read bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_READ\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskReadOpsPerSecondMaximum | The maximum disk read operations per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Disk read (operations/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk read operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_READ\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskWriteBytesPerSecondMaximum | The maximum disk write bytes per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Disk write (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk write bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_WRITE\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskWriteOpsPerSecondMaximum | The maximum disk write operations per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Disk write (operations/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk write operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_WRITE\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsReadBytesPerSecondMaximum | The maximum bytes read per second for volumes attached to an instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **EBS read bandwidth (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics EBS read bandwidth bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_READ\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsReadOpsPerSecondMaximum | The maximum number of read operations per second for volumes attached to an instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **EBS read operations (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics EBS read throughput operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_READ\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsWriteBytesPerSecondMaximum | The maximum bytes written per second for volumes attached to an instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **EBS write bandwidth (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics EBS write bandwidth bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_WRITE\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsWriteOpsPerSecondMaximum | The maximum number of write operations per second for volumes attached to an instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **EBS write operations (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics EBS write throughput operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_WRITE\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsMemoryMaximum | The maximum memory utilization metric of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Memory utilization (percent)** graph in the EC2 instance details page. This field is labeled **Utilization metrics memory maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkInBytesPerSecondMaximum | The maximum network in bytes per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Network in (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network in bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_IN\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkOutBytesPerSecondMaximum | The maximum network out bytes per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Network out (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network out bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_OUT\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkPacketsInPerSecondMaximum | The maximum network packets in per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Network packets in (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network packets in per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_PACKETS\_IN\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkPacketsOutPerSecondMaximum | The maximum network packets out per second of the current instance observed during the lookback period (up to 14 days).<br />This field is displayed as the **Network packets out (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network packets out per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_PACKETS\_OUT\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics | The status of the enhanced infrastructure metrics recommendation preference for the listed recommendation. An **Active** status confirms the recommendation listed is considering the longer three-month lookback period. An **Inactive** status confirms that the recommendation is not yet considering the longer lookback period. For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).<br />This field is displayed as the **Effective enhanced infrastructure metrics** column in the EC2 instance recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Effective recommendation preferences enhanced infrastructure metrics**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics**. | 
| EffectiveRecommendationPreferencesExternalMetricsSource | The status of the external metrics recommendation preference for the listed recommendation. For more information, see [ External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Effective recommendation preferences external metrics source**, and in the export CSV file format it's labeled as **EffectiveRecommendationPreferencesExternalMetricsSource**. | 
| EffectiveRecommendationPreferencesCpuVendorArchitectures | The CPU vendor and architecture for an EC2 instance recommendation.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Effective recommendation preferences CPU vendor architectures**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesCpuVendorArchitectures**. | 
| CurrentPerformanceRisk | The performance risk rating for a current instance.<br />This field is displayed as the **Current performance risk** column in the EC2 instances recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Current performance risk**, and in the export CSV file, it's labeled as **CurrentPerformanceRisk**. | 
| RecommendationOptionsSavingsOpportunityPercentage | The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for an instance.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options savings opportunity percentage**, and in the export CSV file, it's labeled as **RecommendationOptionsSavingsOpportunityPercentage**. | 
| RecommendationOptionsEstimatedMonthlySavingsCurrency | The currency of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings currency**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsCurrency**. | 
| RecommendationOptionsEstimatedMonthlySavingsValue | The value of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings value**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsValue**. | 
| EffectiveRecommendationPreferencesInferredWorkloadTypes | The status of the inferred workload type recommendation preference for the listed recommendation. For more information, see [Inferred workload type](#inferred-workload-type).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Effective recommendation preferences inferred workload types**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesInferredWorkloadTypes**. | 
| InferredWorkloadTypes | The application that might be running on the instance as detected by Compute Optimizer. For more information, see [Inferred workload types](#ec2-inferred-workload-types).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Inferred workload types**, and in the export CSV file, it's labeled as **InferredWorkloadTypes**. | 
| RecommendationOptionsMigrationEffort | The level of effort that might be required to migrate from the current instance type to the recommended instance type. For more information, see [Inferred workload types](#ec2-inferred-workload-types).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options migration effort**, and in the export CSV file, it's labeled as **RecommendationOptionsMigrationEffort**. | 

#### Auto Scaling group recommendation fields
<a name="recommendations-file-asg"></a>


| API field name | Description | 
| --- | --- | 
| AccountId | The account ID in which the current Auto Scaling group was created.<br />This field is displayed as the **Account ID** column in the Auto Scaling groups recommendations and group details pages of the Compute Optimizer console. This field is labeled **Account ID** on the Export recommendations page of the Compute Optimizer console, and as **accountId** in the export CSV file. | 
| AutoScalingGroupArn | The Amazon Resource Name (ARN) of the current Auto Scaling group.<br />This field is not displayed in the Compute Optimizer console. This field is labeled **Auto Scaling group ARN** on the Export recommendations page of the Compute Optimizer console, and as **autoScalingGroupArn** in the export CSV file. | 
| AutoScalingGroupName | The name of the Auto Scaling group.<br />This field is displayed as the **Auto Scaling group name** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Auto Scaling group name** on the Export recommendations page of the Compute Optimizer console, and as **autoScalingGroupName** in the export CSV file. | 
| CurrentConfigurationDesiredCapacity | The desired capacity of the current Auto Scaling group.<br />This field is displayed as the **Desired number of instances** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current desired capacity** on the Export recommendations page of the Compute Optimizer console, and as **currentConfiguration\_desiredCapacity** in the export CSV file. | 
| CurrentConfigurationInstanceType | The instance type of instances in the current Auto Scaling group.<br />This field is displayed as the **Current instancce type** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current instance type** on the Export recommendations page of the Compute Optimizer console, and as **currentConfiguration\_instanceType** in the export CSV file. | 
| CurrentConfigurationMaxSize | The maximum size of the current Auto Scaling group.<br />This field is displayed as the **Current maximum size** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current maximum size** on the Export recommendations page of the Compute Optimizer console, and as **currentConfiguration\_maxSize** in the export CSV file. | 
| CurrentConfigurationMinSize | The minimum size of the current Auto Scaling group.<br />This field is displayed as the **Current minimum size** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current minimum size** on the Export recommendations page of the Compute Optimizer console, and as **currentConfiguration\_minSize** in the export CSV file. | 
| CurrentMemory | The memory of instances in the current Auto Scaling group.<br />This field is displayed as the **Memory** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Current memory** on the Export recommendations page of the Compute Optimizer console, and as **current\_memory** in the export CSV file. | 
| CurrentNetwork | The network performance, or rate of data transfer, of instances in the current Auto Scaling group.<br />This field is displayed as the **Network** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Current network** on the Export recommendations page of the Compute Optimizer console, and as **current\_network** in the export CSV file. | 
| CurrentOnDemandPrice | The On-Demand price of instances in the current Auto Scaling group. The price that's listed might not reflect the actual price that you pay for the instance.<br />This field is displayed as the **Current On-Demand price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current On-Demand price** on the Export recommendations page of the Compute Optimizer console, and as **current\_onDemandPrice** in the export CSV file. | 
| CurrentStandardOneYearNoUpfrontReservedPrice | The Reserved Instances, standard 1-year no upfront price of instances in the current Auto Scaling group. The price listed might not reflect the actual price you pay for the instance.<br />This field is displayed as the **Current 1-year RI price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current 1-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **current\_standardOneYearNoUpfrontReservedPrice** in the export CSV file. | 
| CurrentStandardThreeYearNoUpfrontReservedPrice | The Reserved Instances, standard 3-year no upfront price of instances in the current Auto Scaling group. The price listed might not reflect the actual price you pay for the instance.<br />This field is displayed as the **Current 3-year RI price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Current 3-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **current\_standardThreeYearNoUpfrontReservedPrice** in the export CSV file. | 
| CurrentStorage | The local storage volume of instances in the current Auto Scaling group.<br />This field is displayed as the **Storage** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Current storage** on the Export recommendations page of the Compute Optimizer console, and as **current\_storage** in the export CSV file. | 
| CurrentVCpus | The number of vCPUs of instances in the current Auto Scaling group.<br />This field is displayed as the **vCPUs** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Current vCPUs** on the Export recommendations page of the Compute Optimizer console, and as **current\_vcpus** in the export CSV file. | 
| Finding | The finding classification for the current Auto Scaling group. Auto Scaling groups can be classified as not optimized or optimized. For more information, see [Auto Scaling group finding classifications](#asg-recommendations-findings). This field is displayed as the **Finding** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Finding** on the Export recommendations page of the Compute Optimizer console, and as **finding** in the export CSV file. | 
| LastRefreshTimestamp | The timestamp of when the Auto Scaling group recommendation was last refreshed. <br />This field is not displayed in the Compute Optimizer console. This field is labeled **Last refresh timestamp** on the Export recommendations page of the Compute Optimizer console, and as **lastRefreshTimestamp** in the export CSV file. | 
| LookbackPeriodInDays | The number of preceding days for which Compute Optimizer analyzed metric data from the current Auto Scaling group to generate the recommendation. <br />This field is not displayed in the Compute Optimizer console. This field is labeled **Lookback period in days** on the Export recommendations page of the Compute Optimizer console, and as **lookBackPeriodInDays** in the export CSV file. | 
| RecommendationOptionsConfigurationDesiredCapacity | The desired capacity of the Auto Scaling group recommendation. <br />This field is displayed as the **Desired number of instances** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options desired capacity** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_configuration\_desiredCapacity** in the export CSV file. | 
| RecommendationOptionsConfigurationInstanceType | The instance type of the Auto Scaling group recommendation. <br />This field is displayed as the **Recommendation instance type** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Recommendation options Instance type** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_configuration\_instanceType** in the export CSV file. | 
| RecommendationOptionsConfigurationMaxSize | The maximum size of the Auto Scaling group recommendation. <br />This field is displayed as the **Maximum number of instances** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options maximum size** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_configuration\_maxSize** in the export CSV file. | 
| RecommendationOptionsConfigurationMinSize | The minimum size of the Auto Scaling group recommendation. <br />This field is displayed as the **Minimum number of instances** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options minimum size** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_configuration\_minSize** in the export CSV file. | 
| RecommendationOptionsMemory | The memory of the Auto Scaling group recommendation. <br />This field is displayed as the **Memory** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options memory** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_memory** in the export CSV file. | 
| RecommendationOptionsNetwork | The network performance, or rate of data transfer, of the Auto Scaling group recommendation. <br />This field is displayed as the **Network** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options network** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_network** in the export CSV file. | 
| RecommendationOptionsOnDemandPrice | The On-Demand price of the Auto Scaling group recommendation. <br />This field is displayed as the **Recommended On-Demand price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Recommendation options On-Demand price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_onDemandPrice** in the export CSV file. | 
| RecommendationOptionsPerformanceRisk | The performance risk of the Auto Scaling group recommendation. <br />This field is displayed as the **Performance risk** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options performance risk** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_performanceRisk** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsCpuMaximum | The projected maximum CPU utilization metric of the Auto Scaling group recommendation. This value defines the maximum CPU utilization of the recommended instance type if you used the recommended instance type during the look-back period. <br />This field is displayed as an overlay on the **CPU utilization (percent)** metric graph in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics CPU maximum** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum | The projected maximum memory utilization metric of the Auto Scaling group recommendation. This value defines the maximum memory utilization of the recommended instance type if you used the recommended instance type during the look-back period. <br />This field is displayed as an overlay on the **Memory utilization (percent)** metric graph in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics memory maximum** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 
| RecommendationOptionsStandardOneYearNoUpfrontReservedPrice | The Reserved Instances, standard 1-year no upfront price for the Auto Scaling group recommendation. <br />This field is displayed as the **Recommended 1-year RI price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Recommended options 1-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_standardOneYearNoUpfrontReservedPrice** in the export CSV file. | 
| RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice | The Reserved Instances, standard 3-year no upfront price for the Auto Scaling group recommendation. <br />This field is displayed as the **Recommended 3-year RI price** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. This field is labeled **Recommended options 3-year RI price** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_standardThreeYearNoUpfrontReservedPrice** in the export CSV file. | 
| RecommendationOptionsStorage | The local storage volume of the Auto Scaling group recommendation. <br />This field is displayed as the **Storage** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options storage** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_storage** in the export CSV file. | 
| RecommendationOptionsVcpus | The vCPUs of the Auto Scaling group recommendation. <br />This field is displayed as the **vCPUs** column in the Auto Scaling group details page of the Compute Optimizer console. This field is labeled **Recommendation options vCPUs** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_vcpus** in the export CSV file. | 
| UtilizationMetricsCpuMaximum | The maximum CPU utilization metric of instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **CPU utilization (percent)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics CPU maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskReadBytesPerSecondMaximum | The maximum disk read bytes per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Disk read (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk read bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_READ\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskReadOpsPerSecondMaximum | The maximum disk read operations per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Disk read (operations/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk read operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_READ\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskWriteBytesPerSecondMaximum | The maximum disk write bytes per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Disk write (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk write bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_WRITE\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsDiskWriteOpsPerSecondMaximum | The maximum disk write operations per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Disk write (operations/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics disk write operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_DISK\_WRITE\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsReadBytesPerSecondMaximum | The maximum bytes read per second for volumes attached to instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **EBS read bandwidth (MiB/second)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics EBS read bandwidth bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_READ\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsReadOpsPerSecondMaximum | The maximum number of read operations per second for volumes attached to instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **EBS read operations (per second)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics EBS read throughput operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_READ\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsWriteBytesPerSecondMaximum | The maximum bytes written per second for volumes attached to instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **EBS write bandwidth (MiB/second)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics EBS write bandwidth bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_WRITE\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsEbsWriteOpsPerSecondMaximum | The maximum number of write operations per second for volumes attached to instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **EBS write operations (per second)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics EBS write throughput operations per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_EBS\_WRITE\_OPS\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsMemoryMaximum | The maximum memory utilization metric of instances in the current Auto Scaling group observed during the lookback period (up to 14 days). <br />This field is displayed as the **Memory utilization (percent)** graph in the Auto Scaling group details page. This field is labeled **Utilization metrics memory maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkInBytesPerSecondMaximum | The maximum network in bytes per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Network in (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network in bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_IN\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkOutBytesPerSecondMaximum | The maximum network out bytes per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Network out (MiB/second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network out bytes per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_OUT\_BYTES\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkPacketsInPerSecondMaximum | The maximum network packets in per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Network packets in (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network packets in per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_PACKETS\_IN\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsNetworkPacketsOutPerSecondMaximum | The maximum network packets out per second of the current instance observed during the lookback period (up to 14 days). <br />This field is displayed as the **Network packets out (per second)** graph in the EC2 instance details page. This field is labeled **Utilization metrics network packets out per second maximum** on the Export recommendations page of the Compute Optimizer console, and as **utilizationMetrics\_NETWORK\_PACKETS\_OUT\_PER\_SECOND\_MAXIMUM** in the export CSV file. | 
| EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics | The status of the enhanced infrastructure metrics recommendation preference for the listed recommendation. An **Active** status confirms the recommendation listed is considering the longer three-month lookback period. An **Inactive** status confirms that the recommendation isn't considering the longer lookback period. For more information, see [Enhanced infrastructure metrics](#enhanced-infrastructure-metrics).<br />This field is displayed as the **Effective enhanced infrastructure metrics** column in the Auto Scaling group recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Effective recommendation preferences enhanced infrastructure metrics**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics**. | 
| EffectiveRecommendationPreferencesCpuVendorArchitectures | The CPU vendor and architecture for an Auto Scaling group recommendation.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Effective recommendation preferences CPU vendor architectures**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesCpuVendorArchitectures**. | 
| CurrentPerformanceRisk | The performance risk rating for a current Auto Scaling group.<br />This field is displayed as the **Current performance risk** column in the Auto Scaling groups recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Current performance risk**, and in the export CSV file, it's labeled as **CurrentPerformanceRisk**. | 
| RecommendationOptionsSavingsOpportunityPercentage | The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for an Auto Scaling group.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options savings opportunity percentage**, and in the export CSV file, it's labeled as **RecommendationOptionsSavingsOpportunityPercentage**. | 
| RecommendationOptionsEstimatedMonthlySavingsCurrency | The currency of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings currency**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsCurrency**. | 
| RecommendationOptionsEstimatedMonthlySavingsValue | The value of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings value**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsValue**. | 
| EffectiveRecommendationPreferencesInferredWorkloadTypes | The status of the inferred workload type recommendation preference for the listed recommendation. For more information, see [Inferred workload type](#inferred-workload-type).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Effective recommendation preferences inferred workload types**, and in the export CSV file, it's labeled as **EffectiveRecommendationPreferencesInferredWorkloadTypes**. | 
| InferredWorkloadTypes | The application that might be running on the instances in the Auto Scaling group as detected by Compute Optimizer. For more information, see [Inferred workload types](#ec2-inferred-workload-types).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Inferred workload types**, and in the export CSV file, it's labeled as **InferredWorkloadTypes**. | 
| RecommendationOptionsMigrationEffort | The level of effort that might be required to migrate from the current instance type to the recommended instance type. For more information, see [Inferred workload types](#ec2-inferred-workload-types).<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options migration effort**, and in the export CSV file, it's labeled as **RecommendationOptionsMigrationEffort**. | 

#### EBS volume recommendation fields
<a name="recommendations-file-ebs"></a>


| API field name | Description | 
| --- | --- | 
| AccountId | The AWS account ID that the current EBS volume was created under.<br />This field is displayed as the **Account ID** column in the Amazon EBS volumes recommendations and volume details pages of the Compute Optimizer console. This field is labeled **Account ID** on the Export recommendations page of the Compute Optimizer console, and as **accountId** in the export CSV file. | 
| CurrentConfigurationVolumeBaselineIOPS | The baseline input/output operations per second (IOPS) of the current EBS volume. <br />This field is displayed as the **Current IOPS** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Current baseline IOPS** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeBaselineIOPS** in the export CSV file. | 
| CurrentConfigurationVolumeBaselineThroughput | The baseline throughput of the current EBS volume. <br />This field is displayed as the **Current throughput** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Current baseline throughput** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeBaselineThroughput** in the export CSV file. | 
| CurrentConfigurationVolumeBurstIOPS | The burst input/output operations per second (IOPS) of the current EBS volume. <br />This field is displayed as the **Burst IOPS** column in the Amazon EBS volume details page of the Compute Optimizer console. This field is labeled **Current burst IOPS** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeBurstIOPS** in the export CSV file. | 
| CurrentConfigurationVolumeBurstThroughput | The volume burst throughput of the current EBS volume. <br />This field is displayed as the **Burst throughput** column in the Amazon EBS volume details page of the Compute Optimizer console. This field is labeled **Current burst throughput** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeBurstThroughput** in the export CSV file. | 
| CurrentConfigurationVolumeSize | The current size (in GB) of the current EBS volume. <br />This field is displayed as the **Current size** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Current volume size** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeSize** in the export CSV file. | 
| CurrentConfigurationVolumeType | The volume type of the current EBS volume. <br />This field is displayed as the **Current volume type** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Current volume type** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationVolumeType** in the export CSV file. | 
| CurrentMonthlyPrice | The current monthly price of the current EBS volume.<br />This field is displayed as the **Current monthly price** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Current monthly price** on the Export recommendations page of the Compute Optimizer console, and as **currentMonthlyPrice** in the export CSV file. | 
| Finding | The finding classification for the current EBS volume. EBS volumes can be classified as optimized, or not optimized. For more information, see [EBS volume finding classifications](#ebs-recommendations-findings). <br />This field is displayed as the **Finding** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Finding** on the Export recommendations page of the Compute Optimizer console, and as **finding** in the export CSV file. | 
| LastRefreshTimestamp | The timestamp of when the EBS volume recommendation was last refreshed. <br />This field is not displayed in the Compute Optimizer console. This field is labeled **Last refresh timestamp** on the Export recommendations page of the Compute Optimizer console, and as **lastRefreshTimestamp** in the export CSV file. | 
| LookbackPeriodInDays | The number of preceding days for which Compute Optimizer analyzed metric data from the current EBS volume to generate the recommendation. <br />This field is not displayed in the Compute Optimizer console. This field is labeled **Look-back period in days** on the Export recommendations page of the Compute Optimizer console, and as **lookBackPeriodInDays** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeBaselineIOPS | The baseline input/output operations per second (IOPS) of the EBS volume recommendation. <br />This field is displayed as the **Recommended IOPS** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Recommended baseline IOPS** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeBaselineIOPS** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeBaselineThroughput | The baseline throughput of the EBS volume recommendation. <br />This field is displayed as the **Recommended throughput** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Recommended baseline throughput** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeBaselineThroughput** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeBurstIOPS | The burst input/output operations per second (IOPS) of the EBS volume recommendation. <br />This field is displayed as the **Burst IOPS** column in the Amazon EBS volume details page of the Compute Optimizer console. This field is labeled **Recommended burst IOPS** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeBurstIOPS** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeBurstThroughput | The volume burst throughput of the EBS volume recommendation. <br />This field is displayed as the **Burst throughput** column in the Amazon EBS volume details page of the Compute Optimizer console. This field is labeled **Recommended burst throughput** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeBurstThroughput** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeSize | The current size (in GB) of the EBS volume recommendation. <br />This field is displayed as the **Recommended size** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Recommended volume size** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeSize** in the export CSV file. | 
| RecommendationOptionsConfigurationVolumeType | The volume type of the EBS volume recommendation. <br />This field is displayed as the **Recommended volume type** in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Recommended volume type** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationVolumeType** in the export CSV file. | 
| RecommendationOptionsMonthlyPrice | The monthly price of the EBS volume recommendation. <br />This field is displayed as the **Recommended monthly price** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Recommended monthly price** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_MonthlyPrice** in the export CSV file. | 
| RecommendationOptionsPerformanceRisk | The performance risk of the EBS volume recommendation. <br />This field is displayed as the **Performance risk** column in the Amazon EBS volume details page of the Compute Optimizer console. This field is labeled **Performance risk** on the Export recommendations page of the Compute Optimizer console, and as **recommendationOptions\_{{<rank>}}\_performanceRisk** in the export CSV file. | 
| UtilizationMetricsVolumeReadBytesPerSecondMaximum | The maximum read bytes per second metric of the current EBS volume observed during the lookback period (up to 32 days). <br />This field is displayed as the **Read bandwidth (KiB/second)** graph in the Amazon EBS volume details page. This field is labeled **Utilization metrics EBS read bytes per second (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsVolumeReadBytesPerSecondMaximum** in the export CSV file. | 
| UtilizationMetricsVolumeReadOpsPerSecondMaximum | The maximum read operations per second metric of the current EBS volume observed during the lookback period (up to 32 days). <br />This field is displayed as the **Read operations (per second)** graph in the Amazon EBS volume details page. This field is labeled **Utilization metrics EBS read operations per second (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsVolumeReadOpsPerSecondMaximum** in the export CSV file. | 
| UtilizationMetricsVolumeWriteBytesPerSecondMaximum | The maximum write bytes per second metric of the current EBS volume observed during the lookback period (up to 32 days). <br />This field is displayed as the **Write bandwidth (KiB/second)** graph in the Amazon EBS volume details page. This field is labeled **Utilization metrics EBS write bytes per second (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsVolumeWriteBytesPerSecondMaximum** in the export CSV file. | 
| UtilizationMetricsVolumeWriteOpsPerSecondMaximum | The maximum write operations per second metric of the current EBS volume observed during the lookback period (up to 32 days). <br />This field is displayed as the **Write operations (per second)** graph in the Amazon EBS volume details page. This field is labeled **Utilization metrics EBS write operations per second (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsVolumeWriteOpsPerSecondMaximum** in the export CSV file. | 
| CurrentConfigurationRootVolume | Contains the image used to boot the current instance during launch.<br />This field is displayed as the **Root volume** column in the Amazon EBS volumes recommendations page of the Compute Optimizer console. This field is labeled **Root volume** on the Export recommendations page of the Compute Optimizer console, and labeled **rootVolume** in the export CSV file. | 
| RootVolume | Contains the image used to boot the instance during launch.<br />This field is displayed as the **Root volume** column in the Amazon EBS volumes recommendations and volume details pages of the Compute Optimizer console. This field is labeled **Root volume** on the Export recommendations page of the Compute Optimizer console, and labeled **rootVolume** in the export CSV file. | 
| VolumeArn | The Amazon Resource Name (ARN) of the current EBS volume. <br />This field is not displayed in the Compute Optimizer console. This field is labeled **EBS volume ARN** on the Export recommendations page of the Compute Optimizer console, and as **VolumeArn** in the export CSV file. | 
| CurrentPerformanceRisk | The performance risk rating for a current EBS volume.<br />This field is displayed as the **Current performance risk** column in the EBS volumes recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Current performance risk**, and in the export CSV file, it's labeled as **CurrentPerformanceRisk**. | 
| RecommendationOptionsSavingsOpportunityPercentage | The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for an EBS volume.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options savings opportunity percentage**, and in the export CSV file, it's labeled as **RecommendationOptionsSavingsOpportunityPercentage**. | 
| RecommendationOptionsEstimatedMonthlySavingsCurrency | The currency of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings currency**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsCurrency**. | 
| RecommendationOptionsEstimatedMonthlySavingsValue | The value of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings value**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsValue**. | 

#### Lambda function recommendation fields
<a name="recommendations-file-lambda"></a>


| API field name | Description | 
| --- | --- | 
| AccountId | The AWS account ID in which the current Lambda function was created.<br />This field is displayed as the **Account ID** column in the Lambda functions recommendations and function details pages of the Compute Optimizer console. This field is labeled **Account ID** on the Export recommendations page of the Compute Optimizer console, and as **accountId** in the export CSV file. | 
| CurrentConfigurationMemorySize | The amount of memory (in MB) currently configured on the current Lambda function. <br />This field is displayed as the **Current configured memory** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Current configured memory** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationMemorySize** in the export CSV file. | 
| CurrentConfigurationTimeout | The timeout time currently configured on the current Lambda function. <br />This field is displayed as the **Timeout** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Timeout** on the Export recommendations page of the Compute Optimizer console, and as **CurrentConfigurationTimeout** in the export CSV file. | 
| CurrentCostAverage | The average current cost of the current Lambda function. <br />This field is displayed listed as the **Current cost (average)** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Current cost (average)** on the Export recommendations page of the Compute Optimizer console, and as **CurrentCostAverage** in the export CSV file. | 
| CurrentCostTotal | The total current cost of the current Lambda function. <br />This field is listed as the **Current cost** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Current cost (total)** on the Export recommendations page of the Compute Optimizer console, and as **CurrentCostTotal** in the export CSV file. | 
| Finding | The finding classification for the current Lambda function. Lambda functions can be classified as under-provisioned, over-provisioned, or optimized. For more information, see [Lambda function finding classifications](#lambda-recommendations-findings). <br />This field is listed as the **Finding** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Finding** on the Export recommendations page of the Compute Optimizer console, and as **finding** in the export CSV file. | 
| FindingReasonCodes | The finding reason for the current Lambda function. Lambda functions can have a finding reason of memory under-provisioned, memory over-provisioned, insufficient data, or inconclusive. For more information, see [Lambda finding classifications](#lambda-recommendations-findings). <br />This field is listed as the **Finding reason** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Finding reason** on the Export recommendations page of the Compute Optimizer console, and as **FindingReasonCodes** in the export CSV file. | 
| FunctionArn | The Amazon Resource Name (ARN) of the current Lambda function. <br />This field is not listed in the Compute Optimizer console. This field is labeled **Function ARN** on the Export recommendations page of the Compute Optimizer console, and as **FunctionArn** in the export CSV file. | 
| FunctionVersion | The version of the current Lambda function. <br />This field is listed as the **Function version** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Function version** on the Export recommendations page of the Compute Optimizer console, and as **FunctionVersion** in the export CSV file. | 
| LastRefreshTimestamp | The timestamp of when the Lambda function recommendation was last refreshed. <br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Last refresh timestamp** on the Export recommendations page of the Compute Optimizer console, and as **lastRefreshTimestamp** in the export CSV file. | 
| LookbackPeriodInDays | The number of preceding days for which Compute Optimizer analyzed metric data from the current Lambda function to generate the recommendation. <br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Look-back period in days** on the Export recommendations page of the Compute Optimizer console, and as **lookBackPeriodInDays** in the export CSV file. | 
| NumberOfInvocations | The number of invocations for the current Lambda function during the look-back period. <br />This field is displayed as the **Invocations (count)** graph in the Lambda function details page. This field is labeled **Number of invocations** on the Export recommendations page of the Compute Optimizer console, and as **NumberOfInvocations** in the export CSV file. | 
| RecommendationOptionsConfigurationMemorySize | The amount of memory (in MB) of the Lambda function recommendation. <br />This field is listed as the **Recommended configured memory** in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Recommended configured memory** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ConfigurationMemorySize** in the export CSV file. | 
| RecommendationOptionsCostHigh | The upper range cost of the Lambda function recommendation. <br />This field is displayed as the **Recommended cost (high)** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Recommended cost (high)** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_CostHigh** in the export CSV file. | 
| RecommendationOptionsCostLow | The lower range cost of the Lambda function recommendation. <br />This field is displayed as the **Recommended cost (low)** column in the Lambda functions recommendations page of the Compute Optimizer console. This field is labeled **Recommended cost (low)** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_CostLow** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsDurationExpected | The projected duration of the Lambda function recommendation. <br />This field is listed as the **Projected duration (expected)** column in the Lambda functions details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda duration milliseconds expected** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ProjectedUtilizationMetricsDurationExpected** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound | The projected minimum amount of time that the recommended Lambda function spends processing events if the recommended Lambda function is used during the look-back period. The lower bound together with the upper bound form a range of time that the Lambda function recommendation option is projected to spend processing an event. <br />This field is listed as the **Projected duration (low)** column in the Lambda functions details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda duration milliseconds (lower bound)** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ProjectedUtilizationMetricsDurationLowerBound** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound | The projected maximum amount of time that the recommended Lambda function spends processing events if the recommended Lambda function is used during the look-back period. The lower bound together with the upper bound form a range of time that the Lambda function recommendation option is projected to spend processing an event. <br />This field is listed as the **Projected duration (high)** column in the Lambda functions details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda duration milliseconds (upper bound)** on the Export recommendations page of the Compute Optimizer console, and as **RecommendationOptions\_{{<rank>}}\_ProjectedUtilizationMetricsDurationUpperBound** in the export CSV file. | 
| UtilizationMetricsDurationAverage | The average duration metric of the current Lambda function observed during the lookback period (up to 14 days). <br />This field is displayed as the **Duration (average)** column in the Lambda function details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda duration milliseconds (average)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsDurationAverage** in the export CSV file. | 
| UtilizationMetricsDurationMaximum | The maximum duration metric of the current Lambda function observed during the lookback period (up to 14 days). <br />This field is displayed as the **Duration (maximum)** column in the Lambda function details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda duration milliseconds (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsDurationMaximum** in the export CSV file. | 
| UtilizationMetricsMemoryAverage | The average memory utilization metric of the current Lambda function observed during the lookback period (up to 14 days). <br />This field is displayed as the **Used memory (average)** column in the Lambda function details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda memory used MB (average)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsMemoryAverage** in the export CSV file. | 
| UtilizationMetricsMemoryMaximum | The maximum memory utilization metric of the current Lambda function observed during the lookback period (up to 14 days). <br />This field is displayed as the **Memory (maximum)** column in the Lambda function details page of the Compute Optimizer console. This field is labeled **Utilization metrics Lambda memory used MB (maximum)** on the Export recommendations page of the Compute Optimizer console, and as **UtilizationMetricsMemoryMaximum** in the export CSV file. | 
| CurrentPerformanceRisk | The performance risk rating for a current Lambda function.<br />This field is displayed as the **Current performance risk** column in the Lambda functions recommendations page of the Compute Optimizer console. On the Export recommendations page of the Compute Optimizer console, it's labeled as **Current performance risk**, and in the export CSV file, it's labeled as **CurrentPerformanceRisk**. | 
| RecommendationOptionsSavingsOpportunityPercentage | The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a Lambda function.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options savings opportunity percentage**, and in the export CSV file, it's labeled as **RecommendationOptionsSavingsOpportunityPercentage**. | 
| RecommendationOptionsEstimatedMonthlySavingsCurrency | The currency of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings currency**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsCurrency**. | 
| RecommendationOptionsEstimatedMonthlySavingsValue | The value of the estimated monthly savings.<br />On the Export recommendations page of the Compute Optimizer console, this field is labeled as **Recommendation options estimated monthly savings value**, and in the export CSV file, it's labeled as **RecommendationOptionsEstimatedMonthlySavingsValue**. | 

#### Recommendation fields for Amazon ECS services on Fargate
<a name="recommendations-file-ecs"></a>


| API field name | Description | 
| --- | --- | 
| AccountId | The AWS account ID that created the current Amazon ECS service on Fargate.<br />This field is displayed as the **Account ID** column in the Amazon ECS services recommendations and details pages of the Compute Optimizer console. This field is labeled **Account ID** on the Export recommendations page of the Compute Optimizer console, and labeled **accountId** in the export CSV file. | 
| ServiceArn | The Amazon Resource Name (ARN) of the current Amazon ECS service.<br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Service ARN** on the Export recommendations page of the Compute Optimizer console, and labeled **serviceArn** in the export CSV file. | 
| LookbackPeriodInDays | The number of preceding days Compute Optimizer analyzed metric data from the current service to generate the recommendation.<br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Lookback period in days** on the Export recommendations page of the Compute Optimizer console, and labeled **lookBackPeriodInDays** in the export CSV file. | 
| LastRefreshTimestamp | The timestamp of when the Amazon ECS service recommendation was last refreshed.<br />This field isn't displayed in the Compute Optimizer console. This field is labeled **Last refresh timestamp** on the Export recommendations page of the Compute Optimizer console, and labeled **lastRefreshTimestamp\_UTC** in the export CSV file. | 
| LaunchType | The capacity provider for the current Amazon ECS service.<br />This field is displayed as the **Launch type** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Launch type** on the Export recommendations page of the Compute Optimizer console, and as **launchType** in the export CSV file. | 
| CurrentPerformanceRisk | The performance risk rating for the current Amazon ECS service.<br />This field is displayed as the **Current performance risk** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Current performance risk** on the Export recommendations page of the Compute Optimizer console, and labeled **CurrentPerformanceRisk** in the export CSV file. | 
| CurrentServiceConfigurationMemory | The memory size of the current Amazon ECS service tasks.<br />This field is displayed as the **Current configured memory size** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Current configured memory** on the Export recommendations page of the Compute Optimizer console, and labeled **currentServiceConfiguration\_memory** in the export CSV file. | 
| CurrentServiceConfigurationCpu | The CPU size of the current Amazon ECS service tasks.<br />This field is displayed as the **Current configured CPU size** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Current configured CPU** on the Export recommendations page of the Compute Optimizer console, and labeled **currentServiceConfiguration\_cpu** in the export CSV file. | 
| CurrentServiceConfigurationTaskDefinitionArn | The task definition ARN of the current Amazon ECS service.<br />This field is displayed as the **Task definition name** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Task definition name** on the Export recommendations page of the Compute Optimizer console, and labeled **currentServiceConfiguration\_taskDefinitionArn** in the export CSV file. | 
| CurrentServiceConfigurationAutoScalingConfiguration | The Auto Scaling configuration of your current Amazon ECS service.<br />This field is displayed as the **Auto Scaling configuration** column in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Auto Scaling configuration** on the Export recommendations page of the Compute Optimizer console, and labeled **currentServiceConfiguration\_autoScalingConfiguration** in the export CSV file. | 
| CurrentServiceContainerConfigurations | The current container configurations of the current Amazon ECS service task.<br />This field is displayed in the **Compare current settings with recommended container size** table of the Compute Optimizer console's service details page. This field is labeled **Container configurations** on the Export recommendations page of the Compute Optimizer console. In the export CSV file, the following labels are populated:+   **currentServiceContainerConfiguration\_{{container\_number}}\_containerName**  <br />+   **currentServiceContainerConfiguration\_{{container\_number}}\_memory**  <br />+   **currentServiceContainerConfiguration\_{{container\_number}}\_memoryReservation**  <br />+   **currentServiceContainerConfiguration\_{{container\_number}}\_cpu**   | 
| UtilizationMetricsCpuMaximum | The maximum percentage of CPU capacity that's used in the Amazon ECS service.<br />This field is displayed as the **CPU utilization (percent)** graph in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Projected utilization max CPU metric** on the Export recommendations page of the Compute Optimizer console, and labeled **utilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| UtilizationMetricsMemoryMaximum | The maximum percentage of memory capacity that's used in the Amazon ECS service.<br />This field is displayed as the **Memory utilization (percent)** graph in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Projected utilization max memory metric** on the Export recommendations page of the Compute Optimizer console, and labeled **utilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 
| Findings | The finding classification for the Amazon ECS service. Amazon ECS services on Fargate can be classified as under-provisioned, over-provisioned, or optimized. For more information, see [Finding classifications](#ecs-recommendations-findings). <br />This field is displayed as the **Findings** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Findings** on the Export recommendations page of the Compute Optimizer console, and labeled **findings** in the export CSV file. | 
| FindingReasonCodes | The finding reasons column describes which specifications of the current Amazon ECS service were under-provisioned, over-provisioned, or optimized.<br />This field is displayed as the **Finding reasons** column in the Amazon ECS services recommendations page of the Compute Optimizer console. This field is labeled **Finding reason codes** on the Export recommendations page of the Compute Optimizer console, and labeled **findingReasonCodes\_{{<code>}}** in the export CSV file. The {{<code>}} portion of the label identifies the service specifications (CPU or memory) that are under-provisioned, over-provisioned, or optimized. | 
| RecommendationOptionsMemory | The memory size of the Amazon ECS service recommendation.<br />This field is displayed as the **Memory size** column in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Recommendation options memory** on the Export recommendations page of the Compute Optimizer console, and labeled **recommendationOptions\_{{<rank>}}\_memory** in the export CSV file. | 
| RecommendationOptionsCpu | The CPU size of the Amazon ECS service recommendation.<br />This field is displayed as the **CPU size** column in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Recommendation options CPU** on the Export recommendations page of the Compute Optimizer console, and labeled **recommendationOptions\_{{<rank>}}\_cpu** in the export CSV file. | 
| RecommendationOptionsSavingsOpportunityPercentage | The approximate monthly cost savings percentage after you adjust the configurations of your Amazon ECS service to Compute Optimizer's recommended configuration.<br />This field is labeled **Recommendation options savings opportunity percentage** on the Export recommendations page of the Compute Optimizer console, and labeled **RecommendationOptionsSavingsOpportunityPercentage** in the export CSV file. | 
| RecommendationOptionsEstimatedMonthlySavingsCurrency | The currency of the estimated monthly savings.<br />This field is labeled **Recommendation options estimated monthly savings currency** on the Export recommendations page of the Compute Optimizer console, and labeled **RecommendationOptionsEstimatedMonthlySavingsCurrency** in the export CSV file. | 
| RecommendationOptionsEstimatedMonthlySavingsValue | The value of the estimated monthly savings.<br />This field is labeled **Recommendation options estimated monthly savings value** on the Export recommendations page of the Compute Optimizer console, and labeled **RecommendationOptionsEstimatedMonthlySavingsValue** in the export CSV file. | 
| RecommendationOptionsContainerRecommendations | The recommedned memory and CPU size of the containers in the Amazon ECS service.<br />This field is displayed in the **Compare current settings with recommended container size** table of the Compute Optimizer console's service details page. This field is labeled **Container recommendations** on the Export recommendations page of the Compute Optimizer console. In the export CSV file, the following labels are populated:+   **recommendationOptions\_{{<index>}}\_containerName\_{{<index>}}**  <br />+   **recommendationOptions\_{{<index>}}\_containerMemory\_{{container\_number}}**  <br />+   **recommendationOptions\_{{<index>}}\_containerMemoryReservation\_{{container\_number}}**  <br />+   **recommendationOptions\_{{<index>}}\_containerCpu\_{{container\_number}}**   | 
| RecommendationOptionsProjectedUtilizationMetricsCpuMaximum | The projected maximum CPU utilization metric of the Amazon ECS service recommendation. If you used the recommended Amazon ECS service during the look-back period, this value defines the maximum CPU utilization of the recommended Amazon ECS service.<br />This field is displayed as an overlay on the **CPU utilization (percent)** metric graph in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics CPU maximum** on the Export recommendations page of the Compute Optimizer console, and labeled **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_CPU\_MAXIMUM** in the export CSV file. | 
| RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum | The projected maximum memory utilization metric of the Amazon ECS service recommendation. If you used the recommended Amazon ECS service during the look-back period, this value defines the maximum memory utilization of the recommended Amazon ECS service.<br />This field is displayed as an overlay on the **Memory utilization (percent)** metric graph in the Amazon ECS service details page of the Compute Optimizer console. This field is labeled **Recommendation options projected utilization metrics memory maximum** on the Export recommendations page of the Compute Optimizer console, and labeled **recommendationOptions\_{{<rank>}}\_projectedUtilizationMetrics\_MEMORY\_MAXIMUM** in the export CSV file. | 

#### Recommendation fields for commercial software licenses
<a name="recommendations-file-license"></a>
+ **`AccountId`**
+ **`ResourceArn`**
+ **`LookbackPeriodInDays`**
+ **`LastRefreshTimestamp`**
+ **`Findings`**
+ **`FindingReasonCodes`**
+ **`NumberOfCores`**
+ **`CurrentLicenseConfigurationInstanceType`**
+ **`CurrentLicenseConfigurationOperatingSystem`**
+ **`CurrentLicenseConfigurationLicenseName`**
+ **`CurrentLicenseConfigurationLicenseEdition`**
+ **`CurrentLicenseConfigurationLicenseModel`**
+ **`CurrentLicenseConfigurationLicenseVersion`**
+ **`MetricsSource`**
+ **`RecommendationOptionsOperatingSystem`**
+ **`RecommendationOptionsLicenseEdition`**
+ **`RecommendationOptionsLicenseModel`**
+ **`RecommendationOptionsSavingsOpportunityPercentage`**
+ **`RecommendationOptionsEstimatedMonthlySavingsCurrency`**
+ **`RecommendationOptionsEstimatedMonthlySavingsValue`**
+ **`Tags`**

#### Recommendation fields for Aurora and RDS databases
<a name="recommendations-file-rds"></a>
+ **`AccountId`**
+ **`ResourceArn`**
+ **`DBClusterIdentifier`**
+ **`Engine`**
+ **`EngineVersion`**
+ **`Idle`**
+ **`MultiAZDBInstance`**
+ **`ClusterWriter`**
+ **`PromotionTier`**
+ **`CurrentDBInstanceClass`**
+ **`CurrentStorageConfigurationStorageType`**
+ **`CurrentStorageConfigurationAllocatedStorage`**
+ **`CurrentStorageConfigurationMaxAllocatedStorage`**
+ **`CurrentStorageConfigurationIOPS`**
+ **`CurrentStorageConfigurationStorageThroughput`**
+ **`CurrentStorageEstimatedMonthlyVolumeIOPsCostVariation`**
+ **`CurrentInstanceOnDemandHourlyPrice`**
+ **`CurrentStorageOnDemandMonthlyPrice`**
+ **`CurrentStorageEstimatedClusterInstanceOnDemandMonthlyCost`**
+ **`CurrentStorageEstimatedClusterStorageOnDemandMonthlyCost`**
+ **`CurrentStorageEstimatedClusterStorageIOOnDemandMonthlyCost`**
+ **`LookbackPeriodInDays`**
+ **`UtilizationMetricsCpuMaximum`**
+ **`UtilizationMetricsMemoryMaximum`**
+ **`UtilizationMetricsEBSVolumeStorageSpaceUtilizationMaximum`**
+ **`UtilizationMetricsNetworkReceiveThroughputMaximum`**
+ **`UtilizationMetricsNetworkTransmitThroughputMaximum`**
+ **`UtilizationMetricsEBSVolumeReadIOPSMaximum`**
+ **`UtilizationMetricsEBSVolumeWriteIOPSMaximum`**
+ **`UtilizationMetricsEBSVolumeReadThroughputMaximum`**
+ **`UtilizationMetricsEBSVolumeWriteThroughputMaximum`**
+ **`UtilizationMetricsDatabaseConnectionsMaximum`**
+ **`UtilizationMetricsStorageNetworkRecieveThroughputMaximum`**
+ **`UtilizationMetricsStorageNetworkTransmitThroughputMaximum`**
+ **`UtilizationMetricsAuroraMemoryHealthStateMaximum`**
+ **`UtilizationMetricsAuroraMemoryNumDeclinedSqlMaximum`**
+ **`UtilizationMetricsAuroraMemoryNumKillConnTotalMaximum`**
+ **`UtilizationMetricsAuroraMemoryNumKillQueryTotalMaximum`**
+ **`UtilizationMetricsReadIOPSEphemeralStorageMaximum`**
+ **`UtilizationMetricsWriteIOPSEphemeralStorageMaximum`**
+ **`UtilizationMetricsVolumeBytesUsed​Average`**
+ **`UtilizationMetricsVolumeReadIOPsAverage`**
+ **`UtilizationMetricsVolumeWriteIOPs​Average`**
+ **`InstanceFinding`**
+ **`InstanceFindingReasonCodes`**
+ **`StorageFinding`**
+ **`StorageFindingReasonCodes`**
+ **`InstanceRecommendationOptionsDBInstanceClass`**
+ **`InstanceRecommendationOptionsRank`**
+ **`InstanceRecommendationOptionsPerformanceRisk`**
+ **`InstanceRecommendationOptionsProjectedUtilizationMetricsCpuMaximum`**
+ **`StorageRecommendationOptionsStorageType`**
+ **`StorageRecommendationOptionsAllocatedStorage`**
+ **`StorageRecommendationOptionsMaxAllocatedStorage`**
+ **`StorageRecommendationOptionsIOPS`**
+ **`StorageRecommendationOptionsStorageThroughput`**
+ **`StorageRecommendationOptionsRank`**
+ **`StorageRecommendationOptionsEstimatedMonthlyVolumeIOPsCostVariation`**
+ **`InstanceRecommendationOptionsInstanceOnDemandHourlyPrice`**
+ **`InstanceRecommendationOptionsSavingsOpportunityPercentage`**
+ **`InstanceRecommendationOptionsEstimatedMonthlySavingsCurrency`**
+ **`InstanceRecommendationOptionsEstimatedMonthlySavingsValue`**
+ **`InstanceRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage`**
+ **`InstanceRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts`**
+ **`InstanceRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts`**
+ **`StorageRecommendationOptionsOnDemandMonthlyPrice`**
+ **`StorageRecommendationOptionsEstimatedClusterInstanceOnDemandMonthlyCost`**
+ **`StorageRecommendationOptionsEstimatedClusterStorageOnDemandMonthlyCost`**
+ **`StorageRecommendationOptionsEstimatedClusterStorageIOOnDemandMonthlyCost`**
+ **`StorageRecommendationOptionsSavingsOpportunityPercentage`**
+ **`StorageRecommendationOptionsEstimatedMonthlySavingsCurrency`**
+ **`StorageRecommendationOptionsEstimatedMonthlySavingsValue`**
+ **`StorageRecommendationOptionsSavingsOpportunityAfterDiscountsPercentage`**
+ **`StorageRecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts`**
+ **`StorageRecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts`**
+ **`EffectiveRecommendationPreferencesCpuVendorArchitectures`**
+ **`EffectiveRecommendationPreferencesEnhancedInfrastructureMetrics`**
+ **`EffectiveRecommendationPreferencesLookBackPeriod`**
+ **`EffectiveRecommendationPreferencesSavingsEstimationMode`**
+ **`LastRefreshTimestamp`**
+ **`Tags`**

#### Recommendation fields for Idle resources
<a name="recommendations-file-idle"></a>
+ **`AccountId`**
+ **`ResourceArn`**
+ **`ResourceID`**
+ **`ResourceType`**
+ **`Findings`**
+ **`FindingReasons`**
+ **`RecommendationOptionsEstimatedMonthlySavingsCurrency`**
+ **`RecommendationOptionsEstimatedMonthlySavingsValue`**
+ **`UtilizationMetricsCpuMaximum`**
+ **`UtilizationMetricsMemoryMaximum`**
+ **`UtilizationMetricsCpuMaximum`**
+ **`UtilizationMetricsMemoryMaximum`**
+ **`UtilizationMetricsNetworkInMaximum`**
+ **`UtilizationMetricsNetworkOutMaximum`**
+ **`UtilizationMetricsEBSVolumeReadIOPSMaximum`**
+ **`UtilizationMetricsEBSVolumeWriteIOPSMaximum`**
+ **`UtilizationMetricsDatabaseConnectionsMaximum`**
+ **`LookbackPeriodInDays`**
+ **`LastRefreshTimestamp`**
+ **`Tags`**

### Metadata file
<a name="metadata-file"></a>

A metadata JSON file is output with every export job. The file includes the schema information for the associated recommendations file, such as the dialect of the data, column definitions, and column descriptions. The file is meant to help parse the export file, and describe its contents. The metadata file is saved in the same S3 bucket and prefix that you specified for the export file.

The metadata file includes the following properties for each exported column or field:
+ **Name** - The export field recommendations column name.
+ **Titles** - The user-friendly recommendations column name.
+ **Datatype** - The type of data for the column.
+ **Null** - The string to expect if the column is null.
+ **Required** - Indicates if the column data is required.

The following is an example of the information that's included in the metadata file.

```
{
  "@context": [
    "http://www.w3.org/ns/csvw"
  ],
  "url": "us-east-1-2020-05-18T001229Z-f264881a-bfb3-4676-9b14-8d1243599ebb.csv",
  "dc:title": "EC2 Instance Recommendations",
  "dialect": {
    "encoding": "utf-8",
    "lineTerminators": [
      "\n"
    ],
    "doubleQuote": true,
    "skipRows": 0,
    "header": true,
    "headerRowCount": 1,
    "delimiter": ",",
    "skipColumns": 0,
    "skipBlankRows": false,
    "trim": false
  },
  "dc:modified": {
    "@value": "2020-05-20",
    "@type": "xsd:date"
  },
  "tableSchema": {
    "columns": [
      {
        "name": "accountId",
        "titles": "Account ID",
        "datatype": "string",
        "null": "",
        "required": false
      },
      {
        "name": "instanceArn",
        "titles": "Instance Arn",
        "datatype": "string",
        "null": "",
        "required": false
      },
      {
        "name": "utilizationMetrics_CPU_MAXIMUM",
        "titles": "Cpu Maximum Utilization Metrics",
        "datatype": "double",
        "null": "",
        "required": false
      },
      {
        "name": "recommendations_count",
        "titles": "Number of recommendations",
        "datatype": "integer",
        "required": true
      },
      {
        "name": "recommendationOptions_1_instanceType",
        "titles": "Recommendation 1 Instance Type",
        "datatype": "integer",
        "null": "",
        "required": false
      },
      {
        "name": "lastRefreshTimestamp_UTC",
        "titles": "Last Resfreshed Timestamp UTC",
        "datatype": "datetime",
        "format": "yyyy-MM-dd HH:mm:ss",
        "null": "",
        "required": false
      },
      {
        "name": "errorCode",
        "titles": "Error Code",
        "datatype": "string",
        "required": true
      },
      {
        "name": "errorMessage",
        "titles": "Error Message",
        "datatype": "string",
        "required": true
      }
    ]
  }
}
```

# Troubleshooting in Compute Optimizer
<a name="troubleshooting-account-opt-in"></a>

This section covers troubleshooting why fails or errors might occur while using Compute Optimizer. The solutions provided in this section show how you can mitigate these problems.

**Topics**
+ [Failed to create service-linked role](#slr-create-failed)
+ [Failed to enable trusted access](#slr-create-failed)
+ [Failed to get or update enhanced infrastructure metrics recommendation preferences](#accounts-eim-missing-permissions)
+ [Troubleshooting failed export jobs](#troubleshooting-exports)

## Failed to create service-linked role
<a name="slr-create-failed"></a>

**Description**  
Accounts show a **Failed** opt-in status, and a description of **Failed to create service-linked role**.

**Cause**  
Compute Optimizer uses AWS Identity and Access Management (IAM) service-linked roles. These roles include all of the permissions that the service requires to call other AWS services on your behalf. You must configure permissions to allow an IAM entity (a user, group, or role) to create a service-linked role for Compute Optimizer. The user who tried to opt in to Compute Optimizer might not have the permissions required to have the service-linked role created.

**Solution**  
Add the required permissions to the user who performs the Compute Optimizer opt-in. For more information, see [Service-linked role permissions](#service-linked-role-permissions).

## Failed to enable trusted access
<a name="slr-create-failed"></a>

**Description**  
Accounts show a **Failed** opt-in status, and a description of **Failed to enable trusted access**.

**Cause**  
You can use *trusted access* to enable Compute Optimizer to perform tasks in your organization and its accounts on your behalf. For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*.When you opt in using your organization's management account and include all member accounts within the organization, trusted access for Compute Optimizer is automatically enabled in your organization account. The user who tried to opt in to Compute Optimizer might not have the permissions required to have trusted access enabled.

**Solution**  
Add the required permissions to the user who perform the Compute Optimizer opt-in. For more information, see [Permissions required to enable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_trusted_access_perms) in the *AWS Organizations User Guide*. After you add the required permissions, opt in to Compute Optimizer again using your organization's management account and include all member accounts within the organization. For more information, see [Opting in to AWS Compute Optimizer](#account-opt-in).

## Failed to get or update enhanced infrastructure metrics recommendation preferences
<a name="accounts-eim-missing-permissions"></a>

**Description**  
A banner is displayed that indicates that the Compute Optimizer console could not get or update enhanced infrastructure metrics recommendation preferences.

**Cause**  
You might not have the permissions required to view or update recommendation preferences.

**Solution**  
Add the required permissions to the user who will view or edit recommendation preferences. For more information, see [Policies to grant access to manage Compute Optimizer recommendation preferences](#enhanced-infrastructure-metrics-permissions).

## Troubleshooting failed export jobs
<a name="troubleshooting-exports"></a>

When you try to export your resource recommendations, you might experience one of the following error messages or issues. Use the information provided to try to resolve the error before trying to export your recommendations again.

**You don't have permissions to the Amazon S3 bucket specified. Confirm the permissions of your S3 bucket and try again.**  
Confirm that you have configured the required permissions on your Amazon S3 bucket. For more information, see [Specifying an existing S3 bucket for your recommendations export](#create-s3-bucket-policy-for-compute-optimizer).

**The Amazon S3 bucket specified is public. Only private S3 buckets are supported.**  
Your Amazon S3 bucket must be set to block public access. For more information, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide*.

**You created a scripted or automatic export job but there is recommendation data missing from your Amazon S3 bucket.**  
Call the `DescribeRecommendationExportJobs` API to verify the final status of the export job. If the export job failed, try to call the `Export{{Resource}}Recommendations` API again. For more information, see [ DescribeRecommendationExportJobs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DescribeRecommendationExportJobs.html) in the *AWS Compute Optimizer API Reference*.

# Security in AWS Compute Optimizer
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Compute Optimizer, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Compute Optimizer. The following topics show you how to configure Compute Optimizer to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Compute Optimizer resources. 

**Topics**
+ [Data protection in AWS Compute Optimizer](#data-protection)
+ [Compliance validation for AWS Compute Optimizer](#compliance-validation)
+ [Monitoring Compute Optimizer Automation](#monitoring-overview)

## Data protection in AWS Compute Optimizer
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Compute Optimizer. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that is stored in Amazon S3.
+ If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form fields such as a **Name** field. This includes when you work with Compute Optimizer or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Compliance validation for AWS Compute Optimizer
<a name="compliance-validation"></a>

Third-party auditors assess the security and compliance of AWS Compute Optimizer as part of multiple AWS compliance programs. AWS Compute Optimizer is FedRAMP authorized for GovCloud and is in scope for that compliance program.

For a list of AWS services in scope of specific compliance programs, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

Your compliance responsibility when using Compute Optimizer is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:
+ [Security and Compliance Quick Start Guides](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance) – These deployment guides discuss architectural considerations and provide steps for deploying security- and compliance-focused baseline environments on AWS.
+ [AWS Compliance Resources](https://aws.amazon.com/compliance/resources/) – This collection of workbooks and guides might apply to your industry and location.
+ [Evaluating Resources with Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *AWS Config Developer Guide* – The AWS Config service assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – This AWS service provides a comprehensive view of your security state within AWS that helps you check your compliance with security industry standards and best practices.

## Monitoring Compute Optimizer Automation
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Compute Optimizer Automation and your other AWS solutions. AWS provides the following monitoring tools to watch Compute Optimizer Automation, report when something is wrong, and take automatic actions when appropriate:
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

*Amazon EventBridge* is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that data to targets such as Lambda. This enables you to monitor events that happen in services, and build event-driven architectures. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).

### Logging AWS Compute Optimizer Automation API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Compute Optimizer Automation is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Compute Optimizer Automation as events. The calls captured include calls from the Compute Optimizer Automation console and code calls to the Compute Optimizer Automation API operations. Using the information collected by CloudTrail, you can determine the request that was made to Compute Optimizer Automation, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**  
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.  
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**  
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.  
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

#### Compute Optimizer Automation management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Compute Optimizer Automation logs all Compute Optimizer Automation control plane operations as management events. For a list of the AWS Compute Optimizer Automation control plane operations that Compute Optimizer Automation logs to CloudTrail, see the [AWS Compute Optimizer Automation API Reference](https://docs.aws.amazon.com/Provide API url).

#### Compute Optimizer Automation event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `ThrottlingException` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "{{ACCESS KEY ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC", 
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-06T20:23:42Z",
                "mfaAuthenticated": "false" 
            }
        }
    },
    "eventTime": "2025-11-06T19:50:12Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetEnrollmentConfiguration",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2f3a4012-f005-4d83-9042-1639a80c54ce",
    "eventID": "29ea5225-2dd6-486f-9bfe-caf7a81c3bab",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "ThrottlingException",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `AccessDenied` operation.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe",
        "accountId": "111122223333", 
        "accessKeyId": "{{ACCESS KEY ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/ReadOnly",
                "accountId": "111122223333",
                "userName": "ReadOnly"
            },
            "attributes": {
                "creationDate": "2025-11-06T19:48:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-06T19:50:12Z",
    "eventSource": "aco-automation.amazonaws.com",
    "eventName": "GetEnrollmentConfiguration",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3f4a5013-f106-4e84-9143-1740b91d55df",
    "eventID": "30fb6336-3ee7-597g-0cgf-dbg8b92d4cbc",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "AccessDenied",
    "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/ReadOnly/john-doe is not authorized to perform: aco-automation:GetEnrollmentConfiguration because no identity-based policy allows the aco-automation:GetEnrollmentConfiguration action",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `NetworkEvent` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",
        "accountId": "111122223333",
        "accessKeyId": "{{ACCESS KEY ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-07T04:23:51Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "4g5b6024-g217-5f95-0254-2851c02e66eg",
    "eventID": "41gc7447-4ff8-608h-1dgh-ech9c03e5dcd",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "GetEnrollmentConfiguration",
    "requestParameters": null,
    "responseElements": null,
    "sharedEventID": "c50cba87-2fb0-4458-b9fb-3c5e0f077718",
    "vpcEndpointId": "AWS Internal",
    "vpcEndpointAccountId": "AWS Internal",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }

}
```

The following example shows a CloudTrail event that demonstrates the `GetEnrollmentConfiguration` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "{{ACCESS KEY ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROASVBPKTAKQR6L32DI4",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "5h6c7135-h328-6ga6-1365-3962d13f77fh",
    "eventID": "52hd8558-5gg9-719i-2ehi-fdi0d14f6ede",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "GetEnrollmentConfiguration",
    "requestParameters": null,
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAccounts` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
       "type": "AssumedRole",        
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",
        "accountId": "111122223333",
        "accessKeyId": "{{ACCESS KEY ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",
                "accountId": "111122223333",
                "userName": "AuthenticatedComputeOptimizerRole"
            },
            "attributes": {
                "creationDate": "2025-11-05T20:23:45Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-05T20:23:48Z",
    "eventSource": "aco-automation.amazonaws.com",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "6i7d8246-i439-7hb7-2476-4073e24g88gi",
    "eventID": "63ie9669-6hh0-820j-3fij-gej1e25g7fef",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "eventName": "ListAccounts",
    "requestParameters": {
        "maxResults": 50
    },
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `GetAutomationRule` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "abcdef01234567890;",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"       
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
"eventTime": "2025-11-06T04:24:01Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "GetAutomationRule",    
    "awsRegion": "us-east-1",    
        "eventTime": "2025-11-06T04:24:01Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "GetAutomationRule",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "7j8e9357-j540-8ic8-3587-5184f35h99hj",
    "eventID": "74jf0770-7ii1-931k-4gjk-hfk2f36h8gfg",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "ruleArn": "arn:aws:compute-optimizer::123456789012:automation-rule/123AbcdEfGHi1jkL"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRules` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:21:59Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationRules",    
    "awsRegion": "us-east-1",
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "8k9f0468-k651-9jd9-4698-6295g46i00ik",
    "eventID": "85kg1881-8jj2-042l-5hkl-igl3g47i9hgh",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListTagsForResource` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:33:00Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListTagsForResource",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "9l0g1579-l762-0ke0-5709-7306h57j11jl",
    "eventID": "96lh2992-9kk3-153m-6ilm-jhm4h58j0ihi",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/035Pcy46SStQHe0A"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRulePreview` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T19:31:22Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T19:31:28Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationRulePreview",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "0m1h2680-m873-1lf1-6810-8417i68k22km",
    "eventID": "07mi3003-0ll4-264n-7jmn-kin5i69k1jij",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true, Note: Please be mindful when interacting with displayed links.
"recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "ruleType": "OrganizationRule",        
        "organizationScope": {            
            "accountIds": [                
                "535045952558"            
            ]        
        },        
        "recommendedActionTypes": [            
            "UpgradeEbsVolumeType",            
            "SnapshotAndDeleteUnattachedEbsVolume"        
        ],        
        "criteria": {            
            "region": [{                
                "comparison": "StringEquals",                
                "values": [                    
                    "us-east-1",                    
                    "us-west-2"                
                ]            
            }],            
            "resourceArn": [{                
                "comparison": "StringLike",                
                "values": [                    
                    "vol-"                
                ]            
            }]        
        },        
        "maxResults": 100    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationRulePreviewSummaries` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T19:14:49Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T19:21:52Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationRulePreviewSummaries",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "1n2i3791-n984-2mg2-7921-9528j79l33ln",
    "eventID": "18nj4114-1mm5-375o-8kon-ljo6j70l2kjk",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",

    "requestParameters": {        
        "ruleType": "AccountRule",        
        "recommendedActionTypes": [            
            "SnapshotAndDeleteUnattachedEbsVolume"        
        ]    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListRecommendedActions` operation.

```
{      
    "eventVersion": "1.11",      
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {          
            "sessionIssuer": {            
                "type": "Role",            
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",            
                "arn": "arn:aws:iam::111122223333:role/Admin",            
                "accountId": "111122223333",            
                "userName": "Admin"          
            },          
            "attributes": {            
                "creationDate": "2025-11-06T04:19:48Z",            
                "mfaAuthenticated": "false"          
            }        
        }      
    },      
    "eventTime": "2025-11-06T04:27:20Z",      
    "eventSource": "aco-automation.amazonaws.com",      
    "eventName": "ListRecommendedActions",      
    "awsRegion": "us-east-1",      
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2o3j4802-o095-3nh3-8032-0639k80m44mo",
    "eventID": "29ok5225-2nn6-486p-9lop-mqp7k81m3lkl",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,      
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListRecommendedActionSummaries` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:31:59Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListRecommendedActionSummaries",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3p4k5913-p106-4oi4-9143-1740l91n55np",
    "eventID": "30pl6336-3oo7-597q-0dqp-nrq8l92n4mlm",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `GetAutomationEvent` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:25:20Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "GetAutomationEvent",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "4q5l6024-q217-5pj5-0254-2851m02o66oq",
    "eventID": "41qm7447-4pp8-608r-1eqr-srr9m03o5nmn",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "eventId": "a12cb3d4e5f67g0h"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEvents` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:24:32Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationEvents",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "5r6m7135-r328-6qk6-1365-3962n13p77pr",
    "eventID": "52rn8558-5qq9-719s-2frs-tss0n14p6ono",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEventSteps` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:28:10Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationEventSteps",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "6s7n8246-s439-7rl7-2476-4073o24q88qs",
    "eventID": "63so9669-6rr0-820t-3gst-utt1o25q7pop",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "eventId": "a12cb3d4e5f67g0h"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `ListAutomationEventSummaries` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:31:03Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "ListAutomationEventSummaries",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "7t8o9357-t540-8sm8-3587-5184p35r99rt",
    "eventID": "74tp0770-7ss1-931u-4htu-vuv2p36r8qpq",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": null,    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `UpdateEnrollmentConfiguration` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",                
                "accountId": "111122223333",                
                "userName": "{{USER NAME}}"            
            },            
            "attributes": {                
                "creationDate": "2025-11-05T20:23:45Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-05T20:23:46Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "UpdateEnrollmentConfiguration",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "8u9p0468-u651-9tn9-4698-6295q46s00su",
    "eventID": "85uq1881-8tt2-042v-5iuv-wvw3q47s9rqr",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "status": "Active",        
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"    
    },    
    "responseElements": {        
        "status": "Active",        
        "lastUpdatedTimestamp": "Nov 5, 2025, 8:23:46 PM"    
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `AssociateAccounts` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",                
                "accountId": "111122223333",                
                "userName": "AuthenticatedComputeOptimizerRole"            
            },            
            "attributes": {                
                "creationDate": "2025-11-05T20:23:45Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-05T20:23:45Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "AssociateAccounts",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "9v0q1579-v762-0uo0-5709-7306r57t11tv",
    "eventID": "96vr2992-9uu3-153w-6jvw-xwx4r58t0srs",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "errorCode": "InvalidParameterValueException",    
    "errorMessage": "The management account or the delegated administrator doesn't have access to this member account.",    
    "requestParameters": {        
        "accountIds": [            
            "123456789012"        
        ],        
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `DisassociateAccounts` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
       "principalId": "EXAMPLEAIZ5FYRFP3POCC:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/AuthenticatedComputeOptimizerRole/MettleCanary",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/AuthenticatedComputeOptimizerRole",                
                "accountId": "111122223333",                
                "userName": "AuthenticatedComputeOptimizerRole"            
            },            
            "attributes": {                
                "creationDate": "2025-11-05T20:23:45Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-05T20:23:47Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "DisassociateAccounts",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "0w1r2680-w873-1vp1-6810-8417s68u22uw",
    "eventID": "07ws3003-0vv4-264x-7kwx-yxy5s69u1tst",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "accountIds": [            
            "123456789012"        
        ],        
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"    
    },    
    "responseElements": {        
        "accountIds": [            
            "123456789012"        
        ]    
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `CreateAutomationRule` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/*****************",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:20:00Z",
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "CreateAutomationRule",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "1x2s3791-x984-2wq2-7921-9528t79v33vx",
    "eventID": "18xt4114-1ww5-375y-8lxy-zyz6t70v2utu",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "ruleName": "TestRule",  
        "ruleType": "AccountRule",        
        "recommendedActionTypes": [            
            "SnapshotAndDeleteUnattachedEbsVolume"        
        ],        
        "schedule": {            
            "scheduleExpression": "cron(0 2 * * ? *)",            
            "scheduleExpressionTimezone": "UTC",            
            "executionWindowInMinutes": 60        
        },        
        "status": "Active",        
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"    
    },    
    "responseElements": {        
        "ruleArn": "arn:aws:compute-optimizer::123456789012:automation-rule/123AbcdEfGHi1jkL",        
        "ruleId": "123AbcdEfGHi1jkL",        
        "name": "SourabTestRule",        
        "ruleType": "AccountRule",        
        "ruleRevision": 1,        
        "priority": "1E-30",        
        "recommendedActionTypes": [            
            "SnapshotAndDeleteUnattachedEbsVolume"        
        ],        
         "criteria": {            
            "region": [{                
                "comparison": "StringEquals",                
                "values": [                    
                    "us-east-1"                
                ]            
            }]        
        },        
        "clientToken": "12345abc-12ab-1234-123a-EXAMPLEeb16b"    
    },    
    "responseElements": {        
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:111122223333:automation-rule/123AbcdEfGHi1jkL"    
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `DeleteAutomationRule` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:26:15Z",
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "DeleteAutomationRule",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "3z4u5913-z106-4ys4-9143-1740v91x55xz",
    "eventID": "30zv6336-3yy7-597a-0eza-b1b8v92x4wvw",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "ruleArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL"    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `UpdateAutomationRule` operation.

```
        {    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:22:30Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "UpdateAutomationRule",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/ComputeOptimizerAutomation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x8664 lang/java#17.0.16 md/OpenJDK64-BitServerVM#17.0.16+8-LTS md/vendor#Amazon.comInc. md/enUS md/kotlin/1.9.21-release-633 exec-env/AWSLambdajava17 m/E,N,i",
    "requestID": "2y3t4802-y095-3xr3-8032-0639u80w44wy",
    "eventID": "29yu5225-2xx6-486z-9myz-a0a7u81w3vuv",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:123456789012:automation-rule/123AbcdEfGHi1jkL",        
        "status": "Active"    
    },    
    "responseElements": {        
        "ruleArn": "arn:aws:compute-optimizer:us-east-1:123456789012:automation-rule/123AbcdEfGHi1jkL"    
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLSAES128GCMSHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `TagResource` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:22:37Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "TagResource",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "6c7x8246-c439-7bv7-2476-4073y24a99ab",
    "eventID": "63cy9669-6bb0-820d-3hcd-ede2y25a7bab",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL",        
        "ruleRevision": 1,        
        "tags": [{            
            "key": "test",            
            "value": "cloudtrail"        
        }]    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `UntagResource` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}"        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:33:09Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "UntagResource",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "7d8y9357-d540-8cw8-3587-5184z35b00bc",
    "eventID": "74dz0770-7cc1-931e-4ide-fef3z36b8cbc",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "resourceArn": "arn:aws:compute-optimizer::111122223333:automation-rule/123AbcdEfGHi1jkL",        
        "ruleRevision": 2,        
        "tagKeys": [            
            "test"        
        ]    
    },    
    "responseElements": null,
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `RollbackAutomationEvent` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}",        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T19:31:22Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T19:35:59Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "RollbackAutomationEvent",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "8e9z0468-e651-9dx9-4698-6295a46c11cd",
    "eventID": "85ea1881-8dd2-042f-5jef-gfg4a47c9dcd",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "eventId": "a52cb5d6d8f24e0c",        
        "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"    
    },    
    "responseElements": {        
        "eventId": "a52cb5d6d8f24e0c",        
        "eventStatus": "ROLLBACK_READY"    
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

The following example shows a CloudTrail event that demonstrates the `StartAutomationEvent` operation.

```
{    
    "eventVersion": "1.11",    
    "userIdentity": {        
        "type": "AssumedRole",        
        "principalId": "abcdef01234567890;:john-doe",        
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/john-doe",        
        "accountId": "111122223333",        
        "accessKeyId": "{{ACCESS KEY ID}}"        
        "sessionContext": {            
            "sessionIssuer": {                
                "type": "Role",                
                "principalId": "EXAMPLEAIZ5FYRFP3POCC",                
                "arn": "arn:aws:iam::111122223333:role/Admin",                
                "accountId": "111122223333",                
                "userName": "Admin"            
            },            
            "attributes": {                
                "creationDate": "2025-11-06T04:19:48Z",                
                "mfaAuthenticated": "false"            
            }        
        }    
    },    
    "eventTime": "2025-11-06T04:27:46Z",    
    "eventSource": "aco-automation.amazonaws.com",    
    "eventName": "StartAutomationEvent",    
    "awsRegion": "us-east-1",    
    "sourceIPAddress": "100.26.200.255",
    "userAgent": "canary-generated aws-sdk-java/2.35.11 md/io#sync md/http#Apache md/internal ua/2.1 api/Compute_Optimizer_Automation#2.37.x-SNAPSHOT os/Linux#5.10.244-267.968.amzn2.x86_64 lang/java#17.0.16 md/OpenJDK_64-Bit_Server_VM#17.0.16+8-LTS md/vendor#Amazon.com_Inc. md/en_US md/kotlin/1.9.21-release-633 exec-env/AWS_Lambda_java17 m/E,N,i",
    "requestID": "9f0a1579-f762-0ey0-5709-7306b57d22de",
    "eventID": "96fb2992-9ee3-153g-6kfg-hgh5b58d0ede",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "requestParameters": {        
        "recommendedActionId": "aa112223333a4444"    
    },    
    "responseElements": {        
            "recommendedActionId": "aa112223333a4444",            
            "eventId": "a12cb3d4e5f67g0h",            
            "status": "READY"        
        }
    },
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "aco-automation-gamma.us-east-1.amazonaws.com"
    }
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.

# FAQs on supported protocols
<a name="cbor-faq"></a>

 The AWS Compute Optimizer and AWS Cost Optimization Hub services are adding SDK support for the [ Smithy RPC v2 CBOR ](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html) protocol in addition to the existing [AWS JSON ](https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html) protocol. The Smithy RPC v2 CBOR protocol is more performant than AWS JSON for most workloads. AWS SDKs will prioritize the protocol that is the most performant for each language. 

## What are the AWS JSON and Smithy RPC v2 CBOR protocols, and how do they differ?
<a name="cbor-faq-what-are-protocols"></a>

 A wire protocol acts as a mediator between a client and the service. The AWS SDK handles the serialization (converting an object to the wire format) and deserialization (converting the wire format back to an object) between the client and server transparently for both protocols. 

 **AWS JSON** - JSON is one of the most widely used and accepted data formats for communication between systems. This service uses AWS JSON as a medium to communicate between an AWS SDK client and the server. An HTTP request for a service API operation accepts input in the form of JSON, the operation is executed, and the response is returned to the SDK client in the form of JSON. 

 **Smithy RPC v2 CBOR** - Smithy RPC v2 CBOR (Concise Binary Object Representation) is a protocol developed by Amazon for more efficient data transmission. It is a data format designed to keep message sizes compact and to allow the format to evolve without requiring version negotiation between systems. The key difference from AWS JSON is that AWS JSON uses human-readable text (like `{"name": "John"}`), while Smithy RPC v2 CBOR uses a binary format (sequences of 1s and 0s). This binary approach creates smaller data packages that travel faster over the network and reduces serialization time since computers process binary data directly. 

## How do I get started with the Smithy RPC v2 CBOR protocol?
<a name="cbor-faq-getting-started"></a>

 To get started, use the latest AWS SDK/CLI version to use the Smithy RPC v2 CBOR protocol for this service. The SDK will automatically use the Smithy RPC v2 CBOR protocol when available. Upgrade your AWS SDK to the specified version or any subsequent version. 

 Starting 2026-04-16, the following AWS SDKs will use the Smithy RPC v2 CBOR protocol, while the other SDKs will continue using the AWS JSON protocol: 
+ AWS SDK for C\+\+
+ AWS SDK for Go V2
+ AWS SDK for Java 2.x
+ AWS SDK for .NET v4
+ AWS Tools for PowerShell v5
+ AWS SDK for Swift
+ AWS SDK for Kotlin

## What are the risks of enabling the Smithy RPC v2 CBOR protocol?
<a name="cbor-faq-risks"></a>

 The added support of Smithy RPC v2 CBOR in the SDKs is expected to be fully transparent and effortless for customers. However, if you are using a custom implementation of the AWS SDK, or a combination of custom clients and the AWS SDK, that depends on AWS JSON-specific serialization behavior, it may be incompatible with the Smithy RPC v2 CBOR protocol. 

## What if my solution does not support Smithy RPC v2 CBOR?
<a name="cbor-faq-compatibility-issues"></a>

 To use the AWS JSON protocol, downgrade your SDK to a version released before 2026-04-16. 

## What AWS Regions support the Smithy RPC v2 CBOR protocol?
<a name="cbor-faq-region-support"></a>

 The Smithy RPC v2 CBOR protocol is supported in all [AWS Regions ](https://docs.aws.amazon.com/general/latest/gr/rande.html) where this service is available. 

## What latency improvements can I expect when upgrading to SDK versions that support Smithy RPC v2 CBOR?
<a name="cbor-faq-performance-improvements"></a>

 Smithy RPC v2 CBOR provides up to 13% lower latency and up to 15% reduction in payload size compared to AWS JSON. The binary encoding eliminates the overhead of JSON text parsing and string escaping, which reduces both network transfer time and serialization cost. 

## Will the AWS JSON protocol be deprecated?
<a name="cbor-faq-json-deprecation"></a>

 AWS JSON protocol will continue to be supported through older versions of SDKs. Also, some language-specific SDKs will continue using AWS JSON as it is more performant than Smithy RPC v2 CBOR due to the available JSON implementation for the language being faster than its CBOR implementation. 

## Where can I find more information about Smithy RPC v2 CBOR?
<a name="cbor-faq-more-information"></a>

 You can find more information about the AWS JSON protocol at [AWS JSON 1.0 protocol ](https://smithy.io/2.0/aws/protocols/aws-json-1_0-protocol.html) and [AWS JSON 1.1 protocol ](https://smithy.io/2.0/aws/protocols/aws-json-1_1-protocol.html) in the Smithy documentation, and about Smithy RPC v2 CBOR at [ Smithy RPC v2 CBOR protocol ](https://smithy.io/2.0/additional-specs/protocols/smithy-rpc-v2.html) in the Smithy documentation. 

# Document history for AWS Compute Optimizer
<a name="doc-history"></a>

The following table describes the documentation for this release of AWS Compute Optimizer.
+ **API version:** 2019-11-30
+ **Latest documentation update:** August 15, 2022

The following table describes the documentation for this release of Compute Optimizer.

| Change | Description | Date | 
| --- |--- |--- |
| [Compute Optimizer supports new EC2 and RDS instance types](#doc-history) | Compute Optimizer now provides recommendations for new Amazon EC2 instance types, including C8a, C8gb, C8i, C8i-flex, C8id, M8a, M8azn, M8gb, M8gn, M8id, R8a, R8gb, R8gn, R8id, x8i, and i7i instances. Compute Optimizer also added support for new RDS DB instance classes, including db.m7i, db.m8g, db.r8g, db.x1, and db.z1d. For more information, see [Supported resources](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html). | April 20, 2026 | 
| [Added FAQ page for supported protocols](#doc-history) | Added a new FAQ page with answers to common questions about the AWS JSON and Smithy RPC v2 CBOR wire protocols. For more information, see [ FAQs on supported protocols](https://docs.aws.amazon.com/compute-optimizer/latest/ug/cbor-faq.html). | April 16, 2026 | 
| [Updated documentation for managed policies](#doc-history) | Added new `ComputeOptimizerAutomationServiceRolePolicy` policy. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | November 19, 2025 | 
| [Compute Optimizer supports new EC2 instance types](#doc-history) | Compute Optimizer now provides recommendations for 99 new Amazon EC2 instance types, including the C8gn, I8ge, M8i, and R8i instances. For more information, see [Supported Amazon EC2 instance types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-ec2-instances). | September 26, 2025 | 
| [Expanded the features of EC2 Auto Scaling group recommendations](#doc-history) | Compute Optimizer now generates rightsizing recommendations for EC2 Auto Scaling groups that use G or P instance types, and idle recommendations for groups with scaling policies and groups that have been scaled down to a single instance. For more information, see [Supported Amazon EC2 Auto Scaling groups ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-asg). | June 16, 2025 | 
| [Amazon Aurora I/O-Optimized recommendations](#doc-history) | Compute Optimizer now provides Aurora I/O-Optimized recommendations for Amazon Aurora DB cluster storage. For more information, see [Viewing Aurora and RDS database recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations). | June 2, 2025 | 
| [Compute Optimizer supports new EC2 instance types](#doc-history) | Compute Optimizer now provides recommendations for 57 new Amazon EC2 instance types, including the I7ie, I8g, High Memory (U-1), P5e, and G6e instances. For more information, see [Supported Amazon EC2 instance types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-ec2-instances). | April 10, 2025 | 
| [Updated an AWS managed policy for AWS Compute Optimizer](#doc-history) | The `ComputeOptimizerServiceRolePolicy` AWS managed policy for AWS Compute Optimizer was updated. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | January 9, 2025 | 
| [Expanded the features of EC2 Auto Scaling group recommendations](#doc-history) | Compute Optimizer now generates recommendations for EC2 Auto Scaling groups that have mixed instance types, scaling policies, or both. For more information, see [Viewing EC2 Auto Scaling group recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-asg-recommendations). | January 9, 2025 | 
| [Updated AWS managed policies for AWS Compute Optimizer](#doc-history) | The `ComputeOptimizerReadOnlyAccess` AWS managed policy for AWS Compute Optimizer was updated. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | November 20, 2024 | 
| [Compute Optimizer generates recommendations for idle resources](#doc-history) | Compute Optimizer helps you identify idle resources that can be deleted or stopped to reduce your AWS cloud costs. For more information, see [ Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations). | November 20, 2024 | 
| [Amazon RDS DB recommendations](#doc-history) | Compute Optimizer now generates Amazon RDS rightsizing recommendations for Aurora MySQL and Aurora PostgreSQL database engines. For more information, see [Viewing RDS DB instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations). | November 20, 2024 | 
| [Compute Optimizer supports new EC2 instance types](#doc-history) | Compute Optimizer now provides recommendations for 80 new Amazon EC2 instance types, including the P4, P5, G5, G6, C7i-flex, C8g, R8g, and X8g instances. For more information, see [Supported Amazon EC2 instance types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-ec2-instances). | October 1, 2024 | 
| [Updated AWS managed policies for AWS Compute Optimizer](#doc-history) | The `ComputeOptimizerReadOnlyAccess` AWS managed policy for AWS Compute Optimizer was updated. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | June 20, 2024 | 
| [Amazon RDS DB recommendations](#doc-history) | Compute Optimizer now generates Amazon RDS rightsizing recommendations for Amazon RDS MySQL and Amazon RDS PostgreSQL database engines. For more information, see [Viewing RDS DB instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations). | June 20, 2024 | 
| [Compute Optimizer supports rightsizing preferences for memory ultilization headroom](#doc-history) | In Compute Optimizer you can use rightsizing recommendation preferences to customize the memory ultilization headroom settings you want Compute Optimizer to use when generating your Amazon EC2 instance recommendations. For more information, see [Rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences). | March 28, 2024 | 
| [Compute Optimizer supports new EC2 instance types](#doc-history) | Compute Optimizer now provides recommendations for 51 new EC2 instance types, including the C7i, r7i, r8g, x2idn, x2iedn, and hpc7a instances. For more information, see [Supported Amazon EC2 instance types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html#supported-ec2-instances). | March 25, 2024 | 
| [Compute Optimizer supports rigthsizing recommendation preferences](#doc-history) | In Compute Optimizer you can use rightsizing recommendation preferences to customize the settings you want Compute Optimizer to consider when generating your Amazon EC2 and Auto Scaling group instance recommendations. For more information, see [Rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences). | November 26, 2023 | 
| [Compute Optimizer supports new specific discounts for rigthsizing recommendations](#doc-history) | You can now allow Compute Optimizer to analyze specific pricing discounts, such Saving Plans and Reserved Instances, when generating the estimated cost savings of rightsizing recommendations. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode). | November 26, 2023 | 
| [Compute Optimizer supports new EC2 instance types and EBS volumes](#doc-history) | Compute Optimizer now provides recommendations for 153 new Amazon EC2 instance types, including the M7a, M7i, M7i-flex, M6a, C7gn, R6a, R7g, X2iezn, I4g, I4i, Hpc7g, and Hpc6id instances. Additionally, Compute Optimizer now supports Provisioned IOPS Amazon EBS volumes that are attached to multiple EC2 instances. For more information, see [AWS resources supported by Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html). | September 28, 2023 | 
| [Compute Optimizer supports GPU-based EC2 instances](#doc-history) | Compute Optimizer now provides rightsizing recommendations for G4dn and P3 instances. For more information, see [ Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances). | September 5, 2023 | 
| [Compute Optimizer generates commercial software license recommendations](#doc-history) | Compute Optimizer now generates license recommendations for commercial software that run on Amazon EC2. Compute Optimizer only provides Microsoft SQL Server license recommendations. For more information, see [ Viewing commercial software license recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-license-recommendations). | August 28, 2023 | 
| [Compute Optimizer supports tag filtering and inferred workload type filtering for recommendations](#doc-history) | In Compute Optimizer you can now filter your EC2 instance, EBS volume, Lambda function, and ECS service recommendations by tag key and tag value. Additionally, you can also filter your EC2 recommendations by inferred workload types. For more information, see [ Viewing EC2 instances recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-view-recommendations). | May 1, 2023 | 
| [Compute Optimizer supports new EC2 instance types](#doc-history) | Compute Optimizer now provides recommendations for 61 new EC2 instance types, including the C6in, R6in, R6idn, M6in, and M6idn instances. For more information, see [ Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances). | March 30, 2023 | 
| [Compute Optimizer supports new EBS volume types](#doc-history) | Compute Optimizer now provides recommendations for three new EBS volume types: HDD `st1` and `sc1`, and Provisioned IOPS SSD `io2 Block Express`. For more information, see [ Amazon EBS volume requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements). | March 30, 2023 | 
| [Compute Optimizer supports EC2 suspension workloads](#doc-history) | Compute Optimizer can now combine utilization data from intermittent workloads to generate EC2 recommendations. For more information, see [ Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances). | March 30, 2023 | 
| [Compute Optimizer generates recommendations for Amazon ECS services on Fargate](#doc-history) | Compute Optimizer now generates recommendations for Amazon ECS services on Fargate. For more information, see [ Recommendations for Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ecs-recommendations). | December 22, 2022 | 
| [Compute Optimizer launches external metrics ingestion feature](#doc-history) | Compute Optimizer can now ingest and analyze external EC2 memory utilization metrics from one of the four observability products to generate EC2 rightsizing recommendations that provide you with additional savings and enhanced performance. For more information, see [ External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion). | November 28, 2022 | 
| [Compute Optimizer supports new EC2 instance types and Windows memory metrics](#doc-history) | Compute Optimizer now provides recommendations for 37 new EC2 instance types, including the M6i.metal, C6i.metal, C7g, and Hpc6a instances. Additionally, Compute Optimizer now prioritizes the `Available MBytes` memory metric when generating recommendations for EC2 Windows instances. For more information, see [Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances) and [ EC2 instance metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#ec2-metrics-analyzed). | October 7, 2022 | 
| [Compute Optimizer launches delegated administrator feature](#doc-history) | Now in Compute Optimizer, an organization's management accounts can delegate a member account as an administrator for their organization. The delegated administrator can access and manage Compute Optimizer recommendations. The delegated administrator can also set recommendation preferences for your entire organization without the need to access the management account. For more information, see [Delegate an administrator account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/delegate-administrator-account.html). | August 15, 2022 | 
| [Updated an AWS managed policy for AWS Compute Optimizer](#doc-history) | The `ComputeOptimizerServiceRolePolicy` AWS managed policy for AWS Compute Optimizer was updated. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | July 25, 2022 | 
| [Compute Optimizer adds support for additional Amazon EC2 instance types](#doc-history) | Compute Optimizer now supports C5d, C6a, C6i, I2, Im4gn, Is4gen, M5ad, M6a, M6i, and R6i Amazon EC2 instance types. These instance types are supported in all the AWS Regions where both these instance types and Compute Optimizer are available. This update doesn't apply in the China (Beijing) and China (Ningxia) Regions. For more information, see [Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances). | April 7, 2022 | 
| [Workload-aware recommendations and migration effort now available](#doc-history) | With the new inferred workload types feature, Compute Optimizer can infer the applications that might be running on your resources. Examples include EC2 instances and Auto Scaling groups. Compute Optimizer does this by analyzing the attributes of your resources, such as resource names, tags, and configuration. By inferring applications, Compute Optimizer can generate recommendations that take your applications into account. It can also identify the level of effort required to migrate from the current instance type to the recommended instance type. For more information, see [Inferred workload type](https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-type.html). | January 10, 2022 | 
| [View savings and performance improvement opportunities for your resources, and activate enhanced infrastructure metrics](#doc-history) | Identify your biggest cost and performance improvement opportunities in the new **Savings opportunity** and **Performance improvement opportunity** sections of the dashboard. For more information, see [Viewing the AWS Compute Optimizer dashboard](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-dashboard.html). You can also now extend the metrics analysis lookback period for EC2 instances and Auto Scaling groups up to three months. By default, the lookback period is 14 days. To do this, activate enhanced infrastructure metrics. The enhanced infrastructure metrics feature is a paid feature of Compute Optimizer. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html). | November 29, 2021 | 
| [Updated AWS managed policies for AWS Compute Optimizer](#doc-history) | The `ComputeOptimizerServiceRolePolicy` and `ComputeOptimizerReadOnlyAccess` AWS managed policies for AWS Compute Optimizer were updated. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | November 29, 2021 | 
| [AWS Graviton based instance recommendations](#doc-history) | Compute Optimizer now provides the price and performance impact for running your workload on AWS Graviton based instances. For more information, see [AWS Graviton-based instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-graviton-recommendations). If your account is your organization's management account, you can now also view the member accounts of an organization that are opted in to Compute Optimizer. For more information, see [Viewing the accounts opted in to AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-accounts.html). | August 26, 2021 | 
| [Amazon EC2 instance recommendations enhancements](#doc-history) | Compute Optimizer now supports a wider range of Amazon EC2 instance types. Compute Optimizer evaluates a wider range of instance metrics to generate recommendations and provides finding instance recommendations reasons. Compute Optimizer also describes the platform differences between the current instance and the recommended instance type. For more information, see [Amazon EC2 instance requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances), [EC2 instance metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#ec2-metrics-analyzed), [Finding reasons](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-finding-reasons), and [Platform differences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html#ec2-platform-differences). | May 24, 2021 | 
| [Recommendations export for Amazon EBS volumes and Lambda functions](#doc-history) | You can now export recommendations for Amazon EBS volumes and Lambda functions to Amazon S3. For more information, see [Exporting recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html). | May 18, 2021 | 
| [Adding documentation for AWS managed policies](#doc-history) | Compute Optimizer now tracks changes for its AWS managed policies. For more information, see [AWS managed policies for AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/managed-policies.html). | May 18, 2021 | 
| [AWS Lambda function recommendations](#doc-history) | Compute Optimizer now generates recommendations for AWS Lambda functions. For more information, see [Viewing AWS Lambda function recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html). | December 23, 2020 | 
| [Amazon EBS volume recommendations](#doc-history) | Compute Optimizer now generates recommendations for Amazon Elastic Block Store (Amazon EBS) volumes. For more information, see [Viewing EBS volume recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html). | December 3, 2020 | 
| [Amazon EBS metrics and encrypted S3 buckets](#doc-history) | Compute Optimizer now analyzes the read/write operations per second (ops), and the read/write bytes per second (Bps) of the Amazon Elastic Block Store (Amazon EBS) volumes that are attached to an instance. The data is used to generate recommendations. You can also view EBS read/write bandwidth (operations per second), and EBS read/write throughput (KiBps) graphs in the Compute Optimizer console. For more information, see [Viewing EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html). You can also now export recommendations to encrypted Amazon S3 buckets. For more information, see [Exporting recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html). | October 7, 2020 | 
| [Recommendations export](#doc-history) | Recommendations can be exported to Amazon Simple Storage Service (Amazon S3). For more information, see [Exporting recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html). | June 10, 2020 | 
| [Self-service opt-out](#doc-history) | AWS Command Line Interface now supports self-service opt-out. For more information, see [Opting out your account](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html#account-opt-out). | April 6, 2020 | 
| [Service release](#doc-history) | Compute Optimizer released. | December 2, 2019 | 