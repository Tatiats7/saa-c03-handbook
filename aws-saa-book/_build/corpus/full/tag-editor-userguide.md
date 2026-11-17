# Tagging AWS Resources and Tag Editor User Guide

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
+ [What is Tag Editor?](#tagging)
   + [Best practices and strategies](#best-practices-and-strats)
   + [Tagging categories](#tag-categories)
+ [Getting started with Tag Editor](#gettingstarted)
   + [Prerequisites for working with Tag Editor](#gettingstarted-prereqs)
   + [Set up permissions](#gettingstarted-prereqs-permissions)
+ [Finding resources to tag](#find-resources-to-tag)
   + [View and edit existing tags for a selected resource](#tagging-resources-view)
+ [Managing tags with Tag Editor](#tagging-resources)
   + [Add tags to selected resources](#tagging-resources-add)
   + [Edit tags of selected resources](#tagging-resources-edit)
   + [Remove tags from selected resources](#tagging-resources-delete)
+ [Using tags in IAM permission policies](#tags-in-iam-policies)
+ [AWS Organizations tag policies](#tag-policies-orgs)
   + [Evaluating compliance for an account](#tag-policies-orgs-finding-noncompliant-tags)
   + [Evaluating organization-wide compliance](#tag-policies-orgs-evaluating-org-wide-compliance)
+ [Monitor tag changes with serverless workflows and Amazon EventBridge](#tag-monitor)
   + [Tutorial: Automatically stopping Amazon EC2 instances that are missing required tags](#monitor-example)
+ [Troubleshooting tag changes](#troubleshooting-tags)
+ [Security in Tag Editor](#security)
   + [Data protection in Tag Editor](#data-protection)
   + [Identity and access management for Tag Editor](#security-iam)
      + [How Tag Editor works with IAM](#security_iam_service-with-iam)
      + [Tag Editor identity-based policy examples](#security_iam_id-based-policy-examples)
      + [Troubleshooting Tag Editor identity and access](#security_iam_troubleshoot)
   + [Logging and monitoring in Tag Editor](#logging-monitoring)
   + [Compliance validation for Tag Editor](#compliance-validation)
   + [Resilience in Tag Editor](#disaster-recovery-resiliency)
   + [Infrastructure security in Tag Editor](#infrastructure-security)
+ [Service quotas](#reference)
+ [Tag Editor document history](#doc-history)

-----



# What is Tag Editor?
<a name="tagging"></a>

Tag Editor enables you to effectively manage tags. *Tags* are key and value pairs that act as metadata for organizing your AWS resources. With most AWS resources, you have the option of adding tags when you create the resource. Examples of resources include an Amazon Elastic Compute Cloud (Amazon EC2) instance, an Amazon Simple Storage Service (Amazon S3) bucket, or a secret in AWS Secrets Manager. 

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

Tags can help you manage, identify, organize, search for, and filter resources. You can create tags to categorize resources by purpose, owner, environment, or other criteria.

Each tag has two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, or `Project`). Tag keys are case sensitive.
+ A *tag value* (for example, `111122223333` or `Production`). Like tag keys, tag values are case sensitive.

**Note**  
Although tag keys are case sensitive, IAM has additional validations for IAM resources to prevent the application of tag keys that only differ in casing. We recommend not using keys that only differ in casing. Refer to [Tags for IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) for more information.

## Resource tagging methods
<a name="intro-tag-methods"></a>

There are three ways to add tags to your AWS resources:
+ **AWS service API operation** – The tagging API operations supported directly an AWS service. To discover what tagging functionality each AWS service provides, see the service's documentation in the [AWS documentation index](https://docs.aws.amazon.com/index.html).
+ **Tag Editor console** – Some services support tagging with the Tag Editor console.
+ **Resource Groups Tagging API** – Most services also support tagging using the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html).

**Note**  
You can also use [AWS Service Catalog TagOptions Library](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/tagoptions.html) to easily manage tags on provisioned products. A *TagOption* is a key-value pair managed in Service Catalog. It is not an AWS tag, but serves as a template for creating an AWS tag based on the TagOption. 

You can tag resources for all cost-accruing services in AWS. For the following services, AWS recommends newer alternative AWS services that support tagging to better meet customer use cases.


|  |  |  | 
| --- |--- |--- |
| Amazon Cloud Directory | Amazon CloudSearch | Amazon Cognito Sync | 
| AWS Data Pipeline | Amazon Elastic Transcoder | Amazon Machine Learning | 
| AWS OpsWorks Stacks | Amazon Glacier Direct | Amazon SimpleDB | 
| Amazon WorkSpaces Application Manager | AWS DeepLens |  | 

### Learn more
<a name="more-info-tagging"></a>

This page provides general information on tagging AWS resources. For more information about tagging resources in a particular AWS service, see its documentation. The following are also good sources of information about tagging:
+ For information about the AWS Resource Groups Tagging API, see the [*Resource Groups Tagging API Reference Guide*](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html).
+ For information about the tagging functionality each AWS service provides, see the service's documentation in the [AWS documentation index](https://docs.aws.amazon.com/index.html).
+ For information about using tags in IAM policies to help control who can view and interact with your AWS resources, see [Controlling access to and for IAM users and roles using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) in the *IAM User Guide*.

## Best practices and strategies
<a name="best-practices-and-strats"></a>

These sections provide information about best practices and strategies when tagging your AWS resources and using Tag Editor. 



### Tagging best practices
<a name="tag-best-practices"></a>

As you create a tagging strategy for AWS resources, follow best practices:
+ Do not add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including billing. Tags are not intended to be used for private or sensitive data.
+ Use a standardized, case-sensitive format for tags, and apply it consistently across all resource types.
+ Consider tag guidelines that support multiple purposes, like managing resource access control, cost tracking, automation, and organization.
+ Use automated tools to help manage resource tags. Tag Editor and the [Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/) enable programmatic control of tags, making it easier to automatically manage, search, and filter tags and resources.
+ Use too many tags rather than too few tags.
+ Remember that it is easy to change tags to accommodate changing business requirements, but consider the consequences of future changes. For example, changing access control tags means you must also update the policies that reference those tags and control access to your resources.
+ You can automatically enforce the tagging standards that your organization chooses to adopt by creating and deploying tag policies using AWS Organizations. Tag policies let you specify tagging rules that define valid key names and the values that are valid for each key. You can choose to only monitor, giving you an opportunity to evaluate and clean up your existing tags. Once your tags are in compliance with your chosen standards, you can then turn on enforcement in the tag policies to prevent non-compliant tags from being created. For more information, see [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the *AWS Organizations User Guide*.

### Tag naming best practices
<a name="id_tags_naming_best_practices"></a>

These are several best practices and naming conventions that we recommend that you use with your tags. Refer to [Naming tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) in the *IAM User Guide* for more information.

A number of tags are predefined by AWS or created automatically by various AWS services. Many *AWS generated tags* use key names that are all lowercase, with hyphens separating words in the name, and prefixes followed by colons to identify the source service for the tag. For example, see the following: 
+ `aws:ec2spot:fleet-request-id` is a tag that identifies the Amazon EC2 Spot Instance Request that launched the instance.
+ `aws:cloudformation:stack-name` is a tag that identifies the CloudFormation stack that created the resource. 
+ `elasticbeanstalk:environment-name` is a tag that identifies the application that created the resource.

Consider naming your tags using the following rules:
+ Use all lowercase for the words.
+ Use hyphens to separate words.
+ Use a prefix followed by a colon to identify the organization name or abbreviated name. 

For example, for a fictitious company named *AnyCompany*, you might define tags such as:
+ `anycompany:cost-center` to identify the internal Cost Center code. 
+ `anycompany:environment-type` to identify whether the environment is development, test, or production.
+ `anycompany:application-id` to identify the application that the resource was created for. 

The prefix ensures that tags are clearly recognizable as defined by your organization and not by AWS or a third-party tool that you might be using. Using all lowercase with hyphens for separators avoids confusion about how to capitalize a tag name. For example, `anycompany:project-id` is simpler to remember than `ANYCOMPANY:ProjectID`, `anycompany:projectID`, or `Anycompany:ProjectId`.

#### Tag naming limits and requirements
<a name="tag-conventions"></a>

The following basic naming and usage requirements apply to tags:
+ Each resource can have a maximum of 50 user created tags. 
+ System created tags that begin with `aws:` are reserved for AWS use, and do not count against this limit. You can't edit or delete a tag that begins with the `aws:` prefix.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ The tag key must be a minimum of 1 and a maximum of 128 Unicode characters in UTF-8.
+ The tag value must be a minimum of 0 and a maximum of 256 Unicode characters in UTF-8.
+ Allowed characters can vary by AWS service. For information about what characters you can use to tag resources in a particular AWS service, see its documentation. In general, the allowed characters are letters, numbers, spaces representable in UTF-8, and the following characters: \_ . : / = \+ - @.
+ Tag keys and values are case sensitive. As a best practice, decide on a strategy for capitalizing tags, and consistently implement that strategy across all resource types. For example, decide whether to use `Costcenter`, `costcenter`, or `CostCenter`, and use the same convention for all tags. Avoid using similar tags with inconsistent case treatment. 

### Common tagging strategies
<a name="tag-strategies"></a>

Use the following tagging strategies to help identify and manage AWS resources.

**Topics**
+ [Tags for resource organization](#tag-strategies-console)
+ [Tags for cost allocation](#tag-strategies-cost-allocation)
+ [Tags for automation](#tag-strategies-automation)
+ [Tags for access control](#tag-strategies-access-control)
+ [Tagging governance](#tag-strategies-governance)

#### Tags for resource organization
<a name="tag-strategies-console"></a>

Tags are a good way to organize AWS resources in the AWS Management Console. You can configure tags to be displayed with resources, and can search and filter by tag. With the AWS Resource Groups service, you can create groups of AWS resources based on one or more tags or portions of tags. You can also create groups based on their occurrence in an AWS CloudFormation stack. Using Resource Groups and Tag Editor, you can consolidate and view data for applications that consist of multiple services, resources, and Regions in one place.

#### Tags for cost allocation
<a name="tag-strategies-cost-allocation"></a>

AWS Cost Explorer and detailed billing reports let you break down AWS costs by tag. Typically, you use business tags such as *cost center/business unit*, *customer*, or *project* to associate AWS costs with traditional cost-allocation dimensions. But a cost allocation report can include any tag. This lets you associate costs with technical or security dimensions, such as specific applications, environments, or compliance programs. 

For some services, you can use an AWS-generated `createdBy` tag for cost allocation purposes, to help account for resources that might otherwise go uncategorized. The `createdBy` tag is available only for supported AWS services and resources. Its value contains data associated with specific API or console events. For more information, see [AWS-Generated Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tags.html) in the *AWS Billing and Cost Management User Guide*.

#### Tags for automation
<a name="tag-strategies-automation"></a>

Resource or service-specific tags are often used to filter resources during automation activities. Automation tags are used to opt in or opt out of automated tasks or to identify specific versions of resources to archive, update, or delete. For example, you can run automated `start` or `stop` scripts that turn off development environments during nonbusiness hours to reduce costs. In this scenario, Amazon Elastic Compute Cloud (Amazon EC2) instance tags are a simple way to identify instances to opt out of this action. For scripts that find and delete stale, out-of-date, or rolling Amazon EBS snapshots, snapshot tags can add an extra dimension of search criteria.

#### Tags for access control
<a name="tag-strategies-access-control"></a>

IAM policies support tag-based conditions, letting you constrain IAM permissions based on specific tags or tag values. For example, IAM user or role permissions can include conditions to limit EC2 API calls to specific environments (such as development, test, or production) based on their tags. The same strategy can be used to limit API calls to specific Amazon Virtual Private Cloud (Amazon VPC) networks. Support for tag-based, resource-level IAM permissions is service specific. When you use tag-based conditions for access control, be sure to define and restrict who can modify the tags. For more information about using tags to control API access to AWS resources, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### Tagging governance
<a name="tag-strategies-governance"></a>

An effective tagging strategy uses standardized tags and applies them consistently and programmatically across AWS resources. You can use both reactive and proactive approaches for governing tags in your AWS environment.
+ **Reactive governance** is for finding resources that are not properly tagged using tools such as the Resource Groups Tagging API, AWS Config Rules, and custom scripts. To find resources manually, you can use Tag Editor and detailed billing reports.
+ **Proactive governance** uses tools such as CloudFormation, Service Catalog, tag policies in AWS Organizations, or IAM resource-level permissions to ensure standardized tags are consistently applied at resource creation.

  For example, you can use the CloudFormation `Resource Tags` property to apply tags to resource types. In Service Catalog, you can add portfolio and product tags that are combined and applied to a product automatically when it is launched. More rigorous forms of proactive governance include automated tasks. For example, you can use the Resource Groups Tagging API to search an AWS environment’s tags, or run scripts to quarantine or delete improperly tagged resources.

## Tagging categories
<a name="tag-categories"></a>

Companies that are most effective in their use of tags typically create business-relevant tag groupings to organize their resources along technical, business, and security dimensions. Companies that use automated processes to manage their infrastructure also include additional, automation-specific tags.


| Technical tags | Tags for automation | Business tags | Security tags | 
| --- | --- | --- | --- | 
|  +  **Name –** Identify individual resources <br />+  **Application ID –** Identify resources that are related to a specific application <br />+  **Application Role –** Describe the function of a particular resource (such as web server, message broker, database) <br />+  **Cluster –** Identify resource farms that share a common configuration and perform a specific function for an application <br />+  **Environment –** Distinguish between development, test, and production resources <br />+  **Version –** Help distinguish between versions of resources or applications   |  +  **Date/Time –** Identify the date or time a resource should be started, stopped, deleted, or rotated <br />+  **Opt in/Opt out –** Indicate whether a resource should be included in an automated activity such as starting, stopping, or resizing instances <br />+  **Security – **Determine requirements, such as encryption or enabling of Amazon VPC flow logs; identify route tables or security groups that need extra scrutiny   |  +  **Project –** Identify projects that the resource supports <br />+  **Owner –** Identify who is responsible for the resource <br />+  **Cost Center/Business Unit –** Identify the cost center or business unit associated with a resource, typically for cost allocation and tracking <br />+  **Customer –** Identify a specific client that a particular group of resources serves   |  +  **Confidentiality –** An identifier for the specific data confidentiality level a resource supports <br />+  **Compliance –** An identifier for workloads that must adhere to specific compliance requirements   | 

# Getting started with Tag Editor
<a name="gettingstarted"></a>

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

To add tags to—or edit or delete tags of—multiple resources at once, use Tag Editor. With Tag Editor, you search for the resources that you want to tag, and then manage tags for the resources in your search results. 

**To start Tag Editor**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home).

1. Perform either of the following steps:
   + Choose **Services**. Then, under **Management & Governance**, choose **Resource Groups & Tag Editor**. In the navigation pane on the left, choose **Tag Editor**.
   + Use the direct link: [AWS Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor/find-resources).

Not all resources can have tags applied. For information about which resources Tag Editor supports, see the **Tag Editor tagging**column at [Supported resource types](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *AWS Resource Groups User Guide*. If a resource type that you want to tag isn't supported, let AWS know by choosing **Feedback** in the lower left corner of the console window.

For information about permissions and roles that are required to tag resources, see [Set up permissions](#gettingstarted-prereqs-permissions).

**Topics**
+ [Prerequisites for working with Tag Editor](#gettingstarted-prereqs)
+ [Set up permissions](#gettingstarted-prereqs-permissions)

## Prerequisites for working with Tag Editor
<a name="gettingstarted-prereqs"></a>

Before you get started working to tag your resources, be sure you have an active AWS account with existing resources and appropriate rights to tag resources and create groups.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Create resources](#gettingstarted-prereqs-create)

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

### Create resources
<a name="gettingstarted-prereqs-create"></a>

You must have resources in your AWS account to tag. For more information about the supported resource types, see the **Tag Editor Tagging** column under [Supported resource types](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *AWS Resource Groups User Guide*.

## Set up permissions
<a name="gettingstarted-prereqs-permissions"></a>

To make full use of Tag Editor, you might need additional permissions to tag resources or to see a resource's tag keys and values. These permissions are in the following categories: 
+ Permissions for individual services so that you can tag resources from those services and include them in resource groups.
+ Permissions that are required to use the Tag Editor console.

If you're an administrator, you can provide permissions for your users by creating policies through the AWS Identity and Access Management (IAM) service. You first create IAM roles, users, or groups, and then apply the policies with the permissions that they need. For information about creating and attaching IAM policies, see [Working with policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingPolicies.html).

### Permissions for individual services
<a name="rg-perms-individual-services"></a>

**Important**  
This section describes permissions that are required if you want to tag resources **from other AWS service consoles and APIs**.

To add tags to a resource, you need the permissions required for the service to which the resource belongs. For example, to tag Amazon EC2 instances, you must have permissions to the tagging operations in that service's API, such as the [Amazon EC2 CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html) operation.

### Permissions required to use the Tag Editor console
<a name="gettingstarted-prereqs-permissions-te"></a>

To use the Tag Editor console to list and tag resources, the following permissions must be added to a user's policy statement in IAM. You can add either AWS managed policies that are maintained and kept up to date by AWS, or you can create and maintain your own custom policy.

#### Using AWS managed policies for Tag Editor permissions
<a name="prereqs-permissions-managedpolicies"></a>

Tag Editor supports the following AWS managed policies that you can use to provide a predefined set of permissions to your users. You can attach these managed policies to any role, user, or group just as you would any other policy that you create.

**[ResourceGroupsandTagEditorReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess)**  
This policy grants the attached IAM role or user permission to call the read-only operations for both AWS Resource Groups and Tag Editor. To read a resource's tags, you must also have permissions for that resource through a separate policy. Learn more in the following **Important** note.

**[ResourceGroupsandTagEditorFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess)**  
This policy grants the attached IAM role or user permission to call any Resource Groups operation and the read and write tag operations in Tag Editor. To read or write a resource's tags, you must also have permissions for that resource through a separate policy. Learn more in the following **Important** note.

**Important**  
The two previous policies grant permission to call the Tag Editor operations and use the Tag Editor console. However, you must also have permissions not only to invoke the operation, but also appropriate permissions to the specific resource whose tags you're trying to access. To grant that access to the tags, you must also attach one of the following policies:  
The AWS managed policy [ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess) grants permissions to the read-only operations for every service's resources. AWS automatically keeps this policy up to date with new AWS services as they become available.
Many services provide service-specific read-only AWS managed policies that you can use to limit access to only the resources provided by that service. For example, Amazon EC2 provides [AmazonEC2ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess).
You can create your own policy that grants access to only the specific read-only operations for the few services and resources you want your users to access. This policy uses either an allowlist strategy or a denylist strategy.  
An allowlist strategy takes advantage of the fact that access is denied by default until you ***explicitly allow*** it in a policy. So, you can use a policy like the following example.  

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [ "tag:*" ],
              "Resource": [
                  "arn:aws:ec2:{{us-east-1}}:{{444455556666}}:*",
                  "arn:aws:s3:::{{amzn-s3-demo-bucket2}}"
                  ]
          }
      ]
  }
  ```
Alternatively, you could use a denylist strategy that allows access to all resources except those that you explicitly block. This requires a separate policy that applies to the relevant users that allows access. The following example policy then denies access to the specific resources listed by the Amazon Resource Name (ARN).  

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Deny",
              "Action": [ "tag:*" ],
              "Resource": [
                  "arn:aws:ec2:{{us-east-1}}:{{123456789012}}:instance:*",
                  "arn:aws:s3:::{{amzn-s3-demo-bucket3}}"
               ]
          }
      ]
  }
  ```

#### Adding Tag Editor permissions manually
<a name="prereqs-permissions-manualadd"></a>
+ `tag:*` (This permission allows all Tag Editor actions. If you instead want to restrict actions that are available to a user, you can replace the asterisk with a [specific action](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awsresourcegroups.html), or with a comma-separated list of actions.)
+ `tag:GetResources`
+ `tag:TagResources`
+ `tag:UntagResources`
+ `tag:getTagKeys`
+ `tag:getTagValues`
+ `resource-explorer:*`
+ `resource-groups:SearchResources`
+ `resource-groups:ListResourceTypes`

**Note**  
The `resource-groups:SearchResources` permission allows Tag Editor to list resources when you filter your search using tag keys or values.   
The `resource-explorer:ListResources` permission allows Tag Editor to list resources when you search resources without defining search tags. 

### Granting permissions for using Tag Editor
<a name="gettingstarted-prereqs-permissions-howto"></a>

To add a policy for using AWS Resource Groups and Tag Editor to a role, do the following.

1. Open the [IAM console to the **Roles** page](https://console.aws.amazon.com/iamv2/home#/roles).

1. Find the role to which you want to grant Tag Editor permissions. Choose the role's name to open the role's **Summary** page.

1. On the **Permissions** tab, choose **Add permissions**.

1. Choose **Attach existing policies directly**.

1. Choose **Create policy**.

1. On the **JSON** tab, paste the following policy statement.

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
           "tag:GetResources",
           "tag:TagResources",
           "tag:UntagResources",
           "tag:getTagKeys",
           "tag:getTagValues",
           "resource-explorer:*",
           "resource-groups:SearchResources",
           "resource-groups:ListResourceTypes"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

------
**Note**  
This example policy statement grants permissions to perform only Tag Editor actions.

1. Choose **Next: Tags** and then choose **Next: Review**.

1. Enter a name and description for the new policy. For example, **AWSTaggingAccess**.

1. Choose **Create policy**.

Now that the policy is saved in IAM, you can attach it to other principals, such as roles, groups, or users. For more information about how to add a policy to a principal, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

### Authorization and access control based on tags
<a name="rg-perms-iam"></a>

AWS services support the following:
+ **Action-based policies** – For example, you can create a policy that allows users to perform `GetTagKeys` or `GetTagValues` operations, but no others.
+ **Resource-level permissions in policies** – Many services support using [ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) to specify individual resources in the policy.
+ **Authorization based on tags** – Many services support using resource tags in the condition of a policy. For example, you can create a policy that allows users full access to a group that has the same tag as the users. For more information, see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *AWS Identity and Access Management User Guide*.
+ **Temporary credentials** – Users can assume a role with a policy that allows Tag Editor operations.

Tag Editor doesn't use any service-linked roles.

For more information about how Tag Editor integrates with AWS Identity and Access Management (IAM), see the following topics in the *AWS Identity and Access Management User Guide*:
+ [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html#management_svcs)
+ [Actions, resources, and condition keys for Tag Editor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstageditor.html)
+ [Controlling access to AWS resources using policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html)

# Finding resources to tag
<a name="find-resources-to-tag"></a>

With Tag Editor, you build a query to find resources in one or more AWS Regions that are available for tagging. You can choose up to 20 individual resource types, or build a query on **All resource types**. Your query can include resources that already have tags, or resources that have no tags. For more information, see the **Tag Editor Tagging** column at [Supported resource types](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *AWS Resource Groups User Guide*.

After you find resources to tag, you can use Tag Editor to add tags, or view, edit, or delete tags.

**To find resources to tag**

1. Open the [Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor).

1. *(Optional)* Choose the AWS Regions in which to search for resources to tag. By default, your current Region is used. For this procedure, choose **us-east-1** and **us-west-2**.

1. Choose at least one resource type from the **Resource types** dropdown list. You can add or edit tags for up to 20 individual resource types at a time, or choose **All resource types**. For this procedure, choose **AWS::EC2::Instance** and **AWS::S3::Bucket**.

1. *(Optional)* In the **Tags** fields, enter a tag key, or a tag key and value pair, to limit the resources in the current AWS Region to only those that are tagged with your specified values. As you enter a tag key, matching tag keys in the current Region appear in a list. You can choose a tag key from the list. Tag Editor auto-completes the tag key for you as you type enough characters to match an existing key. Choose **Add** or press **Enter** when you've finished your tag. In this example, filter for resources that have a tag key of **Stage**. The tag value is optional but narrows the results of the query further. To add more tags, choose **Add**. Queries assign an `AND` operator to tags, so only resources that match both the specified resource type and all specified tags are returned by the query.
**Note**  
The Tag Editor console doesn't currently support wildcards.

   To find resources with multiple values for a tag key, add another tag with the same key to the query, but specify a different value. The results include all resources that are tagged with the same tag key and that have any of the selected values. The search is case sensitive.

   Leave the **Tags** boxes empty to find all resources of the specified type in the selected AWS Regions. This query returns resources that have any tags, and includes those that have no tags. To remove a tag from your query, choose **X** on the tag's label.

   To find resources that have a tag, but with an empty value, choose **(empty value)**. 
**Note**  
Before you can find resources with the specified tags, they must have been applied to at least one resource of the specified type in the current AWS Region.

1. When your query is ready, choose **Search resources**. Results are displayed as a table in the **Resource search results** area.

   To filter a large number of resources, enter any filter text, such as part of the name of a resource, in **Filter resources**.
**Note**  
You can use substrings to filter your results.

1. *(Optional)* To configure the columns that Tag Editor displays in your resource search results, choose the **Preferences** gear icon in the **Resource search results**.

   On the **Preferences** page, choose the number of rows that you want displayed in your search results. If you'd like to see all the text in the table, select the ** Wrap lines** check box.

   Turn on columns that you want Tag Editor to display in your results. You can show a column for each tag that occurs in your search results or a selected subset of your search results. You can do this anytime after you find resources to tag. To enable a column, choose the switch icon next to the tag and change it from off to on.

   When you are finished configuring visible columns and number of displayed rows, choose **Confirm**.

## View and edit existing tags for a selected resource
<a name="tagging-resources-view"></a>

Tag Editor shows you the existing tags on selected resources that are in the results of your **Find resources to tag** query. 

If you enabled any **Tag** columns as described in the previous section, you can see the current value of that tag for each resource in the search results.

**Note**  
This topic explains how to edit the tag for an *individual* resource. You can also bulk edit tags for several selected resources at the same time. For more information, see [Managing tags with Tag Editor](#tagging-resources).

**To edit tags inline in the search results table**

1. Choose the value for the tag on the resource that you want to edit. 
**Note**  
If the chosen resource currently does not have a tag with the chosen key, the value displays as **(not tagged)**.
If the chosen resource does have a tag with the chosen key but without a value, the value displays as '**–**'. 

1. You can enter a new value or choose from any of the values already present on other resources with this tag. You can also delete the tag from this one resource by choosing **Remove tag**.

**To view all tags for an individual resource**

1. In the results of your **Find resources to tag** query, choose the number in the **Tags** column for any resource for which you want to view existing tags. Resources with a dash in the **Tags** column do not have existing tags.

1. View existing tags in **Resource tags**. You can also open this window by choosing **Manage tags of selected resources**, when you're changing or removing tags from the **Manage tags** page.
**Note**  
If you don’t see a tag that you recently applied to a resource, try refreshing your browser window.

### Export results to .csv file
<a name="tagging-resources-csv"></a>

You can export the results of a **Find resources to tag** query to a comma-separated values (.csv) file. The .csv file includes the resource names, services, Region, resource IDs, the total number of tags, and a column for each unique tag key in the collection. The .csv file can help you develop a tagging strategy for resources in your organization, or determine where there are overlaps or inconsistencies in tagging across resources.

1. In the results of your **Find resources to tag** query, choose **Export resources to CSV**.

1. When you're prompted by your browser, choose to open the .csv file, or save it to a convenient location.

# Managing tags with Tag Editor
<a name="tagging-resources"></a>

After you [find resources](#find-resources-to-tag) that you want to tag, you can add, remove, and edit the tags for some or all of your search results. Tag Editor shows you any tags that are attached to resources. It also shows you whether those tags were added in Tag Editor, by the resource's service console, or by using the API.

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

**Other ways to manage your tags**  
This topic discusses tagging resources by using Tag Editor in the AWS Management Console. However, you can also manage the tags on your AWS resources by using the following tools:  
You can type or script commands at your shell prompt by using the [`resourcegroupstaggingapi` commands](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html#cli-aws-resourcegroupstaggingapi) in the AWS Command Line Interface (AWS CLI).
You can create and run PowerShell scripts by using the [AWS Resource Groups Tagging API](https://docs.aws.amazon.com/powershell/latest/reference/items/ResourceGroupsTaggingAPI_cmdlets.html) in the AWS Tools for PowerShell Core.
You can create and run programs with any of the available [AWS SDKs](https://docs.aws.amazon.com/index.html#sdks) by using the [Resource groups tagging APIs](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/), such as the [tagging APIs for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resourcegroupstaggingapi.html) or the [tagging APIs for Java](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/ResourceGroupsTaggingAPI.html).

When you add, remove, or edit existing tags, you're changing tags only on those resources that you select in the results of your **Find resources to tag** query. You can select up to 500 resources on which to manage tags.

## Add tags to selected resources
<a name="tagging-resources-add"></a>

You can use Tag Editor to add tags to selected resources that are in the results of your **Find resources to tag** query.

**Note**  
This topic describes how to bulk edit the tags for *multiple* resources. You can also edit the tag values for an individual resource. For more information, see [View and edit existing tags for a selected resource](#tagging-resources-view).

1. Open the [Tag Editor console](https://console.aws.amazon.com/resource-groups/tag-editor), and submit a query that returns multiple resources that you want to tag.

1. In the results table of your **Find resources to tag** query, select the check boxes next to the resources that you want to add tags to. Enter a text string in **Filter resources** at the top of the table to filter for part of a resource's name, ID, tag keys, or tag values. In the **Tags** column, note that resources in the results already have tags applied to them.

1. Select the check box for one or more resources, and then choose **Manage tags of the selected resources**.

1. On the **Manage tags** page, view the tags on the resources that you selected. Although your original query returned more resources, you're adding tags to only those resources that you selected in step 1. Choose **Add tag**.

1. Enter a tag key and an optional tag value. For this procedure, you'll add the tag key **Team** and the tag value **Development**.
**Note**  
A resource can have a maximum of 50 user-applied tags. You might not be able to add new tags to a resource if you're approaching 50 user-applied tags. AWS generated tags don't apply to the 50-tag limit. Tag keys must also be unique within your selected resources. You can't add a new tag with a key that matches a tag key that already exists in your selected resources. 

1. When you're finished adding tags, choose **Review and apply changes**.

1. If you accept the changes, choose **Apply changes to all selected**.

1. Depending on the number of resources you select, applying new tags can take a few minutes. Don't leave the page or open a different page in the same browser tab. If changes were successful, a green success banner is displayed at the top of the page. Wait for a success or failure banner to appear on the page before you continue.

   If tag changes to some or all resources were not successful, see [Troubleshooting tag changes](#troubleshooting-tags). After you resolve the unsuccessful tag changes (such as insufficient permissions), you can retry the tag changes on resources for which tag changes failed. For more information, see [Retry failed tag changes](#tagging-resources-retry).

## Edit tags of selected resources
<a name="tagging-resources-edit"></a>

You can use Tag Editor to change existing tag values on selected resources that are in the results of your [**Find resources to tag**](#find-resources-to-tag) query. Editing a tag changes the tag's value on all selected resources that have the same tag key. You can't rename a tag key, but you can delete a tag and create a tag with a new name to replace the original tag key. This deletes all tags with that key on selected resources.

**Important**  
Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.

1. In the results of your **Find resources to tag** query, select the check boxes next to the resources for which you want to change existing tags. Enter a text string in **Filter resources** to filter for part of a resource's name or ID. In the **Tags** column, note that resources in the results already have tags applied to them. 

1. Choose **Manage tags of the selected resources**.

1. On the **Manage tags** page, in **Edit tags of selected resources**, view the tags on the resource that you selected. Although your original query might have returned more resources, you are changing tags for only those resources that you selected in step 1.

1. Change, add, or delete tag values. Existing tags must have a tag key, but tag values are optional. 

   In this procedure, we change the value of the **Team** tag to **QA**.

   If resources in your selection have different values for the same key, **Selected resources have different tag values** is displayed in the **Tag value** field. In this case, placing your cursor in the box opens a dropdown list of all available values for this tag key in your selected resources.

   If resources in your selection have the tag value you want, the tag value is highlighted as you type it. For example, if resources in your selection already have the tag value **QA**, the value is highlighted as you type **Q**. The values in the dropdown list help keep tag values consistent across resources. The tag value is changed on all selected resources. In this example, the tag value is changed to **QA** for all selected resources that had a **Team** tag key. For selected resources that don't have the **Team** tag, the **Team** tag with the value **QA** is added.

1. When you're finished changing tags, choose **Review and apply changes**.

1. If you accept the changes, choose **Apply changes to all selected**.

1. Depending on the number of resources you selected, editing tags can take a few minutes. Don't leave the page or open a different page in the same browser tab. If changes were successful, a green success banner is displayed at the top of the page. Wait for a success or failure banner to appear on the page before you continue.

   If tag changes to some or all resources were not successful, see [Troubleshooting tag changes](#troubleshooting-tags). After you resolve the root causes of unsuccessful tag changes (such as insufficient permissions), you can retry tag changes on resources for which tag changes failed. For more information, see [Retry failed tag changes](#tagging-resources-retry).

## Remove tags from selected resources
<a name="tagging-resources-delete"></a>

You can use Tag Editor to remove tags from selected resources that are in the results of your [**Find resources to tag**](#find-resources-to-tag) query. Removing a tag deletes the tag from all selected resources that have the tag. Because you can't edit tag keys, you can remove tags and replace them with new tags if you need to edit a tag key. This deletes all tags with that key on selected resources.

1. In the results of your **Find resources to tag** query, select the check boxes next to the resources you want to remove tags from. Enter a text string in **Filter resources** to filter for part of a resource's name or ID.

1. Choose **Manage tags of the selected resources**.

1. On the **Manage tags** page, in **Edit tags of selected resources**, view the tags on the resources that you selected. Although your original query might have returned more resources, you're changing tags for only those resources that you selected in step 1.

1. Choose **Remove tag** next to any tags that you want to delete. In this procedure, we remove the **Team** tag.
**Note**  
Choosing **Remove tag** removes a tag from all selected resources that have the tag. 

1. Choose **Review and apply changes**.

1. On the confirmation page, choose **Apply changes to all selected**.

1. Depending on the number of resources you selected, removing tags can take a few minutes. Don't leave the page or open a different page in the same browser tab. If changes were successful, a green success banner is displayed at the top of the page. Wait for a success or failure banner to appear on the page before you continue.

   If tag changes to some or all resources were not successful, see [Troubleshooting Tag Changes](#troubleshooting-tags). After you resolve the root causes of unsuccessful tag changes (such as insufficient permissions), you can retry tag changes on resources for which tag changes failed. For more information, see [Retry failed tag changes](#tagging-resources-retry).

# Using tags in IAM permission policies
<a name="tags-in-iam-policies"></a>

[AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/) is the AWS service that you use to create and manage permissions policies that determine who can access your AWS resources. Every attempt to access an AWS service or read or write an AWS resource is access controlled by an IAM policy.

These policies allow you to provide granular access to your resources. One of the features you can use to fine tune this access is the [`Condition`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) element of the policy. This element lets you specify the conditions that must match the request to determine if the request can proceed. Among the things you can check with the `Condition` element are the following:
+ Tags that are attached to the user or role making the request.
+ Tags attached to the resource that is the object of the request.

## Tags and attribute-based access control
<a name="tagging-and-abac"></a>

Tags can be an important part of your AWS access control strategy. For information about using tags as the attributes in an attribute-based access control (ABAC) strategy, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) and [Controlling access to and for IAM users and roles using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html), both in the *IAM User Guide*.

There is a comprehensive tutorial that shows how to grant access to different projects and groups using tags at [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *AWS Identity and Access Management User Guide*.

If you use a SAML-based identity provider (IdP) for single sign-in, you can attach tags to the assumed roles providing access to your users. For more information, see [IAM tutorial: Use SAML session tags for ABAC](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_abac-saml.html) in the *AWS Identity and Access Management User Guide*.

## Tag-related condition keys
<a name="tags-condition-keys"></a>

The following table describes the condition keys that you can use in an IAM permissions policy to control access based on tags. These condition keys let you do the following: 
+ Compare the tags on the principal calling the operation.
+ Compare the tags provided to the operation as a parameter.
+ Compare the tags attached to the resource that would be accessed by the operation.

For complete details about a condition key and how to use it, see the page linked in the **Condition key name** column.


| Condition key name | Description | 
| --- | --- | 
| [aws:PrincipalTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag) | Compares the tag attached to the principal (IAM role or user) making the request with the tag that you specify in the policy. | 
| [aws:RequestTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag) | Compares the tag key-value pair that was passed to the request as a parameter with the tag key-value pair that you specify in the policy. | 
| [aws:ResourceTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) | Compares the key-value pair that is attached to the resource with the tag key-value pair that you specify in the policy. | 
| [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys) | Compares only the tag keys in the request with the keys that you specify in the policy.  | 

## Example IAM policies that use tags
<a name="tags-iam-policy-examples"></a>

**Example 1: Force users to attach a specific tag when they create a resource**  
The following example IAM permissions policy shows how to force the user who creates or modifies an IAM policy's tags to include a tag with the key `Owner`. Also, the policy requires that the value of the tag is set to the same value as the `Owner` tag currently attached to the calling principal. For this strategy to work, all principals must have an `Owner` tag attached, and users must be prevented from modifying that tag. If an attempt to create or modify a policy occurs without including the `Owner` tag, the policy doesn't match and the operation isn't allowed.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "TagCustomerManagedPolicies",
            "Effect": "Allow",
            "Action": [
                "iam:CreatePolicy",
                "iam:TagPolicy"
            ],
            "Resource": "arn:aws:iam::123456789012:policy/*",
            "Condition": {
                "StringEquals": {"aws:RequestTag/Owner": "${aws:PrincipalTag/Owner}"}
            }
        }
    ]
}
```

**Example 2: Use tags to limit access to a resource to its "owner"**  
The following example IAM permissions policy lets the user stop a running Amazon EC2 instance only if the calling principal is tagged with the same `project` tag value as the instance.    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": [
        "ec2:StopInstances"
      ],
      "Resource": [
        "arn:aws:iam::123456789012:instance/*"
      ],
      "Condition": {
        "StringEquals": {"aws:ResourceTag/project": "${aws:PrincipalTag/project}"}
      }
    }
  ]
}
```
This example is an example of [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html). For more information and additional examples of using IAM policies to implement a tag-based access control strategy, see the following topics in the *AWS Identity and Access Management User Guide*:  
+ [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)
+ [Controlling access to and for IAM users and roles using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html)
+ [IAM tutorial: Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) – Shows how to grant access to different projects and groups using multiple tags. 

# AWS Organizations tag policies
<a name="tag-policies-orgs"></a>

A [*tag policy*](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) is a type of policy that you create in AWS Organizations. You can use tag policies to help standardize tags across the resources in your organization's accounts. To use tag policies, we recommend that you follow the workflows described in [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html) in the *AWS Organizations User Guide*. As mentioned on that page, the recommended workflows include finding and correcting noncompliant tags. To accomplish these tasks, you use the Tag Editor console. 

## Prerequisites and permissions
<a name="tag-policies-prereqs"></a>

Before you can evaluate compliance with tag policies in Tag Editor, you must meet the requirements and set the necessary permissions. 

**Topics**
+ [Prerequisites for evaluating compliance with tag policies](#tag-policies-prereqs-overview)
+ [Permissions for evaluating compliance for an account](#tag-policies-permissions-account)
+ [Permissions for evaluating organization-wide compliance](#tag-policies-permissions-org)
+ [Amazon S3 bucket policy for report storage](#bucket-policy)

### Prerequisites for evaluating compliance with tag policies
<a name="tag-policies-prereqs-overview"></a>

Evaluating compliance with tag policies requires the following:
+ You must first enable the feature in AWS Organizations, and create and attach tag policies. For more information, see the following pages in the *AWS Organizations User Guide*:
  + [Prerequisites and permissions for managing tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-prereqs.html)
  + [Enabling tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html)
  + [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html)
+ To [**find noncompliant tags on an account's resources**](#tag-policies-orgs-finding-noncompliant-tags), you need sign-in credentials for that account and the permissions listed in [Permissions for evaluating compliance for an account](#tag-policies-permissions-account).
+ To [**evaluate organization-wide compliance**](#tag-policies-orgs-evaluating-org-wide-compliance), you need sign-in credentials for the organization's management account and the permissions listed in [Permissions for evaluating organization-wide compliance](#tag-policies-permissions-org). You can request the compliance report from only the AWS Region US East (N. Virginia) .

### Permissions for evaluating compliance for an account
<a name="tag-policies-permissions-account"></a>

Finding noncompliant tags on an account's resources requires the following permissions:
+ `organizations:DescribeEffectivePolicy` – To get the contents of the effective tag policy for the account.
+ `tag:GetResources` – To get a list of resources that don't comply with the attached tag policy.
+ `tag:TagResources` – To add or update tags. You also need service-specific permissions to create tags. For example, to tag resources in Amazon Elastic Compute Cloud (Amazon EC2), you need permissions for `ec2:CreateTags`.
+ `tag:UnTagResources` – To remove a tag. You also need service-specific permissions to remove tags. For example, to untag resources in Amazon EC2, you need permissions for `ec2:DeleteTags`.

The following example AWS Identity and Access Management (IAM) policy provides permissions for evaluating tag compliance for an account.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EvaluateAccountCompliance",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeEffectivePolicy",
                "tag:GetResources",
                "tag:TagResources",
                "tag:UnTagResources"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For more information about IAM policies and permissions, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

### Permissions for evaluating organization-wide compliance
<a name="tag-policies-permissions-org"></a>

Evaluating organization-wide compliance with tag policies requires the following permissions:
+ `organizations:DescribeEffectivePolicy` – To get the contents of the tag policy that's attached to the organization, organizational unit (OU), or account.
+ `tag:GetComplianceSummary` – To get a summary of noncompliant resources in all accounts in the organization.
+ `tag:StartReportCreation` – To export the results of the most recent compliance evaluation to a file. Organization-wide compliance is evaluated every 48 hours. 
+ `tag:DescribeReportCreation` – To check the status of report creation.
+ `s3:ListAllMyBuckets` — To assist with accessing the organization-wide compliance report. 
+ `s3:GetBucketAcl` – To inspect the Access Control List (ACL) of the Amazon S3 bucket receiving the compliance report.
+ `s3:GetObject` – To retrieve the compliance report from the service-owned Amazon S3 bucket.
+ `s3:PutObject` – To place the compliance report in the specified Amazon S3 bucket.
+ `s3:PutObject` with `Null: {s3:x-amz-copy-source: true}` – Required to allow multipart upload operations (`InitiateMultipartUpload`, `CompleteMultipartUpload`) when the service delivers large compliance reports. These operations do not include a copy-source header, so they require a separate statement from the copy-based delivery.

If the Amazon S3 bucket where the report is being delivered is encrypted via SSE-KMS, you must also have the `kms:GenerateDataKey` permission for that bucket. 

The following example IAM policy provides permissions for evaluating organization-wide compliance. Replace each {{placeholder}} with your own information: 
+ {{`bucket_name`}} – Your Amazon S3 bucket name 
+ {{`organization_id`}} – Your organization's ID 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EvaluateAccountCompliance",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeEffectivePolicy",
                "tag:StartReportCreation",
                "tag:DescribeReportCreation",
                "tag:GetComplianceSummary",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "GetBucketAclForReportDelivery",
            "Effect": "Allow",
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::{{bucket_name}}",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
                }
            }
        },
        {
            "Sid": "GetObjectForReportDelivery",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::*/tag-policy-compliance-reports/*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
                }
            }
        },
        {
            "Sid": "PutObjectForReportDelivery",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{bucket_name}}/AwsTagPolicies/{{organization_id}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
                },
                "StringLike": {
                    "s3:x-amz-copy-source": "*/tag-policy-compliance-reports/*"
                }
            }
        },
        {
            "Sid": "PutObjectCreateMultipartUpload",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::{{bucket_name}}/AwsTagPolicies/{{organization_id}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "tagpolicies.tag.amazonaws.com"
                },
                "Null": {
                    "s3:x-amz-copy-source": "true"
                }
            }
        }
    ]
}
```

------

For more information about IAM policies and permissions, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

### Amazon S3 bucket policy for report storage
<a name="bucket-policy"></a>

To create an organization-wide compliance report, the identity that you use to call the `StartReportCreation` API must have access to an Amazon Simple Storage Service (Amazon S3) bucket in the US East (N. Virginia) Region to store the report. Tag Policies uses the credentials of the calling identity to deliver the compliance report to the specified bucket. 

If the bucket and the identity being used to call the `StartReportCreation` API *belong to the same account*, additional Amazon S3 bucket policies are not needed for this use case. 

If the account associated with the identity used to call the `StartReportCreation` API is *different* from the account that owns the Amazon S3 bucket, the following bucket policy must be attached to the bucket. Replace each {{placeholder}} with your own information: 
+ {{`bucket_name`}} – Your Amazon S3 bucket name 
+ {{`organization_id`}} – Your organization's ID 
+ {{`identity_ARN`}} – The ARN of the IAM identity used to call the `StartReportCreation` API 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	  
    "Statement": [ 
        { 
            "Sid": "CrossAccountTagPolicyACL", 
            "Effect": "Allow", 
            "Principal": {
                "AWS": "{{identity_ARN}}"
            }, 
            "Action": "s3:GetBucketAcl", 
            "Resource": "arn:aws:s3:::{{bucket_name}}"
         }, 
         { 
            "Sid": "CrossAccountTagPolicyBucketDelivery", 
            "Effect": "Allow", 
            "Principal": {
                "AWS": "{{identity_ARN}}"
            }, 
            "Action": "s3:PutObject", 
            "Resource": "arn:aws:s3:::{{bucket_name}}/AwsTagPolicies/{{organization_id}}/*"
         } 
    ] 
}
```

------

## Evaluating compliance for an account
<a name="tag-policies-orgs-finding-noncompliant-tags"></a>

You can evaluate the compliance of an account in your organization with its effective tag policy.

**Important**  
Untagged resources don't appear as noncompliant in results.  
To find untagged resources in your account, use AWS Resource Explorer with a query that uses **tag:none**. For more information, see [Search for untagged resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-examples.html#example-1) in the *AWS Resource Explorer User Guide*.

The *[effective tag policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-effective.html)* specifies the tagging rules that apply to an account. The effective tag policy is the aggregation of any tag policies that the account inherits, plus any tag policy directly attached to the account. When you attach a tag policy to the organization root, it applies to all accounts in your organization. When you attach a tag policy to an organizational unit (OU), it applies to all accounts and OUs that belong to the OU.

**Note**  
If you haven't yet created tag policies, see [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/tag-policies-getting-started.html) in the *AWS Organizations User Guide*.

To find noncompliant tags, you must have the following permissions:
+ `organizations:DescribeEffectivePolicy`
+ `tag:GetResources`
+ `tag:TagResources`
+ `tag:UntagResources`

**To evaluate an account's compliance with its effective tag policy (console)**

1. While signed in to the account whose compliance you want to check, open the [Tag Policies console](https://console.aws.amazon.com/resource-groups/tag-policies/).

1. The **Effective tag policy** section shows when the policy was last updated and the defined tag keys. You can expand a tag key to see information about its values, case treatment, and whether the values are enforced for specific resources types.
**Note**  
If you're signed in to the management account, you need to choose an account to see its effective policy and view compliance information.

1. In the **Resources with noncompliant tags** section, specify which AWS Region to search for noncompliant tags. Optionally, you can also search by resource type. Then choose **Search resources**.

   Real-time results are shown in the **Search results** section. To change the number of results returned per page or the columns to display, choose the settings icon. 

1. In the search results, select a resource with noncompliant tags.

1. In the dialog box that lists the resource's tags, choose the hyperlink to open the AWS service where the resource was created. From that console, correct the noncompliant tag.
**Tip**  
If you're not sure which tags are noncompliant, go to the **Effective tag policy** section for the account in the Tag Policies console. You can expand a tag key to view its tagging rules. 

1. Repeat the process of finding and correcting tags until the account resources that you care about are compliant in each Region.

**To find noncompliant tags (AWS CLI, AWS API)**  
Use the following commands and operations to find noncompliant tags:
+ AWS Command Line Interface (AWS CLI):
  + [aws resourcegroupstaggingapi get-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html)
  + [aws resourcegroupstaggingapi tag-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/tag-resources.html)
  + [aws resourcegroupstaggingapi untag-resources](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/untag-resources.html)

  For the complete procedure for using tag policies in the AWS CLI, see [Using tag policies in the AWS CLI](https://docs.aws.amazon.com/organizations/latest/userguide/tag-policy-cli.html) in the *AWS Organizations User Guide*.
+ AWS Resource Groups Tagging API:
  + [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html)
  + [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html)
  + [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html)

**Next steps**  
 We recommend that you repeat the process of finding and correcting compliance issues. Continue until the account's resources that you care about are compliant with the effective tag policy in each Region.

Finding and correcting noncompliant tags is an iterative process for multiple reasons, including the following:
+ Your organization's use of tag policies can evolve over time.
+ It takes time to effect change in your organization when creating resources.
+ Compliance can change anytime that a new resource is created or when new tags are assigned to a resource. 
+ An account's effective tag policy is updated whenever a tag policy is attached to or detached from it. The effective tag policy is also updated whenever changes occur to tag the policies that the account inherits.

If you're signed in as the management account in the organization, you can also generate a report. This report shows information about all tagged resources in your organization's accounts. For more information, see [Evaluating organization-wide compliance](#tag-policies-orgs-evaluating-org-wide-compliance).

## Evaluating organization-wide compliance
<a name="tag-policies-orgs-evaluating-org-wide-compliance"></a>

You can evaluate your organization's compliance with its effective tag policy. You can generate a report that lists all tagged resources in accounts across your organization and whether each resource is compliant with the effective tag policy.

**Important**  
Untagged resources don't appear as noncompliant in results.   
To find untagged resources in your account, use AWS Resource Explorer with a query that uses **tag:none**. For more information, see [Search for untagged resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-examples.html#example-1) in the *AWS Resource Explorer User Guide*.

You can generate the report from your organization's management account in the `us-east-1` AWS Region only. The account generating the report must have access to an Amazon S3 bucket in the US East (N. Virginia) Region. The bucket must have an attached bucket policy as shown in [Amazon S3 bucket policy for storing report](#bucket-policy). 

To generate an organization-wide compliance report, you must have the following permissions:
+ `organizations:DescribeEffectivePolicy`
+ `tag:GetComplianceSummary`
+ `tag:StartReportCreation`
+ `tag:DescribeReportCreation`
+ `s3:ListAllMyBuckets`
+ `s3:GetBucketAcl`
+ `s3:GetObject`
+ `s3:PutObject`

For an example IAM policy displaying these permissions, review [ Permissions for evaluating organization-wide compliance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-permissions-org). 

**To generate an organization-wide compliance report (console)**

1. Open the [Tag Policies console](https://console.aws.amazon.com/resource-groups/tag-policies/).

1. Choose the **This organization root** tab, and near the bottom of the page, choose **Generate report**.

1. On the **Generate report** screen, specify where to store the report. 

1. Choose **Start exporting**.

When the report is complete, you can download it from the **Noncompliance report** section on the **Organization root** tab. 

**Notes**  
Organization-wide compliance is evaluated every 48 hours. This results in the following:  
It can take up to 48 hours for changes to a tag policy or resources to be shown in the organization-wide compliance report. For example, assume that you have a tag policy that defines a new standardized tag for a resource type. Resources of that type that don't have this tag can show as compliant in the report for up to 48 hours.
Although you can generate the report at any time, report results aren't updated until the next evaluation is complete.
The **NoncompliantKeys** column lists tag keys on the resource that are noncompliant with the effective tag policy.
The **KeysWithNonCompliantValues** column lists keys defined in the effective policy that are on the resource with either incorrect case treatment or noncompliant values. 
If you close an AWS account that was a member of the organization, it can continue to appear in the tag compliance report for up to 90 days.

**To generate an organization-wide compliance report (AWS CLI, AWS API)**  
Use the following commands and operations to generate an organization-wide compliance report, check on its status, and view the report:
+ AWS Command Line Interface AWS CLI):
  + [aws resourcegroupstaggingapi start-report-creation](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/start-report-creation.html)
  + [aws resourcegroupstaggingapi describe-report-creation](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/describe-report-creation.html)
  + [aws resourcegroupstaggingapi get-compliance-summary](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-compliance-summary.html)

  For the complete procedure for using tag policies in the AWS CLI, see [Using tag policies in the AWS CLI](https://docs.aws.amazon.com/organizations/latest/userguide/tag-policy-cli.html) in the *AWS Organizations User Guide*.
+ AWS API:
  + [StartReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_StartReportCreation.html)
  + [DescribeReportCreation](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_DescribeReportCreation.html)
  + [GetComplianceSummary](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html)

# Monitor tag changes with serverless workflows and Amazon EventBridge
<a name="tag-monitor"></a>

Amazon EventBridge supports tag changes on AWS resources. Using this EventBridge type, you can build EventBridge rules to match tag changes and route the events to one or more targets. For example, a target might be an AWS Lambda function to invoke automated workflows. This topic provides a tutorial for using Lambda to build a cost-effective serverless solution to securely process tag changes on your AWS resources.

## Tag changes generate EventBridge events
<a name="generate-events"></a>

EventBridge delivers a near real-time stream of system events that describe changes in AWS resources. Many AWS resources support tags, which are custom, user-defined attributes to easily organize and categorize AWS resources. Common use cases for tags are cost allocation categorization, access-control security, and automation. 

With EventBridge, you can monitor for changes to tags and track the tag state on AWS resources. Previously, to achieve similar functionality, you might have continuously polled APIs and orchestrated multiple calls. Now, any change to a tag including individual service APIs, [Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html), and the [Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/index.html) will initiate the tag change on resource event. The following example shows a typical EventBridge event prompted by a tag change. It shows the new, updated, or deleted tag keys, and their associated values.

```
{
  "version": "0",
  "id": "bddcf1d6-0251-35a1-aab0-adc1fb47c11c",
  "detail-type": "Tag Change on Resource",
  "source": "aws.tag",
  "account": "123456789012",
  "time": "2018-09-18T20:41:38Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ec2:us-east-1:123456789012:instance/i-0000000aaaaaaaaaa"
  ],
  "detail": {
    "changed-tag-keys": [
      "a-new-key",
      "an-updated-key",
      "a-deleted-key"
    ],
    "tags": {
      "a-new-key": "tag-value-on-new-key-just-added",
      "an-updated-key": "tag-value-was-just-changed",
      "an-unchanged-key": "tag-value-still-the-same"
    },
    "service": "ec2",
    "resource-type": "instance",
    "version": 3,
  }
}
```

All EventBridge events have the same top-level fields:
+ **version** – By default, this value is set to `0` (zero) in all events.
+ **id** – A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets and are processed.
+ **detail-type** – Identifies, in combination with the `source` field, the fields and values that appear in the detail field.
+ **source** – Identifies the service that was the source of the event. The source for tag changes is `aws.tag`.
+ **time** – The timestamp of the event.
+ **region** – Identifies the AWS Region where the event originated.
+ **resources** – This JSON array contains Amazon Resource Names (ARNs) that identify resources that are involved in the event. This is the resource where tags have changed.
+ **detail** – A JSON object, whose content is different depending on event type. For tag change on resource, the following detailed fields are included:
  + **changed-tag-keys** – The tag keys that changed by this event.
  + **service** – The service that the resource belongs to. In this example, the service is `ec2`, which is Amazon EC2.
  + **resource-type** – The type of resource of the service. In this example, it is an Amazon EC2 instance.
  + **version** – The version of the tag set. The version starts at 1 and increments when tags are changed. You can use the version to verify the order of tag change events.
  + **tags** – The tags attached to the resource after the change.

For more information, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

By using EventBridge, you can create rules that match specific event patterns based on the different fields. We demonstrate how to do this in the tutorial. Also, we show how an Amazon EC2 instance can be stopped automatically if a specified tag isn’t attached to the instance. We use the EventBridge fields to create a pattern to match the tag events for the instance that launches a Lambda function.

## Lambda and serverless
<a name="lambda-and-serverless"></a>

AWS Lambda follows the serverless paradigm to run code in the cloud. You run code only when it’s needed, without thinking about servers. You pay only for the exact compute time you use. Even though it’s called *serverless*, it doesn’t mean that there are no servers. Serverless in this context means that you don’t have to provision, configure, or manage the servers that are used to run your code. AWS does all of that for you, so you can focus on your code. For more information about Lambda, see the [AWS Lambda Product Overview](https://aws.amazon.com/lambda).

## Tutorial: Automatically stopping Amazon EC2 instances that are missing required tags
<a name="monitor-example"></a>

As your pool of AWS resources and AWS accounts that you manage grows, you can use tags to make it easier to categorize your resources. Tags are commonly used for critical use cases such as cost allocation and security. To effectively manage AWS resources, your resources need to be consistently tagged. Often, when a resource is provisioned, it gets all the appropriate tags. However, a later process can result in a tag change that results in drift from the corporate tag policy. By monitoring changes to your tags, you can spot tag drift and immediately respond. This gives you more confidence that the processes that depend on your resources being properly categorized will produce the desired results.

The following example demonstrates how to monitor for tag changes on Amazon EC2 instances to verify that a specified instance continues to have the required tags. If the instance's tags change and the instance no longer has the required tags, a Lambda function is invoked to shut down the instance automatically. Why would you want to do this? It ensures that all resources are tagged according to your corporate tag policy, for effective cost allocation, or to be able to trust security based on [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html).

**Important**  
We strongly recommend that you perform this tutorial in a non-production account where you can't inadvertently shut down important instances.  
The example code in this tutorial intentionally limits the impact of this scenario to only the instances on a list of instance IDs. You must update the list with instance IDs that you are willing to shut down for the test. This helps ensure that you can't accidentally shut down every instance in a Region in your AWS account.   
After testing, make sure that all of your instances are tagged according to your company's tagging strategy. Then, you can remove the code that limits the function to only the instance IDs on the list.

This example uses JavaScript and the 16.x version of Node.js. The example uses example AWS account ID 123456789012 and the AWS Region US East (N. Virginia) (`us-east-1`). Replace these with your own test account ID and Region. 

**Note**  
If your console uses a different Region for its default, ensure that you switch the Region you're using in this tutorial whenever you change consoles. A common cause of this tutorial failing is having the instance and function in two different Regions.

If you use a different Region than `us-east-1`, ensure that you change all references in the following code examples to your chosen Region.

**Topics**
+ [Step 1. Create the Lambda function](#monitor-example-step-1)
+ [Step 2. Set up the required IAM permissions](#monitor-example-step-2)
+ [Step 3. Do a preliminary test of your Lambda function](#monitor-example-step-3)
+ [Step 4. Create the EventBridge rule that launches the function](#monitor-example-step-4)
+ [Step 5. Test the complete solution](#monitor-example-step-6)
+ [Tutorial summary](#summary)

### Step 1. Create the Lambda function
<a name="monitor-example-step-1"></a>

**To create the Lambda function**

1. Open the [AWS Lambda management console](https://console.aws.amazon.com/lambda/home).

1. Choose **Create function** and then choose **Author from scratch**.

1. For **Function name**, type **AutoEC2Termination**.

1. For **Runtime**, choose **Node.js 16.x**.

1. Keep all other fields at their default values, and choose **Create function**.

1. On the **Code** tab of the `AutoEC2Termination` detail page, open the **index.js** file to view its code.
   + If a tab with **index.js** is open, you can choose the edit box in that tab to edit its code.
   + If a tab with **index.js** isn't open, secondary-click the **index.js** file under the **AutoEC2Terminator** folder in the navigation pane. Then choose **Open**.

1. In the **index.js** tab, paste the following code in the editor box, replacing anything that is already present.

    Replace the value `RegionToMonitor` with the Region that you want to run this function in.

   ```
   // Set the following line to specify which Region's instances you want to monitor
   // Only instances in this Region are succesfully stopped on a match
   
   const RegionToMonitor = "us-east-1"
   
   // Specify the instance ARNs to check.
   // This limits the function for safety to avoid the tutorial shutting down all instances in account
   // The first ARN is a "dummy" that matches the test event you create in Step 3.
   // Replace the second ARN with one that matches a real instance that you want to monitor and that you can 
   // safely stop
   
   const InstanceList = [
       "i-0000000aaaaaaaaaa",
       "i-05db4466d02744f07"
   ];
   
   // The tag key name and value that marks a "valid" instance. Instances in the previous list that
   // do NOT have the following tag key and value are stopped by this function
   
   const ValidKeyName = "valid-key";
   const ValidKeyValue = "valid-value";
   
   // Load and configure the AWS SDK
   const AWS = require('aws-sdk');
   // Set the AWS Region
   AWS.config.update({region: RegionToMonitor});
   // Create EC2 service object.
   const ec2 = new AWS.EC2({apiVersion: '2016-11-15'});
   
   exports.handler = (event, context, callback) => {
   
     // Retrieve the details of the reported event.
     var detail = event.detail;
     var tags = detail["tags"];
     var service = detail["service"];
     var resourceType = detail["resource-type"];
     var resource = event.resources[0];
     var resourceSplit = resource.split("/");
     var instanceId = resourceSplit[resourceSplit.length - 1];
   
     // If this event is not for an EC2 resource, then do nothing.
     if (!(service === "ec2")) {
       console.log("Event not for correct service -- no action (", service, ")" );
       return;
     }
   
     // If this event is not about an instance, then do nothing.
     if (!(resourceType === "instance")) {
       console.log("Event not for correct resource type -- no action (", resourceType, ")" );
       return;
     }
   
     // CAUTION - Removing the following 'if' statement causes the function to run against 
     //           every EC2 instance in the specified Region in the calling AWS account. 
     //           If you do this and an instance is not tagged with the approved tag key 
     //           and value, this function stops that instance.
   
     // If this event is not for the ARN of an instance in our include list, then do nothing.
     if (InstanceList.indexOf(instanceId)<0) {
       console.log("Event not for one of the monitored instances -- no action (", resource, ")");
       return;
     }
   
     console.log("Tags changed on monitored EC2 instance (",instanceId,")");
   
     // Check attached tags for expected tag key and value pair
     if ( tags.hasOwnProperty(ValidKeyName) && tags[ValidKeyName] == "valid-value"){
       // Required tags ARE present
       console.log("The instance has the required tag key and value -- no action");
       callback(null, "no action");
       return;
     }
     
     // Required tags NOT present
     console.log("This instance is missing the required tag key or value -- attempting to stop the instance");
   
     var params = {
       InstanceIds: [instanceId], 
       DryRun: true
     };
   
     // call EC2 to stop the selected instances
     ec2.stopInstances(params, function(err, data) {
       if (err && err.code === 'DryRunOperation') {
         // dryrun succeeded, so proceed with "real" stop operation
         params.DryRun = false;
         ec2.stopInstances(params, function(err, data) {
           if (err) {
             console.log("Failed to stop instance");
             callback(err, "fail");
           } else if (data) {
             console.log("Successfully stopped instance", data.StoppingInstances);
             callback(null, "Success");
           }
         });
       } else {
         console.log("Dryrun attempt failed");
         callback(err);
       }
     });
   };
   ```

1. Choose **Deploy** to save your changes and make the new version of the function active.

This Lambda function checks the tags of an Amazon EC2 instance, as reported by the tag change event in EventBridge. In this example, if the instance in the event is missing the required tag key `valid-key` or if that tag doesn't have the value `valid-value`, then the function tries to stop the instance. You can change this logical check or the tag requirements for your own specific use cases.

Keep the Lambda console window open in your browser.

### Step 2. Set up the required IAM permissions
<a name="monitor-example-step-2"></a>

Before the function can successfully run, you must grant the function the permission to stop an EC2 instance. The AWS provided role [lambda\_basic\_execution](https://console.aws.amazon.com/iamv2/home#/roles/details/lambda_basic_execution) doesn't have that permission. In this tutorial, you modify the default IAM permission policy that is attached to the function's execution role named `AutoEC2Termination-role-{{uniqueid}}`. The minimum additional permission required for this tutorial is `ec2:StopInstances`. 

For more information about creating Amazon EC2 specific IAM policies, see [Amazon EC2: Allows starting or stopping an EC2 Instance and modifying a security group, programmatically and in the console](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_instance-securitygroup.html) in the *IAM User Guide*.

**To create an IAM permission policy and attach it to the Lambda function's execution role**

1. In a different browser tab or window, open the [Roles](https://console.aws.amazon.com/iamv2/home#/roles) page of the IAM console.

1. Start typing the role name **AutoEC2Termination**, and when it appears in the list, choose the role name. 

1. On the role's **Summary** page, choose the **Permissions** tab and choose the name of the one policy that is already attached.

1. On the policy's **Summary** page, choose **Edit policy**.

1. On the **Visual Editor** tab, choose **Add additional permissions**.

1. For **Service**, choose **EC2**.

1. For **Actions**, choose **StopInstances**. You can type **Stop** in the search bar, and then choose `StopInstances` when it appears.

1. For **Resources**, choose **All resources**, choose **Review policy**, and then choose **Save changes**. 

   This automatically creates a new version of the policy and sets that version as the default.

   Your final policy should look similar to the following example.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "VisualEditor0",
               "Effect": "Allow",
               "Action": "ec2:StopInstances",
               "Resource": "*"
           },
           {
               "Sid": "VisualEditor1",
               "Effect": "Allow",
               "Action": "logs:CreateLogGroup",
               "Resource": "arn:aws:logs:us-east-1:123456789012:*"
           },
           {
               "Sid": "VisualEditor2",
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/AutoEC2Termination:*"
           }
       ]
   }
   ```

------

### Step 3. Do a preliminary test of your Lambda function
<a name="monitor-example-step-3"></a>

In this step, you submit a test event to your function. The Lambda test functionality works by submitting a manually provided test event. The function processes the test event just as if the event had come from EventBridge. You can define multiple test events with different values to exercise all of the different parts of your code. In this step, you submit a test event that indicates that an Amazon EC2 instance's tags changed, and the new tags don't include the required tag key and value.

**To test your Lambda function**

1. Return to the window or tab with the Lambda console and open the **Test** tab for your **AutoEC2Termination** function.

1. Choose **Create new event**.

1. For **Event name**, enter **SampleBadTagChangeEvent**.

1. In the **Event JSON**, replace the text with the sample event shown in the following example text. You don't need to modify the accounts, Region, or instance ID for this test event to work correctly.

   ```
   {
     "version": "0",
     "id": "bddcf1d6-0251-35a1-aab0-adc1fb47c11c",
     "detail-type": "Tag Change on Resource",
     "source": "aws.tag",
     "account": "123456789012",
     "time": "2018-09-18T20:41:38Z",
     "region": "us-east-1",
     "resources": [
       "arn:aws:ec2:us-east-1:123456789012:instance/i-0000000aaaaaaaaaa"
     ],
     "detail": {
       "changed-tag-keys": [
         "valid-key"
       ],
       "tags": {
         "valid-key": "NOT-valid-value"
       },
       "service": "ec2",
       "resource-type": "instance",
       "version": 3
     }
   }
   ```

1. Choose **Save**, and then choose **Test**.

   The test appears to fail, but that's OK. 

   You should see the following error in the **Execution results** tab under **Response**.

   ```
   {
     "errorType": "InvalidInstanceID.NotFound",
     "errorMessage": "The instance ID 'i-0000000aaaaaaaaaa' does not exist",
     ...
   }
   ```

   The error occurs because the instance specified in the test event doesn't exist. 

   The information on the **Execution results** tab, in the **Function Logs** section , demonstrates that your Lambda function successfully attempted to stop an EC2 instance. However, it failed because the code initially attempts a [`DryRun`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html#API_StartInstances_RequestParameters) operation to stop the instance, which indicated that the instance ID was not valid. 

   ```
   START RequestId: 390c1f8d-0d9b-4b44-b087-8de64479ab44 Version: $LATEST
   2022-11-30T20:17:30.427Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    Tags changed on monitored EC2 instance ( i-0000000aaaaaaaaaa )
   2022-11-30T20:17:30.427Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    This instance is missing the required tag key or value -- attempting to stop the instance
   2022-11-30T20:17:31.206Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    INFO    Dryrun attempt failed
   2022-11-30T20:17:31.207Z    390c1f8d-0d9b-4b44-b087-8de64479ab44    ERROR   Invoke Error     {"errorType":"InvalidInstanceID.NotFound","errorMessage":"The instance ID 'i-0000000aaaaaaaaaa' does not exist","code":"InvalidInstanceID.NotFound","message":"The instance ID 'i-0000000aaaaaaaaaa' does not exist","time":"2022-11-30T20:17:31.205Z","requestId":"a5192c3b-142d-4cec-bdbc-685a9b7c7abf","statusCode":400,"retryable":false,"retryDelay":36.87870631147607,"stack":["InvalidInstanceID.NotFound: The instance ID 'i-0000000aaaaaaaaaa' does not exist","    at Request.extractError (/var/runtime/node_modules/aws-sdk/lib/services/ec2.js:50:35)","    at Request.callListeners (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:106:20)","    at Request.emit (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:78:10)","    at Request.emit (/var/runtime/node_modules/aws-sdk/lib/request.js:686:14)","    at Request.transition (/var/runtime/node_modules/aws-sdk/lib/request.js:22:10)","    at AcceptorStateMachine.runTo (/var/runtime/node_modules/aws-sdk/lib/state_machine.js:14:12)","    at /var/runtime/node_modules/aws-sdk/lib/state_machine.js:26:10","    at Request.<anonymous> (/var/runtime/node_modules/aws-sdk/lib/request.js:38:9)","    at Request.<anonymous> (/var/runtime/node_modules/aws-sdk/lib/request.js:688:12)","    at Request.callListeners (/var/runtime/node_modules/aws-sdk/lib/sequential_executor.js:116:18)"]}
   END RequestId: 390c1f8d-0d9b-4b44-b087-8de64479ab44
   ```

1. To prove that the code doesn't try to stop the instance when the correct tag is used, you can create and submit another test event. 

   Choose the **Test** tab above **Code source**. The console displays your existing **SampleBadTagChangeEvent** test event.

1. Choose **Create new event**.

1. For **Event name**, type **SampleGoodTagChangeEvent**.

1. In line 17, delete **NOT-** to change the value to **valid-value**.

1. At the top of the **Test event** window, choose **Save**, and then choose **Test**.

   The output displays the following, which demonstrates that the function recognizes the valid tag and doesn't attempt to shut down the instance.

   ```
   START RequestId: 53631a49-2b54-42fe-bf61-85b9e91e86c4 Version: $LATEST
   2022-12-01T23:24:12.244Z    53631a49-2b54-42fe-bf61-85b9e91e86c4    INFO    Tags changed on monitored EC2 instance ( i-0000000aaaaaaaaaa )
   2022-12-01T23:24:12.244Z    53631a49-2b54-42fe-bf61-85b9e91e86c4    INFO    The instance has the required tag key and value -- no action
   END RequestId: 53631a49-2b54-42fe-bf61-85b9e91e86c4
   ```

   Keep the Lambda console open in your browser.

### Step 4. Create the EventBridge rule that launches the function
<a name="monitor-example-step-4"></a>

Now you can create an EventBridge rule that matches the event and points to your Lambda function.

**To create the EventBridge rule**

1. In a different browser tab or window, open the [EventBridge console](https://console.aws.amazon.com/events/home#/rules/create) to the **Create Rule** page.

1. For **Name**, enter **ec2-instance-rule**, and then choose **Next**.

1. Scroll down to **Creation method** and choose **Custom pattern (JSON editor)**.

1. In the editing box, paste the following pattern text, and then choose **Next**.

   ```
   {
     "source": [
       "aws.tag"
     ],
     "detail-type": [
       "Tag Change on Resource"
     ],
     "detail": {
       "service": [
         "ec2"
       ],
       "resource-type": [
         "instance"
       ]
     }
   }
   ```

   This rule matches `Tag Change on Resource` events for Amazon EC2 instances and invokes whatever you specify as the **Target** in the next step. 

1. Next, add your Lambda function as the target. In the **Target 1** box, under **Select a target**, choose **Lambda function**.

1. Under **Function**, choose the **AutoEC2Termination** function that you created previously, and then choose **Next**.

1. On the **Configure tags** page, choose **Next**. Then on the** Review and create** page, choose **Create rule**. This also automatically grants permission for EventBridge to invoke the specified Lambda function.

### Step 5. Test the complete solution
<a name="monitor-example-step-6"></a>

You can test your final result by creating an EC2 instance and watching what happens when you change its tags.

**To test the monitoring solution with a real instance**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/v2/home#Instances:) to the **Instances** page.

1. Create an Amazon EC2 instance. Before you launch it, attach a tag with the key `valid-key` and the value `valid-value`. For information about how to create and launch an instance,see [Step 1: Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) in the *Amazon EC2 User Guide*. In the procedure *To launch an instance*, in step 3, where you enter the **Name** tag, also choose **Add additional tags**, choose **Add tag**, and then enter the **Key** of **valid-key** and **Value** of **valid-value**. You can **Proceed without a key pair** if this instance is solely for the purposes of this tutorial and you plan on deleting this instance after you complete it. Return to this tutorial when you reach the end of **Step 1**; you don't need to do **Step 2: Connect to your instance**.

1. Copy the **InstanceId** from the console.

1. Switch from the Amazon EC2 console to the Lambda console. Choose your **AutoEC2Termination** function, choose the **Code** tab, and then choose the **index.js** tab to edit your code.

1. Change the second entry in the `InstanceList` by pasting the value you copied from the Amazon EC2 console. Ensure that the `RegionToMonitor` value matches the Region that contains the instance you pasted.

1. Choose **Deploy** to make your changes active. The function is now ready to be activated by tag changes to that instance in the specified Region.

1. Switch from the Lambda console to the Amazon EC2 console.

1. Change the **Tags** attached to the instance by either deleting the **valid-key** tag or by changing that key's value. 
**Note**  
For information about how to change the tags on a running Amazon EC2 instance, see [Add and delete tags on an individual resource](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#adding-or-deleting-tags) in the *Amazon EC2 User Guide*.

1. Wait a few seconds, and then refresh the console. The instance should change its **Instance state** to **Stopping** and then to **Stopped**.

1. Switch from the Amazon EC2 console to the Lambda console with your function, and choose the **Monitor** tab. 

1. Choose the **Logs** tab, and in the **Recent invocations** table, choose the most recent entry in the **LogStream** column.

   The Amazon CloudWatch console opens to the **Log events** page for the last invocation of your Lambda function. The last entry should look similar to the following example.

   ```
   2022-11-30T12:03:57.544-08:00    START RequestId: b5befd18-2c41-43c8-a320-3a4b2317cdac Version: $LATEST
   2022-11-30T12:03:57.548-08:00    2022-11-30T20:03:57.548Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO Tags changed on monitored EC2 instance ( arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0 )
   2022-11-30T12:03:57.548-08:00    2022-11-30T20:03:57.548Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO This instance is missing the required tag key or value -- attempting to stop the instance
   2022-11-30T12:03:58.488-08:00    2022-11-30T20:03:58.488Z b5befd18-2c41-43c8-a320-3a4b2317cdac INFO Successfully stopped instance [ { CurrentState: { Code: 64, Name: 'stopping' }, InstanceId: 'i-1234567890abcdef0', PreviousState: { Code: 16, Name: 'running' } } ]
   2022-11-30T12:03:58.546-08:00    END RequestId: b5befd18-2c41-43c8-a320-3a4b2317cdac
   ```

### Tutorial summary
<a name="summary"></a>

This tutorial demonstrated how to create an EventBridge rule to match against a tag change on a resource event for Amazon EC2 instances. The rule pointed to a Lambda function that automatically shuts down the instance if it doesn't have the required tag.

The Amazon EventBridge support for tag changes on AWS resources opens possibilities to build event-driven automation across many AWS services. Combining this capability with AWS Lambda provides you with tools to build serverless solutions that access AWS resources securely, scale on demand, and are cost effective.

Other possible use cases for the tag-change-on-resource EventBridge event include:
+ **Launch a warning if someone accesses your resource from an unusual IP address** – Use a tag to store the source IP address of each visitor that accesses your resource. Changes to the tag generates a CloudWatch event. You can use that event to compare the source IP address to a list of valid IP addresses and activate a warning email if the source IP address isn't valid.
+ **Monitor if there are changes to your tag-based access control for a resource** – If you have set up access to a resource using [attribute (tag) based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html), you can use EventBridge events generated by any changes to the tag to prompt an audit by your security team.

# Troubleshooting tag changes
<a name="troubleshooting-tags"></a>

The following checklist might be helpful if errors occur when you try to apply or change tags on selected resources in [**Find resources to tag**](#find-resources-to-tag) query results.
+ The resource might already have the maximum number of tags. Generally, resources can have a maximum of 50 user-defined tags. AWS generated tags don't count toward the 50-tag maximum. Other users might also be adding tags to the same resource at the same time, which could raise the resource's tags to the maximum.
+ Some services allow a different character set (or restrict the character set that is allowed) for creating tags. If you added or changed tags using special characters, review the tag requirements in the resource's service documentation to verify that those characters are allowed by the service.
+ You might not have permissions to modify the tags for the resource. If you don't have permissions to view existing tags on a resource, you can't make changes to the resource's tags.
+ You might not have permissions to change the resource. Changes to the resource's metadata might be restricted by another administrator.
+ The resource might have been edited or deleted by another user or process. For example, assume that a resource was launched as part of the creation of an CloudFormation stack. If the stack was deleted or is no longer in an active state, the resource might no longer be available.
+ Tag changes might not be possible if a resource is offline or terminated, or if other updates (such as software upgrades) to the resource are in progress.
+ Tag changes can fail if you close the browser tab or change the page before the tag changes complete. Let tag changes finish, and wait for the success or failure banner to appear on the page, before you leave the page.
+ While there's a rate limit for the AWS Resource Groups Tagging API, the service you're tagging might impose a separate limit which you might hit before the Resource Groups Tagging API limit.

## Retry failed tag changes
<a name="tagging-resources-retry"></a>

If tag changes fail on at least one of your selected resources, Tag Editor displays a red banner at the bottom of the page. The banner shows an error message for each type of failure that occurs. For each error, the banner identifies the specific resources on which Tag Editor couldn't make tag changes. After you review and [troubleshoot the errors](#troubleshooting-tags), choose **Retry failed tag changes on resources** to retry changes on only those resources on which tag changes failed.

# Security in Tag Editor
<a name="security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). For more information about the compliance programs that apply to Tag Editor, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility model when using Tag Editor. The following topics show you how to configure Tag Editor to meet your security and compliance objectives.

**Topics**
+ [Data protection in Tag Editor](#data-protection)
+ [Identity and access management for Tag Editor](#security-iam)
+ [Logging and monitoring in Tag Editor](#logging-monitoring)
+ [Compliance validation for Tag Editor](#compliance-validation)
+ [Resilience in Tag Editor](#disaster-recovery-resiliency)
+ [Infrastructure security in Tag Editor](#infrastructure-security)

## Data protection in Tag Editor
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Tag Editor. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Tag Editor or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

### Data encryption
<a name="data-encryption"></a>

Tagging information is not encrypted. Although not encrypted, tags can contain information used as part of your security strategy, so it's important to control who can access tags on resources. It's especially critical that you control who can modify tags because such access could be used to elevate one's permissions.

#### Encryption at rest
<a name="encryption-rest"></a>

There are no additional ways of isolating service or network traffic that are specific to Tag Editor. If applicable, use AWS specific isolation. You can use the Tag Editor API and console in a virtual private cloud (VPC) to help maximize privacy and infrastructure security.

#### Encryption in transit
<a name="encryption-transit"></a>

Tag Editor data is encrypted in transit to the service's internal database for backup. This is not user-configurable.

#### Key management
<a name="key-management"></a>

Tag Editor is not currently integrated with AWS Key Management Service and does not support AWS KMS keys.

### Internetwork traffic privacy
<a name="protection-privacy"></a>

Tag Editor uses HTTPS for all transmissions between Tag Editor users and AWS. Tag Editor uses transport layer security (TLS) 1.3, but also supports TLS 1.2.

## Identity and access management for Tag Editor
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Tag Editor resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Audience](#security_iam_audience_taged)
+ [Authenticating with identities](#security_iam_authentication_taged)
+ [Managing access using policies](#security_iam_access-manage-taged)
+ [How Tag Editor works with IAM](#security_iam_service-with-iam)
+ [Tag Editor identity-based policy examples](#security_iam_id-based-policy-examples)
+ [Troubleshooting Tag Editor identity and access](#security_iam_troubleshoot)

### Audience
<a name="security_iam_audience_taged"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting Tag Editor identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [How Tag Editor works with IAM](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [Tag Editor identity-based policy examples](#security_iam_id-based-policy-examples))

### Authenticating with identities
<a name="security_iam_authentication_taged"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

#### AWS account root user
<a name="security_iam_authentication-rootuser-taged"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

#### Users and Groups
<a name="security_iam_authentication-iamuser-taged"></a>

An *[IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)* is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*.

An [*IAM group*](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html) in the *IAM User Guide*.

#### Roles
<a name="security_iam_authentication-iamrole-taged"></a>

An *[IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)* is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

### Managing access using policies
<a name="security_iam_access-manage-taged"></a>

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the *IAM User Guide*.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

#### Identity-based policies
<a name="security_iam_access-manage-id-based-policies-taged"></a>

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

Identity-based policies can be *inline policies* (embedded directly into a single identity) or *managed policies* (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html) in the *IAM User Guide*.

#### Resource-based policies
<a name="security_iam_access-manage-resource-based-policies-taged"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

#### Access control lists (ACLs)
<a name="security_iam_access-manage-acl-taged"></a>

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC are examples of services that support ACLs. To learn more about ACLs, see [Access control list (ACL) overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) in the *Amazon Simple Storage Service Developer Guide*.

#### Other policy types
<a name="security_iam_access-manage-other-policies-taged"></a>

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:
+ **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
+ **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the *AWS Organizations User Guide*.
+ **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide*.

#### Multiple policy types
<a name="security_iam_access-manage-multiple-policies-taged"></a>

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

### How Tag Editor works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Tag Editor, you should understand what IAM features are available to use with Tag Editor. To get a high-level view of how Tag Editor and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Tag Editor identity-based policies](#security_iam_service-with-iam-id-based-policies-arg-te)
+ [Resource-based policies](#security_iam_resource-based-policies)
+ [Authorization based on tags](#security_iam_tags)
+ [Tag Editor IAM roles](#security_iam_roles)

#### Tag Editor identity-based policies
<a name="security_iam_service-with-iam-id-based-policies-arg-te"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources in addition to the conditions under which actions are allowed or denied. Tag Editor supports specific actions, resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

##### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions-arg-te"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Tag Editor use the following prefix before the action: `tag:`. Tag Editor actions are performed entirely in the console, but have the prefix `tag` in log entries.

For example, to grant someone permission to tag a resource with the `tag:TagResources` API operation, you include the `tag:TagResources` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Tag Editor defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple tagging actions in a single statement, separate them with commas as follows.

```
"Action": [
      "tag:action1",
      "tag:action2",
      "tag:action3"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Get`, include the following action.

```
"Action": "tag:Get*"
```

To see a list of Tag Editor actions, see [Actions, resources, and condition keys for Tag Editor](https://docs.aws.amazon.com/service-authorization/latest/reference/list_tageditor.html) in the *Service Authorization Reference*.

##### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources-arg-te"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Tag Editor does not have any resources of its own. Instead, it manipulates the metadata (tags) that are attached to resources created by other AWS services.

##### Condition keys
<a name="security_iam_id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Tag Editor does not define any service-specific condition keys.

##### Examples
<a name="security_iam-id-based-policies-examples"></a>

To view examples of Tag Editor identity-based policies, see [Tag Editor identity-based policy examples](#security_iam_id-based-policy-examples).

#### Resource-based policies
<a name="security_iam_resource-based-policies"></a>

Tag Editor does not support resource-based policies because it doesn't define any of its own resources.

#### Authorization based on tags
<a name="security_iam_tags"></a>

Authorization based on tags is part of the security strategy called attribute-based access control (ABAC).

To control access to a resource based on its tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. You can apply tags to a resource when you are creating or updating the resource.

To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [Viewing groups based on tags](#security_iam_policy-examples-view-tags). For more information about attribute-based access control (ABAC), see [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*.

#### Tag Editor IAM roles
<a name="security_iam_roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions. Tag Editor does not have or use service roles.

##### Using temporary credentials with Tag Editor
<a name="security_iam_roles-tempcreds"></a>

In Tag Editor, you can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

##### Service-linked roles
<a name="security_iam_roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf.

Tag Editor does not have or use service-linked roles.

##### Service roles
<a name="security_iam_roles-service"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf.

Tag Editor does not have or use service roles.

### Tag Editor identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM principals, such as roles and users, don't have permission to create or modify tags. They also can't perform tasks using the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS APIs. An IAM administrator must create IAM policies that grant principals permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the principals that require those permissions.

For instructions on creating an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_policy-best-practices)
+ [Using the Tag Editor console and Resource Groups Tagging API](#security_iam_policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_policy-examples-own-permissions)
+ [Viewing groups based on tags](#security_iam_policy-examples-view-tags)

#### Policy best practices
<a name="security_iam_policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Tag Editor resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

#### Using the Tag Editor console and Resource Groups Tagging API
<a name="security_iam_policy-examples-console"></a>

To access the Tag Editor console and the Resource Groups Tagging API, you must have a minimum set of permissions. These permissions must allow you to list and view details about the tags attached to resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console and API commands won't function as intended for the IAM principals with that policy.

To ensure that those principals can still use Tag Editor, attach the following policy (or a policy that contains the permissions listed in the following policy) to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*:

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
        "tag:GetResources",
        "tag:TagResources",
        "tag:UntagResources",
        "tag:getTagKeys",
        "tag:getTagValues",
        "resource-explorer:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

------

For more information about granting access to Tag Editor and Resource Groups Tagging API, see [Granting permissions for using Tag Editor](#gettingstarted-prereqs-permissions-howto).

#### Allow users to view their own permissions
<a name="security_iam_policy-examples-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

#### Viewing groups based on tags
<a name="security_iam_policy-examples-view-tags"></a>

You can use conditions in your identity-based policy to control access to Tag Editor resources based on tags. This example shows how you might create a policy that allows viewing a resource, in this example, a resource group. However, permission is granted only if the group tag `project` has the same value as the `project` tag attached to the calling principal.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "resource-groups:ListGroups",
            "Resource": "arn:aws:resource-groups:{{us-east-1}}:{{111122223333}}:group/{{group_name}}"
        },
        {
            "Effect": "Allow",
            "Action": "resource-groups:ListGroups",
            "Resource": "arn:aws:resource-groups:{{us-east-1}}:{{111122223333}}:group/{{group_name}}",
            "Condition": {
                "StringEquals": {"aws:ResourceTag/project": "${aws:PrincipalTag/project}"}
            }
        }
    ]
}
```

------

You can attach this policy to the users in your account. If a user with the tag key `project` and tag value `alpha` attempts to view a resource group, the group must also be tagged `project=alpha`. Otherwise the user is denied access. The condition tag key `project` matches both `Project` and `project` because condition key names are not case-sensitive. For more information, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

### Troubleshooting Tag Editor identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Tag Editor and IAM.

**Topics**
+ [I am not authorized to perform an action in Tag Editor](#security_iam_troubleshoot-permissions-taged)
+ [I am not authorized to perform iam:PassRole](#security_troubleshoot-passrole)

#### I am not authorized to perform an action in Tag Editor
<a name="security_iam_troubleshoot-permissions-taged"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your sign-in credentials.

The following example error occurs when the user `mateojackson` tries to use the console to view tags on a resource but does not have `tag:GetTagKeys` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: tag:GetTagKeys on resource: arn:aws:resource-groups::us-west-2:123456789012:{{resource-type}}/my-test-resource
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `my-test-resource` resource using the `tag:GetTagKeys` action.

#### I am not authorized to perform iam:PassRole
<a name="security_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to Tag Editor.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in Tag Editor. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## Logging and monitoring in Tag Editor
<a name="logging-monitoring"></a>

All Tag Editor actions are logged in AWS CloudTrail.

### Logging Tag Editor API calls with CloudTrail
<a name="logging-using-cloudtrail"></a>

Tag Editor is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Tag Editor. CloudTrail captures all API calls for Tag Editor as events, including calls from the Tag Editor console and from code calls to the Resource Groups Tagging API. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Tag Editor. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Tag Editor, the IP address from which the request was made, who made the request, when it was made, and additional details. 

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

#### Tag Editor information in CloudTrail
<a name="resource-groups-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Tag Editor, or in the Tag Editor console, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Tag Editor, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following resources: 
+ [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Tag Editor actions are logged by CloudTrail and are documented in the [Tag Editor API Reference](https://docs.aws.amazon.com/ARG/latest/APIReference/). Tag Editor actions in the console are logged by CloudTrail, and are shown as events with `tagging.amazonaws.com` as the `eventSource`.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail `userIdentity` element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

#### Understanding Tag Editor log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the action `TagResources`.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEEXAMPLE:botocore-session-1661372702",
        "arn": "arn:aws:sts::123456789012:assumed-role/cli-role/botocore-session-1661372702",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEEXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/cli-role",
                "accountId": "123456789012",
                "userName": "cli-role"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-08-24T20:25:03Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2022-08-24T20:27:14Z",
    "eventSource": "tagging.amazonaws.com",
    "eventName": "TagResources",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "72.21.198.65",
    "userAgent": "aws-cli/2.7.14 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/resourcegroupstaggingapi.tag-resources",
    "requestParameters": {
        "resourceARNList": [
            "arn:aws:events:us-east-1:123456789012:rule/SecretsManagerMonitorRule"
        ],
        "tags": {
            "owner": "alice"
        }
    },
    "responseElements": {
        "failedResourcesMap": {}
    },
    "requestID": "8f9ea891-4125-460c-802f-26c11EXAMPLE",
    "eventID": "b2c9322a-aad7-424b-8f0b-423daEXAMPLE",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "tagging.us-east-1.amazonaws.com"
    }
}
```

## Compliance validation for Tag Editor
<a name="compliance-validation"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Resilience in Tag Editor
<a name="disaster-recovery-resiliency"></a>

Tag Editor performs automated backups to internal service resources. These backups are not user-configurable. Backups are encrypted, both at rest and in transit. Tag Editor stores customer data in Amazon DynamoDB.

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

If you delete tags accidentally, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## Infrastructure security in Tag Editor
<a name="infrastructure-security"></a>

Tag Editor doesn't provide additional ways of isolating service or network traffic. If applicable, use AWS specific isolation. You can use the Tag Editor API and console in a virtual private cloud (VPC) to help maximize privacy and infrastructure security.

You use AWS published API calls to access Tag Editor through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TSL 1.2 and recommend TSL 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an AWS Identity and Access Management (IAM) principal. Or, you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/) (AWS STS) to generate temporary security credentials to sign requests.

Tag Editor does not support resource-based policies.

You can call Tag Editor API operations from any network location, but Tag Editor does support resource-based access policies, which can include restrictions based on the source IP address. You can also use Tag Editor policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this approach isolates network access to a given resource from only the specific VPC within the AWS network.

# Service quotas
<a name="reference"></a>

The following table provides information about the service quotas for Tag Editor. 

These quotas are currently not adjustable using the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/resource-groups/quotas). Contact [Support](https://console.aws.amazon.com/support/home#/).


| Name | Default | 
| --- | --- | 
| Tags attached per resource | 50 user-defined tags (AWS generated tags don't count against this limit.) | 
| Tag key name | Minimum of 1, maximum 128 Unicode characters in UTF-8.<br />Allowed characters include letters, numbers, spaces, and the following characters:<br />`_ . : / = + - @`<br />Key names can't begin with `aws:` because that prefix is reserved for AWS use. Some AWS services have some additional character or length restrictions. For details, see the documentation for the specific service.  | 
| Tag values | Minimum of 0, maximum of 256 Unicode characters in UTF-8.<br />Allowed characters include letters, numbers, spaces, and the following characters:<br />`_ . : / = + - @` Some AWS services have some additional character or length restrictions. For details, see the documentation for the specific service.  | 
| Rate of calling the [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) API operation | Maximum of 15 calls per second | 
| Rate of calling the following API operations:+  [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) <br />+  [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html) <br />+  [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html) <br />+  [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html)  | Maximum of 5 calls per second | 

# Tag Editor document history
<a name="doc-history"></a>

| Change | Description | Date | 
| --- |--- |--- |
| [Updated permissions for evaluating organization-wide compliance](#doc-history) | Updated the [ Permissions for evaluating organization-wide compliance](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-permissions-org) to include permissions that assist with accessing the compliance report.  | August 28, 2024 | 
| [Updated content](#doc-history) | Updated topic titles and reorganized content to improve readability and discoverability.  | July 25, 2024 | 
| [Tagging content from AWS General Reference moved to this guide](#doc-history) | The topics about tagging your AWS resources was moved from the AWS General Reference to this guide. | March 24, 2023 | 
| [IAM best practices update](#doc-history) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | January 3, 2023 | 
| [Moving Tag Editor documentation to its own guide](https://docs.aws.amazon.com/tag-editor/latest/userguide) | Tag Editor documentation is now provided in its own user guide instead of being part of the AWS Resource Groups User Guide. | December 13, 2022 | 
| [Check for compliance with tag policies](#doc-history) | After you create and attach tag policies to accounts using AWS Organizations, you can find noncompliant tags on resources in your organization's accounts.  | November 26, 2019 | 
| [Tag Editor now supports finding untagged resources](#doc-history) | You can now search for resources in Tag Editor that do not have tag values applied for a specific tag key. | June 18, 2019 | 
| [Tag Editor console moves out of AWS Systems Manager console](#doc-history) | The Tag Editor console is now independent from the Systems Manager console. Although you can still find pointers to the Tag Editor console in the Systems Manager left navigation bar, you can open the Tag Editor console directly from the drop-down menu at the upper left of the AWS Management Console. | June 5, 2019 | 
| [Older, legacy Tag Editor tools are no longer available](#doc-history) | Mentions of older, classic, or legacy Tag Editor have been removed; these tools are no longer available in AWS. Use Tag Editor instead. | May 14, 2019 | 
| [Tag Editor now supports tagging resources across multiple regions](#doc-history) | Tag Editor now lets you search for and manage tags of resources across multiple regions, with your current region added to resource queries by default. | May 2, 2019 | 
| [Tag Editor now supports exporting query results to a CSV](#doc-history) | You can export the results of a query on the **Find Resources to tag** page to a CSV-formatted file. A new Region column is shown in Tag Editor query results. Tag Editor now lets you search for resources that have empty values for a specific tag key. Tag key values auto-complete as you type a unique value among existing keys. | April 2, 2019 | 
| [Tag Editor now supports adding all resource types to a query](#doc-history) | You can apply tags to up to 20 individual resource types in a single operation, or you can choose **All resource types** to query all resource types in a region. Autocompletion has been added to the **Tag key** field of a query to help enable consistent tag keys among resources. If tag changes fail on some resources, you can retry tag changes on just resources for which tag changes failed. | March 19, 2019 | 
| [Tag Editor now supports multiple resource types in a search](#doc-history) | You can apply tags to up to 20 resource types in a single operation. You can also choose the columns that are shown to you in search results, including columns for each unique tag key found in your search results or selected resources from results. | February 26, 2019 | 