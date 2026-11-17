# Service Quotas User Guide

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
+ [What is Service Quotas?](#intro)
+ [Customizing the Service Quotas dashboard](#getting-started)
+ [Viewing service quotas](#gs-request-quota)
+ [Requesting a quota increase](#request-quota-increase)
   + [Verifying your quota request](#quota-history)
+ [Managing Service Quotas resources with tags](#sq-tagging)
   + [Enabling the required permissions for tagging Service Quotas resources](#sq_tags_permissions)
   + [Managing Service Quotas tags](#sq_tags_managing-console)
   + [Controlling access using Service Quotas tags](#sq_tags_access)
+ [Service Quotas Automatic Management](#automatic-management)
   + [Getting started with Service Quotas Automatic Management](#getting-started-auto-mgmt)
   + [Viewing Service Quotas Automatic Management configuration](#viewing-automatic-management)
   + [Updating Service Quotas Automatic Management configuration](#updating-automatic-management)
   + [Excluding service quotas from Service Quotas Automatic Management](#excluding-quotas)
   + [Stopping Service Quotas Automatic Management](#stopping-automatic-management)
   + [Service Quotas Automatic Management frequently asked questions](#automatic-management-faq)
+ [Using Service Quotas request templates](#organization-templates)
+ [Security in Service Quotas](#security)
   + [Data protection in Service Quotas](#data-protection)
   + [Logging and monitoring Service Quotas](#monitoring-overview)
      + [Logging Service Quotas API calls using AWS CloudTrail](#logging-using-cloudtrail)
         + [Service Quotas Automatic Management AWS CloudTrail logs](#auto-mgmt-ct-logs)
      + [Service Quotas and Amazon CloudWatch alarms](#configure-cloudwatch)
   + [Identity and access management in Service Quotas](#identity-access-management)
      + [AWS managed policies for Service Quotas](#security-iam-awsmanpol)
   + [Integrating event-driven applications with Service Quotas using Amazon EventBridge](#eventbridge-integration)
   + [Compliance validation for Service Quotas](#SERVICE-compliance)
   + [Resilience in Service Quotas](#disaster-recovery-resiliency)
   + [Infrastructure Security in Service Quotas](#infrastructure-security)
+ [Service quotas for Service Quotas](#reference_limits)
+ [Service Quotas Document history](#document-history)

-----



# What is Service Quotas?
<a name="intro"></a>

With Service Quotas, you can view and manage your quotas for AWS services from a central location. Quotas, also referred to as limits in AWS services, are the maximum values for the resources, actions, and items in your AWS account. Each AWS service defines its quotas and establishes default values for those quotas. If your business needs aren't met by the default limit of service resources or operations that apply to an AWS account, resource, or an AWS Region, you might need to increase your service quota values. Service Quotas enables you to look up your service quotas and to request increases. Support might approve, deny, or partially approve your requests.

**Topics**
+ [Features of Service Quotas](#features)
+ [Terminology in Service Quotas](#intro_getting-started)
+ [Accessing Service Quotas](#access)

## Features of Service Quotas
<a name="features"></a>

Service Quotas provides the following features:

**View your service quotas**  
The Service Quotas console provides quick access to the AWS default quota values for your account, across all AWS Regions. When you select a service in the Service Quotas console, you see the service's quotas and if that quota is adjustable at the AWS account level. *Applied quotas* are overrides, or increases for a specific quota, over the AWS default value. 

**Request a service quota increase**  
To see if a quota is adjustable, go into the console, navigate to AWS services, and select the service from the list. From the service's details page, view the **Adjustable** column.   
Each adjustable quota says at which level the quota can be increased. For service quotas that are adjustable at the *account* level, you can use Service Quotas to request a quota increase.   
You can also increase certain quotas at the *resource* level.   
To request a quota increase in the Service Quotas console, select the service and the specific quota, and then choose **Request quota increase**. Increases do take some time to review, process, and approve. You can also use Service Quotas API operations or the AWS CLI tools to request service quota increases. 

**View current utilization of resources**  
After your account becomes active for a period of time, you can view a graph of your resource utilization.

**Service Quotas Automatic Management**  
[Service Quotas Automatic Management](#automatic-management), once started, allows AWS to monitor service quotas usage and send you notifications when quotas before you run out of your allocated quotas.

## Terminology in Service Quotas
<a name="intro_getting-started"></a>

The following terms are important for understanding Service Quotas and how it works.

**service quota**  
The maximum number of service resources or operations that apply to an AWS account or an AWS Region. The number of AWS Identity and Access Management (IAM) roles per account is an example of an account-based quota. The number of virtual private clouds (VPCs) per Region is an example of a Region-based quota. To determine whether a service quota is Region-specific, check the description of the service quota.

**adjustable value**  
A quota value that can be increased.

**applied quota**  
The updated quota value after a quota increase.

**default value**  
The initial quota value established by AWS.

**global quota**  
A service quota applied at an account level. Global quotas are available in all AWS Regions. You can request an increase to a global quota only from US East (N. Virginia) for Public AWS partition, AWS GovCloud (US-West) for AWS GovCloud (US) Regions, and China (Beijing) for AWS China Regions. 

**usage**  
The number of resources or operations in use for a service quota.

**utilization**  
The percentage of a service quota in use. For example, if the quota value is 200 resources and 150 resources are in use, then the utilization is 75 percent.

**quota context info**  
A structure that describes the context for a resource-level quota. For resource-level quotas, such as `Instances per OpenSearch Service Domain`, you can apply the quota value at the resource-level for each OpenSearch Service Domain in your AWS account. Together the attributes of this structure help you understand how the quota is implemented by AWS and how you can manage it.

**context ID**  
Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or \*. If the value is an ARN, the quota value applies to that resource. If the value is \*, then the quota value applies to all resources of that specific type.

**context scope**  
Specifies the scope to which the quota value is applied.

**context scope type**  
Specifies the resource type to which the quota can be applied.

**quota applied at level**  
Filters an API response to return applied quota values at either the account level, resource level, or all levels.

**quota requested at level**  
Filters an API response to return quota requests at either the account level, resource level, or all levels.

## Accessing Service Quotas
<a name="access"></a>

You can work with Service Quotas in the following ways:

**AWS Management Console**  
[The Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard) is a browser-based interface that you can use to view and manage your service quotas. You can perform almost any task that's related to your service quotas by using the console. You can access Service Quotas from any AWS Management Console page by choosing it on the top navigation bar, or by searching for Service Quotas in the AWS Management Console.

**AWS Command Line Interface tools**  
By using the AWS Command Line Interface tools, you can issue commands at your system's command line to perform Service Quotas and other AWS tasks. This can be a faster and more convenient approach than using the console. The command line tools also are useful if you want to build scripts that perform AWS tasks.  
AWS provides two sets of command line tools: the [AWS Command Line Interface](https://aws.amazon.com/cli/)  and the [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/). For information about installing and using the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). For information about installing and using the Tools for Windows PowerShell, see the [AWS Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/).  
You need AWS CLI version 2.13.20 or higher to view and manage resource-level quotas such as `Instances per domain` for Amazon OpenSearch Service.

**AWS SDKs**  
The AWS SDKs consist of libraries and sample code for various programming languages and platforms (for example, [Java](https://aws.amazon.com/sdk-for-java/), [Python](https://aws.amazon.com/sdk-for-python/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [.NET](https://aws.amazon.com/sdk-for-net/), [iOS and Android](https://aws.amazon.com/mobile/resources/), and [others](https://aws.amazon.com/tools/#sdk)). The SDKs include tasks such as cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the AWS SDKs, including how to download and install them, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/#SDKs).

# Customizing the Service Quotas dashboard
<a name="getting-started"></a>

When you open the Service Quotas console, the dashboard displays cards for up to nine AWS services. Each card lists the number of service quotas for that AWS service. Choosing a card opens a page displaying the quotas for the service. You can modify which services appear on the dashboard.

**To modify the dashboard service cards**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. On the dashboard, choose **Modify dashboard cards**.

1. The services that are currently selected appear on the right. If you have selected nine services, you must remove a service before you can add a different service. For each service that you don't want on the dashboard, choose **Remove**.

1. To add a service to the dashboard, select it from **Choose services**.

1. When you have finished adding and removing services, choose **Save**.

**Next steps**
+ [View the AWS default value and applied values](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) of a particular quota. 
+ For adjustable quotas, you can [request a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html). 

# Viewing service quotas
<a name="gs-request-quota"></a>

**Note**  
If you are searching for service quotas for a specific AWS service, review [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the *AWS General Reference guide*. 

Service Quotas enables you to review the AWS default value and applied values of a particular *quota*. Certain resource-level quotas, such as `Instances per domain` for Amazon OpenSearch Service, also display applied quota values per resource. Refer to [Terminology in Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html#intro_getting-started) for detailed definitions of these values. 

Your account's actual quota value may be less than the AWS default quota value if you recently created the account, or if you use the account minimally. 

------
#### [ AWS Management Console ]

**To view the quotas for a service**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, choose **AWS services**.

1. Select an AWS service from the list, or enter the name of the service in the search field. 

   The console displays details for the selected service's quota, including the **quota name**, **applied quota value**, **AWS default quota**, **utilization**, and if the quota is **adjustable** at the account-level or resource-level. 

   If the applied quota value or utilization is not available, the console displays **Not available**. You can request your applied quota value through the Support Center Console.

1. Choose a specific **quota name** to view the Details page, which displays that quota's **description**, **quota code**, **quota ARN**, **utilization**, **applied quota value**, and the **AWS default quota**. 

   If applicable, the Details page also displays any **resource-level quota**, **alarms**, **quota increase request history**, and any of the quota's **tags**. 

------
#### [ AWS CLI ]

**Viewing default quota values**

View the default values for the quotas for a specific AWS service.
+ Call the [ListDefaultServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListDefaultServiceQuotas.html) operation with a service code. If you don't have the service code, you can get a list of supported services with the [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html) operation. The response includes the `ServiceCode` and `ServiceName` for each service. The `ServiceCode` for Amazon OpenSearch Service is `es`. The following CLI example retrieves default values for Amazon OpenSearch Service quotas.

  ```
  $ aws service-quotas list-aws-default-service-quotas \
          --service-code es \
  {
      "Quotas": [
          {
              "QuotaName": "Domains per Region",
              "Adjustable": true,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
              "Value": 100.0,
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-076D529E",
              "Unit": "None",
          },
          {
              "QuotaName": "Dedicated master instances per domain",
              "Adjustable": false,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-AE676A72",
              "Value": 5.0,
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-AE676A72",
              "Unit": "None",
          },
          {
              "QuotaName": "Warm instances per domain",
              "Adjustable": false,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-1F053E6F",
              "Value": 150.0,
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-1F053E6F",
              "Unit": "None",
          },
          {
              "QuotaName": "Instances per domain",
              "Adjustable": true,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
              "Value": 80.0,
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-6408ABDE",
              "Unit": "None",
              "QuotaContext": {
                                "ContextScope": "RESOURCE",
                                "ContextScopeType": "AWS::OpenSearchService::Domain",
               }
          }
      ]
  }
  ```

**Viewing applied quota values**

View the applied quota values for a specified AWS service. For some quotas, only the default values are available. If the applied quota value isn't available for a quota, the quota is not returned in the response. If this happens, contact Support for the applied quota value.
+ Call the [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html) operation with a service code. You can choose to retrieve all applied quota values either at the account-level, resource-level, or all levels by passing `ACCOUNT`, `RESOURCE`, or `ALL` respectively as the value for the parameter `QuotaAppliedAtLevel`.

  The following CLI example retrieves all quota values applied at the account-level for OpenSearch Service. 

  ```
  $ aws service-quotas list-service-quotas \
          --service-code es \
          --quota-applied-at-level ACCOUNT
  {
      "Quotas": [
          {
              "QuotaName": "Domains per Region",
              "Adjustable": true,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
              "Value": 100.0,
              "QuotaAppliedAtLevel": "ACCOUNT",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-076D529E",
              "Unit": "None",
          },
          {
              "QuotaName": "Dedicated master instances per domain",
              "Adjustable": false,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-AE676A72",
              "Value": 5.0,
              "QuotaAppliedAtLevel": "ACCOUNT",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-AE676A72",
              "Unit": "None",
          },
          {
              "QuotaName": "Warm instances per domain",
              "Adjustable": false,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-1F053E6F",
              "Value": 150.0,
              "QuotaAppliedAtLevel": "ACCOUNT",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-1F053E6F",
              "Unit": "None",
          },
          {
              "QuotaName": "Instances per domain",
              "Adjustable": true,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
              "Value": 80.0,
              "QuotaAppliedAtLevel": "ACCOUNT",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-6408ABDE",
              "Unit": "None",
              "QuotaContext": {
                                "ContextScope": "RESOURCE",
                                "ContextScopeType": "AWS::OpenSearchService::Domain",
                                "ContextId": "*"
               }
          }
      ]
  }
  ```

------

# Requesting a quota increase
<a name="request-quota-increase"></a>

For adjustable quotas, you can request a quota increase at the *account-level* or the *resource-level*. Smaller increases are usually automatically approved while larger requests are submitted to Support. Larger increase requests take time to review, process, approve, and deploy. You can track your request case in the Support console. 

**Note**  
Quota increase requests don't receive priority support. Support can approve, deny, or partially approve your requests. If you have an urgent quota request, or if your quota increase request is denied, contact Support for assistance.

## Using the AWS Management Console to request an increase
<a name="quota-console-increase"></a>

Increase your quotas at the account or resource level in the [Getting Started with the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html).

**To request a service quota increase**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, choose **AWS services**.

1. Choose an AWS service from the list, or enter the name of the service in the search box.

1. If the quota is adjustable, you can request a quota increase at either the account-level or resource-level based on the value listed in the **Adjustability** column. 
   + **Account-level** – Request a quota increase at the account-level for an account-level quota such as `Domains per Region` for Amazon OpenSearch Service. To do so, select the quota from the list and choose **Request increase at account-level**.
   + **Resource-level** – Request a quota increase for a specific resource for a resource-level quota such as `Instances per domain` for Amazon OpenSearch Service. To do so, choose the quota name to view additional information about the quota. Under the **Resource-level quotas** section, select the resource for which you want to increase the quota value, and choose the **Request increase at resource-level** button. 

1. For **Increase quota value**, enter the new value. The new value must be greater than the current value.

1. Choose **Request**.

1. To view any pending or recently resolved requests in the console, navigate to the **Request history** tab from the service's details page, or choose **Dashboard** from the navigation pane. For pending requests, choose the status of the request to open the request receipt. The initial status of a request is **Pending**. After the status changes to **Quota requested**, you'll see the case number with Support. Choose the case number to open the ticket for your request.

## Using the AWS CLI to request a quota increase
<a name="quota-cli-increase"></a>

Requesting a quota increase using the AWS CLI requires you to provide Service Quotas with the necessary permission to create a support case on your behalf. You can provide this permission by attaching the [AWS managed policy](#predefined-policies) `ServiceQuotasFullAccess` to your IAM principal or adding `iam:CreateServiceLinkedRole` [to your existing IAM policy.](#iam-policies) 

------
#### [ Account-level increase request AWS CLI ]

**To request a quota increase at the account-level**

The `RequestServiceQuotaIncrease` operation, which submits the request, requires the quota code for the quota. So begin by getting the quota code.

The following example commands show how to request a quota increase at the account-level for the Amazon OpenSearch Service.

1. Get the list of services supported by Service Quotas with the [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html) operation. The response includes the `ServiceCode` and `ServiceName` for each service. The `ServiceCode` for Amazon OpenSearch Service is `es`.

1. Get the list of Amazon OpenSearch Service quotas and their corresponding applied quota values at the account-level by calling the [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html) operation with request parameters `ServiceCode` as `es`, and `QuotaAppliedAtLevel` as `ACCOUNT`. The response includes the `QuotaName`, `QuotaCode`, `Value`, and `QuotaAppliedAtLevel` for each quota of the Amazon OpenSearch Service that is applied at the account-level. If the value in the `QuotaAppliedAtLevel` field is `ACCOUNT`, then the `Value` represents the Applied quota value at the account-level. The following CLI example retrieves the quota code for a OpenSearch Service quota.

   ```
   $ aws service-quotas list-service-quotas \
           --service-code es \  
           --quota-applied-at-level ACCOUNT
   {
       "Quotas": [
           {
               "QuotaName": "Domains per Region",
               "Adjustable": true,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
               "Value": 100.0,
               "QuotaAppliedAtLevel": "ACCOUNT",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-076D529E",
               "Unit": "None",
           },
           {
               "QuotaName": "Dedicated master instances per domain",
               "Adjustable": false,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-AE676A72",
               "Value": 5.0,
               "QuotaAppliedAtLevel": "ACCOUNT",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-AE676A72",
               "Unit": "None",
           },
           {
               "QuotaName": "Warm instances per domain",
               "Adjustable": false,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-1F053E6F",
               "Value": 150.0,
               "QuotaAppliedAtLevel": "ACCOUNT",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-1F053E6F",
               "Unit": "None",
           },
           {
               "QuotaName": "Instances per domain",
               "Adjustable": true,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
               "Value": 80.0,
               "QuotaAppliedAtLevel": "ACCOUNT",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-6408ABDE",
               "Unit": "None",
               "QuotaContext": {
                                "ContextScope": "RESOURCE",
                                "ContextScopeType": "AWS::OpenSearchService::Domain",
                                "ContextId": "*"
           }
       ]
   }
   ```

1. Next, call the [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html) operation and specify the `QuotaCode` in the request parameter.

   The following example requests an increase at the account-level in the `Instances per domain` quota to `100`. It uses the required quota code, `L-6408ABDE`, to identify the quota. If the command completes successfully, the `Status` field in the response displays the current status of the request. The `QuotaRequestedAtLevel` field in the response specifies that this request applies to the account-level.
**Note**  
You can't request a quota increase at the account-level for a resource-level quota through the AWS CLI. This operation results in the creation of a support case where you can provide the ARN to specify the resource on which the new quota value should apply. However, the `Instances per domain` quota for Amazon OpenSearch Service is an exception. 

   ```
   $ aws service-quotas request-service-quota-increase \
           --service-code es \
           --quota-code L-6408ABDE \
           --desired-value 100
   {
       "RequestedQuota": {
           "QuotaName": "Instances per domain",
           "Status": "PENDING",
           "DesiredValue": 100,
           "Created": 1580446904.067,
           "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
           "ServiceName": "Amazon OpenSearch Service",
           "GlobalQuota": false,
           "ServiceCode": "es",
           "QuotaCode": "L-6408ABDE",
           "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
           "QuotaRequestedAtLevel": "ACCOUNT"
           "Id": "a12345",
           "Unit": "None"
           "QuotaContext": {
                            "ContextId": "*"
                            "ContextScopeType": "AWS::OpenSearchService::Domain",
                            "ContextScope": "RESOURCE",
           }
       }
   }
   ```

1. To get the updated status of the request, use the [GetRequestedServiceQuotaChange](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetRequestedServiceQuotaChange.html), [ListRequestedServiceQuotaChangeHistory](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.html) or [ListRequestedServiceQuotaChangeHistoryByQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.html) operations.

------
#### [ Resource-level quota increase request AWS CLI ]

**To request a quota increase at the resource-level**

The `RequestServiceQuotaIncrease` operation, which submits the request, requires the quota code for the quota. So begin by getting the quota code. To request a quota increase for a specific resource, use the Amazon Resource Name (ARN) `ResourceARN` as the value for the `ContextId` parameter when you make your request.

The following example commands show how to request a resource-level quota increase for the OpenSearch Service.

1. Get the list of services supported by Service Quotas with the [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html) operation. The response includes the `ServiceCode` and `ServiceName` for each service. The `ServiceCode` for Amazon OpenSearch Service is `es`.

1. Get the list of Amazon OpenSearch Service quotas and their corresponding applied quota values at the resource-level by calling the [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html) operation with request parameters `ServiceCode` as `es`, and `QuotaAppliedAtLevel` as `RESOURCE`. The response includes the `QuotaName`, `QuotaCode`, `Value`, and `QuotaAppliedAtLevel` for each quota of the Amazon OpenSearch Service that is applied at the resource-level. If the value in the `QuotaAppliedAtLevel` field is `RESOURCE`, then the `Value` represents the Applied quota value at the resource-level. In this case, the response for this quota will also contain the `QuotaContext` structure which further specifies the `ContextId` or the ARN to which the quota value is applied. The following CLI example retrieves the quota code for a OpenSearch Service quota.

   ```
   $ aws service-quotas list-service-quotas \
           --service-code es \
           --quota-applied-at-level RESOURCE
   {
       "Quotas": [
            {
               "QuotaName": "Instances per domain",
               "Adjustable": true,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
               "Value": 100.0,
               "QuotaAppliedAtLevel": "RESOURCE",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-6408ABDE",
               "Unit": "None",
               "QuotaContext": {
                                "ContextScope": "RESOURCE",
                                "ContextScopeType": "AWS::OpenSearchService::Domain",
                                "ContextId": "arn:aws:esus-east-1:123456789012:domain/opensearch-domain-1",
                       }
          },
          {
          "QuotaName": "Instances per domain",
               "Adjustable": true,
               "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
               "Value": 100.0,
               "QuotaAppliedAtLevel": "RESOURCE",
               "ServiceName": "Amazon OpenSearch Service",
               "GlobalQuota": false,
               "ServiceCode": "es",
               "QuotaCode": "L-6408ABDE",
               "Unit": "None",
               "QuotaContext": {
                                "ContextScope": "RESOURCE",
                                "ContextScopeType": "AWS::OpenSearchService::Domain",
                                "ContextId": "arn:aws:esus-east-1:123456789012:domain/opensearch-domain-2",
                       }
            }           
       ]
   }
   ```

1. Next, call the [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html) operation and specify the `ServiceCode`, `QuotaCode`, `ContextId`, and `DesiredValue` request parameters.

   The following example requests an increase in the `Instances per domain` quota to `100` for a specific Amazon OpenSearch Service domain with the ARN as arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1. If the command completes successfully, the `Status` field in the response displays the current status of the request. `QuotaRequestedAtLevel` field in the response contains the value `RESOURCE` which specifies that this request is for a specific resource.

   ```
   $ aws service-quotas request-service-quota-increase \
           --service-code es \
           --quota-code L-6408ABDE \
           --desired-value 200 \
           --context-id arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1
   {
       "RequestedQuota": {
           "QuotaName": "Instances per domain",
           "Status": "PENDING",
           "DesiredValue": 200.0,
           "Created": 1580446904.067,
           "QuotaArn": "arn:aws:servicequotas:us-east-1:123456789012:es/L-6408ABDE",
           "ServiceName": "Amazon OpenSearch Service",
           "GlobalQuota": false,
           "ServiceCode": "es",
           "QuotaCode": "L-6408ABDE",
           "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
           "QuotaRequestedAtLevel": "RESOURCE",
           "Id": "a12345",
           "Unit": "None"
           "QuotaContext": {
                            "ContextId": "arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1"
                            "ContextScopeType": "AWS::OpenSearchService::Domain",
                            "ContextScope": "RESOURCE",
                }            
       }
   }
   ```

1. To get the updated status of the request, use the [GetRequestedServiceQuotaChange](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetRequestedServiceQuotaChange.html), [ListRequestedServiceQuotaChangeHistory](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.html) or [ListRequestedServiceQuotaChangeHistoryByQuota](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistoryByQuota.html) operations.

------

After the request is resolved, the **Applied quota value** for the quota is set to the new value.

## Verifying your quota request
<a name="quota-history"></a>

Verify your quota request by viewing the request history history in the Service Quotas console. The console displays all open quota requests and requests closed in the last year.

**Note**  
Some AWS services may only be available in certain AWS Regions. If you have quota increase requests in different Regions, be sure to select the appropriate Region first. 

------
#### [ Using the AWS Management Console ]

**To view the quota request history**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. To view any pending or recently resolved requests, choose **Quota request history** from the navigation pane.

The **Recent quota increase requests** panel displays information about your open recent quota increase requests and any requests closed within the last year.
+ **Service** – Displays the service name selected for the request.
+ **Quota name** – Displays the quota name selected for the quota increase.
+ **Status** – Displays the status of a request for a quota increase.

  You may see the following status types:
  + **Pending** – Quota increase request is under review by AWS.
  + **Case opened** – Service Quotas has opened a support case to process the request.
  + **Approved** – Quota increase request is approved.
  + **Rejected** – Quota increase request can't be approved by Service Quotas. Contact Support for more details.
  + **Case closed** – The support case associated with this request was closed. View the support case correspondence for more information.
  + **Request not valid** – Service Quotas can't process your resource-level quota increase request because the `ResourceARN` specified as part of the `ContextId` attribute is not valid.
+ **Requested quota value** – The increased quota value you requested for the quota.
+ **Request date** – The date you requested the quota increase.
+ **Last updated date** – The last date the request received an update.

View details about a service, quota name, and status in the **Quota request history** table by choosing one of the entries.

------
#### [ Using AWS CLI ]

**To view the quota request history**
+ The `ListRequestedServiceQuotaChangeHistory` operation, which submits the request, requires a `QuotaRequestedAtLevel` parameter. The following CLI example is for all resource and account level requests.

  ```
  $ aws service-quotas list-requested-service-quota-change-history \
          --quota-applied-at-level ALL
  {
      "RequestedQuotas": [
          {
              "QuotaName": "Instances per domain",
          "Status": "PENDING",
          "DesiredValue": 200.0,
          "Created": 1580446904.067,
          "QuotaArn": "arn:aws:servicequotas:us-east-1:123456789012:es/L-6408ABDE",
          "ServiceName": "Amazon OpenSearch Service",
          "GlobalQuota": false,
          "ServiceCode": "es",
          "QuotaCode": "L-6408ABDE",
          "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
          "QuotaRequestedAtLevel": "RESOURCE",
          "Id": "a12345",
          "Unit": "None"
          "QuotaContext": {
                           "ContextId": "arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-1"
                           "ContextScopeType": "AWS::OpenSearchService::Domain",
                           "ContextScope": "RESOURCE"           
          }
        },
        {
          "QuotaName": "Instances per domain",
          "Status": "PENDING",
          "DesiredValue": 200.0,
          "Created": 1580446904.067,
          "QuotaArn": "arn:aws:servicequotas:us-east-1:123456789012:es/L-6408ABDE",
          "ServiceName": "Amazon OpenSearch Service",
          "GlobalQuota": false,
          "ServiceCode": "es",
          "QuotaCode": "L-6408ABDE",
          "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
          "QuotaRequestedAtLevel": "RESOURCE",
          "Id": "a12345",
          "Unit": "None"
          "QuotaContext": {
                           "ContextId": "arn:aws:es:us-east-1:123456789012:domain/opensearch-domain-2",
                           "ContextScopeType": "AWS::OpenSearchService::Domain",
                           "ContextScope": "RESOURCE" 
          }
        },
        {
              "QuotaName": "Domains per Region",
              "Status": "PENDING",
              "DesiredValue": 120.0,
              "Created": 1580446904.067,
              "Adjustable": true,
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-076D529E",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-076D529E",
              "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}"
              "QuotaRequestedAtLevel": "ACCOUNT",
              "Id": "a123456",
              "Unit": "None",
        },
        {
              "QuotaName": "Instances per domain",
              "Status": "PENDING"
              "DesiredValue": 300.0,
              "Created": 1580446904.067,            
              "QuotaArn": "arn:aws:servicequotas:us-east-1::123456789012:es/L-6408ABDE",
              "ServiceName": "Amazon OpenSearch Service",
              "GlobalQuota": false,
              "ServiceCode": "es",
              "QuotaCode": "L-6408ABDE",
              "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}"
              "QuotaRequestedAtLevel": "ACCOUNT",
              "Id": "a1234567",
              "Unit": "None",
              "QuotaContext": {
                               "ContextId": "*",                                
                               "ContextScopeType": "AWS::OpenSearchService::Domain",
                               "ContextScope": "RESOURCE"
                           }
        }
      ]
  }
  ```

------

# Managing Service Quotas resources with tags
<a name="sq-tagging"></a>

You can use tags to categorize resources by purpose, owner, environment, or other criteria. A *tag* is a custom attribute label that you add to an AWS resource to make it easier to identify, organize, and search for resources. Each tag includes two parts: 
+ A **tag key**, such as `CostCenter`, `Environment`, or `Project`. Tag keys are case sensitive.
+ A **tag value**, such as `111122223333` or `Production`. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

Tags help you do the following:
+ Identify and organize your AWS resources. Many services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related.
+ Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly cost allocation report to you. For more information, see [Use cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the [AWS Billing User Guide](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ Control access to your AWS resources. For more information, see [Controlling access using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the * [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)*. 

**Topics**
+ [Service Quotas resources that support tagging](#sq-supported-resources)
+ [Tag restrictions](#sq-tagging-restrictions)
+ [Enabling the required permissions for tagging Service Quotas resources](#sq_tags_permissions)
+ [Managing Service Quotas tags](#sq_tags_managing-console)
+ [Controlling access using Service Quotas tags](#sq_tags_access)

## Service Quotas resources that support tagging
<a name="sq-supported-resources"></a>

Service Quotas supports tagging the **Applied quotas** resource. An applied quota is a quota that you requested an increase for, *and* the increase was approved by Support.

**Important**  
You can only tag quotas if they have an applied quota value. Quotas with default quota values cannot be tagged.  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are not intended to be used for private or sensitive data.

## Tag restrictions
<a name="sq-tagging-restrictions"></a>

Restrictions apply to tags on Service Quotas resources, including:
+ Maximum number of tags that you can assign to a resource – 50 
+ Maximum tag key length – 128 Unicode characters 
+ Maximum tag value length – 256 Unicode characters 
+ Valid characters for tag key and value – a-z, A-Z, 0-9, space, and the following characters: \_ . : / = \+ - and @
+ Tag keys and values are case sensitive.
+ Don't use `aws:` as a prefix for tag keys. It is reserved for AWS use.

## Enabling the required permissions for tagging Service Quotas resources
<a name="sq_tags_permissions"></a>

You must configure permissions to allow your users or roles to manage tags in Service Quotas. The permissions that are required to administer tags generally correspond to the API operations for the task.

To allow IAM principles, such as roles or users, to use Service Quotas for tagging operations, attach the [`ServiceQuotasReadOnlyAccess`AWS managed policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ServiceQuotasReadOnlyAccess$jsonEditor) to the principals. 


| Task | Required permission | 
| --- | --- | 
| Add tags to applied quotas | `servicequotas:ListTagsForResource`<br />`servicequotas:TagResource`<br /> | 
| View tags for an applied quota | `servicequotas:ListTagsForResource`<br /> | 
| Remove existing tags from an applied quota | `servicequotas:UntagResource`<br /> | 
| Edit existing tag values for applied quotas | `servicequotas:ListTagsForResource`<br />`servicequotas:TagResource`<br />`servicequotas:UntagResource`<br /> | 

## Managing Service Quotas tags
<a name="sq_tags_managing-console"></a>

You can manage Service Quotas tags by using the AWS Management Console, the AWS CLI, or the AWS API.

### Managing tags from the AWS Management Console
<a name="sq_tags_managing-console"></a>

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation page, choose **AWS services**.

1. Choose an AWS service from the list, or enter the name of the service in the search box.

1. Choose a service that has a value in the **Applied quota value** column.

1. In the **Tags** section, choose **Manage tags**. This option is not available for quotas that don't have an applied quota value.

1. You can add or remove tags, or you can edit tag values for existing tags. Enter a name for the tag in **Key**. You can add an optional value for the tag in **Value**.

1. After making all of your changes to tags, choose **Save changes**.

If the operation is successful, you return to the quota details page where you can verify your changes. If the operation fails, follow the instructions in the error message to resolve it.

### Managing Service Quotas tags using the AWS CLI or API
<a name="sq_tags_managing-cli"></a>

To manage Service Quotas tags using the CLI or API, choose a management task and use the corresponding CLI command or API call. 


| Tag management task | CLI command | API call | 
| --- | --- | --- | 
| Add tags to applied quotas | `aws service-quotas [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/tag-resource.html)` | [`TagResource`](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_TagResource.html)<br /> | 
| View tags for an applied quota | `aws service-quotas [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-tags-for-resource.html)` | `[ListTagsForResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListTagsForResource.html)`<br /> | 
| Delete existing tag values for applied quotas | `aws service-quotas [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/untag-resource.html)` | `[UntagResource](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_UntagResource.html)`<br /> | 

## Controlling access using Service Quotas tags
<a name="sq_tags_access"></a>

To control access to Service Quotas resources based on tags, you provide the tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about these condition keys, see [Controlling access to AWS resources using resource tags ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

For example, when you attach the following policy to an AWS Identity and Access Management (IAM) role or user, that principal can request an increase to Amazon Athena applied quotas that are tagged with the tag key **Owner** and tag value **admin**.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["servicequotas:RequestServiceQuotaIncrease"],
            "Resource": "arn:aws:servicequotas:*:*:athena/*",
            "Condition": {
                "StringEquals": {"aws:ResourceTag/Owner": "admin"}
            }
        }
    ]
}
```

------

You can also attach tags to IAM principals to use attribute-based access control (ABAC). ABAC is an authorization strategy that defines permissions based on attributes. Tagging entities and resources is the first step of ABAC. Then you design ABAC policies to allow operations when the principal's tag matches the tag on the resource that they're trying to access. ABAC is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome.

For more information about ABAC, see [What is ABAC?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

# Service Quotas Automatic Management
<a name="automatic-management"></a>

Service Quotas Automatic Management monitors your service quotas usage and notifies you before you run out of your allocated quotas. You gain better visibility and proactive awareness, enabling you to run your applications without interruptions.Key features of Automatic Management

**Opt-in options**  
Enable Automatic Management using the Service Quotas console, AWS CLI, or API.

**Usage notifications**  
Receive notifications when quota usage reaches the following utilization thresholds:  
+ 80% utilization
+ 95% utilization

**Auto-Adjust**  
Automatic Management can make a service quota increase request on your behalf with Notify and Auto-Adjust mode.

**Notification channels**  
Configure notifications through multiple channels:  
+ AWS Console Mobile Application
+ Email
+ Slack

**Integration options**  
+ Subscribe to [Amazon EventBridge events](#eventbridge-integration) for automation workflows
+ View notifications in the [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) dashboard

**Topics**
+ [Service Quotas Automatic Management modes](#automatic-management-modes)
+ [Service Quotas Automatic Management permissions](#permissions)
+ [Getting started with Service Quotas Automatic Management](#getting-started-auto-mgmt)
+ [Viewing Service Quotas Automatic Management configuration](#viewing-automatic-management)
+ [Updating Service Quotas Automatic Management configuration](#updating-automatic-management)
+ [Excluding service quotas from Service Quotas Automatic Management](#excluding-quotas)
+ [Stopping Service Quotas Automatic Management](#stopping-automatic-management)
+ [Service Quotas Automatic Management frequently asked questions](#automatic-management-faq)

## Service Quotas Automatic Management modes
<a name="automatic-management-modes"></a>

There are two modes with Automatic Management: Notify and Auto-Adjust and Notify Only. Both modes send you notifications about supported service quotas usage to the [AWS Health dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-dashboard-status.html).

The following table highlights different features for each mode.


| Mode | Creates service quota increase request when service usage exceeds 80% of utilization threshold | Creates service quota increase request when service usage exceeds 95% of utilization threshold | Sends notifications when your service increase request fails | Monitors service quotas usage and sends notifications when approaching 80% service utilization threshold | Monitors service quotas usage and sends notifications when approaching 95% service utilization thresholds  | 
| --- | --- | --- | --- | --- | --- | 
| Notify and Auto Adjust | Yes | Yes | Yes | No | Yes | 
| Notify Only | No | No | No | Yes | Yes | 

### How service quota increase requests work with Notify and Auto-Adjust mode
<a name="quota-increase-requests"></a>

Automatic Management monitors your service usage and sends these metrics to CloudWatch. When your usage for [adjustable services quotas](#intro_getting-started) are greater than the [utilization threshold](#notification-thresholds), Automatic Management generates a service quota increase for that quota.

#### Auto-adjust vs manual quota increase requests
<a name="auto-adjust-vs-manual"></a>

Auto-adjust requests are processed differently than manual quota increase requests:

Auto-adjust requests  
+ Use automated processing without creating a support case
+ Only work for quotas that support automated approval
+ May have more restrictive approval criteria
+ Do not provide detailed rejection reasons when not approved

Manual requests  
+ Go through AWS Support with human review
+ Can consider additional context and account-specific factors
+ Provide detailed feedback through the support case process
+ May be approved even when auto-adjust requests for the same quota are not

**Important**  
Auto-adjustable status does not guarantee approval. If an auto-adjust request is not approved, you should submit a manual quota increase request through the Service Quotas console or API.

## Service Quotas Automatic Management permissions
<a name="permissions"></a>

To start Automatic Management, you'll need permissions to view AWS Health notifications and use the Service Quotas console, AWS CLI, or API actions. 

**Permissions to use Automatic Management**
+ You should use the following AWS Managed Policies for Automatic Management.
  + [`ServiceQuotasFullAccess`](https://docs.aws.amazon.com/servicequotas/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-POLICYNAME)
  + [`AWSHealthFullAccess`](https://docs.aws.amazon.com/health/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSHealthFullAccess)

**Permissions to view Automatic Management**
+ [`AWSHealthFullAccess`](https://docs.aws.amazon.com/health/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSHealthFullAccess)

For more information on creating IAM policies, see the following links.
+ [IAM tutorial: Create and attach your first customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html) in the *AWS Identity and Access Management User Guide*
+ [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *AWS Identity and Access Management User Guide*
+ [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *AWS Identity and Access Management User Guide*

## Getting started with Service Quotas Automatic Management
<a name="getting-started-auto-mgmt"></a>

Service Quotas Automatic Management monitors service quotas usage patterns and sends you notifications when your usage approaches your [utilization thresholds](#notification-thresholds). Automatic Management works with both adjustable and non-adjustable quotas to help you track your quota utilization. To allow AWS to monitor quotas in your AWS account, you need to start the Automatic Management. The following procedures walks through how you can start Automatic Management with either the AWS Management Console or AWS CLI.

**Supported quotas**  
Not all service quotas support Automatic Management. Only quotas that have usage metrics available can be monitored. Automatic Management monitors both adjustable and non-adjustable quotas. However, only a subset of adjustable quotas support auto-adjustment. To view which quotas are supported in your account, navigate to the Automatic Management section in the Service Quotas console, which displays only the quotas that support Automatic Management in your account and region.

------
#### [ AWS Management Console ]

Use the following steps to start Automatic Management using the AWS Management Console.

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, select **Automatic Management**.

   1. Alternatively, in the Service Quotas dashboard, under **Automatic Management**, select **Start**.
**Important**  
This starts Automatic Management for all available Service Quotas and only sends notifications to the Health Dashboard.

1. Under **Automatic Management Mode**, Select **Notify Only**. There are two modes: Notify Only and Notify and Auto-Adjust. To learn more, see [Service Quotas Automatic Management modes](#automatic-management-modes)..
**Note**  
Automatic Management monitors all the monitored service quotas and sends notifications to Health Dashboard. Optionally, you can send notifications to your preferred channels in the next steps. Otherwise, choose **Skip to Review and Confirm** to continue.

   1. (Optional) You can enable **User Notification Service** to receive notifications on your preferred channel like email, app, or chat channels. Select your preferred notification method and then choose **Next**.

   1. (Optional) You can select exceptions for service quotas you do not want AWS to monitor and notify you about in your AWS account. Select your preferred exceptions and then choose **Next**.

1. Review your options on the **Review and Confirm** page. Make any edits and choose **Submit**.

1. Confirm your selection in the confirmation pop-up box.

------
#### [ AWS CLI ]

Using Automatic Management with the AWS CLI requires you to provide Service Quotas with the necessary permission to create a AWS Support case on your behalf. You can provide this permission by attaching the AWS managed policy [`ServiceQuotasFullAccess`](#security-iam-awsmanpol-POLICYNAME) to your IAM principal.

**Example Start Automatic Management for your account**  
The following example starts Automatic Management for an AWS account in Canada (Central) AWS Region. Replace the {{italicized placeholder text}} in the example command with your information.  

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region {{ca-central-1}}
```

Automatic Management supports adding your [User Notification (UNO)](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) to receive notifications in your preferred channels like app, chat, or email. To add UNO configuration, provide your UNO ARN configuration with the parameter `--notification-arn`.

**Example Start Automatic Management with UNO configuration**  
The following example starts Automatic Management for a UNO ARN in an AWS account in the Canada (Central) AWS Region. Replace the {{italicized placeholder text}} in the example command with your information.  

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region {{ca-central-1}} \
  --notification-arn arn:aws:notifications::{{111122223333}}:configuration/{{abc123def456gh789}}
```

------

## Viewing Service Quotas Automatic Management configuration
<a name="viewing-automatic-management"></a>

Use the following procedure to view Service Quotas Automatic Management configurations for your AWS account using the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **Automatic Management**.

   1. You can edit your notification configurations, [add exceptions for AWS services you don't want to monitor with Automatic Management](#excluding-quotas) or [stop Automatic Management](#stopping-automatic-management).

------
#### [ AWS CLI ]

Use the following command to view your Automatic Management configuration. Replace the {{italicized placeholder text}} in the example command with your information.

```
aws service-quotas get-auto-management-configuration --region {{ca-central-1}}
```

**Example response**  

```
{
    "OptInLevel": "ACCOUNT",
    "OptInType": "NotifyAndAdjust",
    "OptInStatus": "ENABLED",
    "NotificationArn": "arn:aws:notifications::{{111122223333}}:configuration/{{abc123def456gh789}}"
    "ExclusionList": {
        "dynamodb": [{
            "QuotaCode": "{{L-E123ABC4}}",
            "QuotaName": "Maximum number of tables"
        }]
    }}
```

------

## Updating Service Quotas Automatic Management configuration
<a name="updating-automatic-management"></a>

You can update your Service Quotas Automatic Management by adding service quotas to the exclusion list or changing your Automatic Management notification configuration. Use the following procedure to update Automatic Management configuration for your AWS account using the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **Automatic Management**.

1. Make the changes to your Automatic Management configuration.

   1. **Exclusion list update** - you can add service quotas from the exclusion list. See [Excluding service quotas from Service Quotas Automatic Management](#excluding-quotas).

   1. **Notification configuration update** - Under **Notification configuration**, choose **Edit**. You're directed to the AWS User Notifications console where you can edit the notifications for Automatic Management. For more information, see [Creating your first notification configuration in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html) in the *AWS User Notifications User Guide*.

------
#### [ AWS CLI ]

To update Automatic Management notifications with the AWS CLI, use the AWS User Notifications command, [update-notification-configuration](https://docs.aws.amazon.com/cli/latest/reference/notifications/update-notification-configuration.html) or [UpdateNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateNotificationConfiguration.html) in the *AWS User Notifications API Reference*. 

**Example Exclude Amazon DynamoDB quota from Automatic Management**  
The following example excludes DynamoDB from Automatic Management for an AWS account in the Canada (Central) AWS Region. Replace the {{italicized placeholder text}} in the example command with your information.  

```
aws service-quotas update-auto-management \
  --opt-in-type NotifyOnly \
  --region {{ca-central-1}} \
  --exclusion-list '{"{{dynamodb}}":["{{L-E123ABC4}}"]}'
```

------

## Excluding service quotas from Service Quotas Automatic Management
<a name="excluding-quotas"></a>

You won't be notified of service quotas utilizations for AWS services added to the Automatic Management exclusion list. 

You can exclude a service quota or list of quotas from being monitored by Automatic Management using the `--exclusion-list`. You'll need the service code and quota code to exclude the quota from Automatic Management in the AWS CLI.

Use the following procedure to exclude quotas from Automatic Management monitoring for your AWS account using either the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, select **Automatic Management**.

1. Under **Selected quotas for exceptions**, add the AWS services you do not want monitored with Automatic Management. After making your selection, choose **Add exceptions**. 

------
#### [ AWS CLI ]

See the following AWS CLI examples for adding supported AWS services to the Automatic Management exclusion list. You'll need to include the AWS service code and Service Quotas code in your commands.
+ **Finding supported AWS services code**
  + Use [ListServices](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServices.html) to list AWS services supported by Service Quotas. The response includes the `ServiceCode` and `ServiceName` for each service. For example, the `ServiceCode` for Amazon DynamoDB is `dynamodb`.
+ **Finding Service Quotas codes**
  + Use [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html) to list AWS services Service Quotas codes. You can specify the service with the request parameter `ServiceCode`. The response includes the `QuotaName`, `QuotaCode`, `Value`, and `QuotaAppliedAtLevel`.

**Example Starts Automatic Management and excludes Amazon DynamoDB quota**  
The following example both starts Automatic Management and excludes DynamoDB as a service quota that will not be monitored with Automatic Management. Replace the {{italicized placeholder text}} in the example command with your information.  

```
aws service-quotas start-auto-management \
  --opt-in-level ACCOUNT \
  --opt-in-type NotifyOnly \
  --region {{ca-central-1}} \
  --exclusion-list '{"{{dynamodb}}":["{{L-E123ABC4}}"]}'
```

**Example Exclude Amazon DynamoDB quota from Automatic Management**  
The following example excludes DynamoDB from Automatic Management for an AWS account in the Canada (Central) AWS Region. Replace the {{italicized placeholder text}} in the example command with your information.  

```
aws service-quotas update-auto-management \
  --opt-in-type NotifyOnly \
  --region {{ca-central-1}} \
  --exclusion-list '{"{{dynamodb}}":["{{L-E123ABC4}}"]}'
```

------

## Stopping Service Quotas Automatic Management
<a name="stopping-automatic-management"></a>

Use the following procedure to stop Service Quotas Automatic Management of service quotas for supported AWS services in your AWS account using the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **Automatic Management**.

1. Choose **Stop Automatic Management** at the top corner of the page.

1. Confirm your selection in the confirmation pop-up box.

------
#### [ AWS CLI ]

Use the following command to stop Automatic Management. Replace the {{italicized placeholder text}} in the example command with your information.

```
aws service-quotas stop-auto-management-configuration --region {{ca-central-1}}
```

------

## Service Quotas Automatic Management frequently asked questions
<a name="automatic-management-faq"></a>

### Notifications and monitoring
<a name="faq-notifications-monitoring"></a>

Q1: When will I receive notifications about my quota usage?  
After you start Automatic Management, it can take up to 24 hours for the initial opt-in to take effect and begin monitoring your quotas. Once Automatic Management is active, notifications are typically delivered within an hour of reaching a configured threshold.

Q2: How often will I receive reminder notifications?  
If the quota threshold breach remains active, you'll receive reminder notifications at different frequencies based on your utilization level:  
+ **At or above 95% utilization:** Once every 6 hours
+ **Below 95% utilization:** Once every 24 hours

Q3: Why didn't I receive a notification even though my quota usage reached the configured thresholds?  
Notifications are typically delivered within an hour of reaching a threshold. If you consistently don't receive expected notifications, contact AWS Support with details about the specific quota, Region, and timeframe for further investigation.

Q4: Can I exclude specific resources from notifications?  
No, you can't configure notification exclusions at the resource level. Automatic Management operates at the quota level, not the resource level. You can only exclude notifications on a quota basis. For instructions on excluding specific quotas from notifications, see [Excluding quotas from Automatic Management](#excluding-quotas).

Q5: Why did I receive an APPROACHING\_THRESHOLD notification instead of THRESHOLD\_BREACH even though my quota reached 100% utilization?  
The notification type is determined by whether the quota supports automatic adjustment, not by the utilization level:  
+ **APPROACHING\_THRESHOLD:** Sent for quotas that support automatic adjustment. This notification type indicates that you can optimize your quota utilization or request a quota increase.
+ **THRESHOLD\_BREACH:** Sent for quotas that cannot be automatically adjusted. This notification type indicates that you need to optimize your quota utilization to mitigate the threshold breach.
Even if your utilization reaches 100%, you'll receive an APPROACHING\_THRESHOLD notification if the quota supports automatic adjustment. For more information about notification types, see [Integrating event-driven applications with Service Quotas using Amazon EventBridge](#eventbridge-integration).

Q6: Why am I receiving alerts for quotas when my usage hasn't changed?  
More AWS services are making their quota utilization available through Service Quotas. When a service enables utilization, Service Quotas Automatic Management may begin alerting on quotas whose utilization was not previously available. This may trigger quota utilization alerts for resources that were already at or near their quota.  
This is expected behavior and indicates improved monitoring coverage, not a change in your usage.

Q7: Why am I still seeing an Automatic Management notification after my quota was already increased?  
Automatic Management Health Events have a fixed 7-day display window. Once an event is raised, it stays visible in the AWS Health Dashboard until it expires 7 days after its creation, even if your utilization has since dropped or the quota increase has already been applied. No new event is generated in that case. The existing one simply remains until the end of its 7-day window.

### Auto-adjustment process
<a name="faq-auto-adjustment"></a>

Q8: What happens when the system automatically requests a quota increase on my behalf?  
When you enable **Notify and Auto-Adjust** mode, the system automatically submits a quota increase request when your usage breaches the configured threshold.  
**How auto-adjustment works**    
Automatic processing  
Auto-adjustment submits quota increase requests without creating a support case.  
Notification of results  
You receive notifications about the result of auto-adjustment requests.  
Manual fallback  
If the request can't be processed through auto-adjustment, the request result shows as `NOT_APPROVED` and you receive a Health notification. In these cases, submit a quota increase request manually through AWS Service Quotas.

Q9: Are auto-adjust requests evaluated differently than manual Service Quotas requests?  
Yes, auto-adjust requests are processed differently than manual quota increase requests. Auto-adjust requests only work for quotas that support automated processing and are submitted without creating a support case. These requests use a streamlined approval process that may have different criteria than manual requests that go through AWS Support.  
If an auto-adjust request isn't approved, you can submit a manual quota increase request through the Service Quotas console or API, which may be approved even if the auto-adjust request wasn't.

Q10: Why don't I see explicit rejection reasons for auto-adjust failures?  
Auto-adjust requests use an automated approval process that doesn't provide detailed rejection reasons. When an auto-adjust request fails, you receive a notification that the request was `NOT_APPROVED`, but specific rejection details aren't available.  
For more information about why a quota increase wasn't approved, submit a manual quota increase request through the Service Quotas console, which provides more detailed feedback through the support case process.

Q11: Which quotas support auto-adjust?  
Not all service quotas support auto-adjustment. Only quotas that support automated processing can be auto-adjusted. Auto-adjustable status doesn't guarantee approval. If an auto-adjust request fails, submit a manual quota increase request through the Service Quotas console or API.  
To view which quotas are supported in your account:  

1. Open the Service Quotas console.

1. Navigate to **Automatic Management**.

1. View the list of monitored quotas, which shows only the quotas that support Automatic Management in your account and Region.

### Troubleshooting
<a name="faq-troubleshooting"></a>

Q12: My auto-adjust request failed, but a manual request for the same quota was approved. Why?  
Auto-adjust requests and manual quota increase requests use different approval processes:  
+ **Auto-adjust requests** use automated processing with predefined criteria and may be more restrictive.
+ **Manual requests** go through AWS Support and can be reviewed by support engineers who can consider additional context and factors.
If your auto-adjust requests consistently fail, consider submitting manual quota increase requests through the Service Quotas console for those specific quotas.

Q13: How can I track auto-adjust request results?  
You can monitor auto-adjust request results through several methods:  
+ **AWS Health Dashboard:** View notifications about auto-adjust request results.
+ **Request quota increase history:** Use the `ListRequestedServiceQuotaChangeHistoryByQuota` API to view the history of quota increase requests for a specific quota.
+ **Configured notification channels:** Receive notifications through email, AWS Console Mobile Application, or other configured channels.

### Need more help?
<a name="faq-need-help"></a>

If you have additional questions or need assistance with Automatic Management, contact AWS Support or refer to the [Service Quotas documentation](https://docs.aws.amazon.com/servicequotas/).

# Using Service Quotas request templates
<a name="organization-templates"></a>

**Note**  
Quota request templates are only supported in commercial AWS Regions. Templates are not supported in China Regions or opt-in Regions (Regions that require manual selection to be activated). 

A *quota request template *helps you save time when customizing quotas for new AWS accounts in your organization. To use a template, configure the desired service quota increases for new accounts. Then, enable template association. This associates the template with your organization in AWS Organizations. Whenever new accounts are created in your organization, the template automatically requests quota increases for you.

**Note**  
You can only use quota request templates with AWS accounts that are members of an organization managed by AWS Organizations. 

To use a request template, you must use AWS Organizations and the new accounts must be created in the same organization. Your organization must have all features enabled, [all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html). If you use consolidated billing features only, you can't use quota request templates.

You can update the request template by adding or removing service quotas. You can also increase the values for adjustable quotas. As soon as you adjust the template, those service quota values are requested for new accounts. Updating a request template doesn't update quota values for existing accounts.

**To enable template association**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, expand **Organization**, and then choose **Quota request template**. 

1. In the **Template association** section, choose **Enable**.

**To add a quota to your request template**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, expand **Organization**, and then choose **Quota request template**. 

1. In the **Added quotas** section, choose **Add quota**.
**Note**  
You add up to 10 quotas to your request template.

1. On the **Add quota** page, choose a **Region**, **Service**, **Quota**, and **Desired quota value**, and then choose **Add**.

**To remove a quota from your request template**

You can remove service quota requests from the template regardless of whether the template is associated with an organization. If you reach the maximum number of service quota requests, you might need to remove some quotas from your request template.

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, expand **Organization**, and then choose **Quota request template**. 

1. In the **Added quotas** section, select the option button for the quota that you want to remove.

1. Choose **Remove**.

**To disable the template association**

If you disable the automatic template association, new accounts receive the AWS default quota values for all quotas. Disabling the template association from the organization doesn't delete the service quota requests from the template. You can continue to edit the service quotas in the template.

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, expand **Organization**, and then choose **Quota request template**. 

1. In the **Template association** section, choose **Disable**.

# Security in Service Quotas
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Service Quotas, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Service Quotas. The following topics show you how to configure Service Quotas to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Service Quotas resources. 

**Topics**
+ [Data protection in Service Quotas](#data-protection)
+ [Logging and monitoring Service Quotas](#monitoring-overview)
+ [Identity and access management in Service Quotas](#identity-access-management)
+ [Integrating event-driven applications with Service Quotas using Amazon EventBridge](#eventbridge-integration)
+ [Compliance validation for Service Quotas](#SERVICE-compliance)
+ [Resilience in Service Quotas](#disaster-recovery-resiliency)
+ [Infrastructure Security in Service Quotas](#infrastructure-security)

## Data protection in Service Quotas
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Service Quotas. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Service Quotas or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



### Encryption at rest
<a name="encryption-rest"></a>

Quota-related information, such as applied quota values and quota request history, are encrypted at rest. Unique encryption keys are used for each Region.

### Encryption in transit
<a name="encryption-transit"></a>

Customer requests and all associated data is encrypted in transit using [Transport Later Security (TLS)](https://datatracker.ietf.org/doc/html/rfc5246) 1.2 or later. All Service Quotas endpoints support HTTPS for encrypting data in transit.

## Logging and monitoring Service Quotas
<a name="monitoring-overview"></a>

### Overview
<a name="monitor-sq"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Service Quotas and your other AWS solutions. AWS provides the following monitoring tools to watch Service Quotas, report when something is wrong, and take automatic actions when appropriate:
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
+ *Amazon CloudWatch* monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

### Logging Service Quotas API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Service Quotas is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Service Quotas. CloudTrail captures all API calls for Service Quotas as events. The calls captured include calls from the Service Quotas console and code calls to the Service Quotas API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Service Quotas. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Service Quotas, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

#### Service Quotas information in CloudTrail
<a name="service-quotas-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Service Quotas, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for Service Quotas, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Service Quotas actions are logged by CloudTrail and are documented in the [Service Quotas API Reference](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/Welcome.html). For example, calls to the `GetServiceQuota`, `RequestServiceQuotaIncrease` and `ListAWSDefaultServiceQuotas` actions generate entries in the CloudTrail log files.

Every event or log entry contains information that helps you determine who made the request.
+  AWS account root credentials. 
+ Temporary security credentials from an AWS Identity and Access Management role or federated user.
+ Long-term security credentials from an IAM user.
+ Another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

#### Understanding Service Quotas log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `RequestQuotaIncrease` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDA123456789012Example",
        "arn": "arn:aws:iam::123456789012:user/admin",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": " admin",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-01-24T16:57:04Z",
                "mfaAuthenticated": "true"
            }
        }
    },
    "eventTime": "2022-01-24T17:00:15Z",
    "eventSource": "servicequotas.amazonaws.com",
    "eventName": "RequestServiceQuotaIncrease",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "172.21.16.1",
    "userAgent": "aws-internal/3 aws-sdk-java/1.12.127 Linux/5.4.147-83.259.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.312-b07 java/1.8.0_312 vendor/Oracle_Corporation cfg/retry-mode/standard",
    "requestParameters": {
        "serviceCode": "ec2",
        "quotaCode": "L-CEED54BB",
        "desiredValue": 10
    },
    "responseElements": {
        "requestedQuota": {
            "id": "cd3ad3d9-2776-4ef1-a904-4c229d1642ee",
            "serviceCode": "ec2",
            "serviceName": "Amazon Elastic Compute Cloud (Amazon EC2)",
            "quotaCode": "L-CEED54BB",
            "quotaName": "EC2-Classic Elastic IPs",
            "desiredValue": 10,
            "status": "PENDING",
            "created": "Jan 24, 2022 5:00:15 PM",
            "requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:user/admin\"}",
            "quotaArn": "arn:aws:servicequotas:us-east-1:123456789012:ec2/L-CEED54BB",
            "globalQuota": false,
            "unit": "None"
        }
    },
    "requestID": "3d3f5cdc-af30-4121-b69a-84b2f5c33be5",
    "eventID": "0cb51588-e460-4e00-bc48-a9d4820cad83",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

This example shows that the user named `admin` generated a request for additional Amazon Elastic Compute Cloud Elastic IP addresses on January 24, 2022. The requested increase was 10, an increase of 5 from the default quota of 5.

The following is an example of an approved quota increase in Service Quotas:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "accountId": "123456789012",
        "invokedBy": "servicequotas.amazonaws.com"
    },
    "eventTime": "2022-01-24T17:02:17Z",
    "eventSource": "servicequotas.amazonaws.com",
    "eventName": "UpdateServiceQuotaIncreaseRequestStatus",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "servicequotas.amazonaws.com",
    "userAgent": "servicequotas.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "e331b0a0-9395-4895-aeba-73cbab9ebcb0",
    "readOnly": false,
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "requestId": "cdc5f1f78739459e6642407bb2bZKO8GKUM",
        "newStatus": "CASE_CLOSED",
        "createTime": "2022-01-24T17:00:15.363Z",
        "newQuotaValue": "10.0",
        "serviceName": "Amazon Elastic Compute Cloud (Amazon EC2)",
        "quotaName": "EC2-Classic Elastic IPs",
        "unit": "None"
    },
    "eventCategory": "Management"
}
```

From the `serviceEventDetails` section, you can determine that Support approved the request for a quota increase to 10 Elastic IP addresses, and closed the request. The `newQuotaValue` displays 10 as the new quota.

#### Service Quotas Automatic Management AWS CloudTrail logs
<a name="auto-mgmt-ct-logs"></a>

The following are AWS CloudTrail logs for Automatic Management critical and non-critical events.

##### Critical
<a name="critical-events"></a>

The following is an example of an EventBridge event for Automatic Management. This event shows the utilization for AWS CloudTrail and is a critical event where you'd receive notification.

```
{
    "version": "0",
    "id": "97c1eb9w-0f16-f3d5-b0d6-d6b8d6614315",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "************",
    "time": "2025-09-12T02:18:36Z",
    "region": "ca-central-1",
    "resources": ["Service: cloudtrail | Quota Name: Trails per region | Utilization: 80.0%"],
    "detail": {
        "eventArn": "arn:aws:health:ca-central-1::event/SERVICEQUOTAS/AWS_SERVICEQUOTAS_THRESHOLD_BREACH/AWS_SERVICEQUOTAS_THRESHOLD_BREACH-YUL-1757643474686",
        "service": "SERVICEQUOTAS",
        "eventTypeCode": "AWS_SERVICEQUOTAS_THRESHOLD_BREACH",
        "eventTypeCategory": "accountNotification",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "a26c337bff88e2bcb6ec65835dda2152ec3f870926433ccf6c871712ed655221-1",
        "startTime": "Fri, 12 Sep 2025 02:17:54 GMT",
        "lastUpdatedTime": "Fri, 12 Sep 2025 02:17:54 GMT",
        "statusCode": "open",
        "eventRegion": "ca-central-1",
        "eventDescription": [{
            "language": "en_US",
            "latestDescription": "You are receiving this message because you opted to receive notifications from Service Quotas when utilization exceeds (80/95)% threshold.\n\nAt Fri, 12 Sep 2025 02:17:54 GMT, we detected that this AWS account has reached the utilization threshold for one or more service quotas.\n\nA list of your affected service quota(s) can be found in the \"Affected resources\" tab of your AWS Health Dashboard under the format \"Service | Quota Name | Utilization Pe Percentage\".\n\nFor unchangeable or non-adjustable quotas, we recommend designing your architecture for applications and services to prevent these limits from impacting reliability as per the AWS well architected framework.\nPlease refer to AWS Well-Architected document (1) for details.\n\nIf you have any questions or concerns, please contact the AWS Support Team (2).\n\n(1) https://docs.aws.amazon.com/wellarchitected/2025-02-25/framework/rel_manage_service_limits_aware_fixed_limits.html\n(2) https://aws.amazon.com/support"
        }],
        "affectedEntities": [{
            "entityValue": "Service: cloudtrail | Quota Name: Trails per region | Utilization: 80.0%",
            "lastUpdatedTime": "Fri, 12 Sep 2025 02:17:54 GMT"
        }],
        "affectedAccount": "111122223333",
        "page": "1",
        "totalPages": "1"
    }}
```

##### Non-critical
<a name="non-critical-events"></a>

The following is an example of an EventBridge event for Automatic Management. This event shows the utilization for Amazon DynamoDB and is a non-critical event. This event is sent to CloudTrail.

```
{
    "version": "0",
    "id": "ecf5de2a-0c6e-6627-761e-a60a482f0d00",
    "detail-type": "AWS Service Event via CloudTrail",
    "source": "aws.servicequotas",
    "account": "************",
    "time": "2025-09-12T08:19:07Z",
    "region": "ca-central-1",
    "resources": [],
    "detail": {
        "eventVersion": "1.10",
        "userIdentity": {
            "accountId": "555555555555",
            "invokedBy": "servicequotas.amazonaws.com"
        },
        "eventTime": "2025-09-12T08:19:07Z",
        "eventSource": "servicequotas.amazonaws.com",
        "eventName": "ServiceQuotasUtilizationBreachingThreshold",
        "awsRegion": "ca-central-1",
        "sourceIPAddress": "servicequotas.amazonaws.com",
        "userAgent": "servicequotas.amazonaws.com",
        "requestParameters": null,
        "responseElements": null,
        "eventID": "ee20d580-8015-4c20-bd6d-ef53b969aefb",
        "readOnly": false,
        "eventType": "AwsServiceEvent",
        "managementEvent": true,
        "recipientAccountId": "555555555555",
        "serviceEventDetails": {
            "action": "NOTIFY_ONLY",
            "created": "Fri Sep 12 08:19:07 UTC 2025",
            "serviceCode": "dynamodb",
            "requester": "339712738202",
            "quotaCode": "L-F98FE922",
            "quotaName": "Maximum number of tables",
            "utilizationValue": "2500.0",
            "breachingThreshold": "95",
            "adjustability": "Adjustable",
            "quotaArn": "arn:aws:servicequotas:ca-central-1:555555555555:dynamodb/L-F98FE922"
        },
        "eventCategory": "Management"
    }}
```

### Service Quotas and Amazon CloudWatch alarms
<a name="configure-cloudwatch"></a>

You can create Amazon CloudWatch alarms to notify you when you're close to a quota value threshold. Setting an alarm can help alert you if you need to request a quota increase.

**To create a CloudWatch alarm for a quota**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home).

1. In the navigation pane, choose **AWS services** and then select a service.

1. Select a quota that supports CloudWatch alarms.

   If you actively use the quota, utilization appears beneath the quota description. If CloudWatch alarms are supported, the CloudWatch alarms section appears at the bottom of the page.

1. In **Amazon CloudWatch alarms**, choose **Create**.

1. For **Alarm threshold**, choose a threshold.

1. For **Alarm name**, enter a name for the alarm. This name must be unique within the AWS account.

1. Choose **Create**.

**Note**  
To add a notification to the CloudWatch alarm, see [Creating a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the *Amazon CloudWatch User Guide*.

**To delete a CloudWatch alarm**

1. Choose the service quota with the alarm.

1. Select the alarm.

1. Choose **Delete**.

## Identity and access management in Service Quotas
<a name="identity-access-management"></a>

AWS uses security credentials to identify you and to grant you access to your AWS resources. You can use features of AWS Identity and Access Management (IAM) to allow other users, services, and applications to use your AWS resources fully or in a limited way. You can do this without sharing your security credentials.

By default, principals, such as IAM roles or users, don't have permission to create, view, or modify AWS resources. To allow a principal to access resources such as a load balancer, and to perform tasks, perform the following steps:

1. Create an IAM policy that grants the principal permission to use the specific resources and API actions they need.

1. Attach the policy to the IAM principal or the group that the principal belongs to.

When you attach a policy to a user or group of users, it allows or denies the users permission to perform the specified tasks on the specified resources.

For example, you can use IAM to create roles or users as the principals in your AWS account. A principal can represent a person, a system, or an application. Then you grant permissions to the principals to perform specific actions on the specified resources using an IAM policy.

### Grant permissions using IAM policies
<a name="iam-policies"></a>

When you attach a policy to a principal or a group of principals, it allows or denies those principals permission to perform the specified tasks on the specified resources.

An IAM policy is a JSON document that consists of one or more statements. The following lists the different statements in an IAM policy. For more information, see the *[IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)*.
+ **`Effect`** – The value for **effect** can be either `Allow` or `Deny`. By default, IAM principals don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.
+ **`Action`** – The value for **action** is the specific API action for which you are granting or denying permission. For more information about specifying `Action`, see [API actions for Service Quotas](#api-actions).
+ `Resource` – The resource that's affected by the action. With some Service Quotas API actions, you can restrict the permissions granted or denied to a specific quota. To do so, specify its Amazon Resource Name (ARN) in this statement. Otherwise, you can use the wildcard character (`*`) to specify all Service Quotas resources. For more information, see [Service Quotas resources](#resources).
+ `Condition` – You can optionally use conditions to control when your policy is in effect. For more information, see [Condition keys for Service Quotas](#condition-keys).

### API actions for Service Quotas
<a name="api-actions"></a>

In the `Action` element of your IAM policy statement, you can specify any API action that Service Quotas offers. You must prefix the action name with the lowercase string `servicequotas:`, as shown in the following example.

```
"Action": "servicequotas:GetServiceQuota"
```

To specify multiple actions in a single statement, enclose them in square brackets and separate them with a comma, as shown in the following example.

```
"Action": [
    "servicequotas:ListRequestedServiceQuotaChangeHistory",
    "servicequotas:ListRequestedServiceQuotaChangeHistoryByQuota"
]
```

You can also specify multiple actions using the wildcard character (`*`). The following example specifies all API action names for Service Quotas that start with `Get`.

```
"Action": "servicequotas:Get*"
```

To specify all API actions for Service Quotas, use the wildcard character (`*`), as shown in the following example.

```
"Action": "servicequotas:*"
```

For the list of API actions for Service Quotas, see [Service Quotas Actions](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_Operations.html).

### Service Quotas resources
<a name="resources"></a>

*Resource-level permissions* refers to the ability to specify which resources users are allowed to perform actions on. For API actions that support resource-level permissions, you can control the resources that users are allowed to use with the action. To specify a resource in a policy statement, you must use its Amazon Resource Name (ARN).

The ARN for a quota has the format shown in the following example.

```
arn:aws:servicequotas:{{region-code}}:{{account-id}}:{{service-code}}/{{quota-code}}
```

For API actions that don't support resource-level permissions, you must specify the resource statement shown in the following example.

```
"Resource": "*"
```

### Resource-level permissions for Service Quotas
<a name="resource-level-permissions"></a>

The following Service Quotas actions support resource-level permissions:
+ [PutServiceQuotaIncreaseRequestIntoTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_PutServiceQuotaIncreaseRequestIntoTemplate.html)
+ [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html)

For more information, see [Actions defined by Service Quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_servicequotas.html#servicequotas-actions-as-permissions) in the *Service Authorization Reference*.

### Condition keys for Service Quotas
<a name="condition-keys"></a>

When you create a policy, you can specify the conditions that control when the policy is in effect. Each condition contains one or more key-value pairs. There are global condition keys and service-specific condition keys.

The `servicequotas:service` key is specific to Service Quotas. The following Service Quotas API actions support this key:
+ [PutServiceQuotaIncreaseRequestIntoTemplate](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_PutServiceQuotaIncreaseRequestIntoTemplate.html)
+ [RequestServiceQuotaIncrease](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html)

For more information about global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

### Predefined AWS managed policies for Service Quotas
<a name="predefined-policies"></a>

The managed policies created by AWS grant the required permissions for common use cases. You can attach these policies to your IAM principals, based on the access to Service Quotas that they require:
+ `ServiceQuotasFullAccess` – Grants full access required to use Service Quotas features.
+ `ServiceQuotasReadOnlyAccess` – Grants read-only access to Service Quotas features.

### Permissions for Service Quotas Automatic Management
<a name="permissions-for-auto-mgmt"></a>

To enable Service Quotas Automatic Management to send notifications via AWS User Notifications, you'll need the following IAM permissions.
+ `notifications:ListChannels`
+ `notifications:ListEventRules`
+ `notifications:ListNotificationConfigurations`
+ `notifications:GetNotificationConfiguration`
+ `notifications:GetEventRule`
+ `notifications:AssociateChannel`
+ `notifications:DisassociateChannel`
+ `notifications:CreateEventRule`
+ `notifications:CreateNotificationConfiguration`
+ `notifications:UpdateNotificationConfiguration`
+ `notifications:DeleteNotificationConfiguration`
+ `notifications:ListNotificationHubs`
+ `notifications:RegisterNotificationHub`
+ `notifications-contacts:ListEmailContacts`
+ `notifications-contacts:SendActivationCode`
+ `notifications-contacts:CreateEmailContact`
+ `notifications-contacts:ActivateEmailContact`
+ `notifications-contacts:GetEmailContact`
+ `notifications:UpdateEventRule`
+ `chatbot:ListMicrosoftTeamsChannelConfigurations`
+ `chatbot:DescribeChimeWebhookConfigurations`
+ `chatbot:DescribeSlackChannelConfigurations`
+ `consoleapp:ListDeviceIdentities`
+ `consoleapp:GetDeviceIdentity`

The following IAM policy example allows these permissions.

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
                "notifications:ListChannels",
                "notifications:ListEventRules",
                "notifications:ListNotificationConfigurations",
                "notifications:GetNotificationConfiguration",
                "notifications:GetEventRule",
                "notifications:AssociateChannel",
                "notifications:DisassociateChannel",
                "notifications:CreateEventRule",
                "notifications:CreateNotificationConfiguration",
                "notifications:UpdateNotificationConfiguration",
                "notifications:DeleteNotificationConfiguration",
                "notifications:ListNotificationHubs",
                "notifications:RegisterNotificationHub",
                "notifications-contacts:ListEmailContacts",
                "notifications-contacts:SendActivationCode",
                "notifications-contacts:CreateEmailContact",
                "notifications-contacts:ActivateEmailContact",
                "notifications-contacts:GetEmailContact",
                "notifications:UpdateEventRule",
                "chatbot:ListMicrosoftTeamsChannelConfigurations",
                "chatbot:DescribeChimeWebhookConfigurations",
                "chatbot:DescribeSlackChannelConfigurations",
                "consoleapp:ListDeviceIdentities",
                "consoleapp:GetDeviceIdentity"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### AWS managed policies for Service Quotas
<a name="security-iam-awsmanpol"></a>



An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

#### AWS managed policy: ServiceQuotasFullAccess
<a name="security-iam-awsmanpol-POLICYNAME"></a>

You can attach `ServiceQuotasFullAccess` to your users, groups, and roles.

This policy grants permissions that allow full administrative control of the Service Quotas service. You can perform all tasks involved in viewing and managing your quotas for AWS services in Service Quotas in the AWS Regions in your account.

**Permissions details**

This policy includes permissions that allow all actions for Service Quotas, including viewing AWS default values and applied values, requesting a service quota increase, and viewing current utilization of resources. This policy also includes 18 permissions that are not part of Service Quotas and can be broadly split into **non-mutating** and **mutating** operations. Non-mutating operations include permissions from trusted advisors to retrieve applied quota value and view current utilization of resources. Mutating operations include permission to create and delete alarms on utilization of resources, and permissions to create the service-linked role necessary to create a support case on your behalf while requesting a quota increase. 

This policy includes the following non-mutating and mutating operations that are *not* part of Service Quotas: 

**Non-mutating operations**
+ `autoscaling:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for AWS Auto Scaling quotas.
+ `cloudformation:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for CloudFormation quotas.
+ `cloudwatch:DescribeAlarmsForMetric` – Allows you to retrieve alarms for specified metrics from Service Quotas that were created for notifying automatically whenever a specified quota reaches a percentage of the maximum or reaches the maximum level. 
+ `cloudwatch:DescribeAlarms` – Allows you to retrieve alarms from Service Quotas that were created for notifying automatically whenever a specified quota reaches a percentage of the maximum or reaches the maximum level. 
+ `cloudwatch:GetMetricData` – Allows Service Quotas to view current utilization of resources. 
+ `cloudwatch:GetMetricStatistics` – Allows Service Quotas to view current utilization of resources. 
+ `dynamodb:DescribeLimits` – Allows Service Quotas to retrieve applied quota value for DynamoDB quotas. 
+ `elasticloadbalancing:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for Elastic Load Balancing quotas. 
+ `iam:GetAccountSummary` – Allows Service Quotas to retrieve applied quota value for IAM. 
+ `kinesis:DescribeLimits` – Allows Service Quotas to retrieve applied quota value for Amazon Kinesis quotas. 
+ `organizations:DescribeAccount` and `organizations:DescribeOrganization` – Allows Service Quotas to create and execute quota templates. 
+ `rds:DesceibeAccountAttributes` – Allows Service Quotas to retrieve applied quota value for Amazon RDS quotas. 
+ `route53:GetAccountLimit` – Allows Service Quotas to retrieve applied quota value for Amazon Route 53 quotas. 
+ `tag:GetTagKeys` – Allows Service Quotas to get tag keys currently in use in the specified AWS Region for the calling account. 
+ `tag:GetTagValues` – Allows Service Quotas to get tag values for the specified key that are used in the specified AWS Region for the calling account. 

**Mutating operations**
+ `cloudwatch:PutMetricAlarm` – Allows Service Quotas to create an alarm for notifying you automatically whenever a specified quota reaches a percentage of the maximum or the maximum level.
+ `cloudwatch:DeleteAlarms` – Allows Service Quotas to delete the specified alarm. 
+ `organizations:EnableAWSServiceAccess` – Allows Service Quotas to create a [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in all the accounts in your organization. This allows Service Quotas to perform operations on your behalf in your organization and its accounts. 
+ `iam:CreateServicelinkedRole` – Allows Service Quotas to create an IAM role that allows Service Quotas to create a support case on your behalf when you request a quota increase. 



To see the latest version of this AWS managed policy, see [`ServiceQuotasFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ServiceQuotasFullAccess.html) in the *AWS Managed Policy Reference Guide*.

#### AWS managed policy: ServiceQuotasReadOnlyAccess
<a name="security-iam-awsmanpol-POLICYNAME2"></a>

You can attach `ServiceQuotasReadOnlyAccess` to your users, groups, and roles.

This policy grants permissions that allow users to view their AWS default quotas, applied quotas, and view current utilization of resources.

**Permissions details**

This policy includes permissions that allow your to perform the Service Quotas `Get*`, and `List*` operations to view your AWS default quotas and applied quotas. You can also view current utilization of resources. 

**Note**  
This policy does not allow you to request a service quota increase.

This policy includes the following non-mutating operations that are *not* part of Service Quotas: 

**Non-mutating operations**
+ `autoscaling:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for AWS Auto Scaling quotas.
+ `cloudformation:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for CloudFormation quotas.
+ `cloudwatch:DescribeAlarmsForMetric` – Allows you to retrieve alarms for specified metrics from Service Quotas that were created for notifying automatically whenever a specified quota reaches a percentage of the maximum or reaches the maximum level. 
+ `cloudwatch:DescribeAlarms` – Allows you to retrieve alarms from Service Quotas that were created for notifying automatically whenever a specified quota reaches a percentage of the maximum or reaches the maximum level. 
+ `cloudwatch:GetMetricData` – Allows Service Quotas to view current utilization of resources. 
+ `cloudwatch:GetMetricStatistics` – Allows Service Quotas to view current utilization of resources. 
+ `dynamodb:DescribeLimits` – Allows Service Quotas to retrieve applied quota value for DynamoDB quotas. 
+ `elasticloadbalancing:DescribeAccountLimits` – Allows Service Quotas to retrieve applied quota value for Elastic Load Balancing quotas. 
+ `iam:GetAccountSummary` – Allows Service Quotas to retrieve applied quota value for IAM. 
+ `kinesis:DescribeLimits` – Allows Service Quotas to retrieve applied quota value for Amazon Kinesis quotas. 
+ `organizations:DescribeAccount` and `organizations:DescribeOrganization` – Allows Service Quotas to create and execute quota templates. 
+ `rds:DesceibeAccountAttributes` – Allows Service Quotas to retrieve applied quota value for Amazon RDS quotas. 
+ `route53:GetAccountLimit` – Allows Service Quotas to retrieve applied quota value for Amazon Route 53 quotas. 
+ `tag:GetTagKeys` – Allows Service Quotas to get tag keys currently in use in the specified AWS Region for the calling account. 
+ `tag:GetTagValues` – Allows Service Quotas to get tag values for the specified key that are used in the specified AWS Region for the calling account. 
+ `notifications:ListChannels` - Allows Service Quotas to list the channels for your Automatic Management configuration.
+ `notifications:ListEventRules` - Allows Service Quotas to list the event rules Automatic Management configuration.
+ `notifications:ListNotificationConfigurations` - Allows Service Quotas to list the notifications configuration for your Automatic Management configuration.
+ `notifications:GetNotificationConfiguration` - Allows Service Quotas to retrieve the notification configuration for your Automatic Management configuration.
+ `notifications:GetEventRule` - Allows Service Quotas to retrieve the event rules for your Automatic Management configuration.
+ `notifications:ListNotificationHubs` - Allows Service Quotas to list the notification hubs for your Automatic Management configuration.
+ `notifications-contacts:ListEmailContacts` - Allows Service Quotas to list all the email contacts under the AWS account.
+ `notifications-contacts:GetEmailContact` - Allows Service Quotas to retrieve all the email contacts under the AWS account.
+ `chatbot:ListMicrosoftTeamsChannelConfigurations` - Allows Service Quotas to list all Amazon Q Developer Microsoft Team channel configurations in an AWS account.
+ `chatbot:DescribeChimeWebhookConfigurations` - Allows Service Quotas to list all Amazon Chime webhook configurations in an AWS account.
+ `chatbot:DescribeSlackChannelConfigurations` - Allows Service Quotas to list all Slack channel configurations in an AWS account.
+ `consoleapp:ListDeviceIdentities` - Allows Service Quotas to list all the devices' identities in an AWS account.
+ `consoleapp:GetDeviceIdentity` - Allows Service Quotas to retrieve all the devices' identities in an AWS account.

To see the latest version of this AWS managed policy, see [`ServiceQuotasReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ServiceQuotasReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

#### AWS managed policy: ServiceQuotasServiceRolePolicy
<a name="security-iam-awsmanpol-POLICYNAME3"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

This policy grants permissions that allows Service Quotas to create support cases on your behalf.

**Permissions details**

This policy includes the following operations: 
+ `support:CreateCase` – Allows Service Quotas to create support cases on your behalf when you request a quota increase. 
+ `support:DescribeCases` – Allows Service Quotas to retrieve the details and status of your support case for the quota increase request. 
+ `support:RresolveCase` – Allows Service Quotas to resolve support cases on your behalf. 

To see the latest version of this AWS managed policy, see [`ServiceQuotasServiceRolePolicy`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ServiceQuotasServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.





#### Service Quotas updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Service Quotas since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Service Quotas Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [ServiceQuotasReadOnlyAccess](#security-iam-awsmanpol-POLICYNAME2) – Update policy permissions | Service Quotas modified the permissions for `ServiceQuotasReadOnlyAccess` to support [Automatic Management](#automatic-management). `ServiceQuotasReadOnlyAccess` allows the following actions:+   `notifications:ListChannels`  <br />+   `notifications:ListEventRules`  <br />+   `notifications:ListNotificationConfigurations`  <br />+   `notifications:GetNotificationConfiguration`  <br />+   `notifications:GetEventRule`  <br />+   `notifications:ListNotificationHubs`  <br />+   `notifications-contacts:ListEmailContacts`  <br />+   `notifications-contacts:GetEmailContact`  <br />+   `chatbot:ListMicrosoftTeamsChannelConfigurations`  <br />+   `chatbot:DescribeChimeWebhookConfigurations`  <br />+   `chatbot:DescribeSlackChannelConfigurations`  <br />+   `consoleapp:ListDeviceIdentities`  <br />+   `consoleapp:GetDeviceIdentity`   | October 3, 2025 | 
| [ServiceQuotasFullAccess](#security-iam-awsmanpol-POLICYNAME) – New policy | Added a new AWS managed policy that allows full administrative control of the Service Quotas service. You can perform all tasks involved in viewing and managing your quotas for AWS services in Service Quotas in the AWS Regions in your account. | May 30, 2024 | 
| [ServiceQuotasReadOnlyAccess](#security-iam-awsmanpol-POLICYNAME2) – New policy | Added a new AWS managed policy that allows users to view their AWS default quotas, applied quotas, and view current utilization of resources. | May 30, 2024 | 
| [ServiceQuotasServiceRolePolicy](#security-iam-awsmanpol-POLICYNAME3) – New policy | Added a new AWS managed policy that allows Service Quotas to create support cases on your behalf. | May 30, 2024 | 
| Service Quotas started tracking changes | Service Quotas started tracking changes for its AWS managed policies.  | May 30, 2024 | 

## Integrating event-driven applications with Service Quotas using Amazon EventBridge
<a name="eventbridge-integration"></a>

With Amazon EventBridge rules, you can monitor Service Quotas events and AWS Health notifications to automate responses when quotas change or approach their limits. To monitor these Service Quotas events, you'll need to [start Service Quotas Automatic Management](#getting-started-auto-mgmt). These events trigger remediation actions when quota utilization changes occur.

You do this by using Amazon EventBridge to route events from Service Quotas to other software components. Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to integrate AWS services like Service Quotas into event-driven architectures without additional code and operations.

**Topics**
+ [How EventBridge routes Service Quotas events](#eventbridge-routes-service-events)
+ [Service Quotas events](#eventbridge-service-events)
+ [Creating event patterns that match Service Quotas events](#eventbridge-event-delivery-filter)
+ [Receiving events from EventBridge](#eventbridge-service-as-target)

### How EventBridge routes Service Quotas events
<a name="eventbridge-routes-service-events"></a>

Here's how EventBridge works with Service Quotas events:

As with many AWS services, Service Quotas generates and sends events to the EventBridge default *event bus*. An event bus is a router that receives events and routes them to the destinations, or *targets*, that you specify. Targets can include other AWS services, custom applications, and SaaS partner applications. 

EventBridge routes events according to *rules* you create on the event bus. For each rule, you specify a filter, or *event pattern*, to select only the events you want. Whenever an event is sent to the event bus, EventBridge compares it against each rule. If the event matches the rule, EventBridge routes the event to the specified target(s).

![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge routes the event to the targets specified for that rule.](https://docs.aws.amazon.com/servicequotas/latest/userguide/images/eventbridge-integration-how-it-works.png)


### Service Quotas events
<a name="eventbridge-service-events"></a>

For a list of Service Quotas events sent to EventBridge, refer to the Service Quotas topic in the [*EventBridge Events Reference*](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html).

#### Event structure
<a name="eventbridge-event-structure"></a>

All events from AWS services contain two types of data:
+ A common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others. For definitions of these general fields, see [Event structure ](https://docs.aws.amazon.com/eventbridge/latest/ref/overiew-event-structure.html) in the *Amazon EventBridge Events Reference*. 
+ A `detail` field that contains data specific to that particular service event. 

#### Service Quotas event delivery via AWS CloudTrail
<a name="eventbridge-events-via-cloudtrail"></a>

AWS services can send events directly to the EventBridge default event bus. In addition, AWS CloudTrail sends events originating from numerous AWS services to EventBridge as well. These events can include API calls, console signins and actions, service events, and CloudTrail Insights. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *EventBridge User Guide*. 

### Creating event patterns that match Service Quotas events
<a name="eventbridge-event-delivery-filter"></a>

Event patterns are filters that specify the data to match the events you want to select.

Each event pattern is a JSON object that contains:
+ A `source` attribute that identifies the service sending the event. For Service Quotas events generated by Automatic Management, the source is `{{aws.health}}`.
+ A `detail-type` attribute set to `AWS Health Events`, which specifies the type of event.
+ A `detail` attribute containing the following fields:
  + A `service` field set to `SERVICEQUOTAS`
  + An `eventTypeCode` field that matches one or more of these values:
    + `AWS_SERVICEQUOTAS_APPROACHING_THRESHOLD`
    + `AWS_SERVICEQUOTAS_INCREASE_REQUEST_FAILED`
    + `AWS_SERVICEQUOTAS_THRESHOLD_BREACH`
  + An `eventTypeCategory` field set to `accountNotification`

For example, the following event pattern would select all {{Event Name}} events from Service Quotas:

```
{
    "source": ["aws.health"],
    "detail-type": ["AWS Health Event"],
    "detail": {
        "service": ["SERVICEQUOTAS"],
        "eventTypeCode": [
            "AWS_SERVICEQUOTAS_THRESHOLD_BREACH",
            "AWS_SERVICEQUOTAS_INCREASE_REQUEST_FAILED",
            "AWS_SERVICEQUOTAS_APPROACHING_THRESHOLD"
        ],
        "eventTypeCategory": ["accountNotification"]
    }
}
```

The following describes the different event type codes.
+ `AWS_SERVICEQUOTAS_THRESHOLD_BREACH` - Tracks Service Quotas that cannot be adjusted. You'll need to optimize your quota utilization to mitigate further Service Quota threshold breach.
+ `AWS_SERVICEQUOTAS_INCREASE_REQUEST_FAILED` - Tracks failed attempts to automatically increase service quotas when usage thresholds are exceeded.
+ `AWS_SERVICEQUOTAS_APPROACHING_THRESHOLD` - Tracks Service Quotas that can be adjusted. You can optimize your quota utilization or request a quota increase to mitigate further Service Quota approaching threshold.

For more information on writing event patterns, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *EventBridge User Guide*.

### Receiving events from EventBridge
<a name="eventbridge-service-as-target"></a>

With Service Quotas Automatic Management, you can specify your custom applications as targets for EventBridge rules. This enables your applications to receive events from AWS services like Service Quotas. For more information, see [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *EventBridge User Guide*. 

For a full list of the AWS services that you can specify as targets, see [Target types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets) in the *EventBridge Events Reference*. 

## Compliance validation for Service Quotas
<a name="SERVICE-compliance"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Resilience in Service Quotas
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, Service Quotas offers several features to help support your data resiliency and backup needs.

## Infrastructure Security in Service Quotas
<a name="infrastructure-security"></a>

As a managed service, Service Quotas is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Service Quotas through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

You can call these API operations from any network location, but Service Quotas does support resource-based access policies, which can include restrictions based on the source IP address. 

# Service quotas for Service Quotas
<a name="reference_limits"></a>

The following tables list the maximum values for Service Quotas resources for your AWS account. 

All of these quota values are per AWS Region, unless noted otherwise. 

You can't adjust these quota values.


**Increase requests**  

| Quota | Default | 
| --- | --- | 
| Active requests per account (Global) | 20 | 
| Active requests per account per opt-in Region | 2 | 
| Active requests per quota | 1 | 
| Active requests per resource | 1 | 


**API request rates**  

| Quota | Default | 
| --- | --- | 
| GetAWSDefaultServiceQuota requests per second | 5 | 
| Additional GetAWSDefaultServiceQuota requests per second sent in one burst | 5 | 
| GetRequestedServiceQuotaChange requests per second | 5 | 
| Additional GetRequestedServiceQuotaChange requests per second sent in one burst | 5 | 
| GetServiceQuota requests per second | 5 | 
| Additional GetServiceQuota requests per second sent in one burst | 5 | 
| ListAWSDefaultServiceQuotas requests per second | 10 | 
| Additional ListAWSDefaultServiceQuotas requests per second sent in one burst | 10 | 
| ListRequestedServiceQuotaChangeHistory requests per second | 5 | 
| Additional ListRequestedServiceQuotaChangeHistory requests per second sent in one burst | 5 | 
| ListRequestedServiceQuotaChangeHistoryByQuota requests per second | 5 | 
| Additional ListRequestedServiceQuotaChangeHistoryByQuota requests per second sent in one burst | 5 | 
| ListServiceQuotas requests per second | 10 | 
| Additional ListServiceQuotas requests per second sent in one burst | 10 | 
| ListServices requests per second | 10 | 
| Additional ListServices requests per second sent in one burst | 10 | 
| ListTagsForResource requests per second | 10 | 
| ListTagsForResource requests per second sent in one burst | 10 | 
| RequestServiceQuotaIncrease requests per second | 3 | 
| Additional RequestServiceQuotaIncrease requests per second sent in one burst | 3 | 
| TagResource requests per second | 10 | 
| TagResource requests per second sent in one burst | 10 | 
| UntagResource requests per second | 10 | 
| UntagResource requests per second sent in one burst | 10 | 


**Quota request template API request rates**  

| Quota | Default | 
| --- | --- | 
| AssociateQuotaTemplate requests per second | 1 | 
| Additional AssociateQuotaTemplate requests per second sent in one burst | 1 | 
| DeleteServiceQuotaIncreaseRequestFromTemplate requests per second | 2 | 
| Additional DeleteServiceQuotaIncreaseRequestFromTemplate requests per second sent in one burst | 1 | 
| DisassociateQuotaTemplate requests per second | 1 | 
| Additional DisassociateQuotaTemplate requests per second sent in one burst | 1 | 
| GetAssociationForQuotaTemplate requests per second | 2 | 
| Additional GetAssociationForQuotaTemplate requests per second sent in one burst | 2 | 
| GetServiceQuotaIncreaseRequestFromTemplate requests per second | 2 | 
| Additional GetServiceQuotaIncreaseRequestFromTemplate requests per second sent in one burst | 1 | 
| ListServiceQuotaIncreaseRequestsInTemplate requests per second | 2 | 
| Additional ListServiceQuotaIncreaseRequestsInTemplate requests per second sent in one burst | 1 | 
| PutServiceQuotaIncreaseRequestIntoTemplate requests per second | 1 | 
| Additional PutServiceQuotaIncreaseRequestIntoTemplate per second sent in one burst | 1 | 


**Overall API request rate**  

| Quota | Default | 
| --- | --- | 
| API requests per AWS account (requests per second) | 50 | 
| API requests per AWS Organization (requests per second) | 100 | 

# Service Quotas Document history
<a name="document-history"></a>

The following table describes the important changes to the documentation since the last release of Service Quotas. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Service Quotas Automatic Management](#document-history) | [Notify and Auto-Adjust](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html) allows AWS to monitors your service quotas usage and request a service quotas increase on your behalf. | November 21, 2025 | 
| [Updated managed policy](#document-history) | Service Quotas updated [`ServiceQuotasReadOnlyAccess`](https://docs.aws.amazon.com/servicequotas/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-POLICYNAME2)to support Automatic Management feature. | October 3, 2025 | 
| [Service Quotas Automatic Management](#document-history) | [Service Quotas Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html) allows AWS to monitors your service quotas usage and notifies you before you run out of your allocated quotas. | October 3, 2025 | 
| [Updated content](#document-history) | Updated topic titles and reorganized content to improve readability and discoverability.  | June 20, 2024 | 
| [Adding new AWS managed policies](https://docs.aws.amazon.com/servicequotas/latest/userguide/security-iam-awsmanpol.html) | You can now attach `ServiceQuotasFullAccess` and `ServiceQuotasReadOnlyAccess` policies to your users, groups, and roles.  | May 30, 2024 | 
| [Adding support for context based quota management](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) | You now have greater visibility and control over your service quotas. View applied values, monitor usage, and programmatically request increases for quotas that not only apply at the AWS account level, but at the resource level. | August 30, 2023 | 
| [IAM best practices update](#document-history) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | January 3, 2023 | 
| [Tagging Service Quotas resources](https://docs.aws.amazon.com/servicequotas/latest/userguide/sq-tagging.html) | You can now attach tags to applied quotas and write policies to control access to those quotas. | December 21, 2020 | 
| [Initial release](#document-history) | This release introduces Service Quotas. | June 24, 2019 | 