# Best Practices for Tagging AWS Resources AWS Whitepaper

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
+ [Best Practices for Tagging AWS Resources](#tagging-best-practices)
+ [What are tags?](#what-are-tags)
+ [Building your tagging strategy](#building-your-tagging-strategy)
   + [Defining needs and use cases](#defining-needs-and-use-cases)
   + [Defining and publishing a tagging schema](#defining-and-publishing-a-tagging-schema)
   + [AWS Organizations – Tag policies](#aws-organizations-tag-policies)
   + [Implementing and enforcing tagging](#implementing-and-enforcing-tagging)
   + [Measuring tagging effectiveness and driving improvements](#measuring-tagging-effectiveness-and-driving-improvements)
+ [Tagging use cases](#tagging-use-cases)
   + [Tags for cost allocation and financial management](#tags-for-cost-allocation-and-financial-management)
      + [Cost allocation tags](#cost-allocation-tags)
      + [Building a cost allocation strategy](#building-a-cost-allocation-strategy)
   + [Tags for operations and support](#tags-for-operations-and-support)
      + [Automated infrastructure activities](#automated-infrastructure-activities)
      + [Workload lifecycle](#workload-lifecycle)
      + [Incident management](#incident-management)
      + [Patching](#patching)
      + [Operational observability](#operational-observability)
   + [Tags for data security, risk management, and access control](#tags-for-data-security-risk-management-and-access-control)
      + [Data security and risk management](#data-security-and-risk-management)
      + [Tags for identity management and access control](#tags-for-identity-management-and-access-control)
         + [ABAC for individual resources](#abac-for-individual-resources)
+ [Conclusion](#conclusion)
+ [Contributors](#contributors)
+ [Further reading](#further-reading)
+ [Document revisions](#document-revisions)
+ [Notices](#notices)
+ [AWS Glossary](#glossary)

-----



# Best Practices for Tagging AWS Resources
<a name="tagging-best-practices"></a>

Publication date: **March 30, 2023** ([Document revisions](#document-revisions))

 Amazon Web Services (AWS) allows you to assign metadata to many of your AWS resources in the form of tags. Each tag is a simple label consisting of a key and an optional value to store information about the resource or data retained on that resource. This whitepaper focuses on tagging use cases, strategies, techniques, and tools that can help you to categorize resources by purpose, team, environment, or other criteria relevant to your business. Implementing a consistent tagging strategy can make it easier to filter and search for resources, monitor cost and usage, and manage your AWS environment. 

 This paper builds on the practices and guidance provided in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper. It is recommended that you read that whitepaper before this one. AWS recommends that you establish your cloud foundation in a holistic way. For additional information, refer to [Establishing your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html). 

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar. 

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/). 

## Introduction
<a name="introduction"></a>

 AWS makes it easy to deploy your workloads in AWS by creating resources, such as [Amazon EC2 instances](https://aws.amazon.com/ec2), [Amazon EBS volumes](https://aws.amazon.com/ebs/), [security groups](https://docs.aws.amazon.com/AWSEC2/latest/DeveloperGuide/using-network-security.html), and [AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). You can also scale and grow the ﬂeet of AWS resources that hosts your applications, stores your data, and expands your AWS infrastructure over time. As your AWS usage grows to many resource types spanning multiple applications, you will need a mechanism to track which resources are assigned to which application. Use this mechanism to support your operational activities, such as cost monitoring, incident management, patching, backup, and access control. 

 In on-premises environments, this knowledge is often captured in knowledge management systems, document management systems, and on internal wiki pages. With a configuration management database (CMDB), you can store and manage the relevant detailed metadata using standard change control processes. This approach provides governance, but requires additional effort to develop and maintain. You can take a structured approach to the naming of resources, but a resource name can only hold a limited amount of information. 

![Picture showing the decomposition of the name of a resource into its parts.](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/images/structured-approach-to-resource-naming.png)


 For example, EC2 instances have a predefined tag called Name that provides similar functionality and allows you to name workloads as they are moved to AWS. 

 In 2010, AWS launched [*resource tags*](https://aws.amazon.com/blogs/aws/new-amazon-ec2-feature-resource-tagging/) to provide a ﬂexible and scalable mechanism for attaching metadata to your resources. This whitepaper guides you through the process of developing and implementing a robust tagging strategy across your AWS environment. This guidance will help you ensure tagging consistency and coverage that supports your decision-making and operational activities 

# What are tags?
<a name="what-are-tags"></a>

A tag is a [*key-value pair*](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) applied to a resource to hold metadata about that resource. Each tag is a label consisting of a key and an optional value. Not all services and resource types currently support tags (see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html)). Other services may support tags via their own APIs. It should be noted that tags are not encrypted and should not be used to store sensitive data, such as personally identifiable information (PII). 

Tags that a user creates and applies to AWS resources using the AWS CLI, API, or the AWS Management Console are known as *user-defined* tags. Several AWS services, such as AWS CloudFormation, Elastic Beanstalk, and Auto Scaling, automatically assign tags to resources that they create and manage. These keys are known as *AWS generated* tags and are typically prefixed with `aws`. This prefix cannot be used in user-defined tag keys. 

 There are usage requirements and limits on the number of user-defined tags that can be added to an AWS resource. For more information, refer to [*Tag naming limits and requirements*](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-conventions) in the *AWS General Reference guide*. AWS generated tags do not count against these user-defined tag limits. 

*Table 1 – Examples of user-defined tag keys and values *


|  Instance ID  |  Tag Key  |  Tag Value  | 
| --- | --- | --- | 
| i-01234567abcdef89a  | CostCenter  | 98765  | 
|   | Stack  | Test  | 
| i-12345678abcdef90b  | CostCenter  | 98765  | 
|   | Stack  | Production  | 

*Table 2 – Examples of AWS generated tags *


|  AWS Generated Tag Keys  |  Rationale  | 
| --- | --- | 
| aws:ec2spot:fleet-request-id | Identifies the Amazon EC2 Spot Instance request that launched the instance  | 
| aws:cloudformation:stack-name | Identifies the AWS CloudFormation stack that created the resource  | 
| lambda-console:blueprint | Identifies blueprint used as a template for an AWS Lambda function  | 
| elasticbeanstalk:environment-name  | Identifies the application that created the resource  | 
| aws:servicecatalog:provisionedProductArn | The provisioned product Amazon Resource Name (ARN)  | 
| aws:servicecatalog:productArn | The ARN of the product from which the provisioned product was launched  | 

 AWS generated tags form a namespace. For example, in a CloudFormation template, you define a set of resources to be deployed together in a `stack`, where `stack-name` is a descriptive name that you assign to identify it. If you examine a key such as `aws:cloudformation:stack-name`, you can see the namespace that is used to scope the parameter uses three elements: **aws** the *organization,* **cloudformation** the *service, and* **stack-name** the *parameter.* 

 User-defined tags can also use namespaces and using an organizational identifier as a prefix is recommended. This helps you quickly identify whether a tag is something from your managed schema, or something defined by a service or tool that you are using in your environment. 

 In the [Establishing Your Cloud Foundation on AWS](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html) whitepaper, we recommend a set of tags that should be implemented. It’s highly likely that different businesses will have different allowed patterns and different lists for a given tag. Looking at the example in Table 3: 

*Table 3 – Same tag key, different value validation rules *


|   Organization   |  Tag Key  |  Tag Values Validation  |  Tag Value Example  | 
| --- | --- | --- | --- | 
|  Company A  | CostCenter  | 5432, 5422, 5499  | 5432  | 
|  Company B  | CostCenter  | ABC\*  | ABC123  | 

 If these two schemas are in separate organizations, then there is no issue with tag conflicts. However, should these two environments merge, then the namespaces can conflict and validation becomes more complex. This scenario might seem unlikely, but businesses are acquired or merged, and there are other scenarios, such as clients working with a managed service provider, game publisher, or venture capital business, where accounts from different organizations are part of a shared AWS Organization. By using the business name as a prefix to define a unique namespace, these challenges can be avoided, as shown in Table 4: 

*Table 4 – Use of namespaces in tag keys *


|   Organization   |  Tag Key  |  Tag Values Validation  |  Tag Value Example  | 
| --- | --- | --- | --- | 
| Company A | company-a:CostCenter  | 5432, 5422, 5499  | 5432  | 
| Company B | company-b:CostCenter  | ABC\*  | ABC123  | 

 In large and complex organizations where businesses are acquired and divested regularly, this situation will occur more frequently. As the new acquisition’s processes and practices are harmonized across the wider group, the situation is resolved. Having distinct namespaces helps because the use of the older tags can be reported on and the relevant teams contacted to adopt the new schema. A namespace can also be used to indicate a scope or represent a use case or an area of responsibility that is aligned to organizational owners. 

*Table 5 – Example of scope or use case scope within tag keys *


|  Use Case  |  Tag Key  |  Rationale  |  Allowed Values  | 
| --- | --- | --- | --- | 
| Data Classification  | example-inc:info-sec:data-classification | Information security defined set of data classification  | sensitive, company-confidential, customer-identifiable  | 
| Operations  | example-inc:dev-ops:environment | Implement scheduling of test and development environments  | development, staging, quality-assurance, production  | 
| Disaster Recovery  | example-inc:disaster-recovery:rpo | Define the recovery point objective (RPO) for a resource  | 6h, 24h  | 
| Cost Allocation  | example-inc:cost-allocation:business-unit | Finance teams need cost reporting on each team's usage and spend  | corporate, recruitment, support, engineering  | 

 Tags are simple and ﬂexible. Both the key and the value of the tag are variable-length strings and can support a wide character set. For more information on lengths and character sets, see [Tagging AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *AWS General Reference*. Tags are case sensitive, meaning that `costCenter` and `costcenter` are different tag keys. In different countries, the spelling of a word might differ, which might affect your keys. For example, in the United States, one might define a key as `costcenter`, but in the United Kingdom, `costcentre` might be preferred. These are different keys from the resource-tagging perspective. Define spelling, case, and punctuation as part of your tagging strategy. Use these definitions as a reference for anyone creating or managing resources. This topic is discussed in more detail in the next section, [Building your tagging strategy](#building-your-tagging-strategy). 

**Note**  
Although tag keys are case sensitive, IAM has additional validations for IAM resources to prevent the application of tag keys that only differ in casing. We recommend not using keys that only differ in casing. Refer to [Tags for IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html#id_tags_rules) for more details.

# Building your tagging strategy
<a name="building-your-tagging-strategy"></a>

 As with many practices in operations, implementing a tagging strategy is *a process of iteration and improvement*. Start small with your immediate priority and grow the tagging schema as you need to. 

![Diagram showing a graphical representation of the tagging strategy iteration and improvement cycle](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/images/tagging-strategy-cycle.png)


 Throughout this process, ownership is key to accountability and progress. Because tags can be used for a variety of purposes, the overall tagging strategy can be split into areas of responsibility within an organization. Tagging allows a programmatic approach to activities that depend upon the characterization of resources. The range of stakeholders that can benefit from tagging will depend on the size of the organization and operational practices. Larger organizations can benefit from clearly defining the responsibilities of the teams involved in building and implementing a tagging strategy. Some stakeholders can be responsible for identifying the needs (defining use cases) for tagging; others can be responsible for maintaining, implementing, and improving the tagging strategy. 

 By assigning ownership, you are in a good position to implement individual aspects of the strategy. Where appropriate, this ownership can be formalized as policy and documented in a responsibility matrix (for example, RACI: Responsible, Accountable, Consulted, and Informed), or in a shared responsibility model. In smaller organizations, teams might play multiple roles in a tagging strategy, from requirements definition to implementation and enforcement. 

## Defining needs and use cases
<a name="defining-needs-and-use-cases"></a>

Start building your strategy by engaging with stakeholders who have a fundamental underlying need to consume metadata. These teams define the metadata that resources need to be tagged with to support their activities, such as reporting, automation, and data classification. They outline how the resources need to be organized and which policies they need to be mapped to. Examples of roles and functions that these stakeholders can have in organizations include: 
+ **Finance** and **Line of Business** need to understand the value of investment by mapping it to costs to prioritize actions that need to be taken when addressing ineﬃciency. Understanding *cost vs value generated* helps to identify unsuccessful lines of business or product offerings. This leads to informed decisions about continuing support, adopting an alternative (for example, using a SaaS offering or managed service), or retiring an unprofitable business offering. 
+ **Governance** and **Compliance** need to understand the categorization of data (for example, public, sensitive, or confidential), whether a specific workload is in or out of scope for audit against a specific standard or regulation, and the criticality of the service (whether the service or application is business-critical) to apply appropriate controls and oversight, such as permissions, policies, and monitoring. 
+ **Operations** and **Development** need to understand the workload lifecycle, implemented stages of their supported products, and management of release stages (for example, Development, Test, Production split) and their associated support prioritizations and stakeholder management requirements. Duties such as Backups, Patching, Observability and Deprecation also need to be defined and understood. 
+ **Information Security (InfoSec)** and **Security Operations (SecOps)** outline what controls must be applied and which are recommended. InfoSec normally defines the implementation of the controls, and SecOps is generally responsible for managing those controls. 

Depending on your use case, priorities, size of your organization, and operational practices, you might need representation from various teams within the organization, such as Finance (including Procurement), Information Security, Cloud Enablement, and Cloud Operations. You also need representation from application and process owners for functions such as patching, backup and restore, monitoring, job scheduling, and disaster recovery. These representatives help drive the definition, implementation, and measure the effectiveness of the tagging strategy. They should [*work backwards*](https://www.youtube.com/watch?v=aFdpBqmDpzM) from stakeholders and their use cases, and conduct a cross-functional workshop. In the workshop, they get a chance to share their perspectives and needs, and help drive an overall strategy. Examples of participants and their involvement in various use cases are described later in this whitepaper. 

The stakeholders also define and validate the keys for mandatory tags, and can recommend the scope for optional tags. For example, Finance Teams might need to relate a resource to an internal cost center, business unit, or both. Thus, they might require that certain tag keys, such as `CostCenter` and `BusinessUnit`, be made mandatory. Individual development teams might decide to use additional tags for automation purposes, such as `EnvironmentName`, `OptIn`, or `OptOut`. 

Key stakeholders need to agree on the tagging strategy approach, and document the answers for compliance- and governance-related questions, such as: 
+  What use cases need to be addressed? 
+  Who is responsible for tagging resources (implementation)? 
+  How are tags enforced and what methods and automation will be used (proactive or reactive)? 
+  How are tagging effectiveness and goals measured? 
+  How often should the tagging strategy be reviewed? 
+  Who drives improvements? How is this done? 

 Business functions, such as Cloud Enablement, Cloud Business Oﬃce, and Cloud Platform Engineering, can then play a role of facilitators for the process of building the tagging strategy, help drive its adoption, and ensure consistency of its application by measuring progress, removing roadblocks, and reducing duplicated effort. 

## Defining and publishing a tagging schema
<a name="defining-and-publishing-a-tagging-schema"></a>

 Employ a consistent approach in tagging your AWS resources, both for mandatory and optional tags. A comprehensive tagging schema helps you to achieve this consistency. The following examples can help get you started: 
+  Agree on the mandatory tag keys 
+  Define acceptable values and tag naming conventions (upper or lower case, dashes or underscores, hierarchy, and so on) 
+  Confirm values would not constitute personally identifiable information (PII) 
+  Decide who can define and create new tag keys 
+  Agree on how to add new mandatory tag values and how to manage optional tags 

 Review the following [tagging categories](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) table, which can be used as a baseline of what you might include in your tagging schema. You still need to determine the convention you will use for the tag key and what values are permitted for each. The tagging schema is the document in which you define this for your environment. 

 *Table 6 – Example of a definitive tagging schema* 


| Use Case  | Tag Key  | Rationale  | Allowed Values (Listed or value prefix/suﬃx)  | Used for Cost Allocation  | Resource Types  | Scope  | Required  | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
|  Cost Allocation  | example-inc:cost-allocation:ApplicationId  |  Track cost vs value generated by each line of business  | DataLakeX, RetailSiteX  | Y  | All  | All  | Mandatory  | 
|  Cost Allocation  | example-inc:cost-allocation:BusinessUnitId  |  Monitor costs by business unit  | Architecture, DevOps, Finance  | Y  | All  | All  | Mandatory  | 
|  Cost Allocation  | example-inc:cost-allocation:CostCenter  |  Monitor costs by cost center  | 123-\*  | Y  | All  | All  | Mandatory  | 
|  Cost Allocation  | example-inc:cost-allocation:Owner  |  Which budget holder is responsible for this workload  | Marketing, RetailSupport  | Y  | All  | All  | Mandatory  | 
|  Access Control  | example-inc:access-control:LayerId  |  Identify SubComponent / Layer to grant access to resources based on the role  | DB\_Layer, Web\_Layer, App\_Layer  |  N  | All  | All  | Optional  | 
|  Automation  | example-inc:automation:EnvironmentId  |  Implement scheduling of test and development environments, also referred to as software development lifecycle (SDLC) stage  | Prod, Dev, Test, Sandbox  |  N  | EC2, RDS, EBS  | All  | Mandatory  | 
|  DevOps  | example-inc:operations:Owner  |  Which team/squad is responsible for the creation and maintenance of the resource  | Squad01  |  N  | All  | All  | Mandatory  | 
|  Disaster Recovery  | example-inc:disaster-recovery:rpo  |  Define the recovery point objective (RPO) for a resource  | 6h, 24h  |  N  | S3, EBS  | Prod  | Mandatory  | 
|  Data Classification  | example-inc:data:classification  |  Classify data for compliance and governance  | Public, Private, Confidential, Restricted  |  N  | S3, EBS  | All  | Mandatory  | 
|  Compliance  | example-inc:compliance:framework  |  Identifies the compliance framework the workload is subject to  | PCI-DSS, HIPAA  |  N  | All  | Prod  | Mandatory  | 

 After the tagging schema is defined, manage the schema in a version-controlled repository that is made accessible to all the relevant stakeholders for easy reference and trackable updates. This approach improves eﬃciency and allows for agility. 

## AWS Organizations – Tag policies
<a name="aws-organizations-tag-policies"></a>

 Policies in AWS Organizations allow you to apply additional types of governance to AWS accounts in your organization. A [*tag policy*](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) is how you can express your tagging schema in JSON form so that the platform can report and optionally enforce the schema within your AWS environment. The tag policy defines the values that are acceptable for a tag key on specific resource types. This policy can be in the form of a list of values, or a prefix followed by a wildcard character (`*`). The simple prefix approach is less rigorous than a discrete list of values but requires less maintenance. 

 The following examples show how to define a tagging policy to validate the values that are acceptable for a given key. Working from the human-friendly tabular definition of the schema, you can transcribe this information into one or more tag policies. Separate policies can be used to support delegated ownership or some policies might only apply in specific scenarios. 

### ExampleInc-CostAllocation.json
<a name="exampleinc-costallocation.json"></a>

 The following is an example of a tag policy that reports on Cost Allocation tags: 

```
{
  "tags": {
    "example-inc:cost-allocation:ApplicationId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:ApplicationId"
      },
      "tag_value": {
        "@@assign": [
          "DataLakeX",
          "RetailSiteX"
        ]
      }
    },
    "example-inc:cost-allocation:BusinessUnitId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:BusinessUnitId"
      },
      "tag_value": {
        "@@assign": [
          "Architecture",
          "DevOps",
          "FinanceDataLakeX"
        ]
      }
    },
    "example-inc:cost-allocation:CostCenter": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:CostCenter"
      },
      "tag_value": {
        "@@assign": [
          "123-*"
        ]
      }
    }
  }
}
```

### ExampleInc-DisasterRecovery.json
<a name="exampleinc-disasterrecovery.json"></a>

 The following is an example of a tag policy that reports on Disaster Recovery tags: 

```
{
    "tags": {
        "example-inc:disaster-recovery:rpo": {
            "tag_key": {
                "@@assign": "example-inc:disaster-recovery:rpo"
            },
            "tag_value": {
                "@@assign": [
                    "6h",
                    "24h"
                ]
            }
        }        
    }
}
```

 In this example, the `ExampleInc-CostAllocation` tag policy is attached to the `Workloads` OU, and therefore applies to all the accounts in both the `Prod` and `Test` child OUs. Similarly, the `ExampleInc-DisasterRecovery` tag policy is attached to the `Prod` OU and therefore only applies to accounts below this OU. The [Organizing Your Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper explores the recommended OU structures in more detail. 

![Diagram showing the attachment of tag policies to an OU structure and the effective policy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/images/adding-tagging-to-policies-in-ou-structure.png)


 Looking at the `marketing-prod` account in the diagram, both tag policies apply to this account, so we have the concept of an *effective policy*, which is the convolution of the policies of a given type that apply to an account. If you primarily manage your resources manually, then you can review the effective policy by visiting the [Resource Groups & Tag Editor:Tag policies](http://console.aws.amazon.com/resource-groups/tag-policies) in the console. If you use infrastructure as code (IaC) or scripting to manage your resources, you can use the [`AWS::Organizations::DescribeEffectivePolicy`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) API call. 

## Implementing and enforcing tagging
<a name="implementing-and-enforcing-tagging"></a>

 In this section, we’ll introduce you to the tools available for the following resource management strategies: manual, infrastructure as code (IaC), and continuous integration/continuous delivery (CI/CD). The key dimension for these approaches is an increasingly frequent rate of deployment. 

### Manually managed resources
<a name="manually-managed-resources"></a>

 These are typically workloads that fall into the [foundation or migration stages of adoption](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-program-implementation/reviewing-frameworks.html). Often, these are simple largely static workloads that have been built using traditional written procedures or those migrated *as is* using tools such as AWS Transform MGN from an on-premises environment. Migration tools, such as Migration Hub and MGN, can apply tags as part of the migration process. However, if tags were not applied during the original migration or the tagging schema has changed since then, the [Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html) (a feature of the AWS Management Console) allows you to search for resources using a variety of search criteria and add, modify, or delete tags in bulk. Search criteria can include resources with or without the presence of a particular tag or value. The AWS Resource Tagging API allows you to perform these functions programmatically. 

 As these workloads are modernized, resource types such as Auto Scaling groups are introduced. These resource types allow for greater elasticity and improved resilience. The auto scaling group manages Amazon EC2 instances on your behalf, however, you might still want the EC2 instances to be tagged consistently with the manually created resources. An [*Amazon EC2 launch template*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) provides the means to specify the tags that the Auto Scaling should apply to instances that it creates. 

 When the resources of a workload are being managed manually, it can be helpful to automate the tagging of resources. There are various solutions available. One approach is to use AWS Config Rules, which can check for `required_tags` and then start a Lambda function to apply them. AWS Config Rules is described in more detail later in this whitepaper. 

### Infrastructure as code (IaC) managed resources
<a name="infrastructure-as-code-iac-managed-resources"></a>

 AWS CloudFormation provides a common language for provisioning all the infrastructure resources in your AWS environment. CloudFormation templates are JSON or YAML files that create AWS resources in an automated manner. When you create AWS resources using CloudFormation templates, you can use the CloudFormation Resource Tags property to apply tags to supported resource types upon creation. Managing the tags as well as the resources with IaC helps ensure consistency. 

 When resources are created by AWS CloudFormation, the service automatically applies a set of AWS defined tags to the resources created by the AWS CloudFormation template. These are: 

```
aws:cloudformation:stack-name
aws:cloudformation:stack-id
aws:cloudformation:logical-id
```

 You can easily define a resource group based on the AWS CloudFormation stack. These AWS defined tags are inherited by the resources created by the stack. However, for Amazon EC2 instances within an Auto Scaling group, the [`AWS::AutoScaling::AutoScalingGroup` TagProperty](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html) needs to be set in the definition of the Auto Scaling group in your AWS CloudFormation template. Alternatively, if you are using an [EC2 Launch Template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) with the Auto Scaling group then you can define the tags in its definition. Using [EC2 Launch Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) with Auto Scaling groups or with an AWS container service is recommended. These services can help ensure consistent tagging of your Amazon EC2 instances and also support [Auto Scaling Across Multiple Instance Types & Purchase Options](https://aws.amazon.com/blogs/aws/new-ec2-auto-scaling-groups-with-multiple-instance-types-purchase-options/), which can improve resilience and optimize your compute costs. 

 [AWS CloudFormation Hooks](https://aws.amazon.com/blogs/mt/proactively-keep-resources-secure-and-compliant-with-aws-cloudformation-hooks/) provide developers with a means of keeping key aspects of their application consistent with their organization’s standards. Hooks can be configured to provide a *warning* or *prevent deployment*. This feature is best suited to checking key configuration elements in your templates, such as whether an Auto Scaling group is configured to apply customer defined tags to all the Amazon EC2 instances it launches, or to ensure that all Amazon S3 buckets are created with the required encryption settings. In both cases, evaluation of this compliance is being pushed to the earlier in the deployment process with AWS CloudFormation hooks before deployment. 

 AWS CloudFormation provides the capability to detect when a resource (see [Resources that support drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html)) provisioned from a template has been modified and resources no longer match their expected template configurations. This is known as *drift*. If you use automation to apply tags to resources managed via IaC, then you are modifying them, introducing drift. When using IaC, it's currently recommended to manage any tagging requirements as part of the IaC templates, implement AWS CloudFormation hooks, and publish AWS CloudFormation Guard rule sets that can be used by automation. 

### CI/CD pipeline managed resources
<a name="cicd-pipeline-managed-resources"></a>

 As the maturity of a workload increases, it’s likely that techniques such as continuous integration and continuous deployment (CI/CD) are adopted. These techniques help to reduce deployment risk by making it easier to deploy small changes more frequently with increased automation of testing. An observability strategy that detects unexpected behavior introduced by a deployment can automatically roll back the deployment with minimal user impact. As you get to the stage of deploying tens of times a day, applying tags retroactively is simply no longer practical. Everything needs to be expressed as code or configuration, version controlled, and, wherever possible, tested and evaluated before deployment into production. In the combined [develop and operations (DevOps) model](https://aws.amazon.com/devops/what-is-devops/), many of the practices address operational considerations as code and validate them early in the deployment lifecycle. 

 Ideally, you want to push these checks as early in the process as you can (as shown with AWS CloudFormation hooks), so that you can be confident that your AWS CloudFormation template meets your policies before they leave the developer's machine. 

 [AWS CloudFormation Guard 2.0](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/) provides the means to write preventative compliance rules for anything you can define with CloudFormation. The template is validated against the rules in the development environment. Clearly, this feature has a range of applications, but in this whitepaper, we will just look at some examples that would ensure the [`AWS::AutoScaling::AutoScalingGroup` TagProperty](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html) is always being used. 

The following is an example of a CloudFormation Guard rule: 

```
let all_asgs = Resources.*[ Type == 'AWS::AutoScaling::AutoScalingGroup' ]

rule tags_asg_automation_EnvironmentId when %all_asgs !empty {
    let required_tags = %all_asgs.Properties.Tags.*[ 
        Key == 'example-inc:automation:EnvironmentId' ] 
    %required_tags[*] {
        PropagateAtLaunch == 'true'
        Value IN ['Prod', 'Dev', 'Test', 'Sandbox']
        <<Tag must have a permitted value
          Tag must have PropagateAtLaunch set to 'true'>>
    }
}

rule tags_asg_costAllocation_CostCenter when %all_asgs !empty {
    let required_tags = %all_asgs.Properties.Tags.*[ 
        Key == 'example-inc:cost-allocation:CostCenter' ]
    %required_tags[*] {
        PropagateAtLaunch == 'true'
        Value == /^123-/
        <<Tag must have a permitted value
          Tag must have PropagateAtLaunch set to 'true'>>
    }
}
```

 In the code example, we filter the template for all resources that are of the type `AutoScalingGroup`, and then have two rules: 
+  **`tags_asg_automation_EnvironmentId`** - Checks that a tag with this key exists, has a value within the allowed list of values, and that `PropagateAtLaunch` is set to `true` 
+  **`tags_asg_costAllocation_CostCenter`** - Checks that a tag exists with this key, has a value that begins with the defined prefix value, and that `PropagateAtLaunch` is set to `true` 

### Enforcement
<a name="enforcement"></a>

 As described previously, **Resource Groups & Tag Editor** provides the means to identify where your resources fail to meet the tagging requirements defined in the tag policies applied to the OUs of the organization. Accessing the **Resource Groups & Tag Editor** console tool from within an Organization member account shows you the policies that apply to that account and the resource within the account that fail to meet the tag policy’s requirements. If accessed from the management account (and if **Tag policies** has *Access enabled* in services under AWS Organizations), then it is possible to view the [tag policy compliance for all the linked accounts in the organization](https://docs.aws.amazon.com/ARG/latest/userguide/tag-policies-orgs-evaluating-org-wide-compliance.html). 

 Within the Tag Policy itself, you can enable enforcement for specific resource types. In the following policy example, we’ve added enforcement such that all resources of types `ec2:instance` and `ec2:volume` are required to be compliant with the policy. There are some known limitations, such as there must be a tag on a resource for it to be evaluated by the tag policy. See [Resources that support enforcement with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_supported-resources-enforcement.html) for a list. 

#### ExampleInc-Cost-Allocation.json
<a name="exampleinc-cost-allocation.json"></a>

 The following is an example of a tag policy that reports and/or enforces Cost Allocation tags: 

```
{
  "tags": {
    "example-inc:cost-allocation:ApplicationId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:ApplicationId"
      },
      "tag_value": {
        "@@assign": [
          "DataLakeX",
          "RetailSiteX"
        ]
      },
      "enforced_for": {
        "@@assign": [
          "ec2:instance",
          "ec2:volume"
        ]
      }
    },
    "example-inc:cost-allocation:BusinessUnitId": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:BusinessUnitId"
      },
      "tag_value": {
        "@@assign": [
          "Architecture",
          "DevOps",
          "FinanceDataLakeX"
        ]
      },
      "enforced_for": {
        "@@assign": [
          "ec2:instance",
          "ec2:volume"
        ]
      }
    },
    "example-inc:cost-allocation:CostCenter": {
      "tag_key": {
        "@@assign": "example-inc:cost-allocation:CostCenter"
      },
      "tag_value": {
        "@@assign": [
          "123-*"
        ]
      },
      "enforced_for": {
        "@@assign": [
          "ec2:instance",
          "ec2:volume"
        ]
      }
    }
  }
}
```

 **AWS Config (`required_tag`)** 

 AWS Config is a service that allows you to assess, audit, and evaluate the configurations of your AWS resources (see [Resource types supported by AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)). In the case of tagging, we can use it to identify resources that are lacking tags with specific keys, using the `required_tags` rule (refer to [Resource types supported by required\_tags](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html)). From the earlier example, we might test for the existence of the key on all Amazon EC2 instances. In cases where the key doesn’t exist, the instance will be registered as non-compliant. This AWS CloudFormation template describes an AWS Config Rule to test for the presence of the mandatory keys describe in the table, on Amazon S3 buckets, Amazon EC2 instances, and Amazon EBS volumes. 

```
 Resources:
  MandatoryTags:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: ExampleIncMandatoryTags
      Description: These tags should be in place
      InputParameters:
        tag1Key: example-inc:cost-allocation:ApplicationId
        tag2Key: example-inc:cost-allocation:BusinessUnitId
        tag3Key: example-inc:cost-allocation:CostCenter
        tag4Key: example-inc:automation:EnvironmentId
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
        - "AWS::EC2::Instance"
        - "AWS::EC2::Volume"
      Source:
        Owner: AWS
        SourceIdentifier: REQUIRED_TAGS
```

 For environments where resources are managed manually, an AWS Config rule can be enhanced to automatically add the missing tag key to the resources using an automated remediation via an AWS Lambda function. While this works well for static workloads, it's progressively less effective as you start managing your resources via IaC and deployment pipelines. 

 **AWS Organizations – Service control policies (SCPs)** are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization or organizational unit (OU). SCPs only affect users and roles that are managed by accounts that are part of the organization. Although they do not affect resources directly, they restrict the permissions of users and roles which includes the permissions for tagging actions. With regards to tagging, SCPs can provide additional granularity for tag enforcement in addition to what tag policies can provide. 

 In the following example, the policy will deny `ec2:RunInstances` requests where the `example-inc:cost-allocation:CostCenter` tag is not present. 

 The following is a deny SCP: 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "DenyRunInstanceWithNoCostCenterTag",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:*:*:instance/*"
      ],
      "Condition": {
        "Null": {
          "aws:RequestTag/example-inc:cost-allocation:CostCenter": "true"
        }
      }
    }
  ]
}
```

------

 It is not possible to retrieve the effective service control policy that applies to a linked account by design. Where you enforce tagging with SCPs, documentation needs to be available to developers so they can ensure their resources meet the policies that have been applied to their accounts. Providing read only access to CloudTrail events within their account can support developers in the task of debugging when their resources fail to comply. 

## Measuring tagging effectiveness and driving improvements
<a name="measuring-tagging-effectiveness-and-driving-improvements"></a>

 After you have implemented a tagging strategy, it's important to measure its effectiveness against the target use cases. The measure of effectiveness will vary by use case. For example: 
+  **Cost attribution** - You could measure the tagging coverage of resources based on spend using tools such as [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/). For example, you could track the *percent of tagged or untagged* resources that generate charges, particularly monitoring specific tag keys. 
+  **Automation** - You might want to audit if the desired result has been achieved. For example, whether non-production Amazon EC2 instances are suspended outside of business hours, auditing instance start and stop times. 

 [Resource Groups & Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) within the management account provides additional capabilities to analyze tag policy compliance for all the linked accounts in your organization. 

 Based on the results of the measurement of your tagging effectiveness, identify if any improvements or alterations are needed in any of the steps such as use case definition, tagging schema implementation or enforcement. Make necessary changes and repeat the cycle until desired effectiveness is achieved. In the example with cost attribution, you can look at percentage improvement. 

 Since it’s the developers and operators that need to perform the actual tagging of resources, it's critical to have them take ownership. This isn’t the only additional responsibility that teams typically assume in their journey of AWS adoption. Increased responsibility for the security and cost of developing and operating their application are also important. Organizations often use goals and targets as means of motivating the adoption of new practices, so this can also apply here. 

# Tagging use cases
<a name="tagging-use-cases"></a>

**Topics**
+ [Tags for cost allocation and financial management](#tags-for-cost-allocation-and-financial-management)
+ [Tags for operations and support](#tags-for-operations-and-support)
+ [Tags for data security, risk management, and access control](#tags-for-data-security-risk-management-and-access-control)

## Tags for cost allocation and financial management
<a name="tags-for-cost-allocation-and-financial-management"></a>

 One of the first tagging use cases organizations often tackle is visibility and management of cost and usage. There are usually a few reasons for this: 
+  **It's typically a well understood scenario and requirements are well known.** For example, finance teams want to see the total cost of workloads and infrastructure that span across multiple services, features, accounts, or teams. One way to achieve this cost visibility is through consistent tagging of resources. 
+  **Tags and their values are clearly defined.** Usually, cost allocation mechanisms already exist in an organization’s finance systems, for example, tracking by cost center, business unit, team, or organization function. 
+  **Rapid, demonstrable return on investment.** It’s possible to track cost optimization trends over time when resources are tagged consistently, for example, for resources that were rightsized, auto-scaled, or put on a schedule. 

 Understanding how you incur costs in AWS allows you to make informed financial decisions. Knowing where you have incurred costs at the resource, workload, team, or organization level enhances your understanding of the value delivered at the applicable level when compared to the business outcomes achieved. 

 The engineering teams might not have experience with financial management of their resources. Attaching a person with a specialized skill in AWS financial management who can train engineering and development teams on the basics of AWS financial management and create a relationship between finance and engineering to foster the culture of FinOps will help achieve measurable outcomes for the business and encourage teams to build with cost in mind. Establishing good financial practices is covered in depth by the [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) of the Well-Architected Framework, but we will touch on a few of the fundamental principles in this whitepaper. 

### Cost allocation tags
<a name="cost-allocation-tags"></a>

 Cost allocation refers to the assignment or distribution of incurred costs to the users or beneficiaries of those costs following a defined process. In the context of this whitepaper, we divide cost allocation into two types: *showback* and *chargeback*. 

 *Showback* tools and mechanisms help increase cost awareness. *Chargeback* helps with cost recovery and drives enablement of cost awareness. *Showback* is about presentation, calculation, and reporting of charges incurred by a specific entity, such as business unit, application, user, or cost center. For example: “the infrastructure engineering team was responsible for $X of AWS spend last month”. *Chargeback* is about an actual charging of incurred costs to those entities via an organization’s internal accounting processes, such as financial systems or journal vouchers. For example: “$X was deducted from the infrastructure engineering team's AWS budget.” In both cases, tagging resources appropriately can help allocate the cost to an entity, the only difference being whether or not someone is expected to make a payment. 

 Your organization's financial governance might require transparent accounting of costs incurred at the application, business unit, cost center, and team level. Performing cost attribution supported by [Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) provides you the data necessary to accurately attribute the costs incurred by an entity from appropriately tagged resources. 
+  **Accountability** — Ensure that cost is allocated to those who are responsible for resource usage. A single point of service or group can be accountable for spend reviews and reporting. 
+  **Financial transparency** — Show a clear view into cash allocations towards IT by creating effective dashboards and meaningful cost analysis for leadership. 
+  **Informed IT investments** — Track ROI based on project, application, or business line, and empower teams to make better business decisions, for example, allocate more funding to revenue generating applications. 

 In summary, cost allocation tags can help to tell you: 
+  Who owns the spend and is responsible for optimizing it? 
+  What workload, application, or product is incurring the spend? Which environment or stage? 
+  What spend areas are growing fastest? 
+  How much spend can be deducted from an AWS budget based on past trends? 
+  What was the impact of cost optimization efforts within particular workloads, applications, or products? 

 Activating resource tags for cost allocation helps with the definition of measurement practices within the organization that can be used to provide the visibility of AWS usage that increases transparency into accountability for spend. It also focuses on creating an appropriate level of granularity with respect to cost and usage visibility and inﬂuencing cloud consumption behaviors through cost allocation reporting and KPI tracking. 

### Building a cost allocation strategy
<a name="building-a-cost-allocation-strategy"></a>

#### Defining and implementing a cost allocation model
<a name="defining-and-implementing-a-cost-allocation-model"></a>

Create account and cost structure for the resources being deployed in AWS. Establish the relationship between costs from AWS spend, how those costs were incurred, and who or what incurred those costs. Common cost structures are based on AWS Organizations, AWS accounts, environments, and entities within your organizations, such as a line of business or workload. Cost structures can be based on multiple attributes to permit the examination of costs in different ways or at different levels of granularity such as rolling up the costs of individual workloads to the line of business they serve.

 When choosing a cost structure that aligns with the desired outcomes, evaluate the cost allocation mechanisms on the *ease of implementation* versus *desired accuracy*. This might include considerations in regards to accountability, tooling availability, and cultural changes. Three popular cost allocation models that AWS customers usually start from are: 
+  **Account-based** — This model requires the least amount of effort and provides high accuracy for showbacks and chargebacks, and is suitable for organizations that have a defined account structure (and is consistent with the recommendations of the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper). This provides clear cost visibility on a per-account basis. For cost visibility and allocation, you can use [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html), [Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), as well as [AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html) for cost monitoring and tracking. These tools provide filtering and grouping options by AWS accounts. From a cost allocation perspective, this model doesn’t have to rely on accurate tagging of individual resources. 
+  **Business Unit or Team-based** — Cost allocatable to teams, business units, or organizations within an enterprise. This model requires a moderate amount of effort, provides high accuracy for showbacks and chargebacks, and is suitable for organizations that have a defined account structure (typically using AWS Organizations), with separation between various teams, applications, and workload types. This provides clear cost visibility across teams and applications, and as additional benefit reduces the risk of hitting [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) within a single AWS account. For example, each team may have five accounts (`prod`, `staging`, `test`, `dev`, `sandbox`), and no two teams and applications will share the same account. With such structure [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) will then provide the functionality to group accounts or other tags (“meta-tagging”) into categories, which can be tracked in the tools mentioned in the previous example. It’s important to note that AWS Organizations allows tagging of accounts and organizational units (OUs), however these tags will not be applicable for cost allocation and billing reporting (that is, you cannot group or filter your cost in AWS Cost Explorer by OU). AWS Cost Categories should be used for this purpose. 
+  **Tag-based** — This model requires more effort compared to the previous two and will provide high accuracy for showbacks and chargebacks depending on the requirements and end goal. While we strongly recommend that you adopt the practices outlined in [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper, realistically customers often find themselves with mixed and complex account structures that take time to migrate away from. Implementing a rigorous and effective tagging strategy is the key in this scenario, followed by [activating relevant tags for cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the Billing and Cost Management console (in AWS Organizations, tags can be activated for cost allocation only from the Management Payer account). After tags are activated for cost allocation, then tools for cost visibility and allocation that were mentioned in the previous methods can be used for showbacks and chargebacks. Note that cost allocation tags are not retrospective, and will only appear in billing reporting and cost tracking tools after they were activated for cost allocation. 

 To summarize, if you need to track costs by business unit, you can use [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html) to group linked accounts within AWS Organization accordingly and view this grouping in billing reports. When you create separate accounts for production and non-production environments, you can also filter the costs related to environments in tools such as [AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html), or track those costs using [AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html). Finally, if your use case requires more granular cost tracking, for example, by individual workloads or applications, you can tag resources within those accounts accordingly, [activate those tag keys for cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) on the management account, and then filter that cost by tag keys in the billing reporting tools. 

#### Establishing cost reporting and monitoring processes
<a name="establing-cost-reporting-and-monitoring-processes"></a>

 Start with identifying the types of costs that are important for internal stakeholders (for example, daily spend, cost by account, cost by X, amortized costs). By doing so, you can mitigate budgetary risks associated with unexpected or anomalous spend faster than waiting for the finalized AWS invoice. Tags provide the attribution that enables these reporting scenarios. Insights gained from reporting can inform your actions to mitigate the impact from anomalous and unexpected spend on financial budgets. When there is an unexpected surge in costs, it's important to evaluate if there has been an unexpected surge in the value delivered so that you can determine if and what action is required. 

 When developing a tagging strategy to support cost allocation, keep in mind the following elements: 
+  **AWS Organizations** - Cost allocation within multiple accounts can be performed by account, groups of accounts, or group of tags created for resources on those accounts. Tags created for resources residing in individual accounts in AWS Organizations can be used for cost allocation only from the management account. 
+  **AWS Account** - Cost allocation within one AWS account can be performed by additional dimensions such as services or regions. It’s possible to further tag resources within an account and work with the groups of such resource tags. 
+  **Cost Allocation Tags** - Both user-created tags and AWS generated tags can be activated for cost allocation, if necessary. Enabling tags for cost allocation in the billing console (of the management account in AWS Organizations) helps with showbacks and chargebacks. 
+  **Cost Categories** - AWS Cost Categories allow grouping accounts and grouping tags (“meta-tagging”) within an AWS Organization, which further provides capability to analyze the cost related to these categories through tools such as AWS Cost Explorer, AWS Budgets and AWS Cost and Usage Report. 

#### Performing showback and chargeback for business units, teams, or organizations within the enterprise
<a name="performing-showback-and-chargeback-for-business-units"></a>

 Attribute costs using your cost allocation process supported by your cost structure and cost allocation tags. Tags can be used to provide showback to teams that are not directly responsible to pay for costs but are responsible for having incurred those costs. This approach provides awareness of their contribution to spend and how those costs are incurred. Perform chargeback to the teams that are directly responsible for costs to recover the expense of the resources they have consumed, and to provide them with awareness of those costs and how they were incurred. 

#### Measuring and circulating eﬃciency or value KPIs
<a name="measuring-and-circulating-kpis"></a>

 Agree on a set of unit cost or KPI metrics to measure the impact of your cloud financial management investments. This exercise creates a common language across technology and business stakeholders, and tells an eﬃciency-based story, rather than a story focused solely on absolute, aggregate spend. For additional information check this blog that talks [how unit metrics can help create alignment between business functions](https://aws.amazon.com/blogs/aws-cloud-financial-management/unit-metrics-help-create-alignment-between-business-functions/). 

#### Allocating unallocatable spend
<a name="allocating-unallocatable-spend"></a>

 Depending on the organization’s accounting practices, different charge types might require different treatment. Identify the resources or cost categories that cannot be tagged. Depending on the services used and those planned to be used, agree on the mechanisms on how to treat and measure such unallocatable spend. For example, check the list of resources that are supported by [AWS Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the *AWS Resource Groups and Tags User Guide*. 

 A common example of cost category that cannot be tagged is some fees for commitment-based discounts such as Reserved Instances (RI) and Savings Plans (SP). While subscription fees and unused SP and RI fees cannot be tagged in advance of appearing in billing reporting tools, you can track how RI and SP discounts apply to accounts, resources and their tags in AWS Organizations after the fact. For example, in AWS Cost Explorer it’s possible to look at the amortized cost, group that spend by the relevant tag keys and apply filters relevant to your use case. In AWS Cost and Usage Report (CUR), you can filter out lines that correspond to usage covered by RI and SP discounts (read more in the use cases section of the [CUR documentation](https://docs.aws.amazon.com/cur/latest/userguide/use-cases.html)) and select the columns that are only relevant to you. Each tag key activated for cost allocation will be presented in its own separate column at the end of the CUR report, similarly to how it's presented in other legacy billing reports, such as [monthly cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html). For additional reference, check the [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/cost/300_labs/300_cur_queries/) for examples of gaining cost and usage insights from CUR data. 

#### Reporting
<a name="reporting-charges"></a>

 In addition to AWS tools available to assist with showbacks and chargebacks, there is a range of other AWS created and third-party solutions that can help monitor the cost of tagged resources, and measure the effectiveness of the tagging strategy. Depending on both the requirements and the end objective of the organization, one could either invest time and resources into building customized solutions or purchase tools provided by one of the [AWS Cloud Management Tools Competency Partners](https://aws.amazon.com/products/management-tools/partner-solutions/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-type=%2Aall&awsf.Filter%20Name%3A%20partner-solutions-filter-partner-use-case=%2Aall&awsf.partner-solutions-filter-partner-location=%2Aall). If you decide to create your own *single source of truth* cost allocation tool with controlled parameters relevant for the business, AWS Cost and Usage Report (CUR) provides most detailed cost and usage data and enables creation of customized optimization dashboards, allowing filtering and grouping by accounts, services, cost categories, cost allocation tags, and multiple other dimensions. Among CUR-based solutions developed by AWS that can be used as one of these tools, check [Cloud Intelligence Dashboards](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/) on the AWS Well-Architected Labs website. 

## Tags for operations and support
<a name="tags-for-operations-and-support"></a>

 An AWS environment will have multiple accounts, resources, and workloads with differing operational requirements. Tags can be used to provide context and guidance to support operations teams to enhance management of your services. Tags can also be used to provide operational governance transparency of the managed resources. 

 Some of the main factors driving consistent definition of operational tags are: 
+  **To filter resources during automated infrastructure activities.** For example, when deploying, updating or deleting resources. Another is the scaling of resources for cost optimization and out of hours usage reductions. See [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) solution for a working example. 
+  **Identifying isolated or deprecating resources.** Resources that have exceeded their defined lifespan or have been flagged for isolation by internal mechanisms should be appropriately tagged so as to assist support personnel in their investigation. Deprecating resources should be tagged before isolation, archival and deletion. 
+  **Support requirements for a group of resources.** Resources often have different support requirements, for example, these requirements could be negotiated between teams or set as part of an applications criticality. Further guidance on operating models can be found in the [Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model.html). 
+  **Enhance the incident management process.** By tagging resources with tags that offer greater transparency in incident management process, support teams and engineers as well as Major Incident Management (MIM) teams can more effectively manage events. 
+  **Backups.** Tags can also be used to identify the frequency your resources need to be backed up, and where the backup copies need to go or where to restore the backups. [Prescriptive guidance for Backup and recovery approaches on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/welcome.html). 
+  **Patching.** Patching mutable instances running in AWS is crucial in both your overarching patching strategy and for the patching of zero-day vulnerabilities. Deeper guidance on the wider patching strategy can be found in the [prescriptive guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/welcome.html). Patching of zero-day vulnerabilities is discussed in this [blog](https://aws.amazon.com/blogs/mt/avoid-zero-day-vulnerabilities-same-day-security-patching-aws-systems-manager/). 
+  **Operational observability**. Having an operational KPI strategy translated to resource tags will help operations teams to better track whether targets are being met to enhance business requirements. Developing a KPI strategy is a separate topic, but tends to be focused on a business operating in a steady state or where to measure the impact and outcomes of change. The [KPI Dashboards](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/cost-usage-report-dashboards/dashboards/2c_kpi_dashboard/) (AWS Well-Architected labs) and the Operations KPI Workshop (an [AWS Enterprise Support proactive service](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/)) both address measure performance in a steady state. The AWS enterprise strategy blog article [Measuring the Success of Your Transformation](https://aws.amazon.com/blogs/enterprise-strategy/measuring-the-success-of-your-transformation/), explores KPI measurement for a transformation program, such as IT modernization or migrating from on premises to AWS. 

### Automated infrastructure activities
<a name="automated-infrastructure-activities"></a>

 Tags can be used in a wide range of automation activities when managing infrastructure. Use of [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/index.html), for example, will allow you to manage automations and runbooks on resources specified by the defined key-value pair you create. For managed nodes, you could define a set of tags to track or target nodes by operating system and environment. You could then run an update script for all nodes in a group or review the status of those nodes. [Systems Manager Resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/taggable-resources.html) can also be tagged to further refine and track your automated activities. 

 Automating the start and stop lifecycle of environment resources can provide a significant cost reduction to any organization. [Instance scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/) is an example of a solution that can start and stop Amazon EC2 and Amazon RDS instances when they are not required. For example, developer environments utilizing Amazon EC2 or Amazon RDS instances that are not required to be running on weekends are not utilizing the cost saving potential that the shutting down of those instances can provide. By analyzing the needs of teams and their environments, and properly tagging these resources to automate their management, you can utilize your budget effectively. 

 *An example schedule tag used by instance scheduler on an Amazon EC2 instance:* 

```
{
    "Tags": [
        {
            "Key": "Schedule",
            "ResourceId": "i-1234567890abcdef8",
            "ResourceType": "instance",
            "Value": "mon-9am-fri-5pm"
        }
    ]
}
```

### Workload lifecycle
<a name="workload-lifecycle"></a>

**Review accuracy of supporting operational data.** Make sure that there are periodic reviews of the tags associated with your workload lifecycle, and that the appropriate stakeholders are involved in these reviews. 

 *Table 7 – Review operational tags as part of the workload lifecycle* 


|  Use Case  |  Tag Key  |  Rationale  |  Example Values  | 
| --- | --- | --- | --- | 
|  Account Owner  | example-inc:account-owner:owner  |  The owner of the account and it's contained resources.  | ops-center, dev-ops, app-team  | 
|  Account Owner Review  | example-inc:account-owner:review  |  Review of account ownership details being up to date and correct.  | <review date in the correct format defined in your tagging library>  | 
|  Data Owner  | example-inc:data-owner:owner  |  The data owner of the accounts residing data.  | bi-team, logistics, security  | 
|  Data Owner Review  | example-inc:data-owner:review  |  Review of data ownership details being up to date and correct.  | <review date in the correct format defined in your tagging library>  | 

#### Assigning tags to suspending accounts before migrating to the suspended OU
<a name="assigning-tags-to-suspending-accounts"></a>

 Before suspending an account and moving into the suspended OU as detailed in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper, tags should be added to the account to aid in your internal tracing and auditing of an account’s lifecycle. For example, a relative URL or ticket reference on an organization’s ITSM ticketing system, that shows the audit trail for an application being suspended. 

 *Table 8 - Add operational tags when workload lifecycle enters new stage* 


|  Use Case  |  Tag Key  |  Rationale  |  Example Values  | 
| --- | --- | --- | --- | 
|  Account Owner  | example-inc:account-owner:owner  |  The owner of the account and it's contained resources.  | ops-center, dev-ops, app-team  | 
|  Data Owner  | example-inc:data-owner:owner  |  The data owner of the accounts residing data.  | bi-team, logistics, security  | 
|  Suspended Date  | example-inc:suspension:date  |  The date that the account was suspended  |  <suspended date in the correct format defined in your tagging library>  | 
|  Approval for suspension  | example-inc:suspension:approval  |  The link to the approval of account suspension  | workload/deprecation  | 

### Incident management
<a name="incident-management"></a>

 Tags can play a vital part in all phases of incident management starting from incident logging, prioritization, investigation, communication, resolution to closure. 

 Tags can detail where an incident should be logged, the team or teams that should be informed of the incident, and the defined escalation priority. It’s important to remember that tags are not encrypted, so consider what information you store in them. Also, in organizations, teams, and reporting lines, responsibilities change, so consider storing a link to a secure portal where this information can be more effectively managed. These tags don’t need to be exclusive. For instance, the application ID could be used to lookup the escalation paths in an IT service management portal. Make sure it is clear in your operational definitions that this tag is being used for multiple purposes. 

 Operational requirement tags can be detailed as well, to help incident managers and operations personnel further refine their objectives in response to an incident or event. 

 Relative links (to the knowledge system base URL) for [runbooks](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.runbook.en.html) and [playbooks](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.playbook.en.html) can be included as tags to assist the responding teams in identifying corresponding process, procedure and documentation. 

 *Table 9 - Use operational tags to inform incident management* 


|  Use Case  |  Tag Key  |  Rationale  |  Example Values  | 
| --- | --- | --- | --- | 
|  Incident Management  | example-inc:incident-management:escalationlog  |  The system in use by the supporting team to log incidents  | jira, servicenow, zendesk  | 
|  Incident Management  | example-inc:incident-management:escalationpath  |  Path of escalation  | ops-center, dev-ops, app-team  | 
|  Cost Allocation and Incident Management  | example-inc:cost-allocation:CostCenter |  Monitor costs by cost center. This is an example of a dual use tag where the cost center is being used as an application code for incident logging  | 123-\*  | 
|  Backup Schedule  | example-inc:backup:schedule  |  Backup schedule of the resource  | Daily  | 
|  Playbook / Incident Management  | example-inc:incident-management:playbook  |  Documented playbook  | webapp/incident/playbook  | 

### Patching
<a name="patching"></a>

 Organizations can automate their patching strategy for mutable compute environments and keep mutable instances in-line with the defined patch baseline of that application environment by using AWS Systems Manager Patch Manager and AWS Lambda. A tagging strategy for mutable instances within these environments can be managed by assigning said instances to **Patch Groups** and **Maintenance Windows**. See the following examples for a Dev → Test → Prod split. AWS prescriptive guidance is available for the [patch management of mutable instances.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/welcome.html) 

 *Table 10 - Operational tags can be environment specific* 


|  Development  |  Staging  |  Production  | 
| --- | --- | --- | 
|  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab111",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#1 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab222",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab333",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-DEV-AL2"<br />}<br />]<br />}<br /></pre>  |  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab444",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#2 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab555",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab666",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-TEST-AL2"<br />}<br />]<br />}<br /></pre>  |  <pre>{<br />"Tags": [<br />{<br />"Key": "Maintenance Window",<br />"ResourceId": "i-012345678ab9ab777",<br />"ResourceType": "instance",<br />"Value": "cron(30 23 ? * TUE#3 *)"<br />},<br />{<br />"Key": "Name",<br />"ResourceId": "i-012345678ab9ab888",<br />"ResourceType": "instance",<br />"Value": "WEBAPP"<br />},<br />{<br />"Key": "Patch Group",<br />"ResourceId": "i-012345678ab9ab999",<br />"ResourceType": "instance",<br />"Value": "WEBAPP-PROD-AL2"<br />}<br />]<br />}<br /></pre>  | 

 Zero-day vulnerabilities can also be managed by having tags defined to complement your patching strategy. Refer to [Avoid zero-day vulnerabilities with same-day security patching using AWS Systems Manager](https://aws.amazon.com/blogs/mt/avoid-zero-day-vulnerabilities-same-day-security-patching-aws-systems-manager/) for detailed guidance. 

### Operational observability
<a name="operational-observability"></a>

 Observability is required to gain actionable insights into the performance of your environments and help you to detect and investigate problems. It also has a secondary purpose that allows you to define and measure key performance indicators (KPIs) and service level objectives (SLOs) such as uptime. For most organizations, important operations KPIs are mean time to detect (MTTD) and mean time to recover (MTTR) from an incident. 

Throughout observability, context is important, because data is collected and then associated tags are gathered. Regardless of the service, application, or application tier that you are focusing on, you can filter and analyze for that specific dataset. Tags can be used to automate onboarding to CloudWatch Alarms so that the right teams can be alerted when certain metric thresholds are breached. For example, a tag key `example-inc:ops:alarm-tag` and the value on it could indicate creation of the CloudWatch Alarm. A solution demonstrating this is described in [Use tags to create and maintain Amazon CloudWatch alarms for Amazon EC2 instances](https://aws.amazon.com/blogs/mt/use-tags-to-create-and-maintain-amazon-cloudwatch-alarms-for-amazon-ec2-instances-part-1/).

 Having too many alarms configured can easily create an alert storm—when a large number of alarms or notifications rapidly overwhelm operators and reduce their overall effectiveness while operators are manually triaging and prioritizing individual alarms. Additional context for the alarms can be provided in the form of tags, which means that rules can be defined within Amazon EventBridge to help ensure that focus is given to the upstream issue rather than downstream dependencies. 

 The role of operations alongside DevOps is often overlooked, but for many organizations, central operations teams still provide a critical first response outside of normal business hours. (More details can be found about this model in the [Operational Excellence whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/separated-aeo-ieo-with-cent-gov-and-partner.html).) Unlike the DevOps team that owns the workload, they typically do not have the same depth of knowledge, so the context that tags provide within dashboards and alerts, can direct them to the correct runbook for the issue, or initiate an automated runbook (refer to the blog post [Automating Amazon CloudWatch Alarms with AWS Systems Manager](https://aws.amazon.com/blogs/mt/automating-amazon-cloudwatch-alarms-with-aws-systems-manager/)). 

## Tags for data security, risk management, and access control
<a name="tags-for-data-security-risk-management-and-access-control"></a>

 Organizations have varying needs and obligations to meet regarding the appropriate handling of data storage and processing. Data classification is an important precursor for several use cases, such as access control, data retention, data analysis, and compliance. 

### Data security and risk management
<a name="data-security-and-risk-management"></a>

Within an AWS environment, you will probably have accounts with differing compliance and security requirements. For example, you might have a developer sandbox, and an account hosting the production environment for a highly regulated workload, such as processing payments. By isolating them into different accounts, you can [apply distinct security controls](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html#apply-distinct-security-controls-by-environment), [constrain access to sensitive data](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html#constrain-access-to-sensitive-data), and reduce the scope of audit for regulated workloads. 

 Adopting a single standard for all workloads can lead to challenges. While many controls apply equally across an environment, some controls are excessive or irrelevant for accounts that don't need to meet specific regulatory frameworks, and accounts where no personal identifiable data will ever be present (for example, a developer sandbox, or workload development accounts). This typically leads to false positive security findings that must be triaged and closed with no action, which takes effort away from findings that should be investigated. 

 *Table 11 – Example data security and risk management tags* 


|  Use case  |  Tag Key  |  Rationale  |  Example Values  | 
| --- | --- | --- | --- | 
| Incident management  | example-inc:incident- management:escalationlog |  The system in use by the supporting team to log incidents  |  jira, servicenow, zendesk  | 
| Incident management  | example-inc:incident- management:escalationpath |  Path of escalation  | ops-center, dev-ops, app-team  | 
| Data classification  | example-inc:data:classification |  Classify data for compliance and governance  | Public, Private, Confidential, Restricted  | 
| Compliance  | example-inc:compliance:framework |  Identifies the compliance framework the workload is subject to  | PCI-DSS, HIPAA  | 

 Manually managing different controls across an AWS environment is both time consuming and error prone. The next step is to automate the deployment of appropriate security controls, and configure inspection of resources, based on the classification of that account. By applying tags to the accounts and the resources within them, the deployment of controls can be automated and configured appropriately for the workload. 

**Example: **

 A workload includes an Amazon S3 bucket with the tag `example-inc:data:classification` with the value `Private`. The security tooling automation deploys AWS Config rule `s3-bucket-public-read-prohibited`, which checks the Amazon S3 bucket’s Block Public Access settings, the bucket policy, and the bucket access control list (ACL), confirming the bucket’s configuration is appropriate for its data classification. To ensure the content of the bucket is consistent with the classification, [Amazon Macie can be configured to check for personal identifiable information (PII)](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-macie-supports-criteria-based-bucket-selection-sensitive-data-discovery-jobs/). The blog [Using Amazon Macie to Validate S3 Bucket Data Classification](https://aws.amazon.com/blogs/architecture/using-amazon-macie-to-validate-s3-bucket-data-classification/) explores this pattern in greater depth. 

 Certain regulatory environments, such as insurance and healthcare, might be subject to mandatory data retention policies. Data retention using tags, combined with Amazon S3 Lifecycle policies, can be an effective and simple way to scope object transitions to a different storage tier. Amazon S3 Lifecycle rules can also be used to expire objects for data deletion after the mandatory hold period expires. Refer to [Simplify your data lifecycle by using object tags with Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/) for an in-depth guide to this process. 

 Additionally, when triaging or addressing security finding, tags can provide the investigator with important context that helps qualify the risk, and aids in engaging the appropriate teams to investigate or mitigate the finding. 

### Tags for identity management and access control
<a name="tags-for-identity-management-and-access-control"></a>

 When managing access control across an AWS environment with AWS IAM Identity Center, tags can enable several patterns for scaling. There are several delegation patterns that can be applied, some are based on tagging. We’ll address them individually and provide links to further reading on each. 

#### ABAC for individual resources
<a name="abac-for-individual-resources"></a>

 IAM Identity Center users and IAM roles support attribute-based access control (ABAC), which allows you to define access to operations and resources based on tags. ABAC helps reduce the need to update permission policies and helps you to base access off of employee attributes from your corporate directory. If you are already using a multi-account strategy, ABAC can be used in addition to role-based access control (RBAC) to provide multiple teams operating in the same account granular access to different resources. For example, IAM Identity Center users or IAM roles can include conditions to limit access to specific Amazon EC2 instances which otherwise would have to be explicitly listed in each policy in order to access them. 

 Since an ABAC authorization model depends on tags for access to operations and resources, it is important to provide guardrails to prevent unintended access. SCPs can be used to protect tags across your organization by only allowing tags to be modified under certain conditions. The blogs [Securing resource tags used for authorization using a service control policy in AWS Organizations](https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/) and [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) provide information on how to implement this. 

 Where long-lived Amazon EC2 instances are being used to support more traditional operations practices then this approach can be utilized, the blog [Configure IAM Identity Center ABAC for Amazon EC2 instances and Systems Manager Session Manager](https://aws.amazon.com/blogs/security/configure-aws-sso-abac-for-ec2-instances-and-systems-manager-session-manager/) discusses this form of attribute based access control in more detail. As mentioned earlier, not all resource types support tagging, and of those that do, not all support enforcement using tag policies, so it’s a good idea to evaluate this prior to starting to implement this strategy on an AWS account.

To learn about services that support ABAC, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). 

# Conclusion
<a name="conclusion"></a>

AWS resources can be tagged for a variety of purposes, from implementing a cost allocation strategy to supporting automation or authorizing access to AWS resources. Implementing a tagging strategy can be challenging for some organizations, owing to the number of stakeholder groups involved and considerations such as data sourcing and tag governance. 

 In this whitepaper, we’ve outlined recommendations regarding designing and implementing a tagging strategy in an organization based on operational practices, defined use cases, stakeholders involved in the process, and tools and services provided by AWS. When it comes to a tagging strategy, it’s a process of iteration and improvement, where you start small from your immediate priority, identify relevant use cases across your organization, and then implement and grow the tagging schema as you need to, while continuously measuring and improving effectiveness. We’ve pointed out that a well-defined set of tags within your organization will allow you to relate AWS usage and consumption to teams responsible for the resources and business purpose for which they exist, in order to align with organizational strategy and value.

# Contributors
<a name="contributors"></a>

 Contributors to this document include: 
+  Chris Pates, Sr Specialist Technical Account Manager, Amazon Web Services 
+  Vijay Shekhar Rao, Enterprise Support Lead, Amazon Web Services 
+  Nataliya Godunok, Sr Specialist Technical Account Manager, Amazon Web Services 
+  Yogish Kutkunje Pai, Sr Solutions Architect, Amazon Internet Services Private Limited 
+  Jamie Ibbs, Sr Specialist Technical Account Manager, Amazon Web Services 

# Further reading
<a name="further-reading"></a>

 For more information, refer to the following resources: 
+  [AWS re:Invent 2020: Working backwards: Amazon’s approach to innovation](https://www.youtube.com/watch?v=aFdpBqmDpzM) 
+  [AWS Prescriptive Guidance: Automated patching for mutable instances in the hybrid cloud using AWS Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patch-management-hybrid-cloud/patch-management-hybrid-cloud.pdf) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 

 **AWS Well-Architected** 
+  [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) 
+  [Operational Excellence Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html) 
+  [Plan for Disaster Recovery (DR) - AWS Well-Architected Reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html) 
+  [Cost Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) 
+  [AWS Well-Architected Labs: Enable AWS-Generated Cost Allocation Tags](https://wellarchitectedlabs.com/cost/100_labs/100_1_aws_account_setup/8_cost_tags/) 
+  [AWS Well-Architected Labs: Tag Policies](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/) 
+  [AWS Well-Architected Labs: AWS CUR Query Library](https://wellarchitectedlabs.com/cost/300_labs/300_cur_queries/) 

 **AWS blogs** 
+  [AWS Health Aware – Customize AWS Health Alerts for Organizational and Personal AWS Accounts](https://aws.amazon.com/blogs/mt/aws-health-aware-customize-aws-health-alerts-for-organizational-and-personal-aws-accounts/) 
+  [How to Automatically Tag Amazon EC2 Resources in Response to API Events](https://aws.amazon.com/blogs/security/how-to-automatically-tag-amazon-ec2-resources-in-response-to-api-events/) 
+  [AWS Generated vs. User-Defined Cost Allocation Tag](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-allocation-blog-series-2-aws-generated-vs-user-defined-cost-allocation-tag/) 
+  [Cost Tagging and Reporting with AWS Organizations](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/) 
+  [Patching your Windows EC2 instances using AWS Systems Manager Patch Manager](https://aws.amazon.com/blogs/mt/patching-your-windows-ec2-instances-using-aws-systems-manager-patch-manager/) 
+  [Avoid zero-day vulnerabilities with same-day security patching using AWS Systems Manager](https://aws.amazon.com/blogs/mt/avoid-zero-day-vulnerabilities-same-day-security-patching-aws-systems-manager/) 

 **AWS documentation** 
+  [Using Cost Allocation Tags - AWS Billing and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) 
+  [What are AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) 
+  [AWS Resource Groups API Reference](https://docs.aws.amazon.com/ARG/latest/APIReference/Welcome.html) 
+  [How can I use IAM policy tags to restrict how an EC2 instance or EBS volume can be created?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-tags-restrict/) 
+  [Mutable vs immutable update models](https://docs.aws.amazon.com/managedservices/latest/appguide/compute-instance-mutability-aog.html) 

 **Other** 
+  Bryar, C. and Carr, B. (2021). [*Working Backwards: Insights, Stories, and Secrets from Inside Amazon*](https://www.amazon.com/dp/1250267595). London Macmillan. 
+  [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) (GitHub) 

# Document revisions
<a name="document-revisions"></a>

To be notified about updates to this whitepaper, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Minor update](#document-revisions) | Clarified guidance to recommend not using keys that only differ in casing. | June 10, 2025 | 
| [Minor update](#document-revisions) | Changed CloudEndure references to AWS Transform MGN. | May 8, 2025 | 
| [Minor update](#document-revisions) | Updates to identity management | March 30, 2023 | 
| [Minor revision](#document-revisions) | Updated reference in ABAC for individual resources. | February 24, 2023 | 
| [Minor revision](#document-revisions) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | February 6, 2023 | 
| [Major revision](#document-revisions) | Added more specific reference for resource types supported by AWS Config rule `required_tags`. | January 18, 2023 | 
| [Major revision](#document-revisions) | Updated to include the latest practices and service capabilities, especially in the area of identity. | September 29, 2022 | 
| [Minor update](#document-revisions) | Fixed table formatting in PDF version. | April 25, 2022 | 
| [Major revision](#document-revisions) | Updated document structure and expanded Tagging Strategy and Use Cases sections. Added more prescriptive guidance based on the latest tools, techniques, and available resources. | April 22, 2022 | 
| [Initial publication](#document-revisions) | Whitepaper first published. | December 1, 2018 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.

# Notices
<a name="notices"></a>

 Customers are responsible for making their own independent assessment of the information in this document. This document: (a) is for informational purposes only, (b) represents current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers. 

 © 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. 

# AWS Glossary
<a name="glossary"></a>

For the latest AWS terminology, see the [AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary Reference*.