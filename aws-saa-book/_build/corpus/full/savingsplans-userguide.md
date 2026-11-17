# Savings Plans User Guide

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
+ [What are Savings Plans?](#what-is-savings-plans)
   + [Savings Plans types](#plan-types)
   + [Compute Savings Plans and Reserved Instances](#sp-ris)
+ [Getting started with Savings Plans](#get-started)
+ [Services eligible for Savings Plans benefits](#sp-services)
+ [Understanding Savings Plans recommendations](#sp-recommendations)
   + [Understanding your recommendation calculations](#sp-rec-calculations)
   + [Customizing Savings Plans recommendations](#sp-rec-customizing)
   + [Viewing Savings Plans recommendation details](#sp-rec-details-view)
   + [Downloading Savings Plans recommendations](#sp-rec-downloading)
+ [Deciding which Savings Plans to purchase](#sp-analyzer)
   + [Understanding your analysis calculations](#sp-purchase-analysis-calculations)
   + [Running a Savings Plan purchase analysis](#sp-purchase-analysis)
   + [Reviewing your Savings Plan purchase analysis](#sp-review-purchase-analysis)
   + [Completing your Savings Plan purchase analysis](#sp-purchase-analysis-next-steps)
+ [Purchasing Savings Plans](#sp-purchase)
   + [Evaluating Savings Plans recommendations](#purchase-rec)
   + [Purchasing a custom Savings Plan commitment](#purchase-sp-direct)
   + [Queuing a Savings Plan purchase](#queued-sp-cart)
   + [Reviewing and finalizing Savings Plans purchases](#review-purchase-cart)
   + [Returning a purchased Savings Plan](#return-sp)
+ [Understanding your savings opportunities](#sp-overview)
   + [Viewing Savings Plans details](#sp-overview-details)
   + [Managing your Savings Plans alerts](#sp-alert)
+ [Monitoring your Savings Plans](#sp-monitoring)
   + [Viewing your Savings Plans inventory](#ce-sp-inventory)
      + [Renewing a Savings Plan](#queue-sp-replace)
      + [Deleting a queued Savings Plan](#ce-sp-queued-delete)
      + [Downloading your Savings Plans rates](#ce-sp-download-pr)
      + [Downloading your Savings Plans inventory](#ce-sp-download-inventory)
   + [Using the Savings Plans utilization report](#ce-sp-usingPR)
      + [Understanding utilization metrics and calculations](#ce-sp-pr-metrics)
      + [Downloading your Savings Plans utilization report](#ce-dl-pr)
   + [Using the Savings Plans coverage report](#ce-sp-usingCR)
      + [Understanding coverage metrics and calculations](#ce-sp-cr-metrics)
      + [Downloading your Savings Plans coverage report](#ce-dl-cr)
   + [Using budgets for Savings Plans](#sp-usingBudgets)
      + [Using a template to create a Savings Plans budget](#sp-create-savingsplans-budget-template)
      + [Customizing a Savings Plans budget](#sp-create-savingsplans-budget)
+ [Understanding how Savings Plans apply to your usage](#sp-applying)
+ [Automating Savings Plans with Amazon EventBridge](#automating-savingsplans-with-eventbridge)
+ [Identity and Access Management for Savings Plans](#identity-access-management)
+ [Logging Savings Plans API Calls with AWS CloudTrail](#logging-using-cloudtrail)
+ [Quotas and restrictions](#sp-quotas)
+ [Document history](#doc-history)

-----



# What are Savings Plans?
<a name="what-is-savings-plans"></a>

Savings Plans provide savings beyond On-Demand rates in exchange for a commitment of using a specified amount of compute power (measured per hour) for a one or three year period.
+ **One year:** A year is defined as 365 days (31,536,000 seconds).
+ **Three years:** Three years is defined as 1,095 days (94,608,000 seconds).

Savings Plans offer a flexible pricing model that provides savings on AWS usage. You can save up to 72% on your AWS compute workloads. Compute Savings Plans provide lower prices on Amazon EC2 instance usage regardless of instance family, instance size, OS, tenancy, or AWS Region. This also applies to AWS Fargate and AWS Lambda usage. SageMaker AI Savings Plans provide you with lower prices for your Amazon SageMaker AI instance usage, regardless of your instance family, instance size, component, or AWS Region. 

You can manage your plans by using recommendations, performance reporting, and budget alerts in AWS Cost Explorer.

When you sign up for Savings Plans, the prices you'll pay for usage stays the same through the plan term. You can pay for your commitment using **All upfront**, **Partial upfront**, or **No upfront** payment options.

To get started, use AWS Cost Explorer to view your recommended Savings Plans commitment, refresh Savings Plans recommendations, purchase Savings Plans, manage your Savings Plans, and view your historical AWS usage. These recommendations make it easy for you to know the optimal Savings Plans commitment level for you. You can customize the recommendation to meet your needs and then purchase your Savings Plan. To see a full list of AWS services that are eligible for Savings Plans, see [Services eligible for Savings Plans benefits](#sp-services).

**Topics**
+ [Savings Plans types](#plan-types)
+ [Compute Savings Plans and Reserved Instances](#sp-ris)

## Savings Plans types
<a name="plan-types"></a>

AWS offers four types of Savings Plans: Compute Savings Plans, Database Savings Plans, EC2 Instance Savings Plans, and SageMaker AI Savings Plans.
+ **Compute Savings Plans** provide the most flexibility and prices that are up to 66% off of On-Demand rates. These plans automatically apply to your EC2 instance usage, regardless of instance family (for example, m5, c5, etc.), instance size (for example, c5.large, c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), operating system (for example, Windows, Linux, etc.), or tenancy (for example, Dedicated, default, Dedicated Host). They also apply to your Fargate and Lambda usage. With Compute Savings Plans, you can move a workload from c5 to m5, shift your usage from EU (Ireland) to EU (London), or migrate your application from Amazon EC2 to Amazon ECS using Fargate at any time. You can continue to benefit from the low prices provided by Compute Savings Plans as you make these changes.
+ **Database Savings Plans** provide flexibility to use AWS database services while reducing costs by up to 35% on Aurora, RDS, DynamoDB, ElastiCache, DocumentDB, Timestream, Neptune, Keyspaces, DMS, and Amazon OpenSearch Service. These plans automatically apply to the latest provisioned instance generations regardless of engine, instance family, size, Availability Zone (AZ), or Region, and also apply to serverless usage. For example, with Database Savings Plans, you can change between Aurora db.r7g and db.r8g instances, shift a workload from EU (Ireland) to EU (London), modernize from RDS for Oracle to Aurora PostgreSQL-Compatible Edition, or move a workload from RDS to DynamoDB while maintaining your discounted rates.
+ **EC2 Instance Savings Plans** provide savings up to 72% off On-Demand, in exchange for a commitment to a specific instance family in a chosen AWS Region (for example, m5 in Virginia). These plans automatically apply to usage regardless of instance size (for example, m5.xlarge, m5.2xlarge, etc.), OS (for example, Windows, Linux, etc.), and tenancy (Host, Dedicated, Default) within the specified family in a Region.

  With an EC2 Instance Savings Plan, you can change your instance size within the instance type (for example, from c5.xlarge to c5.2xlarge) or the operating system (for example, from Windows to Linux), or move from Dedicated tenancy to Default and continue to receive the discounted rate provided by your EC2 Instance Savings Plan.
+ **SageMaker AI Savings Plans** provide savings up to 64% off of On-Demand rates. These plans automatically apply to your SageMaker AI instance usage regardless of instance family (for example, ml.m5, ml.c5, etc.), instance sizes (for example ml.c5.large, ml.c5.xlarge, etc.), Region (for example, us-east-1, us-east-2, etc.), and component (for example, Notebook, Training, etc.). 

  With SageMaker AI Savings Plans, you can move a workload from ml.c5 to ml.m5, shift your usage from Europe (Ireland) to Europe (London), or migrate your usage from Training to Inference at any time and continue to receive benefits.
**Note**  
Savings Plans provides low prices in exchange for commitment. The terms of the commitment can't be changed after purchase. As your usage changes, you can sign up for additional Savings Plans.  
Dedicated Instances are charged $2/hour in every Region you have at least one Dedicated Instance running. These dedicated fees are not discounted by Savings Plans.  
Both Compute and EC2 Instance plan types apply to EC2 instances that are a part of Amazon EMR, Amazon EKS, and Amazon ECS clusters. Amazon EKS charges will not be covered by Savings Plans, but the underlying EC2 instances will be.

## Compute Savings Plans and Reserved Instances
<a name="sp-ris"></a>

Compute Savings Plans are a flexible pricing model that offers low prices, just like Amazon EC2 Reserved Instances (RI), but with added flexibility. With Savings Plans, you can reduce your bill by committing to a consistent amount of compute usage (measured in $/hour), instead of specific instance configurations. Savings Plans give you the flexibility to use the compute option that best suits your needs at low prices, without having to perform exchanges or modifications.

Compute Savings Plans provide savings up to 66% off On-Demand, similar to Convertible RIs. Compute Savings Plans automatically reduce your cost on EC2 instance usage, Fargate, and Lambda. EC2 Instance Savings Plans offer savings up to 72% off of On-Demand, similar to Standard RIs. They also automatically save you money on any instance usage within a given EC2 instance family in your Region of choice. For more information, see [Savings Plans types](#plan-types).


**Comparing Savings Plans and RIs**  

|  | Compute Savings Plans | EC2 Instance Savings Plans | Convertible RIs\* | Standard RIs | 
| --- | --- | --- | --- | --- | 
| Savings over On-Demand | Up to 66% | Up to 72% | Up to 66% | Up to 72% | 
| Lower price in exchange for monetary commitment | ✓ | ✓ | — | — | 
| Automatically applies pricing to any instance family | ✓ | — | — | — | 
| Automatically applies pricing to any instance size | ✓ | ✓ | —\*\* | —\*\* | 
| Automatically applies pricing to any Tenancy or OS | ✓ | ✓ | — | — | 
| Automatically applies to Amazon ECS and Amazon EKS using Fargate | ✓ | — | — | — | 
| Automatically applies to Lambda | ✓ | — | — | — | 
| Automatically applies pricing across AWS Regions | ✓ | — | — | — | 
| Term length options of 1 or 3 years | ✓ | ✓ | ✓ | ✓ | 

**\*** Convertible RIs can be changed across instance family, instance size, OS, and tenancy, but requires you to manually perform exchanges.

**\*\*** Regional convertible RIs and Regional standard RIs provide instance size flexibility.

**Note**  
Savings Plans doesn't provide capacity reservations, but you can allocate On-Demand Capacity Reservation (ODCR) for your needs and your Savings Plans will apply.  
Savings Plans prices for instances running SUSE Linux Enterprise Server (SLES) are different compared to the corresponding RI price.  
Savings Plans prices do not change based on the amount of hourly commitment.  
Savings Plans doesn't apply to spot usage or usage covered by RIs.  
Savings Plans offer lower prices compared to On-Demand pricing in exchange for a commitment, and can't be cancelled during the term.

# Getting started with Savings Plans
<a name="get-started"></a>

To get started with Savings Plans, you'll need to enable Cost Explorer. Cost Explorer helps you optimize your costs with Savings Plans. In Cost Explorer, you can access customized purchase recommendations based on your past AWS usage, purchase Savings Plans, and easily manage your purchased Savings Plans.

Start by enabling your settings and permissions in Cost Explorer before using the AWS Billing and Cost Management console to view, analyze, and manage your Savings Plans.<a name="prerequisites"></a>

**Prerequisites**
+ **Enable Cost Explorer**. Manage access to your Savings Plans by first enabling your Cost Explorer access. It can take up to 24 hours for the data required to create recommendations to become available. For more information, see [Controlling Access for Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html) in the *AWS Cost Management User Guide*.
+ **Enable purchases using APIs**. Managing IAM permissions for Savings Plans APIs are found in the [Savings Plans API Reference](https://docs.aws.amazon.com/savingsplans/latest/APIReference/Welcome.html).

# Services eligible for Savings Plans benefits
<a name="sp-services"></a>

AWS offers three types of Savings Plans: Compute Savings Plans, EC2 Instance Savings Plans, and SageMaker Savings Plans. Compute Savings Plans apply to usage across Amazon EC2, AWS Lambda, and AWS Fargate. EC2 Instance Savings Plans apply to EC2 usage and SageMaker AI Savings Plans apply to SageMaker AI usage.

## Amazon EC2
<a name="sp-ec2"></a>

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the Amazon Web Services, Inc. (AWS) cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.

For more information about Amazon EC2, see [What Is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/concepts.html) in the *Amazon EC2 Getting Started Guide*.

## AWS Fargate
<a name="sp-fargate"></a>

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

Fargate is eligible for Compute Savings Plans.

For more information about Amazon ECS on Fargate, see [What is Amazon Elastic Container Service?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) in the *Amazon Elastic Container Service Developer Guide*.

For more information about Amazon EKS on Fargate, see [What is Amazon Elastic Kubernetes Service?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in the **Amazon EKS User Guide**.

## AWS Lambda
<a name="sp-lambda"></a>

AWS Lambda is a compute service that lets you run code without provisioning or managing servers. AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time you consume - there is no charge when your code is not running. With AWS Lambda, you can run code for virtually any type of application or backend service - all with zero administration. AWS Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging.

Lambda is eligible for Compute Savings Plans.

For more information about Lambda, see [What Is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/services-costmanagement.html) in the *AWS Lambda Developer Guide*.

## Amazon SageMaker AI
<a name="sp-sagemaker"></a>

Amazon SageMaker AI is a fully managed machine learning service. With SageMaker AI, data scientists and developers can quickly and easily build and train machine learning models, and then directly deploy them into a production-ready hosted environment. 

SageMaker AI provides an integrated Jupyter authoring notebook instance for easy access to your data sources for exploration and analysis, so you don't have to manage servers. It also provides common machine learning algorithms that are optimized to run efficiently against extremely large data in a distributed environment. 

With native support for bring-your-own-algorithms and frameworks, SageMaker AI offers flexible distributed training options that adjust to your specific workflows. Deploy a model into a secure and scalable environment by launching it with a few clicks from SageMaker AI Studio or the SageMaker AI console. 

SageMaker AI is eligible for SageMaker AI Savings Plans.

For more information about Amazon SageMaker AI, see [What Is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) in the *Amazon SageMaker AI Developer Guide*.

# Understanding Savings Plans recommendations
<a name="sp-recommendations"></a>

To help you save money, AWS provides customized Savings Plans recommendations based on your past usage. You can use these recommendations to understand what you can save, how the commitment will be used, and more.

You can view the recommendations for your AWS account. If you're using AWS Organizations, you can view recommendations from the management account or member account level.<a name="sp-rec-customize-howto"></a>

**To access your Savings Plans recommendations**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

The **Recommended Savings Plans** section on the **Recommendations** page shows a detailed breakdown of your Savings Plans selection. Your recommendations include the following summary metrics:
+ **Monthly On-Demand spend** – The estimated On-Demand spend based on your usage over the selected time period. This includes all active Savings Plans that you own at the time of computation. This value represents what your On-Demand spend would be on a monthly basis, based on your past usage and current Savings Plan commitments.
+ **Estimated monthly spend** – The projected spend based on the recommended Savings Plans commitments. This value consists of the recommended commitment and any usage projected to remain on On-Demand due to hour-to-hour variations in usage.
+ **Estimated monthly savings** – The monthly net savings amount based on the usage over the selected time period, if you purchased the recommended Savings Plans.

**Note**  
You can also receive your Savings Plans recommendations via the [AWS Cost Explorer API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html).  
When you use billing transfer as a bill source account, your estimated savings in Savings Plans recommendations might not match the effective savings data in your AWS Cost and Usage Report, Cost Explorer, and Bills page. This is because Savings Plans recommendations don't use custom data generated by Billing Conductor. The recommended commitment amount remains accurate to maximize savings on your account.

## Understanding your recommendation calculations
<a name="sp-rec-calculations"></a>

Savings Plans recommendations examine your usage over a selected time period. Based on the usage, we calculate what your bill could have been if you had purchased an additional Savings Plans commitment for that time period. We identify and recommend the commitment value that we estimate will result in the largest savings.

**Important**  
The recommendations don’t forecast your usage. Recommendations are based on your historical usage over the selected lookback period. Be sure to select a lookback period that reflects your future usage. If you've recently switched to CPU-optimized EC2 instances, select a lookback period after the change since license costs are no longer eligible for Savings Plans coverage. Recommendations don't account for any queued or scheduled purchases because recommendations are based on the usage in the lookback period. Recommendations are also generated for immediate purchases, and not for future purchases.  
Recommendations are calculated based on your **Reserved Instances and Savings Plans discount sharing** preferences. To view or change your preferences, see [Turning off reserved instances and Savings Plans discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) in the *AWS Billing User Guide*.
Recommendations at the management account level are calculated considering usage across all of the accounts in your AWS organization that have Reserved Instances or Savings Plans discount sharing enabled, to recommend a commitment that maximizes savings across accounts. Member account recommendations are calculated at the individual account level, to maximize savings for each isolated account.
Recommendations are generated for customers that have an average On-Demand spend of $0.10/hour during the lookback period (7, 30, or 60 days). If you recently purchased a Savings Plan, returned a Savings Plan, or if your Savings Plans recently expired, refresh your Savings Plans recommendations to take your current Savings Plans inventory and latest usage data into account.
Compute and EC2 Instance Savings Plans recommendations are created using the same set of usage. You can purchase both Compute Savings Plans and EC2 Instance Savings Plans to cover your usage, but the two sets of recommendations are not meant to be taken together simultaneously.
Recommendations are calculated using Savings Plans rates referenced in [Pricing with Savings Plans](https://aws.amazon.com/savingsplans/pricing/).

## Customizing Savings Plans recommendations
<a name="sp-rec-customizing"></a>

You can customize your Savings Plans recommendations using parameters shown on the **Recommendations** page.<a name="sp-rec-customize-howto"></a>

**To customize your Savings Plans recommendations**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

1. For **Savings Plan type**, choose **Compute Savings Plans**, **Database Savings Plans**, **EC2 Instance Savings Plans**, or **SageMaker AI Savings Plans**.

1. Choose a **Savings Plans term**.

1. Choose a **Payment option**.

1. Choose the number of days for **Based on the past**.

1. (Management account level only) Choose the **Linked accounts** tab, and then select the account IDs you want the recommendations for.

1. (Optional) To purchase the plans, select the check box next to your desired plans, and choose **Add Savings Plans to cart**.

Your recommendations change as you customize your selections. You’ll see the most optimal option presented to you in the **Our recommendation** section.

## Viewing Savings Plans recommendation details
<a name="sp-rec-details-view"></a>

Savings Plans recommendation details offer visibility into the potential impact of a recommended Savings Plan on your hourly On-Demand cost, coverage, and utilization. Each recommendation is designed to maximize your savings, taking into account your chosen **Recommendation parameters**, your current Savings Plans inventory, and your On-Demand spend over the lookback period. You can also access **Purchase Analyzer** from the **Recommendation details** page to customize your recommendations and estimate the cost, coverage, and utilization impact of your next Savings Plan purchase for custom commitments.

**To view the details of a Savings Plan recommendation**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

1. In the **Recommended Savings Plans** section on the **Recommendations** page, for a specific Savings Plan, choose **View details**.

The **Recommendation details** page shows three simulated charts that illustrate the impact of purchasing the recommended commitment:
+ **On-Demand cost**: Shows the current Savings Plan commitment, the recommended Savings Plan purchase, and the remaining On-Demand spend.
+ **Coverage**: Shows the coverage both before and after the recommended Savings Plan purchase.
+ **Utilization**: Shows the utilization of the recommended Savings Plan purchase.

**Note**  
You can also receive the details of recommended Savings Plans using the [AWS Cost Explorer API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlanPurchaseRecommendationDetails.html).

## Downloading Savings Plans recommendations
<a name="sp-rec-downloading"></a>

You can download your Savings Plans recommendations in CSV file format. CSV file format is useful to review or share recommendations.<a name="sp-rec-downloading-howto"></a>

**To download your Savings Plans recommendations**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

1. In the **Recommended Savings Plans** section on the **Recommendations** page, choose **Download CSV**.

**Note**  
You can also download recommendations for a specific Savings Plan on the **Recommendation details** page.

### CSV field details
<a name="sp-rec-csv"></a>

You will find the following information in your downloaded CSV file:
+ **Account ID** – The unique identifier for a member account.
+ **Offering ID** – The unique identifier for the Savings Plans prices used to generate the recommendations.
+ **Hourly commitment to purchase** – The recommended Savings Plan hourly commitment, based on your selected parameters.
+ **Estimated Savings Plans cost** – The estimated total cost of your recommended Savings Plans after purchase, over the selected time period (7, 30, or 60 days).
+ **Estimated On-Demand cost** – The estimated total On-Demand cost after the purchase of the recommended Savings Plans, over the select time period (7, 30, or 60 days).
+ **Current average hourly On-Demand spend** – The average hourly On-Demand spend observed over the selected time period.
+ **Current minimum hourly On-Demand spend** – The minimum hourly On-Demand spend observed over the selected time period.
+ **Current maximum hourly On-Demand spend** – The maximum hourly On-Demand spend observed over the selected time period.
+ **Estimated average utilization** – The expected utilization percentage of the recommended Savings Plan, based on your current eligible On-Demand costs.
+ **Estimated monthly savings amount** – The estimated savings that will result from your Savings Plans purchase, based on your past usage and the Savings Plans you already own.
+ **Estimated savings percentage** – The amount your Savings Plan commitment will save you from your current, Savings Plans-eligible On-Demand costs.
+ **Estimated ROI** – The estimated return on investment of the Savings Plan. This is calculated by taking your estimated savings and dividing it by the cost of the Savings Plan.

# Deciding which Savings Plans to purchase
<a name="sp-analyzer"></a>

Savings Plans Purchase Analyzer is a feature that allows you to model and evaluate potential Savings Plans purchases. You can calculate these purchases by using the recommended purchase amount, targeting a coverage percentage, or entering your own custom amount to see the impact on savings, coverage, and utilization. You can fine-tune the results by adjusting the lookback period or removing expiring Savings Plans from the analysis. Purchase Analyzer helps you in the decision-making process by enabling you to evaluate key metrics, including estimated monthly savings and coverage percentage.

Using Purchase Analyzer you can:
+ Estimate the cost, coverage, and utilization impact of planned Savings Plans purchases.
+ Model different purchase scenarios with customizable parameters.
+ Compare savings and risk for different commitment amounts.
+ Make more informed Savings Plan purchasing decisions.

**To access Savings Plans Purchase Analyzer**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Purchase Analyzer**.

## Understanding your analysis calculations
<a name="sp-purchase-analysis-calculations"></a>

A Savings Plan purchase analysis examines your cost, coverage, and utilization over a selected time period. Based on the analysis, we calculate what your On-Demand spend could be if you were to purchase an additional Savings Plan commitment for that time period.

**Important**  
The analyses don’t forecast your usage. Analyses are based on your historical usage over the selected lookback period. Be sure to select a lookback period that reflects your future usage. If you've recently switched to CPU-optimized EC2 instances, select a lookback period after the change since license costs are no longer eligible for Savings Plans coverage. Analyses don't account for any queued or scheduled purchases because analyses are based on the usage in the lookback period. Analyses are also generated for immediate purchases, and not for future purchases.
Analyses at the management account level are calculated considering usage across all of the accounts in your AWS organization that have Savings Plans discount sharing enabled, to recommend a commitment that maximizes savings across accounts or to calculate the impact of a custom commitment. Member account analyses are calculated at the individual account level, to recommend a commitment that maximizes savings or calculate custom commitment impact for each isolated account.

## Running a Savings Plan purchase analysis
<a name="sp-purchase-analysis"></a>

Use Purchase Analyzer to configure multiple parameters for your planned Savings Plan purchase analysis.<a name="sp-rec-customize-howto"></a>

**To run a purchase analysis**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Purchase Analyzer**.

1. Choose **Compute Savings Plans**, **Database Savings Plans**, **EC2 Instance Savings Plans**, or **SageMaker AI Savings Plans**.

1. For **EC2 Instance Savings Plans**, choose a **Region** and **Instance family**.

1. Under **Analysis level**, choose **Payer** or **Linked account**.

1. If you chose **Linked account**, select a linked account from the dropdown menu.

1. Under **Term**, choose a **1-year** or **3-year** commitment term.

1. Under **Payment option**, choose **All upfront**, **Partial upfront**, or **No upfront**.

1. Under **Lookback period**, choose a lookback period within the last 60 days.

1. Under **Exclude expiring Savings Plans**, select Savings Plans expiring within the next 90 days that you’d like to exclude from the analysis.

1. Under **Commitment**, choose **Recommended**, **Target coverage (%)**, or **Custom**.

1. If you chose **Target coverage (%)**, under **Target coverage (%)**, enter your target coverage percentage.

1. If you chose **Custom**, under **Hourly commitment ($)**, enter your preferred hourly commitment amount.

1. Choose **Run analysis**.

## Reviewing your Savings Plan purchase analysis
<a name="sp-review-purchase-analysis"></a>

After setting parameters and running the analysis, Purchase Analyzer applies the resulting Savings Plan to each hour of the historical lookback period. This process takes into account the composition of usage across different services and Regions, as well as the Savings Plans inventory after removing any Savings Plans that were excluded. This allows you to review the impact of a purchase on your unique environment. The data is presented in three charts: cost, coverage, and utilization. You can switch between tabs to view the different metrics and hover over data points for detailed hourly information.

The **Analysis** section on the **Purchase Analyzer** page shows visual overtime charts and includes the following summary metrics:
+ **Estimated monthly savings** – The monthly net savings amount based on the usage over the selected time period, if you purchased the recommended or custom commitment.
+ **Average hourly coverage increase** – The estimated average hourly coverage increase, if you were to purchase the recommended or custom commitment.
+ **Average hourly utilization** – The estimated average hourly utilization of the recommended or custom commitment.

**Note**  
You can also receive your purchase analyses via the [AWS Cost Explorer API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html).

**To model different scenarios**

1. Adjust the parameters as required.

1. Choose **Run analysis**.

   This generates new results.

1. Compare results across different commitment amounts or terms.

## Completing your Savings Plan purchase analysis
<a name="sp-purchase-analysis-next-steps"></a>

Once you've modeled purchase scenarios, you can choose to download your Savings Plan analysis in CSV file format, which is useful to review or share, or add your Savings Plan to cart.

**To complete your Savings Plan analysis**

1. On the **Purchase Analyzer** page, choose **Download CSV** to download the analysis in CSV file format.

1. On the **Purchase Analyzer** page, choose **Add Savings Plan to cart**, and then review your order on the **Cart** page.

### CSV field details
<a name="sp-analysis-csv"></a>

You will find the following information in your downloaded CSV file:
+ **Offering ID** – The unique identifier for the Savings Plans prices used to generate the recommended or custom commitment.
+ **Hourly commitment to purchase** – The Savings Plan hourly commitment, based on your selected parameters.
+ **Estimated Savings Plans cost** – The estimated total cost of your Savings Plan after purchase, over the selected time period (7, 30, or 60 days).
+ **Estimated On-Demand cost** – The estimated total On-Demand cost after the purchase of the Savings Plan, over the select time period (7, 30, or 60 days).
+ **Current average hourly On-Demand spend** – The average hourly On-Demand spend observed over the selected time period.
+ **Current minimum hourly On-Demand spend** – The minimum hourly On-Demand spend observed over the selected time period.
+ **Current maximum hourly On-Demand spend** – The maximum hourly On-Demand spend observed over the selected time period.
+ **Estimated average utilization** – The expected utilization percentage of the Savings Plan, based on your current eligible On-Demand costs.
+ **Estimated monthly savings amount** – The estimated savings that will result from your Savings Plan purchase, based on your past usage and the Savings Plans you already own.
+ **Estimated savings percentage** – The amount your Savings Plan commitment will save you compared to your current Savings Plans-eligible On-Demand costs.
+ **Estimated ROI** – The estimated return on investment of the Savings Plan. This is calculated by taking your estimated savings and dividing it by the cost of the Savings Plan.

# Purchasing Savings Plans
<a name="sp-purchase"></a>

You can access Savings Plans in the AWS Billing and Cost Management console. You can add your selection to your Savings Plans cart from the **Recommendations** page or from the **Purchase Savings Plans** page. We suggest that you use the **Recommendations** page to see Savings Plans recommendations based on your past usage. You can also use **Purchase Analyzer** to estimate the cost, coverage, and utilization impact of your next Savings Plan purchase.

**Note**  
When you use billing transfer, you can purchase Savings Plans and Reserved Instances only in the AWS Organizations where they apply. Savings Plans and Reserved Instances can't be shared outside the purchasing organization. The account that purchases Savings Plans and Reserved Instances is responsible for the purchase, even when another account pays their bill.

**Topics**
+ [Evaluating Savings Plans recommendations](#purchase-rec)
+ [Purchasing a custom Savings Plan commitment](#purchase-sp-direct)
+ [Queuing a Savings Plan purchase](#queued-sp-cart)
+ [Reviewing and finalizing Savings Plans purchases](#review-purchase-cart)
+ [Returning a purchased Savings Plan](#return-sp)

## Evaluating Savings Plans recommendations
<a name="purchase-rec"></a>

You can visit your **Recommendations** page to see the Savings Plans that AWS recommends to help you save on eligible usage. These recommendations can be refreshed at any time to make it easy for you to purchase the optimal Savings Plans to help you save. You can directly add Savings Plans that are recommended for your account to your cart. For more information about how to view your **Recommendations** page, or to learn how recommendations are calculated, see [Understanding Savings Plans recommendations](#sp-recommendations).<a name="purchase-rec-howto"></a>

**To purchase Savings Plans from the **Recommendations** page**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Recommendations**.

1. Refresh your Savings Plans recommendations to include recent usage and up-to-date Savings Plans inventory.

1. In the **Recommendation parameters** section, choose your preferred **Savings Plans type**, **Savings Plans term**, **Payment option**, and lookback period.

1. In the **Recommended Savings Plans** table, select the check boxes next to the Savings Plans that you want to purchase.
**Note**  
The recommended commitment is the Savings Plans rate, and not the On-Demand spend.

1. Choose **Add Savings Plans to cart**.
**Note**  
For member account recommendations, only the member account owner can add Savings Plans recommendations to the cart and proceed to purchase recommendations.

1. (Optional) To queue the recommended purchase for a future use, see [Queuing a Savings Plan purchase](https://docs.aws.amazon.com/savingsplans/latest/userguide/queued-sp-cart.html).

1. To complete your purchase, choose **Cart** in the left pane.

1. In the **Cart** page, review your order and choose **Submit order**.

   To learn more about the **Cart** page, see [Reviewing and finalizing Savings Plans purchases](https://docs.aws.amazon.com/savingsplans/latest/userguide/review-purchase-cart.html).

## Purchasing a custom Savings Plan commitment
<a name="purchase-sp-direct"></a>

You can purchase a Savings Plan with a commitment amount that is different from the recommended commitment. Purchase a commitment of your choice on the **Purchase Savings Plans** page.<a name="ce-sp-compute-howto"></a>

**To purchase a Savings Plan**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Purchase Savings Plans**.

1. Under **Savings Plans type**, choose **Compute Savings Plans**, **Database Savings Plans**, **EC2 Instance Savings Plans**, or **SageMaker AI Savings Plans**.

1. For **EC2 Instance Savings Plans**, choose a **Region** and **Instance family**.

1. Under **Term**, choose a commitment term for your Savings Plans.

1. Under **Purchase commitment**, in **Hourly commitment**, enter an hourly commitment amount.
**Note**  
The **Hourly commitment** is the Savings Plans rate, and not the On-Demand spend.

1. Under **Payment option**, choose between **All upfront**, **Partial upfront**, and **No upfront**.

1. If you chose **Partial upfront**, enter the **Partial upfront payment** amount.

1. (Optional) To queue the Savings Plan to start on a future date, set the **Start date**.

1. Choose **Add to cart**.
**Note**  
Before adding to cart, you can choose **Analyze Savings Plan** to transfer your Savings Plan details and commitment to **Purchase Analyzer**. There, you can review, update, or run analysis to see the impact of your planned Savings Plan purchase.

1. On the **Cart** page, review your order, and choose **Submit order**.

## Queuing a Savings Plan purchase
<a name="queued-sp-cart"></a>

You can *queue*, or schedule, a Savings Plan purchase to occur on a future date. The date can be specific to the exact second that you want to start coverage. Any upfront or recurring fee is charged only when the queued purchase is processed on the start date you choose. You can delete this queued purchase at any time before the start date.<a name="queued-sp-cart-howto"></a>

**To queue future Savings Plan purchases**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. Add your Savings Plans from the **Purchase Savings Plans** page or the **Recommendations** page.

   To learn more about this process, see [Evaluating Savings Plans recommendations](#purchase-rec) or [Purchasing a custom Savings Plan commitment](#purchase-sp-direct).

1. In the navigation pane, under **Savings Plans**, choose **Cart**.

1. Select your Savings Plans.

1. Choose **Set start date**.

1. Choose a **Date** and **Time**.

   You can queue a purchase up to three years in the future. You can also specify to the exact second. Past dates aren't applicable.
**Note**  
Savings Plan purchases are processed and validated at the time of the **Start date**, and must pass all validations and be invoiced within the same calendar month of the **Start date**. Savings Plan purchases will be marked as payment-failed and will not discount any usage if the process isn't completed by the end of the month in the UTC time zone.

1. Choose **Confirm**.

1. (Optional) To clear the **Start date**, choose **Set start date**.

   1. Choose **Remove start date**.

1. Choose **Submit order**.

Any queued purchases will appear with the status **Queued** in your **Account Inventory** page. To delete any queued purchases before the start date, see [Deleting a queued Savings Plan](#ce-sp-queued-delete).

## Reviewing and finalizing Savings Plans purchases
<a name="review-purchase-cart"></a>

The Savings Plans **Carts** page keeps your commitments until you're ready to make a purchase.<a name="review-cart-howto"></a>

**To review and finalize purchases from the **Cart** page**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Cart**.

1. Review your order as follows:
   + **Type**: The type of Savings Plan. For more information, see [Savings Plans types](#plan-types).
   + **Term**: Your term commitment in years. Choose a **1-year** or **3-year** term.
**Note**  
**One year:** A year is defined as 365 days (31,536,000 seconds).  
**Three years:** Three years is defined as 1,095 days (94,608,000 seconds).
   + **Region**: (Only applicable to EC2 Instance Savings Plans) The AWS Region you're committing to. For example, `US East (N. Virginia)`.
   + **Instance type**: The instance family (for example, M5, C5, R5, C5d, etc.) that you are committing to (only applicable to EC2 Instance Savings Plans).
   + **Purchase option**: The purchase option of the commitment. Choose from **All Upfront**, **Partial Upfront**, or **No Upfront**.
   + **Start date**: The date and time when your commitment will be purchased (UTC). By default, the date is set to **Now**, indicating the purchase will complete as soon as you submit the order.
   + **Commitment**: The hourly commitment associated with your Savings Plan and term at the Savings Plan rate.
   + **Upfront payment**: The upfront portion of the payment you will be charged at checkout, in accordance with your selected payment option.
   + **Monthly payment**: The monthly charge amount for your Savings Plans. This amount is billed each month over the plan's term.
   + **Total cost**: The total commitment for the Savings Plans over the selected term. This includes the **upfront payment** and recurring **monthly payments** over the length of your term.

1. Review the following contents in the **Summary** section:
   + **Total commitment**: The sum of all Savings Plans costs currently in your cart, regardless of **Start date** and **Payment option**.
   + **Total commitment starting now**: The sum of the **Upfront payment** for any Savings Plan with the **Start date** set to **Now**.

1. (Optional) Remove any Savings Plan from your cart by selecting each item and choosing **Remove from cart**.

1. (Optional) To start over, remove all items by choosing **Clear cart**.

1. (Optional) Add new commitments by choosing **Add another Savings Plan**.

1. Choose **Submit order**.

If you encounter any error messages or unsuccessful attempts when you're completing your purchase, contact Support. For details on how to contact Support, see [Getting help with your bills and payments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-get-answers.html) in the *AWS Billing User Guide*.

## Returning a purchased Savings Plan
<a name="return-sp"></a>

When you purchase a Savings Plan, you make a commitment for one or three years. However, in the case that you purchase a Savings Plan and quickly identify a purchase error that you want to rectify, you'll have a limited time period to do so. Any Savings Plan with an hourly commitment of $100 or less that has been purchased in the last seven days and in the same calendar month can be returned, provided you haven't reached your return limit. Once the calendar month ends (UTC time), these purchased Savings Plans can no longer be returned. For more information about quotas, see [Quotas and restrictions](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-quotas.html).

When you return a Savings Plan, you'll receive a 100% refund for any upfront charges made towards your plan and these refunds will be reflected in your bill within 24 hours of the return. Any usage that was covered by the plan will be charged at On-Demand rates or get covered by a different Savings Plan, if applicable.

You can return a Savings Plan using the console or by calling the `ReturnSavingsPlan` action through the AWS SDK/CLI.

**To return an active Savings Plan**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. Choose a Savings Plan to open the **Savings Plan details** page.

1. Choose **Return Savings Plan**.
**Note**  
The **Return Savings Plan** button is only visible in the details page when a Savings Plan is eligible for return.  
When you use billing transfer, the account that purchases Savings Plans must request the return, even when another account pays their bill.

1. In the **Return Savings Plan** dialog box, choose **Confirm return**.
**Note**  
This action can’t be reverted.

You can view returned Savings Plans in the **Savings Plans inventory** page in the console or by calling the `DescribeSavingsPlans` action in the AWS SDK/CLI. Returned Savings Plans appear with the status of **Returned**.

### Savings Plan return restrictions
<a name="return-sp-restrictions"></a>

If you submit a request to return a Savings Plan and it is ineligible, you'll receive an error related to one of the following reasons:
+ The limit for your consolidated billing family has been met. If you're using a single AWS account, the limit for that account has been met.

  For more information about quotas, see [Quotas and restrictions](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-quotas.html).
+ The Savings Plan is not in an "active" state. Only Savings Plans that have been activated can be returned. To return a “payment-pending” Savings Plan, wait for it to activate.
+ The hourly commitment is greater than $100.
+ The request has been made by a user with insufficient permissions.
**Note**  
Only root users or IAM users with the `savingsplans:returnSavingsPlan` permission can return a Savings Plan in their account. The AWS managed policy `AWSSavingsPlansFullAccess` includes that permission.
+ The Savings Plan was purchased in a different month or in the same month but more than seven days ago.
+ The Savings Plan is an All Upfront or Partial Upfront Savings Plan and you are registered under AWS Brazil or AWS Turkey.

  For more information about seller of record (SOR), see [Finding the seller of record](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/finding-the-seller-of-record.html).
+ The management account is not the same as the management account used when purchasing the Savings Plan.

# Understanding your savings opportunities
<a name="sp-overview"></a>

You can use the **Overview** page on the AWS Cost Management console to see any Savings Plans that you own, in addition to potential savings opportunities.

**Note**  
If you currently don't own any Savings Plans, the **Overview** page shows a summary of how Savings Plans work, along with recommended Savings Plans purchases based on your past usage.<a name="ce-sp-accessoverview"></a>

**To access the Savings Plans overview**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Overview**.

Your savings opportunities are shown under **Additional savings opportunities** or **Savings opportunities**, depending on whether you’ve made past Savings Plans purchases or not.

To view your detailed recommendations, choose **View recommended savings plans**. To learn more about how your Savings Plans recommendations are calculated, see [Understanding Savings Plans recommendations](#sp-recommendations).

## Viewing Savings Plans details
<a name="sp-overview-details"></a>

After you purchase Savings Plans, you see a **Details** section in your **Overview** page. The **Details** section shows the following metrics related to your purchased Savings Plans:
+ **Type** – Determines the summary by Savings Plans type.
+ **MTD/YTD plans** – The number of Savings Plans that have been active during the selected period.
+ **MTD/YTD commitment** – The total amortized commitments during the selected period.
+ **MTD/YTD utilization** – The average utilization percentage during the selected period.
+ **MTD/YTD savings** – The total savings from Savings Plans during the selected period.

To see details of the Savings Plans you own, choose **View all** in the **Details** section, or choose **Inventory** in the left navigation pane.

## Managing your Savings Plans alerts
<a name="sp-alert"></a>

You can track your Savings Plans expirations and upcoming queued Savings Plans in Cost Explorer. You can use Savings Plans alerts to receive advance email alerts 1, 7, 30, or 60 days before your Savings Plans expiration date, or in when a commitment is queued for purchase. These notifications also alert you on the expiration date, and can be sent to up to 10 email recipients.

For information about how to manage your Savings Plans alert subscriptions, see [View, create, update, and delete reservation and Savings Plans alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-example-policies.html#example-view-ce-expiration) in the *AWS Billing User Guide*.<a name="ce-sp-alerts-process"></a>

**To turn on Savings Plans expiration or queued purchases alerts**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Overview**.

1. Choose **Manage alert subscriptions**.

1. In the **Alert frequency** section, select all of the dates that you want to receive your alerts.

1. In the **Email recipients** section, enter your recipients' email addresses.

1. Choose **Save**.

AWS monitors your Savings Plans settings and automatically sends you alerts according to your preferences.

# Monitoring your Savings Plans
<a name="sp-monitoring"></a>

Monitoring is an important part of your Savings Plans usage. Understanding the Savings Plans that you own, how they are applying to your usage, and what usage is being covered are important parts of optimizing your costs with Savings Plans. You can monitor your usage in the Savings Plans **Inventory** page or by using utilization and coverage reports. You can also set budgets for your Savings Plans utilization, coverage, and costs.

**Topics**
+ [Viewing your Savings Plans inventory](#ce-sp-inventory)
+ [Using the Savings Plans utilization report](#ce-sp-usingPR)
+ [Using the Savings Plans coverage report](#ce-sp-usingCR)
+ [Using budgets for Savings Plans](#sp-usingBudgets)

## Viewing your Savings Plans inventory
<a name="ce-sp-inventory"></a>

The Savings Plans **Inventory** page shows a detailed overview of the Savings Plans that you own, or have queued for future purchase.

If you're a user in a member account of AWS Organizations, you can view the Savings Plans owned by your specific member account. If you’re a user in the management account of an organization, you can either view Savings Plans that are owned only by the management account, or you can view Savings Plans that are owned by all accounts in your organization. You can change views by choosing **Account inventory** or **Organization inventory**.

**Note**  
You can see your recently purchased Savings Plans in your **Account inventory** shortly after purchase. It might take longer for Savings Plans to appear in your **Organization inventory** view.<a name="review-sp-inventory-howto"></a>

**To view your **Inventory** page**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

The Savings Plans table shows the following information for your purchased Savings Plans:
+ **Savings Plan ID** – The unique identifier for each individual Savings Plan.
+ **Account ID** – The account ID that owns the particular Savings Plan. This column only appears in the **Organization inventory** view.
+ **Status** – The status of each Savings Plan. For example, active, queued, etc.
+ **Type** – The type of Savings Plan.
+ **Instance family** – The instance family that your Savings Plan is committed to. This only applies to the EC2 Instance Savings Plans type.
+ **Region** – The AWS Region that your Savings Plan is committed to. This only applies to the EC2 Instance Savings Plans type.
+ **Commitment** – The hourly committed spend for the particular Savings Plan.
+ **MTD net savings** – The actual savings amount compared to On-Demand, based on the usage of the particular Savings Plan commitment. This column only appears in the **Organization inventory** view.
+ **Start date** – The date when the Savings Plan commitment started.
+ **End date** – The date when the Savings Plan commitment ends.

### Renewing a Savings Plan
<a name="queue-sp-replace"></a>

If your active Savings Plans are nearing expiration, you can queue a purchase to start as soon as the active Savings Plans expire. This helps ensure that you have continuous Savings Plans coverage.<a name="queue-sp-replace-howto"></a>

**To queue a Savings Plan purchase to replace an expiring Savings Plan**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. Select the reference Savings Plan using the check box.

   You can only select one Savings Plan at a time. The selected Savings Plan must be in active status.

1. Choose **Actions**.

1. Choose **Renew Savings Plan**.

1. (Alternative) Choose the reference Savings Plan.

   1. On the **Savings Plan details** page, choose **Renew Savings Plan**.
**Note**  
**Renew Savings Plan** renews your plan with the same configuration, and fees are charged using the current Savings Plan rate. This automatically sets the new Savings Plan start date to be one second after the reference Savings Plan expiration.   
You might want to change your commitment amount depending on changes in your usage or Savings Plans rates from the time you purchased the reference Savings Plan.

1. On the **Cart** page, choose **Submit order**.

To learn more about the **Cart** page, see [Reviewing and finalizing Savings Plans purchases](#review-purchase-cart).

### Deleting a queued Savings Plan
<a name="ce-sp-queued-delete"></a>

You can use queued Savings Plans to have continued coverage for your On-Demand usage. However, we understand that your preferences might change as the start date approaches. You can delete your queued purchased using the following process.<a name="ce-sp-queued-delete-howto"></a>

**To delete a queued Savings Plan purchase**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the navigation pane, choose **Inventory** under the **Savings Plans** section.

1. Select the queued Savings Plans to delete.

   The status must be marked as `Queued`.

1. Choose **Actions**.

1. Choose **Delete queued Savings Plans**.

1. (Alternative) Choose the queued Savings Plan.

   1. On the **Savings Plan details** page, choose **Delete queued Savings Plan**.

1. In the pop-up window, choose **Delete**.

### Downloading your Savings Plans rates
<a name="ce-sp-download-pr"></a>

You can download a CSV file with detailed information for each Savings Plan you own. The file might take longer to download for Compute Savings Plans.<a name="ce-sp-downloadpr-howto"></a>

**To download your Savings Plans rates file**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. In the **Savings Plans** section, choose **Savings Plans ID**.

1. On the **Savings Plans details page**, choose **Download Savings Plans Rates**.

You can also download your Savings Plans rates using the AWS Price List bulk API. For more information, see [Using the bulk API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-ppslong.html) in the *AWS Billing User Guide*.

### Downloading your Savings Plans inventory
<a name="ce-sp-download-inventory"></a>

You can download a CSV file with all of the detailed information for Savings Plans in your Savings Plans table.<a name="ce-sp-downloadinv-howto"></a>

**To download your Savings Plans inventory file**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. In the **Savings Plans** section, choose **Download CSV**.

   You can download all Savings Plans on your **Inventory** page, or select any number of Savings Plans before downloading the CSV file.

## Using the Savings Plans utilization report
<a name="ce-sp-usingPR"></a>

Savings Plans utilization shows you the percentage of your Savings Plans commitment that you're using across your On-Demand usage. You can use your Savings Plans utilization report to visually understand how your Savings Plans apply to your usage over the configured time period. Along with a visualized graph, the report shows high-level metrics based on your selected Savings Plan, filters, and lookback periods. Utilization is calculated based on how your Savings Plans applied to your usage over the lookback period.

For example, if you have a $10/ hour commitment, and your usage billed with Savings Plans rates totals to $9.80 for the hour, your utilization for that hour is 98 percent.<a name="ce-sp-sf-howto"></a>

**To view your utilization report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. In the **Savings Plans** section, choose the relevant **Savings Plan ID**.

1. In the **Savings Plan details**, choose **View utilization report**.

**Note**  
When your account is in a billing group (standard or billing transfer), Savings Plans utilization reports show pro forma data. For more information about pro forma data, see [What is Billing Conductor?](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

### Understanding utilization metrics and calculations
<a name="ce-sp-pr-metrics"></a>

You can find high-level metrics in the **Utilization report** section.
+ **Savings Plans spend** – Your Savings Plans commitment spend over the lookback period.
+ **On-Demand spend equivalent** – The amount you would have spent on the same usage if you didn’t commit to Savings Plans. This amount is the equivalent On-Demand cost based on current On-Demand rates.
+ **Total net savings** – The amount you saved using Savings Plans commitments over the selected time period, compared to the On-Demand cost estimate.

You can see your Savings Plans utilization at an hourly, daily, or monthly granularity, based on your lookback period. You can customize your filters by member account, AWS Region, Savings Plans type, and instance family in the **Filters** section.

If you’re a user in a management account, you can see the aggregated utilization for the entire Consolidated Billing family.

### Downloading your Savings Plans utilization report
<a name="ce-dl-pr"></a>

You can download a CSV file of your Savings Plans utilization report data.<a name="ce-dl-pr-howto"></a>

**To download your utilization report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Utilization report**.

1. On the **Utilization report** page, choose **Download chart (CSV)**.

## Using the Savings Plans coverage report
<a name="ce-sp-usingCR"></a>

The Savings Plans coverage report shows what percentage of your applicable AWS usage costs are being covered by your Savings Plans during your selected time period.

**To view your coverage report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Inventory**.

1. In the **Savings Plans** section, choose the relevant **Savings Plan ID**.

1. In the **Savings Plan details**, choose **View coverage report**.

**Note**  
When your account is in a billing group (standard or billing transfer), Savings Plans utilization reports show pro forma data. For more information about pro forma data, see [What is Billing Conductor?](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

### Understanding coverage metrics and calculations
<a name="ce-sp-cr-metrics"></a>

You can find the following high-level metrics in the **Coverage report** section:
+ **On-Demand spend not covered** – The amount of eligible savings spend that was not covered by Savings Plans or Reserved Instances over the lookback period.
+ **Average coverage** – The aggregated Savings Plans coverage percentage based on the selected filters and look-back period.
+ **Potential monthly savings vs On-Demand** – Your potential savings amount based on your Savings Plans recommendations. This is shown as a monthly amount.

Coverage is calculated as:

(On-Demand equivalent of usage covered by your Savings Plans)

÷

(On-Demand equivalent usage covered by your Savings Plans \+ Savings Plans eligible amount that was billed at On-Demand rates)

For example, if you are running 10 identical instances with an On-Demand price of $1.00/hour, and 9 of the 10 instances that you're running are covered by your Savings Plans commitment, your coverage would be 90 percent.

(9 Savings Plans covered instance \* $1.00/hour OD rate)

÷

(9 Savings Plans covered instances \* $1.00/hour OD rate \+ 1 On-Demand Instance \* $1.00/hour OD rate)

You can see your usage at an hourly, daily, or monthly granularity. Usage is calculated using your selected lookback period. You can customize your filters by member account, AWS Region, instance family, service, and cost category in the **Filters** section.

If you’re a user in the management account, you can see the aggregated coverage for the entire Consolidated Billing family.

### Downloading your Savings Plans coverage report
<a name="ce-dl-cr"></a>

You can download a CSV file of your Savings Plans coverage report data.<a name="ce-dl-pr-howto"></a>

**To download your coverage report**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Savings Plans**, choose **Coverage report**.

1. On the **Coverage report** page, choose **Download chart (CSV)**.

## Using budgets for Savings Plans
<a name="sp-usingBudgets"></a>

You can use AWS Budgets to set budgets for your Savings Plan utilization, coverage, and costs. You can track your costs as you continue to optimize through AWS.

You can create and set up a budget for your Savings Plans in two ways:
+ [Using a template (simplified)](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-create-savingsplans-budget-template.html)
+ [Customizing a budget (advanced)](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-create-savingsplans-budget.html)

For more information, see [Managing Your Costs with AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html) in the *AWS Cost Management User Guide*.

### Using a template to create a Savings Plans budget
<a name="sp-create-savingsplans-budget-template"></a>

Use the following procedure to create a coverage budget for your Savings Plans using a template.

You can create a budget using a template with recommended configurations. Budget templates are a simplified way to start using AWS Budgets, with a single page workflow, unlike the 5-step workflow that is required for [Customizing a budget (advanced)](https://docs.aws.amazon.com/cost-management/latest/userguide/custom-budgets.html).

**To create a Savings Plans coverage budget using a template**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Use a template (simplified)**.

1. Under **Templates**, choose **Daily Savings Plans coverage budget**.

1. For **Budget name**, enter the name of your budget. Your budget name must be unique within your account and can use A-Z, a-z, spaces, and the following characters:

   ```
   _.:/=+-%@
   ```

1. For **Coverage threshold**, enter the coverage percentage that you want AWS to notify you at. For example, for a coverage budget where you want to stay above 80 percent, enter **80**. Budget notifies you when your overall coverage goes below 80 percent.

1. For **Email recipients**, enter the email addresses that you want the notifications to be sent to. Separate multiple email addresses with a comma. A notification can have up to 10 email addresses.

1. Choose **Create budget**.

### Customizing a Savings Plans budget
<a name="sp-create-savingsplans-budget"></a>

Use the following procedure to create a customized budget for Savings Plans utilization or Savings Plans coverage.

You can customize a budget to set parameters specific to your use case. You can customize the time period, the start month, and specific accounts. Creating a customized budget involves a 5-step workflow.<a name="savingsplans-budget"></a>

**To create a Savings Plans budget**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Budgets**.

1. At the top of the page, choose **Create budget**.

1. Under **Budget setup**, choose **Customize (advanced)**.

1. Under **Budget types**, choose **Savings Plans budget**.

1. Choose **Next**.

1. For **Budget name**, enter the name of your budget. Your budget name must be unique within your account and can use A-Z, a-z, spaces, and the following characters:

   ```
   _.:/=+-%@
   ```

1. For **Period**, choose how often you want the budget to reset the actual and forecasted spend. Choose **Daily** for every day, **Monthly** for every month, **Quarterly** for every three months, or **Annually** for every year. All budget times are in UTC.

1. For **Monitor my spend against**, choose what you want the budget to track.

   **Utilization of Savings Plans** is how much of your Savings Plans you've used.

   **Coverage of Savings Plans** is how much of your usage a Savings Plan covers.

1. For **Utilization threshold**, enter the utilization percentage that you want AWS to notify you at. For example, for a utilization budget where you want to stay above 90 percent Savings Plans utilization, enter **90**, and the budget notifies you when your overall Savings Plans utilization goes below 90 percent.

1. For **Coverage threshold**, enter the coverage percentage that you want AWS to notify you at. For example, for a coverage budget where you want to stay above 80 percent, enter **80**. Budget notifies you when your overall coverage goes below 80 percent.

1. Under **Budget scope**, add [filtering](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create-filters.html) and use advanced options to narrow the set of cost information tracked as part of your budget.

1. Choose **Next**.

1. Under **Alert settings**, choose whether to send budget alerts via email and/or Amazon SNS topic.

1. For **Email recipients**, enter the email addresses that you want the notifications to be sent to. Separate multiple email addresses with a comma. A notification can have up to 10 email addresses.

1. (Optional) For **Amazon SNS ARN**, enter the Amazon Resource Name (ARN) for your Amazon SNS topic.

   If you want to use an Amazon SNS topic for your notification but don't have one, see [Create a Topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) in the *Amazon Simple Notification Service Developer Guide*.

   AWS verifies that your budget has permission to send notifications to your Amazon SNS topic by sending a test email to your Amazon SNS topic. 

   For a sample policy and instructions on granting your budget permissions, see [Creating an Amazon SNS Topic for Budget Notifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-sns-policy.html). A notification can be subscribed to only one Amazon SNS topic.

1. Choose **Next**.

1. Choose **Create budget**.

# Understanding how Savings Plans apply to your usage
<a name="sp-applying"></a>

If you have active Savings Plans, they apply automatically to your eligible AWS usage to reduce your bill.

## Calculating bills with Savings Plans
<a name="calc-bills-sp"></a>

Savings Plans apply to your usage after the Amazon EC2 Reserved Instances (RI) are applied.

Your current Savings Plans are grouped together and applied to the eligible usage. **EC2 Instance Savings Plans** are applied before **Compute Savings Plans** because **Compute Savings Plans** have broader applicability. 

In a *Consolidated Billing Family*, Savings Plans are applied first to the owner account's usage, and then to other accounts' usage. This occurs only if you have sharing enabled.

We calculate your potential savings percentages of each combination of eligible usage. This percentage compares the Savings Plans rates with your current On-Demand rates. Your Savings Plans are applied to your highest savings percentage first. If there are multiple usages with equal savings percentages, Savings Plans are applied to the first usage with the lowest Savings Plans rate. Savings Plans continue to apply until there are no more remaining usages, or your commitment is exhausted. Any remaining usage is charged at the On-Demand rates.

## Savings Plans example
<a name="sp-example"></a>

The rates in these examples are illustrative only. In this example, you have the following usage in a single hour:
+ 4x `r5.4xlarge` Linux, shared tenancy instances in us-east-1, running for the duration of a full hour
+ 1x `m5.24xlarge` Windows, dedicated tenancy instance in us-east-1, running for the duration of a full hour
+ 400 vCPU and 1,600 GB of Fargate usage in us-west-1
+ 1 million requests for 512 MB (0.5 GB) memory of AWS Lambda usage in us-east-2, lasting for 3 seconds each


**Pricing example**  

|  | On-Demand rate | Compute Savings Plans rate | Compute Savings Plans savings % | EC2 Instance Savings Plans rate | EC2 Instance Savings Plans savings % | 
| --- | --- | --- | --- | --- | --- | 
| r5.4xlarge Linux | $1.00 | $0.70 | 30% | $0.60 | 40% | 
| Fargate vCPU | $0.04 | $0.03 | 25% | N/A | N/A | 
| Fargate GB | $0.004 | $0.003 | 25% | N/A | N/A | 
| m5.24xlarge Windows | $10.00 | $8.20 | 18% | $7.80 | 22% | 
| Lambda duration (per GB/sec) | $0.000015 | $0.00001275 | 15% | N/A | N/A | 
| Lambda requests (per 1M requests) | $0.20 | $0.20 | 0% | N/A | N/A | 

This example assumes one-year duration, partial upfront Savings Plans matching the configuration of your usage. Rates and discount percentages are hypothetical for simplification.

**Example scenarios**
+ [Scenario 1: Savings Plans apply to all usage](#scenario-1)
+ [Scenario 2: Savings Plans apply to some usage](#scenario-2)
+ [Scenario 3: Savings Plans apply to some usage, across products](#scenario-3)
+ [Scenario 4: Savings Plans and EC2 reserved instances apply to the usage](#scenario-4)
+ [Scenario 5: Multiple Savings Plans apply to the usage](#scenario-5)

### Scenario 1: Savings Plans apply to all usage
<a name="scenario-1"></a>

You purchase a one-year, partial upfront Compute Savings Plan with a $50.00/hour commitment.

Your Savings Plan covers all of your usage because multiplying each of your usages by the equivalent Compute Savings Plans is $47.13. This is still less than the $50.00/hour commitment.

Without Savings Plans, you would be charged at On-Demand rates in the amount of $59.10.

**Note**  
Each hour's commitment can only be used within that hour and cannot be carried over.

### Scenario 2: Savings Plans apply to some usage
<a name="scenario-2"></a>

You purchase a one-year, partial upfront Compute Savings Plan with a $2.00/hour commitment.

In any hour, your Savings Plans apply to your usage starting with the highest discount percentage (30 percent). 

 Your $2.00/hour commitment is used to cover approximately 2.9 units of this usage. The remaining 1.1 units are charged at On-Demand rates, resulting in $1.14 of On-Demand charges for `r5`.

The Fargate `m5.24xlarge` and Lambda usage are also charged at On-Demand rates, resulting in $55.10 of On-Demand charges. The total On-Demand charges for this usage are $56.24.

### Scenario 3: Savings Plans apply to some usage, across products
<a name="scenario-3"></a>

You purchase a one-year, partial upfront Compute Savings Plan with a $19.60/hour commitment.

Your Savings Plans are first applied to the `r5.4xlarge` because it has the highest discount percentage (30 percent). 

 Savings Plans apply to the Fargate usage next because it has the next highest discount percentage (25 percent). Savings Plans apply to memory (GB) before compute (vCPU) because it has the lower Savings Plans rate. The hourly commitment of $19.60 is met, and the remaining usage is charged at On-Demand rates.

The `m5.24xlarge` and Lambda usage on On-Demand charges are $32.70.

### Scenario 4: Savings Plans and EC2 reserved instances apply to the usage
<a name="scenario-4"></a>

You purchase a one-year, partial upfront Compute Savings Plan with an $18.20/hour commitment. You have two EC2 Reserved Instances (RI) for `r5.4xlarge` Linux shared tenancy in us-east-1.

First, the RI covers two of the `r5.4xlarge` instances. Then, the Savings Plans rate is applied to the remaining `r5.4xlarge` and the Fargate usage, which exhausts the hourly commitment of $18.20.

The `m5.24xlarge` and Lambda usage On-Demand charges are $32.70.

### Scenario 5: Multiple Savings Plans apply to the usage
<a name="scenario-5"></a>

You purchase a one-year, partial upfront EC2 Instance Family Savings Plan for the `r5` family in us-east-1 with a $3.00/hour commitment. You also have a one-year, partial upfront Compute Savings Plan with a $16.80/hour commitment.

Your EC2 Instance Family Savings Plan (`r5`, us-east-1) covers all of the `r5.4xlarge` usage because multiplying the usage by the EC2 Instance Family Savings Plan rate is $2.40. This is less than the $3.00/hour commitment.

Next, the Compute Savings Plan is applied to the Fargate usage because it has the highest discount percentage (25 percent) of the remaining usage. Savings Plans apply to memory (GB) before compute (vCPU) because memory has the lower Savings Plans rate. The hourly commitment of $16.80 is met, and the remaining usage is charged at On-Demand rates. 

The `m5.24xlarge` and Lambda usage On-Demand charges are $32.70.

For more information, see [Understanding Consolidated Bills](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/con-bill-blended-rates.html#cb_savingsplans) in the *AWS Billing and Cost Management User Guide*.

# Automating Savings Plans with Amazon EventBridge
<a name="automating-savingsplans-with-eventbridge"></a>

EventBridge helps you automate your AWS services and respond automatically to system events such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near-real time. Events are emitted on a best-effort basis. Based on the rules you create, EventBridge calls one or more target actions when an event matches the values that you specify in a rule. 

The actions that can be automatically triggered include the following:
+ Invoking an AWS Lambda function
+ Invoking Amazon EC2 Run Command
+ Relaying the event to Amazon Kinesis Data Streams
+ Activating an AWS Step Functions state machine
+ Notifying an Amazon SNS topic or an AWS SMS queue

Some examples of using CloudWatch Events with Savings Plans include:
+ Activating a Lambda function when a Savings Plans retires.
+ Notifying an Amazon SNS topic when a Savings Plans is marked `payment-failed` or `active`.

For more information, see the [Amazon CloudWatch Events User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/).

## Sample events from Savings Plans
<a name="SP-event-samples"></a>

This section includes example events from Savings Plans. Savings Plans generate two types of events. State change events that are triggered upon state changes, and state change alerts events that notify an upcoming state change that will occur in one or seven days.

### Savings Plans state change event
<a name="SP-state-change"></a>

Savings Plans state changes are generated when a Savings Plans transitions from one state to another. For example, `payment-pending` state changes to `active`, or an `active` state changes to `retired`.

```
{
    "version": "0",
    "id": "999cccaa-eaaa-0000-1111-123456789012",
    "detail-type": "Savings Plans State Change",
    "source": "aws.savingsplans",
    "account": "123456789012",
    "time": "2020-09-16T20:43:05Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:savingsplans::123456789012:savingsplan/07ec53ab-91c3-4ac5-bde6-79fd53192252"
    ],
    "detail": {
        "severity": "INFO",
        "previousState": "payment-pending",
        "currentState": "active",
        "message": "PaymentSuccessful"
    }
}
```

The state change event contains fields for resources (Savings Plans ARNs), previous state, current state, severity, and message. 


**Possible values for state change events**  

| previousState | currentState | severity | message | 
| --- | --- | --- | --- | 
| queued | payment-pending | INFO | `QueuedPurchaseFulfillment` | 
| queued | payment-failed | ERROR | `LimitExceededException` <br />or <br />`SavingsPlanOfferingNotAvailableException` | 
| queued | queued-deleted | INFO | `SavingsPlanQueuedDeleted` | 
| payment-pending | active | INFO | `PaymentSuccessful` | 
| payment-pending | payment-failed | ERROR | `LimitExceededException` <br />or <br />`PaymentUnsuccessful` | 
| active | retired | INFO | `SavingsPlanExpiration` | 
| active | pending-return | INFO | `SavingsPlanReturnRequested` | 
| pending-return | returned | INFO | `SavingsPlanReturnSuccessful` | 
| pending-return | active | ERROR | `SavingsPlanReturnUnsuccessful` | 

### Savings Plans state change alert event
<a name="SP-state-alert"></a>

Savings Plans state change alerts are generated when a Savings Plans transitions from the `queued` state to `active`, or `active` to `retired` in one or seven days. This is a proactive notification to alert you if any Savings Plans is retiring, or a queued state is fulfilled.

```
{
    "version": "0",
    "id": "999cccaa-eaaa-0000-1111-123456789012",
    "detail-type": "Savings Plans State Changange Alert",
    "source": "aws.savingsplans",
    "account": "123456789012",
    "time": "2020-09-16T00:15:00Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:savingsplans::123456789012:savingsplan/07ec53ab-91c3-4ac5-bde6-79fd53192252",
        "arn:aws:savingsplans::123456789012:savingsplan/19a9fa12-911a-18ed-9aa1-3a2615149a14"
    ],
    "detail": {
        "currentState": "queued",
        "nextState": "active",
        "remainingdays": "1",
        "nextStateChangeDate": "2020-09-17",
        "message": "queued savings plans will go to active state on 2020-09-17"
    }
}
```

The state change alert event contains fields for resources (Savings Plans ARNs), current state, next state, remaining days, next state change date, and message.


**Possible values for state change alert events**  

| currentState | nextState | remainingDays | message | 
| --- | --- | --- | --- | 
| queued | active | 1 | Queued Savings Plans will go to active state on `YYYY-MM-DD`. | 
| queued | active | 7 | Queued Savings Plans will go to active state on `YYYY-MM-DD`. | 
| active | retired | 1 | Active Savings Plans will go to retired state on `YYYY-MM-DD`. | 
| active | retired | 7 | Active Savings Plans will go to retired state on `YYYY-MM-DD`. | 

# Identity and Access Management for Savings Plans
<a name="identity-access-management"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. As an administrator, you can create roles under your AWS account that your users can assume. You control the permissions that your users have to perform tasks using AWS resources. You can use IAM at no additional charge.

By default, users don't have permissions for Savings Plans resources and operations. To allow users to manage Savings Plans resources, you must create a role to delegate permissions to a user. Follow the instructions in [Creating a role for a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.

## Policy structure
<a name="iam-policy-structure"></a>

An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows.

```
{
  "Statement":[{
    "Effect":"{{effect}}",
    "Action":"{{action}}",
    "Resource":"{{arn}}",
    "Condition":{
      "{{condition}}":{
        "{{key}}":"{{value}}"
        }
      }
    }
  ]
}
```

There are various elements that make up a statement:
+ **Effect:** The *effect* can be `Allow` or `Deny`. By default, users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.
+ **Action**: The *action* is the specific API action for which you are granting or denying permission.
+ **Resource**: The resource that's affected by the action. Some Amazon EC2 API actions allow you to include specific resources in your policy that can be created or modified by the action. To specify a resource in the statement, you need to use its Amazon Resource Name (ARN). For more information, see [Actions Defined by Savings Plans](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awssavingsplans.html#awssavingsplans-actions-as-permissions).
+ **Condition**: Conditions are optional. They can be used to control when your policy is in effect. For more information, see [Condition Keys for Savings Plans](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awssavingsplans.html#awssavingsplans-policy-keys).

## AWS managed policies
<a name="aws-managed-policies"></a>

The managed policies created by AWS grant the required permissions for common use cases. After you create a role that your user can assume, you can attach your policy to it, based on the access needed. Each policy grants access to all or some of the API actions for Savings Plans.

The following are the AWS managed polices for Savings Plans:
+ **AWSSavingsPlansFullAccess**–Grants full access to Savings Plans.
+ **AWSSavingsPlansReadOnlyAccess**–Grants read-only access to Savings Plans.

## Example policies
<a name="iam-policy-examples"></a>

In an IAM policy statement, you can specify any API action from any service that supports IAM. For Savings Plans, use the following prefix with the name of the API action: `savingsplans:`. For example:
+ `savingsplans:CreateSavingsPlan`
+ `savingsplans:DescribeSavingsPlans`

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": ["savingsplans:action1", "savingsplans:action2"]
```

You can also specify multiple actions using wildcards. For example, you can specify all Savings Plans API actions whose name begins with the word "Describe" as follows:

```
"Action": "savingsplans:Describe*"
```

To specify all Savings Plans API actions, use the \* wildcard as follows:

```
"Action": "savingsplans:*"
```

# Logging Savings Plans API Calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Savings Plans is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Savings Plans. CloudTrail captures all API calls for Savings Plans as events. The calls captured include calls from the AWS Management Console and code calls to the Savings Plans API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Savings Plans. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Savings Plans, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Savings Plans Information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Savings Plans, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Savings Plans, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Savings Plans actions are logged by CloudTrail and are documented in the [AWS Savings Plans API Reference](https://docs.aws.amazon.com/savingsplans/latest/APIReference/). For example, calling the `CreateSavingsPlan` action generates an entry in the CloudTrail logs.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or user role credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Savings Plans Log File Entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following is an example CloudTrail log entry for the `CreateSavingsPlan` action.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "[principalId]/[userName]",
        "arn": "arn:aws:sts::[accountId]:assumed-role/[userName]/",
        "accountId": "[accountId]",
        "accessKeyId": "[accessKeyId]",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-10-01T00:00:00Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "[principalId]",
                "arn": "arn:aws:iam::[accountId]:role/[userName]",
                "accountId": "[accountId]",
                "userName": "[userName]"
            }
        }
    },
    "eventTime": "2019-10-01T00:00:00Z",
    "eventSource": "savingsplans.amazonaws.com",
    "eventName": "CreateSavingsPlan",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "127.0.0.1",
    "userAgent": "[userAgent]",
    "requestParameters": {
        "commitment": "2.50",
        "savingsPlanOfferingId": "[savingsPlanOfferingId]",
        "clientToken": "[clientToken]",
        "tags": {
            "tag-key": "tag-value"
        }
    },
    "responseElements": {
        "savingsPlanId": "[savingsPlanId]"
    },
    "requestID": "[requestId]",
    "eventID": "[eventId]",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "[accountId]"
}
```

# Quotas and restrictions
<a name="sp-quotas"></a>

The following table describes the current quotas and restrictions within Savings Plans features.

## Savings Plans
<a name="sp-quotas-details"></a>



|  |  | 
| --- |--- |
| Maximum number of daily refresh requests for Savings Plans recommendations per consolidated billing family | 3 | 
| Maximum number of purchased Savings Plans you can return per calendar year, as long as within seven days of purchase in the same calender month | 10 per management account The management account used when returning the Savings Plan must be the same as the management account that was used to purchase the plan.  | 
| Maximum number of daily Savings Plans Purchase Analyzer runs per account ID | 20 | 

# Document history
<a name="doc-history"></a>

The following table describes the releases for this service.

| Change | Description | Date | 
| --- |--- |--- |
| [Savings Plans Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-analyzer.html) | Added a new feature to help you estimate the cost, coverage, and utilization impact of the Savings Plans you plan to purchase. | November 21, 2024 | 
| [Return Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html#return-sp) | Added a new feature to return any Savings Plan with an hourly commitment of $100 or less, purchased in the last seven days and in the same calendar month. | March 20, 2024 | 
| [Visual Savings Plans recommendations](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-recommendations.html#sp-rec-details-view) | Added a new feature to help you understand and validate your Savings Plans recommendations through new visual graphs. | July 24, 2023 | 
| [Refresh Savings Plans recommendations](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html#purchase-rec) | Added a new feature to refresh your Savings Plans recommendations in order to take your current Savings Plans inventory and latest usage data into account. | December 5, 2022 | 
| [Expanded AWS Fargate Savings Plans](#doc-history) | Savings Plans adds support for AWS Fargate usage on both Amazon ECS and Amazon EKS. | August 10, 2020 | 
| [Lambda service onboarded](#doc-history) | Lambda launched as a new service that is eligible for Savings Plans. | February 20, 2020 | 
| [Initial release](#doc-history) | This release introduces Savings Plans. | November 6, 2019 | 