# AWS Well-Architected User Guide

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
+ [What is AWS Well-Architected?](#well-architected)
   + [What is AWS Well-Architected Framework?](#waf)
   + [AWS Well-Architected glossary](#definitions)
+ [What is AWS Well-Architected Agent (preview)?](#agent)
   + [AWS Well-Architected Agent Concepts and terminology](#agent-concepts)
   + [Getting started with AWS Well-Architected Agent](#agent-getting-started)
      + [API quickstart](#agent-api-quickstart)
      + [Troubleshooting AWS Well-Architected Agent](#agent-troubleshooting)
   + [Agent profiles](#agent-manage-profiles)
      + [Viewing your agent profiles](#agent-view-profiles)
      + [Switching the active agent profile](#agent-switch-profiles)
      + [Updating an agent profile](#agent-update-profile)
      + [Editing goals](#agent-edit-goals)
      + [Updating application context](#agent-update-app-context)
      + [Deleting an agent profile](#agent-delete-profile)
   + [Recommendations](#agent-rec-management)
      + [Filter recommendations in AWS Well-Architected Agent](#agent-filter-rec)
      + [View recommendations in AWS Well-Architected Agent](#agent-view-rec)
      + [Export recommendations in AWS Well-Architected Agent](#agent-export-rec)
      + [Share recommendations in AWS Well-Architected Agent](#agent-share-rec)
      + [Implement recommendations in AWS Well-Architected Agent](#agent-implement-rec)
      + [Prescheduled remediations for recommendations in AWS Well-Architected Agent](#agent-prescheduled-rec)
      + [View archived recommendations in AWS Well-Architected Agent](#agent-rec-history)
      + [Reopen recommendations in AWS Well-Architected Agent](#agent-rec-reopen)
      + [Recommendation refresh and data freshness](#agent-refresh-cadence)
   + [Conducting architecture reviews](#agent-architecture-reviews)
   + [Goals and personalization in AWS Well-Architected Agent](#agent-goals)
   + [AWS Well-Architected Agent Quotas and limits](#agent-quotas)
   + [Related services](#agent-related-services)
+ [What is AWS Well-Architected Tool?](#tool)
   + [Getting started with AWS Well-Architected Tool](#getting-started)
      + [Providing users, groups, or roles access to AWS WA Tool](#iam-auth-access)
      + [Activating support in AWS WA Tool for other AWS services](#activate-integrations)
         + [Activating AppRegistry for a workload](#activate-appregistry)
         + [Activating AWS Trusted Advisor for a workload](#activate-ta-for-workload)
            + [Activating Trusted Advisor for a workload in IAM](#activate-ta-in-iam)
            + [Deactivating Trusted Advisor for a workload](#deactivate-ta-for-workload)
      + [Defining a workload in AWS WA Tool](#define-workload)
      + [Documenting a workload in AWS WA Tool](#start-workflow-review)
      + [Reviewing a workload with AWS Well-Architected Framework](#continue-workflow-review)
      + [Viewing Trusted Advisor checks for your workload](#ta-checks-page)
      + [Saving a milestone for a workload in AWS WA Tool](#save-milestone)
   + [Tutorial: Document an AWS Well-Architected Tool workload](#tutorial)
   + [Well-Architected Framework Review (WAFR)](#wa-framework-review)
      + [Preparing for a WAFR](#preparing-for-a-wafr)
         + [Workload and scope](#workload-and-scope)
         + [People and culture](#people-and-culture)
         + [Documentation and infrastructure](#documentation-and-infrastructure)
      + [Running a WAFR](#running-a-wafr)
      + [Improving your workload](#improving-your-workload)
         + [Identify and understand risks](#identify-and-understand-risks)
         + [Determine prescriptive solutions](#determine-prescriptive-solutions)
         + [Prioritize improvements](#prioritize-improvements)
         + [Implement and track improvements](#implement-and-track-improvements)
   + [Workloads](#workloads)
      + [Define a workload in AWS Well-Architected Tool](#workloads-define)
      + [View a workload in AWS Well-Architected Tool](#workloads-page)
      + [Edit a workload in AWS Well-Architected Tool](#workloads-edit)
      + [Share a workload in AWS Well-Architected Tool](#workloads-sharing)
         + [Considerations when sharing AWS Well-Architected Tool workloads](#sharing-considerations)
         + [Delete shared access in AWS Well-Architected](#sharing-remove)
         + [Modify shared access in AWS Well-Architected](#sharing-change)
         + [Accept and reject workload invitations in AWS Well-Architected](#sharing-invitations)
      + [Delete a workload in AWS Well-Architected Tool](#workloads-delete)
      + [Generate a workload report in AWS Well-Architected Tool](#workloads-report)
      + [View workload details in AWS Well-Architected Tool](#workload-details)
         + [The AWS Well-Architected Tool Overview tab](#details-review)
         + [The AWS Well-Architected Tool Milestones tab](#details-milestones)
         + [The AWS Well-Architected Tool Properties tab](#details-properties)
         + [The AWS Well-Architected Tool Shares tab](#details-permissions)
   + [Using lenses in AWS WA Tool](#lenses)
      + [Adding a lens to a workload in AWS WA Tool](#lenses-add)
      + [Removing a lens from a workload in AWS WA Tool](#lenses-remove)
      + [Viewing lens details for a workload in AWS WA Tool](#lenses-details)
      + [Custom lenses for workloads in AWS WA Tool](#lenses-custom)
         + [Viewing custom lenses in AWS WA Tool](#lenses-viewing)
         + [Creating a custom lens for a workload in AWS WA Tool](#lenses-create)
         + [Previewing a custom lens for a workload in AWS WA Tool](#lenses-preview)
         + [Publishing a custom lens in AWS WA Tool for the first time](#lenses-publish)
         + [Publishing an update to a custom lens in AWS WA Tool](#lenses-publish-update)
         + [Sharing a custom lens in AWS WA Tool](#lenses-sharing)
         + [Adding tags to a custom lens in AWS WA Tool](#lenses-tagging)
         + [Deleting a custom lens in AWS WA Tool](#lenses-deleting)
         + [Lens format specification in AWS WA Tool](#lenses-format-specification)
      + [Lens upgrades in AWS WA Tool](#lens-upgrades)
         + [Determining which lens to upgrade in AWS WA Tool](#lenses-selecting)
         + [Upgrading a lens in AWS WA Tool](#lenses-upgrading)
      + [Lens Catalog for AWS WA Tool](#lens-catalog)
   + [Review templates in AWS WA Tool](#review-templates)
      + [Creating a review template in AWS WA Tool](#creating-a-review-template)
      + [Editing a review template in AWS WA Tool](#editing-review-templates)
      + [Sharing a review template in AWS WA Tool](#sharing-review-templates)
      + [Defining a workload from a template in AWS WA Tool](#define-workload-from-template)
      + [Deleting a review template in AWS WA Tool](#deleting-review-templates)
   + [Tool profiles](#tool-profiles)
      + [Creating a profile](#tool-creating-a-profile)
      + [Editing a profile in AWS WA Tool](#tool-editing-profiles)
      + [Sharing a profile in AWS WA Tool](#tool-sharing-profiles)
      + [Adding a profile to a workload in AWS WA Tool](#tool-adding-profiles-to-workloads)
      + [Removing a profile from a workload in AWS WA Tool](#tool-removing-profiles-from-workloads)
      + [Deleting a profile from AWS WA Tool](#tool-deleting-profiles)
   + [AWS Well-Architected Tool Connector for Jira](#jira)
      + [Setting up the connector](#setting-up-jira)
      + [Configuring the connector](#configuring-jira)
      + [Syncing a workload](#syncing-workload)
      + [Uninstalling the connector](#uninstalling-jira)
   + [Milestones](#milestones)
      + [Saving a milestone](#milestones-save)
      + [Viewing milestones](#milestones-view)
      + [Generating a milestone report](#milestone-report)
   + [Share invitations](#invitations)
   + [Notifications](#notifications)
   + [Dashboard](#dashboard)
      + [Summary](#dashboard-summary)
      + [Well-Architected Framework issues per pillar](#dashboard-issues-per-pillar)
      + [Well-Architected Framework issues per workload](#dashboard-issues-per-workload)
      + [Well-Architected Framework issues by improvement plan item](#dashboard-issues-by-plan-item)
   + [Sharing your AWS WA Tool resources](#sharing)
   + [Tagging your AWS WA Tool resources](#tagging)
   + [EventBridge](#eventbridge)
+ [Security in AWS Well-Architected](#wa-security)
   + [Data protection in AWS Well-Architected](#data-protection)
   + [Compliance validation for AWS Well-Architected](#wat-compliance)
   + [Incident response in AWS Well-Architected](#incident-response)
   + [Resilience in AWS Well-Architected](#disaster-recovery-resiliency)
   + [Infrastructure security in AWS Well-Architected](#infrastructure-security)
   + [Configuration and vulnerability analysis in AWS Well-Architected](#vulnerability-analysis)
   + [Identity and access management for AWS Well-Architected](#security-iam)
      + [AWS Well-Architected Tool access model](#security_iam_service-with-iam)
      + [AWS Well-Architected Agent access model](#security-iam-agent)
      + [AWS Well-Architected identity-based policy examples](#security_iam_id-based-policy-examples)
      + [AWS managed policies for AWS Well-Architected](#security-iam-awsmanpol)
      + [Troubleshooting AWS Well-Architected identity and access](#security_iam_troubleshoot)
   + [Cross-service confused deputy prevention](#cross-service-confused-deputy-prevention)
   + [Logging AWS Well-Architected API calls with AWS CloudTrail](#logging-using-cloudtrail)
+ [API actions](#wa-api-actions)
+ [Release notes](#release-notes)
+ [AWS Glossary](#glossary)

-----



AWS Well-Architected Agent is in preview release and is subject to change.

# What is AWS Well-Architected?
<a name="well-architected"></a>

Last updated: **October 1, 2026** ([Release notes](#release-notes))

 AWS Well-Architected provides two distinct ways to review your cloud architecture: 
+ **AWS Well-Architected Agent:** An AI-powered service that delivers contextual, personalized optimization recommendations based on your specific architecture and business goals. It provides ready-to-use automation scripts and infrastructure as code (IaC) template updates that align with AWS best practices.

  To get started with the AWS Well-Architected Agent, see [What is AWS Well-Architected Agent (preview)?](#agent)
+ **AWS Well-Architected Tool:** A service that provides a consistent process for reviewing and measuring your architecture using the AWS Well-Architected Framework. You can document decisions, identify areas for improvement, and track progress over time using workloads, lenses, and milestones.

  To get started with the AWS Well-Architected Tool, see [What is AWS Well-Architected Tool?](#tool)

The following table summarizes the differences between the two services:


**Comparison of AWS Well-Architected Agent and AWS Well-Architected Tool**  

|  | AWS Well-Architected Agent | AWS Well-Architected Tool | 
| --- | --- | --- | 
| Approach | Automated, AI-powered analysis of your deployed resources and IaC templates. | Manual, guided self-review of your workloads against the AWS Well-Architected Framework. | 
| Primary entity | Profile (defines the accounts, AWS Regions, pillars, and goals to analyze). | Workload (documents a set of components that deliver business value). | 
| Output | Prioritized recommendations with trade-off analysis, automation scripts, and updated IaC templates. | Identified risks (HRIs and MRIs) and an improvement plan based on your review answers. | 
| When to use | Continuous, goal-driven optimization of your environment with ready-to-act remediation. | Structured architecture reviews, governance, and tracking improvements over time with milestones. | 

The two services complement each other, and you can use both at the same time from the AWS Well-Architected console.

## What is AWS Well-Architected Framework?
<a name="waf"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) documents a set of foundational questions that enable you to understand how a specific architecture aligns with cloud best practices. The framework provides a consistent approach for evaluating systems against the qualities that are expected from modern cloud-based systems. Based on the state of your architecture, the framework suggests improvements that you can make to better achieve those qualities.

By using the framework, you learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud. It provides a way for you to consistently measure your architectures against best practices and identify areas for improvement. The framework is based on six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

When designing a workload, you make trade-offs between these pillars based on your business needs. These business decisions help drive your engineering priorities. In development environments, you might optimize to reduce cost at the expense of reliability. In mission-critical solutions, you might optimize reliability and be willing to accept increased costs. In ecommerce solutions, you might prioritize performance, since customer satisfaction can drive increased revenue. Security and operational excellence are generally not traded off against the other pillars.

For much more information on the framework, visit the [AWS Well-Architected website](https://aws.amazon.com/architecture/well-architected/).

## AWS Well-Architected glossary
<a name="definitions"></a>

The following defines common terms used in AWS Well-Architected Tool, AWS Well-Architected Agent, and the AWS Well-Architected Framework.

### AWS Well-Architected Agent terms
<a name="definitions-agent"></a>

**Profile**  
The primary entity that defines the scope, goals, and cross-account configuration for recommendation generation. A profile specifies which AWS accounts to analyze, which AWS Regions to scan, which optimization pillars to focus on, and what business goals to prioritize. Each profile is scoped to a single AWS account and AWS Region.

**Recommendation**  
The output of the AWS Well-Architected Agent analysis system. Each recommendation contains a title, description, impact assessment, trade-offs, guided actions, and remediation steps. A recommendation has a lifecycle with three states: active, completed, and suppressed.

**Recommendation type**  
The scope level of a recommendation. AWS Well-Architected Agent generates three types: Resource (targets a specific AWS resource), Application (spans multiple related resources within a discovered application), and Architecture (generated from IaC template analysis).

**Pillar**  
An optimization dimension that AWS Well-Architected Agent analyzes. The available pillars are: Cost optimization, Security, Resilience, and Performance.

**Goal**  
A natural language business objective associated with a pillar. Goals drive recommendation prioritization and ranking. Each goal consists of a goal statement and a target pillar. For best results, goals should be specific, measurable, and time-bound.

**Execution role**  
An AWS Identity and Access Management role in the profile account that AWS Well-Architected Agent assumes to orchestrate resource discovery across your configured accounts. The execution role must trust the `wellarchitected.amazonaws.com` service principal and have permission to assume access roles in target accounts.

**Access role**  
An IAM role deployed in each target AWS account that you want AWS Well-Architected Agent to analyze. The access role grants AWS Well-Architected Agent read-only permissions to discover and analyze resources in that account.

**Generation**  
The process of producing recommendations. Generation can be proactive (running automatically on a recurring schedule) or on-demand (triggered by you, such as for architecture reviews).

**View**  
A saved filter configuration that controls which recommendations appear when listing. Views filter by pillar, service, goal, account, and region. Views are sharable across users in the same AWS account and do not affect which recommendations are generated.

**Context**  
Additional customer-provided data that informs recommendation generation. Context can include IaC templates, custom best practices (uploaded as CSV), and other supplemental information.

**Remediation**  
Actionable steps to implement a recommendation. Remediation can be SSM Runbook automation (for recommendations derived from AWS Trusted Advisor checks) or guided actions (AI-generated step-by-step instructions for console, AWS CLI, SDK, or IaC implementation).

### AWS Well-Architected Tool terms
<a name="definitions-tool"></a>

**Profile**  
A collection of business-context questions and answers that you attach to workloads. Profiles prioritize the review questions and improvement plan risks that are most relevant to your business. AWS WA Tool profiles are unrelated to AWS WA Agent profiles.

**Workload**  
A set of components that deliver business value. The workload is usually the level of detail that business and technology leaders communicate about. Examples include marketing websites, ecommerce websites, the backend for a mobile app, and analytic platforms. Workloads vary in architectural complexity from a static website to microservices architectures with multiple data stores.

**Milestone**  
A marker for key changes in your architecture as it evolves throughout the product lifecycle: design, testing, go live, and production.

**Lens**  
A way for you to consistently measure your architectures against best practices and identify areas for improvement. In addition to the lenses provided by AWS, you can create and use your own lenses, or use lenses that have been shared with you.

**High risk issue (HRI)**  
An architectural or operational choice that AWS has found might result in significant negative impact to a business. HRIs might affect organizational operations, assets, and individuals.

**Medium risk issue (MRI)**  
An architectural or operational choice that AWS has found might negatively impact business, but to a lesser extent than HRIs.  
For additional information, see [High Risk Issues (HRIs) and Medium Risk Issues (MRIs)](#wat-hri-mri).

# What is AWS Well-Architected Agent (preview)?
<a name="agent"></a>

AWS Well-Architected Agent (AWS WA Agent) is an AI-powered cloud optimization service that continuously analyzes your AWS environment and delivers personalized, prioritized recommendations across cost, security, performance, and resilience. The service generates recommendations at three levels (resource, application, and architecture) with ready-to-deploy automation scripts so you can act immediately.

**Important**  
Application-level recommendations are a new recommendation format currently in beta. We are actively seeking customer feedback to improve their quality and relevance. As with any AI-generated content, please thoroughly review each recommendation before taking any action based on it.

To set up AWS WA Agent and generate your first recommendations, see [Getting started with AWS Well-Architected Agent](#agent-getting-started).

AWS WA Agent is intended for both business leadership and technical teams. By tying recommendations to your stated business goals, it helps leadership and engineering teams align on technical remediation priorities derived from business objectives.

## Key capabilities
<a name="agent-intro-capabilities"></a>
+ **Automated analysis:** Unlike point-in-time architecture reviews, AWS WA Agent analyzes your environment on an ongoing schedule. Scheduled recommendations are refreshed on a weekly cadence.
+ **Ready-to-deploy remediation:** Recommendations include prescriptive guidance and ready-to-implement fixes like updated IaC code, not only findings.
+ **Goal-aligned prioritization:** Recommendations are ranked against the business goals you define. For more information, see [Goals and optimization pillars](#agent-concept-goals).
+ **Cross-pillar impacts:** Every recommendation shows how acting on the recommendation provides positive impact on the other pillars, alongside an impact category.
+  **Trade-off analysis:** Each recommendation describes trade-offs that occur from implementing the recommendation, including pillar, risk level, and mitigation strategy. 
+ **Scale:** A single agent profile can analyze up to 100 AWS accounts and scan resources in all commercial AWS Regions. For limits, see [AWS Well-Architected Agent Quotas and limits](#agent-quotas).
+ **Builds on existing AWS optimization services:** AWS WA Agent ingests findings from services such as AWS Trusted Advisor and adds personalization, goal-aligned prioritization, and automation-ready remediation. This reduces manual triage of optimization findings. For more information, see [Related services](#agent-related-services).

## How it works
<a name="agent-intro-how-it-works"></a>

1. Create an agent profile that defines your accounts, Regions, optimization pillars, and business goals.

1. AWS WA Agent scans the resources in your configured accounts.

1. AWS WA Agent generates prioritized recommendations at the resource, application, and architecture levels.

1. You review recommendations and deploy remediations using the provided guidance.

You can also run architecture reviews of IaC templates on demand. For more information, see [Conducting architecture reviews](#agent-architecture-reviews).

AWS WA Agent analyzes your infrastructure across four optimization pillars: cost optimization, security, resilience, and performance. For more information, see [AWS Well-Architected Agent Concepts and terminology](#agent-concepts).

## Accessing AWS WA Agent
<a name="agent-intro-accessing"></a>
+ **AWS Well-Architected console:** AWS WA Agent is available from the AWS Well-Architected console. For a step-by-step walkthrough of setting up your first agent profile using the console, see [Getting started with AWS Well-Architected Agent](#agent-getting-started).
+ **APIs:** Programmatic access is available through the `wellarchitected` service namespace. For a CLI-based setup walkthrough, see [API quickstart](#agent-api-quickstart). For available operations, see [API actions](#wa-api-actions). For complete API documentation, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).

## Availability
<a name="agent-intro-availability"></a>

**Support plan eligibility:** AWS WA Agent is available to customers with an AWS Support plan at the Business\+ tier or higher: Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations. Customers on Developer or Business tier plans do not have access to AWS WA Agent. For tier-specific entitlements, see [AWS Well-Architected Agent Quotas and limits](#agent-quotas).

**Region availability:** AWS WA Agent profiles are hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon). From these hosting Regions, AWS WA Agent scans resources in all commercial AWS Regions. See [AWS Well-Architected Agent Quotas and limits](#agent-quotas).

## AWS Well-Architected Agent Concepts and terminology
<a name="agent-concepts"></a>

This topic defines the key concepts you need to understand before using AWS Well-Architected Agent.

### Agent profiles
<a name="agent-concept-profiles"></a>

An agent profile is the primary entity in AWS WA Agent. It defines which AWS accounts and Regions the agent monitors, the goals it optimizes for, and details about your applications. AWS WA Agent uses the profile to scan your resources and generate recommendations.

**Note**  
AWS Well-Architected Tool also has a feature named profiles. AWS WA Tool profiles are questionnaires that you attach to workloads to prioritize review questions, and are unrelated to AWS WA Agent profiles. This section describes AWS WA Agent profiles only. For information about AWS WA Tool profiles, see [Tool profiles](#tool-profiles).

When you create a profile, you can create an execution role during the setup process or select an existing one. You create access roles in your workload accounts before or after profile creation, then link them by updating the access role trust policies.

Each profile has the following attributes:
+ A unique name within an AWS account and AWS Region.
+ Business goals that direct the optimization focus.
+ Optimization pillars to analyze.
+ Accounts to scan for resources.

### Execution roles and access roles
<a name="agent-concept-roles"></a>

AWS WA Agent uses two types of IAM roles to discover and analyze resources across your accounts:
+ **Execution role:** An IAM role in the same account as your AWS WA Agent profile. You create this role during profile setup or select an existing one. AWS WA Agent assumes this role to orchestrate resource discovery across your configured accounts. The trust policy allows the `wellarchitected.amazonaws.com` service principal to assume the role.
+ **Access role:** An IAM role that you create in each account you want AWS WA Agent to analyze. The access role is encouraged to use the `WellArchitectedAgentResourceScanning` managed policy, which grants read-only access to resource metadata and configuration. Alternatively, you can scope the access role permissions to only the actions you want AWS WA Agent to perform on your behalf. You update the trust policy on each access role to allow the execution role to assume it.

Neither role grants AWS WA Agent permission to modify your resources. The execution role's only permission is to assume your access roles, and access roles grant read-only access to resource metadata and configuration.

You can use the same role name across all workload accounts (common name pattern) or use different names per account (per-account ARN). During profile creation, you specify which approach you are using.

### Goals and optimization pillars
<a name="agent-concept-goals"></a>

Business goals are plain-text statements that guide how AWS WA Agent prioritizes and ranks recommendations. You add goals during profile creation and can modify them at any time afterward. Each goal is associated with one optimization pillar.

AWS WA Agent analyzes your infrastructure across four optimization pillars:
+ Cost optimization
+ Security
+ Resilience
+ Performance

### Application context
<a name="agent-concept-app-context"></a>

Application context provides AWS WA Agent with additional information about your workloads so that it can generate more relevant, personalized recommendations. You add application context after your profile is created.

Application context includes the following:
+ Application overview
+ Accounts and Regions
+ Tags (key-value pairs to scope resource discovery)
+ Services and resource types. Some resource types are not supported. For more information, see [Unsupported resource types](#agent-unsupported-resources).
+ Industry
+ Application type (`SAS`, `DESKTOP_APPLICATION`, or `OTHER`)
+ Criticality level (`TEST_DEVELOPMENT`, `NON_CRITICAL`, `MISSION_CRITICAL`, or `BUSINESS_CRITICAL`)
+ Architecture overview (plain text)
+ Additional context (plain text)

### Recommendation types
<a name="agent-concept-rec-types"></a>

AWS WA Agent generates three types of recommendations:
+ **Resource:** Targets a specific resource such as an Amazon EC2 instance, Lambda function, or Amazon RDS database. Identifies optimization opportunities at the individual resource level.
+ **Application:** Spans multiple related resources within a discovered application. Considers how resources interact and provides guidance that accounts for relationships between components.
+ **Architecture:** Generated from IaC template analysis. Upload your CloudFormation, Terraform, or AWS CDK templates and receive recommendations aligned to AWS Well-Architected best practices, along with deployment-ready updated templates.

### Architecture reviews
<a name="agent-concept-arch-reviews"></a>

Architecture reviews are on-demand analyses of your Infrastructure as Code (IaC) projects against the AWS Well-Architected Framework. You provide an Amazon S3 URI pointing to your IaC files or upload a single document directly through the console. Select which pillars to review, and AWS WA Agent returns architecture-type recommendations with updated templates.

Architecture reviews differ from resource and application recommendations in that they target templates before deployment, enabling you to identify issues before they reach production.

## Getting started with AWS Well-Architected Agent
<a name="agent-getting-started"></a>

To use AWS Well-Architected Agent, you create an agent profile that defines the scope of your infrastructure analysis. Creating an agent profile is the onboarding step. You need a profile before you can view recommendations, conduct architecture reviews, or use any other AWS WA Agent feature.

**Tip**  
Baseline recommendations from AWS Trusted Advisor are available without creating a profile. To receive personalized, goal-aligned recommendations with cross-pillar trade-off analysis, complete the following setup steps.

The setup process uses two AWS services:
+ **AWS Well-Architected** (Well-Architected console): Create your agent profile, configure accounts, pillars, goals, and application context.
+ **IAM**: Create access roles in your workload accounts and update trust policies to establish cross-account access.

This page describes the console-based setup. To set up AWS WA Agent using the AWS CLI instead, see [API quickstart](#agent-api-quickstart).

 Once a profile is created and properly configured, AWS WA Agent begins generating scheduled recommendations within 48 hours. For more information on scheduled recommendations and recommendation types, see [Recommendations](#agent-rec-management). 

### Prerequisites
<a name="agent-prerequisites"></a>
+ You have an active AWS Support plan at the Business\+ tier or higher (Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations). Developer and Business tier customers do not have access to AWS WA Agent. For tier-specific entitlements, see [AWS Well-Architected Agent Quotas and limits](#agent-quotas).
+ **(Optional)** You have enabled AWS Cost Explorer in your account for accurate cost data. There are two separate features to check to fully enable Cost Explorer for AWS WA Agent:
  +  Enable the main AWS Cost Explorer service. 
  +  In **Cost Management Preferences** in the Cost Explorer sidebar, under **Granular data**, select the **Resource-level data at daily granularity** checkbox. 
**Note**  
 Without Cost Explorer enabled, AWS WA Agent estimates costs from public AWS pricing. 
+ You have the IAM permissions required to create a AWS WA Agent profile, including permissions to create IAM roles (`iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`) and AWS WA Agent actions (`wellarchitected:CreateAgentProfile`). For more information about the AWS WA Agent access model, see [AWS Well-Architected Agent access model](#security-iam-agent).
+ You have identified the AWS account IDs that you want AWS WA Agent to analyze (maximum 100 accounts).
+ You have defined your business goals and selected the optimization pillars you want to focus on.

### Step 1: Create an agent profile
<a name="agent-create-profile"></a>

Create an agent profile from the AWS WA Agent console. During profile creation, you can create an execution role or select an existing one.

**To create an agent profile**

1. Open the AWS Management Console and navigate to AWS Well-Architected.

1. Open the AWS WA Agent console.

1. Choose **Agent profiles** in the left-hand navigation.

1. In the top right corner, choose **Add profile**.

1. Enter a profile name between 3 and 128 characters. Use only letters, numbers, hyphens (-), and underscores (\_). For example, `product-backend-team`.

1. Enter a description for the profile.

1. Under **Select accounts & regions**, select AWS Regions to monitor and analyze.

1. Under **Accounts to monitor**, enter account IDs separated by commas (up to 100 accounts).

1.  Then, under **Common access role name**, enter the access role name to use across all accounts in the profile. The recommended name is `AccessRoleForWellArchitectedAgent`. 
**Note**  
 Whether you create your own access role name or use the recommended one, you must use that exact same access role name across all accounts in the profile. This only applies to the console onboarding experience. 

### Step 2: Add goals and optimization pillars
<a name="agent-goals-pillars"></a>

During profile creation, configure the following in **Optimization pillars**:
+ **Optimization pillar:** Select at least one pillar for AWS WA Agent to analyze: Cost optimization, Security, Resilience, or Performance.
+ **Goal statement:** Enter at least one plain-text goal statement. Each profile requires a minimum of one goal for AWS WA Agent to generate prioritized recommendations. Goals are editable at any time after creation. For guidance on writing effective goals, see [Goals and personalization in AWS Well-Architected Agent](#agent-goals).

### Step 3: Configure permissions and integrations
<a name="agent-permissions-integrations"></a>

After configuring pillars, under **Permissions and Integrations**, you can either select an existing execution role or create a new one.

The execution role is an IAM role in your profile account that AWS WA Agent assumes to orchestrate resource discovery. The execution role chains to the access roles in your workload accounts. When you choose **Create new role**, the console creates the IAM execution role for you automatically, applying the required trust policy and permissions policy. You do not need to navigate to the IAM console separately.

**To create a new execution role**

1. Choose **Create new role**.

1. The console pre-populates the **Role name** field with `ExecutionRoleForWellArchitectedAgent`. We recommend using this default name.

1. (Optional) To review the trust policy and permissions policy the console will apply, choose **View trust policy**.

1. Choose **Create role**.

1. Determine whether to enable or disable Termination protection. It is recommended to enable this feature to avoid accidental profile deletion.

If you do not want to enable AWS Cost Explorer, choose **Get started** to finish creating your profile. After the profile is created, complete the remaining setup. To enable cross-account discovery, you must create access roles in your workload accounts, as described in [Step 6: Create access roles in your workload accounts](#agent-access-roles).

If you want to enable Cost Explorer, go to [(Optional) Step 4: Enable AWS Cost Explorer](#agent-cost-explorer) before finishing profile creation.

### (Optional) Step 4: Enable AWS Cost Explorer
<a name="agent-cost-explorer"></a>

**Note**  
Enabling AWS Cost Explorer is an optional step to enhance the specificity of cost data. Cost Explorer is enabled at the AWS account level, not per AWS WA Agent profile. If you enable Cost Explorer in your organization's management account, all member accounts are also granted access.   
 After you enable Cost Explorer, it cannot be disabled, though the optional granular data preferences (resource-level data) can be changed at any time.

To use real-time, accurate cost data and resources from your accounts, you can enable AWS Cost Explorer.

 With Cost Explorer and hourly and [resource-level data at daily granularity](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-resource-daily.html) both enabled, AWS WA Agent can provide recommendations and optimizations with your exact cost data.

Without Cost Explorer enabled, AWS WA Agent estimates costs based on public AWS pricing.

There is no charge for using the Cost Explorer console. Charges apply for Cost Explorer API requests and for the resource-level granular data preferences. Resource-level cost attribution in AWS WA Agent recommendations requires the granular data preferences. To estimate these charges, see [AWS Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/).

To get started with Cost Explorer in your AWS WA Agent profile, choose **Open Cost Explorer**, then configure Cost Explorer for your AWS account. For more detail, see [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html).

 After enabling Cost Explorer, it can take up to 24 hours for the data to be available to AWS WA Agent, and resource-level data at daily granularity can take up to 48 hours to propogate. 

### Step 5: Add application context
<a name="agent-app-context"></a>

After your profile is created, add application context to help AWS WA Agent generate more relevant recommendations. Application context provides details about your workloads that AWS WA Agent cannot discover automatically.

**Important**  
At least one application context is required per profile for AWS WA Agent to generate scheduled recommendations. Without application context, your profile is flagged as invalid and scheduled recommendation generation does not run.

**To add application context to a profile**

1.  In the left-hand navigation, choose **Agent profiles**. 

1.  In the profile you already created, choose **Profile Details**. 

1.  Select the **Application context** tab. 

1.  Choose **Add application context**. 

1.  Enter details on your application context, including Application name, overview, accounts in the application, AWS Regions, and tags. For a full overview of adding or updating application context, see [Updating application context](#agent-update-app-context). 

1. After filling in your application context, choose **Add application**.

### Step 6: Create access roles in your workload accounts
<a name="agent-access-roles"></a>

After you create your profile, create an IAM access role in each AWS account that you selected to monitor. Access roles allow AWS WA Agent to discover and analyze resources in those accounts.

When profile creation finishes, the create-profile page shows an **Action required** prompt indicating that the selected accounts still need an access role. Creating these roles is a separate task that you perform manually in the IAM console. The console does not create the roles for you, and it does not open the IAM console automatically. AWS WA Agent does not monitor or analyze an account until that account's access role exists.

The role name must match the **Common access role name** that you entered during profile creation. The recommended name is `AccessRoleForWellArchitectedAgent`.

The execution role's permissions policy grants `sts:AssumeRole` on the access roles, and each access role's trust policy allows the execution role to assume it. Use the same role name in every workload account.

Use the following trust policy template for your access roles. {{ProfileOwningAccountId}} is the account where you created the agent profile. {{ExecutionRoleName}} is the name of the execution role in the agent profile. By default, this is usually `ExecutionRoleForWellArchitectedAgent`.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{ProfileOwningAccountId}}:role/service-role/{{ExecutionRoleName}}"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Important**  
The execution role ARN format depends on how the role was created:  
If you used the **Create new role** button in [Step 3: Configure permissions and integrations](#agent-permissions-integrations), the console places the role under the `service-role/` path: `arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent`
If you created the execution role manually in IAM beforehand and selected it during profile creation, use the ARN without the `service-role/` prefix: `arn:aws:iam::{{111122223333}}:role/ExecutionRoleForWellArchitectedAgent`

**To create an access role**

1. Open the IAM console in the workload account.

1. In the left-hand navigation, choose **Roles**, then choose **Create role**.

1. For **Trusted entity type**, choose **Custom trust policy**.

1. Paste the trust policy shown in the preceding template, and substitute the required information.

1. Choose **Next**. On the **Add permissions** page, search for and attach the [`WellArchitectedAgentResourceScanning` managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html). This grants read-only access to resource metadata and configuration.

1. Choose **Next**. Enter the role name (it must match the **Common access role name** from profile creation - we recommend `AccessRoleForWellArchitectedAgent`) and choose **Create role**. Use the same name in every workload account.

**Note**  
If you already created access roles with a broader trust policy, edit each role's **Trust relationships** tab to use the trust policy shown in the preceding template.

Repeat this procedure in each workload account you want AWS WA Agent to analyze. For more information about the AWS WA Agent access model and role chain, see [AWS Well-Architected Agent access model](#security-iam-agent).

### Next steps
<a name="agent-next-steps"></a>

After you complete your profile setup, you can:
+ View your personalized recommendations in the AWS WA Agent dashboard ([Recommendations](#agent-rec-management)). Scheduled recommendations typically become available within 24 hours of completing profile setup.
+ Conduct an architecture review by uploading your IaC files ([Conducting architecture reviews](#agent-architecture-reviews)).
+ Manage your profile settings at any time ([Agent profiles](#agent-manage-profiles)).

### API quickstart
<a name="agent-api-quickstart"></a>

You can set up AWS WA Agent entirely through the AWS CLI or SDK instead of the console. This quickstart walks through creating a profile, adding a goal, adding application context, and verifying eligibility.

**Note**  
Before using the API, create the execution role and access roles as described in [Step 3: Configure permissions and integrations](#agent-permissions-integrations) and [Step 6: Create access roles in your workload accounts](#agent-access-roles). The API does not create IAM roles for you.

#### Step 1: Create an agent profile
<a name="agent-api-create-profile"></a>

Create a profile with your execution role, target pillars, and account configuration.

**To create an agent profile (CLI)**

1. Run the following command. Replace the placeholder values with your account IDs, role ARNs, and target Regions.
**Note**  
 You can choose a common access role name or enter an access role name per account. This is only available in the API version of onboarding, not in the console. 

   ```
   aws wellarchitected create-agent-profile \
       --name "my-production-profile" \
       --execution-role-arn "arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent" \
       --pillars COST_OPTIMIZATION SECURITY RESILIENCE PERFORMANCE \
       --aggregation-configuration '[{"accountId":"{{444455556666}}","accessRoleArn":"arn:aws:iam::{{444455556666}}:role/AccessRoleForWellArchitectedAgent","regions":["us-east-1","us-west-2"]}]'
   ```

1. In the response, note the profile ARN. You will use this value in subsequent commands.

#### Step 2: Add an optimization goal
<a name="agent-api-create-goal"></a>

Add a goal to drive recommendation prioritization. Each goal is associated with one or more optimization pillars.

**To add a goal (CLI)**
+ Run the following command. Replace the profile ARN with the value from Step 1.

  ```
  aws wellarchitected create-agent-goal \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
      --title "Reduce EC2 spend by 20% by Q4 through rightsizing and Reserved Instance coverage" \
      --pillars COST_OPTIMIZATION
  ```

#### Step 3: Add application context
<a name="agent-api-create-context"></a>

Provide application metadata so AWS WA Agent can generate more relevant, personalized recommendations.

**To add application context (CLI)**
+ Run the following command. Replace the profile ARN and content fields with your application details.

  ```
  aws wellarchitected create-agent-context \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
      --title "Payment processing service" \
      --context-type APPLICATION \
      --content '{"applicationOverview":"Real-time payment processing","criticality":"MISSION_CRITICAL","accountIds":["{{444455556666}}"],"regions":["us-east-1"]}'
  ```

#### Step 4: Verify profile eligibility
<a name="agent-api-verify-eligibility"></a>

Check that your profile is valid and eligible for recommendation generation.

**To verify eligibility (CLI)**

1. Run the following command:

   ```
   aws wellarchitected get-agent-profile \
       --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-production-profile}}" \
       --query '{eligible: eligibleForScheduledGeneration, errors: fieldErrors}'
   ```

1. If `eligibleForScheduledGeneration` is `true`, your profile is properly configured. Scheduled recommendations will begin generating within 48 hours.

1. If `eligibleForScheduledGeneration` is `false`, check the `fieldErrors` map for specific issues. See [Troubleshooting AWS Well-Architected Agent](#agent-troubleshooting) for common resolutions.

For the complete API reference, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).

### Troubleshooting AWS Well-Architected Agent
<a name="agent-troubleshooting"></a>

This section provides solutions to common issues you may encounter when setting up and using AWS Well-Architected Agent.

#### Profile shows eligibleForScheduledGeneration: false
<a name="agent-ts-not-eligible"></a>

**Possible causes and solutions:**
+ **Missing application context:** At least one application context is required per profile. Navigate to **Profile Details**, choose the **Application context** tab, and add an application.
+ **No pillars selected:** Your profile must have at least one optimization pillar. Edit the profile and select one or more pillars.
+ **Access role trust policy not configured:** The access roles in your workload accounts must trust the execution role. Complete [Step 6: Create access roles in your workload accounts](#agent-access-roles) and confirm the execution role ARN format is correct.
+ **Execution role does not exist or lacks permissions:** Verify the execution role ARN in your profile details page exists in IAM and has a permissions policy allowing `sts:AssumeRole` on your access roles.
+ **No accounts configured:** Your aggregation configuration must include at least one account. Edit the profile and add accounts to monitor.

To identify the specific issue, call `GetAgentProfile` and check the `fieldErrors` map in the response.

#### Cross-account role configuration errors
<a name="agent-ts-trust-policy"></a>

**Possible causes and solutions:**
+ **Missing service-role/ path prefix:** If you created the execution role using the **Create new role** button in the AWS WA Agent console, the role is placed under the `service-role/` path. Use `arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent`, not `arn:aws:iam::{{111122223333}}:role/ExecutionRoleForWellArchitectedAgent`. Confirm the exact ARN from your profile details page.
+ **Wrong account ID in trust policy:** The Principal ARN must reference the account where your AWS WA Agent profile is created (the profile-owning account), not the workload account.
+ **Trust policy not applied to all accounts:** Each workload account in your aggregation configuration needs its own access role with the trust policy. Verify every account listed in your profile has a correctly configured access role.
+ **Execution role missing `sts:AssumeRole` permission:** The execution role in your profile account must have a permissions policy that allows `sts:AssumeRole` on your access roles. Verify the execution role's permissions policy includes an `sts:AssumeRole` action with the access role ARNs as resources. If you created the execution role through the AWS WA Agent console, the permissions policy must specify an access role name (for example, `AccessRoleForWellArchitectedAgent`) and cannot use wildcard (`*`) resources.

#### No recommendations after 48 hours
<a name="agent-ts-no-recs"></a>

**Possible causes and solutions:**
+ **Profile not eligible:** Call `GetAgentProfile` and confirm `eligibleForScheduledGeneration` is `true`. If `false`, resolve the `fieldErrors` first.
+ **Missing application context:** At least one application context is required. Check the **Application context** tab in your profile details.
+ **Access role permissions insufficient:** Verify the [`WellArchitectedAgentResourceScanning`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) managed policy is attached to each access role.
+ **Recently created profile:** Scheduled recommendations can take up to 48 hours after profile setup is complete. If less than 48 hours have elapsed, wait for the next generation cycle.

#### ServiceQuotaExceededException during profile creation
<a name="agent-ts-quota-exceeded"></a>

**Possible causes and solutions:**
+ **Maximum profiles reached:** You have reached the maximum number of agent profiles for your support plan tier. See [AWS Well-Architected Agent Quotas and limits](#agent-quotas) for tier-specific limits. Delete an unused profile or upgrade your support plan tier.

## Agent profiles
<a name="agent-manage-profiles"></a>

After you create an agent profile, you can manage it from the AWS WA Agent console in **Agent profiles**. You can update goals, pillars, accounts, and application context at any time. If you have multiple profiles, you can switch between them to view profile-scoped recommendations and reviews.

**Note**  
This section describes how to manage existing agent profiles. If you have not created an agent profile yet, see [Step 1: Create an agent profile](#agent-create-profile) in the **Getting started** section for instructions.

You can also manage profiles programmatically using the AWS CLI or SDK. For the complete list of operations, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).

**Topics**
+ [Viewing your agent profiles](#agent-view-profiles)
+ [Switching the active agent profile](#agent-switch-profiles)
+ [Updating an agent profile](#agent-update-profile)
+ [Editing goals](#agent-edit-goals)
+ [Updating application context](#agent-update-app-context)
+ [Deleting an agent profile](#agent-delete-profile)

### Viewing your agent profiles
<a name="agent-view-profiles"></a>

#### Console
<a name="agent-view-profiles-console"></a>

To view a list of your profiles, choose **Agent profiles** in the left-hand navigation.

This view lists all of your configured AWS WA Agent profiles, along with action required notices for misconfigured profiles. From this page, you can:
+ Choose **Go to Dashboard** to view recommendations for a profile.
+ Choose **See profile details** to view the profile details page.
+ Choose **Actions** to edit the profile, copy the profile ARN, or delete the profile.

The profile details page displays:
+ **Profile summary:** Host account, goals, accounts in the profile, AWS Regions, optimization pillars, applications, termination protection status, and a copiable **Execution role ARN** for the profile.
+ **Next steps (optional):** Provides optional next steps for the profile when the particular actions haven't been taken. You can choose **Provide profile access to team members** to share a profile with team members, or choose **Create applications with context** to define application context in the profile.

The profile details page has four tabs:
+ **Accounts in profile:** Lists accounts configured for the profile. You can edit accounts and filter by Region.
+ **Profile Access:** Shows AWS accounts with access to this profile and their access level (read or read/write). You can provide access to additional accounts or remove access.
+  **Applications:** Lists application contexts defined for the profile. You can add, edit, or delete application contexts, and search or filter by Region. 
+ **Schedule** Displays your chosen refresh schedule for how often AWS WA Agent generates scheduled recommendations. You can also update your refresh schedule here by choosing a new schedule period, and then choosing **Save**.

#### CLI
<a name="agent-view-profiles-cli"></a>

To list all agent profiles in your account:

```
aws wellarchitected list-agent-profiles
```

To view details for a specific profile:

```
aws wellarchitected get-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

### Switching the active agent profile
<a name="agent-switch-profiles"></a>

In the AWS WA Agent **Dashboard**, recommendations are shown for only the current profile.

You can switch the active profile using the **Profile** dropdown at the top of the dashboard.

### Updating an agent profile
<a name="agent-update-profile"></a>

You can update a profile's display name, description, pillars, execution role, aggregation configuration, deletion protection, and business overview at any time.

#### Console
<a name="agent-update-profile-console"></a>

**To update a profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Edit profile**.

1. Update the fields you want to change.

1. Choose **Save**.

#### CLI
<a name="agent-update-profile-cli"></a>

**Important**  
When you update a profile using the API or CLI (`UpdateAgentProfile`), you must specify all fields in the request, not only the fields you want to change. Any field omitted from the update request is reset to its default value or cleared. The update operation uses full replacement semantics (PUT), not partial update semantics (PATCH). The console handles this automatically by pre-populating all current values.

To avoid unintentionally clearing fields, retrieve the current profile configuration first, modify the values you want to change, then pass the full object back:

```
# 1. Get the current profile configuration
aws wellarchitected get-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"

# 2. Update the profile with all fields specified
aws wellarchitected update-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --display-name "{{My Profile}}" \
    --description "{{Profile description}}" \
    --pillars COST_OPTIMIZATION SECURITY \
    --execution-role-arn "{{arn:aws:iam::111122223333:role/MyExecutionRole}}" \
    --aggregation-configuration '{{[{"accountId":"111122223333","regions":["us-east-1"],"accessRoleArn":"arn:aws:iam::111122223333:role/MyRole"}]}}' \
    --deletion-protection \
    --business-overview "{{Overview of the business context}}"
```

### Editing goals
<a name="agent-edit-goals"></a>

**Important**  
Each profile requires at least one goal. If you delete all goals from a profile, scheduled recommendations are not generated until you add a new goal.

#### Console
<a name="agent-edit-goals-console"></a>

Goals can be added either in **Agent profiles** or in the **Dashboard** for the profile.

**To add goals from the profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions**, then **Edit profile**.

1. In **Optimization pillars**, enter a free text goal statement for each optimization pillar you are reviewing.
**Note**  
Concrete, specific goals help AWS WA Agent prioritize and recommend actions. For example, "optimize costs" is vague, while "optimize cost of X and Y AWS service by 15%" is specific and measurable.

1. After entering goals, choose **Save**.

**To add goals from the dashboard**

1. Choose **Dashboard** in the left-hand navigation.

1. Verify that you have the correct profile selected under **Profile**.

1. On the right side of the screen, choose the **pencil icon** in **Your goals**.

1. Enter, update, or remove **Optimization pillars** and **Goal statements**.

1. Choose **Save**.

#### CLI
<a name="agent-edit-goals-cli"></a>

To create a new goal:

```
aws wellarchitected create-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --title "{{Reduce EC2 spend by 20%}}" \
    --pillars COST_OPTIMIZATION
```

To update an existing goal:

```
aws wellarchitected update-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --goal-id "{{goal-id}}" \
    --title "{{Updated goal statement}}"
```

To delete a goal:

```
aws wellarchitected delete-agent-goal \
    --profile-arn "{{profile-arn}}" \
    --goal-id "{{goal-id}}"
```

### Updating application context
<a name="agent-update-app-context"></a>

Application context tells AWS WA Agent what your applications are, what they do, and what infrastructure they run on. AWS WA Agent uses this information to scope recommendations to the resources that belong to each application and to personalize guidance based on your architecture, criticality, and constraints.

The more context you provide, the more targeted your recommendations become. A profile with application overviews, architecture descriptions, criticality levels, and resource tags produces recommendations that account for your specific environment and priorities as opposed to generic recommendations.

**Important**  
You must have at least one application context defined per profile to generate scheduled recommendations.

Follow these guidelines when defining application context:
+ Create one context entry per logical application, not per resource or per team. For example, if you have an order processing system that spans multiple services, define it as a single application context.
+ Set the criticality level. It directly affects recommendation prioritization. Mission-critical applications receive higher-priority findings than test or development workloads.
+ Use resource tags to scope your applications. If multiple applications share the same accounts, tags are how AWS WA Agent distinguishes which resources belong to which application.

#### Console
<a name="agent-update-app-context-console"></a>

**To add application context**

1. Choose **Agent profiles** in the left-hand navigation. Then, on the profile to add the application context, choose **Profile Details**.

1. Select the **Application context** tab. Then, choose **Add application context**.

1. Enter details for the application. For additional customization, expand the **Additional details** dropdown.

   Application context includes the following fields:
   + **Application name:** Name of your application.
   + **Application overview:** Overview of what your application does.
   + **Accounts in this application:** Any AWS accounts this application includes or uses.
   + **Regions:** AWS Regions where this application resides or operates in.
   + **Tags:** Key value pairs included in this application. Tags have two different filtering behaviors depending on what's selected:
     +  **Only the tag is selected:** Includes every resource carrying that tag (and any type of tag) within the selected AWS accounts or AWS Regions.
     +  **Tag selected with services or resource types:** Displays the intersection of the tag with the services or resources. All resources returned in the filter must have that selected tag and be a part of one of the selected services or resource types. 
   + **Additional details:**
     + **Services:** Which services your application uses. Selecting a service automatically selects all of its associated resources.
**Note**  
 When adding or updating a service in an application context, use the CloudFormation canonical service name. For example, for `AWS::DynamoDB::Table CloudFormation`, the service name is `DynamoDB`. 
     + **Resources:** Additional resources your application uses outside of the ones auto-included by the service dropdown. Some resource types are not supported. For more information, see [Unsupported resource types](#agent-unsupported-resources).
     + **Industry:** What industry your application serves.
     + **Type:** The type of application.
     + **Criticality:** How critical this application is to your organization.
     + **Architecture overview:** Plain-text overview of your architecture.
     + **Additional context:** Any further context you want AWS WA Agent to consider during reviews and recommendations.

1. After entering your context, choose **Add application**. You will see the new application context in the **All applications** list.

1. After adding application context, it can take up to 24 hours to generate scheduled recommendations based on this new context.

#### CLI
<a name="agent-update-app-context-cli"></a>

To add application context:

```
aws wellarchitected create-agent-context \
    --profile-arn "{{profile-arn}}" \
    --title "{{My application}}" \
    --context-type APPLICATION \
    --content '{"applicationOverview":"{{Description}}","criticality":"{{MISSION_CRITICAL}}"}'
```

**Note**  
 When adding or updating a service in an application context, use the CloudFormation canonical service name. For example, for `AWS::DynamoDB::Table CloudFormation`, the service name is `DynamoDB`. 

To update existing application context:

```
aws wellarchitected update-agent-context \
    --profile-arn "{{profile-arn}}" \
    --context-id "{{context-id}}" \
    --title "{{Updated application name}}" \
    --content '{"applicationOverview":"{{Updated description}}"}'
```

To delete application context:

```
aws wellarchitected delete-agent-context \
    --profile-arn "{{profile-arn}}" \
    --context-id "{{context-id}}"
```

### Deleting an agent profile
<a name="agent-delete-profile"></a>

**Important**  
 Deleting an agent profile also deletes all goals, application contexts, and recommendations in the profile. Before deleting, verify that you have saved any information you may need from the profile. 

#### Console
<a name="agent-delete-profile-console"></a>

**To delete a profile**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Delete profile**.

1. Confirm the deletion.

If the **Delete profile** option is unavailable (grayed out), termination protection is enabled on the profile. Disable it first:

**To disable termination protection**

1. Choose **Agent profiles** in the left-hand navigation.

1. Choose **Actions** on the profile, then **Edit profile**.

1. In **Permissions and Integrations**, disable the **Termination protection** toggle.

1. Choose **Save**.

After disabling termination protection, return to **Agent profiles** and delete the profile using **Actions**, **Delete profile**.

#### CLI
<a name="agent-delete-profile-cli"></a>

To delete a profile:

```
aws wellarchitected delete-agent-profile \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

**Note**  
If deletion protection is enabled, you must first disable it using `UpdateAgentProfile` with `--deletion-protection false` before deleting the profile.

## Recommendations
<a name="agent-rec-management"></a>

AWS Well-Architected Agent provides personalized recommendations in the AWS WA Agent dashboard to help you optimize your AWS infrastructure costs, improve performance, and enhance security. Recommendations are based on your goals and generated by analyzing your AWS environment across multiple data sources. You can view, filter, export, share, and implement recommendations.

The AWS WA Agent dashboard displays three types of recommendations:
+ **Resource:** Targets a specific resource such as an Amazon EC2 instance, Lambda function, or Amazon RDS database. Resource-level recommendations address optimization opportunities at the individual resource level.
+ **Application:** Spans multiple related resources within a discovered application. Application-level recommendations consider how resources interact and provide guidance that accounts for relationships between components.
+ **Architecture:** Generated from IaC template analysis. These recommendations target your infrastructure design before deployment and include updated templates with best-practice fixes applied.

 AWS WA Agent provides both scheduled and manual recommendations. Application- and resource-level recommendations occur in the scheduled recommendations, which are generated roughly every 7 days. Architecture recommendations are only provided through the manual architecture review process. 

**Important**  
Application-level recommendations are a new recommendation format currently in beta. We are actively seeking customer feedback to improve their quality and relevance. As with any AI-generated content, please thoroughly review each recommendation before taking any action based on it.

**Note**  
To generate Architecture type recommendations, choose **Architecture review** in the left-hand navigation. For more information, see [Conducting architecture reviews](#agent-architecture-reviews). 

The AWS WA Agent dashboard presents recommendations in the following categories:
+ **High priority recommendations:** Dynamically ranked recommendations based on your goals and potential impact.
+ **All recommendations:** A complete list of cloud optimization recommendations.
+ **Reviews:** Status updates and information on architecture reviews.

**Topics**
+ [Filter recommendations in AWS Well-Architected Agent](#agent-filter-rec)
+ [View recommendations in AWS Well-Architected Agent](#agent-view-rec)
+ [Export recommendations in AWS Well-Architected Agent](#agent-export-rec)
+ [Share recommendations in AWS Well-Architected Agent](#agent-share-rec)
+ [Implement recommendations in AWS Well-Architected Agent](#agent-implement-rec)
+ [Prescheduled remediations for recommendations in AWS Well-Architected Agent](#agent-prescheduled-rec)
+ [View archived recommendations in AWS Well-Architected Agent](#agent-rec-history)
+ [Reopen recommendations in AWS Well-Architected Agent](#agent-rec-reopen)
+ [Recommendation refresh and data freshness](#agent-refresh-cadence)

### Filter recommendations in AWS Well-Architected Agent
<a name="agent-filter-rec"></a>

Use filters to narrow down recommendations based on specific criteria to focus on the most relevant optimizations for your environment and priorities.

#### Console
<a name="agent-filter-rec-console"></a>

The Filters panel on the left side of the dashboard allows you to refine recommendations by:
+ **Type:** Application, Architecture, or Resource-level recommendations
+ **Pillars:** Cost Optimization, Security, Resilience, or Performance
+ **Effort:** Small, Medium, or Large effort to fix
+ **Impact:** High, Medium, or Low impact fixes
+ **Services:** Select services from the list

You can select multiple filter criteria simultaneously. The **Clear filters** button removes all applied filters to return to the full recommendations view.

You can use the search bar to find a specific recommendation using keywords or recommendation names.

#### CLI
<a name="agent-filter-rec-cli"></a>

To filter recommendations by state (open or closed):

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --state OPEN
```

To filter by pillar:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --pillar COST_OPTIMIZATION
```

### View recommendations in AWS Well-Architected Agent
<a name="agent-view-rec"></a>

#### Console
<a name="agent-view-rec-console"></a>

When you select a recommendation from the AWS WA Agent dashboard, the recommendation detail page displays the full context needed to evaluate and act on it.

The detail page includes the following sections:
+ **Overview:** A summary of what was detected and the recommended action.
+ **Details:** Metadata including priority, pillar, source (for example, Trusted Advisor), fix effort, detection date, and the number of affected resources.
+ **Insights:** Explains why this recommendation was generated. Includes a plain-language insight statement and the signals detected in your environment that triggered it. Signals reference specific resource ARNs and configuration states.
+ **Impact:** The pillar-specific impact of acting on this recommendation, including cross-pillar impacts and trade-offs. For example, a cost optimization recommendation may also improve performance while maintaining security. Impacts include quantified estimates where available (for example, "Up to 99% KMS cost reduction").
+ **Recommended fix:** A high-level summary of the remediation steps before you enter the guided workflow.
+ **Affected resources:** A table listing each resource targeted by this recommendation, including the ARN, service, account, and Region. You can search and filter by service, account, or Region. Choosing a resource ARN navigates you to that resource in the AWS console (for example, selecting an S3 bucket ARN opens that bucket in the Amazon S3 console).

##### Cross-pillar impacts
<a name="agent-cross-pillar-impacts"></a>

Choose **Cross-pillar impacts** to view how this recommendation positively affects other optimization pillars beyond the primary pillar. The badge shows the total number of impacts (for example, "Cross-pillar impacts (4)").

Each cross-pillar impact includes:
+ **Impact description:** What the cross-pillar benefit is and why it occurs.
+ **Pillar:** The affected pillar (Cost Optimization, Security, Resilience, or Performance).
+ **Impact category:** The severity of the positive impact (High, Medium, or Low).

For example, enabling S3 Bucket Keys for cost optimization also reduces KMS API latency (Performance, High), improves resilience against KMS rate limiting (Resilience, Medium), and simplifies encryption audit trails (Security, Medium).

##### Trade-offs
<a name="agent-trade-offs"></a>

Choose **Trade-offs** to view potential risks and considerations before implementing the recommendation. The badge shows the total number of trade-offs (for example, "Trade-offs (3)").

Each trade-off includes:
+ **Trade-off:** A title describing the potential risk.
+ **Description:** A detailed explanation of the trade-off and when it applies.
+ **Mitigation strategy:** Specific guidance for reducing or eliminating the risk.
+ **Pillar:** The pillar most affected by this trade-off.
+ **Risk:** The overall risk level of this trade-off.

Review all trade-offs and their mitigation strategies before beginning remediation. Trade-offs help you make informed decisions about whether to implement a recommendation as-is, implement with mitigations, or defer the recommendation.

##### Recommendation actions
<a name="agent-rec-actions"></a>

The **Actions** dropdown on the recommendation detail page provides the following options:
+ **Share recommendation:** Share the recommendation with other AWS accounts. Enter a comma-separated list of account IDs (up to 100 accounts) and select an access level:
  + **Read only:** Recipients can view the recommendation but cannot take actions on it.
  + **Read/write:** Recipients can view the recommendation and take actions such as starting remediation or marking it complete.

  Choose **Share recommendation** to share.

  After sharing, choose **Accounts recommendation shared with** to view which accounts have access. You can switch between a JSON view and a list view. To revoke access, select the account and un-share the recommendation.
+ **Mark as complete:** Mark the recommendation as implemented. The recommendation moves to your archived recommendations.
+ **Suppress recommendation:** Suppress the recommendation if it is not relevant to your environment. Suppressed recommendations are hidden from the active list and moved to the archive.
+ **Recommendation feedback:** Provide feedback to help AWS WA Agent improve the relevance and accuracy of future recommendations.

**Console**  
In the **Actions** dropdown, choose **Recommendation feedback**. Select **Useful** or **Not Useful**. You can optionally add comments explaining your feedback. Choose **Submit** to send. If you select **Not Useful**, the recommendation is suppressed after submission.

**API**  
Use the `PutAgentRecommendationFeedback` API to submit feedback programmatically:

  ```
  aws wellarchitected put-agent-recommendation-feedback \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-profile}}" \
      --recommendation-id "{{rec-id}}" \
      --feedback-type USEFUL
  ```

  Valid values for `--feedback-type` are `USEFUL` and `NOT_USEFUL`.

#### CLI
<a name="agent-view-rec-cli"></a>

To list all active recommendations for a profile:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

To list suppressed recommendations for a profile:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --state CLOSED
```

To get the full details of a specific recommendation:

```
aws wellarchitected get-agent-recommendation \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}"
```

To list the individual items (affected resources) for a recommendation:

```
aws wellarchitected list-agent-recommendation-items \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}"
```

### Export recommendations in AWS Well-Architected Agent
<a name="agent-export-rec"></a>

Export your recommendations in AWS WA Agent to share with stakeholders or integrate with external systems for tracking and implementation planning. Recommendations are exported in the CSV file format.

**To export recommendations for a profile**

1.  Open the profile dashboard in **Agent profiles** and choose **Export**. 

1.  Select which recommendations you want to export between Prioritized, Archived, or All recommendations. 

1.  Choose **Export** to download the CSV file. 

The export includes all visible recommendation details and guided actions to implement the recommendation.

### Share recommendations in AWS Well-Architected Agent
<a name="agent-share-rec"></a>

Share specific recommendations with other AWS accounts or team members to collaborate on optimization initiatives.

You can share recommendations in two ways:

**From the dashboard**  
In **All recommendations**, select the radio button next to a recommendation and choose **Share**. Enter the email addresses of your intended recipients and choose **Share** to send.

**From the recommendation detail page**  
Choose **Actions**, then **Share recommendation** to share with other AWS accounts.

**To share a recommendation**

1. Enter a comma-separated list of AWS account IDs to share with (up to 100 accounts).

1. Choose an access level: **Read only** or **Read/write**.

1. Choose **Share recommendation**.

To view or manage shared access, choose **Accounts recommendation shared with** on the recommendation detail page. You can view shared accounts in a list or JSON format, and un-share the recommendation with specific accounts.

### Implement recommendations in AWS Well-Architected Agent
<a name="agent-implement-rec"></a>

AWS WA Agent provides multiple implementation options including automated remediation through AWS Systems Manager, self-service guided actions, and human-in-the-loop support available with Premier Support plans.

#### Remediation models
<a name="agent-remediation-models"></a>

AWS WA Agent uses two remediation models depending on how the recommendation was generated:
+ **SSM Runbook automation:** Recommendations derived from AWS Trusted Advisor checks have pre-built SSM Runbooks. These are deterministic, tested automation that can be run directly or scheduled for recurring execution. AWS WA Agent can trigger one-click remediation on your behalf with your consent.
+ **Guided actions (AI-generated):** Recommendations generated by the AWS WA Agent AI engine (resource, application, and architecture types) include step-by-step guided actions. These may include AWS CLI commands, SDK code, console walkthroughs, or updated IaC templates. Guided actions are advisory and should be reviewed before execution.

**Important**  
AWS WA Agent does not execute AI-generated remediation steps on your behalf. AI-generated guided actions are provided for your review and validation. You are responsible for reviewing, testing, and executing these steps in your environment. This follows the AWS shared responsibility model for AI-generated content.

#### Run SSM Runbook for remediation
<a name="agent-ssm-runbook-remediation"></a>

When a prescheduled auto remediation is not configured for a recommendation, you can view the SSM Runbook details and run the SSM Runbook for remediation.

**To use automated remediation**

1. Navigate to the specific recommendation details page.

1.  Go to the "prescheduled auto-remediation" section, if available.

1. Review the SSM Runbook details including schedule and next run time.

1. Choose the SSM Runbook.

1. Choose **Execute SSM runbook** to run the automation immediately.

1. Monitor the execution status and results.

#### Starting guided remediation
<a name="agent-start-remediation"></a>

After reviewing a recommendation, choose **Start remediation** to begin a guided remediation workflow. AWS WA Agent generates a step-by-step standard operating procedure (SOP) tailored to the specific resources in your environment. The SOP is resource-aware: each step references actual resource names and ARNs from your account rather than generic placeholders.

**To start remediation**

1. On the recommendation detail page, choose **Start remediation**.

1. Select a remediation method:
   + **Using AWS Management Console:** Step-by-step console navigation instructions.
   + **Using AWS CLI:** AWS CLI commands you can copy and run.
   + **Using SDK:** SDK code (Python/boto3) you can adapt and execute.

AWS WA Agent generates a phased SOP for the selected method. Each method produces a different SOP with instructions appropriate to that tool. For example, the console SOP walks you through UI navigation, while the CLI SOP provides ready-to-run commands.

#### Following the guided SOP
<a name="agent-follow-sop"></a>

The remediation view is organized into three panels:
+ **Left panel (phases):** Lists all phases in the SOP (for example, Phase 1 of 10, Phase 2 of 10). The current phase is highlighted. Phase titles describe the action (for example, "Enable S3 Bucket Keys for the CloudTrail logs bucket").
+ **Center panel (instructions):** Detailed instructions for the current phase. Depending on the remediation method, this may include console navigation steps, CLI commands with copy buttons, or SDK code snippets.
+ **Right panel (resources):** Links to relevant AWS documentation for the current phase.

To progress through the SOP:
+ Choose **Mark as complete** to record that you have finished the current phase, then choose **Next** to advance.
+ You can navigate to any phase by selecting it in the left panel.
+ Phases are specific to your resources. For example, if a recommendation affects four S3 buckets, the SOP includes a separate phase for each bucket, referencing it by name.

Typical SOP phases include:

1. Prerequisites (verify tool installation, credentials)

1. Per-resource remediation steps (one or more phases per affected resource)

1. Verification (confirm the change took effect)

1. Documentation (record changes for compliance and audit)

**Important**  
Remediation SOPs are generated using AWS generative AI capabilities and may contain errors or incomplete information. Recommendations might contain information related to security, a nuanced topic. You are responsible for evaluating the recommendation in your specific context and implementing appropriate oversight and safeguards. Review all steps before executing in production. For more information about AWS Responsible AI practices, see [https://aws.amazon.com/ai/responsible-ai/policy/](https://aws.amazon.com/ai/responsible-ai/policy/).

#### Downloading the complete SOP
<a name="agent-download-sop"></a>

Choose **Download complete SOP** to export the full procedure for the currently selected remediation method. The download contains all phases, commands, and resource references in a single document.

Each remediation method (Console, CLI, SDK) has its own downloadable SOP. Switch methods using the radio buttons at the top of the remediation page to download the version you need.

Downloaded SOPs are useful for:
+ Offline execution in environments without console access
+ Attaching to change management tickets for approval
+ Handing off implementation to another team member
+ Archiving as a record of the remediation procedure

#### Completing remediation
<a name="agent-complete-remediation"></a>

##### Console
<a name="agent-complete-remediation-console"></a>

After completing all phases, choose **Mark recommendation as complete** at the top of the remediation page. The recommendation moves to your archived recommendations. If the underlying condition recurs in a future refresh cycle, AWS WA Agent generates a new recommendation.

##### CLI
<a name="agent-complete-remediation-cli"></a>

To mark a recommendation as complete:

```
aws wellarchitected update-agent-recommendation-status \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}" \
    --status COMPLETED
```

To suppress a recommendation:

```
aws wellarchitected update-agent-recommendation-status \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}" \
    --status SUPPRESSED \
    --update-reason "{{Not applicable to our environment}}"
```

To reopen a previously closed recommendation:

```
aws wellarchitected update-agent-recommendation-status \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}" \
    --status ACTIVE
```

### Prescheduled remediations for recommendations in AWS Well-Architected Agent
<a name="agent-prescheduled-rec"></a>

Prescheduled remediations automate the implementation of recommendations at predetermined times using AWS Systems Manager Runbooks. This feature applies recommendations consistently without manual intervention.

In the recommendation details page, choose **View Details** to go to AWS Systems Manager and change the remediation schedule for a recommendation.

### View archived recommendations in AWS Well-Architected Agent
<a name="agent-rec-history"></a>

To view recommendations that were completed or suppressed, choose **View archived recommendations** in the AWS WA Agent dashboard. Each archived recommendation contains information about the status, type, pillars, and closed date. 

When you view an archived recommendation, you see a snapshot of the recommendation from before it was implemented. If the recommendation was suppressed, the reason for suppression is listed on the page. 

### Reopen recommendations in AWS Well-Architected Agent
<a name="agent-rec-reopen"></a>

You can reopen recommendations that are marked as complete or suppressed. Reopened recommendations return to your recommendations list and follow the regularly scheduled refresh cycle.

**To reopen a recommendation**

1. In the AWS WA Agent dashboard, choose **View archived recommendations**.

1. Locate the recommendation that you want to reopen from the recommendations list.

1. Choose the recommendation to view its details page.

1. In the recommendation details page, choose **Reopen**.

1. In the confirmation dialog, review the recommendation details and choose **Reopen** to confirm.

After you reopen a recommendation, AWS WA Agent displays a confirmation message indicating that the recommendation has been reopened and will follow the regularly scheduled refresh cycle. The recommendation returns to your recommendations list where you can view updated details, impacts, and guided actions based on your current AWS environment.

**Note**  
When you reopen a recommendation, AWS WA Agent analyzes your current AWS environment to provide updated insights and impact calculations. The reopened recommendation may show different details than when it was originally generated if your infrastructure has changed.

### Recommendation refresh and data freshness
<a name="agent-refresh-cadence"></a>

AWS WA Agent keeps recommendations current through scheduled refresh cycles:
+ **Scheduled refresh:** Resource and application recommendations are refreshed automatically on a weekly cadence after the initial set of recommendations is generated. You do not need to trigger this manually.
+ **Cooldown periods:** Scheduled recommendation generation runs on a weekly cycle for the same profile. You cannot trigger resource or application recommendations on demand.

**Note**  
Architecture recommendations are not part of the scheduled refresh cycle. They are generated on demand through architecture reviews. For more information, see [Conducting architecture reviews](#agent-architecture-reviews).

**Staleness detection:** Recommendation timestamps are updated during each refresh cycle, even when the recommendation content does not change. A recommendation without a recent timestamp update may no longer be relevant to your current environment.

**Infrastructure changes:** Changes to your environment (new resources, modified configurations) are picked up during the next scheduled refresh cycle. Recommendations are re-evaluated against the current state of your infrastructure at each refresh.

## Conducting architecture reviews
<a name="agent-architecture-reviews"></a>

Architecture reviews analyze your infrastructure as code (IaC) templates against the AWS Well-Architected Framework and return deployment-ready updated templates with best-practice fixes applied. Unlike resource and application recommendations, architecture reviews target templates before deployment, enabling you to identify and resolve issues before they reach production.

Unlike Resource and Application recommendations, AWS WA Agent, Architecture type recommendations are not automatically generated. You must manually conduct an architecture review to generate them.

### Supported input formats
<a name="agent-review-supported-inputs"></a>

You provide an Amazon S3 URI containing your infrastructure as code (IaC) templates for an architecture review. AWS CDK and Terraform projects are supported. The following input types are accepted:
+ **.zip file:** A compressed archive of your IaC project files. The .zip file cannot exceed 25 MB.
+ **Amazon S3 folder:** A folder in Amazon S3 containing your IaC project files. The total folder size cannot exceed 100 MB, and no individual file can exceed 1 MB.

AWS WA Agent validates submitted files and rejects requests that contain malicious content or files that exceed these size limits. Binary and media files are excluded from the review.

### Conducting a review
<a name="agent-conduct-review"></a>

#### Console
<a name="agent-conduct-review-console"></a>

**To conduct an architecture review**

1. In the AWS WA Agent dashboard, choose **Architecture review**.

1. In Review details, enter a name for your architecture review. The name must contain only letters, numbers, hyphens (-), and underscores (\_). Spaces and special characters are not permitted.

1. Upload your file using an S3 URI. Then, choose an **Object version**. You can also choose **Browse S3** to explore files in your S3 buckets.
**Note**  
 AWS WA Agent expects that your S3 buckets are in the same AWS Region as your agent profile. If you cannot find your IaC files, verify that they're in an S3 bucket in the same Region as your profile. 

1.  Select the consent checkbox to allow AWS WA Agent to access the contents of the file. Without selecting this checkbox, you cannot run an architecture review. 

1. Select the **Well-Architected Framework** lens. This is the only lens available for architecture reviews at this time.

1. Select which pillars you want to review.

1. Choose **Start review**.

#### CLI
<a name="agent-conduct-review-cli"></a>

Use the `StartAgentRecommendationGeneration` API to start an architecture review. Only the `ARCHITECTURE` recommendation type is supported for on-demand generation. Resource and application recommendations are generated exclusively through the scheduled refresh cycle and cannot be triggered on demand.

The following parameters control the review request:

`--name` (optional)  
The name of the architecture review. The name can be 1 to 128 characters and must contain only letters, numbers, hyphens (-), and underscores (\_). Spaces and special characters are not permitted.

`--types` (required)  
The recommendation types to generate. Specify `ARCHITECTURE`.

`--scope` (required)  
A JSON object that defines what the review covers. Required for architecture reviews.    
`pillars` (required)  
A list of Well-Architected pillars to review. Valid values: `COST_OPTIMIZATION`, `SECURITY`, `RESILIENCE`, `PERFORMANCE`.  
`goalIds` (optional)  
A list of up to 10 optimization goal IDs to prioritize the review against. You can retrieve goal IDs using `ListAgentGoals`. For information about creating goals, see [Editing goals](#agent-edit-goals).  
`items` (optional)  
A per-pillar filter that narrows the review to specific items. Each object has two required members: `pillar` (a single pillar value) and `ids` (a list of item IDs to process for that pillar, such as best practice IDs like `SEC02-BP02`, AWS service names, or resource ARNs). When `items` is omitted, all items are processed for the selected pillars.

`--additional-context` (optional)  
A JSON object specifying the IaC template location and lens selection. An architecture review analyzes an IaC template, so you provide the template location through this parameter.    
`s3Uri` (required)  
The Amazon S3 URI of the IaC template, .zip archive, or folder to review.  
`s3VersionId` (optional)  
The object version ID of the Amazon S3 object.  
`lensArns` (required)  
A list of lens ARNs to review against. Only the Well-Architected Framework lens (`arn:aws:wellarchitected::aws:lens/wellarchitected`) is supported for architecture reviews at this time.

```
aws wellarchitected start-agent-recommendation-generation \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --types ARCHITECTURE \
    --name "{{my-architecture-review}}" \
    --scope '{
  "pillars": ["COST_OPTIMIZATION", "SECURITY"]
}' \
    --additional-context '{
  "s3Uri": "s3://{{your-bucket}}/{{your-template.yaml}}",
  "s3VersionId": "{{optional-version-id}}",
  "lensArns": ["arn:aws:wellarchitected::aws:lens/wellarchitected"]
}'
```

To monitor the status of an architecture review, use `GetAgentRecommendationGeneration` or `ListAgentRecommendationGenerations`:

```
aws wellarchitected list-agent-recommendation-generations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

### Architecture review limits
<a name="agent-review-limits"></a>

Architecture reviews are limited to 5 reviews per day per profile. You can run reviews consecutively while daily quota remains. Architecture reviews are not subject to the weekly scheduled recommendation generation cycle.

### Viewing review results
<a name="agent-review-results"></a>

You can monitor the status of the review as it progresses or return to the AWS WA Agent dashboard by choosing **Go to dashboard**. The Reviews tab on the dashboard shows all your in-progress and completed reviews.

The generated recommendations include code in the same language as your source template. For example, if you upload a Terraform file, the updated template is returned as Terraform.

## Goals and personalization in AWS Well-Architected Agent
<a name="agent-goals"></a>

AWS Well-Architected Agent uses business goals to prioritize and rank your recommendations. The goals you define during onboarding directly shape which recommendations appear first and how they align with your organization's objectives.

### Immediate value and personalized experience
<a name="agent-immediate-value"></a>

AWS WA Agent provides two tiers of value depending on how much context you provide:
+ **Immediate value (no setup):** Baseline recommendations are available out-of-the-box with no configuration. AWS WA Agent surfaces findings from AWS Trusted Advisor and CloudWatch automatically.
+ **Personalized experience (with onboarding):** When you complete the onboarding workflow and declare business goals, permission boundaries, organizational metadata, and tagging conventions, AWS WA Agent delivers fully personalized, goal-aligned recommendations ranked by business impact.

### How goals drive recommendations
<a name="agent-how-goals-work"></a>

Your personalized recommendations in AWS WA Agent are based on goals that you define in your AWS WA Agent profile. Business goals guide the analysis and recommendation prioritization. Each goal consists of the following:
+ **Goal statement:** A natural language description of your business objective. Make goals specific, measurable, and time-bound for best results.
+ **Target pillar:** The optimization pillar that the goal addresses (Cost optimization, Security, Resilience, or Performance).

AWS WA Agent uses your goals to rank recommendations by relevance and potential impact against your stated objectives. Each recommendation is annotated with the goals that contributed to its generation.

### View your goals in the dashboard
<a name="agent-view-goals-dashboard"></a>

The AWS WA Agent dashboard contains a total of five active goals. By default, the dashboard displays up to three of your active goals. To see all your active goals, choose **View all goals**.

Your active goals represent your organization's strategic objectives and priorities. Active goals help generate personalized recommendations that align with your business needs.

Each recommendation also contains the associated goals that the recommendation is based on. To see the associated goals for a recommendation, in the **Recommendation details** page, choose **view associated goals**.

### Tips for writing effective goals
<a name="agent-goal-best-practices"></a>

The quality of your business goals directly affects how well AWS WA Agent prioritizes and ranks recommendations. Follow these guidelines when defining goals:
+ **Be specific:** Vague goals like "improve security" produce broadly ranked recommendations. Specific goals like "eliminate all public Amazon S3 buckets" produce focused, actionable results.
+ **Include metrics:** Goals with quantifiable targets (for example, "reduce infrastructure cost by 20% year-over-year") allow AWS WA Agent to calculate progress and prioritize by impact.
+ **Specify timeframes:** Time-bound goals help AWS WA Agent prioritize quick wins over long-term improvements when appropriate.
+ **Name the pillar explicitly:** While AWS WA Agent can infer the pillar from goal text, explicitly associating a goal with its pillar (Cost optimization, Security, Resilience, or Performance) produces more accurate targeting.
+ **Avoid overlapping goals:** Multiple goals targeting the same pillar with similar intent can dilute prioritization. Consolidate related objectives into a single, well-defined goal.

## AWS Well-Architected Agent Quotas and limits
<a name="agent-quotas"></a>

### Access and entitlements
<a name="agent-access"></a>

AWS WA Agent access and entitlements depend on your AWS Support plan tier.


**Support tier entitlements**  

| Support tier | Access | Max profiles | Max applications per profile | 
| --- | --- | --- | --- | 
| Developer | No | — | — | 
| Business | No | — | — | 
| Business\+ | Yes | 2 | 7 | 
| Enterprise On-Ramp | Yes | 10 | 30 | 
| Enterprise Support | Yes | 10 | 30 | 
| Unified Operations | Yes | 10 | 30 | 

### Quotas and limits
<a name="agent-quotas-limits"></a>


| Resource | Default limit | Notes | 
| --- | --- | --- | 
| Accounts per profile | 100 | Maximum AWS accounts that a single profile can analyze. | 
| Goals per profile | 10 | Maximum active business goals per profile. | 
| Profile hosting Regions | 3 | Profiles can be hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon). | 
| Scannable Regions | All commercial | AWS WA Agent can scan resources in any commercial AWS Region, regardless of where the profile is hosted. | 
| Recommendations per generation run | 30 | Maximum recommendations produced per scheduled or manual generation run. There is no limit on total stored recommendations. Future runs can add new recommendations. | 
| Architecture reviews per day | 5 | Maximum architecture review generations per day, per profile. Reviews can be run consecutively without cooldown while quota remains. | 
| Scheduled recommendation generation cooldown | 7 days (1 week) | Minimum time between scheduled recommendation generation runs for the same profile. | 
| Maximum .zip file upload size | 25 MB | Maximum compressed size of an uploaded .zip file for architecture reviews. | 
| Maximum Amazon S3 folder size | 100 MB | Maximum total size of an Amazon S3 folder referenced for architecture reviews. | 
| Maximum individual file size (Amazon S3 folder) | 1 MB | Maximum size of each individual file in an Amazon S3 folder referenced for architecture reviews. | 

### Unsupported resource types
<a name="agent-unsupported-resources"></a>

AWS WA Agent does not analyze the CloudFormation resource types in the following table. If your application uses these resource types, AWS WA Agent does not retrieve their configuration data and does not include them in resource-level recommendations.

For more information about specifying the services and resource types your application uses, see [Updating application context](#agent-update-app-context).


**Resource types not supported by AWS WA Agent**  

| Service | Unsupported resource types | 
| --- | --- | 
| `AWS::ACMPCA` |  + `AWS::ACMPCA::Certificate`<br />+ `AWS::ACMPCA::CertificateAuthorityActivation`<br />+ `AWS::ACMPCA::Permission`  | 
| `AWS::AmplifyUIBuilder` |  + `AWS::AmplifyUIBuilder::Component`<br />+ `AWS::AmplifyUIBuilder::Form`<br />+ `AWS::AmplifyUIBuilder::Theme`  | 
| `AWS::ApiGateway` |  + `AWS::ApiGateway::Account`<br />+ `AWS::ApiGateway::Method`  | 
| `AWS::ApiGatewayV2` |  + `AWS::ApiGatewayV2::IntegrationResponse`<br />+ `AWS::ApiGatewayV2::RouteResponse`  | 
| `AWS::AppConfig` |  + `AWS::AppConfig::Deployment`<br />+ `AWS::AppConfig::HostedConfigurationVersion`  | 
| `AWS::ApplicationAutoScaling` |  + `AWS::ApplicationAutoScaling::ScalableTarget`<br />+ `AWS::ApplicationAutoScaling::ScalingPolicy`  | 
| `AWS::AppStream` |  + `AWS::AppStream::AppBlock`<br />+ `AWS::AppStream::Application`<br />+ `AWS::AppStream::ApplicationEntitlementAssociation`<br />+ `AWS::AppStream::ApplicationFleetAssociation`<br />+ `AWS::AppStream::Entitlement`  | 
| `AWS::AppSync` |  + `AWS::AppSync::DomainNameApiAssociation`  | 
| `AWS::AppTest` |  + `AWS::AppTest::TestCase`  | 
| `AWS::AuditManager` |  + `AWS::AuditManager::Assessment`  | 
| `AWS::Bedrock` |  + `AWS::Bedrock::GuardrailVersion`  | 
| `AWS::BillingConductor` |  + `AWS::BillingConductor::BillingGroup`<br />+ `AWS::BillingConductor::CustomLineItem`<br />+ `AWS::BillingConductor::PricingPlan`<br />+ `AWS::BillingConductor::PricingRule`  | 
| `AWS::Cassandra` |  + `AWS::Cassandra::Keyspace`<br />+ `AWS::Cassandra::Type`  | 
| `AWS::CE` |  + `AWS::CE::AnomalyMonitor`<br />+ `AWS::CE::AnomalySubscription`  | 
| `AWS::CertificateManager` |  + `AWS::CertificateManager::Account`  | 
| `AWS::CloudFormation` |  + `AWS::CloudFormation::ModuleVersion`<br />+ `AWS::CloudFormation::Publisher`<br />+ `AWS::CloudFormation::ResourceDefaultVersion`<br />+ `AWS::CloudFormation::ResourceVersion`  | 
| `AWS::CloudFront` |  + `AWS::CloudFront::MonitoringSubscription`  | 
| `AWS::CloudTrail` |  + `AWS::CloudTrail::ResourcePolicy`  | 
| `AWS::Cognito` |  + `AWS::Cognito::LogDeliveryConfiguration`<br />+ `AWS::Cognito::ManagedLoginBranding`<br />+ `AWS::Cognito::UserPoolDomain`<br />+ `AWS::Cognito::UserPoolRiskConfigurationAttachment`<br />+ `AWS::Cognito::UserPoolUICustomizationAttachment`<br />+ `AWS::Cognito::UserPoolUserToGroupAttachment`  | 
| `AWS::Config` |  + `AWS::Config::OrganizationConformancePack`  | 
| `AWS::Connect` |  + `AWS::Connect::ContactFlowVersion`<br />+ `AWS::Connect::DataTableAttribute`<br />+ `AWS::Connect::DataTableRecord`<br />+ `AWS::Connect::InstanceStorageConfig`<br />+ `AWS::Connect::UserHierarchyStructure`<br />+ `AWS::Connect::ViewVersion`  | 
| `AWS::ControlTower` |  + `AWS::ControlTower::EnabledBaseline`<br />+ `AWS::ControlTower::EnabledControl`  | 
| `AWS::DataZone` |  + `AWS::DataZone::DataSource`<br />+ `AWS::DataZone::DomainUnit`<br />+ `AWS::DataZone::Environment`<br />+ `AWS::DataZone::EnvironmentActions`<br />+ `AWS::DataZone::FormType`<br />+ `AWS::DataZone::Owner`<br />+ `AWS::DataZone::PolicyGrant`<br />+ `AWS::DataZone::ProjectMembership`<br />+ `AWS::DataZone::ProjectProfile`  | 
| `AWS::Deadline` |  + `AWS::Deadline::QueueEnvironment`  | 
| `AWS::Detective` |  + `AWS::Detective::OrganizationAdmin`  | 
| `AWS::DeviceFarm` |  + `AWS::DeviceFarm::DevicePool`<br />+ `AWS::DeviceFarm::InstanceProfile`<br />+ `AWS::DeviceFarm::NetworkProfile`<br />+ `AWS::DeviceFarm::Project`<br />+ `AWS::DeviceFarm::TestGridProject`<br />+ `AWS::DeviceFarm::VPCEConfiguration`  | 
| `AWS::EC2` |  + `AWS::EC2::EnclaveCertificateIamRoleAssociation`<br />+ `AWS::EC2::GatewayRouteTableAssociation`<br />+ `AWS::EC2::VPCBlockPublicAccessOptions`  | 
| `AWS::ECS` |  + `AWS::ECS::ExpressGatewayService`<br />+ `AWS::ECS::PrimaryTaskSet`<br />+ `AWS::ECS::TaskSet`  | 
| `AWS::ElasticLoadBalancingV2` |  + `AWS::ElasticLoadBalancingV2::ListenerRule`  | 
| `AWS::EMR` |  + `AWS::EMR::Step`  | 
| `AWS::EventSchemas` |  + `AWS::EventSchemas::RegistryPolicy`  | 
| `AWS::Evidently` |  + `AWS::Evidently::Experiment`<br />+ `AWS::Evidently::Feature`<br />+ `AWS::Evidently::Launch`<br />+ `AWS::Evidently::Project`<br />+ `AWS::Evidently::Segment`  | 
| `AWS::FMS` |  + `AWS::FMS::NotificationChannel`<br />+ `AWS::FMS::Policy`<br />+ `AWS::FMS::ResourceSet`  | 
| `AWS::GlobalAccelerator` |  + `AWS::GlobalAccelerator::EndpointGroup`  | 
| `AWS::Glue` |  + `AWS::Glue::IdentityCenterConfiguration`<br />+ `AWS::Glue::SchemaVersionMetadata`  | 
| `AWS::IAM` |  + `AWS::IAM::GroupPolicy`<br />+ `AWS::IAM::RolePolicy`<br />+ `AWS::IAM::ServiceLinkedRole`<br />+ `AWS::IAM::UserPolicy`  | 
| `AWS::IdentityStore` |  + `AWS::IdentityStore::GroupMembership`  | 
| `AWS::Inspector` |  + `AWS::Inspector::AssessmentTarget`<br />+ `AWS::Inspector::AssessmentTemplate`<br />+ `AWS::Inspector::ResourceGroup`  | 
| `AWS::InspectorV2` |  + `AWS::InspectorV2::CisScanConfiguration`  | 
| `AWS::IoT` |  + `AWS::IoT::ThingType`  | 
| `AWS::IoTAnalytics` |  + `AWS::IoTAnalytics::Channel`<br />+ `AWS::IoTAnalytics::Dataset`<br />+ `AWS::IoTAnalytics::Datastore`<br />+ `AWS::IoTAnalytics::Pipeline`  | 
| `AWS::IoTEvents` |  + `AWS::IoTEvents::AlarmModel`<br />+ `AWS::IoTEvents::DetectorModel`<br />+ `AWS::IoTEvents::Input`  | 
| `AWS::IoTFleetWise` |  + `AWS::IoTFleetWise::Campaign`<br />+ `AWS::IoTFleetWise::DecoderManifest`<br />+ `AWS::IoTFleetWise::Fleet`<br />+ `AWS::IoTFleetWise::ModelManifest`<br />+ `AWS::IoTFleetWise::SignalCatalog`<br />+ `AWS::IoTFleetWise::StateTemplate`<br />+ `AWS::IoTFleetWise::Vehicle`  | 
| `AWS::IoTSiteWise` |  + `AWS::IoTSiteWise::Dashboard`  | 
| `AWS::Kinesis` |  + `AWS::Kinesis::ResourcePolicy`  | 
| `AWS::LakeFormation` |  + `AWS::LakeFormation::PrincipalPermissions`<br />+ `AWS::LakeFormation::TagAssociation`  | 
| `AWS::Lambda` |  + `AWS::Lambda::LayerVersion`<br />+ `AWS::Lambda::LayerVersionPermission`  | 
| `AWS::LicenseManager` |  + `AWS::LicenseManager::Grant`<br />+ `AWS::LicenseManager::License`  | 
| `AWS::Logs` |  + `AWS::Logs::AccountPolicy`  | 
| `AWS::LookoutVision` |  + `AWS::LookoutVision::Project`  | 
| `AWS::Macie` |  + `AWS::Macie::AllowList`<br />+ `AWS::Macie::CustomDataIdentifier`<br />+ `AWS::Macie::FindingsFilter`  | 
| `AWS::MediaConnect` |  + `AWS::MediaConnect::BridgeOutput`<br />+ `AWS::MediaConnect::BridgeSource`  | 
| `AWS::MediaLive` |  + `AWS::MediaLive::ChannelPlacementGroup`<br />+ `AWS::MediaLive::Cluster`<br />+ `AWS::MediaLive::Network`<br />+ `AWS::MediaLive::SdiSource`  | 
| `AWS::MediaPackageV2` |  + `AWS::MediaPackageV2::ChannelPolicy`<br />+ `AWS::MediaPackageV2::OriginEndpoint`<br />+ `AWS::MediaPackageV2::OriginEndpointPolicy`  | 
| `AWS::MediaTailor` |  + `AWS::MediaTailor::ChannelPolicy`  | 
| `AWS::NetworkFirewall` |  + `AWS::NetworkFirewall::LoggingConfiguration`  | 
| `AWS::Notifications` |  + `AWS::Notifications::ManagedNotificationAccountContactAssociation`<br />+ `AWS::Notifications::ManagedNotificationAdditionalChannelAssociation`  | 
| `AWS::ObservabilityAdmin` |  + `AWS::ObservabilityAdmin::OrganizationCentralizationRule`<br />+ `AWS::ObservabilityAdmin::OrganizationTelemetryRule`<br />+ `AWS::ObservabilityAdmin::TelemetryRule`  | 
| `AWS::ODB` |  + `AWS::ODB::CloudAutonomousVmCluster`<br />+ `AWS::ODB::CloudExadataInfrastructure`<br />+ `AWS::ODB::CloudVmCluster`<br />+ `AWS::ODB::OdbNetwork`<br />+ `AWS::ODB::OdbPeeringConnection`  | 
| `AWS::OpenSearchServerless` |  + `AWS::OpenSearchServerless::AccessPolicy`<br />+ `AWS::OpenSearchServerless::LifecyclePolicy`<br />+ `AWS::OpenSearchServerless::SecurityConfig`<br />+ `AWS::OpenSearchServerless::SecurityPolicy`  | 
| `AWS::OpenSearchService` |  + `AWS::OpenSearchService::Domain`  | 
| `AWS::Organizations` |  + `AWS::Organizations::Account`<br />+ `AWS::Organizations::OrganizationalUnit`<br />+ `AWS::Organizations::Policy`<br />+ `AWS::Organizations::ResourcePolicy`  | 
| `AWS::Panorama` |  + `AWS::Panorama::PackageVersion`  | 
| `AWS::PCAConnectorAD` |  + `AWS::PCAConnectorAD::TemplateGroupAccessControlEntry`  | 
| `AWS::QLDB` |  + `AWS::QLDB::Stream`  | 
| `AWS::QuickSight` |  + `AWS::QuickSight::Analysis`<br />+ `AWS::QuickSight::Dashboard`<br />+ `AWS::QuickSight::DataSet`<br />+ `AWS::QuickSight::DataSource`<br />+ `AWS::QuickSight::RefreshSchedule`<br />+ `AWS::QuickSight::Template`<br />+ `AWS::QuickSight::Theme`<br />+ `AWS::QuickSight::Topic`<br />+ `AWS::QuickSight::VPCConnection`  | 
| `AWS::Rbin` |  + `AWS::Rbin::Rule`  | 
| `AWS::RefactorSpaces` |  + `AWS::RefactorSpaces::Application`<br />+ `AWS::RefactorSpaces::Route`<br />+ `AWS::RefactorSpaces::Service`  | 
| `AWS::ResourceExplorer2` |  + `AWS::ResourceExplorer2::DefaultViewAssociation`  | 
| `AWS::RTBFabric` |  + `AWS::RTBFabric::InboundExternalLink`<br />+ `AWS::RTBFabric::Link`<br />+ `AWS::RTBFabric::OutboundExternalLink`  | 
| `AWS::S3` |  + `AWS::S3::AccessGrant`<br />+ `AWS::S3::AccessGrantsLocation`<br />+ `AWS::S3::MultiRegionAccessPointPolicy`  | 
| `AWS::S3ObjectLambda` |  + `AWS::S3ObjectLambda::AccessPointPolicy`  | 
| `AWS::S3Outposts` |  + `AWS::S3Outposts::AccessPoint`<br />+ `AWS::S3Outposts::Bucket`<br />+ `AWS::S3Outposts::BucketPolicy`  | 
| `AWS::S3Tables` |  + `AWS::S3Tables::Table`<br />+ `AWS::S3Tables::TablePolicy`  | 
| `AWS::SageMaker` |  + `AWS::SageMaker::Device`<br />+ `AWS::SageMaker::DeviceFleet`  | 
| `AWS::SecurityHub` |  + `AWS::SecurityHub::AggregatorV2`<br />+ `AWS::SecurityHub::AutomationRule`<br />+ `AWS::SecurityHub::AutomationRuleV2`<br />+ `AWS::SecurityHub::ConfigurationPolicy`<br />+ `AWS::SecurityHub::ConnectorV2`<br />+ `AWS::SecurityHub::DelegatedAdmin`<br />+ `AWS::SecurityHub::FindingAggregator`<br />+ `AWS::SecurityHub::Insight`<br />+ `AWS::SecurityHub::OrganizationConfiguration`<br />+ `AWS::SecurityHub::PolicyAssociation`<br />+ `AWS::SecurityHub::ProductSubscription`<br />+ `AWS::SecurityHub::SecurityControl`<br />+ `AWS::SecurityHub::Standard`  | 
| `AWS::SecurityLake` |  + `AWS::SecurityLake::AWSLogSource`<br />+ `AWS::SecurityLake::Subscriber`<br />+ `AWS::SecurityLake::SubscriberNotification`  | 
| `AWS::ServiceCatalog` |  + `AWS::ServiceCatalog::CloudFormationProvisionedProduct`<br />+ `AWS::ServiceCatalog::PortfolioProductAssociation`<br />+ `AWS::ServiceCatalog::ServiceActionAssociation`<br />+ `AWS::ServiceCatalog::TagOption`<br />+ `AWS::ServiceCatalog::TagOptionAssociation`  | 
| `AWS::SES` |  + `AWS::SES::VdmAttributes`  | 
| `AWS::Shield` |  + `AWS::Shield::DRTAccess`<br />+ `AWS::Shield::ProactiveEngagement`<br />+ `AWS::Shield::Protection`<br />+ `AWS::Shield::ProtectionGroup`  | 
| `AWS::SimSpaceWeaver` |  + `AWS::SimSpaceWeaver::Simulation`  | 
| `AWS::SNS` |  + `AWS::SNS::TopicInlinePolicy`  | 
| `AWS::SQS` |  + `AWS::SQS::QueueInlinePolicy`  | 
| `AWS::SSMContacts` |  + `AWS::SSMContacts::Rotation`  | 
| `AWS::SSO` |  + `AWS::SSO::Application`<br />+ `AWS::SSO::ApplicationAssignment`<br />+ `AWS::SSO::Assignment`<br />+ `AWS::SSO::InstanceAccessControlAttributeConfiguration`<br />+ `AWS::SSO::PermissionSet`  | 
| `AWS::Timestream` |  + `AWS::Timestream::Database`<br />+ `AWS::Timestream::ScheduledQuery`<br />+ `AWS::Timestream::Table`  | 
| `AWS::VoiceID` |  + `AWS::VoiceID::Domain`  | 
| `AWS::VpcLattice` |  + `AWS::VpcLattice::AuthPolicy`<br />+ `AWS::VpcLattice::ResourcePolicy`<br />+ `AWS::VpcLattice::Rule`  | 
| `AWS::WAFv2` |  + `AWS::WAFv2::IPSet`<br />+ `AWS::WAFv2::RegexPatternSet`<br />+ `AWS::WAFv2::RuleGroup`<br />+ `AWS::WAFv2::WebACL`<br />+ `AWS::WAFv2::WebACLAssociation`  | 
| `AWS::Wisdom` |  + `AWS::Wisdom::AIAgentVersion`<br />+ `AWS::Wisdom::AIGuardrailVersion`<br />+ `AWS::Wisdom::AIPromptVersion`  | 

## Related services
<a name="agent-related-services"></a>

AWS Well-Architected Agent integrates with the following AWS services:


| Service | Relationship | 
| --- | --- | 
| AWS Trusted Advisor | AWS WA Agent ingests Trusted Advisor findings as baseline signals. AWS WA Agent adds personalization, cross-pillar analysis, and automation-ready remediation on top of these findings. | 
| AWS Compute Optimizer | AWS WA Agent uses AWS Compute Optimizer rightsizing signals for Amazon EC2, Lambda, and Amazon RDS. AWS WA Agent contextualizes these within your business goals and application topology. | 
| AWS Security Hub CSPM | AWS WA Agent ingests Security Hub CSPM findings. AWS WA Agent adds goal-aligned prioritization and cross-pillar trade-off analysis. | 
| AWS Resilience Hub | AWS WA Agent uses resilience assessment data. AWS WA Agent incorporates your RTO/RPO targets and provides cross-pillar impact analysis. | 
| AWS Cost Optimization Hub | AWS WA Agent uses cost optimization signals. AWS WA Agent ranks cost recommendations against your stated business goals. | 
| AWS Cost Explorer | AWS WA Agent uses Cost Explorer data for accurate, resource-level cost attribution in cost optimization recommendations. Without Cost Explorer enabled, AWS WA Agent estimates costs from public AWS pricing. For more information about enabling Cost Explorer, see [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html). | 
| AWS Well-Architected Tool | AWS WA Agent launches within the AWS Well-Architected console. AWS WA Tool provides manual review workflows. AWS WA Agent provides automated, AI-powered analysis. Both can be used simultaneously. | 
| AWS Systems Manager | AWS WA Agent delivers remediation through SSM Runbooks for automated execution of recommendations. | 

# What is AWS Well-Architected Tool?
<a name="tool"></a>

AWS Well-Architected Tool (AWS WA Tool) is a service in the cloud that provides a consistent process for measuring your architecture using AWS best practices. AWS WA Tool helps you throughout the product lifecycle by doing the following:
+ Assisting with documenting the decisions that you make
+ Providing recommendations for improving your workload based on best practices
+ Guiding you in making your workloads more reliable, secure, efficient, and cost-effective

You can use AWS WA Tool to document and measure your workload using the best practices from the AWS Well-Architected Framework. These best practices were developed by AWS Solutions Architects based on their years of experience building solutions across a wide variety of businesses. The framework provides a consistent approach for measuring architectures and provides guidance for implementing designs that scale with your needs over time.

In addition to AWS best practices, you can use custom lenses to measure your workload using your own best practices. You can tailor the questions in a custom lens to be specific to a particular technology or to help you meet the governance needs within your organization. Custom lenses extend the guidance provided by the AWS lenses.

Integrations with [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) and [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) helps you more easily discover the information needed to answer AWS Well-Architected Toolreview questions. 

This service is intended for those involved in technical product development, such as chief technology officers (CTOs), architects, developers, and operations team members. AWS customers use AWS WA Tool to document their architectures, provide product launch governance, and to understand and manage the risks in their technology portfolio.

**Topics**
+ [Getting started with AWS Well-Architected Tool](#getting-started)
+ [Tutorial: Document an AWS Well-Architected Tool workload](#tutorial)
+ [Well-Architected Framework Review (WAFR)](#wa-framework-review)
+ [Workloads](#workloads)
+ [Using lenses in AWS WA Tool](#lenses)
+ [Review templates in AWS WA Tool](#review-templates)
+ [Tool profiles](#tool-profiles)
+ [AWS Well-Architected Tool Connector for Jira](#jira)
+ [Milestones](#milestones)
+ [Share invitations](#invitations)
+ [Notifications](#notifications)
+ [Dashboard](#dashboard)
+ [Sharing your AWS WA Tool resources](#sharing)
+ [Tagging your AWS WA Tool resources](#tagging)
+ [EventBridge](#eventbridge)

## Getting started with AWS Well-Architected Tool
<a name="getting-started"></a>

To get started using AWS Well-Architected Tool, you first provide the appropriate permissions to the your users, groups, and roles, and activate support for the AWS services you want use with AWS WA Tool. Next, you define and document a workload. You can also save a *milestone* of the current state of a workload.

The following topics explain how to get started using AWS WA Tool. For a step-by-step tutorial showing how to use AWS Well-Architected Tool, see [Tutorial: Document an AWS Well-Architected Tool workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/tutorial.html).

**Topics**
+ [Providing users, groups, or roles access to AWS WA Tool](#iam-auth-access)
+ [Activating support in AWS WA Tool for other AWS services](#activate-integrations)
+ [Defining a workload in AWS WA Tool](#define-workload)
+ [Documenting a workload in AWS WA Tool](#start-workflow-review)
+ [Reviewing a workload with AWS Well-Architected Framework](#continue-workflow-review)
+ [Viewing Trusted Advisor checks for your workload](#ta-checks-page)
+ [Saving a milestone for a workload in AWS WA Tool](#save-milestone)

### Providing users, groups, or roles access to AWS WA Tool
<a name="iam-auth-access"></a>

You can grant users, groups, or roles full control or read-only access to AWS Well-Architected Tool.

**Provide access to AWS WA Tool**

1. To provide access, add permissions to your users, groups, or roles:
   + Users and groups in AWS IAM Identity Center:

     Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
   + Users managed in IAM through an identity provider:

     Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
   + IAM users:
     + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
     + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

1. To grant full control, apply the **WellArchitectedConsoleFullAccess** managed policy to the permission set or role.

   Full access allows the principal to perform all actions in AWS WA Tool. This access is required to define workloads, delete workloads, view workloads, update workloads, share workloads, create custom lenses, and share custom lenses.

1. To grant read-only access, apply the ** WellArchitectedConsoleReadOnlyAccess** managed policy to the permission set or role. Principals with this role can only view resources.

For more information on these policies, see [AWS managed policies for AWS Well-Architected](#security-iam-awsmanpol).

### Activating support in AWS WA Tool for other AWS services
<a name="activate-integrations"></a>

Activating Organization access permits AWS Well-Architected Tool to gather information about your organization's structure to share resources more easily (see [Activate resource sharing within AWS Organizations](#getting-started-sharing-orgs) for more information). Activating Discovery support gathers information from [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html), [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html), and related resources (such as CloudFormation stacks in AppRegistry resource collections) to help you more easily discover the information needed to answer Well-Architected review questions, and tailor the Trusted Advisor checks for a workload. 

Activating support for AWS Organizations, or activating Discovery support automatically creates a service-linked role for your account. 

**To turn on support for other services that AWS WA Tool can interact with, navigate to Settings.**

1. To gather information from AWS Organizations, turn on **Activate AWS Organizations support**. 

1. Turn on **Activate Discovery support** to gather information from other AWS services and resources.

1. Select **View role permissions** to view the service-linked role permissions or trust relationship policies.

1. Select **Save settings**.

#### Activating AppRegistry for a workload
<a name="activate-appregistry"></a>

Using AppRegistry is optional, and AWS Business and Enterprise Support customers can activate it on a per-workload basis.

Whenever Discovery support is turned on and AppRegistry is associated with a new or existing workload, AWS Well-Architected Tool creates a service-managed attribute group. The attribute group **Metadata** in AppRegistry contains the workload ARN, the workload name, and the risks associated with the workload. 
+  When Discovery support is turned on, any time there is a change to the workload, the attribute group is updated.
+  When Discovery support is turned off or the application is removed from the workload, the workload information is removed from AWS Service Catalog.

If you want an AppRegistry application to drive the data fetched from Trusted Advisor, set your workload **Resource definition** as **AppRegistry** or **All**. Create roles for all accounts that own resources in your application following the guidelines in [Activating Trusted Advisor for a workload in IAM](#activate-ta-in-iam). 

#### Activating AWS Trusted Advisor for a workload
<a name="activate-ta-for-workload"></a>

You can optionally integrate AWS Trusted Advisor and activate it on a per-workload basis for AWS Business and Enterprise Support customers. There is no cost to integrate Trusted Advisor with AWS WA Tool, but for Trusted Advisor pricing details, see [AWS Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html). Activating Trusted Advisor for workloads can provide you a more comprehensive, automated, and monitored approach to reviewing and optimizing your AWS workloads. This can help you improve the reliability, security, performance, and cost optimization for your workloads.

**To activate Trusted Advisor for a workload**

1. To activate Trusted Advisor, workload owners can use AWS WA Tool to update an existing workload, or create a new workload by choosing **Define workload**. 

1. Enter an account ID used by Trusted Advisor in the **Account IDs** field, select an application ARN in the **Application** field, or both to activate Trusted Advisor. 

1. In the **AWS Trusted Advisor** section, select **Activate Trusted Advisor**.  
![Screenshot of the Activate Trusted Advisor section when defining a workload.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/defining-workload-activate-ta-support.png)

1. A notification that the **IAM service role will be created** displays the first time Trusted Advisor is activated for a workload. Choosing **View permissions** displays the IAM role permissions. You can view the **Role name**, as well as the **Permissions** and **Trust relationships** JSON automatically created for you in IAM. After the role is created, for subsequent workloads activating** Trusted Advisor**, only the notification for **Additional setup needed** is shown. 

1. In the **Resource definition** dropdown, you can select **Workload Metadata**, **AppRegistry**, or **All**. The **Resource definition** selection defines what data AWS WA Tool fetches from Trusted Advisor to provide the status checks in the workload review that map to Well-Architected best practices.

   **Workload Metadata** – the workload is defined by account IDs and AWS Regions specified in the workload.

   **AppRegistry** – the workload is defined by resources (such as CloudFormation stacks) that are present in the AppRegistry application associated with the workload.

   **All** – the workload is defined by both the workload metadata and AppRegistry resources.

1. Choose **Next**. 

1. Apply the **AWS Well-Architected Framework** to your workload, and choose **Define workload**. Trusted Advisor checks are only linked to the AWS Well-Architected Framework, and not other lenses.

The AWS WA Tool periodically gets data from Trusted Advisor using the roles created in IAM. The IAM role is automatically created for the workload owner. However, to view Trusted Advisor information, the owners of any associated accounts on the workload must go to IAM and create a role, see [Activating Trusted Advisor for a workload in IAM](#activate-ta-in-iam) for more details. If this role does not exist, AWS WA Tool cannot obtain Trusted Advisor information for that account and displays an error. 

For more information about creating a role in AWS Identity and Access Management (IAM), see [Creating a role for an AWS service (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *IAM User Guide*.

##### Activating Trusted Advisor for a workload in IAM
<a name="activate-ta-in-iam"></a>

**Note**  
Workload owners should **Activate Discovery support** for their account before creating a Trusted Advisor workload. Choosing to **Activate Discovery support** creates the role required for the workload owner. Use the following steps for all other associated accounts. 

The owners of associated accounts for workloads that have activated Trusted Advisor must create a role in IAM to see Trusted Advisor information in AWS Well-Architected Tool.

**To create a role in IAM for AWS WA Tool to get information from Trusted Advisor**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the **IAM** console, choose **Roles**, and then choose **Create role**.

1. Under **Trusted entity type** choose **Custom trust policy**. 

1. Copy and paste the following **Custom trust policy** into the JSON field in the **IAM** console, as shown in the following image. Replace {{`WORKLOAD_OWNER_ACCOUNT_ID`}} with the workload owner's account ID, and choose **Next**. 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "wellarchitected.amazonaws.com"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{WORKLOAD_OWNER_ACCOUNT_ID}}"
                   },
                   "ArnEquals": {
                       "aws:SourceArn": "arn:aws:wellarchitected:*:{{111122223333}}:workload/*"
                   }
               }
           }
       ]
   }
   ```

------  
![Screenshot of the Custom trust policy in the IAM console.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/custom-trust-policy.png)
**Note**  
The `aws:sourceArn` in the condition block of the preceeding custom trust policy is `"arn:aws:wellarchitected:*:{{WORKLOAD_OWNER_ACCOUNT_ID}}:workload/*"`, which is a generic condition stating this role can be used by AWS WA Tool for all of the workload owner's workloads. However, access can be narrowed to a specific workload ARN, or set of workload ARNs. To specify multiple ARNs, see the following example trust policy.  

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "wellarchitected.amazonaws.com"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}"
                   },
                   "ArnEquals": {
                       "aws:SourceArn": [
                       "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:workload/{{WORKLOAD_ID_1}}",
       "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:workload/{{WORKLOAD_ID_2}}"
                       ]
                   }
               }
           }
       ]
   }
   ```

1. On the **Add permissions** page, for **Permissions policies** choose **Create policy** to give AWS WA Tool access to read data from Trusted Advisor. Selecting **Create policy** opens a new window.
**Note**  
Additionally, you have the option to skip creating the permissions during the role creation and create an inline policy after creating the role. Choose **View role** in the successful role creation message and select **Create inline policy** from the **Add permissions** dropdown in the **Permissions** tab.

1. Copy and paste the following **Permissions policy** into the JSON field. In the `Resource` ARN, replace {{`YOUR_ACCOUNT_ID`}} with your own account ID, specify the Region or an asterisk (`*`), and choose **Next:Tags**.

   For details about ARN formats, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference Guide*.

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
                   "trustedadvisor:DescribeCheckRefreshStatuses",
                   "trustedadvisor:DescribeCheckSummaries",
                   "trustedadvisor:DescribeRiskResources",
                   "trustedadvisor:DescribeAccount",
                   "trustedadvisor:DescribeRisk",
                   "trustedadvisor:DescribeAccountAccess",
                   "trustedadvisor:DescribeRisks",
                   "trustedadvisor:DescribeCheckItems"
               ],
               "Resource": [
                   "arn:aws:trustedadvisor:*:{{111122223333}}:checks/*"
               ]
           }
       ]
   }
   ```

------

1. If Trusted Advisor is activated for a workload and the **Resource definition** is set to **AppRegistry** or **All**, all of the accounts that own a resource in the AppRegistry application attached to the workload must add the following permission to their Trusted Advisor role's **Permissions policy**.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "DiscoveryPermissions",
               "Effect": "Allow",
               "Action": [
                   "servicecatalog:ListAssociatedResources",
                   "tag:GetResources",
                   "servicecatalog:GetApplication",
                   "resource-groups:ListGroupResources",
                   "cloudformation:DescribeStacks",
                   "cloudformation:ListStackResources"
               ],
               "Resource": "*"
           }
       ]
   }
   ```

------

1. (Optional) Add tags. Choose **Next: Review**.

1. Review the policy, give it a name, and select **Create policy**.

1. On the **Add permissions** page for the role, select the policy name you just created, and select **Next**. 

1. Enter the **Role name**, which must use the following syntax: `WellArchitectedRoleForTrustedAdvisor-{{WORKLOAD_OWNER_ACCOUNT_ID}}` and choose **Create role**. Replace {{`WORKLOAD_OWNER_ACCOUNT_ID`}} with the workload owner's account ID.

   You should get a success message at the top of the page notifying you that the role has been created. 

1. To view the role and associated permissions policy, in the left navigation pane under **Access management**, choose **Roles** and search for the `WellArchitectedRoleForTrustedAdvisor-{{WORKLOAD_OWNER_ACCOUNT_ID}}` name. Select the name of the role to verify that the **Permissions** and **Trust relationships** are correct.

##### Deactivating Trusted Advisor for a workload
<a name="deactivate-ta-for-workload"></a>

**To deactivate Trusted Advisor for a workload**

You can deactivate Trusted Advisor for any workload from the AWS Well-Architected Tool by editing your workload and deselecting **Activate Trusted Advisor**. For more information on editing workloads, see [Edit a workload in AWS Well-Architected Tool](#workloads-edit). 

Deactivating Trusted Advisor from the AWS WA Tool does not delete the roles created in IAM. Deleting roles from IAM requires a separate cleanup measure. Workload owners or owners of associated accounts should delete the IAM roles created when Trusted Advisor is deactivated in AWS WA Tool, or to stop AWS WA Tool from collecting Trusted Advisor data for the workload. 

**To delete the `WellArchitectedRoleForTrustedAdvisor` in IAM**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the **IAM** console, choose **Roles**.

1. Search for `WellArchitectedRoleForTrustedAdvisor-{{WORKLOAD_OWNER_ACCOUNT_ID}}` and select the role name.

1. Choose **Delete**. In the pop-up window, type the name of the role to confirm deletion, and select **Delete** again.

For more information about deleting a role from IAM, see [Deleting an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-managingrole-deleting-console) in the *IAM User Guide*.

### Defining a workload in AWS WA Tool
<a name="define-workload"></a>

A workload is a set of components that deliver business value. For example, workloads can be marketing websites, ecommerce websites, the backend for a mobile app, and analytic platforms. Accurately defining a workload helps ensure a comprehensive review against the AWS Well-Architected Framework pillars. 

**To define a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. If this is your first time using AWS WA Tool, you see a page that introduces you to the features of the service. In the **Define a workload** section, choose **Define workload**.

   Alternately, in the left navigation pane, choose **Workloads** and choose **Define workload**.

   For details on how AWS uses your workload data, choose **Why does AWS need this data, and how will it be used?**

1. In the **Name** box, enter a name for your workload.
**Note**  
The name must be between 3 and 100 characters. At least three characters must not be spaces. Workload names must be unique. Spaces and capitalization are ignored when checking for uniqueness.

1. In the **Description** box, enter a description of the workload. The description must be between 3 and 250 characters.

1. In the **Review owner** box, enter the name, email address, or identifier for the primary group or individual that owns the workload review process.

1. In the **Environment** box, choose the environment for your workload:
   + **Production** – Workload runs in a production environment.
   + **Pre-production** – Workload runs in a pre-production environment.

1. In the **Regions** section, choose the Regions for your workload:
   + **AWS Regions** – Choose the AWS Regions where your workload runs, one at a time.
   + **Non-AWS regions** – Enter the names of the Regions outside of AWS where your workload runs. You can specify up to five unique Regions, separated by commas.

   Use both options if appropriate for your workload.

1. (Optional) In the **Account IDs** box, enter the IDs of the AWS accounts associated with your workload. You can specify up to 100 unique account IDs, separated by commas. 

   If Trusted Advisor is activated, any account IDs specified are used to get data from Trusted Advisor. See [Activating AWS Trusted Advisor for a workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/activate-ta-for-workload.html) to grant AWS WA Tool permissions to get Trusted Advisor data on your behalf within IAM. 

1. (Optional) In the **Application** box, enter the application ARN of an application from the [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) that you want to associate with this workload. Only one ARN can be specified per workload, and the application and workload must be in the same Region.

1. (Optional) In the **Architectural design** box, enter the URL for your architectural design.

1. (Optional) In the **Industry type** box, choose the type of industry associated with your workload.

1. (Optional) In the **Industry** box, choose the industry that best matches your workload.

1. (Optional) In the **Trusted Advisor** section, to turn on Trusted Advisor checks for your workload, select **Activate Trusted Advisor**. Additional setup might be needed for accounts associated with your workload. See [Activating AWS Trusted Advisor for a workload](#activate-ta-for-workload) to grant AWS WA Tool permissions to get Trusted Advisor data on your behalf. Select from **Workload Metadata**, **AppRegistry**, or **All** under **Resource definition** to define what resources AWS WA Tool uses to run Trusted Advisor checks.

1.  (Optional) In the **Jira** section, to turn on workload-level Jira sync settings for the workload, select **Override account level settings**. Additional setup might be needed for accounts associated with your workload. See [AWS Well-Architected Tool Connector for Jira](#jira) to get started with setting up and configuring the connector. Select from **Do not sync workload**, **Sync workload - Manual**, and **Sync workload - Automatic**, and optionally enter a **Jira project key** to sync to. 
**Note**  
 If you do not override account-level settings, workloads will default to the account-level Jira sync setting. 

1. (Optional) In the **Tags** section, add any tags you want to associate with the workload.

   For more information on tags, see [Tagging your AWS WA Tool resources](#tagging).

1. Choose **Next**.

   If a required box is blank or if a specified value is not valid, you must correct the issue before you can continue.

1. (Optional) In the **Apply Profile** step, associate a profile with the workload by selecting an existing profile, searching for the profile name, or choosing **Create profile** to [create a profile](#tool-creating-a-profile). Choose **Next**.

1. Choose the lenses that apply to this workload. Up to 20 lenses can be added to a workload. For descriptions of official AWS lenses, see [Lenses](#lenses).

    Lenses can be selected from **[Custom lenses](#lenses-custom)** (lenses that you created or that were shared with your AWS account), **[Lens Catalog](#lens-catalog)** (AWS official lenses available to all users), or both. 
**Note**  
 The **Custom lenses** section is empty if you have not created a custom lens or had a custom lens shared with you. 
**Disclaimer**  
By accessing and/or applying custom lenses created by another AWS user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the AWS Customer Agreement.

1. Choose **Define workload**.

   If a required box is blank or if a specified value is not valid, you must correct the issue before your workload is defined.

### Documenting a workload in AWS WA Tool
<a name="start-workflow-review"></a>

After you've defined a workload in AWS Well-Architected Tool, you can document its state by opening the Review workload page. This helps you assess your workload and track its progress over time. 

**To document the state of a workload**

1. After you initially define a workload, you see a page that shows the current details of your workload. Choose **Start reviewing** to begin.

   Otherwise, in the left navigation pane, choose **Workloads** and select the name of the workload to open the workload details page. Choose **Continue reviewing**.

   (Optional) If a profile is associated with your workload, then the left navigation pane contains a list of **Prioritized** workload review questions you can use to speed up the workload review process.

1. You are now presented with the first question. For each question:

   1. Read the question and determine if the question applies to your workload.

      For additional guidance, choose **Info** and view the information in the help pane.
      + If the question does not apply to your workload, choose **Question does not apply to this workload**.
      + Otherwise, select the best practices that you are currently following from the list.

        If you are currently not following any of the best practices, choose **None of these**.

      For additional guidance on any item, choose **Info** and view the information in the help pane.

   1. (Optional) If one or more best practices do not apply to your workload, choose **Mark best practice(s) that don't apply to this workload** and select them. For each selected best practice, you can optionally select a reason and provide additional details. 

   1. (Optional) Use the **Notes** box to record information related to the question.

      For example, you might describe why the question does not apply or provide additional details about the best practices selected.

   1. Choose **Next** to continue to the next question.

   Repeat these steps for each question in each pillar.

1. Choose **Save and exit** at any time to save your changes and pause documenting your workload.

After you've documented your workload, you can return to the questions to continuing reviewing it at anytime. For more information, see [Reviewing a workload with AWS Well-Architected Framework](#continue-workflow-review).

### Reviewing a workload with AWS Well-Architected Framework
<a name="continue-workflow-review"></a>

You can review your workload in the console on the Review workload page. This page provides best practices and helpful resources for your workload's performance.

![The Review workload page showing a question and best practices.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/gs-qacallouts-console.png)


1. To open the Review workload page, from the workload details page, choose **Continue reviewing**. The left navigation pane shows the questions for each pillar. Questions that you have answered are marked **Done**. The number of questions answered in each pillar is shown next to the pillar name.

   You can navigate to questions in other pillars by choosing the pillar name and then choosing the question you want to answer. 

   (Optional) If a profile is associated with your workload, then AWS WA Tool uses the information in the profile to determine which questions in the workload review are **Prioritized** and which questions are not applicable for your business. In the left navigation pane you can use the **Prioritized** questions to help speed up the workload review process. A notification icon appears next to questions that are newly added to the list of **Prioritized** questions. 

1. The middle pane displays the current question. Select the best practices that you are following. Choose **Info** to get additional information about the question or a best practice. Choose **Ask an expert** to access the AWS re:Post community dedicated to [AWS Well-Architected](https://repost.aws/topics/TA5g9gZfzuQoWLsZ3wxihrgw/well-architected-framework?trk=1053da05-d131-4bfd-8d08-01af135ae52a&sc_channel=el). AWS re:Post is a topic-based question-and-answer community replacement for AWS Forums. With re:Post, you can find answers, answer questions, join a group, follow popular topics, and vote on your favorite questions and answers. 

   (Optional) To mark one or more best practices as not applicable, choose **Mark best practice(s) that don't apply to this workload** and select them.

   Use the buttons at the bottom of this pane to go to the next question, return to the previous question, or save your changes and exit.

1. The right help pane displays additional information and helpful resources. Choose **Ask an expert** to access the AWS re:Post community dedicated to [AWS Well-Architected](https://repost.aws/topics/TA5g9gZfzuQoWLsZ3wxihrgw/well-architected-framework?trk=1053da05-d131-4bfd-8d08-01af135ae52a&sc_channel=el). In this community, you can ask questions related to designing, building, deploying, and operating workloads on AWS.

### Viewing Trusted Advisor checks for your workload
<a name="ta-checks-page"></a>

If Trusted Advisor is activated for your workload, a **Trusted Advisor checks** tab is displayed next to **Question**. If there are any checks available for the best practice, a notification that there are Trusted Advisor checks available is displayed following the question selection. Selecting **View checks** takes you to the **Trusted Advisor checks** tab. 

![Screenshot of the Trusted Advisor checks available notification on the Question page.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/documenting-workload-ta-checks-available-view-checks.png)


On the **Trusted Advisor checks** tab, you can view more detailed information about the best practice checks from Trusted Advisor, view links to the Trusted Advisor documentation in the **Help resources** pane, or **Download check details**, which provides a report of the Trusted Advisor checks and statuses for each best practice in a CSV file.

![Screenshot of the Trusted Advisor checks page.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/documenting-workload-ta-checks-page.png)


The check categories from Trusted Advisor are displayed as colored icons, and the number next to each icon shows the number of accounts in that status.
+ **Action recommended (red) **– Trusted Advisor recommends an action for the check.
+ **Investigation recommended (yellow)** – Trusted Advisor detects a possible issue for the check.
+ **No problems detected (green)** – Trusted Advisor doesn't detect an issue for the check.
+ **Excluded items (gray)** – The number of checks that have excluded items, such as resources that you want a check to ignore.

For more information on the checks Trusted Advisor provides, see [View check categories](https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html#view-check-categories) in the *Support User Guide*.

Selecting the **Info** link next to each Trusted Advisor check displays information about the check in the **Help resources** pane. For more information, see [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) in the *Support User Guide*.

### Saving a milestone for a workload in AWS WA Tool
<a name="save-milestone"></a>

You can save a milestone for a workload at any time. A milestone records the current state of the workload.

**To save a milestone**

1. From the workload details page, choose **Save milestone**.

1. In the **Milestone name** box, enter a name for your milestone.
**Note**  
The name must be between 3 and 100 characters. At least three characters must not be spaces. Milestone names associated with a workload must be unique. Spaces and capitalization are ignored when checking for uniqueness.

1. Choose **Save**.

After a milestone is saved, you can't change the workload data that was captured in that milestone.

For more information, see [Milestones](#milestones).

## Tutorial: Document an AWS Well-Architected Tool workload
<a name="tutorial"></a>

This tutorial describes using AWS Well-Architected Tool to document and measure a workload. This example illustrates, step by step, how to define and document a workload for a retail ecommerce website.

**Topics**
+ [Step 1: Define a workload](#tutorial-step1)
+ [Step 2: Document the workload state](#tutorial-step2)
+ [Step 3: Review the improvement plan](#tutorial-step3)
+ [Step 4: Make improvements and measure progress](#tutorial-step4)

### Step 1: Define a workload
<a name="tutorial-step1"></a>

You begin by defining a workload. There are two ways to define a workload. In this tutorial, we are not defining a workload from a review template. For more details on defining a workload from a review template, see [Define a workload in AWS Well-Architected Tool](#workloads-define).

**To define a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).
**Note**  
The user who documents the workload state must have [full access permissions](#iam-auth-access) to AWS WA Tool.

1. In the **Define a workload** section, choose **Define workload**.

1. In the **Name** box, enter **Retail Website - North America** as the workload name.

1. In the **Description** box, enter a description for the workload.

1. In the **Review owner** box, enter the name of the person responsible for the workload review process.

1. In the **Environment** box, indicate that the workload is in a production environment.

1. Our workload runs on both AWS and at our local data center:

   1. Select **AWS Regions**, and choose the two Regions in North America where the workload runs.

   1. Also select **Non-AWS regions**, and enter a name for the local data center.

1. The **Account IDs** box is optional. Do not associate any AWS accounts with this workload. 

1. The **Application** box is optional. Do not enter an Application ARN for this workload.

1. The **Architectural diagram** box is optional. Do not associate an architectural diagram with this workload.

1. The **Industry type** and **Industry** boxes are optional and are not specified for this workload.

1.  The **Trusted Advisor** section is optional. Do not **Activate Trusted Advisor Support** for this workload.

1.  The **Jira** section is optional. Do not **Override account level settings** in the Jira section for this workload. 

1. For this example, do not apply any tags to the workload. Choose **Next**.

1. The **Apply profile** step is optional. Do not apply a profile for this workload. Choose **Next**.

1. For this example, apply the AWS Well-Architected Framework lens, which is automatically selected. Choose **Define workload** to save these values and define the workload.

1. After the workload is defined, choose **Start reviewing** to begin documenting the state of the workload.

### Step 2: Document the workload state
<a name="tutorial-step2"></a>

To document the state of the workload, you are presented with questions for the selected lens that span the pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. 

For each question, choose the best practices that you are following from the list provided. If you need details about a best practice, choose **Info** and view the additional information and resources in the right panel. 

Choose **Ask an expert** to access the AWS re:Post community dedicated to [AWS Well-Architected](https://repost.aws/topics/TA5g9gZfzuQoWLsZ3wxihrgw/well-architected-framework?trk=1053da05-d131-4bfd-8d08-01af135ae52a&sc_channel=el). In this community, you can ask questions related to designing, building, deploying, and operating workloads on AWS.

![Picture showing the question and answer portion of a workload review.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/tut-qascreen-console.png)


1. Choose **Next** to proceed to the next question. You can use the left panel to navigate to a different question in the same pillar or to a question in a different pillar.

1. If you choose **Question does not apply to this workload** or **None of these**, AWS recommends that you include the reason in the **Notes** box. These notes are included as part of the workload report and can be helpful in the future as changes are made to the workload.
**Note**  
Optionally, you can mark one or more individual best practices as not applicable. Choose **Mark best practice(s) that don't apply to this workload** and select the best practice that does not apply. You can optionally select a reason and provide additional details. Repeat for each best practice that does not apply.  
![Picture showing marking a best practice as not applicable.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/tut-nachoices-console.png)
**Note**  
You can pause this process at any time by choosing **Save and exit**.To resume later, open the AWS WA Tool console and choose **Workloads** in the left navigation pane.

1. Select the name of the workload to open the workload details page.

1. Choose **Continue reviewing** and then navigate to where you left off.

1. After you complete all of the questions, an overview page for the workload appears. You can review these details now or navigate to them later by choosing **Workloads** in the left navigation pane and selecting the workload name.

After documenting the state of your workload for the first time, you should save a milestone and generate a workload report.

A milestone captures the current state of the workload and enables you to measure progress as you make changes based on your improvement plan.

From the workload details page: 

1. In the **Workload overview** section, choose the **Save milestone** button.

1. Enter **Version 1.0 - initial review** as the **Milestone name**.

1. Choose **Save**.

1. To generate a workload report, select the desired lens and choose **Generate report** and a PDF file is created. This file contains the state of the workload, the number of risks identified, and a list of suggested improvements.

### Step 3: Review the improvement plan
<a name="tutorial-step3"></a>

Based on the best practices selected, AWS WA Tool identifies areas of high and medium risk as measured against the AWS Well-Architected Framework Lens.

To review the improvement plan:

1. Choose **AWS Well-Architected Framework** from the **Lenses** section of the **Overview** page. 

1. Then choose **Improvement plan**.

For this particular example workload, three high risk issues and one medium risk issue were identified by the AWS Well-Architected Framework Lens.

![Picture showing the first part of the improvement plan.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/tut-imprplanstatus-console.png)


Update the **Improvement status** for the workload to indicate that improvements to the workload have not been started. 

To change the **Improvement status**:

1. From the Improvement plan, click on the name of the workload (**Retail Website - North America**) in the breadcrumbs at the top of the page.

1. Click on the **Properties** tab.

1. Navigate to the **Workload status** section and select **Not Started** from the dropdown list.  
![Picture showing workload status dropdown.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/tut-wlstatus-console.png)

1. Navigate back to the Improvement plan from the **Properties** tab by clicking on the **Overview** tab and then clicking on the **AWS Well-Architected Framework** link in the **Lenses** section. Then click on the **Improvement plan** tab at the top of the page.

The **Improvement items** section shows the recommended improvement items identified in the workload. The questions are ordered based on the pillar priority that is set, with any high risk issues listed first followed by any medium risk issues. 

Expand **Recommended improvement items** to show the best practices for a question. Each recommended improvement action links to detailed expert guidance to help you eliminate, or at least mitigate, the risks identified. 

If a profile is associated with the workload, a count of prioritized risks is displayed in the **Improvement plan overview** section, and you can filter the list of **Improvement items** by selecting **Prioritized by profile**. The list of improvement items display a **Prioritized** label. 

### Step 4: Make improvements and measure progress
<a name="tutorial-step4"></a>

As part of this improvement plan, one of the high risk issues was addressed by adding Amazon CloudWatch and AWS Auto Scaling support to the workload. 

From the **Improvement items** section:

1. Choose the pertinent question and update the selected best practices to reflect the changes. **Notes** are added to record the improvements. 

1. Then choose **Save and exit** to update the state of the workload.

1. After making changes, you can return to the **Improvement plan** and see the effect those changes had on the workload. In this example, those actions have improved the risk profile — reducing the number of high risk issues from three to only one.

![Picture showing better risk scores after improvements.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/suc-improved-console.png)


You can save a milestone at this point, and then go to **Milestones** to see how the workload has improved.

## Well-Architected Framework Review (WAFR)
<a name="wa-framework-review"></a>

 The [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) describes key concepts and design principles for creating and running workloads in the cloud. It helps you understand the pros and cons of decisions you make while building systems on AWS. With the help of the Framework you will learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable applications. 

 During the *Well-Architected Framework Review (WAFR)*, you will answer a set of foundational questions to learn how well your architecture aligns with cloud best practices and receive guidance for implementing improvements. 

### WAFR phases
<a name="wafr-phases"></a>

 The WAFR process consists of three main phases: 
+  **[Prepare:](#preparing-for-a-wafr)** Set up for success with proper planning and stakeholder alignment 
+  **[Review:](#running-a-wafr)** Conduct the actual assessment against AWS best practices 
+  **[Improve:](#improving-your-workload)** Turn findings into actionable improvements for your workload 

 This document guides you through the three phases, verifying that you have sufficient preparation to derive the most value from the review phase. We also guide you towards turning your WAFR findings into actionable improvements for your workload. 

### Preparing for a WAFR
<a name="preparing-for-a-wafr"></a>

 It's important not to rush into running a Well-Architected Framework Review (WAFR) without sufficient preparation. Rushing can lead to the process taking longer than expected, which provides a less favorable outcome and makes taking action more difficult. 

 Reviewing an architecture has an associated human cost. If a group or team member can prepare upfront, this saves time in later stages, where more people are required to attend sessions. This can also remove the requirement for larger group discussions through improved session planning and asynchronous communication techniques. 

 Having a clear definition of who owns the workload, how it is architected, its purpose, and its alignment with your organization's business outcomes can help you achieve a better result during the *review* and *improve* phases. 

 The *preparation* phase consists of three key elements: 

1.  Workload and scope 

1.  People and culture 

1.  Documentation and infrastructure 

#### Mechanisms
<a name="mechanisms"></a>

 *Mechanisms* replace human best efforts with repeatable, scalable processes and tools, which are often automated, to achieve a desired outcome. A mechanism is a complete cycle where you create a tool or a process, drive its adoption, and inspect the results to make course corrections. This cycle takes controllable inputs and transforms them into ongoing outputs to address a recurring business challenge. 

![Mechanisms flywheel](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/mechanism-flywheel.png)


 The cyclic nature of a mechanism makes it best suited for solving recurring problems or opportunities. The WAFR is a mechanism with a tool, an adoption process, and an inspection process that all operate in a complete cycle. 

 When conducting WAFRs of your workloads, you identify improvement opportunities to develop other mechanisms in your organization. The outcomes from a WAFR should not be one time fixes for a single team but should instead be shared across multiple teams to deliver most value. 

#### Business outcomes
<a name="business-outcomes"></a>

 Before you start making changes to technology, determine your business priorities. It's less effective to review your architecture without a clear understanding of your organization's priorities. These priorities can serve as guidelines to help you maintain alignment and deliver better results. 

 Business outcomes are key high-value business objectives that are tied to organizational strategy and driven by customer feedback. They are purposefully high level so that different teams can define more specific goals to achieve those outcomes. 

 Examples of common business outcomes are: 
+  Reduce costs 
+  Increase profit 
+  Improve customer satisfaction 
+  Improve customer retention 
+  Improve staff retention 
+  Improve environmental sustainability 
+  Improve security posture 

 Being aware of and working backwards from your organization's business outcomes helps you save time by focusing on the technology changes that can make the most impact toward your organization's goals. This in turn increases trust with your leadership. 

 Discover and discuss what are currently the business priorities for your organization, business unit, or team. 

#### Resources
<a name="resources-2"></a>
+  [How to perform a Well-Architected Framework Review - Part 1](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part1/) 

#### Workload and scope
<a name="workload-and-scope"></a>

 According to the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads.html): 

 A workload is a collection of resources and code that delivers business value, such as a customer-facing application or a backend process. A workload might consist of a subset of resources in a single AWS account or be a collection of multiple resources spanning multiple AWS accounts. A small business might have only a few workloads while a large enterprise might have thousands. 

 A workload is more than cloud services or resources. It also includes people, teams, processes, and runbooks, along with the technology and infrastructure that deliver business value. Before running a WAFR, invest time to understand and document components of your workload. This can help you save time during the review phase. 

##### Choosing a workload for a WAFR
<a name="choosing-a-workload-for-a-wafr"></a>

 To prepare a workload for a WAFR, discuss the following questions with the team: 
+  Who owns the workload? Who is responsible if a disruption of the workload impacts the business? 
+  What is the purpose of the workload? Are there analytics for the business? Does it have a sandbox, training, and logging? 
+  Does this workload need to exist? What happens if you shut it down? 
+  Is the workload customer-facing or internal? 
+  Is the workload production or non-production? 
+  What phase is the workload in its lifecycle? 
+  What is the impact if the workload had a disruption? 
+  What are the boundaries of the workload? 
+  What dependencies does this workload have? 

 You should be able to clearly answer most of these questions when evaluating your workload before continuing with the WAFR. 

##### What is the scope of the review?
<a name="what-is-the-scope-of-the-review"></a>

 Although ultimately a WAFR spans [all pillars of the Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), we can identify trade-offs and understand the context before making decisions. A good way to start is to focus on prioritized pillars or a particular area of the workload. 

 Defining the larger review process, producing some actionable results, and iterating helps you produce more value for the workload and the business. 

 Consider a phased approach: 

1.  Identify two to three major pillars that are most relevant to the current business and technical context 

1.  Demonstrate the value of your workload within these pillars 

1.  After you get satisfactory results, repeat with more pillars 

 To reduce scope further, use lenses that are designed specifically for your workloads. 

#### People and culture
<a name="people-and-culture"></a>

 Every workload needs an owner, and many people and teams may be involved in the lifecycle of a workload. However, before running a WAFR, define a single-threaded owner (STO) for the workload. 

 This person must be able to make decisions and control the budget, headcount, and roadmap. Examples of this role are a product owner, product manager, head architect, or engineering manager. 

 Ultimately, this role is responsible if the workload no longer functions as intended. 

 It's important to run a WAFR with an STO to improve your outcomes. For example, you may find improvement items for the workload but have little success in prioritizing them on the product roadmap. Alternatively, you may struggle to acquire funding or resources to carry out the work. 

 This often results in gathering an unachievable list of backlog items. The STO helps you avoid this outcome, as they own the WAFR and are invested in the process. 

![Single-threaded owner](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/STO.png)


##### Required stakeholders
<a name="required-stakeholders"></a>

 The STO can't answer all the questions. Many people and teams are involved in either architecting, developing, securing, or operating a workload. Depending on the organization and size of the workload, the number of stakeholders and teams involved will vary. 

![Team structure diagram showing single threaded owner above suggested WAFR participants](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/WorkloadTeam.png)


 Consider the following questions regarding stakeholders: 

1.  Who needs to be present to answer each category of questions? 

1.  Which stakeholders are required to be present during which parts of the WAFR? 

1.  How can you inform different stakeholders of the questions in advance? 

##### Pillar sponsors
<a name="pillar-sponsors"></a>

 The Well-Architected Framework consists of [six pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html). While defining an STO is crucial, it's as important to gather support from pillar-specific sponsors or champions to accelerate and increase the value of the WAFR process. 

![Team structure diagram showing single threaded owner above six pillar specific champions](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/Champions.png)


 Define pillar sponsors or champions who can: 
+  Attend specific parts of the WAFR to provide information or guidance 
+  Own the outcomes for their subject matter area 
+  Define, influence, and communicate strategic cross-organizational changes 

 Does your organization have a Cloud Center of Excellence or Cloud Community of Practice? Start small and grow a group of like-minded people who can support each other with architectural health discussions and improvements. 

##### Create a safe space
<a name="create-a-safe-space"></a>

 Developing a healthy organizational culture is crucial to healthy, productive discussions about technology choices. The group of people involved in the WAFR could be new or old to the workload, of different tenure and seniority, or involved as partners and third parties. It's critical to nurture a healthy, respectful conversation about a workload to improve the likelihood of lasting, useful improvement. 

 Set a positive intent from the beginning and re-emphasizing throughout to maintain alignment and focus on discovering improvement opportunities. Technology and best practices evolve, so a WAFR must be framed as an opportunity to discover improvements. 

 A WAFR is not an audit. While the findings can help you meet different compliance standards, the process does not exist to "score" a workload. Focus on increasing architectural health. 

 A WAFR is a chance to ask "where are we?" and to capture a point in time view of the workload. Then, you can use the findings to make an informed decision to answer "where should we go?" 

 Architectural improvement is a journey that AWS Well-Architected guides. Consider the following questions as you begin your WAFR process: 

1.  Why are you running the WAFR? 

1.  What do you hope to get out of it? 

1.  How will the experience benefit everyone? 

1.  Where are you now, and where do you want to get to? 

##### Resources
<a name="resources-1"></a>
+  [Accountability Blog Post](https://aws.amazon.com/blogs/enterprise-strategy/two-pizza-teams-are-just-the-start-accountability-and-empowerment-are-key-to-high-performing-agile-organizations-part-2/) 
+  [Amazon Two Pizza Teams](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/) 

#### Documentation and infrastructure
<a name="documentation-and-infrastructure"></a>

 When running a WAFR, you may find that for many of the best practices you are following, you will have a documented process, standard operating procedure (SOP), runbook, or playbook. During the WAFR, record information and context in the notes field within the Well-Architected Tool (WA Tool). You can save time during the review by gathering all relevant documentation artifacts that relate to the workload in advance. 

 Consider the following questions as you consider your documentation: 
+  What documentation exists about the workload? 
+  What documentation is missing? 
+  What tools would be used to create and store these artifacts? 
+  Who would be involved in the creation and maintenance of these artifacts? 

 Some examples of documentation about your workload include: 
+  Workload wiki pages 
+  Architectural diagrams 
+  Architectural decision record (ADR) 
+  Standard operating procedures (SOPs) 
+  Infrastructure as code (IaC) repositories 
+  Networking topology 
+  Playbooks and runbooks 
+  Organization or team structure 
+  Multi-account strategy documentation 
+  Central identity provider configuration 
+  Central monitoring solution configuration 
+  Documentation for dependent workloads 
+  API reference guide 
+  Software library versions 
+  Correction of errors (COE) process and history 
+  Chaos engineering strategy 
+  Load testing team details 
+  Threat model 
+  Team retrospectives 
+  Game day documents 

##### Anti-patterns
<a name="anti-patterns"></a>

 If none of these resources exist, you can still run the WAFR as a discovery mechanism. However, the process can take longer without these artifacts. Creating documentation assets can be the first step towards architectural health improvement. 

##### Workload discovery
<a name="workload-discovery"></a>

 It's difficult to efficiently review an architecture without knowing its components and resources. Legacy workloads often evolve over time or change ownership, and they may not have been defined using infrastructure as code (IaC) tools like AWS CloudFormation, AWS CDK, or Terraform. 

 Before discussing improvements, understand the different architectural components of the workload and its dependencies, and create a visual representation to provide a shared understanding. 

 There are many third party discovery and auto-diagramming tools available directly from the software vendors, from [AWS Marketplace](https://aws.amazon.com/marketplace/search/results/), or as open source solutions. 

##### Resources
<a name="resources"></a>
+  [AWS Reference Architecture Diagrams](https://aws.amazon.com/architecture/reference-architecture-diagrams) 
+  [Architectural Decision Record Process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) 
+  [ADR GitHub Home](https://adr.github.io/) 
+  [Why you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) 
+  [Workload Discovery On AWS Solution](https://aws.amazon.com/solutions/implementations/workload-discovery-on-aws/) 

### Running a WAFR
<a name="running-a-wafr"></a>

 After all the required preparation, it is time for you to run a Well-Architected Framework Review (WAFR). In this section, we'll explore tips and tricks to become more efficient while conducting your WAFR. 

#### Before the WAFR
<a name="before-the-wafr"></a>

 Before you begin discussing the workload as a group, go over the following section and discuss the rules of engagement for the session. You should have a consensus in your group for how to proceed. 

##### Define roles and responsibilities
<a name="define-roles-and-responsibilities"></a>
+  Who is leading the WAFR? 
+  Who will be sharing their screen, and what they will be sharing on it? 
+  Who will be taking notes in the WA Tool or another format? 
+  Which pillars will you be reviewing and in which order? 
+  Do you have the right people in the room to answer the questions? 
+  How will you capture out of scope items, and how will you create your backlog for these items? 
+  How much time do you want to allocate for each section or pillar? 
+  What do you want to achieve in the time you have allocated? 

#### Review tips
<a name="review-tips"></a>

 Plan the meetings around capturing data points about the workload architectural choices. There's a number of things you can do to make this section of the WAFR as smooth as possible. 

1.  **Communicate positive intent:** Revisit the positive intent of the WAFR with the participants. Critical conversations about work can be difficult, so reaffirm that the WAFR is being conducted to find improvement opportunities. Reinforce a *no blame culture*. There is no attack or defense, but rather a collaborative discussion about architectural improvement. 

1.  **Bring a supporter:** Navigating a complex workload architecture, asking questions, moderating responses, and taking notes can be challenging for one person. A successful WAFR is a team activity. Designate alternate roles, which allows one person to run the review while another takes notes, checks the documentation, and monitors the discussion. 

1.  **Stay on topic:** It's common when having group conversations around architectural decisions for people to get sidetracked. If you want to be efficient with time, make sure that WAFR participants respectfully hold each other to stay on topic. Capture side concepts and ideas in a centralized place that can be picked up during future discussion sessions. 

1.  **Take good notes:** Simply ticking boxes in the WA Tool does not provide context to someone revisiting the WAFR in later milestones. Use the notes box in the WA Tool, or create an external document linked from the WAFR notes box if you exceed the character limit. Context helps other parties, especially people who are new to the workload, understand ongoing work and determine what to prioritize. 

1.  **Don't focus on solutions:** Focus on capturing data points about the workload rather than solutions. Too much focus on solutions can waste time during your WAFR session and prevent you from capturing important data points. It's not the best use of other participants' time if you brainstorm something that is out of scope. 

1.  **Focus on the workload, not the tool:** It's common for people to share their screen showing the Well-Architected Tool (WA Tool) in the AWS Management Console. Although capturing data in the WA Tool is crucial, don't focus exclusively on the tool. Focus your discussion on the architecture instead. Keep the review conversational, and paraphrase the questions to align with the context. 

1.  **Divide the discussion into parts:** It can be difficult to review all six pillars in one meeting. Spread the review out into smaller sessions, which allows for a more topic-targeted approach and can be easier to schedule with your participants. 

1.  **Remember to take breaks:** Reviewing architecture thoroughly can be tiring for participants, and their concentration can lapse over time. Schedule frequent breaks during the WAFR. Be frugal with participants' time, and allow for people to drop when they are no longer required. 

1.  **Think carefully about maybes:** If you find the answer for a question is "maybe," "kind of," or "we have something in the backlog to address that," carefully consider if this actually means "no." A WAFR is about capturing the honest and *current* state of the workload, not the intended state. 

1.  **Consider trade-offs:** Well-Architected is about making trade-offs between pillars. To make a workload more resilient might come at the detriment of your cost optimization, or further optimizing cost might have an impact on your workload's environmental impact. The pillars are there to provide a structure for your conversations and to help you make informed architectural choices. 

1.  **Recognize that no workload can be perfect:** Workloads are rarely perfect and often do not need to be. Avoid turning your WAFR into an exercise of making everything perfect, and focus on making the workload function safely and efficiently for its intended business purpose. 

#### Running the WAFR
<a name="running-the-wafr"></a>

 Run the WAFR in the AWS account alongside the workload. You can then share the workload review with other AWS accounts. 

 [Share the review](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html) with a central account using AWS Organizations. You can then use the [dashboard](https://docs.aws.amazon.com/wellarchitected/latest/userguide/dashboard.html) to view your organization's workloads centrally. 

 This can help you recognize patterns of risks and improvements across all your workloads. You can then address the challenge centrally with a pattern-based approach that can be shared and used across many accounts and workloads. 

#### IAM access
<a name="iam-access"></a>

 Accessing the AWS WA Tool in the AWS Management Console requires IAM permissions. Determine who needs access in advance to save time at the beginning of the WAFR session. 

 For more detail, see [Providing users, groups, or roles access to AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/iam-auth-access.html). 

 You can set up a [cross-account IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) to allow external stakeholders to access the WA Tool and edit or view reviews. 

#### Resources
<a name="resources-3"></a>
+  [How to perform a Well-Architected Framework Review Part 2](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part2/) 

### Improving your workload
<a name="improving-your-workload"></a>

 At this point, you've prepared for the WAFR, completed a review, and assessed your workload against AWS best practices. 

 The output from the WAFR will have identified architectural risks based on the answers captured during the review. These risks are categorized as *high risk issues (HRIs)* and *medium risk issues (MRIs)*. 

 During the last phase, you will create an improvement plan that involves creating a list of risks, understanding their impact on your business, identifying solutions, and implementing those solutions according to your organization's priorities. 

 The following sections provide detailed guidance on the workload improvement process: 
+  Identify and understand risks 
+  Determine prescriptive solutions 
+  Prioritize improvements 
+  Implement and track improvements 

 The following cycle shows the main steps included in the *improvement* phase of the WAFR. 

![Improvement cycle](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/improvement_cycle.png)


#### Timeline after the WAFR
<a name="timeline-after-the-wafr"></a>

 **One day after the WAFR:**

1. Create a recap email with the improvement plan, and summarize: 
   + Who was in the review
   + Key findings
   + Timeline for next steps

1. Attach the improvement plan

1. Orient the teams to plan

 **Two to three days after the WAFR:**

1. Create an HRI prioritization meeting, and prioritize HRIs: 
   + By effort
   + By impact
   + With the teams responsible for the workloads

1. Collaborate on what really matters most to the business

 **One week after the WAFR:**

1. Begin the improvement plan

1. Consider the following recommendations: 
   + **Duration:** 90 or 180 days
   + Identify priority HRIs
   + Develop mitigations for each
   + Try to maximize initiatives to solve multiple HRIs

 **Routine tasks:**

1. Build a cadence for follow-up meetings regarding the improvement plan

1. Review actions to take to improve the workload

1. Consider the following recommendations: 
   + Set attendee expectations
   + Send them WA question links
   + Conduct follow up reviews

#### Identify and understand risks
<a name="identify-and-understand-risks"></a>

 View identified risks as improvement opportunities. 

 There are two categories of risks in the context of a WAFR: *high risk issues (HRIs)* and *medium risk issues (MRIs)*. 
+  **High risk issue (HRI):** Architectural and operational choices that may cause significant negative impact to a business. A high risk best practice is considered a foundational, must-do practice within a pillar. They may impact organizational operations, assets, and individuals. An example of an HRI from the security pillar is not securing your AWS account. 
+  **Medium risk issue (MRI):** Choices that may also impact your business negatively, but to a lesser extent than HRIs. A medium risk best practice represents an enabling practice that can substantially improve a workload. An example of MRI on the security pillar is not auditing and rotating credentials periodically. 

##### Generating a report
<a name="generating-a-report"></a>

 The first step to visually identify HRIs and MRIs is to generate a report that shows the risks for each workload you reviewed. 

 The [AWS Well-Architected Tool (AWS WA Tool) dashboard](https://docs.aws.amazon.com/wellarchitected/latest/userguide/dashboard.html) provides access to your workloads and their associated HRIs and MRIs. You also can include workloads that have been shared with you. Using the dashboard, you can filter the issues by workload, pillar, or by severity (high or medium). 

 In the dashboard page, you can see the list of HRI and MRIs filtered by pillar or severity. Once an improvement item is selected, it takes you directly to the best practices associated with it from the Well-Architected Framework. From there, you can read about the recommended action needed to take to remediate the issue along with necessary resources. 

 You can combine all these findings in one report by choosing [Generate report](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-report.html) from the WA Tool Dashboard. 

 We recommend sending a recap email to the WAFR attendees along with the report, and summarize the key findings and the suggested improvement plan to prepare them for the next step. 

##### Managing risks
<a name="managing-risks"></a>

 To effectively manage a risk, it's critical to define the risk and its acceptable level. With risk analysis, explore what the potential problems are and how to know if they are problems. 

 There are two primary methods to conduct a risk assessment: 
+  **Quantitative:** Uses weighted objective data to assess the impact of a risk in terms of cost overrun, resource consumption, and schedule delays. 
+  **Qualitative:** Uses subjective data not tied to the actual values of the cost or benefits to measure the probability and the overall impact. 

 In some cases, you may end up using a hybrid approach that merges the best of both approaches to assess the impact of a risk. 

 When evaluating the level of the risk based on HRI and MRI definitions, consider asking the following questions: 
+  What is the likelihood of risk resulting in impact? 
+  What would be the customer impact? 
+  What would be the business impact as a result? 
+  Can the risk be removed entirely or only mitigated? 
+  Who owns the risk? 
+  Who owns the improvement work to remove or mitigate? 
+  What's the probability that this outcome happens again? Is it likely to cause the same impact? 
+  Can you identify a relationship between the likelihood of an outcome and a pattern of recurrence? 

 Having key stakeholders or business owners answer these questions will help you create a list of the most important risks to focus on along with the projected time to address them. 

##### Risk magnitude
<a name="risk-magnitude"></a>

 You can use following table to help you determine risk magnitude: 


| Likehood x impact | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Critical (5) | 
| --- | --- | --- | --- | --- | --- | 
| Almost certain (5) | 5 | 10 | 15 | 20 | 25 | 
| Likely (4) | 4 | 8 | 12 | 26 | 20 | 
| Possible (3) | 3 | 6 | 9 | 12 | 15 | 
| Unlikely (2) | 2 | 4 | 6 | 8 | 10 | 
| Rare (1) | 1 | 2 | 3 | 4 | 5 | 

 Work as a group on HRIs and MRIs and the risks they bring to business. Create a list of HRIs that need to be addressed. Rank the risks based on business criticality to establish priority. 

#### Determine prescriptive solutions
<a name="determine-prescriptive-solutions"></a>

 Once risks and improvement opportunities are understood in your organization's context, work with the teams on the mitigation. At this phase, each team needs to work on the HRIs found in their areas and determine a prescriptive solution to address the HRI. 

 This step may require additional research, discussions, or building proof of concepts. It's important not to spend too much time jumping into the implementation details of a solution in this phase. It will happen later if you decide that the HRI in question is a priority. 

 The purpose of this step is to understand the complexity of the solution and what resources are required so you can factor them in when prioritizing tasks based on time, complexity, and impact. 

 Work as a group to gather a list of possible solutions for the HRIs. Keep things high level and do not get into implementation details. 

#### Prioritize improvements
<a name="prioritize-improvements"></a>

 No organization has unlimited time and resources. Addressing all identified HRIs and MRIs at once might not be the right way to get the most out of a WAFR. 

 Start with a selected number of issues that can make the most impact on the business and that are easier to implement. Work on the solution. Track the improvement, and then iterate on that approach. 

##### Prioritize for implementation
<a name="prioritize-for-implementation"></a>

 One approach that can help you visualize solutions priority is the [Eisenhower-style plot](https://www.eisenhower.me/eisenhower-matrix/). There are different ways to use the tool. When evaluating, consider both the importance of the improvement (how much value it brings to your business) and the effort to implement the improvement (time required, complexity to implement, or headcount). 

![Eisenhower plot](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/eisenhower.png)


 The output of this analysis provides a set of risks that have the most impact on your business but are not too complex to implement. These are good candidates to start implementing in the first iteration. 

##### Solution characteristics
<a name="solution-characteristics"></a>

 When selecting a solution for an identified risk, consider the following: 
+  [**SMART goals:**](https://www.forbes.com/advisor/business/smart-goals/) Think of specific, measurable, achievable, relevant, and time-bound (SMART) goals. 
+  **Owners:** For every solution, identify an owner. 
+  **Simple over complex:** Complex solutions can work, but they make the improvement more difficult to implement, and they can take longer to create. Choose simplicity over complexity unless the complex solution is a non-negotiable requirement. 
+  [**Make two-way door decisions:**](https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/) Solutions should be extensible and designed to improve and evolve over time. When possible, avoid static solutions that cannot adapt as your architecture develops. 
+  **Target pattern-based solutions:** Consider solutions that can be codified, reused, and re-shared. Don't reinvent the wheel. Access the [AWS Architecture Center](https://aws.amazon.com/architecture/) for examples. 
+  **Work continually as a team:** Work as a group to create a list of solutions for the HRIs. Prioritize them in an Eisenhower matrix. 

#### Implement and track improvements
<a name="implement-and-track-improvements"></a>

 The ideal outcome of successful implementations is a reduction in HRIs and MRIs, resulting in an improvement to the architectural health of your workload. 

 Implementation of remediations should be done iteratively, using milestones in the WA Tool that record the state of a workload at a particular point in time. Each time you conduct a review session, or when you complete improvement items, save a milestone to measure the progress as you go. 

##### WAFR in agile
<a name="wafr-in-agile"></a>

 The output from a WAFR prioritization exercise can be used to prioritize tickets for sprints and backlogs for development teams. Developers should be able to understand the impact of the implementations and own the contribution to an improved architectural health. WAFR improvement and tracking can be integrated in an agile retrospective. 

 Retrospectives are meetings held at the end of an iteration or sprints. During the retrospective, the team reflects on what happened in the iteration and identifies actions for improvement going forward. It is an ideal mechanism to include WAFR reviews for discussion and empower members in architectural health. 

##### Timeline
<a name="timeline"></a>

 The timeline for these steps varies per organization, as every organization is different and has unique challenges. However, following successful WAFRs performed with many customers at AWS, we recommend this phase to take between 90 and 180 days. 

 If your list of HRIs and MRIs takes longer, re-prioritize them and come up with a shorter list so that you can start practicing the process to get some improvement. Then, repeat with your remaining items. 

## Workloads
<a name="workloads"></a>

A workload is a collection of resources and code that delivers business value, such as a customer-facing application or a backend process.

A workload might consist of a subset of resources in a single AWS account or be a collection of multiple resources spanning multiple AWS accounts. A small business might have only a few workloads while a large enterprise might have thousands.

The **Workloads** page, available from the left navigation, provides information about your workloads and any workloads that have been shared with you.

The following information is displayed for each workload:

**Name**  
The name of the workload.

**Owner**  
The AWS account ID that owns the workload.

**Questions answered**  
The number of questions answered.

**High risks**  
The number of high risk issues (HRIs) identified.

**Medium risks**  
The number of medium risk issues (MRIs) identified.

**Improvement status**  
The improvement status that you have set for the workload:  
+ None
+ Not Started
+ In Progress
+ Complete
+ Risk Acknowledged

**Last updated**  
Date and time that the workload was last updated.

After you choose a workload from the list:
+ To review the details of the workload, choose **View details**. 
+ To change the properties of the workload, choose **Edit**.
+ To manage sharing of the workload with other AWS accounts, users, AWS Organizations, or organization units (OUs), choose **View details** and then **Shares**.
+ To delete the workload and all of its milestones, choose **Delete**. Only the owner of the workload can delete it.
**Warning**  
Deleting a workload cannot be undone. All data associated with the workload is deleted.

### High Risk Issues (HRIs) and Medium Risk Issues (MRIs)
<a name="wat-hri-mri"></a>

**High risk issues (HRIs)** identified in the AWS Well-Architected Tool are architectural and operational choices that AWS has found might result in significant negative impact to a business. These HRIs might affect organizational operations, assets, and individuals. **Medium risk issues (MRIs)** also might negatively impact business, but to a lesser extent. These issues are based on your responses in the AWS Well-Architected Tool. The corresponding best practices are widely applied by AWS and AWS customers. These best practices are the guidance defined by the AWS Well-Architected Framework and lenses.

**Note**  
These are guidelines only and customers should evaluate and measure what impact not implementing the best practice would have on their business. If there are specific technical or business reasons that prevent applying a best practice to the workload, then the risk might be lower than indicated. AWS suggests that customers document these reasons, and how they affect the best practice, in the workload notes. For all identified HRIs and MRIs, AWS suggests customers implement the best practice as defined in the AWS Well-Architected Tool. If the best practice is implemented, indicate that the issue has been resolved by marking the best practice as met in the AWS Well-Architected Tool. If customers choose not to implement the best practice, AWS suggests that they document the applicable business level approval and reasons for not implementing it. 

### Define a workload in AWS Well-Architected Tool
<a name="workloads-define"></a>

There are two ways to define a workload. On the **Workloads** page in AWS WA Tool you can define a workload without a template. Or, on the **Review templates** page, you can use an existing review template or create a new template to define a workload.

**To define a workload from the Workloads page**

1. Select **Workloads** in the left navigation pane.

1. Select the **Define workload** dropdown.

1. Choose **Define workload**. Or, if you have created a review template and want to define a workload from it, choose **Define from review template**.

1. Follow the instructions in [Defining a workload in AWS WA Tool](#define-workload) to specify the workload properties, or (optionally) apply profiles and lenses.

**To define a workload from the Review templates page**

1. Select **Review templates** in the left navigation pane.

1. Select the name of an existing review template, or follow the instructions in [Creating a review template in AWS WA Tool](#creating-a-review-template) to create a new review template.

1. Choose **Define workload from template**.

1. Follow the instructions in [Defining a workload from a template in AWS WA Tool](#define-workload-from-template) to create the workload from your review template.

### View a workload in AWS Well-Architected Tool
<a name="workloads-page"></a>

You can view the details of workloads that you own and workloads that have been shared with you.

**To view a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload to view in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

The workload details page is displayed.

**Note**  
A required field, **Review owner**, was added to allow you to easily identify the primary person or group that is responsible for the review process.  
The first time you view a workload that was defined before this field was added, you are notified of this change. Choose **Edit** to set the **Review owner** field and no further action is required.  
Choose **Acknowledge** to defer setting the **Review owner** field. For the next 60 days, a banner is displayed to remind you that the field is blank. To remove the banner, edit your workload and specify a **Review owner**.  
If you do not set the field by the specified date, your access to the workload is restricted. You can continue to view the workload and delete it, but you cannot edit it, except to set the **Review owner** field. Shared access to the workload is not affected while your access is limited.

### Edit a workload in AWS Well-Architected Tool
<a name="workloads-edit"></a>

You can edit the details of a workload that you own.

**To edit a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload that you want to edit and choose **Edit**.

1. Make your changes to the workload.

   For a description of each of the fields, see [Defining a workload in AWS WA Tool](#define-workload).
**Note**  
When updating an existing workload, you can **Activate Trusted Advisor**, which automatically creates the IAM role for the workload owner. The owners of associated accounts for workloads with Trusted Advisor activated need to create a role in IAM. For details, see [Activating Trusted Advisor for a workload in IAM](#activate-ta-in-iam).

1. Choose **Save** to save your changes to the workload.

   If a required field is blank or if a specified value is not valid, you must correct the issue before your updates to the workload are saved.

### Share a workload in AWS Well-Architected Tool
<a name="workloads-sharing"></a>

You can share a workload that you own with other AWS accounts, users, an organization, and organization units (OUs) in the same AWS Region.

**Note**  
You can only share workloads within the same AWS Region.   
When sharing a workload with another AWS account, if the recipient does not have the `wellarchitected:UpdateShareInvitation` permission, they cannot accept the share invitation. See [Providing users, groups, or roles access to AWS WA Tool](#iam-auth-access) for permission policy examples. 

**To share a workload with other AWS accounts and users**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select a workload that you own in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**. Then choose **Create** and **Create shares to users or accounts** to create a workload invitation.

1. Enter the 12-digit AWS account ID or the ARN of the user that you want to share the workload with.

1. Choose the permission that you want to grant.  
**Read-Only**  
Provides read-only access to the workload.  
**Contributor**  
Provides update access to answers and their notes, and read-only access to the rest of the workload.

1. Choose **Create** to send a workload invitation to the specified AWS account or user.

If the workload invitation is not accepted within seven days, the invitation is automatically expired. 

If a user and the user's AWS account both have workload invitations, the workload invitation with the highest level permission is applied to the user. 

**Important**  
Before sharing a workload with an organization or organization units (OUs), you must [enable AWS Organizations access](#getting-started-sharing-orgs).

**To share a workload with your organization or OUs**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select a workload that you own in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**. Then choose **Create** and **Create shares to Organizations**.

1. On the **Create workload share** page, choose whether to grant permissions to the entire organization, or to one or more OUs.

1. Choose the permission that you want to grant.  
**Read-Only**  
Provides read-only access to the workload.  
**Contributor**  
Provides update access to answers and their notes, and read-only access to the rest of the workload.

1. Choose **Create** to share the workload.

To see who has shared access to a workload, choose **Shares** from the [View workload details in AWS Well-Architected Tool](#workload-details) page.

To prevent an entity from sharing workloads, attach a policy that denies `wellarchitected:CreateWorkloadShare` actions.

You can also share custom lenses that you own with other AWS accounts, users, your organization, and OUs in the same AWS Region. For details, refer to [Sharing a custom lens in AWS WA Tool](#lenses-sharing).

#### Considerations when sharing AWS Well-Architected Tool workloads
<a name="sharing-considerations"></a>

A workload can be shared with up to 20 different AWS accounts and users. A workload can only be shared with accounts and users that are in the same AWS Region as the workload.

To share a workload in a Region introduced after March 20, 2019, both you and the shared AWS account must enable the Region in the AWS Management Console. For more information, refer to [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

You can share a workload with an AWS account, individual users in an account, or both. When you share a workload with an AWS account, all users in that account are given access to the workload. If only specific users in an account require access, follow the best practice of granting least privilege and share the workload individually with those users.

If both an AWS account and a user in the account have workload invitations, the workload invitation with the highest level permissions determines the user's permission to the workload. If you delete the workload invitation for the user, the user's access is determined by the workload invitation for the AWS account. Delete both workload invitations to remove the user's access to the workload.

Before sharing a workload with an organization or one or more organization units (OUs), you must enable AWS Organizations access.

If you share a workload with both an organization and one or more OUs, the workload invitation with the highest level permissions determines the account's permission to the workload.

**To enable AWS Organizations sharing**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Settings**.

1. Choose **Enable AWS Organizations support**.

1. Choose **Save settings**.

#### Delete shared access in AWS Well-Architected
<a name="sharing-remove"></a>

You can delete a workload invitation. Deleting a workload invitation removes shared access to the workload.

**To delete shared access to a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**.

1. Select the workload invitation to delete and choose **Delete**.

1. Choose **Delete** to confirm.

If a user and the user's AWS account have workload invitations, you must delete both workload invitations to remove the user's permission to the workload.

#### Modify shared access in AWS Well-Architected
<a name="sharing-change"></a>

You can modify a pending or accepted workload invitation.

**To modify shared access to a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select a workload that you own in one of the following ways:
   + Choose the name of the workload.
   + Select the workload and choose **View details**.

1. Choose **Shares**.

1. Select the workload invitation to modify and choose **Edit**.

1. Choose the new permission that you want to grant to the AWS account or user.  
**Read-Only**  
Provides read-only access to the workload.  
**Contributor**  
Provides update access to answers and their notes, and read-only access to the rest of the workload.

1. Choose **Save**.

If the modified workload invitation is not accepted within seven days, it's automatically expired.

#### Accept and reject workload invitations in AWS Well-Architected
<a name="sharing-invitations"></a>

A workload invitation is a request to share a workload that is owned by another AWS account. If you accept the workload invitation, the workload is added to your **Workloads** and **Dashboard** pages. If you reject the workload invitation, it's removed from the workload invitation list.

You have seven days to accept a workload invitation. If you do not accept the invitation within seven days, it's automatically expired.

**Note**  
Workloads can only be shared within the same AWS Region.

**To accept or reject a workload invitation**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workload invitations**.

1. Select the workload invitation to accept or reject.
   + To accept the workload invitation, choose **Accept**.

     The workload is added to the **Workloads** and **Dashboard** pages.
   + To reject the workload invitation, choose **Reject**.

     The workload invitation is removed from the list.

To reject shared access after a workload invitation has been accepted, choose **Reject share** from the [View workload details in AWS Well-Architected Tool](#workload-details) page for the workload.

### Delete a workload in AWS Well-Architected Tool
<a name="workloads-delete"></a>

You can delete a workload when it's no longer needed. Deleting a workload removes all data associated with the workload including any milestones and workload share invitations. Only the owner of a workload can delete it.

**Warning**  
Deleting a workload cannot be undone. All data associated with the workload is permanently removed.

**To delete a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the workload you want to delete and choose **Delete**.

1. In the **Delete** window, choose **Delete** to confirm the deletion of the workload and its milestones.

To prevent an entity from deleting workloads, attach a policy that denies `wellarchitected:DeleteWorkload` actions.

### Generate a workload report in AWS Well-Architected Tool
<a name="workloads-report"></a>

You can generate a workload report for a lens. The report contains your responses to the workload questions, your notes, and the current number of high and medium risks identified. If a question has one or more risks identified, the improvement plan for that question lists actions to take to mitigate those risks.

If your workload has an associated profile, the profile overview information and the prioritized risks are displayed on the workload report.

A report enables you to share details about your workload with others who do not have access to AWS Well-Architected Tool. 

**To generate a workload report**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the desired workload and choose **View details**.

1. Select the lens you want to generate a report for and choose **Generate report**.

   The report is generated and you can download or view it.

### View workload details in AWS Well-Architected Tool
<a name="workload-details"></a>

The workload details page provides information about your workload including its milestones, improvement plan, and any workload shares. Use the tabs at the top of the page to navigate to the different detail sections.

To delete the workload, choose **Delete workload**. Only the owner of a workload can delete it.

To remove your access to a shared workload, choose **Reject share**.

**Topics**
+ [The AWS Well-Architected Tool Overview tab](#details-review)
+ [The AWS Well-Architected Tool Milestones tab](#details-milestones)
+ [The AWS Well-Architected Tool Properties tab](#details-properties)
+ [The AWS Well-Architected Tool Shares tab](#details-permissions)

#### The AWS Well-Architected Tool Overview tab
<a name="details-review"></a>

When you initially view a workload, the **Overview** tab is the first information displayed. This tab provides the overall state of your workload followed by the state of each lens. 

If you have not completed all of the questions, a banner appears to remind you to start or continue documenting your workload.

The **Workload overview** section shows the current overall state of the workload and any **Workload notes** that you have entered. Choose **Edit** to update the state or notes.

To capture the current state of the workload, choose **Save milestone**. Milestones are immutable and cannot be changed after they are saved.

To continue documenting the state of the workload, choose **Start reviewing** and select the desired lens.

#### The AWS Well-Architected Tool Milestones tab
<a name="details-milestones"></a>

To display the milestones for your workload, choose the **Milestones** tab.

After you select a milestone, choose **Generate report** to create the workload report associated with the milestone. The report contains the responses to the workload questions, your notes, and the number of high and medium risks in the workload at the time that the milestone was saved.

You can view details about the state of your workload at the time of a specific milestone by either:
+ Choosing the name of the milestone.
+ Selecting the milestone and choosing **View milestone**.

#### The AWS Well-Architected Tool Properties tab
<a name="details-properties"></a>

To display the properties of your workload, choose the **Properties** tab. Initially, these properties are the values that were specified when the workload was defined. Choose **Edit** to make changes. Only the owner of the workload can make changes.

For descriptions of the properties, see [Defining a workload in AWS WA Tool](#define-workload).

#### The AWS Well-Architected Tool Shares tab
<a name="details-permissions"></a>

To display or modify your workload invitations, choose the **Shares** tab. This tab is only displayed for the owner of a workload.

The following information is displayed for each AWS account and user that has shared access to the workload:

**Principal**  
The AWS account ID or user ARN with shared access to the workload.

**Status**  
The status of the workload invitation.  
+ Pending

  The invitation is waiting to be accepted or rejected. If a workload invitation is not accepted within seven days, it's automatically expired.
+ Accepted

  The invitation was accepted.
+ Rejected

  The invitation was rejected.
+ Expired

  The invitation was not accepted or rejected within seven days.

**Permission**  
The permission granted to the AWS account or user.  
+ Read-Only

  The principal has read-only access to the workload.
+ Contributor

  The principal can update answers and their notes, and has read-only access to the rest of the workload.

**Permission details**  
Detailed description of the permission.

To share the workload with another AWS account or user in the same AWS Region, choose **Create**. A workload can be shared with up to 20 different AWS accounts and users.

To delete a workload invitation, select the invitation and choose **Delete**.

To modify a workload invitation, select the invitation and choose **Edit**.

## Using lenses in AWS WA Tool
<a name="lenses"></a>

In AWS Well-Architected Tool, you can use lenses to consistently measure your architectures against best practices and identify areas for improvement. The **AWS Well-Architected Framework Lens** is automatically applied when a workload is defined.

A workload can have one or more lenses applied. Each lens has its own set of questions, best practices, notes, and improvement plan. 

 There are two kinds of lenses that can be applied to your workloads: **Lens Catalog** lenses and **Custom lenses**. 
+  **[Lens Catalog](#lens-catalog):** Official lenses that are created and maintained by AWS. The Lens Catalog is available to all users and does not require any additional installation to use. 
+  **[Custom lenses](#lenses-custom):** User-defined lenses that are not AWS official content. You can [create custom lenses](#lenses-create) with your own pillars, questions, best practices, and improvement plans, as well as [share custom lenses](#lenses-sharing) with other AWS accounts. 

Five lenses can be added at a time to a workload, with a maximum of 20 lenses applied to one workload.

If a lens is removed from a workload, the data associated with the lens is retained. The data is restored if you add the lens back to the workload.

### Adding a lens to a workload in AWS WA Tool
<a name="lenses-add"></a>

Adding a lens to a workload helps you better understand your architecture's strengths and weaknesses, identify improvements, and ensure your workloads follow best practices.

**To add a lens to a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the desired workload and choose **View details**.

1. Select the lens to add choose **Save**.

    Lenses can be selected from **Custom lenses**, **Lens Catalog**, or both. 

Up to 20 lenses can be added to a workload.

For more information about the AWS lens catalog, visit [AWS Well-Architected Lenses](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc#AWS_Well-Architected_Lenses). Note that not every lens whitepaper is provided as a lens in the lens catalog.

**Disclaimer**  
By accessing and/or applying custom lenses created by another AWS user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the AWS Customer Agreement.

### Removing a lens from a workload in AWS WA Tool
<a name="lenses-remove"></a>

If a lens is no longer relevant for your workload, you can remove it.

**To remove a lens from a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Workloads**.

1. Select the desired workload and choose **View details**.

1. Deselect the lens that you want to remove and choose **Save**.

   The AWS Well-Architected Framework Lens cannot be removed from a workload.

The data associated with the lens is retained. If the lens is added back to the workload, the data is restored.

### Viewing lens details for a workload in AWS WA Tool
<a name="lenses-details"></a>

You can view details about your lenses on the AWS Well-Architected Tool console. To view details about a lens, select the lens.

#### Overview tab
<a name="lenses-overviewtab"></a>

The **Overview** tab provides general information about the lens, such as the number of questions answered. From this tab, you can continue reviewing a workload, generate a report, or edit the lens notes.

#### Improvement plan tab
<a name="lenses-improvementtab"></a>

The **Improvement Plan** tab provides a list of recommended actions to improve your workload. You can filter recommendations based on risk and pillar.

#### Shares tab
<a name="lenses-sharestab"></a>

For a custom lens, the **Shares** tab provides a list of IAM principals that the lens has been shared with.

### Custom lenses for workloads in AWS WA Tool
<a name="lenses-custom"></a>

You can create custom lenses with your own pillars, questions, best practices, and improvement plan. You apply custom lenses to a workload in the same way that you apply AWS provided lenses. You can also share custom lenses that you create with other AWS accounts, and custom lenses owned by others can be shared with you.

You can tailor the questions in a custom lens to be specific to a particular technology, help you meet the governance needs within your organization, or extend the guidance provided by the Well-Architected Framework and the AWS lenses. Like the existing lenses, you can track progress over time by creating milestones, and provide periodic status by generating reports.

**Topics**
+ [Viewing custom lenses in AWS WA Tool](#lenses-viewing)
+ [Creating a custom lens for a workload in AWS WA Tool](#lenses-create)
+ [Previewing a custom lens for a workload in AWS WA Tool](#lenses-preview)
+ [Publishing a custom lens in AWS WA Tool for the first time](#lenses-publish)
+ [Publishing an update to a custom lens in AWS WA Tool](#lenses-publish-update)
+ [Sharing a custom lens in AWS WA Tool](#lenses-sharing)
+ [Adding tags to a custom lens in AWS WA Tool](#lenses-tagging)
+ [Deleting a custom lens in AWS WA Tool](#lenses-deleting)
+ [Lens format specification in AWS WA Tool](#lenses-format-specification)

#### Viewing custom lenses in AWS WA Tool
<a name="lenses-viewing"></a>

You can view the details of custom lenses that you own and custom lenses that have been shared with you.

**To view a lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.
**Note**  
 The **Custom lenses** section is empty if you have not created a custom lens or had a custom lens shared with you. 

1. Choose which custom lenses you want to view:
   + **Owned by me** – Shows custom lenses that you have created.
   + **Shared with me** – Shows custom lenses that have been shared with you.

1. Select the custom lens to view in one of the following ways:
   + Choose the name of the lens.
   + Select the lens and choose **View details**.

The [Viewing lens details for a workload in AWS WA Tool](#lenses-details) page is displayed.

The **Custom lenses** page has the following fields:

**Name**  
The name of the lens.

**Owner**  
The AWS account ID that owns the custom lens.

**Status**  
A status of **PUBLISHED** means that the custom lens has been published and can be applied to workloads or shared with other AWS accounts.  
A status of **DRAFT** means that the custom lens has been created but has not yet been published. A custom lens must be published before it can be applied to workloads or shared.

**Version**  
The version name of the custom lens.

**Last updated**  
Date and time that the custom lenses was last updated.

#### Creating a custom lens for a workload in AWS WA Tool
<a name="lenses-create"></a>

**To create a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Choose **Create custom lens**.

1. Choose **Download file** to download the JSON template file.

1. Open the JSON template file with your favorite text editor and add the data for your custom lens. This data includes your pillars, questions, best practices, and improvement plan links.

   Refer to [Lens format specification in AWS WA Tool](#lenses-format-specification) for details. A custom lens cannot exceed 500 KB in size.

1. Choose **Choose file** to select your JSON file.

1. (Optional) In the **Tags** section, add any tags you want to associate with the custom lens.

1. Choose **Submit & Preview** to preview the custom lens, or **Submit** to submit the custom lens without previewing.

   If you choose to **Submit & Preview** your custom lens, you can select **Next** to navigate through the lens preview, or select **Exit Preview** to go back to **Custom lenses**.

If validation fails, edit your JSON file and try creating the custom lens again.

After AWS WA Tool validates your JSON file, your custom lens is displayed in **Custom lenses**.

After a custom lens has been created, it's in **DRAFT** status. You must [publish the lens](#lenses-publish) before it can be applied to workloads or shared with other AWS accounts. 

You can create up to 15 custom lenses in an AWS account.

**Disclaimer**  
Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.

#### Previewing a custom lens for a workload in AWS WA Tool
<a name="lenses-preview"></a>

**To preview a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Only lenses in a **DRAFT** status can be previewed. Select the desired **DRAFT** custom lens and choose **Preview experience**.

1. Choose **Next** to navigate through the lens preview.

1. (Optional) You can review your **Improvement plan** by selecting best practices within each question in the preview, and choosing **Update based on answers** to test your risk logic. If there are changes needed, you can update the [Risk Rules](#lenses-format-risk-rules) in your JSON template before publishing. 

1. Choose **Exit Preview** to go back to the custom lens.

**Note**  
You can also preview a custom lens by selecting **Submit & Preview** when [Creating a custom lens](#lenses-create). 

#### Publishing a custom lens in AWS WA Tool for the first time
<a name="lenses-publish"></a>

**To publish a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the desired custom lens and choose **Publish lens**.

1. In the **Version name** box, enter a unique identifier for the version change. This value can be up to 32 characters and must only contain alphanumeric characters and periods (".").

1. Choose **Publish custom lens**.

   After a custom lens has been published, it's in **PUBLISHED** status. 

The custom lens can now be applied to workloads or shared with other AWS accounts or users.

#### Publishing an update to a custom lens in AWS WA Tool
<a name="lenses-publish-update"></a>

**To publish an update to an existing custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the desired custom lens and choose **Edit**.

1. If you do not have an updated JSON file ready, choose **Download file** to download a copy of the current custom lens. Edit the downloaded JSON file with your favorite text editor and make your desired changes.

1. Choose **Choose file** to select your updated JSON file and choose **Submit & Preview** to preview the custom lens, or **Submit** to submit the custom lens without previewing.

   A custom lens cannot exceed 500 KB in size.

   After AWS WA Tool validates your JSON file, your custom lens is displayed in **Custom lenses** in **DRAFT** status.

1. Select the custom lens again and choose **Publish lens**.

1. Choose **Review changes before publishing** to verify that the changes made to your custom lens are correct. This includes validating:
   + The name of the custom lens
   + The pillar names
   + The new, updated, and deleted questions

   Choose **Next**.

1. Specify the type of version change.  
**Major version**  
Indicates that substantial changes have been made to the lens. Use for changes that impact the meaning of the custom lens.  
Any workloads with the lens applied will be notified that a new version of the custom lens is available.  
Major version changes are *not* automatically applied to workloads using the lens.  
**Minor version**  
Indicates that minor changes have been made to the lens. Use for small changes, such as text changes or updates to the URL links.  
Minor version changes are automatically applied to workloads using the custom lens.

   Choose **Next**.

1. In the **Version name** box, enter a unique identifier for the version change. This value can be up to 32 characters and must only contain alphanumeric characters and periods (".").

1. Choose **Publish custom lens**.

   After a custom lens has been published, it's in **PUBLISHED** status. 

The updated custom lens can now be applied to workloads or shared with other AWS accounts or users.

If the update is a *major version change*, any workloads with the previous version of the lens applied will be notified that a new version is available and given the option to upgrade.

Minor version updates are automatically applied without any notification.

You can create up to 100 versions of a custom lens.

#### Sharing a custom lens in AWS WA Tool
<a name="lenses-sharing"></a>

You can share a custom lens with other AWS accounts, users, AWS Organizations, and organization units (OUs).

**To share a custom lens with other AWS accounts and users**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the custom lens to be shared and choose **View details**.

1. On the [Viewing lens details for a workload in AWS WA Tool](#lenses-details) page, choose **Shares**. Then choose **Create** and **Create shares to users or accounts** to create a lens share invitation.

1. Enter the 12-digit AWS account ID or the ARN of the user that you want to share the custom lens with.

1. Choose **Create** to send a lens share invitation to the specified AWS account or user.

You can share a custom lenses with up to 300 AWS accounts or users.

If the lens share invitation is not accepted within seven days, the invitation is automatically expired. 

**Important**  
Before sharing a custom lens with an organization or organization units (OUs), you must [enable AWS Organizations access](#getting-started-sharing-orgs).

**To share a custom lens with your organization or OUs**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the custom lens to be shared.

1. On the [Viewing lens details for a workload in AWS WA Tool](#lenses-details) page, choose **Shares**. Then choose **Create** and **Create shares to Organizations**.

1. On the **Create custom lens share** page, choose whether to grant permissions to the entire organization, or to one or more OUs.

1. Choose **Create** to share the custom lens.

To see who has shared access to a custom lens, choose **Shares** from the [Viewing lens details for a workload in AWS WA Tool](#lenses-details) page.

**Disclaimer**  
By sharing your custom lenses with other AWS accounts, you acknowledge that AWS will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own AWS account or terminate your AWS account.

#### Adding tags to a custom lens in AWS WA Tool
<a name="lenses-tagging"></a>

**To add tags to a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the custom lens you want to update.

1. In the **Tags** section, choose **Manage Tags**.

1. Select **Add new tag** and enter the **Key** and **Value **for each tag you want to add.

1. Select **Save**. 

To remove a tag, choose **Remove** next to the tag you want to remove. 

#### Deleting a custom lens in AWS WA Tool
<a name="lenses-deleting"></a>

**To delete a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. In the left navigation pane, choose **Custom lenses**.

1. Select the custom lens to be deleted and choose **Delete**.

1. Choose **Delete**.

   Existing workloads with the lens applied are notified that the custom lens has been deleted, but can continue to use it. The custom lens can no longer be applied to new workloads.

**Disclaimer**  
By sharing your custom lenses with other AWS accounts, you acknowledge that AWS will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own AWS account or terminate your AWS account.

#### Lens format specification in AWS WA Tool
<a name="lenses-format-specification"></a>

Lenses are defined using a specific JSON format. When you start to create a custom lens, you have the option to download a template JSON file. You can use this file as the basis for your custom lenses as it defines the basic structure for the pillars, questions, best practices, and improvement plan.

##### Lens section
<a name="lenses-format-lens"></a>

This section defines the attributes for the custom lens itself. This is its name and description.
+ `schemaVersion`: The version of the custom lens schema to use. Set by the template, do not change.
+ `name`: Name of the lens. The name can be up to 128 characters. 
+ `description`: Text description of the lens. This text is displayed when selecting lenses to add during workload creation, or when selecting a lens to apply to an existing workload later. The description can be up to 2048 characters.

```
    "schemaVersion": "2021-11-01",
    "name": "{{Company Policy ABC}}",
    "description": "{{This lens provides a set of specific questions to assess compliance with company policy ABC-2021 as revised on 2021/09/01.}}",
```

##### Pillars section
<a name="lenses-format-pillars"></a>

This section defines the pillars associated with the custom lens. You can map your questions to the pillars of the AWS Well-Architected Framework, define your own pillars, or both.

You can define up to 10 pillars in a custom lens.
+ `id`: ID for the pillar. The ID can be between 3 and 128 characters and contain only alphanumeric and underscore ("\_") characters. The IDs used in a pillar must be unique. 

  When mapping your questions to the pillars of the Framework, use the following IDs:
  + `operationalExcellence`
  + `security`
  + `reliability`
  + `performance`
  + `costOptimization`
  + `sustainability`
+ `name`: Name of the pillar. The name can be up to 128 characters.

```
     "pillars": [
        {
            "id": "{{company_Privacy}}",
            "name": "{{Privacy Excellence}}",
            .
            .
            .
        },
        {
            "id": "{{company_Security}}",
            "name": "{{Security}}",
            .
            .
            .
        }
     ]
```

##### Questions section
<a name="lenses-format-questions"></a>

This section defines the questions associated with a pillar.

You can define up to 20 questions in a pillar in a custom lens.
+ `id`: ID for the question. The ID can be from 3 to 128 characters and contain only alphanumeric and underscore ("\_") characters. The IDs used in a question must be unique. 
+ `title`: Title of the question. The title can be up to 128 characters.
+ `description`: Describes the question in more detail. The description can be up to 2048 characters.
+ `helpfulResource displayText`: Optional. Text that provides helpful information about the question. The text can be up to 2048 characters. Must be specified if `helpfulResource url` is specified. 
+ `helpfulResource url`: Optional. A URL resource that explains the question in more detail. The URL must start with `http://` or `https://`.

**Note**  
 When syncing a custom lens workload to Jira, questions display both the "id" and "title" of the question.   
 The format used in Jira tickets is `[ QuestionID ] QuestionTitle`. 

```
"questions": [
    {
        "id": "{{privacy01}}",
        "title": "{{How do you ensure HR conversations are private?}}",
        "description": "{{Career and benefits discussions should occur on secure channels only and be audited regularly for compliance.}}",
        "helpfulResource": {
            "displayText": "{{This is helpful text for the first question}}",
            "url": "{{https://example.com/poptquest01_help.html}}"
        },
        .
        .
        .
    },
    {
        "id": "{{privacy02}}",
        "title": "{{Is your team following the company privacy policy?}}",
        "description": "{{Our company requires customers to opt-in to data use and does not disclose customer data to third parties either individually or in aggregate.}}",
        "helpfulResource": {
            "displayText": "{{This is helpful text for the second question}}",
            "url": "{{https://example.com/poptquest02_help.html}}"
        },
        .
        .
        .
    }
]
```

##### Choices section
<a name="lenses-format-choices"></a>

This section defines the choices that are associated with a question.

You can define up to 15 choices for a question in a custom lens.
+ `id`: ID for the choice. The ID can be between 3 and 128 characters and contain only alphanumeric and underscore ("\_") characters. A unique ID must be specified for each choice in a question. Adding a choice with a suffix of `_no` will act as a `None of these` choice for the question. 
+ `title`: Title of the choice. The title can be up to 128 characters.
+ `helpfulResource displayText`: Optional. Text that provides helpful information about a choice. The text can be up to 2048 characters. Must be included if `helpfulResource url` is specified.
+ `helpfulResource url`: Optional. A URL resource that explains the choice in more detail. The URL must start with `http://` or `https://`.
+ `improvementPlan displayText`: Text that describes how a choice can be improved upon. The text can be up to 2048 characters. An `improvementPlan` is required for each choice, except for a `None of these` choice.
+ `improvementPlan url`: Optional. A URL resource that can help with improvement. The URL must start with `http://` or `https://`.
+ `additionalResources type`: Optional. The type of additional resources. Value can be either `HELPFUL_RESOURCE` or `IMPROVEMENT_PLAN`.
+ `additionalResources content`: Optional. Specifies the `displayText` and `url` values for the additional resource. Up to five additional helpful resources and up to five additional improvement plan items can be specified for a choice.
  + `displayText`: Optional. Text that describes the helpful resource or improvement plan. The text can be up to 2048 characters. Must be included if `url` is specified.
  + `url`: Optional. A URL resource for the helpful resource or improvement plan. The URL must start with `http://` or `https://`.

**Note**  
 When syncing a custom lens workload to Jira, choices display the "id" of the question and choice, as well as the "title" of the choice.   
 The format used is `[ QuestionID | ChoiceID ] ChoiceTitle`. 

```
    "choices": [
         {
             "id": "{{choice_1}}",
             "title": "{{Option 1}}",
             "helpfulResource": {
                 "displayText": "{{This is helpful text for the first choice}}",
                 "url": "{{https://example.com/popt01_help.html}}"
             },
             "improvementPlan": {
                 "displayText": "{{This is text that will be shown for improvement of this choice.}}",
                 "url": "{{https://example.com/popt01_iplan.html}}"
             }
         },
         {
             "id": "{{choice_2}}",
             "title": "{{Option 2}}",
             "helpfulResource": {
                 "displayText": "{{This is helpful text for the second choice}}",
                 "url": "{{https://example.com/hr_manual_CORP_1.pdf}}"
             },
             "improvementPlan": {
                 "displayText": "{{This is text that will be shown for improvement of this choice.}}",
                 "url": "{{https://example.com/popt02_iplan_01.html}}"
             },
             "additionalResources":[
                {
                  "type": "HELPFUL_RESOURCE",
                  "content": [
                    {
                      "displayText": "{{This is the second set of helpful text for this choice.}}",
                      "url": "{{https://example.com/hr_manual_country.html}}"
                    },
                    {
                      "displayText": "{{This is the third set of helpful text for this choice.}}",
                      "url": "{{https://example.com/hr_manual_city.html}}"
                    }
                  ]
                },
                {
                  "type": "IMPROVEMENT_PLAN",
                  "content": [
                    {
                      "displayText": "{{This is additional text that will be shown for improvement of this choice.}}",
                      "url": "{{https://example.com/popt02_iplan_02.html}}"
                    },
                    {
                      "displayText": "{{This is the third piece of improvement plan text.}}",
                      "url": "{{https://example.com/popt02_iplan_03.html}}"
                    }
                    {
                      "displayText": "{{This is the fourth piece of improvement plan text.}}",
                      "url": "{{https://example.com/popt02_iplan_04.html}}"
                    }
                  ]
                }
              ]
         },
         {
              "id": "option_no",
              "title": "None of these",
              "helpfulResource": {
                "displayText": "{{Choose this if your workload does not follow these best practices.}}",
                "url": "{{https://example.com/popt02_iplan_none.html}}"
              }
              
            }
```

##### Risk Rules section
<a name="lenses-format-risk-rules"></a>

This section defines how the choices selected determine the risk level.

You can define a maximum of three risk rules per question, one for each level of risk.
+ `condition`: A Boolean expression of the choices that maps to a risk level for the question, or `default`.

  There must be a `default` risk rule for each question.
+ `risk`: Indicates the risk associated with the condition. Valid values are `HIGH_RISK`, `MEDIUM_RISK`, and `NO_RISK`.

The order of your risk rules is significant. The first `condition` that evaluates to `true` sets the risk for the question. A common pattern for implementing risk rules is to start with your least risky (and typically most granular) rules and work your way down to your most risky (and least specific) rules.

For example:

```
 "riskRules": [
       {
         "condition": "{{choice_1 && choice_2 && choice_3}}",
         "risk": "{{NO_RISK}}"   
       },
       {
         "condition": "{{((choice_1 || choice_2) && choice_3) || (!choice_1 && choice_3)}}",
         "risk": "{{MEDIUM_RISK}}"
       },
       {
         "condition": "{{default}}",
         "risk": "{{HIGH_RISK}}"
       }
 ]
```

If the question has three choices (`choice_1`, `choice_2`, and `choice_3`), these risk rules result in the following behavior:
+ If all three choices are selected, there is no risk.
+ If either `choice_1` or `choice_2` is selected **and** `choice_3` is selected, there is medium risk.
+ If `choice_1` is **not** selected but `choice_3` is selected, there is also medium risk.
+ If none of these prior conditions were true, there is high risk.

### Lens upgrades in AWS WA Tool
<a name="lens-upgrades"></a>

The AWS Well-Architected Framework Lens and other lenses provided by AWS are updated as new services are introduced, existing best practices for cloud-based systems are refined, and new best practices are added. When a new version of a lens is made available, AWS WA Tool is upgraded to reflect the latest best practices. Any new workloads that are defined use the new version of the lens.

A lens upgrade also occurs when a custom lens that you have applied to a workload or a review template has a new major version published.

A lens upgrade can consist of any combination of:
+ Adding new questions or best practices
+ Removing old questions or practices that are no longer recommended
+ Updating existing questions or best practices 
+ Adding or removing pillars

Your answers to existing questions are retained.

**Note**  
You cannot undo a lens upgrade. After a workload has been upgraded to the latest lens version, you cannot go back to the previous version of the lens.

#### Determining which lens to upgrade in AWS WA Tool
<a name="lenses-selecting"></a>

You can find which workloads aren't using the most current lens version by viewing the **Notifications** page. 

The following information is displayed on the **Notifications** page for each workload:

**Resource**  
The name of the workload or review template.

**Resource type**  
The type of resource. This can be either **Workload** or **Review template**.

**Associated resource**  
The name of the lens.

**Notification type**  
The type of upgrade notification.  
+ **Not current** – The workload is using a version of the lens that is no longer current. Upgrade to the current lens version for better guidance.
+ **Deprecated** – The workload is using a version of the lens that no longer reflects best practices. Upgrade to the current lens version.
+ **Deleted** – The workload is using a lens that has been deleted by its owner.

**Version in use**  
The lens version currently used for the workload.

**Current available version**  
The lens version available for upgrade, or **None** if the lens has been deleted.

To upgrade the lens associated with a workload, select the workload and choose **Upgrade lens version**.

#### Upgrading a lens in AWS WA Tool
<a name="lenses-upgrading"></a>

Lenses can be upgraded for workloads and review templates.

**Note**  
You can't undo a lens upgrade. After a workload or review template has been upgraded to the latest lens version, you can't go back to the previous version of the lens.

**Upgrading a lens for a workload**

1. On the **Notifications** page, select a workload to upgrade, and choose **Upgrade lens version**. Information about what changed in each pillar is displayed.
**Note**  
You can also choose **View available upgrades** from the workload **Overview** tab.

1. Before upgrading a lens for a workload, a milestone is created to save the state of your existing workload for future reference. Enter a unique name for the milestone in the **Milestone name** field.

1. Select the **Confirmation** box next to **I understand and accept these changes** and choose **Save**.

Once the lens is upgraded, you can view the previous version of the lens from the **Milestones** tab. 

**Upgrading a lens for a review template**

1. To upgrade the lens for a review template, choose

1. On the **Notifications** page, select a review template to upgrade, and choose **Upgrade lens version**. Information about what changed in each pillar is displayed.
**Note**  
You can also choose **View available upgrades** from the review template **Overview** tab.

1. Select the **Confirmation** box next to **I understand and accept these changes** and choose **Upgrade and edit template answers** to adjust answers to best practice questions for your review template, or **Upgrade** to upgrade the lens without adjusting your template answers.

### Lens Catalog for AWS WA Tool
<a name="lens-catalog"></a>

 The **Lens Catalog** is a collection of official, AWS lenses created for AWS Well-Architected Tool that offer up-to-date technology and industry-focused best practices. These lenses are available to all users and do not require any additional installation to use. 

 The following table describes all AWS official lenses currently available in the Lens Catalog. 


| Lens name | Description | 
| --- | --- | 
| AWS Well-Architected Framework | Applied by default to all workloads. Collection of architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud. | 
| Connected Mobility | Best practices for integrating technology into transportation systems and enhancing the overall mobility experience. | 
|  Container Build  |  Provides best practices on the container design and build process.  | 
|  Data Analytics  |  Contains insights that AWS has gathered from real-world case studies, and helps you learn the key design elements of Well-Architected analytics workloads, along with recommendations for improvement.  | 
| DevOps | Describes a structured approach that organizations of all sizes can follow to cultivate a high-velocity, security-focused culture capable of delivering substantial business value using modern technologies and DevOps best practices. | 
| Financial Services Industry | Best practices for architecting your Financial Services Industry workloads on AWS. | 
| Generative AI | Best practices for architecting your generative AI workloads on AWS. | 
| Government |  Best practices for designing and delivering government services on AWS. | 
|  Healthcare Industry  |  Best practices and guidance for how to design, deploy, and manage your healthcare workloads in the AWS Cloud.  | 
|  IoT  |  Best practices for managing your Internet of Things (IoT) workloads in AWS.  | 
|  Mergers and Acquisitions  | Best practices for workload integration and migration to the cloud during mergers and acquisitions. | 
|  Machine Learning  |  Best practices for managing your Machine Learning resources and workloads in AWS.  | 
| Migration | Best practices for how to migrate to the AWS Cloud. | 
| SaaS | Focused on designing, deploying, and architecting your software as a service (SaaS) workloads in the AWS Cloud. | 
|  SAP  |  Design principles and best practices for SAP workloads in the AWS Cloud.  | 
| Serverless Applications | Best practices for build serverless workloads on AWS. Covers scenarios such as RESTful microservices, mobile app backends, stream processing, and web applications.  | 

## Review templates in AWS WA Tool
<a name="review-templates"></a>

You can create review templates in AWS WA Tool that contain pre-filled answers for Well-Architected Framework and custom lens best practice questions. Well-Architected review templates reduce the need to manually fill in the same answers for best practices that are common across multiple workloads when performing a Well-Architected review, and they help drive consistency and standardization of best practices across teams and workloads.

You can [create a review template](#creating-a-review-template) to answer common best practice questions or create notes, which can be shared with another IAM user or account, or an organization or organizational unit in the same AWS Region. You can [define a workload from a review template](#define-workload-from-template), which helps scale common best practices and reduce redundancy across your workloads.

### Creating a review template in AWS WA Tool
<a name="creating-a-review-template"></a>

**To create a review template**

1. Select **Review templates** in the left navigation pane.

1. Choose **Create template**.

1. On the **Specify template details** page, provide a **Name** and **Description** for your review template.

1. (Optional) In the **Template notes** and **Tags** sections, add any template notes or tags you want to associate with the review template. Any notes added are applied to all workloads that use the review template, whereas tags are specific to the review template.

   For more information on tags, see [Tagging your AWS WA Tool resources](#tagging).

1. Choose **Next**.

1. On the **Apply lenses** page, select the lenses that you want to apply to the review template. The maximum number of lenses that can be applied is 20. 

    Lenses can be selected from **Custom lenses**, **Lens Catalog**, or both. 
**Note**  
Lenses that are shared with you cannot be applied to the review template.

1. Choose **Create template**.

**To begin answering questions for the review template you just created**

1. On the template **Overview** tab, in the **Start answering questions** information alert, select the lens in the **Answer questions** dropdown.
**Note**  
You can also go to the **Lenses** section, select the lens, and choose **Answer questions**.

1. For each lens you have applied to your review template, answer the applicable questions and choose **Save and exit** when done.

Once your review template is created, you can define a new workload from it. 

The **Overview** tab of the review template should reflect the total number of **Questions answered** in the **Template details** section, and the **Questions answered** for each lens in the **Lenses** section.

### Editing a review template in AWS WA Tool
<a name="editing-review-templates"></a>

**To edit a review template**

1. Select **Review templates** in the left navigation pane.

1. Select the name of the review template you want to edit.

1. To update the **Name**, **Description**, or **Template notes** for the review template, choose **Edit** in the **Template details** section of the **Overview** tab.

   1. Make your changes to the **Name**, **Description**, or **Template notes**.

   1. Choose **Save template** to update the review template with your changes.

1. To update which lenses are applied to the review template, in the **Lenses** section of the **Overview** tab, choose **Edit applied lenses**.

   1.  Select or deselect the checkboxes of the lenses you want to add or remove.

       Lenses can be selected or deselected from **Custom lenses**, **Lens Catalog**, or both. 

   1.  Choose **Save template** to save your changes. 

1. To update the answers to best practice questions on the lens, in the **Lenses** section of the **Overview** tab, select the name of the lens.

   1. In the **Lens overview** section, choose **Answer questions**.
**Note**  
Optionally, you can select the name of the lens under the **Review templates** dropdown in the left navigation pane to get to the **Lens overview** section.

   1. Select or deselect the checkboxes next to the best practice answers you want to change.

   1. Choose **Save and exit** to save your changes.

### Sharing a review template in AWS WA Tool
<a name="sharing-review-templates"></a>

Review templates can be shared with users or accounts, or they can be shared with an entire organization or organizational unit.

**To share a review template**

1. Select **Review templates** in the left navigation pane.

1. Select the name of the review template you want to share.

1. Choose the **Shares** tab.

1. To share to a user or account, choose **Create** and select **Share with IAM users or accounts**. In the **Send invitations** box, specify the user or account IDs, and choose **Create**.

1. To share to an organization or organizational unit, choose **Create** and select **Share with Organizations**. To share to an entire organization, select **Grant permissions to the entire Organization**. To share with an organizational unit, select **Grant permissions to individual Organizational Units**, specify the organizational unit in the box, and choose **Create**.

**Important**  
Before sharing a profile with an organization or organizational unit (OU), you must [enable AWS Organizations access](#getting-started-sharing-orgs).

### Defining a workload from a template in AWS WA Tool
<a name="define-workload-from-template"></a>

You can define a workload from a review template that you created or a review template that has been shared with you. You cannot define a new workload from a review template that has been deleted, and if the review template contains an outdated version of a lens, you must upgrade the review template before you can define a new workload from it. For information on how to upgrade a review template, see [Upgrading a lens in AWS WA Tool](#lenses-upgrading).

**Note**  
To define a workload from a review template, you must have IAM permissions to create a workload enabled:`wellarchitected:CreateWorkload`, as well as the following review template permissions: `wellarchitected:GetReviewTemplate`, `wellarchitected:GetReviewTemplateAnswer`, `wellarchitected:ListReviewTemplateAnswers`, and `wellarchitected:GetReviewTemplateLensReview`. For more information about IAM permissions, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

**To define a workload from a review template**

1. Select **Review templates** in the left navigation pane.

1. Select the name of the review template you want to define a workload from.

1. Choose **Define workload from template**.
**Note**  
You can also choose **Define from review template** from the **Define workload** dropdown on the **Workloads** page.

1. On the **Select review template** step, select the review template card, and choose **Next**.

1. On the **Specify properties** step, fill out required fields for the workload properties, and choose **Next**. For more detail, see [Defining a workload in AWS WA Tool](#define-workload).

1. (Optional) On the **Apply Profile** step, associate a profile with the workload by selecting an existing profile, searching for the profile name, or choosing **Create profile** to [create a profile](#tool-creating-a-profile). Choose **Next**.

   [Well-Architected profiles](#tool-profiles) and review templates can be used in tandem. The questions that are pre-filled in your review template remain answered in the workload, and the questions are prioritized based on your profile.

1. (Optional) On the **Apply lenses** step, you may choose to apply additional lenses from **Custom lenses** or **Lens catalog** that were not already applied to the review template.

1. Choose **Define workload**.

### Deleting a review template in AWS WA Tool
<a name="deleting-review-templates"></a>

**To delete a review template**

1. Select **Review templates** in the left navigation pane.

1. In the **Review templates** section, choose the review template you want to delete and in the **Actions** dropdown, select **Delete**.
**Note**  
You may also select the name of the template and choose **Delete** from the review template **Overview** tab.

1. In the **Delete** review template dialog box, enter the name of the review template in the field to confirm deletion.

1. Choose **Delete**.

You cannot create a new workload from a review template that has been deleted. If you have shared a review template that you deleted with other IAM users, accounts, or organizations, they will not be able to create workloads from it. 

## Tool profiles
<a name="tool-profiles"></a>

You can create profiles to provide your business context, and identify goals you'd like to accomplish when performing a Well-Architected review. AWS Well-Architected Tool uses the information gathered from your profile to help you focus on a prioritized list of questions that are relevant to your business during the workload review. Attaching a profile to your workload also helps you see which risks are prioritized for you to address with your improvement plan. 

**Note**  
AWS Well-Architected Agent also has a feature named profiles. AWS WA Agent profiles define the scope and optimization targets for AI-powered infrastructure analysis, and are unrelated to AWS WA Tool profiles. For information about AWS WA Agent profiles, see [AWS Well-Architected Agent Concepts and terminology](#agent-concepts).

You can [create a profile](#tool-creating-a-profile) from the **Profiles** page and associate it to a new workload, or you can [add a profile to an existing workload](#tool-adding-profiles-to-workloads). 

### Creating a profile
<a name="tool-creating-a-profile"></a>

**To create a profile**

1. Select **Profiles** in the left navigation pane.

1. Choose **Create profile**.

1. In the **Profile properties** section, provide a **Name** and **Description** for your profile.

1. To refine the information prioritized for your business in the workload review and improvement plan, select the answers that are most relevant to your business in the **Profile questions** section.

1. (Optional) In the **Tags** section, add any tags you want to associate with the profile.

   For more information on tags, see [Tagging your AWS WA Tool resources](#tagging).

1. Choose **Save**. A success message appears when the profile is created successfully.

When a profile is created, the profile overview is displayed. The overview shows the data associated with the profile, including the name, description, ARN, created and updated dates, and the answers to the profile questions. From the profile overview page you can edit, delete, or share your profile.

### Editing a profile in AWS WA Tool
<a name="tool-editing-profiles"></a>

**To edit a profile**

1. Select **Profiles** in the left navigation pane, or choose **View profile** from the **Profiles** section of the workload.

1. Select the name of the profile you want to update.

1. Choose **Edit** on the **Profile overview** page.

1. Make any necessary updates to the profile questions.

1. Choose **Save**.

### Sharing a profile in AWS WA Tool
<a name="tool-sharing-profiles"></a>

Profiles can be shared with users or accounts, or they can be shared with an entire organization or organizational unit.

**To share a profile**

1. Select **Profiles** in the left navigation pane.

1. Select the name of the profile you want to share.

1. Choose the **Shares** tab.

1. To share to a user or account, choose **Create** and select **Create shares to IAM users or accounts**. In the **Send invitations** box, specify the user or account IDs, and choose **Create**.

1. To share to an organization or organizational unit, choose **Create** and select **Create shares to Organizations**. To share to an entire organization select **Grant permissions to the entire Organization**. To share with an organizational unit, select **Grant permissions to individual Organization Units**, specify the organizational unit in the box, and choose **Create**.

**Important**  
Before sharing a profile with an organization or organizational unit (OU), you must [enable AWS Organizations access](#getting-started-sharing-orgs).

### Adding a profile to a workload in AWS WA Tool
<a name="tool-adding-profiles-to-workloads"></a>

You can add a profile to an existing workload, or when defining a workload, to speed up the workload review process. AWS WA Tool uses the information gathered from your profile to prioritize questions in the workload review that are relevant to your business. 

For more information on adding a profile when defining a workload, see [Defining a workload in AWS WA Tool](#define-workload). 

**To add a profile to an existing workload**

1. Select **Workloads** in the left navigation pane, and select the name of the workload you want to associate with a profile.
**Note**  
Only one profile can be associated with a workload.

1. In the **Profile** section, choose **Add profile**.

1. Select the profile you want to apply to the workload from the list of available profiles, or choose **Create profile**. For more information, see [Creating a profile](#tool-creating-a-profile).

1. Choose **Save**.

The **Workload overview** displays a count of prioritized questions answered and prioritized risks based on the information in the associated profile. Choose **Continue reviewing** to address the prioritized questions in the workload review. For more information, see [Documenting a workload in AWS WA Tool](#start-workflow-review).

The **Profile** section displays the name, description, ARN, version, and last updated date for the profile associated with the workload.

### Removing a profile from a workload in AWS WA Tool
<a name="tool-removing-profiles-from-workloads"></a>

Removing a profile from the workload reverts the workload to the version prior to when the profile was associated with it, and workload review questions and risks are no longer prioritized.

**To remove a profile from a workload**

1. From the **Profiles** section of the workload, choose **Remove**.

1. To confirm removal, enter the name of the profile in the text input field.

1. Choose **Remove**.

A notification that the profile has been successfully removed from the workload is displayed. Removing a profile reverts the workload to the version prior to when the profile was associated with it, and workload review questions and risks are no longer prioritized.

### Deleting a profile from AWS WA Tool
<a name="tool-deleting-profiles"></a>

If you created a profile, you can delete the profile from the list of profiles available in AWS WA Tool. 

Deleting a profile from the **Profiles** page does not remove the profile from any associated workloads. You can continue using profiles that were shared and associated with a workload before deletion, however, no new workloads can be associated with a deleted profile. [Profile notifications](#profiles-notifications) are sent to workload owners using deleted profiles. 

**Disclaimer**  
By sharing your profiles with other AWS accounts, you acknowledge that AWS will make your profiles available to those other accounts. Those other accounts may continue to access and use your shared profiles even if you delete the profile from your own AWS account or terminate your AWS account.

**To delete a profile from your list of profiles**

1. Select **Profiles** in the left navigation pane.

1. Select the name of the profile you want to remove.

1. Choose **Delete**.

1. To confirm removal, enter the profile name in the text input field.

1. Choose **Delete**.

If you want to keep a profile in your **Profiles** list, but remove it from a workload, see [Removing a profile from a workload in AWS WA Tool](#tool-removing-profiles-from-workloads).

## AWS Well-Architected Tool Connector for Jira
<a name="jira"></a>

 You can use the AWS Well-Architected Tool Connector for Jira to link your Jira account with AWS Well-Architected Tool and sync improvement items from your workloads to Jira projects to help you create a closed-loop mechanism in implementing improvements. 

 The connector provides both Automatic and Manual syncing. For more detail, see [Configuring the connector.](#configuring-jira) 

 The connector can be set up at the account level and the workload level, with the option to override your account-level settings per workload. At the workload level, you can also choose to exclude a workload from syncing entirely. 

 You can choose to have improvement items synced to the default WA Jira project, or specify an existing project key to sync to. At the workload level, you can sync each workload to a unique Jira project if necessary. 

**Note**  
 The connector only supports scrum and kanban projects in Jira. 

 When improvement items are synced to Jira, they are organized in the following way: 
+  **Project:** WA (or existing project you specify) 
+  **Epic:** Workload 
+  **Task:** Question 
+  **Sub-task:** Best practice 
+  **Label:** Pillar 

 After you set up Jira account syncing in the **Settings** page, you can [configure the Jira connector](#configuring-jira) and [sync improvement items to your Jira account](#syncing-workload). 

### Setting up the connector
<a name="setting-up-jira"></a>

**To install the connector**
**Note**  
 All of the following steps are performed in your Jira account, not in your AWS account. 

1.  Log in to your Jira account. 

1.  In the top navigation bar, choose **Apps**, then select **Explore more apps**. 

1. In the **Discover apps and integrations for Jira** page, enter AWS Well-Architected. Then, choose the **AWS Well-Architected Tool Connector for Jira**.

1. In the app page, choose **Get app**.

1.  In the **Add to Jira** pane, choose **Get it now**. 

1.  After the app installs, to complete setup, choose **Configure**. 

1.  In the **AWS Well-Architected Tool Configuration** page, choose **Connect a new AWS account**. 

1.  Enter your **AccessKeyId** and **Secret Key**. Optional: Enter your **Session Token**. Then, choose **Connect**. 
**Note**  
 Make sure your account has the permission `wellarchitected:ConfigureIntegration`. This permissions is required to add AWS accounts to Jira.   
 Multiple AWS accounts can be connected to AWS WA Tool. 
**Note**  
 As a security best practice, its highly recommended to use short-term IAM credentials. For detail on creating an **AccessKeyId** and **Secret Key** for your AWS account, see [Managing access keys (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey), and for detail on using short term credentials, see [Requesting temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html). 

1.  For **Regions**, select the AWS Regions you want to connect. Then, choose **Connect**. 

 

 **Jira project setup** 

 When using custom projects, make sure you have the following issue types in your project setup: 
+  **Scrum:** Epic, Story, Subtask 
+  **Kanban:** Epic, Task, Subtask 

 For detail on managing issue types, see [Atlassian Support \| Add, edit, and delete an issue type](https://support.atlassian.com/jira-cloud-administration/docs/add-edit-and-delete-an-issue-type/). 

 

**To check the status of the connector in AWS Well-Architected Tool**

1.  Log in to your AWS account and navigate to AWS Well-Architected Tool. 

1.  Select **Settings** in the left navigation pane. 

1.  In the **Jira account syncing** section, under **Jira app connection status**, check for the **Configured** status. 

 The connector is now set up and ready to be configured. To configure Jira sync settings at the account and workload level, see [Configuring the connector](#configuring-jira). 

### Configuring the connector
<a name="configuring-jira"></a>

 With the AWS Well-Architected Tool Connector for Jira, you can configure Jira syncing at the account level, the workload level, or both. You can configure workload-level Jira settings independent of account-level settings, or override your account-level settings on a specific workload to specify the workload's sync behavior. You can also configure Jira settings when [Defining a workload](#define-workload). 

 The connector provides two sync methods: **Automatic** and **Manual** sync. In both sync methods, changes that are made in AWS WA Tool are reflected in your Jira project, and changes made in Jira are synced back to AWS WA Tool. 

**Important**  
 By using Automatic sync, you consent to AWS WA Tool modifying your workload in response to changes in Jira.   
 If you have sensitive information you do not wish to sync to Jira, do not input this information into the **Notes** field in your workloads. 
+  **Automatic sync:** The connector automatically updates your Jira project and your workload each time a question is updated, including selecting or deselecting a best practice and completing a question. 
+  **Manual sync:** You must choose **Sync with Jira** in the workload dashboard when you want to sync improvement items between Jira and the AWS WA Tool. You can also choose which specific pillars and questions you want to sync. For more detail, see [Syncing a workload](#syncing-workload). 

**To configure the connector at the account level**

1.  Select **Settings** in the left navigation pane. 

1.  In the **Jira account syncing** pane, choose **Edit**. 

1.  For **Sync type**, select one of the following: 

   1.  To automatically sync workloads when changes are made, select **Automatic**. 

   1.  To manually choose when to sync workloads, select **Manual**. 

1.  By default, the connector creates a **WA** Jira project. To specify your own Jira project key, do the following: 

   1.  Select **Override default Jira project key**. 

   1.  Enter your **Jira project key**. 
**Note**  
 The specified **Jira project key** is used for all workloads unless you change the project at the workload level. 

1.  Choose **Save settings**. 

**To configure the connector at the workload level**

1.  Select **Workloads** in the left navigation pane, and select the name of the workload you want to configure. 

1.  Choose **Properties**. 

1.  In the **Jira** pane, choose **Edit**. 

1.  To configure the workload's Jira settings, select **Override account level settings**. 
**Note**  
 **Override account level settings** must be selected in order to apply workload-specific settings. 

1.  For **Sync override**, select one of the following: 

   1.  To exclude the workload from Jira sync, select **Do not sync workload**. 

   1.  To manually choose when to sync the workload, select **Sync workload - Manual**. 

   1.  To sync workload changes automatically, select **Sync workload - Automatic**. 

1.  (Optional) For **Jira project key**, enter the project key to sync the workload to. This project key can be different from your account-level project key. 

    If you don't specify a project key, the connector creates a **WA** Jira project. 

1.  Choose **Save**. 

 For detail on performing a manual sync, see [Syncing a workload](#syncing-workload). 

### Syncing a workload
<a name="syncing-workload"></a>

 For Automatic syncing, the connector automatically syncs improvement items when you update a workload (for example, when you complete a question or select a new best practice). 

 In both Manual and Automatic syncing, any changes made in Jira (like completing a question or best practice) are synced back to AWS Well-Architected Tool. 

**To manually sync a workload**

1.  When you are ready to sync your workload to Jira, select **Workloads** in the left navigation pane. Then, select the workload you want to sync. 

1.  In the workload overview, choose **Sync with Jira**. 

1.  Select the lens you want to sync. 

1.  For **Questions to sync to Jira**, select the questions or entire pillars you want to sync to the Jira project. 

   1.  For any questions you want to remove, select the **X** icon next to the question title. 

1.  Choose **Sync**. 

### Uninstalling the connector
<a name="uninstalling-jira"></a>

 To fully uninstall the AWS Well-Architected Tool Connector for Jira, perform the following tasks: 
+  Turn off Jira sync in any workloads that override account-level sync settings 
+  Turn off Jira sync at the account level 
+  Unlink your AWS account in Jira 
+  Uninstall the connector from your Jira account 

**To turn off the connector at the account level**
**Note**  
 The following steps are performed in your AWS account. 

1.  Select **Settings** in the left navigation pane. 

1.  In the **Jira account syncing** section, choose **Edit**. 

1.  Clear the **Turn on Jira account syncing** option. 

1.  Choose **Save settings**. 

**To unlink an AWS account**
**Note**  
 All of the following steps are performed in your Jira account, not in your AWS account. 

1.  Log in to your Jira account. 

1.  In the top navigation bar, choose **Apps**, then select **Manage your apps**. 

1.  Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**, then choose **Configure**. 

1.  In the AWS Well-Architected Tool Configuration pane, to unlink an AWS account, choose **X** under **Actions**. 

**To uninstall the connector**
**Note**  
 All of the following steps are performed in your Jira account, not in your AWS account.   
 We recommend verifying that all connected AWS accounts are unlinked in the configuration of the connector prior to uninstalling the connector. 

1.  Log in to your Jira account. 

1.  In the top navigation bar, choose **Apps**, then select **Manage your apps**. 

1.  Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**. 

1.  Choose **Uninstall**, then choose **Uninstall app**. 

## Milestones
<a name="milestones"></a>

A milestone records the state of a workload at a particular point in time.

Save a milestone after you initially complete all the questions associated with a workload. As you change your workload based on items in your improvement plan, you can save additional milestones to measure progress.

A best practice is to save a milestone every time you make improvements to a workload.

### Saving a milestone
<a name="milestones-save"></a>

A milestone records the current state of a workload. The owner of a workload can save a milestone at any time.

**To save a milestone**

1. From the workload details page, choose **Save milestone**.

1. In the **Milestone name** box, enter a name for your milestone.
**Note**  
The name must be between 3 and 100 characters. At least three characters must not be spaces. Milestone names associated with a workload must be unique. Spaces and capitalization are ignored when checking for uniqueness.

1. Choose **Save** to save the milestone.

After a milestone is saved, you cannot change the workload data that was recorded. When you delete a workload, its associated milestones are also deleted.

### Viewing milestones
<a name="milestones-view"></a>

You can view milestones for a workload in the following ways:
+ On the workload details page, choose **Milestones** and choose the milestone you want to view.
+ On the **Dashboard** page, choose the workload and in the **Milestones** section, choose the milestone you want to view.

### Generating a milestone report
<a name="milestone-report"></a>

You can generate a milestone report. The report contains the responses to the workload questions, your notes, and any high and medium risks that were present when the milestone was saved.

A report enables you to share details about the milestone with others who do not have access to the AWS Well-Architected Tool. 

**To generate a milestone report**

1. Select the milestone in one of the following ways.
   + From the workload details page, choose **Milestones** and choose the milestone.
   + From the **Dashboard** page, choose the workload with the milestone that you want to report on. In the **Milestones** section, choose the milestone.

1. Choose **Generate report** to generate a report.

   The PDF file is generated and you can download or view it.

## Share invitations
<a name="invitations"></a>

A share invitation is a request to share a workload, custom lens, or review template owned by another AWS account. A workload or lens can be shared with all users in an AWS account, individual users, or both. 
+ If you accept a workload invitation, the workload is added to your **Workloads** and **Dashboard** pages. 
+ If you accept a custom lens invitation, the lens is added to your **Custom lenses** page.
+ If you accept a profile invitation, the profile is added to your **Profiles** page.
+ If you accept a review template invitation, the template is added to your **Review templates** page.

If you reject the invitation, it's removed from the list.

**Note**  
Workloads, custom lenses, profiles, and review templates can only be shared within the same AWS Region.

The owner of the workload or custom lens controls who has shared access.

The **Share invitations** page, available from the left navigation, provides information about your pending workload and custom lens invitations.

The following information is displayed for each workload invitation:

**Name**  
The name of the workload, custom lens, or review template to be shared.

**Resource type**  
The type of invitation, either **Workload**, **Custom lens**, **Profiles**, or **Review template**.

**Owner**  
The AWS account ID that owns the workload.

**Permission**  
The permission that you are being granted to the workload.  
+ Read-Only

  Provides read-only access to the workload, custom lens, profiles, or review template.
+ Contributor

  Provides update access to answers and their notes, and read-only access to the rest of the workload. This permission is only available for workloads.

**Permission details**  
Detailed description of the permission.

### Accepting a share invitation
<a name="invitation-accept"></a>



**To accept a share invitation**

1. Select the share invitation to accept.

1. Choose **Accept**.

For workload invitations, the workload is added to the **Workloads** and **Dashboard** pages. For custom lens invitations, the custom lens is added to the **Custom lenses** page. For profile invitations, the profile is added to the **Profiles** page. For review template invitations, the template is added to the **Review templates** page.

You have seven days to accept an invitation. If you do not accept the invitation within seven days, it's automatically expired.

If a user and their AWS account both have accepted workload invitations, the workload invitation for the user determines the user's permission.

### Rejecting a share invitation
<a name="invitation-reject"></a>

**To reject a share invitation**

1. Select the workload or custom lens invitation to reject.

1. Choose **Reject**.

The invitation is removed from the list.

## Notifications
<a name="notifications"></a>

The **Notifications** page displays version differences for workloads and review templates that have lenses and profiles associated with them. You can upgrade to the newest version of a lens or profile for a workload from the Notifications page. 

### Lens notifications
<a name="lenses-notifications"></a>

When a new version of a lens is available, a banner appears at the top of the **Workloads** or **Review templates** page to notify you. If you view a specific workload or review template using an outdated lens, you will also see a banner indicating that a new lens version is available.

Choose **View available upgrades** for a list of workloads or review templates that can be upgraded.

See [Upgrading a lens in AWS WA Tool](#lenses-upgrading) for instructions on upgrading a lens for a workload or a review template. 

When the owner of a shared lens deletes it, if you have a workload associated with the deleted lens, you will receive a notification that you can still use the lens in your existing workload, but you will not be able to add it to new workloads.

### Profile notifications
<a name="profiles-notifications"></a>

There are two types of **Profile notifications**: 
+ Profile upgrade
+ Profile deletion

 When a profile associated with a workload has been edited (for more information, see [Editing a profile in AWS WA Tool](#tool-editing-profiles)), a notification that there is a new version of the profile is displayed in **Profile notifications**.

 When the owner of a shared profile deletes it, if you have a workload associated with the deleted profile, you will receive a notification that you can still use the profile in your existing workload, but you will not be able to add it to new workloads.

**To upgrade a profile version**

1. In the left navigation pane, select **Notifications**.

1. Select the name of the workload from the list on the **Profile notifications** tab, or use the search bar to search by workload name. 

1. Choose **upgrade profile version**.

1. In the **Acknowledgment** section, select the confirmation box for **I understand and accept these changes**.

1. (Optional) If choosing to save a milestone, select the **Save a milestone** box and provide a **Milestone name**.

1. Select **Save**.

Once the profile is upgraded, the latest version number and updated date is displayed in the **Profile** section of the workload. 

See [Tool profiles](#tool-profiles) for more information.

## Dashboard
<a name="dashboard"></a>

The **Dashboard**, available from the left navigation, gives you access to your workloads and their associated medium and high risk issues. You also can include workloads that have been shared with you. The **Dashboard** consists of four sections.
+ **Summary** — Shows the total number of workloads, how many have high and medium risks, and the total number of high and medium risk issues across all workloads.
+ **Well-Architected Framework issues per pillar** — Shows a graphical representation of high and medium risk issues by pillar for all your workloads.
+ **Well-Architected Framework issues per workload** — Shows the high and medium risk issues by pillar for each of your workloads. 
+ **Well-Architected Framework issues by improvement plan item** — Shows the improvement plan items for all your workloads.

### Summary
<a name="dashboard-summary"></a>

This section shows the total number of workloads and the number of workloads with high and medium risk issues across the Well-Architected Framework lens and all other lenses. The total number of high and medium risk issues across all workloads, either owned by or shared with your AWS account, are shown.

Choose **Include workloads shared with me** to have the summary statistics, the consolidated report, and the other dashboard sections reflect both your workloads and workloads that have been shared with you.

Choose **Generate report** to have a consolidated report created for you as a PDF file.

The report name is in the form of: `wellarchitected_consolidatedreport_{{account-ID}}.pdf`.

### Well-Architected Framework issues per pillar
<a name="dashboard-issues-per-pillar"></a>

The **Well-Architected Framework issues per pillar** section shows a graphical representation of the number of high and medium risk issues by pillar for all workloads.

Use the remaining sections of the dashboard to move from one level of detail to the next.

**Note**  
Only issues from the Well-Architected Framework lens are included in this section.

### Well-Architected Framework issues per workload
<a name="dashboard-issues-per-workload"></a>

The **Well-Architected Framework issues per workload** section displays information for each workload.

![Picture showing the issues per workload section of the Dashboard.](https://docs.aws.amazon.com/wellarchitected/latest/userguide/images/dashboard-issues-per-workload.png)


The following information is displayed for each workload:

**Name**  
The name of the workload. The number of questions answered, and the number of lenses applied to the workload are also shown.  
Choose the workload name to visit the workload details page and view milestones, improvement plans, and shares.

**Total issues**  
The total number of issues identified by the Well-Architected Framework lens for the workload.  
Choose the number of high or medium risk issues to view the recommended improvement plans for those issues.

**Operational Excellence**  
The number of high risk issues (HRIs) and medium risk issues (MRIs) identified in the workload for the Operational Excellence pillar.

**Security**  
The number of HRIs and MRIs identified for the Security pillar.

**Reliability**  
The number of HRIs and MRIs identified for the Reliability pillar.

**Performance Efficiency**  
The number of HRIs and MRIs identified for the Performance Efficiency pillar.

**Cost Optimization**  
The number of HRIs and MRIs identified for the Cost Optimization pillar.

**Sustainability**  
The number of HRIs and MRIs identified for the Sustainability pillar.

**Last updated**  
Date and time that the workload was last updated.

For each workload, the pillar with the highest number of high risk issues (HRIs) is highlighted.

**Note**  
Only issues from the Well-Architected Framework lens are included in this section.

### Well-Architected Framework issues by improvement plan item
<a name="dashboard-issues-by-plan-item"></a>

The **Well-Architected Framework issues by improvement plan item** section displays the improvement plan items for all your workloads. You can filter the items based on pillar and severity.

The following information is displayed for each improvement plan item:

**Improvement item**  
The name of the improvement plan item.  
Choose the name to show the best practice associated with the improvement plan item.

**Pillar**  
The pillar associated with the improvement item.

**Risk**  
Indicates if the associated issue is high or medium risk.

**Applicable workloads**  
The number of workloads where this improvement plan applies.

Select an improvement plan item to see the applicable workloads.

**Note**  
Only improvement plan items from the Well-Architected Framework lens are included in this section.

## Sharing your AWS WA Tool resources
<a name="sharing"></a>

To share a resource that you own, do the following:
+ [Activate resource sharing within AWS Organizations](#getting-started-sharing-orgs) (optional)
+ [Share a workload](#workloads-sharing)
+ [Share a custom lens](#lenses-sharing)
+ [Share a profile](#tool-sharing-profiles)
+ [Share a review template](#sharing-review-templates)

**Notes**  
Sharing a resource makes it available for use by principals outside of the AWS account that created the resource. Sharing doesn't change any permissions that apply to the resource in the account that created it.
AWS WA Tool is a Regional service. The principals that you share with can access resource shares in only the AWS Regions in which they were created.
To share resources in a Region introduced after March 20, 2019, both you and the shared AWS account must enable the Region in the AWS Management Console. For more information, refer to [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

### Activate resource sharing within AWS Organizations
<a name="getting-started-sharing-orgs"></a>

When your account is managed by AWS Organizations, you can take advantage of that to share resources more easily. With or without Organizations, a user can share with individual accounts. However, if your account is in an organization, then you can share with individual accounts, or with all accounts in the organization or in an OU without having to enumerate each account.

To share resources within an organization, you must first use the AWS WA Tool console or AWS Command Line Interface (AWS CLI) to enable sharing with AWS Organizations. When you share resources in your organization, AWS WA Tool doesn't send invitations to principals. Principals in your organization gain access to shared resources without exchanging invitations.

When you activate resource sharing within your organization, AWS WA Tool creates a service-linked role called `AWSServiceRoleForWellArchitected`. This role can be assumed by only the AWS WA Tool service, and grants AWS WA Tool permission to retrieve information about the organization it is a member of, by using the AWS managed policy `AWSWellArchitectedOrganizationsServiceRolePolicy`. 

If you no longer need to share resources with your entire organization or OUs, you can disable resource sharing.

**Requirements**
+ You can perform these steps only while signed in as a principal in the organization's management account.
+ The organization must have all features enabled. For more information, see [ Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.

**Important**  
You must turn on sharing with AWS Organizations by using the AWS WA Tool console. This ensures that the `AWSServiceRoleForWellArchitected` service-linked role is created. If you activate trusted access with AWS Organizations by using the AWS Organizations console or the [ enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html) AWS CLI command, the `AWSServiceRoleForWellArchitected` service-linked role isn't created, and you can't share resources within your organization.

**To activate resource sharing within your organization**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

   You must sign in as a principal in the organization's management account.

1. In the left navigation pane, choose **Settings**.

1. Choose **Activate AWS Organizations support**.

1. Choose **Save settings**.

**To disable resource sharing within your organization**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

   You must sign in as a principal in the organization's management account.

1. In the left navigation pane, choose **Settings**.

1. Unselect **Activate AWS Organizations support**.

1. Choose **Save settings**.

## Tagging your AWS WA Tool resources
<a name="tagging"></a>

To help you manage your AWS WA Tool resources, you can assign your own metadata to each resource in the form of *tags*. This topic describes tags and shows you how to create them.

**Topics**
+ [Tag basics](#tag-basics)
+ [Tagging your resources](#tag-resources)
+ [Tag restrictions](#tag-restrictions)
+ [Working with tags using the console](#tag-resources-console)
+ [Working with tags using the API](#tag-resources-api-sdk)

### Tag basics
<a name="tag-basics"></a>

A tag is a label that you assign to an AWS resource. Each tag consists of a *key* and an optional *value*, both of which you define.

Tags enable you to categorize your AWS resources by, for example, purpose, owner, or environment. When you have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned to it. For example, you can define a set of tags for your AWS WA Tool services to help you track each service's owner and stack level. We recommend that you devise a consistent set of tag keys for each resource type.

Tags are not automatically assigned to your resources. After you add a tag, you can edit tag keys and values or remove tags from a resource at any time. If you delete a resource, any tags for the resource are also deleted.

Tags don't have any semantic meaning to AWS WA Tool and are interpreted strictly as a string of characters. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value.

You can work with tags using the AWS Management Console, the AWS CLI, and the AWS WA Tool API.

If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create, edit, or delete tags.

### Tagging your resources
<a name="tag-resources"></a>

You can tag new or existing AWS WA Tool resources.

If you're using the AWS WA Tool console, you can apply tags to new resources when they are created or to existing resources at any time. For existing workloads you can apply tags through the **Properties** tab. For existing custom lenses, profiles, and review templates you can apply tags through the **Overview** tab. 

If you're using the AWS WA Tool API, the AWS CLI, or an AWS SDK, you can apply tags to new resources using the `tags` parameter on the relevant API action or to existing resources using the `TagResource` API action. For more information, see [TagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TagResource.html).

Some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags cannot be applied during resource creation, the resource creation process fails. This ensures that resources you intended to tag on creation are either created with specified tags or not created at all. If you tag resources at the time of creation, you don't need to run custom tagging scripts after resource creation.

The following table describes the AWS WA Tool resources that can be tagged, and the resources that can be tagged on creation.


**Tagging support for AWS WA Tool resources**  

| Resource | Supports tags | Supports tag propagation | Supports tagging on creation (AWS WA Tool API, AWS CLI, AWS SDK) | 
| --- | --- | --- | --- | 
| AWS WA Tool workloads | Yes | No | Yes | 
| AWS WA Tool custom lenses | Yes | No | Yes | 
| AWS WA Tool profiles | Yes | No | Yes | 
| AWS WA Tool review templates | Yes | No | Yes | 

### Tag restrictions
<a name="tag-restrictions"></a>

The following basic restrictions apply to tags:
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple AWS services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are letters, numbers, spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Don't use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values, as it is reserved for AWS use. You can't edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags-per-resource limit.

### Working with tags using the console
<a name="tag-resources-console"></a>

Using the AWS WA Tool console, you can manage the tags associated with new or existing resources.

#### Adding tags on an individual resource on creation
<a name="adding-tags-creation"></a>

You can add tags to AWS WA Tool resources when you create them.

#### Adding and deleting tags on an individual resource
<a name="adding-or-deleting-tags"></a>

AWS WA Tool allows you to add or delete tags associated with your resources directly from the **Properties** tab for a workload, and from the **Overview** tab for custom lenses, profiles, and review templates. 

**To add or delete a tag on a workload**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. From the navigation bar, choose the Region to use.

1. In the navigation pane, choose **Workloads**.

1. Select the workload to modify and choose **Properties**.

1. In the **Tags** section, choose **Manage tags**.

1. Add or delete your tags as necessary.
   + To add a tag, choose **Add new tag** and fill in the **Key** and **Value** fields.
   + To delete a tag, choose **Remove**. 

1. Repeat this process for each tag you want to add, modify, or delete. Choose **Save** to save your changes.

**To add or delete a tag on a custom lens**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. From the navigation bar, choose the Region to use.

1. In the navigation pane, choose **Custom lenses**.

1. Select the name of the custom lens to modify.

1. In the **Tags** section of the **Overview** tab, choose **Manage tags**.

1. Add or delete your tags as necessary.
   + To add a tag, choose **Add new tag** and fill in the **Key** and **Value** fields.
   + To delete a tag, choose **Remove**. 

1. Repeat this process for each tag you want to add, modify, or delete. Choose **Save** to save your changes.

**To add or delete a tag on a profile**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. From the navigation bar, choose the Region to use.

1. In the navigation pane, choose **Profiles**.

1. Select the name of the profile to modify.

1. In the **Tags** section of the **Overview** tab, choose **Manage tags**.

1. Add or delete your tags as necessary.
   + To add a tag, choose **Add new tag** and fill in the **Key** and **Value** fields.
   + To delete a tag, choose **Remove**. 

1. Repeat this process for each tag you want to add, modify, or delete. Choose **Save** to save your changes.

**To add or delete a tag on a review template**

1. Sign in to the AWS Management Console and open the AWS Well-Architected Tool console at [https://console.aws.amazon.com/wellarchitected/](https://console.aws.amazon.com/wellarchitected/).

1. From the navigation bar, choose the Region to use.

1. In the navigation pane, choose **Review templates**.

1. Select the name of the review template to modify.

1. In the **Tags** section of the **Overview** tab, choose **Manage tags**.

1. Add or delete your tags as necessary.
   + To add a tag, choose **Add new tag** and fill in the **Key** and **Value** fields.
   + To delete a tag, choose **Remove**. 

1. Repeat this process for each tag you want to add, modify, or delete. Choose **Save** to save your changes.

### Working with tags using the API
<a name="tag-resources-api-sdk"></a>

Use the following AWS WA Tool API operations to add, update, list, and delete the tags for your resources.


**Tagging support for AWS WA Tool resources**  

| Task | API action | 
| --- | --- | 
| Add or overwrite one or more tags. | [TagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TagResource.html) | 
| Delete one or more tags. | [UntagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UntagResource.html) | 
| List tags for a resource. | [ListTagsForResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTagsForResource.html) | 

Some resource-creating actions enable you to specify tags when you create the resource. The following actions support tagging on creation.


| Task | API action | 
| --- | --- | 
| Create a workload | [CreateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkload.html) | 
| Import a new lens | [ImportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImportLens.html) | 
| Create a profile | [CreateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfile.html) | 
| Create a review template | [CreateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateReviewTemplate.html) | 

## EventBridge
<a name="eventbridge"></a>

AWS Well-Architected Tool sends events to Amazon EventBridge when actions are taken on Well-Architected resources. You can use EventBridge and these events to write rules that take actions, such as notifying you, when a resource change occurs. For more information, see [What is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html) 

**Note**  
Events are delivered on a best-effort basis.

The following actions result in EventBridge events:
+ Workload-related
  + Creating or deleting a workload
  + Creating a milestone
  + Updating the properties of a workload
  + Sharing or unsharing a workload
  + Updating the status of a share invitation
  + Adding or removing tags
  + Updating an answer
  + Updating review notes
  + Adding or removing a lens from a workload
+ Lens-related
  + Importing or exporting a custom lens
  + Publishing a custom lens
  + Deleting a custom lens
  + Sharing or unsharing a custom lens
  + Updating the status of a share invitation
  + Adding or removing a lens from a workload

### Sample events from AWS WA Tool
<a name="sample-eventbridge-events"></a>

This section includes example events from AWS Well-Architected Tool.

**Updating an answer in a workload**

```
 {
   "version":"0",
   "id":"00de336a-83cc-b80b-f0e6-f44c88a96050",
   "detail-type":"AWS API Call via CloudTrail",
   "source":"aws.wellarchitected",
   "account":"123456789012",
   "time":"2022-02-17T08:01:25Z",
   "region":"us-west-2",
   "resources":[],
   "detail":{
      "eventVersion":"1.08",
      "userIdentity":{
         "type":"AssumedRole",
         "principalId":"AKIAI44QH8DHBEXAMPLE:sample-user",
         "arn":"arn:aws:sts::123456789012:assumed-role/Admin/example-user",
         "accountId":"123456789012",
         "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
         "sessionContext":{
            "sessionIssuer":{
               "type":"Role",
               "principalId":"AKIAI44QH8DHBEXAMPLE",
               "arn":"arn:aws:iam::123456789012:role/Admin",
               "accountId":"123456789012",
               "userName":"Admin"
            },
            "webIdFederationData":{},
            "attributes":{
               "creationDate":"2022-02-17T07:21:54Z",
               "mfaAuthenticated":"false"
            }
         }
      },
      "eventTime":"2022-02-17T08:01:25Z",
      "eventSource":"wellarchitected.amazonaws.com",
      "eventName":"UpdateAnswer",
      "awsRegion":"us-west-2",
      "sourceIPAddress":"10.246.162.39",
      "userAgent":"aws-internal/3 aws-sdk-java/1.12.127 Linux/5.4.156-94.273.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.312-b07 java/1.8.0_312 vendor/Oracle_Corporation cfg/retry-mode/standard",
      "requestParameters":{
         "Status":"Acknowledged",
         "SelectedChoices":"***",
         "ChoiceUpdates":"***",
         "QuestionId":"priorities",
         "WorkloadId":"ee73fda518f9bd4aa804c6252e4e37b0",
         "IsApplicable":true,
         "LensAlias":"wellarchitected",
         "Reason":"NONE",
         "Notes":"***"
      },
      "responseElements":{
         "Answer":"***",
         "LensAlias":"wellarchitected",
         "WorkloadId":"ee73fda518f9bd4aa804c6252e4e37b0"
      },
      "requestID":"7bae1153-26a8-4dc0-9307-68b17b107619",
      "eventID":"8339c258-4ddd-48aa-ab21-3f82ce9d79cd",
      "readOnly":false,
      "eventType":"AwsApiCall",
      "managementEvent":true,
      "recipientAccountId":"123456789012",
      "eventCategory":"Management"
   }
}
```

**Publishing a custom lens**

```
{
   "version":"0",
   "id":"4054a34b-60a9-53c1-3146-c1a384dba41b",
   "detail-type":"AWS API Call via CloudTrail",
   "source":"aws.wellarchitected",
   "account":"123456789012",
   "time":"2022-02-17T08:58:34Z",
   "region":"us-west-2",
   "resources":[],
   "detail":{
      "eventVersion":"1.08",
      "userIdentity":{
         "type":"AssumedRole",
         "principalId":"AKIAI44QH8DHBEXAMPLE:example-user",
         "arn":"arn:aws:sts::123456789012:assumed-role/Admin/example-user",
         "accountId":"123456789012",
         "accessKeyId":"AKIAIOSFODNN7EXAMPLE",
         "sessionContext":{
            "sessionIssuer":{
               "type":"Role",
               "principalId":"AKIAI44QH8DHBEXAMPLE",
               "arn":"arn:aws:iam::123456789012:role/Admin",
               "accountId":"123456789012",
               "userName":"Admin"
            },
            "webIdFederationData":{},
            "attributes":{
               "creationDate":"2022-02-17T07:21:54Z",
               "mfaAuthenticated":"false"
            }
         }
      },
      "eventTime":"2022-02-17T08:58:34Z",
      "eventSource":"wellarchitected.amazonaws.com",
      "eventName":"CreateLensVersion",
      "awsRegion":"us-west-2",
      "sourceIPAddress":"10.246.162.39",
      "userAgent":"aws-internal/3 aws-sdk-java/1.12.127 Linux/5.4.156-94.273.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.312-b07 java/1.8.0_312 vendor/Oracle_Corporation cfg/retry-mode/standard",
      "requestParameters":{
         "IsMajorVersion":true,
         "LensVersion":"***",
         "ClientRequestToken":"03f46163-e95c-4455-8479-266373aa09c7",
         "LensAlias":"***"
      },
      "responseElements":{
         "LensArn":"arn:aws:wellarchitected:us-west-2:123456789012:lens/6261deecb9def44f9aecc938ca25d94e",
         "LensVersion":"***"
      },
      "requestID":"167b7051-980d-42ee-9967-0b4b3163e948",
      "eventID":"c7ef2b47-419d-45b7-8982-fbade9b558c7",
      "readOnly":false,
      "eventType":"AwsApiCall",
      "managementEvent":true,
      "recipientAccountId":"123456789012",
      "eventCategory":"Management"
   }
}
```

# Security in AWS Well-Architected
<a name="wa-security"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data centers and network architectures that are built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+ **Security of the cloud**: AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to AWS Well-Architected, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud**: Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using AWS Well-Architected services. The following topics show you how to configure these services to meet your security and compliance objectives. You also learn how to use other AWS services that help you monitor and secure your resources.

The security information in this chapter applies to both the AWS Well-Architected Tool and AWS Well-Architected Agent. Where the access model differs between services, service-specific guidance is provided.

**Topics**
+ [Data handling and privacy](#agent-security-data-handling)
+ [Shared responsibility for AI-generated content](#agent-security-ai-responsibility)
+ [Data protection in AWS Well-Architected](#data-protection)
+ [Compliance validation for AWS Well-Architected](#wat-compliance)
+ [Incident response in AWS Well-Architected](#incident-response)
+ [Resilience in AWS Well-Architected](#disaster-recovery-resiliency)
+ [Infrastructure security in AWS Well-Architected](#infrastructure-security)
+ [Configuration and vulnerability analysis in AWS Well-Architected](#vulnerability-analysis)
+ [Identity and access management for AWS Well-Architected](#security-iam)
+ [Cross-service confused deputy prevention](#cross-service-confused-deputy-prevention)
+ [Logging AWS Well-Architected API calls with AWS CloudTrail](#logging-using-cloudtrail)

## Data handling and privacy
<a name="agent-security-data-handling"></a>

AWS WA Agent analyzes resource telemetry, usage patterns, and configuration data from your AWS environment. It does not access the contents of your data stores such as Amazon S3 objects or database records.

All permissions granted to AWS WA Agent through the managed policy use read-only actions (`Get*`, `List*`, `Describe*`). AWS WA Agent cannot create, modify, or delete resources in your accounts.

## Shared responsibility for AI-generated content
<a name="agent-security-ai-responsibility"></a>

AWS WA Agent does not execute AI-generated remediation steps on your behalf. AI-generated guided actions are provided for your review and validation. You are responsible for reviewing, testing, and executing these steps in your environment.

Remediation derived from AWS Trusted Advisor checks uses pre-built SSM Runbooks that are deterministic and tested. AWS WA Agent can trigger these on your behalf with your consent.

## Data protection in AWS Well-Architected
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Well-Architected. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Well-Architected or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

### Encryption at rest
<a name="data_protection-encryption-at-rest"></a>

All data stored by AWS Well-Architected is encrypted at rest.

### Encryption in transit
<a name="data_protection-encryption-in-transit"></a>

All data sent to and from AWS Well-Architected is encrypted in transit.

### How AWS uses your data
<a name="data_protection-how-aws-uses-data"></a>

The AWS Well-Architected team collects aggregated data from the AWS Well-Architected to provide and improve the AWS Well-Architected service for customers. Individual customer data may be shared with AWS account teams to support our customers’ efforts to improve their workloads and architecture. The AWS Well-Architected team can only access workload properties and selected choices for each question. AWS does not share any data from the AWS Well-Architected outside of AWS.

Workload properties that the AWS Well-Architected team has access to include:
+ Workload name
+ Review owner
+ Environment
+ Regions
+ Account IDs
+ Industry type

The AWS Well-Architected team does *not* have access to:
+ Workload description
+ Architecture design
+ Any notes that you entered

## Compliance validation for AWS Well-Architected
<a name="wat-compliance"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Incident response in AWS Well-Architected
<a name="incident-response"></a>

Incident response for AWS Well-Architected is an AWS responsibility. AWS has a formal, documented policy and program that governs incident response.

AWS operational issues with broad impact are posted on the [AWS Service Health Dashboard.](https://status.aws.amazon.com/)

Operational issues are also posted to individual accounts via the AWS Health Dashboard. For information on how to use the Health Dashboard, see the [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html).

## Resilience in AWS Well-Architected
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## Infrastructure security in AWS Well-Architected
<a name="infrastructure-security"></a>

As a managed service, AWS Well-Architected is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access AWS Well-Architected through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

## Configuration and vulnerability analysis in AWS Well-Architected
<a name="vulnerability-analysis"></a>

Configuration and IT controls are a shared responsibility between AWS and you, our customer. For more information, see the AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## Identity and access management for AWS Well-Architected
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS Well-Architected resources. IAM is an AWS service that you can use with no additional charge.

**Topics**
+ [Audience](#security_iam_audience)
+ [Authenticating with identities](#security_iam_authentication)
+ [Managing access using policies](#security_iam_access-manage)
+ [AWS Well-Architected Tool access model](#security_iam_service-with-iam)
+ [AWS Well-Architected Agent access model](#security-iam-agent)
+ [AWS Well-Architected identity-based policy examples](#security_iam_id-based-policy-examples)
+ [AWS managed policies for AWS Well-Architected](#security-iam-awsmanpol)
+ [Troubleshooting AWS Well-Architected identity and access](#security_iam_troubleshoot)

### Audience
<a name="security_iam_audience"></a>

How you use AWS Identity and Access Management (IAM) differs based on your role:
+ **Service user** - request permissions from your administrator if you cannot access features (see [Troubleshooting AWS Well-Architected identity and access](#security_iam_troubleshoot))
+ **Service administrator** - determine user access and submit permission requests (see [AWS Well-Architected Tool access model](#security_iam_service-with-iam))
+ **IAM administrator** - write policies to manage access (see [AWS Well-Architected identity-based policy examples](#security_iam_id-based-policy-examples))

### Authenticating with identities
<a name="security_iam_authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

#### AWS account root user
<a name="security_iam_authentication-rootuser"></a>

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

#### Federated identity
<a name="security_iam_authentication-federated"></a>

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A *federated identity* is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

#### IAM users and groups
<a name="security_iam_authentication-iamuser"></a>

An *[IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)* is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*.

An [*IAM group*](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html) in the *IAM User Guide*.

#### IAM roles
<a name="security_iam_authentication-iamrole"></a>

An *[IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)* is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

### Managing access using policies
<a name="security_iam_access-manage"></a>

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the *IAM User Guide*.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

#### Identity-based policies
<a name="security_iam_access-manage-id-based-policies"></a>

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

Identity-based policies can be *inline policies* (embedded directly into a single identity) or *managed policies* (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html) in the *IAM User Guide*.

#### Resource-based policies
<a name="security_iam_access-manage-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

#### Other policy types
<a name="security_iam_access-manage-other-policies"></a>

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:
+ **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
+ **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the *AWS Organizations User Guide*.
+ **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the *IAM User Guide*.

#### Multiple policy types
<a name="security_iam_access-manage-multiple-policies"></a>

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

### AWS Well-Architected Tool access model
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to AWS Well-Architected, learn what IAM features are available to use with AWS Well-Architected.


**IAM features you can use with AWS Well-Architected**  

| IAM feature | AWS Well-Architected support | 
| --- | --- | 
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes | 
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies) |  No  | 
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes | 
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes | 
| [Policy condition keys (service-specific)](#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes | 
| [ACLs](#security_iam_service-with-iam-acls) |  No  | 
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Yes | 
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes | 
| [Principal permissions](#security_iam_service-with-iam-principal-permissions) |  Yes | 
| [Service roles](#security_iam_service-with-iam-roles-service) |  No  | 
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  No  | 

To get a high-level view of how AWS Well-Architected and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### AWS Well-Architected identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

#### Resource-based policies within AWS Well-Architected
<a name="security_iam_service-with-iam-resource-based-policies"></a>

**Supports resource-based policies:** No 

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

#### Policy actions for AWS Well-Architected
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Well-Architected use the following prefix before the action: `wellarchitected:`. For example, to allow an entity to define a workload, an administrator must attach a policy that allows `wellarchitected:CreateWorkload` actions. Similarly, to prevent an entity from deleting workloads, an administrator can attach a policy that denies `wellarchitected:DeleteWorkload` actions. Policy statements must include either an `Action` or `NotAction` element. AWS Well-Architected defines its own set of actions that describe tasks that you can perform with this service.

To see a list of AWS Well-Architected actions, see [Actions Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions) in the *Service Authorization Reference*. 

#### Policy resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

To see a list of AWS Well-Architected resource types and their ARNs, see [Resources defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions).

The AWS WA Tool workload resource has the following ARN:

```
arn:${Partition}:wellarchitected:${Region}:${Account}:workload/${ResourceId} 
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

The ARN can be found on the **Workload properties** page for a workload. For example, to specify a specific workload:

```
"Resource": "arn:aws:wellarchitected:{{us-west-2}}:{{123456789012}}:workload/{{11112222333344445555666677778888}}" 
```

To specify all workloads that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:wellarchitected:{{us-west-2}}:{{123456789012}}:workload/*" 
```

Some AWS Well-Architected actions, such as those for creating and listing workloads, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To see a list of AWS Well-Architected resource types and their ARNs, see [Resources Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions).

#### Policy condition keys for AWS Well-Architected
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

AWS Well-Architected provides one service-specific condition key (`wellarchitected:JiraProjectKey`) and supports using some global condition keys. To see all AWS global condition keys, see [AWS Global Condition Context Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *Service Authorization Reference*.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

#### ACLs in AWS Well-Architected
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No 

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

#### Authorization based on AWS Well-Architected tags
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

#### Using temporary credentials with AWS Well-Architected
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

#### Cross-service principal permissions for AWS Well-Architected
<a name="security_iam_service-with-iam-principal-permissions"></a>

**Supports forward access sessions (FAS):** Yes

 Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

#### Service roles for AWS Well-Architected
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** No 

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

#### Service-linked roles for AWS Well-Architected
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** No 

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

For details about creating or managing service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). Find a service in the table that includes a `Yes` in the **Service-linked role** column. Choose the **Yes** link to view the service-linked role documentation for that service.

### AWS Well-Architected Agent access model
<a name="security-iam-agent"></a>

AWS Well-Architected Agent uses customer-managed IAM roles rather than service-linked roles. This design gives you full control over the permissions that AWS WA Agent has in your environment and supports the cross-account access patterns required for multi-account infrastructure analysis.

Three principals interact with AWS WA Agent through IAM:
+ **Admin users** create and manage profiles, define scope and goals, configure cross-account access, and provide additional customer context. Admin users need permissions for profile management actions such as `wellarchitected:CreateAgentProfile` and `wellarchitected:DeleteAgentProfile`.
+ **Regular users** access generated recommendations, update recommendation lifecycle (mark as complete or suppress), and provide feedback. Regular users need permissions for actions such as `wellarchitected:ListAgentRecommendations` and `wellarchitected:GetAgentRecommendation`.
+ **AWS WA Agent as an AWS service** accesses your AWS infrastructure (like accounts, resources, and applications) and understands context (like business goals) to generate recommendations. This access is implemented through a pass role mechanism where you create and manage your own IAM roles.
<a name="security-iam-agent-pass-role"></a>
**Execution roles**  
When you create a profile, you pass an execution role to AWS WA Agent. The execution role is an IAM role in the same AWS account as the profile. AWS WA Agent assumes this role to orchestrate resource discovery across your configured accounts. The execution role requires a trust policy allowing the `wellarchitected.amazonaws.com` service principal to assume it, and a permissions policy granting `sts:AssumeRole` on the access roles in your target accounts. AWS WA Agent performs a pass role check during profile creation to validate that the caller has permission to pass the specified role to the service.
<a name="security-iam-agent-cross-account"></a>
**Cross-account access**  
AWS WA Agent uses IAM role chaining to access resources across multiple accounts:

1. **Admin account (profile account):** Contains the AWS WA Agent profile and the execution role. AWS WA Agent assumes the execution role in this account.

1. **Target accounts:** Each target account contains an access role that the execution role can assume. The access role grants AWS WA Agent read-only permissions to discover and analyze resources.

1. **Role chain:** AWS WA Agent assumes the execution role, which then assumes the access role in each target account.

Each access role requires:
+ A trust policy allowing the execution role to assume it.
+ The `WellArchitectedAgentResourceScanning` managed policy attached (recommended), or a custom policy scoped to only the actions you want AWS WA Agent to perform.

Use the following trust policy template for your access roles:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{ProfileOwningAccountID}}:role/service-role/{{ExecutionRoleName}}"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Replace {{ProfileOwningAccountID}} with the AWS account ID where your AWS WA Agent profile is created, and {{ExecutionRoleName}} with the name of the execution role. When the AWS WA Agent console creates the execution role, it places it under the `service-role/` path. Confirm the exact ARN from your profile details page. Onboarding is opt-in per account. For details on setting up roles, see [Getting started with AWS Well-Architected Agent](#agent-getting-started).
<a name="security-iam-agent-confused-deputy"></a>
**Confused deputy prevention**  
AWS WA Agent uses the profile ARN as an external ID in the role assumption chain, preventing the execution role from being used outside the context of its configured profile. AWS WA Agent also performs a pass role check during profile creation to validate that the calling principal has permission to pass the execution role to the service.
<a name="security-iam-agent-revoke"></a>
**Revoking access**  
You retain full control over AWS WA Agent's access at all times. Remove the trust policy from an access role, delete an access role entirely, or revoke active sessions to terminate in-progress data collection. If AWS WA Agent encounters a permission denial during recommendation generation, the details appear in the generation records.
<a name="security-iam-agent-best-practices"></a>
**Best practices**  
Run AWS WA Agent profiles from a dedicated AWS account without production workloads. Use the execution role ARN (not the root principal) in access role trust policies. Monitor AWS CloudTrail for AWS WA Agent API activity. Periodically review access role permissions and remove accounts that no longer require analysis.

### AWS Well-Architected identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify AWS Well-Architected resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the AWS Well-Architected console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [AWS Well-Architected Tool examples](#security_iam_id-based-policy-examples-tool)
+ [AWS Well-Architected Agent examples](#security_iam_id-based-policy-examples-agent)

#### Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS Well-Architected resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

#### Using the AWS Well-Architected console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS Well-Architected console, you must have a minimum set of permissions. These permissions must allow you to list and view details about AWS Well-Architected resources in your AWS account, including workloads, lenses, and agent profiles. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

To ensure that those entities can still use the AWS Well-Architected console, also attach the following AWS managed policy to the entities:

```
WellArchitectedConsoleReadOnlyAccess
```

To allow the ability to create, change, and delete workloads and manage agent profiles, attach the following AWS managed policy to the entities:

```
WellArchitectedConsoleFullAccess
```

For more information, see [Adding Permissions to a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that you're trying to perform.

#### Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

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

#### AWS Well-Architected Tool examples
<a name="security_iam_id-based-policy-examples-tool"></a>

The following examples show policies for common access patterns in the AWS Well-Architected Tool.

##### Granting full access to workloads
<a name="security_iam_id-based-policy-examples-full-access"></a>

In this example, you want to grant a user in your AWS account full access to your workloads. Full access allows the user to perform all actions in AWS WA Tool. This access is required to define workloads, delete workloads, view workloads, and update workloads.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement" : [  
     {
     "Effect" : "Allow",
     "Action" : [
          "wellarchitected:*"
     ],
     "Resource": "*"
     }
   ]
}
```

------

##### Granting read-only access to workloads
<a name="security_iam_id-based-policy-examples-readonly-access"></a>

In this example, you want to grant a user in your AWS account read-only access to your workloads. Read-only access only allows the user to view workloads in AWS WA Tool.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement" : [  
     {
     "Effect" : "Allow",
     "Action" : [
          "wellarchitected:Get*",
          "wellarchitected:List*"
     ],
     "Resource": "*"
     }
   ]
}
```

------

##### Accessing one workload
<a name="security_iam_id-based-policy-examples-access-one-workload"></a>

In this example, you want to grant a user in your AWS account read-only access to one of your workloads, `99999999999955555555555566666666`, in the `us-west-2` Region. Your account ID is `777788889999`.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement" : [  
     {
     "Effect" : "Allow",
     "Action" : [
          "wellarchitected:Get*",
          "wellarchitected:List*"
     ],
     "Resource": "arn:aws:wellarchitected:us-west-2:777788889999:workload/999999999999555555555555666666666"
     }
   ]
}
```

------

##### Using a service-specific condition key for the AWS Well-Architected Tool Connector for Jira
<a name="security_iam_id-based-policy-examples-service-specific-condition-key"></a>

 This example demonstrates how to use the service-specific condition key `wellarchitected:JiraProjectKey` to control which Jira projects can be linked to workloads in your account. 

 The following describes relevant uses for the condition key: 
+  **`CreateWorkload:`** When you apply `wellarchitected:JiraProjectKey` to `CreateWorkload`, you can define which custom Jira projects can be linked to any workload created by the user. For example, if a user tries to create a new workload with project ABC, but the policy only specifies project PQR, the action is denied. 
+  **`UpdateWorkload:`** When you apply `wellarchitected:JiraProjectKey` to `UpdateWorkload`, you can define which custom Jira projects can be linked to this particular workload or any workload. For example, if a user tries to update an existing workload with project ABC, but the policy specifies project PQR, the action is denied. Additionally, if the user has a workload that is linked to project PQR and tries to update the workload to be linked to project ABC, the action is denied. 
+  **`UpdateGlobalSettings:`** When you apply `wellarchitected:JiraProjectKey` to `UpdateGlobalSettings`, you can define which custom Jira projects can be linked to the AWS account. The account-level setting protects workloads in your account that do not override account-level Jira settings. For example, if a user has access to `UpdateGlobalSettings`, they cannot link workloads in your account to any projects that are not specified in the policy. 

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
			"Action": [
				"wellarchitected:UpdateGlobalSettings",
				"wellarchitected:CreateWorkload"
			],
			"Resource": "*",
			"Condition": {
				"StringEqualsIfExists": {
					"wellarchitected:JiraProjectKey": ["ABC, PQR"]
				}
			}
		},
		{
			"Sid": "VisualEditor1",
			"Effect": "Allow",
			"Action": [
				"wellarchitected:UpdateWorkload"
			],
			"Resource": "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:{{workload/example-workload}}",
			"Condition": {
				"StringEqualsIfExists": {
					"wellarchitected:JiraProjectKey": ["ABC, PQR"]
				}
			}
		}
	]
}
```

------

#### AWS Well-Architected Agent examples
<a name="security_iam_id-based-policy-examples-agent"></a>

The following examples show policies for common access patterns in AWS Well-Architected Agent.

##### Allow AWS WA Agent profile administration
<a name="security_iam_id-based-policy-examples-agent-admin"></a>

This policy grants full administrative access to AWS WA Agent, including creating and managing profiles, goals, and application context. Attach this policy to users who set up and configure AWS WA Agent profiles for your organization.

This policy also grants `iam:PassRole` so the administrator can pass the execution role to AWS WA Agent during profile creation. The condition restricts `PassRole` to the Well-Architected Agent service principal.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AgentProfileManagement",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:CreateAgentProfile",
                "wellarchitected:UpdateAgentProfile",
                "wellarchitected:DeleteAgentProfile",
                "wellarchitected:GetAgentProfile",
                "wellarchitected:ListAgentProfiles"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AgentGoalManagement",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:CreateAgentGoal",
                "wellarchitected:UpdateAgentGoal",
                "wellarchitected:DeleteAgentGoal"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AgentContextManagement",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:CreateAgentContext",
                "wellarchitected:UpdateAgentContext",
                "wellarchitected:DeleteAgentContext"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AgentRecommendationGeneration",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:StartAgentRecommendationGeneration",
                "wellarchitected:GetAgentRecommendationGeneration",
                "wellarchitected:ListAgentRecommendationGenerations"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PassExecutionRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::*:role/service-role/*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "wellarchitected-agent.amazonaws.com"
                }
            }
        }
    ]
}
```

##### Allow viewing and acting on AWS WA Agent recommendations
<a name="security_iam_id-based-policy-examples-agent-consumer"></a>

This policy grants access to view recommendations and update their status without allowing profile management. Attach this policy to users who triage and act on recommendations but do not configure AWS WA Agent profiles.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewRecommendations",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:ListAgentRecommendations",
                "wellarchitected:GetAgentRecommendation",
                "wellarchitected:ListAgentRecommendationItems"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ActOnRecommendations",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:UpdateAgentRecommendationStatus",
                "wellarchitected:PutAgentRecommendationFeedback"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ViewProfiles",
            "Effect": "Allow",
            "Action": [
                "wellarchitected:GetAgentProfile",
                "wellarchitected:ListAgentProfiles"
            ],
            "Resource": "*"
        }
    ]
}
```

### AWS managed policies for AWS Well-Architected
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

#### AWS managed policy: WellArchitectedConsoleFullAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleFullAccess"></a>

You can attach the `WellArchitectedConsoleFullAccess` policy to your IAM identities.

This policy grants full access to AWS Well-Architected, including the Well-Architected Tool for workload reviews and lens management, and AWS Well-Architected Agent for automated architecture analysis. Includes permissions for AWS Organizations delegated administrator management, AWS Trusted Advisor data access, service-linked role management for Well-Architected service principals, IAM role and policy creation scoped to `service-role/*` for console-guided execution role setup, and `iam:PassRole` conditioned to Well-Architected and Agent service principals. 

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleFullAccess.html) in the *AWS Managed Policy Reference*.

#### AWS managed policy: WellArchitectedConsoleReadOnlyAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess"></a>

You can attach the `WellArchitectedConsoleReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to AWS Well-Architected, including the Well-Architected Tool for viewing workloads and lenses, and AWS Well-Architected Agent for viewing architecture analysis results. Includes read-only permissions for AWS Organizations organization structure visibility and AWS Trusted Advisor data access. 

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

#### AWS managed policy: WellArchitectedAgentResourceScanning
<a name="security-iam-awsmanpol-WellArchitectedAgentResourceScanning"></a>

You can attach the `WellArchitectedAgentResourceScanning` policy to the access roles in your workload accounts that AWS Well-Architected Agent analyzes.

This policy grants AWS WA Agent read-only access to AWS resource configurations, security settings, and operational data across your accounts to generate optimization recommendations. The policy provides broad read-only access because AWS WA Agent must evaluate cross-service configurations holistically. All actions are read-only (`Get*`, `Describe*`, `List*`, `BatchGet*`). No create, update, delete, or invoke actions are included.

For more details about this policy, including the full JSON policy document, see [WellArchitectedAgentResourceScanning](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) in the *AWS Managed Policy Reference*.

#### AWS managed policy: AWSWellArchitectedOrganizationsServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedOrganizationsServiceRolePolicy"></a>

You can attach the `AWSWellArchitectedOrganizationsServiceRolePolicy` policy to your IAM identities.

This policy grants administrative permissions in AWS Organizations that are required to support AWS Well-Architected Tool integration with Organizations. These permissions allow the organization management account to enable resource sharing with AWS WA Tool. 

**Permissions details**

This policy includes the following permissions.
+ `organizations:ListAWSServiceAccessForOrganization` – Allows principals to check if the AWS service access is enabled for AWS WA Tool. 
+ `organizations:DescribeAccount` – Allows principals to retrieve information about an account in the organization.
+ `organizations:DescribeOrganization` – Allows principals to retrieve information about the organization configuration.
+ `organizations:ListAccounts` – Allows principals to retrieve the list of accounts that belong to an organization.
+ `organizations:ListAccountsForParent` – Allows principals to retrieve the list of accounts that belong to an organization from a given root node in the organization.
+ `organizations:ListChildren` – Allows principals to retrieve the list of accounts and organization units that belong to an organization from a given root node in the organization.
+ `organizations:ListParents` – Allows principals to retrieve the list of immediate parents specified by the OU or account within an organization.
+ `organizations:ListRoots` – Allows principals to retrieve the list of all root nodes within an organization.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedOrganizationsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedOrganizationsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

#### AWS managed policy: AWSWellArchitectedDiscoveryServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedDiscoveryServiceRolePolicy"></a>

You can attach the `AWSWellArchitectedDiscoveryServiceRolePolicy` policy to your IAM identities.

This policy allows AWS Well-Architected Tool to access AWS services and resources that relate to AWS WA Tool resources. 

**Permissions details**

This policy includes the following permissions.
+ `trustedadvisor:DescribeChecks` – Lists Trusted Advisor checks available. 
+ `trustedadvisor:DescribeCheckItems` – Fetches Trusted Advisor check data, including status and resources flagged by Trusted Advisor.
+ `servicecatalog:GetApplication` – Fetches details of an AppRegistry application.
+ `servicecatalog:ListAssociatedResources` –Lists resources associated with an AppRegistry application. 
+ `cloudformation:DescribeStacks` –Gets details of CloudFormation stacks.
+ `cloudformation:ListStackResources` –Lists resources associated with the CloudFormation stacks. 
+ `resource-groups:ListGroupResources` –Lists resources from a ResourceGroup. 
+ `tag:GetResources` – Required for ListGroupResources.
+ `servicecatalog:CreateAttributeGroup` – Creates a service-managed attribute group when required.
+ `servicecatalog:AssociateAttributeGroup` – Associates a service-managed attribute group with an AppRegistry application.
+ `servicecatalog:UpdateAttributeGroup` – Updates a service-managed attribute group.
+ `servicecatalog:DisassociateAttributeGroup` –Disassociates a service-managed attribute group from an AppRegistry application.
+ `servicecatalog:DeleteAttributeGroup` – Deletes a service-managed attribute group when required.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedDiscoveryServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedDiscoveryServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

#### AWS Well-Architected policy updates
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Well-Architected since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed in [Release notes](#release-notes).


| Change | Description | Date | 
| --- | --- | --- | 
| [WellArchitectedAgentResourceScanning](#security-iam-awsmanpol-WellArchitectedAgentResourceScanning) – New policy | AWS Well-Architected Agent added a new managed policy for resource scanning access roles. This policy grants read-only access to resource configurations across your AWS accounts for optimization recommendation generation. | July 17, 2025 | 
| [WellArchitectedConsoleFullAccess](#security-iam-awsmanpol-WellArchitectedConsoleFullAccess) – Updated policy | Updated to include permissions for AWS Well-Architected Agent, including AWS Organizations delegated administrator management, IAM role and policy creation for execution role setup, and `iam:PassRole` for Well-Architected and Agent service principals. | July 17, 2025 | 
| [WellArchitectedConsoleReadOnlyAccess](#security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess) – Updated policy | Updated to include read-only permissions for AWS Well-Architected Agent, including AWS Organizations organization visibility and AWS Trusted Advisor read access. | July 17, 2025 | 
| AWS Well-Architected started tracking policy changes | AWS Well-Architected started tracking changes for its AWS managed policies. | July 17, 2025 | 
| AWS WA Tool changed managed policy | Added `"wellarchitected:Export*"` to ` WellArchitectedConsoleReadOnlyAccess`. | June 22, 2023 | 
| AWS WA Tool added service role policy | Added `AWSWellArchitectedDiscoveryServiceRolePolicy` to allow AWS Well-Architected Tool to access AWS services and resources that relate to AWS WA Tool resources. | May 3, 2023 | 
| AWS WA Tool added permissions | Added a new action to grant `ListAWSServiceAccessForOrganization` to allow AWS WA Tool to check if the AWS service access is enabled for AWS WA Tool. | July 22, 2022 | 
| AWS WA Tool started tracking changes | AWS WA Tool started tracking changes for its AWS managed policies. | July 22, 2022 | 

### Troubleshooting AWS Well-Architected identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Well-Architected and IAM.

**Topics**
+ [I'm not authorized to perform an action in AWS Well-Architected](#security_iam_troubleshoot-no-permissions)

#### I'm not authorized to perform an action in AWS Well-Architected
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your sign-in credentials.

The following example error occurs when the {{mateojackson}} user tries to use the console to perform the `DeleteWorkload` action, but does not have permissions.

```
User: arn:aws:iam::{{123456789012}}:user/{{mateojackson}} is not authorized to perform: {{wellarchitected:DeleteWorkload}} on resource: {{11112222333344445555666677778888}}
```

For this example, ask your administrator to update your policies to allow you to access the `11112222333344445555666677778888` resource using the `wellarchitected:DeleteWorkload` action.

## Cross-service confused deputy prevention
<a name="cross-service-confused-deputy-prevention"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account. 

We recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource policies to limit the permissions that AWS Well-Architected gives another service to the resource. Use `aws:SourceArn` if you want only one resource to be associated with the cross-service access. Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

The most effective way to protect against the confused deputy problem is to use the `aws:SourceArn` global condition context key with the full ARN of the resource. If you don't know the full ARN of the resource or if you are specifying multiple resources, use the `aws:SourceArn` global context condition key with wildcard characters (`*`) for the unknown portions of the ARN. For example, `arn:aws:wellarchitected:*:{{123456789012}}:*`. 

If the `aws:SourceArn` value does not contain the account ID, such as an Amazon S3 bucket ARN, you must use both global condition context keys to limit permissions. 

The value of `aws:SourceArn` must be a workload or lens.

The following example shows how you can use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in AWS Well-Architected to prevent the confused deputy problem.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": {
    "Sid": "ConfusedDeputyPreventionExamplePolicy",
    "Effect": "Allow",
    "Principal": {
      "Service": "wellarchitected.amazonaws.com"
    },
    "Action": "wellarchitected:{{CreateWorkload}}",
    "Resource": [
    "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:{{ResourceName}}/*"
    ],
    "Condition": {
      "ArnLike": {
        "aws:SourceArn": "arn:aws:wellarchitected:*:{{123456789012}}:*"
      },
      "StringEquals": {
        "aws:SourceAccount": "{{123456789012}}"
      }
    }
  }
}
```

------

## Logging AWS Well-Architected API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS Well-Architected is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Well-Architected. CloudTrail captures all API calls for AWS Well-Architected as events. The calls captured include calls from the AWS Well-Architected console and code calls to the AWS Well-Architected API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Well-Architected. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Well-Architected, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

### AWS Well-Architected information in CloudTrail
<a name="wat-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Well-Architected, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for AWS Well-Architected, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS Well-Architected actions are logged by CloudTrail and are documented in [Actions Defined by AWS Well-Architected](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awswell-architectedtool.html#awswell-architectedtool-actions-as-permissions). For example, calls to the `CreateWorkload`, `DeleteWorkload`, and `CreateWorkloadShare` actions generate entries in the CloudTrail log files. 

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with user or root user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

### Understanding AWS Well-Architected log file entries
<a name="understanding-wat-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `CreateWorkload` action.

```
   {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:dev-dsk-xiulan-2a-1111111c.us-west-2.amazon.com",
        "arn": "arn:aws:sts::444455556666:assumed-role/well-architected-api-svc-integ-test-read-write/dev-dsk-xiulan-2a-1111111c.us-west-2.amazon.com",
        "accountId": "444455556666",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::444455556666:role/well-architected-api-svc-integ-test-read-write",
                "accountId": "444455556666",
                "userName": "well-architected-api-svc-integ-test-read-write"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-10-14T03:41:39Z"
            }
        }
    },
    "eventTime": "2020-10-14T04:43:13Z",
    "eventSource": "wellarchitected.amazonaws.com",
    "eventName": "CreateWorkload",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "198.51.100.178",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.848 Linux/4.9.217-0.1.ac.205.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation",
    "requestParameters": {
           "ClientRequestToken": "08af866a-0238-4070-89c2-b689ca8339f7",
           "Description": "***",
           "AwsRegions": [
               "us-west-2"
           ],
           "ReviewOwner": "***",
           "Environment": "PRODUCTION",
           "Name": "***",
           "Lenses": [
               "wellarchitected",
               "serverless"
           ]
    },
    "responseElements": {
         "Arn": "arn:aws:wellarchitected:us-west-2:444455556666:workload/8cdcdf7add10b181fdd3f686dacffdac",
         "Id": "8cdcdf7add10b181fdd3f686dacffdac"
    },
    "requestID": "22bad4e3-aa51-4ff1-b480-712ee07cedbd",
    "eventID": "50849dfd-36ed-418e-a901-49f6ac7087e8",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "444455556666"
}
```

# API actions
<a name="wa-api-actions"></a>

The following API actions are available for AWS Well-Architected services. All actions use the `wellarchitected` service namespace. For complete API reference documentation, see the [AWS Well-Architected API Reference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/Welcome.html).

## AWS Well-Architected Agent actions
<a name="agent-api-agent-actions"></a>

The following actions are for AWS Well-Architected Agent.

### Profiles
<a name="agent-api-profiles"></a>
+ [CreateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentProfile.html)
+ [DeleteAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentProfile.html)
+ [GetAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentProfile.html)
+ [ListAgentProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentProfiles.html)
+ [UpdateAgentProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentProfile.html)

### Goals
<a name="agent-api-goals"></a>
+ [CreateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentGoal.html)
+ [DeleteAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentGoal.html)
+ [GetAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentGoal.html)
+ [ListAgentGoals](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentGoals.html)
+ [UpdateAgentGoal](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentGoal.html)

### Application context
<a name="agent-api-context"></a>
+ [CreateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateAgentContext.html)
+ [DeleteAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteAgentContext.html)
+ [GetAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentContext.html)
+ [ListAgentContexts](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentContexts.html)
+ [UpdateAgentContext](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentContext.html)

### Recommendations
<a name="agent-api-recommendations"></a>
+ [GetAgentRecommendation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendation.html)
+ [ListAgentRecommendations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendations.html)
+ [ListAgentRecommendationItems](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationItems.html)
+ [UpdateAgentRecommendationStatus](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAgentRecommendationStatus.html)
+ [PutAgentRecommendationFeedback](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_PutAgentRecommendationFeedback.html)

### Recommendation generation
<a name="agent-api-recommendation-generation"></a>
+ [StartAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_StartAgentRecommendationGeneration.html)
+ [GetAgentRecommendationGeneration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAgentRecommendationGeneration.html)
+ [ListAgentRecommendationGenerations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentRecommendationGenerations.html)

## AWS Well-Architected Tool actions
<a name="agent-api-tool-actions"></a>

The following actions are for the AWS Well-Architected Tool.

### Workloads
<a name="wa-tool-api-workloads"></a>
+ [CreateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkload.html)
+ [DeleteWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkload.html)
+ [GetWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetWorkload.html)
+ [ListWorkloads](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloads.html)
+ [UpdateWorkload](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkload.html)

### Workload sharing
<a name="wa-tool-api-workload-sharing"></a>
+ [CreateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkloadShare.html)
+ [DeleteWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteWorkloadShare.html)
+ [ListWorkloadShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListWorkloadShares.html)
+ [UpdateWorkloadShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkloadShare.html)
+ [ListShareInvitations](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListShareInvitations.html)
+ [UpdateShareInvitation](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateShareInvitation.html)

### Lenses
<a name="wa-tool-api-lenses"></a>
+ [AssociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateLenses.html)
+ [CreateLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensShare.html)
+ [CreateLensVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateLensVersion.html)
+ [DeleteLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLens.html)
+ [DeleteLensShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteLensShare.html)
+ [DisassociateLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateLenses.html)
+ [ExportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ExportLens.html)
+ [GetLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLens.html)
+ [GetLensVersionDifference](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensVersionDifference.html)
+ [ImportLens](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ImportLens.html)
+ [ListLenses](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLenses.html)
+ [ListLensShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensShares.html)
+ [UpgradeLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeLensReview.html)

### Lens reviews
<a name="wa-tool-api-lens-reviews"></a>
+ [GetAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetAnswer.html)
+ [GetLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReview.html)
+ [GetLensReviewReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetLensReviewReport.html)
+ [ListAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAnswers.html)
+ [ListLensReviewImprovements](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviewImprovements.html)
+ [ListLensReviews](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListLensReviews.html)
+ [UpdateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateAnswer.html)
+ [UpdateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateLensReview.html)

### Milestones
<a name="wa-tool-api-milestones"></a>
+ [CreateMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateMilestone.html)
+ [GetMilestone](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetMilestone.html)
+ [ListMilestones](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListMilestones.html)

### Profiles
<a name="wa-tool-api-profiles"></a>
+ [AssociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AssociateProfiles.html)
+ [CreateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfile.html)
+ [CreateProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfileShare.html)
+ [DeleteProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfile.html)
+ [DeleteProfileShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteProfileShare.html)
+ [DisassociateProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DisassociateProfiles.html)
+ [GetProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfile.html)
+ [GetProfileTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetProfileTemplate.html)
+ [ListProfileNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileNotifications.html)
+ [ListProfiles](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfiles.html)
+ [ListProfileShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileShares.html)
+ [UpdateProfile](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateProfile.html)
+ [UpgradeProfileVersion](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeProfileVersion.html)

### Review templates
<a name="wa-tool-api-review-templates"></a>
+ [CreateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateReviewTemplate.html)
+ [CreateTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateTemplateShare.html)
+ [DeleteReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteReviewTemplate.html)
+ [DeleteTemplateShare](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_DeleteTemplateShare.html)
+ [GetReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplate.html)
+ [GetReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateAnswer.html)
+ [GetReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetReviewTemplateLensReview.html)
+ [ListReviewTemplateAnswers](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplateAnswers.html)
+ [ListReviewTemplates](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListReviewTemplates.html)
+ [ListTemplateShares](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTemplateShares.html)
+ [UpdateReviewTemplate](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplate.html)
+ [UpdateReviewTemplateAnswer](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateAnswer.html)
+ [UpdateReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateReviewTemplateLensReview.html)
+ [UpgradeReviewTemplateLensReview](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpgradeReviewTemplateLensReview.html)

### AWS Trusted Advisor checks
<a name="wa-tool-api-checks"></a>
+ [ListCheckDetails](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckDetails.html)
+ [ListCheckSummaries](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListCheckSummaries.html)

### Notifications and settings
<a name="wa-tool-api-notifications-settings"></a>
+ [GetConsolidatedReport](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetConsolidatedReport.html)
+ [GetGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetGlobalSettings.html)
+ [ListNotifications](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListNotifications.html)
+ [UpdateGlobalSettings](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateGlobalSettings.html)
+ [UpdateIntegration](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateIntegration.html)

### Tagging
<a name="wa-tool-api-tagging"></a>
+ [ListTagsForResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UntagResource.html)

# Release notes
<a name="release-notes"></a>

This page describes changes to the AWS Well-Architected user guide. For notification about updates to this documentation, you can subscribe to the RSS feed.

## AWS Well-Architected Agent released (10-1-2026)
<a name="update-2026-10-01"></a>

### AWS Well-Architected Agent (preview)
<a name="release-notes-waa-preview"></a>

AWS Well-Architected Agent is an AI-powered cloud optimization service that continuously analyzes your AWS environment and delivers personalized, prioritized recommendations across cost, security, performance, and resilience. The agent generates recommendations at three levels (resource, application, and architecture) with ready-to-deploy SSM runbooks so you can act immediately.

Key capabilities added with this release:
+ **Automated, ongoing analysis:** Unlike point-in-time architecture reviews, AWS WA Agent analyzes your environment on a weekly cadence and refreshes recommendations automatically.
+ **Ready-to-deploy remediation:** Recommendations include AI-generated SSM runbooks, not only findings.
+ **Goal-aligned prioritization:** Recommendations are ranked against the business goals you define in your agent profile.
+ **Cross-pillar impact and trade-off analysis:** Every recommendation shows positive impacts on other pillars, as well as trade-offs with risk level and mitigation strategies.
+ **IaC architecture reviews:** On-demand architecture reviews of CloudFormation and Terraform templates, returning findings aligned to AWS Well-Architected best practices.
+ **Multi-account scale:** A single agent profile can analyze multiple AWS accounts and scan resources across multiple AWS Regions.

AWS WA Agent is available to customers with a Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations support plan. Agent profiles are hosted in US East (N. Virginia), US East (Ohio), or US West (Oregon), and scan resources across all commercial AWS Regions.

For more information, see [What is AWS Well-Architected Agent (preview)?](#agent).

## Historic AWS Well-Architected releases
<a name="release-notes-historic"></a>

The following table describes earlier updates to this guide.


| Change | Description | Date | 
| --- | --- | --- | 
| Added Well-Architected Framework Review (WAFR) section | Added a new section with guidance on performing a WAFR using the AWS Well-Architected Tool. | October 13, 2025 | 
| New lens | This release added one new lens to the Lens Catalog. | April 17, 2025 | 
| New and updated lenses | This release added one new lens to the Lens Catalog and updated one other lens. | June 27, 2024 | 
| Jira | This release added the AWS Well-Architected Tool Connector for Jira. | April 16, 2024 | 
| New lenses | This release added new lenses to the Lens Catalog. | March 26, 2024 | 
| Updated functionality | This release adds the Lens Catalog feature to AWS WA Tool. | November 26, 2023 | 
| Updated functionality | This release adds the Review Templates feature to AWS WA Tool. | October 3, 2023 | 
| Updated functionality | This release adds the Profiles feature to AWS WA Tool. | June 13, 2023 | 
| Updated functionality | This release enhances the AWS Trusted Advisor and AWS Service Catalog AppRegistry integration, and adds the `AWSWellArchitectedDiscoveryServiceRolePolicy` to AWS managed policies. | May 3, 2023 | 
| Content update | Corrected name of WellArchitectedConsoleReadOnlyAccess policy. | January 19, 2023 | 
| Updated functionality | This release removes the FTR lens from the tool. | December 14, 2022 | 
| Updated functionality | This release adds the AWS Trusted Advisor and AWS Service Catalog AppRegistry integration. | November 7, 2022 | 
| Content update | Corrected a problem in the custom lens JSON example for `choices`. | September 29, 2022 | 
| Content update | The `choices` section of the custom lens JSON specification was updated. | August 2, 2022 | 
| Updated functionality | This release adds the ability to specify additional resources for choices in a custom lens, to preview a custom lens before publishing it, and add tags to custom lenses. | June 21, 2022 | 
| Updated functionality | This release adds the ability to access the AWS Well-Architected community on AWS re:Post. | May 31, 2022 | 
| Updated functionality | This release adds the sustainability pillar and minor updates to Tutorial. | March 31, 2022 | 
| Updated functionality | Individual best practices can now be marked as not applicable. | July 14, 2021 | 
| Updated functionality | This release adds the FTR and SaaS lenses to the tool. | December 3, 2020 | 
| Content update | Clarified that after you upgrade a workload to use a new lens that you cannot go back to the previous version. | July 8, 2020 | 
| Content update | Clarified sharing in AWS Regions introduced after March 20, 2019. | June 24, 2020 | 
| Updated functionality | Access to a workload share is removed immediately when a workload share invitation is rejected. Shared access is granted when the share is accepted. | June 17, 2020 | 
| Updated functionality | This release adds a review owner to the workload. | April 1, 2020 | 
| Updated functionality | This release adds an architectural diagram link to the workload. | March 10, 2020 | 
| Content update | Clarified that workload shares are AWS Region-specific. | January 10, 2020 | 
| Updated functionality | This release adds workload sharing. | January 9, 2020 | 
| Content update | Security section updated with latest guidance. | December 6, 2019 | 
| Updated functionality | This release makes the industry fields optional when defining a workload. | August 19, 2019 | 
| Updated functionality | This release adds improvement plan items to the workload report. | July 29, 2019 | 
| Updated functionality | The release adds the DeleteWorkload action to the policy. | July 18, 2019 | 
| Content update | The content in this guide has been updated with minor fixes. | June 19, 2019 | 
| Content update | The content in this guide has been updated with minor fixes. | May 30, 2019 | 
| Updated functionality | This release supports upgrading the version of the framework used for a workload review. | May 1, 2019 | 
| Updated functionality | This release adds the ability to specify non-AWS Regions when defining a workload. | February 14, 2019 | 
| AWS Well-Architected Tool general availability | This release introduces the AWS Well-Architected Tool. | November 29, 2018 | 

# AWS Glossary
<a name="glossary"></a>

For the latest AWS terminology, see the [AWS glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary Reference*.